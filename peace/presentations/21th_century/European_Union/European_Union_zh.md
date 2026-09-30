# 和平奖得主立传提示词（OpenPeace 21 世纪批次 4：European Union）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 European Union（2012 诺贝尔和平奖得主、欧洲联盟组织机构）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【机构专属】` 的部分需按目标机构替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业机构。
- **本实例**：European Union（欧洲联盟，超国家政治经济联盟，27 个成员国）。
- **设计哲学**：**组织机构立传以「机构概览页」替代人物「身份信息页」**——旗帜/成立条约/总部/成员国数/治理结构替代生卒与师承；「从煤钢共同体到政治联盟」的条约演进是本篇的灵魂。

---

## 二、背景信息 【机构专属】

- **目标机构**：European Union（1993-11-01 《马斯特里赫特条约》生效时正式成立，总部布鲁塞尔（事实上的），在存续中）
- **气质关键词**：**从战争废墟中生长的联盟、主权共享的实验、和平与和解的工程** —— 2012 诺贝尔和平奖获奖理由：
  > "for over six decades contributed to the advancement of peace and reconciliation, democracy and human rights in Europe"（表彰其六十余年来对推进欧洲和平与和解、民主与人权的贡献）
- **设计母题**：**十二星环与条约之链（circle of twelve stars and the chain of treaties）**。蓝底金星旗、巴黎—罗马—马斯特里赫特—里斯本的条约序列、法德和解的起点——这是比「和平鸽」更贴合 EU 的视觉语言。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/21th_century/European_Union/page.md`（含 frontmatter QID Q458）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：使命领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【机构专属】

- ✅ 已下载四件套到 `peace/presentations/pages/21th_century/European_Union/`（**事实基准如下**）：
  - 机构性质（政治与经济联盟，27 个成员国，supranational union；常被描述为兼具联邦与邦联特征的 sui generis 政治实体）
  - 成立（Maastricht Treaty 1993-11-01 生效正式确立 EU；其前身为欧洲各共同体：ECSC 1952 / EEC 与 Euratom 1958；2009 里斯本条约赋予单一法律人格）
  - 条约时间线（巴黎条约 1951/生效 1952；罗马条约 1957/生效 1958；合并条约 1967；单一欧洲法案 1986/1987；马斯特里赫特 1992/1993；阿姆斯特丹 1997/1999；尼斯 2001/2003；里斯本 2007/2009）
  - 扩大（1973 英爱丹 → 1981 希腊 → 1986 西葡 → 1995 奥芬瑞 → 2004 十国 → 2007 保罗 → 2013 克罗地亚第 28 国；2020 英国脱欧，唯一退出成员国）
  - 治理（欧盟理事会/欧盟委员会/欧洲议会/欧盟法院/欧洲央行；驻地分设布鲁塞尔、卢森堡、法兰克福、斯特拉斯堡）
  - 货币（欧元，2002 纸币硬币流通；欧元区现 21 国）
  - 关键荣誉（Nobel Peace Prize 2012；Princess of Asturias Award for Concord）
  - 使命领域清单（①法德和解与欧洲和平 ②单一市场与关税同盟 ③人员货物服务资本自由流动 ④申根区 ⑤共同外交与安全政策 ⑥扩张与候选国标准）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下创建 `European_Union/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=European_Union_zh`、`VIDEO_NAME=European_Union_zh`

### 第 3 步：收集图片 【机构专属】

- 查看 `images.txt`；欧盟旗帜/马斯特里赫特条约签署照/成员国地图为候选主视觉
- 无合适图像时用装饰图形占位（须在图注写明）

### 第 4 步：使命领域梳理 + 入库 【模板通用，机构专属内容】

> 把使命领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 5 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | european integration | 欧洲一体化 | 从煤钢共同体到政治联盟的主线 | 全篇 |
| 1 | peace and reconciliation | 和平与和解 | 2012 诺奖核心理由（法德和解起点） | 和平页 |
| 2 | democracy | 民主 | 哥本哈根标准与议会直选 | 治理页 |
| 3 | human rights | 人权 | 欧洲人权公约传统与入盟标准 | 治理页 |
| 4 | economic integration | 经济一体化 | 关税同盟、单一市场、欧元 | 经济页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，机构专属内容】

> 以下 3 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| other | European Coal and Steel Community | 无向 | 法律前身，1952 年巴黎条约建立 |
| other | European Economic Community | 无向 | 法律前身，1958 年罗马条约建立 |
| other | European Atomic Energy Community | 无向 | 平行条约共同体，1958 年与 EEC 同批生效 |

- 组织机构省略 gender/nationalities；birth_date 用成立日（1993-11-01，page.md 明载）
- 前身机构由 seed_person.py 自动建占位记录

### 第 5 步：设计配色方案 【模板通用，机构专属色彩】

- **气质**：庄重、星空、条约的连续性
- **配色**：深靛紫（manifest 预分配主色 `#372A75`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeTreaty` 条约演进 — 钢蓝 `#2E5E8C`
  - `badgeEnlarg` 扩大进程 — 森绿 `#1E4D3B`
  - `badgeSingle` 单一市场与欧元 — 琥珀 `#E07B30`
  - `badgeNobel` 2012 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 十二星环弧线意象（低饱和），呼应「星环之盟」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有主视觉**：右上角旗帜/签署照 + `draw=coveraccent!50` 细边框 + 机构名小字注。
2. **封面有性质行**：顶部副标题或底部状态栏明示机构性质（Supranational union / 27 member states），底部状态栏给出 `性质 | 总部 | 主要奖项` 三要素。
3. **必须有机构概览页（替代身份信息页）**：封面之后、核心内容之前。左侧主视觉 + 右侧信息网格，含至少：成立（条约与日期）、前身、总部、成员国数、官方语言数、治理机构、主要荣誉、使命领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【机构专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 从战争废墟到联盟 / European Union 1993– + 四色 badge + 右上主视觉 + 性质行
02  机构概览页（★ 必做）— 左主视觉 + 右信息网格（成立、前身、总部、成员国、治理、荣誉、使命）
03  核心概览 — 关税同盟 / 单一市场 / 和平与和解 / 条约演进 / 2012 诺奖
04  战后起点：两次大战的反面 (1945–1950) — 丘吉尔苏黎世演讲、舒曼宣言 1950-05-09、关键动机（煤钢联营使战争"不仅不可想象，而且物质上不可能"为 page.md 明载口径的转述）
05  煤钢共同体 (1951–1957) — 巴黎条约、六创始国、ECSC 为欧盟主要机构之源
06  罗马条约与三共同体 (1957–1967) — EEC/Euratom、关税同盟、合并条约
07  扩大与深化 (1973–1992) — 英爱丹、希腊西葡、单一欧洲法案、申根、直选议会
08  马斯特里赫特：EU 的诞生 (1993) — 三支柱、欧盟公民身份、哥本哈根标准
09  里斯本条约与法律人格 (2009) — 单一法律实体、常任理事会主席、三支柱终结
10  2012 诺贝尔和平奖 — 获奖理由原文、六十年和平与和解、领奖事实
11  货币与市场 — 欧元 2002、欧元区 21 国、申根区
12  脱欧与考验 (2016–2020) — 2016 公投 51.9%、2020-01-31 退出、 Next Generation EU
13  今天的欧盟 — 27 国、候选国九个、目标 2030 年 35 成员国的政治优先（page.md 明载口径）
14  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 机构专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**EU 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| "成立"三种口径 | ECSC 1952 / EEC 1958 / EU（马约生效）1993-11-01——机构概览页与封面一律用 1993-11-01，前身在独立页交代，勿混写"成立于 1958" |
| 诺奖理由 | 官方理由 "for over six decades contributed to the advancement of peace and reconciliation, democracy and human rights in Europe"，照抄勿改写；2012 年为单独得主，无共同得主 |
| 领导人≠缔造者 | 在任领导人（von der Leyen/Costa/Metsola 等）仅可写"现任职务"，禁写"创始人"；欧盟没有单一"创始人"，只有"founding fathers"群体叙事 |
| 马约设计者归属 | page.md 明文 "whose main architects were Horst Köhler, Helmut Kohl and François Mitterrand"——若引用须照录页面原文；外界常见归功（Kohl/Mitterrand/Delors）中 Delors 为 page.md 未载，禁写 |
| 成员国数 | 2012 获奖时 27 国（克罗地亚 2013 入盟后才 28、英国 2020 退出后复 27）；写"27 个成员国"指当前口径，注意上下文年份 |
| 舒曼宣言日期 | 1950-05-09（欧洲日来源）；勿与巴黎条约 1951-04-18 签署/1952-07-23 生效混淆 |
| 经济数据 | GDP/人口为 2026 年估算值且随修订变动，幻灯片引用须带"2026 年估算"口径，或干脆不用具体数字 |
| 地缘敏感 | 涉俄乌战争、对俄制裁、Brexit 谈判等内容全部按 page.md 客观记录时间线，不加立场表述 |
| 无载禁写 | 不写诺奖委员会内部讨论细节；不写欧盟军队等 page.md 未展开的领域；不写 2025 年 12 月泄露事件的后续（page.md 仅载泄露本身，若用须注明"据页面所载"） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| supranational union | 超国家联盟 | EU 的机构性质 |
| European Coal and Steel Community | 欧洲煤钢共同体 | ECSC，1952–2002 |
| Treaty of Rome | 罗马条约 | 1957 签署/1958 生效，创 EEC |
| Treaty of Maastricht | 马斯特里赫特条约 | 1992 签署/1993-11-01 生效，创 EU |
| Treaty of Lisbon | 里斯本条约 | 2009-12-01 生效，单一法律人格 |
| Copenhagen criteria | 哥本哈根标准 | 1993 年入盟标准 |
| Schengen Area | 申根区 | 1985 协定，护照管控取消 |
| eurozone | 欧元区 | 现 21 国 |
| sui generis | 自成一格 | 描述 EU 政治实体的学术用语 |
| Brexit | 英国脱欧 | 2016 公投/2020-01-31 退出 |

---

## 四、背景音乐选择 ✅ 【机构专属】

- **选定曲目**: **Timeless** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 沉稳 / 纪录片 / 长期纲领
- **匹配理由**:
  - "Timeless" 呼应"六十余年的和平工程"——EU 的本质是一部跨越条约代际的长期纲领
  - 沉稳纪录片气质匹配条约演进的叙事节奏，而非英雄史诗
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → `presentations/21th_century/European_Union/Timeless.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/European_Union/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/21th_century/European_Union/images.txt` | 旗帜与插图 URL |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/European_Union.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
