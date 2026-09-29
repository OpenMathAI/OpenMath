# 物理学家立传提示词（Anton Zeilinger，2022 诺贝尔物理学奖）

> **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Anton Zeilinger（安东·蔡林格），2022 诺贝尔物理学奖得主（纠缠光子实验与量子信息科学）。
> **设计哲学**：骨架照搬 Kenneth_G_Wilson_zh.md 标杆；Zeilinger 的立传主线是「从中子干涉术到量子隐形传态——把纠缠从思想变成技术」。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史。
- **本实例**：Anton Zeilinger（安东·蔡林格）。
- **设计哲学**：Zeilinger 是「量子纠缠的工程师」——最早的中子干涉术训练、GHZ 三粒子纠缠、量子隐形传态、纠缠光子密码学直到卫星量子通信愿景；立传强调「一位实验家的好奇心如何接连开辟多个领域」。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Anton Zeilinger（1945-05-20 生于奥地利上奥地利州里德因克赖斯，在世）
- **气质关键词**：**量子隐形传态的实现者、GHZ 纠缠的开辟者、奥地利量子旗舰的缔造者** —— 2022 诺贝尔物理学奖获奖理由（官方原文，page.md 载）：
  > "for experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science"（因纠缠光子实验、确立 Bell 不等式的违背并开创量子信息科学）
  - 注：2022 年奖由 Zeilinger、Alain Aspect、John Clauser 三人共享（等额，无半奖之分）。
- **设计母题**：**传送（teleportation）**。量子态在一处消失、在另一处重现——视觉上可用「一组光子态在左端散开、在右端按原样重组」的分身/传送母题，辅以多瑙河两岸实验室的地景线。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Anton_Zeilinger/page.md`
- **html/images**：**待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/Anton_Zeilinger`（第 0 步下载 html 与 infobox 肖像到本目录 `images/`；正文有 Zeilinger 与 Voss-Andreae 雕塑合照可作插图）
- **参考模板**：
  - 物理学家标杆骨架：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ⬜ html 与 images **待下载**：`https://en.wikipedia.org/wiki/Anton_Zeilinger`
- 已核对 page.md，**事实基准如下**：
  - 生卒：1945-05-20 生于里德因克赖斯（上奥地利，盟军占领期），在世
  - 国籍：奥地利
  - 教育：1963–1971 维也纳大学物理；1971 博士（论文《Neutron depolarization measurements on a Dy-single crystal》，导师 Helmut Rauch）；1979 维也纳工业大学特许任教资格（habilitation）
  - 任职机构（含年份）：维也纳原子研究所研究助理（1970s）→ MIT 中子衍射实验室副研究员（至 1979）→ 原子研究所助理教授 1979 → MIT 物理系副教授 1981–1983 → 维也纳工业大学/慕尼黑工业大学/因斯布鲁克大学/维也纳大学教授（1980–1990 间）→ IQOQI（奥地利科学院量子光学与量子信息研究所维也纳分所）科学主任 2004–2013 → 维也纳大学荣休教授 2013 → **奥地利科学院院长 2013–2022**；IST Austria（奥地利科学技术研究所）董事会副主席（2006 起，该机构由其提议发起）；2009 创办 International Academy Traunkirchen（资助资优学生）
  - 关键荣誉（含年份）：European Optics Prize 1996；Pour le Mérite 2000；奥地利科学与艺术荣誉勋章 2001；Klopsteg Memorial Award 2004；Descartes Prize 2004（IST-QuQuComm 项目组）；King Faisal 国际奖 2005；Wilhelm Exner Medal 2005；欧洲物理学会量子电子奖 2007；**Isaac Newton Medal 首枚 2008**（引言作 2007、荣誉列表作 2008，见陷阱表）；德国联邦十字大功绩星章 2009；**Wolf Prize 2010**（与 Aspect、Clauser；page.md 荣誉列表误作 2012，见陷阱表）；AAAS Fellow 2012；**John Stewart Bell Prize 2017**（与 Ronald Hanson、Sae Woo Nam）；捷克参议院银质奖章 2017；Cozzarelli Prize（PNAS）2018；IEEE 荣誉会士 2018；**Micius Quantum Prize 2019**（与 Wiesner、Bennett、Brassard、Ekert、潘建伟）；海森堡奖章 2022；**Nobel Prize in Physics 2022**；奥地利共和国大金质荣誉勋章 2024；荣誉博士学位（柏林洪堡、格但斯克、因斯布鲁克）等
  - 知名博士生（infobox 明载）：Stefanie Barz、潘建伟（Pan Jianwei）、Thomas Jennewein、Julian Voss-Andreae、Gregor Weihs
  - 核心贡献清单：
    1. **中子干涉术**（师承 Rauch；ILL 格勒诺布尔：自旋相位旋转变号验证、物质波相干自旋叠加；MIT 与 C.G. Shull 合作动力学衍射；极冷中子干涉仪；S18 仪器单中子双缝）
    2. **GHZ 态与定理**：1990 与 Daniel Greenberger、Michael Horne 率先研究两量子比特以上纠缠；GHZ 定理是局域实在论与量子力学最简洁的矛盾；1999 首次实验证实三粒子以上纠缠并完成 GHZ 非定域性检验
    3. **量子隐形传态**：独立量子比特隐形传态的最早实现之一；自由传播传送 qubit 源；加那利群岛两岛间 144 km 传送
    4. **纠缠交换**（entanglement swapping）：提议后 1998 由其小组首次实验实现
    5. **纠缠光子量子密码**首次实现（1998，2000 发表）；2005 单向量子计算首次实现（Knill–Laflamme–Milburn 方案）
    6. **Bell 检验漏洞关闭**：1998 用超快随机数发生器关闭通信漏洞；首个满足 freedom-of-choice 条件的 Bell 实验；首个对光子无 fair sampling 假设的 Bell 检验；Leggett 不等式实验违背（超越 Bell 定理的非局域实在论检验）
    7. 宏观量子叠加：富勒烯 C60/C70 干涉（1999）；与 Kwiat 共同开发的偏振纠缠光子对源；轨道角动量纠缠至 300 ħ；微镜自冷却（2006）
  - 关键时间线（1945 出生 → 1963 入维也纳大学 → 1971 博士 → 1970s 原子研究所+MIT → 1979 habilitation+助理教授 → 1981–83 MIT 副教授 → 1980–90 四校教授 → 1990 GHZ → 1998 纠缠交换/QKD/关闭通信漏洞 → 1999 富勒烯干涉+GHZ 实验证据 → 2004 IQOQI 主任 → 2005 单向量子计算 → 2006 IST Austria → 2008 Isaac Newton Medal → 2009 Traunkirchen → 2013 荣休+奥地利科学院院长 → 2017 Bell Prize → 2019 Micius → 2022 诺贝尔奖 → 2024 奥地利大金勋章）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Anton_Zeilinger/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆目录 `Makefile`，设置 `MAIN=Anton_Zeilinger_zh`、`VIDEO_NAME=Anton_Zeilinger_zh`

### 第 3 步：收集图片 【人物专属】

- ⬜ 下载 infobox 肖像到 `images/`（infobox 用 2019 年照；与 Voss-Andreae 雕塑合照可作 GHZ 页插图）

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | quantum entanglement | 量子纠缠 | 研究主线（导语明载） | 核心页 |
| 1 | quantum teleportation | 量子隐形传态 | 独立 qubit 传送、144 km 岛际 | 传送页 |
| 2 | quantum information | 量子信息 | 密码/计算/通信协议 | 信息页 |
| 3 | quantum optics | 量子光学 | 纠缠光子源、轨道角动量 | 光子页 |
| 4 | neutron interferometry | 中子干涉术 | 最早工作、后续研究的根基 | 早年页 |

- 入库：`MySQL/seed_person.py data/Anton_Zeilinger.yaml`（幂等；person_field 带 rank）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Helmut Rauch | 师→生（博士导师） | 维也纳大学博士导师（1971），中子退极化论文 |
| advisor-student | Pan Jianwei | Zeilinger→学生 | 博士生（infobox 明载），量子通信实验物理学家 |
| advisor-student | Stefanie Barz | Zeilinger→学生 | 博士生（infobox 明载） |
| advisor-student | Thomas Jennewein | Zeilinger→学生 | 博士生（infobox 明载） |
| advisor-student | Julian Voss-Andreae | Zeilinger→学生 | 博士生（infobox 明载），后为量子主题雕塑家 |
| advisor-student | Gregor Weihs | Zeilinger→学生 | 博士生（infobox 明载） |
| co-honored | Alain Aspect | 无向 | 2022 诺贝尔物理学奖共同得主；2010 Wolf Prize 亦三人共享 |
| co-honored | John F. Clauser | 无向 | 2022 诺贝尔物理学奖共同得主；2010 Wolf Prize 亦三人共享 |
| colleague | Daniel Greenberger | 无向 | 1990 年共同提出 GHZ 态/定理 |
| colleague | Michael Horne | 无向 | 1990 年共同提出 GHZ 态/定理 |
| colleague | Clifford G. Shull | 无向 | 在 MIT 中子衍射实验室合作研究中子动力学衍射（诺奖得主） |
| colleague | Paul Kwiat | 无向 | 共同开发偏振纠缠光子对源（时任 Zeilinger 组博士后） |

- 入库：同一 yaml `relations` 段；仅收 page.md 明载关系（Kippenberg/Heidmann 仅微镜实验一行点名，Knill/Laflamme/Milburn 仅协议名义引用，均不入库）

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：阿尔卑斯深绿、传动的蓝光、未来感
- **主色**：深松绿 `#1E5B4F`（奥地利山水与量子通信 fiber）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeTeleport` 隐形传态 — 靛蓝 `#4C5FD5`
  - `badgeGHZ` GHZ 纠缠 — 玫瑰 `#C4204F`
  - `badgeNeutron` 中子干涉 — 琥珀 `#E07B30`
  - `badgeCrypto` 量子密码/通信 — 青绿 `#0E7C7B`
- **背景母题**：一条光子态从画面左缘散化为波纹、在右缘重组为原样（传送母题），下缘衬多瑙河两岸实验室剪影与卫星弧线

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 量子隐形传态的实现者 / Anton Zeilinger 1945– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地、教育、师承、任职、荣誉、核心领域、门生）
03  核心贡献概览 — 中子干涉 / GHZ / 隐形传态 / 量子通信与密码
04  早年与中子干涉术 (1945–1979) — Rauch 门下、Dy 单晶中子退极化、ILL 自旋相位变号
05  MIT 与 C.G. Shull — 动力学衍射、极冷中子干涉仪、S18 单中子双缝
06  GHZ 态：三粒子纠缠（核心贡献页）— 1990 与 Greenberger/Horne 的定理、1999 首次实验证据（概念图式：三粒子关联，page.md 无公式）
07  量子隐形传态 — 独立 qubit 传送、纠缠交换 1998、加那利群岛 144 km
08  量子通信与量子密码 — 纠缠光子 QKD 首实现（1998/2000）、多瑙河→维也纳→卫星梦想、单向量子计算 2005
09  关闭 Bell 漏洞与 Leggett 检验 — 1998 超快随机数、freedom-of-choice、无 fair sampling、非局域实在论
10  宏观量子叠加 — 富勒烯 C60/C70 干涉 1999、轨道角动量 300 ħ、微镜自冷却
11  门生与传承 — 潘建伟、Gregor Weihs、Stefanie Barz 等
12  荣誉年表 — Nobel 2022 · Isaac Newton 2008 · Wolf 2010 · Bell Prize 2017 · Micius 2019
13  科学旗舰与公众 — 奥地利科学院院长、IST Austria、Traunkirchen 学院、42 号帆船
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Zeilinger 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖份额 | 2022 奖三人**等额共享**（Zeilinger/Clauser/Aspect），勿写半奖 |
| Wolf 奖年份两说 | page.md infobox 作 **2010**（与 Aspect/Clauser 页一致），但本页荣誉列表误作 2012——**取 2010 并注记页面内矛盾** |
| Isaac Newton Medal 两说 | 引言作 2007、荣誉列表作 2008（首枚）——**取荣誉列表 2008** 并注记 |
| 传送年份红线 | 量子隐形传态的**具体年份 page.md 未标**（勿写 1997）；1998 明载的是纠缠交换首实现、纠缠光子 QKD（2000 发表）、关闭通信漏洞 Bell 检验；144 km 岛际传送 page.md 亦未标年 |
| GHZ 双年份 | 1990 是与 Greenberger/Horne **开始研究**多粒子纠缠；1999 才是**首次实验证据**——两个年份勿混 |
| Shull 同名区分 | MIT 合作者 C.G. **Shull（Clifford G. Shull，1994 物理诺奖，中子）**，勿与 Bell 检验语境的 Shimony（CHSH 的 S）混淆 |
| Horne 双合作 | Michael Horne 既在 CHSH（Clauser 侧）又在 GHZ（本页 1990）——两篇均 page.md 明载，note 写清语境 |
| Kwiat 身份 | 时为 Zeilinger 组**博士后**（非博士生），建 colleague 不建 advisor-student |
| 潘建伟 | infobox 博士生名单用 "Pan Jianwei"；中文界面写潘建伟；note 不引申其后续成就细节（Micius 同奖共得主一行可提） |
| 行政职务 | 奥地利科学院院长 2013–2022（至诺奖年）；IQOQI 科学主任 2004–2013；IST Austria 由其提议发起——三个机构层级勿混 |
| 42 号帆船 | 《银河系漫游指南》书迷、帆船命名 42 可作公众页趣闻（page.md 明载），勿扩写 |
| 在世口径 | 1945-05-20 生、在世，death_date 留白，勿编卒年 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| quantum teleportation | 量子隐形传态 | 勿译"量子瞬移"；传态非克隆（no-cloning） |
| entanglement swapping | 纠缠交换 | 纠缠态的传送 |
| GHZ state / theorem | GHZ 态/定理 | Greenberger–Horne–Zeilinger 三人缩写 |
| multi-particle entanglement | 多粒子纠缠 | 首次实验证据 1999 |
| Bell test loopholes | Bell 检验漏洞 | 通信漏洞/fair sampling/freedom-of-choice 三类 |
| Leggett inequality | Leggett 不等式 | 非局域实在论检验，超越 Bell |
| neutron interferometry | 中子干涉术 | 早年根基 |
| spinor phase | 旋量相位 | 4π 周期（旋转变号） |
| one-way quantum computation | 单向量子计算 | 测量型量子计算（KLM 方案） |
| quantum cryptography | 量子密码学 | 纠缠光子实现 |
| orbital angular momentum | 轨道角动量 | 光子 OAM 纠缠至 300 ħ |
| Dr. habil. / Habilitation | 特许任教资格 | 德奥制度，勿译"博士" |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Ascension** — Cold Cinema（2:32，科幻/史诗/上升）
- **匹配理由**: "上升/科幻" 呼应隐形传态与卫星量子通信的梦想（把纠缠光源送上轨道）；上升感贴合从原子研究所到科学院院长的层层跃迁叙事。
- **本地路径**: `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav` → 复制为 `presentations/21th_century/Anton_Zeilinger/Ascension.wav`
- **备选**: Mirage（梦幻/抽象，匹配传送母题）；Winds Of Freedom（英雄/史诗）

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Anton_Zeilinger/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 人物 + 领域 + 关系入库（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
