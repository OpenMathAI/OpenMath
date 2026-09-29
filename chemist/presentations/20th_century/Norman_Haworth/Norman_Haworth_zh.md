# Norman Haworth（诺曼·霍沃思）立传提示词

> qid=Q204600 · 1883-03-19 – 1950-03-19 · 英国化学家 · 20 世纪 · 诺贝尔化学奖（1937，与 Paul Karrer 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Norman_Haworth/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传的 Beamer 格式与提示词结构**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 无真实肖像，先尝试 Wikipedia REST API `page/summary` 取 infobox 原图（Commons `Special:FilePath` 回退，250px 改 500px）；全部 404 则用**装饰圆占位**（主色渐变圆 + 首字母），并在 Review 时记录。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 糖环与维生素 C\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Sir Walter Norman Haworth、国籍、出生地 White Coppice（Lancashire）/去世地 Barnt Green（Worcestershire）、教育（Manchester / Göttingen）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「糖环 / 吡喃环」母题——圆形暗示 Haworth 投影式中的六元环平面。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 Haworth 投影 / 维生素 C 合成式。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir Walter Norman Haworth（中文惯称：沃尔特·诺曼·霍沃思；通称 Norman Haworth，FRS，1947 年受封 Knight Bachelor）
- **生卒**：1883-03-19 生于英格兰兰开夏郡 White Coppice 村 → 1950-03-19 逝于伍斯特郡 Barnt Green（**67 岁生日当天**心脏病突发猝逝）
- **国籍**：United Kingdom（英国）
- **身份**：化学家（有机化学；碳水化合物与维生素 C）
- **家庭**：14 岁起在父亲管理的当地 Rylands 油毡厂做工；父母最初**极力反对**他升学；1922 年娶 Violet Chilton Dobbie（Sir James Johnston Dobbie 之女），育二子 James 与 David
- **教育轨迹**：
  - 1903 通过入学考试进入 University of Manchester 学化学（不顾父母反对）
  - 1906 一等荣誉学士；随后在 William Henry Perkin Jr. 指导下获硕士学位
  - 获 1851 Research Fellowship，赴 University of Göttingen，在 Otto Wallach 实验室**仅一年**即获 PhD
  - 1911 获 Manchester DSc；短期任 Imperial College of Science and Technology 高级化学示范员
- **导师**：William Henry Perkin Jr.（硕士导师）、Otto Wallach（哥廷根博士导师，1910 诺贝尔化学奖得主）
- **研究领域**：有机化学——糖类结构（碳水化合物化学）、维生素 C（抗坏血酸）合成、Haworth 投影式

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **油毡厂学徒（1883–1903）**：14 岁起在父亲的 Rylands 油毡厂做工，靠自修通过曼彻斯特大学入学考试——父母反对下的自我教育。
2. **曼彻斯特转折（1903–1906）**：入学即崭露头角，1906 一等荣誉学位；师从 William Henry Perkin Jr. 完成硕士。
3. **哥廷根一年博士（1906 后）**：持 1851 Research Fellowship 赴 Wallach 实验室，仅一年获 PhD——效率惊人的留学记录。
4. **DSc 与帝国理工（1911）**：曼彻斯特 DSc；Imperial College 高级示范员（Senior Demonstrator in Chemistry）。
5. **圣安德鲁斯转向糖化学（1912）**：任 United College 讲师；彼时 Thomas Purdie 与 James Irvine 正在圣安德鲁斯研究碳水化合物化学，Haworth 由此进入糖领域。
6. **Haworth 甲基化（1915）**：用硫酸二甲酯 + 碱制备糖的甲醚新方法（今称 Haworth methylation）。
7. **一战军工组织者（1914–1918）**：在圣安德鲁斯组织实验室为英国政府生产化学品与药品。
8. **双糖结构定音（至 1928）**：确认麦芽糖、纤维二糖、乳糖、龙胆二糖、蜜二糖、龙胆三糖、棉子糖等结构，以及醛糖的葡萄糖苷环互变异构结构。
9. **伯明翰 Mason 讲席（1920/1925）**：1920 任 Durham 大学 Armstrong College 有机化学教授（次年任系主任），1925 起任伯明翰 Mason Professor of Chemistry（至 1948）。
10. **维生素 C 的合成（1933）**：与 Edmund Hirst 及 Maurice Stacey 领衔的博士后团队，在正确推定结构与光学异构性质后报道合成维生素 C；样品来自 Albert Szent-Györgyi（可从匈牙利辣椒大量提取的 "hexuronic acid"）；与 Szent-Györgyi 共同提出新名 "ascorbic acid"。
11. **《The Constitution of Sugars》（1929）**：糖结构经典教科书。
12. **1937 诺贝尔化学奖**：官方理由 "for his investigations on carbohydrates and vitamin C"，与瑞士化学家 Paul Karrer（维生素方面的工作）**共享**。
13. **Haworth 投影与身后**：透视法把三维糖结构画成二维平面图，至今广泛用于生物化学；二战期间为 MAUD 委员会（英国原子弹研究）成员；伯明翰大学有 Haworth Building 与 Haworth Chair；1977 年 Royal Mail 发行纪念邮票；FRS（1928）、Royal Medal（1942）、1947 年新年受勋名录受封爵士；1950-03-19 67 岁生日当天心脏病去世。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海蓝 deepsea） | `#16324F` | 糖环结构的严谨与深度（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（糖化学 badgeSugar） | `#2E5A9E` | 蓝双糖结构 / Haworth 甲基化 |
| 分类色 2（维生素 C badgeVitC） | `#C9702A` | 橙抗坏血酸 / 1933 合成 |
| 分类色 3（构象与投影 badgeProj） | `#1B7A43` | 绿 Haworth 投影式 / 环状结构 |
| 分类色 4（机构与传承 badgeLegacy） | `#8C3A5B` | 玫瑰伯明翰 / MAUD 委员会 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「吡喃糖六元环」的平面圆环意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Pathfinder** — Ghostwriter Music（文件 `music_audio/inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav`；不要复制 wav 文件，Makefile 直接引用该路径）
- **风格**：开拓 / 探路者 / 温暖上扬
- **匹配理由**：
  - "探路者" 匹配霍沃思的学术轨迹——从油毡厂学徒到哥廷根博士再到糖化学版图的开拓（甲基化法、双糖结构、投影式）
  - "温暖上扬" 匹配维生素 C 合成（1933）这一造福公众健康的顶点叙事
  - 纪录片质感匹配「工匠之子 → 曼彻斯特 → 哥廷根 → 伯明翰 → 诺贝尔」的线性传记
- **时长对齐**：以实际曲目时长与 15 页 × 7 秒 ≈ 105 秒比较，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 糖环与维生素 C / Norman Haworth 1883–1950 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育/博士导师/领域/荣誉）
03  霍沃思的一生 — 高斯式时间线（10 节点：1883→1903→1906→1911→1912→1915→1925→1933→1937→1950）
04  早年：油毡厂里的化学家 (1883–1903) — 表格「时间|事件|结果」
05  曼彻斯特与哥廷根 (1903–1911) — 表格「阶段|导师|收获」+ 公式框：1851 Fellowship → 一年 PhD
06  圣安德鲁斯：进入糖的世界 (1912–1919) — 表格「问题|方法|结果」（甲基化法 + 一战化工组织）
07  双糖结构定音 (1920–1929) — 表格「糖|结构贡献|意义」+ 公式框：醛糖葡萄糖苷环互变异构
08  维生素 C：从 hexuronic acid 到 ascorbic acid (1933) — 表格「人物|角色|贡献」+ 公式框：合成路线
09  1937 诺贝尔化学奖 — 官方获奖理由 + 与 Paul Karrer 共享（表格「得主|领域|理由」）
10  Haworth 投影式 — 高斯式图表页：三维结构 → 二维透视表示法（至今通用）
11  战时与晚年 — MAUD 委员会 / 1947 爵士 / 荣誉清单（Longstaff 1933、Davy 1934、Nobel 1937、Royal Medal 1942）
12  家庭与传承 — Violet Chilton Dobbie、二子 James/David；伯明翰 Haworth Building / Haworth Chair / 1977 邮票
13  遗产：糖化学的坐标系 — 四分类遗产盒 + 公式框：Haworth projection
14  结尾 — 「他把糖画成了人人可读的环。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1937 共享 | 与 Paul Karrer **共享** 1937 诺贝尔化学奖（Karrer 因维生素方面工作）；勿写 Haworth 独享 |
| 获奖理由 | 官方措辞 "for his investigations on carbohydrates and vitamin C"——勿泛化成"合成维生素 C 获奖alone"，也勿把 Karrer 的工作并进 Haworth 理由 |
| 姓名口径 | 全名 Sir Walter Norman Haworth，通称 Norman Haworth——勿与同性同姓的其他 Haworth 混淆；标题用 Norman Haworth |
| 博士导师 | 硕士导师 William Henry Perkin Jr.（勿漏 "Jr."，其父同为化学家）；博士导师 Otto Wallach——两者勿混 |
| 学位顺序 | Manchester 本科 1906 → 硕士（Perkin Jr.）→ Göttingen PhD（Wallach，约一年）→ 1911 Manchester DSc——PhD 在 Göttingen 而非 Manchester |
| 维生素 C 分工 | 结构推定 + 合成是 Haworth 组（Hirst、Stacey）；发现其维生素属性的是 Szent-Györgyi 与 Charles Glen King；命名 "ascorbic acid" 是 Haworth 与 Szent-Györgyi 共同提出——勿把发现属性写成 Haworth |
| Charles Glen King | 仅是 Szent-Györgyi 的并列发现者，与 Haworth 无直接合作记载——**不入库**，行文至多一笔带过 |
| 出生地/去世地 | 生于 White Coppice（Lancashire），逝于 Barnt Green（Worcestershire），67 岁生日当天心脏病——勿写"剑桥" |
| 受封 | 1947 New Year Honours 受封 Knight Bachelor——头衔 Sir；与 Sanger "拒爵位" 情节相反，勿混淆 |
| MAUD 委员会 | 二战期间成员，监督英国原子弹研究——可客观一句，勿展开 |
| PCT 年份 | Purdie（1843–1916）/ Irvine（1877–1950）在圣安德鲁斯研究糖化学是 Haworth 转向的**背景**，与其无直接师承/合作记载——勿写成导师或合作者 |
| 教育反差 | 父母**极力反对**其升学——勿美化成"家庭支持" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q204600 | ✅（metadata.json） |
| name_zh | 诺曼·霍沃思 | ✅ |
| name_en | Norman Haworth | ✅（page.md 规范名，db_id 空） |
| birth_date | 1883-03-19 | ✅ |
| death_date | 1950-03-19 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：carbohydrate chemistry / vitamins / structural chemistry / conformational analysis，带 rank） | ✅ |
| has_biography | false（立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 共同得主**（仅收 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | William Henry Perkin Jr. | 师→生（硕士导师） | Manchester 硕士导师 |
| advisor-student | Otto Wallach | 师→生（博士导师） | Göttingen 实验室一年获 PhD |
| spouse | Violet Chilton Dobbie | 无向 | 1922 年结婚，Dobbie 爵士之女 |
| colleague | Edmund Hirst | 无向 | 1933 共同完成维生素 C 结构推定与合成 |
| colleague | Maurice Stacey | 无向 | 博士后团队领衔，参与维生素 C 合成 |
| colleague | Albert Szent-Györgyi | 无向 | 提供维生素 C 参考样品；共同命名 ascorbic acid |
| co-honored | Paul Karrer | 无向 | 1937 诺贝尔化学奖共同得主 |

**门生**：page.md 无 doctoral students 明载——**不设学生关系**。

> **禁入库名单（metadata-only / 背景人物）**：Charles Glen King（Szent-Györgyi 的并列发现者，与 Haworth 无直接关系记载）、Thomas Purdie、James Irvine（圣安德鲁斯背景人物）、James Johnston Dobbie（岳父）、Nigel Simpkins、Neil Champness（后世 Haworth Chair 持有者）、父母（未载名）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1937，与 Paul Karrer 共享，"for his investigations on carbohydrates and vitamin C"）
- Longstaff Prize（1933）
- Davy Medal（1934）
- Royal Medal（1942）
- Fellow of the Royal Society，FRS（1928）
- 1851 Research Fellowship
- Knight Bachelor（1947 New Year Honours）
- 荣誉学位：University of Oslo、University of Manchester、Queen's University Belfast（honorary doctorate）
- Royal Society Bakerian Medal（infobox award_received 载）

## 9. 机构清单

- 教育：University of Manchester（1903 入学，1906 一等荣誉，硕士，1911 DSc）、University of Göttingen（PhD，Wallach 实验室）
- 任职：Imperial College of Science and Technology（高级示范员）、United College of University of St Andrews（1912 讲师）、Durham University Armstrong College（1920 有机化学教授，1921 系主任）、University of Birmingham（1925 Mason Professor of Chemistry，至 1948）
- 纪念：Haworth Building（伯明翰化学学院）、Haworth Chair of Chemistry、1977 Royal Mail 邮票

## 10. 终审清单

- [ ] 生卒 1883-03-19 / 1950-03-19，67 岁生日当天去世；出生地 White Coppice、去世地 Barnt Green
- [ ] 1937 与 Paul Karrer 共享表述准确；获奖理由英文原句准确
- [ ] 硕士导师 Perkin Jr.、博士导师 Wallach 表述准确；PhD 在 Göttingen
- [ ] 维生素 C 分工表述准确（Haworth 组推定结构+合成；Szent-Györgyi/King 发现维生素属性；共同命名）
- [ ] 双糖清单与 1929 教科书表述准确；Haworth methylation（1915）表述准确
- [ ] 1947 受封爵士表述准确
- [ ] 中文引号内无 page.md 无法溯源的"原话"；无"第一次/唯一"类断言
- [ ] 引语全部可在本地 Wikipedia 原文找到（获奖理由原句、命名 ascorbic acid 记载）
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Norman_Haworth/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 无真实肖像——REST API / Special:FilePath 尝试结果与占位方案记录回写本节
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（获奖理由原句）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 模板）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，执行者不改。
> **最重要的事：每写一页就 make，看到溢出就修。**
