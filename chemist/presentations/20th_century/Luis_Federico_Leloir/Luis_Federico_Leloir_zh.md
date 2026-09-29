# Luis Federico Leloir（路易斯·费德里科·莱卢瓦尔）立传提示词

> qid=Q233985 · 1906-09-06 – 1987-12-02 · 阿根廷生物化学家 · 20 世纪 · 诺贝尔化学奖（1970，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Luis_Federico_Leloir/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 `images.txt` / Commons 下载；404 则用装饰圆占位并在 Review 记录）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 糖核苷酸的发现者\enspace·\enspace 阿根廷`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「糖核苷酸 / 代谢通路」母题——离散圆点暗示糖单元在通路中的接力。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Luis Federico Leloir（中文惯称：路易斯·费德里科·莱卢瓦尔；头衔 ForMemRS）
- **生卒**：1906-09-06 生于法国巴黎（81 Víctor Hugo 路老宅，距凯旋门数个街区）→ 1987-12-02 逝于阿根廷布宜诺斯艾利斯（心脏病发作，从实验室回家后不久），享年 81；葬于 La Recoleta 公墓家族墓
- **国籍**：Argentina（阿根廷，后归化取得国籍）；生于法国，1908 年随母返阿——nationalities 多条带 rank
- **身份**：医师出身的生物化学家（physician & biochemist）、1970 年诺贝尔化学奖得主
- **家庭**：父母 Federico Augusto Rufino 与 Hortencia Aguirre de Leloir 为治父病赴巴黎，父于路易斯出生前约一周病逝；外祖父母自西班牙巴斯克地区移民阿根廷，家族拥有 400 km² 海岸地产 *El Tuyú*；兄弟姐妹八人；1943 年娶 Amelia Zuberbuhler（1920–2013），育一女 Amelia
- **教育轨迹**：
  - Escuela General San Martín（小学）、Colegio Lacordaire（中学）、英国 Beaumont College 数月
  - 巴黎 École Polytechnique 建筑学肄业（很快放弃）
  - University of Buenos Aires 医学院（解剖学考了四次才通过）；1932 获医师文凭；两年后获最佳博士论文表彰
- **博士导师**：Bernardo Houssay（1933 年起；1947 年诺贝尔生理学或医学奖得主）
- **研究领域**：生物化学——糖核苷酸、碳水化合物代谢、肾性高血压、半乳糖血症

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **生于巴黎的阿根廷人（1906）**：父亲为治病携妻赴巴黎，却在一周内病逝——遗腹般出生的路易斯 1908 年随母返回阿根廷。
2. **潘帕斯草原的观察者**：童年在 *El Tuyú* 庄园观察自然现象，学校功课平平，建筑学半途而废。
3. **高尔夫酱（1920s）**：在 Mar del Plata 海洋俱乐部把番茄酱与蛋黄酱混调出 *salsa golf*；他后来打趣"当初要是给这酱申请专利，现在科研经费就宽裕多了"（间接转述）。
4. **从病房转向实验室（1932–1933）**：行医受挫后自述（转述）"我们对病人能做的太少了……抗生素、精神药物那时都还不存在"——转向实验室研究。
5. **遇见 Houssay（1933）**：经亲戚姻亲 Udaondo 医生引荐，进入 Bernardo Houssay 门下，博士论文研究肾上腺与碳水化合物代谢；诺奖演讲中自称"整个研究生涯都受一个人影响：Bernardo A. Houssay 教授"。
6. **剑桥进修（1936–1937）**：赴剑桥在另一位诺奖得主 Frederick Gowland Hopkins 指导下深造，研究氰化物与焦磷酸对琥珀酸脱氢酶的作用——从此专攻碳水化合物代谢。
7. **流亡美国（1943–1945）**：Houssay 因联名反对纳粹被军政府开除，莱卢瓦尔流亡——华盛顿大学圣路易斯药理系副教授（与 Carl Cori、Gerty Cori 夫妇合作）→ 哥伦比亚大学随 David E. Green 任研究助理。
8. **白色革命：Campomar 研究所（1947）**：实业家 Jaime Campomar 出资创办研究所，莱卢瓦尔任所长至 1981 年——五个房间起家的私人研究所。
9. **无细胞系统（1940s 末）**：与 J. M. Muñoz 制得活性无细胞体系（学界首次）；买不起冷冻离心机，就用塞满盐和冰的轮胎土法离心。
10. **糖核苷酸（1948，★ 核心贡献）**：1948 年初鉴定出碳水化合物代谢的关键**糖核苷酸**——Campomar 研究所从此世界闻名。
11. **Leloir 通路与半乳糖血症**：阐明半乳糖代谢初级机制（今称 Leloir pathway），确定半乳糖血症病因（缺乏 Galactose-1-phosphate uridylyltransferase）——奠定诊断与治疗基础。
12. **1970 诺贝尔化学奖（独享）**：表彰"发现碳水化合物合成及其在体内转化为能量的代谢通路"；领奖时借用丘吉尔 1940 年名言（转述）"never have I received so much for so little"；8 万美元奖金全部投入研究；团队用试管喝香槟庆祝。
13. **科学苦行僧（1987）**："真正的科学修士"——妻子每天开 Fiat 600 送他上班、同一件灰色工装、同一把草编椅坐几十年；1983 年成为第三世界科学院创始成员；1987-12-02 心脏病去世，葬 La Recoleta 公墓。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深砖红 brickred） | `#8A1E2D` | 潘帕斯烈日与南美科学殉道者的底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（糖核苷酸 badgeSugar） | `#1E5A8A` | 蓝 UDP-葡萄糖 / 糖核苷酸 |
| 分类色 2（代谢通路 badgePathway） | `#1B7A43` | 绿 Leloir 通路 / 半乳糖代谢 |
| 分类色 3（流亡与建所 badgeExile） | `#6E4A1E` | 暗金流亡美国 / Campomar 研究所 |
| 分类色 4（临床遗产 badgeClinic） | `#5B2A6E` | 紫半乳糖血症 / 高血压 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「糖核苷酸接力代谢通路」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgy** — AShamaluevMusic（文件：`music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav`；不要复制 wav 到人物目录，video 阶段按路径引用）
- **风格**：忧伤 / 电影感 / 纪录片
- **匹配理由**：
  - "怀旧" 匹配其身份母题——生于巴黎、心属阿根廷、自传取名 "Long Ago and Far Away"（取自 Hudson 小说）
  - "忧伤" 匹配清贫而坚韧的科学人生——轮胎离心机、纸板排水槽、自掏诺奖奖金做经费
  - "纪录片" 匹配传记叙事——巴黎 → 布宜诺斯艾利斯 → 剑桥 → 流亡 → Campomar → 诺奖
- **时长核对**：video 阶段用 ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 糖核苷酸的发现者 / Luis Federico Leloir 1906–1987 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  莱卢瓦尔的一生 — Sanger 式时间线（10 节点：1906→1932→1933→1936→1943→1947→1948→1957→1970→1987）
04  巴黎出生与潘帕斯童年 (1906–1920s) — 表格「时间|事件|结果」+ 高尔夫酱轶事
05  从医学到实验室 (1932–1935) — 表格「时间|事件|结果」（解剖四次 / 最佳博士论文 / 转向研究）
06  Houssay 与剑桥 (1933–1937) — 表格「导师|课题|结果」
07  流亡美国 (1943–1945) — 表格「机构|合作者|结果」（Cori 夫妇 / David E. Green）
08  Campomar 研究所 (1947–1957) — 表格「条件|方法|结果」（五个房间 / 轮胎离心机 / 无细胞系统）
09  糖核苷酸与 Leloir 通路（★ 核心页）— 表格「问题|方法|结果」+ 公式框：半乳糖 → 葡萄糖（GALT 缺陷）
10  1970 诺贝尔化学奖 — 表格「人物|贡献|理由」+ 公式框：碳水化合物合成与能量转换通路（独享）
11  荣誉年表 — Sanger 式「年份|荣誉|意义」表格（Horwitz 1967 / ForMemRS 1972 / Legion of Honour 1982 / Konex 1983）
12  科学修士 — 表格「习惯|细节|意义」（Fiat 600 / 灰工装 / 试管香槟 / 奖金全投研究）
13  遗产：第三世界的科学灯塔 — 四分类遗产盒 + 公式框：Leloir pathway（今研究所 20 名资深研究员）
14  结尾 — 「在清贫的土地上，科学依然可以生根。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1970 获奖口径 | **独享**（1956–1990 年代罕见的化学奖独享）；理由为"发现碳水化合物合成及转化为能量的代谢通路"（page.md 叙述口径）；12-02 领奖——恰与其 1987 年忌日同月同日，可作注但勿渲染 |
| 出生地 | 生于**法国巴黎**（1906-09-06）——国籍是阿根廷：勿写成"生于阿根廷" |
| infobox 机构年份噪声 | infobox 列 Cambridge "1936–1943" 与正文"1937 年返回布宜诺斯艾利斯"矛盾——**以正文为准**（剑桥进修仅 1936–37 一年左右） |
| Houssay 关系 | 博士导师 + 终身合作者（至 1971 年去世）；Houssay 1947 获诺奖是**生理学或医学奖**——勿写化学奖 |
| 剑桥身份 | 1936 年是博士学位**之后**的进修（under the supervision of Hopkins）——勿写成攻读博士 |
| Cori 夫妇 | Carl Cori 与 Gerty Cori 是华盛顿大学时期的**合作者**——勿写成师承 |
| 解剖考试 | 四次才通过的是**解剖学考试**——勿写"多次挂科"泛化 |
| 引语红线 | "If I had patented that sauce..."、"we could do little for our patients..."、"never have I received so much for so little"、Houssay 影响句、获奖感言段——均须忠实 page.md 原文或明确标注为转述；无出处的"原话"一律改间接转述 |
| "第三位阿根廷诺奖得主" | page.md 原文 "becoming only the third Argentine to receive the prestigious honor **at the time**"——必须带"当时"限定 |
| 死因 | 1987-12-02 心脏病发作，从实验室回家后不久——勿写"在实验室猝死" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q233985 | ✅ |
| name_zh | 路易斯·费德里科·莱卢瓦尔 | ✅ |
| name_en | Luis Federico Leloir | ✅ |
| birth_date | 1906-09-06 | ✅ |
| death_date | 1987-12-02 | ✅ |
| nationality | Argentina（rank 0）+ France（rank 1，出生地） | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / carbohydrate metabolism / sugar nucleotides / renal hypertension，带 rank） | ✅ |
| has_biography | 0（Beamer 立传完成后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同研究者 / 婚姻**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Bernardo Houssay | 师→生（博士导师） | 1933 年起指导肾上腺与碳水化合物代谢论文；1947 诺奖生理学或医学奖 |
| colleague | Frederick Gowland Hopkins | 无向 | 1936 剑桥在其指导下进修（博士学位之后，非师承攻读） |
| colleague | Carl Cori | 无向 | 1943–44 华盛顿大学圣路易斯合作 |
| colleague | Gerty Cori | 无向 | 1943–44 华盛顿大学圣路易斯合作 |
| colleague | David E. Green | 无向 | 哥伦比亚大学共事；Green 激励其回国自建研究 |
| colleague | Ranwel Caputto | 无向 | 1947 年起 Campomar 团队核心成员（乳腺研究/碳水储存） |
| colleague | Enrico Cabib | 无向 | 1947 年起团队成员；后与 Leloir 同任 UBA 名誉教授 |
| colleague | Raúl Trucco | 无向 | 1947 年团队名单明载 |
| colleague | Alejandro Paladini | 无向 | 1947 年团队名单明载 |
| colleague | Carlos Eugenio Cardini | 无向 | 团队成员；与 Leloir/Cabib 同任 UBA 名誉教授 |
| colleague | José Luis Reissig | 无向 | 1947 年团队名单明载 |
| colleague | J. M. Muñoz | 无向 | 合作制得首个活性无细胞体系 |
| other | Jaime Campomar | 无向 | 实业家资助人，1947 出资创办研究所 |
| spouse | Amelia Zuberbuhler | 无向 | 1943 年结婚（1920–2013），育一女 Amelia |

> metadata.json-only 的关系一律不入库；Mario Bunge 是其友与评述者（回忆性表述），仅作叙事素材不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1970，独享）
- Third National Science Award（阿根廷，1943）
- T. Ducett Jones Memorial Award（1958）
- 美国国家科学院国际院士（1960）；American Academy of Arts and Sciences（1961）；American Philosophical Society（1963）
- Bunge and Born Foundation Award（1965）；Gairdner Foundation Award（1966）
- Louisa Gross Horwitz Prize（哥伦比亚大学，1967）
- Benito Juárez Award（1968）；科尔多瓦国立大学荣誉博士（1968）；Juan José Jolly Kyle Award（阿根廷化学会，1968）
- 英国生化学会荣誉会员（1969）
- Orden de Andrés Bello（1971）；Foreign Member of the Royal Society，ForMemRS（1972）
- Grand Cross of the Order of Bernardo O'Higgins（智利，1976）
- Legion of Honour（法国，1982）；Diamond Konex Award（科学与技术，1983）
- 荣誉博士：University of Granada、University of Paris、University of Bordeaux-II

## 9. 机构清单

- 教育：Escuela General San Martín、Colegio Lacordaire、Beaumont College（英，数月）、École Polytechnique（肄业）、University of Buenos Aires（医师 1932；最佳博士论文）
- 任职：University of Buenos Aires 医学系；华盛顿大学圣路易斯（1943–44，药理系副教授）；哥伦比亚大学（1944–45，研究助理）；Fundación Instituto Campomar 所长（1947–1981；1958 迁入原女子学校；后更名 Fundación Instituto Leloir，并入 UBA 体系）
- 创始成员：Third World Academy of Sciences / The World Academy of Sciences（1983）；World Cultural Council 相关页面无载（★ 注意：World Cultural Council 创始成员是 Herzberg/Anfinsen，Leloir 页面无载，勿写）

## 10. 终审清单

- [x] 生卒 1906-09-06 / 1987-12-02，享年 81，出生地巴黎、去世地布宜诺斯艾利斯（心脏病）
- [x] 1970 独享；"当时第三位阿根廷诺奖得主"带时间限定
- [x] 剑桥身份=博士后的进修（非攻读）；infobox 机构年份噪声以正文为准
- [x] 双国籍 rank：Argentina 0 / France 1
- [x] 团队成员七人（Caputto/Cabib/Trucco/Paladini/Cardini/Reissig/Muñoz）均为 page.md 明载
- [x] 引语全部可在 page.md 溯源或标注转述；无杜撰"原话"
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Luis_Federico_Leloir/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 images.txt / Commons 下载（早期 20 余岁照片可用）；404 用装饰圆占位并记录
- [ ] **国籍**：封面顶部明示阿根廷（生地巴黎作小注）
- [ ] **引语核对**： golf 酱 / 病房 / 丘吉尔 / 获奖感言——逐一溯源
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 骨架）对齐

---

> **名单状态**：本文件由 chem-batch-14 生成；`chemist/generate_20th_century_list.py` 由主控统一更新。
> **最重要的事：每写一页就 make，看到溢出就修。**
