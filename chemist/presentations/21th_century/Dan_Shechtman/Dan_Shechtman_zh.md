# Dan Shechtman（达尼埃尔·谢赫特曼）立传提示词

> qid=Q44111 · 1941-01-24 生于特拉维夫（当时属英国托管巴勒斯坦）· 在世 · 以色列化学家 · 诺贝尔化学奖（2011，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Dan_Shechtman/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页，是本次写作的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从本地 `images.txt` 列表下载，如 1985 年 NIST 会议照；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 准晶体之父\enspace·\enspace 以色列`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、研究领域、任职、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「准周期镶嵌」母题——按照数学规则排布但永不重复的圆点阵列，暗合 Alhambra 镶嵌与准晶衍射斑点。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式/衍射条件即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Dan Shechtman（希伯来文 דן שכטמן；中文惯称：达尼埃尔·谢赫特曼）
- **生卒**：1941-01-24 生于特拉维夫（当时属英国托管巴勒斯坦 Mandatory Palestine，1948 年起属以色列）→ 在世（卒日留白）
- **国籍**：Israel（以色列；frontmatter 另载 United States——长年在美国 NIST/Iowa State 任职，yaml 按 Israel rank 0 + United States rank 1 入库）
- **身份**：化学家 / 材料科学家——Technion（以色列理工学院）Philip Tobias 材料科学教授、Ames 国家实验室（美国能源部）Associate、Iowa State University 材料科学教授；六位获诺贝尔化学奖的以色列人之一
- **家庭**：犹太家庭，在 Petah Tikva 与 Ramat Gan 长大；祖父母于第二次 Aliyah（1904–1914）移民巴勒斯坦并创办印刷所；妻子 Tzipora Shechtman 为海法大学咨询与人类发展系主任、心理治疗领域两书作者；四子女——儿子 Yoav Shechtman（曾在 W. E. Moerner 实验室做博士后，现为 Technion 教授）、三个女儿 Tamar Finkelstein（以色列警方领导力中心组织心理学家）、Ella Shechtman-Cory、Ruth Dougoud-Nevo（后两位均为临床心理学博士）
- **教育轨迹**（全部在 Technion）：
  - 1966 机械工程 B.Sc.
  - 1968 材料工程 M.Sc.
  - 1972 材料工程 Ph.D.（博士导师：页面无载，勿写）
- **童年**：痴迷儒勒·凡尔纳《神秘岛》（1874）反复读过多遍，梦想成为书中主角工程师 Cyrus Smith 式的人物；原话 "I thought that was the best thing a person could do..."（页面明载可引用）
- **研究领域**：材料科学——准晶体（quasicrystals）、晶体学、物理冶金（钛铝合金、快速凝固铝合金、CVD 金刚石）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **《神秘岛》的工程师梦（1940s）**：凡尔纳笔下 "knows mechanics and physics" 的 Cyrus Smith 是童年偶像——工程师式的"从无到有创造整个生活方式"成为终身志向。
2. **Technion 三级跳（1966–1972）**：机械工程学士 → 材料工程硕士 → 材料工程博士，全部在以色列理工学院完成。
3. **Wright-Patterson 空军基地（1972–1975）**：NRC fellow，在航空研究实验室用三年研究钛铝金属间化合物的显微组织与物理冶金。
4. **回巢 Technion（1975）**：加入材料工程系，此后以 Technion 为学术大本营。
5. **约翰斯·霍普金斯访问（1981–1983）**：与 NBS（美国国家标准局）联合计划中研究快速凝固铝-过渡金属合金。
6. **1982-04-08：发现二十面体相**：在 NBS 的 sabbatical 期间拍摄到十次对称电子衍射图——"ordered but not periodic"（有序但无平移对称）的二十面体相，打开准周期晶体这一全新领域。
7. **1984 年 PRL 论文**：与 Blech、Gratias、Cahn 发表 "Metallic Phase with Long-Range Orientational Order and No Translational Symmetry"（Phys. Rev. Lett. 53, 1951）。
8. **十年孤独论战（1984–1994）**：从论文发表到 Pauling 去世，持续遭受两度诺奖得主 Linus Pauling 的敌意；Pauling 名言 "There is no such thing as quasicrystals, only quasi-scientists"；研究组长先令他 "go back and read the textbook"，数日后又以 "bringing disgrace"（令团队蒙羞）为由请他离开；他自述 "For a long time it was me against the world"。
9. **学界反转（1987–）**：到 1987 年多个研究组合成出类似准晶体，测得低热导/低电导与高结构稳定性；准晶体后来也在自然界被发现。
10. **1981 年 Kleinert–Maki 论文注记**：Pauling 显然不知道 Kleinert 与 Maki 早在 1981 年已指出准晶中非周期二十面体相的可能性（历史注记，非谢赫特曼本人关系）。
11. **2011 诺贝尔化学奖（独享）**：官方理由 "for the discovery of quasicrystals"；瑞典皇家科学院诺贝尔委员会评语——"his discovery was extremely controversial" 但其工作 "eventually forced scientists to reconsider their conception of the very nature of matter"；奖金 1000 万瑞典克朗（约 150 万美元）。
12. **2014 年以色列总统竞选**：2014-01-17 宣布参选，获 10 名议员连署，2014-06-10 选举中仅得 1 票；以色列媒体戏称 "quasi-president"（准总统），呼应 "quasi-scientist"（建议一笔带过或略过，见 §5）。
13. **应用与谦逊**：准晶体可望用于精密仪器耐用钢、电线与炊具不粘绝缘层等——但页面明言 "presently have no technological applications"（如实写，勿夸大应用前景）；2014 年起任托木斯克理工大学国际科学委员会主席。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海军蓝 deepnavy） | `#16324F` | 电子衍射图的深空与以色列理工的严谨（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（准晶体 badgeQuasi） | `#2E5A9E` | 蓝二十面体相 / 十次对称衍射 |
| 分类色 2（论战岁月 badgeDebate） | `#A63A2B` | 砖红 "me against the world" / Pauling 论战 |
| 分类色 3（冶金与钛铝 badgeMetal） | `#5C6B73` | 钢灰钛铝合金 / 快速凝固 |
| 分类色 4（荣誉 badgeHonor） | `#1B7A43` | 绿 Israel Prize / Wolf Prize |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——准周期镶嵌：圆点按规则散布却永不周期重复，呼应 Alhambra / Darb-i Imam 镶嵌与准晶衍射花样。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Pathfinder** — Ghostwriter Music（Daniel Beijbom 作曲，布达佩斯录制；文件 `23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (...).wav`，**勿复制 wav 文件**）
- **风格**：史诗 / 坚毅 / 孤身开拓者的行进感
- **匹配理由**：
  - "Pathfinder（探路者）" 精准对应其身份——在"晶体必须周期"的百年教条之外独自探出一条新路
  - "坚毅" 匹配 1982–1994 十余年 "me against the world" 的孤独坚守，音乐的情绪弧线与论战—反转—加冕的叙事同构
  - "史诗" 匹配结尾立场的最终翻转——诺奖委员会 "forced scientists to reconsider the very nature of matter" 的分量
- **时长核对**：以 ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒的幻灯时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 准晶体之父 / Dan Shechtman 1941– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/领域/任职/家庭/荣誉）
03  谢赫特曼的一生 — Sanger 式时间线（10 节点：1941→1966→1972→1975→1981→1982→1984→1987→2011→2014）
04  早年：《神秘岛》的工程师梦 (1941–1966) — 表格「时间|事件|结果」
05  Technion 与冶金学徒期 (1966–1975) — 表格「阶段|对象|产出」（钛铝金属间化合物）
06  1982-04-08：二十面体相的发现 — 表格「背景|观察|结论」+ 公式框：五次对称衍射 / 有序但无平移对称
07  1984 PRL 论文与十年论战 (1984–1994) — 表格「对手|立场|结果」+ Pauling "quasi-scientists"
08  学界反转与确证 (1987–) — 表格「挑战|方法|结果」（多组合成、低热导、自然界发现）
09  2011 诺贝尔化学奖 — 表格「奖项|年份|理由」+ 公式框：for the discovery of quasicrystals
10  家庭与传承 — 表格「人物|身份|结果」（Tzipora / Yoav / 三女）
11  荣誉与奖项 — Sanger 式「类别|代表|意义」表格（含 itemize 荣誉清单）
12  从特拉维夫到 Ames — 机构流程图（Technion → Wright-Patterson → JHU/NBS → NIST → Iowa State）
13  遗产：教科书被改写 — 四分类遗产盒 + 公式框：准周期镶嵌与诺贝尔委员会评语
14  结尾 — 「自然比教科书更丰富，而实验是唯一的裁判。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2011 获奖口径 | **独享**，勿写共享；官方理由 "for the discovery of quasicrystals"（页面明载） |
| 发现日期 | 1982 年 **4 月 8 日**（intro 与正文一致）；勿写 1984（那是论文发表年） |
| 出生地口径 | 1941-01-24 生于特拉维夫，当时属 **Mandatory Palestine**（1948 年起属以色列）——勿写"生于以色列"后又不加注 |
| Pauling 论战 | page.md 明载可写：Pauling 直到 1994 年去世都反对非周期解读、"quasi-scientists" 名言、"me against the world" 自述、组长 "go back and read the textbook"/"bringing disgrace" 逐客——均属**争议叙事（controversy）**，呈现时保持客观、以诺贝尔委员会评语收束；Kleinert–Maki 1981 论文是历史注记，勿写成谢赫特曼的学术关系 |
| 应用前景 | 页面明言 "presently have no technological applications"——勿写"已广泛应用"；可写的仅为 potential 用途（耐用钢、不粘绝缘） |
| 总统竞选 | 2014 年仅得 1 票、"quasi-president" 之谑——政治色彩内容建议正文一笔带过或整体略过，勿铺陈以色列国内政治语境 |
| 国籍口径 | 页面主体称 "Israeli chemist"；frontmatter nationality 兼列 United States（常年美国任职）——封面只写以色列，yaml 双国籍分 rank |
| 同名区分 | 儿子 Yoav Shechtman ≠ 本人；W. E. Moerner（2014 诺奖）只是**儿子的博士后东家**，与谢赫特曼本人无直接关系，勿入库 |
| 论文合作者 | 1984 PRL 四作者 Shechtman/Blech/Gratias/Cahn——Cahn（John W. Cahn）与 Gratias（Denis Gratias）有全名可入库；Blech 页面仅载缩写 "Blech, I."，规范全名无法本地溯源，**不入库** |
| 在世口径 | 无卒日，封面与身份页一律 "1941–" 留白，勿虚构 |
| 中文译名 | 惯称「达尼埃尔·谢赫特曼」（任务口径），勿写「丹·谢克特曼」等其他形式 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q44111 | ✅ |
| name_zh | 达尼埃尔·谢赫特曼 | ✅ |
| name_en | Dan Shechtman | ✅ |
| birth_date | 1941-01-24 | ✅ |
| death_date | NULL（在世留白） | ✅ |
| nationality | Israel（rank 0）+ United States（rank 1） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | crystallography（person_field 细分：quasicrystals / crystallography / materials science / extractive metallurgy，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**家人 / 论战对手 / 合作者**（★红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Tzipora Shechtman | 无向 | 海法大学咨询与人类发展系主任，心理治疗两书作者 |
| parent-child | Yoav Shechtman | 无向（from<to） | 儿子；曾为 W. E. Moerner 实验室博士后，现为 Technion 教授 |
| controversy | Linus Pauling | 无向 | 1984–1994 坚决反对准晶非周期解读，"quasi-scientists" 出自其口；诺贝尔委员会称发现 "extremely controversial" |
| colleague | John W. Cahn | 无向 | 1984 PRL 准晶论文共同作者 |
| colleague | Denis Gratias | 无向 | 1984 PRL 准晶论文共同作者；1986 合著二十面体准晶标定论文 |

> **禁入库名单**（页面无规范全名或非本人直接关系）：I. Blech（1984 PRL 共同作者，页面仅载缩写 "Blech, I."）、H. Kleinert 与 K. Maki（1981 论文历史注记）、Reuven Rivlin（总统颁奖同框，政治人物）、W. E. Moerner（系儿子 Yoav 的博士后东家）、未具名研究组长（"go back and read the textbook" 当事人）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2011，独享，"for the discovery of quasicrystals"）
- Israel Prize（1998，物理）
- Wolf Prize in Physics（1999）
- Gregori Aminoff Prize（2000，瑞典皇家科学院）
- EMET Prize in Chemistry（2002）
- Muriel & David Jacknow Technion Award for Excellence in Teaching（2000）
- E-MRS 25th Anniversary Award（2008）
- Fray International Sustainability Award（2014，SIPS）
- Rothschild Prize in Engineering（1990）
- Weizmann Science Award（1993）
- International Award for New Materials（1988，美国物理学会，即 James C. McGroddy Prize）
- New England Academic Award of the Technion（1988）
- Physics Award of the Friedenberg Fund（1986）
- Honorary John von Neumann Professor（2019）；Bar-Ilan University 荣誉博士（2013）；Aix-Marseille 大学与斯洛伐克理工大学荣誉博士（frontmatter）

## 9. 机构清单

- 教育：Technion – Israel Institute of Technology（B.Sc. 1966 机械工程 / M.Sc. 1968 / Ph.D. 1972 材料工程）
- 任职：Wright-Patterson AFB 航空研究实验室 NRC fellow（1972–1975）；Technion 材料工程系（1975–）；Johns Hopkins University sabbatical（1981–1983，与 NBS 联合计划）；NIST sabbatical（1992–1994，CVD 金刚石）；Iowa State University 教授（2004–，每年约 5 个月在 Ames）；Ames National Laboratory（美国能源部）Associate；Technion Louis Edelstein Center / Wolfson Centre（主任）
- 其他：Tomsk Polytechnic University 国际科学委员会主席（2014–）

## 10. 终审清单

- [ ] 生卒 1941-01-24 / 在世留白；出生地特拉维夫（当时 Mandatory Palestine）表述准确
- [ ] 2011 **独享**，官方理由 "for the discovery of quasicrystals" 表述准确
- [ ] 发现日期 1982-04-08（NBS sabbatical 期间）与 1984 PRL 论文年份区分清楚
- [ ] Pauling 论战表述以 page.md 实载为限，无杜撰引语（"quasi-scientists"、"me against the world"、组长两句话均有原文）
- [ ] "presently have no technological applications" 如实呈现
- [ ] 国籍封面只写以色列；yaml 双国籍分 rank
- [ ] 引语全部可在本地 Wikipedia 原文找到（凡尔纳段、"quasi-scientists"、"me against the world"、诺贝尔委员会两句评语）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Dan_Shechtman/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 `images.txt` 列表下载（如 1985 NIST 会议照 / 2011 斯德哥尔摩照），失败用装饰圆占位
- [ ] **国籍**：封面顶部明示以色列
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（获奖理由、Pauling 名言、"me against the world"、委员会评语）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，本提示词不直接改动总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
