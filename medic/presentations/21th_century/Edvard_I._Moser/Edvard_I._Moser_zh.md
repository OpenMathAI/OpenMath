# 医学家立传提示词（Edvard Moser）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2014 年得主（与 May-Britt Moser 共享一半；另一半归 John O'Keefe）。
> 本文件是 Edvard Moser 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面，
> 执行方按本提示词产出 15 页 Beamer 立传（本阶段不写 tex，仅沉淀事实与规范）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Edvard Ingjald Moser（1962-04-27 生于挪威奥勒松，在世）
- **气质关键词**：**网格细胞的共同发现者、大脑 GPS 系统的总工程师、三代卓越中心的建造者**
- **诺奖获奖理由（2014，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discoveries of cells that constitute a positioning system in the brain"
  > （因其发现构成大脑定位系统的细胞）——注意共享结构：Moser 夫妇共享一半，另一半归 O'Keefe
- **设计母题**：**坐标系（coordinate system）**。网格细胞给大脑以度量与坐标，2018 年又发现时间坐标——
  视觉母题用空间菱格与一条时间轴正交叠加，象征"空间与时间在大脑中的双重测绘"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Edvard_I._Moser/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/21th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/21th_century/Edvard_I._Moser/`，数据库写 greatminds 库（MySQL）。

- **第 0 步**：核对本地 page.md 事实基准（本提示词第三、四、七节已沉淀，执行时再逐句复核）
- **第 1 步**：建目录 `medic/presentations/21th_century/Edvard_I._Moser/`（含 `images/`）
- **第 2 步**：复制 Makefile，设 `MAIN=Edvard_I_Moser_zh`、`VIDEO_NAME=Edvard_I_Moser_zh`（宏名禁点号）
- **第 3 步**：收集肖像（page.md 无 infobox 肖像 URL 时用 Commons Special:FilePath 回退，404 则装饰圆占位）
- **第 4~9 步**：tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuroscience | 神经科学 | 网格细胞/边界细胞/定位系统，诺奖核心 | 核心页 |
| 1 | psychology | 心理学 | 奥斯陆 cand.psychol.（1990）出身 | 身份页 |
| 2 | neurophysiology | 神经生理学 | 1995 dr.philos. 学位科目 | 教育页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Per Andersen | 师→生 | 奥斯陆时期在其指导下工作（dr.philos. 神经生理学 1995） |
| advisor-student | Richard G. Morris | 师→生（博士后导师） | 爱丁堡大学神经科学中心博士后（1995–1997） |
| colleague | John O'Keefe (neuroscientist) | 无向 | 曾为 UCL 其实验室访问博士后（两月）；page.md 称其 "previous mentor" |
| co-honored | John O'Keefe (neuroscientist) | 无向 | 2014 诺贝尔生理学或医学奖共享（发现构成大脑定位系统的细胞） |
| spouse | May-Britt Moser | 无向 | 1985 结婚，2016 宣布离婚，科研合作持续 |
| co-honored | May-Britt Moser | 无向 | 2014 诺贝尔生理学或医学奖共享（发现构成大脑定位系统的细胞） |
| advisor-student | Marianne Fyhn | Edvard Moser→学生 | infobox Doctoral students 明载 |

> 说明：relations=7（行数）。夫妇互指 spouse+co-honored 双行（同对异型并存，参照库内先例）。
> O'Keefe 关系按 page.md "long-term collaborator and then-wife, and previous mentor John O'Keefe" 的
> mentor 表述以 colleague 入库（不建 advisor-student，防与 O'Keefe 侧口径冲突）。
> 对手方规范名：**O'Keefe 必须写全名 "John O'Keefe (neuroscientist)"**（manifest 消歧义形式，防裸名分裂）。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 7。

## 五、配色方案

- **气质**：系统、建造、空间与时间的双重测绘
- **主色**：深峡湾绿 `#0F4C5C`（挪威海岸与神经地图的深邃）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：
  - `badgeGrid` 网格细胞 — 电光蓝 `#4C5FD5`
  - `badgeBorder` 边界细胞 — 冷青 `#0E7C7B`
  - `badgeTime` 时间细胞 — 暖橙 `#E07B30`
  - `badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：空间菱格与水平时间轴正交叠加，交点缀金点

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover 共享首页）
01  封面 — 大脑 GPS 的总工程师 / Edvard Moser 1962– + 四色 badge + 国籍行（Norway）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒/奥勒松出身/教育奥斯陆大学（cand.psychol. 1990 + dr.philos. 1995）/任职 NTNU/核心领域
03  核心贡献概览 — 网格细胞 / 边界细胞 / 时间细胞 / 三代卓越中心
04  管风琴匠人之子 (1962–1990) — 生于奥勒松、长于 Hareid；德裔移民家庭（父 Eduard Paul Moser 为管风琴匠，1953 自法兰克福邻郊移居挪威）；保守基督教家庭成长；奥斯陆 cand.psychol. 1990
05  奥斯陆与同行者 (1985–1995) — 1985 与 May-Britt 结婚；dr.philos. 神经生理学 1995；早期在 Per Andersen 指导下工作；数学与统计训练
06  博士后双站 (1995–1997) — 爱丁堡 Richard G. Morris 实验室（1995–1997）+ UCL O'Keefe 实验室访问两月
07  归国与晋升 (1996–1998) — 1996 NTNU 生物学心理学副教授、1998 神经科学正教授（早于 May-Britt 两年，各忠于本页）
08  2005：网格细胞（核心贡献页）— 与 May-Britt 在内嗅皮层发现网格细胞：提供坐标系与空间度量的特化神经元；紧随其后的边界细胞（border cells）等定位细胞家族
09  2014 诺贝尔奖 — 理由逐字；结构：夫妇共享一半 + O'Keefe 一半；2014 当选美国科学院外籍院士
10  2018：时间坐标 — 发现侧内嗅皮层表达时间体验与记忆的神经网络——空间之外的第二坐标系
11  荣誉与认可 — Spencer 2005 · Koetser 2006 · Bettencourt 2006 · Fernström 2008 · Louis-Jeantet 2011 · Anders Jahre 2011（与 May-Britt）· Perl-UNC 2012（与 May-Britt）· Horwitz 2013（与 May-Britt/O'Keefe）· Lashley 2014 · Körber 2014 · NAS 外籍院士 2014 · Nobel 2014 · St. Olav 大十字勋章 2018（与 May-Britt）
12  三代卓越中心 — Centre for the Biology of Memory（2002–2012）→ Centre for Neural Computation（2012–2022）→ Centre for Algorithms in the Cortex（2023–2033）；2007 合并为 Kavli 系统神经科学研究所并任所长
13  离婚不分家 — 2016 宣布离婚；Moser 研究环境共同领导与合作科研持续——"then-wife" 口径以 2014 为界
14  学术服务与传承 — 四院院士；Science 评审编辑（2004 起）；FENS Forum 2006 程序委员会主席；马普神经生物学研究所外部科学成员（2015 起）；爱丁堡荣誉教授；学生 Marianne Fyhn（内嗅皮层空间表征 2004 Science）
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由与结构 | 逐字 "for their discoveries of cells that constitute a positioning system in the brain"；夫妇共享**一半**、另一半归 O'Keefe，勿写成三人均分 |
| 2 | 德裔背景 | 父母 Eduard Paul Moser 与 Ingeborg Annamarie Herholz 均为德国人（法兰克福邻郊 Kronberg 长大），1953 年父移居挪威做管风琴匠——国籍仍是 Norway（出生挪威），背景一句即可 |
| 3 | 姐姐身份 | 姐姐 Ingunn Moser 是社会学家、VID 大学创始校长——仅一句注脚，不入库 |
| 4 | 学位口径 | cand.psychol.（1990，心理学）与 dr.philos.（1995，神经生理学）——挪威学位体系，勿写成 PhD/MD |
| 5 | 博士后年份差 | 本页载爱丁堡 1995–1997；May-Britt 页载 1994–1996——**各忠于本人页面**，勿强行统一 |
| 6 | 导师口径 | Per Andersen 在本页仅 "worked under the supervision of"，学位导师表述弱于 May-Britt 页——本侧 advisor note 用"在其指导下工作"弱措辞 |
| 7 | O'Keefe 全名 | 库内规范名 "John O'Keefe (neuroscientist)"——yaml 引用与正文首次出现均用全名，防裸名分裂；"previous mentor" 表述照实 |
| 8 | 离婚口径 | 2016 宣布离婚，合作持续——全篇 "then-wife（2014 时点）/long-term collaborator" 措辞 |
| 9 | 2005 vs 2018 | 2005 网格细胞（内嗅皮层）与 2018 时间细胞网络（侧内嗅皮层）是两条成果，年份勿串 |
| 10 | 教授年份 | 本页 1998 正教授；May-Britt 页 2000——各忠于本人页面 |
| 11 | 在世者 | Edvard 在世（1962- ）；relations=7 为明载诚实值 |
| 12 | 宗教背景 | "conservative Christian family" 系 page.md 明载的成长事实，一句带过不做评价 |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| grid cell | 网格细胞 | 内嗅皮层，空间坐标系与度量 |
| border cell | 边界细胞 | 定位细胞家族成员（又称 boundary cell） |
| medial entorhinal cortex | 内嗅皮层内侧部 | 网格细胞所在 |
| lateral entorhinal cortex | 内嗅皮层外侧部 | 2018 时间细胞网络所在 |
| positioning system | 定位系统 | 诺奖理由措辞（大脑 GPS 的官方表述） |
| dr.philos. | 挪威博士学位 | 1995 神经生理学，勿写 PhD/MD |
| cand.psychol. | 心理学职业学位 | 1990 奥斯陆，勿写 BA |
| Kavli Institute | 卡维利系统神经科学研究所 | 2007 年三中心合并而成 |

## 九、背景音乐选择

- **选定曲目**：**Savage** — Alex-Productions（manifest 预分配）
- **匹配理由**：Savage 的力量感与推进感对应"总工程师"式的科研建造者气质——从网格细胞到边界细胞
  再到时间坐标，一座座把大脑定位系统的地基夯实；也贴合其三代卓越中心的组织者形象。
- **备选（未采用）**：Through the Darkness（深沉感可用但更配"逆境"叙事，本篇是"建造"叙事）、EmpireCollapse（宏大但基调不合）
- **本地路径**：`music_audio/` 下 alex-productions 曲库按 curated_tracks.md 对应条目复制为
  `medic/presentations/21th_century/Edvard_I._Moser/Savage.wav`
