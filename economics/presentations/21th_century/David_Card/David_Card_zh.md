# 经济学家立传提示词（David Card）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2021 年得主 David Card（戴维·卡德）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/David_Card/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：David Edward Card（1956 生于加拿大安大略省圭尔夫，在世，卒年留白）
- **气质关键词**：**最低工资的实证颠覆者、自然实验的开拓者、劳动经济学的"可信度革命"旗手**
- **诺奖获奖理由**（2021 拆分理由：Card 独得一半；Angrist 与 Imbens 共享另一半。英文逐字引自 `economics/nobel_economics_citations.json` 2021 David Card 条目）：
  > "for his empirical contributions to labour economics"（表彰他对劳动经济学的实证贡献）
  > ——中译对照 `economics/economics_list_data.py` 2021 年 `||` 拆分第一段。
- **设计母题**：**自然实验与对照（natural experiment & counterfactual）**——新泽西与宾州快餐店的最低工资对照，是「同一时刻两条平行世界曲线」的视觉隐喻：左右分屏的双柱/双曲线构图构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/David_Card/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/David_Card/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=David_Card_zh`、`VIDEO_NAME=David_Card_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Card 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | labour economics | 劳动经济学 | Discipline 明载；2021 诺奖获奖理由核心词 | 封面、核心页 |
| 1 | economics of education | 教育经济学 | 学校资源/受教育年限对长期收入的影响 | 教育页 |
| 2 | immigration economics | 移民经济学 | Mariel boatlift 研究：新移民对工资影响极小 | 移民页 |
| 3 | empirical microeconomics | 实证微观经济学 | BBVA 评审词 "contributions to empirical microeconomics" | 方法页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Orley Ashenfelter | Ashenfelter → Card | 普林斯顿博士导师，论文 "Indexation in long term labor contracts"（1983） |
| advisor-student | Thomas Lemieux | Card → 学生 | infobox Doctoral students 明载 |
| advisor-student | Phillip B. Levine | Card → 学生 | infobox 明载 |
| advisor-student | Christoph M. Schmidt | Card → 学生 | infobox 明载 |
| advisor-student | Michael Greenstone | Card → 学生 | infobox 明载 |
| advisor-student | Jesse Rothstein | Card → 学生 | infobox 明载 |
| advisor-student | Philip Oreopoulos | Card → 学生 | infobox 明载 |
| advisor-student | David Lee | Card → 学生 | infobox 明载；economist（防同名，勿与物理侧 David Lee 混淆） |
| advisor-student | Janet Currie | Card → 学生 | infobox 明载 |
| advisor-student | Enrico Moretti | Card → 学生 | infobox 明载 |
| advisor-student | Heather Royer | Card → 学生 | infobox 明载 |
| advisor-student | Elizabeth Cascio | Card → 学生 | infobox 明载 |
| advisor-student | Ethan G. Lewis | Card → 学生 | infobox 明载 |
| advisor-student | Nicole Maestas | Card → 学生 | infobox 明载 |
| collaborator | Alan B. Krueger | 无向 | 时任普林斯顿同事；最低工资快餐店自然实验与《Myth and Measurement》（1995）合著者 |
| co-honored | Joshua Angrist | 无向 | 2021 诺奖同届：Card 独得一半，Angrist 与 Imbens 共享另一半 |
| co-honored | Guido Imbens | 无向 | 2021 诺奖同届：Card 独得一半，Angrist 与 Imbens 共享另一半 |
| co-honored | Richard Blundell | 无向 | 2014 BBVA Foundation Frontiers of Knowledge Award（经济金融与管理类）共同得主 |
| colleague | N. Gregory Mankiw | 无向 | 两人共同当选 2014 年度美国经济学会（AEA）副主席 |

**不入库但提示词可叙述**：Joseph Stiglitz 与 Paul Krugman（正文仅说"接受其发现"，非持续关系）； Steven Raphael（论文集合编者，仅参考文献列表）；Rebecca Blank / Richard B. Freeman / Giovanni Peri 等合编者（仅参考文献列表，无正文合作叙述）；Harvard 招生案（仅专家证人事件）。

## 五、配色方案 【人物专属】

- **气质**：务实、严谨、以数据说话的"可信度革命"
- **主色**：`#0E4D64`（manifest 预分配——深青蓝，劳动市场的冷静实证感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeLabour` 劳动经济学 — 深青蓝 `#0E4D64`
  - `badgeWage` 最低工资研究 — 琥珀 `#C07A2A`
  - `badgeImmi` 移民经济学 — 灰紫 `#52307C`
  - `badgeEdu` 教育经济学 — 青绿 `#0E7C7B`
- **背景母题**：左右分屏的对照柱形与平行折线（新泽西 vs 宾州的差分构图），呼应「自然实验」的核心方法。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 劳动经济学的实证颠覆者 / David Card 1956– + 四色 badge + 右上头像 + 国籍行（Canada / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年 1956 圭尔夫、Queen's BA 1978、Princeton PhD 1983、
    任职 UC Berkeley（1997 起，Class of 1950 Professor）、诺奖 2021、核心领域）
03  核心贡献概览 — 最低工资自然实验 / 移民经济学 / 教育经济学 / 实证方法革命
04  早年：奶牛场之子 (1956–1978) — 圭尔夫出生，John F. Ross 中学 1970–75，本科原学物理后转经济，Queen's BA 1978
05  普林斯顿博士 (1978–1983) — 导师 Orley Ashenfelter，论文《Indexation in long term labor contracts》
06  最低工资的自然实验（核心贡献页）— 新泽西 vs 宾州快餐店对照、difference in differences、
    "最低工资上涨未减少快餐业就业"
07  《Myth and Measurement》(1995) — 与 Krueger 合著；对 90% 经济学家共识的挑战与后续证实
08  移民经济学：Mariel boatlift — 迈阿密低技能劳动力骤增 7% 而工资未受显著影响
09  教育经济学 — 大学邻近度工具变量、班级规模与学校资源对长期收入的影响
10  荣誉：Clark Medal 到 Nobel — 1995 Clark / 2006 IZA / 2008 Frisch / 2014 BBVA（与 Blundell）/ 2019 Mincer
11  2021 诺贝尔经济学奖 — 一半独得："for his empirical contributions to labour economics"；
    Angrist 与 Imbens 共享另一半（同届拆分示意）
12  期刊编辑与学会服务 — JoLE 副编辑 1988–92、Econometrica co-editor 1993–97、AER co-editor 2002–05、
    2014 AEA 副主席（与 Mankiw 同届当选）
13  学术风格与立场 — 只做实证、不公开站队政策；"对移民的经济反对论据是二阶的"（NYT 访谈原文）
14  遗产与结尾 — 可信度革命确立 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生年双值 | frontmatter `date_of_birth: ["1956-00-00", "1955-11-30"]` 系噪声；正文只说 born 1956（Guelph, Ontario），**月日不写**，幻灯片写 "1956–" |
| 2021 拆分理由 | Card **独得一半**，Angrist 与 Imbens 共享另一半；获奖理由只写本人那句 "for his empirical contributions to labour economics"，勿把 Angrist/Imbens 的 "for their methodological contributions..." 混入 Card 篇 |
| 国籍口径 | yaml 按 manifest "Canada / United States" 拆两条；frontmatter nationality 只有 Canada，正文作 Canadian-American，以 manifest+正文口径为准 |
| Krueger 表述 | page.md 只载"当时普林斯顿同事 + 合著者"；Krueger 的生卒/去世 page.md 无载，**禁写** |
| Mariel 数字 | 迈阿密低技能劳动力增加 7%，低技能工资未受显著影响、整体失业率与工资不变——数字按 page.md 原文，勿夸大 |
| 引语红线 | 可引原文仅两处：NYT 访谈 "I honestly think the economic arguments [against immigration] are second order. They are almost irrelevant."（引原文+译文）；Clark Medal 授奖词 "that American economist under the age of forty..."（引原文+译文）。其余叙述不得加中文引号冒充原话 |
| 学生名单 | infobox Doctoral students 13 人全部明载、全部入库；David Lee 须注 "(economist)" 语义防同名混淆 |
| Stiglitz/Krugman | 正文仅说其"接受发现"，不建关系边；Harvard 招生案只客观叙述专家证人身份 |
| 自然实验归属 | 差分中的差分（difference in differences）方法学页.md 说 "its claim have been disputed"——争议客观带过，勿写成"方法公认无争议" |
| 诺奖研究口径 | 正文 Awards 节口径：研究显示最低工资上涨不导致雇佣减少、移民不降低本地工人工资——与获奖理由分两处呈现，勿互相替换 |
| metadata 噪声 | metadata.json description "Canadian economist and university teacher (born 1956)"，与正文一致可放心引用 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| natural experiment | 自然实验 | 与受控实验对照，方法论关键词 |
| difference in differences | 双重差分 | Card–Krueger 快餐店研究的核心方法 |
| minimum wage | 最低工资 | 获奖理由落点之一，勿写"工资下限"泛称 |
| Mariel boatlift | 马列尔偷渡事件 | 1980 古巴移民潮，移民经济学代表作 |
| instrumental variable | 工具变量 | 教育经济学中"大学邻近度"IV |
| labour economics | 劳动经济学 | 获奖理由用英式拼写 labour（官方原文），勿改成 labor |
| empirical microeconomics | 实证微观经济学 | BBVA 评审词原文 |
| credibility revolution | 可信度革命 | Imbens 页有此词条，Card 篇按正文口径谨慎转述 |
| John Bates Clark Medal | 约翰·贝茨·克拉克奖章 | 1995，授奖词限"四十岁以下美国经济学家" |
| spillover effect | 溢出效应 | 《Myth and Measurement》结论用词 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**："探路者"契合 Card 以自然实验为经济学开辟实证新路的形象——最低工资与移民研究都是在无人区先行、再被后来者证实的探路叙事；曲风的推进感匹配"可信度革命"的层层推进。
- **本地路径**：复制 `music_audio/inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav` 到 `economics/presentations/21th_century/David_Card/Pathfinder.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/David_Card/page.md` | ★ 事实基准（唯一事实来源） |
| `economics/presentations/pages/21th_century/David_Card/metadata.json` | QID/生卒/国籍结构化参考（冲突以 page.md 为准） |
| `economics/presentations/pages/21th_century/David_Card/images.txt` | 肖像候选 URL（page.md 引用 "Card in 2021" 照） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 共享封面（`\input`） |
| `MySQL/data/David_Card.yaml` | 社会关系/研究领域入库存档（本批次已入库） |
| `economics/nobel_economics_citations.json` | 2021 拆分获奖理由英文原文（Card 条目） |
| `economics/economics_list_data.py` | 2021 年中译对照（`||` 拆分第一段） |

## 十一、执行清单（供 Beamer agent 核对） 【模板通用】

1. 核对事实基准：所有事实与 page.md 逐条对照，冲突一律以 page.md 为准并在陷阱表记录裁定。
2. 复制 Makefile：`MAIN=David_Card_zh`、`VIDEO_NAME=David_Card_zh`。
3. 肖像：优先 images.txt 真实肖像（"Card in 2021"）；404 则装饰圆占位（勿用无授权图）。
4. 配色：主色 `#0E4D64` + badge 四色 + 背景母题（新泽西 vs 宾州分屏对照柱形）。
5. 幻灯片序列：按第六节 15 页规划，第 02 页身份信息页必做。
6. 编译循环：`make distclean && make`，0 error、vbox ≤ 10pt、hbox ≤ 50pt；pdftoppm 逐页目检。
7. 引语红线：只有第七节列出的两处 page.md 原文可入引文框（引原文+译文），其余叙述不加中文引号。
8. 结尾页品牌口径：底部标注 `OpenMathAI`（与共享 GitHub 一致），引号用半角 " "。
9. 完成后 `make images && make video` 产出 mp4，向主控汇报页数与体积。

## 十二、版式补遗 【模板通用】

- **共享封面**：第 00 页 `\input` OpenEcon 统一封面，子 deck 不重复 GitHub 链接。
- **封面页**：主标题字号沿用模板；badge 主字体 scriptsize、副行 `\fontsize{6.5}{7.8}`；右上肖像细边框 + 姓名小字注。
- **身份信息页**：左头像 + 右信息网格，含至少生年/出生地/教育/师承/任职/主要荣誉/核心领域七要素。
- **表格页安全负间距**：顶部 -0.35cm、`arraystretch 0.78-0.82`、公式框前 -0.35~-0.55cm；拥挤时 `itemize` 的 `topsep=0pt`。
- **时间线页**：`\foreach` 分隔符必须 ASCII 逗号；勿给 foreach 节点套 tikz style。
- **年份留白**：在世者卒年一律 "1956–"；生年不写月日（page.md 正文无载）。
- **获奖理由引用框**：英文原句 + 中文翻译两行制，英文逐字来自 `nobel_economics_citations.json`。

## 十三、关键时间线速查 【人物专属】

| 年份 | 事件（均出自 page.md） |
|------|------|
| 1956 | 生于加拿大安大略省圭尔夫（Guelph），奶牛场家庭 |
| 1970–1975 | 就读 John F. Ross Collegiate Vocational Institute |
| 本科 | 原修物理，后转经济学 |
| 1978 | Queen's University（Kingston）文学士毕业 |
| 1982–1983 | 芝加哥大学商学研究生院商业经济学助理教授 |
| 1983 | 普林斯顿经济学博士；论文 "Indexation in long term labor contracts"（导师 Orley Ashenfelter） |
| 1983–1997 | 普林斯顿大学任教 |
| 1988–1992 | Journal of Labor Economics 副编辑 |
| 1990–1991 | 哥伦比亚大学访问教授 |
| 1990 年代初 | 与 Alan B. Krueger 新泽西最低工资快餐店研究引发广泛关注 |
| 1993–1997 | Econometrica 联合主编 |
| 1995 | 约翰·贝茨·克拉克奖章；《Myth and Measurement》出版 |
| 1997 至今 | UC Berkeley（Class of 1950 Professor of Economics） |
| 2002–2005 | American Economic Review 联合主编 |
| 2006 / 2008 | IZA 劳动经济学奖 / Frisch Medal |
| 2009 | 美国经济学会 Richard T. Ely Lecture（旧金山） |
| 2014 | BBVA Frontiers of Knowledge Award（与 Blundell 共同）；与 Mankiw 同届当选 AEA 副主席 |
| 2018 | 哈佛招生案出庭专家证人 |
| 2019 | Jacob Mincer Award；2011 年调查评为"60 岁以下第五受欢迎在世经济学家" |
| 2021 | 当选美国国家科学院院士；诺贝尔经济学奖（独得一半） |

> 表内每条均有 page.md 明载；「本科」一栏无年份，按原文叙述呈现即可。
