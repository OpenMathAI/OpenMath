# 扎里斯基 (Oscar Zariski) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)。参考: cartan, weyl, lebesgue, serre 的版式。

---

## 背景信息

- **目标**: Oscar Zariski (1899–1986)，原名 Ascher Zaritsky
- **气质关键词**: **代数几何的代数化先驱、意大利学派的终结者、Zariski 拓扑的创立者**
- **Wikipedia**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Oscar_Zariski/`

## 第 0 步：Wikipedia 校验

- **生卒**：1899-04-24 ~ 1986-07-04，享年 87 岁
- **国籍**：美国（生于俄罗斯帝国，今白俄罗斯）
- **出生地**：Kobryn, Russian Empire (now Belarus)
- **博士导师**：Guido Castelnuovo（罗马大学, 1925）
- **博士论文**：伽罗瓦理论，由 Castelnuovo 命题（1924年完成，1926年发表）
- **任职**：约翰·霍普金斯大学 (1927–1945)、伊利诺伊大学 (1946–1947)、哈佛大学 (1947–1969)
- **荣誉**：Wolf 奖 (1981)、Steele 奖 (1981)、美国国家科学奖章 (1965)、伦敦数学会荣誉会员
- **学生**：Heisuke Hironaka（奇点解消，Fields 奖 1970）、David Mumford（Fields 奖 1974）、Michael Artin、Steven Kleiman、Joe Lipman
- **学术谱系**：Castelnuovo → Zariski → Hironaka, Mumford, Artin（三代 Fields 奖得主链）

### 时间线
- 1899-04-24: 生于白俄罗斯 Kobryn（当时属俄罗斯帝国），犹太家庭
- 1918: 因俄国革命和反犹浪潮，流亡至基辅→意大利
- 1921: 入读罗马大学，师从 Castelnuovo —— 加入意大利代数几何学派
- 1925: 博士。随后发现意大利学派的"直觉几何"方法缺乏严格性
- 1926: 博士论文发表。发表时将名字从 Ascher Zaritsky 改为 Oscar Zariski
- 1927: 由 Solomon Lefschetz 帮助，移民美国，加入约翰·霍普金斯大学
- 1935: 出版《代数曲面》(Algebraic Surfaces) —— 用代数方法重写意大利学派成果
- 1939: 获 Guggenheim Fellowship
- 1940: 引入 Zariski 拓扑 —— 代数簇上以代数子簇为闭集的拓扑
- 1944: 获 Cole Prize in Algebra
- 1944–1946: 在巴西圣保罗大学访问，1945 年与 André Weil 深入交流代数几何的严格化
- 1946–1947: 伊利诺伊大学
- 1947: 受聘哈佛大学 Dwight Parker Robinson 讲席教授
- 1950s: 在奇点理论、局部环理论中取得突破；提出奇点解消猜想
- 1958: 与 Pierre Samuel 合著《交换代数》两卷 —— 成为该领域必读经典
- 1964: 学生 Hironaka 证明奇点解消定理（特征 0），获 Fields 奖
- 1965: 获美国国家科学奖章
- 1969: 从哈佛退休；当选美国数学会 (AMS) 主席 (1969–1970)
- 1981: 获首届 Wolf 数学奖（与 Lars Ahlfors 共享）
- 1986-07-04: 在马萨诸塞州 Brookline 去世，享年 87 岁

### 人格画像
安静、谦逊但极有主见。Zariski 不是一个张扬的革命者——他更像一个工匠：用代数工具一块一块地替换意大利学派基于直觉的论证。他曾说："我不相信几何直觉——我要求代数证明。"他对学生极其慷慨，培养出了 Hironaka、Mumford、Artin 等一代大师。晚年回顾时他说："我一生做的事就是让代数几何变得严格。"

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_zariski_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q381307` | ⚠️ 待核 |
| 2 | `people` | name_zh | `奥斯卡·扎里斯基` | ⚠️ NULL |
| 3 | `people` | name_variants | `["代数几何的公理化者","意大利学派的美国传人","Zariski 拓扑"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1899-04-24` / `1986-07-04` | ⚠️ 仅年份 |
| 6 | `people` | description | `American mathematician (1899–1986)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`university teacher(1)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `algebraic geometry`、`mathematics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Cole 1944`、`NMS 1965`、`Wolf 1981`（已有）、`Steele 1981`、`Guggenheim` | ⚠️ 部分 |
| 10 | `person_institution` | 教育/任职 | `education: Sapienza Rome、Kyiv`；`employment: Johns Hopkins、Illinois、Harvard、São Paulo` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `Russian Empire`、`United States` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见第 4.5 步（7 条） | ⚠️ 全空 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。新建 `MySQL/seed_zariski_relations.py`。

**入库范围（7 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | Guido Castelnuovo → Zariski | 有向 | ⚠️ 占位（意大利学派） |
| 学生 | Zariski → David Mumford | 有向 | ✅ 在库（id=36） |
| 学生 | Zariski → Michael Artin | 有向 | ✅ 在库（id=190） |
| 学生 | Zariski → Robin Hartshorne | 有向 | ⚠️ 占位 |
| 学生 | Zariski → Heisuke Hironaka | 有向 | ⚠️ 占位 |
| 同事 | André Weil | 无向 | ✅ 在库（id=8） |
| 同事 | Solomon Lefschetz | 无向 | ✅ 在库（id=54） |

- 缺失人物（3 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`

---

## 核心贡献

| 领域 | 具体贡献 | 年代 |
|------|---------|:--:|
| 代数几何 | **Zariski 拓扑** — 代数簇上闭集=代数子簇的拓扑 | 1940 |
| 代数几何 | **双有理变换的代数化** — 用赋值环替代意大利学派的几何操作 | 1930s–1940s |
| 奇点理论 | **奇点解消的猜想与局部理论** — 特征 0 情形由 Hironaka 完成 | 1950s–1964 |
| 交换代数 | **Zariski–Nagata 纯性定理**、Zariski 主定理 | 1950s |
| 教科书 | **《交换代数》**(与 Samuel 合著, 1958) —— 一代数学家的标准教材 | 1958 |
| 代数曲面 | **《代数曲面》**(1935, 1971 增补版) —— 严格化意大利学派成果 | 1935/1971 |

### ★ 叙事主线
1. **意大利学派的"背叛者"** — Zariski 是意大利学派的嫡传弟子（Castelnuovo 的学生），但他用代数严格性"终结了"这个学派的方法论。这不是背叛，是超越。
2. **Zariski 拓扑的革命性** — 在代数簇上定义拓扑，使得"闭集=代数子簇"。这看似简单，但为 Grothendieck 的概形论铺平了道路。Zariski 拓扑是代数几何从"几何直觉"走向"代数结构"的关键一步。
3. **三代 Fields 奖得主链** — Castelnuovo → Zariski → Hironaka & Mumford。他本人未获 Fields 奖（因年龄限制），但他的学生和学生的学生都是 Fields 奖得主。
4. **俄国→意大利→美国的移民** — 三次被迫迁移，三种文化交汇，最终在哈佛成为一代宗师。
5. **代数比几何更可靠** — 他一生的信条：不要相信你的眼睛，相信你的代数。

## ⚠️ 史实陷阱
- **不是 Grothendieck** — Zariski 的代数化 ≠ Grothendieck 的概形论。Zariski 在 Grothendieck 之前，他的 Zariski 拓扑是 Grothendieck 概形论的必要前提。关系：Zariski 提供了舞台（拓扑），Grothendieck 重写了剧本（概形）。
- **Zariski 拓扑的含义** — 1940 年引入。闭集 = 代数子簇（即多项式方程零点集）。这个拓扑非常粗糙（非 Hausdorff），但恰好捕捉了代数簇的代数结构。不是所有闭集都是"曲线"——任何代数子簇都是闭集。
- **意大利学派的"缺陷"** — 不是他们"错了"。意大利学派（Castelnuovo, Enriques, Severi）发现和分类了大量代数曲面，成果惊人。但他们的方法依赖"几何直觉"和"图形论证"，很多证明不严格。Zariski 尊重他们的发现，但要求用代数方法重新验证一切。
- **出生地与原名** — Ascher Zaritsky, 生于 Kobryn, 今白俄罗斯（当时俄罗斯帝国）。"Zariski" 是意大利化后的拼写。
- **巴西岁月 (1944-1946)** — 在圣保罗与 Weil 的交流对代数几何严格化至关重要，不应遗漏。

## ⚠️ 终审高危
| 高危点 | 检查 |
|---------|------|
| 出生地与原名 | Ascher Zaritsky (Osher), Kobryn (Belarus, 当时俄罗斯帝国) |
| 博士导师 | Guido Castelnuovo, 罗马大学, 1925 (论文1924完成, 1926发表) |
| 博士论文 | 伽罗瓦理论（非代数曲面/意大利学派） |
| Zariski 拓扑 | 1940, 闭集=代数子簇 |
| 学生 Hironaka | 1964 奇点解消, Fields 奖 1970 |
| 学生 Mumford | Fields 奖 1974 |
| Wolf 奖 | 1981 (首届，与 Ahlfors 共享) |
| Cole Prize | 1944 (遗漏高危) |
| 巴西岁月 | 1944–1946, 与 Weil 交流 (1945) |
| 《代数曲面》 | **1935** (非1937), 1971 增补版 |

## 配色：白俄罗斯暖金 + 哈佛深红 + 石板灰 + 象牙白
- **badgeZtop** (Zariski 拓扑) — 哈佛深红 `#A51C30`
- **badgebirat** (双有理/代数化) — 暖金 `#D4A017`  
- **badgecomm** (交换代数) — 石板灰 `#5A5A5A`
- **badgelegacy** (传承/学生) — 靛蓝 `#2E4057`
- **coveraccent** — 哈佛深红 `#A51C30`
- **coverprimary** — 深棕色 `#3B2F2F`
- **bgmain** — 暖象牙白 `RGB{248,245,240}`

## 幻灯片（15 页内容 + 封面 + 结束 = 17 页）

### 0. OpenMath 项目首页
使用 `\openmathslide`

### 1. 封面 — 《扎里斯基：代数几何的严格化者》
- 大标题：奥斯卡·扎里斯基
- 副标题：Oscar Zariski · 1899 — 1986
- 标签：Zariski 拓扑 · 双有理变换 · 交换代数 · 代数曲面
- 引用："我不相信几何直觉——我要求代数证明。"
- 右上角肖像（如可用）
- 底部：Wolf 奖 1981 · 美国国家科学奖章 1965 · 哈佛大学

### 2. Hook — 从意大利的直觉到代数的严格
- 四个面板：(1) 意大利学派嫡传 — Castelnuovo 的学生 (2) 发现"直觉"的不足 — 很多证明不严格 (3) 用代数重建一切 — 赋值环 + 局部环 (4) 为 Grothendieck 铺路 — Zariski 拓扑
- 底部金句："他学的是几何，用的是代数的刀。"

### 3. 早年与求学：俄→意→美 (1899–1927)
- **1899** · 生于白俄罗斯 Kobryn，犹太家庭。幼年体弱多病，但数学天赋极高。
- **1918** · 俄国革命 + 反犹迫害 → 流亡意大利。途中失去大部分家人。
- **1921** · 入读罗马大学，师从 Castelnuovo。意大利代数几何学派的黄金时代——Severi, Enriques 都在那里。
- **1927** · 博士毕业。因意大利反犹政策抬头（墨索里尼时期），移民美国。
- 底部金句："三次被迫离开家园——最终在数学中找到了永恒的故乡。"

### 4. 意大利代数几何学派的辉煌与"缺陷"
- **意大利学派的成就**：Castelnuovo, Enriques, Severi 用几何直觉分类了大量代数曲面，成果惊人。
- **方法论问题**：(1) 依赖"图形论证"——画图证明 (2) "显然可约"有时不显然 (3) 缺乏严格的代数基础 (4) 很多"证明"后来被发现有空隙
- **Zariski 的态度**：尊重发现，但不接受方法。他决定用代数和拓扑重建一切。
- 底部金句："他们的眼睛看到了真相——但他们的手没有证明它。"

### 5. Zariski 拓扑 (1940) — 代数几何的"新眼睛"
- **定义**：在代数簇上定义拓扑，闭集 = 代数子簇（多项式方程组的零点集）。
- **特性**：(1) 非常粗糙——开集很少 (2) 非 Hausdorff——两点不一定能被开集分开 (3) 但恰好捕捉了代数簇的"代数"结构
- **为何重要**：(1) 让"连续"和"代数"可以对话 (2) 为层论 (sheaf theory) 提供了自然的底空间 (3) Grothendieck 在 Zariski 拓扑上建造了概形论
- **比较**：Zariski 拓扑之于代数几何 ≈ 度量拓扑之于实分析
- 底部金句："他给代数簇装上了一套新的神经系统。"

### 6. 双有理变换的代数化 (1930s–1940s)
- **问题**：意大利学派用"吹胀"(blow up) 和"收缩"(blow down) 等几何操作处理双有理变换。但这些操作在严格意义下是什么？
- **Zariski 的方案**：用赋值环 (valuation ring) 替代几何直觉。每个双有理变换对应一个赋值环，用代数语言精确描述。
- **Zariski 主定理**：正规簇的双有理→同构（局部意义下）。这是代数几何一系列"主定理"的鼻祖。
- 底部金句："他说：不要画图，写下方程。"

### 7. 奇点理论与局部环 (1950s)
- **问题**：代数簇上的奇点是什么？如何"消除"奇点？
- **Zariski 的方法论**：用局部环 (local ring) 研究奇点的局部结构。一个点在簇上是光滑的 ⟺ 对应的局部环是正则局部环。
- **奇点解消猜想**：任何代数簇都可以通过一系列 blow-up 变为光滑簇（特征 0）。Zariski 证明了曲面（维数 2）的情形，并提出了三维的猜想。
- 底部金句："奇点不是缺陷——它们是代数几何的DNA。"

### 8. Hironaka 与奇点解消 (1964) — 学生完成导师的梦想
- **Hironaka**：Zariski 在哈佛的学生，日本数学家。
- **1964 定理**：特征 0 的代数簇上，奇点解消总是可能的（任意维数）。震惊世界。
- **Fields 奖 1970**：Hironaka 因此获得 Fields 奖。
- **师承的意义**：Zariski 证明了 dim≤2 情形、提出了 dim=3 的猜想、发展了局部环理论——Hironaka 站在巨人的肩膀上。
- 底部金句："导师画了地图，学生登上了顶峰。"

### 9. 《交换代数》(1958) — 与 Samuel 合著的经典
- **两卷本**：卷一基础理论（理想、模、局部化、整扩张），卷二赋值论（赋值环、Dedekind 整环、完备化）
- **影响**：(1) 一代数学家的标准教材 (2) 用"Zariski-Samuel"说法已成为交换代数的代名词 (3) 直接哺育了 Grothendieck 的 EGA/SGA
- **风格**：清晰、严格、全面——典型的 Zariski 风格（没有多余的修辞）
- 底部金句："这本书不是让你欣赏——是让你学会交换代数。"

### 10. 哈佛岁月 (1947–1969) — 美国代数几何的奠基人
- **1947**：受聘哈佛 Dwight Parker Robinson 讲席教授
- **哈佛之前**：约翰·霍普金斯 (1927–1945) → 巴西圣保罗 (1944–46) → 伊利诺伊 (1946–47) → 哈佛
- **哈佛的影响**：(1) 建立了美国代数几何学派 (2) 培养了 Hironaka, Mumford, Artin, Kleiman, Lipman (3) 使哈佛成为 1950-70 年代代数几何的世界中心之一
- **个人风格**：安静的办公室、耐心的导师、对数学严格性的执念
- 底部金句："他从意大利带来了种子，在美国种下了一片森林。"

### 11. 意大利学派的终结者 — 一场安静的革命
- **不是对抗是超越**：Zariski 从未公开攻击意大利学派。他用行动说话——把他们的成果用代数严格证明一遍。
- **《代数曲面》**(1935, 1971 增补版)：意大利学派关于代数曲面的一切，被 Zariski 用代数语言重写。
- **历史意义**：意大利学派的发现没有消失——它们被吸收进严格化的代数几何中。Zariski 不是毁灭者，是翻译者。
- 底部金句："他没有推翻大厦——他换了地基。"

### 12. 学生：三代 Fields 奖得主链
- **导师 Castelnuovo**：意大利学派领袖
- **Zariski 本人**：未获 Fields 奖（年龄限制），但获 Wolf 奖（1981）
- **学生 Hironaka**：Fields 奖 1970（奇点解消）
- **学生 Mumford**：Fields 奖 1974（模空间理论、代数几何）
- **学生 Artin**：代数几何与代数论大师，虽未获 Fields 奖但影响深远
- **谱系意义**：Castelnuovo → Zariski → Hironaka, Mumford, Artin → 下一代
- 底部金句："他没有拿到那个奖——但他的学生拿了两个。"

### 13. Wolf 奖与荣誉 (1981) — 迟到的加冕
- **Wolf 奖 1981**：首届 Wolf 数学奖得主之一（与 Lars Ahlfors 共享）。评语：表彰他对代数几何的代数基础的根本性贡献。
- **美国国家科学奖章 (1965)**：由总统颁发，美国最高科学荣誉。
- **Steele 奖 (1981)**：美国数学会终身成就奖。
- **其他荣誉**：伦敦数学会荣誉会员、美国国家科学院院士、美国艺术与科学院院士
- 底部金句："78 岁时，他用一个奖，证明了 60 年前的选择是对的。"

### 14. 扎里斯基的遗产 — Zariski 拓扑之后
- **Zariski 拓扑**：从 "代数簇上的奇怪拓扑" 变成了代数几何的标准语言。
- **概形论**：Grothendieck 在 Zariski 拓扑的基础上定义了概形（scheme），开创新纪元。
- **交换代数**：Zariski-Samuel 至今仍是基础教材。
- **美国学派**：哈佛→MIT→Berkeley 的代数几何传统源于 Zariski。
- **命名的概念**：Zariski 拓扑、Zariski 切空间、Zariski 主定理、Zariski 环、Zariski–Nagata 定理……
- 底部金句："一个概念以一个人命名，是荣誉。十多个概念以同一个人命名，是基石。"

### 15. 结束页 — 引语页
- 大引语："我不相信几何直觉——我要求代数证明。"
- 小字：奥斯卡·扎里斯基 · Oscar Zariski · 1899 — 1986
- 底部：代数几何的严格化者 · 意大利学派的终结者 · Zariski 拓扑的创立者

## 背景音乐选择 ✅

- **选定曲目**: **Timeless** — Alex-Productions (132k views, 最高受众)
- **风格**: 沉稳 / 纪录片 / 长期纲领
- **匹配理由**:
  - "沉稳" 匹配 Zariski 安静谦逊的工匠气质 —— 他不用革命的语言，而是用代数工具一块一块替换几何直觉
  - "纪录片" 匹配传记 17 页叙事 —— 从 Kobryn 到罗马，从 Hopkins 到哈佛，三代 Fields 奖传承链
  - "长期纲领" = Timeless —— Zariski 拓扑 (1940) 在 Grothendieck (1960s) 手中开花；Zariski-Samuel 至今仍是标准教材；他严格化代数几何的工作跨越了四十余年
  - 不像 Expedition 过于"史诗"（Zariski 不是征服者，是重建地基的人），不像 Awaken 过于"明亮"（Zariski 的克制品格需要更深沉的声音）
- **备选** (未采用):
  - ★★ Expedition — "探索/史诗/几何拓扑" 匹配三次移民的漂泊旅程和拓扑创新，但史诗标签偏重
  - ★ PAST — "历史感/深沉" 匹配意大利学派的时代背景，但受众偏低 (86k views)
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → `presentations/Oscar_Zariski-W/Timeless.wav`
- **时长**: 128 秒 > 17 页 × 7 秒 = 119 秒 → ffmpeg `-shortest` 自动对齐

## Round 2 高危: 
1. **《代数曲面》年份** — Wikipedia 明确写 "published in 1935" 非 1937。1971 增补版 = 1935 + 36 年。
2. **博士论文题目** — Galois 理论 (Castelnuovo 命题)，非代数曲面/意大利学派。
3. **Cole Prize 1944** — 遗漏重要奖项。
4. **Guggenheim Fellowship 1939** + **AMS 主席 1969-1970** — 遗漏。
5. Zariski vs Grothendieck 时序关系 — Zariski 拓扑 (1940) 提供底空间，Grothendieck (1960s) 建造概形论。
6. 意大利学派的"缺陷"准确描述 — 用"直觉/不严格"而非"错误/失败"。
7. 出生地确认 — Kobryn, 今白俄罗斯 (当时俄罗斯帝国)。
8. Zariski 主定理 vs Grothendieck 版的关系 — ZMT 是 Grothendieck 版的前身。

> **开始执行。**
