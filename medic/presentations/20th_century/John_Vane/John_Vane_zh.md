# 医学家立传提示词（John Vane）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：John Vane（1982 年诺贝尔生理学或医学奖得主，英国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/John_Vane/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir John Robert Vane（约翰·罗伯特·文，1927-03-29 伍斯特郡塔德比格 ~ 2004-11-19 肯特郡，享年 77 岁）
- **气质关键词**：**揭开阿司匹林奥秘的药理学家、前列环素的发现团队掌门、ACE 抑制剂与 COX-2 药物浪潮的源头** —— 1982 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Bergström、Samuelsson 三人共享）：
  > "for their discoveries concerning prostaglandins and related biologically active substances"
  > （因其关于前列腺素及相关生物活性物质的发现）
- **设计母题**：**「一粒阿司匹林的机关」**。百年老药阿司匹林靠阻断前列腺素合成而止痛消炎——视觉隐喻：一粒药片剖面中，被闸门拦住的级联反应管道。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/John_Vane/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/John_Vane/`，成目录 `medic/presentations/20th_century/John_Vane/`，Makefile 复制后设 `MAIN=John_Vane_zh`、`VIDEO_NAME=John_Vane_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pharmacology | 药理学 | 阿司匹林机理与生物检定，1982 诺奖核心 | 总览页 |
| 1 | prostaglandins | 前列腺素 | 阿司匹林抑制前列腺素合成的机理（与 Piper 合著） | 机理页 |
| 2 | bioassay | 生物检定 | 其自创的级联灌流生物检定技术 | 技术页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/John_Vane.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Geoffrey S. Dawes | 师 | 牛津博士导师，1953 年获 DPhil |
| influence | Harold Burn | — | 1946 年入其牛津药理学系，从此爱上药理学 |
| co-honored | Sune Bergström | — | 1982 诺贝尔生理学或医学奖三人共享（前列腺素等） |
| co-honored | Bengt I. Samuelsson | — | 1982 诺贝尔生理学或医学奖三人共享（前列腺素等） |
| collaborator | Salvador Moncada | — | 携其赴 Wellcome 建前列腺素研究部，共发现前列环素 |
| collaborator | Priscilla Piper | — | 合著阿司匹林与前列腺素关系论文（1982 诺奖核心） |
| spouse | Elizabeth Daphne Page | — | 1948 年成婚，2021 年卒 |
| parent-child | Maurice Vane | 父 | 俄国犹太移民之子 |
| parent-child | Frances Vane | 母 | 伍斯特郡农家出身 |

> 说明：Dawes 师生边 body+frontmatter 双载，无争议。Burn 是引路人（「Under Burn's guidance...found motivation and enthusiasm for pharmacology」）建 influence。Stacey（推荐他的化学教授）为过场不入库。两个女儿未具名不入库。1977 Lasker 与 1982 Nobel 均基于前列环素/前列腺素工作——与 Moncada 的合作是团队叙事（其领导下发现前列环素），以 collaborator 边承载。

## 五、配色方案 【人物专属】

- **气质**：英伦实验药理学的老派功夫、工业研究所的果断、维多利亚老医院的复兴者
- **主色**：药片象牙白金 `#B8946A`（阿司匹林的药片暖调）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 药理学 — 灌流青 `#2E7A8C`
  - `badgeB` 前列腺素 — 级联橙 `#C08A2E`
  - `badgeC` 生物检定 — 器官浴灰 `#8A8F98`
  - `badgeD` 临床转化 — 血管红 `#A83A4A`
- **背景母题**：级联灌流管路示意（器官浴串联）与药片剖面圆，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 揭开阿司匹林奥秘的人 / John Vane 1927–2004 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — 阿司匹林机理 / 前列环素 / ACE 抑制剂先声 / 生物检定技术
04  伯明翰少年 (1927–1944) — 俄裔犹太移民祖父、伍斯特农家母亲、King Edward's School 的化学兴趣
05  伯明翰-牛津 (1944–1953) — 化学失望但爱实验、Stacey 推荐、Burn 门下找到药理学的热情、1953 牛津 DPhil（Dawes 指导）
06  耶鲁与伦敦 (1953–1966) — 耶鲁助理教授、伦敦基础医学科学研究所高级讲师
07  皇家外科学院教授 (1966–1973) — 生物检定技术、ACE 与阿司匹林双线
08  与 Piper 的关键论文（核心页）— 阿司匹林与前列腺素关系的合著论文——1982 诺奖的直接来源
09  Wellcome 研究所长 (1973–1985)（核心页）— 携同事转战工业界、Moncada 领导的前列腺素研究部、前列环素的发现
10  1982 诺贝尔奖（核心页）— citation 原文、三人共享（瑞典结构化学+英国机理的两支拼图）、诺奖讲坛
11  威廉哈维研究所 (1985–) — 圣巴托罗缪医院旧地重建研究所、COX-2 选择性抑制剂、NO/内皮素与血管调控
12  荣誉链 — FRS 1974 · Lasker 1977（前列环素）· Nobel 1982 · knighthood 1984 · Royal Medal 1989 · Golden Plate 2000
13  药物浪潮的源头 — ACE 抑制剂（高血压）、前列环素类似物、COX-2 药物——一条机理通向三代药物
14  晚年与身后 — 2004 年 5 月摔伤骨折、11 月 19 日并发症辞世；Lady Vane 2021 年卒
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries concerning prostaglandins and related biologically active substances"（their 三人共享同一理由） |
| 2 | 三人分工 | 瑞典系（Bergström/Samuelsson）做结构与下游产物、Vane 做阿司匹林机理（抑制前列腺素合成）——Vane 页主打「机理」叙事，与两篇瑞典篇区分 |
| 3 | 诺奖核心论文 | 与 Priscilla Piper 合著的阿司匹林-前列腺素关系论文是诺奖直接来源——Piper 建 collaborator 边、正文给足戏份，勿只写 Moncada |
| 4 | 前列环素 | 发现于 Wellcome 时期（Moncada 领导的研究部）、Lasker 1977 即因此——「prostacyclin」是团队成果，正文明载 Vane 携同事赴 Wellcome 的团队叙事 |
| 5 | ACE 抑制剂 | 其 ACE 研究最终「leading to the introduction of ACE inhibitors」——是基础贡献转译为药物，勿写成其本人发明某种具体降压药 |
| 6 | 引语红线 | Burn 实验室的引语（the laboratory gradually became...）有英文原文可引；其余叙事无直接引语，禁编造 |
| 7 | 犹太裔背景 | 父亲系俄国犹太移民之子——身份页一句家世叙述，不展开 |
| 8 | 死因 | 2004 年 5 月腿部与髋部骨折、11 月 19 日死于长期并发症（Princess Royal University Hospital）——时间线勿错；与 Bergström 同年（2004）辞世可作对照帧 |
| 9 | 荣誉年代链 | FRS 1974 · Lasker 1977 · Nobel 1982 · knighthood 1984 · Royal Medal 1989 · Golden Plate 2000，勿错置；Fu Jen 2011 荣誉博士（辅仁大学）可提 |
| 10 | metadata 冲突 | frontmatter doctoral_advisor=Geoffrey S. Dawes 与正文 supervised by Dawes 双载一致；education 双校（Birmingham BSc/Oxford DPhil）分清 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| aspirin | 阿司匹林 | 机理为抑制前列腺素合成 |
| prostacyclin | 前列环素（PGI2） | Wellcome 团队发现 |
| ACE (angiotensin-converting enzyme) | 血管紧张素转化酶 | ACE 抑制剂药物源头 |
| bioassay | 生物检定 | 其级联灌流技术 |
| COX-2 | 环氧化酶-2 | 晚年选择性抑制剂方向 |
| nitric oxide / endothelin | 一氧化氮 / 内皮素 | 晚年血管调控双线 |
| Royal College of Surgeons | 皇家外科学院 | 1966 教授任所 |
| Wellcome Foundation | 威康基金会（药厂） | 1973-85 研究所长 |
| William Harvey Research Institute | 威廉哈维研究所 | 1985 年创立 |
| Lasker Award | 拉斯克奖 | 1977（前列环素） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「锐利/强力」匹配阿司匹林机理的一击致命式发现——百年老药的奥秘被一次级联灌流实验切开
  - 也匹配其从学界转战工业研究所的果断性格
- **备选**（未采用）：Last Hope（药物救人意象贴切但留给更绝望题材）、Daylight（本批 Samuelsson 已用，三人组区分）
- **本地路径**：按 music_audio/ 内 Alex-Productions Savage 曲目复制至 `medic/presentations/20th_century/John_Vane/Savage.wav`，ffmpeg `-shortest` 对齐
