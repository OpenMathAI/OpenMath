# 和平奖得主立传提示词（OpenPeace · Médecins Sans Frontières，组织机构篇）

> **本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」**，以 Médecins Sans Frontières（无国界医生，1999 诺贝尔和平奖，本篇为组织机构实例）。
> 结构对齐物理学家侧标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节），并按 OpenPeace 工作流第 2 节执行组织机构特别规则。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库）。
- **本实例**：Médecins Sans Frontières（MSF，无国界医生）——国际人道医疗非政府组织，本篇为 **组织机构立传**。
- **设计哲学**：机构篇以「机构概览页」替代人物「身份信息页」；强调「使命领域」的结构化表达；切勿把机构领导人写成创始人。

---

## 二、背景信息 【机构专属】

- **目标机构**：Médecins Sans Frontières（MSF，1971-12-22 成立于巴黎）
- **获奖**：1999 诺贝尔和平奖，官方获奖理由：
  > "in recognition of the organization's pioneering humanitarian work on several continents."
  > （中译照抄名录：表彰该组织在多个大洲的开创性人道主义工作）
- **气质关键词**：**无国界的急诊室、见证的伦理、独立的人道主义**
- **设计母题**：**红线与界线（the crossed border）**。MSF 的名字本身就是「跨越国界」——视觉母题用被红线划过的地图边界/医药箱，表达「医疗援助无视种族、宗教、教派与政治归属」的建会初心。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Médecins_Sans_Frontières/page.md`（Wikipedia 全文 + frontmatter，事实基准唯一来源）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - OpenPeace 项目首页：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【机构专属，第一轮已核对】

- **成立**：1971-12-22，巴黎（由 Biafra 之殇的 Groupe d'intervention médicale et chirurgicale en urgence 与 Raymond Borel 的 Secours Médical Français 两组合并而成）；总部今在日内瓦，六个行动中心（阿姆斯特丹 OCA、巴塞罗那-雅典 OCBA、布鲁塞尔 OCB、巴黎 OCP、日内瓦 OCG、西非与中非 WaCA）。
- **机构性质**：国际非政府组织（NGO），法语名意为「无国界医生」；对联合国经社理事会具一般咨商地位；私人捐助约占经费 98%；2024 年在 75+ 国家开展项目、人员 67,000+（2025 年 49,771 名雇员，年收支约 26/25 亿欧元）。
- **创始背景**：1967–1970 尼日利亚内战（比夫拉封锁）期间，一批在法国红十字会志愿的法国医生目睹平民被屠杀与饿毙、公开批评后认定需要新组织；1970 Bhola 气旋（东巴基斯坦，死亡 62.5 万+）促成 Borel 组队。
- **创始名单（正文「Original founders」节明载 13 人）**：Jacques Bérès、Philippe Bernier、Raymond Borel、Jean Cabrol、Marcel Delcourt、Xavier Emmanuelli、Pascal Grellety Bosviel、Gérard Illiouz、Bernard Kouchner、Gérard Pigeon、Vladan Radoman、Max Récamier、Louis Schittly（Kouchner 后入法国政坛，2007–2010 任外交部长）。
- **行动里程碑**：首项任务 1972 马那瓜地震（尼加拉瓜）；1974 飓风 Fifi（洪都拉斯）首个长期任务；1975–1979 泰国首个难民营任务；1976–1984 黎巴嫩内战九年战地手术（中立声誉）；1979-12 苏联入侵阿富汗后即设医疗任务；1980-02 公开谴责红色高棉；1984–1985 埃塞俄比亚饥荒营养项目（因谴责滥用援助与强制迁徙被驱逐，引发法国人道伦理大辩论）；1990s 利比里亚、库尔德难民、索马里、波黑斯雷布雷尼察（1993–1995 唯一提供医疗的组织）；1994 卢旺达大屠杀（与 ICRC 维持基加利主要医院运转，本方近 100 名当地员工罹难；此后其中立立场向 ICRC 靠拢）；1999 车臣谴责但不再要求军事干预。
- **治理**：国际理事会协调 24 个协会（国家办公室）核心政策；国际主席沿革（page.md 列表）：Rony Brauman（1991–1994 两任）、Jacques De Milliano、Doris Schopper、Philippe Biberson、James Orbinski（1998–2000，1999 代表领奖并发表诺奖演说）、Morten Rostrup、Rowan Gillies、Christophe Fournier、Unni Karunakara、Joanne Liu（2013–2019）、Christos Christou（2019–2025）、Javid Abdelmoneim（2025–）；CEO Tirana Hassan。
- **关键荣誉**：Nobel Peace Prize 1999；Seoul Peace Prize 1996（获奖前）；Lasker–Bloomberg Public Service Award 2015；Hamdan 志愿人道医疗服务奖 2016；frontmatter 另载 Indira Gandhi Peace Prize、阿斯图里亚斯亲王和谐奖、欧洲人权奖、Nansen 难民奖、LennonOno Grant for Peace、Fulbright Prize 等。
- **机构概览要素清单（机构概览页★必做用）**：成立日期/地点、性质（国际 NGO）、总部与六行动中心、使命原则（宪章、Chantilly 原则、La Mancha 协议）、 témoignage（见证）传统、资金结构（98% 私人捐助）、1999 诺奖与 Orbinski 演说。
- **关键时间线（15 节点）**：1967–1970 比夫拉封锁 → 1970 Bhola 气旋 → 1971-12-22 两组合并成立 MSF → 1972 马那瓜首项任务 → 1974 洪都拉斯长期任务 → 1975–1979 泰国难民营 → 1976–1984 黎巴嫩战地九年 → 1977 Malhuret 任主席、témoignage 路线之争 → 1979「越南之船」事件与 Kouchner 另立门户 → 1982 Brauman 任主席、邮募筹资专业化 → 1980s 各国分部相继建立 → 1985 被埃塞俄比亚驱逐 → 1994 卢旺达大屠杀 → 1999 诺贝尔和平奖 → 2020 内部反种族主义请愿 → 2024 关闭药品可及运动。

### 第 4 步：使命领域梳理 + 入库 【模板通用，机构专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | humanitarian aid | 人道主义援助 | 建会使命总纲，1999 诺奖核心 | 概览页 |
| 1 | medical care | 医疗照护 | 冲突地区与疫病流行国的急诊医疗 | 医疗页 |
| 2 | refugee relief | 难民救济 | 泰国首营至地中海搜救 | 行动页 |
| 3 | neglected diseases | 被忽视疾病 | 蛇伤列入 WHO A 类、耐药结核等 | 行动页 |
| 4 | access to medicines | 药品可及 | 专项运动（2024 关闭另设新机制） | 治理页 |

### 第 4.5 步：社会关系梳理 + 入库 【机构专属，与 yaml 完全一致】

| 关系类型 | 对方（name_en） | 方向 | note |
|---------|------|------|------|
| founder | Bernard Kouchner | 无向 | 13 位创始人之一，比夫拉志愿医生出身 |
| founder | Raymond Borel | 无向 | Secours Médical Français 发起人，两组合并成 MSF |
| colleague | James Orbinski | 无向 | 1998–2000 国际主席，1999 代表领奖并演说 |
| colleague | Rony Brauman | 无向 | 1982 起任主席，推动专业化与筹资独立 |
| colleague | Claude Malhuret | 无向 | 1977 任主席，témoignage 路线之争 |
| other | Médecins du Monde | 无向 | 1979 Kouchner 等人另立的机构，非前身继承关系 |

### 第 5 步：设计配色方案 【模板通用，机构专属色彩】

- **气质**：急迫、克制、独立
- **配色**：主色深海蓝 `#0E4D64`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` 人道援助 — 深青 `#0E7490`
  - `badgeB` 医疗照护 — 靛蓝 `#4C5FD5`
  - `badgeC` 难民救济 — 琥珀 `#E07B30`
  - `badgeD` 见证/倡导 — 玫瑰 `#C4204F`
- **背景母题**：被红线划过的地图边界（呼应「跨越国界」母题）。

### 第 6 步：规划幻灯片序列 【机构专属，13 页；机构概览页替代身份信息页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 无国界医生 / Médecins Sans Frontières 1971– + 四色 badge + 「国际组织」标注
02  机构概览页（★ 必做）— 成立/总部/六行动中心/资金结构/使命原则/诺奖
03  比夫拉之殇 (1967–1970) — 封锁、法国红会志愿医生、公开批评
04  1971 成立 — 两组合并、13 位创始人
05  早期行动 (1972–1979) — 马那瓜、Fifi 飓风、泰国难民营
06  黎巴嫩九年 (1976–1984) — 战地手术、中立声誉
07  路线之争与专业化 (1977–1986) — témoignage、Kouchner 分裂、Brauman 改革
08  1980s 大洲行动 — 阿富汗、谴责红色高棉、埃塞俄比亚驱逐
09  1990s — 利比里亚、斯雷布雷尼察、卢旺达大屠杀
10  1999 诺贝尔和平奖 — Orbinski 演说、沉默会杀人
11  遗产与扩张 — 无国界系组织、MUAC「生命手环」入 MoMA
12  治理与今日 — 24 国协会、六行动中心、2020s 事件
13  结尾
```

### 第 7 步：版式要点 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；机构概览页信息网格参照标杆 `\profileslide` 改造。
- 每写完一页 `make` 编译，`pdftoppm` 截图检查溢出；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距。

### 第 8 步：专属陷阱表 【机构专属，红线】

| 陷阱 | 说明 |
|------|------|
| 政治敏感红线 | 各战区/各方行为只按 page.md 客观记录（如斯雷布雷尼察、卢旺达、车臣、加沙停摆、香港争议节），禁评价性语句、禁站队 |
| 勿把领导人写成创始人 | Kouchner/Borel 是 13 位创始人中有正文专述者；历任国际主席（Brauman/Orbinski 等）是领导人，禁写成 founder |
| 创始人全名单 | 「Original founders」节明载 13 人全名；关系表仅入 Kouchner+Borel 两人防噪声，其余在提示词层保留 |
| Médecins du Monde | 是 1979 Kouchner 另立的机构（分裂），非 MSF 前身或继承——type: other + note 注明「非前身继承关系」 |
| 1999 授奖人 | Orbinski 以时任国际主席身份代表领奖并发表演说；演说引语「Silence has long been confused with neutrality...」与患者故事有英文原文方可引用 |
| 生卒字段 | 机构无 gender/nationalities；birth_date 用成立日 1971-12-22（page.md 明载日期） |
| 首项任务 | 1972 马那瓜地震——抵达比红会晚三天，page.md 明载此细节，勿写成「最先抵达」 |
| 港/加沙节 | 「Decline of medical aid during the Hong Kong protests」「Suspension of operation in Gaza」两节仅客观转述机构自述，不展开 |
| 无肖像 | 机构无人物肖像——封面/概览页用标志色装饰圆或地图母题，禁用领导人照片充当机构肖像 |
| 目录名一致 | 目录 `Médecins_Sans_Frontières/`（含变音符），Makefile `MAIN=Médecins_Sans_Frontières_zh`；xelatex 文件名含变音符时确认编译通过，若 latexmk 出错可另用 ASCII 临时名验证 |

### 第 9 步：术语审查 【机构专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Médecins Sans Frontières | 无国界医生 | 法语缩写 MSF；勿译「医生无国界」 |
| humanitarian aid | 人道主义援助 | 使命总纲 |
| témoignage | 见证 | 法国词，指公开陈述所见苦难 |
| neutrality | 中立 | 与「沉默」的关系是 1999 演说主题 |
| Chantilly Principles | 尚蒂伊原则 | 机构原则文件 |
| La Mancha Agreement | 拉曼查协议 | 治理文件 |
| operational centre | 行动中心 | 六个，独立决策 |
| International Council | 国际理事会 | 24 协会代表 |
|kwashiorkor|夸希奥科（恶性营养不良）|比夫拉图片图注词，慎用|
| MUAC | 中上臂围测量带 | 「生命手环」，2025 入 MoMA |
| Biafra | 比夫拉 | 尼日利亚内战东南部政权 |

---

## 四、背景音乐选择 ✅ 【机构专属】

- **选定曲目**: **Expedition** — Alex-Productions（manifest 预分配，勿改）
- **匹配理由**: 「远征」匹配 MSF 的组织气质——从比夫拉到 75+ 国家的五十年全球远征；急诊出发的急迫节奏呼应「最后一个到达的人道组织却是最先进入战区的」这一建会神话。
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` → 复制为 `presentations/20th_century/Médecins_Sans_Frontières/Expedition.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Médecins_Sans_Frontières/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/PROMPTS_WORKFLOW.md` | 第 2 节组织机构特别规则 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/Médecins_Sans_Frontières.yaml` | 社会关系/领域入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
