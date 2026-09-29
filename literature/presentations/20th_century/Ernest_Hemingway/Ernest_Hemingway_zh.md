# 文学家立传提示词（Ernest Hemingway / 欧内斯特·海明威）

> **OpenLiterature** 诺贝尔文学奖得主「人物专属立传提示词」，结构对齐 OpenPhysicist 标杆 Kenneth_G_Wilson_zh.md。
> 适配要点：文学家无公式框——用**名句引文框 / 意象图式 / 代表作书影**替代；核心页为「文学领域表」。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Ernest Miller Hemingway（欧内斯特·海明威），美国小说家/短篇作家/记者，1954 年诺贝尔文学奖得主。
- **设计哲学**：保留「身份信息页 + 研究领域结构化」骨架，叙事重心放在**冰山理论与"迷惘的一代"文风革命**上——以极简句法支撑人物命运的重量。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Ernest Miller Hemingway（1899-07-21 ~ 1961-07-02，享年 61 岁）
- **诺奖年份**：1954 年诺贝尔文学奖，官方获奖理由（EN 原文，禁止改写）：
  > "for his mastery of the art of narrative, most recently demonstrated in The Old Man and the Sea, and for the influence that he has exerted on contemporary style"
  > （中译：表彰其叙事艺术的精湛，近作《老人与海》尤为明证；并表彰其对当代文风的影响）
- **气质关键词**：**冰山理论的锻造者、迷惘的一代代言人、冒险生活的人格化**
- **设计母题**：**八分之七在水下（the iceberg）**——以"水面线 + 上小下大的冰山剖面"意象图式呼应冰山理论：文字露出水面八分之一，结构沉在水下。
- **本地数据源**：`literature/presentations/pages/20th_century/Ernest_Hemingway/page.md`（+ metadata.json、images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Ernest_Hemingway
- **肖像**：第 0 步待下载（1939 年照片，见 infobox）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1899-07-21 生于伊利诺伊州橡树园（Oak Park，芝加哥西郊）~ 1961-07-02 逝于爱达荷州凯彻姆（Ketchum），享年 61 岁；1961-07-02 在凯彻姆寓所自杀身亡（page.md 明载，客观陈述）。
- 国籍：美国。
- 家庭：父 Clarence Edmonds Hemingway（医生）；母 Grace Hall Hemingway（音乐家）；兄妹六人排行第二。四任妻子：Hadley Richardson（1921–1927）、Pauline Pfeiffer（1927–1940）、Martha Gellhorn（1940–1945）、Mary Welsh（1946–1961）。三子：Jack（"Bumby"，1923）、Patrick、Gloria。
- 教育：Oak Park and River Forest High School（1913–1917，校报/年刊编辑，笔名仿 Ring Lardner）。
- 关键荣誉：诺贝尔文学奖 1954；普利策小说奖 1953（《The Old Man and the Sea》）；意大利银质英勇勋章（1918）与战争功绩十字；Bronze Star Medal。
- 核心作品与贡献（4–6 条）：
  1. 《Three Stories and Ten Poems》（1923，巴黎首部）与《In Our Time》（1925，美国版短篇集）；
  2. 《The Sun Also Rises》（1926）——"迷惘的一代"代表作，常被评为其最伟大作品；
  3. 《A Farewell to Arms》（1929）——一战经历的小说化；
  4. 《Death in the Afternoon》（1932，非虚构斗牛）与西班牙内战报道 → 《For Whom the Bell Tolls》（1940，写于哈瓦那）；
  5. 《The Old Man and the Sea》（1952）——普利策奖与诺奖直接推手；
  6. **冰山理论（iceberg theory / theory of omission）**——"事实浮出水面，支撑结构与象征沉在水下"（page.md 明载此定义，可引）；《堪萨斯城星报》风格指南（短句、短段、有力英文）为其文体基础。
- 关键时间线（15–20 节点）：
  1. 1899 生于橡树园；密歇根 Walloon Lake 夏令营学狩猎垂钓；
  2. 1917 高中毕业 →《堪萨斯城星报》见习记者六个月（文体基础）；
  3. 1918-05 赴意大利前线，红十字救护车司机；1918-07-08 Fossalta di Piave 迫击炮重伤（双腿弹片），救运伤员获意大利银质英勇勋章；
  4. 1918–19 米兰医院养伤；恋 Agnes von Kurowsky，1919-03 被其诀别（"弃人者先弃"模式的起点，按传记转述）；
  5. 1920 芝加哥任《Cooperative Commonwealth》副编辑，遇 Sherwood Anderson；
  6. 1921-09-03 娶 Hadley Richardson；经 Anderson 建议并写介绍信赴巴黎，任《多伦多星报》驻外记者；
  7. 1922-12 Hadley 在里昂车站丢失手稿箱（几乎全部早期作品散佚）；
  8. 1923 首书《Three Stories and Ten Poems》；长子 Jack 生；
  9. 1923–25 遇 Gertrude Stein（导师、Jack 教母）、Ezra Pound（1922 偶遇，强力提携）、James Joyce；1925 遇 F. Scott Fitzgerald；
  10. 1925-07 庞普洛纳奔牛节 → 动笔《The Sun Also Rises》（8 周完稿）；
  11. 1926-10 《The Sun Also Rises》由 Scribner's 出版；
  12. 1927 与 Hadley 离异、娶 Pauline Pfeiffer；1928 定居 Key West；
  13. 1929 《A Farewell to Arms》；
  14. 1932 《Death in the Afternoon》；
  15. 1937 赴西班牙报道内战；
  16. 1940 《For Whom the Bell Tolls》（哈瓦那写成）；同年娶 Martha Gellhorn；
  17. 1944 二战随盟军报道诺曼底登陆与巴黎解放；1946 娶 Mary Welsh；
  18. 1952 《The Old Man and the Sea》 → 1953 普利策奖；
  19. 1954 两度坠机重伤（非洲之旅）；1954 获诺贝尔文学奖；
  20. 1961-07-02 卒于凯彻姆。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | iceberg theory | 冰山理论 | 省略法：事实在水上，结构在水下（官方理由"影响当代文风"核心） | 核心页 |
| 1 | modernist fiction | 现代主义小说 | "迷惘的一代"巴黎现代主义圈 | 核心页 |
| 2 | war novel | 战争小说 | 《永别了武器》《丧钟为谁而鸣》 | 战争页 |
| 3 | short story | 短篇小说 | 六部短篇集；先以短篇练出"以少胜多" | 短篇页 |
| 4 | war correspondence | 战地报道 | 西班牙内战、二战诺曼底/巴黎解放 | 记者页 |

#### 4.1 入库操作

- 新建 `people` 记录（name_en=`Ernest Hemingway`，qid=Q23434），`primary_occupation='writer'`、`has_social_data=1`
- occupations：writer(0)、novelist(1)、journalist(2)
- 5 个领域写入 `person_field`（iceberg theory / war novel 等缺失字典项先补建）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

> 只收 page.md 明载关系。Agnes von Kurowsky 为恋爱关系非婚姻，不入 spouse（需时可 controversy/无——本批不入，仅提示词呈现）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Hadley Richardson | 无向 | 第一任（1921–1927），巴黎岁月伴侣 |
| spouse | Pauline Pfeiffer | 无向 | 第二任（1927–1940） |
| spouse | Martha Gellhorn | 无向 | 第三任（1940–1945），战地记者 |
| spouse | Mary Welsh | 无向 | 第四任（1946–1961） |
| parent-child | Clarence Edmonds Hemingway | 对方→本人 | 父，医生 |
| parent-child | Grace Hall Hemingway | 对方→本人 | 母，音乐家 |
| parent-child | Jack Hemingway | 本人→对方 | 长子（"Bumby"，1923） |
| parent-child | Patrick Hemingway | 本人→对方 | 子 |
| parent-child | Gloria Hemingway | 本人→对方 | 子 |
| influence | Gertrude Stein | 对方→本人 | 巴黎时期导师（mentor）、现代主义堡垒 |
| influence | Ezra Pound | 对方→本人 | 1922 偶遇后提携其早期创作 |
| colleague | F. Scott Fitzgerald | 无向 | 1925 年起的"admiration and hostility"之谊 |
| colleague | Sherwood Anderson | 无向 | 建议赴巴黎并写介绍信 |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#5C3A1E`（深褐——皮革、斗牛场与海明威式的粗粝）
- **辅助**：诺奖香槟金 `#C9A227`
- badge 四分类：badgeIceberg 靛蓝 `#4C5FD5`；badgeWar 青绿 `#0E7C7B`；badgeParis 琥珀 `#E07B30`；badgeSea 玫瑰 `#C4204F`
- **背景母题**：冰山剖面（水面线横贯版面，水下大面积深色）

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 冰山之下 / Ernest Hemingway 1899–1961 + badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/四任妻子/荣誉/核心领域）
03  核心创作概览 — 冰山理论 / 迷惘的一代 / 战争小说 / 短篇与报道
04  早年：橡树园与堪萨斯城星报 (1899–1917)【风格指南引文框】
05  一战：意大利前线与重伤 (1918–1919)【意象图式】
06  巴黎：Stein / Pound / Joyce 与手稿之失 (1921–1926)【人物群像】
07  《太阳照常升起》与"迷惘的一代" (1926)【书影】
08  《永别了武器》与西班牙内战 (1929–1940)【书影：For Whom the Bell Tolls】
09  《老人与海》：普利策与诺奖 (1952–1954)【书影+引文框：官方理由】
10  冰山理论——文体革命【图式：水面线】
11  晚年、坠机与凯彻姆 (1954–1961)——自杀按事实一句陈述
12  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式宏名统一；冰山图式可用 tikz 简单三角形+水平线，勿复杂化；身份页 `\profileslide`。
- 陷阱表：

| 陷阱 | 说明 |
|------|------|
| 死因 | "died by suicide"（1961-07-02 凯彻姆）——一句客观陈述，勿渲染细节 |
| 四任妻子年份 | 1921–27 / 1927–40 / 1940–45 / 1946 起，勿错位；Gloria 出生于 Pauline 婚内（1931）|
| 《太阳照常升起》定性 | "recognized as Hemingway's greatest work"是评论转述，可注明"评论界"；"迷惘的一代"一词 Stein 首创、Hemingway 以本书推广（page.md 明载）|
| 冰山理论 | page.md 原文定义"the facts float above water; the supporting structure and symbolism operate out of sight"——可引英文；别名 theory of omission |
| 引语红线 | 传记转述（Meyers/Kert/Baker 等）须标"据传记家 XX"，勿作本人原话 |
| 星报风格指南 | "Use short sentences. Use short first paragraphs. Use vigorous English. Be positive, not negative."——page.md 载原文，可引 |
| 军衔 | 意大利陆军中尉/少尉与 A.R.C. 军衔并存但"从未在美国军队授衔"（page.md 明载），勿写"美军军官" |
| 诺奖理由 | 官方句含《老人与海》与"对当代文风的影响"两部分，勿只引前半 |
| 坠机年份 | 1954 年非洲两度坠机（获诺奖同年），勿写成 1953 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| iceberg theory | 冰山理论 | 亦称 theory of omission（省略法） |
| Lost Generation | 迷惘的一代 | Stein 首创、本书推广 |
| The Sun Also Rises | 太阳照常升起 | 1926 |
| A Farewell to Arms | 永别了，武器 | 1929 |
| For Whom the Bell Tolls | 丧钟为谁而鸣 | 1940，西班牙内战 |
| The Old Man and the Sea | 老人与海 | 1952，普利策 1953 |
| Fossalta di Piave | 皮亚韦河畔福萨尔塔 | 1918 受伤地 |
| corrida | 斗牛 | Pamplona 奔牛节起 fascination |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions
- **匹配理由**：Expedition 的"远征感"匹配海明威一生跨越意大利前线、巴黎、西班牙、古巴、非洲的地理半径；节奏明快中的粗粝感匹配其户外冒险人格与简洁文风。
- **本地路径**：`music_audio/alex-productions/` 下 Expedition 对应 wav → `presentations/20th_century/Ernest_Hemingway/Expedition.wav`（对照 `curated_tracks.md` 取实际文件名）。

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Ernest_Hemingway/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Ernest_Hemingway/images.txt` | 肖像/插图 URL 清单（1939 年照片） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 总名录（官方理由中译） |
| `literature/generate_20th_century_list.py` | `CITATION_ZH`（获奖理由取用，禁止改写该脚本） |
| `MySQL/data/Ernest_Hemingway.yaml` | 社会关系入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库（Expedition 实际文件名） |

## 六、执行清单 【模板通用，逐项打勾】

1. ☐ 第 0 步：核对 page.md 事实基准 + 下载肖像（infobox 1939 年照片，curl -A "Mozilla/5.0" + file 验证；404 则按 Wikipedia REST API / Special:FilePath 回退，仍失败用装饰圆占位）
2. ☐ 第 1 步：建目录 `Ernest_Hemingway/images/`
3. ☐ 第 2 步：复制 Makefile，设 `MAIN=Ernest_Hemingway_zh`、`VIDEO_NAME=Ernest_Hemingway_zh`
4. ☐ 第 3 步：复制 Expedition.wav（对照 curated_tracks.md 文件名）
5. ☐ 第 4 步：yaml 入库（fields≥4、relations≥2，已完成）
6. ☐ 第 5 步：按配色写 tex 头部宏（mainclr=#5C3A1E）
7. ☐ 第 6 步：逐页写 slide → 逐页 make → pdftoppm 截图检查
8. ☐ 第 7 步：0 error、vbox≤10pt、hbox≤50pt 达标
9. ☐ 第 8 步：逐页目检（人物/年份/书名拼写；引语归属复核）
10. ☐ 第 9 步：make images + make video（mp4）→ 汇报

> **开始执行。每完成一步汇报。最重要的事：逐页 make，看到溢出就修。**
