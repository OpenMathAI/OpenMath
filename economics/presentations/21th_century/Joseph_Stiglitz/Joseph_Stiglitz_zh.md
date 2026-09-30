# 经济学家立传提示词（Joseph Stiglitz）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2001 年得主 Joseph Stiglitz（约瑟夫·斯蒂格利茨）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Joseph_Stiglitz/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Joseph Eugene Stiglitz（1943-02-09 生于印第安纳州加里市，在世）
- **气质关键词**：**筛选理论的缔造者、市场失灵的吹哨人、公共知识分子的经济学家**
- **诺奖获奖理由**（三人共享，逐字取自 manifest）：
  > "for their analyses of markets with information asymmetry"（表彰他们对信息不对称市场的分析）
  > page.md 正文另载引申表述 "for laying the foundations for the theory of markets with asymmetric information"，展示以 manifest 官方句为准
- **设计母题**：**筛与网（screening & the net）**——Stiglitz 的核心贡献是「筛选」：无信息的一方设计机制让有信息的一方自己显形；视觉隐喻用「筛网截流/分层滤光」：一束光穿过多层筛网，被分离成不同色带。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Joseph_Stiglitz/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Joseph_Stiglitz/page.md`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Joseph_Stiglitz_zh`、`VIDEO_NAME=Joseph_Stiglitz_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库（yaml 在 `MySQL/data/Joseph_Stiglitz.yaml`），无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Stiglitz 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | information economics | 信息经济学 | 筛选（screening），诺奖核心 | 核心页 |
| 1 | macroeconomics | 宏观经济学 | 新凯恩斯主义，效率工资与失业 | 宏观页 |
| 2 | public economics | 公共经济学 | Henry George 定理、财政与税制 | 公共页 |
| 3 | economic inequality | 经济不平等 | The Price of Inequality 等著述主线 | 著述页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Solow | Stiglitz → 学生 | MIT 博士导师（1967，论文增长与收入分配） |
| advisor-student | Anton Korinek | 学生 | 博士生（infobox 明载） |
| advisor-student | Katrin Eggenberger | 学生 | 博士生（infobox 明载） |
| co-honored | George Akerlof | 无向 | 2001 诺贝尔经济学奖三人共享 |
| co-honored | Michael Spence | 无向 | 2001 诺贝尔经济学奖三人共享 |
| colleague | Hirofumi Uzawa | 无向 | 1965 芝加哥大学在其指导下研究，1969 合编增长理论文选 |
| colleague | Amartya Sen | 无向 | Stiglitz-Sen-Fitoussi 委员会共同主席（2008-2009） |
| colleague | Jean-Paul Fitoussi | 无向 | Stiglitz-Sen-Fitoussi 委员会共同主席（2008-2009） |
| collaborator | Michael Rothschild | 无向 | 1970 风险厌恶论文合著者（JET） |
| collaborator | Andrew Weiss | 无向 | 信贷配给论文合著者 |
| collaborator | Sanford J. Grossman | 无向 | Grossman-Stiglitz 信息效率悖论 |
| collaborator | Avinash Dixit | 无向 | Dixit-Stiglitz 垄断竞争模型 |
| collaborator | Carl Shapiro | 无向 | Shapiro-Stiglitz 效率工资模型（1984） |
| collaborator | Bruce Greenwald | 无向 | Greenwald-Stiglitz 定理与货币经济学合著者 |
| collaborator | Anthony B. Atkinson | 无向 | Lectures on Public Economics 1980 合著者 |
| spouse | Jane Hannaway | 无向 | 1978 结婚后离异 |
| spouse | Anya Schiffrin | 无向 | 2004-10-28 结婚，任教哥大 SIPA |
| influence | John Maynard Keynes | 无向 | infobox Influences 明载 |
| influence | James Mirrlees | 无向 | infobox Influences 明载 |
| influence | Henry George | 无向 | 亨利·乔治定理以之为名 |

**不入库但提示词可叙述**：Lawrence Summers（财政部长的紧张关系属行政博弈叙述，不建边）；育有四子三孙（子女未具名）；World Bank/IMF 是机构任职非人际关系。

## 五、配色方案 【人物专属】

- **气质**：穿透信息的锐利、公共议题的热度、筛选的秩序感
- **主色**：`#372A75`（manifest 预分配的深紫罗兰——与同届三人组统一底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeScreen` 筛选/信息经济学 — 深紫 `#372A75`
  - `badgeMacro` 新凯恩斯宏观 — 靛蓝 `#16324F`
  - `badgePublic` 公共经济学 — 琥珀 `#C07A2A`
  - `badgeIneq` 不平等研究 — 玫瑰 `#C4204F`
- **背景母题**：水平筛网线条与下落光粒（光粒穿过筛网被分层），呼应「机制让信息显形」的核心思想。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 筛选理论的缔造者 / Joseph Stiglitz 1943– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地加里市、教育 Amherst BA/MIT PhD 1967、
    任职 Yale/Stanford/Oxford/Princeton→Columbia 2001–、诺奖 2001、核心领域）
03  核心贡献概览 — 筛选 / 效率工资 / 公共财政 / 全球化批判
04  加里市少年 (1943–1965) — 钢铁城犹太家庭、Amherst 辩论队与学生会主席
05  MIT 与剑桥 (1965–1970) — Solow 门下 PhD 1967、Fulbright 赴 Fitzwilliam、Uzawa 指导
06  筛选：让信息自己显形（核心贡献页）— 逆向选择的另一面、保险市场分离均衡
07  市场失灵的地图 — Grossman-Stiglitz 悖论、信贷配给（与 Weiss）、Greenwald-Stiglitz 定理
08  效率工资与失业 — Shapiro-Stiglitz 模型、怠工与失业均衡
09  公共财政与亨利·乔治定理 — 地租融资地方公共品、Georgism 的现代表述
10  政策岁月 (1993–2000) — CEA 主席 1995-97、世界银行首席经济学家 1997-2000、2000 辞任
11  全球化的批评者 — Globalization and Its Discontents 2002、对 IMF 方式的质疑（客观简述）
12  度量社会进步 — Stiglitz-Sen-Fitoussi 委员会 2009 报告、GDP 之外
13  著述长廊 — Whither Socialism? / The Roaring Nineties / Freefall / The Road to Freedom 2024
14  遗产与结尾 — 信息经济学三巨头之一 + 结尾页（品牌 OpenMathAI）
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | manifest/官方句 "for their analyses of markets with information asymmetry"；page.md 另有 "for laying the foundations..." 引申句，展示以 manifest 为准 |
| 三人分工 | Stiglitz=筛选（无信息方设计机制）、Akerlof=逆向选择、Spence=信号传递，勿写成"共同提出" |
| 职业年限两说 | 世界银行首席经济学家 page.md 一处作 "from 1996 until last November"（本人自述），官方时间线为 1997-02 至 2000-02；时间线页用 1997–2000 口径 |
| 政治内容红线 | Labour Party 背书（Corbyn）、对 Obama/Clinton 的评价、Brexit/TTIP/TPP 立场、15M 运动支持等政治表态一律禁写；Clinton/世界银行任职仅作职业事实客观陈述 |
| IMF 批评的分寸 | 允许一句客观表述「因公开质疑 IMF 危机应对方式于 2000 年辞任」，不展开、不评价、不引用攻击性原话 |
| 引语红线 | page.md 有英文原文的引语（如诺奖演讲 "I hope to show that Information Economics..."）方可入引文框并附译文；无原文的中文转述禁加引号 |
| 拆分 stub 风险 | 对手方 Rothschild/Weiss/Grossman/Dixit/Shapiro/Greenwald/Atkinson 均为新建 stub，页面上引用其成果名（Dixit-Stiglitz 等）时人名拼写须与 yaml 一致 |
| 侧栏噪声 | page.md 中 Georgism/Macroeconomics 两大导航侧栏包含大量人名（含 Ostrom、Vickrey 等），全部是链接导航非本篇关系，严禁据此建边 |
| frontmatter 噪声 | metadata.json occupation 含 critic/non-fiction writer 等多项，primary_occupation 取 economist；生卒无噪声 |
| 妻子顺序 | Jane Hannaway（1978 婚，后离异）在前、Anya Schiffrin（2004-10-28 婚）在后，"third time" 指本人第三次结婚，勿写成"两次婚姻" |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| screening | 筛选 | Stiglitz 诺奖核心，无信息方主动设计；勿与 signaling（信号传递，Spence）混用 |
| information asymmetry | 信息不对称 | 获奖理由核心词 |
| adverse selection | 逆向选择 | 保险市场分离均衡被破坏的机制 |
| credit rationing | 信贷配给 | 与 Weiss：利率的信息与激励效应 |
| efficiency wages | 效率工资 | Shapiro-Stiglitz 模型，怠工防阻 |
| Henry George theorem | 亨利·乔治定理 | 地租融资地方公共品 |
| Greenwald-Stiglitz theorem | Greenwald-Stiglitz 定理 | 信息不完备下市场失灵为常态 |
| Dixit-Stiglitz model | Dixit-Stiglitz 模型 | 垄断竞争可解模型 |
| market failure | 市场失灵 | 贯穿全部贡献的关键词 |
| Invisible hand | 看不见的手 | Stiglitz 称其不存在，可作引语点题 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：深海的暗流贴合「信息藏于水面之下」——筛选的全部要义是让看不见的动机与类型显形；曲名的开阔感也匹配其从纯理论到全球公共议题的跨度（2001 三人共享奖同曲，属批次内撞曲，出片阶段由主控统一协调）。
- **本地路径**：复制 `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` 到 `economics/presentations/21th_century/Joseph_Stiglitz/SEA.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
