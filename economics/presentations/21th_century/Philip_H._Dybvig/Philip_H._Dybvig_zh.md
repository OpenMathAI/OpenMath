# 经济学家立传提示词（Philip H. Dybvig）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2022 年得主 Philip H. Dybvig（菲利普·迪布维格）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Philip_H._Dybvig/page.md`，与其冲突时以 page.md 为准（metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：Philip Hallen Dybvig（1955-05-22 生于佛罗里达州盖恩斯维尔，**在世**，卒年留白）
- **气质关键词**：**银行挤兑的建模者、多重均衡的揭示者、跨太平洋的金融学教授** —— 2022 年诺贝尔经济学奖获奖理由（与 Ben Bernanke、Douglas Diamond 共享，逐字引自 `economics/nobel_economics_citations.json` 2022 年 Philip H. Dybvig 条目）：
  > "for research on banks and financial crises"（表彰他们关于银行与金融危机的研究）
  —— 2022 年三人共享**同一句**理由，三人条目 citation 逐字一致，勿拆分改写。
- **设计母题**：**挤兑与多重均衡（bank run & multiple equilibria）**——Diamond–Dybvig 模型的本质：同一座银行，在「人人信任」与「人人挤兑」两个均衡之间摇摆，信念自我实现。视觉隐喻：一条水平面上并排的两组存款人剪影，一侧平静存款（实心圆），一侧涌向柜台（密集箭头），中间以天平/分岔线隔开，呼应诺奖演讲题 *Multiple Equilibria*。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Philip_H._Dybvig/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Philip_H._Dybvig/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Philip_H._Dybvig_zh`、`VIDEO_NAME=Philip_H._Dybvig_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Dybvig 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | economics of banking | 银行经济学 | Diamond–Dybvig 模型所在，诺奖核心 | 封面、核心页 |
| 1 | asset pricing | 资产定价 | 正文 Career 节明载的专长首位 | 核心页 |
| 2 | finance | 金融学 | infobox field_of_work；职业身份底盘 | 身份页 |
| 3 | corporate governance | 公司治理 | 正文 Career 节明载的专长之一 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 4 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Stephen A. Ross | 师→生（博士导师） | Yale 博士导师（1979），论文 Recovering Additive Utility Functions |
| co-honored | Douglas Diamond | 无向 | 2022 诺贝尔经济学奖三人共享（银行与金融危机研究） |
| co-honored | Ben Bernanke | 无向 | 2022 诺贝尔经济学奖三人共享（银行与金融危机研究） |
| collaborator | Douglas Diamond | 无向 | Diamond–Dybvig 模型；1983 合著 Bank Runs, Deposit Insurance, and Liquidity |

**不入库但提示词可叙述**：2022 年七名前学生的不当行为指控（正文 Controversies 节明载，当事人未具名不建关系；叙述时**客观一句带过**，禁展开细节、禁渲染、禁评价）；Southwestern University of Finance and Economics（机构非个人）；Western Finance Association（机构）；各期刊编委职务（机构）。

## 五、配色方案 【人物专属】

- **气质**：冷静、均衡、危机边缘的张力
- **主色**：`#123C5B`（manifest 预分配深蓝——银行大厅深夜灯光的冷峻感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRun` 银行挤兑模型 — 深蓝 `#123C5B`
  - `badgeAsset` 资产定价 — 青蓝 `#175E73`
  - `badgeGov` 公司治理 — 灰紫 `#52307C`
  - `badgeNobel` 诺奖荣誉 — 金 `#C9A227`
- **背景母题**：分岔的双均衡构图（平静存款侧 vs 挤兑侧），呼应「多重均衡」的核心思想。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 银行挤兑的建模者 / Philip H. Dybvig 1955– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地盖恩斯维尔、教育 Indiana BA 1976 /
    Penn 一年 / Yale MA·MPhil·PhD 1978–1979、任职 WashU Olin、诺奖 2022、核心领域）
03  核心贡献概览 — Diamond–Dybvig 模型 / 银行挤兑 / 存款保险 / 资产定价
04  早年与求学 (1955–1979) — Indiana 数学+物理双 BA（1976）→ Penn 一年 → Yale 三级学位
05  Yale 博士：Stephen A. Ross 门下 (1979) — 论文 Recovering Additive Utility Functions
06  Diamond–Dybvig 模型（核心贡献页）— 1983 论文 Bank Runs, Deposit Insurance, and Liquidity
07  银行挤兑的双重均衡 — 信念自我实现：不挤兑均衡 vs 挤兑均衡
08  存款保险的政策含义 — 为什么政府担保能消除坏均衡
09  资产定价与公司治理 — 专长的另外两翼
10  学术服务 — Western Finance Association 主席（2002–2003）、多刊编委
11  跨太平洋足迹 — 成都西南财经大学金融研究院院长（2010–2021）
12  2022 诺贝尔经济学奖 — 与 Bernanke / Diamond 共享；演讲 Multiple Equilibria（2022-12-08）
13  争议与反思 — 2022 年指控的客观一笔（仅一句，禁细节）
14  遗产与结尾 — 银行危机研究的现代格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由表述 | 2022 三人共享**同一句** "for research on banks and financial crises"，勿写成「Dybvig 因存款保险获奖」等拆分表述；中译统一「表彰他们关于银行与金融危机的研究」 |
| 模型署名 | 模型名是 **Diamond–Dybvig**（Diamond 在前），勿写成 Dybvig–Diamond；两人 1983 年合著论文首提 |
| 学位序列 | Indiana BA 1976（**数学与物理**，非经济）→ Penn 经济博士项目仅**一年**即转 Yale → Yale MA 1978 / MPhil 1978 / PhD 1979；勿漏 Penn 一年、勿把 BA 写成经济学 |
| 博士导师 | infobox 作 Stephen Ross，正文作 Stephen A. Ross，入库用 **Stephen A. Ross**（Yale 1979），勿与Rossby/Prentice 等同姓者混淆 |
| 任职线 | 现职 = 圣路易斯华盛顿大学 Olin 商学院 Boatmen's Bancshares 银行与金融讲席教授；曾任 Yale 教授、Princeton 助理教授；勿把 Olin 写成「华盛顿大学（西雅图）」 |
| 西南财大 | 2010–2021 任西南财经大学金融研究院院长（成都）；page.md 明载可写，但这是「在华任职事实」，叙述保持客观中立 |
| 争议节 | Controversies 一节按 page.md 客观存在；提示词与成稿**只允许一句**客观提及「2022 年遭七名前学生指控」，禁止转述具体指控细节（正文细节描述一律不进幻灯片），禁止评价与形容词 |
| 诺奖演讲 | 题为 *Multiple Equilibria*（2022-12-08），可作设计母题呼应；勿与获奖理由混淆 |
| 在世口径 | 1955 年生、在世，生卒页卒年留白，三处（封面/身份页/结尾）口径一致 |
| metadata 噪声 | metadata.json educated_at 缺 University of Pennsylvania，以 page.md infobox/正文为准（Penn 一年在读） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| bank run | 银行挤兑 | 模型核心场景，勿译「银行跑路」 |
| Diamond–Dybvig model | 戴蒙德–迪布维格模型 | 署名顺序 Diamond 在前 |
| multiple equilibria | 多重均衡 | 诺奖演讲题；两均衡并存 |
| deposit insurance | 存款保险 | 消除坏均衡的政策工具 |
| liquidity | 流动性 | 1983 论文题眼，勿译「清偿力」 |
| asset pricing | 资产定价 | 专长首位，与银行经济学并列 |
| corporate governance | 公司治理 | 专长之一 |
| Boatmen's Bancshares Professor | Boatmen's Bancshares 讲席教授 | 讲席名号含银行名，勿拆译 |
| Olin Business School |奥林商学院 | 隶属圣路易斯华盛顿大学 |
| Western Finance Association | 西部金融协会 | 2002–2003 任主席 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy**（主控补分配，`music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`；manifest 原为 null）
- **匹配理由**：Diamond–Dybvig 银行挤兑模型的悲剧性主题——存款人在「信任」与「恐慌」两个均衡间的自我实现式崩塌，本身就是金融史反复上演的悲剧脚本；Tragedy 的危机叙事张力正匹配「平静与恐慌只隔一条线」的一触即发感，同时贴合 2022 年诺奖「银行与金融危机」研究的沉重底色。
- **备选**（未采用）：★★ Mirage（双均衡的「似真幻象」感）；★ The Invisible Light（冷静纪录片感）。
- **本地路径**：复制 wav 到 `economics/presentations/21th_century/Philip_H._Dybvig/Tragedy.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、执行清单 【模板通用】

1. 读本提示词 + `Kenneth_G_Wilson_zh.tex` 骨架，建目录 `economics/presentations/21th_century/Philip_H._Dybvig/`；
2. 从 images.txt / Commons 下载肖像（250px→500px），404 则装饰圆占位；
3. 复制 Makefile 设 `MAIN=Philip_H._Dybvig_zh`、`VIDEO_NAME=Philip_H._Dybvig_zh`；
4. 写 tex（配色按第五节、Slide 序列按第六节），每写一页 `make` 查溢出（0 error、vbox≤10pt、hbox≤50pt）；
5. `make pdf` → `pdftoppm` 逐页目检 → `make images` → `make video` 出 mp4；
6. 全程遵守第七节陷阱表；引语仅限 page.md 载有英文原文者（引原文+译文），无原文不得造「原话」。
