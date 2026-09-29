# Robert Bruce Merrifield（罗伯特·布鲁斯·梅里菲尔德）立传提示词

> qid=Q224153 · 1921-07-15 – 2006-05-14 · 美国生物化学家 · 20 世纪 · 诺贝尔化学奖（1984，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Robert_Bruce_Merrifield/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + Sanger 式时间线 + 表格语义化 tabularx + 金色公式框 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 page.md 图注照片取；若下载失败用装饰圆占位并注记）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{book-open}\enspace 固相合成的发明者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「固相树脂珠 / 逐个接肽」母题——离散圆点暗示固相载体上逐个延伸的氨基酸链。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（固相肽合成：固相载体 → 逐个接肽 → 裂解；1969 RNase A 全合成 124 残基）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Robert Bruce Merrifield（中文惯称：罗伯特·布鲁斯·梅里菲尔德）
- **生卒**：1921-07-15 生于得克萨斯州 Fort Worth → 2006-05-14 逝于新泽西州 Cresskill 自宅（久病之后），享年 84
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist）；The Rockefeller University 教授
- **家庭**：George E. Merrifield 与 Lorene（娘家姓 Lucas）的独子；1923 年举家迁加州；1949-06-20（博士毕业次日）娶 Elizabeth Furlong（Libby，生物学科班出身，婚后加入其实验室工作逾 23 年）；育 6 子女：James、Nancy、Betsy、Cathy、Laurie、Sally；Libby 于 2017-09-13 去世；在世时有 16 名孙辈
- **教育轨迹**：
  - 加州辗转九所小学、两所中学，1939 年毕业于 Montebello High School（在此同时爱上化学与天文学）
  - Pasadena Junior College 两年 → 转学 University of California, Los Angeles（UCLA）化学
  - 毕业后一年在 Philip R. Park Research Foundation 照料实验动物群落、参与合成氨基酸饲料生长实验
  - 返回 UCLA 化学系读研：PhD 1949（导师 M.S. Dunn，论文 *Microbiological Studies in Pyrimidines*）
- **导师**：Max S. Dunn（M.S. Dunn，UCLA 生物化学教授）
- **博士**：1949，UCLA
- **研究领域**：生物化学——固相肽合成（solid phase peptide synthesis, SPPS）、肽化学、酶的化学合成

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **得州出生、加州长大（1921–1939）**：Fort Worth 独子，1923 年迁加州；辗转多所学校，在 Montebello High School 同时爱上化学与天文。
2. **Pasadena → UCLA（1939–1943）**：两年社区学院后转入 UCLA 化学系。
3. **Philip R. Park 研究基金会（本科毕业后一年）**：照料动物群落、参与合成氨基酸饲料实验——其中 Geiger 用「最低律」首次证明**必需氨基酸必须同时存在**生长才能发生。
4. **UCLA 博士（1949）**：随 M.S. Dunn 发展嘧啶的微生物定量方法；6 月 19 日毕业，次日结婚，再一日携妻赴纽约。
5. **Rockefeller 与 Woolley（1949–）**：任 D.W. Woolley 博士的 Assistant——做读博期间发现的二核苷酸生长因子与 Woolley 早年的肽生长因子；正是这些研究引出对**肽合成**的需求。
6. **SPPS 的构想（1959）**：固相肽合成的想法诞生——把肽链锚定在不溶性固相载体上逐个延伸。
7. **1963 年 JACS 经典论文**：**唯一作者**发表 "solid phase peptide synthesis" 方法——该文是 JACS 历史上**引用第五高**的论文。
8. **1960 年代中期战果**：实验室先后合成缓激肽（bradykinin）、血管紧张素（angiotensin）、去氨基催产素（desamino-oxytocin）与胰岛素。
9. **1969 酶的全合成**：与同事 Bernd Gutte 宣布首次化学合成酶——核糖核酸酶 A（ribonuclease A）；证明酶的本质是化学的。
10. **一维序列决定三维结构**：RNase A 全合成的更深意义——氨基酸线性序列经肽键连接直接决定蛋白质三级结构：一维信息直接编码三维分子。
11. **SPPS 的辐射效应**：极大推动生物化学、药理学与医学进展——酶、激素、抗体活性结构基础的系统探索成为可能；方法后扩展至核苷酸与糖类的固相合成。
12. **1984 诺贝尔化学奖（独享）**：page.md 口径 "for the invention of solid phase peptide synthesis"——固相肽合成的发明。
13. **晚年与身后**：一直在 Rockefeller 实验台前活跃；1993 年 Jeffrey I. Seeman 为 ACS "Profiles, Pathways, and Dreams" 系列出版其自传 *Life during a Golden Age of Peptide Chemistry*；1998 获 ABRF 杰出贡献奖；2006-05-14 于 Cresskill 自宅去世；2013 年 NAS 传记回忆录（Ulf Ragnarsson 执笔）刊行。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深松绿 pine green） | `#1E6B52` | 固相树脂的沉稳与肽链的生机（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（固相合成 badgeSPPS） | `#2E5A9E` | 蓝固相载体 / 逐个接肽 |
| 分类色 2（酶的全合成 badgeEnzyme） | `#C0395B` | 玫瑰 RNase A / 酶的化学本质 |
| 分类色 3（生物活性肽 badgePeptide） | `#D97B29` | 琥珀缓激肽 / 血管紧张素 / 胰岛素 |
| 分类色 4（方法学辐射 badgeImpact） | `#1B4D3E` | 墨绿生物化学·药理学·医学的推进 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「树脂珠上的肽链延伸」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（`music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`；执行 Beamer 时复制为本目录 `Tragedy.wav`，勿直接引用外部路径）
- **风格**：低回 / 深情 / 迟来的桂冠
- **匹配理由**：
  - "低回深情" 匹配其一生的静水深流——独子、辗转多校、博士后次日结婚当天赴任，人生底色朴素克制
  - "迟来的桂冠" 匹配其诺奖叙事——1959 年构想、1963 年论文，1984 年 63 岁方获诺奖，MethodName 改变世界却长期在实验台前默默耕耘
  - "悲悯底色" 匹配久病之后在自宅安然辞世的收束——Tragedy 曲名的悲怆恰好托住全篇的沉稳收尾
- **时长对齐**：ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 把肽链种在树脂上的人 / Robert Bruce Merrifield 1921–2006 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/出生地/去世地/教育/博士/师承/领域/荣誉）
03  梅里菲尔德的一生 — Sanger 式时间线（10 节点：1921→1939→1943→1949→1959→1963→1969→1984→1993→2006）
04  得州独子与加州求学 (1921–1943) — 表格「时间|事件|结果」
05  UCLA 博士与三日三事 (1949) — 表格「时间|事件|结果」（毕业→结婚→赴纽约）
06  Rockefeller 与 Woolley 岁月 — 表格「问题|方法|结果」（生长因子 → 肽合成需求）
07  固相肽合成的诞生 (1959–1963) — 表格「问题|方法|结果」+ 公式框：SPPS 固相载体→接肽→裂解
08  1969：酶的化学全合成 — 表格「挑战|合作|意义」+ 公式框：RNase A 全合成证明一维序列决定三维结构
09  1984 诺贝尔化学奖（独享） — 表格「主题|内容|意义」+ 获奖口径公式框
10  家族实验室 — 表格「人物|角色|结果」（Libby 23 年 / 六子女 / 16 孙辈）
11  荣誉清单 — Sanger 式「类别|代表|意义」表格（Lasker 1969 / Gairdner 1970 / Nobel 1984 / Seaborg Medal 1993）
12  身后与纪念 — Sanger FFT 页式流程图（1993 自传 → 1998 ABRF 奖 → 2006 辞世 → 2013 NAS 回忆录）
13  遗产：合成生物学的地基 — 四分类遗产盒 + 公式框：SPPS → 多肽药物与疫苗工业
14  结尾 — 「把化学固定在固体上，让生命可以在流水线上生长。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1984 独享 | 诺贝尔化学奖 **独享**（无共同得主）——勿写共享 |
| 获奖理由 | page.md 口径 "for the invention of solid phase peptide synthesis"——**官方 citation 英文原句页面无载，禁止杜撰整句**；用 page.md 转述口径或间接表述 |
| 1963 论文 | JACS **唯一作者**（sole author）、JACS 历史引用第五——两个数字勿混淆（勿写"第五篇论文"） |
| 1969 全合成 | 与 **Bernd Gutte** 合作首合成核糖核酸酶 A——意义两层：证明酶的化学本质 + 一维序列决定三维结构；勿写成"第一个合成蛋白质"以外的自行发挥 |
| 1960s 合成清单 | 缓激肽、血管紧张素、去氨基催产素、胰岛素——四项并列如实列举，勿加"首次"之类页面无载断言 |
| SPPS 构想年 | page.md 表述 "eventually, to the idea for solid phase peptide synthesis (SPPS) in 1959"——构想 1959、成文 1963——勿合并为一年 |
| 结婚日期 | **1949-06-20 毕业次日结婚、次日赴纽约**——三日三事的时间线按 page.md |
| 博士导师 | Max S. Dunn（M.S. Dunn）——勿与其他 UCLA 学者混淆 |
| 妻子 | Elizabeth Furlong（Libby），生物学科班出身、婚后加入其实验室工作 **逾 23 年**——勿写"共同发表"（页面无载） |
| 出生名 | **Robert Bruce Merrifield**——正文惯称 R. Bruce Merrifield / Bruce Merrifield，同一人 |
| 引语 | 本地页面**无任何其个人直接引语**——中文引号内容一律间接转述 |
| 页面较短 | 本地页面仅 infobox + 正文数节——凡 page.md 无载的生平细节（如军旅、宗教、其他职务）**一律禁写** |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q224153 | ✅ |
| name_zh | 罗伯特·布鲁斯·梅里菲尔德 | ✅ |
| name_en | Robert Bruce Merrifield | ✅ |
| birth_date | 1921-07-15 | ✅ |
| death_date | 2006-05-14 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / solid phase peptide synthesis / peptide chemistry，带 rank） | ✅ |
| has_biography | 0（立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 家人**（只收 page.md 正文或 infobox 明载；本页 metadata 无额外可入库关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Max S. Dunn | 师→生（博士导师） | UCLA PhD 1949 |
| colleague | D. W. Woolley | 无向 | Rockefeller 时期共事（任其 Assistant）；肽生长因子研究引向肽合成需求 |
| colleague | Bernd Gutte | 无向 | 1969 共同宣布首次化学合成核糖核酸酶 A |
| spouse | Elizabeth Furlong | 无向 | 1949-06-20 结婚；生物学家，后在其实验室工作逾 23 年 |

> **禁入库名单**：Geiger（仅系引用其实验的关联人物）、Jeffrey I. Seeman（自传出版者，非学术合作关系）、Ulf Ragnarsson（NAS 回忆录执笔者）——均不入库。metadata.json 未载 advisor/student 补充名单。

## 8. 奖项清单

- Nobel Prize in Chemistry（1984，独享）
- Albert Lasker Award for Basic Medical Research（1969）
- Gairdner Foundation International Award（1970）
- Golden Plate Award of the American Academy of Achievement（1985）
- Glenn T. Seaborg Medal（1993）；Chemical Pioneer Award（1993）
- ACS Award for Creative Work in Synthetic Organic Chemistry；William H. Nichols Medal；Centenary Prize；Ralph F. Hirschmann Award in Peptide Chemistry
- 荣誉博士：University of Montpellier-II
- Association of Biomolecular Resource Facilities Award（1998，杰出贡献于生物分子技术）

## 9. 机构清单

- 教育：Montebello High School（1939）、Pasadena Junior College（两年）、University of California, Los Angeles（化学；PhD 1949）
- 任职：Philip R. Park Research Foundation（本科毕业后一年）；The Rockefeller Institute for Medical Research → The Rockefeller University（1949–，实验台前活跃至晚年）
- 出版纪念：Life during a Golden Age of Peptide Chemistry（ACS Profiles, Pathways, and Dreams 系列，1993，Seeman 执笔）；NAS Biographical Memoirs（2013）

## 10. 终审清单

- [ ] 生卒 1921-07-15 / 2006-05-14（享年 84），出生地 Fort Worth、去世地 Cresskill 自宅
- [ ] 1984 **独享**；获奖理由用 page.md 口径，官方 citation 整句禁写
- [ ] 1963 JACS 唯一作者 + 引用第五；1959 构想 / 1963 成文
- [ ] 1969 与 Gutte 首合成 RNase A；一维→三维结构意义
- [ ] 1949-06-20 结婚次日赴纽约时间线准确
- [ ] 全文无直接引语（页面无载）——中文引号内容全部间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Robert_Bruce_Merrifield/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 肖像已就位或装饰圆占位并注记
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：全文无直引（页面无其原话）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：由主控统一更新 `chemist/generate_20th_century_list.py`（执行者不改）。
