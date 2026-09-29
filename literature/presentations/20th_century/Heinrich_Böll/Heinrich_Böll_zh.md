# 文学家立传提示词（OpenLiterature · Heinrich Böll）

> **目标项目**：OpenLiterature —— 开放文学史（与 OpenPhysicist/OpenChemist 共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Heinrich Theodor Böll（海因里希·伯尔，1972 诺贝尔文学奖）。
> **设计哲学**：文学家立传沿用「身份信息页 + 结构化研究领域」骨架；本篇无公式框，以**代表作书影/名句引文框/意象图式**替代。

---

## 一、模板定位

- **目标人物**：Heinrich Böll，1972 年诺贝尔文学奖得主，战后德语文学代表。
- **一句话定位**：从废墟中写出普通人尊严的「德国良知」——废墟文学（Trümmerliteratur）的领军者与坚定的和平主义者。
- **适配说明**：物理学家的「公式框」在本篇一律替换为「名句引文框/书影框」（如「never war again」与《Katharina Blum》书影）。

---

## 二、背景信息 【人物专属】

- **姓名**：Heinrich Theodor Böll；中文通译 海因里希·伯尔（又译贝尔/布尔）。
- **生卒**：1917-12-21 生于科隆（时属普鲁士、德意志帝国）～ 1985-07-16 逝于 Langenbroich（Eifel 地区 Kreuzau，西德），享年 67 岁。
- **获奖**：1972 年诺贝尔文学奖。官方获奖理由（EN 原文，禁止改写）：
  > "for his writing which through its combination of a broad perspective on his time and a sensitive skill in characterization has contributed to a renewal of German literature"
  > 中译（名录 CITATION_ZH）：「表彰其写作以其对时代的广阔视野与敏感的人物刻画相结合，促成了德国文学的更新」。
- **气质关键词**：**废墟的记录者、小人物的辩护人、和平主义的良心**。
- **设计母题**：**废墟与重建（Rubble & Rebuilding）**——被轰炸的科隆、废墟中的天使、瓦砾间的日常生活；背景可用稀疏碎块/砖石纹理装饰圆。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Heinrich_Böll/page.md`（Wikipedia 全文，已核对）
  - 同目录 `metadata.json`、`images.txt`；Wikipedia URL：https://en.wikipedia.org/wiki/Heinrich_B%C3%B6ll
- **肖像**：第 0 步待下载（page.md 内嵌 1981 年照）。

---

## 三、任务流程 【逐步执行，每步汇报】

### 第 0 步：事实基准（已核对 page.md，禁止再杜撰）

- **家庭与少年**：生于科隆天主教和平主义家庭，家人反对纳粹；1930 年代拒绝加入希特勒青年团；先做书店学徒，后入科隆大学攻读德语文学（German studies）与古典学。中学时代一位反纳粹教师（Mr. Bauer）特别讲授罗马讽刺诗人 Juvenal——伯尔购得 1838 年译本随身带过整场战争。
- **战争经历**：应征入伍（Wehrmacht），先后在波兰、法国、罗马尼亚、匈牙利、苏联作战；四次负伤并染伤寒；1945-04 被美军俘虏，入战俘营。
- **战后**：回科隆在家族木器作坊工作，又在市统计局工作一年，后辞职冒险成为作家——30 岁起全职写作。
- **文学生涯起点**：1949 首部长篇《Der Zug war pünktlich》（The Train Was on Time）；受邀出席 1949 四七社（Group 47）聚会，1951 年其作品被评为该社最佳。
- **代表作**：《And Never Said a Word》(1953)、《The Bread of Those Early Years》(1955)、《Billiards at Half-past Nine》(1959)、《The Clown》(1963)、《Group Portrait with Lady》(1971)、《The Lost Honour of Katharina Blum》(1974)、《The Safety Net》(1979)；旅行文学《Irish Journal》(1957)；写于 1949/50 的《The Silent Angel》1992 年才出版（描写科隆大轰炸之后）。作品译成 30 余种语言，仅苏联一国即售数百万册。
- **荣誉一览**：1953 德国工业文化奖/南德广播奖/德国评论家奖；1954 Tribune de Paris 奖；1955 法国最佳外国小说奖；1958 Wuppertal Eduard von der Heydt 奖/巴伐利亚美术学院奖；1959 北威州大艺术奖/科隆文学奖/美因茨科学与文学院院士；1960 巴伐利亚美术学院成员/Charles Veillon 奖；1967 格奥尔格·毕希纳奖（Georg Büchner Prize）；1972 诺贝尔文学奖；1974 美国艺术暨文学学会成员/Ossietzky 奖章（表彰其对人权的捍卫与贡献）；1983 美国哲学学会；1984 美国艺术与科学院。
- **职务**：1971-1973 任国际笔会（PEN International）主席；此前任西德 P.E.N. 主席——以西德 P.E.N. 主席身份推荐索尔仁尼琴获诺贝尔奖；常以新德国文化代表出访。
- **争议与媒体围攻**：1963 《The Clown》因对天主教会与基民盟的负面描写引发论战；1972 文章《Soviel Liebe auf einmal》批评《图片报》造假新闻，被《明镜》改题后反遭「同情恐怖主义」指控（源于其坚持 Baader-Meinhof 案的正当程序），被施普林格报团记者称为「暴力的精神之父」；1974-02-07 柏林 BZ 报率先报道其家被搜查（实际搜查在报纸发行之后）；1977 Schleyer 绑架案后 40 名警察据匿名举报搜查其家（称其子为同伙，查无实据），此后被基民盟列入黑名单——立传中只客观陈述事件链，不作政治评价。
- **信仰与晚年**：1976 公开退出天主教会（「没有背离信仰」）；与妻子居于科隆与 Eifel，并常驻爱尔兰西海岸 Achill 岛度假屋（1992 起成为作家驻地）；1985-07-16 逝世。
- **关键时间线（15 节点）**：1917 科隆出生 → 1930s 拒绝希特勒青年团 → 书店学徒 → 科隆大学德语文学与古典学 → 1939-45 从军五国战场、四度负伤 → 1942 与 Annemarie Cech 结婚 → 1945-04 美军战俘营 → 战后木器作坊与统计局 → 1949 处女长篇 + Group 47 → 1951 四七社最佳 → 1953-55 连获三奖 → 1957 《Irish Journal》→ 1959 《九点半打台球》→ 1963 《小丑之争》论战 → 1967 毕希纳奖 → 1971-73 国际笔会主席 → 1972 诺贝尔奖 → 1974 《Katharina Blum》与搜查风波 → 1976 退教 → 1985-07-16 逝世于 Langenbroich。

### 第 4 步：文学领域表（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | rubble literature | 废墟文学 | Trümmerliteratur，战后德国文学重建 | 核心页 |
| 1 | postwar German fiction | 战后德语小说 | 《九点半打台球》《女士及众生相》 | 代表作页 |
| 2 | pacifist literature | 和平主义文学 | 「永不重蹈战争」的创作母题 | 战争页 |
| 3 | social satire | 社会讽刺 | 《小丑》《丧失了名誉的卡塔琳娜·布鲁姆》 | 论战页 |
| 4 | radio drama | 广播剧 | field_of_work 明载的体裁 | 体裁页 |

### 第 4.5 步：社会关系表（与 yaml relations 完全一致，仅收 page.md 明载）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Annemarie Cech | 无向 | 1942 结婚，三子，长期合作翻译英语文学 |
| colleague | Aleksandr Solzhenitsyn | 无向 | 1962 苏联之行结识，1974 收留于 Eifel 家中，以西德 P.E.N. 主席身份推荐其获诺奖 |

> page.md 载及的翻译对象作家（Behan/Synge/Shaw/O'Brien/Salinger 等）是翻译工作而非私人关系，禁建关系；Graham Greene/Georges Bernanos 仅为评论者的类比，Juvenal 经由教师间接阅读，William Morris 仅为 "seems to have been an admirer"——一律禁建关系。三子 page.md 未具名，不入库。

### 第 5 步：配色方案

- **主色**（预分配）：深墨绿 `#145C54`（废墟上重建的坚韧）
- **辅色**：诺奖香槟金 `C9A227`
- **badge 四分类色**：
  - `badgeRubble` 废墟文学 — 砖灰 `#6D6A6A`
  - `badgePacifist` 和平主义文学 — 苔原绿 `#4E6B5A`
  - `badgeSatire` 社会讽刺 — 铁锈红 `#A63A2B`
  - `badgeIreland` 爱尔兰岁月 — 海蓝 `#2E6E8E`
- **背景母题**：稀疏的碎砖块与圆角矩形（废墟与重建意象）。

### 第 6 步：幻灯片序列（15 页）

```
00  OpenLiterature 项目首页（\input 共享封面）
01  封面 — 废墟上的德国良知 / Heinrich Böll 1917–1985 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/科隆/婚姻/战争/荣誉/核心领域）
03  核心贡献概览 — 废墟文学 / 战后小说 / 和平主义 / 社会讽刺
04  科隆少年 (1917–1939) — 天主教和平主义家庭、拒入希特勒青年团、Juvenal 译本
05  五国战场与战俘营 (1939–1945) — 四次负伤、伤寒、美军俘虏
06  从统计局到 Group 47 (1945–1951) — 30 岁全职写作、处女长篇、四七社最佳
07  《The Silent Angel》：废墟里的天使（核心贡献页·书影替代公式框）
08  崛起的十年 (1953–1963) — 三部长篇连发、《爱尔兰日记》
09  《小丑之争》(1963)（名句引文框）— 教会与政党批评引发的论战
10  毕希纳奖与诺贝尔奖 (1967/1972) — 官方获奖理由 + 保守媒体攻击一笔
11  国际笔会主席与索尔仁尼琴 (1971–1974) — 推荐诺奖、Langenbroich 收留
12  媒体围攻的岁月 (1972–1977) — Bild 论战、搜查风波（客观事件链）
13  《卡塔琳娜·布鲁姆》(1974)（书影框）— 对小报暴力的文学回答
14  Achill 岛与晚年 (1957–1985) — 爱尔兰度假屋、退教、遗作
15  结尾
```

### 第 7 步：版式要点

- 身份信息页国籍行写「德国（普鲁士科隆 → 西德）」；出生地年代口径：1917 出生时科隆属普鲁士/德意志帝国。
- 引文框可用两条：战争总结 "never war again"（page.md 明载短语）与索尔仁尼琴受奖演说引伯尔作品的转述；《Katharina Blum》1974 书影框放代表作页。
- 争议页（12）克制排版：只列「年份 + 事件 + 结果」三栏，不引施普林格报团的攻击性称号入大字标题。

### 第 8 步：专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 只用官方句 "for his writing which through its combination of a broad perspective on his time and a sensitive skill in characterization has contributed to a renewal of German literature"，勿改写 |
| 「德国良知」标签 | Gewissen der Nation 是他人加的称号且伯尔本人想摆脱（认为会遮蔽真正责任机构的清算）——立传提及须注明此层，勿当作尊号使用 |
| The Silent Angel | 写于 1949/50，1992 年才出版——勿写成 1950 年代出版 |
| 搜查时序 | 1974-02-07 BZ 报先报道、当日晚才实际搜查——顺序勿颠倒 |
| 与索尔仁尼琴关系方向 | 是伯尔收留索氏、推荐其诺奖；索氏受奖演说引伯尔作品——勿写成师承或合著 |
| 翻译归属 | 70 余种译作多为夫妇二人合作；单独署名伯尔的仅少数（如 The Hard Life）——勿全部记于其一人名下 |
| 政治红线 | Baader-Meinhof 相关争议只按 page.md 客观陈述其「主张正当程序」立场，不引「暴力的精神之父」等攻击语入正文标题 |
| 无载禁写 | 不写博士导师/文学师承（page.md 无）；不写与 Greene/Bernanos 的私人交往（仅评论类比）；三子未具名不入库 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险点 |
|------|------|------|
| Trümmerliteratur | 废墟文学 | 战后德国文学流派标签 |
| Group 47 | 四七社 | 1949 受邀、1951 最佳 |
| The Train Was on Time | 《列车正点到达》 | 1949 处女长篇 |
| Billiards at Half-past Nine | 《九点半打台球》 | 1959 |
| The Clown | 《小丑》 | 1963，又译《小丑之见》 |
| Group Portrait with Lady | 《女士及众生相》 | 1971 |
| The Lost Honour of Katharina Blum | 《丧失了名誉的卡塔琳娜·布鲁姆》 | 1974 |
| The Safety Net | 《保护网下》 | 1979 |
| Irish Journal | 《爱尔兰日记》 | 1957 旅行文学 |
| Georg Büchner Prize | 格奥尔格·毕希纳奖 | 1967，德语文学最高奖之一 |
| PEN International | 国际笔会 | 1971-73 任主席 |
| never war again | 「永不重蹈战争」 | page.md 明载的和平主义信条 |
| Achill Island | 阿基尔岛 | 爱尔兰西海岸居所 |

---

## 四、BGM 建议

- **选定曲目**：**With Me** — Alex-Productions（预分配）。
- **匹配理由**：曲名「与我同行」匹配伯尔一生与普通人并肩的写作立场（护士抱怨来探病的都是「底层朋友」）；曲风沉稳含蓄，匹配废墟文学「不动声色的道德叙述」；收束段落的力量感匹配其晚年笔耕不辍的形象。
- **备选**（未采用）：Timeless（已用于他篇，气质偏宏大）；The Flow of Time（历史感强但张力不足）。
- **时长**：以 `music_audio/curated_tracks.md` 为准，>15 页 × 7 秒即可，ffmpeg `-shortest` 对齐。

---

## 五、数据入库说明（已完成）

- **yaml**：`MySQL/data/Heinrich_Böll.yaml`，name_en=`Heinrich Böll`（frontmatter 原形），qid=Q42747，primary_occupation=`writer`，fields 5 条（第 4 步表），relations 2 条（第 4.5 步表，page.md 明载仅此二）。
- **入库**：`python3 seed_person.py data/Heinrich_Böll.yaml`（幂等，按 QID → name_en 匹配）。
- **验证**：has_social_data=1、person_field≥4、person_relation≥2。

> **开始执行 Beamer 立传时，每写一页就 make，看到溢出就修。**
