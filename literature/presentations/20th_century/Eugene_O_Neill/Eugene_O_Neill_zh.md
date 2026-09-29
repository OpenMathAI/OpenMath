# 文学家立传提示词（Eugene O'Neill）

> **OpenLiterature 人物专属立传提示词**：Eugene O'Neill（尤金·奥尼尔，1936 诺贝尔文学奖，美国现代悲剧奠基人）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框——用名句引文框/意象图式/书影替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Eugene Gladstone O'Neill（1888–1953），四度普利策戏剧奖、美国悲剧观念的开创者。
- **设计哲学**：文学家立传必须有「身份信息页」，并以**代表作书影/名句引文框/意象图式**替代公式框——本篇设计母题为「海雾、旅馆与长日入夜」。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Eugene Gladstone O'Neill（1888-10-16 ~ 1953-11-27，享年 65 岁）
- **气质关键词**：**美国戏剧之父、悲剧观念的独创者、永远的水手**
- **官方获奖理由（禁止改写）**：
  - EN: "for the power, honesty and deep-felt emotions of his dramatic works, which embody an original conception of tragedy"
  - 中译（取自 CITATION_ZH）：「表彰其戏剧作品的力量、真诚与深切情感，体现了独创的悲剧观念」
  - 注：1936 年由瑞典学院院士 **Henrik Schück** 提名。
- **设计母题**：**海雾、旅馆与长日入夜**。生于旅馆、逝于旅馆的一生闭环；海员岁月的海雾；视觉语言用海雾光斑、旅馆窗灯、日晷式暮色渐变。
- **本地数据源**：`literature/presentations/pages/20th_century/Eugene_O_Neill/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Eugene_O%27Neill
- **肖像**：第 0 步待下载（infobox 1936 年照；images.txt 无 URL 则回退 REST API / Special:FilePath，404 用装饰圆占位）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】（已核对 page.md）

- 生卒：1888-10-16 生于纽约朗埃克广场（今时代广场）Barrett House 旅馆 ~ 1953-11-27 逝于波士顿 Bay State Road Sheraton 旅馆（今波士顿大学 Kilachand Hall），享年 65 岁；临终低语 "Born in a hotel room and died in a hotel room"（英文原句可引）；葬于波士顿森林丘公墓；2000 年尸检研究结论：死因是小脑皮质萎缩（与酒精或帕金森无关）——与正文早先"帕金森样震颤"两口径并存
- 家庭：父 James O'Neill（1847 生，爱尔兰移民演员，酗酒）；母 Mary Ellen Quinlan（Ella，爱尔兰裔，因难产第三子而吗啡成瘾）；兄 Jamie 45 岁饮酒致死；父母与兄长在其成名前后三年内相继去世
- 童年：1895 入布朗克斯 St. Aloysius 天主教寄宿学校；1900 曼哈顿 De La Salle 走读；夏季度假地新伦敦蒙特克里斯托小屋（Monte Cristo Cottage，1971 国家历史地标）
- 教育：普林斯顿大学一年后退学（原因诸说不一——含"向 Woodrow Wilson 教授窗户扔啤酒瓶"的"或属无稽"传闻——禁选定单一说法）
- 海员岁月：数年海上生涯，抑郁酗酒与对海的深情并存——海成为多部剧的核心场景（Glencairn 系列以船上为幕）；加入 IWW 海运工人工会
- 1912 谷底与"重生"：在 Jimmy-the-Priest 寄宿公寓自杀未遂（该处与 Hell Hole 后来成为《送冰的人来了》场景）；同年与首妻离婚、感染肺结核；疗养院康复期自认"重生"，立志 "I want to be an artist or nothing"（原句可引）
- 师承：1914 秋入哈佛 **George Pierce Baker** 的著名编剧课 "Workshop 47"，一年后离开
- Provincetown Players：1916 年中加入（Susan Glaspell 回忆其 Commercial Street 客厅读剧 Bound East for Cardiff）；早期剧在普罗温斯敦与格林尼治村 MacDougal 街剧场演出，The Emperor Jones 等随后上百老汇
- 成名序列：Beyond the Horizon（1920 百老汇+首普利策）→ The Emperor Jones（1920）→ Anna Christie（1920，普利策 1922）→ The Hairy Ape（1922）→ Desire Under the Elms（1924）→ Strange Interlude（1928，普利策）→ Mourning Becomes Electra（1931）→ 唯一知名喜剧 Ah, Wilderness!（1933）→ 十年停笔 → The Iceman Cometh（1939 写/1946 上演）→ A Moon for the Misbegotten（1947 首演，数十年后被视为杰作）→ Long Day's Journey into Night（1941 写/1956 上演，1957 普利策+托尼，公认最佳）
- **唯一四度获普利策戏剧奖的剧作家**（1920/1922/1928/1957）
- 荣誉：1935 当选美国哲学学会；1936 诺贝尔文学奖（Schück 提名）；1957 托尼最佳戏剧奖；美国戏剧名人堂；1967 美国 1 美元邮票；1964 Eugene O'Neill Theatre Center 创立
- Strindberg 情结：深受 **August Strindberg** 影响，诺奖演说大半篇幅献给他（对 Russel Crouse 自陈"绝对真诚"）；对 Sophus Keith Winther 说 "I wish immortality were a fact..."
- 婚姻三段：Kathleen Jenkins（1909–1912 离异，子 Eugene Jr.）→ Agnes Boulton（1918–1929 离异，子 Shane、女 Oona）→ Carlotta Monterey（1929 起，为其组织生活支持写作，后溴化钾成瘾，分居未离）
- 子女悲剧：Eugene Jr.（耶鲁古典学家，1950 自杀）；Shane（成瘾后被父断绝关系，后跳窗自杀）；Oona（1943 年 18 岁嫁 54 岁 Charlie Chaplin，被父断绝关系至死未见）——**仅客观一句带过**
- Tao House 与 "the Cycle"：1937 迁丹维尔（今 Eugene O'Neill 国家历史遗址 1976）；计划十一剧的 Cycle（1755–1932 美国生活史诗）仅完成 A Touch of the Poet 与 More Stately Mansions；1943 写完三部自传剧后因手抖丧失写作能力
- 遗著：Long Day's Journey 1956 由 Carlotta 安排出版——违背其"死后 25 年不公开"遗嘱
- 关键时间线：1888 生于旅馆 → 1895 寄宿学校 → 1906 普林斯顿一年 → 1909 首婚 → 1910s 海上岁月 → 1912 自杀未遂+肺结核 → 1914–15 哈佛 47 工坊 → 1916 Provincetown → 1920 Beyond the Horizon+首普利策 → 1922 Anna Christie 普利策 → 1928 Strange Interlude 普利策 → 1931 Mourning Becomes Electra → 1936 诺奖 → 1937 Tao House → 1943 封笔 → 1953-11-27 逝于旅馆 → 1956 Long Day's Journey 出版 → 1957 第四普利策+托尼

### 第 1–3 步：目录 / Makefile / 图片 【模板通用】

- `literature/presentations/20th_century/Eugene_O_Neill/` + `images/`；Makefile 改 `MAIN=Eugene_O_Neill_zh`；肖像 `file` 验证。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | tragedy | 悲剧 | 独创悲剧观念（获奖理由核心词） | 核心页 |
| 1 | American realism | 美国现实主义 | 首批把 Chekhov/Ibsen/Strindberg 技法引入美国 | 核心页 |
| 2 | family drama | 家庭剧 | Long Day's Journey 等自传性家庭悲剧 | 自传页 |
| 3 | vernacular drama | 美语口语戏剧 | 美国英语口语对白入剧的先驱 | 语体页 |
| 4 | classical mask revival | 古典面具复归 | 希腊悲剧与日本能剧面具的现代复活 | 形式页 |

- 入库：`MySQL/seed_person.py data/Eugene_O_Neill.yaml`。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

> 仅收 page.md 明载。Louise Bryant 恋情无对应类型不入库；Charlie Chaplin 为姻亲但白名单无对应类型，不入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Kathleen Jenkins | 无向 | 1909 结婚，1912 离异；子 Eugene Jr. |
| spouse | Agnes Boulton | 无向 | 1918 结婚，1929 离异；子 Shane、女 Oona |
| spouse | Carlotta Monterey | 无向 | 1929 结婚，为其组织生活支持写作 |
| parent-child | James O'Neill | 无向 | 父，爱尔兰移民演员 |
| parent-child | Mary Ellen Quinlan | 无向 | 母（即 Ella O'Neill） |
| parent-child | Eugene O'Neill Jr. | 无向 | 长子，耶鲁古典学家，1950 自杀 |
| parent-child | Shane O'Neill | 无向 | 次子，成瘾后被父断绝关系 |
| parent-child | Oona O'Neill | 无向 | 女，1943 嫁 Chaplin 后被父断绝关系 |
| influence | August Strindberg | 对方→本人 | 自认深受其影响，诺奖演说大半献给他 |
| advisor-student | George Pierce Baker | 导师=对方 | 哈佛 47 号戏剧工坊导师（1914–1915） |
| colleague | Susan Glaspell | 无向 | 普罗温斯敦剧社同人，回忆其 1916 读剧 |

### 第 5 步：配色 【人物专属】

- 主色 `#A31621`（分批预分配，悲剧深红）+ 香槟金 `C9A227` + badgeA–D（badgeA 悲剧 `#7E1E23` / badgeB 现实主义 `#2E4A5E` / badgeC 家庭 `#8E5A2E` / badgeD 面具 `#3E5E4E`）。
- 背景母题：海雾光斑+旅馆窗灯矩形+日晷式暮色渐变。

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面头像+细边框；封面国籍行 `United States`。
2. **身份信息页必做**（生卒均为旅馆的闭环/国籍/父母/教育/三任配偶/荣誉 Nobel 1936+普利策×4+托尼 1957/核心领域）。
3. 品牌口径统一 `OpenMathAI`；引号半角 `" "`。
4. 引文框只放 page.md 英文原句："Born in a hotel room and died in a hotel room"、"I want to be an artist or nothing"、官方获奖理由句；台词禁自译编造。
5. 家族悲剧（三子女）与 Oona/Chaplin 事件各一句客观带过，不渲染。

### 第 6 步：幻灯片序列 【人物专属，14 页】

```
00  OpenLiterature 项目首页
01  封面 — 美国悲剧的奠基人 / Eugene O'Neill 1888–1953 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）
03  核心概览 — 悲剧 / 美国现实主义 / 家庭剧 / 口语戏剧 / 面具复归
04  旅馆里出生的孩子 (1888–1906) — 演员之父、寄宿学校、新伦敦夏日
05  普林斯顿一年与海上岁月 (1906–1912) — 离校诸说并写、IWW、Glencairn 船
06  1912：谷底与重生 — Jimmy-the-Priest、肺结核、"artist or nothing"
07  哈佛 47 号工坊与 Provincetown (1914–1916) — Baker、Glaspell、码头首演
08  百老汇的早期爆破 (1920–1924) — Beyond the Horizon、Emperor Jones、Anna Christie
09  实验的十年 (1924–1933) — Desire Under the Elms、Strange Interlude、面具剧
10  Strindberg 情结与 1936 诺奖 — 影响自陈、演说献词、官方理由引文框
11  Tao House 与未竟的 Cycle (1937–1943) — 十一剧计划、封笔
12  家族的三重悲剧 — Eugene Jr./Shane/Oona 各一句，克制的暗页
13  死后抵达的巅峰 (1953–1957) — Long Day's Journey 出版、第四普利策、托尼
14  遗产：生与死都在旅馆 — 闭环意象图式与结尾
```

### 第 7–8 步：Beamer 与布局检查 【模板通用】

- 头部宏复用同侧成品骨架；每页 make+pdftoppm 目检；剧作序列表格页压缩行距。

### 第 9 步：史实 + 术语审查 【人物专属】

**O'Neill 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 旅馆闭环 | 生于 Barrett House 旅馆，逝于波士顿 Sheraton 旅馆——闭环引语可引；勿写"生于医院" |
| 死因双口径 | 正文早先作帕金森样震颤；2000 年尸检结论为小脑皮质萎缩（与酒精/帕金森无关）——两口径并列或采用 2000 结论并标注 |
| 普林斯顿退学 | 原因诸说不一（威尔逊啤酒瓶"或属无稽"）——禁选定单一说法 |
| 普利策 | 四度（1920/1922/1928/1957），唯一四夺戏剧奖者——1957 座来自 1941 年写就的 Long Day's Journey |
| 遗嘱违背 | 1956 出版违背"死后 25 年不公开"遗嘱——Carlotta 的决定，客观写 |
| 姓名口径 | 全名 Eugene Gladstone O'Neill（Sr.）；子 Eugene O'Neill Jr. 勿与父混写 |
| Strindberg | influence（影响者）非师承 |
| Baker | 哈佛 47 号工坊一年——编剧课导师，勿写成"博士导师" |
| Chaplin | Oona 嫁 Chaplin 被断绝关系——客观一句，Chaplin 不入关系库 |
| 爱尔兰裔 | 父母均为爱尔兰移民/爱尔兰裔——国籍 United States，族裔另注 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Long Day's Journey into Night | 《长日入夜行》 | 1941 写/1956 出版/1957 普利策 |
| The Iceman Cometh | 《送冰的人来了》 | 1939 写/1946 上演 |
| The Hairy Ape | 《毛猿》 | 1922 |
| Mourning Becomes Electra | 《素娥怨——悲悼三部曲》 | 1931 |
| Strange Interlude | 《奇异的插曲》 | 1928，普利策 |
| Beyond the Horizon | 《天边外》 | 1920，首普利策 |
| Provincetown Players | 普罗温斯敦剧社 | 1916 起点 |
| Workshop 47 | 哈佛 47 号工坊 | Baker 编剧课 |
| Tao House | 陶宅 | 丹维尔故居，国家历史遗址 |
| the Cycle | （美国生活史诗）Cycle 计划 | 十一剧仅成二部 |
| Monte Cristo Cottage | 蒙特克里斯托小屋 | 新伦敦夏日故居 |
| tragic farce | （对比词）悲闹剧 | 属 Pirandello，勿混用 |

---

## 四、BGM 建议 ✅ 【人物专属】

- **选定曲目**: **Expedition** — Alex-Productions
- **匹配理由**: "远征" 匹配奥尼尔的一生航程——海上岁月、格林尼治村闯荡、百老汇爆破、丹维尔封笔：一部不断驶向自身黑暗的远征；进取与悲怆并置，契合其"独创悲剧观念"。
- **备选**（未采用）: Tragedy（被 turing 侧 1975-1982 与同侧多批使用过，避重）；The Flow of Time（时间感偏冷静）。
- **本地路径**: 复制 Expedition 对应曲目 → `presentations/20th_century/Eugene_O_Neill/Expedition.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Eugene_O_Neill/page.md` | 事实基准（已核对） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 获奖理由中译（禁改） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
