# Isaac Barrow（艾萨克·巴罗）立传提示词

> qid=Q207718 · 1630-10 – 1677-05-04 · 英国数学家/神学家 · 17 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/Isaac_Barrow/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**注意：本地 images.txt 无肖像**（仅书影与 Trinity 礼拜堂雕像照）；执行时从 Wikimedia Commons 下载 **Mary Beale 所绘巴罗肖像**（infobox 提及）至 `images/barrow_portrait.jpg`；失败则用 Trinity 雕像照或装饰圆 `\faIcon{user}` 占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒（生年仅月）、国籍、出生地、职业（数学家/神学家/希腊语学者）、教育、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「微分三角形 / 切线」之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 0.5 模板机制（执行立传前必读）

> 黄金参照 `Johann_Bernoulli/Johann_Bernoulli_zh.tex` 逐帧改写；机械要点（14 帧结构 / 共享封面 `\input{../../cover/openmath_page.tex}` / Makefile 复制改 MAIN / 肖像下载与装饰圆占位 / `make distclean && make` 编译循环 / 已知陷阱）见 **`17th_century/TEMPLATE_GUIDE.md`**。

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Isaac Barrow（The Reverend Isaac Barrow，中文：艾萨克·巴罗）
- **生卒**：1630 年 **10 月**（page.md 仅到月，**无具体日**）生于伦敦 → 1677-05-04 逝于伦敦，享年 46；葬于 Westminster Abbey；**未婚无子**（"Barrow died unmarried in London at the early age of 46"）
- **国籍**：Kingdom of England（英格兰），现代对应英国/英格兰
- **身份**：数学家、基督教神学家、希腊语学者（Regius Professor of Greek）、布道家（布道文为 "masterpieces of argumentative eloquence"）
- **家庭**：父 Thomas Barrow（亚麻布商）；母 Ann（约 1634 年去世），巴罗似为唯一活过婴孩期的孩子；父再娶 Katherine Oxinden
- **教育轨迹**：
  - Charterhouse School（顽劣——父曾祷告 "if it pleased God to take any of his children he could best spare Isaac"）
  - Felsted School（师从清教徒校长 Martin Holbeach——**十年前也教过约翰·沃利斯**；习希腊语、希伯来语、拉丁语、逻辑）
  - Trinity College, Cambridge（Walpole 家族资助入学）：1648 学位、1649 fellow、1652 M.A.（导师 James Duport）
  - 1655–1659 游学法国、意大利、土耳其（İzmir、Istanbul），1659 返英；旅途中曾从海盗手中救下所乘船只
- **导师**：James Duport（古典学 mentor）；数学真正的学习对象是 **Gilles Personne de Roberval**（巴黎）与 **Vincenzo Viviani**（佛罗伦萨）——infobox 注释明确区分

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **微积分基本定理的早期证明**："generally given credit for his early role in the development of infinitesimal calculus; in particular, for a proof of the fundamental theorem of calculus"——FTC 的先驱。
2. **微分三角形（巴罗三角形）**：在曲线上 P 点邻点 Q 处作小三角形 PQR，"which he called the differential triangle, because its sides QR and RP were the differences of the abscissae and ordinates of P and Q"。
3. **实质是微分学程序**：原文明确对照 "This is exactly the procedure of the differential calculus, except that there we have a rule by which we can get the ratio a/e or dy/dx directly without the labour..."——差的比即导数。
4. **切线法的应用**：抛物线 y²=px 得 TM=2x；kappa 曲线切线的首算者；应用于 x³+y³=r³、笛卡尔叶形线、割圆曲线等。
5. **正割函数积分闭式的首得**："Barrow was the first to find the integral of the secant function in closed form"。
6. **光学者作**：《Lectiones Opticae et Geometricae》（1669）——反射折射、几何焦点定义、薄透镜性质，"considerably simplified the Cartesian explanation of the rainbow"。
7. **首任卢卡斯教授（1663）**：剑桥 Lucasian Professor of Mathematics 首任；**1669 年辞职让与牛顿**——"In 1669 he resigned his professorship in favour of Isaac Newton."
8. **古典数学译注**：欧几里得《几何原本》拉丁本（1655/1659）与英译（1660）、《Data》（1657）、阿波罗尼奥斯《圆锥曲线论》（1675）、阿基米德《著作集》（1675）、Theodosius《球面学》（1675）。
9. **《Lectiones Mathematicae》（1664–66 讲稿）**："mostly on the metaphysical basis for mathematical truths"；1667 年讲稿提示阿基米德主要结果的分析思路。
10. **神学著述**：《Expositions of the Creed, The Lord's Prayer, Decalogue, and Sacraments》等；1672 年任 Trinity College Master 并**创建学院图书馆**。
11. **三一学院学脉**：巴罗→牛顿的卢卡斯教席交接（1663 首任 → 1669 牛顿接任，26 岁）。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（三一蓝） | `#2B5F75` | 剑桥三一学院 / 英格兰 |
| 强调色（先驱金） | `#C9A227` | 微积分基本定理先驱 / 首任卢卡斯教授 |
| 分类色 1（微积分先驱 — 靛蓝） | `#4C5FD5` | 微分三角形 / FTC |
| 分类色 2（几何与切线 — 青绿） | `#0E7C7B` | 切线法 / kappa 曲线 |
| 分类色 3（光学 — 琥珀） | `#E07B30` | Lectiones Opticae / 彩虹 |
| 分类色 4（古典学与神学 — 玫红） | `#B76E79` | 欧几里得译注 / 布道文 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「微分三角形 / 切线束」之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**剑桥古典 / 庄重虔诚**（学者-牧师双面人生）
- **匹配理由**：
  - 巴罗是数学家与神学家的合体——需**庄重、虔诚**的配乐
  - "古典" 匹配其希腊语教席与古籍译注
  - "庄重" 匹配其三一学院 Master 与 Westminster Abbey 长眠
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列已统一采用，保持一致）
  - 备选：巴洛克 / 英国圣公会合唱传统风格曲目
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「牛顿之师 · 微积分基本定理先驱」+ 艾萨克·巴罗 1630–1677 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 国籍 / 出生地 / 职业 / 教育 / 核心领域）
3. **巴罗的一生：时间线**（`\timelineslide`）：1630-10 伦敦出生 → Felsted → 1648 三一学院 → 1655–59 游学欧陆（Roberval/Viviani）→ 1660 Regius 希腊语教授 → 1662 Gresham 几何 → 1663 首任卢卡斯教授 → 1669 让与牛顿 → 1672 三一学院 Master → 1677 去世
4. **早年与教育**（`\earlyslide`）：伦敦布商之家、Charterhouse 的顽童祷告轶事、Felsted 的 Holbeach、三一学院与游学
5. **微分三角形与切线法**（核心贡献页，表格 + 公式框）：PQR 小三角形、TM:MP = QR:RP、"exactly the procedure of the differential calculus"
6. **微积分基本定理的早期证明**（核心贡献页，表格 + 公式框）："a proof of the fundamental theorem of calculus"
7. **正割积分与曲线应用**（核心贡献页，表格 + 公式框）：∫sec x 首得闭式、kappa 曲线、叶形线
8. **光学的几何化**（核心贡献页，表格 + 公式框）：反射折射、薄透镜、简化笛卡尔彩虹理论
9. **首任卢卡斯教授与让位牛顿**（表格）：1663 首任、1669 辞职"resigned in favour of Isaac Newton"、牛顿校订的仅是光学部分
10. **古典数学的守护者**（表格）：欧几里得/阿波罗尼奥斯/阿基米德译注
11. **神学家与布道家**（表格）：神学著述、布道文"argumentative eloquence"、1672 三一学院 Master 与图书馆
12. **师承与游学**（表格）：Duport（古典学）、Roberval（巴黎）、Viviani（佛罗伦萨）、海盗脱险轶事
13. **荣誉与传承**（表格）：三教席（希腊语/Gresham/Lucasian）、Westminster Abbey、月球环形山 Barrow、FTC 先驱地位
14. **终章**：46 岁、"为牛顿铺路的人"的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **出生日期**：page.md 仅 "October 1630"，**无具体日**；metadata 的 `1630-10-00` 亦缺日——封面写"1630 年 10 月"，任何具体出生日都是外加的。
- **"让位"动机**：page.md 只写 "In 1669 he resigned his professorship in favour of Isaac Newton."——**未解释动机**；流行的"慧眼识珠主动让贤"说法在本页无依据，slide 不应写成有史料支撑的动机叙述。
- **牛顿校订讲稿的范围**："it seems probable ... the additions were confined to the parts which dealt with optics."——勿笼统说牛顿"修订其数学讲义"，更可能仅光学部分。
- **导师表述**：Duport 是古典学 mentor；数学学习对象是 Roberval（巴黎）与 Viviani（佛罗伦萨）——勿把 Duport 写成数学导师。
- **《Lectiones》书名与年份**：正文 "In 1669 he issued his Lectiones Opticae et Geometricae"（合订）vs Publications 列表《Lectiones Opticae》1669 /《Lectiones Geometricae》1670 分列——引用注明版本。
- **FRS 年份**：metadata 有 Fellow of the Royal Society 记录，但 page.md **未给年份**——勿写具体年份。
- **死因**：John Aubrey《Brief Lives》归因于"在土耳其期间染上的鸦片瘾"——**传闻性质**，引用须注明出处（Aubrey）。
- **未婚无子**："Barrow died unmarried in London at the early age of 46, and was buried at Westminster Abbey."——事实呈现即可。
- **称号**："牛顿之师"可用（1663–1669 卢卡斯教席的上下级 + 1669 交接事实）；"微积分基本定理先驱"用原文 "early role in the development of infinitesimal calculus; in particular, for a proof of the fundamental theorem of calculus"。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q207718 | 待写入 |
| name_zh | 艾萨克·巴罗 | 待写入 |
| name_en | Isaac Barrow | 待写入 |
| birth_date | 1630-10（仅年月） | 待写入 |
| death_date | 1677-05-04 | 待写入 |
| nationality | United Kingdom（Kingdom of England） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / geometry / optics / theology | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：James Duport（古典学 mentor，Trinity）；Gilles Personne de Roberval（巴黎，数学）；Vincenzo Viviani（佛罗伦萨，数学）
- **学生**：Isaac Newton（卢卡斯教席交接 1669）
- **恩主 / 提携**：Charles II（机智获宠、1670 Royal mandate 授 D.D.）；Walpole 家族（入学资助）
- **通信 / 学术**：John Collins（学术通信枢纽，牛顿《De analysi》经由巴罗转交）
- **家庭**：父 Thomas Barrow（亚麻布商）、母 Ann（早逝）；未婚无子

## 8. 奖项清单

- 无近代意义奖项记载（FRS 见 metadata 但年份原文无）；荣誉体现为：首任卢卡斯教授、三教席、月球环形山 Barrow、Westminster Abbey 长眠、FTC 先驱地位

## 9. 机构清单

- 教育：Charterhouse School；Felsted School；Trinity College, Cambridge（1648 学位 / 1649 fellow / 1652 M.A.）
- 任职：Regius Professor of Greek, Cambridge（1660）；Gresham College 几何教授（1662）；**首任 Lucasian Professor of Mathematics（1663–1669）**；Trinity College Master（1672–1677，创建学院图书馆）

## 10. 终审清单

- [ ] 生卒"1630 年 10 月"（无日）/ 1677-05-04，享年 46，出生地/逝世地均 London
- [ ] 国籍用「英国」，历史政权注明英格兰王国
- [ ] "1669 辞职让与牛顿"不写动机叙事
- [ ] 牛顿校订讲稿"限于光学部分"限定语在位
- [ ] 导师 Duport/Roberval/Viviani 区分准确
- [ ] 死因"Aubrey 称鸦片瘾"注明传闻出处
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Isaac_Barrow/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 Wikimedia Commons 下载 Mary Beale 肖像，失败则 Trinity 雕像照/装饰圆占位
- [ ] **国籍**：封面顶部徽章明示英国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 "This is exactly the procedure of the differential calculus..."）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（沃利斯 / 格雷戈里 / 牛顿）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
