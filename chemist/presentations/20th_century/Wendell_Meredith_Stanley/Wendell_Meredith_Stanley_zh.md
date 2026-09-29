# Wendell Meredith Stanley（温德尔·梅雷迪思·斯坦利）立传提示词

> qid=Q105937 · 1904-08-16 – 1971-06-15 · 美国生物化学家、病毒学家 · 20 世纪 · 诺贝尔化学奖（1946，¼ 份额共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Wendell_Meredith_Stanley/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 已就位则用真照，缺图用装饰圆占位并注「肖像暂缺」）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{virus}\enspace 让病毒现出晶体之形\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、师承（★ 页面无载博士导师，写「页面无载」）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「晶体 / 病毒颗粒」母题——规整圆点暗示病毒在晶体中整齐排列。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 TMV 结晶示意式。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Wendell Meredith Stanley（中文惯称：温德尔·梅雷迪思·斯坦利）
- **生卒**：1904-08-16 生于美国印第安纳州 Ridgeville → 1971-06-15 逝于西班牙 Salamanca，享年 66
- **国籍**：United States（美国）
- **身份**：生物化学家、病毒学家（biochemist & virologist；1946 年诺贝尔化学奖 ¼ 份额得主）
- **家庭**：1929 年娶 Marian Staples（1905–1984）；三女 Marjorie、Dorothy、Janet，一子 Wendell Meredith Junior；女儿 Marjorie 嫁给金州勇士队与奥克兰突袭者队队医 Robert Albo。UC Berkeley 的 Stanley Hall（今 Stanley Biosciences and Bioengineering Facility）与 Earlham College 的 Stanley Hall 均以其命名
- **教育轨迹**：
  - Richmond High School（印第安纳州 Richmond，infobox）
  - Earlham College（Richmond, Indiana），化学 BSc
  - University of Illinois Urbana-Champaign：1927 硕士（MS in science），两年后（1929）化学博士
- **博士导师**：本地页面无载（★ 勿脑补；§7 不入库 advisor 关系）
- **研究领域**：生物化学、病毒学——病毒结晶、核酸蛋白（nucleoprotein）、二苯乙烯立体化学、甾醇化学、抗麻风化合物

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **印第安纳农家子（1904）**：生于 Ridgeville 小镇，先入 Earlham College（Richmond）读化学本科——从内陆小城走向大科学的起点。
2. **伊利诺伊双学位（1927/1929）**：1927 获 MS，1929 获化学 PhD，完成从化学到生命科学的装备。
3. **国家研究委员会与慕尼黑（1929–1931）**：身为 National Research Council 成员，赴慕尼黑与 Heinrich Wieland（1927 诺贝尔化学奖得主）做短期学术工作，1931 年返美。
4. **洛克菲勒研究所（1931–1948）**：1931 年获批任助理；1937 年升 Associate Member；1940 年升 Member——十五年间从助手到正式成员。
5. **烟草花叶病毒结晶（1935）**：从烟草花叶病毒（TMV）颗粒制得晶体——被广泛报道，登上 1935-06-28《纽约时报》头版；人们惊讶于病毒这类"类生命体"竟能结晶。
6. **病毒第一次"被看见"（1935）**：这是病毒首次以某种形式"被看见"——此前病毒仅以能穿过最细陶瓷滤器的极小感染源被间接表征；真正的单个病毒颗粒要到 1942 年电子显微镜发明后由 Thomas F. Anderson 与 Salvador Luria 在噬菌体上实现。
7. **核蛋白结论（1935 前后）**：分离出显示 TMV 活性的核蛋白（nucleoprotein）——"病毒是化学物质"的实证宣言。
8. **三院院士（1940/1941/1949）**：1940 美国哲学学会、1941 美国国家科学院、1949 美国艺术与科学院——战时美国科学界的高度认可。
9. **1946 诺贝尔化学奖（¼ 份额）**：因 TMV 结晶工作获奖，份额 ¼——页面未列共同得主姓名（同届 Sumner ½、Northrop ¼ 属诺奖史常识，但本地页面无载，§5 见红线）。
10. **伯克利创业（1948）**：任 UC Berkeley 生物化学教授，创建 Virus Laboratory 与独立的生物化学系大楼——即今 Stanley Hall。
11. **诚实的科学史脚注**：其诺奖研究的多数结论很快被证明有误——尤其是"病毒晶体是纯蛋白、靠自催化组装"两点；诺贝尔奖也会奖励开辟方向的人（★ 必写，立传的诚实底线）。
12. **笔耕与荣誉**：著书 "Chemistry: A Beautiful Thing"，曾获普利策奖提名；Newcomb Cleveland Prize（1936）、Nichols Medal（1946）、Willard Gibbs Award（1947）、Franklin Medal（1948）、旭日章（1966）。
13. **落幕西班牙（1971）**：1971-06-15 逝于西班牙 Salamanca，享年 66——大西洋两岸都留下他的足迹。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（病毒晶体蓝 slateblue） | `#37548D` | 结晶学的冷峻与病毒的神秘（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（病毒结晶 badgeCrystal） | `#1B4F72` | 深蓝 TMV 晶体 / 1935 头版 |
| 分类色 2（病毒学 badgeVirus） | `#5B2C6F` | 紫 TMV 活性 / 核蛋白 |
| 分类色 3（洛克菲勒岁月 badgeRockefeller） | `#148F77` | 青 1931–1948 研究所生涯 |
| 分类色 4（伯克利岁月 badgeBerkeley） | `#B9770E` | 琥珀 Virus Laboratory / Stanley Hall |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「晶体 / 病毒颗粒」的规整排列。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（`music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`；不要复制 wav 文件，Makefile 直接引用路径）
- **风格**：磅礴 / 戏剧性 / 开拓气魄
- **匹配理由**：
  - "磅礴" 匹配 TMV 结晶的震撼——1935 年《纽约时报》头版级的科学事件
  - "戏剧性" 匹配其经历的起伏——诺奖加冕与结论被修正并存的一生
  - "开拓气魄" 匹配 1948 年伯克利白手创建 Virus Laboratory 的创业气质
- **时长**：以实际文件为准；ffmpeg `-shortest` 自动对齐幻灯片时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 让病毒现出晶体之形 / Wendell Meredith Stanley 1904–1971 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/师承注"页面无载"/出生地/去世地/领域/荣誉）
03  斯坦利的一生 — Sanger 式时间线（10 节点：1904→1927→1929→1931→1935→1940→1946→1948→1966→1971）
04  早年与求学 (1904–1929) — 表格「时间|事件|结果」
05  慕尼黑与洛克菲勒 (1929–1940) — 表格「时间|事件|结果」（Wieland 短期合作 / 助理→Member）
06  病毒结晶 (1935) — 表格「问题|方法|结果」+ 公式框：TMV → 结晶核蛋白
07  一夜之间登上头版 (1935) — 表格「事件|报道|意义」（NYT 1935-06-28 头版 / 病毒首次"被看见"）
08  电镜时代的对照 (1942) — 表格「人物|工具|结果」（Anderson & Luria / 电镜 / 噬菌体实拍）
09  1946 诺贝尔化学奖 — 表格「年份|奖项|份额」+ 公式框：1946 ¼ share
10  伯克利创业 (1948) — Sanger FFT 页式流程图（教授 → Virus Laboratory → 生化系大楼 → Stanley Hall）
11  荣誉与院士 — Sanger 式「类别|代表|意义」表格（含 itemize 荣誉清单 / 三院院士）
12  诚实的脚注 — 表格「当年结论|后来的修正|启示」（纯蛋白→含 RNA；自催化→页面结论表述）
13  遗产：病毒学的化学化 — 四分类遗产盒 + 公式框：「病毒亦可结晶」
14  结尾 — 「当病毒凝成晶体，生命与化学的边界从此改写。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1946 获奖份额 | 页面明载 "awarded a ¼ share"——写 **¼ 份额共享**；页面未点名共同得主，**勿自行写 Sumner/Northrop 入正文或入库**（§7 红线） |
| 1946 获奖理由官方原文 | 本地页面**无载** citation 原句——勿杜撰英文获奖理由；只写 "因烟草花叶病毒结晶相关工作获奖" |
| "第一个看见病毒" | 只能写"病毒首次以某种形式被看见（in some form）"；真正单个病毒颗粒 1942 年才由 Anderson/Luria 用电镜在噬菌体上实现——勿写"第一个看到病毒" |
| 结论被修正 | **必须如实写**：其诺奖研究多数结论很快被证明有误（晶体是纯蛋白、自催化组装）——这是页面明载的诚实脚注，勿美化 |
| 博士导师 | 页面（正文+infobox+metadata）**均无载**——身份页写「页面无载」，§7 不建 advisor 关系，禁脑补 |
| Wieland 身份 | 页面只写 "temporary academic work with Heinrich Wieland"（慕尼黑短期学术合作）——他是 1927 化学奖得主属实，但**师生/导师关系页面无载**，只入 colleague |
| 入职年份 | 洛克菲勒 1931 助理 → 1937 Associate Member → 1940 Member；Berkeley 1948 教授——年份勿错位 |
| 出生/去世地 | 生于印第安纳 Ridgeville、逝于西班牙 Salamanca——勿混淆；页面未载去世缘由，勿写 |
| 配偶与子女 | Marian Staples（1905–1984），1929 年结婚；三女一子；女儿 Marjorie 之夫 Robert Albo 为球队医生——趣闻可一句带过，不入库 |
| 同名区分 | Wendell Meredith Stanley 无常见重名；与斯坦利·米勒（Miller-Urey）无关，勿混 |
| 引语红线 | 页面**无任何直接引语**——全书改间接转述；书名 "Chemistry: A Beautiful Thing" 与普利策提名是事实可写，勿配"原话" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q105937 | ✅ |
| name_zh | 温德尔·梅雷迪思·斯坦利 | ✅ |
| name_en | Wendell Meredith Stanley | ✅ |
| birth_date | 1904-08-16 | ✅ |
| death_date | 1971-06-15 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry, virology（person_field 细分：biochemistry / virology / stereochemistry / sterol chemistry，带 rank） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Heinrich Otto Wieland | 无向 | 1931 前在慕尼黑与之短期学术工作（页面作 Heinrich Wieland，入库用规范全名） |
| spouse | Marian Staples | 无向 | 1929 年结婚；三女一子 |

> **禁入库名单（页面无载或 metadata-only）**：James B. Sumner、John Howard Northrop（1946 同届共同得主，本页正文未点名——不建 co-honored，由其本人页面批次决定）；Thomas F. Anderson、Salvador Luria（仅为电镜史实人物，与 Stanley 无直接关系载述）；博士导师（页面无载）；Robert Albo（女婿，姻亲不入库）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1946，¼ 份额）
- Newcomb Cleveland Prize（1936）
- William H. Nichols Medal（1946）
- Willard Gibbs Award（1947）
- Franklin Medal（1948）
- Order of the Rising Sun 旭日章（1966）
- Rosenburger Medal、Alder Prize、John Scott Award、Golden Plate Award、AMA Scientific Achievement Award、Silliman Memorial Lectures（年份页面无载，如实标注）
- Guggenheim Fellowship（infobox；年份无载）
- 哈佛、耶鲁、普林斯顿、巴黎大学等多校荣誉学位（页面明载 "including Harvard, Yale, Princeton and the University of Paris"）

## 9. 机构清单

- 教育：Richmond High School；Earlham College（BSc，化学）；University of Illinois Urbana-Champaign（MS 1927、PhD 1929）
- 访学：慕尼黑（与 Heinrich Wieland 短期学术工作，1931 前返美）
- 任职：United States National Research Council（成员）；The Rockefeller Institute for Medical Research（1931 助理 → 1937 Associate Member → 1940 Member，至 1948）；University of California, Berkeley（1948 起生物化学教授；创建 Virus Laboratory 与生物化学系大楼——今 Stanley Hall）
- 命名机构：UC Berkeley Stanley Hall（今 Stanley Biosciences and Bioengineering Facility）；Earlham College Stanley Hall

## 10. 终审清单

- [ ] 生卒 1904-08-16 / 1971-06-15，享年 66，出生地 Ridgeville（印第安纳）、去世地 Salamanca（西班牙）
- [ ] 1946 诺奖 ¼ 份额表述准确；**正文不点名共同得主**；获奖理由官方原文不杜撰
- [ ] 1927 MS / 1929 PhD / 1931 洛克菲勒助理 / 1937 Associate / 1940 Member / 1948 Berkeley 年份链准确
- [ ] 1935 TMV 结晶 + NYT 头版（1935-06-28）+ "in some form" 口径准确；1942 Anderson/Luria 对照准确
- [ ] 结论被修正（纯蛋白、自催化）如实呈现
- [ ] 博士导师写「页面无载」；无任何杜撰引语
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误，溢出达标

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Wendell_Meredith_Stanley/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 肖像核对（缺图用装饰圆占位并注记）
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：全书无杜撰"原话"（页面无直接引语）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动该脚本。
> **最重要的事：每写一页就 make，看到溢出就修。**
