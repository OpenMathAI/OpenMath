# 经济学家立传提示词（Paul Samuelson）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1970 年得主 Paul Samuelson（保罗·萨缪尔森）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Paul_Samuelson/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Paul Anthony Samuelson（1915-05-15 生于印第安纳州加里市 ~ 2009-12-13 逝于马萨诸塞州贝尔蒙特，享年 94 岁）
- **气质关键词**：**首位美国经济学诺奖得主、数学经济学的奠基人、史上最畅销经济学教科书的作者**
- **诺奖获奖理由**（1970 独得，逐字引用 manifest）：
  > "for the scientific work through which he has developed static and dynamic economic theory and actively contributed to raising the level of analysis in economic science"（表彰他发展静态与动态经济理论的科学工作，并积极推动经济科学分析水平的提升）
- **设计母题**：**极大化与统一（maximization & unity）**——"用一套极大化方法重写大部分经济理论"；视觉上以「共同骨架上的多领域分支图」与极大化的一阶条件曲线构成背景母题，呼应其"经济问题与分析技术在根本上是统一的"的核心信条。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Paul_Samuelson/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Paul_Samuelson/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Paul_Samuelson_zh`、`VIDEO_NAME=Paul_Samuelson_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Samuelson 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | mathematical economics | 数理经济学 | 数学是经济学的"自然语言"；Foundations of Economic Analysis | 封面、核心页 |
| 1 | macroeconomics | 宏观经济学 | 乘数-加速器模型、世代交叠模型、新古典综合 | 核心页 |
| 2 | microeconomics | 微观经济学 | 显示偏好理论开创者 | 核心页 |
| 3 | welfare economics | 福利经济学 | Lindahl–Bowen–Samuelson 条件、公共品最优配置 | 福利页 |
| 4 | international economics | 国际经济学 | Stolper–Samuelson 定理、Balassa–Samuelson 效应 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Joseph Schumpeter | 师→生 | 哈佛求学期间授业老师（infobox Doctoral advisor 明载） |
| advisor-student | Wassily Leontief | 师→生 | 哈佛求学期间授业老师（infobox Doctoral advisor 明载） |
| advisor-student | Lawrence Klein | Samuelson→学生 | infobox Doctoral students 明载；1980 经济学诺奖得主 |
| advisor-student | Robert C. Merton | Samuelson→学生 | infobox Doctoral students 明载；1997 经济学诺奖得主 |
| influence | John Maynard Keynes | 单向 | infobox Influences 明载 |
| influence | Gottfried Haberler | 单向 | 哈佛求学期间授业老师（正文 studied under 明载） |
| influence | Alvin Hansen | 单向 | 哈佛求学期间授业老师、"美国凯恩斯"（正文 studied under 明载） |
| influence | Edwin Bidwell Wilson | 单向 | infobox Influences 明载 |
| influence | Knut Wicksell | 单向 | infobox Influences 明载 |
| influence | Erik Lindahl | 单向 | infobox Influences 明载 |
| spouse | Marion Crawford | 无向 | 1938 年结婚，1978 年去世 |
| spouse | Risha Clay | 无向 | 1981 年结婚 |
| colleague | Milton Friedman | 无向 | Newsweek 对立立场专栏并写多年（萨缪尔森"自助餐厅凯恩斯主义者" vs 弗里德曼货币主义），1967 年专栏为杂志赢得 Gerald Loeb 特别奖 |

**不入库但提示词可叙述**：兄 Robert Summers（改姓经济学家）、弟媳 Anita Summers、内弟 Kenneth Arrow、外甥 Larry Summers——姻亲/旁系关系无对应入库类型（Arrow 的 co-honored 边属 1972 Hicks/Arrow 篇，非 Samuelson 边）；对 Friedman 与 Hayek 的公开批评（意识形态论战，只客观转述不加评价）；1989 年致 Rosovsky 信中关于哈佛反犹氛围的叙述（敏感个人指控，客观简述、引语谨慎）；Kennedy/Johnson 总统顾问、美国财政部/预算局/经济顾问委员会咨询（机构关系）；学生 Tjalling Koopmans 名下的 Tinbergen 师承边与本篇无关。

## 五、配色方案 【人物专属】

- **气质**：新英格兰的智识自信、数学的澄澈与教科书式的亲和
- **主色**：`#16324F`（剑桥蓝——MIT 与哈佛之间的学术深蓝）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMath` 数理经济 — 深蓝 `#16324F`
  - `badgeMacro` 宏观综合 — 青蓝 `#0E4D64`
  - `badgeWelfare` 福利与公共 — 琥珀 `#C07A2A`
  - `badgeTrade` 国际贸易 — 深红 `#7E1E23`
- **背景母题**：极大化的一阶条件曲线与领域分支树——同一根骨架分出宏观、微观、福利、贸易诸枝，呼应"分析技术的根本统一"。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 首位美国经济学诺奖得主 / Paul Samuelson 1915–2009 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育芝大 BA 1935/哈佛 MA 1936 PhD 1941、
    导师 Schumpeter/Leontief、任职 MIT 1940 起、诺奖 1970、核心领域）
03  核心贡献概览 — 数学革命 / 显示偏好 / 新古典综合 / 公共品 / 国际贸易定理
04  加里市与芝加哥 (1915–1935) — "1932-01-02 早八点生于经济学"的自述；Malthus 讲座；Simons 与 Knight
05  哈佛博士岁月 (1935–1941) — Schumpeter/Leontief/Haberler/Hansen 门下；Wells 奖最佳博士论文
06  转赴 MIT (1940) — 反犹氛围与离哈入麻的传记叙述；1947 正教授、1962 Institute Professor
07  Foundations of Economic Analysis（核心贡献页）— 比较静态学；极大化行为+稳定均衡两大假设
08  显示偏好与消费者理论（核心贡献页）— 由观察行为反推效用函数
09  宏观经济学：新古典综合 — 乘数-加速器、世代交叠、Phillips 曲线分析
10  Economics 教科书传奇 (1948) — 史上最畅销；41 种语言、逾 400 万册；"让我写教科书就够了"
11  Newsweek 双雄论战 — 与 Friedman 对立专栏；"自助餐厅凯恩斯主义者"自况
12  荣誉集锦 — Clark 奖章 1947、诺奖 1970、国家科学奖章 1996、各学会职务
13  家学与传承 — Klein/Merton 诺奖学生；Summers-Arrow 家族（姻亲叙述）
14  遗产与结尾 — "在巨人肩膀上的巨人"（Poterba 悼词）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| "首位"限定 | 1970 年是**首位获得经济学诺奖的美国人**（page.md 原文 first American to win）；勿写成"首位经济学诺奖得主"（那是 1969 Tinbergen/Frisch） |
| 获奖评语双版本 | 瑞典皇家科学院 awarding 评语 "has done more than any other contemporary economist to raise the level of scientific analysis in economic theory"（intro）与委员会正式 statement（"He has simply rewritten considerable parts of economic theory..."）并存——引语须注明出处语境，获奖理由以 manifest citation 为准 |
| 双博士导师 | infobox Doctoral advisor 是 Schumpeter **与** Leontief 两人并立；正文另载 studied under 四人（加 Haberler/Hansen）——后两人用 influence 类型非 advisor-student |
| 教科书数据口径 | 1948 初版；每版 1961-1976 年间销量 30 万+；41 种语言；2018 年统计逾 400 万册；1985 年第 12 版起 Nordhaus 加入合著——数字与年份勿互相套用 |
| Foundations 年份 | 博士论文 1941（Wells 奖）；书 1947 初版、1983 扩充版——page.md 正文一处作 "Foundations of Economic Analysis (1946)"，出版物清单与Selected publications 作 1947：**取 1947**（出版物清单口径），陷阱表注明 1946 系页内异说 |
| 意识形态引语 | 对 Friedman/Hayek 的批评含 Genghis Khan/FDR/paranoid 等尖锐措辞——如引用须逐字并标明系 Samuelson 单方言论，建议以忠实转述为主 |
| 反犹叙述 | 离开哈佛的原因取自其传记作者与 1989 年致 Rosovsky 信（点名 Burbank/Chamberlin 等）——客观转述、不评价，人物点名可保留（page.md 明载） |
| 家族关系 | 兄 Robert Summers 是经济学家（本姓 Summers，Samuelson 是其本姓改姓来的兄长——page.md 只称 brother，勿推定改姓方向）；内弟 Kenneth Arrow、外甥 Larry Summers——均不入库（无类型） |
| Ulam 之问 | Ulam 挑战"既真又非平凡的社会科学理论"，Samuelson 数年后答以李嘉图比较优势——引语原文 page.md 明载可引 |
| 在世/去世 | 2009-12-13 短病后去世，享年 94；第二任妻子 Risha Clay 2019 年去世（death 段明载） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| revealed preference | 显示偏好 | 由选择行为反推偏好，勿写成"偏好显示定理"泛称 |
| neoclassical synthesis | 新古典综合 | 凯恩斯+新古典的合流，Samuelson 核心旗号 |
| comparative statics | 比较静态学 | Foundations 形式化的核心方法 |
| Stolper–Samuelson theorem | 斯托尔珀-萨缪尔森定理 | 国际贸易要素价格定理 |
| Balassa–Samuelson effect | 巴拉萨-萨缪尔森效应 | 汇率与生产率 |
| Lindahl–Bowen–Samuelson conditions | LSB 条件 | 公共支出效率判据 |
| multiplier-accelerator model | 乘数-加速器模型 | 与 Hansen 学派传统关联 |
| overlapping generations model | 世代交叠模型 | 1958 消费贷款模型 |
| turnpike theorem | 大道定理 | 资本理论 |
| efficient-market hypothesis | 有效市场假说 | Samuelson 金融侧贡献 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**："永恒"对应教科书七十年长销与理论框架的持久影响力——从 1948 教材到新古典综合仍主导主流经济学；曲目的沉稳长线感贴合"重写了大部分经济理论"的浩繁一生。
- **本地路径**：复制 `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` 到 `economics/presentations/20th_century/Paul_Samuelson/Timeless.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
