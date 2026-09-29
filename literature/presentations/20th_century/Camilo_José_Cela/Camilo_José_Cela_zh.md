# 文学家立传提示词（OpenLiterature：Camilo José Cela）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Camilo José Cela（卡米洛·何塞·塞拉），1989 年诺贝尔文学奖得主，西班牙战后小说的旗帜人物。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对塞拉，即「蜂房与荒原」：以怪诞而讥诮的现实主义凝视战后西班牙的贫瘠与暴力，以一句百余页的长句挑战小说的边界；其一生亦是文学荣耀与政治依附并存的公案，须**双线并陈、客观呈现、不作评价**。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Camilo José Cela y Trulock（卡米洛·何塞·塞拉，Iria Flavia 第一代侯爵，1916–2002），西班牙小说家、诗人、散文家，'36 一代（Generation of '36）代表作家；1989 年诺贝尔文学奖得主。
- **设计哲学**：以「蜂房与荒原」为核心叙事——《蜂房》以三百余人物群像写马德里的寒冷与饥饿，怪诞现实主义（tremendismo 一脉）重塑战后西班牙小说；晚期转向形式实验，一句百页长句写 O.K. Corral 枪战。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Camilo José Cela（卡米洛·何塞·塞拉，1916-05-11 ~ 2002-01-17，享年 85 岁）
- **官方获奖理由（Nobel 1989，禁止改写）**：
  > "for a rich and intensive prose, which with restrained compassion forms a challenging vision of man's vulnerability"
  > （表彰其丰富而凝练的散文，以克制的怜悯构成了对人之脆弱性的挑战性审视）
- **气质关键词**：**怪诞现实的凝视者、战后小说的重塑者、文体实验的挑衅者**
- **设计母题**：**蜂房与荒原（the hive & the barren land）**——《蜂房》三百余人物如蜂巢中拥挤的众生，构成视觉母题 A；《帕斯夸尔·杜阿尔特一家》的暴力荒原与《阿尔卡里亚之旅》的荒村行旅构成视觉母题 B；侯爵纹章（1996）为徽记元素。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Camilo_José_Cela/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Camilo_Jos%C3%A9_Cela
- **肖像**：第 0 步优先用 page.md 内嵌图 Ruizanglada 1988 照片（佩尼亚索莱拉阿拉贡致敬会）；404 则用装饰圆占位。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1916-05-11 生于加利西亚 A Coruña 省 Padrón 的乡村堂区 Iria Flavia ～ 2002-01-17 卒于马德里 Centro 医院（心脏病），享年 85 岁；葬于故乡 Santa María de Adina 教区墓地。西班牙语写作。
- **家庭与童年**：九个孩子中最年长；父 Camilo Crisanto Cela y Fernández 为加利西亚人，母 Camila Emanuela Trulock y Bertorini 为有英格兰与意大利血统的加利西亚人；上中产家庭；他自述童年「快乐得难以长大」（"so happy it was hard to grow up"）。
- **教育与疾病**：1921–1925 举家住 Vigo，1925 迁马德里，入 Piarist 学校；1931 确诊肺结核入 Guadarrama 疗养院，利用养病时间写首作 *Pabellón de reposo*（《静养所》）；养病期间精读 **José Ortega y Gasset** 与 Antonio de Solís y Ribadeneyra 的著作。
- **内战**：1936 内战爆发时 20 岁、大病初愈；政治立场保守，逃往叛军控制区，参军后负伤，在 Logroño 住院。
- **成名**：战后一度在纺织业办事处谋生，在此写出首部长篇 *La familia de Pascual Duarte*（《帕斯夸尔·杜阿尔特一家》），1942 年出版时 26 岁；主人公无法在常规道德中找到依托而连环犯罪且无动于衷——该书对塑造二战后西班牙小说的方向起了重大作用。
- **审查官与《蜂房》**：1943 年成为佛朗哥西班牙的审查官；代表作《蜂房》（*La colmena*）1951 年被迫在布宜诺斯艾利斯出版——因情色主题被视为不道德而在西班牙遭禁，其名字一度不得出现于印刷媒体；小说以西班牙现实主义与英语法语当代作家的双重影响，写三百余个人物；其标志性风格——讥诮而常显怪诞的现实主义——在《蜂房》中登峰造极。他始终忠于佛朗哥政权，甚至曾为秘密警察充当线人、告发异见团体活动并出卖同行知识分子（**客观简述，不作评价**）。
- **实验转向**：1960 年代末自《圣卡米洛，1936》（*San Camilo, 1936*）起作品愈发实验性；1988 年《基督对亚利桑那》（*Cristo versus Arizona*）用一个**超过一百页的单句**讲述 O.K. Corral 枪战。
- **晚年争议（客观简述，不作评价）**：以丑闻式发言闻名；1969–1971 年出版俚语与禁忌词词典 *Diccionario secreto* 曾先震动西班牙社会；1998 年在 Mercedes Milá 的国家电视台访谈中夸口演示以肛门吸水（**粗俗细节只客观转述，不引原话**）；1998 年在 Lorca 百年纪念之际就同性恋团体出席纪念发表不当言论（**粗俗语句禁引，只写「发表不当言论引发争议」**）。
- **荣誉时间线**：1957-05-26 入选皇家西班牙语言学院（Seat Q，在任至 2002-01-17）→ 立宪 Cortes 王家参议员，对 1978 年西班牙宪法的措辞施加过影响 → 1986 Creu de Sant Jordi → 1987 阿斯图里亚斯亲王文学奖 → 1988 Castelao Medal → **1989 诺贝尔文学奖** → 1994 Planeta 小说奖（该奖客观性时受质疑，有得主拒绝领奖的先例）→ 1995 塞万提斯奖（此前他获奖后曾形容该奖「涂满了屎」——**粗俗原话禁引，只客观转述其态度转变**）→ 1996-05-17 被胡安·卡洛斯一世封为 Iria Flavia 侯爵（世袭爵位，身后传子）。
- **遗嘱争议**：遗嘱偏袒年轻第二任妻子 Marina Castaño 而亏待首婚之子 Camilo José Cela Conde，引发争议；Conde 后获其父遗产的三分之二。
- **核心作品与贡献（5 条）**：
  1. *La familia de Pascual Duarte*（1942）——暴力与冷漠的战后经典，重塑战后西班牙小说方向；
  2. *La colmena*（《蜂房》，1951 布宜诺斯艾利斯版）——三百余人群像 + 怪诞现实主义，曾遭本国查禁；
  3. 《阿尔卡里亚之旅》（*Viaje a la Alcarria*，1948）——西班牙语旅行文学名作（另有 Ávila、Castilla、安达卢西亚等系列行旅之作）；
  4. 实验转向：*San Camilo, 1936*（1969）、*Cristo versus Arizona*（1988，百页单句）；
  5. *Diccionario secreto*（1968/1969–1971）与《色情百科全书》（1977）——对俚语与禁忌语的词典学整理。
- **关键时间线（16 节点）**：1916 生于 Iria Flavia → 1921–25 Vigo → 1925 迁马德里入 Piarist 学校 → 1931 肺结核入 Guadarrama 疗养院、写 *Pabellón de reposo* → 1936 内战爆发、参军负伤 → 1939 战后在纺织业办事处工作 → 1942 *Pascual Duarte* → 1943 任审查官 → 1944 首婚 → 1948 *Viaje a la Alcarria* → 1951 *La colmena* 布宜诺斯艾利斯出版、本土遭禁 → 1957 入皇家学院 Seat Q → 1969 *San Camilo, 1936* → 1978 宪法参政 → 1988 *Cristo versus Arizona* → 1989 诺贝尔文学奖 → 1995 塞万提斯奖 → 1996 封侯 → 2002-01-17 卒于马德里。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | postwar Spanish novel | 战后西班牙小说 | *Pascual Duarte* 塑造二战后西班牙小说方向 | 成名页 |
| 1 | grotesque realism | 怪诞现实主义 | 讥诮而常显怪诞的现实主义（tremendismo 一脉） | 蜂房页 |
| 2 | social realism | 社会现实主义 | 《蜂房》融合西班牙现实主义与英法当代作家影响 | 蜂房页 |
| 3 | experimental novel | 实验小说 | *San Camilo, 1936* 与百页单句的 *Cristo versus Arizona* | 实验页 |
| 4 | travel writing | 旅行文学 | 《阿尔卡里亚之旅》及系列行旅之作 | 行旅页 |

#### 4.1 入库操作

- 新建/更新 `people` 主记录（`name_en` 用 page.md frontmatter 的 name，`qid` 以分批文件为准），设置 `primary_occupation='writer'`、`has_social_data=1`（`has_biography` 待 Beamer 立传后置 1）
- 关联职业 `writer`（rank 0）与 page.md 明载副职业（poet/novelist/playwright/essayist 等，1–3 行），国籍按 Nobel 官方口径
- 将上表 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`（fields 应为 5）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | María del Rosario Conde Picavea | 无向 | 1944 年结婚，1990 年离婚，育有独子 |
| spouse | Marina Castaño | 无向 | 1991 年结婚，相伴至 2002 年去世 |
| parent-child | Camilo José Cela Conde | 无向 | 独子，承袭 Iria Flavia 第二代侯爵，后获遗产三分之二 |
| influence | José Ortega y Gasset | Cela ← 对方 | 养病期间精读其著作，早期思想资源 |

> 病中精读的另一位 Antonio de Solís y Ribadeneyra（17 世纪史家）为阅读谱系次要条目**不入库**；《与流亡者的通信》13 位流亡作家（Zambrano/Alberti 等）仅书信往来**不入库**；1988 合影者无关系实载。

#### 4.5.1 入库操作

- 以 `name_en` 为中心写入 `person_relation`（yaml 路径见分批文件 `MySQL/data/Camilo_José_Cela.yaml`，引擎 `MySQL/seed_person.py`，幂等按 QID → name_en 匹配）
- 方向约定：`advisor-student` 有向（direction: advisor=对方是导师 / student=对方是学生）；`spouse` / `parent-child` / `colleague` / `influence` 无向（seed 自动 from<to 归一，yaml 勿写 direction）
- 对手方无库内记录时建 stub（不编造 qid，name_en 用规范全名）；库内已有同名记录按名幂等匹配并回填 QID；note 含 `: ` 须整体单引号包裹
- 校验：`SELECT COUNT(*) FROM person_relation WHERE from_id=<id> OR to_id=<id>`

- 校验本人物 relations 应为 4 行

### 第 5 步：设计配色 【人物专属】

- **主色**：深海军蓝 `#2A4B7C`（蜂房的冷峻与战后马德里的寒意）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgePasc` 帕斯夸尔·杜阿尔特 — 铁锈红 `#8B3A2E`
  - `badgeHive` 蜂房/群像 — 蜜蜡褐 `#B8860B`
  - `badgeTravel` 行旅 — 橄榄绿 `#556B2F`
  - `badgeExp` 实验/侯爵 — 石板灰 `#4A5568`
- **背景母题**：柔和气泡 + 蜂巢六边形稀疏网格（群像母题），行旅页转为黄土色带曲线。

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有肖像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明「肖像待补」。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 代表作 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧肖像 + 右侧信息网格，含至少：本名/笔名演变、生卒（含享年）、国籍、婚姻子女、教育与讲席任职、主要荣誉、核心领域。事实取自 page.md infobox 与正文，不得杜撰。
4. **文学家替代公式框**：代表作书影框 / 名句引文框 / 意象图式三选一——核心贡献页与诺奖页至少各出现一处；引语只允许使用第 7–8 步「引语白名单」内的条目，其余禁杜撰。
5. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenLiterature`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 蜂房与荒原 / Camilo José Cela 1916–2002 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（本名、生卒、国籍、爵位、学院席位、荣誉、核心领域）
03  核心贡献概览 — 战后小说 / 怪诞现实主义 / 群像蜂房 / 行旅与实验
04  早年：Iria Flavia 与疗养院 (1916–1935) — 九子之长、Vigo、马德里、肺结核、首作
05  内战岁月 (1936–1939) — 参军、Logroño 负伤
06  帕斯夸尔·杜阿尔特一家 (1942) — 暴力与冷漠、重塑战后小说（引文框①：获奖理由 EN 原文）
07  审查官与蜂房 (1943–1951) — 审查官身份、布宜诺斯艾利斯出版、本土遭禁（意象图式②：蜂巢群像）
08  行旅西班牙 (1948–1965) — Alcarria、Ávila、Castilla、安达卢西亚
09  学院与参政 (1957–1978) — Seat Q、王家参议员、1978 宪法措辞
10  实验转向 (1969–1988) — San Camilo 1936、Cristo versus Arizona 百页单句（书影框③）
11  词典与禁忌 (1968–1977) — Diccionario secreto、色情百科全书
12  1989 诺贝尔奖 — 获奖理由引文框 + Planeta/塞万提斯/侯爵
13  争议与晚年（客观简述）— 丑闻式发言、遗嘱之争
14  遗产 — 战后西班牙小说的方向塑造者、Iria Flavia 纪念
15  结尾
```

> 文学家无公式框：第 6/7/10/12 页用**代表作书影框 / 意象图式 / 获奖理由原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "for a rich and intensive prose, which with restrained compassion forms a challenging vision of man's vulnerability"，逐词照引禁止改写 |
| 政治内容红线 | 审查官、秘密警察线人、忠于佛朗哥政权：**只按 page.md 客观事实简述，不作政治评价、不展开政治叙事**；西班牙保守主义 portal 侧栏系维基导航框，与本人生平无涉禁写 |
| 粗俗内容红线 | 1998 年电视访谈言论、Lorca 百年纪念言论、"covered with shit" 塞万提斯奖评论——**粗俗原文一律禁引**，只客观转述「发表引发争议的不当言论/曾以粗俗言辞批评某奖」 |
| 《蜂房》出版地 | 1951 年首版于**布宜诺斯艾利斯**（因西班牙本土审查），勿写成马德里；「其名不得见于印刷媒体」是禁令细节 |
| 单句长篇 | *Cristo versus Arizona* 的单句**超过一百页**（more than one hundred pages），勿写成「整书一句」或「百字长句」 |
| 学院席位 | 1957-05-26 入选皇家西班牙语言学院 Seat Q，在任至去世（1957–2002），preceded by Rafael Estrada Arnaiz |
| 爵位 | 1996-05-17 封 Iria Flavia 第一代侯爵（世袭），身后传子 Camilo José Cela Conde；勿与出生地 Iria Flavia 混写 |
| 遗产份额 | 儿子 Conde 获遗产**三分之二**（遗嘱偏袒遗孀引发争议后经裁定），勿写成「儿子分文未得」 |
| Planeta 奖 | 1994 年获 Premio Planeta，注明「该奖客观性时受质疑」的 page.md 原注，勿写成单纯荣誉 |
| 两度同名 | *Oficio de tinieblas 5* 在书单中 1973 与 1989 两次出现（不同出版社版本），勿误作两部书 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| La familia de Pascual Duarte | 《帕斯夸尔·杜阿尔特一家》 | 1942，成名作 |
| La colmena | 《蜂房》 | 1951，三百余人群像 |
| Viaje a la Alcarria | 《阿尔卡里亚之旅》 | 1948，旅行文学 |
| San Camilo, 1936 | 《圣卡米洛，1936》 | 1969，实验转向起点 |
| Cristo versus Arizona | 《基督对亚利桑那》 | 1988，百页单句 |
| Diccionario secreto | 《秘密词典》 | 俚语禁忌词典，1968/1969–71 |
| tremendismo | 惨烈主义/怪诞现实主义 | 标签性术语，写「常被归入」 |
| Generation of '36 | '36 一代 | infobox 明载所属运动 |
| Real Academia Española | 皇家西班牙语言学院 | Seat Q，1957 |
| Marquess of Iria Flavia | Iria Flavia 侯爵 | 1996 世袭爵位 |
| Premio Cervantes | 塞万提斯奖 | 1995，态度有反复 |
| Piarist school | 比亚里学校 | 马德里中学教育 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（Alex-Productions）
- **风格标签**：沉稳 / 纪录片 / 长期纲领
- **匹配理由**：塞拉的创作生涯跨越六十年（1942–1999），从战后废墟写到百页单句——「长期纲领」匹配其一以贯之的怪诞现实主义文体自觉；「沉稳」匹配蜂房群像式的冷峻凝视；「纪录片」匹配从加利西亚村落到马德里审查局的生平行旅。以冷色深蓝配 Timeless，与「蜂房与荒原」的寒意一致。
- **备选**（未采用）：★★ Expedition —— 「远征/行旅」匹配《阿尔卡里亚之旅》的荒村行旅，但受众与沉稳感弱于 Timeless；★ The Flow of Time —— 时间感匹配六十年创作跨度，但受众偏低。
- **本地路径**：`music_audio/` 下 Alex-Productions Timeless（对照 `curated_tracks.md`）→ 复制到 `literature/presentations/20th_century/Camilo_José_Cela/Timeless.wav`。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Camilo_José_Cela/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Camilo_José_Cela/images.txt` | 内嵌图片 URL 清单（肖像第 0 步下载） |
| `literature/generate_20th_century_list.py` | 名录与获奖理由 CITATION_ZH（EN 原文+中译，禁止改写） |
| `literature/prompt_batches_lit.json` | 分批清单（qid/year/color/bgm 预分配） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `literature/presentations/cover/` | 统一封面 `\input` 模板 |
| `MySQL/data/Camilo_José_Cela.yaml` | 人物 fields + relations 入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 QID → name_en 匹配） |

> **开始执行。每完成一步汇报；无载禁写与政治内容红线是最高红线。**
