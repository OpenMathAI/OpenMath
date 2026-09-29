# James B. Sumner（詹姆斯·B·萨姆纳）立传提示词

> qid=Q106756 · 1887-11-19 – 1955-08-12 · 美国生物化学家 · 20 世纪 · 诺贝尔化学奖（1946，与 Northrop/Stanley 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/James_B._Sumner/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考化学家桑格立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 images.txt 优先用 1946 年照；404 则装饰圆占位，图注如实标注）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 第一个让酶结晶的人\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育（Harvard）、博士（1914，Otto Folin 门下）、独臂往事、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「酶结晶析出」母题——离散圆点暗示丙酮冷却后缓缓析出的尿素酶晶簇。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如「尿素酶提纯 + 丙酮 + 冷却 → 结晶」流程具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：James Batcheller Sumner（中文惯称：詹姆斯·B·萨姆纳 / 萨姆纳；infobox 姓名 James B. Sumner）
- **生卒**：1887-11-19 生于马萨诸塞州 Canton → 1955-08-12 逝于纽约州布法罗（癌症），享年 67
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist；1946 年诺贝尔化学奖得主之一；**首个把酶以结晶态分离、并证明酶是蛋白质**的人）
- **家庭**：1915-07-10 娶 Cid Ricketts（本名 Bertha Louise Ricketts，密西西比 Brookhaven 人，当时在康奈尔读医学院），育四子女；1930 年离婚（她保留夫姓，后成为作家，代表作 *Tammy Tell Me True*、*Quality*；1970 年被外孙 John R. Cutler 谋杀——页面明载，如使用须克制）。1931 年娶 Agnes Lundkvist，1943 年离婚；同年娶 Mary Beyer，育两子女
- **独臂往事（1904）**：17 岁打猎时被同伴误伤，左臂肘下截肢；原本惯用左手，此后一切改用右手
- **教育轨迹**：
  - Roxbury Latin School（metadata）→ 1910 年获哈佛大学学士学位（同窗结识 Roger Adams、Farrington Daniels、Frank C. Whitmore、James Bryant Conant、Charles Loring Jackson 等化学名家）
  - 毕业后在舅舅的棉针织厂短暂工作 → 加拿大 Mount Allison University 任教 → 1911–12 年在伍斯特理工学院任化学助教
- **导师**：Otto Folin（博士导师）
- **博士**：1914，哈佛医学院（Harvard Medical School），生物化学方向
- **研究领域**：生物化学、酶学（urease / catalase 结晶；infobox Fields: Biochemistry）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **独臂少年（1904）**：17 岁打猎被同伴误伤，左臂肘下截肢——用一只右手后来做出了让酶结晶的精细活。
2. **哈佛本科（1910）**：结识 Roger Adams、James Bryant Conant 等一代化学名家。
3. **辗转教职（1910–1912）**：棉针织厂 → 加拿大 Mount Allison 大学 → 伍斯特理工学院助教——坚持转向生物化学。
4. **Folin 门下博士（1912–1914）**：入哈佛医学院学生物化学，1914 年获博士学位；随后任康奈尔医学院生物化学助理教授。
5. **1917 年立下目标**：在康奈尔开始「把酶以纯态分离」的研究——此前从未有人做到。
6. **尿素酶（urease）攻坚战（1917–1926）**：选刀豆（jack bean）尿素酶为对象；多年失败，同行多认为不可能；1926 年终于把纯化尿素酶与丙酮混合、冷却后**析出结晶**。
7. **酶=蛋白质（1926）**：化学检验证明纯尿素酶是蛋白质——**第一个酶是蛋白质的实验证明**，终结当时争议。
8. **正教授与 Stocking Hall（1924–1929）**：1924 年起实验室设在康奈尔新乳品科学楼 Stocking Hall 二层（今食品科学楼）——正是他日后获诺奖研究的所在；1929 年升正教授。
9. **第二个结晶酶：过氧化氢酶（1937）**：成功分离并结晶 catalase——证明酶结晶是**普适方法**。
10. **北欧访学与 Scheele 奖（1937）**：获 Guggenheim Fellowship，在瑞典随 **Theodor Svedberg** 工作 5 个月；同年获斯德哥尔摩 Scheele Award。
11. **Northrop 印证（1929–）**：洛克菲勒研究所的 John Howard Northrop 以同类方法于 1929 年结晶胃蛋白酶——两人的工作互为印证，「酶皆蛋白质」渐成定论。
12. **1946 诺贝尔化学奖（三人共享）**：与 John Howard Northrop、Wendell Meredith Stanley 共享——页面叙述口径 "for crystallization of enzymes"（Sumner 页面未载官方 citation 整句，**勿杜撰**）；1946-12-12 诺奖演讲 *The Chemical Nature of Enzymes*；1947 年出任康奈尔酶化学实验室主任。
13. **身后（1948–1955）**：1948 年当选美国国家科学院院士、1949 年当选美国艺术与科学院 Fellow；1955-08-12 因癌症逝于布法罗，享年 67；Dounce 在《Nature》为其撰写讣告。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫紫罗兰 purple） | `#52307C` | 结晶之美的沉静与酶学攻坚的坚韧（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签；亦呼应酶晶体的折光） |
| 分类色 1（尿素酶结晶 badgeUrease） | `#1B7A43` | 绿 1926 结晶 / 刀豆尿素酶 |
| 分类色 2（酶=蛋白质 badgeProtein） | `#2E5A9E` | 蓝化学检验证明 / 序列时代的先声 |
| 分类色 3（过氧化氢酶 badgeCatalase） | `#D97B29` | 琥珀 1937 第二个结晶酶 / 普适方法 |
| 分类色 4（共同得主 badgeCoLaureate） | `#C0395B` | 玫瑰 Northrop / Stanley 三人共享 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「冷却的丙酮溶液中缓缓析出的酶晶体」——从浑浊到清亮的过程感。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（文件 `35-jqIDnltiDRI-The-Flow-of-Time.wav`；不要复制 wav 到本目录，Makefile 由主控预置）
- **风格**：时间之流 / 沉稳绵长 / 坚韧的长期主义
- **匹配理由**：
  - "时间之流" 匹配九年攻坚（1917→1926）——不被看好的漫长等待里，结晶在低温中一寸寸析出
  - "坚韧" 匹配独臂科学家的一生——失去左臂后用右手重学一切，再到改写酶学
  - "沉稳绵长" 匹配其晚年——诺奖之后仍守着康奈尔的酶化学实验室直到生命最后一年
- **时长**：以曲目实际时长为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 第一个让酶结晶的人 / James B. Sumner 1887–1955 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士/师承/出生地/去世地/独臂往事/领域/荣誉）
03  萨姆纳的一生 — 高斯式时间线（10 节点：1887→1904→1910→1914→1917→1926→1937→1946→1948→1955）
04  早年：独臂与哈佛 (1887–1912) — 表格「时间|事件|结果」
05  Folin 门下与康奈尔 (1912–1917) — 表格「阶段|内容|结果」
06  尿素酶结晶 (1917–1926) — 表格「问题|方法|结果」+ 公式框：尿素酶提纯 + 丙酮 + 冷却 → 结晶
07  酶是蛋白质 (1926) — 表格「争议|证据|结论」+ 公式框：酶 = 蛋白质（首个实验证明）
08  过氧化氢酶与普适方法 (1929–1937) — 表格「对象|方法|结果」（Northrop 胃蛋白酶 1929 互证）
09  北欧访学 (1937) — 表格「资助|东家|荣誉」（Guggenheim / Svedberg / Scheele Award）
10  1946 诺贝尔化学奖 — 表格「人物|方向|结果」（三人共享，页面叙述口径；1946-12-12 演讲标题）
11  荣誉与晚年 — 高斯式「类别|代表|意义」表格（NAS 1948 / AAAS Fellow 1949 / 康奈尔酶化学实验室主任 1947）
12  遗产：结晶酶开启的结构生物学 — 高斯式流程图（1926 结晶 → 酶=蛋白质 → 蛋白质晶体学时代）
13  遗产：一只右手改写酶学 — 四分类遗产盒 + 公式框：1917→1926 九年攻坚
14  结尾 — 「结晶那一刻，酶第一次以真面目示人。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1946 诺奖理由 | 页面叙述口径 "for crystallization of enzymes"（Sumner 页面未载官方 citation 整句，**勿杜撰官方原句**）；**三人共享**：Sumner + John Howard Northrop + Wendell Meredith Stanley——勿写共享两人或独享 |
| 分工表述 | Sumner：结晶尿素酶 + 证明酶是蛋白质；Northrop：同类方法结晶胃蛋白酶等；Stanley：结晶病毒（详情以其本人篇为准）——三人贡献勿互相混写 |
| 首创归属 | "First to isolate an enzyme in crystallized form" 与 "First to show that an enzyme is a protein" 均为 infobox 明载——两项首创**属于 Sumner**，Northrop 是方法互证 |
| 独臂往事 | 17 岁打猎**被同伴误伤**、左臂肘下截肢、由左撇子改右手——细节按页面，勿写成「事故」一笔带过或渲染悲情 |
| 截肢年份 | 页面仅载 "While hunting at age 17"（1887+17≈1904/05）——写「17 岁时」即可，勿编造确切日期 |
| 博士时间线 | 1912 入哈佛医学院学**生物化学**、1914 获博士（Otto Folin 门下）——勿写成哈佛大学文理学院 |
| Cid Ricketts 结局 | 1930 离婚后成为作家，1970 年被**外孙** John R. Cutler 谋杀——页面明载但较阴暗，如使用仅一句客观带过 |
| 婚姻次数 | 三段婚姻（Cid Ricketts 1915/1930 离；Agnes Lundkvist 1931/1943 离；Mary Beyer 1943–）——勿漏第三段 |
| Svedberg 关系 | 1937 年 Guggenheim 访学 5 个月的**接待东家**（随其工作）——师承勿升格 |
| 引用红线 | 全篇页面无直接引语——一律间接转述，**不得出现引号内"原话"**（演讲标题、职位等可原样呈现） |
| 学生口径 | infobox Doctoral students 仅 **Alexander Dounce**（其 Nature 讣告作者）；metadata 另列 Theodore Sourkes 无正文载，**不予入库** |
| 去世地 | 1955-08-12 逝于**布法罗**（Buffalo, NY），癌症，享年 67——勿与出生地 Canton 混淆 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q106756 | ✅ |
| name_zh | 詹姆斯·B·萨姆纳 | ✅ |
| name_en | James B. Sumner（新建记录；页面标题/manifest 形式，全名 James Batcheller Sumner） | ✅ |
| birth_date | 1887-11-19 | ✅ |
| death_date | 1955-08-12 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：enzymology / biochemistry / protein crystallization，带 rank） | ✅ |
| has_biography | false（Beamer 立传完成后由主控置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 学生 / 访学东家 / 共同得主**（仅收 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Otto Folin | 师→生（博士导师） | 1914 年哈佛医学院生物化学博士 |
| advisor-student | Alexander Dounce | Sumner → 学生 | infobox Doctoral students；1955 年为其撰 Nature 讣告 |
| colleague | Theodor Svedberg | 无向 | 1937 年 Guggenheim Fellowship 赴瑞典随其工作 5 个月 |
| co-honored | John Howard Northrop | 无向 | 1946 年诺贝尔化学奖共同得主 |
| co-honored | Wendell Meredith Stanley | 无向 | 1946 年诺贝尔化学奖共同得主 |

> **禁入库名单**：Theodore Sourkes（metadata doctoral_student，正文与 infobox 无）。Harvard 同窗 Roger Adams、Farrington Daniels、Frank C. Whitmore、James Bryant Conant、Charles Loring Jackson 仅为 "acquainted"（结识），无实质合作，**不入库**。

## 8. 奖项清单

- Nobel Prize in Chemistry（1946，与 Northrop / Stanley 共享；1946-12-12 诺奖演讲 *The Chemical Nature of Enzymes*）
- Scheele Award（1937，斯德哥尔摩）
- Guggenheim Fellowship（1937）
- Member of the National Academy of Sciences（1948）
- Fellow of the American Academy of Arts and Sciences（1949）

## 9. 机构清单

- 教育：Roxbury Latin School → Harvard University（BA 1910）→ Harvard Medical School（1912 入；PhD 1914，Otto Folin 门下）
- 任职：舅舅的棉针织厂（短暂）→ Mount Allison University（加拿大 Sackville, New Brunswick，任教）→ Worcester Polytechnic Institute（1911–12 化学助教）→ Cornell Medical School 生物化学助理教授（1914–）→ 康奈尔大学（1917 起酶研究；1924 起实验室设于 Stocking Hall 二层；1929 正教授；1947 酶化学实验室主任）
- 院士：National Academy of Sciences（1948）；American Academy of Arts and Sciences（1949）

## 10. 终审清单

- [ ] 生卒 1887-11-19 / 1955-08-12，享年 67，出生地 Canton、去世地布法罗
- [ ] 独臂往事表述准确（17 岁、同伴误伤、肘下截肢、改右手）
- [ ] 1926 尿素酶结晶 + 酶=蛋白质双首创；1937 过氧化氢酶
- [ ] 1946 三人共享（Northrop、Stanley），理由用页面叙述口径，勿编官方 citation
- [ ] 博士：1914、Folin 门下、生物化学
- [ ] 全篇无直接引语——不得出现引号内"原话"
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/James_B._Sumner/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 images.txt 装载（1946 年照优先；404 则装饰圆占位并如实标注）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：全篇不得出现引号内"原话"（页面无直接引语）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐
