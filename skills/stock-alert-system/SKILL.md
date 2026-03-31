---
name: stock-alert-system
description: A 股智能监控系统。为用户管理自选股池，提供定时推送服务：(1) 每日热点板块推送 (2) 盘中自选股扫描 (3) 收盘复盘。支持添加/删除/查看自选股，自动执行定时任务推送行情和操作建议。
---

# Stock Alert System - A 股智能监控系统

## 核心功能

### 1. 自选股管理
- **添加股票**：用户说"添加 XXX 到自选股" → 记录股票代码和名称
- **删除股票**：用户说"从自选股删除 XXX" → 移除对应股票
- **查看列表**：用户问"我的自选股有啥" → 显示当前持仓

### 2. 定时推送任务
| 任务 | 时间 | 内容 |
|------|------|------|
| 每日热点板块 | 每天 08:30 | 推送当天 3-5 个热门板块及上涨原因 |
| 上午盘中扫描 | 每天 10:30 | 扫描自选股走势 + 操作建议 |
| 下午盘中扫描 | 每天 14:30 | 扫描自选股走势 + 操作建议 |
| 收盘复盘 | 工作日 16:00 | 复盘当日表现 + 明日关注点 |

## 配置管理

### 自选股存储
文件位置：`/home/admin/.openclaw/workspace/skills/stock-watcher/.clawdbot/stock_watcher/watchlist.txt`

格式：
```
# 自选股列表
# 格式：股票代码 | 股票名称

300750|宁德时代
300502|新易盛
300290|荣科科技
```

### 定时任务配置
使用 `openclaw cron` 命令管理：

```bash
# 添加任务
openclaw cron add --name "任务名" --cron "表达式" --tz "Asia/Shanghai" \
  --session "isolated" --wake "now" \
  --message "任务描述" \
  --channel "openclaw-weixin" --to "用户 ID" --account "账户 ID"

# 查看任务
openclaw cron list

# 编辑任务
openclaw cron edit <job-id> --cron "新表达式"

# 删除任务
openclaw cron rm <job-id>
```

## Cron 表达式参考

| 频率 | 表达式 |
|------|--------|
| 每天 08:30 | `30 8 * * *` |
| 每天 10:30 | `30 10 * * *` |
| 每天 14:30 | `30 14 * * *` |
| 工作日 16:00 | `0 16 * * 1-5` |

## 记忆同步

重要配置需同步到用户记忆：

**长期记忆 (MEMORY.md)：**
```markdown
## 📈 投资配置

### 自选股池
| 代码 | 名称 |
|------|------|
| 300750 | 宁德时代 |
| 300502 | 新易盛 |
| 300290 | 荣科科技 |

### 定时推送任务
| 任务 | 时间 | 说明 |
|------|------|------|
| 每日热点板块 | 每天 08:30 | 推送热门板块 |
| 上午盘中扫描 | 每天 10:30 | 自选股走势 + 建议 |
| 下午盘中扫描 | 每天 14:30 | 自选股走势 + 建议 |
| 收盘复盘 | 工作日 16:00 | 当日表现 + 明日关注 |
```

**每日记忆 (memory/YYYY-MM-DD.md)：**
- 记录当日配置变更
- 记录对话摘要

## 使用示例

### 添加自选股
用户："添加宁德时代，添加新易盛，添加荣科科技到自选股里"

操作：
1. 查询股票代码
2. 更新 watchlist.txt
3. 同步到 stock-analysis 的 data.json
4. 更新 MEMORY.md
5. 回复确认

### 查看自选股
用户："我的自选股有啥"

操作：
1. 读取 watchlist.txt
2. 读取 data.json
3. 汇总显示

### 设置定时任务
用户："每天早上 9 点前推送热点板块"

操作：
1. 创建 cron 任务 (08:30)
2. 配置推送内容
3. 更新记忆文件
4. 回复确认

## 注意事项

1. **时区**：所有定时任务使用 `Asia/Shanghai` 时区
2. **推送渠道**：使用 `openclaw-weixin` 渠道
3. **记忆同步**：配置变更后必须更新 MEMORY.md
4. **任务验证**：设置后使用 `openclaw cron list` 验证
5. **测试推送**：新任务可用 `openclaw cron run <job-id>` 测试

## 相关文件

- 自选股列表：`skills/stock-watcher/.clawdbot/stock_watcher/watchlist.txt`
- 股票分析数据：`skills/stock-analysis/.clawdbot/stock-analysis/data.json`
- 长期记忆：`MEMORY.md`
- 每日记忆：`memory/YYYY-MM-DD.md`
