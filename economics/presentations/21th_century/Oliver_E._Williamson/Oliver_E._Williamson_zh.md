# 经济学家立传提示词（Oliver E. Williamson）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2009 年得主 Oliver E. Williamson（奥利弗·威廉姆森）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Oliver_E._Williamson/page.md`，与其冲突时以 page.md 为准。
> ★ 数据库备注：库内已有记录 id=1408（db_social=0），本批 seed_person 幂等 UPD 回填 qid，不新建。

## 一、背景信息 【人物专属】

- **目标经济学家**：Oliver Eaton Williamson（1932-09-27 生于威斯康星州苏必利尔 ~ 2020-05-21 逝于加州伯克利，享年 87 岁）
- **气质关键词**：**交易成本经济学的集大成者、企业边界的测绘者、新制度经济学的中坚**
- **诺奖获奖理由**（2009 与 Ostrom 共享，本人那条，逐字引用）：
  > "for his analysis of economic governance, especially the boundaries of the firm"（表彰他对经济治理尤其是企业边界的分析）
  > ——共享年份拆分理由：取自 `economics/nobel_economics_citations.json` 2009 年 Oliver E. Williamson 条目；中文对照 `economics/economics_list_data.py` 该年 "||" 拆分第二段。
- **设计母题**：**企业与市场的边界（boundaries of the firm）**——市场圆点群与科层树状结构之间一条可移动的分界线：交易费用决定活动落入哪一侧，分界线的呼吸式伸缩构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Oliver_E._Williamson/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/21th_century/Oliver_E._Williamson/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Oliver_E._Williamson_zh`、`VIDEO_NAME=Oliver_E._Williamson_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Williamson 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | transaction cost economics | 交易成本经济学 | 核心贡献：交易属性与治理结构匹配 | 核心页 |
| 1 | theory of the firm | 企业理论 | 企业边界的治理结构观 | 核心页 |
| 2 | new institutional economics | 新制度经济学 | 学派归属（infobox School 明载） | 学派页 |
| 3 | industrial organization | 产业组织 | 《Markets and Hierarchies》的反托拉斯应用 | 应用页 |
| 4 | law and economics | 法与经济学 | Yale 时期创办 JLEO | 期刊页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Richard Cyert | Cyert → Williamson | 卡内基梅隆博士导师（1963 论文，infobox+正文明载） |
| advisor-student | Ronald Coase | Coase → Williamson | 正文「A student of Ronald Coase」明载；交易成本思想源头 |
| advisor-student | Herbert A. Simon | Simon → Williamson | 正文「A student of Herbert A. Simon」明载；有限理性思想来源 |
| influence | Kenneth Arrow | 无向 | infobox Influences 明载 |
| influence | Chester Barnard | 无向 | infobox Influences 明载；组织理论来源 |
| influence | Friedrich Hayek | 无向 | infobox Influences 明载 |
| influence | Ian Roderick Macneil | 无向 | infobox Influences 明载；关系性契约理论 |
| influence | John R. Commons | 无向 | infobox Influences 明载；制度经济学先驱 |
| co-honored | Elinor Ostrom | 无向 | 2009 诺贝尔经济学奖共享（经济治理分析，两人工作各自独立） |
| spouse | Dolores Celini | 无向 | 1957 年华盛顿特区相识，育有五名子女（子女不具名不入库） |

**不入库但提示词可叙述**：五名子女（不具名）；Paul L. Joskow（实证检验其交易成本理论的论文作者，文献关系）；BBC 转述的颁奖理由（paraphrase，非官方原文）；Haas 商学院 Williamson Award 历届得主（纪念奖项受方，非本人关系）。

## 五、配色方案 【人物专属】

- **气质**：厚重的制度感、契约的经纬、科层的秩序
- **主色**：`#1E5631`（manifest 预分配，与同届 Ostrom 一致；深绿——制度的生长底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeTCE` 交易成本 — 深绿 `#1E5631`
  - `badgeFirm` 企业边界 — 靛蓝 `#1E3A5F`
  - `badgeLaw` 法与经济学 — 玫瑰 `#A63A2B`
  - `badgeHist` 卡内基传统 — 琥珀 `#C07A2A`
- **背景母题**：市场（离散圆点）与科层（树状结构）之间的可移动分界线，呼应「治理结构的选择」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 交易成本经济学的集大成者 / Oliver E. Williamson 1932–2020 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地苏必利尔、教育 MIT BS 1955 / Stanford MBA 1960 /
    CMU PhD 1963、任职 Berkeley/Pennsylvania/Yale、诺奖 2009、核心领域）
03  核心贡献概览 — 交易成本 / 企业边界 / 治理结构 / 信息受制
04  工程师起点 (1932–1963) — 苏必利尔教师之子、Ripon+MIT 双注册、GE 项目工程师与 CIA 工作经历
05  卡内基岁月：三重师承 — Cyert 导师 + Coase/Simon 思想浸润，1963 论文《The Economics of Discretionary Behaviour》
06  从 Penn 到 Yale 到 Berkeley (1965–1988) — Yale 创办 JLEO、1988 起 Berkeley Edgar F. Kaiser 讲座教授
07  交易成本经济学（核心贡献页一）— 现货议价 vs 关系专用契约，重复交易的经济逻辑
08  企业边界：治理结构观（核心贡献页二）— 反对「企业只是契约联结」的视角
09  信息受制与机会主义 — information impactedness、有限理性+机会主义双前提
10  实证回响 — Joskow 1987 煤炭契约研究等对交易成本理论的检验
11  2009 诺贝尔奖 — 与 Ostrom 各自独立共享（企业边界 vs 公地治理）；2009-12-08 诺奖演讲《Transaction Cost Economics: The Natural Progression》
12  至暗与告别 — 2020-05-21 逝于伯克利；Nobel Museum 陈列的烟斗架
13  荣誉与认可 — von Neumann Award 1999 · NAS 1994 · Distinguished Fellow 2007 · 荣誉博士群
14  遗产与结尾 — 不完全契约理论的思想源头之一；Haas Williamson Award + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享但独立 | 2009 与 Ostrom 各自独立工作共享（Williamson 企业边界、Ostrom 公地治理），勿写成合作 |
| 获奖理由 | 官方拆分理由为本人那条 "for his analysis of economic governance, especially the boundaries of the firm"（his + boundaries of the firm）；BBC 转述句（firms as structures for conflict resolution）是 paraphrase，引文框只用官方原文 |
| 三重师承 | 正文原句 "A student of Ronald Coase, Herbert A. Simon and Richard Cyert"——三人**并列**入库 advisor-student，勿只写 Cyert；Coase 是思想师承（未任其正式导师）须在 note 写明出处口径 |
| 学位路径 | BS 管理学 MIT Sloan 1955（Ripon College+MIT 双注册）→ MBA Stanford 1960 → PhD Carnegie Mellon 1963；三段学位勿混年份 |
| 任职顺序 | Berkeley 助教 1963–65 → Penn 教授 1965–83 → Yale Gordon B. Tweedy 讲座教授 1983–88（创办 JLEO）→ Berkeley 1988 起；勿倒置 |
| 自我定位 | 其自述 "a blend of soft social science and abstract economic theory"（软社会科学与抽象经济理论的混合）可引原文 |
| 前一年撞名 | 2007 得主 Oliver Hart 同为「契约/企业理论」名家，两人研究方向相关但**并非同一人**，幻灯片中不可混写 |
| 师承对手方 | Herbert A. Simon 用库内记录 'Herbert A. Simon'（#223，图灵奖侧已入库）；Kenneth Arrow 用库内 #2639；John R. Commons 用库内 #1403——勿新建分裂 stub |
| 不完全契约 | 正文说该进路 "is partly based on the work of Williamson and Coase"——写「思想源头之一」，勿写成创始人 |
| metadata 噪声 | metadata.json educated_at 含 Superior High School 与 Tepper School（CMU 商学院别名），正常；生卒 1932-09-27 / 2020-05-21 与正文一致 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| transaction cost | 交易成本 | 核心词，Coase 1937 传统 |
| transaction cost economics | 交易成本经济学 | 简称 TCE，其体系化成果 |
| boundaries of the firm | 企业边界 | 获奖理由关键词 |
| governance structure | 治理结构 | 交易与制度的匹配框架 |
| opportunism | 机会主义 | 行为假设之一，勿译贬义泛化 |
| bounded rationality | 有限理性 | 承自 Simon 的行为假设 |
| information impactedness | 信息受制 | 其创造的术语，信息获取不平等状况 |
| relationship-specific contract | 关系专用契约 | 与现货议价相对 |
| Markets and Hierarchies | 《市场与科层》 | 1975 代表作 |
| The Economic Institutions of Capitalism | 《资本主义经济制度》 | 1985 代表作 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Cinematic Experience**（manifest 预分配，与同届 Ostrom 共用；音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：2009 两篇共享同曲；对 Williamson 而言，曲名的宏大叙事感对应其「从工程师到制度理论家」的漫长弧线——半个世纪把交易成本从直觉打磨成体系。
- **本地路径**：复制 `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav` 到 `economics/presentations/21th_century/Oliver_E._Williamson/CinematicExperience.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
