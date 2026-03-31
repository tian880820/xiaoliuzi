# MEMORY.md - Long-Term Memory

## Preferences

- **联网搜索优先使用 searxng skill** —— 只要涉及联网搜索任务，优先调用 searxng 技能而非直接使用 web_search 工具。

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
| 每日热点板块 | 每天 08:30 | 推送当天 3-5 个热门板块及上涨原因 |
| 上午盘中扫描 | 每天 10:30 | 扫描自选股走势 + 操作建议 |
| 下午盘中扫描 | 每天 14:30 | 扫描自选股走势 + 操作建议 |
| 收盘复盘 | 工作日 16:00 | 复盘当日表现 + 明日关注点 |

## 🔑 API Keys

### 东方财富妙想
- **MX_APIKEY**: `mkt_ob-qOWyAI5ZW_bHLkGuGV5poElCv_vU4GtybOtP0tck`
- 存储位置：`~/.openclaw/.env` + `~/.bashrc`
- 用途：妙想金融数据、资讯搜索、智能选股、自选股管理、模拟组合

## Notes

- Created: 2026-03-05
- 2026-03-31: 
  - 建立股票监控体系（3 只自选股 + 4 个定时任务）
  - 安装妙想 Skill 技能包（mx-data/mx-search/mx-xuangu/mx-zixuan/mx-moni）
