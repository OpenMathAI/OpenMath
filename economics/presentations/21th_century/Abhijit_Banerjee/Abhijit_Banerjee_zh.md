# 经济学家立传提示词（Abhijit Banerjee）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2019 年得主 Abhijit Banerjee（阿比吉特·班纳吉）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Abhijit_Banerjee/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Abhijit Vinayak Banerjee（1961-02-21 生于印度孟买，在世）
- **气质关键词**：**贫穷的实验者、田野中的经济学家、RCT 革命的三驾马车之一**
- **诺奖获奖理由**（逐字引用，2019 三人共享）：
  > "for their experimental approach to alleviating global poverty"（表彰他们以实验性方法减轻全球贫困）
- **设计母题**：**随机分组（randomization）**——把人群像临床试验一样随机分成处理组与对照组，用硬币般的随机性剥离因果；视觉隐喻为错落分布的试验田块与随机散点，呼应「发展经济学即田野科学」。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Abhijit_Banerjee/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Abhijit_Banerjee/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Abhijit_Banerjee_zh`、`VIDEO_NAME=Abhijit_Banerjee_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Banerjee 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | development economics | 发展经济学 | infobox Sub-discipline 明载；诺奖核心 | 封面、核心页 |
| 1 | randomized controlled trials | 随机对照试验 | 借鉴临床试验的方法论革命 | 方法页 |
| 2 | applied microeconomics | 应用微观经济学 | 教育卫生等微观发展议题 | 研究页 |
| 3 | information economics | 信息经济学 | 哈佛博士论文主题（1988） | 博士页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Eric Maskin | Banerjee ← 导师 | 哈佛博士论文指导（infobox 明载） |
| advisor-student | Andreu Mas-Colell | Banerjee ← 导师 | 哈佛博士导师之一（infobox 明载） |
| advisor-student | Jerry Green | Banerjee ← 导师 | 哈佛博士导师之一（infobox 明载） |
| advisor-student | Esther Duflo | Banerjee → 学生 | MIT 博士生（infobox 明载），后为其妻与共同得主 |
| advisor-student | Dean Karlan | Banerjee → 学生 | infobox Doctoral students 明载 |
| advisor-student | João Leão | Banerjee → 学生 | infobox 明载 |
| advisor-student | Benjamin Jones | Banerjee → 学生 | infobox 明载 |
| advisor-student | Nancy Qian | Banerjee → 学生 | infobox 明载 |
| advisor-student | Maitreesh Ghatak | Banerjee → 学生 | infobox 明载 |
| advisor-student | Asim Ijaz Khwaja | Banerjee → 学生 | infobox 明载 |
| co-honored | Esther Duflo | 无向 | 2019 三人共享（实验性方法减轻全球贫困） |
| co-honored | Michael Kremer | 无向 | 2019 三人共享（实验性方法减轻全球贫困） |
| spouse | Esther Duflo | 无向 | 2015 结婚，第六对共同获诺奖的夫妇 |
| spouse | Arundhati Tuli Banerjee | 无向 | 第一任妻子（文学学者），2014 离异 |
| parent-child | Dipak Banerjee | Banerjee ← 父 | 父·普雷西登西学院经济学教授 |
| parent-child | Nirmala Banerjee | Banerjee ← 母 | 母·社会科学研究中心教授 |
| colleague | Sendhil Mullainathan | 无向 | J-PAL 共同创始人 |

**不入库但提示词可叙述**：本科课程老师 Mihir Rakshit/Nabhendu Sen、JNU 老师 Anjan Mukherjee/Krishna Bharadwaj（任教授课非导师关系）；哈佛同窗 Tyler Cowen/Alan Krueger/Nouriel Roubini 等（同学非可归类关系）；曾短暂担任 Jeffrey Sachs 研究助理（一次性助理经历）；2026 赴苏黎世大学系 Lemann 基金捐赠事件。

## 五、配色方案 【人物专属】

- **气质**：田野、随机、务实的贫民窟数据感
- **主色**：`#1E3A5F`（manifest 预分配·田野深蓝——统计报表与南亚泥土的双重色调）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRCT` 随机对照试验 — 深蓝 `#1E3A5F`
  - `badgeField` 田野实验 — 赭石 `#8C5A2B`
  - `badgeJPAL` J-PAL 机构 — 青绿 `#1B6B5A`
  - `badgeBook` 著作与传播 — 玫瑰 `#A3455A`
- **背景母题**：随机散点与分块试验田（处理组/对照组双色交错的抽象点阵），呼应「随机分组剥离因果」的核心方法。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 贫穷的实验者 / Abhijit Banerjee 1961– + 四色 badge + 右上头像 + 国籍行（India / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒孟买、Presidency BSc 1981、JNU MA 1983、
    哈佛 PhD 1988、MIT Ford Foundation 国际讲席教授、诺奖 2019、核心领域）
03  核心贡献概览 — RCT 方法论 / J-PAL / 贫穷的本质 / 发展经济学主流化
04  早年：孟买到加尔各答 (1961–1983) — 南点学校、ISI 一周退学、Presidency、JNU
05  哈佛博士：信息经济学 (1983–1988) — Maskin 指导，论文 Essays on Information Economics
06  执教之路：Princeton→Harvard→MIT (1988–1993)
07  田野实验的诞生：教育与健康（核心贡献页）— 拉贾斯坦邦豆子换接种、助教实验
08  J-PAL：把证据变成政策 (2003–) — 与 Duflo/Mullainathan 共创，MIT 全球研究中心
09  Poor Economics 与 Good Economics — 两本著作与 2012 Loeb 荣誉提名
10  2019 诺贝尔奖 — 三人共享、夫妻档第六对、诺奖演讲 Field experiments and the practice of economics
11  全球影响 — J-PAL 受益超 4 亿人（Duflo 页面口径，本篇按需引用）、UN 千年发展目标专家组 2013
12  苏黎世新章 (2026–) — Lemann 中心联合主任、MIT 兼职保留
13  门生与传承 — Duflo、Karlan、Nancy Qian 等七位博士生
14  遗产与结尾 — 实验方法「现已完全主导发展经济学」（瑞典科学院新闻稿口径）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 政治敏感红线 | page.md 后半载印度 BJP 对其获奖的批评、与 Rahul Gandhi/NYAY 基本收入的关联、Piyush Goyal/Rahul Sinha 言论等——**全部禁写**（政治敏感内容）；立传仅到学术事实为止 |
| 三位博士导师 | infobox 载 Eric Maskin/Andreu Mas-Colell/Jerry Green 三人；正文只明说论文由 Maskin supervised——note 措辞区分（Maskin 写"博士论文指导"） |
| 夫妻与学生双重关系 | Duflo 同时是 Banerjee 的博士生（infobox）、第二任妻子（2015）、共同得主——三条关系并行，note 各自写清，勿混 |
| 儿子之死 | 第一段婚姻的独子 2016 自杀——可客观一句带过或不写，**禁渲染细节** |
| ISI 退学 | 印度统计学院就读**一周即退学**转 Presidency，勿写成"ISI 求学" |
| 获奖理由归属 | citation 是 "their"（三人共享）；Banerjee 个人诺奖演讲题目 *Field experiments and the practice of economics*（2019-12-08），勿与理由句混淆 |
| J-PAL 创始人 | page.md 载与 Duflo 及 Sendhil Mullainathan 共同创立（一处行文含乱码 "the thavam"，忽略）；另 Kremer 妻 Glennerster 为 J-PAL 首任主管（载于 Duflo 页，本篇不写） |
| 苏黎世时间线 | 2025-10 宣布、2026-07 赴任 UZH 并共同执掌 Lemann 中心，MIT 保留兼职——三个时间点勿混 |
| 诺奖捐赠 | 三人将奖金捐给 Weiss Fund（载于 Kremer 页；Banerjee 页无载，**本篇禁写**） |
| metadata 噪声 | metadata.json 国籍序为 US,India，page.md 正文按 Nobel 口径 India/United States，yaml 取 manifest "India / United States" |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| randomized controlled trials (RCT) | 随机对照试验 | 获奖理由核心词，勿简写为"随机实验" |
| development economics | 发展经济学 | 勿译"经济开发学" |
| field experiments | 田野实验 | 诺奖演讲题目用词 |
| Poverty Action Lab (J-PAL) | 贫困行动实验室 | 全称 Abdul Latif Jameel Poverty Action Lab |
| Poor Economics | 《贫穷的本质》 | 2011 与 Duflo 合著，通行中译书名 |
| Good Economics for Hard Times | 《艰难时代的良好经济学》 | 2019 合著，书名译法以通行译名为准 |
| Millennium Development Goals | 千年发展目标 | 2013 UN 专家组背景 |
| Ford Foundation International Professor | 福特基金会国际讲席教授 | MIT 职衔全称 |
| advance of evidence-based policy | 循证政策 | 叙述用语，非专名 |
| co-honored laureates | 同届共享得主 | 2019 三人，勿写"平分"细节 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Mirage（海市蜃楼）暗合其研究主题——贫困常被直觉与教条笼罩如幻景，RCT 用最朴素的随机性把真实因果从迷雾中打捞出来；电子乐的冷静节拍也贴合"数据与田野"的方法论气质。
- **本地路径**：复制 `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` 到 `economics/presentations/21th_century/Abhijit_Banerjee/Mirage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
