# 和平奖得主立传提示词（OpenPeace 批次实例：Linus Pauling）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Linus Pauling（1962 诺贝尔和平奖，唯一两次独享诺贝尔奖的科学家）的**和平视角**为实例。
> 本人与 1954 诺贝尔化学奖的科学家立传口径见化学侧既有文档；本篇定位为**和平事业立传**，化学成就仅作背景。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放和平奖得主人物史（与 OpenPhysicist / OpenChemist 等共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：沿用物理学家侧标杆 Kenneth G. Wilson 提示词的 0–11 节骨架，适配和平奖得主叙事（身份信息页 + 研究领域/事业领域表 + 社会关系表）。
- **本实例**：Linus Carl Pauling（莱纳斯·鲍林，1901–1994）——化学家与和平活动家的双重身份，本篇取**和平视角**。
- **设计哲学**：和平奖得主立传强调「科学家如何变成和平活动家」的信念转变史——核裁军事业结构化 + 社会关系网（同道、论战对手、家庭），构成骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Linus Carl Pauling（1901-02-28 ~ 1994-08-19，享年 93 岁）
- **气质关键词**：**唯一两次独享诺贝尔奖的人、核试验禁止运动的旗手、"科学的良心"** —— 1962 诺贝尔和平奖获奖理由（1963-10-10 颁布，即《部分禁止核试验条约》生效当日）：
  > "for his fight against the nuclear arms race between East and West"（表彰他对抗东西方核军备竞赛的斗争）
- **设计母题**：**和平请愿书（the petition）**。1958 年 Pauling 夫妇向联合国递交 11,021 名科学家联署的停止核试验请愿——纸页、签名、展开的卷轴是贴合其和平事业的视觉母题；可用蓝灰色纸张纹理 + 香槟金印章与四色 badge 呼应。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Linus_Pauling/page.md`（已抓取，事实基准见第 0 步）
- **参考模板**：
  - 物理学家标杆提示词：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节结构母本）
  - 同批成品参照：`peace/presentations/20th_century/Dag_Hammarskjöld/Dag_Hammarskjöld_zh.md`
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：社会关系已在化学奖批次入库（id=2034，has_social_data=1）；本批 yaml **幂等补写和平侧 fields/occupations/awards（1962 和平奖）与和平视角 relations**，指向同一记录，化学侧行保留。

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 已抓取页面到 `peace/presentations/pages/20th_century/Linus_Pauling/page.md`，**和平视角事实基准如下**：
  - 生卒：1901-02-28 生于俄勒冈州波特兰 ~ 1994-08-19 卒于加州大瑟尔（Big Sur）家中（前列腺癌），享年 93 岁
  - 国籍：美国
  - 家庭：妻 Ava Helen Miller（1923-06-17 结婚至 1981 年她去世，人权活动家，和平活动的深度参与者）；子女 4 人
  - 教育：Oregon State University 化学工程学士（1922）→ Caltech 物理化学与数学物理博士（1925，导师 Roscoe Dickinson + Richard Tolman）
  - 任职（和平活动时期口径）：Caltech（1927–1963，1958 被董事会要求卸任化学与化工系主任，领和平奖奖金后辞职）→ Center for the Study of Democratic Institutions（1963–1967）→ UC San Diego（1967–1969）→ Stanford（1969–1975）
  - 关键荣誉（和平侧）：**Nobel Peace Prize 1962**、Lenin Peace Prize 1970（国际列宁和平奖，1970/1968–69 两种口径见 infobox "1968–1969"，正文作 1970，二说并存须注）、Gandhi Peace Award、Medal for Merit（1948，战时军研贡献）
  - 核心和平事业清单：① 1945-11 起公开演讲原子武器危险，加入 ICCASP ② 1946 加入爱因斯坦主持的 Emergency Committee of Atomic Scientists ③ 1955 联署 Russell-Einstein Manifesto、支持 Mainau Declaration ④ 1957-05 与 Barry Commoner 发起科学家停止核试验请愿，1958-01-15 夫妇向联合国秘书长递交 11,021 人签名 ⑤ 1958 电视辩论与 *No More War!* 出版 ⑥ 支持圣路易斯 CNI 的 Baby Tooth Survey（乳牙锶-90 研究，1961 证实核试验沉降危害）
  - 关键时间线（15–20 节点）：1901 生于波特兰 → 1917 入 OSU → 1922 结识 Ava Helen / 入 Caltech → 1925 博士 → 1926–27 欧洲游学（Sommerfeld/Bohr/Schrödinger）→ 1927 Caltech 助理教授 → 1936 化学系主任/Gates & Crellin 实验室主任 → 1939–45 战时军研（氧分压计、血浆代用品；OSRD 14 项合同）→ 1945-11 ICCASP 演讲（和平转向起点）→ 1946 加入 Einstein 紧急原子科学家委员会 → 1952 护照被拒（伦敦科学会议）→ 1954-06 护照恢复/获诺贝尔化学奖 → 1955-07-09 联署 Russell-Einstein Manifesto → 1957-05 发起请愿 → 1958-01-15 向联合国递交 11,021 签名 / 2 月与 Teller 电视辩论 / 出版 *No More War!* → 1958 Caltech 董事会施压 → 1960 参议院国内安全小组委员会传唤 → 1962-12-10 获 1962 诺贝尔和平奖（Oslo）→ 1963-10-10《部分禁止核试验条约》生效当日颁布 / 辞去 Caltech 教职 → 1963–1967 CSDI → 1968–69 Lenin 和平奖（正文 1970）→ 1963 控告 National Review 诽谤败诉（1968 上诉败诉）→ 1974 共创 International League of Humanists → 1994-08-19 卒于大瑟尔
  - 同批次交叉：**1958-01-15 夫妇向联合国秘书长 Dag Hammarskjöld 递交请愿书**（与 peace-batch-12 的 Hammarskjöld 篇互为镜像）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Linus_Pauling/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品的 `Makefile`，设置 `MAIN=Linus_Pauling_zh`、`VIDEO_NAME=Linus_Pauling_zh`

### 第 3 步：收集图片 【人物专属】

- 优先用 `page.md` 正文 Commons 图（如 1954 全家福、1952 护照拒签信扫描件、诺贝尔博物馆贝雷帽）；下载失败用装饰圆占位并在图注说明

### 第 4 步：研究领域/事业领域表 【已入库（与化学侧 fields 并存），与 yaml 一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nuclear disarmament | 核裁军 | 反核军备竞赛，诺奖理由核心 | 核活动页 |
| 1 | peace activism | 和平运动 | 1945 起的公开演讲、请愿与组织参与 | 活动页 |
| 2 | nuclear test ban | 禁止核试验 | 1957–58 请愿 → 1963 部分禁止核试验条约 | 请愿页 |
| 3 | scientific responsibility | 科学家的社会责任 | Einstein 委员会、Russell-Einstein 宣言 | 组织页 |
| 4 | humanism | 人道主义 | International League of Humanists 共同创始人 | 晚年页 |

### 第 4.5 步：社会关系表 【和平视角增量，与 yaml 一致；化学侧既有 26 条关系保留】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Albert Einstein | 无向 | 1946 加入其主持的紧急原子科学家委员会 |
| colleague | Bertrand Russell | 无向 | 1955 Russell-Einstein Manifesto 联署人 |
| colleague | Barry Commoner | 无向 | 1957 联合发起科学家停止核试验请愿，支持其 Baby Tooth Survey |
| colleague | Dag Hammarskjöld | 无向 | 1958-01-15 夫妇向这位联合国秘书长递交 11,021 人请愿书 |
| competitor | Edward Teller | 无向 | （化学侧已入库）1958 电视辩论核试验放射性尘埃致突变风险 |
| spouse | Ava Helen Pauling | 无向 | （化学侧已入库）1923 结婚，和平活动深度参与者 |

- 入库操作见 `MySQL/data/Linus_Pauling.yaml`（seed_person.py 幂等 UPD 同一记录 id=2034）
- **方向约定**：本批新增全部为无向 colleague；化学侧 advisor-student 有向行原样保留

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：理想主义、论战性、科学家良知
- **配色**：深蓝（manifest 预分配主色 `#2A4B7C`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeDisarm` 核裁军 — 警示红 `#A63A2B`
  - `badgePetition` 请愿运动 — 纸灰蓝 `#5B7599`
  - `badgeNobel` 诺奖 — 香槟金 `#C9A227`
  - `badgeScience` 科学家良知 — 深绿 `#1B5E20`
- **背景母题**：稀疏纸张纹理圆与展开卷轴线条，呼应「和平请愿书」母题

### 5.1 和平奖得主格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注；无肖像用装饰圆占位。
2. **封面有国籍**：明示 United States，底部状态栏给出 `国籍 | 身份（化学家·和平活动家）| 主要奖项` 三要素。
3. **必须有身份信息页**：左侧头像 + 右侧信息网格，含至少：生卒、全名、国籍、教育、两次诺贝尔奖（1954 化学 + 1962 和平）、和平任职、核心和平事业。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover 封面模板）
01  封面 — 两次诺奖的科学家 / Linus Pauling 1901–1994 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育、双诺奖、和平任职、家庭）
03  核心事业概览 — 核裁军 / 和平请愿 / 核试验禁令 / 科学家的社会责任
04  转折点：从化学到和平 (1945–1946) — 战时军研背景、Oppenheimer 邀请婉拒、ICCASP 演讲
05  Einstein 委员会与冷战初年 (1946–1952) — 紧急原子科学家委员会、护照被拒
06  Russell-Einstein 宣言 (1955) — 联署、Mainau Declaration 支持
07  和平请愿书 (1957–1958) — 与 Commoner 发起、11,021 签名递交联合国
08  公开论战 (1958) — 与 Teller 电视辩论、No More War! 出版
09  婴儿牙齿调查与公众压力 — CNI、Baby Tooth Survey、锶-90 证据链
10  政治批评与传唤 (1960–1963) — 参议院小组委员会、National Review 诽谤诉讼
11  诺贝尔和平奖 (1962) — 颁奖日恰逢条约生效、诺奖委员会评价、Ava 的贡献
12  离开 Caltech 与晚年活动 — CSDI、International League of Humanists、反战运动
13  遗产 — 唯一两次独享诺奖者、Linus Pauling Institute、 Oregon 州 Pauling Day
14  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

**Pauling 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 两次诺奖口径 | 1954 化学 + 1962 和平，**唯一两次独享（unshared）诺贝尔奖者**；另一位于不同领域两获诺奖者是 Marie Curie（化学+物理），两人口径勿混 |
| 获奖理由 | 官方为 "for his fight against the nuclear arms race between East and West"，强调**对抗东西方核军备竞赛**；诺奖委员会同日另有长段评价（"ever since 1946 has campaigned ceaselessly..."）可作补充引文 |
| 颁奖年份错位 | 1962 年度奖 **1963-10-10 颁布**（恰为《部分禁止核试验条约》生效当日），此前该年度空缺；时间线须按"1962 年度 / 1963-10 颁布"双口径呈现 |
| 战时军研背景 | 曼哈顿计划化学部负责人之邀被婉拒（不愿迁家），但确有 14 项 OSRD 军研合同与 1948 Medal for Merit——两面都写，勿美化或隐去 |
| Lenin 和平奖年份 | infobox 作 1968–1969、正文作 1970，**两说并存须加注**，勿单选 |
| 政治争议 | 参议院传唤、"苏联共产主义天真的代言人"批评、National Review 诉讼败诉均按 page.md 客观呈现，禁单侧叙事；Vietnam 章节涉及 Ho Chi Minh 只作事实记录 |
| 优生学立场 | page.md 明载其有限优生学主张（缺陷基因携带者强制标记），属争议史实，可客观简述但禁引申评价 |
| 维生素 C | 属医学争议非本篇主线，一句带过即可；"orthomolecular" 相关内容禁写成医学定论 |
| 妻子贡献 | Pauling 本人承认 Ava 深度参与和平工作并遗憾她未共享和平奖——此为 page.md 明载，可写；"夫唱妇随"之类评价禁写 |
| 无载禁写 | Oppenheimer 追求 Ava 事件属化学侧往事（本篇可入陷阱注或一句带过）；除此之外不给 Oppenheimer/Teller 编造新互动 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| nuclear disarmament | 核裁军 | 诺奖理由核心 |
| nuclear arms race | 核军备竞赛 | 东西方对峙语境 |
| nuclear fallout | 放射性尘埃/沉降 | 致突变风险论战场 |
| Russell-Einstein Manifesto | 罗素-爱因斯坦宣言 | 1955-07-09 发布 |
| Emergency Committee of Atomic Scientists | 紧急原子科学家委员会 | Einstein 主持 |
| Partial Test Ban Treaty | 《部分禁止核试验条约》 | 1963 生效 |
| Baby Tooth Survey | 婴儿牙齿调查 | 锶-90 公共卫生研究 |
| petition | 请愿书 | 11,021 名科学家签名 |
| fellow traveller | 同路人 | 政治指控语，引用须带出处 |
| Senate Internal Security Subcommittee | 参议院国内安全小组委员会 | 1960 传唤 |
| orthomolecular | 正分子（医学） | 争议术语，勿作定论 |
| unshared Nobel Prize | 独享诺贝尔奖 | 其独有口径 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Savage** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 张力 / 论战 / 冷峻
- **匹配理由**:
  - "张力" 匹配其双重身份——化学讲坛与和平请愿之间的论战张力，与 Teller 电视辩论的正面交锋
  - "冷峻" 匹配冷战语境——护照被拒、参议院传唤、媒体攻击，是其和平事业的黑暗底色
  - "论战" 匹配叙事——这不是温和的道德叙事，而是一位科学家以数据对抗体制的战斗纪录
- **本地路径**: `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav` → `presentations/20th_century/Linus_Pauling/Savage.wav`
- **时长**: 以实际音频时长为准，15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Linus_Pauling/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 0–11 节结构母本 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `MySQL/data/Linus_Pauling.yaml` | 和平侧 fields/awards/relations 增量入库文件（幂等 UPD id=2034） |
| `peace/nobel_peace_citations.json` | 获奖理由英文原文 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
