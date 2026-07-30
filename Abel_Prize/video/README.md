# 阿贝尔奖纪录片系列 — Abel Prize Video Series

> 以 `Fields_Medal/video_timeline` 的 Beamer 版式为模板，按年份顺序列出 **2003–2026 全部 29 位阿贝尔奖得主**。
> 人物照片取自 `Abel_Prize/pages/` 离线维基百科页面。

---

## 剧集目录

| 集数 | 标题 | 年份 | 得主数 |
|---|---|---|---:|
| 00 | 什么是阿贝尔奖 | — | — |
| 01 | 奠基年代 | 2003–2007 | 6 |
| 02 | 代数与几何的黄金时代 | 2008–2013 | 7 |
| 03 | 分析与数论的巅峰 | 2014–2019 | 7 |
| 04 | 新的前沿 | 2020–2026 | 9 |
| allinone | **合集**（00–04 汇为一册） | 2003–2026 | 29 |

> `episode-allinone/abel_prize_allinone_zh.tex` 将全部得主汇集为**单一文档**（34 页）：1 张总封面 + 4 张分章标题页 + 29 张人物页，方便一次浏览或整片输出。

**得主合计：29 人**（含 5 个双人共享年份：2004、2008、2015、2020、2021）

---

## 各集人物

- **第 01 集（2003–2007）**：Serre · Atiyah · Singer · Lax · Carleson · Varadhan
- **第 02 集（2008–2013）**：Thompson · Tits · Gromov · Tate · Milnor · Szemerédi · Deligne
- **第 03 集（2014–2019）**：Sinai · Nash · Nirenberg · Wiles · Meyer · Langlands · Uhlenbeck
- **第 04 集（2020–2026）**：Furstenberg · Margulis · Lovász · Wigderson · Sullivan · Caffarelli · Talagrand · Kashiwara · Faltings

亮点：Wiles 因费马大定理获奖（2016）；Uhlenbeck 首位女性得主（2019）；Kashiwara 首位日本得主（2025）；Faltings 首位德国得主（2026）。

---

## 版式说明

- 每集为独立的 XeLaTeX + Beamer 讲义（16:9，中文 PingFang SC）。
- 人物页统一使用 `\personslide` 宏：左侧照片、中间信息卡（获奖/生卒/国别/机构）、右侧核心贡献。
- 配色以深蓝（`#0B3D91`）+ 银灰为主，区别于菲尔兹奖系列的金色。
- 每集以标题页开场、以「本集综述」时间线收束。

---

## 编译

需要 `xelatex`（TeX Live）。生成视频还需 `pdftoppm`（poppler）与 `ffmpeg`。

```bash
make              # 编译全部 PDF
make EP=01        # 只编译第 01 集
make EP=01,02     # 编译第 01、02 集
make -j4 pdf      # 并行编译

make images       # 由 PDF 生成每页 PNG（output/images/）
make video        # 合成 MP4（若目录内放入 .wav 则自动作为背景音乐）
make clean        # 清理中间文件
make distclean    # 清理全部生成物
```

单集目录内同样支持 `make` / `make images` / `make video` / `make clean`。

> **背景音乐**：各集 Makefile 会自动探测本目录下的 `*.wav`；若存在则作为循环 BGM，否则生成无声视频。将音乐文件放入对应 `episode-*/` 目录即可。

---

## 资料来源

- 离线人物页面：`Abel_Prize/pages/<年份>/<姓名>/`
- 得主名录与获奖理由：`Abel_Prize/abel_prize_laureates.md`
- 官方网站：<https://abelprize.no/abel-prize-laureates>
- 阿贝尔奖（Wikipedia）：<https://en.wikipedia.org/wiki/Abel_Prize>
