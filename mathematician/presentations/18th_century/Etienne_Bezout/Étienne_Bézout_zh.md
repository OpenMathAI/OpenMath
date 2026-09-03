# Étienne Bézout（艾蒂安·贝祖）立传提示词

> qid=Q289471 · 1730-03-31 – 1783-09-27 · 法国数学家 · 18 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/18th_century/pages/Étienne_Bézout/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考 18 世纪 Euler 模板）

> 本提示词正文（Beamer tex）**采用 Euler/d'Alembert 18 世纪模板形式**。硬性要求：

1. **封面有头像**：右上角肖像 + 细边框（Commons 肖像已就位 `images/bezout_portrait.jpg`，280×326 标准 JPEG）。
2. **封面有国籍**：副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏三要素。
3. **必须有身份信息页**（★ 必做）：左侧肖像 + 右侧 2×2 信息网格，事实取自 Wikipedia infobox。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；气泡呼应「曲线交点 / 消元法」母题。
5. **品牌口径统一**：结尾页 `OpenMathAI`；引号半角。

---

## 1. 背景信息（Slide 1-3）

- **全名**：Étienne Bézout（中文惯称：贝祖，尊称"消元理论之父 / 海军炮兵数学教育家"）
- **生卒**：1730-03-31 生于 Nemours（塞纳-马恩省，法兰西王国）→ 1783-09-27 逝于 Avon（塞纳-马恩省，枫丹白露附近，Île-de-France），享年 53
- **国籍**：法国（Kingdom of France）
- **身份**：数学家（infobox Fields: Mathematics；metadata field_of_work 记 number theory）
- **家庭**：**次子**，父 Pierre Bézout 与祖父皆任地方行政官（district magistrate），家族政治背景显赫；母 Jeanne-Hélène Filz；24 岁结婚
- **研究领域**：数学——代数方程、方程理论、消元理论、数论
- **受 Euler 影响**：早年深受欧拉影响，选择数学为业

## 2. 核心叙事亮点（Slide 4-14）

1. **贝祖定理（Bézout's theorem）**：平面代数曲线论基本定理——两条代数曲线的交点数（计重数与无穷远点）等于其次数之积。
2. **Little Bézout 定理**：即多项式余数定理——多项式 $f(x)$ 除以 $x-a$ 的余数为 $f(a)$；与曲线交点的贝祖定理是两个不同命题，勿混同。
3. **贝祖恒等式（Bézout's identity）**：$ax + by = \gcd(a,b)$ 的整数解存在性，数论基本结论。
4. **贝祖矩阵**：用于求多项式最大公因式的结式矩阵。
5. **贝祖整环（Bézout domain）**：主理想环的推广，每对元素有 Bézout 关系的整环。
6. **消元理论**：《代数方程的一般理论》（Théorie générale des équations algébriques，1779，巴黎）——最著名著作，汇集方程理论诸论文，含消元理论与根的对称函数大量新成果。
7. **入法国科学院（1758，28 岁）**：当选力学 adjoint；1768 升 associé；1770 升 pensionnaire。（⚠️ Wikipedia 英文条目自相矛盾写"19 岁"，1730 年生 1758 年应为 28 岁，勿采"19 岁"。）
8. **海军卫队数学教育**：1763 年经 Choiseul 公爵授职，任 Gardes de la Marine 数学教师与考官；受命编写海军学员专用教材——四卷《Cours de mathématiques à l'usage des Gardes du Pavillon et de la Marine》（1764–1767）。
9. **炮兵考官与六卷教科书**：1768 年炮兵考官 Camus 去世，贝祖继任 Corps d'Artillerie 考官；为此再编《Cours complet de mathématiques à l'usage de la marine et de l'artillerie》六卷（1770–1782），影响深远。
10. **行列式的早期使用**：1764 年《Histoire de l'académie royale》论文中使用行列式，但未处理一般理论。
11. **方程的可解类研究**：《Sur plusieurs classes d'équations de tous les degrés qui admettent une solution algébrique》考察将一元方程"化为"两个二元方程求解的途径。
12. **身后纪念**：Nemours 故里立像；2000 年小行星 17285 Bezout 以他命名。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（法国蓝） | `#1F4E79` | 法国 / 枫丹白露 |
| 强调色（代数金） | `#C9A227` | 代数与消元尊崇 |
| 分类色 1（代数几何 — 靛蓝） | `#4C5FD5` | 贝祖定理 |
| 分类色 2（数论 — 青绿） | `#0E7C7B` | 贝祖恒等式 |
| 分类色 3（教育 — 琥珀） | `#E07B30` | 海军炮兵教材 |
| 分类色 4（人生/纪念 — 玫红） | `#B76E79` | 考官生涯 / 身后纪念 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡，呼应「曲线交点 / 代数方程」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】
- **风格定调**：古典典雅 / 启蒙理性的沉稳（消元理论奠基者）
- **候选方向**：古典 / 典雅曲目（沿用 Timeless）；时长 ≥ 13 页 × 7 秒 ≈ 91 秒。

## 4. Slide 规划（15 页 = openmath 1 + 正文 14，参照 Euler 18 世纪模板）

> 正文版式对齐 Euler 模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；特色页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「消元理论之父 · 海军数学教育家」+ 贝祖 1730–1783 + 右上肖像 + 国籍行「法国」+ 状态栏 + 4 分类 badge（代数几何/数论/教育/方程理论）
2. **身份信息页**（`\profileslide`，★ 必做）：左肖像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 家庭 / 职务 / 荣誉 / 核心领域 / 出生地）
3. **贝祖的一生：时间线**（`\timelineslide`，8 段）：1730 Nemours 出生 → 1758 入科学院（28 岁）→ 1763 Choiseul 授职海军卫队 → 1764-67 四卷教材 → 1768 继任炮兵考官 → 1770 pensionnaire / 六卷开编 → 1779《代数方程一般理论》→ 1783 去世
4. **早年与教育**（`\earlyslide`，表格）：次子、父祖两代行政官、Euler 影响择业、24 岁结婚
5. **贝祖定理**（核心贡献页，表格 + 公式框）：曲线交点 = 次数之积、Little Bézout 区分
6. **贝祖恒等式**（核心贡献页，表格 + 公式框）：$ax+by=\gcd(a,b)$
7. **贝祖矩阵与贝祖整环**（核心贡献页，表格）：结式矩阵、主理想环推广
8. **《代数方程的一般理论》**（核心贡献页，表格）：1779、消元理论、根的对称函数、可解类研究
9. **海军卫队与四卷教材**（`\navyslide`，特色表格）：Choiseul 授职、Gardes du Pavillon et de la Marine、1764-67
10. **炮兵考官与六卷教科书**（特色表格）：1768 继 Camus、Corps d'Artillerie、六卷 1770-82
11. **行列式与对称函数**（`\detonslide`，特色表格）：1764 使用未及一般理论、根的对称函数成果
12. **荣誉与传承**（`\honorslide`，表格）：科学院三级晋升、Nemours 立像、小行星 17285 Bezout、命名家族（定理/恒等式/矩阵/整环）
13. **终章**（`\closingslide`）：53 岁、"消元理论之父"的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **"19 岁入科学院"勘误（重要）**：Wikipedia 英文条目自相矛盾（"At the age of 19 (in 1758)"），1730 年生 1758 年应为 **28 岁**——勿采"19 岁"，表述"1758 年（28 岁）当选"。
- **两个"贝祖定理"**：代数几何中"两曲线交点 = 次数之积"（需计重数与无穷远点）是 Bézout's theorem；"Little Bézout"即多项式余数定理——**两个不同命题，勿混在一条里**。
- **贝祖恒等式**：$ax+by=\gcd(a,b)$ 整数解存在性，是数论基本结论——勿写"贝祖发明最大公约数"。
- **行列式**：1764 年《Histoire de l'académie royale》论文中使用行列式，但**未发展一般理论**——勿写"贝祖创立行列式理论"。
- **消元理论**：《Théorie générale des équations algébriques》（1779，巴黎）是代表作，贡献在消元法与根的对称函数——表述准确。
- **职业结构**：主要精力在教学与教材编纂（海军卫队+炮兵考官），代数研究时间有限——表述准确。
- ** Choiseul 授职**：1763 年海军卫队职位由 Choiseul 公爵提供；24 岁结婚与接受此职相关（正文表述）。
- **头像**：Commons 肖像 280×326 偏小但可用；勿用 Justin Sanson 雕像照（Nemours 立像）作头像。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q289471 | 已写入 |
| name_zh | 贝祖 | 已写入 |
| name_en | Étienne Bézout | 已写入 |
| birth_date | 1730-03-31 | 已写入 |
| death_date | 1783-09-27 | 已写入 |
| nationality | Kingdom of France | 已写入 |
| primary_occupation | mathematician | 已写入 |
| has_biography | 1 | 已置 1 |

## 7. 社会关系入库清单（§20，已入库 2 条）

- **受影响**：Leonhard Euler（早年深受欧拉影响，colleague）——已入库
- **父**：Pierre Bézout（Nemours 地方行政官，parent-child）——2026-09-03 补入库

## 8. 奖项清单

- 无特别个人奖项（以命名纪念为主）

## 9. 机构清单

- 任职：French Academy of Sciences（法国科学院，1758 adjoint / 1768 associé / 1770 pensionnaire）
- 教学：École des gardes de la marine（海军卫队学校）；École d'artillerie de La Fère（拉费尔炮兵学校）

## 10. 终审清单

- [x] 生卒 1730-03-31 / 1783-09-27，享年 53，出生地 Nemours
- [x] 国籍「法国」表述准确
- [x] "1758 年（28 岁）入科学院"勘误（勿采"19 岁"）
- [x] 贝祖定理 vs Little Bézout vs 恒等式区分清楚
- [x] 行列式"使用未发展一般理论"表述准确
- [x] 消元理论贡献表述准确
- [x] Choiseul 授职 + Camus 继任线索表述准确
- [x] 教学教材贡献表述准确
- [x] 正文采用 Euler 模板（真实肖像）+ 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审（2026-09-03 完成）
- [x] 结合本地 `pages/Étienne_Bézout/page.md` 建立事实基准（qid=Q289471 核对）
- [x] 头像：Commons `Etienne Bezout2.jpg`（280×326）已下载至 `images/bezout_portrait.jpg`
- [x] 编译验证 `make distclean && make`，15 页无错误
- [x] 更新提示词写回本文件（§0 改 Euler 模板；§1 次子/家族两代行政官/Fields；§2 亮点 9→12 条——勘误"19 岁"为 28 岁、拆分两个贝祖定理、补 Choiseul/Camus 线索、可解类研究；§3 补第 4 分类色；§4 重排 15 页；§5 补勘误/ Choiseul/头像陷阱；§7 父子关系补入库）

### 第 2 轮（Review-2）：结构优化（2026-09-03 完成）
- [x] Overfull/Underfull 告警检查与修复
- [x] 身份信息页与 Euler 模板对齐（肖像 + 2×2 信息网格）
- [x] 中文标点 / 断行 / 间距统一
- [x] 与同世纪数学家（Euler / d'Alembert / de Moivre / Maclaurin / Bernoulli / Lambert / Monge / Waring）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
