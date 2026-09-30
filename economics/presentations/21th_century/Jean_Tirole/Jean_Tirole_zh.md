# 经济学家立传提示词（Jean Tirole）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2014 年得主 Jean Tirole（让·梯若尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Jean_Tirole/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Jean Marcel Pierre Tirole（1953-08-09 生于法国特鲁瓦，在世）
- **气质关键词**：**驯服巨头的人、产业组织的集大成者、图卢兹学派的奠基者**
- **诺奖获奖理由**（2014 独得，manifest citation_en 已给出，逐字引用）：
  > "for his analysis of market power and regulation"（表彰他对市场力量与监管的分析）
  - page.md Awards 节口径为 "his analysis of market power and the regulation of natural monopolies"（对市场力量与自然垄断监管的分析）——两处口径并存，引用以官方短句为准。
- **设计母题**：**驯服（taming）**——用缰绳与天平驯服庞然巨物：巨型企业轮廓与监管天平的视觉隐喻，取自其 2014 诺奖演讲题 "The science of taming powerful firms"，构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Jean_Tirole/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Jean_Tirole/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Jean_Tirole_zh`、`VIDEO_NAME=Jean_Tirole_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Tirole 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | industrial organization | 产业组织理论 | 《The Theory of Industrial Organization》(1988) 集大成；infobox Discipline | 封面、核心页 |
| 1 | game theory | 博弈论 | infobox Discipline；寡头竞争战略效应分类 | 核心页 |
| 2 | regulation | 监管经济学 | 2014 诺奖核心——市场力量与自然垄断监管 | 核心页 |
| 3 | microeconomics | 微观经济学 | infobox Discipline；激励理论、双边市场 | 贡献页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 8 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Eric Maskin | 对方是导师 | MIT 博士导师（1981 论文《Essays in economic theory》） |
| advisor-student | Roland Bénabou | 本人 → 学生 | infobox Doctoral students 明载 |
| collaborator | Jean-Jacques Laffont | 无向 | 合著《A Theory of Incentives in Procurement and Regulation》《Competition in Telecommunications》；共创图卢兹经济学院 |
| collaborator | Drew Fudenberg | 无向 | 合著《Game Theory》(1991)《Dynamic Models of Oligopoly》；寡头竞争战略效应分类 |
| collaborator | Oliver Hart | 无向 | 合著纵向合并封锁（foreclosure）条件论文 |
| collaborator | Jean-Charles Rochet | 无向 | 双边市场竞争政策分析（Rochet–Tirole） |
| collaborator | Mathias Dewatripont | 无向 | 合著《The Prudential Regulation of Banks》《Balancing the Banks》 |
| collaborator | Bengt Holmström | 无向 | 合著《Inside and Outside Liquidity》(2011) |

**不入库但提示词可叙述**：Jean-Jacques Laffont 基金会董事长职务（机构非人物关系）；Corps of Bridges, Waters and Forests 工程师军团履历（机构）；2025 年荣誉军团司令勋位（Commander of the Légion d'honneur，荣誉非关系）。

## 五、配色方案 【人物专属】

- **气质**：法式理性、缜密、在数学模型中驯服市场力量
- **主色**：`#A63A2B`（manifest 预分配，赤陶红——图卢兹砖城的学术底色与监管天平的锋利感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeIO` 产业组织 — 赤陶红 `#A63A2B`
  - `badgeReg` 监管理论 — 深蓝 `#16324F`
  - `badgeTwo` 双边市场 — 青绿 `#0E7C7B`
  - `badgeGame` 博弈论 — 琥珀 `#C07A2A`
- **背景母题**：监管天平与巨型企业轮廓（驯服 powerful firms 的抽象），呼应「监管不应妨碍创新而须维持公平规则」的核心立场。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 驯服巨头的人 / Jean Tirole 1953– + 四色 badge + 右上头像 + 国籍行（France）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1953-08-09 特鲁瓦、Polytechnique 1976/
    Ponts et Chaussées 1978/Paris Dauphine、MIT PhD 1981 导师 Maskin、图卢兹第一大学、
    诺奖 2014、核心领域）
03  核心贡献概览 — 产业组织综合 / 监管科学 / 双边市场 / 银行与公司金融
04  法国工程师精英路线 (1953–1981) — Polytechnique、Ponts et Chaussées、桥林水森军团、
    Dauphine 决策数学、21 岁转向经济学
05  MIT 门下 (1981) — Maskin 导师；《Essays in economic theory》；1984-1991 回 MIT 任教
06  《产业组织理论》(1988) — 以博弈论革命综合寡头竞争，定义现代产业组织
07  监管科学：信息不对称下的契约 — 成本加成 vs 固定价格契约；独立监管机构的承诺问题
08  单边市场垄断 — 「公平接入」的悖论；垄断取得是否公允的判定
09  双边市场 — Rochet–Tirole；平台倾斜定价（用户免费/广告主付费）；监管误判风险
10  知识产权与专利池 — 标准必要专利；FRAND 承诺难题
11  银行与流动性 — Laffont/Dewatripont/Holmström 合作脉络；银行短视冒险与 QE 政策建议
12  图卢兹学派的创建 — 与 Laffont 共创 TSE；IDEI 科学主任；Laffont 基金会董事长
13  荣誉与认可 — 诺奖 2014、CNRS 金质奖章 2007、Nemmers 2014、BBVA 2008、荣誉军团司令
14  遗产与结尾 — 监管经济学成为政策科学 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 官方短句 "for his analysis of market power and regulation"（2014 独得，非共享）；page.md Awards 节另有 "the regulation of natural monopolies" 长口径——引用以官方短句为准，勿混入他人 |
| Laffont 忌讳 | Laffont 2004 年早逝是常识但 **page.md 未载卒年**——立传中禁写卒年，只写「共创 TSE、多部合著、基金会以其命名」 |
| 双边市场表述 | "Rochet and Tirole analysed the implications of 2-sided markets"——Rochet 全名 Jean-Charles Rochet 见合著书目《Balancing the Banks》；勿把双边市场理论写成 Tirole 独创 |
| Hart 定性 | Hart 与 Tirole 是合著一篇论文（纵向合并封锁条件）——collaborator 而非 colleague；Hart 2016 诺奖属契约理论，勿混入 Tirole 获奖理由 |
| 研究方法定性 | 正文明确 Tirole 的工作 "largely theoretical and explored in mathematical models, not empirical research"——与 2013 三人（实证）形成学科光谱对照，勿写错 |
| 教育时间线 | Polytechnique 工程师学位 **1976**、Ponts et Chaussées **1978**、Dauphine DEA 1976 + 第三阶段博士（决策数学）1978、MIT 经济学 PhD **1981**——四个年份勿混 |
| MIT 任职 | 1984–1991 任 MIT 经济学教授（1981 博士后先在 Ponts et Chaussées 做研究）；现为 MIT 访问教授——勿写成一直在图卢兹 |
| 学会职务 | 计量经济学会主席 1998、欧洲经济学会主席 2001——年份勿互换 |
| 在世者生卒 | 1953-08-09 生，在世——卒日留白，全篇一致 |
| 引语红线 | 21 岁转向经济学的自述（"very rigorous"、"still a social science"）page.md 有英文原文可引原文+译文；诺奖演讲题 "The science of taming powerful firms" 是标题可直引；其余勿杜撰 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| market power | 市场力量 | 企业把价格抬到成本之上/提供低质量的能力；诺奖核心词 |
| regulation | 监管 | 对自然垄断与市场力量的治理 |
| natural monopoly | 自然垄断 | 长口径获奖理由用词 |
| foreclosure | 纵向封锁 | 与 Hart 合著论文主题：纵向合并排斥下游 |
| two-sided market | 双边市场 | 平台向两侧倾斜定价（Rochet–Tirole） |
| patent pool | 专利池 | 降价与抬价池的分界难题 |
| standard essential patent | 标准必要专利 | FRAND 承诺的语境 |
| cost-plus contract | 成本加成契约 | 免疫成本波动但弱化降本激励 |
| fixed price contract | 固定价格契约 | 强降本激励但可能牺牲质量 |
| incentive theory | 激励理论 | 与 Laffont 合著主线 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Empire Collapse**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「帝国崩塌」的史诗张力恰合 Tirole 的主题——垄断帝国的边界、监管与反垄断对巨头势力的驯服；曲名的宏大戏剧感对应其在数学模型中推演市场力量兴衰的学术版图。
- **本地路径**：复制上述 wav 到 `economics/presentations/21th_century/Jean_Tirole/EmpireCollapse.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
