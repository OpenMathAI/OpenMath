# 巴拿赫 (Stefan Banach) 立传提示词

> 本提示词严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 **Gödel、Turing、Weil** 等最新成品为参考模板（含 §二十 社会关系入库 + §二十一 数据库字段核对）。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Stefan Banach (1892–1945)
- **气质关键词**: **自学成才的天才、Lwów 学派灵魂、苏格兰咖啡馆数学、波兰数学的荣耀、被战争吞噬的分析巨人**
- **Wikipedia 页面**: ✅ **已下载**（`pages/Stefan_Banach/` 完整，含 page.md + metadata.json + images.txt）
- **参考模板**: `godel/`, `turing/`, `weil/`, `neumann/`, `kolmogorov/` 等完整源码
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`
- **数据库**: `greatminds`（MySQL），Banach id=11 已在库（⚠️ 主表字段待补全，见第 0.5 步）

---

## 第 0 步：核对元数据（metadata.json）

对照 `pages/Stefan_Banach/metadata.json` 核对以下字段，**确保 tex 与数据库一致**：

- **qid**：Q180217（数据库中已填）
- **生卒**：1892-03-30 ~ 1945-08-31，享年 53 岁（⚠️ 库中缺失，待补）
- **性别**：male（⚠️ 库中缺失，待补）
- **中文名**：斯特凡·巴拿赫（⚠️ 库中缺失，待补）
- **国籍**：波兰（奥匈帝国 Cisleithania 出生 → 波兰第二共和国 → 苏联/纳粹占领期）
- **出生地**：Kraków (克拉科夫)，当时属奥匈帝国加利西亚
- **死亡地**：Lwów (利沃夫)，当时被苏联占领（今乌克兰）
- **博士导师**：Hugo Steinhaus（非正式指导，发现者）；metadata 另列 Kazimierz Twardowski（哲学家）
- **博士论文**：1920，《Sur les opérations dans les ensembles abstraits et leur application aux équations intégrales》— 包含 Banach 空间和 Hahn–Banach 定理的核心思想
- **主要任职机构**：
  - 1920–1922: Lwów 理工大学（Lviv Polytechnic）助理
  - 1922–1941: 利沃夫大学（Jan Kazimierz 大学）
  - 1941–1944: 纳粹占领期被剥夺教职，在 Weigl 研究所靠喂养虱子为生
  - 1944–1945: 利沃夫大学复职（短暂）
- **关键荣誉**：
  - 1924: 波兰学习院成员（Polish Academy of Learning membership）— ★ 唯一同时代、可入库的荣誉
  - 1930: 波兰数学学会主席
  - 1936: 奥斯陆 ICM 全体大会报告
  - ⚠️ **Order of the White Eagle（2018 追授）— 晚于数学家 73 年，按 §21.5 原则不收**
  - ⚠️ 多次被提名但从未获得 Fields 奖（Fields 1936 年才设立，Banach 已 44 岁）
- **重要合作者/同事/学生**：
  - 发现者与合作者: Hugo Steinhaus（公园长椅"发现"）
  - Lwów 学派核心成员: Stanisław Mazur（学生/合作者）, Stanisław Ulam, Juliusz Schauder, Władysław Orlicz
  - Banach–Tarski 悖论共同提出者: Alfred Tarski
  - 苏联数学家: Sergei Sobolev, Andrey Kolmogorov（苏联占领期访问 Lwów）
  - 学生: Stanisław Mazur（苏格兰咖啡馆问题集联合提出者）

---

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。**「现状」列已标注库中是否已有；缺失项按 §21.5 写 `MySQL/seed_banach_full.py` 补齐（`INSERT IGNORE` 幂等）。⚠️ 本表 people 主表多项缺失，必须补齐。**

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q180217` | ✅ 已填 |
| 2 | `people` | name_en | `Stefan Banach` | ✅ |
| 3 | `people` | name_zh | `斯特凡·巴拿赫` | ⚠️ **NULL 需补** |
| 4 | `people` | name_variants | `["泛函分析之父","苏格兰咖啡馆的灵魂"]` | ⚠️ 空需补 |
| 5 | `people` | gender | `male` | ⚠️ **NULL 需补** |
| 6 | `people` | birth_date | `1892-03-30` | ⚠️ **NULL 需补** |
| 7 | `people` | death_date | `1945-08-31` | ⚠️ **NULL 需补** |
| 8 | `people` | description | `Polish mathematician (1892–1945)` | ⚠️ 待核 |
| 9 | `people` | primary_occupation | `mathematician` | ✅ |
| 10 | `person_occupation` | 职业（rank 排序） | `mathematician(0)`、`university teacher(1)` | ⚠️ 需补（现仅 mathematician） |
| 11 | `person_field` | 领域（rank 排序） | `mathematics`、`functional analysis`、`topology`、`measure theory`、`set theory`、`Banach space`、`integral` | ✅ 7 项已有 |
| 12 | `award_laureate` | 获奖（year/note） | `Member of the Polish Academy of Learning 1924` | ⚠️ 空（需补字典）；⚠️ **White Eagle 2018 追授不收** |
| 13 | `person_institution` | 教育/任职 | `education: Lviv Polytechnic、Jagiellonian University、Lviv University`；`employment: Lviv Polytechnic(1920–1922)、Lviv University(1922–1941)` | ⚠️ 全空 |
| 14 | `person_nationality` | 国籍 | `Cisleithania`、`Second Polish Republic`、`Ukrainian SSR`、`Reichskommissariat Ukraine` | ✅ 4 项已有 |
| 15 | `person_relation` | 社会关系 | 见第 4.5 步（8 条） | ⚠️ 全空 |
| 16 | `rankings` | 榜单（list_key/rank/status） | `OpenMath_20th_Century_Top50` 名次待查 | ⚠️ 待确认 |

核对完成后：写 `MySQL/seed_banach_full.py`，入库后按 §21.4 一键校验并汇报：「新建/更新 X 人、职业 Y 条、领域 Z 条、奖项 A 条、机构 B 条、国籍 C 条、社会关系 D 条」。

---

## 核心数学与科学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 泛函分析 | Banach 空间的公理化定义 — 完备赋范向量空间 | 1920–1922 |
| 线性算子理论 | Banach–Steinhaus 定理（一致有界原理） | 1927 |
| 泛函分析 | Hahn–Banach 定理（线性泛函延拓定理） | 1927 |
| 泛函分析 | 开映射定理与闭图像定理 | 1929–1930 |
| 测度论 | Banach–Tarski 悖论 — 一个球分成有限块重组为两个同大之球 | 1924（1932 发表） |
| 专著 | 《Théorie des opérations linéaires》— 泛函分析的开山经典 | 1931 |
| 期刊创建 | 《Studia Mathematica》— 世界上第一本泛函分析专业期刊 | 1929 |

### ★ 巴拿赫独有的叙事线索

1. **自学成才的天才** — Banach 从未系统接受过数学教育。他不按课程走——只在 Lwów 理工大学上自己感兴趣的课，从未取得正式工程学位。Steinhaus 称这次发现为"我一生中最重要的数学发现"——他发现的不是定理，而是一个人。
2. **苏格兰咖啡馆** — Lwów 的苏格兰咖啡馆，Banach 和同事（Mazur, Ulam, Schauder 等）在烟雾缭绕中讨论数学，用笔记本记录问题和解答。这不是浪漫化——这是 Lwów 学派的实际工作方式。
3. **苏格兰咖啡馆问题集** — Mazur 买的一本专用笔记本，记录了 193 个未解决的问题。问题 153 的奖励是"活鹅"——1972 年 Per Enflo 解决该问题时，Mazur 在华沙公开仪式上把一只活鹅交给了他。
4. **Banach 空间** — 现代泛函分析的 DNA。Banach 不是第一个使用函数空间的人（Hilbert 空间 1900s 就被研究），但他给出了**公理化定义**：完备的赋范向量空间。这定义简单到能写在一行，却统一了整个分析领域。
5. **Banach–Tarski 悖论** — 严格定理，选择公理的惊人后果。Banach 本人对此态度冷静——它是 AC 的后果，不是物理事实。
6. **战争中的数学** — 苏联占领期受到相对优待（Kolmogorov 和 Sobolev 亲自访问）；纳粹占领期被迫放弃教职，在 Weigl 研究所喂虱子维持生存。但他没有停止数学。
7. **《线性算子理论》** — 1931 年出版的泛函分析"圣经"，为整个领域建立了统一语言。
8. **53 岁肺癌去世** — 二战结束后不到一年。他有机会成为雅盖隆大学数学系主任（波兰最高学术荣誉），但疾病夺走了这个机会。

---

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。Banach 当前 `person_relation` **全空**，需新建脚本 `MySQL/seed_banach_relations.py` 全量入库。
> 数据库全部字段核对见 §21.5（第 0.5 步）。

**入库范围（8 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师（advisor-student） | Hugo Steinhaus → Banach | 有向 | ✅ 已在库（id=341，note 注明"非正式指导/发现者"） |
| 学生（advisor-student） | Banach → Stanisław Mazur | 有向 | ⚠️ 占位 |
| 同事（colleague） | Stanisław Ulam | 无向 | ⚠️ 占位（Lwów 学派，后 Los Alamos） |
| 合作者（collaborator） | Juliusz Schauder | 无向 | ⚠️ 占位（Schauder 不动点定理，1943 年被纳粹杀害） |
| 合作者（collaborator） | Alfred Tarski | 无向 | ⚠️ 占位（Banach–Tarski 悖论共同提出者） |
| 同事（colleague） | Andrey Kolmogorov | 无向 | ✅ 已在库（id=5，苏联占领期访问 Lwów） |
| 同事（colleague） | Sergei Sobolev | 无向 | ✅ 已在库（id=44，苏联占领期与战后联系） |
| 同事（colleague） | Władysław Orlicz | 无向 | ⚠️ 占位（Lwów 学派核心成员，Orlicz 空间） |

- 缺失人物（Mazur/Ulam/Schauder/Tarski/Orlicz 共 5 人）先建占位：`INSERT INTO people (name_en, primary_occupation, has_biography) VALUES (..., 'mathematician', 0)`
- 关系 `note` 加 `[材料待展开]` 前缀打标识
- 幂等：`INSERT IGNORE` + 联合主键 `(from_id, to_id, relation_type)`

**校验**：
```sql
SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
FROM person_relation pr JOIN people a ON a.id=pr.from_id
JOIN people b ON b.id=pr.to_id JOIN relation_types rt ON rt.relation_key=pr.relation_type
WHERE a.name_en='Stefan Banach' OR b.name_en='Stefan Banach';
```

---

## 第 5 步：设计配色方案

- 巴拿赫的气质关键词：**温暖、醇厚、波兰土地的色调、咖啡馆的暗金光泽、分析的严谨与深度**
- **建议配色：深琥珀（波兰蜂蜜酒）+ 深松绿（波兰森林）+ 象牙纸** — 咖啡馆的温暖 + 波兰自然 + 泛函分析论文的象牙白

> ⚠️ 已有配色回顾（避免撞色）：
> - Hilbert：普鲁士蓝+金 | Grothendieck：深靛+金 | Noether：深紫罗兰+暗玫瑰金
> - Riemann：墨绿+银灰 | von Neumann：深黑+电路绿 | Turing：深黑+暗青+冷银
> - Kolmogorov：深松绿+古铜金 | Serre：勃艮第红+象牙暖金 | Weyl：深琥珀金+星夜紫
> - Weil：勃艮第深红+石板暖灰 | Gödel：深勃艮第+古金+暗灰

- Banach 配色方案（必须区分于 Kolmogorov 和 Weyl）：
  - **主色 (coverprimary)**：**深琥珀棕** — 波兰蜂蜜酒的醇厚、苏格兰咖啡馆的暖木调、旧书的暗金色泽。区别于 Kolmogorov 的松绿（更冷），也不同于 Weyl 的琥珀金（更亮）
  - **强调色 (coveraccent)**：**象牙米白** — 泛函分析论文的象牙纸色、咖啡馆的晨光
  - 四个分类色，对应 Banach 的四大支柱：
    - **badgespace** (Banach 空间/泛函分析) — 深松绿 `#2E5A47`（分析的严谨深度，致敬波兰森林）
    - **badgetheorem** (三大基本定理) — 暗金铜 `#B8860B`（定理的经典光泽）
    - **badgecafe** (Lwów 学派/苏格兰咖啡馆) — 暖琥珀 `#C77A33`（咖啡与伏特加的色调）
    - **badgewarsaw** (波兰/战争) — 暗红陶 `#A52A2A`（波兰国旗中的红色，但不张扬）
  - 各面板色：amberpanel(暖琥珀)/greenpanel(深松绿)/goldpanel(暗金铜)/redpanel(暗红陶)/graypanel(象牙灰)

---

## 第 6 步：规划幻灯片序列

Banach 的故事有三条主线：泛函分析的创立 + Lwów 学派的传奇 + 战争的毁灭，建议 17 页：

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 封面与总览 ===
01  封面 — 《巴拿赫：泛函分析的奠基人》 / Stefan Banach 1892–1945 + 四色badge
02  为什么巴拿赫改变了分析的面貌 — Banach 空间 · 三大基本定理 · 苏格兰咖啡馆 · 波兰学派的灵魂

=== 自学成才 ===
03  克拉科夫的私生子 (1892–1916) — 由洗衣女工抚养 · 自学数学 · 一战逃回克拉科夫
04  公园长椅上的偶遇 (1916) — Steinhaus 发现了 Banach — "我一生中最重要的数学发现"

=== 泛函分析的诞生 ===
05  Banach 空间 (1920–1922) — 完备赋范向量空间的公理化定义 — 泛函分析的基石
06  三大基本定理 — Hahn–Banach · Banach–Steinhaus · 开映射定理/闭图像定理

=== 苏格兰咖啡馆 ===
07  苏格兰咖啡馆与 Lwów 学派 — 伏特加、咖啡与数学 — 20 世纪最著名的数学聚集地
08  苏格兰咖啡馆问题集 — 193 个未解决问题 · 活鹅的承诺 · 数学共同体精神

=== 专著与悖论 ===
09  《线性算子理论》(1931) — 泛函分析的"圣经"，统一了整片数学疆域
10  Banach–Tarski 悖论 — 选择公理的惊人后果 — 一个球变成两个

=== 战争岁月 ===
11  1939–1941: 苏联占领 — Sobolev 和 Kolmogorov 的访问 · 在学术真空中的坚持
12  1941–1944: 纳粹占领 — 大学关闭 · 在 Weigl 研究所喂虱子 · 秘密教学
13  被战争摧毁的学派 — Schauder 死于纳粹之手 (1943) · Ulam 流亡 · Lwów 的终结

=== 终章 ===
14  战后的最后一年 (1944–1945) — 雅盖隆大学的召唤 · 53 岁肺癌去世
15  巴拿赫的遗产 — Banach 空间是整个现代泛函分析的 DNA · 从 PDE 到量子力学的每一处

=== 结尾 ===
16  思想回响 — 在咖啡馆里，一群波兰数学家创建了现代分析最基本的语言
17  结束页 — "他说：给我一个完备的赋范向量空间，我把它命名为家。"
```

> **可以微调。** 征求我的意见后再开始写代码。

---

## 第 9 步：史实审查 + 术语审查

### 巴拿赫特有的史实陷阱（★ 必须逐页扫描）

| 陷阱类型 | 巴拿赫特有的高危点 |
|---------|---------------------|
| **私生子出身** | Banach 的父亲是奥匈帝国军官 Stefan Greczek，母亲 Katarzyna Banach 是未婚洗衣女工。Banach 随母姓。不要说"被父亲抛弃"——父亲提供了抚养费并送他上学。但 Banach 确实由祖母/养母抚养长大。 |
| **自学而非正式教育** | ★ Banach 从未取得 Lwów 理工大学正式工程学位。他不按课程走，只上感兴趣的课。不要说"Banach 毕业于…" |
| **博士学位的非常规路径** | 1920 年获博士学位，但"博士论文"基于已发表的成果，他从未进行常规博士培养。口试委员会不得不适应他的"非标准"知识结构。 |
| **公园长椅偶遇** | Steinhaus 在 Planty 公园听到 Banach 和朋友讨论 Lebesgue 积分。当时 Banach 不是"无名之辈"——他已自学做出重要发现。这是"被发现"而非"被创造"。 |
| **Hahn–Banach 定理的命名** | ★ Hahn 和 Banach 独立发现。Hahn 的版本 1927 年发表，Banach 的更早（博士论文已有思想萌芽）。不要写"Banach 发现了 Hahn–Banach 定理"——写"Banach 独立证明了线性泛函延拓定理，后与 Hahn 的工作合称 Hahn–Banach 定理"。 |
| **Banach–Tarski 悖论的时间** | 1924 年证明，1932 年才在 Fundamenta Mathematicae 发表。不要混淆发现年和发表年。 |
| **纳粹占领期的"虱子喂养"** | ★ Banach 在 Rudolf Weigl 的斑疹伤寒疫苗研究所工作，喂养感染斑疹伤寒的虱子（虱子装在绑在腿上的小盒子里，以人体血液喂养）。极端艰苦但保护了他不被送往集中营。不要轻描淡写。 |
| **Schauder 的死因** | Schauder 是犹太人，1943 年在 Lwów 被纳粹盖世太保杀害。这是 Lwów 学派被战争摧毁的核心悲剧事件。 |
| **苏联占领的评价** | 苏联占领 Lwów 期间 Banach 受相对优待（Sobolev 和 Kolmogorov 访问了他）。但这不是"亲苏联"——这是生存策略。叙事保持中立。 |
| **Lwów 的地理归属** | 战前 Lwów 属于波兰第二共和国。战后划归苏联（今乌克兰利沃夫）。不要说"Lwów 在乌克兰"来描述战前时期。 |
| **白鹰勋章** | ★ Order of the White Eagle 是 **2018 年追授**（独立 100 周年仪式），晚于数学家 73 年。按 §21.5 原则不入库；Beamer 中可作为"迟到的荣誉"一句带过，但不可写成 Banach 在世时的成就。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| Banach space | Banach 空间 | 完备赋范向量空间 |
| normed vector space | 赋范向量空间 | — |
| Hahn–Banach theorem | Hahn–Banach 定理 | 不称"Banach 延拓定理" |
| Banach–Steinhaus theorem | Banach–Steinhaus 定理 | 也称一致有界原理 |
| open mapping theorem | 开映射定理 | Banach 空间版 |
| closed graph theorem | 闭图像定理 | — |
| Banach–Tarski paradox | Banach–Tarski 悖论 | 严格定理，不是悖论 |
| axiom of choice (AC) | 选择公理 | — |
| Scottish Café | 苏格兰咖啡馆 | Kawiarnia Szkocka（波兰语） |
| Scottish Book | 苏格兰咖啡馆问题集 | — |
| Théorie des opérations linéaires | 《线性算子理论》 | 法文原版书名 + 中文注释 |
| Studia Mathematica | 《数学研究》 | 泛函分析第一本专业期刊 |
| typhus vaccine | 斑疹伤寒疫苗 | Weigl 研究所的产品 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| **"第一部"叙事** | 不说"第一部泛函分析专著"→ "泛函分析领域最具奠基性的经典专著" |
| **"发现"的夸大** | Steinhaus "发现"了 Banach，但 Banach 当时已是自学成才的数学研究者 |
| **战争叙事过重** | 叙事比例：数学60%+学派20%+战争20% |
| **伪引语** | 苏格兰咖啡馆没有录音——大部分故事来自 Ulam 和 Steinhaus 的回忆录。使用间接引语 |
| **地理精确性** | Lwów 的战前/战时/战后归属不同。只说"波兰的 Lwów"或"今乌克兰利沃夫"而不混淆时代 |
| **公理化定义的归属** | ★ 不要把 "Banach 空间"定义为"Hilbert 空间的推广"——Banach 的公理化定义独立于 Hilbert 空间提出，两者平行发展 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

### 终审执行流程

```
1. 打开 pages/Stefan_Banach/page.md，从头到尾逐段阅读全文
2. 同时打开 Stefan_Banach_zh.tex 源码，逐页对照
3. 发现不一致 → 标注优先级（P0/P1/P2）
4. 全部扫描完毕 → 先修复所有 P0，再评估 P1，P2 可选
5. 修复后重新编译 → 确认零错误
```

### ⚠️ Banach 特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **博士学位的非常规路径** | 容易写成常规博士叙事 | page.md 搜索 "doctorate" "habilitation" |
| **公园偶遇的时间地点** | Planty 公园、1916 年 | page.md 搜索 "Planty" "Steinhaus overheard" |
| **Hahn–Banach 的优先权** | Hahn 版本命名但 Banach 更早 | page.md 搜索 "Hahn" "Banach" "extension" |
| **纳粹时期的生存细节** | "虱子喂养"的具体描述 | page.md 搜索 "Weigl" "lice" "typhus" |
| **Schauder 的死因** | 1943 年被纳粹杀害 | page.md 搜索 "Schauder" "murdered" |
| **Lwów 战后归属** | 划归苏联 | page.md 搜索 "annexed" "Soviet" |
| **苏格兰咖啡馆问题集** | 193 个问题的确切数量 | page.md 搜索 "Scottish Book" "193" |
| **白鹰勋章年份** | 2018 追授，非在世荣誉 | page.md 搜索 "White Eagle" "posthumously" |

### 优先级定义

| 优先级 | 定义 | Banach 实际案例 |
|:--:|------|------|
| 🔴 P0 | **事实错误** | "Banach 毕业于 Lwów 理工大学"；"Banach 发现了 Hahn–Banach 定理" |
| 🟡 P1 | **来源存疑/捏造** | 无法验证的咖啡馆引语；公园偶遇的过度渲染 |
| 🟢 P2 | **重要遗漏** | 苏联占领期的 Sobolev 和 Kolmogorov 访问；Orlicz 空间 |
| ⚪ P3 | **可选补充** | 活鹅奖励的完整故事；Banach 的婚姻与家庭细节 |

---

## 第 14 步：音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

巴拿赫的气质：**温暖、醇厚、波兰土地的朴实、咖啡馆的亲密感、战争的伤痕** — 避免过于宏大的交响乐，苏格兰咖啡馆不适合管弦乐队尺度。

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | Nostalgia | alex-productions | `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` | 怀旧温和，Lwów 咖啡馆的黄金时代 |
| ★★★ | With Me | alex-productions | `music_audio/alex-productions/83-DXAblXGck-k-With-Me.wav` | 温和稳定，人物传记段落 |
| ★★ | Tragedy | alex-productions | `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav` | 深色戏剧性，战争伤痕与 Schauder 之死 |
| ★ | SEA | alex-productions | `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` | 流动平稳，泛函分析的连续叙事 |

**操作**：复制选定的 `.wav` 到 `Stefan_Banach/` 目录，`make video` 自动混入。

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `mathematician/presentations/Mathematician_Biography_Guide.md` | 完整操作手册（§二十 社会关系 / §二十一 字段梳理） |
| `mathematician/pages/Stefan_Banach/page.md` | Banach Wikipedia 正文 |
| `mathematician/pages/Stefan_Banach/metadata.json` | Banach Wikidata 元数据 |
| `mathematician/pages/Stefan_Banach/images.txt` | 图片 URL 清单 |
| `MySQL/seed_banach_relations.py` | 社会关系入库脚本（第 4.5 步） |
| `MySQL/seed_banach_full.py` | 全字段补全脚本（第 0.5 步） |
| `mathematician/presentations/godel/Kurt_Godel_zh.tex` | Gödel 完整源码（最新参考） |
| `mathematician/presentations/kolmogorov/Andrey_Kolmogorov_zh.tex` | Kolmogorov 完整源码 |

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Banach 的独特性不在于"他发现了什么定理"——而在于他**创建了泛函分析的语言本身**
> 2. 苏格兰咖啡馆不是修饰——它是数学史最真实、最浪漫的工作场景
> 3. 不要写成"苦难叙事"——Lwów 黄金时代的欢乐和创造力应该和战争悲剧同等篇幅
> 4. Banach 空间的定义简单到可以写在一页幻灯片里——但它是整个现代分析的基石
> 5. Schauder 的死亡是必要的叙事节点——它让战争的毁灭力具体化
> 6. 活鹅是真实的——这不需要过度渲染，它本身就很有力量
> 7. 三大基本定理每一定理都需要一句话直观解释——不要只列名字
> 8. **数据库同步**：先完成第 0.5 步（⚠️ 补全 people 主表的 gender/生卒/中文名，再补职业/获奖/机构）与第 4.5 步（8 条社会关系、5 人占位），再开始立传
> 9. 白鹰勋章（2018 追授）不入库——只收同时代荣誉（波兰学习院 1924）
> 10. 结尾主题句：**"在咖啡馆的烟雾中，一群波兰数学家发明了现代分析的语言。"**
