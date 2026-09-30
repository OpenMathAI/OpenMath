# 经济学家立传提示词（Elinor Ostrom）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2009 年得主 Elinor Ostrom（埃莉诺·奥斯特罗姆）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Elinor_Ostrom/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Elinor Claire "Lin" Ostrom（本姓 Awan，1933-08-07 生于洛杉矶 ~ 2012-06-12 逝于印第安纳州布卢明顿，享年 78 岁）
- **气质关键词**：**公地治理的田野观察者、多中心秩序的倡导者、经济学诺奖首位女性**
- **诺奖获奖理由**（2009 与 Williamson 共享，本人那条，逐字引用）：
  > "for her analysis of economic governance, especially the commons"（表彰她对经济治理尤其是公共资源的分析）
  > ——共享年份拆分理由：取自 `economics/nobel_economics_citations.json` 2009 年 Elinor Ostrom 条目；中文对照 `economics/economics_list_data.py` 该年 "||" 拆分第一段。
- **设计母题**：**公共地与多中心网络（commons & polycentric networks）**——牧场、渔场、灌溉系统上叠加的多层治理圆环：没有单一中心，而是嵌套互联的小圆构成大秩序，对应八项设计原则与嵌套企业（nested enterprises）。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Elinor_Ostrom/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/21th_century/Elinor_Ostrom/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Elinor_Ostrom_zh`、`VIDEO_NAME=Elinor_Ostrom_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Ostrom 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | common-pool resources | 公共池资源治理 | 《Governing the Commons》，诺奖核心 | 核心页 |
| 1 | polycentric governance | 多中心治理 | 与 Vincent 共同发展的秩序观 | 治理页 |
| 2 | public choice theory | 公共选择理论 | 布卢明顿学派所在传统 | 学派页 |
| 3 | new institutional economics | 新制度经济学 | 制度分析与 IAD 框架 | 框架页 |
| 4 | collective action | 集体行动 | 合作的深层机制 | 机制页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Dwaine Marvick | Marvick → Ostrom | UCLA 政治学博士导师（infobox Doctoral advisor 明载） |
| spouse | Charles Scott | 无向 | 大学毕业后首婚，任职 General Radio 时期，后离异 |
| spouse | Vincent Ostrom | 无向 | 1963 结婚，研究生研讨课导师，一生「爱与论争」的伙伴，1973 共创 Workshop |
| co-honored | Oliver E. Williamson | 无向 | 2009 诺贝尔经济学奖共享（经济治理分析，两人工作各自独立） |
| influence | Garrett Hardin | 无向 | 「公地悲剧」（1968）提出者，Ostrom 理论对话与修正的对象 |

**不入库但提示词可叙述**：Lee Anne Fennell（Ostrom's law 表述者，文献引用）；Kenneth Arrow / Thomas Schelling / Amartya Sen（1998 Seidman 奖讨论人，一次性事件）；Johan Rockström（吊唁与里约对话转述者）；Michael McGinnis / Michael McRobbie（讣闻与捐赠叙述）；无子女（夫妇二人明确无子）。

## 五、配色方案 【人物专属】

- **气质**：深绿田野、牧场的肌理、公共地上的秩序感
- **主色**：`#1E5631`（manifest 预分配；深田野绿——牧场与森林的公共地底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeCPR` 公共池资源 — 深绿 `#1E5631`
  - `badgePoly` 多中心治理 — 靛蓝 `#1E3A5F`
  - `badgeField` 田野方法 — 琥珀 `#C07A2A`
  - `badgeFirst` 首位女性 — 玫瑰 `#A34774`
- **背景母题**：嵌套多中心圆环（大小圆互联无单一核心），呼应多中心治理与嵌套企业原则。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 公地治理的田野观察者 / Elinor Ostrom 1933–2012 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地洛杉矶、教育 UCLA BA 1954 / MA 1962 / PhD 1965、
    导师 Marvick、任职 Indiana 47 年、诺奖 2009、核心领域）
03  核心贡献概览 — 公地悲剧的修正 / 八项设计原则 / IAD 框架 / 多中心治理
04  早年：辩论队里的女孩 (1933–1954) — 大萧条后家庭、Beverly Hills 高中、三年读完 UCLA
05  被经济学博士项目拒之门外的政治学家 — 因无数学背景被 UCLA 经济 PhD 拒收，转政治学
06  西盆地水井战：博士论文 (1960s) — 南加州地下水公地研究，共治的起点
07  布卢明顿岁月 (1965–) — 与 Vincent 同赴 Indiana，1973 共创 Workshop
08  《Governing the Commons》：八项设计原则（核心贡献页）— 西班牙灌溉/瑞士山村/菲律宾梯田/新斯科舍渔场
09  公地悲剧并非宿命 — 对 Hardin 1968 的田野修正：社群自治可持续
10  Ostrom's law 与 SES 框架 — 「实践中可行的资源安排在理论上也可行」
11  2009 诺贝尔奖 — 首位女性经济学奖得主；与 Williamson 各自独立共享；奖金捐给 Workshop
12  至最后的学者 — 2011 确诊胰腺癌仍写作授课，去世当日发表最后一文；Vincent 17 天后随行
13  荣誉与认可 — Skytte 1999 首位女性 · Carty 2004 · NAS 2001 · Time 100 · 雕像与纪念
14  遗产与结尾 — 多中心秩序与公共治理研究的全球网络 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享但独立 | 2009 与 Williamson 是**各自独立工作共享**（Ostrom 经济治理/公地，Williamson 企业边界），勿写成合作研究 |
| 获奖理由 | 官方拆分理由为 Ostrom 个人那条 "for her analysis of economic governance, especially the commons"（her + the commons）；勿用 Williamson 的 "his...boundaries of the firm"，也不合并成一句 |
| 首位女性 | page.md 明载她是**经济学奖首位女性得主**（2009）；1999 Skytte 奖也是该奖首位女性，两个「首位」勿混 |
| 出身学科 | 训练与身份是政治科学家（UCLA 政治学 BA/MA/PhD），经济学博士项目曾拒收她（缺数学）——「经济学家」是事后追认，primary_occupation 按手册取 economist 但提示词必须交代政治学出身 |
| 导师 | 博士导师 Dwaine Marvick 仅 infobox/frontmatter 明载（正文只述 Vincent 的研讨课）；可入库，但勿把 Vincent 写成博士导师——他是研究生研讨课教授+丈夫 |
| 两任丈夫 | 首任 Charles Scott（离异）、第二任 Vincent Ostrom（1963–2012，她去世 17 天后 Vincent 随行）；Vincent 享年 92 |
| 八项设计原则 | 出处是《Governing the Commons》(1990)；引述时保留 page.md 的列表原意，第 8 条 nested enterprises 仅适用于更大系统 |
| 引语红线 | Hardin 理论、Rockström 吊唁、2010 访谈引语均有英文原文可引；中文引号内不得自造「原话」 |
| 捐赠 | 诺奖奖金捐给她参与创办的 Workshop（正文明载其历年多次捐出奖金）——如实呈现，勿写成「全部个人所得」 |
| 死亡细节 | 2011-10 确诊胰腺癌；2012-06-12 6:40 a.m. 逝于 IU Health Bloomington 医院，享年 78；去世当日 Project Syndicate 发表 "Green from the Grassroots" |
| metadata 噪声 | frontmatter 仅单一国籍 United States，与 manifest 一致；生卒无冲突 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| common-pool resources (CPR) | 公共池资源 | 简称 CPR，勿译「公共财产」泛化 |
| tragedy of the commons | 公地悲剧 | Hardin 1968 提出的猜想，Ostrom 修正对象 |
| Governing the Commons | 《公地治理》 | 1990 名著，八项设计原则出处 |
| design principles | （制度）设计原则 | 八条，针对长存续 CPR 制度 |
| polycentric governance | 多中心治理 | 与「去中心化」不同义 |
| IAD framework | 制度分析与发展框架 | 她的机构分析框架 |
| collective action | 集体行动 | 合作机制研究传统 |
| nested enterprises | 嵌套企业 | 第八项原则，多层治理组织 |
| social-ecological systems (SES) | 社会-生态系统 | 晚年综合框架 |
| Ostrom's law | 奥斯特罗姆定律 | Fennell 表述：实践中可行的安排在理论上也可行 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Cinematic Experience**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：纪录片式的大地质感对应其田野方法——从洛杉矶地下水到尼泊尔灌溉、从西班牙牧场到印尼渔场，全球公地的影像志；曲名的电影感也贴合「首位女性」打破天花板的叙事弧线。
- **本地路径**：复制 `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav` 到 `economics/presentations/21th_century/Elinor_Ostrom/CinematicExperience.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
