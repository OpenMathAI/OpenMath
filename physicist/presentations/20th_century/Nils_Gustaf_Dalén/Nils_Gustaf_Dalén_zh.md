# 物理学家立传提示词（Nils Gustaf Dalén）

> 本文件是 OpenPhysicist「人物专属立传提示词」，以 Kenneth G. Wilson 标杆结构为骨架，为 Nils Gustaf Dalén（1912 诺贝尔物理学奖，灯塔自动调节器）定制。
> 凡标注 `【模板通用】` 的部分原样复用；标注 `【人物专属】` 的部分已按本人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Nils Gustaf Dalén（尼尔斯·古斯塔夫·达伦，通称 Gustaf Dalén）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；本篇人物是**发明家/实业家型**获奖者，叙事重心是"工程发明改变世界"，与理论物理学家篇形成互补。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Nils Gustaf Dalén（1869-11-30 生于瑞典 Stenstorp ~ 1937-12-09 逝于瑞典 Lidingö，享年 68 岁）
- **气质关键词**：**灯塔守护者、盲眼实业家、"不可能想法"的试验者** —— 1912 诺贝尔物理学奖获奖理由：
  > "for his invention of automatic regulators for use in conjunction with gas accumulators for illuminating lighthouses and buoys"（因其发明与气体蓄存器联合使用的自动调节器，用于灯塔与浮标照明）
- **设计母题**：**昼夜交替的光（the light that tends itself）**。太阳阀（sun valve）白天自动熄灭、入夜自动点亮——以明暗节奏、海岸线、灯塔光束的视觉语言贯穿全篇。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Nils_Gustaf_Dalén/page.md`（Wikipedia 全文，事实基准已核对）
- **参考模板**：
  - 提示词标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 物理学家成品参照：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已随提示词同步入库 greatminds 库（MySQL），无需重复整理。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 本地 Wikipedia 已就位：`20th_century/20th_century/Nils_Gustaf_Dalén/` 下已有 `page.html` / `page.md` / `metadata.json` / `images.txt`（无需再下载）
- ⬜ **待下载头像**：`images.txt` 已有 `Gustaf_Dalén_1895.png`（青年工程师照）与 `Gustaf_Dalén_1926.jpg`（事业顶峰照，**建议用此**），250px 改 500px
- 事实基准（已按本地 page.md 核对）：
  - 生卒：1869-11-30 生于 Stenstorp ~ 1937-12-09 逝于 Lidingö，享年 68 岁
  - 国籍：瑞典
  - 父母：Anders 与 Lovisa Dalén；本人经营家庭农场（扩至市场园艺、种子行、乳品）
  - 教育：自学者出身；1892 发明牛奶脂肪测定器，赴斯德哥尔摩求见 Gustaf de Laval，得其赏识并被鼓励接受技术教育；Chalmers University of Technology 1896 毕业
  - 博士导师/学位：page.md 无载（无博士学位，工程师路线）
  - 任职：1906 Gas Accumulator Company 总工程师；1909 AGA（Svenska Aktiebolaget Gasaccumulator）成立任总经理直至 1937 去世
  - 核心发明：Agamassan（吸收乙炔的安全基材）、Dalén light（灯塔照明系统）、sun valve（太阳阀，白天熄灭夜间点亮）、Dalen Flasher（闪光器，省气 90% 以上）、AGA cooker（1922 专利）
  - 关键荣誉：Nobel Physics 1912；瑞典皇家科学院院士；科学与工程科学院成员；一生 100+ 项专利
  - 家庭：1901 娶 Elma Persson，两女两子（Maja、Gunnar、Anders、Inga-Lisa）
  - 1912 年初乙炔爆炸失明，同年获诺奖，由弟弟（卡罗琳医学院眼科教授 Albin Dalén）代为出席
  - AGA 灯塔覆盖巴拿马运河全线；Blockhusudden 灯塔自 1912 运行至 1980 电气化时无需大修

  - 关键时间线（15–20 节点）：
    - 1869-11-30 生于 Stenstorp，农家子弟
    - 1892 发明牛奶脂肪测定器，赴斯德哥尔摩求见 Gustaf de Laval
    - de Laval 赏识，鼓励其接受正规技术教育
    - 1896 毕业于 Chalmers University of Technology
    - 1901 与 Elma Persson 结婚（育两女两子）
    - 1906 任 Gas Accumulator Company 总工程师
    - 1909 公司重组为 AGA，出任总经理
    - 1910 在 Lidingö 购地建厂（1912 建成迁入）
    - 1912 年初 乙炔爆炸实验事故失明
    - 1912 AGA 灯塔 Blockhusudden 投用（太阳阀连续运行至 1980 无需大修）
    - 1912-12 获诺贝尔物理学奖，弟弟 Albin Dalén 代为出席
    - 1922 AGA cooker 专利（Villa Ekbacken 自家厨房完成大部分测试）
    - 1930s AGA 成为瑞典最具创新力企业之一，产品线逐年扩张
    - 1937-12-09 逝于 Lidingö，享年 68 岁，掌舵 AGA 直至最后
    - 身后：一生 100+ 项专利；Stenstorp 建有 Dalén 博物馆

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下使用 `Nils_Gustaf_Dalén/` 并建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆目录 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Nils_Gustaf_Dalén_zh`、`VIDEO_NAME=Nils_Gustaf_Dalén_zh`

### 第 3 步：收集图片 【人物专属】

- ⬜ 肖像见第 0 步（images.txt 两张照片任选，建议 1926 照）；插图均取自 images.txt：`Stockholm_Sweden_Blockhusudden-lighthouse-01.jpg`（灯塔）、`AGA_1920.png`（厂区）、`Gustaf_Dalén_1937.jpg`（夫妇合影）

### 第 4 步：研究领域 【模板通用，人物专属内容】

**Dalén 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | applied physics | 应用物理 | 发明家路线的物理学实践 | 核心页 |
| 1 | acetylene technology | 乙炔技术 | Agamassan 安全储存基材 | 核心页 |
| 2 | automatic regulators | 自动调节器 | 太阳阀，1912 诺奖核心 | 核心页 |
| 3 | lighthouse engineering | 灯塔工程 | Dalén light、浮标、巴拿马运河 | 应用页 |
| 4 | physical chemistry | 物理化学 | 气体吸收与材料（frontmatter 明载） | 早年页 |

### 第 4.5 步：社会关系 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Gustaf de Laval | 无向 | 蒸汽涡轮发明家/企业家，赏识其乳脂测定器并鼓励他接受技术教育 |
| spouse | Elma Persson | 无向 | 1901 年结婚，育两女两子 |

> ⚠️ page.md 明载关系仅此 2 条：无学术师承、无学生、无共享奖项对象（弟弟 Albin 代领属非白名单类型）。禁止从诺奖颁奖词或 AGA 公司史反推关系。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深海、昼夜、守护
- **配色**：灯塔深海蓝绿（主色 `#0E5A6D`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` 太阳阀 — 琥珀 `#D98E04`
  - `badgeB` 乙炔之光 — 砖红 `#B03A48`
  - `badgeC` AGA 工业 — 靛蓝 `#4C5FD5`
  - `badgeD` 灯塔海岸 — 青绿 `#0E7C7B`
- **背景母题**：暗底上稀疏的灯塔光束扇形与浮标圆点，呼应"昼夜交替的光"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框）。
2. 封面明示国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项`。
3. 必须有身份信息页（左头像 + 右信息网格：生卒/本名/国籍/出生地/教育/任职/荣誉/核心领域）。
4. 结尾页品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，13 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 灯塔守护者 / Nils Gustaf Dalén 1869–1937 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — Agamassan / Dalén light / 太阳阀 / AGA cooker
04  早年：农场发明家 (1869–1896) — 乳脂测定器、de Laval 的知遇、Chalmers
05  AGA 岁月 (1906–1937) — 总工程师→总经理，Lidingö 建厂
06  Dalén light 与太阳阀（核心贡献页，无公式 → 概念图式：昼熄夜亮原理）
07  1912：爆炸与诺贝尔奖 — 失明、弟弟代领、颁奖词的致敬
08  盲眼掌舵 — 继续主持 AGA 至 1937、100+ 专利
09  AGA 炉灶与家居发明 (1922) — Villa Ekbacken 厨房里的测试
10  灯塔版图 — 巴拿马运河全线、Blockhusudden 68 年免维护
11  遗产：工程物理学的诺奖样本
12  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现参照标杆 `\profileslide`。
- 头部宏（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）整体复用 `Kenneth_G_Wilson_zh.tex` 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Dalén 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方措辞是 "automatic regulators ... gas accumulators ... lighthouses and buoys"（自动调节器），勿写成"发明了乙炔"或泛称"照明技术" |
| 失明与获奖同年 | 1912 年初爆炸失明、同年 12 月获诺奖，两件事同年不同月，勿倒置因果；他并未因失明停止工作 |
| 代领人 | 代为出席颁奖的是弟弟 Albin Dalén（卡罗琳医学院眼科教授），勿写"妻子代领"或"本人缺席即未领奖" |
| 身份口径 | 工程师/发明家/实业家，教育止于 Chalmers 1896，勿写"博士"或虚构大学教职 |
| 三个名词 | Agamassan（吸收基材）/ Dalén light（照明系统）/ Dalen Flasher（闪光省气装置）三者勿混 |
| 太阳阀实绩 | Blockhusudden 灯塔 1912 装设、1980 电气化时太阳阀仍无需大修，是"可靠性"的实证，勿写成"用到 1980 年才坏" |
| 享年 | 1937-12-09 卒，68 岁（1869-11-30 生） |
| 关系红线 | page.md 无学术师承/学生记载，勿编造导师（de Laval 是知遇鼓励者，非导师） |
| 失明后细节 | 「依靠记忆、听觉与 describer 协助工作」一类描述 page.md 无载，勿写；只写「失明后仍掌舵 AGA 直至 1937 去世」 |
| 品牌之外 | AGA 灯塔覆盖巴拿马运河全线是 page.md 明载，可写；勿再加"全世界灯塔过半用 AGA"一类无载数字 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| sun valve | 太阳阀 | 昼熄夜亮的自动阀，诺奖核心 |
| gas accumulator | 气体蓄存器 | AGA 公司名之源 |
| acetylene / ethyne | 乙炔 | IUPAC 名 ethyne，勿混淆 |
| Agamassan | 阿加马桑 | 吸收乙炔的安全基材，专有名词 |
| Dalén light | 达伦灯 | 灯塔照明系统总称 |
| automatic regulator | 自动调节器 | 获奖理由关键词 |
| buoy | 浮标 | 与灯塔并列的照明对象 |
| AGA cooker | AGA 炉灶 | 1922 专利的家居发明 |
| milk-fat tester | 乳脂测定器 | 1892 年出道发明 |
| flasher | 闪光器 | 省气 90% 以上 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Daylight** — Alex-Productions（明亮 / 轻快，`music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav`）
- **匹配理由**: 曲名即太阳阀「昼亮灯灭」的判据——失明者造出了给全世界引路的光，以轻快而非悲情处理失明后的坚韧（与存量底稿 `Nils_Gustaf_Dalen/Nils_Gustaf_Dalen_zh.md` 的选定一致；其声称的落地 wav 尚未复制，执行时需自行复制到人物目录）。
- **备选**（未采用）: The Invisible Light — Infraction（纪录片 / 稳重，"无形的光"契合灯塔母题）。
- **批内查重**: batch 2 内无人复用此曲。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Nils_Gustaf_Dalén/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Nils_Gustaf_Dalén.yaml` | 已入库的领域/关系数据 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
