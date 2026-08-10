# 哈里什-钱德拉 (Harish-Chandra) 立传提示词 — 优化版

> 严格遵循 [Mathematician_Biography_Guide.md](../Mathematician_Biography_Guide.md)。
> 模板版本: v2.0 (2026-08-07)，参考: Cartan, Weyl, Schwartz, Gelfand。

---

## 一、结构化元数据

| 字段 | 值 | 来源 |
|------|-----|------|
| 全名 | Harish-Chandra (单名, 印度教名字+父名) | Wikidata Q1585395 |
| 生卒 | 1923-10-11 ~ 1983-10-16 (60岁) | Wikidata |
| 国籍 | 英属印度 → 印度 → 美国 | Wikidata |
| 出生地 | Kanpur, 印度 (英属印度时期) | Wikipedia |
| 逝世地 | Princeton, New Jersey, 美国 | Wikipedia |
| 博士导师 | Paul Dirac (理论物理学家, Cambridge) | Wikidata |
| 博士论文 | "Infinite Irreducible Representations of the Lorentz Group", 1947 | Wikipedia |
| 硕士 | 物理学硕士 (1940, 年仅17岁), University of Allahabad | Wikipedia |
| 任职 | Indian Institute of Science (Bangalore), Columbia University, Harvard University, Tata Institute, IAS Princeton (1963–1983) | Wikipedia |
| 荣誉 | Cole 奖 (代数) 1954, FRS 1973, Ramanujan 奖章 1974, Padma Bhushan 1977, 耶鲁荣誉博士 1981, 美国国家科学院院士 | Wikidata |
| 知名概念 | Harish-Chandra 同态/同构, Harish-Chandra 模, Harish-Chandra 特征标公式, Harish-Chandra c-函数, Harish-Chandra Schwartz 空间, Harish-Chandra $\Xi$ 函数, 尖点形式哲学 | Wikipedia |
| 继承者 | Robert Langlands 明确指出 HC 的工作是 Langlands 纲领的直接先驱 | Wikipedia |
| 历史地位 | 半单李群表示论之父; 几乎获1958年Fields奖; 印度数学的骄傲; Harish-Chandra 研究所 (HRI) 以他命名 | Wikipedia |

## 二、精确时间线

| 年份 | 事件 |
|------|------|
| 1923.10.11 | 生于英属印度 Kanpur |
| 1940 | Allahabad 大学物理学硕士 (17岁) |
| 1940–1945 | 印度科学研究所 (Bangalore), 在 Homi Bhabha 指导下研究宇宙射线 |
| 1945 | 赴剑桥大学, 成为 Paul Dirac 的学生 |
| 1945–1947 | 剑桥期间参加 Wolfgang Pauli 讲座, 当场指出 Pauli 错误 — 两人成为终身朋友 |
| 1947 | 剑桥博士 — 论文研究 Lorentz 群的无限不可约表示 |
| 1947–1963 | 辗转任职: Columbia, Harvard, Tata 研究所 |
| 1952 | 与 Lalitha "Lily" Kale 结婚 |
| 1954 | Cole 奖 (代数) — AMS |
| 1958 | 被考虑授予 Fields 奖, 因 Bourbaki 派系之争被搁置 (Langlands 证实) |
| 1963 | 加入 IAS Princeton — 在此度过余生 |
| 1968 | 《Automorphic Forms on Semisimple Lie Groups》出版 |
| 1973 | 当选英国皇家学会院士 (FRS) |
| 1974 | 印度国家科学院 Ramanujan 奖章 |
| 1977 | Padma Bhushan (印度第三高平民荣誉) |
| 1981 | 耶鲁大学荣誉博士 |
| 1983.10.16 | 在 Princeton 因心脏病逝世 (第5次发作), 享年60岁 |

## 二五、数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_harishchandra_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q1585395` | ⚠️ 待核 |
| 2 | `people` | name_zh | `哈里什-钱德拉` | ⚠️ NULL |
| 3 | `people` | name_variants | `["半单李群表示论之王","Harish-Chandra 互反律","分析学的隐者"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1923-10-11` / `1983-10-16` | ⚠️ **NULL 全缺** |
| 6 | `people` | description | `Indian-American mathematician (1923–1983)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`physicist(1)`、`university teacher(2)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `representation theory`、`harmonic analysis`、`Lie group`、`mathematics`、`physics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Cole 1954`、`FRS`、`Ramanujan Medal`、`Padma Bhushan`、`Guggenheim` | ⚠️ 空 |
| 10 | `person_institution` | 教育/任职 | `education: Allahabad、Cambridge、TIFR`；`employment: IAS、Harvard、Columbia、TIFR` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `British Raj`、`India`、`United States`、`Dominion of India` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见二六（6 条） | ⚠️ 仅 1 条 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 二六、社会关系入库 ★（§二十）

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | Paul Dirac → Harish-Chandra | 有向 | ⚠️ 占位（剑桥博士导师） |
| 合作者 | Armand Borel | 无向 | ✅ 在库（id=402，Borel–Harish-Chandra 定理） |
| 同事 | Robert Langlands | 无向 | ✅ 在库（id=176） |
| 同事 | Atle Selberg | 无向 | ✅ 在库（id=40，迹公式与表示论） |
| 同事 | Israel Gelfand | 无向 | ✅ 在库（id=436） |
| 同事 | Michael Atiyah | 无向 | ✅ 在库（id=19） |

- 缺失人物（1 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`。脚本：`MySQL/seed_harishchandra_relations.py`

## 三、核心贡献表

| 领域 | 贡献 | 关键年份 |
|------|------|:--:|
| 李群表示论 | Harish-Chandra 同态/同构 — 包络代数中心与 Weyl 群不变多项式的同构 | 1950s |
| 李群表示论 | Harish-Chandra 特征标公式 — Weyl 特征标公式的无限维推广 | 1950s–1960s |
| 调和分析 | 半单李群 Plancherel 公式 — 用 c-函数显式表达 Plancherel 测度 | 1950s–1970s |
| 调和分析 | 离散系列表示的构造与分类 | 1960s |
| 调和分析 | Harish-Chandra c-函数, Schwartz 空间, $\Xi$ 函数 | 1960s–1970s |
| 自守形式 | 半单李群的尖点形式理论 — Langlands 纲领的先驱 | 1960s |
| p-进群 | p-进约化群上的调和分析 — 局部特征标与 Plancherel 公式 | 1970s |

## 四、三幕叙事结构

### 第一幕: 物理天才的数学转向 (1923–1947)
- 英属印度 Kanpur — 17 岁物理学硕士
- Bhabha 指导下的宇宙射线研究
- 剑桥 — Paul Dirac 的学生
- 指出 Pauli 错误 — 震撼欧洲物理学界
- 1947 年博士 — Lorentz 群表示 — 从物理转向最纯的数学

### 第二幕: 半单李群王朝的建立 (1947–1963)
- 哥伦比亚、哈佛、Tata — 辗转的三地
- 1954 年 Cole 奖 — 代数领域最高荣誉
- Harish-Chandra 同构/特征标公式 — 表示论丰碑
- 离散系列表示 — 无限维推广 Weyl
- 1958 年 Fields 奖 — 被 Bourbaki 派系之争搁置

### 第三幕: IAS 的孤独巨匠 (1963–1983)
- IAS Princeton — 二十年的孤独工作
- Plancherel 公式 — 30 年完成半单李群调和分析完整体系
- 尖点形式哲学 — Langlands 纲领的地图
- p-进群的调和分析 — 统一的证明
- 1983年心脏病逝世 — 四卷 Collected Papers 成为不朽遗产
- HRI 研究所 — 印度数学的最高殿堂之一

## 五、史实陷阱清单

| 陷阱 | 真相 |
|------|------|
| 名字格式 | ✅ 单名 "Harish-Chandra" (不是姓 Chandra, 不是 Harish Chandra) |
| 博士导师 | ✅ Paul Dirac — 物理学家, 不是数学家 |
| 国籍变迁 | ✅ 英属印度 (1923–1947) → 印度 (1947–1960s) → 美国 (入籍) |
| Fields 奖 1958 | ✅ 被考虑但被 Bourbaki 派系之争搁置 — Langlands 亲笔证实 |
| Cole 奖 | ✅ 1954 年, 代数奖 (不是数论奖) |
| Ramanujan 奖章 | ✅ 1974 年 (印度国家科学院) |
| 逝世 | ✅ 1983-10-16, 第5次心脏病发作, Princeton, 60岁 |
| HRI | ✅ Harish-Chandra Research Institute, 印度政府命名, 位于 Allahabad |
| 1963 移居美国 | ✅ 1963 年加入 IAS, 不是更早 |
| Pauli 故事 | ✅ 确实发生 — Cambridge 讲座期间 |

## 六、配色方案

**气质**: 印度藏红 + 调和分析绿 + IAS 蓝

| 变量 | 色值 | 用途 |
|------|------|------|
| `coverprimary` | `#FF9933` | 印度藏红 — 封面主色 |
| `coveraccent` | `#138808` | 印度绿 — 强调/分隔线 |
| `coverdark` | `#1F2937` | 深灰 — 正文文本 |
| `bgmain` | `#F8F6F3` | 象牙白 — 背景 |
| `badgeRT` | `#FF9933` | 表示论 橙 |
| `badgeHA` | `#138808` | 调和分析 绿 |
| `badgeCF` | `#000080` | 尖点形式 海军蓝 |
| `badgeLegacy` | `#8A8A8A` | 遗产 灰 |

## 七、幻灯片设计 (9 页)

| 页 | 标题 | 核心内容 |
|:--:|------|------|
| 00 | OpenMath 首页 | 统一品牌 |
| 01 | 封面 | 姓名、肖像、🇮🇳→🇺🇸、Dirac学生、Cole奖、Fields逸事 |
| 02 | 总览 | 表示论 + 调和分析 + 尖点形式 + 荣誉 |
| 03 | 早年 | Kanpur→Allahabad→Bhabha→Cambridge→Dirac→Pauli故事 |
| 04 | 表示论 | HC同态、特征标公式、离散系列 |
| 05 | 尖点形式 | 尖点形式哲学、Schwartz空间、Langlands先驱 |
| 06 | Fields 奖逸事 | Langlands证词、1958、Bourbaki派系 |
| 07 | 遗产 | HC同态→特征标→Plancherel→尖点形式→Langlands纲领 |
| 08 | 结束页 | "真正的数学家独自建造一座数学大厦" |

## 八、国籍标识

封面: `\faIcon{globe}\enspace 英属印度 $\rightarrow$ 印度 $\rightarrow$ 美国`

## 九、音乐建议

- 主轨道: 印度古典 raga + 剑桥沉思
- 情绪弧: 殖民地少年 → 欧洲震撼 → 孤独巨匠

## 十、编译验证清单

- [ ] 生: 1923-10-11 ✅
- [ ] 卒: 1983-10-16 (60岁) ✅
- [ ] 博士: Dirac 1947 ✅
- [ ] Cole 奖 1954 ✅
- [ ] Fields 1958 逸事 ✅
- [ ] Padma Bhushan 1977 ✅
- [ ] HRI 研究所 ✅

> **开始执行。**