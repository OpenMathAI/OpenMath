# 物理学家立传提示词（James Franck）

> 本文件是 OpenPhysicist「物理学家立传提示词」的人物专属实例，以 James Franck（1925 诺贝尔物理学奖，电子-原子碰撞定律，与 Gustav Hertz 共享）为对象。
> 结构对齐标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节），凡标注 `【模板通用】` 可复用，`【人物专属】` 为弗兰克定制品。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：James Franck（詹姆斯·弗兰克）。
- **设计哲学**：物理学家立传必须有「身份信息页」与「研究领域」结构化表达；弗兰克篇是"实验物理学家 + 良知科学家"双线叙事——Franck–Hertz 实验与 Franck–Condon 原理的科学线，与 1933 年辞职抗议、1945 年 Franck Report 的良知线并重，两条线互为注脚。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：James Franck（1882-08-26 ~ 1964-05-21，享年 81 岁）
- **气质关键词**：**电子碰撞定律的发现者、量子跃迁的实验证人、科学良知的化身** —— 1925 诺贝尔物理学奖获奖理由（官方原文，禁改写；与 Gustav Hertz 共享）：
  > "for their discovery of the laws governing the impact of an electron upon an atom"（表彰他们发现了电子与原子碰撞所遵循的定律）
- **设计母题**：**4.9 电子伏的门槛（the 4.9 eV threshold）**。电子撞上汞原子，非整段能量不交——碰撞曲线上的等距台阶是量子化能级最直观的实验肖像；视觉上用碰撞曲线的台阶、电子轨迹与能级梯呈现"能量交换的阶梯"。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/James_Franck/page.md`（Wikipedia 全文 + frontmatter）
- **待下载**：`https://en.wikipedia.org/wiki/James_Franck` → `James_Franck/James_Franck.html`（本批人物暂无 html 与 images/，第 0/3 步需补下载）
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- 🔲 待下载 `https://en.wikipedia.org/wiki/James_Franck` 到 `James_Franck.html`
- 事实基准（已按本地 page.md 核对）：
  - 生卒：1882-08-26 生于汉堡（德意志帝国）~ 1964-05-21 卒于西德哥廷根（访问期间心脏病发），享年 81 岁；葬于芝加哥（与第一任妻子合葬）
  - 国籍与变迁：德国（汉堡/魏玛）→ 美国（1941-07-21 入籍）
  - 家庭：犹太家庭；父 Jacob Franck 为银行家、母 Rebecca Nachum Drucker 出身拉比世家；姐 Paula、弟 Robert
  - 教育：1891 入汉堡 Wilhelm-Gymnasium；1901 入海德堡大学（本欲学法律，因结识 Max Born 转物理）；后转柏林大学，师从 Planck 与 Warburg
  - 博士导师：Emil Warburg（infobox 与正文明载）；frontmatter 另列 Paul Drude（1906 年去世，写法须谨慎）
  - 学位与论文：1906 博士《Über die Beweglichkeit der Ladungsträger der Spitzenentladung》（尖端放电中载流子的迁移率，发表于 Annalen der Physik）；1911 柏林 Habilitation（以 34 篇论文路线）
  - 婚姻：1907-12-23 于哥德堡与瑞典钢琴家 Ingrid Josefson 结婚（女 Dagmar 1909、Elisabeth 1912）；Ingrid 1942-01-10 卒；1946-06-29 与 Hertha Sponer 再婚
  - 一战：1914 志愿入伍；1915 转入 Fritz Haber 的氯气部队（与 Otto Hahn 负责选址）；铁十字二级 1915-03-30、汉萨十字 1916-01-11、一级 1918-02-23；1917 毒气袭击重伤；俄国前线痢疾
  - 任职：柏林 extraordinaire 教授（1916-09-19 缺勤任命）→ 战后 Haber 的威廉皇帝物理化学所 → 1920-11-15 哥廷根实验物理正教授兼第二实验物理研究所所长（Born 的来哥廷根条件）→ 1933 辞职 → 1933-34 哥本哈根玻尔研究所（与 Hilde Levi 合作，转向光合作用）→ 1935 Johns Hopkins → 1938 芝加哥大学 → 1942-02 Met Lab 化学部主任 → 1947 芝加哥荣休教授仍研究光合作用
  - 关键荣誉（含年份）：Nobel 1925（与 Hertz 共享）；Max Planck Medal 1951（与 Hertz 共同获得）；Rumford Prize 1955（"For his fundamental studies on photosynthesis"）；NAS 1944；英国皇家学会外籍会员 1964
  - 知名学生（infobox Doctoral students 明载者择要）：Fritz Houtermans、Hans Kopfermann、Heinz Maier-Leibnitz、Arthur R. von Hippel（后为其女婿）、Wilhelm Hanle、Heinrich Kuhn
  - 核心贡献清单：①Franck–Hertz 实验（1914，电子与汞原子碰撞 4.9 eV 定值失能，紫外发射对应；玻尔模型的实验支柱）②Franck–Condon 原理（电子-振动跃迁强度由振动波函数重叠决定，光谱学与量子化学基石）③亚稳态（metastable）术语的提出（与 Sponer 等）④Franck Report（1945-06-11，建议不经警告不对日本城市使用原子弹）⑤流亡学者援助（协助 Lindemann 安置被解职的犹太科学家）⑥光合作用机理研究（晚年主线）
  - 关键时间线（18 节点）：1882 生于汉堡 / 1901 入海德堡（遇 Born）/ 1906 柏林博士 / 1911 Habilitation / 1914 Franck–Hertz 实验 / 1914-18 一战服役（Haber 毒气部队）/ 1918-12 与 Hertz 的最后一篇合作论文（承认玻尔理论）/ 1920-11-15 哥廷根正教授 / 1925 诺贝尔奖 / 1926-12-10 授奖 / 1933-04-17 辞职抗议 / 1933-11 离德赴哥本哈根 / 1935 Johns Hopkins / 1938 芝加哥 / 1941-07-21 入籍美国 / 1942 Met Lab 化学部主任 / 1945-06-11 Franck Report / 1946 与 Sponer 再婚 / 1951 Max Planck Medal（与 Hertz）/ 1955 Rumford Prize / 1964-05-21 卒于哥廷根 / 1967 芝加哥 James Franck Institute 命名

### 第 1 步：建立目录 【模板通用】

- 已存在 `physicist/presentations/20th_century/James_Franck/`，补建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=James_Franck_zh`、`VIDEO_NAME=James_Franck_zh`

### 第 3 步：收集图片 【人物专属】

- 🔲 待下载弗兰克肖像（Wikipedia infobox 1925 年照）到 `images/Franck.jpg`，curl 带 `-A "Mozilla/5.0"` 并 `file` 验证；Franck–Hertz 曲线图（`Franck-Hertz_en.svg`，基于 1914 原始论文）与 1954 年玻尔/弗兰克/爱因斯坦/拉比四人合影可作插图

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Franck 的研究领域（按 rank 排序，与 yaml 完全一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | experimental physics | 实验物理 | 精密碰撞实验传统 | 核心页 |
| 1 | atomic physics | 原子物理 | Franck–Hertz 实验，能级量子化的实验证据 | 碰撞页 |
| 2 | molecular spectroscopy | 分子光谱学 | Franck–Condon 原理 | 跃迁页 |
| 3 | photochemistry | 光化学 | 晶体光化学过程（与 Teller 合作） | 光化学页 |
| 4 | biophysics | 生物物理 | 晚年光合作用机理研究 | 光合页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Emil Warburg | 对方是导师 | 柏林大学博士导师，离子迁移率论文（1906） |
| advisor-student | Paul Drude | 对方是导师 | frontmatter 明载的博士导师之一 |
| co-honored | Gustav Ludwig Hertz | 无向 | 1925 诺贝尔物理学奖共同得主 |
| colleague | Gustav Ludwig Hertz | 无向 | Franck–Hertz 实验合作者，19 篇合作论文 |
| colleague | Max Born | 无向 | 海德堡结识的终生挚友，哥廷根理论物理所长 |
| colleague | Lise Meitner | 无向 | 柏林时期合作者，其学术生涯的提携者 |
| spouse | Hertha Sponer | 无向 | 1946 年再婚，长期合作者与助手 |
| colleague | Fritz Haber | 无向 | 一战毒气部队与战后威廉皇帝研究所同事 |
| colleague | Otto Hahn | 无向 | 毒气攻击选址同事 |
| colleague | Niels Bohr | 无向 | 哥本哈根研究所避难一年，诺奖奖章托其保管 |
| advisor-student | Fritz Houtermans | 对方是学生 | 哥廷根博士学生 |
| advisor-student | Hans Kopfermann | 对方是学生 | 哥廷根博士学生 |
| advisor-student | Heinz Maier-Leibnitz | 对方是学生 | 哥廷根博士学生 |
| advisor-student | Arthur R. von Hippel | 对方是学生 | 哥廷根博士学生，后为其女婿 |
| colleague | Edward Teller | 无向 | 芝加哥首篇合作论文（晶体光化学过程） |
| colleague | Eva von Bahr | 无向 | 柏林时期最常合作者之一 |

#### 4.5.1 入库操作

- `cd MySQL && python3 seed_person.py data/James_Franck.yaml`
- 方向约定：师生有向；配偶/同事/共同荣誉无向；缺失人物自动建 stub

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：温厚、坚韧、德国学院绿
- **配色**：格廷根绿（主色，批内专属 `#2E5E4E`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeColl` 碰撞实验 — 电子蓝 `#2B6CB0`
  - `badgeCond` Franck–Condon — 振动紫 `#7B5EA7`
  - `badgePhoto2` 光合作用 — 叶绿青 `#3B8A4E`
  - `badgeConsc` 科学良知 — 熔岩红 `#B03A2E`
- **背景母题**：碰撞曲线的等距台阶——一段上升的阶梯曲线横贯版面，电子沿"能级梯"逐级跃迁，呼应 4.9 eV 的量子化门槛

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 电子碰撞定律的发现者 / James Franck 1882–1964 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、师承、任职、荣誉、核心领域）
03  核心贡献概览 — Franck–Hertz 实验 / Franck–Condon 原理 / Franck Report / 光合作用
04  汉堡银行家之子 (1882–1906) — 法律转物理、Born 挚友、柏林师从 Planck 与 Warburg
05  柏林的合作者时代 (1907–1914) — 与 Hertz 19 篇、Meitner/von Bahr、34 篇论文的 Habilitation
06  Franck–Hertz 实验（核心贡献页）— 4.9 eV、碰撞曲线、紫外发射（公式框放 E=f·h 能频关系；I–V 曲线概念图式）
07  与玻尔理论的和解 (1918) — 最后一篇合作论文、诺奖演讲自承"竟未认出玻尔理论的意义"（原话可引）
08  一战：Haber 部队与铁十字 (1914–1918) — 毒气选址、负伤、三章
09  哥廷根黄金年代 (1920–1933) — Born 双璧、bonzen 合影、博士弟子群、亚稳态、Franck–Condon 原理
10  1933：辞职抗议 — 依该法辞职的第一位学者（正文原话口径）、Lindemann 援助网、奖章托付玻尔
11  流亡与美国 (1933–1942) — 哥本哈根一年、Johns Hopkins、芝加哥、入籍
12  Met Lab 与 Franck Report (1942–1945) — 化学部主任、报告核心主张、Interim Committee 决定相反
13  晚年：光合作用与传承 (1946–1964) — Sponer、荣休研究、门生（Houtermans/Kopfermann/von Hippel）
14  荣誉与认可 — Nobel 1925 · Max Planck 1951（与 Hertz）· Rumford 1955 · James Franck Institute
15  遗产：实验证实量子世界的人 + 敢说"不"的人
```

### 第 7–8 步：编写 Beamer 源码与布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照标杆 `\profileslide`；头部宏复用 `Kenneth_G_Wilson_zh.tex` 骨架
- 每写完一页 `make` 并 `pdftoppm` 目检；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Franck 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方原文 "for their discovery of the laws governing the impact of an electron upon an atom"（与 Hertz 共享），禁改写 |
| 1914 实验初衷 | 当时并非为验证玻尔模型（诺奖演讲自承 "completely incomprehensible that we had failed to recognise the fundamental significance of Bohr's theory"，正文载可引）；1918-12 最后一篇论文才与玻尔理论和解——勿写成"一开始就为验证玻尔模型" |
| Franck–Condon 原理 | Condon 是 Edward Uhler Condon；原理内容为电子跃迁中振动波函数重叠决定强度——勿作其他引申 |
| 毒气部队 | 与 Haber、Hahn 的战时关系按正文客观表述（选址职责、三章），禁渲染禁洗白 |
| 1933 辞职 | 正文口径是"依该法辞职的第一位学者"（first academic to resign in protest over the law）——禁扩大为"首位公开反抗纳粹的德国人" |
| Franck Report | 1945-06-11 完成，建议"不经警告不对日本城市使用原子弹"；Interim Committee 决定相反——两半都要写；委员会成员含 Seaborg、Szilárd |
| 奖章王水故事 | 执行溶解者是 Hevesy，奖章属 Franck 与 Laue，存放于玻尔研究所——勿写成玻尔本人溶解或 Franck 自行处理 |
| Drude 师承 | frontmatter 列 Drude 为博士导师之一，但 infobox 与正文只认 Warburg，且 Drude 1906 年去世——表述限定为"frontmatter 明载" |
| 卒葬地 | 卒于哥廷根（访问期间心梗）、葬于芝加哥——勿写"葬于哥廷根" |
| 双重身份 | von Hippel 既是博士学生又是女婿（娶 Dagmar），两个身份都明载 |
| 国籍口径 | 出生汉堡（德意志帝国）、1941 入籍美国——DB 国籍写 Germany + United States 两条 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Franck–Hertz experiment | 弗兰克–赫兹实验 | 能级量子化的实验证据 |
| electron volt | 电子伏 | 4.9 eV 是汞原子第一激发能 |
| Franck–Condon principle | 弗兰克–康登原理 | 电子-振动跃迁强度规则 |
| metastable state | 亚稳态 | 与 Sponer 等提出的术语 |
| habilitation | 教授资格 | 德国学术制度，34 篇论文路线 |
| professor ordinarius | 正教授 | 哥廷根职衔 |
| Franck Report | 弗兰克报告 | 1945，反对无警告使用核武 |
| Metallurgical Laboratory | 冶金实验室 | 曼哈顿计划芝加哥分部 |
| photosynthesis | 光合作用 | 晚年研究主线 |
| aqua regia | 王水 | 奖章保存故事，勿挪用到他人名下 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Lonesome** — AShamaluevMusic（inspiring-electronic 合辑首位，3:17）
- **风格**: 悲伤 / 电影感 / 情感
- **匹配理由**:
  - "孤独/情感" 匹配弗兰克的人生底色——1933 年独自辞职的良知抉择、1945 年报告被驳回的孤立、流亡岁月的离散
  - "电影感" 匹配其叙事张力——从汉堡到柏林到哥廷根到芝加哥，一位"直线前行"的实验物理学家的传记弧光（Meitner 评语：研究沿着一条几乎笔直的线，正文载）
  - 批内唯一使用，不与其他四位重复
- **本地路径**: `music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav` → 复制为 `presentations/20th_century/James_Franck/Lonesome.wav`
- **时长**: 3:17 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/James_Franck/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/James_Franck.yaml` | 研究领域 + 社会关系入库文件 |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 qid → name_en 匹配） |

> **开始执行。每完成一步向主控汇报。**
