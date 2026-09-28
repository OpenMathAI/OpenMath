# 物理学家立传提示词（模板标杆实例：Max Planck）

> **本文件是 OpenPhysicist 的「物理学家立传提示词模板标杆」的人物专属实例**，目标人物为 Max Planck（1918 诺贝尔物理学奖，能量量子化之父、量子理论奠基人）。
> 凡标注 `【模板通用】` 的部分可原样复用到任何物理学家；标注 `【人物专属】` 的部分需按本文件内容替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆（Hilbert / Grothendieck 的提示词 + tex 结构）与物理学家侧首例（Eugene Wigner）的实战经验。
- **本实例**：Max Karl Ernst Ludwig Planck（马克斯·普朗克）。
- **设计哲学**：物理学家立传与数学家立传的核心差异，在于**物理学家必须有「身份信息页」（Identity / Bio 速览页）**，且强调「研究领域」的结构化表达——这两点构成物理学家模板的骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Max Karl Ernst Ludwig Planck（1858-04-23 ~ 1947-10-04，享年 89 岁）
- **气质关键词**：**量子理论的奠基者、保守的革命者、德国科学的守夜人** —— 1918 诺贝尔物理学奖获奖理由（官方英文原文，禁止改写）：
  > "In recognition of the services he rendered to the advancement of Physics by his discovery of energy quanta."（因其发现能量量子而对物理学进步所作贡献）
- **设计母题**：**能量子（quantum of action）**。能量的发射不是连续之流，而是不可再分的最小单元 hν——「量子」。视觉语言可用「连续曲线在最小刻度处断裂为离散台阶」表达 1900-12-14 那次改变物理学的报告。
- **本地 Wikipedia**：`physicist/presentations/20th_century/20th_century/Max_Karl_Ernst_Ludwig_Planck/page.md`（已有全文）
  - `{Dir}.html` 与 `images/`：**待下载**（Wikipedia URL: `https://en.wikipedia.org/wiki/Max_Planck`）
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（16 页）
  - 数学家标杆：`mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- `{Dir}.html` **待下载**：`https://en.wikipedia.org/wiki/Max_Planck`（page.md 已有全文可先建立事实基准）
- 头像 **待下载**（Wikipedia infobox 照片，1938 年像；下载到 `images/`）
- 提取 infobox 与正文，事实基准如下（源自 page.md）：
  - 生卒日期（1858-04-23 生于基尔，时属荷尔斯泰因公国 ~ 1947-10-04 逝于格丁根，享年 89 岁；葬于格丁根 Stadtfriedhof）
  - 国籍（德国；出生时荷尔斯泰因属丹麦王朝治下公国，正文口径为 German theoretical physicist）
  - 父母（父 Johann Julius Wilhelm Planck，基尔与慕尼黑大学法学教授；母 Emma Patzig，父之第二任妻子；父系曾祖与祖父均为格丁根大学神学教授；家中第六子）
  - 教育（1867 迁慕尼黑入 Maximiliansgymnasium，受教于数学家 Hermann Müller——由此初识能量守恒定律，17 岁提前毕业；1874 入慕尼黑大学，在 Philipp von Jolly 指导下做过一生唯一的实验——氢经受热铂的扩散，随即转向理论物理；1877 赴柏林大学一年，听 Helmholtz、Kirchhoff、Weierstrass，自读 Clausius 著作选定热力学；1878-10 通过资格考试；1879-02 答辩博士论文《Über den zweiten Hauptsatz der mechanischen Wärmetheorie》；1880 完成教授资格论文《Gleichgewichtszustände isotroper Körper in verschiedenen Temperaturen》）
  - 博士导师（Alexander von Brill）
  - 博士后（无载；1880 慕尼黑无俸讲师 Privatdozent）
  - 主要任职机构（1880 慕尼黑 Privatdozent；1885-04 基尔大学理论物理副教授；1889 应 Helmholtz 举荐继任 Kirchhoff 柏林教席，1892 正教授，1926-01-10 退休，继任者为 Schrödinger；1907 曾获聘维也纳 Boltzmann 教席但婉拒；1909 哥伦比亚大学 Ernest Kempton Adams 讲席）
  - 关键荣誉（Nobel 物理学奖 1918 年奖、1919 年领取；Franklin Medal 1927；Lorentz Medal 1927；Copley Medal 1929；Max Planck Medal 1929（首届）；Goethe Prize 1945；Pour le Mérite 1915；皇家学会外籍会员 1926；美国哲学学会 1933 等）
  - 知名学生（博士：Max Abraham 1897、Max von Laue 1903、Moritz Schlick 1904、Walther Meissner 1906、Fritz Reiche 1907、Walter Schottky 1912、Walther Bothe 1914；其他著名学生：Lise Meitner 等；博士生总数约 20，未建立学派）
  - 家庭（1887 与 Marie Merck 结婚，育四子 Karl/Emma/Grete/Erwin，Marie 1909 去世；1911-03 与 Marga von Hösslin 再婚，1911-12 生幼子 Hermann；长子 Karl 1916 凡尔登阵亡，双胞胎女儿 Grete 1917、Emma 1919 先后死于难产；Erwin 1945-01-23 因参与 7·20 刺杀希特勒未遂案被处决）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（约 20 个节点）：1858 生于基尔 → 1864 早期记忆：普鲁士与奥地利军队开进基尔（普丹战争）→ 1867 迁慕尼黑 → 1874 入慕尼黑大学 → 1877 柏林学习年（Helmholtz/Kirchhoff/Weierstrass，自读 Clausius）→ 1879 博士论文（热力学第二定律）→ 1880 Privatdozent + 教授资格论文 → 1885 基尔副教授 → 1887 与 Marie Merck 结婚 → 1889 继任 Kirchhoff 柏林教席 → 1892 柏林正教授 → 1894 转向黑体辐射问题 → 1897《热力学教程》→ 1898 推动德国物理学会（DPG）合并成立 → 1899 「基本无序原理」导出 Wien–Planck 律、引入作用量子 h → 1900-10-19 DPG 会议提出辐射律第一版 → 1900-12-14 DPG 会议提出能量量子化假设 E=hν（量子物理诞生）→ 1901 辐射律正式发表 → 1905 力挺爱因斯坦狭义相对论并改写为作用量形式 → 1907 婉拒维也纳 Boltzmann 教席 → 1909 哥伦比亚讲席；Marie 去世 → 1911 与 Nernst 组织第一届索尔维会议；与 Marga 再婚 → 1914 促成爱因斯坦受聘柏林 → 1915 Pour le Mérite → 1918 诺贝尔奖（1919 领取）→ 1920 与 Haber 创立德国科学紧急联合会 → 1926 退休；皇家学会外籍会员 → 1929 Copley 奖章 + 首届 Max Planck Medal → 1930 出任威廉皇帝学会主席 → 1933-05 面陈希特勒为犹太科学家辩护（失败）→ 1936 威廉皇帝学会主席任期结束（纳粹施压不再连任）→ 1938 辞普鲁士科学院主席以抗议纳粹接管 → 1944-02 柏林宅邸毁于空袭（科学手稿与通信尽毁）→ 1945-01-23 Erwin 被处决 → 1947-10-04 逝于格丁根

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Max_Karl_Ernst_Ludwig_Planck/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录 `Eugene_Wigner/Makefile`，设置 `MAIN=Max_Karl_Ernst_Ludwig_Planck_zh`、`VIDEO_NAME=Max_Karl_Ernst_Ludwig_Planck_zh`

### 第 3 步：收集图片 【人物专属】

- 头像 **待下载**：优先 Wikipedia infobox 照片（1938 年 Planck 像；Commons `Special:FilePath/Max_Planck_1938.jpg?width=600`，404 则经 Wikipedia REST API 查 infobox 实际文件名）
- 可用插图（page.md 明载）：1878 年 Planck 像、1901 年 Planck 像、柏林洪堡大学「作用量子 h」纪念铭牌、1931 年 Nernst/Einstein/Planck/Millikan/Laue 五人合影、格丁根 Stadtfriedhof 墓

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

**Planck 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | theoretical physics | 理论物理 | 毕生主战场，柏林「当时唯一的理论物理学家」 | 全篇 |
| 1 | quantum theory | 量子理论 | 1900 能量量子化假设，量子物理的诞生 | 量子页 |
| 2 | thermodynamics | 热力学 | 博士论文起点，熵与不可逆过程 | 熵页 |
| 3 | black-body radiation | 黑体辐射 | 1900 辐射律的物理背景 | 辐射律页 |
| 4 | philosophy of science | 科学哲学 | 从马赫实证主义转向科学实在论 | 哲学页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Alexander von Brill | 师→生（博士导师） | 慕尼黑大学博士导师（1879 热力学第二定律论文） |
| advisor-student | Hermann von Helmholtz | 师→生（导师） | 柏林学习年导师，后成挚友并举荐其继任基尔霍夫教席 |
| advisor-student | Gustav Kirchhoff | 师→生（导师） | 柏林学习年导师；1889 Planck 继任其柏林教席 |
| advisor-student | Philipp von Jolly | 师→生（导师） | 慕尼黑导师，指导其一生唯一的实验；曾劝其勿入理论物理 |
| advisor-student | Max Abraham | 生→师（学生） | 1897 年博士，电动力学 |
| advisor-student | Max von Laue | 生→师（学生） | 1903 年博士，1914 诺奖（X 射线晶体衍射） |
| advisor-student | Moritz Schlick | 生→师（学生） | 1904 年博士，后为维也纳学派创始人 |
| advisor-student | Walther Meissner | 生→师（学生） | 1906 年博士，迈斯纳效应 |
| advisor-student | Fritz Reiche | 生→师（学生） | 1907 年博士 |
| advisor-student | Walter Schottky | 生→师（学生） | 1912 年博士，肖特基势垒 |
| advisor-student | Walther Bothe | 生→师（学生） | 1914 年博士，1954 诺奖 |
| advisor-student | Lise Meitner | 生→师（学生） | 其六学期理论物理课程听众，忆其讲课「从不看讲稿、从不出错」 |
| colleague | Albert Einstein | 无向 | 1914 促成爱因斯坦受聘柏林，挚友，常在家中合奏音乐 |
| spouse | Marie Merck | 无向 | 1887 年结婚，1909 年去世，育四子 |
| spouse | Marga von Hösslin | 无向 | 1911 年再婚，1911 年生幼子 Hermann |
| parent-child | Erwin Planck | 父→子 | 幼子（Erwin 之子），1945-01-23 因 7·20 案被纳粹处决 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深邃、庄重、新旧之交
- **配色**：普鲁士深蓝（保守而划时代）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeQ` 量子理论 — 靛蓝 `#4C5FD5`
  - `badgeThermo` 热力学 — 琥珀 `#E07B30`
  - `badgeBB` 黑体辐射 — 玫瑰 `#C4204F`
  - `badgePhil` 科学哲学 — 青绿 `#0E7C7B`
- **背景母题**：断续台阶（连续曲线被离散小方块打断，稀疏排布），呼应「能量发射从连续到量子化」——1900-12-14 的观念断裂（与第 2 步设计母题一致）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍、出生地、师承、任职、主要荣誉、核心领域。事实取自 page.md，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 量子理论奠基人 / Max Planck 1858–1947 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含出生地基尔、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 量子化 / 辐射律 / 熵与热力学 / 科学哲学（公式框：E = hν）
04  早年：基尔与慕尼黑 (1858–1874) — 法学教授之家、Hermann Müller 与能量守恒、音乐天赋
05  求学：慕尼黑与柏林 (1874–1880) — Jolly 劝退论、一生唯一的实验、Clausius 自学、博士论文
06  基尔岁月：熵与不可逆 (1885–1889) — 副教授、独立于 Gibbs 的化学热力学、电解质理论
07  柏林教席：继任基尔霍夫 (1889–1894) — Helmholtz 举荐、正教授、DPG 合并
08  黑体辐射困境 (1894–1900) — Kirchhoff 问题、Wien 律失效、Rayleigh–Jeans 紫外灾难
09  1900：量子化的诞生（核心贡献页，公式框 E = hν）— 10-19 第一版 / 12-14 量子假设、「绝望之举」
10  从质疑到接受 — 保守的革命者（Born 评语）、Rayleigh/Jeans/Lorentz 置 h=0、Planck 坚守
11  爱因斯坦与相对论 — 1905 力挺、作用量形式改写、1911 索尔维、1914 促成柏林受聘、合奏音乐
12  战争与家国之殇 — 《93 人宣言》、Karl 阵亡凡尔登、两个女儿难产而亡、Erwin 被处决
13  守夜人：纳粹时期 — 1933 面陈希特勒、庇护 Haber 纪念会、辞普鲁士科学院主席、柏林宅邸被毁
14  荣誉与纪念 — Nobel 1918 · Copley 1929 · Max Planck Medal 首届 · 威廉皇帝学会→马克斯·普朗克学会 · 2 马克硬币 · Planck 月球环形山
15  遗产：作用量子 h 与现代物理的基石
16  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）可整体复用标杆骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Planck 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 本名与署名 | 洗礼名含 "Marx Planck"（appellation name），十岁起自行改签 "Max"——若提及须写清是同一名，勿写成两个人或改名误会 |
| 诺奖年份口径 | **1918 年奖、1919 年才领取**（一战结束所致），两个年份都要交代，勿混写 |
| 获奖理由措辞 | 官方表格版 "In recognition of the services he rendered to the advancement of Physics by his discovery of energy quanta."；导语另有 "for the services he rendered..." 版本，以表格版为准，勿再改写 |
| 紫外灾难 | page.md 明载：紫外灾难**并非** Planck 的研究动机（"contrary to many textbooks, this was not a motivation"），禁写为动机 |
| h 的引入时间 | 作用量子 h 于 **1899 年已引入**（"introduced already in 1899"），量子化假设则提出于 1900-12-14，两个日期勿混 |
| 第一版辐射律 | 1900-10-19 的第一版**不含能量量子化、不用统计力学**；11 月才借 Boltzmann 统计诠释重推——勿把量子假设提前到 10 月 |
| 「绝望之举」 | 原话 "an act of despair ... I was ready to sacrifice any of my previous convictions about physics"（英文原文可引）；另 "a discovery of the first rank" 是 1918-12 对儿子 Erwin 所说 |
| Copenhagen 解释 | Planck 与 Schrödinger、Laue、Einstein 一样**拒绝**哥本哈根诠释，并期望波动力学取代自己的量子论——勿写成支持者 |
| 纳粹时期口径 | 必须平衡：一面签《93 人宣言》、劝科学家留守、1933 面陈希特勒失败；另一面暗中庇护犹太科学家继续在威廉皇帝学会工作、为 Haber 举行纪念会、1938 辞职抗议——勿单面化 |
| 名言辨伪 | "A new scientific truth does not triumph..."（科学真理在反对者死亡中胜利）常被引用，但 page.md 指出其有多个反例（含 Planck 本人学说十年内即被同行接受），引用时须带此注记 |
| 死亡日期噪声 | frontmatter 有 1947-10-04 与 1947-12-04 两值，正文确认 **1947-10-04**，以正文为准 |
| 宗教口径 | 信义会成员、被科学史家 Heilbron 定性为 deistic（自然神论），明言不信人格化的上帝；1937/1944 关于宗教与科学的演讲可写，勿写成正统基督徒 |
| 同名区分 | Max Planck Medal（德国物理学会最高奖章，1929 首届授予 de Broglie 于 1938 年颁奖礼语境）与马克斯·普朗克学会（1948 由威廉皇帝学会改名）勿混；其子 **Erwin Planck**（政治家，1945 被处决）勿与物理学家混淆 |
| 无载禁写 | 与 Stark 的「德意志物理学」冲突仅载 Stark 方攻击 Sommerfeld/Heisenberg 时连带 Planck（称其 "white Jews" 一词出自 Stark 攻击 Sommerfeld/Heisenberg/Planck 一行），勿展开为个人恩怨专题；Weierstrass 仅列名于 Berlin 学习年，无具体互动记载，禁编师生细节 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| energy quanta | 能量量子 | 诺奖理由用词，勿写「光量子」（photon 是 Einstein 概念且一度被 Planck 拒绝） |
| Planck constant / action quantum | 普朗克常数 / 作用量子 | h，1899 引入 |
| Planck postulate | 普朗克假设 | E=hν，1900-12-14 提出 |
| Planck's law | 普朗克辐射律 | 黑体辐射定律，勿与 Wien–Planck 律（1899 过渡版）混淆 |
| black-body radiation | 黑体辐射 | Kirchhoff 1859 提出的问题 |
| ultraviolet catastrophe | 紫外灾难 | 后起名词，且非 Planck 动机 |
| entropy | 熵 | Clausius 1865 定义，Planck 早期主战场 |
| Privatdozent | 无俸讲师 | 德语学术职衔，直译勿意译 |
| Kaiser Wilhelm Society | 威廉皇帝学会 | 1948 改名马克斯·普朗克学会 |
| Manifesto of the 93 | 《九十三人宣言》 | 1914 战争宣传文件，Planck 签署 |
| Deutsche Physik | 德意志物理学 | Stark 的「雅利安物理学」运动，勿译作中性词 |
| scientific realism | 科学实在论 | 与马赫实证主义的对立 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Timeless** — Alex-Productions
- **风格**: 沉稳 / 纪录片 / 长期纲领
- **匹配理由**:
  - 「长期纲领」完美匹配 Planck 的地位——量子理论不是一个单点突破，而是整个现代物理的地基，其影响贯穿百年至今
  - 「沉稳」匹配其保守革命者的气质——Born 评其「天性保守，却宣布了震撼物理学的最革命思想」
  - 「纪录片」匹配其跌宕一生——基尔 → 慕尼黑 → 柏林 → 1900 量子诞生 → 两战与家国之殇 → 格丁根
- **备选** (未采用):
  - ★★ Through the Darkness — 「黑暗/推进」匹配纳粹时期与丧子之痛，但全篇基调应落在科学遗产而非悲剧
  - ★★ The Flow of Time — 「时间感」匹配 89 年人生跨度，但受众偏低
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → `presentations/20th_century/Max_Karl_Ernst_Ludwig_Planck/Timeless.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Max_Karl_Ernst_Ludwig_Planck/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 标杆 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex` | 物理学家首例成品参考 |
| `mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex` | 数学家标杆参考 |
| `MySQL/seed_person.py` | 人物主记录 + fields/relations 入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
