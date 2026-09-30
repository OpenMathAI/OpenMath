# 经济学家立传提示词（Clive Granger）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2003 年得主 Clive Granger（克莱夫·格兰杰）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Clive_Granger/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Clive William John Granger（1934-09-04 生于威尔士斯旺西 ~ 2009-05-27 逝于加州拉霍亚斯克里普斯纪念医院，享年 74 岁）
- **气质关键词**：**协整之父、Granger 因果的命名者、时间序列的摆渡人**
- **诺奖获奖理由**（2003 为拆分理由年份，取**本人那条**，逐字引用）：
  > "for methods of analyzing economic time series with common trends (cointegration)"（表彰他提出了分析具有共同趋势的经济时间序列的方法（协整））
  - 来源：`economics/nobel_economics_citations.json` 2003 年 Clive Granger 条目（json 原值 "( cointegration )" 含空格噪声，已清理为 "(cointegration)"）；中译对照 `economics/economics_list_data.py` 2003 年 "||" 拆分**第二段**（官方获奖者顺序 Engle 在前、Granger 在后，勿取错段）
- **设计母题**：**协整（cointegration）**——两条各自随机游走、看似永不相交的序列，被一条看不见的长期均衡线系在一起；一红一蓝两条时间序列曲线在金色均衡线上交汇，是「短期漂移、长期归位」的视觉隐喻，构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Clive_Granger/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Clive_Granger/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Clive_Granger_zh`、`VIDEO_NAME=Clive_Granger_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至十二节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Granger 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 计量经济学 | infobox Discipline；诺奖核心学科 | 封面、核心页 |
| 1 | time series analysis | 时间序列分析 | 一生主线：谱分析、因果、协整 | 核心页 |
| 2 | financial economics | 金融经济学 | 诺奖工作对金融与宏观数据分析的改写 | 应用页 |
| 3 | forecasting | 预测 | 与 Newbold 的标准参考专著与组合预测 | 预测页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Harry Pitt | 师→生（博士导师） | 诺丁汉统计系博士导师，1959 论文《Testing for Non-stationarity》 |
| influence | David Hendry | 无向 | infobox Influences 明载 |
| influence | Norbert Wiener | 无向 | infobox Influences 明载（库内 id=56） |
| influence | John Denis Sargan | 无向 | infobox Influences 明载 |
| influence | Alok Bhargava | 无向 | infobox Influences 明载（经济学家，勿混库内数学家 Manjul Bhargava id=149） |
| co-honored | Robert F. Engle | 无向 | 2003 诺贝尔经济学奖共享（分析经济时间序列的方法） |
| colleague | Robert F. Engle | 无向 | UCSD 同事（助其加盟），1987 协整论文合著 |
| advisor-student | Mark Watson | Granger → 学生 | 博士生（infobox 明载；与 Engle 联合指导） |
| advisor-student | Tim Bollerslev | Granger → 学生 | infobox Doctoral students 明载 |
| advisor-student | Heather M. Anderson | Granger → 学生 | infobox Doctoral students 明载 |
| advisor-student | Kuan Chung-ming | Granger → 学生 | infobox Doctoral students 明载 |
| advisor-student | Paul Newbold | Granger → 学生 | 博士后研究员合作者；1974 伪回归论文与 1977 预测专著合著 |
| collaborator | Michio Hatanaka | 无向 | 普林斯顿共同助手，1964《经济时间序列谱分析》合著 |
| collaborator | Oskar Morgenstern | 无向 | 邀其入普林斯顿计量研究项目，1970《股价可预测性》合著（库内 id=353） |
| collaborator | John Tukey | 无向 | 普林斯顿傅里叶分析项目中担任其助手（库内 id=559） |
| collaborator | Roselyne Joyeux | 无向 | 分数积分（ARFIMA）合作 |
| collaborator | Timo Teräsvirta | 无向 | 非线性时间序列合作 |
| spouse | Patricia | 无向 | 1960 结婚直至去世（Lady Granger） |

**不入库但提示词可叙述**：一子 Mark William John 与一女 Claire Amanda Jane（正文具名但未书姓氏，防臆造不入 parent-child）；Arnold Zellner（人口普查局季节调整委员会主席，一次性职务交集）；George Box 与 Gwilym Jenkins（读其书稿引发预测兴趣，仅书缘）；断言其「永不会成功」的小学教师（无具名）。

## 五、配色方案 【人物专属】

- **气质**：均衡、回归、时间深处的秩序
- **主色**：`#52307C`（协整紫——两条漂移序列被长期均衡系住的深邃感；manifest 预分配，与同届共享得主 Engle 同色，同批撞色为 manifest 口径）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeCoint` 协整 — 协整紫 `#52307C`
  - `badgeCaus` 格兰杰因果 — 靛蓝 `#1F3A5F`
  - `badgeSpur` 伪回归警报 — 铁锈红 `#A63A2B`
  - `badgeSpec` 谱分析 — 琥珀 `#C07A2A`
- **背景母题**：红蓝两条随机游走曲线与一条金色长期均衡线在画面下三分之一处交汇，呼应「短期漂移、长期归位」的协整思想。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 协整之父 / Clive Granger 1934–2009 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地斯旺西、诺丁汉 BA 1955/PhD 1959、
    诺丁汉 22 年 → UCSD 1974–2003、诺奖 2003、2005 爵士、核心领域）
03  核心贡献概览 — 格兰杰因果 / 协整 / 伪回归 / 谱分析与预测
04  威尔士童年与战时迁居 (1934–1952) — 斯旺西出生、随母迁剑桥、战后诺丁汉、小学教师断言
05  诺丁汉：从数学到时间序列 (1952–1959) — 经济数学联合学位转纯数学、21 岁任初级讲师、
    Pitt 门下博士《Testing for Non-stationarity》
06  普林斯顿一年 (1959–1960) — Harkness Fellowship、Morgenstern 相邀、Tukey 项目、Hatanaka
07  谱分析时代 (1963–1969) — 1964 与 Hatanaka 合著、1966 典型谱形、1969 格兰杰因果
08  伪回归警报 (1974) — 与 Newbold 模拟研究重审既有实证工作，改写计量方法论
09  UCSD 二十二年 (1974–2003) — 助 Engle 加盟、Joyeux 分数积分、Teräsvirta 非线性时间序列
10  协整：共同趋势的长期均衡（核心贡献页）— 1987 Econometrica 论文、误差修正表示
11  2003 诺贝尔经济学奖 — 与 Engle 共享、理由按人拆分（本篇用协整条）
12  预测与超域应用 — 1977 预测专著、亚马逊雨林毁林预测、墨尔本/坎特伯雷访问学者
13  荣誉与认可 — Knight Bachelor 2005、计量学会会士 1972、英国科学院通讯会士 2002、
    100 Welsh Heroes 2004、Sir Clive Granger Building
14  遗产与结尾 — 协整与格兰杰因果成为金融/宏观标准工具 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 拆分理由年份 | 2003 理由按人拆分：本篇只用 Granger 条（common trends/cointegration），**禁用** Engle 条（time-varying volatility/ARCH）；中译照 `economics_list_data.py` 第二段「表彰他提出了分析具有共同趋势的经济时间序列的方法（协整）」 |
| 与 Engle 的关系层次 | co-honored（2003 共享）与 colleague（UCSD 同事+1987 合著+助其加盟）**两行并存**，note 各表其意，勿合并成一行 |
| 博士导师身份 | Harry Pitt 是诺丁汉**统计学**教授，博士论文为《Testing for Non-stationarity》（1959）；勿写成经济学导师或另编论文题 |
| Influences 口径 | Hendry/Wiener/Sargan/Bhargava 四人按 infobox Influences 入 **influence** 边，禁写「导师/合作者」；Alok Bhargava 是发展经济学家，勿与库内数学家 Manjul Bhargava（id=149）混淆（后者不入库） |
| 封爵与更名 | 2005 New Year Honours 封 Knight Bachelor（称 Sir）；2005 诺丁汉经济与地理系大楼更名 Sir Clive Granger Building 系**诺奖荣誉**（2003 得奖、2005 落实），两事同年勿混因果 |
| 协整论文年份 | 协整概念出自 **1987** Econometrica 论文（与 Engle 合著）；勿写成 1983、勿写成「诺奖当年提出」 |
| 关键年份三连 | 1969 格兰杰因果、1974 伪回归（与 Newbold）、1987 协整（与 Engle）；三组年份与合著者勿互换 |
| 子女不入库 | 正文具名 Mark William John / Claire Amanda Jane 但未书姓氏；**防臆造不入 parent-child**，幻灯片如提及仅说「一子一女」 |
| 引语红线 | 小学教师断言 "[Clive] would never be successful" 系 Granger 回忆转述，若引用必须用英文原文并注明转述性质，禁写成中文「原话」 |
| 在世/去世口径 | 2009-05-27 逝于拉霍亚 Scripps Memorial Hospital，享年 74；封面写 1934–2009，勿写「在世」 |
| 机构年代 | 诺丁汉 22 年（含 1956 21 岁任初级讲师）→ UCSD 1974–2003（2003 荣休 professor emeritus）；普林斯顿 1959–60 仅一年 Harkness Fellowship，勿写成教职 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cointegration | 协整 | 获奖理由核心词；「共同趋势+长期均衡」 |
| common trends | 共同趋势 | 获奖理由用词，勿译「公共趋势」 |
| Granger causality | 格兰杰因果 | 预测意义上的因果，非哲学因果 |
| spurious regression | 伪回归 | 1974 论文核心，非「虚假回归」泛称 |
| time series | 时间序列 | 全篇基础词 |
| spectral analysis | 谱分析 | 1964 专著方法，傅里叶分析应用于经济数据 |
| typical spectral shape | 典型谱形 | 1966 Econometrica 论文 |
| fractional integration / ARFIMA | 分数积分 | 与 Joyeux 合作方向 |
| error correction | 误差修正 | 协整的表示与估计框架 |
| Knight Bachelor | 下级勋位爵士 | 2005 获封，称 Sir |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：时间序列学者一生与「时间」博弈——因果是时间的方向、协整是时间的归位、伪回归是时间的错觉；「时间之流」的曲名即其学术母题，纪录片式的流动感贴合从斯旺西到 UCSD 的六十年历程。
- **本地路径**：复制 `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav` 到 `economics/presentations/21th_century/Clive_Granger/TheFlowOfTime.wav`
- **撞曲注记**：同届共享得主 Robert F. Engle 同曲（manifest 同批预分配）；若出片阶段需去重，由主控统一裁定，本篇先按 manifest 执行。
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Clive_Granger/page.md` | 事实基准（唯一事实来源） |
| `economics/presentations/pages/21th_century/Clive_Granger/metadata.json` | 结构化参考（冲突以 page.md 为准） |
| `economics/presentations/pages/21th_century/Clive_Granger/images.txt` | 肖像候选 URL |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 统一封面 |
| `economics/nobel_economics_citations.json` | 拆分理由英文原文 |
| `economics/economics_list_data.py` | 拆分理由中译对照（2003 年 "||" 第二段） |

## 十一、执行清单 【模板通用】

1. 通读本提示词与 page.md，建立事实卡（生卒/学位/机构/奖项/关系五组）。
2. 下载肖像（images.txt 或 Commons `Special:FilePath`，500px；404 则装饰圆占位）。
3. 复制 Makefile，设 `MAIN=Clive_Granger_zh`、`VIDEO_NAME=Clive_Granger_zh`；复制 BGM wav。
4. 按 §六逐页写 Beamer tex；每页 `make` 检查溢出（vbox≤10pt、hbox≤50pt）。
5. `make pdf` 0 error → `pdftoppm` 逐页目检 → `make images && make video` 出 mp4。
6. 数据库已由本批次入库（has_social_data=1），立传完成后由主控将 has_biography 置 1。

## 十二、版式补遗 【模板通用】

- 表格页安全负间距：顶部 −0.35cm、`arraystretch 0.78–0.82`；公式框前 −0.35~−0.55cm。
- 文本模式希腊字母需数学模式；带圈数字需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`。
- 引号用半角 `" "`；品牌口径统一 `OpenMathAI`；`\foreach` 分隔符用 ASCII 逗号。
- 结尾页底部标注 GitHub 链接由首页模板 `\input` 继承，子 deck 不重复。
