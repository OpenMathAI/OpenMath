# John E. Walker（约翰·E·沃克）立传提示词

> qid=Q235184 · 1941-01-07 生（在世）· 英国 · 诺贝尔化学奖（1997，与 Boyer 共享一半、与 Skou 共享同年另一半）· 英国生物化学家
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/John_E._Walker/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面头像**：右上角肖像位。`images.txt` 为空、本地无真实肖像 URL——先用装饰圆占位（主色渐变圆 + 姓名首字母），可尝试 Wikipedia REST API `page/summary` 查 infobox 原图名（页面图注为 "Walker in 2018"），失败则保留装饰圆，**不得使用其他人物照片冒充**。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace ATP 合酶的分子发动机\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像位 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地（在世则标注"在世"）、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「分子旋转催化」母题——三个不同构象的催化位点如旋转引擎的三个冲程。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（如 F1-ATPase 三催化位点、ADP + Pi → ATP）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir John Ernest Walker（中文惯称：约翰·欧内斯特·沃克；头衔 Sir、FRS、FMedSci）
- **生卒**：1941-01-07 生于英格兰西约克郡哈利法克斯（Halifax, West Riding of Yorkshire）——**在世**，卒年留白
- **国籍**：United Kingdom（英国）
- **身份**：生物化学家（1997 诺贝尔化学奖得主）；2015 年起任剑桥 MRC 线粒体生物学单元荣休主任与教授、Sidney Sussex College 院士
- **家庭**：父 Thomas Ernest Walker 为石匠，母 Elsie Lawton 为业余音乐家；在乡村环境中与两个妹妹（Judith、Jen）一同长大；1963 年娶 Christina Westcott（infobox 注其 2023-11-17 去世），育有二女
- **教育轨迹**：
  - Rastrick Grammar School（Rastrick High School）；校内运动健将，最后三年专攻物理科学与数学
  - 牛津 St Catherine's College，化学 BA（**三等学位**——正文原文明载 "3rd class Bachelor of Arts degree in chemistry"）
- **导师**：Edward Abraham（牛津，1965 年起研究肽类抗生素）
- **博士**：1969 年获博士学位（infobox 论文条目作 1970；正文口径 1969，**取 1969**），论文 *Studies on naturally occurring peptides*
- **研究领域**：生物化学——线粒体膜蛋白、线粒体基因组、ATP 合酶晶体学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **石匠之子（1941）**：哈利法克斯乡村环境、石匠与业余音乐家的家庭——朴实出身与科学之路上没有捷径的起点。
2. **三等学位的化学家**：牛津 St Catherine's College 化学 BA 仅得三等——却在此后走得更远（如实呈现，不作评价性修辞）。
3. **牛津肽类抗生素（1965–1969）**：随 Edward Abraham 研究天然肽类抗生素，1969 年获博士学位；期间对分子生物学的新进展产生兴趣。
4. **漂泊的博士后岁月（1969–1974）**：1969–1971 威斯康星大学麦迪逊分校；1971–1974 赴法国——两段海外经历。
5. **Sanger 的邀请（1974）**：在剑桥一个研讨会上结识 Fred Sanger，由此受邀加入 MRC 分子生物学实验室（LMB），成为长期任职；LMB 同侪中有 DNA 双螺旋发现者 Francis Crick。
6. **从蛋白质序列到线粒体遗传密码**：先分析蛋白质序列，继而揭示线粒体中**修饰遗传密码**的细节。
7. **转向膜蛋白（1978）**：决意把蛋白质化学方法用于膜蛋白——表征线粒体膜蛋白的亚基组成与线粒体基因组的 DNA 序列。
8. **F1-ATPase 晶体结构（1994）**：与晶体学家 Andrew Leslie 合作，对牛心线粒体 F1-ATPase（ATP 合酶催化区）作里程碑式晶体学研究——非对称中心 stalk 的位置使三个催化位点呈现**三种不同构象**。
9. **支持 Boyer 的旋转催化**：该结构支持 Paul Boyer 提出的 ATP 合酶 binding change 机制与旋转催化假说之一——晶体结构为机制假说提供了实证。
10. **1997 诺贝尔化学奖**：与 Paul D. Boyer 共享一半（"for their elucidation of the enzymatic mechanism underlying the synthesis of adenosine triphosphate"——页面对该半项理由的表述）；同年另一半由 Jens C. Skou 以 Na+/K+-ATPase 的发现**独享**（与 Boyer/Walker 研究无关）。
11. **ATP 合酶结构库**：此后 Walker 与同事产出了 PDB 中线粒体 ATP 合酶**大部分**晶体结构——含过渡态、结合抑制剂与抗生素的结构。
12. **传承**：在 LMB 与 MRC 线粒体生物学单元受训的学生与博后纷纷独立——Leonid Sazanov（博士后，现 ISTA）、Daniela Stock（博士后，现 Sydney）；其门下培养出测定细菌复合物 I 晶体结构与线粒体复合物 I、液泡型 ATPase 冷冻电镜图谱的科学家。
13. **荣誉迟来而厚重**：EMBO Member（1984）→ FRS（1995）→ 诺贝尔奖（1997）→ 爵士（1999，表彰对分子生物学的贡献）→ 荷兰皇家艺术与科学院外籍院士（1999）→ FMedSci（2011）→ Copley Medal（2012）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深酒红 claret） | `#8A1E2D` | 牛心线粒体与血红组织的深红（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（ATP 合酶 badgeATP） | `#B4552E` | 琥珀红 F1-ATPase / 旋转催化 |
| 分类色 2（线粒体 badgeMito） | `#6E2B4F` | 紫红线粒体基因组 / 修饰密码 |
| 分类色 3（膜蛋白 badgeMem） | `#2F5D73` | 青蓝膜蛋白亚基组成 |
| 分类色 4（传承 badgeTrain） | `#3E6B4A` | 绿门生与结构库传承 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），三个一组呼应 F1 的三个催化位点。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**With Me** — Alex-Productions（清单指定文件 `83-DXAblXgCK-k-With-Me.wav`；如目录内尚无软链则从 music_audio 软链，不要复制 wav）
- **风格**：沉稳 / 陪伴感 / 长期主义
- **匹配理由**：
  - "With Me" 的陪伴感匹配 Andrew Leslie 等长期合作者与 LMB 数十年如一日的团队研究
  - 沉稳气质匹配晶体学工作本身——一帧结构、数年打磨
  - 长期主义匹配三等学位 → 肽抗生素 → 线粒体 → ATP 合酶 → 诺奖 → 结构库的一生慢线
- **时长**：以曲目实际时长为准（> 15 页 × 7 秒即由 ffmpeg `-shortest` 自动对齐）

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — ATP 合酶的分子发动机 / John E. Walker 1941– + 四色 badge + 右上头像位 + 国籍行
02  身份信息页（★ 必做）— 左头像位 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/在世/领域/荣誉）
03  沃克的一生 — 高斯式时间线（10 节点：1941→1965→1969→1971→1974→1978→1994→1997→1999→2012）
04  早年：石匠之子与三等学位 (1941–1965) — 表格「时间|事件|结果」
05  牛津与漂泊：肽抗生素与博士后 (1965–1974) — 表格「时间|事件|结果」
06  Sanger 的邀请与 LMB (1974–1978) — 表格「人物|转折|结果」
07  线粒体：膜蛋白与修饰密码 (1978–1990s) — 表格「问题|方法|结果」
08  F1-ATPase 晶体结构 (1994) — 表格「问题|方法|结果」+ 公式框：三催化位点三构象
09  1997 诺贝尔化学奖 — 表格「得主|贡献|份额」+ 公式框：ADP + Pi ⇌ ATP（页面对获奖理由的表述口径）
10  ATP 合酶结构库与传承 — 表格「人物|方向|结果」（Sazanov / Stock / 结构库）
11  荣誉与年表 — 高斯式「类别|代表|意义」表格（含 itemize 荣誉清单：FRS 1995、爵士 1999、Copley 2012）
12  MRC 线粒体生物学单元 — 高斯 FFT 页式流程图（LMB 长期任职 → 1998 更名 MBU 脉络依页面实载 → 荣休主任）
13  遗产：把发动机看清 — 四分类遗产盒 + 公式框：PDB 结构数示意
14  结尾 — 「细胞能量的分子发动机，从此有了原子的形状。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1997 份额结构 | Boyer 与 Walker **共享一半**（ATP 合酶酶学机制）；Skou **独享另一半**（Na+/K+-ATPase，与前者研究无关）——勿写成三人平分或"共同一项" |
| 1997 获奖理由口径 | 页面对 Boyer/Walker 半项的表述为 "for their elucidation of the enzymatic mechanism underlying the synthesis of adenosine triphosphate"；Skou 半项页面仅括注 "(Discovery of the Na+/K+-ATPase)"，**勿替 Skou 补写官方全句** |
| 博士年份 | 正文口径 1969（"received his Doctor of Philosophy degree in 1969"），infobox 论文条目作 1970——**取正文 1969**，年份冲突在脚注注明 |
| 学位等级 | 牛津化学 BA 为**三等**（"3rd class"）——正文明载，如实呈现；勿美化或删改 |
| 在世口径 | 1941 年生、**在世**：封面与身份页卒年留白，享年不写 |
| Sanger 称谓 | 正文作 "Fred Sanger"（即 Frederick Sanger，Q151564）；入库对手方用库内规范名 Frederick Sanger |
| Boyer 的角色 | Boyer 提出 binding change / 旋转催化**假说**，Walker 的结构**支持**该机制——勿写"Walker 提出旋转催化" |
| 配偶卒日 | Christina Westcott 1963 年结婚，infobox 注 2023-11-17 去世；子女为二女（正文 "two daughters"），未具名不入库 |
| Sazanov/Stock 身份 | 均为**博士后研究员**（page 明载 "Postdoctoral Fellow"），非博士——note 写博士后，勿写博士生 |
| 荣誉年份 | EMBO 1984 / FRS 1995 / 爵士 1999（表彰 services to molecular biology）/ 荷兰外籍 1999 / FMedSci 2011 / Copley 2012——勿混淆 |
| 机构名 | MRC Mitochondrial Biology Unit（2015 年时为荣休主任兼教授）；infobox 机构栏 Oxford / LMB / Cambridge |
| 引语 | 本地页面**无 Walker 直接引语**——全部改间接转述，禁止编造引号原话 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q235184 | ✅ |
| name_zh | 约翰·E·沃克 | ✅ |
| name_en | John E. Walker | ✅ |
| birth_date | 1941-01-07 | ✅ |
| death_date | （空，在世） | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：ATP synthase / mitochondrial biology / membrane proteins / protein sequencing，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Edward Abraham | 师→生（博士导师） | 1965 牛津起研究肽类抗生素；1969 博士 |
| spouse | Christina Westcott | 无向 | 1963 结婚；infobox 注其 2023-11-17 去世 |
| colleague | Frederick Sanger | 无向 | 1974 剑桥研讨会结识，受邀加入 LMB 长期任职（页面作 Fred Sanger） |
| colleague | Francis Crick | 无向 | LMB 同侪（DNA 双螺旋发现者） |
| colleague | Andrew Leslie | 无向 | 晶体学家，F1-ATPase 晶体学合作者 |
| co-honored | Paul D. Boyer | 无向 | 1997 诺贝尔化学奖共享一半（ATP 合酶酶学机制） |
| co-honored | Jens Christian Skou | 无向 | 1997 同年共享另一半（Na+/K+-ATPase，与 Boyer/Walker 研究无关） |
| advisor-student | Leonid Sazanov | Walker→学生（博士后） | 博士后研究员（现 ISTA） |
| advisor-student | Daniela Stock | Walker→学生（博士后） | 博士后研究员（现 Sydney） |

> 禁入库名单：父亲 Thomas Ernest Walker、母亲 Elsie Lawton、两个妹妹 Judith/Jen、两个未具名女儿——家庭亲属无规范全名且超出学术关系白名单语义，**不予入库**；Walker 无 doctoral students 具名清单（仅博后二人），勿把结构库贡献者脑补为学生。

## 8. 奖项清单

- Nobel Prize in Chemistry（1997，与 Boyer 共享一半；Skou 独享另一半）
- EMBO Member（1984）
- Fellow of the Royal Society，FRS（1995）
- Knight Bachelor（1999，表彰对分子生物学的贡献）
- Foreign Member，Royal Netherlands Academy of Arts and Sciences（1999）
- Foreign Associate，National Academy of Sciences（年份页面未载，勿写）
- Fellow of the Academy of Medical Sciences，FMedSci（2011）
- Copley Medal（2012）
- Portland Press Excellence in Science Award；Honorary member of the British Biophysical Society；Honorary Fellow，St Catherine's College, Oxford（年份页面未载）

## 9. 机构清单

- 教育：Rastrick Grammar School；St Catherine's College, University of Oxford（化学 BA 三等；1969 PhD）
- 任职：University of Wisconsin–Madison（1969–1971）；法国（1971–1974）；MRC Laboratory of Molecular Biology（1974–，长期任职）；MRC Mitochondrial Biology Unit（2015 年时为荣休主任兼教授）；Sidney Sussex College, Cambridge 院士
- 兼任：Advisory Council, Campaign for Science and Engineering 成员

## 10. 终审清单

- [ ] 生卒 1941-01-07（在世），出生地哈利法克斯
- [ ] 1997 份额结构准确：Boyer+Walker 共享一半 / Skou 独享一半
- [ ] 博士年份取正文 1969；牛津 BA 三等如实呈现
- [ ] 旋转催化为 Boyer 假说、Walker 结构支持——因果方向不错置
- [ ] Sazanov/Stock 写博士后，不写博士生
- [ ] 引语零编造（页面无直接引语，全部间接转述）
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/John_E._Walker/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 为空——REST API 回退失败则装饰圆占位，图注不得虚构照片来源
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：页面无直接引语，任何带引号的"原话"都必须删除
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像位 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐
