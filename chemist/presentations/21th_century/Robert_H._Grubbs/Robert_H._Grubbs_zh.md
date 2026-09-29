# Robert H. Grubbs（罗伯特·格拉布斯）立传提示词

> qid=Q202140 · 1942-02-27（肯塔基州 Marshall County）– 2021-12-19（加州 Duarte，享年 79）· 美国化学家 · 21 世纪 · 诺贝尔化学奖（2005，与 Yves Chauvin / Richard R. Schrock 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Robert_H._Grubbs/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金边公式框，是本次执行的版式语言。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注；肖像优先取本地 `images.txt`（2018 年 Grubbs 照或 AIC Gold Medal 2010 照），404 则装饰圆占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 让分子交换舞伴的催化剂大师\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Robert Howard Grubbs）、国籍、出生地/去世地、教育、博士、导师、核心领域、荣誉。事实取自本地 infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「环化复分解成环」母题——圆点连线成环再断开重连。
5. **表格语义化 + 公式框**（★ 每个核心贡献页必须使用）：`tabularx` 三列表格（表头主色白字、第一列强调色加粗、三列语义化如 问题 | 催化剂 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式框画 Ru=CH–R 卡宾结构与第一代催化剂式 (PCy₃)₂Cl₂Ru=CHCH=CPh₂。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Robert Howard Grubbs（中文惯称：罗伯特·格拉布斯；ForMemRS）
- **生卒**：1942-02-27 生于肯塔基州 Marshall County 农场（Possum Trot 与 Calvert City 之间）→ 2021-12-19 逝于加州 Duarte 的 City of Hope 癌症中心（心脏病发作，时正在治疗淋巴瘤），享年 79
- **国籍**：United States（美国）
- **身份**：化学家；Caltech Victor and Elizabeth Atkins 化学讲席教授（1990 起）；Materia 公司共同创办人
- **家庭**：父 Howard（二战后受训为柴油机修理工）、母 Faye（娘家姓 Atwood，学校教师）；战后全家迁 Paducah，就读 Paducah Tilghman High School；在哥伦比亚大学结识未来妻子 Helen O'Kane（特殊教育教师），育三子女：Barney（1972）、Brendan H.（1974）、Kathleen/Katy（1977）
- **教育轨迹**：
  - University of Florida：本想读农业化学，被 Merle A. Battiste 劝转有机化学；BS 1963、MS 1965
  - Columbia University：与 Ronald Breslow 研究含碳–金属键的有机金属化合物，PhD 1968（论文 *I. Cyclobutadiene Derivatives II. Studies of Cyclooctatetraene Iron Tricarbonyl Complexes*）
- **导师**：Ronald Breslow（博士导师）；博士后 1968–1969 在 Stanford 与 James Collman 合作（NIH fellow）
- **研究领域**：有机金属化学、合成化学——烯烃复分解催化剂（RCM 环化复分解、CMR 交叉复分解、ROMP 开环复分解聚合）、活性聚合（living polymerization）、绿色化学催化

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **肯塔基农场（1942）**：生在 Possum Trot 与 Calvert City 之间的农场——乡村孩子的催化剂帝国从这台"农具哲学"起步。
2. **佛罗里达转向（1960s）**：本读农业化学，被 Merle A. Battiste 劝转有机化学——"化学反应如何发生"从此成为一生问题。
3. **哥伦比亚博士（1968）**：随 Ronald Breslow 做有机金属化合物——环丁二烯衍生物与环辛四烯铁三羰基配合物。
4. **斯坦福博士后（1968–1969）**：与 James Collman 系统考察有机金属化学中的催化过程——当时还是相对崭新的领域。
5. **密歇根州立起步（1969–1978）**：助理教授（1969–1973）、副教授（1973–1978）；MSU 早期前辈（Harold Hart、Karabatsos、LeGoff、Farnum、Reusch、Wagner）是他的引路人；1974–1976 Sloan Fellowship。
6. ** Mülheim 访学（1975）**：洪堡奖学金赴 Max-Planck-Institut für Kohlenforschung——德国煤炭化学重镇。
7. **Caltech 岁月（1978–）**：1978 任化学教授，1990 起 Victor and Elizabeth Atkins 讲席教授——烯烃复分解的主战场。
8. **1992 里程碑**：组里用 RuCl₃/OsCl₃/钨亚烷基成功聚合 7-oxo 降冰片烯衍生物后，鉴定出 Ru(II) 卡宾是有效金属中心，发表首个结构明确的钌基复分解催化剂 (PPh₃)₂Cl₂Ru=CHCH=CPh₂。
9. **第一代商品化（1995）**：三环己基膦配合物 (PCy₃)₂Cl₂Ru=CHCH=CPh₂ 同样活泼——1995 年成为商品化的第一代 Grubbs 催化剂；第二代亦相继开发。
10. **钌的哲学**：钌在空气中稳定、选择性更高、反应性低于此前最有前景的钼——并以绿色化学思路减少危废；Grubbs 催化剂成为普通实验室复分解的标准工具。
11. **Materia 创业（1998）**：与 Mike Giardello 在 Pasadena 共同创办 Materia；Sigma-Aldrich 成为全球独家经销商；2008 与 Cargill 合组 Elevance；2017 催化剂业务售予 Umicore；2021 Materia 被 ExxonMobil 收购。
12. **2005 诺贝尔化学奖**：与 Richard R. Schrock、Yves Chauvin 共享——表彰其在烯烃复分解领域的工作；2015 因"促成商业产品的催化剂进展"当选美国工程院院士。
13. **学术影响**：2021 年 h-index 160（Google Scholar）/137（Scopus）；徒弟满门——博士生 SonBinh Nguyen、Melanie Sanford、Timothy M. Swager，博士后含 Buchwald、Sukbok Chang、Coates、Gregory Fu、Toste、Dong 等。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深祖母绿 deepemerald） | `#0B5351` | 钌催化的沉稳与工业感（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（钌催化剂 badgeRu） | `#1B7A43` | 绿 Ru 卡宾 / 第一二代催化剂 |
| 分类色 2（复分解反应 badgeMeta） | `#2E5A9E` | 蓝 RCM / ROMP / 交叉复分解 |
| 分类色 3（绿色化学 badgeGreen） | `#D97B29` | 琥珀低能耗 / 低危废 |
| 分类色 4（创业转化 badgeMateria） | `#C0395B` | 玫瑰 Materia / Sigma-Aldrich |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（成对圆点断开重连），呼应「复分解交换」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`；**不要复制 wav 文件**，Makefile 按此绝对路径引用）
- **风格**：恢弘 / 长线叙事 / 传承感
- **匹配理由**：
  - 恢弘长线匹配从肯塔基农场到 Caltech 讲席教授的六十年跨度
  - 传承感匹配满门弟子与第一二代催化剂的接力（1992→1995→二代）
  - "Eternals"（恒久）呼应 Grubbs 催化剂至今仍是全世界实验室的标准工具
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 让分子交换舞伴的催化剂大师 / Robert H. Grubbs 1942–2021 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/导师/出生地/去世地/领域/荣誉）
03  格拉布斯的一生 — Sanger 式时间线（10 节点：1942→1963→1965→1968→1969→1978→1992→1995→2005→2021）
04  早年：肯塔基农场 (1942–1963) — 表格「时间|事件|结果」
05  佛罗里达与哥伦比亚 (1963–1968) — 表格「时间|事件|结果」
06  斯坦福与密歇根州立 (1968–1978) — 表格「阶段|合作者|收获」
07  Caltech 与钌转向 (1978–1992) — 表格「问题|方法|结果」
08  1992 里程碑 — 表格「体系|催化剂|意义」+ 公式框：(PPh3)2Cl2Ru=CHCH=CPh2 首个结构明确钌催化剂
09  第一代商品化 (1995) 与钌的哲学 — 表格「对比项|钌|钼」+ 公式框：(PCy3)2Cl2Ru=CHCH=CPh2 · 空气稳定/高选择性
10  RCM / ROMP / 活性聚合 — 表格「反应|特点|应用」
11  Materia 创业与产业转化 — Sanger FFT 页式流程图（1998 创办 → Sigma-Aldrich → 2008 Elevance → 2017 Umicore → 2021 ExxonMobil）
12  2005 诺贝尔化学奖 — 表格「人物|金属|贡献」（Chauvin 机理 / Schrock Mo / Grubbs Ru）
13  满门弟子与学术影响 — 表格「人物|方向|后续」+ h-index 160/137
14  结尾 — 「一个好的催化剂，让化学家少走一步，让世界少冒一缕烟。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 官方获奖理由 | **page.md 未载 2005 官方 citation 整句**——按页面口径写"因其烯烃复分解领域工作共享 2005 诺奖"（intro 原句 "for his work on olefin metathesis"），勿杜撰整句 citation |
| 三人分工 | Chauvin = 机理奠基（1970s 初）；Schrock = 钼/钨催化剂；Grubbs = 钌催化剂——勿混 |
| 死因口径 | 2021-12-19 在 Duarte 的 City of Hope **心脏病发作**去世，**当时正在接受淋巴瘤治疗**——勿写"死于淋巴瘤" |
| 1992 vs 1995 | 1992 = 首个结构明确钌基催化剂 (PPh₃)₂Cl₂Ru=…；1995 = 第一代商品化 (PCy₃)₂Cl₂Ru=…；二代"亦相继开发"页面未载年份——勿写 1995 二代 |
| 钌 vs 钼 | 钌空气稳定、选择性更高、反应性更低——是相对优势表述，勿写成"钼无用" |
| 出生地 | 农场在 Marshall County（Possum Trot 与 Calvert City 之间）；metadata place_of_birth 作 "Possum Trot"——正文口径 Marshall County |
| Oren Scherman | metadata doctoral_student 含 Oren Scherman，但页面 infobox Doctoral students 无——**禁入库** |
| MSU 早期前辈 | Harold Hart 等六人页面作 "early mentors"，语义模糊（前辈同事而非导师）——**禁入库**，正文可提"MSU 早期前辈" |
| Tetrahedron Prize | 2003 年与 Dieter Seebach **共享**——勿写独享 |
| h-index | 160（Google Scholar）/137（Scopus）须注"截至 2021" |
| CMR 术语 | 页面作 cross-metathesis reaction（CMR）——沿用页面缩写，勿擅改 CM |
| 引语 | 正文无带引号直接引语——一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q202140 | ✅ |
| name_zh | 罗伯特·格拉布斯 | ✅ |
| name_en | Robert H. Grubbs | ✅（新建记录，库内无同名） |
| birth_date | 1942-02-27 | ✅ |
| death_date | 2021-12-19 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry / chemistry（metadata 口径）；person_field 细分见下 | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

person_field 细分（rank 表）：

| rank | field | 说明 |
|---|---|---|
| 0 | olefin metathesis | 2005 诺奖工作：钌催化剂 |
| 1 | organometallic chemistry | 碳–金属键一生主业 |
| 2 | polymer chemistry | ROMP / 活性聚合 |
| 3 | green chemistry | 低危废催化理念 |

## 7. 社会关系入库清单

**师长 / 引路人 / 配偶**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ronald Breslow | 师→生（博士导师） | 哥伦比亚大学博士导师，1968 |
| advisor-student | James Collman | 师→生（博士后导师） | 斯坦福 NIH 博士后 1968–1969 |
| influence | Merle A. Battiste | 无向 | 佛罗里达本科导师，劝其从农业化学转向有机化学 |
| spouse | Helen O'Kane | 无向 | 妻子，特殊教育教师，育三子女 |

**共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Yves Chauvin | 无向 | 2005 诺贝尔化学奖共同得主 |
| co-honored | Richard R. Schrock | 无向 | 2005 诺贝尔化学奖共同得主 |
| co-honored | Dieter Seebach | 无向 | 2003 Tetrahedron Prize 共享 |

**门生（infobox Doctoral students 三人 + Post-docs 八人，均明载）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | SonBinh Nguyen | Grubbs → 学生（博士） | infobox 博士生 |
| advisor-student | Melanie Sanford | Grubbs → 学生（博士） | infobox 博士生 |
| advisor-student | Timothy M. Swager | Grubbs → 学生（博士） | infobox 博士生 |
| advisor-student | Steven Buchwald | Grubbs → 学生（博士后） | infobox Post-docs |
| advisor-student | Sukbok Chang | Grubbs → 学生（博士后） | infobox Post-docs |
| advisor-student | Geoffrey W. Coates | Grubbs → 学生（博士后） | infobox Post-docs |
| advisor-student | Gregory Fu | Grubbs → 学生（博士后） | infobox Post-docs |
| advisor-student | Jennifer Love | Grubbs → 学生（博士后） | infobox Post-docs |
| advisor-student | Adam Matzger | Grubbs → 学生（博士后） | infobox Post-docs |
| advisor-student | Dean Toste | Grubbs → 学生（博士后） | infobox Post-docs |
| advisor-student | Guangbin Dong | Grubbs → 学生（博士后） | infobox Post-docs |

> **禁入库名单**：Oren Scherman（metadata-only）、Harold Hart / Gerasimos J. Karabatsos / Gene LeGoff / Don Farnum / Bill Reusch / Pete Wagner（MSU 早期前辈，语义模糊）、Mike Giardello（Materia 共同创办人，商业伙伴非学术关系）。

## 8. 奖项清单

- 1989 National Academy of Sciences 院士；1994 American Academy of Arts and Sciences
- 2000 Benjamin Franklin Medal（Franklin Institute）；2000 ACS Herman F. Mark 聚合物化学奖
- 2001 ACS Herbert C. Brown 奖；2002 Tolman Medal；2002 Arthur C. Cope Award
- 2003 Tetrahedron Prize（与 Dieter Seebach 共享）；2005 Paul Karrer Gold Medal；2005 RSC Honorary Fellow
- 2005 Nobel Prize in Chemistry（与 Schrock/Chauvin 共享）；2006 Golden Plate Award
- 2009 ACS Fellow；2010 American Institute of Chemists Gold Medal；2013 National Academy of Inventors
- 2015 Florida Inventors Hall of Fame；2015 National Academy of Engineering；2015 中国科学院外籍院士
- 2017 Ira Remsen Award；2017 Foreign Member of the Royal Society（ForMemRS）
- 另有.metadata 列出的 Humboldt Prize、Prelog Medal、Centenary Prize、Linus Pauling Award、Roger Adams Award 等（年份页面无载者勿写年份）

## 9. 机构清单

- 教育：Paducah Tilghman High School；University of Florida（BS 1963、MS 1965）；Columbia University（PhD 1968）
- 任职：Stanford University（博士后 1968–1969，与 Collman）；Michigan State University（1969–1978，助理→副教授；Sloan Fellow 1974–1976；Mülheim 煤炭研究所访学 1975）；California Institute of Technology（1978–，1990 起 Victor and Elizabeth Atkins 讲席教授）
- 产业：Materia（1998 与 Mike Giardello 共同创办，Pasadena；2017 催化剂业务售 Umicore、2021 公司售 ExxonMobil）；Elevance Renewable Sciences（2008 与 Cargill 合组）；Reliance Innovation Council 成员

## 10. 终审清单

- [x] 2005 三人共享 + 三人分工表述准确；citation 整句页面无载未杜撰
- [x] 死因"心脏病发作、时在淋巴瘤治疗中"口径准确
- [x] 1992 首例结构明确钌催化剂 / 1995 第一代商品化年份准确
- [x] 钌–钼对比是相对优势表述
- [x] 博士生 3 + 博士后 8 全部为 infobox 明载；Oren Scherman 与 MSU 六前辈禁入库已注
- [x] Tetrahedron Prize 2003 共享表述准确；h-index 注明截至 2021
- [x] 品牌 OpenMathAI、半角引号、封面国籍行、身份信息页齐备
- [x] `make distclean && make` 0 错误（Beamer 执行时验证）

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Robert_H._Grubbs/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 已就位（真实肖像或装饰圆占位，图注如实）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：全篇无引号原话；间接转述均可溯源
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；化学式（Ru 卡宾）排版正常
- [ ] 与 21 世纪批次其他篇格式对齐
