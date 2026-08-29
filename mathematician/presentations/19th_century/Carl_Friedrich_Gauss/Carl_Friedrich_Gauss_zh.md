# Carl Friedrich Gauss（卡尔·弗里德里希·高斯）立传提示词

> qid=Q6722 · 1777-04-30 – 1855-02-23 · 德国数学家、天文学家、物理学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Carl_Friedrich_Gauss/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「数论格点 / 曲面」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Johann Carl Friedrich Gauss（拉丁名 Carolus Fridericus Gauss，中文惯称：高斯，尊称"数学王子" Princeps mathematicorum）
- **生卒**：1777-04-30 生于不伦瑞克（Brunswick，不伦瑞克-沃尔芬比特尔公国）→ 1855-02-23 逝于哥廷根，享年 77（心脏病）
- **国籍**：Germany（德国，出生时属不伦瑞克-沃尔芬比特尔公国，历经莱茵邦联、汉诺威王国）
- **身份**：数学家、天文学家、大地测量学家、物理学家（数论、代数、分析、几何、统计、地磁学）
- **家庭**：出身低微；父 Gebhard Dietrich Gauss（屠夫/泥瓦匠/园丁/丧葬基金出纳）；母 Dorothea（近乎文盲）；两段婚姻（Johanna Osthoff 1805 娶、1809 亡；Minna Waldeck 1810 娶、1831 亡），6 个子女
- **教育轨迹**：
  - 神童，1792–1795 就读 Collegium Carolinum（不伦瑞克公爵资助）
  - 1795–1798 就读哥廷根大学
  - 1799 年获 Helmstedt 大学博士学位（导师 Pfaff 评阅，in absentia 免口试）
- **导师**：Johann Friedrich Pfaff（博士导师）
- **研究领域**：数论、代数、数学分析、微分几何、静电学、光学、天文、大地测量、地磁学

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **神童轶事（1+2+...+100）**：小学时老师 Büttner 让全班求 1 到 100 之和，高斯迅速得出 5050（50 对 101）——虽是轶事，但体现其早慧。
2. **正十七边形（1796，19 岁）**：证明正十七边形可尺规作图，这是 2000 多年来正多边形作图的首次进展，使他从语文学转向数学。此发现开启了他著名的数学日记（1796–1814）。
3. **《算术研究》（Disquisitiones Arithmeticae，1801）**：现代数论奠基之作，引入同余记号 ≡，系统阐述二次互反律（他给出证明）、二次型、高斯合成律。
4. **代数基本定理**：给出第二、第三个完整证明（博士论文 1799 年即其一）。
5. **谷神星与最小二乘法**：1801 年用最小二乘法计算谷神星（Ceres）轨道，使其被重新发现；最小二乘法他**先于 Legendre 发现**（Legendre 1806 年才首次发表）。
6. **高斯曲率与绝妙定理（Theorema Egregium，1827）**：引入高斯曲率，证明曲率是内蕴量（等距变换下不变），是微分几何里程碑。
7. **非欧几何**：**首次发现并研究非欧几何**（并命名），但因谨慎未发表——由 Bolyai 与 Lobachevsky 独立发表。
8. **正态分布（高斯分布）**：最小二乘法的概率基础，正态分布以其命名。
9. **地磁学与物理**：1832 年**首次绝对测量地球磁场**；用球谐分析证明磁场大部分源自地球内部；1833 年与 Wilhelm Weber 合作发明**第一台电磁电报**；1821 年发明回照器（heliotrope）。
10. **快速傅里叶变换**：首次发展 FFT 算法，早于 Cooley–Tukey 约 160 年。
11. **算术-几何平均、超几何级数**：在椭圆函数与超几何级数理论中的奠基性工作。
12. **"不发表不完整的作品"**：以不发表未完成作品著称（"少而精"，印章上刻"Pauca sed matura"=少而成熟），导致许多发现被延迟传播。
13. **荣誉**：Lalande Prize（1809，行星理论）、Copley Medal（1838，地磁学）、Pour le Mérite 等；学生中有 Dedekind、Riemann、Listing、von Staudt 等。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（普鲁士深蓝） | `#1F3A93` | 德意志理性 / 哥廷根 |
| 强调色（数学金） | `#C9A227` | 数学王子 / 尊崇 |
| 分类色 1（数论 — 靛蓝） | `#4C5FD5` | 算术研究 / 二次互反律 |
| 分类色 2（微分几何 — 青绿） | `#0E7C7B` | 高斯曲率 / 绝妙定理 |
| 分类色 3（天文/物理 — 琥珀） | `#E07B30` | 谷神星 / 地磁学 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「数论格点 / 曲率」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典庄严 / 宏大理性**（"数学王子"的庄重与启蒙理性）
- **匹配理由**：
  - 高斯是 19 世纪数学的巅峰，贡献横跨数论、几何、天文、物理——需**庄严、宏大、理性**的配乐
  - "庄重" 匹配其"少而精"的治学风格与数学王子的地位
  - "宏大" 匹配其贡献的广度与深度
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄严/宏大风格）：
  - 首选：古典 / 庄严 / 宏大风格曲目
  - 备选：历史感深沉曲目（呼应 18-19 世纪之交）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「数学王子 · 数论、几何与天文的奠基者」+ 高斯 1777–1855 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：数论 / 微分几何 / 天文与最小二乘 / 物理与地磁 四分类
4. **神童与早年**（1777–1799）：1+100 轶事、正十七边形、数学日记、Helmstedt 博士
5. **《算术研究》与数论**（核心贡献页）：同余 ≡、二次互反律、二次型、高斯合成律
6. **代数基本定理与多项式**：第二、三个完整证明
7. **谷神星与最小二乘法**（核心贡献页）：轨道计算、先于 Legendre 的最小二乘法
8. **微分几何与绝妙定理**（核心贡献页）：高斯曲率、Theorema Egregium（1827）、非欧几何
9. **天文学与大地测量**（1807–1844）：哥廷根台长、汉诺威大地测量、回照器
10. **物理与地磁学**（核心贡献页）：1832 绝对测量地磁场、球谐分析、与 Weber 的电磁电报
11. **荣誉与传承**：Lalande Prize、Copley Medal、学生 Dedekind/Riemann、不发表未完成作品
12. **终章**：77 岁、"数学王子"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **最小二乘法归属**：Gauss **先于 Legendre 发现**，但 Legendre **先发表**（1806）——表述为"Gauss 先发现、Legendre 先发表"，勿写 Gauss 发表了最小二乘法。
- **非欧几何**：Gauss **首次发现并研究**（并命名），但**未发表**——由 Bolyai、Lobachevsky 独立发表。勿写 Gauss 发表了非欧几何。
- **代数基本定理**：Gauss 给出**第二、第三个**完整证明（第一个是 d'Alembert 的不完整证明）——勿写 Gauss 给出第一个证明。
- **1+100 轶事**：是**轶事（apocryphal）**，体现早慧，但需注明是传说。
- **正十七边形**：1796 年证明**可尺规作图**，是 2000 多年来正多边形作图的首次进展——勿写"发明了正十七边形"。
- **博士**：1799 年获 Helmstedt 大学博士（**非哥廷根**，常被误写），in absentia 免口试。
- **国籍**：metadata 国籍为 Confederation of the Rhine（莱茵邦联）、Kingdom of Hanover（汉诺威王国），均以"德国"为现代对应——封面用「德国」。
- **死亡**：1855-02-23 心脏病发作逝于哥廷根，葬于 Albani 公墓。
- **大脑研究**：高斯大脑被 Rudolf Wagner 研究（1492 克），但 2013 年发现**因标签错误大脑被混淆**（与医生 Conrad Heinrich Fuchs 的互换）——若提及需谨慎，属边缘轶事，建议略过或谨慎处理。
- **哥廷根七君子**：高斯的朋友 Weber 和女婿 Ewald 因抗议国王废宪被解职，高斯深受影响但无力相助——可作背景，非高斯本人被解职。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q6722 | 待写入 |
| name_zh | 高斯（或 卡尔·弗里德里希·高斯） | 待写入 |
| name_en | Carl Friedrich Gauss | 待写入 |
| birth_date | 1777-04-30 | 待写入 |
| death_date | 1855-02-23 | 待写入 |
| nationality | Germany | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | number theory / differential geometry / statistics / astronomy | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **博士导师**：Johann Friedrich Pfaff
- **学生**：Richard Dedekind、Bernhard Riemann、Johann Benedict Listing、Karl Georg Christian von Staudt、Christian Ludwig Gerling、Gotthold Eisenstein（非正式）、August Ferdinand Möbius、Moritz Stern 等
- **优先权 / 竞争**：Adrien-Marie Legendre（最小二乘法优先权）、Farkas Bolyai / János Bolyai（非欧几何）、Nikolai Lobachevsky（非欧几何）
- **通信 / 学术**：Sophie Germain（通信，化名 Le Blanc）、Heinrich Wilhelm Olbers（天文）、Wilhelm Eduard Weber（电磁电报合作）、Friedrich Wilhelm Bessel（帮助其获荣誉博士）
- **老师**：Abraham Gotthelf Kästner（数学教授）、Georg Christoph Lichtenberg（物理教授，深受敬重）
- **资助者**：Duke of Brunswick（不伦瑞克公爵，早年资助）

## 8. 奖项清单

- Lalande Prize（1809，行星理论与轨道测定）
- Copley Medal（1838，地磁学研究）
- Pour le Mérite for Sciences and Arts（科学与艺术功勋勋章）
- Fellow of the Royal Society（英国皇家学会会员）
- Bavarian Maximilian Order for Science and Art（巴伐利亚马克西米利安科学与艺术勋章）
- Fellow of the American Academy of Arts and Sciences

## 9. 机构清单

- 教育：Collegium Carolinum、University of Göttingen、University of Helmstedt（博士）
- 任职：University of Göttingen（1807 年起任天文学教授兼哥廷根天文台台长，直至去世）；Royal Academy of Sciences in Göttingen 院长

## 10. 终审清单

- [ ] 生卒 1777-04-30 / 1855-02-23，享年 77，出生地 Brunswick
- [ ] 最小二乘法"Gauss 先发现、Legendre 先发表"表述准确
- [ ] 非欧几何"Gauss 首发现未发表、Bolyai/Lobachevsky 独立发表"表述准确
- [ ] 代数基本定理"第二、三个完整证明"表述准确
- [ ] 1+100 轶事注明"传说"
- [ ] 博士"Helmstedt 大学、in absentia"表述准确（非哥廷根）
- [ ] 正十七边形"2000 年来首次进展"表述准确
- [ ] 国籍用「德国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Carl_Friedrich_Gauss/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先标准肖像（`images.txt` 中 Bendixen 1828 肖像或 Jensen 1840 肖像或 Schwartz 1803 粉彩画青年高斯）
- [ ] **国籍**：封面顶部徽章明示德国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如印章"Pauca sed matura"）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Fourier / Legendre / Abel）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
