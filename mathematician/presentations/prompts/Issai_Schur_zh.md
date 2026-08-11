# 舒尔 (Issai Schur) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)。
> 数据库字段梳理见工作指南 §二十一；社会关系入库见 §二十。

---

## 背景信息

- **目标数学家**: Issai Schur (1875–1941)
- **气质关键词**: **Schur 引理、Schur 函数——表示论与组合学的基础语言**
- **Wikipedia 页面**: ✅ 已下载
  - 路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Issai_Schur/`
  - Wikipedia 英文条目: `Issai Schur`
- **Beamer 文件**: `mathematician/presentations/Issai_Schur/Issai_Schur_zh.tex` (待创建)
- **参考模板**: `wiener/`, `ramanujan/`, `hecke/` 的完整源码
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/wiener/Norbert_Wiener_zh.tex`
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/hecke/Makefile`
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`

---

## 第 0 步：核对 Wikipedia 页面 ✅

已下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Issai_Schur/`

- **全名**: Issai Schur（早年名 Schaia/Isaiah）
- **生卒日期**: 1875-01-10 ~ 1941-01-10，享年 **66** 岁（**生日当天逝世**）
  - ⚠ 注意：metadata.json 写 birth 1875-12-29，但 Wikipedia 正文 infobox 与叙述一致为 **1875-01-10**（"on his 66th birthday, on 10 January 1941, he died"），以正文为准
- **国籍**: 🇷🇺 生于 Russian Empire（俄罗斯帝国，白俄罗斯 Mogilev，今 Mahilyow）→ 入德国籍 German Reich
- **出生地**: Mahilyow, Russian Empire（今白俄罗斯莫吉廖夫）
- **逝世地**: Tel Aviv, Mandatory Palestine（特拉维夫，今以色列）
- **博士导师**: Ferdinand Georg Frobenius、Lazarus Fuchs（柏林大学，1901 博士）
- **教育经历**:
  - Nicolai Gymnasium in Libau（利鲍中学，1888–1894，德国语学校，金奖毕业）
  - University of Berlin（柏林大学，1894–1901，summa cum laude 博士）
- **主要任职机构**:
  - University of Berlin（柏林大学，1903–1913 讲师/副教授）
  - University of Bonn（波恩大学，1913–1916 副教授，接替 Hausdorff）
  - University of Berlin（柏林大学，1916–1935 教授，1921 起任 Schottky 教席）
- **关键荣誉**: 1922 加入普鲁士科学院
- **博士学生（26 人）**: Richard Brauer、Alfred Brauer、Karl Dörge、Bernhard Neumann、Félix Pollaczek、Heinz Prüfer、Richard Rado、Isaac Jacob Schoenberg、Wilhelm Specht、Helmut Wielandt 等
- **研究领域**: representation theory（表示论）、group theory（群论）、combinatorics（组合学）、number theory（数论）、linear algebra（线性代数）、theoretical physics（理论物理）
- **家族**: 妻 Regina Frumkin（1906 结婚）；子 Georg（物理学家）、女 Hilde（1932 嫁 Chaim Abelin）

### 关键时间线：

- 1875: 1月10日生于 Mogilev，犹太家庭（父 Moses 商人）
- 1888: 13 岁赴 Liepāja（利鲍），入德国语 Nicolai Gymnasium
- 1894: 10月入柏林大学，主修数学物理
- 1901: 柏林大学博士（Frobenius 与 Fuchs 指导，summa cum laude），论文《关于可分配给给定矩阵的一类矩阵》——一般线性群的多项式表示论
- 1903: 柏林大学讲师
- 1913: 波恩大学副教授（接替 Hausdorff）
- 1916: 回柏林任副教授（Knoblauch 继任）
- 1919: 个人教授
- 1921: 任 Schottky 教席（柏林大学最高教席之一）
- 1922: 加入普鲁士科学院
- 1933: 纳粹上台，4月被停职；Erhard Schmidt 力争后 1933/34 冬季学期可授特殊课程；拒绝威斯康星访问教席
- 1935: 9月30日被正式解职（柏林最后失去教职的犹太教授）
- 1936: 2月赴苏黎世讲座（Hopf、Pólya、Plancherel 安排）
- 1938: 被迫退出普鲁士科学院委员会；妻挡下 Gestapo 传唤
- 1939: 初离开德国赴伯尔尼，后移居巴勒斯坦（支付 Reich 航班税）
- 1941: 1月10日（66 岁生日）因心脏病逝于特拉维夫

### ★ 叙事亮点：

1. **Schur 引理（1905）** — 不可约表示之间的同态必为零或同构，表示论最基础的引理之一，普泛于量子力学与代数。
2. **Schur 函数 / Schur 多项式** — 博士论文中一般线性群不可约多项式表示的特征，成为组合学与代数几何的核心对称函数，Schur–Weyl 对偶的基石。
3. **Schur 分解** — 复方阵酉相似于上三角阵；数值线性代数（QR 算法）的理论基础。
4. **Schur 定理（组合学）** — 1926 年"有限着色必有单色 x+y=z"——Ramsey 理论的先驱（Ramsey 之前）。
5. **Frobenius–Schur 指示子** — 表示论的精细不变量（1/-1/0）。
6. **柏林学派的灵魂** — Frobenius 逝世（1917）后，Schur 是柏林表示论学派的旗手；26 位博士学生（Brauer 兄弟、Wielandt、Schoenberg、Neumann）撑起现代数学多个分支。
7. **纳粹迫害下的尊严** — 1933 停职、1935 解职，Erhard Schmidt 奔走、学生反击；66 岁生日当天去世于流亡地特拉维夫。

### ★ 史实注意：

- **生卒日期**：metadata 写 1875-12-29（俄历？），但 Wikipedia 正文为 **1875-01-10** 出生、**1941-01-10** 逝世（66 岁生日当天）。以正文一致版本为准。
- **署名混乱**：Schur 以 "I. Schur" 和 "J. Schur" 两种署名发表（后者见于 Crelle 杂志），造成目录索引混淆。
- **Schur 定理**：不同领域多个"Schur 定理"（Ramsey 型、整矩阵迹、超中心子群）——注意区分。
- **Schur 引理 vs Schur 函数 vs Schur 分解**：三个不同对象（同态、对称函数、矩阵分解），分页表述。
- **与 Noether 比肩**：Weyl 评价 Schur 的代数群论贡献可与 Emmy Noether 相比（scope and depth）。

---

## 数据库字段核对表（第 0 步之后必填）

| # | 表 | 字段 | 核对值 |
|:--:|---|------|--------------------------|
| 1 | `people` | qid | `Q72599` |
| 2 | `people` | name_en | `Issai Schur` |
| 3 | `people` | name_zh | `伊赛·舒尔` |
| 4 | `people` | name_variants | `["J. Schur","Schaia Schur","Schur 引理的创造者","Schur 函数的命名者","柏林表示论学派的旗手"]` |
| 5 | `people` | gender | `male` |
| 6 | `people` | birth_date | `1875-01-10` |
| 7 | `people` | death_date | `1941-01-10` |
| 8 | `people` | description | `Russian-German mathematician (1875–1941)` |
| 9 | `people` | primary_occupation | `mathematician` |
| 10 | `person_occupation` | 职业（rank 排序） | `mathematician(0)`、`university teacher(1)` |
| 11 | `person_field` | 领域（rank 排序） | `representation theory(0)`、`group theory(1)`、`combinatorics(2)`、`number theory(3)` |
| 12 | `award_laureate` | 获奖记录 | 无大奖；1922 普鲁士科学院院士（非奖项） |
| 13 | `person_institution` | 教育/任职 | `education: Berlin(1894–1901)`；`employment: Berlin(1903–1913)、Bonn(1913–1916)、Berlin(1916–1935)` |
| 14 | `person_nationality` | 国籍 | `Germany`（生于 Russian Empire） |
| 15 | `person_relation` | 社会关系 | 见 §二十（第 4.5 步） |
| 16 | `rankings` | 榜单 | `OpenMath_20th_Century_51_108`、`rank=64`、`status=🔲/🔲` |

> ★ 奖项列注意：**全部收录**（含追授/政治勋章/名誉类，见 21.2.4）。Schur 无正式奖项，仅院士身份。

---

## 第 4.5 步：社会关系入库（MySQL）

> 已按 §二十 梳理，参考实现 `MySQL/seed_schur_relations.py`。

**社会关系清单：**

| 关系类型 | 对象 | 方向 | note |
|---------|------|------|------|
| 老师 | Ferdinand Georg Frobenius | 师→生 | 柏林博士导师（1901），表示论传承 |
| 老师 | Lazarus Fuchs | 师→生 | 柏林博士导师（1901）（已有 634） |
| 学生 | Richard Brauer | 师→生 | 1925 柏林博士（已有 63） |
| 学生 | Alfred Brauer | 师→生 | 1928 柏林博士（已有 669） |
| 学生 | Heinz Prüfer | 师→生 | 1921，Prüfer 群（新建占位） |
| 学生 | Richard Rado | 师→生 | 1933，组合学（新建占位） |
| 学生 | Bernhard Neumann | 师→生 | 1932，群论（新建占位） |
| 学生 | Isaac Jacob Schoenberg | 师→生 | 1926，样条/Toeplitz（新建占位） |
| 学生 | Helmut Wielandt | 师→生 | 1935，置换群（新建占位） |
| 学生 | Wilhelm Specht | 师→生 | 1932，群环（新建占位） |
| 学生 | Karl Dörge | 师→生 | 1925，图论（新建占位） |
| 学生 | Wolfgang Hahn | 师→生 | 特殊函数（新建占位） |
| 学生 | Félix Pollaczek | 师→生 | 1922，排队论（新建占位） |
| 学生 | Robert Frucht | 师→生 | 图的自同构（新建占位） |
| 学生 | Eberhard Hopf | 师→生 | 遍历/动力系统（新建占位） |
| 学生 | Rose Peltesohn | 师→生 | 组合设计（新建占位） |
| 同事 | Erhard Schmidt | 无向 | 柏林同事，为 Schur 复职奔走（已有 464） |
| 同事 | George Pólya | 无向 | 好友，1913 前相识；组织苏黎世讲座（新建占位） |
| 同事 | Heinz Hopf | 无向 | 柏林同事，高度敬重 Schur（已有 28） |
| 同事 | Hermann Weyl | 无向 | 评价 Schur 可与 Noether 比肩（已有 6） |
| 同事 | Emmy Noether | 无向 | 同为代数大师（已有 4） |

**入库操作：**
1. `people` 表：Schur 已存在（id=64），补齐 qid/Q72599、name_variants、description、birth/death；`has_social_data` 置 1
2. `person_field`：representation theory / group theory / combinatorics / number theory 关联
3. `person_institution`：Berlin（教育+任职）、Bonn（任职）
4. `person_nationality`：Germany
5. `person_relation`：Frobenius、Fuchs → Schur；Schur → 13 位学生；Erhard Schmidt/Pólya/Hopf/Weyl/Noether ↔ Schur
6. 缺失人物先建占位（`has_biography=0`），关系 note 加 `[材料待展开]` 前缀

**校验：**
```sql
SELECT a.name_en AS 甲, rt.name_zh AS 关系, b.name_en AS 乙, pr.note
FROM person_relation pr
JOIN people a ON a.id=pr.from_id
JOIN people b ON b.id=pr.to_id
JOIN relation_types rt ON rt.relation_key=pr.relation_type
WHERE a.name_en='Issai Schur' OR b.name_en='Issai Schur';
```

---

## 第 5 步：设计配色方案

- **建议配色：柏林青 + 引理紫 + 组合金 + 流亡米** —— 表示论的优雅 + 纳粹时代的流亡
- 与已有配色完全不同！

- 主要色值：
  | 用途 | 色名 | 建议色值 | 说明 |
  |------|------|---------|------|
  | 背景 | `bgmain` | `#F8F5EE` | 流亡米 —— 柏林学派的底色 |
  | 主色 | `coverprimary` | `#1F3A5C` | 柏林青 —— 柏林表示论学派 |
  | 强调色 | `coveraccent` | `#7A3A8A` | 引理紫 —— Schur 引理 |
  | 深色文本 | `coverdark` | `#1F2A28` | 深墨色 |
  | 浅色文本 | `covermuted` | `#6A7480` | 蓝灰 |

- 四个分类色：
  - **badgeLemma** (Schur 引理) — 引理紫 `#7A3A8A`
  - **badgeFunction** (Schur 函数) — 组合金 `#C9A227`
  - **badgeDecomp** (Schur 分解) — 数值蓝 `#2E5F8A`
  - **badgeBerlin** (柏林学派) — 柏林青 `#1F3A5C`

---

## 第 6 步：规划幻灯片序列（12 页）

```
00  OpenMath 项目首页

=== 封面与总览 ===
01  封面 — 《舒尔：表示论的优雅之刃》 / Issai Schur 1875–1941
02  Hook — 为什么舒尔独一无二：Schur 引理·Schur 函数·柏林学派的旗手

=== 生平与核心贡献 ===
03  早年的教育 (1875–1901) — Mogilev·利鲍中学·柏林·Frobenius 门下
04  Schur 引理 (1905) — 不可约表示的基石·量子力学的语言
05  Schur 函数与 GL(n) 表示 — 博士论文的遗产·Schur–Weyl 对偶

=== 组合学与矩阵 ===
06  Schur 定理与 Ramsey 先驱 (1926) — 单色 x+y=z·组合数学的先声
07  Schur 分解与数值代数 — 酉三角化·QR 算法的理论基座

=== 学派与传承 ===
08  柏林学派的灵魂 (1917–1935) — Frobenius 之后·26 位博士·Brauer/Wielandt/Schoenberg
09  纳粹迫害下的尊严 (1933–1939) — 停职·Schmidt 奔走·流亡巴勒斯坦

=== 人格与历史 ===
10  Schur 的世纪遗产 — 引理·函数·分解·柏林学派的余晖

=== 结尾 ===
11  结束页 — "他用一个引理照亮了表示的星空，又用一座学派点燃了柏林；66 岁的生日，是他的终章。"
```

---

## 第 9 步：史实审查

### Schur 特有的史实陷阱

| 陷阱类型 | 高危点 |
|---------|--------|
| **生卒日期** | 1875-01-10 出生 / 1941-01-10 逝世（66 岁生日当天）——以正文为准，metadata 1875-12-29 存疑 |
| **署名混淆** | I. Schur 与 J. Schur 两种署名 |
| **多个"Schur 定理"** | Ramsey 型、整矩阵、超中心子群——区分 |
| **Schur 引理/函数/分解** | 三个不同对象，分页表述 |
| **Weyl 评价** | 可与 Noether 比肩（代数群论） |
| **纳粹叙事** | 1933 停职→1935 解职→1939 流亡→1941 逝世；Erhard Schmidt 奔走 |

---

## 第 13 步：Wikipedia 本地文档终审（提交前必做）

### 终审清单
- [ ] 生卒日期 1875-01-10 / 1941-01-10 正确（66 岁生日当天）
- [ ] 博士导师 Frobenius、Fuchs 正确
- [ ] Schur 引理 1905 正确
- [ ] Schur 函数（博士论文）正确
- [ ] 1926 Schur 定理（Ramsey 先驱）正确
- [ ] 1933-1939 纳粹迫害叙事客观
- [ ] 编译: `make distclean && make` — 零错误

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Schur 引理是核心——表示论最基础的引理
> 2. Schur 函数/多项式是组合学与代数几何的桥梁
> 3. 柏林学派传承是叙事主线——Brauer 兄弟、Wielandt、Schoenberg
> 4. 纳粹叙事要克制而尊重——他是"柏林最后失去教职的犹太教授"
> 5. 生卒日期以 Wikipedia 正文 1875-01-10/1941-01-10 为准
> 6. 结尾应回归"表示论的优雅之刃"
