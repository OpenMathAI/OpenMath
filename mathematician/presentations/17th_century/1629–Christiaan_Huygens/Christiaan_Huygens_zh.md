# Christiaan Huygens（克里斯蒂安·惠更斯）立传提示词

> qid=Q39599 · 1629-04-14 – 1695-07-08 · 荷兰数学家/物理学家/天文学家 · 17 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/Christiaan_Huygens/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。images.txt 有多幅肖像可用：**Jean-Jacques Clérion 浮雕（c.1670）或 Bernard Vaillant 粉彩（1686）**，下载至 `images/huygens_portrait.jpg`。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 荷兰`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、国籍、出生地、父兄、师承、教育、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「摆的弧线 / 光的波前」之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 0.5 模板机制（执行立传前必读）

> 黄金参照 `Johann_Bernoulli/Johann_Bernoulli_zh.tex` 逐帧改写；机械要点（14 帧结构 / 共享封面 `\input{../../cover/openmath_page.tex}` / Makefile 复制改 MAIN / 肖像下载与装饰圆占位 / `make distclean && make` 编译循环 / 已知陷阱）见 **`17th_century/TEMPLATE_GUIDE.md`**。

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Christiaan Huygens（克里斯蒂安·惠更斯，Lord of Zeelhem，FRS）
- **生卒**：1629-04-14 生于海牙 → 1695-07-08 逝于海牙，享年 66；葬于 Grote Kerk **无标记的墓**。★ metadata 的 date_of_death 双值含 1695-06-08，以 infobox **1695-07-08** 为准
- **国籍**：Dutch Republic（荷兰共和国），现代对应荷兰
- **身份**：数学家、物理学家、天文学家、发明家（"Dutch mathematician, physicist, engineer, astronomer, and inventor"）
- **家庭**：父 Constantijn Huygens（Orange 王朝外交顾问、**诗人与音乐家**，通信对象含伽利略、梅森、笛卡尔）；母 Suzanna van Baerle（产妹后早逝）；五子女排行第二，兄 Constantijn Huygens Jr.（后为其遗著《Cosmotheoros》出版人）；**终身未婚，无子女**
- **教育轨迹**：
  - 16 岁前家庭教育（1644 年数学教师 Jan Jansz Stampioen）
  - 莱顿大学 1645–1647 学**法律与数学**（Frans van Schooten Jr. 应笛卡尔建议为兄弟俩的私人导师，"brought Huygens's mathematical education up to date"）
  - Orange College of Breda 1647–1649（随英国讲师 John Pell 学数学）
- **导师**：Frans van Schooten（infobox Academic advisors）；早年 Stampioen

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **摆钟（1656 发明 / 1657 专利）**："invented the pendulum clock, which was a breakthrough in timekeeping and became the most accurate timekeeper for almost 300 years until the 1930s"。
2. **《摆钟论》Horologium Oscillatorium（1673）**："the first modern work on mechanics"——证明摆线为等时曲线（tautochrone）、发展渐屈线理论、复摆振动中心；献给路易十四。
3. **单摆周期公式**：`T = 2π√(l/g)`——"the first to derive the formula for the period of an ideal mathematical pendulum"。
4. **离心力公式**：`F_c = mω²r`（1659《De Vi Centrifuga》），"a decade before Isaac Newton"。
5. **《论赌博中的计算》De Ratiociniis in Ludo Aleae（1657）**：期望值理论——"Huygens took from Pascal the concepts of a 'fair game'... and extended the argument to set up a non-standard theory of expected values"；其期望值思想后来启发雅各布·伯努利的概率论（传承链：帕斯卡→惠更斯→雅各布）。
6. **弹性碰撞定律**：《De Motu Corporum ex Percussione》（1656 完稿/1703 出版），"first identified the correct laws of elastic collision"。
7. **土星环与泰坦**：1655-03-25 发现土星最大卫星 Titan；1659《Systema Saturnium》提出土星环是 "a thin, flat ring, nowhere touching, and inclined to the ecliptic"；测定火星自转约 24½ 小时。
8. **光的波动说**：1678 年宣读 / 1690 年出版《Traité de la Lumière》——"the first fully mathematized, mechanistic explanation of an unobservable physical phenomenon"，即惠更斯原理（今 Huygens–Fresnel principle）。
9. **惠更斯目镜（1662）**：两片平凸透镜减小色散。
10. **力学方法论**：图挽救"the first modern work on mechanics where a physical problem is idealized by a set of parameters then analysed mathematically"。
11. **皇家学会首位外籍会员**："elected Huygens a Fellow in 1663, making him its first foreign member when he was just 34 years old"；1666 年受 Colbert 之邀赴巴黎出任新成立的法国科学院领导职位。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（海牙蓝） | `#33628C` | 荷兰共和国 / 荷兰黄金时代 |
| 强调色（奥兰治橙金） | `#D08428` | 荷兰王室色 / 摆钟黄铜 |
| 分类色 1（钟表与力学 — 靛蓝） | `#4C5FD5` | 摆钟 / 摆钟论 / 离心力 |
| 分类色 2（光学 — 青绿） | `#0E7C7B` | 波动说 / 惠更斯原理 / 目镜 |
| 分类色 3（天文 — 琥珀） | `#E07B30` | 泰坦 / 土星环 / 星云 |
| 分类色 4（概率 — 玫红） | `#B76E79` | 论赌博中的计算 / 期望值 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「摆的弧线 / 光的波前涟漪」之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**荷兰黄金时代 / 钟摆般精准优雅**（17 世纪荷兰科学巨匠）
- **匹配理由**：
  - 惠更斯是"精准"的化身（摆钟）——需**优雅、精准、绵长**的配乐
  - "精准" 匹配其钟表与天文测量的气质
  - "优雅" 匹配其荷兰黄金时代与巴黎科学院岁月
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列已统一采用，保持一致）
  - 备选：巴洛克 / 荷兰黄金时代风格曲目（斯韦林克气质）
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「摆钟之父 · 光的波动说」+ 克里斯蒂安·惠更斯 1629–1695 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 国籍 / 出生地 / 父兄 / 师承 / 教育 / 核心领域）
3. **惠更斯的一生：时间线**（`\timelineslide`）：1629 海牙出生 → 1645 莱顿（van Schooten）→ 1655 发现泰坦 → 1656/57 摆钟专利 → 1657 概率论著作 → 1663 皇家学会首位外籍会员 → 1666 赴巴黎 → 1673 《摆钟论》→ 1681 返荷 → 1690 《光论》→ 1695 去世
4. **早年与教育**（`\earlyslide`）：诗人外交官之子、莱顿学法律与数学、van Schooten 的近代化数学教育、"new Archimedes"（梅森语）
5. **摆钟与《摆钟论》**（核心贡献页，表格 + 公式框）：1657 专利、摆线等时、渐屈线、"第一部现代力学著作"
6. **单摆周期与离心力**（核心贡献页，表格 + 公式框）：`T = 2π√(l/g)`、`F_c = mω²r`（早于牛顿十年）
7. **弹性碰撞**（核心贡献页，表格 + 公式框）："first identified the correct laws of elastic collision"、伽利略不变性
8. **概率论与期望值**（核心贡献页，表格 + 公式框）：1657《论赌博中的计算》、承帕斯卡启伯努利
9. **土星环与泰坦**（核心贡献页，表格 + 公式框）：1655 发现泰坦、"thin, flat ring, nowhere touching"
10. **光的波动说**（核心贡献页，表格 + 公式框）：惠更斯原理、《Traité de la Lumière》1690、当时不敌牛顿微粒说
11. **光学仪器**（核心贡献页，表格 + 公式框）：惠更斯目镜、与兄磨镜、无筒空中望远镜
12. **学者网络**（表格）：梅森（"new Archimedes"）、帕斯卡、莱布尼茨（1672–76 受其指导）、牛顿（1689 会面通信）、与胡克的游丝优先权之争
13. **荣誉与传承**（表格）：皇家学会首位外籍会员、法国科学院领导职位、Cassini–Huygens 探测器（2005 着陆泰坦）
14. **终章**：66 岁、"洞察之深与成果之丰仅次于牛顿"（Aldersey-Williams 语）的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **卒日**：metadata 双值含 1695-06-08，以 infobox **1695-07-08** 为准。
- **"皇家学会创始会员"是误传**：原文是 "**first foreign member** when he was just 34 years old"（首位外籍会员，1663）——**勿写 founding member**。
- **波动说当时居弱势**：原文 "His theory of light was not widely accepted, while Newton's rival corpuscular theory of light, as found in his Opticks (1704), gained more support."——直到 Young/Fresnel 时代才翻案；勿写"波动说战胜微粒说"于 17 世纪。
- **概率论表述**：承帕斯卡"公平博弈"概念再扩展成期望值理论；**"与帕斯卡 1654 年通信"原文无载**（只有 1655 访巴黎后接触其成果）；"第一部概率论著作"字样原文未直接使用，宜用"the most coherent presentation of a mathematical approach to games of chance"或"首部成书"措辞并核实。
- **摆钟发明权**：专利 1657，荷兰制表人 **Salomon Coster** 承造（巴黎由 Isaac II Thuret 制造）；法国拒绝授权、Rotterdam 的 Simon Douw 与伦敦的 Fromanteel 1658 年仿制；**与伽利略后人的摆钟优先权之争原文无载**，勿写。
- **游丝优先权（与 Hooke）**：各自独立发明，争议持续数百年；2006 年新发现的胡克手稿笔记"presumably tipping the evidence in Hooke's favour"——如实呈现。
- **悬链线命名**：catenaria 一名是 1690 年与莱布尼茨通信中所起——年份勿错。
- **葬礼**：葬于 Grote Kerk 无标记的墓，终身未婚——"晚年孤独"由这些事实组合表述，勿杜撰具体死因疾病。
- **metadata 冲突**：educated_at 含 University of Angers（page.md 未提，弃用）；occupation 含 entomologist（正文无展开，慎用）。
- **称号**："摆钟之父"可用；惠更斯对牛顿的评价原文支持 "rivaled only by Newton in both depth of insight and the number of results obtained"（Legacy 节）。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q39599 | 待写入 |
| name_zh | 克里斯蒂安·惠更斯 | 待写入 |
| name_en | Christiaan Huygens | 待写入 |
| birth_date | 1629-04-14 | 待写入 |
| death_date | 1695-07-08 | 待写入 |
| nationality | Netherlands（Dutch Republic） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / physics / astronomy / optics / probability / horology | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：Frans van Schooten Jr.（莱顿）、Jan Jansz Stampioen（早年）
- **学生 / 提携**：Gottfried Wilhelm Leibniz（1672–1676 巴黎，"tutored in mathematics by Huygens until 1676"）
- **通信 / 学术**：Marin Mersenne（梅森称其 "new Archimedes"）、René Descartes（其父之友，赞其几何才华）、Blaise Pascal（承其概率思想）、Galileo Galilei（其父通信圈）、Isaac Newton（1689 会面与通信）、John Pell、Robert Moray、Henry Oldenburg
- **论战 / 竞争**：Robert Hooke（游丝优先权）、Simon Douw / Ahasuerus Fromanteel（摆钟仿制）、Hevelius（水星凌日记录之争）、Descartes 碰撞定律（证明其 largely wrong）
- **家庭**：父 Constantijn Huygens（诗人外交官）、兄 Constantijn Huygens Jr.（遗著出版人）；终身未婚

## 8. 奖项清单

- 无近代意义奖项记载；荣誉体现为：皇家学会 Fellow（1663，**首位外籍会员**）、法国科学院领导职位（1666）、月球环形山惠更斯（Huygenian region）、惠更斯目镜/惠更斯原理以其命名、ESA Cassini–Huygens 任务（2005 Huygens 探测器着陆泰坦）

## 9. 机构清单

- 教育：Leiden University（1645–1647，法律与数学）；Orange College of Breda（1647–1649）
- 任职：法国科学院（Académie Royale des Sciences，1666–1681，Colbert 之邀的领导职位，居巴黎天文台）；1681 因病返荷，1685 南特敕令废止后无法返法

## 10. 终审清单

- [ ] 生卒 1629-04-14 / 1695-07-08，享年 66，出生地/逝世地均 The Hague
- [ ] 国籍用「荷兰」
- [ ] "皇家学会首位外籍会员（1663）"表述准确，勿写创始会员
- [ ] 波动说"当时不敌牛顿微粒说、19 世纪翻案"表述准确
- [ ] 概率论"承帕斯卡、启雅各布·伯努利"传承链表述准确
- [ ] 摆钟"Coster 承造、仿制者众、海上计时不成功"限定语在位
- [ ] 游丝与胡克各自独立、2006 年档案似有利于胡克——如实呈现
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Christiaan_Huygens/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 Clérion 浮雕或 Vaillant 粉彩肖像（images.txt 有链接）
- [ ] **国籍**：封面顶部徽章明示荷兰
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 "a thin, flat ring, nowhere touching, and inclined to the ecliptic"）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（帕斯卡 / 牛顿 / 雅各布·伯努利）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
