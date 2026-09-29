# 医学家立传提示词（Renato Dulbecco）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1975 年得主 Renato Dulbecco（雷纳托·杜尔贝科）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Renato_Dulbecco/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Renato Dulbecco（1914-02-22 生于意大利 Catanzaro ~ 2012-02-19 逝于加州 La Jolla，享年 97 岁），意大利-美国病毒学家，ForMemRS
- **气质关键词**：**动物病毒定量之父、肿瘤病毒致癌的证明者、人类基因组计划的发起人之一**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1975 条目，Dulbecco/Temin/Baltimore 三人共享）：
  > "for their discoveries concerning the interaction between tumour viruses and the genetic material of the cell"（因其关于肿瘤病毒与细胞遗传物质相互作用的发现）
- **设计母题**：**培养皿上的病毒蚀斑（plaque assay）**——让看不见的动物病毒可以被"数出来"；用「培养皿单层细胞上的蚀斑空洞」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Renato_Dulbecco/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Renato_Dulbecco/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Renato_Dulbecco_zh`、`VIDEO_NAME=Renato_Dulbecco_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Dulbecco 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学（动物病毒定量蚀斑法） | 方法学的开创使动物病毒可定量研究 | 核心页 |
| 1 | tumor virology | 肿瘤病毒学（oncoviruses） | 1975 诺奖核心：病毒基因整合致转化 | 核心页 |
| 2 | cell biology | 细胞生物学 | 细胞转化表型研究 | 核心页 |
| 3 | cancer research | 癌症研究（乳腺肿瘤干细胞） | 晚年至 2011 年 12 月的课题 | 晚年页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Giuseppe Levi | 对方 → 毕业导师 | 都灵大学病理解剖与病理学（22 岁） |
| colleague | Salvador Luria | 无向 | 都灵同学友，战后印第安纳大学噬菌体合作 |
| colleague | Rita Levi-Montalcini | 无向 | 都灵同学友，战后一同赴美 |
| advisor-student | Max Delbrück | 对方 → 噬菌体小组导师 | 1949 年夏加入其加州理工小组（库内 id=2283） |
| colleague | Marguerite Vogt | 无向 | 长期合作者（脊髓灰质炎病毒蚀斑法与肿瘤病毒研究） |
| advisor-student | Howard Martin Temin | Dulbecco → 博士生 | 1950 年代末收门下，教会二人发现逆转录酶所用方法 |
| colleague | David Baltimore | 无向 | 1965 招其加入新建索尔克研究所 |
| co-honored | David Baltimore | 无向 | 1975 诺贝尔生理学或医学奖三人共享 |
| co-honored | Howard Martin Temin | 无向 | 1975 诺贝尔生理学或医学奖三人共享 |

**不入库但提示词可叙述**：Theodore Puck 与 Harry Eagle（1973 Horwitz 奖共同得主——奖项合作非科研关系）；Nicolae Malaxa（其姻亲工业家背景 page.md 无载不入）；Vogt 之外的伦敦 ICRF 阶段同事；1986 年人类基因组计划共同发起科学家群体。

## 五、配色方案 【人物专属】

- **气质**：第勒尼安海岸的暖阳、蚀斑培养皿的冷白、都灵学派的严谨
- **主色**：`#9E2B25`（都灵红——意大利学派的赤诚与病毒学的警示色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgePlaque` 蚀斑定量法 — 都灵红 `#9E2B25`
  - `badgeOnco` 肿瘤病毒 — 深青 `#0E7490`
  - `badgeGenome` 人类基因组计划 — 深蓝 `#1E4E79`
  - `badgeStem` 肿瘤干细胞 — 赭金 `#B07D2B`
- **背景母题**：单层细胞上的蚀斑空洞与病毒颗粒剪影，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 动物病毒定量之父 / Renato Dulbecco 1914–2012 + 四色 badge + 右上头像 + 国籍行（Italy→USA）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Catanzaro 出身成长于 Imperia、都灵大学、
    印第安纳/加州理工/索尔克/伦敦 ICRF/CNR 米兰任职、诺奖 1975、核心领域；"无 PhD"注脚）
03  核心贡献概览 — 动物病毒蚀斑法 / 肿瘤病毒基因整合与细胞转化 / 乳腺癌干细胞 / HGP 发起
04  都灵三人行 (1914–1936) — Levi 门下、与 Luria 和 Levi-Montalcini 的同窗之谊——三位诺奖的起点
05  战争与抵抗 (1936–1945) — 军医征召、法国与俄国前线负伤、法西斯崩溃后加入抵抗运动
06  印第安纳与加州理工 (1946–1953) — 与 Luria 噬菌体合作、1949 夏入 Delbrück 小组、
    不到一年建立西方马脑炎病毒蚀斑法
07  蚀斑法：让动物病毒可数（核心贡献页）— 与 Vogt 用于脊髓灰质炎病毒、动物病毒定量时代开启、
    加州理工副教授→正教授
08  多瘤病毒与细胞转化 (1950s–60s) — oncovirus 致癌机制、病毒基因整合入宿主基因组
09  Temin 与 Baltimore 的老师们 — 收 Temin 门下、把蚀斑与定量方法教给两位未来的共同得主
10  1975 诺奖：三人共享 — 获奖理由逐字呈现、Temin/Baltimore 独立发现逆转录酶、
    Dulbecco 证明肿瘤表型的病毒基因整合基础
11  索尔克—伦敦—米兰 (1962–1997) — 1962 索尔克、1972 伦敦 ICRF、1993-97 回意任 CNR 米兰
    生物医学技术研究所所长、意大利体制无 PhD 的注脚
12  1986：人类基因组计划 — 发起科学家之一
13  荣誉与认可 — Lasker 1964、Marjory Stephenson+AAAS 1965、Ehrlich 1967、Horwitz 1973（与 Puck/Eagle）、
    Waksman+ForMemRS 1974、Nobel 1975、APS 1993、意大利共和国功绩勋章大军官/大十字
14  遗产与结尾 — 逆转录酶抑制剂与抗 HIV 药物的科学根基、乳腺肿瘤干细胞研究至 97 岁 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生卒口径 | 1914-02-22 Catanzaro（卡拉布里亚），成长于利古里亚 Imperia；2012-02-19 逝于 La Jolla，97 岁 |
| 国籍口径 | 意大利+美国（citation json "Italy United States"；metadata 的 Kingdom of Italy 为历史噪声不入库）——双入 Italy(0)+US(1) |
| 无 PhD | 意大利高等教育体制 1980 年前无博士学位——**"没有 PhD"是 page.md 明载事实**，勿写成"博士"；其最高学位为医学毕业（病理解剖与病理学方向） |
| 1975 三人分工 | Dulbecco=肿瘤病毒基因整合与细胞转化；Temin/Baltimore=同时独立发现逆转录酶；page.md 明载 **Dulbecco 未直接参与二人实验，但教会了他们所用方法**——"老师 shared the prize"结构如实呈现 |
| 与 Temin 边 | advisor-student（1950 年代末收为门下）+ co-honored 双边并行勿合并 |
| 与 Levi-Montalcini/Luria | 都灵 Levi 门下三同学皆获诺奖——"同窗三诺奖"叙事主线；Luria 是 colleague（都灵+印第安纳噬菌体合作），Levi-Montalcini 是 colleague（同窗同赴美），勿写成师生 |
| 战争叙事口径 | 意军军医、法俄前线负伤、费西斯政权崩溃后加入抵抗运动——page.md 实载可客观呈现，勿渲染政治立场 |
| 引语红线 | page.md 无 Dulbecco 直接引语——禁编引语 |
| 荣誉年份链 | Guggenheim（年份未载）、Lasker 1964、Marjory Stephenson+AAAS 1965、Ehrlich 1967、Horwitz 1973（与 Puck/Eagle）、Waksman 1974、ForMemRS 1974、Nobel 1975、APS 1993——勿串；意大利共和国功绩勋章大军官/大十字年份未载按名单呈现 |
| 晚年课题 | 乳腺肿瘤干细胞：单个恶性干细胞足以在小鼠诱导癌症、表观遗传修饰参与——研究持续到 2011 年 12 月（逝世前两月），是"工作到最后"的素材 |
| Known for 防混 | infobox Known for 写 reverse transcriptase——**RT 是 Temin/Baltimore 的发现**，Dulbecco 的贡献是 oncovirus 机制与定量方法学，正文以此为准 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| interaction between tumour viruses and the genetic material of the cell | 肿瘤病毒与细胞遗传物质的相互作用 | 获奖理由逐字对应 |
| oncovirus | 肿瘤病毒 | 致癌病毒类群 |
| plaque assay | 蚀斑（空斑）测定法 | 动物病毒定量的关键技术 |
| Western equine encephalitis virus | 西方马脑炎病毒 | 首个被蚀斑法定量的动物病毒 |
| cell transformation | 细胞转化 | 获得肿瘤表型的过程 |
| polyoma | 多瘤病毒 | 其主要研究病毒家族 |
| viral gene integration | 病毒基因整合 | 致癌机制核心 |
| reverse transcriptase | 逆转录酶 | Temin/Baltimore 的发现（Dulbecco 教其方法） |
| cancer stem cell | 肿瘤干细胞 | 晚年课题 |
| Human Genome Project | 人类基因组计划 | 1986 发起人之一 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从法西斯前线到抵抗运动，从都灵旧友各自星散到 97 岁仍在实验室守着乳腺癌干细胞的培养皿——Dulbecco 的背影始终带着孤独的坚韧；Lonesome 的清冷对应他一个人把动物病毒变成"可数的科学"的那段岁月，也对应暮年仍独自凝视培养皿的科学家剪影。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Renato_Dulbecco/Lonesome.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
