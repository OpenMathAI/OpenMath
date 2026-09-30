# 经济学家立传提示词（Ben Bernanke）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2022 年得主 Ben Bernanke（本·伯南克）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Ben_Bernanke/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Ben Shalom Bernanke（1953-12-13 生于美国佐治亚州奥古斯塔，在世，卒年留白）
- **气质关键词**：**大萧条的学生、美联储第 14 任主席、金融危机中的救火队长**
- **诺奖获奖理由**（2022 三人共享，逐字引自 manifest/nobel_economics_citations.json）：
  > "for research on banks and financial crises"（表彰他们关于银行与金融危机的研究）
  > ——Bernanke 本人条目的具体落点：对**大萧条**的分析（银行挤兑如何使危机深重而漫长）。
- **设计母题**：**银行挤兑与灭火（bank run & firefighting）**——排队提款的长龙与一正一反的资金流曲线，是「流动性枯竭-信心崩溃」的视觉隐喻；结尾可用与 Geithner/Paulson 合著《Firefighting》的"救火"意象呼应。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Ben_Bernanke/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Ben_Bernanke/`（含 page.md / page.html / metadata.json / images.txt，肖像取 images.txt 或 Commons `Special:FilePath`，page.md 引用 2008 官方肖像）；Makefile 复制后设 `MAIN=Ben_Bernanke_zh`、`VIDEO_NAME=Ben_Bernanke_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Bernanke 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | macroeconomics | 宏观经济学 | infobox Discipline 明载；两本宏观教科书 | 封面、核心页 |
| 1 | monetary economics | 货币经济学 | LSE 货币理论与政策讲座、NBER 货币经济学项目主任 | 货币页 |
| 2 | banking and financial crises | 银行与金融危机 | 2022 诺奖获奖理由核心；金融加速器 | 核心页 |
| 3 | economic history | 经济史（大萧条） | 1983 AER 论文与《Essays on the Great Depression》 | 大萧条页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Stanley Fischer | Fischer → Bernanke | MIT 博士导师（论文 "Long Term Commitments, Dynamic Optimization, and the Business Cycle"，1979）；后任以色列央行行长 |
| co-honored | Douglas Diamond | 无向 | 2022 诺贝尔经济学奖三人共享："for research on banks and financial crises" |
| co-honored | Philip H. Dybvig | 无向 | 2022 诺贝尔经济学奖三人共享："for research on banks and financial crises" |
| spouse | Anna Friedmann | 无向 | 小学教师，1978-05-29 结婚 |
| influence | Milton Friedman | Friedman → Bernanke | 大萧条货币主义解释的主要来源；Bernanke 多次引用并在其 90 岁生日演讲致意 |
| influence | Anna Schwartz | Schwartz → Bernanke | Friedman 合著者；Bernanke 降息至零的决策曾援引二人研究（Schwartz 本人对伯南克有批评，见陷阱表） |

**不入库但提示词可叙述**：论文评阅人 Irwin S. Bernstein / Rüdiger Dornbusch / Robert Solow / Peter Diamond / Dale Jorgenson（评阅角色非导师）；Mark Gertler（挚友、NYU 经济系主任，"friend" 关系无标准类型）；教科书合著者 Andrew Abel / Robert H. Frank / Dean Croushore（仅书目合著）；Janet Yellen / Alan Greenspan（职务继任/前任非关系类型）；子女 Joel 与 Alyssa（仅具名）；《Firefighting》合著者 Timothy Geithner 与 Henry Paulson（合著书目+危机同事，正文无持续关系叙述，控制噪声）。

## 五、配色方案 【人物专属】

- **气质**：沉稳、镇定、危机中的学术定力
- **主色**：`#123C5B`（manifest 预分配——美联储深蓝）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeMacro` 宏观经济学 — 美联储深蓝 `#123C5B`
  - `badgeDepression` 大萧条研究 — 灰紫 `#52307C`
  - `badgeBank` 银行与金融危机 — 琥珀 `#C07A2A`
  - `badgeFed` 美联储岁月 — 青绿 `#0E7C7B`
- **背景母题**：下沉与回弹的资金曲线（流动性枯竭-政策回注的双色曲线），呼应「金融加速器与救火」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 大萧条的学生 / Ben Bernanke 1953– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（1953-12-13 生于 Augusta、Dillon 长大、Harvard AB 1975、
    MIT PhD 1979、美联储主席 2006–2014、Brookings 特聘研究员、诺奖 2022、核心领域）
03  核心贡献概览 — 大萧条中的银行挤兑 / 金融加速器 / 伯南克学说与大缓和 / 危机中的美联储
04  迪伦少年 (1953–1971) — 南卡 Dillon 药剂师之子；毕业演说代表；无微积分课自学微积分；SAT 1590；
    1965 全美拼字比赛参赛者
05  哈佛与 MIT (1971–1979) — Harvard AB summa cum laude（Phi Beta Kappa）1975；MIT PhD 1979（导师 Stanley Fischer）
06  学界岁月 (1979–2002) — Stanford GSB 1979–85、NYU 访问、Princeton 终身教授并任经济系主任 1996–2002
07  大萧条：银行挤兑的非货币效应（核心贡献页）— 1983 AER 论文：1930–33 金融动荡降低信贷配置效率、
    抬高信贷成本压抑总需求
08  金融加速器 — 温和衰退中银行收缩信贷的恶性循环；DeLong 注：2008 危机使该理论更具现实意义
09  从学者到官员 (2002–2006) — 美联储理事、伯南克学说（通缩防范）、大缓和、2005–06 总统经济顾问委员会主席
10  美联储主席 (2006–2014) — 2006-02-01 就任；两任期；2010 参议院 70–30 连任确认
11  2008 金融危机与非常规措施 — 联邦基金利率 5.25%→0%；2008-11 至 2010-06 创造 1.3 万亿美元量化宽松；
    Time 2009 年度人物
12  争议与辩护 — Merrill Lynch 合并、AIG 救助与 Edward Quince 化名事件（客观并列：国会作证 "I never said
    anything about firing the board and the management"）
13  2022 诺贝尔经济学奖 — 与 Diamond、Dybvig 共享；瑞典科学院口径：银行在经济中的角色、避免银行倒闭为何重要、
    伯南克对大萧条的分析
14  遗产与结尾 — Brookings/Citadel/PIMCO 岁月、《21 世纪货币政策》+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由拆分 | 2022 官方理由只有一句 "for research on banks and financial crises"（manifest 直接给出，**非拆分年份**）；Bernanke 的具体落点是大萧条分析——引用框写全句，正文落点句另述 |
| 政治内容红线 | 公职任命（Bush 提名、Obama 连任）只作时间线客观陈述；党派变化（共和党→2015 无党派）一句客观带过；**不做任何政治评价** |
| 争议节口径 | Merrill Lynch/AIG/Edward Quince 三事按 page.md 客观并列：指控方、伯南克证词与否认均呈现，不单侧叙事；引语只用 page.md 原文 |
| 引语红线 | 可引原文：弗里德曼 90 岁生日演讲 "You're right. We did it. We're very sorry. But thanks to you, we won't do it again."；印钞机演讲 "The U.S. government has a technology, called a printing press..."；国会证词 "I never said anything about firing the board and the management"；Obama 评价 "the epitome of calm"。其余叙述不加引号 |
| 名字拼写 | 名是 **Ben**（非 Benjamin），中间名 Ben Shalom 不缩写（page.md 脚注明载） |
| Friedman 双向 | Friedman/Schwartz 是思想影响者（influence 入库）；但 Anna Schwartz 本人曾公开撰文反对伯南克连任——influence 边与后来的批评并存，提示词如实分述 |
| 双职位年份 | 美联储理事 2002-07-31~2005-06-21、主席 2006-02-01~2014-01-31、CEA 主席 2005-06-21~2006-01-31——三个时间窗勿互换 |
| 确认票数 | 第二任期参议院 70–30（当时该职位最窄Margin），先 77–23 结束辩论——两组数字勿混 |
| 量化宽松数字 | 2008-11 至 2010-06 创造 1.3 万亿美元购买金融资产——数字唯一出处，勿放大 |
| 学位 | Harvard AB+AM（1975），MIT PhD（1979）；Dillon High 无微积分课、自学微积分是趣闻亮点 |
| 大缓和大命名 | "the Great Moderation" 是伯南克 2004-02-20 演讲首提（正文载），"saving glut" 2005 提出——两概念勿合并 |
| 在世留白 | 1953 生、在世；幻灯片年份写 "1953–" |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| financial accelerator | 金融加速器 | 伯南克提出的信贷放大机制 |
| bank run | 银行挤兑 | 与 Diamond–Dybvig 模型呼应，两人模型勿记在伯南克名下 |
| Great Depression | 大萧条 | 获奖落点；勿与 Great Recession（大衰退，2008）混淆 |
| Great Moderation | 大缓和 | 2004 演讲提出的周期波动下降理论 |
| Bernanke doctrine | 伯南克学说 | 2002 通缩防范演讲（怎么防通缩） |
| quantitative easing | 量化宽松 | 2008-11 起的非常规措施 |
| helicopter drop | 直升机撒钱 | 借用弗里德曼说法；"Helicopter Ben" 是批评者绰号 |
| saving glut | 储蓄过剩 | 2005 提出的全球储蓄压低利率假说 |
| deflation | 通货紧缩 | 2002 演讲主题 |
| Federal Reserve / the Fed | 美联储 | 主席任期两段 2006–2014 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Empire Collapse**（主控分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「帝国崩塌」的宏大暗流贴合伯南克的两重叙事——学术上研究 1930–33 银行体系如何把衰退拖成大萧条，实务上亲历 2008 金融体系濒临崩塌的至暗时刻；曲风的沉稳张力匹配"救火队长"在崩塌边缘稳住金融帝国的形象。
- **本地路径**：复制 `music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav` 到 `economics/presentations/21th_century/Ben_Bernanke/EmpireCollapse.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Ben_Bernanke/page.md` | ★ 事实基准（唯一事实来源） |
| `economics/presentations/pages/21th_century/Ben_Bernanke/metadata.json` | QID/生卒/国籍结构化参考（冲突以 page.md 为准） |
| `economics/presentations/pages/21th_century/Ben_Bernanke/images.txt` | 肖像候选 URL（2008 官方肖像） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 共享封面（`\input`） |
| `MySQL/data/Ben_Bernanke.yaml` | 社会关系/研究领域入库存档（本批次已入库） |
| `economics/nobel_economics_citations.json` | 2022 获奖理由英文原文（Bernanke 条目） |

## 十一、执行清单（供 Beamer agent 核对） 【模板通用】

1. 核对事实基准：所有事实与 page.md 逐条对照，冲突一律以 page.md 为准并在陷阱表记录裁定。
2. 复制 Makefile：`MAIN=Ben_Bernanke_zh`、`VIDEO_NAME=Ben_Bernanke_zh`。
3. 肖像：优先 images.txt 真实肖像（2008 官方肖像）；404 则装饰圆占位。
4. 配色：主色 `#123C5B` + badge 四色 + 背景母题（下沉与回弹的资金曲线）。
5. 幻灯片序列：按第六节 15 页规划，第 02 页身份信息页必做。
6. 编译循环：`make distclean && make`，0 error、vbox ≤ 10pt、hbox ≤ 50pt；pdftoppm 逐页目检。
7. 引语红线：只有第七节列出的四处 page.md 原文可入引文框（引原文+译文）。
8. 政治敏感红线：公职任命客观陈述、争议节双侧呈现、零政治评价；主语聚焦「学者与央行家」身份。
9. 结尾页品牌口径：底部标注 `OpenMathAI`，引号用半角 " "。
10. 完成后 `make images && make video` 产出 mp4，向主控汇报页数与体积。

## 十二、版式补遗 【模板通用】

- **共享封面**：第 00 页 `\input` OpenEcon 统一封面，子 deck 不重复 GitHub 链接。
- **封面页**：主标题字号沿用模板；badge 主字体 scriptsize、副行 `\fontsize{6.5}{7.8}`；右上肖像细边框 + 姓名小字注。
- **身份信息页**：左头像 + 右信息网格，含至少生卒/出生地/教育/师承/任职/主要荣誉/核心领域七要素。
- **表格页安全负间距**：顶部 -0.35cm、`arraystretch 0.78-0.82`；公职时间窗建议三行小表。
- **时间线页**：`\foreach` 分隔符必须 ASCII 逗号；勿给 foreach 节点套 tikz style。
- **获奖理由引用框**：英文原句 + 中文翻译两行制，英文逐字 "for research on banks and financial crises"。

## 十三、关键时间线速查 【人物专属】

| 年份 | 事件（均出自 page.md） |
|------|------|
| 1953-12-13 | 生于佐治亚州奥古斯塔；在南卡 Dillon 东 Jeff 街长大（犹太家庭） |
| 1965 | 参加第 38 届全美拼字比赛 |
| 高中 | Dillon High 毕业演说代表；自学微积分；SAT 1590；National Merit Scholar |
| 1971 | 入 Harvard College（Winthrop House） |
| 1975 | Harvard AB（economics, summa cum laude, Phi Beta Kappa）+ AM |
| 1978 | 与小学教师 Anna Friedmann 结婚（1978-05-29） |
| 1979 | MIT 经济学博士（导师 Stanley Fischer；评阅含 Solow、Peter Diamond、Dornbusch、Jorgenson） |
| 1979–1985 | Stanford GSB 任教；1985 迁新泽西 Montgomery Township |
| 1985–2002 | 普林斯顿大学（1996 起任经济系主任至 2002-09 公共服务假） |
| 2002–2005 | 美联储理事；2002-11 伯南克学说演讲；2004-02 大缓和演讲 |
| 2005–2006 | 总统经济顾问委员会第 23 任主席 |
| 2006-02-01 – 2014-01-31 | 美联储第 14 任主席（历经 Bush/Obama 两任总统） |
| 2008–2010 | 金融危机应对：利率降至 0%、量化宽松 1.3 万亿美元 |
| 2009 | Time 年度人物；家乡 I-95 出口命名 Ben Bernanke Interchange |
| 2010-01-28 | 参议院 70–30 确认连任 |
| 2014-02-03 | 卸任（继任 Janet Yellen）；转任 Brookings 特聘研究员 |
| 2015 | 《The Courage to Act》；任 Citadel 与 PIMCO 顾问 |
| 2020 / 2021 | BBVA Frontiers of Knowledge Award / 当选 NAS 院士 |
| 2022-10-10 | 诺贝尔经济学奖（与 Diamond、Dybvig 共享） |
| 2022 | 《21st Century Monetary Policy》出版 |

> 表内每条均有 page.md 明载；争议事件（Merrill/AIG/Quince）不入时间线速查表，仅在第 12 页客观呈现。
