# 经济学家立传提示词（Joel Mokyr）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2025 年得主（独得一半）Joel Mokyr（乔尔·莫基尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Joel_Mokyr/page.md`，与其冲突时以 page.md 为准；`metadata.json` 仅作结构化参考。

## 一、背景信息 【人物专属】

- **目标经济学家**：Joel Michael Mokyr（1946-07-26 生于荷兰莱顿，在世）
- **气质关键词**：**经济史的Builder、文化增长论的旗手、技术进步的史官** —— 美籍/以色列双重公民经济史学家，西北大学 Robert H. Strotz Professor of Arts and Sciences，兼特拉维夫大学 Eitan Berglas 经济学院 senior adjunct professor
- **诺奖获奖理由**（2025 年经济学奖**独得一半**；拆分理由年份，逐字引自 `economics/nobel_economics_citations.json` 2025 年 Joel Mokyr 条目；中文对照 `economics/economics_list_data.py` 2025 年 `||` 拆分第一段）：
  > "for having identified the prerequisites for sustained growth through technological progress"（表彰他识别了通过技术进步实现持续增长的前提条件）
  > 另一半由 Philippe Aghion 与 Peter Howitt 共享（理由为 creative destruction 理论，勿混写）。
  > 诺贝尔委员会另 credit 其 "demonstrat[ing] that if innovations are to succeed one another in a self-generating process, we not only need to know that something works, but we also need to have scientific explanations for why."（page.md 明载原文，方括号照录）
- **设计母题**：**自发生长的链条（self-generating chain of innovation）**——创新环环相扣、逐级攀升的阶梯与齿轮咬合，呼应委员会「创新相继接续的自发生成过程」：背景母题用错落上升的链环/阶梯与香槟金节点。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Joel_Mokyr/page.md`（同目录 `metadata.json` 仅作参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Joel_Mokyr/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Joel_Mokyr_zh`、`VIDEO_NAME=Joel_Mokyr_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Mokyr 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | economic history | 经济史 | discipline 明载，学术身份核心 | 封面、核心页 |
| 1 | Industrial Revolution | 工业革命 | 核心解释对象（A Culture of Growth 等） | 核心页 |
| 2 | technological change | 技术变革 | 获奖理由核心词（technological progress） | 核心页 |
| 3 | sustained economic growth | 持续经济增长 | 获奖理由核心词（sustained growth） | 核心页 |
| 4 | culture and growth | 文化与增长 | A Culture of Growth 主题；书评节 | 专著页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 11 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Philippe Aghion | 无向 | 2025 经济学奖，Mokyr 独得一半 |
| co-honored | Peter Howitt | 无向 | 2025 经济学奖，Aghion 与 Howitt 共享另一半 |
| spouse | Margalit Birnbaum | 无向 | 妻，UIC 生化与分子生物学教授，育两女 |
| advisor-student | Avner Greif | Mokyr → 学生 | infobox Doctoral students 明载；2025 合著 |
| advisor-student | Ran Abramitzky | Mokyr → 学生 | infobox Doctoral students 明载 |
| advisor-student | Mauricio Drelichman | Mokyr → 学生 | infobox Doctoral students 明载 |
| advisor-student | Marlous van Waijenburg | Mokyr → 学生 | infobox Doctoral students 明载 |
| influence | Cormac Ó Gráda | 无向 | infobox Influenced 明载，思想受其影响 |
| colleague | David Landes | 无向 | 2010 合编 The Invention of Enterprise |
| colleague | William Baumol | 无向 | 2010 合编 The Invention of Enterprise |
| colleague | Guido Tabellini | 无向 | 2025 合著 Two Paths to Prosperity |

**不入库但提示词可叙述**：frontmatter doctoral_advisor（John C.H. Fei / William N. Parker）系 metadata-only，page.md 正文与 infobox 均未载，**禁建边**（陷阱表裁定）；兄 Rob Mok（荷兰前总辩护人，已故）系亲属红链接人物不入库；书评人 McCloskey / DeLong / Bateman / Coyle / Hodgson 仅书评叙述非合作关系。

## 五、配色方案 【人物专属】

- **气质**：厚重、史感、知识累积的暖意
- **主色**：`#283593`（manifest 预分配——深靛蓝，学术厚重与知识纵深）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeEconHist` 经济史 — 深靛 `#283593`
  - `badgeIR` 工业革命 — 钢蓝 `#1E4E79`
  - `badgeTech` 技术变革 — 琥珀 `#C07A2A`
  - `badgeCulture` 文化与增长 — 青绿 `#0E7C7B`
- **背景母题**：错落上升的链环/阶梯与香槟金节点（创新接续自发生长的抽象），呼应设计母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 技术进步史的诺贝尔奖 / Joel Mokyr 1946– + 四色 badge + 右上头像 + 国籍行（United States / Israel）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地莱顿、教育希伯来大学 BA 1968 +
    Yale MPhil 1972 / PhD 1974、任职西北大学、诺奖 2025 半份、核心领域）
03  核心贡献概览 — 技术进步的前提 / 文化与增长 / 工业革命解释 / 经济史编纂
04  早年：莱顿到海法 (1946–1968) — 大屠杀幸存者家庭、父 Salomon Mok 早逝、1955 移居以色列
05  希伯来大学与耶鲁 (1968–1974) — 经济+历史双学士、MPhil/PhD、论文低地国家工业化 (1974)
06  西北大学岁月 (1974– ) — assistant professor 起从未离开、Robert H. Strotz 教席、特拉维夫兼职
07  主编与学会 (1990s–2003) — Princeton 书系、Oxford 百科五卷、JEH 联合主编、EHA 主席 2002–03
08  获奖理由核心页（★）— 持续增长的前提：创新自发生成需要科学解释（委员会 credit 原文）
09  A Culture of Growth (2016) — 文化作为增长<boosting 因素的解释
10  书评与反响 — McCloskey "brilliant book"（原文引语框）、DeLong (Nature)、Bateman、The Economist
11  批评与对话 — Hodgson "too much explanatory weight"（原文）、文化定义之辨（The Economist 指出）
12  主要著作 — Lever of Riches 1992 / Gifts of Athena 2002 / Enlightened Economy 2009 /
    Two Paths to Prosperity 2025（与 Greif、Tabellini 合著）
13  荣誉与认可 — Heineken History 2006 · Balzan 2015 · 荷兰皇家科学院外籍 2001 ·
    AAAS 1996 · Econometric Society Fellow 2011 · AEA Distinguished Fellow 2018 · Clarivate 2021
14  遗产与结尾 — 经济史与文化增长论的现代格局；2026 Carnegie Great Immigrants；结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 拆分理由年份 | 2025 为拆分理由年份：**Mokyr 独得一半**（"for having identified the prerequisites..."），Aghion 与 Howitt **共享另一半**（"for the theory of sustained growth through creative destruction"）。两条理由勿混写、勿写成三人共享同一句 |
| 出生国 | 生于**荷兰莱顿**（非以色列）；1955 年 9 岁随母移居以色列、海法长大。yaml 国籍按 Nobel 口径填 United States / Israel（infobox Citizenship 明载 American + Israeli） |
| 博士导师 metadata-only | frontmatter 载 John C.H. Fei 与 William N. Parker，但 page.md 正文与 infobox 均未载 → **不入库**（禁建边）；提示词叙述亦不展开 |
| 引语红线 | McCloskey 书评（"brilliant book..."）、Hodgson 批评（"too much explanatory weight"）、委员会 credit（"demonstrat[ing] that..."）均有 page.md 英文原文，**引原文+译文**；方括号 [ing] 照录；中文引号内不得写「原话」除非有英文原文 |
| "Nobel-worthy" 性质 | McCloskey 书评誉其为 "Nobel-worthy economic scientist"——是**书评预言**而非获奖注记，勿写成「早被预判获奖」类叙事 |
| 姓氏细节 | 本人姓 Mokyr，父亲姓 **Mok**（Salomon Mok），兄为 Rob Mok——三种拼写并存系家族史实，勿「统一」 |
| 西北大学 | 1974 年起 assistant professor 至今，**从未离开**；Robert H. Strotz Professor of Arts and Sciences；另兼特拉维夫大学 senior adjunct professor（勿写成全职） |
| 妻子专业 | 妻 Margalit（née Birnbaum）是 **UIC 生化与分子生物学教授**，勿与经济学混淆 |
| A Culture of Growth 书名 | 2016 年 Princeton University Press；副题 *The Origins of the Modern Economy*；书中解释对象是工业革命，勿写「解释中国」等书外延伸 |
| 学位年份 | BA 1968（希伯来大学，经济+历史）、MPhil 1972、PhD 1974（均 Yale）；论文 1974，修订版 1976 由 Yale Press 出版（书名作 *Industrialization in the Low Countries, 1795–1850*）——论文与成书年份/书名两套口径勿混 |
| 在世者 | 得主在世，生卒页只写生年 1946-07-26，卒位留白 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| economic history | 经济史 | discipline 核心词，勿泛化为 history |
| sustained growth | 持续增长 | 获奖理由核心词 |
| technological progress | 技术进步 | 获奖理由核心词，与 creative destruction（他人理由）区分 |
| self-generating process | 自发生成过程 | 委员会 credit 措辞 |
| Industrial Revolution | 工业革命 | 解释对象，专名大写 |
| A Culture of Growth | 《增长的文化》 | 2016 专著，获奖核心著作 |
| creative destruction | 创造性破坏 | **Aghion/Howitt 理由词**，Mokyr 篇仅对照出现 |
| economic historian | 经济史学家 | 职业身份 rank 表述 |
| prerequisites | 前提条件 | 获奖理由首词，勿译「基础」 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（manifest 预分配，本批三人均为 PAST）
- **匹配理由**：经济史学家立传天然带有「历史感/深沉」气质——从莱顿战后来到海法、再到西北大学半个世纪的经济史书写，PAST 的历史纵深感与其「为增长寻找历史前提」的学术形象契合。
- **本地路径**：`music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → 复制为 `economics/presentations/21th_century/Joel_Mokyr/PAST.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
- **撞曲提示**：本批 Mokyr / Howitt / Aghion 三人同曲 PAST，出片阶段如需去重由主控统一裁定，本篇按 manifest 值执行。
