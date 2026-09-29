# Jerome Karle（杰罗姆·卡尔）立传提示词

> qid=Q106733 · 1918-06-18 – 2013-06-06 · 美国物理化学家 · 20 世纪 · 诺贝尔化学奖（1985，与 Herbert A. Hauptman 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Jerome_Karle/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：参考 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`（表格语义化 tabularx + 公式展示框 + 时间线页）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像用 `images/Karle_Retirement.jpg`（2009 退休仪式照，Jerome 位于画面左前景——裁左侧入框；合影原图注须保留"与妻子 Isabella"语义时改图注，不得冒充单人官方肖像）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 晶体结构的直接读出者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Jerome Karfunkle）、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆），母题呼应「晶体中原子的离散点位 / 衍射点阵」——规则排列的圆点暗示晶格与衍射图样。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（Sayre 方程、直接法相位关系）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Jerome Karle（出生名 Jerome Karfunkle；中文惯称：杰罗姆·卡尔）
- **生卒**：1918-06-18 生于纽约市 → 2013-06-06 逝于弗吉尼亚州 Annandale 的 Leewood Healthcare Center（肝癌），享年 94；安葬于弗吉尼亚州阿灵顿 Columbia Gardens Cemetery
- **国籍**：United States（美国）
- **身份**：物理化学家（physical chemist）、晶体学家；美国海军研究实验室（NRL）首席科学家
- **家庭**：犹太家庭，父母 Sadie Helen（娘家姓 Kun）与 Louis Karfunkle，家庭有浓厚艺术氛围——少年学钢琴并参加多场比赛，但更爱科学；1942 年娶 Isabella Helen Lugoski（1921–2017，密歇根大学物理化学课上邻座相识），三女皆从事科学：Louise（1946，理论化学家）、Jean（1950，有机化学家）、Madeleine（1955，地质领域博物馆专家）
- **教育轨迹**：
  - Brooklyn Abraham Lincoln High School（校友含 1959 医学奖 Arthur Kornberg 与 1980 化学奖 Paul Berg）
  - 15 岁入大学；1937 City College of New York 学士（额外修生物学、化学与数学）
  - 1938 Harvard University 硕士（主修生物学）
  - 1940 入 University of Michigan；1943 完成博士学业、1944 获博士学位
- **导师**：Lawrence O. Brockway（物理化学家；妻子 Isabella 与他同受业于 Brockway 门下）
- **研究领域**：物理化学——X 射线晶体学、直接法（direct methods）测定晶体结构

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **布鲁克林的少年（1918）**：艺术之家出身的科学少年——钢琴比赛与手球、滑冰、触身式橄榄球、大西洋边游泳并行。
2. **15 岁上大学（1933）**：CCNY 1937 学士；为攒研究生学费赴纽约州卫生局（Albany）任职，开发溶解氟化物测量法——后成为饮水加氟的标准技术。
3. **哈佛硕士（1938）**：主修生物学；转身物理化学，1940 入密歇根大学。
4. **邻座结缘（1940–1942）**：第一节物理化学课上与 Isabella Lugoski 邻座相识，1942 结婚；夫妇同出 Brockway 门下，科学伉俪一生同行。
5. **曼哈顿计划（1943）**：博士毕业后偕妻赴芝加哥大学参加曼哈顿计划；Isabella 是计划中最年轻的科学家之一、亦是少数女性。
6. **落户 NRL（1944–1946）**：1944 回密歇根大学承接海军研究实验室项目；1946 夫妇迁华盛顿特区正式加入 NRL。
7. **直接法（1950s 起）**：与 Herbert A. Hauptman 合作，在中心对称结构中运用 Sayre 方程，发展所谓"直接法"——从衍射数据直接求解晶体中原子位置，无需先验结构模型。
8. **1985 诺贝尔化学奖**：与 Hauptman 共享，理由为"使用 X 射线散射技术对晶体结构的直接分析"（page.md 口径）；该技术用于研究生物、化学、冶金与物理特性。
9. **技术影响**：直接法成为新药与其他合成材料研发的重要工具——测定分子结构后即可设计流程复制所研究的分子。
10. **学术领袖**：美国晶体学会（ACA）主席（1972）；国际晶体学联合会（IUCr）主席（1981–1984）。
11. **127 年服务（2009）**：2009-07-31 夫妇同日从 NRL 退休——Karle 1944 入职、妻子晚两年，合计为美国政府服务 127 年；时任物质结构实验室首席科学家；海军部长 Ray Mabus 出席退休仪式并授予海军杰出平民服务奖（海军对文职人员的最高表彰）。
12. **荣誉**：1976 当选美国国家科学院院士；1986 Golden Plate Award；1990 美国哲学学会；荣誉博士（马里兰大学、克拉科夫雅盖隆大学）；Captain Robert Dexter Conrad Award。
13. **同葬一穴**：2013-06-06 辞世后与 2017 年去世的妻子合葬于 Columbia Gardens Cemetery——一段从课堂邻座开始的 71 年婚姻的终章。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绛红 crimson） | `#7A1E28` | 晶体衍射的严谨与海军实验室的庄重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（直接法 badgeDirect） | `#2E5A9E` | 蓝相位问题 / Sayre 方程 |
| 分类色 2（X 射线晶体学 badgeXray） | `#1B7A43` | 绿衍射 / 原子定位 |
| 分类色 3（结构生物学应用 badgeStruct） | `#D97B29` | 琥珀药物 / 材料设计 |
| 分类色 4（科学伉俪 badgeDuo） | `#8C5A8F` | 紫曼哈顿计划 / NRL 双星 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 篇一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题「晶格点位 / 衍射点阵」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（清单预置 `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`；执行时按项目惯例软链至本目录，不复制 wav 文件）
- **风格**：恢弘 / 沉静 / 时间纵深
- **匹配理由**：
  - "Eternals" 匹配晶体结构的永恒性——直接法测定的是物质内部亘古不变的原子排列
  - 沉静的时间纵深匹配夫妇二人在 NRL 近六十年的长期坚守（合计 127 年公职）
  - 恢弘感匹配直接法对整个晶体学乃至药物研发的奠基性影响
- **时长核对**：执行时确认音轨时长 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 晶体结构的直接读出者 / Jerome Karle 1918–2013 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名 Karfunkle/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  卡尔的一生 — 时间线（10 节点：1918→1937→1938→1940→1942→1943→1946→1985→2009→2013）
04  早年：艺术之家的科学少年 (1918–1937) — 表格「时间|事件|结果」（钢琴/高中/15 岁入学/CCNY）
05  求学之路：CCNY→哈佛→密歇根 (1937–1944) — 表格「时间|事件|结果」（氟化物测量法/邻座相识/Brockway 门下）
06  曼哈顿计划与 NRL (1943–1946) — 表格「时间|事件|结果」
07  相位问题 (1950s) — 表格「问题|方法|结果」+ 公式框：Sayre 方程（中心对称结构）
08  直接法的诞生 (1985 诺奖) — 表格「挑战|方法|结果」+ 公式框：衍射数据 → 原子位置
09  技术影响：药物与材料 — 表格「领域|应用|意义」
10  学术领袖：ACA 与 IUCr — 表格「机构|职务|年份」（ACA 1972 / IUCr 1981–84 / NAS 1976）
11  科学伉俪 — 双栏页：Isabella 与三个女儿（Louise/Jean/Madeleine）+ 127 年服务
12  荣誉清单 — 「类别|代表|意义」表格（含 itemize：诺奖/Navy 奖/两校荣誉博士/Conrad Award）
13  遗产：直接法改变晶体学 — 四分类遗产盒 + 公式框：直接法 × 新药研发
14  结尾 — 「原子的位置，从此可以从衍射数据中直接读出。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由口径 | 以 page.md 为准："for the direct analysis of crystal structures using X-ray scattering techniques"（使用 X 射线散射技术对晶体结构的直接分析）；勿擅自改写诺贝尔官方 citation 全句 |
| 共享得主 | 1985 与 **Herbert A. Hauptman** 共享（两人）；勿写成独享、勿掺入第三人 |
| 出生名 | 出生名 **Jerome Karfunkle**，后改 Karle——身份页与 §1 须写本名 |
| 博士年份 | 1943 **完成学业**、1944 **获授 PhD**——两个年份勿混（§1 与时间线页须区分） |
| 妻子角色 | Isabella 是独立科学家（曼哈顿计划最年轻科学家之一）；勿写成"Karle 的助手"；两人同师 Brockway |
| 合葬照片 | images.txt 第二张是墓碑照（Karle_Retirement 才是人物照）——墓碑照禁用作肖像 |
| 荣誉细节 | Navy Distinguished Civilian Service Award 授予于 **2009 退休仪式**（海军部长 Mabus 颁发）；frontmatter 另列 Captain Robert Dexter Conrad Award 与两校荣誉博士——页面对后三者的具体年份无载，留白不写年份 |
| 同名区分 | 与晶体学家 Jerome Karle 同时代的 Isabella Karle 未单独获诺贝尔奖——勿写夫妇共同获奖 |
| 引语 | page.md 全文无 Karle 直接引语——全篇禁编引语，用间接转述 |
| Kornberg/Berg | 仅是同一高中（Abraham Lincoln High School）的校友诺奖得主——不是个人关系，禁写入社会关系 |
| 政治内容 | 曼哈顿计划只写科学史实，不展开军事评价 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q106733 | ✅ |
| name_zh | 杰罗姆·卡尔 | ✅ |
| name_en | Jerome Karle | ✅ |
| birth_date | 1918-06-18 | ✅ |
| death_date | 2013-06-06 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：physical chemistry / crystallography / X-ray crystallography / direct methods，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Lawrence O. Brockway | 师→生（博士导师） | 密歇根大学物理化学博士导师；妻子 Isabella 同门 |
| spouse | Isabella Karle | 无向 | 1942 结婚；物理化学课邻座相识；NRL 同事与曼哈顿计划同役（1921–2017） |
| co-honored | Herbert A. Hauptman | 无向 | 1985 诺贝尔化学奖共同得主（直接法） |

> **禁入库名单**：Arthur Kornberg 与 Paul Berg（仅同为 Abraham Lincoln 高学毕业的诺奖校友并列提及——校友同榜非社会关系，不入库）；三个女儿 Louise/Jean/Madeleine Karle（正文有载但均非公众人物，防噪声不入库）；Ray Mabus（仅为颁奖官员）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1985，与 Hauptman 共享）
- Navy Distinguished Civilian Service Award（2009，海军最高文职表彰）
- Captain Robert Dexter Conrad Award
- 荣誉博士：University of Maryland；Jagiellonian University of Krakow
- 美国国家科学院院士（1976）
- Golden Plate Award of the American Academy of Achievement（1986）
- 美国哲学学会会士（1990）

## 9. 机构清单

- 教育：Abraham Lincoln High School（Brooklyn）；City College of New York（BS 1937）；Harvard University（MS 1938）；University of Michigan（1940 入学，PhD 1944）
- 任职：New York State Department of Health（Albany，氟化物测量）；University of Chicago（1943，曼哈顿计划）；University of Michigan（1944，NRL 项目）；U.S. Naval Research Laboratory（1946–2009-07-31，物质结构实验室首席科学家）
- 学术职务：ACA 主席（1972）；IUCr 主席（1981–1984）

## 10. 终审清单

- [ ] 生卒 1918-06-18 / 2013-06-06，享年 94，出生地纽约、去世地 Annandale, Virginia（肝癌）
- [ ] 出生名 Karfunkle、1943 完成/1944 授 PhD 双年份口径准确
- [ ] 1985 与 Hauptman 共享、获奖理由按 page.md 口径
- [ ] Isabella 独立科学家身份、127 年服务与 2009 退休仪式表述准确
- [ ] 全篇无编造引语；高中校友（Kornberg/Berg）不入师承/同事语义
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 `pages/Jerome_Karle/page.md` 逐页对照 Beamer tex 全部事实
- [ ] 头像：Karle_Retirement.jpg 裁左入框，图注如实
- [ ] 国籍：封面明示美国
- [ ] 编译验证：`make distclean && make`
- [ ] Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt、hbox≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：由 chem-batch-19 批次产出提示词与数据入库；立传与 Review 列由主控统一收尾。
