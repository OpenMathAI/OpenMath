# 经济学家立传提示词（Dale T. Mortensen）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2010 年得主 Dale T. Mortensen（戴尔·莫滕森）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Dale_T._Mortensen/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Dale Thomas Mortensen（1939-02-02 生于俄勒冈州企业镇 Enterprise ~ 2014-01-09 逝于伊利诺伊州威尔米特，享年 74 岁）
- **气质关键词**：**摩擦性失业的破译者、搜寻匹配理论的先行者、DMP 模型的 M**
- **诺奖获奖理由**（2010 三人共享，逐字引用）：
  > "for their analysis of markets with search frictions"（表彰他们对存在搜寻摩擦的市场的分析）
- **设计母题**：**摩擦与流动（friction & turnover）**——劳动力市场上岗位与工人的双向搜寻带、相遇与分离的往复：横向流动带上的相遇节点与断裂节点交替，构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Dale_T._Mortensen/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/21th_century/Dale_T._Mortensen/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Dale_T._Mortensen_zh`、`VIDEO_NAME=Dale_T._Mortensen_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Mortensen 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | labour economics | 劳动经济学 | infobox Discipline，搜寻匹配理论所在领域 | 核心页 |
| 1 | search and matching theory | 搜寻匹配理论 | DMP 模型的 M，摩擦性失业分析 | 核心页 |
| 2 | macroeconomics | 宏观经济学 | 失业动态与职位流动 | 宏观页 |
| 3 | economic theory | 经济理论 | 匹配博弈与讨价还价（1982 论文） | 理论页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Michael C. Lovell | Lovell → Mortensen | 卡内基梅隆博士导师（1967 论文，infobox Doctoral advisor 明载） |
| advisor-student | Ronald G. Ehrenberg | Mortensen → Ehrenberg | 博士生（infobox Doctoral students 明载），劳动经济学名家 |
| colleague | Christopher A. Pissarides | 无向 | 1994 合著《Job Creation and Job Destruction in the Theory of Unemployment》+2005 IZA 劳动经济学奖共同获得 |
| co-honored | Christopher A. Pissarides | 无向 | 2010 诺贝尔经济学奖三人共享（搜寻摩擦市场分析） |
| co-honored | Peter Diamond | 无向 | 2010 诺贝尔经济学奖三人共享（搜寻摩擦市场分析） |
| spouse | Beverly Mortensen | 无向 | 西北大学教授，正文明载 |

**不入库但提示词可叙述**：E. Nagypál / K. Burdett（合著论文作者，文献合作不建边）；E. Phelps（1972 论文集主编，文献关系）；Aarhus 大学 Niels Bohr 访问教授（职务非关系）；家属捐赠诺奖奖章予西北大学（事件）。

## 五、配色方案 【人物专属】

- **气质**：西北深蓝、中西部平原的沉静、失业搜寻的冷峻
- **主色**：`#1E6B52`（manifest 预分配，与同届 Pissarides 一致；蓝绿——搜寻场的冷暖交叠）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeSearch` 搜寻匹配 — 深绿 `#1E6B52`
  - `badgeDMP` DMP 模型 — 靛蓝 `#1E3A5F`
  - `badgeTurn` 劳动力流动 — 玫瑰 `#A63A2B`
  - `badgeMidwest` 中西部学统 — 琥珀 `#C07A2A`
- **背景母题**：双向搜寻流动带（相遇与断裂节点交替的横向流线），呼应劳动力市场流动（turnover）。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 摩擦性失业的破译者 / Dale T. Mortensen 1939–2014 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地 Enterprise、教育 Willamette BA 1961 /
    Carnegie Mellon PhD 1967、导师 Lovell、任职 Northwestern 1965–、诺奖 2010、核心领域）
03  核心贡献概览 — 搜寻匹配理论 / DMP 模型 / 职位流动 / 匹配博弈
04  从俄勒冈到匹兹堡 (1939–1967) — Enterprise 出身、Willamette 学士、卡内基梅隆博士（永久收入假说的宏观含义）
05  西北岁月 (1965–) — 执教西北大学、1980 起 Kellogg 管理经济与决策科学教授
06  搜寻理论先行（核心贡献页一）— 1970 论文集章节《A theory of wage and employment dynamics》
07  匹配博弈与财产权 (1982) — 「交配、竞赛与相关游戏的效率」、讨价还价框架
08  1994 论文：职位的创造与毁灭（核心贡献页二）— 与 Pissarides 合著、劳动力流动模型
09  工资离散之谜 — 1998 Burdett-Mortensen、专著《Wage Dispersion》（2005）
10  2010 诺贝尔奖 — 与 Diamond、Pissarides 三人共享；诺奖演讲《Markets with Search Frictions and the DMP Model》
11  奥胡斯之缘 — Niels Bohr 访问教授（2006–2010）、Dale T. Mortensen 大楼与 Dale's Café
12  荣誉与认可 — Henderson Award 1965 · Econometric Society Fellow 1979 · AAAS Fellow 2000 · IZA 2005
13  告别 — 2014-01-09 逝于肺癌四期（享年 74）；2019 家属向西北大学捐出诺奖奖章
14  遗产与结尾 — DMP 成为动态宏观劳动经济学的标准件 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方 citation "for their analysis of markets with search frictions"（三人共享同句）；勿添加 Diamond 的「奠基」分工叙事——本 page.md 未载分工 |
| DMP 命名 | 模型缩写 D=Diamond、M=Mortensen、P=Pissarides；DMP 是学界通称但本 page.md 仅在诺奖演讲标题处出现（"the DMP Model"），可放心使用该处口径 |
| 双边关系 | 与 Pissarides 同时存在 colleague（1994 合著+IZA 2005 共同获奖）与 co-honored（2010 诺奖）两行，为合法双行，勿去重 |
| 导师与学生 | 导师 Michael C. Lovell、学生 Ronald G. Ehrenberg 均 infobox 明载可入库；E. Nagypál 等合著者不入库 |
| 出生地名 | Enterprise, Oregon——镇名直译「企业镇」，图注写英文原名 + 俄勒冈州，勿意译 |
| IZA 年份 | IZA Prize in Labor Economics 2005（与 Pissarides 共同）；诺奖 2010——两个共享荣誉年份勿混 |
| 去世细节 | 2014-01-09 逝于威尔米特家中，肺癌四期（stage 4），享年 74；安葬 Skokie 纪念公园墓园——病名可写但措辞克制 |
| 奖章捐赠 | 2019 年家属将其诺奖奖章捐赠西北大学——如实呈现事件即可 |
| 卒后荣誉 | 2011-05 母校 Willamette 荣誉博士、2011-02 奥胡斯大学 Dale T. Mortensen 大楼命名（在世时）；年份顺序勿倒 |
| metadata 噪声 | metadata.json 无卒日冲突（1939-02-02 / 2014-01-09 与正文一致）；educated_at 含 Tepper School（CMU 商学院）与 Willamette，正常 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| search frictions | 搜寻摩擦 | 获奖理由核心词 |
| search and matching theory | 搜寻匹配理论 | 其开创性贡献 |
| DMP model | DMP 模型 | 诺奖演讲标题口径 "the DMP Model" |
| frictional unemployment | 摩擦性失业 | 与周期性失业区分 |
| job creation / job destruction | 职位创造 / 职位毁灭 | 1994 论文双主题 |
| labor turnover | 劳动力流动 | 其研究延伸方向 |
| wage dispersion | 工资离散 | 1998 论文与 2005 专著主题 |
| matching function | 匹配函数 | 共同奠基的建模工具（Pissarides 侧多写） |
| bargaining game | 讨价还价博弈 | 1982 论文框架 |
| Review of Economic Dynamics | 《动态经济学评论》 | 其创办期刊之一（founding editor） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome**（manifest 预分配，与同届 Pissarides 共用；音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：与 Pissarides 共享同曲；对 Mortensen 而言，「Lonesome」的克制低回对应其半个世纪在搜寻与摩擦话题上的深耕——把失业者「寻找」的孤独过程写进标准理论模型。
- **本地路径**：复制 `music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav` 到 `economics/presentations/21th_century/Dale_T._Mortensen/Lonesome.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
