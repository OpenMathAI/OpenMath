# Alan J. Heeger（艾伦·J·黑格）立传提示词

> qid=Q106751 · 1936-01-22 生于美国爱荷华州苏城（在世） · 美国物理学家/化学家 · 20 世纪 · 诺贝尔化学奖（2000，与 Alan G. MacDiarmid、Hideki Shirakawa 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Alan_J._Heeger/`（page.md + metadata.json + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次立传的核心版式语言。

---

## 0. 正文形式说明（参考桑格立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 为空、images/ 目录无肖像——优先用 Wikipedia REST API `page/summary` 查 infobox 原图（页面注明 "Heeger in 2013"，存在真实照片）下载；仍失败则用**装饰圆占位**（主色渐变 + 姓名首字母），并在 §10 勾选项如实标注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace 让塑料导电的人\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Alan Jay Heeger、国籍、出生地（Sioux City, Iowa）、教育（Nebraska / Berkeley）、博士（1961）、师承（Alan M. Portis）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「掺杂/载流子」母题——离散圆点暗示掺杂剂进入共轭链后产生载流子。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 1977 年 PRL 论文 «Electrical Conductivity in Doped Polyacetylene» 的碘掺杂电导率跃升（$\sim 10^{-10} \to 10^{3}\ \mathrm{S/cm}$ 量级须按页面实载表述，页面未载具体数值则写「绝缘体→类金属」）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Alan Jay Heeger（中文惯称：艾伦·J·黑格）
- **生卒**：1936-01-22 生于美国爱荷华州 Sioux City（在世，页面无卒日）
- **国籍**：United States（美国）
- **身份**：物理学家、学者、诺贝尔化学奖得主（页面 description "American chemist, physicist"）
- **家庭**：犹太家庭出身；在爱荷华州 Akron 长大，父亲经营一家杂货店；9 岁时父亲去世，全家迁回苏城。妻子 Ruth（infobox：Spouse Ruth，2 children）；其子 David Heeger 为神经科学家、Peter Heeger 为免疫学家（正文明载）
- **教育轨迹**：
  - Omaha Central High School（metadata educated_at 有载）
  - University of Nebraska–Lincoln：1957 年获物理与数学 B.S.
  - University of California, Berkeley：1961 年获物理学 Ph.D.
- **导师**：Alan M. Portis（博士导师；infobox 与 frontmatter 一致）
- **博士**：1961（正文），论文 *Studies on the magnetic properties of canted antiferromagnets*（infobox 论文年份标注 1962——年份口径见 §5）
- **研究领域**：物理学与化学交叉——导电聚合物、凝聚态物理、半导体/金属聚合物、SSH 拓扑模型
- **职业生涯**：1962–1982 任教宾夕法尼亚大学；1982 起任加州大学圣塔芭芭拉分校（UCSB）物理系与材料系教授至今（页面口径 "present appointment"）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **杂货店之子（1936）**：爱荷华小镇犹太移民式成长；9 岁丧父、迁居苏城——早年颠沛与日后 "Never Lose Your Nerve!" 的韧性底色。
2. **内布拉斯加（1957）**：物理 + 数学双修 B.S.——为日后"用物理学家眼光做化学"埋下伏笔。
3. **伯克利博士（1961）**：师从 Alan Portis，研究倾转反铁磁体的磁性——凝聚态实验物理的科班训练。
4. **宾大二十年（1962–1982）**：固体物理与聚合物化学群星汇聚的宾大，为 1977 年的跨学科合作提供土壤。
5. **迁至 UCSB（1982）**：任物理系与材料系教授，开启聚合物光电的第二个主场。
6. **聚乙炔导电（1977）**：与 MacDiarmid、白川英树合作，掺杂聚乙炔使导电率大幅提升，成果 1977 年发表（PRL «Electrical Conductivity in Doped Polyacetylene» 等）——"塑料也能导电"由此改写教科书。
7. **2000 诺贝尔化学奖**：三人共享，获奖理由 "for their discovery and development of conductive polymers"——物理学家获化学奖的交叉典范。
8. **SSH 模型**：导电聚合物工作引出 Su–Schrieffer–Heeger 模型——日后成为拓扑绝缘体的简单模型（页面明载）。
9. **获奖前夜已获物理界认可**：1983 年 Oliver E. Buckley 凝聚态奖（APS）、1995 年 Balzan Prize（非生物材料科学）——先物理后化学的双料轨迹。
10. **科学家创业**：研究成果孵化多家公司——Uniax（后被 DuPont 收购）、Konarka、Sirigen（2003 年由 Guillermo C. Bazan、Patrick J. Dietzen、Brent S. Gaylord 创办）。
11. **国家工程院（2002）**：以 "co-founding the field of conducting polymers" 与推动技术应用当选美国国家工程院院士。
12. **门生**：infobox Doctoral students 载 Park Yung-woo（博士生）与 Fan Chunhai（博士后学生）——导电聚合物研究扩散到亚洲学界的见证。
13. **自传与科学观（2015）**：*Never Lose Your Nerve!*；引语（页面原文）"Perhaps the greatest pleasure of being a scientist is to have an abstract idea, then to do an experiment ... that demonstrates the idea was correct"——抽象观念 → 实验证实的创造力循环。2010 年参加 USA Science and Engineering Festival "Lunch with a Laureate"，三度（2006/2007/2010）任 STAGE 国际剧本竞赛评委。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海蓝 deepnavy） | `#1E3A5F` | 导电聚合物的"金属光泽"与凝聚态物理的深度（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（导电聚合物 badgePoly） | `#2E7D5B` | 绿掺杂聚乙炔 / 1977 论文 |
| 分类色 2（聚合物光电 badgeOpto） | `#B4632C` | 琥珀 LED / 太阳能电池 / 发光二极管应用 |
| 分类色 3（凝聚态物理 badgeCond） | `#3E5C94` | 蓝反铁磁体博士课题 / Buckley 奖 |
| 分类色 4（SSH 拓扑模型 badgeSSH） | `#8E4A6E` | 紫孤子 / 拓扑绝缘体 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「掺杂载流子」的离散点缀。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Through the Darkness** — Audiomachine（源文件 `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`；不要复制 wav 文件，Makefile 中引用路径即可）
- **风格**： cinematic / epic / 由暗至明的推进感
- **匹配理由**：
  - "由暗至明" 匹配其叙事——塑料从绝缘的"黑暗"中被掺杂点亮为导体，正是 conductivity 破晓的故事
  - "cinematic" 匹配从爱荷华小镇到诺贝尔领奖台的跨度
  - 史诗感匹配导电聚合物这一"开辟新领域"（field co-founding）的分量
- **时长**：以实际曲目时长为准，> 15 页 × 7 秒即可由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 让塑料导电的人 / Alan J. Heeger 1936– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士/师承/领域/荣誉）
03  黑格的一生 — 高斯式时间线（10 节点：1936→1957→1961→1962→1977→1982→1983→1995→2000→2002）
04  早年：杂货店之子 (1936–1957) — 表格「时间|事件|结果」
05  伯克利：凝聚态实验物理 (1957–1962) — 表格「时间|事件|结果」+ 公式框：倾转反铁磁体课题
06  宾大二十年 (1962–1982) — 表格「阶段|方向|结果」
07  聚乙炔导电 (1976–1977) — 表格「问题|方法|结果」+ 公式框：碘掺杂聚乙炔 (CH)x 导电化
08  2000 诺贝尔化学奖 — 表格「得主|领域|理由」（三人共享标注醒目）+ citation 英文原句
09  SSH 模型与拓扑 — 表格「对象|机制|意义」+ 公式框：SSH 链模型示意
10  UCSB 与聚合物光电 (1982– ) — 表格「方向|成果|应用」（LED/太阳能电池/显示）
11  科学家创业 — 高斯式「公司|方向|结局」表格（Uniax→DuPont / Konarka / Sirigen）
12  门生与传播 — 表格「人物|方向|结果」（Park Yung-woo / Fan Chunhai）
13  荣誉清单 — 高斯式「类别|代表|意义」表格（Buckley 1983 / Balzan 1995 / NAE 2002）
14  结尾 — "Perhaps the greatest pleasure of being a scientist ..." + 品牌 OpenMathAI
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖口径 | 2000 化学奖为**三人共享**（Heeger、Alan G. MacDiarmid、Hideki Shirakawa）；理由英文以本地页面口径 "for their discovery and development of conductive polymers"；勿写"独享"或把理由泛化为"发明导电塑料" |
| 博士年份 | 正文 "Ph.D. in physics from the University of California, Berkeley in 1961"，而 infobox Thesis 标注 1962——**取正文 1961**，若需提及论文信息可加注 infobox 标注差异 |
| 同名/全名 | 全名 Alan Jay Heeger；共同得主 Alan G. MacDiarmid 勿简写成 "Alan Heeger" 或与 MacDiarmid 混写；数据库对手方统一用 "Alan G. MacDiarmid" |
| 学科身份 | 他是**物理学家**获化学奖（B.S. 物理+数学、PhD 物理）；页面 description 亦作 "chemist, physicist" 双身份——勿只写化学家 |
| SSH 模型 | 页面仅说导电聚合物工作 "led to" SSH 模型、是拓扑绝缘体的简单模型——**勿展开拓扑绝缘体技术细节**（页面无载） |
| 具体电导数值 | 页面未给出掺杂前后电导率具体数字——公式框写「绝缘体→类金属导电」定性表述，**禁编造数值** |
| 创业公司角色 | Uniax 是 "Alan Heeger was a founder"（明载）；Sirigen 是 Bazan/Dietzen/Gaylord 创办（Heeger 仅为研究成果相关，页面未载他创办 Sirika）——勿写"创办 Sirigen" |
| 门生范围 | infobox 仅载 **Park Yung-woo**（博士生）与 **Fan Chunhai**（postdoc student）；metadata 另有 Lee Kwang-hee 但页面正文/infobox 无——**不予入库、勿写入 Beamer** |
| 家人 | 妻 Ruth、子 David（神经科学家）/Peter（免疫学家）页面明载——身份信息页可提；勿写入数据库 relations（按本批化学家惯例仅收学术关系） |
| 引语红线 | 全页仅一条引语（自传 *Never Lose Your Nerve!* 那段 "Perhaps the greatest pleasure ..."）——中文引号内不得出现其他"原话"；诺奖演讲标题 «Semiconducting and Metallic Polymers: The Fourth Generation of Polymeric Materials»（2000-12-08）只作标题引用 |
| ENI award / 荣誉年份 | infobox 载 ENI award、John Scott Award、西班牙国家研究委员会金奖、Alicante 荣誉博士、APS/AAAS Fellow，但**页面未载年份**——荣誉页年份仅写有年份者（Buckley 1983、Balzan 1995、NAE 2002），其余不标年份 |
| 演讲/评审细节 | Lunch with a Laureate（2010-10）、STAGE 评委（2006/2007/2010）为边缘轶事，建议一句带过或略过 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q106751 | ✅ |
| name_zh | 艾伦·J·黑格 | ✅ |
| name_en | Alan J. Heeger | ✅（page.md 规范名；本批新建记录） |
| birth_date | 1936-01-22 | ✅（在世，death_date 留空） |
| nationality | United States | ✅ |
| primary_occupation | physicist | ✅（occupations 另含 chemist） |
| field_of_work | physics, chemistry（person_field 细分见下表，带 rank） | ✅ |

**person_field 细分（rank 表）**：

| name_en | rank | name_zh | 依据 |
|---|---|---|---|
| conductive polymers | 0 | 导电聚合物 | 诺奖理由核心 |
| polymer physics | 1 | 聚合物物理 | 金属聚合物/光电研究主线 |
| condensed matter physics | 2 | 凝聚态物理 | 博士课题 + Buckley 奖 |
| polymer photovoltaics | 3 | 聚合物光伏 | Uniax/Konarka 太阳能电池方向（DOE 报告与创业实载） |

## 7. 社会关系入库清单（★ 红线：只收 page.md 正文或 infobox 明载者）

**师长 / 门生 / 共同得主 / 合作**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Alan M. Portis | 师→生（博士导师） | UC Berkeley 物理学博士（1961），课题为倾转反铁磁体磁性 |
| advisor-student | Park Yung-woo | Heeger → 学生 | infobox Doctoral students 明载博士生 |
| advisor-student | Fan Chunhai | Heeger → 学生 | infobox 注明 postdoc student（博士后学生） |
| co-honored | Alan G. MacDiarmid | 无向 | 2000 诺贝尔化学奖共同得主 |
| co-honored | Hideki Shirakawa | 无向 | 2000 诺贝尔化学奖共同得主 |
| colleague | Alan G. MacDiarmid | 无向 | 宾大长期合作，掺杂聚乙炔系列论文共同作者 |
| colleague | Hideki Shirakawa | 无向 | 1976 起合作发展聚乙炔电导率 |
| spouse | Ruth | 无向 | 妻子（infobox），育有两子 |

**禁入库名单（metadata.json-only，页面正文/infobox 无载）**：
- Lee Kwang-hee（metadata doctoral_student，页面无载）
- University of Utah / University of Geneva（metadata employer，页面正文未展开，非人物关系）
- 子女 David Heeger / Peter Heeger 虽页面明载，按本批化学家惯例仅收学术关系，**不入库**

## 8. 奖项清单

- Nobel Prize in Chemistry（2000，与 MacDiarmid / Shirakawa 三人共享）
- Oliver E. Buckley Condensed Matter Prize（1983，American Physical Society）
- Balzan Prize（1995，Science of Non-Biological Materials）
- 美国国家工程院院士（2002，理由为 co-founding the field of conducting polymers）
- Guggenheim Fellowship；ENI award；John Scott Award
- Gold medal of the Spanish National Research Council（西班牙国家研究委员会金奖）
- honorary doctor of the University of Alicante（阿利坎特大学荣誉博士）
- Fellow of the American Physical Society；Fellow of the American Association for the Advancement of Science

## 9. 机构清单

- 教育：Omaha Central High School → University of Nebraska–Lincoln（B.S. 1957，物理与数学）→ University of California, Berkeley（PhD 1961，物理学）
- 任职：University of Pennsylvania（1962–1982 教职）→ University of California, Santa Barbara（1982– 物理系与材料系教授）
- 创业关联：Uniax（创始人之一，后被 DuPont 收购）、Konarka、Sirigen（2003，Bazan/Dietzen/Gaylord 创办）

## 10. 终审清单

- [ ] 生卒：1936-01-22 生于 Sioux City, Iowa；**在世**（全篇无卒日、无享年表述）
- [ ] 2000 化学奖三人共享表述准确；citation 用本地页面英文原句
- [ ] 博士年份取 1961（正文）；导师 Alan M. Portis
- [ ] 宾大 1962–1982 → UCSB 1982– 任职轨迹准确
- [ ] SSH 模型只写页面实载的"由导电聚合物工作引出、是拓扑绝缘体的简单模型"
- [ ] 创业公司角色表述准确（Uniax 是创始人；Sirigen 不是）
- [ ] 门生仅 Park Yung-woo / Fan Chunhai（postdoc）；Lee Kwang-hee 不出现
- [ ] 引语仅自传一段，可在 page.md 原文找到；中文引号内无杜撰"原话"
- [ ] 肖像：REST API 成功则用真实照片，否则装饰圆占位并在本清单如实勾选
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Alan_J._Heeger/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：真实照片或装饰圆占位，图注与来源一致
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：仅自传一段，必须在 Wikipedia 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐

---

> **名单状态**：chem-batch-25（2000 三人组之一）；`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不负责改总表。
