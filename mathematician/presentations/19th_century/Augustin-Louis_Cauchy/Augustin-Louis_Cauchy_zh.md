# Augustin-Louis Cauchy（奥古斯丁-路易·柯西）立传提示词

> qid=Q8814 · 1789-08-21 – 1857-05-23 · 法国数学家、工程师、物理学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Augustin-Louis_Cauchy/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「复平面 / 围道」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Augustin-Louis Cauchy（中文惯称：柯西）
- **生卒**：1789-08-21 生于巴黎（法兰西王国）→ 1857-05-23 逝于索镇（Sceaux，法兰西第二帝国），享年 67（支气管疾病）
- **国籍**：France（法国）
- **身份**：数学家、工程师、物理学家（复分析奠基、实分析创建、分析严格化）
- **家庭**：父 Louis François Cauchy（旧制度下巴黎警察高官，法国大革命后失职，后成为参议院秘书长，直接受拉普拉斯领导）；母 Marie-Madeleine Desestre；两兄弟；1818 年娶 Aloïse de Bure（其家族是出版柯西大部分著作的出版商），育两女 Marie Françoise Alicia、Marie Mathilde
- **教育轨迹**：
  - 幼年随家避难 Arcueil，由父亲启蒙
  - 1802 年入 École Centrale du Panthéon（巴黎当时最好的中学）
  - 1805 年以 293 名考生中第 2 名考入 École Polytechnique
  - 1807 年（18 岁）毕业，入 École des Ponts et Chaussées（桥梁道路学校），以最高荣誉毕业
- **师承**：Joseph-Louis Lagrange（家族友人，建议其入学）、Pierre-Simon Laplace（其父上司）
- **研究领域**：数学分析、复分析、几何、弹性力学、抽象代数、连续介质力学

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **复分析的奠基者（最著名贡献）**：独自发展了复变函数理论。柯西积分定理（1814 提出雏形，1825 完整形式）、柯西积分公式（1831）、留数定理（1831）至今仍是物理与电气工程教学的核心。
2. **实分析的创建者 / 分析严格化**：《Cours d'analyse》（1821）首次引入不等式与 ε–δ 论证，被 Grabiner 称为"把严格分析教给全欧洲的人"。他是**第一个严格陈述并证明微积分关键定理**者之一。
3. **柯西序列**：以他命名的收敛性概念，是实数完备性的基础。
4. **柯西-施瓦茨不等式**：分析中最基本的不等式之一。
5. **柯西-黎曼方程**：复变函数可微性的充要条件。
6. **泰勒定理**：第一个严格证明泰勒定理（及其余项形式）。
7. **费马多边形数定理**：第一个证明费马多边形数定理。
8. **弹性力学与柯西应力张量**：引入 3×3 对称矩阵（柯西应力张量），创立应力理论，其弹性力学贡献近乎与 Poisson 相当。
9. **超高产**：约 800 篇论文、5 部教材，论文数量仅次于欧拉，全集 27 大卷。
10. **争议与流亡**：强烈保皇派、虔诚天主教徒，1830 年七月革命后拒绝效忠宣誓，流亡瑞士、意大利（都灵，1832–1833 任理论物理教授）、布拉格（1833–1838 任波尔多公爵 Henri d'Artois 科学导师）；因宗教狂热与同事关系紧张，Abel 称他"偏执的天主教徒"但称赞其数学才能。
11. **荣誉**：Pour le Mérite、荣誉军团骑士、Grand Prix（1816 波动理论）、埃菲尔塔 72 名之一。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

> ★ 区别于高斯（普鲁士深蓝 + 数学金），柯西采用**法国国旗主题**配色：法兰西蓝为理性主色，法兰西红为强调色（呼应其保皇派立场与宗教热情），与同世纪高斯形成鲜明区分。

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（法国蓝） | `#0055A4` | 法兰西理性 / 复分析 |
| 强调色（法国红） | `#C0392B` | 保皇派 / 宗教热情 |
| 分类色 1（复分析 — 靛蓝） | `#3D5C9E` | 积分定理 / 留数定理 |
| 分类色 2（实分析 — 青绿） | `#0E7C7B` | 柯西序列 / ε–δ |
| 分类色 3（弹性/代数 — 琥珀） | `#C97B2F` | 应力张量 / 置换群 |
| 分类色 4（生平/遗产 — 石板灰） | `#55606E` | 流亡 / 高产 |
| 背景 | `#F7F6F5` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「复平面 / 围道积分」的视觉语言。
- **tex 配色变量命名建议**：`frenchblue`（主色）、`frenchred`（强调色）、`badgeComplex` / `badgeReal` / `badgeElastic` / `badgeLegacy`（分类色）、`complexpanel` / `realpanel` / `elasticpanel` 等面板底色。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典庄重 / 宗教虔诚**（保皇派天主教徒的严谨与信仰）
- **匹配理由**：
  - 柯西是复分析奠基者、超高产数学家，也是虔诚天主教徒——需**庄重、典雅、有信仰厚度**的配乐
  - "庄重" 匹配其分析严格化的地位
  - "虔诚" 呼应其宗教立场与流亡经历（可选宗教性/管风琴风格的备选）
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：古典 / 庄重 / 典雅风格曲目
  - 备选：宗教宁静 / 历史感深沉曲目（呼应其信仰与流亡）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「复分析的奠基者 · 分析严格化的先驱」+ 柯西 1789–1857 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：复分析 / 实分析 / 弹性与代数 / 生平 四分类
4. **早年与教育**（1789–1810）：巴黎、避难 Arcueil、École Polytechnique、桥梁道路学校
5. **分析严格化与《Cours d'analyse》**（核心贡献页）：ε–δ、柯西序列、泰勒定理
6. **复分析的奠基**（核心贡献页）：柯西积分定理、积分公式、留数定理
7. **柯西-黎曼方程与复变函数**（核心贡献页）
8. **弹性力学与柯西应力张量**（核心贡献页）：应力理论
9. **数论与群论**：费马多边形数定理、置换群
10. **流亡与宗教立场**（核心叙事页）：七月革命、拒誓、都灵/布拉格、宗教狂热
11. **荣誉与高产**：800 篇论文、Grand Prix、Pour le Mérite、埃菲尔塔 72 名
12. **终章**：67 岁、复分析与严格分析的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **复分析"奠基者"**：柯西**独自发展**了复变函数理论，是奠基者——但需注意其理论一度被同代人认为"太复杂"而忽视，直到 1840 年代才被接受（Laurent 是继他之后第一个做出实质贡献者）。
- **实分析"创建者"**：柯西是**最早严格陈述并证明微积分关键定理者之一**，创建实分析——但 Bolzano 也独立做了严格化工作（ε–δ），勿写柯西是"唯一"或"第一个"引入 ε–δ 的人。
- **泰勒定理**：柯西是**第一个严格证明**者——勿写他发明了泰勒定理（泰勒早在 1715 年提出）。
- **柯西积分定理**：雏形 1814 年（24 岁），完整形式 1825 年——勿混淆时间。
- **宗教争议**：Abel 称柯西"偏执的天主教徒"、"疯了、拿他没办法"，但**同时称赞其数学才能**——引用时需完整，勿断章取义。
- **流亡**：1830 年七月革命后**拒绝效忠宣誓**而失去职位流亡——是"因拒誓流亡"，非政治犯罪。
- **波尔多公爵导师**：1833–1838 年任 Henri d'Artois 科学导师，但柯西**是出了名的差讲师**，Henri d'Artois 对数学毫无兴趣——客观表述。
- **与 Liouville 的嫌隙**：因 Libri 事件（Libri 被指控偷书后由 Liouville 而非柯西接替）导致柯西与 Liouville 关系破裂——属学术政治纠葛，可略写。
- **死亡**：1857-05-23 逝于 Sceaux，享年 67，支气管疾病，接受临终圣礼。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q8814 | 待写入 |
| name_zh | 柯西（或 奥古斯丁-路易·柯西） | 待写入 |
| name_en | Augustin-Louis Cauchy | 待写入 |
| birth_date | 1789-08-21 | 待写入 |
| death_date | 1857-05-23 | 待写入 |
| nationality | France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematical analysis / complex analysis / elasticity theory | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **师承**：Joseph-Louis Lagrange（家族友人）、Pierre-Simon Laplace（父上司）
- **学生**：Viktor Bunyakovsky、Mikhail Ostrogradsky、Francesco Faà di Bruno、Gabriel Oltramare
- **竞争 / 争议**：Niels Henrik Abel（称其偏执天主教徒、但赞其数学）、Joseph Liouville（因 Libri 事件嫌隙）、Jean-Marie Constant Duhamel（非弹性碰撞争议，柯西被 Poncelet 证明有误）
- **学术相关**：Augustin-Jean Fresnel（波动理论）、Charles Hermite（柯西病中照料其，引导其皈依天主教）
- **家族**：父 Louis François Cauchy、妻 Aloïse de Bure、两女

## 8. 奖项清单

- Grand prix des sciences mathématiques（法国科学院数学大奖，1816，波动理论）
- Pour le Mérite for Sciences and Arts（科学与艺术功勋勋章）
- Knight of the Legion of Honour（荣誉军团骑士）
- Concours général（全国会考奖）
- Foreign Member of the Royal Society（英国皇家学会外籍会员）
- Fellow of the American Academy of Arts and Sciences
- 1831 年瑞典皇家科学院外籍会员
- 埃菲尔铁塔 72 位法国科学家刻名之一（身后纪念）

## 9. 机构清单

- 教育：École Nationale des Ponts et Chaussées、Lycée Henri-IV、École polytechnique
- 任职：University of Paris（索邦）、University of Turin（都灵，1832–1833）、École polytechnique（1816 起教授）、Collège de France、Corps of bridges, waters and forests（桥梁道路工程兵）

## 10. 终审清单

- [ ] 生卒 1789-08-21 / 1857-05-23，享年 67，出生地巴黎
- [ ] 复分析"奠基者、一度被忽视"表述准确
- [ ] 实分析"最早严格化者之一、Bolzano 亦独立"表述准确
- [ ] 泰勒定理"第一个严格证明"表述准确
- [ ] 柯西积分定理"1814 雏形、1825 完整"表述准确
- [ ] Abel 引语"完整引用（偏执但赞数学）"表述准确
- [ ] 流亡"拒誓"表述准确
- [ ] 波尔多公爵导师"差讲师"客观表述
- [ ] 国籍用「法国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Augustin-Louis_Cauchy/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先 Wikipedia infobox 肖像（`images.txt` 第一张 Cauchy-Portrait.jpg 或第二张石版画）
- [ ] **国籍**：封面顶部徽章明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 Abel 的评价、Grabiner 的评价）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Poisson / Gauss / Poncelet）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
