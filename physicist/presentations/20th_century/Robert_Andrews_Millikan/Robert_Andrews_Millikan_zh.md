# 物理学家立传提示词（Robert A. Millikan）

> 本文件是 OpenPhysicist「物理学家立传提示词」的人物专属实例，以 Robert Andrews Millikan（1923 诺贝尔物理学奖，基本电荷与光电效应）为对象。
> 结构对齐标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节），凡标注 `【模板通用】` 可复用，`【人物专属】` 为密立根定制品。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Robert Andrews Millikan（罗伯特·安德鲁斯·密立根）。
- **设计哲学**：物理学家立传必须有「身份信息页」与「研究领域」结构化表达；密立根篇是"实验物理学家 + 科学院缔造者"双线叙事——油滴实验的精密之美与 Caltech 从 Throop 小校到研究重镇的转型史并重，争议段落（Fletcher、数据取舍、优生学）须按正文客观呈现。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Robert Andrews Millikan（1868-03-22 ~ 1953-12-19，享年 85 岁）
- **气质关键词**：**电子电荷的测量者、光电方程的验证者、Caltech 的缔造者** —— 1923 诺贝尔物理学奖获奖理由（官方原文，禁改写）：
  > "for his work on the elementary charge of electricity and on the photoelectric effect"（表彰他对基本电荷与光电效应的工作）
- **设计母题**：**悬浮的油滴（suspended droplet）**。带电油滴在重力与电场间悬停——个体微小却承载了基本电荷的普适秘密；视觉上用悬浮微粒、电场线与刻度盘呈现"以小测大"的实验美学。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Robert_Andrews_Millikan/page.md`（Wikipedia 全文 + frontmatter）
- **待下载**：`https://en.wikipedia.org/wiki/Robert_Andrews_Millikan` → `Robert_Andrews_Millikan/Robert_Andrews_Millikan.html`（本批人物暂无 html 与 images/，第 0/3 步需补下载）
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- 🔲 待下载 `https://en.wikipedia.org/wiki/Robert_Andrews_Millikan` 到 `Robert_Andrews_Millikan.html`
- 事实基准（已按本地 page.md 核对）：
  - 生卒：1868-03-22 生于伊利诺伊州 Morrison ~ 1953-12-19 卒于加州 San Marino，享年 85 岁；葬 Glendale 的 Forest Lawn 纪念园"荣誉庭院"
  - 国籍：美国
  - 父母：父 Silas Franklin Millikan 为公理会牧师；母 Mary Jane Andrews
  - 教育：Maquoketa 高中；Oberlin College 1891 BA / 1893 MA（希腊教授指派教物理而入门，1889 暑期自修 Avery《物理学原理》）；Columbia 1895 PhD，论文《On the polarization of light emitted from the surfaces of incandescent solids and liquids》
  - 博士导师：Ogden Rood（infobox 明载）；frontmatter 另列 Albert Abraham Michelson（芝加哥大学前辈）
  - 博士后：1895-96 赴德国柏林、哥廷根各半年
  - 任职：1896 芝加哥大学助理 → 1910 物理学教授；1917 起应 George Ellery Hale 之邀每年数月赴 Throop College；1921 完全转任 Caltech，任 Norman Bridge 物理实验室主任（至 1945 退休）兼执行委员会主席（Caltech 治理机构首脑，1921–1945）
  - 战时：一战国家研究委员会副主席，研发反潜与气象装置；离心机枪设计指控曾被调查，后由 McIntyre 复查洗清
  - 关键荣誉（含年份）：Comstock Prize 1913；Edison Medal 1922；Nobel 1923；Hughes Medal 1923；Matteucci 1925；ASME Medal 1926；Franklin Medal 1937；Oersted Medal 1940；Medal for Merit 1949（杜鲁门颁发）；中国采玉勋章 1940
  - 会员：American Philosophical Society 1914、American Academy of Arts and Sciences 1914、NAS 1915、OSA 荣誉会员 1950
  - 知名学生（infobox Doctoral students 明载者择要）：Harvey Fletcher（油滴实验共同完成者）、Carl David Anderson（1936 诺奖）、Ira Bowen、Arthur Dempster、Charles Lauritsen、Luke Chia-Liu Yuan（袁家骝）
  - 核心贡献清单：①油滴实验（1909–1913，与 Harvey Fletcher，测得 e=1.592×10⁻¹⁹ C，证明电荷量子化）②光电效应十年实验计划（1914/1916 发表，逐点验证 Einstein 方程并测 Planck 常数）③"cosmic rays"一词的创造者（正文 coined）④引进物理教科书改革（概念性问题导向）⑤缔造 Caltech 研究型大学
  - 关键时间线（17 节点）：1868 生于 Morrison / 1886 入 Oberlin / 1889 代课物理自修入门 / 1891 BA / 1893 MA / 1895 哥伦比亚博士 / 1895-96 德国游学 / 1896 入芝加哥大学 / 1902 与 Greta Irvin Blanchard 结婚 / 1909-13 油滴实验 / 1910 教授 / 1913 Comstock Prize / 1914-16 光电效应验证 / 1917 应 Hale 之邀赴 Throop / 1921 转 Caltech 任实验室主任与执委会主席 / 1923 诺贝尔奖 / 1930s 宇宙线论战（Compton 正确）/ 1938 Westinghouse 时间胶囊题词 / 1945 退休 / 1949 Medal for Merit / 1953-12-19 卒于 San Marino

### 第 1 步：建立目录 【模板通用】

- 已存在 `physicist/presentations/20th_century/Robert_Andrews_Millikan/`，补建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Robert_Andrews_Millikan_zh`、`VIDEO_NAME=Robert_Andrews_Millikan_zh`

### 第 3 步：收集图片 【人物专属】

- 🔲 待下载密立根肖像（Wikipedia infobox 1923 年照或 Commons `Robert_A._Millikan_1924.png`）到 `images/Millikan.jpg`，curl 带 `-A "Mozilla/5.0"` 并 `file` 验证；油滴装置照片 `Millikan's_oil-drop_apparatus_1.jpg` 可作插图页素材

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Millikan 的研究领域（按 rank 排序，与 yaml 完全一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | experimental physics | 实验物理 | 油滴实验式的精密测量传统 | 核心页 |
| 1 | photoelectric effect | 光电效应 | 验证 Einstein 方程并测 Planck 常数 | 光电页 |
| 2 | cosmic rays | 宇宙线 | 术语创造者，光子说论战一方 | 宇宙线页 |
| 3 | physics education | 物理教育 | 影响深远的教科书系列与 Caltech 缔造 | 教育页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ogden Rood | 对方是导师 | 哥伦比亚大学博士导师，白炽光偏振论文（1895） |
| advisor-student | Albert Abraham Michelson | 对方是导师 | frontmatter 明载的博士导师之一，芝加哥大学前辈 |
| advisor-student | Harvey Fletcher | 对方是学生 | 研究生，油滴实验共同完成者 |
| advisor-student | Carl David Anderson | 对方是学生 | 博士学生，1936 诺贝尔物理学奖得主 |
| colleague | George Ellery Hale | 无向 | 天文学家，1917 邀其共建 Throop（Caltech 前身） |
| colleague | Albert Einstein | 无向 | 光电方程的实验验证者，1932 Caltech 合影 |
| controversy | Arthur Compton | 无向 | 1930s 宇宙线本性论战（光子 vs 带电粒子），Compton 被证明正确 |
| spouse | Greta Irvin Blanchard | 无向 | 1902 年结婚 |
| colleague | Marie Curie | 无向 | 国联国际智力合作委员会共事（1922-31） |
| colleague | Hendrik Lorentz | 无向 | 国联国际智力合作委员会共事（1922-31） |

#### 4.5.1 入库操作

- `cd MySQL && python3 seed_person.py data/Robert_Andrews_Millikan.yaml`
- 方向约定：导师/门生有向；配偶/同事/争议无向；缺失人物自动建 stub

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：明亮、务实、加州暖调
- **配色**：油滴琥珀棕（主色，批内专属 `#A65E2E`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeDrop` 油滴实验 — 琥珀 `#D08C2E`
  - `badgePhoto` 光电效应 — 亮青 `#1F8A9D`
  - `badgeCosmic` 宇宙线 — 深空紫 `#5B4B8A`
  - `badgeCaltech` Caltech 缔造 — 加州橙 `#C75B12`
- **背景母题**：悬浮微粒与电场线——稀疏圆点在平行的极板色带间悬停，呼应油滴实验"以小测大"的意象

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 基本电荷的测量者 / Robert A. Millikan 1868–1953 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 油滴实验 / 光电效应 / 宇宙线 / Caltech 缔造
04  牧师之子与希腊教授的"物理启蒙" (1868–1895) — Oberlin、自修物理、哥伦比亚博士
05  芝加哥岁月 (1896–1917) — 教科书改革、1909 油滴实验启动
06  油滴实验（核心贡献页）— 悬停油滴受力平衡（公式框放 qE=mg 与 e 的整数倍性概念式）、电荷量子化
07  光电效应：不情愿的验证者 (1914–1916) — 真空车间、"vacuo machine shop"、1916 引语与 1950 自传转向
08  宇宙线与 Compton 论战 (1930s) — coined "cosmic rays"、"birth cries"假说、被磁场偏转观测证伪
09  Caltech 缔造者 (1921–1945) — Norman Bridge 实验室、执委会主席、研究型大学转型
10  战时与公共事务 — NRC 副主席、国联智力合作委员会、1933 地震建筑规范、时间胶囊
11  门生与传承 — Harvey Fletcher、Carl David Anderson、袁家骝等
12  荣誉与认可 — Nobel 1923 · Edison 1922 · Hughes 1923 · Medal for Merit 1949
13  争议与再评价 — Fletcher 协议、数据取舍之争、优生学记录与 2020-21 校园更名（按正文客观呈现）
14  遗产：从 e 的测量到现代粒子物理的实验传统
15  结尾
```

### 第 7–8 步：编写 Beamer 源码与布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照标杆 `\profileslide`；头部宏复用 `Kenneth_G_Wilson_zh.tex` 骨架
- 每写完一页 `make` 并 `pdftoppm` 目检；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Millikan 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方原文 "for his work on the elementary charge of electricity and on the photoelectric effect"，禁改写 |
| e 值口径 | 油滴实验测得 1.592×10⁻¹⁹ C（偏低因空气黏度取值不准），现代值 1.60217653×10⁻¹⁹ C——勿写"测得现代精确值" |
| Fletcher 协议 | 正文口径：Fletcher 以另一论文的完整署名为条件让出油滴论文署名，保密至去世——禁写"窃取学生成果"，也禁写成无合作关系 |
| 数据取舍争议 | Allan Franklin（"cosmetic surgery"缩小统计误差）与 David Goodstein（辩护口径）两说并存，须两说并陈 |
| 光电效应立场 | 他验证了 Einstein 方程但至 1916 仍公开否定光子诠释，1950 自传才承认——勿写成"为支持光子说而做实验" |
| 可用原话 | "Einstein's photoelectric equation... cannot in my judgment be looked upon at present as resting upon any sort of a satisfactory theoretical foundation"（1916，正文载） |
| 宇宙线 | 一词由他首创（coined），但"光子说"输给 Compton 的"带电粒子说"——两项事实都要写，勿只留其一 |
| 优生学争议 | Human Betterment Foundation 创始 trustee、San Marino "Anglo-Saxon" 言论、1936 致 Duke 校长信——按正文客观记载，禁美化禁渲染；2020 Pomona 与 2021 Caltech 更名须注明时间点 |
| 战时指控 | 离心机枪设计指控由 Wood 调查建议撤职、McIntyre 复查洗清——两段都要写 |
| 师承区分 | 博士导师是 Ogden Rood（哥伦比亚）；Michelson 是 frontmatter 另载的博士导师之一/芝加哥前辈，勿颠倒主次 |
| 去世地 | San Marino, California（非 Pasadena）；葬 Glendale Forest Lawn |
| 宗教立场 | 基督教有神论者与有神进化论支持者（Terry Lectures 1926-27 → Evolution in Science and Religion），与优生学段落分开表述 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| oil drop experiment | 油滴实验 | 电荷量子化的实验证明 |
| elementary charge | 基本电荷 | e，勿译"元电荷"泛称 |
| photoelectric effect | 光电效应 | 验证对象是 Einstein 方程 |
| Planck constant | 普朗克常数 | 他用光电发射图测得其值 |
| cosmic rays | 宇宙线 | 术语由他首创 |
| charge quantization | 电荷量子化 | 整数倍性 |
| Executive Council | 执行委员会 | Caltech 早期治理机构 |
| Norman Bridge Laboratory | 诺曼·布里奇实验室 | Caltech 物理实验室 |
| eugenics | 优生学 | 争议段落，客观表述 |
| Medal for Merit | 功绩勋章 | 1949 美国文职最高奖之一 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **New Lands** — Alex-Productions（152k views，曲库最高受众）
- **风格**: 高受众 / 史诗 / 开阔
- **匹配理由**:
  - "开阔/新大陆" 匹配密立根的身份——从伊利诺伊牧师之家到缔造美国研究型大学（Caltech）的实验物理领军者
  - "史诗" 匹配油滴实验与光电验证的里程碑气质，也匹配 1949 Medal for Merit 的国家致敬
  - 批内唯一使用，不与其他四位重复
- **本地路径**: `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav` → 复制为 `presentations/20th_century/Robert_Andrews_Millikan/New Lands.wav`
- **时长**: 足覆盖 16 页 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Robert_Andrews_Millikan/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Robert_Andrews_Millikan.yaml` | 研究领域 + 社会关系入库文件 |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 qid → name_en 匹配） |

> **开始执行。每完成一步向主控汇报。**
