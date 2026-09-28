# 物理学家立传提示词（Manne Siegbahn）

> 本文件是 OpenPhysicist「物理学家立传提示词」的人物专属实例，以 Karl Manne Georg Siegbahn（1924 诺贝尔物理学奖，X 射线谱学）为对象。
> 结构对齐标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节），凡标注 `【模板通用】` 可复用，`【人物专属】` 为西格班定制品。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Karl Manne Georg Siegbahn（卡尔·曼内·乔治·西格班，通称 Manne Siegbahn）。
- **设计哲学**：物理学家立传必须有「身份信息页」与「研究领域」结构化表达；西格班篇是"精密测量学派"叙事——以谱仪精度的逐级提升为主线，呈现 X 射线谱学如何为量子理论与原子物理提供实验地基；父子双诺奖是天然的高光页。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Karl Manne Georg Siegbahn（1886-12-03 ~ 1978-09-26，享年 91 岁）
- **气质关键词**：**X 射线谱学的精密大师、Siegbahn 记号的立法者、瑞典实验物理的奠基者** —— 1924 诺贝尔物理学奖获奖理由（官方原文，禁改写）：
  > "for his discoveries and research in the field of X-ray spectroscopy"（表彰他在 X 射线谱学领域的发现与研究）
- **设计母题**：**谱线色散（dispersed spectral lines）**。一束 X 射线经晶体色散为精细谱线——K/L/M 系、α/β 分量在底片上依次排开；视觉上用渐变细线束与波长刻度呈现"越测越细"的精密美学。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Karl_Manne_Georg_Siegbahn/page.md`（Wikipedia 全文 + frontmatter）
- **待下载**：`https://en.wikipedia.org/wiki/Karl_Manne_Georg_Siegbahn` → `Karl_Manne_Georg_Siegbahn/Karl_Manne_Georg_Siegbahn.html`（本批人物暂无 html 与 images/，第 0/3 步需补下载）
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- 🔲 待下载 `https://en.wikipedia.org/wiki/Karl_Manne_Georg_Siegbahn` 到 `Karl_Manne_Georg_Siegbahn.html`
- 事实基准（已按本地 page.md 核对）：
  - 生卒：1886-12-03 生于瑞典 Örebro ~ 1978-09-26 卒于斯德哥尔摩，享年 91 岁（frontmatter 死亡日期有 09-24/09-26 两说，infobox 与正文均作 09-26，以正文为准）
  - 国籍：瑞典
  - 父母：父 Nils Reinhold Georg Siegbahn 为铁路站长（station master）；母 Emma Sofia Mathilda Zetterberg
  - 教育：1906 斯德哥尔摩毕业（Norra Real）入隆德大学；在校任 Johannes Rydberg 的秘书助理；1908 赴哥廷根大学；1911 隆德 PhD《Magnetische feldmessung》（磁场测量）
  - 博士导师：Johannes Rydberg（infobox 明载）
  - 任职：Rydberg 健康恶化期间代行教授职，1920 其去世后继任隆德正教授；1923 转乌普萨拉大学物理学教授；1937 任瑞典皇家科学院实验物理研究教授（该职 1988 年更名 Manne Siegbahn Institute，MSI）
  - 关键荣誉（含年份）：Björkén Prize 1919 与 1923（乌普萨拉大学；Notes 载分别与 Carl Wilhelm Oseen、Theodor Svedberg 共同获得）；Nobel 1924；Hughes Medal 1934（"for his work as a physicist and technician on long-wave X-rays"）；Rumford Medal 1940（高精度 X 射线谱学先驱工作）；Duddell Medal 1948；英国皇家学会外籍会员 1954
  - 学生：page.md 无博士学生名单（勿编造）
  - 主要著作：The Spectroscopy of X-Rays（1925，正文 Works 节唯一专著，附书影四幅）
  - 名下机构：1937 年研究教授职 1988 年更名 Manne Siegbahn Institute（MSI）；研究组经改组后，其名存于斯德哥尔摩大学主办的 Manne Siegbahn Laboratory
  - 核心贡献清单：①改良 X 射线谱仪实现高精度波长测量 ②发现 Moseley 谱线的多分量结构 ③据此几乎完整弄清电子壳层结构 ④创立特征谱线命名体系 Siegbahn notation ⑤发明分子拖拽泵（molecular drag pump）⑥精密测量推动量子理论与原子物理发展
  - 关键时间线（15 节点）：1886-12-03 生于 Örebro / 1906 斯德哥尔摩毕业入隆德大学 / 1908 哥廷根一学期 / 1911 隆德博士《Magnetische feldmessung》/ 1914 起转向 X 射线谱学（自 Moseley 谱仪起点） / 1919 Björkén Prize（与 Oseen）/ 1920 Rydberg 去世后继任隆德正教授 / 1923 转乌普萨拉大学教授 / 1923 Björkén Prize（与 Svedberg）/ 1924 诺贝尔物理学奖 / 1925-12-11 诺奖演讲 The X-ray Spectra and the Structure of the Atoms / 1925 出版 The Spectroscopy of X-Rays / 1937 任皇家科学院实验物理研究教授 / 1954 英国皇家学会外籍会员 / 1978-09-26 卒于斯德哥尔摩（享年 91 岁）
  - 家庭：1914 与 Karin Högbom 结婚；长子 Bo Siegbahn（1915–2008，外交官与政治家）；次子 Kai Siegbahn（1918–2007，物理学家，1981 诺贝尔物理学奖——X 射线光电子能谱 XPS）

### 第 1 步：建立目录 【模板通用】

- 已存在 `physicist/presentations/20th_century/Karl_Manne_Georg_Siegbahn/`，补建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Karl_Manne_Georg_Siegbahn_zh`、`VIDEO_NAME=Karl_Manne_Georg_Siegbahn_zh`

### 第 3 步：收集图片 【人物专属】

- 🔲 待下载西格班肖像（Wikipedia infobox 1924 年照）到 `images/Siegbahn.jpg`，curl 带 `-A "Mozilla/5.0"` 并 `file` 验证；《The Spectroscopy of X-Rays》1925 书影可作著作页插图

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Siegbahn 的研究领域（按 rank 排序，与 yaml 完全一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | X-ray spectroscopy | X 射线谱学 | 1924 诺奖核心 | 核心页 |
| 1 | atomic physics | 原子物理 | 电子壳层结构的实验地基 | 壳层页 |
| 2 | spectroscopy | 光谱学 | 谱仪改良与谱线测量 | 谱仪页 |
| 3 | precision measurement | 精密测量 | 高精度波长测量推动量子理论 | 精密页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Johannes Rydberg | 对方是导师 | 隆德大学博士导师，曾任其秘书助理 |
| spouse | Karin Högbom | 无向 | 1914 年结婚 |
| parent-child | Kai Siegbahn | 无向 | 之子，物理学家，1981 诺贝尔物理学奖（XPS） |
| co-honored | Carl Wilhelm Oseen | 无向 | 乌普萨拉大学 Björkén Prize 共同得主 |
| co-honored | Theodor Svedberg | 无向 | 乌普萨拉大学 Björkén Prize 共同得主 |

#### 4.5.1 入库操作

- `cd MySQL && python3 seed_person.py data/Karl_Manne_Georg_Siegbahn.yaml`
- 方向约定：师生有向；配偶/亲子/共同荣誉无向；缺失人物自动建 stub

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：精密、冷冽、北欧
- **配色**：X 射线紫罗兰（主色，批内专属 `#4B3F8C`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeXray` X 射线谱学 — 紫罗兰 `#6C5CE7`
  - `badgeShell` 电子壳层 — 石墨青 `#2C7A7B`
  - `badgeInstr` 谱仪与仪器 — 钢灰蓝 `#4A6FA5`
  - `badgeFamily` 父子传承 — 瑞典金 `#D4A017`
- **背景母题**：色散谱线束——一组从左向右渐细的平行亮线，模拟 X 射线底片上的 K/L/M 系谱线排布

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — X 射线谱学奠基人 / Manne Siegbahn 1886–1978 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 高精度谱仪 / 谱线多分量 / 电子壳层 / Siegbahn 记号
04  站长之子与 Rydberg 助理 (1886–1911) — Örebro、隆德、哥廷根、磁场测量博士
05  转向 X 射线 (1914) — 从 Moseley 的起点出发
06  精密谱学（核心贡献页）— 谱仪改良、Moseley 谱线的多分量结构（page.md 无公式，公式框放 Siegbahn notation 能级图式并注明为概念图）
07  电子壳层的实验拼图 — "几乎完整的电子壳层理解"、量子理论与原子物理的实验地基
08  Siegbahn 记号 — K/L/M 系与 α/β 命名体系
09  隆德 → 乌普萨拉 → 皇家科学院 (1920–1937) — 教席变迁与 MSI 前身
10  发明家侧面 — 分子拖拽泵（molecular drag pump）
11  父子双诺奖 — Kai Siegbahn 与 XPS（1981）、Bo 的外交官生涯
12  荣誉与认可 — Nobel 1924 · Hughes 1934 · Rumford 1940 · Duddell 1948 · 皇家学会外籍会员 1954
13  著作与遗产 — The Spectroscopy of X-Rays (1925)、Manne Siegbahn Laboratory
14  结尾
```

### 第 7–8 步：编写 Beamer 源码与布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照标杆 `\profileslide`；头部宏复用 `Kenneth_G_Wilson_zh.tex` 骨架
- 每写完一页 `make` 并 `pdftoppm` 目检；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距
- 身份信息页信息网格至少含：生卒、国籍、出生地、师承、任职、主要荣誉、核心领域（事实取自 infobox，不得杜撰）
- 封面右上肖像加 `draw=coveraccent!50` 细边框 + 姓名小字注；底部状态栏三要素 `国籍 | 机构 | 主要奖项`
- 结尾页底部品牌标注统一写 `OpenMathAI`（不是 OpenPhysicist）；引号用半角 `" "`
- 表格页安全负间距经验：顶部 -0.35cm、`arraystretch` 0.78-0.82；公式框前 -0.35~-0.55cm
- 记住 `\foreach` 时间线分隔符必须用 ASCII 逗号（中文逗号会吞条目）

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Siegbahn 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方原文 "for his discoveries and research in the field of X-ray spectroscopy"，禁改写 |
| 卒日噪声 | frontmatter 有 09-24/09-26 两说；infobox 与正文均作 1978-09-26 → 以正文为准 |
| Björkén Prize 级别 | 是乌普萨拉大学的奖项（1919 与 1923 两度），Notes 明载分别与 Oseen、Svedberg 共同获得——勿拔高为国际大奖，勿与诺奖混淆 |
| 学生名单 | page.md 无博士学生名单——禁编造门生页；传承素只能用家庭（Kai/Bo） |
| 分子拖拽泵 | Known for 明载 molecular drag pump，可作仪器侧写页，勿夸大为真空技术革命 |
| Rumford 授奖词 | 正文原文含拼写错误 "poioneer [sic]"——引用时可保留原拼写并注 [sic] |
| 无载禁写 | page.md 未载诺奖竞选内幕、未载与 Moseley 的私人交往细节（仅提及其谱仪与谱线关系）、未载二战经历——一律不写 |
| 父子诺奖 | Kai 获 1981 年奖（XPS 方法），与父亲 1924 年奖（X 射线谱学）领域相关但不同——表述勿混 |
| 通称 | 国际通称 Manne Siegbahn，全名 Karl Manne Georg Siegbahn；入库用全名（分批文件口径） |
| 谱仪技术口径 | 正文称其"改良实验装置实现高精度测量"并"发现 Moseley 谱线由多分量构成"——勿写成"发明 X 射线谱仪" |
| 与玻尔学派关系 | 正文仅载其精密测量"推动量子理论与原子物理发展"，未载与玻尔研究所的直接交往——勿编造合作叙事 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| X-ray spectroscopy | X 射线谱学 | 诺奖理由用词 |
| Siegbahn notation | 西格班记号 | K/L/M 壳层与 α/β 谱线命名体系 |
| characteristic X-rays | 特征 X 射线 | 与元素一一对应 |
| electron shell | 电子壳层 | 其测量的结构对象 |
| spectrometer | 谱仪 | 改良对象，勿译"分光计"泛称 |
| molecular drag pump | 分子拖拽泵 | 其仪器发明 |
| long-wave X-rays | 长波 X 射线 | Hughes Medal 授奖词用词 |
| X-ray photoelectron spectroscopy | X 射线光电子能谱（XPS） | 属于 Kai 的贡献，须标注清楚 |
| Björkén Prize | 比约肯奖 | 乌普萨拉大学奖 |
| foreign member | 外籍会员 | 英国皇家学会 1954 |
| spectral line components | 谱线分量 | 对 Moseley 单线结论的修正 |
| wavelength measurement | 波长测量 | 高精度路线的方法论标签 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions（75k views）
- **风格**: 高受众 / 流动 / 平稳
- **匹配理由**:
  - "流动/平稳" 匹配精密测量的气质——谱线徐徐展开，六十年科学生涯平稳绵长（19 岁入隆德到 91 岁辞世）
  - 北欧海洋意象贴合瑞典科学传统，与"谱线色散"母题的横向线条感一致
  - 批内唯一使用，不与其他四位重复
- **本地路径**: `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` → 复制为 `presentations/20th_century/Karl_Manne_Georg_Siegbahn/SEA.wav`
- **时长**: 足覆盖 15 页 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Karl_Manne_Georg_Siegbahn/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Karl_Manne_Georg_Siegbahn.yaml` | 研究领域 + 社会关系入库文件 |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 qid → name_en 匹配） |

> **开始执行。每完成一步向主控汇报。**
