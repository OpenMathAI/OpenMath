# 人道主义者立传提示词（OpenPeace 批次 10 实例：Albert Schweitzer）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Albert Schweitzer（1952 诺贝尔和平奖，兰巴雷内医院创办人、「敬畏生命」哲学者）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享体系，与 OpenPhysicist / OpenMedic 平级）。
- **本实例**：Ludwig Philipp Albert Schweitzer（路德维希·菲利普·阿尔贝特·施韦泽，OM）—— 阿尔萨斯出身的通才：神学家、管风琴家、音乐学家、哲学家、医生、人道主义者。
- **设计哲学**：和平奖得主（通才/人道主义者类）与科学家立传的核心差异，在于必须有「身份信息页」，且叙事重心是「**四重身份的一根主线**」——神学（历史耶稣研究）、音乐（巴赫）、哲学（敬畏生命）、医学（兰巴雷内）最终汇入和平主义（反核）一条河；「研究领域」用「事业领域」结构化表达，务必保留骨架。

---

## 二、背景信息 【人物专属】

- **目标人物**：Albert Schweitzer（1875-01-14 生于阿尔萨斯-洛林凯瑟斯贝格（时属德意志帝国）~ 1965-09-04 卒于加蓬兰巴雷内，享年 90 岁；国籍 1919 年前德国、1919 年起法国——名录口径 France）
- **气质关键词**：**「敬畏生命」的哲人、兰巴雷内的丛林医生、巴赫的诠释者、反核的良心**
- **诺奖**：1952 诺贝尔和平奖，获奖理由（Nobel 官方英文原文照抄）：
  > "for his altruism, reverence for life, and tireless humanitarian work which has helped making the idea of brotherhood between men and nations a living one."（表彰他的利他主义、敬畏生命的精神与不知疲倦的人道主义工作，使人人与国国之间手足情谊的理念成为现实）
- **设计母题**：**管风琴与十字木（organ & crosswood）**。巴赫管风琴声与兰巴雷内手制十字架墓标——欧洲文明之声与丛林行医之地在同一人身上交汇；视觉语言采用管风琴音管、河流（奥果韦河）、棕榈与十字轮廓；柔和圆点背景呼应「生命意志之间彼此敬畏」的哲学底色。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Albert_Schweitzer/page.md`
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报。数据库同步要求：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库。

### 第 0 步：事实基准（第一轮已核对，勿改） 【人物专属】

- 生卒：1875-01-14 生于 Kaysersberg（Alsace-Lorraine，德意志帝国）~ 1965-09-04 卒于兰巴雷内（今加蓬），享年 90 岁；墓在奥果韦河畔，墓标十字架为其亲手所制
- 国籍：德国（至 1919）→ 法国（1919 年起，阿尔萨斯回归法国时恢复父母的战前法国国籍）；童年 Gunsbach（父为当地 EPCAAL 路德-福音派牧师）
- 家庭：父 Louis Théophile Schweitzer（牧师）、母 Adèle（née Schillinger）；堂姐 Anne-Marie Schweitzer Sartre 是让-保罗·萨特之母
- 教育：Mulhouse 文理中学 Abitur 1893 → 管风琴师从 Eugène Munch（1885–1893）→ 1893 巴黎为 Widor 演奏获免费收徒 → 斯特拉斯堡新教神学（1893 起，兼从 Gustav Jacobsthal 学钢琴与对位）→ 1894 义务兵役 → 1898–1899 巴黎索邦（康德宗教哲学博士论文）+ 师从 Marie Jaëll → 1899 柏林大学夏季学期 → 1899 图宾根出版博士论文、获斯特拉斯堡神学学位 → 1905 起斯特拉斯堡学医，MD 1913
- 任职（含年份）：1899 圣尼古拉教堂执事 → 1900 授神职（神学执照完成）→ 1902 圣托马斯神学院代理院长（1903 转正）→ 1905-01-06 布道后决意赴非行医 → 巴黎巴赫学会六位创办人之一（1905，与 Widor；至 1913 常任管风琴）→ 1913 与妻赴兰巴雷内建医院（Hôpital Albert Schweitzer）→ 一战中被法国军方监视，1917 送押 Bordeaux（Garaison，后 Saint-Rémy-de-Provence），1918-07 获释并恢复法国籍 → 战后 Strasbourg 行医兼助理牧师、开演奏会筹款 → 1922 牛津 Dale Memorial Lectures（成书《文明的衰败与重建》《文明与伦理》）→ 1924 携 Noel Gillespie 重返非洲 → 1927、1929–1932、1935 多轮往返 → 1937-01 起长驻兰巴雷内贯穿二战 → 1934–1935 爱丁堡 Gifford Lectures → 1948 战后首返欧洲
- 关键荣誉：1952 诺贝尔和平奖（获奖演说 *The Problem of Peace*，1954-11-04；3.3 万美元奖金全数建兰巴雷内麻风病院）；1928 歌德奖；1959 James Cook Medal；1955 伊丽莎白二世授名誉功绩勋章（OM）；荣誉军团勋章多级；Pour le Mérite；德意志书商和平奖等（frontmatter 长表可择要）
- 配偶：Helene Bresslau（犹太泛德意志史学家 Harry Bresslau 之女，孤儿院督察；1912-06 结婚；兰巴雷内手术麻醉师；1923 后因健康移居欧洲，1957 去世）；女 Rhena Schweitzer Miller
- 核心事业清单：①历史耶稣研究（《耶稣生平研究史》1906、彻底末世论立场）②保罗神学（《保罗的神秘主义》1931，「在基督里」首要论）③巴赫诠释与管风琴改革运动（*J. S. Bach* 1905/1908、1906 小册子启动 Orgelbewegung、国际管风琴制造规则）④「敬畏生命」哲学（*Civilization and Ethics* 1923；自认其最重要的遗产）⑤兰巴雷内医院（1913–1965，麻风、昏睡病、疟疾等热带病诊疗）⑥反核运动（1952 起与 Einstein、Hahn、Russell 同行；1957-04-23 「Declaration of Conscience」广播；1957/1958 Radio Oslo 四篇演讲成书 *Peace or Atomic War*；1957 参与 SANE 委员会创立）
- 关键时间线（18 节点）：1875 Kaysersberg 生 / 1893 Abitur + 为 Widor 演奏 / 1899 博士论文（图宾根）+ 神学学位 + 执事 / 1900 授神职 / 1902 圣托马斯神学院代理院长 / 1905 决意赴非 + 巴黎巴赫学会创办 + 《J. S. Bach》出版 / 1906 《耶稣生平研究史》+ 管风琴小册子 / 1908 德文版 *J. S. Bach* 两卷 / 1912-06 与 Helene 结婚 / 1913 MD + 赴兰巴雷内 / 1917–1918 法国拘押、恢复法国籍 / 1922 Dale 讲座 / 1923 《文明与伦理》（敬畏生命哲学成书）/ 1924 重返非洲 / 1937–1945 长驻兰巴雷内贯穿二战 / 1948 战后首返欧洲 / 1952 诺贝尔和平奖（1954-11-04 演说、奖金建麻风病院）/ 1957 反核广播 + SANE 创立 / 1965-09-04 卒于兰巴雷内

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/Albert_Schweitzer/` 下建 `images/`；Makefile 设 `MAIN=Albert_Schweitzer_zh`、`VIDEO_NAME=Albert_Schweitzer_zh`
- 肖像：正文图有 1912 年 Émile Schneider 油画肖像（斯特拉斯堡现当代艺术博物馆藏）、1955 年正装照片——优先 1955 照片（经 Wikipedia REST API 查 infobox 原图名下载），油画作备选；404 则装饰圆占位并核对图注

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | medicine | 医学 | 兰巴雷内热带病行医 MD 1913 | 医学页 |
| 1 | theology | 神学 | 历史耶稣研究、保罗神秘主义 | 神学页 |
| 2 | musicology | 音乐学 | 巴赫诠释、管风琴改革运动 | 音乐页 |
| 3 | philosophy | 哲学 | 「敬畏生命」（Ehrfurcht vor dem Leben） | 哲学页 |
| 4 | medical missions | 医疗传道 | 1913–1965 非洲医院与麻风病院 | 医院页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Theobald Ziegler | 师→生 | 博士导师（infobox Doctoral advisor） |
| advisor-student | Heinrich Julius Holtzmann | 师→生 | 其他学术导师（新约神学） |
| advisor-student | Robert Wollenberg | 师→生 | 其他学术导师（医学） |
| advisor-student | Hans Münch | 生→师 | 学生，指挥家兼作曲家 |
| influence | Eugène Munch | 无向 | 早年管风琴老师（1885–1893），引其热爱瓦格纳与巴赫 |
| colleague | Charles-Marie Widor | 无向 | 管风琴恩师（免费收徒）、巴黎巴赫学会共同创办人、合作出版巴赫管风琴全集 |
| spouse | Helene Bresslau Schweitzer | 无向 | 1912-06 结婚，1913 同赴兰巴雷内任手术麻醉师，1957 去世 |
| parent-child | Louis Théophile Schweitzer | 子→父 | 父亲，Gunsbach 路德-福音派牧师 |
| parent-child | Adèle Schillinger | 子→母 | 母亲 |
| parent-child | Rhena Schweitzer Miller | 父→子 | 女儿 |
| colleague | Albert Einstein | 无向 | 1952 起共同致力于反对核试验与核武器 |
| colleague | Otto Hahn | 无向 | 1952 起共同致力于反对核试验与核武器 |
| colleague | Bertrand Russell | 无向 | 1952 起共同致力于反对核试验与核武器 |

- 方向约定：advisor-student 有向（direction: advisor / student），parent-child 用 direction: parent / child，influence 与其余无向（seed 幂等归一 from<to）
- 不入库（无类型可归或仅事件性）：Cosima Wagner（朋友与通信者）、Ernest Newman（英译者）、Clara Faisst（通信作曲家）、Donald Tovey（题献者）、Noel Gillespie（助理志愿者）、James Cameron / Chinua Achebe / John Gunther / Edgar Berman（批评与传记作者，争议叙事页呈现）、Jean-Paul Sartre（堂甥，无姨表类型）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：欧洲的深邃、丛林的热忱、良知的清澈
- **配色**：主色深紫 `#372A75`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeLife` 敬畏生命 — 香槟金 `#C9A227`
  - `badgeMed` 兰巴雷内 — 深紫 `#372A75`
  - `badgeBach` 巴赫与管风琴 — 靛 `#4C5FD5`
  - `badgeNuke` 反核良知 — 琥珀 `#E07B30`
- **背景母题**：柔和圆点，疏朗澄澈，呼应音管林立与热带树冠交叠的「两个世界一人担」意象

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）；2. 封面明示国籍与 `国籍 | 机构 | 主要奖项` 状态栏；3. **必须有身份信息页**（左头像 + 右信息网格：生卒、本名、国籍、出生地、教育、任职、荣誉、核心事业）；4. 品牌口径统一 `OpenMathAI`，引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，16 页规划】

```
00  OpenPeace 项目首页（\input cover 封面）
01  封面 — 敬畏生命 / Albert Schweitzer 1875–1965 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  事业概览 — 医学 / 神学 / 音乐学 / 哲学 / 医疗传道
04  阿尔萨斯少年 (1875–1893) — Kaysersberg、Gunsbach 牧师之家、宗教宽容环境、Mulhouse 与 Munch
05  Widor 门下 (1893–1899) — 巴黎免费收徒、索邦康德论文、图宾根出版、神学学位
06  神学家与巴赫诠释者 (1899–1906) — 圣尼古拉执事、圣托马斯神学院、《J. S. Bach》、《耶稣生平研究史》（核心页之一）
07  管风琴改革运动 — 1906 小册子、维也纳报告、国际管风琴制造规则、巴黎巴赫学会
08  转身：三十岁学医 (1905–1913) — 1905-01-06 布道、医学博士 1913、Helene 与婚礼
09  兰巴雷内医院 (1913–1917) — 奥果韦河 14 天木筏、首批 2000 病人、铁皮医院、一战监视与拘押（核心页之一）
10  重建与「敬畏生命」(1919–1924) — 演奏筹款、Dale 讲座、《文明与伦理》、1924 重返
11  丛林医院六十年 — 1927/1929/1935/1937 各阶段、贯穿二战、 pedal piano 轶事
12  1952 诺贝尔和平奖 — 理由、The Problem of Peace 演说、奖金建麻风病院（核心页）
13  反核的良心 (1952–1965) — Declaration of Conscience、Radio Oslo 四讲、Peace or Atomic War、与 Einstein/Hahn/Russell 同行
14  争议与自省 — Cameron/Achebe/Gunther 的批评与 Berman 的辩护，父权争议原文并列（客观记录页）
15  遗产：每个人都可以有自己的兰巴雷内 + 结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；每写完一页 `make`，`pdftoppm` 目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Schweitzer 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 国籍口径 | 名录按 Nobel 口径** France**（生于德属阿尔萨斯-洛林，1919 年起法国籍）；身份页与封面写 France，年表可注「德国（至 1919）→法国」变迁，勿写成纯德国人 |
| 诺奖年份 | 1952 年度奖；获奖演说 *The Problem of Peace* 日期 1954-11-04（参考文献口径）；本地页面未载 1953 授奖仪式字样，禁自行写入「1953 年领奖」 |
| 四重身份排序 | 医生/神学家/音乐学家/哲学家并列；「敬畏生命」哲学是他自认最重要的遗产（而非医院——原话 "my own improvisation on the theme of Reverence for Life"），遗产页要按此口径 |
| 殖民争议 | 正文同时载有：1905 布道对殖民暴行的严厉批判 + 第二回忆录对殖民统治的辩护 + "junior brother / elder brother" 言论 + Achebe/Gunther/Cameron 批评 + Berman 辩护——**全部客观并列，禁单侧叙事**；Achebe 引语可引英文原文但须注明是其转述 |
| 神学内容 | 历史耶稣「彻底末世论」与保罗「在基督里」神秘主义按学术立场客观转述；*The Quest* 两段英文原文引语（"He comes to us as One unknown..." 等）是 page.md 明载可引的少数段落；禁加入任何信仰评判 |
| 莱姆病/素食 | 素食问题正文载三说并存（Ratter 1950 / Bentley / Stamos）——按「晚年倾向、学界三说」处理，禁写定论 |
| 反核史实 | 1957-04-23 "Declaration of Conscience"；Radio Oslo 四篇广播（1957/1958）成书 *Peace or Atomic War*；SANE（Committee for a Sane Nuclear Policy）1957 共同创办——三个事实勿混；与 Einstein/Hahn/Russell「共同致力于反核」为正文原句口径，勿扩写成联合组织 |
| 一战拘押 | 1917 送 Bordeaux、先 Garaison 后 Saint-Rémy-de-Provence、1918-07 释放并恢复法国籍——地名顺序勿乱 |
| 录音史 | 1935–1936 Columbia 录音在伦敦 All Hallows 与斯特拉斯堡 Ste Aurélie、Günsbach 教堂录音、"Schweitzer technique" 录音术——择要一句即可，勿喧宾夺主 |
| 同名区分 | 勿与 Hans Münch（其学生、指挥家）混淆于奥斯维辛的臭名同名者；Robert Wollenberg 为 infobox 所列医学导师（红链，无独立条目，note 只写 infobox 口径） |
| 家庭 | 堂姐 Anne-Marie 是萨特之母——冷知识一句即可，禁展开萨特叙事 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Reverence for Life | 敬畏生命 | 德文 Ehrfurcht vor dem Leben，勿译「生命敬畏」 |
| Hôpital Albert Schweitzer | 施韦泽医院（兰巴雷内） | 1913 创办 |
| Lambaréné | 兰巴雷内 | 奥果韦河畔，今加蓬 |
| The Quest of the Historical Jesus | 《耶稣生平研究史》 | 1906，英译名沿用 |
| consistent eschatology | 彻底末世论 | 其历史耶稣研究立场 |
| The Mysticism of Paul the Apostle | 《保罗的神秘主义》 | 1931 |
| Orgelbewegung | 管风琴改革运动 | 1906 小册子启动 |
| Paris Bach Society | 巴黎巴赫学会 | 1905 与 Widor 共同创办 |
| pedal piano | 踏板钢琴 | 赴非特制乐器 |
| The Problem of Peace | 《和平的问题》 | 1954-11-04 诺奖演说 |
| Peace or Atomic War | 《和平还是原子战争》 | 1958 广播演讲结集 |
| Declaration of Conscience | 良知宣言 | 1957-04-23 Radio Oslo |
| leprosarium | 麻风病院 | 诺奖奖金所建 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Timeless** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 沉稳 / 纪录片 / 超越时间
- **匹配理由**: "Timeless"（超越时间）贴合四重身份汇成一生的叙事——神学、音乐、哲学、医学在九十年人生中不分先后地互相成全；"沉稳"匹配丛林医院半个世纪的日常坚韧，"纪录片"匹配 1913–1965 一条河流般的行医长卷。
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → 复制为 `presentations/20th_century/Albert_Schweitzer/Timeless.wav`
- **时长**: 128 秒 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Albert_Schweitzer/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译口径 |
| `MySQL/data/Albert_Schweitzer.yaml` | 入库 yaml（第 4 / 4.5 步落地） |
| `MySQL/seed_person.py` | 幂等入库引擎 |
| `music_audio/curated_tracks.md` | BGM 曲库 |

- **备选** (未采用):
  - ★★ Eternals — 「永恒」匹配敬畏生命哲学的普世性，但偏宏大叙事，弱于丛林行医的日常质感
  - ★ The Flow of Time — 「时间之流」匹配奥果韦河意象与九十年人生，但与管风琴声学的厚重感略隔

---

## 六、数据库落地命令 【模板通用】

- **yaml**: `MySQL/data/Albert_Schweitzer.yaml`（第 4 步事业领域表与第 4.5 步关系表为其唯一事实来源）
- **入库**（幂等；撞 fields/occupations 字典表唯一键时等 2 秒重跑一次）：

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Albert_Schweitzer.yaml
```

- **验证**（要求 `has_social_data=1`、fields≥4、relations≥2）：

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 -c "
from db_mysql import get_conn
conn=get_conn(); cur=conn.cursor()
cur.execute(\"SELECT id,name_en,has_social_data FROM people WHERE qid='Q49325'\")
p=cur.fetchone(); print(p)
cur.execute('SELECT COUNT(*) FROM person_field WHERE person_id=%s',(p[0],)); print('fields:',cur.fetchone()[0])
cur.execute('SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s',(p[0],p[0])); print('relations:',cur.fetchone()[0])"
```

- **本实例参考值**: 已入库 id=7302，fields=5，relations=13（导师 3 + 学生 1 + influence 1 + colleague 4 + spouse 1 + 父母 2 + 女儿 1）；`Albert Einstein`（id=349）、`Bertrand Russell`（id=74）、`Otto Hahn`（id=2055）均沿用库内既有记录，零分裂。
- **注意事项**: nationalities 按 Nobel 口径 France rank 0（era_note 1919 年起）+ Germany rank 1（era_note 1919 年前）；`Robert Wollenberg` 为 infobox 红链人物，stub note 只写「其他学术导师（医学）」口径，勿补外部生平。

> **开始执行。每完成一步汇报。**
> **最重要的事：殖民与种族争议全客观并列禁单侧；每写一页就 make，看到溢出就修。**
