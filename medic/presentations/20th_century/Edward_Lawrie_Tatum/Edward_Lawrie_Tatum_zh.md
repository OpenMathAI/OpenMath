# 医学家立传提示词（Edward Lawrie Tatum）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1958 年得主 Edward Lawrie Tatum（爱德华·劳里·塔特姆）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Edward_Lawrie_Tatum/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Edward Lawrie Tatum（1909-12-14 生于科罗拉多州博尔德 ~ 1975-11-05 逝于纽约，享年 65 岁），美国遗传学家，NAS/APS/AAAS 三院会员
- **气质关键词**：**一基因一酶的实验家、红色面包霉的驯服者、Lederberg 的博士导师**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1958 条目，Tatum/Beadle 共享一半；Lederberg 独得另一半）：
  > "for their discovery that genes act by regulating definite chemical events"（因其发现基因通过调控特定化学反应而起作用）
- **设计母题**：**射线诱变的红色面包霉与营养缺陷型（X-ray → Neurospora mutants → one gene-one enzyme）**；用「培养管中的橙红霉与代谢通路阻断点」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Edward_Lawrie_Tatum/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Edward_Lawrie_Tatum/`（肖像见 images.txt；本页无头像图则装饰圆占位）。Makefile 复制后设 `MAIN=Edward_Lawrie_Tatum_zh`、`VIDEO_NAME=Edward_Lawrie_Tatum_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Tatum 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | genetics | 遗传学 | infobox Fields 明载 | 全篇 |
| 1 | biochemical genetics | 生化遗传学（一基因一酶） | 1958 诺奖核心 | 核心页 |
| 2 | microbial genetics | 微生物遗传学 | 细菌遗传学、E. coli 接合 | 研究页 |
| 3 | biochemistry | 生物化学 | 色氨酸生物合成途径 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | George Wells Beadle | 无向 | 1937 年起斯坦福合作，Neurospora 生化突变研究（1941），一基因一酶 |
| co-honored | George Wells Beadle | 无向 | 1958 诺贝尔生理学或医学奖共享一半 |
| co-honored | Joshua Lederberg | 无向 | 1958 同届诺奖（Lederberg 独得细菌遗传重组一半） |
| advisor-student | Joshua Lederberg | Tatum → 博士生 | 耶鲁博士导师（1947，大肠杆菌遗传重组；亦为合作发现细菌接合） |
| advisor-student | Carolyn Slayman | Tatum → 博士生 | infobox Doctoral students 明载 |
| advisor-student | Esther Lederberg | Tatum → 门下学生 | infobox Other notable students 明载，Joshua 之妻 |
| spouse | Elsie Bergland | 无向 | 最后一任妻子（1998 年去世） |

**不入库但提示词可叙述**：父亲 Arthur L. Tatum（威斯康星药理学教授——家学渊源可叙述，亲子边不建）；博士导师无载（威斯康星 1934 博士，**勿杜撰 advisor 边**）；与 Beadle 的合作由 colleague+co-honored 双边承载。

## 五、配色方案 【人物专属】

- **气质**：威斯康星的湖蓝、Neurospora 的橙红、实验记录本的克制
- **主色**：`#27548C`（威斯康星蓝——湖畔校园与博士岁月）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGene` 一基因一酶 — 深蓝 `#27548C`
  - `badgeMold` 红色面包霉 — 砖橙 `#C1502E`
  - `badgeMicro` 微生物遗传学 — 青灰 `#0E7490`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：培养管中的霉丝与代谢通路阻断点，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 一基因一酶的实验家 / Edward Lawrie Tatum 1909–1975 + 四色 badge + 头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、博尔德出身、芝加哥大学/威斯康星大学、
    斯坦福/耶鲁/洛克菲勒研究所任职、诺奖 1958、核心领域）
03  核心贡献概览 — Neurospora 生化突变 1941 / 一基因一酶 / E. coli 接合 / 色氨酸途径
04  化学家之子 (1909–1931) — 父亲威斯康星药理学教授、芝加哥两年转威斯康星、1931 BA
05  威斯康星博士 (1931–1934) — 《微生物的生物化学研究》论文、果蝇早期工作
06  斯坦福与 Beadle 相遇 (1937–1945) — 果蝇合作转向 Neurospora、X 射线诱变
07  1941：营养缺陷型三突变体（核心贡献页）— 最小培养基+单一补加物、代谢通路单步阻断
08  一基因一酶假说（核心页）— 基因调控特定化学反应、遗传学根本革命的口径
09  耶鲁与 Lederberg (1945–1948) — 指导 Lederberg 发现 E. coli 接合（1946-47）
10  1958 诺奖：与 Beadle 共享一半 — 获奖理由逐字呈现、Lederberg 独得另一半（结构讲清）
11  洛克菲勒岁月 (1957–1975) — 最后的执教地、色氨酸生物合成与细菌遗传学
12  荣誉与认可 — NAS 1952、APS 1957、AAAS 1959、Remsen Award
13  门生谱系 — Lederberg（1958 诺奖）、Carolyn Slayman、Esther Lederberg
14  遗产与结尾 — 分子遗传学的实验范式、65 岁早逝（心肺疾患）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | **yaml/入库用 manifest 形式 "Edward Lawrie Tatum"**；封面写 Edward L. Tatum 或全名均可 |
| 1958 的"一半"结构 | **Tatum/Beadle 共享一半（基因调控化学反应）+ Lederberg 独得另一半（细菌重组）**——勿三人平分；与 Beadle 同句理由（"for their discovery..."），与 Lederberg 理由不同句 |
| 与 Lederberg 双边 | co-honored（同届）+ advisor-student（耶鲁博士导师）两条边并行勿合并；接合（conjugation）发现是师生合作 |
| 无博士导师边 | 威斯康星 1934 博士论文《微生物的生物化学研究》，**page.md 未载导师姓名**——勿杜撰；父亲 Arthur L. Tatum 是威斯康星药理学教授（家学渊源），亲子边不建 |
| 学生边方向 | Slayman/Esther 是**其学生**（infobox Doctoral students / Other notable students），yaml 用 direction: student；Esther 同时是 Tatum→学生 与 Joshua→配偶/同事——三角关系各归其位，勿混写 |
| 死因口径 | 重度吸烟者，死于心力衰竭并发慢性肺气肿（1975-11-05，纽约）——可客观写"心肺疾患"，吸烟细节可一句带过 |
| 职年链 | 芝加哥两年 → 威斯康星 BA 1931/PhD 1934 → 斯坦福 1937 → 耶鲁 1945 → 斯坦福 1948 → 洛克菲勒研究所 1957 直至去世——六段勿串 |
| Neurospora 论文 | 1941 年发表生化突变先驱研究（与 Beadle）；X 射线诱变红色面包霉——勿写成"发现链霉菌/大肠杆菌"（那是 Lederberg/Ōmura 线） |
| 引语红线 | page.md 全篇无直接引语——禁编引语 |
| 荣誉年份 | NAS 1952、APS 1957、AAAS 1959、Remsen Award（metadata 有载年份不详）——荣誉页按此呈现 |
| 果蝇→霉菌转轨 | 早期科研对象是果蝇（Drosophila，图片说明明载），1937 与 Beadle 合作后转 Neurospora——转轨叙事勿倒置 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| genes act by regulating definite chemical events | 基因通过调控特定化学反应起作用 | 获奖理由逐字对应 |
| one gene, one enzyme | 一基因一酶假说 | 与 Beadle 共同提出，有"限定与修正"口径 |
| Neurospora crassa | 粗糙脉孢菌（红色面包霉） | X 射线诱变的实验生物，斜体 |
| auxotroph | 营养缺陷型 | 最小培养基需补加单一营养素 |
| minimal medium | 最小培养基 | 筛选体系核心 |
| bacterial conjugation | 细菌接合 | 与 Lederberg 合作发现 |
| Escherichia coli | 大肠杆菌 | 接合实验材料，斜体 |
| tryptophan biosynthesis | 色氨酸生物合成 | 实验室长期主题 |
| metabolic pathway | 代谢通路 | 突变阻断的分析对象 |
| Rockefeller Institute | 洛克菲勒研究所 | 1957-1975 最后一站 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Tatum 的科学方法正是"把生命拆开来看"——射线打断代谢通路的一步、突变体在最小培养基上"缺什么补什么"，Falling Apart 的解构感对应这种逐级拆解的生命观；而 65 岁因心肺疾患早逝的结局，也赋予全篇一层深沉的挽歌底色。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Edward_Lawrie_Tatum/FallingApart.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
