# 经济学家立传提示词（Angus Deaton）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2015 年得主 Angus Deaton（安格斯·迪顿）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Angus_Deaton/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Sir Angus Stewart Deaton（1945-10-19 生于苏格兰爱丁堡，在世；2016 年受封下级勋位爵士）
- **气质关键词**：**穷人世界的观察者、需求系统的建筑师、绝望之死的记录者**
- **诺奖获奖理由**（2015 独得，manifest citation_en 已给出，逐字引用）：
  > "for his analysis of consumption, poverty, and welfare"（表彰他对消费、贫困与福利的分析）
- **设计母题**：**从个体选择到总量图景（linking individual choices to aggregate outcomes）**——无数细小消费选择汇聚成福利图景：细密散点向上汇聚为宏观曲线的视觉隐喻（瑞典皇家科学院明载表述 "By linking detailed individual choices and aggregate outcomes"），构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Angus_Deaton/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Angus_Deaton/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Angus_Deaton_zh`、`VIDEO_NAME=Angus_Deaton_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Deaton 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microeconomics | 微观经济学 | infobox Discipline；消费需求与福利分析 | 封面、核心页 |
| 1 | development economics | 发展经济学 | 贫困测量与发展政策；获奖理由核心 | 核心页 |
| 2 | health economics | 健康经济学 | 健康、福祉与「绝望之死」研究 | 应用页 |
| 3 | welfare economics | 福利经济学 | 获奖理由第三词；消费聚合与福祉度量 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 4 条——诚实值偏低，勿误判缺失）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Richard Stone | 对方是导师 | 剑桥博士导师（1975 论文《Models of Consumer Demand and Their Application to the United Kingdom》） |
| colleague | Terry Barker | 无向 | 剑桥应用经济系与 Stone、Barker 共事的研究官员 |
| collaborator | John Muellbauer | 无向 | 合创 Almost Ideal Demand System (AIDS, 1980)；合著《Economics and Consumer Behavior》 |
| spouse | Anne Case | 无向 | 妻，普林斯顿 SPIA 教授；合著「绝望之死」系列与《Deaths of Despair》(2020) |

**不入库但提示词可叙述**：前妻（page.md 仅载 "previously widowed"，无姓名）；两名子女（1970/1971 年生，**不具名不入库**）；Terry Barker 之外的剑桥同僚；2015 瑞典皇家科学院评语（机构评价非人物关系）。relations=4 系 page.md 明载诚实值，防 Review 误判。

## 五、配色方案 【人物专属】

- **气质**：温厚、人本、从数据深处看见具体的人
- **主色**：`#9E2B25`（manifest 预分配，苏格兰砖红——爱丁堡到剑桥到普林斯顿的学术长路）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeAIDS` 需求系统 — 砖红 `#9E2B25`
  - `badgePov` 贫困与发展 — 深蓝 `#16324F`
  - `badgeWell` 福祉度量 — 青绿 `#0E7C7B`
  - `badgeDespair` 绝望之死 — 琥珀 `#C07A2A`
- **背景母题**：细密个体散点汇聚为宏观福利曲线，呼应「微观选择—总量结果」的联结。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 穷人世界的观察者 / Angus Deaton 1945– + 四色 badge + 右上头像 + 国籍行（United Kingdom / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1945-10-19 爱丁堡、Hawick High School/
    Fettes College、剑桥 Fitzwilliam BA/MA/PhD 1975、导师 Stone、Bristol→Princeton 1983、
    诺奖 2015、核心领域）
03  核心贡献概览 — AIDS 需求系统 / 贫困测量 / 健康与福祉 / 绝望之死
04  苏格兰边区少年 (1945–1964) — Hawick、Fettes 基金会奖学金学者、1964 夏 Portmeirion 打工
05  剑桥岁月 (1964–1976) — Fitzwilliam 学生与 fellow；Stone 门下；应用经济系研究官员
06  布里斯托尔与弗里施奖章 (1976–1983) — 计量经济学教授；1978 首届 Frisch Medal
07  Almost Ideal Demand System (1980) — 与 Muellbauer 合创；AER 百年 top 20 论文
08  普林斯顿 (1983–) — Eisenhower 讲席教授；2017 起 USC 联合聘任；2016 荣休 Senior Scholar
09  贫困的测量 — 《The Analysis of Household Surveys》；印度贫困大辩论
10  《大逃亡》(2013) — 健康、财富与不平等的起源
11  绝望之死 (2015–2020) — 与 Case 合著 PNAS 论文：白人非西语裔中年死亡率回升；
    阿片、自杀、肝硬化；2020 成书
12  诺奖时刻 (2015) — 获奖理由；瑞典皇家科学院评语（引原文）；2015 NAS 院士、2016 受封爵士
13  荣誉与学会 — Frisch 1978、AEA 主席 2007、BBVA 2011、英国科学院 FBA、多校荣誉博士
14  遗产与结尾 — 让微观选择照亮宏观政策 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 2015 **独得**，理由 "for his analysis of consumption, poverty, and welfare"；勿写成共享 |
| 生年噪声 | frontmatter date_of_birth 双值 ["1945-10-19", "1945-00-00"]——以 infobox 正文 **1945-10-19** 为准 |
| 国籍口径 | 英美双重：page.md 正文明载 "holds both British and American citizenship"；manifest country 亦 UK/US——yaml 两条国籍，勿只写其一 |
| Stone 定性 | Richard Stone 是博士导师（1975 论文明载 under the supervision of Stone）；Stone 为 1984 诺贝尔经济学奖得主——此点 page.md 未载，**禁写**其诺奖身份 |
| Case 双重身份 | Anne Case 既是妻子又是最重要合著者——只建 **spouse** 一行（note 兼述合著），勿同人双行 |
| 子女不具名 | 两名子女仅年份（1970/1971），无姓名——不入库；"previously widowed" 前妻无姓名不入库 |
| 绝望之死表述 | Case & Deaton 2015 PNAS 论文与 2017 续作、2020 成书是**合作研究**；「绝望之死」（deaths of despair）是他们提出的分类——按 page.md 口径转述，勿引申为政治评论；Case 关于政治人物的评论是 Case 个人观点，立传可注明「Case 认为」但不入 Deaton 口 |
| 政治红线 | 2024 年 16 位诺奖得主联署公开信涉美国政党政治，立传**不写**；苏格兰独立问题 page.md 明载 Deaton 拒绝表态——照录「拒绝表态」即可，勿推断立场 |
| AER top 20 | 1980 需求论文与 AIDS 论文同属 AER 百年 top 20——是两处表述同一论文族，勿写成两篇论文各自入选 |
| Frisch 首届 | 1978 年成为**首位** Frisch Medal 得主（每两年一次授予近五年 Econometrica 应用论文）——「首届」是 page.md 明载，勿删 |
| relations 诚实值 | 仅 4 条（导师/剑桥同僚/合著者/妻子）——page.md 明载如此，防 Review 误判缺失；metadata 的 educated_at 等不产生人物边 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Almost Ideal Demand System (AIDS) | 近乎理想需求系统 | 与 Muellbauer 1980 合创；勿与疾病 AIDS 混淆（Beamer 页注意语境） |
| consumption | 消费 | 获奖理由首词 |
| welfare | 福利 | 获奖理由第三词；勿译「福利国家」 |
| deaths of despair | 绝望之死 | Case–Deaton 提出：药物酒精中毒、自杀、肝病 |
| aggregate outcomes | 总量结果 | 微观选择与总量结果的联结 |
| household surveys | 家庭调查 | 贫困测量的数据基础 |
| Frisch Medal | 弗里施奖章 | 1978 首届得主 |
| Knight Bachelor | 下级勋位爵士 | 2016 年 Queen's Birthday Honours 受封 |
| Engel curve | 恩格尔曲线 | AIDS 理论性质涉及（无需平行线性恩格尔曲线） |
| The Great Escape | 《大逃亡》 | 2013 专著；健康财富与不平等起源 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Ascension**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「攀升」呼应《大逃亡》的主题——人类整体从贫困与早夭中的大逃逸，以及 Deaton 本人从苏格兰边区小镇到普林斯顿讲席、再到斯德哥尔摩的人生爬升；曲名的上行结构亦暗合「个体选择汇聚为总量改善」的研究母题。
- **本地路径**：复制上述 wav 到 `economics/presentations/21th_century/Angus_Deaton/Ascension.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
