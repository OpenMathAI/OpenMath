# 医学家立传提示词（Gregg L. Semenza）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2019 年得主（格雷格·塞门扎，HIF-1 的发现者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Gregg Leonard Semenza（1956-07-12 生于纽约市法拉盛，在世）
- **气质关键词**：**HIF-1 的发现者、缺氧适应分子开关的解密者、从转基因小鼠到临床医学的转化者** —— 2019 获奖理由（与 William Kaelin Jr.、Peter J. Ratcliffe 三人共享）：
  > "for their discoveries of how cells sense and adapt to oxygen availability"（因发现细胞如何感知并适应氧气供应）
- **设计母题**：**双亚基的氧闸**。HIF-1 由稳定的 HIF-1β 与氧敏感的 HIF-1α 组成——氧足则 α 消亡，氧乏则 α 累积并驱动 EPO。视觉隐喻：一枚双瓣分子闸门，一瓣恒亮、一瓣随氧明灭。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Gregg_L._Semenza/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Gregg_L._Semenza/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Gregg_L._Semenza/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Gregg_L._Semenza_zh`、`VIDEO_NAME=Gregg_L._Semenza_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Gregg_L._Semenza/images.txt`（2019 斯德哥尔摩照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Gregg_L._Semenza.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | oxygen sensing | 氧感知 | HIF-1 发现者，2019 诺奖核心 | 核心页 |
| 1 | transcription factors | 转录因子 | HIF-1α/β 双亚基结构 | 核心页 |
| 2 | hypoxia | 缺氧应答 | EPO 产生的缺氧调控 | 核心页 |
| 3 | vascular biology | 血管生物学 | Hopkins 细胞工程研究所血管项目创始主任 | 身份页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | William Kaelin Jr. | 无向 | 2019 诺贝尔生理学或医学奖三人共享（细胞感知与适应氧气供应的发现） |
| co-honored | Peter J. Ratcliffe | 无向 | 2019 诺贝尔生理学或医学奖三人共享（细胞感知与适应氧气供应的发现） |
| colleague | Peter J. Ratcliffe | 无向 | 研究交汇，共同确定细胞氧检测与 HIF-EPO 调控机制 |
| colleague | William Kaelin Jr. | 无向 | 研究交汇于细胞氧检测机制 |
| advisor-student | Elias Schwartz | 导师 | 宾大 MD-PhD 导师（β地中海贫血基因测序，1984 论文） |
| advisor-student | Saul Surrey | 导师 | 宾大 MD-PhD 导师 |
| spouse | Laura Kasch-Semenza | 无向 | Johns Hopkins 相识结婚，主持该校基因分型设施 |

> 在世者，relations=7 为诚实值，Review 勿误判虚增或缺漏。
> 不入库：Naoki Mori（2011 撤稿论文合著者——撤稿事件为学术诚信议题，非个人关系边）；四名兄弟姐妹；实验室成员未具名。
> 库内当时无 William Kaelin Jr. / Elias Schwartz / Saul Surrey / Laura Kasch-Semenza 记录，均由本 yaml 新建 stub（Kaelin 用 citation json 形式 `William Kaelin Jr.`，其本人批次 agent 将 UPD 回填）；Ratcliffe 已由本批 Ratcliffe yaml 规范化。

## 五、配色方案 【人物专属】

- **气质**：纽约郊区的克制 + 转录因子开关的精密 + 儿科医生的温度
- **主色**：深靛蓝 `#35459C`（HIF-1 转录因子的"分子蓝"，精密与深潜）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` HIF-1 发现 — 深靛蓝 `#35459C`
  - `badgeB` EPO 与转基因模型 — 暗红 `#8C2F1B`
  - `badgeC` 缺氧与癌症关联 — 灰紫 `#5C5470`
  - `badgeD` 血管生物学 — 青绿 `#0E7C7B`
- **背景母题**：双瓣闸门形细线元素（一瓣实、一瓣虚）+ 稀疏大圆，呼应 HIF-1α/β 双亚基。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — HIF-1 的发现者 / Gregg L. Semenza 1956– + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生纽约法拉盛、教育 Harvard AB/宾大 MD-PhD
    1984/Duke 儿科住院医、导师 Schwartz & Surrey、任职 Johns Hopkins、
    荣誉 Nobel 2019/Lasker 2016/NAS 2008、核心领域）
03  核心贡献概览 — HIF-1 的发现 / α/β 双亚基机制 / EPO 调控 / 氧感知与癌症
04  纽约郊区少年 (1956–1974) — 法拉盛出生、Westchester County 长大、
    意裔父系与德英爱裔母系、Tarrytown 中小学、Sleepy Hollow High School 1974（足球队中场）
05  哈佛与宾大 (1974–1984) — 哈佛本科研究医学遗传学、21 号染色体基因作图、
    宾大 MD-PhD（Schwartz/Surrey 门下）测序 β地中海贫血相关基因
06  Duke 儿科与 Hopkins 博后 — 儿科住院医训练、Johns Hopkins 博士后、
    转基因动物中评估基因表达对 EPO 产生的影响
07  HIF-1 的发现 — 鉴定表达 HIF 蛋白的基因序列、HIF-1β 稳定亚基 + HIF-1α 氧依赖降解亚基、
    双亚基结构的阐明
08  HIF-1α 是关键 — 缺失 HIF-1α 的实验动物血管畸形、EPO 水平下降、
    HIF 蛋白见于多种实验动物；HIF-1α 过表达可致癌——两面都要呈现
09  研究交汇：Semenza–Kaelin–Ratcliffe — 三组研究互相衔接确定细胞氧检测机制与
    HIF 对 EPO 生成的调控、催生调控该过程的药物（贫血/肾衰竭患者）
10  2016 Lasker → 2019 Nobel — Lasker 三人共享为前奏、2019 三人共享诺奖、
    2019-12-07 Nobel Lecture "Hypoxia-Inducible Factors in Physiology and Medicine"
11  学术荣誉序列 — Markey Scholar 1989、ASCI 1995、E. Mead Johnson 2000、NAS/AAP 2008、
    Gairdner 2010、IOM 2012、Lefoulon-Delalande 2012、Korsmeyer 2012、Wiley 2014
12  撤稿与学术诚信 ★ — 2011 撤回 Biochem J 论文、2022 撤回 PNAS 四篇、
    2022 PubPeer 对 52 篇合著论文图像的质疑、2023 PNAS/Oncogene 再撤、
    截至 2024 共 13 篇撤稿（图像复制/疑似数据处理问题）——按 page.md 客观陈述，不渲染不辩解
13  个人生活 — 妻 Laura Kasch-Semenza（Hopkins 相识，主持该校基因分型设施之一）
14  遗产 — HIF-1 成为缺氧生物学的枢纽概念、
    Hopkins 遗传医学教授与细胞工程研究所血管项目创始主任、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries of how cells sense and adapt to oxygen availability"（三人共享、their） |
| 三人分工 | Semenza 发现 HIF-1 及其双亚基结构；Kaelin 阐明 VHL 关联；Ratcliffe 证明氧感知普遍性并打通降解链——本篇以 HIF-1 发现为主线，勿越位 |
| HIF-1 结构 | HIF-1β 稳定 + HIF-1α 氧依赖降解——"哪个亚基对氧敏感"勿写反 |
| HIF-1α 双面 | 缺失→血管畸形+EPO 下降；过表达→致癌——抑制与过表达两面都要写，勿单面化 |
| 撤稿内容呈现 ★ | 13 篇撤稿（截至 2024）、PubPeer 52 篇质疑、2022 PNAS 四篇——page.md 明载且设独立章节，**须客观陈述时间线与原因（图像复制/疑似不当处理），不渲染、不为其辩护、不回避**；诺奖理由本身不受影响的判断勿擅自添加（page.md 未载） |
| metadata description 噪声 | metadata description 含 "author of many retracted papers" 编辑性短语——yaml 已采用不含该短语的客观描述，此处记录裁定 |
| 双导师 | Elias Schwartz + Saul Surrey 并列（infobox Doctoral advisors）——两条边都入库 |
| 本科研究 | 哈佛本科即作医学遗传学（21 号染色体基因作图）——是本科阶段，勿写成博士成果 |
| 妻子姓氏 | Laura Kasch-Semenza——婚后联合姓氏，勿写成 "Laura Kasch" 或 "Laura Semenza" |
| 出生地点 | 法拉盛（Flushing, Queens）——"纽约市"口径下可精确到 Flushing |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| HIF-1 | 缺氧诱导因子 1 | 其核心发现 |
| HIF-1α / HIF-1β | α/β 亚基 | α 氧敏感降解、β 稳定 |
| erythropoietin (EPO) | 促红细胞生成素 | 缺氧靶基因 |
| transgenic animals | 转基因动物 | 其博后阶段研究手段 |
| beta-thalassemia | β地中海贫血 | MD-PhD 论文对象 |
| gene mapping (chromosome 21) | 21 号染色体基因作图 | 本科阶段工作 |
| retraction | 论文撤稿 | 学术诚信事件，客观呈现 |
| vascular program | 血管项目 | Hopkins 细胞工程研究所内机构 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage**（manifest 预分配）
- **风格**：迷离 / 内省 / 氛围渐显
- **匹配理由**：HIF-1α 如"随氧明灭的幻影"——常氧时消散、缺氧时显形；Mirage 的渐显氛围匹配双亚基开关的隐现机制，亦呼应本篇如实呈现高光与撤稿阴影并存的复杂学术人生。
- **本地路径**：`music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` → 复制为 `presentations/21th_century/Gregg_L._Semenza/Mirage.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；撤稿章节务必客观、忠实 page.md 时间线。**
