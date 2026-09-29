# 物理学家立传提示词（Isamu Akasaki · 2014 诺贝尔物理学奖）

> **本文件是 OpenPhysicist 21 世纪批次的人物专属立传提示词**，以 Isamu Akasaki（2014 诺贝尔物理学奖，蓝光 LED）为目标人物。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Isamu Akasaki（赤崎勇），2014 诺贝尔物理学奖（与 Hiroshi Amano、Shuji Nakamura 共享）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；本篇另需突出**三十年的材料长征**——从 1960 年代末起步到 1989 年首支 GaN p–n 结蓝光 LED，一条"低温柔性缓冲层"点亮的工程史诗。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Isamu Akasaki（1929-01-30 生于鹿儿岛知览 ~ 2021-04-01 逝于名古屋，享年 92 岁）
- **气质关键词**：**蓝光 LED 的点灯人、氮化镓的垦荒者、低温缓冲层的发明者** —— 2014 诺贝尔物理学奖获奖理由：
  > "for the invention of efficient blue light-emitting diodes which has enabled bright and energy-saving white light sources"（因其发明高效蓝光发光二极管，实现了明亮且节能的白色光源）
- **设计母题**：**蓝宝石上的蓝光（blue light on sapphire）**。在蓝宝石衬底上长出高质量 GaN 晶体并发出蓝光——"三十年不发光的材料终于点灯"，是比泛泛「LED」更贴合 Akasaki 的视觉语言。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Isamu_Akasaki/page.md`（✅ 已有本地）
- **html/images**：待下载 —— Wikipedia URL：`https://en.wikipedia.org/wiki/Isamu_Akasaki`（第 0 步下载 `Isamu_Akasaki.html` 与 infobox 肖像到 `images/`）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地（事实基准如下）；html 与 images/ 待下载（URL 见上）
- 事实基准（取自 page.md frontmatter + infobox + 正文）：
  - 生卒：1929-01-30 生于鹿儿岛县知览（Chiran），在鹿儿岛长大 ~ 2021-04-01 因肺炎逝于名古屋的医院，享年 92 岁
  - 国籍：日本
  - 家庭：兄 Masanori Akazaki（电子工程研究者，九州大学荣休教授；姓氏"赤﨑"亦读 Akazaki）；妻 Ryoko，居名古屋，无子女
  - 教育：鹿儿岛县立第二鹿儿岛中学（今县立鹿儿岛南高中）1946 → 第七高等学校造士馆（今鹿儿岛大学）1949 → 京都大学理学部 1952 → 名古屋大学 1964 D.Eng.（论文：Ge 的气相外延生长研究）
  - 任职机构：Kobe Kogyo Corporation（今富士通）研究员 1952– → 名古屋大学电子学系研究助理/助理教授/副教授 1959–1964 → 松下电器东京研究所（基础研究第四实验室主任→半导体部部长）→ 名古屋大学教授 1981 → 明治大学理工学部教授 1992 → 名古屋大学赤崎纪念研究馆（2006-10-20 开馆，以专利使用费建成）→ 氮化物半导体核心技术研究中心主任 2011；JST「GaN 基蓝光 LED 研发」项目负责人 1987–1990、「GaN 基短波长半导体激光器研发」1993–1999；北海道大学客座教授 1995–1996；JSPS Future 计划 1996–2001；明治大学「氮化物半导体高科技研究中心」负责人 1996–2004；METI 氮化物无线器件战略委员会委员长 2003–2006
  - 关键荣誉：IEEE Jack A. Morton Award 1998；Rank Prize for Optoelectronics 1998；C&C Prize 1998；Gordon E. Moore Medal 1999；Asahi Prize（表格作 2000，infobox 作 2001）；John Bardeen Award 2006；Kyoto Prize in Advanced Technology 2009；IEEE Edison Medal 2011；Order of Culture（文化勋章，明仁天皇）2011；Karl Ferdinand Braun Prize 2013；Nobel 2014（与 Amano、Nakamura 共享）；Charles Stark Draper Prize 2015（与 Craford、Dupuis、Holonyak、Nakamura）；Asia Game Changer Award 2015；Asian Scientist 100 2016；Queen Elizabeth Prize for Engineering 2021；IEEE Fellow 1999；美国国家工程院国际院士 2008；旭日小绶章、紫绶褒章、文化功劳者（frontmatter 有载，年份无）
  - 知名学生：Hiroshi Amano（infobox Doctoral students 明载）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点，见幻灯片序列）

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Akasaki 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | gallium nitride | 氮化镓（GaN） | 高质量晶体生长与 p/n 型控制 | 核心贡献页 |
| 1 | light-emitting diodes | 发光二极管（LED） | 1989 首支 GaN p–n 结蓝光/紫外 LED | 蓝光 LED 页 |
| 2 | semiconductor technology | 半导体技术 | 器件结构与异质结构 | 器件页 |
| 3 | epitaxial growth | 外延生长 | MOVPE 与低温缓冲层技术 | 材料页 |
| 4 | materials science | 材料科学 | infobox Fields 口径 | 总览页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hiroshi Amano | student（对方是学生） | 名古屋大学博士生，2014 诺贝尔物理学奖共同得主 |
| co-honored | Hiroshi Amano | 无向 | 2014 诺贝尔物理学奖共享（高效蓝光 LED 的发明） |
| co-honored | Shuji Nakamura | 无向 | 2014 诺贝尔物理学奖共享（高效蓝光 LED 的发明） |
| spouse | Ryoko Akasaki | 无向 | 妻子，居名古屋，无子女 |

#### 4.5.1 入库操作

- 以 `name_en='Isamu Akasaki'`（qid Q1673706，库内无记录，seed 新建）为中心写入 `person_relation`
- 对手方：`Hiroshi Amano`、`Shuji Nakamura` 库内暂无记录，seed 以规范全名建 stub（batch 8 随后以 QID Q11443689/Q730065 UPD 回填同一记录，勿另建别名）；Ryoko 建新 stub
- 方向约定：师生有向（student=对方是学生）；共同荣誉/夫妻无向

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：蓝色之光、三十年坚持的工程韧性
- **配色**：亮蓝（蓝光 LED 本色）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeGaN` 氮化镓 — 深青绿 `#1B6B5A`
  - `badgeLED` 蓝光 LED — 亮蓝 `#2E86C1`
  - `badgeMovpe` 外延生长 — 琥珀 `#E07B30`
  - `badgePnj` p–n 结 — 玫瑰 `#C4204F`
- **主色**：`#1E4E79`（亮蓝，批内唯一）
- **背景母题**：柔和气泡——蓝宝石衬底上的晶圆光泽渐变，中心一点蓝光呼应「点灯时刻」

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页（封面之后、核心贡献之前）：左头像 + 右信息网格（生卒、出生地、国籍、教育、任职、主要荣誉、核心领域；博士导师 page.md 无载，勿填）。
4. 品牌口径统一：结尾页底部品牌写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 蓝光 LED 的点灯人 / Isamu Akasaki 1929–2021 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地知览、京都大学/名古屋大学、Kobe Kogyo→松下→名大→明治大学、Nobel 2014、核心领域）
03  核心贡献概览 — GaN 晶体 / 低温缓冲层 / p–n 结蓝光 LED / 量子阱激光
04  鹿儿岛少年 (1929–1952) — 知览出生、第七高中、京都大学理学部
05  从企业到讲坛 (1952–1964) — Kobe Kogyo、名古屋大学、Ge 气相外延博士论文、松下研究所
06  选定 GaN： MOVPE 路线 (1960s 末–1981) — 松下时期的坚持
07  1981 重返名大：从头再来 — 1985 低温柔性缓冲层突破（核心贡献页）
08  1989：点灯 — p 型 GaN（Mg 掺杂+电子辐照激活）与首支 GaN p–n 结蓝光/紫外 LED
09  1990–2000：从 LED 到激光 — n 型控制、室温受激辐射、388 nm 量子阱器件、QCSE
10  荣誉与认可 — Nobel 2014 · Kyoto Prize 2009 · Edison Medal 2011 · 文化勋章 2011 · QEPrize 2021
11  赤崎纪念研究馆与传承 — 专利使用费建馆、学生 Amano、明治大学中心
12  遗产：照亮世界的白光
13  结尾
```

- 公式框：page.md 无公式，用**概念图式**——「蓝宝石衬底 / LT 缓冲层 / GaN 层 / p–n 结的分层结构示意」，并注明"示意图，非 page.md 公式"。

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

- 版式：每页写完 `make clean && make`，pdftoppm 截图查溢出；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标。

**Akasaki 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖归属 | 2014 诺奖**三人共享**（Akasaki、Amano、Nakamura），且正文点名 Amano 是其博士生；勿写独得，也勿写成"师生三人组"（Nakamura 与他无师生关系） |
| Nakamura 身份 | Nakamura 是日亚化学的独立突破者，page.md 未载与 Akasaki 的任何个人关系，**只建 co-honored，勿建 colleague/advisor-student** |
| Amano 双关系 | 对 Amano 同时是 advisor-student（博士生）与 co-honored（2014 诺奖），两条都要建，类型勿混 |
| 发光年份 | 1989 首支 GaN p–n 结蓝光/紫外 LED（co-inventing，与团队共同）；1990 室温受激辐射；勿把 1985 缓冲层写成"发明 LED 之年" |
| 学历口径 | 本科京都大学 1952、**博士学位是名古屋大学 1964（在职取得）**，勿写"京都大学博士"；Kobe Kogyo（今富士通）是企业非高校 |
| Asahi Prize 年份 | 奖项表格作 2000、infobox 作 2001，页面两说并存——以表格为准并加注 |
| 兄长姓名 | 兄 Masanori 姓氏拼作 **Akazaki**（"赤﨑"的另一读法），且是电子工程学者（九州大学荣休），非诺奖物理学家；兄弟姐妹关系不在类型白名单，不入库 |
| Draper Prize | 2015 与 Craford、Dupuis、Holonyak、Nakamura 五人共享（注 3），勿写成独得 |
| QEPrize | 2021 年获 Queen Elizabeth Prize for Engineering，本人于当年 4 月去世——**身后获颁**，措辞注意 |
| 去世原因 | 2021-04-01 名古屋的医院，肺炎，享年 92；勿写"猝逝"等 page.md 未载细节 |
| 家庭 | 妻 Ryoko，无子女——个人生活仅此一点，勿扩展 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| gallium nitride (GaN) | 氮化镓 | 蓝 LED 的核心材料，勿译"氮化镓镓" |
| blue LED | 蓝光发光二极管 | 诺奖理由核心词 |
| p–n junction | p–n 结 | 1989 首次实现于 GaN |
| MOVPE | 金属有机气相外延 | 选定的生长方法 |
| low-temperature buffer layer | 低温柔性缓冲层 | 1985 关键突破，勿译"低温缓冲层技术"以外的编造名 |
| sapphire substrate | 蓝宝石衬底 | GaN 生长的衬底 |
| p-type / n-type | p 型 / n 型 | Mg 掺杂得 p 型、Si 掺杂得 n 型 |
| electron irradiation | 电子辐照 | p 型激活手段 |
| hetero structure | 异质结构 | 高效器件设计 |
| quantum confined Stark effect | 量子限制斯塔克效应（QCSE） | 1997 氮化物体系中验证 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Through the Darkness** — Audiomachine（史诗 / 黑暗 / 推进）
- **匹配理由**:
  - "攻克难题、突破前夕" 正是 Akasaki 三十年 GaN 长征的写照——全世界都认为 GaN 无法点亮，他在黑暗中把晶体质量一步步做上去
  - "史诗/推进" 匹配 1989 点灯到 2014 诺奖的终章弧线（与批内其他曲目不重复）
- **备选**（未采用）: Ascension（上升感合但更偏太空意象）、Expedition（探索感偏地理叙事）
- **本地路径**: `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Isamu_Akasaki/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
