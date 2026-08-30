# Ferdinand Georg Frobenius（费迪南德·格奥尔格·弗罗贝尼乌斯）立传提示词

> qid=Q57228 · 1849-10-26 – 1917-08-03 · 德国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Ferdinand_Georg_Frobenius/`（page.md + metadata.json）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「自相似 / 群作用」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Ferdinand Georg Frobenius（中文惯称：弗罗贝尼乌斯）
- **生卒**：1849-10-26 生于柏林郊区的夏洛滕堡（Charlottenburg）→ 1917-08-03 逝于柏林，享年 67
- **国籍**：Kingdom of Prussia（普鲁士王国）/ German Empire（德意志帝国）
- **身份**：数学家、大学教师（群表示论、群特征标理论奠基人）
- **父母**：父 Christian Ferdinand Frobenius（新教牧师）；母 Christine Elizabeth Friedrich
- **教育轨迹**：
  - 1860 年入 Joachimsthal Gymnasium（近 11 岁）
  - 1867 年毕业后入哥廷根大学（仅一学期）
  - 返回柏林，先后听 Leopold Kronecker、Ernst Kummer、Karl Weierstrass 的课
  - 1870 年获博士学位（Weierstrass 指导，以优等授予），博士论文研究微分方程的解
- **任职轨迹**：
  - 中学教师：Joachimsthal Gymnasium → Sophienrealschule
  - 1874 年：柏林大学数学副教授（extraordinary professor）
  - **1875–1892 年：苏黎世理工学院（ETH Zürich）正教授，共 17 年**——在此结婚、成家，并完成大量跨领域重要工作
  - 1891 年 12 月 Kronecker 去世，柏林教席空缺；Weierstrass 力荐 Frobenius 接任
  - **1893 年回柏林**，当选普鲁士科学院（Prussian Academy of Sciences）院士
- **研究领域**：群论、表示论、数论、微分方程、椭圆函数、代数（双线性型 / 二次型）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **群论奠基（后半生主方向）**：给出 Sylow 定理的**抽象群**证明（此前证明仅对置换群），第一 Sylow 定理（存在性）的证明至今仍被广泛使用。
2. **群特征标与群表示理论**：1896 年第一篇特征标论文构造了 PSL(2,p) 的特征标表；创立群特征标与群表示理论，成为研究群结构的基本工具；导出 Frobenius 互反律、定义 Frobenius 群。
3. **Frobenius 群与一个百年猜想**：若 n 整除有限群 G 的阶，则 x^n=1 的解数为 k·n；猜想 k=1 时解集构成子群——该猜想直到 1991 年（有限单群分类完成后）才被完全证明。
4. **数论：Frobenius 自同构 / 元素 / 共轭类**：给出把素数典范地映到 Galois 群共轭类的方法（Frobenius conjugacy class / Frobenius element），推广 Dirichlet 素数定理，是研究无穷次扩张 Galois 群的关键构造。
5. **微分方程：Frobenius 方法**：在标准 Taylor 级数法失效的正则奇点处，用幂级数法解线性变系数常微分方程，该算法今称 Frobenius 方法。
6. **Cayley–Hamilton 定理首个完整证明**；最早引入有理函数逼近（今称 Padé 逼近）；Frobenius–Stickelberger 公式（椭圆函数行列式恒等式）。
7. **以 Frobenius 命名的海量成果**：Frobenius 范数 / 内积（矩阵）、Perron–Frobenius 定理（非负矩阵）、Frobenius 流形（现代数学物理）等，横跨代数、分析、几何、数学物理。
8. **学术传承**：博士生含 Richard Fuchs、Edmund Landau、Issai Schur、Konrad Knopp、Walter Schnee 等；Schur 继承其表示论衣钵。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（普鲁士深蓝） | `#1A237E` | 柏林 / 普鲁士学术传统 |
| 强调色（学术金） | `#C9A227` | 普鲁士科学院 / 奠基性贡献 |
| 分类色 1（群表示 — 靛蓝） | `#4C5FD5` | 群论与表示论 |
| 分类色 2（数论 — 青绿） | `#0E7C7B` | Frobenius 自同构 |
| 分类色 3（微分方程 — 琥珀） | `#E07B30` | Frobenius 方法 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「群作用下的轨道 / 共轭类」与「自相似」的视觉语言（与 Wilson 的自相似气泡背景一致）。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**: **Timeless** — Alex-Productions（沉稳 / 纪录片 / 长期纲领）
- **风格**: 沉稳纪录片风，呼应群表示论「永恒的结构语言」
- **匹配理由**:
  - "永恒" 完美匹配 Frobenius 的贡献本质 —— 群表示论与特征标理论不是单一技巧，而是研究群结构的**永久框架**：对称性的分解、群作用的轨道、共轭类——这些结构跨越一个世纪仍是表示论的核心语言
  - "沉稳" 匹配其气质 —— 普鲁士柏林学术传统的严谨克制，从柏林到苏黎世再到柏林科学院，理论纵深胜过戏剧张力
  - "纪录片" 匹配传记叙事 —— 夏洛滕堡牧师之家 → 柏林受业于 Weierstrass/Kronecker → ETH 17 年 → 回柏林接替 Kronecker 教席，是思想演进的纪录，而非英雄史诗
- **备选** (未采用):
  - ★★★ Monumental — "纪念碑式/奠基性" 匹配群表示论的奠基地位，但气势过宏，与 Frobenius 克制的学者气质略不匹配
  - ★★ Beethoven Symphony No. 7 — "律动庄严" 匹配普鲁士古典学术，但古典乐气质偏重，纪录片叙事感弱于 Timeless
  - ★★ PAST — "历史感深沉" 匹配 19 世纪柏林学术传统，但更适合黎曼式「猜想悬置」的怅惘，而非 Frobenius 式的「结构奠基」
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → `presentations/19th_century/Ferdinand_Georg_Frobenius/Timeless.wav`
- **时长**: 128 秒 > 12 页 × 7 秒 ≈ 84 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「群表示论的奠基人」+ 弗罗贝尼乌斯 1849–1917 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 任职 / 荣誉 / 核心领域）
3. **弗罗贝尼乌斯的一生：时间线**（`\timelineslide`）：1849 出生 → 1870 博士 → 1875 苏黎世 → 1893 回柏林 → 1896 特征标 → 1917 去世
4. **早年与教育**（1849–1874，表格）：夏洛滕堡出生、牧师之家、Joachimsthal Gymnasium、哥廷根一学期、柏林听 Kronecker/Kummer/Weierstrass、1870 博士
5. **苏黎世岁月**（1875–1892，表格）：ETH 17 年、成家、跨领域高产
6. **群论与表示论**（核心贡献页，表格 + Frobenius 互反律公式框）：Sylow 定理抽象群证明、特征标理论、Frobenius 互反律、Frobenius 群
7. **数论：Frobenius 自同构**（核心贡献页，表格 + Frobenius 元素公式框）：素数到 Galois 群共轭类的典范映射、推广 Dirichlet 定理
8. **微分方程：Frobenius 方法**（核心贡献页，表格 + 方法公式框）：正则奇点幂级数法
9. **以 Frobenius 命名的成果**（表格）：Frobenius 范数 / 内积、Perron–Frobenius、Frobenius 流形、Padé 逼近、Cayley–Hamilton 证明
10. **学术传承**（表格）：Landau、Schur、Knopp 等门生
11. **回柏林与科学院**（1893–1917，表格）：接替 Kronecker、普鲁士科学院院士
12. **终章**：67 岁、遗产与历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **导师归属**：metadata `doctoral_advisor` 含 Ernst Kummer 与 Karl Weierstrass 两人；但 Wikipedia 正文明确「supervised by Weierstrass」——正文写「Weierstrass 指导」，Kummer 列为「柏林受业教师」而非博士导师，勿混淆。
- **Frobenius 群猜想**：k=1 时解集构成子群，直到 1991 年（有限单群分类完成后）才被完全证明，勿写成「已证多年」或「Frobenius 本人证明」。
- **Sylow 定理归属**：Frobenius 给出**抽象群**的证明，Sylow 定理本身归属 Ludwig Sylow，勿写成「Frobenius 发现 Sylow 定理」。
- **Perron–Frobenius 定理**：非负矩阵的谱性质，与 Oskar Perron 共同命名，Frobenius 是后者（1912 年论文），勿写独占。
- **Cayley–Hamilton 定理**：Frobenius 给出**首个完整（一般情形）证明**，定理本身归属 Cayley 与 Hamilton。
- **Padé 逼近**：Frobenius 最早引入有理函数逼近思想，今称 Padé 逼近（以 Henri Padé 命名），注意「最早引入」与「命名」之别。
- **国籍表述**：生卒横跨普鲁士王国与德意志帝国，封面顶部用「德国」作为现代对应（与 Klein 的 Germany 处理一致）。
- **生卒核对**：1849-10-26 / 1917-08-03，享年 67，metadata 与正文一致。
- **出生地**：Charlottenburg 是柏林郊区（夏洛滕堡），勿与柏林市中心混淆。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q57228 | 待写入 |
| name_zh | 费迪南德·格奥尔格·弗罗贝尼乌斯（或 弗罗贝尼乌斯） | 待写入 |
| name_en | Ferdinand Georg Frobenius | 待写入 |
| birth_date | 1849-10-26 | 待写入 |
| death_date | 1917-08-03 | 待写入 |
| nationality | Kingdom of Prussia / German Empire | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | algebra / group theory / topology | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **博士导师**：Karl Weierstrass（新建）、Ernst Kummer（新建，柏林受业教师）
- **柏林受业教师**：Leopold Kronecker（新建）
- **学生（代表性）**：Richard Fuchs、Edmund Landau、Issai Schur、Konrad Knopp、Walter Schnee、Ernst Jacobsthal、Robert Remak 等（metadata `doctoral_student` 全量）
- **被接替者 / 教席前任**：Leopold Kronecker（1891 去世后其柏林教席空缺）

## 8. 奖项清单

- 1893 年当选普鲁士科学院（Prussian Academy of Sciences）院士
- （metadata 无 `award_received` 字段，Frobenius 生前荣誉以科学院院士为主，勿杜撰其他奖项）

## 9. 机构清单

- 教育：University of Göttingen（1867）、Frederick William University Berlin（现柏林洪堡大学，1870 博士）、Joachimsthalsches Gymnasium
- 任职：Joachimsthal Gymnasium（中学教师）、Sophienrealschule（中学教师）、University of Berlin（1874 副教授）、ETH Zurich（1875–1892 正教授）、University of Berlin（1893–1917 正教授）

## 10. 终审清单

- [ ] 导师归属正确（Weierstrass 指导，Kummer/Kronecker 为受业教师）
- [ ] Frobenius 群猜想 1991 年证明，时间线准确
- [ ] Sylow 定理归属 Ludwig Sylow，Frobenius 给抽象群证明
- [ ] Perron–Frobenius 与 Perron 共同命名
- [ ] Cayley–Hamilton 定理「首个完整证明」措辞准确
- [ ] Padé 逼近「最早引入 / 今称」措辞准确
- [ ] 国籍用「德国」现代对应，生卒 1849-10-26 / 1917-08-03
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Ferdinand_Georg_Frobenius/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先 Wikipedia infobox 照片（`images.txt`）；无则用装饰圆占位
- [ ] **国籍**：封面顶部徽章明示德国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到，否则忠实转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Klein / Riemann）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**

---

## Review-1 记录 (2026-08-20)

> 结合本地 Wikipedia (`pages/Ferdinand_Georg_Frobenius/page.md` + `metadata.json`) 逐页比对。

- **头像** ✅：`images/Ferdinand_Georg_Frobenius.jpeg`（竖版 373×536 JPEG，已提供）。封面右上角圆角裁剪 `clip[rounded corners=4pt]` 2.0×2.9cm + 姓名小字注；身份信息页左侧竖版裁剪 2.6×3.5cm。原「无肖像存世」占位符已移除。
- **国籍** ✅：封面顶部 `\faIcon{globe}\enspace 德国`，身份信息页 `德国（普鲁士王国）`（Wikidata nationality: ["Kingdom of Prussia"]，用「德国」现代对应）。
- **身份信息页** ✅：Slide 2 已存在（`\profileslide`），涵盖生卒/本名/国籍/师承/任职/荣誉/核心领域，符合 Wilson 模板硬性要求。
- **事实复核**：生卒(1849-10-26~1917-08-03, 67岁)/Charlottenburg 出生(柏林郊区)/父 Christian Ferdinand Frobenius(新教牧师)/母 Christine Elizabeth Friedrich/1860 入 Joachimsthal Gymnasium(近11岁)/1867 哥廷根一学期/柏林听 Kronecker·Kummer·Weierstrass 课/1870 博士(Weierstrass 指导,优等)/1874 柏林大学副教授/1875–1892 ETH Zürich(十七年,成家)/1891-12 Kronecker 去世/1893 回柏林接替其教席并当选普鲁士科学院院士/1917-08-03 逝于柏林——全部与 Wikipedia 一致。
- **核心贡献复核**：Sylow 定理抽象群证明(第一 Sylow 存在性)、1896 特征标论文 PSL(2,p) 特征标表、Frobenius 互反律、Frobenius 群、Frobenius 群猜想(1991 有限单群分类后证明)、Frobenius 自同构/元素/共轭类(推广 Dirichlet 定理)、Frobenius 方法(正则奇点)、Cayley–Hamilton 首个完整证明、Padé 逼近最早引入、Perron–Frobenius 定理(与 Perron 共同命名)、Frobenius 流形——全部准确，无杜撰。
- **门生**：Issai Schur、Edmund Landau、Konrad Knopp、Richard Fuchs、Walter Schnee、Ernst Jacobsthal、Robert Remak 等，与 metadata `doctoral_student` 一致。
- **编译**：`make distclean && make` → ✅ 13 页，0 错误。

## Review-2 记录 (2026-08-20)

> 结构优化 + Overfull 修复 + 编译验证。

- **Overfull 修复**：
  1. **profileslide（身份信息页）**：原 Overfull hbox 24.125pt + vbox 3.563pt。根因是头像 3.0×3.9cm 过大 + 信息网格 `text width=4.8cm` 过宽 + 位置过于靠边。修复：头像缩至 2.6×3.5cm（位置 -6.15→-6.0）、infob `text width=4.8cm→4.35cm`、`inner xsep=10pt→9pt`、`inner ysep=9pt→8pt`、字号 7.4/9.4→7.2/9.2、四节点位置收拢（±1.8→±1.6 / ±3.8→±3.5，纵向 2.35/2.01→2.3/1.85）。
  2. **namedslide（以 Frobenius 命名的成果）**：原 Overfull hbox 10.43pt。根因是 4 个成果卡片 `text width=3.05cm` 过宽。修复：`text width=3.05cm→2.85cm`、`inner xsep=7pt→6pt`、字号 6.6/8.6→6.5/8.5、位置收拢（±5.4→±5.3 / ±1.8→±1.77）。
- **结果**：仅剩 Overfull hbox 3.92pt（<10pt 可接受），0 错误。
- **编译**：`make distclean && make` → ✅ 13 页，169 比例（453.54×255.12 pts），肖像已嵌入（PDF 167KB→201KB）。
