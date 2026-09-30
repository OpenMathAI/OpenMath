# 经济学家立传提示词（Gary Becker）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1992 年得主 Gary S. Becker（加里·贝克尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Gary_Becker/page.md`，与其冲突时以 page.md 为准（同目录 metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：Gary Stanley Becker（1930-12-02 生于宾夕法尼亚州波茨维尔 ~ 2014-05-03 逝于芝加哥，享年 83 岁，死于手术并发症）
- **气质关键词**：**把经济学带进生活的经济学帝国主义者、人力资本之父、第三代芝加哥学派领袖**
- **诺奖获奖理由**（1992，独得，manifest citation 逐字）：
  > "for having extended the domain of microeconomic analysis to a wide range of human behaviour and interaction, including non-market behaviour"（表彰他将微观经济分析的领域扩展到包括非市场行为在内的人类行为与互动的广泛范围）
- **设计母题**：**理性之光照进生活（rationality into life）**——歧视、犯罪、婚姻、生育、成瘾，这些看似"非经济"的领域在贝克尔笔下皆可作理性选择分析：以家庭轮廓、天平、钥匙与锁孔等生活意象叠加在供需曲线上构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Gary_Becker/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）
- **一句话画像**：普林斯顿本科（1951，毕业论文论多国贸易）、芝加哥博士（1955）；先任教哥伦比亚大学（1957-1968）兼 NBER 研究，1970 回芝加哥、1983 获社会学系合聘；把微观经济学推进社会学领地——歧视、犯罪、家庭、成瘾皆成经济学题目；2011 年经济学教授调查中被选为「60 岁以上最受欢迎的在世经济学家」；Friedman 称他是「20 世纪后半叶最伟大的社会科学家」。

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Gary_Becker/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Gary_Becker_zh`、`VIDEO_NAME=Gary_Becker_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。
> 布局检查照模板第 8 步：每写完一页 `make distclean && make`，`pdftoppm` 截图逐页目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

## 三、研究领域梳理 + 入库 【人物专属】

**Becker 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microeconomics | 微观经济学 | 获奖理由核心：微观分析扩展到非市场行为 | 封面、核心页 |
| 1 | human capital | 人力资本 | 《Human Capital》(1964) 引入概念，成为资本理论的一部分 | 核心页 |
| 2 | family economics | 家庭经济学 | 与 Mincer 共创现代家庭经济学（NHE）；《A Treatise on the Family》(1981)、rotten kid theorem | 家庭页 |
| 3 | economics of crime | 犯罪经济学 | 1968 犯罪与惩罚的经济分析；Posner 称其是犯罪经济学写作的泉源 | 犯罪页 |
| 4 | labor economics | 劳动经济学 | 时间配置理论 (1965)、歧视经济学 (1957 博士论文)；贝克尔视劳动经济学为资本理论一部分 | 劳动页 |

补充说明（供立传 agent 取材）：代表作谱系——博士论文《The Economics of Discrimination》(1955/1957)；《Human Capital》(1964，1975/1993 再版)；犯罪与惩罚（1968 JPE）；家庭三部曲（marriage part I/II 1973-74；《A Treatise on the Family》1981，1991 扩展版）；理性成瘾（1988 与 Murphy）；社会经济学（2000 与 Murphy）；器官市场（2007 与 Elias）。奖项：John Bates Clark Medal 1967、Nobel 1992、Pontifical Academy 1997、National Medal of Science 2000、John von Neumann Award 2004、Presidential Medal of Freedom 2007；Google Scholar 引用逾 20 万次；TGG Group 创始合伙人；Mont Pelerin Society 1990 年会长。

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | H. Gregg Lewis | Lewis → 导师 | 芝加哥博士导师（1955 PhD，论文 The Economics of Discrimination）；1973 又合著子女数量与质量互动论文 |
| influence | Milton Friedman | 无向 | 贝克尔自述 Friedman 是「迄今最好的老师」，其微观课程重燃对经济学的兴趣 |
| influence | Theodore Schultz | 无向 | 芝加哥求学期间深刻影响其日后工作的经济学家之一 |
| influence | Aaron Director | 无向 | 芝加哥求学期间深刻影响其日后工作的经济学家之一 |
| influence | Leonard Jimmie Savage | 无向 | 芝加哥求学期间深刻影响其日后工作的经济学家之一 |
| spouse | Doria Slote | 无向 | 1954 结婚，1970 妻病逝；育二女 Catherine 与 Judy |
| spouse | Guity Nashat | 无向 | 1980 再婚，伊朗裔中东史历史学家；1997 合著《The Economics of Life》 |
| colleague | Jacob Mincer | 无向 | 哥伦比亚劳动研讨班共同主持，1960s 共创现代家庭经济学（New Home Economics） |
| collaborator | Kelvin Lancaster | 无向 | 1960s 中期共同提出家庭生产函数概念 |
| collaborator | George Stigler | 无向 | 合著 De gustibus non est disputandum (1977 AER) |
| collaborator | Kevin M. Murphy | 无向 | 合著理性成瘾 (1988) 与 Social Economics (2000) |
| colleague | Richard Posner | 无向 | 2004-12 共同开写 The Becker-Posner Blog；Posner 论定其犯罪经济学之深远影响 |
| colleague | Alan Blinder | 无向 | Business Week 专栏 1985-2004 轮替撰稿（一保守派一自由派） |
| collaborator | Julio Jorge Elias | 无向 | 合著 2007 器官捐献市场激励论文（肾约 $15,000、肝约 $32,000 的定价估算） |
| advisor-student | Shoshana Grossbard | Becker → 学生 | 正文与 infobox 双载（芝大时期学生）；NHE 史作者 |
| advisor-student | David O. Meltzer | Becker → 学生 | infobox Doctoral students 明载 |
| advisor-student | Russ Roberts | Becker → 学生 | infobox 明载 |
| advisor-student | Walter Block | Becker → 学生 | infobox 明载 |
| advisor-student | Darius Lakdawalla | Becker → 学生 | infobox 明载 |
| advisor-student | Rodrigo R. Soares | Becker → 学生 | infobox 明载 |
| advisor-student | Scott Drewianka | Becker → 学生 | infobox 明载 |

**不入库但提示词可叙述**：NHE 传统下的学生与同仁群像（Andrea Beller、Barry Chiswick、Carmel Chiswick、Victor Fuchs、Michael Grossman、Robert Michael、June E. O'Neill、Sol Polachek、Robert Willis——只列名于 NHE 历史叙述，无逐一师生明载）；James Heckman（受 NHE 传统影响、1969 起参加哥伦比亚劳动研讨班，仅叙述）；女儿 Catherine Becker（无链接仅具名，parent-child 不入）；Eleanor Stier（伴侣关系无白名单类型）；Leon M. Lederman（2001 Golden Plate 颁奖人，一次性事件）；Robert Dole（1996 竞选顾问，政治事件不入库）；Charles I. Jones（对其 2013 言论的批评者，controversy 级别弱于学术争论，不入库）；Justin Wolfers / Robert Solow / Kenneth Arrow（仅评价性提及）。

## 五、配色方案 【人物专属】

- **气质**：明快、锐利、把日常世界数学化的智识冲劲
- **主色**：`#5B2A86`（manifest 预分配，深紫——理性与生活的交界，学术冷静中带人文暖色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMicro` 微观与人力资本 — 深紫 `#5B2A86`
  - `badgeFamily` 家庭经济学 — 玫瑰 `#C4204F`
  - `badgeCrime` 犯罪与惩罚 — 深海蓝 `#1E3A5F`
  - `badgeLabor` 劳动与歧视 — 青绿 `#0E7C7B`
- **背景母题**：家庭轮廓与天平叠加供需曲线（理性选择分析覆盖生活领域的视觉隐喻）；共享封面版式按 `economics/presentations/cover/` 统一口径（品牌标注 OpenMathAI）。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex，品牌口径 OpenMathAI）
01  封面 — 把经济学带进生活的人 / Gary S. Becker 1930–2014 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒（1930-12-02 Pottsville ~ 2014-05-03 Chicago，享年 83）、
    教育（Princeton BA 1951 / Chicago PhD 1955）、任职（Columbia 1957-68 → Chicago 1970-2014，
    经济学+社会学合聘）、诺奖 1992、核心领域
03  核心贡献概览 — 微观分析扩展 / 人力资本 / 家庭经济学 / 犯罪经济学（四 badge 横排）
04  早年与普林斯顿 (1930–1951) — 波茨维尔犹太家庭；Princeton 1951 BA，毕业论文多国贸易理论
05  芝加哥淬炼 (1951–1955) — Friedman 微观课重燃兴趣（自述「迄今最好的老师」）；
    Gregg Lewis / T. W. Schultz / Director / Savage 的群体影响；博士论文《The Economics of Discrimination》
06  歧视经济学 (1957) — 偏好的经济代价：歧视提高企业成本的分析框架；市场惩罚歧视者的逻辑
07  哥伦比亚岁月与 NHE 创立 (1957–1968) — 与 Jacob Mincer 共同主持劳动研讨班；
    生育 (1960)、时间配置 (1965)、女性劳动供给 (Mincer 1962)；Clark Medal 1967
08  人力资本 (1964)（核心贡献页）— 教育、培训、健康皆投资；劳动经济学归入资本理论；
    工资差距的知识投资解释；1975/1993 再版
09  犯罪与惩罚 (1968)（核心贡献页）— 罪犯理性权衡收益与被抓概率、定罪与惩罚成本；
    罚金与监督的成本不对称→「重罚少监」的政策推论；Posner 的评价
10  家庭经济学与 Treatise (1970s–1981)（核心贡献页）— 婚姻、离婚、利他主义、对子女的投资；
    rotten kid theorem；1981《A Treatise on the Family》、1991 扩展版
11  与 Murphy 的两度合著 — 理性成瘾 (1988)：成瘾行为的理性框架；
    Social Economics (2000)：社会环境中的市场行为
12  公共声量 — Business Week 专栏 1985-2004 与 Blinder 轮替；1996 Dole 竞选高级顾问；
    2004 Becker-Posner Blog；2013 华尔街日报言论及 Jones 的批评（客观并置）
13  荣誉与认可 — Clark 1967 / Nobel 1992 / 教宗科学院 1997 / National Medal of Science 2000 /
    von Neumann Award 2004 / Presidential Medal of Freedom 2007；2014 芝大三天纪念会议
14  遗产与结尾 — 「最伟大的社会科学在生活里」：经济学与社会学、人口学的边界消融 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | manifest citation 用 "behaviour"（英式拼写）逐字用；正文另有美式 "behavior" 措辞，引用时以 manifest 为准 |
| 《Human Capital》书名 | 正文一处作 "Human Capital Theories"（1964），文献列表作 *Human capital: a theoretical and empirical analysis*（1993 第三版标注 1964 初版）——书名按文献列表口径，勿把 "Human Capital Theories" 当书名 |
| 导师口径 | infobox Doctoral advisor 与 frontmatter 一致：**H. Gregg Lewis**；Friedman/Schultz/Director/Savage 是「影响其日后工作」的群体（influence），勿写成博士导师 |
| 两段婚姻 | Doria Slote（1954-1970，病逝，育 Catherine/Judy 两女）与 Guity Nashat（1980-，伊朗裔历史学家，合著 1997）；勿混年份 |
| 子女入库裁定 | 二女仅具名（Catherine 无链接、Judy 仅链接），按批次纪律 parent-child 不入库，提示词可叙述 |
| 政治身份 | 政治保守派、1996 年任 Dole 竞选高级顾问——时间线客观一笔即可，勿展开政治评价 |
| 2013 言论争议 | 关于女性职场壁垒的 WSJ 言论与 Charles I. Jones 的批评（"Productivity could be 9 percent to 15 percent higher..."）客观并置，勿单侧评价；属言论争议非学术 controversy，不入库 |
| 「经济帝国主义」 | 学界对其风格的习惯称呼，page.md 未以原文载此词作定论；可作气质关键词但勿引为引语 |
| 引语红线 | Friedman 评价（"the greatest social scientist who has lived and worked..."）、Becker 自述（"by far the greatest living teacher I have ever had"）、Wolfers 评价均 page.md 有英文原文，可引原文+译文；中文引号内不得出现无原文支撑的「原话」 |
| rotten kid theorem | 家庭理论核心：利他者家庭中自利子女的行为也可与家庭整体利益一致（1981 美国家庭数据）；「跨代家庭未必最大化共同收入」的检验结果一并叙述 |
| 器官市场争议 | 2007 与 Elias 的论文给出肾约 $15,000、肝约 $32,000 的估算；批评者认为会剥削发展中国家捐赠者——客观并置，勿替作者辩护或批判 |
| 家庭专门化模型批评 | 女性主义/文化经济学对其家庭专门化模型的批评（嵌入性别规范、忽视议价与外部选择）page.md 有专节，立传可作一页素材，叙述平衡 |
| metadata 噪声 | metadata.json 职业含 criminologist/educator——以 infobox+正文为准（economist + university teacher）；获奖理由以 manifest citation 逐字为准 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| human capital | 人力资本 | 教育/培训/健康的投资视角；勿与「人力资源」混用 |
| economics of discrimination | 歧视经济学 | 博士论文题目；歧视被建模为偏好而非纯偏见叙事 |
| nonmarket behaviour | 非市场行为 | 获奖理由核心词，manifest 英式拼写 behaviour |
| rotten kid theorem | 坏孩子定理 | 利他家长与自利子女的家庭内激励一致性问题 |
| household production function | 家庭生产函数 | 与 Lancaster 共同提出（1960s 中期） |
| allocation of time | 时间配置 | 1965 EJ 论文；劳动经济学的微观基础 |
| rational addiction | 理性成瘾 | 1988 与 Murphy；成瘾作为理性选择的连续决策 |
| New Home Economics (NHE) | 新家庭经济学 | 与 Mincer 在哥伦比亚劳动研讨班共创的家庭经济学分支 |
| deadweight loss | 无谓损失 | 芝加哥政治经济分析（掠夺与抵抗的非线性）中的核心机制 |
| Becker-Posner Blog | 贝克尔-波斯纳博客 | 2004-12 开写；两人共同公共写作平台 |
| economics of crime | 犯罪经济学 | 1968 JPE 论文为泉源；「重罚少监」推论要点 |
| John Bates Clark Medal | 克拉克奖章 | 1967 获得者，写全称勿简写为「克拉克奖」 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：贝克尔的事业是把「看不见的理性」照进看似混沌的日常——歧视、犯罪、婚姻、成瘾在表象之下皆有可分析的结构，恰如海市蜃楼之下真实地形的投影；Mirage 的电子氛围既带学术的冷静纵深，也呼应他让经济学跨越边界、直至与「幻象」交锋（成瘾与偏见的非理性表象）的一生。
- **本地路径**：复制 `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` 到 `economics/presentations/20th_century/Gary_Becker/Mirage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
