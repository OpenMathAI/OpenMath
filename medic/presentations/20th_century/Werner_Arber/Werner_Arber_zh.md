# 医学家立传提示词（Werner Arber）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1978 年**得主（与 Hamilton O. Smith、Daniel Nathans 三人共享）。
> 本文件是 Arber 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Werner Arber（1929-06-03 生，在世），瑞士微生物学家、遗传学家
- **气质关键词**：**限制性内切酶现象的理论预言者、噬菌体遗传学家、宗座科学院的首位新教院长** —— 1978 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for the discovery of restriction enzymes and their application to problems of molecular genetics"（因其发现限制性内切酶及其在分子遗传学问题上的应用）
- **设计母题**：**细菌的剪刀与印章（scissors and seals）**。限制-修饰系统：酶切割外源 DNA，甲基化标记自家 DNA——以「被印章保护与被剪刀剪断的双链」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Werner_Arber/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Werner_Arber/`；Makefile 复制后设 `MAIN=Werner_Arber_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microbiology | 微生物学 | 1978 诺奖核心：噬菌体与宿主限制现象 | 核心页 |
| 1 | molecular genetics | 分子遗传学 | 限制-修饰系统假说 | 核心页 |
| 2 | bacteriophage research | 噬菌体研究 | λ 噬菌体缺陷突变体论文起点 | 早年页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Hamilton O. Smith | 无向 | 1978 诺贝尔生理学或医学奖三人共享（限制酶） |
| co-honored | Daniel Nathans | 无向 | 1978 诺贝尔生理学或医学奖三人共享（限制酶） |
| colleague | Daisy Roulland Dussoix | 无向 | 日内瓦实验室学生/合作者，其工作为诺奖奠基 |
| colleague | Jean Weigle | 无向 | λ 前噬菌体研究的关键启发者 |
| colleague | Grete Kellenberger | 无向 | λ 前噬菌体研究的关键启发者 |
| colleague | Gio Bertani | 无向 | 1958 赴南加州大学随其作噬菌体遗传学 |
| colleague | Gunther Stent | 无向 | 访 Berkeley 数周；1963 甲基化证据出自其实验室 |
| colleague | Joshua Lederberg | 无向 | 1959-60 访斯坦福其实验室数周 |
| colleague | Esther Lederberg | 无向 | 1959-60 访斯坦福其实验室数周 |
| colleague | Salvador Luria | 无向 | 1959-60 访 MIT 其实室数周 |

**方向约定**：无向关系 from<to 自动归一。

## 五、配色方案 【人物专属】

- **气质**：瑞士的精确、噬菌体世界的微观秩序、信仰与科学的从容共存
- **主色**：`#146B5A`（放线菌绿，噬菌体与微生物）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeRestr` 限制酶 — 剪刀红 `#A33A2E`；`badgeModif` 甲基化修饰 — 印章蓝 `#3B4E8C`；`badgePhage` 噬菌体 — 病毒青 `#1B7A6B`；`badgeVatican` 宗座科学院 — 教廷赭 `#8C5A26`
- **背景母题**：浅绿底上双链线条，一段被波浪标记（修饰）、一段被剪口断开（限制），错落成网。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 细菌剪刀的预言者 / Werner Arber b.1929 + 四色 badge + 右上肖像 + 国籍行（Switzerland）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生、Gränichen、ETH/日内瓦/巴塞尔、巴塞尔 Biozentrum、荣誉）
03  核心贡献概览 — 限制-修饰系统假说 / 甲基化机制 / 噬菌体遗传学 / 重组 DNA 之基
04  阿劳与 ETH (1929–1953) — 化学与物理、1953 日内瓦电子显微镜助理
05  从电镜到噬菌体 (1953–1958) — λ 缺陷前噬菌体突变体论文、1958 博士、Morse 与 Lederberg 夫妇的转导实验启发
06  Weigle 与 Kellenberger 的助力 — 「极具成效」的指引、转向分子遗传学的自述
07  加州游学 (1958–1960) — USC Bertani 处噬菌体遗传学、Stent/Lederberg 夫妇/Luria 实验室数周
08  限制现象的理论化（核心贡献页）— 宿主控制限制与修饰、Dussoix 的实验贡献、1965 日内瓦特聘教授
09  1963 甲基化证据 — Stent 的 Berkeley 实验室中得出：修饰即核苷酸甲基化
10  巴塞尔 Biozentrum (1971–) — 新建跨学科生物中心的首批入驻者
11  1978 诺贝尔奖 — 与 Smith/Nathans 三人共享、通往重组 DNA 技术之路
12  Dussoix 的信 — 1978 年信件自述其贡献未被充分承认——荣誉分配的又一案例，客观呈现
13  宗座科学院 (1981–2017) — 本笃十六世任命为首任新教院长、World Cultural Council 创始成员
14  信仰与进化 — 有神进化论自述（引原文两段）、「Lindau 诺奖大会 27 次传灯」
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生年双值 | frontmatter 有 1929-06-03 与 1929-01-01 两值；正文 infobox 作 **3 June 1929**（Gränichen, Aargau）——取 06-03，此处注明 |
| 在世人物 | 1978 诺奖得主中仍在世者（b. 1929）；卒年留白不杜撰 |
| 获奖理由 | "for the discovery of restriction enzymes and their application to problems of molecular genetics"——**their**（与 Smith/Nathans 共享） |
| 三人分工 | Arber 是**限制-修饰现象的理论化者**（假说+甲基化机制预言）；Smith 分离出首个 II 型酶；Nathans 作图应用——分工链条勿混 |
| Dussoix 争议 | 1978 年她致信表达对其研究未获承认的失望（图注明载）——本篇客观呈现「其工作为诺奖奠基」；colleague 边不升级为 controversy（正文非对抗性叙述） |
| 名字规范 | 信件署名 Daisy Dussoix、正文亦作 Daisy Roulland Dussoix——yaml 用 'Daisy Roulland Dussoix' |
| Kellenberger | Grete Kellenberger(-Gujer)；库内另有 Eduard Kellenberger(4385)——勿混 |
| 引语 | 诺奖自传长段（lambda 转导启发）+ 信仰两段引语——引原话须用这些，勿自造 |
| 家庭 | 已婚（妻未具名）、二女含 Silvia Arber（著名神经科学家）——本批不建 parent-child 边 |
| 宗教表述 | 有神进化论是其公开自述——客观收录引语，不加评断 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| restriction endonuclease | 限制性内切酶 | 诺奖理由核心词 |
| restriction-modification system | 限制-修饰系统 | 其理论框架 |
| nucleotide methylation | 核苷酸甲基化 | 1963 修饰机制证据 |
| bacteriophage lambda | λ 噬菌体 | 其论文起点 |
| lysogenic strain | 溶原菌株 | 缺陷突变体研究 |
| transduction | 转导 | Lederberg 夫妇/Morse 实验语境 |
| recombinant DNA | 重组 DNA | 三人工作的应用方向 |
| Biozentrum | 巴塞尔生物中心 | 1971 起的东家 |
| Pontifical Academy of Sciences | 宗座科学院 | 2011-2017 任首位新教院长 |
| Lindau Nobel Laureate Meetings | 林道诺奖得主大会 | 1981 起 27 次参与 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage** — Alex-Productions（manifest 预分配）
- **风格**：神秘 / 微观 / 探秘感
- **匹配理由**：细菌世界里「外源 DNA 被剪、自家 DNA 被印」的隐形机制，在噬菌体实验的迷雾中被 Arber 一层层揭开——Mirage 的探秘感匹配限制-修饰系统从现象到假说到甲基化证据的解谜之旅（第二次使用该曲，首用 Dehmelt，同为微观世界守望者）。
- **本地路径**：`music_audio/` 下 Mirage 曲目 → 复制为 `presentations/20th_century/Werner_Arber/Mirage.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

