# 经济学家立传提示词（James Tobin）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1981 年得主 James Tobin（詹姆斯·托宾）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/James_Tobin/page.md`，与其冲突时以 page.md 为准。

## 0. 背景信息 【人物专属】

- **目标经济学家**：James Tobin（1918-03-05 生于伊利诺伊州尚佩恩 ~ 2002-03-11 逝于康涅狄格州纽黑文，享年 84 岁）
- **气质关键词**：**金融市场的分析大师、凯恩斯主义的守护者、托宾税的提出者** —— 1981 诺贝尔经济学奖获奖理由：
  > "for his analysis of financial markets and their relations to expenditure decisions, employment, production and prices"（表彰他对金融市场及其与支出决策、就业、生产和价格关系的分析）
- **设计母题**：**风险与回报的天平（risk-return balance）**——托宾 1958 年把组合选择化约为均值-方差的权衡：天平两端是风险与预期回报，背景是资产市场的K线与现金流；天平意象 + 现金/债券双账户的几何块构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/James_Tobin/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 一、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/James_Tobin/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取——page.md 有 1962 年照片，404 则装饰圆占位）；Makefile 复制后设 `MAIN=James_Tobin_zh`、`VIDEO_NAME=James_Tobin_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库（见下二、三节），无需重复执行；第 5 步起按本文第四至八节执行。

## 二、研究领域梳理 + 入库 【人物专属】

**Tobin 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | macroeconomics | 宏观经济学 | infobox Discipline；凯恩斯主义微观基础 | 封面、核心页 |
| 1 | financial markets | 金融市场 | 获奖理由核心；组合选择理论 | 核心页 |
| 2 | monetary economics | 货币经济学 | 流动性偏好即风险行为；Baumol–Tobin | 货币页 |
| 3 | econometrics | 经济计量学 | Tobit 模型（截取因变量回归） | 方法页 |

## 三、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Joseph Schumpeter | 师→生（本人受教） | 哈佛博士（1947）论文导师，正文+infobox 明载 |
| influence | John Maynard Keynes | 无向 | 1936 读《通论》启蒙；毕业论文批判其非自愿失业均衡机制 |
| spouse | Elizabeth Fay Ringo | 无向 | 1946-09-14 结婚，Samuelson 的 MIT 学生，育四子女 |
| advisor-student | William Brainard | 本人→学生 | 博士生（infobox）；耶鲁同事与频繁合作者 |
| advisor-student | Willem Buiter | 本人→学生 | 博士生（infobox 明载） |
| advisor-student | Duncan K. Foley | 本人→学生 | 博士生（infobox 明载） |
| advisor-student | Koichi Hamada | 本人→学生 | 博士生（infobox 明载） |
| advisor-student | Edmund Phelps | 本人→学生 | 博士生（infobox 明载） |
| advisor-student | Janet Yellen | 本人→学生 | 博士生（infobox 明载） |
| advisor-student | Hiroshi Yoshikawa | 本人→学生 | 博士生（infobox 明载） |
| collaborator | James Meade | 无向 | 1977 与 Meade 共同提出名义 GDP 目标制（1980 成文） |
| collaborator | William Nordhaus | 无向 | 1972 合著 Is Growth Obsolete? 提出经济福利度量 MEW |
| collaborator | Arthur Okun | 无向 | 肯尼迪任内 CEA 共事，密切合作设计凯恩斯经济政策 |
| collaborator | Robert Solow | 无向 | 肯尼迪任内 CEA 共事，密切合作设计凯恩斯经济政策 |
| collaborator | Kenneth Arrow | 无向 | 肯尼迪任内 CEA 共事，密切合作设计凯恩斯经济政策 |

**入库备注**：Okun/Solow/Arrow 三人均为 page.md 明载「in close collaboration with」；Arrow 复用库内既有记录 id=2639（防分裂），Okun/Solow 新建 stub。Brainard 一人建 advisor-student 单边（同事合作写入 note，不另开 colleague 边防重复）。

**不入库但提示词可叙述**（防 Review 误判）：
- 四个子女：page.md 未具名，不入库。
- Walter Heller（CEA 主席）、Kennedy 政府：上下级/雇用关系非学术关系。
- Robert Mundell：Tobin's notable ideas 列 Mundell–Tobin effect，但正文未叙述两人交往——模型命名提及不入库。
- Palda：转述 Tobin 1958 贡献的作者，仅文献叙述。
- Adair Turner：2009 年重提金融交易税的政治人物——事件叙述不建边。
- Robert Shiller 等：未出现；AEA/计量学会等会员资格不建边。
- James Tobin（同名者）：正文无同名混淆风险，无需消歧义。

## 四、配色方案 【人物专属】

- **气质**：温和的理性、凯恩斯传统的守夜人、市场与政府的平衡者
- **主色**：`#0B5351`（manifest 预分配，深青绿——耶鲁的沉稳与金融市场的冷静）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeFin` 金融市场 — 深青绿 `#0B5351`
  - `badgeKeyn` 凯恩斯宏观 — 深靛 `#2A3468`
  - `badgeMon` 货币理论 — 钢青蓝 `#37548D`
  - `badgeTobit` 计量方法 — 麦金 `#C8922A`
- **背景母题**：一台抽象的天平（风险 vs 预期回报），支点上方悬浮 q 值曲线；淡色资产K线作底纹。

## 五、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover 路径按 economics 执行）
01  封面 — 金融市场与凯恩斯传统 / James Tobin 1918–2002 + 四色 badge + 右上头像 + 国籍行
    （United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地尚佩恩、教育哈佛 1935 入学/
    博士 1947、任职耶鲁 1950–2002 与 Cowles Foundation、诺奖 1981、核心领域）
03  核心贡献概览 — 组合选择理论 / Tobin's q / Tobit 模型 / 托宾税
04  尚佩恩少年与哈佛 (1918–1939) — 父亲路易斯是「返校节」发明人（校媒口径）；
    1935 全国奖学金入哈佛；1936 初读凯恩斯《通论》；1939 summa cum laude
05  战时岁月 (1941–1945) — 物价管理办公室与战时生产局；1942 入美国海军，
    驱逐舰军官（含 USS Kearny）
06  哈佛博士与 Society of Fellows (1946–1950) — Schumpeter 指导消费函数论文；
    1947 Junior Fellow
07  耶鲁与考尔斯基金会 (1950–) — 1957 Sterling 讲席；Cowles 主席（1955–61/1964–65）；
    为凯恩斯经济学提供微观基础
08  组合选择理论（核心贡献页）— 1958 流动性偏好即风险行为；均值-方差权衡；
    无穷状态下的效用最大化化约
09  以 Tobin 命名的成果 — Tobit 模型（1958a）· Tobin's q（1969）· Baumol–Tobin 模型
    （1956）· Mundell–Tobin effect
10  托宾税 — 对外汇交易征税以抑制投机（他视为危险且无产出）；2009 Turner 重提之回响
11  白宫岁月 (1961–1968) — 肯尼迪 CEA 成员（主席 Walter Heller）；与 Okun/Solow/Arrow
    合作设计凯恩斯经济政策；美联储与财政部顾问
12  MEW 与政策论战 — 1972 与 Nordhaus 合著 Is Growth Obsolete? 提出经济福利度量；
    1977/1980 与 Meade 名义 GDP 目标制；1971 AEA 主席
13  荣誉与认可 — Nobel 1981 · Clark 奖章 1955 · Sterling Professor · 三院院士
14  遗产与结尾 — 组合选择理论进入教科书；耶鲁 James Tobin 研究档案 + 结尾页
```

## 六、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由两版本 | page.md 正文引语作 "creative and extensive work on the analysis of financial markets..."（带修饰语），manifest/官方 citation 为 "for his analysis of financial markets and their relations to expenditure decisions, employment, production and prices"；**以 manifest 为准**，正文版本可在 citation 页加注 |
| 「托宾税」立场 | 设计目的是减少国际货币市场投机（他视为 dangerous and unproductive）——照录其立场，勿写成「反全球化主张」或政治标签 |
| 师承两点 | Schumpeter 是**博士**论文导师（1947 消费函数）；Keynes 是思想启蒙+毕业论文批判对象，入库用 influence，勿写成「师从凯恩斯」 |
| Brainard 边数 | infobox 博士生 + 正文「耶鲁同事与频繁合作者」双重身份——yaml 只建 advisor-student 单边，合作写入 note，防重复边 |
| Okun/Solow/Arrow | page.md 原文 "in close collaboration with Arthur Okun, Robert Solow and Kenneth Arrow"——三人一律 collaborator 语义；Arrow 用库内 id=2639 规范记录 |
| Meade 年份 | 正文句为 "Along with ... James Meade in 1977, Tobin proposed nominal GDP targeting as a monetary policy rule in 1980"——1977 与 1980 两年份照录原文口径，勿擅自归一 |
| 父亲「发明返校节」 | "credited as the inventor of 'Homecoming'" 系 page.md 转述，用「被称为/获誉」措辞，勿写成确证史实 |
| Palda 长段引文 | page.md Legacy 节的 Palda 大段转述是其二手阐释，幻灯片只取 Tobin 1958 的核心洞见本身，勿把 Palda 文字当 Tobin 引语 |
| 海军经历 | 1942 入伍，驱逐舰军官（含 USS Kearny DD-432）——「among possibly others」措辞照录 |
| metadata 冲突 | metadata.json occupation 含 statistician/military personnel 等 Wikidata 推断项；yaml 职业按 page.md 实际身份取 economist/university teacher |
| 引语红线 | page.md 无 Tobin 本人直接引语；citation 评价为官方英文，引用须原文+中译；不得造中文「原话」 |

## 七、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| portfolio theory | 组合（资产组合）选择理论 | 1958 风险行为模型；勿与 Markowitz 均值-方差框架混为同一人贡献 |
| Tobin's q | 托宾 q | 企业市场价值与资本重置成本之比（1969） |
| Tobit model | Tobit 模型 | 截取回归（1958a），名称= Tobin + probit 类比 |
| Tobin tax | 托宾税 | 外汇交易税，勿写成「金融投机税」泛称 |
| Baumol–Tobin model | 鲍莫尔–托宾模型 | 交易性货币需求（1956），两人独立提出 |
| liquidity preference | 流动性偏好 | 凯恩斯概念；托宾赋予风险行为解释 |
| nominal GDP targeting | 名义 GDP 目标制 | 1977 与 Meade 共同提出（1980 成文） |
| Measure of Economic Welfare | 经济福利度量（MEW） | 1972 与 Nordhaus 合著提出 |
| Sterling Professor | 斯特林讲席教授 | 耶鲁最高讲席（1957） |
| Council of Economic Advisers | 总统经济顾问委员会（CEA） | 1961–62 成员，勿与美联储混 |

## 八、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「永恒」贴合托宾成果的长时段生命力——组合选择理论、Tobin's q、Tobit 模型与 Baumol–Tobin 模型至今是教科书标准内容，托宾税在 2009 年金融危机后仍被重提；曲目的绵长织体对应「理论穿越周期」的传记主线。
- **本地路径**：复制 `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` 到 `economics/presentations/20th_century/James_Tobin/Eternals.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 九、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/James_Tobin/page.md` | ★ 事实基准 |
| `economics/presentations/pages/20th_century/James_Tobin/metadata.json` | 结构化参考（冲突以 page.md 为准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` | 任务流程第三章 |
| `MySQL/data/James_Tobin.yaml` | 已入库 yaml 存档 |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册 |

## 十、执行清单 【模板通用】

1. 建目录 `economics/presentations/20th_century/James_Tobin/`（`images/` 子目录）。
2. 肖像：images.txt 有 URL 直接用（250px 改 500px）；无 URL 用 Commons `Special:FilePath`（curl 加 `-A "Mozilla/5.0"`，`file` 验证），404 则装饰圆占位。
3. 复制参照 Makefile，设 `MAIN=James_Tobin_zh`、`VIDEO_NAME=James_Tobin_zh`。
4. 按 §五 写 15 帧；每帧 `make` 编译，`pdftoppm` 截图目检。
5. 编译达标：0 error、vbox ≤ 10pt、hbox ≤ 50pt。
6. `make images && make video` 出 mp4；核对 BGM 时长。
7. Review-1 修正写回本提示词。

## 十一、版式补遗 【模板通用】

- 表格页安全负间距：顶部 `-0.35cm`、`arraystretch 0.78–0.82`；公式框/引语框前 `-0.35 ~ -0.55cm`。
- 「以 Tobin 命名的成果」页四条目命名页：itemize 压缩 `\itemsep -2.5pt` + 顶部 `-0.55cm`；公式 q=市值/重置成本 用 inline math。
- 天平母题 tikz：两侧托盘用简单矩形+线段，避免 clip 越界；`\foreach` 分隔符 ASCII 逗号。
- 年份区间（1918–2002 / 1961–68）用 en-dash `--`；宏名禁数字；带圈数字需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`。
- 引语框英文原文 `\itshape` + 中译 `\small`；半角引号 `" "`。

## 十二、生平时间线节点 【人物专属】

> 供时间线页/身份信息页取材（全部出自 page.md，勿外加）：

| 年份 | 事件 |
|------|------|
| 1918-03-05 | 生于伊利诺伊州尚佩恩；父 Louis Michael Tobin（记者，被誉「返校节」发明人）、母 Margaret Edgerton Tobin（社工） |
| 1935 | 全国奖学金入哈佛学院 |
| 1936 | 初读凯恩斯《通论》 |
| 1939 | summa cum laude 毕业（论文批判凯恩斯非自愿失业均衡机制） |
| 1940 | 哈佛硕士 |
| 1941 | 供职物价管理办公室与战时生产局；首篇论文发表 |
| 1942 | 入美国海军，任驱逐舰军官（含 USS Kearny DD-432） |
| 1946-09-14 | 与 Elizabeth Fay Ringo 结婚（育四子女） |
| 1947 | 哈佛博士（Schumpeter 指导，消费函数）；当选 Society of Fellows Junior Fellow |
| 1950 | 移教耶鲁大学（终其学术生涯） |
| 1955 | 获约翰·贝茨·克拉克奖章；Cowles Foundation 迁耶鲁 |
| 1955–61/1964–65 | 两度任 Cowles Foundation 主席 |
| 1957 | 任耶鲁 Sterling 经济学讲席教授 |
| 1956/1958a/1958b/1969 | Baumol–Tobin / Tobit / 流动性偏好即风险行为 / Tobin's q 四大成果发表 |
| 1961–62 | 出任肯尼迪总统经济顾问委员会（CEA）成员（主席 Walter Heller），1962–68 转顾问 |
| 1971 | 出任美国经济学会（AEA）主席 |
| 1972 | 与 Nordhaus 合著 Is Growth Obsolete? 提出经济福利度量（MEW） |
| 1977/1980 | 与 Meade 提出名义 GDP 目标制 |
| 1978 | 提出对外汇交易征税（后世称「托宾税」） |
| 1981 | 获诺贝尔经济学奖（金融市场分析及其与支出、就业、生产、价格的关系） |
| 1982–83 | 伯克利加州大学 Ford 访问研究教授 |
| 1988 | 自耶鲁正式退休，续任荣休教授授课著述 |
| 2002-03-11 | 逝于康涅狄格州纽黑文，享年 84 |

## 十三、肖像与图像素材指引 【人物专属】

- **优先**：`images.txt` 列出的 infobox 肖像（page.md 有 1962 年照片，250px 改 500px 下载）。
- **备用**：Commons `Special:FilePath/<文件名>?width=600`（curl 加 `-A "Mozilla/5.0"`，`file` 验证为真图）。
- **404 兜底**：装饰圆占位（姓名首字母 + 主色），图注注明「肖像暂缺」。
- **禁用**：宏观经济学导航框内任何人物头像；与 Tobin R. Sosnick 等同姓者混淆的照片；Janet Yellen 后来的公职照片不当本传主图。

