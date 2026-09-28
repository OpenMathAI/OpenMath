# Jack S. Kilby（杰克·基尔比）立传提示词

> qid=Q182031 · 1923-11-08 – 2005-06-20 · 美国电气工程师 · 20 世纪 · 2000 诺贝尔物理学奖
> 本地 Wikipedia 数据源：`physicist/presentations/20th_century/20th_century/Jack_S._Kilby/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家标杆 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**。物理学家立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。**Kilby 无真实肖像可用**（images.txt 中 `Kilby_solid_circuit.jpg` 是他 1958 年的第一块集成电路照片，**不是人物肖像**）——封面与身份页用**装饰圆占位**（`\faIcon{user}\enspace Portrait`）；IC 照片可另用于"发明"叙事页作实物插图。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、任职、主要荣誉、核心领域（Kilby 无博士导师栏，写"无（工业界发明家路线）"）。
4. **配色 + 气泡背景**：主色 + 强调色（诺奖金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「把电路缩进一块芯片」母题。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Jack St. Clair Kilby（杰克·圣克莱尔·基尔比）
- **生卒**：1923-11-08 生于杰斐逊城（Jefferson City，密苏里州，美国）→ 2005-06-20 逝于达拉斯（Dallas，得克萨斯州，美国），享年 81（癌症）
- **国籍**：美国
- **身份**：电气工程师、发明家、大学教师（Texas A&M 杰出教授）、摄影师、物理学家
- **少年往事**：在堪萨斯州大本德（Great Bend）长大，父亲经营服务堪萨斯西部乡村的小电力公司；高中时一场大冰暴摧毁电话与电力线杆，父亲靠业余无线电爱好者维持通信——这场灾难点燃了他对电子学的兴趣
- **服役与教育**：
  - 二战期间任美国陆军电子技术员
  - 1947 年获伊利诺伊大学（University of Illinois）电气工程学士（B.S.）
  - 入职密尔沃基 Centralab Division of Globe Union 期间半工半读，1950 年获密尔沃基州立师范学院（今威斯康星大学密尔沃基分校）硕士（M.S.）
- **师承**：无博士导师（工业界发明家路线，非学院派）
- **家庭**：1948 年与 Barbara Annegers 结婚，两女 Ann 与 Janet
- **任职主线**：Texas Instruments（1958 加入；1970 休假独立发明；1983 退休）、Texas A&M University（1978–1984 电气工程杰出教授）
- **领域**：电气工程、物理、集成电路、微电子

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **冰暴与业余无线电**（1930s）：堪萨斯乡村大冰暴、父亲公司的应急电台——一个工程师家庭少年的电子学启蒙。
2. **战后工程师之路**（1945–1958）：陆军电子技术员 → 伊利诺伊学士（1947）→ 密尔沃基 Centralab 半工半读硕士（1950）——非学院派的工业路线。
3. **1958 夏：新员工的"无假之夏"**：初入德州仪器（TI）还没资格休年假，整个夏天泡在"数字暴政"（tyranny of numbers）难题里——电路元件数量爆炸、手工连线不可持续。
4. **结论：一块半导体上的批量元件**：他断定在单块半导体材料上成批制造电路元件才是出路——用**锗**造出第一块集成电路。
5. **1958-09-12 历史性演示**：向公司管理层（含 Mark Shepherd）展示一块接上示波器的锗片——按下开关，屏幕出现连续正弦波：集成电路真的工作了。
6. **U.S. Patent 3,138,743**："Miniaturized electronic circuits"（小型化电子电路），**1959-02-06 提交**——第一项集成电路专利，关键在"晶体管、二极管、电阻、电容同处单一衬底"。
7. **双雄并立：与 Robert Noyce**：Fairchild 半导体的 Robert Noyce **数月后**独立做出类似电路——"Kilby 一般被认为是集成电路的共同发明人（co-inventor）"（page.md 原话口径）；两人共同分享 1989 年 Draper Prize（获奖理由用 "their independent development of the monolithic integrated circuit"）。
8. **手持计算器与热打印机**：与 Jerry Merryman、James Van Tassel 共同发明手持计算器；热打印机共同发明人；另有七项其他专利。
9. **微芯片应用拓荒**：领军团队造出首个 incorporating IC 的军用系统与首台用 IC 的计算机——军用、工业、商用三条线铺开。
10. **独立发明人与教授**（1970–1984）：1970 年离开 TI 岗位休假，探索太阳能硅技术发电等课题；1978–1984 任 Texas A&M 电气工程杰出教授；1983 年从 TI 退休。
11. **2000 诺贝尔物理学奖**："for his part in the invention of the integrated circuit"（表彰他在集成电路发明中的贡献）——独得当年一半，另一半由 Alferov 与 Kroemer 共享。
12. **荣誉之列**：Ballantine 奖章（1966）、IEEE Sarnoff 奖（1966）、美国国家科学奖章（1969，尼克松授予）、IEEE 荣誉奖章（1986）、Draper Prize（1989）、国家技术奖章（1990，老布什授予）、计算机先驱奖（1993）、京都奖先进技术部门（1993）、华盛顿奖（1999）、Harold Pender 奖（2000）。
13. **身后纪念**：Kilby 奖基金会（1980）、IEEE Jack S. Kilby 信号处理奖章（1995 设立）、TI 的 Kilby Labs、爱丁堡龙比亚大学 Jack Kilby 计算机中心、得州大学达拉斯分校 TI 广场的雕像、大本德 Barton 社区学院年度 Jack Kilby STEM Day；手稿与照片捐赠南卫理公会大学（SMU）DeGolyer 图书馆，2008 年 SMU 联合国会图书馆举办"数字时代诞生 50 周年"纪念。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（硅晶深灰蓝） | `#37474F` | 集成电路 / 硅与锗的工程质感 |
| 强调色（诺奖金） | `#C9A227` | 诺贝尔奖 / 尊崇 |
| 分类色 1（集成电路 — 青灰蓝） | `#468189` | 第一块 IC / 专利 3,138,743 |
| 分类色 2（发明生涯 — 赭石） | `#B0713A` | 手持计算器 / 热打印机 |
| 分类色 3（应用拓荒 — 橄榄） | `#6B705C` | 军用系统 / 计算机 / 太阳能 |
| 分类色 4（荣誉与纪念 — 玫瑰灰） | `#7D4E57` | 诺奖 / 国家奖章 / 身后纪念 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「晶体管/电阻/电容同处一芯 / 微观世界宏观影响」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：英雄 / 史诗 / 伟大成就（一项改变文明形态的工程发明）
- **选定曲目**：Really Slow Motion & Giant Apes **Winds Of Freedom**（管弦 / 英雄 / 史诗），匹配"集成电路改变世界"的宏大成就叙事。
- **落地文件**：`physicist/presentations/20th_century/Jack_Kilby/WindsOfFreedom.wav`（复制自音乐库，不入 git）。
- **匹配理由**：Kilby 的叙事核心是"工程师的胜利"——数字暴政的困局被一块锗片破解、信息时代自此发端，英雄管弦气质与其"伟大成就 + 片尾升华"的定位契合；组内五人 BGM 不雷同。

## 4. Slide 规划（约 15 页，Wilson 式结构）

1. **封面**（`\titleslide`）：顶部标签「集成电路 · 美国」+ Kilby 1923–2005 + 右上装饰圆占位 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像（装饰圆）+ 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 任职 / 主要荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：集成电路发明 / 手持计算器 / 微芯片应用拓荒 / 荣誉与纪念
4. **堪萨斯冰暴与电子学启蒙**（1923–1945）：大本德、父亲的电力公司、业余无线电
5. **战后工程师之路**（1945–1958）：陆军、伊利诺伊、密尔沃基半工半读
6. **1958 夏：无假之夏与"数字暴政"**：TI 新员工、批量制造电路元件的断想
7. **1958-09-12：锗片上的正弦波**：历史性演示、第一块集成电路（插图：Kilby_solid_circuit.jpg）
8. **专利 3,138,743**（1959-02-06）："Miniaturized electronic circuits"、单一衬底多元件
9. **双雄并立：Kilby 与 Noyce**：数月之差的独立发明、"co-inventor"口径、1989 Draper Prize 的 "their independent development"——平衡呈现
10. **2000 诺贝尔奖**："for his part in the invention of the integrated circuit"、独得一半 + Alferov/Kroemer 共享另一半
11. **手持计算器与热打印机**：与 Merryman、Van Tassel 的三人组、另七项专利
12. **微芯片应用拓荒**：首个 IC 军用系统与 IC 计算机、太阳能探索（1970 独立发明人岁月）
13. **教授与退休**（1978–1983–2005）：Texas A&M 杰出教授、TI 退休、SMU 捐赠
14. **荣誉与身后纪念**：国家科学奖章/国家技术奖章、IEEE 荣誉奖章、京都奖；Kilby Labs / 小行星之外的纪念地标
15. **结尾**：81 岁、"把世界装进一块芯片的工程师"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **双雄平衡（本篇第一红线）**：page.md 首段即写 Kilby "took part, **along with Robert Noyce** of Fairchild Semiconductor, in the realization of the first integrated circuit"，且明文 "Kilby is generally credited as **co-inventor** of the integrated circuit"——**必须双雄并立呈现，勿写成 Kilby 独享发明**；Noyce 的表述限于 page.md 实载："数月后独立做出类似电路"。
- **无载禁写**：page.md 未载 Noyce 的"硅 + 平面工艺"细节、未载两人专利诉讼与庭外和解、未载"诺奖百年 + 千禧年"的评论、未载 Kilby 获奖感言——正文一律禁写（Noyce 工艺细节与诉讼可在本陷阱表注明"不展开"）。
- **诺奖理由精确口径**："For his part in the invention of the integrated circuit"——**"his part"（他在发明中的那一份贡献）**措辞本身就是委员会对双雄格局的回应；总名单中文表述"表彰他在集成电路发明中的贡献"。份额：Kilby 独得一半，Alferov 与 Kroemer 共享另一半。
- **年份三线勿混**：1958-09-12 **演示**（锗 + 示波器正弦波）→ 1959-02-06 **专利提交**（U.S. Patent 3,138,743）→ 2000 **诺奖**——演示年与专利年勿互换。
- **材料口径**：第一块 IC 用**锗**——"硅"只出现在 1970 年代他的太阳能探索与 TI Kilby Labs 描述中，勿写"用硅造出第一块 IC"。
- **计算器归属**：手持计算器是与 **Jerry Merryman、James Van Tassel 三人共同**发明——勿写"Kilby 独自发明计算器"；热打印机为共同发明、另有七项专利。
- **引语红线**：page.md **无任何 Kilby 直接引语**——全文不得出现加引号的"Kilby 原话"，全部间接转述；"tyranny of numbers" 是通用术语名（可保留原文并加注"数字暴政"），不是引语。
- **肖像 vs 实物照**：`Kilby_solid_circuit.jpg` 是 1958 年第一块 IC 的实物照片——只可作发明叙事页插图，**不可当肖像**；封面/身份页用装饰圆占位。
- **教育口径**：学士伊利诺伊大学（1947）、硕士密尔沃基州立师范学院（1950，今 UW–Milwaukee）——metadata.json 另列 UW–Madison（1990 荣誉博士）与 Great Bend High School，勿混淆学历与荣誉学位。
- **卒因**：2005-06-20 癌症逝于达拉斯，享年 81——从简。
- **先驱归属注**：集成电路先驱另有 Geoffrey Dummer（仅见 page.md See also）——正文不展开，可在陷阱表注明"不展开"。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q182031 | 待写入 |
| name_zh | 基尔比（或 杰克·基尔比） | 待写入 |
| name_en | Jack S. Kilby | 待写入 |
| birth_date | 1923-11-08 | 待写入 |
| death_date | 2005-06-20 | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | electrical engineer | 待写入 |
| field_of_work | electrical engineering / integrated circuits | 待写入 |
| has_biography | 本次入库置 0（Beamer 立传完成后由主控置 1） | 待执行 |

## 7. 社会关系入库清单（已按 page.md 核对，✅=yaml 入库 / ✗=不入库）

- ✅ **共同发明人**：Robert Noyce（colleague；类型白名单无 co-inventor，用 colleague + note 注明双雄格局与 1989 Draper Prize 共享；"1990 去世未获诺奖"仅为背景不入 note 关系方向）
- ✅ **计算器三人组**：Jerry Merryman、James Van Tassel（各一条 colleague，手持计算器共同发明人，page.md 明载）
- ✅ **诺奖同届另一半**：Zhores I. Alferov、Herbert Kroemer（各一条 co-honored，page.md 注 3 明载 "Shared with Zhores Alferov and Herbert Kroemer"）
- ✅ **配偶**：Barbara Annegers（spouse，1948 年结婚，page.md Family 节明载）
- ✗ **授奖渊源**：Richard Nixon（1969 国家科学奖章）、George H. W. Bush（1990 国家技术奖章）——颁奖人为奖项程序事实，不建关系
- ✗ **机构**：Texas Instruments、Texas A&M University——机构非人物关系，不入 person_relation
- ✗ **子女**：Ann、Janet——page.md 仅载名无姓，规范全名不可得，不入库

## 8. 奖项清单

- 诺贝尔物理学奖（2000，独得一半；理由 "For his part in the invention of the integrated circuit"）
- Stuart Ballantine Medal（1966，"单片集成电路（微芯片）的发展"）
- IEEE David Sarnoff Award（1966）
- 美国国家科学奖章（1969，尼克松授予）
- IEEE Cledo Brunetti Award（1978）
- Holley Medal（1982、1989，ASME）
- IEEE Medal of Honor（1986，"半导体集成电路技术的奠基性贡献"）
- Charles Stark Draper Prize（1989，与 Noyce 共享，"their independent development of the monolithic integrated circuit"）
- Robert Henry Thurston Lecture Award（1990，ASME）
- 美国国家技术奖章（1990，老布什授予）
- Computer Pioneer Award（1993，IEEE 计算机学会，"co-inventing the integrated circuit"）
- 京都奖先进技术部门（1993）
- Washington Award（1999）
- Harold Pender Award（2000）
- NAE 成员（1967）、美国哲学会成员（2001）、国家发明家名人堂
- 荣誉博士：伊利诺伊大学（1988）、威斯康星大学麦迪逊分校（1990）、SMU（1995）、耶鲁大学（1996）

## 9. 机构清单

- 教育：Great Bend 高中、伊利诺伊大学（B.S. 1947）、密尔沃基州立师范学院（M.S. 1950，今 UW–Milwaukee）
- 任职：Centralab Division of Globe Union（密尔沃基）、Texas Instruments（1958 加入；1970 休假独立发明；1983 退休）、Texas A&M University 电气工程杰出教授（1978–1984）
- 身后文献：SMU DeGolyer 图书馆（手稿与照片收藏）、TI Historic TI Archives（2005-12-14 设立）

## 10. 终审清单

- [ ] 生卒 1923-11-08 / 2005-06-20，享年 81，出生地 Jefferson City，去世地 Dallas
- [ ] "Kilby 与 Noyce 双雄并立 / co-inventor"平衡呈现，无独享发明表述
- [ ] Noyce 硅+平面工艺、专利诉讼、诺奖百年评论等无载内容一律未写
- [ ] 诺奖理由 "for his part in the invention of the integrated circuit" 表述精确
- [ ] 年份三线：1958-09-12 演示 / 1959-02-06 专利提交 / 2000 诺奖——准确
- [ ] 第一块 IC 材料为锗（非硅）
- [ ] 手持计算器为 Merryman、Van Tassel 三人共同
- [ ] 无 Kilby 直接引语，全部间接转述
- [ ] IC 实物照仅作插图、肖像用装饰圆占位
- [ ] 正文采用 Wilson 式：身份信息页 + 封面装饰圆 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `Jack_S._Kilby/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：装饰圆占位（images.txt 仅 IC 实物照，非肖像）
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：page.md 无直接引语——全文不得出现加引号的"Kilby 原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐（无师承栏的处理）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 Alferov/Kroemer 篇互检（2000 同届份额结构：三篇口径完全一致）；"双雄并立"页与 Noyce 相关表述与 Draper Prize 引用一致

---

## 12. 研究领域表（fields，对齐 yaml 与 person_field）

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | integrated circuits | 集成电路 | 1958 首块 IC（锗）、专利 3,138,743 |
| 1 | electrical engineering | 电气工程 | infobox Fields 主线 |
| 2 | microelectronics | 微电子学 | 军用/工业/商用应用拓荒 |
| 3 | semiconductor devices | 半导体器件 | 晶体管/二极管/电阻/电容单一衬底 |

## 13. 术语清单（第 9 步史实/术语审查）

| 英文 | 中文 | 风险点 |
|------|------|------|
| integrated circuit | 集成电路 | 第一块用锗，勿写"硅" |
| tyranny of numbers | 数字暴政 | 通用术语名，非引语 |
| co-inventor | 共同发明人 | 与 Noyce 双雄并立口径（page.md 原话） |
| handheld calculator | 手持计算器 | 与 Merryman/Van Tassel 三人共同 |
| thermal printer | 热打印机 | 共同发明 |
| monolithic integrated circuit | 单片集成电路 | Ballantine/Draper 理由用词 |
| Nobel citation | 诺奖理由 | 原句 "For his part in the invention of the integrated circuit"，"his part" 措辞勿改 |
| Draper Prize | 德雷珀奖 | 1989 与 Noyce 共享，理由 "their independent development of the monolithic integrated circuit" |

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
