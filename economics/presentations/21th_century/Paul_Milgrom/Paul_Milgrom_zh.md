# 经济学家立传提示词（Paul Milgrom）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2020 年得主 Paul Milgrom（保罗·米尔格罗姆）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Paul_Milgrom/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Paul Robert Milgrom（1948-04-20 生于美国密歇根州底特律，在世）
- **气质关键词**：**拍卖理论的奠基人、频谱拍卖的设计师、从精算师到经济工程师**
- **诺奖获奖理由**（逐字引用，2020 两人共享）：
  > "for improvements to auction theory and inventions of new auction formats"（表彰他们对拍卖理论的改进以及新拍卖形式的发明）
- **设计母题**：**同步加价（simultaneous ascending）**——多轮同步竞拍的时钟与波形：所有许可证同时升价、信息在回合间扩散；视觉隐喻为并列上升的阶梯与连接线，呼应「把博弈论变成经济工程」。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Paul_Milgrom/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Paul_Milgrom/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Paul_Milgrom_zh`、`VIDEO_NAME=Paul_Milgrom_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Milgrom 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | auction theory | 拍卖理论 | 诺奖核心；关联原理/赢家诅咒 | 封面、核心页 |
| 1 | game theory | 博弈论 | 声誉效应/超模博弈/重复博弈 | 理论页 |
| 2 | market design | 市场设计 | FCC 频谱拍卖与激励拍卖 | 政策页 |
| 3 | incentive theory | 激励理论 | 多任务委托代理（与 Holmström） | 理论页 |
| 4 | organizational economics | 组织经济学 | 互补性与影响力成本（与 Roberts） | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert B. Wilson | Milgrom ← 导师 | 斯坦福博士导师（1979 论文竞争性投标中的信息结构） |
| advisor-student | Susan Athey | Milgrom → 学生 | 博士生（infobox 明载），单调比较静态扩展者 |
| advisor-student | Luís Cabral | Milgrom → 学生 | infobox 明载 |
| advisor-student | Joshua Gans | Milgrom → 学生 | infobox 明载，单一交叉性质再表述者 |
| advisor-student | Gillian Hadfield | Milgrom → 学生 | infobox 明载 |
| advisor-student | Li Shengwu | Milgrom → 学生 | infobox 明载 |
| co-honored | Robert B. Wilson | 无向 | 2020 两人共享（拍卖理论的改进与新拍卖形式的发明） |
| spouse | Eva Meyersson | 无向 | 妻（infobox Spouse 明载） |
| colleague | John Roberts | 无向 | 长期合著者：限价/掠夺性定价/组织经济学/教科书 |
| colleague | Nancy Stokey | 无向 | no-trade theorem 共同提出者（1982） |
| colleague | Bengt Holmström | 无向 | 多任务委托代理系列合著者（1987/1991/1994） |
| colleague | Robert J. Weber | 无向 | 分布策略（1985）与关联/活动规则合著者 |
| colleague | David M. Kreps | 无向 | 1982 声誉效应"四人组"论文合著者 |

**Roth 边的归属裁定**：与 Alvin Roth 的共同开课关系由 Roth 侧 yaml 入库（库内规范名 **Alvin Eliot Roth**，collaborator 边）；本篇 yaml 不重复建边，正文照常叙述。

**不入库但提示词可叙述**：西北大学同事群 Roger Myerson/Bengt Holmström 任职期重叠（一次性叙述）；Chris Shannon（单调比较静态 1994 合著）与 Ilya Segal（包络定理 2002 合著）等单篇合著者（防 stub 膨胀）；Douglass North/Barry Weingast/Avner Greif（Law Merchant/商人行会论文合著）；Larry Ausubel/Peter Cramton/Bob Day（拍卖设计合著）；Jeremy Bulow/Jon Levin（Comcast 咨询）；Evan Kwerel（FCC 经济学家，评价者）。

## 五、配色方案 【人物专属】

- **气质**：精密、工程化、规则设计的秩序感
- **主色**：`#16324F`（manifest 预分配·拍卖场深蓝——竞价时钟与频谱波段的沉稳底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeAuction` 拍卖理论 — 深蓝 `#16324F`
  - `badgeGame` 博弈论 — 青绿 `#146B5A`
  - `badgeFCC` FCC 与市场设计 — 琥珀 `#B07A2A`
  - `badgeOrg` 组织与激励 — 玫瑰 `#A3455A`
- **背景母题**：同步上升的阶梯与回合线（多标的并行竞价的时间序列抽象），呼应 SMR 同步加价拍卖的核心发明。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 拍卖理论奠基人 / Paul Milgrom 1948– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒底特律、密歇根 BA 数学 1970、
    精算师生涯、斯坦福 MS 统计 1978/PhD 1979、Stanford Ely 讲席教授、诺奖 2020、核心领域）
03  核心贡献概览 — 拍卖理论 / 声誉与超模博弈 / 市场设计 / 组织与激励
04  早年：底特律与精算师 (1948–1975) — 犹太家庭四子之二、Ross 数学营第一名、准精算师十年
05  斯坦福博士：Wilson 门下 (1975–1979) — 统计硕士转商学博士、竞争性投标中的信息结构
06  西北与耶鲁 (1979–1987) — Kellogg 信息经济学群体、Weber 数分钟顿悟轶事
07  拍卖理论（核心贡献页）— 关联原理/公开性效应/赢家诅咒的缓解
08  声誉效应与超模博弈 — Kreps-Milgrom-Roberts-Wilson 四人组 1982、单调比较静态
09  组织经济学与激励设计 — 多任务委托代理、互补性、Economics, Organization and Management
10  FCC 频谱拍卖 1993-94（核心贡献页）— SMR 同步多轮拍卖、活动规则、Kwerel 证言
11  激励拍卖与 Auctionomics — 2016-17 广播激励拍卖、2006 Comcast 省 12 亿美元、2024 技术艾美奖
12  2020 诺贝尔奖 — 师徒共享、瑞典科学院"惠及全球卖者买者与纳税人"口径
13  荣誉与影响 — Nemmers 2008/BBVA 2012/Golden Goose 2014/Carty 2018、NAS 2006
14  遗产与结尾 — 经济工程学：理论照进市场 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由主体 | citation 主语是 "their"（与 Wilson 两人共享）；瑞典科学院补充语 "used their insights to design new auction formats..." 可引原文 |
| 师徒共享 | Wilson 是其博士导师兼共同得主——advisor-student 与 co-honored 两条边并行，note 区分；2020 是"师徒同台"罕见案例可点题 |
| 政治敏感红线 | page.md "Political views" 节载 2024 六诺奖得主联名公开信批评 Trump 财政贸易政策——**全部禁写** |
| 获奖年份口径 | 2020 诺奖；1996 年他为 Vickrey 致诺奖纪念演讲（Vickrey 宣布三天后去世）——勿把 1996 与其获奖混淆 |
| 精算师生涯 | 1970 密歇根数学 BA 后做精算师数年（旧金山/哥伦布），1974 Society of Actuaries Fellow，1975 才入斯坦福——时间线勿压缩 |
| 博士学位口径 | PhD 是 Stanford **business** (1979)，MS 是 statistics (1978)；论文 The structure of information in competitive bidding |
| Weber 轶事 | Weber 回忆"几分钟内写下前两篇合著论文的心脏"有英文原文可引（"And there, in a matter of a few minutes, was the heart of our first two joint papers."） |
| Kwerel 证言 | FCC 设计师 Kwerel 对其说服力的长段评价有原文；引用择短，勿整段搬运 |
| 关联合著者取舍 | Shannon/Segal/North/Weingast/Greif/Ausubel 等合著者只在正文叙述，不建库边（防 stub 膨胀，本篇 yaml 仅收 14 条） |
| 犹太口径 | page.md See also 挂 List of Jewish Nobel laureates，正文载父母犹太裔——一句背景可写，不展开 |
| 技术艾美奖 | 2024 Auctionomics 因频谱拍卖设计获技术与工程艾美奖——是公司获奖口径，勿写成个人演艺奖 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| auction theory | 拍卖理论 | 诺奖理由核心词 |
| simultaneous multiple round (SMR) auction | 同步多轮拍卖 | FCC 采用的设计名称 |
| activity rule | 活动规则 | 保证活跃竞价的机制，与 Weber 共同提出 |
| winner's curse | 赢家诅咒 | 共同价值拍卖的核心概念 |
| linkage principle | 关联原理 | Milgrom-Weber 1982，2004 改述为 publicity effect |
| no-trade theorem | 不交易定理 | 与 Stokey 1982 |
| supermodular games | 超模博弈 | 与 Roberts 1990c |
| monotone comparative statics | 单调比较静态 | 与 Shannon 1994 |
| multitask principal-agent | 多任务委托代理 | 与 Holmström 1991 |
| incentive auction | 激励拍卖 | 2016-17 双向拍卖重配电视频谱 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Shine Like The Sun**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav`，选曲参考 `curated_tracks.md`）
- **匹配理由**：昂扬上升的管弦电子气质对应「同步加价」的阶梯式上升意象与 1993 频谱拍卖从理论到百亿美元级应用的工程胜利；也贴合"经济工程学"改变世界拍卖方式的宏大落点（2020 诺奖）。
- **本地路径**：复制 `music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav` 到 `economics/presentations/21th_century/Paul_Milgrom/ShineLikeTheSun.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
