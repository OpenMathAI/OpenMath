# Bonaventura Cavalieri（博纳文图拉·卡瓦列里）立传提示词

> qid=Q214544 · 1598 – 1647-11-30 · 意大利数学家 · 17 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/17th_century/pages/Bonaventura_Cavalieri/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**注意：本地 images.txt 无本人肖像**，仅有 1844 年米兰布雷拉宫纪念雕像（可作备选）；执行时从 Wikimedia Commons 下载 infobox 所用《Trattato della sfera》(1682) 内页肖像或雕像图至 `images/cavalieri_portrait.jpg`；失败则用装饰圆 `\faIcon{user}` 占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 意大利`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、国籍、出生地、修会、导师、教育、核心领域。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆），母题呼应「不可分线束 / 无穷细分」的层叠之美。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Bonaventura Francesco Cavalieri（拉丁文名 Bonaventura Cavalerius，中文：博纳文图拉·卡瓦列里）
- **生卒**：1598 生于米兰（米兰公国，时属哈布斯堡西班牙；**仅知年份，具体日期 page.md 未载**）→ 1647-11-30 逝于博洛尼亚（教皇国），享年 48–49
- **国籍**：metadata 记 Duchy of Milan（米兰公国），现代对应意大利
- **身份**：数学家、天文学家、神学家
- **宗教身份**：**Jesuate（垫佐会/耶稣善会士）**——15 岁入会，1615 年（17 岁）正式宣誓；★ **不是耶稣会士**（page.md 原文 "not to be confused with the Jesuits"）
- **家庭**：父母与兄弟姐妹 page.md 无记载——身份信息页不写家庭栏或写"史料无载"
- **健康**：1626 年起患痛风（gout），行动受限终生；晚年关节炎致无法执笔，书信由学生代笔
- **教育轨迹**：1616 年起在比萨大学学几何，师从 Benedetto Castelli（经他可能引荐认识伽利略）；1620 回米兰任助祭、在 San Gerolamo 修道院学神学；后任 Lodi 圣彼得修道院院长

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **不可分法（method of indivisibles）**：以图形内"所有线/所有面"比较面积与体积，受伽利略早期思想启发——**积分学的先声**（"the precursors of infinitesimal calculus"）。
2. **《Geometria indivisibilibus》（1627 写成 / 1635 出版）**：作为博洛尼亚求职材料写成，系统阐述不可分法。
3. **卡瓦列里原理**：等距截面面积相等的两立体体积相等——page.md 特别指出中国**祖暅（480–525）**已在球体积特例上早用同一原理（"祖暅原理"）。
4. **积分结果**：算得 ∫₀¹ x² dx = 1/3（阿基米德螺线求积中）；在《Exercitationes geometricae sex》(1647) 推广得 ∫₀¹ xⁿ dx = 1/(n+1)（n=3,…,9）。
5. **圆锥体积**：证明圆锥体积为外接圆柱的三分之一。
6. **对数引入意大利**：出版对数表及用法，强调天文、地理实用价值。
7. **光学与反射性质**：《Lo Specchio Ustorio》(1632) 给出许多曲线反射性质的**第一个证明**；提出**三种反射镜望远镜方案**（远早于牛顿的实践）。
8. **光速有限的思想**：论证"若光速有限且确定，焦点成像干涉极小"（当时纯理论）。
9. **与伽利略通信**至少 112 封；1629 年经伽利略向博洛尼亚元老院推荐获**博洛尼亚大学数学讲席**（任职至去世）。
10. **后世地位**：据 Gilles-Gaston Granger，与牛顿、莱布尼茨、帕斯卡、沃利斯、麦克劳林并列"重新定义数学对象"的人物。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（米兰深红） | `#8B1A1A` | 米兰公国 / 意大利文艺复兴余晖 |
| 强调色（几何金） | `#C9A227` | 不可分法 / 积分先声 |
| 分类色 1（不可分法 — 靛蓝） | `#4C5FD5` | Geometria indivisibilibus |
| 分类色 2（积分先驱 — 青绿） | `#0E7C7B` | ∫xⁿ = 1/(n+1) / 卡瓦列里原理 |
| 分类色 3（光学 — 琥珀） | `#E07B30` | 反射望远镜构想 / 镜面反射 |
| 分类色 4（修会与传承 — 玫红） | `#B76E79` | Jesuate 修会 / 伽利略学派 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题呼应「不可分线束 / 无穷层叠」之美。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**文艺复兴晚风 / 虔敬沉静**（17 世纪意大利修会数学家）
- **匹配理由**：
  - 卡瓦列里是修会士+数学家——需**虔敬、沉静**的配乐
  - "沉静" 匹配其痛风缠身仍笔耕不辍的一生
  - 意大利文艺复兴向巴洛克过渡的时代气质
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：沿用系列曲目 **Timeless**（本系列已统一采用，保持一致）
  - 备选：17 世纪意大利 / 巴洛克早期风格曲目
  - 时长需 ≥ 14 页 × 7 秒 ≈ 98 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 14 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐梅森/伯努利模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「不可分法 · 积分学的先声」+ 博纳文图拉·卡瓦列里 1598–1647 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 国籍 / 出生地 / 修会 / 导师 / 教育 / 核心领域）
3. **卡瓦列里的一生：时间线**（`\timelineslide`）：1598 米兰出生 → 1615 入 Jesuate → 1616 比萨学几何（Castelli）→ 1629 博洛尼亚讲席 → 1632 《燃烧镜》→ 1635 《Geometria》出版 → 1647 去世
4. **早年与教育**（`\earlyslide`）：米兰、入垫佐会（非耶稣会！）、比萨师从 Castelli、伽利略的间接引荐
5. **不可分法**（核心贡献页，表格 + 公式框）：所有线/所有面、"comparable but not equal"的哲学谨慎
6. **卡瓦列里原理与祖暅**（核心贡献页，表格 + 公式框）：等距截面、中国祖暅（480–525）早用于球体积
7. **积分的先声**（核心贡献页，表格 + 公式框）：`∫₀¹ x² dx = 1/3`、`∫₀¹ xⁿ dx = 1/(n+1)`、圆锥体积
8. **《Geometria indivisibilibus》**（核心贡献页，表格 + 公式框）：1627 写成 / 1635 出版 / 1653 再版
9. **光学与反射望远镜构想**（核心贡献页，表格 + 公式框）：《燃烧镜》1632、三种反射镜方案、光速有限论证
10. **对数引入意大利**（核心贡献页，表格 + 公式框）：对数表与天文地理应用
11. **与 Guldin 的论战**（表格）：剽窃指控"without substance"、无穷可比性之争、1647 《六篇几何练习》回击
12. **伽利略学派网络**（表格）：与伽利略通信 112 封、与 Mersenne/Torricelli/Viviani 通信、学生 Stefano degli Angeli（metadata 亦记 Pietro Mengoli）
13. **荣誉与传承**（表格）：博洛尼亚大学讲席、月球环形山 Cavalerius、积分学前驱地位
14. **终章**：48–49 岁、"自阿基米德以来深入几何第一人"（伽利略语）的历史定位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **Jesuate ≠ Jesuit**：他是**垫佐会（Jesuate）士**，page.md 原文 "not to be confused with the Jesuits"——严禁写成耶稣会士。
- **出生日期**：page.md 仅 "1598"；metadata 的 `1598-01-01` 是 Wikidata 占位补日——封面写"1598 年"，勿写"1598-01-01"。
- **享年**：48–49 岁（infobox "aged 48–49"）——勿写精确 48 或 49。
- **《Geometria》年份**：1627 在帕尔马**写成**、**1635 才出版**（1653 再版）——勿混用。
- **卡瓦列里原理非他首创**：原文 "The same principle had been previously used by Zu Gengzhi (480–525) of China, in the specific case of calculating the volume of the sphere"——必须注明祖暅早于他近千年在球体积上使用。
- **Guldin 论战定性**：剽窃指控 "The charges of plagiarism were without substance"（无实据）；但 Cavalieri 的自辩 page.md 也评 "He argued, disingenuously"（略显言不由衷）、"These arguments were not convincing to contemporaries"——两面都要写，勿单方面洗白。
- **伽利略引荐是"可能"**：原文 "who probably introduced him to Galileo Galilei"——用"经 Castelli（可能）引荐"表述。
- **占星书 ≠ 信占星**：两本天文学著作用占星语言，但原文声明 "he did not believe in or practice astrology"；metadata field_of_work 的 "astrology" 是机械归类——勿写"占星学家"。
- **死因**：page.md "he died, probably of gout"（可能死于痛风）——勿写伤寒/疟疾。
- **学生**：Stefano degli Angeli 有 page.md 依据；Pietro Mengoli 仅见于 metadata（Wikidata），引用需标注来源。
- **无院士记录**：page.md/metadata 均无林琴学院等院士身份——不得虚构。
- **Tacquet 拼写**：page.md 正文拼 "Andre Taquet"，正确名 André Tacquet。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q214544 | 待写入 |
| name_zh | 博纳文图拉·卡瓦列里 | 待写入 |
| name_en | Bonaventura Cavalieri | 待写入 |
| birth_date | 1598（仅年份） | 待写入 |
| death_date | 1647-11-30 | 待写入 |
| nationality | Italy（Duchy of Milan） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematics / geometry / physics / optics / astronomy | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：Benedetto Castelli（比萨大学几何教师，metadata 亦记 doctoral advisor）；Galileo Galilei（间接引荐/通信导师，"probably introduced"）
- **赞助人**：枢机 Federico Borromeo、Cesare Marsili
- **学生（提携 / 指导）**：Stefano degli Angeli（page.md）；Pietro Mengoli（仅 metadata/Wikidata，注明来源）
- **通信 / 学术**：Galileo Galilei（≥112 封）、Marin Mersenne、Evangelista Torricelli、Vincenzo Viviani
- **论战 / 竞争**：Paul Guldin（剽窃指控与无穷可比性之争）、André Tacquet（回应其方法）
- **家庭**：史料无载

## 8. 奖项清单

- 无奖项/院士身份记载；荣誉体现为：博洛尼亚大学数学讲席（1629，伽利略推荐）、月球环形山 Cavalerius、与牛顿/莱布尼茨并列的"重新定义数学对象"评价（Granger）

## 9. 机构清单

- 教育：University of Pisa（1616 起学几何，师从 Castelli）
- 任职：University of Bologna 数学讲席教授（1629–1647，经伽利略推荐获任）
- 修会：Jesuate（垫佐会）米兰院舍、Lodi 圣彼得修道院院长

## 10. 终审清单

- [ ] 生卒"1598 年"（勿写 1598-01-01）/ 1647-11-30，享年 48–49，出生地 Milan、逝世地 Bologna
- [ ] 国籍用「意大利」，历史政权注明米兰公国
- [ ] "垫佐会（Jesuate）而非耶稣会"表述准确
- [ ] 卡瓦列里原理注明"祖暅早用于球体积"
- [ ] 《Geometria》"1627 写成 / 1635 出版"表述准确
- [ ] Guldin 论战"指控无实据、自辩亦不孚众"两面表述
- [ ] 死因"可能死于痛风"表述准确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Bonaventura_Cavalieri/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：本地无肖像——从 Wikimedia Commons 下载 infobox 肖像/布雷拉雕像，失败则装饰圆占位
- [ ] **国籍**：封面顶部徽章明示意大利
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如伽利略评语 "few, if any, since Archimedes..."）——忠实转述，勿造伪引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（托里拆利 / 梅森）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
