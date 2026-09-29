# Giulio Natta（吉利奥·纳塔）立传提示词

> qid=Q234145 · 1903-02-26 – 1979-05-02 · 意大利化学家 · 20 世纪 · 诺贝尔化学奖（1963，与 Karl Ziegler 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Giulio_Natta/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 `images.txt` / REST API 下载；404 则装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{cubes}\enspace 立构规整聚合之父\enspace·\enspace 意大利`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「等规立构」母题——圆点按规整间距排列，暗示全同立构聚丙烯的甲基规则排布。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），聚合反应式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Giulio Natta（中文惯称：吉利奥·纳塔；意大利语发音 [ˈd͡ʒu.ljo ˈnat.ta]）
- **生卒**：1903-02-26 生于意大利王国 Imperia → 1979-05-02 逝于意大利 Bergamo，享年 76
- **国籍**：Italy（意大利）
- **身份**：化学工程师、化学家、发明家、大学教授（Italian chemical engineer and Nobel laureate）
- **家庭**：富裕家庭出身；1935 年娶 Rosita Beati（文学专业毕业，为丈夫发现的聚合物创造 "isotactic / atactic / syndiotactic" 术语；1968 年去世），子女 Giuseppe 与 Franca；1956 年确诊帕金森病，1963 年诺贝尔仪式上需儿子与四位同事协助完成演讲
- **教育轨迹**：
  - 热那亚大学（先读纯数学）
  - Politecnico di Milano（1924 化学工程学位；1927 通过教授资格考试）
- **博士导师**：page.md 无载（infobox 无 doctoral advisor 一栏，**页面无载禁写**）
- **研究领域**：有机化学——高分子立体化学、X 射线衍射分析、立构规整聚合

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **因佩里亚之子（1903）**：利古里亚海滨小城的富裕家庭——先数学后化学工程的教育转向。
2. **X 射线衍射先驱（1920 年代起）**：用衍射法解析无机化合物与结晶固体的微观结构，发现催化剂晶体结构与催化性能的显著关联——为日后理解 Ziegler 催化剂埋下伏笔。
3. **打破德国垄断（1930 年代初）**：与 Montecatini 合作开发新甲醇合成工艺，首次打破德国工业在该领域的垄断——从此确立"理论化学的技术与工业应用"这条贯穿终身的路线。
4. **学术版图（1929–1938）**：米兰大学理学院物理化学负责人（1929–1933）；帕维亚大学普通化学研究所正教授兼所长（1933–1935，解析膦、胂等结构）；罗马大学物理化学正教授（1935）；都灵理工大学工业化学研究所所长（1936–1938）。
5. **执掌米兰理工（1938）**：接任米兰理工化学工程系主任——前任 Mario Giacomo Levi 因法西斯意大利的犹太人种族法被迫去职，接任方式"颇有争议"（史实敏感点，见 §5）。
6. **合成橡胶与超声聚合（1938–战后）**：参与建设意大利第一座合成橡胶厂（费拉拉，1938）；战后回到高分子化学，研究超声在聚合物化学中的应用。
7. **研究中心网络（1946–1947）**：1946 创建国家研究委员会（CNR）工业化学研究中心；1947 与 Montecatini 总监 Pier Giustiniani 访美考察石油化学，归国后获资金与设施建成先进化学研究中心。
8. **转向立构规整（1950 年代初）**：对聚合物立体化学产生浓厚兴趣，关注 Karl Ziegler 在 Max Planck 煤炭研究所的有机金属催化剂研究；用 Ziegler 型催化剂从乙烯等单体获得高度线性的结晶聚合物。
9. **1954-03-11 等规聚丙烯**：用 Ziegler 型催化剂变体把路线应用于丙烯及其他高碳 α-烯烃，得到全新有机化合物——高度有序晶体结构的 isotactic polypropylene（等规聚丙烯）。
10. **命名与专利**：Ziegler–Natta 催化剂由此得名；1950 年代中期起的专利构成全球等规聚丙烯工业生产的基础。
11. **1963 诺贝尔化学奖**：与 Karl Ziegler 共享——表彰其在高分子（high density polymer）方面的工作；此前 Ziegler 发现低压聚乙烯催化的消息激励他把同一方法推向丙烯。
12. **大分子化学研究所（1961）**：经 CNR 批准创建大分子化学研究所，培养出大批进入大学与产业的研究者。
13. **病中的斯德哥尔摩（1956–1979）**：帕金森病 1956 确诊、1963 年演讲需协助——科学意志与身体衰退的对照；1969 获罗蒙诺索夫金奖；四个国家的科学院成员（Lincei 1955、纽约科学院 1960、法国科学院 1964、苏联科学院 1966）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 deepviolet） | `#52307C` | 立构规整结构的秩序与优雅（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（等规聚丙烯 badgeIso） | `#6A4AA0` | 蓝紫 isotactic PP / 1954-03-11 |
| 分类色 2（X 射线衍射 badgeXray） | `#1B6B8F` | 青 diffractometry / 催化剂晶体结构 |
| 分类色 3（工业化学 badgeMonte） | `#B0432A` | 砖红 Montecatini / 甲醇 / 合成橡胶 |
| 分类色 4（学术与荣誉 badgeAcad） | `#2E6B4F` | 绿四大科学院 / 罗蒙诺索夫金奖 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），但圆点按等距规整网格排列，呼应"等规（isotactic）"的秩序感。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（`music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`，不要复制 wav 文件，Makefile 直接引用该路径）
- **风格**：辽阔 / 深沉 / 史诗感
- **匹配理由**：
  - "辽阔" 匹配利古里亚海滨出身与工业尺度的叙事——从因佩里亚到全球聚丙烯工业
  - "深沉" 匹配其逆境底色——帕金森病 25 年与病中斯德哥尔摩的坚持
  - "史诗感" 匹配 1954-03-11 等规聚丙烯诞生这一转折点
- **时长**：对齐 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 立构规整聚合之父 / Giulio Natta 1903–1979 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/师承留白注明/出生地/去世地/领域/荣誉）
03  纳塔的一生 — 高斯式时间线（10 节点：1903→1924→1933→1938→1946→1952→1954→1963→1969→1979）
04  早年：从数学到化学工程 (1903–1927) — 表格「时间|事件|结果」
05  X 射线衍射先驱 (1929–1935) — 表格「对象|方法|结果」
06  都灵与米兰 (1936–1945) — 表格「事件|语境|结果」（合成橡胶厂/执掌米兰理工/战时）
07  Montecatini 与研究中心 (1946–1952) — 表格「人物|事件|结果」（Giustiniani 访美/CNR 中心）
08  Ziegler 催化剂与丙烯 (1952–1954) — 表格「问题|方法|结果」+ 公式框：丙烯 → isotactic PP（1954-03-11）
09  1963 诺贝尔化学奖（与 Ziegler 共享） — 表格「人物|贡献|结果」+ 公式框：立构规整聚合
10  命名者 Rosita — 表格「术语|创造者|意义」（isotactic/atactic/syndiotactic，Rosita Beati 命名）
11  病中的科学 (1956–1979) — 表格「年份|事件|结果」（1956 确诊/1963 演讲协助/1969 罗蒙诺索夫金奖）
12  荣誉与科学院 — 高斯式「类别|代表|意义」表格（Lincei 1955 / 纽约 1960 / 法国 1964 / 苏联 1966）
13  遗产：立构规整的世界 — 四分类遗产盒 + 公式框：Ziegler–Natta 催化剂 → 全球等规聚丙烯工业
14  结尾 — 「当甲基排成队列，塑料第一次有了秩序。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 诺奖官方获奖理由 | **page.md 无官方英文 citation 原文**（"for his work on high density polymer" 是正文叙述口径，禁写成官方 citation 全句）——立传按 page.md 口径转述 |
| 共享方向 | 1963 与 **Karl Ziegler 共享**；Ziegler 低压聚乙烯在先、Natta 推广至丙烯立构规整聚合——纳塔篇勿把聚乙烯原始发现写成自己的 |
| Levi 接任事件 | 1938 年前任 Mario Giacomo Levi 因**法西斯种族法**被迫去职、纳塔接任"somewhat controversial"——page.md 明载可写但保持一句客观陈述，**勿展开政治评论、勿渲染** |
| "isotactic" 命名 | 术语由其妻 **Rosita Beati**（文学背景）创造——纳塔篇亮点页可写，勿误归 Natta 本人或 Ziegler |
| 帕金森时间线 | 1956 确诊；1963 诺贝尔仪式**需儿子与四位同事协助**完成演讲——年份勿写反 |
| 等规聚丙烯日期 | **1954-03-11** 获得该新化合物——勿写成 1953 或"1950 年代初" |
| 博士导师 | **page.md 无载**（infobox 无 advisor 栏）——身份信息页师承栏留白注明"页面无载"，严禁编造 |
| 热那亚阶段 | 先在 University of Genoa 读**纯数学**后转米兰化学工程——勿写成一直读化工 |
| 诺奖演讲题目 | 1963-12-12《From the Stereospecific Polymerization to the Asymmetric Autocatalytic Synthesis of Macromolecules》（Nobelprize.org 链接注载）——引用时注明来源页脚 |
| 与 Ziegler 关系 | 1952 年纳塔以 Montecatini **顾问**身份接触 Ziegler 披露的催化剂——是技术承接与合作者关系，page.md 未载私人交恶细节，禁写"决裂/专利大战" |
| metadata 噪声 | metadata.json nationality 含 "Kingdom of Italy"（历史国名）——国籍入库用规范国名 Italy |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q234145 | ✅ |
| name_zh | 吉利奥·纳塔 | ✅ |
| name_en | Giulio Natta（page.md 规范名；库内无既有记录） | ✅ |
| birth_date | 1903-02-26 | ✅ |
| death_date | 1979-05-02 | ✅ |
| nationality | Italy | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：polymer chemistry / stereochemistry / X-ray crystallography / organic chemistry，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**共同得主 / 配偶 / 同事**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Karl Ziegler | 无向 | 1963 诺贝尔化学奖共同得主（对手方 yaml 用同名规范形式） |
| spouse | Rosita Beati | 无向 | 1935 结婚；1968 年去世；创造 isotactic/atactic/syndiotactic 术语 |
| colleague | Pier Giustiniani | 无向 | Montecatini 总监，1947 同访美国，资助米兰先进化学研究中心 |

> **禁入库名单**（page.md 提及但按红线/惯例不入库）：Mario Giacomo Levi（前任，种族法去职——历史事件非个人实质关系）；子女 Giuseppe/Franca（page.md 明载但按批次惯例不入库，防噪声）；Karl Ziegler 之外的机构（Montecatini/CNR 为机构非人物）。metadata-only 无新增。

## 8. 奖项清单

- Nobel Prize in Chemistry（1963，与 Karl Ziegler 共享）
- Lomonosov Gold Medal（1969，苏联科学院）
- John Scott Award
- Knight Grand Cross of the Order of Merit of the Italian Republic（意大利共和国功勋大十字骑士）
- 科学院成员：Accademia dei Lincei（1955）、New York Academy of Sciences（1960）、French Academy of Sciences（1964）、Academy of Sciences of the Soviet Union（1966）

## 9. 机构清单

- 教育：University of Genoa（纯数学）、Politecnico di Milano（1924 化学工程学位；1927 教授资格）
- 任职：University of Milan 理学院物理化学负责人（1929–1933）；Pavia University 普通化学研究所正教授兼所长（1933–1935）；University of Rome La Sapienza 物理化学正教授（1935）；Politecnico di Torino 工业化学研究所所长（1936–1938）；Politecnico di Milano 化学工程系主任（1938–）
- 创建机构：CNR 工业化学研究中心（1946）；大分子化学研究所（1961，CNR 批准）；费拉拉合成橡胶厂（参与，1938）

## 10. 终审清单

- [x] 生卒 1903-02-26 / 1979-05-02，享年 76，出生地 Imperia、去世地 Bergamo
- [x] 1963 与 Ziegler 共享；官方 citation 原文页面无载已标注
- [x] 1954-03-11 等规聚丙烯；"isotactic" 命名归 Rosita Beati
- [x] 帕金森 1956 确诊、1963 演讲需协助；博士导师页面无载已留白
- [x] Levi 事件一句客观陈述不展开；四大科学院年份准确
- [x] 师承关系：仅 Ziegler co-honored + Giustiniani colleague（page.md 明载范围）
- [x] 引语全部可在本地 Wikipedia 原文找到（"isotactic polypropylene" 句、"somewhat controversial manner" 句）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 等距规整气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Giulio_Natta/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 `images.txt` 下载并核验（page.md 内嵌图为纳塔与妻子 1960s 合照，可裁作肖像或插图；404 则装饰圆占位）
- [ ] **国籍**：封面顶部明示意大利
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（等规聚丙烯句、Rosita 术语句、帕金森演讲句）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 骨架）对齐；与 Karl Ziegler 篇（本批）共享口径互查

---

> **名单状态**：由主控统一更新 `chemist/generate_20th_century_list.py`，本文件不改总表。
