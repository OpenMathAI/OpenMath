# 经济学家立传提示词（Daron Acemoglu）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2024 年得主 Daron Acemoglu（达龙·阿西莫格鲁）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Daron_Acemoglu/page.md`，与其冲突时以 page.md 为准（metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：Kamer Daron Acemoğlu（1967-09-03 生于伊斯坦布尔卡德柯伊，土耳其/美国双重公民，**在世**，卒年留白）
- **气质关键词**：**制度经济学的挖掘者、殖民地自然实验的设计师、MIT 最高讲席的年轻得主** —— 2024 年诺贝尔经济学奖获奖理由（与 James A. Robinson、Simon Johnson 共享，逐字引自 `economics/nobel_economics_citations.json` 2024 年 Daron Acemoglu 条目）：
  > "for studies of how institutions are formed and affect prosperity"（表彰他们关于制度如何形成并影响繁荣的研究）
- **设计母题**：**汲取型与包容型制度的分岔（extractive vs inclusive institutions）**——三人组的理论核心：殖民地疾病环境决定定居模式、定居模式决定早期制度、制度具有持续性并决定今日繁荣。视觉隐喻：一条道路在中段分成明暗两股，明股两侧有列柱与市集（包容），暗股被高墙锁闭（汲取），分岔点用诺奖金色高亮。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Daron_Acemoglu/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Daron_Acemoglu/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Daron_Acemoglu_zh`、`VIDEO_NAME=Daron_Acemoglu_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Acemoglu 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | political economy | 政治经济学 | infobox Discipline 首位；制度与民主研究纲领核心 | 封面、核心页 |
| 1 | development economics | 发展经济学 | 国家间繁荣差异的比较研究 | 核心页 |
| 2 | economic growth | 经济增长 | 《现代经济增长引论》教材；增长理论 | 增长页 |
| 3 | labor economics | 劳动经济学 | 机器人与就业、自动化与工资不平等 | 劳动页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 20 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Kevin W. S. Roberts | 师→生（博士导师） | LSE 博士导师（1992） |
| influence | Joel Mokyr | 无向 | infobox Influences 明载，技术史与制度 |
| influence | Kenneth Sokoloff | 无向 | infobox Influences 明载 |
| influence | Douglass North | 无向 | infobox Influences 明载，制度经济学奠基 |
| influence | Seymour Martin Lipset | 无向 | infobox Influences 明载 |
| influence | Barrington Moore Jr. | 无向 | infobox Influences 明载，书名致敬其 1966 著作 |
| co-honored | James A. Robinson | 无向 | 2024 诺贝尔经济学奖三人共享（制度如何形成并影响繁荣） |
| co-honored | Simon Johnson | 无向 | 2024 诺贝尔经济学奖三人共享（制度如何形成并影响繁荣） |
| collaborator | James A. Robinson | 无向 | 长期合著三书：独裁与民主的经济起源（2006）/ 国家的失败（2012）/ 窄廊（2019） |
| collaborator | Simon Johnson | 无向 | 合著殖民地起源（2001）与 Power and Progress（2023） |
| collaborator | Philippe Aghion | 无向 | 2001 合著去工会化与技能偏向型技术变革 |
| collaborator | Pascual Restrepo | 无向 | 合著机器人与就业（2020）、自动化与工资不平等（2022） |
| advisor-student | Robert Shimer | Acemoglu → 学生 | 博士生（infobox 明载） |
| advisor-student | Mark Aguiar | Acemoglu → 学生 | 博士生（infobox 明载） |
| advisor-student | Pol Antràs | Acemoglu → 学生 | 博士生（infobox 明载） |
| advisor-student | Gabriel Carroll | Acemoglu → 学生 | 博士生（infobox 明载） |
| advisor-student | Melissa Dell | Acemoglu → 学生 | 博士生（infobox 明载） |
| advisor-student | Benjamin Jones | Acemoglu → 学生 | 博士生（infobox 明载，经济学家） |
| advisor-student | Ufuk Akcigit | Acemoglu → 学生 | 博士生（infobox 明载） |
| spouse | Asuman Özdağlar | 无向 | MIT 电气工程与计算机科学教授，两人合著多篇文章 |

**不入库但提示词可叙述**：两位儿子 Arda 与 Aras（page.md 具名但未成年亲属按惯例不入库）；James Malcomson（博士论文考官，其评语「七章中最弱的三章已远超博士学位所需」可引，非导师非合作者非关系类型）；Erdoğan 政府 OECD 代表任命之辞（一次性事件）；Pashinyan/Kılıçdaroğlu 等政界互动（政治敏感禁写，见第七节）。

## 五、配色方案 【人物专属】

- **气质**：宏阔、制度纵深、数据驱动的历史叙事
- **主色**：`#14324F`（manifest 预分配藏蓝——制度大厦的基石感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeInst` 制度与繁荣 — 藏蓝 `#14324F`
  - `badgeDemo` 民主与发展 — 青绿 `#175E54`
  - `badgeRobot` 机器人与劳动 — 琥珀 `#C07A2A`
  - `badgeNobel` 诺奖荣誉 — 金 `#C9A227`
- **背景母题**：制度的明暗分岔道路（汲取 vs 包容），呼应三人组的核心理论图式。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 制度经济学的挖掘者 / Daron Acemoglu 1967– + 四色 badge + 右上头像 + 国籍行（Turkey / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地伊斯坦布尔、教育 York BA 1989 /
    LSE MSc 1990·PhD 1992、任职 MIT 1993–、诺奖 2024、核心领域）
03  核心贡献概览 — 殖民地起源 / 制度持续性 / 民主与增长 / 机器人与劳动
04  伊斯坦布尔少年 (1967–1989) — 亚美尼亚裔家庭、Galatasaray 高中、York BA
05  LSE 神童 (1989–1992) — 25 岁前获 PhD；考官 Malcomson 评语；导师 Kevin W. S. Roberts
06  MIT 晋阶 (1993–2019) — 助理教授→1998 终身→2019 Institute Professor（MIT 最高教席）
07  殖民地起源（核心贡献页）— 2001 三人合著： settler mortality 自然实验；制度解释约四分之三收入差
08  汲取与包容 — Why Nations Fail（2012）：创造性破坏需要制度约束；英国 1689 例
09  独裁与民主的经济 origins（2006）— 精英承诺问题；书名致敬 Barrington Moore Jr.
10  民主与增长的实证 — 民主化长期提升人均 GDP 约 20%；收入与民主无因果（2008）
11  窄廊与红皇后 (2019) — 国家与社会力量平衡的自由理论
12  机器人与劳动 — 与 Restrepo：机器人暴露地区就业下降、工资不平等上升
13  2024 诺贝尔经济学奖 — 三人共享；第二位亚美尼亚裔、第三位土耳其籍诺奖得主；RePEc 十年最高被引
14  遗产与结尾 — 新制度经济学的当代旗手 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由表述 | 2024 三人共享**同一句** "for studies of how institutions are formed and affect prosperity"；勿写成「因《国家的失败》获奖」等转述；中译统一「表彰他们关于制度如何形成并影响繁荣的研究」 |
| 政治敏感红线 | Views 与 Political involvement 两节（Trump/Chávez/Putin 类比、Erdoğan 与土耳其政局、亚美尼亚政治、中国叙事、Sanders 团队评论、Bailout 请愿、Nordic model 论战）**全部禁写**；成稿只做学术立传，任何政要姓名与评价性表述不得出现 |
| 姓名拼写 | 全名 Kamer Daron Acemoğlu（ğ 带软音符）；目录/yaml 用 ASCII 形式 **Daron Acemoglu**（manifest 口径），tex 正文可写 Acemoğlu，但库内匹配键是 Daron Acemoglu |
| 影响者名单 | infobox Influences 五人（Mokyr/Sokoloff/North/Lipset/Moore）与正文 Research 节一致，全部入库 influence；Barrington Moore 规范名用 **Barrington Moore Jr.**（1966 书名来源） |
| 博士论文题 | 正文两处微差（Contracts and *Macroeconomic* Performance vs *Economic* Performance），infobox 为准用 *Essays in Microfoundations of Macroeconomics: Contracts and Macroeconomic Performance*（1992） |
| 学生名单 | 入库 infobox 七人；正文另有「已指导 60+ 博士生」总数勿当名单；Akcigit 在 infobox 与正文各出现一次（拼作 Akçiġit/Akcigit），统一 **Ufuk Akcigit** |
| 国籍口径 | 双重公民 Turkey + United States（infobox Citizenship）；亚美尼亚裔是族裔背景非国籍，可客观提及 |
| 荣誉年份 | Clark Medal 2005 / Nemmers 2012 / BBVA 2016 / 诺奖 2024 勿串年；von Neumann Award 2007 是 Rajk László College 颁发，非计算机界同名奖 |
| 被引数据 | RePEc 2015「过去十年最高被引经济学家」、Google Scholar 2024-11 约 25 万次——两数字来源与口径不同，勿混写 |
| 合著边界 | 与 Robinson 是 co-honored + collaborator 双边；与 Johnson 是 co-honored + collaborator 双边；Aghion/Restrepo 仅 collaborator；配偶 Özdağlar 是「合著文章+配偶」仅入 spouse |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| extractive institutions | 汲取型制度 | 与 inclusive 相对，勿译「榨取」 |
| inclusive institutions | 包容型制度 | 获奖研究核心词 |
| settler mortality | 定居者死亡率 | 殖民地起源论文的工具变量 |
| creative destruction | 创造性破坏 | 借用熊彼特概念 |
| critical juncture | 关键节点 | 制度分岔的历史时刻 |
| new institutional economics | 新制度经济学 | 学术流派归属 |
| natural experiment | 自然实验 | 方法论关键词 |
| Red Queen effect | 红皇后效应 | 窄廊一书概念 |
| Institute Professor | 学院教授 | MIT 最高教席荣誉 |
| skill-biased technical change | 技能偏向型技术变革 | 与 Aghion 合著论文术语 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配，`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`）
- **匹配理由**：制度研究本身就是「长时段」的学问——数百年的殖民史与制度持续性；Timeless 的沉稳纪录片气质匹配「制度如何跨越世纪塑造繁荣」的叙事纵深，也呼应其《现代经济增长引论》的教科书式体系感。
- **本地路径**：复制 wav 到 `economics/presentations/21th_century/Daron_Acemoglu/Timeless.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、执行清单 【模板通用】

1. 读本提示词 + `Kenneth_G_Wilson_zh.tex` 骨架，建目录 `economics/presentations/21th_century/Daron_Acemoglu/`；
2. 从 images.txt / Commons 下载肖像（250px→500px），404 则装饰圆占位；
3. 复制 Makefile 设 `MAIN=Daron_Acemoglu_zh`、`VIDEO_NAME=Daron_Acemoglu_zh`；
4. 写 tex（配色按第五节、Slide 序列按第六节），每写一页 `make` 查溢出（0 error、vbox≤10pt、hbox≤50pt）；
5. `make pdf` → `pdftoppm` 逐页目检 → `make images` → `make video` 出 mp4；
6. 全程遵守第七节陷阱表；引语仅限 page.md 载有英文原文者（引原文+译文），无原文不得造「原话」；政治内容零出现。
