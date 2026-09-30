# 和平奖得主立传提示词（OpenPeace 21 世纪批次 4：OPCW）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 OPCW（2013 诺贝尔和平奖得主、禁止化学武器组织）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【机构专属】` 的部分需按目标机构替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业机构。
- **本实例**：Organisation for the Prohibition of Chemical Weapons（禁止化学武器组织，OPCW，政府间组织，总部海牙）。
- **设计哲学**：**组织机构立传以「机构概览页」替代人物「身份信息页」**——193 个缔约国、核查与销毁的日常、把化武变成国际法禁忌的工程是本篇的灵魂。

---

## 二、背景信息 【机构专属】

- **目标机构**：OPCW（1997-04-29 《化学武器公约》生效日与《公约》同步成立，总部荷兰海牙，在存续中）
- **气质关键词**：**化武禁忌的守门人、核查与销毁的执行者、海牙的多边机制** —— 2013 诺贝尔和平奖获奖理由：
  > "for its extensive efforts to eliminate chemical weapons"（表彰其为消除化学武器所做的广泛努力）
- **设计母题**：**禁忌之盾与半圆 HQ（the taboo shield and the semicircle HQ）**。八层半圆总部大楼、楼后对全体受害者的永久纪念装置、核查员的联合国通行证——这是比「和平鸽」更贴合 OPCW 的视觉语言。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/21th_century/Organisation_for_the_Prohibition_of_Chemical_Weapons/page.md`（含 frontmatter QID Q842490）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：使命领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【机构专属】

- ✅ 已下载四件套到 `peace/presentations/pages/21th_century/Organisation_for_the_Prohibition_of_Chemical_Weapons/`（**事实基准如下**）：
  - 机构性质（政府间组织；《化学武器公约》CWC 的实施机构；193 个成员国=全部 CWC 缔约国；4 个联合国会员国未加入——埃及、以色列（仅签署未批准）、朝鲜、南苏丹）
  - 成立（CWC 1997-04-29 生效；总干事列表首任 José Bustani 1997-05-13 就任）
  - 总部（海牙，力压维也纳与日内瓦的选址竞争；1998-05-20 荷兰女王 Beatrix 主持启用；美国建筑师 Gerhard Kallmann 设计的八层半圆楼；楼后设全体受害者永久纪念装置；Rijswijk 有设备库与实验室）
  - 治理（缔约国大会 CSP/执行理事会 EC 41 国/技术秘书处 TS；官方语言六种；2020 年预算 70,958,760 欧元）
  - 关键荣誉（Nobel Peace Prize 2013-10-11 宣布；以此为基础 2014 年设立 OPCW–The Hague Award，奖金约 90 万欧元诺奖奖金作基金）
  - 使命领域清单（①化武销毁核查 ②缔约国申报评估与现场视察 ③附表化学品工业核查 ④指称使用化武的事实调查 ⑤与联合国体系的合作）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下创建 `Organisation_for_the_Prohibition_of_Chemical_Weapons/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Organisation_for_the_Prohibition_of_Chemical_Weapons_zh`、`VIDEO_NAME=Organisation_for_the_Prohibition_of_Chemical_Weapons_zh`

### 第 3 步：收集图片 【机构专属】

- 查看 `images.txt`；OPCW 总部大楼照/缔约国大会照/成员国分布图为候选主视觉
- 无合适图像时用装饰图形占位（须在图注写明）

### 第 4 步：使命领域梳理 + 入库 【模板通用，机构专属内容】

> 把使命领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 5 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | disarmament | 裁军 | 2013 诺奖核心理由（消除化学武器） | 核心页 |
| 1 | chemical weapons convention | 化学武器公约 | CWC 的实施机构 | 公约页 |
| 2 | arms control | 军备控制 | 多边军控体系中的定位 | 体系页 |
| 3 | non-proliferation | 防扩散 | 附表化学品与出口管控 | 核查页 |
| 4 | international law | 国际法 | 化武使用成为国际法下的禁忌（Jagland 语） | 诺奖页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，机构专属内容】

> 以下 2 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| other | United Nations | 无向 | 非 UN 专门机构，2000-09-07 与 UN 签署合作协议，系联合国体系内相关组织 |
| colleague | José Bustani | 无向 | 首任总干事（1997 年就任），2002 年被缔约国特别会议解职 |

- 组织机构省略 gender/nationalities；birth_date 用成立日（1997-04-29，page.md 明载 Formation）
- 对手方由 seed_person.py 自动建占位记录（United Nations 用库内既有记录 id 6777）

### 第 5 步：设计配色方案 【模板通用，机构专属色彩】

- **气质**：冷峻、秩序、禁忌的重量
- **配色**：深绯红（manifest 预分配主色 `#7A1E28`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeCWC` 化武公约 — 钢蓝 `#2E5E8C`
  - `badgeVerify` 核查与销毁 — 森绿 `#1E4D3B`
  - `badgeHague` 海牙多边机制 — 琥珀 `#E07B30`
  - `badgeNobel` 2013 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 半圆楼弧线意象（低饱和），呼应「半圆之盟」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有主视觉**：右上角总部/标志图 + `draw=coveraccent!50` 细边框 + 机构名小字注。
2. **封面有性质行**：顶部副标题或底部状态栏明示机构性质（Intergovernmental organization / The Hague），底部状态栏给出 `性质 | 总部 | 主要奖项` 三要素。
3. **必须有机构概览页（替代身份信息页）**：封面之后、核心内容之前。左侧主视觉 + 右侧信息网格，含至少：成立（CWC 生效日）、总部、成员国数、官方语言、治理机构、总干事（现任）、主要荣誉、使命领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【机构专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 化武禁忌的守门人 / OPCW 1997– + 四色 badge + 右上主视觉 + 性质行
02  机构概览页（★ 必做）— 左主视觉 + 右信息网格（成立、总部、成员国、语言、治理、总干事、荣誉、使命）
03  核心概览 — CWC 实施 / 核查 / 销毁 / 调查 / 2013 诺奖
04  公约与诞生 (1992–1997) — CWC 生效 1997-04-29、海牙选址之争（压过维也纳与日内瓦）
05  半圆总部 (1998) — Beatrix 女王启用、Kallmann 设计、受害者永久纪念装置
06  三大机构 — 缔约国大会 CSP / 执行理事会 EC 41 国 / 技术秘书处 TS
07  核查的日常 — 销毁设施 24/7（CCTV 评估）、附表 1/2/3 化学品工业核查时限
08  权限与调查 — 指称使用调查、2018-06 授予指认袭击责任方的权限（82:24 表决）
09  首任总干事风波 (2002–2003) — Bustani 被特别会议解职（48:7:43）、ILO 行政法庭 2003 判决程序不当并判赔偿——按 page.md 逐条客观呈现
10  2013 诺贝尔和平奖 — "for its extensive efforts to eliminate chemical weapons"、Jagland 禁忌评语、叙利亚背景
11  叙利亚任务 (2013–2014) — 监督叙利亚申报化武销毁，至 2014-09 约 97% 销毁；2021-04-21 叙利亚被中止表决权
12  规则演进 — 2019-11 诺维乔克列入管控清单、OPCW–The Hague Award 2014
13  安全威胁 — 2018-04 GRU 人员渗透未遂被荷兰情报部门拘捕驱逐（与 Skripal 案调查相关的英方指控口径）——客观记录
14  今天的 OPCW — 现任总干事 Sabrina Dallafior Matter（2026 年就任，首位女性领导人）、193 国
15  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 机构专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**OPCW 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 成立日期 | 机构成立与 CWC 生效同为 1997-04-29（page.md Formation 明载）；勿写成"1997-05-13"（那是首任总干事就任日） |
| 诺奖理由 | 官方理由 "for its extensive efforts to eliminate chemical weapons"，照抄勿改写；主语是 it（机构独得，无共同得主）；宣布日 2013-10-11 |
| Bustani 事件 | 双方说法并陈：美方三点理由 vs Bustani 自辩（伊拉克批约触怒美方）；ILO 行政法庭 2003-07-16 判决"解职不当"；Monbiot 观点为页面转述的评论，标注"卫报专栏观点"勿写成定论——全程不做评价性收束 |
| 叙利亚内容 | 叙利亚化武销毁（97% 口径至 2014-09）与 2021 中止表决权均客观记录；"屡次使用毒气"按页面原文口径呈现，不加定性形容 |
| 俄/英指控 | 2018 GRU 渗透未遂与 Skripal 案关联为"英国文化大臣的指控口径"；Novichok 列管的表决背景同理——照录事件链，不写"俄方渗透/恶意"等定性语 |
| 领导人≠创始人 | 总干事是雇员首长非"创始人"；OPCW 由 CWC 缔约国创立，勿写"某某创立了 OPCW"；Sabrina Dallafior Matter 2026 年就任且是首位女性领导人（page.md 明载） |
| 预算数字 | 2020 年预算 70,958,760 欧元带年份口径，勿写成"当前预算" |
| 无载禁写 | 不写 CWC 谈判史细节（page.md 未展开）；不写未具名 inspector 的个体故事；不写预算构成；不写诺奖典礼细节（page.md 未载） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Chemical Weapons Convention | 化学武器公约 | CWC，1997-04-29 生效 |
| Conference of the States Parties | 缔约国大会 | CSP，年度例会 |
| Executive Council | 执行理事会 | EC，41 国两年任期 |
| Technical Secretariat | 技术秘书处 | TS，核查执行主体 |
| Schedule 1/2/3 chemicals | 附表 1/2/3 化学品 | 核查强度递减，勿混时限 |
| Director-General | 总干事 | 最长两任四年 |
| Novichok agents | 诺维乔克毒剂 | 2019-11 列入管控清单 |
| OPCW–The Hague Award | OPCW–海牙奖 | 2014 设立，诺奖奖金约 90 万欧元作基金 |
| challenge inspection | 质询视察 | 3/4 多数可阻止发起 |
| taboo | 禁忌 | Jagland 评语核心词，引用时保留原词 |

---

## 四、背景音乐选择 ✅ 【机构专属】

- **选定曲目**: **PAST** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 历史感 / 深沉 / 修复
- **匹配理由**:
  - "PAST" 呼应 OPCW 的使命本质——把化学战的黑暗过去封存为国际法禁忌
  - 深沉的历史感匹配核查与销毁这份不显眼但持续的制度工程
- **本地路径**: `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → `presentations/21th_century/Organisation_for_the_Prohibition_of_Chemical_Weapons/PAST.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Organisation_for_the_Prohibition_of_Chemical_Weapons/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/21th_century/Organisation_for_the_Prohibition_of_Chemical_Weapons/images.txt` | 总部与插图 URL |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Organisation_for_the_Prohibition_of_Chemical_Weapons.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
