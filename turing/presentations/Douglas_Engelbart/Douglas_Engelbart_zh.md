# Douglas Engelbart（道格拉斯·恩格尔巴特）立传提示词

> qid=Q92614 · 1925-01-30 – 2013-07-02 · 美国工程师、发明家 · 20 世纪 · 1997 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1997/Douglas Engelbart/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（鼠标专利 / NLS 系统的信息结构化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Douglas Carl Engelbart（中文惯称：道格拉斯·恩格尔巴特）
- **生卒**：1925-01-30 生于 Portland, Oregon（美国）→ 2013-07-02 逝于 Atherton, California 家中，享年 88（死因页面实载：肾衰竭 kidney failure；Doug Engelbart Institute 称其 2007 年确诊阿尔茨海默病后长期患病）
- **国籍**：美国（American）
- **身份**：工程师、发明家、计算机科学先驱；人机交互（HCI）领域奠基人
- **家庭**：父 Carl Louis Engelbart、母 Gladys Charlotte Amelia Munson Engelbart；德/瑞典/挪威裔；三子女居中；8 岁随家迁往 Johnson Creek 沿岸乡下、**9 岁丧父**
- **婚姻**：1951-05-05 与 Ballard Fish（1928-08-18 – 1997-06-18）在 Portola State Park 结婚，育四子女（Gerda、Diana、Christina、Norman）；2008-01-26 再婚 Karen O'Leary Engelbart
- **教育轨迹**：
  - 1942 年毕业于 Portland 的 Franklin High School
  - Oregon State University 电气工程本科（期间 1944 前后入美国海军服役两年，任菲律宾无线电/雷达技师）
  - 1948 年获 Oregon State 电气工程学士（BS）
  - UC Berkeley 电气工程（计算机方向）：MS 1953、PhD 1955；博士论文 *A Study of High-Frequency Gas-Conduction Electronics in Digital Computers*
- **博士导师**：Paul L. Morton、John R. Woodyard（Berkeley）
- **研究领域**：人机交互（human–computer interaction）、交互计算、发明

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **"As We May Think" 的菲律宾相遇（1945）**：在 Leyte 岛高脚屋中读到 Vannevar Bush 的 *"As We May Think"*——影响其一生方向（可引 Engelbart 给 Bush 的信中自述：在"丛林边缘的红十字图书馆"读到此文，页面实载）。
2. **1950 年的职业顿悟**：订婚之际意识到自己除"稳定工作、结婚、幸福生活"外没有职业目标，遂立下"以毕生之力让世界更好"的纲领——立志用计算机**增强人类集体智慧**（harnessing collective intellect）。
3. **Berkeley 时代**：协助建造 CALDIC，研究生工作取得 8 项专利；毕业后留校任助理教授一年，因无法实现其愿景离开；创办过 Digital Techniques 初创。
4. **1962 年纲领报告**：*Augmenting Human Intellect: A Conceptual Framework*（SRI Summary Report AFOSR-3223）——其愿景与议程的奠基文献；ARPA 由此资助其研究。
5. **增强研究中心 ARC**：1957 年入职 SRI（时称 Stanford Research Institute），先与 Hewitt Crane 合作磁性器件；后创立 Augmentation Research Center，提出"bootstrapping strategy"实验室组织原则。
6. **鼠标（与 Bill English）**：木壳双金属轮鼠标在 **1965 年前**与首席工程师 Bill English 共同研制；**1967 年申请专利、1970 年获批**（U.S. patent 3,541,541），专利文件称 "X-Y position indicator for a display system"；绰号"mouse"因"尾巴从末端伸出"——**Engelbart 终身未获任何分成**，SRI 曾以约 4 万美元授权给 Apple（Engelbart 采访原话，页面实载）。
7. **NLS（oN-Line System）**：ARC 在 ARPA 资助下开发的系统，演示了鼠标、位图屏幕、文字处理、超文本、和弦键盘（chorded keyboard）等——多数已成今日通用技术；GUI 的前身。
8. **The Mother of All Demos（1968）**：1968-12-09 在旧金山 Fall Joint Computer Conference 的技术演示——页面直接使用"The Mother of All Demos"表述，可写。
9. **Engelbart's law**：人类内在绩效（intrinsic rate of human performance）呈指数增长——以其命名的观察。
10. **后期生涯的落寞与再出发**：1970 年代多位研究员转投 Xerox PARC；Mansfield Amendment（1969）等导致经费萎缩；实验室 1976 年并入 Tymshare（NLS 更名 Augment）；1984 年随收购进入 McDonnell Douglas；1986 年退休；1988 年与女儿 Christina 创办 Bootstrap Institute（后为 The Doug Engelbart Institute）；2005 年获 NSF 资助开源 HyperScope 项目。
11. **荣誉序列**：Turing Award 1997、Lemelson-MIT Prize 1997（50 万美元，当时世界最大单项发明奖）、National Medal of Technology 2000（克林顿总统颁发，美国最高技术奖）、Lovelace Medal 2001、CHM Fellow 2005、NAE 院士 1996 等。
12. **身后**：2013-07-02 去世；挚友、超文本先驱 Ted Nelson 致悼词；九个孙辈。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（人机交互 — 蓝） | `#2E5A9E` | HCI 奠基 / ARC |
| 分类色 2（鼠标与输入装置 — 青绿） | `#1E8E8E` | 鼠标专利 / 和弦键盘 |
| 分类色 3（超文本与 NLS — 琥珀） | `#D9A441` | 超文本 / NLS / Augment |
| 分类色 4（增强集体智慧 — 玫瑰） | `#C0395B` | Augmenting Human Intellect / Collective IQ |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「飞越信息空间的工作站」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：觉醒 / 远见（丛林书页中的顿悟、用机器增强人类心智）
- **选定曲目**：Alex-Productions **Awaken**（manifest 预分配，直接沿用；物理学家 't Hooft 篇同曲，属正常复用），匹配"1950 年立志、以毕生唤醒集体智慧"的叙事。
- **落地文件**：`turing/presentations/Douglas_Engelbart/Awaken.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「鼠标之父 · 美国」+ 恩格尔巴特 1925–2013 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 导师 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1925–2013 生平纵览
4. **早年：波特兰与海军岁月**（1925–1948）：9 岁丧父、菲律宾雷达技师、Leyte 岛读 Bush
5. **Berkeley 博士与顿悟**（1950–1955）：CALDIC、8 项专利、Morton/Woodyard 门下
6. **1962 年纲领**：Augmenting Human Intellect: A Conceptual Framework（公式框：概念框架）
7. **SRI 与增强研究中心 ARC**（1957–）：Hewitt Crane、bootstrapping 策略
8. **鼠标的发明**（1965 前–1970）：与 Bill English、专利 3,541,541、无分成
9. **NLS：oN-Line System**：位图屏幕、超文本、和弦键盘、GUI 前身
10. **The Mother of All Demos（1968）**：旧金山 Fall Joint Computer Conference
11. **落寞年代**（1970s–1986）：PARC 分流、经费萎缩、Tymshare/McDonnell Douglas、Augment 更名
12. **再出发：Bootstrap 与 Institute**（1988–）：与女儿 Christina、Collective IQ、HyperScope
13. **荣誉**：Turing 1997、Lemelson-MIT 1997、National Medal of Technology 2000、Lovelace 2001、CHM Fellow 2005
14. **遗产**：鼠标、超文本、GUI、 Engelbart's law
15. **结尾**：88 岁、"让世界更好"的毕生纲领与传承

## 5. 史实陷阱与敏感点（终审必须检查）

- **鼠标的"并行独立发明"**：页面明确注明"The computer mouse has been subject to a parallel and independent invention"——勿写"全世界唯一发明者"；写"发明者（与 Bill English 共同研制）"。
- **鼠标时间线**：1965 **前**研制 → **1967 申请**专利 → **1970 获批**——三个年份勿混；专利名 "X-Y position indicator for a display system" 可引用。
- **鼠标无分成**：Engelbart **从未获得任何版税**；SRI 以约 $40,000 授权 Apple——是 Engelbart 采访原话，引用时注明"Engelbart 后来说"。
- **"Mother of All Demos"**：页面正文确实使用该表述（1968）——可用；日期 1968-12-09（Fall Joint Computer Conference，旧金山）。
- **图灵奖**：页面只写"won the 1997 ACM Turing Award"，**未给出整句 citation**——勿自行编造 ACM citation，表述为"1997 年获图灵奖"即可。
- **教育**：Oregon State 电气工程 BS（1948，海军服役中断两年）；Berkeley MS 1953 / PhD 1955——勿写 PhD 年份为 1956（那是thesis标注年，infobox 论文 1955 毕业，正文 1955）。
- **双重死因口径**：直接死因 kidney failure； Institute 称 2007 年确诊阿尔茨海默病、长期患病——两者按页面并写，勿只取其一渲染。
- **婚姻年份**：首婚 **1951-05-05**（Ballard Fish，1997 年去世）；再婚 **2008-01-26**（Karen O'Leary）——勿混。
- **EST 与实验室 morale**：1972 年起 ARC 多名成员参与 Erhard Seminars Training、争议削弱团队凝聚力——按实载一笔带过，勿渲染细节。
- **房屋失火**：Atherton 的家在此期间烧毁（页面实载）——可一笔带过，勿加细节。
- **荣誉年份**：Franklin Institute Certificate of Merit **1996**、Benjamin Franklin Medal **1999**——勿互换；NAE 院士 **1996**；National Inventors Hall of Fame **1998**（入選的是鼠标发明）。
- **在世亲属**：第二任妻子、第一次婚姻的四子女、九个孙辈——按实载。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | manifest 为 null，待补 |
| name_zh | 恩格尔巴特（或 道格拉斯·恩格尔巴特） | 待写入 |
| name_en | Douglas Engelbart | 待写入 |
| birth_date | 1925-01-30 | 待写入 |
| death_date | 2013-07-02 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | engineer and inventor（computer science pioneer） | 待写入 |
| field_of_work | human–computer interaction / hypertext / interactive computing | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Paul L. Morton、John R. Woodyard（UC Berkeley）
- **核心合作者**：Bill English（鼠标首席工程师、NLS）、Hewitt Crane（SRI 磁性器件，挚友）
- **思想源头**：Vannevar Bush（"As We May Think"，影响者，非师承）
- **女儿**：Christina Engelbart（Bootstrap Institute / Doug Engelbart Institute 联合创办人）
- **相关先驱**：Ted Nelson（挚友、超文本先驱、悼词）；Bob Taylor（政府资助方）——页面实载，按"同仁"关系入库
- **无载禁写**：页面未列其博士生名单——勿编造学生关系

## 8. 奖项清单

- Turing Award（1997）
- Lemelson-MIT Prize（1997，50 万美元）
- National Medal of Technology（2000-12，克林顿总统颁发）
- BCS Lovelace Medal（2001）
- Norbert Wiener Award for Social and Professional Responsibility（CPSR 颁发）
- Franklin Institute Certificate of Merit（1996）；Benjamin Franklin Medal（1999，Computer and Cognitive Science）
- CHI Lifetime Achievement Award（1998）；CHI Academy（2002）
- National Inventors Hall of Fame（1998）；Stibitz-Wilson Award（1998）
- NAE Member（1996）
- Computer History Museum Fellow Award（2005）
- 首位 Yuri Rubinsky Memorial Award 获得者（1995-12，后更名）
- NMC Fellow（2009）；IEEE Intelligent Systems AI's Hall of Fame（2011）
- Yale University 荣誉工程与技术博士（2011-05，该校首个此类荣誉学位）

## 9. 机构清单

- 教育：Oregon State University（电气工程 BS 1948，海军服役中断）、UC Berkeley（MS 1953、PhD 1955）
- 任职：NACA Ames Research Center（风洞维护）、UC Berkeley（助理教授约一年）、Digital Techniques（创业）、SRI International（1957 年起，创立 ARC）、Tymshare（Senior Scientist，1976 起）、McDonnell Douglas（至 1986 退休）、Bootstrap Institute / The Doug Engelbart Institute（1988 年起，Founder Emeritus）

## 10. 终审清单

- [ ] 生卒 1925-01-30 / 2013-07-02，享年 88，出生地 Portland, Oregon，去世地 Atherton, California
- [ ] 鼠标"与 Bill English 共同研制、1967 申请/1970 获批、无版税"表述准确，注明存在并行独立发明
- [ ] "Mother of All Demos" 1968-12-09 表述准确
- [ ] 1962 纲领报告标题完整：Augmenting Human Intellect: A Conceptual Framework
- [ ] 图灵奖只写"1997 年获奖"，不编造 citation
- [ ] Berkeley MS 1953 / PhD 1955、导师 Morton & Woodyard
- [ ] 双重死因口径（kidney failure + 2007 确诊阿尔茨海默病长期患病）
- [ ] NLS→Augment 更名（Tymshare 1976 / McDonnell Douglas 1984）链条准确
- [ ] 引语仅限页面实载（给 Bush 的信、$40,000 采访语），标注出处
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | SRI · Tymshare · McDonnell Douglas | Turing 1997`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1997/Douglas Engelbart/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/SRI_Douglas_Engelbart_1968_cropped_.jpg`（1968 年真肖像，已就绪）；鼠标实物图 `500px-SRI_Computer_Mouse.jpg` 可作插图
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同代图灵奖得主（1996 Pnueli / 1998 Gray）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
