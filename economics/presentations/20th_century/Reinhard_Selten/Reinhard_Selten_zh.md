# 经济学家立传提示词（Reinhard Selten）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1994 年得主 Reinhard Selten（莱因哈德·泽尔腾）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Reinhard_Selten/page.md`，与其冲突时以 page.md 为准（同目录 metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：Reinhard Justus Reginald Selten（1930-10-05 生于布雷斯劳（今波兰弗罗茨瓦夫）~ 2016-08-23 逝于波兰波兹南，享年 85 岁）
- **气质关键词**：**子博弈完美化的精炼者、实验经济学奠基人之一、世界语学者**
- **诺奖获奖理由**（1994，与 John Nash、John Harsanyi 三人共享，manifest citation 逐字）：
  > "for their pioneering analysis of equilibria in the theory of non-cooperative games"（表彰他们在非合作博弈理论中关于均衡的开创性分析）
- **设计母题**：**博弈树与修剪（game tree & pruning）**——子博弈完美纳什均衡的核心是「在每一个子博弈上都最优」：以横向展开的博弈树、被剪除的不可信枝条与实验室格子构成背景母题，呼应「精炼均衡」与「实验经济学」的双重身份。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Reinhard_Selten/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

- **关键时间线（事实基准，取自 page.md）**：
  - 1930-10-05 生于下西里西亚布雷斯劳（时属魏玛德国，今波兰弗罗茨瓦夫）；父 Adolf Selten 犹太裔盲人书商（1942 卒），母 Käthe Luther 新教徒，本人按新教抚养
  - 童年随家短暂流亡萨克森与奥地利；战后回黑森州读中学，读 Fortune 杂志 John D. McDonald 论博弈的文章启蒙
  - 1957 法兰克福歌德大学数学 diploma；随后任 Heinz Sauermann 科研助手至 1967
  - 1959 与 Elisabeth Langreiner 结婚（无子女）；同年成为世界语者（经世界语运动结识妻子）
  - 1961 法兰克福数学博士（n 人博弈估值论文）
  - 1969–1972 柏林自由大学；1972–1984 比勒费尔德大学
  - 1984 起波恩大学；建成 BonnEconLab 实验经济学实验室，退休后仍活跃
  - 1994 诺贝尔经济学奖（与 Nash、Harsanyi 共享）——德国首位经济学诺奖得主，去世时仍是唯一
  - 2001 与 Gerd Gigerenzer 合编《Bounded Rationality: The Adaptive Toolbox》
  - 2009 欧洲议会选举中作为 Europe – Democracy – Esperanto 德国支部首席候选人
  - 2016-08-23 逝于波兰波兹南

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Reinhard_Selten/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 取——page.md infobox 明载 "Selten in 2001" 照片；404 则装饰圆占位）；Makefile 复制后设 `MAIN=Reinhard_Selten_zh`、`VIDEO_NAME=Reinhard_Selten_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

### 流程要点细化

- **第 0 步**：事实基准已在本文第一、七节固化（page.md 已核对），直接使用，勿再凭记忆改写；
- **第 1 步**：目录 `economics/presentations/20th_century/Reinhard_Selten/` 已存在（本提示词所在），只需建 `images/`；
- **第 2 步**：Makefile 从同世纪已完成篇目复制，仅改 `MAIN`/`VIDEO_NAME` 两行；
- **第 3 步**：infobox 有 "Selten in 2001" 真实照片，优先下载；
- **第 4/4.5 步**：已入库（见第三节 rank 表与第四节关系表），立传 agent 只读不写库；
- **第 5-9 步**：配色、幻灯片序列、编写、布局检查、史实审查按本文第五、六、七、十一、十二节执行，每写一页就编译一次。

## 三、研究领域梳理 + 入库 【人物专属】

**Selten 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | game theory | 博弈论 | 1994 诺奖核心；子博弈完美均衡 | 封面、核心页 |
| 1 | experimental economics | 实验经济学 | 奠基人之一；创建 BonnEconLab | 实验页 |
| 2 | bounded rationality | 有限理性 | 晚期主线；与 Gigerenzer 合编论文集 | 有限理性页 |
| 3 | aggregative games | 加总博弈 | 被认为完成该类博弈的首项研究 | 贡献页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Wolfgang Franz | Franz → 导师 | 法兰克福数学博士导师（1961 n 人博弈估值论文，infobox 明载） |
| advisor-student | Eric van Damme | Selten → 学生 | 博士生（infobox 明载） |
| advisor-student | Rosemarie Nagel | Selten → 学生 | 博士生（infobox 明载） |
| spouse | Elisabeth Langreiner | 无向 | 1959 结婚，无子女；经世界语运动结识 |
| co-honored | John Harsanyi | 无向 | 1994 经济学奖共享（非合作博弈均衡的开创性分析） |
| co-honored | John Forbes Nash | 无向 | 1994 经济学奖共享（非合作博弈均衡的开创性分析） |
| colleague | John Harsanyi | 无向 | 1988 合著《A General Theory of Equilibrium Selection in Games》 |
| colleague | Gerd Gigerenzer | 无向 | 2001 合编《Bounded Rationality: The Adaptive Toolbox》 |
| colleague | Heinz Sauermann | 无向 | 法兰克福时期（至 1967）任其科研助手 |

**不入库但提示词可叙述**：Ewald Burger（仅 metadata.json doctoral_advisor 有载、page.md infobox 只列 Franz——metadata-only 不入库）；父母 Adolf Selten / Käthe Luther（page.md 明载但不建学术关系）；John D. McDonald（Fortune 文章作者，红链接，启蒙阅读非关系）；Thomas Marschak（1974 合著 General Equilibrium with Price-Making Firms，仅书目行——保守起见未入库，如需可补）。

## 五、配色方案 【人物专属】

- **气质**：缜密、克制、实验室的冷静秩序
- **主色**：`#1E3A5F`（manifest 预分配，深海蓝——与 Harsanyi 同届同色系）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGame` 博弈论 — 深海蓝 `#1E3A5F`
  - `badgeExp` 实验经济学 — 青绿 `#0E7C7B`
  - `badgeBound` 有限理性 — 琥珀 `#C07A2A`
  - `badgeEsper` 世界语运动 — 玫瑰 `#C4204F`
- **背景母题**：博弈树与被剪除的枝条（细线树形图 + 虚线剪枝痕），呼应「子博弈完美 = 每个子博弈都可信」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 子博弈完美的精炼者 / Reinhard Selten 1930–2016 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、布雷斯劳出生、法兰克福数学 diploma 1957/博士 1961、
    任职波恩大学、诺奖 1994、核心领域）
03  核心贡献概览 — 子博弈完美 / 实验经济学 / 有限理性 / Selten's Horse
04  布雷斯劳童年与战时流亡 (1930–1945) — 犹太裔父亲、新教家庭、萨克森与奥地利流亡、战后黑森
05  一篇杂志文章的启蒙 — Fortune 杂志博弈论文章；上下学路上在脑中摆弄初等几何与代数
06  法兰克福：数学与 Sauermann 岁月 (1951–1967) — diploma 1957、科研助手、1961 数学博士
07  世界语与婚姻 (1959–) — 经世界语运动结识 Elisabeth；国际科学院 San Marino 共同创立
08  柏林与比勒费尔德 (1969–1984) — 自由大学、比勒费尔德大学执教
09  子博弈完美：把均衡变可信（核心贡献页）— 子博弈完美纳什均衡；Selten's Horse
10  实验经济学奠基 — BonnEconLab 的建立与退休后的坚持
11  有限理性 — Bounded Rationality: The Adaptive Toolbox（与 Gigerenzer 合编 2001）
12  1994 诺贝尔经济学奖 — 德国首位（去世时唯一）经济学诺奖得主；三人共享
13  荣誉与晚年 — Pour le Mérite、北威州勋章、多所荣誉博士；2009 欧洲议会世界语政党首席候选人
14  遗产与结尾 — 从精炼均衡到行为与实验经济学的现代格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 三人共享 | 1994 与 **John Nash、John Harsanyi** 三人共享；citation 三人同句「their pioneering analysis」；勿写成独得或两人 |
| 双导师之争 | metadata.json doctoral_advisor 有 Ewald Burger + Wolfgang Franz 两值，**page.md infobox 只载 Wolfgang Franz**——入库只建 Franz；Burger 仅可在提示词叙述中提"另有记载"，不建边 |
| 学位口径 | 法兰克福学位全是**数学**（1957 diploma、1961 博士论文 n 人博弈估值）；勿写"经济学博士" |
| 出生地名 | 生于布雷斯劳（Breslau，今波兰弗罗茨瓦夫，时属魏玛德国）；卒于波兹南（Poznań，波兰）——两个波兰城市、三种国籍语境，行文注明"今属波兰" |
| 德语第一 | page.md 明载 Selten 是**德国首位**经济学诺奖得主，且去世时仍是唯一——此为可写强断言 |
| 教职顺序 | 1969-72 柏林自由大学 → 1972-84 比勒费尔德 → 1984 起波恩；勿与 1957-67 法兰克福助手期混淆 |
| Selten's Horse | 因**扩展型（extensive form）表述**得名"马"，不是形状像马；勿编造来历 |
| 非匿名审稿 | page.md 载其刻意在非匿名评审期刊发文以免被迫改稿——可作趣闻，不评价 |
| 世界语党派 | 2009 欧洲议会选举为 Europe – Democracy – Esperanto 德国支部**首席候选人**——客观事实陈述，不展开政治议题 |
| 姓名缩写 | 全名 Reinhard Justus Reginald Selten；行文用 Reinhard Selten；勿缩写为 R. Selten 作标题 |
| 对手方规范名 | co-honored 对手方用库内 **John Forbes Nash**(967) 与本批新建 **John Harsanyi**(7686)；勿用 'John Nash'(429) |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| subgame perfect Nash equilibrium | 子博弈完美纳什均衡 | 核心贡献；"精炼（refinement）"概念 |
| extensive form | 扩展型表述 | Selten's Horse 得名来源 |
| backward induction | 逆向归纳 | 与子博弈完美配套的求解思想 |
| bounded rationality | 有限理性 | 晚期主线，与 Simon 概念一脉 |
| experimental economics | 实验经济学 | BonnEconLab；奠基人之一 |
| aggregative game | 加总博弈 | 被认为完成首项研究 |
| impulse balance theory | 冲量平衡理论 | 最后著作（2015）主题 |
| Esperanto | 世界语 | 1959 年起；学术界罕见的第二身份 |
| BonnEconLab | 波恩实验经济学实验室 | 命名实体，勿拆译 |
| Pour le Mérite | 蓝马克斯功勋勋章（科学与艺术类） | 德国最高荣誉之一，勿与军功类混淆 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/23-GiwYLGgJw7w-... Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav`）
- **匹配理由**：「探路者」双重贴合——其一，在均衡精炼与实验经济学两条无人区开路；其二，从布雷斯劳流亡少年到波恩实验室掌门，一生都在未知地形上前行。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `economics/presentations/20th_century/Reinhard_Selten/Pathfinder.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/Reinhard_Selten/page.md` | ★ 事实基准（唯一事实来源） |
| `economics/presentations/pages/20th_century/Reinhard_Selten/metadata.json` | QID/生卒/国籍结构化参考（双导师噪声以 page.md 为准） |
| `economics/presentations/pages/20th_century/Reinhard_Selten/images.txt` | 肖像候选 URL（infobox "Selten in 2001"） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照（身份信息页/配色宏/页序列） |
| `economics/presentations/cover/` | OpenEcon 共享封面（`\input` 统一首页） |
| `MySQL/data/Reinhard_Selten.yaml` | 本人物入库 yaml（fields/relations 与本文第三、四节一致） |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册（入库命令、note 引号规则、对手方规范名） |

## 十一、执行清单与验收标准 【模板通用】

1. 复制同世纪已完成篇目 Makefile，改 `MAIN=Reinhard_Selten_zh`、`VIDEO_NAME=Reinhard_Selten_zh`。
2. 下载肖像（images.txt 有 URL 直接用；无则 Commons `Special:FilePath/<File>?width=600`，404 则装饰圆占位）。
3. 配色宏按第五节：`mainclr=#1E3A5F`，badgeA-D 四色照抄；宏名统一 `mainclr/accentclr/badgeA..D`，注释写语义。
4. 幻灯片序列按第六节 15 页规划逐页实现；身份信息页（02）必做。
5. 编译循环：`make distclean && make`（latexmk 多遍），0 error；溢出指标 vbox ≤ 10pt / hbox ≤ 50pt。
6. `pdftoppm` 逐页目检，修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。
7. 全篇事实回查：每条陈述可溯源到 page.md；本篇无直接引语，全部转述（"mind with problems..." 仅 page.md 转述句，禁作引文框原话）。
8. 品牌口径：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。
9. 验收：pdfinfo 页数 = 规划页数；BGM wav 已复制到本目录。

## 十二、版式补遗（Beamer 实现要点） 【模板通用】

- 时间线 `\foreach` 分隔符必须 ASCII 逗号（中文逗号会吞条目）。
- 表格页安全负间距：顶部 -0.35cm、`arraystretch` 0.78-0.82；公式框前 -0.35 ~ -0.55cm。
- 博弈树 tikz 节点数控制在 15 个以内，剪枝枝条用 dashed 灰线，避免页面拥挤。
- `remember picture` 需两遍编译；取日志单遍 xelatex 后必须重新 `make pdf`。
- `\newcommand` 宏名禁数字；世界语帽子字母（ŝ/ĝ）如出现须检查字体 fallback，必要时数学模式或改拼 ASCII。
