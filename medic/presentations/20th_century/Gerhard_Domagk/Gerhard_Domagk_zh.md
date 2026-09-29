# 医学家立传提示词（Gerhard Domagk）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1939 年得主 Gerhard Domagk（格哈德·多马克）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Gerhard_Domagk/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Gerhard Johannes Paul Domagk（1895-10-30 生于勃兰登堡拉戈（今波兰境内） ~ 1964-04-24 逝于西德黑森林布尔格贝格，享年 68 岁）
- **气质关键词**：**磺胺的发现者、染色剂变良药、被纳粹禁领诺奖的化学治疗家**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1939 条目）：
  > "for the discovery of the antibacterial effects of prontosil"（因其发现百浪多息的抗菌作用）
- **设计母题**：**从染缸到药瓶（from dye vat to medicine bottle）**——偶氮染料经磺胺侧链变为人类第一种商品化抗生素；用「染料分子→细菌溶破」的渐变图形作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Gerhard_Domagk/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Gerhard_Domagk/`。Makefile 复制后设 `MAIN=Gerhard_Domagk_zh`、`VIDEO_NAME=Gerhard_Domagk_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Domagk 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | bacteriology | 细菌学 | 抗菌化学治疗，1939 诺奖核心 | 封面、核心页 |
| 1 | chemotherapy | 化学治疗 | Prontosil/磺胺；抗结核药先导 | 核心页 |
| 2 | pathology | 病理学 | 明斯特病理系出身；IG Farben 病理与细菌研究所所长 | 职业页 |
| 3 | antimicrobial chemotherapy | 抗微生物化学治疗 | Zephirol 消毒剂、E-39 抗癌药 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Max Buerger | 对方 → 导师 | 基尔博士论文《肌活动对尿肌酐排出的影响》由其指导，1921 获学位 |
| colleague | Walter Gross | 无向 | 格赖夫斯瓦尔德病理所长：任命其为初级医师、支持其吞噬研究，后邀其赴明斯特 |
| colleague | Joseph Klarer | 无向 | IG Farben 化学家，合成 KL730/磺胺米柯定（Prontosil 前体），Domagk 测试 |
| colleague | Fritz Mietzsch | 无向 | IG Farben 化学家，与 Klarer 共同合成并预言磺胺侧链价值 |
| influence | Paul Ehrlich | 对方 → 影响 | 染料作抗生素的路线源头（库内既有 id=766）；Domagk 延续其染色剂-药物思路 |
| colleague | Albert Einstein | 无向 | 1950-51 人民世界大会（PWC）共同赞助人（库内既有 id=349） |
| spouse | Gertrud Strube | 无向 | 1925 结婚，时任德国商会驻巴塞尔顾问，育三子一女 |

**不入库但提示词可叙述**：长女 Hildegarde（1935 链球菌感染被 Prontosil 救治，仅具名无科学身份，事件详述但不建边）；Leonard Colebrook（首个独立验证者，"independent" 禁写合作）；P. Eisenberg、Heinrich Hörlein、Werner Schulemann、Hans Mauss（化学供给团队旁支）；Elie Metchnikoff（吞噬作用发现者，研究主题渊源非师承）；Carl von Ossietzky（禁领奖背景人物）；Georg Hoppe-Seyler（基尔助手期雇主，仅一句带过）。

## 五、配色方案 【人物专属】

- **气质**：染料的浓烈与实验室的克制、战间期的沉重
- **主色**：`#5C3A21`（染料棕——偶氮染料与布尔格贝格的木屋）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeDye` 染料化学治疗 — 染料棕 `#5C3A21`
  - `badgeSulfa` 磺胺与 Prontosil — 深红 `#8C1F28`
  - `badgeWar` 一战与纳粹岁月 — 军灰 `#37474F`
  - `badgeTb` 结核与抗癌 — 深金 `#B8860B`
- **背景母题**：偶氮染料分子骨架向细菌溶破图谱的渐变点阵。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 磺胺的发现者 / Gerhard Domagk 1895–1964 + 四色 badge + 右上头像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、拉戈出身、基尔大学 1914 入学/1921 博士、
    IG Farben 实验病理所长 1927/1929–1961、诺奖 1939（1947 补领）、核心领域）
03  核心贡献概览 — Prontosil / 磺胺 / Zephirol / 化学治疗纲领
04  拉戈少年与一战 (1895–1918) — 志愿兵、头部中弹、战地救护；誓言引语（page.md 明载原文）
05  基尔求学 (1918–1921) — 博士论文肌酐排出，导师 Max Buerger；Hoppe-Seyler 助手
06  格赖夫斯瓦尔德与明斯特 (1923–1927) — 遇 Walter Gross；吞噬作用研究；网状内皮论文 1924
07  IG Farben 岁月 (1927–1961) — 实验病理与细菌研究所所长；染料筛选纲领（承 Ehrlich 路线）
08  KL730 与 Prontosil（核心贡献页）— Klarer/Mietzsch 合成、Domagk 小鼠实验：26 感染鼠 12 治愈 14 对照全死
09  机制的两个关键 — 活性在磺胺基非偶氮基；体外无效、体内代谢后起效
10  女儿的痊愈 (1935) — Hildegarde 缝衣针刺伤→链球菌感染→拒截肢→Prontosil 救回（叙事高点）
11  独立验证与推广 — Colebrook 产褥热临床试验（1935-36）；磺胺年代
12  诺奖风波 (1939–1947) — Ossietzky 事件→1937 禁令；电报、盖世太保拘押一周、被迫拒奖；1947 补领（无奖金）
13  战后与遗产 — 抗结核药 thiosemicarbazone/isoniazid；E-39 抗癌药 1956；皇家学会外籍会员 1959
14  结尾 — 从染缸到现代抗生素时代 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 授奖 vs 领奖 | 1939 授奖但纳粹禁止领奖（Ossietzky 事件→1937 希特勒禁令）；Domagk 曾遭盖世太保拘押一周、被逼「婉拒」；**1947 年**才领奖章与文凭，且无奖金（已退回基金会）——三个时间点勿混 |
| 政治叙事分寸 | 纳粹禁令、逮捕、宣誓效忠核查等按 page.md 事实克制陈述，聚焦其科学命运，不展开政治渲染 |
| 获奖理由 | 官方口径 "for the discovery of the antibacterial effects of prontosil"（prontosil 小写官方原文），勿扩写为「磺胺的发现」 |
| Prontosil 机制 | 活性成分是**磺胺基**而非偶氮基（当时误判）；磺胺本身无活性、经体内代谢才起效——故早期体外实验失败；两个关键点写清 |
| KL730 / D 4145 | KL=Klarer、D=Domagk 的化合物代号；Streptozon（水溶型）与 Prontosil rubrum（弱溶型）两个商品名——命名沿革勿混 |
| 三人分工 | Klarer/Mietzsch 合成、Domagk 生物学测试——合作各建一行 colleague，勿写成 Domagk 独自合成 |
| 女儿事件 | 1935-12-04 缝衣针刺伤→链球菌感染→14 处切口后医生建议截肢→Domagk 争取用 Prontosil→痊愈。详述事件但不给 Hildegarde 建库边（仅具名无科学身份） |
| Colebrook 边界 | 首个独立验证者（产褥热、64 例），明载 "independent research"——禁写为 Domagk 的合作者 |
| IG Farben 加入年份 | page.md 明载两说（1927 受邀/1929 正式，sabbatical 两年无薪）——两说并存或写「1927 受邀、1929 正式加入」 |
| Ehrlich 定位 | influence 而非师承：Ehrlich 1915 已逝，Domagk 延续其染料-药物路线（基于其亚甲蓝治疟等工作） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| sulfamidochrysoidine (KL730) | 磺胺米柯定 | Prontosil 的化学名 |
| Prontosil | 百浪多息 | 首个商品化抗生素品牌名 |
| sulfonamide | 磺胺 | 活性基团 |
| azo dye | 偶氮染料 | IG Farben 主业源头 |
| streptococcal infection | 链球菌感染 | 小鼠模型与女儿事件病原 |
| Gram-positive | 革兰阳性 | 早期小鼠实验的有效谱 |
| puerperal fever | 产褥热 | Colebrook 临床适应症 |
| Zephirol | 泽菲罗（季铵盐消毒剂） | 1932/1935；quats 之始 |
| thiosemicarbazone / isoniazid | 氨硫脲 / 异烟肼 | 抗结核后继药物 |
| E-39 | 乙撑亚胺醌类抗癌药 | 1956 报道，未进处方 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Shine Like The Sun**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Prontosil 是「人类第一种商品化抗生素」——在磺胺之前，链球菌感染近乎无药可医；「如太阳般闪耀」对应抗菌药物照亮现代医学的转折点；明亮曲调也契合 1947 年迟来八年的诺奖补领时刻。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Gerhard_Domagk/ShineLikeTheSun.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
