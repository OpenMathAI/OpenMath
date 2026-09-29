# John Cornforth（约翰·康福思）立传提示词

> qid=Q135154 · 1917-09-07 – 2013-12-08 · 澳大利亚–英国化学家 · 20 世纪 · 诺贝尔化学奖（1975，与 Vladimir Prelog 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/John_Cornforth/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 桑格模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像下载后放 `images/`；Commons 404 则按 Rest delta API 回退，再失败用装饰圆占位并在 Review 记录）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 无声世界的立体化学大师\enspace·\enspace 澳大利亚 / 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍/公民身份、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「手性 / 镜像」母题——成对的圆点暗示酶催化反应中的立体化学替换。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir John Warcup Cornforth Jr.（中文惯称：约翰·沃克普·康福思；头衔 AC CBE FRS FAA，1977 年获 Knight Bachelor）
- **生卒**：1917-09-07 生于澳大利亚悉尼 → 2013-12-08 逝于英格兰 Sussex，享年 96
- **国籍**：澳大利亚（frontmatter 口径）；公民身份 Australian British（双籍）
- **身份**：澳大利亚–英国化学家；page.md 明载「唯一出生于新南威尔士州的诺贝尔奖得主」
- **家庭**：四个孩子中的次子；父 John Warcup Cornforth 为英格兰出生、牛津受教育的校长/教师；母 Hilda Eipper（1887–1969）曾为产科护士，是长老会传教士 Christopher Eipper 的孙女
- **听觉**：约 10 岁出现耳聋征兆，确诊耳硬化症（otosclerosis），20 岁完全失聪——这使他放弃原本想学的法律转向化学
- **教育轨迹**：
  - Sydney Boys High School：1933 年 16 岁以全班第一（dux）毕业；化学老师 Leonard ("Len") Basser 引导其从法律转向化学
  - 1934 入 University of Sydney：1937 年以一等荣誉 + University Medal 毕业（BSc）
  - 1939 与 Rita Harradence 各获一枚 1851 Research Fellowship（Royal Commission for the Exhibition of 1851，海外两年）
  - Oxford：St Catherine's College（Rita 在 Somerville College）；1941 双双获有机化学 D.Phil.
- **导师**：Robert Robinson（牛津博士导师；在牛津与其合作共 14 年）
- **博士论文**：《Synthesis of analogues of steroid hormones》（1941）
- **研究领域**：有机化学——酶催化反应的立体化学、甾体/萜类合成、胆固醇生物合成

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **悉尼医生之家以外的教师之子（1917）**：父亲是牛津出身的教师；10 岁起耳硬化症，20 岁完全失聪。
2. **失聪改写人生（1930s）**：原想学法律，因听觉障碍改学化学；对 Kroto 的 Vega 采访原话（page.md 明载可引）："I had to find something in which the loss of hearing would not be too severe a handicap...I chose chemistry..."——并说发现文献并非完全正确时先是震惊、继而是兴奋："Because I can set this right!"
3. **Sydney Boys High 与 Basser（1933）**：dux 毕业；化学老师 Basser 点燃其化学志向。
4. **悉尼双子星（1934–1939）**：与高一年级的 Rita Harradence 相识于悉尼大学；两人 1939 年各自独立赢得两枚 1851 Research Fellowship 之一。
5. **牛津与 Robinson（1939–1941）**：St Catherine's College；与 Robinson 激烈辩驳直到一方说服另一方；1941 双双获 D.Phil.；同年结婚。
6. **修烧瓶定情（本科时期）**：Rita 在二年级打碎 Claisen 烧瓶，Cornforth 以吹玻璃手艺修复——相识缘起（page.md 明载）。
7. **战时青霉素（1940s）**：在 Oxford 参与青霉素纯化与浓缩，测量青霉素产量（任意单位），参与撰写 *The Chemistry of Penicillin*。
8. **MRC/NIMR 甾体岁月（1946–）**：1946 夫妇离开牛津加入 MRC，在国家医学研究所（NIMR）继续甾醇（含胆固醇）合成。
9. **1951 双雄并立**：与 Robert Burns Woodward 同时完成非芳香甾体的首次全合成。
10. **Popják 与胆固醇生物合成**：在 NIMR 与 George Popják 合作阐明多聚异戊二烯与甾体的生物合成途径，1968 两人同获 Davy Medal。
11. **1975 诺贝尔化学奖**：与 Vladimir Prelog 共享；获奖方向是**酶催化反应的立体化学**——用氢同位素替换定位酶在底物链/环上替换了哪些氢原子，从而详述胆固醇的生物合成。
12. **Warwick 与 Sussex（1965–2013）**：1965–1971 任 Warwick 教授；1975 迁 University of Sussex 任 Royal Society Research Professor，研究活跃至去世。
13. **诺奖演讲谢妻（1975）**：获奖演说原话（page.md 明载可引）："Throughout my scientific career my wife has been my most constant collaborator..."——Rita 既是终生合作者，也替他弥合失聪带来的交流困难；2017-09-07 Google 以 Doodle 纪念其百岁诞辰；RACI 以 Cornforth Medal 奖励全澳最佳化学博士论文。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海蓝 deepocean） | `#123C5B` | 立体化学的严谨与深海般的沉静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（酶催化立体化学 badgeEnz） | `#2E6E8E` | 青蓝酶催化位点氢替换 |
| 分类色 2（甾体与胆固醇 badgeSteroid） | `#1B7A43` | 绿甾体全合成 / 胆固醇生物合成 |
| 分类色 3（青霉素与战时工作 badgePen） | `#D97B29` | 琥珀战时青霉素纯化 |
| 分类色 4（无声之声 badgeDeaf） | `#C0395B` | 玫瑰失聪 chemist 的生命叙事 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「手性镜像」的成对圆点。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Mirage** — Notan Nigres（`music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav`；不要复制 wav 文件，Makefile 引用即可）
- **风格**：迷离 / 内省 / 纪录片
- **匹配理由**：
  - "迷离" 呼应其完全失聪后于无声世界中以纸笔与分子模型"看见"立体化学的独特感知方式
  - "内省" 匹配其气质——把生理障碍转化为研究方向抉择的沉默坚毅
  - "纪录片" 匹配传记叙事——悉尼 → 失聪 → 牛津 Robinson 门下 → 青霉素 → 甾体 → 1975 诺奖 → Sussex
- **时长**：以实际曲目时长为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 无声世界的立体化学大师 / John Cornforth 1917–2013 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  康福思的一生 — 高斯式时间线（10 节点：1917→1933→1937→1941→1946→1951→1965→1975→1977→2013）
04  早年：失聪的悉尼少年 (1917–1933) — 表格「时间|事件|结果」（耳硬化症、法律→化学、dux）
05  悉尼大学与 1851 奖学金 (1934–1939) — 表格「时间|事件|结果」+ 与 Rita 相识/修烧瓶
06  牛津：Robinson 门下与战时青霉素 (1939–1946) — 表格「问题|方法|结果」+ 公式框：青霉素产量测定
07  NIMR：甾体全合成双雄并立 (1946–1951) — 表格「问题|方法|结果」（与 Woodward 同期完成非芳香甾体全合成）
08  酶催化反应的立体化学 (1950s–1975) — 表格「问题|方法|结果」+ 公式框：酶在底物上替换氢的位置定位 → 1975 诺奖
09  胆固醇生物合成与 Popják (1950s–1968) — 表格「挑战|方法|结果」+ 公式框：多聚异戊二烯→甾体途径 · Davy Medal
10  Rita：终生合作者 — 表格「人物|方向|结果」（1941 结婚 / 一子二女 / 诺奖演讲谢妻）
11  荣誉与晚期 — 高斯式「类别|代表|意义」表格（FRS 1953 / CBE 1972 / 皇家勋章 1976 / 爵士 1977 / Copley 1982 / AC 1991）
12  Sussex 岁月与遗产 — 高斯式流程图（1975 迁 Sussex → Royal Society Research Professor → 研究至去世 → 2017 Google Doodle）
13  遗产：立体化学的丰碑 — 四分类遗产盒 + 公式框：Cornforth reagent / Cornforth rearrangement（Known for 明载）
14  结尾 — 「在无声的世界里，分子用几何说话。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1975 获奖理由 | page.md 口径 "for his work on the stereochemistry of enzyme-catalysed reactions"（酶催化反应的立体化学）——勿泛化成"发明胆固醇合成"；Prelog 是另一半（有机分子与反应的立体化学） |
| 共享方向 | 1975 与 **Vladimir Prelog** 共享——勿写成独享；也勿把 Prelog 的 CIP 规则成就安到 Cornforth 头上 |
| 失聪表述 | 耳硬化症（otosclerosis），约 10 岁现征兆、20 岁完全失聪——勿写"先天失聪"或"老年失聪" |
| 转专业原因 | 因失聪放弃**法律**转向化学（Basser 引导）——勿写"因家境" |
| 原定领域 | 采访原话仅说明法律→化学；勿写"原想学医" |
| Robinson 关系 | 牛津**博士导师**且合作 14 年——勿写成"博士后同事" |
| Woodward 关系 | 1951 **同期（simultaneously）**完成非芳香甾体首次全合成——勿写"合作"或"竞争败北" |
| Davy Medal | 1968 与 **George Popják** 因多聚异戊二烯/甾体生物合成**共同**获得——勿写独得 |
| Australian of the Year | 1975 与少将 **Alan Stretton** 共享——与科学无关，建议一句带过或不写 |
| 国籍口径 | frontmatter 国籍 Australia；infobox Citizenship 为 Australian British——封面写"澳大利亚 / 英国"，勿只写其一 |
| 获奖时机构 | 1975 年获奖时已迁 **University of Sussex**（Royal Society Research Professor）——勿写 NIMR/Warwick |
| 引语红线 | 仅可引 page.md 明载两段：Kroto 采访（"I had to find something..." / "Because I can set this right!"）与诺奖演讲谢妻段；其余一律间接转述 |
| metadata 噪声 | frontmatter 奖项含 Flintoff medal / Portland Press Excellence in Science Award，正文 infobox 奖项清单未列年份——展示时以正文 infobox 年份为准，无年份奖项慎写 |
| 个人信念 | page.md 明载他是 sceptic 与 atheist——一句客观带过即可，不展开 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q135154 | ✅ |
| name_zh | 约翰·康福思 | ✅ |
| name_en | John Cornforth | ✅ |
| birth_date | 1917-09-07 | ✅ |
| death_date | 2013-12-08 | ✅ |
| nationality | Australia（+United Kingdom 变迁，rank 1） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分见下表，带 rank） | ✅ |

**person_field rank 表**：

| field | rank | 语义 |
|---|---|---|
| organic chemistry | 0 | 学科大类（frontmatter field_of_work） |
| stereochemistry | 1 | 酶催化反应立体化学（诺奖方向） |
| steroid synthesis | 2 | 甾体全合成（1951 双雄并立） |
| cholesterol biosynthesis | 3 | 胆固醇生物合成途径（Popják 合作） |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Robinson | 师→生（博士导师） | 牛津 D.Phil. 导师（1941），合作共 14 年 |
| spouse | Rita Harradence | 无向 | 1941 结婚，化学家，终生科学合作者 |
| colleague | George Popják | 无向 | NIMR 胆固醇合作者，1968 Davy Medal 共同得主 |
| colleague | Robert Burns Woodward | 无向 | 1951 同期完成非芳香甾体首次全合成 |
| influence | Hermann Emil Fischer | 无向 | Cornforth 自述尤其受其著作影响 |
| co-honored | Vladimir Prelog | 无向 | 1975 诺贝尔化学奖共同得主 |

> **禁入库名单（metadata-only 或非个人关系）**：Howard Florey（青霉素工作背景提及）、Alan Stretton（Australian of the Year 共享）、Harry Kroto（采访者）、Christopher Eipper（外曾祖辈传教士）、Leonard Basser（中学教师）。

## 8. 奖项清单

- Corday–Morgan Medal（1953）
- Fellow of the Royal Society，FRS（1953）
- Davy Medal（1968；与 George Popják 共同）
- Ernest Guenther Award（1969）
- Commander of the Order of the British Empire，CBE（1972）
- Nobel Prize in Chemistry（1975；与 Vladimir Prelog 共享）
- Australian of the Year（1975；与 Alan Stretton 共享）
- Royal Medal（1976）
- Knight Bachelor（1977）；University of Sydney 荣誉 D.Sc.（1977）；Australian Academy of Science Corresponding Fellow（1977）
- Royal Netherlands Academy of Arts and Sciences 外籍成员（1978–）
- Copley Medal（1982）
- Companion of the Order of Australia，AC（1991）
- Centenary Medal（2001）
- 1851 Research Fellowship（1939）；University Medal（Sydney，1937）

## 9. 机构清单

- 教育：Sydney Boys High School（–1933）；University of Sydney（1934–1937，BSc 一等荣誉 + University Medal）；St Catherine's College, Oxford（D.Phil. 1941）
- 任职：University of Oxford（–1946，战时青霉素）；MRC / National Institute for Medical Research（1946–）；University of Warwick 教授（1965–1971）；University of Sussex（1975–，Royal Society Research Professor，研究至去世）
- 命名纪念：RACI Cornforth Medal（全澳最佳化学博士论文奖）；2017-09-07 Google Doodle 百岁诞辰

## 10. 终审清单

- [ ] 生卒 1917-09-07 / 2013-12-08，享年 96，出生地 Sydney、去世地 Sussex
- [ ] 1975 与 Prelog **共享**；获奖理由为"酶催化反应的立体化学"口径准确
- [ ] 失聪：耳硬化症、约 10 岁起、20 岁完全失聪；法律→化学转向表述准确
- [ ] Robinson=博士导师（合作 14 年）；Woodward=同期全合成非合作；Davy Medal=与 Popják 共同
- [ ] 引语仅两段（Kroto 采访、诺奖谢妻），均可在 page.md 原文找到
- [ ] 荣誉年份逐一对照 §8；frontmatter 无年份奖项不进时间线
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/John_Cornforth/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认肖像就位（Commons/Wikipedia REST API；失败则装饰圆占位并记录）
- [ ] **国籍**：封面顶部明示"澳大利亚 / 英国"
- [ ] **引语核对**：仅两段明载引语，其余不得出现引号"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改动该文件。
