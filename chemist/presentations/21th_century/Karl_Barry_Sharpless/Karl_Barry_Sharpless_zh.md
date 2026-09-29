# Karl Barry Sharpless（卡尔·巴里·夏普莱斯）立传提示词

> qid=Q110925 · 1941-04-28 –（在世）· 美国立体化学家 · 21 世纪 · 诺贝尔化学奖（2001 半奖·氧化；2022 三分之一·点击化学——化学史上第三位同类别两度诺奖者）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Karl_Barry_Sharpless/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框。images.txt 仅一张 `2022_Nobel_awards_ceremony.jpg`（与 Finn、Kolb 在 2022 诺奖典礼的**三人合影**）——**非单人肖像**：封面用装饰圆占位；合影裁中（Sharpless 居中）可作 2022 诺奖页插图（图注必须写全三人）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace\ 两度诺奖的立体化学家\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧装饰圆头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育（Dartmouth BA / Stanford MS+PhD）、博士导师（Eugene van Tamelen）、博士后（Collman / Bloch）、任职（MIT / Stanford / Scripps / 九州大学）、核心领域（立体化学·不对称氧化·点击化学）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「点击 / 咔哒成环」母题——两个圆点相触成键的图形隐喻。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——如 Sharpless 不对称环氧化反应框、叠氮-炔 Huisgen 环加成 → 1,2,3-三唑公式框。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Karl Barry Sharpless（中文惯称：卡尔·巴里·夏普莱斯；infobox 表头即 Karl Barry Sharpless，行文简称 K. Barry Sharpless）
- **生卒**：1941-04-28 生于美国宾夕法尼亚州费城——**在世**（2026 年 3 月起本地页面仍载 "Sharpless in 2026" 照片说明）
- **国籍**：United States（美国）
- **身份**：立体化学家（stereochemist；两度诺贝尔化学奖得主）；Scripps Research 主持实验室；九州大学 Distinguished University Professor
- **家庭**：1965 年娶 Jan Dueser，育有三名子女
- **教育轨迹**：
  - Friends' Central School（1959 毕业）
  - Dartmouth College（A.B. 1963）——本拟读医学院，被科研导师说服转向化学
  - Stanford University（MS；PhD 1968，有机化学）
- **导师**：Eugene van Tamelen（博士导师）
- **博士论文**：1968，《Studies of the Mechanism of Action of 2,3-oxidosqualene-lanosterol cyclase...》（角鲨烯氧化物酶促环化机理）
- **博士后**：Stanford（1968–1969，James P. Collman 组，金属有机化学）；Harvard（1969–1970，Konrad E. Bloch 组，酶学）
- **研究领域**：立体化学——不对称氧化（环氧化/双羟化/氨羟化）、点击化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **费城与曼斯奎恩河（1941）**：生于费城；童年在新泽西 Manasquan 河畔家族小屋度过——钓鱼之爱贯穿一生，大学暑假在渔船上做工。
2. **弃医从化（1963）**：Dartmouth 毕业本要读医学院，被科研教授劝留化学——一生的分岔点。
3. **Stanford 博士（1963–1968）**：师从 Eugene van Tamelen 研究角鲨烯环化酶机理。
4. **两段博士后**：Stanford Collman 组学金属有机 → Harvard Konrad E. Bloch 组学酶学——不对称氧化与「酶般的效率」两条线索在此交汇。
5. **MIT 岁月（1970–1977, 1980–1990）**：两段 MIT 教职之间夹着 Stanford（1977–1980）。
6. **1970 年 NMR 爆炸事故**：到 MIT 不久，NMR 管爆炸致**单眼失明**——此后他反复强调实验室必须全程佩戴护目镜（引语见 §5）。
7. **Sharpless 不对称环氧化（Stanford 期间发现）**：烯丙醇的不对称环氧化反应，曾用于合成 (+)-disparlure——把不对称合成「从科幻变成常规操作」的代表反应之一。
8. **氧化反应家族**：aminohydroxylation（氨羟化）、dihydroxylation（双羟化）、Sharpless asymmetric epoxidation——立体选择性氧化的完整工具箱。
9. **乙酰胆碱酯酶抑制剂**：证明以叠氮与炔为起点、经酶催化可生成飞摩尔级（femtomolar）效力的抑制剂——点击化学思想的前奏。
10. **2001 诺贝尔化学奖（半奖）**：官方理由 "for his work on chirally catalysed oxidation reactions"；另一半由 Knowles 与 Noyori 共享（氢化）。
11. **点击化学（click chemistry，约 2000 年命名）**：2001 年与 Hartmuth Kolb、M.G. Finn 在 Scripps 首次完整阐述——高选择性、放热、温和条件；最成功实例是叠氮-炔 Huisgen 环加成生成 1,2,3-三唑。
12. **2022 再度诺奖（三分之一）**：与 Carolyn R. Bertozzi、Morten P. Meldal 共享，理由 "for the development of click chemistry and bioorthogonal chemistry"——史上第五位两度诺奖者（另两位组织之外：Curie、Bardeen、Pauling、Sanger），**同类别两度的第三人**（继 Bardeen、Sanger 之后）。
13. **学术生命力**：截至 2024 年 Scopus h-index 130；2019 年 Priestley Medal（ACS 最高荣誉）；2023 年美国化学家学会金奖；在 Scripps 实验室持续运转至今。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海蓝 deepsea） | `#0E4D64` | 立体化学的冷峻精确（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（不对称氧化 badgeOxid） | `#2E5A9E` | 蓝环氧化 / 双羟化 / 氨羟化 |
| 分类色 2（点击化学 badgeClick） | `#1B7A43` | 绿叠氮-炔 / 1,2,3-三唑 |
| 分类色 3（诺贝尔 badgeNobel） | `#D97B29` | 琥珀 2001 + 2022 两度获奖 |
| 分类色 4（传承 badgeMentor） | `#C0395B` | 玫瑰 Finn / Kolb / Jacobsen 弟子群 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），其中两圆相切象征「点击」成键。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions（`music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`；**不要复制 wav 文件，Makefile 直接引用该路径**）
- **风格**：回望 / 深沉 / 时间纵深
- **匹配理由**：
  - "PAST" 匹配两度诺奖的**时间纵深**——2001 与 2022 间隔 21 年，一部跨越世纪的学术人生
  - "回望" 匹配其叙事结构——从费城童年钓鱼到 Scripps 实验室，一生的反应工具箱层层叠加
  - "深沉" 匹配立体化学气质——不动声色地改写了合成化学的默认操作
- **时长核对**：以实际曲目时长为准，> 15 页 × 7 秒即可由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 两度诺奖的立体化学家 / Karl Barry Sharpless 1941– + 四色 badge + 右上装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/博士后/机构/领域/荣誉）
03  Sharpless 的一生 — 时间线（10 节点：1941→1959 FCS→1963 Dartmouth→1968 Stanford PhD→1970 MIT→1977 Stanford→环氧化→2001 诺奖→2000s 点击化学→2022 诺奖）
04  早年：费城与渔船 (1941–1959) — 表格「时间|事件|结果」
05  求学：弃医从化 (1959–1968) — 表格「时间|事件|结果」（Dartmouth→Stanford van Tamelen）
06  博士后与 MIT (1968–1977) — 表格「阶段|师从|收获」（Collman/Bloch/MIT+1970 事故）
07  Sharpless 不对称环氧化 — 表格「问题|方法|结果」+ 公式框：不对称环氧化 → (+)-disparlure
08  氧化反应家族 — 表格「反应|特点|意义」（环氧化/双羟化/氨羟化）
09  2001 诺贝尔化学奖 — 表格「得主|份额|理由」+ 公式框：官方英文获奖理由
10  点击化学 (2000–2001) — 表格「概念|方法|实例」+ 公式框：叠氮-炔 Huisgen 环加成 → 1,2,3-三唑
11  2022 再度诺奖 — 表格「得主|份额|理由」+ 三人合影插图（Finn/Sharpless/Kolb 图注齐全）
12  事故与安全引语页 — 表格「事件|后果|影响」+ 安全眼镜引语（页面原文）
13  荣誉与弟子 — 「类别|代表|意义」表格 + itemize（Priestley/Wolf/Harvey/King Faisal…）+ 弟子 Finn/Fu/Jacobsen/Kolb
14  结尾 — 「从科幻到常规：他两次改写了合成化学的默认操作。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 两次诺奖份额 | 2001 是**半奖**（另一半 Knowles+Noyori 共享）；2022 是**三分之一**（与 Bertozzi、Meldal）——勿写成两次都独享或两次半奖 |
| 两度诺奖定位 | 页面口径：史上第五位两度诺奖者（外加两个组织），继 **Bardeen、Sanger 之后同类别（化学）两度的第三人**——表述勿拔高为「第一人」 |
| 2001 获奖理由 | 官方英文 "for his work on chirally catalysed oxidation reactions"（氧化）——勿并入氢化；Knowles/Noyori 的另一半才是氢化 |
| 2022 获奖理由 | 官方英文 "for the development of click chemistry and bioorthogonal chemistry"——click chemistry 概念为 Sharpless 提出，bioorthogonal chemistry 主要归 Bertozzi 方向，理由是共享的整体表述 |
| 点击化学命名 | "click chemistry" 一词由 Sharpless **约 2000 年**创造，2001 年与 **Kolb、Finn** 在 Scripps 首次完整阐述——三人勿漏 |
| MALDI 无关 | 本篇不涉及 MALDI（那是 2002 Fenn/Tanaka 篇的争议）——勿串场 |
| Wolf Prize 2001 | 与 **Henri B. Kagan、Ryōji Noyori** 三人共享（页面明载）——Kagan 是页面明载的共同得主，可入库 |
| 1970 事故 | NMR 管爆炸致**单眼失明**（blinded in one eye）——勿写成双目失明；引语 "there's simply never an adequate excuse for not wearing safety glasses in the laboratory at all times."（at all times 为斜体强调）须逐字 |
| 弟子分层 | infobox 明确分层：博士 students=M.G. Finn；undergrads=Gregory Fu；post-docs=Eric Jacobsen、Hartmuth Kolb——入库 note 须写明层级，勿一律写成博士生 |
| 合影图注 | 2022 诺奖典礼合影三人 Finn（左）/Sharpless（中）/Kolb（右）——图注三人齐全，勿只写本人 |
| 生卒 | 1941-04-28 生，**在世**——封面与身份页留白不写卒年（与两度诺奖叙事中 Sanger 等已故者区分） |
| 入库名规范 | 本人入库名 Karl Barry Sharpless；共同得主对手方名用 **Carolyn Bertozzi / Morten P. Meldal**（2022 组另批处理，须精确一致）；Knowles 用 William Standish Knowles；Noyori 用 Ryōji Noyori |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q110925 | ✅ |
| name_zh | 卡尔·巴里·夏普莱斯 | ✅ |
| name_en | Karl Barry Sharpless | ✅（新建记录） |
| birth_date | 1941-04-28 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分见下表） | ✅ |

**person_field 细分 rank 表**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | stereochemistry | 立体化学 |
| 1 | asymmetric oxidation | 不对称氧化 |
| 2 | click chemistry | 点击化学 |
| 3 | bioorthogonal chemistry | 生物正交化学 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Eugene van Tamelen | 师→生（博士导师） | Stanford 博士导师（1968，角鲨烯环化机理） |
| advisor-student | James P. Collman | 师→生（博士后导师） | Stanford 博士后（1968–69），金属有机化学 |
| advisor-student | Konrad E. Bloch | 师→生（博士后导师） | Harvard 博士后（1969–70），酶学（Bloch 为 1964 诺贝尔生理学或医学奖得主——如写须注明，页面仅载其名） |
| advisor-student | M.G. Finn | 师→生（博士生） | infobox Doctoral students；点击化学共同阐述者 |
| advisor-student | Gregory Fu | 师→生（本科生） | infobox Other notable students 之 Undergrads |
| advisor-student | Eric Jacobsen | 师→生（博士后） | infobox Other notable students 之 Post-docs |
| advisor-student | Hartmuth Kolb | 师→生（博士后） | infobox Post-docs；2001 点击化学共同阐述者 |
| spouse | Jan Dueser | 无向 | 1965 年结婚，育有三名子女 |
| co-honored | William Standish Knowles | 无向 | 2001 诺贝尔化学奖（Knowles 与 Noyori 共享另一半·氢化） |
| co-honored | Ryōji Noyori | 无向 | 2001 诺贝尔化学奖 + 2001 Wolf Prize 共同得主 |
| co-honored | Henri B. Kagan | 无向 | 2001 Wolf Prize 共同得主（页面明载三人共享） |
| co-honored | Carolyn Bertozzi | 无向 | 2022 诺贝尔化学奖共同得主（点击化学/生物正交化学） |
| co-honored | Morten P. Meldal | 无向 | 2022 诺贝尔化学奖共同得主（点击化学/生物正交化学） |

> **禁入库名单**：van Tamelen 之外的求学阶段老师（Dartmouth 劝其留化学的 research professor 未具名——禁写）；Huisgen（反应以人名命名，非个人关系）；Marie Curie / Bardeen / Pauling / Sanger（仅两度诺奖并列提及，非个人关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2001 半奖·不对称氧化；2022 三分之一·点击化学与生物正交化学）
- Chemical Pioneer Award（1988）
- Scheele Award（1991）
- Arthur C. Cope Award（1992）
- Tetrahedron Prize（1993）
- King Faisal International Prize（1995）
- Harvey Prize（1998）
- Chirality Medal（2000）
- Benjamin Franklin Medal（2001，Franklin Institute）
- Wolf Prize in Chemistry（2001，与 Henri B. Kagan、Ryōji Noyori 共享）
- William H. Nichols Medal（2006）
- Priestley Medal（2019，ACS 最高荣誉——理由含催化不对称氧化方法、点击化学概念与铜催化叠氮-炔环加成的发展）
- American Institute of Chemists Gold Medal（2023）
- 荣誉学位：KTH Royal Institute of Technology（1995）、Technical University of Munich（1995）、Catholic University of Louvain（1996）、Wesleyan University（1999）

## 9. 机构清单

- 教育：Friends' Central School（1959）→ Dartmouth College（A.B. 1963）→ Stanford University（MS；PhD 1968）
- 博士后：Stanford（Collman，1968–69）→ Harvard（Bloch，1969–70）
- 任职：MIT 教授（1970–1977；1980–1990）→ Stanford 教授（1977–1980）→ Scripps Research（2023 年仍在主持实验室）→ 九州大学 Distinguished University Professor

## 10. 终审清单

- [ ] 2001 半奖 / 2022 三分之一 份额准确；两条官方英文获奖理由逐字
- [ ] 「第五位两度诺奖者、同类别第三位（继 Bardeen、Sanger）」表述准确
- [ ] 点击化学命名 ~2000 + 2001 三人（Sharpless/Kolb/Finn）完整阐述
- [ ] 1970 NMR 事故单眼失明 + 安全眼镜引语逐字（at all times 斜体）
- [ ] 弟子分层（Finn 博士生 / Fu 本科生 / Jacobsen+Kolb 博士后）准确
- [ ] 在世——全篇无卒年
- [ ] 入库对手方名：Carolyn Bertozzi / Morten P. Meldal / William Standish Knowles / Ryōji Noyori / Henri B. Kagan（规范全名，与 2022 批次精确一致）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Karl_Barry_Sharpless/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：装饰圆占位；2022 合影仅作插图且图注三人齐全
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：安全眼镜引语逐字对照 page.md
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2001 批次（Knowles / Noyori 篇）及 2022 批次（Bertozzi / Meldal 篇）的获奖格局表述交叉一致

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
