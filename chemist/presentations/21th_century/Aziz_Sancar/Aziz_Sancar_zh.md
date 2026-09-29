# Aziz Sancar（阿齐兹·桑贾尔）立传提示词

> qid=Q15118973 · 1946-09-08 – 在世 · 土耳其/美国分子生物学家 · 21 世纪 · 诺贝尔化学奖（2015，与 Tomas Lindahl、Paul L. Modrich 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Aziz_Sancar/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页，是本次执行的版式语言。

---

## 0. 正文形式说明（参考桑格立传模板，★ 硬性要求）

1. **封面有头像位**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 `images.txt` **无真实肖像**（仅 Savur 风景照、伊斯坦布尔大学医学院楼、光复活酶结构模型三张）——封面用主色装饰圆占位（圆内 `\faIcon{sun}` 呼应光修复），图注注明「装饰圆占位 · 页面无肖像」；正文可用 1QNF 光复活酶结构模型图作插图。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{book-open}\enspace 修复阳光损伤的人\enspace·\enspace 土耳其 / 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素（UNC 医学院 · DNA 修复与生物钟 · 2015 诺贝尔化学奖）。
3. **必须有身份信息页**（★ 必做）：左侧头像（装饰圆）+ 右侧 2×2 信息网格，至少含：生卒、本名 Aziz Sancar、国籍（Turkey / United States）、出生地 Savur, Mardin、教育（Istanbul University MD 1969 / UT Dallas PhD 1977）、博士导师 Claud Stan Rupert、核心领域 DNA repair / photolyase / circadian clock、机构（UNC School of Medicine）、荣誉。事实取自本地 page.md，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「光 / 修复」母题——光斑般的圆点暗示蓝光唤醒修复酶。
5. **表格语义化 + 公式框**（★ 桑格版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Aziz Sancar（土耳其语发音 [aˈziz ˈsandʒaɾ]；中文惯称：阿齐兹·桑贾尔）
- **生卒**：1946-09-08 生于土耳其东南部 Mardin 省 Savur → 在世（页面无卒日，全篇留白处理）
- **国籍**：Turkey（土耳其）、United States（美国）；2025-07-31 获北塞浦路斯土耳其共和国（TRNC）公民身份（页面明载）
- **身份**：土耳其-美国分子生物学家；UNC 医学院 Sarah Graham Kenan 生物化学与生物物理学教授、UNC Lineberger 综合癌症中心成员
- **家庭**：八个孩子中的第七个；长兄 Kenan Sancar 为土耳其军队准将（退役）；表亲 Mithat Sancar 为政界人士（页面明载，仅背景）；1978 年与在达拉斯读博士时相识的 Gwen Boles Sancar 结婚——她同为 UNC 生物化学与生物物理学教授；二人共同创办 Aziz & Gwen Sancar 基金会与 Carolina Türk Evi（北卡土耳其之家）
- **教育轨迹**：
  - Savur 家乡附近完成小学；高中想学化学，因五位同学同考医学院而改学医
  - 1969 伊斯坦布尔大学医学院 MD（以第一名毕业）
  - 1971–1973 TÜBİTAK 奖学金赴 Johns Hopkins 学习生物化学（约 1.5 年后因不适应返土耳其行医 1.5 年）
  - 1977 得克萨斯大学达拉斯分校 Ph.D.（论文 *A study on photoreactivating enzyme (DNA photolyase) of Escherichia coli*，导师 Claud Stan Rupert 实验室）
- **导师**：Claud Stan Rupert（UT Dallas 博士导师；DNA 修复领域发现者之一）
- **研究领域**：DNA 修复（光复活/photolyase、核苷酸切除修复 NER）、细胞周期检查点、生物钟（circadian clock）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **萨武尔农家（1946）**：土耳其中下层家庭第八个孩子中的第七个；父母未受过教育却极重视子女教育，乡村学院出身的理想主义教师给他一生的影响。
2. **医学院第一名（1969）**：想学化学却进了伊斯坦布尔大学医学院，以榜首毕业；毕业后回 Savur 行医 1.5 年。
3. **约翰·霍普金斯的挫折（1971–1973）**：TÜBİTAK 奖学金赴美学生物化学，因社交与语言障碍（抵美时只会法语）返回土耳其——又行医 1.5 年。
4. **写信给 Rupert（1973–1977）**：致信 DNA 修复先驱 Rupert 获录取，赴 UT Dallas 攻读分子生物学；研究主题是「细菌经致死剂量紫外线照射后被蓝光照亮即可复活」。
5. **克隆光复活酶基因（1976）**：作为博士论文工作成功复制（clone）photolyase 基因——修复胸腺嘧啶二聚体的酶。
6. **三次被拒（1977）**：博士毕业后三份博士后申请均被拒，遂到耶鲁大学做实验室技术员，一待五年。
7. **耶鲁五年：NER 机制（1977–1982）**：在 Dean Rupp 实验室阐明核苷酸切除修复的分子细节——鉴定 UvrABC 内切酶及其编码基因，发现这些酶在损伤链上切两刀、切下含损伤部分的 12–13 个核苷酸。
8. **50 份申请唯一答复（1982 后）**：向 50 所大学求职只有北卡罗来纳大学一个正面答复——出任 UNC 讲师；他自述英语口音曾不利于讲师生涯。
9. ** chapel Hill 完成 NER 全图**：在 UNC 续写细菌 NER 的后续步骤，并研究人体中更复杂的同类机制。
10. **追了 20 年的自由基（PNAS 就职论文）**：捕获追踪近 20 年的光复活酶自由基，直接观察到胸腺嘧啶二聚体修复的光循环。
11. **生物钟（2014）**：团队发现 *Period* 与 *Cryptochrome* 两个基因维持人体所有细胞的昼夜节律并与 24 小时同步（2014-09-16 发表于 Genes & Development）；为时差、季节性情感障碍与癌症治疗优化提供理解框架。
12. **2015 诺贝尔化学奖**：与 Tomas Lindahl、Paul L. Modrich 共享，表彰「DNA 修复的机制学研究」；2005 年当选 NAS 院士——首位土耳其籍院士；土耳其第二位诺奖得主（仅次于同门校友 Orhan Pamuk）。
13. **金归安卡（2016）**：将诺贝尔金奖章与证书于 2016-05-19（土耳其独立战争发起 97 周年纪念日）以总统仪式捐赠安纳托利亚的 Atatürk 陵墓 Anıtkabir；复制品交给母校伊斯坦布尔大学。

## 3. 配色方案（桑格式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青 teal-deep） | `#0B5351` | 光复活酶的「蓝光修复」母题（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（光复活 badgePhoto） | `#D98E04` | 琥珀·photolyase / 光循环 |
| 分类色 2（核苷酸切除修复 badgeNER） | `#1F6F8B` | 青蓝·UvrABC / 双切 12–13 nt |
| 分类色 3（生物钟 badgeClock） | `#5B2A86` | 紫·Period / Cryptochrome 昼夜节律 |
| 分类色 4（诺奖与家国 badgeHonor） | `#A63A2B` | 砖红·斯德哥尔摩 / Anıtkabir 捐章 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），光斑圆点暗示「紫外损伤 → 蓝光修复」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（`music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`；不要复制 wav 文件，Makefile 里直接引用原路径）
- **风格**：深沉 / 逆境 / 迟来的公允
- **匹配理由**：
  - 「逆境」匹配其前半生——乡村医生之子、两度返土行医、三份博士后被拒、50 份求职唯一答复
  - 「迟来的公允」匹配 photolyase 自由基「追了 20 年」的长跑
  - 结尾转明亮，呼应从 Savur 到斯德哥尔摩的弧线
- **时长**：按 Makefile 默认 `-shortest` 对齐 15 页即可

## 4. Slide 规划（15 页，桑格式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 修复阳光损伤的人 / Aziz Sancar 1946– + 四色 badge + 右上头像占位 + 国籍行「土耳其 / 美国」
02  身份信息页（★ 必做）— 左头像占位 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士导师/领域/机构/荣誉）
03  桑贾尔的一生 — 桑格式时间线（10 节点：1946→1969→1971→1973→1977→1978→1982→2005→2015→2016）
04  早年：萨武尔的第七个孩子 (1946–1969) — 表格「时间|事件|结果」
05  从行医到达拉斯 (1969–1977) — 表格「阶段|内容|结果」+ 公式框：光复活——紫外线损伤 + 蓝光 → 复活
06  耶鲁技术员：NER 机制 (1977–1982) — 表格「问题|方法|结果」+ 公式框：UvrABC 双切 12–13 nt
07  chapel Hill：NER 全图与人体机制 (1982–) — 表格「挑战|方法|结果」
08  追光二十年 (PNAS 就职论文) — 表格「问题|方法|结果」+ 公式框：photolyase 光循环
09  2015 诺贝尔化学奖 — 公式框：官方获奖理由 "for mechanistic studies of DNA repair"（与 Lindahl / Modrich 共享）
10  生物钟 (2014) — 表格「问题|发现|意义」（Period / Cryptochrome；jet-lag / 季节性情感障碍 / 癌症治疗）
11  荣誉与学会 — 桑格式「类别|代表|意义」表格 + itemize 清单（TÜBİTAK 1995 / NAS 2005 首位土耳其籍 / Vehbi Koç 2007）
12  金归 Anıtkabir — 桑格 FFT 页式流程图（2015 获奖 → 2016-05-19 总统仪式捐章 → 复制品赠伊斯坦布尔大学）
13  遗产：从 Savur 到斯德哥尔摩 — 四分类遗产盒（Aziz & Gwen Sancar 基金会 / Carolina Türk Evi / 首位土耳其籍 NAS / DNA 修复机制）
14  结尾 — 「被蓝光照亮而复活的，不只是细菌。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2015 获奖理由 | 官方口径 "for mechanistic studies of DNA repair"；三人分工——Sancar=核苷酸切除修复/光复活、Modrich=错配修复、Lindahl=碱基切除修复，**勿互相张冠李戴** |
| 共享口径 | 2015 为**三人共享**；对另两人一律用规范全名 Tomas Lindahl / Paul L. Modrich |
| 在世口径 | 页面无卒日——全篇写 1946-09-08 – 在世，**禁止编造卒年** |
| MD 与 PhD | MD=伊斯坦布尔大学 1969（第一名毕业）；PhD=得克萨斯大学达拉斯分校 1977——两校勿混 |
| Johns Hopkins | 是 TÜBİTAK 奖学金进修生物化学（非学位项目，约 1971–1973）——勿写成「在霍普金斯读博」 |
| 耶鲁身份 | 是**实验室技术员**（lab technician）五年，在 Dean Rupp 实验室完成 NER 机制工作——勿写成「耶鲁教授」或「博士后」 |
| 求职叙事 | 「50 份申请唯一正面答复=UNC 讲师」——勿写成「50 次博士后被拒」 |
| 族裔敏感 | 页面载有族裔/出身争议、青年时期组织关联、泛突厥主义表态等高度敏感内容——**一律禁写**；只写「土耳其-美国分子生物学家」 |
| 表亲政治 | Mithat Sancar 的政党职务只作家庭背景一句带过或不写，**不展开**；兄 Kenan Sancar 同理（家庭成员不入库） |
| 北塞浦路斯 | 2025-07-31 获 TRNC 公民身份页面明载，可客观一笔；**不做任何政治评论** |
| 引语红线 | 页面仅有 "I'm a Turk, that's it." 等涉及族裔的引语——**禁用**；中文引号内不得出现无法在 page.md 溯源的「原话」，一律间接转述 |
| 第二位土耳其诺奖得主 | 页面明载「仅次于 Orhan Pamuk」——须写全「第二位土耳其诺贝尔奖得主（继 Pamuk 之后）」，勿写成「土耳其首位」（首位是 NAS 首位土耳其籍院士 2005，两事勿混） |
| 捐章日期 | 2016-05-19（土耳其独立战争发起 97 周年）；奖章原件赠 Anıtkabir、复制品赠伊斯坦布尔大学——勿颠倒 |
| 妻子 | Gwen (Boles) Sancar 1978 结婚，达拉斯读博时相识，同为 UNC 教授——spouse 关系入库；基金会二人共同创办 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q15118973 | ✅ |
| name_zh | 阿齐兹·桑贾尔 | ✅ |
| name_en | Aziz Sancar | ✅ |
| birth_date | 1946-09-08 | ✅ |
| death_date | 空（在世） | ✅ |
| nationality | Turkey（rank 0）/ United States（rank 1）/ Northern Cyprus（rank 2，era_note：2025-07-31 入籍，页面明载） | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | DNA repair（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| name_en | rank | name_zh |
|---|---|---|
| DNA repair | 0 | DNA 修复 |
| nucleotide excision repair | 1 | 核苷酸切除修复 |
| photolyase | 2 | 光复活酶 |
| circadian clock | 3 | 昼夜节律生物钟 |
| biochemistry | 4 | 生物化学 |

## 7. 社会关系入库清单

**师长 / 同行 / 共同得主 / 家人**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Claud Stan Rupert | 师→生（博士导师） | UT Dallas 博士导师，DNA 修复先驱，1977 光复活酶论文 |
| colleague | Dean Rupp | 无向 | 耶鲁五年在其实验室（任实验室技术员），完成 UvrABC/NER 机制阐明 |
| co-honored | Tomas Lindahl | 无向 | 2015 诺贝尔化学奖共同得主 |
| co-honored | Paul L. Modrich | 无向 | 2015 诺贝尔化学奖共同得主 |
| spouse | Gwen Boles Sancar | 无向 | 1978 结婚；达拉斯读博相识，同为 UNC 生物化学与生物物理学教授；共同创办 Aziz & Gwen Sancar 基金会 |

> **禁入库名单**（页面明载但不入库）：兄 Kenan Sancar（家庭成员）、表亲 Mithat Sancar（家庭成员且涉政治）；Orhan Pamuk（仅「同校友、先后诺奖」的比较性表述，非个人关系）；Rupert 之外的奖项命名人。 metadata.json 中无额外关系字段。

## 8. 奖项清单

- TÜBİTAK Science Award（1995）
- Presidential Young Investigator Award（NSF，Molecular Biophysics，1984）
- Member of the National Academy of Sciences（2005，首位土耳其籍院士）
- Vehbi Koç Award（2007）
- Nobel Prize in Chemistry（2015，与 Lindahl / Modrich 共享）
- 北塞浦路斯公民身份（2025-07-31，页面明载）
- Order of Cultural Ambassador of the Turkic World（TÜRKSOY，2025-01-19）
- 其他（metadata 载）：Shohrat Order、阿塞拜疆总统荣誉证书、American Academy of Arts and Sciences 会士、Turkish Academy of Sciences 荣誉会员

## 9. 机构清单

- 教育：Savur 家乡小学 → 伊斯坦布尔大学医学院（MD 1969）→ Johns Hopkins（TÜBİTAK 奖学金进修，约 1971–1973）→ University of Texas at Dallas（PhD 1977，Rupert 实验室）
- 任职：Savur 行医两段（毕业后与 1973 返美前）；Yale University 实验室技术员（约五年，Dean Rupp 实验室）；University of North Carolina at Chapel Hill（讲师起步 → Sarah Graham Kenan Professor；UNC Lineberger Comprehensive Cancer Center 成员）
- 共同创办：Aziz & Gwen Sancar 基金会；Carolina Türk Evi（UNC 校园旁土耳其中心）

## 10. 终审清单

- [ ] 生卒 1946-09-08 – 在世（全篇无卒日留白一致）；出生地 Savur, Mardin, Turkey
- [ ] 2015 三人共享（Lindahl / Modrich）表述准确；获奖理由 "for mechanistic studies of DNA repair" 口径准确
- [ ] 三人分工不串位：Sancar=NER/光复活、Modrich=错配修复、Lindahl=BER
- [ ] MD 1969 伊斯坦布尔 / PhD 1977 UT Dallas；耶鲁身份=实验室技术员
- [ ] 「首位土耳其籍 NAS 院士（2005）」与「第二位土耳其诺奖得主」两个表述不混淆
- [ ] 捐章 2016-05-19 Anıtkabir、复制品赠伊斯坦布尔大学
- [ ] 族裔/政治内容零出现；全篇无编造引语
- [ ] 正文采用桑格式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make pdf` 编译通过，0 错误、vbox≤10pt、hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Aziz_Sancar/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：装饰圆占位（页面无肖像），图注注明；正文插图仅用 1QNF 光复活酶结构模型
- [ ] 国籍：封面顶部明示土耳其 / 美国
- [ ] 引语核对：中文引号内不得出现族裔相关引语或编造原话
- [ ] 编译验证：`make distclean && make pdf`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt、hbox<50pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批（Modrich / Sauvage / Stoddart / Feringa）及桑格既有格式对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，执行者不改。
> **数据事实来源唯一**：`chemist/presentations/21th_century/pages/Aziz_Sancar/page.md`；页面无载的数据如实标注「页面无载」，禁止编造。
