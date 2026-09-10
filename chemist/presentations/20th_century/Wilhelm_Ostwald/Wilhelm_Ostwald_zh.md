# Wilhelm Ostwald（威廉·奥斯特瓦尔德）立传提示词

> qid=Q12658 · 1853-09-02 – 1932-04-04 · 波罗的海德意志化学家/哲学家 · 20 世纪 · 诺贝尔化学奖（1909）
> 官方理由（总名单措辞照抄）：表彰他在催化方面的工作，以及他对支配化学平衡和反应速率基本原理的研究
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Wilhelm_Ostwald/`（page.md + metadata.json + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**（`mathematician/presentations/19th_century/Carl_Friedrich_Gauss/Carl_Friedrich_Gauss_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像执行阶段下载，见 §11 Review-1 头像指引）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 物理化学的奠基者\enspace·\enspace 波罗的海德意志`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「体系化 / 统一」母题——圆点大小错落暗示能量转化、催化加速与 Ostwald 色立体（双锥）的几何。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Wilhelm Friedrich Ostwald（中文惯称：威廉·奥斯特瓦尔德；1899 年获萨克森国王授予 Geheimrat 枢密顾问头衔）
- **生卒**：1853-09-02（俄历 O.S. 8 月 21 日）生于俄罗斯帝国利沃尼亚省里加（今拉脱维亚）→ 1932-04-04 逝于莱比锡一家医院，享年 78；安葬于 Großbothen 乡间庄园
- **国籍**：Baltic German（波罗的海德意志人；生于俄国帝国，1887 年起定居德国莱比锡直至去世；总名单标注 "German, born in Latvia"）
- **身份**：化学家、哲学家（polymath 博物学家；物理化学奠基人之一；亦是画家、作家、国际语运动者、社会学家）
- **家庭**：父亲 Gottfried Wilhelm Ostwald 为箍桶匠（master-cooper），母亲 Elisabeth Leuckel；三兄弟中的老二（兄 Eugen、弟 Gottfried）；幼年即痴迷科学，在家做烟花与摄影实验。1880-04-24 娶 Helene von Reyher（1854–1946），育有五子女：Grete（1882–1960）、Wolfgang（1883–1943，后成胶体化学知名科学家）、Elisabeth（1884–1968）、Walter（1886–1958）、Carl Otto（1890–1958）
- **教育轨迹**：里加文理中学（Riga State Gymnasium No.1，见 metadata.json）→ 1872 入 Imperial University of Dorpat（今爱沙尼亚塔尔图大学）→ 1875 通过 Kandidatenschrift 考试 → 1877 获 Magisterial 学位（取得授课资格）→ 1878 博士论文
- **导师**：博士导师 Carl Schmidt（Dorpat 化学实验室；同时期同侪 Johann Lemberg 教会其无机分析、平衡与反应速率测量基础）；另在大学物理研究所随 Arthur von Oettingen 学习（metadata.json 将 Oettingen 并列导师）
- **博士论文**：1878 年于 Dorpat 发表，题为 *Volumchemische und Optisch-Chemische Studies*（容量化学与光化学研究）
- **研究领域**：物理化学（催化、化学平衡、反应速率、电化学、稀释理论、结晶/多晶型）；晚年转向色彩学、哲学（唯能论、一元论）、国际语言（Esperanto→Ido）与社会改革

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **里加箍桶匠之子（1853）**：波罗的海德意志家庭、手工业者的作坊——幼年烟花与摄影实验，是动手化学的起点。
2. **Dorpat 岁月（1872–1881）**：Carl Schmidt 实验室的无薪研究者，从 Lemberg 学得平衡与速率的测量之术；1878 博士论文《容量化学与光化学研究》。
3. **亲和力三维表**：早期核心问题是化学亲和力——他造出兼顾温度与酸碱亲和力常数的三维亲和力表，并研究质量作用、电化学与化学动力学。
4. **Riga 教授（1881）→ Leipzig 首席（1887）**：1881 任 Riga Polytechnicum 化学教授；1887 转任莱比锡大学，成为**世界上第一位专设的物理化学教授**，任职至 1906 退休。
5. **稀释定律（Ostwald's dilution law）**：弱电解质行为遵循质量作用原理，在无限稀释时充分解离——可用电化学方法实验观测。
6. **催化的现代定义**：承接 Berzelius 首创的催化概念，Ostwald 明确：催化剂是**不成为反应物或产物的一部分、却能加速反应速率**的物质；广泛应用于酶催化与工业过程。
7. **硝酸工艺（Ostwald process）**：氨氧化制硝酸、用催化剂并给出近理论极限产率的条件，获专利；恰逢 Haber–Bosch 合成氨（1911 或 1913 完成）提供廉价氨，二者结合造就化肥与炸药的大规模生产（一战德国短缺物资）。此工艺至今仍广泛使用。
8. **结晶三定律**：Ostwald's rule（固体未必结晶成最热力学稳定相，相对速率取决于表面张力）；Ostwald ripening（溶液随时间演化、大晶体吞小晶体——冰淇淋变糙是日常例）；Ostwald–Freundlich equation（溶解度随晶粒尺寸变化，1900 首次发表、1909 由 Freundlich 精化）。与 Liesegang 合作解释周期性结晶（Liesegang rings）。
9. **mole 一词与原子论之争**：约 1900 年 Ostwald 把 "mole" 引入化学词汇（分子量以克计、联系理想气体）；讽刺的是这正是他**唯能论反对原子论**的产物——他与 Ernst Mach 是原子论最后两位坚守者，后在与 Sommerfeld 的谈话中自陈被 **Jean Perrin 的布朗运动实验**说服。
10. **创刊与建制（1887–1911）**：1887 创刊 *Zeitschrift für Physikalische Chemie*（任主编至 1922）；1894 创德国电化学学会（后成德国 Bunsen 学会）；1889 创 *Klassiker der exakten Wissenschaften*（已出 250+ 卷）；1902 创 *Annalen der Naturphilosophie*（1921 年首次德文刊出维特根斯坦《逻辑哲学论》）；1927 创 *Die Farbe*；1911 参与创建 Die Brücke 研究所（诺贝尔奖金资助）并任国际化学学会联合会首任主席。
11. **门生济济**：实验室走出未来诺奖得主 Svante Arrhenius、Jacobus van 't Hoff、Walther Nernst（正文称 research students），以及 Arthur Noyes、Willis Rodney Whitney、池田菊苗（Kikunae Ikeda）；infobox 博士学生另有 Paul Walden、Georg Bredig、Frederick G. Donnan 等。1901 年 Einstein 曾来求职被拒——后来 Ostwald 两度（1910、1913）提名爱因斯坦诺贝尔奖。
12. **1909 诺贝尔化学奖**：官方理由 "his scientific contributions to the fields of catalysis, chemical equilibria and reaction velocities"；此前自 1904 起被提名 20 次；获奖后将奖金一半捐给 Ido 国际语运动。
13. **退休后的第二人生（1906–1932）**：转向哲学、政治、艺术——色彩体系（双锥色立体、*The Color Primer*/*The Color Atlas* 1916–8，影响 Mondrian、De Stijl、Klee 与包豪斯）；留下逾 1000 幅油画与 3000 幅色粉/色彩习作；投身 Berta von Suttner 的和平运动；庄园区取名 "Landhaus Energie"（能量之屋）——毕生体系化与「不浪费能量」伦理的注脚。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青蓝 deepcyan） | `#17435B` | 物理化学的精密与度量（表头 / 公式文本） |
| 强调色（诺贝尔金，OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（催化与工业 badgeCat） | `#A84B2A` | 赭红催化定义 / 硝酸工艺 |
| 分类色 2（稀释与电化学 badgeDil） | `#1E6E8C` | 青蓝稀释定律 / 电导测量 |
| 分类色 3（结晶与规则 badgeCry） | `#4C5F8F` | 灰蓝 Ostwald 规则 / 熟化 / Freundlich 方程 |
| 分类色 4（色彩与体系 badgeCol） | `#8A1F3D` | 绛红色立体 / 唯能论 / 一元论 |
| 背景 | `#F6F7F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「体系化 / 统一」——由小及大的圆点暗示 Ostwald 熟化与能量的转化。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`）
- **风格**：宏大 / 深远 / 长期影响
- **匹配理由**：
  - "宏大 / 深远" 匹配 Ostwald 的 polymath 气质——从催化到唯能论到色彩学到国际语，一生都在做「体系化与统一」的宏大工程
  - "长期影响" 匹配其遗产——物理化学建制（期刊、学会、教材）延续至今，硝酸工艺至今广泛使用
  - 相比 heroic/epic 的征服感，Eternals 的沉稳深远更贴合「奠基者而非征服者」的定位
- **时长**：`make video` 时 ffmpeg `-shortest` 自动对齐；**wav 复制在执行立传阶段进行**（`cp` 到本目录，勿现在复制）。

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 物理化学的奠基者 / Wilhelm Ostwald 1853–1932 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  奥斯特瓦尔德的一生 — 高斯式时间线（10 节点：1853 里加出生→1872 入 Dorpat→1878 博士论文→1881 Riga 教授→1887 Leipzig+创刊→1900 mole 一词→1906 退休→1909 诺贝尔奖→1911 Die Brücke/一元论会主席→1932 去世）
04  早年：里加箍桶匠之子 (1853–1872) — 表格「时间|事件|结果」
05  Dorpat：亲和力与测量之术 (1872–1881) — 表格「时间|事件|结果」
06  Riga→Leipzig：物理化学奠基 (1881–1906) — 表格「问题|方法|结果」+ 公式框：稀释定律 K = cα²/(1−α)（见 §5 公式注记）
07  催化：从 Berzelius 到现代定义 — 表格「概念|内容|结果」
08  硝酸工艺 (Ostwald process) — 表格「问题|方法|结果」+ 公式框：NH₃ 催化氧化制 HNO₃（见 §5 公式注记）
09  结晶世界：规则·熟化·Freundlich 方程 — 表格「现象|解释|命名」+ 公式框：Ostwald–Freundlich 方程（尺寸—溶解度）
10  mole 与原子论之争 — 表格「立场|论据|转折」（唯能论 vs 原子论；Perrin 布朗运动说服）+ 公式框：mole 定义 n = m/M
11  建制者：期刊·学会·Die Brücke — 高斯「类别|代表|意义」表格（1887/1889/1894/1902/1911/1927 六件套）
12  第二人生：色彩学与艺术 (1906–1932) — 双锥色立体示意 + Mondrian/Klee/包豪斯影响 + Ido 运动
13  荣誉与纪念 — 表格「类别|代表|意义」（Nobel 1909 / Faraday 1904 / Exner 1923 / Geheimrat 1899 / 月球背面 Ostwald 环形山 / Grimma 博物馆）
14  结尾 — 「不浪费能量，而把它转化为最有用的形式。」（page.md 实载伦理观）+ 品牌 OpenMathAI
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 生卒双重历法 | 1853-09-02（公历 N.S.；俄历 O.S. 8 月 21 日）；metadata.json 两值并列（1853-08-21 / 1853-09-02），**以 page.md 公历 1853-09-02 为准**，O.S. 仅作括注 |
| 去世地冲突 | metadata.json place_of_death 给 Großbothen/Grimma；page.md 明文 **died in a hospital in Leipzig**、葬于 Großbothen 庄园——以 page.md 为准：去世地莱比锡、安葬地 Großbothen（**page.md 与 metadata 冲突点，已在 §7/§6 同步**） |
| 国籍表述 | page.md 称 Baltic German（波罗的海德意志人），生于俄国帝国里加（今拉脱维亚）；总名单 "German, born in Latvia" 可作底注；**勿单写"德国籍"**，也勿写"拉脱维亚人"（他是德意志族裔） |
| 博士导师 | page.md 明文博士论文导师 **Carl Schmidt**；Oettingen 是物理研究所学习经历（metadata.json 将二人并列 doctoral_advisor）——入库以 Carl Schmidt 为博士导师、Oettingen 以 "物理研究所指导" 单独注明 |
| 诺奖理由措辞 | 中文照抄总名单「表彰他在催化方面的工作，以及他对支配化学平衡和反应速率基本原理的研究」；page.md 另有两处英文表述（catalysis/chemical equilibria/reaction velocities），**1909 独享、无共享者** |
| 催化概念史 | 催化概念**由 Berzelius 首创**（page.md：the concept of chemical catalysis first articulated by Berzelius）；Ostwald 之功是给出**催化剂的现代定义**——勿写"发明/发现催化" |
| 硝酸工艺归属 | 氨氧化制硝酸的基本工艺 **64 年前已被 Kuhlmann 专利**（因无廉价氨未工业化）；Ostwald 之功在催化剂 + 近理论极限产率条件 + 借 Haber–Bosch 廉价氨实现工业规模——勿写"首创硝酸工艺" |
| 原子论之争 | Ostwald 与 Ernst Mach 是**原子论最后两位反对者**（唯能论）；被说服的依据是 **Perrin 的布朗运动实验**（对 Sommerfeld 的谈话中自陈，page.md 有载可写）；勿写" Ostwald 发现原子"或淡化其反对立场 |
| mole 的来历 | "mole" 一词约 1900 由 Ostwald 引入，且**与他的唯能论直接相关**（联系理想气体）——勿把 mole 概念写成"原子论的胜利成果" |
| 三位诺奖"学生" | 正文称 Arrhenius、van 't Hoff、Nernst 曾是其 **research students**（未来诺奖得主）——非 infobox 博士学生；入库归 colleague/other 并注明，**勿冒填 advisor-student** |
| Einstein 轶事 | 1901 Ostwald **拒绝** Einstein 求职申请；后于 1910、1913 两度提名爱因斯坦诺奖——勿写"Ostwald 是爱因斯坦的导师/伯乐第一人"之类戏剧化因果 |
| 奖金捐赠数据张力 | 一处写捐出 1909 奖金**一半**给 Ido 运动（资助 *Progreso* 杂志），另一处写捐出**逾 40,000 美元**——两处皆 page.md 实载，引用时任取其一并保留原文口径，勿自行换算合并 |
| 色彩学年份 | *Malerbriefe* 1904（**退休前**）；*Die Farbenfibel*/*The Color Primer* 1916、*The Color Atlas* 1916–8——勿把全部色彩学著作归入 1906 退休后 |
| 一元论与优生学 | page.md 载 Ostwald 任 Deutscher Monistenbund 主席（1911）、一元论者倡导自愿优生/安乐死并间接便利后来的社会达尔文主义——**敏感历史评价，建议 Beamer 略过**；如必须提及须完整保留"自愿选择、防止痛苦"语境并注明"Ostwald 死于纳粹政策之前" |
| 公式框注记 | 稀释定律 K=cα²/(1−α)、NH₃ 氧化方程、Ostwald–Freundlich 方程、n=m/M 均为该命名定律/定义的**通用教科书数学形式**；page.md 仅定性描述——公式可上片，但正文叙述须以 page.md 定性文字为准，不得添加 page.md 无载的推导细节 |
| 机构雇主 | metadata.json employer 含 MIT；正文只有 **Harvard 首任交换教授（1904–1905）**——MIT 无载禁写 |
| 引语纪律 | 可引原话仅限 page.md 实载："Poetry, music and painting have given me refreshment and new courage…"（Ostwald 署名引语）、"coping with the infinite diversity of appearances through the formation of appropriate concepts"、science builds "intellectual ideas; art constructs visual ones"、"not waste energy, but convert it into its most useful form"（伦理观）。其余一律间接转述，不得加引号 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q12658 | ✅ |
| name_zh | 威廉·奥斯特瓦尔德 | ✅ |
| name_en | Wilhelm Ostwald | ✅ |
| birth_date | 1853-09-02（公历；O.S. 1853-08-21 仅注） | ✅ |
| death_date | 1932-04-04 | ✅ |
| nationality | Baltic German（俄国帝国里加出生，1887 起定居德国；总名单口径 "German, born in Latvia"） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：catalysis / chemical equilibria / reaction rates / color science / energeticism，带 rank） | ✅ |
| has_biography | 待立传后置 1 | 🔲 |

## 7. 社会关系入库清单

**师长 / 同侪 / 合作者**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Carl Schmidt | 师→生（博士导师） | Dorpat 化学实验室；1878 博士论文导师 |
| advisor-student | Arthur von Oettingen | 师→生（物理研究所指导） | metadata.json 并列导师；正文为物理研究所学习经历 |
| colleague | Johann Lemberg | 无向 | Dorpat 同侪，教其无机分析/平衡/速率测量基础 |
| colleague | Svante Arrhenius | 无向 | 正文称 research student、物理化学共同奠基人；非 infobox 博士学生 |
| colleague | Jacobus Henricus van 't Hoff | 无向 | 物理化学共同奠基人（与 Nernst 并列）；与 Ostwald 有合影存世 |
| colleague | Walther Nernst | 无向 | 物理化学共同奠基人 |
| colleague | Raphael E. Liesegang | 无向 | 合作解释周期性结晶（Liesegang rings） |
| other | Herbert Freundlich | 无向 | 1909 精化 Ostwald–Freundlich 方程 |
| other | Albert Einstein | 无向 | 1901 拒其求职申请；1910/1913 两度提名其诺奖 |
| other | Ernst Haeckel | 无向 | 一元论学会（Deutscher Monistenbund）创始者，Ostwald 1911 任主席 |

**门生（Ostwald → 学生，源自本地 Wikipedia 正文 infobox）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Arthur Amos Noyes | Ostwald → 学生 | infobox 博士学生；美国物理化学名家 |
| advisor-student | Georg Bredig | Ostwald → 学生 | infobox 博士学生 |
| advisor-student | Paul Walden | Ostwald → 学生 | infobox 博士学生 |
| advisor-student | Frederick G. Donnan | Ostwald → 学生 | infobox 博士学生（Donnan 平衡） |
| advisor-student | Louis Albrecht Kahlenberg | Ostwald → 学生 | infobox 博士学生 |
| advisor-student | James Walker | Ostwald → 学生 | infobox 博士学生 |
| advisor-student | Willis Rodney Whitney | Ostwald → 学生 | infobox 博士学生；正文亦列 |
| advisor-student | Kikunae Ikeda | Ostwald → 学生 | 正文列于 "Other students"（味之素发明者） |

> metadata.json `doctoral_student` 另含 Ejnar Hertzsprung、Alwin Mittasch、Christian Füchtbauer、George Jaffé、Max Trautz、Otto Pufahl、Colin G. Fink 等，但正文 infobox 无此数人，**不予入库**；正文 infobox 的 James Walker、Paul Walden、Kahlenberg 反不在 metadata 列表——**两源冲突时以正文 infobox 为准**。

## 8. 奖项清单

- Nobel Prize in Chemistry（1909，独享；获奖理由：催化 + 化学平衡与反应速率基本原理；诺奖讲演 *On Catalysis*，1909-12-12；自 1904 起被提名 20 次，并曾为他人提交 9 次提名）
- Faraday Lectureship Prize（1904）
- Wilhelm Exner Medal（1923，表彰其科学贡献的经济影响）
- Order of Saint Stanislaus、Albert Order（metadata.json 有载，年份无；如需引用仅列名）
- Geheimrat 枢密顾问（1899，萨克森国王授予）
- 荣誉会籍：Manchester Literary and Philosophical Society（1894）、American Academy of Arts and Sciences（1905）、美国 National Academy of Sciences（1906）、American Philosophical Society（1912）、荷兰皇家艺术与科学院外籍院士（1904）
- 荣誉博士：Aberdeen、Cambridge、Karlsruhe、Halle-Wittenberg、Toronto、Liverpool（metadata.json 有载，正文概述为"德英美多校"）

## 9. 机构清单

- 教育：Riga State Gymnasium No.1（metadata.json；正文未展开）、Imperial University of Dorpat（1872 入学；1875 Kandidatenschrift、1877 Magister、1878 博士）
- 任职：University of Dorpat（1875 起无薪研究者，1879 起 Carl Schmidt 有薪助手；~1877 起物理研究所有薪助手）、Riga Polytechnicum 化学教授（1881–1887）、Leipzig University 物理化学教授（1887–1906，世界首位专设物理化学教授）、Harvard University 首任交换教授（1904–1905）
- 命名机构：Wilhelm Ostwald Park and Museum（德国 Grimma，其度假庄园原址，藏其大量学术遗物）；Ostwald 环形山（月球背面）；退休庄园 "Landhaus Energie"（Großbothen）

## 10. 终审清单

- [ ] 生卒 1853-09-02（O.S. 08-21）/ 1932-04-04，享年 78；出生地里加、去世地莱比锡医院、安葬 Großbothen
- [ ] 1909 独享；诺奖理由中文与总名单逐字一致；催化概念归 Berzelius、现代定义归 Ostwald
- [ ] 硝酸工艺注明 Kuhlmann 64 年前专利与 Haber–Bosch 廉价氨前提；勿写"首创"
- [ ] 唯能论/原子论之争：Mach 并列最后反对者、Perrin 布朗运动为转折
- [ ] 博士导师 Carl Schmidt（Oettingen 单独注明）；三位诺奖"research students"不入 advisor-student
- [ ] 公式框四处均有 §5 公式注记；正文叙述不超出 page.md 定性范围
- [ ] 色彩学著作年份（1904 / 1916 / 1916–8）准确；一元论/优生学段落按建议略过或完整语境呈现
- [ ] 奖金捐赠口径（一半 vs 逾 40,000 美元）不自行合并
- [ ] 引语全部可在 page.md 找到原文（音乐绘画引语、科学与艺术两处、"不浪费能量"伦理观）
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Wilhelm_Ostwald/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt **无独立肖像 URL**（仅 van 't Hoff 与 Ostwald 330px 合照缩略图、诺奖证书、色立体图等）；infobox 记有 "Photograph of Ostwald c. 1913"——执行时经 Wikipedia REST API `page/summary` 查 infobox 原图文件名下载（250px→500px），或 Commons `Special:FilePath` 回退；404 则装饰圆占位。合照（Van_'t_Hoff_und_Ostwald_01.jpg）可裁右半作身份页备选，图注须写明与 van 't Hoff 合影
- [ ] **国籍**：封面顶部明示"波罗的海德意志"，底注 "German, born in Latvia" 口径
- [ ] **引语核对**：引语必须在 page.md 原文找到（§5 引语纪律所列四组）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox ≤10pt、hbox ≤50pt）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；引号半角
- [ ] 与数学家侧（高斯）及化学家侧既有格式（Sanger 标杆）对齐

---

> **名单状态**：本提示词已完成；Beamer 立传待执行。`chemist/generate_20th_century_list.py` 的 `BIOGRAPHIES_DONE` **暂不更新**（执行立传完成后再同步）。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
