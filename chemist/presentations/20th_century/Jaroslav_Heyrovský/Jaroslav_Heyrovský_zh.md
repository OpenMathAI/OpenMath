# Jaroslav Heyrovský（雅罗斯拉夫·海罗夫斯基）立传提示词

> qid=Q157701 · 1890-12-20 – 1967-03-27 · 捷克化学家 · 20 世纪 · 诺贝尔化学奖（1959，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Jaroslav_Heyrovský/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（本页 images.txt 若无肖像则用装饰圆占位并注明"页面无可用肖像"）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace 极谱法的发明者\enspace·\enspace 捷克斯洛伐克`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育（布拉格查理大学/UCL）、博士（1918 布拉格）、师承（Ramsay/Donnan）、核心领域、荣誉（ForMemRS）。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「滴汞电极上的电流—电压曲线」母题——离散圆点暗示极谱波的阶梯形波形。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（Ilkovič 方程式属页面无载禁写，可改放极谱波示意/电化学还原通式并注明"示意"）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Jaroslav Heyrovský（中文惯称：雅罗斯拉夫·海罗夫斯基；头衔 ForMemRS）
- **生卒**：1890-12-20 生于布拉格（时属奥匈帝国波希米亚王国）→ 1967-03-27 逝于布拉格（捷克斯洛伐克），享年 76；安葬于布拉格 Vyšehrad 公墓
- **国籍**：Czechoslovakia（捷克斯洛伐克；出生时为奥匈帝国）
- **身份**：化学家与发明家（chemist and inventor；极谱法发明人）
- **家庭**：第五子；父 Leopold Heyrovský 为布拉格查理大学罗马法教授，母 Clara（娘家姓 Hanl von Kirchtreu）。1926 年娶 Marie（Mary）Koranová，育一女 Jitka、一子 Michael
- **教育轨迹**：
  - 中学教育至 1909 年
  - 1909 起在布拉格查理大学修化学、物理与数学
  - 1910–1914 就读 University College London（师从 Sir William Ramsay、W. C. McC. Lewis、F. G. Donnan），1913 年 BSc；对 Donnan 的电化学尤为倾心
  - 一战期间在军医院任药剂化学师与放射线技师
  - 1918 年于布拉格获 PhD；1921 年于伦敦获 DSc
- **导师**：infobox 博士导师双载 Frederick G. Donnan 与 William Ramsay（UCL 时期）；PhD 学位实为 1918 年布拉格查理大学
- **研究领域**：电化学——极谱法（polarography）、物理化学、分析化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **法学教授之家（1890）**：布拉格，罗马法教授的第五子——人文家庭里走出的电化学家。
2. **UCL 求学（1910–1914）**：Ramsay、Lewis、Donnan 三位教授门下；尤其追随 Donnan 研究电化学。
3. **一战军医院（1914–1918）**：任药剂化学师与放射线技师，得以继续学业——1918 布拉格 PhD、1921 伦敦 DSc。
4. **布拉格起步**：任查理大学分析化学研究所 B. Brauner 教授助手；1922 年升 Associate Professor。
5. **极谱法诞生（1922）**：发明极谱法（polarographic method）——此后毕生科学活动皆投入这一电化学新分支的开拓。
6. **布拉格第一位物理化学教授（1926）**：成为查理大学首位物理化学教授。
7. **捷克极谱学派**：在大学内培养形成捷克极谱学家学派，本人始终站在极谱研究最前沿。
8. **全球讲学（1933–1961）**：1933 美国、1934 苏联、1946 英格兰、1947 瑞典、1958 中国、1960/1961 埃及（U.A.R.）。
9. **极谱研究所（1950）**：出任新设立的极谱研究所所长；1952 年该所并入捷克斯洛伐克科学院。
10. **1959 诺贝尔化学奖**：表彰其极谱法的发明（page.md 口径 "for his invention of polarography"）；1959-12-11 诺奖演讲 "The Trends of Polarography"。
11. **国际荣誉网**：美国艺术与科学院荣誉会员（1933）、匈牙利科学院（1955）、印度科学院班加罗尔（1955）、波兰科学院（1962）、德国科学院柏林通讯会员（1955）、Leopoldina（1956）、丹麦皇家科学院外籍会员（1962）、伦敦极谱学会主席暨首位荣誉会员、日本极谱学会荣誉会员。
12. **ForMemRS（1965）**：当选皇家学会外籍会员；1927 年已当选 UCL Fellow。
13. **月球环形山**：月球上的 Heyrovský 环形山以其命名；布拉格 Kaprova 街有纪念牌。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深靛蓝 deepindigo） | `#123C5B` | 极谱曲线的深邃与电化学的理性（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（极谱法 badgePola） | `#2E5A9E` | 蓝滴汞电极 / 极谱波 |
| 分类色 2（电化学 badgeElec） | `#1B7A43` | 绿电化学分支开拓 |
| 分类色 3（极谱研究所 badgeInst） | `#D97B29` | 琥珀 1950 建所 / 1952 入科学院 |
| 分类色 4（国际荣誉 badgeHonor） | `#8E44AD` | 紫ForMemRS / 全球讲学 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「极谱波的阶梯」排列。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Pathfinder** — Ghostwriter Music（Composed by Daniel Beijbom；文件路径见 manifest `music_audio/inspiring-electronic/23-GiwYLGgJw7w-...`；**不要复制 wav 文件**）
- **风格**：开拓感 / 明快 / 现代纪实
- **匹配理由**：
  - "Pathfinder（开拓者）" 直指其身份——从零开创极谱法这一全新分支，并形成整个学派
  - "明快纪实" 匹配仪器方法类科学家的气质——不是思辨者，是把测量做进历史的工程师型学者
  - 曲名呼应其一生单点深耕：1922 年发明 → 1950 年建所 → 1959 年诺奖
- **时长**：以实际文件为准 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 极谱法的发明者 / Jaroslav Heyrovský 1890–1967 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  海罗夫斯基的一生 — Sanger 式时间线（10 节点：1890→1910→1913→1918→1921→1922→1926→1950→1959→1967）
04  布拉格与伦敦（1890–1914）— 表格「时间|事件|结果」（法学教授之子 → Charles University → UCL 三师门下）
05  一战与双学位（1914–1921）— 表格「处境|坚持|结果」（军医院 → 1918 PhD 布拉格 → 1921 DSc 伦敦）
06  极谱法的诞生 (1922) — 表格「问题|方法|结果」+ 公式框：极谱波电流—电压示意
07  学派与讲席 (1922–1926) — 表格「职位|方向|意义」（Brauner 助手 → Associate Prof → 首位物理化学教授）
08  全球讲学 (1933–1961) — 表格「年份|地点|意义」（美/苏/英/瑞典/中国/埃及）
09  极谱研究所 (1950/1952) — 表格「事件|年份|意义」+ Sanger FFT 页式流程图（1950 建所 → 1952 入科学院）
10  1959 诺贝尔化学奖 — 表格「领域|贡献|认可」+ 公式框：获奖口径原文（"for his invention of polarography"）
11  国际荣誉网 — Sanger 式「类别|代表|意义」表格（科学院会员/荣誉博士/极谱学会）
12  家庭与身后 — 表格「人物|关系|注」（妻 Marie Koranová、子女 Jitka/Michael、Vyšehrad 公墓、月球环形山）
13  遗产：电分析化学的奠基 — 四分类遗产盒 + 公式框：从极谱法到现代电分析
14  结尾 — 「一滴悬汞，称出了溶液里每一种离子的重量。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1959 诺奖 | **独享**；page.md 只给出 "for his invention of polarography" 口径——完整官方 citation（"…and development of the polarographic methods of analysis"）**页面无载，禁写** |
| 博士学位归属 | PhD 为 1918 **布拉格查理大学**（战时军医院工作期间完成）；UCL 只授 BSc（1913）与 DSc（1921）——勿写"博士毕业于 UCL" |
| 博士导师 | infobox 双载 Donnan 与 Ramsay（UCL 时期导师）；两人名按 infobox 入库，note 须注明 UCL 时期——勿写"布拉格博士导师" |
| 发明年份 | 极谱法 "dates from 1922"——勿写 1920 或 1923；1926 是升任物理化学教授 |
| 国籍口径 | 出生时为奥匈帝国波希米亚，殁于捷克斯洛伐克——国籍按 page.md 写 Czechoslovakia，叙事注明"出生时属奥匈帝国" |
| 妻子姓名 | Marie（Mary）Koranová，1926 年结婚——勿写错昵称位置 |
| 子女 | 女 Jitka、子 Michael——勿增删 |
| ForMemRS | **1965 年**当选（"in 1965"）；1927 年当选的是 UCL Fellow——两个年份勿混 |
| 国家荣誉 | 1951 State Prize First Grade、1955 Order of the Czechoslovak Republic——勿与诺贝尔年混排 |
| 荣誉博士 | Dresden 1955 / Warsaw 1956 / Aix-Marseille 1959 / Paris 1960——年份各归各校 |
| 讲学地点 | 1958 年在中国讲学、1960 与 1961 在埃及（U.A.R.）——勿增删站点 |
| 引语 | page.md 正文无直接引语——全文禁用引号"原话"（仅诺奖口径英文一处） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q157701 | ✅ |
| name_zh | 雅罗斯拉夫·海罗夫斯基 | ✅ |
| name_en | Jaroslav Heyrovský | ✅ |
| birth_date | 1890-12-20 | ✅ |
| death_date | 1967-03-27 | ✅ |
| nationality | Czechoslovakia | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | polarography（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（立传 Beamer 完成后置 1） | ✅ |

**person_field 细分 rank 表**：

| name_en | rank | name_zh | 依据 |
|---|---|---|---|
| polarography | 0 | 极谱法 | 1959 诺奖理由 |
| electrochemistry | 1 | 电化学 | page.md 明载新分支 |
| physical chemistry | 2 | 物理化学 | 布拉格首位物理化学教授 |
| analytical chemistry | 3 | 分析化学 | 极谱分析方法属性 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Frederick G. Donnan | 师→生（UCL 导师） | 1910–1914 UCL 师从 Donnan 研电化学；infobox 博士导师 |
| advisor-student | William Ramsay | 师→生（UCL 导师） | 1910–1914 UCL 师从 Ramsay；infobox 博士导师 |
| colleague | B. Brauner | 无向 | 大学职业生涯起步：Brauner 分析化学研究所助手 |
| spouse | Marie Koranová | 无向 | 1926 结婚；育女 Jitka、子 Michael |

> **禁入库名单（page.md 无人际明载）**：W. C. McC. Lewis（仅并列授课教师，非导师）、Klement Gottwald（奖项名非人）、各国科学院（机构非人）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1959，独享；"for his invention of polarography"）
- Klement Gottwald State Prize, First Grade（1951）
- Order of the Czechoslovak Republic（1955）
- Foreign Member of the Royal Society，ForMemRS（1965）
- 荣誉博士：Technical University Dresden（1955）、University of Warsaw（1956）、University Aix-Marseille（1959）、University of Paris（1960）
- 荣誉会员：American Academy of Arts and Sciences（1933）、Hungarian Academy of Sciences（1955）、Indian Academy of Sciences, Bangalore（1955）、Polish Academy of Sciences（1962）
- Corresponding Member, German Academy of Sciences, Berlin（1955）；German Academy of Natural Scientists Leopoldina（1956）；Foreign Member, Royal Danish Academy of Sciences, Copenhagen（1962）
- Polarographic Society, London 主席暨首位荣誉会员；日本极谱学会荣誉会员；捷克斯洛伐克/奥地利/波兰/英格兰/印度化学会荣誉会员
- University College, London Fellow（1927）

## 9. 机构清单

- 教育：布拉格查理大学（1909 起；PhD 1918）；University College London（1910–1914，BSc 1913；DSc 1921）
- 任职：查理大学分析化学研究所（Brauner 助手）→ Associate Professor（1922）→ 首位物理化学教授（1926）；极谱研究所所长（1950–）；1952 年该所并入捷克斯洛伐克科学院
- 公职：International Union of Physics 副主席（1951–1957）
- 纪念：月球 Heyrovský 环形山；布拉格 Kaprova 街纪念牌；安葬 Vyšehrad 公墓

## 10. 终审清单

- [ ] 生卒 1890-12-20 / 1967-03-27，享年 76，出生地与去世地均为布拉格（国名口径注明奥匈→捷克斯洛伐克）
- [ ] 1959 **独享**，获奖口径 "for his invention of polarography"（完整官方 citation 页面无载禁写）
- [ ] PhD 1918 布拉格；BSc 1913 / DSc 1921 伦敦——学位归属勿混
- [ ] 极谱法 1922 年发明；1926 首位物理化学教授；1950 建所
- [ ] ForMemRS 1965（勿与 1927 UCL Fellow 混淆）
- [ ] 全文无杜撰引语（page.md 无直接引语，一律间接转述）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Jaroslav_Heyrovský/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：核对 images/（无则装饰圆占位并注明）
- [ ] **国籍**：封面顶部明示捷克斯洛伐克
- [ ] **引语核对**：全文无引号"原话"（仅诺奖口径英文一处）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 等）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动该脚本。
