# 和平奖得主立传提示词（OpenPeace 21 世纪批次 4：Kailash Satyarthi）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Kailash Satyarthi（2014 诺贝尔和平奖得主、印度儿童权利活动家）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业人物。
- **本实例**：Kailash Satyarthi（凯拉什·萨蒂亚尔蒂，本名 Kailash Sharma，在世）。
- **设计哲学**：和平奖得主立传必须有「身份信息页」与「事业领域」的结构化表达；Satyarthi 是「电气工程师→解放者→全球议程推动者」的角色跃迁，"解放 138,000 个孩子"与"80,000 公里的全球大游行"是本篇的灵魂。

---

## 二、背景信息 【人物专属】

- **目标人物**：Kailash Satyarthi（1954-01-11 生于印度中部维迪沙（时属 Madhya Bharat，今中央邦），在世）
- **气质关键词**：**童工的解放者、教育权的推动者、从讲台走向街头的工程师** —— 2014 诺贝尔和平奖获奖理由：
  > "for their struggle against the suppression of children and young people and for the right of all children to education"（表彰他们对抗对儿童与青年的压迫、争取所有儿童受教育权的斗争）
- **设计母题**：**小脚印与大游行（small footprints and the long march）**。被解放孩子迈出的第一步、103 国 80,000 公里的 Global March、地毯上的 GoodWeave 认证标签——这是比「和平鸽」更贴合 Satyarthi 的视觉语言。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/21th_century/Kailash_Satyarthi/page.md`（含 frontmatter QID Q3442375）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载四件套到 `peace/presentations/pages/21th_century/Kailash_Satyarthi/`（**事实基准如下**）：
  - 出生（1954-01-11 生于 Vidisha，在世；本名 Kailash Sharma，婚后受 Arya Samaj 改革运动影响弃姓氏改 Satyarthi，意为"求真者"）
  - 国籍（印度）
  - 家庭（父 Ramprasad Sharma 退休警察警长；母 Chironjibai 家庭主妇；四兄一姐中最幼；妻 Sumedha Satyarthi；居新德里，另有子、儿媳、孙、女、女婿——仅具名父母与妻子入库）
  - 教育（Government Boys Higher Secondary School Vidisha；Samrat Ashok Technological Institute 电气工程 B.E. 与高压工程 M.E.（时属博帕尔大学，今 Barkatullah University）；毕业后在本校任讲师数年）
  - 任职（讲师→1980 弃工从运；BBA 创始人 1980；Rugmark/GoodWeave International 创立者；Global March Against Child Labour 发起人 1998；Global Campaign for Education 主席 1999–2011（四位共同创始人之一）；KSCF 创立 2004；100 Million Campaign 2016）
  - 关键荣誉（Nobel Peace Prize 2014；Robert F. Kennedy Human Rights Award 1995；Wallenberg Medal 2002；Aachener International Peace Award 1994；Harvard Humanitarian of the Year 2015；Fortune 世界最伟大领袖 2015；Ashoka Fellow 1993 等）
  - 核心事业清单（①BBA 解救超过 138,000 名童工/奴役/拐卖儿童 ②GoodWeave 地毯无童工认证体系 ③1998 Global March 103 国 80,000 公里推动 ILO 182 号公约 ④教育促进全球运动与 SDG 议程 ⑤Bharat Yatra 2017 反儿童性侵大游行 ⑥多本著作）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下创建 `Kailash_Satyarthi/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Kailash_Satyarthi_zh`、`VIDEO_NAME=Kailash_Satyarthi_zh`

### 第 3 步：收集图片 【人物专属】

- 查看 `images.txt`；2023 年照（infobox 主图）为首选主肖像；2014 与 Malala 领奖前记者会合影可作诺奖页插图
- 无肖像时用装饰圆占位（须在图注写明）

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

> 把事业领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 5 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | child rights | 儿童权利 | 一生主线的总纲 | 全篇 |
| 1 | child labour abolition | 消除童工 | BBA 与 Global March 的核心 | 核心页 |
| 2 | right to education | 受教育权 | 2014 诺奖核心理由之一 | 诺奖页 |
| 3 | child trafficking prevention | 防止儿童拐卖 | BBA 解救与康复 | 事业页 |
| 4 | ethical trade | 道德贸易 | GoodWeave 认证与供应链问责 | GoodWeave 页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 8 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Malala Yousafzai | 无向 | 2014 诺贝尔和平奖共同得主 |
| spouse | Sumedha Satyarthi | 无向 | 妻子 |
| parent-child | Ramprasad Sharma | 无向 | 父亲，退休警察警长 |
| influence | Mahatma Gandhi | 无向 | 自陈灵感来源 |
| founder | Bachpan Bachao Andolan | 人→机构 | 1980 年创立的拯救童年运动 |
| founder | Global March Against Child Labour | 人→机构 | 1998 年发起，103 国八万公里大游行 |
| founder | Kailash Satyarthi Children's Foundation | 人→机构 | 2004 年创立 |
| founder | Global Campaign for Education | 人→机构 | 1999 年与 ActionAid、Oxfam、Education International 共同创立并任主席至 2011 |

- 方向约定：founder 人→机构有向；co-honored/spouse/parent-child/influence 无向自动 from<to 归一
- 对手方 name_en 用 manifest 规范名（Malala 为批次 5 对象，本 yaml 先建 stub、对方本人 yaml 回填 QID）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：温热、坚定、行进
- **配色**：深绿（manifest 预分配主色 `#1B4D3E`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeChild` 儿童权利 — 暖橙 `#C96A1E`
  - `badgeMarch` 大游行 — 砖红 `#A63A2B`
  - `badgeWeave` 道德贸易 — 靛蓝 `#2E5E8C`
  - `badgeNobel` 2014 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 沿对角线延伸的脚印点列意象（低饱和），呼应「小脚印走出大游行」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（India），底部状态栏给出 `国籍 | 事业 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：出生、本名、国籍、家庭、教育、任职、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 童工的解放者 / Kailash Satyarthi 1954– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（本名、家庭、教育、任职、荣誉、核心领域）
03  核心贡献概览 — BBA / GoodWeave / Global March / GCE / Bharat Yatra
04  早年：维迪沙的少年 (1954–1980) — 四兄一姐中最幼、穆斯林邻里学乌尔都文、母 亲的影响、电气工程学位与讲师岁月
05  改名与转向 — 本名 Sharma（婆罗门姓氏暗示）婚后弃姓改 Satyarthi，Arya Samaj 改革运动影响、1980 弃工从运
06  Bachpan Bachao Andolan (1980–) — 拯救童年运动、超过 138,000 名儿童获解放（BBA 团队口径）
07  GoodWeave：从地毯到标签 (1980s–2009) — Rugmark 首个自愿认证体系、消费者意识运动、2009 更名 GoodWeave
08  1998 全球大游行 — 103 国 80,000 公里、童工幸存者同行、直接推动 ILO 182 号公约 1999 全票通过
09  全球教育议程 (1999–2015) — GCE 主席 12 年、UNESCO 相关机构、Fast Track Initiative/GPE、把童工议题带入 SDG
10  2014 诺贝尔和平奖 — 与 Malala 共享、理由原文、首位在印度本土出生的和平奖得主
11  Bharat Yatra (2017) — 09-11 自科摩林角出发、35 天逾万公里、《2018 刑法修正案》严惩儿童性侵
12  100 Million Campaign (2016–) — 6000 名青年同行者、35 国五大洲、学生组织网络
13  荣誉长廊 — RFK 1995 / Wallenberg 2002 / Harvard 2015 / Fortune 2015 / 荣誉博士多枚
14  日常与遗产 — 新德里、2017 奖牌失窃复得、著作五种、未竟的"每个孩子都自由、安全、受教育"
15  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Satyarthi 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 本名与改姓 | 本名 Kailash Sharma；Satyarthi 是婚后所改（Arya Samaj 影响），勿写成"笔名/组织化名" |
| 诺奖理由 | 官方理由主语 "their"（与 Malala 共享），照抄勿改写成个人独得；"首位在印度本土出生的诺贝尔和平奖得主"是 page.md 明载口径，勿拔高为"首位印度人" |
| 解救人数 | "超过 138,000 名"是 BBA 团队累计口径，引用时带"其团队"主语；勿与 ILO 全球统计混用 |
| 里程两说 | Bharat Yatra 里程：引言段作 19,000 km/35 天，Bharat Yatra 节作 12,000 km 以上——两说并存，同篇内选定一处口径并加注，勿跨页混用 |
| 学位口径 | B.E. 与 M.E. 均出自 Samrat Ashok Technological Institute（M.E. 为高压工程方向）；"时属博帕尔大学（今 Barkatullah University）"按正文口径； Amrita Vishwa Vidyapeetham 仅 frontmatter 出现，正文未展开，勿写入片 |
| 同名区分 | Kailash Satyarthi Children's Foundation（KSCF）与其个人同名是机构名，勿写成"以他父亲命名"或拆错缩写 |
| 政治敏感 | 涉印度总理会见照片（Modi）、美国前总统 Obama 接见照片等仅客观图注；Bharat Yatra 的立法成果按 page.md 客观记录，不作政治评价 |
| 家庭成员 | 仅父（Ramprasad Sharma）、母（Chironjibai）、妻（Sumedha Satyarthi）具名；子/女/孙仅具关系不具名，禁写名字 |
| 无载禁写 | 不写其兄弟姐妹姓名（page.md 未具名）；不写 BBA 解救行动的具体案例细节（page.md 未载）；不写诺奖典礼演说内容（本地页面无载，禁编造引语） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Bachpan Bachao Andolan | 拯救童年运动 | BBA，1980 创立 |
| Global March Against Child Labour | 反对童工全球大游行 | 1998，103 国 80,000 公里 |
| ILO Convention 182 | 国际劳工组织 182 号公约 | 最恶劣形式童工公约，1999 通过 |
| GoodWeave International | GoodWeave 国际 | 原名 Rugmark，2009 更名 |
| Global Campaign for Education | 全球教育促进运动 | GCE，1999 四方共同创立 |
| Kailash Satyarthi Children's Foundation | 凯拉什·萨蒂亚尔蒂儿童基金会 | KSCF，2004 创立 |
| 100 Million Campaign | 一亿人运动 | 2016 发起的青年主导运动 |
| Bharat Yatra | 印度之旅大游行 | 2017-09-11 出发，35 天 |
| Arya Samaj | 雅利安社 | 印度教改革运动，改姓的思想背景 |
| Ashoka Fellow | 阿育王研究员 | 1993 当选的社会企业家称号 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Nostalgia** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 温情 / 回望 / 希冀
- **匹配理由**:
  - "Nostalgia" 呼应"还给每个孩子童年"的事业内核——被夺走的童年与被追回的童年
  - 温情而不滥情的气质匹配其四十年的坚持
- **本地路径**: `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` → `presentations/21th_century/Kailash_Satyarthi/Nostalgia.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Kailash_Satyarthi/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/21th_century/Kailash_Satyarthi/images.txt` | 肖像与插图 URL |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Kailash_Satyarthi.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
