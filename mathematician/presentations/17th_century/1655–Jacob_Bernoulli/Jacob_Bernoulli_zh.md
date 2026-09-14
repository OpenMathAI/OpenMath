# Jacob Bernoulli（雅各布·伯努利）立传提示词

> qid=Q122392 · 1655-01-06（旧历 1654-12-27）– 1705-08-16 · 瑞士数学家 · 17 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/Jacob_Bernoulli/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**注意：本地 images.txt 无肖像**（仅墓志铭照片与书影）；执行时从 Wikimedia Commons 下载雅各布·伯努利肖像（Nicholas Bernoulli after J. R. Huber 的通行画像）至 `images/jacob_portrait.jpg`；失败则用墓志铭照片或装饰圆 `\faIcon{user}` 占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 瑞士`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒（注新旧历）、国籍、出生地、家庭（新教香料商世家）、弟弟约翰、教育、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「对数螺线 / 概率树」之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 0.5 模板机制（执行立传前必读）

> 黄金参照 `Johann_Bernoulli/Johann_Bernoulli_zh.tex` 逐帧改写；机械要点（14 帧结构 / 共享封面 `\input{../../cover/openmath_page.tex}` / Makefile 复制改 MAIN / 肖像下载与装饰圆占位 / `make distclean && make` 编译循环 / 已知陷阱）见 **`17th_century/TEMPLATE_GUIDE.md`**。

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Jacob Bernoulli（德文 **Jakob**、英文 **James**、法文 **Jacques**、拉丁署名 *Jacobus Bernoullius*；为与 Jakob II 区分有时称 Jacob I Bernoulli）——中文：雅各布·伯努利，slide 全篇统一"雅各布"
- **生卒**：**1655-01-06**（旧历 O.S. 1654-12-27）生于巴塞尔 → 1705-08-16 逝于巴塞尔，享年 50（墓志铭 "at the age of 50 years and 7 months"）。★ metadata 的 date_of_birth 1655-01-05 与 infobox 01-06 差一天，以 infobox 为准
- **国籍**：Switzerland（出生时属 Old Swiss Confederacy 瑞士邦联）
- **身份**：数学家、物理学家、医师、大学教授（metadata）；巴塞尔大学教授逾 18 年
- **家庭**：新教香料商世家（父系两代），"His mother was born into a family engaged in banking and city governing"——父名 page.md 未载，身份页写"巴塞尔新教香料商世家"；**弟弟 Johann Bernoulli**（约翰，先随兄学习后成对手）；1684 年娶 Judith Stupanus，育二子（墓志铭 "his wife for 20 years, and his two children"）
- **教育轨迹**：**巴塞尔大学**——遵父愿学神学并准备担任牧职，"But contrary to the desires of his parents, he also studied mathematics and astronomy"；D.Th. 1676（论文 *Primi et Secundi Adami Collatio*，导师 Peter Werenfels）、Dr. phil. hab. 1684；1676–1682 游学欧洲（研读 Hudde、Boyle、Hooke 等最新成果）
- **学术引路人**：莱布尼茨（1684 年起与弟研读其《Nova methodus》与 von Tschirnhaus 论文；infobox 记莱布尼茨为 epistolary correspondent）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **大数定律的第一版**："he derived the first version of the law of large numbers in his work *Ars Conjectandi*"——墓志铭所谓 **Golden Theorem（黄金定理）**。
2. **《猜度术》Ars Conjectandi（1713，死后八年出版）**：组合学综述 + 伯努利数与指数级数 + 概率论（a priori/a posteriori、数学期望与道德期望）+ 大数定律；**"Bernoulli trial"（伯努利试验）一词由此而来**；"The work was incomplete at the time of his death"。
3. **常数 e 的最早逼近（1683）**：研究复利得 `lim_{n→∞}(1+1/n)^n`，"Bernoulli only calculated this constant far enough to determine that its value was greater than 2.5 and less than 3"——e 之名由**欧拉后命名**。
4. **调和级数发散**：∑1/n 发散——伯努利以为首创，实为 Mengoli（40 年前）与 Oresme（14 世纪）先证——**易错点**。
5. **∑1/n² 收敛但未得闭式**：证明收敛且极限 < 2——巴塞尔问题的前奏（欧拉 1737 解决）。
6. **等时线（tautochrone，1690）**：化为一阶非线性微分方程并以**分离变量**求解；**"integral"（积分）一词首次以积分含义出现**（*Acta Eruditorum*）。
7. **伯努利微分方程（1696）**：`y' = p(x)y + q(x)yⁿ`。
8. **伯努利数**：《猜度术》中给出（幂和公式）。
9. **对数螺线 spira mirabilis 与双纽线（1694）**：渐伸线/渐屈线一般方法、caustics 研究；**墓志铭刻对数螺线**——"Eadem mutata resurgo"（虽经变化，我故我重来）。
10. **变分法共同奠基**："he, along with his brother Johann, was one of the founders of the calculus of variations"。
11. **兄弟之争**："the atmosphere of collaboration between the two brothers turned into rivalry... By 1697, the relationship had completely broken down"——公开互攻、互出难题。
12. **莱布尼茨学派的旗手**："He sided with Gottfried Wilhelm Leibniz during the Leibniz–Newton calculus controversy and was an early proponent of Leibnizian calculus."

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（巴塞尔红） | `#8B1A1A` | 瑞士 / 伯努利家族 |
| 强调色（螺线金） | `#C9A227` | 对数螺线 / Eadem mutata resurgo |
| 分类色 1（概率 — 靛蓝） | `#4C5FD5` | 猜度术 / 大数定律 / 伯努利试验 |
| 分类色 2（分析与曲线 — 青绿） | `#0E7C7B` | 等时线 / 对数螺线 / 双纽线 |
| 分类色 3（常数与级数 — 琥珀） | `#E07B30` | e 的逼近 / 调和级数 / 伯努利数 |
| 分类色 4（家族与传承 — 玫红） | `#B76E79` | 伯努利王朝 / 与约翰的竞争 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「对数螺线的自我相似 / 概率树分叉」之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**巴塞尔的严谨 / 巴洛克晚风**（伯努利数学王朝的开创者）
- **匹配理由**：
  - 雅各布是家族数学王朝第一人——需**严谨、绵长**的配乐
  - "严谨" 匹配其概率论与"最多正直"的评语（"there is a maximum of integrity"）
  - "绵长" 匹配对数螺线"虽经变化、故我重来"的墓志铭意象
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列已统一采用，保持一致）
  - 备选：巴洛克 / 17–18 世纪之交风格曲目
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「概率论先驱 · 大数定律」+ 雅各布·伯努利 1655–1705 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒含新旧历 / 国籍 / 出生地 / 家庭 / 教育 / 核心领域）
3. **雅各布·伯努利的一生：时间线**（`\timelineslide`）：1655-01-06 巴塞尔出生 → 1676 D.Th. / 开始游学 → 1682 游学归来 → 1684 成婚 / Dr. phil. / 读莱布尼茨 → 1687 巴塞尔数学教授 → 1690 等时线（"integral"首用）→ 1696 伯努利方程 → 1697 与弟决裂 → 1705-08-16 去世 → 1713 《猜度术》出版
4. **早年与教育**（`\earlyslide`）：香料商世家、违父愿学数学与天文、神学学位、1676–1682 游学
5. **《猜度术》与大数定律**（核心贡献页，表格 + 公式框）：黄金定理、"Bernoulli trial"得名、死后八年出版
6. **常数 e 的最早逼近**（核心贡献页，表格 + 公式框）：`(1+1/n)^n`、2.5 < e < 3、欧拉后命名
7. **级数与伯努利数**（核心贡献页，表格 + 公式框）：调和级数发散（Mengoli/Oresme 先证注记）、∑1/n² < 2、伯努利数
8. **等时线与"积分"的诞生**（核心贡献页，表格 + 公式框）：1690 论文、分离变量、integral 一词首次以积分含义出现
9. **伯努利微分方程**（核心贡献页，表格 + 公式框）：`y' = p(x)y + q(x)yⁿ`
10. **对数螺线与双纽线**（核心贡献页，表格 + 公式框）：spira mirabilis、渐伸线一般方法、1694 双纽线
11. **变分法的共同奠基**（核心贡献页，表格 + 公式框）：与约翰共同奠基 calculus of variations
12. **兄弟之争**（表格）：合作转竞争、公开互攻、1697 决裂；与莱布尼茨结盟
13. **荣誉与传承**（表格）：巴塞尔教授 18 年、巴黎/柏林科学院成员（墓志铭）、伯努利家族王朝之始
14. **终章**：50 岁、对数螺线墓志铭（工匠误刻阿基米德螺线的轶事）与 "Eadem mutata resurgo" 的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **名字拼写**：Jakob/Jacob/James/Jacques/Jacobus 同一人——slide 统一"雅各布·伯努利（Jacob Bernoulli）"，首次出现可注明各语言拼写。
- **生日**：infobox **1655-01-06**（O.S. 1654-12-27）；metadata 1655-01-05 差一天——以 infobox 为准。
- **生卒**：1705-08-16 逝于巴塞尔，享年 50（50 岁 7 个月）；死因仅墓志铭 "Of a chronic illness, of sound mind to the end"（慢性病，神志清醒至终）——勿编具体病名。
- **巴塞尔教授 1687**：原文 "People believe he was appointed professor of mathematics at the University of Basel in 1687"（据信）——表述留有余地。
- **FRS 1699 误传**：page.md 全文未载；墓志铭写 "member of the Royal Academies of Paris and Berlin"（巴黎、柏林科学院）——**勿写皇家学会会员**。
- **调和级数**：伯努利误以为首证 ∑1/n 发散，实为 Mengoli/Oresme 先证——勿写"伯努利首证"。
- **e 的命名**：常数由雅各布逼近，"the number that Euler later named e"——勿写"伯努利命名 e"。
- **兄弟竞争分寸**：变分法是兄弟**共同**奠基（原文）；等时线 1690 论文系雅各布独作（但 Huygens 1687、Leibniz 1689 亦曾研究该曲线）；**勿把共同成果写成一人独解**；"1697 年关系彻底破裂"是原文表述。
- **《猜度术》出版**：1713 年、死后八年、"incomplete at the time of his death"——"由侄子 Nikolaus 出版"page.md 未载【存疑】，勿写死；受惠更斯《论赌博中的计算》启发（"Inspired by Huygens' work"）可写。
- **"大数定律"一词**：page.md 未提 Poisson 命名——可写"第一版大数定律/黄金定理"，"law of large numbers"一词的命名者勿写死。
- **metadata 冲突**：doctoral_advisor 含 Nicolas Malebranche（infobox 只列 Peter Werenfels；莱布尼茨为 epistolary correspondent）——表述为"神学导师 Werenfels、自学莱布尼茨微积分"。
- **极坐标**："极坐标引入者之一"page.md/metadata 均未提及——删去。
- **伯努利不等式**：infobox 有条目但原文未给公式——若用 (1+x)ⁿ ≥ 1+nx 需另行查证或注明通行形式。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q122392 | 待写入 |
| name_zh | 雅各布·伯努利 | 待写入 |
| name_en | Jacob Bernoulli | 待写入 |
| birth_date | 1655-01-06 | 待写入 |
| death_date | 1705-08-16 | 待写入 |
| nationality | Switzerland | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / probability / calculus / mechanics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：Peter Werenfels（神学论文导师）；Gottfried Wilhelm Leibniz（通信引路人，1684 起研读其微积分）
- **学生**：Jacob Hermann、Nicolaus I Bernoulli（侄）、Johann Bernoulli（弟，早期由其辅导数学）
- **通信 / 学术**：Gottfried Wilhelm Leibniz（微积分之争盟友）、Christiaan Huygens（概率论启发源，研读其《论赌博中的计算》）
- **竞争 / 嫌隙**：Johann Bernoulli（弟弟，公开互攻、1697 决裂）
- **家庭**：巴塞尔新教香料商世家；妻 Judith Stupanus（1684，二子女）；弟 Johann Bernoulli

## 8. 奖项清单

- 墓志铭载 "member of the Royal Academies of Paris and Berlin"（巴黎、柏林科学院成员）；荣誉体现为：伯努利数/伯努利试验/伯努利分布/伯努利微分方程/伯努利不等式以其命名、巴塞尔 Münster 墓志铭（对数螺线）

## 9. 机构清单

- 教育：University of Basel（D.Th. 1676 / Dr. phil. hab. 1684）
- 任职：University of Basel 数学教授（1687 据信，至 1705 去世）

## 10. 终审清单

- [ ] 生卒 1655-01-06（O.S. 1654-12-27）/ 1705-08-16，享年 50，出生地/逝世地均 Basel
- [ ] 国籍用「瑞士」（Old Swiss Confederacy）
- [ ] "1687 教授（据信）"、死因"慢性病"表述留有余地
- [ ] 勿写 FRS 1699（墓志铭为巴黎/柏林科学院）
- [ ] 调和级数"Mengoli/Oresme 先证"注记；e 由欧拉命名
- [ ] 兄弟竞争"合作转竞争、1697 决裂、变分法共同奠基"表述准确
- [ ] 《猜度术》"死后八年出版、未完稿、受惠更斯启发"表述准确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Jacob_Bernoulli/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 Wikimedia Commons 下载通行画像，失败则墓志铭照片/装饰圆占位
- [ ] **国籍**：封面顶部徽章明示瑞士
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如墓志铭 "Eadem mutata resurgo"、"the incomparable mathematician"）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（约翰·伯努利 / 莱布尼茨 / 惠更斯）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
