# 经济学家立传提示词（Claudia Goldin）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2023 年得主 Claudia Goldin（克劳迪娅·戈尔丁）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Claudia_Goldin/page.md`，与其冲突时以 page.md 为准（metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：Claudia Dale Goldin（1946-05-14 生于纽约市布朗克斯，**在世**，卒年留白）
- **气质关键词**：**女性劳动力史的经济侦探、U 型曲线的绘制者、哈佛经济系首位女性终身教授** —— 2023 年诺贝尔经济学奖获奖理由（独享，逐字引自 `economics/nobel_economics_citations.json` 2023 年 Claudia Goldin 条目）：
  > "for having advanced our understanding of women's labour market outcomes"（表彰她增进了我们对女性劳动力市场表现的理解）
- **设计母题**：**U 型曲线与静默革命（U-shaped curve & quiet revolution）**——女性劳动参与率随经济发展先降后升的 U 型轨迹，是 Goldin 最具辨识度的图形语言；「greedy jobs」「静默革命」则是其晚期叙事。视觉隐喻：一条贯穿百年的 U 型曲线从背景穿过，曲线两端缀满代表不同代际女性的小圆点，向右上方延伸出「趋同」的收束。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Claudia_Goldin/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Claudia_Goldin/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Claudia_Goldin_zh`、`VIDEO_NAME=Claudia_Goldin_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Goldin 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | labor economics | 劳动经济学 | infobox Discipline；女性劳动力市场为诺奖核心 | 封面、核心页 |
| 1 | economic history | 经济史 | 身份定位 economic historian；NBER DAE 项目主任 28 年 | 核心页 |
| 2 | economics of gender | 性别经济学 | 性别工资差距、U 型参与率、greedy jobs | 核心页 |
| 3 | economics of education | 教育经济学 | 《教育与技术的赛跑》、大学性别差距逆转 | 教育页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 9 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Fogel | 师→生（博士导师） | 芝加哥大学博士导师（1972），论文城市奴隶制经济 |
| influence | Alfred E. Kahn | 无向 | 康奈尔本科课堂引路人，激发转向经济学 |
| spouse | Lawrence F. Katz | 无向 | 哈佛经济学同事，正文 Personal life 明载 |
| collaborator | Lawrence F. Katz | 无向 | 合著避孕药论文（2002）、教育与技术的赛跑（2008）等 |
| collaborator | Frank Lewis | 无向 | 1975 合著内战经济成本论文 |
| collaborator | Ilyana Kuziemko | 无向 | 2006 合著大学性别差距逆转论文 |
| colleague | Claudia Olivetti | 无向 | NBER Gender in the Economy 研究组共同主任 |
| colleague | Jessica Goldberg | 无向 | NBER Gender in the Economy 研究组共同主任 |
| advisor-student | Leah Boustan | Goldin → 学生 | 博士生（infobox Doctoral students 明载） |

**不入库但提示词可叙述**：父母 Leon Goldin / Lucille Rosansky Goldin（正文有载但职业非学术谱系，family 叙事页可写、不入 parent-child——按医侧惯例直系父母可入库，若 Review 认为应入库再补）；Gary S. Becker（frontmatter doctoral_advisor 有载、正文全无载，**不入库**并注明）；第一只金毛 Kelso 与治疗犬 Pika（叙事彩蛋，非人物关系）；Tatyana Avilova（UWE 项目合作者，一次性项目）。

## 五、配色方案 【人物专属】

- **气质**：温润、历史纵深、史料侦探的沉稳
- **主色**：`#0F4C5C`（manifest 预分配深青——档案卷宗与老照片的沉静感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeLabor` 女性劳动史 — 深青 `#0F4C5C`
  - `badgePill` 避孕药与职业生涯 — 玫瑰 `#A64D6D`
  - `badgeRace` 教育与技术的赛跑 — 琥珀 `#C07A2A`
  - `badgeNobel` 诺奖荣誉 — 金 `#C9A227`
- **背景母题**：百年 U 型曲线 + 散点代际群像，呼应「静默革命」的渐进感。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 女性劳动力史的经济侦探 / Claudia Goldin 1946– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地布朗克斯、教育 Cornell BA 1967 /
    Chicago MA 1969·PhD 1972、任职 Harvard、诺奖 2023、核心领域）
03  核心贡献概览 — U 型参与率 / 避孕药革命 / 教育与技术的赛跑 / 贪婪的工作与性别趋同
04  布朗克斯的考古学少女 (1946–1967) — Microbe Hunters 引向细菌学 → Cornell 修 Alfred Kahn 课转向经济
05  芝加哥博士 (1969–1972) — Robert Fogel 门下，城市奴隶制论文；「经济学家如侦探」
06  晋阶之路 (1971–1990) — Wisconsin→Princeton→Penn→Harvard；1990 哈佛经济系首位女性终身教职
07  U 型曲线（核心贡献页）— 农业到工业参与率下降、服务业扩张回升
08  避孕药的威力 — 与 Katz 合著（2002）：推迟婚育、投资教育与职业
09  静默革命 (2006) — 三阶段转型；「nice jobs」与期望的改变
10  教育与技术的赛跑 (2008) — 与 Katz 合著：1980 年代前教育跑赢技术、此后逆转与不平等
11  贪婪的工作与性别趋同 (2014/2021) — A Grand Gender Convergence；Career and Family
12  公共服务与荣衔 — NBER DAE 主任 28 年、AEA 主席 2013、IZA/Nemmers/BBVA
13  2023 诺贝尔经济学奖 — 独享；第三位获奖女性、首位独享女性；BBC 100 Women
14  遗产与结尾 — 性别差距研究的现代格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 2023 **独享**，理由句 "for having advanced our understanding of women's labour market outcomes"（英式 labour）；勿写成三人共享、勿漏 "labour market outcomes" 原文 |
| 第三位女性 | page.md 明载「third woman to win the award, first to win solo」，可写；排序口径以 page.md 为准，勿自行数出「第四位」 |
| 博士导师 | infobox 只载 **Robert Fogel**；frontmatter doctoral_advisor 三值（Fogel/Alfred E. Kahn/Gary S. Becker）系 Wikidata 噪声——Kahn 是康奈尔本科课堂（用 influence），Becker 正文无载禁入库 |
| 政治观点节 | Political views 节（2018 不平等评论、2024 十六得主联名信、2025 数据担忧）涉 Donald Trump 等政治内容，**一律禁写**；诺奖叙事不涉政治 |
| 2026 WNBA | page.md 明载 2026 年协助 WNBA 球员谈判薪资上涨 400%，可作一句趣闻，客观陈述不评价 |
| 任职序列 | Wisconsin 1971–73 → Princeton 1973–79 → Penn 1979–90 → Harvard 1990 起；「Princeton 与 Penn 首位获授/达成终身教职的女性经济学家」是 page.md 明载可写 |
| 合著分工 | 避孕药论文 2002-08 发表（*The Power of the Pill*）；《赛跑》书 2008（版权页 2008，正文一处作 2009——统一用 2008 并可在陷阱表注两说）；Kuziemko 论文 2006 |
| 名犬 Pika | 金毛 Pika 2024 去世、闻迹赛获奖、治疗犬——人文化彩蛋可作引言/结尾点缀，勿喧宾夺主 |
| 在世口径 | 1946 年生、在世，卒年留白，三处口径一致 |
| NBER 双职 | DAE 项目主任（1989–2017）与 Gender in the Economy 研究组共同主任（与 Olivetti/Goldberg）是两条不同线，勿混 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| women's labour market outcomes | 女性劳动力市场表现 | 获奖理由核心词，英式 labour 拼写照抄 |
| U-shaped female labor force function | U 型女性劳动参与函数 | 1994 工作论文，先降后升 |
| The Power of the Pill | 避孕药的威力 | 2002 合著论文，勿泛译「药丸的力量」 |
| quiet revolution | 静默革命 | 2006 论文，第三阶段的定名 |
| greedy jobs | 贪婪的工作 | 2014 论文概念，加班时长回报递增的岗位 |
| The Race Between Education and Technology | 教育与技术的赛跑 | 2008 合著书名，勿意译跑错 |
| gender wage gap | 性别工资差距 | 「数百年存在」是 page.md 结论 |
| Development of the American Economy (DAE) | 美国经济发展项目 | NBER 项目名，Goldin 主任 28 年 |
| Henry Lee Professor | Henry Lee 讲席教授 | 哈佛教席名号 |
| industrial organization | 产业组织 | 博士方向之一（与 labor 并列） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands**（manifest 预分配，`music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`）
- **匹配理由**：Goldin 的研究跨越两个世纪的美国女性就业史——从农业社会到静默革命，是一条不断开拓「新大陆」的长时段叙事；New Lands 的开阔感匹配 U 型曲线终段的上扬与「性别趋同最后一章」的希望基调。
- **本地路径**：复制 wav 到 `economics/presentations/21th_century/Claudia_Goldin/NewLands.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、执行清单 【模板通用】

1. 读本提示词 + `Kenneth_G_Wilson_zh.tex` 骨架，建目录 `economics/presentations/21th_century/Claudia_Goldin/`；
2. 从 images.txt / Commons 下载肖像（250px→500px），404 则装饰圆占位；
3. 复制 Makefile 设 `MAIN=Claudia_Goldin_zh`、`VIDEO_NAME=Claudia_Goldin_zh`；
4. 写 tex（配色按第五节、Slide 序列按第六节），每写一页 `make` 查溢出（0 error、vbox≤10pt、hbox≤50pt）；
5. `make pdf` → `pdftoppm` 逐页目检 → `make images` → `make video` 出 mp4；
6. 全程遵守第七节陷阱表；引语仅限 page.md 载有英文原文者（如 "I was slighting the family member who would undergo the most profound change over the long run – the wife and mother. I neglected her because the sources had." 引原文+译文），无原文不得造「原话」。
