# Arthur Cayley（阿瑟·凯莱）立传提示词

> qid=Q159430 · 1821-08-16 – 1895-01-26 · 英国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Arthur_Cayley/`（page.md + metadata.json + images.txt）

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

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典典雅 / 维多利亚学者风范**（剑桥 Sadleirian 教授的典雅）
- **匹配理由**：
  - 凯莱是维多利亚时代的英国数学巨匠，剑桥三一学院教授——需**典雅、庄重、有维多利亚学者风范**的配乐
  - "典雅" 匹配其放弃高薪法律职业而选择学术的从容
  - "庄重" 匹配其 967 篇论文的高产与学术地位
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/典雅/庄重风格）：
  - 首选：古典 / 典雅 / 庄重风格曲目（呼应维多利亚学者）
  - 备选：历史感深沉曲目（呼应 19 世纪剑桥）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「抽象群与矩阵理论的奠基者」+ 凯莱 1821–1895 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：群论 / 矩阵 / 代数几何与组合 / 生平 四分类
4. **早年与剑桥求学**（1821–1842）：圣彼得堡、King's College School、Senior Wrangler、Smith's Prize
5. **抽象群概念**（核心贡献页）：第一个定义抽象群、Cayley 定理、Cayley 表
6. **Cayley–Hamilton 定理与矩阵**（核心贡献页）
7. **与 Sylvester 的合作**（核心叙事页）：Lincoln's Inn 散步、不变量理论
8. **代数几何**（核心贡献页）：27 条直线、直纹曲面
9. **组合学与 Cayley 公式**（核心贡献页）：n^(n−2) 树、生成函数
10. **律师与 Sadleirian 教授**（核心叙事页）：14 年律师、放弃高薪、剑桥 35 年
11. **荣誉与高产**：Copley Medal、全集 13 卷 967 篇论文
12. **终章**：73 岁、从抽象群到现代代数的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **抽象群概念**：Cayley **第一个定义抽象群**（区别于 Galois 的置换群）——是"第一个定义抽象群概念"，但需注意 Galois 已发展置换群，Cayley 的贡献是**抽象化**。
- **Cayley–Hamilton 定理**：Cayley **提出并验证了 2 阶、3 阶情形**，未给出一般证明（一般证明是后人的工作）——勿写 Cayley 证明了该定理的一般情形。
- **Cayley 公式**：n 个标号顶点有 n^(n−2) 棵树——是"开创性使用生成函数"计数，勿写 Cayley 发明了图论（图论概念更早）。
- **八元数（Cayley 代数）**：Cayley–Dickson 构造，八元数——需注意与 Graves 的优先权（Graves 1843 年独立发现八元数）。
- **27 条直线**：Cayley 与 Salmon **共同发现**三次曲面上的 27 条直线——勿写 Cayley 独发现。
- **律师生涯**：Cayley 曾当律师 14 年（conveyancing 专业），是"先律师后教授"的轨迹——与 Sylvester（也是先律师）相似。
- **Sadleirian 教授**：1863 年任剑桥 Sadleirian 纯数学教授（首任），**放弃高薪法律职业选择微薄薪水**——是"放弃高薪"，体现其纯粹学术追求。
- **无肖像**：`images.txt` 中无 Cayley 本人肖像（第一张为数学公式），封面头像需用装饰圆占位（Wikipedia 有 Dickinson 1874 年肖像、Longmaid 1884 年肖像）。
- **国籍**：United Kingdom of Great Britain and Ireland，今英国——封面用「英国」。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q159430 | 待写入 |
| name_zh | 凯莱（或 阿瑟·凯莱） | 待写入 |
| name_en | Arthur Cayley | 待写入 |
| birth_date | 1821-08-16 | 待写入 |
| death_date | 1895-01-26 | 待写入 |
| nationality | United Kingdom | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | group theory / matrix theory / algebraic geometry | 待写入 |
| has_biography | 1 | 本次置 1 |

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

- [ ] 生卒 1821-08-16 / 1895-01-26，享年 73，出生地里士满
- [ ] 抽象群"第一个定义、Galois 置换群先行"表述准确
- [ ] Cayley–Hamilton"提出并验证 2/3 阶、一般证明后人"表述准确
- [ ] Cayley 公式"生成函数计数"表述准确
- [ ] 八元数"与 Graves 优先权"表述准确（若提及）
- [ ] 27 直线"与 Salmon 共同发现"表述准确
- [ ] 律师→Sadleirian 教授"放弃高薪"表述准确
- [ ] 头像确认（无肖像则装饰圆占位）
- [ ] 国籍用「英国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Arthur_Cayley/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：无肖像，用装饰圆占位
- [ ] **国籍**：封面顶部徽章明示英国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Weierstrass / Boole / Sylvester）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
