# 物理学家立传提示词（模板标杆实例：Charles Glover Barkla）

> **本文件是 OpenPhysicist 的「物理学家立传提示词模板标杆」的人物专属实例**，目标人物为 Charles Glover Barkla（1917 诺贝尔物理学奖，特征 X 射线的发现者）。
> 凡标注 `【模板通用】` 的部分可原样复用到任何物理学家；标注 `【人物专属】` 的部分需按本文件内容替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：综合数学家侧标杆（Hilbert / Grothendieck 的提示词 + tex 结构）与物理学家侧首例（Eugene Wigner）的实战经验。
- **本实例**：Charles Glover Barkla（查尔斯·格洛弗·巴克拉）。
- **设计哲学**：物理学家立传与数学家立传的核心差异，在于**物理学家必须有「身份信息页」（Identity / Bio 速览页）**，且强调「研究领域」的结构化表达——这两点构成物理学家模板的骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Charles Glover Barkla（1877-06-07 ~ 1944-10-23，享年 67 岁）
- **气质关键词**：**特征 X 射线的发现者、X 射线极化的证明者、固执的实验主义者** —— 1917 诺贝尔物理学奖获奖理由（官方英文原文，禁止改写）：
  > "For his discovery of the characteristic Röntgen radiation of the elements."（因其发现各元素的特征伦琴辐射）
- **设计母题**：**特征谱线（characteristic radiation）**。每种元素受 X 射线激发后发出属于自己的特征辐射——如同每个元素的身份指纹。视觉语言可用「同一束入射线下，不同元素发出不同波长的离散谱线」表达其一生研究的核心。
- **本地 Wikipedia**：`physicist/presentations/20th_century/20th_century/Charles_Glover_Barkla/page.md`（已有全文）
  - `{Dir}.html` 与 `images/`：**待下载**（Wikipedia URL: `https://en.wikipedia.org/wiki/Charles_Glover_Barkla`）
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（16 页）
  - 数学家标杆：`mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- `{Dir}.html` **待下载**：`https://en.wikipedia.org/wiki/Charles_Glover_Barkla`（page.md 已有全文可先建立事实基准）
- 头像 **待下载**（Wikipedia infobox 照片，下载到 `images/`）
- 提取 infobox 与正文，事实基准如下（源自 page.md）：
  - 生卒日期（1877-06-07 生于英格兰威德尼斯 Widnes ~ 1944-10-23 逝于苏格兰爱丁堡自宅，享年 67 岁）
  - 国籍（英国）
  - 父母（父 John Martin Barkla，出身康沃尔郡 Wendron，Atlas Chemical Company 秘书；母 Sarah Glover）
  - 教育（Liverpool Institute 中学；利物浦大学学院——县议会奖学金 + Bibby 奖学金，初学数学后转物理，1898 物理一等荣誉毕业，1899 硕士；1899 获 1851 Research Fellowship 入剑桥三一学院，师从 J. J. Thomson 于卡文迪许实验室；后转剑桥国王学院——为加入其唱诗班，独唱极受欢迎）
  - 博士导师（infobox Academic advisors 两位：Oliver Lodge——利物浦时期；J. J. Thomson——剑桥时期；frontmatter doctoral_advisor 仅列 Lodge，两位均可写）
  - 博士后（无载）
  - 主要任职机构（1902 回利物浦任 Oliver Lodge Fellow；1909 伦敦大学 Wheatstone 物理学教授；1913 爱丁堡大学自然哲学教授，直至去世）
  - 关键荣誉（Nobel 物理学奖 1917；Hughes Medal 1917；FRS 1912；FRSE 1914）
  - 知名学生（Marion Ross，infobox Doctoral students 明载）
  - 家庭（1907 与 Mary Esther Cowell 结婚，育两子一女；卫理公会信徒）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（见下，16 个节点）：1877 生于 Widnes → Liverpool Institute → 1898 利物浦一等荣誉毕业 → 1899 硕士 + 入剑桥三一学院（1851 Research Fellowship）→ 师从 J. J. Thomson 研究电磁波沿不同导线的传播 → 转剑桥国王学院（唱诗班）→ 1902 回利物浦任 Oliver Lodge Fellow → 1903 开始研究气体中次级 X 射线 → 1904《Nature》发表 X 射线极化简报 → 1905《Phil. Trans. R. S.》发表详细论述 → 1907 与 Mary Esther Cowell 结婚 → 1909 伦敦大学 Wheatstone 教授 → 1912 FRS → 1913 爱丁堡大学自然哲学教授 → 1914 FRSE → 1917 诺贝尔物理学奖 + Hughes Medal → 1920-06-03 诺贝尔演讲《Characteristic Röntgen Radiation》→ 1922–1938 住爱丁堡 Hermitage of Braid → 1944-10-23 逝于爱丁堡自宅

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Charles_Glover_Barkla/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录 `Eugene_Wigner/Makefile`，设置 `MAIN=Charles_Glover_Barkla_zh`、`VIDEO_NAME=Charles_Glover_Barkla_zh`

### 第 3 步：收集图片 【人物专属】

- 头像 **待下载**：优先 Wikipedia infobox 照片（Commons `Special:FilePath/<文件名>?width=600`，404 则经 Wikipedia REST API 查 infobox 实际文件名）
- 可用插图（page.md 明载）：爱丁堡 Hermitage of Braid 宅邸照片、Hermitage of Braid 上的 Barkla 纪念铭牌

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> 把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

**Barkla 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | X-ray spectroscopy | X 射线谱学 | 特征 X 射线的发现与谱线规律，诺奖核心 | 核心贡献页 |
| 1 | atomic physics | 原子物理 | 元素特征辐射与原子结构关联 | 特征辐射页 |
| 2 | X-ray scattering | X 射线散射 | 散射定律与穿透物质的原则 | 散射页 |
| 3 | electromagnetic radiation | 电磁辐射 | 证明 X 射线可极化、属电磁波（1904/1905） | 极化页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Oliver Lodge | 师→生（导师） | 利物浦大学学院导师，Barkla 早期物理训练 |
| advisor-student | J. J. Thomson | 师→生（导师） | 剑桥三一学院卡文迪许实验室导师（1851 Research Fellowship） |
| advisor-student | Marion Ross | 生→师（学生） | 爱丁堡时期博士生（infobox Doctoral students） |
| spouse | Mary Esther Cowell | 无向 | 1907 年结婚，育两子一女 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：冷冽、离散、穿透
- **配色**：深青蓝（X 射线的冷光）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `badgeSpec` 特征谱线 — 青蓝 `#0E7490`（主色同源）
  - `badgeAtom` 原子物理 — 琥珀 `#E07B30`
  - `badgeScat` 散射 — 玫瑰 `#C4204F`
  - `badgeEM` 电磁辐射 — 靛蓝 `#4C5FD5`
- **背景母题**：离散竖谱线（稀疏短竖线组，四种颜色错落），呼应「每种元素发出自己的特征谱线」——特征辐射的身份指纹思想（与第 2 步设计母题一致）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍、出生地、师承、任职、主要荣誉、核心领域。事实取自 page.md，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 特征 X 射线的发现者 / Charles Glover Barkla 1877–1944 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含出生地 Widnes、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 特征辐射 / X 射线极化 / 散射定律 / J 现象
04  早年：威德尼斯与利物浦 (1877–1899) — 化学公司秘书之子、初学数学后转物理、1898 一等荣誉
05  剑桥岁月：Thomson 门下与国王学院唱诗班 (1899–1902) — 1851 Research Fellowship、电磁波沿导线、独唱
06  X 射线极化：证明电磁性 (1903–1905) — Wilberforce 三次辐射设想、自建装置、Nature 1904 / Phil. Trans. 1905
07  特征辐射：元素的身份指纹（核心贡献页，无具体发现年份则用概念图式）
08  散射、穿透与次级 X 射线 — 散射定律与激发原则
09  J 现象：一场未被接受的主张 — 与 Compton 散射的争议、学界未被说服、理论失败
10  教授生涯：伦敦与爱丁堡 — 1909 Wheatstone 教授、1913 自然哲学教授
11  荣誉与认可 — Nobel 1917 · Hughes Medal 1917 · FRS 1912 · FRSE 1914
12  家庭与信仰 — Mary Esther Cowell、两子一女、卫理公会的「探寻造物主」
13  纪念 — 月球 Barkla 环形山、Hermitage of Braid 铭牌、利物浦讲演厅
14  遗产：特征谱线与 X 射线谱学的开端
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）可整体复用标杆骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Barkla 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 特征 X 射线发现年份 | page.md 正文**未载具体发现年份**（infobox 仅 "Known for"），幻灯片禁写 1906/1907 等编造年份，用概念图式呈现 |
| 诺奖年份口径 | page.md 载 **1917 年奖**（含 Hughes Medal 同年），勿写成 1918；诺贝尔演讲时间为 1920-06-03，勿与获奖年份混淆 |
| 极化证明归属 | 三次辐射方案由 Lionel Wilberforce 提出、因太弱无法测量，Barkla 改建设计后自行证明——勿写成 Barkla 独创想法，也勿把证明归 Wilberforce |
| J 现象 | 是**未被学界接受的假说**（学界不认为它不同于 Compton 散射等已知机制），必须如实呈现为失败理论，勿写成成就 |
| 师承两位 | infobox Academic advisors 列 Oliver Lodge 与 J. J. Thomson 两位；frontmatter doctoral_advisor 仅列 Lodge——两位均可写，方向都是「导师」 |
| 转学原因 | 转入剑桥国王学院是**为加入唱诗班**（音乐原因），其独唱极受欢迎；勿写成学术调动 |
| 卒地卒龄 | 1944-10-23 逝于**爱丁堡自宅**，享年 67；勿与出生地 Widnes 混淆 |
| 宗教引语 | 卫理公会信徒，唯一可引英文原话："part of the quest for God, the Creator."；其余中文转述禁加引号 |
| 职业字段 | occupations 除 physicist 外另有 university teacher（frontmatter 明载）；fields 勿写入 nuclear physics——frontmatter 虽有，正文无实载支撑 |
| 无载禁写 | Barkla 与 Bragg 之父子的学术争论、家庭子嗣后续、Marion Ross 的生平细节，page.md 均无载，禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| characteristic X-rays | 特征 X 射线 | 官方诺奖理由作 "characteristic Röntgen radiation"，两者勿混译 |
| Röntgen radiation | 伦琴辐射 | 即 X 射线，诺奖理由原文用词 |
| secondary X-rays | 次级 X 射线 | 受激辐射，非散射的同义词 |
| X-ray polarization | X 射线极化 | 证明电磁性的关键证据 |
| J-phenomenon | J 现象 | Barkla 的失败假说，学界未接受 |
| X-ray fluorescence | X 射线荧光 | J 现象设想的类比机制 |
| Compton scattering | 康普顿散射 | 与 J 现象争议相关，勿写成 Barkla 的研究 |
| 1851 Research Fellowship | 1851 研究奖学金 | 入剑桥的资助来源 |
| Wheatstone Professor | 惠斯通教授 | 伦敦大学教席名 |
| Natural Philosophy | 自然哲学 | 爱丁堡教席的历史名称，勿意译为「自然物理」 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **The Invisible Light** — Infraction
- **风格**: 纪录片 / 电影 / 稳重
- **匹配理由**:
  - 曲名「不可见之光」与 X 射线研究完美同构——Barkla 一生研究肉眼不可见、却能揭示元素身份的辐射
  - 「纪录片」匹配传记叙事——威德尼斯 → 利物浦 → 剑桥唱诗班 → 特征辐射 → 爱丁堡，是实验者的一生纪录
  - 「稳重」匹配其固执、克制的实验主义气质
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav` → `presentations/20th_century/Charles_Glover_Barkla/The Invisible Light.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Charles_Glover_Barkla/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 标杆 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex` | 物理学家首例成品参考 |
| `mathematician/presentations/20th_century/Alexander_Grothendieck-F/Alexander_Grothendieck_zh.tex` | 数学家标杆参考 |
| `MySQL/seed_person.py` | 人物主记录 + fields/relations 入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
