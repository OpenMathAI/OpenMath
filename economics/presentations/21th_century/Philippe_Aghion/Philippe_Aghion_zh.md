# 经济学家立传提示词（Philippe Aghion）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2025 年得主（与 Peter Howitt 共享一半）Philippe Aghion（菲利普·阿吉翁）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Philippe_Aghion/page.md`，与其冲突时以 page.md 为准；`metadata.json` 仅作结构化参考。

## 一、背景信息 【人物专属】

- **目标经济学家**：Philippe Mario Aghion（1956-08-17 生于巴黎，在世）
- **气质关键词**：**创造性破坏的理论家、熊彼特增长模型的缔造者、法兰西公学院讲席教授** —— Collège de France 经济制度创新与增长讲席教授、INSEAD Kurt Björklund 创新与增长讲席教授、LSE 访问教授
- **诺奖获奖理由**（2025 年经济学奖**与 Peter Howitt 共享一半**；拆分理由年份，逐字引自 `economics/nobel_economics_citations.json` 2025 年 Philippe Aghion 条目；中文对照 `economics/economics_list_data.py` 2025 年 `||` 拆分第二段）：
  > "for the theory of sustained growth through creative destruction"（表彰他们关于通过创造性破坏实现持续增长的理论）
  > 另一半由 Joel Mokyr 独得（理由为识别技术进步实现持续增长的前提条件，勿混写）。
- **设计母题**：**创造性破坏（creative destruction）**——新事物破土而出的裂变意象：一半是完好几何、一半是碎裂重生的分裂图形，喻示创新使旧技术过时的「business-stealing」机制。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Philippe_Aghion/page.md`（同目录 `metadata.json` 仅作参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Philippe_Aghion/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取——page.md 明载 2015 年 2 月 Boston University 照片可用，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Philippe_Aghion_zh`、`VIDEO_NAME=Philippe_Aghion_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Aghion 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | endogenous growth theory | 内生增长理论 | 1992 与 Howitt 奠基性模型，诺奖核心 | 核心页 |
| 1 | creative destruction | 创造性破坏 | 熊彼特机制，获奖理由核心词 | 核心页 |
| 2 | innovation economics | 创新经济学 | discipline 明载首项；创新与竞争 | 封面、核心页 |
| 3 | competition and growth | 竞争与增长 | 2000s 倒 U 型关系；2006 专著 | 研究页 |
| 4 | contract theory | 契约理论 | discipline 明载 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 8 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Peter Howitt | 无向 | 2025 经济学奖共享一半，Aghion–Howitt 模型 |
| co-honored | Joel Mokyr | 无向 | 2025 经济学奖，Mokyr 独得另一半 |
| parent-child | Gaby Aghion | Gaby Aghion → 子 | 母，时装品牌 Chloé 创始人 |
| parent-child | Raymond Aghion | Raymond Aghion → 子 | 父，圣日耳曼大道画廊主 |
| colleague | Rachel Griffith | 无向 | 2006 合著 Competition and Growth |
| colleague | Steven N. Durlauf | 无向 | 2005 合编 Handbook of Economic Growth |
| colleague | Celine Antonin | 无向 | 2021 合著 The Power of Creative Destruction |
| colleague | Simon Bunel | 无向 | 2021 合著 The Power of Creative Destruction |

**不入库但提示词可叙述**：frontmatter doctoral_advisor（Yves Balasko / Jerry Green / Eric Maskin）系 metadata-only，page.md 正文仅言 Harvard PhD 1987 未载导师名，**禁建边**（陷阱表裁定）；Ufuk Akcigit 系 page.md 转述其评述（"According to Ufuk Akcigit..."），非合作关系；Ban Ki-moon / Hollande / Zuma / Pécresse / Pangestu / Pazarbasioglu / Stern / Macron 均系机构任职、政策咨询或政治场合人物，非学术关系且涉政治内容，一律不建边；父母双方埃及亚历山大犹太家庭背景仅作身世叙述。

## 五、配色方案 【人物专属】

- **气质**：锋利、现代、破坏与重建的张力
- **主色**：`#283593`（manifest 预分配——深靛蓝，与同批 Mokyr/Howitt 同色系，三人群像统一）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGrowth` 内生增长 — 深靛 `#283593`
  - `badgeCreative` 创造性破坏 — 玫瑰红 `#C4204F`
  - `badgeCompete` 竞争与增长 — 钢蓝 `#1E4E79`
  - `badgePolicy` 政策与机构 — 琥珀 `#C07A2A`
- **背景母题**：分裂-重生几何（一半完好/一半碎裂重排的色块），呼应创造性破坏的设计母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 创造性破坏的增长理论家 / Philippe Aghion 1956– + 四色 badge + 右上头像 + 国籍行（France）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地巴黎、教育 ENS Cachan 数学部 +
    Paris 1 DEA/D3C + Harvard PhD 1987、任职 Collège de France/INSEAD/LSE、诺奖 2025 半份）
03  核心贡献概览 — Aghion–Howitt 模型 / 创造性破坏 / 竞争与创新倒 U / 中等收入陷阱
04  早年与家世 (1956–) — 母 Gaby Aghion（Chloé 创始人、prêt-à-porter 一词据称出自其口）、
    父 Raymond 画廊主、亚历山大犹太家庭、艺术家环境（Lagerfeld 仅一句）
05  法国数理经济训练 — ENS Cachan 数学部、Paris 1 DEA 与第三阶段博士（数理经济学）
06  Harvard PhD 与 MIT 起点 (1987–1989) — 1987 博士、MIT assistant professor
07  回流法国与 EBRD (1989–1996) — CNRS 研究员、EBRD 副首席经济学家、Nuffield/UCL
08  获奖理由核心页（★）— 1992 Aghion–Howitt 模型：创新使旧技术过时（business-stealing）、
    租金为胡萝卜/创造性破坏为大棒的企业进入退出动力学（按 Akcigit 转述口径）
09  竞争、制度与增长 (2000s) — 竞争强度与创新强度的倒 U 型关系
10  中等收入陷阱 — 资本积累与模仿驱动的追赶临近技术前沿而受限
11  Aghion Report (2010) — 大学自治国际比较、balanced governance 双治理机构建议（交 Pécresse）
12  Collège de France 与 INSEAD (2015– ) — 法兰西公学院讲席（法国学界崇高地位）、
    INSEAD 讲席、创新经济实验室学术主任
13  荣誉与认可 — BBVA Frontiers 2019（与 Howitt）· CNRS 银奖 · John von Neumann Award ·
    Yrjö Jahnsson Award · 荣誉军团骑士 2012 · 国家功勋军官 2018 · AAAS Fellow 2009 · EEA 主席 2017
14  遗产与结尾 — 熊彼特增长理论的现代格局；结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 拆分理由年份 | 2025 为拆分理由年份：Aghion 与 Howitt **共享一半**（"for the theory of sustained growth through creative destruction"），Mokyr **独得另一半**（识别技术进步实现持续增长的前提条件）。两条理由勿混写、勿写成三人共享同一句 |
| 博士导师 metadata-only | frontmatter 载 Yves Balasko / Jerry Green / Eric Maskin，但 page.md 正文只写「Harvard PhD in economics 1987」未载任何导师名 → **不入库**（禁建边）；叙述亦不展开 |
| 政治内容红线 | page.md 载 2012 年支持 Hollande 联署、2017 支持 Macron、学生时代共产主义同情者、Hollande/Zuma 共同主持的 UN 专家组——**政治人物与选举内容立传一律禁写**；Aghion Report 仅写报告本身（对象是大学治理），不写政绩评价 |
| 引语红线 | Akcigit 对模型的转述（"revolutionized the analysis..."）系 page.md 叙述文本非直接引语，按叙述口径转述；AOC Media 批评（techno-optimism）可一句客观提及，不展开不评价 |
| 母亲名言 | Gaby "is said to have coined" prêt-à-porter——用「据称/被认为」，勿写成断言 |
| 技术前沿红链 | page.md 中 Technology frontier 为红链接，叙述写「技术前沿」概念即可，勿当作既定术语展开 |
| 任职链 | MIT 1987 → CNRS 1989 → EBRD 副首席经济学家 1990 → Nuffield → UCL 1996 → Harvard Waggoner 讲席 2002–2015 → LSE Centennial 2015 + Collège de France 讲席 2015 → INSEAD 2020——时间线密集，勿合并年份 |
| EEA vs EHA | Aghion 是 **European** Economic Association 主席 2017（勿与 Mokyr 的 Economic History Association 主席 2002–03 混淆） |
| BBVA 奖名 | 2019 BBVA Foundation Frontiers of Knowledge Award in Economics, Finance and Management（与 Howitt 共同获得），与 2025 诺奖是两回事 |
| 在世者 | 得主在世，生卒页只写生年 1956-08-17，卒位留白 |
| 姓氏拼写 | infobox 表头误拼 Phillipe，正文与 frontmatter 均作 Philippe——以正文为准 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| creative destruction | 创造性破坏 | 获奖理由核心词，熊彼特机制 |
| endogenous growth theory | 内生增长理论 | 1992 模型所属传统 |
| Aghion–Howitt model | 阿吉翁–豪伊特模型 | 两人连字符命名，顺序勿倒 |
| business-stealing effect | 抢生意效应 | 创新使旧技术过时的机制表述 |
| inverted-U relationship | 倒 U 型关系 | 竞争强度与创新 |
| middle-income trap | 中等收入陷阱 | 新兴经济体赶超受限概念 |
| Schumpeterian | 熊彼特式的 | school or tradition 明载 |
| Collège de France | 法兰西公学院 | 机构专名，勿译「法兰西学院」泛称 |
| statutory chair | 法定讲席 | 法国公学院讲席性质表述 |
| prêt-à-porter | 成衣（ready-to-wear） | 母亲「据称」创用词 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（manifest 预分配，本批三人均为 PAST）
- **匹配理由**：创造性破坏理论回望熊彼特百年遗产——「历史感/深沉」的 PAST 与从 1992 模型到 2025 诺奖三十余年理论积淀的叙事相配。
- **本地路径**：`music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → 复制为 `economics/presentations/21th_century/Philippe_Aghion/PAST.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
- **撞曲提示**：本批 Mokyr / Howitt / Aghion 三人同曲 PAST，出片阶段如需去重由主控统一裁定，本篇按 manifest 值执行。
