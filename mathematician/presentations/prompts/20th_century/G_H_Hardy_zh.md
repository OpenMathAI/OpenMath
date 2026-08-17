# G.H. 哈代 (G.H. Hardy) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)，以 Milnor、Atiyah、Thurston 等成品为参考模板。

---

## 背景信息

- **目标数学家**: Godfrey Harold Hardy (1877–1947)
- **气质关键词**: **纯数学的守护者、英国数学的改革者、拉马努金的伯乐、解析数论的英国学派灵魂、板球鉴赏家、《一个数学家的辩白》**
- **Wikipedia 页面**: ✅ 已下载
  - 页面路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/G._H._Hardy/`
- **参考模板**: `milnor/`, `atiyah/`, `thurston/`

---

## 第 0 步：Wikipedia 页面校验

- **全名**: Godfrey Harold Hardy FRS
- **生卒**: 1877-02-07 ~ 1947-12-01，享年 70 岁
- **国籍**: 英国
- **出生地**: Cranleigh, Surrey, England
- **逝世地**: Cambridge, England（心脏病后自杀未遂，一日清晨听妹妹读板球史时猝逝）
- **博士导师**: A. E. H. Love, E. T. Whittaker
- **教育**: Winchester College → Trinity College, Cambridge
- **主要任职**:
  - 1906–1919: Trinity College, Cambridge 讲师
  - 1919–1931: Oxford 大学 Savilian 几何教授 (New College)
  - 1928–1929: Princeton 大学交换 (与 Oswald Veblen)
  - 1931–1942: Cambridge Sadleirian 纯粹数学教授
- **关键荣誉**:
  - 1901: Smith's Prize
  - 1910: FRS（皇家学会院士）
  - 1920: Royal Medal
  - 1929: De Morgan Medal
  - 1932: Chauvenet Prize
  - 1940: Sylvester Medal
  - 1947: Copley Medal（逝世当年）
- **重要合作者**:
  - J. E. Littlewood (1911–1945, 数学史上最伟大的合作)
  - Srinivasa Ramanujan (1914–1919, "一生中唯一的浪漫事件")
  - E. M. Wright (合著《数论导引》)
- **重要学生**: Mary Cartwright, E. C. Titchmarsh, Donald C. Spencer, Harry Pitt, Richard Rado, Robert Rankin

### 关键时间线:
- 1877: 2月7日生于英国萨里郡 Cranleigh 教师家庭
- 2岁: 写数字到百万位，在教堂因式分解赞美诗编号
- 1896: 入读剑桥三一学院
- 1900: 当选 Trinity Prize Fellowship
- 1901: 获 Smith's Prize
- 1906: Trinity 讲师
- 1908: 出版《纯数学教程》(A Course of Pure Mathematics)——改变了英国数学教育
- 1908: 独立发现 Hardy–Weinberg 原理（与板球伙伴 Punnett 的聊天中）
- 1911: 开始与 Littlewood 长达35年的合作
- 1913.1.16: 收到 Ramanujan 来信——"一生中唯一的浪漫事件"
- 1914: Ramanujan 到达剑桥
- 1917: 与 Ramanujan 合作证明整数分拆的渐近公式
- 1919: 因 Russell 事件离开剑桥，赴牛津任 Savilian 几何教授
- 1920: Hardy–Littlewood 圆法——解析数论的核心工具
- 1928–1929: 普林斯顿交换，Gibbs 讲座
- 1931: 返回剑桥任 Sadleirian 教授
- 1938: 与 E. M. Wright 合著《数论导引》——至今标准教材
- 1939: 冠心病，创造力衰退
- 1940: 出版《一个数学家的辩白》(A Mathematician's Apology)
- 1947: 获 Copley Medal，自杀未遂，12月1日逝世

### 人格特质:
- 2岁能在教堂因式分解赞美诗编号——数学天才从摇篮开始
- 极其害羞、社交笨拙——住酒店会盖住所有镜子
- 板球狂热——用 Bradman 级别评价数学家
- 无神论者，20岁拒绝进任何学院礼拜堂
- 终生单身，晚年由妹妹 Gertrude 照顾
- 智力自评: Hardy=25, Littlewood=30, Hilbert=80, Ramanujan=100
- 对 Ramsey 和 Wittgenstein 等剑桥思想圈有深远影响
- 六条新年决心：黎曼假设、211 not out、证明上帝不存在、登顶珠峰、担任英德苏联总统、暗杀墨索里尼

---

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_hardy_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q184337` | ⚠️ 待核 |
| 2 | `people` | name_zh | `戈弗雷·哈罗德·哈代` | ⚠️ NULL |
| 3 | `people` | name_variants | `["纯数学的捍卫者","拉马努金的发现者","G.H. Hardy"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1877-02-07` / `1947-12-01` | ⚠️ **NULL 全缺** |
| 6 | `people` | description | `British mathematician (1877–1947)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`university teacher(1)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `number theory`、`mathematical analysis`、`pure mathematics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Smith's 1901`、`Royal Medal 1920`、`De Morgan 1929`、`Chauvenet 1932`、`Sylvester 1940`、`Copley 1947`、`FRS`、`Gibbs` | ⚠️ 空 |
| 10 | `person_institution` | 教育/任职 | `education: Trinity、Cambridge`；`employment: Cambridge、Oxford` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `United Kingdom` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见第 4.5 步（7 条） | ⚠️ 仅 2 条 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。新建 `MySQL/seed_hardy_relations.py` 补足。

**入库范围（7 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | A. E. H. Love → Hardy | 有向 | ⚠️ 占位 |
| 导师 | E. T. Whittaker → Hardy | 有向 | ⚠️ 占位 |
| 学生 | Hardy → Srinivasa Ramanujan | 有向 | ✅ 在库（id=57） |
| 学生 | Hardy → Mary Cartwright | 有向 | ⚠️ 占位 |
| 学生 | Hardy → E. C. Titchmarsh | 有向 | ⚠️ 占位 |
| 合作者 | J. E. Littlewood | 无向 | ✅ 在库（id=22） |
| 同事 | Bertrand Russell | 无向 | ✅ 在库（id=74） |

- 缺失人物（4 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`

---

## 核心数学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 解析数论 | Hardy–Littlewood 圆法——解析数论核心方法 | 1920 |
| 解析数论 | Waring 问题定量进展 | 1920s |
| 素数理论 | 第一/第二 Hardy–Littlewood 猜想 | 1923 |
| 分析 | Hardy 空间——复分析与调和分析的基石 | 1915 |
| 分析 | Hardy 不等式、Hardy–Littlewood 极大函数 | 1920s |
| 分析 | Tauberian 定理——级数求和理论 | 1914 |
| 组合 | 与 Ramanujan 的分拆渐近公式 | 1917 |
| 遗传学 | Hardy–Weinberg 原理 | 1908 |
| 数论 | Hardy–Ramanujan 数 1729 的轶事 | — |
| 教育 | 《纯数学教程》《数论导引》——改变英国数学 | 1908/1938 |

### ★ 哈代独有的叙事线索

1. **发现 Ramanujan** — 1913年1月16日收到印度小职员来信。晨读以为是疯子，晚上意识到可能是天才——"伟大的数学家比如此高超的骗子更常见"。这是哈代认为自己一生最大的贡献。"在数学能力的天平上，我25，Littlewood 30，Hilbert 80，Ramanujan 100。"

2. **"Hardy–Littlewood"——第三个数学家** — Bohr 说："现在只有三个真正伟大的英国数学家：Hardy、Littlewood 和 Hardy–Littlewood。" 两人合作35年，通过信件交换思想——从圆法到 Tauberian 定理到素数分布。合作规则：互不干扰对方的写作风格。

3. **《一个数学家的辩白》(1940)** — 失去创造力后写下的"数学讣告"。Graham Greene 将其与 Henry James 笔记并列，称为"关于创造性艺术家心灵最好的描述"。核心论点："我从未做过任何'有用'的事。"但 Hardy–Weinberg 原理成为群体遗传学基石——讽刺的是，他无意中做了最有用的数学。

4. **改革英国数学** — 20世纪初，英国数学仍沉浸在牛顿的阴影中——重应用、轻严格。Hardy 以 Jordan 的《分析教程》为武器，将欧洲大陆的严格性带入剑桥。他的《纯数学教程》(1908)是英国第一本现代分析教材，改变了一代人的数学思维。

5. **板球场上的数学家** — 数学研究的最顶级水平是"Hobbs 级"，后来升级为"Bradman 级"。Keynes 感叹：如果 Hardy 用读板球比分的热情每天读半小时股市行情，他早就是富翁了。

6. **恐惧镜子** — 极端害羞，住酒店时用毛巾盖住所有镜子。厌恶被介绍给陌生人。领奖时无法面对全校师生。这种人格在 Bloomsbury 团体和剑桥使徒的精英圈中找到了归属。

7. **与 Russell 的友谊和决裂** — 一战期间 Russell 因反战被剥夺 Trinity 教职，Hardy 愤而离开剑桥前往牛津。这段"政治流放"持续了12年。直到1931年才回到剑桥（部分原因是牛津65岁强制退休）。

---

## 第 5 步：设计配色

- **剑桥蓝 + 板球绿 + 牛津金 + 数学白** — 英格兰的学术景观
- 四个分类色:
  - **badgeRamanujan** (拉马努金 / 伙伴) — 印度藏红花橙 `#D4782F`
  - **badgeAnalysis** (分析 / 数论) — 剑桥蓝 `#1B3A5C`
  - **badgeApology** (辩白 / 纯数学哲学) — 学术象牙白 `#E8DCC8`
  - **badgeLegacy** (遗产 / 教育) — 板球绿 `#2E5F3E`

---

## 第 6 步：幻灯片序列（16 页）

```
00  OpenMath 项目首页
=== 封面 ===
01  封面 — 《哈代：纯数学的守护者》/ G.H. Hardy 1877–1947
02  为什么哈代定义了英国数学的灵魂 — 拉马努金·圆法·辩白·板球

=== 早年 ===
03  神童的童年 (1877–1900) — 两岁分解赞美诗·Winchester·Trinity
04  改革英国数学 (1906–1908) — 《纯数学教程》·Hardy–Weinberg 原理

=== 拉马努金 ===
05  "一生中唯一的浪漫事件" (1913) — 收到 Ramanujan 来信
06  Hardy–Ramanujan 合作 — 分拆·1729·天才的燃烧

=== 数学 ===
07  "Hardy–Littlewood"：第三个数学家 (1911–1945) — 35年合作·圆法
08  圆法与素数 — Waring 问题·Hardy–Littlewood 猜想
09  Hardy 空间与分析 — 调和分析·Tauberian 定理·不等式

=== 哲学 ===
10  《一个数学家的辩白》(1940) — "我从未做过任何有用的事"

=== 人格 ===
11  板球·镜子·使徒 — 害羞怪人与他的精英圈子
12  Oxford–Cambridge 十二年 — Russell 事件·Princeton·回归

=== 荣誉 ===
13  Royal·De Morgan·Sylvester·Copley — 英国数学的最高荣誉链

=== 遗产 ===
14  哈代的遗产 — 教材·Hardy 空间·1729·圆法

=== 结尾 ===
15  ⚰️ 结束页 — "一位创造性的艺术家……渴望他最好的作品被后世纪念。"
```

---

## 第 9 步：史实审查（高危陷阱）

| 陷阱 | 要点 |
|------|------|
| **Ramanujan 评价** | Hardy=25, Littlewood=30, Hilbert=80, Ramanujan=100。精确数字，不写"约" |
| **Hardy–Weinberg** | 1908年独立发现，与德国 Wilhelm Weinberg 同时。不是抄袭 |
| **圆法** | Hardy–Littlewood circle method。不要写成 Ramanujan 的工作 |
| **A Mathematician's Apology** | 1940年出版，前言为 C.P. Snow 1967年版所写 |
| **牛津剑桥交换** | 1919 → 牛津，1931 → 回剑桥。原因是 Russell 事件 + 退休年龄 |
| **Copley Medal** | 1947年，逝世同年。不是逝世后追授 |
| **1729** | 出租车号码轶事。不要写成 Ramanujan 在医院"当场"给出答案（实际上Ramanujan说"不，这是一个非常有趣的数字……"） |
| **自杀** | 1947年早期，巴比妥过量。不要回避，但以尊重态度叙述 |
| **板球** | "Hobbs class"和"Bradman class"是他的原话。Hobbs和Bradman都是板球传奇 |

### 术语清单

| 英文 | 中文 |
|------|------|
| Hardy–Littlewood circle method | Hardy–Littlewood 圆法 |
| Hardy space | Hardy 空间 |
| Hardy's inequality | Hardy 不等式 |
| Tauberian theorem | Tauberian 定理 |
| partition function | 分拆函数 |
| Waring's problem | Waring 问题 |
| Savilian Professor of Geometry | Savilian 几何教授 |
| Sadleirian Professor | Sadleirian 教授 |
| A Mathematician's Apology | 《一个数学家的辩白》 |
| Cambridge Apostles | 剑桥使徒 |

---

## 第 14 步：音乐选择

哈代的气质：**英国学院传统的高贵、纯数学的宁静深远、板球场上的英式优雅、Ramanujan 带来的东方异彩**

| 优先级 | 曲目 | 来源 | 理由 |
|:--:|------|------|------|
| ★★★ | Timeless | alex-productions | 永恒——"纯数学是永恒的，不像应用数学会过时" |
| ★★ | Expedition | alex-productions | 远征——从剑桥到牛津再到印度天才的发现 |

---

## 第 18 步：Makefile

复制 Milnor/Makefile，修改 MAIN = G_H_Hardy_zh

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. **Hardy 最独特的标签是"发现 Ramanujan"** ——他自己认为这是他最大的贡献
> 2. **"Hardy–Littlewood"被戏称为第三个数学家**——Harald Bohr 的名言
> 3. **《辩白》是20世纪最重要的数学哲学文献之一** ——核心引语："我从未做过任何有用的事"
> 4. **2岁分解赞美诗编号** ——天才的起源故事
> 5. **1729 出租车轶事** ——必须出现，最著名的数学故事之一
> 6. **板球**贯穿始终——用板球比喻来评价数学是 Hardy 独有的风格
> 7. **智力自评 25-30-80-100** ——Hardy 特有的谦逊与慷慨
