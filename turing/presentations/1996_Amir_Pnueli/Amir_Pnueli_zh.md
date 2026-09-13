# Amir Pnueli（阿米尔·普努利）立传提示词

> qid=Q92649 · 1941-04-22 – 2009-11-02 · 以色列计算机科学家 · 20 世纪 · 1996 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1996/Amir Pnueli/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 以色列`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（时态逻辑 / 模型检验的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Amir Pnueli（希伯来文：אמיר פנואלי；中文惯称：阿米尔·普努利）
- **生卒**：1941-04-22 生于 Nahalal（英国托管巴勒斯坦，今以色列）→ 2009-11-02 逝于纽约（New York，美国），享年 68（死因页面实载：脑出血 brain hemorrhage）
- **国籍**：以色列（Israeli）
- **身份**：计算机科学家，1996 年图灵奖得主
- **家庭**：有三个子女、四个孙辈（页面对父母/配偶无载，勿编造）
- **教育轨迹**：
  - 中学：Tel Aviv 的 Tichon Hadash 高中
  - Technion（以色列理工学院）**数学**学士（BS，Haifa）
  - Weizmann Institute of Science **应用数学**硕士+博士（MS, PhD）；**1967 年**获博士，论文题为 *"Calculation of Tides in the Ocean"*（海洋潮汐计算）——是应用数学论文，**非计算机科学**
  - Stanford University 博士后期间转向计算机科学
- **师承**：页面未载博士导师姓名（Math Genealogy 仅作参考来源），勿编造导师
- **研究领域**：时态逻辑（temporal logic）、模型检验（model checking）、并发系统（concurrent systems）的公平性（fairness）性质

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **时态逻辑引入计算科学**：1996 图灵奖核心贡献——"for seminal work introducing temporal logic into computing science and for outstanding contributions to program and systems verification"（获奖理由整句引用）。
2. **数学→计算机的转型**：应用数学博士（潮汐计算，1967）→ Stanford 博士后转向计算机科学——研究方向的大转折是其生平最大叙事节点。
3. **时态逻辑与模型检验**：工作聚焦时态逻辑与 model checking，尤其**并发系统的公平性性质**（fairness properties of concurrent systems）。
4. **Tel Aviv 大学计算机系创始人**：回以色列后任研究者，是 Tel Aviv University 计算机科学系的**创始人与首任系主任**（founder and first chair）。
5. **Weizmann 教授（1981）**：1981 年起任 Weizmann Institute of Science 计算机科学教授。
6. **纽约大学双聘（1999–2009）**：自 1999 年直至去世兼任 NYU 计算机科学系教授——以色列与美国两地穿梭的学术生涯。
7. **多机构履历**：曾任 University of Pennsylvania 与 Joseph Fourier University 副教授；早年机构还包括 Stanford 博士后。
8. **创业者的一面**：职业生涯中创办过**两家**科技初创公司。
9. **以色列计算机科学的旗帜**：2000 年获 Israel Prize（计算机科学）——以色列国内最高科学荣誉。
10. **荣誉序列**：Uppsala University 荣誉博士（1997-05-30）、美国国家工程院外籍院士（1999）、ACM Fellow（2007）；Weizmann 设立以其命名的纪念讲座系列。
11. **门生**：博士学生包括 Mordechai Ben-Ari、Dana Fisman、Nissim Francez、Doron A. Peled、Ofer Strichman、Lenore Zuck（infobox 实载）。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（时态逻辑 — 蓝） | `#2E5A9E` | 时态逻辑引入计算科学 |
| 分类色 2（模型检验 — 青绿） | `#1E8E8E` | model checking |
| 分类色 3（并发与公平性 — 琥珀） | `#D9A441` | concurrent systems / fairness |
| 分类色 4（程序与系统验证 — 玫瑰） | `#C0395B` | program and systems verification |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「时间在逻辑中流动」的时态逻辑视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：深潜 / 反思（时态逻辑的严谨与早逝的遗憾）
- **选定曲目**：Alex-Productions **Falling Apart**（manifest 预分配，直接沿用），匹配"形式化验证的冷峻与 68 岁猝然离场"的叙事底色。
- **落地文件**：`turing/presentations/Amir_Pnueli/FallingApart.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「时态逻辑之父 · 以色列」+ 普努利 1941–2009 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 转型节点 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1941–2009 生平纵览
4. **早年：Nahalal 的少年**（1941–1959）：托管巴勒斯坦出生、Tichon Hadash 中学、Technion 数学
5. **Weizmann 应用数学博士**（1959–1967）：潮汐计算论文——**非 CS** 的起点
6. **Stanford 转折**（1967 年后）：博士后期间转向计算机科学
7. **时态逻辑进入计算科学**：图灵奖获奖理由整句 + 时态逻辑的形式化表达（公式框）
8. **并发系统的公平性**：concurrent systems / fairness 性质
9. **模型检验与程序验证**：model checking、program and systems verification
10. **Tel Aviv：从零建系**：创始人与首任系主任
11. **Weizmann 与 NYU 双城记**（1981–2009）：以色列—纽约两地学术生涯
12. **创业者与师者**：两家初创公司、六位博士学生
13. **荣誉**：Turing 1996、Israel Prize 2000、NAE 外籍院士 1999、Uppsala 荣誉博士 1997、ACM Fellow 2007
14. **遗产**：时态逻辑成为程序验证与模型检验的基石
15. **结尾**：68 岁、脑出血猝逝纽约、Weizmann 纪念讲座的传承

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由整句**："for seminal work introducing temporal logic into computing science and for outstanding contributions to program and systems verification"——核心红线，勿改写、勿只取半句。
- **博士论文主题**：*"Calculation of Tides in the Ocean"*（海洋潮汐），是**应用数学**论文——勿写成计算机/时态逻辑相关；转向 CS 发生在 **Stanford 博士后**期间。
- **学位**：Technion 数学学士、Weizmann 应用数学 MS+PhD（1967）——**无 CS 学位**；勿把 PhD 年份写错（1967）。
- **博士导师**：页面正文未载导师姓名——勿编造（勿自行补 Math Genealogy 之外的导师名）。
- **Tel Aviv 任职**：是"创始人兼**首任**系主任"（founder and first chair）——勿写成普通教授或写错机构。
- **Weizmann 教授年份**：**1981** 起——勿写早；NYU 兼任 **1999 年起**直至去世——勿写错。
- **死因**：2009-11-02 逝于纽约，死因**脑出血**（brain hemorrhage，页面实载）——仅此一种写法，勿加"心脏病"等。
- **Israel Prize**：**2000 年**、计算机科学（computer science）——勿与图灵奖 1996 混淆；也勿写成"以色列奖"其他类别。
- **No Nobel / 无图灵之外的大奖延伸**：勿编造 Kyoto Prize、 ieee honors 等页面未载荣誉。
- **全文无直接引语**：页面除图灵奖获奖理由外无任何本人直接引语——勿编造"普努利曾说……"。
- **家庭细节**：仅"三个子女、四个孙辈"——父母/配偶页面对照无载，勿渲染。
- **生卒**：1941-04-22 ~ 2009-11-02，享年 68；出生地 Nahalal（时为英国托管巴勒斯坦）——表述"生于英国托管时期的 Nahalal（今以色列）"。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | manifest 为 null，待补 |
| name_zh | 普努利（或 阿米尔·普努利） | 待写入 |
| name_en | Amir Pnueli | 待写入 |
| birth_date | 1941-04-22 | 待写入 |
| death_date | 2009-11-02 | 待写入 |
| nationality | Israel | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | temporal logic / model checking / program and systems verification | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士学生**（infobox 实载）：Mordechai Ben-Ari、Dana Fisman、Nissim Francez、Doron A. Peled、Ofer Strichman、Lenore Zuck
- **博士导师**：页面无载——明写"无载禁写"
- **合作者**：页面未列具名合作者——明写"无载禁写"，勿从其他来源补
- **机构同仁参照**：Stanford（博士后转型）、Tel Aviv / Weizmann / NYU（任职）仅作履历，不作"关系"入库

## 8. 奖项清单

- Turing Award（1996，图灵奖，获奖理由见 §5 红线）
- Uppsala University 荣誉博士（1997-05-30，瑞典，Faculty of Science and Technology）
- 美国国家工程院外籍院士（Foreign Associate of the U.S. NAE，1999）
- Israel Prize（2000，计算机科学）
- ACM Fellow（2007）
- Weizmann Institute 纪念讲座系列以其命名（身后荣誉，非奖项）

## 9. 机构清单

- 教育：Technion（数学 BS）、Weizmann Institute of Science（应用数学 MS、PhD 1967）、Stanford University（博士后，转型 CS）
- 任职：Tel Aviv University（计算机系创始人与首任系主任）、Weizmann Institute（教授，1981 年起）、New York University（1999–2009 兼任至去世）、University of Pennsylvania（副教授）、Joseph Fourier University（副教授）

## 10. 终审清单

- [ ] 生卒 1941-04-22 / 2009-11-02，享年 68，出生地 Nahalal（托管巴勒斯坦→今以色列），去世地纽约
- [ ] 图灵奖获奖理由整句引用无误
- [ ] 博士论文"海洋潮汐、应用数学、1967"表述准确，转型在 Stanford 博士后
- [ ] Tel Aviv"创始人与首任系主任"表述准确
- [ ] Weizmann 1981 / NYU 1999 年份红线
- [ ] 死因仅"脑出血"，无渲染
- [ ] Israel Prize 2000（计算机科学）不与图灵奖混淆
- [ ] 全文无本人直接引语（除获奖理由），无编造导师
- [ ] 国籍用「以色列」，封面底部状态栏 `以色列 | Technion · Weizmann · Tel Aviv · NYU | Turing 1996`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1996/Amir Pnueli/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/Amir_Pnueli.jpg`（实照，已就绪；250px 版 `250px-Amir_Pnueli.jpg` 可作降级）
- [ ] **国籍**：封面顶部徽章明示以色列
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（仅图灵奖理由）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同代图灵奖得主（1997 Engelbart / 1998 Gray）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
