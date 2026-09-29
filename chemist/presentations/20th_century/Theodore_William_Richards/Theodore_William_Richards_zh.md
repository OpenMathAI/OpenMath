# Theodore William Richards（西奥多·威廉·理查兹）立传提示词

> qid=Q189465 · 1868-01-31 – 1928-04-02 · 美国物理化学家 · 20 世纪 · 诺贝尔化学奖（1914，独享；美国首位化学诺奖得主）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Theodore_William_Richards/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取本地 images/ 目录 1914 年照；404 则用装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{balance-scale}\enspace 原子量的丈量者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地（Germantown, Philadelphia）/去世地（Cambridge, Massachusetts）、教育（Haverford College / Harvard University）、博士导师（Josiah Parsons Cooke）、核心领域（物理化学 / 原子量测定）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「原子量 / 天平与结晶」母题——离散圆点暗示他反复重结晶提纯的盐粒与原子量数值点。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），"15,000 次重结晶提纯铥" 与铅原子量双值是天然具象化素材。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Theodore William Richards（中文惯称：西奥多·威廉·理查兹）
- **生卒**：1868-01-31 生于美国宾夕法尼亚州费城 Germantown → 1928-04-02 逝于马萨诸塞州 Cambridge，享年 60；据其一位后人所述，长期受"慢性呼吸系统疾病与长期抑郁"困扰
- **国籍**：United States（美国）
- **身份**：物理化学家（美国首位诺贝尔化学奖得主）
- **家庭**：父 William Trost Richards 为风景与海景画家，母 Anna Matlack Richards 为诗人——他学前教育大部分来自母亲；1896 娶 Miriam Stuart Thayer；一女 Grace Thayer（嫁 James Bryant Conant）、两子 Greenough Thayer 与 William Theodore（两子均死于自杀）
- **宗教**：贵格会（Quaker）
- **教育轨迹**：1878–1880 随家旅欧（多居英国），科学兴趣日浓 → 1883（14 岁）入 Haverford College，1885 获理学学士 → 1886 获 Harvard 文学学士（作为研究生预备）→ 留哈佛攻博，博士论文题为氧相对氢的原子量测定
- **导师**：Josiah Parsons Cooke（博士导师；童年新港度假时曾以小望远镜为他指认土星光环，后来同在 Cooke 实验室工作）
- **博士**：Harvard University（氧相对氢原子量测定；页面未载具体年份，禁写）
- **博士后**：德国一年，在 University of Göttingen 随 Victor Meyer 等研究
- **研究领域**：物理化学——原子量测定、热化学、电化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **画家与诗人之家（1868）**：费城 Germantown 出身艺术家庭，母亲承担其大部分学前与中学前教育。
2. **土星光环（约 1870 年代）**：新港度假偶遇哈佛教授 Josiah Parsons Cooke，小望远镜里的土星光环——日后师承的种子。
3. **少年大学生（1883）**：14 岁入 Haverford College，两年后（1885）获 BS；再入 Harvard 取 BA（1886）。
4. **博士课题（1886 起）**：以"氧相对氢的原子量测定"为博士论文主题，师从 Cooke——原子量研究自此持续到去世（1886–1928，约一半的科研工作）。
5. **哥廷根博士后（1889 前后）**：随 Victor Meyer 在 Göttingen 及其他机构研修一年后返哈佛。
6. **哈佛阶梯（1889–1903）**：助理 → 讲师 → 助理教授 → 1901 正教授；1903 任哈佛化学系主任；1912 任 Erving 化学教授兼新建 Wolcott Gibbs Memorial Laboratory 主任。
7. **婉拒哥廷根（1901）**：成为极少数被欧洲名校聘为正教授的美国科学家之一，选择留在美国。
8. **误差猎手**：发现原子量测定的潜在误差源——某些盐沉淀时会包藏气体或外来溶质；为测铥的原子量做了 **15,000 次**溴酸铥重结晶以获取纯铥（Emsley 记载）。
9. **同位素的化学前兆**：第一个用化学分析证明**同一元素可有不同原子量**——受托分析天然铅与放射性衰变铅，两者原子量不同，支持同位素概念。
10. **量热与电化学**：研究原子压缩度、溶解热与中和热、汞齐电化学；其低温电化学电位研究与他人工作共同导向 Nernst 热定理与热力学第三定律——其间他与 Nernst 有激烈争论。
11. **仪器发明**：绝热量热计（adiabatic calorimeter）与浊度计（nephelometer，为锶原子量工作而设计）。
12. **1914 诺贝尔化学奖（独享）**："in recognition of his exact determinations of the atomic weights of a large number of the chemical elements"——美国首位诺贝尔化学奖得主；据 Forbes，到 1932 年 Richards 及其学生已研究过 55 种元素的原子量。
13. **学会领袖与学生**：美国化学会会长（1914）、AAAS 会长（1917）、美国艺术与科学院院长（1919–1921）；博士生含 Gilbert N. Lewis、James B. Conant（后为哈佛校长）、Farrington Daniels 等；1932 年起 ACS 东北分会设 Theodore Richards Medal（Dallin 设计塑模）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海青 deep teal） | `#0F4C5C` | 天平刻度的精密与计量化学的克制（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（原子量 badgeAtom） | `#2E5A9E` | 蓝 55 种元素原子量测定 |
| 分类色 2（同位素先兆 badgeIso） | `#1B7A43` | 绿双铅原子量 / 同位素支持 |
| 分类色 3（热化学与电化学 badgeThermo） | `#D97B29` | 琥珀量热 / 低温电位 |
| 分类色 4（师承网络 badgeTree） | `#C0395B` | 玫瑰 Cooke 师承 / Lewis、Conant 门生 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「原子量 / 重结晶盐粒」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（清单指定 `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`）
- **风格**：苏醒 / 上行 / 奠基感
- **匹配理由**：
  - "Awaken" 匹配其贡献本质——为整个元素周期表重新"称重"，让化学计量从粗估走向精确
  - "苏醒" 匹配其历史定位——美国化学诺奖第一人，标志美国化学在世界舞台的觉醒
  - "奠基" 匹配叙事结构——师承 Cooke → 哥廷根研修 → 55 种元素 → 1914 诺奖 → 门生 Lewis/Conant 开枝散叶
- **时长对齐**：以曲目实际时长 > 15 页 × 7 秒为宜，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 原子量的丈量者 / Theodore W. Richards 1868–1928 + 四色 badge + 右上头像 + 国籍行（美国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  理查兹的一生 — 高斯式时间线（10 节点：1868→1883→1886→1889→1901→1903→1912→1913→1914→1928）
04  画家之子与少年大学生 (1868–1886) — 表格「时间|事件|结果」
05  哈佛与哥廷根 (1886–1901) — 表格「时间|事件|结果」
06  原子量测定 (1886–1928) — 表格「问题|方法|结果」+ 公式框：55 种元素 · 15,000 次重结晶
07  误差猎手 — 表格「误差源|对策|结果」+ 公式框：盐包藏气体/溶质 → 提纯
08  双铅与同位素先兆 — 表格「样品|测量|结论」+ 公式框：天然铅 ≠ 放射性铅
09  热化学与电化学 — 表格「课题|方法|意义」+ 公式框：低温电位 → Nernst 热定理 / 第三定律（含争论注）
10  1914 诺贝尔化学奖 — 表格「得主|理由|史实」+ 公式框：官方理由原文 · 美国首位化学诺奖
11  门生与传承 — 表格「人物|方向|结果」（Lewis / Daniels / Dole / Smyth / Willard / Conant）
12  荣誉 — 高斯式「类别|代表|意义」表格（Davy 1910 / Faraday 1911 / Gibbs 1912 / Franklin 1916 / FRS 1919）
13  遗产：计量化学的基准 — 四分类遗产盒 + 公式框：Richards Medal 1932（Dallin 设计）
14  结尾 — 「他一生都在称量原子，也把美国化学称进了世界。」（无出处意境句）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1914 独享 | **独享**（页面无共同得主）；官方理由 "in recognition of his exact determinations of the atomic weights of a large number of the chemical elements"——引文照录 |
| "第一"断言 | 页面明载可写：美国首位诺贝尔化学奖得主；"one of the first American scientists ever offered a full professorship in a major European university"——注意是"极少数/最早一批之一"而非"第一个"；其余"第一次/唯一"禁写 |
| 博士年份 | 页面未载博士学位授予年份——**禁写**；Haverford BS 1885 / Harvard BA 1886 有载 |
| 获奖理由指向 | 理由是"精确测定大量化学元素的原子量"——**不是**热化学或电化学；勿混 |
| 同位素表述 | 他只是"以化学分析支持同位素概念"（first to show an element could have different atomic weights）——勿写"发现同位素" |
| 与 Nernst 争论 | 低温电位工作"in the hands of others"导向热定理与第三定律，其间有 heated debate——如实写"争论"，勿写成合作或从属 |
| 两子自杀 | 页面明载"both sons died by suicide"——**一句话中性记载或不写**，禁展开细节、禁心理揣测 |
| 死因口径 | 逝于 Cambridge, Massachusetts，60 岁；"chronic respiratory problems and a prolonged depression"是**其后人所述**（据传），须带"据其后人所述"限定 |
| 师承两人 | Cooke（博士导师）与 Victor Meyer（哥廷根博士后随其研究）都 page 明载——两行分立，Meyer 注明"博士后研修"非正式博士导师 |
| Conant 双重身份 | James Bryant Conant 既是其博士生（infobox）又是女婿（女儿 Grace 之夫）——两重关系都 page 明载，note 分写 |
| Richards Medal | Theodore Richards Medal 1932 **追授**首颁（奖章 1928 年设立，Dallin 设计）——勿写他生前获奖 |
| 同名区分 | 与 Robert Coleman Richardson（1996 物理诺奖）无关；与画家父亲 William Trost Richards 区分 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q189465 | ✅ |
| name_zh | 西奥多·威廉·理查兹 | ✅ |
| name_en | Theodore William Richards | ✅（清单 db_id 为空，按 page.md 规范名新建） |
| birth_date | 1868-01-31 | ✅ |
| death_date | 1928-04-02 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：physical chemistry / atomic weights / thermochemistry / electrochemistry，带 rank） | ✅ |

## 7. 社会关系入库清单

**师长 / 门生 / 家人**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Josiah Parsons Cooke | 师→生（博士导师） | 博士论文为氧相对氢原子量测定；童年新港望远镜之缘 |
| advisor-student | Victor Meyer | 师→生（博士后研修） | 哥廷根大学博士后随其研究一年 |
| advisor-student | Gilbert N. Lewis | Richards→学生 | 博士生（infobox） |
| advisor-student | Farrington Daniels | Richards→学生 | 博士生（infobox） |
| advisor-student | Malcolm Dole | Richards→学生 | 博士生（infobox） |
| advisor-student | Charles Phelps Smyth | Richards→学生 | 博士生（infobox） |
| advisor-student | Hobart Hurd Willard | Richards→学生 | 博士生（infobox） |
| advisor-student | James B. Conant | Richards→学生 | 博士生（infobox）；后娶其女 Grace |
| competitor | Walther Nernst | 无向 | 低温电化学电位之争，关联热定理与第三定律（heated debate） |
| spouse | Miriam Stuart Thayer | 无向 | 1896 成婚（infobox/正文） |
| parent-child | William Trost Richards | 家长→子女 | 其父，风景与海景画家 |
| parent-child | Anna Matlack Richards | 家长→子女 | 其母，诗人，承担其大部分学前教育 |
| parent-child | Grace Thayer | 家长→子女 | 其女，嫁 James Bryant Conant |
| parent-child | Greenough Thayer | 家长→子女 | 其子（一句话中性记载） |
| parent-child | William Theodore | 家长→子女 | 其子（一句话中性记载） |

> 禁入库名单：Cyrus Dallin（奖章设计者，雕塑家友人，非学术关系）；Forbes / Emsley（文献作者）；Berzelius、Stas、Daniels 等 See-also 条目仅为导航链接。Nernst 关系类型取 competitor（页面明载 heated debate；非合作非师承）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1914，独享；官方理由 "in recognition of his exact determinations of the atomic weights of a large number of the chemical elements"）
- American Philosophical Society member（1902）
- Lowell Lectures（1908）
- Davy Medal（1910）
- Faraday Lectureship（1911）
- Willard Gibbs Award（1912）
- Franklin Medal（1916）
- Honorary Member of the Royal Irish Academy（1918）
- Foreign Member of the Royal Society of London（1919）
- Lavoisier Medal（1922）；Le Blanc Medal（1922）
- Honorary Fellow of the Royal Society of Edinburgh（1923）
- Member of the International Atomic Weights Committee
- Theodore Richards Medal（1932 首颁；奖章 1928 设立，Cyrus Dallin 设计——ACS 东北分会，两年一届）
- 诺贝尔演讲：1919-12-06《Atomic Weights》（注：1914 年奖，演讲因一战延至 1919——页面 External links 载 1919-12-06，勿写成 1914 演讲）

## 9. 机构清单

- 教育：Haverford College（1883–1885，BS）；Harvard University（1886 BA；博士，师从 Cooke）
- 博士后：University of Göttingen（Victor Meyer 实验室，一年）
- 任职：Harvard University——化学助理 → 讲师 → 助理教授 → 正教授（1901）；化学系主任（1903）；Erving 化学教授兼 Wolcott Gibbs Memorial Laboratory 主任（1912）
- 拒聘：University of Göttingen 正教授聘约（1901，婉拒留美）
- 学会职务：美国化学会会长（1914）；AAAS 会长（1917）；美国艺术与科学院院长（1919–1921）

## 10. 终审清单

- [ ] 生卒 1868-01-31 / 1928-04-02，享年 60，出生地 Germantown（费城）、去世地 Cambridge（马萨诸塞）
- [ ] 1914 独享表述准确；官方理由引文逐字核对；美国首位化学诺奖口径准确
- [ ] 博士年份禁写；Haverford 1885 BS / Harvard 1886 BA 年份准确
- [ ] 15,000 次重结晶 / 55 种元素（1932，Forbes）/ 双铅同位素支持表述准确
- [ ] Nernst 争论（competitor）与"in the hands of others"归因表述准确
- [ ] Conant 学生 + 女婿双重关系 note 分写；两子自杀一句话中性处理
- [ ] 哥廷根 1901 拒聘为"最早一批之一"而非"第一个"
- [ ] 无引语杜撰（全文页面无直接引语，死后后人转述带限定）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Theodore_William_Richards/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（1914 照）；404 用装饰圆占位并注明
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：仅官方获奖理由为可引原文；其余全部间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾；本文件由 chem-batch-01 agent 维护。
> **最重要的事：每写一页就 make，看到溢出就修。**
