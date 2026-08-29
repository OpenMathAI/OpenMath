# Jean-Victor Poncelet（让-维克托·庞斯莱）立传提示词

> qid=Q168452 · 1788-07-01 – 1867-12-22 · 法国工程师、数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Jean-Victor_Poncelet/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「射影 / 对偶」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Jean-Victor Poncelet（中文惯称：庞斯莱）
- **生卒**：1788-07-01 生于梅斯（Metz，法兰西王国）→ 1867-12-22 逝于巴黎（法兰西第二帝国），享年 79
- **国籍**：France（法国）
- **身份**：数学家、工程师（军事工程师）、物理学家（射影几何复兴者、机械功概念开创者）
- **家庭**：父 Claude Poncelet（梅斯议会律师、富有的地主），母 Anne-Marie Perrein（出身较普通）；庞斯莱是私生子，后被父亲合法化
- **教育轨迹**：
  - 就读 Metz 的 Lycée Fabert（法贝尔中学）
  - 1808–1810 就读 École Polytechnique（巴黎综合理工）
  - 毕业后加入军事工程兵，就读 Metz 应用学校，获陆军中尉军衔
- **导师**：Gaspard Monge
- **研究领域**：射影几何、力学、机械功

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **战俘营中写就奠基之作（最动人叙事）**：1812 年参加拿破仑远征俄国，在克拉斯内战役中被俘，囚禁于萨拉托夫（Saratov）。1813–1814 年在狱中**凭记忆（无任何书籍）**写出射影几何奠基之作《图形的射影性质论》（Traité des propriétés projectives des figures），1814 年获释后才得以出版。
2. **射影几何的复兴者**：1822 年出版《图形的射影性质论》，是自 17 世纪 Desargues 以来第一部系统论述射影几何的著作，被视为现代射影几何的奠基之作。
3. **对偶原理（principle of duality）**：由射影调和共轭、极点极线等发现引出对偶原理；与 Gergonne 就优先权发生激烈争执。
4. **连续性原理（principle of continuity）**：发展连续性原理，助力复数概念的发展。
5. **无穷远点与圆无穷远点**：发展平行线交于无穷远点的概念，定义平面上所有圆共有的圆无穷远点（circular points at infinity）。
6. **庞斯莱闭形定理（Poncelet's porism）**：一个多边形内接于一圆锥曲线且外切于另一圆锥曲线时，必属于一个无穷多边形族。
7. **Poncelet–Steiner 定理**：1822 年发现（1833 年 Steiner 证明）——若给定一个圆及其圆心，欧几里得尺规作图可仅用直尺完成。
8. **机械功概念的开创者**：任力学教授期间，独立于 Coriolis 开创"功"（work）概念与功-能定理，并**创造"机械功"（mechanical work）一词**。
9. **水轮机改进**：改进水轮机与水车设计（其设计的涡轮机 1838 年才建成，但 12 年前就已构想）。
10. **荣誉与地位**：1837 年索邦大学专门为他设立"物理与实验力学教席"；1848 年成为母校 École Polytechnique 的校长（Commanding General）；Pour le Mérite（1863）、ForMemRS（1842）、荣誉军团各级、埃菲尔塔 72 名之一。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（法国深蓝） | `#1F3A93` | 法兰西理性 |
| 强调色（工程金） | `#C9A227` | 工程师 / 军事工程 |
| 分类色 1（射影几何 — 靛蓝） | `#4C5FD5` | 射影 / 对偶原理 |
| 分类色 2（机械功 — 青绿） | `#0E7C7B` | 功 / 水轮机 |
| 分类色 3（无穷远 — 琥珀） | `#E07B30` | 无穷远点 / 连续性原理 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「射影 / 圆锥曲线」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**坚毅沉思 / 战俘营中的创造**（逆境中的坚持与智慧）
- **匹配理由**：
  - 庞斯莱在俄国战俘营中凭记忆写出奠基之作——需**坚毅、沉思、有韧性**的配乐，呼应逆境中的创造
  - "沉思" 匹配其在狱中独自构建射影几何体系
  - "坚毅" 匹配其军事工程师的生涯与复出后的成就
- **候选方向**（执行时从音乐库核对具体曲目，优先坚毅/沉思/韧性风格）：
  - 首选：坚毅 / 沉思 / 韧性风格曲目（呼应战俘营创造）
  - 备选：古典 / 庄重曲目（呼应法国工程师传统）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「射影几何的复兴者 · 机械功的开创者」+ 庞斯莱 1788–1867 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：射影几何 / 机械功 / 无穷远点 / 生平 四分类
4. **早年与教育**（1788–1812）：Metz、École Polytechnique、军事工程兵、中尉
5. **战俘营中的创造**（核心叙事页）：1812 远征俄国、克拉斯内被俘、萨拉托夫狱中写书
6. **射影几何的复兴**（核心贡献页）：《图形的射影性质论》、自 Desargues 以来首部系统著作
7. **对偶原理与连续性原理**（核心贡献页）：对偶、连续性、与 Gergonne 之争
8. **无穷远点与圆无穷远点**：平行线、circular points、助力复数
9. **庞斯莱闭形定理与 Poncelet–Steiner 定理**（核心贡献页）
10. **机械功与工程**（核心贡献页）：功-能定理、"机械功"一词、水轮机
11. **荣誉与地位**：索邦教席、École Polytechnique 校长、Pour le Mérite、埃菲尔塔 72 名
12. **终章**：79 岁、从战俘营到射影几何复兴的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **战俘营著书**：庞斯莱在萨拉托夫狱中**凭记忆**写出《图形的射影性质论》，**1814 年获释后才出版**（1822 年才正式出版）——勿写成"狱中出版"。
- **射影几何复兴者**：是"复兴"（自 Desargues 以来），非"发明"射影几何——Monge 此前也写过少量相关工作。
- **Poncelet–Steiner 定理**：Poncelet **1822 年发现**，Steiner **1833 年证明**——勿混淆发现与证明。
- **对偶原理优先权**：与 **Gergonne** 有激烈优先权之争——客观表述为"有争议"，勿单方面归功。
- **机械功**：**独立于 Coriolis** 开创"功"概念，并创造"机械功"一词——勿写成与 Coriolis 合作。
- **水轮机**：其设计的涡轮机 1838 年才建成，但 12 年前已构想——勿写成 1838 年才发明。
- **私生子身份**：是私生子后经父亲合法化（1825 年）——可作背景，不必过度强调。
- **无肖像**：`images.txt` 中无明确肖像照片（第一张为签名），封面头像需确认是否有可用肖像，否则用装饰圆占位。
- **国籍表述**：封面顶部用「法国」作为现代对应。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q168452 | 待写入 |
| name_zh | 庞斯莱（或 让-维克托·庞斯莱） | 待写入 |
| name_en | Jean-Victor Poncelet | 待写入 |
| birth_date | 1788-07-01 | 待写入 |
| death_date | 1867-12-22 | 待写入 |
| nationality | France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | projective geometry / mechanics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：Gaspard Monge
- **优先权之争**：Joseph Diaz Gergonne（对偶原理优先权之争）
- **定理相关**：Jakob Steiner（Poncelet–Steiner 定理证明者）
- **机械功相关**：Gaspard-Gustave de Coriolis（独立开创功概念）
- **学术帮助**：Louis Jacques Thénard（支持其索邦教席）
- **同事**：Charles Julien Brianchon（早期合作，对 Feuerbach 定理的贡献）

## 8. 奖项清单

- Pour le Mérite for Sciences and Arts（科学与艺术功勋勋章，1863）
- Foreign Member of the Royal Society（英国皇家学会外籍会员，1842）
- Knight / Officer / Commander / Grand Officer of the Legion of Honour（荣誉军团各级勋章）
- Montyon Science Award（蒙蒂永科学奖）
- Fellow of the American Academy of Arts and Sciences（1865）
- 埃菲尔铁塔 72 位法国科学家刻名之一（身后纪念）

## 9. 机构清单

- 教育：École Polytechnique、Lycée Fabert、École d'application de l'artillerie et du génie in Metz
- 任职：École Polytechnique（1848 起任校长）、Engineering Arm（工程兵）、École d'application（Metz，1825–1835 力学教授）、University of Paris（索邦，1837 起物理与实验力学教授）

## 10. 终审清单

- [ ] 生卒 1788-07-01 / 1867-12-22，享年 79，出生地 Metz
- [ ] 战俘营"凭记忆著书、获释后出版"表述准确
- [ ] 射影几何"复兴者"（自 Desargues）表述准确
- [ ] Poncelet–Steiner"Poncelet 发现、Steiner 证明"表述准确
- [ ] 对偶原理"与 Gergonne 有优先权之争"表述准确
- [ ] 机械功"独立于 Coriolis、创造机械功一词"表述准确
- [ ] 水轮机"构想早于建成 12 年"表述准确
- [ ] 头像确认（无肖像则装饰圆占位）
- [ ] 国籍用「法国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Jean-Victor_Poncelet/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认有无可用肖像，无则用装饰圆占位
- [ ] **国籍**：封面顶部徽章明示法国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Poisson / Gauss / Fourier）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
