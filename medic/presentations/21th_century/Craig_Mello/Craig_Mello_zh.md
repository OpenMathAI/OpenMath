# 医学家立传提示词（Craig Mello）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2006 年得主（与 Andrew Fire 共享）。
> 本文件是 Craig Mello 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面，
> 执行方按本提示词产出 15 页 Beamer 立传（本阶段不写 tex，仅沉淀事实与规范）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Craig Cameron Mello（1960-10-18 生于康涅狄格州纽黑文，在世）
- **气质关键词**：**RNA 干扰的共同发现者、餐桌辩论养成的科学家、RNA 治疗学的布道者**
- **诺奖获奖理由（2006，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discovery of RNA interference - gene silencing by double-stranded RNA"
  > （因其发现 RNA 干扰——双链 RNA 引发的基因沉默）——注意 "their"：与 Andrew Fire 共享
- **设计母题**：**对话与争论（the dinner-table argument）**。Mello 自述家庭餐桌辩论塑造了他——
  视觉母题用两段对话气泡交汇成一条双链 RNA 螺旋，象征"争鸣催生发现"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Craig_Mello/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/21th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/21th_century/Craig_Mello/`，数据库写 greatminds 库（MySQL）。

- **第 0 步**：核对本地 page.md 事实基准（本提示词第三、四、七节已沉淀，执行时再逐句复核）
- **第 1 步**：建目录 `medic/presentations/21th_century/Craig_Mello/`（含 `images/`）
- **第 2 步**：复制 Makefile，设 `MAIN=Craig_Mello_zh`、`VIDEO_NAME=Craig_Mello_zh`
- **第 3 步**：收集肖像（infobox 载 Commons 图 "Craig Mello, Davos 2015 - Rewriting Human Genes (cropped).png"，
  优先 Commons Special:FilePath 抓取；404 则装饰圆占位）
- **第 4~9 步**：tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | genetics | 遗传学 | RNA 干扰与基因调控，诺奖核心 | 核心页 |
| 1 | molecular biology | 分子生物学 | dsRNA→mRNA 降解机制 | 核心页 |
| 2 | biochemistry | 生物化学 | Brown 本科 biochemistry & molecular biology 专业出身 | 身份页 |
| 3 | developmental biology | 发育生物学 | Fred Hutchinson 博士后（James Priess 实验室，线虫发育） | 博士后页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Daniel Stinchcomb | 师→生（博士导师） | 哈佛博士导师（先随 David Hirsh 至科罗拉多，后随其转工业界转投 Stinchcomb），1990 博士 |
| advisor-student | Victor Ambros | 师→生 | infobox Academic advisors 明载 |
| advisor-student | James Priess | 师→生（博士后导师） | Fred Hutchinson 癌症研究中心博士后 |
| influence | Stephen J. Gould | 无向 | page.md 明载 "admired and worked with"，受其博物随笔与科学哲学启发 |
| co-honored | Andrew Fire | 无向 | 2006 诺贝尔生理学或医学奖共享（发现 RNA 干扰——双链 RNA 引发的基因沉默） |

> 说明：infobox Academic advisors 另列 Nelson Fausto、Susan Gerbi、Ken Miller、Frank Rothman——
> 除 Ken Miller 为 page.md **正文**明载的 Brown 细胞生物学老师外，其余仅 infobox 有载，**不入库**防噪声。
> Ken Miller 属本科授课老师，也不入 advisor-student（仅可在叙事页提及其"real pain in the ass"轶事——page.md 有载轶事，无引语化处理）。
> Wiley/Massry/Rosenstiel 奖项共同得主（Tuschl/Baulcombe/Ambros/Ruvkun）不入库（co-honored 仅诺奖同届）。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 5。

## 五、配色方案

- **气质**：好奇、善辩、把课堂好奇心做成诺贝尔奖
- **主色**：深青绿 `#145C54`（RNA 世界与亚速尔群岛祖先的海洋绿）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：
  - `badgeRNAi` RNA 干扰 — 冷青 `#0E7C7B`
  - `badgeArgue` 餐桌辩论 — 暖橙 `#E07B30`
  - `badgeThera` RNA 治疗学 — 靛蓝 `#4C5FD5`
  - `badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：对话气泡与短双链片段交错，疏密有致

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover 共享首页）
01  封面 — 争鸣出的发现 / Craig Mello 1960– + 四色 badge + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒/纽黑文出身/教育 Brown BS 1982 + Harvard PhD 1990/任职 UMass/核心领域
03  核心贡献概览 — RNA 干扰 / 1998 Nature 论文 / HHMI / RNAi 产业化
04  亚速尔移民之家 (1960–1982) — 祖父母自亚速尔群岛移民；父 James 古生物学家（耶鲁 1962 PhD、USGS、史密森尼）、母 Sally 艺术家；餐桌辩论传统
05  Brown 时光 (1982) — biochemistry & molecular biology；Ken Miller 回忆其"grade 不最好但好奇心极强"（忠实转述，勿引语化）
06  博士弯路：从科罗拉多到哈佛 (1982–1990) — 先随 David Hirsh（后其转工业界）转 Harvard 续随 Dan Stinchcomb；1990 PhD
07  Fred Hutchinson 博士后 — James Priess 实验室，线虫发育生物学
08  1998 Nature 论文（核心贡献页）— Mello & Fire 与 SiQun Xu、Mary Montgomery、Stephen Kostas、Sam Driver；RNA 小片段诱使细胞销毁基因的 mRNA——关闭特定基因
09  2006 诺贝尔奖 — 理由逐字；凌晨 4:30 半的获奖电话轶事（page.md 明载 HHMI 会议自述，忠实转述）；诺奖演讲 "Return to the RNAi World: Rethinking Gene Expression and Evolution"
10  "fundamental mechanism" — Karolinska 引言（与 Fire 篇同一英文原句）；Nick Hastie 评语（BBC 转引，注明）
11  HHMI 与 UMass — 2000 年起 HHMI investigator；UMass Chan 医学院 RNA 治疗学研究所与分子医学项目教授
12  荣誉与认可 — NAS 分子生物学奖 2003（与 Fire）· Wiley 2003 · Massry 2005 · Gairdner 2005 · Paul Ehrlich 2006 · 首届 Dr. Paul Janssen Award 2006 · Nobel 2006
13  RNAi 走向产业 — RXi Pharmaceuticals 联合创始人（任科学顾问委员会主席）；Beeologics 2010（2011 被 Monsanto 收购）
14  跨界的科学观 — 受 Stephen J. Gould 启发；2015 中国友谊奖演讲 "Science is a unifier..."（page.md 有英文全文，可节引并注明出处语境）；信仰与科学和解的个人立场（一句带过）
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for their discovery of RNA interference - gene silencing by double-stranded RNA"；"their" 表共享 |
| 2 | 博士导师链 | 先在科罗拉多大学博尔德随 **David Hirsh**，Hirsh 转工业界后转哈佛随 **Dan Stinchcomb**，1990 年哈佛博士——两站都要交代，导师入库只写 Stinchcomb（PhD 完成导师） |
| 3 | 1998 论文署名 | 六人合著（Fire、Mello、Xu、Montgomery、Kostas、Driver），勿写成两人论文 |
| 4 | 研究地点分工 | Fire 在卡内基、Mello 在 UMass——page.md 明载两地分工（"conducted at the Carnegie Institution for Science (Fire) and the University of Massachusetts Medical School (Mello)"），勿写反 |
| 5 | 学术导师清单 | infobox 六位 advisors 中只入 Stinchcomb（正文明载 PhD）与 Ambros（infobox）；Fausto/Gerbi/Miller/Rothman 不入库；Ambros 同时是 2024 诺奖得主——如库中另有其记录须用规范名 |
| 6 | Ken Miller 轶事 | "did not receive the best grades of the class" 与 "real pain in the ass" 系 page.md 转述 Miller 回忆，转述时不得加引号装原话 |
| 7 | 中国友谊奖 | 2015 年 10 月自李克强总理领取；演讲英文全文 page.md 有载，节引须注明"2015 中国友谊奖获奖演讲"；政治人物只出现职务性一笔，不展开 |
| 8 | 获奖电话轶事 | HHMI 2006-11-13 会议自述：凌晨 4:30 半、妻子以为是恶作剧——忠实转述即可，勿添油加醋 |
| 9 | Monsanto | Beeologics 2011 年被 Monsanto 收购——事实性一笔，勿做企业评价 |
| 10 | 在世者 | Mello 在世（1960- ）；relations=5 中 3 条师承，诚实值，防 Review 误判"关系太少" |
| 11 | 葡萄牙裔 | 祖父母来自亚速尔群岛（葡萄牙）——文化背景可提，国籍仍按 Nobel 官方口径 United States |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| RNA interference (RNAi) | RNA 干扰 | 与 Fire 共同发现，1998 Nature |
| gene silencing | 基因沉默 | dsRNA 降解匹配 mRNA |
| RNA Therapeutics Institute | RNA 治疗学研究所 | UMass Chan 医学院，Mello 任职机构 |
| HHMI investigator | 休斯医学研究所研究员 | 2000 年起 |
| RXi Pharmaceuticals | RXi 制药 | Mello 联合创办 |
| Caenorhabditis elegans | 秀丽隐杆线虫 | 论文模式生物 |
| Azores | 亚速尔群岛 | 祖源，葡萄牙 |
| China Friendship Award | 中国友谊奖 | 2015，演讲素材来源 |

## 九、背景音乐选择

- **选定曲目**：**Cinematic Experience** — Alex-Productions（manifest 预分配）
- **匹配理由**：Cinematic Experience 的叙事起伏对应本篇最强的故事线——童年餐桌辩论、获奖电话的戏剧性凌晨、
  从线虫到 RNAi 产业的跨界——是本批次最具"电影感"的传记弧线，音乐的画面感与之匹配。
- **备选（未采用）**：Awaken（唤醒感可用但已被多篇占用）、Expedition（探险感偏"地理叙事"，不如本篇的"人生剧场"贴合）
- **本地路径**：`music_audio/` 下 alex-productions 曲库按 curated_tracks.md 对应条目复制为
  `medic/presentations/21th_century/Craig_Mello/Cinematic_Experience.wav`
