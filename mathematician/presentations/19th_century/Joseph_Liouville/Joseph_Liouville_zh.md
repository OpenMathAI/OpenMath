# Joseph Liouville（约瑟夫·刘维尔）立传提示词

> qid=Q214549 · 1809-03-24 – 1882-09-08 · 法国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Joseph_Liouville/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「超越数 / 相空间」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Joseph Liouville（中文惯称：刘维尔）
- **生卒**：1809-03-24 生于圣奥梅尔（Saint-Omer，法兰西第一帝国）→ 1882-09-08 逝于巴黎（法兰西第三共和国），享年 73
- **国籍**：France（法国）
- **身份**：数学家（数论、复分析、数学物理）
- **家庭**：父 Claude-Joseph Liouville（军官）、母 Thérèse Liouville（née Balland）
- **教育轨迹**：
  - 1825 年入 École Polytechnique，1827 年毕业
  - 后入 École des Ponts et Chaussées（桥梁道路学校，如 Cauchy 一样学工程，但选择数学职业）
- **导师**：Siméon Denis Poisson、Louis Jacques Thénard
- **研究领域**：数学分析、数论、复分析、数学物理

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **第一个证明超越数存在（1844，最著名贡献）**：证明存在超越数（transcendental number），给出具体例子（刘维尔数）。他的不等式表明"有理数是代数无理数的糟糕逼近"，成为超越性的判据；后来 Hermite 证明 e 超越、Lindemann 证明 π 超越都基于其贡献。
2. **刘维尔定理（复分析）**：有界整函数必为常数——复分析的基本定理。
3. **刘维尔定理（哈密顿力学）**：保守力学系统的相空间体积守恒——统计力学的基本结果（Gibbs 之后被认定为统计力学基础）。
4. **Sturm–Liouville 理论**：与好友 Jacques Charles François Sturm 在 1830 年代建立，是求解积分方程的标准方法，推广了傅里叶分析（受傅里叶圆柱热扩散启发），是泛函分析的早期进展。
5. **出版伽罗瓦著作**：最早理解伽罗瓦贡献的数学家之一，1846 年在自己创办的杂志上编辑出版伽罗瓦的著作，使伽罗瓦理论引起广泛注意，间接推动了现代代数与群论发展。
6. **创办《纯数学与应用数学杂志》**：1836 年创办 Journal de Mathématiques Pures et Appliquées（仿 Crelle's Journal），成为法国一流数学期刊，人称"刘维尔杂志"。
7. **刘维尔函数**：数论中的重要函数，以其命名。
8. **Liouville–Green 方法（WKB 近似）**：1837 年寻求变系数二阶线性微分方程的近似解（渐近级数），后由 Jeffreys（1923）、Wentzel–Kramers–Brillouin（1926）在量子力学薛定谔方程研究中重新发现，即 WKB 近似。
9. **分数阶微积分（Riemann–Liouville 积分）**：在电动力学研究中发展任意阶微分与积分。
10. **荣誉**：荣誉军团指挥官、ForMemRS；月球环形山 Liouville 以其命名。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（法国深蓝） | `#1F3A93` | 法兰西理性 |
| 强调色（数学金） | `#C9A227` | 超越数 / 尊崇 |
| 分类色 1（数论/超越数 — 靛蓝） | `#4C5FD5` | 刘维尔数 / 刘维尔函数 |
| 分类色 2（复分析 — 青绿） | `#0E7C7B` | 刘维尔定理 |
| 分类色 3（数学物理 — 琥珀） | `#E07B30` | Sturm–Liouville / WKB |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「超越数 / 相空间」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典庄重 / 学术出版家的严谨**（创办杂志、编辑伽罗瓦著作的学术严谨）
- **匹配理由**：
  - 刘维尔是超越数证明者、Sturm–Liouville 理论创立者、伽罗瓦著作的编辑出版者——需**庄重、典雅、严谨**的配乐
  - "严谨" 匹配其分析、数论的深度
  - "典雅" 匹配其创办杂志、编辑出版的文化贡献
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：古典 / 庄重 / 典雅风格曲目
  - 备选：历史感深沉曲目（呼应 19 世纪法国）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「超越数的证明者 · Sturm–Liouville 理论的创立者」+ 刘维尔 1809–1882 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：超越数 / 复分析 / 数学物理 / 出版 四分类
4. **早年与教育**（1809–1836）：Saint-Omer、École Polytechnique、桥梁道路学校
5. **超越数的证明**（核心贡献页）：1844 第一个证明超越数存在、刘维尔数、判据
6. **刘维尔定理（复分析）**（核心贡献页）：有界整函数为常数
7. **Sturm–Liouville 理论**（核心贡献页）：与 Sturm 合作、推广傅里叶分析
8. **刘维尔定理（哈密顿力学）与相空间**（核心贡献页）：相空间体积守恒、统计力学基础
9. **出版伽罗瓦著作**（核心叙事页）：1846 编辑出版、推动群论发展
10. **创办杂志与学术生涯**：Journal de Mathématiques、政治参与（1848 制宪议会）
11. **Liouville–Green 方法与其他贡献**：WKB 近似、分数阶微积分、刘维尔函数
12. **终章**：73 岁、从超越数到数学物理的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **超越数"第一个证明"**：Liouville 1844 年**第一个证明超越数存在**，并给出具体例子（刘维尔数）——但需注意"超越数存在"此前 Liouville 之前无人严格证明（刘维尔数是最早的显式超越数例子）。勿写"发明了超越数"。
- **刘维尔定理（复分析）**：有界整函数为常数——这是复分析的刘维尔定理，与哈密顿力学的刘维尔定理是**两个不同定理**，勿混淆。
- **刘维尔定理（哈密顿力学）**：1838 年论文证明相空间体积守恒，Gibbs 之后被认定为**统计力学基础**——是"后被认定"，勿写 Liouville 建立了统计力学。
- **Sturm–Liouville 理论**：与 Sturm **合作**建立（1830 年代），受傅里叶圆柱热扩散**启发**，是傅里叶分析的推广——勿写 Liouville 独创，也勿写完全严格（原表述未充分处理特征函数完备性，后由 Bôcher、Mason、Birkhoff 等完善）。
- **出版伽罗瓦著作**：Liouville **编辑出版**伽罗瓦的著作（1846），使伽罗瓦理论广为人知——是"编辑出版"而非"发现"伽罗瓦理论（伽罗瓦本人已创立，只是生前未获认可）。
- **Liouville–Green 方法（WKB）**：Liouville 1837 年、Green 同年独立发现；1923 年 Jeffreys、1926 年 Wentzel–Kramers–Brillouin 重新发现——勿写 Liouville 命名了 WKB。
- **创办杂志**：1836 年创办，仿 Crelle's Journal，人称"刘维尔杂志"（甚至 1875 年辞去主编后仍如此称呼）——表述准确。
- **无肖像**：`images.txt` 中无 Liouville 本人肖像（第一张为杂志封面），封面头像需确认可用肖像，否则用装饰圆占位。
- **死亡**：1882-09-08 逝于巴黎，享年 73（死亡登记为 9 月 9 日，以 Wikipedia infobox 9 月 8 日为准）。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q214549 | 待写入 |
| name_zh | 刘维尔（或 约瑟夫·刘维尔） | 待写入 |
| name_en | Joseph Liouville | 待写入 |
| birth_date | 1809-03-24 | 待写入 |
| death_date | 1882-09-08 | 待写入 |
| nationality | France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematical analysis / number theory / complex analysis | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：Siméon Denis Poisson、Louis Jacques Thénard
- **学生**：Nikolai Bugaev、Eugène Charles Catalan、Charles Hermite（非正式）
- **合作者**：Jacques Charles François Sturm（Sturm–Liouville 理论）
- **编辑出版**：Évariste Galois（1846 出版其著作）
- **通信 / 学术**：William Thomson（Lord Kelvin）、Carl Gustav Jacob Jacobi、Peter Gustav Lejeune Dirichlet
- **支持的后辈**：Joseph Bertrand、Joseph-Alfred Serret
- **争议**：Guillaume Libri（法国科学院争吵，见 Historia Mathematica）

## 8. 奖项清单

- Commander of the Legion of Honour（荣誉军团指挥官）
- Foreign Member of the Royal Society（英国皇家学会外籍会员）
- Officer of the Legion of Honour（荣誉军团军官）
- 1851 年瑞典皇家科学院外籍会员、1853 年美国哲学会会员

## 9. 机构清单

- 教育：École Polytechnique、École Nationale des Ponts et Chaussées、Lycée Saint-Louis
- 任职：École Polytechnique（1838 起教授）、Collège de France（1851 起）、Journal de Mathématiques Pures et Appliquées（主编）、Science Faculty of Paris（1857 理性力学教席）、Bureau des Longitudes

## 10. 终审清单

- [ ] 生卒 1809-03-24 / 1882-09-08，享年 73，出生地 Saint-Omer
- [ ] 超越数"第一个证明存在、刘维尔数"表述准确
- [ ] 两个刘维尔定理（复分析 vs 哈密顿力学）区分清楚
- [ ] 哈密顿力学定理"后被认定为统计力学基础"表述准确
- [ ] Sturm–Liouville"与 Sturm 合作、推广傅里叶分析"表述准确
- [ ] 出版伽罗瓦著作"编辑出版"表述准确
- [ ] Liouville–Green"WKB 后重新发现"表述准确
- [ ] 创办杂志"仿 Crelle's Journal"表述准确
- [ ] 头像确认（无肖像则装饰圆占位）
- [ ] 国籍用「法国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Joseph_Liouville/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认有无可用肖像（本地 images.txt 无本人肖像，需用装饰圆占位或另寻）
- [ ] **国籍**：封面顶部徽章明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Hamilton / Dirichlet / Jacobi）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
