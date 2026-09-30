# 经济学家立传提示词（Milton Friedman）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1976 年得主 Milton Friedman（米尔顿·弗里德曼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Milton_Friedman/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Milton Friedman（1912-07-31 生于纽约布鲁克林 ~ 2006-11-16 逝于旧金山，享年 94 岁）
- **气质关键词**：**货币主义的旗手、芝加哥学派的领袖、二十世纪后半叶最具影响力的经济学家**
- **诺奖获奖理由**（1976 独得，逐字引用 manifest）：
  > "for his achievements in the fields of consumption analysis, monetary history and theory and for his demonstration of the complexity of stabilisation policy"（表彰他在消费分析、货币史与货币理论领域的成就，以及他对稳定化政策复杂性的论证）
- **设计母题**：**货币之流（money supply）**——恒定小步扩张的货币流与「直升机撒钱」意象：金色流线与错落圆构成背景母题，呼应「通货膨胀在任何时空都是货币现象」的核心论断。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Milton_Friedman/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Milton_Friedman/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 取，如 Milton_Friedman_1976.jpg，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Milton_Friedman_zh`、`VIDEO_NAME=Milton_Friedman_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Friedman 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | macroeconomics | 宏观经济学 | infobox Discipline；货币主义的大本营 | 封面、核心页 |
| 1 | monetary economics | 货币经济学 | 现代数量论/货币主义，诺奖核心 | 核心页 |
| 2 | consumption analysis | 消费分析 | 永久收入假说（1957），诺奖理由之一 | 核心页 |
| 3 | statistics | 统计学 | 序贯抽样、Friedman test；职业身份 statistician | 方法页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Simon Kuznets | Friedman → 学生 | NBER 期间师从合著职业收入研究；infobox 列为博士导师 |
| advisor-student | Phillip Cagan | Friedman → 学生 | infobox Doctoral students 明载 |
| advisor-student | Harry Markowitz | Friedman → 学生 | infobox Doctoral students 明载 |
| advisor-student | Lester G. Telser | Friedman → 学生 | infobox Doctoral students 明载 |
| advisor-student | David I. Meiselman | Friedman → 学生 | infobox Doctoral students 明载 |
| advisor-student | Neil Wallace | Friedman → 学生 | infobox Doctoral students 明载 |
| advisor-student | Miguel Sidrauski | Friedman → 学生 | infobox Doctoral students 明载 |
| advisor-student | Edgar L. Feige | Friedman → 学生 | infobox Doctoral students 明载 |
| advisor-student | Thomas Sowell | Friedman → 学生 | infobox Doctoral students 明载 |
| influence | Gary S. Becker | 无向 | 芝加哥招募/指导的门生，1992 诺奖得主 |
| influence | Robert Fogel | 无向 | 芝加哥招募/指导的门生，1993 诺奖得主 |
| influence | Robert Lucas | 无向 | 芝加哥招募/指导的门生，1995 诺奖得主 |
| influence | Jacob Viner | 无向 | 芝加哥硕士阶段深受影响的老师 |
| influence | Frank Knight | 无向 | 芝加哥硕士阶段深受影响的老师 |
| influence | Henry Calvert Simons | 无向 | 芝加哥硕士阶段深受影响的老师 |
| influence | Harold Hotelling | 无向 | 哥伦比亚 fellowship 年师从习统计 |
| influence | Henry Schultz | 无向 | 曾任其研究助理（《需求理论与测量》时期） |
| influence | Jeremy Bentham | 无向 | infobox Influences 明载 |
| influence | Henry George | 无向 | infobox Influences 明载 |
| influence | Friedrich Hayek | 无向 | infobox Influences 明载 |
| influence | Homer Jones | 无向 | 终身挚友兼思想影响者（正文一处作 Homer Johnson 系拼写差异） |
| influence | Adam Smith | 无向 | infobox Influences 明载 |
| influence | Karl Marx | 无向 | infobox Influences 明载 |
| influence | John Maynard Keynes | 无向 | infobox Influences 明载（对话与论战的靶心） |
| colleague | George Stigler | 无向 | 芝加哥学派共同领袖、终身挚友 |
| colleague | Arthur F. Burns | 无向 | NBER 主任邀其重返，主持货币与商业周期研究 |
| colleague | W. Allen Wallis | 无向 | 终身挚友，战时哥伦比亚战争研究部共事 |
| collaborator | Anna Schwartz | 无向 | 合著《美国货币史（1867–1960）》（1963） |
| spouse | Rose Friedman | 无向 | 芝加哥相遇结为夫妻，合著《自由选择》《两个幸运的人》 |
| parent-child | David D. Friedman | Friedman → 子 | 经济学家，《The Machinery of Freedom》作者 |
| parent-child | Jan Martel | Friedman → 子 | 律师与桥牌选手 |
| controversy | Gunnar Myrdal | 无向 | 1976 授奖争议中公开批评弗里德曼（连带批评 Hayek） |

**不入库但提示词可叙述**：父母 Sára Ethel Landau 与 Jenő Saul Friedman（匈牙利裔移民干货商，仅具名无条目）；Paul Samuelson（1968–1978 同参与 Economics Cassette Series，一次性项目弱关系）；Ben Bernanke（在致敬演讲中认账「你们是对的，是我们干的」——事件叙述非关系）；Edmund Phelps（自然失业率并列归属，学术并列非人际）；Robert Lucas 另有理性预期对弗里德曼适应性预期的学术演进（influence 边已覆盖门生面，禁再建 controversy）；Anna Schwartz 的批评者 Kaldor/Hendry/Temin/Krugman 等仅是学术批评事件。

## 五、配色方案 【人物专属】

- **气质**：锐利、雄辩、市场信念的暖金
- **主色**：`#372A75`（深紫——货币理论的深邃与雄辩锋芒）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMoney` 货币主义 — 深紫 `#372A75`
  - `badgeIncome` 永久收入假说 — 靛蓝 `#283593`
  - `badgeStats` 统计学 — 青绿 `#0E7C7B`
  - `badgePolicy` 政策论战 — 玫瑰 `#C4204F`
- **背景母题**：金色流线与错落圆（货币供应恒定扩张之流）。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 货币主义的旗手 / Milton Friedman 1912–2006 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地布鲁克林、教育 Rutgers/芝加哥 MA/Columbia PhD 1946、
    任职 Chicago 1946–1977→Hoover Institution、诺奖 1976、核心领域）
03  核心贡献概览 — 永久收入假说 / 美国货币史 / 自然失业率 / 货币主义
04  移民之子 (1912–1932) — 布鲁克林出生、Rahway 长大、Rutgers 竞争奖学金、家中第一个大学生
05  芝加哥与哥伦比亚 (1932–1935) — Viner/Knight/Simons 的影响；Columbia 师从 Hotelling
06  华盛顿岁月与 NBER (1935–1941) — New Deal 时期政府工作、随 Kuznets 研究职业收入
07  战时统计学家 (1941–1945) — 财政部战时税收、哥伦比亚战争研究部、序贯抽样
08  芝加哥三十年 (1946–1977) — 接替 Viner 教席、货币与银行工作坊、芝加哥学派共同体
09  永久收入假说（核心贡献页）—《消费函数理论》1957、y = y_p + y_t
10  《美国货币史》（核心贡献页）— 与 Schwartz 合著 1963、大收缩 The Great Contraction、Bernanke 认账名言
11  菲利普斯曲线与自然率 — 1968 就职演说、与 Phelps 并列归属、滞胀预言
12  公共知识人 —《资本主义与自由》1962、《自由选择》1980、Newsweek 专栏 1966–84
13  1976 诺贝尔经济学奖 — 独得；授奖争议一段客观简述（Myrdal 批评）
14  遗产与结尾 — 「凯恩斯的时代让位于弗里德曼的时代」（Galbraith 语）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生卒与享年 | 1912-07-31 纽约布鲁克林生 ~ 2006-11-16 旧金山逝（心力衰竭），享年 94；卒后次日 WSJ 还刊其专栏（最后专栏） |
| 婚期两说 | infobox 作 m. 1936，正文作「1932 相遇六年后 1938 成婚」——page.md 内部冲突，yaml 不写婚年、提示词叙述用「1930 年代成婚」或并列两说 |
| 学位链 | Rutgers BA 1932 → 芝加哥 MA 1933 → **Columbia PhD 1946**（以 1940 完成的职业收入研究为博士论文）；博士导师栏 Kuznets 系 NBER 合作导师口径，勿写成「哥伦比亚导师」 |
| 影响者大表 | infobox Influences 16 人全部明载： ideology 类（Bentham/George/Smith/Marx/Keynes/Hayek/Jones）与师承类（Viner/Knight/Simons/Hotelling/Schultz/Kuznets/Burns/Stigler）分流入库（师承类部分另入 advisor/colleague 边，勿重复） |
| Homer Jones 拼写 | 正文一处作 "Homer Johnson"、infobox 链接为 Homer_Jones_(economist)——按 infobox 取 Homer Jones，陷阱表注明 |
| 门生三类 | infobox Doctoral students 8 人（advisor-student）；正文明载「招募或指导」的三位诺奖门生 Becker/Fogel/Lucas（influence，勿升格为博士导师）；对方 yaml 名字用 manifest 形式 Gary S. Becker/Robert Fogel/Robert Lucas |
| Keynes/Marx/Smith 复用 | 库内已有规范记录：John Maynard Keynes(850)、Karl Marx(5441)；Adam Smith/Henry George/Jeremy Bentham 库内无，新建 stub 用标准全名 |
| Richard Kahn 辨名 | 剑桥的 Richard Kahn（卡恩勋爵，乘数）库内不存在，与互联网先驱 Robert E. Kahn(260) 无关；本篇不建 Kahn 边（Friedman 无直接关系） |
| 1976 授奖争议 | 智利背景（1975 应邀访智讲学）与 Myrdal 批评按 page.md 客观简述：弗里德曼自辩「从未担任顾问、只讲学与见官员」；不展开政治评价、不作单侧叙事、正文引语只取 page.md 载明者 |
| 引语白名单 | 可用引语（page.md 载英文原文）："Inflation is always and everywhere a monetary phenomenon."（1963）；Bernanke "you're right, we did it..."；Rose "his achievement is my achievement"；其余议论禁杜撰原话 |
| 新闻周刊专栏 | 1966–84（正文），1968 获 Gerald Loeb Special Award；Cambridge 访问为 1954–55 Fulbright（Gonville and Caius） |
| 荣誉年份 | Clark Medal 1951；NAS 1973；National Medal of Science 与 Presidential Medal of Freedom 均 1988（勿拆年份）；Cato 的 Milton Friedman Prize 2002 起设 |
| The Economist 评语 | "the most influential economist of the second half of the 20th century ... possibly of all of it"（卒时讣闻，page.md 载原文可用） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| monetarism | 货币主义 | 与凯恩斯主义对举，勿译「货币学派」泛化 |
| permanent income hypothesis | 永久收入假说 | 1957《消费函数理论》核心 |
| natural rate of unemployment | 自然失业率 | 1968 提出；宏观语境下渐被 NAIRU 取代（说明性脚注） |
| The Great Contraction | 大收缩 | 1929–1933 特指，勿与 Great Depression 混用 |
| k-percent rule | k 百分比规则 | 货币供应恒率增长主张 |
| helicopter money | 直升机撒钱 | 思想实验意象，勿写实为政策建议 |
| Friedman–Savage utility function | 弗里德曼–萨维奇效用函数 | 与 Leonard Savage 合作成果，萨维奇非其导师 |
| sequential sampling | 序贯抽样 | 战时统计贡献（New Palgrave 评价可用） |
| floating exchange rates | 浮动汇率 | 1953《实行浮动汇率的主张》 |
| negative income tax | 负所得税 | 反贫困政策主张 |
| stagflation | 滞胀 | 其菲利普斯曲线批判的预言对象 |
| school vouchers | 教育券 | 1996 与 Rose 创立 Friedman Foundation（后更名 EdChoice） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从布鲁克林移民之子到「二十世纪下半叶最有影响力的经济学家」，弗里德曼的一生纵贯大萧条、二战、战后宏观革命与世纪末的思想转向——「时间之流」的叙事感贴合货币史家的身份：他毕生论证的正是时间序列中货币与经济的共生。
- **本地路径**：复制 `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav` 到 `economics/presentations/20th_century/Milton_Friedman/TheFlowOfTime.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
