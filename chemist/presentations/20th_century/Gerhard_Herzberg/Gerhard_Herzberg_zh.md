# Gerhard Herzberg（格哈德·赫茨贝格）立传提示词

> qid=Q76602 · 1904-12-25 – 1999-03-03 · 德裔加拿大物理化学家 · 20 世纪 · 诺贝尔化学奖（1971，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Gerhard_Herzberg/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 `images.txt` / Commons 下载；404 则用装饰圆占位并在 Review 记录）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{broadcast-tower}\enspace 分子光谱的圣经作者\enspace·\enspace 加拿大`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、全名、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「分子光谱线」母题——离散圆点暗示光谱中一根根分立的谱线。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Gerhard Heinrich Friedrich Otto Julius Herzberg（中文惯称：格哈德·赫茨贝格；头衔 PC CC FRSC FRS）
- **生卒**：1904-12-25 生于德国汉堡 → 1999-03-03 逝于加拿大安大略省渥太华，享年 94
- **国籍**：Canada（加拿大公民）；生于德国——nationalities 多条带 rank
- **身份**：物理学家与物理化学家（physicist & physical chemist）、1971 年诺贝尔化学奖得主；1973–1980 任 Carleton University 校监
- **家庭**：父 Albin H. Herzberg（1914 年因水肿与心脏并发症去世，年仅 43）、母 Ella Biber；兄 Walter（1904-01 生）；家庭是无神论者（hidden）。1929 年娶 Luise Herzberg（娘家姓 Oettinger）——光谱学家、同行研究者；Luise 1971 年去世
- **教育轨迹**：
  - Gelehrtenschule des Johanneums（汉堡中学；出麻疹晚入学，父逝后不久毕业）
  - Technische Universität Darmstadt（靠私人奖学金就读；1928 年获 Dr.-Ing.）
  - 博士后（1928–30）：哥廷根大学与布里斯托尔大学——随 James Franck、Max Born、John Lennard-Jones
- **博士导师**：Hans Rau（达姆施塔特）
- **研究领域**：原子与分子光谱学、双原子/多原子分子结构、自由基、天体化学分析

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **汉堡圣诞之子（1904）**：圣诞日出生；11 岁丧父；曾立志天文学，汉堡天文台回信劝退——"没有私人财力别干天文"。
2. **达姆施塔特工科博士（1928）**：靠私人奖学金在 TU Darmstadt 师从 Hans Rau 完成 Dr.-Ing.。
3. **哥廷根-布里斯托尔博士后（1928–1930）**：随 Franck、Born、Lennard-Jones——量子力学黄金年代的现场亲历者。
4. **纳粹阴影（1933–1935）**：1933 年纳粹立法禁止"犹太人配偶"的男性在大学任教；妻子 Luise 是犹太人——1935 年夫妇离开德国时**每人只被允许携带相当于 2.50 美元的现金**与随身物品。
5. **萨斯喀彻温的新生（1935–1945）**：曾来访的物理化学家 John Spinks 帮他在萨斯喀彻温大学谋得职位——1935 客座教授、1936–45 物理学教授；1939 当选加拿大皇家学会会士。
6. **叶凯士与 NRC（1945–1948）**：芝加哥大学叶凯士天文台光谱学教授（1945–48）→ 1948 任加拿大国家研究委员会（NRC）纯粹物理部主任。
7. **分子光谱的圣经（1950 前后）**：《Atomic Spectra and Atomic Structure》与四卷本《Molecular Spectra and Molecular Structure》——被同行称为 "the spectroscopist's bible"。
8. **双原子与多原子（1950s）**：用光谱技术确定双原子与多原子分子的结构——1951 当选伦敦皇家学会会士（FRS）；1956–57 加拿大物理学家协会主席；1957–63 IUPAP 副主席。
9. **自由基猎手（★ 核心贡献）**：自由基用其他手段极难研究，赫茨贝格用光谱把它们一一定结构——1971 年诺奖演讲 *Spectroscopic Studies of Molecular Structure*。
10. **1971 诺贝尔化学奖（独享）**：理由 "for his contributions to the knowledge of electronic structure and geometry of molecules, particularly free radicals"；颁奖词称他为"举世公认的首要分子光谱学家"。
11. **天文化学的开拓**：把分子光谱用于**天体化学分析**——自由基本领恰好成为解读星际分子的钥匙（Herzberg 天体物理研究所以他命名）。
12. **荣誉满载**：Tory Medal（1953）、Bakerian Medal & Lecture（1960）、Frederic Ives Medal（1964）、Willard Gibbs Award（1969）、Faraday Lectureship Prize（1970）、Royal Medal（1971）、Companion of the Order of Canada（1968）、1992 年入加拿大枢密院。
13. **身后之名**：小行星 3316 Herzberg、NSERC 加拿大科学与工程金质奖（2000 年设，加拿大最高科研奖）、Carleton 的 Herzberg 实验楼、John Abbott College 主楼、Saskatoon 的 Herzberg 公园——1999-03-03 逝于渥太华。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（赭红 ochred） | `#A63A2B` | 枫叶与光谱焰色的暖调（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（分子光谱 badgeSpec） | `#1E4E79` | 蓝双原子/多原子结构 |
| 分类色 2（自由基 badgeRadical） | `#C0395B` | 玫瑰红自由基（核心贡献主视觉） |
| 分类色 3（流亡与新生 badgeExile） | `#6E4A1E` | 暗金 1935 离德 / 萨斯喀彻温 |
| 分类色 4（天文化学 badgeAstro） | `#2E5A5E` | 青星际分子 / Herzberg 天体物理研究所 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「分子光谱的分立谱线」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Through the Darkness** — Audiomachine（文件：`music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`；不要复制 wav 到人物目录，video 阶段按路径引用）
- **风格**：穿越黑暗 / 史诗 / 坚毅
- **匹配理由**：
  - "穿越黑暗" 匹配其人生主线——纳粹迫害、被迫离德、每人仅 2.50 美元起步，最终在加拿大登顶诺奖
  - "坚毅" 匹配光谱学家长跑——四十年如一日打磨一套方法
  - "史诗" 匹配从汉堡到渥太华、从原子到星际的科学版图
- **时长核对**：video 阶段用 ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 分子光谱的圣经作者 / Gerhard Herzberg 1904–1999 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/全名/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  赫茨贝格的一生 — Sanger 式时间线（10 节点：1904→1928→1930→1935→1945→1948→1951→1971→1973→1999）
04  汉堡童年与天文学之梦 (1904–1922) — 表格「时间|事件|结果」（天文台劝退）
05  达姆施塔特与量子年代 (1922–1930) — 表格「阶段|导师|结果」（Rau / Franck / Born / Lennard-Jones）
06  纳粹阴影与出走 (1933–1935) — 表格「时间|事件|结果」+ 数字框：每人 2.50 美元
07  萨斯喀彻温与 NRC (1935–1948) — 表格「时间|机构|结果」（Spinks 引路 / 叶凯士 / NRC 主任）
08  分子光谱的圣经（★ 方法页）— 表格「著作|内容|地位」+ 公式框：光谱 → 分子结构
09  自由基猎手（★ 核心页）— 表格「问题|方法|结果」+ 公式框：自由基光谱定结构
10  1971 诺贝尔化学奖 — 表格「人物|贡献|理由」+ 公式框：获奖理由原文（独享）
11  荣誉与骑士 — Sanger 式「类别|代表|意义」表格（Tory/Ives/Gibbs/Faraday/Royal Medal/CC）
12  天文化学与身后之名 — 表格「形式|内容|意义」（星际分子 / 小行星 3316 / NSERC 金奖）
13  门生与传承 — 表格「人物|方向|结果」（Takeshi Oka；Carleton 校监 1973–80）
14  结尾 — 「每一根谱线，都是分子写给人类的自述。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1971 获奖口径 | **独享**；理由 "for his contributions to the knowledge of electronic structure and geometry of molecules, particularly free radicals"（page.md 实载英文原句）；勿把"世界第一分子光谱学家"写成获奖理由本身（那是颁奖词评语） |
| 身份口径 | 他是**物理学家/物理化学家**获化学奖——封面与身份页写 physical chemist，勿写"化学家" |
| 流亡细节 | 1935 年离开德国时每人仅带 **2.50 美元**等值现金——数字勿写错；导火索是 1933 年"犹太人配偶禁教令"、妻子 Luise 是犹太人 |
| Spinks 角色 | John Spinks 是**曾来访共事的物理化学家**，帮其获得萨斯喀彻温教职——colleague 关系，勿写成导师 |
| 博士后归属 | 1928–30 哥廷根/布里斯托尔随 Franck/Born/Lennard-Jones 是**博士后**——colleague 关系，勿写成师承 |
| Royal Medal 年份 | infobox 列 "(1971) (1972)" 两个年份——提示词与 tex 采 **1971**（与诺奖同年），并加注 infobox 存双值 |
| 国籍口径 | 生于德国、公民为加拿大（infobox Citizenship Canadian）；frontmatter "Nazi Germany" 为历史政权标签，不入库 |
| Luise 姓名 | 库内写作 Luise Herzberg（née Oettinger），1971 年去世；她是光谱学家与同行——spouse 关系 |
| 博士生名单 | infobox 仅载 **Takeshi Oka** 一人——其余不入库 |
| 引语红线 | page.md 正文无赫茨贝格直接引语（"foremost molecular spectroscopist" 是颁奖词转述）——全篇不得杜撰"赫茨贝格说过" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76602 | ✅ |
| name_zh | 格哈德·赫茨贝格 | ✅ |
| name_en | Gerhard Herzberg（★ 复用库内 id=2293，须用此精确形式回填 QID） | ✅ |
| birth_date | 1904-12-25 | ✅ |
| death_date | 1999-03-03 | ✅ |
| nationality | Canada（rank 0）+ Germany（rank 1，出生） | ✅ |
| primary_occupation | physical chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：molecular spectroscopy / atomic spectroscopy / physical chemistry / physics，带 rank） | ✅ |
| has_biography | 0（Beamer 立传完成后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 博士后东家 / 同事 / 门生 / 婚姻**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hans Rau | 师→生（博士导师） | 达姆施塔特 TU，1928 年 Dr.-Ing. |
| colleague | James Franck | 无向 | 1928–30 哥廷根博士后 |
| colleague | Max Born | 无向 | 1928–30 哥廷根博士后 |
| colleague | John Lennard-Jones | 无向 | 1928–30 布里斯托尔博士后 |
| colleague | John Spinks | 无向 | 萨斯喀彻温同事，助其 1935 年流亡后获得教职 |
| advisor-student | Takeshi Oka | Herzberg → 学生 | infobox doctoral students 唯一明载 |
| spouse | Luise Herzberg | 无向 | 1929 年结婚；光谱学家与同行研究者（née Oettinger）；1971 年去世 |

> metadata.json-only 的关系一律不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1971，独享）
- Henry Marshall Tory Medal（1953）；Centenary Prize（1958）
- Bakerian Medal and Lecture（1960）
- Frederic Ives Medal（OSA，1964；后获该会荣誉会员）
- Willard Gibbs Award（1969）；Faraday Lectureship Prize（1970）
- Royal Medal（1971）
- Linus Pauling Award（1971）；Chemical Institute of Canada Medal（1972）；Watts Lecture（1974）；Earle K. Plyler Prize（1985）
- Companion of the Order of Canada（1968）；Queen's Privy Council for Canada（1992）
- 会士：FRS（1951）、FRSC（1939）、美国 NAS（1968）、American Philosophical Society（1972）、American Academy of Arts and Sciences（1965）、International Academy of Quantum Molecular Science

## 9. 机构清单

- 教育：Gelehrtenschule des Johanneums（汉堡）、Technische Universität Darmstadt（Dr.-Ing. 1928）、哥廷根大学/布里斯托尔大学（博士后 1928–30）
- 任职：TU Darmstadt 私讲师（1930–）→ 萨斯喀彻温大学（1935 客座教授，1936–45 物理教授）→ 芝加哥大学叶凯士天文台光谱学教授（1945–48）→ 加拿大国家研究委员会 NRC（1948 纯粹物理部主任；1969 Distinguished Research Scientist）→ Carleton University 校监（1973–1980）
- 命名机构：Herzberg Institute of Astrophysics；Carleton Herzberg Laboratories；John Abbott College 主楼；NSERC Gerhard Herzberg Canada Gold Medal（2000 设立）；小行星 3316 Herzberg

## 10. 终审清单

- [x] 生卒 1904-12-25 / 1999-03-03，享年 94，出生地汉堡、去世地渥太华
- [x] 1971 独享；获奖理由英文原句准确；"第一光谱学家"为颁奖词评语非获奖理由
- [x] 流亡叙事：1933 禁教令 → 1935 出走、每人 2.50 美元——数字准确
- [x] 博士后关系（Franck/Born/Lennard-Jones）用 colleague、不用师承
- [x] 双国籍 rank：Canada 0 / Germany 1；"Nazi Germany" 不入库
- [x] 博士生仅 Takeshi Oka；正文无直接引语、全篇不杜撰
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Gerhard_Herzberg/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 images.txt / Commons 下载（infobox 为 1952 年照片）；404 用装饰圆占位并记录
- [ ] **国籍**：封面顶部明示加拿大（德裔作小注）
- [ ] **引语核对**：全篇不得出现无法在 page.md 溯源的"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 骨架）对齐

---

> **名单状态**：本文件由 chem-batch-14 生成；`chemist/generate_20th_century_list.py` 由主控统一更新。
> **最重要的事：每写一页就 make，看到溢出就修。**
