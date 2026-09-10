# Dennis Gabor（丹尼斯·加博尔）立传提示词

> qid=Q155786 · 1900-06-05 – 1979-02-09 · 匈牙利-英国物理学家 / 发明家 · 20 世纪 · 1971 诺贝尔物理学奖（独得）
> 本地 Wikipedia 数据源：`physicist/presentations/20th_century/20th_century/Dennis_Gabor/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家标杆 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**。物理学家立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。肖像用 `images.txt` 中 `Dennis_Gabor_1971.jpg`（1971 年获奖之年肖像），250px 改 500px 下载。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 匈牙利 / 英国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色（诺奖金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「全息干涉条纹 / 波前衍射」母题——可做同心干涉环变体，视觉语言贴合全息术。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。
6. **特殊气质**：电气工程师出身的物理诺奖得主（与 Alfvén 相映）；"超前时代"叙事核心——1947 年的发明要等 1960 年激光问世才真正复兴。

---

## 1. 背景信息（用于 Slide 1-3）

- **本名与改名**：原名 **Günszberg Dénes**（匈牙利语姓名顺序），布达佩斯犹太家庭；1900 年全家改宗信义宗；1902 年获准改姓 Gábor（加博尔）——"Dennis Gabor" 是英文化写法
- **生卒**：1900-06-05 生于布达佩斯（Budapest，奥匈帝国）→ 1979-02-09 逝于伦敦南肯辛顿一家养老院（South Kensington, London），享年 78
- **国籍**：匈牙利 → 英国（1946 年入籍英国公民，1946–1979；生前大半生在英格兰度过）
- **身份**：物理学家、发明家、大学教授、全息术发明人（holographer）；宗教上晚年自认不可知论者（agnostic）
- **家庭**：长子，父 Günszberg Bernát、母 Jakobovits Adél；1936-08-08 与 Marjorie Louise Butler 结婚，无子女
- **一战经历**：曾随匈牙利炮兵在意大利北部服役（一战期间）
- **教育轨迹**：
  - 1918 年入布达佩斯技术与经济大学学工程
  - 转赴德国柏林夏洛滕堡工业大学（Technische Hochschule Charlottenburg，今柏林工业大学 TU Berlin）
  - 1927 年获 PhD，论文 *Recording of Transients in Electric Circuits with the Cathode Ray Oscillograph*（用阴极射线示波器记录电路中的瞬态过程）
- **研究领域**：物理、电子光学、全息术、通信与听觉、时频分析、社会未来学

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **从高压输电线到电子光学**：职业生涯起点是用阴极射线示波器分析高压输电线路特性，由此迷上电子光学，进而研究示波器的基本过程——电子显微镜、电视显像管皆由此而来。
2. **柏林岁月与等离子体灯**：1927 年博士论文之后在德国从事等离子体灯（plasma lamps）研究；1933 年因纳粹上台（在德国被认定为犹太人）逃离德国。
3. **BTH 拉格比岁月**：受邀赴英国 Rugby 的 British Thomson-Houston（BTH）公司发展部工作——全息术发明之地；1936 年在拉格比结识 Marjorie Butler 并结婚；1946 年入籍英国。
4. **全息术的发明（1947，BTH）**：基于电子显微镜的思路（用电子而非可见光成像）发明全息术；实验用强滤波汞弧灯作光源——**诺奖理由的直接依据**。
5. **核心思想：振幅 + 相位**：完美光学成像必须利用全部信息——不仅是常规光学成像的振幅，还有相位，如此才能得到完整的 holo-spatial 图像；1946–1951 年间以系列论文发表其全息理论（注意年份组合，见 §5）。
6. **超前时代：等待激光的十六年**：激光 1960 年问世——第一种相干光源；**1964 年最早的可视全息图**才得以实现，此后全息术走向商业化——1947 年的发明沉睡十余年后复兴，是"超前时代"叙事的核心（时序以 page.md 为准）。
7. **颗粒合成与时频分析**：研究人类如何通信与听觉，成果为颗粒合成（granular synthesis）理论——希腊作曲家 Xenakis 声称自己才是该技术最早发明人（争议如实并陈）；其这方面工作是时频分析发展的基础。Known-for 系列命名：Gabor atom / Gabor filter / Gabor limit / Gabor transform / Gabor wavelet。
8. **帝国理工与维纳的控制论**：1948 年从拉格比转到帝国理工学院，1958 年任应用物理教授至 1967 年退休；1959-03-03 就职演说 "Electronic Inventions and their Impact on Civilisation" 直接启发了维纳 1961 年版《控制论》倒数第二章关于自复制机器的论述。
9. **平板电视的专利战（1958）**：为 CRT 相关研发申请平板电视新概念专利（电子枪垂直于屏面）；与美国同年推出的 Aiken tube 显著相似，引发多年专利战——Aiken 保住美国权利、Gabor 拿下英国；1970 年代被 Sinclair 接手商业化，终因真空管内细丝制造困难而未成。
10. **未来学三书与 Club of Rome**：*Inventing the Future*（1963）提出现代社会的三大威胁——战争、人口过剩、闲暇时代，留下名言"the future cannot be predicted, but futures can be invented"（未来无法预测，但未来可以被发明——page.md 明载，可引）；*Innovations*（1970）；*The Mature Society*（1972）；加入罗马俱乐部，主持能源与技术变迁工作组，成果 *Beyond the Age of Waste*（1978）——对若干问题发出早期预警，多年后才被广泛关注。
11. **1971 诺贝尔奖（独得）**："for his invention and development of the holographic method"；诺奖演说中回顾了 1948 年以来全息术的发展史（**演说标题勿引**，见 §5 页内错误）。
12. **退休岁月**：退休后常住意大利拉维尼奥（Lavinio, 罗马），保持帝国理工 senior research fellow 身份，兼任康涅狄格州 CBS Laboratories 科学家，与终身好友、CBS Labs 总裁 Peter C. Goldmark 合作多项通信与显示新方案。
13. **激光时代的世界声誉**：随激光的迅速发展与全息术的广泛应用（艺术、信息存储、模式识别等），他在生前即获得公认的成功与全世界关注。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（全息深蓝） | `#1F5F7A` | 波前与干涉的深水色 / 帝国理工的工程传统 |
| 强调色（诺奖金） | `#C9A227` | 诺贝尔奖 / 尊崇 |
| 分类色 1（全息 — 干涉青绿） | `#0F8C7F` | 全息术 / 振幅+相位 / 相干光 |
| 分类色 2（电子光学 — 琥珀） | `#B77A26` | 示波器 / 电子显微镜 / 平板电视 |
| 分类色 3（时频分析 — 紫罗兰） | `#6B4FA0` | Gabor 变换 / 颗粒合成 / Gabor 滤波 |
| 分类色 4（未来学 — 玫瑰红） | `#C14A68` | Inventing the Future / 罗马俱乐部 / 成熟社会 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「全息干涉环 / 波前衍射」的视觉语言（可做同心环变体，见 §0.4）。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：纪录片 / 稳重 / "光"的主题（全息术是"用光记录光的全部信息"——曲目名与人物贡献直接呼应）
- **选定曲目**：Infraction **The Invisible Light**（纪录片 / 电影 / 稳重，Inspiring Electronic 合辑）。
- **落地文件**：`physicist/presentations/20th_century/Dennis_Gabor/The-Invisible-Light.wav`（复制自音乐库 `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`，不入 git）。
- **匹配理由**：曲目名 "The Invisible Light"（不可见之光）与全息术"把相位这一不可见信息变为可见"的物理内核高度同构；纪录片气质匹配"1947 发明沉睡十余年、1960 激光唤醒"的缓慢复兴叙事。
- **组内查重**：本批次五人曲目互不重复（PAST / Eternals / SEA / Timeless / The Invisible Light）。

## 4. Slide 规划（约 15 页，Wilson 式结构）

1. **封面**（`\titleslide`）：顶部标签「全息术之父 · 匈牙利/英国」+ Gabor 1900–1979 + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 Günszberg Dénes / 国籍 / 出生地 / 去世地 / 教育 / 任职 / 主要荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：全息术 / 电子光学与时频分析 / 发明家的专利世界 / 未来学与社会批判
4. **早年：布达佩斯与柏林**（1900–1933）：Günszberg 改姓 Gábor、一战炮兵、示波器博士论文、等离子体灯
5. **逃离纳粹德国**（1933）：赴英、BTH 拉格比、1936 结婚、1946 入籍英国
6. **全息术的发明**（1947）：电子显微镜思路、汞弧灯实验、"振幅 + 相位"核心思想
7. **系列论文与理论化**（1946–1951）：holo-spatial 完整成像、时序细节见 §5
8. **等待激光的十六年**：1960 激光 → 1964 最早可视全息图 → 商业化——"超前时代"叙事页
9. **帝国理工岁月**（1948–1967）：应用物理教授、1959 就职演说启发维纳《控制论》
10. **时频分析与颗粒合成**：Gabor 变换 / filter / limit / wavelet、Xenakis 争议并陈
11. **平板电视专利战**（1958）：Aiken tube、英美分权、Sinclair 尝试与失败
12. **1971 诺贝尔奖（独得）**：获奖理由（发明并发展全息术方法）、诺奖演说回顾全息发展史
13. **未来学三书与罗马俱乐部**：Inventing the Future（三大威胁 + 名言）、The Mature Society、Beyond the Age of Waste
14. **荣誉与身后纪念**：FRS 1956、Young Medal 1967、Rumford 1968、IEEE Medal of Honor 1970、CBE 1970、诺奖 1971、Holweck 1972；身后——SPIE Dennis Gabor Award（1983）、皇家学会 Gabor Medal（1989）、小行星 72071 Gábor（2000）、蓝牌匾（2006）、IOP Dennis Gabor Medal（2008）、Gabor Hall（2009）、Dennis Gabor University（布达佩斯）
15. **结尾**：78 岁、"未来无法预测，但未来可以被发明"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **死亡日期噪声**：metadata.json 的 date_of_death 同时有 "1979-02-09" 与 "1979-02-08"，**以 page.md 为准：1979-02-09**，享年 78。
- **全息术年份组合（最易错处）**：发明于 **1947 年（在 BTH 工作期间）**；理论系列论文发表于 **1946–1951**（两处年份并存，page.md 如此，勿强行统一）；1948 年他离开拉格比赴帝国理工；**1960 年激光问世；1964 年最早的可视全息图实现**——"沉睡十余年"表述以这条时间链为准，勿写"1948 年发明全息"或"获奖即复兴"。
- **诺奖演说标题勿引**：page.md 外部链接一节写 "Nobel Lecture, 11 December 1970 *Magnetism and the Local Molecular Field*"——这是 **Néel 条目的演说标题**，属本页面的复制粘贴错误；正文只写"他在诺奖演说中回顾了 1948 年以来全息术的发展史"，标题一律不引。
- **国籍表述**：匈牙利-英国（Hungarian-British）；1946 年入英国籍（citizenship 栏：Hungary; UK 1946–1979）；封面写「匈牙利 / 英国」，勿写"英国籍匈牙利裔物理学家"之外的引申。出生地当时属**奥匈帝国**。
- **本名**：Günszberg Dénes（匈牙利语姓前名后），1902 年全家改姓 Gábor——身份信息页"本名"格照此写，勿写成 "Dennis Gábor Dénes" 之类的混合体。
- **颗粒合成优先权争议**：Xenakis 声称自己是颗粒合成最早发明人——如实并陈"Gabor 的研究结果是颗粒合成理论 / Xenakis 声称最早发明"，不作裁决。
- **平板电视结局**：Sinclair 的商业化因真空管内多细丝制造困难"从未成功"——如实写失败结局，勿写成"Gabor 发明了平板电视（成功）"。
- **引语白名单**（page.md 有载原文）：①"the future cannot be predicted, but futures can be invented"（《Inventing the Future》，page.md 标注"now well-known expression"，可引）；②Nigel Calder 对该概念的转述。其余一律间接转述。
- **纳粹德国逃离**：page.md 一句带过（"1933 年逃离纳粹德国，在德国他被认定为犹太人"）——按此呈现，不展开渲染。
- **宗教背景**：犹太家庭出身、1900 年改宗信义宗、晚年不可知论——身份页可一笔带过，不展开。
- **诺奖为 1971 年独得**（single recipient）——本批次无同届共享者；诺奖理由用总名单中文表述"表彰他发明并发展全息术方法"。
- **生卒确认**：1900-06-05 / 1979-02-09（享年 78）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q155786 | 待写入 |
| name_zh | 加博尔（或 丹尼斯·加博尔） | 待写入 |
| name_en | Dennis Gabor | 待写入 |
| birth_date | 1900-06-05 | 待写入 |
| death_date | 1979-02-09（metadata 有 1979-02-08 噪声，以 page.md 为准） | 待写入 |
| nationality | Hungary; United Kingdom（1946–1979） | 待写入 |
| primary_occupation | physicist（inventor / holographer） | 待写入 |
| field_of_work | physics（电子光学 / 全息术 / 时频分析 / 未来学） | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：page.md 未载——**禁建**导师关系
- **著名博士生**：Eric Ash、Anthony G. Constantinides（metadata 亦列 Jack Cowan，page.md 未载——以 page.md/infulist 两人为准，Jack Cowan 若入库须注明"仅 metadata"）
- **终身好友/合作者**：Peter C. Goldmark（CBS Labs 总裁，通信与显示方案合作）
- **专利对手**：Hancock Aiken（Aiken tube 平板电视专利战——英/美分权结局，建 controversy 关系可选）
- **学术思想受其启发**：Norbert Wiener（1959 就职演说启发《控制论》1961 版自复制机器章节）
- **优先权争议**：Iannis Xenakis（颗粒合成最早发明人之争，如实并陈）
- ** Club of Rome 同事**：Umberto Colombo、Alexander King、Ricardo Galli（《Beyond the Age of Waste》合著者）
- **纪念关系（以其命名）**：SPIE Dennis Gabor Award（1983）、皇家学会 Gabor Medal（1989）、Dennis Gabor University 布达佩斯（1992）、NOVOFER International Dennis Gabor Award（1993）、IOP Dennis Gabor Medal and Prize（2008）、小行星 72071 Gábor（2000）
- **诺贝尔奖同届**：1971 年由 Gabor **独得**

## 8. 奖项清单

- 诺贝尔物理学奖（1971，独得——发明并发展全息术方法）
- Fellow of the Royal Society（FRS，1956）
- 匈牙利科学院荣誉院士（1964）、伦敦大学 D.Sc.（1964）
- Young Medal and Prize（1967，光学领域卓越研究）
- Columbus Award, International Institute for Communications, Genoa（1967）
- Albert A. Michelson Medal（1968，富兰克林学会**首枚**）
- Rumford Medal, Royal Society（1968）
- 荣誉博士：南安普顿大学（1970）、代尔夫特理工（1971）
- IEEE Medal of Honor（1970）
- Commander of the Order of the British Empire（CBE，1970）
- Holweck Prize, Société Française de Physique（1972）
- 美国光学学会荣誉会员（1972）
- National Inventors Hall of Fame（仅 metadata 奖项列表有、page.md 未列年份——若收录须注明）

## 9. 机构清单

- 教育：布达佩斯技术与经济大学（1918 起）；柏林夏洛滕堡工业大学（今 TU Berlin，PhD 1927）
- 任职：British Thomson-Houston（BTH）公司发展部，Rugby（1933–1948，全息术发明地）
- 帝国理工学院（1948 起；1958 年任应用物理教授，1967 年退休；退休后任 senior research fellow）
- CBS Laboratories（Stamford, Connecticut，staff scientist，与 Goldmark 合作）
- 退休居所：意大利拉维尼奥（罗马）
- 纪念地点：伦敦南肯辛顿 79 Queen's Gate 蓝牌匾（1949 年至 1960 年代初居所）；Imperial College Gabor Hall（2009）；波茨坦 Dennis-Gabor-Straße；布达佩斯 Dennis Gabor University（前身 Gábor Dénes College）

## 10. 终审清单

- [ ] 生卒 1900-06-05 / 1979-02-09，享年 78，出生地 Budapest（奥匈帝国），去世地 London
- [ ] 本名 Günszberg Dénes 与 1902 改姓 Gábor 表述准确
- [ ] 全息时间链：1947 发明（BTH）→ 1946–1951 系列论文 → 1960 激光 → 1964 最早可视全息图
- [ ] 诺奖理由用总名单中文表述（发明并发展全息术方法），1971 独得
- [ ] 诺奖演说标题不引（page.md 该处为 Néel 条目串页错误）
- [ ] Xenakis 颗粒合成争议、Aiken 专利战、平板电视失败结局均如实中性呈现
- [ ] 引语只用 "the future cannot be predicted, but futures can be invented" 白名单
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `20th_century/Dennis_Gabor/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images.txt` 中真实肖像（Dennis_Gabor_1971.jpg，250px 改 500px 下载）
- [ ] **国籍**：封面顶部徽章明示匈牙利 / 英国
- [ ] **引语核对**：引语必须在 page.md 原文找到（名言一条白名单）
- [ ] **全息时间链复核**：1947 / 1946–1951 / 1960 / 1964 四个年份逐一对照原文
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一（半角引号 " "；变音字母 Gábor / Dénes 排版正常）
- [ ] 与同世纪物理学家（Heisenberg / Landau / Planck）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
