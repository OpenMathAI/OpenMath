# 工会领袖立传提示词（OpenPeace 批次 10 实例：Léon Jouhaux）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Léon Jouhaux（1951 诺贝尔和平奖，法国总工会总书记）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享体系，与 OpenPhysicist / OpenMedic 平级）。
- **本实例**：Léon Jouhaux（莱昂·茹奥）—— 法国工会领袖，1951 诺贝尔和平奖得主。
- **设计哲学**：和平奖得主（工会/社会正义类）与科学家立传的核心差异，在于必须有「身份信息页」，且叙事重心是「**车间里的和平主义**」——把工人权益斗争（八小时工作制、集体谈判）与反战和平事业串成一条线；「研究领域」用「事业领域」结构化表达，务必保留骨架。

---

## 二、背景信息 【人物专属】

- **目标人物**：Léon Jouhaux（1879-07-01 生于 Pantin（塞纳-圣但尼）~ 1954-04-28 卒于巴黎，享年 74 岁）
- **气质关键词**：**从火柴厂学徒到 CGT 总书记、布痕瓦尔德幸存者、以社会正义抗击战争的和平工会主义者**
- **诺奖**：1951 诺贝尔和平奖，获奖理由（Nobel 官方英文原文照抄）：
  > "for having devoted his life to the fight against war through the promotion of social justice and brotherhood among men and nations."（表彰他毕生通过促进社会正义与人人、国国之间的友爱来抗击战争）
- **设计母题**：**火柴与鸽羽（match & dove feather）**。其父被白磷灼瞎双眼的火柴厂，是他一生的起点——火柴既象征工人苦难也象征抗争火星；辅以鸽羽与集体谈判桌意象；柔和圆点背景呼应「社会正义是和平的地基」的核心信念。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Léon_Jouhaux/page.md`
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报。数据库同步要求：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库。
> **注意**：本条 page.md 较短（约 60 行），第 0 步事实基准已穷尽正文——**无载禁写**，严禁从诺奖颁奖词或外部知识扩充事实。

### 第 0 步：事实基准（第一轮已核对，勿改） 【人物专属】

- 生卒：1879-07-01 生于 Pantin（Seine-Saint-Denis）~ 1954-04-28 卒于巴黎，享年 74 岁；葬于巴黎拉雪兹神父公墓（Père Lachaise）
- 国籍：法国
- 家庭：父 Adolphe Jouhaux 在 Aubervilliers 火柴厂做工（因白磷灼瞎双眼）；中学学业因父亲罢工断薪而中断
- 教育：中学（因家困中断）；16 岁进火柴厂当工人
- 任职（含年份）：16 岁入火柴厂并即刻投身工会 → 1900 因兵役短暂赴法属阿尔及利亚，回国即参加反对白磷的罢工被解雇，经工会斡旋复职 → 1906 被地方工会选为法国总工会（CGT）代表 → 1909 任临时司库，旋即任 CGT 总书记，任职至 1947 → 二战中被捕，囚于布痕瓦尔德集中营，后转伊特尔城堡（Castle Itter），1945 伊特尔城堡战役中被美德两军（守军与进攻方）合力解救 → 战后脱离 CGT 另创社会民主派工会 Workers' Force（CGT-FO）→ 国际层面：ILO（国际劳工组织）创建的重要推手；国际工会联合会（IFTU）及其战后继承者世界工会联合会（WFTU，至其分裂）高层
- 关键荣誉：1951 诺贝尔和平奖；荣誉军团勋章（骑士级与军官级，infobox 合载）
- 工会目标清单（正文原列）：八小时工作制、工会代表权、集体谈判权、带薪休假
- 配偶：Catherine Metternich（1904–1946 婚姻）；Augustine Brüchlen（1946 年结婚）
- 关键时间线（15 节点）：1879 Pantin 生 / 少年时父亲被白磷灼瞎、家困辍学 / 16 岁入火柴厂入工会 / 1900 兵役+反白磷罢工被解雇后复职 / 1906 当选 CGT 代表 / 1909 临时司库→CGT 总书记 / 1904 与 Catherine Metternich 结婚 / 1914–1918 一战期间领导 CGT（正文仅作「组织抗议、反战立场与战时转向」的概述，细节无载勿扩）/ 1936 人民阵线、《马蒂尼翁协定》签署人（八小时工作制等权利落入法国工人之手）/ 1939–1945 被捕、布痕瓦尔德、伊特尔城堡、1945 获救 / 1947 任 CGT 总书记至该年、脱离 CGT 创立 CGT-FO / 1946 与 Augustine Brüchlen 结婚 / ILO 创建的关键推动者 / 1951 诺贝尔和平奖（12-11 诺奖演讲 *Fifty Years of Trade-Union Activity in Behalf of Peace*）/ 1954-04-28 卒、葬拉雪兹公墓
- 遗产：Aix-en-Provence、Grenoble、Lyon、Genas、Villefranche-sur-Saône、Paris 六城的 rue Léon Jouhaux 以其命名

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/Léon_Jouhaux/` 下建 `images/`；Makefile 设 `MAIN=Leon_Jouhaux_zh`、`VIDEO_NAME=Leon_Jouhaux_zh`（文件名建议用 ASCII 变体 `Leon_Jouhaux_zh.tex`，规避 LaTeX 对 é 的路径风险；Makefile MAIN 与文件名一致即可）
- 肖像：正文图有 1933 年正装肖像（Léon Jouhaux 1933.jpg，Wikimedia Commons）——直接下载使用，404 则经 Wikipedia REST API 查 infobox 原图名，仍 404 用装饰圆占位并核对图注

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | trade unionism | 工会运动 | CGT 总书记 1909–1947、CGT-FO 创立 | 生平页 |
| 1 | labour rights | 劳工权利 | 八小时工作制、集体谈判、带薪休假 | 生平页 |
| 2 | social justice | 社会正义 | 诺奖理由的核心措辞 | 获奖页 |
| 3 | international labour movement | 国际劳工运动 | ILO 创建推手、IFTU/WFTU 高层 | 国际页 |
| 4 | peace activism | 和平运动 | 以社会正义促进兄弟情谊抗击战争 | 获奖页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Adolphe Jouhaux | 子→父 | 父亲，Aubervilliers 火柴厂工人，因白磷灼瞎双眼 |
| spouse | Catherine Metternich | 无向 | 1904–1946 婚姻 |
| spouse | Augustine Brüchlen | 无向 | 1946 结婚，相伴至终 |

- 方向约定：spouse / colleague / co-honored 无向（seed 幂等归一 from<to），parent-child 用 direction: parent（对方是父亲）
- 不入库（无载或无类型可归）：1936《马蒂尼翁协定》其他签署人（page.md 未具名）、CGT/CGT-FO 继任者（未具名）、ILO/IFTU/WFTU 同僚（未具名）——page.md 全文未具名任何同侪对手，**relations=3 即诚实值，勿强凑**

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：车间的粗粝、工人的执拗、和平者的宽厚
- **配色**：主色深海军蓝 `#16324F`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeUnion` 工会运动 — 香槟金 `#C9A227`
  - `badgeLabour` 劳工权利 — 靛 `#4C5FD5`
  - `badgeJustice` 社会正义 — 青绿 `#0E7C7B`
  - `badgeIntl` 国际劳工 — 琥珀 `#E07B30`
- **背景母题**：柔和圆点，疏朗坚毅，呼应车间火星与鸽羽并置的「斗争与和平同源」意象

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）；2. 封面明示国籍与 `国籍 | 机构 | 主要奖项` 状态栏；3. **必须有身份信息页**（左头像 + 右信息网格：生卒、本名、国籍、出生地、教育、任职、荣誉、核心事业）；4. 品牌口径统一 `OpenMathAI`，引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，13 页规划】

```
00  OpenPeace 项目首页（\input cover 封面）
01  封面 — 车间里的和平主义者 / Léon Jouhaux 1879–1954 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  事业概览 — 工会运动 / 劳工权利 / 国际劳工 / 和平
04  早年：白磷之痛 (1879–1906) — Pantin、火柴厂、父亲失明、反白磷罢工
05  CGT 总书记 (1906–1914) — 从地方代表到 1909 总书记
06  工会的目标 — 八小时工作制、集体谈判、带薪休假（核心页之一）
07  人民阵线与《马蒂尼翁协定》(1936) — 签署人身份与权利落地
08  战争与集中营 (1939–1945) — 布痕瓦尔德、伊特尔城堡、1945 获救
09  分裂与重建 (1947) — 脱离 CGT、创立 CGT-FO
10  国际劳工舞台 — ILO 创建推手、IFTU 与 WFTU 高层（核心页之一）
11  1951 诺贝尔和平奖 — 理由、诺奖演讲 Fifty Years of Trade-Union Activity in Behalf of Peace
12  遗产：六城同名街巷 + 结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；每写完一页 `make`，`pdftoppm` 目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。
- **短页面对策**：正文素材有限，宁可 13 页内留白从容，不可为凑页数扩写无载内容；一页一个主题，信息密度宁低勿虚。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Jouhaux 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 页面短小 | page.md 仅约 60 行，所有事实以上文第 0 步清单为限；禁从诺奖颁奖词、CGT 会史等外部知识补料 |
| 引语唯一 | 全文仅一条引语 "I would not go so far as to say that the French trade unions attached greater importance to the struggle for peace than the others did; but they certainly seemed to take it more to heart."——除此之外禁编任何引语 |
| 总书记任期 | CGT 总书记 1909–1947（正文口径 "held until 1947"）；1947 脱离 CGT 创立 CGT-FO——两个 1947 勿混为一事 |
| 伊特尔获救 | 囚于布痕瓦尔德后转 Castle Itter，1945 伊特尔城堡战役中「被美德两军解救」（守军德军与进攻美军罕见的并肩，正文口径如此）——客观转述勿戏剧化 |
| 父亲失明 | 因火柴厂白磷灼瞎双眼——这是他 1900 反白磷罢工的个人动因，两处事实要连成线 |
| 一战立场 | 正文只有三句：战前组织大规模抗议且其组织反对战争；开战后支持国家（认为纳粹德国胜利将摧毁欧洲民主）；被捕入营——禁扩写「左派爱国主义论战」等无载内容 |
| 政治红线 | 工会分裂（CGT vs CGT-FO）、共产主义/社会民主派分歧等只作 page.md 明载的客观事实记录，禁任何意识形态评价 |
| 婚姻两段 | Catherine Metternich（1904–1946）→ Augustine Brüchlen（1946–）；两段都入库 spouse，叙事页按时间并列即可 |
| 同名区分 | 勿与 Georges Sorel、Benjamin Péret 等法国工运人物混淆；姓氏 Jouhaux 勿误拼 Jouaux/Jouhaud |
| 文件名 | 提示词/目录名保留 é（Léon_Jouhaux），tex/Makefile 建议用 ASCII 变体 Leon_Jouhaux_zh，两者在 Makefile MAIN 中对齐 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| General Confederation of Labour (CGT) | 法国总工会 | 1906 入会、1909 总书记 |
| Workers' Force (CGT-FO) | 法国工人民主联合会（工人力量） | 1947 创立，社会民主派 |
| Matignon Agreements (1936) | 《马蒂尼翁协定》 | 人民阵线产物，其为签署人 |
| Popular Front | 人民阵线 | 1936 法国政治联盟 |
| International Labour Organization (ILO) | 国际劳工组织 | 其创建的重要推手 |
| International Federation of Trade Unions (IFTU) | 国际工会联合会 | 战前国际工会组织 |
| World Federation of Trade Unions (WFTU) | 世界工会联合会 | 战后继承者，「至其分裂」 |
| eight-hour day | 八小时工作制 | 工会目标清单之一 |
| collective bargaining | 集体谈判权 | 工会目标清单之一 |
| white phosphorus | 白磷 | 火柴厂职业病之源 |
| Buchenwald | 布痕瓦尔德集中营 | 二战囚禁地 |
| Castle Itter | 伊特尔城堡 | 1945 获救地 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **New Lands** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 前行感 / 电子律动 / 破土新生
- **匹配理由**: "New Lands"呼应 CGT-FO 的另立门户与战后国际劳工新秩序（ILO/WFTU）的开拓——旧阵地破碎后开垦新大陆的工会人生；律动的行进感匹配从火柴厂车间到拉雪兹公墓之间五十年不停歇的组织者生涯。
- **本地路径**: `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav` → 复制为 `presentations/20th_century/Léon_Jouhaux/New Lands.wav`
- **时长**: 以实际文件为准 → ffmpeg `-shortest` 自动对齐 13 页 × 7 秒 ≈ 91 秒

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Léon_Jouhaux/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译口径 |
| `MySQL/data/Léon_Jouhaux.yaml` | 入库 yaml（第 4 / 4.5 步落地） |
| `MySQL/seed_person.py` | 幂等入库引擎 |
| `music_audio/curated_tracks.md` | BGM 曲库 |

- **备选** (未采用):
  - ★★ Expedition — 「行进」匹配工会组织者的动员生涯，但朝向前行明亮，与集中营经历的沉郁不称
  - ★ The Invisible Light — 「微光」匹配车间火星意象，但整体氛围偏冷，弱于 New Lands 的重建感

---

## 六、数据库落地命令 【模板通用】

- **yaml**: `MySQL/data/Léon_Jouhaux.yaml`（第 4 步事业领域表与第 4.5 步关系表为其唯一事实来源）
- **入库**（幂等；撞 fields/occupations 字典表唯一键时等 2 秒重跑一次）：

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Léon_Jouhaux.yaml
```

- **验证**（要求 `has_social_data=1`、fields≥4、relations≥2）：

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 -c "
from db_mysql import get_conn
conn=get_conn(); cur=conn.cursor()
cur.execute(\"SELECT id,name_en,has_social_data FROM people WHERE qid='Q155415'\")
p=cur.fetchone(); print(p)
cur.execute('SELECT COUNT(*) FROM person_field WHERE person_id=%s',(p[0],)); print('fields:',cur.fetchone()[0])
cur.execute('SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s',(p[0],p[0])); print('relations:',cur.fetchone()[0])"
```

- **本实例参考值**: 已入库 id=7133，fields=5，relations=3（父 1 + 两任配偶 2）——**page.md 全文未具名任何同侪对手，relations=3 为诚实值**，严禁为凑数扩写。
- **注意事项**: 父 Adolphe Jouhaux 的 parent-child 用 direction: `parent`（对方是父亲）；yaml 文件名保留 é（Léon_Jouhaux.yaml），与 manifest 一致。

> **开始执行。每完成一步汇报。**
> **最重要的事：本条页面短小，无载禁写从严；每写一页就 make，看到溢出就修。**
