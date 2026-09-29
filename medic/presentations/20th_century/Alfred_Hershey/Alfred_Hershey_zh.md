# 医学家立传提示词（Alfred Hershey）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1969 年得主（阿尔弗雷德·赫尔希，证明 DNA 是遗传物质的搅拌实验设计者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Alfred Day Hershey（1908-12-04 生于密歇根州奥沃索 ~ 1997-05-22 卒于纽约州 Syosset，享年 88 岁）
- **气质关键词**：**以一台厨房搅拌机裁决 DNA 与蛋白质之争的实验大师、Phage Group 的"圣人"、冷泉港的隐者** —— 1969 获奖理由（与 Max Delbrück、Salvador Luria 三人共享）：
  > "for their discoveries concerning the replication mechanism and the genetic structure of viruses"（因发现病毒的复制机制与遗传结构）
- **设计母题**：**一台搅拌机分开两种真相**。1952 年 Hershey-Chase 实验用搅拌机把噬菌体的蛋白质外壳与 DNA 分开——放射性标记落在 DNA 上，遗传物质之谜裁决。视觉隐喻：一台 Waring 搅拌机与两道分离的荧光轨迹。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Alfred_Hershey/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Alfred_Hershey/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Alfred_Hershey/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Alfred_Hershey_zh`、`VIDEO_NAME=Alfred_Hershey_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Alfred_Hershey/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Alfred_Hershey.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | bacteriology | 细菌学 | PhD 专业与噬菌体研究起点 | 早年页 |
| 1 | genetics | 遗传学 | 噬菌体遗传重组，1969 诺奖核心 | 核心页 |
| 2 | bacteriophage | 噬菌体 | Hershey-Chase 搅拌实验 | 核心页 |
| 3 | molecular biology | 分子生物学 | DNA 为遗传物质的证明 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Jacques Bronfenbrenner | 无向 | 华盛顿大学系主任，共事研究噬菌体（1934-50） |
| co-honored | Max Delbrück | 无向 | 1969 诺贝尔生理学或医学奖三人共享（病毒复制机制与遗传结构） |
| co-honored | Salvador Luria | 无向 | 1969 诺贝尔生理学或医学奖三人共享（病毒复制机制与遗传结构） |
| colleague | Max Delbrück | 无向 | Phage Group 三圣之一（被引为圣人）；1943 Vanderbilt 相识，1946 各自独立发现噬菌体遗传重组 |
| colleague | Salvador Luria | 无向 | Phage Group 共同成员（1945 冷泉港噬菌体课程） |
| collaborator | Martha Chase | 无向 | 1952 Hershey-Chase（Waring Blender）实验，证明 DNA 而非蛋白质是遗传物质 |
| spouse | Harriet Davidson | 无向 | 妻（1918-2000），独子 Peter Manning Hershey（1956-1999） |

> relations=7 为诚实值，Review 勿误判虚增。
> 不入库：Robert Day 与 Alma Wilbur Hershey（父母，背景叙事）；Frank Stahl（"Phage Church"引语作者——引语可引用，人物不入库）；Watson/Crick（语境人物）；世界文化理事会（机构）。
> 库内当时无 Jacques Bronfenbrenner / Martha Chase / Harriet Davidson 记录，均由本 yaml 新建 stub；Delbrück/Luria 由其本人 yaml 或并行批次规范化（Luria 已有库内 stub #6054，按名幂等）。

## 五、配色方案 【人物专属】

- **气质**：密歇根的朴素灰蓝 + 冷泉港林间的深绿 + 搅拌实验的干脆利落
- **主色**：冷泉港绿 `#2F6B4F`（林间实验室与 DNA 生命的底色）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 搅拌实验 — 冷泉港绿 `#2F6B4F`
  - `badgeB` 噬菌体遗传重组 — 钢蓝 `#2E4A66`
  - `badgeC` Phage Group — 灰紫 `#5C5470`
  - `badgeD` λ 噬菌体与晚年 — 琥珀 `#A0722D`
- **背景母题**：一道离心分离的分界线（蛋白/核酸两侧），badge 圆点分列两域。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 用搅拌机裁决 DNA 之争 / Alfred Hershey 1908–1997 + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Owosso、教育 Michigan State
    BS 1930/PhD 1934、任职 Washington Univ. St. Louis（1934-50）/卡内基遗传系
    （1950 起，冷泉港前身）、荣誉 Nobel 1969/Lasker 1958/Kimber Genetics Award、核心领域）
03  核心贡献概览 — 噬菌体遗传重组 / Hershey-Chase 实验 / Phage Group / λ 噬菌体
04  密歇根与圣路易斯 (1908–1950) — Owosso 出生、Michigan State 化学 BS 1930/
    细菌学 PhD 1934、华盛顿大学细菌学与免疫学讲师（1934-50）
05  与 Bronfenbrenner 共研噬菌体 — 系主任 Bronfenbrenner 合作研究噬菌体、
    病毒感染靶标能力的影响因素——进入 Delbrück/Luria 的视野
06  1943：Phage Group 成形 — Delbrück 邀其赴 Vanderbilt 讨论噬菌体研究、
    与 Luria 三人构成非正式网络的"三位一体"
07  1946：噬菌体遗传重组 — Hershey 与 Delbrück 各自独立发现：
    不同噬菌株感染同一细菌时可交换遗传物质、产生杂交噬菌体、
    Hershey 命名为 genetic recombination
08  1950：冷泉港岁月 — 转任卡内基基金会遗传学部（CSHL 前身）、
    1962 任遗传学部主任（至 1970 退休）、终生居于 CSHL 园区
09  1952：Hershey-Chase 搅拌实验 — 与 Martha Chase 用 Waring 搅拌机分离
    噬菌体蛋白质外壳与 DNA、放射性标记证明 DNA（而非蛋白质）是遗传物质
10  1969 诺贝尔奖 — 三人共享官方理由逐字引用、Lasker 1958 与 Kimber Genetics Award 为前奏、
    Stahl "Phage Church" 引语：Delbrück 是教皇、Luria 是神父、Al 是圣人（可引原文）
11  晚年项目 — 1971 主编《The Bacteriophage λ》巨著（CSHL Press）、
    1981 世界文化理事会创始成员、退休后仍持续新课题
12  个人生活与身后 — 妻 Harriet Davidson（1918-2000）、独子 Peter Manning Hershey
    （1956-1999）、充血性心力衰竭卒于 Laurel Hollow 家中（1997-05-22，88 岁）
13  学术风格画像 — 委员会口径"三人中 Hershey 是最出色的实验家"、
    实验极简主义者的冷泉港隐者形象（以 page.md 事实为限）
14  遗产 — DNA 唯一遗传物质地位的最终裁决者之一、
    分子生物学的实验标准由 Phage Group 立规、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries concerning the replication mechanism and the genetic structure of viruses"（三人共享、their） |
| 三人分工 | 委员会口径：Delbrück 理论分析、Luria 理论+社会敏感、**Hershey 是最出色的实验家**（Delbrück 页载委员会评语，可交叉引用）；本篇以实验大师定位 |
| 搅拌实验表述 | 1952 年与 **Martha Chase** 共同完成、即 Hershey-Chase 或 "Waring Blender" 实验——结论是"DNA（而非蛋白质）是遗传物质"；Chase 以 collaborator 入库，勿掠其名 |
| 1946 重组发现 | Hershey 与 Delbrück **各自独立**发现不同噬菌株可交换遗传物质——independently 口径保留；命名 genetic recombination 系 Hershey |
| Phage Church 引语 | Stahl："三位一体——Delbrück 是教皇、Luria 是勤恳的神父、Al 是圣人"（page.md 英文原文在，可引原文+译文）——趣味叙事的题眼，注明 Stahl 系 Phage Group 成员 |
| 学位口径 | Michigan State 化学 BS 1930 + **细菌学** PhD 1934——description 称 "chemist" 但 Ph.D. 是细菌学，两说并存如实呈现 |
| Carnegies/CSHL | 卡内基基金会遗传学部是 CSHL 的前身机构——沿革表述照 page.md，勿写成"直接加入 CSHL" |
| 独子 | Peter Manning Hershey（1956-1999）——page.md 明载其早逝，客观一句 |
| 死因 | 充血性心力衰竭（congestive heart failure）、卒于 Laurel Hollow 家中——勿写"卒于 Syosset"（infobox 地）与死地 Laurel Hollow 的差异，照 page.md 正文 |
| 在世者规则 | 本篇主角 1997 年逝；relations=7 系 page.md 所限诚实值 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Hershey-Chase experiment | Hershey-Chase 实验 | 又名 Waring Blender 实验 |
| genetic recombination | 遗传重组 | 其命名（1946） |
| bacteriophage | 噬菌体 | 研究对象 |
| Phage Group | 噬菌体小组 | 非正式研究网络 |
| The Bacteriophage λ | 《噬菌体 λ》 | 1971 主编巨著 |
| Carnegie Institution | 卡内基基金会 | CSHL 前身机构 |
| World Cultural Council | 世界文化理事会 | 1981 创始成员 |
| Phage Church | 噬菌体教会 | Stahl 戏称（引语） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Empire Collapse**（manifest 预分配）
- **风格**：厚重 / 张力 / 史诗推演
- **匹配理由**：1952 年那台搅拌机终结了一个延续世纪的"蛋白质帝国"假设——Empire Collapse 的厚重推演匹配"用最简单的机械裁决最大科学争论"的叙事，也呼应 Phage Group 以纪律与实验立规、旧范式崩塌的历史时刻。
- **本地路径**：`music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav` → 复制为 `presentations/20th_century/Alfred_Hershey/Empire_Collapse.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；搅拌实验归属与 Phage Church 引语务必忠实 page.md。**
