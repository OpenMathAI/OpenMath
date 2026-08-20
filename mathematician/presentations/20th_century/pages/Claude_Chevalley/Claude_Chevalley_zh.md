# 谢瓦莱 (Claude Chevalley) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)。参考: cartan, weyl, lebesgue, milnor, morse, zariski, whitney 的版式。

---

## 背景信息

- **目标**: Claude Chevalley (1909–1984)
- **气质关键词**: **Bourbaki 创始成员、Chevalley 群的构造者、李型有限单群的奠基人、代数群与概形论的先驱**
- **Wikipedia**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Claude_Chevalley/`

## 第 0 步：Wikipedia 校验

- **全名**：Claude Chevalley（法语发音 [ʃəvalɛ]）
- **生卒**：1909-02-11 ~ 1984-06-28，享年 75 岁
- **国籍**：法国 + 美国（双重国籍，二战期间入籍美国）
- **出生地**：Johannesburg, Transvaal Colony（今南非），父为法国外交官
- **去世地**：巴黎第 18 区，法国
- **博士导师**：**René Garnier**（巴黎大学，1933）⚠️ 不是 Picard！（Wikipedia 说他曾在 ENS 跟 Picard 学习，但官方博士导师是 Garnier）
- **博士论文**：1933，类域论（用代数方法消除 L-函数的依赖）
- **教育**：École Normale Supérieure (1929 毕业) → Hamburg (Emil Artin) → Marburg (Helmut Hasse) → Paris (博士)
- **任职**：Princeton (1939–1947)、Columbia (1947–1955)、巴黎大学 / Paris VII (1957–1978)
- **荣誉**：Cole 数论奖 (1941)、Guggenheim Fellowship、Prix Francoeur、Cours Peccot
- **学生**：Michel Broué, Gerhard Hochschild, Leon Ehrenpreis, Lê Dũng Tráng, Michèle Vergne
- **合作者**：André Weil (Bourbaki 同事+挚友)、Henri Cartan (Séminaire Cartan–Chevalley)、Armand Borel (代数群)
- **父亲**：Abel Chevalley——法国外交官，与妻子合编《The Concise Oxford French Dictionary》
- **ACM Chevalley 奖**：AMS 于 2014 设立 Chevalley Prize in Lie Theory

### 时间线
- 1909-02-11: 生于南非约翰内斯堡，父为法国外交官
- 1926–1929: ENS 学习，师从 Émile Picard
- 1929–1930s: 先后赴德国 Hamburg (Emil Artin) 和 Marburg (Helmut Hasse) 深造，结识日本数学家弥永昌吉 (Iyanaga)
- 1933: 博士，导师 René Garnier。论文用代数方法重构类域论
- 1935: Bourbaki 创始成员（与 Weil, Cartan, Dieudonné 等）
- 1936: 出版《矩阵代数中的算术》
- 1939: 二战爆发时恰在 Princeton，无法返回法国，留在美国
- 1939–1947: Princeton 大学。期间成为美国公民，著作多用英文
- 1940: 发表 "La théorie du corps de classes"
- 1941: 获 Cole 数论奖
- 1946: 出版《Theory of Lie Groups》——经典著作
- 1947–1955: Columbia 大学
- 1950s: 完成三卷 Lie 群论著
- 1955: 发表 "Sur certains groupes simples" —— **Chevalley 群** 的构造。9/18 族有限单群由此诞生
- 1955–1956: **Séminaire Cartan–Chevalley**——概形论(scheme theory)的起源。后被 Grothendieck 大力发展
- 1955–1958: Séminaire Chevalley——代数群的系统分类
- 1957: 经历 Weil 著名的 "Science Française?" 论战后，最终获巴黎大学教职
- 1970: 转入 Université de Paris VII
- 1978: 退休
- 1984-06-28: 在巴黎去世，享年 75 岁
- 2014: AMS 设立 Chevalley Prize in Lie Theory

### 人格画像
Chevalley 是一个典型的"Bourbaki 人格"：追求极致的抽象与严格。他与 Weil 是 Bourbaki 中最亲密的朋友——Weil 甚至为他写了一篇名为 "Science Française?" 的檄文，抨击法国学术体制拒绝给 Chevalley 教职。Chevalley 同时也是 1930 年代法国"非从众主义者"(non-conformists) 的一员——既投身前卫政治，也热衷前卫艺术。他的论文集编辑写道："数学是他生命中最重要的部分，但他从未在数学与生活的其余部分之间画任何界限。"

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_chevalley_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q634850` | ⚠️ 待核 |
| 2 | `people` | name_zh | `克劳德·谢瓦莱` | ✅ 已有 |
| 3 | `people` | name_variants | `["布尔巴基创始人之一","Chevalley 群之父","代数群理论的奠基者"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1909-02-11` / `1984-06-28` | ⚠️ **NULL 全缺** |
| 6 | `people` | description | `French mathematician (1909–1984)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`university teacher(1)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `mathematics`、`algebra` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Guggenheim`、`Cole Prize in Number Theory`、`Prix Francoeur`、`Cours Peccot` | ⚠️ 空 |
| 10 | `person_institution` | 教育/任职 | `education: ENS、Hamburg、Marburg、Paris`；`employment: Princeton、Columbia、Paris` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `France` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见第 4.5 步（7 条） | ⚠️ 仅 3 条 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。新建 `MySQL/seed_chevalley_relations.py` 补足。

**入库范围（7 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | René Garnier → Chevalley | 有向 | ⚠️ 占位 |
| 学生 | Chevalley → Michel Broué | 有向 | ✅ 在库（id=400） |
| 学生 | Chevalley → Gerhard Hochschild | 有向 | ⚠️ 占位 |
| 学生 | Chevalley → Léon Ehrenpreis | 有向 | ⚠️ 占位 |
| 同事 | André Weil | 无向 | ✅ 在库（id=8，布尔巴基） |
| 同事 | Henri Cartan | 无向 | ✅ 在库（id=69，布尔巴基） |
| 同事 | Jean Dieudonné | 无向 | ✅ 在库（id=370，布尔巴基） |

- 缺失人物（3 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`

---

## 核心贡献

| 领域 | 具体贡献 | 年代 |
|------|---------|:--:|
| 群论 | **Chevalley 群** — 9/18 族有限单群的统一构造 | 1955 |
| 代数群 | **代数群系统理论** — Séminaire Chevalley (1956–58) | 1950s |
| 类域论 | **类域论的代数化** — 消除 L-函数依赖，用代数方法 | 1933/1940 |
| 数论 | **Chevalley–Warning 定理** — 有限域上方程的可解性 | 1935 |
| 代数几何 | **Chevalley 定理** — 可构造集的像仍是可构造集 | 1950s |
| 李理论 | **Chevalley basis** — 半单李代数的整基 | 1950s |
| 代数拓扑 | **Chevalley–Eilenberg 代数** — Lie 代数上同调 | 1948 |
| 概形论 | **Séminaire Cartan–Chevalley** — 概形论的起源 | 1955–56 |
| Bourbaki | **创始成员** | 1935 |
| 教科书 | **多部经典** — Lie 群三卷、代数函数论、旋量论 | 1946–1958 |

### ★ 叙事主线
1. **Chevalley 群：李群的有限版本** — Chevalley 的核心贡献是发现：任何复半单李代数的 Chevalley basis 在任意域上定义了一个群——在有限域上，这恰好是有限单群。9 个族（占 18 族的一半）由 Chevalley 群而来。
2. **Bourbaki 的创始人之一** — 1935 年与 Weil, Cartan, Dieudonné 等人创建了 20 世纪最有影响力的数学集体。Chevalley 负责群论和代数部分。
3. **南非出生 → 法国 → 德国 → 美国 → 法国的全球旅程** — 生于外交官家庭，在德国跟随 Artin 和 Hasse 学习，二战后滞留美国且入籍，1957 年历经波折返回巴黎。
4. **Weil 的"Science Française?"** — Chevalley 申请巴黎大学教职时遭遇困难，Weil 在《新法兰西评论》发表檄文。这是法国数学界的一段著名公案。
5. **概形论的种树人** — Séminaire Cartan–Chevalley (1955–56) 是 Grothendieck 概形论的直接源头。Chevalley 种下了种子，Grothendieck 让它长成了森林。

## ⚠️ 史实陷阱
- **博士导师** — **不是 Picard！** René Garnier 是官方博士导师。Chevalley 在 ENS 跟 Picard 学习过，但论文指导教授是 Garnier。
- **Chevalley 群与有限单群分类** — Chevalley 贡献了 9/18 个族 ≠ 完成了分类。最终分类由数十人在 1980s 才完成。
- **Bourbaki 角色** — 创始成员，但不如 Weil 和 Dieudonné 那样是 "leader"。Chevalley 的贡献主要在群论和代数的部分。
- **Chevalley–Tarski 定理** — 这个"定理"在 Wikidata 中没有。逻辑学家把 Chevalley 关于可构造集的结果称为"量词消去"，但这与 Tarski 的关系是间接的。应使用 **Chevalley 定理（可构造集）** 而非 Chevalley–Tarski。
- **美国国籍** — 二战期间滞留美国时入籍。许多文献标注他同时有法美双重国籍。Weil 在 "Science Française?" 事件中提及这一点——有人用"美国化"来质疑他的法国学术正统性。
- **Séminaire Cartan–Chevalley** — 这是概形论的起点——但 Grothendieck 的发展太快太彻底，以至于历史痕迹几乎被覆盖。Chevalley 是策源地之一。

## ⚠️ 终审高危
| 高危点 | 正确值 | 常见错误 |
|--------|--------|----------|
| 博士导师 | René Garnier | Picard |
| 国籍 | 法国 + 美国 | 仅法国 |
| Chevalley 群 | 1955, 9/18 族 | 全部 18 族 |
| Chevalley–Tarski | 应称 Chevalley 定理(可构造集) | Chevalley–Tarski |
| Séminaire C-C | 1955–56, 概形论起源 | 未提及 |
| Weil 檄文 | "Science Française?" | 遗漏 |
| AMS Chevalley 奖 | 2014 设立 | 遗漏 |

## 配色：Bourbaki 深灰 + 代数蓝 + 南非金 + 银灰
- **badgeGroups** (群论/Chevalley 群) — 代数蓝 `#002147`
- **badgeBourbaki** (Bourbaki) — 深灰 `#2F3542`  
- **badgeAlgebra** (代数群/类域论) — 南非金 `#D4A017`
- **badgeLegacy** (遗产) — 银灰 `#A8A8A8`
- **coveraccent** — 代数蓝 `#002147`
- **coverprimary** — 墨色 `#111827`
- **bgmain** — 暖象牙白 `RGB{248,246,243}`

## 幻灯片（15 页内容 + 封面 + 结束 = 17 页）

### 0. OpenMath 项目首页
使用 `\openmathslide`

### 1. 封面 — 《谢瓦莱：Bourbaki 的群论之手》
- 大标题：克劳德·谢瓦莱
- 副标题：Claude Chevalley · 1909 — 1984
- 标签：Chevalley 群 · Bourbaki 创始人 · 代数群 · 类域论
- 底部：Cole 奖 1941 · Bourbaki 1935 · 双重国籍（法国/美国）
- 顶部右侧：头像（如可用）

### 2. Hook — 从李群到有限单群
- 四个面板：(1) Bourbaki 创始成员——1935 (2) Chevalley 群——9/18 族有限单群的统一构造 (3) 类域论代数化——消除 L-函数 (4) Séminaire Cartan–Chevalley——概形论起源
- 底部金句："他找到了李群的有限版本——从而开启了现代有限单群分类的大门。"

### 3. 早年：南非→巴黎→德国 (1909–1933)
- **1909** · 生于南非约翰内斯堡。父亲 Abel Chevalley 是法国外交官，与妻子合编了《牛津简明法英词典》。
- **1926–1929** · ENS，师从 Picard 等。毕业后赴德国：Hamburg (Emil Artin)、Marburg (Helmut Hasse)。结识日本数学家弥永昌吉。
- **1933** · 巴黎大学博士，导师 René Garnier。论文：类域论——用代数方法消除 L-函数的依赖。
- 底部金句："生于南非的法国外交官之子，在德国的代数圣地学成——一个注定国际化的数学人生。"

### 4. Bourbaki 的创始故事 (1935)
- **1935** · 与 Weil, Cartan, Dieudonné, Delsarte 共同创建 Nicolas Bourbaki。Chevalley 是创始成员中最年轻的几个之一（26 岁）。
- **角色**：负责群论和代数部分。Bourbaki 的目标——用公理化方法重写所有数学——与 Chevalley 的抽象思维完美契合。
- **影响**：Bourbaki 的《代数》卷深受 Chevalley 的影响。他后来半开玩笑地说 Bourbaki"扼杀了法国数学的直觉"。
- 底部金句："26 岁那年，他和几个朋友决定改写全部数学。他们没有成功——但他们改变了数学的面貌。"

### 5. 类域论与数论 (1933–1941)
- **博士论文 (1933)**：用代数方法重构类域论，消除了对 L-函数的依赖。这是类域论算术化的关键一步。
- **"La théorie du corps de classes" (1940)**：类域论的里程碑著作。Weil 在《Basic Number Theory》序言中说，该书的核心路径来自 Chevalley 一份未发表手稿。
- **Chevalley–Warning 定理 (1935)**：有限域上多项式方程组若有足够多变量，则解数被特征整除。数论与代数几何的交叉经典。
- **Cole 数论奖 (1941)**：37 岁获 AMS Cole Prize——数论最高荣誉。
- 底部金句："他让类域论不再依赖 L-函数——用纯代数替代了分析。"

### 6. 战时流亡：Princeton → Columbia (1939–1947)
- **1939** · 二战爆发时正在 Princeton，无法返回法国。留在美国——这是他人生的转折点。
- **Princeton (1939–47)** · 期间成为美国公民，大量著作改用英文写作。学生包括 Hochschild 和 Ehrenpreis。1946 年出版《Theory of Lie Groups》——英文经典。
- **Columbia (1947–55)** · 继续在美国教书。完成三卷 Lie 群论著 (1946–1955)。
- 底部金句："战争把他从巴黎推到了普林斯顿——命运却给了他一个跨大西洋的数学人生。"

### 7. Lie 群三卷 (1946–1955) — 经典教科书
- **卷 I (1946)**：《Theory of Lie Groups》(Princeton UP)。**卷 II (1951)**：代数群。**卷 III (1955)**：李代数的结构定理。
- **Chevalley basis**：半单李代数的整基——可以在任意域（不仅是实数/复数）上定义李代数。这是 Chevalley 群构造的前提。
- **贡献**：将李理论从实数/复数的依赖中解放出来——代数群理论的基础由此奠定。
- 底部金句："三卷 Lie 群——写完第三卷那年，他即将做出自己最伟大的发现。"

### 8. Chevalley 群 (1955) — 九族新有限单群
- **"Sur certains groupes simples" (1955, Tôhoku Math. J.)**：这篇论文构造了 Chevalley 群——复半单李代数的 Chevalley basis 在有限域上的群。
- **核心思想**：每个 Dynkin 图对应一族 Chevalley 群。取有限域 GF(q) 时，得到有限群——绝大多数是有限单群。
- **影响**：9 族新的有限单群被一次性构造出来——占 18 族的一半。有限单群分类的进度从此加速。
- **意义**：李理论（连续）与有限群论（离散）被 Chevalley 桥接在一起。
- 底部金句："一篇 53 页的论文，一次性地构造出了 9 族有限单群——这是群论史上最高产的单项工作。"

### 9. 有限单群分类的基石
- **Chevalley 群 = 9/18 族**：A_n, B_n, C_n, D_n, E_6, E_7, E_8, F_4, G_2。每个 Dynkin 图对应一族群。
- **扭 Chevalley 群 (Steinberg, Suzuki, Ree)**：Steinberg 等人在 Chevalley 的基础上构造了"扭"版本——额外 7 族。
- **最终分类 (1980s)**：18 族无穷族 + 26 个散在群 + 交替群。Chevalley 群是其中最大的组成部分。
- 底部金句："有限单群分类这部史诗中，Chevalley 写了一章——而且是最长的那一章。"

### 10. Chevalley–Warning 定理与代数几何
- **Chevalley–Warning 定理**：有限域上 n 元 m 次多项式组，若变量数 > 总次数，则解数 ≡ 0 (mod p)。数论与有限域的交叉。
- **Chevalley 定理（可构造集）**：可构造集（Zariski 开闭集生成的布尔代数）在代数簇态射下的像仍是可构造集。逻辑学家称此为"量词消去"。
- **Jordan–Chevalley 分解**：代数群中元素的半单-幂单分解。线性代数群理论的基本定理。
- 底部金句："从有限域方程到代数几何的可构造集——Chevalley 在不同尺度上刻画了'代数'的本质。"

### 11. 重返法国 & Séminaire Cartan–Chevalley (1955–1958)
- **1957 · "Science Française?"**：Weil 在《新法兰西评论》发表檄文，揭露法国学术体制拒绝 Chevalley 的教职申请。Chevalley 是文中 "professeur B"。最终 Chevalley 获巴黎大学教职。
- **Séminaire Cartan–Chevalley (1955–56)**：与 Henri Cartan 联合主持，讨论代数群和代数几何的基础。**这是概形论 (scheme theory) 的起源**。
- **Séminaire Chevalley (1956–58)**：系统分类代数群。后由 Pierre Cartier 修订再版 (2005)。
- 底部金句："他在巴黎的一次讨论班上种下了种子——Grothendieck 让这颗种子长成了概形论的参天大树。"

### 12. 代数群与晚年工作
- **代数群理论**：Chevalley 是线性代数群理论的先驱。与 Armand Borel 的合作深刻影响了这个领域。
- **旋量代数理论 (1954)**：《The Algebraic Theory of Spinors》——旋量的公理化处理，至今仍是经典。
- **代数函数论 (1951)**：《Introduction to the Theory of Algebraic Functions of One Variable》。
- **Chevalley–Eilenberg 代数**：Lie 代数上同调的基本工具。
- 底部金句："从李群到代数群、从类域论到旋量——他的数学版图横跨了代数、几何和数论。"

### 13. 荣誉与 Chevalley 奖
- **Cole 数论奖 (1941)**：AMS 颁发，表彰他在类域论和数论方面的贡献。
- **Prix Francoeur** · **Cours Peccot** · **Guggenheim Fellowship**
- **AMS Chevalley Prize in Lie Theory (2014 设立)**：以他命名的李理论奖。首奖得主 Geordie Williamson (2016)，后续 Dennis Gaitsgory (2018), Xuhua He (2022) 等。
- **名誉**：巴黎科学院通讯院士。1940 年代当选 American Philosophical Society。
- 底部金句："AMS 在 2014 年用他的名字命名了一个奖——以此纪念那位让李群与有限群握手的人。"

### 14. 那些以 Chevalley 命名的概念
- **Chevalley 群** — 9 族有限单群
- **Jordan–Chevalley 分解** — 半单-幂单分解
- **Chevalley–Warning 定理** — 有限域方程
- **Chevalley–Eilenberg 代数** — Lie 代数上同调
- **Chevalley basis** — 李代数的整基
- **Chevalley 定理** — 可构造集的像
- **Chevalley restriction theorem**
- **Chevalley–Shephard–Todd 定理**
- **Chevalley–Iwahori–Nagata 定理**
- **Chevalley scheme** — 概形论
- **Chevalley automorphism**
- **Séminaire Cartan–Chevalley** — 概形论起源
- **AMS Chevalley Prize** — 李理论奖
- 底部金句："以他命名的概念超过十二个——从群论到数论，从李代数到概形。"

### 15. 结束页
- 大引语："Il n'y a pas de frontière entre les mathématiques et la vie."（数学与生活之间没有边界。）
- 小字：克劳德·谢瓦莱 · Claude Chevalley · 1909 — 1984
- 底部：Bourbaki 创始成员 · Chevalley 群的构造者 · 代数群的先驱 · 法国/美国数学家

## 背景音乐选择 ✅

- **选定曲目**: **Timeless** — Alex-Productions (132k views, 最高受众)
- **风格**: 沉稳 / 纪录片 / 长期纲领
- **匹配理由**:
  - "长期纲领" 完美匹配 Chevalley 的贡献本质 —— Chevalley 群 (1955) 不是单一的突破，而是一个结构性的纲领：每个 Dynkin 图对应一族有限单群，一次性构造 9/18 族。Chevalley basis 让李代数可以在任意域上定义 —— 这不是征服，是奠基
  - "沉稳" 匹配 Bourbaki 的抽象气质 —— 公理化、严格化、系统化重写全部数学。Chevalley 是其中最安静的成员之一（不如 Weil 张扬，不如 Dieudonné 高产），但他负责的群论和代数部分是 Bourbaki 大厦的承重墙
  - "纪录片" 匹配传记叙事 —— 南非出生 → 巴黎 ENS → 德国 Artin/Hasse 门下 → 二战滞留美国入籍 → Weil "Science Française?" 檄文 → 1957 重返法国。不是探险，是命运推动的流亡与回归
  - Chevalley 的核心悲剧感也契合 Timeless 的深沉：Séminaire Cartan–Chevalley 是概形论的起源 —— 但种子是他种的，森林却是 Grothendieck 的。他种下结构，别人收获名声。晚年甚至批评 Bourbaki "扼杀了法国数学的直觉" —— 一个建造了抽象大厦的人，对自己参与的事业产生了反思
- **备选** (未采用):
  - ★★ Expedition — "探索/史诗" 匹配南非→法国→德国→美国→法国的跨洲旅程和 Weil 檄文事件的戏剧性，但 Chevalley 的本质不是远征者——他的旅程是被迫的流亡，不是主动的探索。Expedition 属于 Morse（登山家+一战勋章）和 Whitney（骨灰撒阿尔卑斯山顶），不属于 Bourbaki 的书斋建筑师
  - ★ PAST — "历史感/深沉" 匹配 Bourbaki 的时代背景和 Séminaire 的历史意义，但受众偏低 (86k)
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → `presentations/Claude_Chevalley/Timeless.wav`
- **时长**: 128 秒 > 17 页 × 7 秒 = 119 秒 → ffmpeg `-shortest` 自动对齐

## Round 2 高危: 博士导师 Garnier 非 Picard、双重国籍、Chevalley–Tarski 应为 Chevalley 定理(可构造集)、Séminaire Cartan–Chevalley、Weil 檄文、Chevalley 群 = 9/18 族。

> **开始执行。**
