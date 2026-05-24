# 无尽海 · Endless Sea

**匿名漂流瓶虚拟世界 — 把你的心事投向大海**

写下你的秘密、心事、或一声叹息，让它漂向大海。被一个你永远不会认识的人捞起。完全匿名，无需注册。

---

## 🌊 这是什么？

无尽海是一个匿名的漂流瓶系统。你可以：

- **✍️ 写一个瓶子** — 写下心事，贴上情绪印章，选择信纸和瓶身，投向大海
- **🫧 捞起瓶子** — 随机捞起海面上陌生人漂来的瓶子，阅读、回复、或传递
- **💬 聊天室** — 当有人回复你的瓶子，一个匿名聊天室自动开启
- **🌟 灯塔许愿** — 在灯塔留下愿望，用海玻璃为别人的愿望助力
- **📖 协作故事** — 在沙滩上共同创作故事，一人一句接力
- **🧘 静心湾** — 心情记录、呼吸练习、树洞倾诉、求助热线
- **🛖 小屋装饰** — 用海玻璃装饰你的海边小屋

## 🏗 技术架构

```
endless-sea/
├── server.py          # 纯 Python 标准库后端 (~1000行)
├── server/
│   └── index.html     # 单文件前端 (~68KB)
├── config.json        # 配置文件
├── requirements.txt   # 依赖 (纯 stdlib，无外部依赖)
├── Procfile           # Heroku 部署
├── qr.jpg             # 打赏二维码
└── data/              # 运行时数据目录 (JSONL/JSON 文件存储)
```

### 技术栈

- **后端**: Python 3 stdlib `http.server` — 零外部依赖
- **前端**: 单文件 HTML/CSS/JS，原生实现
- **存储**: JSONL + JSON 文件数据库，无需安装数据库
- **部署**: 支持 Heroku / 任意 VPS

### API 一览

| 方法 | 路径 | 说明 |
|------|------|------|
| GET | `/api/identity` | 获取/创建匿名身份 |
| GET | `/api/bottles/pickup` | 捞取漂流瓶 |
| GET | `/api/bottles/mine` | 我扔过的瓶子 |
| GET | `/api/bottles/log` | 全部瓶子日志 |
| GET | `/api/chatrooms` | 我的聊天室列表 |
| GET | `/api/chatrooms/<id>` | 聊天室消息 |
| GET | `/api/lighthouse` | 灯塔许愿列表 |
| GET | `/api/stories` | 协作故事列表 |
| GET | `/api/stats` | 全站统计 |
| GET | `/api/calmcove/moods` | 心情记录 |
| GET | `/api/calmcove/treehole` | 树洞瓶子 |
| GET | `/api/calmcove/helplines` | 求助热线 |
| POST | `/api/bottles/throw` | 扔一个瓶子 |
| POST | `/api/bottles/reply` | 回复瓶子 |
| POST | `/api/chatrooms/<id>/send` | 发送聊天消息 |
| POST | `/api/chatrooms/<id>/close` | 关闭聊天室 |
| POST | `/api/lighthouse/wish` | 许愿 |
| POST | `/api/lighthouse/boost` | 助力愿望 |
| POST | `/api/stories/start` | 开始故事 |
| POST | `/api/stories/continue` | 续写故事 |
| POST | `/api/user/settings` | 更新设置（含青少年模式） |
| POST | `/api/report` | 举报内容 |
| POST | `/api/block` | 拉黑用户 |
| POST | `/api/gift` | 赠送海玻璃 |
| POST | `/api/calmcove/mood` | 记录心情 |
| POST | `/api/calmcove/treehole/throw` | 投树洞 |
| POST | `/api/calmcove/treehole/echo` | 树洞回声 |

## 🚀 部署

```bash
# 本地运行
python server.py

# 访问
open http://localhost:8765
```

Heroku 一键部署：

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## ⚙️ 配置

编辑 `config.json`：

- **server.port** — 服务端口，默认 8765
- **server.public_url** — 公网地址
- **propagation** — 跨平台传播（Reddit / Telegram / Pastebin / 留言板）
- **harvest** — 有趣内容自动采集

## 🎨 主题

支持日间/夜间模式，带潮汐过渡动画。右上角 🌓 按钮切换。

## 🪙 海玻璃经济

- 扔瓶子 +1 🪙
- 瓶子被捞起 +1 🪙
- 初始赠送 5 🪙
- 用于助力愿望、赠送他人、装饰小屋

## 📄 许可

MIT License

---

*"大海从不会评判任何一条河流。" — 无尽海*
