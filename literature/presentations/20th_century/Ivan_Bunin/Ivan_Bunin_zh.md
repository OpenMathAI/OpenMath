# 文学家立传提示词（Ivan Bunin）

> **OpenLiterature 人物专属立传提示词**：Ivan Bunin（伊万·蒲宁，1933 诺贝尔文学奖，首位获诺奖的俄语作家）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框——用名句引文框/意象图式/书影替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Ivan Alekseyevich Bunin（1870–1953），俄国现实主义传统在 20 世纪的守护者、白俄流亡文学的道德与艺术代言人。
- **设计哲学**：文学家立传必须有「身份信息页」，并以**代表作书影/名句引文框/意象图式**替代公式框——本篇设计母题为「流亡者的庄园暮色与暗巷」。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Ivan Alekseyevich Bunin（伊万·阿列克谢耶维奇·蒲宁，1870-10-22 [旧历 10-10] ~ 1953-11-08，享年 83 岁）
- **气质关键词**：**"蒲宁锦缎"的文体家、俄国古典散文的守夜人、巴黎的流亡贵族**
- **官方获奖理由（禁止改写）**：
  - EN: "for the strict artistry with which he has carried on the classical Russian traditions in prose writing"
  - 中译（取自 CITATION_ZH）：「表彰其以严谨的艺术性承续俄国古典散文写作的传统」
  - 注：1933 年获奖，授奖直接契机是自传体小说《阿尔谢尼耶夫的一生》；诺奖演说称瑞典学院首次将奖授予一位流亡者。
- **设计母题**：**庄园暮色与暗巷**。奥廖尔省贵族庄园的童年麦田、安托诺夫苹果的香气，与巴黎 16 区雅克·奥芬巴赫路 1 号的流亡窗口、"幽暗的林荫道"（Dark Avenues）意象；视觉语言用俄式庄园剪影、雪原、烛光与塞纳河暮色。
- **本地数据源**：`literature/presentations/pages/20th_century/Ivan_Bunin/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Ivan_Bunin
- **肖像**：第 0 步待下载（infobox 1928 年照；images.txt 无 URL 则回退 REST API / Special:FilePath，404 用装饰圆占位）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】（已核对 page.md）

- 生卒：1870-10-22（旧历 10-10）生于沃罗涅日省家族庄园 ~ 1953-11-08 凌晨逝于巴黎阁楼公寓，享年 83 岁（死因：心力衰竭、心源性哮喘、肺硬化）；1954-01-30 葬于圣热纳维耶芙德布瓦俄国公墓
- 家世：俄国古老贵族后裔，先祖含诗人 Anna Bunina（1774–1829）与 Vasily Zhukovsky（1783–1852）；父 Aleksey Nikolayevich Bunin（1827–1906，豪爽嗜赌致家道中落）；母 Lyudmila（1835–1910，引其进入俄罗斯民间传说世界）
- 兄长 **Yuly Bunin**：因民粹派活动被遣返家中，为其家庭教师（心理学/哲学/社会科学），鼓励读俄国经典并写作，1920 年前是其"最亲密的朋友与导师"
- 教育：1881 入叶列茨公立学校，1886-03 因家贫未按期返校被开除（未完成学业）
- 早期：1887-05 首诗 Village Paupers 发表于彼得堡杂志 Rodina；1889 哈尔科夫政府文书→奥廖尔 Orlovsky Vestnik 报编辑助理→实际主编，与 Varvara Pashchenko 相恋（1894 终，嫁其友 Bibikov）
- 1895 首访首都：结识 Mikhailovsky、Chekhov（结成通信挚友）、Balmont、Bryusov 等；1899 与 **Gorky** 友谊始，加入其 Znanie（知识）出版社同人圈
- 1894-01 莫斯科会 **Leo Tolstoy**，一度追随其生活方式（探访教派村社、做粗活，因非法散发托尔斯泰派文献被判三月监禁遇大赦免）；后视其哲学为空想，但终生敬其散文
- 诗歌→散文转向：Falling Leaves（Листопад，1901）获首个普希金奖（连同《海华沙之歌》译本 1898）；Gorky 致 Bryusov 信中称其"我们时代的第一诗人"
- 1906-11 与 **Vera Muromtseva**（1881–1961）相恋，1922 年才正式结婚；其回忆录《蒲宁的一生》使她本身成名
- 名作序列：Antonov Apples（1900，首部公认杰作）→ The Village（1910，争议与盛名，Gorky 称"当日俄国最佳作家"）→ Dry Valley（1912）→ The Gentleman from San Francisco（1915–16，D. H. Lawrence 英译）→ Mitya's Love（1924）→ Sunstroke（1925）→ The Life of Arseniev（1927–33/39，Paustovsky 誉为俄国散文之巅）→ Dark Avenues（1943 纽约/1946 巴黎全本）→ Cursed Days（1918–20 日记，1926）
- 第二个普希金奖 1909（《诗集 1903–1906》+ Byron《该隐》等译）；同年当选俄国科学院院士
- 流亡：1917-04 与 Gorky 决裂（终生未愈）；1918-05 离莫斯科；1920-01-26 乘敖德萨最后一艘法轮离开，1920-03-28 抵巴黎；此后往返于巴黎寓所与格拉斯（Grasse）租别墅
- 1933 诺奖：法国俄侨社群狂欢（Zaitsev 回忆）；捐 10 万法郎入文学奖助基金但分配引发侨民作家争论——与 **Zinaida Gippius、Dmitry Merezhkovsky** 关系恶化（Merezhkovsky 曾提议分奖被拒）
- 战时：1941 拒赴美；居格拉斯 Villa Jeanette，家中长住 Leonid Zurov（1929 来访后终生）与 Nikolai Roshchin；坚定反纳粹，冒险藏匿逃亡者（含犹太钢琴家 A. Liebermann 夫妇），称 Hitler/Mussolini 为 "rabid monkeys"；占领期拒绝一切出版
- 晚年：1945 回巴黎；1946 获苏联国籍恢复令但终未回国（《回忆录》1950 对苏联文化界严苛批评+日丹诺夫决议是原因）；1948 与 Tsetlin/Zaitsev 争吵退出俄国作家记者联合会；1951 当选国际笔会首位名誉会员（代表流亡作家社群）
- 政治口径红线：Cursed Days/1924 流亡宣言等仅按 page.md 客观简述，**不作政治评价、不展开政治叙事、不引宣言原文**
- 关键时间线：1870 生 → 1881–86 叶列茨学校 → 1887 首诗发表 → 1889 奥廖尔办报 → 1894 遇托尔斯泰 → 1895 遇契诃夫 → 1898 首婚 Anna Tsakni → 1901 Falling Leaves+首个普希金奖 → 1906 遇 Muromtseva → 1909 院士+第二普希金奖 → 1910 The Village → 1915–16 San Francisco → 1917 与 Gorky 决裂 → 1920 流亡巴黎 → 1922 与 Muromtseva 正式完婚 → 1927–33 Arseniev → 1933 诺奖 → 1939–46 Dark Avenues → 1940–44 格拉斯藏匿逃亡者 → 1950 Memoirs → 1951 PEN 名誉会员 → 1953-11-08 去世

### 第 1–3 步：目录 / Makefile / 图片 【模板通用】

- `literature/presentations/20th_century/Ivan_Bunin/` + `images/`；Makefile 改 `MAIN=Ivan_Bunin_zh`；肖像 `file` 验证。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | short story | 短篇小说 | 短篇大师（Dark Avenues / San Francisco） | 核心页 |
| 1 | lyric poetry | 抒情诗 | 诗人成名在先（Falling Leaves、两获普希金奖） | 诗歌页 |
| 2 | poetic prose | 诗化散文 | 以诗的节奏驱动散文（自比 Turgenev） | 文体页 |
| 3 | literary realism | 文学现实主义 | Tolstoy/Chekhov 传统的忠实继承者 | 评价页 |
| 4 | émigré literature | 流亡文学 | 白俄流亡社群的道德与艺术代言人 | 流亡页 |

- 入库：`MySQL/seed_person.py data/Ivan_Bunin.yaml`。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

> 仅收 page.md 明载。Galina Kuznetsova 恋情（1927–1942）page.md 明载但类型白名单无对应（非配偶），**不入库**；Zurov/Roshchin 为家中长住者非学术关系，不入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Vera Muromtseva | 无向 | 1906 相恋相伴终生，1922 正式结婚；著《蒲宁的一生》 |
| spouse | Anna Tsakni | 无向 | 1898 结婚，1900 年激烈分居；子 Nikolai 早夭（1905） |
| influence | Leo Tolstoy | 对方→本人 | 1894 莫斯科会面，一度追随其生活方式；终生效敬其散文 |
| influence | Yuly Bunin | 对方→本人 | 兄长兼家庭教师，鼓励读俄国经典并写作 |
| colleague | Anton Chekhov | 无向 | 1895/1896 相识，通信挚友至 1904 |
| colleague | Maxim Gorky | 无向 | 1899 友谊始，Znanie 出版社同人；1917 决裂终生未愈 |
| controversy | Zinaida Gippius | 无向 | 1933 奖金分配风波致关系恶化 |
| controversy | Dmitry Merezhkovsky | 无向 | 曾提议共享诺奖被拒；奖金分配风波后交恶 |

### 第 5 步：配色 【人物专属】

- 主色 `#372A75`（分批预分配，深流亡紫）+ 香槟金 `C9A227` + badgeA–D（badgeA 短篇 `#5B4A9E` / badgeB 诗歌 `#8A6A3E` / badgeC 现实主义 `#3E6E7C` / badgeD 流亡 `#8E3E4E`）。
- 背景母题：俄式庄园剪影+雪原光斑+暗巷纵深线条。

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面头像+细边框；封面国籍行 `Russian Empire → France (émigré)`。
2. **身份信息页必做**（生卒含新旧历/国籍变迁/家世贵族/教育叶列茨/两任配偶/荣誉 Nobel 1933+普希金奖×2+院士/核心领域）。
3. 品牌口径统一 `OpenMathAI`；引号半角 `" "`。
4. 引文框只放 page.md 英文原文：1933 诺奖演说 "For us writers, especially, freedom is a dogma and an axiom..." 节句；诗句引文禁编造。
5. 政治内容（宣言/日记/战后归国之议）一律客观一句带过，不作评价、不引原文。

### 第 6 步：幻灯片序列 【人物专属，14 页】

```
00  OpenLiterature 项目首页
01  封面 — 俄国古典散文的守夜人 / Ivan Bunin 1870–1953 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）
03  核心概览 — 短篇 / 抒情诗 / 诗化散文 / 现实主义 / 流亡
04  沃罗涅日贵族的农家童年 (1870–1886) — 家世、Yuly 兄、叶列茨辍学
05  奥廖尔的年轻编辑 (1887–1895) — 首诗、Pashchenko、办报
06  托尔斯泰与契诃夫 (1894–1904) — 追随与背离、通信挚友
07  Gorky 圈与诗名 (1899–1909) — Znanie、Falling Leaves、两获普希金奖
08  The Village 与 Dry Valley (1910–1914) — 争议与盛名
09  环球旅人与 San Francisco (1907–1916) — 东方之行、Bird's Shadow
10  流亡：从敖德萨末班船到巴黎 (1917–1920) — 与 Gorky 决裂
11  Arseniev 与 1933 诺奖 — 官方理由引文框、流亡演说句、奖金风波
12  战时格拉斯 (1939–1944) — 藏匿逃亡者、Dark Avenues 写作
13  晚年：未归的归途 (1945–1953) — 苏德国籍令、Memoirs、PEN 名誉会员
14  遗产："蒲宁锦缎" — 文体传承与结尾
```

### 第 7–8 步：Beamer 与布局检查 【模板通用】

- 头部宏复用同侧成品骨架；每页 make+pdftoppm 目检；时间线页条目多注意行距压缩。

### 第 9 步：史实 + 术语审查 【人物专属】

**Bunin 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生日历法 | 新历 10-22 / 旧历 10-10 并写；frontmatter 噪声值 1870-01-01/1953-01-01 弃用 |
| 配偶次序 | Anna Tsakni（1898）在前、Vera Muromtseva（1922 正式）在后；Muromtseva 是相伴终生的伴侣 |
| 婚期 | 与 Muromtseva 1906 相恋但 1922 年才正式结婚（此时才办妥与 Tsakni 离婚）——勿写 1907 结婚 |
| 与 Gorky | 1899–1917 友谊与 1917 决裂并写；Gorky 决裂后仍荐其文为典范的细节保留 |
| 获奖理由 | 官方原句锚定"古典俄国散文传统"，勿替换为"因《幽暗的林荫道》"（1943 在获奖之后） |
| 首位 | "首位获诺贝尔文学奖的俄国作家"——勿写成"首位苏联作家"（他是流亡者） |
| Kuznetsova | 1927–1942 恋情明载但无对应关系类型——不入库，提示词注明即可 |
| 政治内容 | Cursed Days/宣言/日丹诺夫决议客观一句，禁评价禁引原文 |
| 战时 | 反纳粹+藏匿逃亡者（Liebermann 夫妇）明载可写；"rabid monkeys" 原语可引 |
| 死因 | 心衰+心源性哮喘+肺硬化——勿写单一"心脏病" |
| 葬地 | 圣热纳维耶芙德布瓦俄国公墓（1954-01-30 落葬）——勿与巴黎殡仪混淆 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Bunin brocade | 蒲宁锦缎 | 文体质地喻称 |
| The Village | 《乡村》 | 1910 |
| Dry Valley | 《苏霍多尔》（旱谷） | 1912 |
| The Gentleman from San Francisco | 《旧金山来的绅士》 | 1915–16 |
| The Life of Arseniev | 《阿尔谢尼耶夫的一生》 | 1927–33，获奖直接契机 |
| Dark Avenues | 《幽暗的林荫道》 | 1943/1946 |
| Cursed Days | 《该死的日子》 | 1918–20 日记 |
| Falling Leaves | 《落叶集》 | 1901 |
| Antonov Apples | 《安托诺夫苹果》 | 1900 |
| Pushkin Prize | 普希金奖 | 1903、1909 两获 |
| White emigre | 白俄流亡者 | 群体口径 |
| Znanie | 知识出版社 | Gorky 主导的同人出版圈 |
| Sreda | 星期三文学社 | 莫斯科同人圈 |

---

## 四、BGM 建议 ✅ 【人物专属】

- **选定曲目**: **Awaken** — Alex-Productions
- **匹配理由**: "觉醒" 匹配蒲宁的一生弧线——从庄园童年的感官觉醒（安托诺夫苹果、七颗昴星）到流亡中的文体自觉，再到 Dark Avenues 的晚年内心复燃；庄重中带暗涌，契合"锦缎"质地。
- **备选**（未采用）: Nostalgia（乡愁主题亦合但已分配给同批 Galsworthy）；Eternals（宏大但缺其内在张力）。
- **本地路径**: 复制 Awaken 对应曲目（alex-productions 36-aqLUvpAdLNQ）→ `presentations/20th_century/Ivan_Bunin/Awaken.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Ivan_Bunin/page.md` | 事实基准（已核对） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 获奖理由中译（禁改） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
