# 物理学家立传提示词（21 世纪批次 · Masatoshi Koshiba）

> **本文件是 OpenPhysicist 21 世纪诺奖物理学家立传提示词**，目标人物：Masatoshi Koshiba（2002 诺贝尔物理学奖，中微子天文学）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Masatoshi Koshiba（小柴昌俊），21 世纪（2002）诺奖得主系列。
- **设计哲学**：保留「身份信息页 + 研究领域表」骨架；Koshiba 篇是日本中微子天文三代传承（朝永→小柴→梶田）的枢纽人物——Kamiokande 与 Super-Kamiokande、"神冈之水"是全篇视觉母题。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Masatoshi Koshiba（1926-09-19 生于爱知县丰桥市 ~ 2020-11-12 逝于东京江户川医院，享年 94 岁）
- **气质关键词**：**中微子天文学的创立者之一、Kamiokande/Super-Kamiokande 的缔造者、师承朝永门下贯通两代诺奖** —— 2002 诺贝尔物理学奖获奖理由（官方原文，禁止改写）：
  > "for pioneering contributions to astrophysics, in particular for the detection of cosmic neutrinos"（因对天体物理学的开创性贡献，特别是宇宙中微子的探测）
- **设计母题**：**不可见之光（the invisible light）**。Kamiokande 把本为质子衰变而建的探测器改造成"看见"太阳中微子的眼睛——封面视觉用深蓝水体中一束被点亮的穿透光束呼应母题。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Masatoshi_Koshiba/page.md`（**已有本地**）
- **页面 HTML 与图片**：`Masatoshi_Koshiba.html` 与 `images/` **待下载**，Wikipedia URL：`https://en.wikipedia.org/wiki/Masatoshi_Koshiba`
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇到歧义先征求意见再继续。
> 数据库写入 `greatminds`（MySQL），yaml 母本 `MySQL/data/Kenneth_G_Wilson.yaml`，入库引擎 `MySQL/seed_person.py`。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ `page.md` 已有本地（21th_century/21st_century/Masatoshi_Koshiba/）
- 🔲 待下载 `Masatoshi_Koshiba.html` 与 infobox 头像 `images/`（404 则装饰圆占位；与 Koizumi 合照禁用作主肖像）
- 事实基准（已按 page.md 核对）：
  - 生卒：1926-09-19 生于爱知县丰桥 ~ 2020-11-12 逝于东京江户川医院，享年 94 岁；父 Toshio 为军官，母 Hayako 于其三岁时去世，父续娶其妻之姐；成长于横须贺
  - 国籍：日本（frontmatter 含 Empire of Japan 出生口径，正文统一写日本）
  - 教育：旧制第一高等学校成绩平平（宿舍澡堂听到老师贬语→发愤，室友 Kozo Kuchitsu 辅导物理）；东京大学物理 1951 毕业（理论物理仍吃力）；罗切斯特大学物理 PhD 1955（Fulbright 奖学金，朝永振一郎推荐信），论文《High energy electron-proton cascade in cosmic radiation》
  - 博士导师：罗切斯特 Morton F. Kaplon（infobox doctoral advisor）；朝永振一郎为东大恩师/Fulbright 推荐人/frontmatter doctoral_advisor——两说并存，yaml 双条目收录并注明年份口径
  - 任职：芝加哥大学 research associate 1955-07~1958-02（1959-11~1962-08 请假期间任高能物理与宇宙线实验室代理主任）；东京大学原子核研究所副教授 1958-03~1963-10；东大物理系副教授 1963-03、教授 1970-03、1987 名誉教授；东海大学 1987–1997；ICEPP 高级顾问
  - 关键荣誉：旭日奖 1987 · 仁科纪念奖 1987 · 日本学士院奖 1989 · 洪堡奖 1997 · 文化勋章 1997 · Wolf 2000 · Nobel 2002 · Panofsky 2002 · 富兰克林奖章 2003 · 勋一等旭日大绶章 2003 · 德国联邦功绩十字勋章 1985；东大设 Koshiba Hall 2005；Koshiba 奖 2003 设立
  - 核心贡献：①宇宙线研究出身；②1969 转入正负电子对撞机物理，参与德国 JADE 探测器（支持标准模型）；③与 Masayuki Nakahata、Atsuto Suzuki 设计 Kamiokande（原为质子衰变实验，后借 Davis 的美国先行工作改造为探测太阳中微子）；④1987 探测到银河系外超新星 SN 1987A 的中微子——中微子天文学确立；⑤1996 启用 Super-Kamiokande，后证实大气中微子振荡（由其学生梶田隆章主持运行）
  - 学生：Yoji Totsuka、Atsuto Suzuki（infobox 博士生）；Takaaki Kajita（other notable students，正文"run under the direction of Koshiba's student"）
  - 师承名言："在我继承我事业的学生中，有两位配得诺贝尔奖"（指 Totsuka 与 Kajita）；Totsuka 2008-07-10 因结肠癌去世，Koshiba 在《文艺春秋》撰文悼念；2010 设 Shuji Orimoto 奖与 Yoji Totsuka 奖
  - 个人生活：1950s 末回日本后娶美术馆策展人 Kyoto Kato（朝永为媒人）；一子（香川大学工学部教授小柴俊）一女；晚年沉迷电子游戏自称"世界最年长玩家"（最爱 Final Fantasy），喜好莫扎特
  - 诺奖演讲：2002-12-08 "Birth of Neutrino Astrophysics"
  - 关键时间线（≥15 节点）：1926 生丰桥 → 三岁丧母 → 横须贺长大 → 一高"澡堂贬语"发愤 → 1951 东大毕业 → Fulbright 赴美 → 1955 罗切斯特博士 → 1955–1958 芝加哥大学 → 1958 原研副教授 → 1963 东大副教授 → 1969 转向对撞机物理 → 1970s 初与 Budker 合作 → 1970-03 东大教授 → 1980s Kamiokande 建成 → 1987 SN 1987A 中微子 → 1987 旭日/仁科奖 → 1989 学士院奖 → 1996 Super-K 投入运行 → 1997 洪堡奖/文化勋章 → 1998 大气中微子振荡证据 → 2000 Wolf → 2002 诺奖+Panofsky → 2003 富兰克林奖章/绶章/Koshiba Hall → 2008 Totsuka 去世 → 2010 设奖纪念 → 2020 逝于东京

### 第 4 步：研究领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neutrino astronomy | 中微子天文学 | Kamiokande/Super-K 缔造，2002 诺奖核心 | 核心页 |
| 1 | particle physics | 粒子物理 | JADE 对撞机实验、质子衰变搜索 | 方法页 |
| 2 | astrophysics | 天体物理 | 获奖理由领域、超新星中微子 | 核心页 |
| 3 | cosmic rays | 宇宙线 | 出身方向、罗切斯特博士论文 | 早年页 |
| 4 | collider physics | 对撞机物理 | 1969 转向、JADE | 对撞机页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Morton F. Kaplon | 师→生（博士导师） | 罗切斯特大学博士导师，宇宙线方向 |
| advisor-student | Sin-Itiro Tomonaga | 师→生（恩师） | 东大时代恩师，Fulbright 推荐人，1965 诺奖 |
| colleague | Gersh Budker | 无向 | 1970s 初合作，苏联电子冷却先驱 |
| advisor-student | Yoji Totsuka | Koshiba→学生 | 博士生，Super-K 方向继承者，2008 卒 |
| advisor-student | Atsuto Suzuki | Koshiba→学生 | 博士生，Kamiokande 共同设计者 |
| advisor-student | Takaaki Kajita | Koshiba→学生 | 学生，Super-K 运行主持者，2015 诺奖 |
| co-honored | Raymond Davis Jr. | 无向 | 2002 诺贝尔物理学奖共享（宇宙中微子探测） |
| co-honored | Riccardo Giacconi | 无向 | 2002 诺贝尔物理学奖共享（X 射线天文学） |
| spouse | Kyoto Kato | 无向 | 美术馆策展人，1950s 末结婚，朝永为媒人 |

> 方向约定：导师有向；学生有向；同事/共同荣誉/配偶无向。
> 对手方规范名核对：Tomonaga 用库内记录 `Sin-Itiro Tomonaga`（id 2411，勿用 Shinichiro 变体）。

### 第 5 步：设计配色方案

- **气质**：深水、穿透、三代传承的静默荣光
- **配色**：深紫蓝（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - `mainclr` 深紫蓝 `#43305E`
  - `badgeNeu` 中微子天文学 `#5E4A8C`
  - `badgeSK` Kamiokande/Super-K `#2E7BA6`
  - `badgePart` 粒子/对撞机 `#C4783C`
  - `badgeCos` 宇宙线/超新星 `#8C2F3E`
- **背景母题**：柔和气泡——深蓝水体内一束穿透光带，呼应"不可见之光"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. 封面明示国籍，底部状态栏 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：左头像 + 右信息网格，事实取自 page.md，不得杜撰。
4. 品牌口径：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列（14 页）

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 中微子天文学的缔造者 / Masatoshi Koshiba 1926–2020 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — Kamiokande / SN 1987A / Super-K / 中微子振荡证据链
04  丰桥到东京：澡堂里的贬语 (1926–1951) — 丧母、一高发愤、东大物理
05  罗切斯特博士：宇宙线 (1951–1955) — Fulbright、朝永推荐信、Kaplon 指导
06  芝加哥与东大 (1955–1970) — 高能宇宙线、原研、东大教授
07  转向对撞机：JADE (1969–1980s) — 支持标准模型、与 Budker 的合作
08  Kamiokande：为质子衰变而建，因中微子而名（核心贡献页；公式框放概念图式——深蓝水体穿透光束示意，page.md 无公式，注明）
09  1987：SN 1987A 与中微子天文学的诞生
10  Super-Kamiokande：三代传承 — Totsuka、Kajita、大气中微子振荡
11  荣誉长廊 — Wolf 2000 · Nobel 2002 · 文化勋章 1997 · 旭日大绶章 2003
12  师门与人事 — "两位配得诺贝尔"、悼念 Totsuka、设奖纪念
13  晚年与遗产 — "世界最年长玩家"、Koshiba Hall
14  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 表格页安全负间距：顶部 −0.35cm、arraystretch 0.78–0.82；公式框前 −0.35~−0.55cm；希腊字母一律数学模式；日文罗马字注音（Koshiba Masatoshi）保持原文。

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句"pioneering contributions to astrophysics, in particular for the detection of cosmic neutrinos"（与 Davis 完全同句），勿写成"发现太阳中微子" |
| 双导师口径 | infobox doctoral advisor = Morton F. Kaplon（罗切斯特）；frontmatter doctoral_advisor = 朝永（东大恩师/Fulbright 推荐人）；yaml 双条目并注，勿混为一人或只取其一 |
| Tomonaga 规范名 | 库内记录为 `Sin-Itiro Tomonaga`（id 2411），yaml/正文沿用该形式，勿写 Shinichiro/Shin'ichirō 变体造成分裂 |
| Kajita 身份 | infobox 列于 Other notable students（正文称"其学生"），与 Totsuka/Suzuki 的 doctoral students 有别，note 措辞统一为"学生"不写"博士导师栏" |
| "两位配得诺奖" | Koshiba 原话经 page.md 转述（英译），指 Totsuka 与 Kajita——引用时标"generally believed"，勿坐实 |
| 改造 Kamiokande 的顺序 | Kamiokande 原为质子衰变实验（Koshiba 与 Nakahata、Suzuki 设计），未测到质子衰变后改造探测中微子、"following the pioneering U.S. work of Davis"——Davis 的先行地位勿抹去 |
| SN 1987A | 探测到银河系外（大麦哲伦云）超新星中微子，是中微子天文学确立的标志事件，年份 1987 |
| 合照 | 与 Koizumi 的合影、与 Koizumi+Tanaka 的首相官邸合影禁用作主肖像（政治人物同框） |
| 与田中耕一 | 诺奖次日田中获化学奖、媒体对比一事可客观一句，勿渲染两人恩怨 |
| 在世口径 | 1926-09-19 ~ 2020-11-12，享年 94 岁，勿漏卒日 |

### 第 9 步：术语审查清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Kamiokande | 神冈探测器 | 专名不译；全称 Kamioka Nucleon Decay Experiment |
| Super-Kamiokande | 超级神冈探测器 | 1996 投入运行 |
| neutrino astronomy | 中微子天文学 | 新学科创立口径 |
| SN 1987A | SN 1987A（超新星） | 大麦哲伦云，1987 |
| proton decay | 质子衰变 | 大统一理论预言，未测得 |
| neutrino oscillation | 中微子振荡 | 解释太阳中微子问题，证实归 Kajita 一代 |
| JADE | JADE 探测器 | 德国 DESY 对撞机实验，支持标准模型 |
| electron cooling | 电子冷却 | Budker 的加速器技术 |
| ICEPP | 基本粒子物理国际中心 | 东大，晚年任高级顾问 |
| Order of Culture | 文化勋章 | 日本 1997 年授予 |
| Koshiba Hall | 小柴霍尔/小柴厅 | 东大 2005 设立，可保留 Koshiba Hall |
| Fulbright Scholarship | 富布莱特奖学金 | 赴罗切斯特的资助来源 |

---

## 四、背景音乐选择 ✅

- **选定曲目**：**The Invisible Light** — Infraction（2:34，纪录片/电影/稳重）
- **匹配理由**：曲名"不可见之光"与中微子探测的设计母题天然同构；纪录片底色匹配 Kamiokande→Super-K 的长程叙事与 1987 超新星之夜的历史时刻。
- **本地路径**：`music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav` → 复制为 `presentations/21th_century/Masatoshi_Koshiba/The_Invisible_Light.wav`
- **备选**：Through the Darkness（突破前夕）、Last Hope

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Masatoshi_Koshiba/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
