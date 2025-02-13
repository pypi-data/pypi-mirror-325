use std::collections::{HashMap, VecDeque};
use std::sync::Arc;
use tokio::sync::{RwLock, Mutex};
use pyo3::prelude::*;
use tracing::error;
use crate::types::*;
use crate::error::*;
use crate::ws_client::WsClient;
use super::resample_kline::{ResampleKlineNode, ResampleKlineData};

pub struct ResampleKlineCluster {
    nodes: HashMap<String, Arc<ResampleKlineNode>>,
    period_queue: Arc<RwLock<VecDeque<i64>>>,
    period_data: Arc<RwLock<HashMap<i64, HashMap<String, ResampleKlineData>>>>,
    freq: String,
    ws_client: Arc<WsClient>,
    sending_lock: Arc<Mutex<()>>,
}

impl ResampleKlineCluster {
    pub fn new(
        freq: String,
        nodes: HashMap<String, Arc<ResampleKlineNode>>,
        ws_client: Arc<WsClient>,
    ) -> Self {
        Self {
            nodes,
            period_queue: Arc::new(RwLock::new(VecDeque::new())),
            period_data: Arc::new(RwLock::new(HashMap::new())),
            freq,
            ws_client,
            sending_lock: Arc::new(Mutex::new(())),
        }
    }

    pub async fn start(&self, callback: PyObject) -> Result<()> {
        // 为每个节点设置数据接收处理
        for (instrument_id, node) in &self.nodes {
            let period_queue = self.period_queue.clone();
            let period_data = self.period_data.clone();
            let instrument_id = instrument_id.clone();
            let callback = callback.clone();
            let sending_lock = self.sending_lock.clone();
            let total_instruments = self.nodes.len();
            let freq = self.freq.clone();
            let ws_client = self.ws_client.clone();

            let mut receiver = node.subscribe();
            
            tokio::spawn(async move {
                while let Ok(data) = receiver.recv().await {
                    let period_id = data.period_id;
                    
                    // 更新 period 数据
                    {
                        let mut period_data = period_data.write().await;
                        let period_map = period_data.entry(period_id).or_insert_with(HashMap::new);
                        period_map.insert(instrument_id.clone(), data.clone());

                        // 检查是否所有 instrument 的数据都已收集
                        if period_map.len() == total_instruments {
                            // 添加到队列
                            let mut queue = period_queue.write().await;
                            if !queue.contains(&period_id) {
                                queue.push_back(period_id);
                            }
                        }
                    }

                    // 发送数据
                    let _lock = sending_lock.lock().await;
                    let mut queue = period_queue.write().await;
                    let period_data = period_data.read().await;

                    while let Some(pid) = queue.front() {
                        if let Some(data_map) = period_data.get(pid) {
                            if data_map.len() == total_instruments {
                                // 构建响应数据
                                ws_client.update_time().await;
                                let current_time = ws_client.get_current_time().await;
                                let response = serde_json::json!({
                                    "type": "resample_kline_cluster",
                                    "freq": freq,
                                    "period_id": pid,
                                    "timestamp": current_time,
                                    "status": DataStatus::BasicValid,
                                    "data": serde_json::to_value(data_map).unwrap_or_default(),
                                });

                                // 发送数据
                                Python::with_gil(|py| {
                                    if let Err(e) = callback.call1(py, (response.to_string(),)) {
                                        error!("Failed to call Python callback: {:?}", e);
                                    }
                                });

                                queue.pop_front();
                            } else {
                                break;
                            }
                        }
                    }
                }
            });
        }

        Ok(())
    }
} 