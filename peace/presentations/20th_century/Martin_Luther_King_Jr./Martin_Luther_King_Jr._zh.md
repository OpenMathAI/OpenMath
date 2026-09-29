# 和平奖得主立传提示词（OpenPeace 批次实例：Martin Luther King Jr.）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Martin Luther King Jr.（1964 诺贝尔和平奖，美国民权运动领袖）为实例。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放和平奖得主人物史（与 OpenPhysicist / OpenChemist 等共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：沿用物理学家侧标杆 Kenneth G. Wilson 提示词的 0–11 节骨架，适配和平奖得主叙事（身份信息页 + 研究领域/事业领域表 + 社会关系表）。
- **本实例**：Martin Luther King Jr.（本名 Michael King Jr.，马丁·路德·金，1929–1968）。
- **设计哲学**：和平奖得主立传强调「非暴力信念的组织化实践」——事业领域结构化 + 社会关系网（家庭、师承、思想来源、同道与批评者），构成骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Martin Luther King Jr.（1929-01-15 ~ 1968-04-04，享年 39 岁；本名 Michael King Jr.，1934 年因其父改名而改）
- **气质关键词**：**史上最年轻的和平奖得主、"我有一个梦想"的演说家、非暴力民权运动的组织者** —— 1964 诺贝尔和平奖获奖理由：
  > "for his non-violent struggle for civil rights for the Afro-American population"（表彰他为美国黑人争取公民权利的非暴力斗争）
- **设计母题**：**讲道台与林肯纪念堂的台阶（the pulpit and the steps）**。从 Ebenezer 浸信会的讲道台到 1963 年林肯纪念堂前的演说台阶——布道与演说是其视觉语言的核心；可用深绿色石阶线条 + 香槟金光晕与四色 badge 呼应。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Martin_Luther_King_Jr./page.md`（已抓取，事实基准见第 0 步）
- **参考模板**：
  - 物理学家标杆提示词：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节结构母本）
  - 同批成品参照：`peace/presentations/20th_century/Albert_Luthuli/Albert_Luthuli_zh.md`
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：社会关系已入库（第 4.5 步），立传 Beamer 完成后由主控将 `has_biography` 置 1。

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 已抓取页面到 `peace/presentations/pages/20th_century/Martin_Luther_King_Jr./page.md`，**事实基准如下**：
  - 生卒：1929-01-15 生于佐治亚州亚特兰大 ~ 1968-04-04 在田纳西州孟菲斯遇刺身亡（枪击），享年 39 岁
  - 国籍：美国；本名 Michael King Jr.（1934 年父访德归国后父子双双改名 Martin Luther King）
  - 家庭：父 Martin Luther King Sr.（Ebenezer 浸信会牧师）；母 Alberta Williams King；妻 Coretta Scott King（1953-06-18 结婚于阿拉巴马州 Heiberger）；子女 4 人（Yolanda 1955–2007、Martin III 生于 1957、Dexter 1961–2024、Bernice 生于 1963）；姐 Christine King Farris、弟 A. D. King
  - 教育：15 岁跳级入 Morehouse College（1948 社会学 BA）→ Crozer Theological Seminary（1951 神学士 BDiv，任学生会主席）→ Boston University 系统神学博士（1955-06-05，论文比较 Tillich 与 Wieman 的上帝观；最初导师 Edgar S. Brightman，其去世后由 Lotan Harold DeWolf 指导）
  - 任职：Dexter Avenue Baptist Church 牧师（1954 就任，蒙哥马利）→ SCLC 首任主席（1957-01-10 ~ 1968-04-04）→ Ebenezer Baptist Church 与父亲共同牧会（1959/1960 起至去世）
  - 关键荣誉：Nobel Peace Prize 1964（1964-10-14 公布，史上最年轻和平奖得主）、Presidential Medal of Freedom（身后追授 1977）、Congressional Gold Medal（2004/2003 两口径，infobox 作 2004）、Spingarn Medal 1957、Anisfield-Wolf Book Award 1959、Margaret Sanger Award 1966、Time 年度人物 1963、格莱美最佳诵读专辑 1971（身后）、英国 Newcastle 荣誉博士 1967（首位获此的非洲裔美国人）、MLK Day 联邦假日（1986 首次实施）
  - 核心事业清单：① 1950 Maple Shade Mary's Cafe 静坐（非暴力策略的首次演练）② 1955–56 Montgomery 公车抵制（385 天，Browder v. Gayle 胜诉）③ 1957 与同道创建 SCLC ④ 1963 Birmingham 运动（《Letter from Birmingham Jail》）与 March on Washington（"I Have a Dream"）⑤ 1965 Selma 至 Montgomery 游行（Bloody Sunday）与《投票权法》⑥ 1967 Beyond Vietnam 反战演讲 ⑦ 1968 Poor People's Campaign 与孟菲斯环卫工罢工声援
  - 立法成果：Civil Rights Act 1964、Voting Rights Act 1965、Fair Housing Act 1968
  - 关键时间线（15–20 节点）：1929 生于亚特兰大 → 1944 首次公开演讲/入 Morehouse → 1948 BA 毕业 → 1951 Crozer BDiv → 1953-06-18 与 Coretta 结婚 → 1954 Dexter Avenue 牧师 → 1955-06 博士 / 12-01 Rosa Parks 被捕 / 12-05 抵制开始（385 天，住宅被炸）→ 1957-01-10 创建 SCLC / Prayer Pilgrimage 首次全国演讲 → 1958-09-20 哈莱姆遇刺（Izola Curry 持刀）→ 1959-02~03 访问印度（甘地之旅）→ 1960 Atlanta 静坐入狱（Kennedy 兄弟施压获释）→ 1961 Albany 运动 → 1963 Birmingham / 08-28 March on Washington / FBI 开始窃听 → 1963 Time 年度人物 → 1964-10-14 最年轻和平奖得主 → 1965 Selma / 投票权法 → 1966 Chicago 公开住房运动 → 1967-04-04 Beyond Vietnam 演讲（恰好遇刺一周年前）→ 1968 孟菲斯 / 04-04 遇刺（James Earl Ray 定罪，阴谋论争议延续）→ 1977/1986/2004/2011 追授与纪念物
  - 同批次交叉：与 **Albert Luthuli** —— 1962-09 联合发布 Appeal For Action Against Apartheid（American Committee on Africa 组织）；1964-12-10 奥斯陆领奖演讲中称 Luthuli 为自由运动的"领航员"（pilot）；King 页 Legacy 节明载其工作成为 Luthuli 斗争的灵感来源

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Martin_Luther_King_Jr./` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品的 `Makefile`，设置 `MAIN=Martin_Luther_King_Jr._zh`、`VIDEO_NAME=Martin_Luther_King_Jr._zh`

### 第 3 步：收集图片 【人物专属】

- 优先用 `page.md` 正文 Commons 图（如 1964 持奖章照 Martin_Luther_King_Jr_with_medallion_NYWTS.jpg、1963 March on Washington 照）；下载失败用装饰圆占位并在图注说明

### 第 4 步：研究领域/事业领域表 【已入库，与 yaml fields 一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nonviolent resistance | 非暴力抵抗 | 甘地式公民不服从的民权实践 | 非暴力页 |
| 1 | civil rights movement | 公民权利运动 | SCLC 主席 1957–1968 | 运动页 |
| 2 | peace movement | 和平运动 | 1964 诺贝尔和平奖的核心口径 | 诺奖页 |
| 3 | anti-war movement | 反战运动 | 1967 Beyond Vietnam 演讲 | 反战页 |
| 4 | Baptist ministry | 浸信会牧职 | Dexter/Ebenezer 牧会与布道 | 早年页 |

### 第 4.5 步：社会关系表 【已入库，与 yaml relations 一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Coretta Scott King | 无向 | 1953 结婚，育有四子女 |
| parent-child | Martin Luther King Sr. | 无向 | 父，Ebenezer 浸信会牧师，1934 父子改名 |
| parent-child | Alberta Williams King | 无向 | 母 |
| advisor-student | Edgar S. Brightman | 博士→导师 | 波士顿大学博士论文最初导师 |
| advisor-student | Lotan Harold DeWolf | 博士→导师 | Brightman 去世后接任博士导师 |
| influence | Mahatma Gandhi | 对方→本人 | 非暴力抵抗思想来源，1959 访印深化 |
| influence | Henry David Thoreau | 对方→本人 | 《论公民不服从》"拒绝与恶的合作" |
| influence | Walter Rauschenbusch | 对方→本人 | 社会福音神学，"indelible imprint" |
| influence | Benjamin Mays | 对方→本人 | Morehouse 校长，其自认的"精神导师" |
| colleague | Ralph Abernathy | 无向 | SCLC 共同创始人，副手与继任主席 |
| colleague | Bayard Rustin | 无向 | SCLC 共同创始人，非暴力策略首席顾问 |
| colleague | Albert Luthuli | 无向 | 1962 联合发布 Appeal For Action Against Apartheid，相互推崇 |
| controversy | Malcolm X | 无向 | 运动内部批评者，主张暴力抗辩与非暴力路线对立 |

- 入库操作见 `MySQL/data/Martin_Luther_King_Jr..yaml`（seed_person.py 幂等入库）
- **方向约定**：advisor-student / influence 为有向；其余无向

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：庄重、希望、布道感
- **配色**：深绿（manifest 预分配主色 `#145C54`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeNonviolence` 非暴力抵抗 — 暖赭 `#B4552D`
  - `badgeCivilRights` 民权运动 — 深蓝 `#1E4E79`
  - `badgeNobel` 诺奖 — 香槟金 `#C9A227`
  - `badgeMinistry` 牧职与讲道 — 暮紫 `#52307C`
- **背景母题**：石阶级进线条 + 柔和光晕圆，呼应「从讲道台到纪念堂台阶」母题

### 5.1 和平奖得主格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注；无肖像用装饰圆占位。
2. **封面有国籍**：明示 United States，底部状态栏给出 `国籍 | 机构（SCLC）| 主要奖项` 三要素。
3. **必须有身份信息页**：左侧头像 + 右侧信息网格，含至少：生卒、本名与改名、教育（Morehouse→Crozer→BU）、牧职、SCLC 任职、主要荣誉、核心事业。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover 封面模板）
01  封面 — 非暴力民权运动的领袖 / Martin Luther King Jr. 1929–1968 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、本名、教育、牧职、SCLC、荣誉、家庭）
03  核心事业概览 — Montgomery 抵制 / SCLC / Birmingham 与华盛顿 / Selma / 反战
04  亚特兰大童年 (1929–1948) — 本名 Michael King Jr.、1934 改名、Morehouse 与 Mays
05  神学教育 (1948–1955) — Crozer 学生会主席、波士顿大学博士、双博士导师
06  Montgomery 公车抵制 (1955–1956) — Rosa Parks、385 天、住宅被炸、Browder v. Gayle
07  创建 SCLC (1957) — Abernathy/Rustin/Shuttlesworth/Lowery、黑人教会的组织力量
08  甘地之旅 (1959) — 访印、非暴力信念的深化、与 Rustin/Wofford 的策略合作
09  Birmingham 与 March on Washington (1963) — Letter from Birmingham Jail、"I Have a Dream"
10  诺贝尔和平奖 (1964) — 史上最年轻、获奖理由、领奖演讲中向 Luthuli 致意
11  Selma 与立法成果 (1965) — Bloody Sunday、投票权法、三大民权立法
12  Beyond Vietnam 与贫民运动 (1967–1968) — 反战立场争议、Poor People's Campaign
13  孟菲斯与身后 (1968–) — 遇刺、James Earl Ray 定罪、MLK Day、纪念与遗产
14  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

**King 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | 本名 Michael King Jr.，1934 年因父访德（BWA 大会 + 宗教改革纪念地）改名 Martin Luther King——改名典故须完整呈现，勿写成"生于马丁·路德·金" |
| 获奖理由 | 官方为 "for his non-violent struggle for civil rights for the Afro-American population"；正文另有 "for combating racial inequality through nonviolent resistance" 的转述，勿混用 |
| 最年轻口径 | 1964-10-14 获奖时**史上最年轻和平奖得主**（35 岁），此口径 page.md 明载，可写 |
| 甘地影响 | King 最初对甘地知之甚少、甚至备枪自卫，经 Rustin/Wofford/Smiley 等 pacifist 引导才转向非暴力——转变过程勿简化为"自幼受甘地感召" |
| 博士导师 | 波士顿大学博士论文**最初导师是 Edgar S. Brightman**，其去世后由 **Lotan Harold DeWolf** 接任——两人并列，勿只写 DeWolf |
| 领奖时引语 | 领奖演讲中称 Luthuli 为 freedom movement 的"pilot"（Luthuli 页明载）；King 页 Legacy 节亦载其工作启发了 Luthuli——双向明载，关系类型用 colleague |
| FBI 监控 | COINTELPRO、1963 起窃听、1964 威胁信——按 page.md 客观记录；"communist ties" 指控无证据（页文明载 no evidence emerged），勿采信 |
| 遇刺定罪 | James Earl Ray 被定罪，但阴谋论争议延续（Loyd Jowers 审判等）——两说按时间线客观呈现，勿下结论 |
| 运动内部批评 | Malcolm X/Stokely Carmichael/Ella Baker 的批评按 page.md 客观转述，禁单侧评价；仅 Malcolm X 入库 controversy，其余只叙述 |
| 私生活章节 | 婚外情指控（allegations of adultery）与性向传闻类内容**禁写**，与 Hammarskjöld 同纪律 |
| 政治敏感红线 | 种族、政党（Kennedy/Nixon 选举介入）、越战等内容一律只作 page.md 明载的客观事实记录，不加评价性语句 |
| 无载禁写 | Thích Nhất Hạnh 仅有通信（Correspondence 节）不入库；Billy Graham 仅"友人布道 crusades 激发灵感"一句，不入库；Niebuhr/Tillich 影响仅一句叙述不入库（Tillich 还是博士论文研究对象，非私人关系） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| civil rights movement | 民权运动 | 1955–1968 美国语境 |
| nonviolent resistance | 非暴力抵抗 | 甘地-金路线 |
| civil disobedience | 公民不服从 | 源自 Thoreau |
| Montgomery bus boycott | 蒙哥马利公车抵制 | 385 天 |
| SCLC | 南方基督教领袖会议 | 1957 成立 |
| Birmingham campaign | 伯明翰运动 | 1963 |
| March on Washington | 向华盛顿进军 | 1963-08-28 |
| "I Have a Dream" | 《我有一个梦想》 | 演说名，引语仅限 page.md 载原文处 |
| Selma to Montgomery marches | 塞尔玛至蒙哥马利游行 | 1965，Bloody Sunday |
| Letter from Birmingham Jail | 《伯明翰狱中书信》 | 1963 |
| Beyond Vietnam | 《超越越南》 | 1967 反战演讲 |
| Poor People's Campaign | 贫民运动 | 1968 未竟事业 |
| Jim Crow laws | 吉姆·克劳法 | 南方种族隔离法律体系 |
| agape | 圣爱 | 基督教博爱概念 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **With Me** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 陪伴 / 坚定 / 民谣感
- **匹配理由**:
  - "陪伴" 匹配其运动本质——与同道（Abernathy、Rustin）、家庭（Coretta）与千百万普通人同行
  - "坚定" 匹配其气质——四十年最大的抵制、游行与演讲背后，是始终不改的非暴力信念
  - "民谣感" 匹配布道与演说的韵律——其语言本身就有音乐的质地
- **本地路径**: `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` → `presentations/20th_century/Martin_Luther_King_Jr./With-Me.wav`
- **时长**: 以实际音频时长为准，15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Martin_Luther_King_Jr./page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 0–11 节结构母本 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `MySQL/data/Martin_Luther_King_Jr..yaml` | 研究领域 + 社会关系入库文件 |
| `peace/nobel_peace_citations.json` | 获奖理由英文原文 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
