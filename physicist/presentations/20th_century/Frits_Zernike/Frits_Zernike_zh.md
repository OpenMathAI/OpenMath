# Frits Zernike（弗里茨·泽尔尼克）立传提示词

> qid=Q188293 · 1888-07-16 – 1966-03-10 · 荷兰物理学家 · 20 世纪 · 1953 诺贝尔物理学奖
> 本地 Wikipedia 数据源：`physicist/presentations/20th_century/20th_century/Frits_Zernike/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家标杆 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**。物理学家立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。注意：`images.txt` 中**无 Zernike 本人肖像**（仅有旗帜与 logo 图标），肖像缺位时用装饰圆 + `\faIcon{user}` 占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 荷兰`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像位 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色（诺奖金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「相位光环 / 光波干涉纹」母题。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Frederik "Frits" Zernike（弗里茨·泽尔尼克；infobox 本名 Frederick Zernike，Frits 为惯称）
- **生卒**：1888-07-16 生于阿姆斯特丹（荷兰）→ 1966-03-10 逝于 Amersfoort（Utrecht 省，医院），享年 77（晚年缠绵病榻）
- **国籍**：荷兰（Kingdom of the Netherlands）
- **身份**：物理学家、数学家、发明家、大学教师、化学家（infobox occupation 五项齐列——学科跨度大）
- **家庭**：父 Carl Frederik August Zernike、母 Antje Dieperink——**双亲均为数学教师**，他尤承父亲对物理的热情；首任妻子 Dora van Bommel van Vloten（1945 年去世），育一子；1954 年再婚 Lena Koperberg-Baanders；退休后偕妻移居 Naarden
- **家族荣光**：侄曾孙 **Gerard 't Hooft** 获 1999 年诺贝尔物理学奖；孙女 Kate Zernike 为记者
- **教育轨迹**：
  - 1905 入阿姆斯特丹大学：主修化学，兼修数学、物理
  - 1912 B.Sc.（化学）；同年以气体乳光（opalescence）博士级工作获奖
  - 1915 Ph.D.（物理）
- **博士导师**：Andreas Smits（metadata.json）
- **研究领域**：物理（光学 / 统计物理 / 波动现象——infobox field_of_work: physics）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **教师之家**（1888–1905）：双亲皆为数学教师；从母亲的课堂与父亲的物理热情中起步。
2. **化学主修的物理学博士**（1905–1915）：阿姆斯特丹大学化学主修 + 数学物理兼修；1912 年凭**气体临界点乳光**研究获奖（该方向日后凝结为统计物理经典成果）。
3. **Ornstein–Zernike 方程**（1914）：与 Leonard Ornstein 合作推导临界点理论中的 OZ 方程——至今仍是液体统计力学与高分子物理的核心方程（page.md 明载 "jointly responsible for the derivation"——两人并列）。
4. **格罗宁根的起点**（1913）：任天文学家 Jacobus Kapteyn 在格罗宁根大学天文实验室的助手；1915 任理论力学与数学物理讲师（lector），1920 升**数学物理教授**——此后一生扎根格罗宁根。
5. **1930：幽灵线的相位**：研究光谱线时发现光栅光谱中主线的"**ghost lines**"（鬼线）与主线存在 **90° 相位差**——从光谱学的疑难一步跨入相位光学的核心洞见。
6. **1933：相衬法的诞生**：在 Wageningen 的物理与医学大会上首次描述**相衬技术**（phase contrast technique）在显微术中的应用；并把方法推广用于检验凹面镜面形。
7. **相衬显微镜的生物学革命**：首台相衬显微镜建于**二战期间**；它使无色透明的**活细胞**无需染色即可直接观察——生物学与医学观察方式的范式转变。
8. **Zernike 多项式**：正交圆多项式给出光学像差的"最佳平衡"表述，解决 Seidel 幂级数表述无法清晰分离像差类型与阶数的百年难题；1960 年代起广泛用于光学设计、光学计量与图像分析（如自适应光学、波前检测的行业标准语言）。
9. **相干理论**（1938）：发表 Van Cittert 1934 年定理的更简推导——即 **Van Cittert–Zernike 定理**（远源辐射相干性），其工作唤醒了部分相干光研究；该定理日后成为射电天文干涉成像的理论基石。
10. **Rumford Medal**（1952，皇家学会；理由 "In recognition of his outstanding work in the development of phase contrast microscopy"）——诺奖前夜的国际承认。
11. **1953 诺贝尔物理学奖（独得）**：英文理由 "For his demonstration of the phase contrast method, especially for his invention of the phase contrast microscope"；中文（总名单）"表彰他论证相衬法，尤其是他发明相衬显微镜"。
12. **身后纪念**：格罗宁根大学 **Zernike Campus**、月球 **Zernike 环形山**、小行星 **11779 Zernike**；家族两代诺奖（'t Hooft 1999）传为佳话。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（光学深青） | `#0E7490` | 相位光学 / 相衬的清澈透亮 |
| 强调色（诺奖金） | `#C9A227` | 诺贝尔奖 / 尊崇 |
| 分类色 1（相衬显微镜 — 湖蓝） | `#2E86AB` | ghost lines / 相衬法 / 活细胞观察 |
| 分类色 2（Zernike 多项式 — 紫） | `#7C3AED` | 像差正交多项式 / 光学设计 |
| 分类色 3（相干理论 — 琥珀） | `#E07B30` | OZ 方程 / Van Cittert–Zernike 定理 |
| 分类色 4（格罗宁根传承 — 玫瑰） | `#C4204F` | Kapteyn 实验室 / Zernike Campus / 家族荣光 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「相位光环 / 光波干涉环」的视觉语言——透明的圆环暗喻"让不可见变得可见"。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：纪录片 / 稳重 / "看见不可见之物"（从鬼线疑云到相衬显微镜的耐心长跑）
- **选定曲目**：Inspiring Electronic **The Invisible Light**（纪录片 / 电影 / 稳重）——曲目名与"相衬法让无色透明之物显形"的物理意象天然互文。
- **落地文件**：`physicist/presentations/20th_century/Frits_Zernike/TheInvisibleLight.wav`（复制自音乐库，不入 git）。
- **匹配理由**：Zernike 的故事是"从 1930 年鬼线到 1953 年诺奖"的长线纪录片；The Invisible Light 的稳重叙事感契合光学主题与其沉潜气质，且与本组其他曲目（Expedition / Nostalgia / Eternals / The Flow of Time）来源与气质均不雷同。

## 4. Slide 规划（约 15 页，Wilson 式结构）

1. **封面**（`\titleslide`）：顶部标签「相衬显微镜之父 · 荷兰」+ Zernike 1888–1966 + 右上头像位 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像位 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：相衬法与显微镜 / Zernike 多项式 / 统计物理与相干理论 / 格罗宁根传承
4. **时间线页**：1888 Amsterdam → 1905 入阿姆斯特丹大学 → 1912 B.Sc. 与乳光奖 → 1913 Kapteyn 助手 → 1914 OZ 方程 → 1915 Ph.D. → 1920 教授 → 1930 ghost lines → 1933 Wageningen 相衬 → 二战首台相衬显微镜 → 1952 Rumford → 1953 诺奖 → 1966 逝世
5. **教师之家与化学主修**（1888–1915）：双亲皆数学教师、气体乳光研究获奖
6. **格罗宁根：Kapteyn 助手到数学物理教授**（1913–1920）：天文实验室、1914 OZ 方程、讲席与讲席教授
7. **统计物理遗产**：Ornstein–Zernike 方程（与 Ornstein 并列署名）——液体统计力学的支柱
8. **1930：光谱里的幽灵线**：光栅鬼线与 90° 相位差——问题驱动的光学洞察
9. **1933：相衬法的诞生**：Wageningen 大会、相衬技术、推广至镜面检验——相衬原理示意页
10. **二战期间的首台相衬显微镜与生物学革命**：活细胞无需染色——范式转变
11. **Zernike 多项式**：像差的正交表述、1960s 起光学设计/计量/图像分析的通用语言——多项式示意公式框
12. **相干理论**：1938 Van Cittert–Zernike 定理、部分相干光研究的觉醒
13. **Rumford Medal 与 1953 诺奖**：1952 皇家学会先行承认 → 1953 独得诺奖；总名单中文理由
14. **荣誉与身后**：荷兰皇家科学院（1946）、OSA 荣誉会员（1954）、ForMemRS（1956）；Zernike Campus / 月球环形山 / 小行星 11779；'t Hooft 家族佳话
15. **结尾**：77 岁、"让透明的生命显形的人"的历史地位与遗产（可呼应其诺奖演讲标题 "How I discovered phase contrast"，见 §5）

## 5. 史实陷阱与敏感点（终审必须检查）

- **姓名与目录名**：本名 **Frederik / Frederik Zernike**，惯称 **Frits**；输出目录 `Frits_Zernike`，数据目录同名。行文名用"泽尔尼克"，首次出现写"弗里茨·泽尔尼克（Frederik 'Frits' Zernike）"。
- **获奖理由（独得，无共享者）**：1953 **独得**，中文理由（总名单）"表彰他论证相衬法，尤其是他发明相衬显微镜"；英文 "For his demonstration of the phase contrast method, especially for his invention of the phase contrast microscope"（page.md 载）。**勿**与任何他人并列共享。
- **Zernike 多项式 ≠ 获奖理由（本篇第一大陷阱）**：多项式（光学像差表述）是未获奖的另类重要工作——诺奖表彰的是**相衬法与相衬显微镜**。行文须明确区分两条线，勿写"因 Zernike 多项式获奖"。
- **"被蔡司忽视十几年"**：page.md **无载**任何公司（蔡司/Zeiss）忽视或拒绝的情节——**禁写**具体商业故事；可只用 page.md 可支撑的时间线表述："1930 发现 → 1933 首次描述 → 首台显微镜建于二战期间 → 1953 诺奖"，即从发现到诺奖认可历时二十余年。
- **二战表述**：page.md 仅载"首台相衬显微镜建于二战期间（built during World War II）"——**无**荷兰占领期个人处境的记载，禁写占领、地下抵抗等情节。
- **出生/死亡日期的元数据噪声**：metadata.json 中 date_of_birth/date_of_death 各有两个值（1888-07-16 与 1888-01-01；1966-03-10 与 1966-01-01）——**以 page.md infobox 为准**：1888-07-16 生、1966-03-10 卒。
- **学科身份**：infobox occupation 含 chemist——博士是"化学主修的物理学博士"（B.Sc. 化学 1912 / Ph.D. 物理 1915），身份信息页照实呈现，勿简化成"纯物理学家"。
- **OZ 方程署名**：page.md 明载"Zernike 与 Leonard Ornstein **共同**推导"——勿写 Zernike 单独。
- **Van Cittert–Zernike 定理**：Zernike 1938 的工作是 Van Cittert 1934 定理的**更简推导**（page.md 明载）——定理名含两人，勿写成 Zernike 独立提出原定理。
- **博士导师**：Andreas Smits（metadata.json doctoral_advisor；page.md 未在正文提及）——按 metadata 采用，page.md 无载处以 metadata 为据并保持谨慎。
- **引语**：page.md **无 Zernike 原话**；其诺奖演讲**标题** "How I discovered phase contrast"（1953-12-11，见 page.md 外链注）可照录标题，其余一律间接转述。
- **家族关系**：'t Hooft 为"侄曾孙"（great-nephew）——亲缘代际较远，社会关系库**不建** parent-child 类条目（避免自环/错向），只在叙事中提及。
- **配偶**：两任妻子均有载（Dora 卒于 1945；Lena 1954 再婚）——spouse 条目可建两行或择一注明，注意 Dora 卒年勿写成"离异"。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q188293 | 待写入 |
| name_zh | 泽尔尼克（或 弗里茨·泽尔尼克） | 待写入 |
| name_en | Frits Zernike | 待写入 |
| birth_date | 1888-07-16（以 page.md 为准，弃 metadata 的 1888-01-01） | 待写入 |
| death_date | 1966-03-10（以 page.md 为准，弃 metadata 的 1966-01-01） | 待写入 |
| nationality | Netherlands | 待写入 |
| primary_occupation | physicist | 待写入 |
| field_of_work | physics（光学 / 统计物理 / 相干理论） | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Andreas Smits（metadata.json）
- **合作者（collaborator）**：Leonard Ornstein（Ornstein–Zernike 方程，1914）；Van Cittert（Van Cittert–Zernike 定理脉络）
- **导师侧同事**：Jacobus Kapteyn（格罗宁根天文实验室助手时期）
- **著名博士生**（metadata.json doctoral_student）：Christoffel Jacob Bouwkamp、Herman Johannes de Boer、Harold Hopkins、Bernard Nijboer、Hendrik Groendijk、Clasine van Winter
- **妻子（spouse）**：Dora van Bommel van Vloten（1945 去世）；Lena Koperberg-Baanders（1954 结婚）
- **家族（亲缘）**：Gerard 't Hooft（侄曾孙，1999 诺奖）——亲缘过远，**不建标准关系条目**，仅叙事提及
- **诺贝尔奖同届**：1953 年诺贝尔物理学奖由 Zernike **独得**，无共享者

## 8. 奖项清单

- 诺贝尔物理学奖（1953，独得）
- Rumford Medal（1952，英国皇家学会；"表彰其在相衬显微术发展中的杰出工作"）
- ForMemRS（英国皇家学会外籍院士，1956）
- 荷兰皇家艺术与科学院院士（1946）
- 美国光学学会（OSA）荣誉会员（1954）
- 普瓦捷大学名誉博士（metadata.json：honorary doctor of the University of Poitiers）

## 9. 机构清单

- 教育：阿姆斯特丹大学（1905 入学；B.Sc. 化学 1912；Ph.D. 物理 1915）
- 任职：格罗宁根大学（1913 起——Kapteyn 天文实验室助手 → 1915 lector（理论力学与数学物理）→ 1920 数学物理教授；直到退休）
- 纪念：格罗宁根大学 Zernike Campus；月球 Zernike 环形山；小行星 11779 Zernike

## 10. 终审清单

- [ ] 生卒 1888-07-16 / 1966-03-10，享年 77，出生地 Amsterdam，去世地 Amersfoort（弃 metadata 噪声日期）
- [ ] 诺奖"1953 独得"及总名单中文理由表述准确
- [ ] "获奖理由 = 相衬法与相衬显微镜；Zernike 多项式不在获奖理由中"区分清晰
- [ ] "蔡司忽视"等商业故事未出现（page.md 无载）；二战个人处境未虚构
- [ ] OZ 方程"与 Ornstein 共同"、VCZ 定理"Van Cittert 1934 原定理 + Zernike 1938 简化推导"表述准确
- [ ] 无虚构引语（仅可照录诺奖演讲标题）
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像位 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `Frits_Zernike/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images.txt` 无本人肖像——用装饰圆占位，或经确认后从 Commons Special:FilePath 另行取图（可试 "Frits Zernike.jpg"，404/HTML 即回退占位）
- [ ] **国籍**：封面顶部徽章明示荷兰
- [ ] **引语核对**：仅允许照录诺奖演讲标题 "How I discovered phase contrast"，其余间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪物理学家（Wilson / Wigner / Heisenberg）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
