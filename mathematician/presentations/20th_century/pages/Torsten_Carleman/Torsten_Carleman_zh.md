# Torsten Carleman（托尔斯滕·卡莱曼）立传提示词

> 榜单：#103 · qid=Q526581 · 1892-07-08 – 1949-01-11 · 瑞典数学家
> 数据库主记录：id=103（经典分析大师，Mittag-Leffler 研究所所长 20+ 年）

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Tage Gillis Torsten Carleman
- **生卒**：1892-07-08 维斯尔托夫塔（Visseltofta，斯科讷省）→ 1949-01-11 斯德哥尔摩，享年 56
- **国籍**：瑞典
- **身份**：数学家、大学教师（瑞典最有影响力的数学家）
- **机构轨迹**：
  - 教育：乌普萨拉大学（博士，导师 Holmgren）
  - 任职：隆德大学 → 斯德哥尔摩大学 → **Mittag-Leffler 研究所所长（20+ 年）**
- **研究领域**：经典分析、奇异积分方程、积分算子谱论、复分析（整函数）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **Carleman 不等式**：级数不等式（Hardy 不等式的加强）——分析学经典不等式。
2. **Carleman 矩阵与线性化**：非线性动力系统的线性化表示（Carleman linearization）——现代动力系统/控制论工具。
3. **Carleman 核与积分算子谱论**：奇异积分方程的谱理论。
4. **Denjoy–Carleman 定理 / Denjoy–Carleman–Ahlfors 定理**：整函数理论（与 Denjoy、Ahlfors 相关）。
5. **Carleman 条件**：矩问题的可解性条件。
6. **均值遍历定理（mean ergodic theorem）**：遍历理论的基础结果（与 von Neumann 相关）。
7. **Mittag-Leffler 研究所所长 20+ 年**：瑞典数学的实际掌门人。
8. **Björkén 奖（1941）与 Peccot 讲座（1922）**。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（斯德哥尔摩蓝） | #1E4E79 | 斯德哥尔摩传统 |
| 辅助（分析青） | #1E6E6E | 经典分析 |
| 强调（算子金） | #B8860B | 积分算子谱论 |
| 背景 | #FAF6EF | 米白纸色 |

## 4. 12 页 Slide 规划

1. 封面：大标题 + 副标题「Carleman 不等式 · 积分算子谱论 · 瑞典数学掌门人」
2. 生平总览：时间轴（1892 → 博士 → 隆德/斯德哥尔摩 → Mittag-Leffler 所长 → 1949 去世）
3. Carleman 不等式：Hardy 的加强
4. Carleman 矩阵与线性化
5. Carleman 核与积分算子谱论
6. Denjoy–Carleman–Ahlfors 定理
7. Carleman 条件：矩问题
8. 均值遍历定理
9. Mittag-Leffler 研究所 20+ 年
10. 瑞典分析学派：Fredholm 传统
11. 荣誉：Björkén 1941、Peccot 1922
12. 终章：56 岁、历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **均值遍历定理归属**：与 von Neumann 相关（von Neumann 1932 证希尔伯特空间版本）——**不写 Carleman 独占**。
- **Denjoy–Carleman 归属**：与 Denjoy 共同命名（整函数）——表述精确。
- **Carleman 不等式 vs 矩阵 vs 条件 vs 核**：多个 Carleman 命名——slide 中区分。
- **Mittag-Leffler 所长**：20+ 年（正文明确）。
- **生卒核对**：1892-07-08 / 1949-01-11。
- **Fredholm 关联**：瑞典分析学派传统（Fredholm(73)）。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q526581 | 需更新（当前 NULL） |
| name_zh | 托尔斯滕·卡莱曼 | 已统一（卡莱曼） |
| birth_date | 1892-07-08 | 需更新 |
| death_date | 1949-01-11 | 需更新 |
| has_biography | 0 | 保持 |
| has_social_data | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20，已由 seed 脚本完成）

- 导师：Erik Albert Holmgren（新建）
- 学生：Åke Pleijel（新建）、Hans Rådström（新建）
- 相关：Gösta Mittag-Leffler（778，研究所）、Erik Ivar Fredholm（73，瑞典分析传统）

## 8. 奖项清单（全部收录）

- Björkén Prize 1941（259）
- Cours Peccot 1922（99）

## 9. 机构清单

- 教育：Uppsala University（144）
- 任职：Lund University（114）、Stockholm University（115）、Mittag-Leffler Institute（新建）

## 10. 终审清单

- [ ] 均值遍历定理归属
- [ ] 多个 Carleman 命名区分
- [ ] Mittag-Leffler 所长 20+ 年
- [ ] has_biography 保持 0
## 11. Review 流程规范（两轮 Review，§16 Wikipedia 终审 + 项目标准）

> 立传完成后按此规范执行两轮 Review（参照 #73 Fredholm Review-1 执行标准）。

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/<Name>/page.md` 建立事实基准，逐页对照 Beamer tex 的全部事实（生卒/机构/年份/奖项/荣誉/家族/引语）
- [ ] **头像**：优先使用 Wikipedia infobox 照片（`images.txt` 或 infobox `image` 字段），下载原图到 `images/<name>_portrait.jpg`；无照片时用装饰圆替代
- [ ] **国籍**：封面顶部徽章明确国籍（`\faIcon{globe}\enspace <Country>`），与 Cartan/Borel/Fredholm 立传格式一致
- [ ] **引语核对**：tex 引语必须能在 Wikipedia 原文找到（§14.6 伪引语红线）；找不到则改为忠实转述
- [ ] **编译验证**：`make distclean && make`（latexmk 自动多遍编译；remember picture 需要多遍）
- [ ] **更新提示词**：Review 修正（头像来源/国籍/新细节）写回 `prompts/<Name>_zh.md`
- [ ] **更新排行榜**：`✅/🔲` → `✅/✅✅`

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 结束页时间线 ≥7 段拆两行（避免溢出）
- [ ] 中文标点/断行/间距统一
- [ ] 与同榜数学家格式对齐（封面/配色/结构）
- [ ] 排行榜标记 `✅✅/🔲` → `✅✅/✅✅`

---

## Review-1 记录 (2026-08-13)

> ⚠️⚠️ **灾难性错误修复**：结合本地 Wikipedia (`pages/Torsten_Carleman/page.md`) 发现，本 tex 文件原内容**几乎完整复制自 Vladimir Rokhlin**——标题改成了 Torsten Carleman，但正文残留大量 Rokhlin 内容（Rokhlin 引理/定理、Lebesgue--Rokhlin、Gudkov 猜想、二战战俘、Baku 出生、列宁格勒学派、俄文 `Владимир Абрамович Рохлин`、错误学生名单"Alexandrov/Vershik"等）。
> **已整体重写整个 tex 文件**，替换为正确的 Torsten Carleman 内容。

- **头像** ✅：`Torsten_Carleman.jpg` 原在根目录，已复制到 `images/` 并采用标准圆角框（1.92cm）
- **国籍** ✅：封面 `\faIcon{globe}\enspace Sweden\enspace·\enspace Mittag-Leffler Institute\enspace·\enspace 56 岁`（Wikidata nationality: Sweden）
- **身份信息页** ✅：重写 `\earlyslide`（Visseltofta 出生、Uppsala 大学导师 Erik Albert Holmgren、奇异积分方程、Lund/Stockholm/Mittag-Leffler 任职轨迹）
- **重写核心事实**（全部基于 Wikipedia）：
  - 生卒 1892-07-08 ~ 1949-01-11（享年 56）✅；全名 Tage Gillis Torsten Carleman ✅
  - 导师 Erik Albert Holmgren（Uppsala）✅
  - Carleman 不等式（Hardy 加强，$\sum (a_1\cdots a_n)^{1/n} \le e\sum a_n$，1926）✅
  - Carleman 核与积分算子谱论（博士论文+1920s 早期，奇异积分方程）✅
  - Denjoy--Carleman 定理（拟解析函数充要条件）+ Carleman 条件（矩问题）✅
  - Carleman 线性化（Carleman embedding，1932，Poincaré/Fredholm/Koopman 后续）✅
  - 平均遍历定理（1930s，独立于 von Neumann）+ 广义 Fourier 变换（1935，预示 Sato/Schwartz）✅
  - Carleman 估计 + Boltzmann 方程全局存在性首次证明（空间齐次，posthumous 1957）+ Denjoy--Carleman--Ahlfors 定理（1933）✅
  - Mittag-Leffler 所长 20+ 年（1927 起）+ Acta Mathematica 编辑 ✅
  - 荣誉：Björkén 奖 1941、Peccot 讲座 1922、瑞典皇家科学院院士 1926、芬兰科学与文学学会 1934 ✅
  - 学生：Åke Pleijel、Hans Rådström、Ulf Hellsten、Karl Persson ✅
  - 争议：反犹指控 + William Feller 事件 + 晚年酗酒/神经痛/黄疸（客观记录）✅
- **格式统一**：section title 字号 20/24 + 副标题 7.5/9.5；封面国籍行 `\enspace` + 14pt；英文名行 `1892--1949`（去空格）；封面 badge 2 行；配色调整 coveraccent/badgeHist 由苏联红 → 瑞典金 `#B8860B`
- **修复**：`warslide` 缺反斜杠 → `\warslide`；slide 顺序（`\warslide` 移 `\closingslide` 之前，结束页置末）
- **编译**：`make distclean && make` → ✅ 13页，0错误；无 Missing character / Undefined；hbox 5.33pt + vbox 8.19/7.12/9.48pt 均 <10pt
- **排行榜**：#103 保持 `✅/✅✅`（榜单已预标记，本轮完成第1轮实际 review）

---

## Review-2 记录 (2026-08-13)

- **Overfull/Underfull** ✅：hbox 5.33pt + vbox 8.19/7.12/9.48pt，均 <10pt 阈值
- **结束页时间线** ✅：两行 3+3 段（`Visseltofta → Uppsala → Lund/Stockholm` / `Mittag-Leffler 所长 1927 → Björkén 1941 → Stockholm 1949`），无溢出
- **中文标点统一** ✅：无 `\u201c`/`\u201d` 转义残留（grep 计数 0）
- **残留清理** ✅：已确认无 Rokhlin/俄文/Gudkov/Baku/Plessner/Lebesgue--Rokhlin 等错误内容残留（整体重写后彻底清除）
- **格式对齐** ✅：封面（圆角头像框 + 国籍 `\enspace Sweden` + 2 行 badge）、配色（瑞典蓝 + 金 `#B8860B`）、结构（13 页）均与同榜数学家一致
- **编译**：`make distclean && make` → ✅ 13页，0错误
- **排行榜**：#103 Review 列保持 `✅✅`（第2轮完成）

---

## Review-3 记录 (2026-08-13)

> 用户要求"再来 review 一次"——针对上一轮整体重写后遗留的代码卫生问题与头像真实性做复检。

- **头像真实性** ✅：`file` 命令确认 `Torsten_Carleman.jpg` 为有效 JPEG（124×180，AppleMark），与 `figure_my/Torsten Carleman.jpg` 尺寸一致——是真实肖像照片而非占位图（Wikipedia infobox 无照片，项目自备头像库提供）
- **⚠️ 命令名残留清理（上一轮遗漏）**：整体重写时保留了 4 个 Rokhlin 模板的命令名，语义与内容完全不符，已重命名：
  | 旧命令名 | 新命令名 | 对应内容 |
  |---|---|---|
  | `\gudkovslide` | `\linearizationslide` | Carleman 线性化（Gudkov 是 Rokhlin 内容） |
  | `\lpspaceslide` | `\quasianalyticslide` | Denjoy--Carleman 定理（Lp 空间完全无关） |
  | `\leningradschoolslide` | `\mathphysicsslide` | 数学物理（列宁格勒学派是 Rokhlin 内容） |
  | `\warslide` | `\controversyslide` | 争议与晚年（war 不准确） |
- **残留复查** ✅：grep 确认无 `gudkovslide/lpspaceslide/leningradschoolslide/warslide` 及 `Rokhlin/Рохлин/Gudkov/Baku/Plessner/Lebesgue--Rokhlin` 任何残留
- **编译**：`make distclean && make` → ✅ 13页，0错误；重命名未引入 Undefined；hbox 5.33pt + vbox 8.19/7.12/9.48pt 均 <10pt
- **事实复核**：13 页全部事实（生卒/全名/导师/机构/荣誉/贡献/争议）与 Wikipedia 一致，无新增事实错误

