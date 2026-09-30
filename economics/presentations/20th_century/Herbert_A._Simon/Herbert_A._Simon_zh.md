# 经济学家立传提示词（Herbert A. Simon）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1978 年得主 Herbert A. Simon（赫伯特·西蒙）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Herbert_A._Simon/page.md`，与其冲突时以 page.md 为准。
> **★ 特殊裁定**：Simon 库内记录 id=223（Q181529）已由 **图灵奖 1975 侧完整入库**（has_social_data=1）。本批次照常写提示词 md 与 yaml，**yaml 仅存档不执行 seed_person**（`MySQL/data/Herbert_A._Simon.yaml` 文件头已注明）。领域/关系数据以库内既有记录为准，本篇第三节、第四节为存档口径。

## 一、背景信息 【人物专属】

- **目标经济学家**：Herbert Alexander Simon（1916-06-15 生于威斯康星州密尔沃基 ~ 2001-02-09 逝于宾夕法尼亚州匹兹堡，享年 84 岁）
- **气质关键词**：**有限理性的发现者、满意度决策的命名者、横跨经济学与人工智能的通才**
- **诺奖获奖理由**（1978 独得，逐字引用 manifest）：
  > "for his pioneering research into the decision-making process within economic organizations"（表彰他对经济组织内部决策过程的开创性研究）
- **设计母题**：**有限理性（bounded rationality）**——完全理性之圆被认知边界裁切、在边界内寻找「足够好」的解：缺角圆与渐进收敛的折线构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Herbert_A._Simon/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Herbert_A._Simon/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Herbert_A._Simon_zh`、`VIDEO_NAME=Herbert_A._Simon_zh`。**第 4 步与第 4.5 步无需执行**（图灵奖侧已入库，见文件头裁定）；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属，存档口径】

**Simon 的研究领域（图灵奖侧已入库；经济侧视角按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | decision-making | 决策理论 | 诺奖核心：经济组织内的决策过程 | 封面、核心页 |
| 1 | bounded rationality | 有限理性 | 与 satisficing 构成行为经济学中心主题 | 核心页 |
| 2 | artificial intelligence | 人工智能 | Logic Theorist/GPS，图灵奖理由 | AI 页 |
| 3 | organization theory | 组织理论 | 与 March 合著《组织》 | 组织页 |
| 4 | political science | 政治科学 | 其博士训练本行（BA/PhD 1936/1943） | 早年页 |

## 四、社会关系梳理 + 入库 【人物专属，存档口径】

**只收 page.md 明载关系（图灵奖侧已入库；本表为 yaml 存档口径，未执行 seed）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Henry Schultz | Simon → 学生 | 芝加哥大学最重要的导师（econometrician）；Schultz 库内 id=1399 |
| spouse | Dorothea Isabel Pye | 无向 | 1938 结婚，63 年婚姻；库内 id=1415 |
| parent-child | Katherine / Peter / Barbara | Simon → 子 | 三子女（仅具名，无独立条目，存档不入库） |
| advisor-student | Edward Feigenbaum | Simon → 学生 | infobox Doctoral students；EPAM 合作者 |
| advisor-student | Allen Newell | Simon → 学生 | 图灵奖共同得主；库内 id=222 |
| advisor-student | John Muth | Simon → 学生 | infobox Doctoral students 明载 |
| advisor-student | Oliver E. Williamson | Simon → 学生 | infobox Doctoral students 明载；2009 诺奖得主 |
| advisor-student | Richard E. Korf | Simon → 学生 | infobox Doctoral students 明载 |
| advisor-student | William F. Pounds | Simon → 学生 | infobox Doctoral students 明载 |
| advisor-student | Saras Sarasvathy | Simon → 学生 | infobox Doctoral students 明载 |
| advisor-student | Richard Waldinger | Simon → 学生 | infobox Doctoral students 明载 |
| colleague | James G. March | 无向 | 合著《组织》（1958，现代组织理论奠基） |
| collaborator | David Hawkins | 无向 | 共同发现并证明 Hawkins–Simon 定理（投入产出矩阵正解条件） |

**不入库但提示词可叙述**：导师群像 Lasswell/Rashevsky/Carnap/Merriam（「studied under」列举，非单独师承关系；Henry Schultz 是 page.md 明载的 most important mentor）；J.C. (Cliff) Shaw（Logic Theorist/GPS 与 IPL 合作者，RAND 时期）；Clarence Ridley（1938 合著市政测量，早年助手关系）；图灵奖侧已入库的关系以库内为准，本批次不重复建边。

## 五、配色方案 【人物专属】

- **气质**：跨界的智识雄心、认知边界的冷静
- **主色**：`#52307C`（深紫——认知科学与人工智能的交融色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRational` 有限理性 — 深紫 `#52307C`
  - `badgeAI` 人工智能 — 靛蓝 `#283593`
  - `badgeOrg` 组织理论 — 青绿 `#0E7C7B`
  - `badgePol` 政治科学 — 玫瑰 `#C4204F`
- **背景母题**：缺角圆与渐进收敛折线（在认知边界内寻找满意解）。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 有限理性的发现者 / Herbert A. Simon 1916–2001 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地密尔沃基、教育芝加哥大学 BA 1936/PhD 1943、
    任职 IIT 1942–49→Carnegie Mellon 1949–2001、图灵奖 1975+诺奖 1978 双冠、核心领域）
03  核心贡献概览 — 有限理性 / 满意化 / 组织决策 / 人工智能
04  密尔沃基少年 (1916–1933) — 父为德国移民电气工程师、舅舅 Harold Merkel 引其入社会科学之门
05  芝加哥岁月 (1933–1943) — 政治科学训练、Henry Schultz 最重要导师、Berkeley 运筹组主任
06  《管理行为》1947（核心贡献页）— 博士论文改写；「如果人类理性没有限度，管理理论将是一片荒芜」
07  有限理性与满意化（核心贡献页）— 对 homo economicus 的替代；procedural vs substantive rationality
08  Cowles 与经济学 (1940s) — 参加 Cowles Commission 研讨班（Haavelmo/Marschak/Koopmans 在列）；Hawkins–Simon 定理
09  卡内基的创建年代 (1949–1967) — 工业管理系主任、卡内基工学院→CMU；帮助创建 CMU 计算机学院
10  与 Newell 的黄金十年 (1956–1975) — Logic Theorist、GPS、IPL；1975 图灵奖
11  图灵奖与诺奖双冠 — 1975 ACM Turing Award（AI、人类认知心理学、表处理）；1978 诺贝尔经济学奖
12  专长与 50,000 组块 — 与 Ericsson 口语报告分析；十年成专家
13  荣誉满载 — NAS 1967、National Medal of Science 1986、von Neumann Theory Prize 1988、APA 双奖
14  遗产与结尾 — 行为经济学的源头活水（2001-01 手术并发症去世）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 双奖身份 | 1975 图灵奖（与 Newell 共享，AI/认知心理学/表处理三项理由）+ 1978 诺贝尔经济学奖（独得）——本篇为经济学侧立传，诺奖理由在前，图灵奖一句带过；禁把图灵奖理由误当诺奖理由 |
| yaml 存档裁定 | 库内 id=223 已由图灵奖侧完整入库（has_social_data=1）——本批次 **不执行 seed_person**，yaml 文件头注明存档身份；Review 时勿以「yaml 未入库」报错 |
| 博士导师口径 | page.md 明载 most important mentor = **Henry Schultz**（库内 1399）；Lasswell/Rashevsky/Carnap/Merriam 是「studied under」群像（frontmatter other academic advisors 有载但 page.md 无单独师承叙事），存档 yaml 不建边、提示词叙述即可 |
| 生卒 | 1916-06-15 密尔沃基生 ~ 2001-02-09 匹兹堡逝（腹部肿瘤手术并发症，2001-01 手术）；享年 84 |
| 任职跨度 | CMU 1949–2001 整 52 年（前身 Carnegie Institute of Technology，1967 更名 CMU）；此前 IIT 1942–49 任政治科学教授兼系主任；Berkeley 1939–42 运筹组主任——三段勿混 |
| Cowles 时期 | Simon 在 IIT 期间参加 Cowles Commission 研讨班，同列者 Haavelmo/Marschak/**Koopmans**（1975 得主，本批次第一人）——叙述可交叉引用，但 Simon-Koopmans 无 page.md 级直接关系记载，禁建边 |
| 图灵奖引语 | 1975 图灵奖理由为 ACM 官方原句（"In joint scientific efforts extending over twenty years..."），page.md 载英文原文可用；《管理行为》引语（"If there were no limits to human rationality..."）亦可用 |
| 预测失误 | 1957「十年内计算机棋艺超人」与 1965「二十年内机器能做人类一切工作」两条著名预测落空（分别用了约 40 年）——客观记录，勿美化回避 |
| 三子女 | Katherine/Peter/Barbara 仅具名（无独立条目），存档不入库；妻 Dorothea Pye 1938 成婚、63 年婚姻、2002 年去世 |
| Georgism 底色 | 青年时期信奉亨利·乔治单税论、1979 年仍主张地价税取代工资税——经济学思想史细节，叙述可用，Henry George 影响不入库（图灵奖侧 yaml 无此边） |
| 中文学名 | 赫伯特·西蒙（name_zh），勿与同为 Simon 的其他人混淆；本名 Herbert Alexander Simon |
| 彩色盲轶事 | 因色盲与实验室笨拙放弃生物学转向社会科学——早年叙事可用 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| bounded rationality | 有限理性 | 诺奖核心概念，行为经济学中心主题 |
| satisficing | 满意化（决策） | Simon 自造词，勿译「满足化」歧义 |
| procedural / substantive rationality | 程序理性/实质理性 | 两学科定义分野 |
| homo economicus | 理性经济人 | Simon 模型的对照面 |
| Logic Theorist / General Problem Solver | 逻辑理论家/通用问题求解器 | 与 Newell（及 Shaw）合作 |
| Information Processing Language | 信息处理语言（IPL） | Newell/Shaw/Simon 共同开发；链表初名 NSS memory |
| EPAM | 初等知觉与记忆器 | 与 Feigenbaum 合作的学习理论 |
| Hawkins–Simon theorem | 霍金斯–西蒙定理 | 投入产出矩阵正解条件 |
| Administrative Behavior | 《管理行为》 | 1947 初版，一生工作的基石 |
| chunk | 组块 | 专长习得约 50,000 组块的估算 |
| verbal protocol analysis | 口语报告分析 | 与 Ericsson 开发的实验技术 |
| near-decomposability | 近似可分解性 | 其数理经济学定理之一 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Savage**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Simon 是二十世纪罕见的双冠通才——用心理学拆解经济学、用计算机模拟人类思维；「Savage」的锋利感贴合其对古典理性人假设的凌厉解剖，也呼应卡内基黄金十年里人机共智的先锋气质。
- **本地路径**：复制 `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav` 到 `economics/presentations/20th_century/Herbert_A._Simon/Savage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
