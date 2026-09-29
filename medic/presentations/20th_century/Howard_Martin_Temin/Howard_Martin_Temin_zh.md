# 医学家立传提示词（Howard Martin Temin）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1975 年得主 Howard Martin Temin（霍华德·马丁·特明）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Howard_Martin_Temin/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Howard Martin Temin（1934-12-10 生于费城 ~ 1994-02-09 逝于威斯康星州麦迪逊，享年 59 岁）
- **气质关键词**：**逆转录酶的发现者、中心法则的挑战者、麦迪逊的孤独先行者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1975 条目，三人共享同句）：
  > "for their discoveries concerning the interaction between tumour viruses and the genetic material of the cell"（因其关于肿瘤病毒与细胞遗传物质相互作用的发现）
- **设计母题**：**逆向的信息流（the reverse flow）**——RNA→DNA 的逆转录颠覆了单向中心法则的流行解读；用「双向箭头的螺旋与一条逆行的金色流线」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Howard_Martin_Temin/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Howard_Martin_Temin/`（1975 年像，见 images.txt）。Makefile 复制后设 `MAIN=Howard_Martin_Temin_zh`、`VIDEO_NAME=Howard_Martin_Temin_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Temin 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | Rous 肉瘤病毒与逆转录酶，1975 诺奖核心 | 封面、核心页 |
| 1 | genetics | 遗传学 | 前病毒（provirus）假说与基因组整合 | 核心页 |
| 2 | retrovirology | 逆转录病毒学 | 逆转录酶；HIV 疫苗后期研究 | 核心页 |
| 3 | oncology | 肿瘤学 | McArdle 癌症研究所；病毒致癌机制 | 职业页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Renato Dulbecco | 对方 → 导师 | Caltech 博士导师（1960 动物病毒学博士论文：Rous 肉瘤病毒与细胞的体外相互作用），博士后续留其实验室 |
| co-honored | Renato Dulbecco | 无向 | 1975 诺贝尔生理学或医学奖三人共享（官方理由句同一） |
| co-honored | David Baltimore | 无向 | 1975 诺贝尔生理学或医学奖三人共享（Baltimore 在鼠白血病病毒中独立同时发现逆转录酶；库内既有 id=5955） |
| colleague | Satoshi Mizutani | 无向 | 博士后，1969 共同搜寻 RNA→DNA 的酶 |
| advisor-student | Edward F. Fritsch | Temin → 学生 | 博士生，《Molecular Cloning》共同作者 |
| spouse | Rayla Greenberg | 无向 | 1962 结婚，UW-Madison 遗传学家，育二女 |

**不入库但提示词可叙述**：Harry Rubin（Dulbecco 实验室博士后，偶遇引其入病毒学）；Francis Crick（中心法则被误读的当事人，仅思想史叙述）；C.C. Little（Jackson 实验室项目主任，其评价引语）；父母与兄弟 Peter（经济史学家）/Michael（律师）；两名女儿。

## 五、配色方案 【人物专属】

- **气质**：逆流者的孤独与坚韧、麦迪逊的湖风、逆转录的冷光
- **主色**：`#14574B`（逆流深青——被质疑岁月里实验室的冷光）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRT` 逆转录酶 — 深青 `#14574B`
  - `badgePro` 前病毒假说 — 深蓝 `#16324F`
  - `badgeRsv` Rous 肉瘤病毒 — 暗红 `#7A1E28`
  - `badgeAids` AIDS 与公共事务 — 深金 `#B8860B`
- **背景母题**：双向箭头的双螺旋，一条金色流线逆向而行。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 逆转录酶的发现者 / Howard M. Temin 1934–1994 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、费城出身、Swarthmore BA 1955、Caltech 博士 1960、
    威斯康星麦迪逊 1960–1994、诺奖 1975、核心领域）
03  核心贡献概览 — 前病毒假说 / 逆转录酶 / 中心法则的修正 / AIDS 时代的遗产
04  费城与杰克逊实验室 (1934–1955) — 犹太家庭、社会正义价值观；高中夏校获 C.C. Little 评价引语
05  Swarthmore 与 Caltech (1955–1960) — 胚胎学起步转动物病毒学；入 Dulbecco 实验室（Rubin 偶遇引路）
06  Rous 肉瘤病毒与整合 (1957–1960) — 病毒突变改变受染细胞结构→基因组整合发生
07  麦迪逊的地下室 (1960) — McArdle 招募（彼时病毒学被认为与癌症无关）；「supremely self-confident」
08  前病毒假说（核心贡献页一）— actinomycin D 实验：前病毒是 DNA 或位于细胞 DNA 上
09  被无视的十年 — 众人斥为不可能；Crick 中心法则的流行误读 vs 其原话的区分
10  逆转录酶 (1969–1970)（核心贡献页二）— 与博士后 Mizutani 搜寻酶；Baltimore 在 MIT 独立同时发现
11  1975 三人共享诺奖 — 与 Dulbecco（导师）、Baltimore；官方理由句
12  逆转录酶的时代意义 — AIDS/HBV 的核心酶；RT-PCR 与诊断医学
13  诺奖后的公共担当 — 苏联犹太科学家的人道声援（简述）；晚宴反烟发言与移走烟灰缸；NIH/NIAID/WHO 顾问
14  家与遗产 — 妻 Rayla（遗传学家）；1994 肺癌辞世于麦迪逊（反烟者的病与志）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1975 三人共享同句理由 | 与 Dulbecco、Baltimore 共享且官方理由同句（"for their discoveries concerning the interaction between tumour viruses and the genetic material of the cell"）——引用以 citations json 逐字为准；Baltimore 于鼠白血病病毒独立同时发现，勿写两人合作 |
| Dulbecco 双线 | Caltech **博士导师** + **共同得主**两重关系，yaml 分建 advisor-student 与 co-honored 两行，勿合并 |
| 中心法则的表述精度 | page.md 明确：Crick 原话只称信息不能从蛋白质流向 DNA/RNA，**被普遍误读**为「信息只从 DNA→RNA→蛋白」——立传写「其工作修正了中心法则的流行解读」，禁写「推翻了克里克中心法则」 |
| 被质疑的岁月 | 「Many highly respected scientists disregarded his work and declared it impossible」——1960s 孤独坚持是叙事主轴，1975 后「from a rebel to a highly respected researcher」对照 |
| Mizutani 边界 | 1969 年与博士后 Mizutani 共同搜寻酶——colleague 边已建；诺奖归 Temin/Baltimore 两人，Mizutani 勿写成共同发现人 |
| 公共事务的叙事分寸 | 苏联犹太科学家声援段涉及 KGB 等，建议**简述其人道行动**（探望、赠送文献、录音公开化）不作政治渲染；反烟发言（含丹麦王后在场、移走烟灰缸）可完整保留 |
| 遗憾的对照 | 反烟倡导者 1994 死于**肺癌**——事实性呈现，不作宿命论渲染 |
| 家庭 | 妻 Rayla Greenberg（1962，遗传学家）入库 spouse；二女、兄弟 Peter/Michael 不入库（无配偶/ sibling 类型） |
| 学生 | 仅 Edward F. Fritsch 一人明载（infobox Doctoral students + Mentoring 节）；勿杜撰其他门生 |
| 会员年份 | AAAS 1973 / NAS 1974 / APS 1978 / 皇家学会外籍 1988 / 国家科学勋章 1992——五个年份勿混 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| reverse transcriptase | 逆转录酶 | 获奖成果核心；RNA 依赖的 DNA 聚合酶 |
| provirus | 前病毒 | 其命名的病毒基因组整合形式 |
| Rous sarcoma virus (RSV) | 劳氏肉瘤病毒 | 全程研究载体（鸡） |
| central dogma | 中心法则 | 表述须精确：修正流行解读而非推翻 Crick 原话 |
| actinomycin D | 放线菌素 D | 抑制 DNA 表达的关键实验试剂 |
| tumor virus | 肿瘤病毒 | 理由句核心词 |
| RT-PCR | 逆转录聚合酶链反应 | 逆转录酶的技术遗产 |
| retroviral variation | 逆转录病毒变异 | 诺奖后研究方向 |
| animal virology | 动物病毒学 | Caltech 博士方向 |
| McArdle Laboratory | 麦卡德尔癌症研究所 | UW-Madison 任职单位 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Invisible Light**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：逆转录酶在被整个学界判定「不可能」的十年里，是一束看不见的光——直到它照亮 AIDS 与乙肝的治疗路径；曲名的深邃与「逆流者终见天光」的弧线相合。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Howard_Martin_Temin/TheInvisibleLight.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
