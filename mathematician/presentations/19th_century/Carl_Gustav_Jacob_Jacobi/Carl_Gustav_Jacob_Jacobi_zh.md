# Carl Gustav Jacob Jacobi（卡尔·古斯塔夫·雅各布·雅可比）立传提示词

> qid=Q76564 · 1804-12-10 – 1851-02-18 · 德国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Carl_Gustav_Jacob_Jacobi/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「椭圆函数 / 周期格」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Carl Gustav Jacob Jacobi（本名 Jacques Simon Jacobi，拉丁名 Carolus Gustavus Jacobus Jacobi，中文惯称：雅可比）
- **生卒**：1804-12-10 生于波茨坦（Potsdam，勃兰登堡侯国，普鲁士王国）→ 1851-02-18 逝于柏林，享年 46（天花）
- **国籍**：Kingdom of Prussia（普鲁士王国，今德国）
- **身份**：数学家（椭圆函数、动力学、微分方程、行列式、数论）
- **家庭**：阿什肯纳兹犹太裔；父 Simon Jacobi（银行家）；四子女中排行第二；兄 Moritz von Jacobi（后成为工程师、物理学家）；由伯父 Lehman 家教启蒙
- **教育轨迹**：
  - 1816 年入波茨坦文科中学（Gymnasium），半年后跳级到高年级（因年龄不足 16 岁无法入大学，在毕业班待到 1821）
  - 1821 年入柏林大学，起初兼顾语文学与数学
  - 1825 年获柏林大学博士学位（导师 Enno Dirksen 主持答辩，论文关于有理分式的部分分式分解），随后 habilitation，并**皈依基督教**
- **导师**：Enno Dirksen（博士导师）
- **研究领域**：椭圆函数、微分几何、数论、力学、行列式

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **椭圆函数理论奠基（最著名贡献）**：1829 年《椭圆函数新理论基础》（Fundamenta nova theoriae functionum ellipticarum）系统发展了椭圆函数与椭圆 theta 函数理论；雅可比椭圆函数、theta 函数、雅可比三重积公式。
2. **与 Abel 的竞争**：与阿贝尔在椭圆函数领域激烈竞争，共同推动椭圆函数从椭圆积分走向椭圆函数本身。
3. **"总是反转"（Invert, always invert）**：名言"man muss immer umkehren"——反转已知结果开辟新领域（如反转椭圆积分、聚焦椭圆函数与 theta 函数的本质）。
4. **Hamilton–Jacobi 理论**：对经典力学的奠基性贡献，Hamilton–Jacobi 方程。
5. **雅可比矩阵 / 行列式（Jacobian）**：由 n 个函数的偏导数构成的行列式，在多重积分变量替换中至关重要；雅可比特征值算法。
6. **雅可比恒等式（Jacobi identity）**：李代数中结合律的类比，是李理论、哈密顿力学、算子代数的核心。
7. **雅可比符号（Jacobi symbol）**：数论中二次互反律的推广；继续高斯的工作。
8. **数论贡献**：第一个把椭圆函数应用于数论，证明费马二平方定理、拉格朗日四平方定理（及 6、8 平方的类似结果）。
9. **行列式理论**：行列式理论的早期奠基者之一，重新引入 Legendre 的偏导符号 ∂（1841 年起成为标准）。
10. **生平**：1829 年任柯尼斯堡大学数学教授（直至 1842）；1843 年因过度劳累精神崩溃，访问意大利休养；1848 年革命中参与政治（自由派竞选失败，皇家津贴一度被削减，后经洪堡干预恢复）；1851 年死于天花。
11. **荣誉**：Pour le Mérite、Grand prix des sciences mathématiques、ForMemRS；月球环形山 Jacobi 以其命名。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（普鲁士深蓝） | `#1F3A93` | 德意志理性 |
| 强调色（数学金） | `#C9A227` | 高产 / 天才 |
| 分类色 1（椭圆函数 — 青绿） | `#0E7C7B` | theta 函数 / 椭圆函数 |
| 分类色 2（力学 — 靛蓝） | `#4C5FD5` | Hamilton–Jacobi / 恒等式 |
| 分类色 3（数论/行列式 — 琥珀） | `#E07B30` | 雅可比符号 / Jacobian |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「椭圆函数的周期格 / theta 函数」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典庄重 / 天才早逝的怅惘**（46 岁天才的辉煌与早逝）
- **匹配理由**：
  - 雅可比是椭圆函数奠基者、天才数学家，46 岁死于天花——需**庄重、典雅、略带怅惘**的配乐，呼应天才早逝
  - "典雅" 匹配其椭圆函数、theta 函数的优美理论
  - "怅惘" 匹配其精神崩溃、政治挫折与早逝
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：古典 / 庄重 / 典雅风格曲目
  - 备选：历史感深沉 / 怀旧曲目（呼应天才早逝）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「椭圆函数理论的奠基者 · 总是反转的天才」+ 雅可比 1804–1851 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：椭圆函数 / 力学 / 数论与行列式 / 生平 四分类
4. **早年与教育**（1804–1826）：波茨坦、犹太裔、跳级、柏林大学、皈依基督教
5. **椭圆函数理论**（核心贡献页）：Fundamenta nova、theta 函数、雅可比三重积
6. **与 Abel 的竞争**（核心叙事页）：椭圆函数竞争、"总是反转"
7. **Hamilton–Jacobi 理论与雅可比恒等式**（核心贡献页）
8. **雅可比矩阵与行列式**（核心贡献页）：Jacobian、∂ 符号重引入
9. **数论贡献**（核心贡献页）：雅可比符号、二平方/四平方定理
10. **生平与晚年**：柯尼斯堡教授、精神崩溃、1848 革命、死于天花
11. **荣誉与遗产**：Pour le Mérite、Grand prix、月球环形山、Gesammelte Werke
12. **终章**：46 岁、椭圆函数与力学天才的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **生卒日期**：出生日 metadata 有 1804-12-10 与 1805-12-10 两个值，以 Wikipedia infobox **1804-12-10** 为准；死亡 1851-02-18，享年 46。
- **椭圆函数与 Abel**：雅可比与阿贝尔**竞争**（共同推动椭圆函数发展），但雅可比在阿贝尔 1829 年早逝后系统发展了该理论——勿写成"雅可比独占"或"完全独立"。
- **"总是反转"**：原文 "man muss immer umkehren"，是雅可比对其研究方法的概括（反转已知结果开辟新领域），非严谨定理——引用时注明是教学格言。
- **Hamilton–Jacobi 理论**：是 Hamilton 与 Jacobi 共同发展的理论——勿写成雅可比独创。
- **Jacobian 与 ∂ 符号**：∂ 符号是 **Legendre 引入**，雅可比 1841 年**重新引入并推广为标准**——勿写雅可比发明了 ∂。
- **皈依基督教**：雅可比为获得大学教职而皈依基督教（犹太裔）——客观表述，勿渲染。
- **精神崩溃**：1843 年因**过度劳累**精神崩溃，访问意大利休养——是"过劳崩溃"，非其他原因。
- **死亡**：1851 年死于**天花**（smallpox），享年 46——勿误写为其他死因。
- **1848 革命**：参与自由派政治，竞选失败，皇家津贴被削减，后经 Alexander von Humboldt 干预恢复——客观表述。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76564 | 待写入 |
| name_zh | 雅可比（或 卡尔·古斯塔夫·雅各布·雅可比） | 待写入 |
| name_en | Carl Gustav Jacob Jacobi | 待写入 |
| birth_date | 1804-12-10 | 待写入 |
| death_date | 1851-02-18 | 待写入 |
| nationality | Germany（普鲁士王国） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | elliptic function / mechanics / number theory | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **博士导师**：Enno Dirksen
- **学生**：Otto Hesse、Paul Gordan、Carl Wilhelm Borchardt、Friedrich Julius Richelot、Wilhelm Scheibner、Gustav Kirchhoff（非正式）
- **竞争 / 合作**：Niels Henrik Abel（椭圆函数竞争）、Adrien-Marie Legendre（∂ 符号来源）、William Rowan Hamilton（Hamilton–Jacobi 理论）、Karl Weierstrass（超椭圆 theta 函数）
- **家族**：兄 Moritz von Jacobi（工程师、物理学家）
- **贵人**：Alexander von Humboldt（干预恢复其皇家津贴）

## 8. 奖项清单

- Pour le Mérite for Sciences and Arts（科学与艺术功勋勋章）
- Grand prix des sciences mathématiques（法国科学院数学大奖）
- Foreign Member of the Royal Society（英国皇家学会外籍会员）

## 9. 机构清单

- 教育：Frederick William University Berlin（柏林大学，博士）、University of Königsberg、Hermann-von-Helmholtz-Gymnasium
- 任职：University of Königsberg（1829–1842 数学教授）、Frederick William University Berlin、Joachimsthalsches Gymnasium

## 10. 终审清单

- [ ] 生卒 1804-12-10 / 1851-02-18，享年 46，出生地波茨坦
- [ ] 椭圆函数"与 Abel 竞争"表述准确
- [ ] "总是反转"注明是教学格言
- [ ] Hamilton–Jacobi"与 Hamilton 共同发展"表述准确
- [ ] ∂ 符号"Legendre 引入、Jacobi 重引入推广"表述准确
- [ ] 皈依基督教客观表述
- [ ] 精神崩溃"过劳"表述准确
- [ ] 死亡"天花"表述准确
- [ ] 国籍用「德国（普鲁士王国）」表述准确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Carl_Gustav_Jacob_Jacobi/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先 Wikipedia infobox 肖像（`images.txt` 第三张 Carl_Jacobi2.jpg）
- [ ] **国籍**：封面顶部徽章明示德国（普鲁士王国）
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 "man muss immer umkehren"）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Cauchy / Gauss / Abel）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
