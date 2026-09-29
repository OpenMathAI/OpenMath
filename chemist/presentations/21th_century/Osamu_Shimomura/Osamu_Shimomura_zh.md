# Osamu Shimomura（下村脩）立传提示词

> qid=Q205345 · 1928-08-27 生于福知山（京都府） – 2018-10-19 逝于长崎 · 日本有机化学家、海洋生物学家 · 21 世纪 · 诺贝尔化学奖（2008，与 Chalfie / Tsien 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Osamu_Shimomura/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页，是本篇的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像用 `images/` 目录本地文件，若缺省用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{water}\enspace 从深海荧光到生命之光\enspace·\enspace 日本`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（下村 脩）、国籍、出生地/去世地、教育、博士导师、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「海洋浮游生物的发光点」母题——散落的青绿光点暗示 *Aequorea victoria* 水母的荧光。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（对象 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如海萤荧光素结构、aequorin 发光反应、GFP 色基形成。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Osamu Shimomura（下村 脩；中文惯称：下村脩）
- **生卒**：1928-08-27 生于京都府福知山市（时为 Empire of Japan）→ 2018-10-19 逝于长崎（癌症），享年 90
- **国籍**：Japan（日本）
- **身份**：有机化学家、海洋生物学家；Woods Hole 海洋生物学实验室（MBL）与波士顿大学医学院荣休教授
- **家庭**：幼年因父任职帝国陆军军官随家移居满洲（Manchukuo）与大阪，后定居长崎谏早；妻 Akemi 于长崎大学相识，同为有机化学家、研究伙伴；子 Tsutomu Shimomura 为计算机安全专家（参与抓捕 Kevin Mitnick）；女 Sachi Shimomura 为弗吉尼亚联邦大学英语系本科教学主任
- **教育轨迹**：
  - 长崎医科大学药学部（今长崎大学药学部）——校园毁于 1945 年原子弹，药学部临时校区恰在其家附近
  - 1951 获药学 BS；留校任 lab assistant 至 1955
  - 1956 赴名古屋大学任 Yoshimasa Hirata 助手；1958 获有机化学 MS
  - 1960 于名古屋大学获有机化学 PhD（论文《海ホタルルシフェリンの構造》海萤荧光素的结构，1960）
- **导师**：Yoshimasa Hirata（名古屋大学，博士导师）
- **研究领域**：有机化学、生物化学、海洋生物学、生物发光（bioluminescence）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **战火中的少年（1928–1945）**：生于福知山，随父驻防长于满洲与大阪；1945 年 8 月，16 岁的他在距长崎原爆爆心 25 公里的谏早——先听见 Bockscar 轰炸机掠过，闪光致其失明约 30 秒，随后被"黑雨"淋透（page.md 明载三点，客观带过）。
2. **废墟旁的入学（1945–1951）**：长崎医大药学部校园全毁，临时校区恰在他家附近——这段"偶然的邻近"开启了他的求学之路；1951 获药学学士。
3. **海萤之谜（1956–1960）**：名古屋大学 Hirata 实验室；导师交给他"湿水即发光的甲壳类海萤（*Vargula hilgendorfii*，umi-hotaru）发光物质"这一难题。
4. **结晶荧光素（1960）**：成功鉴定发光蛋白，以 "Crystalline Cypridina luciferin" 发表于《日本化学会志》——普林斯顿的 Frank Johnson 因此文向他伸出橄榄枝。
5. **远渡普林斯顿（1960）**：加入 Johnson 实验室（生物学系），转向生物发光研究。
6. ** collecting 水母的夏天**：多年夏天赴华盛顿大学 Friday Harbor Laboratories 采集多管水母 *Aequorea victoria*。
7. **1962：aequorin 与 GFP 同年发现**：从约一万只水母中纯化出发光蛋白 aequorin 与绿色荧光蛋白 GFP——2008 年他因此获诺贝尔化学奖的三分之一奖金（page.md 原文 "a third of the Nobel Prize"）。
8. **Woods Hole 岁月**：MBL 与波士顿大学医学院荣休教授，把毕生献给生物发光化学。
9. **2008 诺贝尔化学奖（三人共享）**：与哥伦比亚大学 Martin Chalfie、加州大学圣地亚哥分校 Roger Y. Tsien 共享，表彰 "the discovery and development of the green fluorescent protein, GFP"（GFP 的发现与发展）；GFP 的**发现**归于他。
10. **荣誉接踵（2004–2013）**：Pearse Prize（2004）、Emile Chamot Award（2005）、朝日奖（2006）、文化勋章与文化功劳者（2008）、Golden Goose Award（2012）、美国国家科学院外籍院士（2013）。
11. **身后哀荣**：2018 年 10 月 19 日因癌症逝于长崎；日本政府追授从三位（Junior third rank, posthumous）。
12. **著述**：《Bioluminescence: Chemical Principles And Methods》（2012）；日文回忆录《クラゲに学ぶ：ノーベル賞への道》（2010）。
13. **科学家的家族**：妻 Akemi 是研究伙伴；子 Tsutomu 是抓捕 Kevin Mitnick 的计算机安全专家；女 Sachi 是文学学者——一门三途，皆成风景（克制叙述，page.md 明载）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海翠绿 deepbiolum） | `#1E6B52` | 海萤与水母的生物发光绿——黑暗深海中的生命之光（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（海萤荧光素 badgeLuciferin） | `#8A5A2C` | 琥珀 Cypridina luciferin 结晶 |
| 分类色 2（aequorin badgeAequorin） | `#2C5F8A` | 蓝发光蛋白 aequorin |
| 分类色 3（GFP badgeGFP） | `#1B7A43` | 绿绿色荧光蛋白 |
| 分类色 4（海洋采集 badgeOcean） | `#175873` | 深蓝 Friday Harbor 采集之夏 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「深海中漂浮的发光浮游生物」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Through the Darkness** — Audiomachine（文件 `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`；不要复制 wav 文件，Makefile 直接引用）
- **风格**：史诗 / 穿越黑暗 / 希望渐明
- **匹配理由**：
  - "穿越黑暗" 直接呼应其人生弧线——原爆阴影下的废墟少年，走到发现生命之光的诺贝尔奖台
  - "史诗" 匹配从海萤到水母、从长崎到普林斯顿再到 Woods Hole 的六十年长跑
  - 曲名中的黑暗与光的意象，恰是生物发光研究本身的隐喻

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 从深海荧光到生命之光 / Osamu Shimomura 1928–2018 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/领域/机构/荣誉）
03  下村脩的一生 — Sanger 式时间线（10 节点：1928→1945→1951→1956→1960→1962→2006→2008→2013→2018）
04  战火中的少年 (1928–1951) — 表格「时间|事件|结果」
05  名古屋与海萤之谜 (1956–1960) — 表格「对象|方法|结果」+ 公式框：海萤荧光素结晶
06  普林斯顿与采集之夏 (1960–1962) — 表格「对象|方法|结果」
07  aequorin 与 GFP (1962) — 表格「挑战|方法|结果」+ 公式框：aequorin 发光反应
08  2008 诺贝尔化学奖 — 公式框：获奖理由原句 + 三人分工（发现 / 表达 / 发展）
09  Woods Hole 与生物发光化学 — 表格「对象|方法|结果」
10  荣誉长廊 — Sanger 式「类别|代表|意义」表格（文化勋章 / 朝日奖 / NAS 院士等 itemize）
11  一门三途 — 表格「家人|领域|成就」（Akemi / Tsutomu / Sachi）
12  著述与传承 — 高斯式流程图（回忆录 → 专著 → Golden Goose Award）
13  遗产：GFP 照亮生命科学 — 四分类遗产盒 + 公式框：GFP 色基形成需氧不自援
14  结尾 — 「黑暗越深，微光越亮。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2008 获奖 | **三人共享**（Shimomura / Chalfie / Tsien）；下村获奖金的 **三分之一**（page.md 原文 "a third of the Nobel Prize in Chemistry in 2008"）——勿写独得或对半 |
| 获奖理由 | 官方口径 "for the discovery and development of the green fluorescent protein, GFP"（GFP 的发现与发展）；下村的分工是 **发现**（1962 aequorin + GFP），Chalfie 是表达应用、Tsien 是改造发展——三者勿混 |
| 1962 年份 | aequorin 与 GFP 均为 **1962 年**与 Frank Johnson 合作发现——勿写 1961 或他独自发现 |
| 原爆经历 | 仅写 page.md 实载三点：闻 Bockscar 声、闪光致盲约 30 秒、被黑雨淋透；距爆心 25 公里（谏早 Isahaya）；其余细节页面无载禁写；叙述客观克制 |
| 出生地 | 京都府 **福知山市**（Fukuchiyama）；幼年移居满洲/大阪、后定居谏早——出生地与成长地勿混 |
| 学位年份 | BS 1951（长崎）、MS 1958、PhD 1960（均名古屋）——勿错配 |
| 博士导师 | **Yoshimasa Hirata**（名古屋大学）；Frank Johnson 是普林斯顿合作者/招募者，**非博士导师**——二人身份勿混 |
| 国籍噪声 | frontmatter 含 "Empire of Japan"，系出生时政权口径—— nationality 入库仅 Japan，勿入 Empire of Japan |
| 妻名 | 页面仅载名 **Akemi**（长崎大学相识、有机化学家、研究伙伴）——姓氏扩写须克制，引语红线适用 |
| 去世 | 2018-10-19 逝于长崎，**癌症**（cancer），享年 90——勿写其他死因 |
| 引语 | page.md 正文**无任何直接引语**——全篇禁用引号原话，一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q205345 | ✅ |
| name_zh | 下村脩 | ✅ |
| name_en | Osamu Shimomura | ✅ |
| birth_date | 1928-08-27 | ✅ |
| death_date | 2018-10-19 | ✅ |
| nationality | Japan | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分见下表） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | field_en | field_zh |
|---|---|---|
| 0 | organic chemistry | 有机化学 |
| 1 | biochemistry | 生物化学 |
| 2 | marine biology | 海洋生物学 |
| 3 | bioluminescence | 生物发光 |

## 7. 社会关系入库清单

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Yoshimasa Hirata | 师→生（博士导师） | 1956 入名古屋大学 Hirata 实验室，1960 获有机化学博士 |
| colleague | Frank Johnson | 无向 | 普林斯顿生物学系合作者，1960 招募其赴美；1962 共同发现 aequorin 与 GFP |
| co-honored | Martin Chalfie | 无向 | 2008 诺贝尔化学奖共同得主（GFP 表达应用） |
| co-honored | Roger Y. Tsien | 无向 | 2008 诺贝尔化学奖共同得主（GFP 改造发展） |
| spouse | Akemi Shimomura | 无向 | 妻子，长崎大学相识；同为有机化学家、研究伙伴（page.md 仅载名 Akemi） |
| parent-child | Tsutomu Shimomura | 下村脩 → 子 | 计算机安全专家，参与抓捕 Kevin Mitnick |
| parent-child | Sachi Shimomura | 下村脩 → 女 | 弗吉尼亚联邦大学英语系本科教学主任 |

> metadata.json 无博士生字段；三人 GFP 组内 Chalfie/Tsien 互指由各篇 yaml 双向对齐（规范全名）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2008，与 Chalfie / Tsien 三人共享）
- Pearse Prize, Royal Microscopical Society（2004）
- Emile Chamot Award（2005）
- Asahi Prize 朝日奖（2006）
- Order of Culture 文化勋章（2008）；Person of Cultural Merit 文化功劳者（2008）
- Golden Goose Award（2012）
- United States National Academy of Sciences 院士（2013）
- Junior third rank 从三位（2018，追授）

## 9. 机构清单

- 教育：Nagasaki Medical College 药学部（今 Nagasaki University；BS 1951）、Nagoya University（MS 1958、PhD 1960）
- 任职：长崎医大 lab assistant（1951–1955）→ 名古屋大学 Hirata 实验室助手（1956–）→ Princeton University 生物学系（1960–，Johnson 实验室）→ Marine Biological Laboratory（Woods Hole）与 Boston University School of Medicine 荣休教授
- 采集地：University of Washington Friday Harbor Laboratories（历年夏天采集 *Aequorea victoria*）

## 10. 终审清单

- [x] 生卒 1928-08-27 / 2018-10-19，享年 90，出生地福知山、去世地长崎
- [x] 2008 三人共享、下村获三分之一；获奖理由原句忠实；发现（1962）/表达/发展三人分工准确
- [x] 博士导师 Hirata；Johnson 为普林斯顿合作者（非导师）表述准确
- [x] 原爆经历仅写 page.md 实载三点，客观克制
- [x] 引语红线：全篇无引号原话（page.md 无直接引语）
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Osamu_Shimomura/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 目录照片就位（缺省装饰圆占位）
- [ ] 国籍：封面顶部明示日本
- [ ] 引语核对：确认全篇无杜撰引号原话（获奖理由英文原句除外，须与页面一致）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金参照）对齐
