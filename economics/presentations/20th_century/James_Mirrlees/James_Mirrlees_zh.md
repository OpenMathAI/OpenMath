# 经济学家立传提示词（James Mirrlees）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1996 年得主 James Mirrlees（詹姆斯·莫里斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/James_Mirrlees/page.md`，与其冲突时以 page.md 为准（同目录 metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：Sir James Alexander Mirrlees（1936-07-05 生于苏格兰 Minnigaff ~ 2018-08-29 逝于英格兰剑桥，享年 82 岁；1997 生日荣誉受封爵士）
- **气质关键词**：**最优所得税的设计师、道德 Hazard 原理的阐明者、不对称信息经济学奠基人**
- **诺奖获奖理由**（1996，与 William Vickrey 两人共享，manifest citation 逐字）：
  > "for their fundamental contributions to the economic theory of incentives under asymmetric information"（表彰他们对不对称信息下激励经济理论的基础性贡献）
- **设计母题**：**阶梯与单一交点（single-crossing）**——Spence–Mirrlees 条件的核心是「不同类型者的无差异曲线只相交一次」：以一组只交一次的曲线族、天平与税率阶梯构成背景母题，呼应「用可观察的排序揭示不可观察的类型」。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/James_Mirrlees/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

- **关键时间线（事实基准，取自 page.md）**：
  - 1936-07-05 生于苏格兰 Wigtownshire 的 Minnigaff；中学 Douglas Ewart High School
  - 1957 爱丁堡大学 MA（数学与自然哲学）
  - 1963 剑桥三一学院 PhD（论文 Optimum Planning for a Dynamic Economy，导师 Richard Stone）； Mathematical Tripos 出身
  - 求学期间活跃辩论；同时代人 Quentin Skinner 提及其与 Amartya Sen 同为剑桥使徒社成员
  - 1963–1968 剑桥执教；1968–1995 牛津（Edgeworth 经济学教授 1968–1995）；1995–2018 回剑桥
  - 1968–1976 三度任 MIT 访问教授；1986 UC Berkeley、1989 Yale 访问
  - 1962 与 N. Kaldor 合著 "A New Model of Economic Growth"（RES）
  - 1971 "An Exploration in the Theory of Optimum Income Taxation"（RES）；与 P.A. Diamond 连发最优税收与公共生产 I/II（AER 1971）
  - 1971 Diamond–Mirrlees 效率定理（生产效率）
  - 1996 诺贝尔经济学奖（与 William Vickrey 共享）；1996-12-09 诺奖演讲 Information and Incentives: The Economics of Carrots and Sticks
  - 1997 生日荣誉受封 Knight Bachelor
  - 晚年：剑桥政治经济学荣休教授、三一学院 Fellow；每年数月在墨尔本大学；香港中文大学 Distinguished Professor-at-Large 与晨兴书院创院院长（2009）；澳门大学同职
  - 苏格兰经济顾问委员会成员；主持 IFS 的 Mirrlees Review（英国税制评估，2011 成书 Tax by Design）
  - 2018-08-29 逝于剑桥

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/James_Mirrlees/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 取；404 则装饰圆占位）；Makefile 复制后设 `MAIN=James_Mirrlees_zh`、`VIDEO_NAME=James_Mirrlees_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

### 流程要点细化

- **第 0 步**：事实基准已在本文第一、七节固化（page.md 已核对），直接使用，勿再凭记忆改写；
- **第 1 步**：目录 `economics/presentations/20th_century/James_Mirrlees/` 已存在（本提示词所在），只需建 `images/`；
- **第 2 步**：Makefile 从同世纪已完成篇目复制，仅改 `MAIN`/`VIDEO_NAME` 两行；
- **第 3 步**：肖像按 images.txt 降级链处理，404 装饰圆占位；
- **第 4/4.5 步**：已入库（见第三节 rank 表与第四节关系表），立传 agent 只读不写库；
- **第 5-9 步**：配色、幻灯片序列、编写、布局检查、史实审查按本文第五、六、七、十一、十二节执行，每写一页就编译一次。

## 三、研究领域梳理 + 入库 【人物专属】

**Mirrlees 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | economic theory | 经济理论 | infobox field_of_work；理论经济学家定位 | 封面、核心页 |
| 1 | optimal income taxation | 最优所得税 | 1971 论文确立该领域标准方法 | 核心页 |
| 2 | asymmetric information | 不对称信息 | 1996 诺奖核心：激励理论的信息前提 | 核心页 |
| 3 | moral hazard | 道德风险 | 阐明其原理（Vickrey 书中议题的推进） | 核心页 |
| 4 | development economics | 发展经济学 | 发展中国家项目评估手册（与 Little 合著） | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Richard Stone | Stone → 导师 | 剑桥三一学院博士导师（1963 动态经济最优计划论文） |
| co-honored | William Vickrey | 无向 | 1996 经济学奖共享（不对称信息下激励理论的基础性贡献） |
| colleague | Peter Diamond | 无向 | Diamond–Mirrlees 效率定理（1971）；AER/QJE/Bell 等多篇合著 |
| colleague | Nicholas Kaldor | 无向 | 1962 合著 "A New Model of Economic Growth"（RES） |
| colleague | I.M.D. Little | 无向 | 合著发展中国家项目分析手册（1969）与 Project Appraisal and Planning（1974） |
| colleague | Avinash Dixit | 无向 | 1975 合著 "Optimum Saving with Economies of Scale"（RES） |
| advisor-student | Partha Dasgupta | Mirrlees → 学生 | 博士生（infobox+正文并列明载） |
| advisor-student | Nicholas Stern | Mirrlees → 学生 | 博士生（infobox+正文）；后为勋爵/世行首席经济学家（正文表述） |
| advisor-student | Peter J. Hammond | Mirrlees → 学生 | 博士生（infobox 明载） |
| advisor-student | Franklin Allen | Mirrlees → 学生 | 博士生（infobox+正文） |
| advisor-student | Barry Nalebuff | Mirrlees → 学生 | 博士生（infobox 明载） |
| advisor-student | Geoffrey M. Heal | Mirrlees → 学生 | 博士生（infobox 明载） |
| advisor-student | Huw Dixon | Mirrlees → 学生 | 博士生（infobox+正文） |
| advisor-student | Anthony Venables | Mirrlees → 学生 | 博士生（infobox+正文） |
| advisor-student | John Vickers | Mirrlees → 学生 | 博士生（infobox+正文） |
| advisor-student | Alan Manning | Mirrlees → 学生 | 博士生（infobox 明载） |
| advisor-student | Gareth Myles | Mirrlees → 学生 | 博士生（infobox 明载） |
| advisor-student | Paul Seabright | Mirrlees → 学生 | 博士生（infobox 明载） |
| advisor-student | Hyun-Song Shin | Mirrlees → 学生 | 博士生（infobox+正文） |
| advisor-student | Zhang Weiying | Mirrlees → 学生 | 博士生（infobox+正文，张维迎） |

**不入库但提示词可叙述**：Amartya Sen（Skinner "has suggested" 二人同属剑桥使徒社——转述存疑；且合见于 Sen/Williams 编 Utilitarianism and beyond 文集，非直接合作，不建边）；Quentin Skinner（提供转述的同时代人）；N.H. Stern 合著 "Fairly Good Plans"（与已入库的博士生 Nicholas Stern 为同一人，不重复建边）；P.J. Hammond 合著 "Agreeable Plans"（已以博士生建边）；I.M.D. Little 之外的书目合著者（J.A. Kay、J. Helms 等单次出现不入库）。

## 五、配色方案 【人物专属】

- **气质**：古典、精微、税表背后的数学秩序
- **主色**：`#0E4D64`（manifest 预分配，孔雀蓝——剑桥的深沉与最优控制的精密）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeTax` 最优税收 — 孔雀蓝 `#0E4D64`
  - `badgeInfo` 不对称信息 — 青绿 `#0E7C7B`
  - `badgeMH` 道德风险 — 琥珀 `#C07A2A`
  - `badgeDev` 发展经济学 — 玫瑰 `#C4204F`
- **背景母题**：单一交点曲线族（两三条不同颜色曲线只交一次的抽象）与税率阶梯，呼应 Spence–Mirrlees 条件。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 最优所得税的设计师 / James Mirrlees 1936–2018 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、苏格兰 Minnigaff 出生、爱丁堡 MA 1957/剑桥 PhD 1963、
    任职牛津 Edgeworth 讲席 1968–1995/剑桥、诺奖 1996、核心领域）
03  核心贡献概览 — 最优所得税 / 道德风险 / 不对称信息 / Diamond–Mirrlees 效率定理
04  苏格兰少年与爱丁堡 (1936–1957) — Minnigaff、Douglas Ewart 中学、数学与自然哲学 MA
05  剑桥与 Stone 门下 (1957–1963) — Mathematical Tripos；1963 博士论文 Optimum Planning for a Dynamic Economy
06  早期增长理论 (1962–1967) — 与 Kaldor 合著 1962；技术变迁下的最优增长 1967
07  牛津岁月与最优所得税 (1968–1995) — Edgeworth 讲席；1971 论文确立标准方法
08  道德风险与激励（核心贡献页）— 演示道德风险与最优所得税原理（推进 Vickrey 书中议题）；方法论成为领域标准
09  与 Diamond 的合作 — 效率定理 1971；AER/QJE/Bell 系列合著
10  1996 诺贝尔经济学奖 — 与 Vickrey 共享；演讲 Information and Incentives: The Economics of Carrots and Sticks
11  门生谱系 — Dasgupta、Stern、Vickers、Shin、张维迎等十四人（门生页表格）
12  中国与亚洲足迹 — 香港中文大学 Distinguished Professor-at-Large、晨兴书院创院院长 2009、澳门大学、墨尔本
13  Mirrlees Review 与晚年 — IFS 英国税制评估（Tax by Design 2011）；苏格兰经济顾问委员会
14  遗产与结尾 — 从最优税收到机制设计的现代格局；2018-08-29 逝于剑桥 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 两人共享 | 1996 与 **William Vickrey** 两人共享；citation 两人同句 "their fundamental contributions"；勿写成三人 |
| 学生名单规模 | 正文列举 8 人 + infobox 共 14 人——**全部入库**（infobox 属 page.md 明载）；表格页（第 11 页）14 行需压缩行距防溢出 |
| Vickrey 的角色 | 正文说 Mirrlees "demonstrated the principles of moral hazard and optimal income taxation discussed in the books of William Vickrey"——是**推进/演示 Vickrey 书中议题**，勿写成"师承 Vickrey"或"合作" |
| Diamond 定理年份 | Diamond–Mirrlees 效率定理 page.md 作 **1971 developed**；与 AER 1971 两篇 Optimal Taxation and Public Production 同期，行文统一 1971 |
| 使徒社表述 | "A contemporary, Quentin Skinner, has **suggested** that Mirrlees was a member of the Cambridge Apostles along with... Amartya Sen"——是他人转述且用 suggested，行文保留存疑语气，Sen 不入库 |
| Kaldor 缩写 | 书目作 "N. Kaldor"，入库用规范名 **Nicholas Kaldor**（N. = Nicholas，同剑桥增长理论经济学家） |
| Dixit 缩写 | 书目作 "A.K. Dixit"，入库用规范名 **Avinash Dixit**；勿因缩写另建 stub |
| Edgeworth 讲席 | 牛津 Edgeworth Professor of Economics 1968–1995——是教席名（纪念 F.Y. Edgeworth），**与经济学家 Edgeworth 本人无关系**，勿建边 |
| 中港机构 | 香港中文大学 + 澳门大学同为 Distinguished Professor-at-Large；晨兴书院（Morningside College）**创院院长 2009**——机构任职不建人物边，仅叙述 |
| 爵位 | 1997 Birthday Honours 受封 Knight Bachelor（Sir）；行文首次出现可用 Sir James Mirrlees，其后用 Mirrlees |
| 生卒地 | 生于苏格兰 Minnigaff（Dumfries and Galloway 的 Wigtownshire）；逝于英格兰剑桥——国籍按 manifest 口径 United Kingdom |
| 门生身份口径 | Nicholas Stern 正文作 "Lord Nicholas Stern"；infobox 作 "Nicholas Stern, Baron Stern of Brentford"——入库用简洁形式 **Nicholas Stern**，正文叙述可带勋爵 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| asymmetric information | 不对称信息 | 诺奖理由核心词 |
| moral hazard | 道德风险 | 定译；勿译"道德危险" |
| optimal income taxation | 最优所得税 | 1971 论文主题 |
| Spence–Mirrlees condition | 斯彭斯–莫里斯条件 | 又名 single-crossing condition |
| single-crossing condition | 单一交点条件 | 曲线族只交一次的技术假设 |
| Diamond–Mirrlees efficiency theorem | 戴蒙德–莫里斯效率定理 | 1971，生产效率 |
| Mathematical Tripos | 剑桥数学荣誉学位考试 | 英国特有学制名，勿意译 |
| Edgeworth Professor | 埃奇沃思讲席教授 | 牛津教席名，非本人 Edgeworth |
| Mirrlees Review | 莫里斯评估 | IFS 主持的英国税制评估 |
| Knight Bachelor | 下级勋位爵士 | 与 KBE 等骑士团勋位不同类 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands**（manifest 预分配，音乐库 `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`）
- **匹配理由**：「新大陆」贴合其两次开疆——在牛津把最优税收从思想实验变成标准方法，晚年远赴中国香港/澳门与墨尔本开书院育才；曲名的开阔感也呼应从剑桥数学到信息经济学的跨域之旅。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `economics/presentations/20th_century/James_Mirrlees/NewLands.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/James_Mirrlees/page.md` | ★ 事实基准（唯一事实来源） |
| `economics/presentations/pages/20th_century/James_Mirrlees/metadata.json` | QID/生卒/国籍结构化参考（与正文冲突以 page.md 为准） |
| `economics/presentations/pages/20th_century/James_Mirrlees/images.txt` | 肖像候选 URL |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照（身份信息页/配色宏/页序列） |
| `economics/presentations/cover/` | OpenEcon 共享封面（`\input` 统一首页） |
| `MySQL/data/James_Mirrlees.yaml` | 本人物入库 yaml（fields/relations 与本文第三、四节一致） |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册（入库命令、note 引号规则、对手方规范名） |

## 十一、执行清单与验收标准 【模板通用】

1. 复制同世纪已完成篇目 Makefile，改 `MAIN=James_Mirrlees_zh`、`VIDEO_NAME=James_Mirrlees_zh`。
2. 下载肖像（images.txt 有 URL 直接用；无则 Commons `Special:FilePath/<File>?width=600`，404 则装饰圆占位）。
3. 配色宏按第五节：`mainclr=#0E4D64`，badgeA-D 四色照抄；宏名统一 `mainclr/accentclr/badgeA..D`，注释写语义。
4. 幻灯片序列按第六节 15 页规划逐页实现；身份信息页（02）必做；门生页（11）14 行表格用 arraystretch ≤0.62 压缩。
5. 编译循环：`make distclean && make`（latexmk 多遍），0 error；溢出指标 vbox ≤ 10pt / hbox ≤ 50pt。
6. `pdftoppm` 逐页目检，修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。
7. 全篇事实回查：每条陈述可溯源到 page.md；本篇无 page.md 载英文原话，全部转述。
8. 品牌口径：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。
9. 验收：pdfinfo 页数 = 规划页数；BGM wav 已复制到本目录。

## 十二、版式补遗（Beamer 实现要点） 【模板通用】

- 时间线 `\foreach` 分隔符必须 ASCII 逗号（中文逗号会吞条目）。
- 表格页安全负间距：顶部 -0.35cm、`arraystretch` 0.78-0.82；公式框前 -0.35 ~ -0.55cm；14 行门生表用两栏排布或 arraystretch 0.58 + 顶部 -0.55cm。
- 单一交点曲线族用 tikz plot 三条曲线限域绘制，交点用金色圆点标记。
- `remember picture` 需两遍编译；取日志单遍 xelatex 后必须重新 `make pdf`。
- `\newcommand` 宏名禁数字；en-dash（–）用于年份区间，TeX 下直接输入即可。
