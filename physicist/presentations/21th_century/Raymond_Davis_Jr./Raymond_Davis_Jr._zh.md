# 物理学家立传提示词（21 世纪批次 · Raymond Davis Jr.）

> **本文件是 OpenPhysicist 21 世纪诺奖物理学家立传提示词**，目标人物：Raymond Davis Jr.（2002 诺贝尔物理学奖，太阳中微子探测）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Raymond Davis Jr.（雷蒙德·戴维斯），21 世纪（2002）诺奖得主系列。
- **设计哲学**：保留「身份信息页 + 研究领域表」骨架；Davis 篇是"一个化学家在中微子物理里凿了四十年矿"的独角戏——南达科他 Homestake 金矿地下 1.5 公里的六百吨四氯化碳，是全篇的视觉与叙事锚点。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Raymond Davis Jr.（1914-10-14 生于华盛顿特区 ~ 2006-05-31 逝于纽约州 Blue Point，享年 91 岁）
- **气质关键词**：**Homestake 实验的领军人、首个探测到太阳中微子的人、化学家的中微子苦旅** —— 2002 诺贝尔物理学奖获奖理由（官方原文，禁止改写）：
  > "for pioneering contributions to astrophysics, in particular for the detection of cosmic neutrinos"（因对天体物理学的开创性贡献，特别是宇宙中微子的探测）
- **设计母题**：**深地（deep underground）**。地下矿井里的放射性计数把天上的太阳"看见"——封面视觉用矿井竖井剖面与一枚被点亮的氩-37 原子呼应"向下挖掘，向上观天"。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Raymond_Davis_Jr./page.md`（**已有本地**）
- **页面 HTML 与图片**：`Raymond_Davis_Jr..html` 与 `images/` **待下载**，Wikipedia URL：`https://en.wikipedia.org/wiki/Raymond_Davis_Jr.`
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇到歧义先征求意见再继续。
> 数据库写入 `greatminds`（MySQL），yaml 母本 `MySQL/data/Kenneth_G_Wilson.yaml`，入库引擎 `MySQL/seed_person.py`。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ `page.md` 已有本地（21th_century/21st_century/Raymond_Davis_Jr./）
- 🔲 待下载 `Raymond_Davis_Jr..html` 与 infobox 头像 `images/`（2001 授勋照可用；404 则装饰圆占位）
- 事实基准（已按 page.md 核对）：
  - 生卒：1914-10-14 生于华盛顿特区 ~ 2006-05-31 逝于纽约州 Blue Point（阿尔茨海默病并发症），享年 91 岁；父为国家标准局摄影师；弟 Warren 小 14 个月；幼年唱诗班经历
  - 国籍：美国
  - 教育：马里兰大学化学 BS 1938（并获该校硕士）；耶鲁大学物理化学 PhD 1942，论文《碳酸的电离常数与二氧化碳在水及氯化钠溶液中的溶解度 (0–50 °C)》
  - 博士导师：page.md **无载**，禁写
  - 军旅：1942 以预备役军官入伍，二战大部分时间在犹他州达格威试验场观察化学武器试验、勘探大盐湖盆地（史前 Lake Bonneville 证据）
  - 任职：1945 起孟山都 Mound 实验室（俄亥俄 Miamisburg，AEC 相关放射化学）；1948 加入布鲁克海文国家实验室（BNL，"找点有趣的东西研究"→中微子）；1984 从 BNL 退休；infobox 机构另列宾夕法尼亚大学
  - 关键荣誉：Comstock（NAS）1978 · Tom W. Bonner（APS）1988 · Panofsky（APS）1992 · Beatrice M. Tinsley（AAS）1994 · George Ellery Hale（AAS）1996 · Wolf 2000 · 国家科学奖章 2001 · Nobel 2002 · Enrico Fermi Award 2003 · Benjamin Franklin Medal 2003（与 Bahcall、Koshiba 共享）· Glenn T. Seaborg 核化学奖
  - 核心贡献：①氯-氩(37Cl→37Ar) 放射化学中微子探测法；②1954 Brookhaven 反应堆/萨凡纳河反应堆实验——证明反应堆产生的反中微子不触发氯反应，确立中微子与反中微子之别；③Homestake 实验领军人（1960s–1980s），首次探测到太阳中微子，揭示太阳中微子问题；④1998 Homestake 最终结果论文（Cleveland et al.）
  - 个人生活：与 Anna Torrey 在 Brookhaven 相识结婚；共建 21 英尺木帆船 Halcyon；五个孩子；Blue Point 同一住所 50 余年
  - 诺奖演讲：2002-12-08 "A Half-Century with Solar Neutrinos"；获奖时 88 岁
  - 关键时间线（≥15 节点）：1914 生华盛顿 → 唱诗班/水门音乐会 → 1938 马里兰 BS → 耶鲁硕博 → 1942 物理化学博士 → 入伍/达格威 → 1945 孟山都 Mound → 1948 入 BNL → 氯-氩探测法研究 → 1953–1954 反应堆实验（反中微子不响应）→ 1964 Solar Neutrinos II（Homestake 提案）→ 1960s–1980s Homestake 运行 → 首测太阳中微子 → 太阳中微子问题 → 1978 Comstock → 1984 退休 → 1988 Bonner → 1992 Panofsky → 1994 Tinsley → 1996 Hale → 1998 最终结果 → 2000 Wolf → 2001 国家科学奖章 → 2002 诺奖（88 岁）→ 2003 Fermi 奖/Franklin 奖 → 2006 逝于 Blue Point

### 第 4 步：研究领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neutrino detection | 中微子探测 | 氯-氩放射化学法，毕生主线 | 核心页 |
| 1 | solar neutrinos | 太阳中微子 | Homestake 首测 + 中微子问题 | 核心页 |
| 2 | radiochemistry | 放射化学 | Mound/BNL 本业 | 方法页 |
| 3 | physical chemistry | 物理化学 | 耶鲁博士方向 | 早年页 |
| 4 | neutrino astrophysics | 中微子天体物理 | 2002 诺奖理由领域 | 荣誉页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Masatoshi Koshiba | 无向 | 2002 诺贝尔物理学奖共享（宇宙中微子探测） |
| co-honored | Riccardo Giacconi | 无向 | 2002 诺贝尔物理学奖共享（X 射线天文学） |
| co-honored | John N. Bahcall | 无向 | 2003 Benjamin Franklin Medal 共同得主 |
| spouse | Anna Torrey | 无向 | Brookhaven 相识结婚，共建帆船 Halcyon |

> 方向约定：共同荣誉与配偶无向。Davis 博士导师与学生 page.md 均无载，禁写。
> relations=4 为 page.md 明载之下的诚实值（此人无师生记录）。

### 第 5 步：设计配色方案

- **气质**：深地、坚韧、化学家的静默长跑
- **配色**：酒渍深红（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - `mainclr` 酒渍深红 `#6E2639`
  - `badgeNeu` 中微子探测 `#8C3A50`
  - `badgeSun` 太阳中微子 `#B07B30`
  - `badgeRadio` 放射化学 `#4E5A78`
  - `badgeAstro` 中微子天体物理 `#3E6B5A`
- **背景母题**：柔和气泡——深井剖面竖线与零星闪烁计数点，呼应"深地观天"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. 封面明示国籍，底部状态栏 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：左头像 + 右信息网格，事实取自 page.md，不得杜撰。
4. 品牌口径：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列（14 页）

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 深地数中微子的化学家 / Raymond Davis Jr. 1914–2006 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 氯-氩探测法 / 中微子≠反中微子 / Homestake / 太阳中微子问题
04  华盛顿童年与化学求索 (1914–1942) — NBS 摄影师之子、马里兰、耶鲁物理化学
05  战争与放射化学 (1942–1948) — 达格威试验场、孟山都 Mound 实验室
06  BNL 起点："找点有趣的东西研究" (1948) — 中微子选题的由来
07  反应堆实验 (1954–1956) — 氯不响应反中微子、与 Reines-Cowan 路线之别
08  Homestake：地下 1.5 公里的太阳观测站（核心贡献页；公式框放概念图式——矿井竖井剖面与 37Ar 计数示意，page.md 无公式，注明）
09  太阳中微子问题 — 测得流量偏少、四十年悬案
10  1998 最终结果与科学界回响
11  荣誉长廊 — Comstock 1978 · Bonner 1988 · Panofsky 1992 · Wolf 2000 · Nobel 2002 · Fermi 2003
12  家庭与晚年 — Anna Torrey、Halcyon 号、Blue Point
13  遗产：中微子天文学的起点之一
14  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 表格页安全负间距：顶部 −0.35cm、arraystretch 0.78–0.82；公式框前 −0.35~−0.55cm；希腊字母一律数学模式；上标 37Cl/37Ar 用数学模式 ^{37}。

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句强调"对天体物理学的开创性贡献，特别是宇宙中微子的探测"；Giacconi 获同奖另一半但方向为 X 射线天文学，勿把 X 射线写进 Davis 理由 |
| 诺奖结构 | 2002 一半给 Davis+Koshiba（宇宙中微子），另一半给 Giacconi（X 射线天文学）——"共享"表述须准确，勿写三人等分 |
| 化学家身份 | Davis 是化学家出身的物理学家（frontmatter field_of_work: chemistry；论文为物理化学），称"化学家兼物理学家"，勿只写物理学家 |
| 博士导师 | page.md 无载，禁写；禁从耶鲁物理化学反推 |
| 学生 | page.md 无博士生记录，禁写门生 |
| 反应堆实验结论 | 是"氯反应由太阳/宇宙中微子触发而反应堆反中微子不触发"的证据，勿写成 Davis 首次探测到中微子（Reines-Cowan 1956 直接探测反中微子在先，且 page.md 未载 Reines，勿提及） |
| Bahcall 身份 | page.md 仅在 2003 Benjamin Franklin Medal 共享处出现 Bahcall，note 只写共同获奖，勿补写"太阳中微子理论家"（该身份本页无载） |
| Homestake 地点 | page.md 只写 Homestake Experiment，未写南达科他与地下深度——视觉图式可示意矿井，但正文勿擅自补"1.5 km/南达科他"数字 |
| 享年 | 91 岁（1914-10-14 ~ 2006-05-31），勿误写 90 |
| 妻子 | Anna Torrey，在 Brookhaven 相识；帆船 Halcyon 21 英尺木帆船，细节可用 |

### 第 9 步：术语审查清单

| 英文 | 中文 | 风险 |
|------|------|------|
| chlorine-argon method | 氯-氩探测法 | 37Cl(ν,e−)37Ar，放射化学计数 |
| Homestake Experiment | Homestake 实验 | 金矿中的大型放射化学探测器，专名不译 |
| solar neutrino problem | 太阳中微子问题 | 测得流量低于预期，后由中微子振荡解释（解释者非本篇主角） |
| antineutrino | 反中微子 | 与中微子之别是 1950s 反应堆实验要点 |
| radiochemistry | 放射化学 | Davis 本业 |
| carbon tetrachloride | 四氯化碳 | 早期探测介质 |
| argon-37 | 氩-37 | 放射性产物，半衰期计数 |
| beta decay | β 衰变 | 中微子假说的物理背景 |
| physical chemistry | 物理化学 | 耶鲁博士方向 |
| cosmic neutrino | 宇宙中微子 | 获奖理由原文用词 |

---

## 四、背景音乐选择 ✅

- **选定曲目**：**PAST** — Alex-Productions（86k views，历史感/深沉）
- **匹配理由**："人物回顾/冷战时期/数学传统"场景标签正合 Davis 从 1940s 放射化学到 1980s Homestake 的四十年长跑；深沉底色匹配深地矿井与 88 岁获奖的迟来加冕。
- **本地路径**：`music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → 复制为 `presentations/21th_century/Raymond_Davis_Jr./PAST.wav`
- **备选**：The Flow of Time（时间感/纪录片）、Tragedy

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Raymond_Davis_Jr./page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
