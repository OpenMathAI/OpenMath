# Robert Robinson（罗伯特·鲁宾逊）立传提示词

> qid=Q49351 · 1886-09-13 – 1975-02-08 · 英国有机化学家 · 20 世纪 · 诺贝尔化学奖（1947，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Robert_Robinson_organic_chemist/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 已就位则用真照，缺图用装饰圆占位并注「肖像暂缺」）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 天然产物的建筑大师\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士导师（William Henry Perkin Jr.）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「苯环 / 环状分子」母题——圆环暗示苯环中央的圆圈（Robinson 1923 年首创）。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如托品酮一锅合成路线。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir Robert Robinson（OM FRS FRSE；中文惯称：罗伯特·鲁宾逊）
- **生卒**：1886-09-13 生于德比郡 Chesterfield 附近 Rufford House Farm → 1975-02-08 逝于白金汉郡 Great Missenden，享年 88
- **国籍**：United Kingdom（英国）
- **身份**：有机化学家（organic chemist；1947 年诺贝尔化学奖独享得主；皇家学会第 48 任主席 1945–1950）
- **家庭**：父 James Bradbury Robinson 为外科敷料制造商，母 Jane Davenport；1912 年娶 Gertrude Maud Walsh（1954 年去世）；1957 年再娶寡妇 Sylvia Hillstrom（娘家姓 Hershey）
- **教育轨迹**：
  - Chesterfield Grammar School（今 Brookfield Community School）、私立 Fulneck School
  - University of Manchester 读化学，1905 年 BSc
  - 1907 年获 1851 Research Fellowship，留曼彻斯特继续研究
- **博士导师**：William Henry Perkin Jr.（infobox 与 frontmatter 明载；其曼彻斯特讲席的前任正是 Lapworth 与 Perkin Jr.）
- **研究领域**：有机化学——天然产物（花青素苷/植物色素、生物碱）、有机合成、仿生合成、箭头推电子（curly arrows）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **德比郡农场之子（1886）**：生于 Rufford House Farm，父业外科敷料制造——家境殷实、早慧于化学。
2. **曼彻斯特起点（1905/1907）**：1905 年 BSc；1907 年 1851 Research Fellowship——青年才俊的第一桶金。
3. **南半球讲席（1912）**：悉尼大学首位 Pure and Applied Organic Chemistry 教授——28 岁执掌教席。
4. **利物浦与染料业（1915–1920）**：利物浦大学有机化学讲席（1915–20）；后任 British Dyestuffs Corporation 研究主任——学术与工业双线。
5. **托品酮一锅合成（1917）**：tropinone（阿托品与苯扎托品的前体）的合成不仅是生物碱化学一大步，更证明**一锅串联反应**可构筑双环分子——仿生合成的里程碑。
6. **苯环加圈（1923）**：在圣安德鲁斯大学工作期间首创**苯环中央加圆圈**的符号——今天每本教科书的苯环画法源自于此。
7. **箭头推电子第一人**：第一个使用 curly arrows 表示电子移动——现代有机反应机理书写的奠基者。
8. **吗啡与青霉素结构**：测定吗啡与青霉素的分子结构——战时化学的巅峰任务之一。
9. **牛津岁月（1930–）**：1930 年起任牛津 Waynflete Professor of Chemistry 兼 Magdalen College Fellow；此前 1928–1930 执教 UCL；1921–22 短暂任教圣安德鲁斯。
10. **士的宁结构（1946）**：测定 strychnine（士的宁）结构——获奖前一年完成的最复杂天然产物之一。
11. **1947 诺贝尔化学奖（独享）**：表彰其对**植物色素（花青素苷）与生物碱**的研究；同年获 Medal of Freedom with Silver Palm；诺奖演说 "Some Polycyclic Natural Products"（1947-12-12）。
12. **三院国际成员 + 皇家学会主席（1945–1950）**：1934 美国 NAS 国际成员、1944 美国哲学学会、1948 美国艺术与科学院；皇家学会第 48 任主席（前任 Henry Hallett Dale、后任 Edgar Adrian）。
13. **象棋与《Tetrahedron》**：强力业余棋手——1944-12 牛津联队对布莱切利园友谊赛中输给计算机先驱 I. J. Good；1950–53 任英国棋联主席，与 Raymond Edwards 合著 *The Art and Science of Chess*（1972）；1957 年为 Pergamon 创办期刊 *Tetrahedron*（邀 50 位编辑）；已烯雌酚（diethylstilboestrol）原始合成亦与 Edward Charles Dodds 并肩完成。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海蓝青） | `#0B5351` | 天然产物化学的深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（生物碱 badgeAlkaloid） | `#1D6A96` | 蓝托品酮 / 士的宁 / 吗啡 |
| 分类色 2（植物色素 badgeAnthocyanin） | `#8E2A4A` | 玫红花青素苷 / 植物染料 |
| 分类色 3（机理符号 badgeArrow） | `#C4761B` | 琥珀 curly arrows / 苯环加圈 |
| 分类色 4（牛津与皇家学会 badgeOxford） | `#3F6B4F` | 绿 Waynflete 讲席 / RS 主席 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「苯环 / 环状分子」的圆环排列。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（`music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`；不要复制 wav 文件，Makefile 直接引用路径）
- **风格**：深沉 / 戏剧张力 / 厚重史诗
- **匹配理由**：
  - "深沉" 匹配 19 世纪末出生的一代化学大家——从维多利亚式学徒制走向现代机理化学的漫长人生（1886–1975，横跨 89 年）
  - "戏剧张力" 匹配天然产物结构测定的智力搏杀——吗啡、青霉素、士的宁皆是硬仗
  - "厚重史诗" 匹配其身份厚度——诺奖、OM、皇家学会主席、殿堂级符号首创者
- **时长**：以实际文件为准；ffmpeg `-shortest` 自动对齐幻灯片时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 天然产物的建筑大师 / Robert Robinson 1886–1975 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  鲁宾逊的一生 — Sanger 式时间线（10 节点：1886→1905→1912→1917→1923→1930→1945→1946→1947→1975）
04  德比郡与曼彻斯特 (1886–1907) — 表格「时间|事件|结果」
05  从悉尼到利物浦 (1912–1920) — 表格「时间|任职|结果」
06  托品酮一锅合成 (1917) — 表格「问题|方法|结果」+ 公式框：tropinone 串联合成示意
07  符号革命 (1923) — 表格「符号|首创|意义」（苯环加圈 / curly arrows）
08  天然产物三战 — 表格「目标|成果|意义」（吗啡 / 青霉素 / 士的宁 1946）
09  1947 诺贝尔化学奖（独享） — 表格「年份|奖项|理由」+ 公式框：plant dyestuffs & alkaloids
10  牛津与皇家学会 (1930–1950) — Sanger FFT 页式流程图（Waynflete 讲席 → Magdalen Fellow → RS 第 48 任主席）
11  棋盘上的化学家 — 表格「棋事|对手|结果」（Bletchley Park 1944 / I. J. Good / 英国棋联主席）
12  荣誉与纪念 — Sanger 式「类别|代表|意义」表格（OM / Copley / Davy / Royal Medal / 四地命名实验室）
13  遗产：机理书写的语言 — 四分类遗产盒 + 公式框：curly arrows 遍布今日教科书
14  结尾 — 「苯环中的那个圆，是他留给化学的签名。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1947 获奖口径 | 页面口径：**独享**；理由为 "his research on plant dyestuffs (anthocyanins) and alkaloids"——勿杜撰更长/更短的诺贝尔官方 citation 原句；勿写与他人共享 |
| 博士导师姓名 | infobox 作 "William Henry Perkin, Jr."、正文作 "William Henry Perkin Jr."——入库用 **William Henry Perkin Jr.**（防与老 Perkin 混淆，其父 William Henry Perkin 是苯胺紫发现者，勿混） |
| 博士生名单 | 以 **page.md infobox 为准**（Edward Abraham、Arthur John Birch、William Sage Rapson、John Cornforth、Rita Harradence、K. Venkataraman 六人）；metadata 另有 Richard Manske、Alexander Todd、Lindsay Heathcote Briggs——**metadata-only 禁入库**（Todd 虽是诺奖得主亦不入） |
| "first to use curly arrows" | 页面明载 "He was the first to use curly arrows"——可写"第一个使用箭头表示电子移动"，但注明这是 Wikipedia 口径 |
| 苯环加圈 | 页面明载 1923 年在**圣安德鲁斯**工作期间首创——勿写"在牛津发明" |
| 青霉素结构 | 页面写 "discovered the molecular structures of morphine and penicillin"——照页面口径写"测定/发现分子结构"，勿展开团队合作细节（页面无载） |
| 士的宁年份 | **1946** 年测定 strychnine 结构——在获奖（1947）之前，勿写反 |
| 已烯雌酚 | 与 Edward Charles Dodds 并肩（"Alongside"）参与原始合成——colleague 关系可入库；勿写"独立发明" |
| 皇家学会届次 | 第 48 任 President（1945–1950）；前任 Henry Hallett Dale、后任 Edgar Adrian——届次与人物方向勿错 |
| 棋局对手 | 1944-12 输给 **I. J. Good**（布莱切利园计算机先驱）——"输"的方向勿写反 |
| 两段婚姻 | 1912 Gertrude Maud Walsh（1954 去世）→ 1957 寡妇 Sylvia Hillstrom（née Hershey）——两段都要写，勿只写第一段 |
| 同名区分 | 目录名 Robert_Robinson_organic_chemist——与数学家 Robert Robinson 等他人无关；正文首现即注 "Robert Robinson (chemist)" |
| 引语红线 | 页面**无任何直接引语**——全书改间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q49351 | ✅ |
| name_zh | 罗伯特·鲁宾逊 | ✅ |
| name_en | Robert Robinson | ✅ |
| birth_date | 1886-09-13 | ✅ |
| death_date | 1975-02-08 | ✅ |
| nationality | United Kingdom（另有出生时的 United Kingdom of Great Britain and Ireland，rank 次序） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：organic chemistry / organic synthesis / alkaloid chemistry / biomimetic synthesis，带 rank） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | William Henry Perkin Jr. | 师→生（博士导师） | 曼彻斯特大学；其讲席前任即 Lapworth 与 Perkin Jr. |
| advisor-student | Edward Abraham | Robinson→学生 | infobox Doctoral students |
| advisor-student | Arthur John Birch | Robinson→学生 | infobox；后创 Birch 还原 |
| advisor-student | William Sage Rapson | Robinson→学生 | infobox |
| advisor-student | John Cornforth | Robinson→学生 | infobox；1975 诺贝尔化学奖得主 |
| advisor-student | Rita Harradence | Robinson→学生 | infobox；Cornforth 之妻 |
| advisor-student | K. Venkataraman | Robinson→学生 | infobox |
| colleague | Edward Charles Dodds | 无向 | 与之并肩参与己烯雌酚原始合成 |
| spouse | Gertrude Maud Walsh | 无向 | 1912 年结婚，1954 年去世；infobox Spouse 即此人（婚後名 Gertrude Maud Robinson） |
| spouse | Sylvia Hillstrom | 无向 | 1957 年再婚，寡妇，娘家姓 Hershey |

> **禁入库名单（metadata-only，页面 infobox 无）**：Richard Helmuth Frederick Manske、Alexander Todd、Lindsay Heathcote Briggs（metadata doctoral_student 三人——Todd 虽为 1957 诺奖得主亦不入）；I. J. Good（棋局对手，非科学关系）；Henry Hallett Dale、Edgar Adrian（皇家学会职务前后任，非个人关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1947，独享）
- Longstaff Prize（1927）
- Davy Medal（1930）
- Royal Medal（1932）
- Copley Medal（1942）
- Medal of Freedom with Silver Palm（1947）
- Franklin Medal（1947）
- Albert Medal（1947）
- Faraday Lectureship Prize（1947）
- Knight Bachelor；Order of Merit（OM）
- Knight of the Legion of Honour（法国荣誉军团勋章）
- Priestley Medal；Paracelsus Prize；August Wilhelm von Hofmann Medal；Bakerian Medal；Honorary Fellow of the Royal Society Te Apārangi；萨格勒布大学与马德里康普顿斯大学、巴黎大学荣誉博士

## 9. 机构清单

- 教育：Chesterfield Grammar School（今 Brookfield Community School）、Fulneck School；University of Manchester（BSc 1905；1851 Research Fellowship 1907）
- 任职：University of Sydney（1912，首位 Pure and Applied Organic Chemistry 教授）→ University of Liverpool（1915–20）→ British Dyestuffs Corporation（研究主任）→ St Andrews（1921–22）→ University of Manchester（讲席）→ University College London（1928–1930）→ University of Oxford（1930 起 Waynflete Professor；Magdalen College Fellow）
- 学会：皇家学会第 48 任主席（1945–1950）；美国 NAS 国际成员（1934）、美国哲学学会（1944）、美国艺术与科学院国际荣誉成员（1948）
- 命名纪念：Oxford 的 Robinson Close；Liverpool 的 Robert Robinson Laboratory；Manchester 的 Sir Robert Robinson Laboratory of Organic Chemistry；Sydney 的 Robinson and Cornforth Laboratories
- 期刊：创办 *Tetrahedron*（1957，Pergamon Press，50 位编辑）

## 10. 终审清单

- [ ] 生卒 1886-09-13 / 1975-02-08，享年 88，出生地 Rufford House Farm（Chesterfield 附近）、去世地 Great Missenden
- [ ] 1947 独享、理由口径 "plant dyestuffs (anthocyanins) and alkaloids" 准确
- [ ] 托品酮 1917、苯环加圈 1923（圣安德鲁斯）、士的宁 1946、*Tetrahedron* 1957 年份链准确
- [ ] 博士生只收 infobox 六人；metadata-only 三人不入库
- [ ] 皇家学会第 48 任主席（1945–1950）方向准确
- [ ] 两段婚姻齐全；棋局"输给 Good"方向准确
- [ ] 全书无杜撰引语
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误，溢出达标

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Robert_Robinson_organic_chemist/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 肖像核对（缺图用装饰圆占位并注记）
- [ ] 国籍：封面顶部明示英国
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
