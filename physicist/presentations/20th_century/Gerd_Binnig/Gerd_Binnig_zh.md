# Gerd Binnig（格尔德·宾宁）立传提示词

> qid=Q76766 · 1947-07-20 生（在世） · 德国物理学家 · 20 世纪 · 1986 诺贝尔物理学奖（与 Heinrich Rohrer 共享一半）
> 本地 Wikipedia 数据源：`physicist/presentations/20th_century/20th_century/Gerd_Binnig/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家标杆 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**。物理学家立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。images.txt 无本人肖像（page.md 图注有 "Binnig in 2013" 但无图片 URL）→ 用装饰圆占位（Review 阶段可尝试 Commons 检索 "Gerd Binnig 2013"）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（或装饰圆）+ 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色（诺奖金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「隧穿探针 / 原子表面起伏」母题。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Gerd Karl Binnig（格尔德·卡尔·宾宁）
- **生卒**：1947-07-20 生于法兰克福（Frankfurt am Main，德国）→ **在世**（去世地留白）
- **国籍**：德国（German / allied-occupied Germany 出生期）
- **身份**：物理学家（发明家、企业家）
- **童年**：在战后废墟的城市里玩耍长大；家住法兰克福与奥芬巴赫两地，两城各上过学；10 岁立志成为物理学家，随后一度怀疑选择，转向音乐——组过乐队、15 岁学小提琴、在校乐团演奏
- **家庭**：1969 年与心理学家 Lore Wagler 结婚，一女生于瑞士、一子生于加州；爱好阅读、游泳、高尔夫
- **教育轨迹**：
  - 法兰克福大学（Goethe University Frankfurt）物理，1973 年学士（bachelor's degree）
  - 留校在 Werner Martienssen 组读博，指导人为 Eckhardt Hoenig，1978 年获博士
- **博士导师**：Werner Martienssen（组）；指导人（supervisor）Eckhardt Hoenig
- **研究领域**：物理（扫描探针显微术、纳米科学）
- **任职**：IBM 苏黎世研究实验室（1978 加入）→ IBM Almaden Valley（加州，1985–1988）+ 斯坦福大学访问教授 → IBM Fellow（1987）+ IBM Physics group Munich → 创办 Definiens（1994）

### 1.5 研究领域表（第 4 步入库用，与 yaml fields 一致）

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | scanning probe microscopy | 扫描探针显微术 | STM + AFM 共同开创的学科 |
| 1 | scanning tunneling microscopy | 扫描隧道显微术 | 1986 诺奖核心成果 |
| 2 | atomic force microscopy | 原子力显微术 | 1985 年发明，覆盖绝缘表面 |
| 3 | nanoscience | 纳米科学 | Kavli Prize in Nanoscience（2016）所属领域 |

### 1.6 术语清单（第 9 步用）

| 英文 | 中文 | 风险 |
|------|------|------|
| scanning tunneling microscope (STM) | 扫描隧道显微镜 | "设计"而非"发现"原理 |
| scanning probe microscopy (SPM) | 扫描探针显微术 | STM/AFM 的统称 |
| atomic force microscope (AFM) | 原子力显微镜 | 1985 年，勿写 1986 |
| tunneling current | 隧道电流 | 物理原理之前已知 |
| insulating surfaces | 绝缘表面 | AFM 相对 STM 的增量 |
| Cognition Network Technology | 认知网络技术 | Definiens 公司核心技术 |
| Kavli Prize in Nanoscience | 卡夫利纳米科学奖 | 2016 年，距诺奖三十年 |
| IBM Fellow | IBM 院士 | 1987 年授予，勿与诺奖年份混淆 |

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **废墟上长大的战后孩子**：1947 年生于法兰克福，"在城市废墟中玩耍"的童年——从瓦砾到原子，一条从摧毁到看见的隐喻线。
2. **物理与音乐之间的少年**：10 岁立志物理；乐队、15 岁的小提琴与校乐团——科学之外的第二生命线，1987 年他在慕尼黑主持的 IBM 物理组还研究"创造力"。
3. **法兰克福求学**（至 1978）：Martienssen 组、Hoenig 指导下完成博士。
4. **1978 入 IBM 苏黎世**：与 Heinrich Rohrer、Christoph Gerber、Edmund Weibel 同组——STM 四人组在此集结。
5. **STM 的诞生**：发明扫描隧道显微镜（scanning tunneling microscope）——在原子尺度对表面成像的仪器，开创扫描探针显微术（scanning probe microscopy）。
6. **诺奖委员会评语（可引）**：委员会如此描述 STM 对科学的影响——"entirely new fields are opening up for the study of the structure of matter."（"全新的研究领域正在为物质结构研究打开大门"）——这是**委员会评语**，标注清楚出处，勿当 Binnig 原话。
7. **原理已知、实现为艰**：STM 依据的物理原理在 IBM 团队之前已知；Binnig 与同事们是**率先解决将其付诸实现的关键实验难题**的人——"发明"的本质在实验攻坚，勿写"从零发现隧穿原理"。
8. **连获大奖**：德国物理奖、Otto Klung 奖、Hewlett-Packard 奖、费萨尔国王奖——IBM 苏黎世团队在诺奖前已被密集承认（个人名下另有 Klung Wilhelmy 科学奖 1983、EPS Europhysics 奖 1984、King Faisal 奖 1984）。
9. **1986 诺贝尔物理学奖**：与 Heinrich Rohrer 共享一半（两人各四分之一），另一半授予 Ernst Ruska；获奖理由"表彰他们设计扫描隧道显微镜"。诺奖演讲（1986-12-08）：*Scanning Tunneling Microscopy – From Birth to Adolescence*（与 Rohrer 同题联讲）。
10. **AFM：给绝缘表面一双眼睛**（1985）：发明原子力显微镜（atomic force microscope），与 Christoph Gerber、Calvin Quate 共同做出可用于绝缘表面的工作样机——STM 只能看导电表面，AFM 补齐了另一半世界。
11. **加州岁月**（1985–1988）：IBM Almaden Valley + 斯坦福大学访问教授；1987 年任 IBM Fellow，同年创建 IBM Physics group Munich（研究方向：创造力与原子力显微术）。
12. **从实验室到产业**：1994 年创办 Definiens，2000 年转型商业公司，开发模拟人眼与脑的图像分析"认知网络技术"（2014 年被阿斯利康收购，此条 page.md 外链标题有载可提）。
13. **2016 Kavli 纳米科学奖**：三十年后再次因 STM 获国际大奖；当选挪威科学与文学院院士。IBM 在吕施利孔的 Binnig and Rohrer Nanotechnology Center 以两人命名。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（琥珀铜） | `#A64B00` | 隧道电流的暖光 / 年轻一代的锐气 |
| 强调色（诺奖金） | `#C9A227` | 诺贝尔奖 / 尊崇 |
| 分类色 1（STM — 靛蓝） | `#4C5FD5` | 扫描隧道显微镜 / 原子成像 |
| 分类色 2（AFM — 青绿） | `#0E7C7B` | 原子力显微镜 / 绝缘表面 |
| 分类色 3（产业与创造 — 琥珀） | `#E07B30` | Definiens / 创造力研究 |
| 分类色 4（荣誉与传承 — 玫瑰） | `#C4204F` | 诺奖 / Kavli / 传承中心 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「探针扫过原子表面」的视觉语言——探针针尖划过起伏表面时的等电流线涟漪。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：史诗 / 美丽 / 振奋（"全新的领域正在打开"——看到原子的那一刻）
- **选定曲目**：Really Slow Motion **Shine Like The Sun**（史诗 / 美丽 / 振奋），匹配"打开物质结构研究全新领域"的开创者气质。
- **落地文件**：`physicist/presentations/20th_century/Gerd_Binnig/ShineLikeTheSun.wav`（复制自音乐库，不入 git）。
- **匹配理由**：Binnig 是 1986 届三人中最年轻者，STM 让人类第一次"看见"原子——Shine Like The Sun 的明亮与升腾感匹配"全新领域打开"的意象，也匹配他从废墟童年到 Kavli 奖的完整弧线；与本组其他五人曲目不重复。

## 4. Slide 规划（约 15 页，Wilson 式结构）

1. **封面**（`\titleslide`）：顶部标签「纳米科学 · 德国」+ Binnig 1947– + 右上头像/装饰圆 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：扫描隧道显微镜 / 原子力显微镜 / 纳米科学的开创 / 产业与创造力
4. **早年：废墟与琴弦**（1947–1969）：战后法兰克福、10 岁立志、音乐少年
5. **法兰克福求学**（1969–1978）：Martienssen 组、Hoenig 指导、1978 博士
6. **IBM 苏黎世四人组**（1978–）：Rohrer / Gerber / Weibel、Rüschliken 实验室
7. **STM 的诞生**：原子尺度表面成像、实验攻坚（原理已知、实现为艰）
8. **诺奖委员会的判词**：可引评语 "entirely new fields..."、奖项密集而来的前夜
9. **1986 诺贝尔物理学奖**：与 Rohrer 共享一半、与 Ruska 同台、联袂诺奖演讲
10. **1985 AFM**：绝缘表面的成像、Gerber 与 Quate 协作
11. **加州岁月**（1985–1988）：Almaden Valley、斯坦福访问教授
12. **IBM Fellow 与慕尼黑**（1987–）：创造力研究、IBM Physics group Munich
13. **Definiens：第二次创业**（1994–）：认知网络技术、图像智能
14. **2016 Kavli 纳米科学奖**：三十年回响、Binnig and Rohrer Nanotechnology Center
15. **结尾**：在世大师、"教会人类看见原子的人"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **诺奖切分**：Binnig 与 Rohrer **共享一半**（各四分之一），另一半是 Ruska——勿写"三人平分"，也勿写 Binnig/Rohrer"独享"。
- **获奖理由**："表彰他们设计扫描隧道显微镜"（for their design of the scanning tunneling microscope）——"设计"而非"发现"；STM 的物理原理在之前已知，IBM 团队率先解决实验实现难题——勿写"发现了隧穿效应""从零发明 STM 原理"。
- **委员会引语归属**："entirely new fields are opening up for the study of the structure of matter." 是**诺贝尔委员会评语**（page.md 明载 "The Nobel committee described the effect..."）——引用时须标注"诺奖委员会"，勿当 Binnig 本人的话。
- **AFM 年份与伙伴**：1985 年发明 AFM；工作样机是与 **Christoph Gerber、Calvin Quate** 共同完成（面向绝缘表面）——勿写 Binnig 独自完成，年份勿写 1986。
- **四人组表述**：STM 开发团队为 Binnig、Rohrer、Gerber、Weibel 四人（page.md 原文），但获奖者是 Binnig 与 Rohrer 两人——Gerber/Weibel 的贡献可在叙事中致意，勿在获奖表述中扩列。
- **在世人物**：无卒日——生卒行写"1947-07-20 生"，去世地留白；勿写"享年"。
- **总名单国籍列差异**：总名单国籍列为 "Switzerland"（IBM 苏黎世工作地），page.md 明确为 **Germany**（生于法兰克福、德国物理学家）——**国籍一律按 page.md 写德国**，并在 Review 时建议核对总名单。
- **导师表述**：博士在 Werner Martienssen 组完成、由 Eckhardt Hoenig 指导（page.md："a PhD within Werner Martienssen's group, supervised by Eckhardt Hoenig"）——两人关系层次勿混：Martienssen 是组负责人，Hoenig 是指导人。
- **学位时点**：1973 年 page.md 写 "bachelor's degree"（学士）——勿擅自升格为硕士（Diplom）。
- **联袂演讲**：1986-12-08 诺奖演讲题目 *Scanning Tunneling Microscopy – From Birth to Adolescence* 与 Rohrer **同题**——可作"两人联袂"的叙事细节。
- **Definiens 被购**：2014 年阿斯利康完成收购（page.md 外链标题可溯）——如写则注明年份与事实层级，或干脆不写。
- **引语红线**：Binnig 本人在 page.md 中无直接引语；唯一可引句是委员会评语（须标注出处）。
- **肖像**：images.txt 仅 Wikiquote logo，**无本人肖像**——装饰圆占位（Review 可尝试 Commons "Gerd Binnig 2013"）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76766 | 待写入 |
| name_zh | 格尔德·宾宁 | 待写入 |
| name_en | Gerd Binnig | 待写入 |
| birth_date | 1947-07-20 | 待写入 |
| death_date | （在世，留白） | 待写入 |
| nationality | Germany | 待写入 |
| primary_occupation | physicist | 待写入 |
| field_of_work | physics（扫描探针显微术） | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士师承**：Werner Martienssen（组负责人）、Eckhardt Hoenig（指导人）——advisor-student（Hoenig 为直接指导人，Martienssen 为组/教席层）
- **共同得主**：Heinrich Rohrer（1986 共享一半，co-honored）；Ernst Ruska（同届另一半，co-honored）
- **STM 合作团队**：Christoph Gerber、Edmund Weibel（IBM 苏黎世）
- **AFM 合作伙伴**：Christoph Gerber、Calvin Quate（1985-1986 工作样机）
- **博士生**：Franz Josef Giessibl（infobox 载）
- **配偶**：Lore Wagler（心理学家，1969 结婚）
- **任职机构同事侧**：IBM 苏黎世研究实验室（1978–）、IBM Almaden Valley（1985–1988）、斯坦福大学访问教授、IBM Physics group Munich（1987 起）
- **诺贝尔奖同届**：1986 年物理学奖三人共享（Ruska + Binnig + Rohrer，但切分不同）

## 8. 奖项清单

- 诺贝尔物理学奖（1986，与 Heinrich Rohrer 共享一半）
- Klung Wilhelmy Science Award（1983，即 German Physics Prize / Otto Klung 奖一脉）
- EPS Europhysics Prize（1984）
- King Faisal Prize（King Faisal International Prize in Science，1984）
- The Elliott Cresson Medal（1987）
- Kavli Prize in Nanoscience（2016）
- IBM Fellow（1987）
- National Inventors Hall of Fame（入选）
- Bavarian Order of Merit、Bavarian Maximilian Order for Science and Art、Great Cross with Star and Sash of the Order of Merit of the Federal Republic of Germany、Gustav Hertz Prize、Urania Medal（metadata 有载）
- 挪威科学与文学院院士（2016）

## 9. 机构清单

- 教育：法兰克福大学（1973 学士、1978 博士，Martienssen 组 / Hoenig 指导）
- 任职：IBM 苏黎世研究实验室（1978 加入，Rüschlikon）、IBM Almaden Valley（1985–1988）、斯坦福大学访问教授（1985–1988）、IBM Fellow + IBM Physics group Munich（1987 起）
- 创业：Definiens（1994 创办，2000 商业化，认知网络技术）
- 纪念：Binnig and Rohrer Nanotechnology Center（IBM，Rüschlikon）

## 10. 终审清单

- [ ] 生卒 1947-07-20 / 在世，出生地 Frankfurt am Main
- [ ] 诺奖切分 = Binnig/Rohrer 共享一半 + Ruska 一半
- [ ] 获奖理由"设计扫描隧道显微镜"，无"发现隧穿原理"表述
- [ ] 委员会引语标注出处（诺奖委员会，非 Binnig 本人的话）
- [ ] AFM 1985 + Gerber/Quate 协作表述准确
- [ ] 国籍按 page.md 写"德国"（总名单 Switzerland 差异已注记）
- [ ] 导师层次：Martienssen 组 / Hoenig 指导
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像/装饰圆 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `20th_century/Gerd_Binnig/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：装饰圆占位；如 Review 阶段从 Commons 取得真人照则替换并记录来源
- [ ] **国籍**：封面顶部徽章明示德国
- [ ] **引语核对**：唯一加引号句为诺奖委员会评语，须标注出处
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪物理学家（Ruska / Rohrer / Lawrence）格式对齐

---

> **开始执行。每完成一步汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
