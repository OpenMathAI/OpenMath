# John Napier（约翰·纳皮尔）立传提示词

> qid=Q159592 · 1550-02-01 – 1617-04-04 · 苏格兰数学家 · 16 世纪（核心贡献跨 16–17 世纪）
> 本地 Wikipedia 数据源：`mathematician/presentations/16th_century/pages/John_Napier/`（@page.md + metadata.json + images.txt，事实基准以 page.md 为准）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（page.md 内嵌 1616 年 Napier 肖像与苏格兰国家肖像画廊雕像照片可作候选，见 `images.txt`；下载失败则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 苏格兰`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
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

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「对数的发现者 · 神奇的梅尔切斯顿」+ 约翰·纳皮尔 1550–1617 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 家庭 / 教育 / 核心领域）
3. **约翰·纳皮尔的一生：时间线**（`\timelineslide`）：1550 梅尔切斯顿出生 → 1563 入 St Andrews → 1571 自欧陆学成归苏 → 1574 购 Gartness 城堡 → 1593《A Plaine Discovery》→ 1614《Descriptio》→ 1615 Briggs 来访 → 1617 去世
4. **早年与教育**（`\earlyslide`）：梅尔切斯顿塔、13 岁入圣安德鲁斯、舅父建议下的欧陆求学（何校不可考）、1574 Gartness
5. **《Mirifici Logarithmorum Canonis Descriptio》（1614）**（核心贡献页，表格 + 公式框）：对数的发现，57 页说明 + 90 页三角函数对数表
6. **从纳皮尔对数到常用对数**（核心贡献页，表格 + 公式框）：e 带来的实用困难、1615 Briggs 来访、重标度共识、委托 Briggs 计算
7. **Napier's bones 与 Promptuary**（核心贡献页，表格 + 公式框）：格子乘法的改良、编号算筹乘法工具
8. **小数点的推广**（核心贡献页，表格 + 公式框）：改进 Stevin 记法、句点作分隔符（引《构造》1889 英译原句可核实后使用）
9. **球面三角学与圆部分法则**（核心贡献页，表格 + 公式框）：Napier's Rules of Circular Parts、纳皮尔圆记忆法
10. **防御发明与「术士」传闻**（表格）：1596 秘密发明上书；黑公鸡捉贼、醉鸽捕鸟等传说（口径见 §5）
11. **神学著作《A Plaine Discovery》（1593）**（表格）：《启示录》的数学化解读、多语译本、献给 James VI
12. **影响与追随者**（表格）：Gresham College 的迅速接受、Gunter / Speidell 早期追随者、对数推动十进制算术普及
13. **身后名与纪念**（表格）：neper 单位、月球环形山 Neper、爱丁堡纳皮尔大学、St Cuthbert's 教堂纪念碑
14. **终章**：67 岁、「使计算化繁为简」的历史地位与遗产

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
- **合作 / 交往**：Henry Briggs（collaborator，来访商讨对数重标度、受托计算修正表）、John Craig（collaborator，友人，向第谷宣告对数发现）、Tycho Brahe（collaborator，经 Craig 有往来）、Edward Wright（collaborator，《Descriptio》英译者）
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
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/John_Napier/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先 1616 年肖像；下载失败用装饰圆占位并在图注说明
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
