# Marvin Minsky（马文·明斯基）立传提示词

> qid=Q210636 · 1927-08-09 – 2016-01-24 · 美国计算机科学家、认知科学家 · 20 世纪 · 1969 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1969/Marvin Minsky/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（心智社会 / 框架理论 / 感知机的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Marvin Lee Minsky（中文惯称：马文·明斯基）
- **生卒**：1927-08-09 生于纽约市（New York City，美国）→ 2016-01-24 逝于波士顿（Boston，马萨诸塞州），享年 88（死因未详述，勿编造）
- **国籍**：美国（American）
- **身份**：计算机科学家、认知科学家（AI 奠基人之一、"fathers of AI" 之一）
- **家庭**：父 Henry Minsky（眼科医生）、母 Fannie Reiser（犹太复国主义活动家）；犹太家庭
- **教育轨迹**：
  - 中学：Ethical Culture Fieldston School、Bronx High School of Science、Phillips Academy (Andover, MA)
  - 1944–1945 服役于美国海军（U.S. Navy）
  - 1950 年 Harvard University **数学**学士（A.B.）
  - Princeton University **数学**硕士+博士（MA, PhD）；1954 年获博士，论文 *Theory of neural-analog reinforcement systems and its application to the brain-model problem*
- **博士导师**：Albert W. Tucker（Princeton 数学家，博弈论"囚徒困境"命名者）
- **研究领域**：人工智能、神经网络、知识表示、认知科学

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **"AI 之父"之一**：与 Claude Shannon、Nathaniel Rochester、John McCarthy 因参与 Dartmouth workshop（达特茅斯会议，1956）被并称为 "fathers of AI"——是**之一**，勿写"唯一之父"。
2. **SNARC（1951）**：最早**随机连线（randomly wired）神经网络学习机**——Stochastic Neural Analog Reinforcement Calculator，早于其 MIT 入职。
3. **Harvard 数学学士（1950）→ Princeton 神经网络博士（1954）**：博士论文关于神经网络-模拟强化系统，导师 Tucker——**无 CS 学位**（当时无 CS 博士）。
4. **MIT AI Lab 共同创始人（1959）**：1958 年加入 MIT Lincoln Lab，1959 年与 McCarthy 共同发起 AI Lab 前身（2003 年定名 CSAIL）。
5. **Perceptrons（与 Seymour Papert，1969）**：批评 Frank Rosenblatt 的感知机，成为人工神经网络分析奠基之作；**被认为助长 1970 年代 AI 寒冬（AI winter）**——是"争议性"贡献。
6. **框架理论（frames）**：论文 *A Framework for Representing Knowledge* 开创知识表示新范式，到 1975 年已广泛应用。
7. **Society of Mind（心智社会理论，1986）**：1970 年代初与 Papert 在 MIT AI Lab 提出——智能是**无智能部分交互**的可能产物；1986 年出版大众向著作《The Society of Mind》。
8. **发明家的一面**：世界上第一台头戴图形显示器（1963）、共聚焦显微镜（1957，现代共聚焦激光扫描显微镜前身）、与 Papert 开发首个 Logo 语言驱动的"乌龟机器人"。
9. **7 状态 4 符号图灵机（1962）**：研究小型通用图灵机，发表著名的 7 状态 4 符号图灵机。
10. **大众文化**：Stanley Kubrick《2001: A Space Odyssey》顾问，片中角色 Victor Kaminski 以其命名；Arthur C. Clarke 同名小说提及 Minsky；发明"无用机器（useless machine）"哲学玩笑（Shannon 造出首个工作原型）。
11. **荣誉**：Turing Award 1969（ACM 称其为 "computer science's highest prize"）、Japan Prize 1990、Franklin Medal 2001、Computer History Museum Fellow 2006、IEEE AI Hall of Fame 2011 等。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（人工智能 — 蓝） | `#2E5A9E` | AI 之父 / Dartmouth 会议 |
| 分类色 2（神经网络 — 青绿） | `#1E8E8E` | SNARC / Perceptrons |
| 分类色 3（知识表示 — 琥珀） | `#D9A441` | 框架理论 / frames |
| 分类色 4（认知与心智 — 玫瑰） | `#C0395B` | Society of Mind |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「心智社会 / 无智能部分的交互」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：开创 / 哲思（AI 之父、心智社会）
- **选定曲目**：Alex-Productions **New Lands**（史诗 / 开阔），与 Knuth / McCarthy 同曲，匹配"让机器拥有心智"的开创叙事。
- **落地文件**：`turing/presentations/Marvin_Minsky/NewLands.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「AI 之父 · 美国」+ 明斯基 1927–2016 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1927–2016 生平纵览
4. **早年：纽约的犹太少年与海军岁月**（1927–1950）：眼科医生之子、海军服役、哈佛数学
5. **Princeton 神经网络博士**（1950–1954）：Tucker 门下、神经网络-模拟强化系统
6. **SNARC：第一台神经网络学习机**（1951）：随机连线、随机强化
7. **Dartmouth 会议与 AI 之父们**（1956）：与 Shannon/Rochester/McCarthy 共创 AI
8. **共启 MIT 人工智能实验室**（1959）：与 McCarthy 的合作
9. **Perceptrons 与感知机之争**（1969）：与 Papert、批评 Rosenblatt、AI 寒冬争议
10. **框架理论：知识表示的新范式**：frames、A Framework for Representing Knowledge
11. **Society of Mind：心智社会**（1986）：智能来自无智能部分的交互
12. **发明家的一面**：头戴显示器、共聚焦显微镜、Logo 乌龟机器人
13. **荣誉与传承**：Turing 1969、门生 Manuel Blum/Ivan Sutherland
14. **遗产**：AI、神经网络、知识表示、认知科学的奠基者
15. **结尾**：88 岁、"AI 之父"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **"AI 之父"表述**：与 Shannon、Rochester、McCarthy **四人并列**称为 "fathers of AI"，是**之一**，勿写"唯一之父"。
- **达特茅斯会议**：Dartmouth workshop 于 **1956** 年，由 McCarthy 等人发起，Minsky 是**参与者**——勿写"Minsky 发起"或写错年份。
- **MIT AI Lab 创建年**：1958 年加入 MIT/Lincoln Lab，**1959 年**与 McCarthy 共同发起 AI Lab 前身；实验室 **2003 年才定名 CSAIL**——勿写"1958 年创建 CSAIL"。
- **Perceptrons 争议**：与 Papert 的 *Perceptrons*（1969）批评 Rosenblatt 感知机，**被认为助长 AI 寒冬**——是"争议性"贡献，保留"争议"语境，勿写成纯正面突破。
- **框架 vs 框架理论**："frames" 是 Minsky 的**知识表示**理论（论文 *A Framework for Representing Knowledge*），与 GUI 窗口 "frame" 无关——勿与图形界面混淆。
- **SNARC 年份**：**1951** 年建造（早于 MIT 入职），是首台随机连线神经网络学习机——勿写成 1958 或混同感知机。
- **学位**：本科数学（Harvard 1950）、Princeton 硕士+博士（博士 1954，论文关于神经网络-模拟强化系统，导师 Tucker）——**无 CS 学位**（当时无 CS 博士）。
- **头戴显示器/共聚焦**：头戴图形显示器 **1963**；共聚焦显微镜 **1957**——是**光学/显示**发明，非 AI，放"发明家一面"页，勿与 AI 贡献混列。
- **生卒**：已故 1927-08-09 ~ 2016-01-24，写作 `1927–2016`，享年 88；死因未明确（勿编造）。
- **荣誉**：图灵奖 1969、Japan Prize 1990、Franklin Medal 2001、Computer History Museum Fellow 2006、IEEE AI Hall of Fame 2011 等；**无** Nobel、无 National Medal（勿编造）。Dan David 2014、BBVA 2013 可列但非核心。
- **大众文化**：《2001》顾问、片中角色 Victor Kaminski 以其命名；"useless machine" 是 Minsky 发明的哲学玩笑，**Shannon 造出首个工作原型**——勿把原型归给 Minsky。
- **图灵奖理由**：1969 年图灵奖，ACM 称其为 "computer science's highest prize"——表述为"计算机科学最高奖"，勿过度延伸。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q210636 | 待写入 |
| name_zh | 明斯基（或 马文·明斯基） | 待写入 |
| name_en | Marvin Minsky | 待写入 |
| birth_date | 1927-08-09 | 待写入 |
| death_date | 2016-01-24 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | artificial intelligence / neural networks / knowledge representation / cognitive science | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Albert W. Tucker（Princeton 数学家，博弈论"囚徒困境"命名者）
- **AI 之父同仁**：John McCarthy、Claude Shannon、Nathaniel Rochester（Dartmouth 会议共同参与者）
- **合作者**：Seymour Papert（Perceptrons 合著、Logo 乌龟机器人、Society of Mind 共同研究）
- **著名博士生**：Manuel Blum（1995 图灵奖得主）、Ivan Sutherland（1988 图灵奖得主）

## 8. 奖项清单

- Turing Award（1969，图灵奖，"computer science's highest prize"）
- Golden Plate Award（American Academy of Achievement，1982）
- Japan Prize（1990，日本国际奖）
- IJCAI Award for Research Excellence（1991）
- Benjamin Franklin Medal（Franklin Institute，2001）
- Computer History Museum Fellow（2006）
- IEEE Intelligent Systems AI Hall of Fame（2011）
- BBVA Foundation Frontiers of Knowledge Award（2013）
- Dan David Prize（"Future" 类，2014）
- 美国国家科学院院士（NAS，1973）、美国国家工程院院士（NAE，1989）

## 9. 机构清单

- 教育：Harvard University（数学 A.B. 1950）、Princeton University（数学 MA/PhD 1954）
- 任职：Harvard Society of Fellows 初级研究员（1954–1957）、MIT Lincoln Laboratory（1958）、MIT（1959 年起，与 McCarthy 共启 AI Lab；荣休时 Toshiba Professor of Media Arts and Sciences）

## 10. 终审清单

- [ ] 生卒 1927-08-09 / 2016-01-24，享年 88，出生地 New York City，去世地 Boston
- [ ] "AI 之父"表述为"之一"，与 Shannon/Rochester/McCarthy 并列
- [ ] Dartmouth 会议"1956、参与者"表述准确
- [ ] MIT AI Lab"1959 共启、2003 定名 CSAIL"表述准确
- [ ] Perceptrons"争议性、被认为助长 AI 寒冬"表述准确
- [ ] SNARC"1951、首台随机连线神经网络学习机"表述准确
- [ ] 博士"Harvard 数学学士、Princeton 数学博士、Tucker 导师"表述准确
- [ ] 头戴显示器 1963 / 共聚焦 1957 归入"发明家一面"，不与 AI 混列
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | MIT · Harvard · Princeton | Turing 1969`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1969/Marvin Minsky/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 OLPC 肖像（`images/Minsky.jpg`，已就绪）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Knuth/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同代图灵奖得主（McCarthy / Knuth）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
