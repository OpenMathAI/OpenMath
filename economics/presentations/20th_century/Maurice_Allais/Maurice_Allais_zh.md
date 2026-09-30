# 经济学家立传提示词（Maurice Allais）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1988 年得主 Maurice Allais（莫里斯·阿莱）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Maurice_Allais/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Maurice Félix Charles Allais（1911-05-31 生于巴黎 ~ 2010-10-09 逝于巴黎近郊 Saint-Cloud 自宅，享年 99 岁）
- **气质关键词**：**法语世界的一般均衡先驱、阿莱悖论的发现者、钟摆旁的经济学家**
- **获奖理由**（1988 独得，逐字引用，中文翻译照抄总名录）：
  > "for his pioneering contributions to the theory of markets and efficient utilization of resources"
  > （表彰他对市场理论与资源有效利用理论的开创性贡献）
- **设计母题**：**钟摆与分叉（pendulum & bifurcation）**——阿莱既是经济学家又是实验物理学家（1952–1960 副锥摆实验），「钟摆轨迹的分叉」同时隐喻阿莱悖论对期望效用假说的分叉挑战：一条线在临界点分裂为二，构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Maurice_Allais/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/20th_century/Maurice_Allais/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Maurice_Allais_zh`、`VIDEO_NAME=Maurice_Allais_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Allais 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | general equilibrium theory | 一般均衡理论 | *Traité d'économie pure*（1943），市场理论与资源有效利用，诺奖核心 | 封面、核心页 |
| 1 | decision theory | 决策理论 | 不确定性下的选择理论、基数效用，1953 阿莱悖论 | 核心页 |
| 2 | monetary dynamics | 货币动态 | HRL 理论、货币数量论重构（1965） | 核心页 |
| 3 | capital theory | 资本与增长理论 | *Économie et Intérêt*（1947），最优增长黄金律 | 贡献页 |
| 4 | behavioral economics | 行为经济学 | 风险下决策的先驱工作，先于 Kahneman/Tversky | 贡献页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Léon Walras | 无向 | 阿莱自认的首要影响者（Walrasian 传统） |
| influence | Vilfredo Pareto | 无向 | 阿莱自认的首要影响者 |
| influence | Irving Fisher | 无向 | 阿莱自认的首要影响者 |
| influence | Gérard Debreu | 无向 | 战后深刻影响的一代法国经济学家 |
| influence | Jacques Lesourne | 无向 | 战后深刻影响的一代法国经济学家 |
| influence | Edmond Malinvaud | 无向 | 战后深刻影响的一代法国经济学家 |
| influence | Marcel Boiteux | 无向 | 战后深刻影响的一代法国经济学家 |
| colleague | Jacques Rueff | 无向 | 1959 共同创立 Mouvement pour une société libre |

**不入库但提示词可叙述**（page.md 仅叙述性对照，无持续关系）：John Maynard Keynes（正文"Keynes 反驳市场自我调节但重申了阿莱部分观点"）；Paul Samuelson（"Had Allais earliest writings been in English…"赞语与"更早获奖"之憾，引语注明是 Samuelson 所言）；John Hicks（与新古典综合并列贡献叙述）；John von Neumann 与 Oskar Morgenstern（战争条件下独立于《博弈论》开展研究）；Daniel Kahneman 与 Amos Tversky（行为经济学归属叙述）；Milton Friedman（1968 对 HRL 理论的赞语，仅叙述）；Assar Lindbeck（"a giant within the world of economic analysis"评语）；Bruce Caldwell（Georgist 措辞引述）。

## 五、配色方案 【人物专属】

- **气质**：严谨、法兰西、跨学科的双重生命
- **主色**：`#8A1E2D`（法兰西红——manifest 预分配；对应法国经济学传统的厚重与钟摆实验的深红）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGE` 一般均衡 — 深蓝 `#1E3A5F`
  - `badgePara` 决策与悖论 — 灰紫 `#52307C`
  - `badgeMon` 货币动态 — 深青 `#0E4D64`
  - `badgePhys` 物理与钟摆 — 琥珀 `#C07A2A`
- **背景母题**：钟摆轨迹弧线与分叉点（阿莱悖论的路径分裂抽象），呼应「钟摆与分叉」母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 法语世界的一般均衡先驱 / Maurice Allais 1911–2010 + 四色 badge + 右上头像 + 国籍行（France）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地巴黎、教育 École Polytechnique / Mines Paris /
    Paris 大学博士工程师 1949、任职 Mines Paris 教授 1944 起、经济分析中心主任 1946 起、诺奖 1988、核心领域）
03  核心贡献概览 — 一般均衡 / 决策理论与阿莱悖论 / 货币动态 HRL / 资本与增长
04  早年与工程师之路 (1911–1943) — Lycée Lakanal → École Polytechnique → Mines Paris；1933 大萧条美国之行转向经济学
05  纯经济学奠基 (1943) — *Traité d'économie pure*；市场均衡与最大效率的等价定理（先于 Arrow–Debreu 1954）
06  1947 年的先声 — *Économie et Intérêt*：首个迭代模型（OLG，后常归于 Samuelson 1958）、
    最优增长黄金律（先于 Swan/Phelps）、货币交易需求规则（先于 Baumol/Tobin）
07  阿莱悖论 (1953) — "the less the risk is, the more speculators flee"；质疑理性选择传统模型、
    与期望效用假说相矛盾；行为经济学先驱
08  货币动态 HRL 理论 — 心理时间与历法时间的区分；Friedman 1968 赞语（英文原文+注明出自 Friedman）
09  远离一般均衡：剩余理论 — 1960s 转向真实市场与失衡研究；"new scholastic totalitarianism" 批评
10  双重生命：钟摆与物理学 (1952–1960) — 引力/狭义相对论/电磁学实验；1954/1959 日食期间的
    副锥摆异常（Allais effect）；后续复现结果不一（mixed），客观表述
11  法国经济学的教父 — 深刻影响 Debreu / Lesourne / Malinvaud / Boiteux；Samuelson 评价
    （引语英文原文）；Lindbeck 评语
12  1988 诺贝尔奖与荣誉 — 诺奖 1988；CNRS Gold medal；荣誉博士（Mons/Groningen/Lisbon）等
13  自由与计划的探索 — 蒙佩勒林学会成立大会唯一拒签者（财产权分歧）；1959 与 Rueff 共创
    Mouvement pour une société libre；"competitive planning" 主张（客观转述）
14  遗产与结尾 — 法语写作与被重新发现的命运；99 岁辞世 Saint-Cloud + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1988 独得 | 1988 年诺奖由 Allais 独得，与 Hicks/Samuelson 无关——正文只是把三人对新古典综合的贡献并列（Hicks *Value and Capital* 1939、Samuelson *Foundations* 1947），勿写成"共享" |
| 首创归属 | OLG 模型 1947 首创（后常归于 Samuelson 1958）、黄金律先于 Swan/Phelps、交易需求规则先于 Baumol/Tobin、等价定理先于 Arrow–Debreu 1954——一律用「首创/先于/后常归于」措辞，勿写成他人首创 |
| 阿莱悖论年份 | 1953 年提出，质疑期望效用假说；正文引语 "the less the risk is, the more speculators flee" 可用（page.md 英文原文） |
| 引语红线 | Samuelson 赞语与 Lindbeck 评语是**他人评价**，引用时注明说话人；阿莱本人对自由/社会主义关系的表述（"For the true liberal…"）是 page.md 载英文转述，可用但注明为转述 |
| 政治经济主张 | 全球化批判、马斯特里赫特条约批评、单一货币保留意见（1990s–2005）只按 page.md 客观简述一两句，不作评价、不展开；书名 dedication 引语可省略 |
| 物理侧面 | 副锥摆异常实验（1954/1959 两次日食）学界复现**结果不一（mixed）**——写"存在争议/结果不一"，勿写成"被证实"或"被证伪" |
| 生卒 | 1911-05-31 巴黎 ~ 2010-10-09 Saint-Cloud（巴黎近郊）自宅，享年 99；frontmatter 单值无冲突 |
| 职业口径 | 正文首句 "French physicist and economist"——economist 为主职业，physicist/engineer 为辅；metadata occupation 另有 researcher 不入 |
| 学会拒签 | 出席 Mont Pelerin Society 成立大会但是**唯一**拒绝签署宗旨宣言的与会者（财产权范围分歧）——按 Caldwell 的转述客观呈现，勿上升为立场评价 |
| 机构 | Mines Paris（École Nationale Supérieure des Mines de Paris）经济学教授 1944 起、经济分析中心主任 1946 起；另在巴黎第十大学 Nanterre 任教——年份勿混 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| general equilibrium theory | 一般均衡理论 | 诺奖理由核心词 |
| Allais paradox | 阿莱悖论 | 1953，反期望效用假说 |
| expected utility hypothesis | 期望效用假说 | 悖论所挑战的对象 |
| overlapping generations model | 迭代交叠模型（OLG） | 1947 首创、后归于 Samuelson |
| golden rule of optimal growth | 最优增长黄金律 | 先于 Swan/Phelps |
| HRL theory | HRL 货币动态理论 | Hereditary-Relativist-Logistic 缩写 |
| paraconical pendulum | 副锥摆 | 物理实验器械 |
| Allais effect | 阿莱效应 | 日食期间摆面异常，存争议 |
| neoclassical synthesis | 新古典综合 | 与 Hicks/Samuelson 并列贡献 |
| Mont Pelerin Society | 蒙佩勒林学会 | 1947 成立，阿莱拒签宗旨宣言 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Ascension**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「攀升/上升」贴合从 Mines 工程师到 1988 诺奖的长程学术生命；曲名的庄严感也呼应其在法语世界被重新发现、最终登顶的迟来承认。
- **本地路径**：复制 `music_audio/inspiring-electronic/20-gYUC-sXt_8M-...Ascension.wav` 到 `economics/presentations/20th_century/Maurice_Allais/Ascension.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
