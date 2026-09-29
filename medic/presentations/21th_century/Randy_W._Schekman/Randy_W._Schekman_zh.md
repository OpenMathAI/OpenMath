# 医学家立传提示词（Randy Schekman）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2013 年得主（与 James Rothman、Thomas C. Südhof 三人共享）。
> 本文件是 Randy Schekman 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面，
> 执行方按本提示词产出 15 页 Beamer 立传（本阶段不写 tex，仅沉淀事实与规范）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Randy Wayne Schekman（1948-12-30 生于明尼苏达州圣保罗，在世）
- **气质关键词**：**囊泡运输的遗传学破译者、酵母筛选大师、开放获取出版的旗手**
- **诺奖获奖理由（2013，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discoveries of machinery regulating vesicle traffic, a major transport system in our cells"
  > （因其发现调节囊泡运输的机制——细胞内的一个主要转运系统）——注意 "their"：与 James Rothman、Thomas C. Südhof 三人共享
- **设计母题**：**囊泡与分拣（vesicle and sorting）**。酵母突变体里堆积的分泌中间体、被 COPII 包被的运输囊泡——
  视觉母题用一枚枚出芽的小圆泡沿弯曲路径行进，象征"细胞物流系统的调度员"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Randy_W._Schekman/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/21th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/21th_century/Randy_W._Schekman/`，数据库写 greatminds 库（MySQL）。

- **第 0 步**：核对本地 page.md 事实基准（本提示词第三、四、七节已沉淀，执行时再逐句复核）
- **第 1 步**：建目录 `medic/presentations/21th_century/Randy_W._Schekman/`（含 `images/`）
- **第 2 步**：复制 Makefile，设 `MAIN=Randy_W_Schekman_zh`、`VIDEO_NAME=Randy_W_Schekman_zh`（宏名禁点号）
- **第 3 步**：收集肖像（page.md 无 infobox 肖像 URL 时用 Commons Special:FilePath 回退，404 则装饰圆占位）
- **第 4~9 步**：tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cell biology | 细胞生物学 | 膜组装与囊泡运输的分子机制，诺奖核心 | 核心页 |
| 1 | molecular biology | 分子生物学 | sec 突变体基因克隆与生化反应重建 | 核心页 |
| 2 | biochemistry | 生物化学 | 无细胞反应重现分泌途径事件 | 核心页 |
| 3 | genetics | 遗传学 | 酵母遗传筛选法（ brilliantly conceived genetic screen） | 方法页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Arthur Kornberg | 师→生（博士导师） | 斯坦福博士导师（1959 诺奖得主），1975 DNA 复制论文 |
| advisor-student | David Julius | Schekman→学生 | infobox Doctoral students 明载（2021 诺奖得主） |
| advisor-student | David Baker | Schekman→学生 | infobox Doctoral students 明载（2024 化学诺奖得主） |
| co-honored | James Rothman | 无向 | 2013 诺贝尔生理学或医学奖三人共享（发现调节囊泡运输的机制） |
| co-honored | Thomas C. Südhof | 无向 | 2013 诺贝尔生理学或医学奖三人共享（发现调节囊泡运输的机制） |
| spouse | Nancy Walls | 无向 | 妻子，2017 年秋因帕金森病去世（患病 20 年） |

> 说明：infobox 之外的家人（父 Alfred、母 Esther、妹妹 Wendy）不入库；
> 但 Esther and Wendy Schekman 讲席命名背景（母妹皆死于癌症、捐出 40 万美元奖金设席）是第 12 页素材。
> Lasker/Horwitz 2002 的共同得主 James Rothman 属非诺奖共享，不另建边（co-honored 已覆盖诺奖同届）。
> 对手方规范名：Arthur Kornberg 用库内 id=3780；David Baker 用库内 id=4129（Q3814528）；
> James Rothman 库内暂无，本侧建 stub（其本人 yaml 归属另一批次，届时 UPD 回填）。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 6。

## 五、配色方案

- **气质**：系统、调度、直谏出版体制的锋芒
- **主色**：伯克利蓝 `#1E4E79`（加州校色与细胞物流的理性）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：
  - `badgeVesicle` 囊泡运输 — 冷青 `#0E7C7B`
  - `badgeYeast` 酵母筛选 — 暖橙 `#E07B30`
  - `badgeOpen` 开放获取 — 猩红 `#C4204F`
  - `badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：出芽的小圆泡（囊泡）沿弧线散布，大小错落

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover 共享首页）
01  封面 — 细胞物流的调度员 / Randy Schekman 1948– + 四色 badge + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒/圣保罗出身/教育 UCLA BA 1971 + Edinburgh 交换 + Stanford PhD 1975/任职/核心领域
03  核心贡献概览 — sec 突变体 / COPII 与 Sec61 / 囊泡运输 / 开放获取
04  移民之家与加州少年 (1948–1966) — 俄裔与比萨拉比亚犹太移民家庭；1950s 迁加州 Rossmoor；Western High School 1966
05  UCLA 与爱丁堡 (1966–1971) — 分子生物学 BA 1971；第三年爱丁堡交换
06  斯坦福：Kornberg 门下 (1971–1975) — DNA 复制研究，博士论文 multienzyme DNA replication reaction
07  伯克利建组 (1977– ) — 1981 副教授、1984 正教授；1991 起 HHMI investigator
08  酵母遗传筛选（核心贡献页）— sec 突变体积累分泌中间体 → 克隆基因 → 无细胞生化反应重现分泌途径（ForMemRS 褒奖语）
09  COPII、Sec61 与纯化运输囊泡 — 分泌领域从形态描述走向分子机制
10  2013 诺贝尔奖 — 理由逐字；三人分工一句（Schekman 遗传学/Rothman 生化/Südhof 突触）
11  荣誉与认可 — NAS 1992 · Rosenstiel 1993 · Gairdner 1996 · Eli Lilly 1987 · Lasker+Horwitz 2002（与 Rothman）· Massry+E.B. Wilson Medal 2010 · ForMemRS 2013 · Golden Plate 2017 · 摩尔多瓦科学院荣誉院士 2021
12  捐奖金与纪念讲席 — 40 万美元奖金捐赠设立 Esther and Wendy Schekman 基础癌症生物学讲席（母亲与妹妹均死于癌症）
13  开放获取的旗手 — 2013-12 宣布实验室不再投 Nature/Cell/Science；PNAS 前主编、eLife 创刊主编（2011 宣布、2012 上线）；Shaw Prize 评选委员会主席
14  抗击帕金森 — 妻 Nancy Walls 2017 年秋去世（患病 20 年）；出任 ASAP 科学主任（与 Michael J. Fox 基金会合作，2022 年 35 团队 165 实验室）
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for their discoveries of machinery regulating vesicle traffic, a major transport system in our cells"；"machinery" 表机制复合体 |
| 2 | 三人分工 | Schekman=酵母遗传筛选、Rothman=囊泡转运生化、Südhof=突触释放——page.md 未逐句分工，表述克制："their ground-breaking work on cell membrane vesicle trafficking" |
| 3 | 博士论文主题 | 是 **DNA 复制**（multienzyme DNA replication reaction, 1975）非囊泡运输——转方向发生在伯克利建组后，勿倒置 |
| 4 | 两位诺奖学生 | David Julius（2021 医学奖，辣椒素受体）与 David Baker（2024 化学奖，蛋白质设计）均出自 infobox Doctoral students——教科书级"桃李满门"素材，勿与"门生不详"混淆 |
| 5 | 捐款去向 | 40 万美元（其份额）捐给 UC Berkeley 设 **Esther and Wendy Schekman** 基础癌症生物学讲席——纪念母亲与妹妹，勿写成"捐给癌症研究基金会"泛称 |
| 6 | 开放获取 | 2013 年 12 月宣布不再投 Nature/Cell/Science，批评其人为限流与追逐引用；eLife 由 HHMI/Max Planck/Wellcome 三方创办——表述对事不对人 |
| 7 | PNAS/eLife | Known for 是 **former** editor-in-chief（PNAS）与 eLife 主编——均已卸任，勿写现任 |
| 8 | Lasker/Horwitz 2002 | 两奖均与 James Rothman 共享（发现细胞膜运输）——这是非诺奖共享，勿写进 2013 三人组叙述 |
| 9 | Kavli 混淆 | Schekman **未获** Kavli 奖（那是 Südhof 2010 与 O'Keefe 2014）；勿张冠李戴 |
| 10 | ASAP | 妻子 2017 年秋去世（20 年帕金森病程）；Schekman 出任 ASAP（Aligning Science Across Parkinson's）科学主任——ASAP 全称 page.md 未展开，勿杜撰缩写释义 |
| 11 | 犹太裔 | 俄裔与比萨拉比亚（Bessarabia）移民家庭——背景一句，勿展开 |
| 12 | 在世者 | Schekman 在世（1948- ）；relations=6 中含 2 位诺奖学生，诚实值 |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| vesicle traffic | 囊泡运输 | 诺奖理由核心词，勿译"囊泡交通" |
| sec mutants | sec 突变体 | 分泌途径缺陷突变株 |
| COPII | COPII 包被复合体 | 内质网→高尔基体运输包被 |
| Sec61 | Sec61 转位复合体 | 蛋白质跨膜转位通道 |
| secretory pathway | 分泌途径 | 酵母筛选的作用对象 |
| eLife | eLife 期刊 | 开放获取，2012 创刊 |
| open access | 开放获取 | 出版改革主张 |
| ASAP | 帕金森科学计划 | 科学主任身份，全称按 page.md 谨慎处理 |

## 九、背景音乐选择

- **选定曲目**：**SEA** — Alex-Productions（manifest 预分配）
- **匹配理由**：SEA 的开阔与秩序感对应"细胞物流系统"的全局图景——从酵母突变体筛起、
  把一个描述性领域改造成分子机制领域，是系统性长跑者的画像；也贴合其捐奖金、办 eLife、抗帕金森的公共担当。
- **备选（未采用）**：Timeless（纲领感强但已有系列占用）、Ascension（上升感可用但本篇更重"秩序"而非"攀升"）
- **本地路径**：`music_audio/` 下 alex-productions 曲库按 curated_tracks.md 对应条目复制为
  `medic/presentations/21th_century/Randy_W._Schekman/SEA.wav`
