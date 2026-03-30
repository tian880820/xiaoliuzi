---
name: stock-watcher
description: Stock watchlist management with real-time quotes from 同花顺 (10jqka.com.cn). Supports A-shares market.
metadata:
  {
    "openclaw":
      {
        "requires": { "bins": [] },
        "install": [],
      },
  }
---

# Stock Watcher Skill

This skill provides comprehensive stock watchlist management capabilities, allowing users to track their favorite stocks and get performance summaries using real-time data from 同花顺 (10jqka.com.cn).

## 自选股行情查看

当你要求查看自选股行情时，系统会直接显示以下信息：

- 每只股票的代码和名称
- 近期表现指标（涨跌幅等关键数据）
- 详细信息链接（可点击查看）

无需额外命令，直接为你呈现简洁明了的行情概览。

## 管理自选股

### 添加股票

使用股票代码（6 位数字）添加到自选股：

- 例如：添加 600053 九鼎投资

### 删除股票

通过股票代码删除自选股：

- 例如：删除 600053

### 查看自选股列表

显示当前所有自选股的完整列表

### 清空自选股列表

完全清空所有自选股

## 数据来源

主要使用同花顺 (10jqka.com.cn) 作为数据源：

- 股票页面：https://stockpage.10jqka.com.cn/{stock_code}/
- 支持沪深 A 股及科创板市场
- 提供实时行情、技术分析和资金流向数据

## 自选股管理

### 文件格式

自选股存储在 `~/.clawdbot/stock_watcher/watchlist.txt`：

```
600053|九鼎投资
600018|上港集团
688785|恒运昌
```

### 支持操作

- 添加股票：验证股票代码格式并添加到自选股
- 删除股票：按股票代码精确匹配删除
- 查看列表：显示当前自选股
- 清空列表：完全清空自选股
- 行情总结：获取所有股票的最新数据并提供简洁摘要

## 行情摘要特点

- 直接显示关键行情指标，无冗余信息
- 提供股票详情链接便于深入查看
- 自动处理网络错误和数据异常
- 合理控制请求频率（每秒 1 次）

## 注意事项

- 股票代码格式：使用 6 位数字代码（如 600053）
- 数据延迟：行情可能有 1-3 分钟延迟
- 网络依赖：需要网络连接获取实时数据
- 市场范围：主要支持 A 股市场（沪市/深市/科创板）

## 使用示例

```bash
# 添加股票
python3 {baseDir}/scripts/add_stock.py 600053 九鼎投资

# 删除股票
python3 {baseDir}/scripts/remove_stock.py 600053

# 查看列表
python3 {baseDir}/scripts/list_stocks.py

# 清空列表
python3 {baseDir}/scripts/clear_watchlist.py

# 行情总结
python3 {baseDir}/scripts/summarize_performance.py
```
