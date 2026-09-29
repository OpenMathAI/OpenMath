# 和平奖得主立传提示词（OpenPeace 批次 9：Cordell Hull）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Cordell Hull（科德尔·赫尔，1945 诺贝尔和平奖得主、美国史上任期最长的国务卿）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用到任何和平奖得主；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业人物。
- **本实例**：Cordell Hull（科德尔·赫尔，1871–1955）。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」（Identity / Bio 速览页）与「事业领域」的结构化表达；Hull 的一生有「山间木屋 → 22 年国会议员 → 12 年国务卿 → 联合国缔造者」的长跑叙事，以「贸易即和平」为思想主轴——这是本篇的灵魂。

---

## 二、背景信息 【人物专属】

- **目标人物**：Cordell Hull（1871-10-02 田纳西州 Olympus ~ 1955-07-23 华盛顿特区，享年 83 岁）
- **气质关键词**：**任期最长的国务卿、互惠贸易的旗手、联合国的缔造者** —— 1945 诺贝尔和平奖获奖理由：
  > "for his indefatigable work for international understanding and his pivotal role in establishing the United Nations"（表彰他不知疲倦地促进国际理解，并在创建联合国中发挥的关键作用）
- **设计母题**：**贸易即和平（trade as peace-maker）**。从 1913 年联邦所得税法、1934 年《互惠贸易协定法》到 1943 年联合国宪章草案——「降低关税、开放市场、以经济互联消弭战争」是比「和平鸽」更贴合 Hull 的视觉语言。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Cordell_Hull/page.md`（含 frontmatter QID Q202979）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Cordell_Hull` 四件套到 `peace/presentations/pages/20th_century/Cordell_Hull/`（**第一轮已核对，事实基准如下**）：
  - 生卒（1871-10-02 生于田纳西州 Olympus 的原木小屋〔当时属 Overton County，今属 Pickett County〕~ 1955-07-23 逝于华盛顿特区家中，享年 83 岁；葬华盛顿国家教堂 St. Joseph of Arimathea 小堂墓穴）
  - 家庭（五子中排行第三；父 William Paschal Hull 1840–1923，母 Mary Elizabeth Hull née Riley 1841–1903；1917 年 45 岁娶寡居的 Rose Frances (Witz) Whitney 1875–1954，无子女）
  - 教育（National Normal University 1889–1890；1891 年获 Cumberland University Cumberland School of Law LL.B. 并取得律师资格）
  - 任职（田纳西州众议员 1893–1897；美西战争任第四田纳西志愿步兵团上尉赴古巴未参战；联邦众议员 1907–1921 与 1923–1931 共 11 届；1913–1917 兼任地方法官——终生被尊称 Judge；DNC 主席 1921-11-02 ~ 1924-07-22；联邦参议员 1931–1933；国务卿 1933-03-04 ~ 1944-11-30，11 年 9 个月为美国史上最长）
  - 关键荣誉（Nobel Peace Prize 1945；Medal for Merit〔frontmatter〕；1963 美国 5 美分纪念邮票）
  - 核心事业清单（①1913 年「几乎独力」起草联邦所得税法补 Underwood 关税减税缺口 ②1934《互惠贸易协定法》与互惠关税体系 ③睦邻政策（Good Neighbor policy）主要设计者 ④「Hull formula」征收补偿「prompt, adequate and effective」进入多国投资条约 ⑤主持 1942 战后外交政策咨询委员会、1943 年中与幕僚起草联合国宪章、1943 莫斯科会议美方代表 ⑥1945 诺奖）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Cordell_Hull/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Cordell_Hull_zh`、`VIDEO_NAME=Cordell_Hull_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 本地 `images.txt` 有真实肖像与多幅插图：
  - 主肖像 `HULL,_CORDELL._HONORABLE_LCCN2016856662_Trim.jpg`（Harris & Ewing c.1913 官方肖像，250px 改 500px）
  - 备选插图 `FreeTradeAgreement1935.jpg`（1935-11-16 美加贸易协定签署，与 King、Roosevelt 同框）、`Hull,_Nomura_and_Kurusu_on_7_December_1941.jpg`（1941-11-17 会见日本使节）、`Washington,_D.C._Representatives_of_26_United_Nations_at_Flag_day_ceremonies...jpg`（1942 联合国家代表）、`Cordell-hull-birthplace-cabin.jpg`（出生木屋）

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 5 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international trade diplomacy | 国际贸易外交 | 互惠贸易协定法 1934、以开放市场消弭战争 | 贸易页 |
| 1 | united nations founding | 联合国创建 | 1942 咨询委员会主席、1943 章程起草、1945 诺奖理由 | 联合国页 |
| 2 | good neighbor policy | 睦邻政策 | 对拉丁美洲政策的主要设计者 | 睦邻页 |
| 3 | tariff and tax reform | 关税与税制改革 | 1913 联邦所得税法、终身低关税主张 | 众议员页 |
| 4 | international investment law | 国际投资法 | Hull formula「prompt, adequate and effective」补偿原则 | 睦邻页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 7 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Franklin D. Roosevelt | 无向 | 1933 任命其为国务卿；1945 为其提名诺贝尔和平奖 |
| colleague | Edward Stettinius Jr. | 无向 | 副手之一；1944-11-30 接任国务卿 |
| colleague | Woodrow Wilson | 无向 | 1913 起草联邦所得税法配套其政府关税法案；1919 支持其加入国际联盟主张 |
| controversy | Sumner Welles | 无向 | 副国务卿 1937 起实际主导国务院；1943 Hull 以辞职相威胁迫其去职 |
| controversy | Henry Morgenthau Jr. | 无向 | 中国白银基金、对德关税、西班牙内战政策多次冲突 |
| influence | Albert Gore Sr. | 无向 | 1938 力劝其竞选联邦众议员 |
| spouse | Rose Frances (Witz) Whitney | 无向 | 1917 结婚，无子女；1954 去世 |

- 方向约定：spouse 无向自动 from<to 归一；controversy/colleague 无向
- 对手方 name_en 用 manifest 规范名；缺失人物由 seed_person.py 自动建占位记录

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：坚韧、务实、制度缔造
- **配色**：钢青蓝（manifest 预分配主色 `#37548D`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeTrade` 互惠贸易 — 航海蓝 `#1F4E79`
  - `badgeUN` 联合国创建 — 金赭 `#8C6A2F`
  - `badgeNeighbor` 睦邻政策 — 深绿 `#2E5E4E`
  - `badgeNobel` 1945 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 低饱和的关税税率下行折线与公文纸网格意象，呼应「贸易即和平」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角 1913 年官方肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（United States），底部状态栏给出 `国籍 | 事业 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、出生地、国籍、家庭、教育、任职（州议员→众议员→参议员→国务卿）、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 联合国缔造者 / Cordell Hull 1871–1955 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（含出生木屋、家庭、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 所得税法 / 互惠贸易 / 睦邻政策 / 联合国 / 1945 诺奖
04  早年：山间木屋的杰斐逊信徒 (1871–1893) — 五子之三、16 岁首次演讲、19 岁任 Clay County 民主党主席
05  法律与戎装 (1889–1898) — Cumberland 法学院 LL.B. 1891、田纳西州众议员 1893–1897、美西战争上尉
06  众议员 22 年：税制改革旗手 (1907–1931) — Ways and Means、1913 联邦所得税法、地方法官 1913–1917
07  DNC 主席与参议员 (1921–1933) — 还清党债、留下 3 万美元盈余、1931 入参议院
08  国务卿十二年 (1933–1944) — 史上最长任期、伦敦经济会议、新政中的定位
09  互惠贸易协定法 (1934) — 降低关税、为更开放的世界市场铺路
10  睦邻政策与 Hull formula — 对拉美政策设计者、补偿原则「prompt, adequate and effective」
11  联合国的缔造 (1942–1945) — 1942 咨询委员会主席、1943 起草宪章、莫斯科会议、1945 诺奖（Roosevelt 提名）
12  与国务院的暗流 — Welles 之争与 Morgenthau 冲突（客观呈现）、1944-11-30 因健康辞职
13  晚年与遗产 — 两卷回忆录 1948、Cordell Hull Dam/Lake、出生地州立公园 1997（藏其诺奖奖章）、1963 纪念邮票
14  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Hull 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由措辞 | 官方理由强调 **international understanding + 联合国创建**；勿写成「因创建联合国独享全部功劳」——Roosevelt 被视为外交掌舵者，Hull 是「underlying force and architect」的 page.md 口径 |
| 任期口径 | 国务卿 1933-03-04 ~ 1944-11-30，正文称「nearly twelve years / eleven years and nine months」，导语另作 1933 to 1944——三处口径并存，全篇统一用「11 年 9 个月（美国史上最长）」 |
| 众议院届数 | 11 届（1907–1921 与 1923–1931）共 22 年；导语称「both houses for 24 years」含参议员 2 年；勿把 22/24 两数混用 |
| 1941-11-26 Hull note | page.md 明载其无接受时限、自称 tentative，历史学家 Bix 认为并非最后通牒；按 page.md 客观呈现，勿写成「Hull 发出最后通牒引发珍珠港」 |
| 政治敏感 | 涉及战时外交（苏联建交、维希法国、戴高乐、SS St. Louis 事件等）一律只作 page.md 明载的客观事实记录，不加任何评价性语句；SS St. Louis 一节按 page.md 记录数字（936 名乘客、约 254 人遇害系部分历史学家估计），必须保留「估计」字样 |
| 引语 | 可引用 page.md 明载原文：珍珠港当日 "In all my fifty years of public service..."；回忆录称 Roosevelt 为 "one of the greatest social reformers in our modern history"；Roosevelt 评 Hull "the one person in all the world..."。其余对话（如 1939 年 6 月电话记录）为转述材料，不整段入引文框 |
| 妻子身世 | Rose Frances (Witz) Whitney 出自弗吉尼亚 Staunton 的奥地利犹太家庭；按 page.md 客观记录即可，不展开相关社会背景叙述 |
| 健康状况 | 患家族性复发性结节病（sarcoidosis），常被误作肺结核；辞职主因为健康恶化 |
| 无载禁写 | 不写「1944 年辞职是为诺奖铺路」、不编造子女（无子女）、不从诺奖颁奖词反推关系、不写与 Nomura/Kurusu 的私人友谊 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Reciprocal Trade Agreements Act | 《互惠贸易协定法》 | 1934，降低关税的核心立法 |
| Good Neighbor policy | 睦邻政策 | 对拉美，非泛称友好外交 |
| Hull formula | 赫尔公式 | 征收补偿「prompt, adequate and effective」，与 Calvo doctrine 并存至今 |
| United Nations Charter drafting | 联合国宪章起草 | 1943 年中由 Hull 及其幕僚起草 |
| Ways and Means Committee | 众议院筹款委员会 | Hull 任内推动税改的平台 |
| Underwood tariff | 《安德伍德关税法》 | 1913，配套联邦所得税法 |
| Secretary of State | 国务卿 | 第 47 任；任期美国史上最长 |
| sarcoidosis | 结节病 | 家族性复发性，勿误作肺结核 |
| Moscow Conference (1943) | 莫斯科会议 | 1943，Hull 任美方代表 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Last Hope** — Victor Cooper（manifest 预分配，勿改）
- **风格**: 戏剧性 / 恢弘 / 终章感
- **匹配理由**:
  - "Last Hope" 呼应 Hull 的事业内核——在二战浩劫中把「以贸易互联与集体安全防止下一场战争」当作文明的最后希望，联合国即这一希望的建制化
  - 曲名的终章感匹配其 12 年国务卿长跑与 1945 年诺奖的收官叙事：木屋少年 → 国会 22 年 → 联合国缔造者
- **本地路径**: `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav` → `presentations/20th_century/Cordell_Hull/Last_Hope.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Cordell_Hull/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/20th_century/Cordell_Hull/images.txt` | 肖像与插图 URL |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Cordell_Hull.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
