# 文学家立传提示词（OpenLiterature 实例：Anatole France）

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（OpenMathAI 共享仓库，与 OpenPhysicist/OpenTuring 平级）。
- **本实例**：Anatole France（阿纳托尔·法朗士，1921 诺贝尔文学奖，法国讽刺大师与人文主义文人典范）。
- **设计哲学**：文学家立传以「作品意象 + 名句引文框」替代科学家的公式框；身份信息页与研究领域结构化表达仍是骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Anatole France（本名 François-Anatole Thibault，1844-04-16 生于巴黎 ~ 1924-10-12 逝于 Saint-Cyr-sur-Loire，享年 80 岁）
- **1921 官方获奖理由**（禁止改写）：
  > EN: "in recognition of his brilliant literary achievements, characterized as they are by a nobility of style, a profound human sympathy, grace, and a true Gallic temperament"
  > 中译（CITATION_ZH, key=("1921","Anatole France")）：表彰其辉煌的文学成就，以风格的高贵、深切的人类同情、优雅与真正的高卢气质为特征
- **气质关键词**：**优雅的反讽者、书斋里的人文主义者、第三共和国文坛盟主**
- **设计母题**：**反讽之灯（旧书铺与启蒙寓言）**。书商之子、终身藏书家——以旧书铺灯光、鹅毛笔与书卷为底纹；辅以《企鹅岛》的企鹅剪影呼应其把人性讽刺推向寓言高度的文学世界。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Anatole_France/page.md`（Wikipedia 全文，事实基准）
  - `literature/presentations/pages/20th_century/Anatole_France/metadata.json`、`images.txt`（辅助，冲突以正文为准）
  - Wikipedia URL：https://en.wikipedia.org/wiki/Anatole_France
  - 肖像（第 0 步待下载）：`Anatole_France_1921.jpg`（正文插图，c. 1921 真实照片）；备选 Vanity Fair 1909 Guth 漫画像（核对图注防误用）

---

## 三、任务流程 【逐步执行，每步汇报】

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- **生卒**：1844-04-16 生于巴黎；1924-10-12 逝于 Saint-Cyr-sur-Loire（近 Tours），享年 80 岁；葬于 Neuilly-sur-Seine 旧公墓
- **本名**：François-Anatole Thibault（笔名 Anatole France）
- **国籍**：法国
- **家庭**：书商之子（其父书店专营法国大革命书刊，为文人学者聚处）；1877 与 Valérie Guérin de Sauville 结婚（1893 离婚），女 Suzanne（1881–1918）；1888 起与大沙龙女主人 Léontine Lippmann（Mme Arman de Caillavet）长久交往至其 1910 去世；1920 与原管家 Emma Laprévotte 再婚
- **教育**：Collège Stanislas（私立天主教学校）；毕业后在父书店帮工，后任 Bacheline-Deflorenne 与 Lemerne 书目编目员
- **任职**：1876 年起任法国参议院（Senate）图书馆员
- **文学师承与影响**：page.md 未载明确师承（勿编造导师）；属帕尔纳斯派圈子（1869 年《Le Parnasse contemporain》刊其诗、1875 年入第三辑编委会）
- **关键荣誉**：Nobel 1921；法兰西学术院院士（1896 当选）；《Le Crime de Sylvestre Bonnard》获法兰西学术院奖；Montyon Prize、Vitet Prize、半个世纪最佳小说大奖（frontmatter award_received）；荣誉军团勋章（骑士/军官）
- **核心作品与贡献（4–6 条）**：
  1. 《Le Crime de Sylvestre Bonnard》（1881）——成名作，优雅文体获法兰西学术院奖
  2. 《Thaïs》（1890）、《La Rôtisserie de la Reine Pédauque》（1893）——讽刺神秘主义与世纪末风潮
  3. 《L'Île des Pingouins》（1908）——企鹅受洗变人的法兰西讽刺史，直指德雷福斯事件并终于反乌托邦未来
  4. 《Les dieux ont soif》（1912）——以罗伯斯庇尔信徒写恐怖统治，警示政治与意识形态狂热
  5. 《La Révolte des anges》（1914）——堕天使革命寓言，公认其最深刻反讽之作
  6. 社会批评散文《Le Jardin d'Épicure》（1895）等；名句「法律以其庄严的平等，禁止富人和穷人同样睡在桥洞下、沿街乞讨、偷窃面包」（出自《The Red Lily》，page.md 英文原文在载）
- **关键时间线（15–20 节点）**：
  1. 1844-04-16 生于巴黎，书商之家
  2. 就读 Collège Stanislas（天主教学校）
  3. 1867 起为记者撰稿
  4. 1869 《Le Parnasse contemporain》刊诗 "La Part de Madeleine"
  5. 1873 《Poèmes dorés》
  6. 1875 入《Le Parnasse contemporain》第三辑编委会
  7. 1876 任法国参议院图书馆员
  8. 1877 与 Valérie Guérin de Sauville 结婚
  9. 1879 《Jocaste et le chat maigre》
  10. 1881 《Le Crime de Sylvestre Bonnard》成名并获法兰西学术院奖；女 Suzanne 生
  11. 1885 《Le Livre de mon ami》（回忆录）
  12. 1888 与 Léontine Lippmann 开始长久交往（其沙龙为第三共和国文坛枢纽）
  13. 1890 《Thaïs》
  14. 1893 与妻离婚；同年《La Rôtisserie de la Reine Pédauque》与《Les Opinions de Jérôme Coignard》
  15. 1895 《Le Jardin d'Épicure》
  16. 1896 当选法兰西学术院院士
  17. 1897–1901 四部曲《L'Histoire contemporaine》（含《Monsieur Bergeret à Paris》1901，写德雷福斯事件）
  18. 德雷福斯事件中签署左拉的支持 Dreyfus 的宣言
  19. 1908 《L'Île des Pingouins》《Vie de Jeanne d'Arc》
  20. 1912 《Les dieux ont soif》；1914 《La Révolte des anges》
  21. 1920 与 Emma Laprévotte 再婚；支持新创法国共产党
  22. 1921 获诺贝尔文学奖
  23. 1922-05-31 全部著作被列入天主教《禁书目录》（Index Librorum Prohibitorum），他视之为「殊荣」
  24. 1924-10-12 逝于 Saint-Cyr-sur-Loire

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下创建 `Anatole_France/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已成品目录的 Makefile，设 `MAIN=Anatole_France_zh`、`VIDEO_NAME=Anatole_France_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：优先 `Anatole_France_1921.jpg`（真实照片，500px）；下载用 `curl -A "Mozilla/5.0"` + `file` 验证；失败则用装饰圆占位（禁止把书影/签名当肖像）

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | satirical fiction | 讽刺小说 | 反讽与怀疑精神贯穿一生 | 核心页 |
| 1 | literary criticism | 文学批评 | 《Alfred de Vigny》《Le Génie Latin》等 | 批评页 |
| 2 | social criticism | 社会批评 | 《Le Jardin d'Épicure》、德雷福斯介入 | 社会页 |
| 3 | poetry | 诗歌 | 帕尔纳斯派起点（1869–1876） | 早年页 |
| 4 | memoir | 回忆录 | 《Le Livre de mon ami》四部 | 回忆页 |

- 入库：`MySQL/data/Anatole_France.yaml` → `python3 seed_person.py data/Anatole_France.yaml`（person_field 带 rank）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Valérie Guérin de Sauville | 无向 | 1877 结婚，1893 离婚；女 Suzanne（1881–1918） |
| spouse | Emma Laprévotte | 无向 | 1920 再婚（原管家） |
| colleague | Léontine Lippmann | 无向 | 1888–1910 长年伴侣；主持第三共和国著名文学沙龙 |
| colleague | Émile Zola | 无向 | 德雷福斯事件中签署其支持 Dreyfus 的宣言 |

**禁写（无载/非社会关系）**：Marcel Proust 笔下 Bergotte「widely believed」以其为原型——非二人交往，禁写成师友；George Orwell 的辩护系后世评论，不入关系；俄国革命/法共支持仅客观一笔，不作政治评价。

### 第 5 步：设计配色方案 【人物专属】

- **主色**：#8B1A1A（诺奖红——典雅人文）+ 诺奖香槟金 `C9A227`
- **badgeA** 讽刺小说 — 深红 `#8B1A1A`；**badgeB** 文学批评 — 靛蓝 `#1E4E79`；**badgeC** 社会批评 — 琥珀 `#E07B30`；**badgeD** 诗歌/回忆录 — 青绿 `#0E7C7B`
- **背景母题**：旧书铺灯光下的书卷剪影 + 稀疏圆点（呼应企鹅岛寓言的童话感）

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 优雅的反讽者 / Anatole France 1844–1924 + 主色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（本名、生卒、教育、任职、婚姻、荣誉、核心领域）
03  核心贡献概览 — 讽刺小说 / 文学批评 / 社会批评 / 诗歌
04  早年：书铺之子（1844–1876）— Collège Stanislas、编目员、参议院图书馆员
05  帕尔纳斯起点（1867–1879）— 诗人与记者
06  成名：《Sylvestre Bonnard》（1881）— 优雅文体与学术院奖
07  世纪末讽刺（1890–1896）— Thaïs、Reine Pédauque、Jérôme Coignard、入院士
08  介入：德雷福斯事件 — 签署左拉宣言、Monsieur Bergeret
09  讽刺巅峰（1908–1914）— 企鹅岛 / 诸神渴了 / 诸神的 revolt 三书并列
10  名句引文框 — 「法律以其庄严的平等……」（The Red Lily，英文原文在载）
11  晚年与争议 — 二婚、支持法共（客观一笔）、1922 禁书目录（自认殊荣）
12  荣誉与诺奖 — 1921 获奖理由四要素（nobility of style / human sympathy / grace / Gallic temperament）
13  遗产：第三共和国文人典范 — Proust 原型之争（只写 believed，勿坐实）
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照既有成品 `\profileslide` 模式

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，`pdftoppm` 截图目检溢出/重叠；修复优先级：删装饰条 → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标

### 第 9 步：史实审查 + 术语审查 【人物专属】

**France 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 本名 | François-Anatole Thibault，笔名 Anatole France，勿混 |
| Proust 原型 | page.md 只说「widely believed」，禁写成「Proust 的导师/挚友」 |
| 两段婚姻 | 1877 结婚–1893 离婚；1920 再婚 Emma Laprévotte，勿混年份 |
| Léontine Lippmann | 姓夫家 Caillavet，交往至其 1910 去世；是沙龙主人非妻子 |
| 禁书目录 | 1922-05-31 全部著作入 Index，他视为「distinction」——讽刺点，勿写成被迫害惨事 |
| 政治内容 | 支持俄国革命/法共只按 page.md 客观一句，不作政治评价不展开 |
| 女儿 | Suzanne 1881 生、1918 卒，勿漏卒年 |
| 死亡地 | Saint-Cyr-sur-Loire（近 Tours），勿写成巴黎 |
| 获奖理由 | 官方强调 style 高贵/人类同情/优雅/高卢气质四要素，勿用二手转述替代 |
| 肖像 | Vanity Fair 1909 是 Guth 漫画像、c.1921 是真实照片，图注必须核对 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Académie Française | 法兰西学术院 | 1896 当选；学术院奖系另一项 |
| Index Librorum Prohibitorum | 禁书目录 | 1922 列入、1966 废止 |
| Dreyfus affair | 德雷福斯事件 | 签署宣言的史实口径 |
| Parnasse contemporain | 当代帕尔纳斯 | 诗集平台，勿写成流派成员身份坐实 |
| fin de siècle | 世纪末 | 1893 两书的风潮背景 |
| Gallic temperament | 高卢气质 | 获奖理由原文，勿译成「法国脾气」 |
| man of letters | 文人 | 导语原文定位 |
| irony / skepticism | 反讽/怀疑主义 | 人物气质双关键词 |
| L'Île des Pingouins | 企鹅岛 | 1908，讽刺史结构 |
| Les dieux ont soif | 诸神渴了 | 1912，恐怖统治警示 |
| La Révolte des anges | 天使的叛变 | 1914，「最深刻反讽」评价在载 |
| Crainquebille | 克兰克比尔 | 1901 小说/1903 戏剧同名两作 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition**（分批文件预分配）
- **匹配理由**：从书铺编目员到参议院图书馆员、再到院士与诺奖的漫长文学生涯，是一场贯穿第三共和国的「文学远征」；曲风的行进感匹配其介入时代事件（德雷福斯）的公共知识分子姿态，也匹配企鹅岛式寓言的叙事推进。
- **本地路径**：按 `music_audio/curated_tracks.md` 对应文件复制为本目录 `Expedition.wav`
- **时长**：以曲目实际长度与成片页数对齐（ffmpeg `-shortest`）
