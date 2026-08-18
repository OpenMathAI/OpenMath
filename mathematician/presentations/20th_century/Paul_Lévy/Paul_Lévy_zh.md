# 列维 (Paul Lévy) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)。
> 数据库字段梳理见工作指南 §二十一；社会关系入库见 §二十。

---

## 背景信息

- **目标数学家**: Paul Pierre Lévy (1886–1971)
- **气质关键词**: **Lévy 过程、Lévy 稳定分布——随机分析的基础构件**
- **Wikipedia 页面**: ✅ 已下载
  - 路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Paul_Lévy/`
  - Wikipedia 英文条目: `Paul Lévy (mathematician)`
- **Beamer 文件**: `mathematician/presentations/Paul_Lévy/Paul_Lévy_zh.tex` (待创建)
- **参考模板**: `wiener/`, `ramanujan/`, `hecke/` 的完整源码
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/wiener/Norbert_Wiener_zh.tex`
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/hecke/Makefile`
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`

---

## 第 0 步：核对 Wikipedia 页面 ✅

已下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Paul_Lévy/`

- **全名**: Paul Pierre Lévy
- **生卒日期**: 1886-09-15 ~ 1971-12-15，享年 **85** 岁
- **国籍**: 🇫🇷 France（法国）
- **出生地**: Paris（巴黎，犹太家庭，家族已有多位数学家）
- **逝世地**: Paris（巴黎）
- **博士导师**: Jacques Hadamard、Vito Volterra（巴黎大学/综合理工）
- **教育经历**:
  - Lycée Saint-Louis（圣路易中学）
  - École Polytechnique（综合理工学院，1905 年 19 岁发表首篇论文，Lévy–Steinitz 定理）
  - Mines ParisTech（矿业学院，学习 3 年，1913 教授）
  - University of Paris
- **主要任职机构**:
  - École des Mines（矿业学院，1913 教授）
  - École Polytechnique（综合理工学院，1920 分析学教授，1959 退休）
- **关键荣誉**:
  - Cours Peccot（1920）
  - Poncelet Prize（1932）
  - Commander of the Legion of Honour（荣誉军团司令）
  - Émile Picard Medal（1953，法国科学院）
  - Concours général（中学竞赛奖）
- **博士学生**: Wolfgang Doeblin、Michel Loève、Benoît Mandelbrot、Georges Matheron、Pierre Rosenstiehl
- **研究领域**: probability theory（概率论）、stochastic process（随机过程）、functional analysis（泛函分析）
- **家族**: 妻 Suzanne Lévy（1913 结婚）；女 Marie-Hélène Schwartz（数学家）、Denise；子 Jean Claude；女婿 Laurent Schwartz（数学家）

### 关键时间线：

- 1886: 9月15日生于巴黎，犹太数学家家族（父 Lucien 是综合理工考官）
- 1905: 19 岁综合理工本科发表首篇论文，引入 **Lévy–Steinitz 定理**
- 1913: 与 Suzanne Lévy 结婚；矿业学院教授
- 一战: 为法国炮兵做数学分析工作
- 1920: 综合理工学院分析学教授（学生包括 Mandelbrot、Matheron）
- 1930s: 研究相依随机变量的大数定律，引入**鞅（martingale）**概念
- 1937: 出版《Théorie de l'addition des variables aléatoires》——用特征函数证明中心极限定理一般版本，独立于 Khinchin 引入无穷可分律与 **Lévy–Khintchine 表示**
- 1940: 德军占领后迁里昂任教
- 1940.12: 维希政府犹太教师解职令，12 月 19 日收到解职通知；综合理工院长 1941.3.14 恢复其职位
- 1942.11: 纳粹压迫加剧，流亡藏匿于女婿 Robert Piron 家（Montbonnot），一周后德军进占维希法国；藏匿至盟军解放，期间继续数学工作
- 1948: 出版《Processus stochastiques et mouvement brownien》——布朗运动的开创性专著（Lévy 面积、arcsine 律、local time）
- 1953: 获法国科学院 Émile Picard 奖章
- 1959: 退休
- 1971: 12月15日逝世于巴黎，享年 85 岁

### ★ 叙事亮点：

1. **Lévy 过程** — 独立增量过程的一般理论，布朗运动与泊松过程的统一框架。Lévy 飞行、Lévy 度量、Lévy 测度遍布现代概率论与 AI（随机游走、MCMC）。
2. **稳定分布** — 独立变量和的稳定分布，证明中心极限定理一般版本（1937）。
3. **鞅（1930s）** — 独立于 Doob 之前引入条件期望性质 E(S_{n+1}|S_1...S_n)=S_n，为 Doob 的鞅理论奠基。
4. **Lévy–Khintchine 表示** — 与 Khinchin 独立发现无穷可分律的刻画。
5. **布朗运动专著（1948）** — Lévy 面积、arcsine 律、local time——布朗运动的现代图景。
6. **纳粹统治下的数学家** — 1940 解职 → 1941 复职 → 1942 藏匿；犹太数学家的幸存叙事。
7. **Lévy C 曲线** — 分形曲线的优雅例子，数学之美的具象。

### ★ 史实注意：

- **页面是消歧页**：必须用 `Paul Lévy (mathematician)`（qid=Q441127），不能用 `Paul Lévy` 消歧页。
- **鞅的归属**：Lévy 1930s 独立引入（条件期望性质），Doob 后来发展成一般理论。不能写成"Doob 发明"。
- **Lévy–Khintchine**：Lévy 与 Khinchin **独立**发现。
- **纳粹叙事**：1940.12 解职、1941.3 复职、1942.11 藏匿——时间线精确。
- **Lévy 家族**：女 Marie-Hélène Schwartz 与女婿 Laurent Schwartz（分布论）都是数学家——数学世家。
- **military service**：毕业后服役一年，后入矿业学院三年。

---

## 数据库字段核对表（第 0 步之后必填）

| # | 表 | 字段 | 核对值 |
|:--:|---|------|--------------------------|
| 1 | `people` | qid | `Q441127` |
| 2 | `people` | name_en | `Paul Lévy` |
| 3 | `people` | name_zh | `保罗·列维` |
| 4 | `people` | name_variants | `["Paul Pierre Lévy","Lévy 过程的命名者","稳定分布的引入者","鞅理论的先驱"]` |
| 5 | `people` | gender | `male` |
| 6 | `people` | birth_date | `1886-09-15` |
| 7 | `people` | death_date | `1971-12-15` |
| 8 | `people` | description | `French mathematician (1886–1971)` |
| 9 | `people` | primary_occupation | `mathematician` |
| 10 | `person_occupation` | 职业（rank 排序） | `mathematician(0)`、`university teacher(1)`、`engineer(2)` |
| 11 | `person_field` | 领域（rank 排序） | `probability theory(0)`、`stochastic process(1)`、`functional analysis(2)` |
| 12 | `award_laureate` | 获奖记录 | `Cours Peccot、Poncelet Prize 1932、Commander of the Legion of Honour、Émile Picard Medal 1953、Concours général` |
| 13 | `person_institution` | 教育/任职 | `education: École Polytechnique、Mines ParisTech、University of Paris`；`employment: École des Mines(1913–1920)、École Polytechnique(1920–1959)` |
| 14 | `person_nationality` | 国籍 | `France` |
| 15 | `person_relation` | 社会关系 | 见 §二十（第 4.5 步） |
| 16 | `rankings` | 榜单 | `OpenMath_20th_Century_51_108`、`rank=66`、`status=🔲/🔲` |

> ★ 奖项列注意：**全部收录**（含追授/政治勋章/名誉类，见 21.2.4）。

---

## 第 4.5 步：社会关系入库（MySQL）

> 已按 §二十 梳理，参考实现 `MySQL/seed_levy_relations.py`。

**社会关系清单：**

| 关系类型 | 对象 | 方向 | note |
|---------|------|------|------|
| 老师 | Jacques Hadamard | 师→生 | 博士导师（已有 70） |
| 老师 | Vito Volterra | 师→生 | 博士导师（新建占位） |
| 学生 | Wolfgang Doeblin | 师→生 | 1940 阵亡的概率论天才（新建占位） |
| 学生 | Michel Loève | 师→生 | 概率论教科书作者（新建占位） |
| 学生 | Benoît Mandelbrot | 师→生 | 分形几何之父（新建占位） |
| 学生 | Georges Matheron | 师→生 | 地质统计学（新建占位） |
| 学生 | Pierre Rosenstiehl | 师→生 | 图论与组合（新建占位） |
| 家族 | Marie-Hélène Schwartz | 父→女 | 女儿，数学家（已有 424） |
| 家族 | Laurent Schwartz | 姻亲 | 女婿，分布论创始人（已有 17） |
| 同事 | Aleksandr Khinchin | 无向 | 独立发现 Lévy–Khintchine 表示（已有 367） |
| 同事 | Joseph L. Doob | 无向 | 鞅理论继承者（新建占位） |
| 同事 | Norbert Wiener | 无向 | 布朗运动（Wiener 过程）共同奠基（已有 56） |
| 同事 | Suzanne Lévy | 夫妻 | 妻（1913 结婚）（新建占位） |

**入库操作：**
1. `people` 表：Lévy 已存在（id=66），补齐 qid/Q441127、name_variants、description、birth/death；`has_social_data` 置 1
2. `person_field`：probability theory / stochastic process / functional analysis 关联
3. `award_laureate`：Cours Peccot、Poncelet Prize、Commander of the Legion of Honour、Émile Picard Medal、Concours général（全部已存在）
4. `person_institution`：École Polytechnique（6）、Mines ParisTech（7）、University of Paris（8）
5. `person_nationality`：France
6. `person_relation`：Hadamard、Volterra → Lévy；Lévy → 5 位学生 + Marie-Hélène；Schwartz 姻亲；Khinchin/Doob/Wiener/Suzanne ↔ Lévy
7. 缺失人物先建占位（`has_biography=0`），关系 note 加 `[材料待展开]` 前缀

**校验：**
```sql
SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
FROM person_relation pr
JOIN people a ON a.id=pr.from_id
JOIN people b ON b.id=pr.to_id
JOIN relation_types rt ON rt.relation_key=pr.relation_type
WHERE a.name_en='Paul Lévy' OR b.name_en='Paul Lévy';
```

---

## 第 5 步：设计配色方案

- **建议配色：巴黎靛蓝 + 稳定分布金 + 鞅红 + 手稿米** —— 随机过程的流动之美 + 巴黎的优雅
- 与已有配色完全不同！

- 主要色值：
  | 用途 | 色名 | 建议色值 | 说明 |
  |------|------|---------|------|
  | 背景 | `bgmain` | `#F8F5EE` | 手稿米 —— 概率手稿的气质 |
  | 主色 | `coverprimary` | `#1F3A5C` | 巴黎靛蓝 —— 巴黎学派 |
  | 强调色 | `coveraccent` | `#C9A227` | 稳定分布金 —— 稳定分布 |
  | 深色文本 | `coverdark` | `#1F2A28` | 深墨色 |
  | 浅色文本 | `covermuted` | `#6A7480` | 蓝灰 |

- 四个分类色：
  - **badgeLevyProcess** (Lévy 过程) — 过程青 `#1F7A8C`
  - **badgeStable** (稳定分布) — 稳定分布金 `#C9A227`
  - **badgeMartingale** (鞅) — 鞅红 `#B04A4A`
  - **badgeBrownian** (布朗运动) — 布朗紫 `#7A3A8A`

---

## 第 6 步：规划幻灯片序列（12 页）

```
00  OpenMath 项目首页

=== 封面与总览 ===
01  封面 — 《列维：随机世界的建筑师》 / Paul Lévy 1886–1971
02  Hook — 为什么列维独一无二：Lévy 过程·稳定分布·鞅·布朗运动专著

=== 生平与核心贡献 ===
03  早年的教育 (1886–1913) — 巴黎·综合理工·19 岁首篇论文·Hadamard/Volterra
04  Lévy 过程 (1930s) — 独立增量·Lévy–Khintchine 表示·无穷可分律
05  稳定分布与 CLT — 1937 专著·特征函数·中心极限定理一般版本

=== 概率论的黄金 ===
06  鞅的诞生 (1930s) — 条件期望性质·Doob 的理论继承
07  布朗运动专著 (1948) — Lévy 面积·arcsine 律·local time

=== 学派与传承 ===
08  学生与数学世家 — Doeblin·Loève·Mandelbrot·Matheron·Schwartz 家族
09  纳粹统治下的幸存 (1940–1944) — 解职·复职·藏匿·数学不息

=== 人格与历史 ===
10  Lévy 的世纪遗产 — 从 Lévy 过程到 AI 时代的随机工具
11  Lévy C 曲线 — 分形之美·数学的诗意

=== 结尾 ===
12  结束页 — "他把'随机'变成了'结构'；从 Lévy 过程到深度学习，整个随机的时代都在他的坐标里。"
```

---

## 第 9 步：史实审查

### Lévy 特有的史实陷阱

| 陷阱类型 | 高危点 |
|---------|--------|
| **消歧页** | 必须用 Paul Lévy (mathematician)，qid=Q441127 |
| **鞅的归属** | Lévy 1930s 独立引入（条件期望性质）；Doob 发展为一般理论 |
| **Lévy–Khintchine** | 与 Khinchin 独立发现 |
| **纳粹时间线** | 1940.12 解职 → 1941.3 复职 → 1942.11 藏匿 → 1944 解放 |
| **数学世家** | 女 Marie-Hélène + 女婿 Laurent Schwartz |
| **19 岁首篇** | 1905 综合理工本科，Lévy–Steinitz 定理 |

---

## 第 13 步：Wikipedia 本地文档终审（提交前必做）

### 终审清单
- [x] 生卒日期与正文一致（1886-09-15 ~ 1971-12-15）
- [x] 博士导师 Hadamard、Volterra 正确
- [x] 19 岁 Lévy–Steinitz 定理正确
- [x] 鞅 1930s 独立引入正确
- [x] 1948 布朗运动专著正确
- [x] 纳粹时间线精确（1940-1944）

---

### Review-1 记录 (2026-08-12)

> 结合本地 Wikipedia (`pages/Paul_Lévy/page.md`) 逐页比对。此前排行榜误标 ✅/✅✅（提示词无 Review 记录），本次实际完成。

- **头像** ✅：`Paul_Levy.jpg`（290×370，Wikipedia `Paul_Pierre_Levy_1886-1971.jpg` 下载，封面右上角 3.2cm）
- **国籍** ✅：封面 `\faIcon{globe}\enspace France\enspace·\enspace Picard Medal 1953\enspace·\enspace 鞅的独立引入者`（Wikipedia nationality: France）
- **事实复核**：生卒(1886-09-15~1971-12-15, 85岁)/巴黎犹太家庭(父亲 Lucien 综合理工考官)/1905 19 岁首篇论文(Lévy–Steinitz 定理)/Hadamard+Volterra 导师/服役一年+École des Mines 三年+1913 教授/1913 娶 Suzanne/三子女(Marie-Hélène 1913·Denise 1916·Jean Claude 1918)/一战炮兵/1920 Polytechnique 分析教授至 1959/学生 Mandelbrot+Matheron/稳定分布+特征函数+1937 一般 CLT 书《随机变量加法理论》/与 Khinchin 独立无穷可分+Lévy–Khintchine/1930s 鞅+条件期望+Doob 发展/1948 布朗运动专著(Lévy area+arcsine law+local time)/纳粹:1940-12-19 解雇→1941-03-14 复职→1942-11-11 前一周藏匿 Montbonnot/法国科学院+伦敦数学会荣誉会员+Picard Medal 1953/数学世家(Marie-Hélène Schwartz+女婿 Laurent Schwartz 1950 Fields)——全部与 Wikipedia 一致
- **修正 1（伪引语红线 §14.6）**：closingslide 英文自创引语"In the darkest days of WWII, he kept building the mathematics of the future."（Wikipedia 无此原文）→ 改中文忠实转述"在二战最黑暗的日子里，他依然在构建数学的未来。"
- **格式修复**：Unicode `→` 20 处 → `$\rightarrow$`；半角引号 4 处 → 全角；"85岁" → "85 岁"（格式统一）
- **编译**：`make distclean && make` → 0 错误 11 页；仅 1 个模板固有 Overfull hbox 5.33pt（无 vbox 溢出，与 Brauer/Schur 同样干净）
- **排行榜**：#66 保持 `✅/✅✅`（实质达标：Review-1 完成 + 编译干净）
- [ ] 编译: `make distclean && make` — 零错误

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Lévy 过程是核心——独立增量的统一框架
> 2. 鞅的归属要写清楚——Lévy 独立引入，Doob 发展
> 3. Lévy–Khintchine 是与 Khinchin 独立发现
> 4. 1948 布朗运动专著是巅峰成就
> 5. 纳粹幸存叙事要精确而尊重
> 6. 结尾应回归"随机变成了结构"
