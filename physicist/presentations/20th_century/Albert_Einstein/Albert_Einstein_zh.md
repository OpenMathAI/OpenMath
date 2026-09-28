# 物理学家立传提示词（模板标杆实例：Albert Einstein）

> **本文件是 OpenPhysicist 的「物理学家立传提示词模板标杆」的人物专属实例**，目标人物为 Albert Einstein（1921 诺贝尔物理学奖，相对论创立者、光电效应定律的发现者）。
> 凡标注 `【模板通用】` 的部分可原样复用到任何物理学家；标注 `【人物专属】` 的部分需按本文件内容替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆（Hilbert / Grothendieck 的提示词 + tex 结构）与物理学家侧首例（Eugene Wigner）的实战经验。
- **本实例**：Albert Einstein（阿尔伯特·爱因斯坦）。
- **设计哲学**：物理学家立传与数学家立传的核心差异，在于**物理学家必须有「身份信息页」（Identity / Bio 速览页）**，且强调「研究领域」的结构化表达——这两点构成物理学家模板的骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Albert Einstein（1879-03-14 ~ 1955-04-18，享年 76 岁）
- **气质关键词**：**相对论的创立者、光电效应定律的发现者、世纪良心** —— 1921 诺贝尔物理学奖获奖理由（官方英文原文，禁止改写）：
  > "for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect"（因他对理论物理学的贡献，尤其是发现了光电效应定律）
- **设计母题**：**弯曲的时空（curved spacetime）**。引力不是力，而是质量使时空弯曲——视觉语言可用「网格在球体附近下陷变形」贯穿全篇；副母题为「光」——光电效应、光速不变、引力使光线弯曲。
- **本地 Wikipedia**：`physicist/presentations/20th_century/20th_century/Albert_Einstein/page.md`（已有全文）
  - `{Dir}.html` 与 `images/`：**待下载**（Wikipedia URL: `https://en.wikipedia.org/wiki/Albert_Einstein`）
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（16 页）
  - 数学家标杆：`mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- `{Dir}.html` **待下载**：`https://en.wikipedia.org/wiki/Albert_Einstein`（page.md 已有全文可先建立事实基准）
- 头像 **待下载**（可用 1921 年官方诺奖像或 1935 年 Princeton 像，下载到 `images/`）
- 提取 infobox 与正文，事实基准如下（源自 page.md）：
  - 生卒（1879-03-14 生于德意志帝国符腾堡王国乌尔姆 ~ 1955-04-18 逝于普林斯顿医院——腹主动脉瘤破裂后拒绝再手术，享年 76 岁；遗体特伦顿火化、骨灰撒于未公开地点）
  - 公民权变迁（符腾堡→1896-01 无国籍→1901-02 瑞士（终身保留）→1914 普鲁士/德国（1913-07-24 入普鲁士科学院）→1933-03-28 安特卫普交回护照放弃→1940 美国公民）
  - 父母（父 Hermann Einstein——销售员兼工程师，与叔父 Jakob 在慕尼黑创办直流电气设备厂；母 Pauline Koch；1880 迁慕尼黑，1894 迁意大利米兰/帕维亚）
  - 教育（圣彼得天主教小学、Luitpold 文理中学；1894 年底持医生证明退学赴帕维亚；1895 报考 ETH 总分未达标但物理数学出色，入阿劳州立中学，1896-09 Matura（物理/代数/几何/画法几何/历史满分）；1896 十七岁入 ETH 数学物理师范专业，1900 毕业；1905-04-30 完成苏黎世大学博士论文《Eine neue Bestimmung der Moleküldimensionen》（题献 Marcel Grossmann），1906-01-15 正式授博士）
  - 博士导师（Alfred Kleiner——苏黎世大学；infobox 其他学术导师：Heinrich Friedrich Weber——ETH）
  - 主要任职机构（伯尔尼瑞士专利局 1902–1909：三级技术专家→1903 转正→1906 二等；伯尔尼大学 Privatdozent 1908；苏黎世大学副教授 1909；布拉格德意志大学正教授 1911；ETH 理论物理讲席 1912–1914；普鲁士科学院院士 + 洪堡大学教授 1914–1933；威廉皇帝物理研究所首任所长 1917–1933；德国物理学会主席 1916–1918；普林斯顿高等研究院 IAS 1933–1955，首批四位教授之一）
  - 关键荣誉（Nobel 物理学奖 1921 年奖、1922 年颁发；Barnard Medal 1920；Matteucci Medal 1921；皇家学会外籍会员 1921；Copley Medal 1925；皇家天文学会金质奖章 1926；Max Planck Medal 1929；NAS 院士 1942；《时代》世纪人物 1999；元素 Einsteinium 1955 年命名）
  - 家庭（1903-01 与 Mileva Marić 结婚——1902 年初生女 Lieserl 下落不明；1904 长子 Hans Albert 生于伯尔尼；1910 次子 Eduard 生于苏黎世，后确诊精神分裂症；1919-02-14 离婚，依协议诺奖奖金归 Marić；1919 与表亲 Elsa Löwenthal 结婚，1936-12 Elsa 去世）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（20 个节点）：1879 生于乌尔姆 → 1880 迁慕尼黑 → 五岁病中得指南针 → 十二岁自学微积分、十三岁读康德 → 1894 退学赴意大利 → 1896 Matura + 入 ETH → 1902 专利局任职 + 组「奥林匹亚学院」→ 1901 首篇论文（毛细现象）→ 1902–1903 热力学统计两文 → 1905 奇迹年四文 → 1906 授博士 + 升等 → 1908 伯尔尼 Privatdozent → 1909 苏黎世副教授 → 1911 布拉格教授 + 首算光线偏折 + 首届索尔维 → 1912 回 ETH（Grossmann 协助黎曼几何）→ 1913 Planck/Nernst 亲赴苏黎世相邀 → 1914 迁柏林 → 1915-11 场方程完成 → 1916 引力波预言 → 1917 宇宙学常数 + 受激辐射 → 1919 日食验证 → 1921 诺贝尔奖（1922 领）→ 1924 Bose–Einstein → 1933 流亡入 IAS → 1939 致罗斯福信 → 1940 美国公民 → 1955 Russell–Einstein 宣言、04-18 逝世

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Albert_Einstein/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录 `Eugene_Wigner/Makefile`，设置 `MAIN=Albert_Einstein_zh`、`VIDEO_NAME=Albert_Einstein_zh`

### 第 3 步：收集图片 【人物专属】

- 头像 **待下载**：优先 Wikipedia infobox 照片（1947 年像）或 1921 诺奖官方像（Commons `Special:FilePath` / REST API）
- 可用插图（page.md 明载）：1882 童年照、1896 Matura 成绩单、1904 专利局照、1919 日食照片、1921 抵纽约照、1927 索尔维会议合影（居中者）、1931 与 Chaplin 同框、1939 致罗斯福信影印件、1951 吐舌照

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

**Einstein 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | theoretical physics | 理论物理 | 毕生主战场；诺奖理由首句 | 全篇 |
| 1 | theory of relativity | 相对论 | 1905 狭义 + 1915 广义 | 相对论页 |
| 2 | quantum theory | 量子理论 | 光量子、受激辐射、Bose–Einstein、EPR | 量子页 |
| 3 | statistical mechanics | 统计力学 | 1902–1905 奠基、布朗运动、临界乳光 | 统计页 |
| 4 | cosmology | 宇宙学 | 1917 宇宙学常数、现代宇宙学起点 | 宇宙页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Alfred Kleiner | 师→生（博士导师） | 苏黎世大学博士论文认可者，1909 力邀其回苏黎世任教 |
| advisor-student | Heinrich Friedrich Weber | 师→生（导师） | ETH 时期学术导师（infobox 载） |
| colleague | Marcel Grossmann | 无向 | ETH 同学：助其谋专利局职位、博士论文题献者、广义相对论数学协助者 |
| colleague | Max Planck | 无向 | 最先接受狭义相对论；1913 与 Nernst 亲赴苏黎世相邀；柏林家中常合奏音乐 |
| colleague | Walther Nernst | 无向 | 1913 与 Planck 共同赴苏黎世相邀 |
| controversy | Niels Bohr | 论战双方 | 玻尔–爱因斯坦论战：就量子力学完备性公开交锋，EPR 思想实验源于 1930 与 Bohr 之辩 |
| colleague | Satyendra Nath Bose | 无向 | 1924 译投 Bose 论文并推广至原子，创立玻色–爱因斯坦统计/凝聚 |
| colleague | Nathan Rosen | 无向 | 1935 EPR 悖论与 Einstein–Rosen 桥（虫洞）合作者 |
| colleague | Boris Podolsky | 无向 | 1935 EPR 悖论合作者 |
| colleague | Leó Szilárd | 无向 | 1926 共同发明吸收式「爱因斯坦冰箱」（1930 专利）；1939 共同署名致罗斯福信 |
| colleague | Wander Johannes de Haas | 无向 | 1915 爱因斯坦–德哈斯效应实验合作者（其唯一亲手做成的实验） |
| colleague | Otto Stern | 无向 | 其助手；1913 合作氢分子比热与零点能研究，发表后即撤回支持 |
| colleague | Kurt Gödel | 无向 | IAS 挚友，常散步长谈 |
| colleague | Hendrik Lorentz | 无向 | page.md 称其 former physics professor；国际智力合作委员会同事 |
| colleague | Marie Curie | 无向 | 国际智力合作委员会（国际联盟）同事 |
| colleague | Leopold Infeld | 无向 | 长期合作者，《The Evolution of Physics》合著者 |
| colleague | Peter Bergmann | 无向 | 长期合作者 |
| spouse | Mileva Marić | 无向 | 1903-01 结婚，1919-02-14 离婚；诺奖奖金依协议归 Marić |
| spouse | Elsa Löwenthal | 无向 | 母系堂亲+父系二级表亲，1919 结婚，1936-12 去世 |
| parent-child | Hans Albert Einstein | 父→子 | 长子，1904 生于伯尔尼 |
| parent-child | Eduard Einstein | 父→子 | 次子，1910 生于苏黎世，约二十岁时确诊精神分裂症 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深邃、开阔、人格张力
- **配色**：深紫罗兰（思想深度与人文情怀）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeRel` 相对论 — 靛蓝 `#4C5FD5`
  - `badgeQuan` 量子理论 — 琥珀 `#E07B30`
  - `badgeCos` 宇宙学 — 玫瑰 `#C4204F`
  - `badgeHum` 和平与公义 — 青绿 `#0E7C7B`
- **背景母题**：弯曲网格（稀疏的时空网格线在圆球附近下陷），呼应「质量使时空弯曲」的广义相对论图景（与第 2 步设计母题一致）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍（含变迁）、出生地、师承、任职、主要荣誉、核心领域。事实取自 page.md，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 相对论创立者 / Albert Einstein 1879–1955 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含出生地 Ulm、公民权变迁、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 狭义/广义相对论 / 光量子 / Bose–Einstein（公式框：E = mc²，"世界最著名的方程"）
04  早年：乌尔姆→慕尼黑→帕维亚 (1879–1895) — 指南针、十二岁自学微积分、退学赴意大利
05  阿劳与苏黎世理工 (1895–1900) — Matura 满分科目、ETH 师范专业、Mileva 与 Grossmann
06  专利局与奥林匹亚学院 (1902–1909) — 三级技术专家、Poincaré/Mach/Hume 读书会
07  1905 奇迹年（核心贡献页，公式框 E = mc²）— 光电效应/布朗运动/狭义相对论/质能等价四文
08  从狭义到广义 (1907–1915) — 等效原理、Grossmann 的黎曼几何、1915-11 场方程
09  1919：日食验证与世纪名人 — Eddington、Príncipe/Sobral、《泰晤士报》头条
10  量子之路与论战 — 光量子遭拒、受激辐射与激光、Bose–Einstein、与 Bohr 论战（1927 索尔维合影）
11  宇宙学常数 — 1917 静态宇宙、"最大错误"传说辨伪（Gamow 转述，Livio 质疑）
12  柏林岁月与家庭 — 1913 受邀柏林、两段婚姻、三名子女、诺奖钱归 Marić
13  流亡 (1933) — 纳粹抄家/焚书/悬赏、放弃国籍、Churchill 会面援救、入 IAS
14  致罗斯福的信与悔意 — Einstein–Szilárd letter、曼哈顿计划、1954 对 Pauling 引语、1955 Russell–Einstein 宣言
15  公义之声 — NAACP、Lincoln University、为 Marian Anderson 让宅
16  晚年与身后 — 统一场论未竟、1955-04-18 普林斯顿逝世、Einsteinium、遗产归希伯来大学
17  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）可整体复用标杆骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Einstein 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖口径 | **1921 年奖、1922 年才颁发**（当年无人达标顺延）；理由是光电效应定律而非相对论（委员会对相对论仍有疑虑）；授奖词未认可光的粒子性——四层口径勿混 |
| 诺奖钱去向 | 依 1919 离婚协议诺奖奖金归 Mileva Marić，有载可写 |
| 可引原话 | 仅 "God does not play dice" 与 1954 对 Pauling 的 "I made one great mistake..." 两处英文原句可引；其余「名言」多系误传（page.md 明言 misattributed 泛滥），禁编引语 |
| ETH 入学 | 1895 报考 **总分未达标**（仅物理数学出色），经阿劳中学补学后入学——勿写成「破格神童」 |
| 专利局职衔 | 三级技术专家→1903 转正→1906 二等技术专家；勿写成「职员」或「局长」 |
| 年份链 | 等效原理 1907、光线偏折首算 1911、场方程 1915-11、引力波 1916、宇宙学常数 1917——五级年份勿互串 |
| Entwurf 弯路 | 1913 与 Grossmann 的 Entwurf 理论是失败草案（1915-11 弃），勿略去或写成成功阶段 |
| "最大错误" | 「宇宙学常数是最大错误」出自 Gamow 转述、被 Livio 质疑无实据——引用须注记存疑 |
| Lieserl | 1902 年初生于诺维萨德，**下落不明**（1903 信中或送人或死于猩红热）——禁编结局 |
| 1922 亚洲行 | 日记对中日印人群有贬损记述（page.md 明载）——本篇不必展开，若提及须客观注明；禁为其辩护亦禁渲染 |
| 以色列总统 | 1952 Weizmann 去世后受邀、**婉拒**——勿写「被任命」 |
| 曼哈顿计划 | 只写「其信件被视为美国启动核武器研究的关键推动」——Einstein 本人未参与（page.md 无载），禁写「参与研制原子弹」 |
| Konenkova | Margarita Konenkova「间谍」说出自已被质疑的回忆录（page.md 注明 discredited），禁采用 |
| 无载禁写 | Besso、家族其他成员细节、100+ 本传记细节——均禁引入 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| photoelectric effect | 光电效应 | 诺奖理由核心，勿与 Compton 效应混 |
| special / general relativity | 狭义/广义相对论 | 狭义 1905、广义 1915 |
| mass–energy equivalence | 质能等价 | E=mc²，出自狭义相对论 |
| equivalence principle | 等效原理 | 1907，广义相对论起点 |
| cosmological constant | 宇宙学常数 | 1917 引入，1929 后放弃 |
| gravitational waves | 引力波 | 1916 预言，2015 LIGO 探测 |
| Bose–Einstein statistics / condensate | 玻色–爱因斯坦统计/凝聚 | 1924；凝聚 1995 实验证实 |
| EPR paradox | EPR 悖论 | 1935，量子信息论基石 |
| Einstein–Rosen bridge | 爱因斯坦–罗森桥 | 虫洞模型，1935，不稳定 |
| annus mirabilis | 奇迹年 | 1905，物理学史类比 1666 牛顿 |
| Olympia Academy | 奥林匹亚学院 | 伯尔尼读书会，自嘲式命名 |
| Institute for Advanced Study | 普林斯顿高等研究院（IAS） | 勿与 Princeton University 混 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Eternals** — Alex-Productions
- **风格**: 宏大 / 深远 / 长期影响
- **匹配理由**:
  - 「宏大」匹配相对论重塑时空观的体量——一位人物改写了自牛顿以来物理学的基本框架
  - 「深远/长期影响」匹配其遗产——从 GPS 到引力波探测（1916 预言 → 2015 验证），其思想仍在持续兑现
  - 「世纪人物」的一生配「长期影响」主题曲，是人物史系列的自然顶点之一
- **备选** (未采用):
  - ★★ New Lands — 「史诗/开阔」匹配流亡与新大陆，但「长期纲领」感弱于 Eternals
  - ★★ Ascension — 「上升/史诗」匹配 1919 成名后的升华，但受众偏低
- **本地路径**: `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` → `presentations/20th_century/Albert_Einstein/Eternals.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Albert_Einstein/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 标杆 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex` | 物理学家首例成品参考 |
| `mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex` | 数学家标杆参考 |
| `MySQL/seed_person.py` | 人物主记录 + fields/relations 入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**

