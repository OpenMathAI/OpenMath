# 医学家立传提示词（Har Gobind Khorana）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1968 年得主（哈尔·霍拉纳，遗传密码的化学解读者、首个合成基因的缔造者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Har Gobind Khorana（1922-01-09 生于英属印度旁遮普 Raipur（今巴基斯坦）~ 2011-11-09 卒于马萨诸塞州 Concord，享年 89 岁）
- **气质关键词**：**用化学合成破译遗传密码的建筑师、世界首个合成基因的缔造者、化学生物学的奠基人之一** —— 1968 获奖理由（与 Robert W. Holley、Marshall Warren Nirenberg 三人共享）：
  > "for their interpretation of the genetic code and its function in protein synthesis"（因解析遗传密码及其在蛋白质合成中的功能）
- **设计母题**：**用字母造生命**。从重复单元 RNA（UCUCUCU…）到世界首个人工合成基因——"化学家把遗传语言写成句子"。视觉隐喻：重复的碱基字母块逐级组装成基因长链。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Har_Gobind_Khorana/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Har_Gobind_Khorana/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Har_Gobind_Khorana/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Har_Gobind_Khorana_zh`、`VIDEO_NAME=Har_Gobind_Khorana_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Har_Gobind_Khorana/images.txt`（NIH 讲座奖照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Har_Gobind_Khorana.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | molecular biology | 分子生物学 | 遗传密码解析，1968 诺奖核心 | 核心页 |
| 1 | genetic code | 遗传密码 | 重复单元 RNA 与密码子指认、终止密码子 | 核心页 |
| 2 | oligonucleotide synthesis | 寡核苷酸合成 | 首位化学合成者→首个合成基因（1972） | 研究页 |
| 3 | chemical biology | 化学生物学 | 同行称其"奠基人之一" | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Roger J.S. Beer | 导师 | 利物浦大学博士导师（1948，有机化学） |
| advisor-student | Vladimir Prelog | 导师 | ETH 苏黎世博士后（1948-49，生物碱化学，无薪职位） |
| advisor-student | Alexander R. Todd | 导师 | 剑桥博士后（1950-52，肽与核苷酸） |
| advisor-student | George Wallace Kenner | 导师 | 剑桥博士后同期合作指导（肽与核苷酸） |
| advisor-student | Shiladitya DasSarma | 学生 | infobox 明载博士生 |
| co-honored | Robert W. Holley | 无向 | 1968 诺贝尔生理学或医学奖三人共享（遗传密码的解析及其在蛋白质合成中的功能） |
| co-honored | Marshall Warren Nirenberg | 无向 | 1968 诺贝尔生理学或医学奖三人共享（遗传密码的解析及其在蛋白质合成中的功能） |
| spouse | Esther Elizabeth Sibler | 无向 | 1952 年于瑞士相识结婚，2001 年去世，育三子女 |

> relations=8 为诚实值，Review 勿误判虚增。
> 不入库：父母 Ganpatrai Khorana（patwari 村税务员）与 Krishna Devi（背景叙事）；子女 Julia/Emily/Dave（Emily 早逝仅一句）；Todd 实验室其他成员；Scripps 科学理事会（机构职务）。
> 库内既有 Vladimir Prelog（#3341, Q83501，1975 诺奖化学）、Alexander R. Todd（#3582, Q157242，1957 诺奖化学）规范记录直接引用；本人记录 UPD 复用库内 stub #3916 回填 Q107462；其余对手方新建 stub。

## 五、配色方案 【人物专属】

- **气质**：旁遮普麦田的金 + 化学合成的严谨蓝 + "从树下乡学到 MIT 讲席"的纵深
- **主色**：合成蓝 `#24506E`（化学合成的精密与实验室的冷光）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 遗传密码 — 合成蓝 `#24506E`
  - `badgeB` 合成基因 — 琥珀 `#B4632C`
  - `badgeC` 化学生物学 — 深青 `#0E7C7B`
  - `badgeD` 从难民到讲席 — 灰紫 `#5C5470`
- **背景母题**：重复字母块（UCU/UCU…）沿对角线渐次组装为长链，四色块交替。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 用化学书写遗传密码 / Har Gobind Khorana 1922–2011 + 四色 badge + 右上头像 + 国籍行 India/USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生英属印度 Raipur、教育 Punjab 大学/
    Liverpool PhD 1948、ETH/Cambridge 博后、任职 UBC/Wisconsin/MIT（1970-2007）、
    荣誉 Nobel 1968/National Medal of Science 1987/Padma Vibhushan 1969、核心领域）
03  核心贡献概览 — 重复 RNA 破译密码 / 终止密码子 / 首个合成基因 / 化学生物学
04  村里的穷孩子 (1922–1945) — 英属印度旁遮普 Raipur 村、五子中最幼、
    父为 patwari（村税务员）、全村约百人中"几乎唯一识字的家庭"、
    最初四年在树下上课、6 岁才有第一支铅笔、D.A.V. 中学与 Government College Lahore、
    印巴分治全家迁德里为难民、此后终生未回出生地
05  利物浦与苏黎世 (1945–1949) — 印度政府奖学金赴 Liverpool、1948 PhD（Beer 门下）、
    ETH Zurich 随 Prelog 无薪研究生物碱化学近一年
06  剑桥与温哥华 (1949–1960) — 奖学金返英随 Kenner 与 Todd（1957 诺奖化学）研究肽与核苷酸、
    1952 UBC 英国哥伦比亚研究理事会——"给了全世界最多的自由"（mentor 引语转述）、
    核酸与重要生物分子的合成
07  Wisconsin 与密码破译 (1960–1970) — 酶研究所共同主任、1962 生化教授、1964 Elvehjem 讲席、
    重复单元 RNA 实验：UCUCUCU→两种氨基酸交替、三重复→三种肽链、
    含 UAG/UAA/UGA 的四重复只产生二肽三肽→揭示三个终止密码子
08  1968 诺贝尔奖 — 三人共享官方理由逐字引用、Nobel web 口径：Khorana"用酶构建不同 RNA 链、
    产出蛋白质、其氨基酸序列解出谜底"、1968-12-12 共同发表诺奖演讲、
    同年获 Louisa Gross Horwitz Prize（与 Nirenberg）
09  1972：世界首个合成基因 — 首位化学合成寡核苷酸者→离体全合成功能基因、
    非水相化学延伸长链 DNA、连接酶/聚合酶组装、方法预示 PCR 的发明
10  合成生物学的日常化 — 人工基因片段用于测序/克隆/动植物工程、
    寡核苷酸订购的商业化——"从任何公司邮购一段基因"
11  后期研究 — 细菌视紫红质（bacteriorhodopsin，光能→质子梯度）→视紫红质（rhodopsin）
12  荣誉序列 — NAS 1966/AAAS 1967/美国哲学会 1973/ForMemRS 1978、
    Padma Vibhushan 1969、Horwitz 与 Lasker 1969、Willard Gibbs 1974、Gairdner 1980、
    National Medal of Science 1987、2018-01-09 96 岁冥诞 Google Doodle
13  个人生活与身后 — 妻 Esther Elizabeth Sibler（瑞士相识，1952 结婚，2001 先逝）、
    三子女（Emily Anne 早逝）、2011-11-09 卒于 Concord（89 岁）
14  遗产 — Khorana Program（印美学生交流奖学金）、UBC 园区 Khorana 公园、
    "化学生物学的奠基人之一"（前同事评价口径）、从合成基因到 CRISPR 时代的引用谱系、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their interpretation of the genetic code and its function in protein synthesis"（三人共享、their）；Khorana 角色按 Nobel web 转述："用酶构建不同 RNA 链→产出蛋白质→氨基酸序列解出谜底" |
| 生日口径 ★ | 出生于英属印度，page.md 明言"确切日期不确定、他自认可能是 1922-01-09、后载于部分文件并被广泛接受"——yaml 取 01-09，幻灯片可加"（自述日期）"注记 |
| 国籍裁定 ★ | manifest 仅 United States；citation json 官方 "India United States"；page.md citizenship 仅 US、metadata 列四朝——yaml 取 India(0)+United States(1)（官方顺序），出生地今属巴基斯坦的事实照 page.md 呈现，供主控统一口径 |
| 停止密码子 | UAG/UAA/UGA 三个终止密码子由其四重复 RNA 实验揭示——三个并列勿漏 |
| 首个合成基因年份 | 首位化学合成寡核苷酸者（1968 诺奖时的成就口径）→ **1972** 首个离体全合成功能基因——两个"第一"年份勿混 |
| PCR 关系 | 其方法"预示（anticipated）PCR 的发明"——是预示不是发明，措辞照 page.md |
| 四位导师 | Beer（PhD）+ Prelog（ETH 无薪博后）+ Todd 与 Kenner（剑桥博后）——四条 advisor-student 边 note 区分阶段；Prelog/Todd 用库内规范记录 |
| 分治叙事 | 全家因印巴分治迁德里为难民、终生未回出生地——客观一句，勿煽情 |
| 自传引语 | "Although poor, my father was dedicated to educating his children..."（page.md 英文原文在，可引原文+译文） |
| 姓名变体 | 正文 Har Gobind Khorana；Nobel 页作 "H. Gobind Khorana"——正文统一前者的规范名 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| genetic code | 遗传密码 | 1968 诺奖核心 |
| stop codon | 终止密码子 | UAG/UAA/UGA |
| repeating-unit RNA | 重复单元 RNA | UCUCUCU 实验设计 |
| oligonucleotide synthesis | 寡核苷酸合成 | 首位化学合成者 |
| synthetic gene | 合成基因 | 1972 世界首例 |
| bacteriorhodopsin | 细菌视紫红质 | 1970s 后期研究对象 |
| patwari | 村税务员 | 父亲职业（自传转述） |
| Padma Vibhushan | 莲花装勋章 | 印度第二高文民勋章，1969 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage**（manifest 预分配）
- **风格**：迷离 / 反思 / 氛围渐显
- **匹配理由**：从树下课堂到破译生命密码——Mirage 的渐显氛围匹配"最不可能的起点长出最确定的结构"的叙事张力；重复字母块的实验设计也带着海市蜃楼般的重复韵律，最终显影为真实的密码表。
- **本地路径**：`music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` → 复制为 `presentations/20th_century/Har_Gobind_Khorana/Mirage.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；生日/国籍裁定与两个"第一"的年份务必精确。**
