# George de Hevesy（乔治·德海韦西）立传提示词

> qid=Q76951 · 1885-08-01 – 1966-07-05 · 匈牙利放射化学家 · 20 世纪 · 诺贝尔化学奖（1943，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/George_de_Hevesy/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考化学家桑格立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 images.txt 优先用 c. 1913 实照；404 则装饰圆占位，图注如实标注）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 放射性示踪的开创者\enspace·\enspace 匈牙利`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（György Bischitz）、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「放射性同位素在体内迁移」母题——离散圆点暗示示踪原子随代谢途径的散布与累积。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（如 ^{212}Pb 示踪豆苗吸收、王水溶金反应）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：George Charles de Hevesy（出生名 György Bischitz；匈牙利语 Hevesy György Károly；德语 Georg Karl von Hevesy；中文惯称：乔治·德海韦西）
- **生卒**：1885-08-01 生于布达佩斯（奥匈帝国匈牙利王国）→ 1966-07-05 逝于联邦德国弗莱堡，享年 80；2001 年应家人要求迁葬布达佩斯 Kerepesi 墓园（匈牙利科学院 27 区）
- **国籍**：Hungary（匈牙利；infobox citizenship 兼列 Hungary 与 Germany；1943 年后长期居留瑞典）
- **身份**：放射化学家（radiochemist；1943 年诺贝尔化学奖得主；铪元素共同发现者）
- **家庭**：富裕的受封贵族匈牙利犹太家庭，八兄弟姊妹中排行第五；父 Lajos Bischitz，母 Eugénia（Jenny）Schossberger 女男爵（受封 "De Tornya"）；双方祖辈都曾任佩斯犹太社团主席。家族 1904 年姓氏为 Hevesy-Bischitz，后自行简化为 Hevesy。1924 年娶瑞典人 Pia Riis，育一子三女；其女 Eugenie 嫁给瑞典诺奖得主斯万特·阿伦尼乌斯之孙
- **教育轨迹**：
  - 1903 毕业于布达佩斯 Piarist Gimnázium（比达[Gymnasium]中学）
  - 布达佩斯大学学化学一年 → 柏林-夏洛滕堡理工学院（今 TU Berlin）数月 → 弗莱堡大学转学完成学业；在弗莱堡结识 Ludwig Gattermann
- **导师**：Georg Franz Julius Meyer（博士导师，1906 年在弗莱堡开始博士论文）
- **博士**：1908 年获**物理学**博士学位（弗莱堡大学；论文方向物理化学）
- **研究领域**：放射化学、放射性示踪法（radioactive tracers）、中子活化分析、核化学（infobox Fields: Chemistry, Radiochemistry）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **贵族医生世家的犹太裔少年（1885）**：布达佩斯富裕受封家庭，祖父辈两任佩斯犹太社团主席——优渥家境让他一生可以自由选择研究环境。
2. **游学三国（1903–1906）**：布达佩斯 → 柏林夏洛滕堡 → 弗莱堡；1906 年随 Georg Franz Julius Meyer 开始博士论文，1908 年获物理学博士。
3. **独立 wealth 的自由研究生（1908–1910）**：获 ETH Zürich 职位却因家境殷实可自选去处；先赴卡尔斯鲁厄随 Fritz Haber 工作，再赴曼彻斯特随 Ernest Rutherford 工作——在曼彻斯特结识 Niels Bohr。
4. **回乡教授（1918）**：1918 年在布达佩斯任物理化学教授；1920 年定居哥本哈根。
5. **发现铪（1922）**：与 Dirk Coster 在哥本哈根共同发现 72 号元素铪（Hf，拉丁名 Hafnia 即「哥本哈根」）——依据 Bohr 原子模型判定 72 号应为过渡元素；对 "Bohr 预言" 的通行说法，Mansel Davies 与 Eric Scerri 持异议（归功化学家 Charles Bury）——两说并存。
6. **洛克菲勒基金资助的多产之年**：发展 X 射线荧光分析法、发现钐 α 射线；从此开创用放射性同位素研究动植物代谢的示踪方法。
7. **第一篇示踪论文（1923）**：用天然放射性 ^{212}Pb 作示踪剂，追踪其在蚕豆（Vicia faba）根、茎、叶中的吸收与转运——放射性示踪法的开山之作。
8. **弗莱堡教授与康奈尔讲席（1924/1930）**：1924 年回弗莱堡任物理化学教授；1930 年任康奈尔大学 Baker Lecturer。
9. **重返哥本哈根（1934）**：纳粹上台后离开德国回到 Bohr 研究所；1936 年发明**中子活化分析**（Neutron Activation Analysis）。
10. **王水溶金救奖章（二战）**：Max von Laue 与 James Franck 把金质诺奖奖章寄存丹麦；德军入侵丹麦后奖章面临搜查——海维西用王水将其溶解，静置于哥本哈根研究所架子上；战后捞出金沉淀，诺贝尔学会重铸奖章归还两位得主。
11. **流亡斯德哥尔摩（1943）**：哥本哈根已容不下犹太科学家，流亡瑞典；在斯德哥尔摩大学工作至 1961 年退休后仍任科学同事。同年获 1943 年诺贝尔化学奖——"for his key role in the development of radioactive tracers to study chemical processes such as in the metabolism of animals"（本地页面口径）。
12. **与 von Euler-Chelpin 的战时合作**：在斯德哥尔摩受到德裔瑞典教授、诺奖得主 Hans von Euler-Chelpin 接待；后者亲德立场未改，二人战时战后仍合作发表多篇论文。
13. **Copley 之傲与身后（1949–2005）**：1949 获 Copley Medal——自述 "The public thinks the Nobel Prize in chemistry for the highest honor that a scientist can receive, but it is not so. Forty or fifty have received Nobel chemistry prizes, but there are only ten foreign members of the Royal Swedish Academy, and only two have received a Copley."（另一人是 Bohr）；1958 获 Atoms for Peace Award；一生发表 397 篇科学文献；2005 年丹麦 Risø 国家实验室成立 Hevesy Laboratory，尊其为「同位素示踪原理之父」。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（靛蓝 indigo） | `#283593` | 放射化学的深邃与原子世界的不可见之光（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签；亦呼应「王水溶金」的金色母题） |
| 分类色 1（放射性示踪 badgeTracer） | `#1565C0` | 蓝 ^{212}Pb 示踪 / 中子活化分析 |
| 分类色 2（铪的发现 badgeHafnium） | `#00695C` | 青 72 号元素 / X 射线荧光 |
| 分类色 3（战时传奇 badgeWartime） | `#AD1457` | 玫瑰王水溶金 / 流亡斯德哥尔摩 |
| 分类色 4（核化学谱系 badgeNuclear） | `#6A1B9A` | 紫 Bohr 研究所 / 应用放射化学 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「示踪原子在生物体内的迁移路径」——从根到叶的离散落点。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（文件 `36-aqLUvpAdLNQ-Awaken.wav`；不要复制 wav 到本目录，Makefile 由主控预置）
- **风格**：曙光 / 觉醒 / 由暗到明的上行叙事
- **匹配理由**：
  - "觉醒" 匹配示踪法的开创——首次让不可见的化学过程「被看见」，原子从此亮起微光
  - "由暗到明" 匹配其战时经历——纳粹阴影下流亡、王水守护奖章，战后在斯德哥尔摩迎来 1943 诺奖
  - "上行叙事" 匹配一生轨迹——布达佩斯 → 弗莱堡 → 曼彻斯特 → 哥本哈根 → 斯德哥尔摩，每一步都是新的黎明
- **时长**：以曲目实际时长为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 放射性示踪的开创者 / George de Hevesy 1885–1966 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  海维西的一生 — 高斯式时间线（10 节点：1885→1906→1908→1918→1920→1922→1923→1936→1943→1966）
04  早年：布达佩斯与三国游学 (1885–1908) — 表格「时间|事件|结果」
05  随 Haber 与 Rutherford 做研究 (1908–1918) — 表格「时间|地点|收获」（卡尔斯鲁厄/曼彻斯特/布达佩斯教授）
06  发现铪 (1922) — 表格「问题|方法|结果」+ 公式框：72 号元素 Hf = Hafnia（哥本哈根）
07  放射性示踪法 (1923) — 表格「问题|方法|结果」+ 公式框：^{212}Pb 示踪蚕豆吸收与转运
08  中子活化分析 (1936) — 表格「挑战|方法|结果」
09  王水溶金救奖章 (1940–1945) — 表格「处境|对策|结果」+ 公式框：Au + 王水 → HAuCl₄ 溶液静置 → 复沉、重铸
10  流亡斯德哥尔摩与 1943 诺奖 — 表格「人物|方向|结果」（von Euler-Chelpin 合作 / Stockholm 大学 / 诺奖演讲 1944-12-12）
11  荣誉与谦逊 — 高斯式「类别|代表|意义」表格（含 itemize 荣誉清单：Copley 1949 / Faraday 1950 / Atoms for Peace 1958 / Niels Bohr 金奖 1961）
12  Hevesy Laboratory 与示踪原理的传承 — 高斯式流程图（1923 首篇示踪论文 → 医学诊断 → 中子活化 → 2005 Risø Hevesy Laboratory）
13  遗产：让不可见的过程现形 — 四分类遗产盒 + 公式框：397 篇文献 · 「同位素示踪原理之父」
14  结尾 — 「给原子点上微光，化学过程从此现形。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1943 诺奖理由 | 本地页面口径 "for his key role in the development of radioactive tracers to study chemical processes such as in the metabolism of animals"——页面未载官方 citation 整句的其他表述，**禁止杜撰**；独享（页面无共同得主记载） |
| 博士学科 | 1908 年获**物理学**博士学位（弗莱堡）——勿写成化学博士 |
| 本名与姓氏 | 出生名 György Bischitz，家族 1904 年为 Hevesy-Bischitz，后自行改为 Hevesy——三段式演变勿混 |
| 铪的预言归属 | 通行说法是依据 Bohr 原子模型寻 72 号元素；但 Mansel Davies 与 Eric Scerri 主张「72 号为过渡元素」的预言应归化学家 Charles Bury——**两说并存**，勿写成定论 |
| 铪命名 | 拉丁名 Hafnia = 哥本哈根（Bohr 的家乡）——勿写 "Hafnia 是哥本哈根古称之外的含义" |
| 共同发现者 | 铪是与 **Dirk Coster** 共同发现——勿只写海维西一人 |
| 死亡地 | 1966-07-05 逝于**弗莱堡**（西德），享年 80；安葬：初葬弗莱堡，**2001 年迁葬布达佩斯 Kerepesi 墓园**——两步勿混 |
| 王水溶金 | 对象是 **Laue 与 Franck** 的金质诺奖奖章；地点是哥本哈根 Bohr 研究所实验室；战后由诺贝尔学会**重铸**归还——勿写 "奖章藏在地窖/夹墙" 或 "自己重铸" |
| 名言红线 | Copley 名言整句页面明载（"Forty or fifty have received Nobel chemistry prizes..."）可引；其余无原文一律改间接转述 |
| von Euler-Chelpin | 他是**德裔瑞典教授、1929 诺奖得主**，战时亲德但与海维西持续合作——人物评价按页面如实，勿加戏 |
| 阿伦尼乌斯关系 | 只是**其女 Eugenie 嫁给阿伦尼乌斯之孙**——姻亲后辈关系，非本人直接关系，不入库 |
| 学生口径 | infobox Doctoral students 仅 **Rolf Hosemann、Johann Böhm** 两人，另有 Erika Cremer（postdoc）——metadata 另列 Maximilian Pahl 无正文载，**不予入库** |
| 博士导师口径 | 正文/infobox 只载 **Georg Franz Julius Meyer**；metadata 另列 Franz Himstedt 无正文载，**不予入库** |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76951 | ✅ |
| name_zh | 乔治·德海韦西 | ✅ |
| name_en | George de Hevesy（复用库内 #2132 记录形式） | ✅ |
| birth_date | 1885-08-01 | ✅ |
| death_date | 1966-07-05 | ✅ |
| nationality | Hungary（主）+ Germany / Sweden（居留与公民身份） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：radiochemistry / radioactive tracers / nuclear chemistry，带 rank） | ✅ |
| has_biography | false（Beamer 立传完成后由主控置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 东家 / 合作者**（仅收 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Georg Meyer | 师→生（博士导师） | 1906 年弗莱堡开始博士论文，1908 获物理学博士 |
| advisor-student | Fritz Haber | 师→生（infobox other academic advisors） | 1908 年起在卡尔斯鲁厄随 Haber 工作 |
| advisor-student | Ernest Rutherford | 师→生（infobox other academic advisors） | 曼彻斯特随 Rutherford 工作，结识 Niels Bohr |
| colleague | Niels Bohr | 无向 | 曼彻斯特结识；1920 起定居哥本哈根 Bohr 研究所 |
| colleague | Dirk Coster | 无向 | 1922 年共同发现铪 |
| colleague | Hans von Euler-Chelpin | 无向 | 斯德哥尔摩接待者，战时战后合作多篇论文 |
| spouse | Pia Riis | 无向 | 1924 年结婚，一子三女 |
| advisor-student | Rolf Hosemann | Hevesy → 学生 | infobox Doctoral students |
| advisor-student | Johann Böhm | Hevesy → 学生 | infobox Doctoral students（化学家 Johann Böhm，注意同名消歧义） |
| advisor-student | Erika Cremer | Hevesy → 学生 | infobox other notable students（postdoc） |

> **禁入库名单**（metadata.json / frontmatter 有、page.md 正文与 infobox 无）：Maximilian (Max) Karl Franz Pahl（metadata doctoral_student）、Franz Himstedt（metadata doctoral_advisor）。Svante Arrhenius 仅为姻亲后辈联结（其女嫁 Arrhenius 之孙），非本人直接关系，不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1943，独享；1944-12-12 诺奖演讲 *Some Applications of Isotopic Indicators*）
- Copley Medal（1949；自称尤为自豪——外国会员仅十人、获 Copley 者仅二，另一人是 Bohr）
- Faraday Lectureship Prize（1950）
- Atoms for Peace Award（1958，表彰放射性同位素的和平利用）
- Niels Bohr International Gold Medal（1961）
- Foreign Member of the Royal Society；Baly Medal；Pour le Mérite for Sciences and Arts

## 9. 机构清单

- 教育：Piarist Gymnasium of Budapest（–1903）→ University of Budapest（一年）→ Technische Universität Berlin（数月）→ University of Freiburg（1908 物理学博士）
- 任职：ETH Zürich（1908 受邀）→ 卡尔斯鲁厄（随 Haber）→ 曼彻斯特（随 Rutherford）→ 布达佩斯大学物理化学教授（1918）→ 哥本哈根 Bohr 研究所（1920–；1922 发现铪）→ 弗莱堡大学物理化学教授（1924）→ 康奈尔大学 Baker Lecturer（1930）→ 哥本哈根 Bohr 研究所（1934–1943）→ 斯德哥尔摩有机化学研究所同事 / 斯德哥尔摩大学（1943–1961，退休后仍任科学同事）
- 荣誉教职：根特大学 Franqui Professor（1949）
- 命名机构：Hevesy Laboratory（2005-05-10，丹麦 Risø 国家实验室，今 DTU Nutech）

## 10. 终审清单

- [ ] 生卒 1885-08-01 / 1966-07-05，享年 80，出生地布达佩斯、去世地弗莱堡、2001 迁葬 Kerepesi
- [ ] 1908 博士为**物理学**博士；博士导师 Georg Franz Julius Meyer
- [ ] 1922 铪 = 与 Dirk Coster 共同发现；命名 Hafnia=哥本哈根；预言归属两说并存
- [ ] 1923 首篇示踪论文（^{212}Pb / 蚕豆）；1936 中子活化分析
- [ ] 王水溶金：Laue + Franck 奖章、Bohr 研究所、战后重铸归还
- [ ] 1943 诺奖独享，理由用页面口径原句；1944-12-12 演讲标题如实
- [ ] Copley 名言整句页面明载方可引用；其余一律间接转述
- [ ] 引语全部可在本地 Wikipedia 原文找到；无原文不造引语
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/George_de_Hevesy/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 images.txt 装载（c. 1913 实照优先；404 则装饰圆占位并如实标注）
- [ ] **国籍**：封面顶部明示匈牙利
- [ ] **引语核对**：Copley 名言须在 Wikipedia 原文找到；其余不得出现引号内"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐
