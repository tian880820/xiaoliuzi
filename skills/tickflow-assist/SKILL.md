---
name: tickflow-assist
description: 通过 TickFlow Python SDK 获取 A 股、港股、美股、期货等市场的实时行情、K 线数据。支持多市场、多周期，适用于量化交易、数据分析等场景。
metadata:
  {
    "openclaw":
      {
        "requires": { "bins": ["uv", "python3"] },
        "install": [],
      },
  }
---

# TickFlow Assist Skill

通过 TickFlow Python SDK 获取 A 股、港股、美股、期货等市场的实时行情、K 线数据。支持多市场、多周期，适用于量化交易、数据分析等场景。

## 环境配置

### 1. 安装 uv（如果未安装）

```bash
# 检查 uv 是否已安装
uv --version

# 如果未安装，运行官方安装脚本：
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 配置 TickFlow 工作环境

```bash
# 创建 python 工作目录
cd /home/admin/.openclaw/workspace/skills/tickflow-assist
mkdir -p python
cd python

# 创建 pyproject.toml 文件
cat > pyproject.toml << 'EOF'
[project]
name = "tickflow-workspace"
version = "0.1.0"
description = "TickFlow workspace for market data analysis"
requires-python = ">=3.10"
dependencies = [
 "tickflow[all]>=0.1.17",
]
EOF

# 使用 uv 同步依赖
uv sync
```

### 3. 配置 API Key

访问 [tickflow.org](https://tickflow.org) 获取 API Key，然后配置环境变量：

```bash
# macOS/Linux
export TICKFLOW_API_KEY="your-api-key"

# 建议添加到 shell 配置文件
echo 'export TICKFLOW_API_KEY="your-api-key"' >> ~/.bashrc
source ~/.bashrc
```

## 标的代码格式

所有查询使用统一格式：**代码。市场后缀**（例如：600000.SH）

### 常用市场后缀

| 后缀 | 市场 | 说明 |
|------|------|------|
| SH | 上海证券交易所 | 沪市 A 股、ETF、债券等 |
| SZ | 深圳证券交易所 | 深市 A 股、创业板、ETF 等 |
| BJ | 北京证券交易所 | 北交所股票 |
| SHF | 上海期货交易所 | 上期所期货 |
| DCE | 大连商品交易所 | 大商所期货 |
| ZCE | 郑州商品交易所 | 郑商所期货 |
| CFX | 中国金融期货交易所 | 中金所股指/国债期货 |
| INE | 上海国际能源交易中心 | 原油等期货 |
| GFE | 广州期货交易所 | 广期所期货 |
| US | 美股 | 美国证券市场 |
| HK | 港股 | 香港联交所 |

### 标的代码示例

- **A 股**：600000.SH（浦发银行）、000001.SZ（平安银行）、920662.BJ（北交所股票）
- **美股**：AAPL.US（苹果）、TSLA.US（特斯拉）、MSFT.US（微软）
- **港股**：00700.HK（腾讯控股）、09988.HK（阿里巴巴）
- **ETF**：510300.SH（沪深 300ETF）、159915.SZ（创业板 ETF）
- **指数**：000001.SH（上证指数）、399006.SZ（创业板指数）
- **期货**：au2604.SHF（黄金期货）、i2605.DCE（铁矿石期货）

### 目前支持状态

- ✅ **A 股（SH/SZ/BJ）**：实时行情、日 K、分钟 K、日内分时、财务数据、标的池
- ✅ **国内期货**：支持主力合约查询
- ✅ **美股（US）**：实时行情、全量历史日 K 线（支持前复权/后复权）、除权因子
- ✅ **港股（HK）**：实时行情、全量历史日 K 线（支持前复权/后复权）、除权因子

## 快速开始

### 免费服务（适合历史数据分析）

无需 API Key，直接使用：

```python
from tickflow import TickFlow

tf = TickFlow.free()

# 获取历史日 K 线
df = tf.klines.get("600000.SH", period="1d", count=100, as_dataframe=True)
print(df.tail())

# 查询标的信息
instruments = tf.instruments.get(symbols=["600000.SH", "000001.SZ"])
for inst in instruments:
    print(f"{inst.symbol}: {inst.name}")
```

**免费服务特点：**
- ✅ 历史日 K 线（1d、1w、1M、1Q、1Y）
- ✅ 标的信息、交易所、标的池查询
- ❌ 不支持实时行情
- ❌ 不支持分钟级 K 线（1m、5m、15m、30m、60m）

### 完整服务（实时行情 + 全部功能）

```python
from tickflow import TickFlow

# 自动读取环境变量 TICKFLOW_API_KEY
tf = TickFlow()

# 获取实时行情（支持多市场）
quotes = tf.quotes.get(symbols=["600000.SH", "AAPL.US", "00700.HK"])
for q in quotes:
    print(f"{q['symbol']}: {q['last_price']}")
```

## 常用 K 线周期

| 类型 | 周期代码 | 说明 |
|------|----------|------|
| 日内 | 1m | 1 分钟 K 线 |
| 日内 | 5m | 5 分钟 K 线 |
| 日内 | 15m | 15 分钟 K 线 |
| 日内 | 30m | 30 分钟 K 线 |
| 日内 | 60m | 60 分钟 K 线 |
| 日线及以上 | 1d | 日 K 线 |
| 日线及以上 | 1w | 周 K 线 |
| 日线及以上 | 1M | 月 K 线 |
| 日线及以上 | 1Q | 季 K 线 |
| 日线及以上 | 1Y | 年 K 线 |

## 使用示例

### 1. 获取实时行情

```python
from tickflow import TickFlow

tf = TickFlow()

# 按标的代码查询（支持 A 股、港股、美股混合查询）
quotes = tf.quotes.get(symbols=["600000.SH", "000001.SZ", "AAPL.US", "00700.HK"])
for q in quotes:
    print(f"{q['symbol']}: {q['last_price']}")
```

### 2. 获取历史 K 线

```python
from tickflow import TickFlow

tf = TickFlow()

# 单只股票日 K 线（最近 100 天）
df = tf.klines.get("600000.SH", period="1d", count=100, as_dataframe=True)
print(df.tail())

# 批量获取多只股票的 K 线
symbols = ["600000.SH", "000001.SZ", "600519.SH"]
dfs = tf.klines.batch(symbols, period="1d", count=100, as_dataframe=True, show_progress=True)
```

### 3. 获取日内分时数据

```python
from tickflow import TickFlow

tf = TickFlow()

# 获取当日 1 分钟 K 线
df = tf.klines.intraday("600000.SH", as_dataframe=True)
print(f"今日已有 {len(df)} 根分钟 K 线")
```

### 4. 查询标的信息

```python
from tickflow import TickFlow

tf = TickFlow()

# 查询单个或多个标的信息
instruments = tf.instruments.get(symbols=["600000.SH", "000001.SZ"])

# 查询标的池
a_stocks = tf.instruments.get(universes=["CN_Equity_A"])
print(f"共有 {len(a_stocks)} 只 A 股")
```

### 5. 获取财务数据

```python
from tickflow import TickFlow

tf = TickFlow()

# 利润表
income_df = tf.financials.income(["000001.SZ", "600519.SH"], as_dataframe=True)

# 资产负债表
balance_df = tf.financials.balance_sheet(["000001.SZ"], as_dataframe=True)

# 现金流量表
cashflow_df = tf.financials.cash_flow(["000001.SZ"], as_dataframe=True)

# 核心财务指标
metrics_df = tf.financials.metrics(["000001.SZ"], as_dataframe=True)
```

## 注意事项

- 必须在当前 skills 项目的 `python` 文件夹下使用 `uv run python` 运行脚本
- 首次使用需要运行 `uv sync` 安装依赖
- SDK 支持 Python 3.9+，推荐使用 Python 3.10 或更高版本
- 免费服务仅提供历史日 K 线，不含实时行情和分钟 K 线
- 单次单标的最多获取 10000 根 K 线
- API Key 通过环境变量 `TICKFLOW_API_KEY` 配置
- 使用 `as_dataframe=True` 参数可直接返回 pandas DataFrame

## 运行脚本

```bash
cd /home/admin/.openclaw/workspace/skills/tickflow-assist/python
uv sync  # 确保依赖已安装
uv run python your_script.py
```
