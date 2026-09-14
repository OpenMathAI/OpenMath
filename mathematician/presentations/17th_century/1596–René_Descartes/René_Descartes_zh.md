# René Descartes（勒内·笛卡尔）立传提示词

> qid=Q9191 · 1596-03-31 – 1650-02-11 · 法国数学家/哲学家 · 17 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/René_Descartes/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。使用 images.txt 中的 **Jan Baptist Weenix 肖像**（下载至 `images/descartes_portrait.jpg`）；勿用传统归于 Frans Hals 的那张（归属存疑，见 §5）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、国籍、出生地、父亲职业、教育、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「笛卡尔坐标系 / 坐标网格」的理性之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 0.5 模板机制（执行立传前必读）

> 黄金参照 `Johann_Bernoulli/Johann_Bernoulli_zh.tex` 逐帧改写；机械要点（14 帧结构 / 共享封面 `\input{../../cover/openmath_page.tex}` / Makefile 复制改 MAIN / 肖像下载与装饰圆占位 / `make distclean && make` 编译循环 / 已知陷阱）见 **`17th_century/TEMPLATE_GUIDE.md`**。

## 1. 背景信息（用于 Slide 1-3）

- **全名**：René Descartes（拉丁化 Renatus Cartesius，中文：勒内·笛卡尔）
- **生卒**：1596-03-31 生于 La Haye en Touraine（今法国 Descartes 镇，安德尔-卢瓦尔省）→ 1650-02-11 逝于斯德哥尔摩（瑞典帝国，Chanut 家中），享年 53
- **国籍**：法国（Kingdom of France）；逝于瑞典
- **身份**：哲学家、数学家、物理学家、音乐理论家、作家、polymath（metadata 列 mechanical automaton engineer、military personnel 等）
- **家庭**：父 Joachim Descartes（雷恩高等法院成员）、母 Jeanne Brochard（1597 年产死胎后数日去世，笛卡尔由外祖母抚养长大）；未婚，与女仆 Helena Jans van der Strom 生一女 Francine（1635 生，5 岁死于猩红热）
- **宗教**：家庭与本人均为罗马天主教；后半生生活在信奉新教的荷兰与瑞典
- **教育轨迹**：
  - 1607–1614 拉弗莱什耶稣会学院（因体弱入学晚）
  - 1615–1616 普瓦捷大学，1616 获教会法与民法 Baccalauréat 与 Licence（LL.B.）
  - 1629 弗拉讷克大学旁听（Adriaan Metius）；1630 莱顿大学旁听（数学随 Jacobus Golius、天文随 Martin Hortensius）
  - 1618–1620 从军（荷兰联省军队，随 Maurice of Nassau；后随巴伐利亚军，1620 白山战役在场）
- **导师/引路人**：Isaac Beeckman（1618 布雷达相识，物理兴趣的起点）；infobox Academic advisors 另列 Golius、Metius、Étienne Noël

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **方法论怀疑（Cartesian doubt）**：以普遍怀疑重建知识根基——"怀疑是土壤，新知识是其上的建筑"。
2. **"我思故我在"**：`Cogito, ergo sum`（法语 Je pense, donc je suis），其哲学第一原理。
3. **解析几何与笛卡尔坐标系**：连接此前分离的几何与代数，被誉为**解析几何之父**——本系列立传的核心定位。
4. **《La Géométrie》（1637）**：《方法谈》三篇附录之一，数学代表作。
5. **笛卡尔符号法则** 与**笛卡尔叶形线**（`x³+y³=3axy`）、**法线法**（method of normals）。
6. **运动量守恒与三条运动定律**：《哲学原理》中的体系，"Newton's own laws of motion would later be modeled on Descartes's exposition"——牛顿运动定律的先驱（注意：守恒的是 size×speed，非现代动量）。
7. **功的概念先声**（1637）："举 100 磅 2 次 1 英尺 = 举 200 磅 1 英尺 = 举 100 磅 2 英尺"。
8. **光学**：用折射定律推出彩虹角半径 42°；折射定律在法国称"笛卡尔定律"；其光学论文首次发表反射定律。
9. **以太旋涡说（vortices）与充实主义（plenism）**：以旋涡解释重力；《Le Monde》因伽利略案不敢出版。
10. **磁素（effluvia）说**："a predecessor of the concept of magnetic field"。
11. **心身二元论**与蜡块论证；《沉思集》《方法谈》《哲学原理》构成近代哲学起点。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（笛卡尔蓝） | `#2B4C7E` | 理性主义 / 坐标系 |
| 强调色（理性金） | `#C9A227` | 近代哲学之父 / 解析几何 |
| 分类色 1（解析几何 — 靛蓝） | `#4C5FD5` | 笛卡尔坐标系 / La Géométrie |
| 分类色 2（方法论 — 青绿） | `#0E7C7B` | 方法论怀疑 / 我思故我在 |
| 分类色 3（光学与物理 — 琥珀） | `#E07B30` | 折射定律 / 运动定律 |
| 分类色 4（哲学思辨 — 玫红） | `#B76E79` | 心身二元论 / 旋涡说 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「坐标网格 / 解析几何」的理性秩序之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**巴洛克典雅 / 理性沉静**（17 世纪上半叶法国理性主义奠基人）
- **匹配理由**：
  - 笛卡尔是近代哲学与解析几何的奠基者——需**沉静、理性、典雅**的配乐
  - "理性" 匹配其方法论怀疑与几何化宇宙观
  - "典雅" 匹配其法国贵族出身与巴洛克时代
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列欧拉、高斯、梅森等已统一采用，保持一致）
  - 备选：巴洛克 / 法国 17 世纪风格曲目
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「解析几何之父 · 我思故我在」+ 勒内·笛卡尔 1596–1650 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 国籍 / 出生地 / 父亲职业 / 教育 / 核心领域）
3. **勒内·笛卡尔的一生：时间线**（`\timelineslide`）：1596 出生 → 1607 拉弗莱什 → 1616 普瓦捷 LL.B. → 1618 从军遇 Beeckman → 1628 移居荷兰 → 1637 《方法谈》→ 1641 《沉思集》→ 1644 《哲学原理》→ 1649 赴瑞典 → 1650 去世
4. **早年与教育**（`\earlyslide`）：拉弗莱什耶稣会学院、弃笔从军、Beeckman 引路、定居荷兰二十年
5. **解析几何与笛卡尔坐标系**（核心贡献页，表格 + 公式框）：连接代数与几何、《La Géométrie》1637
6. **方法论怀疑与我思故我在**（核心贡献页，表格 + 公式框）：普遍怀疑、`Cogito, ergo sum`
7. **笛卡尔符号法则与叶形线**（核心贡献页，表格 + 公式框）：符号法则、`x³+y³=3axy`、法线法
8. **运动定律与运动量守恒**（核心贡献页，表格 + 公式框）：三条运动定律、牛顿的先驱
9. **光学与折射定律**（核心贡献页，表格 + 公式框）：彩虹 42°、"笛卡尔定律"、反射定律首次发表
10. **旋涡说与磁素说**（核心贡献页，表格 + 公式框）：以太旋涡解释重力、磁场概念先声
11. **心身二元论**（表格）：《沉思集》1641、蜡块论证
12. **学者网络与论战**（表格）：Mersenne 通信、伊丽莎白公主六年通信、与乌得勒支大学 Voetius 之争、1643 被迫出逃
13. **荣誉与身后**（表格）：瑞典女王 Christina 延请、1663 著作入禁书目录、1819 改葬圣日耳曼德佩
14. **终章**：53 岁、"近代哲学之父 / 解析几何之父"的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **肖像归属**：最著名的"哈尔斯肖像"归属存疑——原文 "Although the uncertain authorship of this most iconic portrait of Descartes was traditionally attributed to Frans Hals, there is no record of their meeting."——封面用 **Weenix 肖像**（images.txt 有链接），勿标注"哈尔斯作"。
- **生卒**：1596-03-31 生、1650-02-11 逝于斯德哥尔摩，享年 53——封面用此口径。
- **出生地**：page.md 为 "La Haye en Touraine (now Descartes)"；metadata 的 place_of_birth "Descartes" 是**现代地名**——封面写"拉艾-图赖讷（今笛卡尔镇）"。
- **死亡叙事**："瑞典严冬冻死笛卡尔"是简化叙事——原文指出 "The winter seems to have been mild"（冬大部分时间温和），死因为 1650-02-01 患肺炎、02-11 去世；死因另有争议（peripneumonia 说法、御医放血被阻等），勿写成"冻死"定论。
- **1619 年"炉中三梦"**：出自 Adrien Baillet 的记载，属传说性质——引用需注明出处，勿当定史。
- **乌得勒支大学**：metadata educated_at 含 Utrecht University，但 page.md 从未记载——**弃用**；1643 年乌得勒支反而谴责其哲学、迫其出逃。
- **《Le Monde》与伽利略案**：1633 年闻伽利略受审后不敢出版（哥白尼立场），此为《方法谈》1637 才问世的原因之一——表述准确。
- **与费马的关系**：解析几何有优先权之争，page.md 中 "In La Géométrie, Descartes exploited the discoveries he made with Pierre de Fermat" 措辞含混——表述为"与费马各自独立发展解析几何，存在优先权争议"。
- **动量守恒**：笛卡尔守恒的是 size×speed（速率而非矢量速度），非现代动量守恒——勿写"提出动量守恒定律"。
- **生前著作并不畅销**：法文《沉思集》到他去世都没卖完一版——勿拔高"一经问世轰动欧洲"。
- **身后**：1663 著作被列入禁书目录、1671 路易十四禁止讲授笛卡尔主义——可如实提及。
- **称号**：可用"近代哲学之父""解析几何之父"；**勿写"发明了坐标系"**（坐标思想先有阿波罗尼奥斯/奥雷姆等渊源，笛卡尔是系统化者）。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q9191 | 待写入 |
| name_zh | 勒内·笛卡尔 | 待写入 |
| name_en | René Descartes | 待写入 |
| birth_date | 1596-03-31 | 待写入 |
| death_date | 1650-02-11 | 待写入 |
| nationality | France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / analytic geometry / philosophy / physics / optics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师 / 引路人**：Isaac Beeckman（物理兴趣起点，1630 年反目）、Jacobus Golius、Adriaan Metius、Étienne Noël
- **学生 / 提携**：Henricus Regius（一度追随，后反目）
- **通信 / 学术**：Marin Mersenne（挚友、学术中介）、波希米亚的伊丽莎白公主（六年通信，《论灵魂激情》题献）、Constantijn Huygens、Frans van Schooten、Girard Desargues、Pierre Chanut（瑞典东道主）
- **赞助人**：瑞典女王 Christina（1649 延请赴瑞典）
- **论战 / 竞争**：Voetius 与乌得勒支大学（1643 谴责）、Martin Schoock（指控无神论）、René Descartes vs Fermat（解析几何优先权）、Blaise Pascal（批评其哲学）、与 Beeckman 的剽窃指责（1630）
- **家庭**：父 Joachim Descartes（高等法院成员）、母 Jeanne Brochard（早逝）、女 Francine（早夭）

## 8. 奖项清单

- **无任何奖项或院士身份记载**（page.md/metadata 均无）——勿杜撰；其"荣誉"体现为近代哲学与解析几何的奠基地位

## 9. 机构清单

- 教育：Jesuit College of La Flèche（1607–1614）；University of Poitiers（LL.B. 1616）；Franeker / Leiden（旁听 1629–1630）
- 任职：荷兰联省军队与巴伐利亚军（1618–1620）；1649 受聘瑞典宫廷（讲授哲学/筹建科学院，实际授课仅四五次）
- 无正式大学教授职位（定居荷兰隐居著述二十年）

## 10. 终审清单

- [ ] 生卒 1596-03-31 / 1650-02-11，享年 53，出生地 La Haye en Touraine、逝世地 Stockholm
- [ ] 国籍用「法国」；出生地写"拉艾-图赖讷（今笛卡尔镇）"
- [ ] 死因"肺炎"表述准确，勿写"冻死"定论
- [ ] 封面用 Weenix 肖像，勿标注"哈尔斯作"
- [ ] 与费马解析几何"各自独立、有优先权之争"表述准确
- [ ] 运动量守恒"非现代动量守恒"限定语在位
- [ ] 弃用 metadata 的 Utrecht University
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/René_Descartes/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 Weenix 肖像（images.txt 已有链接，下载至 `images/`）
- [ ] **国籍**：封面顶部徽章明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 "Cogito, ergo sum"、帕斯卡的批评原句）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（梅森 / 费马 / 帕斯卡）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
