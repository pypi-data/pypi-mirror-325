import json
import time

from rnode import init_resample_kline_node

instrument_ids = [
    "EXCHANGE_BINANCE.BTC-USDT.SECURITY_TYPE_PERP.CONTRACT_TYPE_LINEAR.USDT.UNSPECIFIED",
    "EXCHANGE_BINANCE.ETH-USDT.SECURITY_TYPE_PERP.CONTRACT_TYPE_LINEAR.USDT.UNSPECIFIED",
    "EXCHANGE_BINANCE.ADA-USDT.SECURITY_TYPE_PERP.CONTRACT_TYPE_LINEAR.USDT.UNSPECIFIED",
    "EXCHANGE_BINANCE.XRP-USDT.SECURITY_TYPE_PERP.CONTRACT_TYPE_LINEAR.USDT.UNSPECIFIED",
    "EXCHANGE_BINANCE.LINK-USDT.SECURITY_TYPE_PERP.CONTRACT_TYPE_LINEAR.USDT.UNSPECIFIED",
    "EXCHANGE_BINANCE.SOL-USDT.SECURITY_TYPE_PERP.CONTRACT_TYPE_LINEAR.USDT.UNSPECIFIED",
]


def resample_kline_callback(data: str):
    """处理K线数据的回调"""
    # print(f"\nReceived resample kline data: {data}")
    result = json.loads(data)
    instrument_id = result["instrument_id"]
    data = result["data"]
    open_time = data["open_time"]
    print(open_time, instrument_id)


def main():
    try:
        init_resample_kline_node(
            "ws://43.207.106.154:5002/ws/dms",
            instrument_ids,
            "5s",
            resample_kline_callback,
        )

        print("Services started. Waiting for data...")

        while True:
            time.sleep(1)
            print(".", end="", flush=True)

    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
