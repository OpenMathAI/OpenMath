# 经济学家立传提示词（Jan Tinbergen）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1969 年得主 Jan Tinbergen（扬·廷贝亨）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Jan_Tinbergen/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Jan Tinbergen（1903-04-12 生于海牙 ~ 1994-06-09 逝于海牙，享年 91 岁）
- **气质关键词**：**首届经济学诺奖得主、计量经济学奠基人、首个国民经济宏观模型构建者**
- **诺奖获奖理由**（1969 与 Ragnar Frisch 共享首届奖，逐字引用 manifest）：
  > "for having developed and applied dynamic models for the analysis of economic processes"（表彰他们为经济过程分析开发并应用了动态模型）
- **设计母题**：**目标与工具（targets & instruments）**——政策制定者须用数量相等的工具去命中数量相等的目标；视觉上以「靶心 + 操纵杆」的双元意象、瞄准线与调节旋钮构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Jan_Tinbergen/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Jan_Tinbergen/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Jan_Tinbergen_zh`、`VIDEO_NAME=Jan_Tinbergen_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Tinbergen 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 计量经济学 | 计量经济学奠基人之一，诺奖核心 | 封面、核心页 |
| 1 | macroeconomics | 宏观经济学 | 首个国家综合宏观经济模型（1936 荷兰，后推美国、英国） | 核心页 |
| 2 | economic policy | 经济政策 | targets/instruments 分类与 Tinbergen Rule | 政策页 |
| 3 | development economics | 发展经济学 | 为多国政府与国际组织提供咨询 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Paul Ehrenfest | 师→生 | 莱顿大学博士导师（1929），物理学家；论文《物理学与经济学中的极小化问题》 |
| co-honored | Ragnar Frisch | 无向 | 1969 首届诺贝尔经济学奖共享（发展并应用动态模型分析经济过程） |
| advisor-student | Tjalling Koopmans | Tinbergen→学生 | infobox Doctoral students 明载；1975 经济学诺奖得主 |
| advisor-student | Hans van den Doel | Tinbergen→学生 | infobox Doctoral students 明载（工党政治人物） |
| advisor-student | Supachai Panitchpakdi | Tinbergen→学生 | infobox Doctoral students 明载 |
| advisor-student | Ashok Mitra | Tinbergen→学生 | infobox Doctoral students 明载 |
| colleague | Henri Theil | 无向 | 1956 共同创建鹿特丹经济计量研究所，Theil 亦为其接班人 |
| controversy | John Maynard Keynes | 无向 | 计量建模引发的 Tinbergen debate 参与者 |
| controversy | Milton Friedman | 无向 | Tinbergen debate 参与者 |

**不入库但提示词可叙述**：弟弟 Nikolaas "Niko" Tinbergen（1973 生理学或医学诺奖得主；兄弟俩是仅有的双双获诺奖的兄弟——兄弟关系无对应入库类型）；幼弟 Luuk Tinbergen（鸟类学家）；莱顿求学期间与 Kamerlingh Onnes、Hendrik Lorentz、Pieter Zeeman、Albert Einstein 的多次讨论（page.md 仅载"讨论"，非师承/同事实质关系）；Economists for Peace and Security 创始受托人（机构关系）。

## 五、配色方案 【人物专属】

- **气质**：荷兰式的清明理性、政策工程的秩序感
- **主色**：`#1E3A5F`（代尔夫特深蓝——荷兰工程理性与宏观模型的冷峻感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeEcon` 计量经济 — 靛蓝 `#1E3A5F`
  - `badgeMacro` 宏观模型 — 青蓝 `#175E54`
  - `badgePolicy` 政策工具 — 琥珀 `#C07A2A`
  - `badgePeace` 和平与发展 — 深红 `#7E1E23`
- **背景母题**：靶心与调节旋钮（targets 与 instruments 数量相等的抽象），呼应「用等量工具命中等量目标」的 Tinbergen Rule。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 首届经济学诺奖得主 / Jan Tinbergen 1903–1994 + 四色 badge + 右上头像 + 国籍行（Netherlands）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒海牙、教育莱顿大学 PhD 1929、
    导师 Ehrenfest、任职鹿特丹/CPB、诺奖 1969 首届、核心领域）
03  核心贡献概览 — 首个宏观模型 / 计量经济学 / Tinbergen Rule / 发展规划
04  海牙少年与莱顿岁月 (1903–1929) — 数学与物理学出身，Ehrenfest 门下
05  博士论文：物理与经济在极小化问题中相遇 — Ehrenfest 建议选题，四种兴趣合一
06  CBS 与首批宏观模型 (1930s) — 中央统计局商情调查部首任主任；1936 荷兰模型，推至美英
07  动态模型：诺奖理由的核心（核心贡献页）— 首个宏观计量模型与经济动态分析
08  Tinbergen Rule：目标与工具 — targets/instruments 分类；今日央行的利率-通胀框架
09  计量方法的其他贡献 — 识别问题的解、Tinbergen debate（Keynes/Frisch/Friedman 参与的论战）
10  CPB：经济政策分析局 (1945–1955) — 创立并任首任局长；哈佛访问教授一年
11  鹿特丹与经济计量研究所 (1956) — 与 Henri Theil 共同创建
12  发展规划与国际咨询 — 阿联、土耳其、委内瑞拉、苏里南、印尼、巴基斯坦等
13  收入分配与最优社会秩序 — Tinbergen Norm（5:1 比率；本人 1981 年文章讨论过技术细节）
14  遗产与结尾 — 兄弟双诺奖佳话 + 计量经济学制度化（Tinbergen Institute 以其命名）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 首届奖共享 | 1969 是诺贝尔经济学奖**第一届**，Tinbergen 与 Frisch **共享**；获奖理由用"他们"（官方原文 "for having developed and applied dynamic models..."），勿写成个人独得或各自理由 |
| 兄弟诺奖 | 弟 Niko Tinbergen 获 1973 生理学或医学奖；兄弟俩是**唯一双双获诺奖的兄弟**——page.md 明载可写，但兄弟关系不入库（无 sibling 类型） |
| Tinbergen Norm 谨慎表述 | page.md 明言"没有廷贝亨本人的著作正式陈述该准则"，是他死后被广泛讨论的原则；只能说 1981 年文章讨论过 5:1 收入比的技术细节，勿写成他正式提出 |
| 博士学科 | 1929 博士论文《Minimumproblemen in de natuurkunde en de economie》是**物理学与经济学**的极小化问题——学科交叉点，勿写成纯经济学博士 |
| 职业线时间轴 | CBS 至 1945；1931 起阿姆斯特丹大学统计学教授；1933 起鹿特丹荷兰经济学院任数学与统计学副教授至 1973；1945 创立 CPB 并任首任局长、1955 离任；勿混淆 |
| Tinbergen debate | 计量建模引发的论战参与者为 Keynes、Frisch、Friedman 等；写论战客观简述，勿加立场评价 |
| Delta Works | 1953 北海洪灾后任三角洲工程委员会成员，1954/1960 两次成本收益分析——"最早的国家基础设施项目正式社会成本收益评估之一"，按 page.md 口径 |
| Klein 的继承 | 宏观模型工作由 Lawrence Klein 继续并再获诺奖——叙述可写，Klein 的师承边在 Samuelson 篇入库（非 Tinbergen 学生） |
| 与物理学家的"讨论" | 莱顿期间与 Onnes/Lorentz/Zeeman/Einstein 仅有讨论记载，**禁写**师承或合作 |
| metadata 无冲突 | frontmatter 生卒与正文一致（1903-04-12 / 1994-06-09），直接使用 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| econometrics | 计量经济学 | 奠基人之一；与"经济计量学"为同义译名，全篇统一 |
| macroeconometric model | 宏观计量模型 | 首个国家综合模型，1936 荷兰 |
| targets and instruments | 目标与工具 | 政策变量二分法 |
| Tinbergen Rule | 廷贝亨法则 | 目标数=工具数 |
| identification problem | 识别问题 | 计量经济学经典问题 |
| Tinbergen Norm | 廷贝亨准则 | 非本人正式陈述，措辞须谨慎 |
| dynamic model | 动态模型 | 获奖理由核心词 |
| business cycle | 经济周期 | 早期研究主题 |
| cost–benefit analysis | 成本收益分析 | 三角洲工程委员会工作 |
| development planning | 发展规划 | 晚年咨询主线 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**："新大陆"的开拓感对应首届诺奖的拓荒身份——Tinbergen 把物理学工具带入经济学，开辟了计量经济学与政策分析的新疆域；曲目的探索气质也贴合他从海牙 CBS 到各国发展规划咨询的职业生涯。
- **本地路径**：复制 `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav` 到 `economics/presentations/20th_century/Jan_Tinbergen/NewLands.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
- **撞曲说明**：1969 两人共享奖，Frisch 篇 manifest 同配 New Lands；出片阶段如需去重由主控统一裁定。
