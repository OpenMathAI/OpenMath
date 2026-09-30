# 经济学家立传提示词（Simon Kuznets）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1971 年得主 Simon Kuznets（西蒙·库兹涅茨）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Simon_Kuznets/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Simon Smith Kuznets（1901-04-30 生于俄国平斯克（今白俄罗斯） ~ 1985-07-08 逝于马萨诸塞州剑桥，享年 84 岁）
- **气质关键词**：**GDP 之父、国民收入核算体系的总工程师、实证增长理论的开山者**
- **诺奖获奖理由**（1971 独得，逐字引用 manifest）：
  > "for his empirically founded interpretation of economic growth which has led to new and deepened insight into the economic and social structure and process of development"（表彰他对经济增长的实证性阐释，使人们对经济与社会结构及发展过程有了更新、更深的认识）
- **设计母题**：**核算与增长曲线（accounting & curves）**——把一国全部生产装进一张账户表格、用长期序列画出增长与不平等的倒 U 曲线；视觉上以「账目表格 + 倒 U 曲线」的叠加意象构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Simon_Kuznets/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Simon_Kuznets/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Simon_Kuznets_zh`、`VIDEO_NAME=Simon_Kuznets_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Kuznets 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | economic growth | 经济增长 | 14 国 60 年实证增长研究，1971 诺奖核心 | 封面、核心页 |
| 1 | national income accounting | 国民收入核算 | 首次官方估算美国国民收入；现代国民账户体系基础 | 核心页 |
| 2 | development economics | 发展经济学 | 反"线性阶段"论，开创后发国家独立研究路径 | 发展页 |
| 3 | econometrics | 计量经济学 | 推动经济学成为实证科学、量化经济史 | 方法页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Wesley Clair Mitchell | 师→生 | 哥伦比亚大学求学指导者；1931 受其嘱托主持 NBER 国民收入核算 |
| advisor-student | Baidyanath Misra | Kuznets→学生 | infobox Doctoral students 明载 |
| advisor-student | Milton Friedman | Kuznets→学生 | infobox Doctoral students 明载；1976 经济学诺奖得主 |
| advisor-student | Richard Easterlin | Kuznets→学生 | infobox Doctoral students 明载 |
| advisor-student | Stanley Engerman | Kuznets→学生 | infobox Doctoral students 明载 |
| advisor-student | Robert Fogel | Kuznets→学生 | infobox Doctoral students 明载；1993 经济学诺奖得主 |
| advisor-student | Subramanian Swamy | Kuznets→学生 | infobox Doctoral students 明载 |
| advisor-student | Lance Taylor | Kuznets→学生 | infobox Doctoral students 明载 |
| influence | Joseph Schumpeter | 单向 | 正文明载 "was influenced by the work of"（创新与经济周期理论） |
| influence | A. C. Pigou | 单向 | 正文明载（市场失灵研究） |
| influence | Vilfredo Pareto | 单向 | 正文明载（收入分配法则） |

**不入库但提示词可叙述**：妻子与子女 page.md 无载（禁写）；哈尔科夫商学院授课诸教授（Fomin/Antsiferov/Levitsky/S. Bernstein/Davats 等——仅课程教导非博士导师关系）；1920s 评述并翻译 Kondratiev/Slutsky/Pervushin/Weinstein 论文（文献译介非个人关系）；Mitchell 嘱托主持核算（已含于导师行 note）；两个弟弟 Solomon 与 George（仅具名）。

## 五、配色方案 【人物专属】

- **气质**：账房的严谨与史家的纵深、移民学者的踏实
- **主色**：`#0E4D64`（账簿蓝绿——国民账户表格的冷青与长期序列的深水感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGrowth` 增长理论 — 深青 `#0E4D64`
  - `badgeAccount` 国民核算 — 靛蓝 `#16324F`
  - `badgeDev` 发展经济 — 琥珀 `#C07A2A`
  - `badgeCurve` 库兹涅茨曲线 — 深红 `#7E1E23`
- **背景母题**：账目表格与倒 U 曲线叠加——1934 年第一份官方国民收入估算与 1955 年倒 U 假说的视觉合体。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — GDP 之父 / Simon Kuznets 1901–1985 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生于平斯克、哈尔科夫商学院→哥伦比亚
    BS 1923/MA 1924/PhD 1926、导师 Mitchell、NBER/Penn/JHU/Harvard 任职线、诺奖 1971）
03  核心贡献概览 — 国民收入核算 / 库兹涅茨周期 / 库兹涅茨曲线 / 增长结构转型
04  平斯克与哈尔科夫 (1901–1922) — 犹太家庭；战时劳资统计处首篇论文（1920 哈尔科夫工资动态）
05  移民与哥伦比亚 (1922–1926) — Mitchell 门下；硕士论文《舒umpeter 经济体系》；博士论文 1930 成书
06  NBER 岁月与国民收入核算（核心贡献页）— 1931 受 Mitchell 嘱托主持；1934 首份 1929-32 官方估算；
    "国民福祉难以从国民收入推得"的自我警句
07  库兹涅茨周期 (1930s) — 15-25 年"长摆动"，介于康德拉季耶夫长波与短周期之间
08  推翻凯恩斯消费假说 (1942) — 长期储蓄率恒定，为 Friedman 永久收入假说铺路
09  库兹涅茨曲线 (1955/1963)（核心贡献页）— 增长与不平等的倒 U 假说
10  现代经济增长 (1966) — 四要素增长研究纲领；结构转型是增长的本质
11  发展经济学的分水岭 — 后发国家≠先发国家的重演；"线性阶段"观的终结
12  战时与战后咨询 — 战时生产局副主任；中/日/印/韩/台/以色列核算体系顾问
13  荣誉与传承 — AEA 主席 1954、ASA 主席 1949、Walker 奖章 1977；Friedman/Fogel 诺奖学生；
    2013 哈尔科夫经济大学冠名
14  遗产与结尾 — GDP 的缔造者与它的首位批评者 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 卒日两说 | frontmatter date_of_death 双值 ["1985-07-08","1985-07-09"]；**取正文 1985-07-08**（infobox 与正文一致；Fogel 2000 NBER 论文标题作 July 9——页内异说注存疑，正文优先） |
| 国籍口径 | yaml 按 Nobel 口径仅 **United States**；frontmatter 有 Russian Empire；正文口径 "Russian-born American economist"（生于平斯克，今白俄罗斯） |
| GDP 谨慎表述 | "pioneered the concept of gross domestic product"——首创/开拓概念，勿写成"发明 GDP"或"设计 SNA 全体系"；且他本人**反对**把国民收入当福祉指标（"the welfare of a nation can scarcely be inferred from a measure of national income"） |
| 非首位尝试者 | page.md 明言 "Although Kuznets was not the first economist to try this, his work was so comprehensive..."——国民收入核算**并非他首创**，是全面性与系统性树立标准；勿写"第一个核算国民收入的人" |
| 哈尔科夫教授们 | Fomin/Antsiferov/Levitsky/Bernstein/Davats 等仅是授课者（且信息源于"学院课程"叙述），不建 advisor-student；真正的博士导师只有 Mitchell |
| Schumpeter 影响 | 影响发生地是**哈尔科夫**求学时期（接触其创新与周期理论），后有硕士论文《舒umpeter 经济体系》——注意与哥伦比亚 Mitchell 门下的时段区分 |
| 康德拉季耶夫关联 | 评述/翻译 Kondratiev 等人是文献工作；"Kuznets cycles" 是独立于"长波"的 15-25 年周期，勿混同 |
| 学生名单 | 7 位学生全收（infobox Doctoral students 明载）；Friedman/Fogel 为诺奖得主；Lance Taylor 勿与本批 Hicks/其他 Taylor 混淆 |
| 任职时间轴 | NBER 1927-1961；Penn 兼职 1931-36→全职 1936-1954；JHU 1954-1960；Harvard 1960/1961-1970 退休——正文明载 "From 1961 until his retirement in 1970" 与 infobox "(1960–1971)" 有约一年出入，按正文 1961 叙述、infobox 数字另注 |
| 二战角色 | 1942-1944 战时生产局规划与统计局副局长；用国民核算+线性规划雏形评估军工扩张潜力——叙述按 page.md |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| national income | 国民收入 | 核算对象；与 GDP/GNP 层次区分 |
| gross domestic product | 国内生产总值 | "pioneered the concept"措辞 |
| Kuznets cycle | 库兹涅茨周期 | 15-25 年长摆动，勿与康氏长波混淆 |
| Kuznets curve | 库兹涅茨曲线 | 增长-不平等倒 U 假说（1955/1963） |
| structural transformation | 结构转型 | 现代经济增长的核心命题 |
| permanent income hypothesis | 永久收入假说 | Friedman 假说，其铺垫者是 Kuznets 的长期储蓄发现 |
| absolute income hypothesis | 绝对收入假说 | 凯恩斯 1936 假说，被其 1942 数据动摇 |
| linear programming | 线性规划 | 战时军工潜力评估的"粗糙形式" |
| NBER | 美国国家经济研究局 | 1927-1961 的研究基地 |
| secular movements | 长期运动 | 1930 博士成书主题 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**："过去"对应 Kuznets 的历史纵深——用 60 年的长期序列回望 14 国增长史，把经济史变成可核算的数据；曲目的深沉历史感贴合"量化经济史"开创者的底色。
- **本地路径**：复制 `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` 到 `economics/presentations/20th_century/Simon_Kuznets/PAST.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
