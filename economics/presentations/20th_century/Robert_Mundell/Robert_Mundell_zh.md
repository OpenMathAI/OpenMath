# 经济学家立传提示词（Robert Mundell）

> 本文件是 OpenMathAI OpenEcon 项目 20 世纪诺贝尔经济学奖 **1999 年得主 Robert Mundell（罗伯特·蒙代尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Robert_Mundell/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Robert Alexander Mundell（1932-10-24 生于加拿大安大略省金斯顿 ~ 2021-04-04 逝于意大利锡耶纳，享年 88 岁）
- **气质关键词**：**最优货币区之父、"欧元之父"、供给学派的启动者**
- **诺奖获奖理由**（1999 独得，逐字引用）：
  > "for his analysis of monetary and fiscal policy under different exchange rate regimes and his analysis of optimum currency areas"（表彰他对不同汇率制度下货币与财政政策的分析，以及对最优货币区域的分析）
- **设计母题**：**三难选择（trilemma）**——货币政策自主、固定汇率、资本自由流动三者不可兼得，视觉隐喻：三角形的三个顶点只能同时点亮两个；另一翼是最优货币区向欧元硬币的收束。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Robert_Mundell/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/20th_century/Robert_Mundell/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Robert_Mundell_zh`、`VIDEO_NAME=Robert_Mundell_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Mundell 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | monetary economics | 货币经济学 | infobox Discipline；货币动态学 | 封面、核心页 |
| 1 | international economics | 国际经济学 | 著作 *International Economics*（1968） | 核心页 |
| 2 | optimum currency areas | 最优货币区 | 诺奖理由后半句；欧元理论根基 | 核心页 |
| 3 | macroeconomic policy | 宏观经济政策 | Mundell–Fleming 模型：汇率制度下的货币财政政策 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 8 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Charles Kindleberger | Kindleberger → Mundell | MIT 博士导师（infobox 明载） |
| advisor-student | Jacob A. Frenkel | Mundell → 学生 | infobox Doctoral students 明载 |
| advisor-student | Rudi Dornbusch | Mundell → 学生 | infobox Doctoral students 明载 |
| advisor-student | Carmen Reinhart | Mundell → 学生 | infobox Doctoral students 明载 |
| collaborator | Marcus Fleming | 无向 | 1962 合著 Mundell–Fleming 汇率模型 |
| controversy | Milton Friedman | 无向 | 通胀与货币问题上的著名 point/counterpoint 交锋 |
| spouse | Valerie Natsios-Mundell | 无向 | 结缡 20 余年，1997 年得一子，居锡耶纳蒙特里久尼 35 年 |
| parent-child | William Mundell | 父 → Mundell | 军官，执教加拿大皇家军事学院 |
| parent-child | Lila Teresa Hamilton | 母 → Mundell | 遗产继承人 |

（注：共 8 个对手方 9 行——Frenkel/Dornbusch/Reinhart 三学生 + 导师 + Fleming + Friedman + 配偶 + 双亲，实际入库 9 行。）

**不入库但提示词可叙述**：1997 年出生的儿子（无具名不入库）；"famously the uncle of Nick"（无姓氏信息）；任职机构 IMF/世行/欧盟委员会/美联储理事会/美国财政部等（机构不建人物边）；Greg Palast 批评（见陷阱表）。

## 五、配色方案 【人物专属】

- **气质**：宏大、体系、国际货币秩序的设计师
- **主色**：`#14324F`（manifest 预分配——深夜蓝，布雷顿森林与全球货币体系的深水底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMon` 货币动态学 — 深蓝 `#14324F`
  - `badgeOCA` 最优货币区 — 靛蓝 `#372A75`
  - `badgeMF` Mundell–Fleming — 青绿 `#0E7C7B`
  - `badgeEuro` 欧元与政策 — 琥珀 `#C07A2A`
- **背景母题**：三难选择三角与货币区拼图（两个顶点点亮、一个熄灭；欧洲各国轮廓收束为单一硬币），呼应 trilemma 与最优货币区。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 最优货币区之父 / Robert Mundell 1932–2021 + 四色 badge + 右上头像 + 国籍行（Canada）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒金斯顿/锡耶纳、UBC BA、MIT PhD、
    导师 Kindleberger、任职芝加哥/滑铁卢/哥伦比亚/香港中文、诺奖 1999）
03  核心贡献概览 — Mundell–Fleming 模型 / 三难选择 / 最优货币区 / 供给学派
04  安大略农场少年 (1932–1950s) — 金斯顿出生、二战后迁 BC、拳击与棋弈
05  从 UBC 到 MIT — 经济学与俄语 BA、华盛顿大学奖学金、MIT 博士（兼读 LSE）、导师 Kindleberger
06  IMF 与芝加哥 (1961–1972) — 1961 入 IMF；1962 与 Fleming 合著模型；芝大教授兼 JPE 主编
    （页内两说 1965–72/1966–71，择一并保持一致）
07  Mundell–Fleming 模型（核心贡献页）— IS/LM 的开放经济扩展；三难选择：
    货币自主/固定汇率/资本自由流动三者至多取二
08  最优货币区理论 — 单一货币区依赖相近价格稳定；欧洲货币联盟的理论根基
09  "欧元之父" — 1960s 起推动欧洲经货联盟；欧元的智力奠基人
10  供给学派的启动 — 1971 普林斯顿小册子 The Dollar and the Policy Mix；
    预言 1970s 通胀与滞胀；1974 主张大幅减税与平准税率
11  与 Friedman 的交锋 — 布雷顿森林解体归因的 point/counterpoint；
    浮动汇率下货币扩张只能来自国际收支顺差的判断
12  哥伦比亚岁月与政策顾问 (1974–2021) — University Professor 2001；UN/IMF/世行/欧盟委员会/
    美联储/财政部顾问；香港中文大学杰出教授
13  荣誉与认可 — 诺奖 1999（演讲 A Reconsideration of the Twentieth Century：世纪三分）、
    Guggenheim 1971、加拿大勋章同伴 2002、Kiel 全球经济奖 2005、中关村蒙代尔国际企业家大学命名
14  遗产与结尾 — 欧元与开放经济宏观的结构框架 + 结尾页（2021-04-04 逝于锡耶纳，胆管癌）
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 芝加哥任期页内两说 | 一处作 "professor of economics and editor of the JPE at the University of Chicago from 1965 to 1972"，另一处作 "from 1966 to 1971"——幻灯片择一口径并全篇一致，勿混排 |
| "欧元之父"表述 | page.md 明载 "known as the 'father' of the euro" 可用；但 2000s 他的一系列预测（欧元区扩至 50 国等）未兑现——可客观一句，勿渲染 |
| Palast 批评 | Greg Palast 2012 "evil genius of the euro" 系单一作者观点，如引用须与 Mundell 本人 2014 反对财政 union 的立场并列呈现，勿单侧叙事；宁可不展开 |
| 2014 引语 | "it would be insane to have a central European authority that controls all the taxes..." 是 page.md 载英文原话，可引；勿改写为其他场合 |
| 诺奖理由与供给学派 | 获奖理由是汇率制度+最优货币区（非供给学派）；正文明言 "in economics it is for his work on currency areas... that he was awarded"；供给学派只是其获奖演讲中显著呈现——勿写成"因供给学派获奖" |
| 世纪三分 | 诺奖演讲把 20 世纪分三段（至大萧条/二战至 1973/其后通胀纪元），讲稿结论句 "the international monetary system depends only on the power configuration..." 可引原文 |
| Frontmatter 顾问名 | frontmatter 作 Charles Poor Kindleberger，infobox 与正文作 Charles Kindleberger——yaml 用 infobox 形式 'Charles Kindleberger' |
| 死因 | 2021-04-04 逝于意大利锡耶纳，胆管癌（cholangiocarcinoma），享年 88——客观一句 |
| Letterman 等电视节目 | 页面 Television appearances 一节为趣闻，幻灯片至多一行或省略，勿喧宾夺主 |
| 国籍 | 加拿大；逝于意大利但不改国籍 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Mundell–Fleming model | 蒙代尔–弗莱明模型 | IS/LM 的开放经济扩展；与 Fleming 合著（1962） |
| trilemma | 三难选择 | 三目标至多取二，勿写成"两难" |
| optimum currency area | 最优货币区 | 诺奖理由后半句核心词 |
| exchange rate regime | 汇率制度 | 诺奖理由前半句核心词 |
| supply-side economics | 供给学派 | 其 1971 小册子被视为奠基，但非获奖理由 |
| Bretton Woods system | 布雷顿森林体系 | 纪律更多来自美联储而非黄金 |
| stagflation | 滞胀 | 其对脱离布雷顿森林后果的预言 |
| Mundell–Tobin effect | 蒙代尔–托宾效应 | 与托宾名字共享的效应，非合作 |
| capital flows | 资本流动 | 三难选择的第三个顶点 |
| gold standard | 金本位 | 其历史研究主题 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**："怀旧"贴合其诺奖演讲《对 20 世纪的再思考》——把整个世纪切成三段的宏观史观；也呼应布雷顿森林时代一去不返的秩序感与托斯卡纳乡居的晚年。
- **本地路径**：复制 `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` 到 `economics/presentations/20th_century/Robert_Mundell/Nostalgia.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
