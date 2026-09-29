# Irving Langmuir（欧文·朗缪尔）立传提示词

> qid=Q184286 · 1881-01-31 – 1957-08-16 · 美国化学家/物理学家 · 20 世纪 · 诺贝尔化学奖（1932，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Irving_Langmuir/`（page.md + metadata.json + page.html + images.txt）

---

## 0. 正文形式说明（参考 Frederick Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Langmuir-sitting.jpg`，约 1900 年照，执行时下载 500px；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 界面之上的分子世界\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「单分子层 / 界面」母题——离散圆点暗示水面上定向排列的油膜分子。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（Langmuir 吸附等温式 / 单分子层示意）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Irving Langmuir（中文惯称：欧文·朗缪尔）
- **生卒**：1881-01-31 生于纽约布鲁克林 → 1957-08-16 逝于马萨诸塞州 Woods Hole（心脏病，短病之后），享年 76；讣告登上《纽约时报》头版
- **国籍**：United States（美国）
- **身份**：化学家、物理学家、冶金工程师（metallurgical engineer）；1932 年诺贝尔化学奖（表面化学）
- **家庭**：四个孩子中的第三个；父 Charles Langmuir、母 Sadie（娘家姓 Comings）；兄 Arthur Langmuir 是研究化学家，鼓励其好奇心并帮他布置人生第一个卧室角落化学实验室；11 岁矫正视力后对自然的兴趣大增。1912 年娶 Marion Mersereau（1883–1971），领养一子 Kenneth、一女 Barbara；自述不可知论者（agnostic）
- **教育轨迹**：先后就读美国与巴黎多所学校（1892–1895 在巴黎）→ 1898 年毕业于费城 Chestnut Hill Academy → 1903 年哥伦比亚大学矿冶学院冶金工程学士（Met.E.）→ 1906 年哥廷根大学博士
- **博士**：1906，论文《Ueber partielle Wiedervereinigung dissociierter Gase im Verlauf einer Abkühlung》（冷却过程中离解气体的部分再复合），实验用 Nernst 发明的 Nernst glower
- **导师**：Friedrich Dolezalek（博士导师，infobox 明载）；Walther Nernst 为 other academic advisor（frontmatter metadata 误把 Nernst 当唯一博士导师——以 infobox 为准）
- **研究领域**：表面化学、等离子体物理、原子结构、大气科学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **布鲁克林观察家（1881）**：父母鼓励仔细观察自然并做详细记录；兄 Arthur 引领入门化学——工程师之家走出的实验科学家。
2. **矿冶工程师的转身（1898–1906）**：Chestnut Hill Academy → 哥伦比亚矿冶学院 → 哥廷根，在 Dolezalek 指导下用 Nernst glower 研究气体再复合获博士学位。
3. **GE 之家（1909–1950）**：入职通用电气研究实验室（Schenectady），41 年工业研究——产学结合的典范；此前短期执教 Stevens Institute of Technology。
4. **白炽灯革命（1909–1913）**：改进扩散泵 → 高真空整流管与放大管；与 Lewi Tonks 发现充惰性气体（氩）可大幅延长钨丝寿命，关键在全过程极端洁净；灯丝绕成紧螺旋提高效率。
5. **表面化学起点**：发现分子氢在钨丝灯泡内离解为原子氢、在玻壳表面形成单原子层——表面化学研究由此发端；1917 年油膜论文成为 1932 年诺奖的直接基础。
6. **单分子层理论（1917）**：带亲水端基的脂肪链油分子在水面上定向排列成单分子厚膜（亲水端入水、疏水链聚于表面），由已知体积与面积即可测膜厚——光谱术之前研究分子构型的利器。
7. **等离子体之父（1920s）**：首批研究等离子体的科学家，因联想到 blood plasma 而命名 ionized gas 为 plasma；与 Tonks 发现电子密度波（Langmuir 波）；提出电子温度概念；1924 年发明静电探针（Langmuir probe），至今等离子体物理标配。
8. **同心原子结构理论（1919）**：在 Gilbert N. Lewis 立方原子与 Walther Kossel 化学键理论基础上发表《The Arrangement of Electrons in Atoms and Molecules》，提出 atomic structure 的 concentric theory；定义现代价壳层（valence shell）概念——与 Lewis 发生优先权之争，理论的荣誉主要属 Lewis，而朗缪尔的演讲才能使理论广为传播。
9. **原子氢焊（发明）**：发现原子氢并发明 atomic hydrogen welding——史上第一次等离子焊接，后发展为 gas tungsten arc welding。
10. **与 Blodgett 的单分子层（1930s）**：与 Katharine B. Blodgett 合作研究薄膜与表面吸附，引入 monolayer（单分子层）概念与描述这种表面的二维物理（Langmuir–Blodgett film）。
11. **1932 诺贝尔化学奖**：官方理由 "for his discoveries and investigations in surface chemistry"——**独享**；1927 年出席第五届索尔维会议。
12. **大气科学与云播撒（1938–1947）**：驳斥鹿马蝇时速 800 英里之说（估算 25 mph）；从马尾藻海漂流海草发现风驱表层环流（Langmuir circulation）；二战与 Vincent J Schaefer 研究声呐、烟幕与机翼除冰，进而用干冰与碘化银实现云播撒（cloud seeding，效率至今有争议）。
13. **病态科学（1953）**：创造 "pathological science" 一词——遵循科学方法却被无意识偏倚污染的研究，原演说举 ESP 与飞碟为例；晚年居 Schenectady（故居 1976 年列为 National Historic Landmark），山顶、冰川命名（阿拉斯加 Mount Langmuir）、ACS 表面科学期刊即名 *Langmuir*。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（铁锈红 rustred） | `#A63A2B` | 工业研究的炽热钨丝与金属光泽（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（表面化学 badgeSurf） | `#2E5A9E` | 蓝单分子层 / 油膜 / 吸附等温线 |
| 分类色 2（等离子体 badgePlasma） | `#8E44AD` | 紫 plasma / Langmuir 波 / 探针 |
| 分类色 3（原子结构 badgeAtom） | `#1B7A43` | 绿同心理论 / 价壳层 |
| 分类色 4（大气科学 badgeAtm） | `#D97B29` | 琥珀云播撒 / Langmuir 环流 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「界面单分子层」的定向排列。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（Documentary Cinematic，路径 `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-...The Invisible Light.wav`）
- **风格**：纪录片 / 电影感 / 工业与探究气质
- **匹配理由**：
  - "纪录片" 匹配其 41 年 GE 工业研究的长期叙事——从灯泡到诺贝尔奖再到云播撒
  - "电影感" 匹配等离子体与大气科学的视觉意象（辉光、云层、海面环流）
  - 曲名 "看不见的光" 暗合其研究对象：肉眼不可见的原子层、电子波与离子气体
- **时长**：执行时核对，不足 15 页 × 7 秒则循环或 ffmpeg 对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 界面之上的分子世界 / Irving Langmuir 1881–1957 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  朗缪尔的一生 — 高斯式时间线（10 节点：1881→1903→1906→1909→1917→1919→1924→1932→1947→1957）
04  早年与教育：布鲁克林到哥廷根 (1881–1906) — 表格「时间|事件|结果」
05  GE 实验室：白炽灯与高真空 (1909–1913) — 表格「问题|方法|结果」+ 公式框：充氩钨丝寿命
06  表面化学：油膜与单分子层 (1917–1932) — 表格「问题|方法|结果」+ 公式框：Langmuir 吸附等温式
07  等离子体：命名与探针 (1920s) — 表格「对象|方法|结果」+ 公式框：Langmuir probe 原理
08  同心原子结构理论 (1919) — 表格「人物|理论|结果」（Lewis/Kossel/Langmuir）+ 优先权之争注记
09  原子氢焊与薄膜 — 表格「技术|原理|影响」（atomic hydrogen welding / Langmuir–Blodgett film）
10  1932 诺贝尔化学奖 — 官方理由原句 + 表格「奖项|年份|意义」
11  大气科学与云播撒 (1938–1950s) — 表格「问题|方法|结果」（botfly 25mph / Langmuir circulation / cloud seeding）
12  病态科学 (1953) — 高斯 FFT 页式流程图（科学方法 → 无意识偏倚 → 自我欺骗，ESP/飞碟例）
13  遗产与命名 — 四分类遗产盒（表面化学/等离子体/工业研究/大气科学）+ Langmuir 命名清单
14  结尾 — 「把看不见的界面，变成可以度量的科学。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1932 诺奖理由 | 官方措辞 "for his discoveries and investigations in surface chemistry"（表面化学），**独享**——勿泛化成"发明等离子体"或"原子结构"获奖 |
| 博士导师 | infobox 明载 **Friedrich Dolezalek**；Nernst 是 other academic advisor（博士工作用其发明的 Nernst glower）；metadata.json frontmatter 误写 doctoral_advisor=Nernst，**以 infobox 为准** |
| Lewis 之争 | 1919 同心理论 building on Lewis 的 cubical atom——page.md 明文 "credit for the theory itself belongs mostly to Lewis"，朗缪尔功劳在 presentation/popularization；勿写朗缪尔"创立"电子层理论独得荣誉 |
| plasma 命名 | 朗缪尔是**命名者**（因联想 blood plasma），也是首批研究者之一——勿写"等离子体的发现者" |
| 云播撒 | 与 Vincent Schaefer 用干冰与碘化银诱导降水，page.md 明文 "efficiency of this technique remains controversial today"——勿写成确定性突破 |
| 鹿马蝇 | 朗缪尔估算时速 **25 英里**（驳斥 Townsend 的 800 英里说）——数字勿写反 |
| 子女 | Kenneth 与 Barbara 均为**领养**——勿写亲生 |
| 去世地 | Woods Hole, Massachusetts，心脏病，享年 76——勿与出生地 Brooklyn 混淆 |
| 同名区分 | 与德国物理化学家无关之人与 *Langmuir* 期刊、Langmuir isotherm / Langmuir probe / Langmuir waves / Child–Langmuir law / Langmuir–Blodgett film 各为独立条目——引用时勿混 |
| 虚构作品 | Vonnegut《猫的摇篮》Dr. Felix Hoenikker 以朗缪尔为灵感（其兄 Bernard 与朗缪尔共事）——只作轶事一句，不写"朗缪尔发明 ice-nine" |
| 精神信仰 | 自述 agnostic——可在个人生活页一笔带过，勿渲染 |
| 引语红线 | 中文引号内不得出现 page.md 无法溯源的"原话"；正文无直接引语，全部改间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q184286 | ✅ |
| name_zh | 欧文·朗缪尔 | ✅ |
| name_en | Irving Langmuir | ✅ |
| birth_date | 1881-01-31 | ✅ |
| death_date | 1957-08-16 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | surface chemistry（person_field 细分：surface chemistry / plasma physics / atomic structure / atmospheric science，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 学术对手**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Friedrich Dolezalek | 师→生（博士导师） | 哥廷根 1906 博士学位 |
| advisor-student | Walther Nernst | 师→生（other academic advisor） | 博士研究用 Nernst glower |
| influence | Gilbert N. Lewis | 无向 | 1919 同心理论建基于其立方原子模型；两人有优先权之争（理论荣誉主要属 Lewis） |
| colleague | Lewi Tonks | 无向 | 充气灯泡钨丝寿命发现、Langmuir 波共同发现 |
| colleague | Katharine B. Blodgett | 无向 | 单分子层与薄膜合作（Langmuir–Blodgett film） |
| colleague | William Comings White | 无向 | 表兄兼真空管研究助手 |
| colleague | Vincent Schaefer | 无向 | 二战声呐/除冰与云播撒合作 |
| colleague | Guglielmo Marconi | 无向 | 1922 在 GE 实验室展示 20 kW 三极管（合影图注明载） |

**家庭**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Marion Mersereau | 无向 | 1912 年结婚；领养 Kenneth 与 Barbara |

> metadata.json-only 或 page.md 未载实质关系者（无）——本页无禁入库名单；John B. Taylor（Langmuir–Taylor detector，以其工作为基础由 Taylor 自行发展）为单向致谢式命名，不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1932，独享）
- William H. Nichols Medal（1915、1920 两次）
- Hughes Medal（1918）
- Rumford Prize
- Perkin Medal（1928）
- Willard Gibbs Award（1930）
- Franklin Medal（1934）
- Faraday Lectureship Prize（1939）
- Faraday Medal（1944）
- John J. Carty Award for the Advancement of Science（1950）
- Holley Medal；John Scott Award；National Inventors Hall of Fame
- Fellow of the American Academy of Arts and Sciences（1918）；美国国家科学院院士（1918）；American Philosophical Society（1922）；英国皇家学会外籍院士（ForMemRS）

## 9. 机构清单

- 教育：Chestnut Hill Academy（–1898）、Columbia University School of Mines（–1903，冶金工程 BS）、University of Göttingen（PhD 1906）
- 任职：Stevens Institute of Technology（–1909）；General Electric 研究实验室，Schenectady（1909–1950）
- 命名遗产：Langmuir Laboratory for Atmospheric Research（新墨西哥）；ACS 期刊 *Langmuir*；Mount Langmuir（阿拉斯加）；Langmuir College（Stony Brook，1970）；Schenectady 故居（National Historic Landmark，1976）；月球 Joliot 之外的陨石坑另有其名不在本页——本页只写 Mount Langmuir 与期刊

## 10. 终审清单

- [ ] 生卒 1881-01-31 / 1957-08-16，享年 76，出生地 Brooklyn、去世地 Woods Hole
- [ ] 1932 独享、理由为表面化学原句表述准确
- [ ] 博士导师 Dolezalek（infobox 口径）、Nernst 为 other advisor 表述准确
- [ ] Lewis 之争 "理论荣誉主要属 Lewis" 表述准确；plasma 为命名者非发现者
- [ ] 鹿马蝇 25 mph、云播撒"效率有争议"表述准确
- [ ] 子女为领养表述准确；单分子层 1917 论文为诺奖基础表述准确
- [ ] 引语全部可在本地 Wikipedia 原文找到（1932 获奖理由原句）；无原话处全部间接转述
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Irving_Langmuir/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/Langmuir-sitting.jpg`（Commons c.1900 照，250px→500px 下载；失败则装饰圆占位）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（1932 获奖理由）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐
