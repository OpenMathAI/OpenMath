# 图灵奖得主立传提示词（人物实例：Maurice Wilkes）

> **本文件是 OpenTuring 的「图灵奖得主立传提示词」实例**，以 Maurice Wilkes（莫里斯·威尔克斯，1967 图灵奖，EDSAC 与微程序奠基者）为样板。
> 参照标杆实例 Donald E. Knuth（`Donald_Knuth/Donald_Knuth_zh.md`）与通用模板 `Turing_Bio_Prompt_Template.md`。
> 凡标注 `【模板通用】` 的部分可原样复用到任何图灵奖得主；标注 `【人物专属】` 的部分需按目标人物替换。

---

## 一、模板定位

- **目标项目**：OpenTuring —— 开放图灵奖得主人物史（与 OpenMath 数学家侧、OpenChemist、OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Sir Maurice Vincent Wilkes（莫里斯·文森特·威尔克斯，1913-06-26 生于英格兰伍斯特郡达德利，2010-11-29 逝于英格兰剑桥，享年 97）。**1967 图灵奖得主**。
- **设计哲学**：图灵奖得主必须有「身份信息页」，贡献表现为**存储程序计算机 / 微程序 / 计算机实验室建制**——Wilkes 是"实用存储程序计算机"的先驱，气质为**工程 / 系统 / 开创**。

---

## 二、背景信息 【人物专属】

- **目标得主**：Sir Maurice Vincent Wilkes（1913-06-26 ~ 2010-11-29，已故）
- **气质关键词**：**EDSAC 设计者、微程序（microprogramming）发明者、符号标号/宏/子程序库先驱、剑桥计算机实验室主任、英国计算机学会创始会长** —— 1967 图灵奖官方 citation（ACM）："Professor Wilkes is best known as the builder and designer of the EDSAC, the first computer with an internally stored program. Built in 1949..."（EDSAC 是**第一台内部存储程序计算机**；注意：此处 "first" 指"实用、成功运行"的存储程序计算机，区别于 Manchester Baby/SSEM 1948 的首次存储程序运行）。
- **设计母题**：**工程 / 系统 / 开创**——"让一台计算机真正跑起来服务全大学"的实用主义母题。视觉语言：泡泡背景（稀疏大块实心圆）；配色用图灵紫主色 + 四分类色（存储程序计算机 / 微程序 / 程序库方法 / 网络与分布式）。
- **本地 Wikipedia**：
  - 原始 HTML：`turing/pages/1967/Maurice Wilkes/index.html`（106 KB，含 infobox + 完整正文）
  - 元数据：`turing/pages/1967/Maurice Wilkes/metadata.json`
  - 头像：`turing/pages/1967/Maurice Wilkes/images/Maurice_Vincent_Wilkes_1980_3_cropped_.jpg`（已复制到 `presentations/Maurice_Wilkes/images/Wilkes.jpg`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 本地数据已就绪：`turing/pages/1967/Maurice Wilkes/index.html` 与 `metadata.json`
- ✅ 头像已就绪：`turing/pages/1967/Maurice Wilkes/images/Maurice_Vincent_Wilkes_1980_3_cropped_.jpg`
- **事实基准**（全部取自本地 index.html infobox 与正文）：
  - **生卒**：1913-06-26 生于英格兰伍斯特郡达德利（Dudley, Worcestershire）；2010-11-29 逝于英格兰剑桥（Cambridge, Cambridgeshire），享年 97
  - **本名**：John Maurice Vincent Wilkes（infobox 记为 John Maurice Vincent Wilkes）；爵位 Sir（Knight Bachelor）；FRS / FREng / FBCS
  - 国籍：英国
  - 家庭：1947 年与 Nina Twyman 结婚（妻 2008 年去世）；一子二女
  - **教育**：
    - King Edward VI College, Stourbridge
    - St John's College, Cambridge，1931–1934 读 Mathematical Tripos
    - 1936 年 Cambridge **物理**博士，论文 *The reflexion of very long wireless waves from the ionosphere*（电离层甚长无线电波的反射），导师 **John Ashworth Ratcliffe**
  - **任职**：
    - 二战期间在 Telecommunications Research Establishment (TRE) 从事雷达与运筹研究
    - 1945 年任 Cambridge Mathematical Laboratory（后改名 Computer Laboratory）**第二任主任**
    - 1957–1960 任英国计算机学会（BCS）**首任会长**（founder member & first president）
    - 1980 年退休后加入 Digital Equipment Corporation (DEC) 中央工程团队（美国马萨诸塞州 Maynard）
  - **核心成就（infobox Known for）**：EDSAC、Microprogramming（微程序）、Cache memory（缓存）
  - **关键事实**：
    - **EDSAC**（Electronic Delay Storage Automatic Calculator）：1946 年 8 月乘船赴美参加 Moore School Lectures（因行程延误只赶上最后两周），返程五天的航程中在纸上详细勾画了 EDSAC 的逻辑结构；回到剑桥后立即开工；**1949 年 5 月成功运行，是第二台完成的实用存储程序计算机**，比 EDVAC 早一年多
    - 1950 年与 David Wheeler 用 EDSAC 求解 Fisher 关于基因频率的微分方程，是**计算机首次用于生物学问题**
    - **1951 年提出微程序（microprogramming）概念**：用 ROM 中微型专用程序控制 CPU，极大简化 CPU 设计；1951 年曼彻斯特计算机会议首次描述，1955 年 IEEE Spectrum 发表；**首次实现于 EDSAC 2**（EDSAC 2 还用"位片 bit slices"简化设计）
    - 与 David Wheeler、Stanley Gill 合著 *Preparation of Programs for Electronic Digital Computers*（1951），**首次有效引入程序库（program libraries）**
    - 也 credited with 符号标号（symbolic labels）、宏（macros）、子程序库（subroutine libraries）—— 为高级编程语言铺路
    - 后期：Titan（1963 与 Ferranti 合作，UK 首个分时系统之一，启发自 CTSS，其密码加密系统后来被 Unix 采用）；Cambridge CAP（能力基安全计算机）；Cambridge Ring（1974 受瑞士 Hasler AG 环形拓扑网络启发，UK 广泛部署）
  - **荣誉（infobox Awards）**：Turing Award 1967 · Distinguished Fellow of BCS 1973 · Faraday Medal 1981 · Harold Pender Award 1982 · Mountbatten Medal 1997；另获 Knight Bachelor、FRS、FREng、Harry H. Goode Memorial Award 1968

### 第 1 步：建立目录 【模板通用】

- 已创建 `turing/presentations/Maurice_Wilkes/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 `Donald_Knuth/Makefile`（标杆实例），设置 `MAIN=Maurice_Wilkes_zh`、`VIDEO_NAME=Maurice_Wilkes_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 复制 `turing/pages/1967/Maurice Wilkes/images/Maurice_Vincent_Wilkes_1980_3_cropped_.jpg` 到 `presentations/Maurice_Wilkes/images/Wilkes.jpg`

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | computer architecture | 计算机体系结构 | EDSAC 存储程序计算机、EDSAC 2、Titan、CAP |
| 1 | microprogramming | 微程序 | 1951 发明，首次实现于 EDSAC 2 |
| 2 | programming systems | 编程系统 | 程序库、符号标号、宏、子程序库 |
| 3 | computer networks | 计算机网络与分布式 | Cambridge Ring、分布式计算 |

- 入库脚本：`MySQL/seed_wilkes_full.py`（people 新建 id，4 领域 + 国籍 + 职业）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John Ashworth Ratcliffe | 师→生 | 博士导师，Cambridge（物理/电离层） |
| colleague | David Wheeler | 无向 | EDSAC 合作、"Preparation of Programs"合著、Wheeler 是 Wilkes 的博士生 |
| colleague | Stanley Gill | 无向 | "Preparation of Programs"合著 |
| doctoral-student | David Wheeler | 师→生 | 知名博士生（Wheeler 延迟、EDSAC 2） |
| doctoral-student | Peter Wegner | 师→生 | 知名博士生 |
| doctoral-student | Michael Kay | 师→生 | 知名博士生（XSLT） |

- 入库脚本：`MySQL/seed_wilkes_relations.py`

### 第 5 步：设计配色方案 【人物专属】

- **气质**：工程 / 系统 / 开创（实用主义，"让计算机真正跑起来"）
- **配色**：图灵紫（品牌主色）+ 强调红 + 四分类色
  - `badgeArch` 计算机体系结构 — 蓝 `#2E5A9E`
  - `badgeMicro` 微程序 — 青绿 `#1E8E8E`
  - `badgeProg` 编程系统 — 琥珀 `#D9A441`
  - `badgeNet` 网络与分布式 — 玫瑰 `#C0395B`
- **背景母题**：柔和气泡（稀疏大块实心圆），呼应"工程务实"叙事

### 5.1 图灵奖格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。✅
2. **封面有国籍**：底部状态栏 `英国 | University of Cambridge · DEC | Turing 1967`；注意 Sir 爵位可标注。✅
3. **必须有身份信息页**：封面之后第 3 页，左头像 + 右 2×2 信息网格（含生卒/本名/国籍/师承/任职/出生地/教育/荣誉/核心领域）。✅
4. **品牌口径统一**：结尾页底部写 `OpenMathAI`；GitHub 链接由首页模板 `\input` 继承。✅

### 5.2 背景音乐 【人物专属】

- **气质定位**：工程 / 系统（实用存储程序计算机先驱、微程序）—— 史诗 / 工程感。
- **选定曲目**：Alex-Productions **New Lands**（史诗 / 开阔，匹配"建造第一台实用存储程序计算机"的奠基叙事），与 Knuth / Perlis 同曲。
- **落地文件**：`turing/presentations/Maurice_Wilkes/NewLands.wav`（复制自音乐库，不入 git）。

### 第 6 步：规划幻灯片序列 【人物专属】

```
00  OpenTuring 项目首页（\input cover/openturing_page.tex）
01  封面 — 主标题「莫里斯·威尔克斯」+ 英文名/生卒 + 四色 badge + 右上头像 + 国籍行（Sir 爵位）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格
03  核心贡献概览 — 体系结构/微程序/编程系统/网络
04  早年：达德利的无线电少年 (1913–1931)
05  Cambridge 数学 Tripos 与电离层博士 (1931–1936)
06  战时雷达与运筹：从物理到计算
07  1945 剑桥数学实验室主任与 von Neumann 的 EDVAC 报告
08  赴美 Moore School Lectures 与返程航程上的 EDSAC 草图
09  EDSAC：让第一台实用存储程序计算机跑起来 (1949)
10  程序库、符号标号与"Preparation of Programs"
11  微程序：用 ROM 中的小程序驾驭 CPU (1951)
12  EDSAC 2、Titan 与剑桥分时系统
13  剑桥环（Cambridge Ring）与晚年 DEC
14  荣誉与遗产：英国计算之父
15  结尾 — "我清楚地记得那个领悟第一次完全击中我的时刻"
16  彩蛋 — 本页由 XeLaTeX + Beamer 排版
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；四分类色与 `\plainbar`/`\deckbackground`/`\sectiontitle`/`\lab` 复用 Knuth/Thompson 标杆骨架。
- ⚠ 注意：命令名不能含"字母+数字+字母"歧义（如 `\\edsac2slide` 会解析失败），应写作 `\\edsacIIslide`。

### 第 8 步：布局检查 【模板通用】

- `make distclean && make` 返回 EXIT=0，16–18 页，无缺字、无致命溢出（仅 ≤9.53pt 轻微 Overfull，可接受）。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Wilkes 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| "first" 的语义 | ACM citation 称 EDSAC 是 "the first computer with an internally stored program"——此处指**实用、成功运行**的存储程序计算机；**Manchester Baby/SSEM 于 1948 年 6 月完成首次存储程序运行**，是"第一台运行存储程序的计算机"。勿把二者混淆，可表述为"第二台完成的实用存储程序计算机""第一台投入实际服务的存储程序计算机" |
| EDSAC 与 EDVAC | EDSAC 是 Wilkes 受 von Neumann 的 EDVAC 报告启发而建；EDVAC 由 Eckert & Mauchly 在 Moore School 建造，比 EDSAC 晚一年多才完成。勿写成"Wilkes 建造了 EDVAC" |
| 微程序年份 | 1951 年提出概念，1955 年 IEEE Spectrum 发表；**首次实现于 EDSAC 2**（非 EDSAC）。勿写成"在 EDSAC 上实现微程序" |
| 博士专业 | 博士是**物理**（电离层无线电波反射），非计算机（当时无 CS 博士）；本科为 Mathematical Tripos（数学） |
| 博士年份 | Wikipedia 内部矛盾：正文写 **1936** 年完成 PhD，infobox Thesis 标注 **1939**；本提示词采用正文的 1936，立传时如需标年份建议写"1930 年代中期"或注明 1936，避免与 infobox 的 1939 冲突 |
| 任职时序 | TRE（战时雷达）→ 1945 剑桥数学实验室主任 → BCS 首任会长（1957–1960）→ 1980 退休后加入 DEC |
| 合著者 | *Preparation of Programs for Electronic Digital Computers*（1951）与 **David Wheeler、Stanley Gill** 合著；Wheeler 同时是 Wilkes 的博士生 |
| 本名 | infobox 记 "John Maurice Vincent Wilkes"，常称 Maurice Wilkes；Sir（Knight Bachelor）。勿漏爵位或错写名字顺序 |
| 生卒 | 已故：1913-06-26 ~ 2010-11-29，写作 `1913–2010`，享年 97 |
| 荣誉 | 图灵奖 1967、Faraday Medal 1981、Pender 1982、Mountbatten 1997；**无** National Medal、无 IEEE 等（勿编造） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| EDSAC | EDSAC（电子延迟存储自动计算器） | Wilkes 设计与建造，1949 运行 |
| EDVAC | EDVAC | 启发源（von Neumann 报告），非 Wilkes 建造 |
| Microprogramming | 微程序 | Wilkes 1951 发明，EDSAC 2 首次实现 |
| Stored-program computer | 存储程序计算机 | EDSAC 是实用/服务级首台 |
| Manchester Baby / SSEM | 曼彻斯特婴儿机 | 1948 首次存储程序运行（区分用） |
| Moore School Lectures | 摩尔学院讲座 | 1946，Wilkes 只赶上最后两周 |
| Program library | 程序库 | Wilkes/Wheeler/Gill 1951 引入 |
| Cambridge Ring | 剑桥环 | 1974 网络，受 Hasler AG 启发 |
| Titan | Titan 计算机 | 1963 与 Ferranti，UK 早期分时 |

**遗产页布局红线（★ 实测踩坑，来自 Ken Thompson 立传）**：

- ⚠ **禁止用 2×2 网格 + `text width=5.6cm`**：下排卡片与底部总结框在 16:9 画布上**纵向重叠**。
- ✅ **必须对齐 Andrew_Yao / Leslie_Lamport 标杆的 1×4 横排布局**：四张小卡 `text width=3.05cm`、`node[leg] style` 含 `rounded corners=6pt, inner xsep=6pt, inner ysep=8pt, font=\fontsize{6.4}{8.4}`，横排 `x = -5.4 / -1.8 / 1.8 / 5.4`、`y=1.3`；底部总结框 `y=-1.6`、`text width=13.0cm`。经 `make distclean && make` 验证无重叠。

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（史诗 / 开阔）
- **来源**：与 Knuth / Perlis 标杆同曲（工程/奠基气质）；本地路径 `music_audio/alex-productions/...New Lands.wav` → `turing/presentations/Maurice_Wilkes/NewLands.wav`
- **匹配理由**："建造第一台实用存储程序计算机"的奠基叙事，匹配工程务实与开疆拓土的史诗感。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `turing/pages/1967/Maurice Wilkes/index.html` | 本地 Wikipedia 正文 |
| `turing/pages/1967/Maurice Wilkes/metadata.json` | 简化元数据 |
| `turing/presentations/Turing_Bio_Prompt_Template.md` | 图灵奖通用模板 |
| `turing/presentations/cover/openturing_page.tex` | 项目首页模板（统一 `\input`） |
| `turing/presentations/Donald_Knuth/Donald_Knuth_zh.tex` | 通用标杆实例 Beamer 源码 |
| `turing/turing_award_winners.md` | 图灵奖得主总名单（含立传/Review 标志位） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
