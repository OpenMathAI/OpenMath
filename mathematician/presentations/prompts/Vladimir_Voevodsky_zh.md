# 沃埃沃茨基 (Vladimir Voevodsky) 立传提示词 — 优化版

> 严格遵循 [Mathematician_Biography_Guide.md](../Mathematician_Biography_Guide.md)。
> 模板版本: v2.0 (2026-08-07)，参考: Grothendieck, Milnor, Morel, Suslin, Friedlander。

---

## 一、结构化元数据

| 字段 | 值 | 来源 |
|------|-----|------|
| 全名 | Vladimir Alexandrovich Voevodsky (Владимир Александрович Воеводский) | Wikidata Q369662 |
| 生卒 | 1966-06-04 ~ 2017-09-30 (51岁，动脉瘤骤逝) | Wikidata |
| 国籍 | 苏联 → 美国 | Wikidata |
| 出生地 | Moscow, Soviet Union | Wikipedia |
| 逝世地 | Princeton, New Jersey, United States | Wikipedia |
| 父母 | 父: Aleksander Voevodsky (核物理学家, 高能轻子实验室主任), 母: Tatyana (化学家) | Wikipedia |
| 博士导师 | David Kazhdan (Harvard) | Wikidata |
| 博士论文 | 1992, Harvard — 未经正式申请, 无本科学位即获博士 | Wikipedia |
| 教育 | Moscow State University (被开除, 无学位), Harvard PhD 1992 | Wikipedia |
| 任职 | IAS Princeton (2002–2017, 终身教授) | Wikipedia |
| 荣誉 | Fields Medal (2002), 哥德堡大学荣誉博士 (2016) | Wikidata |
| 知名合作者 | Fabien Morel (A¹-同伦论), Andrei Suslin, Eric Friedlander (motivic 上同调) | Wikipedia |
| 知名工作 | A¹-同伦论 (Morel–Voevodsky), motivic 上同调, Milnor 猜想证明 (1996), Bloch–Kato 猜想证明 (2009), 单价基础 (HoTT), UniMath | Wikidata + Wikipedia |
| 影响领域 | 代数几何, 代数拓扑, 动机理论, 数论, 数学基础, 类型论, 计算机形式化 | Wikipedia |
| 历史地位 | 代数几何同伦论革命的领袖; Grothendieck 动机梦想的实现者; HoTT/单价基础的奠基人之一; 51岁骤逝留下未完成的数学基础革命 | Wikipedia |

## 二、精确时间线

| 年份 | 事件 |
|------|------|
| 1966.06.04 | 生于苏联 Moscow |
| 1980s前期 | 进入莫斯科国立大学 — 拒绝上课, 成绩不及格, 被开除 (无本科学位) |
| 1980s | 导师 George Shabat 给他 Grothendieck 的《Esquisse d'un Programme》— 为读懂它自学法语 |
| 1990 | 独立发表多篇论文后, David Kazhdan 推荐他直接攻读哈佛博士 |
| 1992 | Harvard 博士 — 未经正式申请, 无本科学位 |
| 1996 | A¹-同伦论 (与 Fabien Morel 合作) — 概形上的同伦理论 |
| 1996 | 证明 Milnor 猜想 — $K_n^M(F)/2 \cong H_{\text{ét}}^n(F, \mathbb{Z}/2)$ |
| 1998 | ICM 柏林大会报告 (A¹-Homotopy Theory) |
| 2000 | Cycles, Transfers and Motivic Homology Theories (与 Suslin, Friedlander 合著) |
| 2002 | Fields Medal — 北京 ICM (因 SARS 推迟至 2010 颁发) |
| 2002 | 加入 IAS Princeton 终身教授 |
| 2006 | 转向 Homotopy Type Theory (HoTT) — 发现类型论与同伦论的深刻联系 |
| 2009 | Grothendieck 纪念会议 — 宣布 Bloch–Kato 猜想完全证明 |
| 2009 | 在单纯集中构造了单价 (univalent) 模型 |
| 2010s | 启动 UniMath 项目 — 在 Coq 中用单价基础形式化数学 |
| 2016 | 哥德堡大学荣誉博士 |
| 2017.09.30 | 在 Princeton 家中因动脉瘤 (aneurysm) 骤逝, 享年 51 岁 |

## 二五、数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_voevodsky_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q369662` | ⚠️ 待核 |
| 2 | `people` | name_zh | `弗拉基米尔·沃耶沃茨基` | ⚠️ NULL |
| 3 | `people` | name_variants | `["动机同伦理论的创立者","A1 同伦论","单值化公理之父"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1966-06-04` / `2017-09-30` | ⚠️ 仅年份 |
| 6 | `people` | description | `Russian mathematician (1966–2017)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`topologist(1)`、`logician(2)`、`university teacher(3)` | ⚠️ 需补 |
| 8 | `person_field` | 领域 | `algebraic geometry`、`topology`、`Galois theory`、`foundations of mathematics`、`mathematics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Fields 2002`（已有） | ⚠️ 部分 |
| 10 | `person_institution` | 教育/任职 | `education: MSU、Harvard`；`employment: IAS` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `Soviet Union`、`United States` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见二六（6 条） | ⚠️ 全空 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 二六、社会关系入库 ★（§二十）

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | David Kazhdan → Voevodsky | 有向 | ✅ 在库（id=439） |
| 学生 | Voevodsky → Alexander Vishik | 有向 | ⚠️ 占位 |
| 学生 | Voevodsky → Simone Borghesi | 有向 | ⚠️ 占位 |
| 合作者 | Andrei Suslin | 无向 | ⚠️ 占位（母题上同调与代数 K-理论） |
| 同事 | Alexander Beilinson | 无向 | ✅ 在库（id=194，动机理论） |
| 同事 | John Tate | 无向 | ✅ 在库（id=183，代数 K-理论） |

- 缺失人物（3 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`。脚本：`MySQL/seed_voevodsky_relations.py`

## 三、核心贡献表

| 领域 | 贡献 | 关键年份 |
|------|------|:--:|
| 代数几何 | A¹-同伦论 (Morel–Voevodsky) — 概形范畴上的同伦论 | 1996 |
| 动机理论 | motivic 上同调 — Grothendieck 动机理论的"正确"上同调 | 1996–2000 |
| K-理论 | Milnor 猜想证明 — K-理论与 Galois 上同调的同构 | 1996 |
| 数论 | Bloch–Kato 猜想证明 — Milnor 猜想的全素数推广 | 2009 |
| 数学基础 | 单价基础 (Univalent Foundations) — 同伦类型论的数学基础 | 2006–2014 |
| 计算机 | UniMath — 基于 Coq 的形式化数学库 | 2010–2017 |

## 四、三幕叙事结构

### 第一幕: 被开除的天才 (1966–1992)
- 1966年生于莫斯科科学家庭
- 莫斯科大学 — 拒绝上课, 被开除
- 为读懂 Grothendieck 的《Esquisse》自学法语
- David Kazhdan 推荐 — 无本科学位获哈佛博士

### 第二幕: 代数几何的同伦论革命 (1992–2006)
- 1996: A¹-同伦论 + Milnor 猜想证明
- 1998: ICM 柏林大会报告
- 2000: motivic 上同调完整理论
- 2002: Fields Medal (北京)
- 2002: IAS Princeton 终身教授

### 第三幕: 数学的新地基 (2006–2017)
- 2006: 转向 HoTT — 从纯代数几何到计算机逻辑
- 2009: Bloch–Kato 完全证明 + 单价模型
- 2010s: UniMath 项目
- 2017: 51岁动脉瘤骤逝 — 数学基础革命未完成

## 五、史实陷阱清单

| 陷阱 | 真相 |
|------|------|
| 本科 | ✅ 被莫斯科大学开除, 无本科学位 |
| 博士 | ✅ Harvard 1992, David Kazhdan (未正式申请) |
| Fields Medal 颁发 | ✅ 2002北京ICM, 因SARS推迟至2010年颁发 |
| Milnor 猜想 | ✅ 1996 证明, 不是 Bloch–Kato |
| Bloch–Kato | ✅ 2009 完全证明 (在 Grothendieck 纪念会议上宣布) |
| A¹-同伦论 | ✅ 与 Fabien Morel 合作 (Morel–Voevodsky) |
| 死因 | ✅ 动脉瘤 (aneurysm), 不是癌症, 不是心脏病 |
| Fields 奖 | ✅ 2002, 同时获奖者为 Laurent Lafforgue |
| HoTT | ✅ Voevodsky 是推动者 — Martin-Löf 类型论在先 |
| 死于 | ✅ 2017-09-30, Princeton 家中 |
| Grothendieck 影响 | ✅ 为读《Esquisse d'un Programme》自学法语 |

## 六、配色方案

**气质**: 同伦紫 + 动机金 + 单价森林绿

| 变量 | 色值 | 用途 |
|------|------|------|
| `coverprimary` | `#4B0082` | 同伦紫 (靛蓝) — 封面主色 |
| `coveraccent` | `#DAA520` | 动机金 — 强调/分隔线 |
| `coverdark` | `#1F2937` | 深灰 — 正文文本 |
| `bgmain` | `#F8F6F3` | 象牙白 — 背景 |
| `badgeAH` | `#4B0082` | A¹-同伦论 紫 |
| `badgeMC` | `#DAA520` | motivic 上同调 金 |
| `badgeUF` | `#2E5A40` | 单价基础 森林绿 |
| `badgeLegacy` | `#8A8A8A` | 遗产 灰 |

## 七、幻灯片设计 (9 页)

| 页 | 标题 | 核心内容 |
|:--:|------|------|
| 00 | OpenMath 首页 | 统一品牌 |
| 01 | 封面 | 姓名、肖像、🇷🇺→🇺🇸、Fields2002、A¹-同伦+motivic+HoTT |
| 02 | 总览 | A¹-同伦 + motivic + HoTT + 传奇 |
| 03 | 早年 | 莫斯科→被开除→Grothendieck→法语→Harvard博士 |
| 04 | A¹-同伦论 | Morel–Voevodsky, motivic 上同调 |
| 05 | Milnor/Bloch–Kato | 1996 Milnor + 2009 Bloch–Kato |
| 06 | 单价基础 | HoTT, UniMath, 数学的新地基 |
| 07 | 遗产 | A¹-同伦→motivic→Milnor→Bloch–Kato→HoTT→UniMath |
| 08 | 结束页 | "数学的终极目标是让证明不再出错" |

## 八、国籍标识

封面: `\faIcon{globe}\enspace 苏联 $\rightarrow$ 美国`

## 九、音乐建议

- 主轨道: 俄罗斯深沉交响 + 计算机脉冲电子
- 情绪弧: 莫斯科阴影 → algebraic revolution → 数学未来的曙光

## 十、编译验证清单

- [ ] 生: 1966-06-04 ✅
- [ ] 卒: 2017-09-30 (动脉瘤, 51岁) ✅
- [ ] 博士: Kazhdan 1992 (未申请, 无本科学位) ✅
- [ ] A¹-同伦论 1996 (Morel–Voevodsky) ✅
- [ ] Milnor 猜想 1996 ✅
- [ ] Bloch–Kato 2009 ✅
- [ ] Fields 2002 ✅
- [ ] HoTT/UniMath ✅

> **开始执行。**
