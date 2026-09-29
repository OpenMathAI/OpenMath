# 医学家立传提示词（Victor Ambros）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2024 年得主 Victor Ambros（维克托·安布罗斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Victor_Ambros/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Victor Robert Ambros（1953-12-01 生于美国新罕布什尔州汉诺威，在世）
- **气质关键词**：**首个 microRNA 的发现者、被哈佛错过的人、小 RNA 世界的大门开启者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2024 条目，与 Gary Ruvkun 共享同一理由）：
  > "for the discovery of microRNA and its role in post-transcriptional gene regulation"（因发现 microRNA 及其在转录后基因调控中的作用）
- **设计母题**：**22 个核苷酸的开关（lin-4 小 RNA）**——微小的 RNA 链扣住靶 mRNA 的 3' 端、关闭蛋白翻译的意象：以短链 RNA 钳住长链的几何图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Victor_Ambros/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Victor_Ambros/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Victor_Ambros_zh`、`VIDEO_NAME=Victor_Ambros_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | microRNA | 微 RNA | 1993 发现首个 miRNA lin-4，2024 诺奖核心 |
| 1 | molecular biology | 分子生物学 | frontmatter field_of_work |
| 2 | developmental biology | 发育生物学 | C. elegans 幼虫发育时序（lin-4/LIN-14） |
| 3 | gene regulation | 基因调控 | 转录后抑制的反义 RNA 机制 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | David Baltimore | 对方 → 导师 | MIT 博士导师（1979；1975 诺奖得主） |
| advisor-student | H. Robert Horvitz | 对方 → 导师 | MIT 博士后导师（其实验室第一位博士后）；库内规范名 id=4751 |
| colleague | Gary Ruvkun | 无向 | lin-4/lin-14 3'UTR 互补配对合作发现者 |
| colleague | Rosalind Lee | 无向 | 1993 Cell 论文合作者（co-workers 明载） |
| colleague | Rhonda Feinbaum | 无向 | 1993 Cell 论文合作者（co-workers 明载） |
| co-honored | Gary Ruvkun | 无向 | 2024 诺贝尔生理学或医学奖共享（microRNA 与转录后基因调控） |

**不入库但提示词可叙述**：父 Longin（波兰移民、二战强制劳工、战后任美军翻译、1946 移美，家世叙述）；Howard Scott Silverman（捐赠冠名讲席，事件非关系）；Bartel/Tuschl（2002 Newcomb Cleveland 共享）；Mello/Fire/Baulcombe（多个共享奖，一次性奖项关系）；Baltimore 2008 "They lost a potential Nobel laureate" 引语可引原文。

## 五、配色方案 【人物专属】

- **气质**：隐微、精巧、被低估者的厚积薄发
- **主色**：`#52307C`（深紫——显微镜下被忽视的小分子之光）+ 香槟金诺奖色
- **badge 四分类色**：`badgeMiRNA` microRNA 深紫 `#52307C`；`badgeLin4` lin-4 时序开关 青绿 `#0E7C7B`；`badgeWorm` 线虫模型 苔绿 `#175E54`；`badgeUMass` UMass 岁月 琥珀 `#C07A2A`
- **背景母题**：短链 RNA 钳住长链的几何图案，呼应「22 个核苷酸的开关」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 首个 microRNA 的发现者 / Victor Ambros 1953– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1953-12-01 Hanover、佛蒙特奶牛场长大、
    MIT BS 1975/PhD 1979、UMass Chan Silverman 讲席、诺奖 2024）
03  核心贡献概览 — lin-4 非编码小 RNA / 3'UTR 反义配对 / lin-4L/lin-4S / miRNA 确立
04  波兰Roots与佛蒙特农场 (1953–1971) — 父亲二战流亡与移民史、八子女家庭、Woodstock 高中
05  MIT 双学位与 Baltimore 门下 (1971–1979) — BS 1975、PhD 1979（脊髓灰质炎病毒 RNA）
06  Horvitz 实验室的第一位博士后 (1979–1984) — C. elegans 异时性基因 lin-4 与 LIN-14 之谜
07  哈佛的错过 (1984–1992) — 发现 microRNA 前后未获终身教职；Baltimore 2008 评语可引
08  1993：lin-4 不编码蛋白（核心贡献页）— 与 Lee、Feinbaum 报告 22/61 核苷酸小 RNA、茎环结构
09  与 Ruvkun 的会师（核心贡献页）— lin-4S 与 lin-14 3'UTR 部分互补配对、反义抑制翻译
10  2000：let-7 与保守性 — Ruvkun 实验室鉴定第二个 miRNA 并证明跨物种保守（含人类）
11  Dartmouth 与 UMass (1992–) — Dartmouth 1992–2007、UMass Chan 2008–、Silverman 讲席
12  荣誉与认可 — Newcomb Cleveland 2002、Rosenstiel 2004、GSA Medal 2006、NAS 2007、
    Gairdner/Franklin/Lasker 2008、Horwitz/Massry 2009、Breakthrough 2015、Nobel 2024
13  波兰国籍 (2026) — 2026-03 申请、同年 9 月获批；波兰科学院讲演（身份叙述，勿过度展开）
14  遗产与结尾 — 从被拒的终身教职到 microRNA 时代；RNA 干扰与 miRNA 药物
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 双导师结构 | 博士导师 **David Baltimore**（infobox Doctoral advisor + 正文）；博士后导师 **H. Robert Horvitz**（正文"first postdoctoral fellow in the lab"）——frontmatter 把 Horvitz 也列为 doctoral_advisor 系 metadata 噪声，以 page.md 正文口径为准：师生边两条，Horvitz 注记博士后 |
| 发现年份 | lin-4 小 RNA 的鉴定报告发表于 1993 年 *Cell*；frontmatter 无冲突，但 Ruvkun 篇背景作"discovered in 1992 by Ambros' lab"——两篇各自忠于本人页面，引用时以"1992-1993 鉴定、1993 发表"表述 |
| 机制归属 | lin-4 编码小 RNA 是 Ambros 侧发现；与 lin-14 3'UTR 的互补配对是 **Ambros 与 Ruvkun 共同**发现——机制拼图两人各半，勿全归 Ambros |
| let-7 归属 | 第二个 miRNA let-7 及其跨物种保守性由 **Ruvkun 实验室** 2000 年鉴定——Ambros 篇只作"确认了一类分子"的呼应，勿写成自己的成果 |
| 哈佛未授终身教职 | page.md 明载 "Harvard denied tenure"——可如实叙述，Baltimore 2008 评语可引原文；勿渲染成"哈佛之耻"式标题党 |
| 国籍双口径 | Nobel 官方/总表=United States；page.md 明载 2026-03 申请、2026-09 获**波兰国籍**——yaml 取 US(0)+Poland(1)，封面国籍行 US，正文可叙述波兰渊源（父系移民史） |
| 奖项年份 | Newcomb Cleveland 2002、Rosenstiel 2004、GSA Medal 2006、NAS 2007、Gairdner/Franklin/Lasker/Warren 2008、Dickson/Horwitz/Massry 2009、Janssen 2012、Keio 2013、Gruber/Wolf 2014、Breakthrough 2015、March of Dimes 2016、Nobel 2024——勿串 |
| 在世者生卒 | 仅生年 1953-12-01，无卒年——封面用 1953– 开放区间 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| microRNA (miRNA) | 微 RNA | 获奖理由核心词 |
| lin-4 | lin-4 基因 | 首个 miRNA（异时性突变基因） |
| lin-4S / lin-4L | 短/长形式小 RNA | 22 与 61 核苷酸 |
| LIN-14 | LIN-14 蛋白 | 被 lin-4 渐进抑制的靶蛋白 |
| 3' untranslated region | 3' 非翻译区 | miRNA 结合位点所在 |
| antisense RNA mechanism | 反义 RNA 机制 | 早期对抑制机制的表述 |
| stem-loop | 茎环结构 | lin-4L 前体折叠 |
| let-7 | let-7 | 第二个 miRNA（Ruvkun 实验室，勿归 Ambros） |
| post-transcriptional gene regulation | 转录后基因调控 | 获奖理由核心词 |
| C. elegans | 秀丽隐杆线虫 | 模式生物 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从佛蒙特奶牛场到 MIT、从哈佛的冷遇到 UMass 的沉潜三十年——Ambros 的故事像一片深海的潜流，在最不起眼处积蓄着改变生物学图景的力量；"SEA" 的辽阔与深邃呼应 microRNA 世界被打开的瞬间。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Victor_Ambros/SEA.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
