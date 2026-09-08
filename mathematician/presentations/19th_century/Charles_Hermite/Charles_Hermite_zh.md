# Charles Hermite（夏尔·埃尔米特）立传提示词

> qid=Q168401 · 1822-12-24 – 1901-01-14 · 法国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Charles_Hermite/`（page.md + metadata.json + images.txt）
>
> **立传状态：✅ 已完成（参考高斯基准模板）**——tex（12 页正文）+ Makefile + 头像就位，`make distclean && make` 编译通过、Overfull = 0；头像采用 Wikipedia Commons 1887 年晚年照片（`images/hermite_portrait.jpg`，本地 images.txt 已含肖像）；BGM 已选 **Symphony No. 3 "Eroica"**（Karajan，英雄/壮丽，契合身残志坚与里程碑成就），视频 `make video` 已生成。

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「正交 / 超越」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Charles Hermite（中文惯称：埃尔米特）
- **生卒**：1822-12-24 生于迪厄兹（Dieuze，摩泽尔，法兰西王国波旁复辟）→ 1901-01-14 逝于巴黎（法兰西第三共和国），享年 78
- **国籍**：France（法国）
- **身份**：数学家（数论、分析、代数、超越数）
- **家庭**：父 Ferdinand Hermite（从事妻家布料生意，兼艺术家）、母 Madeleine Lallemand；七个孩子中排行第六；**右脚畸形，终身跛行**
- **教育轨迹**：
  - 南锡中学（Collège de Nancy）、巴黎 Collège Henri IV、Lycée Louis-le-Grand
  - 由 Eugène Charles Catalan 辅导备考 École Polytechnique
  - 1842 年入 École Polytechnique，一年后因脚畸形被要求退学，**未毕业**（学校施加苛刻条件，Hermite 不接受）
  - 私下攻读五年，1847 年获 baccalauréat
- **导师**：Eugène Charles Catalan（博士导师）、Joseph Liouville（学术顾问）
- **研究领域**：代数、数论、分析、二次型、正交多项式、椭圆函数

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **证明 e 是超越数（最著名贡献）**：1873 年用两种方法证明自然对数底 e 是超越数（基于 Liouville 的先行工作），是超越数理论的里程碑。同年证明 π² 因此 π 无理，但**未证明 π 超越**（认为超出自己能力），后由 Lindemann 1882 年用类似技巧完成。
2. **埃尔米特多项式（Hermite polynomials）**：1864 年引入，是量子谐振子薛定谔方程的解（埃尔米特函数 = 埃尔米特多项式 × 高斯函数）。
3. **埃尔米特矩阵（Hermitian matrix）**：1855 年证明 Hermitian 矩阵（等于自身共轭转置）的特征值恒为实数，推广了 Cauchy 1829 年关于实对称矩阵的结果；后经 Hilbert 扩展，成为量子力学严格数学表述的基础（Wiener、Born、von Neumann 等使用 Hermitian 算子）。
4. **正交矩阵**：1854 年引入正交矩阵概念（等于其转置的逆）。
5. **五次方程与椭圆积分**：1858、1865、1866 年证明五次多项式方程的根可用椭圆积分求得（延续 Abel–Ruffini 定理：五次方程不可根式解，但可用椭圆函数解）。
6. **不变量理论**：与 Cayley、Sylvester 同时发展不变量理论，发现互反律（law of reciprocity）。
7. **生平与残疾**：右脚畸形终身跛行，1842 年入 École Polytechnique 后一年因脚畸形被要求退学——是"身残志坚"的动人叙事。
8. **荣誉**：荣誉军团大官（Grand Officer）、Pour le Mérite、ForMemRS；月球北极附近的 Hermite 环形山以其命名。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（法国深蓝） | `#1F3A93` | 法兰西理性 |
| 强调色（数学金） | `#C9A227` | 超越数 / 尊崇 |
| 分类色 1（超越数 — 靛蓝） | `#4C5FD5` | e 超越 / π 无理 |
| 分类色 2（正交/矩阵 — 青绿） | `#0E7C7B` | Hermitian 矩阵 / 正交矩阵 |
| 分类色 3（多项式/椭圆函数 — 琥珀） | `#E07B30` | Hermite 多项式 / 五次方程 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「正交 / 超越」的视觉语言。

### 3.5 背景音乐选择 ✅ 【已选定】

- **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
- **选定曲目**：**Symphony No. 3 "Eroica"**（Beethoven / Karajan，优先级 2，`music_audio/beethoven-karajan/03-BgIjGSPmk7I-Beethoven ＂Symphony No 3＂ Karajan.wav`，48:52，已软链为 `bgm.wav`）
- **匹配理由**：标签"古典 / 英雄 / 壮丽"，适用"伟大成就、里程碑、片尾升华"——契合埃尔米特证明 e 超越性的里程碑成就与身残志坚的坚毅气质
- （避免与他片重复：Poncelet 用 The Flow of Time，Cayley 用 Timeless）

## 4. Slide 规划（实际 12 页正文 + OpenMath 封面，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「埃尔米特」+ 副题「法兰西科学院院士 · 索邦教授 · 超越数的证明者」+ 右上头像 + 国籍行 + 底部三要素状态栏 + 4 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1822 出生（右脚畸形）→ 1842 入综合理工 → 1843 被退学 → 1847 获学位 → 1848 回母校任教+当选科学院 → 1869 索邦教授 → 1873 证明 e 超越 → 1901 逝世
4. **早年与残疾**（1822–1847）：Dieuze、脚畸形、Catalan 辅导、综合理工退学、私下攻读五年（4 行表格）
5. **1873 · 证明 e 是超越数**（核心贡献页）：超越数定义、Liouville 思想两种方法、1873《论指数函数》、Hilbert 简化（表格 + 公式框）
6. **从 e 到 π**（核心贡献页）：π² 无理 → π 无理、未证 π 超越、Lindemann 1882（表格 + 里程碑公式框）
7. **Hermitian 矩阵与正交矩阵**（核心贡献页）：1854 正交（Frobenius 1878 现代定义）、1855 Hermitian 特征值实数（推广 Cauchy 1829）、量子力学（表格 + 公式框 $A=A^\dagger\Rightarrow\lambda\in\mathbb{R}$）
8. **Hermite 多项式**（核心贡献页）：1864、正交性、量子谐振子（表格 + 薛定谔方程解公式框）
9. **椭圆积分解五次方程**（核心贡献页）：1842 首篇论文、1858/1865/1866 椭圆积分求解、与 Jacobi 通信（表格）
10. **不变量理论与教学生涯**（核心叙事页）：与 Cayley/Sylvester 并肩互反律、ENS/索邦/综合理工教职、学生 Poincaré/Stieltjes/Padé、1848 当选科学院（表格；不变量理论与生涯合并为一页）
11. **荣誉与遗产**（`\honorslide`）：生前荣誉 / 身后纪念 / 以他命名（itemize 表格）
12. **终章**（`\closingslide`）：「被校园拒绝的身体，证明了最纯粹的数。」

## 5. 史实陷阱与敏感点（终审必须检查）

- **e 超越性证明**：Hermite 1873 年证明 e 超越，是**基于 Liouville 的先行工作**——勿写 Hermite 完全独立证明。
- **π 超越 vs 无理**：Hermite 证明 π² 因此 π **无理**，但**未证明 π 超越**（认为超出自己能力）——π 超越由 Lindemann 1882 年用类似技巧证明。勿写 Hermite 证明了 π 超越。
- **Hermitian 矩阵**：Hermite 1855 年证明 Hermitian 矩阵特征值恒为实数，**推广了 Cauchy 1829 年**关于实对称矩阵的结果——勿写 Hermite 首创该性质。
- **正交矩阵**：Hermite 1854 年**引入正交矩阵概念**，但现代正式定义由 Frobenius 1878 年首次给出——勿写 Hermite 给出了现代定义。
- **五次方程与椭圆积分**：Hermite 证明五次方程根可用椭圆积分求解——这是"可用椭圆函数解"，与 Abel–Ruffini"不可根式解"不矛盾，勿混淆。
- **脚畸形**：右脚畸形终身跛行，1842 年入 École Polytechnique 后一年因脚畸形被要求退学——是"学校劝退"，Hermite 拒绝苛刻条件而退学，未毕业。
- **死亡**：1901-01-14 逝于巴黎，享年 78，晚年患哮喘、食欲不振、睡眠不佳。
- **国籍**：France（法国）——封面用「法国」。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q168401 | ✅ 已入库（MySQL/data/Charles_Hermite.yaml） |
| name_zh | 埃尔米特（或 夏尔·埃尔米特） | ✅ 已入库 |
| name_en | Charles Hermite | ✅ 已入库 |
| birth_date | 1822-12-24 | ✅ 已入库 |
| death_date | 1901-01-14 | ✅ 已入库 |
| nationality | France | ✅ 已入库 |
| primary_occupation | mathematician | ✅ 已入库 |
| field_of_work | number theory / algebra / orthogonal polynomials | ✅ 已入库 |
| has_biography | true | ✅ 本次置 true；另修正 relations 中 Picard 备注（"岳父"→"女婿"，Picard 娶 Hermite 之女） |

## 7. 社会关系入库清单（§20）

- **导师**：Eugène Charles Catalan（博士导师）、Joseph Liouville（学术顾问）
- **学生**：Henri Poincaré、Thomas Joannes Stieltjes、Jules Tannery、Henri Padé、Gaston Floquet
- **学术合作**：Carl Gustav Jacob Jacobi（椭圆函数通信）、Arthur Cayley、James Joseph Sylvester（不变量理论同时发展）
- **学术相关**：Augustin-Louis Cauchy（影响其重拾天主教信仰）、Ferdinand von Lindemann（后续证明 π 超越）
- **家族**：妻 Louise（Joseph Bertrand 之妹）

## 8. 奖项清单

- Grand Officer of the Legion of Honour（荣誉军团大官，70 岁生日晋升）
- Pour le Mérite for Sciences and Arts（科学与艺术功勋勋章）
- Foreign Member of the Royal Society（英国皇家学会外籍会员）
- Commanders Grand Cross of the Order of the Polar Star（北极星勋章大十字）
- Honorary doctor of the University of Liège（列日大学荣誉博士）

## 9. 机构清单

- 教育：Lycée Henri-IV、Lycée Louis-le-Grand、École Polytechnique（未毕业）
- 任职：École Normale Supérieure（1862–1873 讲师）、University of Paris（索邦，1869 起教授）、École Polytechnique（1869–1876 教授）

## 10. 终审清单

- [x] 生卒 1822-12-24 / 1901-01-14，享年 78，出生地 Dieuze
- [x] e 超越"基于 Liouville 先行工作"表述准确（Slide 5：方法来源行明确"基于 Liouville 的思想"）
- [x] π"证明无理、未证超越、Lindemann 后续"表述准确（Slide 6：专页呈现，"他的方法未能直接证明 π 超越——这是他未跨过的最后一步"）
- [x] Hermitian 矩阵"推广 Cauchy 1829 结果"表述准确（Slide 7 表格 + 公式框均注明）
- [x] 正交矩阵"概念引入、Frobenius 现代定义"表述准确（Slide 7：1854 提出，Frobenius 1878 现代定义）
- [x] 五次方程"椭圆积分求解、与 Abel–Ruffini 不矛盾"表述准确（Slide 9：从"不可根式解"走向"椭圆积分构造"）
- [x] 脚畸形"学校劝退、未毕业"表述准确（Slide 3 / 4：因脚畸形被要求退学，未毕业；身份页教育栏注明）
- [x] 国籍用「法国」现代对应
- [x] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误，Overfull = 0；e 超越页公式框溢出已修复（拆两行）

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [x] **结合本地 Wikipedia**：逐页对照 Beamer tex 全部事实（生卒、退学原因与年份、1847 学位、1848 科学院、教职年份、奖项均与 page.md 一致）
- [x] **头像**：✅ 采用本地 images.txt 首张 `Charles_Hermite_circa_1887.jpg`（Commons 6/65，500×788），下载至 `images/hermite_portrait.jpg`，封面与身份页均采用
- [x] **国籍**：封面顶部徽章明示法国
- [x] **引语核对**：未使用直接引语，全部为间接表述
- [x] **编译验证**：`make distclean && make` 通过，13 页 PDF，Overfull = 0；e 超越页公式框溢出修复（拆两行）；`make images && make video` 完成（BGM: Eroica）
- [x] **更新提示词**：Review 修正已写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Cayley / Weierstrass / Boole）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
