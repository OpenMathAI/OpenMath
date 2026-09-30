# 经济学家立传提示词（Richard Thaler）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2017 年得主 Richard Thaler（理查德·塞勒）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Richard_Thaler/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Richard H. Thaler（1945-09-12 生于美国新泽西州东奥兰治，在世，卒年留白）
- **气质关键词**：**行为经济学的拓荒者、助推的设计师、让经济学"更像人"的异见者**
- **诺奖获奖理由**（2017 独得，逐字引自 manifest / `economics/nobel_economics_citations.json`）：
  > "for his contributions to behavioural economics"（表彰他对行为经济学的贡献）
- **设计母题**：**助推与选择架构（nudge & choice architecture）**——默认选项悄然改变行为而保留自由；以滑槽/路径分岔与被轻推的圆点构成背景母题，隐喻"自由家长制"（libertarian paternalism）。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Richard_Thaler/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Richard_Thaler/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Richard_Thaler_zh`、`VIDEO_NAME=Richard_Thaler_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Thaler 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | behavioral economics | 行为经济学 | 2017 诺奖核心 | 封面、核心页 |
| 1 | behavioral finance | 行为金融 | infobox Fields 明载；De Bondt 合作过度反应等 | 金融页 |
| 2 | nudge theory | 助推理论 | 与 Sunstein 合创 choice architecture 概念 | 助推页 |
| 3 | mental accounting | 心理账户 | Thaler 提出的标志性概念 | 核心页 |
| 4 | decision-making | 决策研究 | 有限理性/社会偏好/缺乏自制三支柱 | 理论页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 9 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Sherwin Rosen | Rosen → 导师 | Rochester 博士导师（1974），生命价值市场估计论文 |
| collaborator | Daniel Kahneman | 无向 | 1977–78 斯坦福合作研究，提供禀赋效应等理论框架 |
| collaborator | Amos Tversky | 无向 | 1977–78 斯坦福合作研究（同上） |
| collaborator | Cass Sunstein | 无向 | 合著 Nudge（2008/2021），合创 choice architecture 术语 |
| collaborator | Shlomo Benartzi | 无向 | 合著短视性损失厌恶与股权溢价之谜（1995） |
| collaborator | Hersh Shefrin | 无向 | 自我控制 planner-doer 双系统模型合著（诺奖表彰提及） |
| colleague | Robert Shiller | 无向 | NBER 行为经济学项目共同主任（1991–2015） |
| colleague | Russell Fuller | 无向 | 1993 合创 Fuller & Thaler 资管公司 |
| spouse | France Leclerc | 无向 | 妻，前芝加哥大学营销学教授、摄影家 |

**不入库但提示词可叙述**：Richard Rosett（"曾受教于系主任"，酒类购买习惯成为其研究素材——非正式师承不入库）；父母 Roslyn 与 Alan Maurice Thaler（父母身份叙述，不建 parent-child 双边时无职业关系载体——按"仅 page.md 明载父母职业叙述、人物库边不建"裁定不建，因其父职业仅一句叙述）；前三子未具名不入库；Selena Gomez / Steven Levitt（媒体与播客一次性事件）不入库。

## 五、配色方案 【人物专属】

- **气质**：诙谐、反叛、温和的颠覆感
- **主色**：`#5B2A86`（助推紫——manifest 预分配；紫色的"心理感"对应行为经济学对理性人假设的柔性颠覆）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeBehav` 行为经济学 — 紫 `#5B2A86`
  - `badgeNudge` 助推与选择架构 — 青绿 `#0E7C7B`
  - `badgeFin` 行为金融 — 琥珀 `#C07A2A`
  - `badgeMental` 心理账户 — 靛蓝 `#37474F`
- **背景母题**：滑槽与分岔路径上被轻推的小圆点（默认选项的力量），呼应「不禁止任何选项、只改变呈现方式」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 行为经济学的拓荒者 / Richard H. Thaler 1945– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地东奥兰治、教育 Case Western BA 1967 /
    Rochester MA 1970 / PhD 1974、师承 Sherwin Rosen、任职 Chicago Booth、诺奖 2017、核心领域）
03  核心贡献概览 — 禀赋效应 / 心理账户 / 短视性损失厌恶 / 助推与自由家长制
04  早年与教育 (1945–1974) — 新泽西东奥兰治、犹太家庭（父为 Prudential 精算师）、
    Case Western BA 1967、Rochester MA 1970 / PhD 1974
05  Rochester 博士与 Rosett 的启发 (1974–1977) — Rosen 门下论文 The Value of Saving a Life；
    系主任 Rosett 的买酒习惯成为研究素材
06  斯坦福一年：遇见 Kahneman 与 Tversky (1977–1978) — 合作研究、为经济异象找到理论框架（禀赋效应）
07  康奈尔岁月 (1978–1995) — SC Johnson 商学院、1989 创立行为经济学与决策研究中心任首任主任、
    JEP「Anomalies」专栏（1987–1990）
08  禀赋效应与心理账户（核心贡献页）— 拥有即高估；「心理账户」概念：钱的来源改变花钱方式
09  短视性损失厌恶与股权溢价之谜（核心贡献页，与 Benartzi 1995）
10  助推与自由家长制（核心贡献页，与 Sunstein）— Nudge（2008/2021 终版含 sludge 章）、
    默认选项：退休储蓄 ~90% 参与率、器官捐献「prompted choice」立场
11  芝加哥 Booth 与应用 — 1995 起执教、Walgreen 讲席、AEA 主席 2015、Fuller & Thaler 资管（1993）、
    NBER 行为经济学项目（与 Shiller 1991–2015）、英国 Behavioural Insights Team 参与建立
12  自我控制与两系统模型 — 与 Shefrin 的 planner-doer 模型：调和 Adam Smith 两股传统的
    「deep tension」（颁奖词明载）
13  荣誉与认可 — Nobel 2017 · NAS 院士 2018 · AAAS 院士 · 2017-12-08 诺奖演讲
    From Cashews to Nudges · 《大空头》客串与 Erdős–Bacon 数 5
14  遗产与结尾 — 行为经济学从异端到主流的格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生日双值 | frontmatter date_of_birth 有 1945-09-12 / 1945-12-09 两值；以 infobox 与正文一致口径 **1945-09-12** 为准，yaml 填 09-12，陷阱表注记 |
| 获奖独得 | 2017 独得（非共享）；理由 "for his contributions to behavioural economics" 为本人一条，勿写成共享 |
| 姓名规范 | name_en 用 manifest 形式 `Richard Thaler`（目录同）；正文全名 Richard H. Thaler 可在封面副题使用 |
| Kahneman/Tversky 关系 | page.md 明载 1977–78 斯坦福「collaborating and researching」——入 collaborator 边；勿写"师从"或"导师" |
| Rosett 不入库 | "studied under departmental chair Richard Rosett" 是非正式受教叙述，非学位导师——不入 advisor-student，仅在早年页叙述 |
| 颁奖现场引语 | Per Strömberg 评语（self-control 工作 "finally liberated Adam Smith"）与 Peter Gärdenfors 评语 "made economics more human" 均为 page.md 原文英文，引用时须英文原文+译文，不得改写为中文"原话" |
| Thaler 本人引语 | "as irrationally as possible"（花钱计划玩笑）与 "economic agents are human..." 为 page.md 明载原话，可入引文框（英中对照）；碳税播客长段对话仅客观转述、不整段照录 |
| Krugman/Shiller 评语 | Krugman 推文正面、Shiller 提及部分经济学家质疑——两说并列客观呈现，勿单侧化 |
| 政治内容红线 | 碳税话题涉美国两党立场：只客观记录 Thaler 支持碳税的事实与瑞典例证，不评价任何政党；Nudge 涉政府项目清单（Race to the Top 等）仅作概念背景不展开 |
| 书名与年份 | Nudge 初版 2008（Yale UP）、更新版 2009、终版 2021（删章节+增 sludge）；Misbehaving 2015；The Winner's Curse 1992——版本年份勿互串 |
| metadata 噪声 | metadata.json 无实质冲突；frontmatter doctoral_advisor 与 infobox/正文一致（Sherwin Rosen） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| behavioral economics | 行为经济学 | 获奖理由核心词 |
| endowment effect | 禀赋效应 | 拥有即高估，勿译"捐赠效应" |
| mental accounting | 心理账户 | Thaler 标志性概念 |
| myopic loss aversion | 短视性损失厌恶 | 与 Benartzi 1995 合著 |
| equity premium puzzle | 股权溢价之谜 | MLA 解释对象 |
| nudge | 助推 | 与 Sunstein 合创概念 |
| choice architecture | 选择架构 | Thaler 与 Sunstein 合创术语 |
| libertarian paternalism | 自由家长制 | 勿带褒贬色彩直译呈现 |
| sludge | 污渍/摩擦（助推的反面） | 2021 终版新增章，勿写成"淤泥" |
| planner-doer model | 计划者-执行者模型 | 与 Shefrin 合著的自我控制模型 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Winds Of Freedom**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：助推的核心承诺是"不剥夺自由的前提下让人过得更好"——「自由之风」的意象正对应 libertarian paternalism 中"自由"的那一半；曲风的昂扬感也贴合从异端到 AEA 主席的叙事弧线。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `economics/presentations/21th_century/Richard_Thaler/WindsOfFreedom.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Richard_Thaler/page.md` | ★ 唯一事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 统一首页模板 |
| `MySQL/data/Richard_Thaler.yaml` | 入库 yaml（已执行） |
| `economics/nobel_economics_citations.json` | 获奖理由英文原文 |

## 十一、执行清单 【模板通用】

1. 读本提示词 + page.md 建立事实基准；2. 下载肖像（250px 改 500px，Commons 404 则装饰圆占位）；3. 复制 Makefile 设 `MAIN=Richard_Thaler_zh`；4. 按 §六写 15 页 Beamer；5. `make distclean && make` 编译循环（0 error、vbox≤10pt、hbox≤50pt）；6. pdftoppm 逐页目检；7. 两轮 Review；8. DB `has_biography` 置 1。

## 十二、版式补遗 【模板通用】

- 表格页安全负间距：顶部 -0.35cm、arraystretch 0.78-0.82；公式框前 -0.35~-0.55cm。
- 时间线 `\foreach` 分隔符必须 ASCII 逗号；文本模式希腊字母须数学模式；宏名禁数字。
- 引语框：英文原文+译文（citation 与 page.md 明载引语）；半角引号；品牌口径 `OpenMathAI`。
