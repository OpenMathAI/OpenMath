# Alexander R. Todd（亚历山大·罗伯塔斯·托德勋爵）立传提示词

> qid=Q157242 · 1907-10-02 – 1997-01-10 · 英国生物化学家 · 20 世纪 · 诺贝尔化学奖（1957，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Alexander_R._Todd/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 下取 1957 年照 "Alexander Todd in 1957"，若 images.txt 无可用图则用装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace\enspace 核苷酸的建造者\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育（格拉斯哥/法兰克福/牛津）、博士（双博士：Dr.phil.nat. 1931 + DPhil 1933）、师承（Borsche/Robinson）、核心领域、荣誉（OM 勋爵）。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「核苷酸单元的逐级连接」母题——离散圆点连线暗示糖环—磷酸骨架的链式结构。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（ATP/FAD 结构式、3′-5′ 磷酸二酯键骨架）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Alexander Robertus Todd, Baron Todd（中文惯称：亚历山大·托德勋爵；头衔 OM FRS FRSE）
- **生卒**：1907-10-02 生于苏格兰格拉斯哥近郊 Cathcart → 1997-01-10 逝于剑桥（infobox 作 Oakington；正文作 Cambridge），享年 89，死因心脏病发作
- **国籍**：United Kingdom（英国；苏格兰格拉斯哥出身）
- **身份**：生物化学家（biochemist；1957 诺贝尔化学奖独享得主；后为终身贵族、皇家学会会长）
- **家庭**：长子；父 Alexander Todd 为格拉斯哥地铁（Glasgow Subway）职员、JP，母 Jane Lowry。1937 年娶 Alison Sarah Dale（1987 卒），她是诺贝尔奖得主 Henry Hallett Dale 之女——翁婿二人先后出任皇家学会会长。育一子二女：Alexander Henry（1939）、Helen Jean（1941）、Hilary Alison（1946）
- **教育轨迹**：
  - Allan Glen's School（格拉斯哥）
  - University of Glasgow，1928 年 BSc
  - Goethe University Frankfurt，1931 年 Dr Phil.nat.（胆汁酸化学论文）
  - 1851 Research Fellowship 资助下赴 Oriel College, Oxford，1933 年 DPhil
- **导师**：Walther Borsche（法兰克福博士导师）、Robert Robinson（牛津博士导师）——infobox 双载
- **博士**：1931 法兰克福（胆汁酸）；1933 牛津 DPhil
- **研究领域**：核苷酸、核苷与核苷酸辅酶的结构与合成；生物碱、花青素、维生素

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **格拉斯哥职员之子（1907）**：Cathcart 出身，Allan Glen's School 起步——非学术世家的奋斗路径。
2. **欧陆双博士（1931/1933）**：法兰克福胆汁酸化学（Borsche）→ 牛津 DPhil（Robinson），横跨德英两派有机化学传统。
3. **早期职位（1934–1938）**：Lister Institute → 爱丁堡大学（1934–1936）→ 伦敦大学生物化学 Reader。
4. **加州理工半年（1938）**：访问教授，婉拒教职offer——随即回国接任曼彻斯特 Sir Samuel Hall 讲席教授兼化学实验室主任。
5. **最年轻教授（1938）**：31 岁出任曼彻斯特化学讲席，"Frankland 以来最年轻的化学教授"；同年入选 Manchester Literary and Philosophical Society；在此开启核苷（nucleosides）研究——DNA/RNA 结构单元。
6. **剑桥 1702 讲席（1944）**：任 BP 有机化学教授直至 1971 年退休；同年当选 Christ's College, Cambridge Fellow。
7. **ATP 与 FAD 合成（1949）**：合成腺苷三磷酸（ATP）与黄素腺嘌呤二核苷酸（FAD）——能量货币与辅酶的人工合成里程碑。
8. **DNA 骨架（1951）**：与剑桥合作者以生化方法确定 DNA 主链由糖的 3 位与 5 位碳原子经磷酸逐级连接——为 Crick/Watson 1953 年 X 射线结构工作提供了佐证。
9. **维生素 B12（1955）**：参与阐明维生素 B12 结构（最终结构与分子式由 Dorothy Hodgkin 及其团队确定）；此后研究维生素 B1、维生素 E、花青素（花果色素）与昆虫来源生物碱，并研究大麻中的生物碱——1940 年即以氢化法首次合成 H4-CBD 与 H2-CBD。
10. **1957 诺贝尔化学奖**：官方理由 "for his work on nucleotides and nucleotide co-enzymes."（核苷酸与核苷酸辅酶）。
11. **政府科学政策（1952–1964）**：出任英国政府科学政策咨询委员会主席——科学家参政的典范。
12. **学术领袖（1963–1980）**：Christ's College Master（1963–1978）；Strathclyde 大学首任 Chancellor（1965）；皇家学会会长（1975–1980）；1977 年获女王颁 Order of Merit；1981 年为 World Cultural Council 创始成员。
13. **贵族学者**：1954 年受封爵士，1962-04-16 册封终身贵族 Baron Todd of Trumpington；40 余个荣誉学位；剑桥化学系有其皇家化学会蓝牌纪念。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海青 deepteal） | `#0E4D64` | 核苷酸化学的精密与纵深（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（核苷酸化学 badgeNucl） | `#1E5A8A` | 蓝核苷/核苷酸结构 |
| 分类色 2（辅酶合成 badgeCoEnz） | `#1B7A43` | 绿 ATP / FAD 合成 |
| 分类色 3（维生素与天然产物 badgeNatProd） | `#D97B29` | 琥珀 B12 / B1 / E、花青素 |
| 分类色 4（公共服务与学术领袖 badgeStates） | `#8E44AD` | 紫皇家学会会长 / 科学政策 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「核苷酸单元逐级连接」的链式排列。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Really Slow Motion & Giant Apes（Epic Beautiful Uplifting；文件路径见 manifest `music_audio/inspiring-electronic/15-w6kT1BfvETI-...`；**不要复制 wav 文件**）
- **风格**：恢弘 / 明亮 / 上扬的史诗感
- **匹配理由**：
  - "光明上扬" 匹配托德的双重身份——实验室里的核苷酸建造者 + 白厅的科学政策掌舵人
  - "史诗感" 匹配其地位轨迹——从格拉斯哥地铁职员之子到皇家学会会长、终身贵族
  - "美丽昂扬" 匹配 ATP/FAD 合成的开创性时刻与 1957 诺奖的加冕
- **时长**：以实际文件为准 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 核苷酸的建造者 / Alexander R. Todd 1907–1997 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/双博士/师承/出生地/去世地/领域/荣誉）
03  托德的一生 — Sanger 式时间线（10 节点：1907→1928→1931→1933→1938→1944→1949→1957→1962→1975）
04  格拉斯哥到欧陆（1907–1933）— 表格「时间|事件|结果」（Allan Glen's → Glasgow → Frankfurt → Oxford）
05  曼彻斯特：核苷研究的起点（1938）— 表格「职位|课题|意义」+ 最年轻教授
06  ATP 与 FAD 的合成 (1949) — 表格「目标|方法|结果」+ 公式框：ATP / FAD 结构示意
07  DNA 骨架与维生素 B12 (1951/1955) — 表格「问题|方法|结果」+ 公式框：3′-5′ 磷酸二酯键骨架
08  1957 诺贝尔化学奖 — 表格「领域|贡献|认可」+ 公式框：官方获奖理由原文
09  维生素与天然产物 (1940s–1950s) — 表格「对象|方向|结果」（B1/E、花青素、大麻生物碱、1940 H4-CBD/H2-CBD 首次合成）
10  科学政策与学术领袖 (1952–1980) — 表格「机构|职务|年份」（咨询委员会主席/Christ's Master/Strathclyde Chancellor/皇家学会会长）
11  荣誉与贵族 — Sanger 式「类别|代表|意义」表格（含 itemize 荣誉清单）+ 爵士→终身贵族
12  家族与 Dale 联姻 — 表格「人物|关系|注」（妻 Alison Sarah Dale、岳父 Henry Hallett Dale、翁婿两代皇家学会会长）
13  遗产：核苷酸化学的奠基 — 四分类遗产盒 + 公式框：从核苷酸到分子生物学的桥梁
14  结尾 — 「他把生命的能量货币，先一步造了出来。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1957 诺奖 | **独享**，官方理由 "for his work on nucleotides and nucleotide co-enzymes."——勿写成"核酸结构"或"DNA 双螺旋" |
| 双博士 | 法兰克福 1931（Dr Phil.nat.，胆汁酸）+ 牛津 1933（DPhil）——勿只写一个 |
| 双博士导师 | infobox 明载 Walther Borsche（法兰克福）与 Sir Robert Robinson（牛津）两位——勿漏 Borsche |
| 出生地/去世地 | 生于 Cathcart（格拉斯哥近郊）；卒于 1997-01-10，infobox 作 Oakington（剑桥郡村）、正文作 Cambridge——两处口径并注，勿混写 |
| B12 分工 | 托德只是"帮助阐明"结构；**最终结构与分子式由 Dorothy Hodgkin 团队确定**——勿写托德"测定了 B12 结构" |
| DNA 骨架 | 1951 年确定的是 3′/5′ 碳—磷酸连接的**生化证据**，佐证 1953 Crick/Watson 的 X 射线结构——勿写托德"参与发现双螺旋" |
| CBD 合成 | 1940 年首次合成 H4-CBD/H2-CBD 是 page.md 实载，可客观写为天然产物化学工作；勿渲染成大麻应用 |
| 大麻研究 | "studied alkaloids found in cannabis" 为实载研究内容——措辞保持中性学术口径 |
| 头衔顺序 | 1954 爵士 → 1962-04-16 终身贵族 Baron Todd of Trumpington → 1977 OM——勿倒置；勿写"世袭贵族" |
| 皇家学会会长 | 1975–1980；岳父 Henry Hallett Dale 亦任过会长——"翁婿两代会长"须各归各人，勿混 |
| 最年轻教授 | 31 岁、曼彻斯特、"Frankland 以来最年轻"——勿泛化为"史上最年轻" |
| 女儿姓名 | Alexander Henry（1939）/ Helen Jean（1941）/ Hilary Alison（1946）——勿编造 |
| 引语 | page.md 正文无直接引语——全文禁用引号"原话"，一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q157242 | ✅ |
| name_zh | 亚历山大·R·托德 | ✅ |
| name_en | Alexander R. Todd | ✅ |
| birth_date | 1907-10-02 | ✅ |
| death_date | 1997-01-10 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | organic chemistry（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（立传 Beamer 完成后置 1） | ✅ |

**person_field 细分 rank 表**：

| name_en | rank | name_zh | 依据 |
|---|---|---|---|
| nucleotide chemistry | 0 | 核苷酸化学 | 1957 诺奖理由 |
| nucleosides | 1 | 核苷 | 曼彻斯特起步课题 |
| coenzyme synthesis | 2 | 辅酶合成 | ATP/FAD 1949 |
| natural products chemistry | 3 | 天然产物化学 | 维生素/花青素/生物碱 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Walther Borsche | 师→生（法兰克福博士导师） | 1931 胆汁酸化学博士 |
| advisor-student | Robert Robinson | 师→生（牛津博士导师） | 1933 DPhil（Oriel College） |
| advisor-student | J. Rodney Quayle | Todd → 学生 | infobox Doctoral students 唯一载者 |
| colleague | Dorothy Hodgkin | 无向 | 1955 合作阐明维生素 B12 结构（最终结构由 Hodgkin 团队确定） |
| spouse | Alison Sarah Dale | 无向 | 1937 结婚；Henry Hallett Dale 之女；1987 卒 |
| other | Henry Hallett Dale | 无向 | 岳父；翁婿二人先后任皇家学会会长 |

> **禁入库名单（metadata.json-only 或非人际学术关系）**：Francis Crick / James Watson（正文仅为"研究佐证"学术关联，非直接合作人际）、Joel Hildebrand（无）、Atherton–Todd 反应（See also 条目，对手方 Atherton 无人际叙述）。政府对内职务（科学政策委员会）非人际不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1957，独享；"for his work on nucleotides and nucleotide co-enzymes."）
- Tilden Prize（1940）；Meldola Medal and Prize
- Fellow of the Royal Society，FRS（1942）
- Davy Medal（1949）；Royal Medal（1955）
- Knight Bachelor（1954，Sir Alexander Todd）
- 美国国家科学院外籍/院士（1955）；American Academy of Arts and Sciences（1957）；American Philosophical Society（1965）
- Life Peer — Baron Todd of Trumpington（1962-04-16）
- Paul Karrer Gold Medal（1963）
- Copley Medal（1970）；Lomonosov Gold Medal（1978）
- Order of Merit，OM（1977）
- Pour le Mérite for Sciences and Arts；Royal Society Bakerian Medal；Longstaff Prize；Robert Robinson Award；Lavoisier Medal
- 40 余个荣誉博士学位（马德里康普顿斯、斯特拉斯堡、巴黎、香港大学、香港中文、Leicester、Kiel、Yale、Sheffield、Exeter 等）

## 9. 机构清单

- 教育：Allan Glen's School；University of Glasgow（BSc 1928）；Goethe University Frankfurt（Dr Phil.nat. 1931）；Oriel College, Oxford（DPhil 1933）
- 任职：Lister Institute；University of Edinburgh（1934–1936）；University of London（生物化学 Reader）；California Institute of Technology（1938 访问教授）；University of Manchester（1938 Sir Samuel Hall 讲席教授兼化学实验室主任）；University of Cambridge（1944–1971，1702 讲席/BP 有机化学教授）；Christ's College, Cambridge（1944 Fellow，1963–1978 Master）；University of Strathclyde（1965 首任 Chancellor）；Hatfield Polytechnic（1978–1986 访问教授）
- 公职：英国政府科学政策咨询委员会主席（1952–1964）；皇家学会会长（1975–1980）；World Cultural Council 创始成员（1981）
- 纪念：剑桥大学化学系皇家化学会蓝牌

## 10. 终审清单

- [ ] 生卒 1907-10-02 / 1997-01-10，享年 89，出生地 Cathcart、去世地口径两注（Oakington/Cambridge）
- [ ] 1957 **独享**，官方理由原文 "for his work on nucleotides and nucleotide co-enzymes."
- [ ] 双博士（1931 法兰克福 / 1933 牛津）与双导师（Borsche / Robinson）表述完整
- [ ] B12 归属 Hodgkin 团队、DNA 骨架为佐证性贡献——分工勿混淆
- [ ] 头衔时间序：1954 爵士 → 1962 终身贵族 → 1977 OM；皇家学会会长 1975–1980
- [ ] 全文无杜撰引语（page.md 无直接引语，一律间接转述）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Alexander_R._Todd/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：核对 images/（1957 年照；无则装饰圆占位并注明）
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：全文无引号"原话"（仅允许诺奖理由英文原文一处）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger/van 't Hoff 等）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动该脚本。
