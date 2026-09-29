# 物理学家立传提示词（F. Duncan M. Haldane）

> 本文件是 OpenPhysicist 21 世纪批次「物理学家立传提示词」，目标人物：F. Duncan M. Haldane（2016 诺贝尔物理学奖，拓扑物态理论）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节），按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Frederick Duncan Michael Haldane（弗雷德里克·邓肯·迈克尔·霍尔丹）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Haldane 篇的视觉主线是**拓扑物态**——从一维自旋链的隐藏序到分数量子霍尔态的几何描述。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：F. Duncan M. Haldane（1951-09-14 生于伦敦，在世）
- **气质关键词**：**拓扑物态的奠基人、量子自旋液体的高手、分数量子霍尔效应的解构者** —— 2016 诺贝尔物理学奖获奖理由（与 Thouless / Kosterlitz 共享）：
  > "for theoretical discoveries of topological phase transitions and topological phases of matter"（因其拓扑相变与拓扑物态的理论发现）
- **设计母题**：**缠绕与隐藏序（entanglement & hidden order）**。自旋链中整数量子数的「隐藏对称性保护」、FQHE 态由 unimodular 度规场描述的「复合玻色子形状」，都指向「局部看不见、整体才显形」的拓扑视觉语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/F._Duncan_M._Haldane/page.md`
- **第 0 步状态**：page.md 已有本地；`{Dir}.html` 与 `images/` **待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/F._Duncan_M._Haldane`
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 数据库同步：含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1951-09-14 生于英国伦敦；在世（享年留白）
- 国籍：英国 + 斯洛文尼亚（2019-03-22 于华盛顿斯洛文尼亚使馆授予）；美国永久居民
- 家庭：父亲为英国陆军军医，驻南斯拉夫/奥地利边境时结识学医的斯洛文尼亚人 Ljudmila Renko（母亲），婚后返英；妻子 Odile Belmont，现居新泽西州普林斯顿
- 教育：St Paul's School, London；剑桥大学 Christ's College（BA， PhD 1978）
- 博士导师：Philip Warren Anderson（1977 诺贝尔物理学奖得主）；博士论文《An extension of the Anderson model as a model for mixed valence rare earth materials》（1978）
- 任职机构：Institut Laue–Langevin（法国格勒诺布尔，1977–1981 物理学家）→ University of Southern California（1981-08 助理教授，至 1987）→ University of California, San Diego（1986-07 起教授，至 1992-02）→ Princeton University（1990 至今；1999 Eugene Higgins 讲席教授，2017 Sherman Fairchild 大学讲席教授）；Perimeter Institute Distinguished Visiting Research Chair（2013–2018）
- 关键荣誉：APS Fellow（1986）；Sloan Research Fellow（1984–88）；American Academy of Arts and Sciences Fellow（1992）；Oliver E. Buckley Condensed Matter Prize（1993）；FRS（1996）；Institute of Physics Fellow（1996）；AAAS Fellow（2001）；Lorentz Chair（2008）；ICTP Dirac Medal（2012）；Cergy-Pontoise 大学荣誉博士（2015）；Nobel Prize in Physics（2016，与 Thouless / Kosterlitz 共享）；NAS 院士（2017）；Lise Meitner Distinguished Lecturer（2017）；Golden Plate Award（2017）；卢布尔雅那大学荣誉博士
- 知名学生：Ashvin Vishwanath（infobox 明载的唯一博士生）
- 核心贡献清单：
  1. 一维反铁磁自旋链理论（Haldane 相：整数自旋链有能隙、半整数自旋链无能隙）
  2. 分数量子霍尔效应的 Haldane 赝势理论
  3. Luttinger 液体理论
  4. 量子反常霍尔效应（known for 明载）
  5. 排除统计（exclusion statistics）与纠缠谱（entanglement spectra）
  6. FQHE 的「Chern-Simons + 量子几何」描述：复合玻色子的 unimodular（行列式 1）度规张量场作为集体自由度
- 关键时间线（15 节点）：1951 生于伦敦 → St Paul's School → 剑桥 Christ's College BA → 1977–1981 ILL 格勒诺布尔 → 1978 博士（Anderson 指导）→ 1981-08 USC 助理教授 → 1984–88 Sloan Fellow → 1986 APS Fellow → 1986-07 UCSD 教授 → 1990 Princeton 教授 → 1992 美国艺术与科学院 → 1993 Buckley 奖 → 1996 FRS / IoP Fellow → 1999 Eugene Higgins 讲席 → 2001 AAAS Fellow → 2008 Lorentz Chair → 2012 Dirac Medal → 2013–2018 Perimeter 讲席 → 2015 荣誉博士 → 2016-10 诺贝尔奖 → 2017 Sherman Fairchild 讲席 / NAS 院士 → 2019-03-22 斯洛文尼亚国籍

### 第 4 步：研究领域表 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | condensed matter physics | 凝聚态物理 | 主领域（infobox Fields） | 全篇 |
| 1 | topological phases | 拓扑物态 | 2016 诺奖核心之一 | 核心页 |
| 2 | fractional quantum Hall effect | 分数量子霍尔效应 | Haldane 赝势、复合玻色子几何 | FQHE 页 |
| 3 | spin chains | 自旋链（一维量子自旋系统） | Haldane 相 / 能隙猜想 | 自旋链页 |
| 4 | Luttinger liquid | Luttinger 液体 | 一维相互作用电子理论 | 贡献页 |

### 第 4.5 步：社会关系表 【与 yaml 完全一致，仅收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Philip Warren Anderson | 对方是导师 | 剑桥 Christ's College 博士导师（1978），1977 诺贝尔物理学奖得主 |
| advisor-student | Ashvin Vishwanath | 对方是学生 | infobox 明载博士生 |
| co-honored | David J. Thouless | 无向 | 2016 诺贝尔物理学奖共同得主（拓扑相变与拓扑物态） |
| co-honored | J. Michael Kosterlitz | 无向 | 2016 诺贝尔物理学奖共同得主（拓扑相变与拓扑物态） |
| spouse | Odile Belmont | 无向 | 妻子，现居新泽西州普林斯顿 |

> 无载不入库：Haldane–Shastry 模型仅见 See also 链接，与 Shastry 的合作关系 page.md 正文无载禁写；母亲 Ljudmila Renko、父亲为家庭成员非学术关系，不入 `person_relation`。

### 第 5 步：配色方案 【人物专属】

- **气质**：拓扑、缠绕、深水下的隐藏序
- **配色**：拓扑深青（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 `mainclr` — 拓扑深青 `#0F5B5E`（本批专属，勿与他篇重复）
  - `badgeA` 拓扑物态 — 青 `#0E7C7B`
  - `badgeB` FQHE — 琥珀 `#E07B30`
  - `badgeC` 自旋链 — 靛蓝 `#4C5FD5`
  - `badgeD` Luttinger 液体 — 玫瑰 `#C4204F`
- **背景母题**：相互缠绕的细环链（细线圆环两两相扣、疏密错落），呼应「拓扑缠绕」与自旋链隐藏序

### 第 6 步：幻灯片序列 【人物专属，13 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 拓扑物态奠基人 / F. Duncan M. Haldane 1951– + 四色 badge + 右上头像 + 国籍行（United Kingdom · Slovenia）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 自旋链 Haldane 相 / FQHE 赝势 / Luttinger 液体 / 量子反常霍尔效应 / 纠缠谱
04  早年与剑桥 (1951–1978) — St Paul's School、Christ's College、Anderson 门下、混合价稀土论文
05  从 ILL 到美国 (1977–1992) — 格勒诺布尔中子散射、USC、UCSD
06  一维自旋链：Haldane 相（核心贡献页）— 整数/半整数自旋能隙二分；page.md 无公式 → 用能隙示意概念图式并注明
07  分数量子霍尔效应：Haldane 赝势 — Laughlin 态之外的赝势展开视角
08  量子反常霍尔效应与拓扑物态 — known for 口径；仅写明载内容
09  FQHE 的量子几何 (2011) — 复合玻色子形状、unimodular 度规、Chern-Simons + 量子几何取代 Chern-Simons + Ginzburg-Landau 范式；公式框放 unimodular 条件 det g = 1 概念式并注明为示意
10  门生与传承 — Ashvin Vishwanath
11  荣誉与认可 — Nobel 2016 · Buckley 1993 · Dirac 2012 · FRS 1996 · NAS 2017
12  结尾 — 底部品牌 OpenMathAI
```

### 第 7–8 步：版式要点 + 陷阱表

版式照标杆（身份信息页左头像右网格、\plainbar 可删减、每页 make 后 pdftoppm 目检）。**Haldane 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生卒日期 | frontmatter 有双值 `["1951-09-14","1951-11-14"]`，以 infobox 与正文 **1951-09-14** 为准 |
| 同名区分 | 库内另有 J. B. S. Haldane（遗传学家，id=485），勿混；本人库内 stub 为 `Duncan Haldane`（id=2631），yaml name_en 沿用此形式 |
| 导师规范名 | 库内有 `Philip W. Anderson`(2607) 与 `Philip Warren Anderson`(2628, Q190770) 两条，**一律用后者** |
| USC 年份 | 正文自相矛盾（"assistant professor 1981 remained until 1987" 与 "associate professor in 1981, professor in 1986" 并存），主线写 1981-08 助理教授、1987 离任，勿自行圆整另一说 |
| USC/UCSD 重叠 | 正文称 1986-07 加入 UCSD 又称 USC 至 1987，照原文呈现两段，不加解释 |
| 诺奖三人分工 | Thouless / Kosterlitz 主攻**拓扑相变**（BKT），Haldane 主攻**拓扑物态**（一维自旋链等）；勿把 BKT 相变归到 Haldane 名下 |
| 量子反常霍尔效应 | known for 明载可写标题级事实；1988 Haldane model、2013 实验观测等 page.md 无载禁写 |
| Haldane–Shastry | 仅 See also 出现，合作细节与年份无载禁写 |
| 斯洛文尼亚国籍 | 2019-03-22 授予（母亲为斯洛文尼亚人、生于伦敦），勿写「生于斯洛文尼亚」或「斯洛文尼亚裔」之外引申 |
| 博士生 | 仅 Ashvin Vishwanath（infobox），勿扩大名单 |
| 妻子 | Odile Belmont 可写婚姻关系；其职业/背景 page.md 无载禁写 |

### 第 9 步：术语清单 【8–12 条】

| 英文 | 中文 | 风险 |
|------|------|------|
| topological phase transitions | 拓扑相变 | 三人共享理由，主体是 Thouless/Kosterlitz |
| topological phases of matter | 拓扑物态 | Haldane 的诺奖主贡献 |
| Haldane phase | Haldane 相 | 整数自旋链有能隙的隐藏序态 |
| Haldane pseudopotential | Haldane 赝势 | FQHE 波函数系统构造法 |
| fractional quantum Hall effect | 分数量子霍尔效应（FQHE） | 勿漏「分数」 |
| Luttinger liquid | Luttinger 液体 | 一维电子液体，勿译「液体理论」 |
| quantum anomalous Hall effect | 量子反常霍尔效应 | 无外磁场的量子化霍尔态 |
| exclusion statistics | 排除统计 | 介于玻色/费米之间的统计 |
| entanglement spectrum | 纠缠谱 | 勿与「能谱」混淆 |
| composite boson | 复合玻色子 | FQHE 量子几何描述的基本自由度 |
| unimodular metric | 行列式为 1 的度规 | det g = 1，约束「形状」 |
| Chern-Simons theory | 陈-西蒙斯理论 | 拓扑场论框架 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**: **Expedition** — Alex-Productions（66k views，标签：探索 / 史诗）
- **匹配理由**: 「几何、拓扑、远征式叙事」正是 Haldane 的写照——从伦敦到格勒诺布尔再到普林斯顿，理论远征横贯一维自旋链、FQHE 与拓扑物态；2016 年三人共享诺奖是这场远征的高潮。
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`
- **备选**: The Invisible Light（纪录片稳重感）；The Flow of Time（时间线叙事）。

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/F._Duncan_M._Haldane/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/F._Duncan_M._Haldane.yaml` | 社会关系入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID → name_en 匹配） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
