# Kenichi Fukui（福井谦一）立传提示词

> qid=Q217734 · 1918-10-04 – 1998-01-09 · 日本化学家 · 20 世纪 · 诺贝尔化学奖（1981，与 Roald Hoffmann 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Kenichi_Fukui/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传模板**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 内若缺，先按常规流程下载 Wikipedia 肖像，404 则装饰圆占位；京都大学福井纪念碑照片可作插图备用）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 前线轨道的先行者\enspace·\enspace 日本`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。日文名并行标注：福井 謙一（Fukui Ken'ichi）。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育（京都帝国大学）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「前线轨道 / 波函数节面」母题——明暗相接的圆点暗示 HOMO/LUMO 的电子云。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 FMO 要义：HOMO（一方）× LUMO（另一方）的相互作用决定反应性。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Kenichi Fukui（福井 謙一，Fukui Ken'ichi；中文惯称：福井谦一）
- **生卒**：1918-10-04 生于奈良县生驹郡 → 1998-01-09 逝于京都，享年 79
- **国籍**：Japan（日本）
- **身份**：化学家（chemist；1981 诺贝尔化学奖得主——首位获诺贝尔化学奖的东亚裔）
- **家庭**：三兄弟中的长子；父 Ryokichi Fukui（外贸商人）、母 Chie Fukui；1947 年娶 Tomoe Horie，育有一子 Tetsuya 与一女 Miyako
- **教育轨迹**：
  - 学生时代（1938–1941）被量子力学与薛定谔方程激发兴趣
  - 京都帝国大学工业化学专业（父向挚友 **Gen-itsu Kita** 教授咨询后定下的方向）
  - 1941 毕业于京都帝国大学
- **博士导师**：Shinjiro Kodama（infobox 明载）
- **研究领域**：理论化学——前线分子轨道理论、量子化学、反应机理、聚合动力学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **奈良商人之家长子（1918）**：外贸商人之子，中学时代化学竟非最爱——「选化学的理由并不容易解释」。
2. **父亲的咨询（1930s）**：父向京都帝大 **Gen-itsu Kita** 教授求教，福井由此进入工业化学专业——他自述这是"教育生涯中最决定性的事件"。
3. **量子力学的召唤（1938–1941）**：学生时代迷上量子力学与薛定谔方程；形成终生信念——「科学的突破来自相距遥远领域的意外融合」。
4. **战时燃料实验室（1941–1943）**：毕业后入日本陆军燃料研究所服役；1943 年受任京都帝大燃料化学讲师，从此开始实验有机化学家生涯。
5. **一百个实验（1940s）**：早期完成 100 余个实验项目与论文；后来他反其道而行——给学生**布置实验课题**以平衡其理论倾向。
6. **京都帝大教授（1951–1982）**：1951 年任物理化学教授，执掌讲席三十一年。
7. **1952 年的惊雷**：与年轻合作者 **T. Yonezawa、H. Shingu** 在 *Journal of Chemical Physics* 发表芳香烃反应性的分子轨道理论——当时**几乎无人理会**。
8. **诺奖演讲的自省（1981）**：福井在演讲中说原始论文 'received a number of controversial comments'，并自陈理论根基 "was obscure or rather improperly given"（因自己经验能力不足）——先知式的寂寞。
9. **1965 年的追认**：Woodward 与 Hoffmann 的立体选择规则发表后，前线轨道概念才被广泛认可；福井在诺奖演讲中坦言 'It is only after the remarkable appearance of the brilliant work by Woodward and Hoffmann that I have become fully aware...'。
10. **FMO 理论三观察**：不同分子的占据轨道相互排斥；一方正电荷吸引另一方负电荷；一方的占据轨道与另一方的未占据轨道（尤其 HOMO–LUMO）相互作用产生吸引——反应性由此简化为 HOMO/LUMO 的对话。
11. **没有大计算机的时代**：福井的核心思想诞生于化学家尚无大型计算机建模的年代——纯理论直觉的胜利。
12. **多面的化学家**：除反应理论外，尚有凝胶化的统计理论、无机盐参与有机合成、聚合动力学等贡献；著《Theory of Orientation and Stereoselection》（1975）。
13. **日本的科学批评者（1985）**：接受 *New Scientist* 访谈，直陈日本大学讲席制的等级森严束缚年轻人原创、产业界难投入纯粹化学——「即使年轻人当不上早期副教授，也应鼓励他们做原创工作」。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青深绿 darkteal） | `#0B5351` | 量子化学的深邃与京都的沉稳（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（前线轨道 badgeFMO） | `#2E5A9E` | 蓝 HOMO/LUMO 相互作用 |
| 分类色 2（反应机理 badgeMech） | `#1B7A43` | 绿立体选择规则呼应 |
| 分类色 3（聚合与凝胶 badgePoly） | `#D97B29` | 琥珀聚合动力学 / 凝胶统计理论 |
| 分类色 4（科学与教育 badgeSci） | `#C0395B` | 玫瑰讲席制批评 / 理论与实验的平衡 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「波函数节面」明暗相接的圆点几何。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（文件 `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`，不复制 wav）
- **风格**：探索 / 开拓 / 理性昂扬
- **匹配理由**：
  - "探索" 匹配 FMO 理论的先行者姿态——在没有大计算机的年代独闯量子化学荒原
  - "开拓" 匹配「远隔领域融合」的信念——工业化学出身的实验家写出理论化学的世纪之作
  - "理性昂扬" 匹配 1985 访谈中的锋芒——对日本科学体制的直言是另一种远征
- **时长**：以实际曲目时长为准，超过 15 页 × 7 秒由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 前线轨道的先行者 / Kenichi Fukui 1918–1998 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  福井的一生 — 时间线（10 节点：1918→1941→1943→1947→1951→1952→1962→1981→1988→1998）
04  早年：奈良与父亲的咨询 (1918–1941) — 表格「时间|事件|结果」+ Kita 教授的指路
05  战时与讲席之路 (1941–1951) — 表格「阶段|机构|结果」（陆军燃料研究所 → 京都帝大讲师 → 教授）
06  1952 年的惊雷 — 表格「问题|方法|结果」+ 公式框：芳香烃反应性的 MO 理论（Yonezawa/Shingu 合作）
07  前线轨道理论 — 表格「观察|内容|推论」+ 公式框：HOMO × LUMO 相互作用三观察
08  迟到的追认 (1965) — 表格「事件|内容|意义」+ Woodward–Hoffmann 规则与福井的自省引语
09  1981 诺贝尔化学奖 — 表格「人物|方法|贡献」+ 公式框：福井与 Hoffmann 各自独立的机理研究
10  理论与实验的平衡 — 表格「特质|表现|结果」（百个实验/布置实验课题/无计算机时代）
11  荣誉清单 — 「类别|代表|意义」表格（含 itemize 荣誉清单）
12  京都的 institutions — 流程图页（京大教授 → 工艺纤维大学校长 1982–88 → 基础化学研究所长 1988–98）
13  遗产：科学批评与东亚第一人 — 四分类遗产盒 + 公式框：远隔领域的融合
14  结尾 — 「反应为何发生？他回答说：去看前线。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1981 诺奖口径 | 与 Roald Hoffmann **共享**，理由是两人的**各自独立**研究（"for their independent investigations into the mechanisms of chemical reactions"）——勿写成两人合作 |
| "东亚第一人"表述 | page.md 明载 "the first person of East Asian ancestry to be awarded the Nobel Prize in Chemistry"——照原文口径，勿扩写成"亚洲首位诺奖"或"日本首位" |
| 引语归属 | "选化学的理由并不容易解释…" 与 1981 诺奖演讲两段引语出自 *The Chemical Intelligencer* 访谈/诺奖演讲（page.md 转载）——注明出处；1985 批评引语出自 *New Scientist* 访谈 |
| 理论遭冷遇 | 1952 论文"failed to garner adequate attention"——冷遇是**当年的**状态，勿写成一生被忽视；1965 Woodward–Hoffmann 后获认可 |
| Woodward–Hoffmann | 福只是**承认其工作使自己充分意识到轨道节面性质的意义**——勿写成 Woodward-Hoffmann 抢先或剽窃 |
| frontmatter 噪声 | field_of_work 写作 "chemist"（词条噪声）——以 chemistry / theoretical chemistry 为准 |
| 国籍条目 | frontmatter 含 "Empire of Japan"——正文统一用 Japan，帝国时期仅在时间线语境出现 |
| 师承 | 博士导师 Shinjiro Kodama 仅 infobox 明载；Gen-itsu Kita 是**报考方向的建议者**（非正式导师），以 influence 入库 |
| 合作者名 | T. Yonezawa / H. Shingu 仅缩写名（page.md 未给全名）——正文可写，**不入库**（防分裂 stub） |
| 博士生 | Keiji Morokuma、Gernot Frenking 仅 infobox 明载二人——勿添加 |
| 任职年份 | 京大物理化学教授 1951–1982；工艺纤维大学校长 1982–1988；基础化学研究所长 1988–逝世；日本化学会长 1983–84——勿错置 |
| 荣誉年份 | 日本学士院奖 1962、文化勋章 1981、文化功劳者 1981、旭日大绶章 1988、ForMemRS 1989——年份照 infobox/正文 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q217734 | ✅ |
| name_zh | 福井谦一 | ✅ |
| name_en | Kenichi Fukui | ✅ |
| birth_date | 1918-10-04 | ✅ |
| death_date | 1998-01-09 | ✅ |
| nationality | Japan | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：theoretical chemistry / frontier molecular orbital theory / quantum chemistry / reaction mechanism，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 门生**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Shinjiro Kodama | 师→生（博士导师） | infobox 明载 |
| advisor-student | Keiji Morokuma | 福井 → 学生 | 博士生（infobox） |
| advisor-student | Gernot Frenking | 福井 → 学生 | 博士生（infobox） |
| influence | Gen-itsu Kita | 无向 | 京都帝大教授，其建议使福井进入工业化学专业 |
| co-honored | Roald Hoffmann | 无向 | 1981 诺贝尔化学奖共同得主，各自独立研究 |

**家庭**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Tomoe Horie | 无向 | 1947 结婚 |

> **禁入库名单**：T. Yonezawa / H. Shingu（1952 论文合作者，page.md 仅缩写名，无法给出规范全名，防分裂 stub）；Robert B. Woodward（仅理论呼应，无直接个人关系）；Ryokichi / Chie Fukui（父母，背景叙述）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1981，与 Roald Hoffmann 共享）
- Japan Academy Prize（1962）
- Order of Culture 文化勋章（1981）
- Person of Cultural Merit 文化功劳者（1981）
- Grand Cordon of the Order of the Rising Sun 旭日大绶章（1988）
- Schrödinger Medal（年份未载）
- Foreign Member of the Royal Society, ForMemRS（1989）
- International Academy of Quantum Molecular Science 会员；International Academy of Science, Munich 名誉会员

## 9. 机构清单

- 教育：京都帝国大学工业化学专业（1941 毕业）
- 任职：日本陆军燃料研究所（1941–1943）→ 京都帝国大学燃料化学讲师（1943）→ 京都大学物理化学教授（1951–1982）→ 京都工艺纤维大学校长（1982–1988）→ 基础化学研究所所长（1988–1998 逝世）
- 学会：日本化学会会长（1983–84）
- 纪念：京都大学校内福井纪念碑

## 10. 终审清单

- [ ] 生卒 1918-10-04 / 1998-01-09，享年 79，出生地奈良、去世地京都
- [ ] 1981 共享（Hoffmann）且"各自独立"表述准确
- [ ] "东亚裔首位化学诺奖"口径与 page.md 原文一致
- [ ] 1952 遭冷遇 → 1965 追认的因果链照原文
- [ ] 引语出处（The Chemical Intelligencer / Nobel lecture / New Scientist）均已标注
- [ ] Yonezawa/Shingu 未入库、Kita 以 influence 入库的裁定已落实
- [ ] 任职年份（京大/工纤大/基础研/化学会长）无错置
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Kenichi_Fukui/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：下载 Wikipedia 肖像（250px→500px；404 用 REST API 查 infobox 原图名；仍失败装饰圆占位）
- [ ] **国籍**：封面顶部明示日本
- [ ] **引语核对**：引语必须在 page.md 转载的原文中找到（三处访谈/演讲引语）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt、hbox≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；日文名假名与罗马字标注一致
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
