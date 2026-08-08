# 图灵奖视频系列 — ACM Turing Award Video Series

> 以 `Fields_Medal/video`、`COPSS/video` 的 Beamer 版式为模板。
> 按研究方向分 10 集（T1–T10）+ 序章 + 合集，覆盖 **1966–2025 全部 81 位图灵奖得主**。
> 照片取自 `turing/pages/` 离线维基百科页面。

## 剧集目录

| 集数 | 标题 | 年代 | 得主数 | 页数 |
|---:|---|---|---:|---:|
| 00 | 什么是图灵奖 | — | — | 6 |
| 01 | 理论计算机科学 | 1966–2023 | 11 | 13 |
| 02 | 程序设计语言与软件方法学 | 1966–2020 | 15 | 17 |
| 03 | 人工智能与机器学习 | 1969–2024 | 12 | 14 |
| 04 | 操作系统与体系结构 | 1967–2017 | 8 | 10 |
| 05 | 数据库与数据管理 | 1973–2014 | 4 | 6 |
| 06 | 网络与万维网 | 2004–2022 | 4 | 6 |
| 07 | 分布式系统与形式验证 | 1972–2013 | 8 | 10 |
| 08 | 密码学与量子信息 | 2000–2025 | 10 | 12 |
| 09 | 数值计算与高性能计算 | 1968–2021 | 4 | 6 |
| 10 | 计算机图形学与人机交互 | 1988–2019 | 5 | 7 |
| allinone | **合集**（封面 + 81 人） | 1966–2025 | 81 | 82 |

## 各集人物

- **01 理论计算**：Cook · Karp · Hopcroft · Tarjan · Knuth · Rabin · Blum · Valiant · Wigderson · Hartmanis · Stearns
- **02 语言·编译**：Perlis · Backus · Floyd · Hoare · Wirth · Milner · Brooks · Aho · Ullman · Scott · Dahl · Nygaard · Kay · Iverson · Naur
- **03 AI·ML**：Minsky · McCarthy · Newell · Simon · Feigenbaum · Reddy · Pearl · Bengio · Hinton · LeCun · Barto · Sutton
- **04 系统**：Wilkes · Thompson · Ritchie · Cocke · Corbató · Allen · Hennessy · Patterson
- **05 数据库**：Bachman · Codd · Gray · Stonebraker
- **06 网络**：Cerf · Kahn · Berners-Lee · Metcalfe
- **07 分布式**：Dijkstra · Lampson · Pnueli · Clarke · Emerson · Sifakis · Lamport · Liskov
- **08 密码学**：Yao · Rivest · Shamir · Adleman · Goldwasser · Micali · Diffie · Hellman · Bennett · Brassard
- **09 数值**：Hamming · Wilkinson · Kahan · Dongarra
- **10 图形**：Sutherland · Engelbart · Thacker · Catmull · Hanrahan

亮点：Simon 唯一图灵+诺贝尔双料；Yao 首位（也是唯一）华人得主；Allen 首位女性；2018 深度学习三杰；2025 量子信息。

## 版式说明

- XeLaTeX + Beamer（16:9，中文 PingFang SC）。
- 人物页统一 `\personslide` 宏：左侧照片（或姓名缩写圆盘）、中间信息卡（获奖/生卒/国别/机构）、右侧核心贡献 + 主要荣誉。
- 配色：**图灵紫**（`#5B2D8E`）+ 琥珀金 + 青绿，区别于菲尔兹（金）、阿贝尔（深蓝）、陈省身（深青）、COPSS（统计蓝）。
- 封面：得主头像网格 + 标题 + 交叉荣誉徽标（♣N 诺贝尔 · ◆K 京都 · ◇G 哥德尔 · ★A 阿贝尔 · ★S 香农）。
- 每集以标题页开场、以「本集综述」收束。

## 编译

```bash
make              # 编译全部 PDF
make EP=01        # 只编译第 01 集
make images       # 由 PDF 生成每页 PNG
make video        # 合成 MP4（目录内 .wav 自动作为背景音乐）
make clean        # 清理中间文件
```

依赖：`xelatex`、`pdftoppm`、`ffmpeg`、`python3`。

> 背景音乐：各集 `awaken.wav` 指向 `music_audio/bgm.wav`（符号链接）。
> 重新生成人物页：`python3 gen_turing.py`（依据内嵌 81 人数据生成各集 tex）。

## 资料来源

- 离线页面：`turing/pages/<年份>/<姓名>/`
- 得主名录：`turing/turing_award_winners.md`
- 分类：`turing/turing_award_classification.md`
- Wikipedia：<https://en.wikipedia.org/wiki/Turing_Award>
