# 文学家立传提示词（Luigi Pirandello）

> **OpenLiterature 人物专属立传提示词**：Luigi Pirandello（路伊吉·皮兰德娄，1934 诺贝尔文学奖，意大利现代主义戏剧家）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框——用名句引文框/意象图式/书影替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Luigi Pirandello（1867–1936），《六个寻找剧作家的角色》作者，悲闹剧大师，荒诞派戏剧的先声。
- **设计哲学**：文学家立传必须有「身份信息页」，并以**代表作书影/名句引文框/意象图式**替代公式框——本篇设计母题为「面具与镜」。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Luigi Pirandello（1867-06-28 ~ 1936-12-10，享年 69 岁）
- **气质关键词**：**人格面具的解剖者、戏中戏的发明者、悲闹剧（tragic farce）大师**
- **官方获奖理由（禁止改写）**：
  - EN: "for his bold and ingenious revival of dramatic and scenic art"
  - 中译（取自 CITATION_ZH）：「表彰其大胆而巧妙地复兴了戏剧与舞台艺术」
  - 注：1934 年由意大利皇家学院院士 **Guglielmo Marconi** 提名。
- **设计母题**：**面具与镜**。面具即人物、镜中即自我——"一个、没有一个、十万零一个"的人格分裂主题；视觉语言用喜剧面具（意大利假面喜剧传统）、镜面碎片、舞台侧幕与聚光灯锥形光束。
- **本地数据源**：`literature/presentations/pages/20th_century/Luigi_Pirandello/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Luigi_Pirandello
- **肖像**：第 0 步待下载（infobox 1932 年照；images.txt 无 URL 则回退 REST API / Special:FilePath，404 用装饰圆占位）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】（已核对 page.md）

- 生卒：1867-06-28 生于西西里阿格里真托（当时名 Girgenti，出生地片区名 "Caos"）~ 1936-12-10 逝于罗马 Via Bosio 自宅，享年 69 岁；拒授国葬，1947 骨灰归葬西西里
- 家世：富有的硫磺业家族；父 Stefano Pirandello 参加加里波第千人远征直至 Aspromonte 战役；母 Caterina Ricci Gramitto 13 岁随父流亡马耳他——两家族均为反波旁、投身 Risorgimento 的理想主义者，统一后幻灭（这一理想与现实的落差渗透其幽默论）
- 教育：家中启蒙（老仆 Maria Stella 的传奇故事）；12 岁已写第一部悲剧；巴勒莫读中学（沉迷 Carducci、Graf）；1887 转罗马文学系（因与拉丁语教授冲突退学）→ 波恩大学，1891-03 以阿格里真托方言语音论文获罗曼语语文学博士；读德国浪漫派（Jean Paul、Tieck、Heine、Goethe），译歌德《罗马哀歌》
- 婚姻：1894 与 Maria Antonietta Portulano（1871–1959）结婚（父之荐），育二子一女：Stefano、Fausto、Rosalia "Lietta"
- **1903 家族灾难**：Aragona 硫磺矿水淹（父投入自有资本与妻子嫁妆），家道破产；妻精神受创半僵直，后偏执猜忌与暴力日重，**1919 被送入疗养院且再未离开**；Pirandello 白天授课写作、夜里看护病妻——就在此期间连载的小说《已故的帕斯卡尔》（Il Fu Mattia Pascal，1904）爆得大名（1905 德译）
- 论战：1908《论幽默》（L'Umorismo）引发与 **Benedetto Croce** 长年论战（愈演愈烈）
- 文学友人：**Luigi Capuana** 鼓励其专事叙事写作；与 Fleres、Gnoli、Ferri 等作家记者过从；1898 与 Italo Falbo、Ugo Fleres 创办周刊 Ariel
- 剧场突破：1916 Liolà、Pensaci, Giacomino!（Angelo Musco 成功演出）；1917 Così è (se vi pare)；1918 Il Gioco delle Parti；**1921** Valle 剧院首演《六个寻找剧作家的角色》（Sei Personaggi in Cerca d'Autore）罗马首演惨败（观众喊 "Asylum, Asylum!"），米兰演出大成功，随后伦敦、纽约——国际声誉确立；1922《亨利四世》（Enrico IV）米兰首演获普遍赞誉
- 代表作：小说 The Late Mattia Pascal（1904）、The Old and the Young（1913）、One, No One and One Hundred Thousand（1925–26 连载）；短篇集 Novelle per un anno（15 卷 1922–37）；剧作约 40 部（部分以西西里语写作）
- 政治口径红线：与法西斯关系只按 page.md 客观事实简述（1924 致墨索里尼申请入党信、1925 借墨氏之助出任罗马艺术剧院艺术指导、自称 "a Fascist because I am Italian" 与 "I'm apolitical" 并存、1927 当面撕党证、余生受 OVRA 监视、1935 诺奖奖章捐给 "Oro alla Patria" 熔金运动、纽约声明支持兼并埃塞俄比亚）——**逐条客观列出，不作政治评价、不加辩护或谴责叙事**
- 荣誉与晚年：1929 "Academic of Italy"；1934 诺奖（Marconi 提名）；1936-12-10 独自去世——他死后是最后一位获奖的意大利剧作家，直到 1997 Dario Fo
- 传播史：1930-07-14 BBC 播出《嘴上含花的人》改编——史上第一次声画兼备的电视剧广播
- 影响链（page.md 明载）：启发 Samuel Beckett、Harold Pinter 的存在探索戏剧；Sartre 的存在主义哲学受其人格分裂与存在暧昧主题启发
- 关键时间线：1867 生于 Girgenti → 1880 迁巴勒莫 → 1886 硫磺矿做工 → 1887 罗马 → 1889–91 波恩 → 1891 博士 → 1894 成婚+首部短篇集 → 1897 罗马师范学院教书 → 1903 矿灾 → 1904 Mattia Pascal → 1908 L'Umorismo+Croce 论战 → 1917 Così è → 1919 妻入疗养院 → 1921 Six Characters 罗马惨败/米兰大胜 → 1922 Enrico IV → 1924 入党申请信 → 1925 Teatro d'Arte → 1926 Uno, Nessuno → 1927 撕党证 → 1929 Academic of Italy → 1934 诺奖 → 1935 捐奖章 → 1936-12-10 去世

### 第 1–3 步：目录 / Makefile / 图片 【模板通用】

- `literature/presentations/20th_century/Luigi_Pirandello/` + `images/`；Makefile 改 `MAIN=Luigi_Pirandello_zh`；肖像 `file` 验证。插图可用 1935 与 Einstein 合影（page.md 图注称 "his friend"）。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | tragic farce | 悲闹剧 | 其闹剧被视为荒诞派戏剧先声 | 核心页 |
| 1 | metatheatre | 元戏剧 | 《六个寻找剧作家的角色》戏中戏结构 | 核心页 |
| 2 | humorism | 幽默论 | L'Umorismo（1908）理论纲领，Croce 论战焦点 | 理论页 |
| 3 | modernist drama | 现代主义戏剧 | 意大利现代主义运动代表（infobox Movement） | 戏剧页 |
| 4 | Sicilian literature | 西西里文学 | 部分剧作以西西里语写作；方言博士论文 | 乡土页 |

- 入库：`MySQL/seed_person.py data/Luigi_Pirandello.yaml`。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

> 仅收 page.md 明载。女儿 Rosalia 仅列名无链接，不入库；Grazia Deledda 仅为小说中的文本内指涉，无实际关系，禁入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Maria Antonietta Portulano | 无向 | 1894 结婚；1903 矿灾后精神受创，1919 入疗养院 |
| parent-child | Stefano Pirandello | 无向 | 长子，一战志愿参军被奥匈俘虏战后归家 |
| parent-child | Fausto Pirandello | 无向 | 次子 |
| colleague | Luigi Capuana | 无向 | 作家友人，鼓励其专事叙事写作 |
| controversy | Benedetto Croce | 无向 | 1908 L'Umorismo 引发的长年论战 |
| colleague | Albert Einstein | 无向 | 1935 合影，page.md 图注称 "his friend" |
| colleague | Guglielmo Marconi | 无向 | 意大利皇家学院院士，1934 年为其提名诺奖 |

### 第 5 步：配色 【人物专属】

- 主色 `#16324F`（分批预分配，深地中海蓝）+ 香槟金 `C9A227` + badgeA–D（badgeA 闹剧 `#3E5E8E` / badgeB 元戏剧 `#7C4E8E` / badgeC 幽默论 `#8E6E3E` / badgeD 西西里 `#4E7C5B`）。
- 背景母题：面具轮廓+镜面碎裂光斑+舞台光束。

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面头像+细边框；封面国籍行 `Italy`。
2. **身份信息页必做**（生卒/国籍/出生地 Girgenti/教育波恩博士/配偶/子女/任职师范学院+Teatro d'Arte/荣誉 Nobel 1934/核心领域）。
3. 品牌口径统一 `OpenMathAI`；引号半角 `" "`。
4. 引文框只放 page.md 英文原文：罗马首演观众喊 "Asylum, Asylum!"、官方获奖理由句；意大利语台词禁自译编造。
5. 法西斯相关七条事实按客观清单呈现（第 0 步红线），一页内完成、不铺陈。

### 第 6 步：幻灯片序列 【人物专属，14 页】

```
00  OpenLiterature 项目首页
01  封面 — 面具与镜的解剖者 / Luigi Pirandello 1867–1936 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）
03  核心概览 — 悲闹剧 / 元戏剧 / 幽默论 / 现代主义戏剧 / 西西里
04  阿格里真托的 Risorgimento 之子 (1867–1880) — 千人远征家世、Caos 片区、幻灭的种子
05  波恩的罗曼语文学者 (1887–1891) — 德国浪漫派、译《罗马哀歌》、方言博士论文
06  Capuana 与罗马记者圈 (1893–1902) — 叙事转向、Ariel 周刊
07  1903：矿灾与 Mattia Pascal — 家道破产、夜间看护、白天写作
08  L'Umorismo 与 Croce 论战 (1908) — 幽默论理论图式
09  妻病与家庭暗面 (1903–1919) — 偏执、疗养院、沉默的代价
10  1921：从"疯人院！"到世界舞台 — Six Characters 罗马惨败/米兰大胜
11  亨利四世与悲闹剧谱系 — 1922–1924 剧作序列
12  Uno, Nessuno e Centomila — 人格分裂主题意象图式
13  1934 诺奖与最后的冬天 — Marconi 提名、官方理由引文框、拒国葬
14  遗产：从荒诞派到存在主义 — Beckett/Pinter/Sartre 影响链与结尾
```

### 第 7–8 步：Beamer 与布局检查 【模板通用】

- 头部宏复用同侧成品骨架；每页 make+pdftoppm 目检；法西斯清单页条目多，用窄行距。

### 第 9 步：史实 + 术语审查 【人物专属】

**Pirandello 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 出生地 | Girgenti（1927 年改名 Agrigento）；出生片区名 "Caos"——可作趣味注脚，勿引申为象征解读 |
| 博士论文 | 阿格里真托方言语音研究（罗曼语语文学博士）——勿写成文学博士 |
| 意大利语书名 | 《已故的帕斯卡尔》= Il Fu Mattia Pascal（1904）；《一个、没有一个、十万零一个》= Uno, Nessuno e Centomila（1925–26）——书名年份勿混 |
| 妻病时间链 | 1903 矿灾致精神受创 → 偏执渐重 → 1919 入疗养院且再未离开——勿写成"1903 直接入疗养院" |
| 1921 惨败 | 罗马首演观众分裂喊 "Asylum!"，作者从侧门离开；米兰即大胜——两幕并写勿只取其一 |
| 政治事实 | 七条客观事实（入党申请/艺术剧院/双自陈/撕党证/OVRA/捐奖章/埃塞俄比亚声明）并列呈现——禁选择性只写单侧 |
| 诺奖提名 | 由 Marconi 提名——勿写成墨索里尼运作 |
| 拒国葬 | 拒绝墨索里尼提供的国葬，1947 骨灰归葬西西里——体现晚年与体制疏离 |
| Deledda | 其小说 Suo marito 含对 Deledda 的隐含指涉——仅为文本内指涉，禁建两人关系 |
| 意大利剧作家断代 | 最后一位获奖的意大利剧作家，直到 1997 Dario Fo——口径照 page.md |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| tragic farce | 悲闹剧 | 荒诞派先声口径 |
| Sei personaggi in cerca d'autore | 六个寻找剧作家的角色 | 1921 |
| metatheatre | 元戏剧 | 戏中戏结构 |
| L'Umorismo | 《论幽默》 | 1908 理论文本 |
| Enrico IV | 《亨利四世》 | 1922 |
| Il Fu Mattia Pascal | 已故的帕斯卡尔 | 1904 |
| Novelle per un anno | 为一年而作 | 15 卷短篇总集 |
| Teatro d'Arte di Roma | 罗马艺术剧院 | 1925 出任艺术指导 |
| Risorgimento | 意大利统一运动 | 家族背景 |
| Sicilian language | 西西里语 | 部分剧作用语 |
| OVRA | 法西斯秘密警察 | 1927 起受其监视 |
| Oro alla Patria | 献给祖国的黄金 | 1935 熔金运动 |

---

## 四、BGM 建议 ✅ 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions
- **匹配理由**: "海" 匹配地中海出身（阿格里真托面向西西里海的硫磺之乡）与其戏剧的潮汐式结构——罗马惨败与米兰大胜、理想与幻灭的两极涨落；开阔中带不安，契合面具之下的暗流。
- **备选**（未采用）: Tragedy（过重，盖过闹剧的乖张感）；The Flow of Time（已分配同批 O'Neill）。
- **本地路径**: 复制 SEA 对应曲目 → `presentations/20th_century/Luigi_Pirandello/SEA.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Luigi_Pirandello/page.md` | 事实基准（已核对） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 获奖理由中译（禁改） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
