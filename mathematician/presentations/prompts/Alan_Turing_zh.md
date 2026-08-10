# 图灵 (Alan Turing) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 **Weil、Weyl** 等最新成品为参考模板（含 §二十 社会关系入库 + §二十一 数据库字段核对）。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Alan Turing (1912–1954)
- **气质关键词**: **可计算性之父、密码破译者、人工智能先驱、悲剧英雄、"计算的普罗米修斯"**
- **Wikipedia 页面**: ✅ **已下载**（`pages/Alan_Turing/` 完整，含 page.md + metadata.json + images.txt）
- **参考模板**: `weil/`, `weyl/`, `neumann/`, `hilbert/`, `grothendieck/`, `riemann/` 等完整源码
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`
- **数据库**: `greatminds`（MySQL），Turing id=9 已在库

---

## 第 0 步：核对元数据（metadata.json）

对照 `pages/Alan_Turing/metadata.json` 核对以下字段，**确保 tex 与数据库一致**：

- **qid**：Q7251（数据库中已填）
- **生卒**：1912-06-23 ~ 1954-06-07，享年 41 岁（英年早逝）
- **国籍**：英国（United Kingdom）
- **出生地**：Maida Vale, London（后就读于 Sherborne School）
- **死亡地**：Wilmslow, Cheshire（家中，氰化物中毒）
- **博士导师**：Alonzo Church（普林斯顿大学，1938 年获博士学位）
- **博士论文**：1938，《Systems of Logic Based on Ordinals》— 序数逻辑系统
- **主要任职机构**：
  - 1936–1938: 普林斯顿大学（与 Church 合作）
  - 1939–1945: Bletchley Park（英国政府密码学校，二战密码破译）
  - 1945–1947: 国家物理实验室（NPL）— ACE 计算机设计
  - 1948–1954: 曼彻斯特大学（计算机实验室副主任）
- **关键荣誉**：
  - 1936: Smith's Prize（剑桥大学数学最高奖）
  - 1946: OBE（大英帝国官佐勋章，因战时密码破译贡献）
  - 1951: FRS（皇家学会会士，年仅 39 岁）
  - 2009: 英国政府正式道歉
  - 2013: 伊丽莎白二世女王颁发皇家赦免令
- **重要合作者/同事/学生**：
  - 博士导师: Alonzo Church（λ 演算发明者）
  - 学生: Robin Gandy、Beatrice Worsley
  - Bletchley Park 同僚: Gordon Welchman, Hugh Alexander, Joan Clarke, Jack Good
  - 普林斯顿时期: John von Neumann (曾邀请 Turing 留任 IAS 助手)
  - 曼彻斯特时期: Max Newman (导师兼同事)
  - 密码学先驱: Claude Shannon (信息论之父，战时在贝尔实验室见过 Turing)
  - 剑桥时期: Ludwig Wittgenstein（数学哲学辩论）

---

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。**「现状」列已标注库中是否已有；缺失项按 §21.5 写 `MySQL/seed_turing_full.py` 补齐（`INSERT IGNORE` 幂等）。**

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q7251` | ✅ 已填 |
| 2 | `people` | name_en | `Alan Turing` | ✅ |
| 3 | `people` | name_zh | `艾伦·图灵` | ✅ |
| 4 | `people` | name_variants | `["计算的普罗米修斯","可计算性之父","人工智能先驱"]` | ✅（可补充） |
| 5 | `people` | gender | `male` | ✅ |
| 6 | `people` | birth_date | `1912-06-23` | ✅ |
| 7 | `people` | death_date | `1954-06-07` | ✅ |
| 8 | `people` | description | `English computer scientist (1912–1954)` | ✅ |
| 9 | `people` | primary_occupation | `mathematician` | ✅ |
| 10 | `person_occupation` | 职业（rank 排序） | `mathematician(0)`、`computer scientist(1)`、`university teacher(2)`、`cryptographer(3)`、`logician(4)`、`statistician(5)` | ⚠️ 需补（现仅 mathematician；**cryptographer 需补字典**） |
| 11 | `person_field` | 领域（rank 排序） | `computer science`、`cryptanalysis`、`cryptography`、`logic`、`mathematics` | ✅ 5 项已有 |
| 12 | `award_laureate` | 获奖（year/edition/note） | `Smith's Prize 1936`、`OBE 1946`、`Fellow of the Royal Society 1951` | ⚠️ 全空（前两项需补字典） |
| 13 | `person_institution` | 教育/任职 | `education: King's College、Princeton University、Sherborne School、Hazlehurst`；`employment: Cambridge(1931–1936)、Bletchley Park/GCHQ(1939–1945)、NPL(1945–1947)、Manchester(1948–1954)` | ⚠️ 全空 |
| 14 | `person_nationality` | 国籍 | `United Kingdom` | ✅ |
| 15 | `person_relation` | 社会关系 | 见第 4.5 步（11 条） | ⚠️ 全空 |
| 16 | `rankings` | 榜单（list_key/rank/status） | `OpenMath_20th_Century_Top50` 名次待查 | ⚠️ 待确认 |

核对完成后：写 `MySQL/seed_turing_full.py`，入库后按 §21.4 一键校验并汇报：「新建/更新 X 人、职业 Y 条、领域 Z 条、奖项 A 条、机构 B 条、国籍 C 条、社会关系 D 条」。

---

## 核心数学与科学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 计算理论 | Turing 机 — 可计算性的形式化定义 | 1936 |
| 判定问题 | 停机问题不可判定 — 一劳永逸地解决了 Entscheidungsproblem | 1936 |
| 密码学 | Bombe 机的设计 — 破解 Enigma，加速二战胜利 | 1939–1940 |
| 计算机架构 | ACE 计算机设计 — 存储程序计算机的独立先驱 | 1945–1947 |
| 人工智能 | Turing 测试 — AI 的哲学与操作基础 | 1950 |
| 数理逻辑 | 序数逻辑系统 (博士论文) — Church–Turing 论题 | 1938 |
| 生物数学 | 反应扩散方程 — 形态发生的化学基础 (Turing patterns) | 1952 |
| 密码分析 | Banburismus — 序贯分析在密码破译中的应用 | 1940–1941 |

### ★ 图灵独有的叙事线索

1. **从数学到计算机到密码到 AI 到生物** — Turing 的天才在于他总能从一个领域跳跃到完全不同的另一个领域，并在每个领域留下奠基性贡献。这不是百科全书式的广度，而是"核心洞察力"的反复迁移。
2. **Turing 机不是一台"机器"** — 它是一个数学思想实验：一条无限长的纸带、一个读写头、一张有限状态表。这是历史上第一个对"算法"和"计算"的精确数学定义。它远早于任何实际计算机。
3. **Bletchley Park** — Turing 在二战中领导了 Enigma 密码的破译工作。他的 Bombe 机电装置将解密时间从天降到了小时。历史学家估计他的工作让二战缩短了 2–4 年，拯救了数百万人的生命。
4. **Turing 测试** — 1950 年的论文《计算机器与智能》以 "I propose to consider the question, 'Can machines think?'" 开篇。至今仍是最著名的 AI 哲学基准。
5. **Christopher Morcom** — Turing 16 岁时的挚友，因牛结核病于 1930 年猝逝。这是理解 Turing 人格和精神世界的关键：他对"心灵是否能在物质死亡后继续存在"的终身追问，可能源于此。
6. **化学阉割与悲剧结局** — 1952 年被判"严重猥亵罪"后，选择雌激素注射替代监狱。身心遭受巨大摧残。1954 年 6 月 7 日死于氰化物中毒，年仅 41 岁。
7. **Turing 图案** — 在遭受化学阉割最痛苦的时期，他发表了关于动物皮毛图案形成的数学论文。这篇论文成为数学生物学领域的开山之作——斑马条纹、豹子斑点都可以用反应扩散方程解释。
8. **国家机器的恶与迟到的正义** — Turing 为国家做出了英雄般的贡献，但国家却因为他的性取向摧毁了他。2009 年 Gordon Brown 代表政府正式道歉，2013 年获皇室赦免。

---

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。Turing 当前 `person_relation` **全空**，需新建脚本 `MySQL/seed_turing_relations.py` 全量入库。
> 数据库全部字段核对见 §21.5（第 0.5 步）。

**入库范围（11 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师（advisor-student） | Alonzo Church → Turing | 有向 | ⚠️ 占位（has_biography=0） |
| 学生（advisor-student） | Turing → Robin Gandy | 有向 | ⚠️ 占位 |
| 学生（advisor-student） | Turing → Beatrice Worsley | 有向 | ⚠️ 占位 |
| 同事（colleague） | Max Newman | 无向 | ⚠️ 占位 |
| 同事（colleague） | Gordon Welchman | 无向 | ⚠️ 占位 |
| 合作者（collaborator） | Joan Clarke | 无向 | ⚠️ 占位 |
| 合作者（collaborator） | Jack Good | 无向 | ⚠️ 占位 |
| 同事（colleague） | John von Neumann | 无向 | ✅ 已在库（id=3） |
| 合作者（collaborator） | Claude Shannon | 无向 | ✅ 已在库（id=33） |
| 同事（colleague） | Ludwig Wittgenstein | 无向 | ⚠️ 占位 |
| 挚友（colleague） | Christopher Morcom | 无向 | ⚠️ 占位（note 注明"少年挚友，非学术同事"） |

- 缺失人物（Church/Gandy/Worsley/Newman/Welchman/Clarke/Good/Wittgenstein/Morcom 共 9 人）先建占位：`INSERT INTO people (name_en, primary_occupation, has_biography) VALUES (..., 'mathematician', 0)`
- 关系 `note` 加 `[材料待展开]` 前缀打标识
- 幂等：`INSERT IGNORE` + 联合主键 `(from_id, to_id, relation_type)`

**校验**：
```sql
SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
FROM person_relation pr JOIN people a ON a.id=pr.from_id
JOIN people b ON b.id=pr.to_id JOIN relation_types rt ON rt.relation_key=pr.relation_type
WHERE a.name_en='Alan Turing' OR b.name_en='Alan Turing';
```

---

## 第 5 步：设计配色方案

- 图灵的气质关键词：**计算的冷峻理性、密码学的暗色秩序、AI 的前沿光芒、悲剧英雄的暗金底色**
- **建议配色：深黑 + 氰绿 + 冷银**（计算机终端黑底绿字 + 密码学的暗色 + 金属银的光泽）

> ⚠️ 必须与已有数学家配色完全不同！已有配色：
> - Hilbert：普鲁士蓝 + 金
> - Grothendieck：深靛 + 金
> - Noether：深紫罗兰 + 暗玫瑰金
> - Riemann：墨绿 + 银灰
> - von Neumann：深黑 + 电路绿 (**注意！图灵不能和 von Neumann 撞色！**)
> - Kolmogorov：深松绿 + 古铜金
> - Serre：勃艮第红 + 象牙暖金
> - Weyl：深琥珀金 + 星夜紫
> - Weil：勃艮第深红 + 石板暖灰

- 图灵配色方案（区分于 von Neumann 的电路绿）：
  - **主色 (coverprimary)**：**深黑 + 暗青** — 不同于 von Neumann 的亮电路绿，图灵用更暗、更克制的青色，对应早期显示器的磷光绿和密码学的暗色氛围
  - **强调色 (coveraccent)**：**冷银白** — 算法与机器的金属光泽，也暗示"计算的纯粹之光"
  - 四个分类色，对应图灵的四大支柱：
    - **badgecomputation** (可计算性/Turing 机) — 暗青绿 `#00897B`（磷光终端色）
    - **badgecrypto** (密码学/Enigma) — 深灰蓝 `#37474F`（暗号与秩序）
    - **badgeAI** (人工智能/Turing 测试) — 冷银白 `#B0BEC5`（未来的光芒）
    - **badgebio** (形态发生/数学生物) — 暖金 `#F9A825`（生命的温度 — Turing 图案的暗金底色）
  - 各面板色：darkpanel(深灰黑)/cyanpanel(暗青光)/graypanel(冷灰)/goldpanel(暖金)

---

## 第 6 步：规划幻灯片序列

> ★ **第 0 页（OpenMath 首页）必须使用统一模板 `../cover/OpenMath_Cover.tex`**，禁止自行编写。
> 详见 [数学家立传工作指南 §3.4](../../Mathematician_Biography_Guide.md#34-openmath-项目首页-统一使用-cover-模板)。

图灵的故事有四条线索 —— 计算、密码、AI、悲剧 —— 建议 18 页：

```
00  OpenMath 项目首页（从 cover 模板 \input）

=== 封面与总览 ===
01  封面 — 《图灵：计算的普罗米修斯》 / Alan Turing 1912–1954 + 四色badge
02  为什么图灵是改变人类文明的数学家 — Turing 机 → 计算机 → Enigma → AI → 生物数学

=== Turing 机与可计算性 ===
03  Turing 机的诞生 (1936) — 《论可计算数》— 一个思想实验改变世界
04  判定问题与停机问题 — 一劳永逸地回答 Hilbert 的 Entscheidungsproblem

=== 战争密码 ===
05  Bletchley Park (1939–1945) — 秘密战争中的数学家
06  Bombe 与 Enigma 的破解 — 数学如何击败纳粹密码机

=== 计算机的蓝图 ===
07  ACE 与存储程序架构 (1945–1947) — 从数学机器到电子计算机的独立设计
08  曼彻斯特岁月 (1948–1954) — Ferranti Mark I、计算机实验室、计算的黎明

=== 人工智能的诞生 ===
09  Turing 测试 (1950) — "机器能思考吗？"— 一个哲学问题的工程转化
10  人工智能的哲学深度 — 从 Chess 到 Learning Machines，Turing 为 AI 铺设了五十年蓝图

=== 生命与模式的数学 ===
11  Turing 图案 (1952) — 反应扩散方程 — 斑马条纹、豹子斑点的数学
12  在黑暗中创造光明 — 化学阉割期间，Turing 发表了生物数学的奠基论文

=== 悲剧与遗产 ===
13  国家的恶 (1952–1954) — 化学阉割、定罪、孤立
14  最后的苹果 (1954) — 41 岁的终点，"A computer would deserve to be called intelligent…"
15  Turing 的遗产 — 从你的手机到 ChatGPT，他的思想无处不在

=== 结尾 ===
16  思想回响 — Turing 证明了：思想永远不属于任何国家机器
17  结束页 — "He gave us the mathematical definition of 'computable', and the world has never been the same."
```

> **可以微调。** 以上只是一个建议序列，你觉得哪页多余、哪页缺了就调整。征求我的意见后再开始写代码。

---

## 第 9 步：史实审查 + 术语审查

### 图灵特有的史实陷阱（★ 必须逐页扫描）

| 陷阱类型 | 图灵特有的高危点 |
|---------|---------------------|
| **"计算机之父"归属** | ★ Turing 是"可计算性理论之父"和"AI 之父"，但不是单一的"计算机之父"。存储程序架构由 Turing、von Neumann 和 Eckert–Mauchly 独立发展。Beamer 中应使用"可计算性与计算理论的奠基者"而非"计算机之父"。 |
| **Turing 机≠物理机器** | ★ Turing 机是数学定义，不是工程蓝图。Beamer 第一页就要澄清这一点。 |
| **Bombe 机≠Turing 机** | Bombe 是密码破译的机电装置，Turing 机是理论模型——两者完全不同。Bombe 基于波兰数学家 Rejewski 的早期工作改进而来。 |
| **Enigma 非 Turing 单独破解** | 波兰密码局 (Marian Rejewski 等) 在 1932 年已破解 Enigma。Turing 的贡献是设计了 Bombe 机以应对 Enigma 的持续改进。要说"领导破解 Enigma 的持续改进"而非"破解 Enigma"。 |
| **ACE 计算机** | Turing 的 ACE 设计是存储程序计算机的独立方案，但最终建成的 Pilot ACE 大幅简化了他的设计。不要写"Turing 建造了 ACE"。 |
| **Turing 测试的精确表述** | 1950 年论文的原名是 "Computing Machinery and Intelligence"，Turing 提出了 "Imitation Game"（模仿游戏），后来才被称为 Turing 测试。使用"模仿游戏"作为原始术语。 |
| **性取向定罪的精确描述** | 1952 年 Turing 被判 "gross indecency"（严重猥亵罪）—— 英国 1885 年刑法修正案。不要使用"同性恋罪"这种不精确表述。 |
| **死因** | 官方裁定自杀（氰化物中毒），但一些学者（如 Jack Copeland）提出了意外中毒的可能。可以说"吃了一个氰化物浸泡的苹果"，但不要断言"就是自杀"。 |
| **"苹果标志致敬"是都市传说** | ★ Apple 公司创始人多次否认其彩虹苹果 logo 与 Turing 有关。不要在 Beamer 中断言 Apple 的 logo 是为纪念 Turing。 |
| **化学阉割的精确描述** | 雌激素注射 (stilboestrol)，导致乳房发育和阳痿。"化学阉割"是准确但尖锐的翻译，要说明这是被迫的"治疗"而非刑罚。 |
| **奥运马拉松** | ★ Turing 在 1947 年的马拉松选拔赛中跑了 2:46:03，排第五名。但 Wikipedia 只说这是"an Amateur Athletic Association marathon"，**不是** Olympic trials。要说"接近奥运选拔水平"而非"几乎入选奥运队伍"。 |
| **Christopher Morcom** | Morcom 死于牛结核病 (bovine tuberculosis)，不是"肺结核"（这是两种不同的疾病，虽然相关）。Turing 写给 Morcom 母亲的信件存在，可以使用。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| Turing machine | Turing 机 | 不是"图灵机"，保留英文名 |
| Entscheidungsproblem | 判定问题 | 保留德文原名 |
| halting problem | 停机问题 | — |
| Church–Turing thesis | Church–Turing 论题 | 不是"定理"，是"论题" |
| Bombe | Bombe 机 | 保留英文，首字母大写 |
| Enigma | Enigma 密码机 | 保留英文 |
| stored-program computer | 存储程序计算机 | — |
| imitation game | 模仿游戏 | Turing 测试的原始名称 |
| chemical castration | 化学阉割 | 尖锐但准确 |
| gross indecency | 严重猥亵罪 | 法律术语 |
| Turing pattern | Turing 图案 | — |
| reaction-diffusion equation | 反应扩散方程 | — |
| morphogenesis | 形态发生 | — |
| Banburismus | Banburismus | 保留英文，Turing 命名的序贯分析方法 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| **"第一次/第一个"断言** | 不说"第一个提出 AI 概念"→ "首次系统提出机器智能的判定标准 (Turing 测试)" |
| **悲剧叙事过度** | Turing 首先是一位改变了世界的科学家，其次才是迫害的受害者。叙事比例：贡献70%+生平30% |
| **伪引语** | Turing 的很多"名言"来自电影《模仿游戏》而非历史。不要在 Beamer 中使用任何无法在 page.md 中验证的引语 |
| **Apple 都市传说** | 不要在 Beamer 中提及任何关于 Apple logo 与 Turing 之间关系的说法 |
| **"2 年缩短战争"的精确表述** | ★ 只说历史学家估计缩短了 2–4 年，不说确切的"2 年"或"4 年" |
| **现代术语包装** | Turing 不知道"人工智能"这个词（1956 年 Dartmouth 会议才确立）。用"机器智能"或"模仿游戏"代替 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

### 终审执行流程

```
1. 打开 pages/Alan_Turing/page.md，从头到尾逐段阅读全文
2. 同时打开 Alan_Turing_zh.tex 源码，逐页对照
3. 发现不一致 → 标注优先级（P0/P1/P2）
4. 全部扫描完毕 → 先修复所有 P0，再评估 P1，P2 可选
5. 修复后重新编译 → 确认零错误
```

### ⚠️ 图灵特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **"计算机之父"绝对化** | 争议性称号 | page.md 搜索 "father of computer" |
| **Enigma 独立破解** | 波兰先行者 | page.md 搜索 "Polish" "Rejewski" |
| **奥运马拉松叙事** | 不是奥运会选拔赛 | page.md 搜索 "marathon" "Olympic" |
| **死因断言** | 官方裁定自杀，但存疑 | page.md 搜索 "cyanide" "inquest" "verdict" |
| **Apple 都市传说** | 创始人否认 | page.md 不记载 → 立即可判断 |
| **"2–4 年缩短战争"** | 需引 historically 措辞 | page.md 搜索 "two" "four" "war" |
| **Christopher Morcom 疾病类型** | 牛结核病 ≠ 肺结核 | page.md 搜索 "bovine tuberculosis" |

### 优先级定义

| 优先级 | 定义 | 图灵实际案例 |
|:--:|------|------|
| 🔴 P0 | **事实错误** | "Turing 独立破解 Enigma"（忽略波兰贡献）；"Turing 几乎入选奥运队"（夸大） |
| 🟡 P1 | **来源存疑/捏造** | Apple logo 都市传说；伪造的引语；电影《模仿游戏》中的虚构情节 |
| 🟢 P2 | **重要遗漏** | Turing 的跑步成绩；Turing-Welchman Bombe 的联合设计；贝尔实验室与 Shannon 的会面 |
| ⚪ P3 | **可选补充** | Turing 遗嘱的细节；母亲 Sara Turing 的传记 |

---

## 第 14 步：音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

图灵的气质：**冷峻、理性、暗色中的光芒、悲剧英雄的沉重** — 不应过于昂扬，应带有理性和孤独感。

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | Lonesome | inspiring-electronic | `music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome.wav` | 悲伤电影感，悲剧英雄的孤独 |
| ★★★ | Through the Darkness | inspiring-electronic | `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav` | 史诗黑暗，破解 Enigma 的紧张推进 |
| ★★ | Falling Apart | inspiring-electronic | `music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav` | 电子渐进，化学阉割与 Turing 图案 |
| ★ | Nostalgy | inspiring-electronic | `music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy.wav` | 怀旧深沉，Bletchley Park 的战后回顾 |

**操作**：复制选定的 `.wav` 到 `Alan_Turing/` 目录，`make video` 自动混入。

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `mathematician/presentations/Mathematician_Biography_Guide.md` | 完整操作手册（§二十 社会关系 / §二十一 字段梳理） |
| `mathematician/pages/Alan_Turing/page.md` | Turing Wikipedia 正文 |
| `mathematician/pages/Alan_Turing/metadata.json` | Turing Wikidata 元数据 |
| `mathematician/pages/Alan_Turing/images.txt` | 图片 URL 清单 |
| `MySQL/seed_turing_relations.py` | 社会关系入库脚本（第 4.5 步） |
| `MySQL/seed_turing_full.py` | 全字段补全脚本（第 0.5 步） |
| `mathematician/presentations/weil/Andre_Weil_zh.tex` | Weil 完整源码（最新参考） |
| `mathematician/presentations/neumann/John_von_Neumann_zh.tex` | von Neumann 完整源码 |

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Turing 的独特性在于他不是纯粹的数学家 —— 他的数学改变的是整个人类文明
> 2. Turing 机是数学定义，不是机器 —— 这是整个叙事的基础，必须在第一页就澄清
> 3. 悲剧不是故事的全部 —— 不要写成受害者叙事，Turing 是改变了世界的英雄
> 4. Turing 图案是最被低估的贡献 —— 在化学阉割的痛苦中，他依然在创造科学
> 5. 不要使用任何电影《模仿游戏》中的虚构情节 —— 所有事实必须来自 page.md
> 6. Apple logo 传说绝对不要在 Beamer 中出现 —— 这不是历史事实
> 7. **数据库同步**：先完成第 0.5 步（字段核对表逐项填值）与第 4.5 步（11 条社会关系入库、9 人占位），再开始立传
> 8. 结尾主题句：**"他给了我们'可计算'的数学定义，世界从此不同。"**
