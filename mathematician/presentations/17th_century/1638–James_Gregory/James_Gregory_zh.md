# James Gregory（詹姆斯·格雷戈里）立传提示词

> qid=Q313906 · 1638-11 – 1675-10 · 苏格兰数学家/天文学家 · 17 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/James_Gregory/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**注意：本地 images.txt 无肖像**（仅签名图、书影、望远镜示意图）；执行时从 Wikimedia Commons 下载 **John Scougal 约 1675 年所绘格雷戈里肖像**（infobox 提及）至 `images/gregory_portrait.jpg`；失败则用签名图或装饰圆 `\faIcon{user}` 占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 苏格兰`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒（生卒年仅月）、国籍、出生地、家庭（母系数学传统）、教育、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「级数展开 / 镜筒光路」之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 0.5 模板机制（执行立传前必读）

> 黄金参照 `Johann_Bernoulli/Johann_Bernoulli_zh.tex` 逐帧改写；机械要点（14 帧结构 / 共享封面 `\input{../../cover/openmath_page.tex}` / Makefile 复制改 MAIN / 肖像下载与装饰圆占位 / `make distclean && make` 编译循环 / 已知陷阱）见 **`17th_century/TEMPLATE_GUIDE.md`**。

## 1. 背景信息（用于 Slide 1-3）

- **全名**：James Gregory（苏格兰原拼 **Gregorie**，中文：詹姆斯·格雷戈里）
- **生卒**：1638 年 **11 月**（无日）生于 Drumoak, Aberdeenshire → 1675 年 **10 月**（无日）逝于爱丁堡，享年 36。★ metadata 的 `1638-01-01` / `1675-01-01` 是占位日期，**不可采用**
- **国籍**：Kingdom of Scotland（苏格兰王国），现代对应英国/苏格兰——**是苏格兰人，不是英格兰人**
- **身份**：数学家、天文学家（"a Scottish mathematician and astronomer"）
- **家庭**：父 John Gregory（苏格兰圣公会牧师，1651 年去世）；母 Janet Anderson——其叔祖 **Alexander Anderson (1582–1619)** 是韦达（Viète）的学生兼编辑，"It was his mother who endowed Gregory with his appetite for geometry"；三兄弟中最幼，父死后由兄 David 负责教育；娶 Mary Jameson（画家 George Jameson 之女），其子 James 后任 King's College, Aberdeen 物理学教授
- **教育轨迹**：母启蒙几何 → Aberdeen Grammar School → **Marischal College, Aberdeen（1653–1657，1657 年 AM）** → 1664 赴帕多瓦大学（途经 Flanders、Paris、Rome），受教于 **Stefano Angeli**
- **关键中间人**：John Collins（数学通信枢纽）与 Robert Moray（苏格兰同胞、皇家学会创始人之一）——St Andrews 教席由 Charles II 设立，"probably upon the request of Robert Moray"

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **格雷戈里级数（1671 致 Collins 信）**：`arctan x = x − x³/3 + x⁵/5 − ⋯`——同信还给出 tan x、sec x、log sec x 等**七个函数的幂级数**。
2. **微积分基本定理的首次发表陈述与证明**：《Geometriae Pars Universalis》(1668)——"Gregory gave both the first published statement and proof of the fundamental theorem of the calculus (stated from a geometric point of view, and only for a special class of the curves...) for which he was acknowledged by Isaac Barrow."
3. **Taylor 级数的先行发现**："The first proof of the fundamental theorem of calculus and the discovery of the Taylor series can both be attributed to him."（他先于 Taylor 1715 发现高阶导数求幂级数法，但因"以为是重发现牛顿方法"而未发表）
4. **《Vera circuli et hyperbolae quadratura》(1667)**：用收敛级数逼近圆与双曲线面积，把圆与双曲线度量算到 20 多位小数。
5. **格雷戈里望远镜（1663《Optica Promota》）**：抛物面主镜 + 凹椭球面副镜的反射望远镜设计；"Gregory had no practical skill and he could find no optician capable of actually constructing one"——10 年后 Hooke 才造出实物。
6. **金星凌日测日地距离法**：《Optica Promota》提出，"later advocated by Edmund Halley and adopted as the basis of the first effective measurement of the Astronomical Unit"。
7. **衍射光栅的发现**：让日光穿过鸟羽观察衍射图样——"James Gregory discovered the diffraction grating by passing sunlight through a bird feather"；**晚于牛顿棱镜实验一年**（当时该现象仍 "highly controversial"）。
8. **开普勒问题的无穷级数解**：致 Collins 信中给出。
9. **圣安德鲁斯子午线（1673）**：在其实验室地板铺第一条子午线，"arguably making St Andrews the place where time began"（早于格林尼治 200 年）。
10. **与牛顿**："Gregory, an enthusiastic supporter of Newton, later had much friendly correspondence with him and incorporated his ideas into his own teaching"——经 Collins 收发牛顿的级数并回寄自己的结果。
11. **英年早逝**：约在就任爱丁堡数学教席一年后，"suffered a stroke while viewing the moons of Jupiter with his students. He died a few days later at the age of 36."——与学生观测木星卫星时中风，数日后去世。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（高地蓝） | `#274472` | 苏格兰高地 / 圣安德鲁斯 |
| 强调色（级数金） | `#C9A227` | 格雷戈里级数 / 被低估的天才 |
| 分类色 1（级数与微积分 — 靛蓝） | `#4C5FD5` | arctan 展开 / FTC / Taylor 先声 |
| 分类色 2（光学与望远镜 — 青绿） | `#0E7C7B` | 格雷戈里望远镜 / 衍射光栅 |
| 分类色 3（天文 — 琥珀） | `#E07B30` | 金星凌日 / 木星卫星观测 |
| 分类色 4（苏格兰学术 — 玫红） | `#B76E79` | 圣安德鲁斯 / 爱丁堡教席 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「级数项的收敛 / 镜筒光路」之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**苏格兰苍茫 / 天文台的静谧**（36 岁早逝的苏格兰天才）
- **匹配理由**：
  - 格雷戈里是望远镜与星空的人——需**静谧、苍茫**的配乐
  - "苍茫" 匹配其苏格兰高地出身与英年早逝的遗憾
  - "静谧" 匹配其天文观测与级数的收敛之美
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列已统一采用，保持一致）
  - 备选：巴洛克 / 17 世纪风格曲目
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「被低估的天才 · 格雷戈里级数」+ 詹姆斯·格雷戈里 1638–1675 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 国籍 / 出生地 / 母系数学传统 / 教育 / 核心领域）
3. **格雷戈里的一生：时间线**（`\timelineslide`）：1638-11 Drumoak 出生 → 1657 Marischal AM → 1663 《Optica Promota》→ 1667 《Vera quadratura》→ 1668 FTC 首次发表 / FRS / 圣安德鲁斯教席 → 1671 致 Collins 级数信 → 1673 子午线 / 转任爱丁堡 → 1675-10 观测中中风去世
4. **早年与教育**（`\earlyslide`）：牧师之家、母系韦达学脉、Marischal College、帕多瓦师从 Angeli
5. **格雷戈里级数**（核心贡献页，表格 + 公式框）：`arctan x = x − x³/3 + x⁵/5 − ⋯`、1671 信中七函数级数
6. **FTC 的首次发表证明**（核心贡献页，表格 + 公式框）：《Geometriae Pars Universalis》1668、几何形式、仅限特殊曲线类、巴罗致谢
7. **Taylor 级数的先行发现**（核心贡献页，表格 + 公式框）：高阶导数求幂级数、因"误以为重发现牛顿方法"未发表
8. **《Vera circuli et hyperbolae quadratura》**（核心贡献页，表格 + 公式框）：圆与双曲线的级数逼近、20 多位小数
9. **格雷戈里望远镜**（核心贡献页，表格 + 公式框）：1663 设计、主镜+椭球副镜、找不到光学匠、10 年后 Hooke 建成
10. **衍射光栅与金星凌日**（核心贡献页，表格 + 公式框）：鸟羽衍射（晚于牛顿棱镜一年）、测 AU 的金星凌日法（后为 Halley 采用）
11. **圣安德鲁斯与爱丁堡**（表格）：首任 Regius 数学教授、1673 子午线、"time began"轶事、后转爱丁堡
12. **与牛顿的通信**（表格）：经 Collins 的级数往来、支持牛顿、把牛顿思想纳入教学
13. **荣誉与传承**（表格）：FRS 1668、月球环形山 Gregory、St Andrews 的 James Gregory Telescope、级数以其命名
14. **终章**：36 岁、"观测木星卫星时倒下的天才"的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **生卒日期**：page.md 仅 "November 1638" / "October 1675"，**无具体日**；metadata 的 01-01 是占位符——封面写"1638 年 11 月 / 1675 年 10 月"。
- **"皇家学会创始会员"是误传**：原文 "Upon his return to London in 1668 he was elected a Fellow of the Royal Society"——是 1668 年**当选**；"one of the founders"字样原文只用于 Robert Moray——勿写格雷戈里为创始会员。
- **FTC 优先权表述**：必须带限制语——"first published statement and proof... (stated from a geometric point of view, and only for a special class of the curves...)"——勿写"证明了现代形式的 FTC"。
- **独立发现未发表**：原文 "did not publish his results, thinking he had only rediscovered 'Mr. Newton's universal method'"——"先于 Taylor 得到幂级数法但未发表"是原文依据；"Gregory–Newton 插值公式"**不在本页原文**，勿写。
- **望远镜表述**：1663 年即公开发表设计；建造者是 **Hooke（10 年后）**；"早于牛顿"的对比**原文无此句**——建议只写"1663 年发表设计"，不与牛顿直接对比。
- **衍射实验时间**：晚于牛顿棱镜色散实验**一年**——勿写"先于牛顿"。
- **e 的无理性证明**：page.md **完全未提及**——删去或另行查证。
- **与 Huygens 摆钟论战**：page.md **无此记载**（只有四边形求积中 "Following the example of Huygens"）——勿写。
- **死因**："suffered a stroke while viewing the moons of Jupiter with his students. He died a few days later at the age of 36."——与学生观测木星卫星时中风，表述准确。
- **爱丁堡任职年份**：原文未给——写"后转任爱丁堡数学教授"，勿编年份。
- **姓氏拼写**：苏格兰原拼 Gregorie——可在身份页注明。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q313906 | 待写入 |
| name_zh | 詹姆斯·格雷戈里 | 待写入 |
| name_en | James Gregory | 待写入 |
| birth_date | 1638-11（仅年月） | 待写入 |
| death_date | 1675-10（仅年月） | 待写入 |
| nationality | United Kingdom（Kingdom of Scotland） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / astronomy / optics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师 / 引路人**：Stefano Angeli（帕多瓦）、兄 David Gregory（教育）、母 Janet Anderson（几何启蒙）
- **关键中间人**：John Collins（通信枢纽）、Robert Moray（皇家学会创始人、促成教席）
- **通信 / 学术**：Isaac Newton（友好通信、经 Collins 收发级数）
- **承其衣钵**：其子 James Gregory（King's College, Aberdeen 物理学教授）、侄 David Gregory（FRS 1692）
- **家庭**：父 John Gregory（圣公会牧师）、妻 Mary Jameson

## 8. 奖项清单

- FRS（1668 当选）；荣誉体现为：格雷戈里级数/格雷戈里望远镜以他命名、月球环形山 Gregory、St Andrews 的 James Gregory Telescope

## 9. 机构清单

- 教育：Aberdeen Grammar School；Marischal College, Aberdeen（1653–1657，AM 1657）；University of Padua（1664 起，师从 Stefano Angeli）
- 任职：**首任 Regius Professor of Mathematics, University of St Andrews（1668 年末赴任）**；University of Edinburgh 数学教授（年份原文无载）

## 10. 终审清单

- [ ] 生卒"1638 年 11 月 / 1675 年 10 月"（无日），享年 36，出生地 Drumoak、逝世地 Edinburgh
- [ ] 国籍用「苏格兰」，历史政权注明苏格兰王国
- [ ] "FRS 1668 当选，非创始会员"表述准确
- [ ] FTC"首次发表陈述与证明、几何形式、仅限特殊曲线类"限制语在位
- [ ] "先于 Taylor 发现幂级数法但未发表"表述准确；勿写插值公式/e 无理性
- [ ] 望远镜"1663 发表设计、Hooke 10 年后建成"，不与牛顿直接对比
- [ ] 衍射实验"晚于牛顿棱镜一年"表述准确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/James_Gregory/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 Wikimedia Commons 下载 John Scougal c.1675 肖像，失败则签名图/装饰圆占位
- [ ] **国籍**：封面顶部徽章明示苏格兰
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 "The first proof of the fundamental theorem of calculus and the discovery of the Taylor series can both be attributed to him."）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（沃利斯 / 巴罗 / 牛顿）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
