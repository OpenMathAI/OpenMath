# Christopher Clavius（克里斯托弗·克拉维乌斯）立传提示词

> qid=Q76728 · 1538-03-25 – 1612-02-06 · 德国耶稣会数学家、天文学家 · 16–17 世纪之交（格里高利历改革核心角色）
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Christopher_Clavius/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 `images/clavius_portrait.jpg` + `draw=coveraccent!50` 细边框 + 姓名小字注（★ PORTRAITS.md 核定：克拉维乌斯**有**传世肖像，Rijksmuseum 藏版画像 RP-P-OB-38.439；`images.txt` 三图分别为《天球论注释》1585 版书影、《Refutatio》书影与月球 **Clavius 环形山**照片（330px `Clavius_001.jpg`），**均非肖像**，只能作叙事插图）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧肖像 `clavius_portrait.jpg` + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰；**师承 page.md 无载（Nunes 仅「可能接触」）→ 该格写「—（无载）」，禁填人名**。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应「历法之轮 / 天球」的母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Christopher Clavius, SJ（本名不详，学者推测或为 Christoph Clau / Klau；Clavius 或为德语 Schlüssel「钥匙」的拉丁化——clavis 拉丁语即钥匙；中文惯称：克里斯托弗·克拉维乌斯）
- **生卒**：1538-03-25 生于班贝格（Bamberg，巴伐利亚，神圣罗马帝国；正文生年两说 1538 或 1537，infobox 取 1538-03-25）→ 1612-02-06 逝于罗马（教宗国），享年 73
- **国籍**：德国（German；metadata nationality: Germany；出生地属神圣罗马帝国，卒地属教宗国）
- **身份**：耶稣会士（SJ）、数学家、天文学家、物理学家（page.md 定性 "a Jesuit German mathematician and physicist"）；Collegio Romano 数学家之首（head of mathematicians）、数学公开教授、高等数学学院（Academy of Mathematics）教学与研究主任（正式至 1610，非正式至 1612）
- **家庭**：page.md 无载（禁写）
- **教育轨迹**：1555 年入耶稣会 → 就读葡萄牙科英布拉大学（University of Coimbra，**可能**与数学名家 Pedro Nunes 有所接触——page.md 措辞 "it is possible"）→ 赴罗马入耶稣会 Collegio Romano 学神学 → 1564 年晋铎
- **导师**：page.md 无载（Nunes 仅为「可能接触」，非导师）
- **研究领域**：数学（mathematics）、天文学（astronomy）——page.md infobox Fields 明载两门；metadata field_of_work 仅 mathematics，以 page.md 为准补 astronomy

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **格里高利历改革的核心角色**：梵蒂冈委员会成员，接受 Aloysius Lilius 提出的历法方案；1582 年经教宗格里高利十三世下令在天主教国家采纳，即今日全球通用的格里高利历。
2. **历法的辩护者与阐释者**：先后写下历法改革的辩护与解释著作（1588 *Novi calendarii romani apologia*、1603 *Romani calendarii a Gregorio XIII P.M. restituti explicatio*），含**对 Lilius 工作的郑重致意**（emphatic acknowledgement）。
3. **晚年欧洲最受尊敬的天文学家**：page.md 定性——"in his last years, he was probably the most respected astronomer in Europe"。
4. **教科书影响半个多世纪**：其天文学教科书在欧洲内外被用于天文教育**超过五十年**；《天球论注释》1570–1618 年间至少 16 版，本人七次修订且每次大幅扩充。
5. **1572 新星的独立定位**：1585 版注释中**独立于第谷·布拉赫**将 1572 新星定位于恒星天（仙后座），且对所有观测者位置相同——意味着它远在月球之外，「天不变」教条被证伪。
6. **数学课程的孤军奋战**：在数学常被哲学家（乃至同会士 Benito Pereira 等人）讥讽的时代，**几乎凭一己之力**让耶稣会采纳了严格的数学课程。
7. **Clavius 之律**：逻辑学中 consequentia mirabilis（由命题否定的不一致推出命题为真）以他命名——Clavius' Law。
8. **西方最早使用小数点的人之一**：1593 年《星盘》（*Astrolabium*）三角函数表中使用小数点。
9. **与伽利略的通信与 1611 之会**：与伽利略常年通信讨论证明与理论；1611 年伽利略到罗马拜访，讨论望远镜新观测——克拉维乌斯当时已接受新发现为真，但对月球山峦存疑、并称透过望远镜看不见四颗木星卫星。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（教廷深蓝） | `#16324F` | 罗马学院 / 教廷历法改革的庄重 |
| 强调色（历法金） | `#C9A227` | 1582 年历法改革的划时代 |
| 分类色 1（历法改革 — 古铜） | `#8B5A2B` | 格里高利历 / Lilius 方案 |
| 分类色 2（天文学 — 深青） | `#1B4D6B` | 《天球论注释》/ 1572 新星 |
| 分类色 3（欧几里得 — 青绿） | `#0E7C7B` | 《几何原本十五卷》注释 |
| 分类色 4（耶稣会教育 — 玫红） | `#7A1E28` | 数学学院 / 课程改革 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「天球层 / 历法之轮」的圆周之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**The Flow of Time**（alex-productions，本地文件 `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`）
- **风格定调**：**时间感 / 纪录片 / 沉稳**（为全世界重排时间的人）
- **匹配理由**：
  - 「数学史时间线」场景标签与历法改革主题**字面级契合**——格里高利历就是对时间之流的制度性驯服；
  - 「纪录片、沉稳」匹配其耶稣会士的庄重气质与半个世纪的教科书影响力；
  - 与组内 Ferrari（Savage）、Bombelli（Mirage）互不重复。
  - 时长需 ≥ 13 页 × 7 秒 ≈ 91 秒，ffmpeg `-shortest` 自动对齐。

## 4. Slide 规划（统一 14 页制：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年与教育 + 7 贡献页 + 荣誉与传承 + 终章）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格。
> 页结构（14 页，TEMPLATE_GUIDE §2 标准制）：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年与教育 + 7 个核心贡献页 + 荣誉 + 终章。

1. **共享封面**（`\openmathslide`）：`\input{../../cover/openmath_page.tex}`，不改
2. **人物封面**（`\titleslide`）：大标题「格里高利历的守护者」+ 克里斯托弗·克拉维乌斯 1538–1612 + 右上肖像 `clavius_portrait.jpg` + 国籍行「德国」+ 底部三要素状态栏 + 四分类 badge
3. **身份信息页**（`\profileslide`，★ 必做）：左肖像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
4. **克拉维乌斯的一生：时间线**（`\timelineslide`，竖轴 8 节点）：1538-03-25 班贝格生 → 1555 入耶稣会 → 科英布拉大学 / 1561 到罗马 / 1564 晋铎 → 1570《天球论注释》初版 → 1582 格里高利历颁行 → 1593《星盘》小数点 → 1611 伽利略来访 → 1612-02-06 卒于罗马（仅写 page.md 有年份的节点）
5. **早年与教育**（`\earlyslide`）：本名不详（Christoph Clau/Klau、Schlüssel 拉丁化说）；生年 1538/1537 两说；1555 入耶稣会；科英布拉大学求学（可能接触 Pedro Nunes）；Collegio Romano 学神学；1564 晋铎（师承 page.md 无载，禁写）
6. **格里高利历改革**（贡献页，表格 + 公式框）：Lilius 提出方案、梵蒂冈委员会（发明权属 Lilius，禁写克拉维乌斯「发明」）、Reinhold 普鲁士星表、1582 颁行；1588 辩护 / 1603 阐释著作；对 Lilius 的郑重致意
7. **欧几里得注释**（贡献页，表格 + 公式框）：*Euclidis Elementorum Libri XV*（罗马 1574；科隆 1591；1627 版）
8. **《天球论注释》教科书**（贡献页，表格 + 公式框）：Sacrobosco《天球论》注释，1570–1618 间至少 16 版、本人七次修订且每次大幅扩充；教科书影响天文教育 50 余年
9. **1572 新星：天界可变的证伪**（贡献页，表格 + 公式框）：1585 版注释中**独立于** Tycho Brahe 将 1572 新星定位于恒星天（仙后座），各观测者位置相同 → 必在月球之外
10. **地心说的坚守与伽利略**（贡献页，表格）：坚守地心模型、反对日心说但承认托勒密模型有困难；与伽利略常年通信；1611 来访、接受望远镜新发现为真，但对月球山峦存疑、未见四颗木星卫星
11. **数学课程的改革**（贡献页，表格）：1580 *Ordo servandus* 课程方案（光学 / 静力学 / 天文 / 声学）；1580 方案被拒（仍获数学教授头衔）、1586 再试遭哲学家反对；1593/94 学院官方化；Grienberger 1595 信载门下约十名学生；1610 正式卸任
12. **数学贡献：Clavius 之律与小数点**（贡献页，表格 + 公式框）：consequentia mirabilis（由命题否定的不一致推出其为真）；1593《星盘》三角表中的小数点（西方最早之一）
13. **荣誉与身后**（荣誉页，表格）：月球环形山 Clavius；小行星 20237 Clavius；教科书影响 50 余年；《2001 太空漫游》Clavius 基地趣闻；死后学院旋即式微（1615 后名录无数学家）
14. **终章**（`\closingslide`）：73 岁、「可能是欧洲最受尊敬的天文学家」的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **★ 历法发明权**：格里高利历方案**发明者是 Aloysius Lilius**，克拉维乌斯是**委员会成员 + 辩护阐释者**——禁写克拉维乌斯「发明」格里高利历；须写明其著作含对 Lilius 的郑重致意（emphatic acknowledgement）。
- **★ 生年两说**：正文 "born in Bamberg in either 1538 or 1537"；infobox 与 metadata 均 1538-03-25——**取 1538-03-25**，§1/封面如需说明可注「或 1537」。
- **★ 本名不详**：Christoph Clau/Klau 为学者推测、Clavius 或为 Schlüssel 拉丁化——全部用「推测/或为」措辞，禁写成本名定论。
- **Nunes 接触**：page.md 措辞 "it is possible that he had some kind of contact"——**仅可能、非师承**，禁建 advisor-student 关系（metadata 亦无），叙事用「可能有所接触」。
- **与 Tycho Brahe**：新星定位系 "**independently** of Tycho Brahe"——禁写成合作、竞赛或互引关系。
- **与 Copernicus**：他反对日心模型但**承认托勒密模型存在问题**——两面表述，禁简化为「顽固反对新天文学」或「暗中支持哥白尼」。
- **★ 1611 会见伽利略的口径**：page.md 载他 "had by that time accepted the new discoveries as genuine" **同时** "retained doubts about the reality of the mountains on the Moon" 且 "said he could not see the four Jupiter's satellites"——「接受新发现为真」与「两点存疑」并列，禁写成「全盘接受」或「全盘拒绝」。
- **与伽利略通信**：page.md 明载 "often shared correspondence... discussing proofs and theories"，并可能分享学院逻辑课笔记助其论证（措辞 "It is likely"）——通信为事实、「分享笔记助论证」为推测措辞须保留。
- **Pereira 之争**：Benito Pereira 系「讥讽数学的哲学家/同会士」代表——controversy 口径为**数学课程之争**，非私人恩怨，禁加无载情节。
- **Scaliger 之争**：*Refutatio cyclometriae Iosephi Scaligeri*（Mainz 1609）系驳议著作——controversy 仅写「著书驳斥其化圆测法」，Scaliger 生平勿展开。
- **学生人数**：仅 Grienberger 1595 信载「当时约十人」，具体名单无载——**禁列学生名单**；metadata doctoral_student（Giuseppe Biancani）为 metadata-only，不入库。
- **学院时间线**：学院在克拉维乌斯 1561 到罗马前已非正式存在多年；1580 方案被拒但获数学教授头衔；1586 再试被哲学家反对；1593 或 1594 非官方课程结束、学院正式化；1610 正式卸任、非正式延续至 1612；死后 1615 名录再无数学家——年份细节勿混。
- **metadata employer Collegio Massimo, Naples** 为 metadata-only——不入机构清单。
- ** Reinhold**：普鲁士星表只是计算工具——不入关系，叙事一句带过。
- **★ 肖像口径（Review-1 更正）**：PORTRAITS.md 核定克拉维乌斯**有**传世肖像 → 用 `images/clavius_portrait.jpg`（Rijksmuseum 藏版画像 RP-P-OB-38.439，图注「Clavius 版画像（Rijksmuseum 藏 RP-P-OB-38.439）」）；`images.txt` 三图（《天球论注释》1585 书影、《Refutatio》书影、月球 Clavius 环形山照片）**均非肖像**，只能作叙事插图，严禁充当头像。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76728 | 待写入 |
| name_zh | 克里斯托弗·克拉维乌斯 | 待写入 |
| name_en | Christopher Clavius（metadata label） | 待写入 |
| birth_date | 1538-03-25 | 待写入 |
| death_date | 1612-02-06 | 待写入 |
| nationality | Germany（+ Holy Roman Empire, era_note historical） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / astronomy | 待写入 |
| has_biography | false（本次只入库社会关系，Beamer 立传待做） | 待写入 |

## 7. 社会关系入库清单

- **通信 / 同行**：Galileo Galilei（collaborator——常年通信讨论证明与理论，1611 伽利略来访；★ 库内已有记录命中，name_en 用规范名 "Galileo Galilei"）
- **协作**：Aloysius Lilius（collaborator——梵蒂冈历法委员会采纳其方案并为之辩护）
- **通信 / 同行**：Christoph Grienberger（collaborator——1595 来信，其时克拉维乌斯门下约十名学生）
- **争议**：Benito Pereira（controversy——哲学派同会士贬抑数学、反对数学课程官方化）
- **争议**：Joseph Justus Scaliger（controversy——1609《化圆测法驳议》驳其圆周率测法）
- **不入库**（page.md 无载或仅可能）：Pedro Nunes（"possible" 接触，非导师）、Erasmus Reinhold（仅用其星表）、Tycho Brahe（独立定位，无交往）、Copernicus（仅学说对立，无私人关系，且卒于 1543）、Giuseppe Biancani（metadata-only doctoral_student）、Sacrobosco（注疏对象，中世纪人）、教宗格里高利十三世（颁令者，无对应关系类型）

## 8. 奖项清单

- 无（page.md 无任何奖项记载）
- 荣誉纪念（非奖项，可入叙事不入 awards 表）：月球环形山 Clavius；小行星 20237 Clavius

## 9. 机构清单

- 教育：University of Coimbra（科英布拉大学）；Collegio Romano / Roman College（罗马学院，耶稣会体系——学神学，metadata educated_at 明载）
- 任职：Collegio Romano / Roman College（数学公开教授、数学家之首、高等数学学院主任——正式至 1610、非正式至 1612；page.md "head of mathematicians at the Collegio Romano"）
- 任职：Society of Jesus（耶稣会，1555 年入会——page.md 明载，按任职口径入库）
- 不入库：Collegio Massimo, Naples（metadata-only）

## 10. 终审清单

- [ ] 生卒 1538-03-25（或 1537 注记）/ 1612-02-06，享年 73，班贝格 → 罗马
- [ ] 历法「Lilius 发明、克拉维乌斯委员会采纳并辩护」，禁写克拉维乌斯发明
- [ ] 新星「独立于 Tycho」；托勒密困难两面表述；1611 会见「接受为真 + 两点存疑」并列
- [ ] Nunes 仅「可能接触」，禁写导师
- [ ] 本名均用推测措辞；学生仅「约十人」，禁列名单
- [ ] 通信（Galileo / Grienberger）与争议（Pereira / Scaliger）类型准确
- [ ] 肖像用 `clavius_portrait.jpg`（Rijksmuseum 藏版画像），书影 / 环形山图仅作插图
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像位 + 国籍行 + 气泡背景 + 品牌 OpenMathAI

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Christopher_Clavius/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认 `clavius_portrait.jpg` 落地（Rijksmuseum 藏版画像 RP-P-OB-38.439）；环形山 / 书影仅作插图
- [ ] **国籍**：封面顶部徽章明示德国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 "probably the most respected astronomer in Europe"）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Bombelli / Viète / Napier 篇）格式对齐；与物理学家侧伽利略相关篇目（若有）口径互查

## 12. Review-1 事实终审记录（2026-09-29）

- 核对基准：`pages/Christopher_Clavius/page.md`（+ metadata.json）
- 生卒 / 享年：1538-03-25 生于班贝格（Bamberg, Bavaria, Holy Roman Empire）→ 1612-02-06 卒于罗马（Papal States），享年 73（page.md "aged 73"）；正文另载生年「1538 或 1537」两说，infobox 与 metadata 均取 1538-03-25 → 取 1538-03-25，可注「或 1537」
- 国籍口径：德国（metadata nationality: Germany；page.md "Jesuit German mathematician and physicist"）→ 封面国籍行「德国」；出生地属神圣罗马帝国、卒地属教宗国，按 historical 注明
- 肖像结论：**有**传世肖像 → `clavius_portrait.jpg`，图注「Clavius 版画像（Rijksmuseum 藏 RP-P-OB-38.439）」（PORTRAITS.md 第 9 条，更正原提示词「无真肖像」断言）；`images.txt` 三图（1585《天球论注释》书影、《Refutatio》书影、月球 Clavius 环形山照片）均非肖像，仅作插图
- 引语核对：本篇无成段直接引语，全文转述；页内短引均逐字核过 page.md：① "probably the most respected astronomer in Europe"（page.md："he was probably the most respected astronomer in Europe"）✅；② "independently of Tycho Brahe"（page.md "located (independently of Tycho Brahe) the nova from 1572"）✅；③ "emphatic acknowledgement of Lilius' work"（§2 转述为「郑重致意」）✅；④ "it is possible that he had some kind of contact"（Nunes，仅可能）✅；⑤ "almost single-handedly" ✅
- 本轮修正：① §0-1/§0-3/§4/§5/§10/§11 共 6 处肖像条款由「无真肖像 / 装饰圆占位」改为使用 `clavius_portrait.jpg`（依 PORTRAITS.md 权威结论），§0-3 同时补「师承格写「—（无载）」」；② §4 重排为 14 页制：补入共享封面为第 1 页、人物封面为第 2 页、早年与教育合并为第 5 页（原「谜样的早年」+「科英布拉与罗马」），并将原「《天球论注释》与 1572 新星」拆为第 8、9 两贡献页，使贡献页共 7 页（页数结构对齐 TEMPLATE_GUIDE §2 标准制）；时间线收敛为 **8 节点**（1538 → 1555 → 科英布拉/1561/1564 → 1570 → 1582 → 1593 → 1611 → 1612）；③ §4 原「方案两度被拒」改为「1580 方案被拒（仍获数学教授头衔）、1586 再试遭哲学家反对」——page.md 仅 1580 明确 denied，1586 为 opposition；④ 历法条目内加注「发明权属 Lilius，禁写克拉维乌斯发明」，与 §5 呼应
- 遗留不确定项：① 《天球论注释》初版年份 page.md 只载「1570–1618 间至少 16 版」，「1570 初版」为最早版本锚点推断，若定稿需保守可写「1570 年代起」；② 生年 1537 说 page.md 无旁证，仅作注记；③ 卒月日之外的晋铎/到罗马月份 page.md 无载，不写；④ 曲目 The Flow of Time 未查同世纪撞曲（按纪律仅记录不改）；⑤ metadata notable_work 含 *Geometria practica*，page.md 未载，不写入叙事

## 13. 立传期执行记录（Beamer，2026-09-29，math16-c）

- 产出：`Christopher_Clavius_zh.tex` / `.pdf`，**14 页**（与 §4 一致：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年与教育 + 7 贡献页 + 荣誉与身后 + 终章）；`make distclean && make` **0 error**、Overfull 仅 1 处 **0.48pt**（<10pt，图注换行），体积 375 KB。
- 肖像：用 `images/clavius_portrait.jpg`（Rijksmuseum 藏版画像 RP-P-OB-38.439），封面图注「Clavius 版画像 · Rijksmuseum 藏」、身份页图注「Clavius 版画像（Rijksmuseum 藏 RP-P-OB-38.439）」；《天球论注释》1585 书影、《Refutatio》书影、Clavius 环形山照片均未使用。
- 硬口径落实：历法页明写「梵蒂冈委员会采纳 Lilius 提出的方案」「发明权属 Lilius」，未写克拉维乌斯「发明」格里高利历；生卒 1538-03-25 / 1612-02-06（享年 73），生年「或 1537」仅作注记；师承格写「—（page.md 无载）」；Nunes 仅「可能有所接触」；新星「独立于 Tycho Brahe」；1611 伽利略来访写「接受新发现为真 + 对月球山峦存疑、看不见四颗木星卫星」并列。
- 与 `page.md` **无事实冲突**，未产生 §12 之外的修正。
