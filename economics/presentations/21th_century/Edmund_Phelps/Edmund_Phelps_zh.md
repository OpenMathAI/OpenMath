# 经济学家立传提示词（Edmund Phelps）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2006 年得主 Edmund Phelps（埃德蒙·费尔普斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Edmund_Phelps/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Edmund Strother Phelps（1933-07-26 生于伊利诺伊州埃文斯顿 ~ 2026-05-15 逝于纽约曼哈顿，享年 92 岁，死于阿尔茨海默病）
- **气质关键词**：**自然失业率的命名者、宏观微观基础的奠基人、大众繁荣的歌者**
- **诺奖获奖理由**（2006 单独得主，逐字引用官方 citation）：
  > "for his analysis of intertemporal tradeoffs in macroeconomic policy"（表彰他对宏观经济政策中跨期权衡的分析）
- **设计母题**：**跨期权衡（intertemporal tradeoff）**——今日消费与明日积累的天平：一条黄金律增长曲线与失业率的自然水平线交织，构成「短期与长期之间往复权衡」的视觉隐喻。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Edmund_Phelps/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Edmund_Phelps/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Edmund_Phelps_zh`、`VIDEO_NAME=Edmund_Phelps_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Phelps 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | macroeconomics | 宏观经济学 | infobox Discipline；诺奖理由核心 | 封面、核心页 |
| 1 | unemployment theory | 失业理论 | 自然失业率的存在与决定机制 | 核心页 |
| 2 | economic growth | 经济增长 | 黄金律储蓄率（1961） | 增长页 |
| 3 | labor economics | 劳动经济学 | 菲利普斯曲线的微观基础与预期 | 菲利普斯页 |
| 4 | innovation economics | 创新经济学 | 大众繁荣、经济活力与包容性增长 | 晚期页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 23 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | James Tobin | 师→生（博士导师） | 耶鲁博士导师（infobox 明载），诺奖得主 |
| advisor-student | Arthur Okun | 师→生（博士导师） | infobox Doctoral advisor 明载；Cowles 时期交往 |
| influence | William Fellner | 无向 | 其课程强调行为人预期，对 Phelps 影响甚深 |
| influence | Thomas Schelling | 无向 | 耶鲁求学期间曾随其学习（studied under） |
| influence | Robert Solow | 无向 | Cowles 时期新古典增长理论追随其开创性工作 |
| influence | John Rawls | 无向 | 斯坦福中心相识，《正义论》思想促成其经济正义研究 |
| influence | John von Neumann | 无向 | 黄金律储蓄率概念与其工作相关 |
| colleague | Paul Samuelson | 无向 | 1962–63 MIT 访问期间交往 |
| colleague | Franco Modigliani | 无向 | 1962–63 MIT 访问期间交往 |
| colleague | Amartya Sen | 无向 | 1969–70 斯坦福行为科学高级研究中心讨论 |
| colleague | Kenneth Arrow | 无向 | 斯坦福中心讨论；1990 EBRD 莫斯科之行共同设计改革方案 |
| collaborator | David Cass | 无向 | 增长理论合作 |
| collaborator | Tjalling Koopmans | 无向 | 增长理论合作，未来诺奖得主 |
| collaborator | Guillermo Calvo | 无向 | 不对称信息下最优契约与粘性工资研究合作 |
| collaborator | John B. Taylor | 无向 | 1977 论文合著（理性预期下货币政策稳定力） |
| advisor-student | Roman Frydman | Phelps→学生 | page.md 明载 former student |
| collaborator | Roman Frydman | 无向 | 理性预期批判研究合作（1981 会议/1983 文集） |
| collaborator | Jean-Paul Fitoussi | 无向 | 欧洲高失业研究合著（OFCE 院长） |
| collaborator | Luigi Paganetto | 无向 | 罗马第二大学紧密合作，1988–98 Villa Mondragone 研讨会共同组织 |
| advisor-student | Gylfi Zoega | Phelps→学生 | infobox Doctoral students 明载 |
| collaborator | Raicho Bojilov | 无向 | 《Dynamism》(2020) 合著者 |
| collaborator | Hian Teck Hoon | 无向 | 《Dynamism》(2020) 合著者 |
| spouse | Viviana Montdor | 无向 | 1974 结婚 |

**不入库但提示词可叙述**：James Nelson（Amherst 授课教师，用 Samuelson 教材启蒙，非其本人关系边）；Vickrey/Heckman/Mundell（哥伦比亚同事群体仅正文叙述）；Lucas/Muth（理性预期论战对手，属学术史叙述非持续关系）；Carol Shaw 等 metadata-only 人物。

## 五、配色方案 【人物专属】

- **气质**：温厚、思辨、跨越半个世纪的宏观长河
- **主色**：`#0B5351`（深青——增长与就业长期均衡的沉稳底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMacro` 宏观理论 — 深青 `#0B5351`
  - `badgeGrowth` 增长与黄金律 — 金棕 `#B08A2E`
  - `badgeLabor` 就业与自然率 — 砖红 `#8C3A2B`
  - `badgeDynam` 创新与活力 — 靛蓝 `#2A4B7C`
- **背景母题**：天平两端的时间刻度（今日消费 vs 未来积累），辅以缓慢上扬的增长曲线与水平自然率线的交汇。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 自然失业率的命名者 / Edmund Phelps 1933–2026 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地埃文斯顿、教育 Amherst BA 1955/Yale PhD 1959、
    任职 Cowles→Penn→Columbia、诺奖 2006、核心领域）
03  核心贡献概览 — 黄金律储蓄率 / 预期加强菲利普斯曲线 / 自然失业率 / 大众繁荣
04  早年与求学 (1933–1959) — 埃文斯顿、Hastings-on-Hudson、Amherst 经济学启蒙、耶鲁师从 Tobin
05  Cowles 基金会岁月 (1960–1966) — 黄金律储蓄率 1961、与 Cass/Koopmans 合作、MIT 访问 1962–63
06  黄金律储蓄率（核心贡献页）— 一国应在当期消费与未来积累间如何取舍；von Neumann 渊源
07  宾大与预期加强菲利普斯曲线 (1966–1971) — 1967/1968 论文、不完全信息与预期
08  自然失业率（核心贡献页）— 长期无失业-通胀权衡、需求管理只有暂时效应；"Phelps volume" 1969 会议
09  哥伦比亚与理性预期论战 (1971–) — 与 Calvo/Taylor 重建凯恩斯主义、与 Frydman 质疑理性预期
10  统计性歧视与经济正义 (1972) — Rawls 影响、新领域开创
11  结构性衰退与大众繁荣 (1994–2013) — Structural Slumps、Mass Flourishing、经济活力与包容
12  荣誉与认可 — Nobel 2006 · NAS 1981 · 法军团骑士 2008 · 基尔全球经济奖 · 中国友谊奖 2014 · 名誉博士多校
13  中国结缘与晚年 — 新华都商学院院长 (2010–2016)、清华/北大名誉讲授、2026-05-15 曼哈顿辞世
14  遗产与结尾 — 从微观基础到创新社会的宏观经济学 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生卒口径 | 1933-07-26 ~ **2026-05-15**（曼哈顿，阿尔茨海默病，享年 92）——本页为最新逝世事实，封面/身份页/时间线务必按 page.md 写卒年，勿写"在世" |
| 博士导师口径 | infobox=Tobin+Okun；frontmatter=Fellner+Tobin；正文 studied under Tobin & Schelling。**裁定：advisor-student 只入 Tobin/Okun（infobox 明载）；Fellner/Schelling 入 influence**，防止过度声明 |
| 自然率命名 | 1967 论文中 Phelps 标注 U* 为 equilibrium/warranted rate，**后来才改用 natural rate 一词**（Moorthy 2026 注）——勿写"1967 年首创 natural rate 术语" |
| 获奖理由 | 官方 citation 逐字 "for his analysis of intertemporal tradeoffs in macroeconomic policy"（manifest 作 intertemporal 连写；page.md Honors 节作 inter-temporal 连字符——用 manifest 官方连写形式）；瑞典科学院另句 "deepened our understanding of the relation between short-run and long-run effects of economic policy" 是表述区别，勿混用 |
| 单独得主 | 2006 为 Phelps 单独获奖（非共享），勿写"共享" |
| 政治红线 | 对 Trump 经济政策的批评与 2024 年 16 位诺奖得主联名信属政治内容，**禁写入稿**；2020 紫色经济联署仅客观一句或不写 |
| 中国关联客观记录 | 2014 中国政府友谊奖、2010–2016 闽江学院新华都商学院院长、清华名誉博士 2007——客观记录、不作评价 |
| 不入库边界 | MIT "in contact with" 三人（Samuelson/Solow/Modigliani）只入 Samuelson/Modigliani colleague；**Solow 入 influence**（思想源头），勿建重复 colleague 边 |
| 妻与子女 | 妻 Viviana Montdor（1974 结婚）入库；page.md 无子女记载，勿编造；"不拥有汽车"轶事可作花絮 |
| 引语红线 | 2008 年批评"虚假"新古典模型段有英文原文（Keynes "modernist stuff" 等）——引原文须注明是 Phelps 文章引述 Keynes 之语，非 Phelps 原话 |
| metadata 冲突 | frontmatter 卒日 2026-05-15 与正文一致；metadata 无噪声 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| natural rate of unemployment | 自然失业率 | 勿与 NAIRU 混同表述 |
| golden rule savings rate | 黄金律储蓄率 | 1961 论文核心，与冯·诺依曼 related |
| expectations-augmented Phillips curve | 预期加强菲利普斯曲线 | 1967/1968 论文核心 |
| microfoundations | 微观基础 | 不完全信息+预期支撑宏观理论 |
| adaptive expectations | 适应性预期 | 与 rational expectations 层次不同 |
| hysteresis | 滞后效应 | 1972 书引入（失业部分不可逆） |
| statistical discrimination | 统计性歧视 | 1972 开创领域，勿译"统计歧视"简写失真 |
| structural slumps | 结构性衰退 | 1994 书名，非货币机制解释 |
| inclusive economy / economic inclusion | 包容性经济 | 1990s 中期转向 |
| mass flourishing | 大众繁荣 | 2013 书名固定译法 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：深沉、悲悯、史诗感——匹配费尔普斯一生关注失业者命运的底色（结构性衰退、滞后效应、包容性经济）；晚年阿尔茨海默病中辞世为传记收束添一层挽歌气质；"Tragedy" 的厚重弦乐贴合宏观经济学「跨期权衡」的宏大命题。
- **本地路径**：复制 `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav` 到 `economics/presentations/21th_century/Edmund_Phelps/Tragedy.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
