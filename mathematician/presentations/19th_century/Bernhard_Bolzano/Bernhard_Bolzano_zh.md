# Bernhard Bolzano（伯恩哈德·波尔查诺）立传提示词

> qid=Q184735 · 1781-10-05 – 1848-12-18 · 波西米亚数学家、逻辑学家、哲学家、天主教神父 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Bernhard_Bolzano/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 波西米亚`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「实轴 / 极限」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Bernardus Placidus Johann Nepomuk Bolzano（常称 Bernard Bolzano，中文惯称：波尔查诺）
- **生卒**：1781-10-05 生于布拉格（波西米亚，神圣罗马帝国）→ 1848-12-18 逝于布拉格，享年 67
- **国籍**：Kingdom of Bohemia（波西米亚王国，今捷克）
- **身份**：数学家、逻辑学家、科学哲学家、天主教神父（意大利血统，德裔）
- **家庭**：父 Bernard Pompeius Bolzano（意大利移民）、母 Maria Cecilia Maurer（布拉格德语家庭）；12 个子女中仅 2 人活到成年
- **教育轨迹**：
  - 1791–1796 就读布拉格 Piarist 文科中学
  - 1796 入布拉格大学，学数学、哲学、物理
  - 1800 起学神学，1804 年成为天主教神父
  - 1804 年获布拉格大学博士学位（导师 Franz Josef Gerstner）
- **导师**：Franz Josef Gerstner（博士导师）
- **研究领域**：数学分析、逻辑、科学哲学、认识论、集合论

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **分析严格化的先驱（ε–δ 极限定义）**：最早引入完全严格的 ε–δ 极限定义，是最早为数学分析注入严格性的数学家之一，其目标直到约 50 年后才被 Weierstrass 实现。
2. **Bolzano 定理（介值定理）**：1817 年给出**介值定理的第一个纯解析证明**（中间值定理）。
3. **Bolzano–Weierstrass 定理**：最先证明（后被 Weierstrass 独立发展并发表，一度称 Weierstrass 定理，直到 Bolzano 更早的工作被重新发现）。
4. **最小上界性质**：最早认识到实数的最小上界性质（least-upper-bound property）。
5. **代数基本定理的纯解析证明**：给出**第一个纯解析证明**（此前 Gauss 的证明是几何式）。
6. **《无穷的悖论》（Paradoxien des Unendlichen，1851 身后出版）**：关于无穷的深刻研究，受到 Peirce、Cantor、Dedekind 等后世逻辑学家的高度赞赏，是集合论的先驱。
7. **《科学理论》（Wissenschaftslehre，1837，四卷）**：为所有科学提供逻辑基础，提出"命题自身（Satz an Sich）"、"观念自身"等概念，是逻辑实在论的开创之作，深刻影响了后来的现象学（胡塞尔）与分析哲学（经布伦塔诺、迈农）。
8. **生平与流放**：1805 年任布拉格大学宗教哲学教授，1818 年当选哲学系主任；因宣扬和平、反对军国主义、主张教育改革，观点过于自由，1819-12-24 被免职并流放乡间（拒绝收回信仰），此后专注于社会、宗教、哲学、数学著述。
9. **身后名声**：生前作品多为手稿，流传有限；1881 年 Otto Stolz 重新发现其遗失论文并重印，其贡献才广为人知。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（波西米亚深绿） | `#1B5E20` | 波西米亚 / 布拉格 |
| 强调色（理性金） | `#C9A227` | 逻辑严格 / 神父身份 |
| 分类色 1（数学分析 — 靛蓝） | `#4C5FD5` | ε–δ / Bolzano 定理 |
| 分类色 2（逻辑哲学 — 青绿） | `#0E7C7B` | Wissenschaftslehre / 逻辑实在论 |
| 分类色 3（集合/无穷 — 琥珀） | `#E07B30` | 无穷悖论 / 最小上界 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「实轴 / 极限 / 集合」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**沉思庄重 / 宗教宁静**（神父学者的理性沉思与虔诚）
- **匹配理由**：
  - 波尔查诺是神父、哲学家、数学家，因坚持信仰被流放——需**沉思、庄重、宁静**的配乐，呼应其宗教虔诚与理性沉思
  - "宁静" 匹配其身后默默无闻、长期埋没的命运
  - "沉思" 匹配其逻辑哲学的深度
- **候选方向**（执行时从音乐库核对具体曲目，优先沉思/庄重/宗教宁静风格）：
  - 首选：沉思 / 庄重 / 宗教宁静风格曲目
  - 备选：古典 / 历史感深沉曲目（呼应 19 世纪布拉格）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「分析严格化的先驱 · 逻辑实在论的奠基者」+ 波尔查诺 1781–1848 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：分析严格化 / 逻辑哲学 / 无穷与集合 / 生平 四分类
4. **早年与教育**（1781–1805）：布拉格、神父、博士、宗教哲学教授
5. **ε–δ 与极限定义**（核心贡献页）：分析严格化先驱、先于 Weierstrass
6. **Bolzano 定理与介值定理**（核心贡献页）：第一个纯解析证明（1817）
7. **Bolzano–Weierstrass 定理与最小上界**（核心贡献页）：实分析基础
8. **代数基本定理的纯解析证明**：先于 Gauss 的几何证明
9. **《无穷的悖论》与集合论先驱**（核心贡献页）：Paradoxien des Unendlichen、影响 Cantor/Dedekind
10. **《科学理论》与逻辑实在论**（核心贡献页）：Wissenschaftslehre、命题自身、影响现象学与分析哲学
11. **流放与身后**：1819 被免职流放、手稿埋没、Otto Stolz 1881 重新发现
12. **终章**：67 岁、生前默默无闻身后伟大的历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **【重要】无肖像**：`images.txt` 仅含 Commons/Wikisource logo，**无 Bolzano 肖像照片**。封面与身份信息页头像必须用装饰圆 `\faIcon{user}` 占位。
- **Bolzano–Weierstrass 定理归属**：Bolzano **最先证明**，但 Weierstrass **独立发展并先发表**，一度称 Weierstrass 定理，直到 Bolzano 更早的工作被重新发现才改称 Bolzano–Weierstrass 定理——勿写"两人合作证明"。
- **ε–δ 极限定义**：Bolzano 是**最早引入严格 ε–δ 定义者之一**，但 Weierstrass 才是将其系统化、广泛传播者——勿写 Bolzano 完成了分析严格化（其目标 50 年后才实现）。
- **代数基本定理**：Bolzano 给出**第一个纯解析证明**，Gauss 此前给出的是**几何式证明**（且 Gauss 的证明更早）——勿混淆先后与证明类型。
- **介值定理（Bolzano 定理）**：Bolzano 给出**第一个纯解析证明**——勿写他是第一个证明者（此前有几何式证明）。
- **国籍**：Kingdom of Bohemia（波西米亚王国），今属捷克——封面用「波西米亚」或「捷克」需注明（生时属神圣罗马帝国/奥地利帝国）。
- **职业**：天主教神父（1804 年受戒），这是重要身份特征——勿遗漏。
- **流放**：1819-12-24 因拒绝收回自由观点被免职并流放乡间——是"因信仰坚持被流放"，非政治犯罪。
- **名字拼写**：Wikipedia 标题为 "Bernard Bolzano"（拼作 Bernard），全名 Bernardus Placidus Johann Nepomuk Bolzano——与常见拼写 Bernhard 略有差异，需以本地数据为准。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q184735 | 待写入 |
| name_zh | 波尔查诺（或 伯恩哈德·波尔查诺） | 待写入 |
| name_en | Bernhard Bolzano | 待写入 |
| birth_date | 1781-10-05 | 待写入 |
| death_date | 1848-12-18 | 待写入 |
| nationality | Kingdom of Bohemia（今捷克） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | mathematical analysis / logic / set theory | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **博士导师**：Franz Josef Gerstner
- **学生**：Robert von Zimmermann、Franz Moth
- **后世影响**：Karl Weierstrass（Bolzano–Weierstrass 定理独立发展者）、Georg Cantor（赞赏其无穷悖论）、Richard Dedekind（赞赏）、Charles Sanders Peirce（赞赏）、Edmund Husserl（经布伦塔诺重新发现）、Otto Stolz（1881 重新发现其遗失论文）
- **哲学传承**：Franz Brentano、Alexius Meinong、Kazimierz Twardowski（受其影响的哲学家）

## 8. 奖项清单

- 无生前重要奖项（生前默默无闻，贡献身后才被认可）

## 9. 机构清单

- 教育：Charles University（布拉格大学，1804 博士）、Piarist College and Gymnasium
- 任职：Charles University（1805–1819 宗教哲学教授，1818 哲学系主任）

## 10. 终审清单

- [ ] 生卒 1781-10-05 / 1848-12-18，享年 67，出生地布拉格
- [ ] 【无肖像】封面/身份信息页头像用装饰圆占位
- [ ] Bolzano–Weierstrass"Bolzano 先证、Weierstrass 独立发展先发表"表述准确
- [ ] ε–δ"最早引入者之一、Weierstrass 系统化"表述准确
- [ ] 代数基本定理"Bolzano 纯解析、Gauss 几何式"表述准确
- [ ] 介值定理"Bolzano 第一个纯解析证明"表述准确
- [ ] 国籍"波西米亚（今捷克）"表述准确
- [ ] 神父身份表述准确
- [ ] 流放"因拒绝收回自由观点被免职"表述准确
- [ ] 名字拼写以 Wikipedia 标题 "Bernard Bolzano" 为准
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Bernhard_Bolzano/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：无肖像，用装饰圆占位
- [ ] **国籍**：封面顶部徽章明示波西米亚（今捷克）
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Gauss / Fourier / Legendre）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
