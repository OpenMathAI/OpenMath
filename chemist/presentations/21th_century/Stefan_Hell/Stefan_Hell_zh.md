# Stefan Hell（斯特凡·黑尔）立传提示词

> qid=Q91410 · 1962-12-23 生于罗马尼亚阿拉德 · 在世 · 德国/罗马尼亚双国籍 · 诺贝尔化学奖（2014，与 Betzig/Moerner 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Stefan_Hell/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：参考 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md` §0-§11 结构标杆（高斯式：身份信息页 + 时间线 + 表格语义化 + 公式框）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取 `pages/Stefan_Hell/images.txt`；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{lightbulb}\enspace 击穿衍射极限的人\enspace·\enspace 德国 / 罗马尼亚`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Stefan Walter Hell、国籍（Citizenship: Germany, Romania）、出生地、教育、博士导师、领域、任职、荣誉。事实取自本地 page.md infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「受激发射损耗」母题——中心亮斑外圈被「环形光」压暗的视觉隐喻。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（Abbe 极限 d = λ/(2NA)、STED 耗尽光所致有效分辨率公式）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Stefan Walter Hell（中文惯称：斯特凡·黑尔）
- **生卒**：1962-12-23 生于罗马尼亚阿拉德（Arad）· 在世
- **国籍**：Germany、Romania（infobox Citizenship 双值：Germany Romania；正文口径 Romanian-German；metadata 的 "Romanian German" 排序噪声以 page.md 为准）
- **身份**：物理学家；马克斯·普朗克多学科科学研究所（哥廷根）所长之一，兼马克斯·普朗克医学研究所（海德堡）所长
- **家庭**：罗马天主教巴恩特施瓦本（Banat Swabian）家庭；父为工程师、母为教师；成长于阿拉德附近的 Sântana；1978 随父母移民西德，定居路德维希港
- **教育轨迹**：
  - Sântana 小学（1969–1977）→ 蒂米什瓦拉 Nikolaus Lenau 中学一年 → 1978 移民西德
  - 1981 入海德堡大学，1990 获物理学博士；博士导师固态物理学家 Siegfried Hunklinger；论文 *Imaging of transparent microstructures in a confocal microscope*
- **任职轨迹**：独立发明人（4Pi，短期）→ EMBL 海德堡（1991–1993）→ 芬兰图尔库大学医学物理系 group leader（1993–1996，期间 1993–94 牛津访问半年）→ 1996 海德堡大学特许任教资格（habilitation）→ 2002-10-15 哥廷根马普生物物理化学研究所所长（创建纳米生物光子学系）→ 2003 起兼德国癌症研究中心（DKFZ）光学纳米分析部负责人 + 海德堡大学非预算教授 → 2004 哥廷根大学名誉教授
- **研究领域**：物理、光学——STED 显微、RESOLFT、GSD 显微、4Pi 显微、Minflux

## 2. 核心叙事亮点（约 13 条）

1. **巴恩特施瓦本少年（1962）**：生于罗马尼亚阿拉德的巴恩特施瓦本天主教家庭——德裔少数族群。
2. **跨国童年（1969–1978）**：Sântana 小学 → 蒂米什瓦拉中学一年 → 1978 随父母移民西德路德维希港。
3. **海德堡深造（1981–1990）**：物理学博士，师从固态物理学家 Siegfried Hunklinger；论文研究共聚焦显微镜中的透明微结构成像。
4. **独立发明 4Pi（1990 前后）**：短暂任独立发明人，改进共聚焦显微镜轴向（深度）分辨率——即后来的 4Pi 显微镜。
5. **EMBL 验证 4Pi 原理（1991–1993）**：在欧洲分子生物学实验室成功演示 4-Pi 显微原理。
6. **图尔库孕育 STED（1993–1996）**：在芬兰图尔库大学任 group leader 期间提出**受激发射损耗（STED）显微原理**——获奖技术的摇篮；期间牛津访问半年。
7. ** habilitation 与马普所长（1996–2002）**：1996 海德堡 habilitation；2002-10-15 出任哥廷根马普生物物理化学研究所所长，创建纳米生物光子学系。
8. **击穿 1873 年 Abbe 极限**：Abbe 以来显微镜分辨率被认为不可能突破半波长（>200 nm）；Hell **从理论与实验上首次证明**荧光显微镜分辨率可与衍射解耦，提升至波长的零头（纳米尺度）。
9. **RESOLFT 家族**：STED 及相关可逆饱和/跃迁方法（RESOLFT）构成一套可推广的超分辨框架。
10. **2006 德国未来奖**：2006-11-23 获德国总统颁发的德国创新奖（Deutscher Zukunftspreis）——超分辨对生命科学与医学研究意义的国家级确认。
11. **2014 诺贝尔化学奖**：与 Eric Betzig、William Moerner 共享，官方理由 "for the development of super-resolved fluorescence microscopy"。
12. **巴恩特施瓦本第二位诺奖得主**：继 2009 文学奖得主赫塔·米勒（Herta Müller）之后，该群体第二位诺贝尔奖得主。
13. **高影响力与晚年荣誉**：2024 年 Google Scholar h-index 148；2015 罗马尼亚星大十字勋章、2016 Wilhelm Exner 奖章、2016 美国科学院外籍院士、2022 Pour le Mérite；Minflux（2017 Science，与 Balzarotti 等）持续拓展纳米分辨追踪。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深茄紫 aubergine） | `#46356B` | 受激发射损耗的深环与光学殿堂（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（4Pi 与轴向 badge4Pi） | `#673AB7` | 蓝紫 4Pi / EMBL 岁月 |
| 分类色 2（STED badgeSted） | `#D32F2F` | 红环形耗尽光 / 纳米分辨 |
| 分类色 3（RESOLFT 家族 badgeRes） | `#00897B` | 青可逆饱和跃迁 |
| 分类色 4（Minflux 与追踪 badgeMinflux） | `#F2994A` | 橙最小光子通量追踪 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「亮斑 + 暗环」的光学斑纹。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`，勿复制 wav，Makefile 直接引用路径）
- **风格**：探索感 / 宏大推进 / 史诗
- **匹配理由**：
  - "Expedition" 匹配「从罗马尼亚小城出发、远征 1873 年 Abbe 极限」的探索叙事
  - 宏大推进感匹配 STED 从图尔库原理到马普建制化、再到 2014 诺奖的长征
  - 史诗质感匹配「击穿一个被认为不可能的物理极限」的戏剧性
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 击穿衍射极限的人 / Stefan Hell 1962– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士导师/领域/任职/荣誉）
03  黑尔的一生 — 高斯式时间线（10 节点：1962→1978→1990→1991→1993→1996→2002→2006→2014→2022）
04  巴恩特施瓦本与移民 (1962–1981) — 表格「时间|事件|结果」
05  海德堡：博士与 4Pi (1981–1993) — 表格「问题|方法|结果」+ 公式框：共聚焦轴向分辨率改进
06  图尔库：STED 原理的诞生 (1993–1996) — 表格「挑战|方法|结果」+ 公式框：STED 有效分辨率
07  击穿 Abbe 极限 — 表格「旧观念|新方法|结果」+ 公式框：Abbe 极限 d=λ/2NA 及其突破
08  马普建制化 (2002–) — 表格「机构|方向|结果」（哥廷根纳米生物光子学系 / DKFZ / 海德堡）
09  从 RESOLFT 到 Minflux — 表格「方法|原理|结果」（RESOLFT / GSD / Minflux 2017）
10  2014 诺贝尔化学奖 — 三人共享页（Betzig / Moerner / Hell）+ citation 原句公式框
11  技术谱系：三条路线 — 表格「人物|路线|结果」（Hell=STED；Betzig=PALM；Moerner=单分子基础——分工勿混）
12  荣誉全景 — 高斯式「类别|代表|意义」表格 + itemize 荣誉清单（Leibniz 2008 / Kavli 2014 / Pour le Mérite 2022 等）
13  遗产：纳米显微改变生命科学 — 四分类遗产盒（对生命科学/医学的影响 / h-index 148 / 门生 Testa、Balzarotti）
14  结尾 — 「衍射不是终点。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2014 获奖理由 | 官方原句 "for the development of super-resolved fluorescence microscopy"；三人**共享**（Betzig / Hell / Moerner），勿写独享 |
| 三人分工 | **Hell = STED（受激发射损耗，确定性光学路线）**；Betzig = PALM；Moerner = 单分子/光开关蛋白基础——技术路线分工勿混 |
| 国籍口径 | infobox Citizenship 双值 Germany Romania；正文 Romanian-German；metadata "Romanian German" 是排序噪声——**以 page.md 为准**，封面写「德国 / 罗马尼亚」 |
| Abbe 极限 | 1873 年 Ernst Karl Abbe 提出、此前被认为不可能突破——「首次理论与实验证明可解耦」的口径来自 page.md，勿加戏 |
| 旧极限数值 | 荧光显微旧极限为「所用光半波长（>200 纳米）」——勿写错数值 |
| 博士导师 | Siegfried Hunklinger（固态物理学家，infobox + 正文双载）——勿写他人 |
| 门生口径 | infobox Notable students 仅 **Ilaria Testa、Francisco Balzarotti（均 postdoc）**——入库时注明 postdoc 身份，勿写成博士 |
| 职位表述 | 是马普**多学科科学研究所**（由生物物理化学研究所演变）与马普医学研究所两所所长之一——按 page.md 现口径写 |
| 巴恩特施瓦本第二人 | 「第二位 Banat Swabian 诺奖得主（继 Herta Müller 之后）」系 page.md 明载——写事实即可，不展开文学讨论 |
| 图尔库年份 | 1993–1996；STED 原理在此期间提出——勿写「1990 年代末」 |
| 引语红线 | page.md 无 Hell 直接引语——全部改间接转述，不得编造「原话」 |
| 中文译名 | 斯特凡·黑尔；姓氏 Hell 勿意译 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q91410 | ✅ |
| name_zh | 斯特凡·黑尔 | ✅ |
| name_en | Stefan Hell | ✅ |
| birth_date | 1962-12-23 | ✅ |
| death_date | null（在世） | ✅ |
| nationality | Germany / Romania（双国籍，rank 0/1） | ✅ |
| primary_occupation | physicist | ✅ |
| field_of_work | chemistry, physics, microscopy（person_field 细分见下表） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | field_en | field_zh |
|---|---|---|
| 0 | super-resolution fluorescence microscopy | 超高分辨荧光显微 |
| 1 | STED microscopy | 受激发射损耗显微 |
| 2 | RESOLFT | RESOLFT 可逆饱和跃迁显微 |
| 3 | 4Pi microscopy | 4Pi 显微 |
| 4 | optics | 光学 |

## 7. 社会关系入库清单

**师长 / 共同得主 / 门生**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Siegfried Hunklinger | 师→生（博士导师） | 海德堡固态物理学家，1990 博士论文导师，infobox+正文双载 |
| advisor-student | Ilaria Testa | 生（postdoc） | infobox Notable students 明载 postdoc |
| advisor-student | Francisco Balzarotti | 生（postdoc） | infobox Notable students 明载 postdoc；2017 Minflux 第一作者 |
| co-honored | Eric Betzig | 无向 | 2014 诺贝尔化学奖共同得主 |
| co-honored | William E. Moerner | 无向 | 2014 诺贝尔化学奖共同得主 |

> **禁入库名单**（metadata/奖项名仅提及、非关系实体）：牛津/图尔库/EMBL/DKFZ 同事（page.md 未点名个人）、Butkevich 等论文合作者（仅列于 Publications 清单）、教宗/罗马尼亚王室（授勋行为）。metadata-only 的其余奖项关联不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（2014，与 Betzig/Moerner 共享）
- Kavli Prize in Nanoscience（2014）
- Prize of the International Commission for Optics（2000）；Helmholtz Award（2001，共同获得者）
- Berthold Leibinger Innovationspreis（2002）；Carl-Zeiss Research Award（2002）；Karl-Heinz-Beckurts-award（2002）
- Berlin-Brandenburg Academy Award（2004）；Robert B. Woodward Scholar, Harvard（2006）
- 德国未来奖 Deutscher Zukunftspreis（2006-11-23）；Julius Springer Prize（2007）
- Gottfried Wilhelm Leibniz Prize（2008）；Lower Saxony State Prize（2008）
- Otto Hahn Prize（2009）；Ernst Hellmut Vits Prize（2010）；Lise Meitner Prize, Gothenburg（2010/11）
- Hansen Family Award（2011）；Körber European Science Prize（2011）；Meyenburg Prize（2011）
- Paul Karrer Gold Medal, University of Zürich（2013）；Carus Medal, Leopoldina（2013）；Leopoldina 成员（2013）
- Knight Commander of the Order of the Crown, Romania 王室（2015）；Grand Cross of the Order of the Star of Romania（2015）
- Glenn T. Seaborg Medal（2015）；Wilhelm Exner Medal（2016）；NAS foreign associate（2016）
- HonFRMS 皇家显微学会（2017）；Fellow, Norwegian Academy of Science and Letters
- Pour le Mérite for Sciences and Arts（2022）；Akademie der Wissenschaften zu Göttingen 成员（2007）

## 9. 机构清单

- 教育：Sântana 小学（1969–1977）→ Nikolaus Lenau High School, Timișoara（一年）→ Heidelberg University（1981 入学，PhD 1990；habilitation 1996）
- 任职：独立发明人（短期，4Pi）→ EMBL Heidelberg（1991–1993）→ University of Turku 医学物理系 group leader（1993–1996；1993–94 牛津访问半年）→ Max Planck Institute for Biophysical Chemistry（今 Max Planck Institute for Multidisciplinary Sciences）所长（2002-10-15–，纳米生物光子学系创建人）→ DKFZ 光学纳米分析部负责人 + 海德堡大学 apl. Prof.（2003–）→ 哥廷根大学名誉教授（2004–）

## 10. 终审清单

- [x] 生卒 1962-12-23 / 在世；出生地罗马尼亚阿拉德
- [x] 2014 三人共享表述准确；citation 英文原句完整
- [x] 三人技术路线分工（STED / PALM / 单分子基础）表述准确
- [x] 国籍双值口径（德国/罗马尼亚）与 page.md 一致
- [x] Abbe 极限 1873 / >200 nm 数值准确
- [x] 门生仅 Testa、Balzarotti（postdoc 注明）
- [x] 引语全部间接转述（page.md 无直接引语）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 读取 `pages/Stefan_Hell/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：按 images.txt 下载，404 则装饰圆占位
- [ ] 国籍：封面明示「德国 / 罗马尼亚」
- [ ] 引语核对：无直接引语，全篇间接转述
- [ ] 编译验证：`make distclean && make`
- [ ] Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger/高斯模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2014 三人共享另两篇（Betzig / Moerner）口径交叉对齐
