# William Rowan Hamilton（威廉·罗恩·哈密顿）立传提示词

> qid=Q11887 · 1805-08-04 – 1865-09-02 · 爱尔兰数学家、物理学家、天文学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/William_Rowan_Hamilton/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 爱尔兰`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「四元数 / 相空间」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Sir William Rowan Hamilton（中文惯称：哈密顿）
- **生卒**：1805-08-04 生于都柏林（爱尔兰）→ 1865-09-02 逝于都柏林，享年 60（痛风）
- **国籍**：United Kingdom of Great Britain and Ireland（大不列颠及爱尔兰联合王国，今爱尔兰）
- **身份**：数学家、物理学家、天文学家（四元数、哈密顿力学、光学）
- **家庭**：父 Archibald Hamilton（律师）；九子女中排行第四；3 岁起由叔父 James Hamilton（都柏林三一学院毕业生，在 Trim 办学）抚养；1833 年娶 Helen Bayly，育 3 子女
- **教育轨迹**：
  - 自幼神童，7 岁学希伯来语，13 岁前在叔父指导下掌握约 12 种语言（含波斯语、阿拉伯语、梵语等）
  - 10 岁读欧几里得拉丁文版，12 岁读牛顿《普遍算术》，16 岁通读《原理》大部
  - 1823 年（17 岁）考入都柏林三一学院
  - 1827 年获 BA，1837 年获 MA
- **导师**：John Brinkley（爱尔兰皇家天文学家，称 17 岁的 Hamilton"现在就是同龄人中第一数学家"）
- **研究领域**：力学、光学、四元数、代数、天文

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **四元数的发现（最著名叙事）**：1843 年 10 月 16 日，与妻子在都柏林皇家运河散步时，灵光闪现出方程 **i² = j² = k² = ijk = −1**，随即用小刀把方程刻在附近的布鲁姆桥（Broom Bridge）上。四元数**放弃了交换律**（当时是激进的一步），使 Hamilton 成为现代线性代数的奠基者之一，并创造 "tensor"、"scalar"、"vector" 等词。
2. **哈密顿力学（对物理影响最深）**：对拉格朗日力学的重新表述，揭示动量与位置的对称性；哈密顿量（Hamiltonian）是经典力学与量子力学的核心起点。David Spearman 称"哈密顿形式体系永不过时"。
3. **哈密顿原理（最小作用量原理）**：基于变分法的"变作用"（Varying Action）原理，是分析力学的基石。
4. **Hamilton–Jacobi 方程**：与 Jacobi 共同发展，是理论力学与量子理论的重要工具。
5. **锥形折射（conical refraction）**：从 Fresnel 波面的几何预言：光进入双轴晶体某角度会以空心锥形射出，后被实验证实，1834 年获 Cunningham Medal。
6. **光学-力学类比**：1827 年提出"哈密顿主函数"，统一力学与光学理论，奠定光的波动说的数学基础。
7. **Icosian game / 哈密顿路径**：1856 年发明的"二十面体游戏"基于图论中的哈密顿路径概念。
8. **神童与心算败北**：1813 年（8 岁）与 9 岁美国心算神童 Zerah Colburn 比赛心算败北，从此减少语言学习、专注数学。
9. **荣誉**：1835 年封爵（Knight Bachelor）、Cunningham Medal（1834、1848）、Royal Medal（1835）、1864 年美国国家科学院首批外籍院士名单居首。
10. **个人生活**：早年求婚被拒曾陷抑郁；与诗人华兹华斯、柯勒律治交往；是虔诚基督徒、"柯勒律治信徒"。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（爱尔兰深绿） | `#1B5E20` | 爱尔兰 / 都柏林 |
| 强调色（数学金） | `#C9A227` | 四元数 / 爵士 |
| 分类色 1（四元数 — 靛蓝） | `#4C5FD5` | 四元数 / 向量 |
| 分类色 2（力学 — 青绿） | `#0E7C7B` | 哈密顿力学 / 相空间 |
| 分类色 3（光学 — 琥珀） | `#E07B30` | 锥形折射 / 光学-力学类比 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「四元数 / 相空间」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典典雅 / 灵感闪现的灵动**（散步时灵光一现的传奇）
- **匹配理由**：
  - 哈密顿在散步中灵光一现发现四元数——需**典雅、灵动、有诗意**的配乐，呼应灵感闪现
  - "诗意" 匹配其与华兹华斯、柯勒律治等诗人的交往
  - "典雅" 匹配其爱尔兰学者、爵士的身份
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/典雅/灵动风格）：
  - 首选：古典 / 典雅 / 灵动风格曲目（呼应灵感闪现）
  - 备选：历史感深沉 / 诗意曲目（呼应其诗人气质）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「四元数与哈密顿力学的奠基者」+ 哈密顿 1805–1865 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：四元数 / 哈密顿力学 / 光学 / 生平 四分类
4. **神童与早年**（1805–1823）：语言天赋、心算败北、三一学院、Brinkley 评价
5. **四元数的发现**（核心叙事页）：1843 散步、i²=j²=k²=ijk=−1、Broom Bridge、放弃交换律
6. **向量代数的开创**（核心贡献页）：tensor/scalar/vector、点积叉积
7. **哈密顿力学**（核心贡献页）：哈密顿量、相空间、动量位置对称
8. **哈密顿原理与 Hamilton–Jacobi 方程**（核心贡献页）：变作用、最小作用量
9. **光学与锥形折射**（核心贡献页）：光学-力学类比、1834 Cunningham Medal
10. **Icosian game 与哈密顿路径**（核心贡献页）：图论
11. **荣誉与个人生活**：封爵、皇家奖章、与诗人交往、封爵
12. **终章**：60 岁、从四元数到量子力学的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **四元数发现故事**：Hamilton 1843-10-16 与妻子散步时想出 i²=j²=k²=ijk=−1 并刻在 Broom Bridge 上——是**著名轶事**，但需注意桥上的刻痕已无存（现存的是 1958 年揭幕的石碑）。
- **四元数与 Rodrigues**：1840 年 **Benjamin Olinde Rodrigues** 已得到近乎四元数的结果（差名称）——勿写 Hamilton 完全独创四元数。
- **放弃交换律**：四元数**放弃了交换律**（i·j ≠ j·i），这是当时激进的一步——需强调其革命性。
- **哈密顿力学与量子力学**：哈密顿形式体系"同样适用于量子理论"——是后世评价，勿写 Hamilton 预见了量子力学。
- **Lagrangian 与 Lagrange 方程**：Wikipedia 指出"现在所称的 Lagrangian 与 Lagrange 方程的发现也应归功于 Hamilton"——表述需谨慎，通常归功于 Lagrange，此处是 Wikipedia 的特定观点。
- **锥形折射**：Hamilton 从 Fresnel 波面几何**预言**，后被实验证实——是"预言后被证实"，勿写 Hamilton 做了实验。
- **心算败北**：1813 年与 Zerah Colburn 比赛败北，Colburn 明确胜出——是"败北"轶事，体现其转向数学的契机。
- **语言天赋存疑**：部分史学家对 Hamilton "掌握 12 种语言"的说法存疑（认为只是基础理解）——表述时可用"据称"。
- **无肖像**：`images.txt` 中无 Hamilton 本人肖像（多为铭牌、硬币、雕塑），封面头像需确认可用肖像，否则用装饰圆占位。
- **死亡**：1865-09-02 逝于都柏林，享年 60，痛风发作，葬于 Mount Jerome 公墓；去世时仍在完成《四元数原理》（Elements of Quaternions，762 页，其子 William Edwin 1866 年出版）。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q11887 | 待写入 |
| name_zh | 哈密顿（或 威廉·罗恩·哈密顿） | 待写入 |
| name_en | William Rowan Hamilton | 待写入 |
| birth_date | 1805-08-04 | 待写入 |
| death_date | 1865-09-02 | 待写入 |
| nationality | United Kingdom（今爱尔兰） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | quaternion / mechanics / optics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：John Brinkley（爱尔兰皇家天文学家）
- **学术相关**：Carl Gustav Jacob Jacobi（Hamilton–Jacobi 方程）、Joseph Liouville（扩展其工作）、Augustus De Morgan（通信）、Niels Henrik Abel（五次方程研究）
- **诗人交往**：William Wordsworth、Samuel Taylor Coleridge、Felicia Hemans（听其天文讲座后作诗）
- **家族**：妻 Helen Bayly、子 William Edwin Hamilton（出版《四元数原理》）、姐/妹 Eliza Mary Hamilton（诗人）
- **早期交往**：Maria Edgeworth（小说家）、Catherine Disney（爱慕对象）

## 8. 奖项清单

- Royal Medal（皇家奖章，1835，锥形折射）
- Cunningham Medal（坎宁安奖章，1834、1848，两次）
- Knight Bachelor（爵士，1835）
- Fellow of the American Academy of Arts and Sciences
- 1864 年美国国家科学院首批外籍院士（名单居首）

## 9. 机构清单

- 教育：Trinity College Dublin（BA 1827、MA 1837）、Westminster School
- 任职：Trinity College Dublin（Andrews 天文学教授，1827–1865）、Dunsink Observatory（邓辛克天文台第三任台长，1827–1865）

## 10. 终审清单

- [ ] 生卒 1805-08-04 / 1865-09-02，享年 60，出生地都柏林
- [ ] 四元数"1843 散步、刻桥、Rodrigues 先行"表述准确
- [ ] 放弃交换律"激进一步"表述准确
- [ ] 哈密顿力学"后世用于量子力学"表述准确
- [ ] 锥形折射"预言后被证实"表述准确
- [ ] 心算败北"轶事"表述准确
- [ ] 语言天赋"据称 12 种"表述准确
- [ ] 头像确认（无肖像则装饰圆占位）
- [ ] 国籍用「爱尔兰」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/William_Rowan_Hamilton/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认有无可用肖像（本地 images.txt 无本人肖像，需用装饰圆占位或另寻）
- [ ] **国籍**：封面顶部徽章明示爱尔兰
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 Brinkley"同龄人中第一数学家"、Spearman 评价）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Dirichlet / Jacobi / Cauchy）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
