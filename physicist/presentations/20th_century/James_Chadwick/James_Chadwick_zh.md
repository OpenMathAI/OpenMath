# 物理学家立传提示词（James Chadwick）

> 本文件是 OpenPhysicist 20 世纪诺贝尔物理学奖得主的「人物专属立传提示词」，以 Kenneth G. Wilson 篇为结构母本（0–11 节骨架一致）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：James Chadwick（詹姆斯·查德威克，1935 诺贝尔物理学奖，中子的发现者）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Chadwick 篇的设计重心是**中性的粒子与沉默的测量者**——不带电荷的中子与不爱说话的查德威克互为镜像，立传以「两周实验改变原子核图像」为叙事脊柱。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Sir James Chadwick（1891-10-20 ~ 1974-07-24，享年 82 岁）
- **气质关键词**：**中子的发现者、英国核计划的掌舵人、沉默的实验大师** —— 1935 诺贝尔物理学奖获奖理由：
  > "For the discovery of the neutron."（因发现中子）
- **设计母题**：**穿透（penetration without charge）**。中子不带电荷故能穿透库仑壁垒进入任何原子核——「不动声色地改变一切」正是查德威克一生的写照：曼哈顿计划中几乎无人注意、却拿到除 Groves 外唯一的全设施通行权。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century/20th_century/James_Chadwick/page.md`（Wikipedia 全文已抓取）
- **待下载**：本目录尚无 `James_Chadwick.html` 与 `images/`，第 0 步需从 `https://en.wikipedia.org/wiki/James_Chadwick` 下载页面与肖像（infobox c.1945 照片）。
- **参考模板**：
  - 结构母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- page.md 已在本地（见上），**事实基准如下**（以 page.md 为唯一依据；frontmatter 生卒有噪声 `1891-01-01`/`1974-01-01`，以 infobox/正文 1891-10-20 / 1974-07-24 为准）：
  - 生卒（1891-10-20 生于英格兰柴郡 ~ 1974-07-24 逝于英格兰剑桥，睡梦中去世，享年 82 岁）
  - 国籍（英国）
  - 父母（父 John Joseph Chadwick 棉纺工；母 Anne Mary Knowles 佣工；幼年由外祖父母抚养）
  - 教育（Manchester Central Grammar School for Boys（曾获 Manchester Grammar School 奖学金、因付不起杂费放弃）→ 1908 入维多利亚曼彻斯特大学（本想读数学、误注册物理）→ 1911 一等荣誉毕业 → 1913 MSc（Beyer Fellow）→ 1851 奖学金赴柏林帝国物理技术研究所师从 Hans Geiger → 1921 剑桥 Gonville and Caius College 博士（导师 Rutherford））
  - 任职机构（1919 跟随 Rutherford 入卡文迪许实验室 → 1923 任 Rutherford 助理研究主任（逾十年）→ 1935-10-01 利物浦大学 Lyon Jones 物理学讲席教授（建回旋加速器）→ 1943-44 曼哈顿计划英国代表团团长（Los Alamos，化名 James Chaffee）→ 1948-1958 剑桥冈维尔与凯斯学院第 36 任院长）
  - 关键荣誉（FRS 1927、Hughes Medal 1932、Nobel 1935、Copley Medal 1950、Faraday Medal 1950、Franklin Medal 1951、Knight Bachelor 1945、Companion of Honour 1970、Pour le Mérite 1966、Medal of Freedom）
  - 家庭（1925-08 娶利物浦股票经纪人之女 Aileen Stewart-Brown，Kapitza 任伴郎；1927-02 生双胞胎女儿 Joanna 与 Judith）
  - 知名学生（博士生：Étienne Biéler、Albert Crewe、Maurice Goldhaber、John Riley Holt、Ernest C. Pollard；其他 notable：Charles Drummond Ellis、Norman Feather、Joseph Rotblat）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点）：1891 生 → 1908 入曼彻斯特 → 1912 与 Rutherford 合写首篇论文 → 1913 柏林 Geiger 处证实 β 连续谱 → 1914-18 鲁勒本拘留营（马厩实验室、放射性牙膏做实验）→ 1919 入卡文迪许 → 1920 Clerk Maxwell Studentship → 1921 博士 + Caius Fellow → 1923 助理研究主任 → 1925 结婚 → 1932-01 Feather 转来约里奥-居里论文 → 1932-02 Nature 快信 "Possible Existence of a Neutron" → 1932-05 PRSA 全文 "The Existence of a Neutron" → 1932 Hughes 奖章 → 1933 Bakerian 讲座估算中子质量 1.0067 → 1934 与 Goldhaber 氘核光致分裂定质量 → 1935 利物浦讲席 + 诺贝尔奖（奖金部分付回旋加速器）→ 1939-07 回旋加速器建成 → 1941-07 撰写 MAUD 报告终稿 → 1943 魁北克协定后任英国代表团团长 → 1945-01-01 封爵、1945-07-16 现场观看 Trinity 核试验 → 1946 联合国原子能委员会英方顾问 → 1948 出任 Caius 院长 → 1950 Copley/Faraday → 1958 退休 → 1974-07-24 剑桥逝世

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下使用本目录 `James_Chadwick/` 并创建 `images/`。

### 第 2 步：复制 Makefile 【模板通用】

- 复制参照成品 `Makefile`，设置 `MAIN=James_Chadwick_zh`、`VIDEO_NAME=James_Chadwick_zh`。

### 第 3 步：收集图片 【人物专属】

- 下载 infobox c.1945 肖像到 `images/`；404 用 Commons `Special:FilePath` 回退。可补插图：Groves 与 Chadwick 合影、卡文迪许实验室旧照。

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Chadwick 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nuclear physics | 核物理 | 中子的发现改变原子核图像 | 核心页 |
| 1 | radioactivity | 放射性 | 曼彻斯特时期 γ 吸收、核核电荷测量 | 早年页 |
| 2 | beta radiation | β 辐射 | 1914 证实 β 谱连续（柏林 Geiger 处） | 柏林页 |
| 3 | neutron physics | 中子物理 | 中子质量测量、钋铍源技术 | 核心页 |
| 4 | experimental physics | 实验物理 | 全程实验路线，反对 Big Science | 贯穿页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ernest Rutherford | 导师→本人 | 曼彻斯特本科导师 + 剑桥博士导师，卡文迪许同事 |
| advisor-student | Maurice Goldhaber | 本人→学生 | 博士生，氘核光致分裂法测中子质量 |
| advisor-student | Norman Feather | 本人→学生 | 其他 notable 学生，中子发现的关键提醒者 |
| advisor-student | Joseph Rotblat | 本人→学生 | 其他 notable 学生，战时雇于利物浦 |
| spouse | Aileen Stewart-Brown | 无向 | 1925 年结婚，Kapitza 任伴郎 |
| colleague | Hans Geiger | 无向 | 柏林博士后导师，β 连续谱合作 |
| colleague | John Cockcroft | 无向 | 卡文迪许同事、MAUD 委员会成员 |
| controversy | Patrick Blackett | 无向 | 战后原子能咨询委员会上就英国是否自研核武立场相左 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：内敛、坚实、金属灰绿
- **配色**：石板灰青（主色 `#2F4550`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeNucl` 核物理 — 石板灰青 `#2F4550`
  - `badgeNeut` 中子物理 — 钢青 `#46707E`
  - `badgeBeta` β 辐射 — 琥珀 `#E07B30`
  - `badgeWar` 战时科学 — 暗红 `#8B3A3A`
- **背景母题**：柔和气泡中以「无色圆点穿透色环」的中性粒子图形呼应设计母题。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）与国籍行。
2. 必须有身份信息页：左侧头像 + 右侧信息网格（生卒、本名、国籍、出生地、师承、任职、主要荣誉、核心领域），事实取自 page.md infobox，不得杜撰。
3. 结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 中子的发现者 / James Chadwick 1891–1974 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 中子 / β 连续谱 / 核电荷 / 战时科学
04  误入物理（1891–1913）— 数学志愿填成物理、Rutherford 门下、Beyer Fellow
05  柏林与拘留营（1913–1918）— Geiger、β 连续谱、Ruhleben 马厩实验室
06  卡文迪许十年（1919–1932）— Rutherford 助理研究主任、Gonville and Caius
07  1932：两周的中子（核心贡献页）— Bothe/Becker → Joliot-Curie 误判 → 钋铍源击中靶心
08  公式框页 — 铍核 α 轰击反应 ⁹Be + α → ¹²C + n（page.md 未给显式式，此为反应式图式并注明）
09  中子的质量 — Bakerian 1.0067、Goldhaber 光致分裂 1.0084/1.0090
10  利物浦与回旋加速器 — 诺贝尔奖金付加速器、反 Big Science、与 Lawrence 的 1933 索尔维交锋
11  MAUD 报告与曼哈顿 — "90 per cent sure"、英国代表团团长、化名 James Chaffee
12  门生与传承 — Goldhaber、Feather、Rotblat；Caius 院长任内的 DNA 之年
13  荣誉与认可 — Nobel 1935 · Copley 1950 · 封爵 1945 · CH 1970
14  遗产：从核图像到核时代
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；头部宏定义整体复用结构母本骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make distclean && make pdf`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Chadwick 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句 "For the discovery of the neutron."（独立得奖，非共享），勿写成"因核物理贡献"泛化 |
| 中子发现归属 | Bothe/Becker 首先产生异常辐射、Joliot-Curie 打出质子却误认 γ、Majorana 同结论未发表——Chadwick 的贡献是**两周确证与解释**；勿写成完全独立无前人，也勿把发现权让渡 |
| Pauli 的"中子" | 泡利 1930 提出的 "neutron" 后来被费米改名为 neutrino（中微子），与查德威克中子**不是同一粒子**，勿混 |
| 生卒噪声 | frontmatter 含 1891-01-01 / 1974-01-01 噪声，一律以 infobox/正文 1891-10-20 / 1974-07-24 为准 |
| 志愿误填 | 曼彻斯特本想读数学、误注册物理——有载可写，勿演绎为"命运注定" |
| 拘留营细节 | Ruhleben 期间用"放射性牙膏"等拼凑材料做实验为 page.md 明载，可写 |
| 奖金用途 | 诺贝尔奖金（159,917 kr，约 £8,243）部分支付了总价 £5,184 的回旋加速器——数字勿混（£700 修缮 + £2,000 大学 + £2,000 皇家学会） |
| Big Science | 1933 索尔维会议上质疑 Lawrence 的"新粒子"（后证为污染），且被证实正确——可写，但勿引申为"反对一切大型装置" |
| 同名区分 | 与 1946 化学奖 James B. Sumner 无关；与 R. W. Wilson/C.T.R. Wilson 无关；Caius 院长继任者是 Nevill Mott |
| Caius 岁月 | 任内 Francis Crick（该校博士生）等发现 DNA 双螺旋——是"任内"不是"指导"，勿写成参与 |
| 战时工作 | MAUD 终稿执笔 + 英国代表团团长 + 除 Groves 外唯一全设施通行权 + 无权进入 Hanford——细节多且易混，逐条对照 page.md |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| neutron | 中子 | 不带电核子，勿与 neutrino 混 |
| beta radiation | β 辐射 | 1914 连续谱发现 |
| continuous spectrum | 连续谱 | β 衰变谱 |
| polonium–beryllium source | 钋铍源 | 中子发现实验核心装置 |
| proton | 质子 | Joliot-Curie 打出的反冲粒子 |
| cyclotron | 回旋加速器 | 利物浦 50 吨磁体 |
| MAUD Report | MAUD 报告 | 1941 终稿执笔人 |
| Tube Alloys | 管合金（计划） | 英国原子弹计划代号 |
| Manhattan Project | 曼哈顿计划 | 英国代表团团长 |
| critical mass | 临界质量 | 1941 实验确认铀-235 可能 ≤8 kg |
| Trinity nuclear test | 三位一体核试验 | 1945-07-16 在场 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **PAST** — Alex-Productions（86k views）
- **风格**: 历史感 / 深沉 / 纪录片
- **匹配理由**: 查德威克的一生横跨拘留营、卡文迪许、曼哈顿与战后疲惫的英国——PAST 的历史感与深沉正匹配这位"沉默掌舵人"的世纪叙事，也呼应其晚年 "physically, mentally and spiritually tired" 的重量。
- **备选**（未采用）: Through the Darkness（突破前夕的推进感，匹配 1932 两周实验但已被多批使用）；The Flow of Time（时间感匹配但受众偏低）。
- **本地路径**: `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → `presentations/20th_century/James_Chadwick/PAST.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/James_Chadwick/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` | 人物 + 领域 + 关系入库引擎 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修；所有事实以 page.md 为准，无载禁写。**
