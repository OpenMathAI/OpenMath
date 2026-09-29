# 文学家立传提示词（John Steinbeck）

> **OpenLiterature 人物专属立传提示词**：John Steinbeck（约翰·斯坦贝克，1962 诺贝尔文学奖，美国）。
> 执行 agent 按第三部分第 0–9 步逐步执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMath 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：John Ernst Steinbeck（约翰·恩斯特·斯坦贝克），「美国文学巨人」、大萧条时代的声音。
- **设计哲学**：文学家立传无公式框，以**代表作书影、名句引文框、意象图式**替代物理公式表达；必须有「身份信息页」（Identity / Bio 速览页），务必保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：John Steinbeck（1902-02-27 ~ 1968-12-20，享年 66 岁）
- **官方获奖理由（Nobel 官方 EN 原文 + 名录中译，禁止改写）**：
  > "for his realistic and imaginative writings, combining as they do sympathetic humour and keen social perception"
  > 「表彰其现实主义与想象性兼备的写作，将同情的幽默与敏锐的社会洞察融为一体」（1962 授予）
- **气质关键词**：**加州土地的歌者、劳动者的辩护人、冷峻的社会记录者**。
- **设计母题**：**尘与路（Dust & Road）**。萨利纳斯谷的尘暴、 Monterey 罐头厂街的浪花与 *Travels with Charley* 的房车公路——用沙土颗粒、公路线条与 Monterey 海岸线构成视觉母题。
- **本地数据源**：`literature/presentations/pages/20th_century/John_Steinbeck/page.md`（+ metadata.json / images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/John_Steinbeck
- **肖像**：第 0 步待下载（images.txt 有 1939 照、1962 瑞典行照等真实照片可用）。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；封面 `\input` 项目共享首页。

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md，直接使用）

- 生卒：1902-02-27 生于加州萨利纳斯 ~ 1968-12-20 逝于纽约曼哈顿（心脏病与充血性心力衰竭，时值 1968 流感大流行），享年 66 岁；骨灰 1969-03-04 归葬萨利纳斯 Garden of Memories 家族墓。
- 家庭：德/英/爱尔兰裔；父 John Ernst Steinbeck（ Monterey 县司库），母 Olive Hamilton（教师）；祖父 Johann Adolf Großsteinbeck 为巴勒斯坦 Mount Hope 农业殖民点创始人之一。婚三次：Carol Henning（1930–1943 离异）、Gwyn Conger（1943–1948 离异，二子 Thom 与 John IV）、Elaine Scott（1950 至去世）。
- 教育：Salinas High School 1919 → 斯坦福大学英语文学，1925 辍学无学位（勿写「斯坦福毕业」）。
- 职业：作家/小说家/短篇作家，二战与越战战地记者（*New York Herald Tribune* 1943、*Newsday* 1967）；一生著书 33 部（16 长篇、6 非虚构、2 短篇集）。
- 关键荣誉：California Commonwealth Club 金奖（1935，*Tortilla Flat*）；National Book Award（1939）与 Pulitzer Prize（1940，*The Grapes of Wrath*）；King Haakon VII Freedom Cross（1945，因《月落》对挪威抵抗运动的文学贡献）；**Nobel Literature 1962**（2012 解密档案显示为 Graves/Durrell/Anouilh/Blixen 之间的「折中选择」）；Presidential Medal of Freedom（1964-09，约翰逊授予）；American Academy of Arts and Letters（1948 当选）；三度奥斯卡编剧提名。
- 核心作品（4–6 条）：*The Grapes of Wrath*（1939，masterpiece，1939 畅销榜首、75 周年时销 1400 万册，Kern County 1939-08 禁书至 1941-01）；*Of Mice and Men*（1937，诺奖citation 称 "little masterpiece"）；*East of Eden*（1952，本人视为 magnum opus）；*Tortilla Flat*（1935）与 *Cannery Row*（1945，Monterey Ocean View Avenue 1958 改名 Cannery Row）；中篇 *The Red Pony*（1933）、*The Pearl*（1947）；非虚构 *Travels with Charley*（1960 横穿美国房车行，房车名 Rocinante）与 *The Log from the Sea of Cortez*（1951）。
- 关键时间线（15–20 节点）：1902 生萨利纳斯 → 1919 高中毕业 → 1919–1925 斯坦福辍学 → 1925 赴纽约谋生 → 1928 太浩湖看护人、遇 Carol → 1930 结婚、太平洋丛林定居 → 1930 遇海洋生物学家 Ed Ricketts → 1929 处女作 *Cup of Gold* → 1933 *The Red Pony*/*To a God Unknown* → 1935 *Tortilla Flat* 首个商业成功 → 1936 *In Dubious Battle* → 1937 *Of Mice and Men* → 1938 《丰收吉普赛人》报道系列 → 1939 *The Grapes of Wrath* → 1940 国家图书奖+普利策、科尔特斯海采集之旅 → 1941 离婚、*Sea of Cortez* 合著 → 1942 再婚 Gwyn、*The Moon Is Down* → 1943 战地记者 → 1945 *Cannery Row* → 1947 *The Pearl*、首访苏联（与 Robert Capa）→ 1948 Ricketts 车祸去世、离婚、当选艺术文学院 → 1950 三婚 Elaine → 1952 *East of Eden*（276 天完成初稿）→ 1955 电影 *East of Eden*（James Dean 首作）→ 1959–60 萨默塞特研究亚瑟王 → 1960 *Travels with Charley* 之旅 → 1961 *The Winter of Our Discontent*（最后一部长篇）→ 1962-10-25 诺奖（争议巨大，本人答「Frankly, no」）→ 1964 总统自由勋章 → 1967 越战报道 → 1968-12-20 逝于纽约 → 1976 遗作《亚瑟王及其高贵骑士的事迹》出版。
- 斯德哥尔摩受奖演说（page.md 有英文原文，可引用）："the writer is delegated to declare and to celebrate man's proven capacity for greatness of heart and spirit..."（作家受命宣告并礼赞人类伟大心灵与精神的已证能力）。

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | social realism | 社会现实主义 | 大萧条与流动劳工题材，诺奖理由核心 | 核心贡献页 |
| 1 | regional fiction | 加州地域文学 | 萨利纳斯谷/蒙特雷「Steinbeck Country」 | 地域页 |
| 2 | epic novel | 家族史诗长篇 | *East of Eden* 圣经双线家族叙事 | 长篇页 |
| 3 | novella | 中篇小说 | *Of Mice and Men*/*The Pearl*/*The Red Pony* | 中篇页 |
| 4 | travel literature | 游记文学 | *Travels with Charley*/*Sea of Cortez* | 游记页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Carol Henning | 无向 | 第一任妻子，1930 结婚 1941-1943 离异，*Cannery Row* Mary Talbot 原型 |
| spouse | Gwyn Conger | 无向 | 第二任妻子，1943 结婚 1948 离异，二子 Thom 与 John IV |
| spouse | Elaine Scott | 无向 | 第三任妻子，1950 结婚直至 1968 去世 |
| influence | Ed Ricketts | 对方→本人 | 海洋生物学家挚友与导师，合著 *Sea of Cortez*，「Doc」原型，1948 车祸去世 |
| influence | Lincoln Steffens | 对方→本人 | 激进派作家，page.md 明载曾为其导师 |
| colleague | Arthur Miller | 无向 | 密友，1957 美国众院非美活动委员会听证中为其担当风险声援 |
| colleague | Robert Capa | 无向 | 1947 同访苏联，*A Russian Journal* 由其配图 |
| colleague | Robinson Jeffers | 无向 | 加州邻居、相识的现代主义诗人 |
| colleague | Jack Rudloe | 本人→对方 | 1962 起提携的年轻作家与博物学家，通信至去世 |
| parent-child | Thomas Steinbeck | 本人→对方 | 长子（1944–2016），作家 |
| parent-child | John Steinbeck IV | 本人→对方 | 次子（1946–1991），战地记者 |

入库：`MySQL/seed_person.py data/John_Steinbeck.yaml`（幂等，QID 匹配）。

### 第 5 步：配色方案

- 主色：蓝灰 `#37474F`（尘暴天空与 Monterey 雾色）；辅助：诺奖香槟金 `C9A227`。
- badgeA 社会现实主义 — 锈红 `#9A4A2E`；badgeB 地域文学 — 麦金 `#C9A227` 同系深值 `#8F7420`；badgeC 家族史诗 — 靛蓝 `#2C4A6E`；badgeD 中篇/游记 — 灰绿 `#4E6E5E`。
- 背景母题：尘土颗粒渐远、公路透视线、海浪曲线三选一混排（低饱和）。

### 5.1 格式硬要求 【★ 必须满足】

1. 封面右上角肖像 + 细边框 + 姓名小字注；顶部/底部明示国籍（United States）。
2. **身份信息页**：封面之后、核心贡献之前，左头像右信息网格（生卒/国籍/教育/三次婚姻/记者经历/主要荣誉/核心领域）。
3. 结尾页品牌统一 `OpenMathAI`；引号用半角 `" "`。
4. 名句引文框替代公式框：1962 斯德哥尔摩受奖演说句（page.md 有英文原文）。

### 第 6 步：幻灯片序列（14 页）

```
00 OpenLiterature 项目首页（共享封面 \input）
01 封面 — 美国文学的巨人 / John Steinbeck 1902–1968 + 四色 badge + 右上头像 + 国籍行
02 身份信息页（★ 必做）
03 核心贡献概览 — 社会现实主义 / 加州地域 / 史诗长篇 / 中篇与游记
04 萨利纳斯少年（1902–1925）— 蒙特雷县司库之子、斯坦福辍学、Spreckels 甜菜田劳工
05 漂泊与起步（1925–1935）— 纽约退稿、太浩湖、*Cup of Gold*、*Tortilla Flat* 破局
06 Ricketts 与 Monterey（1930–1948）— 海洋生物学挚友、生态哲学、Doc 原型、*Sea of Cortez*
07 尘暴三部曲（1936–1939）— *In Dubious Battle*/*Of Mice and Men*/*The Grapes of Wrath*（引文框）
08 《愤怒的葡萄》专页 — 乔德一家、禁书风波、国家图书奖+普利策、*New York Times* 1939 畅销榜首
09 战争与好莱坞（1942–1952）— 战地记者、*The Moon Is Down*、挪威自由十字、*The Pearl*、*Viva Zapata!*
10 《伊甸之东》专页 — 276 天初稿、本人 magnum opus、1955 电影与 James Dean
11 最后一程（1959–1968）— 亚瑟王遗作、*Travels with Charley*、*The Winter of Our Discontent*
12 诺奖 1962 — 争议与受奖演说（引文框）、总统自由勋章 1964
13 遗产 — 被禁又被必读、Cannery Row 街名、National Steinbeck Center、Steinbeck Country
14 结尾
```

### 第 7–8 步：Beamer 源码与布局检查

- 每页 `\newcommand{\xxxslide}` 定义；骨架复用 Kenneth_G_Wilson_zh.tex。
- 每写完一页 `latexmk -c` 清理后 `make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查

**Steinbeck 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 学历 | 斯坦福 1919–1925 辍学无学位，勿写「斯坦福毕业」 |
| magnum opus | 本人视 *East of Eden* 为毕生之书；外界通行以 *The Grapes of Wrath* 为 masterpiece——两说并存，页面上分开表述勿合并 |
| 诺奖争议 | 1962 授奖遭《纽约时报》与瑞典媒体讥评；2012 解密档案称其为「折中选择」；本人当记者问是否配得上时答「Frankly, no」——引用保持客观，不加褒贬 |
| Ricketts 身份 | 海洋生物学家、挚友兼「导师」（非学术博士导师），合作 *Sea of Cortez*（1941）含 Ricketts 笔迹；1951 版 *The Log* 仅署 Steinbeck 名 |
| 婚姻时间线 | Carol 1930–1941 分居/1943 离异（两说以 page.md 各处原句为准，写「1930 结婚、1940s 初离异」）；Gwyn 1943–1948；Elaine 1950–1968 |
| 禁书 | Kern County 1939-08 禁 *The Grapes of Wrath* 至 1941-01；1990–2004 被列为美国十大最常被禁作家之一 |
| 越战立场 | 1967 赴越报道、持鹰派立场遭《纽约邮报》抨击——只客观陈述，不作政治评价、不展开政治叙事 |
| 政治红线 | 左翼交往/签署信件/CIA 档案/FBI 盯梢等：只按 page.md 客观简述一句，不作政治评价 |
| 遗作 | 《亚瑟王及其高贵骑士的事迹》1976 遗作出版，未完成——勿写成生前完成 |
| 房车名 | Rocinante 取自堂吉诃德坐骑，游记与国家斯坦贝克中心展品 |
| 无载禁写 | 与 Hemingway/Faulkner 仅是受访时提及的喜爱作家（「Hemingway 的短篇与 Faulkner 几乎所有作品」），可作引语不可建 influence 关系；不给子女以外亲属编造关系 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| The Grapes of Wrath | 《愤怒的葡萄》 | 题名出自《共和国战歌》 |
| Of Mice and Men | 《人鼠之间》 | 中篇+舞台剧+三版电影 |
| East of Eden | 《伊甸之东》 | 萨利纳斯谷家族史诗 |
| Cannery Row | 《罐头厂街》 | 街名 1958 因小说改名 |
| Dust Bowl | 尘暴区/尘盆 | 三部曲历史背景 |
| Tortilla Flat | 《煎饼坪》 | 首个商业成功 |
| Travels with Charley | 《与查理同行》 | 1960 房车游记 |
| Rocinante | 罗西南特 | 房车名，堂吉诃德坐骑 |
| sympathetic humour | 同情的幽默 | 诺奖理由核心词组 |
| keen social perception | 敏锐的社会洞察 | 诺奖理由核心词组 |
| Sea of Cortez | 《科尔特斯海》 | 与 Ricketts 合著 |
| Harvest Gypsies | 《丰收吉普赛人》 | 1936 报道系列 |

---

## 四、背景音乐建议

- **选定曲目**：**New Lands**（分批文件预分配）。
- **匹配理由**：「新大陆/开拓」气质匹配斯坦贝克横穿美国的公路叙事与加州边疆移民史；开阔的推进感贴合 *Travels with Charley* 与尘暴西迁的地理纵深。
- **备选**（未采用）：Expedition（同为公路感但偏冒险）、The Flow of Time（时间感强但缺开阔感）。
- **本地路径**：按 `music_audio/curated_tracks.md` 索引拷贝至 `presentations/20th_century/John_Steinbeck/New Lands.wav`。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/John_Steinbeck/page.md` | 事实基准（唯一来源） |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 名录与中译理由 |
| `MySQL/data/John_Steinbeck.yaml` | 入库 yaml（本提示词第 4/4.5 步落地） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
