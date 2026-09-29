# 文学家立传提示词（OpenLiterature · Patrick White）

> **目标项目**：OpenLiterature —— 开放文学史（与 OpenPhysicist/OpenChemist 共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Patrick Victor Martindale White（帕特里克·怀特，1973 诺贝尔文学奖）。
> **设计哲学**：文学家立传沿用「身份信息页 + 结构化研究领域」骨架；本篇无公式框，以**代表作书影/名句引文框/意象图式**替代。

---

## 一、模板定位

- **目标人物**：Patrick White，1973 年诺贝尔文学奖得主，迄今唯一获诺贝尔文学奖的澳大利亚作家。
- **一句话定位**：以现代主义笔法冲击澳洲现实主义传统、把「一片新大陆引入文学」的隐居预言家。
- **适配说明**：物理学家的「公式框」在本篇一律替换为「名句引文框/书影框」（"The Great Australian Emptiness" 段落与《Voss》书影）。

---

## 二、背景信息 【人物专属】

- **姓名**：Patrick Victor Martindale White；中文通译 帕特里克·怀特。
- **生卒**：1912-05-28 生于伦敦 Knightsbridge（澳大利亚富商父母度假期间）～ 1990-09-30 逝于悉尼家中（凌晨，肺炎/胸膜炎后拒绝住院），享年 78 岁。
  - ⚠️ metadata 死亡日期含 "1990-09-29" 噪声值，infobox 与正文均为 09-30，以正文为准。
- **获奖**：1973 年诺贝尔文学奖（1969 起入围短名单；曾明言不想要该奖，获奖后称其为 "a terrifying and destructive experience"，以健康为由拒绝赴瑞典领奖，由画家 Sidney Nolan 代为出席）。官方获奖理由（EN 原文，禁止改写）：
  > "for an epic and psychological narrative art, which has introduced a new continent into literature"
  > 中译（名录 CITATION_ZH）：「表彰其史诗性而深入心理的叙事艺术，将一片新大陆引入了文学」。
- **气质关键词**：**新大陆的史诗者、心灵的勘探者、孤傲的局外人**。
- **设计母题**：**曼陀罗与荒原（Mandala & Outback）**——其自述伴侣是 "the central mandala in my life's hitherto messy design"；《The Solid Mandala》书名直接呼应；背景可用同心圆/曼陀罗纹样 + 内陆赭红地平线装饰。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Patrick_White/page.md`（Wikipedia 全文，已核对）
  - 同目录 `metadata.json`、`images.txt`；Wikipedia URL：https://en.wikipedia.org/wiki/Patrick_White
- **肖像**：第 0 步待下载（page.md 内嵌 c.1940s 照与 1972 照；另有 de Maistre 1940 肖像与 Louis Kahan 1962 Archibald 奖肖像记载）。

---

## 三、任务流程 【逐步执行，每步汇报】

### 第 0 步：事实基准（已核对 page.md，禁止再杜撰）

- **家庭与童年**：父 Victor Martindale White 为富裕牧羊业主；母 Ruth（娘家姓 Withycombe）；六个月大随家返悉尼；1916 迁入 Elizabeth Bay 大宅 "Lulworth"；四岁患哮喘终生缠身；与保姆 Lizzie Clark 更亲近（教他诚实与「不自吹自擂」）。
- **教育**：1920 Cranbrook School → 1922 南部高地寄宿学校 Tudor House（气候利于肺疾，广泛阅读、写剧本、英语出众）→ 1925-12-1929 英国 Cheltenham College（孤独压抑，自认同性恋加深疏离；表亲画家 Jack Withycombe 家是少数慰藉，其女 Elizabeth Withycombe 成为其首部自印诗集《Thirteen Poems》(c.1929，署名 Patrick Victor Martindale) 的导师）→ 辍学回澳做两年 jackaroo（Monaro Bolaro 与 Barwon Vale 牧场，写两部未刊小说）→ 1932-1935 剑桥 King's College 攻读法德文学。
- **剑桥与伦敦**：阅读 Joyce/Lawrence/Proust/Flaubert/Stendhal/Thomas Mann「with admiration」；赴康沃尔 Zennor 朝圣（Lawrence 写《恋》之地）；1935 《The Ploughman and Other Poems》300 册小量出版，后被其本人封禁；1936 伦敦 Pimlico 结识澳大利亚画家 Roy de Maistre——短暂恋人、终生导师与挚友，鼓励他「从内向外」写作、摆脱自然主义散文。
- **文学生涯**：1939 首部出版长篇《Happy Valley》（1941 获澳大利亚文学学会金奖）；1937 父亲去世遗赠 £10,000 支持全职写作；美国 Viking 出版社掌门 Ben Huebsch 成为其主要文学支持者（Huebsch 曾在美出版 Lawrence 与 Joyce）；《The Living and the Dead》(1941)、《The Aunt's Story》(1948)。
- **二战**：皇家空军情报军官；伦敦 Blitz 期间驻 Bentley Priory；1941-04 调北非，转战埃及、巴勒斯坦、希腊；1941-07 在亚历山大港附近结识等待入伍希腊皇家陆军的 Manoly Lascaris——终身伴侣（1941–1990），怀特自述其为「我此前凌乱人生设计的中心曼陀罗」。
- **回归澳洲**：1947-12 乘船返澳（战后不愿做「伦敦知识分子」）；1948 与 Lascaris 购悉尼郊外 Castle Hill 小农场 "Dogwoods"，务农售花菜奶与雪纳瑞幼犬；1951 年末宗教体验（雨季跌坐泥中）重燃信仰，重启创作；1955 《The Tree of Man》（「借一对平凡男女的一生暗示生活的所有可能面向」）与 1957 《Voss》奠定英美声誉；对澳洲本土批评界感到愤懑。
- **剧场与后期**：1961 《Riders in the Chariot》首次获澳洲普遍赞誉；剧作《The Season at Sarsaparilla》(1962)、《A Cheery Soul》(1963)、《Night on Bald Mountain》(1964) 对澳大利亚戏剧影响重大（《The Ham Funeral》1962 曾被阿德莱德艺术节以「诗歌与社会现实主义无法调和」为由拒演，风波后业余/职业演出均成功）；1964 迁 Centennial Park，离场前烧毁早年诗集与大部分手稿书信日记；1966 《The Solid Mandala》（塔罗/占星/易经/荣格心理学的兴趣入书）。
- **政治转向**：1969-12 首次政治示威（违法公开鼓动青年拒服兵役登记）；反对越战；为 Philip Roth《Portnoy's Complaint》出版作证反对审查；1975 获首任 Companion of the Order of Australia，1976-06 因总督 Kerr 解雇 Whitlam 政府并恢复骑士封号而辞职退勋，自此成为共和制倡导者；支持原住民自决与环保（Fraser Island 采砂抗争）；1981 起领导核裁军运动（1984 公开资助 Nuclear Disarmament Party）。
- **晚年**：1979 《The Twyborn Affair》畅销；1981 回忆录《Flaws in the Glass》（首次公开同性恋与 Lascaris 关系，生前最大畅销书，因辛辣肖像致 Nolan 考虑诽谤诉讼、友谊终结）；与剧场导演 Jim Sharman 长期合作（《The Night the Prowler》电影、《Big Toys》《Signal Driver》《Netherwood》等）；1986《Voss》歌剧；1987 《Three Uneasy Pieces》；坚决抵制 1988 建国二百周年官方庆典（「马戏解决不了严肃问题」）；1990-09-30 凌晨家中逝世。
- **荣誉**：ALS Gold Medal 1941/1955/1965；Miles Franklin Award 1957（首届）/1961；W. H. Smith Literary Award 1959；1970 曾获封爵士但拒绝；Australian of the Year 1973（受奖演称 Australia Day 应是「自省之日而非吹号之日」，并称他人更配此奖）；Nobel 1973；AC 1975（1976 辞）。
- **遗产**：1975 以诺奖奖金创立 Patrick White Award（表彰未获主流认可的澳洲作家）；影响 Keneally/Astley/Stow/Koch 等后辈；2006 国家图书馆购入手稿含未刊长篇《The Hanging Garden》(2012 出版)。
- **关键时间线（16 节点）**：1912 伦敦出生 → 六个月返悉尼 → 1925-29 Cheltenham → 1929-31 牧场 jackaroo → 1932-35 剑桥 → 1936 结识 de Maistre → 1939 《Happy Valley》→ 1940-45 RAF 情报军官 → 1941 结识 Lascaris → 1948 回澳定居 Castle Hill → 1951 宗教体验 → 1955/1957 《人树》《沃斯》→ 1962-64 剧场全盛 → 1964 迁 Centennial Park 焚稿 → 1973 诺贝尔奖（拒赴）+ 年度澳大利亚人 → 1976 辞勋 → 1981 《镜中瑕疵》→ 1990-09-30 逝世。

### 第 4 步：文学领域表（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modernist fiction | 现代主义小说 | 冲击澳洲现实主义传统 | 核心页 |
| 1 | psychological narrative fiction | 心理叙事小说 | 官方获奖理由核心词 | 核心页 |
| 2 | Australian outback epic | 澳洲内陆史诗 | 《人树》《沃斯》 | 大陆页 |
| 3 | satirical fiction | 讽刺小说 | 对物质主义社会的讽刺 | 主题页 |
| 4 | modern drama | 现代戏剧 | 对澳大利亚戏剧影响重大 | 剧场页 |

### 第 4.5 步：社会关系表（与 yaml relations 完全一致，仅收 page.md 明载）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Manoly Lascaris | 无向 | 终身伴侣（1941–1990），自述为人生设计的中心曼陀罗 |
| influence | James Joyce | 无向 | 导语明载的现代主义影响源 |
| influence | D. H. Lawrence | 无向 | 导语明载的现代主义影响源 |
| influence | Virginia Woolf | 无向 | 导语明载的现代主义影响源 |
| colleague | Roy de Maistre | 无向 | 画家，短暂恋人亦为良师益友，鼓励其从内向外写作 |
| colleague | Sidney Nolan | 无向 | 画家挚友，代赴 1973 诺奖典礼，后因回忆录决裂 |
| colleague | Ben Huebsch | 无向 | Viking 出版社社长，其在美国的主要文学支持者 |
| colleague | Elizabeth Withycombe | 无向 | 亲戚，早期诗集的导师 |
| colleague | Jim Sharman | 无向 | 剧场导演，长期合作关系 |

> 婚姻类型说明：White 与 Lascaris 未正式结婚，入库用 spouse 类型、note 注明「终身伴侣」；Proust/Flaubert/Stendhal/Mann 仅为「with admiration」的阅读清单，禁建关系；Eliot 仅出现在批评者叙述（style 节）中，禁建关系；Keneally/Astley/Stow/Koch 为受其影响的后辈（page.md 明载）——如需可作 student 方向影响者，但为防噪声本篇不建（在 Review 时可议）。

### 第 5 步：配色方案

- **主色**（预分配）：赭褐 `#5C3A1E`（内陆荒原与曼陀罗的土色）
- **辅色**：诺奖香槟金 `C9A227`
- **badge 四分类色**：
  - `badgeModern` 现代主义小说 — 深靛紫 `#283593`
  - `badgePsyche` 心理叙事 — 玫瑰灰 `#8C4A5E`
  - `badgeOutback` 澳洲内陆史诗 — 砖红 `#A65A2E`
  - `badgeTheatre` 现代戏剧 — 墨绿 `#1E4E3E`
- **背景母题**：同心圆曼陀罗纹样（稀疏）+ 赭红地平线细线。

### 第 6 步：幻灯片序列（15 页）

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 把新大陆引入文学的人 / Patrick White 1912–1990 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（本名/生卒/教育/伴侣/荣誉/核心领域）
03  核心贡献概览 — 现代主义小说 / 心理叙事 / 内陆史诗 / 现代戏剧
04  两片大陆的童年 (1912–1929) — 伦敦出生、悉尼 Lulworth、哮喘与保姆、Cheltenham 囚笼
05  牧场与剑桥 (1929–1935) — jackaroo 岁月、法德文学、《The Ploughman》
06  伦敦与 de Maistre (1936–1939) — 「从内向外」写作、《Happy Valley》
07  战争与曼陀罗 (1940–1948)（核心贡献页）— RAF 情报军官、Lascaris、三部长篇
08  Castle Hill 的农夫作家 (1948–1955) — Dogwoods 农场、1951 宗教体验、《人树》
09  《Voss》与新大陆史诗 (1957–1961)（书影框）— Miles Franklin 首届、《战车上的骑士》
10  剧场岁月 (1962–1966) — 《Ham Funeral》风波、Sarsaparilla、《The Solid Mandala》
11  诺贝尔奖 1973 — 拒赴斯德哥尔摩、Nolan 代领、「terrifying experience」
12  良心公共人 (1969–1981) — 反战/反审查/辞勋/共和制/核裁军（客观陈述）
13  《镜中瑕疵》与晚年 (1981–1990) — 回忆录、Sharman 合作、抵制二百周年、家中逝世
14  遗产：Patrick White Award 与后辈作家
15  结尾
```

### 第 7 步：版式要点

- 身份信息页国籍行写「澳大利亚（生于英国伦敦）」——「唯一澳大利亚诺奖作家」是身份页必备要素。
- 引文框首选 "The Great Australian Emptiness"（1958 演说段，page.md 明载全文）——注意原文较长，须分栏或摘前两句并注明节选。
- 伴侣关系表述统一用「终身伴侣 Manoly Lascaris」，不用「妻子/丈夫」。

### 第 8 步：专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 死亡日期噪声 | metadata 有 09-29，infobox/正文均 09-30，以 09-30 为准 |
| 「唯一澳大利亚诺奖作家」 | 须加限定：Coetzee 2003 获奖时为南非公民（2006 才入籍澳洲）——page.md 注释明载，立传表述须严谨 |
| 诺奖态度 | 受奖前后言论矛盾（1971 明言不想要 → 获奖后拒绝赴宴但引出作品热潮）——两处都按 page.md 并写，勿只取其一 |
| 影响者层级 | 导语句 Joyce/Lawrence/Woolf 可建 influence；style 节出现 Eliot 是批评者叙述，禁建；剑桥阅读清单禁建 |
| Lascaris 身份 | 1941 亚历山大港相识，等待加入希腊皇家陆军；非「军人同事」，为终身伴侣 |
| 《The Hanging Garden》 | 未完成遗作，2012 才出版，勿列入生前作品年表正文 |
| 政治红线 | 政治立场（越战/惠特拉姆/共和制/核裁军）只按 page.md 客观列举事件与立场，不作评价；与 Whitlam 的 Fraser Island 分歧一句带过 |
| 焚稿事件 | 1963-64 离开 Dogwoods 前买回并烧毁早年诗集与手稿——事实确凿可写，但年份口径「1963 母亲去世、1964 迁居前」分清 |
| Nolan 关系方向 | 1973 代领诺奖（正面）→ 1981 因回忆录肖像决裂（负面）——时间顺序勿颠倒 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险点 |
|------|------|------|
| The Tree of Man | 《人树》 | 1955 |
| Voss | 《沃斯》 | 1957，探险家题材 |
| Riders in the Chariot | 《战车上的骑士》 | 1961 |
| The Solid Mandala | 《坚实的曼陀罗》 | 1966，双胞胎题材 |
| The Vivisector | 《活体解剖者》 | 1970，画家题材 |
| The Eye of the Storm | 《风暴眼》 | 1973 |
| The Twyborn Affair | 《特莱庞的爱情》 | 1979 |
| Flaws in the Glass | 《镜中瑕疵》 | 1981 自传 |
| Trümmerliteratur 无关 | — | 勿与德语战后文学混淆（批次对照） |
| Miles Franklin Award | 迈尔斯·富兰克林奖 | 1957 首届即获奖 |
| Australian of the Year | 年度澳大利亚人 | 1973 |
| jackaroo | 牧场见习工 | 1929-31 职业经历 |
| Manoly Lascaris | 曼诺利·拉斯卡里斯 | 终身伴侣，勿误写为助手 |

---

## 四、BGM 建议

- **选定曲目**：**Eternals** — Alex-Productions（预分配）。
- **匹配理由**：曲名的永恒感匹配「史诗性而深入心理的叙事艺术」的官方评语；宏大而内敛的织体匹配曼陀罗意象与内陆荒原的辽阔；末段升腾感匹配「把一片新大陆引入文学」的开创性。
- **备选**（未采用）：Cinematic Experience（过于戏剧化，弱化心理深度）；The Flow of Time（已用于他篇气质重叠）。
- **时长**：以 `music_audio/curated_tracks.md` 为准，>15 页 × 7 秒即可，ffmpeg `-shortest` 对齐。

---

## 五、数据入库说明（已完成）

- **yaml**：`MySQL/data/Patrick_White.yaml`，name_en=`Patrick White`（frontmatter 原形），qid=Q129187，primary_occupation=`writer`，fields 5 条（第 4 步表），relations 9 条（第 4.5 步表）。
- **入库**：`python3 seed_person.py data/Patrick_White.yaml`（幂等，按 QID → name_en 匹配）。
- **验证**：has_social_data=1、person_field≥4、person_relation≥2。

> **开始执行 Beamer 立传时，每写一页就 make，看到溢出就修。**
