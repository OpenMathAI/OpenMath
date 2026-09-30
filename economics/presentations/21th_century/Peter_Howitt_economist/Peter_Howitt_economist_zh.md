# 经济学家立传提示词（Peter Howitt）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2025 年得主（与 Philippe Aghion 共享一半）Peter Howitt（彼得·豪伊特）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Peter_Howitt_economist/page.md`，与其冲突时以 page.md 为准；`metadata.json` 仅作结构化参考。

## 一、背景信息 【人物专属】

- **目标经济学家**：Peter Wilkinson Howitt（1946-05-31 生于加拿大安大略省圭尔夫，在世）
- **气质关键词**：**创造性破坏的另一半、熊彼特传统的加拿大传人、货币宏观到增长理论的跨越者** —— Brown 大学 Lyn Crost Professor of Social Sciences Emeritus（2013 起荣休）
- **诺奖获奖理由**（2025 年经济学奖**与 Philippe Aghion 共享一半**；拆分理由年份，逐字引自 `economics/nobel_economics_citations.json` 2025 年 Peter Howitt 条目；中文对照 `economics/economics_list_data.py` 2025 年 `||` 拆分第二段）：
  > "for the theory of sustained growth through creative destruction"（表彰他们关于通过创造性破坏实现持续增长的理论）
  > 另一半由 Joel Mokyr 独得（理由为识别技术进步实现持续增长的前提条件，勿混写）。
- **设计母题**：**新旧交替的钟摆（the pendulum of creative destruction）**——旧范式让位于新范式的往复摆动：交替的明暗色块与摆锤弧线，喻示创造性破坏中企业进入与退出的动力学。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Peter_Howitt_economist/page.md`（同目录 `metadata.json` 仅作参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Peter_Howitt_economist/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Peter_Howitt_economist_zh`、`VIDEO_NAME=Peter_Howitt_economist_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Howitt 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | endogenous growth theory | 内生增长理论 | Aghion–Howitt 模型所属传统，诺奖核心 | 核心页 |
| 1 | creative destruction | 创造性破坏 | 获奖理由核心词 | 核心页 |
| 2 | macroeconomics | 宏观经济学 | discipline 明载；现代宏观中的创造性破坏 | 封面、核心页 |
| 3 | monetary economics | 货币经济学 | discipline 明载；博士论文货币动态学 | 早年页 |
| 4 | economic growth | 经济增长 | discipline 明载首项 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 6 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Philippe Aghion | 无向 | 2025 经济学奖共享一半，Aghion–Howitt 模型 |
| co-honored | Joel Mokyr | 无向 | 2025 经济学奖，Mokyr 独得另一半 |
| advisor-student | Robert W. Clower | 师 → 生 | Northwestern 博士导师（1973，正文明载） |
| advisor-student | Roger Farmer | Howitt → 学生 | infobox Doctoral students 明载 |
| advisor-student | Martín Guzmán | Howitt → 学生 | infobox Doctoral students 明载 |
| spouse | Pat Howitt | 无向 | 妻，Howitt 自述其鼓励并支持与 Aghion 的合作 |

**不入库但提示词可叙述**：frontmatter doctoral_advisor 作 John Ledyard，与 page.md 正文及 infobox 的 Robert W. Clower 冲突，**以 page.md 为准（只入 Clower），Ledyard 不入库**（陷阱表裁定）；C. D. Howe Institute 系智库机构关系非个人关系，仅叙述；De Antoni / Leijonhufvud 系纪念 Clower 论文集共同编辑（1999），系一次性编纂活动不入库。

## 五、配色方案 【人物专属】

- **气质**：稳健、过渡、新旧交替的平衡感
- **主色**：`#283593`（manifest 预分配——深靛蓝，与同批 Mokyr/Aghion 同色系，三人群像统一）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGrowth` 内生增长 — 深靛 `#283593`
  - `badgeCreative` 创造性破坏 — 玫瑰红 `#C4204F`
  - `badgeMoney` 货币与宏观 — 钢蓝 `#1E4E79`
  - `badgeCanada` 加拿大学界 — 青绿 `#0E7C7B`
- **背景母题**：摆锤弧线与交替色块（旧范式让位于新范式的往复），呼应设计母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 创造性破坏的另一半 / Peter Howitt 1946– + 四色 badge + 右上头像 + 国籍行（Canada）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地圭尔夫、教育 McGill BA 1968 +
    Western Ontario MA 1969 + Northwestern PhD 1973、任职 Brown、诺奖 2025 半份、核心领域）
03  核心贡献概览 — Aghion–Howitt 模型 / 内生增长 / 创造性破坏 / 货币动态学
04  早年与加拿大求学 (1946–1969) — 圭尔夫出生、McGill 经济学学士、Western Ontario 硕士
05  Northwestern 博士 (1969–1973) — Clower 门下，论文 Studies in the Theory of Monetary Dynamics
06  加拿大执教 (1972–1996) — Western Ontario 二十四年、加拿大经济学会主席 1993–94、
    皇家学会 Fellow 1992
07  南下与 Brown (1996–2013) — Ohio State 1996、Brown 2000、Lyn Crost 教席、2013 荣休
08  获奖理由核心页（★）— 1992 Aghion–Howitt 模型：创造性破坏与持续增长
    （熊彼特机制、企业进入退出、business-stealing，按 Akcigit 转述口径）
09  与 Aghion 的合作 — 1992 奠基论文 / 1998 Endogenous Growth Theory / 2009 The Economics of
    Growth；妻 Pat 对合作的鼓励与支持（page.md 明载）
10  货币经济学一翼 — JMCB 主编 1997–2000、Keynesian Recovery 论文集（1990）
11  政策参与 — C. D. Howe Institute：1986 起发表经济政策报告、2011–15 驻会研究员
12  荣誉与认可 — BBVA Frontiers 2019（与 Aghion）· 皇家学会 Fellow 1992 ·
    Econometric Society Fellow 1994 · Clarivate Citation Laureate · 诺奖 2025
13  门生与传承 — Roger Farmer、Martín Guzmán
14  遗产与结尾 — 熊彼特增长理论的现代格局；结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 拆分理由年份 | 2025 为拆分理由年份：Howitt 与 Aghion **共享一半**（"for the theory of sustained growth through creative destruction"），Mokyr **独得另一半**。两条理由勿混写、勿写成三人共享同一句 |
| 博士导师冲突 | frontmatter 载 John Ledyard，page.md 正文与 infobox 均载 **Robert W. Clower**（1973）→ **以 page.md 为准，只入 Clower**；Ledyard 不入库，Review 勿据 frontmatter 回改 |
| 目录消歧义 | 页面目录为 `Peter_Howitt_economist`（消歧义目录名），yaml/manifest name_en 为 **Peter Howitt**（无后缀）——Beamer 目录照用消歧义名，文案中姓名不带后缀 |
| 同名消歧义页 | Wikipedia 条目 Peter Howitt (economist)，See also 指向消歧义页——立传标题勿写成「Peter Howitt (economist)」字样 |
| 任职时间线 | Western Ontario 执教 **1972–1996**（博士 1973 年获，1972 起已执教，两段时间重叠系 page.md 明载，勿「修正」）；Ohio State 1996 → Brown 2000 → 2013 Professor Emeritus |
| 荣休表述 | Since 2013 Professor **Emeritus** at Brown；Lyn Crost Professor of Social Sciences Emeritus——是荣休教席非现任，勿写成在职 |
| 妻子贡献 | 妻 Pat Howitt「he credits for encouraging and supporting the collaboration with Aghion」——page.md 明载可写，勿演绎为「共同研究者」 |
| BBVA 奖名 | 2019 BBVA Foundation Frontiers of Knowledge Award in Economics, Finance and Management（与 Aghion 共同获得），与 2025 诺奖是两回事 |
| 学派标签 | school or tradition 作 Neo-Schumpeterian economics（新熊彼特传统）——Aghion 篇同款标签，两人篇口径一致 |
| 在世者 | 得主在世，生卒页只写生年 1946-05-31，卒位留白 |
| metadata 噪声 | frontmatter award_received 含 honorary doctor of the University Côte d'Azur（蔚蓝海岸大学荣誉博士），正文未展开——荣誉页如收录须注明仅 frontmatter 有载 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| creative destruction | 创造性破坏 | 获奖理由核心词，熊彼特机制 |
| endogenous growth theory | 内生增长理论 | Aghion–Howitt 模型所属传统 |
| Aghion–Howitt model | 阿吉翁–豪伊特模型 | 两人连字符命名，顺序勿倒 |
| monetary dynamics | 货币动态学 | 博士论文主题，与增长理论分翼 |
| Neo-Schumpeterian economics | 新熊彼特经济学 | 学派标签 |
| Professor Emeritus | 荣休教授 | 2013 起，非在职 |
| fellow-in-residence | 驻会研究员 | C. D. Howe Institute 2011–15 |
| Journal of Money, Credit, and Banking | 《货币、信贷与银行杂志》 | 主编 1997–2000，缩写 JMCB |
| Canadian Economics Association | 加拿大经济学会 | 主席 1993–94 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（manifest 预分配，本批三人均为 PAST）
- **匹配理由**：从货币动态学到熊彼特式增长理论的学术跨越横贯半个世纪——「历史感/深沉」的 PAST 呼应其学脉纵深与加拿大-美国两段学术人生。
- **本地路径**：`music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → 复制为 `economics/presentations/21th_century/Peter_Howitt_economist/PAST.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
- **撞曲提示**：本批 Mokyr / Howitt / Aghion 三人同曲 PAST，出片阶段如需去重由主控统一裁定，本篇按 manifest 值执行。
