# 文学家立传提示词（OpenLiterature 批次实例：Gabriela Mistral）

> 本文件是 OpenLiterature 的「文学家立传提示词」，以 Gabriela Mistral（1945 诺贝尔文学奖，智利诗人）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框，以代表作书影/名句引文框/意象图式替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 共享仓库，结尾页品牌统一 `OpenMathAI`）。
- **本实例**：Gabriela Mistral（加夫列拉·米斯特拉尔，1889–1957），本名 Lucila Godoy Alcayaga，1945 诺贝尔文学奖得主，**首位获诺贝尔文学奖的拉丁美洲作家、第五位女性得主**。
- **设计哲学**：文学家立传以「代表作意象 + 文学领域结构化表达 + 身份信息页」为骨架；Mistral 的核心视觉语言是**风与哀歌（the mistral wind and the elegy）**——笔名里的米斯特拉风、四部诗集中流动的悲伤与母性。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Lucila de María del Perpetuo Socorro Godoy Alcayaga（1889-04-07 ~ 1957-01-10，享年 67 岁），笔名 **Gabriela Mistral**
- **气质关键词**：**拉丁美洲的歌哭之魂、诗人外交家、乡村教师出身的自学者**
- **官方获奖理由（1945）**：
  > EN: "for her lyric poetry, which inspired by powerful emotions, has made her name a symbol of the idealistic aspirations of the entire Latin American world"
  > 中译：表彰其由强烈情感所激发的抒情诗，使其名字成为整个拉丁美洲世界理想主义抱负的象征
  > （来源：`literature/generate_20th_century_list.py` CITATION_ZH[("1945","Gabriela Mistral")] + `literature/nobel_literature_citations.json`，禁止改写）
- **设计母题**：**风与哀歌**——从罗讷河口吹向普罗旺斯的米斯特拉风（笔名意象）贯穿版式：飘动的风纹线 + 悲怆与母性双色调（主色酒红配香槟金）。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Gabriela_Mistral/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`；Wikipedia URL: https://en.wikipedia.org/wiki/Gabriela_Mistral
  - 肖像（第 0 步下载）：`images/` 下待下载（page.md 内嵌青年期照片与 1950s 照，404 则装饰圆占位）

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md）

- **生卒**：1889-04-07 生于智利 Vicuña，成长于安第斯山村 Montegrande ~ 1957-01-10 卒于纽约州 Hempstead（胰腺癌），享年 67 岁；遗体九天后归葬智利，政府宣布全国哀悼三天，数十万人瞻仰。
- **国籍**：智利（Chile）。
- **身份**：诗人-外交家（poet-diplomat）、教育家、记者；广泛阅读神智学著作，1925 年加入世俗（第三）方济各会但很少望弥撒。
- **家庭**：父 Juan Gerónimo Godoy Villanueva 亦为教师，在她 3 岁时弃家出走、1911 年孤独离世；母 Petronila Alcayaga 为裁缝；姐姐 Emelina Molina 是其早年教育的引路人（虽日后有经济纠葛，Mistral 始终敬重她）；侄子 Juan Miguel Godoy（唤作 Yin Yin，视如己出）1943-08-14 自杀身亡（年仅 17），成为《Lagar》的悲怆底色。
- **教育**：正规教育止于 1900；自学成才——1923 年获智利大学**西班牙语教授学衔**。
- **笔名来历（两说并写）**：取自她钟爱的两位诗人 **Gabriele D'Annunzio** 与 **Frédéric Mistral**（1904 诺奖得主）；另一说取自**大天使加百列**与**普罗旺斯米斯特拉风**。1914 年《死之歌》获奖时首次署此名。
- **职业生涯**：15 岁起任助教养家；1906–1912 在 La Serena 附近、Barrancas、Traiguén、Antofagasta 等地任教；1912 Los Andes 中学六年；1918 年教育部长 Pedro Aguirre Cerda 任命为 Punta Arenas 的 Sara Braun 中学校长；1920 调 Temuco（在此结识少年聂鲁达）；1921 击败激进党背景对手任圣地亚哥 Liceo #6（全国最新最负盛名的女子学校）校长；1922 应墨西哥教育部长 José Vasconcelos 之邀赴墨参与图书馆/学校改革与国民教育体系建设；1925 退出智利教育界获养老金；1926 年起定居法国（此后终生流亡海外）；1930–31 哥伦比亚大学 Barnard 学院访问教授、1931 Middlebury/Vassar 短暂任教；**1932 年起任智利领事**（那不勒斯、马德里、里斯本、尼斯、洛杉矶、圣巴巴拉、韦拉克鲁斯、拉帕洛、纽约等地，直至去世）。
- **核心作品与贡献（4–6 条）**：
  1. *Sonetos de la muerte*（《死之歌》，1914）——获圣地亚哥 Juegos Florals 全国文学竞赛首奖，成名作。
  2. *Desolación*（《绝望》，1922，纽约出版，Federico de Onís 协助）——首部诗集，母性、宗教、自然、对儿童之爱；国际声誉的基石。
  3. *Ternura*（《柔情》，1924，马德里）——摇篮曲与童谣集；四千名墨西哥儿童曾齐唱其中诗篇向她致敬；「母性诗人」之称由此而来。
  4. *Tala*（《塔拉》，1938，布宜诺斯艾利斯，Victoria Ocampo 协助出版）——版税捐给西班牙内战孤儿；礼赞拉美与地中海欧洲民俗。
  5. *Lagar*（《压榨》，1954）——生前最后一部诗集（以节略形式出版）；写 Yin Yin 之死与二战/冷战之痛。
  6. 约 **800 篇散文**遍布西语世界报刊——地理、教育、作家剪影等；英语世界广为传引的《Su Nombre es Hoy》（"His Name is Today"，page.md 实载英译可引）。
- **关键荣誉**：Nobel 1945（11-15 得奖、12-10 国王 Gustaf V 亲授）；Chilean National Literature Prize 1951；Mills College 荣誉博士 1947；法国荣誉军团骑士；**智利 5000 比索纸币**肖像；Google Doodle（2015-04-07 诞辰 126 周年）。
- **关键时间线（18 节点）**：
  1. 1889-04-07 生于 Vicuña，本名 Lucila Godoy Alcayaga
  2. 成长于安第斯山村 Montegrande，姐姐任教的乡村小学
  3. 3 岁时父亲弃家出走（1911 独自离世）
  4. 15 岁起在 Compañía Baja 任助教养家
  5. 1904–1908 以多个笔名在 El Coquimbo、La Voz de Elqui 发表早期诗
  6. 1906 或结识铁路工人 Romelio Ureta（1909 自杀；恋情本身存疑，见陷阱表）
  7. 1907 被师范学校无解释拒收
  8. 1906–1912 多地乡村任教
  9. 1912 Los Andes 中学任教六年
  10. 1914 《死之歌》获 Juegos Florals 首奖，「Gabriela Mistral」笔名首用
  11. 1918 出任 Punta Arenas 中学校长；1920 Temuco；1921 圣地亚哥 Liceo #6 校长
  12. 1922 赴墨西哥助教改；*Desolación* 出版（纽约）
  13. 1923 获智利大学西班牙语教授学衔；1924 *Ternura*（马德里）
  14. 1925 退出教育界获养老金；加入第三方济各会
  15. 1925–26 国际联盟智力合作研究所代表；1926 起定居法国（终生流亡开始）
  16. 1932 起辗转各地任领事；1938 *Tala* 出版（版税捐西战孤儿）
  17. 1943 侄子 Yin Yin 自杀；1945 诺贝尔文学奖（首位拉美作家）
  18. 1951 智利国家文学奖；1954 *Lagar*；1957-01-10 卒于 Hempstead，归葬智利
- **实载引语**：《Su Nombre es Hoy》英译文 page.md 全文可引（"We are guilty of many errors and many faults, but our worst crime is abandoning the children..."）——用于儿童主题引文框。

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- `literature/presentations/20th_century/Gabriela_Mistral/`（含 `images/`）；Makefile 设 `MAIN=Gabriela_Mistral_zh`；肖像按 `images.txt` 下载，404 用装饰圆占位。

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | lyric poetry | 抒情诗 | 强烈情感激发的抒情诗（获奖理由核心） | 核心页 |
| 1 | Latin American poetry | 拉丁美洲诗歌 | 整个拉美世界理想主义抱负的象征 | 拉美页 |
| 2 | children's poetry | 儿童诗歌与摇篮曲 | Ternura、「母性诗人」 | 童诗页 |
| 3 | educational essay | 教育随笔 | 约 800 篇散文，教育改革与旅行书写 | 随笔页 |

- 入库：`MySQL/data/Gabriela_Mistral.yaml` → `python3 seed_person.py data/Gabriela_Mistral.yaml`（primary_occupation: writer）。

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Pablo Neruda | 无向 | Temuco 相识引其读诗，终生友谊；马德里领事任内亦有交往 |
| colleague | Victoria Ocampo | 无向 | 长期挚友与通信人，1938 协助在布宜诺斯艾利斯出版 Tala |
| colleague | Doris Dana | 无向 | 晚年伴侣与遗稿编辑（Dana 本人否认恋情，自称继母式关系） |
| rival | Amanda Labarca | 无向 | 教师工会立法语境中 page.md 明载的对手 |
| influence | Frédéric Mistral | Mistral → Mistral | 笔名取自其钟爱诗人（1904 诺奖得主；另有普罗旺斯风一说） |
| influence | Gabriele D'Annunzio | D'Annunzio → Mistral | 笔名取自其钟爱诗人 |

> 情感经历中 Ureta（存疑）不建关系；Pedro Aguirre Cerda（任命者）、José Vasconcelos（赴墨工作指导）属职务互动，page.md 未载私人交谊，不入库；Eleanor Roosevelt 等仅为「信得过的人」名单，不入库。

### 第 5 步：设计配色方案

- **主色**（批次预分配）：酒红 `#6E2B2B`（哀歌的深色与拉美的赤陶）
- **辅色**：诺奖香槟金 `#C9A227`
- **badgeA–D**：badgeA 抒情诗 — 石榴红 `#A34730`；badgeB 拉美诗歌 — 赤陶橙 `#C97B30`；badgeC 儿童诗歌 — 暖沙 `#B08D3E`；badgeD 教育随笔 — 风青 `#2C6E8F`
- **背景母题**：风纹曲线自左上掠过 + 哀歌与摇篮曲的明暗双圆对照。

### 第 6 步：幻灯片序列（16 页）

```
00  OpenLiterature 项目首页（\input cover 共享首页）
01  封面 — 风与哀歌 / Gabriela Mistral 1889–1957 + 主色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（本名/笔名、生卒、国籍、职业三重身份、荣誉、核心领域）
03  核心贡献概览 — 死之歌 / 绝望 / 柔情 / 塔拉 / 压榨
04  山村与弃教 (1889–1904) — Montegrande、父亲出走、15 岁助教
05  早期诗与第一次丧失 (1904–1913) — 报刊笔名、Ureta 存疑注记、师范拒收
06  Juegos Florals (1914) — 死之歌首奖、笔名诞生（两说并写）
07  从乡村教师到 Liceo #6 校长 (1912–1921) — Aguirre Cerda 任命、Temuco 遇聂鲁达
08  墨西哥与《绝望》(1922–1925) — Vasconcelos 教改、Desolación、Ternura、教授学衔
09  官方获奖理由引文框（EN 原文 + 中译，禁止改写）
10  流亡与领事岁月 (1925–1945) — 国联智力合作所、Barnard 讲席、环球领事履历
11  Tala 与奉献 (1938) — Ocampo 协助出版、版税捐西战孤儿、mestiza 认同
12  Lagar 与最后的爱 (1943–1954) — Yin Yin 之死、Doris Dana、生前末集
13  荣誉与身后 — Nobel 1945（首位拉美/第五位女性）、国家文学奖、5000 比索纸币、归葬与国哀
14  遗产 — Su Nombre es Hoy 引文框、对拉美诗歌的深远影响、Pinochet 挪用与学者再解读的客观一笔
15  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

- 版式：五部诗集可用书脊式竖排图式；引文框两条（获奖理由 + Su Nombre es Hoy）。
- **陷阱**：

| 陷阱 | 说明 |
|------|------|
| 本名与笔名 | 本名 Lucila Godoy Alcayaga；yaml name_en 用 frontmatter 的 **Gabriela Mistral**；笔名来历两说（诗人名/天使+风）并写，勿只取其一 |
| 同名区分 | 笔名源自 1904 年文学奖得主 **Frédéric Mistral**（法国，OpenLiterature batch 1 人物）——叙述时注明「同为诺奖得主的普罗旺斯诗人」，勿与智利诗人本人混淆 |
| 诺奖口径 | 1945-11-15 获奖消息、12-10 Gustaf V 亲授；「首位拉美作家、第五位女性」（page.md 明载），勿拔高为「首位拉美诺奖得主」（该口径涵盖所有奖项，页面未载） |
| Ureta 存疑 | 与铁路工人 Romelio Ureta 的恋情「或曾相识」，后续研究者质疑、近亲否认——必须带存疑注记；其自杀对《绝望》的情感印记是 page.md 明载的转述，勿写成既证事实 |
| 生日噪声 | frontmatter 取 1889-04-07 / 1957-01-10；卒因胰腺癌 |
| 政治内容 | Pinochet 时期挪用其形象、Fiol-Matta 的女同性恋论说、Dana 否认恋情——均按 page.md 客观一笔并置两说，**不站队、不评价** |
| Lagar 版本 | 1954 出版时为「节略形式」（truncated form）；Lagar II 1992 才出 |
| 引语 | 仅引 page.md 实载英文（Su Nombre es Hoy 全段）与官方获奖理由，禁编造中文名句 |

### 第 9 步：术语审查清单

| 英文 | 中文 | 风险 |
|------|------|------|
| lyric poetry | 抒情诗 | 获奖理由核心词 |
| Sonetos de la muerte | 死之歌 | 1914，Juegos Florals 首奖 |
| Juegos Florals | 花赛/全国文学竞赛 | 圣地亚哥，1914 |
| Desolación | 绝望 | 1922 首部诗集 |
| Ternura | 柔情 | 1924 摇篮曲童谣集 |
| Tala | 塔拉 | 1938；Gullberg 解作「ravage」 |
| Lagar | 压榨 | 1954 生前末集 |
| Poema de Chile | 智利诗篇 | 1967 遗作，Dana 编辑 |
| mistral wind | 米斯特拉风 | 笔名第二成分来源（一说） |
| poet-diplomat | 诗人外交家 | 职业三重身份之一 |
| Third Franciscan order | 第三方济各会（世俗） | 1925 加入 |
| mestiza | 混血认同 | 「vasco 血统的混血女」自述 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**With Me** — Alex-Productions（批次预分配）
- **匹配理由**：「与我同行」的陪伴感匹配 Mistral 的一生底色——从乡村教师到环球领事，她的哀歌始终为儿童与弱者而唱（版税捐孤儿、Welcome 式关怀、Su Nombre es Hoy）；钢琴式的温情与克制的忧伤，匹配「悲伤与母性」双主题的诗性人格，也匹配她与聂鲁达、Ocampo、Dana 之间跨越流亡岁月的友谊。
- **对照**：`music_audio/curated_tracks.md`（alex-productions 系列）。封面主色 `#6E2B2B`，批次内唯一。
