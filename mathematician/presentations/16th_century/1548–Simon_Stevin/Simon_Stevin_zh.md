# Simon Stevin（西蒙·斯蒂文）立传提示词

> qid=Q23696 · 1548 – 1620 · 佛兰德数学家、物理学家与工程师 · 16–17 世纪之交（跨世纪）
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Simon_Stevin/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。Wikipedia infobox 本体无真实肖像，`images.txt` 全部为插图/雕像/书影（风帆车版画 1649、Bruges 广场雕像 1847 等）——**无真实肖像，用装饰圆 `\faIcon{user}` 占位**；可选以 Bruges 雕像照片作「纪念像」插图页（勿当肖像）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 佛兰德 · 荷兰共和国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、别名 Stevinus、国籍、出生地、职业、教育、代表著作、核心领域。事实取自 Wikipedia infobox 与 page.md，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），呼应「斜面绳圈（Epitaph of Stevinus）/ 风车 / 围圈小数记法」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Simon Stevin（荷兰语发音 [ˈsimɔn steːˈvɪn]），拉丁名 **Simon Stevinus**，别称 **Stevinus**；中文惯称：西蒙·斯蒂文。部分涉及其父的文档拼写 *Stevijn*（16 世纪荷兰语常见拼写移变）
- **生卒**：1548 生于 Bruges（Habsburg Netherlands）→ 1620 逝于 The Hague（或 Leiden），享年 71–72；**page.md 明载：确切出生日期与死亡日期、地点均不确定——只写到年**
- **国籍**：佛兰德人（Flemish，County of Flanders）；生于 Habsburg Netherlands（哈布斯堡尼德兰），亡于 Dutch Republic（荷兰共和国）——两个历史政权均需 era_note
- **身份**：数学家、科学家、音乐理论家（music theorist）、工程师（水利/军事/堡垒工程）、会计师、制图师、测量员；Prince Maurice 的**总顾问与导师**
- **家庭**：母 Cathelijne（Ypres 富家之女，其父 Hubert 为 Bruges 市民 poorter；后嫁丝绸/地毯商人 Joost Sayon，进入加尔文派家庭——斯蒂文很可能在加尔文信仰中长大）；父名字无载；1610 或 1614 结婚（两说并存），育有四子女；去世时留下遗孀与两个孩子
- **教育轨迹**：
  - 推测在家乡 Bruges 受拉丁学校教育（"likely educated at a Latin school"）
  - 1571 离开 Bruges，先在 Antwerp 当商行文书（merchant's clerk）
  - 1571–1577 间游历 Prussia、Poland、Denmark、Norway、Sweden 等北欧地（可能拉长）
  - 1577 返 Bruges 任市秘书（city clerk，1577–1581，在 Brugse Vrije 的 Jan de Brune 办公室）
  - 1581 迁 Leiden；**1583-02-16 以 "Simon Stevinus Brugensis" 注册 Leiden University**，注册在册至 1590，**未毕业**
- **导师**：page.md 无载（**禁写任何导师**）
- **研究领域**：数学、力学、流体静力学、三角学、音乐理论、会计学、军事工程、水利工程

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **《De Thiende》（1585，法译 La Disme）**：35 页小册，**在欧洲确立十进小数**；宣称十进币制、度量衡与权制的普遍推行「只是时间问题」——影响后世小数点记法体系（尽管其本人记法笨重）。
2. **围圈指数记法**：以带圈数字标十分幂次（184⓪5①4②2③9④0 表 184.54290），同一符号兼用于代数幂，不避分数指数——χ 加权下标思想的先声（页面对照表可做公式框）。
3. **实数连续统**：据 van der Waerden，斯蒂文消除了「数」限于整数（Euclid）或有理分数（Diophantus）的古典限制——**实数构成连续统**，其一般实数概念为后世科学家默然接受；近研究认为其在实数发展中的作用被低估。
4. **多项式介值定理**：先于柯西证明多项式的介值定理，用十等分区间的 divide-and-conquer 程序。
5. **一般二次方程解（1594《Arithmetic》）**：把 Brahmagupta（印度，近千年前）已知的一般解带到西方世界。
6. **静力学：Epitaph of Stevinus**：以「绳圈等距重物」图证明斜面上力平衡条件（所需重物与斜边长成正比）——Dijksterhuis 指出其证明借永动机归谬、**直觉使用了能量守恒原理**（早于其明确表述）。
7. **流体静力学：静水佯谬（hydrostatic paradox）**——液体压强与容器形状、底面积无关，只取决于高度；并给出侧壁任意部分的压强度量；**首个用月球引力解释潮汐**。
8. **1586 Delft 塔实验**：演示不同重量物体下落加速度相同。
9. **等程律（equal temperament）**：西方首个与 2 的十二次方根相联系的表述，见于未完成手稿 *Van de Spiegheling der singconst*（约 1605，死后三百年 1884 年才出版）；计算精度不足、弦长数字差一两个单位；受鲁特琴演奏家/理论家 Vincenzo Galilei（伽利略之父）著述启发。
10. **荷兰科学语言运动**：把数学术语译成荷兰语——wiskunde（数学）、natuurkunde（物理）、scheikunde（化学）、sterrenkunde（天文）、meetkunde（几何）——使荷兰语成为少数数学词汇非希腊/拉丁借词的欧洲语言；目标「恢复智慧的第二时代」。
11. **工程实践**：风车改进（慢轮 + 齿轮啮合系统，抽水效率三倍，1586 专利）；land yacht 风帆车（约 1600 与 Maurice 等 26 人乘于 Scheveningen–Petten 海滩，速度胜马）；waterstaet 总监（1592 起）；国家陆军军需总监（quartermaster-general）；在 Leiden 大学创办工程学校；Moers 堡垒设计（1604）。
12. **Prince Maurice 的导师与总顾问**：Willem van Oranje 遇刺后，斯蒂文成为毛里茨亲王的首席顾问与导师（principal advisor and tutor），亲王屡屡问计；并为其推行国家层面的**非个人账户（impersonal accounts）簿记**，亦荐于法国重臣 Sully。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（低地国海蓝） | `#175873` | 尼德兰水乡、北海与风车 |
| 强调色（风车琥珀） | `#D08C2E` | 工程实用、砖石与风车翼 |
| 分类色 1（十进小数 — 墨青） | `#0B5351` | De Thiende / 围圈记法 |
| 分类色 2（静力学·流体 — 石板蓝） | `#3E5F8A` | Epitaph of Stevinus / 静水佯谬 |
| 分类色 3（音乐理论 — 紫） | `#6B4E9B` | 等程律 / 十二律 |
| 分类色 4（工程与荷兰科学语言 — 橄榄绿） | `#5B7553` | 风车/风帆车/堡垒 + wiskunde 新词 |
| 背景 | `#F5F7F6` | 浅灰绿 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「斜面绳圈 / 风车翼 / 围圈数字」母题。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**Expedition**（Alex-Productions，`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`，标签：高受众 / 探索 / 史诗）
- **风格定调**：**探索 / 远征 / 实用科学的行动感**
- **匹配理由**：
  - 斯蒂文一生自带「远征」结构：1571–1577 北欧游历（Prussia/Poland/Denmark/Norway/Sweden）、海滩风帆车疾驰、军需总监随军、堡垒与港口（De Havenvinding）定位——**探索/史诗**气质与内容严丝合缝
  - 「Expedition」的推进感匹配其「理论→应用」的工程节奏（数学、物理、水利、军事工程全线落地）
  - 与本批次另一人 François Viète 的 **Cinematic Experience**（电影感/高张力）互不重复
- 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「十进小数与静力学 · 低地国家的实用科学大师」+ Simon Stevin 1548–1620 + 右上头像（装饰圆）+ 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 别名 Stevinus / 国籍 / 出生地 / 职业 / 教育 / 代表著作 / 核心领域）
3. **斯蒂文的一生：时间线**（`\timelineslide`）：1548 Bruges 出生 → 1571 离乡（Antwerp 文书、北欧游历）→ 1577–81 Bruges 市秘书 → 1583-02-16 注册 Leiden 大学 → 1585 De Thiende → 1586 静力学/流体静力学/Delft 实验/风车专利 → 1592 waterstaet 总监 → ~1600 风帆车 → 1605–08 Wiskonstighe Ghedachtenissen → 1612 定居 The Hague → 1620 去世
4. **早年与北欧远行**（`\earlyslide`）：Bruges、加尔文家庭、Antwerp 商行文书、北欧之行、市秘书、为避宗教迫害离乡（推断口径）
5. **《De Thiende》1585：十进小数**（核心贡献页，表格 + 公式框）：35 页小册、La Disme、围圈记法对照表（184⓪5①4②2③9④0）、献词「祝观星者、测量者…好运」、「一切运算化为整数四则」
6. **实数连续统与介值定理**（核心贡献页，表格 + 公式框）：van der Waerden 评价、十等分 divide-and-conquer、先于 Cauchy
7. **代数与三角**（核心贡献页，表格）：1594《Arithmetic》一般二次方程解（Brahmagupta 千年后再传西方）、《De Driehouckhandel》三角学、多面体框架平面展开、稳定/不稳定平衡区分
8. **静力学：Epitaph of Stevinus**（核心贡献页，表格 + 示意图）：绳圈等距重物斜面证明、力分解、Dijksterhuis「直觉使用能量守恒」
9. **流体静力学、落体与潮汐**（核心贡献页，表格）：静水佯谬（压强只依赖高度）、1586 Delft 塔实验（不同重量同加速度）、首个月球引力潮汐说
10. **音乐理论：等程律**（表格 + 公式框）：Van de Spiegheling der singconst（约 1605，1884 出版）、十二次方根、计算差一二单位、Vincenzo Galilei 之源
11. **荷兰科学语言运动**（表格）：wiskunde / natuurkunde / scheikunde / sterrenkunde / meetkunde 新词表、「智慧的第二时代」、单音节词经验论证
12. **工程与军事**（表格）：风车改进与 1586 专利（效率三倍）、waterstaet 总监（1592）、军需总监、Leiden 工程学校、Moers 堡垒（1604）、Castrametatio（1617）
13. **与 Prince Maurice：导师与总顾问**（表格）：Leiden 结识 Willem the Silent 次子、1592 起的信任岗位、非个人账户簿记（荐于 Maurice 与 Sully）、身后纪念开篇
14. **终章**：Bruges Simon Stevinplein 雕像（1847 落成，像座刻斜面平衡证明）、Stevin Prize（2018）、RV Simon Stevin 科考船（2012）——「理论与应用之桥」的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **生卒只到年**：page.md 原文 "The exact birth date and the date and place of his death are uncertain"——**禁写具体月日**；卒地 **Leiden 或 The Hague 两说并存**（metadata 取 The Hague，yaml 填 1620 年即可）；享年 71–72；metadata `date_of_birth: 1548-00-00` 无月日噪声，与本裁定一致。
- **小数优先权**：十进小数早已见于 al-Uqlidisi（952）与 Al-Kashi（1427《Miftah al-Hisab》系统发展）——**只写「在欧洲确立/其日常使用之确立」（page.md 原口径 "nobody established their daily use before Stevin"），禁写「发明小数」**；"He was thought to have invented... until the middle of the 20th century" 的翻案史可如实交代。
- **小数点非其发明**：小数点见于 Pitiscus 三角表（1612）、被 Napier 采纳（1614/1619）；斯蒂文自己的围圈记法 page.md 评为 "rather unwieldy"（笨重）——勿美化其记法。
- **等程律计算精度不足**（弦长差一两个单位）——如实写；勿写「精确确立等程律」；1884 年才出版的手续可写。
- **介值定理**：为**多项式**证明、anticipating Cauchy——禁写成「一般介值定理的首证」。
- **二次方程**：Brahmagupta 近千年前已载——口径为「把一般解带到西方世界」（"brought to the western world for the first time"）。
- **Delft 塔实验**：page.md 只说 1586 demonstrated 不同重量同加速度——**禁比附伽利略比萨塔传说**（page.md 无载伽利略）。
- **Varignon 语句存疑**：page.md 有 "He demonstrated the resolution of forces before Pierre Varignon" 一句，但 Varignon（1654–1722）晚斯蒂文一代、年代倒挂——**不入库、正文亦谨慎略过或加「据维基页」注**。
- **宗教口径**：斯蒂文「很可能是加尔文派」（从其后来受 Maurice 信任推断）——用推断口径，勿坐实；1577 返 Bruges 与 1576 宗教宽容令的关联用 "may/could explain" 语气。
- **婚姻与子女**：结婚年份**两说 1610/1614 并写**；妻子**无姓名记载，禁写姓名**；四个子女无具名——均不入库。
- **姓名**：父辈文档拼写 Stevijn；大学注册名 Simon Stevinus Brugensis——aliases 可列，勿混用主名。
- **国籍 era**：生于 Habsburg Netherlands、卒于 Dutch Republic，均为历史政权——yaml 两条 nationality 均加 `era_note: historical`；封面口径「佛兰德 · 荷兰共和国」。
- **引语白名单**（其余一律禁编引语）：①De Thiende 献词 "Simon Stevin wishes the stargazers, surveyors, carpet measurers, body measurers in general, coin measurers and tradespeople good luck."；②"[this text] teaches us all calculations that are needed by the people without using fractions..."；③van der Waerden 对其实数概念的转述（注明转述）。其余禁编。
- **无奖项记载**（§8 写无；Legacy 三项为纪念命名非奖项，勿混淆——Stevin Prize 2018 是荷兰 NWO 现代奖，可入 Legacy/终章，不入「斯蒂文所获奖项」）。
- ** minYears：land yacht 年份写「约 1600」；风车效率「三倍」（page.md "improved threefold"）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q23696 | 待写入 |
| name_zh | 西蒙·斯蒂文 | 待写入 |
| name_en | Simon Stevin | 待写入 |
| birth_date | 1548 | 待写入（年，月日 page.md 明载不确定） |
| death_date | 1620 | 待写入（年，同上） |
| nationality | Habsburg Netherlands / Dutch Republic（均 era_note: historical） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / mechanics / hydrostatics / music theory / hydraulic engineering / military engineering | 待写入 |
| has_social_data | 1 | 本次入库置 1 |
| has_biography | 0 | 本次仅入库社会关系，立传未做 |

## 7. 社会关系入库清单

- **学生**：Maurice, Prince of Orange（principal advisor and tutor——导师兼总顾问， Willem the Silent 遇刺后；亲王为其设 waterstaet 总监、军需总监等职位）；Isaac Beeckman（infobox Notable students，库内既有 stub id=1303）
- **思想影响**：Vincenzo Galilei（鲁特琴演奏家/音乐理论家，其著述启发了斯蒂文等程律手稿——influence，note 注明「著作启发」）
- **家庭**：母 Cathelijne（Ypres 富家之女，后嫁 Joost Sayon，加尔文派家庭）
- **不入库**：妻子（无名）、四子女（无名）、父（名字无载，仅拼写 Stevijn 线索）、Joost Sayon（继父，page.md 只载母再嫁）、William the Silent（Leiden 创办人、Maurice 之父，与斯蒂文无直接关系载）、Sully（簿记推荐对象，无对应类型）、Pierre Varignon（年代倒挂存疑句，见 §5）、W. Snellius（著作拉丁译者，无对应类型）、Luca Pacioli/Cardano（簿记可能来源，"may have been known" 推断）、al-Uqlidisi/Al-Kashi/Brahmagupta（思想先驱，跨时代过远不建 influence）

## 8. 奖项清单

- 无（page.md 无任何斯蒂文生前所获奖项记载；Legacy 的雕像/科考船/Stevin Prize 均为身后纪念）

## 9. 机构清单

- 教育：Leiden University（莱顿大学，1583-02-16 注册为 Simon Stevinus Brugensis，注册在册至 1590，未毕业）
- 任职：University of Leiden 工程学校（受 Maurice 委托创办，page.md 未给年份——入库不写年份）；其他职位（waterstaet 总监 1592、军需总监、Bruges 市秘书 1577–1581）为公职非学术机构，正文叙述、不入 institutions

## 10. 终审清单

- [ ] 生卒 1548 / 1620（均只到年，月日留白），享年 71–72，卒地两说 Leiden 或 The Hague
- [ ] 小数口径「在欧洲确立、日常使用之确立」而非「发明小数」；al-Uqlidisi/Al-Kashi 先行者有交代
- [ ] 围圈记法 "unwieldy"、小数点属 Pitiscus/Napier——不美化
- [ ] Epitaph of Stevinus + Dijksterhuis 能量守恒直觉口径忠实
- [ ] Delft 塔实验不比附伽利略；介值定理限多项式；二次方程口径「带到西方」
- [ ] 等程律计算精度不足如实写；Varignon 存疑句已回避
- [ ] 婚姻年份两说并写；妻子/子女/父无名不入库
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像（装饰圆）+ 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Simon_Stevin/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：无真实肖像——装饰圆占位；如用 Bruges 雕像图，图注必须写「纪念雕像」非肖像
- [ ] **国籍**：封面顶部徽章明示「佛兰德 · 荷兰共和国」
- [ ] **引语核对**：仅白名单引语，逐条在 page.md 找到原文
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次 François_Viète 及 17 世纪卷（Johann_Bernoulli）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
