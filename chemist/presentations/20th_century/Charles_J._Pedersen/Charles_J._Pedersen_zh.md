# Charles J. Pedersen（查尔斯·佩德森）立传提示词

> qid=Q244998 · 1904-10-03 生于釜山（大韩帝国）– 1989-10-26 逝于美国新泽西 Salem · 美国有机化学家 · 诺贝尔化学奖（1987，与 Donald J. Cram、Jean-Marie Lehn 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Charles_J._Pedersen/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）。本页 infobox 与 images.txt 均无真实肖像——封面用**装饰圆占位**（主色实心圆 + 姓名缩写），插图用 images.txt 的 `18-crown-6-potassium.png`（冠醚配位钾离子）作核心贡献页插图。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{crown}\enspace 冠醚的发现者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（装饰圆）+ 右侧 2×2 信息网格，至少含：生卒、本名（Charles John Pedersen / 安井良男）、国籍、出生地/去世地、教育（Dayton / MIT）、博士（无——明载无 PhD）、核心领域、任职（DuPont 42 年）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「冠醚环 / 环状分子」母题——环形与圆点的包容意象。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Charles John Pedersen（日语名：安井 良男，Yasui Yoshio；中文惯称：查尔斯·佩德森）
- **生卒**：1904-10-03 生于釜山（大韩帝国）→ 1989-10-26 逝于美国新泽西州 Salem，享年 85
- **国籍**：United States（美国）；metadata 另载 Japan——生于朝鲜、父挪威人、母日本人，日本姓名安井良男（封面国籍行统一写美国，身份信息页注「生于釜山 · 挪威裔父 · 日裔母」）
- **身份**：美国有机化学家（DuPont 企业研究员 42 年）
- **家庭**：三个孩子中最小；父 Brede Pedersen 为挪威海事工程师，因家庭变故离乡赴朝鲜入海关系统，后在云山（Unsan County）矿区任机械工程师；母 Takino Yasui 随家自日本移居朝鲜，在云山矿区附近经营大豆与蚕茧贸易；兄在其出生前夭折，姐 Astrid 年长五岁；自述因母仍哀悼早夭兄长而不曾感到被欢迎（转述）。1947 年娶 Susan J. Ault，婚后定居 Salem, New Jersey；无子女（其致 Izatt 信 "I have no child of my own"——page.md 原文可引）
- **教育轨迹**：
  - 约 8 岁被送回日本长崎求学，后转入横滨 St. Joseph College（圣母会体系）
  - 1922 入 University of Dayton（俄亥俄）读化学工程——校网球队主力、高年级队长（教练 Frank Kronauge）、工程师俱乐部副主席
  - 1926 Dayton 化工学士 → MIT 有机化学硕士（导师 James F. Norris）；教授们劝其读博，他决定就业（部分因不愿再靠父亲供养）
- **博士**：无——page.md 明载 "He is one of the few people to win a Nobel Prize in the sciences without having a PhD"
- **研究领域**：有机化学、配位化学、大环化学（冠醚）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **釜山出生（1904）**：挪威工程师之父、日本商人之母，在朝鲜的美国云山矿区圈子里以英语长大——生于日俄战争前夕的东亚，终身以美国为家。
2. **长崎与横滨（约 1912–1922）**：约 8 岁赴长崎求学、转横滨圣母会学校——三国血脉的少年时代。
3. **Dayton 四年（1922–1926）**：化工为主业，网球队四个赛季、高年级队长、工程师俱乐部副主席、Daytonian 编辑部——全面均衡的学生。
4. **MIT 抉择（1926–1927）**：硕士毕业放弃博士（不愿再靠父亲供养）——日后成为极少数无博士学位的科学诺奖得主。
5. **杜邦 42 年（1927 起）**：经导师 James F. Norris 引荐入职杜邦 Wilmington；在 Jackson Laboratory 自 William S. Calcott 手下开始研究，终老于 Wilmington Experimental Station——一名彻底的工业化学家。
6. **聚合物黄金时代**：亲见 Julian Hill、Roy J. Plunkett 等的聚合物突破；自己早期聚焦氧化降解与稳定化，发展金属减活剂（metal deactivators）、大幅改进四乙基铅生产工艺、参与氯丁橡胶（neoprene）开发。
7. **转向配位化学（约 1960）**：应同事 Herman Schroeder 建议，先研究钒的配位化学再及聚合/氧化催化——正是这条路上冠醚不期而至。
8. **意外的 "goo"（约 1960）**：纯化 bis[2-(o-hydroxyphenoxy)ethyl] ether 时发现未知副产物——紫外光谱在碱处理后出现位移，追索钠离子效应，确认溶解度来自钠离子配位而非碱性。
9. **二苯并-18-冠-6（1967）**：该未知物行为如分子量加倍的 2,3-benzo-1,4,7-trioxacyclononane——命名为 dibenzo-18-crown-6，第一种芳香冠化合物；JACS *Cyclic polyethers and their complexes with metal salts*（89, 2495–2496）等两篇系统报道冠醚合成法。
10. **25 论文 · 65 专利**：42 年生涯 25 篇论文、65 项专利，65 岁退休——环状分子与碱金属离子形成稳定配合物，开启大环化学时代。
11. **1987 诺贝尔化学奖**：与 Donald J. Cram、Jean-Marie Lehn 共享——Pedersen 的二维冠醚、Cram 的三维分子、Lehn 的穴醚；杜邦全力护航（专职公关、兼职秘书、因不能乘商业航班而派公司专机送其全家赴斯德哥尔摩）。
12. **Izatt 与学术连接（1968）**：Reed M. Izatt 经芝加哥生理学家 George Eisenman 获知论文，成为杜邦之外第一位来访科学家并获赠冠醚样品；Izatt 的分子识别研究深受其影响。
13. **无后之憾与冠醚为嗣**：Izatt 在最后一次探望时发现其亲笔信 "Most men achieve 'Immortality' through their progeny. I have no child of my own. Possibly, the crown ethers will serve, in a small way, to mark my footprint on earth"——1983 确诊骨髓瘤、同年妻逝；1987 带病赴斯德哥尔摩，1989-10-26 逝于 Salem。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深藏青 deepnavy） | `#1E3A5F` | 工业化学的沉静与严谨（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（冠醚 badgeCrown） | `#2E5A9E` | 蓝冠醚 / 18-crown-6 |
| 分类色 2（配位化学 badgeCoord） | `#1B7A43` | 绿金属离子配位 / 钠钾识别 |
| 分类色 3（工业化学 badgeIndustry） | `#D97B29` | 琥珀杜邦 42 年 / 65 专利 |
| 分类色 4（超分子先声 badgeSupra） | `#C0395B` | 玫瑰大环化学 / 超分子先声 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——环形与圆点，呼应「冠醚环抱金属离子」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Empire Collapse** — Cold Cinema（清单预分配，勿复制 wav 文件，Makefile 引用源路径）
- **文件**：`music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`
- **风格**：电影感 / 低沉 / 壮阔史诗
- **匹配理由**：
  - "Empire Collapse" 呼应 20 世纪工业帝国与旧时代的落幕——一位生于帝国夹缝（大韩帝国）的化学家的一生
  - 低沉 drone 底色匹配其孤独的工业研究员形象——42 年一间实验室、无博士学位、83 岁迟来的加冕
  - 史诗感托住 "crown ethers as my footprint" 的终章独白
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 冠醚的发现者 / Charles J. Pedersen 1904–1989 + 四色 badge + 右上装饰圆头像 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/本名安井良男/国籍/出生地釜山/教育/无博士/领域/DuPont 42 年/家庭/荣誉）
03  佩德森的一生 — 高斯式时间线（10 节点：1904→1912→1922→1927→1960→1967→1983→1987→1989→遗产）
04  早年：釜山·长崎·横滨 (1904–1922) — 表格「时间|事件|结果」（三国血脉与英语童年）
05  Dayton 与 MIT：放弃博士的抉择 (1922–1927) — 表格「时间|事件|结果」
06  杜邦 42 年 (1927–1969) — 表格「阶段|研究|成果」（氧化稳定化/金属减活剂/四乙基铅/neoprene）
07  意外的 goo：冠醚发现 (约 1960) — 表格「问题|方法|结果」+ 公式框：dibenzo-18-crown-6 配位 Na+
08  1967 双论文与冠醚命名 — 表格「问题|方法|结果」+ 18-crown-6-potassium 结构图
09  1987 诺贝尔化学奖 — 表格「得主|贡献|维度」（二维冠醚/三维 Cram/穴醚 Lehn）+ 获奖口径
10  Izatt 与学术连接 — 表格「人物|事件|意义」（Izatt 1968 首访 / Eisenman 牵线）
11  无冕之王的独白 — 高斯式「类别|代表|意义」表格 + Izatt 信件引文框（"Most men achieve 'Immortality'..."）
12  迟来加冕 — 高斯 FFT 页式流程图（1983 确诊→妻逝→1987 斯德哥尔摩专机→杜邦奖章→1989 谢幕）
13  遗产：从冠醚到分子机器 — 四分类遗产盒 + 2016 分子机器诺奖的先声（page.md Legacy 口径）
14  结尾 — 「一个意外的 'goo'，撑起了一个新化学时代。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 出生地口径 | 生于**釜山（大韩帝国）**；勿写"韩国人"——国籍按 metadata 为 United States + Japan；身份页注「生于釜山 · 挪威裔父 · 日裔母 · 日语名安井良男」 |
| 韩国出生诺奖者 | page.md 明载 "one of three Nobel Prize laureates born in Korea"（另两位 Kim Dae-jung、Han Kang）——可写但保持"出生于朝鲜半岛"口径 |
| 无博士 | 明载 "one of the few people to win a Nobel Prize in the sciences without having a PhD"——放弃读博原因是"不再愿靠父亲供养"，勿写其他原因 |
| 1987 诺奖口径 | 与 Cram、Lehn 三人共享；Pedersen 贡献是**发现冠醚并描述其合成法**；官方精确 citation 本地页面无载，禁杜撰全句 |
| 三人维度 | Pedersen 二维环形、Cram 三维空间、Lehn 穴醚与超分子化学——维度勿混 |
| 冠醚发现年份 | page.md 叙事为 "At around 1960" 回到配位化学研究后意外发现 goo；1967 是双论文发表年——两个年份勿混为一谈 |
| Izatt 探望年份 | 原文 "In Izatt's last visit with Pedersen prior to his death in 1988" 语义为"1988 年 Pedersen 在世时/卒前的最后探望"（Pedersen 1989 卒）——引用信件时勿写死探望精确日期 |
| 引语白名单 | 可整句引用仅 Izatt 信 "Most men achieve 'Immortality' through their progeny..." 一处；其余全篇间接转述 |
| 同名区分 | 日语名汉字「安井 良男」固定；勿与其他 Pedersen 混淆 |
| 妻子卒日 | Susan J. Ault 1983-02-08 去世（72 岁）——与其确诊骨髓瘤同年，叙事顺序勿倒置 |
| 专利与论文 | 25 篇论文 + 65 项专利是"65 岁退休时"的累计口径——勿写"冠醚相关 65 项专利" |
| neoprene 口径 | 页面只载 "contributed to the development of neoprene"（参与开发）——勿写"发明氯丁橡胶" |
| 长崎就学年龄 | "At around 8 years old"——约 8 岁，勿写精确年份 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q244998 | ✅ |
| name_zh | 查尔斯·佩德森 | ✅ |
| name_en | Charles J. Pedersen | ✅ |
| birth_date | 1904-10-03 | ✅ |
| death_date | 1989-10-26 | ✅ |
| nationality | United States（rank 0）+ Japan（rank 1，metadata 口径） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分见下表） | ✅ |
| has_biography | 0（待 Beamer 后置 1） | ✅ |

person_field 细分 rank 表：

| name_en | rank | name_zh |
|---|---|---|
| organic chemistry | 0 | 有机化学 |
| coordination chemistry | 1 | 配位化学 |
| macrocyclic chemistry | 2 | 大环化学 |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 家庭**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | James F. Norris | 师→生（硕士研究导师） | MIT 有机化学硕士导师；1927 经其引荐入职杜邦 |
| co-honored | Donald J. Cram | 无向 | 1987 诺贝尔化学奖共同得主（Cram 拓展三维分子） |
| co-honored | Jean-Marie Lehn | 无向 | 1987 诺贝尔化学奖共同得主（Lehn 穴醚/超分子化学） |
| colleague | Reed McNeil Izatt | 无向 | 1968 杜邦之外首位来访科学家；冠醚推广与分子识别合作 |
| colleague | Herman Schroeder | 无向 | 杜邦同事，建议先研究钒配位化学 |
| spouse | Susan J. Ault | 无向 | 1947 结婚；1983-02-08 妻先逝 |

> metadata.json-only 一律不入库。本页禁入库名单：**William S. Calcott**（Jackson Laboratory 主管，"under" 为工作上级语义、关系类型不明）、**Julian Hill / Roy J. Plunkett**（仅"亲见并受启发"的群体叙述）、**George Eisenman**（牵线转告，一次性间接接触）、**Frank Kronauge**（大学网球教练）。无子女（其信自述）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1987，与 Cram、Lehn 共享）
- Lavoisier Medal for Lifetime Technical Achievement（metadata 载）
- DuPont Research Fellows 卓越奖章（1987 诺奖后）
- 65 项专利（职业生涯累计）

## 9. 机构清单

- 教育：长崎（约 8 岁起）→ St. Joseph College, Yokohama → University of Dayton（1922–1926，化工学士）→ MIT（有机化学硕士，导师 James F. Norris）
- 任职：DuPont（1927–约 65 岁退休，共 42 年）——Jackson Laboratory, Deepwater, NJ（起步，Calcott 手下）→ Experimental Station, Wilmington, DE（终老）
- 无博士、无学术教职——纯企业研究员

## 10. 终审清单

- [ ] 生卒 1904-10-03（釜山）/ 1989-10-26（Salem, NJ），享年 85
- [ ] 1987 三人共享（Cram、Lehn）表述准确；获奖理由不杜撰全句
- [ ] 无博士表述准确（放弃读博原因 = 不愿再靠父亲供养）
- [ ] 冠醚发现（约 1960 意外）与 1967 双论文两年份不混
- [ ] Izatt 信引文完整准确；Calcott/Hill/Plunkett/Eisenman/Kronauge 均未入库
- [ ] 国籍行美国、身份页注三国血脉与安井良男
- [ ] 引语仅白名单一处，其余间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Charles_J._Pedersen/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：本页无真实肖像——装饰圆占位；18-crown-6-potassium.png 作插图
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：仅 Izatt 信整句 + 其余间接转述
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像/装饰圆 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：`chemist/prompt_manifest.json` chem-batch-20 · Charles J. Pedersen（1987，BGM Empire Collapse，主色 #1E3A5F）。
> **开始执行。每完成一步向主控汇报。**
