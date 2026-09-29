# 文学家立传提示词（OpenLiterature：Rudyard Kipling）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Rudyard Kipling（1907 诺贝尔文学奖，首位英语获奖者、最年轻得主）为实例。
> 结构对齐母本 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框——用**名句引文框 / 意象图式 / 书影**替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Joseph Rudyard Kipling（约瑟夫·鲁德亚德·吉卜林），1907 年诺贝尔文学奖得主。
- **设计哲学**：文学家立传强调「代表作与文学世界」+ 身份信息页；吉卜林的核心视觉语言是**帝国与丛林**——孟买的诞生地、拉合尔的报纸编辑室、佛蒙特雪夜孕育的《丛林之书》、萨塞克斯 Bateman's 庄园的静水。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Rudyard Kipling（1865-12-30 ~ 1936-01-18，享年 70 岁）
- **气质关键词**：**短篇小说革新者、帝国叙事者、儿童文学大师** —— 1907 诺贝尔文学奖获奖理由：
  > EN 原文（官方，禁止改写）: "in consideration of the power of observation, originality of imagination, virility of ideas and remarkable talent for narration which characterize the creations of this world-famous author."
  > 中译（CITATION_ZH）: 表彰这位举世闻名作家作品中展现的观察力、独创的想象力、思想的活力与非凡的叙事才能
- **设计母题**：**丛林与帝国（jungle & empire）**——狼群养大的 Mowgli、拉合尔博物馆前的老炮 Zam-Zammeh、恒河入海口的航道、威斯敏斯特教堂诗人角。四色 badge 取丛林绿/孟买金/军装红/海峡蓝。
- **本地数据源**：`literature/presentations/pages/20th_century/Rudyard_Kipling/page.md`（+ `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Rudyard_Kipling （肖像第 0 步**待下载**，infobox 有 1895 照片、1891 John Collier 肖像画）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）

---

## 三、任务流程 【逐步执行，每完成一步汇报】

### 第 0 步：事实基准（第一轮已核对 page.md）

- **生卒**：1865-12-30 生于英属印度孟买（Malabar Hill）~ 1936-01-18 卒于伦敦 Middlesex 医院（十二指肠溃疡穿孔）；骨灰葬威斯敏斯特教堂诗人角（Dickens/Hardy 之侧）
- **国籍**：英国（生于英属印度；Anglo-Indian 自我认同）
- **家庭**：父 John Lockwood Kipling（雕塑家/陶艺设计师，孟买 Sir J. J. 艺术学院首任校长/拉合尔 Mayo 艺术学院校长、拉合尔博物馆馆长）；母 Alice MacDonald（MacDonald 四姐妹之一）；表兄 Stanley Baldwin（三度英国首相，其葬礼抬棺人之一）
- **名字由来**：父母在 Staffordshire 的 Rudyard 湖畔定情，长子即以湖为名
- **婚姻**：1892-01-18 伦敦 All Souls 教堂娶 Caroline "Carrie" Starr Balestier（Henry James 证婚/交新娘）；1892 长女 Josephine 生于佛蒙特（1899 肺炎夭折）；1896 次女 Elsie；1897 子 John（1915 卢斯战役阵亡，18 岁）
- **教育**：Southsea 寄养（Lorne Lodge"荒凉之屋"，1871-77）→ United Services College（Westward Ho!, Devon，1878-82，后为《Stalky & Co.》背景）
- **任职/经历**：1882-89 拉合尔《Civil and Military Gazette》副编辑 → 1887-89 阿拉哈巴德《The Pioneer》→ 1889 环球之旅经日美返英 → 1892-96 美国佛蒙特（Naulakha 宅）→ 1897 Torquay/Rottingdean → 1902 购 Bateman's（Burwash，住至逝世）→ 1922-25 任圣安德鲁斯大学名誉校长（Lord Rector）
- **关键荣誉**：Nobel 1907（首位英语得主、时年 41 岁最年轻得主至今；Charles Oman 提名；拒受桂冠诗人与骑士封号多次）；FRSL；巴黎大学/斯特拉斯堡大学荣誉博士
- **核心作品与贡献**：
  1. 《Plain Tales from the Hills》（1888）——首部散文集
  2. 《The Jungle Book》（1894）/《The Second Jungle Book》（1895）
  3. 《The Light That Failed》（1891）、《Kim》（1901）、《Captains Courageous》（1897）
  4. 《Just So Stories》（1902）、《Puck of Pook's Hill》（1906）/《Rewards and Fairies》（1910，含《If—》）
  5. 诗：《Mandalay》《Gunga Din》（1890）、《The White Man's Burden》（1899）、《If—》（1910，1995 BBC 全英最爱诗）
  6. 科幻短篇 "With the Night Mail"（1905）/"As Easy As A.B.C."（1912）——间接说明（indirect exposition）技巧
  7. 《The Ritual of the Calling of an Engineer》（1922，加拿大工程师铁戒仪式文本）
- **关键时间线**（15–20 节点）：1865 生于孟买 → 1871-77 Southsea 寄养"荒凉之屋" → 1878 入 United Services College → 1882 返印度任《Civil and Military Gazette》副编辑 → 1885-88 每年西姆拉休假 → 1886《Departmental Ditties》→ 1888 一年六部短篇集/《Plain Tales》 → 1889 解约、经日本赴伦敦 → 1890《Mandalay》《Gunga Din》→ 1891 订婚 Wolcott 之妹 Carrie、Wolcott 猝逝 → 1892 与 Carrie 成婚（Henry James 交新娘）、定居佛蒙特 → 1892-95 Naulakha 时期：丛林之书诞生 → 1896 家庭纠纷离美返英 → 1897 子 John 生 → 1898 起 annual 南非度假（Rhodes 庄园 The Woolsack）→ 1899《The White Man's Burden》、Josephine 病逝 → 1901《Kim》→ 1902 购 Bateman's、《Just So Stories》→ 1905-07 科幻短篇 → 1907 诺贝尔奖（12-10 斯德哥尔摩受奖）→ 1915 John 阵亡于 Loos → 1918-22 帝国战争墓地委员会措辞（"Their Name Liveth For Evermore"/"Known unto God"/"The Glorious Dead"）→ 1922 铁戒仪式/圣安德鲁斯校长 → 1932 撰写首个皇家圣诞广播讲词 → 1936-01-18 卒

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | short story | 短篇小说 | 被视为短篇艺术的革新者 | 核心页 |
| 1 | poetry | 诗歌 | 军营歌谣、《If—》《White Man's Burden》 | 诗歌页 |
| 2 | children's literature | 儿童文学 | 丛林之书/Just So Stories，经典中的经典 | 儿童页 |
| 3 | travel literature | 旅行文学 | From Sea to Sea、日本与美国纪行 | 环球页 |
| 4 | science fiction | 科幻小说 | Aerial Board of Control 系列、硬科幻先声 | 科幻页 |

#### 4.1 入库操作
- `MySQL/data/Rudyard_Kipling.yaml` → `python3 MySQL/seed_person.py data/Rudyard_Kipling.yaml`
- `primary_occupation='writer'`、occupations：writer(0)/poet(1)/novelist(2)；nationality：United Kingdom
- 校验 fields≥4、relations≥2、has_social_data=1

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | John Lockwood Kipling | 对方→本人 | 父，艺术学院校长，为其谋拉合尔报社职位 |
| parent-child | Alice Kipling | 对方→本人 | 母，MacDonald 四姐妹之一 |
| parent-child | John Kipling | 本人→对方 | 独子，1915 卢斯战役阵亡 |
| spouse | Caroline Starr Balestier | 无向 | 1892 成婚，"Carrie"，共同经营其文学生涯 |
| colleague | Wolcott Balestier | 无向 | 合著《The Naulahka》，1891 猝逝 |
| colleague | Henry James | 无向 | 挚友，1892 婚礼交新娘人，赞其"最完整的天才" |
| colleague | H. Rider Haggard | 无向 | 1889 结识的终生挚友，1920 共创 Liberty League |
| colleague | Edward Elgar | 无向 | 将《The Fringes of the Fleet》谱曲 |

### 第 5 步：设计配色

- **主色**：丛林墨绿 `#145C54` + 诺奖香槟金 `C9A227`
- badgeA 短篇 — 军装红 `#8B1A1A`；badgeB 诗歌 — 峡谷蓝 `#1E4E79`；badgeC 儿童 — 琥珀 `#E07B30`；badgeD 科幻 — 玫瑰 `#C4204F`
- **背景母题**：热带植物叶影 + 老式印刷活字散点（拉合尔编辑室与丛林的双重底色）

### 第 6 步：幻灯片序列（16 页）

```
00  OpenLiterature 项目首页（\input cover 共享封面）
01  封面 — 帝国与丛林的叙事者 / Rudyard Kipling 1865–1936 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/名字由来/教育/婚姻/荣誉/核心领域）
03  核心贡献概览 — 丛林之书 / Kim / 诗歌 / 科幻先声
04  孟买与"荒凉之屋" (1865–1878) — Rudyard 湖命名/寄养创伤/文学起点自述（引文框）
05  拉合尔编辑室 (1882–1889) — Civil and Military Gazette/西姆拉/一年六书
06  环球与伦敦 (1889–1892) — 会晤马克·吐温/Wolcott 合作/与 Carrie 成婚
07  佛蒙特与丛林之书 (1892–1896) — Bliss Cottage 雪夜/Naulakha 宅
08  白人的负担与争议 (1897–1902) — Recessional/White Man's Burden 双读
09  Kim 与 Bateman's (1901–1902) — 拉合尔老炮开篇（引文框）/Just So Stories
10  1907 诺贝尔奖 — 官方理由 EN+中译/首位英语得主/41 岁最年轻
11  帝国诗人与南非岁月 — Rhodes 圈子/布尔战争记者
12  失子之痛 (1915–1918) — John 阵亡/Epitaphs of the War/战争墓地措辞
13  晚年与遗产 (1918–1936) — 铁戒仪式/圣诞广播/诗人角安葬
14  批评与再评价 — Eliot 编选/Orwell 长评/印度读者争议（客观呈现，不站队）
15  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 四要素（观察力/独创想象/思想活力/叙事才能）全引官方句；勿简写为"因丛林之书获奖" |
| 最年轻 | 41 岁得奖、"youngest recipient to date"（至今）——勿写成"史上最年轻得主永远" |
| 拒封号 | 拒桂冠诗人与骑士封号（sounded out 多次），勿写成"被授予" |
| 时代口径 | "The White Man's Burden" 等帝国主义争议：page.md 明载三种解读（颂扬/宣传/反讽警告），**三种并列呈现，不作评价、不站队**；印度 Dyer 事件按 page.md 澄清口径（仅捐 10 镑、"The Man Who Saved India" 非其言） |
| 亲子 | 子 John 1915 阵亡于 Loos（2015 CWGC 确认安葬地 Haisnes）；"My Boy Jack" 诗与 John 的关联 page 明示存疑——勿断言 |
| 引语红线 | 仅引 page.md 英文原句：孟买诗节、荒凉之屋自述、"Words are, of course, the most powerful drug used by mankind."、Henry James 与 Twain 评语；其余禁杜撰 |
| 同名区分 | Wolcott Balestier（合作者兄）≠ Beatty Balestier（妻弟纠纷）；H. Rider Haggard 非别人；John Kipling 之子身份注意与家犬 Jack 区分 |
| 无载禁写 | 不写"吉卜林是诺贝尔文学奖得主中最年轻的英国作家"外的头衔对比；不写与 Twain 有持续交往（仅 1889 一次会面） |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| The Jungle Book | 丛林之书 | 两部曲 1894/1895 |
| Kim | 基姆 | 1901，拉合尔开场 |
| If— | 《如果》 | 1910，末词破折号 |
| The White Man's Burden | 白人的负担 | 1899，争议必须三读并列 |
| indirect exposition | 间接说明 | 间接交代背景的叙事技巧 |
| Barrack-Room Ballads | 军营歌谣 | 1892 集成 |
| Naulakha | Naulakha 宅 | 佛蒙特宅邸，纪念 Wolcott 合作 |
| Anglo-Indian | 英印人 | 19 世纪语义=旅印英国人 |

---

## 四、BGM 建议

- **选定曲目**: **The Flow of Time** — Alex-Productions（56k views，高受众 / 时间感 / 纪录片）
- **匹配理由**: "时间感/纪录片" 匹配吉卜林跨越孟买—伦敦—佛蒙特—萨塞克斯的七十年生命轨迹，以及"帝国时代亲历者—后世不断重估"的世纪叙事；"纪录片" 匹配其记者出身的冷静笔法与战后战争墓地委员会的铭记工作
- **备选**（未采用）: SEA（流动感好但已分配给 Sienkiewicz）；Tragedy（失子之痛贴切但仅覆盖一页，以偏概全）
- **时长对齐**: ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Rudyard_Kipling/page.md` | 事实基准 |
| `MySQL/data/Rudyard_Kipling.yaml` | 入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |

> **开始执行。每写一页就 make，看到溢出就修。**
