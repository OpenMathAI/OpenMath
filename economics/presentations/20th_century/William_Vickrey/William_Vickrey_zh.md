# 经济学家立传提示词（William Vickrey）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1996 年得主 William Vickrey（威廉·维克里）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/William_Vickrey/page.md`，与其冲突时以 page.md 为准（同目录 metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：William Spencer Vickrey（1914-06-21 生于加拿大不列颠哥伦比亚维多利亚 ~ 1996-10-11 逝于纽约州哈里森，享年 82 岁）
- **气质关键词**：**拍卖理论的开启者、拥堵定价之父、身后三天的诺奖得主**
- **诺奖获奖理由**（1996，与 James Mirrlees 两人共享，manifest citation 逐字）：
  > "for their fundamental contributions to the economic theory of incentives under asymmetric information"（表彰他们对不对称信息下激励经济理论的基础性贡献）
- **设计母题**：**第二价格与密封投标（second price & sealed bid）**——Vickrey 拍卖的核心是「报真实估值即最优策略」：以密封信封、报价阶梯与拍槌构成背景母题，呼应「机制让真话成为占略」的激励设计。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/William_Vickrey/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

- **关键时间线（事实基准，取自 page.md）**：
  - 1914-06-21 生于不列颠哥伦比亚维多利亚；父 Charles Vernon Vickrey 公理会牧师，母 Ada Eliza Spencer
  - 幼年随家迁纽约；父任美亚救援委员会（Near East Foundation 前身）总干事
  - 中学 Phillips Academy（Andover, MA）
  - 1935 耶鲁数学 BS；1937 哥伦比亚 MA；1948 哥伦比亚 PhD（500 页论文 An Agenda for Progressive Taxation）
  - 二战期间博士中断：先在国家资源计划委员会、后在财政部税务研究司任职
  - 终身执教哥伦比亚大学；学生包括 Jacques Drèze、Harvey J. Levin、Lynn Turgeon
  - 1951 与 Cecile Thompson 结婚；贵格会教徒（Scarsdale Friends Meeting 成员）
  - 1955 获 Guggenheim Fellowship
  - 1961 "Counterspeculation, Auctions, and Competitive Sealed Tenders"——开创拍卖理论、收入等价定理雏形、第二价格拍卖（Vickrey auction）
  - 1963 "Pricing in Urban and Suburban Transport"——拥堵定价
  - 1969 "Congestion Theory and Transport Investment"——拥堵理论模型化
  - 公共经济学：扩展 Harold Hotelling 的边际成本定价；支持土地价值税（Georgist 立场）
  - 战后曾在麦克阿瑟治下协助日本土地改革
  - 1996-10-08 诺贝尔奖公布（经济学奖）——不列颠哥伦比亚出生的唯一诺奖得主
  - 1996-10-11 赴 Georgist 学者会议途中心脏病发去世；哥伦比亚系同事 C. Lowell Harriss 代领追授之奖
  - 诺奖身后追授史上仅四例：Karlfeldt（文学 1931）、Hammarskjöld（和平 1961）、Vickrey（经济学 1996）、Steinman（生理学或医学 2011）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/William_Vickrey/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 取；404 则装饰圆占位）；Makefile 复制后设 `MAIN=William_Vickrey_zh`、`VIDEO_NAME=William_Vickrey_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

### 流程要点细化

- **第 0 步**：事实基准已在本文第一、七节固化（page.md 已核对），直接使用，勿再凭记忆改写；
- **第 1 步**：目录 `economics/presentations/20th_century/William_Vickrey/` 已存在（本提示词所在），只需建 `images/`；
- **第 2 步**：Makefile 从同世纪已完成篇目复制，仅改 `MAIN`/`VIDEO_NAME` 两行；
- **第 3 步**：肖像按 images.txt 降级链处理，404 装饰圆占位；
- **第 4/4.5 步**：已入库（见第三节 rank 表与第四节关系表），立传 agent 只读不写库；
- **第 5-9 步**：配色、幻灯片序列、编写、布局检查、史实审查按本文第五、六、七、十一、十二节执行，每写一页就编译一次。

## 三、研究领域梳理 + 入库 【人物专属】

**Vickrey 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | public economics | 公共经济学 | 终身主业：公共品定价、税制设计 | 封面、核心页 |
| 1 | auction theory | 拍卖理论 | 1961 开山论文；Vickrey 拍卖与收入等价 | 核心页 |
| 2 | mechanism design | 机制设计 | infobox Discipline；激励相容思想源头之一 | 核心页 |
| 3 | optimal taxation | 最优税收 | 1948 博士论文累进税议程；1996 诺奖一翼 | 税制页 |
| 4 | congestion pricing | 拥堵定价 | 道路定价理论，后部分落地伦敦拥堵费 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Carl Shoup | Shoup → 导师 | 哥伦比亚博士导师（infobox 明载） |
| advisor-student | Robert M. Haig | Haig → 导师 | 哥伦比亚博士导师（infobox 明载） |
| influence | Henry George | 无向 | 经济哲学受其影响（infobox Influences + 正文 Georgist 立场） |
| influence | Harold Hotelling | 无向 | 扩展其边际成本定价方法 |
| influence | John Maynard Keynes | 无向 | 经济哲学受其影响（正文明载） |
| advisor-student | Jacques Drèze | Vickrey → 学生 | 学生（infobox+正文并列明载） |
| advisor-student | David Colander | Vickrey → 学生 | 博士生（infobox 明载） |
| advisor-student | Harvey J. Levin | Vickrey → 学生 | 学生（正文明载） |
| advisor-student | Lynn Turgeon | Vickrey → 学生 | 学生（正文明载） |
| co-honored | James Mirrlees | 无向 | 1996 经济学奖共享（不对称信息下激励理论的基础性贡献） |
| colleague | C. Lowell Harriss | 无向 | 哥伦比亚经济系同事；代领追授之奖 |
| colleague | Robert Solow | 无向 | 1971 合著 "Land Use in a Long, Narrow City"（JET） |
| spouse | Cecile Thompson | 无向 | 1951 结婚（page.md 明载） |

**不入库但提示词可叙述**：James Tobin（评语 "an applied economist's theorist, as well as a theorist's applied economist" 是他人评价非关系）；父 Charles Vernon Vickrey / 母 Ada Eliza Spencer（叙述用）；General MacArthur（占领期共事为事件性叙述，不建个人边）。

## 五、配色方案 【人物专属】

- **气质**：务实、正直、为公共定价奔走一生的土地改革者
- **主色**：`#0E4D64`（manifest 预分配，孔雀蓝——与 Mirrlees 同届同色系）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeAuction` 拍卖理论 — 孔雀蓝 `#0E4D64`
  - `badgeCong` 拥堵定价 — 青绿 `#0E7C7B`
  - `badgeTax` 最优税收 — 琥珀 `#C07A2A`
  - `badgeGeo` 亨利·乔治传统 — 玫瑰 `#C4204F`
- **背景母题**：密封信封与报价阶梯（信封开口的金色微光），呼应「第二价格拍卖让真实报价成为均衡」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 拍卖理论的开启者 / William Vickrey 1914–1996 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、维多利亚出生、耶鲁 BS 1935/哥伦比亚 MA 1937/PhD 1948、
    终身执教哥伦比亚、诺奖 1996、核心领域）
03  核心贡献概览 — Vickrey 拍卖 / 收入等价 / 拥堵定价 / 边际成本定价与土地价值税
04  维多利亚出生与纽约成长 (1914–1931) — 公理会牧师之家； Phillips Academy
05  耶鲁数学与哥伦比亚 (1931–1948) — BS 1935 → MA 1937 → 战时税务研究 → 1948 五百页累进税论文
06  1961：拍卖理论的开山之作 — Counterspeculation, Auctions, and Competitive Sealed Tenders；第二价格拍卖
07  收入等价定理 — 现代拍卖理论的中枢（核心贡献页）
08  拥堵定价：让道路说真话 — 1963/1969 论文；伦敦拥堵费的部分落地
09  公共经济学与边际成本定价 — 扩展 Hotelling；公共品按边际成本供给
10  土地价值税与乔治主义立场 — 以地税替代产税的效率与伦理论证；日本土地改革参与
11  批评芝加哥学派 — 反对平衡预算与反通胀优先（高失业时期）的立场，客观转述
12  1996 诺贝尔奖与身后三天 — 10-08 公布、10-11 逝世；Harriss 代领；身后追授四例
13  荣誉与学生 — Guggenheim 1955、Distinguished Fellow；Drèze/Levin/Turgeon 传承
14  遗产与结尾 — 从拍卖到机制设计的现代格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 两人共享 | 1996 与 **James Mirrlees** 两人共享；citation 两人同句 "their fundamental contributions"；勿写成三人 |
| 身后领奖 | 获奖 3 天后（1996-10-11）逝世，**从未亲自领奖**；由同事 C. Lowell Harriss 代领——page.md 明载「身后追授史上仅四例」，行文保留该列举 |
| 国籍口径 | manifest/infobox 双国籍 **Canada / United States**（生于维多利亚、终身美国生涯）；yaml 顺序按 manifest 加拿大在前 |
| Vickrey 拍卖 | 第二价格密封拍卖——「按第二高价成交」的机制设计，勿写成"荷兰式"或"英国式" |
| 收入等价 | page.md 说 1961 论文 "provided an early revenue-equivalence result"——是**早期结果**，定理的完整一般化是后人工作，勿写"证明收入等价定理" |
| 师承双导师 | infobox Doctoral advisor 双值 Carl Shoup + Robert M. Haig——两人并列入库；正文明载博士工作受战时税务研究中断 |
| Georgist 立场 | 土地价值税主张按 page.md 客观转述（效率论证 + 伦理论证两条）；评价性语言不添加 |
| 批评芝加哥学派 | "sharply critical of the Chicago school... vocal in opposing the political focus on balanced budgets and fighting inflation"——客观转述其立场，不站队 |
| Tobin 评语 | James Tobin 评语可引（page.md 载英文原文），但**只作引文框不建关系边** |
| 日土地改革 | "Working under General MacArthur, Vickrey helped accomplish radical land reform in Japan"——客观一句带过，不展开战后史 |
| metadata 噪声 | metadata.json nationality 顺序 United States 在前；yaml 按 manifest 口径 Canada 在前——以 manifest 为准并在本表记录 |
| 妻子入库 | 妻 Cecile Thompson（1951 结婚）page.md 明载，已按纪律入库 spouse |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Vickrey auction | 维克里拍卖 | 第二价格密封拍卖；勿与荷兰/英式混淆 |
| revenue equivalence theorem | 收入等价定理 | 1961 给出早期结果；一般化归后人 |
| sealed-bid auction | 密封投标拍卖 | 与公开喊价对照 |
| congestion pricing | 拥堵定价 | 伦敦拥堵费为其部分落地 |
| marginal cost pricing | 边际成本定价 | 扩展自 Hotelling |
| land value tax | 土地价值税 | Georgist 核心政策主张 |
| Georgism | 乔治主义 | 以亨利·乔治命名的土地改革思想 |
| progressive taxation | 累进税制 | 1948 博士论文主题 |
| mechanism design | 机制设计 | infobox Discipline；当代称谓 |
| posthumous award | 身后追授 | 诺奖史上仅四例 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands**（manifest 预分配，音乐库 `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`）
- **匹配理由**：「新大陆」双关其一生——生于加拿大新大陆、又不断把经济理论推向新领域（拍卖、拥堵定价、土地税）；曲名的开阔与未竟感也暗合「获奖三天后离世」的悲怆弧线。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `economics/presentations/20th_century/William_Vickrey/NewLands.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/William_Vickrey/page.md` | ★ 事实基准（唯一事实来源） |
| `economics/presentations/pages/20th_century/William_Vickrey/metadata.json` | QID/生卒/国籍结构化参考（国籍顺序以 manifest 为准） |
| `economics/presentations/pages/20th_century/William_Vickrey/images.txt` | 肖像候选 URL |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照（身份信息页/配色宏/页序列） |
| `economics/presentations/cover/` | OpenEcon 共享封面（`\input` 统一首页） |
| `MySQL/data/William_Vickrey.yaml` | 本人物入库 yaml（fields/relations 与本文第三、四节一致） |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册（入库命令、note 引号规则、对手方规范名） |

## 十一、执行清单与验收标准 【模板通用】

1. 复制同世纪已完成篇目 Makefile，改 `MAIN=William_Vickrey_zh`、`VIDEO_NAME=William_Vickrey_zh`。
2. 下载肖像（images.txt 有 URL 直接用；无则 Commons `Special:FilePath/<File>?width=600`，404 则装饰圆占位）。
3. 配色宏按第五节：`mainclr=#0E4D64`，badgeA-D 四色照抄；宏名统一 `mainclr/accentclr/badgeA..D`，注释写语义。
4. 幻灯片序列按第六节 15 页规划逐页实现；身份信息页（02）必做。
5. 编译循环：`make distclean && make`（latexmk 多遍），0 error；溢出指标 vbox ≤ 10pt / hbox ≤ 50pt。
6. `pdftoppm` 逐页目检，修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。
7. 全篇事实回查：每条陈述可溯源到 page.md；引语仅 Tobin 评语一句（page.md 载英文原文），其余转述。
8. 品牌口径：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。
9. 验收：pdfinfo 页数 = 规划页数；BGM wav 已复制到本目录。

## 十二、版式补遗（Beamer 实现要点） 【模板通用】

- 时间线 `\foreach` 分隔符必须 ASCII 逗号（中文逗号会吞条目）。
- 表格页安全负间距：顶部 -0.35cm、`arraystretch` 0.78-0.82；公式框前 -0.35 ~ -0.55cm。
- 信封母题用 tikz 矩形+三角折线+金色描边（低透明度底纹），勿与头像争视觉焦点。
- `remember picture` 需两遍编译；取日志单遍 xelatex 后必须重新 `make pdf`。
- `\newcommand` 宏名禁数字；文本模式希腊字母必须进数学模式。
