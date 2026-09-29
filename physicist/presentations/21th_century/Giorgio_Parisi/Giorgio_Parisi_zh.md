# 物理学家立传提示词（Giorgio Parisi，2021 诺贝尔物理学奖）

> **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Giorgio Parisi（乔治·帕里西），2021 诺贝尔物理学奖得主（复杂系统与无序系统）。
> **设计哲学**：骨架照搬 Kenneth_G_Wilson_zh.md 标杆；Parisi 的立传主线是「从夸克到鸟群——无序与涨落的统一语言」。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史。
- **本实例**：Giorgio Parisi（乔治·帕里西）。
- **设计哲学**：Parisi 是横跨粒子物理、统计力学与复杂系统的「方法大师」——复制方法/复制对称破缺是核心意象；立传强调同一个人在同一套随机性语言下处理夸克、自旋玻璃、生长界面与鸟群。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Giorgio Parisi（1948-08-04 生于意大利罗马，在世）
- **气质关键词**：**无序系统的解密者、复制对称破缺的缔造者、从原子到行星的复杂性远征者** —— 2021 诺贝尔物理学奖获奖理由（官方原文，page.md 载）：
  > "for the discovery of the interplay of disorder and fluctuations in physical systems from atomic to planetary scales"（因其发现从原子到行星尺度的物理系统中无序与涨落的相互作用）
  - 注：2021 年奖一半授 Parisi（复杂系统），另一半授 Manabe 与 Hasselmann（气候物理建模）。
- **设计母题**：**复制与破缺（replicas & symmetry breaking）**。自旋玻璃的多副本结构中每一对副本有不同的重叠序参量——视觉上可用「多份相同图案的拷贝彼此错位、呈现层级式排布」呼应复制对称破缺。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Giorgio_Parisi/page.md`
- **html/images**：**待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/Giorgio_Parisi`（第 0 步下载 html 与 infobox 肖像到本目录 `images/`；infobox 照片 Parisi in 2006）
- **参考模板**：
  - 物理学家标杆骨架：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ⬜ html 与 images **待下载**：`https://en.wikipedia.org/wiki/Giorgio_Parisi`
- 已核对 page.md，**事实基准如下**：
  - 生卒：1948-08-04 生于罗马，在世；血统四分之一翁布里亚/皮埃蒙特/西西里/罗马（七代罗马人）
  - 国籍：意大利
  - 教育：罗马 San Gabriele 高中（1966）；罗马第一大学（La Sapienza）1970 Laurea，博士论文关于希格斯玻色子
  - 学术导师：Nicola Cabibbo（infobox Academic advisors + 正文 "under the supervision of"）
  - 任职机构（含年份）：意大利国家研究委员会 CNR → INFN 弗拉斯卡蒂国家实验室 1971–1981；经 Sidney Drell 介绍与李政道相识，Columbia University 1973–1974；IHES 1976–1977；巴黎高等师范学院 ENS 1977–1978；回意大利任 INFN 研究员；罗马第二大学（Tor Vergata）理论物理正教授 1982–1992；Sapienza 1992 起（授理论物理/量子力学/统计物理/概率等课程）；参与 APE100 格点规范理论研究；Simons Collaboration "Cracking the Glass Problem" 成员；2018 退休，后当选林琴科学院（Accademia dei Lincei）院长（至 2021）；2023 当选世界科学院 TWAS Fellow
  - 关键荣誉（含年份）：Feltrinelli 1986；Boltzmann Medal 1992（自旋玻璃平均场理论的解）；Italgas 1993；ICTP Dirac Medal 1999；Enrico Fermi Prize 2002；Dannie Heineman Prize（数学物理）2005；Nonino Prize 2005；Microsoft Award 2007；Lagrange Prize 2009（复杂性科学）；Max Planck Medal 2011；Nature 科学指导终身成就奖（意大利）2013；EPS HEPP Prize 2015（夸克胶子概率场论框架）；Lars Onsager Prize 2016（自旋玻璃思想用于计算问题）；Pomeranchuk Prize 2018；Extremadura 大学荣誉博士 2019；**Wolf Prize 2021-02；Nobel Prize in Physics 2021-10**；意大利共和国大十字骑士勋章 2021
  - 外籍院士：法国科学院、美国哲学学会、美国国家科学院
  - 核心贡献清单：
    1. **DGLAP / Altarelli–Parisi 方程**：与 Guido Altarelli 共同提出的部分子密度 QCD 演化方程
    2. **自旋玻璃 Sherrington–Kirkpatrick 模型的精确解**：复制方法系统应用于无序系统、复制对称破缺
    3. **KPZ 方程**（Kardar–Parisi–Zhang）：描述生长界面的动态标度/随机聚集
    4. **湍流多重分形模型**：与 Uriel Frisch 共同提出，描述间歇性
    5. **Parisi–Sourlas 随机量子化**
    6. **复杂系统**：鸟群/蜂群集体运动研究；与意大利物理学家共同引入气候变化研究中的随机共振概念
  - 关键时间线（1948 罗马出生 → 1966 San Gabriele 高中 → 1970 Sapienza Laurea（Cabibbo 门下，希格斯论文）→ 1971 CNR/INFN Frascati → 1973–74 Columbia（Drell 介绍识李政道）→ 1976–77 IHES → 1977–78 ENS → 1982 Tor Vergata 正教授 → 1987《Spin glass theory and beyond》→ 1988《Statistical Field Theory》→ 1992 Sapienza 教授 → 2011 Max Planck 奖章 → 2016 Onsager 奖 → 2016 科学资助行动主义 → 2018 退休+林琴科学院院长 → 2021 Wolf 奖 → 2021 诺贝尔奖 → 2023 TWAS Fellow）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Giorgio_Parisi/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆目录 `Makefile`，设置 `MAIN=Giorgio_Parisi_zh`、`VIDEO_NAME=Giorgio_Parisi_zh`

### 第 3 步：收集图片 【人物专属】

- ⬜ 下载 infobox 肖像到 `images/`（Commons `Special:FilePath/<文件名>?width=600`；与意大利总统 Mattarella 合照 2021 为正文插图候选，非肖像）

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | spin glass | 自旋玻璃 | SK 模型精确解、复制对称破缺 | 核心页 |
| 1 | statistical mechanics | 统计力学 | 无序系统、相变 | 统计页 |
| 2 | quantum field theory | 量子场论 | 随机量子化、统计场论 | 场论页 |
| 3 | complex systems | 复杂系统 | 鸟群、随机共振、优化问题 | 复杂系统页 |
| 4 | quantum chromodynamics | 量子色动力学 | DGLAP/Altarelli–Parisi 演化方程 | 粒子页 |

- 入库：`MySQL/seed_person.py data/Giorgio_Parisi.yaml`（幂等；person_field 带 rank）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Nicola Cabibbo | 师→生（导师） | Sapienza 博士导师，1970 学位论文为希格斯玻色子 |
| co-honored | Klaus Hasselmann | 无向 | 2021 诺贝尔物理学奖共同得主（另一半授气候建模） |
| co-honored | Syukuro Manabe | 无向 | 2021 诺贝尔物理学奖共同得主（另一半授气候建模） |
| colleague | Guido Altarelli | 无向 | DGLAP（Altarelli–Parisi）方程共同提出者 |
| colleague | Uriel Frisch | 无向 | 湍流间歇性多重分形模型共同提出者 |

- 入库：同一 yaml `relations` 段；仅收 page.md 明载关系（Kardar/Zhang 仅以方程命名出现，正文未述合作，不入库；Mézard/Virasoro 仅书目合著，不入库）

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：无序、层级、深紫的数学感
- **主色**：紫罗兰 `#5B2A86`（无序系统的层级结构）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeSpin` 自旋玻璃 — 靛蓝 `#4C5FD5`
  - `badgeQFT` 场论/QCD — 青绿 `#0E7C7B`
  - `badgeKPZ` 生长界面/湍流 — 琥珀 `#E07B30`
  - `badgeFlock` 复杂系统 — 玫瑰 `#C4204F`
- **背景母题**：多份相同图案的拷贝彼此错位、层级排布（复制对称破缺的视觉化），四档透明度渐变

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 无序系统的解密者 / Giorgio Parisi 1948– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地、教育、师承 Cabibbo、任职、荣誉、核心领域）
03  核心贡献概览 — DGLAP / 自旋玻璃 / KPZ / 复杂系统
04  罗马少年与 Cabibbo 门下 (1948–1970) — San Gabriele 高中、Sapienza 希格斯论文
05  Frascati 与海外岁月 (1971–1978) — CNR/INFN、Columbia（Drell 介绍识李政道）、IHES、ENS
06  DGLAP 方程：部分子的演化 — Altarelli–Parisi 方程、深度非弹性标度破坏（示意性标度演化式，page.md 无显式公式，注明概念图式）
07  自旋玻璃与复制对称破缺（核心贡献页）— SK 模型精确解、多副本层级结构概念图式
08  KPZ 方程与湍流多重分形 — 随机生长界面、与 Frisch 的间歇性模型
09  从原子到鸟群：复杂系统 — 集体运动、随机共振（气候变化研究）
10  Sapienza 岁月与 APE100 — 1992 教授、格点规范理论、Simons "Cracking the Glass Problem"
11  荣誉年表 — Nobel 2021 · Wolf 2021 · Boltzmann 1992 · Onsager 2016 · Dirac 1999
12  科学行动主义 — Salviamo la Ricerca Italiana（2016 起，为基础研究发声）
13  遗产：一门随机性的统一语言
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Parisi 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖份额 | 2021 奖 **Parisi 独得一半**（复杂系统），Manabe+Hasselmann 共享另一半（气候建模）；勿写三人平分，更勿把 Parisi 写成气候物理学家 |
| 获奖理由措辞 | 官方原文 "for the discovery of the interplay of disorder and fluctuations in physical systems from atomic to planetary scales"；正文另有 "groundbreaking contributions to theory of complex systems" 转述，两者勿混用 |
| 复制方法归属 | replica method **1971 由 Sam Edwards 首创**（page.md 明载）；Parisi 的贡献是"系统应用于无序系统"与复制对称破缺，勿写成"发明复制方法" |
| DGLAP 双名 | Altarelli–Parisi 方程 = Dokshitzer–Gribov–Lipatov–Altarelli–Parisi 方程，两名均 page.md 载；与 Kenneth Wilson 的重整化群是不同语境（QCD 标度演化），勿混淆 |
| KPZ 方程 | page.md 仅以方程名出现，未叙述 Kardar/Zhang 合作细节；slides 只写"以三人命名的随机生长方程"，禁编合作叙事、禁入库关系 |
| 李政道一节 | Drell 介绍 Parisi 与李政道相识、1973–74 在 Columbia 工作为 page.md 明载；但未载与李政道的合作论文，勿写"与李政道合作研究" |
| 鸟群研究 | page.md 只写 "study of whirling flocks of birds"，勿添加罗马广场等未经本页证实的细节 |
| 林琴科学院 | 2018 退休后当选院长（至 2021），勿写成"获诺奖后当选" |
| 书目陷阱 |《Spin glass theory and beyond》（Mézard/Parisi/Virasoro 1987）与《Statistical Field Theory》（1988）可列书影；合著者仅书目证据不入关系库 |
| 引语红线 | 各奖项 citation（Boltzmann/Dirac/Fermi/Onsager/Wolf 等）page.md 有英文原文，可直接引用；正文叙述一律转述 |
| 在世口径 | 1948-08-04 生、在世，death_date 留白，勿编卒年 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| replica trick | 复制技巧 | 勿译"骗局"；Edwards 首创、Parisi 系统化 |
| replica symmetry breaking | 复制对称破缺 | 层级式破缺结构 |
| spin glass | 自旋玻璃 | 与普通玻璃（非晶）区分 |
| Sherrington–Kirkpatrick model | SK 模型 | 无限程自旋玻璃平均场模型 |
| DGLAP equations | DGLAP 演化方程 | 又名 Altarelli–Parisi 方程 |
| parton density | 部子密度 | QCD 标度演化对象 |
| Kardar–Parisi–Zhang equation | KPZ 方程 | 随机生长界面 |
| multifractal | 多重分形 | 湍流间歇性描述 |
| intermittency | 间歇性 | 湍流强涨落现象 |
| stochastic resonance | 随机共振 | 气候变化研究中的概念 |
| stochastic quantization | 随机量子化 | Parisi–Sourlas 程序 |
| Laurea | 意大利大学学位 | 对应本科+硕士连读，勿译"博士" |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Mirage** — Notan Nigres（3:22，电子/梦幻/抽象）
- **匹配理由**: "梦幻/抽象" 匹配自旋玻璃与复制对称破缺的抽象数学美感——在无序的幻象中寻找层级秩序；电子质感贴合复杂系统的现代感（从原子到行星再到鸟群的尺度跳跃）。
- **本地路径**: `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` → 复制为 `presentations/21th_century/Giorgio_Parisi/Mirage.wav`
- **备选**: Eternals（宏大/深远，匹配跨领域遗产）；The Flow of Time（时间感，匹配演化方程）

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Giorgio_Parisi/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 人物 + 领域 + 关系入库（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
