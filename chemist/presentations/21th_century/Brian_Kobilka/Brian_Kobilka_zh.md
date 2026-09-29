# Brian Kobilka（布莱恩·科比尔卡）立传提示词

> qid=Q80907 · 1955-05-30 生于明尼苏达州 Little Falls · 在世 · 美国生理学家 · 诺贝尔化学奖（2012，与 Robert Lefkowitz 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Brian_Kobilka/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从本地 `images.txt` 列表下载，如 2012 斯德哥尔摩 / 2024 斯坦福照；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{project-diagram}\enspace 看见受体的结晶师\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、博士后、研究领域、任职、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「晶体生长」母题——小圆逐渐聚合成规则晶簇，暗合蛋白结晶的漫长等待。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），β2AR–Gs 复合物或受体-配体公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Brian Kent Kobilka（中文惯称：布莱恩·科比尔卡）
- **生卒**：1955-05-30 生于明尼苏达州 Little Falls → 在世（卒日留白）
- **国籍**：United States（美国）
- **身份**：生理学家——斯坦福大学医学院分子与细胞生理学系教授；ConfometRx（专注 GPCR 的生物技术公司）共同创办人；2011 年当选美国国家科学院院士
- **家庭**：Little Falls 面包师世家——祖父 Felix J. Kobilka（1893–1991）与父亲 Franklyn A. Kobilka（1921–2004）均为镇上面包师；祖母 Isabelle Susan Kobilka（娘家姓 Medved，1891–1980）出自普鲁士移民的 Medved 与 Kiewel 家族（1888 年起经营镇上历史悠久的 Kiewel 啤酒厂）；母亲 Betty L. Kobilka（娘家姓 Faust，1930 年生）；在明尼苏达大学德卢斯分校结识马来华裔妻子 Tong Sun Thian；子女 Jason 与 Megan
- **教育轨迹**：
  - Little Falls 的 St. Mary's Grade School（圣克劳德教区）→ Little Falls High School
  - University of Minnesota Duluth：生物学与化学学士（BS）
  - Yale University School of Medicine：M.D.，*cum laude*
  - 圣路易斯华盛顿大学医学院 Barnes-Jewish Hospital：内科住院医
- **博士后**：Duke University，师从 Robert Lefkowitz——在此启动 β2 肾上腺素受体克隆工作
- **研究领域**：晶体学 / GPCR 结构与活性——β2 肾上腺素受体分子结构测定

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **面包师之子（1955）**：明尼苏达小镇 Little Falls 的面包师世家——三代人从烤炉走向实验室。
2. **德卢斯起点**：在明尼苏达大学德卢斯分校读生物学与化学，同时结识未来的妻子 Tong Sun Thian。
3. **耶鲁 M.D.（cum laude）**：以优等成绩从耶鲁医学院毕业；此后在圣路易斯华盛顿大学 Barnes-Jewish Hospital 完成内科住院医训练。
4. **转向实验室（1980s）**：放弃临床路径，到杜克大学在 Robert Lefkowitz 指导下做博士后，开始克隆 β2 肾上腺素受体——"医生转身做结构"的起点。
5. **克隆 β2 受体**：博士后期间参与克隆 β2 肾上腺素受体基因，为 GPCR 家族结构的发现提供关键拼图（与 Lefkowitz 2012 共享诺奖的工作基础）。
6. **西迁斯坦福（1989）**：加入斯坦福医学院分子与细胞生理学系；1987–2003 任 HHMI 研究员。
7. **学界公认难题**：GPCR 是重要的药物靶点，但在 X 射线晶体学中"臭名昭著地难做"（notoriously difficult，页面明载）。
8. **β2AR 结构突破**：实验室测定 β2 肾上腺素受体的分子结构——此前视紫红质（rhodopsin）是唯一有高分辨率结构的 GPCR；β2AR 之后多个 GPCR 结构接连测定。
9. **2011 复合物高峰**：与团队（含妻子 Tong Sun Thian 共同作者）发表 β2 肾上腺素受体–Gs 蛋白复合物晶体结构（Nature 477）。
10. **2007 Science "Breakthrough of the Year" runner-up**：GPCR 结构工作被评为《科学》年度突破亚军。
11. **2012 诺贝尔化学奖**：与恩师 Robert Lefkowitz 共享，表彰 "discoveries that reveal the workings of G protein-coupled receptors"（页面表述）——师与徒同台领奖。
12. **2017 南下深圳**：在深圳「诺贝尔奖科学家实验室」计划下，于香港中文大学（深圳）创办科比尔卡创新药物开发研究院（Kobilka Institute of Innovative Drug Discovery）。
13. **荣誉线**：1994 ASPET John J. Abel 药理学奖；2004 NINDS Javits Neuroscience Investigator Award；2011 NAS 院士；2017 Golden Plate Award；另载 Mendel Medal 与 Julius Axelrod Award（frontmatter）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深钢蓝 deepsteel） | `#123C5B` | 蛋白晶体的冷峻蓝与斯坦福红的沉稳衬底（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（GPCR 结构 badgeStruct） | `#2E5A9E` | 蓝 β2AR 七次跨膜结构 |
| 分类色 2（晶体学 badgeCrystal） | `#5C6B73` | 钢灰 X 射线晶体学 / 视紫红质对照 |
| 分类色 3（复合物与信号 badgeComplex） | `#1B7A43` | 绿 β2AR–Gs 复合物 / 信号转导 |
| 分类色 4（师门与转化 badgeMentor） | `#C0395B` | 玫瑰 Lefkowitz 师承 / ConfometRx 与深圳研究院 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——晶体生长：圆点从稀疏到聚簇，如蛋白分子在溶液中缓慢排布成晶。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（文件 `42-SyPUvzEkPyc-Timeless.wav`，**勿复制 wav 文件**）
- **风格**：沉稳 / 纪录片 / 长线坚持
- **匹配理由**：
  - "Timeless" 对应其研究气质——GPCR 结晶是被同行视为"臭名昭著地难"的长期工程，十年磨一剑
  - "沉稳" 匹配叙事节奏——小镇面包师之家 → 医生转身 → 结晶突破 → 师生共享诺奖，安静而笃定
  - "纪录片" 匹配结构生物学的视觉性——衍射图与电子密度如纪录片的慢镜头
- **时长核对**：以 ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒的幻灯时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 看见受体的结晶师 / Brian Kobilka 1955– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士后/领域/任职/荣誉）
03  科比尔卡的一生 — Sanger 式时间线（10 节点：1955→1977→1981→1980s→1987→1989→2007→2011→2012→2017）
04  早年：面包师之家 (1955–1977) — 表格「时间|事件|结果」（Little Falls / UMD / Yale M.D.）
05  医生转身：从内科到实验室 (1977–1987) — 表格「阶段|转折|结果」（住院医 → 杜克博士后）
06  克隆 β2 受体 (1980s) — 表格「问题|方法|结果」（与 Lefkowitz 合作起点）
07  最难结晶的靶点 (1989–2007) — 表格「挑战|方法|结果」+ 公式框：GPCR 七次跨膜 / rhodopsin 前例
08  β2AR 结构与 Gs 复合物 (2007–2011) — 表格「对象|技术|结果」+ 公式框：β2AR–Gs 复合物（Nature 477）
09  2012 诺贝尔化学奖 — 表格「奖项|年份|理由」+ 公式框：师生共享（Lefkowitz + Kobilka）
10  家庭与团队 — 表格「人物|身份|结果」（Tong Sun Thian / Jason / Megan / ConfometRx）
11  荣誉与奖项 — Sanger 式「类别|代表|意义」表格（含 itemize 荣誉清单）
12  从 Little Falls 到斯坦福 — 机构流程图（UMD → Yale → WashU → Duke → Stanford → CUHK-Shenzhen）
13  遗产：看见药物的锁孔 — 四分类遗产盒 + 公式框：GPCR 药物靶点意义
14  结尾 — 「把最难结晶的蛋白，变成最清晰的药靶。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2012 获奖口径 | 与 Robert Lefkowitz **两人共享**；官方完整 citation 英文全句页面无载——只可用页面实载表述 "discoveries that reveal the workings of G protein-coupled receptors"，**勿杜撰 nobelprize.org 全句** |
| 师承方向 | Kobilka 的身份是**博士后研究员**（postdoctoral fellow under Robert Lefkowitz，Duke）；其页面 frontmatter 记 doctoral_advisor=Robert Lefkowitz、infobox 记 Academic advisors——两篇统一写"博士后导师（Lefkowitz）"，勿写"博士导师"（本人无 PhD，只有 M.D.） |
| 学位口径 | BS（UMD 生物学+化学）+ M.D.（Yale，cum laude）——**无 PhD**；"physiologist" 是页面自我定位（description），勿写"生物化学家"当主头衔（那是 Lefkowitz） |
| 结构次序 | 高分辨率 GPCR 结构此前**只有视紫红质（rhodopsin）**；β2AR 是其后继者——勿写"第一个测出 GPCR 结构的团队" |
| 2011 复合物 | β2AR–Gs 复合物论文（Nature 477, 2011）共同作者含妻子 Tong Sun Thian——家庭与团队可并写，但她是共同作者而非博士后 |
| 深圳研究院 | 2017 年在香港中文大学（深圳）创办——按页面事实中性呈现，勿展开政策语境 |
| 家族史 | 祖父/父亲的面包师身份、祖母的普鲁士移民背景均为页面明载，可写；但须区分三代人，勿张冠李戴 |
| 奖项年份 | John J. Abel Award 1994、Javits 2004、NAS 院士 2011、Nobel 2012、Golden Plate 2017——勿混淆 |
| 在世口径 | 无卒日，封面与身份页一律 "1955–" 留白，勿虚构 |
| 中文译名 | 惯称「布莱恩·科比尔卡」，勿用「柯比尔卡」等其他形式 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q80907 | ✅ |
| name_zh | 布莱恩·科比尔卡 | ✅ |
| name_en | Brian Kobilka | ✅ |
| birth_date | 1955-05-30 | ✅ |
| death_date | NULL（在世留白） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | physiologist | ✅ |
| field_of_work | crystallography（person_field 细分：G protein-coupled receptors / crystallography / structural biology / molecular physiology，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**家人 / 导师 / 共同得主**（★红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Tong Sun Thian | 无向 | 马来华裔妻子，明尼苏达大学德卢斯分校相识；β2AR–Gs 复合物论文共同作者 |
| parent-child | Jason Kobilka | 无向（from<to） | 儿子（页面明载具名） |
| parent-child | Megan Kobilka | 无向（from<to） | 女儿（页面明载具名） |
| advisor-student | Robert Lefkowitz | 师→生 | 杜克博士后导师（1980s，克隆 β2 受体起点） |
| co-honored | Robert Lefkowitz | 无向 | 2012 诺贝尔化学奖共同得主 |

> **禁入库名单**（页面无规范全名或非本人直接关系）：祖父 Felix J. Kobilka、父亲 Franklyn A. Kobilka、祖母 Isabelle、母亲 Betty（仅家族叙事，非科研关系）、Søren G.F. Rasmussen 等 Publications 列表合作者（仅文献著录）、ConfometRx 合伙人（未具名）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2012，与 Robert Lefkowitz 共享）
- John J. Abel Award in Pharmacology（1994，ASPET 美国药理与实验治疗学会）
- Javits Neuroscience Investigator Award（2004，NINDS）
- National Academy of Sciences 院士（2011）
- Golden Plate Award（2017，American Academy of Achievement）
- Mendel Medal、Julius Axelrod Award（frontmatter 载，正文无年份——如写须留白年份）
- GPCR 结构工作获 2007《Science》"Breakthrough of the Year" **runner-up**（亚军，勿写"获奖"）

## 9. 机构清单

- 教育：St. Mary's Grade School 与 Little Falls High School（明尼苏达）；University of Minnesota Duluth（BS，生物学+化学）；Yale University School of Medicine（M.D.，cum laude）；Washington University in St. Louis / Barnes-Jewish Hospital（内科住院医）
- 任职：Duke University（Lefkowitz 实验室博士后，克隆 β2 受体）；Stanford University School of Medicine 分子与细胞生理学系教授（1989–）；HHMI 研究员（1987–2003）；ConfometRx 共同创办人（专注 GPCR 的生物技术公司）；Kobilka Institute of Innovative Drug Discovery（2017，香港中文大学（深圳））

## 10. 终审清单

- [ ] 生卒 1955-05-30 / 在世留白；出生地 Little Falls 表述准确
- [ ] 2012 与 Lefkowitz **两人共享**；获奖理由只用页面实载表述，未杜撰官方全句
- [ ] 师承统一为"博士后导师 Lefkowitz"；本人 M.D.（无 PhD）口径准确
- [ ] rhodopsin 前例与 β2AR 结构次序表述准确；2007 是 runner-up 非获奖
- [ ] 2011 复合物论文与妻子共同作者表述准确
- [ ] 引语核对——页面正文几无直接引语，全篇以间接转述为主
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Brian_Kobilka/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 `images.txt` 列表下载（2012 斯德哥尔摩 / 2024 斯坦福照），失败用装饰圆占位
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：本篇几乎无直接引语——凡引号内容须在原文找到（"notoriously difficult" 可用），否则改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，本提示词不直接改动总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
