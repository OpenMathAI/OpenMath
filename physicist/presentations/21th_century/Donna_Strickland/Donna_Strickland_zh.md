# 物理学家立传提示词（Donna Strickland）

> 本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主的「人物专属立传提示词」。
> 目标人物：Donna Strickland（2018 诺贝尔物理学奖，CPA 实现者，第三位物理学诺奖女性得主）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Donna Theo Strickland（唐娜·西奥·斯特里克兰），2018 年诺贝尔物理学奖（与 Mourou 共享一半），脉冲激光先驱、滑铁卢大学教授。
- **设计哲学**：保留「身份信息页 + 结构化研究领域」骨架；Strickland 篇叙事主线是「实验者的胜利」——自嘲 "laser jock" 的动手派，把 CPA 从论文变成桌面太瓦激光。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Donna Theo Strickland（1959-05-27 生于加拿大安大略省圭尔夫；在世）
- **气质关键词**：**激光实干家（laser jock）、第三位物理学诺奖女性、桌面太瓦激光的开创者**
- **官方获奖理由（2018，与 Mourou 共享一半）**：
  > "for their method of generating high-intensity, ultra-short optical pulses"（因产生高强度超短光脉冲的方法）
  - 另一半授予 Arthur Ashkin（光镊）；本篇重心在 CPA 的实现与下游应用。
- **设计母题**：**桌面上的强光（table-top terawatt）**。CPA 让小型高功率激光系统立上普通光学台——视觉以光学台、光栅对（展宽/压缩）为核心意象。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Donna_Strickland/page.md`（**已有本地**）
- **待下载**：`{Dir}.html` 与 `images/` 肖像待下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Donna_Strickland`
- **参考模板**：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1959-05-27 生于安大略省圭尔夫；在世（death_date 留白）
- **国籍**：加拿大
- **家庭**：父 Lloyd Strickland（电气工程师）、母 Edith J.（née Ranney，英语教师）；夫 Douglas Dykaar（罗切斯特电气工程博士），子女 Hannah（多伦多大学天体物理研究生）与 Adam（Humber College 喜剧方向）；加拿大联合教会活跃成员
- **教育**：Guelph Collegiate Vocational Institute → 麦克马斯特大学工程物理 BEng 1981（全班 25 人中 3 名女性之一；选该校因工程物理含激光与电光学）→ 罗切斯特大学光学研究所 PhD 1989
- **博士导师**：Gérard Mourou（frontmatter + infobox + 正文三处明载）；博士论文 *Development of an Ultra-Bright Laser and an Application to Multi-photon Ionization*（infobox 标 1988，正文作 1989 年获学位）
- **任职机构**：加拿大国家研究委员会（NRC）研究助理 1988–1991（与 Paul Corkum 同在超快现象组，当时拥有世界最强短脉冲激光）→ 劳伦斯利弗莫尔国家实验室激光部 1991–1992 → 普林斯顿大学先进光子与光电子材料技术中心技术员 1992 → 滑铁卢大学助理教授 1997（物理系首位全职女性教授）；2018 诺奖后申请并升任正教授
- **关键荣誉**：Nobel 2018；Sloan Research Fellowship 1998；Premier's Research Excellence Award 1999；Cottrell Scholars Award 2000；Golden Plate Award 2019（Frances Arnold 颁发）；Companion of the Order of Canada 2019；Chevalier de la Légion d'honneur 2022；Joseph Carrier C.S.C. Science Medal（Notre Dame）2022；Optica Fellow 2008 / Honorary Member 2022；FRSC 2019；加拿大工程院荣誉院士 2019；NAS 院士 2020；FRS 2020；教皇科学院院士 2021；澳大利亚科学院通讯院士 2025；BBC 100 Women 2018；阿尔伯塔大学荣誉博士 2024
- **学会服务**：Optica副主席 2011、主席 2013、*Optics Letters* 专题编辑 2004–2010、总统顾问委员会主席；加拿大物理学家协会董事与学术事务总监；滑铁卢 TRuST 学术网络共同主任 2023
- **核心贡献清单**：
  1. 啁啾脉冲放大的实现（1985 论文 *Compression of amplified chirped optical pulses*，Optics Communications 56(3):219–221，与 Mourou）——光谱与时间上先展宽、放大后再压缩，产生太瓦至拍瓦超短脉冲
  2. 突破自聚焦损伤瓶颈：脉冲峰值功率达 GW/cm² 时自聚焦会损毁放大器，CPA 绕开该限制
  3. 「桌面太瓦激光」——小型高功率系统得以建于普通光学台
  4. 超快光学新波长推进：中红外与紫外、双色/多频方法、拉曼产生
  5. 高功率激光在人眼微晶状体加工（治疗老花眼）中的应用研究
- **关键时间线（18 节点）**：1959 生于圭尔夫 → GCVI 毕业 → 1981 麦克马斯特 BEng → 罗切斯特光学研究所 → 1985 CPA 论文 → 1988 博士论文 → 1989 获 PhD → 1988–91 NRC 与 Corkum 合作 → 1991–92 利弗莫尔 → 1992 普林斯顿 → 1997 滑铁卢助理教授（首位全职女性物理教授）→ 2008 Optica Fellow → 2011 Optica 副主席 → 2013 Optica 主席 → 2018-10-02 获诺奖（第三位女性物理学诺奖得主）→ 2018 升正教授 → 2019 加拿大勋章同伴/FRSC → 2020 NAS/FRS 院士 → 2025 澳大利亚科学院通讯院士

### 第 4 步：研究领域表 【人物专属，与 yaml fields 一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | ultrafast optics | 超快光学 | infobox Main interests 首列 | 核心贡献页 |
| 1 | chirped pulse amplification | 啁啾脉冲放大 | 1985 论文，2018 诺奖核心 | 核心贡献页 |
| 2 | nonlinear optics | 非线性光学 | 高强度激光系统研究主线 | 研究页 |
| 3 | intense laser-matter interactions | 强激光-物质相互作用 | Main interests 明载 | 研究页 |
| 4 | pulsed lasers | 脉冲激光 | 导语定位「pulsed lasers 先驱」 | 概览页 |

### 第 4.5 步：社会关系表 【人物专属，与 yaml relations 一致；只收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gérard Mourou | 师→生（博士导师） | 罗切斯特 LLE 博士导师，CPA 共同发明人 |
| co-honored | Gérard Mourou | 无向 | 2018 诺贝尔物理学奖共享（两人共享一半，Ashkin 得另一半） |
| co-honored | Arthur Ashkin | 无向 | 2018 诺贝尔物理学奖共享（Ashkin 得一半，工作互不相关） |
| colleague | Paul Corkum | 无向 | NRC 超快现象组同事（1988–1991） |
| spouse | Douglas Dykaar | 无向 | 罗切斯特电气工程博士 |

### 第 5 步：配色方案 【人物专属】

- **气质**：明快、扎实、突破
- **主色**：深紫罗兰 `#5B2A86`（光谱的短波端与开拓气质）+ 诺奖香槟金 `C9A227`
  - `badgeCPA` CPA — 琥珀 `#E07B30`
  - `badgeTable` 桌面太瓦 — 电光青 `#0E7C9B`
  - `badgeUltra` 超快/新波长 — 玫瑰 `#C4204F`
  - `badgeEye` 眼科应用 — 苔绿 `#3E7C4F`
- **背景母题**：柔和气泡 + 一对平行光栅符号（展宽-压缩意象）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）；无真实肖像则用装饰圆占位。
2. 封面有国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页（封面之后、核心贡献之前）。
4. 结尾页品牌标注统一 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 脉冲激光先驱 / Donna Strickland 1959– + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、出生地、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — CPA / 桌面太瓦 / 新波长 / 眼科应用
04  圭尔夫到麦克马斯特 (1959–1981) — 工程物理、25 人中 3 名女性
05  罗切斯特 LLE：CPA 诞生 (1981–1989) — Mourou 门下、1985 论文（核心贡献页，公式框放展宽-放大-压缩概念图式或脉冲功率公式）
06  自聚焦瓶颈 — GW/cm² 损伤限制与 CPA 的绕行
07  NRC/利弗莫尔/普林斯顿 (1988–1997) — 与 Corkum 超快现象组
08  滑铁卢岁月 (1997–) — 首位全职女性物理教授、超快激光组
09  2018 诺贝尔奖 — 第三位女性、与 Mourou 共享一半、Ashkin 另一半
10  CPA 的世界影响 — 激光微加工、激光手术、视力矫正
11  学会服务 — Optica 编辑/副主席/主席、TRuST
12  荣誉与认可 — Order of Canada 2019 · NAS/FRS 2020 · Légion d'honneur 2022
13  "laser jock" — 实验者的自白（引语页，仅用白名单引语）
14  结尾
```

### 第 7–8 步：版式要点 + 陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖份额 | Strickland 与 Mourou **共享一半**，Ashkin 得另一半（工作互不相关）；勿写成三人平分 |
| 第三位女性 | page.md 明载（居里 1903、Goeppert Mayer 1963 之后）可写；但勿引申「史上唯一/首位加拿大女性诺奖物理」等未载口径 |
| 博士年份 | infobox 论文标 **1988**、正文获学位 **1989**——两个年份并存，写「论文 1988 / 获博士学位 1989」或择一加注 |
| CPA 论文 | 1985 *Compression of amplified chirped optical pulses*（Opt. Comm. 56(3):219–221）；infobox 论文标题大写与正文略异，以期刊页为准 |
| Williamson 注记 | 脚注载 Strickland 曾拟加 Steve Williamson 为作者、被对方以 "he hadn't done enough" 拒绝——正文一般无需展开；如写须按脚注原文 |
| 职称风波 | 获奖时仍非正教授引发评论；Strickland 回应从未申请，2018-10 告诉 BBC 已申请并升正教授——按原文两段写，勿简化成「因性别未升」 |
| 引语白名单 | 仅 page.md 英文原句可用："laser jock" 自述、"we thought we were good with our hands…" 段、"never applied / I do what I want to do" 段、"it would be a significant discovery"（转述）；**其余禁杜撰引语** |
| 机构时序 | NRC 1988–1991 → 利弗莫尔 1991–1992 → 普林斯顿 1992 起 → 滑铁卢 1997 起；勿混淆利弗莫尔与普林斯顿年份 |
| NAS/FRS | NAS 院士与 FRS 均为 2020，两条并列勿漏；教皇科学院 2021、澳科院通讯 2025 勿漏年份 |
| 配偶子女 | 夫 Dykaar（电气工程博士）、女 Hannah（天体物理）、子 Adam（喜剧方向）明载可写；子女不入库 |
| Optica 正名 | 2018 年前名 Optical Society of America（OSA）；正文用 Optica（formerly OSA）口径 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| chirped pulse amplification (CPA) | 啁啾脉冲放大 | 1985 论文核心词 |
| self-focusing | 自聚焦 | 损伤放大器的瓶颈机制 |
| table-top terawatt lasers | 桌面太瓦激光 | CPA 意义的形象说法 |
| ultrafast optics | 超快光学 | Main interests |
| intense laser-matter interactions | 强激光-物质相互作用 | Main interests 原词 |
| multi-photon ionization | 多光子电离 | 博士论文应用 |
| Raman generation | 拉曼产生 | 新波长技术 |
| mid-infrared / ultraviolet | 中红外 / 紫外 | 新波长范围 |
| presbyopia | 老花眼 | 眼晶状体微加工对象 |
| laser micromachining | 激光微加工 | CPA 应用 |
| Laboratory for Laser Energetics (LLE) | 激光能量学实验室 | 罗切斯特下属实验室，勿拼错 |
| Ultrafast Phenomena Section | 超快现象组 | NRC 时期归属 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（鼓舞/明亮/高受众）
- **匹配理由**：「突破性证明/年轻研究者」匹配 1985 年博士生论文问鼎诺奖的长线与 2018 年的破圈时刻；明亮基调贴合其 "laser jock" 的轻快自嘲。
- **备选**（未采用）：Daylight（明亮轻快，但叙事张力弱）；Shine Like The Sun（振奋，留给「光明结尾」更合的篇目）。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Donna_Strickland/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Donna_Strickland.yaml` | 社会关系/领域入库数据 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
