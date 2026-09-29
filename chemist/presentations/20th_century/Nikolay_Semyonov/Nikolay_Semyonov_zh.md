# Nikolay Semyonov（尼古拉·谢苗诺夫）立传提示词

> qid=Q48990 · 1896-04-15 – 1986-09-25 · 苏联物理化学家 · 20 世纪 · 诺贝尔化学奖（1956，与 Cyril Norman Hinshelwood 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Nikolay_Semyonov/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框，是本次书写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像可用 Kustodiyev 1921 油画 Semyonov 与 Kapitsa 合像——注意**裁右取 Semyonov**，图注注明出处；1921 俄罗斯邮票像亦可备选）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{fire}\enspace 链式反应的统帅\enspace·\enspace 苏联`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「链式反应 / 分支」母题——圆点链分支暗示链传递与退化分支。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Nikolay Nikolayevich Semyonov（俄文：Никола́й Никола́евич Семёнов；中文惯称：尼古拉·尼古拉耶维奇·谢苗诺夫；拼法变体 Semenov/Semionov/Semenoff 并存，正文统一 Semyonov）
- **生卒**：1896-04-15（儒略历 4 月 3 日）生于萨拉托夫 → 1986-09-25 逝于莫斯科，享年 90，葬新圣女公墓（Novodevichy Cemetery；frontmatter 双值 04-03/04-15，**取新历 04-15**，与正文 "15 April (O.S. 3 April) 1896" 一致）
- **国籍**：Russian Empire → Soviet Union（生于帝国、成于苏联，两条 nationality）
- **身份**：物理学家兼化学家（physicist and chemist）；**苏联/俄罗斯唯一一位诺贝尔化学奖得主**
- **家庭**：父母 Yelena Dmitrieva 与 Nikolai Aleksandrovich Semyonov；1921 年娶语文学家 Maria Boreishe-Liverovsky（两年后去世）；1924-09-15 娶她的侄女 Natalia Nikolayevna Burtseva，育一子 Yuri、一女 Lyudmila
- **教育轨迹**：
  - 萨马拉实科中学（Samara Real School）
  - 彼得格勒大学物理系（1913–1917），Abram Ioffe 的学生；1916 年发表首篇论文
- **导师**：Abram Ioffe（约飞；infobox Doctoral advisor + 正文 "a student of Abram Fyodorovich Ioffe"）
- **研究领域**：化学物理——链式反应（化学链反应）、退化分支理论、燃烧过程、气体电离

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **萨拉托夫少年（1896）**：伏尔加河畔的省城之子，走进彼得格勒大学物理系。
2. **Ioffe 门下（1913–1917）**：俄国物理学 "Ioffe 学派" 的年轻人；1916 年发表第一篇研究论文。
3. **战乱漂泊（1918–1920）**：托木斯克任教；1919 年内战中被列入 Kolchak 白军征召但获教书缓征免役；同年 12 月被征入红军无线电勤务，1920 年冬退役。
4. **物理技术研究所（1920s）**：回彼得格勒主持物理技术研究所电子现象实验室，后任副所长。
5. **与 Kapitsa 测核磁矩（1922）**：与 Pyotr Kapitsa 共同找到测量原子核磁场的方法——该实验装置后经 Stern 与 Gerlach 改进而发展为著名的 Stern–Gerlach 实验。
6. **与 Frenkel 研究凝聚（1925）**：与 Yakov Frenkel 研究蒸气凝聚与吸附动力学。
7. **《电子化学》（1927）**：研究气体电离，出版重要著作 *Chemistry of the Electron*。
8. **与 Fock 的电介质击穿理论（1928）**：与 Vladimir Fock 共同创立电介质热击穿理论；同年任彼得格勒工学院教授。
9. **创建化学物理研究所（1931）**：在苏联科学院组建化学物理研究所（Institute of Chemical Physics，1943 年迁 Chernogolovka）并任首任所长；1932 年成为科学院正式院士。
10. **《化学动力学与链反应》（1934）**：苏联第一部系统发展非分支与分支链反应理论的专著（1935 出英文版）——1956 诺奖的理论基石。
11. **退化分支与燃烧（1934–1954）**：提出退化分支（degenerate branching）理论，解释氧化过程的诱导期；把链反应理论穷尽地应用于各类反应尤其是燃烧过程；1954 年 *Some Problems of Chemical Kinetics and Reactivity*（1958 修订，有英美德中译本）。
12. **1956 诺贝尔化学奖（共享）**：与英国 Hinshelwood 共享；页面口径 "for his work on the mechanism of chemical transformation"，官方同奖理由 "for their researches into the mechanism of chemical reactions"；诺奖演讲 1956-12-11《Some Problems Relating to Chain Reactions and to the Theory of Combustion》。
13. **身后地名与纪念**：1990 年化学物理研究所以他命名；莫斯科"院士谢苗诺夫街"、萨拉托夫与秋明同名街道、2021 年俄罗斯邮票、2019/2022 年莫斯科塑像——身后哀荣遍及学术与城市。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深钢蓝 steel navy） | `#16324F` | 化学物理的冷峻与燃烧理论的炽热底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（链式反应 badgeChain） | `#B4632A` | 琥珀分支链 / 链传递 |
| 分类色 2（燃烧理论 badgeCombustion） | `#7A1E28` | 深红氧化 / 诱导期 |
| 分类色 3（电离与电子 badgeElectron） | `#2E5A9E` | 蓝电子化学 / 电介质击穿 |
| 分类色 4（建制与传承 badgeInstitute） | `#1B7A43` | 绿化学物理研究所 / 门生 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），圆点链分支呼应「链引发 → 传递 → 分支 → 终止」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Mirage** — Notan Nigres（文件：`music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav`；勿复制 wav，视频阶段直接引用路径）
- **风格**：空灵电子 / 冷峻 / 悬疑推进
- **匹配理由**：
  - "海市蜃楼" 匹配链反应的意象——看不见的自由基链在气体中传递、分支、瞬间燎原
  - 冷峻电子匹配苏联化学物理研究所的气质——物理学家做化学，仪器与公式先行
  - 悬疑推进匹配其人生弧线——战乱漂泊到 Ioffe 门下到莫斯科院士，一部冷战时代的科学史诗（克制处理）
- **时长**：以实际文件为准，视频合成用 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 链式反应的统帅 / Nikolay Semyonov 1896–1986 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  谢苗诺夫的一生 — 时间线（10 节点：1896→1917→1922→1931→1934→1943→1954→1956→1969→1986）
04  早年：萨拉托夫到彼得格勒 (1896–1917) — 表格「时间|事件|结果」
05  战乱漂泊与物理技术所 (1918–1920s) — 表格「时间|事件|结果」
06  与 Kapitsa 测核磁矩 (1922) — 表格「合作者|装置|后续」+ 后续经 Stern–Gerlach 改进
07  1920s 物理化学多线并进 — 表格「合作者|主题|成果」（Frenkel 凝聚/Fock 击穿/电子化学）
08  化学物理研究所 (1931) — 建制页：创建、迁 Chernogolovka、首任所长、1932 院士
09  链反应理论 (1934–1954) — 表格「问题|理论|验证」+ 公式框：分支链增长示意
10  1956 诺贝尔化学奖 — 与 Hinshelwood 共享、双口径理由、苏联唯一化学诺奖
11  苏联科学院的荣誉长廊 — 「类别|代表|意义」表格 + itemize（九枚列宁勋章/Stalin 奖×2/英雄×2/Lomonosov 1969/Lenin 奖 1976）
12  门生与传承 — 表格「人物|方向|结果」（Frank-Kamenetskii/Shilov C-H 活化）
13  遗产 — 研究所以其命名/街道/邮票/塑像 + 理论进教科书（聚合、催化应用）
14  结尾 — 「一条看不见的链，点燃了整个燃烧的时代。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1956 诺奖 | **共享**（与 Cyril Norman Hinshelwood）；页面口径 "for his work on the mechanism of chemical transformation"、官方同奖理由 "for their researches into the mechanism of chemical reactions"——两口径可并注，勿写独享 |
| 苏联唯一 | "唯一一位苏联/俄罗斯化学诺奖得主"——页面明载可写，勿扩大成"苏联唯一诺奖得主" |
| 生卒日 | 1896-04-15（新历）/ 1986-09-25；frontmatter 04-03 是儒略历——Beamer 与 yaml 均用 04-15 并可注 (O.S. 3 April) |
| 与 Kapitsa 合作 | 1922 年共同设计测原子核磁场的装置；**Stern–Gerlach 实验是 Stern 与 Gerlach 后续改进的成果**——勿写"发明 Stern–Gerlach 实验" |
| 敏感点：政治 | 长期支持苏共：1953 年联署驳斥《原子科学家公报》审查指控、1971 年苏联科学家致 Nixon 公开信（Angela Davis 案）——**建议整页回避**；若写仅客观一句置于"时代语境"小节，禁止渲染立场 |
| 敏感点：白军/红军 | 1919 Kolchak 白军缓征免役、同年末被征入红军无线电勤务——页面明载可客观一句，勿渲染"两边押注" |
| 荣誉数字 | 列宁勋章 **九次**（1945、1953、1956、1966、1971、1976、1981 等其中七枚列年）；Hero of Socialist Labour **两次**（1966、1976）；Stalin Prize（1941、1949；frontmatter 等级信息有噪声，正文荣誉表只载年份）——数字勿混 |
| 荣誉噪声 | frontmatter 奖项数组有大量重复（Order of Lenin ×10+、荣誉列表混入 1932 "Honorary Member of The Soviet Academy of Sciences"）——以 §2 Honours 清单为准 |
| 名字拼法 | Semyonov / Semenov / Semionov / Semenoff 变体并存——正文统一 Semyonov；对手方入库名用 "Cyril Norman Hinshelwood" 全名 |
| 学生口径 | infobox Doctoral students 仅 **David A. Frank-Kamenetskii**；Alexander Shilov 是正文 "trained"（培养）——两人都收但 note 区分来源；Frank-Kamenetskii 理论（Semenov theory）勿与本人混淆 |
| Kustodiev 油画 | 1921 年 Kustodiev 为 Semyonov（右）与 Kapitsa 合像——裁图取右半 Semyonov；图注注明 "portrait by Boris Kustodiev, 1921" |
| 引语口径 | 本地页面**无直接引语**——全篇间接转述；1990 年访谈段（ spheron 模型）属 Pauling 篇内容，勿混入 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q48990 | ✅ |
| name_zh | 尼古拉·谢苗诺夫 | ✅ |
| name_en | Nikolay Semyonov | ✅（复用库内 id=2677 记录回填 QID，勿另建 Semenov 拼写 stub） |
| birth_date | 1896-04-15（新历，O.S. 1896-04-03） | ✅ |
| death_date | 1986-09-25 | ✅ |
| nationality | Russian Empire / Soviet Union（两条，rank 0/1） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemical physics（person_field 细分：chemical physics / chemical kinetics / chain reaction theory / combustion theory，带 rank） | ✅ |

## 7. 社会关系入库清单

**师长 / 门生 / 合作者 / 共同得主 / 家人**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Abram Ioffe | 师→生（博士导师） | 彼得格勒大学物理系，Ioffe 学派 |
| advisor-student | David A. Frank-Kamenetskii | Semyonov → 学生 | infobox Doctoral students |
| advisor-student | Alexander Shilov | Semyonov → 学生 | 正文 "trained"；后发现铂催化 C-H 活化 |
| colleague | Pyotr Kapitsa | 无向 | 1922 共同设计测量原子核磁场的装置 |
| colleague | Yakov Frenkel | 无向 | 1925 共同研究蒸气凝聚与吸附动力学 |
| colleague | Vladimir Fock | 无向 | 1928 共同创立电介质热击穿理论 |
| co-honored | Cyril Norman Hinshelwood | 无向 | 1956 诺贝尔化学奖共同得主 |
| spouse | Maria Boreishe-Liverovsky | 无向 | 1921 结婚，语文学家，两年后去世 |
| spouse | Natalia Nikolayevna Burtseva | 无向 | 1924-09-15 结婚（Maria 之侄女），育一子一女 |

> **禁入库名单**（页面无载或仅语境提及）：Otto Stern、Walther Gerlach（仅"后续改进装置"，非合作）；Viktor Zhirmunsky（仅 Maria 的老师语境）；Aleksandr Kolchak（征召语境非关系）；Yuri、Lyudmila（子女，页面无独立学术信息）。共同得主方向须与 Hinshelwood 侧 yaml 互指一致（双方均用全名 Nikolay Semyonov / Cyril Norman Hinshelwood）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1956，与 Hinshelwood 共享）
- Order of Lenin（九次，含 1945、1953、1956、1966、1971、1976、1981）
- Stalin Prize（1941、1949）
- Hero of Socialist Labour（两次：1966、1976）
- Order of the Red Banner of Labour（1946）；Order of the October Revolution（1986）
- Lomonosov Gold Medal（1969）；Lenin Prize（1976）；Mendeleev Prize
- Foreign Member of the Royal Society（1958）；美国国家科学院外籍院士（1963）
- 各国科学院院士/荣誉会员：Leopoldina（1959）、匈牙利（1961）、纽约（1962）、罗马尼亚（1965）、印度（1954）、英国化学会荣誉会员（1943）
- 荣誉博士：Oxford（1960）、Brussels（1962）、London（1965）、Milan（1964）、Budapest Technical University（1965）等

## 9. 机构清单

- 教育：Samara Real School；Petrograd University 物理系（1913–1917）
- 任职：Tomsk University Institute of Technology（1917–）；Perm/Tomsk 高校（1920 前后）；Petrograd Physico-Technical Institute（Ioffe Institute，电子现象实验室主任、副所长）；Petrograd Polytechnical Institute 教授（1928–）；Institute of Chemical Physics 创所所长（1931–，1943 迁 Chernogolovka）；苏联科学院正式院士（1932）
- 命名遗产：N.N. Semenov Institute of Chemical Physics（1990 更名）；莫斯科 Academician Semyonov Street；Aeroflot A321 "N. Semyonov" 号

## 10. 终审清单

- [ ] 生卒 1896-04-15（新历）/ 1986-09-25（享年 90），出生地 Saratov、去世地 Moscow、葬 Novodevichy
- [ ] 1956 共享（Hinshelwood）、双口径获奖理由并注；"苏联唯一化学诺奖"表述准确
- [ ] Kapitsa 1922 合作 + Stern–Gerlach 后续改进口径不越界
- [ ] 列宁勋章九次、英雄两次、Stalin 奖 1941/1949 数字准确
- [ ] 两位配偶时序（1921 Maria→1924 Natalia）与子女两名准确
- [ ] 学生两人 note 区分 infobox/正文来源；Stern/Gerlach 不入库
- [ ] 政治敏感点回避或一句客观；页面无直接引语（全篇转述）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Nikolay_Semyonov/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：Kustodiev 1921 油画裁右（Semyonov）与图注核对；或用 2021 邮票像
- [ ] 国籍：封面顶部明示苏联（生为俄帝国臣民可注）
- [ ] 引语核对：页面无直接引语——确认全篇为间接转述
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改动该文件。
> **数据入库**：yaml 见 `MySQL/data/Nikolay_Semyonov.yaml`（复用库内记录 UPD 回填 QID，含 4 fields / 9 relations）。
