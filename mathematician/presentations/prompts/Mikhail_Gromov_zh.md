# 格罗莫夫 (Mikhail Gromov) 立传提示词 — 优化版

> 严格遵循 [Mathematician_Biography_Guide.md](../Mathematician_Biography_Guide.md)。
> 模板版本: v2.0 (2026-08-07)，参考: Milnor, Thom, Smale, Arnold。

---

## 一、结构化元数据

| 字段 | 值 | 来源 |
|------|-----|------|
| 全名 | Mikhail Leonidovich Gromov (Михаил Леонидович Громов) | Wikidata Q1176865 |
| 生 | 1943-12-23, Boksitogorsk, USSR (在二战期间出生, 82岁, 在世) | Wikidata |
| 国籍 | 苏联 → 法国 (1992年入籍) | Wikidata |
| 出生地 | Boksitogorsk, Leningrad Oblast, USSR | Wikipedia |
| 博士导师 | Vladimir Rokhlin (苏联拓扑学派) | Wikidata |
| 博士论文 | 1969, Leningrad University | Wikipedia |
| 任职 | IHÉS (1981–至今, 终身教授), NYU Courant Institute | Wikipedia |
| 荣誉 | Wolf 奖 (1993), Abel 奖 (2009), Bolyai 奖 (2005), Kyoto 奖 (2002), Balzan 奖 (1999), Steele 奖 (1997) | Wikidata |
| 知名合作者 | Jeff Cheeger (Gromov–Cheeger), Edward Witten (Gromov–Witten), Eliashberg, Lawson | Wikipedia |
| 知名工作 | 双曲群, h-原理 (凸积分), Gromov–Witten 不变量, J-全纯曲线, Gromov 非挤压定理, systolic 不等式, Gromov–Hausdorff 收敛 | Wikidata |
| 影响领域 | 几何群论, 辛几何, 度量几何, 微分拓扑, Riemann 几何, 数学物理 (弦论) | Wikipedia |
| 历史地位 | 在每一个涉足的领域都留下了以自己名字命名的概念; 开创了至少四个数学子领域; "Gromov 的每一个想法都足以开创一个全新的数学领域" | Wikipedia |

## 二、精确时间线

| 年份 | 事件 |
|------|------|
| 1943.12.23 | 生于苏联 Boksitogorsk (二战期间) |
| 1960s | 列宁格勒大学 (圣彼得堡大学) — 师从 Vladimir Rokhlin |
| 1969 | 博士 — Leningrad University |
| 1969–1981 | 在苏联发表 h-原理、凸积分等奠基性工作 |
| 1973 | 凸积分 (Convex Integration) — h-原理最核心工具 |
| 1981 | 移民法国 — 加入 IHÉS (Bures-sur-Yvette) |
| 1981–至今 | IHÉS 终身教授 |
| 1985 | J-全纯曲线 — 辛几何革命 |
| 1986 | 《Partial Differential Relations》— h-原理圣经 |
| 1987 | 《Hyperbolic Groups》— 几何群论诞生 |
| 1993 | Wolf 数学奖 |
| 1995 | Gromov–Witten 不变量 (与 Edward Witten 合作) |
| 1997 | Steele 奖 |
| 1999 | 《Metric Structures for Riemannian and Non-Riemannian Spaces》|
| 2002 | Kyoto 奖 (基础科学) |
| 2005 | Bolyai 奖 |
| 2009 | Abel 奖 — "为几何的革命性贡献" |

## 二五、数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> ⚠️ metadata.json 是消歧义页，字段取自已知资料。缺失项按 §21.5 写 `MySQL/seed_gromov_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q128398` | ⚠️ 待核 |
| 2 | `people` | name_zh | `米哈伊尔·格罗莫夫` | ⚠️ NULL |
| 3 | `people` | name_variants | `["几何学的分形天才","Gromov 双曲空间","伪全纯曲线"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1943-12-23` / `NULL`（在世） | ⚠️ 仅年份 |
| 6 | `people` | description | `Russian-French mathematician (1943–)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`university teacher(1)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `geometry`、`topology`、`partial differential equation`、`mathematics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Veblen 1981`、`Wolf 1993`（已有）、`Steele 1997`、`Kyoto 2002`、`Nemmers 2004`、`Abel 2009`（已有） | ⚠️ 部分 |
| 10 | `person_institution` | 教育/任职 | `education: Leningrad (Rokhlin)`；`employment: NYU、IHÉS、Stony Brook` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `Soviet Union`、`Russia`、`France` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见二六（7 条） | ⚠️ 全空 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 二六、社会关系入库 ★（§二十）

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | Vladimir Rokhlin → Gromov | 有向 | ✅ 在库（id=102） |
| 学生 | Gromov → Marc Burger | 有向 | ⚠️ 占位 |
| 学生 | Gromov → Pierre Pansu | 有向 | ⚠️ 占位 |
| 同事 | William Thurston | 无向 | ✅ 在库（id=20，双曲几何） |
| 同事 | Dennis Sullivan | 无向 | ✅ 在库（id=186） |
| 同事 | Alain Connes | 无向 | ✅ 在库（id=122） |
| 合作者 | Yasha Eliashberg | 无向 | ⚠️ 占位（辛几何，Gromov–Eliashberg） |

- 缺失人物（3 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`。脚本：`MySQL/seed_gromov_relations.py`

## 三、核心贡献表

| 领域 | 贡献 | 关键年份 |
|------|------|:--:|
| 微分拓扑 | h-原理 (同伦原理) + 凸积分 | 1973 |
| 辛几何 | J-全纯曲线, Gromov 非挤压定理, Gromov–Witten | 1985, 1995 |
| 几何群论 | δ-双曲空间, **双曲群** | 1987 |
| 度量几何 | Gromov–Hausdorff 收敛 | 1981 |
| Riemann 几何 | Gromov 体积, systolic 不等式 | 1983 |
| PDE | 偏微分关系理论 (h-原理) | 1986 |
| 数学物理 | Gromov–Witten 不变量 → 弦论, 镜像对称 | 1995 |

## 四、三幕叙事结构

### 第一幕: 列宁格勒的拓扑少年 (1943–1981)
- 二战期间出生 — Rokhlin 的学生
- 1969 年博士 — 列宁格勒拓扑学派
- 在苏联发表 h-原理和凸积分
- 国际化道路受阻 — 1981 年移民法国

### 第二幕: 四大领域的建筑师 (1981–2009)
- 1981 年加入 IHÉS — 思想获得自由
- 1985 年 J-全纯曲线 — 辛几何的革命
- 1987 年双曲群 — 几何群论诞生
- 1995 年 Gromov–Witten 不变量 — 连通弦论
- Wolf 1993 → Abel 2009 — 16 年的终极认可

### 第三幕: 活着的传奇 (2009–至今)
- 82 岁仍活跃在 IHÉS 和 NYU
- 关于生物学和数学的哲学思考
- "Gromov 的头脑是一个数学宇宙"

## 五、史实陷阱清单

| 陷阱 | 真相 |
|------|------|
| 名字拼写 | ✅ Mikhael Gromov 或 Mikhail Gromov (均正确 — Михаи́л 的音译变体) |
| 仍在世 | ✅ 生于 1943-12-23 (82岁) — 不用过去时 |
| 博士导师 | ✅ Vladimir Rokhlin (不是 Rokhlin!) |
| 移民法国年份 | ✅ 1981 (不是 1982) |
| 双曲群论文 | ✅ 1987 (发表在 "Essays in Group Theory") |
| J-全纯曲线 | ✅ 1985 年论文 (Inventiones Math) |
| Gromov–Witten 不变量 | ✅ 1995 年 (与 Witten 合作) |
| Abel 奖年份 | ✅ 2009 |
| Wolf 奖年份 | ✅ 1993 |
| 国籍 | ✅ 苏联→法国 (1981年移居, 1992年入法籍) |

## 六、配色方案

**气质**: 苏联红 + 几何金 + 双曲青

| 变量 | 色值 | 用途 |
|------|------|------|
| `coverprimary` | `#8B0000` | 苏联深红 — 封面主色 |
| `coveraccent` | `#D4AF37` | 几何金 — 强调/分隔线 |
| `coverdark` | `#1F2937` | 深灰 — 正文文本 |
| `bgmain` | `#F8F6F3` | 象牙白 — 背景 |
| `badgeHG` | `#8B0000` | 双曲群 红 |
| `badgeHP` | `#D4AF37` | h-原理 金 |
| `badgeSY` | `#1B3A5C` | 辛几何 青 |
| `badgeLegacy` | `#8A8A8A` | 遗产 灰 |

## 七、幻灯片设计 (9 页)

| 页 | 标题 | 核心内容 |
|:--:|------|------|
| 00 | OpenMath 首页 | 统一品牌 |
| 01 | 封面 | 姓名、肖像、🇷🇺→🇫🇷、Wolf+Abel、h-原理+双曲群+辛几何 |
| 02 | 总览 | 几何群论 + h-原理 + 辛几何 + 荣誉 |
| 03 | 早年 | 列宁格勒→Rokhlin→博士→IHÉS |
| 04 | h-原理 | 凸积分 1973, 微分关系, Nash+Kuiper 统一 |
| 05 | 双曲群 1987 | δ-双曲空间, 几何群论诞生 |
| 06 | 辛几何 | J-全纯曲线, Gromov–Witten, 非挤压定理 |
| 07 | 遗产 | 凸积分→h-原理→双曲群→J-全纯曲线→GW |
| 08 | 结束页 | "数学中最深刻的思想往往来自不同领域的意外碰撞" |

## 八、国籍标识

封面: `\faIcon{globe}\enspace 苏联 $\rightarrow$ 法国/美国`

## 九、音乐建议

- 主轨道: 深沉交响乐 + 几何音乐 (Bach)
- 情绪弧: 苏联禁锢 → 法国自由 → 世界级大师

## 十、编译验证清单

- [ ] 生: 1943-12-23 (在世) ✅
- [ ] 博士: Rokhlin 1969 ✅
- [ ] 凸积分 1973 ✅
- [ ] 双曲群 1987 ✅
- [ ] J-全纯曲线 1985 ✅
- [ ] Gromov–Witten 1995 ✅
- [ ] Wolf 1993, Abel 2009 ✅
- [ ] 苏联→法国 (1992入籍) ✅

> **开始执行。**