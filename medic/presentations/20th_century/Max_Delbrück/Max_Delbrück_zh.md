# 医学家立传提示词（Max Delbrück）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1969 年得主（马克斯·德尔布吕克，分子生物学纲领的发起人、噬菌体学派的"教皇"）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Max Ludwig Henning Delbrück（1906-09-04 生于柏林 ~ 1981-03-09 卒于加州帕萨迪纳，享年 74 岁）
- **气质关键词**：**从天体物理学到噬菌体的跨界者、分子生物学研究纲领的发起人、把噬菌体研究从经验主义变成精确科学的"教皇"** —— 1969 获奖理由（与 Salvador Luria、Alfred Hershey 三人共享）：
  > "for their discoveries concerning the replication mechanism and the genetic structure of viruses"（因发现病毒的复制机制与遗传结构）
- **设计母题**：**从星空到噬菌体**。哥廷根的星空物理学家转身投向最微小的生命复制体——"用物理学解释基因"。视觉隐喻：一条从星座图缩放进培养皿噬菌斑的光路。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Max_Delbrück/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Max_Delbrück/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准——卒日双值裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Max_Delbrück/`（含 `images/`；目录名含 ü，Makefile/shell 注意 UTF-8）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Max_Delbrück_zh`、`VIDEO_NAME=Max_Delbrück_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Max_Delbrück/images.txt`（1940s 初照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 Vanderbilt Buttrick Hall 纪念铭牌图。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Max_Delbrück.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biophysics | 生物物理学 | 分子生物学纲领发起人，1969 诺奖核心 | 核心页 |
| 1 | molecular genetics | 分子遗传学 | 1935 三人论文与噬菌体遗传学 | 研究页 |
| 2 | bacteriophage | 噬菌体 | 一步生长曲线与 Phage Group | 核心页 |
| 3 | theoretical physics | 理论物理 | 哥廷根出身；Delbrück 散射的预言者 | 早年页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Max Born | 导师 | 哥廷根大学博士导师（1930，理论物理） |
| advisor-student | Lise Meitner | 导师 | 1932-34 柏林威廉皇帝化学研究所其助手（infobox 载为博士导师） |
| co-honored | Salvador Luria | 无向 | 1969 诺贝尔生理学或医学奖三人共享（病毒复制机制与遗传结构） |
| co-honored | Alfred Hershey | 无向 | 1969 诺贝尔生理学或医学奖三人共享（病毒复制机制与遗传结构） |
| colleague | Salvador Luria | 无向 | Phage Group 共同领袖；1943 相识，Luria-Delbrück 波动实验（1942） |
| colleague | Alfred Hershey | 无向 | Phage Group 三圣之一；1946 各自独立发现噬菌体遗传重组 |
| collaborator | Emory L. Ellis | 无向 | 1939 合著 The growth of bacteriophage（一步生长） |
| collaborator | Nikolay Timofeev-Ressovsky | 无向 | 1935 三人合著论基因突变与基因结构之本质（分子遗传学基石） |
| collaborator | Karl Zimmer | 无向 | 1935 三人合著论基因突变与基因结构之本质 |
| influence | Niels Bohr | 无向 | 旅行相遇，其生物学兴趣引导 Delbrück 转向基因的物理学解释 |
| influence | Wolfgang Pauli | 无向 | 旅行相遇的物理学家之一 |
| parent-child | Hans Delbrück | 父 | 父，柏林大学历史学教授；母为李比希外孙女 |
| spouse | Mary Bruce | 无向 | 1941 结婚，育四子女 |
| advisor-student | Lily Jan | 学生 | infobox 明载博士生 |
| advisor-student | Yuh Nung Jan | 学生 | infobox 明载博士生 |
| advisor-student | Ernst Peter Fischer | 学生 | infobox 明载博士生 |
| advisor-student | Charles M. Steinberg | 学生 | infobox 明载博士生 |

> relations=17 为诚实值（4 博士生均 infobox 明载），Review 勿误判虚增。
> 不入库：兄 Justus 与姐 Emmi Bonhoeffer、姐夫 Klaus/Dietrich Bonhoeffer（反纳粹抵抗与 7·20 事件——家族史叙事不入关系边，见陷阱表）；子 Tobias Delbruck（事件相机先驱，彩蛋）；Otto Hahn（Meitner 的合作者，语境人物）；Hans Bethe（Delbrück 散射确认者，语境人物）；Erwin Schrödinger（受其启发著《生命是什么》——思想影响指向是 Schrödinger 受 Delbrück 影响，方向反常规，不入库、叙事呈现）；Watson（获其奖学金资助的感谢信——事件性）；Thomas Hunt Morgan/Mendel/Lamarck/Darwin（进化论史语境）。
> 库内既有 Max Born（#644, Q58978）/Lise Meitner（#1989）/Niels Bohr（#1104, Q7085）/Wolfgang Pauli（#1099, Q65989）/Salvador Luria（#6054，并行批次 stub）规范记录直接引用；本人记录 UPD 复用库内 stub #2283 回填 Q76807；其余新建 stub。

## 五、配色方案 【人物专属】

- **气质**：柏林的书卷灰 + 哥廷根星空的深蓝 + 噬菌斑的透明质感
- **主色**：星空深蓝 `#24506E`（从天体物理到基因物理的纵深）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 噬菌体精确科学 — 星空深蓝 `#24506E`
  - `badgeB` 1935 三人论文 — 灰紫 `#5C5470`
  - `badgeC` Phage Group — 深青 `#0E7C7B`
  - `badgeD` 家族与抵抗史 — 暗红 `#8C2F1B`
- **背景母题**：星空点阵渐变为噬菌斑圆点（尺度跨越），四色错落。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 分子生物学纲领的发起人 / Max Delbrück 1906–1981 + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生柏林、教育哥廷根 PhD 1930、
    导师 Born/Meitner 助手、任职威廉皇帝化学研究所/Vanderbilt/Caltech、
    荣誉 Nobel 1969/Horwitz 1969/ForMemRS 1967、核心领域）
03  核心贡献概览 — 噬菌体的精确科学 / Luria-Delbrück 实验 / 1935 三人论文 / Phage Group
04  书香世家 (1906–1930) — 父 Hans Delbrück 为柏林大学历史学教授、
    母系为化学家李比希外孙女、哥廷根天体物理→理论物理、1930 PhD
05  游学与合作者 (1930–1932) — 英/丹/瑞士之旅、遇 Pauli 与 Bohr——
    Bohr 使他对生物学产生兴趣、Delbrück 散射的理论预言（Bethe 二十年后确认并命名）
06  柏林：Meitner 助手与 1935 三人论文 — 1932 任 Meitner 助手（铀中子辐照合作背景）、
    1935 与 Timofeev-Ressovsky/Zimmer 合著《论基因突变与基因结构之本质》——
    分子遗传学的基石、Schrödinger《生命是什么》的思想起点
07  1937：洛克菲勒基金会与美国 — 离开纳粹德国赴美（先加州后田纳西）、
    Caltech 生物学系研究果蝇遗传学→转向细菌与噬菌体
08  1939：一步生长 — 与 Ellis 合著 The growth of bacteriophage：噬菌体"一步"复制
    而非指数增殖——噬菌体定量研究的起点
09  Vanderbilt 与 Luria-Delbrück 实验 (1940–1947) — 教物理、实验室在生物系、
    1941 遇 Luria、1942 发表细菌抗病毒感染的随机突变研究（波动实验）、
    达尔文选择论适用于细菌的证据——重击拉马克主义
10  1945：Phage Group — 与 Luria/Hershey 在冷泉港开设噬菌体遗传学课程、
    非正式研究网络推动分子生物学早期发展
11  1969 诺贝尔奖 — 三人共享官方理由逐字引用、委员会评语"荣誉首先归于 Delbrück：
    他把噬菌体研究从模糊经验主义转变为精确科学"（可引原文+译文）、
    同年 Horwitz Prize（与 Luria）
12  回到 Caltech 与科隆 (1947–1977) — 1947 回任 Caltech 生物学教授、
    协助科隆大学建分子遗传学研究所、1960s 霉菌行为的未果探索（如实）、
    1977 荣休、反还原论猜想与双螺旋的"反驳"（page.md 口径）
13  家族与抵抗史 — 兄 Justus（律师，1945 死于苏联羁押）、
    姐 Emmi Bonhoeffer 与姐夫 Klaus/Dietrich Bonhoeffer 参与 7·20 刺杀希特勒密谋、
    Dietrich 与 Klaus 1945 被处决——克制、客观呈现（page.md 明载）
    彩蛋：子 Tobias Delbruck 为事件相机先驱
14  遗产 — 物理学家进入生物学的大移民由他点燃、
    Schrödinger《生命是什么》→Watson/Crick/Franklin 的思想谱系、
    Max Delbruck Prize（APS）与柏林 Max Delbrück 中心以其命名、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries concerning the replication mechanism and the genetic structure of viruses"（三人共享、their） |
| 卒日双值 ★ | metadata 双值 1981-03-10 / 03-09；page.md 正文明确 **1981-03-09 晚间**逝于帕萨迪纳 Huntington Memorial Hospital——取 03-09 |
| 双导师口径 | metadata doctoral_advisor = Max Born（哥廷根 PhD 1930）；infobox doctoral advisor = Lise Meitner（1932-34 柏林助手）——两条都入库、note 区分"博士导师/柏林时期导师（infobox 口径）" |
| Delbrück 散射 | 1933 论文结论"理论上成立但不适用于当时情形"、Bethe 约二十年后确认并命名——归属表述照 page.md，勿写成"发现了 Delbrück 散射" |
| 1935 三人论文 | 德文标题《Über die Natur der Genmutation und der Genstruktur》、与 Timofeev-Ressovsky/Zimmer 合著——分子遗传学基石 + Schrödinger 思想起点，三人并列勿独占 |
| Phage Group 定位 | 1945 冷泉港课程、Delbrück/Luria/Hershey 三人核心；委员会评语"荣誉首先归于 Delbrück…"（英文原文在 page.md，可引）；Steward：Hershey 被引为"圣人"的 Stahl 引语放 Hershey 篇 |
| Luria-Delbrück 实验 | 亦称波动实验（Fluctuation Test）：证明突变先于选择存在、随机突变+环境选择——进化论叙事（Lamarck/Darwin/Mendel/Morgan）按 page.md 的历史铺垫写、不越出 |
| 家族抵抗史 ★ | 兄姐与 Bonhoeffer 姐夫们的反纳粹抵抗、7·20 密谋与 1945 处决——page.md 明载，**克制客观陈述，不渲染**；Delbrück 本人 1937 离开纳粹德国——离因表述照 page.md |
| 反还原论 | 其"生命或有类波粒二象性悖论"猜想后被双螺旋发现"反驳"（page.md 口径）——如实写其智识冒险与失败 |
| 霉菌行为 | 1960s 行为科学探索"未果"（unfruitful）——失败也如实写，科学家人格的诚实面 |
| 在世者规则 | 本篇主角 1981 年逝；生卒年月取 1906-09-04/1981-03-09 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Delbrück scattering | Delbrück 散射 | 其理论预言（Bethe 确认命名） |
| bacteriophage | 噬菌体 | 感染细菌的病毒 |
| one-step growth | 一步生长 | 1939 Ellis 合作论文 |
| Luria–Delbrück experiment | Luria-Delbrück 实验 | 波动实验/Fluctuation Test |
| Phage Group | 噬菌体小组 | 1945 冷泉港课程起源 |
| Über die Natur der Genmutation | 论基因突变与基因结构之本质 | 1935 三人论文 |
| aperiodic crystal | 非周期性晶体 | Schrödinger 引申概念 |
| What Is Life? | 《生命是什么》 | 1944，受 Delbrück 启发 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness**（manifest 预分配）
- **风格**：黑暗中前行 / 悲怆转光明 / 史诗
- **匹配理由**：从纳粹德国的出走、家族在抵抗中付出的生命代价、到把一个模糊学科锻造成精确科学——Through the Darkness 的"穿越黑暗终见光明"结构匹配其一生：物理学家的流亡、家族的牺牲与分子生物学的黎明。
- **本地路径**：`music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav` → 复制为 `presentations/20th_century/Max_Delbrück/Through_the_Darkness.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；卒日双值、双导师口径与家族史克制呈现务必落实。**
