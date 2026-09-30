# 经济学家立传提示词（Robert Fogel）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1993 年得主 Robert W. Fogel（罗伯特·福格尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Robert_Fogel/page.md`，与其冲突时以 page.md 为准（同目录 metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：Robert William Fogel（1926-07-01 生于纽约市 ~ 2013-06-11 逝于伊利诺伊州奥克朗，享年 86 岁；frontmatter 生年有 1926/1927 两说，以正文 1926-07-01 为准）
- **气质关键词**：**计量史学旗手、奴隶制经济学的挑战者、生理与历史之间的桥接者**
- **诺奖获奖理由**（1993，与 Douglass North 共享，manifest citation 逐字）：
  > "for having renewed research in economic history by applying economic theory and quantitative methods in order to explain economic and institutional change"（表彰他们运用经济理论与量化方法重新开展经济史研究，以解释经济与制度变迁）
- **设计母题**：**数字与铁轨（numbers & rails）**——福格尔的成名作是用反事实法给铁路「算账」：以铁轨延伸线、计数刻度与身高曲线（technophysio evolution 的健康代理指标）构成背景母题，呼应「用数据重审历史结论」的方法论。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Robert_Fogel/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）
- **一句话画像**：敖德萨犹太移民之子，康奈尔历史系出身、青年时期做过八年职业组织者后自认共产主义「不科学」而转向学术；从哥伦比亚到约翰·霍普金斯师承库兹涅茨；用反事实计算证明铁路并非不可或缺、用 plantation 记录重估奴隶制经济；芝加哥人口经济学中心（CPE）创始主任。

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Robert_Fogel/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Robert_Fogel_zh`、`VIDEO_NAME=Robert_Fogel_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。
> 布局检查照模板第 8 步：每写完一页 `make distclean && make`，`pdftoppm` 截图逐页目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

## 三、研究领域梳理 + 入库 【人物专属】

**Fogel 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | economic history | 经济史 | 1993 诺奖核心：经济理论与量化方法重振经济史研究 | 封面、核心页 |
| 1 | cliometrics | 计量史学 | 最著名的倡导者；反事实计算法（《Railroads》1964） | 方法页 |
| 2 | demography | 人口学 | 人口经济学中心（CPE）创始主任；联邦军队老兵 3.5 万样本项目 | 人口页 |
| 3 | nutrition | 营养与健康史 | technophysio evolution；身高作健康代理；诺奖演讲主题 | 晚年页 |
| 4 | slavery economics | 奴隶制经济学 | 《Time on the Cross》(1974) 的量化重估与《Without Consent or Contract》(1989) 的道德控诉 | 争议页 |

补充说明（供立传 agent 取材）：代表作谱系——《The Union Pacific Railroad: A Case in Premature Enterprise》(1960)；《Railroads and American Economic Growth: Essays in Econometric History》(1964)（社会储蓄约 2.7% 的 1890 GNP）；《Time on the Cross》两卷 (1974，与 Engerman)；《Which Road to the Past?》(1983)；《Without Consent or Contract》(1989)；《The Fourth Great Awakening》(2000)（四次大觉醒的「Fogel Paradigm」）；《The Escape from Hunger and Premature Death, 1700-2100》(2004)；《The Changing Body》(2011)；《Political Arithmetic: Simon Kuznets and the Empirical Tradition in Economics》(2013，遗著，与妻 Enid 等)。奖项：Bancroft Prize 1975；院士：AAAS 1972、NAS 1973、American Philosophical Society 2000。

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Douglass North | 无向 | 1993 经济学奖共享（运用经济理论与量化方法重振经济史研究以解释经济与制度变迁） |
| advisor-student | Simon Kuznets | Kuznets → 导师 | 约翰·霍普金斯博士导师（1963 PhD；infobox Doctoral advisor 与正文一致） |
| advisor-student | George Stigler | Stigler → 导师 | 哥伦比亚硕士导师（1960 MA，正文明载 studied under；infobox Other advisors 同载） |
| influence | Evsey Domar | 无向 | 约翰·霍普金斯求学跟随（infobox Other advisors + 正文 studied with） |
| influence | Abba Lerner | 无向 | 约翰·霍普金斯求学跟随（infobox Other advisors + 正文 studied with） |
| influence | Fritz Machlup | 无向 | 约翰·霍普金斯求学跟随（infobox Other advisors + 正文 studied with） |
| collaborator | Stanley Engerman | 无向 | 合著《Time on the Cross》(1974)——其最著名也最具争议的著作 |
| colleague | Deirdre McCloskey | 无向 | 芝加哥同事与其门下受教者；McCloskey 称福格尔「重新统一了经济学与历史」 |
| spouse | Enid Cassandra Morgan | 无向 | 1949 结婚（非裔美国人，反混婚法年代的跨种族婚姻）；育二子；遗著合著者 |
| influence | Thomas McKeown | 无向 | McKeown 论题（营养改善驱动死亡率下降）深刻影响其晚年工作 |

**不入库但提示词可叙述**：兄长（长六岁，青年时期主要智识影响者，仅叙述无具名）；二子（仅具名不出）；T. C. Liu（正文 studied with 但不在 infobox Other advisors，且无其他关系叙述）；Eugene Genovese / George Rawick（青年组织者时期批准开除的未来奴隶史家——一次性事件非关系）；Ulrich Phillips（《Time on the Cross》所反驳的旧共识设定者，文献对手非私人关系）；Angus Deaton（引其《The Great Escape》段落作学理概括，仅引用）；Roderick Floud / Bernard Harris / Sok Chul Hong（《The Changing Body》合著者，文献列表合作无正文叙述）。

## 五、配色方案 【人物专属】

- **气质**：严谨、计算感、直面争议的冷静
- **主色**：`#175E54`（manifest 未预分配，本批自选，墨绿青——计量史学的算尺青与人口数据的沉稳；已向主控报备）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeClio` 计量史学 — 墨绿青 `#175E54`
  - `badgeRail` 反事实与铁路 — 深海蓝 `#1E3A5F`
  - `badgeSlav` 奴隶制经济学 — 深绛红 `#7E1E23`
  - `badgePhysio` 生理与营养史 — 琥珀 `#C07A2A`
- **背景母题**：铁轨延伸线与身高曲线（计数刻度点缀），呼应「用数据重审历史结论」与 technophysio evolution。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex，品牌口径 OpenMathAI）
01  封面 — 给历史算账的人 / Robert W. Fogel 1926–2013 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒（1926-07-01 NYC ~ 2013-06-11 Oak Lawn, IL，享年 86）、
    教育（Cornell BA 1948 历史 / Columbia MA 1960 / Johns Hopkins PhD 1963）、
    任职（Rochester 1960-64 → Chicago 1964-75 → Harvard 1975-81 → Chicago 1981-，
    Walgreen 讲席与 CPE 主任）、诺奖 1993
03  核心贡献概览 — 计量史学 / 反事实与铁路 / 奴隶制重估 / 生理经济学（四 badge 横排）
04  移民之子与青年岁月 (1926–1948) — 敖德萨犹太移民家庭；Stuyvesant 高中 1944；
    康奈尔历史系，American Youth for Democracy 校园支部主席
05  转向 (1948–1960) — 八年职业组织者岁月；自认共产主义「不科学」而弃；
    哥伦比亚师从 Stigler 1960 MA；对 1940 年代末经济的悲观让他转向经济学
06  约翰·霍普金斯与库兹涅茨 (1960–1963) — Kuznets 门下 1963 PhD；
    Domar/Lerner/Machlup/Liu 群体环绕
07  反事实与铁路 (1964)（核心贡献页）— 《Railroads and American Economic Growth》：
    假想 1890 年无铁路的美国，「社会储蓄」约 2.7% GNP——铁路并非不可或缺
08  时间之犁 (1974)（核心贡献页）— 与 Engerman 合著《Time on the Cross》：
    奴隶制对奴隶主是盈利的（规模经济）、南方种植园若无内战不会自行消亡；
    掀起轩然大波
09  争议与澄清 — 「有人误认福格尔为奴隶制辩护」：正文明载他基于道德反对奴隶制、
    仅在经济判断上认为奴隶制并非不盈利；批评与误读的两分
10  道德控诉 (1989) — 《Without Consent or Contract》：高婴儿死亡率、残酷的奴隶层级、
    福音派废墟上的道德反抗——从计算到控诉的自答
11  芝加哥与人口经济学 (1981–2013) — 创立 CPE；NIH 资助的 3.5 万联邦军老兵项目；
    Walgreen 讲席；Bancroft Prize 1975；AAAS/NAS/APS 院士
12  生理演化与大觉醒 — technophysio evolution（技术变革与人体生理的协同）；
    身高作健康代理；《The Fourth Great Awakening》与「Fogel Paradigm」（他称的由他人命名）
13  诺奖与遗产 — 1993 与 North 共享（同句理由）；诺奖演讲论营养与经济增长；
    McCloskey 的评价：重新统一经济学与历史；门生谱系遍布美国经济史学界
14  遗著与结尾 — 《Political Arithmetic: Simon Kuznets and the Empirical Tradition in Economics》(2013)
    致敬导师收束一生 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生年两说 | frontmatter date_of_birth 有 ["1926-07-01","1927-07-01"] 双值，以**正文 1926-07-01** 为准（yaml 填 1926-07-01）；享年 86 |
| 共享奖口径 | 1993 与 **Douglass North** 共享、同一句理由（manifest citation 逐字）；两篇立传用同一口径，co-honored 双向幂等 |
| 博士导师双值 | frontmatter doctoral_advisor 有 Kuznets 与 George Heberton Evans 两值；infobox/正文只载 **Kuznets**——入库用 Kuznets，Evans 不入库（陷阱表注明） |
| 奴隶制叙述红线 | 《Time on the Cross》论点须完整三层呈现：盈利结论 + 奴隶仍受剥削且「记录未捕捉的剥削方式」作者明言 + 引发轩然大波；**必须**写明正文的澄清——福格尔基于道德反对奴隶制，被误读为辩护者；勿单侧呈现 |
| 共产主义经历 | 康奈尔参加 American Youth for Democracy（共产党组织）、毕业后八年职业组织者、批准开除 Genovese/Rawick——正文明载，客观叙述不评价；「rejected communism as unscientific」为原文口径 |
| 反事实法 | 「social savings」约 2.7% 的 1890 GNP——数字与年份绑定，勿写成别的年份；结论是「铁路并非不可或缺」而非「铁路不重要」 |
| Fogel Paradigm | 四次大觉醒周期 diagram「called (by others) 'The Fogel Paradigm'」——命名出自他人非自称 |
| McKeown 论题 | 福格尔工作「largely influenced by the McKeown thesis」（Thomas McKeown，1955 起的营养-死亡率理论）——influence 边的依据；Deaton 引文只作概括呈现 |
| McCloskey 定位 | 正文明载福格尔「mentored」McCloskey、McCloskey 是其 Chicago 同事且为之「reuniting economics and history」正明载——colleague 边成立，勿写成师生入库 |
| 跨种族婚姻 | 1949 年与 Enid Cassandra Morgan 结婚，反混婚法与偏见年代「面临重大困难」——客观叙述，时代背景一笔 |
| metadata 噪声 | metadata.json 职业含 political economist 等，以 infobox+正文为准（economist / economic historian）；国籍 United States |
| 引语红线 | Deaton 段落（"Nutrition was clearly part of the story..."）与 McCloskey 短语为 page.md 英文原文可引；中文引号内不得出现无原文支撑的「原话」 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cliometrics | 计量史学 | 史上最著名倡导者；与 North 共同推广，勿写成一人在 1960 年代独创 |
| counterfactual | 反事实分析 | 「假想无铁路的 1890」是标准例 |
| social savings | 社会储蓄 | 铁路贡献的度量：约 2.7% of 1890 GNP |
| Time on the Cross | 《时间之犁》 | 1974 两卷；奴隶制盈利结论的核心载体；与 Engerman 合著 |
| Without Consent or Contract | 《不经同意或契约》 | 1989；对奴隶制的道德控诉，回应批评 |
| technophysio evolution | 技术生理演化 | 技术变革与人体生理改善的协同（synergism） |
| economies of scale | 规模经济 | 大奴隶农场单位劳动更高产——盈利论证的机制 |
| Fogel Paradigm | 福格尔范式 | 四次大觉醒周期，命名出自他人 |
| McKeown thesis | 麦基翁论题 | 营养改善驱动死亡率下降；福格尔及合作者提供了证据 |
| Early Indicators project | 早期指标项目 | NIH 资助，3.5 万联邦军老兵军饷记录；CPE 支柱项目 |
| Bancroft Prize | 班克罗夫特奖 | 1975 获得者；与诺奖并列的荣誉节点 |
| abolitionism | 废奴主义 | 《Without Consent or Contract》的主题：福音派改革者推动废除 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Shine Like The Sun**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：与 North 同曲（manifest 预分配如此；同批共享同曲可作「1993 同一理由」的呼应设计，出片阶段撞曲裁定权在主控）——福格尔从政治组织者到计量史学旗手的转变，是把历史拖进阳光下的数据检验；上扬的史诗感对应「用数字与道德双重目光重审奴隶制与经济增长」的一生。
- **本地路径**：复制 `music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav` 到 `economics/presentations/20th_century/Robert_Fogel/ShineLikeTheSun.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
