# 文学家立传提示词（OpenLiterature 实例：Thomas Mann）

> 本文件是 OpenLiterature 的「文学家立传提示词」人物专属实例，以 Thomas Mann（1929 诺贝尔文学奖，德语小说大师）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；文学家适配：无公式框，以**代表作书影 / 名句引文框 / 意象图式**替代。
> 政治红线：纳粹迫害与流亡只按 page.md 客观事实简述，**不作政治评价、不展开政治叙事**。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Paul Thomas Mann（托马斯·曼）。
- **设计哲学**：保留「身份信息页」骨架；以**文学领域表**替代研究领域表、以**引文框/书影/意象图式**替代公式框。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Thomas Mann（1875-06-06 ~ 1955-08-12，享年 80 岁）
- **气质关键词**：**市民阶层的史诗画家、讽刺的庄重者、流亡的良心** —— 1929 诺贝尔文学奖获奖理由：
  > "principally for his great novel, Buddenbrooks, which has won steadily increased recognition as one of the classic works of contemporary literature"
  > （官方中译，照 `literature/generate_20th_century_list.py` CITATION_ZH，禁止改写）：主要表彰其伟大小说《布登勃洛克一家》，该书已被稳步公认为当代文学的经典之作
  > 注：page.md 正文未载英文 citation 整句，EN 以 Nobel 官方口径为准、中译照 CITATION_ZH，禁止改写
- **设计母题**：**商行的沉船与魔山**。吕贝克商行账本的衰变曲线（Buddenbrooks 四代家道中落）+ 海拔高处与世隔绝的疗养院阳台（The Magic Mountain）——背景母题用雪山上俯瞰平原的暖色窗光与账本纹样叠加，呼应「艺术家与市民生活的相互关系」。
- **本地数据源**：`literature/presentations/pages/20th_century/Thomas_Mann/page.md`（Wikipedia 全文，事实基准已核对；正文体量大，采信前须复核行号）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Thomas_Mann
- **肖像**：第 0 步待下载（1929 年获奖时像，images.txt 有线索）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（人物专属，第一轮已核对）

- 生卒：1875-06-06 生于吕贝克自由市（汉萨贵族市民阶层）～ 1955-08-12 逝于苏黎世（误诊血栓性静脉炎，尸检实为髂动脉瘤破裂），享年 80 岁；葬于 Kilchberg 村墓园
- 国籍/公民权变迁（按 page.md 分条）：德国（至 1936）→ 捷克斯洛伐克（1936–1944）→ 美国（1944-06-23 入籍）
- 家庭：父 Thomas Johann Heinrich Mann（参议员兼粮食商人，1891 年去世后商行清算）；母 Júlia da Silva Bruhns（巴西裔）；兄 Heinrich Mann（小说家）；妻 Katia Pringsheim（1905 年结婚，富裕世俗犹太实业家家庭）；六子女 Erika(1905)/Klaus(1906)/Golo(1909)/Monika(1910)/Elisabeth(1918)/Michael(1919)，其中 Erika/Klaus/Golo 三人亦成重要作家
- 教育：吕贝克 Katharineum（先理科）→ 慕尼黑大学与慕尼黑工业大学（为记者生涯修历史/经济/艺术史/文学，无学位）
- 任职/流亡：慕尼黑 1891–1933（1894–95 南德火灾保险公司职员；为 *Simplicissimus* 撰稿）；1933 年希特勒上台时在瑞士，经 Arosa/法国 Sanary-sur-Mer 流亡瑞士 Küsnacht；1938 起美国（普林斯顿授课、国会图书馆德语文学顾问 1941、1942–1952 洛杉矶 Pacific Palisades）；麦卡锡时期受 HUAC 压力辞去国会图书馆职务，1952 迁瑞士 Kilchberg，终身未再定居德国
- 文学师承与影响（page.md 明载）：Theodor Fontane 的「温和讽刺」文体影响最深；Goethe 为终生楷模（1949 年赴法兰克福+魏玛双城纪念歌德诞辰 200 周年）；Herman Bang 影响中短篇；Schopenhauer 哲学滋养 Buddenbrooks 的衰败叙事；Nietzsche 影响贯穿（疾病与创造力的关联）；热爱托尔斯泰并敬重果戈理/冈察洛夫/屠格涅夫的俄国文学
- 关键荣誉：Nobel Literature 1929（瑞典学院 Anders Österling 提名）；歌德奖 1949；普鲁士艺术学院诗歌部辞职 1933；波恩大学荣誉博士 1936 被撤销、1946-12-13 恢复；普林斯顿/哈佛/哥伦比亚/牛津/剑桥等十余荣誉博士
- 核心作品与贡献（4–6 条）：
  1. *Buddenbrooks*（1901，吕贝克商人家庭四代衰亡，1929 诺奖主因）
  2. *Tonio Kröger*（1903）/ *Tristan*（1903）中短篇艺术
  3. *Death in Venice*（1912，威尼斯之死）
  4. *The Magic Mountain*（1924，魔山；源自 1912 年 Katia 达沃斯疗养院探视）
  5. *Joseph and His Brothers* 四部曲（1933–1943，诺奖奖金在立陶宛 Nida 建的夏日小屋写成）
  6. *Doctor Faustus*（1947，作曲家 Leverkühn 与德国文化之堕落；音乐咨询 Adorno、融合 Schoenberg 风格）
- 关键时间线（15–20 节点）：
  1. 1875-06-06 生于吕贝克
  2. 1891 父逝，全家迁慕尼黑
  3. 1894–95 南德火灾保险公司
  4. 1898 首个短篇 *Little Herr Friedemann*
  5. 1900 完成 *Buddenbrooks*（1901 出版）
  6. 1903 *Tonio Kröger* / *Tristan*
  7. 1905 与 Katia Pringsheim 结婚
  8. 1905–1906 计划腓特烈大帝小说（未成）
  9. 1909 *Royal Highness*
  10. 1912 陪 Katia 赴达沃斯疗养院（魔山之源）
  11. 1918 《一个不关心政治者的反思》——早期保守立场
  12. 1922 《论德意志共和国》演讲——转向共和
  13. 1924 *The Magic Mountain*（畅销扭转财务）
  14. 1929 诺贝尔文学奖；奖金建 Nida 夏屋（1930–1932 夏季在此写 Joseph）
  15. 1930 柏林演讲《理性的呼吁》反纳粹
  16. 1933-02 流亡（Arosa→瑞士）；03-17 辞去普鲁士艺术学院诗歌部；慕尼黑住宅被没收
  17. 1936 捷克斯洛伐克护照；德国籍被吊销；波恩荣誉博士被撤销
  18. 1938 赴美（普林斯顿）；1940-10 起 BBC 对德广播（每月 8 分钟）；1943 广播集《听，德国！》
  19. 1944-06-23 入籍美国；1947 *Doctor Faustus*；1949 歌德奖与歌德 200 周年双城纪念
  20. 1952 迁 Kilchberg；1955-08-12 卒；1954 未完成 *Confessions of Felix Krull*

### 第 1 步：建立目录

- 在 `literature/presentations/20th_century/` 下创建 `Thomas_Mann/` 与 `images/`

### 第 2 步：复制 Makefile

- 设置 `MAIN=Thomas_Mann_zh`、`VIDEO_NAME=Thomas_Mann_zh`

### 第 3 步：收集图片

- 肖像：待下载（1929 年像或 Bundesarchiv 1932 留声机照）
- 备选插图：Buddenbrookhaus（吕贝克故居，今家族博物馆）、*Buddenbrooks* 1909 版书影

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modernism | 现代主义 | infobox Movement 明载 | 核心页 |
| 1 | novel | 长篇小说 | Buddenbrooks/魔山/浮士德博士的史诗规模 | 代表作页 |
| 2 | novella | 中短篇小说 | Tonio Kröger/威尼斯之死 | 中短篇页 |
| 3 | essay | 随笔/政论 | 不关心政治者的反思、听德国 | 随笔页 |
| 4 | social criticism | 社会批判 | 市民阶层衰变、法西斯氛围讽刺（Mario and the Magician） | 主题页 |

#### 4.1 入库操作（yaml 见 `MySQL/data/Thomas_Mann.yaml`）

- 新建 people 主记录（`name_en='Thomas Mann'`，qid=Q37030），`primary_occupation='writer'`、`has_social_data=1`
- 关联职业 writer(rank 0)/novelist/essayist；国籍 Germany/Czechoslovakia/United States 三条
- 5 个领域写入 `person_field`；校验同标杆第 4 步

### 第 4.5 步：社会关系梳理 + 入库

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Katia Pringsheim | 无向 | 1905 年结婚，富裕世俗犹太实业家家庭出身 |
| parent-child | Erika Mann | 无向 | 长女，作家 |
| parent-child | Klaus Mann | 无向 | 长子，作家 |
| parent-child | Golo Mann | 无向 | 次子，历史学家/作家 |
| parent-child | Monika Mann | 无向 | 女 |
| parent-child | Elisabeth Mann Borgese | 无向 | 女 |
| parent-child | Michael Mann (scholar) | 无向 | 幼子 |
| colleague | Heinrich Mann | 无向 | 兄长，同为小说家，流亡加州时期相互扶持（库无 sibling 类型，以 colleague 表达） |
| influence | Theodor Fontane | 无向 | 「温和讽刺」文体的最深影响者 |
| influence | Johann Wolfgang von Goethe | 无向 | 终生楷模与「诗人国王」榜样 |
| influence | Arthur Schopenhauer | 无向 | Buddenbrooks 衰败叙事的哲学滋养 |
| influence | Friedrich Nietzsche | 无向 | 疾病与创造力关联的影响贯穿其作 |
| influence | Leo Tolstoy | 无向 | 特别钟爱的俄国作家（果戈理/冈察洛夫/屠格涅夫同列敬重） |
| influence | Richard Wagner | 无向 | 挚爱其歌剧；1933 年专文捍卫瓦格纳免遭纳粹挪用 |
| influence | Arnold Schoenberg | 无向 | Doctor Faustus 主人公音乐风格取法其作曲法 |
| colleague | Theodor W. Adorno | 无向 | Doctor Faustus 音乐理论咨询者 |
| colleague | Lion Feuchtwanger | 无向 | 流亡洛杉矶同侪，Villa Aurora 常客 |
| colleague | Bertolt Brecht | 无向 | 加州流亡圈交往 |
| colleague | Helen Tracy Lowe-Porter | 无向 | Knopf 委任的英译者，译其全部作品 |
| colleague | H. L. Mencken | 无向 | 介绍 Mann 与 Knopf 出版社结缘 |
| influence | Yukio Mishima | 无向 | 三岛由纪夫自承受其影响 |
| influence | Joseph Campbell | 无向 | 自述 Mann 是其导师之一 |

#### 4.5.1 入库操作

- 以 `name_en='Thomas Mann'` 为中心写入 `person_relation`；缺失人物建占位（不编造 qid）
- 同名区分：幼子入库名用 `Michael Mann (scholar)`（学者 Michael Mann，1919–1977），勿与同名学者混淆
- ⚠️ Paul Ehrenberg（小提琴画家，青年时期挚友）系日记私谊，关系表不入库（type 无对应、防噪声），提示词正文可提及

### 第 5 步：设计配色方案

- **气质**：庄重、暖褐、市民沙发的呢绒感 + 雪山冷光
- **配色**：深褐（主色，预分配 `#5C3A1E`）+ 香槟金 `C9A227` + 四分类色
  - `badgeA` modernism 现代主义 — 铁灰蓝 `#37474F`
  - `badgeB` novel 长篇小说 — 呢绒红 `#7B3B2E`
  - `badgeC` novella 中短篇小说 — 雪山青 `#4A6B7C`
  - `badgeD` social criticism 社会批判 — 黄铜金 `#A8823C`

### 5.1 文学家格式硬要求

1. 封面有头像 + 细边框 + 姓名小字注。
2. 封面明示国籍（Germany → United States 变迁一行）；底部状态栏 `国籍 | 代表作 | 主要奖项`。
3. 必须有身份信息页（生卒、本名、公民权变迁、家庭六子女、流亡路线、荣誉、核心领域）。
4. 品牌口径 `OpenMathAI`；引号半角。
5. 无公式框——引文框用 BBC 广播原句（英文原文 page.md 有载）："The war is horrible, but it has the advantage of keeping Hitler from making speeches about culture."

### 第 6 步：规划幻灯片序列

```
00  OpenLiterature 项目首页
01  封面 — 市民阶层的史诗画家 / Thomas Mann 1875–1955 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）
03  核心贡献概览 — Buddenbrooks / 魔山 / Joseph 四部曲 / Doctor Faustus
04  吕贝克商人世家 (1875–1894) — 汉萨阶层、父逝迁慕尼黑
05  慕尼黑起步 (1894–1901) — Simplicissimus、Buddenbrooks 成书
06  Buddenbrooks（代表作书影 + 引文框）— 四代衰亡结构图
07  中短篇艺术 (1903–1912) — Tonio Kröger、威尼斯之死
08  魔山 (1924) — 达沃斯疗养院、「平原上的山」意象图式
09  1929 诺贝尔奖 — Österling 提名、「主要表彰 Buddenbrooks」口径
10  流亡：从 Arosa 到太平洋峭壁 (1933–1942) — 国籍变迁三段
11  BBC 广播与约瑟夫兄弟 (1940–1943) — 引文框
12  Doctor Faustus (1947) — Adorno/Schoenberg 与德国文化之堕落
13  晚年与遗产 (1952–1955) — Kilchberg、Exilliteratur 旗手
14  结尾
```

### 第 7–8 步：编写源码与布局检查 【模板通用】

- 每页定义 `\newcommand{\xxxslide}`；写完即 `make` + `pdftoppm` 目检。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Mann 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖口径 | "principally for his great novel, Buddenbrooks..."——「主要表彰」三字不可删；获奖主要因 Buddenbrooks（有影响力的评委个人口味致其余作品未被详引），勿写成「因魔山获奖」 |
| 国籍变迁 | Germany(至1936)→Czechoslovakia(1936–44)→US(1944)；捷克斯洛伐克护照是从未居留的荣誉护照，勿写「移居捷克」 |
| 卒因 | 临床误诊血栓性静脉炎、尸检为髂动脉瘤破裂——两层都要写对 |
| 兄长 | Heinrich Mann 是兄长；库无 sibling 类型，用 colleague + note 明示「兄长」，Review 勿误改为 rival |
| 早期保守 | 1918《一个不关心政治者的反思》保守立场与 1922 后转向共和并存——两个阶段都要写，勿截取一半 |
| 书籍未焚 | 他的书不在 1933 焚书之列（或因诺奖得主身份）——客观一句，勿演绎 |
| 政治红线 | BBC 广播、HUAC、集体罪责表态只按 page.md 客观转述，不作政治评价 |
| 性取向材料 | 日记相关内容仅作「diaries reveal struggles with sexuality, reflected in works」一句，不展开细节清单 |
| 六子女 | Erika/Klaus/Golo 三人成重要作家（正文明载）；幼子入库用 Michael Mann (scholar) 防同名 |
| Nida 夏屋 | 诺奖奖金建于立陶宛 Nida（库尔斯沙嘴），1930–1932 夏季写 Joseph；今为纪念馆 |
| 日记焚毁 | 1945 年 5 月于 Pacific Palisades 焚毁 1933 年 3 月前日记（1918-1921 册保留）——年份别写反 |
| 引语红线 | 正文可直接引用的英文原句仅 BBC 广播句等数处；其余「引语」须核对英文原文，禁编 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| *Buddenbrooks* | 《布登勃洛克一家》 | 1901；副题「一个家族的衰亡」 |
| *The Magic Mountain* | 《魔山》 | 1924；Der Zauberberg |
| *Death in Venice* | 《威尼斯之死》 | 1912 中篇 |
| *Joseph and His Brothers* | 《约瑟夫和他的兄弟们》 | 1933–1943 四部曲 |
| *Doctor Faustus* | 《浮士德博士》 | 1947 |
| Exilliteratur | 流亡文学 | 反纳粹流亡德语文学的总称 |
| Hanseaten | 汉萨市民贵族阶层 | 吕贝克社会背景 |
| *Reflections of a Nonpolitical Man* | 《一个不关心政治者的反思》 | 1918，早期保守立场 |
| *Listen, Germany!* | 《听，德国！》 | 1943 广播集 |

---

## 四、背景音乐选择 【预分配】

- **选定曲目**: **New Lands**
- **风格**: 开拓 / 新大陆 / 转折
- **匹配理由**:
  - "新大陆" 字面匹配其人生后半章——1938 起流亡美国、普林斯顿执教、Pacific Palisades 的德语流亡圈，是 Exilliteratur 在新大陆开枝散叶的故事
  - 「开拓」匹配创作上的不断越境——从吕贝克市民史诗到圣经四部曲再到音乐小说，题材三度远征
  - 收束段落的辽阔感呼应 1949 年歌德 200 周年双城之行：德国文化超越政治边界的宣言
- **本地路径**: 曲库对应曲目拷贝至 `literature/presentations/20th_century/Thomas_Mann/New Lands.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Thomas_Mann/page.md` | 本地 Wikipedia 正文（事实基准；体量大，引用须复核） |
| `literature/generate_20th_century_list.py` | 官方获奖理由中译 CITATION_ZH（禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `music_audio/curated_tracks.md` | BGM 曲库标签对照 |

> **开始执行。最重要的事：事实只写 page.md 明载内容；政治内容客观简述不评价。**
