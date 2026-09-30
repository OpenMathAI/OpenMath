# 经济学家立传提示词（Christopher A. Pissarides）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2010 年得主 Christopher A. Pissarides（克里斯托弗·皮萨里德斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Christopher_A._Pissarides/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Sir Christopher Antoniou Pissarides（1948-02-20 生于尼科西亚，英属塞浦路斯，在世，2013 年受封爵士）
- **气质关键词**：**搜寻摩擦市场的测绘师、DMP 模型的共同奠基人、失业经济学的工程师**
- **诺奖获奖理由**（2010 三人共享，逐字引用）：
  > "for their analysis of markets with search frictions"（表彰他们对存在搜寻摩擦的市场的分析）
- **设计母题**：**搜寻与匹配（search & matching）**——空缺岗位与求职者在噪声中双向摸索、相遇成对的动态过程：两群点在模糊场域中运动、连线成对，构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Christopher_A._Pissarides/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/21th_century/Christopher_A._Pissarides/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Christopher_A._Pissarides_zh`、`VIDEO_NAME=Christopher_A._Pissarides_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Pissarides 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | labour economics | 劳动经济学 | infobox Discipline，DMP 模型所在领域 | 核心页 |
| 1 | search and matching theory | 搜寻匹配理论 | matching function，诺奖核心 | 核心页 |
| 2 | unemployment economics | 失业经济学 | 《Equilibrium Unemployment Theory》 | 专著页 |
| 3 | economic growth | 经济增长 | 结构性增长（Ngai-Pissarides 2007） | 增长页 |
| 4 | economic policy | 经济政策 | 塞浦路斯国家经济委员会主席、未来工作研究 | 政策页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Michio Morishima | Morishima → Pissarides | LSE 博士导师（论文 *Individual behaviour in markets with imperfect information*），infobox+正文双载 |
| colleague | Dale T. Mortensen | 无向 | 1994 合著《Job Creation and Job Destruction in the Theory of Unemployment》+2005 IZA 劳动经济学奖共同获得 |
| co-honored | Dale T. Mortensen | 无向 | 2010 诺贝尔经济学奖三人共享（搜寻摩擦市场分析） |
| co-honored | Peter Diamond | 无向 | 2010 诺贝尔经济学奖三人共享（搜寻摩擦市场分析） |

**不入库但提示词可叙述**：frontmatter doctoral_advisor 另列 Dale T. Mortensen，但 infobox 与正文只载 Morishima——Mortensen 系 frontmatter-only，**禁建导师边**（2010 三人是合作者与共同得主非师生）；Richard Layard / Martin Hellwig（1986 合著论文，非持续关系）；L. Rachel Ngai（2007 合著论文，文献合作不入）；Naomi Climer / Anna Thomas（2018 未来工作研究院共创者，非学术界关系）；Mitsotakis 任命（政策事件）。

## 五、配色方案 【人物专属】

- **气质**：地中海蓝绿、 job search 的动态场、英伦学统
- **主色**：`#1E6B52`（manifest 预分配；地中海蓝绿——爱琴海与伦敦之间的学术桥）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeSearch` 搜寻匹配 — 深绿 `#1E6B52`
  - `badgeDMP` DMP 模型 — 靛蓝 `#1E3A5F`
  - `badgeLab` 劳动市场 — 玫瑰 `#A63A2B`
  - `badgeCy` 塞浦路斯之桥 — 琥珀 `#C07A2A`
- **背景母题**：双向搜寻的连线网络（岗位与求职者两组点动态连线成对），呼应 matching function。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 搜寻摩擦市场的测绘师 / Christopher A. Pissarides 1948– + 四色 badge + 右上头像 + 国籍行（Cyprus / United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地尼科西亚、教育 Essex BSc/MSc / LSE PhD、
    导师 Morishima、任职 LSE 1976–/塞浦路斯大学/HKUST、诺奖 2010、核心领域）
03  核心贡献概览 — 搜寻摩擦 / matching function / 均衡失业理论 / 结构性增长
04  尼科西亚少年 (1948–1970s) — Pancyprian Gymnasium、塞浦路斯国民警卫队服役、Essex 本硕
05  LSE 博士：Morishima 门下 — 不完全信息市场中的个体行为
06  搜寻理论：从 1979 到 DMP（核心贡献页一）— 1979 Job Matchings 论文、职位空缺与失业并存之谜
07  1994 论文：职位的创造与毁灭（核心贡献页二）— 与 Mortensen 合著、matching function、劳动力流动
08  《Equilibrium Unemployment Theory》 — 均衡失业的宏观理论专著（MIT Press，第二版 2000）
09  从理论到政策：欧洲失业之辩 — LSE Regius 教授、宏观中心主席
10  2010 诺贝尔奖 — 与 Diamond、Mortensen 三人共享；2010-12-08 诺奖演讲《Equilibrium in the Labour Market with Search Frictions》
11  政策顾问的十年 — 塞浦路斯国家经济委员会主席（2012–2014）、希腊长期增长战略（2020）、EuroAfrica Interconnector
12  未来工作研究 — 2018 共创 Institute for the Future of Work、Pissarides Review（2022）
13  荣誉与认可 — IZA 2005 · 爵士衔 2013 · 雅典科学院 2015 · 塞浦路斯纪念邮票
14  遗产与结尾 — DMP 模型成为宏观劳动分析的标准件 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方 citation "for their analysis of markets with search frictions"（三人共享同句）；正文首段另一变体句末多 "theory of" 字样，引文框以 citation 原文为准 |
| 三人角色 | 2010 得主 Peter Diamond（MIT）、Dale T. Mortensen（Northwestern）、Pissarides（LSE）：Diamond 奠基搜寻分析、Mortensen 加以扩展、Pissarides 将其实施并做宏观应用——三人分工在诺奖新闻稿中有载，但本 page.md 未载分工细节，幻灯片只写「三人共享」，勿擅自演绎分工 |
| 导师裁定 | 博士导师只入 **Michio Morishima**（infobox+正文双载）；frontmatter 另列 Dale T. Mortensen 系 metadata-only，**禁建导师边**，陷阱表注明防 Review 误建 |
| Mortensen 双边 | 与 Mortensen 同时存在 colleague（1994 合著+IZA 共同获奖）与 co-honored（2010 诺奖）两行，为合法双行（参照 Hench–Kendall 先例），勿去重 |
| 国籍顺序 | manifest "Cyprus / United Kingdom"，page.md citizenship Cypriot British；yaml 按此顺序两条；出生地写英属塞浦路斯（1948 年） |
| Regius 教授 | LSE 经济学 Regius Professor（皇家讲座教授），1976 起执教 LSE；勿与「剑桥 Regius」混淆 |
| 名字拼写 | Christopher Antoniou Pissarides；希腊语 Χριστόφορος Αντωνίου Πισσαρίδης 可作封面装饰，正文献词用英文形式 |
| 爵士衔 | 2013 Birthday Honours 受封 Knight Bachelor（services to economics），此后头衔 Sir；2010 前文献不加 Sir |
| 2012 塞浦路斯 | 任国家经济委员会主席于塞浦路斯金融危机期间，2014 年底辞职专注学术——事件客观呈现 |
| metadata 噪声 | metadata.json date_of_birth 单值 1948-02-20 无冲突；nationality 两值与 manifest 顺序一致 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| search frictions | 搜寻摩擦 | 获奖理由核心词 |
| search and matching theory | 搜寻匹配理论 | DMP 模型的框架 |
| matching function | 匹配函数 | 其核心建模工具 |
| DMP model | DMP 模型 | Diamond-Mortensen-Pissarides 缩写 |
| job creation and job destruction | 职位创造与职位毁灭 | 1994 论文双主题 |
| equilibrium unemployment | 均衡失业 | 专著主题，勿与自然率混译 |
| vacancies | 职位空缺 | 与失业并存的贝弗里奇曲线变量 |
| Beveridge curve | 贝弗里奇曲线 | 空缺-失业关系（若 page.md 未载则仅术语表出现） |
| labour economics | 劳动经济学 | 英式拼写（美式 labor），保持一致即可 |
| Regius Professor | 皇家讲座教授 | LSE 之 Chair，勿译「首席教授」泛化 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：搜寻是个体在市场中的孤独旅程——「Lonesome」的低回情绪对应失业者的等待与空缺岗位的空悬；而相遇成对的匹配瞬间，恰是这首曲子从阴郁走向柔和的转调。
- **本地路径**：复制 `music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav` 到 `economics/presentations/21th_century/Christopher_A._Pissarides/Lonesome.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
