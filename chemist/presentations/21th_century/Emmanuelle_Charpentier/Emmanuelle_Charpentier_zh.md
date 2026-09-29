# Emmanuelle Charpentier（埃玛纽埃勒·沙尔庞捷）立传提示词

> qid=Q17280087 · 1968-12-11 –（在世）· 法国 · 诺贝尔化学奖（2020，与 Jennifer Doudna 共享）· 本地数据源：`chemist/presentations/21th_century/pages/Emmanuelle_Charpentier/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：对齐 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}` 高斯式骨架——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像用本地 `images.txt` 首图 Charpentier in 2015 照或 2016 约克大学 Gairdner 演讲照；下载失败则装饰圆占位并在 Review 注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{scissors}\enspace 基因剪刀的铸造者\enspace·\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、全名（Emmanuelle Marie Charpentier）、国籍、出生地（Juvisy-sur-Orge）、教育（Pierre and Marie Curie University / Pasteur Institute）、博士导师（Patrice Courvalin）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「RNA — 分子剪刀」母题——离散圆点暗示 crRNA/tracrRNA 引导分子与 DNA 靶点的相遇。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配金色边框浅金底公式展示框（`\fcolorbox` + minipage），如 tracrRNA + crRNA → sgRNA 嵌合体 → Cas9 切割示意（文字链式，非公式）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Emmanuelle Marie Charpentier（中文惯称：埃玛纽埃勒·沙尔庞捷）
- **生卒**：1968-12-11 生于法国 Juvisy-sur-Orge（在世，卒日留白；★ frontmatter 另有噪声值 1968-01-01，以 infobox 与正文 12-11 为准）
- **国籍**：France（法国）
- **身份**：学者、微生物学家、遗传学家、生物化学家；2015 年起任柏林马克斯·普朗克感染生物学研究所所长（director）；2018 年创立并出任马克斯·普朗克病原体科学研究所（Max Planck Unit for the Science of Pathogens）创始所长
- **家庭**：父系祖父姓 Sinanian，是亚美尼亚人，于亚美尼亚种族灭绝期间逃亡法国，在马赛结识其妻——家族背景一笔带过，不作政治展开
- **教育轨迹**：
  - Pierre and Marie Curie University（巴黎居里夫妇大学，现索邦大学理学院）：BSc、MSc、PhD（生物化学、微生物学、遗传学）
  - Institut Pasteur 研究生（1992–1995），获研究博士学位
- **博士**：1995，《Antibiotic resistance in Listeria spp》——李斯特菌抗生素抗性的分子机制
- **博士导师**：Patrice Courvalin（巴斯德研究所）
- **研究领域**：微生物学、生物化学、遗传学——细菌免疫系统（CRISPR/Cas9）、RNA 调控、毒力因子

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **巴黎与巴斯德（1992–1995）**：居里夫妇大学本硕博，巴斯德研究所完成博士论文——李斯特菌抗生素抗性机制。
2. **横渡大西洋（1995–2002）**：巴斯德博士后（1995–1996）→ 洛克菲勒大学博士后（1996–1997，Elaine Tuomanen 实验室，研究肺炎链球菌移动遗传元件与万古霉素抗性）→ NYU 医学中心助理研究科学家（1997–1999，Pamela Cowin 实验室，小鼠毛发生长调控论文）→ St. Jude 儿童研究医院与 Skirball 研究所（1999–2002）。
3. **重返欧洲（2002–2009）**：维也纳大学微生物与遗传学研究所实验室主任（2002–2004）；**2004 年发表发现链球菌毒力因子合成调控 RNA 分子**；2006 年完成 habilitation 任 privatdozentin；2006–2009 任 Max F. Perutz Laboratories 实验室主任兼副教授。
4. **乌默奥岁月（2008–2013）**：瑞典 Umeå 大学 MIMS 实验室主任兼副教授（2008–2013 组长，2014–2017 访问教授）。
5. **德国建制（2013–2015）**：布伦瑞克亥姆霍兹感染研究中心与汉诺威医学院系主任兼 W3 教授；2014 年获 Alexander von Humboldt 教授席。
6. **马普所（2015–）**：任马普学会科学会员、马普感染生物学研究所所长；2016 年起洪堡大学荣誉教授；**2018 年创立马克斯·普朗克病原体科学研究所**任创始所长。
7. **破解细菌免疫（CRISPR/Cas9 机制）**：破译细菌免疫系统 CRISPR/Cas9 的分子机制，发现**非编码 RNA 成熟的新机制**——证明小 RNA tracrRNA 对 crRNA 的成熟至关重要（★ 沙尔庞捷的独门贡献）。
8. **2011 圣胡安之会**：2011 年在波多黎各圣胡安的学术会议上结识 Jennifer Doudna，开始合作。
9. **基因剪刀合铸（2012）**：两实验室合作证明 Cas9 可在任意指定 DNA 序列切刻；方法 = Cas9 + 易于构建的合成 "guide RNA"（crRNA 与 tracrRNA 的嵌合体）——CRISPR-Cas9 从此成为相对易用的基因组编辑工具，全球实验室用于编辑植物、动物与细胞系。
10. **从工具到革命**：CRISPR 使科学家得以编辑基因以探究其在健康与疾病中的作用，并开发有望比第一代基因疗法更安全有效的基因疗法——"革新了遗传学"（页面口径）。
11. **创业（2013）**：与 Shaun Foy、Rodger Novak 共同创立 CRISPR Therapeutics 与 ERS Genomics。
12. **2020 诺贝尔化学奖**：与加州大学伯克利分校美国生物化学家 Jennifer Doudna 共享，"for the development of a method for genome editing"（官方理由原句页面明载）；**这是首个仅由两位女性共享的科学类诺贝尔奖**（页面明载 "the first science Nobel Prize ever won by two women only"）。
13. **奖项大满贯**：突破奖（2015）、Louis-Jeantet（2015）、阿斯图里亚斯亲王奖（2015）、Gruber 遗传学奖（2015）、Otto Warburg Medal（2016）、L'Oréal-UNESCO 女科学家奖（2016）、Leibniz Prize（2016）、Canada Gairdner（2016）、唐奖（2016）、Paul Ehrlich 奖（2016）、Kavli 纳米科学奖（2018）、Wolf 医学奖（2020）、日本国际奖（2017）、Pour le Mérite（2017）、National Inventors Hall of Fame（2023）、英国皇家学会外籍院士（2024）等。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海蓝 deepsea） | `#16324F` | 细菌免疫学的沉静与精密（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（细菌免疫 badgeCRISPR） | `#1B7A43` | 绿——CRISPR/Cas9 / tracrRNA |
| 分类色 2（基因编辑革命 badgeEdit） | `#5B2A86` | 紫——sgRNA 嵌合体 / 基因组编辑 |
| 分类色 3（科研轨迹 badgePath） | `#B26A00` | 琥珀——巴斯德→纽约→维也纳→乌默奥→柏林 |
| 分类色 4（荣誉 badgeHonor） | `#7E1E23` | 绯红——突破奖 / Kavli / Nobel |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「guide RNA 与 DNA 靶点的配对」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Mirage** — Notan Nigres（文件 `music_audio/inspiring-electronic/04-5gcb94jhG1I-...Mirage (Audio).wav`，不要复制 wav）
- **风格**：电子氛围 / 冷冽而克制 / 渐显
- **匹配理由**：
  - "Mirage（海市蜃楼）"呼应"曾被认为不可能的细菌免疫系统成了可用的基因剪刀"——科幻照进现实的错位感；
  - 冷冽电子质感匹配 CRISPR 的分子精度与柏林马普所的当代感；
  - 渐显的结构匹配从 tracrRNA 的默默无闻到 2020 诺奖的高光时刻。
- **时长**：以曲目实际时长为准，ffmpeg `-shortest` 自动对齐 15 页 ≈ 105 秒。

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 基因剪刀的铸造者 / Emmanuelle Charpentier 1968– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/全名/国籍/出生地/教育/博士导师/领域/荣誉）
03  沙尔庞捷的轨迹 — 高斯式时间线（10 节点：1968→1995→1996→2002→2004→2008→2011→2015→2018→2020）
04  巴黎与巴斯德 (1992–1995) — 表格「机构|课题|结果」（居里夫妇大学→巴斯德→李斯特菌抗药性博士论文）
05  纽约五年 (1995–2002) — 表格「实验室|对象|发现」（Tuomanen 肺炎链球菌/万古霉素抗性→Cowin 小鼠毛发生长→St. Jude/Skirball）
06  维也纳与毒力 RNA (2002–2009) — 表格「阶段|课题|结果」+ 公式框：2004 毒力因子合成调控 RNA
07  乌默奥与 tracrRNA (2008–2011) — 表格「问题|方法|结果」+ 公式框：tracrRNA → crRNA 成熟机制（独门贡献）
08  2011 圣胡安之会 — 双人结构页：与 Doudna 相识并合作（会议/时点/分工按页面口径）
09  2012 基因剪刀合铸 — 表格「组件|方法|结果」+ 公式框：Cas9 + sgRNA（crRNA-tracrRNA 嵌合体）→ 指定位点切割
10  从工具到革命 — 表格「能力|应用|意义」（动植物/细胞系编辑→基因疗法希望→2013 创业 CRISPR Therapeutics/ERS Genomics）
11  马普所的建制 (2015–2018) — 高斯式「阶段|职务|意义」表格（感染生物学研究所所长→洪堡荣誉教授→病原体科学研究所创始所长）
12  2020 诺贝尔化学奖 — 共享页：与 Jennifer Doudna 共享同一理由；★ 首个仅两位女性共享的科学诺奖（页面明载）
13  遗产：可编辑的 genome — 四分类遗产盒 + 公式框：for the development of a method for genome editing
14  结尾 — 「读懂细菌的免疫系统，为人类铸一把剪刀。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 生日噪声 | frontmatter date_of_birth 双值 1968-12-11 / 1968-01-01——**取 12-11**（infobox 与正文一致）；"噪声值 01-01" 写入裁定 |
| 2020 共享结构 | 与 Jennifer Doudna **两人共享**同一理由 "for the development of a method for genome editing"（原句页面明载）——勿写三人或"各自独立" |
| 两位女性口径 | "the first science Nobel Prize ever won by two women only" 为页面明载——可写；勿扩展成"第 N 位女性诺奖得主"排行榜 |
| tracrRNA 归属 | **tracrRNA 对 crRNA 成熟必不可少**是沙尔庞捷实验室的独门发现；sgRNA 嵌合体是双方合作的成果——贡献归属勿混 |
| Doudna 身份 | 页面口径 "American biochemist Jennifer Doudna of the University of California, Berkeley"——对手方规范名 "Jennifer Doudna"（batch-11 互指一致） |
| 创业合作者 | 2013 年 CRISPR Therapeutics 与 ERS Genomics 与 **Shaun Foy、Rodger Novak** 共同创立——页面明载；但 Foy/Novak 无独立关系类型承载（商业联合创始人非科研关系）——**不入库**，正文可提 |
| 博士后归属 | Tuomanen（洛克菲勒 1996–1997）是博士后实验室负责人→advisor-student 弱师生；Cowin（NYU 1997–1999）是助理研究科学家阶段的实验室负责人→colleague——两类勿混 |
| 多奖共享方向 | 大量奖项与 Doudna 共享；Gabbay/Gairdner/Tang/Harvey 与 **Feng Zhang** 共享；BBVA 与 Doudna+**Francisco Mojica**；Kavli 与 Doudna+**Virginijus Šikšnys**——各奖共享名单勿张冠李戴 |
| 家族背景 | 父系祖父亚美尼亚裔、种族灭绝期间逃亡法国——页面实载的一句家庭背景，**中性一笔带过，不展开政治叙事** |
| 在世口径 | 1968-12-11 生，在世——卒日/享年一律留白 |
| 引语红线 | 本地 page.md 无第一人称直接引语——全文不得出现引号内"原话"；"revolutionized genetics" 等是页面叙述句，作转述不作引语 |
| metadata-only 禁入 | frontmatter `award_received` 超长清单中正文未逐条叙述者（如 Carus Medal 有载、Göran Gustafsson Prize 有载、Scheele Award 2019 有载——逐条核对）；memberships 列表仅为院籍不入关系；*STEM FEMMES* 戏剧、Isaacson 传记《The Code Breaker》为文化条目，正文可提不入关系 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q17280087 | ✅ |
| name_zh | 埃玛纽埃勒·沙尔庞捷 | ✅ |
| name_en | Emmanuelle Charpentier | ✅（页面标题规范名；清单 db_id 为空） |
| birth_date | 1968-12-11 | ✅（frontmatter 噪声值 1968-01-01 弃用） |
| death_date | （空，在世） | ✅ |
| nationality | France | ✅ |
| primary_occupation | microbiologist | ✅（intro 首列身份；biochemist/geneticist 入 occupations） |
| field_of_work | microbiology（person_field 细分：microbiology / biochemistry / genetics，带 rank） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**★红线：只收 page.md 正文或 infobox 明载的关系；metadata-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Patrice Courvalin | 师→生（博士导师） | 巴斯德研究所（1992–1995），李斯特菌抗药性机制博士论文 |
| advisor-student | Elaine Tuomanen | 师→生（博士后导师） | 洛克菲勒大学博士后（1996–1997），肺炎链球菌移动遗传元件与万古霉素抗性 |
| colleague | Pamela Cowin | 无向 | NYU 医学中心（1997–1999）实验室负责人，合作发表小鼠毛发生长调控论文 |
| co-honored | Jennifer Doudna | 无向 | 2020 诺贝尔化学奖共同得主（CRISPR-Cas9 基因组编辑方法）；2011 圣胡安会议结识后合作；另共享突破奖/阿斯图里亚斯/BBVA/日本国际奖/Wolf/National Inventors Hall of Fame 等 |
| co-honored | Francisco Mojica | 无向 | 2017 BBVA Foundation Frontiers of Knowledge Award 共同得主 |
| co-honored | Feng Zhang | 无向 | 2014 Gabbay Award、2016 Canada Gairdner 与 Tang Prize、2018 Harvey Prize 共同得主 |
| co-honored | Virginijus Šikšnys | 无向 | 2018 Kavli Prize in Nanoscience 共同得主 |

> Shaun Foy/Rodger Novak（创业联合创始人）非科研关系，**禁入库**；会员院籍（EMBO/Leopoldina/Royal Society 等）不入关系；对手方规范名 "Jennifer Doudna" 与 batch-11 互指一致（本 yaml 将为其建 stub，batch-11 以 UPD 回填 QID）。Šikšnys 用页面链接原形 Virginijus Šikšnys。

## 8. 奖项清单

- Theodor Körner Prize（2009）；Fernström Prize（2011）
- Alexander von Humboldt Professorship（2014）；Göran Gustafsson Prize for Molecular Biology（2014）
- Dr. Paul Janssen Award（2014，与 Doudna 共享）；Gabbay Award（2014，与 Feng Zhang、Doudna 共享）
- Breakthrough Prize in Life Sciences（2015，与 Doudna 共享）；Louis-Jeantet Prize for Medicine（2015）；Ernst Jung Prize（2015）；Princess of Asturias Awards（2015，与 Doudna 共享）；Gruber 遗传学奖（2015，与 Doudna 共享）；Carus Medal（2015）；Massry Prize（2015）；Hansen Family Award（2015）；*Time* 100（2015，与 Doudna）
- Otto Warburg Medal（2016）；L'Oréal-UNESCO 女科学家奖（2016）；Leibniz Prize（2016）；Canada Gairdner（2016，与 Doudna/Zhang）；Warren Alpert Prize（2016）；Paul Ehrlich 与 Ludwig Darmstaedter Prize（2016，与 Doudna）；Tang Prize（2016，与 Doudna/Zhang）；HFSP Nakasone Award（2016，与 Doudna）；法国荣誉军团骑士（2016）；Meyenburg Prize（2016）；Wilhelm Exner Medal（2016）；John Scott Award（2016）
- BBVA Frontiers of Knowledge Award（2017，与 Doudna/Mojica）；Japan Prize（2017，与 Doudna）；Albany Medical Center Prize（2017，与 Doudna/Marraffini/Mojica/Zhang）；Pour le Mérite（2017）；德国联邦十字勋章 Knight Commander's Cross（2019 前后按列表年份）
- Kavli Prize in Nanoscience（2018，与 Doudna/Šikšnys）；奥地利科学与艺术荣誉勋章（2018）；Bijvoet Medal（2018）；Harvey Prize（2018，与 Doudna/Zhang）
- Scheele Award（2019）
- Wolf Prize in Medicine（2020，与 Doudna）；Nobel Prize in Chemistry（2020，与 Doudna）
- National Inventors Hall of Fame（2023，与 Doudna）；Golden Plate Award（2024）
- 名誉博士：EPFL/KU Leuven/NYU（2016）、Umeå/Western Ontario/HKUST（2017）、UCLouvain/Cambridge/Manchester（2018）、McGill（2019）、Saskatchewan/Perugia（2024）、Ottawa（2026）
- 院士：EMBO（2014）、Leopoldina（2015）、Berlin-Brandenburg 与奥地利/瑞典皇家科学院（2016）、美国 NAS 外籍院士与法国科学院（2017）、Pontifical Academy（2021）、英国皇家学会外籍院士（2024）

## 9. 机构清单

- 教育：Pierre and Marie Curie University（BSc/MSc/PhD）；Institut Pasteur（研究生 1992–1995）
- 博士后/早期：Institut Pasteur（1995–1996）；Rockefeller University（1996–1997）；NYU Medical Center（1997–1999）；St. Jude Children's Research Hospital 与 Skirball Institute（1999–2002）
- 欧洲：University of Vienna（2002–2009，含 Max F. Perutz Laboratories）；Umeå University / MIMS（2008–2013，访问教授至 2017）；Helmholtz Centre for Infection Research（Braunschweig）与 Hannover Medical School（2013–2015）
- 马普：Max Planck Institute for Infection Biology 所长（2015–）；Max Planck Unit for the Science of Pathogens 创始所长（2018–）；Humboldt University 荣誉教授（2016–）
- 创业：CRISPR Therapeutics、ERS Genomics（2013，与 Shaun Foy/Rodger Novak 共同创立）

## 10. 终审清单

- [x] 生卒 1968-12-11（frontmatter 1968-01-01 噪声值弃用）/ 在世留白；出生地 Juvisy-sur-Orge
- [x] 博士导师 Patrice Courvalin（巴斯德）；博士后导师 Tuomanen 与同事 Cowin 两类区分
- [x] 2020 两人共享；理由原句 "for the development of a method for genome editing" 页面明载
- [x] "首个仅两位女性共享的科学诺奖" 页面明载口径
- [x] tracrRNA 发现归沙尔庞捷实验室；sgRNA 嵌合体归双方合作——贡献归属正确
- [x] 多奖共享名单（Doudna/Mojica/Zhang/Šikšnys）各归其位；Foy/Novak 不入库
- [x] 家族背景一句带过不展开；全文无杜撰引语
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Emmanuelle_Charpentier/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：优先本地 `images.txt` 中 2015 年照片或 2016 约克大学照；404 则装饰圆占位
- [ ] 国籍：封面顶部明示法国
- [ ] 引语核对：全文不得出现无法溯源的引号原话
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；分子名（tracrRNA、crRNA、Cas9、sgRNA）等宽或加粗统一
- [ ] 与 Sanger 及 21 世纪批次既有格式对齐；与 batch-11 Doudna 篇共享页口径互查
