# 医学家立传提示词（George Emil Palade）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1974 年得主 George Emil Palade（乔治·埃米尔·帕拉德）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/George_Emil_Palade/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：George Emil Palade（1912-11-19 生于罗马尼亚 Iași ~ 2008-10-07 逝于加州 Del Mar，享年 95 岁），罗马尼亚-美国细胞生物学家，ForMemRS，耶鲁首任细胞生物学系主任
- **气质关键词**：**核糖体的发现者、分泌通路的绘图师、电镜与生化双刀流**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1974 条目，Palade/Claude/de Duve 三人共享）：
  > "for their discoveries concerning the structural and functional organization of the cell"（因其关于细胞结构与功能组织的发现）
- **设计母题**：**内质网上的黑点（ribosomes）与脉冲追踪的时序影像**——1955 年首次描述附着于粗面内质网的核糖体；用「膜网上密布的小圆点与时序箭头」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/George_Emil_Palade/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/George_Emil_Palade/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=George_Emil_Palade_zh`、`VIDEO_NAME=George_Emil_Palade_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Palade 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cell biology | 细胞生物学 | infobox Fields；1974 诺奖学科 | 全篇 |
| 1 | electron microscopy | 电子显微术 | 其诺奖级方法学创新之一 | 核心页 |
| 2 | biochemistry | 生物化学（细胞分级分离） | 与电镜并立的方法学双翼 | 核心页 |
| 3 | secretory pathway | 分泌通路 | 脉冲追踪实验确认粗面 ER 与高尔基体协作 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Albert Claude | 无向 | 1974 诺贝尔生理学或医学奖三人共享 |
| co-honored | Christian de Duve | 无向 | 1974 诺贝尔生理学或医学奖三人共享 |
| advisor-student | Albert Claude | 对方 → 导师 | 1946 年纽约大学结识后加入其洛克菲勒实验室（Claude 页明载其学生） |
| advisor-student | Robert Chambers | 对方 → 博士后东家 | 1946 年纽约大学生物实验室协助其工作 |
| advisor-student | Günter Blobel | Palade → 学生 | infobox Notable students 明载（1999 诺奖得主） |
| spouse | Irina Malaxa | 无向 | 1941-06-12 结婚，1969 年去世 |
| spouse | Marilyn Farquhar | 无向 | 加州大学圣迭戈分校细胞生物学家，1970 年结婚 |
| parent-child | Georgia Palade | 无向 | 女儿（1943 年生） |
| parent-child | Theodore Palade | 无向 | 儿子（1949 年生） |
| colleague | Philip Siekevitz | 无向 | 洛克菲勒长期合作（细胞分级分离路线的分泌研究） |
| colleague | Ewald R. Weibel | 无向 | 共同描述 Weibel-Palade 小体（内皮储存细胞器） |

**不入库但提示词可叙述**：其诺奖自传列出的 1960 年代合作者——Lewis Joel Greene/Colvin Redman/David Sabatini/Yutaka Tashiro（分级分离路线）与 Lucien Caro/James Jamieson（放射自显影路线），按择要口径未逐一建边（Siekevitz 已建）；Robert Chambers 之 NYU 阶段；2009 年核糖体结构化学奖（Ramakrishnan/Steitz/Yonath）为学术继承叙述。

## 五、配色方案 【人物专属】

- **气质**：电镜底片的银灰、罗马尼亚贵族学人的深紫、分泌通路的方向感
- **主色**：`#372A75`（电镜紫——荧光染色下的膜网与颗粒）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRibo` 核糖体 — 电镜紫 `#372A75`
  - `badgeER` 粗面内质网/高尔基体 — 深青 `#0E7490`
  - `badgePulse` 脉冲追踪 — 赭金 `#B07D2B`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：膜网上的小圆点与分泌时序箭头，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 核糖体的发现者 / George E. Palade 1912–2008 + 四色 badge + 右上头像 + 国籍行（Romania→USA）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Iași 出身、布加勒斯特 Carol Davila 医学院 MD 1940、
    洛克菲勒/耶鲁/UCSD 任职、诺奖 1974、核心领域）
03  核心贡献概览 — 核糖体 1955 / 粗面 ER 与高尔基体协作 / 分泌通路 / Weibel-Palade 小体
04  Iași 的贵族学人 (1912–1940) — boyar 家族希腊裔、父亲雅西大学哲学教授、康塔米尔母系、
    希腊东正教、1940 Carol Davila MD
05  布加勒斯特与赴美 (1940–1946) — 布加勒斯特大学教职、1946 赴美博士后
06  纽约与洛克菲勒 (1946–1952) — 协助 Chambers、结识 Claude 并入其实验室、1952 入籍
07  电镜下的细胞器图谱（核心贡献页）— 核糖体/线粒体/叶绿体/高尔基体的内部组织
08  1955：内质网上的核糖体（核心页）— 首次描述附着于 ER 的核糖体——蛋白质合成机器落位
09  脉冲追踪与分泌通路（核心页）— 证实分泌通路存在、粗面 ER 与高尔基体功能协同
10  Weibel-Palade 小体 — 与瑞士解剖学家 Weibel 共同描述内皮特有储存细胞器（vWF）
11  1974 诺奖：三人共享 — 与 Claude（其导师）、de Duve 共享，获奖理由逐字呈现、
    诺奖演讲 "Intracellular Aspects of the Process of Protein Secretion"
12  耶鲁与 UCSD (1973–2008) — 耶鲁首任细胞生物学系主任（George Palade 讲席教授命名）、
    UCSD 医学院科研事务院长
13  荣誉与认可 — Lasker 1966、Gairdner 1967、Horwitz 1970、EB Wilson 1981、ForMemRS 1984、
    NMS 1986、罗马尼亚星勋章、1975 罗马尼亚科学院荣誉院士
14  遗产与结尾 — 提携后进的导师传统（Blobel 1999）、2009 核糖体结构化学奖的学术回响 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生卒日双值 | 正文/intro 作 10 月 7 日，infobox 表格作 10 月 8 日——**以正文 2008-10-07 为准**（yaml 已如此），陷阱表留注防 Review 误改 |
| 国籍双值 | 罗马尼亚生（Iași，1912 年王国时期）+ 美国 1952 入籍——citation json "Romania United States" 双入；封面国籍行 Romania→USA |
| 1974 的三人分工 | Claude=分级分离与电镜开创、Palade=电镜方法学精修+核糖体+分泌通路、de Duve=溶酶体/过氧化物酶体——同句理由下三人贡献各述，勿互相混淆 |
| 无博士导师边 | Carol Davila 医学院 1940 MD，page.md 未载导师——**不建罗马尼亚阶段 advisor 边**；Chambers 是纽约大学博士后东家（assisting），Claude 是洛克菲勒实验室导师——两条边并行 |
| 合作者的择要口径 | 自传引文列出 7 名合作者——只入库 Siekevitz（首席长期合作）；Greene/Redman/Sabatini/Tashiro/Caro/Jamieson 在"不入库"段交代 |
| Horwitz 1970 | 与 Claude、Dulbecco 三人同获（1970）——注意 Dulbecco 是 1975 诺奖得主，此处是 Horwitz 奖语境，勿与 1974 诺奖混淆 |
| 核糖体表述 | "the ribosomes of the endoplasmic reticulum——first described in 1955"；2009 化学奖是"结构与功能研究"——发现权（Palade）与结构解析（2009）分开表述 |
| 政治元素 | 罗马尼亚王国时期出身、2021 罗马尼亚邮票致敬——无敏感；父系 boyar 家族与母系 Cantemir 家族是出身叙述 |
| 引语红线 | 正文仅自传引文（合作者名单）与 NMS 授奖词转述——无 Palade 本人直接引语，禁编 |
| 荣誉年份链 | NAS 1961、HonFRMS 1968、Lasker 1966、Gairdner 1967、Horwitz 1970、Nobel 1974、罗马尼亚科学院 1975、Golden Plate 1975、EB Wilson 1981、ForMemRS 1984、NMS 1986——勿串 |
| 职年链 | 布加勒斯特大学教职至 1946 → NYU 1946 → 洛克菲勒（1958-1973 为教授段）→ 耶鲁 1973-1990 → UCSD 1990-2008——"洛克菲勒 1958-1973"是 infobox 口径，与 1946 年加入不矛盾（1946-1958 为非教授职），叙述注意 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| structural and functional organization of the cell | 细胞的结构与功能组织 | 获奖理由逐字对应 |
| ribosome | 核糖体 | 1955 首次描述于 ER 上 |
| rough ER | 粗面内质网 | 附着核糖体的膜网 |
| pulse-chase analysis | 脉冲追踪实验 | 分泌通路证明方法 |
| secretory pathway | 分泌通路 | ER→高尔基体的蛋白输出路线 |
| zymogen granules | 酶原颗粒 | 分级分离路线的表征对象 |
| cisternal space | 潴泡腔 | 分泌产物分隔处 |
| Weibel-Palade bodies | Weibel-Palade 小体 | 内皮 vWF 储存细胞器 |
| radioautography | 放射自显影 | 第二条研究路线 |
| cell fractionation | 细胞分级分离 | 继承 Claude 的方法学 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：核糖体是每个活细胞里永不停歇的蛋白质工厂——Palade 让人类第一次看见它；从 1955 年的黑白电镜底片到 2009 年的原子级结构，这条学术血脉跨越半个多世纪仍在延续。Eternals 的永恒感正对应"细胞器图谱"从奠基到不朽的传承，也对应其门下 Blobel 到 2009 三人组的代代回响。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/George_Emil_Palade/Eternals.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
