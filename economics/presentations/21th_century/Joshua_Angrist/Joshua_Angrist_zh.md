# 经济学家立传提示词（Joshua Angrist）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2021 年得主 Joshua Angrist（约书亚·安格里斯特）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Joshua_Angrist/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Joshua David Angrist（1960-09-18 生于美国俄亥俄州哥伦布，在世，卒年留白；希伯来名 יהושע אנגריסט）
- **气质关键词**：**越战抽签的计量读心者、工具变量的旗手、可信度革命的代言人**
- **诺奖获奖理由**（2021 拆分理由：Angrist 与 Imbens 共享一半；Card 独得另一半。英文逐字引自 `economics/nobel_economics_citations.json` 2021 Joshua Angrist 条目）：
  > "for their methodological contributions to the analysis of causal relationships"（表彰他们对因果关系分析方法论的贡献）
  > ——中译对照 `economics/economics_list_data.py` 2021 年 `||` 拆分第二段。
- **设计母题**：**抽签与编号（draft lottery & quasi-randomness）**——越战征兵抽签日历是「天然随机化」的最佳视觉符号：以日历格中的抽签号码/骰子点阵为背景母题，呼应准实验设计。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Joshua_Angrist/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Joshua_Angrist/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Joshua_Angrist_zh`、`VIDEO_NAME=Joshua_Angrist_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Angrist 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 计量经济学 | Discipline 明载；LATE 框架与 IV 方法学 | 封面、核心页 |
| 1 | labour economics | 劳动经济学 | Discipline 明载；越战退伍军人收入研究 | 核心页 |
| 2 | economics of education | 教育经济学 | 教育回报/班级规模/特许学校研究主体 | 教育页 |
| 3 | urban economics | 城市经济学 | 正文列举的研究领域之一 | 领域页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Orley Ashenfelter | Ashenfelter → Angrist | 普林斯顿博士导师；论文 "Econometric Analysis of the Vietnam Era Draft Lottery"（1989） |
| advisor-student | David Card | Card → Angrist | infobox Other advisors 明载；同届诺奖另一半得主 |
| advisor-student | Whitney Newey | Newey → Angrist | infobox Other advisors 明载 |
| advisor-student | Esther Duflo | Angrist → 学生 | infobox Doctoral students 明载（2019 诺奖得主） |
| advisor-student | Jonah B. Gelbach | Angrist → 学生 | infobox Doctoral students 明载 |
| advisor-student | Melissa Kearney | Angrist → 学生 | infobox Doctoral students 明载 |
| advisor-student | Jeffrey R. Kling | Angrist → 学生 | infobox Doctoral students 明载 |
| co-honored | Guido Imbens | 无向 | 2021 诺奖共享一半："for their methodological contributions to the analysis of causal relationships" |
| co-honored | David Card | 无向 | 2021 诺奖同届：Angrist 与 Imbens 共享一半，Card 独得另一半 |
| collaborator | Guido Imbens | 无向 | 1994 LATE 论文合著；frequent co-author |
| collaborator | Alan B. Krueger | 无向 | frequent co-author：出生季节-受教育年限、征兵抽签 IV、二战退伍军人研究 |
| collaborator | Victor Lavy | 无向 | frequent co-author：以色列班级规模（Maimonides' rule）、摩洛哥教学语言研究 |
| collaborator | Parag Pathak | 无向 | frequent co-author：波士顿/纽约考试学校与特许学校抽签研究 |
| collaborator | Jörn-Steffen Pischke | 无向 | frequent co-author；合著《Mostly Harmless Econometrics》（2008）与《Mastering 'Metrics'》（2014） |
| collaborator | Daron Acemoglu | 无向 | 强制教育法与人力资本外部性、ADA 残疾人就业研究合作 |

**不入库但提示词可叙述**：Kathryn Graddy / Alberto Abadie / Victor Chernozhukov / Kevin Lang / William Evans / Adriana Kugler / Eric Bettinger / Michael Kremer / Susan Dynarski / Christopher Walters 等单项合作者（正文提及但不属 "frequent co-author" 列表，控制噪声不入库）；John H. Johnson IV（单篇合著）；Blueprint Labs 与 Avela 创业（机构非人物）。

## 五、配色方案 【人物专属】

- **气质**：锋利、机敏、以天然随机性破解因果谜题
- **主色**：`#0E4D64`（manifest 预分配——深青蓝，与本批三人同色系）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeEcon` 计量经济学 — 深青蓝 `#0E4D64`
  - `badgeLab` 劳动经济学 — 琥珀 `#C07A2A`
  - `badgeEdu` 教育经济学 — 青绿 `#0E7C7B`
  - `badgeDraft` 抽签与服役 — 灰紫 `#52307C`
- **背景母题**：日历格与抽签号码（1969-1970 越战征兵抽签日历的抽象化），呼应「天然随机化」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 越战抽签的计量读心者 / Joshua Angrist 1960– + 四色 badge + 右上头像 + 国籍行（United States / Israel）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（1960-09-18 生于哥伦布、Oberlin BA 1982、
    Princeton PhD 1989、MIT Ford 教授（2008 起）、诺奖 2021、核心领域）
03  核心贡献概览 — LATE 框架 / 越战抽签研究 / 教育回报的 IV 估计 / 计量教科书
04  早年与从军 (1960–1985) — 哥伦布出生、匹兹堡长大、Taylor Allderdice 中学 1977；Oberlin 1982；
    1982–85 居以色列并在以色列国防军伞兵旅服役
05  普林斯顿博士 (1985–1989) — 导师 Orley Ashenfelter（另有 David Card、Whitney Newey）；论文以越战征兵抽签为题
06  越战抽签与服役回报（核心贡献页）— 参战使退伍军人终身收入降低约 15%；GI 法案使受教育年限增加约 1.4 年
07  LATE 框架（与 Imbens）— 1994 Econometrica；从自然实验精确推断因果的方法论
08  教育回报的 IV 研究 — 与 Krueger：出生季节与强制教育法；受教育回报接近 OLS 估计
09  以色列学校实验 — Maimonides' rule 班级规模、教师培训、现金激励的性别差异
10  特许学校抽签研究 — KIPP Lynn 数学 +0.35 SD；"No Excuses" 城市特许学校解释
11  计量教科书 — 与 Pischke《Mostly Harmless Econometrics》(2008)、《Mastering 'Metrics'》(2014)
12  2021 诺贝尔经济学奖 — 与 Imbens 共享一半，Card 独得另一半；瑞典科学院长文引语（强制教育延长一年的因果难题）
13  荣誉与服务 — 2006 AAAS Fellow、2007 圣加仑荣誉博士、2011 John von Neumann Award；
    NBER/IZA/计量学会等机构隶属与七刊编辑职务
14  遗产与结尾 — 可信度革命的方法论基石 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 2021 拆分理由 | Angrist 与 Imbens **共享一半**（"for their methodological contributions..."），Card 独得另一半且理由不同；奖金 1000 万瑞典克朗的一半归两人平分——三条数字勿混 |
| 双导师列 | infobox Doctoral advisor 只列 Orley Ashenfelter；David Card、Whitney Newey 在 **Other advisors** 行——三条均入库，note 注明来源行 |
| Card 双重身份 | Card 既是 Angrist 的 infobox 副导师又是同届诺奖得主——建 advisor-student 与 co-honored 两条边，note 各自独立 |
| 以色列服役表述 | 1982–85 居以色列并在国防军**伞兵旅**服役；越战抽签研究是学术对象，勿与本人服役经历混淆 |
| 国籍口径 | manifest "United States / Israel"（dual US–Israeli citizenship，居 Brookline, MA）；frontmatter 同序 |
| 越战研究数字 | 参战使退伍军人终身收入比非退伍军人低约 15%；GI 法案使受教育年限提高约 1.4 年、退伍军人收入提高 6%——三组数字各有所指勿互换 |
| 引语红线 | 可引原文：瑞典科学院获奖解释长文（page.md 已录英文，从 "Data from a natural experiment are difficult to interpret..." 起）；"credibility revolution" 术语可在叙述中使用。其余叙述不加中文引号冒充原话 |
| frequent co-author | 正文明确列 5 人（Imbens/Krueger/Lavy/Pathak/Pischke）——此 5 人建 collaborator；Acemoglu 多次合作另建；其余单篇合作者一律不入库 |
| Duflo 学生身份 | Esther Duflo（2019 诺奖）是 Angrist infobox 明载博士生；未来若入库须复用此 stub 回填 |
| LATE 归属 | 与 Imbens 合著提出，勿写成独著；与 Rubin 的 IV 嵌入工作则另有 Imbens+Rubin 合著论文，两事勿并成一句 |
| 教科书数量 | 两本（Mostly Harmless Econometrics 2008 / Mastering 'Metrics' 2014），均与 Pischke 合著；勿写第三本 |
| 希伯来名 | 封面可小字注 יהושע אנגריסט，需希伯来字体族；如模板无 Hebrew 字体设置则省略 |
| MIT 职衔 | 1996 副教授、1998 正教授、2008 起 Ford Professor of Economics；2018 哥大 Wesley Clair Mitchell 访问教授 |
| 在世留白 | 1960 生、在世；幻灯片年份写 "1960–" |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| draft lottery | 征兵抽签 | 1969-1970 越战时期；天然随机化的经典案例 |
| instrumental variables (IV) | 工具变量 | Angrist 方法学核心，勿译"辅助变量" |
| local average treatment effect (LATE) | 局部平均处理效应 | 与 Imbens 1994 合著提出 |
| quasi-experimental design | 准实验设计 | 强调"准"（quasi），非真实验 |
| two-stage least squares (2SLS) | 两阶段最小二乘 | IV 估计的标准实现 |
| Rubin causal model | Rubin 因果模型 | IV 嵌入框架（与 Imbens/Rubin 合著） |
| Maimonides' rule | 迈蒙尼德规则 | 班级人数上限 40 的断点 |
| compulsory schooling laws | 强制教育法 | 与 Krueger/Acemoglu 研究的政策变量 |
| charter school | 特许学校 | KIPP Lynn / Boston 抽签研究 |
| credibility revolution | 可信度革命 | 2010 年 Angrist 对 Leamer 1983 批评的回应语境 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**："探路者"贴合 Angrist 以抽签、规则断点等天然随机化开路、把因果识别从玄学变成工程的探路者形象；曲风的行进感也呼应其伞兵经历（仅作气质呼应，不做叙事绑定）。
- **本地路径**：复制 `music_audio/inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav` 到 `economics/presentations/21th_century/Joshua_Angrist/Pathfinder.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Joshua_Angrist/page.md` | ★ 事实基准（唯一事实来源） |
| `economics/presentations/pages/21th_century/Joshua_Angrist/metadata.json` | QID/生卒/国籍结构化参考（冲突以 page.md 为准） |
| `economics/presentations/pages/21th_century/Joshua_Angrist/images.txt` | 肖像候选 URL（page.md 引用 "Angrist in 2011" 照） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 共享封面（`\input`） |
| `MySQL/data/Joshua_Angrist.yaml` | 社会关系/研究领域入库存档（本批次已入库） |
| `economics/nobel_economics_citations.json` | 2021 拆分获奖理由英文原文（Angrist 条目） |
| `economics/economics_list_data.py` | 2021 年中译对照（`||` 拆分第二段） |

## 十一、执行清单（供 Beamer agent 核对） 【模板通用】

1. 核对事实基准：所有事实与 page.md 逐条对照，冲突一律以 page.md 为准并在陷阱表记录裁定。
2. 复制 Makefile：`MAIN=Joshua_Angrist_zh`、`VIDEO_NAME=Joshua_Angrist_zh`。
3. 肖像：优先 images.txt 真实肖像（"Angrist in 2011"）；404 则装饰圆占位（勿用无授权图）。
4. 配色：主色 `#0E4D64` + badge 四色 + 背景母题（抽签日历格与号码）。
5. 幻灯片序列：按第六节 15 页规划，第 02 页身份信息页必做。
6. 编译循环：`make distclean && make`，0 error、vbox ≤ 10pt、hbox ≤ 50pt；pdftoppm 逐页目检。
7. 引语红线：只有第七节列出的瑞典科学院长文可入引文框（引原文+译文），其余叙述不加中文引号。
8. 结尾页品牌口径：底部标注 `OpenMathAI`（与共享 GitHub 一致），引号用半角 " "。
9. 完成后 `make images && make video` 产出 mp4，向主控汇报页数与体积。

## 十二、版式补遗 【模板通用】

- **共享封面**：第 00 页 `\input` OpenEcon 统一封面，子 deck 不重复 GitHub 链接。
- **封面页**：主标题字号沿用模板；badge 主字体 scriptsize、副行 `\fontsize{6.5}{7.8}`；右上肖像细边框 + 姓名小字注。
- **身份信息页**：左头像 + 右信息网格，含至少生卒/出生地/教育/师承/任职/主要荣誉/核心领域七要素。
- **表格页安全负间距**：顶部 -0.35cm、`arraystretch 0.78-0.82`、公式框前 -0.35~-0.55cm；拥挤时 `itemize` 的 `topsep=0pt`。
- **时间线页**：`\foreach` 分隔符必须 ASCII 逗号；勿给 foreach 节点套 tikz style。
- **希伯来文**：如需渲染希伯来名，用 `\newfontfamily\hebrewfont[Script=Hebrew]{Arial Hebrew}`（参照图灵奖 Wigderson 篇先例）；字体不可用则整行省略。
- **获奖理由引用框**：英文原句 + 中文翻译两行制，英文逐字来自 `nobel_economics_citations.json`。

## 十三、关键时间线速查 【人物专属】

| 年份 | 事件（均出自 page.md） |
|------|------|
| 1960-09-18 | 生于俄亥俄州哥伦布，犹太家庭；在匹兹堡长大 |
| 1977 | Taylor Allderdice 高中毕业 |
| 1982 | Oberlin College 经济学 BA |
| 1982–1985 | 居住以色列，在以色列国防军伞兵旅服役 |
| 1987 / 1989 | 普林斯顿 MA / PhD；论文 "Econometric Analysis of the Vietnam Era Draft Lottery"（导师 Ashenfelter） |
| 博士后至 1991 | 哈佛大学助理教授 |
| 1991 | 回以色列任希伯来大学 senior lecturer，后升副教授 |
| 1994 | 与 Imbens 发表 LATE 论文（Econometrica） |
| 1996 / 1998 | 加入 MIT 经济系任副教授 / 升正教授 |
| 2006 / 2007 | AAAS Fellow / 圣加仑大学荣誉博士 |
| 2008 至今 | MIT Ford Professor of Economics |
| 2008 / 2014 | 与 Pischke 出版《Mostly Harmless Econometrics》/《Mastering 'Metrics'》 |
| 2010 | 回应 Leamer 1983 批评，提出微观经济学经历了"可信度革命" |
| 2011 | 获布达佩斯 Rajk László 学院 John von Neumann Award |
| 2018 | 哥伦比亚大学 Wesley Clair Mitchell 访问教授 |
| 2021 | 诺贝尔经济学奖（与 Imbens 共享一半；Card 独得另一半） |

> 表内每条均有 page.md 明载；蓝图实验室（Blueprint Labs）与 Avela 创业可在第 13 页或遗产页一句带过。
