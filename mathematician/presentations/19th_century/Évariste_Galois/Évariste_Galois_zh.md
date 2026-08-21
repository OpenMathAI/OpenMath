# Évariste Galois（埃瓦里斯特·伽罗瓦）立传提示词

> qid=Q7091 · 1811-10-25 – 1832-05-31 · 法国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Évariste_Galois/`（page.md + metadata.json）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 身份 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「对称 / 群作用」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Évariste Galois（中文惯称：伽罗瓦）
- **生卒**：1811-10-25 生于巴黎郊区的 Bourg-la-Reine（法兰西第一帝国）→ 1832-05-31 逝于巴黎（七月王朝），享年 20
- **国籍**：France（法国，生卒横跨第一帝国、波旁复辟、七月王朝）
- **身份**：数学家、政治活动家（共和派革命者）
- **父母**：父 Nicolas-Gabriel Galois（共和派，曾任 Bourg-la-Reine 市长）；母 Adélaïde-Marie（née Demante，法学家之女，通晓拉丁语与古典文学，负责其 12 岁前的家庭教育）
- **教育轨迹**：
  - 1823 年入 Lycée Louis-le-Grand（约 12 岁），教师 Louis Paul Émile Richard 赏识其天赋
  - 14 岁起对数学产生浓厚兴趣；读 Legendre《Éléments de Géométrie》"如读小说"，一遍精通
  - 15 岁读 Lagrange 原著《Réflexions sur la résolution algébrique des équations》等
  - 1828 年报考 École Polytechnique（当时法国数学最高学府），因口试缺解释而失败
  - 同年入 École Normale（当时称 École préparatoire，数学地位远逊于 Polytechnique）
  - 1829-07-28 父亲因与村中神父的政治纠纷自杀；数日后第二次报考 Polytechnique 仍失败
  - 1829-12-29 通过 Baccalaureate 考试获学位，进入 École normale
- **任职轨迹**：无正式学术职位；1831 年 1 月被开除出 École Normale 后曾尝试开办高等代数私课，因政治活动优先而不了了之
- **研究领域**：群论、方程理论、伽罗瓦理论、域论、抽象代数、有限域

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **群论奠基**：首次以接近现代技术含义使用 "groupe" 一词，把群分解为左/右陪集（"proper decomposition"），导出今日的**正规子群**概念——群论创始人之一。
2. **伽罗瓦理论（最高成就）**：认识到多项式根式可解性与根的置换群结构（伽罗瓦群）相关；方程可根式解 ⟺ 其伽罗瓦群有一串正规子群塔、商群为阿贝尔（即伽罗瓦群**可解**）。这一方法后来被推广到数学诸多领域。
3. **五次及以上方程无根式解**：给出"任意多项式是否可根式解"的判定理论，解决了困扰学界 350 年的开放问题（Abel 1824 已证五次不可解，Galois 给出更深刻的一般理论）。
4. **有限域（伽罗瓦域）**：首次清晰表述有限域概念（今以 GF(p^n) 记，以他命名）。
5. **有限单群的早期构造**：构造 GL(ν, p) 并计算其阶；构造 PSL(2, p)（分式线性变换），观察到 p≠2,3 时为单群——这是继交错群之后的**第二类有限单群**。
6. **分析与其他贡献**：连分数（1828 第一篇论文，二次无理数循环连分数周期判据）、阿贝尔积分（把代数微分的积分分三类）。
7. **20 岁决斗身亡**：决斗前夜（1832-05-29）写下给 Auguste Chevalier 的"数学遗嘱"信，概述其思想并附三份手稿——Hermann Weyl 称之为"若以思想的新颖与深刻论，也许是人类全部文献中最厚重的一篇"。
8. **身后重见天日**：手稿被 Joseph Liouville 于 1843 年承认价值、1846 年发表于《Journal de Mathématiques Pures et Appliquées》。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（共和深蓝） | `#1A237E` | 法兰西共和 / 理性主义 |
| 强调色（革命红） | `#C62828` | 七月革命 / 决斗与燃烧的青春 |
| 分类色 1（群论 — 靛蓝） | `#4C5FD5` | 群论与对称 |
| 分类色 2（方程理论 — 青绿） | `#0E7C7B` | 伽罗瓦理论 / 可解性 |
| 分类色 3（有限域 — 琥珀） | `#E07B30` | 伽罗瓦域 GF(p^n) |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「群作用的轨道 / 置换对称」与「自相似」的视觉语言（与 Wilson 的自相似气泡背景一致）。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**: **悲剧英雄 / 浪漫燃烧**（短促而炽烈的生命，浪漫主义悲剧英雄）
- **匹配理由**:
  - 伽罗瓦的生命只有 20 年，其思想却燃尽了此后一个多世纪的代数研究——需要**炽烈、决绝、带悲剧张力**的配乐，而非沉稳的纪录片风
  - "浪漫" 匹配其时代——法国复辟与七月革命的动荡，共和派的理想主义与决斗的宿命感
  - "燃烧" 匹配其结局——决斗前夜通宵写下数学遗嘱，把一生思想托付给后世的悲壮
- **候选方向**（执行时从音乐库核对具体曲目，优先悲剧/浪漫/史诗风格，其次怀旧）:
  - 首选：悲剧史诗 / 浪漫主义风格曲目（呼应"20 岁的天才陨落"）
  - 备选：`Nostalgia`（怀旧，若库中仅此可作次选，呼应"遗稿被后世追认"的怅惘）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「群论与伽罗瓦理论的奠基人」+ 伽罗瓦 1811–1832 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 身份 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：群论 / 伽罗瓦理论 / 有限域 / 连分数·阿贝尔积分 四分类
4. **早年与教育**（1811–1829）：Bourg-la-Reine 出生、母家庭教育、Louis-le-Grand、读 Legendre/Lagrange、Polytechnique 两次落榜、父亲自杀
5. **群论奠基**（核心贡献页）：groupe、正规子群、陪集分解
6. **伽罗瓦理论**（核心贡献页）：可解群、五次方程不可解的一般判定
7. **有限域与有限单群**：GF(p^n)、GL(ν,p)、PSL(2,p)
8. **政治风暴与牢狱**（1830–1832）：七月革命、被开除、国民自卫军、"敬酒"事件、Sainte-Pélagie 监狱
9. **决斗与数学遗嘱**（1832 年 5 月）：决斗动机成谜、给 Chevalier 的信、Hermann Weyl 的评价
10. **身后：Liouville 与手稿重见天日**（1843–1846）
11. **连分数与阿贝尔积分**：分析方面的早期贡献
12. **终章**：20 岁、遗产与历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **生卒核对**：1811-10-25 / 1832-05-31，享年 20（20 岁），metadata 与正文一致。
- **决斗动机**：Wikipedia 明确"动机至今不明"（obscure），有 Stéphanie-Félicie Poterin du Motel 恋爱说、共和派政治说等多种推测——**勿断言单一原因**，写"动机成谜"。
- **五次方程归属**：Abel 1824 年已证五次方程不可根式解（Abel–Ruffini 定理）；Galois 给出**判定任意方程可根式解的一般理论**（更深刻）——勿写"Galois 首次证明五次不可解"。
- **群论归属**：Galois 是首次以现代技术含义使用 "groupe" 一词者，但置换群思想前人（Lagrange、Ruffini、Cauchy）已有——勿写"Galois 独自发明置换"。
- **Poisson 评价**：1831 年 Poisson 判其手稿"不可理解"（incomprehensible），但报告结尾鼓励其发表全部工作——勿写成一味否定。
- **Cauchy 审稿**：Cauchy 拒绝了早期论文但被广泛认为**赏识其价值**（建议合并投稿竞逐大奖）——勿写成 Cauchy 打压。
- **Fourier 手稿遗失**：1830 年经 Cauchy 建议投稿给 Fourier 竞逐大奖，Fourier 随即去世、手稿遗失——勿写有人故意丢失。
- **有限域归属**：Galois 首次清晰表述有限域概念（"伽罗瓦域"）——归属无误。
- **PSL(2,p) 单性**：p≠2,3 时为单群（例外 p=5,7,11 作用在 p 点）——注意数学细节。
- **国籍表述**：封面顶部用「法国」作为现代对应（生卒横跨多政权）。
- **去世细节**：1832-05-30 决斗腹部中弹、次日晨在 Hôpital Cochin 去世（可能死于腹膜炎），临终拒见神父——勿渲染。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q7091 | 待写入 |
| name_zh | 埃瓦里斯特·伽罗瓦（或 伽罗瓦） | 待写入 |
| name_en | Évariste Galois | 待写入 |
| birth_date | 1811-10-25 | 待写入 |
| death_date | 1832-05-31 | 待写入 |
| nationality | France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | group theory / Galois theory / abstract algebra | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **数学引路人 / 审稿人**：Augustin-Louis Cauchy（审其早期论文）、Joseph Fourier（大奖投稿后手稿遗失）、Siméon Denis Poisson（判"不可理解"）
- **手稿整理与发表者**：Joseph Liouville（1846 年发表其手稿）、Auguste Chevalier（挚友，数学遗嘱收信人）
- **中学教师**：Louis Paul Émile Richard（Louis-le-Grand 赏识者）
- **家族**：父 Nicolas-Gabriel Galois、母 Adélaïde-Marie (née Demante)、弟 Alfred（临终遗言对象）

## 8. 奖项清单

- Concours général（法国中学生竞赛奖，metadata `award_received` 唯一记录）
- （Galois 生前未获任何学术大奖，勿杜撰；其身后地位由 Liouville 1846 年发表手稿确立）

## 9. 机构清单

- 教育：Lycée Louis-le-Grand、École Normale Supérieure（当时称 École préparatoire，未获学位）
- 报考（落榜）：École Polytechnique（1828、1829 两次）
- 政治：National Guard (France, 1830-1871)（国民自卫军炮兵部队，metadata `employer`）

## 10. 终审清单

- [ ] 决斗动机写成谜，不杜撰
- [ ] 五次方程归属正确（Abel 证不可解，Galois 给一般理论）
- [ ] 群论"首次使用 groupe"措辞准确，不写独自发明置换
- [ ] Poisson "不可理解但鼓励发表"、Cauchy "赏识" 表述准确
- [ ] 有限域、PSL(2,p) 单性数学细节正确
- [ ] 生卒 1811-10-25 / 1832-05-31，享年 20
- [ ] 国籍用「法国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Évariste_Galois/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先 Wikipedia infobox 照片（`images.txt`）；无则用装饰圆占位
- [ ] **国籍**：封面顶部徽章明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到，否则忠实转述（如临终遗言 "Ne pleure pas, Alfred! ..."、遗嘱 "Ask Jacobi or Gauss ..."）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Abel / Frobenius）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
