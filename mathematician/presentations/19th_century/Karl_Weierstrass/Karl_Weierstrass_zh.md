# Karl Weierstrass（卡尔·魏尔斯特拉斯）立传提示词

> qid=Q57103 · 1815-10-31 – 1897-02-19 · 德国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Karl_Weierstrass/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「ε–δ / 处处不可导」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Karl Theodor Wilhelm Weierstraß（常作 Karl Weierstrass，中文惯称：魏尔斯特拉斯）
- **生卒**：1815-10-31 生于奥斯滕费尔德（Ostenfelde，威斯特伐利亚省，普鲁士王国）→ 1897-02-19 逝于柏林，享年 81（肺炎）
- **国籍**：Kingdom of Prussia（普鲁士王国，今德国）
- **身份**：数学家（被誉为"现代分析之父"）
- **家庭**：父 Wilhelm Weierstrass（政府官员）、母 Theodora Vonderforst（莱茵兰天主教家庭）
- **教育轨迹**：
  - 中学（Theodorianum，帕德博恩）期间开始对数学感兴趣
  - 被送入波恩大学学法律、经济、金融（为政府职位准备），但私下研究数学，最终**无学位离校**
  - 后在明斯特学院（Münster Academy）继续学数学，参加 Christoph Gudermann 的讲座，对椭圆函数产生兴趣
  - 获教师资格证，成为中学教师（教数学、物理、植物学、体操）
- **导师**：Christoph Gudermann
- **研究领域**：数学分析、复分析、椭圆函数、变分法

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **ε–δ 语言：折磨一代代微积分初学者（★ 叙事钩子 / 开篇金句）**：
   - 牛顿、莱布尼茨用无穷小，概念混乱；柯西直觉很强，但逻辑不严谨。两百多年数学家被"无穷小到底是不是 0"折磨。
   - 魏尔斯特拉斯抛出 ε–δ 严格定义，把直观的"无限靠近"翻译成量词逻辑 `∀ε∃δ`。
   - 对初学者：量词顺序、去心邻域、逻辑蕴含，极其反直觉；无数人学分析卡在这里。
   - （史实注意：Cauchy 1820 年代已有雏形、Bolzano 1817 年已给较严格定义，Weierstrass 是形式化与系统化者——勿写"第一个提出"。）
2. **现代分析之父（地位定性）**：形式化函数连续性定义、证明介值定理与 Bolzano–Weierstrass 定理，被普遍尊为"现代分析之父"。
3. **魏尔斯特拉斯函数（Weierstrass function）**：构造**处处连续但处处不可导**的函数，是分析史上的著名反例，震动了当时的数学界。
4. **一致收敛（uniform convergence）**：导师 Gudermann 1838 年首次观察到该现象但未定义，Weierstrass 认识到其重要性并**形式化且广泛应用**——纠正了 Cauchy"连续函数逐点极限连续"的错误断言。
5. **魏尔斯特拉斯椭圆函数（℘ 函数）**：以他命名的椭圆函数，是现代椭圆函数理论的基础。
6. **Bolzano–Weierstrass 定理**：闭有界区间上的连续性研究基础。
7. **魏尔斯特拉斯 M 判别法、魏尔斯特拉斯分解定理、Lindemann–Weierstrass 定理**：多项以其命名的分析结果。
8. **变分法**：用其发展的分析工具完整重构变分法理论，建立强极值存在的必要条件，Weierstrass–Erdmann 条件。
9. **与 Sofia Kovalevskaya 的师生情谊（叙事点）**：1870 年（55 岁）结识 Kovalevskaya，因无法让她入大学而私下辅导她四年，视其为最优秀的学生，帮她获海德堡大学博士（免口试）；两人情谊"远超普通师生关系"。1891 年 Kovalevskaya 去世后，Weierstrass 烧掉了她的来信（他的约 150 封信被保留）。
10. **生平与荣誉**：无学位离校→中学教师→荣誉博士（1854 柯尼斯堡）→柏林大学教授（1864）；Copley Medal（1895）、Pour le Mérite、Helmholtz Medal 等。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（普鲁士深蓝） | `#1F3A93` | 德意志理性 |
| 强调色（分析金） | `#C9A227` | 严格 / 尊崇 |
| 分类色 1（ε–δ/连续性 — 靛蓝） | `#4C5FD5` | ε–δ / 一致收敛 |
| 分类色 2（复分析/椭圆函数 — 青绿） | `#0E7C7B` | ℘ 函数 / M 判别法 |
| 分类色 3（反例/变分法 — 琥珀） | `#E07B30` | 处处不可导 / 变分法 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「ε–δ 邻域 / 处处不可导」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典庄重 / 严谨沉思**（现代分析之父的严谨与深刻）
- **匹配理由**：
  - 魏尔斯特拉斯是现代分析之父，以严谨著称——需**庄重、严谨、沉思**的配乐
  - "严谨" 匹配其 ε–δ 形式化与分析的严格化
  - "沉思" 匹配其晚年与 Kovalevskaya 的师生情谊
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/严谨风格）：
  - 首选：古典 / 庄重 / 严谨风格曲目
  - 备选：历史感深沉 / 沉思曲目（呼应其晚年）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「现代分析之父 · 分析的严格化」+ 魏尔斯特拉斯 1815–1897 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：分析严格化 / 复分析与椭圆函数 / 反例 / 生平 四分类
4. **早年与无学位离校**（1815–1843）：中学、波恩大学无学位离校、中学教师
5. **ε–δ 与分析的严格化**（核心贡献页）：开场用 §2 第 1 条的叙事钩子（"折磨一代代微积分初学者"→ 牛顿/莱布尼茨无穷小 → 柯西直觉 → 魏尔斯特拉斯 ∀ε∃δ 量词逻辑）；正文讲连续性定义、介值定理、Bolzano–Weierstrass；可配 ε–δ 定义公式框。
6. **一致收敛**（核心贡献页）：纠正 Cauchy 错误、Gudermann 的先驱观察
7. **魏尔斯特拉斯函数**（核心贡献页）：处处连续处处不可导的反例
8. **复分析与椭圆函数**（核心贡献页）：℘ 函数、M 判别法、分解定理
9. **变分法**（核心贡献页）：理论重构、Weierstrass–Erdmann 条件
10. **与 Sofia Kovalevskaya 的师生情谊**（核心叙事页）：私下辅导、海德堡博士、烧信
11. **荣誉与晚年**：荣誉博士、柏林大学教授、Copley Medal
12. **终章**：81 岁、现代分析之父的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **"现代分析之父"与 ε–δ**：Weierstrass 是 ε–δ 定义的**形式化与系统化者**，但 Cauchy（1820 年代）与 Bolzano（1817 年）已有先行工作——勿写 Weierstrass 是第一个提出 ε–δ 的人。
- **一致收敛**：该概念**首次被 Gudermann（1838）观察到但未定义**，Weierstrass 认识到重要性并**形式化且广泛应用**——勿写 Weierstrass 首次发现一致收敛。
- **纠正 Cauchy 错误**：Cauchy 在 1821 年《Cours d'analyse》中错误断言"连续函数的逐点极限连续"，Weierstrass 用一致收敛概念纠正——是"纠正"，勿写 Cauchy 完全错误（Cauchy 是连续与一致连续未区分）。
- **魏尔斯特拉斯函数**：处处连续处处不可导的函数，是 Weierstrass 构造的**著名反例**——震动当时数学界，是"反例"而非"定理"。
- **Bolzano–Weierstrass 定理**：Bolzano **先证**（但长期不为人知），Weierstrass **独立证明并发表**——与 Bolzano 相关，勿写 Weierstrass 独占。
- **与 Kovalevskaya 的师生情谊**："远超普通师生关系"——客观表述为深厚的师生情谊，勿过度渲染（Wikipedia 用 "far transcended the usual teacher-student relationship"）。
- **无学位离校**：波恩大学**无学位离校**（为政府职位学法律，私下学数学），后获荣誉博士（1854 柯尼斯堡）——是"无学位→荣誉博士"的独特轨迹。
- **无肖像**：`images.txt` 中无 Weierstrass 本人肖像（全为数学公式），封面头像需用装饰圆占位。
- **国籍**：Kingdom of Prussia（普鲁士王国），今属德国——封面用「德国（普鲁士王国）」。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q57103 | 待写入 |
| name_zh | 魏尔斯特拉斯（或 卡尔·魏尔斯特拉斯） | 待写入 |
| name_en | Karl Weierstrass | 待写入 |
| birth_date | 1815-10-31 | 待写入 |
| death_date | 1897-02-19 | 待写入 |
| nationality | Germany（普鲁士王国） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematical analysis / complex analysis / elliptic function | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **博士导师**：Christoph Gudermann
- **学生**：Georg Cantor、Ferdinand Georg Frobenius、Lazarus Fuchs、Wilhelm Killing、Hermann Schwarz、Sofia Kovalevskaya（私下辅导）、Edmund Husserl、Carl Runge 等
- **学术相关**：Bernard Bolzano（Bolzano–Weierstrass 定理）、Augustin-Louis Cauchy（纠正其错误）、Ferdinand von Lindemann（Lindemann–Weierstrass 定理）
- **情谊**：Sofia Kovalevskaya（最优秀的学生、深厚师生情谊）

## 8. 奖项清单

- Copley Medal（科普利奖章，1895）
- Pour le Mérite for Sciences and Arts（科学与艺术功勋勋章）
- Helmholtz Medal（亥姆霍兹奖章）
- Cothenius Medal（科泰尼乌斯奖章）
- Bavarian Maximilian Order for Science and Art（巴伐利亚马克西米利安科学与艺术勋章）
- Foreign Member of the Royal Society（英国皇家学会外籍会员）
- 1854 年柯尼斯堡大学荣誉博士

## 9. 机构清单

- 教育：University of Bonn（无学位离校）、University of Münster、Gymnasium Theodorianum、University of Königsberg（荣誉博士）
- 任职：Frederick William University Berlin（1864 起教授）、Gewerbeinstitut Berlin（1856 起）、Collegium Hosianum（1848 起，Braunsberg）、2nd middle school in Wałcz（1843 起，Deutsch Krone）

## 10. 终审清单

- [ ] 生卒 1815-10-31 / 1897-02-19，享年 81，出生地 Ostenfelde
- [ ] ε–δ"形式化系统化、Cauchy/Bolzano 先行"表述准确
- [ ] 一致收敛"Gudermann 先观察、Weierstrass 形式化"表述准确
- [ ] 纠正 Cauchy 错误"连续与一致连续未区分"表述准确
- [ ] 魏尔斯特拉斯函数"处处连续处处不可导的反例"表述准确
- [ ] Bolzano–Weierstrass"Bolzano 先证、Weierstrass 独立"表述准确
- [ ] 与 Kovalevskaya"深厚师生情谊"客观表述
- [ ] 无学位离校→荣誉博士轨迹表述准确
- [ ] 头像确认（无肖像则装饰圆占位）
- [ ] 国籍用「德国（普鲁士王国）」表述准确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Karl_Weierstrass/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：无肖像，用装饰圆占位
- [ ] **国籍**：封面顶部徽章明示德国（普鲁士王国）
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Boole / Sylvester / Kummer）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
