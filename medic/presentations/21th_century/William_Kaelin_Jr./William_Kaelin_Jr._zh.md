# 医学家立传提示词（William Kaelin Jr.）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2019 年得主（三人共享之一） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：William G. Kaelin Jr.（1957-11-23 生于纽约市，在世）
- **气质关键词**：**VHL 抑癌基因与氧感知的破译者、医生-科学家的典范** —— 2019 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，三人共享同一句）：
  > "for their discoveries of how cells sense and adapt to oxygen availability"
  > （因他们发现了细胞如何感知并适应氧气供应）
- **设计母题**：**氧传感器（oxygen sensor）**。HIF 蛋白在氧充足时被降解、缺氧时点亮 EPO 信号——"细胞里的氧分压计"。
- **本地 Wikipedia 路径**：medic/presentations/pages/21th_century/William_Kaelin_Jr./page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/21th_century/William_Kaelin_Jr./page.md`；目录 `medic/presentations/21th_century/William_Kaelin_Jr./`；Makefile 改 `MAIN=William_Kaelin_Jr._zh`；肖像优先 images.txt 所列 Commons 图（Kaelin in 2019），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/William_Kaelin_Jr..yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | oncology | 肿瘤学 | 职业主领域（infobox Fields） | 封面 |
| 1 | tumor suppressor biology | 抑癌基因生物学 | RB/VHL/p53 三大抑癌基因 | 研究页 |
| 2 | oxygen sensing | 氧感知 | VHL 调控 HIF，诺奖核心 | 核心页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | David M. Livingston | 无向 | Dana-Farber 博士后东家，视网膜母细胞瘤研究入门 |
| co-honored | Peter J. Ratcliffe | 无向 | 2019 诺贝尔生理学或医学奖三人共享（细胞氧感知与适应） |
| co-honored | Gregg L. Semenza | 无向 | 2019 诺贝尔生理学或医学奖三人共享（细胞氧感知与适应） |
| spouse | Carolyn Kaelin | 无向 | 1988 结婚，乳腺癌外科医生，2015 因胶质母细胞瘤去世 |

> 对手方规范名：均无库内记录按 page.md 形式新建 stub（Ratcliffe 用 citation 形式 Peter J. Ratcliffe、Semenza 用 Gregg L. Semenza——库内 J. A. Ratcliffe 系无关物理学家勿混用）；**relations=4 为诚实值**（在世者，page.md 无导师/门生具名记载，勿虚构补边）。

## 五、配色方案

- **气质**：医生-科学家的双轨人生 + 临床关怀与基础机制的交汇 + 罕见病里藏着的普遍真理
- **主色**：深青绿 `#175E54`（氧气与生命线的冷冽色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` VHL/氧感知 — 供氧青 `#1E6B8C`
  - `badgeB` 抑癌基因（RB/p53）— 基因紫 `#5E4B8B`
  - `badgeC` HIF/EPO 通路 — 血氧红 `#A63A2B`
  - `badgeD` Dana-Farber 建制 — 哈佛绯 `#8C1F28`
- **背景母题**：低透明度 O₂ 分子对与渐变氧浓度条带（富氧→缺氧）。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 细胞氧感知的破译者 / William Kaelin Jr. 1957– + 三人共享 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年纽约、Duke 数学+化学 BS / MD 1982、Johns Hopkins 住院医、Dana-Farber/Harvard、诺奖 2019）
03  核心贡献概览 — VHL 与 EPO / HIF 调控 / 氧感知通路 / 缺氧药物
04  纽约与 Duke (1957–1982) — 数学和化学本科、自认"研究非所长"、留校 MD 1982
05  临床训练与转折 — Johns Hopkins 内科住院医、Dana-Farber 肿瘤学 fellow；在 Livingston 实验室做视网膜母细胞瘤研究尝到科研成功
06  1992/1993：自己的实验室 — 沿 Livingston 实验室走廊建组，转向 von Hippel–Lindau 病（VHL）等遗传性癌症
07  VHL 之谜（核心页一）— VHL 肿瘤血管丰富、分泌 EPO（缺氧应答激素）；假说：VHL 肿瘤形成与机体缺氧探测缺陷相关；发现 VHL 突变压制 EPO 过程关键蛋白
08  与 Ratcliffe/Semenza 的汇流 — Semenza/Ratcliffe 分别鉴定 HIF 两部分蛋白（EPO 产生所必需、受血氧触发）；Kaelin：VHL 蛋白调控 HIF——三条线汇成氧感知通路
09  2019 诺贝尔奖 — 与 Ratcliffe、Semenza 共享；官方理由全句；2016 Lasker 三人预演；通路催生贫血与肾衰新药
10  荣誉与学术服务 — Gairdner 2010、NAS 2010、Korsmeyer 奖 2012、Lefoulon-Delalande 大奖 2012、Wiley 2014、Lasker 2016、Massry 2018；Damon Runyon 董事会副主席、礼来董事、SU2C 顾问
11  建制与职位 — Dana-Farber/Harvard 教授 2002、DFCI/Harvard 癌症中心基础科学副主任 2008、HHMI
12  家庭 — 妻 Carolyn Kaelin（乳腺癌外科医生）1988 结婚，2015 因胶质母细胞瘤去世，育两子——克制呈现
13  与诺奖同行的互补分工 — Kaelin=VHL-HIF 调控 / Semenza=HIF 发现 / Ratcliffe=氧依赖降解的普遍性——三人三段拼图
14  遗产：缺氧疗法时代 — 贫血、肾衰、癌症缺氧干预的药理学基础
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 2019 三人共享同一句理由；分工：Semenza=HIF 发现、Kaelin=VHL 对 HIF 的调控、Ratcliffe=氧依赖降解——勿写成 Kaelin 独得或"VHL 基因的发现者"（VHL 病早已命名） |
| VHL 表述 | Kaelin 是揭示 **VHL 蛋白调控 HIF** 的机制，不是发现 VHL 病/基因本身——"hypothesized a connection"系页面原意 |
| HIF 归属 | HIF 由 Semenza/Ratcliffe 分别鉴定（页面口径 "who separately had identified"）；Kaelin 页面仅表述"aligned with"——归属勿混 |
| Livingston 关系 | DFCI fellow 期间在其实验室做 RB 研究（博士后性质）——influence，勿写博士导师（无具名导师，Duke MD 无博士论文） |
| 少年自评 | "deciding as an undergraduate that research was not a strength"——转折叙事保留，勿美化成"自幼立志科研" |
| 在世者与家庭 | 妻 Carolyn 2015 病逝（胶质母细胞瘤）系 page.md 明载——克制一句，勿煽情；两子不入库 |
| 在世留白 | 在世者：无卒日；relations=4 诚实值（page.md 无门生记载） |
| 引语红线 | page.md 无整句直接引语——全部转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| von Hippel–Lindau (VHL) | 希佩尔-林道病/基因 | 抑癌基因，Kaelin 机制对象 |
| HIF | 缺氧诱导因子 | Semenza/Ratcliffe 鉴定 |
| erythropoietin (EPO) | 促红细胞生成素 | 缺氧应答激素 |
| hypoxia | 缺氧 | 低氧状态 |
| tumor suppressor | 抑癌基因 | RB/VHL/p53 |
| retinoblastoma | 视网膜母细胞瘤 | Livingston 实验室入门课题 |
| angiogenesis | 血管新生 | VHL 肿瘤特征 |
| anaemia | 贫血 | 通路药物应用方向 |

## 九、背景音乐选择

- **选定曲目**：**Last Hope** — Alex-Productions（manifest 预分配）
- **匹配理由**："最后的希望"贴合罕见病研究者从 VHL 病例中挖掘出普适生命机制的弧线——从罕见病到贫血/肾衰/癌症的广谱希望；沉稳中带张力的曲式匹配医生-科学家的双重身份。
- **本地路径**：music_audio/ 下 Alex-Productions Last Hope 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
