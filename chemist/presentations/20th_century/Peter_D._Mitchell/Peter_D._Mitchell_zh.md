# Peter D. Mitchell（彼得·米切尔）立传提示词

> qid=Q207992 · 1920-09-29 – 1992-04-10 · 英国生物化学家 · 20 世纪 · 诺贝尔化学奖（1978，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Peter_D._Mitchell/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框 + 气泡背景。
> ⚠️ **本篇数据源较短**（page.md 仅 77 行）：一切以实载为准，严禁脑补；无载处用"页面无载"标注，宁缺毋滥。

---

## 0. 正文形式说明（参考 Sanger 桑格模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像下载后放 `images/`；Commons 404 则按 Wikipedia REST API 回退，再失败用装饰圆占位并在 Review 记录）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{battery-three-quarters}\enspace 化学渗透假说的孤独先知\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰（本篇 frontmatter **无 doctoral_advisor 字段**，信息页不留"师承"栏）。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「跨膜质子梯度」母题——圆点从密到疏排布暗示膜两侧的电化学梯度。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Peter Dennis Mitchell（中文惯称：彼得·丹尼斯·米切尔；FRS 1974）
- **生卒**：1920-09-29 生于英格兰萨里郡 Mitcham → 1992-04-10 逝于英格兰康沃尔郡 Bodmin，享年 71
- **国籍**：United Kingdom（英国）
- **身份**：英国生物化学家；以 ATP 合成的化学渗透（chemiosmotic）机制理论获 1978 诺贝尔化学奖
- **家庭**：父 Christopher Gibbs Mitchell 为公务员；母 Kate Beatrice Dorothy（娘家姓 Taplin）；叔父 Sir Godfrey Mitchell 为建筑公司 George Wimpey 主席（page.md 明载，仅背景一句，不入关系库）
- **教育轨迹**：
  - Queen's College, Taunton
  - Jesus College, Cambridge：自然科学荣誉学位课程（Natural Sciences Tripos），专修生物化学
  - 1942 获剑桥生物化学系研究职位；1951 年初以青霉素作用方式研究获 PhD（论文题目 *The rates of synthesis and proportions by weight of the nucleic acid components of a Micrococcus during growth in normal and in penicillin containing media with reference to the bactericidal action of penicillin*）
- **导师**：页面无载（frontmatter 无 doctoral_advisor）——信息页留空，勿编造
- **研究领域**：生物化学——生物能量转换、化学渗透反应与反应系统、膜生物化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **萨里公务员之子（1920）**：生于 Mitcham；叔父是建筑业大亨——他却走向了与商业最远的纯科学研究。
2. **剑桥与青霉素（1942–1951）**：1942 入剑桥生物化学系任研究职位；1951 年初以青霉素杀菌作用方式（微生物核酸组分的合成速率与比例）获 PhD——与 Cornforth 一样，青霉素是他学术生涯的起点。
3. **爱丁堡创业（1955）**：应 Michael Swann 教授之邀，在爱丁堡大学动物学系组建"化学生物学单元"（Chemical Biology Unit）。
4. **升迁与出走（1961–1963）**：1961 高级讲师、1962 Reader——但**机构对其工作的反对加上健康恶化**，1963 年辞职。这是他人生的分水岭。
5. **Glynn House 的豪赌（1963–1965）**：监督修复康沃尔 Bodmin 附近 Cardinham 的一座摄政时期正立面宅邸 Glynn House，把主要部分改造成研究实验室。
6. **Glynn Research Ltd（1965）**：与前研究同事 Jennifer Moyle 共同创立慈善公司 Glynn Research Ltd 推动基础生物学研究，开启化学渗透反应系统研究纲领——**私立实验室里的诺奖之路**。
7. **时代之问（1960s）**：ATP 已知是生命的能量通货，但线粒体内 ATP 的合成机制被默认为底物水平磷酸化——氧化磷酸化的生化机制无人知晓。
8. **化学渗透假说**：Mitchell 意识到离子跨越**电化学势差**的移动可提供合成 ATP 所需的能量——活细胞有膜电位（内负于外），离子的跨膜移动同时受电场力（正负相吸）与热力学力（从高浓度向低浓度扩散）支配；他进而证明 ATP 合成与这一电化学梯度相耦合。
9. **假说的胜利**：ATP 合酶（膜结合蛋白，利用电化学梯度势能合成 ATP）的发现验证了其假说；Jagendorf 发现叶绿体类囊体膜两侧 pH 差可驱动 ATP 合成，再添铁证。
10. **质子 motive Q 循环**：Mitchell 后来还假想电子传递链的若干复杂细节——把质子泵送与醌基电子分岔（electron bifurcation）耦合，贡献于质子动力势从而 ATP 合成。
11. **1978 诺贝尔化学奖（独享）**："for his contribution to the understanding of biological energy transfer through the formulation of the chemiosmotic theory"——以化学渗透理论阐明生物能量传递。
12. **荣誉轨迹**：FRS 1974；Rosenstiel Award 1976；Sir Hans Krebs Medal 1978；Copley Medal 1981；另有 Feldberg Foundation Prize 与 Croonian Medal and Lecture（frontmatter 明载）。
13. **孤独的范式**：从爱丁堡的不被容到康沃尔私宅实验室——化学渗透假说从"异端"到教科书标准的历程，是 20 世纪科学史上"边缘先行"的典范（叙事限于 page.md 明载事实，勿加戏剧化脑补）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（紫藤深紫 deeppurple） | `#372A75` | 线粒体内膜的幽深与电化学梯度的神秘（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（化学渗透 badgeChemiosm） | `#2E6E8E` | 青蓝质子梯度 / 膜电位 |
| 分类色 2（ATP 合酶 badgeATP） | `#1B7A43` | 绿 ATP 合酶验证 / 氧化磷酸化 |
| 分类色 3（Glynn 岁月 badgeGlynn） | `#D97B29` | 琥珀康沃尔私宅实验室 / Glynn Research |
| 分类色 4（Q 循环 badgeQ） | `#C0395B` | 玫瑰质子 motive Q 循环 / 电子分岔 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），圆点由密到疏排布呼应「跨膜质子梯度」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`；不要复制 wav 文件，Makefile 引用即可）
- **风格**：沉稳 / 纪录片 / 孤独的长期主义
- **匹配理由**：
  - "沉稳" 匹配其气质——机构反对与健康恶化后退守康沃尔私宅，十年守一假说
  - "纪录片" 匹配传记叙事——剑桥 → 爱丁堡 → Glynn House → 1978 诺奖 → Copley
  - "长期主义" 匹配化学渗透假说从异端到教科书标准的漫长等待
- **时长**：以实际曲目时长为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 化学渗透假说的孤独先知 / Peter D. Mitchell 1920–1992 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/出生地/去世地/领域/荣誉；无师承栏）
03  米切尔的一生 — 高斯式时间线（10 节点：1920→1942→1951→1955→1961→1963→1965→1974→1978→1992）
04  早年与剑桥 (1920–1951) — 表格「时间|事件|结果」（Jesus College / 青霉素 PhD）
05  爱丁堡：Chemical Biology Unit (1955–1963) — 表格「时间|事件|结果」+ 机构反对与健康恶化→辞职
06  Glynn House 豪赌 (1963–1965) — 表格「行动|伙伴|结果」（宅邸改造 / Jennifer Moyle / Glynn Research Ltd）
07  时代之问：ATP 从何而来 (1960s) — 表格「共识|疑点|转折」+ 公式框：底物水平磷酸化 vs 氧化磷酸化
08  化学渗透假说 (1961–) — 表格「问题|方法|结果」+ 公式框：离子跨电化学势差移动 → ATP 合成耦合
09  假说的胜利 — 表格「证据|发现者|意义」（ATP 合酶 / Jagendorf 类囊体 pH 差实验）
10  质子 motive Q 循环 — 表格「问题|机制|结果」+ 公式框：质子泵送 × 醌基电子分岔
11  1978 诺贝尔化学奖 — 表格「人物|方向|结果」（独享 · "biological energy transfer through the formulation of the chemiosmotic theory"）
12  荣誉与晚期 — 高斯式「类别|代表|意义」表格（FRS 1974 / Rosenstiel 1976 / Krebs Medal 1978 / Copley 1981）
13  遗产：生命的能量通货 — 四分类遗产盒 + 公式框：chemiosmosis 进入教科书 · H+ 梯度驱动 ATP 与其他生化过程
14  结尾 — 「能量跨过一层膜，生命得以呼吸。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1978 获奖理由 | 官方原文 "for his contribution to the understanding of biological energy transfer through the formulation of the chemiosmotic theory"——勿泛化成"发现 ATP"或"发明 ATP 合酶" |
| 独享 | 1978 **独享**——勿与他人共享 |
| 师承 | page.md **无载**博士导师——信息页留空、正文禁写任何导师；勿从库内 metadata 脑补 |
| ATP 合酶 | **ATP 合酶的发现验证了假说**——发现者 page.md 未具名，勿编造归属；Jagendorf 的是类囊体 pH 差实验 |
| Jagendorf 关系 | André Jagendorf 仅因实验验证假说被提及——**非个人关系不入库** |
| 辞职原因 | 机构对其工作的反对 **coupled with ill health**（1963）——两层原因都要写 |
| Glynn Research | 与 **Jennifer Moyle** 共同创立的**慈善公司**——勿写成大学或政府机构 |
| Q 循环 | "质子泵送与醌基电子分岔耦合"——写 hypothesized/conceived 层面即可，勿写"实验证明" |
| 叔父 | Sir Godfrey Mitchell（George Wimpey 主席）仅背景一句——**不入关系库**（白名单无类型） |
| 早年去向 | page.md 无童年细节——勿编造；Slide 4 严格控制在校教育与博士两事实 |
| 引语红线 | page.md **全文无一句可引原话**（诺奖理由为官方叙述非其原话）——全篇禁用引号"原话"，一律间接转述 |
| metadata 噪声 | frontmatter 奖项含 Portland Press Excellence in Science Award、Feldberg Foundation Prize 等，正文未给年份——展示以正文 infobox 四奖（Rosenstiel 1976 / Nobel 1978 / Krebs Medal 1978 / Copley 1981）为主 |
| 页面较短 | 本篇 page.md 仅 77 行——任何"此外他还……"的扩展叙述都必须能在 page.md 溯源，否则删句 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q207992 | ✅ |
| name_zh | 彼得·米切尔 | ✅ |
| name_en | Peter D. Mitchell | ✅ |
| birth_date | 1920-09-29 | ✅ |
| death_date | 1992-04-10 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表，带 rank） | ✅ |

**person_field rank 表**：

| field | rank | 语义 |
|---|---|---|
| biochemistry | 0 | 学科大类（frontmatter field_of_work） |
| bioenergetics | 1 | 生物能量转换（诺奖方向） |
| molecular biology | 2 | frontmatter 明载 |
| membrane biochemistry | 3 | 跨膜电化学梯度 / 化学渗透（frontmatter 未单列，并入 bioenergetics 叙事） |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。本篇 page.md 较短，关系仅 2 条为诚实值。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Jennifer Moyle | 无向 | 前研究同事；1965 共同创立 Glynn Research Ltd |
| colleague | Michael Swann | 无向 | 1955 邀其赴爱丁堡大学动物学系组建 Chemical Biology Unit |

> **禁入库名单（非个人关系或白名单外类型）**：André Jagendorf（实验验证假说非个人关系）；Godfrey Mitchell（叔父，白名单无类型）；Christopher Gibbs Mitchell / Kate Taplin（父母，无正面叙事需要且 parent-child 方向仅限亲子关系叙事，本篇不涉）。

## 8. 奖项清单

- Fellow of the Royal Society，FRS（1974）
- Rosenstiel Award（1976）
- Nobel Prize in Chemistry（1978，独享）
- Sir Hans Krebs Medal（1978）
- Copley Medal（1981）
- Feldberg Foundation Prize；Croonian Medal and Lecture（frontmatter 明载，正文未给年份——展示慎写）

## 9. 机构清单

- 教育：Queen's College, Taunton；Jesus College, Cambridge（自然科学荣誉学位课程，专修生物化学；BA/MA/PhD per infobox Education 行）
- 任职：University of Cambridge 生物化学系（1942 研究职位）；University of Edinburgh 动物学系 Chemical Biology Unit（1955 创建；1961 Senior Lecturer；1962 Reader；1963 辞职）；Glynn Research Ltd（Glynn House, Cardinham near Bodmin, Cornwall；1963–1965 修复宅邸，1965 与 Moyle 共同创立）
- 去世：1992-04-10 逝于 Bodmin, Cornwall

## 10. 终审清单

- [ ] 生卒 1920-09-29 / 1992-04-10，享年 71，出生地 Mitcham (Surrey)、去世地 Bodmin (Cornwall)
- [ ] 1978 **独享**；获奖理由"化学渗透理论阐明生物能量传递"口径准确
- [ ] 博士导师页面无载——全篇无师承叙述
- [ ] 爱丁堡辞职双因（机构反对 + 健康恶化）；Glynn Research Ltd 与 Moyle 共创表述准确
- [ ] ATP 合酶发现者不具名、Jagendorf 实验表述准确
- [ ] 全篇无引号"原话"（page.md 无可引原话）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Peter_D._Mitchell/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认肖像就位（Commons/Wikipedia REST API；失败则装饰圆占位并记录）
- [ ] **国籍**：封面顶部明示"英国"
- [ ] **引语核对**：全篇禁引号"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改动该文件。
