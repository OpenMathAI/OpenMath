# 经济学家立传提示词（George Akerlof）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2001 年得主 George Akerlof（乔治·阿克洛夫）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/George_Akerlof/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：George Arthur Akerlof（1940-06-17 生于康涅狄格州纽黑文，在世）
- **气质关键词**：**柠檬市场的诊断者、信息经济学的开路人、新凯恩斯主义的叙事者**
- **诺奖获奖理由**（三人共享，逐字取自 manifest）：
  > "for their analyses of markets with information asymmetry"（表彰他们对信息不对称市场的分析）
- **设计母题**：**柠檬与信息面纱（lemons & the veil of information）**——旧车市场上卖方知道车是「桃」还是「柠檬」而买方不知，劣币驱逐良币；视觉隐喻用「半透明的车体/被面纱遮住一半的市场」：一侧清晰、一侧模糊的双色调构图。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/George_Akerlof/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/George_Akerlof/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=George_Akerlof_zh`、`VIDEO_NAME=George_Akerlof_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库（yaml 在 `MySQL/data/George_Akerlof.yaml`），无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Akerlof 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | information economics | 信息经济学 | 信息不对称市场的分析，诺奖核心 | 核心页 |
| 1 | macroeconomics | 宏观经济学 | 新凯恩斯学派，效率工资与自然规范 | 宏观页 |
| 2 | behavioral economics | 行为经济学 | 2001 诺奖演讲 Behavioral Macroeconomics | 行为页 |
| 3 | labor economics | 劳动经济学 | 效率工资模型（与 Yellen 合著） | 应用页 |
| 4 | identity economics | 身份经济学 | 与 Kranton 开创，社会身份进入经济分析 | 身份页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Solow | Akerlof → 学生 | MIT 博士导师（1966，论文 Wages and Capital） |
| advisor-student | Charles Engel | 学生 | 博士生（infobox 明载） |
| advisor-student | Adriana Kugler | 学生 | 博士生（infobox 明载） |
| co-honored | Joseph Stiglitz | 无向 | 2001 诺贝尔经济学奖三人共享 |
| co-honored | Michael Spence | 无向 | 2001 诺贝尔经济学奖三人共享 |
| spouse | Kay Leong | 无向 | 第一任妻子（1974 结婚 1977 离异），建筑师 |
| spouse | Janet Yellen | 无向 | 1978 结婚，效率工资模型合著者，前美联储主席 |
| parent-child | Robert Akerlof | Akerlof → 子 | 生于 1981，经济学家（Warwick/UNSW 教授） |
| collaborator | Rachel Kranton | 无向 | 身份经济学合著者（Economics and Identity 2000） |
| collaborator | Paul M. Romer | 无向 | 1993 合著 Looting（破产牟利） |
| collaborator | Robert J. Shiller | 无向 | Animal Spirits 2009 与 Phishing for Phools 2015 合著者 |
| influence | John Maynard Keynes | 无向 | infobox Influences 明载 |

**不入库但提示词可叙述**：兄 Carl W. Akerlof（密歇根大学物理教授，兄弟关系无对应类型）；父母 Rosalie Clara Grubber 与 Gösta Carl Åkerlöf（瑞典裔化学家发明家）；Gary Becker（「同为社会经济学奠基人」是并称非直接关系）。

## 五、配色方案 【人物专属】

- **气质**：信息之雾、市场明暗两半、温和的怀疑主义
- **主色**：`#372A75`（manifest 预分配的深紫罗兰——信息面纱后的市场底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeInfo` 信息经济学 — 深紫 `#372A75`
  - `badgeMacro` 新凯恩斯宏观 — 靛蓝 `#16324F`
  - `badgeLabor` 效率工资 — 琥珀 `#C07A2A`
  - `badgeIdent` 身份经济学 — 青绿 `#0E7C7B`
- **背景母题**：半明半暗的圆弧与散落柠檬形色块（同一物体两侧对比度不同），呼应「同一市场因信息分布不同而两副面孔」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 柠檬市场的诊断者 / George Akerlof 1940– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地纽黑文、教育 Yale BA 1962/MIT PhD 1966、
    任职 Berkeley→LSE→Berkeley→Georgetown、诺奖 2001、核心领域）
03  核心贡献概览 — 柠檬市场 / 效率工资 / 身份经济学 / 自然规范宏观
04  早年与家世 (1940–1962) — 纽黑文出生、瑞典裔化学家之父、Lawrenceville 1958、Yale 1962
05  MIT 博士：Solow 门下 (1962–1966) — 论文 Wages and Capital
06  柠檬市场：1970 年被退稿三次的论文（核心贡献页）— QJE 发表、逆向选择、劣币驱逐良币
07  从 ISI 到白宫经济顾问 (1967–1978) — 新德里访学、CEA 1973-74、Fed 1977 遇见 Yellen
08  效率工资与礼物交换 — 与 Yellen 合著、高于出清工资的就业理论
09  生殖技术冲击 — 晚 1970s 对婚外生育的经济学解释（客观简述）
10  Looting：破产牟利 (1993) — 与 Romer 合著、存款保险下的掠夺激励
11  身份经济学 — 与 Kranton、社会规范与身份进入形式化分析（2000/2010）
12  自然规范与宏观 (2007 AEA 主席演讲) — 用社会规范解释宏观异象
13  与 Yellen 的双人叙事 — 华盛顿双人线（Berkeley/LSE/Brookings），家庭与学术交织
14  遗产与结尾 — 信息经济学三巨头之一 + 结尾页（品牌 OpenMathAI）
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | manifest/官方口径为 "for their analyses of markets with information asymmetry"；page.md 引言句作 "markets with asymmetric information"，展示以 manifest 官方句为准，勿混写 |
| 三人共享不是同题 | Akerlof=逆向选择（柠檬市场）、Spence=信号传递、Stiglitz=筛选，三人各答信息不对称的一环，页面上须各写各的核心词，勿写成"三人共同提出同一模型" |
| 国籍口径 | yaml 按 manifest/维基表格口径填 United States；正文称 American，无歧义 |
| 兄长不入库 | Carl W. Akerlof 是物理学家兄长，兄弟关系无对应类型，仅叙述 |
| 首任妻子 | Kay Leong 建筑师（1974-1977），与 Janet Yellen 两行 spouse 并存，勿合并或遗漏 |
| 儿子 Robert | 生于 1981 的经济学家（Yale 2003/Harvard PhD 2009/Warwick/UNSW），可入库 parent-child；勿与任何同名学者混淆 |
| 政治内容禁写 | Political views 节（2024 诺奖得主公开信、对 Trump 政策批评）与 External links 中 Bush 批评文章一律禁写，遵守项目政治敏感红线 |
| 判定"Berkeley 拒升"语气 | page.md 明载 1977 年 Berkeley 未予正教授晋升、遂赴 LSE——按事实客观陈述，勿加"不公"等评价 |
| 名字拼写 | 本人规范名 George Akerlof（manifest 形式）；父 Gösta Carl Åkerlöf 带变音符，勿混用 |
| frontmatter 噪声 | metadata.json award_received 含 Fisher-Schultz Lecture 等，以正文与 infobox 为准；生卒日期无双值噪声 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| information asymmetry | 信息不对称 | 获奖理由核心词，勿简写为"信息不对称性" |
| adverse selection | 逆向选择 | 柠檬市场的机制，勿与道德风险混淆 |
| The Market for Lemons | 柠檬市场 | 1970 QJE 论文，"柠檬"=劣质旧车 |
| efficiency wages | 效率工资 | 高于市场出清水平的工资，与 Yellen 合著 |
| gift-exchange game | 礼物交换博弈 | 效率工资的人类学解释 |
| identity economics | 身份经济学 | 与 Kranton 共创 |
| reproductive technology shock | 生殖技术冲击 | Akerlof 自创术语，带引号呈现 |
| looting / bankruptcy for profit | 破产牟利 | 与 Romer 1993 |
| natural norms | 自然规范 | 2007 AEA 主席演讲概念 |
| New Keynesian economics | 新凯恩斯经济学 | infobox School or tradition |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：海面的开阔与雾中的航船贴合「信息面纱下的市场」——柠檬市场讲的正是买家在看不见的水域航行；曲名的平静感也匹配 Akerlof 叙事化、温和而非对抗的学术气质（2001 三人共享奖同曲，属批次内撞曲，出片阶段由主控统一协调）。
- **本地路径**：复制 `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` 到 `economics/presentations/21th_century/George_Akerlof/SEA.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
