# 医学家立传提示词（Peter J. Ratcliffe）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2019 年得主（彼得·拉特克利夫，细胞氧感知机制的阐明者之一）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Peter John Ratcliffe（1954-05-14 生于英格兰兰开夏郡莫克姆，在世）
- **气质关键词**：**从肾脏 EPO 走向普适氧感知的医师科学家、VHL-HIF 分子链的揭示者、临床医学与基础机制的双栖者** —— 2019 获奖理由（与 William Kaelin Jr.、Gregg L. Semenza 三人共享）：
  > "for their discoveries of how cells sense and adapt to oxygen availability"（因发现细胞如何感知并适应氧气供应）
- **设计母题**：**氧的开关**。氧充足时 VHL 结合羟基化的 HIF 并将其降解；缺氧时 PHD 酶停摆、HIF 存活并点亮 EPO 基因——视觉隐喻：一枚随氧压明灭的分子开关，辅以牛津尖塔与肾单位意象。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Peter_J._Ratcliffe/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Peter_J._Ratcliffe/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Peter_J._Ratcliffe/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Peter_J._Ratcliffe_zh`、`VIDEO_NAME=Peter_J._Ratcliffe_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Peter_J._Ratcliffe/images.txt`（2019 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 2019 诺奖 HIF 机制示意图（HIF_Nobel_Prize_Physiology_Medicine_2019_Hegasy_ENG.png）。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Peter_J._Ratcliffe.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | oxygen sensing | 氧感知 | VHL-HIF 机制，2019 诺奖核心 | 核心页 |
| 1 | hypoxia | 缺氧应答 | 细胞低氧反应的普适性 | 核心页 |
| 2 | nephrology | 肾脏病学 | EPO 研究起点、肾内科受训 | 早年页 |
| 3 | cancer biology | 肿瘤生物学 | 缺氧通路在肿瘤中的开启与血管新生 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | William Kaelin Jr. | 无向 | 2019 诺贝尔生理学或医学奖三人共享（细胞感知与适应氧气供应的发现） |
| co-honored | Gregg L. Semenza | 无向 | 2019 诺贝尔生理学或医学奖三人共享（细胞感知与适应氧气供应的发现） |
| colleague | William Kaelin Jr. | 无向 | 联合研究阐明 VHL 结合羟基化 HIF 的氧感知分子链 |
| colleague | Gregg L. Semenza | 无向 | 联合研究揭示 HIF 转录因子激活 EPO 基因的机制 |
| spouse | Fiona Mary MacDougall | 无向 | 1983 结婚 |

> 在世者，page.md 无师承/学生记载（临床学位路径，无博士导师字段），relations=5 为诚实值，Review 勿误判缺漏。
> 不入库：父母（父为律师、母为接线员，非学界）；实验室成员未具名。
> 库内当时无 William Kaelin Jr. / Gregg L. Semenza / Fiona Mary MacDougall 记录，均由本 yaml 新建 stub——**Kaelin 用 citation json 形式 `William Kaelin Jr.`（其本人批次 agent 将 UPD 回填）**；Semenza 用 manifest 全名。

## 五、配色方案 【人物专属】

- **气质**：牛津石墙的冷灰绿 + 缺氧细胞的深碧 + 分子开关的锋利
- **主色**：深碧绿 `#146356`（氧合血红蛋白的深色端，亦含"机制如矿脉般被发现"的意象）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 氧感知/VHL-HIF — 深碧绿 `#146356`
  - `badgeB` EPO 与肾脏 — 暗红 `#8C2F1B`
  - `badgeC` 肿瘤与血管新生 — 灰紫 `#5C5470`
  - `badgeD` 临床转化药物 — 钢蓝 `#2E4A66`
- **背景母题**：横向明暗渐变条带（氧浓度梯度），badge 圆点如氧分压刻度散布。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 细胞氧感知的阐明者 / Peter J. Ratcliffe 1954– + 四色 badge + 右上头像 + 国籍行 United Kingdom
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Morecambe、教育 Cambridge/St Bartholomew's
    MB BChir 1978/Cambridge MD 1987、任职 Oxford Nuffield 教授/Francis Crick/Ludwig、
    荣誉 Nobel 2019/Lasker 2016/爵士 2014、核心领域）
03  核心贡献概览 — EPO 的氧控之谜 / 氧感知的普遍性 / VHL-HIF 分子链 / 从机制到药物
04  兰开夏少年与剑桥医学 (1954–1978) — Morecambe 出生、Lancaster Royal Grammar School、
    1972 Gonville and Caius 学院公开奖学金、St Bartholomew's MB BChir 优等（1978）
05  肾内科与 EPO 之谜 (1978–1989) — 牛津肾内科受训聚焦肾氧合、1987 高级 MD、
    1989 牛津 Nuffield 系建实验室研究 EPO 调控——肾脏如何在低氧时下达造血指令
06  1990 Wellcome Senior Fellowship — 转向细胞缺氧应答、1992-2004 Jesus College 资深研究员
07  氧感知是普遍的 — EPO 通路 mRNA 亦见于脾/脑/睾丸、这些器官的细胞缺氧时也能开启 EPO、
    用该 mRNA 赋予其他细胞氧感知能力——机制超越肾脏
08  VHL-HIF 分子链（上）— 与 Kaelin/Semenza 联合研究、VHL 肿瘤抑制蛋白结合羟基化 HIF、
    泛素化导向降解——氧充足时的"销毁程序"
09  VHL-HIF 分子链（下）— 缺氧时需氧的 HIF 羟基化酶 PHD1/2/3 停摆、VHL 失去结合对象、
    HIF 存活并反式激活 EPO 基因——分钟级快速响应
10  2016 Lasker → 2019 Nobel — Lasker 三人共享为前奏、2019 三人共享诺奖、
    2019-12-07 Nobel Lecture "Elucidation of Oxygen Sensing Systems in Human and Animal Cells"
11  同一路径的暗面：肿瘤 — 缺氧通路在多种肿瘤中开启、促血管新生供养瘤体、
    当前缺氧理解多出自 Ratcliffe 实验室（page.md 口径）
12  临床转化 — 阻断 VHL-HIF 结合的药物用于贫血与肾衰竭——机制研究的医学回报
13  荣誉与认可 — Gairdner 2010、Lasker 2016、Buchanan Medal 2017、Massry 2018、
    Louis-Jeantet 2009、爵士（2014 新年荣誉）、FRS/FMedSci/EMBO、Leopoldina 2020、
    Sir Hans Krebs Medal（2026，FEBS 第 50 届大会）
14  遗产与现在 — 2016 起 Francis Crick 临床研究主任、Ludwig Member（2012）/Distinguished
    Scholar（2022）、Target Discovery Institute 主任、氧生物学成为教科书篇章、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries of how cells sense and adapt to oxygen availability"（三人共享、their）；勿截短为"发现 HIF" |
| 三人分工 | Semenza 发现 HIF-1；Kaelin 阐明 VHL 与缺氧调节的关联；Ratcliffe 证明氧感知的普遍性并打通 VHL-HIF 羟基化降解链——各篇按本人角色书写，勿越位归功 |
| 机制方向 | 氧充足 → VHL 结合羟基化 HIF → 泛素化降解；缺氧 → PHD1/2/3 停摆 → HIF 存活激活 EPO——因果方向勿写反 |
| 机制速度 | page.md 明言该过程"分钟级完成"——快速响应是卖点，勿省略 |
| 无师承 | page.md 无博士导师记载（MB BChir 与高级 MD 均临床学位）——**勿杜撰导师**；metadata 亦无导师字段，诚实值 |
| 妻子 | Fiona Mary MacDougall，1983 结婚——仅一句，勿展开 |
| 2026 奖项 | Sir Hans Krebs Medal（2026，FEBS 第 50 届大会）——当前年份 2026，照 page.md 写；勿当成未来错误删除 |
| 荣誉序列 | Lasker 2016（三人）先于 Nobel 2019；Gairdner 2010；Buchanan Medal 2017（皇家学会）；Massry 2018——年份勿错位 |
| 学位口径 | MB BChir（剑桥/St Bartholomew's，1978 优等）+ 高级 MD（剑桥 1987）——英国临床学位体系，勿写成 PhD |
| 机构时段 | Nuffield 教授兼系主任 2004-2016；Crick 临床研究主任 2016 起；Ludwig Member 2012/Distinguished Scholar 2022——三组年份勿混 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| hypoxia | 缺氧 | 核心场景词 |
| erythropoietin (EPO) | 促红细胞生成素 | 肾脏分泌的造血激素 |
| HIF (hypoxia-inducible factors) | 缺氧诱导因子 | 反式激活 EPO 基因的转录因子 |
| VHL (von Hippel–Lindau) | VHL 肿瘤抑制蛋白 | 结合羟基化 HIF 并导向降解 |
| hydroxylase (PHD1/2/3) | 羟基化酶 | 需氧酶，缺氧时停摆 |
| ubiquitylation | 泛素化 | HIF 降解的标记步骤 |
| trans-activate | 反式激活 | HIF 对 EPO 基因的作用方式 |
| MB BChir | 内外科学士（剑桥） | 英国临床学位，勿当 PhD |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配）
- **风格**：开拓 / 前行 / 沉稳史诗
- **匹配理由**：从肾脏病房的 EPO 之谜出发，一路打通"氧感知是细胞普适能力"的机制长廊——Pathfinder 的行进感匹配"临床医生出身、以二十年实验室求索开辟氧生物学新大陆"的叙事。
- **本地路径**：`music_audio/inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav` → 复制为 `presentations/21th_century/Peter_J._Ratcliffe/Pathfinder.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；VHL-HIF 因果方向与三人分工务必精确。**
