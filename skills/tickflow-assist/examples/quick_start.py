#!/usr/bin/env python3
"""
TickFlow Quick Start Example
快速开始示例 - 演示如何获取股票行情和 K 线数据
"""

from tickflow import TickFlow

def main():
    # 方法 1: 免费服务（仅需历史数据时使用）
    print("=== 免费服务示例 ===")
    tf_free = TickFlow.free()
    
    # 获取历史日 K 线（最近 100 天）
    df = tf_free.klines.get("600000.SH", period="1d", count=100, as_dataframe=True)
    print(f"\n浦发银行 (600000.SH) 最近 5 个交易日:")
    print(df.tail())
    
    # 方法 2: 完整服务（需要 API Key，支持实时行情）
    print("\n=== 完整服务示例 ===")
    tf = TickFlow()
    
    # 获取实时行情（支持多市场混合查询）
    symbols = ["600000.SH", "000001.SZ", "AAPL.US", "00700.HK"]
    try:
        quotes = tf.quotes.get(symbols=symbols)
        print("\n实时行情:")
        for q in quotes:
            change_pct = q['ext']['change_pct'] * 100
            print(f"{q['ext']['name']} ({q['symbol']}): {q['last_price']} ({change_pct:+.2f}%)")
    except Exception as e:
        print(f"获取实时行情失败（可能需要配置 API Key）: {e}")
    
    # 查询标的信息
    print("\n=== 标的信息 ===")
    instruments = tf.instruments.get(symbols=["600000.SH", "000001.SZ", "600519.SH"])
    for inst in instruments:
        print(f"{inst.symbol}: {inst.name}")

if __name__ == "__main__":
    main()
