# 利翁斯 (Jacques-Louis Lions) 立传提示词 — 优化版

> 严格遵循 [Mathematician_Biography_Guide.md](../Mathematician_Biography_Guide.md)。
> 模板版本: v2.0 (2026-08-07)，参考: Schwartz, Dautray, Brezis, Temam。

---

## 一、结构化元数据

| 字段 | 值 | 来源 |
|------|-----|------|
| 全名 | Jacques-Louis Lions | Wikidata Q982534 |
| 生卒 | 1928-05-02 ~ 2001-05-17 (73岁) | Wikidata |
| 国籍 | 法国 | Wikidata |
| 出生地 | Grasse, Alpes-Maritimes, 法国 (香水之都) | Wikipedia |
| 博士导师 | Laurent Schwartz (1950年Fields奖得主) | Wikidata |
| 博士论文 | 1954 | Wikipedia |
| 教育 | ENS Paris (1947), University of Nancy | Wikipedia |
| 任职 | Nancy大学, Paris理学院, École Polytechnique, Collège de France (1973-1998), INRIA所长 (1979), CNES局长 (1984-1992) | Wikipedia |
| 荣誉 | Japan 奖 (1991), Harvey 奖 (1991), John von Neumann 奖 (1986), ForMemRS (1996), 法国科学院院长 (1996), IMU主席 (1991), 荣誉军团司令, 旭日章 | Wikidata |
| 知名学生 | Haïm Brezis, Roger Temam, Jean-Michel Bismut, Alain Bensoussan, Roland Glowinski 等 (共约50位) | Wikipedia |
| 儿子 | Pierre-Louis Lions — 1994年Fields奖 (父子均Fields级成就，数学史上罕见) | Wikipedia |
| 战时经历 | 1943-1944 加入法国抵抗运动 (Résistance), 对抗纳粹占领 (年仅15-16岁) | Wikipedia |
| 知名工作 | Lions–Lax–Milgram定理, Aubin–Lions引理, 均质化理论, 分布参数系统的最优控制, Dautray–Lions 4000页巨著 | Wikidata + Wikipedia |
| 历史地位 | 法国应用数学的总建筑师; 唯一同时领导CNES(法国NASA)和INRIA的数学家; 连接纯数学与国家工业的桥梁 | Wikipedia |

## 二、精确时间线

| 年份 | 事件 |
|------|------|
| 1928.05.02 | 生于法国 Grasse |
| 1943-1944 | 加入法国抵抗运动 (15-16岁) |
| 1947 | 进入 ENS Paris |
| 1954 | 博士 — 导师 Laurent Schwartz |
| 1954-1962 | Nancy大学教授 — 法国PDE学派据点 |
| 1958 | ICM 邀请报告 (30岁) |
| 1962 | Paris理学院教授 |
| 1966 | 通过戴高乐将军邀请苏联数学家Gury Marchuk访法 |
| 1973 | Collège de France 教授 |
| 1973 | 法国科学院院士 |
| 1979 | INRIA 所长 — 推广有限元数值模拟 |
| 1984-1992 | CNES 局长 — 领导法国太空计划 (Ariane火箭) |
| 1986 | John von Neumann 奖 |
| 1991 | Japan 奖 + Harvey 奖 + IMU 主席 |
| 1996 | 法国科学院院长 + ForMemRS |
| 2001.05.17 | 逝世于 Neuilly-sur-Seine, 享年73岁 |

## 二五、数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_lions_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q982534` | ⚠️ 待核 |
| 2 | `people` | name_zh | `雅克-路易·利翁` | ⚠️ NULL |
| 3 | `people` | name_variants | `["变分不等式的创立者","PDE 帝国的建筑师","最优控制之父"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1928-05-02` / `2001-05-17` | ⚠️ **NULL 全缺** |
| 6 | `people` | description | `French mathematician (1928–2001)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`university teacher(1)`、`professor(2)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `partial differential equation`、`mathematical analysis`、`numerical analysis`、`stochastic process`、`mathematics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Peccot 1958`、`von Neumann 1986`、`Harvey 1991`、`Japan 1991`、`ForMemRS 1996`、`Reid 1998`、`Legion of Honour`、`National Order of Merit`、`Rising Sun` | ⚠️ 空 |
| 10 | `person_institution` | 教育/任职 | `education: ENS、Nancy、Paris`；`employment: Nancy、Paris、École polytechnique、Collège de France` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `France` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见二六（7 条） | ⚠️ 仅 1 条 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 二六、社会关系入库 ★（§二十）

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | Laurent Schwartz → Lions | 有向 | ✅ 在库（id=17） |
| 学生 | Lions → Haim Brezis | 有向 | ⚠️ 占位 |
| 学生 | Lions → Roger Temam | 有向 | ⚠️ 占位 |
| 学生 | Lions → Alain Bensoussan | 有向 | ⚠️ 占位 |
| 学生 | Lions → Philippe Ciarlet | 有向 | ⚠️ 占位 |
| 同事 | Jean Leray | 无向 | ✅ 在库（id=37，法国 PDE 传统） |
| 合作者 | Enrico Magenes | 无向 | ⚠️ 占位（Lions–Magenes 引理） |

- 缺失人物（5 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`。脚本：`MySQL/seed_lions_relations.py`

## 三、核心贡献表

| 领域 | 贡献 | 关键年份 |
|------|------|:--:|
| PDE理论 | Lions–Lax–Milgram定理 (非对称双线性形式) | 1950s-1960s |
| PDE理论 | Aubin–Lions引理 (Banach空间紧嵌入) | 1960s |
| PDE理论 | Lions–Magenes引理 (发展方程正则性) | 1960s |
| 均质化 | 渐近均质化理论 — 复合材料与多孔介质 | 1970s-1980s |
| 控制论 | 分布参数系统的最优控制理论 | 1960s-1970s |
| 数值分析 | 变分不等式的数值解法 + 有限元理论 | 1970s-1980s |
| 工业数学 | Dautray–Lions 4000页巨著 (科学与技术的数学分析和数值方法) | 1984-1985 |
| 航天 | CNES领导 — Ariane火箭/卫星数学建模 | 1984-1992 |

## 四、三幕叙事结构

### 第一幕: 抵抗战士→ENS→Schwartz (1928-1962)
- 1928年生于Grasse
- 15-16岁加入法国抵抗运动 — 塑造一生的坚韧
- 1947年ENS — Schwartz的学生
- 1954年博士 → Nancy大学
- 1958年ICM报告 (30岁)

### 第二幕: 数学工业化的总设计师 (1962-1992)
- Collège de France + 法国科学院 (1973)
- INRIA所长 (1979) — 推广有限元
- CNES局长 (1984-1992) — 领导法国NASA
- Japan奖 + Harvey奖 + IMU主席 (1991)
- 4000页Dautray–Lions巨著

### 第三幕: 传承与遗产 (1992-2001)
- 50位博士生: Brezis, Temam, Bismut...
- 儿子Pierre-Louis Lions获Fields奖 (1994) — 数学史上罕见的父子成就
- 法国科学院院长 (1996)
- 2001年逝世 — 法国应用数学的精神丰碑

## 五、史实陷阱清单

| 陷阱 | 真相 |
|------|------|
| 博士导师 | ✅ Laurent Schwartz, 不是其他人 |
| 儿子 Fields | ✅ Pierre-Louis Lions 获1994年Fields奖 — 独立成就, 非"继承" |
| CNES年份 | ✅ 1984-1992 (8年) |
| INRIA年份 | ✅ 1979年起任所长 |
| Japan奖 | ✅ 1991 (与Harvey奖同年) |
| IMU主席 | ✅ 1991 |
| 抵抗运动 | ✅ 1943-1944, 年仅15-16岁 |
| Collège de France | ✅ 1973-1998 |
| ForMemRS | ✅ 1996 |
| 逝世 | ✅ 2001-05-17, Neuilly-sur-Seine |

## 六、配色方案

**气质**: 法国蓝 + 航天红 + 工业绿

| 变量 | 色值 | 用途 |
|------|------|------|
| `coverprimary` | `#002395` | 法国蓝 — 封面主色 |
| `coveraccent` | `#ED2939` | 法国红 — 强调/分隔线 |
| `coverdark` | `#1F2937` | 深灰 — 正文文本 |
| `bgmain` | `#F8F6F3` | 象牙白 — 背景 |
| `badgePDE` | `#002395` | PDE 蓝 |
| `badgeControl` | `#ED2939` | 控制论 红 |
| `badgeSpace` | `#1B5E20` | 航天 绿 |
| `badgeLegacy` | `#8A8A8A` | 遗产 灰 |

## 七、幻灯片设计 (8 页)

| 页 | 标题 | 核心内容 |
|:--:|------|------|
| 00 | OpenMath 首页 | 统一品牌 |
| 01 | 封面 | 姓名、肖像、🇫🇷、Schwartz学生、CNES、IMU |
| 02 | 总览 | PDE理论 + 控制论 + 航天工业 + 传承 |
| 03 | 早年 | 抵抗运动→ENS→Schwartz→Nancy |
| 04 | PDE理论 | Lions–Lax–Milgram, Aubin–Lions, 均质化 |
| 05 | 数学与工业 | INRIA→CNES→Ariane火箭 |
| 06 | 传承 | 50位博士生 + Pierre-Louis Fields 1994 |
| 07 | 结束页 | "数学的真正力量在于它能够改变世界" |

## 八、国籍标识

封面: `\faIcon{globe}\enspace 法国`

## 九、音乐建议

- 主轨道: 法国印象派 + 航天交响
- 情绪弧: 抵抗→学术→工业→不朽

## 十、编译验证清单

- [ ] 生: 1928-05-02 ✅
- [ ] 卒: 2001-05-17 (73岁) ✅
- [ ] 博士: Schwartz 1954 ✅
- [ ] CNES 1984-1992 ✅
- [ ] Japan奖+Harvey奖 1991 ✅
- [ ] 儿子Pierre-Louis Fields 1994 ✅
- [ ] 抵抗运动 1943-1944 ✅

> **开始执行。**