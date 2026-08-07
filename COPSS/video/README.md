# COPSS 会长奖视频系列 — COPSS Presidents' Award Video Series

> 以 `Fields_Medal/video`、`Abel_Prize/video`、`Chern_Medal/video` 的 Beamer 版式为模板。
> 按年代分 5 集 + 序章 + 合集，覆盖 **1981–2026 全部 46 位 COPSS Presidents' Award 得主**。
> 人物照片取自 `COPSS/pages/` 离线维基百科页面（21 人有真人照片，25 人用姓名缩写圆盘占位）。

---

## 剧集目录

| 集数 | 标题 | 年代 | 得主数 | 页数 |
|---|---|---|---|---:|
| 00 | 什么是 COPSS 会长奖 | — | — | 8 |
| 01 | 奠基年代：统计理论大厦的奠基 | 1981–1990 | 10 | 12 |
| 02 | 贝叶斯复兴与计算革命 | 1991–2000 | 10 | 12 |
| 03 | 生物统计爆发与华人崛起 | 2001–2010 | 10 | 12 |
| 04 | 高维统计与机器学习融合 | 2011–2020 | 10 | 12 |
| 05 | 数据科学、AI 与贝叶斯革新 | 2021–2026 | 6 | 8 |
| allinone | **合集**（封面 + 5 章 + 46 人） | 1981–2026 | 46 | 52 |

> `episode-allinone/copss_allinone_zh.tex` 将全部 46 位得主汇集为单一文档：1 张总封面 + 5 张分章标题页 + 46 张人物页。

**得主合计：46 人**（每年 1 人）。其中 9 位华人、6 位女性。

---

## 各集人物

- **第 01 集（1981–1990）**：Bickel · Fienberg · Lai · Hinkley · Berger · Prentice · Wu · Carroll · Hall · McCullagh
- **第 02 集（1991–2000）**：Silverman · Reid · Wong · Donoho · Johnstone · R. Tibshirani · Roeder · Massart · Wasserman · Fan
- **第 03 集（2001–2010）**：Meng · Liu · Gelman · Newton · van der Laan · Lin · Rosenthal · Cai · Irizarry · Dunson
- **第 04 集（2011–2020）**：Chatterjee · Kou · Suchard · Wainwright · Storey · Meinshausen · VanderWeele · Samworth · Wickham · Barber
- **第 05 集（2021–2026）**：Leek · Witten · R. Tibshirani · Ročková · Mackey · Su

亮点：Reid 首位女性得主（1992）；Lai 首位华人得主（1983）；Wickham 首位以软件开发获奖（2019）；Su 以深度学习理论获奖（2026）。

---

## 版式说明

- XeLaTeX + Beamer（16:9，中文 PingFang SC）。
- 人物页统一使用 `\personslide` 宏：左侧照片（或姓名缩写圆盘占位）、中间信息卡（获奖/生卒/国别/机构）、右侧核心贡献。
- 配色以统计蓝（`#2166AC`）+ 统计红（`#B2182B`）+ 暖金（`#E0913A`）+ 紫罗兰（`#6A51A3`）为主，区别于菲尔兹奖（金）、阿贝尔奖（深蓝+翠绿）、陈省身奖章（深青+金）系列。
- 每集以标题页开场、以「本集综述」收束；合集以总封面 + 分章标题页组织。

---

## 编译

需要 `xelatex`（TeX Live）。生成视频还需 `pdftoppm`（poppler）与 `ffmpeg`。

```bash
make              # 编译全部 PDF
make EP=01        # 只编译第 01 集
make EP=01,02     # 编译第 01、02 集
make -j4 pdf      # 并行编译

make images       # 由 PDF 生成每页 PNG（output/images/）
make video        # 合成 MP4（目录内 .wav 自动作为背景音乐）
make clean        # 清理中间文件
make distclean    # 清理全部生成物
```

单集目录内同样支持 `make` / `make images` / `make video` / `make clean`。

> **背景音乐**：各集 `awaken.wav` 为指向 `music_audio/bgm.wav` 的符号链接；Makefile 自动探测 `*.wav` 并循环配音。

> **重新生成人物页**：`python3 gen_copss.py` 依据内嵌的 46 人数据重新生成各集 `copss_epXX_zh.tex` 与合集 tex（编辑数据后运行即可）。

---

## 资料来源

- 离线人物页面：`COPSS/pages/<年份>/<姓名>/`
- 得主名录与获奖理由：`COPSS/copss_winners.md`
- 研究方向分类：`COPSS/copss_classification.md`
- COPSS 官网：<https://community.amstat.org/copss/home>
- Wikipedia：<https://en.wikipedia.org/wiki/COPSS_Presidents%27_Award>
