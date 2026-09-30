# 经济学家立传提示词（Finn E. Kydland）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2004 年得主 Finn E. Kydland（芬恩·基德兰德）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Finn_E._Kydland/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Finn Erling Kydland（1943-12-01 生于挪威罗加兰郡耶斯特尔市镇奥勒高德，在世）
- **气质关键词**：**挪威农场走出的规则设计者、时间一致性的共同揭示者、总量经济学实验室的创立人**
- **诺奖获奖理由**（2004 为共享理由年份，全句逐字引用，manifest `citation_en`/`citation_zh` 已给出）：
  > "for their contributions to dynamic macroeconomics: the time consistency of economic policy and the driving forces behind business cycles"（表彰他们对动态宏观经济学的贡献：经济政策的时间一致性与经济周期背后的驱动力量）
- **设计母题**：**规则线与分叉（rules & discretion）**——一条笔直向前延伸的金色规则线，与一条在岔口摇摆回折的灰色相机抉择曲线分道而行，是「承诺可信、规则致远」的视觉隐喻，构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Finn_E._Kydland/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Finn_E._Kydland/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Finn_E._Kydland_zh`、`VIDEO_NAME=Finn_E._Kydland_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至十二节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Kydland 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | macroeconomics | 宏观经济学 | infobox Discipline；新古典宏观学派 | 封面、核心页 |
| 1 | business cycles | 经济周期 | RBC 共同奠基；教学与研究的主线 | 核心页 |
| 2 | political economy | 政治经济学 | page.md 明载的专长领域 | 政策页 |
| 3 | labor economics | 劳动经济学 | page.md 明载的教学领域 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Edward C. Prescott | 师→生（博士导师） | 卡内基梅隆博士导师（1973），1977/1982 两篇诺奖论文合著 |
| advisor-student | David Cass | 师→生（博士导师） | infobox Doctoral advisor 明载（正文仅提 Prescott） |
| influence | Robert S. Kaplan | 无向 | infobox Influences 明载 |
| co-honored | Edward C. Prescott | 无向 | 2004 诺贝尔经济学奖共享（动态宏观经济学：时间一致性与经济周期驱动力量） |
| colleague | Edward C. Prescott | 无向 | 卡内基梅隆同事，1977《Rules Rather than Discretion》与 1982《Time to Build》合著 |
| spouse | Liv Kjellevold | 无向 | 1968 结婚，育四子 |
| spouse | Tonya Schooler | 无向 | 现妻（page.md Personal life 明载） |

**不入库但提示词可叙述**：四子 Jon Martin、Eirik、Camilla、Kari（仅具名未书姓氏，防臆造不入 parent-child）；LAEF 实验室、Hoover Institution、di Tella 大学等职务与访问任职；挪威科学与文学院等机构成员身份。

## 五、配色方案 【人物专属】

- **气质**：朴素、坚定、农场少年的长程耐心
- **主色**：`#2A3468`（规则蓝——笔直规则线的冷静底色；manifest 预分配，与同届共享得主 Prescott 同色，同批撞色为 manifest 口径）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRule` 规则 vs 相机抉择 — 规则蓝 `#2A3468`
  - `badgeRBC` 真实经济周期 — 深绿 `#175E54`
  - `badgeLAEF` 总量经济学实验室 — 琥珀 `#C07A2A`
  - `badgeFarm` 农场与早年 — 砖红 `#6E2B2B`
- **背景母题**：一条笔直的金色规则线与一条摇摆回折的灰色相机抉择曲线在画面中部同时出发、渐行渐远，呼应「承诺与信用」的核心论证。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 挪威农场的规则设计者 / Finn E. Kydland 1943– + 四色 badge + 右上头像 + 国籍行（Norway）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地奥勒高德、NHH 学士 1968、卡内基梅隆博士 1973、
    卡内基梅隆教授至 2004 → UCSB Henley 讲席、诺奖 2004、核心领域）
03  核心贡献概览 — 时间一致性 / 真实经济周期 / 政策规则 / LAEF
04  挪威农场童年 (1943–1968) — 六子女之长、Søyland 家庭农场、宽松家教、貂场记账启蒙
05  NHH 与赴美 (1968–1973) — 挪威经济学院学士、卡内基梅隆博士、Prescott 门下、Henderson 奖
06  时间一致性：规则的胜利（核心贡献页）— 1977 与 Prescott 合著 Rules Rather than Discretion、
    政策目标与个体预期的互动、可信性问题
07  真实经济周期的共同奠基 (1982)（核心贡献页）— Time to Build and Aggregate Fluctuations、
    技术冲击与约 70% 产出波动、宏观变量微观基础建模
08  卡内基梅隆岁月 (1973–2004) — 博士→NHH 助理教授→1977/1978 回卡内基梅隆（两说注记）→正教授至 2004
09  UCSB 与 LAEF (2004– ) — Henley 经济学讲席、创建总量经济学与金融实验室
10  美联储与研究网络 — Dallas/Cleveland/St. Louis 三家联储 Research Associate、
    UT Austin IC² 研究员、NHH 兼职教授、Hoover 与 di Tella 访问
11  2004 诺贝尔经济学奖 — 与 Prescott 共享（同句理由）；演讲 Quantitative Aggregate Theory (2004-12-08)
12  荣誉与认可 — 计量学会会士 1992、挪威科学与文学院院士、Oslo Business for Peace Award 2017、
    John Stauffer National Fellowship 1982–83
13  家庭与人格 — 前妻 Liv Kjellevold（1968，四子）、现妻 Tonya Schooler；农场价值与自由家教
14  遗产与结尾 — 政策规则理念、央行制度设计讨论与 RBC 传统 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享理由口径 | 2004 为共享理由年份（非拆分），manifest 全句用 "their"；co-honored note 与 Prescott 篇文案一致 |
| 博士导师双值 | infobox Doctoral advisor 载 Prescott+David Cass，正文仅 "supervised by Edward C. Prescott"；两人均入库（infobox 明载），Cass note 注明仅 infobox，禁写成正文叙述 |
| CMU 入职年份两说 | 正文 Scholarship 段作 1977 加入卡内基梅隆教职、Biography 段作 1978 回卡内基梅隆任副教授；幻灯片统一按事件叙述 **1978 回任副教授**（1977 为概述表述），陷阱表留痕 |
| 子女不入库 | Jon Martin/Eirik/Camilla/Kari 仅具名未书姓氏，防臆造不入 parent-child；幻灯片如提及仅说「四子」 |
| Business for Peace 奖 | 2017 国际商会奥斯陆 **Business for Peace Award**（商业为和平奖），非诺贝尔系列奖项，勿与和平奖混淆 |
| Kaplan 身份 | Robert S. Kaplan 按 infobox Influences 入 influence 边；库内无记录新建 stub，勿与任何同名者混淆 |
| Kydland 三行并存 | 与 Prescott：co-honored + colleague + advisor-student（对方是导师，from=Prescott）三行并存，note 各表其意 |
| 在世口径 | 1943 年生在世：封面写 1943–，身份页卒年留白，全文勿写卒年 |
| 国籍口径 | Norway 单一国籍；NHH 全称 Norwegian School of Economics (NHH)，勿写成「奥斯陆经济学院」 |
| LAEF 全称 | Laboratory for Aggregate Economics and Finance（总量经济学与金融实验室），2004 于 UCSB 创建 |
| 名字缩写 | 全名 Finn Erling Kydland，E.=Erling；yaml/manifest name_en 用 Finn E. Kydland |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| time consistency | 时间一致性 | 获奖理由核心词 |
| rules vs discretion | 规则与相机抉择 | 1977 论文核心对举 |
| real business cycle theory | 真实经济周期理论 | 1982 论文共同奠基 |
| decentralized macroeconomic planning | 分散化宏观经济规划 | 博士论文题（1973/1975 双说以正文 1973 为准） |
| aggregate economics | 总量经济学 | LAEF 名称用词 |
| political economy | 政治经济学 | page.md 明载专长 |
| labor economics | 劳动经济学 | page.md 明载教学领域 |
| monetary and fiscal policy | 货币与财政政策 | page.md 明载教学组合 |
| Research Associate | 研究员（联储体系） | 三家联储的兼职身份 |
| Business for Peace Award | 商业为和平奖 | 2017，非诺贝尔系列 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从挪威农场的日光到政策规则的坦途——「日光」的明亮坚定贴合其「规则清晰、承诺可信」的学术气质，也呼应真实经济周期「阳光下的真实力量」这一世界观。
- **本地路径**：复制 `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav` 到 `economics/presentations/21th_century/Finn_E._Kydland/Daylight.wav`
- **撞曲注记**：同届共享得主 Edward C. Prescott 同曲（manifest 同批预分配）；若出片阶段需去重，由主控统一裁定。
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Finn_E._Kydland/page.md` | 事实基准（唯一事实来源） |
| `economics/presentations/pages/21th_century/Finn_E._Kydland/metadata.json` | 结构化参考（冲突以 page.md 为准） |
| `economics/presentations/pages/21th_century/Finn_E._Kydland/images.txt` | 肖像候选 URL |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 统一封面 |
| `economics/prompt_manifest_21th.json` | 批次条目（citation_en/zh、BGM、主色） |

## 十一、执行清单 【模板通用】

1. 通读本提示词与 page.md，建立事实卡（生卒/学位/机构/奖项/关系五组）。
2. 下载肖像（images.txt 或 Commons `Special:FilePath`，500px；404 则装饰圆占位）。
3. 复制 Makefile，设 `MAIN=Finn_E._Kydland_zh`、`VIDEO_NAME=Finn_E._Kydland_zh`；复制 BGM wav。
4. 按 §六逐页写 Beamer tex；每页 `make` 检查溢出（vbox≤10pt、hbox≤50pt）。
5. `make pdf` 0 error → `pdftoppm` 逐页目检 → `make images && make video` 出 mp4。
6. 数据库已由本批次入库（has_social_data=1），立传完成后由主控将 has_biography 置 1。

## 十二、版式补遗 【模板通用】

- 表格页安全负间距：顶部 −0.35cm、`arraystretch 0.78–0.82`；公式框前 −0.35~−0.55cm。
- 文本模式希腊字母需数学模式；带圈数字需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`。
- 引号用半角 `" "`；品牌口径统一 `OpenMathAI`；`\foreach` 分隔符用 ASCII 逗号。
- 结尾页底部标注 GitHub 链接由首页模板 `\input` 继承，子 deck 不重复。
