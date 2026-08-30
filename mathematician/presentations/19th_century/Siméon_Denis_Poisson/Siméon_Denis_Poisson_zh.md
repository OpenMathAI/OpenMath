# Siméon Denis Poisson（西梅翁·德尼·泊松）立传提示词

> qid=Q190772 · 1781-06-21 – 1840-04-25 · 法国数学家、物理学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Siméon_Denis_Poisson/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「概率分布 / 势场」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Siméon Denis Poisson（中文惯称：泊松）
- **生卒**：1781-06-21 生于皮蒂维耶（Pithiviers，巴黎以南约 80 公里）→ 1840-04-25 逝于索镇（Sceaux，近巴黎），享年 58
- **国籍**：France（法国）
- **身份**：数学家、物理学家（概率论、势论、分析力学、电磁学、弹性力学）
- **家庭**：父 Siméon Poisson（参加过七年战争的退伍军人，憎恶贵族）；1817 年娶 Nancy de Bardi，育有 4 个子女
- **教育轨迹**：
  - 1798 年以第一名的成绩考入 École Polytechnique（入学考试竞争激烈）
  - 入学不足两年，在最后一年发表两篇论文（关于 Bézout 消元法、有限差分方程积分个数），出色到 1800 年被**免试毕业**
  - 第二篇论文获 Lacroix 与 Legendre 推荐发表于《Recueil des savants étrangers》，对 18 岁青年是空前荣誉
- **导师**：Joseph-Louis Lagrange（朋友）、Pierre-Simon Laplace（视其如子）
- **研究领域**：概率论、数学分析、力学、理论物理、电磁学、弹性力学

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **泊松斑（Arago spot，最著名轶事）**：作为 1817 年 Fresnel 衍射论文的评审委员，为**反驳波动说**，他计算发现 Fresnel 理论预言圆形障碍物阴影中心会出现一个亮斑（粒子说预言全暗）。他以为这是荒谬的反证，结果 Arago 实验竟证实了这个亮斑——反而**支持了波动说**，Fresnel 因此获奖。这个"泊松斑"是科学史上"想反驳却反而证实"的经典案例。
2. **泊松分布（Poisson distribution）**：1830 年论文《论新生儿男女比例》（Mémoire sur la proportion des naissances des filles et des garçons，1829 作）中首次出现现代泊松分布；1837 年《论判断的概率》（Recherches sur la probabilité des jugements）再次出现。
3. **泊松方程（Poisson's equation）**：1813 年发表的 ∇²φ = −4πρ，是拉普拉斯方程的推广，适用于引力、电、磁。
4. **泊松括号（Poisson bracket）**：1809 年引入，是哈密顿力学的核心工具，Jacobi 后来认识到其重要性并给出 Jacobi 恒等式，成为李代数研究的基础；狄拉克在 1925 年建立量子力学时正是借助泊松括号理解了海森堡的反交换性。
5. **泊松过程、泊松比、泊松核、泊松求和公式**：多项以其命名的概念，体现其贡献广度。
6. **分析力学的继承者**：代表作《力学专论》（Traité de mécanique，两卷），沿拉格朗日、拉普拉斯风格；引入广义动量的显式公式，接近发展正则变换理论（由 Jacobi 完成）。
7. **弹性力学与流体力学**：1829 年独立于 Navier 得到粘性流体运动方程（Navier–Stokes 方程）；与 Cauchy、Germain 同为 19 世纪弹性理论主要贡献者；泊松比首次在此背景下引入。
8. **势论与电磁学**：继承拉普拉斯的势函数概念，1812 年应用于电学；其势论工作启发了 George Green 1828 年的论文。
9. **荣誉与地位**：1827 年接替拉普拉斯任经度局几何学家；1837 年成为法国贵族院议员（peer of France，作为法国科学代表）；Copley Medal、Lalande Prize、FRS、埃菲尔塔 72 名之一。
10. **与 Galois 的互动**：1831 年 Galois 提交论文，Poisson 认为"难以理解"但鼓励其完整发表——这段互动影响了 Galois 后来的抉择。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（法国深蓝） | `#1F3A93` | 法兰西理性 |
| 强调色（物理琥珀） | `#E07B30` | 物理 / 电磁 |
| 分类色 1（概率统计 — 靛蓝） | `#4C5FD5` | 泊松分布 / 概率 |
| 分类色 2（势论/方程 — 青绿） | `#0E7C7B` | 泊松方程 / 势论 |
| 分类色 3（力学 — 玫红） | `#B76E79` | 泊松括号 / 分析力学 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「概率分布 / 势场」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典庄重 / 科学理性**（拉普拉斯学派的严谨继承者）
- **匹配理由**：
  - 泊松是拉普拉斯、拉格朗日的传人，横跨数学与物理——需**庄重、理性、典雅**的配乐
  - "理性" 匹配其大量数学物理贡献
  - "典雅" 匹配其法国科学院、贵族院的地位
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/典雅风格）：
  - 首选：古典 / 庄重 / 典雅风格曲目
  - 备选：历史感深沉曲目（呼应 18-19 世纪之交）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「概率、势论与分析力学的继承者」+ 泊松 1781–1840 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **泊松的一生：时间线**（`\timelineslide`）：1781 出生 → 1798 综合理工 → 1809 泊松括号 → 1817 泊松斑 → 1829 泊松分布 → 1837 贵族院 → 1840 去世
4. **早年与教育**（1781–1800，表格）：Pithiviers、第一名入学、免试毕业、18 岁论文
5. **泊松斑（Arago spot）**（表格）：反驳波动说反证成真、Fresnel 获奖
6. **泊松分布与概率论**（核心贡献页，表格 + 泊松分布公式框）：新生儿男女比例、判断的概率
7. **泊松方程与势论**（核心贡献页，表格 + ∇²φ=−4πρ 公式框）：启发 Green
8. **泊松括号与分析力学**（核心贡献页，表格 + 泊松括号公式框）：哈密顿力学核心工具、Jacobi 恒等式、狄拉克量子力学
9. **弹性与流体力学**（表格）：Navier–Stokes 方程、泊松比、发散定理特例
10. **电磁学与热传导**（表格）：势论、傅里叶级数采纳、泊松核
11. **荣誉与 Galois 互动**（表格）：Copley Medal、贵族院议员、对 Galois 的评审
12. **终章**：58 岁、从概率到物理的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **泊松斑（Arago spot）归属**：泊松**预言**了这个亮斑，但他是**为了反驳波动说**而计算出的（认为荒谬），实际**证实**了波动说；实验由 **Arago** 完成——勿写成"泊松发现了光的波动性"或"泊松支持波动说"。
- **泊松分布**：现代泊松分布**首次出现**于 1829 年论文（1830 发表），早期实例可追溯到 de Moivre《机会的学说》（1718）——勿写泊松是第一个研究该分布的人（他是现代形式的系统化者）。
- **Navier–Stokes 方程**：Navier 1821 年先得到，Poisson 1829 年**独立**得到，Stokes 1845 年重新推导——勿写泊松首创。
- **泊松括号**：Poisson 1809 年引入，但**Jacobi** 首先认识到其理论力学价值并给出 Jacobi 恒等式；"泊松括号"之名可能是 Whittaker 1910 年首次使用——勿写泊松建立了李代数理论。
- **泊松比**：泊松引入的数学模型**后来被证明是错误的**，但泊松比这一概念仍有广泛应用——勿写泊松的弹性理论完全正确。
- **导师**：Lagrange、Laplace 是**学术引路人/导师**（Poisson 视 Laplace 如父），非现代博士导师制——但 metadata 明确标注为 doctoral_advisor，可写"导师"。
- **Galois 评审**：Poisson 认为 Galois 1831 年论文"难以理解"，但**鼓励其完整发表**——是客观评审，勿写成恶意打压。
- **死亡**：1840-04-25 逝于 Sceaux，享年 58；去世时正在撰写一部数学物理专著。
- **男爵身份**：1825 年被授予男爵，但**未领取证书也未使用头衔**——勿写成"使用了男爵头衔"。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q190772 | 待写入 |
| name_zh | 泊松（或 西梅翁·德尼·泊松） | 待写入 |
| name_en | Siméon Denis Poisson | 待写入 |
| birth_date | 1781-06-21 | 待写入 |
| death_date | 1840-04-25 | 待写入 |
| nationality | France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | probability theory / mathematical analysis / mechanics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：Joseph-Louis Lagrange、Pierre-Simon Laplace
- **学生**：Peter Gustav Lejeune Dirichlet、Joseph Liouville、Michel Chasles、Mikhail Ostrogradsky
- **评审 / 互动**：Augustin-Jean Fresnel（泊松斑相关）、François Arago（实验证实泊松斑）、Évariste Galois（1831 论文评审）
- **学术继承**：William Rowan Hamilton、Carl Gustav Jacob Jacobi（受其《力学专论》影响）、George Green（受其势论启发）
- **同期**：Adrien-Marie Legendre（早年论文推荐者）、Joseph Fourier（其傅里叶级数被 Poisson 采纳）、Sophie Germain（弹性理论竞争）
- **家族**：父 Siméon Poisson（退伍军人）、妻 Nancy de Bardi

## 8. 奖项清单

- Copley Medal（科普利奖章）
- Lalande Prize（拉朗德奖）
- Fellow of the Royal Society（英国皇家学会会员，1818）
- Fellow of the American Academy of Arts and Sciences（美国艺术与科学院外籍荣誉会员，1822）
- 1823 年瑞典皇家科学院外籍会员
- 埃菲尔铁塔 72 位法国科学家刻名之一（身后纪念）

## 9. 机构清单

- 教育：École Polytechnique
- 任职：École Polytechnique（教授，1806 接替 Fourier）、Bureau des Longitudes（经度局，1808 天文学家，1827 接替 Laplace 任几何学家）、Faculté des sciences de Paris（1809 理性力学教授）、École Spéciale Militaire de Saint-Cyr（1815 考官）

## 10. 终审清单

- [ ] 生卒 1781-06-21 / 1840-04-25，享年 58，出生地 Pithiviers
- [ ] 泊松斑"泊松预言、为反驳波动说、Arago 实验证实"表述准确
- [ ] 泊松分布"现代形式 1829 首发、早期实例 de Moivre"表述准确
- [ ] Navier–Stokes"Navier 先得、Poisson 独立、Stokes 重推"表述准确
- [ ] 泊松括号"Poisson 引入、Jacobi 认识价值"表述准确
- [ ] 泊松比"数学模型后证有误、概念仍有用"表述准确
- [ ] Galois 评审"客观、鼓励发表"表述准确
- [ ] 男爵"未领取未使用头衔"表述准确
- [ ] 国籍用「法国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Siméon_Denis_Poisson/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：优先 Wikipedia infobox 肖像（`images.txt` 中 E. Marcellot 1804 年肖像）
- [ ] **国籍**：封面顶部徽章明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（如 Arago 转述的"人生只有两件事：做数学和教数学"）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Fourier / Gauss / Legendre）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
