# 医学家立传提示词（Torsten Wiesel）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Torsten Wiesel（1981 年诺贝尔生理学或医学奖得主，美国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Torsten_Wiesel/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Torsten Nils Wiesel（托斯滕·尼尔斯·维泽尔，1924-06-03 瑞典乌普萨拉 ~ 在世，2024-06-03 百岁）
- **气质关键词**：**与 Hubel 并肩二十五年的视觉生理学家、洛克菲勒大学第七任校长、科学家人权事业的全球推动者** —— 1981 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 David H. Hubel 共享，Sperry 得同年另一半）：
  > "for their discoveries concerning information processing in the visual system"
  > （因其关于视觉系统信息处理的发现）
- **设计母题**：**「从乌普萨拉到洛克菲勒」**。瑞典皇家诸 academy 与纽约学术塔尖之间的长路——视觉隐喻：北欧极简线条延伸至大洋彼岸的实验塔。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Torsten_Wiesel/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Torsten_Wiesel/`，成目录 `medic/presentations/20th_century/Torsten_Wiesel/`，Makefile 复制后设 `MAIN=Torsten_Wiesel_zh`、`VIDEO_NAME=Torsten_Wiesel_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neurobiology | 神经生物学 | 哈佛神经生物学系教授与系主任（1973），1981 诺奖核心 | 总览页 |
| 1 | visual system | 视觉系统 | 朝向选择性、眼优势柱、双眼视觉与立体视 | 视皮层页 |
| 2 | cortical plasticity | 皮层可塑性 | 关键期发育与剥夺实验 | 发育页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Torsten_Wiesel.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | David H. Hubel | — | 1981 诺贝尔生理学或医学奖两人共享视觉系统一半 |
| co-honored | Roger Wolcott Sperry | — | 1981 同年共享，Sperry 得大脑半球功能特化另一半 |
| collaborator | David H. Hubel | — | 1958 年相遇，二十余年研究搭档，1959 同赴哈佛 |
| advisor-student | Stephen Kuffler | 师 | 1955 年赴约翰霍普金斯在其门下开始眼科研修 |
| influence | Carl Gustaf Bernhard | — | 1947 年卡罗林斯卡其实验室为科学生涯起点 |
| spouse | Teeri Stenhammar | — | 1956 年成婚，1970 年离异 |
| spouse | Ann Yee | — | 1973 年成婚，1981 年离异 |
| spouse | Jean Stein | — | 1995 年成婚，2007 年离异 |
| spouse | Lizette Mususa Reyes | — | 2008 年成婚 |

> 说明：四段婚姻均具名（page.md 明载），全部建 spouse 边。女儿 Sara Elisabeth（1975）仅具名无叙事不入库。与 Hubel 的镜像边（co-honored+collaborator）按 batch-11 Cori 夫妻先例双边并存。2001 年 NIH 顾问提名被 Tommy Thompson 办公室否决事件为政治性叙事，不建人物边、正文一句带过（详见陷阱 6）。Kuffler 记录复用 batch-17（Eccles 学生）所建库内条目。2024-06-03 百岁寿辰是本篇最新事实点。

## 五、配色方案 【人物专属】

- **气质**：北欧的清冽、学术外交家的风度、百岁长者的沉静
- **主色**：极地蓝灰 `#41627E`（乌普萨拉冬季的天光）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 神经生物学 — 皮层青 `#2E7A8C`
  - `badgeB` 视觉系统 — 光条金 `#C8A02E`
  - `badgeC` 皮层可塑性 — 关键期橙 `#C0622E`
  - `badgeD` 人权事业 — 和平蓝 `#3A6B9E`
- **背景母题**：北欧极简地平线与纽约实验室塔剪影的呼应，稀疏放电波形，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 与 Hubel 并肩的视觉生理学家 / Torsten Wiesel 1924– + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像（2010 照）+ 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — 视觉信息处理 / 眼优势柱与关键期 / 学术外交与人权事业
04  乌普萨斯幼子 (1924–1947) — 五兄弟中最小、1947 入 Bernhard 实验室
05  卡罗林斯卡 (1947–1955) — 1954 医学博士、生理学系执教、儿童精神科病房
06  约翰霍普金斯：Kuffler 门下 (1955–1958) — 眼科研修、1958 助理教授、同年遇见 Hubel
07  与 Hubel 的二十五年（核心页）— 1959 猫视皮层实验、简单/复杂细胞、1959 同赴哈佛
08  眼优势柱与剥夺实验（核心页）— 小猫单眼剥夺、皮层柱接管、双眼视觉与立体视的丧失
09  1981 诺贝尔奖（核心页）— citation 原文、与 Hubel 共享一半、Sperry 另一半、诺奖演讲 The Postnatal Development of the Visual Cortex and the Influence of Environment
10  哈佛 24 年 (1959–1983) — 药理学讲师起步、1968 神经生物学教授、1973 系主任
11  洛克菲勒大学校长 (1991–1998) — 第七任校长、Astor 讲席教授、心智脑行为中心
12  学术外交版图 — 人类前沿科学计划秘书长 (2000-09)、北京 NIBS 顾问、OIST 共同主席、IBRO 主席
13  人权事业 — 美国国家科学院人权委员会十年主席 (1994-2004)、David Rall Medal 2005、以巴科学组织创始成员
14  荣誉与百岁 — National Medal of Science 2005 · 旭日大绶章 2009 · ForMemRS 1982 · 2024-06-03 百岁
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries concerning information processing in the visual system"（their 两人共享）；Sperry 另一半不同理由勿混 |
| 2 | 在世/百岁 | Wiesel 在世，2024-06-03 满 100 岁——生卒栏卒年留白，百岁是本篇亮点事实；勿按旧资料写卒年 |
| 3 | 国籍口径 | citation json 该行 country 标 Sweden（rowspan 视角），manifest/总表口径 United States——yaml 已按 US，正文叙述瑞典出生 |
| 4 | 师承双层 | Bernhard（1947 科学生涯起点，influence）与 Kuffler（1955 约翰霍普金斯门下，师生边）——两层勿混；Kuffler 记录复用 Eccles 篇所建 |
| 5 | 四段婚姻 | Teeri Stenhammar/Ann Yee/Jean Stein/Lizette Mususa Reyes 四段均建 spouse 边；Jean Stein 为作家兼编辑（有独立条目）；女儿 Sara Elisabeth 仅具名不入库 |
| 6 | NIH 事件 | 2001 年顾问提名被 HHS 部长办公室否决（官方称其「在纽约时报签署太多批评总统的公开信」）——page 明载、涉 Bush 政府政治语境：一句史实带过、不建边、不展开党派评价 |
| 7 | 人权事业 | 国家科学院人权委员会主席十年、以巴科学组织创始成员——page 明载可写，一句带过、克制呈现，不展开巴以议题 |
| 8 | 与 Hubel 分工 | 本篇与 Hubel 篇内容高度同构——以 Wiesel 视角行文（瑞典起点/眼科研修/洛克菲勒校长/人权外交），Hubel 篇主打微电极工程与美国段，避免复制粘贴 |
| 9 | 引语红线 | 本篇 page.md 无直接引语，禁编造；诺奖演讲题可作页面标题 |
| 10 | metadata 冲突 | frontmatter 无死亡日期（在世）；nationality 双值 Sweden/US，yaml 按 Nobel 口径 US |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| ocular dominance column | 眼优势柱 | 与 Hubel 篇共用核心术语 |
| binocular vision | 双眼视觉 | 剥夺实验的牺牲品 |
| stereopsis | 立体视 | 双眼深度知觉 |
| cortical plasticity | 皮层可塑性 | 关键期研究主线 |
| critical period | 关键期 | 发育时间窗 |
| deprivation | （单眼）剥夺 | 缝合眼睑实验 |
| Karolinska Institute | 卡罗林斯卡研究所 | 瑞典医学院，勿译「卡罗琳斯卡」 |
| Human Frontier Science Program | 人类前沿科学计划 | 2000-09 秘书长 |
| Rockefeller University | 洛克菲勒大学 | 第七任校长 (1991-98) |
| Order of the Rising Sun | 旭日章 | 2009 日本授予大绶章 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「远征」匹配其跨半球人生——乌普萨拉→约翰霍普金斯→哈佛→洛克菲勒，再加学术外交的全球航线（斯特拉斯堡/北京/冲绳）
  - 行进感契合「从瑞典青年到百岁学术外交家」的长途
- **备选**（未采用）：SEA（本批 Hubel 已用，双人组区分）、New Lands（batch-11 Houssay 已用且意象偏开辟）
- **本地路径**：按 music_audio/ 内 Alex-Productions Expedition 曲目复制至 `medic/presentations/20th_century/Torsten_Wiesel/Expedition.wav`，ffmpeg `-shortest` 对齐
