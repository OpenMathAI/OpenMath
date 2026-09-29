# Hartmut Michel（哈特穆特·米歇尔）立传提示词

> qid=Q77086 · 1948-07-18 生于德国 Ludwigsburg · 在世 · 德国生物化学家 · 诺贝尔化学奖（1988，与 Robert Huber、Johann Deisenhofer 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Hartmut_Michel/`（page.md + metadata.json + page.html + images.txt）
> ⚠️ **本页为短页面**（infobox + 两节正文）且 images.txt 为空、infobox 照片（"Hartmut Michel in 2022"）文件名未导出——执行时从 page.html 查名经 Commons 下载，404 则装饰圆占位；以实载为准、严禁脑补。
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）。优先 page.html 查 infobox "Hartmut Michel in 2022" 图文件名经 Commons 下载（250px 改 500px）；404 则**装饰圆占位**（主色实心圆 + 姓名缩写）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 让膜蛋白长出晶体的人\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：左侧头像 + 右侧 2×2 信息网格：生卒、本名、国籍、出生地、教育（University of Tübingen；metadata 另载 Würzburg）、博士（页面无载导师与年份）、核心领域（膜蛋白结晶）、任职（马普生物物理学研究所所长 1987– / Jilin University 2026–）、配偶（Elena Olkhova）、荣誉。事实取自本地 Wikipedia infobox 与正文，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「晶体 / 脂膜双分子层」母题。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页 `tabularx` 三列表格（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Hartmut Michel（中文惯称：哈特穆特·米歇尔；ForMemRS）
- **生卒**：1948-07-18 生于 Ludwigsburg（时属 Württemberg-Baden，美占区，今巴登-符腾堡州；在世，death_date 留白）
- **国籍**：Germany（metadata 另载 West Germany，历史口径并入 Germany）
- **身份**：生物化学家（biochemist；马普生物物理学研究所分子膜生物学系主任）
- **家庭**：配偶 Elena Olkhova（infobox Spouse 明载）；其余家庭信息 page.md 无载——禁编造
- **教育轨迹**：
  - 服义务兵役（compulsory military service）后入 University of Tübingen 学生物化学
  - 毕业最后一年在 Dieter Oesterhelt 实验室研究嗜盐菌（halobacteria）的 ATPase 活性
  - metadata educated_at 另载 University of Würzburg（正文无载，身份页可注）
- **博士**：page.md **无载**博士年份与博士导师——身份信息页写「页面无载」，禁编造（勿与 Deisenhofer 篇的 Huber 导师关系混淆）
- **研究领域**：生物化学、膜蛋白结晶、X 射线晶体学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **战后德国出生（1948）**：生于美占区 Ludwigsburg（今巴登-符腾堡）——德国重建一代的普通起点。
2. **兵役与图宾根（1960s 末–）**：服完义务兵役入 University of Tübingen 读生物化学——起点朴实、路径清晰。
3. **Oesterhelt 实验室（毕业年）**：最后一年研究嗜盐菌 ATPase 活性——嗜盐菌（紫膜）体系正是后来膜蛋白研究的启蒙土壤。
4. **膜蛋白结晶：无人区**：膜蛋白嵌于脂膜、疏水面巨大，传统结晶方法束手无策——X 射线解析膜蛋白结构的前提是先让它长出有序晶体；Michel 的名号正系于此（infobox Known for: Crystallisation of membrane proteins）。
5. **马普体系**：1987 起任 Max Planck Institute for Biophysics（Frankfurt am Main）分子膜生物学系主任，兼 Goethe University Frankfurt 生物化学教授——自建实验体系长期深耕膜蛋白。
6. **紫色细菌光合反应中心结晶（1982 前后）**：完成光合细菌膜蛋白复合体（photosynthetic reaction center）的结晶——为三人组的结构解析提供关键晶体。
7. **三人组（1982–1985）**：与 Deisenhofer、Huber 用 X 射线晶体学测定该复合体中**超过 10,000 个原子**的精确排布。
8. **第一个膜蛋白晶体结构**：膜结合蛋白-辅因子复合体，光合作用启动环节的关键——史上第一个整合膜蛋白晶体结构。
9. **方法学的确立**：三人的研究「确立了一套膜蛋白结晶方法学」（page.md "established a methodology for crystallising membrane proteins"）——影响远超单个结构。
10. **1986 双奖先声**：Gottfried Wilhelm Leibniz Prize（德国研究联合会 DFG 最高荣誉）与 Max Delbrück Prize 同年而至——诺奖前夜的双重确认。
11. **1988 诺贝尔化学奖**：与 Johann Deisenhofer、Robert Huber 共享——「测定第一个整合膜蛋白晶体结构，一个对光合作用不可或缺的膜结合蛋白-辅因子复合体」（page.md 导语口径）。
12. **植物与细菌的同一性**：结构揭示植物与细菌光合过程的相似性——光合作用机制研究获得普遍理解。
13. **古稀跨界（2026）**：2026 年接受吉林大学（长春）全职教授职位，方向含转化医学、药物开发与结构生物学——诺奖得主与中国学界的晚近联结（正文明载，客观陈述）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（普鲁士蓝深调 deepprussian） | `#123C5B` | 膜蛋白结晶的冷静与执着（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（膜蛋白结晶 badgeCrystal） | `#2E5A9E` | 蓝结晶方法学 / 疏水面膜蛋白 |
| 分类色 2（光合反应中心 badgePhoto） | `#1B7A43` | 绿光合膜蛋白复合体 / 10,000 原子 |
| 分类色 3（马普与德国科学 badgeMPG） | `#D97B29` | 琥珀马普所长 / Leibniz 奖 |
| 分类色 4（国际合作 badgeBridge） | `#C0395B` | 玫瑰吉大任教 / 国际学界桥梁 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——晶体晶胞与脂膜双分子层意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Winds Of Freedom** — Really Slow Motion & Giant Apes（清单预分配，勿复制 wav 文件，Makefile 引用源路径）
- **文件**：`music_audio/inspiring-electronic/25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav`
- **风格**：史诗管弦 / 英雄气 / 开阔
- **匹配理由**：
  - "Winds Of Freedom" 呼应「把嵌在膜里的蛋白解放成晶体」的突破叙事——从不可能到方法学确立
  - 英雄管弦段落托住 10,000 原子结构 + 首个膜蛋白晶体结构的历史分量
  - 开阔收束匹配其 2026 古稀跨越大洲执教的晚章
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 让膜蛋白长出晶体的人 / Hartmut Michel 1948– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士无载/领域/任职/配偶/荣誉）
03  米歇尔的一生 — 高斯式时间线（10 节点：1948→图宾根→Oesterhelt 实验室→1982 结晶→1985 结构→1986 双奖→1987 马普→1988 诺奖→2026 吉大→在世）
04  战后德国与图宾根 (1948–1970s) — 表格「阶段|内容|结果」（短页面实载：兵役 + 图宾根 + Oesterhelt 实验室）
05  膜蛋白结晶之难 — 表格「问题|原因|传统困境」+ 公式框：膜蛋白 = 疏水跨膜段 + 亲水域
06  紫色细菌反应中心结晶 (1982 前后) — 表格「对象|方法|结果」+ 公式框：光合反应中心复合体
07  三人组 (1982–1985) — 表格「人物|途径|贡献」（三人共同用 X 射线晶体学测定）+ 公式框：>10,000 atoms
08  第一个膜蛋白晶体结构 — 表格「层级|内容|意义」+ 方法学确立（page.md 口径）
09  1988 诺贝尔化学奖 — 表格「得主|贡献|机构」（三人共享）+ 获奖口径
10  马普生物物理学研究所 (1987–) — 表格「机构|职务|方向」（分子膜生物学系主任 / Goethe Frankfurt 兼任）
11  1986 双奖先声 — 高斯式「奖项|年份|意义」表格（Leibniz Prize = DFG 最高荣誉 / Max Delbrück Prize）
12  古稀跨界：吉林大学 (2026) — 高斯 FFT 页式流程图或事件面板（全职教授 / 转化医学 / 药物开发 / 结构生物学）
13  遗产：膜蛋白结构生物学的开门人 — 四分类遗产盒（结晶方法学 / 光合机制 / 后续结构井喷 / 德中桥梁）
14  结尾 — 「先让蛋白质长成晶体，再让生命显出形状。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 短页面红线 | 本页 page.md 仅 infobox + 两节正文——中学/本科年份/兵役年份/家庭父母/子女全无载，一律留白，禁编造 |
| 1988 诺奖口径 | 三人共享；page.md 口径 "for determination of the first crystal structure of an integral membrane protein, a membrane-bound complex of proteins and co-factors that is essential to photosynthesis"——从本地导语口径，禁另编 citation 全句 |
| 博士导师红线 | page.md **无载**博士导师与博士年份——禁写 Huber 或 Oesterhelt 为导师；Oesterhelt 仅明载「毕业最后一年在其实验室工作」 |
| Oesterhelt 关系 | 只能写「博士学习最后一年在 Dieter Oesterhelt 实验室研究嗜盐菌 ATPase 活性」（type=other 入库）——勿升格为 advisor-student |
| 三人分工 | page.md 未做明细分工表——Slide 07 只写「三人共同用 X 射线晶体学测定」；Michel 的独立标识是**膜蛋白结晶**（infobox Known for），可写但注明是 infobox 口径 |
| 双奖年份 | Leibniz Prize 与 Max Delbrück Prize 均 1986（page.md 两处明载）——勿错位年份 |
| Leibniz Prize 定性 | 「DFG 授予、德国研究领域最高荣誉」（page.md "the highest honour awarded in German research"）——勿写成"德国最高科学奖"之类泛称 |
| ForMemRS | 2005 当选皇家学会外籍院士——年份勿与他奖混 |
| 吉林大学口径 | 2026 年接受全职教授职位（正文明载 "In 2026, Michel accepted a position as full-time professor"）——客观陈述；涉华表述保持中性学术口径，勿加评论 |
| 出生地口径 | Ludwigsburg 时属 Württemberg-Baden、美占区——今巴登-符腾堡州；正文写「生于 Ludwigsburg（今巴登-符腾堡）」 |
| 国籍 | Germany（metadata 的 West Germany 为历史口径，并入 Germany，不单列） |
| 配偶 | Elena Olkhova 仅 infobox Spouse 一行——可写入身份页，note 入库 spouse；其余婚姻细节无载禁编造 |
| 中文引语 | page.md 无直接引语，全篇禁用引号原话，一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q77086 | ✅ |
| name_zh | 哈特穆特·米歇尔 | ✅ |
| name_en | Hartmut Michel | ✅ |
| birth_date | 1948-07-18 | ✅ |
| death_date | （在世，留白） | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表） | ✅ |
| has_biography | 0（待 Beamer 后置 1） | ✅ |

person_field 细分 rank 表：

| name_en | rank | name_zh |
|---|---|---|
| biochemistry | 0 | 生物化学 |
| membrane protein crystallisation | 1 | 膜蛋白结晶 |
| X-ray crystallography | 2 | X 射线晶体学 |

## 7. 社会关系入库清单

**共同得主 / 家庭 / 师门关联**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Robert Huber | 无向 | 1988 诺贝尔化学奖共同得主 |
| co-honored | Johann Deisenhofer | 无向 | 1988 诺贝尔化学奖共同得主 |
| spouse | Elena Olkhova | 无向 | infobox Spouse 明载 |
| other | Dieter Oesterhelt | 无向 | 博士学习最后一年在其实验室研究嗜盐菌 ATPase 活性（页面未明载导师名义） |

> metadata.json-only 一律不入库。本页禁入库名单：Goethe University Frankfurt / Jilin University（机构非个人）；1982–1985 三人合作已由 co-honored 覆盖，不另建 colleague 行；家庭父母/子女 page.md 无载，无关系可入。

## 8. 奖项清单

- Max Delbrück Prize（1986）
- Gottfried Wilhelm Leibniz Prize（1986；DFG 授予，德国研究领域最高荣誉）
- Nobel Prize in Chemistry（1988，与 Deisenhofer、Huber 共享）
- Bijvoet Medal（1989，Utrecht 大学 Bijvoet Center for Biomolecular Research）
- German Academy of Sciences Leopoldina 院士（1995）
- 皇家荷兰艺术与科学院外籍院士（1995）
- Foreign Member of the Royal Society，ForMemRS（2005）
- Otto Bayer Award；Klung Wilhelmy Science Award；Commander's Cross of the Order of Merit of the Federal Republic of Germany；Order of Merit of Baden-Württemberg；Würzburg 与 Bologna 荣誉博士（metadata 载，年份以官方页面为准）

## 9. 机构清单

- 教育：University of Tübingen（生物化学；毕业年在 Dieter Oesterhelt 实验室）；metadata 另载 University of Würzburg
- 任职：Max Planck Institute for Biophysics, Frankfurt am Main 分子膜生物学系主任（1987–）；Goethe University Frankfurt 生物化学教授（1987–）；Jilin University（长春）全职教授（2026–，方向：转化医学、药物开发、结构生物学）

## 10. 终审清单

- [ ] 生卒 1948-07-18（Ludwigsburg）/ 在世留白
- [ ] 1988 三人共享（Huber、Deisenhofer）表述准确；获奖理由按 page.md 导语口径
- [ ] 博士导师/博士年份无载留白；Oesterhelt 关系类型为 other（非 advisor）
- [ ] Leibniz Prize 与 Max Delbrück Prize 均 1986、Leibniz 定性「DFG 最高荣誉」
- [ ] 1987 马普所长 / 2026 吉大任教年份准确、涉华表述中性
- [ ] 配偶 Elena Olkhova 入库、其余家庭无载留白
- [ ] 引语全篇间接转述（page.md 无直接引语）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Hartmut_Michel/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：infobox "in 2022" 图经 page.html 查名下载；404 则装饰圆占位
- [ ] 国籍：封面顶部明示德国
- [ ] 引语核对：全篇无引号原话（间接转述）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：`chemist/prompt_manifest.json` chem-batch-20 · Hartmut Michel（1988，BGM Winds Of Freedom，主色 #123C5B）。
> **开始执行。每完成一步向主控汇报。**
