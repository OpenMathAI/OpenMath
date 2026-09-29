# Peter Debye（彼得·德拜）立传提示词

> qid=Q103835 · 1884-03-24 – 1966-11-02 · 荷兰裔美国物理学家/物理化学家 · 20 世纪 · 诺贝尔化学奖（1936，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Peter_Debye/`（page.md + metadata.json + page.html + images.txt）

---

## 0. 正文形式说明（参考 Frederick Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。**注意：本地 images.txt 无真实肖像**（仅 Solvay 1933 签名图与马斯特里赫特纪念碑照）——执行时先试 Wikipedia REST API `page/summary` 查 infobox 原图（"Debye in 1912" 应存在）；404 则用**装饰圆占位**（勿把签名图当肖像）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{magnet}\enspace 分子世界的度量者\enspace·\enspace 荷兰 / 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Petrus Josephus Wilhelmus Debije）、国籍（Netherlands → United States 1946）、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「偶极子」母题——成对的正负圆点错落，暗示分子电偶极矩。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——偶极矩页写偶极矩单位 debye（D）与偶极矩-温度-介电常数关系式示意，德拜模型页写低温比热 T³ 律示意，德拜–休克尔页写离子氛屏蔽示意。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Peter Joseph William Debye（出生名 Petrus Josephus Wilhelmus Debije，荷兰语发音；后改用英语化名字）
- **生卒**：1884-03-24 生于荷兰马斯特里赫特 → 1966-11-02 逝于美国纽约州伊萨卡（第二次心脏病发作），享年 82；葬于伊萨卡 Pleasant Grove Cemetery
- **国籍**：Netherlands → United States（1946 入籍；双重口径荷兰裔美国人）
- **身份**：物理学家、物理化学家；偶极矩、X 射线与聚合物研究的开创者；分子偶极矩单位 debye（D）以他命名
- **家庭**：1913 娶 Mathilde Alberer（柏林时期寄宿公寓房东之女，随他改国籍）；子 Peter P. Debye（1916–2012，物理学家，与父亲部分研究合作，其子亦是化学家）、女 Mathilde Maria（1921–1991）；忠诚的天主教徒，坚持全家上教堂；爱钓鳟鱼、园艺、种仙人掌、雪茄
- **教育轨迹**：1901 入亚琛工业大学（RWTH Aachen）→ 1905 电气工程首个学位 → 随 Sommerfeld 转慕尼黑 → 1908 博士（辐射压）
- **博士**：1908，慕尼黑，论文关于辐射压（radiation pressure）；1910 年以比 Planck 本人更简洁的方法重新推导普朗克辐射公式（Planck 认可）
- **导师**：Arnold Sommerfeld（亚琛至慕尼黑；Sommerfeld 自称"最重要的发现是 Peter Debye"）
- **研究领域**：物理化学、理论物理、X 射线衍射、聚合物科学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **马斯特里赫特的工程师少年（1884–1905）**：荷兰边境小城出身，亚琛工大电气工程起步——应用数学功底由此而来；1907 年发表涡流问题的优雅解。
2. **Sommerfeld 门下（1905–1908）**：随师转慕尼黑任助手，1908 以辐射压获博士——Sommerfeld 晚年自称其最重要的科学发现是 Debye（page.md 明载引语）。
3. **更简的普朗克公式（1910）**：重新推导普朗克辐射公式，Planck 亲认更简洁——理论功力一举成名。
4. **偶极矩（1912）**：把电偶极矩概念用于不对称分子的电荷分布，建立偶极矩-温度-介电常数关系式——分子偶极矩单位由此定名 **debye (D)**；同年把 Einstein 比热理论延拓到低温（含低频声子贡献）——**Debye model**（固体比热的德拜 T³ 律）。
5. **椭圆轨道与 X 射线（1913–1915）**：延拓 Bohr 原子结构理论引入椭圆轨道（与 Sommerfeld 同期）；与助手 Paul Scherrer 计算温度对晶体 X 射线衍射图样的影响——**Debye–Waller factor**；Debye–Scherrer 粉末衍射法由此得名。
6. **流徙的教授（1911–1934）**：苏黎世大学（接 Einstein 赴布拉格后的教席）→ 乌特勒支 → 哥廷根 → ETH 苏黎世 → 莱比锡 → 柏林；1914-05 当选荷兰皇家艺术与科学院成员。
7. **哥廷根的偶极矩测量（1918）**：其指导下的 Luise Lange 在哥廷根首次测得溶液中分子的偶极矩。
8. **Debye–Hückel 理论（1923）**：与助手 Erich Hückel 改进 Arrhenius 电解质溶液电导理论——强电解质离子氛模型，仍为理解电解质溶液的重大进展；1926 年 Onsager 进一步改进（Debye–Hückel–Onsager）；同年提出 Compton 效应的理论解释。
9. **1936 诺贝尔化学奖**：官方理由 "for his contributions to the study of molecular structure"（分子结构研究）——主要指偶极矩与 X 射线衍射工作；**独享**；此前已获 Rumford Medal（1930）、Faraday Lectureship Prize（1933）、Lorentz Medal（1935）。
10. **柏林与凯撒·威廉研究所（1934–1939）**：继 Einstein 出任柏林凯撒·威廉物理研究所所长（设施在其任内建成）；1936 起兼柏林大学理论物理教授；1937–1939 任德国物理学会（DPG）主席。
11. **赴美与康奈尔（1939–1950）**：1939 赴康奈尔讲 Baker Lectures；1940 年初离开德国（1 月热那亚登船，2 月初抵纽约），6 月受聘康奈尔任化学系主任十年；1946 入美国籍；1952 退休仍研究至终——晚年以光散射法测定聚合物分子量（源自早年 X 射线散射），战时合成橡胶研究延至蛋白质等大分子。
12. **争议与平反（2006–2008）**：2006 年 Rispens 著作指其在纳粹时期"清洗"犹太科学家（DPG 1938-12-09 通知信）；康奈尔化学系 2006 报告"未发现支持纳粹同情者指控的证据"；NIOD 报告称其为"生存的模糊术"；2008 Terlouw 委员会结论——非党员、非反犹、未协助纳粹战争机器、亦非抵抗英雄，建议保留德拜命名（Utrecht 接受；Maastricht 未接受但奖项继续）；1938–1939 曾冒险协助犹太同事 Lise Meitner 出逃；1950 年获 Max Planck 奖章时 Einstein、Meitner、Franck 无人抗议，Einstein 还重新参与投票支持他。
13. **命名遗产**：debye（偶极矩单位）、Debye model / Debye frequency / Debye relaxation / Debye shielding / Debye length / Debye sheath / Debye–Hückel equation / Debye–Waller factor / Debye–Scherrer method / Lorenz–Mie–Debye theory / 小行星 30852 Debye / 月球背面 Debye 陨石坑 / 马斯特里赫特 Debye 广场纪念碑（偶极矩雕塑）。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青蓝 deepblue） | `#1E3A5F` | 精密测量的冷静蓝——偶极矩与晶格的秩序感（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（偶极矩 badgeDipole） | `#2E5A9E` | 蓝 debye 单位 / 介电常数 |
| 分类色 2（X 射线与晶体 badgeXray） | `#8E44AD` | 紫 Debye–Scherrer / Debye–Waller |
| 分类色 3（溶液与电解质 badgeIon） | `#1B7A43` | 绿 Debye–Hückel / 离子氛 |
| 分类色 4（聚合物与大分子 badgePolymer） | `#D97B29` | 琥珀光散射测分子量 / 合成橡胶 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（正负成对的圆点，四档大小错落），呼应「偶极子」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Really Slow Motion（路径 `music_audio/inspiring-electronic/15-w6kT1BfvETI-...Shine Like The Sun (Epic Beautiful Uplifting).wav`）
- **风格**：上扬 / 明亮 / 壮丽
- **匹配理由**：
  - "明亮" 匹配 X 射线与光散射——以光测量物质结构的一生
  - "上扬" 匹配其流徙七城终成一代宗师的轨迹与康奈尔晚期的二次学术生命
  - "壮丽" 呼应其理论跨度的宏大——从辐射压到聚合物，横跨物理学与化学
- **时长**：执行时核对，不足 15 页 × 7 秒则循环或 ffmpeg 对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 分子世界的度量者 / Peter Debye 1884–1966 + 四色 badge + 右上头像 + 国籍行（荷兰/美国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  德拜的一生 — 高斯式时间线（10 节点：1884→1905→1908→1912→1916→1923→1934→1936→1940→1966）
04  早年：亚琛到慕尼黑 (1884–1908) — 表格「时间|事件|结果」（Sommerfeld 门下 / 辐射压博士）
05  更简的普朗克公式 (1910) — 表格「人物|方法|结果」+ 公式框：普朗克辐射公式两种推导对照
06  偶极矩与德拜模型 (1912) — 表格「问题|方法|结果」+ 公式框：debye 单位与比热 T³ 律
07  X 射线与晶体 (1914–1918) — 表格「问题|合作者|结果」+ Debye–Scherrer 粉末法 / Debye–Waller factor
08  Debye–Hückel 理论 (1923) — 表格「问题|方法|结果」+ 公式框：离子氛屏蔽示意 + Onsager 1926 改进
09  1936 诺贝尔化学奖 — 官方理由原句 "for his contributions to the study of molecular structure" + 表格「奖项|年份|意义」
10  柏林岁月 (1934–1939) — 表格「职务|时间|背景」（凯撒·威廉研究所 / DPG 主席）
11  康奈尔与聚合物 (1939–1966) — 高斯 FFT 页式流程图（Baker Lectures → 化学系主任 → 入籍 1946 → 光散射测分子量）
12  争议与平反 (2006–2008) — 表格「报告|结论|结果」（康奈尔 2006 / NIOD / Terlouw 2008 / Meitner 1938 出逃 / 1950 Planck 奖章无人抗议）
13  遗产：以德拜命名的世界 — 四分类遗产盒 + 命名清单（debye 单位 / 模型族 / 小行星与月球坑）
14  结尾 — 「给分子以量度，给结构以名字。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1936 诺奖理由 | 官方措辞 "for his contributions to the study of molecular structure"（分子结构研究贡献，主要指偶极矩与 X 射线衍射）——**独享**；勿写成"因 Debye–Hückel 理论获奖" |
| 本名拼写 | 出生名 Petrus Josephus Wilhelmus **Debije**（荷兰文 ij）；英语化 **Debye**——身份页两写并注 |
| Sommerfeld 引语 | "his most important discovery was Peter Debye" 为 Sommerfeld 之言，page.md 明载——引用时注明归属，勿写成德拜自述 |
| 普朗克公式 | 1910 德拜以"Planck 本人认可更简洁"的方法重推——勿写成"德拜修正普朗克错误" |
| 国籍口径 | 出生荷兰；1940 赴美、**1946** 入美国籍；infobox Citizenship 双列——封面写"荷兰 / 美国" |
| 纳粹争议（★ 本篇最大雷区） | 2006 Rispens 指控（DPG 1938-12-09 "Heil Hitler" 信）与后续调查必须**平衡呈现**：康奈尔 2006 报告（未发现支持纳粹同情者/合作者/反犹指控的证据）、NIOD 2007（"生存的模糊术"）、Terlouw 2008（非党员/非反犹/非合作者/亦非抵抗英雄，建议保留命名）——禁止单边定性；同时如实写 1938–1939 协助 Meitner 出逃与 1950 Planck 奖章时 Einstein/Meitner/Franck 无人抗议（Einstein 还投票支持）；"2010 Reiding MI6 间谍假说"仅一句"有争议假说"，勿展开 |
| DPG 信 | 德拜 1938 信是"extraordinarily unpleasant fact, forming a dark page"（Terlouw 委员会语）——保留这一定性，同时写 Reich 大学教师联盟抱怨 DPG"仍然太眷恋犹太人"的反向证据 |
| von Laue | 反纳粹的 Max von Laue 认可了 DPG 主席信（Rechenberg 1988 文，page.md 转述）——作为平衡证据写入，不写 Laue"被迫" |
| 家庭 | 妻 Mathilde Alberer（房东之女）；子 Peter P. Debye 是物理学家并合作研究；1939 滞美的儿子、留守柏林的女儿与 official leave of absence 细节只在争议节需要时简述 |
| 同名区分 | Debye（单位）/ Debye model / Debye shielding / Debye length / Debye sheath / Debye relaxation / Debye frequency / Debye function / Debye–Hückel / Debye–Waller / Debye–Scherrer / Lorenz–Mie–Debye / 30852 Debye / 月球 Debye 坑——命名清单页集中呈现，勿混入他人（如 Mie、Lorenz 各为独立人物） |
| 引语红线 | 可用引语仅两条：获奖理由原句、"his most important discovery was Peter Debye"（Sommerfeld 归属）；Terlouw 委员会定性句可转述，中文引号内原话不得超出 page.md 白名单 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q103835 | ✅（回填至既有 stub #2258） |
| name_zh | 彼得·德拜 | ✅ |
| name_en | Peter Debye | ✅（用 db_name_en 精确形式） |
| birth_date | 1884-03-24 | ✅ |
| death_date | 1966-11-02 | ✅ |
| nationality | Netherlands（rank 0）+ United States（rank 1，1946 入籍） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：physical chemistry / theoretical physics / X-ray diffraction / polymer science，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 门生**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Arnold Sommerfeld | 师→生（博士导师） | 亚琛至慕尼黑；1908 辐射压博士 |
| advisor-student | Lars Onsager | 德拜→学生 | infobox doctoral students；1926 改进 Debye–Hückel 方程 |
| advisor-student | Paul Scherrer | 德拜→学生 | infobox；1914–1915 合作 X 射线温度效应（Debye–Waller factor） |
| advisor-student | Fritz Zwicky | 德拜→学生 | infobox doctoral students |
| advisor-student | George K. Fraenkel | 德拜→学生 | infobox doctoral students |
| advisor-student | Luise Lange | 德拜→学生 | 1918 哥廷根首次测得溶液分子偶极矩 |
| colleague | Erich Hückel | 无向 | 1923 共创强电解质 Debye–Hückel 理论 |
| colleague | Lise Meitner | 无向 | 1938–1939 冒险协助其越境出逃纳粹迫害 |
| colleague | Max von Laue | 无向 | 反纳粹立场却认可 DPG 主席信（Rechenberg 文转述）；1950 德拜获 Planck 奖章时未反对 |
| other | Albert Einstein | 无向 | 德拜先后接任其苏黎世教席与凯撒·威廉物理研究所所长；2006 争议中涉及 Einstein 1940 信件往来（康奈尔/FBI 调查口径）；1950 年投票支持德拜获 Planck 奖章 |
| other | Martinus J. G. Veltman | 无向 | 曾为 Rispens 书作序，2006-05 公开撤回序言并要求乌特勒支撤销研究所更名决定（2006 争议事件当事人） |

**家庭**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Mathilde Alberer | 无向 | 1913 年结婚，房东之女 |
| parent-child | Peter P. Debye | 德拜→孩子 | 子，物理学家，与父合作研究 |

> **禁入库名单**（metadata.json-only 或页面无实质载述）：Mathilde Maria（女儿，仅出生年载述）、Paul Rosbaud（2010 间谍假说人物，假说有争议）、Hermann Göring（仅" acquaintances"背景句）、Friedrich Drescher-Kaden（Philip Ball 反驳例）、Sybe Rispens（书作者）、Jan Terlouw / Gijs van Ginkel / Dieter Hoffmann / Mark Walker / Helmut Rechenberg / Jurrie Reiding / Philip Ball / Cees Andriesse（争议节作者与官员）、Svante Arrhenius（理论改进对象非关系）、Niels Bohr（理论延拓对象）、Max Planck（公式重推对象）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1936，独享）
- Rumford Medal（1930，比热与 X 射线光谱学）
- Faraday Lectureship Prize（1933）
- Lorentz Medal（1935）
- Franklin Medal（1937）
- Willard Gibbs Award（1949）
- Max Planck Medal（1950，DPG 最高奖；Einstein 重新参与投票支持）
- William H. Nichols Medal（1961）
- Priestley Medal（1963）
- National Medal of Science（1965）
- Polymer Physics Prize；ACS Award in Colloid Chemistry；Mendel Medal；Order of the Netherlands Lion；Commander of the Order of Leopold II
- 荷兰皇家艺术与科学院成员（1914）；美国哲学会（1936）与美国国家科学院（1947）院士；ForMemRS；AAAS 国际荣誉会士（1927）；Alpha Chi Sigma 名人堂（1982，追授）；Guthrie Lecture

## 9. 机构清单

- 教育：RWTH Aachen（1901–1905，电气工程）→ Ludwig-Maximilians-Universität München（PhD 1908）；后与 ETH Zurich 亦有渊源（任教）
- 任职：University of Zurich（1911–12，接 Einstein 教席）→ Utrecht（1912–14）→ Göttingen（1914–20）→ ETH Zurich（1920–27）→ Leipzig（1927–34）→ University of Berlin / Kaiser Wilhelm Institute for Physics 所长（1934–39；1936 起兼理论物理教授）→ Cornell University（1940–50，化学系主任十年；1952 退休）
- 学术服务：Deutsche Physikalische Gesellschaft 主席（1937–1939）；荷兰皇家艺术与科学院成员（1914）
- 命名遗产：马斯特里赫特 Debye 广场（偶极矩雕塑纪念碑）；小行星 30852 Debye；月球背面 Debye 陨石坑；UCSD 之外多所大学讲座与奖项以他命名（Peter Debye Prize, Maastricht——Terlouw 委员会建议继续颁发）

## 10. 终审清单

- [ ] 生卒 1884-03-24 / 1966-11-02，享年 82，出生地 Maastricht、去世地 Ithaca
- [ ] 1936 独享、理由 "for his contributions to the study of molecular structure" 原句表述准确
- [ ] 本名 Debije / Debye 双写；国籍双列（Netherlands + United States 1946）
- [ ] Sommerfeld 引语归属正确；1910 普朗克公式"更简"表述准确
- [ ] 门生五人（Onsager/Scherrer/Zwicky/Fraenkel/Luise Lange）与 Hückel colleague 口径准确
- [ ] 2006–2008 争议三报告平衡呈现，无单边定性；Meitner 出逃与 1950 奖章证据写入
- [ ] 引语仅两条白名单且可在 page.md 溯源
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Peter_Debye/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：REST API 查 "Debye in 1912" infobox 原图；404 则装饰圆占位（勿用签名图）
- [ ] **国籍**：封面顶部明示"荷兰 / 美国"
- [ ] **引语核对**：两条白名单引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐
