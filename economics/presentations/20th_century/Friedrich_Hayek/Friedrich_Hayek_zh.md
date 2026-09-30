# 经济学家立传提示词（Friedrich Hayek）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1974 年得主 Friedrich Hayek（弗里德里希·哈耶克）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Friedrich_Hayek/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Friedrich August von Hayek（1899-05-08 生于维也纳，奥匈帝国 ~ 1992-03-23 逝于德国弗赖堡，享年 92 岁）
- **气质关键词**：**价格信号的信使、自发秩序的哲学家、大论战的中心人物**
- **诺奖获奖理由**（1974，与 Gunnar Myrdal 共享，逐字引自 manifest）：
  > "for their pioneering work in the theory of money and economic fluctuations and for their penetrating analysis of the interdependence of economic, social and institutional phenomena"（表彰他们在货币理论与经济波动理论方面的开创性工作，以及对经济、社会与制度现象相互依存关系的深刻分析）
- **设计母题**：**价格信号与自发秩序（price signal & spontaneous order）**——分散的知识经由价格汇聚而无需中央设计，是「无指挥的星群各自发光却连成星座」的视觉隐喻：离散光点与隐现连线构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Friedrich_Hayek/page.md`（同目录 `metadata.json` 仅作结构化参考；该页 611 行、202KB，页面最大，立传时用 offset 分块精读）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Friedrich_Hayek/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Friedrich_Hayek_zh`、`VIDEO_NAME=Friedrich_Hayek_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Hayek 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | monetary theory | 货币理论 | 奥地利商业周期理论、诺奖核心理由之一 | 核心页 |
| 1 | business cycle theory | 经济波动理论 | 信用扩张与资本错配（Prices and Production 1931） | 核心页 |
| 2 | political economy | 政治经济学 | 经济计算问题、价格信号（1945 知识论文） | 核心页 |
| 3 | political philosophy | 政治哲学 | The Road to Serfdom / Law, Legislation and Liberty | 哲学页 |
| 4 | theoretical psychology | 理论心理学 | The Sensory Order（1952），Monakow 实验室经历 | 心理学页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Ludwig von Mises | 无向 | 雇主与私塾导师；读《社会主义》后转向古典自由主义并加入其研讨班 |
| influence | Friedrich von Wieser | 无向 | 课堂影响深远并推荐其入职；frontmatter 曾列为博士导师但正文未证实（见陷阱表） |
| controversy | John Maynard Keynes | 无向 | 1931–1932 货币与财政政策论战（库内 id=850 复用） |
| controversy | Piero Sraffa | 无向 | Sraffa–Hayek debate：Sraffa 受 Keynes 之托反驳 |
| co-honored | Gunnar Myrdal | 无向 | 1974 诺贝尔经济学奖共享（货币与波动理论、经济社会制度相互依存分析） |
| colleague | Milton Friedman | 无向 | Mont Pèlerin Society 共同创办；芝加哥共事但不同系、无紧密合作 |
| colleague | Frank Knight | 无向 | Mont Pèlerin Society 共同创办 |
| colleague | George Stigler | 无向 | Mont Pèlerin Society 共同创办 |
| colleague | Lionel Robbins | 无向 | 1931 应 Robbins 之邀加盟 LSE |
| spouse | Helen Berta Maria von Fritsch | 无向 | 1926-08 结婚，1950-07 离异（1901–1960） |
| spouse | Helene Bitterlich | 无向 | 1950 再婚（1900–1996），远房表亲 |
| parent-child | Laurence Hayek | Hayek → 子 | 微生物学家（1934–2004），infobox 明载 |

**不入库但提示词可叙述**：Ludwig Wittgenstein 是其**二代表亲**（无亲缘关系类型，仅叙述；正文明载其哲学影响）；infobox Influences 列 40 余人（Böhm-Bawerk、Menger、Popper 等）防噪声不入库；LSE 时代「studied with」的 Coase、Baumol、Kaldor、Galbraith 等非正式博士生不入库；女 Christine（昆虫学家，无维基链接）不入库；1929 年前后与 Keynes 书信联署事件并入 controversy note 不单独建边。

## 五、配色方案 【人物专属】

- **气质**：冷峻、思辨、跨世纪的论战者
- **主色**：`#14324F`（奥派深蓝——货币与秩序的冷峻感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMoney` 货币与波动 — 深蓝 `#14324F`
  - `badgeSignal` 价格信号 — 青绿 `#0E7C7B`
  - `badgePhil` 政治哲学 — 灰紫 `#52307C`
  - `badgeMind` 心理学与认识论 — 琥珀 `#C07A2A`
- **背景母题**：离散光点与隐现连线（分散知识经价格汇聚的自发秩序抽象），呼应设计母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 价格信号的信使 / Friedrich Hayek 1899–1992 + 四色 badge + 右上头像 + 国籍行（Austria / United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地维也纳、维也纳大学 Dr.jur. 1921/Dr.rer.pol 1923、
    任职 LSE 1931–1950 / Chicago 1950–1962 / Freiburg / Salzburg、诺奖 1974、核心领域）
03  核心贡献概览 — 奥地利商业周期理论 / 经济计算问题与价格信号 / 《通向奴役之路》/ 自发秩序
04  维也纳早年与一战 (1899–1918) — 学术世家、表亲 Wittgenstein、1917 炮兵团意大利前线、左耳失聪
05  维也纳大学与米塞斯圈子 (1918–1931) — 双博士、Monakow 脑解剖实验室与《感觉的秩序》缘起、Geistkreis
06  LSE 岁月 (1931–1950) — Robbins 之邀、Prices and Production、与 Keynes 论战、Sraffa 反驳
07  《通向奴役之路》(1944) — 写作背景、Reader's Digest 节译与大众传播
08  经济计算问题与价格信号（核心贡献页）— 1945 The Use of Knowledge in Society（2011 AER 百年二十文之一）
09  芝加哥与社会思想委员会 (1950–1962) — 薪金由 Volker 基金资助、Mont Pèlerin Society、The Constitution of Liberty
10  弗赖堡与《法律、立法与自由》(1962–1979) — 三卷本 1973/1976/1979、萨尔茨堡的失误自述
11  1974 诺贝尔奖 — 与 Myrdal 共享、自我惊异与政治光谱平衡之说、1929 预测存疑的媒体叙事
12  《感觉的秩序》与心理学 — 连接学习的神经层面、对认识论的终身兴趣
13  影响与荣誉 — 撒切尔与 Reagan 的引用、CH 1984、Presidential Medal of Freedom 1991
14  遗产与结尾 — 价格理论与自发秩序的现代回响 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 博士导师口径 | frontmatter doctoral_advisor 列 Mises + Wieser，但**正文只载**双博士（法学 1921/政治学 1923）且 infobox 未列导师——两人按 influence 入库并注原因，禁建 advisor-student |
| 共享奖张力 | Myrdal 曾抱怨与"空想家"配对获奖；Hayek 自认获奖是为平衡政治光谱——两人 co-honored 双向各写一句客观呈现，禁单侧叙事 |
| 1929 预测叙事 | 诺奖委员会称其曾警告 1929 大危机，但正文指出**无文本证据**且引其 10-26 原文称"无需担心崩盘"——按存疑口径写，勿写成"精准预言崩盘" |
| Keynes 关系定位 | 1932 Times 书信联署、1931 批评《货币论》、Keynes "frightful muddles" 引语——用 controversy 类型；引语必须用 page.md 英文原文，禁改写中文"原话" |
| Friedman 关系 | 政见多合、货币政策有分歧、不同系共事**从未紧密合作**——colleague note 必须带此限定，勿写成"思想同盟挚友" |
| 国籍口径 | 1938 年起入英国籍并保留终身，但 1950 后未居英——yaml 按 manifest 拆 Austria / United Kingdom 两条 |
| Wittgenstein | 二代表亲（second cousin）+ 哲学影响自述——无亲缘 relation 类型，仅正文叙述禁建边 |
| 离婚 scandal | 1950 离婚在 LSE 引发风波、部分同事拒与往来——正文可叙述，两任妻子两行 spouse |
| Christine 不入库 | 女 Christine（昆虫学家）无维基链接不入库；子 Laurence Hayek（微生物学家，有链接）入库 |
| The Fatal Conceit | 1988 年"据称完稿"但**实际作者归属不明**（正文明言）——按存疑口径，勿写成其亲笔定稿 |
| 页面体量 | page.md 611 行 202KB 含大量 sidebar 模板噪声——立传分块精读正文节，勿把 Austrian School sidebar 的链接列表当史实 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| economic calculation problem | 经济计算问题 | 社会主义计算论战核心，非"算账问题" |
| price signal | 价格信号 | 1945 知识论文的核心概念 |
| spontaneous order | 自发秩序 | 勿译"自然秩序" |
| Austrian business cycle theory | 奥地利商业周期理论 | 信用扩张→资本错配机制 |
| dispersed knowledge | 分散的知识 | 与"信息不对称"区分 |
| The Road to Serfdom | 《通向奴役之路》 | 1944，书名定译 |
| The Sensory Order | 《感觉的秩序》 | 1952 理论心理学 |
| Mont Pèlerin Society | 朝圣山学社 | 1947 共同创办的新自由主义者国际论坛 |
| classical liberal | 古典自由主义者 | Hayek 自我认同，拒绝 conservative 标签（正文明载） |
| denationalisation of money | 货币的非国家化 | 自由银行主张，正文载其立场 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：辽阔、冷峻、深不见底——对应分散知识如海面、价格信号如洋流的无形秩序；也贴合其横跨一个世纪、从维也纳到芝加哥再到弗赖堡的漂泊学术人生。同届共享得主 Myrdal 亦分配同曲（manifest 预分配），提示词各自忠于本人页面即可。
- **本地路径**：复制 `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` 到 `economics/presentations/20th_century/Friedrich_Hayek/SEA.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/Friedrich_Hayek/page.md` | 事实基准（唯一事实来源，611 行需分块） |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册 |
| `MySQL/data/Friedrich_Hayek.yaml` | 入库 yaml（与本文第三、四节一致） |
| `economics/economics_list_data.py` / `nobel_economics_citations.json` | 获奖理由中文对照 |

## 十一、执行清单 【模板通用】

1. 读 page.md 建立事实基准（本文件已沉淀，直接核对即可）
2. 下载肖像（images.txt 有 URL 直接用 500px；404 用 Commons `Special:FilePath`，再 404 装饰圆占位）
3. 复制 BGM wav 到人物目录
4. 写 tex（配色按第五节、Slide 序列按第六节）
5. 编译循环：0 error、vbox ≤ 10pt、hbox ≤ 50pt
6. pdftoppm + read_file 逐页目检
7. make images/video；Review-1 修正写回本文件
