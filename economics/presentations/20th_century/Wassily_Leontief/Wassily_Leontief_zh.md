# 经济学家立传提示词（Wassily Leontief）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1973 年得主 Wassily Leontief（华西里·列昂惕夫）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Wassily_Leontief/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Wassily Wassilyevich Leontief（1905-08-05 生于慕尼黑，德意志帝国 ~ 1999-02-05 逝于纽约市，享年 93 岁）
- **气质关键词**：**投入产出之父、让数据说话的定量派、四位诺奖门生的师尊**
- **诺奖获奖理由**（1973，独得，逐字引自 manifest）：
  > "for the development of the input-output method and for its application to important economic problems"（表彰他发展了投入产出方法并将其应用于重要经济问题）
- **设计母题**：**循环流动（circular flow）**——产业之间投入与产出的相互依存网络，是「方格矩阵中水路纵横」的视觉隐喻：棋盘式网格与循环箭头构成背景母题，呼应其博士论文《经济作为循环流动》。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Wassily_Leontief/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Wassily_Leontief/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Wassily_Leontief_zh`、`VIDEO_NAME=Wassily_Leontief_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Leontief 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | input-output analysis | 投入产出分析 | 诺奖核心；产业间投入产出表与矩阵求解 | 核心页 |
| 1 | macroeconomics | 宏观经济学 | infobox field_of_work；国民经济结构分析 | 核心页 |
| 2 | international trade | 国际贸易 | Leontief 悖论（1953 经验发现） | 应用页 |
| 3 | empirical economics | 实证经济学 | 反对「理论假设与非观察事实」的定量主张 | 晚年页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Werner Sombart | Sombart → 师 | 柏林大学博士导师（1928，《经济作为循环流动》） |
| advisor-student | Ladislaus Bortkiewicz | Bortkiewicz → 师 | infobox Doctoral advisor 明载（正文仅载 Sombart） |
| advisor-student | Paul Samuelson | Leontief → 学生 | 正文明载四位诺奖门生之一（1970） |
| advisor-student | Robert Solow | Leontief → 学生 | 正文明载四位诺奖门生之一（1987） |
| advisor-student | Vernon L. Smith | Leontief → 学生 | 正文明载四位诺奖门生之一（2002） |
| advisor-student | Thomas Schelling | Leontief → 学生 | 正文明载四位诺奖门生之一（2005） |
| advisor-student | Kenneth E. Iverson | Leontief → 学生 | infobox 明载；库内已有图灵侧入边（id=228） |
| spouse | Estelle Marks | 无向 | 1932 结婚，诗人（1908–2005），著回忆录 Genia and Wassily |
| parent-child | Svetlana Leontief Alpers | Leontief → 女 | 1936 年生，艺术史学家（独女，page.md 明载） |

**不入库但提示词可叙述**：infobox Doctoral students 另有 Peter B. Dixon、Richard E. Quandt、Hyman Minsky、Dale W. Jorgenson、Michael C. Lovell、Karen R. Polenske、Hollis B. Chenery——防噪声只收正文点名四位诺奖门生 + Iverson（已有库边）；父 Wassily W. Leontief（经济学教授）与母 Evgenia Becker 仅生平叙述、隔代与无学术关系类型缺口不入库；George Dantzig 与线性规划系平行独立发展（正文未载直接交往），仅提示词叙述不入库；支持 Pitirim Sorokin 属一次性历史事件非持续关系。

## 五、配色方案 【人物专属】

- **气质**：表格的秩序、数据的重量、俄罗斯流亡者的坚韧
- **主色**：`#0F4C5C`（投入产出青——矩阵网格与循环水路的深海感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeIO` 投入产出 — 青蓝 `#0F4C5C`
  - `badgeTrade` 贸易悖论 — 深蓝 `#16324F`
  - `badgeComp` 计算先驱 — 琥珀 `#C07A2A`
  - `badgeFam` 家学与门生 — 灰紫 `#52307C`
- **背景母题**：棋盘网格与循环箭头（产业间投入产出表抽象），呼应「经济作为循环流动」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 投入产出之父 / Wassily Leontief 1905–1999 + 四色 badge + 右上头像 + 国籍行（Russian-American）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地慕尼黑、列宁格勒大学 MA 1925、柏林大学 PhD 1928、
    任职 Kiel/Harvard 1932–1975/NYU 1975–、诺奖 1973、核心领域）
03  核心贡献概览 — 投入产出分析 / Mark II 500 部门计算 / Leontief 悖论 / 定量经济学主张
04  彼得格勒早年 (1905–1925) — 旧礼仪派商人家庭、15 岁入彼得格勒大学、1925 十九岁获 Learned Economist 学位
05  苏联岁月与出走 (1921–1925) — 支持学术自治与 Sorokin、多次被 Cheka 拘留、以肉瘤误诊获准离境
06  柏林博士 (1925–1928) — 师从 Sombart、博士论文 Die Wirtschaft als Kreislauf
07  基尔与北京 (1927–1931) — 基尔世界经济研究所、1929 中国铁道部顾问、1931 赴 NBER
08  哈佛岁月 (1932–1975) — 1932 入经济系、1946 正教授、1948 创 Harvard Economic Research Project
09  投入产出分析（核心贡献页）— 投入产出表、固定比例假设、产业间波及估算
10  1949：Mark II 与 500 部门 — 哈佛 Mark II 求解 500 部门线性方程组、计算机数学建模先驱、PageRank 思想前驱
11  Leontief 悖论 — 美国出口相对劳动密集、与要素禀赋预期相反、后续解释
12  门生与传承 — Samuelson/Solow/Vernon Smith/Schelling 四位诺奖门生
13  NYU 晚年与荣誉 (1975–1999) — 创 Institute for Economic Analysis、1970 AEA 主席、荣誉学位与勋章
14  遗产与结尾 — 投入产出表与现代产业经济学 + Leontief Prize + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生年两说 | frontmatter 双值 1906-08-05 / 1905-08-05；infobox 与正文均作 **1905-08-05**（出生证明与诺奖官网口径 1905），yaml 取 1905，metadata 的 1906 为噪声 |
| 出生地 | 生于**慕尼黑**（德意志帝国），勿因俄裔背景误写圣彼得堡；旧礼仪派商人家庭自 1741 住圣彼得堡 |
| 双博士导师 | frontmatter 与 infobox 均载 Bortkiewicz + Sombart 两位；**正文仅明载 Sombart** 指导 1928 博士论文——Bortkiewicz 边以 infobox 明载入库并注明 |
| 四位诺奖门生 | Samuelson 1970 / Solow 1987 / Vernon L. Smith 2002 / Schelling 2005（正文点名）；infobox 另 8 人不入库 |
| Iverson 边 | Kenneth E. Iverson（图灵奖 1979）系 infobox 明载博士生，图灵侧已入库 from=228 边；本篇 yaml 复用同人幂等，防分裂须用全名 Kenneth E. Iverson |
| 姓氏歧义 | 妻 Estelle **Marks**（诗人）勿与库内其他 Estelle 混淆；女 Svetlana Leontief **Alpers** 冠夫姓的艺术史学家 |
| Dantzig 关系 | 正文只说线性规划 1939 由 Leontief 率先提出、数年后 Dantzig 才推进——平行独立发展，无直接交往记载，禁建边 |
| 悖论表述 | Leontief 悖论=美国出口相对劳动密集的**经验发现**与 H-O 理论预期相反；「悖论已被解释」按正文口径转述，勿写成"理论被推翻" |
| 计算页口径 | 1949 用 Harvard Mark II + 劳工统计局数据分 500 部门；「与 Snedecor 用 ABC 并列为最早重要应用之一」按正文措辞，勿写"第一台计算机应用" |
| 引语红线 | Quotes 节两段（学术实证批评、马与拖拉机之喻）有英文原文可引，须附译文；其余处禁杜撰中文"原话" |
| metadata 噪声 | frontmatter doctoral_advisor 顺序与 infobox 一致；nationality 含 Russian Empire 系 Wikidata 历史政权口径，yaml 按 manifest 拆 Soviet Union / United States |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| input-output analysis | 投入产出分析 | 核心词，勿译"投入-产出法"泛化 |
| input-output table | 投入产出表 | 产业间中间投入与最终需求 |
| circular flow | 循环流动 | 博士论文标题意象 |
| Leontief paradox | 列昂惕夫悖论 | 国际贸易经验发现，非"矛盾" |
| Harvard Mark II | 哈佛 Mark II | 1949 求解 500 部门方程组的早期计算机 |
| composite commodity theorem | 复合商品定理 | 正文载其为最早确立者之一 |
| Cheka | 契卡 | 苏联早期秘密警察，史实背景词 |
| Road of Life | 生命之路 | 列宁格勒围城冰上运输线——是 Kantorovich 篇内容，Leontief 篇勿混入 |
| Genia and Wassily | 《根尼亚与瓦西里》 | 妻 Estelle 的回忆录书名 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从彼得格勒到柏林再到哈佛，「唤醒」对应其一生把经济学从书斋理论唤醒到数据与计算的大地——投入产出表让整个经济的血脉第一次可以被计算。
- **本地路径**：复制 `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` 到 `economics/presentations/20th_century/Wassily_Leontief/Awaken.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/Wassily_Leontief/page.md` | 事实基准（唯一事实来源） |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册 |
| `MySQL/data/Wassily_Leontief.yaml` | 入库 yaml（与本文第三、四节一致） |
| `economics/economics_list_data.py` / `nobel_economics_citations.json` | 获奖理由中文对照 |

## 十一、执行清单 【模板通用】

1. 读 page.md 建立事实基准（本文件已沉淀，直接核对即可）
2. 下载肖像（images.txt 有 URL 直接用 500px；404 用 Commons `Special:FilePath`，再 404 装饰圆占位）
3. 复制 BGM wav 到人物目录
4. 写 tex（配色按第五节、Slide 序列按第六节）
5. 编译循环：0 error、vbox ≤ 10pt、hbox ≤ 50pt
6. pdftoppm + read_file 逐页目检
7. make images/video；Review-1 修正写回本文件
