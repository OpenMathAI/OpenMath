# 医学家立传提示词（William C. Campbell）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2015 年得主 William C. Campbell（威廉·坎贝尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/William_C._Campbell_scientist/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：William Cecil Campbell（1930-06-28 生于爱尔兰多尼戈尔郡 Ramelton，**在世**），FRS，爱尔兰/美国双籍（1964 年入籍美国），Merck 研究所 33 年老将、Drew 大学荣休研究员
- **气质关键词**：**土壤细菌里的抗虫密码、伊维菌素的开发者、河盲症的终结者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2015 条目，Campbell/Ōmura 共享一半；屠呦呦独得另一半）：
  > "for their discoveries concerning a novel therapy against infections caused by roundworm parasites"（因其关于线虫寄生虫感染的新疗法的发现）
- **设计母题**：**一捧土壤与一条被"麻痹"的寄生虫（soil bacterium → avermectin → ivermectin）**——从 *Streptomyces avermitilis* 一株土源放线菌到大环内酯类药物；用「培养皿中的菌落与被驯服的线虫」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/William_C._Campbell_scientist/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/William_C._Campbell_scientist/`（世纪目录一律 `21th_century`，肖像见 images.txt；与 Ōmura 的斯德哥尔摩合照可作插图）。Makefile 复制后设 `MAIN=William_C._Campbell_scientist_zh`、`VIDEO_NAME=William_C._Campbell_scientist_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。**在世者注意**：封面写 b.1930，不写卒年。

## 三、研究领域梳理 + 入库 【人物专属】

**Campbell 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | parasitology | 寄生虫学 | infobox Fields 明载；肝吸虫博士论文起步 | 教育/核心页 |
| 1 | biochemistry | 生物化学 | Merck 药物研发的方法学基础 | 职业页 |
| 2 | drug discovery | 药物发现（阿维菌素/伊维菌素） | 2015 诺奖核心；亦发现噻苯咪唑（thiabendazole） | 核心页 |
| 3 | pharmacology | 药理学 | 抗寄生虫药的药效与临床转化 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Satoshi Ōmura | 无向 | Merck 团队研究 Ōmura 的链霉菌培养物，合作开发阿维菌素与伊维菌素 |
| co-honored | Satoshi Ōmura | 无向 | 2015 诺贝尔生理学或医学奖共享一半（线虫寄生虫感染的新疗法） |
| co-honored | Tu Youyou | 无向 | 2015 同届诺奖（Campbell/Ōmura 共享线虫半边，屠呦呦独得疟疾半边） |
| spouse | Mary Mastin Campbell | 无向 | 妻子 |

**不入库但提示词可叙述**：James Desmond Smyth（三一学院本科阶段"studied with"的师承线索，非导师关系，保守不入库）；父亲 R. J. Campbell（农场物资商）；Ernest Walton / Samuel Beckett（仅"第七位爱尔兰诺奖得主"的排位叙述）。

## 五、配色方案 【人物专属】

- **气质**：多尼戈尔的牧场绿、默克实验室的严谨、消除河盲症的人道暖意
- **主色**：`#146B3A`（牧场深绿——爱尔兰乡土与土壤放线菌）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgePara` 寄生虫学 — 深绿 `#146B3A`
  - `badgeDrug` 药物发现 — 深蓝 `#1E4E79`
  - `badgeGive` 无偿捐赠计划 — 赭金 `#B07D2B`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：培养皿菌落与线虫剪影交错，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 伊维菌素的开发者 / William C. Campbell b.1930 + 四色 badge + 右上头像 + 国籍行（Ireland）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生、Ramelton 出身、三一学院都柏林/威斯康星大学、
    Merck/Drew 任职、诺奖 2015、核心领域）
03  核心贡献概览 — 阿维菌素/伊维菌素 / 噻苯咪唑 / Mectizan 无偿捐赠 / 寄生虫学史写作
04  多尼戈尔少年 (1930–1952) — 牧场供应商之子、三一学院都柏林动物学一级荣誉（1952，Smyth 门下）
05  富布赖特与威斯康星 (1952–1957) — 肝吸虫博士论文、1957 PhD
06  Merck 三十三年 (1957–1990) — 噻苯咪唑（治马铃薯晚疫病——爱尔兰的历史伤痛，也治旋毛虫病）
07  Ōmura 的培养物（核心贡献页）— 链霉菌属天然菌株筛选、*S. avermitilis*、大环内酯→阿维菌素→伊维菌素
08  从马到人 (1978–1981) — 马蠕虫疗法的联想、塞内加尔与法国河盲症一期试验、口服麻痹并绝育寄生虫
09  Mectizan 捐赠计划 (1987) — 说服 Merck 无偿捐赠、与 WHO 共创"史无前例"项目、年治疗 2500 万人
10  河盲症的消除 — 哥伦比亚/厄瓜多尔/墨西哥经 Carter Center 独立验证已消除（2013 口径）
11  2015 诺奖：与 Ōmura 共享一半 — 获奖理由逐字呈现、屠呦呦独得另一半（结构讲清）
12  Drew 岁月与寄生虫学史 (1990–2010) — 指导本科生、南极探险寄生虫学史写作（Atkinson/Scott）
13  荣誉与认可 — NAS 2002、ASP 杰出服务奖 2008、FRS 2020、圣帕特里克日科学奖章 2021
14  遗产与结尾 — "全球思考、简单行事"引语、诗人与画家的一面 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名与在世口径 | **yaml/入库用 manifest 消歧义形式 "William C. Campbell (scientist)"**；1930-06-28 生于 Ramelton，**在世**——封面写 b.1930 |
| 2015 的"一半"结构 | 官方结构=**Campbell/Ōmura 两人共享一半（线虫/圆虫新疗法）+ 屠呦呦独得另一半（疟疾）**——勿写成三人平分，也勿把屠呦呦与线虫疗法混写；两人获奖理由同句 "for their discoveries..."，屠呦呦是 "for her discoveries... against malaria" |
| 与屠呦呦的边 | 屠呦呦是同届得主但工作不同半边——co-honored 边 note 已写明"同届/两半结构"，正文叙述同此口径，勿写合作 |
| 无博士导师边 | page.md 载三一学院"studied with James Desmond Smyth"（本科）与威斯康星 PhD 1957（未载导师姓名）——**不入库任何 advisor-student 边**，勿杜撰 |
| 国籍口径 | 页面 "Irish and American"、Citizenship Ireland+United States (since 1964)、citation json "Ireland United States"——两国籍并行（Ireland rank 0），封面国籍行写 Ireland 即可 |
| 分工链路 | **Ōmura 分离培养菌株 → Campbell 团队研究并改造出伊维菌素（ivermectin/Mectizan）**——方向勿颠倒；1978 马蠕虫→人用联想、1981 塞内加尔/法国一期、1987 捐赠决定 |
| 噻苯咪唑双用途 | 治马铃薯晚疫病（爱尔兰大饥荒的"历史克星"叙事可点一句）兼治人旋毛虫病——两种用途都写 |
| 引语红线 | 仅 page.md blockquote 原文可引："The greatest challenge for science is to think globally, think simply and act accordingly..."（引原文+译文）；"extraordinary efficacy" 是对药物疗效的转述引语，可小字用 |
| 河盲症数据 | 截至 2001 年每年约 2500 万人接受治疗、33 国（撒哈拉以南非洲/拉美/中东）；2013 口径下哥伦比亚、厄瓜多尔、墨西哥经 Carter Center 验证已消除——数字年份勿串 |
| 榜位叙述 | "第七位爱尔兰诺奖得主"（前有 Walton 1951 物理、Beckett 1968 文学）——排位可写，两位前人只作背景一笔 |
| 多才一面 | 已出版诗人与画家、乒乓与皮划艇——身份页调剂素材，勿喧宾夺主 |
| 对手方名 | Ōmura yaml name_en="Satoshi Ōmura"（带长音符 Ō）；屠呦呦="Tu Youyou"——yaml 均已按此形式建边 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| roundworm parasites | 线虫（圆虫）寄生虫 | 获奖理由核心词 |
| avermectin | 阿维菌素 | Ōmura 菌株产出的大环内酯类 |
| ivermectin | 伊维菌素 | 阿维菌素衍生物，人用商品名 Mectizan |
| endectocide | 内外兼杀剂 | 世界首个 endectocide（Ōmura 页措辞），新药类 |
| Streptomyces avermitilis | 阿维链霉菌 | 土源放线菌，斜体 |
| river blindness (onchocerciasis) | 河盲症（盘尾丝虫病） | 伊维菌素主适应症 |
| lymphatic filariasis | 淋巴丝虫病（象皮病） | 第二适应症 |
| thiabendazole | 噻苯咪唑 | Campbell 在 Merck 的另一发现（杀真菌剂） |
| macrocyclic lactone | 大环内酯 | 化合物类别 |
| Mectizan Donation Program | Mectizan 捐赠计划 | 1987 起，与 WHO 合作 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Tragedy 的深沉底色对应河盲症曾带给千万人的黑暗——孩童牵引领路人的青铜雕像立遍 Kitasato、WHO 与 Carter Center；而正是这悲剧的重量，反衬 Campbell 从土壤细菌中取出光明的分量。音乐以悲剧收束于救赎，贴合本篇"从黑暗到消除"的叙事弧。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/William_C._Campbell_scientist/Tragedy.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
