# Felix Klein（费利克斯·克莱因）立传提示词

> qid=Q76641 · 1849-04-25 – 1925-06-22 · 德国数学家、数学教育家、数学史家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Felix_Klein/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=erlangengold!50` 细边框 + 姓名小字注（采用 `images/portrait.jpg`，即 Max Liebermann 1912 年竖版画像）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「群轨道 / 曲面」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Felix Christian Klein（中文惯称：克莱因）
- **生卒**：1849-04-25 生于杜塞尔多夫（普鲁士莱茵省）→ 1925-06-22 逝于哥廷根，享年 76
- **国籍**：Kingdom of Prussia（普鲁士王国）/ German Empire（德意志帝国）/ Weimar Republic（魏玛共和国），现代对应「德国」
- **身份**：数学家、数学教育家、数学史家（埃尔朗根纲领作者）
- **家庭**：父 Caspar Klein（1809–1889，普鲁士政府官员秘书）；母 Sophie Elise Klein（1819–1890，娘家姓 Kayser）；1875 年娶 Anne Hegel（哲学家黑格尔孙女）
- **教育轨迹**：
  - 杜塞尔多夫 Gymnasium
  - 1865–1866 波恩大学（本想成为物理学家，师从 Plücker）
  - 1866 成为 Plücker 助手（Plücker 兴趣已转向线几何）
  - 1868 年获波恩大学博士（导师 Plücker；Rudolf Lipschitz 亦为博士导师）
- **任职轨迹**：
  - 1868 年 Plücker 去世后完成其线几何著作下卷，结识 Clebsch
  - 1870 普法战争：被迫离巴黎，短暂任普鲁士军队医护兵
  - 1871 哥廷根 Privatdozent（编外讲师）
  - **1872 埃尔朗根教授（仅 23 岁，Clebsch 力荐）**
  - 1875 慕尼黑工业学院（与 Brill 合教）
  - **1880–1886 莱比锡教授**（1882 健康崩溃，抑郁两年）
  - **1886–1913 哥廷根教授**（重建数学中心，1913 退休）
- **导师**：Julius Plücker（博士导师）、Rudolf Lipschitz（博士导师）
- **研究领域**：群论、几何、复分析、非欧几何、代数方程、数学教育、数学史

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **埃尔朗根纲领（1872，23 岁）**：就职演讲《近代几何学研究的比较考察》提出"几何 = 群 + 不变量"——用对称群分类全部几何学，是几何学最重要的统一纲领（注意：纲领思想受 Helmholtz、Cayley 启发，群概念来自 Sophus Lie 与 Camille Jordan 的影响）。
2. **非欧几何的捍卫者（1871）**：两篇"论所谓的非欧几何"论文证明欧氏与非欧几何都可看作 Cayley–Klein 度量决定的度量空间，得出「非欧几何一致 ⟺ 欧氏几何一致」，终结平行公理千年争论（Cayley 至死不接受，认为循环论证）。
3. **克莱因瓶（Klein bottle）**：不可定向、无边界的闭曲面，不能嵌入 R³（必自交），可嵌入 R⁴；由两个 Möbius 带粘合；原名 "Kleinsche Fläche"（Klein 曲面），英译时 "Fläche" 误作 "Flasche"（瓶）。
4. **Beltrami–Klein 模型**：非欧几何的射影模型（单位圆盘内弦为直线），与 Poincaré 圆盘模型并列。
5. **自守函数与 Poincaré 的竞争（1881–82）**：与 Poincaré 友好竞争自守函数与统一化定理；1882-03-23 凌晨 2:30 哮喘发作中完成统一化定理证明策略。
6. **正二十面体与五次方程（1884）**：《正二十面体讲义》用二十面体群（A₅）给出五次方程的超越解法，将代数、几何、群论编织在一起。
7. **Klein 四次曲面（Klein quartic，1879）**：PSL(2,7)（168 阶）作用下的 Riemann 面，方程 x³y + y³z + z³x = 0，对称群恰为 PSL(2,7)。
8. **Klein 群 / Klein 四元群**：分式线性变换的离散群（复分析/双曲几何核心，Poincaré 独立发现）；V₄ 群论基本对象。
9. **重建哥廷根（1886–1913）**：创办数学阅览室、周讨论班，1895 年招募 Hilbert，1915 年与 Hilbert 邀 Noether；1893 起收女生，Grace Chisholm Young 是哥廷根第一位女性数学博士。
10. **数学教育改革**：1905 Meran 方案（中学引入解析几何、微积分基础、函数概念）；1908 当选 ICMI 首任主席；《从高观点看初等数学》（1908）。
11. **《数学科学百科全书》**：1894 发起编纂，持续到 1935，20 世纪数学总览；主编《Mathematische Annalen》使其成为世界顶级期刊。
12. **荣誉**：1885 皇家学会外籍会员、1893 De Morgan Medal、1912 Copley Medal、1914 Ackermann–Teubner Memorial Award、Pour le Mérite、Bavarian Maximilian Order。
13. **一战争议**：1914 年《93 人宣言》签名者（支持德国入侵比利时）——客观记录，不做价值渲染。
14. **健康危机**：1882 年莱比锡时期健康崩溃、抑郁两年，此后研究重心转向应用与教育。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（哥廷根蓝） | `#1E4E79` | 哥廷根数学中心 |
| 强调色（纲领金） | `#C4A24C` | 埃尔朗根纲领 / 尊崇 |
| 分类色 1（群论/几何 — 靛蓝） | `#1B4A6B` | 埃尔朗根纲领 / 群作用 |
| 分类色 2（拓扑 — 青绿） | `#2D7A6A` | 克莱因瓶 / 非欧几何 |
| 分类色 3（复分析 — 紫罗兰） | `#5A3E85` | 自守函数 / 模函数 |
| 分类色 4（教育/遗产 — 石版灰） | `#4A5568` | 教育改革 / 哥廷根传承 |
| 背景 | `#F7F6F3` | 米白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「群轨道 / 曲面铺砌」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

- **风格定调**：**古典庄严 / 沉稳理性**（"哥廷根的建筑师"的庄重与统筹全局的视野）
- **匹配理由**：
  - 克莱因是 19 世纪末德国数学的"组织者"与"统一者"——需**庄严、沉稳、宏大**的配乐
  - "庄严" 匹配其重建哥廷根、编纂百科全书的学术地位
  - "沉稳" 匹配其跨越研究、教育、行政的统筹气质
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄严风格）：
  - 首选：古典 / 庄严 / 沉稳风格曲目
  - 备选：纪录片风沉稳曲目（呼应其教育改革的传承使命）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构 + 表格 + 公式框）

> 正文版式对齐高斯模板：核心贡献页采用 `tabularx` 表格（`m{3.4cm}|X|p{3.0cm}`）+ `\fcolorbox` 公式框；生平页采用 `p{2.2cm}|X|p{3.0cm}` 表格；第 3 页为「时间线页」。

1. **封面**（`\titleslide`）：大标题「费利克斯·克莱因」+ 副题「埃尔朗根纲领 · 克莱因瓶 · 哥廷根重建者」+ 1849–1925 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **克莱因的一生：时间线**（`\timelineslide`）：1849 出生 → 1868 博士 → 1872 埃尔朗根纲领 → 1886 哥廷根 → 1895 招 Hilbert → 1908 ICMI → 1925 去世
4. **早年与教育**（1849–1872，表格）：杜塞尔多夫出生、牧师之家、波恩大学、Plücker 助手、1868 博士、普法战争医护兵
5. **埃尔朗根纲领**（核心贡献页，表格 + 几何=群+不变量公式框）：1872 就职演讲、群论统一几何
6. **非欧几何与 Klein 模型**（核心贡献页，表格 + Cayley–Klein 度量公式框）：1871 两篇论文、Beltrami–Klein 模型
7. **克莱因瓶与拓扑**（核心贡献页，表格 + Klein quartic 公式框）：不可定向曲面、Klein 四次曲面 x³y+y³z+z³x=0
8. **自守函数与五次方程**（核心贡献页，表格 + 统一化定理公式框）：与 Poincaré 竞争、正二十面体解五次方程
9. **重建哥廷根**（表格）：1895 招 Hilbert、1915 邀 Noether、女性博士
10. **数学教育改革**（表格）：1905 Meran 方案、1908 ICMI 首任主席
11. **荣誉、晚年与遗产**（表格）：De Morgan/Copley Medal、百科全书、一战《93 人宣言》
12. **终章**：76 岁、埃尔朗根纲领的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **《93 人宣言》**：Klein 是 93 位签名者之一（支持德国入侵比利时）——**客观记录事实**，不做价值渲染。
- **埃尔朗根纲领归属**：Klein 1872 提出，**纲领思想受 Helmholtz 与 Cayley 启发，群概念来自 Sophus Lie 与 Camille Jordan 的影响**——不写 Klein 完全独创。
- **Klein 群**：Poincaré 独立发现（1879–81），两人通信后合作命名——**不是 Klein 独占**。
- **克莱因瓶**：1882 提出；不可定向，**嵌入仅 R⁴**（R³ 中必自交）；原名 "Kleinsche Fläche"，英译误作 "Flasche"。
- **Cayley 的态度**：Cayley 至死不接受 Klein 的非欧几何论证（认为循环论证）——历史站在 Klein 一边，但需客观表述。
- **哥廷根重建时间线**：1886–1913 黄金期；Hilbert 是 Klein **1895 年**招募；Noether **1915 年**受邀——时间线精确。
- **Grace Chisholm Young**：哥廷根第一位女性数学博士（1896，Klein 指导，她原是 Cayley 的学生）——重要细节。
- **统一化定理**：Klein 1882-03-23 凌晨 2:30 哮喘发作中完成证明**策略**（表述为"完成证明策略/纲领"，勿过度戏剧化为"一夜证毕"）。
- **生卒核对**：1849-04-25 / 1925-06-22，享年 76，metadata 与正文一致。
- **博士导师**：metadata `doctoral_advisor` 含 Julius Plücker 与 Rudolf Lipschitz 两人；Wikipedia 正文明确"supervised by Plücker"——正文写"Plücker 指导"，Lipschitz 列为共同导师，勿混淆。
- **国籍**：生卒横跨普鲁士王国、德意志帝国、魏玛共和国，封面用「德国」现代对应。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76641 | 待写入 |
| name_zh | 费利克斯·克莱因（或 克莱因） | 待写入 |
| name_en | Felix Klein | 待写入 |
| birth_date | 1849-04-25 | 待写入 |
| death_date | 1925-06-22 | 待写入 |
| nationality | Germany（Kingdom of Prussia / German Empire） | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | group theory / geometry / complex analysis / function theory / education | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **博士导师**：Julius Plücker、Rudolf Lipschitz
- **学术提携人**：Alfred Clebsch（结识/力荐，哥廷根访问赏识）
- **群论引路人**：Sophus Lie（介绍群概念）、Camille Jordan（影响）
- **合作者**：Alexander von Brill（慕尼黑合教）、Robert Fricke（自守函数四卷本合著）、Arnold Sommerfeld（陀螺仪理论合著）、Eduard Study（莱比锡同事）、Friedrich Engel（莱比锡同事）
- **学生（代表性）**：Adolf Hurwitz、Ludwig Bieberbach、Ferdinand von Lindemann、Alexander Ostrowski、Grace Chisholm Young（第一位女性博士）、Maxime Bôcher、Frank Nelson Cole、Philipp Furtwängler、Walther von Dyck、Robert Fricke、Carl Runge、Oskar Bolza、Axel Harnack 等
- **被招募者 / 同事**：David Hilbert（1895 招募）、Emmy Noether（1915 邀）
- **竞争 / 学术**：Henri Poincaré（自守函数/统一化定理竞争）、Arthur Cayley（非欧几何论证分歧）
- **家族**：妻 Anne Hegel（哲学家黑格尔孙女）

## 8. 奖项清单

- Foreign Member of the Royal Society（1885）
- De Morgan Medal（1893，伦敦数学会）
- Copley Medal（1912，皇家学会）
- Ackermann–Teubner Memorial Award（1914）
- Pour le Mérite for Sciences and Arts（科学与艺术功勋勋章）
- Bavarian Maximilian Order for Science and Art（巴伐利亚马克西米利安科学与艺术勋章）

## 9. 机构清单

- 教育：University of Bonn（博士）、Humboldt-Universität zu Berlin、Görres-Gymnasium Düsseldorf
- 任职：University of Erlangen（1872）、Technische Hochschule München（1875–1880）、Universität Leipzig（1880–1886）、University of Göttingen（1871 Privatdozent；1886–1913 正教授）

## 10. 终审清单

- [ ] 生卒 1849-04-25 / 1925-06-22，享年 76，出生地杜塞尔多夫
- [ ] 埃尔朗根纲领"受 Helmholtz/Cayley 启发、群概念来自 Lie/Jordan"表述准确
- [ ] Klein 群"Poincaré 独立发现"表述准确
- [ ] 克莱因瓶"不可定向、嵌入 R⁴、R³ 必自交"表述准确
- [ ] Cayley 不接受非欧几何论证（循环）表述准确
- [ ] 哥廷根时间线精确（1895 Hilbert、1915 Noether）
- [ ] Grace Chisholm Young 第一位女性博士
- [ ] 《93 人宣言》客观记录
- [ ] 统一化定理"证明策略"措辞准确（不戏剧化）
- [ ] 博士导师 Plücker 指导、Lipschitz 共同导师
- [ ] 国籍用「德国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Felix_Klein/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：采用 `images/portrait.jpg`（Max Liebermann 1912 竖版画像）
- [ ] **国籍**：封面顶部徽章明示德国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到，否则忠实转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Gauss / Riemann / Frobenius）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
