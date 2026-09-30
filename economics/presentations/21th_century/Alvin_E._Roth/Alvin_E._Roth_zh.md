# 经济学家立传提示词（Alvin E. Roth）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2012 年得主 Alvin E. Roth（阿尔文·罗思）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Alvin_E._Roth/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Alvin Eliot Roth（1951-12-18 生于纽约市皇后区，在世）
- **气质关键词**：**市场设计的工程师、实验经济学的先驱、把理论开进现实的配对师**
- **诺奖获奖理由**（2012，与 Lloyd Shapley 共享；逐字引自 manifest）：
  > "for the theory of stable allocations and the practice of market design"（表彰他们关于稳定配置的理论与市场设计的实践）
- **设计母题**：**配对（matching）**——医生与医院、学生与学校、捐献者与受捐者：双列圆点之间的牵线与交换环构成「稳定配对」视觉隐喻，Gale–Shapley 算法正是母题的理论内核。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Alvin_E._Roth/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Alvin_E._Roth/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Alvin_E._Roth_zh`、`VIDEO_NAME=Alvin_E._Roth_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Roth 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | market design | 市场设计 | infobox Notable ideas；肾交换/择校/住院医配对，2012 诺奖实践翼 | 核心页 |
| 1 | matching theory | 匹配理论 | 稳定配置理论、Gale–Shapley 算法的应用与证明 | 核心页 |
| 2 | game theory | 博弈论 | Shapley value 效用视角、公理化谈判 | 理论页 |
| 3 | experimental economics | 实验经济学 | 1970s 起先驱，谈判/学习/市场设计实验 | 实验页 |
| 4 | kidney exchange | 肾脏交换 | NEPKE 共同创始人、全球肾交换 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致；共 15 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert B. Wilson | Roth → 学生 | 斯坦福博士导师（1974），论文为合作博弈论专题 |
| advisor-student | Muriel Niederle | Roth → 学生 | 博士生（infobox Doctoral students 明载） |
| advisor-student | Georg Weizsäcker | Roth → 学生 | 博士生（infobox Doctoral students 明载） |
| advisor-student | Parag Pathak | Roth → 学生 | 博士生（infobox Doctoral students 明载） |
| advisor-student | Fuhito Kojima | Roth → 学生 | 博士生（infobox Doctoral students 明载） |
| co-honored | Lloyd Shapley | 无向 | 2012 诺贝尔经济学奖共享（稳定配置理论与市场设计实践） |
| collaborator | David Gale | 无向 | Gale–Shapley 算法 1962 合著者；2013 Golden Goose 三人共同获奖 |
| collaborator | Marilda Sotomayor | 无向 | 合著 Two-Sided Matching（1990） |
| collaborator | Paul Milgrom | 无向 | 2000s 合开首门市场设计研究生课 |
| collaborator | Tayfun Sönmez | 无向 | 肾脏交换理论合作（Kidney Exchange 2004） |
| collaborator | Ido Erev | 无向 | 强化学习系列论文（高被引） |
| collaborator | Axel Ockenfels | 无向 | eBay 拍卖竞价行为系列研究 |
| spouse | Emilie Roth | 无向 | 心理学家，认知工程方向 |
| parent-child | Aaron Roth | Roth → 子 | 长子，宾夕法尼亚大学教授 |
| parent-child | Ben Roth | Roth → 子 | 次子，哈佛商学院副教授（2023 口径） |

**不入库但提示词可叙述**：父母 Ernest 与 Lillian Roth（中学教师，具名仅叙述）；兄 Ted Roth；肾交换合作者 Ünver/Ashlagi（note 内提及）；择校合作者 Abdulkadiroğlu；NRMP 合作者 Peranson/Vande Vate；实验合作者 Murnighan/Kagel/Ochs/Malouf；Global Kidney Exchange 的 Michael Rees；David Gale 的 TTC 算法归 Gale；逾四打博士生为概括数字不逐个建边。政治红线：Political views 节（2024 联署公开信）全篇禁写。

## 五、配色方案 【人物专属】

- **气质**：工程感、务实、理论的执行者
- **主色**：`#7A1E28`（配对绛红——交换环与匹配线的深红）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMatch` 市场设计 — 绛红 `#7A1E28`
  - `badgeExp` 实验经济学 — 靛蓝 `#1E3A5F`
  - `badgeGame` 博弈论 — 琥珀 `#C07A2A`
  - `badgeKidney` 肾脏交换 — 青绿 `#2F5D50`
- **背景母题**：双列圆点牵线与三角交换环（两人配对/三人循环交换），呼应「稳定配对」母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 市场设计的工程师 / Alvin E. Roth 1951– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、皇后区出身、Columbia BS 1971/Stanford PhD 1974、
    导师 Robert B. Wilson、Stanford McCaw 讲席、诺奖 2012、核心领域）
03  核心贡献概览 — 匹配理论 / 市场设计 / 实验经济学 / 肾脏交换
04  神童岁月 (1951–1974) — 16 岁无高中毕业证入哥伦比亚、运筹学 BS、斯坦福博硕、Wilson 门下
05  匹配理论的工程化（核心贡献页一）— NRMP 1984 论文证明稳定与防策略操纵、乡村医院定理
06  肾脏交换（核心贡献页二）— 与 Sönmez/Ünver 的理论、NEPKE 共同创始人、2008 十二人交换链
07  择校设计 — NYC 2003 / Boston 2005 采用学生优先延迟接受算法
08  实验经济学先驱（核心贡献页三）— 谈判实验、四国市场比较、强化学习模型（Erev 合作）
09  eBay 拍卖与市场时机 — 与 Ockenfels 的狙击行为研究、Xing 的 unraveling 研究
10  「反感」与市场边界 — Repugnance as a Constraint on Markets（引语原文）
11  门生与传承 — Niederle / Weizsäcker / Pathak / Kojima；逾四打学生的奖项谱系
12  荣誉与学会 — Lanchester 1990、Golden Goose 2013（与 Shapley/Gale）、NAS 2013、AEA 会长 2017
13  2012 斯德哥尔摩 — 与 Shapley 共享、citation 评语段（页明原文）
14  遗产与结尾 — 市场设计成为学科 + Who Gets What and Why + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | 全名 Alvin Eliot Roth，库内记录与 yaml 用 Alvin Eliot Roth（manifest name 逐字一致）；提示词标题用 Alvin E. Roth（页面主标题口径），两者并存注明 |
| 出生日期 | frontmatter 双值 1951-12-18/12-19，以正文 12-18 为准（陷阱表记录裁定） |
| 获奖理由归属 | 2012 与 Shapley 共享 "for the theory of stable allocations and the practice of market design"——Roth 是「实践翼」（把 Shapley 理论用于真实市场），勿写成纯理论奖 |
| Gale–Shapley 归属 | 算法 1962 由 David Gale 与 Lloyd Shapley 提出，Roth 的贡献是证明 NRMP 即该机制并再设计；勿写「Roth 发明」 |
| 政治红线 | Political views 节（2024 联署公开信）全篇禁写，不做任何转述 |
| 引语红线 | citation 评语段、repugnance 两句、Delmonico 医生的话均页面明载英文原文；引语框引原文+译文，勿造中文「原话」 |
| Golden Goose 2013 | Roth、Shapley、David Gale 三人共同获奖（页明），并入 Gale collaborator 行 note，勿单建 co-honored 重复边 |
| 学生数量 | 「逾四打博士生与约同等数量博士后」是概括表述；infobox 四人（Niederle/Weizsäcker/Pathak/Kojima）建边，勿把 Clark Medalist 等概括归属写成具体人 |
| 教职时间线 | Illinois 至 1982 → Pittsburgh Mellon 讲席 → 1998 Harvard → 2012 返 Stanford（2013 全职+Harvard emeritus），照录勿跳步 |
| 家庭 | 妻 Emilie Roth（认知工程心理学家）与子 Aaron（宾大）/Ben（哈佛商学院）均明载入库；父母仅叙述不入库 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| market design | 市场设计 | 获奖理由核心词，Roth 的旗帜领域 |
| stable allocations | 稳定配置 | 获奖理由核心词 |
| Gale–Shapley algorithm | Gale–Shapley 算法 | 延迟接受算法，勿归功 Roth 单人 |
| deferred acceptance | 延迟接受 | 学生优先变体用于择校 |
| strategy-proofness | 防策略操纵 | Roth 证明 DA 与 TTC 的性质 |
| rural hospital theorem | 乡村医院定理 | Roth 匹配理论成果 |
| kidney exchange | 肾脏交换 | NEPKE/全球肾交换 |
| repugnance | 反感 | Roth 引入经济学的概念 |
| unraveling | 解体（市场时间前移） | 市场设计失败模式 |
| top-trading-cycle | 优先交易循环（TTC） | Gale 提出、Shapley/Scarf 用于证明 |
| experimental economics | 实验经济学 | Roth 先驱贡献 |
| reinforcement learning | 强化学习 | 与 Erev 的选择行为模型 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness**（manifest 预分配，音乐库 `music_audio/`）
- **匹配理由**：市场设计的起点常是失灵的暗处——错配的医生、错配的肾源、被旧规则困住的学校；「穿越黑暗」的推进感对应 Roth 把理论带回现实、逐一修复市场失灵的工程叙事，也贴合肾交换从理论走向手术台的弧线。
- **本地路径**：复制 `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav` 到 `economics/presentations/21th_century/Alvin_E._Roth/Through the Darkness.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
