# 政治家/科学家立传提示词（OpenPeace 批次 10 实例：Lord Boyd-Orr）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 John Boyd Orr, 1st Baron Boyd-Orr（1949 诺贝尔和平奖，FAO 首任总干事）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享体系，与 OpenPhysicist / OpenMedic 平级）。
- **本实例**：John Boyd Orr, 1st Baron Boyd-Orr（约翰·博伊德·奥尔，博伊德-奥尔男爵一世，CH DSO MC FRS FRSE）。
- **设计哲学**：和平奖得主（营养科学家/国际组织缔造者类）与科学家立传的核心差异，在于必须有「身份信息页」，且叙事重心是「**从实验室到世界粮政**」——把营养科学研究与反饥饿的国际政治行动串成一条线；「研究领域」用「事业领域」结构化表达，务必保留骨架。

---

## 二、背景信息 【人物专属】

- **目标人物**：John Boyd Orr（1880-09-23 生于苏格兰艾尔郡 Kilmaurs ~ 1971-06-25 卒于苏格兰安格斯 Brechin，享年 90 岁）
- **气质关键词**：**战胜饥饿的战士、从村小教师到 FAO 首任总干事、把营养学变成和平武器的实用主义者**
- **诺奖**：1949 诺贝尔和平奖，获奖理由（Nobel 官方英文原文照抄）：
  > "for his lifelong effort to conquer hunger and want, thereby helping to remove a major cause of military conflict and war."（表彰他毕生致力于战胜饥饿与匮乏，从而帮助消除军事冲突与战争的一大根源）
- **设计母题**：**面包与橄榄枝（bread & olive branch）**。其家族纹章铭言即 *Panis Et Pax*（面包与和平）——视觉语言采用麦穗、面包、天平与地球粮仓意象；柔和圆点背景呼应「粮食充足是和平地基」的核心信念。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/John_Boyd_Orr_1st_Baron_Boyd-Orr/page.md`
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报。数据库同步要求：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库。

### 第 0 步：事实基准（第一轮已核对，勿改） 【人物专属】

- 生卒：1880-09-23 生于 Kilmaurs（East Ayrshire）~ 1971-06-25 卒于 Brechin（Angus），享年 90 岁；葬 Stracathro Kirkyard（Angus）
- 国籍：英国（苏格兰人）
- 家庭：父 Robert Clark Orr（采石场主，苏格兰自由教会成员）；母 Annie Boyd；七兄弟姐妹中排行居中；5 岁时家船沉没迁 West Kilbride
- 教育：West Kilbride 村小（后四年为 pupil-teacher）→ 13 岁获奖学金入 Kilmarnock Academy（四个月后因家计中断回村小）→ 19 岁获 Queen's Scholarship 入格拉斯哥：MA 1902（古典学三年课程）、BSc 1910、MB ChB 1912（200 名学生中列第 6）、MD 1914 优等（Bellahouston Gold Medal 最佳论文）
- 任职（含年份）：Saltcoats Kyleshill School 教师 3 年 → 船医 4 个月（偿清银行透支）→ Carnegie 研究奖学金入 E. P. Cathcart 实验室（蛋白质/肌酸代谢）→ 1914-04-01 出任阿伯丁新动物营养研究所所长（1922 年获 Rowett 捐款后更名 Rowett Research Institute）→ 一战 RAMC 军医（Somme 后获 Military Cross，Passchendaele 后获 DSO）→ 1929–1944 帝国动物营养局顾问主任 → 二战入 Churchill 食品政策科学委员会 → 1945-04 当选 Combined Scottish Universities 议员（1946 辞职）→ 1945-10 当选格拉斯哥大学 Rector → FAO 首任总干事 1945–1948 → 多家公司董事与股市投资
- 关键荣誉：1949 诺贝尔和平奖；Military Cross（1916 索姆河后）；Distinguished Service Order（1917 帕斯尚尔后）；FRSE 1924；FRS 1932；1935 New Year Honours 爵士；1949 New Year Honours 封 Baron Boyd-Orr（of Brechin Mearn）；Bellahouston Gold Medal；Companion of Honour
- 配偶：Elizabeth Pearson Callum（1915 结婚，West Kilbride 少年时相识）；子女 3 人：Elizabeth Joan（1916 生）、Helen Anne（1919 生）、Donald Noel（1921–1942，二战服役阵亡）
- 核心事业清单：①Rowett 研究所的创建与扩建（自掏预算方案 + 向 Rowett 募款）②1927 年证明学生奶价值→英国免费学生奶政策③1936 报告 *Food, Health and Income*（至少三分之一英国人吃不起健康饮食）④FAO 首任总干事：战后粮荒应急 + 世界粮食委员会（World Food Board）提案（未获英美支持）⑤1949 诺奖奖金全部捐给世界和平与世界政府组织⑥1960 世界艺术与科学院（WAAS）共同创始人兼首任主席（1960–1971）
- 关键时间线（16 节点）：1880 Kilmaurs 生 / 1893 Kilmarnock Academy 奖学金 / 1899–1902 格拉斯哥师范 + MA / 1902 贫民窟学校任教数日即辞职 / 1910 BSc / 1912 MB ChB / 1914 MD 金奖 + 4 月出任阿伯丁研究所所长 / 1914–1918 一战军医（MC、DSO） / 1920 结识 John Quiller Rowett 获 10+10+2 千镑捐款 / 1922 更名 Rowett Research Institute（Queen Mary 揭幕） / 1927 学生奶研究→免费学生奶 / 1935 爵士 / 1936 *Food, Health and Income* / 1945 议员+Rector+FAO 首任总干事 / 1946–1948 World Food Board 提案受挫、辞 FAO / 1949 诺奖+封男爵（奖金全捐） / 1957 国际人文主义大会主席 / 1960 WAAS 首任主席 / 1971 卒于 Brechin

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/John_Boyd_Orr_1st_Baron_Boyd-Orr/` 下建 `images/`；Makefile 设 `MAIN=John_Boyd_Orr_1st_Baron_Boyd-Orr_zh`、`VIDEO_NAME=John_Boyd_Orr_1st_Baron_Boyd-Orr_zh`
- 肖像：page.md infobox 无直链肖像；正文图有出生故居照片；Further reading 载 NPG 藏 1949 Lida Moser 照片、1953 W. Stoneman 底片、Elliott & Fry 1942 照片等——优先经 NPG/Wikipedia REST API 查 infobox 原图名下载，404 则用出生故居照或装饰圆占位并核对图注

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | human nutrition | 人类营养学 | *Food, Health and Income*、学生奶、战时配给 | 研究页 |
| 1 | animal nutrition | 动物营养学 | Rowett 研究所本职研究 | 研究所页 |
| 2 | physiology | 生理学 | Cathcart 实验室的蛋白质/肌酸代谢研究 | 早年页 |
| 3 | medicine | 医学 | MB ChB 1912、MD 1914、一战军医 | 医学页 |
| 4 | world food policy | 世界粮食政策 | FAO 首任总干事、World Food Board 提案 | FAO 页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Edward Provan Cathcart | 师→生 | 格拉斯哥生理化学主任，Carnegie 奖学金导师与一生同事，Rowett 所长职亦因其荐 |
| spouse | Elizabeth Pearson Callum | 无向 | 1915 结婚，少年时相识于 West Kilbride |
| parent-child | Elizabeth Joan Orr | 父→子 | 长女，1916 生 |
| parent-child | Helen Anne Orr | 父→子 | 次女，1919 生 |
| parent-child | Donald Noel Orr | 父→子 | 独子 1921–1942，二战服役阵亡 |
| founder | World Academy of Art and Science | 无向 | 共同创始人兼首任主席（1960–1971） |
| colleague | Albert Einstein | 无向 | 同为 Peoples' World Convention (PWC, 1950–51 日内瓦) 发起赞助人 |
| colleague | Bertrand Russell | 无向 | Russell 主持的 Who Killed Kennedy 委员会成员 |

- 方向约定：advisor-student 有向（direction: advisor），parent-child 用 direction: child（对方是子女），其余无向（seed 幂等归一 from<to）
- 不入库（无类型可归或仅事件性）：John Quiller Rowett（捐款恩人，无对应关系类型，仅在叙事页呈现）、Thomas Barlow Wood、Diarmid Noel Paton、Samson Gemmell（大学师长，未达导师关系明载标准）、Isabella Leitch（助理）、Ritchie Calder（回忆录作序）、世界联邦运动等组织任职

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：苏格兰的务实、科学家的执着、国际主义者的博大
- **配色**：主色深湖蓝 `#1B4D6B`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeFood` 粮食政策 — 香槟金 `#C9A227`
  - `badgeNutri` 营养科学 — 湖蓝 `#1B4D6B`
  - `badgeRowett` Rowett 研究所 — 青绿 `#0E7C7B`
  - `badgeWar` 战时服务 — 琥珀 `#E07B30`
- **背景母题**：柔和圆点，疏朗沉稳，呼应麦浪与地球粮仓的「饱足即和平」意象

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）；2. 封面明示国籍与 `国籍 | 机构 | 主要奖项` 状态栏；3. **必须有身份信息页**（左头像 + 右信息网格：生卒、本名、国籍、出生地、教育、任职、荣誉、核心事业）；4. 品牌口径统一 `OpenMathAI`，引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，15 页规划】

```
00  OpenPeace 项目首页（\input cover 封面）
01  封面 — 战胜饥饿的人 / John Boyd Orr 1880–1971 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  事业概览 — 营养科学 / Rowett / FAO / 和平组织
04  早年：采石场主的儿子 (1880–1899) — Kilmaurs、村小 pupil-teacher、Kilmarnock Academy
05  格拉斯哥岁月 (1899–1914) — 贫民窟震撼、MA/BSc/MB ChB/MD、Cathcart 门下
06  Rowett 研究所的诞生 (1914) — 自掏 5 万镑预算方案与 fait accompli
07  一战军医 (1914–1918) — 索姆河 MC、帕斯尚尔 DSO、菜园防疫的营级经验
08  学生奶与《食物、健康与收入》(1919–1937) — 1927 学生奶、1936 三分之一国民吃不起健康饮食（核心页之一）
09  战时粮政 (1939–1945) — Churchill 食品政策科学委员会、配给制、议员与 Rector
10  FAO 首任总干事 (1945–1948) — IEFC 应急 + World Food Board 提案受挫（核心页）
11  1949 诺贝尔和平奖 — 理由、奖金全捐、封爵
12  和平机构缔造者 — PWC 与 Einstein、世界人文主义大会、WAAS 首任主席
13  面包与橄榄枝 — Panis Et Pax 纹章铭言与遗产（Boyd Orr Building、诺贝尔奖章藏 Hunterian 博物馆）
14  结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；每写完一页 `make`，`pdftoppm` 目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Boyd-Orr 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 卒地两说 | infobox 作 Edzell（Angus），正文 Death and legacy 作 Brechin——统一写 Brechin（正文口径），可注「Angus 郡」；勿写 Edzell |
| 头衔演变 | 1935 爵士（Sir John Boyd Orr）、1949 封男爵（Baron Boyd-Orr, of Brechin Mearn）；诺奖获奖名单作 Lord Boyd-Orr；叙事中 1935 前禁用 Sir |
| 诺奖理由 | 官方理由是「毕生战胜饥饿与匮乏的努力」——FAO 工作与营养研究是支撑，但理由句勿改写成「因创建 FAO」 |
| AFSC 关系 | 注释脚注载 AFSC 是其诺奖**提名人之一**——提名人非社会关系类型，不入库、幻灯片最多一句带过 |
| Rowett 关系 | John Quiller Rowett 是捐款人（1930 自杀背景 page.md 未载禁写）， institute 以其命名；无关系类型可归，勿建 founder/colleague 行 |
| World Food Board | 提案未获英美支持而失败——失败结局要写，勿写成「创立了世界粮食委员会」 |
| 议员任期 | 1945-04 补选当选、同年大选连任、1946 辞职——不足两年，勿写「战后长期议员」 |
| 军功年代 | MC 因索姆河战役（1916）、DSO 因帕斯尚尔战役（1917）——勿互换；1918-05-05 正式授上尉军衔 |
| 子女 | 独子 Donald Noel 二战阵亡（1921–1942）——家史沉痛一笔，勿遗漏也勿渲染 |
| 引语 | "I still look with bitter resentment at having to spend half my time in the humiliating job of hunting for money for the Institute." 为 page.md 有英文原文的唯一自述引语；Shakespeare 注脚引语可转述；其余禁编 |
| 同名区分 | 勿与 Robert W. Boyd 等混淆；「Boyd-Orr」连字符是封号后写法，早年生平用 John Boyd Orr |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Rowett Research Institute | 罗威特研究所 | 1922 更名，纪念捐款人 Rowett |
| Food and Agriculture Organization (FAO) | 联合国粮食及农业组织 | 首任总干事 1945–1948 |
| World Food Board | 世界粮食委员会 | 提案未成，勿写成已建成 |
| International Emergency Food Committee | 国际紧急粮食委员会 | 战后粮荒应急机构 |
| Food, Health and Income | 《食物、健康与收入》 | 1936 报告 |
| pupil-teacher | 见习教师 | 苏格兰师范体系 |
| Military Cross / DSO | 军功十字勋章 / 杰出服务勋章 | 分别因索姆河/帕斯尚尔 |
| Panis Et Pax | 面包与和平 | 家族纹章铭言 |
| World Academy of Art and Science | 世界艺术与科学院 | 1960 共同创立 |
| Rector of the University of Glasgow | 格拉斯哥大学校长（学生选出） | 1945 当选 |
| Combined Scottish Universities | 苏格兰大学联合选区 | 1945 补选议席 |
| free school milk | 免费学生奶 | 1927 研究的政策后果 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Falling Apart** — Michael FK & Andy Leech（manifest 预分配，勿改）
- **风格**: 沉郁 / 后摇式铺陈 / 废墟中的重建感
- **匹配理由**: "Falling Apart"呼应其事业的两条暗线——战后满目疮痍的世界粮荒（FAO 应急）与独子 Donald Noel 二战阵亡的家国之痛；曲名的破碎感与其在废墟上建粮政、建研究所、建和平机构的重建意志形成张力，恰好构成「从饥饿的废墟到和平的地基」的叙事弧。
- **本地路径**: `music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav` → 复制为 `presentations/20th_century/John_Boyd_Orr_1st_Baron_Boyd-Orr/Falling Apart.wav`
- **时长**: 以实际文件为准 → ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/John_Boyd_Orr_1st_Baron_Boyd-Orr/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译口径 |
| `MySQL/data/John_Boyd_Orr_1st_Baron_Boyd-Orr.yaml` | 入库 yaml（第 4 / 4.5 步落地） |
| `MySQL/seed_person.py` | 幂等入库引擎 |
| `music_audio/curated_tracks.md` | BGM 曲库 |

- **备选** (未采用):
  - ★★ The Flow of Time — 「时间纵深」匹配从村小到 FAO 的六十年长程，但与「独子阵亡」的沉郁底色契合度略逊
  - ★ Pathfinder — 「开拓者」匹配世界粮政首创，但气质偏明亮，弱于废墟重建的叙事张力

---

## 六、数据库落地命令 【模板通用】

- **yaml**: `MySQL/data/John_Boyd_Orr_1st_Baron_Boyd-Orr.yaml`（第 4 步事业领域表与第 4.5 步关系表为其唯一事实来源）
- **入库**（幂等；撞 fields/occupations 字典表唯一键时等 2 秒重跑一次）：

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/John_Boyd_Orr_1st_Baron_Boyd-Orr.yaml
```

- **验证**（要求 `has_social_data=1`、fields≥4、relations≥2）：

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 -c "
from db_mysql import get_conn
conn=get_conn(); cur=conn.cursor()
cur.execute(\"SELECT id,name_en,has_social_data FROM people WHERE qid='Q315143'\")
p=cur.fetchone(); print(p)
cur.execute('SELECT COUNT(*) FROM person_field WHERE person_id=%s',(p[0],)); print('fields:',cur.fetchone()[0])
cur.execute('SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s',(p[0],p[0])); print('relations:',cur.fetchone()[0])"
```

- **本实例参考值**: 已入库 id=6958，fields=5，relations=8（advisor 1 + spouse 1 + 子女 3 + founder 1 + colleague 2）；对手方 `Albert Einstein` 沿用库内既有记录（id=349）、`Bertrand Russell`（id=74），零分裂。
- **注意事项**: 子女 direction 用 `child`（对方是子女）；`World Academy of Art and Science` 为库内新建机构 stub，name_en 用 page.md 原文全称。

> **开始执行。每完成一步汇报。**
> **最重要的事：无载禁写；每写一页就 make，看到溢出就修。**
