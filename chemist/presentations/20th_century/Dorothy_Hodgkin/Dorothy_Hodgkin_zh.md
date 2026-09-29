# Dorothy Hodgkin（多萝西·霍奇金）立传提示词

> qid=Q7487 · 1910-05-12 – 1994-07-29 · 英国化学家 · 20 世纪 · 诺贝尔化学奖（1964，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Dorothy_Hodgkin/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 `images.txt` / REST API 下载；404 则装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{eye}\enspace 看见不可见分子的女人\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Dorothy Mary Crowfoot Hodgkin）、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「电子密度图」母题——等高线状的圆点群暗示 X 射线晶体学的电子密度等值线。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），分子式/结构数据即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Dorothy Mary Crowfoot Hodgkin（本姓 Crowfoot；中文惯称：多萝西·霍奇金；OM FRS HonFRSC）
- **生卒**：1910-05-12 生于埃及开罗 → 1994-07-29 逝于英格兰沃里克郡 Ilmington，享年 84
- **国籍**：United Kingdom（英国）
- **身份**：化学家（推进 X 射线晶体学测定生物分子结构，结构生物学的奠基人之一）
- **家庭**：John Winter Crowfoot（1873–1959，埃及教育部任职、后任考古学家）与 Grace Mary Crowfoot（娘家姓 Hood，1877–1957，植物学家，昵称 Molly）四女中之长女；童年与父母聚少离多；1937 年嫁 Thomas Lionel Hodgkin（历史学家，非洲政治研究者，1982-03-25 卒于希腊），子女 Luke（1938–2020，数学教师）、Elizabeth（1941，历史学家）、Toby（1946，植物学/农学）
- **教育轨迹**：
  - Sir John Leman Grammar School（Beccles；仅有的两名可修化学的女生之一；校长 George Watson 为她补习拉丁文以通过牛津入学考试）
  - Somerville College, Oxford（1928 入学读化学，1932 一等荣誉——该学院史上第三位）
  - Newnham College, Cambridge（博士，师从 J. D. Bernal；1937 获 PhD，论文为 X 射线晶体学与甾醇化学）
- **导师**：John Desmond Bernal（她终身称其 "Sage"；科学、政治与个人层面都深刻影响她）
- **疾病**：1934 年（24 岁）确诊类风湿关节炎，双手逐渐变形，晚年大部分时间坐轮椅——仍坚持科研
- **研究领域**：X 射线晶体学、生物化学——青霉素、维生素 B12、胰岛素结构

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **开罗出生的考古学家之女（1910）**：父母在北非/中东的殖民教育与考古工作；童年大部分与祖父母在英格兰度过；10 岁起对晶体的兴趣由母亲远程鼓励。
2. **16 岁的生日礼物（1926 前后）**：母亲送 W. H. Bragg 的《Concerning the Nature of Things》——帮助她决定未来方向。
3. **耶累什的镶嵌画（1928）**：随父母在约旦 Jerash 遗址记录拜占庭教堂马赛克图案并做玻璃镶嵌块化学分析——精密制图习惯与日后化学中的模式识别一脉相承。
4. **Somerville 第三位一等荣誉（1932）**：牛津 Somerville 学院化学一等荣誉，该院史上第三位。
5. **Bernal 与胃蛋白酶（1932–1937）**：剑桥 Newnham；参与 X 射线技术首次用于生物物质（胃蛋白酶）的拍摄——霍奇金一贯申明最初照片是 Bernal 拍的、关键洞见他给的；1937 以甾醇研究获 PhD。
6. **重返牛津（1934–1936）**：1933 获 Somerville 研究奖学金，1934 回牛津自带设备开课；1936 成为该学院首位化学 fellow 兼导师，任职至 1977——其学生之一是 Margaret Roberts（后来的撒切尔首相，唐宁街办公室悬挂她的肖像）。
7. **首个甾体结构（1945）**：与 C. H. Carlisle 发表胆甾醇碘化物——第一个三维甾体生物分子结构。
8. **青霉素与 β-内酰胺（1945/1949）**：与 Barbara Low 等解出青霉素结构，证明含 β-内酰胺环（与当时主流科学意见相反）；1949 年才发表。
9. **维生素 B12（1948–1956）**：1948 年初遇 B12（当年 Merck 首次发现）；发现含钴后判断可用 X 射线分析；由多色性推断环结构；Lawrence Bragg 评价其 B12 研究"如同突破音障"；最终结构 1955–1956 发表——**诺奖成果**。
10. **1964 诺贝尔化学奖（独享）**：page.md 明载她成为**第三位获诺贝尔化学奖的女性**，且是**唯一获诺贝尔科学奖的英国女性科学家**（三大科学奖项口径）；当年她和丈夫在加纳听到获奖消息。
11. **胰岛素（1934–1969）**：1934 年 Robert Robinson 给她一小份胰岛素晶体；35 年后（1969）终于与年轻国际团队首次解出胰岛素结构——为胰岛素大规模生产与改造铺路；与北京/上海的胰岛素研究组保持长期交流（中国组 1971 年独立解出结构、分辨率更高）。
12. **和平与裁军（1976–1988）**：帕格沃什会议主席（1976–1988，任期长于前后任）；1987 接受苏联政府列宁和平奖；因政治活动 1953 年起被禁止入境美国。
13. **荣誉与身后**：FRS（1947）、Royal Medal（1956）、OM（1965，第二位获此勋的女性）、Copley Medal（1976，**首位女性**）、Lomonosov 金奖（1982）、小行星 5422 以她命名（1982 年发现）；1996 年英国皇家邮政"成就女性"邮票；2015 年其 1949 年青霉素论文获 ACS Citation for Chemical Breakthrough Award。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深蓝紫 deepindigo） | `#2A3468` | 电子密度图的深邃与坚定（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（维生素 B12 badgeB12） | `#4A3A9E` | 蓝紫钴胺素环结构 / 1955–1956 |
| 分类色 2（青霉素 badgePen） | `#1B7A43` | 绿 β-内酰胺环 / 1945 |
| 分类色 3（胰岛素 badgeIns） | `#B0432A` | 砖红胰岛素 35 年长跑 / 1969 |
| 分类色 4（和平与公共 badgePeace） | `#C0395B` | 玫瑰帕格沃什 / 列宁和平奖 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应电子密度等值线图。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`，不要复制 wav 文件，Makefile 直接引用该路径）
- **风格**：远征 / 宏阔 / 渐进上扬
- **匹配理由**：
  - "远征" 匹配其事业形态——青霉素、B12、胰岛素三场以十年计的结构远征
  - "渐进上扬" 匹配 35 年胰岛素长跑的叙事弧——1934 的晶体到 1969 的解出
  - "宏阔" 匹配她的公共面向——帕格沃什、国际晶体学联合会、对第三世界的关注
- **时长**：对齐 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 看见不可见分子的女人 / Dorothy Hodgkin 1910–1994 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  霍奇金的一生 — 高斯式时间线（10 节点：1910→1928→1932→1934→1937→1945→1948→1964→1969→1994）
04  早年：开罗与晶体 (1910–1928) — 表格「时间|事件|结果」
05  Bernal 与胃蛋白酶 (1932–1937) — 表格「人物|方法|结果」
06  青霉素与 β-内酰胺 (1945–1949) — 表格「问题|方法|结果」+ 公式框：青霉素 β-内酰胺环
07  维生素 B12 (1948–1956) — 表格「挑战|方法|结果」+ 公式框：B12 钴胺素环 · Bragg "突破音障"评价
08  1964 诺贝尔化学奖（独享） — 表格「奖项|口径|意义」+ 公式框：第三位化学诺奖女性 · 唯一英国女性科学诺奖得主
09  胰岛素 35 年长跑 (1934–1969) — 表格「年份|事件|结果」+ 公式框：1969 胰岛素结构解出
10  师承与门生 — 表格「人物|方向|结果」（Bernal/导师；Howard/James 学生；Dunitz/Blundell/Dodson 博士后；Thatcher 本科生）
11  和平与公共事务 (1953–1988) — 表格「年份|事件|结果」（美国禁令/帕格沃什/列宁和平奖）
12  荣誉与纪念 — 高斯式「类别|代表|意义」表格（FRS 1947 / OM 1965 / Copley 1976 首位女性 / 小行星 5422）
13  遗产：结构生物学之父辈的奠基人 — 四分类遗产盒 + 公式框：X 射线晶体学 → 结构生物学
14  结尾 — 「分子在晶体深处开口，她听懂了。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 诺奖官方获奖理由 | **page.md 无官方英文 citation 原文**——禁写 "for her determinations by X-ray techniques..." 等页面外的措辞；按 page.md 口径：1964 诺奖与维生素 B12 结构测定相关（intro 原句 "mapping the structure of vitamin B12, for which in 1964 she became the third woman to win..."） |
| 两个"女性口径" | page.md 明载两条：① 1964 年成为**第三位**获诺贝尔化学奖的女性；② **唯一获诺贝尔科学奖（三大科学奖）的英国女性科学家**——两处都可写，但勿互相混淆或改写成"第二位" |
| 独享 | 1964 为**独享**，无共同得主——禁写共享 |
| Bernal 关系 | Bernal 是博士导师与终身导师（"Sage"）；page.md 亦载两人战前曾是恋人——立传**只取师承与科学合作**口径，私事不展开；其英共党员背景仅作时代背景一句带过或不写 |
| 胃蛋白酶归属 | "pepsin experiment is largely credited to Hodgkin, however she always made it clear that it was Bernal who initially took the photographs"——两句话都要交代，勿独揽 |
| β-内酰胺发现 | 青霉素结构**证实**（contrary to scientific opinion）；β-内酰胺结构最早由 Merck 化学家与 Oxford 的 Edward Abraham 提出（这在 Woodward 篇有交叉注记）——霍奇金是"用晶体学证明正确"，勿写"她提出 β-内酰胺" |
| 胰岛素样品 | 1934 年 Robert Robinson 提供晶体——勿写成她自行获得 |
| 中国合作 | 1959 年首访中国、共 8 次；1971 年中国组独立解出胰岛素结构（晚于但分辨率更高）；1972–1975 任国际晶体学联合会主席期间未能说服中国入会——可写，保持客观 |
| Ceaușescu 序言 | 73 岁为 Elena Ceaușescu 论文英译本作序、1989 年后被揭穿系造假——**敏感事件，建议立传回避**；若必写须严格按 page.md（hoax 揭露）且不渲染 |
| 撒切尔关系 | Margaret Roberts 是 1940 年代她的学生（undergraduate）；霍奇金是终身工党支持者——师生情谊可写，政治分歧不展开 |
| 姓名口径 | 结婚 12 年后（1949 起）才用 "Dorothy Crowfoot Hodgkin"；诺奖奖匣刻 'Crowfoot Hodgkin'；DB 用 Nobel Foundation 口径 "Dorothy Crowfoot Hodgkin"——三种称谓在文中首次出现时说明 |
| 名字混淆 | 与细菌学家/其他 Hodgkin（如 Thomas Hodgkin 淋巴瘤命名者）无关；其夫 Thomas Lionel Hodgkin 是历史学家 |
| metadata 噪声 | metadata.json nationality 含 "United Kingdom of Great Britain and Ireland"（历史国名）——入库用规范国名 United Kingdom |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q7487 | ✅ |
| name_zh | 多萝西·霍奇金 | ✅ |
| name_en | Dorothy Crowfoot Hodgkin（Nobel Foundation 口径，page.md 明载；库内无既有记录） | ✅ |
| birth_date | 1910-05-12 | ✅ |
| death_date | 1994-07-29 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | X-ray crystallography（person_field 细分：X-ray crystallography / biochemistry / protein crystallography / structural biology，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 学生 / 家人 / 同事**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | J. D. Bernal | 师→生（博士导师） | 剑桥 Newnham，1937 PhD；她终身称其 "Sage" |
| advisor-student | Judith Howard | 霍奇金→学生 | infobox 博士生 |
| advisor-student | Michael N. G. James | 霍奇金→学生 | infobox 博士生 |
| advisor-student | Margaret Thatcher | 霍奇金→学生 | 1940 年代本科生（后任英国首相），非博士生 |
| colleague | Jack D. Dunitz | 无向 | 博士后；1953 年同车赴剑桥看 DNA 双螺旋模型 |
| colleague | Tom Blundell | 无向 | 博士后（infobox other notable students） |
| colleague | Guy Dodson | 无向 | 博士后（infobox other notable students） |
| colleague | June Lindsey | 无向 | 博士后（infobox other notable students） |
| colleague | Robert Robinson | 无向 | 1934 年提供胰岛素晶体样品 |
| colleague | Barbara Low | 无向 | 青霉素结构合作者 |
| colleague | C. H. Carlisle | 无向 | 1945 年合作发表首个甾体三维结构（胆甾醇碘化物） |
| spouse | Thomas Lionel Hodgkin | 无向 | 1937 结婚；历史学家；1982-03-25 卒于希腊 |
| parent-child | John Winter Crowfoot | 父 | 1873–1959；教育部官员/考古学家 |
| parent-child | Grace Mary Crowfoot | 母 | 1877–1957；植物学家，昵称 Molly |

> **禁入库名单**（page.md 提及但按红线/惯例不入库）：子女 Luke/Elizabeth/Toby（明载但按批次惯例不入库，防噪声）；Sydney Brenner/Leslie Orgel/Beryl M. Oughton（1953 赴剑桥车程同行，社交事件）；Charles Harington（远亲，荐书一次）；Mary Slessor/Margery Fry（童年偶像，非个人关系）；Hans Thacher Clarke（其秘书建议用夫姓——出版事件）；Elena Ceaușescu（序言事件且系骗局，禁入库）；Lawrence Bragg（引语评价，无个人实质关系）。metadata-only 无新增。

## 8. 奖项清单

- Nobel Prize in Chemistry（1964，独享；第三位化学诺奖女性、唯一英国女性科学诺奖得主）
- Fellow of the Royal Society，FRS（1947）
- Royal Medal（1956）
- Order of Merit，OM（1965；第二位获此勋的女性）
- Iota Sigma Pi National Honorary Member（1966）
- EMBO Membership（1970）
- Copley Medal（1976；首位女性）
- Dalton Medal（1981，曼彻斯特文学与哲学学会）
- Lomonosov Medal（1982，苏联科学院）
- Austrian Decoration for Science and Art（1983）
- Lenin Peace Prize（1987）
- 小行星 (5422) Hodgkin（1982-12-23 发现，以她命名）
- Foreign Honorary Member, American Academy of Arts and Sciences（1958）
- Citation for Chemical Breakthrough Award（2015，授予牛津，表彰 1949 青霉素论文）

## 9. 机构清单

- 教育：Sir John Leman High School（Beccles）、Somerville College, Oxford（1928–1932，BA 一等荣誉）、Newnham College, Cambridge（PhD 1937）
- 任职：Somerville College 首位化学 fellow 兼导师（1936–1977）；Oxford reader（1955）；Royal Society Wolfson Research Professor（1960–1970）；Wolfson College, Oxford fellow（1977–1983）；University of Bristol Chancellor（1970–1988）
- 学术服务：International Union of Crystallography 主席（1972–1975）；Pugwash Conferences 主席（1976–1988）
- 命名机构：Dorothy Crowfoot Hodgkin Building（牛津生化系 2022 更名）；Dorothy Hodgkin Fellowship（皇家学会）；Somerville 的 Dorothy Hodgkin Quarter

## 10. 终审清单

- [x] 生卒 1910-05-12 / 1994-07-29，享年 84，出生地开罗、去世地 Ilmington
- [x] 1964 独享；"第三位化学诺奖女性"与"唯一英国女性科学诺奖得主"两个口径并列准确
- [x] B12 1955–1956 发表；青霉素 1945 解出 1949 发表；胰岛素 1934→1969
- [x] 胃蛋白酶归属双句交代（Bernal 先拍照）；β-内酰胺是"证实"非"提出"
- [x] 姓名三口径（Crowfoot → Crowfoot Hodgkin → Hodgkin）首次出现有说明
- [x] Ceaușescu 序言事件回避（或严格按 page.md 中性一笔）；撒切尔师生情谊不涉政治展开
- [x] Copley 1976 首位女性；OM 1965 第二位女性——两个"女性第一"勿互换
- [x] 引语全部可在本地 Wikipedia 原文找到（"as breaking the sound barrier"、"Sage"、Bernal 拍照句）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 电子密度气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Dorothy_Hodgkin/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 `images.txt` 下载并核验（page.md 内嵌 Professor_Dorothy_Hodgkin.jpg 为 Bristol 校长任内肖像照；404 则装饰圆占位）
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（Bragg "sound barrier" 句、Bernal "Sage" 句）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 骨架）对齐

---

> **名单状态**：由主控统一更新 `chemist/generate_20th_century_list.py`，本文件不改总表。
