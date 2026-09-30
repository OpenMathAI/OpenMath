# 经济学家立传提示词（Thomas Schelling）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2005 年得主 Thomas Schelling（托马斯·谢林）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Thomas_Schelling/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Thomas Crombie Schelling（1921-04-14 生于加州奥克兰 ~ 2016-12-13 逝于马里兰州贝塞斯达，享年 95 岁）
- **气质关键词**：**聚焦点的发现者、核战略的理性分析师、微观动机与宏观行为的连接者**
- **诺奖获奖理由**（2005 与 Robert Aumann 共享，逐字引用官方 citation）：
  > "for having enhanced our understanding of conflict and cooperation through game-theory analysis"（表彰他们通过博弈论分析增进了我们对冲突与合作的理解）
- **设计母题**：**聚焦点（focal point）**——在无沟通的博弈中，人们的预期不约而同汇聚于某个显著解：散落的点在画面中向一个汇聚点收拢，构成「预期收敛」的视觉隐喻；辅以悬崖边缘的渐进刻度呼应 Kinsley 转述的边缘博弈比喻。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Thomas_Schelling/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Thomas_Schelling/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Thomas_Schelling_zh`、`VIDEO_NAME=Thomas_Schelling_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Schelling 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | game theory | 博弈论 | infobox Discipline；诺奖理由核心词 | 封面、核心页 |
| 1 | conflict management | 冲突管理 | 冲突与合作的战略观，纯冲突罕见 | 核心页 |
| 2 | nuclear strategy | 核战略 | 《军备与影响》、威慑与有限战争 | 著作页 |
| 3 | bargaining theory | 议价理论 | 聚焦点、可信承诺、默契合谋 | 著作页 |
| 4 | social dynamics | 社会动态学 | 种族居住隔离的 tipping 模型 | 微观动机页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 13 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Arthur Smithies | 师→生（博士导师） | 哈佛博士导师（infobox 明载三人之一） |
| advisor-student | Wassily Leontief | 师→生（博士导师） | 哈佛博士导师，1973 诺奖得主（infobox 明载） |
| advisor-student | James Duesenberry | 师→生（博士导师） | 哈佛博士导师（infobox 明载） |
| influence | Carl von Clausewitz | 无向 | infobox Influences 明载 |
| influence | Niccolò Machiavelli | 无向 | infobox Influences 明载 |
| advisor-student | Michael Spence | Schelling→学生 | infobox Doctoral students；2001 诺奖得主 |
| advisor-student | Eli Noam | Schelling→学生 | infobox Doctoral students 明载 |
| advisor-student | Tyler Cowen | Schelling→学生 | infobox Doctoral students 明载 |
| co-honored | Robert Aumann | 无向 | 2005 诺奖共享（同句理由：博弈论分析增进对冲突与合作的理解） |
| collaborator | Morton Halperin | 无向 | 1961 合著《Strategy and Arms Control》 |
| influence | Robert Jervis | 无向 | page.md 明载 Schelling's work influenced Jervis |
| spouse | Corinne Tigay Saposs | 无向 | 1947–1991 结婚，育四子 |
| spouse | Alice M. Coleman | 无向 | 1991 再婚，带来二继子 |

**不入库但提示词可叙述**：四子与二继子（page.md 未具名）；Stanley Kubrick 与 Peter George（《奇爱博士》缘起仅为对话往来，一次性事件）；Michael Kinsley（其学生、专栏作家，悬崖比喻的转述者）；家人将奖章拍卖 18.7 万美元捐南方贫困法律中心（客观事实可叙述）。

## 五、配色方案 【人物专属】

- **气质**：冷静、克制、危机边缘的理性
- **主色**：`#37548D`（战略蓝——冷战桌前深夜推演的沉静底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGame` 博弈论 — 战略蓝 `#37548D`
  - `badgeNucl` 核战略 — 深红 `#7E1E23`
  - `badgeBarg` 议价与聚焦点 — 青绿 `#0E7C7B`
  - `badgeSoc` 社会动态 — 琥珀 `#C07A2A`
- **背景母题**：散点向单一聚焦点收敛的连线网络（预期收敛），辅以棋盘格上的硬币排布（隔离模型演示）。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 聚焦点的发现者 / Thomas Schelling 1921–2016 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地奥克兰、教育 Berkeley BA 1944/Harvard PhD 1951、
    任职 Yale→Harvard→Maryland、诺奖 2005、核心领域）
03  核心贡献概览 — 聚焦点 / 可信承诺 / 核战略议价 / 隔离 tipping 模型
04  早年与政府岁月 (1921–1953) — 圣迭戈中学、Berkeley 经济学学士、马歇尔计划与白宫、夜间写博士论文
05  哈佛博士与耶鲁任教 (1951–1958) — 三位博士导师、RAND 兼任研究员
06  《冲突的战略》(1960)（核心贡献页）— 聚焦点、可信承诺、纯冲突罕见；TLS 评选 1945 以来百大最具影响
07  核战略的理性分析 — 《军备与影响》(1966)：暴力外交、相互警报的动力学
08  默契沟通与边缘博弈 — tacit maneuvers；Kinsley 悬崖比喻（注明转述出处）
09  微观动机与宏观行为 (1978) — 硬币棋盘演示、tipping 与居住隔离
10  全球变暖的议价视角 — 1980 卡特委员会、减排收益归穷国成本归富国的议价结构（客观转述）
11  从哈佛到马里兰 (1990–2016) — 肯尼迪学院缔造者之一、马里兰公共政策学院、AEA 主席 1991
12  荣誉与认可 — Nobel 2005（与 Aumann 共享）· Seidman Award 1977 · NAS 核战争预防研究奖 1993 · 名誉博士
13  大众文化影响 — 《奇爱博士》缘起、"collateral damage" 一词 1961 首用、《Choice and Consequence》
14  遗产与结尾 — 从博弈论到复杂系统（NECSI co-faculty）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享同句理由 | 2005 与 Aumann 共享，官方理由逐字 "for having enhanced our understanding of conflict and cooperation through game-theory analysis"；勿写成两人各半或理由分立 |
| 三位博士导师 | Smithies / Leontief / Duesenberry 均为 infobox Doctoral advisor 明载；正文只提 Harvard PhD 1951，勿杜撰主次 |
| 学生规范名 | infobox 作 "A. Michael Spence"，入库用规范名 **Michael Spence**（2001 诺奖得主，与 batch-01 对手方同名匹配）；勿写成 Michael Spence 之外的变体 |
| Aumann 规范名 | 入库用 **Robert Aumann**（batch-02 同名匹配）；库内另有 Georg Aumann（数学家）勿混 |
| Jervis 方向 | 是"谢林的工作影响了 Jervis"，不是 Jervis 影响谢林；note 须写清 |
| 引语红线 | 悬崖比喻是 Michael Kinsley 的转述（华盛顿邮报专栏、谢林前学生），须注明"Kinsley 转述"，不可当作谢林原话；page.md 无谢林本人英文原话，中文引号内禁写"原话" |
| 全球变暖表述 | 谢林认为气候变化对发展中国家威胁严重、对美国威胁被夸大——这是 page.md 明载立场，**客观转述不作评价**；其 GDP 户外产出引文可引原文 |
| 政治红线 | 不展开冷战政治评价、不作军备政策立场表态；Marshall Plan/White House 履历仅客观一句 |
| metadata 冲突 | metadata.json 无卒日噪声；frontmatter 与 infobox 生卒一致（1921-04-14 / 2016-12-13），以正文为准 |
| 书名与概念 | 聚焦点 focal point 勿写成 "Schelling point" 泛称；egonomics 是其自创词；Hobbesian trap 别名 Schelling's dilemma 仅 see also 级别提及 |
| 奖章拍卖 | 家人拍卖奖章得 $187,000 捐 SPLC，附其妻 Alice 转述其最影响他的书是 *Smoky the Cowhorse*——客观事实，注意是家人转述 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| focal point | 聚焦点 | 无沟通博弈中的显著收敛解，勿译"焦点"泛化 |
| credible commitment | 可信承诺 | 战略约束自身以取信对手 |
| brinkmanship | 边缘博弈/边缘政策 | see also 级别概念 |
| tacit maneuvers | 默契行动 | 以行动代替沟通的信号 |
| tipping point | 倾斜点 | 隔离动态的临界转折 |
| deterrence | 威慑 | 核战略核心词 |
| arms control | 军备控制 | 与 disarmament（裁军）层次不同 |
| Micromotives and Macrobehavior | 微观动机与宏观行为 | 1978 书名，勿与 1969/1971 论文混 |
| collateral damage | 附加损伤 | 1961 文章已知首用 |
| pure conflict | 纯冲突 | 利益完全对立的罕见情形 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Savage**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：冷峻、张力、博弈对峙——"Savage" 的原始张力恰好对应核威慑博弈中「理性与毁灭共舞」的战略美学；聚焦点与边缘博弈的叙事在冷峻节奏中层层推进。
- **本地路径**：复制 `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav` 到 `economics/presentations/21th_century/Thomas_Schelling/Savage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
