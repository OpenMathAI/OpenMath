# 经济学家立传提示词（Franco Modigliani）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1985 年得主 Franco Modigliani（弗兰科·莫迪利安尼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Franco_Modigliani/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Franco Modigliani（1918-06-18 生于罗马 ~ 2003-09-25 逝于美国马萨诸塞州剑桥，享年 85 岁），意大利裔美国经济学家
- **气质关键词**：**生命周期假说的缔造者、M-M 定理的创始人、从罗马流亡到 MIT 的一代宗师**
- **诺奖获奖理由**（逐字引用）：
  > "for his pioneering analyses of saving and of financial markets"（表彰他对储蓄与金融市场的开创性分析）
- **设计母题**：**生命周期的储蓄曲线（life-cycle savings curve）**——工作年份储蓄、退休年份花销，一生消费平滑成一条弧线，是「跨期配置」的视觉隐喻：一条贯穿人生刻度的金色储蓄曲线与两侧的资本资产构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Franco_Modigliani/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Franco_Modigliani/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Franco_Modigliani_zh`、`VIDEO_NAME=Franco_Modigliani_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Modigliani 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | macroeconomics | 宏观经济学 | 储蓄分析（生命周期假说），诺奖核心之一 | 核心页 |
| 1 | financial economics | 金融经济学 | 金融市场分析（M-M 定理），诺奖核心之二 | 核心页 |
| 2 | consumption and saving theory | 消费与储蓄理论 | 生命周期假说的主体内容 | 假说页 |
| 3 | corporate finance | 公司金融 | M-M 定理：融资结构与企业价值 | 定理页 |
| 4 | macroeconometric modeling | 宏观计量建模 | MPS 模型，长期指引华盛顿货币政策 | 模型页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Jacob Marschak | Modigliani ← 导师 | 新学院 1944 博士论文导师（正文+infobox 双明载） |
| advisor-student | Abba Lerner | Modigliani ← 导师 | 1944 博士论文共同指导（正文 supervision 明载） |
| influence | John Maynard Keynes | 无向 | infobox Influences 明载 |
| collaborator | Merton Miller | 无向 | 1958 卡内基共同提出 M-M 定理 |
| collaborator | Emile Grunberg | 无向 | 1954 合著论文，理性预期假说被认为由此发端 |
| advisor-student | Albert Ando | Modigliani → 学生 | infobox Doctoral students 明载；1960s 合著回应 Friedman–Meiselman |
| advisor-student | Robert Shiller | Modigliani → 学生 | infobox Doctoral students 明载 |
| advisor-student | Mario Draghi | Modigliani → 学生 | infobox Doctoral students 明载 |
| advisor-student | Lucas Papademos | Modigliani → 学生 | infobox Doctoral students 明载；1975 合著提出 NIRU |
| controversy | Milton Friedman | 无向 | 1960s 与 Ando 合著回应 Friedman–Meiselman 论文，开启货币/财政政策论战 |
| spouse | Serena Calabi | 无向 | 1939 巴黎结婚，育二子 Andre 与 Sergio |

**不入库但提示词可叙述**：二子 Andre 与 Sergio（仅具名不入 parent-child）；孙女 Leah Modigliani（隔代不入，1997 合创风险调整绩效指标只叙述）；Oskar Lange（早年文章沿其市场社会主义路线行文，思想脉络薄）；Mussolini 颁奖与《Lo Stato》撰稿（历史事实客观简述，不建边、不评价）；David I. Meiselman（Friedman 合著者，论战对面经由 Friedman 单边承载）。

## 五、配色方案 【人物专属】

- **气质**：跨越大西洋的坚韧、理论的优雅、金融与宏观的交汇
- **主色**：`#1E6B52`（ lifecycle 松绿——储蓄曲线贯穿一生的生长与平滑）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeLife` 生命周期假说 — 松绿 `#1E6B52`
  - `badgeMM` M-M 定理 — 靛蓝 `#2E3A59`
  - `badgeMPS` MPS 模型 — 琥珀 `#C07A2A`
  - `badgeNIRU` NIRU — 灰紫 `#52307C`
- **背景母题**：一条贯穿人生刻度的金色储蓄曲线（工作期上行、退休期下行的驼峰形态），呼应「消费平滑、跨期配置」的核心思想。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 生命周期假说的缔造者 / Franco Modigliani 1918–2003 + 四色 badge + 右上头像 + 国籍行（Italy）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地罗马、教育 Sapienza Laurea 1939/
    新学院 PhD 1944、任职 MIT Institute Professor、诺奖 1985、核心领域）
03  核心贡献概览 — 生命周期假说 / M-M 定理 / MPS 模型 / NIRU
04  罗马早年 (1918–1938) — 犹太家庭、Sapienza 法学院、全国经济学竞赛头奖、种族法令后离开意大利
05  流亡与新学院 (1938–1944) — 巴黎、1939 移美、Marschak 与 Lerner 指导、IS–LM 扩展博士论文
06  生命周期假说（核心贡献页）— 工作期储蓄、退休期支出、一生消费平滑
07  M-M 定理（核心贡献页）— 1958 与 Miller、股债融资与企业价值无关性及其假设
08  理性预期的先声 (1954) — 与 Grunberg 论文被视为理性预期假说发端
09  货币/财政政策论战 (1960s) — 与 Ando 回应 Friedman–Meiselman、六十余年论战的开端
10  MPS 模型与政策咨询 — 联储合约、「在华盛顿指引货币政策数十年」、Economists for Peace and Security
11  NIRU 与失业观 (1975) — 与 Papademos、对自然率概念的改进、欧洲失业的需求侧立场
12  门生与传承 — Ando、Shiller、Draghi、Papademos（央行行长与学生）
13  荣誉与认可 — Nobel 1985、MIT Killian 奖 1985、那不勒斯费德里科二世荣誉博士 1997
14  遗产与结尾 — 从储蓄分析到现代公司金融 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由两半 | "pioneering analyses of **saving** and of **financial markets**"——两半分别对应生命周期假说与 M-M 定理，勿只写一半 |
| 双博士导师 | 正文明确 1944 博士论文 "written under the supervision of **Jacob Marschak and Abba Lerner**"（infobox 只列 Marschak）；两人**并列入库** advisor 边，frontmatter 双值与正文一致 |
| 早年法西斯时期史实 | 罗马时期获官方学联竞赛头奖并由 Mussolini 颁奖、为法西斯杂志《Lo Stato》撰稿、撰文论证社会主义经济——均为 page.md 明载历史事实，**只客观简述不评价**，亦不因此建立任何关系边 |
| 理性预期归属 | page.md 措辞 "is **considered** by economists to originate in the paper written by Modigliani and Emile Grunberg in 1954"——用「被认为发端于」，勿写成「发明了理性预期」 |
| NIRU vs NAIRU | 1975 提出 **NIRU**（非通胀失业率），后被称 NAIRU；注释明载 inflation "rises" 不 "accelerates"，两缩写勿混用 |
| 论战性质 | 与 Friedman 的分歧是学术论战（货币主义 vs 财政政策），controversy 边 note 只写「货币/财政政策论战」，禁写人身化表述 |
| 后凯恩斯批评 | Criticism 节客观转述：后凯恩斯学者质疑其「凯恩斯主义」成色（NAIRU、财政赤字立场），同时承认其在失业问题上与异端立场一致——两面并写 |
| MPS 模型名称 | "MIT-Pennsylvania-Social Science Research Council" model，缩写 MPS；勿与 Mont Pelerin Society（MPS，Buchanan 词条）混淆 |
| 学生身份分层 | Ando/Papademos 同时是合著者；Draghi 后任希腊/欧洲央行要职仅按 infobox 学生身份入库，官职细节不展开 |
| 国籍口径 | infobox Citizenship: Italy, United States；yaml 按 frontmatter 填 Italy + United States（1946 归化美国正文有载），Italy 含 Kingdom of Italy 噪声合并为 Italy |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| life-cycle hypothesis | 生命周期假说 | 诺奖核心，储蓄理论 |
| Modigliani–Miller theorem | M-M 定理 | 公司金融资本结构无关性 |
| NIRU | 非通胀失业率 | 后称 NAIRU，两词勿混 |
| MPS model | MPS 模型 | MIT-Penn-SSRC 联储模型 |
| IS–LM model | IS–LM 模型 | 博士论文扩展对象（Hicks） |
| monetary/fiscal policy debate | 货币/财政政策论战 | 与 Friedman–Meiselman 的对峙 |
| rational expectations | 理性预期 | 1954 Grunberg 论文「被认为」发端 |
| Sharpe ratio | 夏普比率 | 1997 风险调整绩效指标的 derivation 基础 |
| The New School for Social Research | 新社会研究学院 | 流亡后的博士训练地 |
| Institute Professor | 学院教授 | MIT 最高教职 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Modigliani 一生的叙事弧线正是「穿越黑暗」——1938 年种族法令下离开罗马、经巴黎流亡纽约，在新学院的夜色里完成博士论文，最终在 MIT 的顶峰俯瞰金融与宏观两条河流；曲名与流亡→重建→开创的命运轨迹严丝合缝。
- **本地路径**：复制 `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav` 到 `economics/presentations/20th_century/Franco_Modigliani/ThroughTheDarkness.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
