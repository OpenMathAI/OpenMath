# Gerolamo Cardano（吉罗拉莫·卡尔达诺）立传提示词

> qid=Q184530 · 1501-09-24 – 1576-09-21 · 意大利文艺复兴数学家、医生、占星家（米兰公国） · 16 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Gerolamo_Cardano/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**Cardano 有真实肖像**：`images.txt` 收录 `Gerolamo_Cardano_(colour).jpg`（圣安德鲁斯大学数学与统计学院藏彩色像）与 Leone Leoni 1550-51 年双面徽章像——执行立传时优先彩色像；**本任务阶段不下载**，提示词只记录候选。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 意大利 · 米兰公国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名异体（Girolamo/Geronimo/Hieronymus Cardanus）、国籍、出生地、教育、主要著作、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），呼应「骰子 / 万向节圆环」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Gerolamo Cardano（意大利语亦作 Girolamo 或 Geronimo；法语 Jérôme Cardan；拉丁语 Hieronymus Cardanus）；中文惯称：吉罗拉莫·卡尔达诺
- **生卒**：1501-09-24 生于帕维亚（Pavia，米兰公国）→ 1576-09-21 逝于罗马（教皇国），享年 74
- **国籍**：米兰公国（Duchy of Milan，历史政权）；卒地罗马属教皇国
- **身份**：文艺复兴博学者（polymath）——数学家、医生、生物学家、物理学家、化学家、占星家、天文学家、哲学家、音乐理论家、作家、赌徒；写下逾 200 部科学著作
- **家庭**：父 Fazio Cardano（数学才华出众的法学家/律师，达·芬奇的密友）；母 Chiara Micheri；其为**私生子**；自述其母曾服多种堕胎药，"I was taken by violent means from my mother; I was almost dead."；其母临产前因鼠疫从米兰逃往帕维亚，另三个孩子死于疫病。1531 年娶 Lucia Banderini（1546 年卒），育有三子女：Giovanni Battista（1534）、Chiara（1537）、Aldo Urbano（1543）；Cardano 自述那是他一生最幸福的时光
- **教育轨迹**：1520 年入帕维亚大学（父望其学法律，他偏爱哲学与科学）；1524 年战事迫使帕维亚大学关闭，转入帕多瓦大学，1525 年获医学博士
- **导师**：page.md 无载——**禁写导师**
- **研究领域**：数学（代数、概率论先驱）、医学、自然哲学、机械发明、音乐理论

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **《Ars Magna》（1545）**：代数史里程碑——欧洲**第一个系统使用负数**；以**署名归功**的方式发表了他人解法：del Ferro 的三次方程解法与其学生 Ferrari 的四次方程解法；并承认虚数（imaginary numbers）的存在（虽不理解其性质）。
2. **Cardano–Tartaglia formula**：1539 年 Tartaglia 以诗体将缺项三次方程解法传给他（Tartaglia 后来声称他曾发誓不公开，并引发十年论战）；因 del Ferro 的解法更早，《大术》以 del Ferro 为首解者归名。
3. **二项式定理西传**：在《Opus novum de proportionibus》中引入二项式系数与二项式定理。
4. **概率论先驱**：《Liber de ludo aleae》（《论掷骰》，约 1564 年写成、1663 年出版）包含**第一个对概率的系统论述**（含出千技巧一节）；以掷骰定义赔率（有利/不利结果之比）、知晓独立事件乘法法则（但不确定该乘哪些值）。
5. **机械发明**：组合锁；三同心环万向节（gimbal，使罗盘/陀螺自由旋转）；带万向节的 Cardan shaft（传动轴，至今用于车辆）；二次曲线内旋轮线（hypocycloids，1570《De proportionibus》）衍生出「Cardano circles」，用于第一代高速印刷机；Cardan 齿轮机构；认为除天体外永动机不可能；1550 年引入密码书写工具 Cardan grille。
6. **蒸汽与真空**：《De Subtilitate》中关注蒸汽的物理性质、以冷凝造真空——史学上被视为蒸汽动力研究复兴的里程碑，是通向蒸汽机的早期思想环节。
7. **聋人教育先驱**：主张聋人有心智能力、应受教育，是最早提出聋人不必先学说话即可学习读写的人之一。
8. **苏格兰行医（1552）**：治愈被认为不治的圣安德鲁斯大主教 John Hamilton 失语症，获 1,400 金克朗酬金；爱丁堡 1562 年仍流传其"merry tales"轶闻。
9. **家庭悲剧与宗教裁判所**：长子 Giovanni Battista 1560 年因毒杀妻子被判斩首（Cardano 无力偿付赔偿金）；幼子 Aldo 赌徒窃财、1569 年被剥夺继承权；1570 年被宗教裁判所以异端罪名逮捕（《De rerum varietate》被指控，尤其「殉道者自戕行为由星象导致」的占星论与 1543 年发表的耶稣星盘），数月监禁、失博洛尼亚教席、弃绝后获释，全部非医学著作被列入《禁书目录》。
10. **罗马晚年**：获教皇格里高利十三世终身年金（先被庇护五世拒绝）、入皇家医师公会、完成自传《De vita propria》，1576 年卒于罗马；月球有以他命名的 Cardanus 环形山。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（文艺复兴紫） | `#4A2A6A` | 文艺复兴博学者 / 米兰宫廷的华贵 |
| 强调色（代数金） | `#C9A227` | 《Ars Magna》/ 代数的尊崇 |
| 分类色 1（代数 — 靛蓝） | `#2F4470` | 三次/四次方程、负数与虚数 |
| 分类色 2（概率 — 骰子红） | `#8C1515` | 《论掷骰》/ 概率论先驱 |
| 分类色 3（机械 — 青铜） | `#8A5A2B` | 万向节 / Cardan 轴 / 机械发明 |
| 分类色 4（医学 — 深绿） | `#1E5631` | 行医生涯 / 聋人教育 |
| 背景 | `#F6F5F8` | 浅灰紫白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「骰子点阵 / 万向节同心圆环」意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**Cinematic Experience**（Alex-Productions，本地文件 `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`）
- **风格定调**：**电影感 / 高张力 / 大开大合**（一生跌宕的全才）
- **匹配理由**：
  - Cardano 一生横跨代数巅峰（《大术》）、概率开创、机械发明、苏格兰王庭行医、丧子之痛与宗教裁判所——「电影感 / 高张力」正匹配其大起大落的戏剧弧线
  - 「大定理、章节高潮」标签匹配《Ars Magna》1545 这一代数史高光页
  - 本组三人（del Ferro / Tartaglia / Cardano）分别用 PAST / Lonesome / Cinematic Experience，互不重复
- 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「文艺复兴全才 · 《大术》与概率的黎明」+ Gerolamo Cardano 1501–1576 + 右上头像（彩色像或徽章像）+ 国籍行（意大利 · 米兰公国）+ 底部三要素状态栏（米兰公国 | 帕维亚/帕多瓦/博洛尼亚大学 | 《大术》/ 负数系统使用 / 概率先驱）+ 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名异体 / 国籍 / 出生地 / 教育 / 主要著作 / 核心领域）
3. **卡尔达诺的一生：时间线**（`\timelineslide`）：1501 帕维亚出生（私生子）→ 1520 帕维亚大学 → 1525 帕多瓦医学博士 → 1531 婚 → 米兰（数学教席+行医）→ 1541 米兰医师公会主席 → 1545《Ars Magna》→ 1552 苏格兰行医 → 1560 长子被斩 → 迁博洛尼亚任医学教授 → 1570 宗教裁判所 → 罗马晚年 → 1576-09-21 去世
4. **早年：私生子与瘟疫**（`\earlyslide`）：父 Fazio 与达·芬奇之交、母堕胎药自述与"violently taken"引语、鼠疫夺走三个兄姐、父望其学法律而他偏爱哲学与科学
5. **求学与行医**（核心贡献页，表格）：帕维亚→战乱闭校→帕多瓦 1525 医学博士；米兰医师公会因其好斗名声与私生出身拒收（1525 多次申请被拒）；在 Piove di Sacco 无照行医；获数学教席后执照到手、双线执业成为米兰最受追捧的医生之一；1536 辞教席；拒绝丹麦/法国国王与苏格兰王后邀约；1541 任米兰医师公会主席并会见查理五世
6. **《Ars Magna》1545（一）：三次方程**（核心贡献页，表格 + 公式框）：1539 Tartaglia 诗体传法（誓言争议，见 §5）；del Ferro 解法更早故归名首解；`ax³+bx+c=0` 缺项情形
7. **《Ars Magna》1545（二）：四次方程与数系扩张**（核心贡献页，表格 + 公式框）：Ferrari 四次方程解法署名发表；欧洲第一个系统使用负数；承认虚数存在（性质由同代 Bombelli 首次描述）；《Opus novum de proportionibus》引入二项式系数与二项式定理
8. **概率论先驱：《论掷骰》**（核心贡献页，表格 + 公式框）：约 1564 写成 1663 出版；赔率定义、独立事件乘法法则（存疑处照写）、出千技巧一节；赌徒与棋手的自筹生计
9. **机械发明**（核心贡献页，表格）：组合锁、三环万向节、Cardan 轴与万向节、Cardano circles 与高速印刷机、Cardan 齿轮、Cardan grille（1550）、永动机否定、蒸汽冷凝造真空
10. **自然哲学与音乐**（核心贡献页，表格）：两部《De Musica》音乐论著（微分音/木管史料）、12 声部经文歌 Beati estis（四重卡农）、两部自然科学百科、聋人教育主张、地质洞见（石化贝壳=海居山地，经 Lyell 引述）
11. **苏格兰行医 1552**（表格）：大主教 Hamilton 失语症治愈、1,400 金克朗、与 Casanatus 的争论、"merry tales"轶闻
12. **家庭悲剧与宗教裁判所**（敏感页，表格）：1560 长子斩首、1569 幼子被剥夺继承权、迁博洛尼亚任医学教授、1570 异端指控（占星论与耶稣星盘）、数月监禁失教席、弃绝获释、非医学著作入《禁书目录》
13. **罗马晚年与遗产**（表格）：格里高利十三世终身年金、皇家医师公会、自传《De vita propria》、1576 卒、Cardanus 月球环形山、后世文化回响（Thomas Browne / Manzoni / Forster，选一两条即可）
14. **终章**：74 岁、"最后一位文艺复兴全才式的数学家"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **生卒**：1501-09-24 生、1576-09-21 卒——metadata 死亡日有第二噪声值 `1576-09-20`，**以 09-21 为准**。
- **名字异体**：Gerolamo / Girolamo / Geronimo / Jérôme / Hieronymus 并存——正文统一用 Gerolamo Cardano，身份信息页列异体一次。
- **「发明权」谨慎**：**万向节（universal joint / Cardan joint）并非 Cardano 所描述**（page.md 明言）；Cardano's Rings（中国环）很可能早于 Cardano；gimbal 与 Cardan shaft 是他「部分发明并描述」（partially invented and described）——用词照 page.md 措辞，禁写「发明了万向节」。
- **三次方程叙事（与 Tartaglia 口径一致，敏感核心）**：Tartaglia 1539 年以诗体相授，"who later claimed that Cardano had sworn not to reveal it, and engaged Cardano in a decade-long dispute"——注意 page.md 的表述是 Tartaglia **后来声称**有誓言；del Ferro 解法更早，故《大术》以 del Ferro 为首解归名。两点并写，勿单侧化；细节主战场在 Tartaglia 篇，本篇从简。
- **虚数**：Cardano 只是**承认其存在**（acknowledged the existence），不理解其性质；首次描述性质的是 Bombelli——勿写 Cardano「创立虚数理论」。
- **概率论定位**：《论掷骰》是「第一个系统论述」且写于约 1564、出版 1663（身后 87 年）——表述勿写成「创立概率论」（奠基者通常归费马/帕斯卡，本页无载此说，禁写）；乘法法则「知晓但不确定该乘什么值」照写。
- **负数**：表述为「欧洲第一个系统使用负数」，勿泛化为「发明负数」。
- **长子之死**：Giovanni Battista 毒杀妻子（发现三子非亲生）→ 无力赔付赔偿金 → 判斩——按 page.md 客观简述，勿渲染；Cardano 将迁博洛尼亚部分归因于此与帕维亚学界积怨及不当行为指控。
- **宗教裁判所（敏感）**：指控内容（占星论、耶稣星盘《De Supplemento Almanach》1543）为 page.md 实载，客观陈述；「弃绝后获释，可能得罗马有力教会人士之助」照写 "probably"。禁展开反宗教叙事。
- **引语红线**：可用引语仅限 page.md 实载——① 自传 "I was taken by violent means from my mother; I was almost dead."；② Lyell《地质学原理》转述的《De Subtilitate》段落（系 Lyell 文字，注明转述来源）；③ Thomas Browne 书目评语与 Butler《Hudibras》打油诗（若用，注明系后世评家文字，非 Cardano 原话）。禁编造 Cardano 名言。
- **福尔摩斯式轶事禁写**：拒绝丹麦/法国国王与苏格兰王后聘约出自 Cardano 自述（"Cardano later wrote that..."）——保留「他自述」限定。
- **苏格兰诊疗细节**：page.md 载「治疗后由其助手完成」（"after the cure was effected by his assistant"）且与 Casanatus 争论功劳——勿写成他一人妙手回春。
- **查理五世与弗朗索瓦一世/苏莱曼**：他既支持查理五世又称赞其对手是"virtuous opponents"——两面表述照写，勿简化为单一立场。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q184530 | 待写入 |
| name_zh | 吉罗拉莫·卡尔达诺 | 待写入 |
| name_en | Gerolamo Cardano | 待写入 |
| name_variants | Girolamo Cardano / Geronimo / Jérôme Cardan / Hieronymus Cardanus | 待写入 |
| birth_date | 1501-09-24 | 待写入 |
| death_date | 1576-09-21 | 待写入 |
| nationality | Duchy of Milan（historical） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / algebra / medicine / probability / engineering / philosophy | 待写入 |
| has_biography | 0 | 本次只入库社会关系，立传未做 |

## 7. 社会关系入库清单（§20）

- **学生**：Lodovico Ferrari（infobox Notable students + 正文 "Cardano's student"，四次方程解法者；**Cardano 篇写一次，Tartaglia 篇已作为 rival 出现，不冲突**）
- **家庭**：父 Fazio Cardano（法学家、达·芬奇密友）、母 Chiara Micheri、妻 Lucia Banderini（1531–1546）、长子 Giovanni Battista（1534–1560 被斩）、女 Chiara（1537）、幼子 Aldo Urbano（1543，1569 剥夺继承权）
- **本组内关系不重复入库**：与 Tartaglia 的 controversy、与 del Ferro 的 influence 已分别在 Tartaglia / del Ferro 的 yaml 写入（无向关系自动成对），本 yaml **不写**这两条
- **不入库**：Leonardo da Vinci（系其父 Fazio 的密友，非 Cardano 本人关系）、查理五世/弗朗索瓦一世/苏莱曼（宫廷赞助/赞颂关系无类型）、教皇格里高利十三世（年金关系无类型）、圣安德鲁斯大主教 Hamilton（医患关系）、William Casanatus（同行争论，单事件）、Rafael Bombelli（仅"同代人首次描述虚数性质"之学术承续，页面无明确关系类型）、Thomas Browne / Manzoni / Forster（后世评家）。

## 8. 奖项清单

- page.md 无载任何奖项——**本节为空，禁杜撰**（教皇年金、皇家医师公会会员非奖项；月球环形山 Cardanus 是命名纪念，可在 §9/正文提及但不入 awards）。

## 9. 机构清单

- 教育：University of Pavia（帕维亚大学，1520 入学，1524 因战乱关闭）；University of Padua（帕多瓦大学，1525 医学博士）
- 任职：Scuole Piatti 之外的米兰数学教席（page.md 未具名机构，仅"obtained a mathematics teaching position in Milan"——**不入库**，正文表述）；University of Pavia（任教，metadata employer 明载、正文语境载其自帕维亚迁博洛尼亚，年份无载不写）；University of Bologna（博洛尼亚大学医学教授，1560 年代迁任、1570 因宗教裁判所失去教席——page.md 未载起止年份，不写年份）

## 10. 终审清单

- [ ] 生卒 1501-09-24 / 1576-09-21，享年 74，出生地 Pavia、卒地 Rome
- [ ] 死亡日弃 09-20 噪声值
- [ ] 名字异体仅身份信息页列一次
- [ ] 《大术》三条腿齐全：del Ferro 首解归名 / Ferrari 四次方程署名 / Tartaglia 相授与誓言争议
- [ ] 万向节「非其所描述」、Cardano's Rings「很可能早于」、gimbal/Cardan 轴「partially invented and described」措辞准确
- [ ] 虚数「承认存在」、负数「欧洲首个系统使用」、概率「第一个系统论述（身后出版）」
- [ ] 长子案与宗教裁判所客观简述、不渲染
- [ ] 引语仅限三处实载且注明转述来源
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Gerolamo_Cardano/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认使用 Gerolamo_Cardano_(colour).jpg 或 Leone Leoni 徽章像，图注写明藏处
- [ ] **国籍**：封面顶部徽章明示意大利 · 米兰公国
- [ ] **引语核对**：三处引语逐一在 page.md 原文找到并注明转述层级
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批 16 世纪数学家（del Ferro / Tartaglia）格式对齐；三次方程叙事与两篇口径完全一致

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
