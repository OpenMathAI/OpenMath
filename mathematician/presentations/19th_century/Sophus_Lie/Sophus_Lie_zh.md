# Sophus Lie（马里乌斯·索菲斯·李）立传提示词

> qid=Q30769 · 1842-12-17 – 1899-02-18 · 挪威数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/Sophus_Lie/`（page.md + metadata.json + images.txt）
>
> **立传状态：✅ 已完成（参考高斯基准模板）**——tex（13 页正文）+ Makefile + 头像就位，`make distclean && make` 编译通过、Overfull = 0；头像采用 Wikipedia 条目主图（挪威国家图书馆藏肖像，`images/lie_portrait.jpg`，1238×1647）；BGM 已选 **The Invisible Light**（Infraction，纪录片风格），视频已生成；MySQL yaml 本次新建入库。

## 1. 人物速览

- **中文全名**：马里乌斯·索菲斯·李（通称索菲斯·李）
- **英文全名**：Marius Sophus Lie（挪威语发音 /liː/）
- **生卒**：1842-12-17 Nordfjordeid — 1899-02-18 Kristiania（今奥斯陆），享年 56
- **身份**：挪威数学家——连续对称理论的缔造者，李群 / 李代数之父
- **国籍**：挪威
- **核心领域**：连续变换群（李群）、微分方程、几何、对称

## 2. 立传硬性要求（Wilson 模板）

- **头像**：Wikipedia 条目主图——已就位 `images/lie_portrait.jpg`
- **国籍徽章**：封面顶部 `\faIcon{globe}\enspace 挪威`，身份页国籍栏「挪威」
- **身份信息页**（★ 必做）：左肖像 + 右 2×2 网格（生卒 / 本名 / 国籍 / 教育 皇家腓特烈大学 / 师承 Bjerknes·Guldberg / 出生地 Nordfjordeid / 荣誉 Lobachevsky·ForMemRS / 核心领域）
- **配色**：北欧峡湾蓝 `nordicblue #1F3A93` + 数学金 `#C9A227` + 分类色（李群靛蓝 `#4C5FD5` / 李代数青绿 `#0E7C7B` / 微分方程琥珀 `#E07B30` / 遗产灰 `#4A5568`）
- **背景母题**：连续对称 / 峡湾曲线——沿用模板 deckbackground 气泡
- **品牌**：`\input{../../cover/openmath_page.tex}` + 页脚 OpenMathAI

### 3.5 背景音乐选择 ✅ 【已选定】

- **选定曲目**：**The Invisible Light**（Infraction，`music_audio/inspiring-electronic/19-tGxXsgSKPiQ-...The Invisible Light.wav`，已软链为 `bgm.wav`）
- **匹配理由**：纪录片风格"无形之光"——隐喻无穷小生成元的线性化思想（连续之光照进微分方程）；契合巴黎误捕、莱比锡岁月与 Abel 奖远见的多幕叙事
- （避免重复：Poncelet=Flow of Time、Cayley=Timeless、Hermite=Eroica、Eisenstein=Lonesome、Kronecker=Beethoven No.5）

## 4. Slide 规划（实际 13 页正文 + OpenMath 封面）

1. **封面**（`\titleslide`）：大标题「索菲斯·李」+ 副题「连续对称理论的缔造者 · 李群与李代数之父」+ 右上头像 + 国籍行 + 三要素状态栏 + 4 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 网格
3. **时间线**（`\timelineslide`）：1842 Nordfjordeid → 从军梦碎 → 1869 首篇+柏林遇 Klein → 1870 巴黎误捕 → 1871 博士 → 1872 特设教授+编 Abel → 1874 成婚 → 1884 Engel 来援 → 1886 莱比锡 → 1889 病倒 → 1898 归国 → 1899 逝世
4. **早年与从军梦碎**（1842–1869）：牧师家庭幼子（六子最幼）、Moss 与奥斯陆求学、参军因视力被拒、皇家腓特烈大学
5. **柏林与巴黎：友谊与牢狱**（1869–1870）：首篇论文（Crelle）、柏林遇 Klein、巴黎遇 Jordan/Darboux、普法战争、Fontainebleau 误捕（德国间谍嫌疑）、Darboux 营救、因祸得福声名鹊起
6. **博士与特设教席**（1871–1876）：博士论文（Darboux"现代几何最美的发现之一"）、议会特设教授、与 Sylow 编 Abel 全集、1874 婚 Anna Birch（三子女）、1876 共同主编 Archiv
7. **连续群与线性化**（核心贡献页）：连续变换群 → 无穷小生成元 → 交换子括号 → 李代数（表格 + 公式框 $[X,Y]=XY-YX$；红线："今称"表述）
8. **《变换群理论》与莱比锡**（核心贡献页）：Klein/Mayer 支持、Engel 合作、3 卷 1888–1893、1886 莱比锡教授（接任 Klein）
9. **以他命名的世界**（核心贡献页）：李群/李代数/李括号/单参数群/切触变换/球几何/Lie 定理/第三定理/Lie–Kolchin/C–J–L/乘积公式
10. **学生与传承**（核心叙事页）：Cartan（20 世纪最伟大之一）、Blichfeldt、Żorawski、Kowalewski、Lovett、Scheffers、Tresse、Bouton
11. **荣誉与晚年**（核心叙事页）：LMS 1878 / 法科院 1892 / 曼彻斯特 1894 / ForMemRS+NAS 1895 / Lobachevsky 1897 / 圣奥拉夫骑士；1889 精神崩溃（客观）、恶性贫血、1898 归国、1899 逝世
12. **遗产：从 Weyl 到 Abel 奖**（核心叙事页）：Weyl 1922/23 → 李群进入量子力学；"19 世纪大师中细节最不为人知"（20 世纪学者评述，注明性质）；推动设立 Abel 奖（Nansen 基金启发 + 诺贝尔无数学奖）
13. **终章**（`\closingslide`）：「他把"连续"变成了群，让对称成为物理的语言。」

## 5. 历史事实清单（对照 page.md 逐条核对）

| 事实 | 使用页 |
|---|---|
| 1842-12-17 生于 Nordfjordeid；路德宗牧师 Johann Herman Lie 六子最幼；母系出自 Trondheim 名门 | S3/S4 |
| 小学 Moss、中学 Christiania；从军志向因视力不佳被军队拒绝；入皇家腓特烈大学 | S4 |
| 1869《Repräsentation der Imaginären der Plangeometrie》刊于 Christiania 科学院与 Crelle；获奖学金赴柏林（1869-09–1870-02） | S5 |
| 柏林遇 Klein 成挚友；巴黎遇 Jordan、Darboux | S5 |
| 1870-07-19 普法战争爆发；Klein 速离；Lie 在 Fontainebleau 被当德国间谍逮捕，Darboux 干预月余获释——在挪威声名鹊起 | S5 |
| 1871 博士《Over en Classe geometriske Transformationer》；Darboux 称"现代几何最美的发现之一" | S6 |
| 1872 议会特设 extraordinary professorship；同年访 Klein（Erlangen program） | S6 |
| 1872 与 Sylow 八个月编出版 Abel 数学著作 | S6 |
| 1872 底向 18 岁 Anna Birch 求婚、1874 成婚；子女 Marie 1877 / Dagny 1880 / Herman 1884 | S6 |
| 1876 与 Worm-Müller、Sars 共同主编 Archiv for Mathematik og Naturvidenskab | S6 |
| 1884 Klein+Mayer 支持 Engel 到 Christiania 协助；《Theorie der Transformationsgruppen》3 卷 1888–1893；Engel 后为全集编辑 | S8 |
| 1886 莱比锡教授（接替去哥廷根的 Klein） | S8 |
| 1889-11 精神崩溃住院至 1890-06；贫血加重；1898-05 辞职、9 月归国；1899-02-18 死于恶性贫血（B12 吸收障碍），56 岁 | S11 |
| 荣誉：LMS 1878、法科院通讯 1892、曼彻斯特文哲会 1894、ForMemRS 1895、美国 NAS 1895、Lobachevsky Medal 1897、圣奥拉夫骑士 | S11 |

### 学术红线

- **线性化表述**：连续变换群（今称李群）经"线性化"研究生成向量场（无穷小生成元）；生成元满足群律的线性化版本（交换子括号），具有今日所谓李代数的结构。**不写李本人发明"李代数"一词，用"今称/今天所谓"。**
- **历史评价**：Hermann Weyl 1922/23 用于群论；李群今日在量子力学中发挥作用；"19 世纪大师中李的工作就细节而言最不为人所知"——注明为后世学者评述，非贬低。
- **Abel 奖**：受 Nansen 基金与诺贝尔无数学奖启发，积极倡议设立纯数学大奖（今 Abel 奖）。
- **学生**：Cartan（20 世纪最伟大之一）、Żorawski、Blichfeldt、Kowalewski、Lovett、Scheffers、Tresse、Bouton。
- **博导**：Bjerknes、Guldberg。
- **引语红线**：Darboux"现代几何最美的发现之一"可直接引用；"最不为人所知"注明后世评述；封面金句自创总结句。

## 6. 数据库核对表（MySQL/data/Sophus_Lie.yaml — 本次新建）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q30769 | ✅ 新建入库 |
| name_zh | 索菲斯·李 | ✅ |
| birth / death | 1842-12-17 / 1899-02-18 | ✅ |
| nationality | Norway 挪威 | ✅ |
| primary_occupation | mathematician | ✅ |
| fields | group theory / geometry / differential equations / symmetry | ✅ |
| relations | 博导 Bjerknes·Guldberg；学生 Cartan·Scheffers·Blichfeldt·Kowalewski·Lovett·Tresse·Bouton·Żorawski·Böttcher·Holst；colleague Klein（挚友）·Sylow（合编 Abel）·Engel（合作）·Darboux（营救） | ✅ |
| has_biography | true | ✅ 本次置 true |

## 7. 终审清单

- [x] 生卒 1842-12-17 / 1899-02-18，享年 56，出生地 Nordfjordeid，逝地 Kristiania
- [x] 巴黎误捕"德国间谍嫌疑、Darboux 营救、因祸得福"客观表述（Slide 5）
- [x] 李群/李代数"今称"表述红线（Slide 7 表格 + 公式框 + Slide 9 命名页均注明）
- [x] "细节最不为人知"注明 20 世纪学者评述（Slide 12）
- [x] Engel 合作与《变换群理论》3 卷年份准确（Slide 8）
- [x] 荣誉年份全部对齐 page.md（Slide 11）
- [x] 头像确认（✅ 挪威国家图书馆藏肖像，`images/lie_portrait.jpg`）
- [x] 国籍用「挪威」现代对应
- [x] Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，Overfull = 0；`make images && make video` 完成（BGM: The Invisible Light）

## 8. Review 轮次记录

### 第 1 轮（Review-1）：事实终审
- [x] 逐页对照 page.md（生卒、教育、误捕、博士、特设教席、编 Abel、婚姻子女、Engel、莱比锡、疾病、荣誉年份）
- [x] 头像：API 条目主图下载验证
- [x] 引语核对：Darboux 评语直接引用；"最不为人所知"注明评述性质
- [x] 编译验证 + 视频生成
- [x] 更新提示词

### 第 2 轮（Review-2）：结构优化
- [x] Overfull = 0
- [x] 身份信息页与 Wilson 模板对齐
- [x] 中文标点 / 断行统一
- [x] 与同世纪数学家（Boole/Poncelet/Cayley/Hermite/Eisenstein/Kronecker）格式对齐
