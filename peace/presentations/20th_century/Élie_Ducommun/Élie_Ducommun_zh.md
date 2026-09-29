# 和平奖得主立传提示词（OpenPeace 批次 1：Élie Ducommun）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Élie Ducommun（1902 诺贝尔和平奖得主、伯尔尼国际和平局首任局长）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用到任何和平奖得主；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业人物。
- **本实例**：Élie Ducommun（埃利·迪科门）。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」与「事业领域」的结构化表达；Ducommun 是「组织者的和平主义」——他一生辗转教书、办报、经商、行政，最终以无薪局长身份把国际和平局经营成首个非政府国际和平组织，结构化表达的重点是「机构的经营」。

---

## 二、背景信息 【人物专属】

- **目标人物**：Élie Ducommun（1833-02-19 日内瓦 ~ 1906-12-07 伯尔尼，享年 73 岁）
- **气质关键词**：**国际和平局首任局长、无薪的理想主义行政家、百科全书式的报人** —— 1902 诺贝尔和平奖获奖理由：
  > "for his untiring and skilful directorship of the Bern Peace Bureau"（表彰他不知疲倦且娴熟地领导伯尔尼国际和平局）
- **设计母题**：**枢纽与齿轮（hub and gears）**。国际和平局是各国和平组织的通信枢纽，Ducommun 是让齿轮咬合运转的行政家——以「中心辐射 + 精密传动」的几何意象替代空泛的橄榄枝。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Élie_Ducommun/page.md`（含 frontmatter QID Q122368）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Élie_Ducommun` 四件套到 `peace/presentations/pages/20th_century/Élie_Ducommun/`（**第一轮已核对，事实基准如下**）：
  - 生卒（1833-02-19 生于日内瓦 ~ 1906-12-07 逝于伯尔尼，享年 73 岁）
  - 国籍（瑞士）
  - 教育（page.md 未载正式学历，禁编造）
  - 任职（家庭教师/语言教师 → 记者 → 瑞士联邦总理府翻译 1869–1873 → Jura-Simplon 钢铁公司书记 1873–1891 → 国际和平局局长 1891–1906 无薪 → 《Correspondance bi-mensuelle》局长 1895 起）
  - 关键荣誉（Nobel Peace Prize 1902 与 Gobat 共享；诺奖演讲 1904-05-16 "The Futility of War Demonstrated by History"）
  - 核心事业清单（①协助创立和平与自由联盟 1867 ②国际和平局首任局长 1891 ③拒领薪水、纯理想主义服务 ④局刊 Correspondance bi-mensuelle 1895 ⑤1902 诺贝尔和平奖）
  - 关键时间线（本页正文较短，15 节点为宜，勿凑数虚增）
- **⚠ 素材量警示**：本篇 page.md 仅 42 行，正文信息远少于同批其他四人。幻灯片按 12–13 页规划（见第 6 步），每页信息以 page.md 明载为限，**宁缺毋滥、禁编造细节**。

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Élie_Ducommun/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Élie_Ducommun_zh`、`VIDEO_NAME=Élie_Ducommun_zh`（宏名避变音符时可用 ASCII 宏名 Ducommun）

### 第 3 步：收集图片 【人物专属】

- ✅ 本地 `images.txt` 无真实肖像（仅 Commons 标志图，禁用作肖像）
- **处理方式**：封面与身份页用装饰圆占位（中央姓名首字母 E.D. 或和平鸽矢量图形），全篇不出现"肖像照"字样，勿把他人照片误用为 Ducommun

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

> 把事业领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 4 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace movement | 和平运动 | 国际和平局经营、和平组织协作 | 和平局页 |
| 1 | international organization | 国际组织 | 首个非政府国际和平组织的管理 | 和平局页 |
| 2 | opinion journalism | 政论新闻 | 记者/翻译出身、局刊 Correspondance bi-mensuelle | 早年页、局刊页 |
| 3 | pacifism | 和平主义 | 无薪服务、理想主义立场 | 概览页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 2 条与 yaml 完全一致，已入库（仅收 page.md 明载关系；本页正文极短，诚实值 relations=2）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Charles Albert Gobat | 无向 | 1902 诺贝尔和平奖共同得主 |
| founder | League of Peace and Freedom | 人→机构 | 1867 协助创立和平与自由联盟 |

- 方向约定：founder 人→机构有向；co-honored 无向自动 from<to 归一
- **禁写清单**：曾外孙 Martin Brauen（亲属关系无类型可挂，不入库）；Gobat 继任和平局方向（1906 Gobat 接任局长，系 Gobat 篇叙事，不反向建关系）；不编造导师/学生/妻子（page.md 全无记载）

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：勤勉、沉静、行政者的深红
- **配色**：深酒红（manifest 预分配主色 `#7A1E28`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeBureau` 国际和平局 — 枢纽红 `#A31621`
  - `badgeJournal` 政论与局刊 — 墨蓝 `#1F3A5F`
  - `badgeLigue` 和平与自由联盟 — 联盟绿 `#2E6B4F`
  - `badgeNobel` 1902 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 同心枢纽辐条意象（低饱和），呼应「枢纽与齿轮」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面无头像时**：装饰圆占位 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（Switzerland），底部状态栏给出 `国籍 | 事业 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧装饰圆 + 右侧信息网格，含至少：生卒、国籍、出生地、任职序列（教师→记者→翻译→钢铁公司→和平局）、主要荣誉、核心领域；教育栏 page.md 无载则写"—"留白，禁编造。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调；素材有限按 12 页规划】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 国际和平局首任局长 / Élie Ducommun 1833–1906 + 四色 badge + 装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右信息网格（含任职序列、荣誉、核心领域；教育栏留白）
03  核心贡献概览 — 和平与自由联盟 / 国际和平局 / 局刊 / 1902 诺奖
04  日内瓦早年 (1833–1867) — 家庭教师、语言教师、记者生涯（以 page.md 明载职业序列为限）
05  和平与自由联盟 (1867) — 协助创立的背景与同代人环境（禁展开联盟后史细节）
06  联邦与实业岁月 (1869–1891) — 联邦总理府翻译 1869–1873、Jura-Simplon 钢铁公司书记 1873–1891
07  国际和平局首任局长 (1891) — 伯尔尼、首个非政府国际和平组织、拒领薪水的理想主义
08  枢纽的经营 — 组织协调各国和平团体、 keen organizational skills 确保团体成功
09  局刊 Correspondance bi-mensuelle (1895) — 和平局的通讯喉舌
10  1902 诺贝尔和平奖 — 与 Gobat 共享、获奖理由、1904-05-16 诺奖演讲 "The Futility of War Demonstrated by History"
11  晚年与遗产 — 任局长至 1906 去世、Gobat 接任、组织者和平主义的示范意义
12  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。素材少时用大字号 + 留白，禁注水。

**Ducommun 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 页面素材极少 | page.md 正文仅导语一段，正文页禁编造生平细节；一切以明载职业序列与和平局事业为限 |
| 诺奖理由措辞 | 官方理由 "for his untiring and skilful directorship of the Bern Peace Bureau"，强调**领导和平局**；获奖年份 1902，勿写 1901 |
| 共同得主 | 与 Charles Albert Gobat 共享 1902；两人分工（Ducommun 管国际和平局 / Gobat 管各国议会联盟系其本人篇叙事）勿在 Duocommun 篇替 Gobat 展开 |
| 机构名 | International Peace Bureau（国际和平局）设于伯尔尼，获奖理由称 Bern Peace Bureau；Gobat 篇称 Permanent International Peace Bureau——本篇统一用 International Peace Bureau |
| 和平与自由联盟 | 1867 协助创立（helped to found）；勿写"创始人/首任主席"，也勿与 Passy 篇的 Ligue Internationale et Permanente de la Paix 混为同一组织 |
| 无薪局长 | refused to accept a salary、纯理想主义服务——可写，是本篇性格锚点 |
| 诺奖演讲 | 1904-05-16 "The Futility of War Demonstrated by History"（nobelprize.org 链接明载），只写标题与日期，禁引用未载原文 |
| 任职年份 | 联邦总理府翻译 1869–1873、钢铁公司书记 1873–1891、和平局局长 1891–1906，三段年份勿混 |
| 无载禁写 | 不写家庭/婚姻/子女（仅曾外孙 Martin Brauen 出现在 infobox Relatives，禁建关系）、不写教育经历、不写去世原因 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| International Peace Bureau | 国际和平局 | 1891 设于伯尔尼，首个非政府国际和平组织 |
| Bern Peace Bureau | 伯尔尼和平局 | 获奖理由措辞，与机构名同指 |
| League of Peace and Freedom | 和平与自由联盟 | 1867 协助创立，非其独创 |
| Correspondance bi-mensuelle | 《双周通讯》 | 和平局局刊，1895 起任局长 |
| federal Chancellery | 瑞士联邦总理府 | 1869–1873 任翻译 |
| opinion journalism | 政论新闻 | frontmatter field_of_work 口径 |
| pacifism | 和平主义 | 与具体政治主张区分 |
| untiring directorship | 不知疲倦的领导 | 官方获奖理由关键词 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **PAST** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 历史感 / 深沉 / 回望
- **匹配理由**:
  - "PAST" 的历史纵深匹配 Ducommun 的角色——他是 19 世纪和平运动史的组织者与记录者，事业本身就是「为历史保存和平的脉络」
  - 深沉回望的气质匹配其无薪坚守与身后荣誉的叙事
- **本地路径**: `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → `presentations/20th_century/Élie_Ducommun/PAST.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Élie_Ducommun/page.md` | 本地 Wikipedia 正文（事实基准，素材极短） |
| `peace/presentations/pages/20th_century/Élie_Ducommun/images.txt` | 无可用肖像（装饰圆占位） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Élie_Ducommun.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
