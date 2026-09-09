# John Wallis（约翰·沃利斯）立传提示词

> qid=Q208359 · 1616-12-03 – 1703-11-08 · 英国数学家 · 17 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/John_Wallis/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**注意：本地 images.txt 无肖像**（仅书影与数线插图）；执行时从 Wikimedia Commons / National Portrait Gallery 下载沃利斯肖像（page.md 外链有 NPG 检索页 "Portraits of John Wallis"）至 `images/wallis_portrait.jpg`；失败则用装饰圆 `\faIcon{user}` 占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒（注新旧历）、国籍、出生地、职业（数学家/牧师/密码学家）、教育、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「无穷符号 ∞ / 连乘积」之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 0.5 模板机制（执行立传前必读）

> 黄金参照 `Johann_Bernoulli/Johann_Bernoulli_zh.tex` 逐帧改写；机械要点（14 帧结构 / 共享封面 `\input{../../cover/openmath_page.tex}` / Makefile 复制改 MAIN / 肖像下载与装饰圆占位 / `make distclean && make` 编译循环 / 已知陷阱）见 **`17th_century/TEMPLATE_GUIDE.md`**。

## 1. 背景信息（用于 Slide 1-3）

- **全名**：John Wallis（拉丁化 Wallisius，中文：约翰·沃利斯）
- **生卒**：1616-12-03 生（旧历 O.S. 1616-11-23）于 Ashford, Kent → 1703-11-08 逝（旧历 O.S. 10-28）于牛津，享年 86。★ metadata.json 存的是旧历日期，与 infobox 新历不一致，统一用新历
- **国籍**：Kingdom of England（英格兰王国），现代对应英国/英格兰
- **身份**：数学家、神学家/牧师（"English clergyman and mathematician"）、密码学家（1643–1689 为议会及王室首席密码官）
- **家庭**：父 Revd. John Wallis（牧师）、母 Joanna Chapman，五子女中排行第三；1645-03-14 娶 Susanna Glynde，育 3 子女（Anne、John（Wallingford 议员）、Elizabeth）；孙子 William Blencowe 继任安妮女王密码官
- **教育轨迹**：
  - Tenterden 文法学校 1625–31（因瘟疫迁居）→ Felsted School 1631–32（师从 Martin Holbeach，首次接触数学）
  - Emmanuel College, Cambridge 1632–40（原打算学医）：B.A. 1637、M.A. 1640
  - Oxford D.D.（神学博士）1654
- **学术导师**：William Oughtred（1647 年数周内啃透其《Clavis Mathematicae》）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **沃利斯乘积**（*Arithmetica Infinitorum*, 1656，插值法导出）：`π/2 = 2/1 · 2/3 · 4/3 · 4/5 · 6/5 · 6/7 ⋯`——π 的无穷连乘积。
2. **无穷符号 ∞**：以 ∞ 表无穷、以 1/∞ 表无穷小——原文措辞 "He is credited with introducing the symbol ∞"（圆锥曲线论著处作 "Wallis popularised the symbol ∞"）。
3. **《Arithmetica Infinitorum》1656**："the most important of Wallis's works"——系统化并扩展 Descartes 与 Cavalieri 的方法，直接启发了牛顿（牛顿 1664 年读到此书）。
4. **分数指数记号**：将幂记号推广到有理数——`x⁰=1`、`x^(1/2)=√x`、`x^(p/q)=q次√(x^p)`。
5. **积分求积**：证明 y=x^m 与 x 轴间面积之比 1/(m+1)，扩展卡瓦列里求积公式。
6. **圆锥曲线的解析定义**（1655）：最早把圆锥曲线定义为二次曲线的书，"It helped to remove some of the perceived difficulty and obscurity of René Descartes' work on analytic geometry"。
7. **插值原理**：为求圆求积奠定插值法原理（导出沃利斯乘积）。
8. **连分数**：《Opera Mathematica》I (1695) 引入术语 "continued fraction"。
9. **数轴与负数**：1685 年用 "+3 yards forward / −3 yards backward" 为负数辩护，"Wallis has been credited as the originator of the number line"。
10. **密码学**：1643–1689 为议会及王室首席密码官；1642 年两小时破译 Chichester 密信起家；1697 年**拒绝**莱布尼茨的密码学请教。
11. **语音学与聋哑人教育**：参与设计教聋童说话的体系（与 William Holder 有功劳之争）。
12. **碰撞理论**：1668 年与 Wren、惠更斯各自给出动量守恒解，沃利斯兼论非完全弹性碰撞。
13. **Hobbes–Wallis 论战**：与霍布斯的长期数学论战（infobox Known for 明确列出）。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（牛津蓝） | `#1E3A5F` | 牛津 Savilian 教席 / 英格兰 |
| 强调色（无穷金） | `#C9A227` | ∞ 符号 / 沃利斯乘积 |
| 分类色 1（无穷小分析 — 靛蓝） | `#4C5FD5` | Arithmetica Infinitorum / 乘积 |
| 分类色 2（代数与记号 — 青绿） | `#0E7C7B` | 分数指数 / 数轴负数 / 连分数 |
| 分类色 3（密码学 — 琥珀） | `#E07B30` | 议会首席密码官 |
| 分类色 4（神学与语音 — 玫红） | `#B76E79` | 牧师 / 聋哑人教育 / Hobbes 论战 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「∞ 无穷环 / 连乘积链」之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**斯图亚特时代典雅 / 沉稳绵长**（86 岁高龄的英格兰数学家）
- **匹配理由**：
  - 沃利斯横跨内战、复辟、光荣革命三个时代——需**沉稳、绵长**的配乐
  - "绵长" 匹配其 54 年 Savilian 教席与 ∞ 意象
  - "典雅" 匹配其牛津与宫廷背景
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列已统一采用，保持一致）
  - 备选：巴洛克 / 英国 17 世纪风格曲目（珀塞尔时代气质）
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「无穷的符号 · ∞ 与沃利斯乘积」+ 约翰·沃利斯 1616–1703 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒含新旧历 / 国籍 / 出生地 / 职业 / 教育 / 核心领域）
3. **沃利斯的一生：时间线**（`\timelineslide`）：1616 出生 → 1632 Felsted 初遇数学 → 1640 剑桥 M.A. → 1643 首席密码官 → 1649 任 Savilian 教席 → 1656 《Arithmetica Infinitorum》→ 1685 《Algebra》→ 1703 去世
4. **早年与教育**（`\earlyslide`）：肯特牧师之家、Felsted 的 Holbeach（十年前也教过巴罗）、剑桥学医未成、"数学在当时不被看作学院学问"的自我回忆
5. **沃利斯乘积**（核心贡献页，表格 + 公式框）：`π/2 = ∏(4n²/(4n²−1))`、插值法导出
6. **无穷符号 ∞**（核心贡献页，表格 + 公式框）：以 ∞ 表无穷、1/∞ 表无穷小（措辞用"引入/推广"）
7. **《Arithmetica Infinitorum》**（核心贡献页，表格 + 公式框）：扩展卡瓦列里、∫x^m 面积比 1/(m+1)、启发牛顿
8. **分数指数与代数记号**（核心贡献页，表格 + 公式框）：`x^(p/q)`、连分数术语、公式化表达
9. **数轴与负数**（核心贡献页，表格 + 公式框）："+3 forward / −3 backward"、数轴起源
10. **圆锥曲线的解析定义**（核心贡献页，表格 + 公式框）：二次曲线定义、化解笛卡尔的晦涩
11. **密码学家沃利斯**（表格）：1642 Chichester 密信、为议会与宫廷服务、拒教莱布尼茨
12. **论战与争议**（表格）：Hobbes–Wallis 论战、聋哑人教育功劳之争（Holder 的讥讽）
13. **荣誉与传承**（表格）：Savilian 几何教席 54 年、小行星 31982 Johnwallis、对牛顿的影响
14. **终章**：86 岁、"牛顿之前英国最重要的数学家"的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **新旧历**：infobox 为新历在前（1616-12-03 [O.S. 11-23]；1703-11-08 [O.S. 10-28]）；metadata.json 存的是**旧历**——统一用新历并可括注旧历。
- **∞ 符号"首创"问题**：infobox Known for 写 "Inventing the symbol ∞"，但正文只说 "is credited with introducing" / "popularised"——slide 用「引入/推广」，勿写"发明"。
- **Savilian 教席任命背景**：原文 "Wallis seems to have been chosen largely on political grounds ... he had no particular reputation as a mathematician."——1649 年获聘时他**还不是知名数学家**（议会清党罢免前任），是后来的工作证明任命正确，勿写"以数学声誉获聘"。
- **FRS 年份**：page.md 与 metadata 均未给出皇家学会当选年份，只说 "joined the group of scientists that was later to evolve into the Royal Society"——勿写具体年份。
- **密码学时段**："Between 1643 and 1689..." 与"复辟后一度未被续聘、1689 光荣革命后再起用"两处表述并存——写年份区间需谨慎。
- **聋哑人教育功劳之争**：Holder 指责沃利斯 "rifling his Neighbours, and adorning himself with their spoyls"——功劳有争议，如实呈现。
- **死因**：page.md 未载——勿杜撰。
- **与牛顿关系**：page.md 仅称 "He was a contemporary of Isaac Newton"——勿加戏为师生/深交。
- **教育经历**：Emmanuel College 原打算学医；1644 当选 Queens' College fellow，因结婚辞职。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q208359 | 待写入 |
| name_zh | 约翰·沃利斯 | 待写入 |
| name_en | John Wallis | 待写入 |
| birth_date | 1616-12-03 | 待写入 |
| death_date | 1703-11-08 | 待写入 |
| nationality | United Kingdom（Kingdom of England） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / infinitesimal calculus / algebra / cryptography | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：William Oughtred（《Clavis Mathematicae》自修）
- **学生 / 提携**：William Brouncker（Brouncker 连分数）、William Neile（半三次抛物线求长）
- **通信 / 学术**：Henry Oldenburg（皇家学会秘书）、Leibniz（关系友好但拒教密码学）
- **论战 / 竞争**：Thomas Hobbes（Hobbes–Wallis 论战）、William Holder（聋哑人教育功劳）、Pierre de Fermat（优先权之争，见费马页）
- **家庭**：父 Revd. John Wallis、妻 Susanna Glynde、3 子女

## 8. 奖项清单

- page.md/metadata 无奖项与 FRS 年份记载——奖项页如实写"无近代意义奖项"；荣誉体现为 Savilian 教席 54 年、小行星 31982 Johnwallis、∞ 与沃利斯乘积以其命名

## 9. 机构清单

- 教育：Felsted School（1631–32）；Emmanuel College, Cambridge（B.A. 1637 / M.A. 1640）；Oxford D.D. 1654
- 任职：Queens' College fellow（1644，因婚辞职）；**Savilian Professor of Geometry, Oxford（1649–1703，54 年直至去世）**；Westminster Assembly 书记员（1643–49）；议会/王室首席密码官（1643–1689，有中断）

## 10. 终审清单

- [ ] 生卒 1616-12-03（O.S. 11-23）/ 1703-11-08（O.S. 10-28），享年 86，出生地 Ashford、逝世地 Oxford
- [ ] 国籍用「英国」，历史政权注明英格兰王国
- [ ] ∞ 符号用"引入/推广"，勿写"发明"
- [ ] Savilian 教席"政治因素任命、非以数学声誉"表述准确
- [ ] FRS 年份不写（原文无载）
- [ ] 密码学年份区间谨慎表述
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/John_Wallis/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 Wikimedia Commons/NPG 下载沃利斯肖像，失败则装饰圆占位
- [ ] **国籍**：封面顶部徽章明示英国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 "+3, signifies 3 Yards Forward; and −3, signifies 3 Yards Backward."）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（巴罗 / 格雷戈里 / 牛顿）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
