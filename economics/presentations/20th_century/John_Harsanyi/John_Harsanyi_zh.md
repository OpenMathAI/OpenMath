# 经济学家立传提示词（John Harsanyi）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1994 年得主 John Harsanyi（约翰·海萨尼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/John_Harsanyi/page.md`，与其冲突时以 page.md 为准（同目录 metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：John Charles Harsanyi（匈牙利语 Harsányi János Károly，1920-05-29 生于布达佩斯 ~ 2000-08-09 逝于加州伯克利，享年 80 岁）
- **气质关键词**：**不完全信息博弈的破解者、贝叶斯博弈之父、规则功利主义者**
- **诺奖获奖理由**（1994，与 John Nash、Reinhard Selten 三人共享，manifest citation 逐字）：
  > "for their pioneering analysis of equilibria in the theory of non-cooperative games"（表彰他们在非合作博弈理论中关于均衡的开创性分析）
- **设计母题**：**幕布与概率（veil & probability）**——不完全信息的本质是「参与者只知概率分布、不知对手真实类型」：以半透明幕布、分层的雾面圆盘与概率树构成背景母题，呼应「自然(Nature)先手抽取类型」的贝叶斯框架。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/John_Harsanyi/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

- **关键时间线（事实基准，取自 page.md）**：
  - 1920-05-29 生于布达佩斯（奥匈解体后的匈牙利王国），父 Károly Harsányi 药房业主，母 Alice（née Gombos）
  - 1939 赴法国里昂大学注册化学工程（父命），因二战爆发中断
  - 1944 布达佩斯大学药理学文凭；同年被征入强制劳役队（东线），七个月后逃亡，获耶稣会房子庇护至战末
  - 1947 布达佩斯大学哲学+社会学双 PhD；任教社会学研究所，结识 Anne Klauber
  - 1948 因公开反马克思主义观点被迫辞职；两年内试图出售家中药房
  - 1950-12-30 与 Anne 及其父母非法越境入奥地利，转赴澳大利亚
  - 1951-01-02 悉尼结婚；白天工厂做工，夜校悉尼大学经济学
  - 1953 悉尼大学 M.A.；1953/1955 在 JPE 发表基数效用两文
  - 1954 昆士兰大学教职（Brisbane）
  - 1956 Rockefeller 奖学金赴斯坦福（师从 Kenneth Arrow）；一学期 Cowles Foundation
  - 1959 斯坦福经济学 PhD（博弈论论文）；返澳（学生签证到期）
  - 1961–1963 Wayne State University（Detroit）经济学教授
  - 1964 起 University of California, Berkeley，直至 1990 退休；到任不久子 Tom 出生
  - 1966–1968 美国载军署博弈论顾问团队（与 Princeton 的 Mathematica 合作）
  - 1967–1968 《Games with incomplete information played by "Bayesian" players》I–III（Management Science）
  - 1988 与 Selten 合著《A General Theory of Equilibrium Selection in Games》（MIT Press）
  - 1994 诺贝尔经济学奖（与 Nash、Selten 共享）
  - 2000-08-09 逝于伯克利（心脏病发作；此前患阿尔茨海默病）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/John_Harsanyi/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=John_Harsanyi_zh`、`VIDEO_NAME=John_Harsanyi_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

### 流程要点细化

- **第 0 步**：事实基准已在本文第一、七节固化（page.md 已核对），直接使用，勿再凭记忆改写；
- **第 1 步**：目录 `economics/presentations/20th_century/John_Harsanyi/` 已存在（本提示词所在），只需建 `images/`；
- **第 2 步**：Makefile 从同世纪已完成篇目复制，仅改 `MAIN`/`VIDEO_NAME` 两行；
- **第 3 步**：本页 infobox 图像栏为空，肖像按第十一节第 2 条降级链处理；
- **第 4/4.5 步**：已入库（见第三节 rank 表与第四节关系表），立传 agent 只读不写库；
- **第 5-9 步**：配色、幻灯片序列、编写、布局检查、史实审查按本文第五、六、七、十一、十二节执行，每写一页就编译一次。

## 三、研究领域梳理 + 入库 【人物专属】

**Harsanyi 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | game theory | 博弈论 | 1994 诺奖核心：非合作博弈均衡分析 | 封面、核心页 |
| 1 | Bayesian games | 贝叶斯博弈 | 不完全信息博弈的标准框架（1967-68 三部曲） | 核心页 |
| 2 | equilibrium selection | 均衡选择 | 与 Selten 合著《A General Theory of Equilibrium Selection in Games》(1988) | 合作页 |
| 3 | utilitarian ethics | 功利主义伦理 | 规则功利主义代表人物；政治与道德哲学中的博弈论应用 | 伦理页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Kenneth Arrow | Arrow → 导师 | 斯坦福博士导师，1959 第二个经济学 PhD（Rockefeller 奖学金赴美） |
| spouse | Anne Klauber | 无向 | 布达佩斯社会学研究所同事，1951-01-02 抵澳后结婚 |
| co-honored | Reinhard Selten | 无向 | 1994 经济学奖共享（非合作博弈均衡开创性分析） |
| co-honored | John Forbes Nash | 无向 | 1994 经济学奖共享（非合作博弈均衡开创性分析） |
| influence | John Forbes Nash | 无向 | 赴美后受 Nash 博弈论论文影响，兴趣日增 |
| colleague | Reinhard Selten | 无向 | 1988 合著《A General Theory of Equilibrium Selection in Games》 |
| colleague | Harold W. Kuhn | 无向 | 1966-68 美国载军署顾问团队（Mathematica）合作，早期鼓励其博弈论研究 |
| colleague | Oskar Morgenstern | 无向 | 1966-68 载军署顾问团队，与 Kuhn 共同领衔 Princeton Mathematica 小组 |

**不入库但提示词可叙述**：James Tobin（与 Arrow 共同帮助其赴美任教，一次性帮助非持续关系）；子 Tom（仅具名）；《The Martians》群体归属（György Marx 的说法）；Adam Smith / Kant / Bentham 等仅为其论文中调和的思想传统，无直接关系记载。

## 五、配色方案 【人物专属】

- **气质**：深邃、缜密、从战火中走出的理性主义者
- **主色**：`#1E3A5F`（manifest 预分配，深海蓝——理性与概率的冷静感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGame` 博弈论 — 深海蓝 `#1E3A5F`
  - `badgeBayes` 贝叶斯博弈 — 青绿 `#0E7C7B`
  - `badgeUtil` 功利主义伦理 — 琥珀 `#C07A2A`
  - `badgeLife` 流亡与新生 — 玫瑰 `#C4204F`
- **背景母题**：半透明幕布与概率树（雾面圆盘错落），呼应「参与者只知先验概率」的不完全信息世界。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 不完全信息博弈的破解者 / John Harsanyi 1920–2000 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、布达佩斯出生、教育里昂/布达佩斯/悉尼/斯坦福、
    任职 Berkeley 1964–1990、诺奖 1994、核心领域）
03  核心贡献概览 — 贝叶斯博弈 / 均衡选择 / 规则功利主义 / 政治与道德哲学中的博弈论
04  布达佩斯少年 (1920–1939) — 犹太家庭改宗天主教、Lutheran Gymnasium、KöMaL 解题高手、Eötvös 竞赛首奖
05  战火中的求学 (1939–1947) — 父命里昂学化工；战起回国改读药理学 1944 文凭；强制劳役、逃亡、耶稣会庇护
06  哲学博士与体制挤压 (1947–1950) — 布达佩斯哲学/社会学双博士 1947；因反马克思主义观点被迫辞职；1950 出走
07  澳大利亚：白天工厂夜晚经济学 (1950–1956) — 悉尼 M.A. 1953；昆士兰执教 1954；经济学论文开始发表
08  斯坦福：Arrow 门下 (1956–1959) — Rockefeller 奖学金；第二个经济学 PhD；Anne 获心理学 MA
09  赴美定居与 Berkeley 岁月 (1961–1990) — Wayne State 1961–63；1964 起 Berkeley 直至 1990 退休
10  贝叶斯博弈：把「不知」变成「概率」（核心贡献页）— 1967-68 三部曲；自然先手抽取类型；共同先验（Harsanyi Doctrine）
11  均衡选择：与 Selten 的合著 (1988) — A General Theory of Equilibrium Selection in Games
12  规则功利主义 — 调和 Smith、Kant 与功利主义者（Bentham/Mill/Sidgwick/Edgeworth）三大传统
13  荣誉与晚年 — Nobel 1994、John von Neumann Award、人大/卡昂荣誉博士；2000-08-09 逝于伯克利
14  遗产与结尾 — 信息经济学与机制设计的地基之一 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 三人共享 | 1994 与 **John Nash、Reinhard Selten** 三人共享；citation 是三人同句「their pioneering analysis」；勿写成两人或独得 |
| Nash 姓名规范 | 对手方用库内规范名 **John Forbes Nash**（id=967，Albert W. Tucker 门生记录）；库内另有 'John Nash'(429) 系他人，勿误挂 |
| 两个 PhD | 第一个 PhD 是布达佩斯 **哲学+社会学**（1947）；第二个才是斯坦福经济学 PhD（1959，Arrow 指导）；勿混为"经济学博士一枚" |
| 早年专业 | 父亲送他去里昂学的是 **化学工程**（1939，因二战中断）；回国读的是 **药理学**（1944 文凭）——均非经济学 |
| Arrow Cross 表述 | 1944 被征入强制劳役队、后逃亡获耶稣会庇护——按 page.md 客观转述即可，集中营遣返只说"德方决定将队伍遣送奥地利集中营"，不展开 |
| 妻子姓氏 | 妻 Anne Klauber（婚后 Anne Harsanyi）；1951-01-02 在悉尼结婚；page.md 明载婚礼轶事（她承诺把饭做得更好吃）可作花絮 |
| Harsanyi Doctrine | 「共同先验」假设的名称是后人对 1967-68 框架的概括，行文用"被称为/即所谓"，勿写成他本人自命 |
| 离职原因 | 1948 因公开表达反马克思主义观点被迫辞去社会学研究所教职——按 page.md 客观转述，不评价 |
| 卒因双要素 | 2000-08-09 逝于伯克利，page.md 载心脏病发作 + 此前已患阿尔茨海默病，两者并列勿只取其一 |
| 获奖工作年份 | 获奖工作是 **1967-1968** 年发表的系列论文（Management Science 三部曲），勿与 1953/1955 早期功利主义论文混淆 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Bayesian game | 贝叶斯博弈 | 不完全信息博弈的标准模型，勿译"贝叶斯对局" |
| incomplete information | 不完全信息 | 与 imperfect information（不完美信息）严格区分 |
| common priors | 共同先验 | Harsanyi Doctrine 的核心假设 |
| equilibrium selection | 均衡选择 | 与 Selten 合著主题 |
| rule utilitarianism | 规则功利主义 | 区别于行为功利主义（act utilitarianism） |
| utility | 效用 | 经济学定译，勿译"功利" |
| Cardinal utility | 基数效用 | 1953/1955 早期论文主题 |
| utilitarian ethics | 功利主义伦理 | 诺奖之外的第二身份 |
| natural moves | 自然的先手行动 | 贝叶斯框架中 Nature 抽取类型 |
| The Martians | 火星人（科学家群体绰号） | 指匈牙利裔杰出科学家群体，行文加引号 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/23-GiwYLGgJw7w-... Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav`）
- **匹配理由**：「探路者」贴合其在无人区开辟不完全信息博弈框架的一生——从布达佩斯战火到悉尼工厂夜校再到 Berkeley 讲席，步步都是开路；录制地 Budapest 与其出生地暗合。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `economics/presentations/20th_century/John_Harsanyi/Pathfinder.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/John_Harsanyi/page.md` | ★ 事实基准（唯一事实来源） |
| `economics/presentations/pages/20th_century/John_Harsanyi/metadata.json` | QID/生卒/国籍结构化参考（与正文冲突以 page.md 为准） |
| `economics/presentations/pages/20th_century/John_Harsanyi/images.txt` | 肖像候选 URL |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照（身份信息页/配色宏/页序列） |
| `economics/presentations/cover/` | OpenEcon 共享封面（`\input` 统一首页） |
| `MySQL/data/John_Harsanyi.yaml` | 本人物入库 yaml（fields/relations 与本文第三、四节一致） |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册（入库命令、note 引号规则、对手方规范名） |

## 十一、执行清单与验收标准 【模板通用】

1. 复制同世纪已完成篇目 Makefile，改 `MAIN=John_Harsanyi_zh`、`VIDEO_NAME=John_Harsanyi_zh`。
2. 下载肖像（images.txt 有 URL 直接用；无则 Commons `Special:FilePath/<File>?width=600`，404 则装饰圆占位；本页 page.md infobox 图像栏为空，优先 REST API 查 infobox 实际文件名，再 404 装饰圆占位）。
3. 配色宏按第五节：`mainclr=#1E3A5F`，badgeA-D 四色照抄；宏名统一 `mainclr/accentclr/badgeA..D`，注释写语义。
4. 幻灯片序列按第六节 15 页规划逐页实现；身份信息页（02）必做。
5. 编译循环：`make distclean && make`（latexmk 多遍），0 error；溢出指标 vbox ≤ 10pt / hbox ≤ 50pt。
6. `pdftoppm` 逐页目检，修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。
7. 全篇事实回查：每条陈述可溯源到 page.md；引语只允许 page.md 英文原文（本篇无直接引语，全部转述）。
8. 品牌口径：结尾页底部写 `OpenMathAI`；引号用半角 `" "`；中文引号内不得出现自称"原话"。
9. 验收：pdfinfo 页数 = 规划页数；BGM wav 已复制到本目录。

## 十二、版式补遗（Beamer 实现要点） 【模板通用】

- 时间线 `\foreach` 分隔符必须 ASCII 逗号（中文逗号会吞条目）。
- 表格页安全负间距：顶部 -0.35cm、`arraystretch` 0.78-0.82；公式框前 -0.35 ~ -0.55cm。
- 文本模式希腊字母必须进数学模式；带圈数字需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`。
- `remember picture` 需两遍编译；取日志单遍 xelatex 后必须重新 `make pdf`。
- `\newcommand` 宏名禁数字；概率树/幕布母题用 tikz 半透明圆盘（opacity 0.12-0.2）避免喧宾夺主。

