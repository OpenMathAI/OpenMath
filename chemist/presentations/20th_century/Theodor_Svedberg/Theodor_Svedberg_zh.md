# Theodor Svedberg（西奥多·斯韦德贝里）立传提示词

> qid=Q186391 · 1884-08-30 – 1971-02-25 · 瑞典化学家 · 20 世纪 · 诺贝尔化学奖（1926，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Theodor_Svedberg/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。★ 本人物 images.txt **为空、无任何图片**（infobox 图注 "Svedberg in 1926" 但本地无图）——封面与身份页用**装饰圆占位**（主色实心圆 + 缩写 TS）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{cog}\enspace 为蛋白质称重的人\enspace·\enspace 瑞典`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：左侧装饰圆 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育（BA/MS/PhD 年份）、博士学生、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡呼应「离心沉降」母题——圆点在旋转场中分层排布。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：tabularx 三列表格 + 金色边框浅金底公式展示框，如「1 svedberg (S) = 10⁻¹³ s = 100 fs」。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Theodor Svedberg（中文惯称：西奥多·斯韦德贝里）
- **生卒**：1884-08-30 生于 Valbo, Sweden → 1971-02-25 逝于 Kopparberg, Sweden，享年 86
- **国籍**：Sweden（瑞典）
- **身份**：化学家（biochemistry / 胶体化学 / 物理化学；infobox occupation 另载 artist）
- **家庭**：父 Elias Svedberg、母 Augusta Alstermark；**结婚四次、共十二个子女**；遗孀 2019 年去世；信义宗（Lutheran）
- **教育轨迹**：grammar school 期间即独立做实验室研究与科学演示；Uppsala University 化学专业——**1905 BA、1907 硕士、1908 博士**
- **博士导师**：Oskar Widman、Carl Benedicks（★ 仅 frontmatter 有载，正文与 infobox 无载——提示词可提，**禁入库**，见 §7）
- **研究领域**：biochemistry——胶体化学（colloids）、分析超离心（analytical ultracentrifugation）、蛋白质
- **机构**：Uppsala University（1900s 中–1949）、Gustaf Werner Institute（1949–1967 主持）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **Valbo 少年（1884）**：生于 Valbo，从小痴迷植物学与各科自然科学；中学就做独立实验研究与科学演示。
2. **Uppsala 快车道（1905–1908）**：1905 BA → 1907 硕士 → 1908 博士，三年三级跳；1905 年即任大学助理化学师。
3. **28 岁的物理化学主任（1907/1912）**：1907 任 docent，1912 出任 Uppsala 物理化学主任。
4. **为布朗运动作证**：胶体实验支持爱因斯坦与斯莫卢霍夫斯基（Marian Smoluchowski）提出的布朗运动理论。
5. **分析超离心技术**：发明并发展 analytical ultracentrifugation——用离心沉降为分子"称重"。
6. **区分纯蛋白质**：用超离心证明不同纯蛋白质可被一一区分——蛋白质化学的定量转折。
7. **客座美国（1920s 初）**：曾短期在 University of Wisconsin 任教。
8. **1926 诺贝尔化学奖**：表彰其胶体与蛋白质研究及超离心方法；诺奖演讲 1927-05-19《The Ultracentrifuge》。
9. **三次 Björkénska priset（1913/1923/1926）**：Uppsala 大学科学奖三度加冕。
10. **以他命名的单位**：沉降系数单位 **svedberg（S）= 10⁻¹³ s = 100 fs**——核糖体 30S/50S 等命名皆源于此；Uppsala 的 The Svedberg Laboratory 亦以其命名。
11. **国际荣誉**：ForMemRS（1944，候选词："distinguished for his work in physical and colloid chemistry and the development of the ultracentrifuge"）、美国国家科学院（1945）、American Philosophical Society（1941 International Member；页面另载 1948 elected）、Franklin Medal（1949，表彰超离心工作）。
12. **Gustaf Werner Institute（1949–1967）**：离开 Uppsala 后主持该所至 1967——科研生命延续 60 余年。
13. **四婚十二子与长寿（1971）**：结婚四次、子女十二人；1971-02-25 逝于 Kopparberg，享年 86。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青碧 deep teal） | `#0B5351` | 北欧极光下的实验精确与沉静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（超离心 badgeCentri） | `#175873` | 深蓝超离心机 / 沉降系数 |
| 分类色 2（胶体 badgeColloid） | `#1B7A43` | 绿胶体化学 / 布朗运动 |
| 分类色 3（蛋白质 badgeProtein） | `#D97B29` | 琥珀蛋白质区分 |
| 分类色 4（荣誉传承 badgeHonor） | `#C0395B` | 玫瑰 S 单位 / 研究所命名 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆 + 同心圆环细线），呼应「离心沉降的分层」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`；不要复制 wav 文件，Makefile 引用路径即可）
- **风格**：恒久 / 大气 / 纪录片
- **匹配理由**：
  - "恒久" 匹配其科学遗产——svedberg 单位进入每一本分子生物学教材，60 余年科学生命横跨 Uppsala 与 Gustaf Werner Institute
  - "大气" 匹配超离心的尺度感——从胶体颗粒到蛋白质分子，物理化学的宏图
  - "纪录片" 匹配传记叙事——Valbo → Uppsala 三级跳 → 布朗运动 → 超离心 → 1926 诺奖 → S 单位永存
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 为蛋白质称重的人 / Theodor Svedberg 1884–1971 + 四色 badge + 右上装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/国籍/教育 BA·MS·PhD/博士学生/出生地/去世地/领域/荣誉）
03  斯韦德贝里的一生 — Sanger 式时间线（10 节点：1884→1905→1907→1908→1912→1920s→1926→1944→1949→1971）
04  Valbo 少年 (1884–1900s) — 表格「时间|事件|结果」
05  Uppsala 三级跳 (1905–1912) — 表格「年份|学位/职务|结果」+ 公式框：1905 BA → 1907 MS → 1908 PhD
06  胶体与布朗运动 — 表格「理论|实验|结果」（Einstein/Smoluchowski 理论被胶体实验支持）+ 公式框：布朗运动
07  分析超离心技术 — 表格「问题|方法|结果」
08  为蛋白质称重 — 表格「问题|方法|结果」+ 公式框：1 S = 10⁻¹³ s = 100 fs
09  1926 诺贝尔化学奖 — 公式框：诺奖演讲 The Ultracentrifuge (1927-05-19)
10  荣誉清单 — 「类别|代表|意义」表格（ForMemRS 1944 / NAS 1945 / Franklin Medal 1949 / Björkénska ×3）
11  Gustaf Werner Institute (1949–1967) — 高斯 FFT 页式流程图
12  家庭与晚年 — 表格（四婚十二子 / 1971 逝于 Kopparberg / 遗孀 2019）
13  遗产：S 单位永存 — 四分类遗产盒 + 公式框：30S/50S 命名源流
14  结尾 — 「离心之力，称出生命分子的重量。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 学位年份 | **1905 BA、1907 硕士、1908 博士**——勿倒置或合并 |
| 导师口径 | Oskar Widman、Carl Benedicks 仅 frontmatter 有载，正文与 infobox 无载——提示词 §1 可提但**禁入库**、Beamer 正文建议淡化 |
| 奖年口径 | 1926 年当年授奖（与 Zsigmondy 1925 奖 1926 授不同——同批对照页注意区分） |
| 获奖理由口径 | page.md 原文 "for his research on colloids and proteins using the ultracentrifuge"——勿泛化成"发明离心机" |
| svedberg 单位 | **10⁻¹³ s = 100 fs**（沉降系数单位，符号 S）——勿与其姓名混淆 |
| APS 双记录 | 页面并存 "1941 International Member" 与 "1948 elected"——如实注记，勿删改 |
| Björkénska | 三次：**1913、1923、1926**——勿写两次 |
| 家庭 | **结婚四次、十二个子女**；遗孀 2019 年去世——勿写"一妻"；子女姓名页面无载禁写 |
| Tiselius | infobox Doctoral students 仅 Arne Tiselius 一人——note 只写"学生"，**勿加 1948 诺奖**（页面无载禁写） |
| Einstein/Smoluchowski | 胶体实验"支持"其布朗运动理论——是思想影响关系，勿写"师承"或"合作" |
| Wisconsin | 1920s 初临时任教——勿编造具体年限 |
| 肖像 | images.txt 为空——装饰圆占位，禁编造"1926 年照片"图注 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q186391 | ✅（复用库内记录 id=2147 回填） |
| name_zh | 西奥多·斯韦德贝里 | ✅ |
| name_en | Theodor Svedberg | ✅（沿用库内精确形式） |
| birth_date | 1884-08-30 | ✅ |
| death_date | 1971-02-25 | ✅ |
| nationality | Sweden | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表） | ✅ |
| has_biography | 0（待立传后置 1） | ✅ |

**person_field 细分（rank 表）**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | colloid chemistry | 胶体化学 |
| 1 | analytical ultracentrifugation | 分析超离心技术 |
| 2 | protein chemistry | 蛋白质化学 |
| 3 | physical chemistry | 物理化学 |

## 7. 社会关系入库清单

**★ 红线**：只收 page.md 正文或 infobox 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Arne Tiselius | 师→生 | infobox Doctoral students 明载（页面未载其获奖，note 勿加诺奖） |
| influence | Albert Einstein | 影响者 | 布朗运动理论，其胶体实验予以支持（沿用库内规范名） |
| influence | Marian Smoluchowski | 影响者 | 布朗运动理论，其胶体实验予以支持 |

**禁入库名单（仅 frontmatter 有载，正文与 infobox 无载）**：

> 博士导师 Oskar Widman、Carl Benedicks（frontmatter `doctoral_advisor` 有载但正文/infobox 无载，按红线禁入库）；父母 Elias Svedberg、Augusta Alstermark（仅一句列举）；四任妻子与十二名子女（页面未载姓名）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1926，独享；诺奖演讲 1927-05-19 The Ultracentrifuge）
- Björkénska priset（1913、1923、1926，Uppsala 大学）
- Foreign Member of the Royal Society，ForMemRS（1944）
- Member of the National Academy of Sciences（1945）
- International Member of the American Philosophical Society（1941；页面另载 1948 elected）
- Franklin Medal（1949，表彰超离心工作）
- doctor honoris causa from the University of Paris（frontmatter 载名）

## 9. 机构清单

- 教育：Uppsala University（BA 1905 / MS 1907 / PhD 1908）
- 任职：Uppsala University（1905 助理化学师 → 1907 docent → 1912 物理化学主任 → 1949 离任）、University of Wisconsin（1920s 初临时任教）、Gustaf Werner Institute（1949–1967 主持）
- 命名：svedberg（S）沉降系数单位；The Svedberg Laboratory（Uppsala）

## 10. 终审清单

- [ ] 生卒 1884-08-30 / 1971-02-25，享年 86，出生地 Valbo、去世地 Kopparberg
- [ ] 学位年份 1905/1907/1908 顺序无误；1926 当年授奖
- [ ] S 单位 = 10⁻¹³ s = 100 fs；30S/50S 命名源流表述准确
- [ ] Tiselius 学生关系有 infobox 出处；note 无编造获奖信息
- [ ] Einstein/Smoluchowski 用 influence 类型；无"师承/合作"表述
- [ ] 四婚十二子表述准确；无编造姓名
- [ ] 全篇无编造引语（Royal Society 候选词引语为 page.md 明载唯一可直接引用句）；引号内不出现 page.md 无法溯源的"原话"
- [ ] 封面/身份页装饰圆占位；封面国籍行明示瑞典
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Theodor_Svedberg/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **肖像**：确认为装饰圆占位（本地无图）
- [ ] **国籍**：封面顶部明示瑞典
- [ ] **引语核对**：仅 Royal Society 候选词一句可直接引用，其余一律间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger / van 't Hoff 等）对齐
