# 文学家立传提示词（OpenLiterature：Naguib Mahfouz）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Naguib Mahfouz（1988 诺贝尔文学奖，唯一阿拉伯世界得主）为执行实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 〇、批次信息 【人物专属】

| 项 | 值 |
|----|----|
| 分批 | `literature/prompt_batches_lit.json` batch 17（agent：lit-batch-17） |
| dir / qid | Naguib_Mahfouz / Q7176 |
| 获奖年份 | 1988 |
| 主色（预分配） | `#0F4C5C` |
| BGM（预分配） | New Lands |
| page.md | `literature/presentations/pages/20th_century/Naguib_Mahfouz/page.md` |
| prompt / yaml | `literature/presentations/20th_century/Naguib_Mahfouz/Naguib_Mahfouz_zh.md` / `MySQL/data/Naguib_Mahfouz.yaml` |

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆与文学家侧首例（Knut Hamsun 等）的实战经验。
- **本实例**：Naguib Mahfouz Abdelaziz Ibrahim Ahmed Al-Basha（纳吉布·马哈福兹，نجيب محفوظ）。
- **设计哲学**：文学家立传无公式框——用**书影、名句引文框、小巷（the lane）意象图式**替代；保留「身份信息页」与「文学领域」的结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Naguib Mahfouz（1911-12-11 ~ 2006-08-30，享年 94 岁）
- **气质关键词**：**开罗小巷的编年史家、阿拉伯叙事艺术的奠基者、书桌前的公务员** —— 1988 诺贝尔文学奖获奖理由（官方原文 + 中译，禁止改写）：
  > "who, through works rich in nuance – now clear-sightedly realistic, now evocatively ambiguous – has formed an Egyptian narrative art that applies to all mankind"
  > （表彰其作品意蕴丰富——时而清明写实，时而唤起朦胧——形成了适用于全人类的阿拉伯叙事艺术）
- **设计母题**：**小巷（the lane）**。获奖理由「适用于全人类的埃及叙事艺术」+ 其小说恒常的「小巷=世界缩影」设定——Gamaleya 街巷、宫门街、Sukkariya 街连成一条可视觉化的长巷。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Naguib_Mahfouz/page.md`（同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Naguib_Mahfouz
- **肖像**：⏳ 第 0 步待下载（images.txt 有 `Naguib_Mahfouz_in_1960s.jpg` 250px 缩略图，建议取 500px 原图；失败则装饰圆占位）
- **参考模板**：
  - 文学家成品参照：`literature/presentations/20th_century/` 下已立传目录
  - 项目首页模板：`literature/presentations/cover/`（以主控实际封面文件为准）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- 生卒：1911-12-11 生于老开罗（Bayt al-Qadi 街区，Gamaleya；时属埃及赫迪夫国）~ 2006-08-30 逝于开罗阿古扎（Agouza，吉萨省），**摔倒并发症**，享年 94 岁
- 国籍：一生历经埃及六种国号（Khedivate→Sultanate→Kingdom→Republic→UAR→Egypt），yaml 收 Egypt 单条；tex 呈现「埃及」口径即可
- 家庭：下中产穆斯林家庭，幼子（七子女中最小，实如独子）；名字取自接生的产科名医 Naguib Pasha Mahfouz（**同名区分陷阱**，非亲属）；父 Abdel-Aziz Ibrahim 为公务员（自称「老派人」），母 Fatimah 为 Al-Azhar 谢赫 Mustafa Qasheesha 之女，不识字却常带其逛埃及博物馆与金字塔；家中宗教氛围严格（其自述引语「你绝不会想到那样的家庭会出艺术家」）
- 教育与职业：1930 入埃及大学（今开罗大学）**哲学系**，1934 毕业；读了一年哲学硕士后 1936 弃学从文；**公务员生涯 1934–1971**——开罗大学职员 → 1938 宗教基金部国会秘书 → 1945 Sultan al-Ghuri 陵墓图书馆（「善贷计划」访谈旧邻）→ 1950s 艺术局审查处长/电影扶持基金会主任 → 文化部顾问，1971 退休
- 文学影响：早期受 Hafiz Najib、Taha Hussein、Salama Moussa（费边派知识分子，其创办的 *Al Majalla Al Jadida* 刊发其处女作）影响；西方文学启蒙=侦探小说+俄国经典+**Proust/Kafka/Joyce 等现代主义作家**；历史小说三部曲受 **Walter Scott** 启发（30 卷埃及通史计划未竟）
- 创作体量：35 部长篇、350+ 短篇、26 部剧本、数百篇专栏、七部剧作，70 年笔耕（1932–2004）；全部小说以埃及为舞台，「小巷」是世界缩影
- 关键经历（客观简述，不作政治评价）：1919 革命窗前所见为其童年最大震动；支持 1978 戴维营协议致其书在多阿拉伯国家遭禁（至获奖后解禁）；因《Children of Gebelawi》争议长期在原教旨主义者「死亡名单」上，**1994-10-14 在开罗寓所外遇刺颈部重伤幸存**，右手神经受损，此后每日只能写作数分钟，终生贴身警卫；《Children of Gebelawi》2006 年（逝世当年）才首获埃及出版许可
- 关键荣誉：Nobel 1988（**唯一获该奖的阿拉伯作家**；因年事已高未赴斯德哥尔摩领奖）；尼罗河勋章大绶带；智利 Gabriela Mistral 勋章；法国艺术与文学指挥官勋章；意大利共和国功劳勋章大军官级；突尼斯国家功劳勋章；开罗大学荣誉博士
- 核心作品与贡献（4–6 条）：
  1. 《开罗三部曲》*The Cairo Trilogy*——《宫间街》（1956）、《思宫街》（1957）、《甘露街》（1957）：三代人、一战至 1944
  2. *Children of Gebelawi*《我们街区的孩子们》（1959）——寓言体代表作，屡遭查禁
  3. *The Thief and the Dogs*《小偷与狗》（1961）——存在主义转向
  4. *Midaq Alley*《梅达格小巷》（1947）——1995 墨西哥改编电影 *El callejón de los milagros*（Salma Hayek 主演）
  5. 历史小说三部曲：*Khufu's Wisdom*（1939）、*Rhadopis*（1943）、*The Struggle of Thebes*（1944）
  6. 晚年短章：《Autumn Quail》《Miramar》《Arabian Nights and Days》《The Harafish》《Akhenaten: Dweller in Truth》及《Echoes of an Autobiography》（1994）
- 关键时间线（约 16 节点）：1911 生于老开罗 → 1919 革命目击 → 1930 入开罗大学哲学系 → 1934 毕业、入公务员序列 → 1936 弃学从文 → 1939 首部长篇 *Khufu's Wisdom* → 1947 *Midaq Alley* → 1945 al-Ghuri 图书馆 → 1950s 审查处长等公职 → 1954 与 Atiyyatallah Ibrahim 结婚 → 1956–57 《开罗三部曲》→ 1959 *Children of Gebelawi*、搁笔数年 → 1959 起复出高产 → 1961 *The Thief and the Dogs* → 1971 公职退休 → 1988 诺贝尔奖 → 1994-10-14 遇刺重伤 → 2006-08-30 逝世；《Children of Gebelawi》埃及出版 → 2019 开罗马哈福兹博物馆开放

### 第 1–3 步：目录、Makefile 与肖像收集 【模板通用】

- 第 1 步：在 `literature/presentations/20th_century/` 下确认/创建 `Naguib_Mahfouz/` 与 `images/`
- 第 2 步：复制邻近已立传目录的 Makefile，改 `MAIN=Naguib_Mahfouz_zh`、`VIDEO_NAME=Naguib_Mahfouz_zh`
- 第 3 步：肖像下载——images.txt 有 URL 直接取（250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证）；404 则改用 Commons `Special:FilePath` 或 Wikipedia REST API `page/summary` 查 infobox 原图名；仍失败用装饰圆占位，图注注明「肖像暂缺」

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | arabic novel | 阿拉伯语小说 | 「适用于全人类的阿拉伯叙事艺术」 | 全篇 |
| 1 | literary realism | 文学现实主义 | infobox 明载 Movement；「清明写实」半边 | 现实主义页 |
| 2 | existentialism | 存在主义 | 与 Taha Hussein 并称的埃及文学先驱（page.md 明载） | 存在主义页 |
| 3 | historical novel | 历史小说 | 1939–1944 Walter Scott 式三部曲 | 历史页 |
| 4 | Cairo in fiction | 小说中的开罗 | 「小巷」缩影；Gamaleya 到 Abbaseya 的街巷地理 | 小巷页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Atiyyatullah Ibrahim | 无向 | 1954 年结婚（亚历山大港科普特正教家庭），两女 Fatima/Umm Kalthum |
| influence | Taha Hussein | direction: 影响者 | 明载早年影响者；二人并称埃及文学存在主义探索先驱 |
| influence | Salama Moussa | direction: 影响者 | 明载影响者；其创办的 Al Majalla Al Jadida 刊发马哈福兹处女作 |
| influence | Hafiz Najib | direction: 影响者 | 明载早年影响者 |
| influence | Walter Scott | direction: 影响者 | 历史小说计划（30 卷埃及通史）之灵感来源 |
| influence | Marcel Proust | direction: 影响者 | 明载西方现代主义阅读三家中之一 |
| influence | Franz Kafka | direction: 影响者 | 明载西方现代主义阅读三家中之一 |
| influence | James Joyce | direction: 影响者 | 明载西方现代主义阅读三家中之一 |
| colleague | Sayyid Qutb | 无向 | 早年开罗文学批评圈相识，Qutb 中期撰文赏识其才华；后于小说 Mirrors 中被负面刻画 |
| colleague | Salman Rushdie | 无向 | 1989 fatwa 事件中公开维护其表达自由（同时批评该书内容） |

**诚实注记**：Naguib Pasha Mahfouz（产科医生，同名来源）非亲属、不入库；Nabil Mounir/Reda Aslan（受其影响的律师）非文学关系、不入库；遇刺事件相关人物只在 tex 客观一句，不入库关系。

### 第 5 步：设计配色 【人物专属】

- **气质**：尼罗河的暮色、老开罗的土黄、书桌的沉静
- **配色**：主色 `#0F4C5C`（预分配深青蓝）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 阿拉伯语小说 — 深青蓝 `#0F4C5C`
  - `badgeB` 现实主义 — 陶赭 `#B4632C`
  - `badgeC` 历史小说 — 琥珀 `#E07B30`
  - `badgeD` 存在主义 — 玫瑰 `#C4204F`
- **背景母题**：透视长巷（两侧墙体色块渐次收窄）+ 暖色窗灯圆点——「小巷=世界缩影」的几何化表达；避免宗教符号（清真寺图形等一律不用）。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 小巷的编年史家 / Naguib Mahfouz 1911–2006 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 生卒、出生地街区、哲学系出身、公务员生涯、荣誉、核心领域
03  核心创作概览 — 现实主义 / 存在主义 / 历史小说 / 小巷叙事
04  早年：老开罗与 1919 (1911–1930) — Gamaleya 街区、严格家教、博物馆与金字塔的启蒙
05  哲学与弃学从文 (1930–1936) — 开罗大学哲学系、Salama Moussa 刊物、Taha Hussein 影响
06  历史小说与 Walter Scott (1939–1944) — 30 卷埃及通史计划及其未竟
07  小巷岁月：公务员与双线写作 (1945–1971) — al-Ghuri 图书馆、审查处长、Midaq Alley
08  代表作页：《开罗三部曲》(1956–57)（书影/引文框替代公式框）
09  《我们街区的孩子们》与搁笔 (1959) — 寓言结构、查禁史（客观一句）
10  存在主义转向与晚年实验 — The Thief and the Dogs / Miramar / Arabian Nights and Days
11  荣誉与认可 — Order of the Nile · Arts et Lettres · 1988 诺贝尔
12  1988 诺贝尔奖 — citation 官方原句引文框；「唯一阿拉伯世界得主」的里程碑
13  遇刺与晚年 (1994–2006) — 1994 遇刺一句客观带过；Echoes of an Autobiography；2006 逝世
14  遗产：从开罗小巷到全人类 — 改编影视（Midaq Alley 墨西哥版）、2019 博物馆
15  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

**Mahfouz 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 官方原句 "who, through works rich in nuance – now clear-sightedly realistic, now evocatively ambiguous – has formed an Egyptian narrative art that applies to all mankind"；中译从 CITATION_ZH 原样取（破折号对齐），禁止改写 |
| 同名区分 | 名字来源于产科医生 **Naguib Pasha Mahfouz**（无亲属关系），身份页/陷阱表必注 |
| 国号流变 | frontmatter 六个国号是历史噪声，tex 只呈现「埃及」；出生时属「埃及赫迪夫国」可一句注 |
| 宗教内容 | 《Children of Gebelawi》的「亚伯拉罕诸教寓言」只按 page.md 客观转述书的内容与查禁史；**不评价宗教、不渲染亵渎争议**；遇刺仅一句事实 |
| 政治内容 | Nasser/Sadat 相关表述、Camp David 立场、Rushdie 事件——只客观一句（「支持戴维营协议后多国禁书」「1989 公开维护 Rushdie 表达自由」），**不评价任何政权与人物** |
| 体量数字 | 35 部长篇/350+ 短篇/26 剧本/七部剧作（导语）与正文另一处「34 部」口径并存——tex 采用导语 35 部口径，不并写 |
| 三部曲年份 | Palace Walk 1956、Palace of Desire 1957、Sugar Street 1957；「完成于 1952 革命前、出版在后」可写 |
| 未赴颁奖礼 | 因年事已高未赴斯德哥尔摩（与 Seifert 因病由女儿代领**不同因**，勿混写） |
| 无载禁写清单 | 具体恋情史、子女私生活细节、获奖演讲（未出席故无演讲）、遗产分配——page.md 均无载，禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| the lane | 小巷 | 「小巷=世界缩影」核心意象 |
| The Cairo Trilogy | 开罗三部曲 | 宫间街/思宫街/甘露街 |
| Children of Gebelawi | 我们街区的孩子们 | 亦译《我们巷里的孩子们》，取通行名 |
| Midaq Alley | 梅达格小巷 | 1947 |
| The Thief and the Dogs | 小偷与狗 | 1961 |
| literary realism | 文学现实主义 | infobox Movement 口径 |
| Khedivate of Egypt | 埃及赫迪夫国 | 出生时国号，注释用 |
| Sayyid Qutb | 赛义德·库特布 | 仅文学批评圈交集口径 |
| Order of the Nile | 尼罗河勋章 | 埃及最高荣衔 |
| El callejón de los milagros | 《奇迹小巷》（墨西哥改编） | 1995，Salma Hayek 主演 |

---

### 第 9 步：执行终检清单 【模板通用】

- [ ] 页数与第 6 步序列一致（`pdftoppm` 逐页目检；出 mp4 后核时长）
- [ ] 获奖理由 EN 原句与 CITATION_ZH 中译逐字核对（含破折号与标点）
- [ ] 生卒/享年三处一致（封面、身份页、结尾页）
- [ ] 溢出：vbox ≤10pt、hbox ≤50pt；引文框不破行
- [ ] yaml 关系与第 4.5 步表逐行一致；note 无裸冒号/引号头
- [ ] 品牌口径：结尾页底部 `OpenMathAI`，引号半角

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **New Lands** — Alex-Productions（预分配）
- **风格**: 探索感 / 开拓 / 辽阔
- **匹配理由**:
  - "新大陆" 匹配其获奖的世界意义 —— 「适用于全人类的阿拉伯叙事艺术」：阿拉伯文学第一次以此姿态进入世界文学版图
  - "辽阔" 匹配三部曲的编年史纵深 —— 一条小巷展开三代人的史诗地理
  - 避开本批已用曲（Tragedy/With Me/Eternals/Cinematic Experience），无撞曲
- **备选** (未采用): ★★ Expedition（编年史远征感，与 Brodsky 侧无撞但气势略窄）；★ Timeless（编年史纵深，高频曲避让）
- **本地路径**: `music_audio/alex-productions/` 下 New Lands 对应 wav（复制到 `literature/presentations/20th_century/Naguib_Mahfouz/New Lands.wav`）
- **时长**: 以实际文件为准，ffmpeg `-shortest` 自动对齐

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：引语只用 page.md 英文原句；无载禁写；宗教/政治内容客观一句不评价；关系表与 yaml 完全一致。**
