# Herbert C. Brown（赫伯特·C·布朗）立传提示词

> qid=Q102406 · 1912-05-22 – 2004-12-19 · 美国化学家（生于英国伦敦） · 20 世纪 · 诺贝尔化学奖（1979，与 Georg Wittig 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Herbert_C._Brown/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传模板**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 内若缺，先按常规流程下载 Wikipedia 肖像，404 则装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 硼化学的一生\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。国籍口径：生于伦敦、1914 年迁美、1936 年入籍美国，封面主徽章用 **美国**。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Herbert Brovarnik）、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「硼氢键 / 三中心两电子」母题——成对圆点暗示硼氢桥键的几何。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 NaBH₄ 合成路线、硼氢化-氧化反应式。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Herbert Charles Brown（中文惯称：赫伯特·C·布朗；本名 Herbert Brovarnik）
- **生卒**：1912-05-22 生于英国伦敦 → 2004-12-19 逝于美国印第安纳州 Lafayette 的医院（心脏病发作），享年 92
- **国籍**：出生英国，1914 年（2 岁）随家迁芝加哥，1936 年入籍美国（nationality：United Kingdom / United States）
- **身份**：化学家（chemist；1979 诺贝尔化学奖得主）
- **家庭**：父母为来自乌克兰 Zhitomir 的犹太移民——母 Pearl（娘家姓 Gorinstein）、父 Charles Brovarnik（五金店经理兼木匠）；妻 Sarah Baylen（1937-02-06 结婚，2005-05-29 逝，享年 89；育有一子）
- **教育轨迹**：
  - Crane Junior College（芝加哥，在此结识 Sarah Baylen；因学院面临关闭）
  - → Wright Junior College 转学
  - 1935 秋入 University of Chicago，用三个季度修完两年课程，1936 获 B.S.
  - 同年（1936）入籍美国，并开始在芝加哥读研究生
- **导师**：Hermann Irving Schlesinger（博士导师；其芝加哥实验室是当时全世界仅有的两个制备乙硼烷的实验室之一）
- **博士**：1938 获 PhD（论文 1939 年发表，研究乙硼烷 B₂H₆ 的反应）
- **研究领域**：有机化学——有机硼化学、硼氢化反应、还原剂谱系、不对称合成
- **命名妙笔**：姓名首字母 H、C、B 恰是氢、碳、硼——他的整个工作领域

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **移民之子（1912）**：伦敦出生的乌克兰犹太移民之子，2 岁迁芝加哥——底层家庭走出的化学家。
2. **太太的红娘戏（1937）**：在 Crane Junior College 结识 Sarah Baylen 并于 1937-02-06 结婚；布朗后来把对硼氢化物的兴趣归功于妻子——这份兴趣最终通向 1979 年诺贝尔奖。
3. **芝加哥速成（1935–1938）**：三个季度修完两年本科；博士阶段研究乙硼烷 B₂H₆——Schlesinger 实验室是全球仅有的两个能制备乙硼烷的实验室之一。
4. **冷板凳论文（1939）**：发现乙硼烷与醛酮反应生成二烷氧基硼烷、水解得醇——当时有机化学家没有温和条件下还原羰基的好方法；但 1939 年博士论文发表后少人问津，因为乙硼烷太稀有、做不成通用试剂。
5. **战时转折（1940–1943）**：为国防研究委员会（NDRC）研究挥发性铀化合物，与 Schlesinger 合成挥发性硼氢化铀(IV)；为解决乙硼烷短缺，用氢化锂 + 三氟化硼（乙醚中）大量制备乙硼烷；再改用氢化钠 + 硼酸甲酯路线。
6. **硼氢化钠问世**：250° 下硼酸甲酯与氢化钠反应得硼氢化钠与甲醇钠；用丙酮分离产物时意外发现 NaBH₄ 能还原丙酮——温和还原剂就此登场（醛、酮、酰氯）；与强力的 LiAlH₄ 构成还原剂光谱两极。
7. **普渡岁月（1947–1978）**：1947 任普渡大学无机化学教授；到普渡后寻找"更强的硼氢化物 + 更温和的铝氢化物"——换金属离子（Li/Mg/Al）增强还原能力、给铝氢化物引入烷氧基减弱还原能力，建成完整的还原剂谱系。
8. **硼氢化-氧化反应**：同事 B. C. Subba Rao 博士发现硼氢化钠与油酸乙酯的异常反应——氢与硼加到碳碳双键上，有机硼产物氧化后成醇；这就是硼氢化-氧化反应：把烯烃变成**反马氏**醇（与 Markovnikov 规则方向相反）。
9. **不对称合成之父**：其工作导出第一个生产不对称纯对映异构体的一般方法。
10. **1979 诺贝尔化学奖**：与 Georg Wittig 共享；引言口径 "for his work with organoboranes"（布朗=硼，维蒂希=磷，官方 citation 见 §5）。
11. **实验室留名**：普渡校园的 Herbert C. Brown Laboratory of Chemistry 以他命名；1960 加入 Alpha Chi Sigma Beta Nu 分会，2000 入选其名人堂。
12. **斯德哥尔摩的分工**：布朗常说获奖后在斯德哥尔摩，他捧奖章、妻子捧 10 万美元奖金——归功于 Sarah 承揽了财务与家务。
13. **谢幕（2004）**：1978 起荣休教授直至 2004-12-19 因心脏病在 Lafayette 医院去世；妻 Sarah 次年（2005-05-29）去世。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 deepviolet） | `#46356B` | 硼氢化物化学的深邃与严谨（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（硼氢化钠 badgeBH） | `#2E5A9E` | 蓝 NaBH₄ / 温和还原 |
| 分类色 2（乙硼烷 badgeDib） | `#8C4A2E` | 赭 B₂H₆ / 三中心两电子键 |
| 分类色 3（硼氢化-氧化 badgeHyb） | `#1B7A43` | 绿 anti-Markovnikov 加成 |
| 分类色 4（不对称合成 badgeAsym） | `#C0395B` | 玫瑰对映异构体 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「三中心两电子桥键」的成对圆点几何。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions（文件 `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`，不复制 wav）
- **风格**：怀旧 / 沉思 / 回望来时路
- **匹配理由**：
  - "怀旧" 匹配其人生轨迹——伦敦出生、芝加哥底层、一战移民家庭，一生回望硼化学的原点
  - "沉思" 匹配其科研气质——从冷板凳的 1939 博士论文到普渡还原剂谱系，是数十年如一日的深耕
  - "回望" 匹配 H·C·B 三个首字母即是氢碳硼的一生隐喻
- **时长**：以实际曲目时长为准，超过 15 页 × 7 秒由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 硼化学的一生 / Herbert C. Brown 1912–2004 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  布朗的一生 — 时间线（10 节点：1912→1914→1936→1937→1938→1940→1947→1969→1979→2004）
04  早年：移民之子 (1912–1935) — 表格「时间|事件|结果」
05  芝加哥：从 B.S. 到乙硼烷 (1935–1939) — 表格「问题|方法|结果」+ 公式框：B₂H₆ ⇌ 2BH₃（三中心两电子键）
06  战时：硼氢化钠的诞生 (1940–1945) — 表格「需求|路线|产物」+ 公式框：NaBH₄ 合成路线
07  普渡：还原剂谱系 (1947–1960) — 表格「问题|方法|结果」+ 公式框：还原剂光谱（NaBH₄ ↔ LiAlH₄）
08  硼氢化-氧化反应 — 表格「发现|机理|意义」+ 公式框：anti-Markovnikov 加成
09  1979 诺贝尔化学奖 — 表格「人物|元素|贡献」+ 公式框：布朗=硼、维蒂希=磷
10  家庭与夫人 Sarah — 表格「人物|角色|结果」（红娘/财务后勤/斯德哥尔摩分工）
11  荣誉清单 — 「类别|代表|意义」表格（含 itemize 荣誉清单）
12  普渡传承 — 流程图页（Brown Lab 命名 → Alpha Chi Sigma 名人堂 → 荣休 → 遗产）
13  遗产：硼化学改变有机合成 — 四分类遗产盒 + 公式框：H·C·B = H·C·B
14  结尾 — 「从乙硼烷到不对称合成，他把硼写进了有机化学的字母表。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1979 诺奖口径 | 页面引言作 "for his work with organoboranes"；官方 citation 为 "for their development of the use of boron- and phosphorus-containing compounds, respectively, into important reagents in organic synthesis"（见 Wittig 篇外链标题）——布朗对应硼、维蒂希对应磷，**共享**勿写独享 |
| 本名 | 出生名 **Herbert Brovarnik**（乌克兰犹太移民之子），勿漏写 |
| 国籍 | 生于伦敦（英国），1914 迁美、1936 入籍——勿只写 American 而抹掉出生国 |
| PhD 年份 | 1938 获学位（"the following year received his degree"），**论文 1939 年发表**——两个年份勿混 |
| NaBH₄ 发现语境 | 战时（NDRC 铀化合物研究）副产物 + Schlesinger 合作——勿写"独立发明还原剂" |
| 硼氢化-氧化发现人 | 异常反应是**同事 B. C. Subba Rao** 发现，布朗发展成通用方法——勿写布朗一人独立发现 |
| 反马氏规则 | 硼氢化-氧化中 OH 加到**取代较少**的碳（与 Markovnikov 规则方向相反）——方向勿写反 |
| 太太角色 | 布朗自述对硼氢化物的兴趣归功于 Sarah；斯德哥尔摩"他捧奖章她捧奖金"是布朗本人说法——转述勿编成她的原话 |
| frontmatter 噪声 | metadata 有 "university teacher / writer" 等职业，主职业以 chemist 为准；Wilbur Wright College 在 frontmatter 作 Malcolm X College 的现名，正文用 Wright Junior College |
| 同名区分 | 与 "Brown 运动"（Robert Brown）无关；亦勿与 Herbert A. Simon 等混淆 |
| 荣誉年份 | Centenary Prize 1955、Nichols 1959、National Medal of Science 1969、Elliott Cresson 1978、Priestley 1981、Perkin 1982、AIC Gold 1985、NAS Award 1987——年份照 infobox，勿倒置 |
| 配偶卒日 | Sarah 2005-05-29 逝、享年 89——勿写进布朗生卒行 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102406 | ✅ |
| name_zh | 赫伯特·C·布朗 | ✅ |
| name_en | Herbert C. Brown | ✅ |
| birth_date | 1912-05-22 | ✅ |
| death_date | 2004-12-19 | ✅ |
| nationality | United Kingdom / United States（双条带 rank，era_note 注明迁美与入籍） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：organoborane chemistry / hydroboration / asymmetric synthesis / reducing agents，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hermann Irving Schlesinger | 师→生（博士导师） | 芝加哥大学硼烷实验室，全球仅有的两个乙硼烷制备地之一 |
| colleague | B. C. Subba Rao | 无向 | 普渡同事，发现硼氢化钠与油酸乙酯的异常反应，导向硼氢化-氧化 |
| co-honored | Georg Wittig | 无向 | 1979 诺贝尔化学奖共同得主（布朗=硼、维蒂希=磷） |

**家庭**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Sarah Baylen | 无向 | 1937-02-06 结婚；布朗自述对硼氢化物的兴趣归功于她 |

> **禁入库名单**：父母 Charles / Pearl Brovarnik（仅背景叙述，非学术关系）；Markovnikov（规则命名引用，无个人关系）。metadata.json 无其他 page.md 未载关系。

## 8. 奖项清单

- Nobel Prize in Chemistry（1979，与 Georg Wittig 共享）
- Centenary Prize（1955）
- William H. Nichols Medal（1959）
- National Medal of Science（1969）
- Golden Plate Award of the American Academy of Achievement（1971）
- Elliott Cresson Medal（1978）
- Priestley Medal（1981）
- Perkin Medal（1982）
- American Institute of Chemists Gold Medal（1985）
- NAS Award in Chemical Sciences（1987）
- 另有（frontmatter 列出、年份未载）：ACS Award for Creative Work in Synthetic Organic Chemistry、Remsen Award、Linus Pauling Award、Roger Adams Award、Chemical Pioneer Award、Oesper Award
- 荣誉博士：哥白尼大学（托伦）、巴黎第十一大学；International Academy of Science, Munich 名誉会员；Alpha Chi Sigma 名人堂（2000）

## 9. 机构清单

- 教育：Crane Junior College → Wright Junior College → University of Chicago（1935 入学，B.S. 1936，PhD 1938）
- 任职：University of Chicago 讲师（1939–1943）→ Wayne University, Detroit 助理教授（1943–，1946 副教授）→ Purdue University 无机化学教授（1947–，1978 起荣休教授至 2004 去世）
- 命名机构：Purdue 校园 Herbert C. Brown Laboratory of Chemistry

## 10. 终审清单

- [ ] 生卒 1912-05-22 / 2004-12-19，享年 92，出生地伦敦、去世地 Lafayette（心脏病）
- [ ] 本名 Herbert Brovarnik；1936 入籍美国；双国籍 rank 表述准确
- [ ] PhD 1938 / 论文发表 1939 两个年份不混淆
- [ ] 1979 共享（Wittig）表述准确；硼/磷分工清楚
- [ ] Subba Rao 发现异常反应的归属表述准确
- [ ] 反马氏加成方向表述准确
- [ ] 引语全部可在本地 Wikipedia 原文溯源（无直接引语则全部间接转述）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Herbert_C._Brown/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：下载 Wikipedia 肖像（250px→500px；404 用 REST API 查 infobox 原图名；仍失败装饰圆占位）
- [ ] **国籍**：封面顶部明示美国（注明生于伦敦）
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（无原文一律间接转述）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt、hbox≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
