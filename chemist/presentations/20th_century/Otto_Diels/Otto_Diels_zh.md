# Otto Diels（奥托·迪尔斯）立传提示词

> qid=Q76616 · 1876-01-23 – 1954-03-07 · 德国化学家 · 20 世纪 · 诺贝尔化学奖（1950，与 Kurt Alder 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Otto_Diels/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（页面实载图为基尔纪念牌 Gedenktafel 与 Diels–Alder 反应图——images/ 有人像则用真照，否则装饰圆占位并注「肖像暂缺」，**勿拿纪念牌照片冒充肖像**）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 双烯与亲双烯体的握手\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、全名（Otto Paul Hermann Diels）、国籍、出生地/去世地、教育（柏林大学）、博士导师（Emil Fischer）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「六元环 / 双键」母题——成对圆环暗示 Diels–Alder 反应中双烯体与亲双烯体的环化握手。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 Diels–Alder [4+2] 环加成示意（化学式取自页面实载 Original Diels-Alder reaction 图）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Otto Paul Hermann Diels（中文惯称：奥托·迪尔斯；子承父业——其父 Hermann Diels 为古典语文学家，**页面无载其父信息，勿写**）
- **生卒**：1876-01-23 生于汉堡（德意志帝国） → 1954-03-07 逝于基尔（西德），享年 78
- **国籍**：Germany（德国）
- **身份**：化学家（chemist；1950 年诺贝尔化学奖共享得主；基尔大学教授至 1945 退休）
- **家庭**：1909 年娶 Paula Geyer；三子二女共五人；其中两子死于二战战场；业余好阅读、音乐与旅行
- **教育轨迹**：
  - 柏林 Joachimsthalsches Gymnasium
  - 1895 年入 University of Berlin，师从 Emil Fischer 读化学，1899 年毕业
- **博士导师**：Emil Fischer（infobox 与 frontmatter 明载；正文口径 "studied chemistry under Emil Fischer"）
- **研究领域**：化学——Diels–Alder 双烯合成反应、环状有机化合物合成、氢芳族化合物（hydroaromatic）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **汉堡开局（1876）**：生于汉堡，两岁随家迁柏林——德意志帝国黄金年代的城市童年。
2. **Joachimsthalsches Gymnasium**：柏林名校出身，1895 年入柏林大学。
3. **Fischer 门下（1895–1899）**：在赫尔曼·费歇尔（Hermann Emil Fischer）指导下读化学，1899 年毕业——19 世纪末有机化学黄金传直接续。
4. **留校升迁（1899–1915）**：毕业即获柏林大学化学研究所职位，一路晋升，1913 年任 Department Head——十六年从新人到系主任。
5. **转战基尔（1915）**：1915 年接受 University of Kiel 职位，直至 1945 年退休——基尔三十年是诺奖工作的全部舞台。
6. **1928：Diels–Alder 反应**：与 Kurt Alder 共同发现 Diels–Alder 反应（页面实载图注 "The reaction discovered by Diels and Alder in 1928"）——共轭双烯与亲双烯体一步成环，合成环己烯衍生物的经典方法。
7. **环状有机合成的通用钥匙**：这一合成方法可制备不饱和环状化合物——被证明对合成橡胶与塑料制造极具价值。
8. **导师与学生同榜**：博士导师 Emil Fischer（1902 诺奖）、博士生 Kurt Alder 与他共享 1950 诺奖——三代化学人两代诺奖的谱系奇观。
9. **1950 诺贝尔化学奖（与 Alder 共享）**："The pair was awarded the Nobel Prize in Chemistry in 1950 for their work"——两人共享（页面未载份额细节，勿写对半/ unequal）；诺奖演说题为 "Description and Importance of the Aromatic Basic Skeleton of the Steroids"。
10. **以化学家之名为城留念**：基尔为其设纪念牌（Gedenktafel）——工作三十年的城市以石铭志。
11. **Diels–Reese 反应**：infobox "Known for" 另列 Diels–Reese reaction——Diels 名下不止一个反应，正文可一句带过。
12. **战火中的家庭**：五个孩子中两个儿子阵亡于二战——德国科学家一代的集体创痕，立传如实一笔。
13. **战后落幕（1945–1954）**：1945 年退休，1954-03-07 逝于基尔；其 1928 年德文原著 "Synthesen in der hydroaromatischen Reihe" 有英译 "Syntheses of the hydroaromatic series" 传世。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（森林绿 deep pine） | `#1E5631` | 有机环系化合物的沉稳与生命感（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（Diels–Alder badgeDA） | `#1B4F72` | 深蓝 [4+2] 环加成 / 1928 发现 |
| 分类色 2（环状合成 badgeRing） | `#7D6608` | 琥珀环己烯合成 / 不饱和环系 |
| 分类色 3（师门谱系 badgeFischer） | `#5B2C6F` | 紫 Fischer 门下 / Alder 同榜 |
| 分类色 4（基尔岁月 badgeKiel） | `#148F77` | 青 1915–1945 三十年基尔 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），成对呼应「双烯体 × 亲双烯体」的环化意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（`music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`；不要复制 wav 文件，Makefile 直接引用路径）
- **风格**：电影感 / 开阔 / 史诗收束
- **匹配理由**：
  - "电影感" 匹配 Diels–Alder 反应的戏剧性——两种分子一步成环，像分镜合成的化学蒙太奇
  - "开阔" 匹配其影响半径——从基础有机化学到合成橡胶与塑料的工业大地
  - "史诗收束" 匹配其人生弧线——1899 年 Fischer 门下起步，1950 年与自己的学生同榜封爵，1954 谢幕
- **时长**：以实际文件为准；ffmpeg `-shortest` 自动对齐幻灯片时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 双烯与亲双烯体的握手 / Otto Diels 1876–1954 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/全名/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  迪尔斯的一生 — Sanger 式时间线（10 节点：1876→1895→1899→1913→1915→1928→1945→1950→1954，另设婚家庭节点）
04  汉堡与柏林 (1876–1895) — 表格「时间|事件|结果」
05  Fischer 门下 (1895–1899) — 表格「阶段|师承|结果」
06  柏林升迁与转战基尔 (1899–1915) — 表格「时间|职位|结果」（1913 系主任 / 1915 基尔）
07  Diels–Alder 反应 (1928) — 表格「问题|方法|结果」+ 公式框：[4+2] 环加成示意（取页面实载图）
08  从实验室到工厂 — 表格「方法|产物|意义」（合成橡胶 / 塑料 / 不饱和环状化合物）
09  1950 诺贝尔化学奖（与 Alder 共享） — 表格「年份|奖项|同榜」+ 公式框：Diels + Alder → Nobel 1950
10  师门谱系 — Sanger FFT 页式流程图（Emil Fischer → Otto Diels → Kurt Alder：三代两诺奖）
11  家庭与战火 — 表格「时间|事件|结果」（1909 婚 / 五子女 / 两子阵亡）
12  荣誉清单 — 表格「奖项|情况|意义」（Nobel 1950 / 联邦十字勋章司令级 / Adolf-von-Baeyer 金章·年份无载）
13  遗产：环加成改变合成化学 — 四分类遗产盒 + 公式框：Diels–Alder → 橡胶与塑料
14  结尾 — 「两个分子握手成环，有机合成从此有了万能的钥匙。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1950 获奖口径 | **与 Kurt Alder 共享**；页面只写 "The pair was awarded..."，**未载份额对半与否**——勿写"各得一半"；获奖理由官方 citation 原句页面无载，勿杜撰 |
| 反应发现年份 | 1928（页面实载图注明）——"discovered by Diels and Alder in 1928"；勿写"1920s 泛指" |
| 博士导师姓名 | 页面正文与 infobox 作 **Emil Fischer**，metadata 作 Hermann Emil Fischer；库内对手方用 **Hermann Emil Fischer**（规范全名，1902 诺贝尔化学奖得主）——勿与其学生 Emil Fischer 同名者或其他 Fischer（Ernst Fischer 等）混淆 |
| 诺奖演说标题 | "Description and Importance of the Aromatic Basic Skeleton of the Steroids"——演说讲甾体芳香骨架，**勿把获奖工作与甾体混为一谈**（获奖工作是 Diels–Alder 反应） |
| Diels–Reese 反应 | infobox Known for 明载——可一句带过，勿展开机理（页面无载） |
| 父亲身份 | 其父为古典语文学家 Hermann Diels 属史实但**本页无载**——禁写 |
| 份额与排名 | 与 Alder 的师承（advisor-student）与共享（co-honored）双关系并立，两条都入库；Alder 亦是 Diels 的博士生（infobox） |
| 两子阵亡 | 页面明载 "Two of his sons were killed in action during World War II"——如实一句，勿展开战役细节 |
| 退休与去世 | 1945 退休；1954-03-07 逝于基尔——与出生汉堡对仗勿混 |
| 奖项年份 | 联邦德国功绩十字司令级十字与 Adolf-von-Baeyer 金章**页面无载年份**——如实标注"年份无载" |
| 同名区分 | Otto Diels 无常见重名；书目英文译名 "Syntheses of the hydroaromatic series" 勿当作发表年份依据 |
| 引语红线 | 页面**无任何直接引语**——全书改间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76616 | ✅ |
| name_zh | 奥托·迪尔斯 | ✅ |
| name_en | Otto Diels | ✅ |
| birth_date | 1876-01-23 | ✅ |
| death_date | 1954-03-07 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：organic chemistry / organic synthesis / hydroaromatic chemistry，带 rank） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hermann Emil Fischer | 师→生（博士导师） | 柏林大学，1895–1899 师从读化学；页面作 Emil Fischer，入库用规范全名 |
| advisor-student | Kurt Alder | Diels→学生 | infobox Doctoral students；基尔共事，1928 共同发现 Diels–Alder 反应 |
| co-honored | Kurt Alder | 无向 | 1950 诺贝尔化学奖共同得主（师生+共享双关系并立） |
| advisor-student | Karl Wilhelm Rosenmund | Diels→学生 | infobox Doctoral students |
| spouse | Paula Geyer | 无向 | 1909 年结婚；三子二女共五人 |

> **禁入库名单（页面无载或非个人关系）**：共同得主的份额信息（页面未载）；其父 Hermann Diels（本页无载）；University of Berlin / Kiel 机构人物（无具体个人关系载述）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1950，与 Kurt Alder 共享）
- Commander's Cross of the Order of Merit of the Federal Republic of Germany（联邦德国功绩十字司令级；年份页面无载）
- Adolf-von-Baeyer Gold Medal（年份页面无载，如实标注）

## 9. 机构清单

- 教育：Joachimsthalsches Gymnasium（柏林）；University of Berlin（1895 入学，师从 Emil Fischer，1899 毕业）
- 任职：University of Berlin 化学研究所（1899–1915；1913 年任 Department Head）→ University of Kiel（1915–1945 退休；诺奖工作全部在基尔完成）
- 纪念：基尔 Otto Diels 纪念牌（Gedenktafel）

## 10. 终审清单

- [ ] 生卒 1876-01-23 / 1954-03-07，享年 78，出生地汉堡、去世地基尔
- [ ] 1950 与 Kurt Alder 共享、份额不写；获奖理由官方 citation 不杜撰
- [ ] 1895 入学 / 1899 毕业 / 1913 系主任 / 1915 基尔 / 1928 反应 / 1945 退休 年份链准确
- [ ] 博士导师用 Hermann Emil Fischer 规范全名；Alder 双关系（student + co-honored）并立
- [ ] 演说标题（甾体）与获奖工作（Diels–Alder）不混淆
- [ ] 全书无杜撰引语；两子阵亡如实一笔
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误，溢出达标

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Otto_Diels/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：页面实载图为纪念牌与反应图——**勿冒充肖像**，缺人像用装饰圆占位并注记
- [ ] 国籍：封面顶部明示德国
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
