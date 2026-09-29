# 和平奖得主立传提示词（OpenPeace 批次 1：William Randal Cremer）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 William Randal Cremer（1903 诺贝尔和平奖得主、各国议会联盟与国际仲裁联盟的共同创始人）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用到任何和平奖得主；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业人物。
- **本实例**：Sir William Randal Cremer（威廉·兰德尔·克里默，通行以中名 Randal 称呼）。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」与「事业领域」的结构化表达；Cremer 是「工人出身的和平建制派」——木匠、工运书记、议员三段人生，以国际仲裁把工人与和平运动接合，结构化表达的重点是「从工坊到议会」的阶梯。

---

## 二、背景信息 【人物专属】

- **目标人物**：William Randal Cremer（1828-03-18 法勒姆 ~ 1908-07-22 伦敦哈格斯顿，享年 80 岁）
- **气质关键词**：**国际仲裁运动的旗手、各国议会联盟共同创始人、工人出身的自由党议员** —— 1903 诺贝尔和平奖获奖理由：
  > "for his longstanding and devoted effort in favour of the ideas of peace and arbitration"（表彰他长期不懈地倡导和平与仲裁理念）
- **设计母题**：**握手与条约（handshake and treaty）**。木匠的手艺之手 → 工会组织之手 → 议会仲裁请愿之手，最终落在 1899/1907 海牙和会的地基上——用「连接线 + 印章」的几何意象替代空泛的橄榄枝。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Randal_Cremer/page.md`（含 frontmatter QID Q189841；目录名/维基标题为 Randal Cremer）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Randal_Cremer` 四件套到 `peace/presentations/pages/20th_century/Randal_Cremer/`（**第一轮已核对，事实基准如下**）：
  - 生卒（1828-03-18 生于汉普郡法勒姆 Fareham ~ 1908-07-22 逝于伦敦哈格斯顿，享年 80 岁；死因肺炎）
  - 国籍（英国）
  - 家庭（工人阶级出身；父为马车夫，Cremer 出生后不久离家；母抚养他与两个姐妹；婚姻 page.md 未载，禁编造）
  - 教育（地方卫理公会学校 + 免费公开讲座自学；木匠学徒出身）
  - 任职（1852 移居伦敦任工会组织者 → 1865 国际工人协会书记（1867 因组织决定女性入会而辞职）→ 1885–1895 及 1900–1908 自由党哈格斯顿选区下院议员）
  - 关键荣誉（Nobel Peace Prize 1903 独享（首位单人获奖者）；法国荣誉军团骑士（Chevalier）；挪威圣奥拉夫骑士；1907 授下级勋位爵士 Knight Bachelor）
  - 核心事业清单（①共同创立各国议会联盟 ②共同创立国际仲裁联盟 ③1897 Olney–Pauncefote 条约推动（被美参议院否决）④1899/1907 海牙和会铺路 ⑤1903 诺贝尔和平奖，£8,000 中 £7,000 捐作国际仲裁联盟基金）
  - 关键时间线（15 节点为宜；页面素材中等偏短，勿凑数虚增）
- **⚠ 素材量警示**：本篇 page.md 正文约 82 行（含注释区），可用正文约 30 行。幻灯片按 12 页规划（见第 6 步），每页以 page.md 明载为限，宁缺毋滥。

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Randal_Cremer/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Randal_Cremer_zh`、`VIDEO_NAME=Randal_Cremer_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 本地 `images.txt` 为空，无可用肖像
- **处理方式**：封面与身份页用装饰圆占位（中央姓名首字母 R.C. 或握手/天平矢量图形），全篇不出现"肖像照"字样

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

> 把事业领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 4 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international arbitration | 国际仲裁 | 一生旗手事业、获奖理由核心 | 仲裁页、诺奖页 |
| 1 | peace movement | 和平运动 | 海牙和会铺路、和平组织创立 | 运动页 |
| 2 | trade unionism | 工会运动 | 伦敦工会组织者、国际工人协会书记 | 早年页 |
| 3 | inter-parliamentary cooperation | 议会间合作 | 各国议会联盟共同创始 | 联盟页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 3 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Frédéric Passy | 无向 | 1888–1889 共同创立议会间会议（后各国议会联盟） |
| founder | Inter-Parliamentary Union | 人→机构 | 1889 共同创始 |
| founder | International Arbitration League | 人→机构 | 共同创始，1903 诺奖 £7,000 捐作其基金 |

- 方向约定：founder 人→机构有向；colleague 无向自动 from<to 归一
- **禁写清单**：Karl Marx（仅"respect by Marx"叙述，无关系类型可挂，不入库）；William Jennings Bryan / Andrew Carnegie（page.md 仅"cultivated allies"一笔带过，禁建 colleague）；父（无名，马车夫离家）与母（无名）均不入库；Passy 篇已建 Passy–Cremer 边，本篇为镜像幂等

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：质朴、坚韧、工人阶级的 slate 灰蓝
- **配色**：石板灰蓝（manifest 预分配主色 `#37474F`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeArbit` 国际仲裁 — 条约蓝 `#1F5F8B`
  - `badgeIPU` 各国议会联盟 — 议事紫 `#5E35B1`
  - `badgeUnion` 工会岁月 — 工装赭 `#8C5A2F`
  - `badgeNobel` 1903 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 印章方框意象（低饱和），呼应「条约与印章」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面无头像时**：装饰圆占位 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（United Kingdom），底部状态栏给出 `国籍 | 事业 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧装饰圆 + 右侧信息网格，含至少：生卒、国籍、出生地、家庭（父/母客观一句）、教育（卫理公会学校/自学/木匠学徒）、任职序列、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调；素材有限按 12 页规划】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 国际仲裁运动旗手 / William Randal Cremer 1828–1908 + 四色 badge + 装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右信息网格（含家庭、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 工运书记 / 议会仲裁请愿 / IPU 与 IAL / 海牙和会铺路 / 1903 诺奖
04  法勒姆的木匠学徒 (1828–1852) — 马车夫之子离家、母亲抚养、卫理公会学校、免费讲座自学、手艺学徒
05  伦敦工运书记 (1852–1868) — 工会组织者、1865 国际工人协会书记、1867 辞职始末（客观一句）
06  仲裁理念的起点 (1868–1885) — 首次竞选下院即倡仲裁、议会外请愿
07  下院议员 (1885–1895; 1900–1908) — 哈格斯顿选区、自由党、两段任期与 1895–1900 空档
08  大西洋两岸的盟友 — Passy/Bryan/Carnegie 的联络网、1897 Olney–Pauncefote 条约及其被否决
09  各国议会联盟 (1887–1889) — 与 Passy 的法英双边请愿（112 签名）、1888 十人代表团、1889 首届大会
10  国际仲裁联盟与海牙铺路 — IAL 共同创始、1899/1907 海牙和会的地基
11  1903 诺贝尔和平奖 — 首位单人得主、获奖理由、£7,000 捐作 IAL 基金、荣誉军团/圣奥拉夫/1907 爵士
12  晚年与身后 (1908–) — 肺炎去世、哈格斯顿小学命名、1985 奖牌拍卖（一句客观）
13  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。素材少时用大字号 + 留白，禁注水。

**Cremer 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 目录名与全名 | 维基标题/目录为 Randal Cremer；manifest 规范名为 William Randal Cremer；封面用全名，正文可称 Randal Cremer，首次出现注明"通行以中名 Randal 称呼" |
| 诺奖理由措辞 | 官方理由 "for his longstanding and devoted effort in favour of the ideas of peace and arbitration"；1903 为**独享**（首位单人得主），勿写与他人共享 |
| 奖金去向 | £8,000 中捐 £7,000 作国际仲裁联盟（International Arbitration League）基金；勿把 IAL 与 IPU 混写 |
| 两个机构 | Inter-Parliamentary Union（各国议会联盟，1889，与 Passy 共同创始）≠ International Arbitration League（国际仲裁联盟），两机构分立 |
| IWA 辞职 | 1867 辞去国际工人协会书记系因组织决定女性入会资格而其本人强烈反对——按 page.md 客观记录一句，不加评价；Marx 尊重他为 page.md 明载，但禁建关系 |
| 反妇女选举权 | page.md 明载其反对妇女选举权（Anti-Suffrage）——客观记录一句，不回避也不渲染 |
| 议员任期 | 1885–1895 与 1900–1908 两段，1895–1900 空档勿抹平；1908 死于肺炎任内 |
| Olney–Pauncefote 条约 | 1897 美英仲裁条约，被美参议院否决、未生效——"would have required"语气，勿写成"促成生效" |
| 无载禁写 | 不写婚姻/子女、不写具体教育机构 beyond 卫理公会学校、不编造工会具体名目、不写海牙和会上的具体角色（仅"preparing the ground"） |
| 荣誉套件 | Chevalier of the Légion d'honneur、挪威圣奥拉夫骑士、1907 Knight Bachelor 三项并列，勿升格或混写年份 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| international arbitration | 国际仲裁 | 获奖理由核心，一生旗手事业 |
| Inter-Parliamentary Union | 各国议会联盟 | 1889 共同创始，与 IAL 区分 |
| International Arbitration League | 国际仲裁联盟 | £7,000 诺奖基金受方 |
| International Workingmen's Association | 国际工人协会 | 1865–1867 任书记 |
| Olney–Pauncefote Treaty | 奥尔尼–庞斯富特条约 | 1897 被美参议院否决 |
| Hague Conventions of 1899 and 1907 | 1899/1907 海牙公约 | Cremer 铺路，非与会主导 |
| trade unionism | 工会运动 | 与 peace movement 分列 |
| Knight Bachelor | 下级勋位爵士 | 1907 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Awaken** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 觉醒 / 上升 / 信念感
- **匹配理由**:
  - "Awaken" 呼应 Cremer 的人生阶梯——从法勒姆木匠学徒到国际仲裁运动的旗手，一路是「觉醒与上升」
  - 信念感匹配获奖理由 "longstanding and devoted effort" 的长期坚持
- **本地路径**: `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` → `presentations/20th_century/Randal_Cremer/Awaken.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Randal_Cremer/page.md` | 本地 Wikipedia 正文（事实基准，素材中等偏短） |
| `peace/presentations/pages/20th_century/Randal_Cremer/images.txt` | 空（装饰圆占位） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Randal_Cremer.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
