# 文学家立传提示词（OpenLiterature 21 世纪批次：Patrick Modiano）

> **本文件是 Patrick Modiano（2014 诺贝尔文学奖）的人物专属立传提示词**，供后续 Beamer 立传 agent 直接复制到新对话中按步执行。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（内容适配文学家）。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 旗下，与 mathematician/physicist/chemist 侧同构）。
- **本实例**：Jean Patrick Modiano（帕特里克·莫迪亚诺），法国小说家，2014 诺贝尔文学奖得主——第 15 位获此奖的法国作家；autofiction（自传体小说）代表作家。
- **设计哲学**：文学家立传保留「身份信息页」与「研究领域结构化表达」两大骨架；文学家无公式框——用**名句引文框 / 代表作书影 / 意象图式**替代。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Jean Patrick Modiano（1945-07-30 生于布洛涅-比扬古，在世）
- **官方获奖理由**（2014，Wikipedia 原文照录，禁止改写）：
  > "for the art of memory with which he has evoked the most ungraspable human destinies and uncovered the life-world of the occupation"（中译照录 `generate_21st_century_list.py` CITATION_ZH：表彰其记忆的艺术，唤起了最难以把握的人类命运，揭示了被占领时期的生命世界）
- **气质关键词**：**记忆的艺术、占领时期的巴黎、寻人者的匿名街道** —— 40 余部著作反复叩问身份、责任、记忆与失落。
- **设计母题**：**记忆的寻人启事（the art of memory）**。其作由旧电话簿、街道门牌、报纸寻人栏拼合而成——视觉语言取「巴黎黑白街景 + 档案纸色块 + 雾感光晕」，呼应「沙地只容足迹存留片刻」的匿名感。
- **本地数据源**：
  - `literature/presentations/pages/21st_century/Patrick_Modiano/page.md`（Wikipedia 全文 + frontmatter）
  - `literature/presentations/pages/21st_century/Patrick_Modiano/metadata.json`、`images.txt`
  - Wikipedia URL: https://en.wikipedia.org/wiki/Patrick_Modiano （肖像：2014-12-06 斯德哥尔摩记者会照，第 0 步待下载）

---

## 三、任务流程 【逐步执行】

> 数据库同步要求：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 greatminds 库（MySQL），yaml 路径 `MySQL/data/Patrick_Modiano.yaml`，入库引擎 `MySQL/seed_person.py`。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已下载（事实基准如下，第一轮已核对）
- 肖像待下载：infobox 照片（Modiano in 2014）
- **事实基准**：
  - 生年：1945-07-30 生于巴黎西郊 Boulogne-Billancourt；在世
  - 国籍：法国；犹太-意大利裔（父系出自萨洛尼卡著名 Italo-Jewish Modiano 家族）
  - 家庭：父 Albert Modiano（1912–77，巴黎人，战时拒戴黄星、1942-02 被捕险遭遣送，**据称**涉黑市与 Carlingue，1977 逝前从未向儿子言明此段）；母 Louisa Colpeyn（1918–2015）佛兰德演员；父母占领巴黎相识，其出生后不久分离；由外祖父母抚养，佛兰德语为第一语言
  - 弟弟 Rudy（小两岁）9 岁病逝；1967–1982 作品皆题献 Rudy
  - 教育：Jouy-en-Josas 蒙塞勒小学 → Thônes 圣约瑟夫中学 → 巴黎亨利四世高中（在此随作家 Raymond Queneau 上几何课）→ 1964 安纳西会考 → 违愿入 hypokhâgne 很快辍课 → 1965 索邦注册（为缓征，未获学位）
  - 婚姻家庭：1970 娶 Dominique Zehrfuss；女 Zina（1974）、Marie（1978）
  - 关键荣誉：Fénéon + Roger Nimier 1968 · 法兰西学院小说大奖 1972 · 书商奖 1976 · 龚古尔奖 1978 · 摩纳哥亲王奖 1984 · Paul-Morand 2000 · Cino Del Duca 2010 · 奥地利国家欧洲文学奖 2012 · Nobel 2014
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列展开）

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/21st_century/` 下创建 `Patrick_Modiano/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同批已完成人物目录的 Makefile，设置 `MAIN=Patrick_Modiano_zh`、`VIDEO_NAME=Patrick_Modiano_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：infobox 照片（curl -A "Mozilla/5.0"，500px）；404 则用 images.txt 兜底，再不行用装饰圆占位
- 可选插图：《Dora Bruder》书影或占领时期巴黎街景意象

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | autofiction | 自传体小说 | 自传与历史虚构的融合，其标志体裁 | 风格页 |
| 1 | historical fiction | 历史小说 | 占领时期法国的人之境遇 | 核心页 |
| 2 | literature of memory | 记忆书写 | 诺奖理由核心词，身份与记忆之考掘 | 主题页 |
| 3 | detective fiction | 侦探小说元素 | Dora Bruder 糅合传记/自传/侦探小说 | 代表作页 |
| 4 | Paris in literature | 巴黎书写 | 街道、习尚与人群的演变 | 风格页 |

- 入库：`fields` 写入 `person_field`（带 rank）；缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

> 只收 page.md 明载关系；yaml 与本表完全一致。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Dominique Zehrfuss | 无向 | 妻子，1970 结婚 |
| parent-child | Albert Modiano | 无向 | 父亲，犹太-意大利裔，1977 逝，从不言明战时经历 |
| parent-child | Louisa Colpeyn | 无向 | 母亲，佛兰德演员 |
| parent-child | Zina Modiano | 无向 | 长女，1974 生 |
| parent-child | Marie Modiano | 无向 | 次女，1978 生 |
| influence | Raymond Queneau | 无向 | 少年时代导师与文学引路人，亨利四世几何课，引荐伽利玛 |
| colleague | Louis Malle | 无向 | 《Lacombe, Lucien》合作编剧（1974 电影） |

### 第 5 步：设计配色方案 【人物专属色彩】

- **主色**：深夜蓝 `#16324F`（占领时期巴黎的雾夜与档案卷宗）
- **诺奖香槟金**：`C9A227`
- 四分类色（badgeA–D）：
  - `badgeA` 记忆书写 — 靛蓝 `#4C5FD5`
  - `badgeB` 占领时期历史 — 琥珀 `#E07B30`
  - `badgeC` 自传体小说 — 青绿 `#0E7C7B`
  - `badgeD` 侦探元素 — 玫瑰 `#C4204F`
- **背景母题**：巴黎黑白街景色块 + 档案纸色 + 雾感光晕，呼应「记忆的寻人启事」

### 5.1 文学家格式硬要求 【★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：底部状态栏给出 `国籍 | 身份 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心内容之前。左头像 + 右信息网格，含至少：生年、全名、国籍、出生地、家庭（父/母/弟 Rudy/妻/女）、教育、职业（小说家/编剧）、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注 `OpenMathAI`；引号用半角 `" "`；中文引号内不写「原话」，除非 page.md 有英文原文。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 记忆的艺术 / Patrick Modiano 1945– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  占领年代出生的孩子 (1945–1964) — 父亲的沉默、佛兰德语童年、弟弟 Rudy 之死、亨利四世
04  雷蒙·格诺：引路人 — 几何课 → 引荐伽利玛；「自青春期起 mentor」
05  一鸣惊人 — 1968 La Place de l'Étoile（22 岁处女作，Fénéon + Roger Nimier 奖）
06  龚古尔之路 — 1972 法兰西学院小说大奖 → 1978 龚古尔（Rue des Boutiques obscures / Missing Person）
07  作品长廊 — 30 余部小说时间轴（La Place de l'Étoile 1968 → La Danseuse 2023）
08  风格（核心贡献页）— 身份之谜 / 记忆与失落 / 巴黎街道演变 / 「富有同情心的悔憾惊悚」
09  Dora Bruder — 传记·自传·侦探小说的混文体；1941 巴黎晚报寻人栏起点的档案书写（客观简述）
10  剧本与电影 — Lacombe Lucien（与 Louis Malle 合写，1974）；Bon Voyage（2003）等
11  荣誉长廊 — 龚古尔 1978 · Cino Del Duca 2010 · 奥地利国家奖 2012 · Nobel 2014
12  遗产与结尾 — 第 15 位法国诺奖文学作家；作品译成 30 余种语言，获奖前多部尚无英译
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现参照成品 `\profileslide`。
- 引文框/意象图式替代公式框：可用 page.md 明载的 Modiano 自述句（如 "After each novel, I have the impression that I have cleared it all away..."）与 Svenbro 颁奖词（Heaney "the poetry of place"）入引文框，逐字照录勿改。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删装饰元素 → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Modiano 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 父亲战时经历 | 黑市与 Carlingue 关联系 page.md 原文 "allegedly"（据称）——保留「据称」措辞，勿坐实；「从未向儿子言明」是明载要点 |
| Rudy 入库裁定 | 弟弟 Rudy（9 岁病逝，1967–1982 作品题献者）系**兄弟关系**，关系白名单无 sibling 类型——不入关系库，只在叙事中呈现 |
| Queneau 定性 | 非学院导师（亨利四世几何课 + 自青春期 mentor + 引荐出版界）——用 influence 类型，勿写 advisor-student |
| Proust 类比 | 「有时被比作普鲁斯特」系他人比较，禁入关系表 |
| 颁奖词引语 | Svenbro 颁奖演说（引 Heaney "the poetry of place"）为 page.md 明载英文原文，可入引文框逐字照录 |
| 诺奖巧合 | Dora Bruder 的 Dora 与诺奖无关的人物考证线索勿混入；Dora 15 岁被逐奥斯维辛——客观简述，不渲染 |
| 译介反差 | 作品译成 30 余种语言，但获奖前多数长篇无英译——对比 Tranströmer 勿串数字 |
| 龚古尔作品名 | Rue des Boutiques obscures 英译 Missing Person（暗店街）；勿把中译「暗店街」当法文原名 |
| 教育噪声 | frontmatter 有 Lycée Michel-Montaigne，正文作 Collège Saint-Joseph de Thônes——以正文为准 |
| 婚礼轶事 | 伴郎 Queneau 与 Malraux 争吵系 Dominique 2003 年《Elle》访谈转述——可作花絮一句，注意是转述口径 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| autofiction | 自传体小说 | 自传+历史虚构融合，勿译「自传」 |
| the art of memory | 记忆的艺术 | 诺奖理由原词 |
| the Occupation | 占领时期 | 1940–44 德占法国，全篇统一口径 |
| Prix Goncourt | 龚古尔奖 | 1978（Rue des Boutiques obscures） |
| Missing Person | 《暗店街》 | 英译名 vs 法文原名勿混 |
| Dora Bruder | 《多拉·布吕代》 | 混文体代表作 |
| amnesia | 失忆 | Missing Person 主角设定 |
| short story cycle 勿混 | — | 本篇关键词是 autofiction 与 memory |
| Lacombe, Lucien | 《拉孔布·吕西安》 | 与 Louis Malle 合编剧本 |
| pedigree | 《家谱》（Un pedigree） | 其自传体回忆录，自称 "pedigree" 非 autobiography |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**: **Cinematic Experience** — Alex-Productions（47k views，较高受众 / 电影感 / 高张力）
- **匹配理由**:
  - 「电影感」直接对应其编剧身份与小说的黑白影像质感 —— Lacombe Lucien、占领时期巴黎的街道镜头感
  - 「高张力」匹配侦探小说元素的悬疑底色 —— 失忆、寻人、身份追踪的叙事引擎
  - 深夜蓝主色 #16324F 与该曲的冷峻电影氛围相称
- **备选**（未采用）：★★ Tragedy（深色/戏剧性，与其挽歌气质相符但同批 Tranströmer 已用，避重）
- **本地路径**: `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav` → 复制到本目录 `CinematicExperience.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Patrick_Modiano/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `literature/generate_21st_century_list.py` | 获奖理由中译（CITATION_ZH）对照 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
