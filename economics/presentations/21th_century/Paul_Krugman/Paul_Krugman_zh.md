# 经济学家立传提示词（Paul Krugman）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2008 年得主 Paul Krugman（保罗·克鲁格曼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Paul_Krugman/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Paul Robin Krugman（1953-02-28 生于纽约州奥尔巴尼，在世）
- **气质关键词**：**新贸易理论的开创者、新经济地理学的奠基人、公共知识分子的双面人生**
- **诺奖获奖理由**（2008 独享，逐字引用）：
  > "for his analysis of trade patterns and location of economic activity"（表彰他对贸易模式与经济活动区位的分析）
- **设计母题**：**集聚（agglomeration）与核心-边缘（core-periphery）**——规模经济 + 消费者多样性偏好 + 运输成本三力互动，使制造业自我强化地聚集于少数地区：疏密两极的圆点群构成背景母题，密集核心与稀疏边缘相互映照。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Paul_Krugman/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/21th_century/Paul_Krugman/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Paul_Krugman_zh`、`VIDEO_NAME=Paul_Krugman_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Krugman 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | new trade theory | 新贸易理论 | 规模经济+多样性偏好解释相似国家间贸易，1979/1980 论文，诺奖核心 | 核心页 |
| 1 | new economic geography | 新经济地理学 | 1991 "Increasing Returns and Economic Geography"，集聚理论 | 核心页 |
| 2 | international finance | 国际金融 | 1979 货币危机模型（第一代投机攻击） | 金融页 |
| 3 | macroeconomics | 宏观经济学 | 流动性陷阱、萧条经济学复兴 | 宏观页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Rudi Dornbusch | Dornbusch → Krugman | MIT 博士导师（1977 论文 *Essays on Flexible Exchange Rates*），克氏誉为最伟大经济学教师之一 |
| advisor-student | Tahir R. Andrabi | Krugman → 学生 | infobox Doctoral students 明载 |
| advisor-student | Richard Baldwin | Krugman → 学生 | infobox Doctoral students 明载 |
| advisor-student | Gordon Hanson | Krugman → 学生 | infobox Doctoral students 明载 |
| advisor-student | Matthew J. Slaughter | Krugman → 学生 | infobox Doctoral students 明载 |
| influence | William Nordhaus | 无向 | infobox Influences 明载 |
| influence | Robert Solow | 无向 | infobox Influences 明载 |
| influence | John Maynard Keynes | 无向 | infobox Influences 明载；凯恩斯主义自我认同 |
| influence | David Hume | 无向 | infobox Influences 明载 |
| colleague | Maurice Obstfeld | 无向 | 合著标准教科书 *International Economics: Theory and Policy* |
| colleague | Elhanan Helpman | 无向 | 合著 *Market Structure and Foreign Trade*（1985）与 *Trade Policy and Market Structure*（1989） |
| colleague | Masahisa Fujita | 无向 | 合著 *The Spatial Economy*（1999） |
| colleague | Anthony Venables | 无向 | 合著 *The Spatial Economy*（1999）与 QJE 1995 论文 |
| collaborator | Gauti Eggertsson | 无向 | 合著 QJE 2012 债务-萧条模型（Fisher-Minsky-Koo 进路） |
| spouse | Robin Wells | 无向 | 1996 结婚，经济学家，多版教科书合著者，现任其 Substack 编辑 |

**不入库但提示词可叙述**：前妻 Robin L. Bergman（设计师，仅具名）；infobox Influences 中的 Rudi Dornbusch（已建 advisor-student，不重复建边）；Dixit 与 Stiglitz（1977 论文系文献引用非个人关系）；Reagan/Clinton/Bush/Obama/Trump 等政治人物（一律禁建）；远亲 David Frum；1976 葡萄牙央行之行同事群。

## 五、配色方案 【人物专属】

- **气质**：绿色理性、贸易与地理的宏大图景、锐利笔锋
- **主色**：`#146B3A`（manifest 预分配；深贸易绿——全球化与增长的底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeNTT` 新贸易理论 — 深绿 `#146B3A`
  - `badgeNEG` 新经济地理 — 靛蓝 `#1E3A5F`
  - `badgeFin` 国际金融 — 玫瑰 `#A63A2B`
  - `badgeMacro` 宏观与专栏 — 琥珀 `#C07A2A`
- **背景母题**：核心-边缘集聚图（疏密两极圆点群），呼应「规模报酬递增驱动的空间集中」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 新贸易理论的开创者 / Paul Krugman 1953– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地奥尔巴尼、教育 Yale BA 1974 / MIT PhD 1977、
    导师 Dornbusch、任职 CUNY/Princeton/MIT/LSE、诺奖 2008、核心领域）
03  核心贡献概览 — 新贸易理论 / 新经济地理 / 货币危机 / 萧条经济学
04  早年与 Asimov 的召唤 (1953–1977) — 心理史学梦、Yale summa cum laude、MIT 博士
05  新贸易理论：规模经济与多样性（核心贡献页一）— 1979 JIE 论文、Dixit-Stiglitz CES、home market effect
06  新经济地理：集聚的自我强化（核心贡献页二）— 1991 JPE 论文、核心-边缘模型、其自述「学术之爱」
07  国际金融：投机攻击与货币危机 — 1979 模型、第一代危机模型
08  流动性陷阱与萧条经济学 — 日本失去的十年、IS-LM、2008 危机预言
09  2008 诺贝尔奖 — 独享、颁奖词、第十二位 Clark→Nobel 双冠人（1991 Clark Medal）
10  公共知识分子 — NYT 专栏 2000–2024、《The Conscience of a Liberal》、Substack 转型
11  治学谱系 — Dornbusch 门下 + 四位知名博士生
12  荣誉与认可 — Clark 1991 · Asturias 2004 · Nobel 2008 · 荣誉博士若干
13  争议与回响 — 专栏笔战的批评与回应（Daniel Okrent / The Economist 等，客观并列）
14  遗产与结尾 — 贸易、地理与宏观经济分析的合流 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 政治内容红线 | 专栏涉及大量党派政治（Bush/Trump/Sanders/9/11 等），**只做时间线客观简述，不引用原话、不做立场评价**；本篇定位是经济学家立传，政治页（若保留）篇幅从简 |
| 获奖理由口径 | 官方 citation 为 "for his analysis of trade patterns and location of economic activity"；正文另有 "for his contributions to New Trade Theory and New Economic Geography" 的转述，两者勿混用，引文框只用前者 |
| 1979 两篇论文 | 同年发表货币危机模型（JMCB）与新贸易理论模型（JIE），勿混为一谈；危机模型改编自 Salant-Henderson 黄金市场讨论稿 |
| Dixit-Stiglitz | 1977 论文是文献引用（CES 效用函数来源），非个人师承关系，禁建关系边 |
| Clark Medal 口径 | 1991 年获约翰·贝茨·克拉克奖章；2009 年前每两年授一人，《The Economist》称其「比诺奖还难拿一点」；他是第 12 位 Clark→Nobel 双冠得主 |
| 新经济地理年份 | 1991 "Increasing Returns and Economic Geography"（JPE），其最常被引论文，自述「学术生涯之爱」；勿写成诺奖后成果 |
| 婚姻 | 第一任 Robin L. Bergman（离异）、第二任 Robin Wells（1996 结婚）；两位 Robin 勿混淆；无子女（其本人专栏澄清过） |
| 专栏生涯 | NYT 专栏 2000–2024，2024-12-09 最后专栏《Finding Hope in an Age of Resentment》；LSE Centennial Professor 名头勿写成全职 |
| 职务口径 | 现 CUNY Graduate Center 杰出教授；Princeton 2000–2015（退休荣休）；MIT 1979–2000（1984 正教授）；Yale 1977–1979 |
| metadata 噪声 | metadata.json occupation 列含 blogger/pundit 等宽泛词，occupations 入库只取 economist/columnist/professor 三类 |
| 亚洲观点 | 1994 "The Myth of Asia's Miracle" 争议客观呈现（东亚增长核算论战），不做胜负判定 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| new trade theory | 新贸易理论 | 获奖核心词，勿译「新贸易主义」 |
| new economic geography | 新经济地理学 | 简称 NEG，与地理学 Economic Geography 期刊区分 |
| economies of scale | 规模经济 / 规模报酬递增 | 集聚机制的引擎 |
| home market effect | 本土市场效应 | 大需求国净出口该品类的意外结论 |
| core-periphery model | 核心-边缘模型 | 集聚与运输成本的均衡图景 |
| monopolistic competition | 垄断竞争 | 建模框架（张伯伦传统 + CES） |
| speculative attack | 投机性攻击 | 第一代货币危机模型核心 |
| liquidity trap | 流动性陷阱 | 其宏观主张的关键词 |
| agglomeration | 集聚 | 生产与人口的空间集中 |
| John Bates Clark Medal | 约翰·贝茨·克拉克奖章 | 1991 年获，双冠叙事锚点 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Eternals 的深远绵长对应「贸易与地理的长期图景」——1979/1991 两篇奠基论文塑造了此后数十年国际经济学的研究版图；曲名的恒久感也贴合其「学术之爱」的新经济地理遗产。
- **本地路径**：复制 `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` 到 `economics/presentations/21th_century/Paul_Krugman/Eternals.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
