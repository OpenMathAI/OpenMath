# 医学家立传提示词（Jack W. Szostak）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2009 年得主（杰克·绍斯塔克，端粒保护实验合作者、生命起源与人工生命的探路人）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Jack William Szostak（1952-11-09 生于伦敦，在世；蒙特利尔/渥太华长大）
- **气质关键词**：**端粒功能合作证明者、世界首个酵母人工染色体的建造者、RNA 时代与生命起源研究的旗手** —— 2009 获奖理由（与 Elizabeth Blackburn、Carol W. Greider 三人共享）：
  > "for the discovery of how chromosomes are protected by telomeres and the enzyme telomerase"（因发现染色体如何受端粒和端粒酶保护）
- **设计母题**：**从端粒到原细胞**。同一双手，先证明染色体末端的保护帽，再试图在实验室里重建生命的起点——视觉隐喻：一条从染色体末端延伸到原始细胞膜的演化线。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Jack_W._Szostak/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Jack_W._Szostak/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Jack_W._Szostak/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Jack_W._Szostak_zh`、`VIDEO_NAME=Jack_W._Szostak_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Jack_W._Szostak/images.txt`（2025 家中照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Jack_W._Szostak.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | telomere biology | 端粒生物学 | 1982 端粒保护实验，2009 诺奖核心 | 核心页 |
| 1 | genetics | 遗传学 | 酵母人工染色体（YAC）与重组机制 | 研究页 |
| 2 | synthetic biology | 合成生物学 | 人工染色体、aptamer、体外进化 | 研究页 |
| 3 | origin of life | 生命起源 | 原细胞、RNA 复制、功能信息 | 晚近页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ray Wu | 导师 | 康奈尔大学生物化学博士导师（1977 PhD） |
| co-honored | Elizabeth Blackburn | 无向 | 2009 诺贝尔生理学或医学奖三人共享（端粒与端粒酶保护染色体） |
| co-honored | Carol W. Greider | 无向 | 2009 诺贝尔生理学或医学奖三人共享（端粒与端粒酶保护染色体） |
| colleague | Elizabeth Blackburn | 无向 | 1982 合作证明四膜虫端粒重复序列保护酵母不稳定质粒 |
| advisor-student | David Bartel | 学生 | infobox 明载学生（随机序列 RNA 连接酶项目） |
| advisor-student | Jennifer Doudna | 学生 | 博士导师，哈佛 1989 年 RNA 复制酶课题 |
| advisor-student | Hiroaki Suga | 学生 | infobox 明载学生 |
| advisor-student | Terry Orr-Weaver | 学生 | infobox 明载学生 |
| colleague | Ruth Sager | 无向 | 初到哈佛时在 Sidney Farber 癌症研究所为其提供职位 |
| collaborator | Katarzyna Adamala | 无向 | 合作证明柠檬酸等弱螯合剂可同时解决原细胞镁离子伤 RNA 与破膜问题 |
| spouse | Terri-Lynn McCormick | 无向 | 结婚，育二子 |

> 在世者，relations=11 为诚实值（4 学生均 infobox 明载），Review 勿误判虚增。
> ★ 库内曾存在并行批次预建的 stub `Jack Szostak`（#4325，含 Doudna 导师边）——本批已按"改指→删 stub"合并入 manifest 规范名 `Jack W. Szostak`，Review 核对库内无 `Jack Szostak` 裸记录即可。
> 不入库：Chen K. Chai（Jackson 实验室暑期导师，人物未建条）；Howard Goodman（招募其赴 MGH）；Leslie E. Orgel（磷酰亚咪唑酯假说先行者，学术先驱非个人关系）；Gerald Joyce（体外进化独立发明者）；Cech/Altman（核酶发现者，领域语境）；Terri-Lynn McCormick 之外的家人。
> Doudna 用库内规范记录（#4248, Q56068）。

## 五、配色方案 【人物专属】

- **气质**：从染色体的深海蓝到生命起源的原始汤
- **主色**：深海蓝 `#24506E`（染色体末端的冷峻，亦含"原始海洋"的生命起源意象）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 端粒保护 — 深海蓝 `#24506E`
  - `badgeB` YAC 与基因组 — 深青 `#0E7C7B`
  - `badgeC` RNA 时代 — 紫红 `#7A3E6E`
  - `badgeD` 原细胞与生命起源 — 琥珀 `#B4632C`
- **背景母题**：一条自上而下的演化线——顶端是染色体末端重复序列，末端化为圆形原细胞轮廓，四色渐变。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 从端粒到生命起源 / Jack W. Szostak 1952– + 四色 badge + 右上头像 + 国籍行 USA/Canada
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 London、成长 Montreal/Ottawa、
    教育 McGill BSc 1972/Cornell PhD 1977、导师 Ray Wu、任职 Harvard/MGH/HHMI/Chicago、
    荣誉 Nobel 2009/Lasker 2006/NAS 分子生物学奖 1994、核心领域）
03  核心贡献概览 — 端粒保护 / 酵母人工染色体 / RNA 时代 / 人工细胞与生命起源
04  神童岁月 (1952–1977) — 伦敦出生、波兰英裔家庭、蒙特利尔/渥太华成长、
    15 岁高中毕业获 scholars prize、19 岁 McGill 细胞生物学学士、
    1970 Jackson 实验室暑期项目（Chai 门下）、康奈尔 Ray Wu 门下 1977 PhD
05  哈佛起步 (1978–1984) — Sidney Farber 癌症研究所自立实验室（Sager 提供职位）、
    基因定位与基因操作技术（哺乳动物基因图谱、人类基因组计划的基石）
06  1982：端粒保护染色体的证明 — 与 Blackburn 合作：四膜虫端粒重复序列保护酵母不稳定质粒、
    端粒序列进化保守、诺奖基金会官方陈述引文（page.md 载）
07  世界首个酵母人工染色体 — YAC 建造、哺乳动物基因定位的工具、
    减数分裂重组（基因洗牌）机制的澄清
08  RNA 时代 (1990s) — Cech/Altman 核酶发现后的转向、体外进化技术（与 Joyce 各自独立）、
    首个 aptamer（术语由其首创）、Bartel 的随机序列 RNA 连接酶
09  学生军团 — Bartel/Doudna（2020 化学诺奖）/Suga/Orr-Weaver（infobox 明载）、
    HHMI 与 MGH 的 Alex Rich Distinguished Investigator
10  2009 诺贝尔奖 — 三人共享、Nobel lecture "DNA Ends: Just the Beginning"（2009-12-07）、
    Lasker 2006（三人）为前奏
11  生命起源：原细胞计划 — 磷酰亚咪唑酯单体的模板延伸、5'-5' 咪唑鎓桥二核苷酸中间体、
    Orgel 的先导假说、功能信息（functional information）概念
12  与 Adamala 的柠檬酸方案 — 镁离子伤 RNA 与破膜两大难题、弱阳离子螯合剂一举两得、
    早期地球原细胞的化学自洽
13  移师芝加哥 (2022–) — University Professor、Origins of Life Initiative、
    2024 Science 评论警示 mirror life 风险
14  遗产 — 端粒到人工生命的统一叙事：基因组如何稳定、生命如何开始、
    NAS/AAAS/美国哲学会会员、Kosciuszko 基金会波兰裔杰出科学家学部、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for the discovery of how chromosomes are protected by telomeres and the enzyme telomerase"；其个人角色是 1982 与 Blackburn 的端粒功能证明（酶的发现属 Blackburn-Greider 线）——分工勿混 |
| 名称规范 ★ | manifest/库内规范名为 **Jack W. Szostak**；并行批次曾建裸 stub `Jack Szostak`（#4325，Doudna 导师边），本批已合并删除——正文首次出现写全名 Jack William Szostak |
| 国籍口径 | 出生伦敦、波兰英裔、蒙特利尔/渥太华长大；Nobel 官方 "Canada United States"；page.md metadata 还列 Poland——yaml 取 United States(0)+Canada(1)（manifest 为主），波兰裔仅作血统叙事不入国籍列，裁定记录于此 |
| 体外进化归属 | "also developed independently by Gerald Joyce"——**独立发明者两人**，勿写成 Szostak 独创 |
| aptamer | 术语由 Szostak 首次使用（"term he used for the first time"）——"首创术语"≠"首个适配体应用" |
| Doudna 师承 | Jennifer Doudna（2020 化学诺奖）是其博士生（库内既有边：哈佛 1989 RNA 复制酶课题）——跨奖师承是亮点，note 沿用既有行 |
| Orgel 定位 | 磷酰亚咪唑酯对早期地球聚合的关键性由 Orgel 等首先提出——Szostak 组是发展者，勿写"首创" |
| 引语 | page.md 仅载诺贝尔基金会官方陈述（telomere 保护机制转述），无本人直接引语——**勿杜撰引语** |
| Polish roots 引语 | 他对 Wprost 周刊自述"记得波兰根源但不识波兰语"——可用（page.md 有转述），注明系访谈 |
| 在世者关系 | relations=11 均有 page.md 依据（4 学生为 infobox Notable students 明载），Review 勿误判虚增 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| telomere | 端粒 | 其诺奖角色是功能证明（1982） |
| yeast artificial chromosome (YAC) | 酵母人工染色体 | 世界首个，基因定位工具 |
| in vitro evolution | 体外进化 | 与 Joyce 独立平行发明 |
| aptamer | 适配体 | 术语首创者 |
| protocell | 原细胞 | 生命起源研究核心模型 |
| phosphorimidazolide | 磷酰亚咪唑酯 | 活化核苷酸单体 |
| functional information | 功能信息 | 其提出的量化概念 |
| mirror life | 镜像生命 | 2024 Science 警示评论主题 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart**（manifest 预分配）
- **风格**：律动 / 解构 / 电子氛围
- **匹配理由**：其科学生涯是两次"拆解与重组"——把染色体末端拆解出保护机制，把生命拆解为可合成的原细胞；Falling Apart 的解构-重建律动匹配"从端粒到生命起源"的双幕叙事。
- **本地路径**：`music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav` → 复制为 `presentations/21th_century/Jack_W._Szostak/Falling_Apart.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；体外进化与 aptamer 归属务必按 page.md 精确表述。**
