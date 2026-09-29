# 和平奖得主立传提示词（OpenPeace · Frank B. Kellogg）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Frank Billings Kellogg（1929 诺贝尔和平奖，《非战公约》共同起草人）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。
> 标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库下的 peace 侧）。
- **本实例**：Frank Billings Kellogg（弗兰克·比林斯·凯洛格），1929 诺贝尔和平奖得主（独享），美国第 45 任国务卿。
- **设计哲学**：和平奖得主多为政治家、活动家与法学家，立传重点不在「研究领域」而在**事业脉络**——从自学成才的律师到反垄断检察官、参议员、国务卿与国际法官的多段仕途，以及《凯洛格—白里安公约》这一高光时刻。模板骨架沿用「身份信息页 + 领域结构化表达」，领域表换为「事业领域表」。

---

## 二、背景信息 【人物专属】

- **目标人物**：Frank Billings Kellogg（1856-12-22 ~ 1937-12-21，享年 80 岁）
- **气质关键词**：**反垄断的铁面检察官、自学成才的外交家、《非战公约》的缔造者** —— 1929 诺贝尔和平奖获奖理由：
  > "for his crucial role in bringing about the Kellogg-Briand Pact."（表彰他在促成《凯洛格—白里安公约》（《非战公约》）中的关键作用）
- **设计母题**：**条约与天平（the pact and the scales）**。Kellogg 一生横跨法庭与外交场：从 Standard Oil 案的公诉席到巴黎的签约桌；视觉母题可用「天平与签字笔」「条约卷轴上的签名」，呼应「以法律废止战争作为国家政策工具」的核心遗产。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Frank_B._Kellogg/page.md`（Wikipedia 全文 + frontmatter，已抓取）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1856-12-22 生于纽约州波茨坦 ~ 1937-12-21 逝于明尼苏达州圣保罗（中风后肺炎，卒于 81 岁生日前夜），享年 80 岁；葬于华盛顿国家大教堂 St. Joseph of Arimathea 小堂。
- 国籍：美国；1865 年随家迁明尼苏达，农家清贫出身。
- 教育：**无正规学历**——乡村单间学校 14 岁辍学，未上过中学/大学/法学院，唯一进阶训练是在私人律师事务所做书记员（read law，1877 年起在罗切斯特执业）；对学历短缺终生自觉。
- 家庭：父 Asa Farnsworth Kellogg，母 Abigail（née Billings）；1886 年娶 Clara May Cook（1861–1942，George Clinton Cook 之女）；1880 年加入罗切斯特共济会第 21 会所。
- 任职轨迹（全部 page.md 明载）：
  1. Rochester 市检察官 1878–1881；Olmsted 县检察官 1882–1887；1886 迁圣保罗开业；
  2. 1905 受老罗斯福之请起诉联邦反垄断案；1906 任州际商务委员会特别法律顾问（E. H. Harriman 调查）；1908 主导 Union Pacific 铁路起诉；
  3. 1911 Standard Oil Co. of New Jersey v. United States（221 U.S. 1）——其最重要案件；
  4. 美国律师协会（ABA）主席 1912–1913；
  5. 共和党参议员（明尼苏达）1917-03-04 ~ 1923-03-03（第 65–67 届国会）；凡尔赛条约批准战中少数支持批准的共和党人；1922 竞选连任失利；1923 出席圣地亚哥第五届美洲国家会议；
  6. 驻英大使 1924-01-14 ~ 1925-02-10（Coolidge 任命）；
  7. 第 45 任美国国务卿 1925-03-05 ~ 1929-03-28（Coolidge/Hoover 内阁）；
  8. 常设国际法院（PCIJ）副院长级同席法官 1930-09-25 ~ 1935-09-09。
- 关键荣誉：1929 诺贝尔和平奖（独享）；法国荣誉军团勋章（1929）；1928 都柏林自由奖；1931 美国哲学学会会员；1976 圣保罗故居列为国家历史地标。
- 核心事业清单：
  1. 反垄断公诉（Standard Oil 案为代表）；
  2. 《凯洛格—白里安公约》（1928）——与法国外长 Briand 共同缔造，「放弃战争作为国家政策工具」，后成为 1945 年后审判德日战犯的法律基础；
  3. 国务卿任内修复美墨关系、斡旋秘鲁—智利 Tacna-Arica 争端；
  4. 远东政策：采纳 Nelson Trusler Johnson 建议、同情中国、促成对华关税改革、废除不平等条约体系一角；
  5. 推动扩展华盛顿海军条约的军备限制（进展有限）；
  6. 1937 捐设 Carleton College「Kellogg 国际关系教育基金」并任校董。
- 关键时间线（15–20 节点）：1856 生于 Potsdam → 1865 迁明尼苏达 → 1877 律师执业 → 1878 市检察官 → 1886 婚 + 迁圣保罗 → 1905 联邦反垄断案 → 1906 ICC 特别顾问 → 1908 Union Pacific 案 → 1911 Standard Oil 案 → 1912–13 ABA 主席 → 1917 参议员 → 1919 支持凡尔赛批准 → 1924 驻英大使 → 1925–29 国务卿 → 1928 《非战公约》签署 + 都柏林自由奖 → 1929 诺奖 + 荣誉军团 → 1930–35 PCIJ 法官 → 1931 美国哲学学会 → 1937 Carleton 基金 + 12-21 逝世。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international law | 国际法 | 《非战公约》、PCIJ 法官 | 公约页 |
| 1 | diplomacy | 外交 | 国务卿、驻英大使 | 国务卿页 |
| 2 | antitrust law | 反垄断法 | Standard Oil 案等联邦公诉 | 早年页 |
| 3 | naval arms limitation | 海军军备限制 | 扩展华盛顿条约限制的尝试 | 国务卿页 |
| 4 | international adjudication | 国际裁判 | 常设国际法院同席法官 1930–35 | 晚年页 |

- 入库：`person_field` 5 条（rank 0–4），与下方 yaml `fields` 完全一致。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 一致】

> 只收 page.md 明载关系；metadata-only 一律不入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Clara Cook Kellogg | 无向 | 1886 年成婚，相伴至终 |
| colleague | Aristide Briand | 无向 | 《凯洛格—白里安公约》共同缔造者（Briand 系 1926 和平奖得主） |

- 说明：Coolidge/Hoover/Roosevelt 等为任命与政务关系，不属私人关系，不入库；Briand 库内已有记录（id=5602，name_en='Aristide Briand'，另一批次所建），按名匹配幂等。
- 入库：`person_relation` 2 条。

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#4E342E`（条约深褐——法律文书与北方农家的厚重，manifest 预分配，勿改）
- **辅色**：诺奖香槟金 `#C9A227`
- badgeA–D 四分类色（事业领域）：
  - `badgeA` 国际法/非战公约 — 条约金 `#B08D3E`
  - `badgeB` 反垄断公诉 — 法槌褐红 `#8C3B2E`
  - `badgeC` 外交仕途 — 麻省蓝 `#3E5F7E`
  - `badgeD` 国际裁判 — 石板灰绿 `#4E6E5D`
- **背景母题**：条约卷轴横幅与细线签名纹理，呼应「条约与天平」。

### 第 6 步：规划幻灯片序列 【人物专属，共 16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 非战公约的缔造者 / Frank B. Kellogg 1856–1937 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 生卒、国籍、教育（无正规学历）、配偶、荣誉、任职轨迹
03  核心事业概览 — 反垄断公诉 / 参议员 / 国务卿 / 非战公约 / 国际法官
04  早年：农场少年与自学律师 (1856–1881) — 14 岁辍学、read law、罗切斯特执业
05  检察官岁月 (1882–1905) — 市检察官、县检察官、迁圣保罗
06  联邦反垄断公诉 (1905–1911) — TR 之请、Harriman、Union Pacific
07  Standard Oil 案 (1911) — 221 U.S. 1，生涯最重要一役
08  ABA 主席与参议员 (1912–1923) — 凡尔赛批准战中少数支持者
09  驻英大使 (1924–1925) — Coolidge 任命
10  国务卿 (1925–1929) — 美墨关系、Tacna-Arica、远东关税改革
11  《凯洛格—白里安公约》(1928) — Briand 提议、「放弃战争作为国家政策工具」（核心页）
12  1929 诺贝尔和平奖 — 官方理由（独享）
13  国际法官与晚年 (1930–1937) — PCIJ、Carleton 基金、1937 逝世
14  遗产：从公约到纽伦堡 — 公约成为战后审判战犯的法律基础
15  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式：每页 `\newcommand{\xxxslide}` 定义；`make` 后 `pdftoppm` 截图查溢出；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距。
- **Kellogg 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 无学历红线 | page.md 明载从未上过中学/大学/法学院，仅律所书记训练；勿杜撰任何学位 |
| 卒日口径 | 1937-12-21（81 岁生日前夜，享年 80），勿写成 81 岁 |
| 公约署名 | 公约以两人命名：Briand 提议在前（其人 1926 已获和平奖），Kellogg 促成在后；勿写成 Kellogg 单独发起 |
| 诺奖独享 | 1929 为 Kellogg 独享（理由用 "his"），勿与 Briand 分享；Briand 1926 已获奖，勿混淆 |
| 案件细节 | Standard Oil 案全名 *Standard Oil Co. of New Jersey v. United States*, 221 U.S. 1 (1911)，勿漏年份 |
| 参议院任期 | 1917-03-04 ~ 1923-03-03，1922 连任失败后卸任，勿写「1923 落选」 |
| PCIJ 职务 | "associate judge"（同席法官），infobox 载 1930-09-25 就任，勿简写「1930–1935 任职」就丢精确日期 |
| 远东表述 | 对华政策只按 page.md 客观记录（关税改革、支持中国避免日本威胁、废不等条约），不加评价 |
| 引语红线 | 公约核心句 "the renunciation of war as an instrument of national policy" 为 page.md 原文可引；其余禁编引语 |
| 无载禁写 | 子女（page.md 未载）、与 Coolidge/Hoover 私交细节等不写 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Kellogg-Briand Pact | 《凯洛格—白里安公约》 | 亦称《非战公约》《巴黎公约》 |
| renunciation of war | 放弃战争 | 公约核心条款表述 |
| antitrust | 反垄断 | 谢尔曼法公诉背景 |
| read law | 研读法律（学徒式） | 非法学院学历 |
| associate judge | 同席法官 | PCIJ 职务，勿译「副庭长」 |
| Permanent Court of International Justice | 常设国际法院 | 国际法院前身 |
| Tacna-Arica controversy | 塔克纳—阿里卡争端 | 秘鲁/智利之间 |
| Legion of Honour | 法国荣誉军团勋章 | 1929 授予 |
| World War Foreign Debts Commission | 一战外债委员会 | 其成员职务 |
| National Historic Landmark | 国家历史地标 | 1976 故居认定 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 时间感 / 纪录片 / 沉稳
- **匹配理由**：Kellogg 的一生横跨美国从镀金年代到两次大战之间的完整弧线——从农家辍学少年到《非战公约》的签字人；"The Flow of Time" 的时间纵深感匹配其八十年仕途的绵长与公约遗产的悠远。
- **本地路径**：`music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav` → 复制到 `peace/presentations/20th_century/Frank_B._Kellogg/The_Flow_of_Time.wav`
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Frank_B._Kellogg/page.md` | 本地 Wikipedia 正文 + frontmatter（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（一~五节） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
> **红线：无载禁写；引语仅限 page.md 原文；政治内容只作客观记录。**
