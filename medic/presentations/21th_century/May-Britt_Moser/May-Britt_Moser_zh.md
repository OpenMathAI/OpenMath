# 医学家立传提示词（May-Britt Moser）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2014 年得主（与 Edvard Moser 共享一半；另一半归 John O'Keefe）。
> 本文件是 May-Britt Moser 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面，
> 执行方按本提示词产出 15 页 Beamer 立传（本阶段不写 tex，仅沉淀事实与规范）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：May-Britt Moser（1963 年生于挪威福斯纳沃格，在世；本名 May-Britt Andreassen）
- **气质关键词**：**网格细胞的共同发现者、特隆赫姆学派的女主人、从乡野"假小子"到诺贝尔奖**
- **诺奖获奖理由（2014，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discoveries of cells that constitute a positioning system in the brain"
  > （因其发现构成大脑定位系统的细胞）——注意共享结构：Moser 夫妇共享一半，另一半归 O'Keefe
- **设计母题**：**网格（grid）**。内嗅皮层网格细胞以菱格铺满空间坐标——视觉母题用缀满节点的
  菱形网格层层延展，一枚金点在其上移动，象征"大脑坐标系的绘出"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/May-Britt_Moser/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/21th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/21th_century/May-Britt_Moser/`，数据库写 greatminds 库（MySQL）。

- **第 0 步**：核对本地 page.md 事实基准（本提示词第三、四、七节已沉淀，执行时再逐句复核）
- **第 1 步**：建目录 `medic/presentations/21th_century/May-Britt_Moser/`（含 `images/`）
- **第 2 步**：复制 Makefile，设 `MAIN=May_Britt_Moser_zh`、`VIDEO_NAME=May_Britt_Moser_zh`（宏名禁连字符）
- **第 3 步**：收集肖像（infobox 载 NTNU 2014 照；Commons Special:FilePath 回退，404 则装饰圆占位）
- **第 4~9 步**：tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuroscience | 神经科学 | 网格细胞与空间定位系统，诺奖核心 | 核心页 |
| 1 | psychology | 心理学 | 奥斯陆心理学本科出身、NTNU 心理学教授 | 身份页 |
| 2 | neurophysiology | 神经生理学 | 1995 博士学位科目（海马结构与空间识别） | 教育页 |
| 3 | biological psychology | 生物学心理学 | 1996 NTNU 副教授席位科目 | 职业页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Per Andersen | 师→生（博士导师） | 奥斯陆大学医学院神经生理学博士导师（1995） |
| advisor-student | Richard G. Morris | 师→生（博士后导师） | 爱丁堡大学神经科学中心博士后（1994–1996） |
| colleague | John O'Keefe (neuroscientist) | 无向 | 曾在 UCL 其实验室做访问博士后两月；长期导师与合作者 |
| co-honored | John O'Keefe (neuroscientist) | 无向 | 2014 诺贝尔生理学或医学奖共享（发现构成大脑定位系统的细胞） |
| spouse | Edvard Moser | 无向 | 1985-07-27 结婚，2016 宣布离婚，科研合作持续 |
| co-honored | Edvard Moser | 无向 | 2014 诺贝尔生理学或医学奖共享（发现构成大脑定位系统的细胞） |
| advisor-student | Marianne Fyhn | M-B Moser→学生 | infobox Doctoral students 明载 |

> 说明：relations=7（行数）。Moser 夫妇互指 spouse+co-honored 双行（同对异型允许并存，参照库内先例）。
> "与其导师 John O'Keefe 共同开拓大脑空间表征研究"系 page.md 明载（"together with their mentor John O'Keefe"），
> 本侧以 colleague 表达 mentor 情谊（O'Keefe 侧不建反向 advisor-student，双侧口径已在各自提示词对齐）。
> 对手方规范名：**O'Keefe 必须写全名 "John O'Keefe (neuroscientist)"**（manifest 消歧义形式，防裸名分裂）。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 7。

## 五、配色方案

- **气质**：坚韧、协作、乡野女孩的好奇心
- **主色**：峡湾青蓝 `#14647E`（挪威西海岸与神经科学的清冽）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：
  - `badgeGrid` 网格细胞 — 电光蓝 `#4C5FD5`
  - `badgeHippo` 海马与空间 — 暖橙 `#E07B30`
  - `badgeCell` 定位细胞家族 — 冷青 `#0E7C7B`
  - `badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：菱形网格点阵延展，一角缀挪威峡湾曲线

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover 共享首页）
01  封面 — 大脑坐标系的绘出者 / May-Britt Moser 1963– + 四色 badge + 国籍行（Norway）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒/福斯纳沃格出身/教育奥斯陆大学 PhD 1995/任职 NTNU/核心领域
03  核心贡献概览 — 网格细胞 / 定位细胞家族 / 记忆中心建设 / 诺奖
04  福斯纳沃格的乡野女孩 (1963– ) — 五个孩子中最小；农家与木匠父亲；自认 "tom-boy"；爱动物、梦想当医生或兽医；母亲的激励
05  奥斯陆与同窗重逢 (1985–1990) — 高中同学 Edvard 重逢、1985-07-27 结婚；心理学/数学/神经生物学；1990 心理学学位
06  博士与育儿并行 (1990–1995) — Per Andersen 门下神经生理学 PhD（海马结构与大鼠空间识别）；两女出生随父母进实验室（page.md 明载）
07  博士后双站 (1994–1997) — 爱丁堡 Richard Morris 实验室（1994–1996）+ UCL O'Keefe 实验室访问两月
08  归国建中心 (1996–2002) — 1996 NTNU 生物学心理学副教授、2000 神经科学正教授；2002 团队升格卓越中心（CBM）
09  2005：网格细胞（核心贡献页）— 与 Edvard 在内嗅皮层发现网格细胞：提供大脑坐标系与空间度量的特化神经元；此后同回路更多空间表征细胞
10  2014 诺贝尔奖 — 理由逐字；结构：夫妇共享一半 + O'Keefe 一半；诺贝尔奖史上第六对获奖夫妇
11  荣誉与认可 — Spencer 2005 · Koetser 2006 · Bettencourt 2006 · Fernström 2008 · Louis-Jeantet 2011 · Anders Jahre 2011 · Perl-UNC 2012 · Horwitz 2013（与 Edvard/O'Keefe）· Lashley 2014 · Körber 2014 · Nobel 2014 · Erna Hamburger 2016 · St. Olav 大十字勋章 2018
12  三座卓越中心 — CBM（2002–2012）→ Centre for Neural Computation（2013–2022 创始主任）→ Centre for Algorithms in the Cortex（2023– 创始主任）；2007 合并为 Kavli 系统神经科学研究所
13  离婚不分家 — 2016 宣布离婚、科研合作与 Moser 研究环境共同领导持续——"former husband" 口径贯穿
14  学院与公共角色 — 挪威皇家科学与文学院等四院院士；ERC 评审小组成员（2007–2009）；2013 Madame Beyer 女性领袖奖
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由与结构 | 逐字 "for their discoveries of cells that constitute a positioning system in the brain"；夫妇共享**一半**、另一半归 O'Keefe（page.md 明载 "shared half"），勿写成三人均分 |
| 2 | 本名 | 出生名 May-Britt **Andreassen**，婚后从夫姓 Moser——出身页可注本名 |
| 3 | 生日口径 | page.md 正文仅 "born in 1963"（无月日）；frontmatter 有 1963-01-04——yaml 存 frontmatter 值并注明层级，页面生年写 1963 即可 |
| 4 | 离婚口径 | 2016 宣布离婚；此后仍共同领导 Moser 研究环境——全篇用 "former husband/then-wife" 措辞；2014 颁奖时点夫妻存续，勿把"前夫"用于此前叙事 |
| 5 | 第六对夫妇 | "The Mosers are one of six couples to be awarded a Nobel Prize"——写"史上第六对诺奖夫妇"，勿写成"首对" |
| 6 | 博士后年份差 | 本页载爱丁堡 1994–1996；Edvard 页载其本人 1995–1997——**各忠于本人页面**，勿强行统一 |
| 7 | 博士导师 | Per Andersen（奥斯陆，1995 神经生理学博士）；Edvard 页称 "worked under the supervision of Per Andersen"——夫妇导师同一人，无冲突 |
| 8 | O'Keefe 全名 | 库内规范名 "John O'Keefe (neuroscientist)"——yaml 引用与正文首次出现均用全名，防裸名分裂 |
| 9 | 网格细胞年份 | **2005** 发现（内嗅皮层）；2002 CBM、2007 Kavli 研究所、2018 Edvard 侧时间细胞网络——各年份勿串 |
| 10 | fields 口径 | 博士是神经生理学、教席是生物学心理学——与 Edvard 结构相同但本位不同，叙述以本页为准 |
| 11 | 在世者 | May-Britt 在世（1963- ）；relations=7 为明载诚实值 |
| 12 | 叙事分寸 | 家庭经济、母亲催学等成长细节系 page.md 明载，可温情呈现；不做价值观引申 |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| grid cell | 网格细胞 | 内嗅皮层，空间坐标系 |
| entorhinal cortex | 内嗅皮层 | 网格细胞所在 |
| positioning system | 定位系统 | 诺奖理由措辞（大脑 GPS 的官方表述） |
| spatial representation | 空间表征 | 定位细胞家族的共同主题 |
| centre of excellence | 卓越中心 | 挪威研究理事会资助体制 |
| hippocampus | 海马 | 博士论文对象（结构与空间识别） |
| neurophysiology | 神经生理学 | 博士学位科目 |

## 九、背景音乐选择

- **选定曲目**：**Daylight** — Alex-Productions（manifest 预分配）
- **匹配理由**：Daylight 的明亮与开阔对应本篇的叙事底色——乡野女孩的好奇心、夫妻并肩同行、
  在特隆赫姆把一间实验室建成世界级坐标——是批次中最"明亮"的人物弧线；网格点亮如晨光铺开。
- **备选（未采用）**：Shine Like The Sun（光感重叠且已被占用）、Ascension（攀升感可用但本篇更重"同行"而非"登顶"）
- **本地路径**：`music_audio/` 下 alex-productions 曲库按 curated_tracks.md 对应条目复制为
  `medic/presentations/21th_century/May-Britt_Moser/Daylight.wav`
