# Niccolò Tartaglia（尼科洛·塔尔塔利亚）立传提示词

> qid=Q201543 · 1499/1500 – 1557-12-13 · 意大利数学家、工程师（威尼斯共和国） · 16 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/Niccolò_Tartaglia/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**Tartaglia 的 infobox 肖像是 Philip Galle 1572 年雕版画**（由 Christophe Plantin 印制、Benito Arias Montano 撰文），但 `images.txt` 未收录该雕版画像（仅书影与插图）——执行立传时可尝试经 Wikipedia REST API 或 Commons `Special:FilePath` 获取雕版像；失败则用装饰圆 `\faIcon{user}` 占位。**本任务阶段不下载**，提示词只记录候选。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 意大利 · 威尼斯共和国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名（存争议）、国籍、出生地、师承（自学者）、主要著作、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），呼应「弹道抛物线 / 塔尔塔利亚三角」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Nicolo，通称 Tartaglia（意大利语"口吃者"绰号）；「本名 Niccolò Fontana」一说**存争议**（见 §5）；中文惯称：尼科洛·塔尔塔利亚
- **生卒**：1499/1500 年生于布雷西亚（Brescia，威尼斯共和国）→ 1557-12-13 逝于威尼斯，享年 56–58
- **国籍**：威尼斯共和国（Republic of Venice，历史政权）
- **身份**：数学家、工程师（设计防御工事）、地形测绘师、簿记员、教师、翻译家、出版人
- **家庭**：父 Yliano Abido de la maison forgentio（信使骑手，1506 年遇劫被害，遗孀与三个孩子陷于贫困；页内另一处作 Michele，见 §5）；1512 年布雷西亚之劫中下颚与上颚被法军士兵马刀劈伤，母救回一命但留下语言障碍，从此留须遮疤、终生不剃
- **教育轨迹**：**完全自学**（infobox Academic advisor: Autodidact）——约 14 岁时随 Master Francesco 学写字母表，学到字母"k"时无力缴费，此后再未请过教师；约 1517 年迁维罗纳，1534 年迁威尼斯
- **导师**：无（自学者）；infobox 明载影响者：Al-Khwarizmi、Euclid
- **研究领域**：数学、工程学；弹道学（首创）、商业算术、代数（三次方程）、立体几何

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **三次方程的独立解法者**：独立解出三次方程（三类不同形式的解法），与 Cardano 并享其名——今称 **Cardano–Tartaglia formula**。
2. ** Fiore 挑战赛**：此前曾被德尔·费罗的学生 Fiore 下战书挑战解题，由此确知解法存在，并最终胜出。
3. **1539 誓言与《大术》风波**：Cardano 以「承诺不发表」劝得塔尔塔利亚以**诗体**交出三类三次方程的解法秘诀；数年后 Cardano 见到 del Ferro 更早的未刊手稿，认定誓言可以违背而将其发表——引发长达十年的公开论战。
4. **弹道学之父**：1537 年《Nova Scientia》（《新星》）**第一个把数学应用于炮弹路径研究**，将早期炮手的实用知识转化为理论化、数学化的框架；结论之一：最大射程在炮身与地面成 **45°** 时取得；弹道模型为「直线段—圆弧段—竖直下落」三段式。
5. **《Nova Scientia》的历史地位**：被 Valleriani 称为「文艺复兴最重要的力学著作之一」；其军事科学著作在欧洲流传极广，至 18 世纪仍是普通炮手的参考书。
6. **翻译家**：1543 年出版 71 页拉丁文版阿基米德著作（重心与浮体诸篇为**首次出版**）；同年《Euclide Megarense philosopho》——**《几何原本》首个现代欧洲语言（意大利语）译本**，依据 Zamberti 的希腊文校勘本纠正了两个世纪以来拉丁译本第五卷（欧多克索斯比例论）的错误，并写下第一个现代且有用的评注。
7. **《General Trattato di Numeri et Misure》**：约 1500 页六卷巨著（威尼斯方言），前三卷 1556 年出版、后三卷 1560 年由其文学遗嘱执行人 Curtio Troiano 出版；被 David Eugene Smith 誉为「那个世纪意大利出现的最佳算术论著」；第一卷 554 页为商业算术（多种货币兑换、利息、合伙分利）。
8. **塔尔塔利亚三角**：在《General Trattato》第二卷明载二项式系数的**加法构成规则**——比帕斯卡早一百年；示例含 `(6+4)^7` 的完整展开。
9. **四面体体积**：《General Trattato》第四卷以 13-14-15 底、20-18-16 棱的不规则四面体为例示范求高（h² 公式出自余弦定理），最终答案 √(240 615/3136)，方法正确（中途抄错一位数字）。
10. **影响伽利略**：伽利略拥有「批注详尽」的塔尔塔利亚弹道著作，并在此基础上最终解决抛体问题；斜面/落体研究部分验证并部分取代了其弹道模型。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（威尼斯深蓝） | `#16324F` | 威尼斯共和国 / 亚得里亚海的深沉 |
| 强调色（火药铜橙） | `#B85C00` | 弹道学 / 炮兵 / 军事工程 |
| 分类色 1（三次方程 — 靛蓝） | `#2F4470` | 三次方程解法 / Cardano–Tartaglia 公式 |
| 分类色 2（算术三角 — 暗金） | `#C9A227` | 塔尔塔利亚三角 / 商业算术 |
| 分类色 3（译经 — 深绿） | `#145C54` | 阿基米德 / 欧几里得翻译 |
| 分类色 4（命运 — 暗紫） | `#46356B` | 布雷西亚之劫 / 自学者之路 |
| 背景 | `#F4F6F8` | 浅灰蓝白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「弹道抛物线 / 数字三角」的几何意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**Lonesome**（AShamaluevMusic，本地文件 `music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`）
- **风格定调**：**悲伤 / 电影感 / 逆境**（孤儿、口吃、自学者的一生）
- **匹配理由**：
  - 塔尔塔利亚 6 岁丧父、少年遭马刀毁容落下「口吃者」绰号、学字母学到"k"即辍学——「悲伤 / 逆境」精准匹配其前半生的苦难底色
  - 「孤独钻研」匹配其完全自学、靠「死人们的著作」与「贫穷之女——勤奋」相伴的学者形象
  - 电影感可托住三次方程论战的戏剧张力而不喧宾夺主
  - 本组三人（del Ferro / Tartaglia / Cardano）分别用 PAST / Lonesome / Cinematic Experience，互不重复
- 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「口吃者 · 弹道学之父」+ Niccolò Tartaglia 1499/1500–1557 + 右上头像（雕版像或装饰圆）+ 国籍行（意大利 · 威尼斯共和国）+ 底部三要素状态栏（威尼斯共和国 | 无固定机构（算盘学校教师） | 三次方程 / 弹道学 / 塔尔塔利亚三角）+ 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名（存争议，作 Tartaglia 通称）/ 国籍 / 出生地 / 师承（自学）/ 主要著作 / 核心领域）
3. **塔尔塔利亚的一生：时间线**（`\timelineslide`）：1499/1500 布雷西亚出生 → 1506 丧父 → 1512 布雷西亚之劫受伤辍学 → 约 1517 迁维罗纳 → 1531 香肠贩摊头发现阿基米德 → 1534 迁威尼斯 → 1537《Nova Scientia》→ 1539 誓言交出三次方程解法 → 1543 两部译著出版 → 1545《大术》发表引论战 → 1556–1560《General Trattato》→ 1557-12-13 去世
4. **布雷西亚之劫**（`\earlyslide`）：1512 法军屠城（逾 45,000 人死难）、主教座堂避难被马刀劈伤下颚与上颚、母亲救回、语言障碍与"口吃者"绰号、终生留须遮疤
5. **自学之路**（核心贡献页，表格 + 引文框）：字母"k"辍学、*Quesiti* 卷六问 8 自传式引语（"From that day, I never returned to a tutor…"）、维罗纳香肠贩摊头读到瓜里科 1503 年拉丁版阿基米德（1531）、威尼斯印刷文化使贫寒学者也能读到早期印本
6. **三次方程与 Fiore 挑战**（核心贡献页，表格 + 公式框）：独立解出三类三次方程、Fiore（del Ferro 之徒）下战书、胜出
7. **誓言与《大术》**（敏感页，表格）：1539 以「不发表」承诺换得诗体秘诀、Cardano 见 del Ferro 更早手稿后认定誓言可破、1545 发表并署名塔尔塔利亚、十年公开论战、与 Ferrari 的公开挑战赛；「塔尔塔利亚余生专为毁掉 Cardano」的流言已被数学史家证伪（fabricated）
8. **弹道学：《Nova Scientia》1537**（核心贡献页，表格 + 公式框）：数学化弹道之首创、45° 最大射角、直线—圆弧—竖直三段弹道模型、Book 2 末对 45° 仰角初始直线段长度的欧几里得式代数论证（*procederemo per algebra*）
9. **译经：阿基米德与欧几里得**（核心贡献页，表格）：1543《Opera Archimedis》（重心/浮体首刊）、1543《Euclide Megarense philosopho》（首个现代欧洲语言《原本》译本、纠正第五卷欧多克索斯比例论）
10. **《General Trattato》**（核心贡献页，表格）：六卷 1500 页商业算术百科、威尼斯方言、Smith 评价、第一卷货币/利息/合伙分利
11. **塔尔塔利亚三角**（核心贡献页，表格 + 公式框）：比帕斯卡早百年的二项式系数三角、加法构成规则明载、`(6+4)^7` 展开示例、几何化思考方式（ab 上的 ac/cb 分段）
12. **四面体体积**（核心贡献页，表格 + 公式框）：13-14-15 底、20/18/16 棱、三角形求高公式 h²=r²−((p²+r²−q²)/2p)²、答案 √(240 615/3136)、V≈433.9513222（方法正确，中途抄错一位）
13. **影响与传承**（表格）：伽利略的详注本与抛体问题最终解决、至 18 世纪仍是炮手参考书、Cardano–Tartaglia 公式的并列命名
14. **终章**：56–58 岁、"自学的巨人"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **本名存争议**：infobox/page.md 明言「本名 Niccolò Fontana」一说有争议——有来源仅凭遗嘱中指定兄弟 Zuampiero Fontana 为继承人推断，并不能证明同姓。**正文名字统一用 Tartaglia / Niccolò Tartaglia**，提及 Fontana 时必须带「一说 / 存争议」限定，禁作定论。
- **生年**：1499/1500 两说并存（metadata 亦有 1499-00-00 与 1500-00-00 两噪声值）——封面与正文写「1499/1500」，禁写死单一日期；享年写 56–58。
- **父名矛盾**：page.md 正文先说父亲是 "Yliano Abido de la maison forgentio"，同段又写 "In 1506, **Michele** was murdered by robbers"——**同页自相矛盾**。裁定：入库与正文用 Yliano Abido（身份信息首次出现的形式），§1 加注页内另作 Michele。
- **引语红线**：可用引语仅限 page.md 实载三处——① *Quesiti* 卷六问 8 的自学自白（"From that day, I never returned to a tutor, but continued to labour by myself over the works of dead men, accompanied only by the daughter of poverty that is called industry"）；② 香肠贩摊头原话（*in mano di un salzizaro in Verona, l'anno 1531*）；③ "ten pennies for one question" 一段的转述。其余一律转述，禁编造。
- **誓言与论战（敏感核心）**：按 page.md 实载顺序写——Cardano **承诺不发表**→塔尔塔利亚以诗体交出解法→Cardano 见到 **del Ferro 更早（dated before Tartaglia's）的未刊成果**→认定誓言可破→发表（虽仍署名塔尔塔利亚）→塔尔塔利亚极为愤怒→与 **Cardano 的学生 Ferrari** 公开挑战赛。措辞勿带单侧道德评判；Cardano 归名 del Ferro 首解与署名塔尔塔利亚两点都要写全。
- **「余生毁掉 Cardano」流言**：page.md 明言 "Widespread stories that Tartaglia devoted the rest of his life to ruining Cardano... appear to be completely fabricated"——若提及必须同时写「已被数学史家证伪」，或直接不写。
- **公式命名**：今称 Cardano–Tartaglia formula（数学史家把功劳并记两人）——本篇标题性表述用此名，勿单写「塔尔塔利亚公式」。
- **45° 结论的局限**：45° 最大射程是其实测/理论结论之一（对真空斜抛恰为真，但其三段弹道模型整体后被伽利略部分取代）——勿把三段模型写成「正确理论」。
- **帕斯卡三角命名**：写「塔尔塔利亚三角（亦称帕斯卡三角）」，时间差一百年，表述为「早一百年明载加法构成规则」，禁写「发明了帕斯卡三角」。
- **学生 Ostilio Ricci**：仅 infobox "Notable students" 明载，正文无事迹——一行即可，禁展开（勿写其为伽利略之师，本页无载）。
- **弹道插图**：《Nova Scientia》弹道轨迹图（images.txt 首条）与《General Trattato》书影、三角图、金字塔图可作插图候选，注意图注准确。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q201543 | 待写入 |
| name_zh | 尼科洛·塔尔塔利亚 | 待写入 |
| name_en | Niccolò Tartaglia | 待写入 |
| name_variants | Niccolò Fontana（存争议，仅作别名记录） | 待写入 |
| birth_date | 1499（1499/1500 两说，取 1499） | 待写入 |
| death_date | 1557-12-13 | 待写入 |
| nationality | Republic of Venice（historical） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / engineering / ballistics / geometry / algebra | 待写入 |
| has_biography | 0 | 本次只入库社会关系，立传未做 |

## 7. 社会关系入库清单（§20）

- **学生**：Ostilio Ricci（infobox Notable students 明载）
- **影响（受影响）**：Al-Khwarizmi（正文明载其数学受其著作影响）、Euclid（infobox 影响者 + 1543 译注《原本》）
- **影响（影响他人）**：Galileo Galilei（伽利略拥有其详注弹道著作并据此最终解决抛体问题）
- **论战（controversy）**：Gerolamo Cardano（1539 誓言换解法→1545《大术》发表→十年论战；**本组内唯一一次入库，Cardano 篇 yaml 不重复写**）
- **论战（controversy）**：Lodovico Ferrari（《大术》发表后的公开解题挑战赛，属三次方程解法归属论战；规范名用 **Lodovico Ferrari**（库内 Q310783），Tartaglia 页面拼写作 Ludovico——入库名以规范拼写为准，正文叙述可用页面拼写并加注；Tartaglia 篇写一次，Cardano 篇不重复）；Antonio Fiore（del Ferro 之徒，曾下战书挑战解题，rival）
- **家庭**：父 Yliano Abido（信使骑手，1506 遇害；页内另作 Michele，见 §5 裁定）
- **不入库**：母亲与两个兄弟姐妹（无姓名）、Curtio Troiano（出版遗嘱执行人，出版关系无类型）、Federigo Commandino（仅引其 1558 年论阿基米德之语，非关系）、Archimedes（系翻译/研习对象，非页面明载 influence）。

## 8. 奖项清单

- page.md 无载任何奖项与荣誉——**本节为空，禁杜撰**（Fiore 挑战赛与 Ferrari 挑战赛是解题决斗，非奖项）。

## 9. 机构清单

- **无正式院校**：自学出身；在威尼斯算盘学校（abacus schools）教授实用数学为生，销售数学咨询（向炮手与建筑师，"ten pennies for one question"）——算盘学校非具名机构，**不入库**，机构行在 Beamer 中表述为「算盘学校（abacus schools）教师」。
- 地点轨迹：布雷西亚 → 约 1517 维罗纳 → 1534 威尼斯（卒）。

## 10. 终审清单

- [ ] 生年 1499/1500 两说并存、卒 1557-12-13，享年 56–58
- [ ] 本名 Fontana 说带「存争议」限定
- [ ] 父名用 Yliano Abido 并注页内另作 Michele
- [ ] 誓言—发表—论战链条顺序与双方行为表述准确（Cardano 承诺→见 del Ferro 手稿→破誓发表但仍署名→论战）
- [ ] 「余生毁掉 Cardano」流言如提及必写「已证伪」
- [ ] 公式命名用 Cardano–Tartaglia formula
- [ ] 引语仅限三处实载，禁编造
- [ ] 塔尔塔利亚三角「早一百年」表述准确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Niccolò_Tartaglia/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认所用肖像为 Philip Galle 1572 雕版像（或装饰圆占位），图注写明雕版信息
- [ ] **国籍**：封面顶部徽章明示意大利 · 威尼斯共和国
- [ ] **引语核对**：三处引语逐一在 page.md 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批 16 世纪数学家（del Ferro / Cardano）格式对齐；三次方程叙事与两篇口径一致

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
