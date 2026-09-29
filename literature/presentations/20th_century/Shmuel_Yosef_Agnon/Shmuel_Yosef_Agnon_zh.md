# 文学家立传提示词（OpenLiterature 批次实例：Shmuel Yosef Agnon）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Shmuel Yosef Agnon（1966 诺贝尔文学奖，现代希伯来文学中坚）为实例。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 数学家/物理学家/化学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson 提示词骨架）+ 文学家适配（无公式框，以名句引文框/意象图式/书影替代）。
- **本实例**：Shmuel Yosef Agnon（萨缪尔·约瑟夫·阿格农），奥地利匈牙利出生的以色列希伯来语小说家、诗人、短篇作家，现代希伯来文学中坚人物。
- **设计哲学**：文学家立传保留「身份信息页」与「领域结构化表达」骨架；视觉重心转向**地理与文本的双重旅程**——本篇以「从加利西亚到耶路撒冷」贯穿。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Shmuel Yosef Agnon（1887-08-08 ~ 1970-02-17，享年 82 岁；本名 Shmuel Yosef Halevi Czaczkes，笔名 S. Y. Agnon / ש"י עגנון）
- **1966 诺贝尔文学奖官方获奖理由**：
  > "for his profoundly characteristic narrative art with motifs from the life of the Jewish people"
  > （中译：表彰其深具个性的叙事艺术，以犹太人民的生活为主题）
- **气质关键词**：**现代希伯来文学的中坚、shtetl 世界的复魅者、古希伯来语与拉比文献的炼字师**
- **设计母题**：**从加利西亚到耶路撒冷（Galicia → Jerusalem）**。他一生辗转布察茨—雅法—柏林—巴特洪堡—耶路撒冷，每一段社群都化为作品；版式可用寄居、藏书、火焰（两次「毁灭」）与旧城石墙的意象图式贯穿。
- **本地数据源**：`literature/presentations/pages/20th_century/Shmuel_Yosef_Agnon/page.md`（Wikipedia 全文 + frontmatter）+ 同目录 `metadata.json`、`images.txt`
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Shmuel_Yosef_Agnon
- **肖像**：第 0 步待下载（infobox 1966 年领奖照片）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 已抓取页面到 `literature/presentations/pages/20th_century/Shmuel_Yosef_Agnon/`（第一轮已核对，事实基准如下）：
  - 生卒（1887-08-08 生于东加利西亚布察茨，奥匈帝国，今乌克兰布恰奇 ~ 1970-02-17 逝于雷霍沃特，享年 82 岁；安葬耶路撒冷橄榄山犹太公墓）
  - **生日裁定**：正文与 infobox 均取 1887-08-08；他后来自称 1888 年 Tisha B'Av（圣殿被毁日）——系 1920 年代为免兵役而采用的虚构日期；**出生日期一律写 1887-08-08**
  - 国籍（奥匈帝国出生 → 德国时期 → 巴勒斯坦 → 以色列；page.md 叙述口径 "Austro-Hungarian-born Israeli"）
  - 家庭（五个孩子中的长子；父为哈西德派；外祖父 Yehuda Farb 属反对哈西德派的 Misnagdim；1920 与 Esther Marx（1889–1973，Königsberg 人，学者 Alexander Marx 之妹）成婚，育有二子；女儿 Emuna Yaron 主持身后出版；严格素食）
  - 教育（3 岁入 cheder 约 6 年后离开，此后由家庭教师与父亲教授塔木德与迈蒙尼德；无现代学院学位）
  - 任职/流亡（1908 移居雅法；1912-1924 侨居德国柏林/莱比锡/巴特洪堡；1924 年巴特洪堡大火焚毁藏书与全部手稿，三个月内离开德国；1929 雅路撒冷 Talpiot 家宅在动乱中被劫——他称两事为 "two destructions"）
  - 关键荣誉（Nobel 1966 与 Nelly Sachs 共享；Bialik Prize 1934、1950 两度；Israel Prize 1954、1958 两度；魏茨曼研究所荣誉博士；耶路撒冷荣誉市民；Ussishkin Prize 1946）
  - 文学影响与师承（page.md 明载：自述首要影响是圣经故事；亦受德国文学与欧陆文学（读德译本：Flaubert、Dostoevsky、Goethe、Fontane）影响；受朋友 Yosef Haim Brenner 与萌芽期希伯来文学影响；在德国与 Bialik、Ahad Ha'am 交往；受哈西德传说、拉比文献与加利西亚 maskilim 文学熏陶）
  - 核心作品与贡献（4–6 条）：①《The Bridal Canopy》（Hakhnasat Kalla，1931，加利西亚犹太史诗，奠定其地位）；②《And the Crooked Shall Be Made Straight》（1912，哈西德故事改编，密集用典成其标志）；③《A Guest for the Night》（1939，战后故乡荒芜）；④《Only Yesterday》（1945，第二次 Aliyah 时代史诗，与上书并称两大杰作）；⑤《A Simple Story》（1935）/《Shira》（未完成，写了约 25 年）；⑥语言贡献：混用现代希伯来语与拉比希伯来语（batei yadayim/rotev 等用例），Bar-Ilan 大学为其建语料库
  - 关键时间线（15–20 节点）：1887 生于布察茨 / 3 岁入 cheder / 1903 起在加利西亚刊物发表 / 1908 赴雅法、以 "Agnon" 署名发表《Agunot》/ 1909 结识 Bialik / 1910 Buber 在 Die Welt 发表其小说德译 / 1912《And the Crooked…》/ Brenner 出资出版 / 1912-1924 德国十二年 / 1914 一战阻断返程 / 1920 与 Esther Marx 成婚 / 1920-21《Hakhnasat Kalla》初版连载 / 1924-06-06 巴特洪堡大火 / 1924 定居耶路撒冷 Talpiot / 1929 家宅被劫 / 1931 Schocken 版全集四卷 / 1935《A Simple Story》/ 1938《Days of Awe》/ 1939《A Guest for the Night》/ 1945《Only Yesterday》/ 1951 心脏病改站立写作为坐写 / 1966 诺贝尔奖（典礼在光明节安息日，先行安息日结束与点灯仪式再领奖）/ 1967 加入大以色列运动 / 1970-02-17 逝于雷霍沃特 / 1985-2014 头像与诺奖演说印上 50 谢克尔纸币

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下创建 `Shmuel_Yosef_Agnon/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同类目录既有 Makefile，设置 `MAIN=Shmuel_Yosef_Agnon_zh`、`VIDEO_NAME=Shmuel_Yosef_Agnon_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像待下载（infobox 1966 领奖照；images.txt 有 URL 直接用，250px 改 500px；404 用装饰圆占位）
- 可选插图：故乡布察茨全景（OldBuchachPanorama.jpg）、Talpiot 书房照、50 谢克尔纸币

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modern hebrew literature | 现代希伯来文学 | 中坚人物，1966 诺奖核心 | 核心页 |
| 1 | hasidic literature | 哈西德文学 | 重述虔诚传说与哈西德故事 | 传统页 |
| 2 | biblical allusion | 圣经典故 | 自述首要影响为圣经故事 | 语言页 |
| 3 | short story | 短篇小说 | 约 25 年持续发表短篇 | 作品页 |
| 4 | rabbinic language | 拉比文献语言 | 古今希伯来语混合的语言艺术 | 语言页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Nelly Sachs | 无向 | 1966 诺贝尔文学奖共享 |
| spouse | Esther Marx | 无向 | 1920 年成婚，学界家族出身 |
| colleague | Martin Buber | 无向 | 柏林挚友，合编哈西德文学选，转发其作品德译 |
| colleague | Hayim Nahman Bialik | 无向 | 1909 雅法相识，巴特洪堡希伯来文学圈同道 |
| colleague | Ahad Ha'am | 无向 | 巴特洪堡希伯来文学圈同道 |
| colleague | Yosef Haim Brenner | 无向 | 挚友与早期知遇者，出资出版《And the Crooked Shall Be Made Straight》 |
| colleague | Gershom Scholem | 无向 | 柏林犹太复国主义青年圈，称其 "the Jews' Jew"，曾译其小说 |
| colleague | Salman Schocken | 无向 | 恩主与出版人，Schocken 出版社为其出书 |

#### 4.5.1 入库操作

- 写入 `MySQL/data/Shmuel_Yosef_Agnon.yaml`，`python3 seed_person.py data/Shmuel_Yosef_Agnon.yaml` 幂等入库
- 方向约定：无向关系自动 from<to 归一；note 含 ": " 用单引号包裹
- 本篇无 advisor-student 关系（page.md 无明确师承——自述影响来自圣经文本，非人）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：古雅、虔诚、流散与归来的双声部
- **配色**：普鲁士蓝（主色，预分配 `#1E4E79`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeHebrew` 现代希伯来文学 — 普鲁士蓝 `#1E4E79`
  - `badgeHasidic` 哈西德文学 — 深褐 `#5C3A1E`
  - `badgeGalicia` 加利西亚世界 — 灰蓝 `#5C7A99`
  - `badgeJerusalem` 耶路撒冷岁月 — 石金色 `#B08D3E`
- **背景母题**：旧书页纹理的细线框 + 少量半透明圆形（灯火意象），克制不密集

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注（含希伯来名 ש"י עגנון 需专用字体族，参照希伯来文渲染经验）。
2. **封面有国籍**：底部状态栏给出 `出生地 | 定居地 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后，左头像 + 右信息网格（生卒/本名与笔名/国籍变迁/教育/两次「毁灭」/主要荣誉/核心领域）。
4. **文学家无公式框**：用名句引文框（仅限 page.md 有英文原文者，如诺奖演说 "As a result of the historic catastrophe in which Titus of Rome destroyed Jerusalem…"）、书影或意象图式替代。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 现代希伯来文学的中坚 / Shmuel Yosef Agnon 1887–1970 + badge + 头像
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 叙事艺术 / 哈西德世界 / 语言炼金 / 两大杰作
04  布察茨童年 (1887–1908) — cheder、父授塔木德、外祖父的 Misnagdim 对照、1903 首次发表
05  雅法与笔名诞生 (1908–1912) — 《Agunot》署名 Agnon、Bialik 相识、Brenner 知遇
06  德国十二年 (1912–1924) — Buber 圈子、Schocken 恩主、Der Jude 园地
07  两次「毁灭」— 1924 大火与 1929 被劫、类比两度圣殿被毁（意象图式）
08  耶路撒冷与两大杰作 — 《A Guest for the Night》/《Only Yesterday》书影
09  语言炼金术 — batei yadayim/rotev 用例、古今希伯来语混合、语料库
10  恢复宗教生活 — Talpiot 的传统主义、与世俗文坛的张力
11  晚年写作 — 站立改坐写、《Shira》未竟、布察茨纪念《Ir u-melo'ah》
12  1966 诺贝尔奖 — 与 Nelly Sachs 共享、引文框、光明节安息日领奖细节
13  荣誉与身后 — 两度 Bialik/Israel Prize、50 谢克尔纸币、Beit Agnon 博物馆
14  遗产 — 从加利西亚 shtetl 到以色列国民文学
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照已有文学侧成品的 `\profileslide` 模式。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Agnon 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生日 | 取 1887-08-08（18 Av 5647）；他自称的 1888 年 Tisha B'Av 日期是 1920 年代自造，仅可作为「他自己采用 1888」叙述，勿当真实生日 |
| 「以色列建国 pray 文祷文」 | 《Prayer for the Welfare of the State of Israel》作者 2018 年研究确认为 Herzog 总拉比、Agnon 仅编辑——勿写「Agnon 所作」，两说均须注明裁定 |
| 死亡地 | 逝于雷霍沃特（Rehovot）而非耶路撒冷，但葬于橄榄山；勿混 |
| 笔名 | "Agnon" 取自首篇发表小说《Agunot》标题，后成法定姓氏；勿写「希伯来语意为『漂泊者』」等无载释义 |
| 与 Sachs | 仅共享 1966 奖；两人无交往记载，勿加写 |
| 政治内容 | 1967 加入大以色列运动一笔带过、按 page.md 客观表述（宗教信念而非政治纲领），不展开政治叙事 |
| Brenner 角色 | Brenner 是挚友+出资人+早期认可者，非导师；勿写「师从 Brenner」 |
| Schocken | 是恩主/出版人（businessman），勿写成「犹太学者导师」 |
| 作品年份 | Hakhnasat Kalla：1920 连载初版 → 1931 扩为长篇出版，两处年份语境不同勿混 |
| 无载禁写 | 具体博士/学位（无）、儿女具体姓名（page.md 仅提女儿 Emuna Yaron）、创作方法论细节 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| shtetl | 犹太小镇（意第绪） | 东欧犹太小镇，勿译「犹太区」 |
| Second Aliyah | 第二次移民潮（阿利亚） | 1904–1914 巴勒斯坦移民运动 |
| cheder | 希伯来启蒙学堂 | 传统初等宗教教育 |
| Hasidism / Misnagdim | 哈西德派 / 反哈西德派 | 两大立场对立，外祖父属后者 |
| Hakhnasat Kalla | 《新娘华盖》 | The Bridal Canopy |
| Temol shilshom | 《昨日未远》/ Only Yesterday | 直译「前天与昨天」 |
| Days of Awe | 《可畏之日》 | 高圣日习俗与传说选 |
| agunot | 被弃之妇 | 笔名出处，宗教法概念 |
| Bialik Prize / Israel Prize | 比亚利克奖 / 以色列奖 | 各两度，年份勿混 |
| two destructions | 两次毁灭 | 大火+被劫的自况 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **SEA**（预分配）
- **风格**: 深海 / 辽阔 / 沉静叙事
- **匹配理由**:
  - "SEA" 的辽阔沉静匹配《In the Heart of the Seas》（Bi-levav yamim，海之心）的航海叙事与流散—归来的海洋意象
  - 深海底色适配其语言的古奥与叙事的绵长——不是奔涌而是深流
  - 曲名的「海」呼应从加利西亚到雅法再到耶路撒冷的地理跨越
- **备选** (未采用): Timeless（沉稳但已被同批其他语言项目高频使用）、Eternals（宏大但偏史诗感，弱于其内省气质）
- **本地路径**: `music_audio/` 下 SEA 曲目 → 复制到 `presentations/20th_century/Shmuel_Yosef_Agnon/SEA.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Shmuel_Yosef_Agnon/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Shmuel_Yosef_Agnon/metadata.json` | properties 辅助（冲突以正文为准） |
| `literature/presentations/pages/20th_century/Shmuel_Yosef_Agnon/images.txt` | 肖像 URL 清单（第 3 步下载源） |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 名录（获奖理由中译） |
| `literature/generate_20th_century_list.py` 的 CITATION_ZH | 官方获奖理由中译（key=(年份,姓名)） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/data/Shmuel_Yosef_Agnon.yaml` | 本人社会关系/领域 yaml（已入库） |
| `music_audio/curated_tracks.md` | BGM 曲库标签对照 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
