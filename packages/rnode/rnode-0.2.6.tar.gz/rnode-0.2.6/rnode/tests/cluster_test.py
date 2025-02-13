import sys
import time

from rnode import init_resample_kline_cluster


def cluster_callback(data: str):
    """处理集群K线数据的回调"""
    print(f"\nReceived cluster data: {data}")


def main():

    # WebSocket 连接配置
    ws_url = "ws://43.207.106.154:5002/ws/dms"
    
    # 要订阅的交易对列表
    instrument_ids = [
        "EXCHANGE_BINANCE.BTC-USDT.SECURITY_TYPE_PERP.CONTRACT_TYPE_LINEAR.USDT.UNSPECIFIED",
        "EXCHANGE_BINANCE.ETH-USDT.SECURITY_TYPE_PERP.CONTRACT_TYPE_LINEAR.USDT.UNSPECIFIED",
        "EXCHANGE_BINANCE.SOL-USDT.SECURITY_TYPE_PERP.CONTRACT_TYPE_LINEAR.USDT.UNSPECIFIED",
    ]
    
    # 设置数据频率
    freq = "10s"

    try:
        # 初始化 resample kline cluster
        init_resample_kline_cluster(
            ws_url,
            instrument_ids,
            freq,
            cluster_callback,
        )

        print(f"Started resample kline cluster for {len(instrument_ids)} instruments")
        print("Waiting for data...")

        # 保持程序运行
        while True:
            time.sleep(1)
            print(".", end="", flush=True)

    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 