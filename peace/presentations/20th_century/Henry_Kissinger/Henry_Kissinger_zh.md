# 和平奖得主立传提示词（人物专属实例：Henry Kissinger）

> 本文件是 OpenPeace 的「和平奖得主立传提示词」，以 Henry Kissinger（1973 诺贝尔和平奖，美国国务卿）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 旗下与 physicist/chemist/medic/literature 平级）。
- **模板来源**：Kenneth_G_Wilson_zh.md 结构母本 + 和平奖项目共享工作流 `peace/PROMPTS_WORKFLOW.md`。
- **本实例**：Henry Alfred Kissinger（亨利·基辛格，1923–2023，美国外交官、政治学者，第 56 任美国国务卿）。
- **设计哲学**：和平奖立传同样需要「身份信息页」（Identity / Bio 速览页）与「事业领域」结构化表达；政治人物立传**只作客观事实记录**，不加任何评价性语句。

---

## 二、背景信息 【人物专属】

- **目标人物**：Henry Alfred Kissinger（1923-05-27 ~ 2023-11-29，享年 100 岁，本名 Heinz Alfred Kissinger）
- **诺奖年份与官方获奖理由**（1973，与 Lê Đức Thọ 共享；英文原文照抄 `peace/nobel_peace_citations.json`，中译照抄名录，禁止改写）：
  > "for jointly having negotiated a cease fire in Vietnam in 1973."（表彰二人共同谈判达成 1973 年越南停火）
- **气质关键词**：**现实政治的操盘手、穿梭外交的开创者、冷战格局的塑造者**
- **设计母题**：**棋盘与航线（chessboard & flight paths）**——地缘博弈的棋盘网格 + 跨洲航线的弧线，呼应「穿梭外交」与全球战略视野。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Henry_Kissinger/page.md`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准（已按 page.md 核对）

- **生卒**：1923-05-27 生于德国菲尔特（Fürth, Bavaria），本名 Heinz Alfred Kissinger；2023-11-29 逝于美国康涅狄格州 Kent（家中，心力衰竭），享年 100 岁；葬阿灵顿国家公墓。
- **国籍变迁**：德国（至 1935）→ 无国籍（1935–1943，纽伦堡法案）→ 美国（1943 入籍至今）。
- **家庭**：父 Louis Kissinger 为学校教师（1933 后被纳粹解职）、母 Paula（née Stern）、弟 Walter（商人）；1949-02-06 与 Anneliese "Ann" Fleischer 结婚（1964 离婚，育 Elizabeth、David 二人）；1974-03-30 与 Nancy Maginnes 结婚。
- **教育**：George Washington High School（夜间完成学业，白天在修面刷工厂做工）→ City College of New York 会计（1943 应征中断）→ 哈佛大学 AB 1950（summa cum laude、Phi Beta Kappa，师从 William Yandell Elliott）/ AM 1951 / PhD 1954（博士论文《Peace, Legitimacy, and the Equilibrium》，1957 出版为《A World Restored》）。
- **军旅**：1943–1946 美军第 84 步兵师→970 反谍报分队（军士），1945-04-10 参与解放 Hannover-Ahlem 集中营分营，获铜星勋章；1946 起任教 Camp King 欧洲司令部情报学校。
- **学术任职**：哈佛政府系任教 1951–1971（Harvard International Seminar 主任 1951–1971、Defense Studies Program 主任 1958–1971）；1958 与 Robert R. Bowie 共同创建 Center for International Affairs。
- **政务任职**：第 7 任美国国家安全顾问（1969-01-20 ~ 1975-11-03）；第 56 任美国国务卿（1973-09-22 ~ 1977-01-20，尼克松与福特两任总统）。
- **卸任后**：Georgetown CSIS/Edmund Walsh 外交学院任教（1970s 后期）；1982 创办 Kissinger Associates（经营至逝世）；2000–2005 任 William & Mary 第 22 任校监；2000–2006 任 Eisenhower Fellowships 董事会主席。
- **关键荣誉**：Nobel Peace Prize 1973（未出席典礼、奖金捐慈善、1975 西贡陷落后提出退还奖章）；总统自由勋章（1977-01-13，with distinction）；National Book Award 1980（《The White House Years》）；Medal of Liberty 1986；名誉 KCMG 1995；Sylvanus Thayer Award 2000；2023 巴伐利亚马克西米利安科学与艺术勋章；Time 年度人物。
- **核心事业清单**：① 对苏缓和（détente，SALT I 与反导条约）；② 打开对华关系（1971 两次秘密访华会晤周恩来）；③ 中东穿梭外交（1973 赎罪日战争后，Sinai I 1974 / Sinai II 1975）；④ 巴黎和平协定谈判（与 Lê Đức Thọ，1973-01-27 签署）；⑤ 外交史与国际关系著述（十余部著作）；⑥ 卸任后地缘政治咨询。
- **关键时间线（16 节点）**：1923 生菲尔特 → 1933 纳粹上台家庭受迫害 → 1938-08-20 全家离德、09-05 抵纽约 → 1943 入籍美国并应征入伍 → 1945 解放 Ahlem 集中营分营、铜星勋章 → 1950 哈佛 BA summa cum laude → 1954 哈佛博士 → 1957《A World Restored》与《Nuclear Weapons and Foreign Policy》出版 → 1969-01 任国家安全顾问 → 1971 两度访华会晤周恩来 → 1972 与 Nixon 访华铺路（1972-02）→ 1973-01-27 巴黎和平协定签署 → 1973-09-22 就任国务卿 → 1973-10–1974 中东穿梭外交 → 1973-12-10 获诺贝尔和平奖（未出席）→ 1982 创办 Kissinger Associates → 2023-11-29 逝于 Kent（100 岁）。

### 第 4 步：事业领域表（与 yaml `fields` 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international relations | 国际关系 | 哈佛学者+国家安全顾问+国务卿 | 学术页、政务页 |
| 1 | diplomacy | 外交 | 穿梭外交、backchannel 谈判 | 核心页 |
| 2 | foreign policy | 外交政策 | 核武器与外交政策专家、《Nuclear Weapons and Foreign Policy》 | 学术页 |
| 3 | geopolitics | 地缘政治学 | Realpolitik（现实政治）倡导者 | 核心页 |
| 4 | diplomatic history | 外交史 | 《A World Restored》《Diplomacy》等 | 著述页 |

### 第 4.5 步：社会关系表（与 yaml `relations` 完全一致）

| 关系类型 | 对方（name_en） | 方向 | note |
|---------|------|------|------|
| co-honored | Lê Đức Thọ | 无向 | 1973 诺贝尔和平奖共同得主，Thọ 拒绝领奖 |
| colleague | Richard Nixon | 无向 | 总统，基辛格任其国家安全顾问与国务卿 |
| colleague | Gerald Ford | 无向 | 继任总统，基辛格留任国务卿至 1977 |
| colleague | Zhou Enlai | 无向 | 1971 两次秘密会谈，中美关系正常化 |
| colleague | Leonid Brezhnev | 无向 | SALT I 与反导条约谈判对手方 |
| spouse | Ann Fleischer | 无向 | 1949 结婚，1964 离婚，育二人 |
| spouse | Nancy Maginnes | 无向 | 1974 结婚 |

### 第 5 步：配色方案 【manifest 预分配，勿改】

- **主色**：`#37548D`（深海军蓝——外交理性与冷战格局）
- **诺奖香槟金**：`#C9A227`
- **四分类色（badgeA–D）**：badgeA 缓和与军控 `#2E5E4E`；badgeB 对华关系 `#8C3B2E`；badgeC 中东穿梭 `#B8860B`；badgeD 越南停火 `#4A3B76`
- **背景母题**：稀疏航线弧线 + 棋盘网格淡纹（呼应穿梭外交与地缘博弈）

### 第 6 步：幻灯片序列（13 页规划，含身份信息页★必做）

```
00  OpenPeace 项目首页（共享封面）
01  封面 — 现实政治的操盘手 / Henry Kissinger 1923–2023 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、本名、国籍变迁、教育、任职、荣誉、核心领域）
03  早年：菲尔特与流亡 (1923–1938) — 纽伦堡法案、1938 抵纽约、夜间中学+工厂
04  二战军旅 (1943–1946) — 入籍、第 84 步兵师、Ahlem 解放、铜星勋章
05  哈佛岁月 (1950–1968) — Elliott 门下、A World Restored、核战略学者
06  国家安全顾问：对华破冰 (1969–1972) — 1971 秘密访华、周恩来会谈
07  巴黎和平协定与 1973 诺贝尔和平奖（核心页）— 与 Lê Đức Thọ 谈判、1973-01-27 签署、Thọ 拒奖、本人未出席典礼
08  国务卿：缓和与中东穿梭 (1973–1977) — SALT I、反导条约、Sinai I/II
09  卸任之后 (1977–2023) — Kissinger Associates、著述、William & Mary 校监
10  荣誉与认可 — 总统自由勋章、National Book Award、名誉爵士等
11  遗产：跨党咨询与外交思想传承（客观事实记录）
12  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

- **版式**：对齐 Kenneth_G_Wilson 模板骨架（\plainbar / \deckbackground / \sectiontitle / \infob）；vbox≤10pt、hbox≤50pt；表格页顶部 -0.35cm + arraystretch 0.62–0.78。
- **陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方仅 "for jointly having negotiated a cease fire in Vietnam in 1973."，勿扩写 |
| 拒奖归属 | 拒绝领奖的是 Lê Đức Thọ（理由为和平未真正实现）；Kissinger 是未出席典礼、捐出奖金、1975 西贡陷落后提出退还奖章——三者勿混淆 |
| 本名 | Heinz Alfred Kissinger，勿写成 Henry 开头即本名 |
| 国籍变迁 | 德国→无国籍(1935–1943)→美国(1943)，三段变迁须完整呈现 |
| 学位年份 | AB 1950 / AM 1951 / PhD 1954，勿混淆 |
| 越战与争议 | 越南战争、柬埔寨轰炸等争议内容一律按 page.md 客观叙述，不作评价、不引侮辱性原话；不展开非 page.md 主线内容 |
| 兄弟 | 弟 Walter 是商人，勿与子 David（传媒业）混淆 |
| 卒地 | 康涅狄格州 Kent（家中），享年 100 岁，葬阿灵顿国家公墓 |

### 第 9 步：术语审查

| 英文 | 中文 | 风险 |
|------|------|------|
| Realpolitik | 现实政治 | 德语借词，意译勿作「强权政治」评价语 |
| détente | 缓和 | 特指 1970s 美苏缓和政策 |
| shuttle diplomacy | 穿梭外交 | 1973–74 中东斡旋的专称 |
| Paris Peace Accords | 巴黎和平协定 | 1973-01-27 签署 |
| SALT I | 第一阶段限制战略武器条约 | 与反导条约（ABM Treaty）并列 |
| National Security Advisor | 国家安全顾问 | 第 7 任，勿与国务卿混淆 |
| backchannel | 秘密渠道（外交） | 绕开国务院的秘密谈判 |
| Kissinger Associates | 基辛格咨询公司 | 1982 创办 |
| Nobel Peace Prize controversy | 诺贝尔和平奖争议 | 仅按 page.md 客观记录（两名委员会成员辞职抗议） |
| Arlington National Cemetery | 阿灵顿国家公墓 | 安葬地 |

---

## 四、背景音乐 ✅ 【manifest 预分配，勿改】

- **选定曲目**：**Last Hope** — Victor Cooper（inspiring-electronic 曲库）
- **匹配理由**：庄重而富有张力的史诗配乐，匹配「流亡少年→哈佛学者→冷战操盘手→百岁外交元老」的世纪跨度叙事；"Last Hope" 亦呼应巴黎停火谈判「以谈判止战」的和平奖主旨。
- **本地路径**：`music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`
- **时长处理**：ffmpeg `-shortest` 自动对齐视频长度。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Henry_Kissinger/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录（中译获奖理由照抄源） |
| `peace/nobel_peace_citations.json` | 官方英文获奖理由 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/PROMPTS_WORKFLOW.md` | 共享工作流与红线 |
| `MySQL/data/Henry_Kissinger.yaml` | 入库 yaml（fields/relations 与本文一致） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：政治人物立传只作客观事实记录，每写一页就 make，看到溢出就修。**
