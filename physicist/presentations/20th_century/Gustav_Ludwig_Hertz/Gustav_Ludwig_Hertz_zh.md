# 物理学家立传提示词（Gustav Ludwig Hertz）

> 本文件是 OpenPhysicist「物理学家立传提示词」的人物专属实例，以 Gustav Ludwig Hertz（1925 诺贝尔物理学奖，电子-原子碰撞定律，与 James Franck 共享）为对象。
> 结构对齐标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节），凡标注 `【模板通用】` 可复用，`【人物专属】` 为赫兹定制品。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Gustav Ludwig Hertz（古斯塔夫·路德维希·赫兹）。
- **设计哲学**：物理学家立传必须有「身份信息页」与「研究领域」结构化表达；赫兹篇是"实验物理学家 + 时代裹挟者"三幕叙事——与 Franck 的量子化实验、纳粹时期的困境与工业研究、战后赴苏参与核计划的复杂岁月，三层都要如实呈现、不作道德简化。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Gustav Ludwig Hertz（1887-07-22 ~ 1975-10-30，享年 88 岁）
- **气质关键词**：**碰撞实验的共同发现者、同位素分离的工程先驱、被时代摆布的诺奖得主** —— 1925 诺贝尔物理学奖获奖理由（官方原文，禁改写；与 James Franck 共享）：
  > "for their discovery of the laws governing the impact of an electron upon an atom"（表彰他们发现了电子与原子碰撞所遵循的定律）
- **设计母题**：**气体放电的辉光（glow discharge）**。真空管中电子束穿过汞蒸气，碰撞后的辉光沿管身分段亮起——碰撞曲线的台阶与辉光的明暗交替，是"能量量子化"最感性的视觉；辅以气体扩散级联的管道意象呼应同位素分离。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Gustav_Ludwig_Hertz/page.md`（Wikipedia 全文 + frontmatter）
- **待下载**：`https://en.wikipedia.org/wiki/Gustav_Ludwig_Hertz` → `Gustav_Ludwig_Hertz/Gustav_Ludwig_Hertz.html`（本批人物暂无 html 与 images/，第 0/3 步需补下载）
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- 🔲 待下载 `https://en.wikipedia.org/wiki/Gustav_Ludwig_Hertz` 到 `Gustav_Ludwig_Hertz.html`
- 事实基准（已按本地 page.md 核对）：
  - 生卒：1887-07-22 生于汉堡（德意志帝国）~ 1975-10-30 卒于东柏林（东德），享年 88 岁；葬汉堡 Ohlsdorf 墓园
  - 家庭与亲属：父 Gustav Theodor Hertz 为律师、母 Auguste Arning；祖父 Gustav Ferdinand Hertz（幼时为犹太人，1834 年全家皈依路德宗）；叔父为物理学家 Heinrich Hertz（电磁波）；表亲 Mathilde Hertz 为生物学家
  - 教育：Gelehrtenschule des Johanneums；哥廷根大学 1906-07、慕尼黑大学 1907-08、柏林腓特烈·威廉大学 1908-11；1911 博士（导师 Heinrich Rubens），论文《Über das ultrarote Adsorptionsspektrum der Kohlensäure...》（CO2 红外吸收谱对压力与分压的依赖）
  - 博士导师：Heinrich Rubens（infobox 与正文明载）；frontmatter 另列 Max Planck（写法须谨慎）
  - 婚姻：1919 与 Ellen Dihlmann 结婚（卒于 1941），两子 Carl Hellmuth 与 Johannes（皆为物理学家）；1943 与 Charlotte Jollasse 再婚
  - 一战：1914 起服役；1915 加入 Haber 的氯气部队，同年重伤；1917 回柏林任 Privatdozent
  - 任职：1913 柏林大学物理研究所研究助理 → 1920 飞利浦（Eindhoven）灯厂研究物理学家 → 1925 哈勒大学物理研究所所长 → 1928 柏林工业大学（THB）物理研究所所长（期间发展气体扩散同位素分离技术）→ 1934 年底因被划为"二等部分犹太人"被迫辞 THB 职务 → 1935-45 从事气体放电/电子原子物理/超声/回旋加速器研发（1939 起属 AGC 工作组）→ 1944-04 西门子研究实验室 II 主任 → 1945 赴苏
  - 苏联时期：与 Manfred von Ardenne、Peter Adolf Thiessen、Max Volmer 立约（"pact to defect"）；任 Institute G 负责人（Agudseri，苏呼米近郊），主导惰性气流扩散法同位素分离；1949 赴 Sverdlovsk-44 咨询铀浓缩；1950 迁莫斯科
  - 晚年：1954-61 任莱比锡大学（时名卡尔·马克思大学）物理研究所所长；1955-67 任东德物理学会主席
  - 关键荣誉（含年份）：Nobel 1925（与 Franck 共享）；Max Planck Medal 1951（与 Franck 共同获得）；Stalin Prize 二等 1951（与 Barwich 共同）；东德国家奖、爱国功勋勋章金质等（frontmatter 载）
  - 知名学生（infobox 明载）：Heinz Barwich（兼西门子副手）、Erwin Müller、Heinz Pose、Wilhelm Walcher；Other notable students：Werner Hartmann、Fritz Houtermans
  - 核心贡献清单：①Franck–Hertz 实验（1914，电子-汞原子碰撞 4.9 eV 定值失能）②与 Franck 合著 19 篇论文（至 1918-12）③气体扩散同位素分离技术（THB 时期发明，苏联时期工程化）④回旋加速器研发（Heidelberg/Leipzig）⑤主编《Lehrbuch der Kernphysik I-III》（1961-66）
  - 关键时间线（16 节点）：1887 生于汉堡 / 1906-11 哥廷根·慕尼黑·柏林求学 / 1911 柏林博士（Rubens）/ 1913 柏林物理所研究助理 / 1914 与 Franck 完成 Franck–Hertz 实验 / 1915 Haber 毒气部队并重伤 / 1917 柏林 Privatdozent / 1920 飞利浦 / 1925 哈勒所长 / 1928 THB 所长、扩散分离技术 / 1934 底被迫辞职 / 1944-04 西门子实验室 II 主任 / 1945 四人协议赴苏、Institute G / 1951 Stalin Prize（与 Barwich）与 Max Planck Medal（与 Franck）/ 1954-61 莱比锡 / 1955-67 东德物理学会主席 / 1975-10-30 卒于东柏林

### 第 1 步：建立目录 【模板通用】

- 已存在 `physicist/presentations/20th_century/Gustav_Ludwig_Hertz/`，补建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Gustav_Ludwig_Hertz_zh`、`VIDEO_NAME=Gustav_Ludwig_Hertz_zh`

### 第 3 步：收集图片 【人物专属】

- 🔲 待下载赫兹肖像（Wikipedia infobox 1925 年照）到 `images/Hertz.jpg`，curl 带 `-A "Mozilla/5.0"` 并 `file` 验证；Franck–Hertz 曲线图（`Franck-Hertz_en.svg`）可作共同实验页插图

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Hertz 的研究领域（按 rank 排序，与 yaml 完全一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | experimental physics | 实验物理 | 碰撞实验与工业实验室传统 | 核心页 |
| 1 | atomic physics | 原子物理 | Franck–Hertz 实验 | 碰撞页 |
| 2 | isotope separation | 同位素分离 | 气体扩散法，苏联核计划的工程核心 | 分离页 |
| 3 | gas discharge | 气体放电 | 1930s 以来持续的研究对象 | 放电页 |
| 4 | nuclear physics | 核物理 | 主编核物理教材、回旋加速器研发 | 核物理页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Heinrich Rubens | 对方是导师 | 柏林大学博士导师，红外吸收光谱论文（1911） |
| advisor-student | Max Planck | 对方是导师 | frontmatter 明载的博士导师之一 |
| co-honored | James Franck | 无向 | 1925 诺贝尔物理学奖共同得主 |
| colleague | James Franck | 无向 | Franck–Hertz 实验合作者，19 篇合作论文 |
| spouse | Ellen Dihlmann | 无向 | 1919 年结婚，卒于 1941 |
| parent-child | Carl Hellmuth Hertz | 无向 | 之子，物理学家 |
| advisor-student | Heinz Barwich | 对方是学生 | 博士学生，西门子副手 |
| co-honored | Heinz Barwich | 无向 | 1951 斯大林奖二等奖共同得主 |
| advisor-student | Erwin Müller | 对方是学生 | 博士学生（infobox 明载） |
| advisor-student | Heinz Pose | 对方是学生 | 博士学生（infobox 明载） |
| advisor-student | Wilhelm Walcher | 对方是学生 | 博士学生（infobox 明载） |
| advisor-student | Fritz Houtermans | 对方是学生 | other notable students 明载 |
| advisor-student | Werner Hartmann | 对方是学生 | other notable students 明载 |
| colleague | Manfred von Ardenne | 无向 | 1945 年协议同行赴苏，Institute A 负责人 |
| colleague | Peter Adolf Thiessen | 无向 | 1945 年协议同行赴苏 |
| colleague | Max Volmer | 无向 | 1945 年协议同行赴苏 |
| colleague | Fritz Haber | 无向 | 1915 毒气部队同事 |

#### 4.5.1 入库操作

- `cd MySQL && python3 seed_person.py data/Gustav_Ludwig_Hertz.yaml`
- 方向约定：师生有向；配偶/亲子/同事/共同荣誉无向；缺失人物自动建 stub

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：冷峻、曲折、工业金属感
- **配色**：电子灰蓝（主色，批内专属 `#37474F`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeColl` 碰撞实验 — 电子蓝 `#2B6CB0`
  - `badgeGlow` 气体放电 — 辉光青 `#18A999`
  - `badgeIso` 同位素分离 — 扩散钢灰 `#607D8B`
  - `badgeExile` 赴苏岁月 — 铁锈红 `#A94438`
- **背景母题**：放电管的分段辉光与扩散级联管道——横贯版面的真空管轮廓上，辉光按碰撞台阶分段亮起

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 电子碰撞定律的共同发现者 / Gustav L. Hertz 1887–1975 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、师承、任职、荣誉、核心领域）
03  核心贡献概览 — Franck–Hertz 实验 / 同位素分离 / 气体放电 / 核物理教材
04  赫兹家族 (1887–1911) — 律师之子、电磁波叔父 Heinrich、Rubens 门下的红外光谱博士
05  与 Franck 的黄金搭档 (1913–1918) — 柏林物理所、19 篇合作论文
06  Franck–Hertz 实验（核心贡献页）— 4.9 eV、碰撞曲线、紫外发射（公式框放 E=f·h 能频关系；I–V 曲线概念图式，注明与 Franck 篇分工）
07  一战与转折 (1914–1920) — Haber 部队、重伤、Privatdozent、飞利浦工业研究
08  三所大学的所长 (1925–1934) — 哈勒、THB、气体扩散同位素分离的发明
09  纳粹时期 (1934–1945) — "二等部分犹太人"口径、AGC、超声与回旋加速器、西门子
10  四人协议与苏联岁月 (1945–1954) — Institute G、同位素分离工程化、Sverdlovsk-44 咨询、Stalin Prize
11  东德晚年 (1954–1975) — 莱比锡、物理学会主席、核物理教材
12  家族与学生 — Heinrich 叔父、子 Carl Hellmuth、Barwich/Müller/Pose/Walcher
13  荣誉与认可 — Nobel 1925 · Max Planck 1951（与 Franck）· Stalin 1951 · 东德勋章
14  遗产：碰撞定律写在教科书、扩散分离改变能源政治
15  结尾
```

### 第 7–8 步：编写 Beamer 源码与布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照标杆 `\profileslide`；头部宏复用 `Kenneth_G_Wilson_zh.tex` 骨架
- 每写完一页 `make` 并 `pdftoppm` 目检；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Hertz 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方原文 "for their discovery of the laws governing the impact of an electron upon an atom"（与 Franck 共享），禁改写 |
| 赫兹家族区分 | 叔父 Heinrich Hertz（电磁波，频率单位以其命名）≠ 父 Gustav Theodor（律师）；子 Carl Hellmuth Hertz（物理学家）；表亲 Mathilde Hertz（生物学家）——四组"赫兹"严禁混淆；频率单位"赫兹"不可写成 Gustav 的荣誉 |
| 与 Franck 的分工 | 实验是 1914 年合作完成（Verh. Dtsch. Phys. Ges. 16, 457-467），最后一篇合作 1918-12；本篇叙事忠于本人页面，与 Franck 篇各写各的视角 |
| Planck 师承 | frontmatter 列 Planck 为博士导师之一，但 infobox 与正文只认 Rubens——表述限定为"frontmatter 明载" |
| 苏联核计划 | Institute G 的任务是同位素扩散分离与铀浓缩咨询（1949 Sverdlovsk-44），按正文客观工程性表述，禁渲染为"苏联原子弹功臣"也禁回避 |
| 四人协议 | 目标三重（防掠夺/继续研究/免起诉），Thiessen 有纳粹党籍且联系共产党人——按正文如实写 |
| 纳粹时期口径 | "second degree part-Jew"（祖父幼时犹太、1834 全家皈依路德宗）是正文原口径；一战军官身份使其一度受保护——勿简化为"犹太血统被迫害" |
| 国籍口径 | 出生汉堡（德意志帝国）→ 苏联工作 → 定居东德；DB 国籍写 Germany + German Democratic Republic 两条 |
| 莱比锡口径 | 正文括注：卡尔·马克思大学即今莱比锡大学（Leipzig University） |
| 无载禁写 | page.md 未载其与玻尔研究所的交往、未载理论物理工作（他是实验物理学家）、未载晚年评价——一律不写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Franck–Hertz experiment | 弗兰克–赫兹实验 | 能级量子化的实验证据 |
| electron volt | 电子伏 | 4.9 eV 是汞原子第一激发能 |
| isotope separation | 同位素分离 | 气体扩散法 |
| gaseous diffusion | 气体扩散 | 铀浓缩的工程路线 |
| gas discharge | 气体放电 | 其长期研究对象 |
| ultraviolet emission | 紫外发射 | 汞原子 254 nm 对应 4.9 eV |
| metastable state | 亚稳态 | Franck–Hertz 系列工作的延伸概念 |
| Stalin Prize | 斯大林奖 | 1951 二等，与 Barwich 共同 |
| Institute G | G 研究所 | 苏呼米近郊 Agudseri |
| Privatdozent | 无俸讲师 | 德国学术制度 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **PAST** — Alex-Productions（86k views）
- **风格**: 高受众 / 历史感 / 深沉
- **匹配理由**:
  - "历史感/冷战时期" 直接匹配赫兹的后半生——从纳粹德国到苏联核计划再到东德，是被大时代反复裹挟的轨迹
  - "深沉" 匹配其叙事的复杂性——不做道德简化，三幕结构需要克制而厚重的音乐
  - 批内唯一使用，不与其他四位重复
- **本地路径**: `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → 复制为 `presentations/20th_century/Gustav_Ludwig_Hertz/PAST.wav`
- **时长**: 足覆盖 16 页 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Gustav_Ludwig_Hertz/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Gustav_Ludwig_Hertz.yaml` | 研究领域 + 社会关系入库文件 |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 qid → name_en 匹配） |

> **开始执行。每完成一步向主控汇报。**
