# John Napier（约翰·纳皮尔）立传提示词

> qid=Q159592 · 1550-02-01 – 1617-04-04 · 苏格兰数学家 · 16 世纪（核心贡献跨 16–17 世纪）
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/John_Napier/`（@page.md + metadata.json + images.txt，事实基准以 page.md 为准）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 `images/napier_portrait.jpg` + `draw=coveraccent!50` 细边框 + 姓名小字注。★ PORTRAITS.md 第 12 条核定：用 **1616 年肖像**版画，图注写「John Napier of Merchiston，1616 年肖像」（page.md infobox 亦载 "1616 portrait of Napier"）；苏格兰国家肖像画廊雕像照片为雕像，只能作插图，不得充当头像。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 苏格兰`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧肖像 `napier_portrait.jpg` + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰；**师承 page.md 无载 → 该格写「—（无载）」，禁填人名**。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应「对数表 / 算筹」的计算母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：John Napier of Merchiston（拉丁化 Ioannes Neper；绰号 Marvellous Merchiston「神奇的梅尔切斯顿」；中文惯称：约翰·纳皮尔）
- **生卒**：1550-02-01 生于爱丁堡梅尔切斯顿塔（Merchiston Tower，苏格兰王国）→ 1617-04-04 逝于爱丁堡梅尔切斯顿城堡，享年 67
- **国籍**：苏格兰（Kingdom of Scotland，苏格兰王国）
- **身份**：数学家、物理学家、天文学家、神学家、发明家；梅尔切斯顿第 8 代领主（8th Laird of Merchiston）
- **家庭**：父 Sir Archibald Napier（梅尔切斯顿城堡领主，约翰出生时年仅 16 岁）、母 Janet Bothwell（政治家兼法官 Francis Bothwell 之女）；1572 年娶 Elizabeth Stirling（Keir 与 Cadder 第 4 代领主 James Stirling 之女，1579 年去世），育有二子；续娶 Agnes Chisholm，再生十子
- **教育轨迹**：
  - 幼年或受私人教育（无记录，系推测）
  - 13 岁入 St Andrews 大学 St Salvator's College（1563 年前后）；宗教改革致校务纷扰，**无完成学业的记录**
  - 依舅父 Adam Bothwell（奥克尼主教）1560-12-05 建议赴欧陆求学；在法国还是佛兰德斯、就读何校**均不可考**，1571 年返苏格兰时已通希腊语
- **导师**：无载（page.md 未记载任何导师）
- **研究领域**：数学（对数、计算器械、球面三角学）、天文学、物理学、神学

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **对数的发现者**：Napier 最著名的身份——对数（logarithms）的发明人，《Mirifici Logarithmorum Canonis Descriptio》（1614）载 57 页说明 + 90 页三角函数对数表。
2. **把计算化繁为简的时代动因**：与当时许多数学家一样致力于减少计算劳动；他看准 prosthaphaeresis（三角恒等式化乘为加）、十进分数、符号指数算术的潜力，并刻意把对数放进**三角学语境**以贴合天文计算实务。
3. **Napier's bones（纳皮尔算筹）**：改进 Fibonacci 使用的格子乘法（lattice multiplication）而得的乘法算筹；另有计算器械 Promptuary。
4. **小数点的推广者**：改进 Simon Stevin 的十进制记数法，引入句点（.）作整数与小数部分的分隔符——今日通用的记法。
5. **球面三角学**：《Descriptio》讨论球面三角定理，即著名的 **Napier's Rules of Circular Parts**（圆部分法则），配有「纳皮尔圆 / 纳皮尔五边形」记忆法（中间部取正弦、相邻部取正切、相对部取余弦）。
6. **布里格斯的来访与常用对数的起点**：对数发明迅速被格雷沙姆学院（Gresham College）接受；Henry Briggs 于 1615 年来访，讨论对数重标度（含今日称为 e 的常数在实用上的困难——**e 的发现是数十年后 Jacob Bernoulli 之功**）；纳皮尔把修正对数表的计算委托给 Briggs。
7. **《构造》与身后出版**：《Mirifici Logarithmorum Canonis Constructio》写于《Descriptio》之前，1619 年由其子 Robert 身后出版；《Rabdologiæ》1617 年身后出版；Edward Wright 英译本 1616 年问世。
8. **防御发明（1596）**：1596-06-07 上书《Secret inventions...》，提出两种远距烧船的聚光镜（burning mirror）、特种炮弹与防火枪金属战车。
9. **神学著作《A Plaine Discovery》（1593）**：以数学分析《启示录》试图推算末日日期（定第七号角为 1541 年，预言末日 1688 或 1700 年）；他认为自视为最重要之作，有荷/法/德/英多语版本。
10. **身后名**：电学单位 neper（奈培）、月球环形山 Neper、爱丁堡纳皮尔大学均以其命名；法/西/葡语称自然对数为 Logarithme Népérien 等。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（苏格兰高地深靛） | `#16324F` | 梅尔切斯顿塔 / 苏格兰夜空 |
| 强调色（对数表金） | `#C9A227` | 90 页对数表的黄铜计算时代 |
| 分类色 1（对数 — 靛蓝） | `#4C5FD5` | 对数的发现 / 布里格斯来访 |
| 分类色 2（计算器械 — 青绿） | `#0E7C7B` | Napier's bones / Promptuary |
| 分类色 3（球面三角 — 琥珀） | `#E07B30` | 圆部分法则 / 纳皮尔圆 |
| 分类色 4（神学与传说 — 深紫） | `#52307C` | 《启示录》研究 / 「术士」传闻 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「对数表刻度 / 算筹阵列」的计算秩序感。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **选定曲目**：**Eternals**（Alex-Productions，`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`，宏大 / 深远）
- **风格定调**：**宏大而深远**（一项发明泽被四百年科学计算）
- **匹配理由**：
  - 对数「为天文学家人为延长了寿命」式的深远影响，匹配 Eternals 的**宏大 / 深远**标签（适合基础理论、长期影响场景）
  - 本组三人内不重复：Harriot 用 Lonesome、Briggs 用 Expedition
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（统一 14 页制：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年与教育 + 7 贡献页 + 荣誉与传承 + 终章）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格。
> 页结构（14 页，TEMPLATE_GUIDE §2 标准制）：共享封面 + 人物封面 + 身份信息 + 时间线 + 早年与教育 + 7 个核心贡献页 + 荣誉 + 终章。Napier 素材多，**勿堆砌**：原「影响与追随者」并入荣誉页。

1. **共享封面**（`\openmathslide`）：`\input{../../cover/openmath_page.tex}`，不改
2. **人物封面**（`\titleslide`）：大标题「对数的发现者 · 神奇的梅尔切斯顿」+ 约翰·纳皮尔 1550–1617 + 右上肖像 `napier_portrait.jpg`（图注「John Napier of Merchiston，1616 年肖像」）+ 国籍行「苏格兰」+ 底部三要素状态栏 + 四分类 badge
3. **身份信息页**（`\profileslide`，★ 必做）：左肖像 `napier_portrait.jpg` + 右信息网格（生卒 / 本名与拉丁化 Ioannes Neper / 国籍 / 出生地 / 家庭 / 教育 / 核心领域；师承格写「—（无载）」）
4. **约翰·纳皮尔的一生：时间线**（`\timelineslide`，竖轴 8 节点）：1550-02-01 梅尔切斯顿塔出生 → 约 1563 入 St Andrews → 1571 自欧陆学成归苏 → 1593《A Plaine Discovery》→ 1596 秘密发明上书 → 1614《Descriptio》→ 1615 Briggs 来访 → 1617-04-04 去世（1574 Gartness、1608 入居梅尔切斯顿城堡等细节置于第 5 页早年页与正文）
5. **早年与教育**（`\earlyslide`）：梅尔切斯顿塔、13 岁入圣安德鲁斯（无完成记录）、舅父 Adam Bothwell 1560-12-05 信建议赴法/佛兰德斯（何校不可考、1571 归苏时通希腊语）、1574 Gartness
6. **《Mirifici Logarithmorum Canonis Descriptio》（1614）**（贡献页，表格 + 公式框）：对数的发现，57 页说明 + 90 页三角函数对数表
7. **从纳皮尔对数到常用对数**（贡献页，表格 + 公式框）：e 带来的实用困难（e 非二人所发现）、1615 Briggs 来访、重标度共识、委托 Briggs 计算修正表
8. **Napier's bones 与 Promptuary**（贡献页，表格 + 公式框）：格子乘法（Fibonacci 已用）的改良、编号算筹乘法工具
9. **小数点的推广**（贡献页，表格 + 公式框）：改进 Stevin 记法、句点作小数分隔符（可引 page.md 注释所载 1889 年英译《构造》原句，须注明为 1889 英译）
10. **球面三角学与圆部分法则**（贡献页，表格 + 公式框）：Napier's Rules of Circular Parts、纳皮尔圆 / 五边形记忆法（中间部取正弦、相邻部取正切、相对部取余弦）
11. **防御发明（1596）与「术士」传闻**（贡献页，表格）：1596-06-07 秘密发明上书（聚光镜 / 特种炮弹 / 防弹金属战车）；黑公鸡捉贼、醉鸽捕鸟等传说（口径见 §5，勿写成事实）
12. **神学著作《A Plaine Discovery》（1593）**（贡献页，表格）：《启示录》的数学化解读（第七号角 1541、末日 1688 或 1700）、多语译本（荷 1600 / 法 1602 / 德 1611、1615 / 英 1611 新版）、1594-01-29 献给 James VI
13. **影响、追随者与身后纪念**（荣誉页，表格）：Gresham College 的迅速接受、Gunter / Speidell 早期追随者、对数推动十进制算术普及、Briggs 十进制对数表；neper 单位、月球环形山 Neper、爱丁堡纳皮尔大学、St Cuthbert's 教堂纪念碑
14. **终章**（`\closingslide`）：67 岁、「使计算化繁为简」的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **生卒口径**：1550-02-01 生、1617-04-04 卒，享年 67（metadata 与 page.md 一致，无噪声）。
- **教育**：**无完成 St Andrews 学业的记录**；欧陆就读大学不可考（巴黎/日内瓦均无注册记录）——勿写「毕业于某大学」；返苏时通希腊语是事实，可写。
- **对数与 e**：纳皮尔与布里格斯讨论的重标度涉及今日称为 e 的常数，但**两人都未发现 e**——e 的发现是数十年后 Jacob Bernoulli 之功，勿写「纳皮尔发现 e」。
- **「自然对数」口径**：page.md 称《Descriptio》的表列有三角函数的 natural logarithms；而现代自然对数 ln 与纳皮尔原始对数定义并不相同——立传表述跟随 page.md，勿自行展开「纳皮尔对数 ≠ ln」的技术细节（page.md 无载），也勿写「纳皮尔发明了自然对数 ln」。
- **布里格斯来访年份**：Napier 页作 1615 年来访；Briggs 本人页作 1616 年来访、次年再访——两页口径不一。**本篇沿用 Napier 页 1615**；入 yaml 的 note 不写具体年份（见 §7）。
- **神学立场**：纳皮尔受 Christopher Goodman 讲道影响持强烈反教皇立场，曾著文称教皇为敌基督——这是 16 世纪苏格兰宗教改革语境的史实，**客观简述、不评价、不展开教义争辩**；末日预测（1541 第七号角、1688/1700）客观陈述即可。
- **「术士」传闻**：随身黑蜘蛛、黑公鸡「使魔」、醉鸽捕鸟等均为传闻/轶事口径（was said / thought to have dabbled），**勿写成事实**；与 Robert Logan of Restalrig 的 Fast Castle 寻宝契约确实存在但从未履行——可作趣闻，注明契约原文出处。
- **死因**：死于痛风（gout）的影响，在梅尔切斯顿城堡家中去世——勿写其他死因。
- **同名与拼写**：拉丁化名 Ioannes Neper；父 Archibald Napier 与本人不同名（无自环风险），但 yaml 中父名用规范形式 Archibald Napier；同代另有苏格兰数学家 John Napier 后裔等勿混。
- **单位与地名**：neper 是分贝的替代单位（电学）、月球环形山 Neper 在正面边缘勿写位置细节（page.md 无载）。
- **★ 肖像口径（Review-1 补）**：PORTRAITS.md 第 12 条核定纳皮尔**有** 1616 年肖像 → 用 `images/napier_portrait.jpg`，图注「John Napier of Merchiston，1616 年肖像」；苏格兰国家肖像画廊雕像照片为雕像，仅作插图。
- **引语来源**：page.md 注释所载 1889 年 Macdonald 英译《构造》小数点定义句（"In numbers distinguished thus by a period in their midst, whatever is written after the period is a fraction..."）可用，**须注明系 1889 年英译**；舅父 1560-12-05 信句 "I pray you, sir, to send John to the schools either to France or Flanders, for he can learn no good at home."（page.md 原文）可用。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q159592 | 待写入 |
| name_zh | 约翰·纳皮尔 | 待写入 |
| name_en | John Napier | 待写入 |
| birth_date | 1550-02-01 | 待写入 |
| death_date | 1617-04-04 | 待写入 |
| nationality | Scotland（Kingdom of Scotland 带 era_note） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / astronomy / physics / theology | 待写入 |
| has_biography | false | 本次只入库社会关系，立传未做 |

## 7. 社会关系入库清单（§20）

> 仅收 page.md 明载关系；note 不写布里格斯来访年份（两页口径不一，见 §5）。

- **家庭**：父 Archibald Napier（parent-child）、母 Janet Bothwell（parent-child）、外祖父 Francis Bothwell（parent-child）、舅父 Adam Bothwell（influence，建议赴欧陆求学）
- **配偶**：Elizabeth Stirling（1572 年结婚，1579 年去世）、Agnes Chisholm
- **合作 / 交往**：Henry Briggs（collaborator，来访商讨对数重标度、受托计算修正表）、John Craig（collaborator，1590 年代向第谷宣告对数发现；page.md 原句 "Tycho Brahe who corresponded with his friend John Craig" 中 "his" 指代不明，**勿坐实为「纳皮尔之友」**）、Tycho Brahe（collaborator——page.md 仅载 "he had contact with Tycho Brahe"，系经 Craig 间接联系，**勿写成合作研究**）、Edward Wright（collaborator，《Descriptio》英译者，1616 年出版）
- **思想影响**：Christopher Goodman（influence，其讲道塑造反教皇解读）、Simon Stevin（influence，纳皮尔改进其十进制记法）、Edmund Gunter（influence，早期追随者）、John Speidell（influence，早期追随者）

## 8. 奖项清单

- page.md 无任何获奖记录——**不设奖项页、不入库**。

## 9. 机构清单

- 教育：University of St Andrews（St Salvator's College，约 1563 年入学，13 岁；无完成记录）
- 任职：无机构任职记录（终身为梅尔切斯顿领主，在家研究）——机构仅入 education 一条。

## 10. 终审清单

- [ ] 生卒 1550-02-01 / 1617-04-04，享年 67，出生地 Merchiston Tower
- [ ] 国籍用「苏格兰」，注明 Kingdom of Scotland 历史政权
- [ ] 无导师、无完成学位——教育表述不得拔高
- [ ] e 的发现归 Jacob Bernoulli，勿写纳皮尔/布里格斯发现 e
- [ ] 布里格斯来访年份本篇用 1615（沿用本人页面）
- [ ] 神学立场客观简述不评价；「术士」传闻不写成事实
- [ ] 死因=痛风的影响，67 岁
- [ ] 引语必须 page.md 原文；page.md 无载禁写
- [ ] 肖像用 `napier_portrait.jpg`（1616 年肖像，图注「John Napier of Merchiston，1616 年肖像」）；雕像仅作插图
- [ ] 正文采用 Wilson 式：身份信息页 + 封面肖像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/John_Napier/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **肖像**：使用 `napier_portrait.jpg`（1616 年肖像，PORTRAITS.md 第 12 条）；雕像照片仅作插图
- [ ] **国籍**：封面顶部徽章明示苏格兰
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如《构造》小数点定义句、舅父 1560-12-05 书信句）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（布里格斯 / 哈里奥特）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**

## 12. Review-1 事实终审记录（2026-09-29）

- 核对基准：`pages/John_Napier/page.md`（+ metadata.json）
- 生卒 / 享年：1550-02-01 生于爱丁堡梅尔切斯顿塔（Merchiston Tower，Kingdom of Scotland）→ 1617-04-04 卒于爱丁堡梅尔切斯顿城堡，享年 67（page.md "aged 67"）；死因：痛风的影响（"died from the effects of gout"）；葬于 St Giles 教堂墓地，后迁 St Cuthbert's 地下墓室并立壁碑；metadata 与本页一致，无噪声
- 国籍口径：苏格兰（Kingdom of Scotland；metadata nationality: Kingdom of Scotland）→ 封面国籍行「苏格兰」，入库加 era_note historical
- 肖像结论：**有** 1616 年肖像 → `napier_portrait.jpg`，图注「John Napier of Merchiston，1616 年肖像」（PORTRAITS.md 第 12 条；page.md infobox 亦载 "1616 portrait of Napier"）；苏格兰国家肖像画廊雕像照片仅作插图
- 引语核对：本篇无成段直接引语，全文转述；可核实的两条来源句均逐字对上 page.md：① 舅父 Adam Bothwell 1560-12-05 信 "I pray you, sir, to send John to the schools either to France or Flanders, for he can learn no good at home."（page.md line 39）✅；② 1889 年 Macdonald 英译《构造》小数点定义句 "In numbers distinguished thus by a period in their midst…"（page.md 注释 13，line 606）✅ ——后者系**译作引语**，tex 中须注明 1889 英译；另有 page.md line 536 "the simple of this island may be instructed" 与 1594 献词 "that justice be done against the enemies of God's church" / "to reform the universal enormities of his country…" 亦为原文，可用
- 本轮修正：① §0/§0-3/§4/§10/§11 共 6 处肖像条款改为使用 `napier_portrait.jpg`（1616 年肖像，依 PORTRAITS.md 权威结论），雕像降为插图；② §4 重排为 14 页制：补入共享封面为第 1 页、人物封面为第 2 页，7 个贡献页为 6–12（Descriptio / 常用对数重标度 / Napier's bones 与 Promptuary / 小数点推广 / 圆部分法则 / 防御发明与术士传闻 / 《A Plaine Discovery》），原「影响与追随者」并入第 13 页荣誉页「影响、追随者与身后纪念」，避免堆砌；③ §0-3 与 §4-3 明确「师承 page.md 无载 → 网格写「—（无载）」，禁填人名」；④ §4-4 时间线按 TEMPLATE_GUIDE 收敛为 **8 节点**（1550-02-01 → 约 1563 → 1571 → 1593 → 1596 → 1614 → 1615 → 1617），并按年序校正 1593/1596 先后；1574 Gartness、1608 入居梅尔切斯顿城堡（page.md：父卒于 1608 年）等细节移入早年页与正文；⑤ §7 澄清 page.md "Tycho Brahe who corresponded with his friend John Craig" 中 "his" 指代不明，禁坐实 Craig 为「纳皮尔之友」；Tycho 关系仅系经 Craig 间接联系（page.md 仅 "had contact with"），禁写合作研究；⑥ §5 补引语来源条款（1889 英译须注明）
- 遗留不确定项：**★ 布里格斯两次爱丁堡会面年份两页矛盾**——Napier 页作 1615 年来访，Briggs 本人页作 1616 年（次年再访）；按纪律**各自忠于本人页面、不得互改**：本篇沿用 1615，入 yaml 的 note 不写具体年份；② 欧陆就读大学不可考（巴黎/日内瓦均无注册记录），教育表述止于「未完成 St Andrews 学业」；③ e 的发现归 Jacob Bernoulli，纳皮尔与 Briggs 均未发现 e；④ 现代自然对数 ln 与纳皮尔原始对数定义并不相同，page.md 无载细节，立传跟随 page.md、勿展开；⑤ 「术士」传闻（黑蜘蛛、黑公鸡、醉鸽）与 Fast Castle 寻宝契约均为传闻/未履行契约口径，勿写成事实；⑥ 背景曲 Eternals 与 Harriot（Lonesome）、Briggs（Expedition）不重复，未查同世纪其他篇目撞曲（按纪律仅记录不改）

## 13. 立传期记录（Beamer 立传，2026-09-29）

- 产出：`John_Napier_zh.tex` + `Makefile`（复制 17 世纪 Johann_Bernoulli 黄金参照，仅改 MAIN/VIDEO_NAME），`make distclean && make` 通过。
- 编译：**0 error**；`Overfull` 仅 1 处 4.67pt，位于**不可修改的共享封面** `cover/openmath_page.tex`（<10pt 可接受）；无 `Underfull`。PDF **14 页**（共享封面 + 人物封面 + 身份信息 + 时间线 + 早年 + 7 贡献页 + 荣誉 + 终章）。
- 肖像：`images/napier_portrait.jpg`（1616 年肖像，图注「John Napier of Merchiston，1616 年肖像」），与 PORTRAITS.md 第 12 条一致；未使用雕像。
- 时间线：采用 §4-4 / §12 的 8 节点（1550 → 约 1563 → 1571 → 1593 → 1596 → 1614 → 1615 → 1617）；1560 舅父书信、1574 Gartness、1608 入居梅尔切斯顿城堡置于早年页与正文。
- 事实核对：逐条对照 `pages/John_Napier/page.md`，**未发现提示词与 page.md 冲突**，无事实修正；布里格斯来访年份本篇守 **1615**（忠于本人页面），未与 Briggs 篇互改。
- 引语：小数点定义句注明系 1889 年 Macdonald 英译《构造》。
