# Jean le Rond d'Alembert（让·勒朗·达朗贝尔）立传提示词

> qid=Q153232 · 1717-11-16 – 1783-10-29 · 法国数学家、物理学家、哲学家、音乐理论家 · 18 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/18th_century/pages/Jean_le_Rond_d'Alembert/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson + 18 世纪 Euler 模板）

> 本提示词正文（Beamer tex）**采用 Euler 立传模板的 18 世纪风格**，主色"法国蓝 + 启蒙金"，参照 Kenneth G. Wilson 物理学家形式（身份信息页 + 气泡背景）。意味着在数学家立传基础上，强调以下格式要求：

1. **封面有头像**：右上角 Lusurier 1777 肖像 + `draw=mathgold!50` 细边框 + 姓名小字注（已下载至 `images/dalembert_portrait.jpg`，500×618 标准 JPEG）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应波动方程的"涟漪"母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Jean Le Rond d'Alembert（中文：达朗贝尔，"d'Alembert"亦可写作"D'Alembert"或"达朗伯"，尊称"启蒙时代的理性之光"）
- **生卒**：1717-11-16 生于巴黎（圣让勒隆教堂台阶，弃婴）→ 1783-10-29 逝于巴黎，享年 65（膀胱疾病，无标记普通墓）
- **国籍**：法国（French，Kingdom of France）
- **身份**：数学家、物理学家、哲学家、音乐理论家、百科全书派（encyclopédiste）、工程师、翻译家、作家
- **身世**：私生子——母 Claudine Guérin de Tencin（作家、贵族）、父 chevalier Louis-Camus Destouches（炮兵军官，出生时在国外）；数日后母亲把他遗弃在 Saint-Jean-le-Rond 教堂台阶，按主保圣人命名；父亲暗中寻回，安置于玻璃匠之妻 Madame Rousseau 家抚养近 50 年
- **教育轨迹**：
  - 1729（12 岁）入詹森派马萨林学院（Collège des Quatre-Nations / Collège Mazarin），学哲学、法律与艺术
  - 1735 获学士（baccalauréat ès arts）
  - 1738 获律师资格（avocat）
  - 1739 首次数学贡献：指出 Reynaud 1708 年《Analyse démontrée》中的错误
- **导师 / 学术影响**：以自学为主；主要受 Newton 与 Descartes 影响（其晚年鄙视笛卡尔的"涡旋说"）；metadata 标注 doctoral_advisor Léonor Caron（学院教师）；与 Maupertuis、Clairaut、Euler、Daniel Bernoulli 通信
- **研究领域**：分析（波动方程、级数审敛）、力学（达朗贝尔原理、虚功）、天体力学（三体问题、岁差）、流体力学（达朗贝尔佯谬）、代数基本定理（法国称达朗贝尔-高斯定理）、哲学（百科全书、唯心论）、音乐理论（拉莫之争）

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **弃婴出身**：出生后数日被遗弃于圣让勒隆教堂台阶；父亲暗中资助，养于玻璃匠之妻 Rousseau 家近 50 年；养母的名言"你将永远只是一个哲学家——而哲学家是什么呢，无非是一头折磨自己一辈子以求死后被人谈论的蠢驴"（Wikipedia 原文忠实转述）。
2. **波动方程（1747）**：建立弦振动的偏微分方程 $\partial^2 u/\partial t^2 = c^2 \partial^2 u/\partial x^2$ 与达朗贝尔公式（行波解）；后来出现的达朗贝尔算子 $\Box = (1/c^2)\partial^2_t - \nabla^2$ 在现代物理中至关重要。
3. **达朗贝尔原理（1743）**：在《Traité de dynamique》中发展自己的运动定律，将动力学问题化为静力学问题（虚功思想先驱）：$\sum_i (\mathbf{F}_i - m_i\mathbf{a}_i) \cdot \delta\mathbf{r}_i = 0$。
4. **比值审敛法**：以比值 $\lim |a_{n+1}/a_n|$ 判定正项级数敛散，是级数理论基本工具。
5. **代数基本定理**：1746 年给出证明（有缺陷，Gauss 1799 纠正）；法国称此定理为"达朗贝尔-高斯定理"。
6. **达朗贝尔佯谬（1752）**：证明无粘不可压流体中物体所受阻力为零——理想流体与现实的经典悖论。
7. **百科全书与启蒙运动**：1740s 后期与狄德罗（Diderot）合编《Encyclopédie》，负责数学与科学部分，撰写 1000+ 条目，著名的《绪论》（Discours préliminaire）规划了"知识之树"；1757 年因日内瓦牧师文章引发争议后退出。
8. **音乐理论**：1749 评论拉莫（Rameau）的 Mémoire，1752 年出版《音乐理论与实践要素》（Éléments de musique théorique et pratique）普及拉莫学说；与拉莫发生争论、友谊破裂。
9. **哲学转向**：从唯物主义转向怀疑主义（怀疑外部世界是否存在），同意贝克莱唯心主义，预示康德的先验唯心主义。
10. **天体力学**：研究三体问题、地球轴岁差与章动（牛顿体系），著《Réflexions sur la cause générale des vents》（1746）等。
11. **后世评价**：法国称代数基本定理为达朗贝尔-高斯定理；达朗贝尔算子、达朗贝尔体系以他命名；学生拉普拉斯（Pierre-Simon de Laplace）成为法国数学物理学派核心。

## 3. 配色方案（参考 18 世纪 Euler 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（法国蓝） | `#1E4E79` | 巴黎 / 法国 / 启蒙理性 |
| 强调色（启蒙金） | `#C9A227` | 18 世纪知识的光辉 |
| 分类色 1（分析 — 靛蓝） | `#4C5FD5` | 波动方程 / 比值审敛法 |
| 分类色 2（力学 — 青绿） | `#0E7C7B` | 达朗贝尔原理 / 佯谬 |
| 分类色 3（哲学/百科全书 — 琥珀） | `#E07B30` | 百科全书 / 哲学 |
| 分类色 4（音乐理论 — 玫红） | `#B76E79` | 拉莫之争 / 音乐 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应波动方程的"弦振动涟漪"——也象征启蒙时代的理性秩序。

### 3.5 背景音乐选择（待执行时确定）

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/`
> （执行时从 `curated_tracks.md` 选定具体曲目，以下给出风格定调与候选方向。）

- **风格定调**：**古典 / 启蒙 / 理性 / 优雅**（"百科全书派"主笔的广博与典雅）
- **匹配理由**：
  - 达朗贝尔是百科全书派的科学主笔，贡献横跨分析、力学、哲学、音乐——需**优雅、理性、典雅**的配乐
  - "典雅" 匹配其 18 世纪法国沙龙文化
  - "理性" 匹配百科全书派与启蒙时代的秩序感
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/启蒙/典雅风格）：
  - 首选：18 世纪古典/巴洛克风格曲目（与欧拉立传统一）
  - 备选：法国启蒙时期作曲家的曲目（贴近 18 世纪巴黎氛围）
  - 时长需 ≥ 16 页 × 7 秒 ≈ 112 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页正文 + 1 页 openmath，参照 Euler 18 世纪模板）

> 正文版式对齐欧拉模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题"达朗贝尔"（24pt 法国蓝）+ Jean le Rond d'Alembert 1717 — 1783 + 副标题"波动方程·达朗贝尔原理·比值审敛法·百科全书" + 国籍行 + 4 分类 badge（分析/力学/哲学/音乐理论）+ Lusurier 1777 肖像 + 底部三要素状态栏
2. **身份信息页**（`\profileslide`，★ 必做）：左 Lusurier 1777 肖像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 荣誉 / 核心领域）
3. **达朗贝尔的一生：时间线**（`\timelineslide`）：1717 巴黎出生（弃婴）→ 1729 马萨林学院 → 1738 律师 → 1741 巴黎科学院 → 1743 动力学论 → 1747 弦振动 → 1754 法兰西学院 → 1783 去世
4. **早年与弃婴身世**（`\earlyslide`）：私生子、圣让勒隆教堂、养母 Rousseau 家、养母名言
5. **波动方程**（核心贡献页，表格 + 公式框）：1747 弦振动、达朗贝尔公式、达朗贝尔算子
6. **达朗贝尔原理**（核心贡献页，表格 + 公式框）：1743《动力学论》、虚功
7. **比值审敛法与代数基本定理**（核心贡献页，表格 + 公式框）：达朗贝尔-高斯定理
8. **达朗贝尔佯谬**（核心贡献页，表格 + 公式框）：1752 无粘流阻力为零
9. **天体力学**（核心贡献页，表格 + 公式框）：三体问题、岁差
10. **百科全书**（特色页，表格）：与狄德罗合编、1000+ 条目、《绪论》
11. **音乐理论：拉莫之争**（特色页，表格）：1749 评论、1752《Élémens》、争论
12. **哲学转向**（特色页，表格）：从唯物主义到怀疑主义、贝克莱、康德先声
13. **更多贡献**（表格）：拉丁学养、塔西佗翻译、沙龙、腓特烈大帝
14. **荣誉与传承**（表格）：法兰西学院常任秘书、皇家学会外籍院士、达朗贝尔-高斯定理
15. **终章**：65 岁、"启蒙时代理性组织者"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **身世**：私生子（natural son），不是普通家庭——必须按 Wikipedia 准确表述（母亲 Tencin、父亲 Destouches、弃婴于 Saint-Jean-le-Rond 教堂、养母 Rousseau）。勿用"出生卑微"等含蓄表述。
- **原名**：原名 Jean-Baptiste Daremberg，后改 d'Alembert——需准确表述（不要写成"出生即名 d'Alembert"）。
- **导师关系**：以自学为主；metadata 标注 doctoral_advisor Léonor Caron，但未受现代博士培养——勿写"师从 Caron"。与 Maupertuis、Clairaut、Euler、Daniel Bernoulli 通信合作需明确（不是"在……指导下"）。
- **早年生平时间线**：1729（12 岁）马萨林学院（不是 13 岁或 11 岁，需精确）；1735 学士；1738 律师——精确年代。
- **波动方程 vs 弦振动论文**：1747 年发表弦振动论文建立波动方程；这是他的"著名成就之一"，勿写"发明"（牛顿/惠更斯已有相关工作）。
- **达朗贝尔原理 vs 达朗贝尔佯谬**：两者都是"达朗贝尔"——前者是 1743 动力学定律的虚功形式，后者是 1752 流体力学悖论。不可混淆。
- **代数基本定理**：1746 给出证明（有缺陷），Gauss 1799 给出严格证明。法国称"达朗贝尔-高斯定理"——勿写"达朗伯特定理"（他证明不严格）。
- **百科全书**：与 Diderot 合编 1000+ 条目；1754 法兰西学院院士，1772-04-09 任常任秘书（permanent secretary）——勿写"主编百科全书"（他是联合主编之一，且百科全书的发起与策划是 Diderot）。
- **晚年与 Julie de Lespinasse**：他与她同住（不是"结婚"——Wikipedia 写"took up residence with her"），不结婚。Julie 是沙龙女主人、Lespinasse 侯爵夫人的侄女。
- **死亡**：1783-10-29，膀胱疾病；无标记普通墓（作为知名无神论者）——勿写"去世时"逸事（Wikipedia 无具体临终场景）。
- **Croix ou Pile 错误**：d'Alembert 错误地认为抛硬币正面概率因反面出现而增加（赌徒谬误）——这是 d'Alembert system（一种 martingale 策略）的来源。Wikipedia 明确说"This is famously known for being incorrect"——需表述为"达朗贝尔的著名错误"。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q153232 | 待写入 |
| name_zh | 达朗贝尔（或 达朗伯） | 待写入 |
| name_en | Jean le Rond d'Alembert | 待写入 |
| birth_date | 1717-11-16 | 待写入 |
| death_date | 1783-10-29 | 待写入 |
| nationality | France / Kingdom of France | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | analysis, mechanics, celestial mechanics, philosophy, music theory | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **博士导师**（metadata）：Léonor Caron（巴黎学院，弃婴 / 早年教育相关）
- **学生**：Pierre-Simon de Laplace（拉普拉斯，重要）
- **合作/通信**：Denis Diderot（狄德罗，《百科全书》联合主编）、Jean le Rond d'Alembert 与 Euler、Clairaut、Maupertuis、Daniel Bernoulli 通信
- **同时代**：Rousseau（卢梭，关于音乐）、Voltaire（伏尔泰，日内瓦文章相关）、Frederick the Great（腓特烈大帝，普鲁士科学院庇护）、Catherine the Great（叶卡捷琳娜大帝，俄罗斯科学院庇护）
- **沙龙**：Geoffrin 夫人、Du Deffand 侯爵夫人、Lespinasse（女主人，伴侣）
- **父母**：Claudine Guérin de Tencin（母，作家）、chevalier Louis-Camus Destouches（父，炮兵军官）
- **资助/庇护**：Berlin Academy（1746 外籍院士）、Académie Royale des Sciences（1741 院士）、Royal Society（1748 ForMemRS）、Académie Française（1754 院士、1772 常任秘书）、American Academy of Arts and Sciences（1781 外籍荣誉院士）

## 8. 奖项清单

- Fellow of the Royal Society（皇家学会外籍院士，ForMemRS，1748）
- 柏林科学院外籍院士（1746）
- 巴黎科学院院士（1741）
- 法兰西学院院士（1754），常任秘书（1772-04-09）
- 美国文理科学院外籍荣誉院士（1781）
- Prenom 命名："达朗贝尔"被腓特烈大帝提议命名金星卫星（被 d'Alembert 婉拒）

## 9. 机构清单

- 教育：Collège des Quatre-Nations / Collège Mazarin（马萨林学院，巴黎）、University of Paris（巴黎大学）
- 任职：Académie Royale des Sciences（巴黎科学院，1741 院士）、Académie des Sciences de Berlin（柏林科学院，1746）、Académie Française（法兰西学院，1754 院士，1772 常任秘书）

## 10. 终审清单

- [x] 生卒 1717-11-16 / 1783-10-29，享年 65，出生地巴黎（弃婴于 Saint-Jean-le-Rond 教堂）
- [x] 国籍用「法国」现代对应，并注明常居巴黎（百科全书派活跃地）
- [x] 身世"私生子/弃婴"表述准确（母 Tencin + 父 Destouches + 养母 Rousseau）
- [x] 波动方程 1747 / 达朗贝尔原理 1743 / 佯谬 1752 时代准确
- [x] 比值审敛法 / 达朗贝尔-高斯定理 / 达朗贝尔算子术语精确
- [x] 百科全书"与 Diderot 合编、1000+ 条目"表述准确（非独立主编）
- [x] 哲学"从唯物主义到怀疑主义/贝克莱/康德先声"表述准确
- [x] Croix ou Pile 错误表述为"达朗贝尔的著名错误"
- [x] 配偶"Julie de Lespinasse 同住"表述准确（未婚）
- [x] 正文采用 Euler 模板：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [x] **结合本地 Wikipedia**：读取 `pages/Jean_le_Rond_d'Alembert/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [x] **头像**：使用 Catherine Lusurier 1777 肖像（`images/dalembert_portrait.jpg`，500×618，标准 JPEG 无 Exif）
- [x] **国籍**：封面顶部徽章明示 France
- [x] **引语核对**：引语必须在 Wikipedia 原文找到（如养母"哲学家/蠢驴"名言、"physical promotion, innate ideas and the vortices"、Baudin 命名等）
- [x] **编译验证**：`make distclean && make`
- [x] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Euler 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Euler / Lagrange / Laplace）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
