# Charles H. Bennett（查尔斯·贝内特）立传提示词

> qid=Q92931 · 1943 –（在世，卒日留白） · 美国物理学家、信息论学家（IBM Fellow） · 20/21 世纪 · 2025 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2025/Charles H. Bennett (physicist)/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**有真实肖像**（`Dr._Charles_Bennett_IBM_Fellow.jpg`，见 §11）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（如 BB84 四态偏振示意 / 可逆计算幺正门示意 / teleportation 双通道示意），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Charles Henry Bennett（中文惯称：查尔斯·贝内特）
- **生卒**：1943 年生于纽约市（New York City；页面仅载年份"1943 (age 82–83)"，**无出生月日，勿编造**）→ **在世，卒日留白**
- **国籍**：美国（American）
- **身份**：物理学家、信息论学家、**IBM Fellow**（IBM Research）；现代量子信息理论**奠基人之一**（页面原载 "one of the founding fathers of modern quantum information theory"）
- **教育轨迹**：
  - Brandeis University：**化学** BS（1964）
  - Harvard University：**PhD（1970）**——分子动力学研究（分子运动的计算机模拟），导师 **David Turnbull 与 Berni Alder 两人**
- **早期经历**：在 Harvard 曾为 James Watson（DNA 双螺旋发现者）做一年遗传密码方向助教；后在 Argonne National Laboratory（University of Chicago 运营）随 Aneesur Rahman 继续该研究两年
- **Known for**（页面实载列表，择用）：quantum teleportation、quantum cryptography、quantum computing、entanglement distillation、reversible computing、overlapping distribution method、logical depth、superdense coding、**BB84**、Bennett's laws、Bennett acceptance ratio
- **研究领域**：计算机科学、量子信息

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **化学学士的物理学家**：Brandeis 化学 BS（1964）→ Harvard 分子动力学博士（1970，双导师 Turnbull + Alder）——"计算模拟分子运动"的博士训练预示了其后"物理 × 信息"的一生。
2. **Watson 与 Argonne 岁月**：在 Harvard 为 James Watson 做一年遗传密码助教；随 Aneesur Rahman 在 Argonne 从事分子动力学两年（1970–1972）。
3. **1972 年加入 IBM Research**（Thomas J. Watson Research Center）——此后一生 IBM，1995 年获评 **IBM Fellow**。
4. **可逆计算（1972–）**：在 IBM 的 **Rolf Landauer** 工作基础上，证明**通用计算可由逻辑与热力学上可逆的装置完成**——可逆计算的开山贡献（Landauer 是思想源头非导师，勿写成师承）。
5. **Maxwell's demon 重释（1982）**：提出对麦克斯韦妖的新诠释——妖无法打破第二定律的原因在于**摧毁（而非获取）信息的热力学成本**；同领域重要论文 *The thermodynamics of computation—a review*（1982, Int. J. Theor. Phys.）。
6. **Bennett acceptance ratio 方法**：估计两系统自由能差的重要方法（分子模拟领域实载成果）。
7. **逻辑深度（logical depth）**：在算法信息论中，用"通用计算机从随机初态模拟出该物理状态演化所需的时间"定义物理状态的内在复杂性——信息与随机性的通用计算刻画。
8. **BB84（1984，与 Brassard）**：与蒙特利尔大学的 **Gilles Brassard** 合作、**建立在 Stephen Wiesner 的理念之上**，发展出量子密码系统 BB84——利用**不确定性原理**，让**初始不共享任何秘密**的双方实现安全通信。
9. **世界首个量子密码工作演示（1989）**：在 **John Smolin** 协助下建成（页面原载 "the world's first working demonstration of quantum cryptography in 1989"）。
10. **量子遥控传态（quantum teleportation，1993）**：Bennett 与 Brassard 联合他人"发现"——未知量子态的完整信息被分解为**纯经典信息**与**纯非经典的 EPR 关联**，经两条独立信道传输后在异地重组出原量子态的精确副本，原态在发送过程中被销毁（1993 年 Bennett-Brassard 篇章的核心机制描述归本篇）。
11. **噪声信道与纠缠蒸馏（1995–1997）**：与 Smolin、Wootters、DiVincenzo 等合作，提出经典与量子信息经噪声信道忠实传输的多种技术；共同提出**纠缠蒸馏（entanglement distillation）**概念。
12. **Bennett's four laws of quantum information**：页面提及（"see Bennett's four laws of quantum information"）——**提及名称即可，勿自行演绎四条内容**。
13. **荣誉**：APS Fellow、NAS 院士、IBM Fellow（1995）、Harvey Prize、Rank Prize、Dirac Medal（ICTP 2017）、Wolf Prize in Physics（2018）、BBVA Frontiers of Knowledge（2019）、Shannon Award（2019）、Breakthrough Prize in Fundamental Physics（2023）、Eduard Rhein Foundation Prize in Technology（2023）；**2025 图灵奖**（2026-03 公布，与 Brassard 共享，理由见 §5）。
14. **博客《The Quantum Pontiff》**：与 Steve Flammia、Aram Harrow 合写、Dave Bacon 托管——一笔带过即可。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（可逆计算与热力学 — 蓝） | `#2E5A9E` | Landauer 路线 / Maxwell's demon |
| 分类色 2（量子密码 BB84 — 青绿） | `#1E8E8E` | BB84 / 1989 首个演示 |
| 分类色 3（算法信息论 — 琥珀） | `#D9A441` | logical depth / Bennett acceptance ratio |
| 分类色 4（量子态操控 — 玫瑰） | `#C0395B` | teleportation / entanglement distillation / superdense coding |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：干涉条纹（稀疏同心弧线），呼应「偏振态叠加与不确定性原理」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：幽微 / 神秘（量子态不可见却承载信息）
- **选定曲目**：Alex-Productions **The Invisible Light**（manifest 预分配，直接沿用），曲目名与"不可见的量子之光"高度契合。
- **落地文件**：`turing/presentations/Charles_H._Bennett/TheInvisibleLight.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「量子信息奠基人 · 美国」+ Bennett 1943–（在世）+ 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1943–至今 生平纵览
4. **早年：纽约与 Brandeis 化学**（1943–1964）：化学 BS 起点
5. **Harvard 博士与 Watson/Argonne 岁月**（1964–1972）：分子动力学、双导师、遗传密码助教
6. **IBM 与 Landauer：可逆计算**（1972–）：逻辑与热力学可逆的通用计算
7. **Maxwell's demon 重释（1982）**：摧毁信息的热力学成本；热力学计算综述
8. **Bennett acceptance ratio 与逻辑深度**：自由能差估计、物理状态的内在复杂性
9. **BB84：量子密码的诞生**（1984）：与 Brassard、Wiesner 理念、不确定性原理、无预共享秘密的安全通信
10. **1989：世界首个量子密码工作演示**：与 John Smolin
11. **量子遥控传态（1993）**：经典信道 + EPR 关联双通道、原态销毁的机制描述
12. **噪声信道与纠缠蒸馏（1995–1997）**：Smolin/Wootters/DiVincenzo 合作
13. **荣誉**：IBM Fellow 1995 / Harvey 2008 / Rank 2006 / Dirac 2017 / Wolf 2018 / BBVA & Shannon 2019 / Breakthrough & Eduard Rhein 2023
14. **2025 图灵奖**：与 Brassard 共享、ACM citation 整句
15. **结尾**：物理与信息的摆渡人、量子信息时代的奠基

## 5. 史实陷阱与敏感点（终审必须检查）

- **出生日期**：页面仅载"1943 (age 82–83)"，**无出生月日**——写作 `b. 1943`，勿编造精确日期。
- **在世**：Bennett 在世，**死亡日期一律留白**。
- **奖项年份冲突（本篇最大疑点）**：infobox 列 "Harvey Prize (2006)"，正文写"awarded the **2008** Harvey Prize by the Technion and the **2006** Rank Prize in opto-electronics"——**以正文为准：Harvey 2008、Rank 2006**；Review-1 必核。
- **Breakthrough Prize 年份**：Bennett 页正文写 2023（Brassard 页写 2022-09 公布）——统一口径"**2023 届 Breakthrough Prize in Fundamental Physics（2022 年 9 月公布）**"，两篇保持一致。
- **学位口径**：Brandeis BS 是**化学**（1964）——勿写成物理学位；Harvard PhD 1970 是**分子动力学**（分子运动的计算机模拟），非量子信息——勿倒填。
- **双导师**：博士导师 **David Turnbull 与 Berni Alder 两人**（infobox 实载）——勿只写一个。
- **Watson 关系**：在 Harvard 为 James Watson 做**一年助教**（遗传密码方向）——写"曾为其助教"，勿写成"师从 Watson"或"与其共研双螺旋"。
- **Landauer 定位**：Rolf Landauer 是可逆计算的思想源头（Bennett "built on the work of"）——写"在其基础上证明"，勿写成 Bennett 的导师。
- **Wiesner 定位**：BB84 "building on an idea of Stephen Wiesner"——按实载提及理念来源，勿夸大也勿省略。
- **teleportation 归属**：1993 年"Bennett and Brassard, in collaboration with others, discovered"——是**共同发现**，勿写成 Bennett 独创或纯实验成就（该页描述为效应/方案，勿写"完成首次实验传送"）；Brassard 篇侧重 1993 PRL 六作者论文署名，本篇侧重机制描述。
- **Bennett's four laws**：页面仅给名称链接——**禁自行编造四条内容**。
- **获奖理由**（ACM citation，页面实载）："for work on the foundations of quantum information science and secure communication and computing"——整句引用，与 Brassard 篇一致；获奖口径"**2025 年图灵奖（2026 年 3 月公布）**"。
- **引语边界**：正文唯一的"引语"是 Bennett 回忆 Asher Peres 的信件内容（2005-01 致家属慰问信，其中 Peres 的笑话为转引）——**可用性存疑，建议不写**；若必写须逐字标注"出自 Bennett 致 Peres 家属的信（2005 年 1 月）"且一笔带过。除此之外全文无其他直接引语，勿编造。
- **私人细节**：Bennett 自认无神论者（页面实载）——一笔带过或不写，不渲染。
- **博客**：The Quantum Pontiff（与 Flammia、Harrow 合写、Bacon 托管）——花絮页一笔带过，勿列为核心贡献。
- **Known for 列表**：superdense coding / overlapping distribution method / Bennett's laws 等页面仅列名——可列荣誉墙式短语，勿展开未经页面支持的技术叙述。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 贝内特（或 查尔斯·贝内特） | 待写入 |
| name_en | Charles H. Bennett | 待写入 |
| birth_date | 1943（无月日） | 待写入 |
| death_date | （在世留白） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | physicist（兼 information theorist） | 待写入 |
| field_of_work | quantum information / quantum cryptography / reversible computing | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：David Turnbull、Berni Alder（Harvard，infobox 实载双导师）
- **博士后指导**：Aneesur Rahman（Argonne，两年；标注 postdoc-advisor，禁写成博士导师）
- **合作者**：Gilles Brassard（BB84 / teleportation / 2025 图灵奖共享者）；John Smolin（1989 首个演示、噪声信道）；Wootters、DiVincenzo（噪声信道/纠缠蒸馏）；Steve Flammia / Aram Harrow / Dave Bacon（博客合作，可选）
- **思想先驱**：Rolf Landauer（可逆计算思想源头，influence）；Stephen Wiesner（BB84 理念来源，influence）
- 其余关系页面无载，禁写。

## 8. 奖项清单

- Turing Award（2025，与 Gilles Brassard 共享；2026-03 公布；citation 见 §5）
- IBM Fellow（1995）
- Rank Prize in opto-electronics（2006，正文口径）
- Harvey Prize（Technion，2008，正文口径；infobox 作 2006 系冲突，以正文为准）
- Dirac Medal（ICTP，2017）
- Wolf Prize in Physics（2018）
- BBVA Foundation Frontiers of Knowledge Award in Basic Sciences（2019）
- Claude E. Shannon Award（2019）
- Breakthrough Prize in Fundamental Physics（2023 届，2022-09 公布）
- Eduard Rhein Foundation Prize in Technology（2023）
- Fellow: American Physical Society；Member: National Academy of Sciences

## 9. 机构清单

- 教育：Brandeis University（化学 BS 1964）、Harvard University（PhD 1970）
- 任职：Argonne National Laboratory（1970–1972，博士后）→ IBM Research / Thomas J. Watson Research Center（1972– 至今；1995 年获评 IBM Fellow）

## 10. 终审清单

- [ ] 生卒 1943（无月日）/ 在世留白
- [ ] Brandeis 化学 BS 1964、Harvard 分子动力学 PhD 1970、双导师 Turnbull+Alder
- [ ] Watson=一年助教、Rahman=Argonne 博士后，均勿升格为导师
- [ ] Landauer=思想源头、Wiesner=BB84 理念来源，均按"built on"实载表述
- [ ] Maxwell's demon 1982=摧毁信息的成本，表述准确
- [ ] BB84 1984 + 1989 首个工作演示（与 Smolin）年份准确
- [ ] teleportation 1993=共同发现，机制描述照页面，勿写实验实现
- [ ] Harvey 2008 / Rank 2006（以正文为准，infobox 冲突已裁定）
- [ ] 获奖口径"2025 图灵奖（2026-03 公布）"，citation 整句引用
- [ ] Bennett's four laws 仅提名称，不演绎内容
- [ ] 封面头像 `Dr._Charles_Bennett_IBM_Fellow.jpg`，底部状态栏 `美国 | IBM Research | Turing 2025`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2025/Charles H. Bennett (physicist)/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-Dr._Charles_Bennett_IBM_Fellow.jpg`（IBM Fellow 正装照，已就绪；勿误用 `Question_book-new.svg.png`）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：仅 ACM citation 为必引；Peres 信件引语默认不写，若写须逐字核对出处
- [ ] **奖项年份**：Harvey 2008 / Rank 2006 / Breakthrough 2023 届口径复核
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与共享奖同伴 Brassard 篇格式对齐、侧重不重复

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
