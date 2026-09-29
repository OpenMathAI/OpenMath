# 文学家立传提示词（OpenLiterature：Henrik Pontoppidan）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Henrik Pontoppidan（亨利克·蓬托皮丹），1917 年诺贝尔文学奖得主（与同胞 Karl Gjellerup 共享）。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对蓬托皮丹，即「丹麦全景画幅」：以巴尔扎克—左拉式的社会全景小说呈现其国家与时代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Henrik Pontoppidan（1857–1943），丹麦现实主义作家，「现代突破」（Modern Break-Through）中最年轻、最具原创性与影响力的一员，1917 年与 Karl Gjellerup 共享诺贝尔文学奖。
- **设计哲学**：以「丹麦全景」为核心叙事——一个既背离保守牧师世家、又与其社会主义同代人保持距离的孤独观察者，用社会批判的笔为他的国家与时代留下了异常完整的画卷。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Henrik Pontoppidan（亨利克·蓬托皮丹，1857-07-24 ~ 1943-08-21，享年 86 岁）
- **官方获奖理由（Nobel 1917，禁止改写）**：
  > "for his authentic descriptions of present-day life in Denmark"
  > （表彰其对当代丹麦生活的真实描写）
- **气质关键词**：**丹麦全景的画师、社会批判的开拓者、悖论缠身的观察者**
- **设计母题**：**丹麦全景画（the broad canvas）**。其三大社会小说「在巴尔扎克与左拉的传统中确立了丹麦版的社会广角描写」——以横幅全景画卷、乡村—都市双景、宪法斗争年代的历史底色构成视觉母题。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Henrik_Pontoppidan/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Henrik_Pontoppidan
- **肖像**：第 0 步优先用 page.md 内嵌图 `Henrik_Pontoppidan.jpg`（c. 1874）或 Michael Ancher 1908 所绘肖像；404 则用装饰圆占位。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1857-07-24 生于 Fredericia（丹麦）～ 1943-08-21 卒于 Charlottenlund（丹麦），享年 86 岁。
- **家庭出身**：日德兰牧师之子，属古老的牧师与作家世家；曾讽刺自己姓氏 Pontoppidan 由丹麦语本源 *Broby* 被拉丁化的历史（page.md 称「著名引语」但**未给原文**，禁杜撰引文）。
- **经历**：放弃工程师学业 → 小学教师 → 自由记者 → 1881 年出道成为全职作家。
- **第一阶段（叛逆的社会批判）**：以平实的短篇无情描写与他朝夕相处的农民与乡村无产者——或许是第一位打破丹麦农民理想化描写的进步作家；结集为 *Landsbybilleder*（《乡村图景》1883）、*Fra Hytterne*（《来自棚屋》1887）；1890 政治短篇集 *Skyer*（《云》）狠批保守党半独裁统治下的丹麦，既谴责压迫者也讥讽丹麦人的逆来顺受。此后转向心理与自然主义问题，但不放弃社会关怀。
- **亵渎风波**：1889 评论《Messias》与 1890《Den gamle Adam》匿名发表，被斥为亵渎引发论战；出版人/报纸编辑 **Ernst Brandes** 因《Messias》于 1891 年 12 月被罚 300 克朗，1892 年自杀。
- **家庭**：第一任妻子 Mette Marie Hansen（北西兰农户之女），三子一女夭折；1889 年结识 Antoinette Caroline Elise Kofoed 后分居，1892 年娶 Kofoed，育一女一子；Kofoed 体弱，1928 年去世；他须同时供养两个家庭，困难重重；两个儿子分别移居美国与巴西。
- **三大社会小说（约 1890–1920）**——丹麦版「社会广角描写」小说，承巴尔扎克与左拉传统：
  1. *Det forjættede Land*（I–III，1891–95；英译 The Promised Land）——幻想家乡村布道梦的自我欺骗与疯狂；
  2. *Lykke-Per*（《幸运的彼尔》，1898–1904，半自传，最著名）——天才青年弃宗教家庭去做工程师与征服者，功成之际被出身追上，弃业归隐孤独；
  3. *De dødes Rige*（《死者之国》，1912–16）——1901 民主表面胜利后的丹麦：政治理想腐朽、资本主义挺进、报刊与艺术堕落。
- **其他作品**：*Mimoser*（1886）、*Isbjørnen*（1887，格陵兰直率牧师 vs 狭隘丹麦教士）、*Nattevagt*（1894，取材画家挚友 L. A. Ring，Ring 视为背叛信任而绝交）、*Den gamle Adam*（1894）、*Ørneflugt*（1899，对安徒生《丑小鸭》的直评反写：鹰在谷场长大终坠粪堆）、*Borgmester Hoeck og Hustru*（1905）、末部大长篇 *Mands Himmerig*（1927，一战爆发时丹麦知识分子的危机）。
- **晚年**：1933–43 写两个版本的《回忆录》；晚年受失明与失聪之困仍关注政治与文化，直至最后岁月。
- **风格与影响**：自然主义文体——平实语言承载符号、暗喻与反讽，常返工旧作；丹麦现代作家中被讨论最多者之一，悖论缠身（时代的开明者/严峻的爱国者/反教权的清教徒/幻灭的斗士，与社会主义者合作却始终独立）；曾被评「既是 Georg Brandes 的绝对对立面，又是其最投缘的学生」；20 世纪丹麦文学的开拓者，「社会小说」标准的奠定者。2010 年 Naomi Lebowitz 译 *Lucky Per* 前英语世界长期无当代译本（2018 Paul Larkin 译 *A Fortunate Man*、2025 NYRB 译《白熊》等）。
- **关键时间线（15 节点）**：
  1857-07-24 生于 Fredericia → 牧师世家 → 弃工程师学业 → 小学教师 → 自由记者 → 1881 出道 → 1883 *Landsbybilleder* → 1886 *Mimoser* → 1887 *Fra Hytterne*/*Isbjørnen* → 1889《Messias》/与发妻分居 → 1890 *Skyer* → 1891–92 亵渎风波、Ernst Brandes 受罚自尽 → 1892 娶 Kofoed → 1891–95 *Det forjættede Land* → 1894 *Nattevagt*（与 Ring 绝交）→ 1898–1904 *Lykke-Per* → 1912–16 *De dødes Rige* → **1917 与 Gjellerup 共享诺贝尔文学奖** → 1927 *Mands Himmerig* → 1933–43 两版本《回忆录》→ 1943-08-21 卒于 Charlottenlund。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | realism | 现实主义 | infobox Genre：Realist writer | 封面、核心页 |
| 1 | social criticism | 社会批判 | 第一阶段叛逆写作、*Skyer* | 乡村页 |
| 2 | social novel | 社会全景小说 | 巴尔扎克—左拉传统的丹麦版广角描写 | 三大小说页 |
| 3 | naturalism | 自然主义 | 其文体定位：平实语言 + 符号反讽 | 风格页 |
| 4 | short story | 短篇小说 | *Landsbybilleder*、*Mimoser*、*Isbjørnen* 等 | 短篇页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Karl Adolph Gjellerup | 无向 | 1917 年诺贝尔文学奖共享（两位丹麦作家平分） |
| spouse | Mette Marie Hansen | 无向 | 第一任妻子，北西兰农户之女，1889 分居 |
| spouse | Antoinette Caroline Elise Kofoed | 无向 | 1892 年结婚，1928 年去世 |
| colleague | Ernst Brandes | 无向 | 刊发《Messias》的出版人/报纸编辑，1891 因此被罚 300 克朗、1892 自杀 |
| controversy | L. A. Ring | 无向 | 挚友画家；*Nattevagt*（1894）取材其生活，Ring 视为背叛信任而绝交 |
| influence | Honoré de Balzac | 对方 → Pontoppidan | 三大社会小说承巴尔扎克传统 |
| influence | Émile Zola | 对方 → Pontoppidan | 三大社会小说承左拉传统 |

> Georg Brandes 仅存「对立面/最投缘学生」两说的批评史评价，非直接师承，**不入库**；H. C. Andersen 仅《丑小鸭》反写对话，**不入库**（均在提示词陷阱表中说明）。对手方入库用规范全名 Honoré de Balzac / Émile Zola。

### 第 5 步：设计配色 【人物专属】

- **主色**：石板青灰 `#37474F`（丹麦现实主义的冷峻与诚实）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgeReal` 现实主义/乡村 — 泥土褐 `#7A5C3E`
  - `badgeSociety` 社会全景小说 — 钢蓝 `#2C5F8A`
  - `badgeScandal` 亵渎风波/争议 — 铁锈红 `#9E3B2B`
  - `badgeLate` 晚年/回忆录 — 石墨 `#4A4A55`
- **背景母题**：柔和气泡 + 全景横卷装饰条（乡村地平线渐入城市天际线），呼应「丹麦全景画」母题。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 当代丹麦生活的真实描写 / Henrik Pontoppidan 1857–1943 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像（Ancher 1908 油画）+ 右信息网格（生卒、国籍、出生地、出身、经历、荣誉、核心领域）
03  核心贡献概览 — 现实主义 / 社会批判 / 社会全景小说 / 自然主义文体
04  早年：牧师世家的出走 (1857–1881) — 弃工程师、教师、记者、1881 出道、Broby 拉丁化之讽
05  乡村写实 (1883–1890) — Landsbybilleder、Fra Hytterne、Skyer：打破农民理想化描写（书影框①）
06  亵渎风波 (1889–1892) — Messias、Den gamle Adam、Ernst Brandes 罚款与自杀
07  三大社会小说总览 (1890–1920) — 巴尔扎克—左拉传统的丹麦版
08  Det forjættede Land (1891–95) — 幻想家的乡村布道梦
09  Lykke-Per (1898–1904) — 最著名的半自传：工程师之梦与孤独归宿（意象图式②）
10  De dødes Rige (1912–16) — 1901 民主胜利后的幻灭
11  短篇画廊 (1886–1905) — Mimoser、Isbjørnen、Nattevagt、Ørneflugt、Borgmester Hoeck
12  Nattevagt 与 Ring 绝交 — 取材挚友、背叛信任的代价
13  家庭与两段婚姻 — Mette Marie Hansen、Kofoed、两个儿子移居海外
14  1917 诺贝尔奖 — 与 Gjellerup 共享（获奖理由 EN 原文引文框）；晚年回忆录（1927–1943）
15  遗产：20 世纪丹麦文学的开拓者 + 结尾 — 翻译史（2010 Lebowitz 译本）
```

> 文学家无公式框：第 5/9/14 页用**代表作书影框 / 意象图式 / 获奖理由原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "for his authentic descriptions of present-day life in Denmark"（json 引号噪声清理后引用），强调「当代丹麦生活的真实描写」 |
| 两个 Brandes | **Ernst Brandes**（出版人/报纸编辑，亵渎风波受罚自尽）≠ **Georg Brandes**（批评家，Gjellerup 篇的 influence 对象）——同名区分是本篇最大陷阱；Georg Brandes 与 Pontoppidan 只有批评史两说（对立面/最投缘学生），勿写成师承 |
| 引语红线 | 「著名引语」讥讽姓氏拉丁化一句 page.md **未给原文**，只可转述"曾讥讽 Pontoppidan 源自 Broby 的拉丁化"；获奖理由 EN 原文是唯一可靠引文 |
| Ring 绝交 | *Nattevagt* 取材挚友 L. A. Ring，Ring 视为背叛信任而绝交——按 page.md 客观呈现，勿写成 Pontoppidan 恶意 |
| Ørneflugt | 是对安徒生《丑小鸭》的反写（谷场养大的鹰坠粪堆），是「直评/对话」非人身攻击，勿升级 |
| 婚姻时序 | 1889 结识 Kofoed 后与发妻分居（非即刻离婚）→ 1892 再婚；Kofoed 1928 去世；两子分别移居美国、巴西——勿合并简写 |
| 共享奖区分 | 1917 与 Gjellerup 共享，两人获奖理由不同（Gjellerup=诗歌理想、Pontoppidan=丹麦现实描写），勿互串 |
| 亵渎风波 | 匿名发表 → 被斥亵渎 → 出版人受罚自尽：按 page.md 客观陈述因果，勿渲染宗教冲突 |
| 译名 | Lykke-Per 通行《幸运的彼尔》（2018 Larkin 译本题 A Fortunate Man，两题并存可注） |
| Modern Break-Through | 本页拼写带连字符，勿与 Gjellerup 篇 Modern Breakthrough 混为拼写错误（同一运动的两种拼写） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Modern Break-Through | 现代突破 | 本页拼写带连字符 |
| Lykke-Per | 《幸运的彼尔》 | 1898–1904，最著名，半自传 |
| Det forjættede Land | 《应许之地》 | 1891–95 三卷 |
| De dødes Rige | 《死者之国》 | 1912–16 |
| Mands Himmerig | 《人的天堂》 | 1927 末部大长篇 |
| Skyer | 《云》 | 1890 政治短篇集 |
| Landsbybilleder | 《乡村图景》 | 1883 |
| latinisation | 拉丁化 | 姓氏 Pontoppidan ← Broby |
| Ernst Brandes | 恩斯特·布兰代斯 | 出版人/编辑，非 Georg Brandes |
| L. A. Ring | L. A. 林 | 丹麦画家，*Nattevagt* 取材对象 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（Alex-Productions）
- **风格标签**：历史感 / 深沉 / 追溯
- **匹配理由**：蓬托皮丹的三大社会小说横跨宪法斗争、工业化与革命觉醒的「过去时代」——「历史感」匹配全景画卷的年代纵深；「深沉」匹配其幻灭与冷峻的现实主义笔触；「追溯」匹配其两版《回忆录》的自我回望。
- **本地路径**：`music_audio/` 下 Alex-Productions PAST（对照 `curated_tracks.md`）→ 复制到 `literature/presentations/20th_century/Henrik_Pontoppidan/PAST.wav`。

> **开始执行。每完成一步汇报；无载禁写是最高红线。**
