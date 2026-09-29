# 诺贝尔和平奖得主立传提示词（International Labour Organization，1969）

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库）。
- **本篇对象**：国际劳工组织 International Labour Organization（ILO），1969 年诺贝尔和平奖得主，**本篇是组织机构条目（is_org=true）**。
- **设计哲学**：机构立传做"使命叙事"——1919 年《凡尔赛条约》第十三编诞生的劳工立法机器，以"劳动不是商品"为贯穿母题；第 6 步用「机构概览页」替代人物身份信息页。

## 二、背景信息 【人物专属】

- **机构全称**：International Labour Organization（ILO），中文：国际劳工组织；联合国专门机构，总部瑞士日内瓦
- **成立**：1919-04-11（infobox Formation 明载"11 April 1919"；正文另有"Founded in October 1919"一说——**取 infobox/条约通过的 1919-04-11，正文 October 口径禁用**）；1946 年成为联合国体系首个专门机构
- **1969 年诺贝尔和平奖，官方获奖理由（EN 原文照抄 Nobel 名录，禁止改写）**：
  > "for creating international legislation insuring certain norms for working conditions in every country."
  > 中译（照抄 `OpenPeace_20th_Century_Nobel_Laureates.md`）：表彰其创建国际劳工立法，保障各国劳动条件的特定标准
- **气质关键词**：**劳工立法的国际先驱、三方协商的独特机制、劳动不是商品**
- **设计母题**：**三方圆桌（tripartite table）**——政府/雇主/工人三角结构、章程条文、日内瓦总部建筑，视觉语言用三足鼎立的几何图形与劳工之手。
- **本地数据源**：`peace/presentations/pages/20th_century/International_Labour_Organization/page.md`

## 三、任务流程

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 成立：1919-04-11，《凡尔赛条约》第 427 条（Part XIII）确立；首年会 1919-10-29 于华盛顿泛美联盟大厦召开，通过头六项公约
- 性质：UN specialized agency；187 个成员国（193 个联合国成员国中的 186 个 + 库克群岛）；员工约 3,381–3,491（107 国）
- 治理：独特的三方结构（政府/雇主/工人）；三主体 = 国际劳工大会（ILC，"国际劳工议会"）/ 理事会（Governing Body，56 名 titular）/ 国际劳工局（秘书处）
- 首任总干事：Albert Thomas（法国社会主义者，1919–1932）；1969 年获奖时任总干事 David A. Morse（1948–1970）
- 里程碑：1944-05-10《费城宣言》——"labour is not a commodity"原则；1946 宪章修订并入费城宣言、成为 UN 首个专门机构；1998《工作中基本原则和权利宣言》四项基本政策
- 关键荣誉：Nobel Peace Prize 1969；Hans Böckler Preis
- 核心事业清单：①国际劳工标准（193 项公约，截至 2026）②童工消除（IPEC 1992）③强迫劳动消除（1930 公约/2014 议定书）④最低工资立法 ⑤劳工统计（KILM、SDG 8 九项指标托管机构）⑥移民工人与家务工权利
- 关键时间线（15–20 节点）：1900 IALL（国际劳工立法协会）成立（前史）→ 1918 Whitley 委员会报告/国际工联 Bern 会议 → 1919-02 劳工立法委员会首会（Gompers 当选主席）→ 1919-03-04 委员会终报 → 1919-04-11 和会通过、成《凡尔赛条约》第十三编 → 1919-10-29 首届 ILC 华盛顿，通过六项公约 → 1919 Albert Thomas 出任首任总干事 → 1920 迁驻日内瓦 → 1926 Centre William Rappard 启用 → 1934-08-20 美国加入（不入国联）→ 1940 战时迁麦吉尔大学（蒙特利尔，至 1948）→ 1944-05-10《费城宣言》→ 1946 成为联合国体系首个专门机构 → 1948–1970 David A. Morse 任总干事 → 1969 诺贝尔和平奖 → 1975-1977 美国退出（PLO 观察员席位争议）、1980 回归 → 1992 IPEC 创立 → 1998《工作中基本原则和权利宣言》→ 2002 世界反对童工日设立 → 2011 家务工公约 → 2019 百年宣言/全球未来工作委员会 → 2022 Gilbert Houngbo 当选（首位非洲籍总干事）

### 第 4 步：使命领域梳理 + 入库 【与 yaml fields 完全一致】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | international labour standards | 国际劳工标准 | 193 项公约体系，1969 诺奖核心 |
| 1 | international labour law | 国际劳动法 | 凡尔赛条约第十三编以来的立法传统 |
| 2 | decent work | 体面劳动 | 自由、公平、安全、有尊严的工作 |
| 3 | social justice | 社会公正 | 机构使命：以社会正义推进和平 |
| 4 | child labour elimination | 消除童工 | IPEC 1992、第 138/182 号公约 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml relations 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Samuel Gompers | 无向 | 1919 劳工立法委员会主席，主持起草 ILO 章程条款 |
| colleague | Albert Thomas | 无向 | 首任总干事（1919–1932） |
| colleague | David A. Morse | 无向 | 任内（1948–1970）获 1969 诺贝尔和平奖 |
| other | League of Nations | 无向 | 1919 年依《凡尔赛条约》在国际联盟下成立 |
| other | United Nations | 无向 | 1946 年成为联合国体系首个专门机构 |

- 入库规则：org 条目无 gender/nationalities；总干事名录中其余人员（Butler/Phelan/Jenks 等）page.md 仅列表载明、关系不紧密，**不入库**；`type: other` 用于国联前身与联合国隶属（工作流第 2 节）。

### 第 5 步：设计配色方案 【manifest 预分配，勿改主色】

- **主色**：`#17435B`（深青蓝——日内瓦与国际官僚机构的稳重）
- **辅助**：诺奖香槟金 `#C9A227` + 四分类色：
  - badgeA 劳工标准 — 钢蓝 `#3A7CA5`
  - badgeB 三方协商 — 琥珀 `#E07B30`
  - badgeC 社会正义 — 橄榄绿 `#6A8532`
  - badgeD 童工消除 — 玫瑰 `#C4204F`
- **背景母题**：三足圆环（三方结构）+ 柔和圆点。

### 第 6 步：幻灯片序列（10–16 页规划）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 国际劳工组织 / ILO · 1969 诺贝尔和平奖 + 四色 badge + 机构徽记位
02  机构概览页（★ 替代身份信息页）— 成立/总部/性质/成员/三方结构/使命六格
03  使命概览 — 劳工标准 / 劳动法 / 体面劳动 / 社会正义 / 童工消除
04  缘起：从凡尔赛到华盛顿 (1919) — 第十三编、劳工立法委员会、首届 ILC
05  章程的诞生 — Gompers 主席、十项美国提案与三条国际增补
06  首任总干事 Albert Thomas 与战间期 (1919–1938)
07  机构概览：三方治理 — ILC / Governing Body / 国际劳工局
08  战时与重建：麦吉尔岁月与费城宣言 (1940–1946) — "labour is not a commodity"
09  联合国时代的扩张 — Morse 任期、发展中国家成员、技术合作
10  1969 诺贝尔和平奖 — 官方理由原文 + 中译
11  危机与调整 — 1975–1977 美国退出与回归（客观记录）
12  核心事业 — 193 项公约/1998 四项基本政策/IPEC
13  劳工统计与 SDG 8 — KILM、九项指标托管
14  遗产：一百年的劳动尊严
15  结尾
```

### 第 7 步：版式要点 【模板通用骨架 + 人物专属】

- 每页 `\newcommand{\xxxslide}{...}`；机构概览页参照成品 `\profileslide` 双栏信息网格实现。
- 配色宏统一 `mainclr/accentclr/badgeA..D/panelA..D`，注释写语义。
- 表格页安全负间距：顶部 -0.35cm、`arraystretch 0.78–0.82`。

### 第 8 步：本机构专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 成立日期 | 取 1919-04-11（infobox Formation + 条约通过日）；正文"Founded in October 1919"是首年会口径，**两说勿混** |
| 领导人≠创始人 | Albert Thomas 是首任总干事**非创始人**；Gompers 是章程起草委员会主席；page.md 未点名任何单一"创始人" |
| 1919 年份口径 | 章程 4 月成条约、首会 10 月开——写时间线时区分"条约通过"与"首次大会" |
| 费城宣言 | 1944-05-10；1946 年并入宪章，两年份勿混 |
| 卡塔尔争议 | 2014–2025 Qatar 相关争议（Qatargate、多哈迁址等）**整节政治/商业敏感，禁入正文**，只可时间线一句客观带过或不写 |
| 冷战内容 | 1975 PLO 观察员席位与美苏阵营冲突只作客观事实简述，禁评价 |
| 名录口径 | 名录 country 列 "International organization"，诺奖 citation 主语机构 |
| 无载禁写 | 具体公约批准国名单细节、总干事个人生平、现任领导人评价 page.md 未载一律不写 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险点 |
|------|------|------|
| International Labour Organization | 国际劳工组织 | 缩写 ILO |
| tripartite structure | 三方结构 | 政府/雇主/工人，ILO 独有 |
| International Labour Conference | 国际劳工大会 | "国际劳工议会"别称 |
| Governing Body | 理事会 | 执行机构，56 名 titular 成员 |
| Declaration of Philadelphia | 费城宣言 | 1944，"labour is not a commodity" |
| convention | 公约 | 与 recommendation（建议书）效力不同 |
| IPEC | 消除童工国际计划 | 1992 创立 |
| fundamental conventions | 基本公约 | 1998 宣言八项/四政策 |
| Treaty of Versailles Part XIII | 凡尔赛条约第十三编 | ILO 章程载体 |
| decent work | 体面劳动 | 机构核心纲领 |

---

## 四、背景音乐 ✅ 【manifest 预分配，勿改】

- **选定曲目**：**Lonesome** — AShamaluevMusic
- **匹配理由**："深沉/情感电影配乐" 匹配百年劳工史的温度——从战间期的理想主义到冷战的分裂与坚守，沉静克制的弦乐气质与机构"以立法护佑劳动者"的庄重叙事相称。
- **本地路径**：`music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/International_Labour_Organization/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

---

## 六、执行清单

1. 建 `peace/presentations/20th_century/International_Labour_Organization/` 目录 + `images/`；下载机构徽记/日内瓦总部照片（无 URL 则装饰圆占位，机构无肖像）。
2. 复制 Makefile，设 `MAIN=International_Labour_Organization_zh`、`VIDEO_NAME=International_Labour_Organization_zh`。
3. 按 §三 第 6 步序列写 tex；每写一页 make 检查溢出（vbox≤10pt、hbox≤50pt）。
4. `pdftoppm` 逐页目检 → make images/video。
5. yaml 入库：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/International_Labour_Organization.yaml`；验证 has_social_data=1。

---

## 七、版式补遗

- 机构条目封面无个人肖像：用机构徽记/三方圆环图形 + 装饰圆占位，图注写明"机构徽记位"。
- 结尾页底部品牌统一 `OpenMathAI`；引号用半角 `" "`。
- \foreach 时间线分隔符必须 ASCII 逗号；宏名禁数字。
