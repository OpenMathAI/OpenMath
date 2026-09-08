# Leopold Kronecker（利奥波德·克罗内克）立传提示词

> qid=Q76410 · 1823-12-07 – 1891-12-29 · 德国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Leopold_Kronecker/`（page.md + metadata.json + images.txt）
>
> **立传状态：✅ 已完成（参考高斯基准模板）**——tex（13 页正文）+ Makefile + 头像就位，`make distclean && make` 编译通过、Overfull 仅 0.8pt（阈值内）；头像经 Wikipedia API 查得 1865 年照片（`images/kronecker_portrait.jpg`，343×450，EXIF "ikronec001p1"）；BGM 已选 **Symphony No. 5**（Beethoven/Karajan，"命运"的庄重力量，契合哲学斗士形象），视频 `make video` 已生成。

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「整数 / 有限」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Leopold Kronecker（中文惯称：克罗内克）
- **生卒**：1823-12-07 生于利格尼茨（Liegnitz，西里西亚省，普鲁士，今波兰 Legnica）→ 1891-12-29 逝于柏林（德意志帝国），享年 68
- **国籍**：Kingdom of Prussia（普鲁士王国，今德国）
- **身份**：数学家（数论、抽象代数、逻辑）
- **家庭**：富裕犹太家庭；父 Isidor、母 Johanna（née Prausnitzer）；弟 Hugo Kronecker（后成为生理学家）；1848 年娶表妹 Fanny Prausnitzer，育 6 子女
- **教育轨迹**：
  - Liegnitz 文科中学（受 Ernst Kummer 教导，Kummer 注意到并鼓励其数学兴趣）
  - 1841 年入柏林大学（兴趣广泛，兼及天文、哲学）
  - 1843 年波恩大学学天文、1843–44 年布雷斯劳大学师从 Kummer
  - 回柏林后师从 Dirichlet，1845 年答辩代数数论博士论文
- **导师**：Johann Franz Encke、Peter Gustav Lejeune Dirichlet（博士导师）；Ernst Kummer（中学老师、终生挚友）
- **研究领域**：数论、抽象代数、逻辑、行列式

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **名言"上帝造整数"（最著名）**："Die ganzen Zahlen hat der liebe Gott gemacht, alles andere ist Menschenwerk"（"上帝造整数，其余都是人的工作"）——体现其**有限主义（finitism）**哲学立场。
2. **有限主义与直觉主义先驱**：反对康托尔的集合论与实无穷，是数学哲学中直觉主义（intuitionism）的先驱。
3. **克罗内克 δ（Kronecker delta）**：以他命名的 δ 符号，是线性代数与数学物理中最常用的符号之一。
4. **克罗内克积（Kronecker product）**：矩阵的张量积，线性代数与量子信息中的重要工具。
5. **Kronecker–Weber 定理**：1853 年论文中表述（未给完整证明，后由 Hilbert 完全证明）。
6. **有限生成阿贝尔群的结构定理**：引入有限生成阿贝尔群的结构定理。
7. **五次方程与群论**：1850 年《论五次一般方程的求解》用群论解五次方程（非根式解，Abel–Ruffini 已证明根式解不可能）。
8. **代数数论中的除子理论**：引入除子（divisor）理论，作为 Dedekind 理想理论（哲学上不接受）的替代；虽长期被忽视，20 世纪被重新复兴。
9. **生平**：富裕犹太家庭，曾管理农场（商人），1855 年回柏林做**私人学者**；1861 年当选柏林科学院院士；1866 年拒绝哥廷根数学教席（高斯、Dirichlet 曾任）；1883 年接替 Kummer 任柏林大学教授。
10. **与 Weierstrass 的冲突**：其数学哲学观点与 Weierstrass 冲突，几乎导致 Weierstrass 1888 年离开大学。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（普鲁士深蓝） | `#1F3A93` | 德意志理性 |
| 强调色（数学金） | `#C9A227` | 整数 / 尊崇 |
| 分类色 1（δ/积 — 靛蓝） | `#4C5FD5` | 克罗内克 δ / 克罗内克积 |
| 分类色 2（代数数论 — 青绿） | `#0E7C7B` | Kronecker–Weber / 除子理论 |
| 分类色 3（有限主义 — 琥珀） | `#E07B30` | 有限主义 / 直觉主义 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「整数 / 有限」的视觉语言。

### 3.5 背景音乐选择 ✅ 【已选定】

- **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
- **选定曲目**：**Symphony No. 5**（Beethoven / Karajan，`music_audio/beethoven-karajan/05-OV6Lp7cnX7s-Beethoven ＂Symphony No 5＂ Karajan.wav`，已软链为 `bgm.wav`）
- **匹配理由**："命运"交响曲的庄重力量，契合克罗内克在数学基础论战中寸步不让的斗士形象与"上帝造整数"的坚定立场
- （避免与他片重复：Poncelet 用 The Flow of Time，Cayley 用 Timeless，Hermite 用 Eroica（No.3），Eisenstein 用 Lonesome）

## 4. Slide 规划（实际 13 页正文 + OpenMath 封面，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「克罗内克」+ 副题「柏林大学教授 · 科学院院士 · 有限主义的先驱」+ 右上头像 + 国籍行 + 底部三要素状态栏 + 4 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1823 利格尼茨 → 1841 柏林大学 → 1845 博士 → 1848 婚+农场十年 → 1855 回柏林 → 1861 科学院 → 1866 拒哥廷根 → 1883 接任 Kummer → 1891 逝世
4. **早年与 Kummer 的启蒙**（1823–1845）：富裕犹太家庭、Kummer 中学教导、柏林大学广泛兴趣、Dirichlet 博士（4 行表格）
5. **"上帝造整数"与有限主义**（核心叙事页）：德文原句 + 中译 + Weber 转述注释（金框）、算术化分析/反对实无穷/有限主义（表格；哲学立场之争客观表述）
6. **克罗内克 δ 与克罗内克积**（核心贡献页）：δ 定义、张量积、其他命名（表格 + 公式框 $\delta_{ij}$ 与 $A\otimes B$）
7. **K--W 定理与阿贝尔群结构定理**（核心贡献页）：K-W 1853 表述（注明 Hilbert 完全证明）、结构定理、1853 memoir 扩展 Galois（表格 + 公式框 $K\subseteq\mathbb{Q}(\zeta_n)$）
8. **五次方程与青春之梦**（核心贡献页）：1850 群论解五次方程（注明非根式解）、椭圆函数、Jugendtraum → Hilbert 第十二问题（表格）
9. **除子理论 vs 理想理论**（核心贡献页）：克罗内克/Dedekind 对比表（哲学不接受理想；20 世纪除子复兴）
10. **私人学者与学术生涯**（核心叙事页）：经商十年、回柏林、科学院+大学开课、拒哥廷根/接任 Kummer（4 行表格）
11. **与 Weierstrass 的冲突**（核心叙事页）：挚友→论敌、处处不可微函数之争、1888 几乎离校（客观表述）、晚年皈依与去世（表格）
12. **荣誉与遗产**（`\honorslide`）：三院院士 / 以他命名 / 身后影响（itemize 表格）
13. **终章**（`\closingslide`）：「上帝造整数，人书写其余的一切。」

## 5. 史实陷阱与敏感点（终审必须检查）

- **名言"上帝造整数"**：原文 "Die ganzen Zahlen hat der liebe Gott gemacht, alles andere ist Menschenwerk"（"上帝造整数，其余都是人的工作"）——是 Heinrich Weber 转述的 Kronecker 名言，引用时需注明是转述。
- **有限主义 vs 反对康托尔**：Kronecker 反对康托尔的**集合论与实无穷**——是"哲学立场分歧"，客观表述，勿写成纯粹个人恩怨。
- **Kronecker–Weber 定理**：Kronecker 1853 年**表述**该定理，但**未给完整证明**（后由 Hilbert 完全证明）——勿写 Kronecker 证明了该定理。
- **五次方程与群论**：Kronecker 用群论解五次方程，是**非根式解**（根式解已被 Abel–Ruffini 证明不可能）——勿混淆。
- **除子理论 vs 理想理论**：Kronecker 引入除子理论作为 Dedekind 理想理论的**替代**（哲学上不接受理想）——是"理论分歧"，勿写两者相同。
- **与 Weierstrass 冲突**：哲学观点分歧导致关系紧张，几乎使 Weierstrass 1888 年离开大学——客观表述。
- **皈依基督教**：1891 年去世前一年皈依基督教——可作背景，不必过度强调。
- **无肖像**：✅ 已解决——本地 `images.txt` 首张虽为墓地照片，但经 Wikipedia API（`prop=pageimages`）查得条目主图 `Leopold_Kronecker_1865.jpg`（Commons c/cc，343×450 竖版，EXIF "ikronec001p1" 确认身份），下载至 `images/kronecker_portrait.jpg`，封面与身份页均采用。
- **国籍**：Kingdom of Prussia（普鲁士王国），今属德国（生于今波兰 Legnica）——封面用「德国（普鲁士王国）」。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76410 | ✅ 已入库（MySQL/data/Leopold_Kronecker.yaml） |
| name_zh | 克罗内克（或 利奥波德·克罗内克） | ✅ 已入库 |
| name_en | Leopold Kronecker | ✅ 已入库 |
| birth_date | 1823-12-07 | ✅ 已入库 |
| death_date | 1891-12-29 | ✅ 已入库 |
| nationality | Germany（普鲁士王国） | ✅ 已入库 |
| primary_occupation | mathematician | ✅ 已入库 |
| field_of_work | number theory / algebra / logic | ✅ 已入库 |
| has_biography | true | ✅ 本次置 true；另修正 relations 中 Dedekind 备注（"Cantor 争议中的对立方"→"除子理论 vs 理想理论"） |

## 7. 社会关系入库清单（§20）

- **博士导师**：Johann Franz Encke、Peter Gustav Lejeune Dirichlet
- **终生挚友 / 老师**：Ernst Kummer（中学老师、终生挚友）
- **好友**：Karl Weierstrass（曾为好友，后因哲学分歧关系紧张）
- **哲学对立**：Georg Cantor（反对其集合论）、Richard Dedekind（除子理论 vs 理想理论）
- **学生**：Kurt Hensel、Adolf Kneser、Mathias Lerch、Franz Mertens、Jules Molk、Paul Stäckel
- **家族**：弟 Hugo Kronecker（生理学家）

## 8. 奖项清单

- Foreign Member of the Royal Society（英国皇家学会外籍会员，1884）
- 1861 年普鲁士科学院院士、1868 年法国科学院外籍院士

## 9. 机构清单

- 教育：University of Bonn、Frederick William University Berlin（博士）、University of Wrocław、Liegnitz Ritter-Akademie
- 任职：Frederick William University Berlin（1883 起接替 Kummer 任教授）、Berlin Academy（柏林科学院）

## 10. 终审清单

- [x] 生卒 1823-12-07 / 1891-12-29，享年 68，出生地 Liegnitz
- [x] 名言"上帝造整数"注明是 Weber 转述（Slide 5 金框：德文原句 + 中译 + "Heinrich Weber 转述的克罗内克名言（1893 讣闻）"）
- [x] 有限主义"反对康托尔集合论、直觉主义先驱"表述准确（Slide 5：明确"哲学立场之争，而非私人恩怨"）
- [x] Kronecker–Weber"1853 表述、Hilbert 完全证明"表述准确（Slide 7 表格 + 公式框 + badge 均注明）
- [x] 五次方程"群论非根式解"表述准确（Slide 8：明确"非根式解（Abel–Ruffini 已排除根式）"）
- [x] 除子理论"替代 Dedekind 理想理论"表述准确（Slide 9 专页对比：哲学不接受理想、20 世纪复兴）
- [x] 与 Weierstrass 冲突客观表述（Slide 11：挚友→论敌、处处不可微函数之争、1888 几乎离校，均客观）
- [x] 头像确认（✅ Wikipedia API 查得 1865 年照片，`images/kronecker_portrait.jpg`）
- [x] 国籍用「德国（普鲁士王国）」表述准确
- [x] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误，Overfull 仅 0.8pt（阈值内）；`make images && make video` 完成（BGM: Beethoven No. 5）

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [x] **结合本地 Wikipedia**：逐页对照 Beamer tex 全部事实（生卒、Liegnitz、Kummer 中学、1845 博士、农场十年、1855 回柏林、1861 科学院、1866 拒哥廷根、1883 接任、学生名单、三院院士年份均与 page.md 一致）
- [x] **头像**：✅ 经 Wikipedia API 查得 1865 年照片并下载（`images/kronecker_portrait.jpg`）
- [x] **国籍**：封面顶部徽章明示德国（普鲁士王国）
- [x] **引语核对**："上帝造整数"名言严格采用 Wikipedia 原文（德文原句 + Weber 转述注释），未杜撰其他引语
- [x] **编译验证**：`make distclean && make` 通过，14 页 PDF，Overfull 仅 0.8pt（阈值内）；`make images && make video` 完成（BGM: Beethoven No. 5）
- [x] **更新提示词**：Review 修正已写回本文件

### 第 2 轮（Review-2）：结构优化
- [x] 检查 Overfull/Underfull 告警：仅 0.8pt（阈值内）
- [x] 身份信息页布局与 Wilson 模板对齐（左肖像 2.95×3.9 + 右 2×2 网格）
- [x] 中文标点 / 断行 / 间距统一（引语用半角 " "）
- [x] 与同世纪数学家（Eisenstein / Hermite / Cayley / Boole / Poncelet）格式对齐（同模板、同结构、同收尾页式样）

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
