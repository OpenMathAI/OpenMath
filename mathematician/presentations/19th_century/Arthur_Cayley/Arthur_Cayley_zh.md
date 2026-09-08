# Arthur Cayley（阿瑟·凯莱）立传提示词

> qid=Q159430 · 1821-08-16 – 1895-01-26 · 英国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Arthur_Cayley/`（page.md + metadata.json + images.txt）
>
> **立传状态：✅ 已完成（参考高斯基准模板）**——tex（13 页正文）+ Makefile + 头像就位，`make distclean && make` 编译通过、Overfull = 0；头像采用 Wikipedia Commons 标准照片（`images/cayley_portrait.jpg`，经 API 查询条目主图获得）；BGM 已选 `Timeless`（alex-productions，沉稳/纪录片，契合"长期纲领"），视频 `make video` 已生成。

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「群 / 矩阵」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Arthur Cayley（中文惯称：凯莱）
- **生卒**：1821-08-16 生于里士满（Richmond，萨里，英格兰）→ 1895-01-26 逝于剑桥，享年 73
- **国籍**：United Kingdom of Great Britain and Ireland（英国）
- **身份**：数学家（抽象群、矩阵、代数几何、组合学）
- **家庭**：父 Henry Cayley（商人，航空先驱 George Cayley 的远房堂亲，定居圣彼得堡）；Arthur 在圣彼得堡度过人生前 8 年；弟 Charles Bagot Cayley（语言学家）
- **教育轨迹**：
  - 14 岁入 King's College School（数学天赋被校长察觉）
  - 17 岁入剑桥三一学院（导师 George Peacock，私人教练 William Hopkins）
  - 获 Senior Wrangler（剑桥数学考试第一名）与 Smith's Prize（第一名）
- **导师**：George Peacock、William Hopkins
- **研究领域**：群论、矩阵理论、代数几何、图论、组合学

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **抽象群概念（最著名贡献）**：**第一个定义抽象群**概念（满足一定律的二元运算集合），区别于 Galois 的置换群概念——是现代群论的开端。
2. **Cayley–Hamilton 定理**：提出并验证（对 2 阶、3 阶矩阵）"每个方阵都是其特征多项式的根"，是线性代数的基本定理。
3. **Cayley 定理**：每个群都同构于某个置换群——群论的基本定理。
4. **Cayley 公式**：n 个标号顶点上有 n^(n−2) 棵树，是组合学的经典结果（开创性地使用生成函数）。
5. **Cayley 图、Cayley 表**：以他命名的群论与图论工具。
6. **八元数（Cayley 代数）**：Cayley–Dickson 构造，八元数（octonion）代数。
7. **代数几何**：与 George Salmon 共同发现三次曲面上的 27 条直线；创立直纹曲面（ruled surface）的代数几何理论。
8. **与 Sylvester 的长期合作**：在 Lincoln's Inn 当律师期间与 Sylvester 散步讨论不变量理论，14 年间产出两三百篇论文。
9. **生平**：曾当律师 14 年（conveyancing 专业）；1863 年（42 岁）任剑桥 Sadleirian 纯数学教授（首任），任职 35 年，放弃了高薪法律职业而选择微薄薪水，但从未后悔。
10. **荣誉与高产**：全集 13 卷、967 篇论文；Copley Medal（1882）、Royal Medal（1859）、De Morgan Medal（1884）、FRS；21 世纪仍有 200 多篇数学论文引用其工作。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（英国深蓝） | `#1F3A93` | 英伦理性 |
| 强调色（数学金） | `#C9A227` | 抽象群 / 尊崇 |
| 分类色 1（群论 — 靛蓝） | `#4C5FD5` | 抽象群 / Cayley 定理 |
| 分类色 2（矩阵/线性代数 — 青绿） | `#0E7C7B` | Cayley–Hamilton / 行列式 |
| 分类色 3（代数几何/组合 — 琥珀） | `#E07B30` | 27 直线 / Cayley 公式 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「群 / 矩阵」的视觉语言。

### 3.5 背景音乐选择 ✅ 【已选定】

- **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
- **选定曲目**：**Timeless**（Alex-Productions，优先级 2，`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`，已软链为 `bgm.wav`）
- **匹配理由**：标签"沉稳 / 纪录片"，适用场景"代数几何、数论、长期纲领"——契合凯莱 967 篇论文、13 卷全集的长期结构化遗产与维多利亚学者的从容
- （Poncelet 已用 The Flow of Time，Cayley 改用 Timeless 避免重复）

## 4. Slide 规划（实际 13 页正文 + OpenMath 封面，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「抽象群与矩阵理论的奠基者」+ 凯莱 1821–1895 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1821 圣彼得堡童年 → 1842 Senior Wrangler → 1846 Lincoln's Inn → 1854–59 抽象群/矩阵论文 → 1863 Sadleirian 教授 → 1882 Copley → 1883 BAAS 主席 → 1889 全集 → 1895 逝世
4. **早年与剑桥求学**（1821–1842）：圣彼得堡、KCS、Senior Wrangler、Smith's Prize（4 行表格）
5. **抽象群：第一个定义**（核心贡献页）：抽象群定义、与 Galois 的关系、Cayley 定理、Cayley 表/图（表格 + 公式框）
6. **Cayley–Hamilton 与矩阵代数**（核心贡献页）：1858《矩阵论专论》、2/3 阶验证、一般证明归后人、1841 行列式（表格 + 公式框 $p_A(A)=O$）
7. **律师楼里的数学家**（核心叙事页）：1846 Lincoln's Inn、都柏林听 Hamilton 四元数讲座、与 Sylvester 散步讨论不变量、14 年两三百篇论文（表格）
8. **代数几何**（核心贡献页）：27 条直线（与 Salmon）、直纹曲面、曲线参数化（Chow 先声）、不变量学派（表格 + 公式框）
9. **组合学与 Cayley 公式**（核心贡献页）：$n^{n-2}$ 棵树、生成函数开创性使用、化学应用（表格 + 公式框 $T_n=n^{n-2}$）
10. **从律师楼到剑桥讲席**（核心叙事页）：1863 首任 Sadleirian、放弃高薪、JHU 讲学、女性教育 Girton/Newnham（表格）
11. **荣誉与高产**（`\honorslide`）：奖项 / 全集 / 身后影响（itemize 表格）
12. **终章**（`\closingslide`）：「他把"运算的对象"，变成了现代数学的骨架。」

## 5. 史实陷阱与敏感点（终审必须检查）

- **抽象群概念**：Cayley **第一个定义抽象群**（区别于 Galois 的置换群）——是"第一个定义抽象群概念"，但需注意 Galois 已发展置换群，Cayley 的贡献是**抽象化**。
- **Cayley–Hamilton 定理**：Cayley **提出并验证了 2 阶、3 阶情形**，未给出一般证明（一般证明是后人的工作）——勿写 Cayley 证明了该定理的一般情形。
- **Cayley 公式**：n 个标号顶点有 n^(n−2) 棵树——是"开创性使用生成函数"计数，勿写 Cayley 发明了图论（图论概念更早）。
- **八元数（Cayley 代数）**：Cayley–Dickson 构造，八元数——需注意与 Graves 的优先权（Graves 1843 年独立发现八元数）。
- **27 条直线**：Cayley 与 Salmon **共同发现**三次曲面上的 27 条直线——勿写 Cayley 独发现。
- **律师生涯**：Cayley 曾当律师 14 年（conveyancing 专业），是"先律师后教授"的轨迹——与 Sylvester（也是先律师）相似。
- **Sadleirian 教授**：1863 年任剑桥 Sadleirian 纯数学教授（首任），**放弃高薪法律职业选择微薄薪水**——是"放弃高薪"，体现其纯粹学术追求。
- **无肖像**：✅ 已解决——本地 `images.txt` 首张为数学公式，但经 Wikipedia API（`prop=pageimages`）查得条目主图 `Arthur_Cayley.jpg`（Commons a/a9，892×1352 竖版照片，EXIF 注明 "Portrait of Arthur Cayley"），下载至 `images/cayley_portrait.jpg`，封面与身份页均采用（相框按 0.66:1 竖版比例定制）。
- **国籍**：United Kingdom of Great Britain and Ireland，今英国——封面用「英国」。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q159430 | ✅ 已入库（MySQL/data/Arthur_Cayley.yaml） |
| name_zh | 凯莱（或 阿瑟·凯莱） | ✅ 已入库 |
| name_en | Arthur Cayley | ✅ 已入库 |
| birth_date | 1821-08-16 | ✅ 已入库 |
| death_date | 1895-01-26 | ✅ 已入库 |
| nationality | United Kingdom | ✅ 已入库 |
| primary_occupation | mathematician | ✅ 已入库 |
| field_of_work | algebra / group theory / graph theory / matrix theory | ✅ 已入库 |
| has_biography | true | ✅ 本次置 true |

## 7. 社会关系入库清单（§20）

- **导师**：George Peacock、William Hopkins
- **合作者**：James Joseph Sylvester（不变量理论长期合作）
- **学生**：H. F. Baker、Andrew Forsyth、Charlotte Scott
- **学术相关**：George Salmon（27 条直线共同发现）、William Rowan Hamilton（听其四元数讲座）
- **家族**：弟 Charles Bagot Cayley（语言学家）

## 8. 奖项清单

- Copley Medal（科普利奖章，1882）
- Royal Medal（皇家奖章，1859）
- De Morgan Medal（德摩根奖章，1884）
- Fellow of the Royal Society（FRS）
- Smith's Prize（史密斯奖，1842，第一名）
- 海德堡大学、爱丁堡大学、博洛尼亚大学、牛津大学、莱顿大学荣誉博士
- Officer of the Legion of Honour（荣誉军团军官）
- Fellow of the American Academy of Arts and Sciences

## 9. 机构清单

- 教育：King's College School、Trinity College, Cambridge、Lincoln's Inn（律师）
- 任职：University of Cambridge（Sadleirian 纯数学教授，1863–1895）、Trinity College, Cambridge（荣誉院士）

## 10. 终审清单

- [x] 生卒 1821-08-16 / 1895-01-26，享年 73，出生地里士满
- [x] 抽象群"第一个定义、Galois 置换群先行"表述准确（Slide 5：明确"Galois 研究置换群，凯莱的贡献是抽象化"）
- [x] Cayley–Hamilton"提出并验证 2/3 阶、一般证明后人"表述准确（Slide 6 表格 + 公式框注明"提出于 1858；2、3 阶已验证"）
- [x] Cayley 公式"生成函数计数"表述准确（Slide 9；并注明"图论概念本身更早"，勿写凯莱发明图论）
- [x] 八元数优先权：本次 tex 未展开 Cayley–Dickson（避免与 Graves 优先权纠缠），列入 Slide 1 badge 之外的遗产页不涉及
- [x] 27 直线"与 Salmon 共同发现"表述准确（Slide 8 表格 + 公式框标注 Cayley & Salmon）
- [x] 律师→Sadleirian 教授"放弃高薪"表述准确（Slide 7 / 10）
- [x] 头像确认（✅ Wikipedia Commons 竖版照片，`images/cayley_portrait.jpg`）
- [x] 国籍用「英国」现代对应
- [x] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误，Overfull = 0；`make images && make video` 完成（BGM: Timeless）

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [x] **结合本地 Wikipedia**：逐页对照 Beamer tex 全部事实（生卒、Senior Wrangler、1846 入 Lincoln's Inn、1863 首任 Sadleirian、35 年教授、967 篇/13 卷、奖项年份均与 page.md 一致）
- [x] **头像**：✅ 经 Wikipedia API 查得条目主图并下载（`images/cayley_portrait.jpg`）
- [x] **国籍**：封面顶部徽章明示英国
- [x] **引语核对**：Sadleirian 职责引文（"to explain and teach..."）以间接表述呈现，未使用中文引号内伪引语
- [x] **编译验证**：`make distclean && make` 通过，13 页正文 PDF，Overfull = 0；封面小字注左移修复（xshift 6.86→6.5cm）
- [x] **更新提示词**：Review 修正已写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Weierstrass / Boole / Sylvester）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
