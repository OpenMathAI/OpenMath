# Ernst Kummer（恩斯特·库默尔）立传提示词

> qid=Q57245 · 1810-01-29 – 1893-05-14 · 德国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Ernst_Kummer/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「理想数 / 分圆域」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Ernst Eduard Kummer（中文惯称：库默尔）
- **生卒**：1810-01-29 生于索劳（Sorau，勃兰登堡，普鲁士）→ 1893-05-14 逝于柏林，享年 83
- **国籍**：Kingdom of Prussia（普鲁士王国，今德国）
- **身份**：数学家（理想数、费马大定理、库默尔理论）
- **家庭**：父为医生，1813 年去世；1840 年娶 Ottilie Mendelssohn（门德尔松家族，Nathan Mendelssohn 之女，Felix Mendelssohn 的表妹），Ottilie 1848 年去世后再娶 Bertha Cauer（Ottilie 的母系表妹），共 13 个子女；女儿 Marie 嫁给数学家 Hermann Schwarz
- **教育轨迹**：
  - 最初学习新教神学，后转学数学
  - 1831 年获哈雷大学（University of Halle）博士（获奖数学论文《De cosinuum et sinuum potestatibus...》）
- **导师**：Heinrich Scherk（博士导师）
- **研究领域**：数论、理想数、库默尔理论、应用数学

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **理想数（ideal number）与费马大定理（最著名贡献）**：为证明费马大定理，引入"理想数"概念（"ideal"一词由库默尔发明），证明费马大定理对**正则素数**（regular prime）指数成立——这是费马大定理研究的一大里程碑，也奠定了后来 Dedekind 理想理论的基础。
2. **正则素数（regular prime）**：引入正则素数概念，是费马大定理证明的核心工具。
3. **库默尔理论（Kummer theory）**：研究域扩张（库默尔扩张），是类域论的基础。
4. **库默尔曲面（Kummer surface）**：二维阿贝尔簇除以循环群 {1, −1} 得到（有 16 个奇点的早期 orbifold）。
5. **超几何级数**：整理了不同超几何级数之间的邻接关系（contiguity relations）。
6. **库默尔函数**：以其命名的特殊函数。
7. **教育贡献**：在 gymnasium（德国文科中学）任教 10 年，**启发了 Leopold Kronecker 的数学事业**；也曾训练德军军官弹道学。
8. **门德尔松家族姻亲**：1840 年娶 Ottilie Mendelssohn（Felix Mendelssohn 表妹），与数学家 Dirichlet（娶 Rebecca Mendelssohn Bartholdy）成为姻亲。
9. **学生众多**：Eisenstein、Frobenius、Fuchs、Killing、Schwarz、Cantor 等一代德国数学家皆出其门下。
10. **荣誉**：巴伐利亚马克西米利安科学与艺术勋章、ForMemRS；小行星 25628 Kummer 以其命名。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（普鲁士深蓝） | `#1F3A93` | 德意志理性 |
| 强调色（数学金） | `#C9A227` | 理想数 / 尊崇 |
| 分类色 1（理想数/费马 — 靛蓝） | `#4C5FD5` | 理想数 / 正则素数 |
| 分类色 2（库默尔理论 — 青绿） | `#0E7C7B` | 库默尔理论 / 类域论 |
| 分类色 3（曲面/函数 — 琥珀） | `#E07B30` | 库默尔曲面 / 库默尔函数 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「理想数 / 分圆域」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典庄重 / 学术严谨**（理想数理论的深刻与严谨）
- **匹配理由**：
  - 库默尔是理想数理论的创立者、费马大定理的重要推进者——需**庄重、严谨、典雅**的配乐
  - "严谨" 匹配其数论工作的深度
  - "典雅" 匹配其门德尔松家族姻亲的文化气质
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：古典 / 庄重 / 典雅风格曲目
  - 备选：历史感深沉曲目（呼应 19 世纪柏林）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「理想数的创立者 · 费马大定理的推进者」+ 库默尔 1810–1893 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：理想数与费马 / 库默尔理论 / 曲面与函数 / 生平 四分类
4. **早年与教育**（1810–1831）：Sorau、神学转数学、哈雷大学博士
5. **理想数与费马大定理**（核心贡献页）：理想数、"ideal"一词、正则素数
6. **正则素数与费马大定理的推进**（核心贡献页）：一类素数指数的证明
7. **库默尔理论**（核心贡献页）：域扩张、类域论基础
8. **库默尔曲面与超几何级数**（核心贡献页）：16 奇点 orbifold、邻接关系
9. **教育与门德尔松姻亲**（核心叙事页）：gymnasium 任教、启发 Kronecker、娶 Ottilie Mendelssohn
10. **学生与学术传承**（核心叙事页）：Eisenstein、Frobenius、Fuchs、Schwarz、Cantor
11. **荣誉与晚年**：巴伐利亚勋章、ForMemRS、1890 退休
12. **终章**：83 岁、从理想数到类域论的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **理想数（ideal number）**：库默尔为证明费马大定理引入"理想数"，发明了"ideal"一词——但库默尔的方法是**理想数**（ideal number），与后来 Dedekind 发展的**理想理论**（ideal theory）不同，库默尔的方法更接近 p-adic 方法——勿写"库默尔建立了理想理论"（那是 Dedekind 的贡献）。
- **费马大定理**：库默尔证明对**正则素数**指数成立（一大类素数），**并非**证明整个费马大定理——勿夸大。
- **正则素数**：库默尔引入正则素数概念，但注意 100 以内的非正则素数仅 37、59、67 等少数几个——正则素数是一大类。
- **库默尔曲面**：由二维阿贝尔簇除以循环群 {1, −1} 得到，有 16 个奇点，是"早期 orbifold"——表述准确。
- **库默尔理论**：是类域论的基础——是"奠基性"，勿写库默尔建立了类域论（类域论是后世的系统理论）。
- **生卒日期**：出生日 metadata 有 1810-01-29 与 1810-00-00，以 Wikipedia infobox **1810-01-29** 为准；死亡日有 1893-05-14/04-14，以 **1893-05-14** 为准。
- **无肖像**：`images.txt` 仅含 Commons logo，无 Kummer 本人肖像，封面头像需用装饰圆占位。
- **国籍**：Kingdom of Prussia（普鲁士王国），今属德国——封面用「德国（普鲁士王国）」。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q57245 | 待写入 |
| name_zh | 库默尔（或 恩斯特·库默尔） | 待写入 |
| name_en | Ernst Kummer | 待写入 |
| birth_date | 1810-01-29 | 待写入 |
| death_date | 1893-05-14 | 待写入 |
| nationality | Germany（普鲁士王国） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | number theory / ideal theory / Kummer theory | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **博士导师**：Heinrich Scherk
- **学生**：Gotthold Eisenstein、Ferdinand Georg Frobenius、Lazarus Fuchs、Wilhelm Killing、Hermann Schwarz、Georg Cantor、Adolf Kneser、Franz Mertens 等
- **启发**：Leopold Kronecker（gymnasium 任教期间启发其数学事业）
- **姻亲**：妻 Ottilie Mendelssohn（门德尔松家族）、Peter Gustav Lejeune Dirichlet（连襟，其妻 Rebecca 为 Ottilie 表妹）
- **合作**：William Rowan Hamilton（共同研究射线系统 ray systems）
- **家族**：女儿 Marie 嫁 Hermann Schwarz

## 8. 奖项清单

- Bavarian Maximilian Order for Science and Art（巴伐利亚马克西米利安科学与艺术勋章）
- Foreign Member of the Royal Society（英国皇家学会外籍会员）

## 9. 机构清单

- 教育：Martin Luther University Halle-Wittenberg（哈雷大学，博士）、Königliches Gymnasium zu Sorau
- 任职：University of Wrocław（布雷斯劳大学）、Technische Universität Berlin（柏林工业大学）、Frederick William University Berlin（柏林大学）、Königliches Gymnasium zu Sorau、Liegnitz Ritter-Akademie

## 10. 终审清单

- [ ] 生卒 1810-01-29 / 1893-05-14，享年 83，出生地 Sorau
- [ ] 理想数"库默尔引入、Dedekind 发展理想理论"表述准确
- [ ] 费马大定理"对正则素数成立、非整个定理"表述准确
- [ ] 库默尔理论"类域论基础"表述准确
- [ ] 库默尔曲面"16 奇点 orbifold"表述准确
- [ ] 启发 Kronecker"gymnasium 任教"表述准确
- [ ] 门德尔松姻亲表述准确
- [ ] 头像确认（无肖像则装饰圆占位）
- [ ] 国籍用「德国（普鲁士王国）」表述准确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Ernst_Kummer/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：无肖像，用装饰圆占位
- [ ] **国籍**：封面顶部徽章明示德国（普鲁士王国）
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Liouville / Hamilton / Dirichlet）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
