from tickflow import TickFlow
import json

tf = TickFlow()

# 获取实时行情
symbols = ["300750.SZ", "300502.SZ", "300290.SZ"]
quotes = tf.quotes.get(symbols=symbols)

# 获取昨日收盘价（用于计算涨跌幅对比）
klines = tf.klines.batch(symbols, period="1d", count=2, as_dataframe=True)

results = []
for q in quotes:
    symbol = q['symbol']
    name_map = {"300750.SZ": "宁德时代", "300502.SZ": "新易盛", "300290.SZ": "荣科科技"}
    name = name_map.get(symbol, symbol)
    
    current_price = q.get('last_price', 0)
    pre_close = q.get('pre_close', 0)
    change_pct = q.get('change_pct', 0)
    volume = q.get('volume', 0)
    turnover_rate = q.get('turnover_rate', 0)
    
    # 获取昨日收盘价
    df = klines.get(symbol)
    if df is not None and len(df) >= 2:
        yesterday_close = df.iloc[-2]['close']
    else:
        yesterday_close = pre_close
    
    results.append({
        "symbol": symbol,
        "name": name,
        "current_price": current_price,
        "pre_close": pre_close,
        "yesterday_close": yesterday_close,
        "change_pct": change_pct,
        "volume": volume,
        "turnover_rate": turnover_rate
    })

print(json.dumps(results, ensure_ascii=False, indent=2))
