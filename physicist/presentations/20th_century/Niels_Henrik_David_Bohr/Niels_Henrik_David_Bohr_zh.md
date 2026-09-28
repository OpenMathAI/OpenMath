# 物理学家立传提示词（Niels Bohr）

> 本文件是 OpenPhysicist「物理学家立传提示词」的人物专属实例，以 Niels Henrik David Bohr（1922 诺贝尔物理学奖，原子结构理论）为对象。
> 结构对齐标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节），凡标注 `【模板通用】` 可复用，`【人物专属】` 为玻尔定制品。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Niels Henrik David Bohr（尼尔斯·玻尔）。
- **设计哲学**：物理学家立传必须有「身份信息页」与「研究领域」结构化表达；玻尔篇另需突出「哥本哈根精神」——研究所作为量子力学中心的枢纽感，以「对话/论战」为叙事骨架。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Niels Henrik David Bohr（1885-10-07 ~ 1962-11-18，享年 77 岁）
- **气质关键词**：**原子结构的立法者、互补性哲学家、哥本哈根精神的中心** —— 1922 诺贝尔物理学奖获奖理由（官方原文，禁改写）：
  > "for his services in the investigation of the structure of atoms and of the radiation emanating from them"（表彰他对原子结构以及由原子发出的辐射之研究所作的贡献）
- **设计母题**：**互补性（complementarity）**。玻尔 1947 年自设计的族徽即阴阳太极，铭文 *Contraria sunt complementa*（对立即互补）——波动与粒子、经典与量子、科学与哲学的对立统一，是比任何单一物理图像都更贴合玻尔的视觉语言。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Niels_Henrik_David_Bohr/page.md`（Wikipedia 全文 + frontmatter）
- **待下载**：`https://en.wikipedia.org/wiki/Niels_Henrik_David_Bohr` → `Niels_Henrik_David_Bohr/Niels_Henrik_David_Bohr.html`（本批人物暂无 html 与 images/，第 0/3 步需补下载）
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇到歧义先征求主控意见再继续。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- 🔲 待下载 `https://en.wikipedia.org/wiki/Niels_Henrik_David_Bohr` 到 `Niels_Henrik_David_Bohr.html`
- 事实基准（已按本地 page.md 核对）：
  - 生卒：1885-10-07 生于哥本哈根 ~ 1962-11-18 卒于哥本哈根卡尔斯伯（Carlsberg）寓所，享年 77 岁；葬 Assistens 墓园家族墓地
  - 国籍：丹麦
  - 父母：父 Christian Bohr 为哥本哈根大学生理学教授；母 Ellen Adler 为丹麦犹太银行家 David Baruch Adler 之女
  - 兄弟妹：姐 Jenny（教师）、弟 Harald Bohr（数学家、1908 伦敦奥运会丹麦国家队足球运动员）
  - 教育：Gammelholm 拉丁学校；1903 入哥本哈根大学，师从 Christian Christiansen 学物理，随 Thiele 学天文数学、Høffding 学哲学；1909 硕士（金属电子论）、1911 博士《Studier over metallernes elektrontheori》
  - 博士导师：Christian Christiansen（infobox 明载）；frontmatter 另列 J. J. Thomson（1911-09 起剑桥卡文迪什访学资助期交往，正文载"未能给 Thomson 留下深刻印象"）
  - 博士后：曼彻斯特 Victoria University，Rutherford 邀请
  - 任职：1914-16 曼彻斯特 reader；1916 哥本哈根大学为其特设理论物理教授席；1920-03 创办理论物理研究所（1921-03-03 开幕，今尼尔斯·玻尔研究所）任所长；1932 迁入 Carlsberg 荣誉邸；1939-03-17 当选丹麦皇家科学院院长
  - 战时：1943-09-29 逃亡瑞典 → 1943-10-06 抵英（Mosquito 轰炸机弹舱、缺氧昏迷）→ Tube Alloys → 曼哈顿计划顾问（化名 Nicholas Baker）
  - 关键荣誉（含年份）：Hughes Medal 1921；Nobel 1922；Matteucci 1923；Franklin 1926；Faraday Lectureship 1930；Max Planck Medal 1930；Copley 1938；Order of the Elephant 1947；Atoms for Peace Award 1957（首届）；Sonning 1961
  - 知名学生（infobox Notable students 明载者择要）：Hans Kramers、Werner Heisenberg、Wolfgang Pauli、Lev Landau、Victor Weisskopf、Aage Bohr、John Wheeler 亦曾合作
  - 核心贡献清单：①玻尔模型（1913 三部曲，量子化定态+能级跃迁）②对应原理 ③互补性原理（1927）④哥本哈根诠释 ⑤BKS 理论（1924，最终被 Bothe–Geiger 实验否定）⑥预言 72 号元素非稀土（铪 1923 由 Coster 与 Hevesy 证实）⑦复合核理论/液滴模型（1936）⑧判定 U-235 为慢中子裂变主因并与 Wheeler 合著裂变机制（1939）⑨战后倡导核能国际合作，参与创建 CERN 与 Nordita
  - 关键时间线（18 节点）：1885 生于哥本哈根 / 1903 入哥本哈根大学 / 1905 皇家科学院金奖（水柱表面张力实验） / 1909 硕士 / 1911 博士 / 1911-09 剑桥卡文迪什 / 1912 曼彻斯特 Rutherford 门下并与 Margrethe Nørlund 结婚 / 1913 三部曲发表（7/9/11 月） / 1916 哥本哈根教授席 / 1921-03-03 研究所开幕 / 1922 诺贝尔奖 / 1922-06 哥廷根 Bohr Festival 七讲 / 1924 BKS 理论 / 1927 互补性原理与 Solvay 会议 / 1936 复合核理论 / 1939-01-26 华盛顿会议传递裂变消息、9 月与 Wheeler 发表裂变机制 / 1943 逃亡并加入曼哈顿计划 / 1947 大象勋章与自设计族徽 / 1950 致联合国公开信 / 1957 首届 Atoms for Peace Award、Nordita 首任主席 / 1962-11-18 卒 / 1965 研究所更名 Niels Bohr Institute

### 第 1 步：建立目录 【模板通用】

- 已存在 `physicist/presentations/20th_century/Niels_Henrik_David_Bohr/`，补建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Niels_Henrik_David_Bohr_zh`、`VIDEO_NAME=Niels_Henrik_David_Bohr_zh`

### 第 3 步：收集图片 【人物专属】

- 🔲 待下载玻尔肖像（Wikipedia infobox 1922 年照；Commons `Niels_Bohr_-_LOC_-_ggbain_-_35303.jpg` 为青年照 c.1910 可备用）到 `images/Bohr.jpg`，curl 带 `-A "Mozilla/5.0"` 并 `file` 验证

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Bohr 的研究领域（按 rank 排序，与 yaml 完全一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | atomic physics | 原子物理 | 玻尔模型与原子结构，1922 诺奖核心 | 核心页 |
| 1 | quantum mechanics | 量子力学 | 哥本哈根诠释、互补性、对应原理 | 量子论战页 |
| 2 | nuclear physics | 核物理 | 复合核理论、液滴模型、U-235 判定 | 核物理页 |
| 3 | theoretical physics | 理论物理 | 哥本哈根大学特设理论物理教授席 | 身份页 |
| 4 | philosophy of science | 科学哲学 | 互补性的认识论、与爱因斯坦的论战 | 哲学页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Christian Christiansen | 对方是导师 | 哥本哈根大学博士导师，金属电子论论文（1911） |
| advisor-student | Joseph John Thomson | 对方是导师 | frontmatter 明载的博士导师之一；1911-12 剑桥卡文迪什访学 |
| colleague | Ernest Rutherford | 无向 | 曼彻斯特博士后接纳者，其原子核模型是玻尔模型的出发点 |
| spouse | Margrethe Nørlund | 无向 | 1912 年结婚，终生伴侣与讨论伙伴 |
| parent-child | Aage Bohr | 无向 | 之子，1975 诺贝尔物理学奖得主 |
| advisor-student | Aage Bohr | 对方是学生 | 知名学生（infobox 明载），战时任其个人助理 |
| advisor-student | Werner Heisenberg | 对方是学生 | 知名学生；1926-27 哥本哈根讲师与助理 |
| advisor-student | Wolfgang Pauli | 对方是学生 | 知名学生（infobox 明载），不相容原理提出者 |
| advisor-student | Hans Kramers | 对方是学生 | 研究所早期来者与合作者，1926 赴乌得勒支任教 |
| advisor-student | Lev Landau | 对方是学生 | 知名学生（infobox 明载），1962 诺贝尔物理学奖得主 |
| advisor-student | Victor Weisskopf | 对方是学生 | 知名学生，后任 CERN 总干事 |
| colleague | Albert Einstein | 无向 | 量子力学诠释的终生论战，友谊式争辩 |
| colleague | Max Born | 无向 | 哥廷根同行，矩阵力学发展中的对话者 |
| colleague | George de Hevesy | 无向 | 曼彻斯特同事与研究所同仁，与 Coster 发现铪证实其预言 |
| colleague | John Wheeler | 无向 | 1939 合著 The Mechanism of Nuclear Fission |
| colleague | James Franck | 无向 | 帮助流亡学者，代为保管其诺贝尔奖章 |

#### 4.5.1 入库操作

- `cd MySQL && python3 seed_person.py data/Niels_Henrik_David_Bohr.yaml`（库内已有 id=1104 `Niels Bohr` 记录，yaml `name_en` 沿用库内形式，seed 会按 name_en 定位并回写 qid=Q7085）
- 方向约定：导师（对方是导师）与门生（对方是学生）有向；配偶/亲子/同事无向
- 缺失人物自动建 stub（`has_biography=0`）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深邃、思辨、丹麦冷调
- **配色**：哥本哈根深蓝（主色，批内专属 `#1B3A5C`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeAtom` 原子模型 — 海湾蓝 `#2E86AB`
  - `badgeComp` 互补性 — 阴阳灰 `#5A6472`
  - `badgeNuc` 核物理 — 铀青 `#0E7C7B`
  - `badgeInst` 哥本哈根精神 — 丹麦克朗红 `#C0392B`
- **背景母题**：阴阳双弧与轨道圆环——以互补的双色弧段与同心电子轨道呼应「互补性」与玻尔族徽太极铭文

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 原子结构理论奠基人 / Niels Bohr 1885–1962 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 玻尔模型 / 互补性 / 复合核 / 哥本哈根精神
04  早年：哥本哈根 (1885–1911) — 教授之子、足球守门员、1905 金奖、金属电子论博士
05  剑桥与曼彻斯特 (1911–1913) — Thomson、Rutherford 邀请、三部曲
06  玻尔模型（核心贡献页）— 定态与跃迁、由模型推出 Balmer/Rydberg 公式（公式框放 1/λ=R_H(1/2²−1/n²) 或 hν=ε₂−ε₁）
07  研究所与哥本哈根精神 (1920–1933) — 1921-03-03 开幕、Kramers/Klein/Hevesy、Bohr Festival、铪的预言
08  量子论战 (1924–1939) — BKS 理论之败、电子自旋插曲、科莫演讲、Einstein 论战
09  原子核岁月 (1936–1939) — 复合核/液滴模型、裂变消息赴美、U-235 判定、与 Wheeler 合著
10  战争与流亡 (1940–1945) — 奖章王水故事、1941 Heisenberg 之会（两说并存）、逃亡、化名 Nicholas Baker
11  战后：开放的世界 (1945–1962) — 致联合国公开信、CERN/Nordita/Risø、大象勋章族徽
12  家族与传承 — Margrethe、六子、Aage 1975 诺奖、Harald（兄）数学家
13  荣誉与认可 — Nobel 1922 · Hughes 1921 · Copley 1938 · Atoms for Peace 1957 · bohrium 命名
14  遗产：互补性与哥本哈根诠释的世纪回响
15  结尾
```

### 第 7–8 步：编写 Beamer 源码与布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`；头部宏可整体复用 `Kenneth_G_Wilson_zh.tex` 骨架
- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Bohr 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方原文 "for his services in the investigation of the structure of atoms and of the radiation emanating from them"，禁改写、禁泛化为"量子力学奠基" |
| 研究所开幕日期 | 导语作 opened in 1920，正文作 1921-03-03 开幕 → 以正文 1921 年为准 |
| 足球传言 | 正文注释 9 明确"玻尔为丹麦国家队出场"是讹传——国家队是弟弟 Harald（1908 奥运）；玻尔是 Akademisk Boldklub 守门员 |
| 1941 Heisenberg 之会 | 双方说法不一且正文两版本并存，禁单边采信；Frayn《哥本哈根》戏剧被史家批评为"怪诞的过度简化"，引用须注明争议 |
| "no quantum world" | 系 Aage Petersen 身后转述的非公开言论，正文明确非玻尔公开所言，禁作原话引用 |
| 可用原话 | Einstein 评三部曲 "the highest form of musicality in the sphere of thought"（正文载）；BKS 失败后致 Darwin 信 "give our revolutionary efforts as honourable a funeral as possible" |
| Thomson 师承 | infobox 博士导师仅 Christiansen；frontmatter 另列 Thomson。正文载访学期"未能给 Thomson 留下深刻印象"——写法须限定为"剑桥访学期间的前辈导师（frontmatter 明载）" |
| 两枚奖章故事勿混 | Laue/Franck 奖章是 Hevesy 用王水溶解保存；玻尔本人的奖章 1940-03 拍卖捐芬兰救济基金——两条线不可混写 |
| Hevesy 与铪 | 铪由 Coster 与 Hevesy 发现，玻尔是预言者，勿写成玻尔亲手发现 |
| 两个 Harald | 兄 Harald Bohr（数学家/奥运球员）与四子 Harald（脑膜炎夭折）同名，严禁混淆 |
| 逃亡日期 | 1943-09-29 渡海赴瑞典、10-06 抵苏格兰——勿与 10-02 瑞典广播赦令日混淆 |
| 身后口径 | 1999 Physics World 评选"史上第四伟大物理学家"（正文载）引用须注明来源 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Bohr model | 玻尔模型 | 定态+量子跃迁，非"行星模型"泛称 |
| stationary state | 定态 | 旧量子论术语 |
| complementarity | 互补性 | 认识论原理，非"互补原理"误写 |
| correspondence principle | 对应原理 | 大量子数极限回归经典 |
| Copenhagen interpretation | 哥本哈根诠释 | 与互补性相关但非同义 |
| BKS theory | BKS 理论 | Bohr–Kramers–Slater，统计守恒被实验否定 |
| compound nucleus | 复合核 | 1936 核理论 |
| liquid drop model | 液滴模型 | 与 Wheeler 裂变机制相关 |
| trilogy | 三部曲 | 1913 三篇 Philosophical Magazine 论文 |
| old quantum theory | 旧量子论 | 1925 前的量子理论 |
| Bohr–Einstein debates | 玻尔–爱因斯坦论战 | 友谊式争辩 |
| hafnium / bohrium | 铪 / 𬭛 | 前者哥本哈根发现，后者以其命名 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Timeless** — Alex-Productions（132k views，曲库最高受众档）
- **风格**: 沉稳 / 纪录片 / 长期纲领
- **匹配理由**:
  - "长期纲领" 匹配玻尔的事业本质——从 1913 三部曲到哥本哈根诠释，是一条跨越半个世纪的思想纲领
  - "沉稳/纪录片" 匹配其思辨气质——哥本哈根研究所作为量子力学中心的枢纽叙事，重在人物群像与思想演进
  - 批内唯一使用，不与其他四位重复
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → 复制为 `presentations/20th_century/Niels_Henrik_David_Bohr/Timeless.wav`
- **时长**: 128 秒 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Niels_Henrik_David_Bohr/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Niels_Henrik_David_Bohr.yaml` | 研究领域 + 社会关系入库文件 |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 qid → name_en 匹配） |

> **开始执行。每完成一步向主控汇报。**
