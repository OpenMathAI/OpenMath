# 经济学家立传提示词（James Heckman）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **2000 年得主 James Heckman（詹姆斯·赫克曼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/James_Heckman/page.md`，与其冲突时以 page.md 为准（metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：James Joseph Heckman（1944-04-19 生于伊利诺伊州芝加哥，**在世**，卒年留白）
- **气质关键词**：**选择性样本的矫正者、微观计量的工程师、人力资本的 counted** —— 2000 年诺贝尔经济学奖获奖理由（本人那条，逐字引自 `economics/nobel_economics_citations.json` 2000 年 James Heckman 条目）：
  > "for his development of theory and methods for analyzing selective samples"（表彰他发展了分析选择性样本的理论与方法）
  —— 2000 年为拆分理由年份，与 Daniel McFadden 共享（McFadden 那条为 "…analyzing discrete choice"），两人理由分立，勿混用。
- **设计母题**：**筛与滤（selection sieve）**——社会科学能观测到的样本永远是「被筛选后的样本」：求职者自选择进入劳动力市场、个体自选择进入培训项目。Heckman correction 的本质是把「看不见的筛选过程」重新纳入模型。视觉隐喻：错落的筛网/漏斗层叠，实心圆代表被观测样本、虚线圆代表被筛除的不可观测部分，二者共同决定落点分布。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/James_Heckman/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/James_Heckman/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=James_Heckman_zh`、`VIDEO_NAME=James_Heckman_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Heckman 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 计量经济学 | Heckman correction 所在，诺奖核心 | 封面、核心页 |
| 1 | microeconomics | 微观经济学 | infobox Discipline 明载 | 核心页 |
| 2 | labor economics | 劳动经济学 | 实证研究主阵地（供给、培训、教育回报） | 劳动页 |
| 3 | human capital | 人力资本 | CEHD 中心纲领、政策评估对象 | 人力资本页 |
| 4 | early childhood education | 早期儿童教育 | 效果评估与生命周期技能形成 | 教育页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Stanley W. Black | 师→生（博士导师） | 普林斯顿博士导师（1971），正文明载 |
| advisor-student | Harry H. Kelejian | 师→生（博士导师） | infobox Doctoral advisors 明载（红链人物） |
| influence | Albert Rees | 无向 | infobox Influences 明载 |
| influence | Gary S. Becker | 无向 | infobox Influences 明载，芝大传统 |
| influence | Jacob Mincer | 无向 | infobox Influences 明载，劳动经济学 |
| co-honored | Daniel McFadden | 无向 | 2000 年共享诺贝尔经济学奖（本人理由 selective samples） |
| spouse | Lynne Pettler-Heckman | 无向 | 社会学家，1979 结婚，2017-07-08 去世 |
| collaborator | Alan Krueger | 无向 | 合著《Inequality in America: What Role for Human Capital Policy?》 |
| collaborator | Edward Leamer | 无向 | 合编《Handbook of Econometrics》第 5/6A/6B 卷 |
| advisor-student | Carolyn Heinrich | Heckman → 学生 | 博士生（infobox 明载） |
| advisor-student | George Borjas | Heckman → 学生 | 博士生（infobox 明载） |
| advisor-student | Petra Todd | Heckman → 学生 | 博士生（infobox 明载） |
| advisor-student | Stephen Cameron | Heckman → 学生 | 博士生（infobox 明载） |
| advisor-student | Mark Rosenzweig (economist) | Heckman → 学生 | 博士生（infobox 明载），发展经济学家 |
| advisor-student | Russ Roberts | Heckman → 学生 | 博士生（infobox 明载） |

**不入库但提示词可叙述**：两名子女（page.md 未具名）；正文另提的博士生群体（"over 70 students" 总数）；Carmen Pages、John Eric Humphries、Tim Kautz、R. Nelson、L. Cabatingan 等其余合著/合编者（只入最显著的 Krueger 专著与 Leamer Handbook 两条，其余仅叙述，防止关系表噪声）；Henry Schultz 讲席教授名号（得名于人名，非师承）；Becker Friedman Institute（机构非个人）。

## 五、配色方案 【人物专属】

- **气质**：严谨、工程感、在噪声中重建因果
- **主色**：`#283593`（manifest 预分配靛蓝——计量工具的冷峻理性）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeSel` 选择性样本 / Heckman correction — 靛蓝 `#283593`
  - `badgeLab` 劳动经济学 — 琥珀 `#C07A2A`
  - `badgeEdu` 人力资本与儿童教育 — 青绿 `#0E7C7B`
  - `badgePol` 政策评估 — 深紫 `#52307C`
- **背景母题**：层叠筛网与实/虚双态圆点（被观测样本 vs 被筛除样本），呼应「分析选择性样本」的获奖理由与第一节设计母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 选择性样本的矫正者 / James Heckman 1944– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1944-04-19 芝加哥、科罗拉多学院数学 BA 1965、
    普林斯顿经济学 PhD 1971、任职芝加哥大学 Henry Schultz 讲席教授、诺奖 2000、核心领域）
03  核心贡献概览 — Heckman correction / 选择偏差与自选择 / 劳动经济学实证 / 早期儿童教育
04  早年：芝加哥与数学本科 (1944–1965) — 父 John Jacob Heckman、母 Bernice Irene Medley；
    Colorado College 数学学士 1965
05  普林斯顿博士 (1965–1971) — 论文 Three Essays on the Supply of Labor and the Demand for Goods，
    Stanley W. Black 指导
06  哥伦比亚到芝加哥 (1973–) — 哥伦比亚助理教授 → 1973 转芝大；Henry Schultz 讲席教授、
    法学院教授、Harris 公共政策学院、CEHD 主任（2014–）、NBER
07  Heckman correction：把筛选纳入模型（核心贡献页）— 选择偏差与自选择、选择性样本分析，
    诺奖理由对应
08  劳动经济学实证 — 教育回报、在职培训、劳动力市场分选、积极劳动市场政策的无效性
09  早期儿童教育与人力资本 (CEHD) — 生命周期技能形成、新社会实验与旧实验再分析、
    Heckman Equation、Pritzker Consortium
10  政策评估与因果 — 《1964 年民权法案》对非裔经济进步的因果效应（客观转述）、
    GED 研究全美关注、高中辍学率上升、IQ 仅解释 1–2% 而 conscientiousness 致富
11  荣誉页 — Clark Medal 1983 · Nobel 2000 · Frisch Medal 2014 · Dan David Prize 2016 ·
    Econometric Society 前主席 · NAS / 美国哲学学会 / AAAS；RePEc 2024-06 全球第三大影响力经济学家
12  门生与传承 — 70 余名博士生：Carolyn Heinrich、George Borjas、Petra Todd、
    Stephen Cameron、Mark Rosenzweig、Russ Roberts
13  合著与个人生活 — 与 Krueger/Leamer 等的专著与手册；1979 与社会学家 Lynne Pettler-Heckman
    结婚（2017 去世）、育二子；诺奖演讲 2000-12-08 Microdata, Heterogeneity and the Evaluation of Public Policy
14  遗产与结尾 — 从选择性样本到全生命周期人力资本经济学 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 拆分理由年份 | 2000 年共享但理由分立：本人为 "for his development of theory and methods for analyzing selective samples"，McFadden 为 "…analyzing discrete choice"；中文对照 `economics_list_data.py` 2000 年 "||" 拆分段（Heckman 在前），逐字使用，勿写共享整句 |
| 博士导师口径 | metadata.json 写 Stanley W. Black + Albert Rees；**page.md infobox 导师为 Harry H. Kelejian + Stanley Warren Black**，Rees/Becker/Mincer 列在 Influences——以 page.md 为准：Black 与 Kelejian 入 advisor-student，Rees 入 influence；正文只点名 Black 指导 |
| Kelejian 红链 | Harry H. Kelejian 是红链人物（无独立维基条目），但 infobox Doctoral advisors 明载，照常入库建边 |
| 学生名单 | metadata.json 列 30 名博士生过宽；**只收 page.md infobox 6 人**（Heinrich/Borjas/Todd/Cameron/Rosenzweig/Roberts），其余 metadata-only 一律不入库 |
| 在世留白 | Heckman 1944 年生、在世；卒年/享年栏留白，全文勿出现卒年 |
| Henry Schultz 讲席 | "Henry Schultz Distinguished Service Professor" 是为纪念经济学家 Henry Schultz 命名的讲席教授职衔，非师承关系，禁建 advisor-student 边 |
| RePEc 口径 | "third-most influential economist in the world" 是 "As of June 2024" 的时点口径，写明时间，勿写成永久排名 |
| IQ 表述 | "a high IQ only improved … by 1 or 2%" 与 conscientiousness（勤勉、毅力与自律）致胜的对比是 page.md 明载结论，按原文口径转述，勿加工成「读书无用论」 |
| 民权法案 | 《1964 年民权法案》促进非裔经济进步的强因果效应是其实证结论，客观转述研究结论即可，不展开政治评价 |
| 子女不具名 | "They had two children" 无姓名，不入库也不具名叙述 |
| 合著者取舍 | 只入 Krueger（专著合著）与 Leamer（Handbook 合编）两条 collaborator；Carmen Pages 等其余合著者仅叙述，防关系表噪声 |
| metadata 噪声 | metadata doctoral_student 含 "Mark Rosenzweig (economist)" 消歧义形式，yaml/库内对手方沿用该形式防与同名心理学家分裂；Borjas 用 infobox 形式 "George Borjas" |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Heckman correction | 赫克曼修正 | 获奖理由对应的核心方法，勿译「海克曼」 |
| selection bias | 选择偏差 | 与 self-selection（自选择）区分 |
| selective samples | 选择性样本 | 本人 citation 关键词，勿写成 "selected samples" |
| discrete choice | 离散选择 | McFadden 那条 citation 关键词，勿安到 Heckman 头上 |
| unobserved heterogeneity | 不可观测异质性 | 其方法论关键词（页面链接名） |
| human capital | 人力资本 | CEHD 与政策评估纲领核心词 |
| early childhood education | 早期儿童教育 | 后期研究重心，勿与普通教育经济学混同 |
| GED | GED 证书（同等学历证书） | 1990s 初全国关注的序列研究，勿展开展开美国制度细节 |
| John Bates Clark Medal | 约翰·贝茨·克拉克奖章 | 1983 年获，勿与诺奖年份混 |
| Frisch Medal | 弗里施奖章 | 2014 年获，得名于首届诺奖得主 Ragnar Frisch，勿与本奖混淆 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：选择性样本研究的本质是「唤醒」——把被筛除、看不见的不可观测部分重新唤回模型；从被忽略的数据中唤醒因果结构，正是 Heckman correction 的智力姿态。「Awaken」的推进感也贴合其从计量工具到全生命周期人力资本经济学的持续开拓。
- **本地路径**：复制 `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` 到 `economics/presentations/20th_century/James_Heckman/Awaken.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
