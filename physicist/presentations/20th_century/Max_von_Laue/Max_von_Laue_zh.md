# 物理学家立传提示词（Max von Laue）

> 本文件是 OpenPhysicist「人物专属立传提示词」，以 Kenneth G. Wilson 标杆结构为骨架，为 Max von Laue（1914 诺贝尔物理学奖，X 射线晶体衍射）定制。
> 凡标注 `【模板通用】` 的部分原样复用；标注 `【人物专属】` 的部分已按本人物替换。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Max Theodor Felix von Laue（马克斯·冯·劳厄）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；本篇叙事有两条主线——**晶体衍射的发现**与**纳粹时期的科学良知**，是"物理学家风骨"篇的样板。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Max Theodor Felix von Laue（1879-10-09 生于 Pfaffendorf（今属科布伦茨）~ 1960-04-24 逝于西柏林，享年 80 岁）
- **气质关键词**：**衍射的发现者、相对论的信使、不动摇的反对者** —— 1914 诺贝尔物理学奖获奖理由：
  > "for his discovery of the diffraction of X-rays by crystals"（因其发现 X 射线在晶体中的衍射）
- **设计母题**：**晶格中的波（waves through the lattice）**。以劳厄斑（衍射斑点阵）、晶格点阵与波纹的视觉语言贯穿全篇。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Max_von_Laue/page.md`（Wikipedia 全文，事实基准已核对）
- **参考模板**：
  - 提示词标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 物理学家成品参照：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已随提示词同步入库 greatminds 库（MySQL），无需重复整理。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 本地 Wikipedia 已就位：`20th_century/20th_century/Max_von_Laue/` 下已有 `page.html` / `page.md` / `metadata.json` / `images.txt`（无需再下载）
- ⬜ **待下载头像**：images.txt 无正脸肖像（infobox「1929 年像」未入库）→ 用 Wikipedia REST API `page/summary` 查 infobox 原图名下载（404 则装饰圆占位）
- 事实基准（已按本地 page.md 核对）：
  - 生卒：1879-10-09 生于 Pfaffendorf ~ 1960-04-24 逝于西柏林，享年 80 岁（frontmatter 死亡字段有 04-23 噪声，以正文/infobox 04-24 为准）
  - 国籍：德国
  - 父母：父 Julius Laue（军政系统文官，1913 年受封世袭贵族，子遂为 Max **von** Laue），母 Minna Zerrenner
  - 教育：1898 Abitur + 一年兵役；Strassburg → Göttingen（受 Voigt、Max Abraham 影响）→ 慕尼黑一学期 → 柏林腓特烈·威廉大学
  - 博士导师：Max Planck，1903 博士《Über die Interferenzerscheinungen an planparallelen Platten》（平行平板上的干涉现象）
  - 博士后/教授资格：1906 年在慕尼黑大学 Arnold Sommerfeld 指导下完成 habilitation
  - 任职：1906 柏林 Privatdozent（结识 Einstein）；1909 慕尼黑 Privatdozent；1912 苏黎世教授；1914 法兰克福正教授；1916 维尔茨堡军事真空管研发；1919–1943 柏林大学物理学正教授；1951–1959 马普物理化学与电化学研究所所长（1953 更名 Fritz-Haber-Institut）
  - 1912 年发现：与 Walter Friedrich、Paul Knipping 用硫酸锌（闪锌矿）晶体实现 X 射线衍射；灵感来自与 Ewald 在英国花园散步的讨论；Sommerfeld 1912-06 向哥廷根物理学会报告
  - 相对论专著两卷（1911 / 1921）；超导：经 PTR 顾问结识 Meissner，1932 阈值场随形状变化，共 12 篇论文 + 1 部专著，1935 与 Fritz/Heinz London 兄弟合著
  - KWIP：1917 托管人，1922 副主任，Einstein 不归后任代理主任（至 1946/48，除 1935–1939 Debye 任正主任）
  - 反纳粹：1933 维尔茨堡物理大会开幕演说（类比伽利略案）、反对 Deutsche Physik、阻止 Stark 入普鲁士科学院（1933-12 被 Stark 解除 PTR 顾问职）、1934 Haber 悼文、1935 与 Planck/Hahn 组织 Haber 纪念会、与挚友 Hahn 秘密助人出逃
  - 诺贝尔奖章：二战中由 de Hevesy 溶于王水藏于玻尔研究所，战后复原重铸
  - 战后：1945 Farm Hall 拘留；1946 重返哥廷根；重建德国科学（德国物理学会、PTR 重组、Verband Deutscher Physikalischer Gesellschaften）；1946 唯一受邀参加英国晶体学国际会议的德国人
  - 关键荣誉：Matteucci 1914、Nobel 1914、Max Planck Medal 1932、Pour le Mérite 1952；皇家学会外籍 1949、美国 NAS 1958 等
  - 知名学生（infobox）：博士生 Friedrich Beck、Karl-Otto Kiepenheuer、Nikhil Ranjan Sen、Leó Szilard；其他知名学生 Johannes Geiss、Maurice Goldhaber、Karl Herzfeld、Fritz London、Werner Reichardt、Eugene Wigner
  - 家庭：1910 娶 Magdalene Degen，两子；子 Theodor（1916–2000，普林斯顿博士，美国历史学教授）
  - 遗赠：1960-04-08 车祸（摩托车手亡），16 天后不治；墓于哥廷根 Stadtfriedhof
  - 休闲：登山、摩托、帆船、滑雪

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下使用 `Max_von_Laue/` 并建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Max_von_Laue_zh`、`VIDEO_NAME=Max_von_Laue_zh`

### 第 3 步：收集图片 【人物专属】

- ⬜ 肖像见第 0 步（REST API 回退）；插图取自 images.txt：`Interferenz-Erscheinungen_bei_Röntgenstrahlen_Tafel_II_Fig._5.jpg`（1912 闪锌矿衍射图版）、`Grave_of_Max_von_Laue_at_Stadtfriedhof_Göttingen_2017_01.jpg`（哥廷根墓照）

### 第 4 步：研究领域 【模板通用，人物专属内容】

**Laue 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | x-ray diffraction | X 射线衍射 | 1912 发现，1914 诺奖核心 | 核心页 |
| 1 | crystallography | 晶体学 | 劳厄方程、空间点阵光学 | 核心页 |
| 2 | theory of relativity | 相对论 | 两卷专著、Einstein 挚友与推广者 | 相对论页 |
| 3 | superconductivity | 超导电性 | 12 篇论文 + 专著，与 London 兄弟合著 | 超导页 |
| 4 | optics | 光学 | 博士论文干涉现象、辐射场熵 | 早年页 |

### 第 4.5 步：社会关系 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Max Planck | 师→生（博士导师） | 柏林大学博士导师，1903 平行平板干涉论文 |
| advisor-student | Arnold Sommerfeld | 师→生 | 1906 慕尼黑大学 habilitation 导师 |
| colleague | Albert Einstein | 无向 | 1906 年柏林结识的终生挚友，其友谊促进了相对论的接受与发展 |
| colleague | Otto Hahn | 无向 | 挚友，纳粹时期共同秘密帮助受迫害同事出逃，战后共建德国科学 |
| colleague | Walther Meissner | 无向 | 帝国物理技术研究所同事，超导研究同行（迈斯纳效应发现者），1960 年为其作传 |
| colleague | Walter Friedrich | 无向 | 1912 年 X 射线晶体衍射实验合作者 |
| colleague | Paul Knipping | 无向 | 1912 年 X 射线晶体衍射实验合作者 |
| advisor-student | Leó Szilard | 生 | 博士生（infobox 明载） |
| advisor-student | Fritz London | 生 | 学生，1935 与其弟 Heinz London 同劳厄合著超导论文 |
| advisor-student | Eugene Wigner | 生 | 知名学生（infobox 明载） |
| controversy | Johannes Stark | 无向 | 1919 诺奖得主、Deutsche Physik 头目；劳厄公开反对并阻止其入普鲁士科学院，1933 被其解除 PTR 顾问职务 |
| spouse | Magdalene Degen | 无向 | 1910 年结婚，育两子 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：晶格、冷光、坚毅
- **配色**：衍射紫罗兰（主色 `#4A2E6F`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` X 射线衍射 — 紫罗兰 `#7E57C2`
  - `badgeB` 晶体学 — 石青 `#2E7D9A`
  - `badgeC` 相对论 — 深蓝 `#1E4E79`
  - `badgeD` 科学良知 — 铁灰红 `#8E3B46`
- **背景母题**：暗底上同心环状的劳厄斑阵，呼应"晶格中的波"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框）。
2. 封面明示国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项`。
3. 必须有身份信息页（左头像 + 右信息网格）。
4. 结尾页品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，15 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 晶格中的波 / Max von Laue 1879–1960 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — X 射线衍射 / 劳厄方程 / 相对论 / 超导
04  求学与师承 (1879–1906) — Voigt/Abraham、Planck 门下、Sommerfeld habilitation
05  柏林与慕尼黑：结识 Einstein (1906–1911) — 辐射场熵、相对论专著第一卷
06  1912：劳厄斑（核心贡献页，概念图式：晶格衍射几何与劳厄方程示意）
07  Friedrich 与 Knipping：一次共同实验 — 合作者与报告经过
08  1914 诺奖与战时 (1914–1918) — 法兰克福、维尔茨堡真空管
09  柏林讲坛 (1919–1943) — 物理讨论班前排、KWIP 副主任/代理主任
10  超导十二年 — Meissner、London 兄弟、专著
11  不动摇者：反纳粹岁月 — Würzburg 演讲、Haber 悼文、被解 PTR 职
12  王水中的金牌 — Hevesy 与玻尔研究所、战后重铸
13  重建德国科学 — Farm Hall 之后、Fritz-Haber-Institut
14  遗产 + 结尾 — 劳厄方程、X 射线晶体学百年、月面环形山
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照标杆 `\profileslide`。
- 头部宏整体复用 `Kenneth_G_Wilson_zh.tex` 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Laue 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 贵族化时间 | 1913 年父受封世袭贵族后才称 "von Laue"，此前名 Max Laue，勿把 von 提前到早年叙事 |
| 卒日 | 1960-04-24（frontmatter 有 04-23 噪声，以正文为准）；1960-04-08 车祸、16 天后去世 |
| 实验归属 | 衍射实验由 Laue 提出构想、Walter Friedrich 与 Paul Knipping 执行，三人共同完成，勿写成劳厄独自完成或写成"学生实验" |
| 灵感来源 | Ewald 在英国花园散步时谈及博士论文晶体模型，是诱因之一，可写但勿夸大为"Ewald 共同发现" |
| 导师分层 | 博士导师 Planck；habilitation 导师 Sommerfeld，两者勿混 |
| 金牌故事 | 被溶于王水的是 **Laue 与 James Franck 两枚**奖章（Hevesy 操作，玻尔研究所），勿写成只有劳厄一枚或写成 Einstein 的 |
| 反纳粹与黑皮书 | page.md 未载劳厄列入纳粹黑皮书名单（那是 W.H. Bragg 页的内容），勿混入 |
| 名言边界 | "science has no race or religion" 为 page.md 转述其观点的引文，可用；其余台词勿杜撰 |
| 诺奖年份 | 1914（同年亦获 Matteucci 奖章），1932 获 Max Planck Medal，勿混 |
| 学生口径 | Szilard 是博士生；Wigner 是"其他知名学生"（非博士），表中 note 勿混写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| x-ray diffraction | X 射线衍射 | 1912 发现 |
| Laue equations | 劳厄方程 | 三向量点阵衍射条件 |
| Laue pattern / spots | 劳厄斑 | 衍射图样 |
| crystal lattice | 晶格/空间点阵 | 衍射的几何载体 |
| interference | 干涉 | 博士论文主题 |
| theory of relativity | 相对论 | 两卷专著 |
| stress–energy tensor | 应力–能量张量 | 其相对论贡献之一 |
| superconductivity | 超导电性 | 晚年主攻 |
| habilitation | 教授资格论文 | 1906 慕尼黑 |
| aqua regia | 王水 | 金牌藏匿 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **PAST** — Alex-Productions（历史感 / 深沉，`music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`）
- **匹配理由**: "历史感/深沉"匹配劳厄的一生跨度（从普朗克门生到战后重建德国科学）与纳粹岁月的沉重叙事。
- **批内查重**: batch 2 内无人复用此曲。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Max_von_Laue/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Max_von_Laue.yaml` | 已入库的领域/关系数据 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
