# 文学家立传提示词（OpenLiterature：Giosuè Carducci）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Giosuè Carducci（1906 诺贝尔文学奖，意大利首位文学奖得主）为实例。
> 结构对齐母本 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框——用**名句引文框 / 古典意象图式 / 书影**替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Giosuè Alessandro Giuseppe Carducci（焦苏埃·卡尔杜齐），1906 年诺贝尔文学奖得主、首位获文学奖的意大利人。
- **设计哲学**：文学家立传强调「代表作与文学世界」+ 身份信息页；卡尔杜齐的核心视觉语言是**古典复兴**——希腊罗马诗体的再造、反浪漫主义的橄榄与橡树、博洛尼亚讲坛上的民族诗人。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Giosuè Carducci（1835-07-27 ~ 1907-02-16，享年 71 岁）
  - ★ 日期裁定：生 7 月 27 日、卒 2 月 16 日以 infobox/正文为准（frontmatter 有 07-28 / 02-08 / 00-00 噪声，弃用）
- **气质关键词**：**民族诗人、古典复兴者、反浪漫主义斗士** —— 1906 诺贝尔文学奖获奖理由：
  > EN 原文（官方，禁止改写）: "not only in consideration of his deep learning and critical research, but above all as a tribute to the creative energy, freshness of style, and lyrical force which characterize his poetic masterpieces."
  > 中译（CITATION_ZH）: 不仅因其深厚的学识与批判性研究，更致敬其诗歌杰作所体现的创造力、清新风格与抒情力量
- **设计母题**：**蛮族颂歌（Barbarian Odes）**——以阿尔凯奥斯/萨福诗体重铸拉丁韵律的"野蛮"缪斯；橡树图腾（Majani 漫画：诗人之头长成橡树）；异教精神对抗教权。
- **本地数据源**：`literature/presentations/pages/20th_century/Giosuè_Carducci/page.md`（+ `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Giosu%C3%A8_Carducci （肖像第 0 步**待下载**，infobox 有 c. 1900 照片）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）

---

## 三、任务流程 【逐步执行，每完成一步汇报】

### 第 0 步：事实基准（第一轮已核对 page.md）

- **生卒**：1835-07-27 生于 Valdicastello di Pietrasanta（托斯卡纳大公国，今卢卡省）~ 1907-02-16 卒于博洛尼亚；葬 Certosa di Bologna
- **国籍**：意大利王国（生于托斯卡纳大公国时期）
- **家庭**：父 Michele Carducci 乡村医生、烧炭党人（因 1831 革命入狱），全家因政治屡迁；母 Ildegonda Celli；弟 Dante 1857 自杀；1858 父逝
- **婚姻**：1859-03 娶 Elvira Menicucci
- **教育**：教会学校至 1852（修辞教师 Piarist 神父 Geremia Barsottini 精译贺拉斯）；比萨师范学校（Scuola Normale Superiore）奖学金，1856 获博士学位与教师资格
- **文学师承与影响**：父亲欲传 Manzoni 浪漫主义而未果（"never acquired a taste for Romanticism"）；少年迷古典——译荷马《伊利亚德》卷 9；受 Foscolo、Mazzini 思想感召；诗风亲和 Victor Hugo 与 Heinrich Heine（page 明载 "affinities"）
- **任职**：San Miniato 中学修辞教师 → Arezzo 希腊语讲席胜出但因父之政治记录被大公政府否决 → Pistoia 希腊语讲席 → 1860 经教育大臣 Mamiani 任命任博洛尼亚大学意大利修辞/文学讲席直至 1904 辞职；1890-11-04 起为意大利王国参议员；1866 加入博洛尼亚共济会 "Galvani" 分会
- **关键荣誉**：Nobel 1906（首位意大利人）；OCI/OSML 勋位；博洛尼亚纪念碑（Bistolfi 设计，1908-1926）；水星上有以他命名的环形山
- **核心作品与贡献**：
  1. *Rime*（1857）——首部诗集
  2. *Juvenilia*（1850-60，1871 成书六卷）
  3. *Inno a Satana*（1863 作/1865 出版）——渎神挑衅之作，"撒旦"为叛逆自由精神之喻
  4. *Giambi ed Epodi*（1882，署名 "Enotrio Romano"）——论战诗
  5. *Odi barbare*（1877 起，蛮族颂歌）——拟古典诗体的巅峰与代表作
  6. *Rime nuove*（1887）/ *Rime e ritmi*（1899）
  7. 散文二十卷：Parini 评注、但丁《Rime》论、Tasso《Aminta》辩护、Foscolo 早期研究；德诗翻译（Heine、Goethe）
- **关键时间线**（15–20 节点）：1835 生于 Valdicastello → 1846 写第一批诗 → 1848 革命后家迁 Lajatico/佛罗伦萨 → 1852 后受 Barsottini 贺拉斯熏陶 → 1855 《L'arpa del popolo》、与 Chiarini/Gargani 创 "Amici Pedanti" → 1857 《Rime》、弟自杀 → 1859 娶 Elvira、与 Barbera 创刊《Il Poliziano》 → 1860 就任博洛尼亚讲席 → 1862 Aspromonte 事件后转向共和派 → 1863《Inno a Satana》→ 1866 入共济会 → 1873 起《Odi barbare》→ 1881-84 为《Cronaca Bizantina》撰稿 → 1882《Giambi ed Epodi》/《Nuove odi barbare》→ 1887《Rime nuove》→ 1890 任参议员 → 1894 圣马力诺演讲（"Mazzini 与华盛顿的上帝"）→ 1899 中风致手瘫 → 1899《Rime e ritmi》→ 1904 辞教（弟子 Pascoli 接任）→ 1906 诺贝尔奖 → 1907-02-16 卒于博洛尼亚

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | lyric poetry | 抒情诗 | 蛮族颂歌与新歌集，现代意大利最伟大抒情诗人之一 | 核心页 |
| 1 | neoclassical poetry | 新古典主义诗歌 | 拟阿尔凯奥斯/萨福体的古典复兴 | 蛮族颂歌页 |
| 2 | literary criticism | 文学批评 | Parini/但丁/Tasso/Foscolo 研究二十卷 | 散文页 |
| 3 | classical philology | 古典文献学 | 博洛尼亚讲席、荷马/贺拉斯译介 | 早年页 |
| 4 | literary translation | 文学翻译 | 海涅、歌德德诗意译 | 作品页 |

#### 4.1 入库操作
- `MySQL/data/Giosuè_Carducci.yaml` → `python3 MySQL/seed_person.py data/Giosuè_Carducci.yaml`
- `primary_occupation='writer'`、occupations：writer(0)/poet(1)/literary critic(2)；nationality：Kingdom of Italy
- 校验 fields≥4、relations≥2、has_social_data=1

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Elvira Menicucci | 无向 | 1859-03 成婚 |
| advisor-student | Giovanni Pascoli | 师→生（弟子） | 博洛尼亚弟子，1904 接任其讲席 |
| colleague | Giuseppe Chiarini | 无向 | 1855 共创反浪漫主义社团 Amici Pedanti |
| colleague | Gabriele D'Annunzio | 无向 | 《Cronaca Bizantina》同刊撰稿人 |
| influence | Victor Hugo | 对方→本人 | 论战诗亲和其风格（page 明载 affinities） |
| influence | Heinrich Heine | 对方→本人 | 讽刺笔法来源，并译其诗入意语 |

### 第 5 步：设计配色

- **主色**：靛蓝紫 `#283593`（古典学养的深湛）+ 诺奖香槟金 `C9A227`
- badgeA 抒情诗 — 靛蓝 `#4C5FD5`；badgeB 新古典 — 大理石青 `#0E7C7B`；badgeC 批评 — 琥珀 `#E07B30`；badgeD 翻译 — 玫瑰 `#C4204F`
- **背景母题**：希腊回纹饰带 + 橡树叶散点（蛮族颂歌的古典躯壳与意大利乡土）

### 第 6 步：幻灯片序列（15 页）

```
00  OpenLiterature 项目首页（\input cover 共享封面）
01  封面 — 意大利首位文学奖得主 / Giosuè Carducci 1835–1907 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/教育/讲席/参议员/婚姻/荣誉/核心领域）
03  核心贡献概览 — 蛮族颂歌 / Inno a Satana / 论战诗 / 批评与翻译
04  早年：烧炭党人之子 (1835–1855) — 屡迁的童年/贺拉斯与荷马/比萨师范
05  Amici Pedanti 与反浪漫主义 (1855–1859) — 同人社/《Rime》/弟丧与父丧
06  博洛尼亚讲席 (1860–) — Mamiani 任命/受欢迎的讲演者
07  Inno a Satana：渎神之诗 (1863–1869) — 撒旦隐喻/梵一会议背景（名句引文框：Hymn to Satan 节选）
08  蛮族颂歌 (1873–1889) — 阿尔凯奥斯/萨福体/"野蛮"之名由来（核心贡献页）
09  论战诗与 Enotrio Romano — Giambi ed Epodi/Hugo 与 Heine 的亲和
10  1906 诺贝尔奖 — 官方理由 EN+中译/首位意大利人
11  民族诗人与参议员 (1890–1904) — Cronaca Bizantina 圈子/晚年转向君主立宪
12  宗教观变迁 — 无神论→社会性有神论/1894 圣马力诺演讲/1895 与天主教会和解之说
13  弟子与传承 — Pascoli 接任/影响 Swinburne 等英语诗人
14  遗产：橡树长存 — Casa Carducci 博物馆/水星环形山/结尾
```

### 第 7–8 步：版式要点 + 专属陷阱

| 陷阱 | 说明 |
|------|------|
| 生卒双值 | frontmatter 出生 07-27/07-28/01-01、卒日 02-08/02-16 三说并存——**以 infobox 与正文 07-27 / 02-16 为准**，页内不并列噪声值 |
| 诺奖理由 | 强调 deep learning + critical research + creative energy/freshness of style/lyrical force；勿简化为"因蛮族颂歌获奖" |
| Inno a Satana | 作于 1863、1865 出版、1869 由《Il Popolo》再刊挑衅——三个年份勿混 |
| 蛮族颂歌得名 | 因按重音而非音长拟古典诗体、"听起来野蛮"——非贬义外号 |
| Amici Pedanti | 反浪漫主义+反教权社团，1855 年前后；Chiarini/Gargani 同创 |
| 政治内容 | 反教权论战、共济会、1871 巴黎公社颂等一律按 page.md 一句客观带过，**不展开、不评价** |
| 引语红线 | 仅可引 page.md 载有的 "Hymn to Satan" 英译文节选与 "Discorso sulla libertà perpetua di San Marino" 中 "the Universal God of Peoples, Mazzini's and Washington's God"；其余禁杜撰 |
| 同名区分 | Giovanni Pascoli（弟子）≠ 意大利其他 Pascoli；Heine 系亲和/翻译双重，note 写明 |
| 无载禁写 | 不写"与邓南遮私交"、不写蒙塔莱/翁加雷蒂受其影响（page 无载）、不写具体 Bologna 讲席年份外细节 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Barbarian Odes | 蛮族颂歌 | Odi barbare，勿译"野蛮颂歌" |
| Hymn to Satan | 撒旦颂 | Inno a Satana，"撒旦"是自由精神隐喻 |
| Amici Pedanti | 学究之友社 | 反浪漫主义社团 |
| Stilnovisti | 新体诗派 | 中世纪意大利诗派 |
| Enotrio Romano | Enotrio Romano（化名） | 论战诗署名 |
| Alcaic / Sapphic | 阿尔凯奥斯体/萨福体 | 古典诗节 |
| Risorgimento | 意大利统一运动 | 背景词 |
| anticlerical | 反教权的 | 与"反宗教"区分 |

---

## 四、BGM 建议

- **选定曲目**: **Expedition** — Alex-Productions（66k views，高受众 / 探索 / 史诗）
- **匹配理由**: "探索/史诗" 匹配卡尔杜齐的古典远征——以现代意大利语重铸希腊罗马诗体，是一场跨越两千年的文学远征；"高受众" 匹配其民族诗人地位（现代意大利官方诗人）；史诗感呼应蛮族颂歌的宏伟诗节
- **备选**（未采用）: Timeless（沉稳合适但已预留给他人批次风格）；Eternals（长期影响贴切但受众 49k 偏低）
- **时长对齐**: ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Giosuè_Carducci/page.md` | 事实基准 |
| `MySQL/data/Giosuè_Carducci.yaml` | 入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |

> **开始执行。每写一页就 make，看到溢出就修。**
