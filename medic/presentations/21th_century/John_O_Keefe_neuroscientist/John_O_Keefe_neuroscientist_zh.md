# 医学家立传提示词（John O'Keefe）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2014 年得主（独享一半；May-Britt Moser 与 Edvard Moser 共享另一半）。
> 本文件是 John O'Keefe 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面，
> 执行方按本提示词产出 15 页 Beamer 立传（本阶段不写 tex，仅沉淀事实与规范）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：John Michael O'Keefe（1939-11-18 生于纽约市，在世）
- **气质关键词**：**位置细胞的发现者、认知地图理论的奠基人、大脑 GPS 的第一位测绘员**
- **诺奖获奖理由（2014，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discoveries of cells that constitute a positioning system in the brain"
  > （因其发现构成大脑定位系统的细胞）——注意 "their"：三人共享；官方结构为 O'Keefe 独享一半、Moser 夫妇共享另一半
- **设计母题**：**地图与坐标（cognitive map）**。海马位置细胞像地图上的亮格随大鼠位置点亮——
  视觉母题用网格坐标上逐格点亮的发光单元，象征"大脑里的经纬度"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/John_O_Keefe_neuroscientist/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/21th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/21th_century/John_O_Keefe_neuroscientist/`，数据库写 greatminds 库（MySQL）。

- **第 0 步**：核对本地 page.md 事实基准（本提示词第三、四、七节已沉淀，执行时再逐句复核）
- **第 1 步**：建目录 `medic/presentations/21th_century/John_O_Keefe_neuroscientist/`（含 `images/`）
- **第 2 步**：复制 Makefile，设 `MAIN=John_OKeefe_zh`、`VIDEO_NAME=John_OKeefe_zh`（宏名禁撇号与括号）
- **第 3 步**：收集肖像（page.md 正文载 Commons 图 "Dr. John O'Keefe, Nobel laureate in Medicine.jpg"——奥斯陆诺奖演讲照，优先抓取；404 则装饰圆占位）
- **第 4~9 步**：tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuroscience | 神经科学 | 位置细胞/海马/大脑定位系统，诺奖核心 | 核心页 |
| 1 | psychology | 心理学 | McGill 心理学 PhD；UCL 认知心理学谱系 | 身份页 |
| 2 | neurobiology | 神经生物学 | frontmatter field_of_work；单个神经元放电分析 | 方法页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ronald Melzack | 师→生（博士导师） | McGill 心理学博士导师（1967），杏仁核单位放电研究 |
| advisor-student | Jonathan Dostrovsky | O'Keefe→学生 | 与其共同发现位置细胞（page.md 明载 "his student"） |
| advisor-student | Neil Burgess | O'Keefe→学生 | infobox Notable students 明载；边界矢量细胞模型合作者 |
| colleague | Patrick Wall | 无向 | 1967 年以 NIMH 博士后身份赴 UCL 在其组内工作 |
| collaborator | Lynn Nadel | 无向 | 合著影响深远的认知地图专著（海马=空间记忆的认知地图） |
| collaborator | Michael Recce | 无向 | 1993 年共同演示 θ 相位precession |
| co-honored | May-Britt Moser | 无向 | 2014 诺贝尔生理学或医学奖共享（发现构成大脑定位系统的细胞） |
| co-honored | Edvard Moser | 无向 | 2014 诺贝尔生理学或医学奖共享（发现构成大脑定位系统的细胞） |

> 说明：relations=8 为 page.md 明载值的诚实汇总。Kavli 2014 的共享者 Brenda Milner、Marcus Raichle
> 系非诺奖共享，**不建边**（陷阱表注明防 Review 误加）。Moser 夫妇曾在其实验室做访问博士后、
> 并促成其 2014 年 NTNU 兼职讲席——这层"导师"关系自 Moser 侧页面表述，本侧以 co-honored 覆盖，
> 不另建 advisor-student（防与 Moser 侧口径冲突，Moser 侧可自建 colleague）。
> 对手方规范名：Melzack/Wall/Dostrovsky/Nadel/Recce/Burgess 库内均无，本侧新建 stub。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 8。

## 五、配色方案

- **气质**：测绘、先驱、五十年扎根一间实验室的定力
- **主色**：海马紫 `#4A2A6A`（海马体与认知地图的神秘紫）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：
  - `badgePlace` 位置细胞 — 电光蓝 `#4C5FD5`
  - `badgeTheta` θ 相位 — 暖橙 `#E07B30`
  - `badgeBoundary` 边界细胞 — 冷青 `#0E7C7B`
  - `badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：稀疏网格坐标点阵，部分格点亮（位置野），金点标注路径

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover 共享首页）
01  封面 — 大脑 GPS 的测绘员 / John O'Keefe 1939– + 四色 badge + 国籍行（United States / United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒/纽约出身/教育 CCNY BA 1963 + McGill MA 1964 PhD 1967/任职 UCL 1967– /核心领域
03  核心贡献概览 — 位置细胞 / 认知地图 / θ 相位precession / 边界矢量细胞
04  爱尔兰移民之子 (1939–1963) — 纽约出生；父母爱尔兰移民（均未在爱尔兰完成小学）；Regis High School；CCNY BA 1963
05  McGill 双学位 (1963–1967) — MA 1964、心理学 PhD 1967（Melzack 门下）；论文：自由活动猫的杏仁核单位放电特性
06  UCL 五十餘年 (1967– ) — NIMH 博士后（与 Patrick Wall 工作）；此后长期扎根 UCL；1987 正教授
07  发现位置细胞（核心贡献页）— 与学生 Jonathan Dostrovsky 系统分析环境影响海马单个神经元放电的因素→位置细胞；数百篇后续研究
08  认知地图理论 — 与 Lynn Nadel 合著：海马作为空间记忆的认知地图的功能假说（影响深远）
09  θ 相位precession (1993) — 与 Michael Recce：大鼠穿越位置野时放电相位前移；时间编码证据，被大量重复
10  预言边界矢量细胞 (1996–2006) — 与 Neil Burgess：屏障移动改变位置野→预言边界矢量细胞；数年后在下托与内嗅皮层获实验证实（border cells）
11  2014 诺贝尔奖 — 理由逐字；结构：O'Keefe 一半 + Moser 夫妇一半；奥斯陆诺奖演讲（2014-12）
12  荣誉与认可 — FRS 1992 · FMedSci 1998 · Feldberg 2001 · Grawemeyer 2006（与 Nadel）· BNA 奖 2007 · FENS EJN 奖 2008 · Gruber 2008 · Horwitz 2013（与 Moser 夫妇）· Kavli 2014（与 Milner/Raichle）· NAS 2016 · 皇家爱尔兰学院荣誉会员 2019
13  Sainsbury Wellcome 中心 — 首任所长（inaugural director）
14  传承与回响 — 2014 起应 Moser 夫妇之邀任 NTNU 兼职讲席；位置细胞→网格细胞：大脑定位系统两代发现人的合流；荣誉博士（UCC 2014/CCNY 2015/McGill 2015）
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由与结构 | 逐字 "for their discoveries of cells that constitute a positioning system in the brain"；结构是 O'Keefe **独享一半**、Moser 夫妇共享另一半（M-B 页面明载 "shared half"），勿写成三人均分 |
| 2 | 国籍口径 | Nobel 官方口径 "United States United Kingdom"（infobox Citizenship 同序）；manifest 仅写 United States，本篇按页面双籍并置，yaml 两条国籍 |
| 3 | 位置细胞发现分工 | 与学生 **Jonathan Dostrovsky** 共同发现——Dostrovsky 常被省略，务必署名 |
| 4 | 书与奖的搭档区分 | 认知地图书搭档 = Lynn Nadel（Grawemeyer 2006 也与 Nadel 共享）；θ 相位搭档 = Michael Recce；边界矢量细胞搭档 = Neil Burgess——三组人勿互串 |
| 5 | Kavli 2014 | 共享者是 **Brenda Milner 与 Marcus Raichle**（记忆与认知网络），不是 Moser 夫妇——与 Horwitz 2013（Moser 夫妇）两奖极易混淆 |
| 6 | Horwitz 2013 | 与 Edvard/May-Britt Moser 共享——诺奖前奏，可与诺奖页呼应但年份奖项勿错置 |
| 7 | 任职年限 | 1967 年至今 UCL（page.md "has been there ever since"）；1967 年身份是 NIMH 博士后研究员（与已故 Patrick Wall 工作）；1987 才升正教授 |
| 8 | NTNU 讲席 | 2014 年应 Edvard/May-Britt 之邀任挪威科技大学**兼职**教授——"at the behest of" 表述照实 |
| 9 | 博士论文 | 自由活动猫的**杏仁核**单位放电（1967）——诺奖工作（海马）是到 UCL 之后，勿把杏仁核写进位置细胞叙事 |
| 10 | 全名与消歧义 | John Michael O'Keefe；库与目录名用 "John O'Keefe (neuroscientist)" 消歧义形式——Moser 夫妇 yaml 引用时也必须用此全名，防分裂 stub |
| 11 | 在世者 | O'Keefe 在世（1939- ）；relations=8 为明载诚实值，防 Review 误判 |
| 12 | 肖像 | page.md 正文有 Commons 诺奖演讲照（Oslo, December 2014）——图注写"奥斯陆诺奖演讲" |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| place cell | 位置细胞 | 海马内对特定位置放电的神经元 |
| cognitive map | 认知地图 | Nadel 合著理论核心 |
| theta phase precession | θ 相位precession | 时间编码现象，1993 与 Recce 演示 |
| hippocampus | 海马 | 位置细胞所在，空间记忆中枢 |
| boundary vector cell | 边界矢量细胞 | 1996 理论预言、后被证实 |
| subiculum | 下托 | 边界细胞实验证实部位之一 |
| entorhinal cortex | 内嗅皮层 | 网格细胞所在（Moser 夫妇端） |
| temporal coding | 时间编码 | 放电时序携带信息 |

## 九、背景音乐选择

- **选定曲目**：**The Flow of Time** — Alex-Productions（manifest 预分配）
- **匹配理由**：The Flow of Time 的时间流动感对应 θ 节律与相位precession的"时间编码"主题——
  放电相位随时间推移前移，正是"时间即坐标"的科学诗意；也贴合其 1967 年至今一甲子扎根 UCL 的长时段叙事。
- **备选（未采用）**：Timeless（时间感重叠且系列占用率高）、Mirage（空间迷航感可用但偏虚幻，不如时间主题贴合）
- **本地路径**：`music_audio/` 下 alex-productions 曲库按 curated_tracks.md 对应条目复制为
  `medic/presentations/21th_century/John_O_Keefe_neuroscientist/The_Flow_of_Time.wav`
