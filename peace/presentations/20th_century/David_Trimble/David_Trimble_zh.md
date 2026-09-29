# 和平奖得主立传提示词（OpenPeace · David Trimble）

> **本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」**，以 David Trimble（1998 诺贝尔和平奖，北爱尔兰首任首席部长）为实例。
> 结构对齐物理学家侧标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库）。
- **本实例**：William David Trimble, Baron Trimble（大卫·特林布尔）。
- **设计哲学**：和平奖得主立传必须有「身份信息页」，且强调「事业领域」的结构化表达——模板骨架务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：David Trimble（1944-10-15 ~ 2022-07-25，享年 77 岁）
- **获奖**：1998 诺贝尔和平奖（与 John Hume 共享），官方获奖理由：
  > "for their efforts to find a peaceful solution to the conflict in Northern Ireland."
  > （中译照抄名录：表彰他们为和平解决北爱尔兰冲突所做的努力）
- **气质关键词**：**转型的阿尔斯特联合主义者、法学家出身的技术型领袖、争议与妥协的承载者**
- **设计母题**：**天平与航向（balance & course change）**。Trimble 的生涯是从强硬起点（Vanguard、Drumcree）转向签署并捍卫耶稣受难日协议的转向轨迹——用天平/罗盘的视觉母题表达「在联合主义传统内部为协议赢得多数」的政治平衡术。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/David_Trimble/page.md`（Wikipedia 全文 + frontmatter，事实基准唯一来源）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - OpenPeace 项目首页：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，第一轮已核对】

- **生卒**：1944-10-15 生于贝尔法斯特惠灵顿公园疗养院 ~ 2022-07-25 逝于北爱尔兰唐郡邓唐纳德（Dundonald）阿尔斯特医院（社区获得性肺炎；2021 确诊混合型失智、2022 年初确诊肺癌），享年 77 岁。
- **国籍**：United Kingdom（北爱尔兰）。
- **家庭**：父 William、母 Ivy Trimble，下中产阶级长老会家庭，住唐郡班戈；祖父 George 生于斯莱戈郡伊斯基。1968 与 Heather McComb 结婚（双胞胎早产夭折，1976 离异）；1978-08-31 与曾任其学生的 Daphne Elizabeth Orr 结婚，育二子二女（Richard、Victoria、Nicholas、Sarah）；女儿 Vicky 2017 年在苏格兰与同性结婚，2019 年 Trimble 在上议院公开表示因此改变对同性婚姻的立场。
- **教育**：Bangor Grammar School（1956–1963）；Queen's University Belfast（1964–1968），获法理学 McKane Medal，一级荣誉法学士（LL.B，三年内女王大学首个一级荣誉）。
- **任职**：1969 取得出庭律师资格；1969 起任 QUB 法学讲师，1973–1975 法学院助理院长，1977 高级讲师，1981–1989 商法与财产法主任；1990 当选上班纳议员后辞去教职。政党轨迹：Vanguard Unionist Progressive Party（1973–1978，曾任 Bill Craig 副手之一）→ UUP（1978–2007，1990 党法律委员会主席等）→ 保守党（2007–）。UUP 第 12 任领袖（1995-09-08 ~ 2005-07-24）；北爱首任首席部长（1998-07-01 ~ 2002-10-14，任期多次中断）；上议院终身贵族 Baron Trimble of Lisnagarvey（2006-06-02 册封）。
- **关键荣誉**：Nobel Peace Prize 1998（共同得主）；枢密院顾问官（1998 新年授勋）；法国荣誉军团军官勋位（1999-12-08 巴黎授勋）；Golden Plate Award 2002。
- **核心事业清单**：① 法学教育与学术生涯（QUB 二十年）；② 1970 年代 Vanguard 时期的联合主义政治（1974 UWC 大罢工法律顾问）；③ 1995 意外当选 UUP 领袖（Drumcree 游行角色之后）；④ 1997-1998 全党谈判 UUP 代表团团长、促成耶稣受难日协议；⑤ 首任首席部长：在 IRA 解除武装僵局中反复维系权力共享行政当局；⑥ 协议后政治：贵族院议员、加入保守党。
- **关键时间线（16 节点）**：1944 生于贝尔法斯特 → 1963 班戈文法学校毕业 → 1968 QUB 一级荣誉法学士 → 1969 取得律师资格、任 QUB 讲师 → 1973 Vanguard 竞选北 Down 落败 → 1974 UWC 大罢工法律顾问（反对 Sunningdale）→ 1975 入选北爱制宪会议（贝尔法斯特南）→ 1978 加入 UUP → 1990-05 上班纳补选进入下议院 → 1995-09-08 意外当选 UUP 领袖 → 1997 成为一个世纪以来首位同意与新芬党谈判的联合主义领袖 → 1998-04-10 签署耶稣受难日协议、5 月公投 71% 赞成 → 1998-07-01 就任首任首席部长、10 月获诺贝尔和平奖 → 2001-07-01 因解除武装僵局辞职、11-05 重新当选 → 2002-10-14 议会遭 suspending（Stormontgate 风波）→ 2005 大选失利辞党魁 → 2006 入上议院、2007 加入保守党 → 2022-07-25 逝世。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | politics | 政治 | UUP 领袖、下议院/上议院/北爱议会 | 身份页 |
| 1 | peace process | 和平进程 | 耶稣受难日协议谈判与捍卫，1998 诺奖核心 | 核心页 |
| 2 | law | 法学 | QUB 法学讲师、出庭律师 | 早年页 |
| 3 | conflict resolution | 冲突解决 | 说服联合主义阵营接受权力共享 | 核心页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方（name_en） | 方向 | note |
|---------|------|------|------|
| co-honored | John Hume | 无向 | 1998 诺贝尔和平奖共同得主 |
| spouse | Heather McComb | 无向 | 1968 结婚，1976 离异 |
| spouse | Daphne Orr | 无向 | 1978 结婚，曾任 QUB 学生 |
| colleague | Seamus Mallon | 无向 | 权力共享行政当局副首席部长同僚 |
| colleague | George Mitchell | 无向 | 全党谈判主席，后主持解除武装委员会 |
| colleague | John Taylor | 无向 | UUP 副领袖，1995 领袖选举对手 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：坚毅、转向、承载争议
- **配色**：主色斯坦福红 `#8C1515`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` 和平进程 — 深青 `#0E7490`
  - `badgeB` 政治 — 靛蓝 `#4C5FD5`
  - `badgeC` 法学 — 琥珀 `#E07B30`
  - `badgeD` 冲突解决 — 青绿 `#0E7C7B`
- **背景母题**：天平与罗盘线条（呼应「天平与航向」母题）。

### 第 6 步：规划幻灯片序列 【人物专属，13 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 北爱尔兰首任首席部长 / David Trimble 1944–2022 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、出生地、教育、任职、荣誉、核心领域）
03  早年与法学之路 (1944–1969) — 班戈、QUB 一级荣誉、出庭律师
04  QUB 讲师岁月 (1969–1990) — 商法主任、Edgar Graham 事件、1994 暗杀预警
05  Vanguard 时期 (1973–1978) — 1974 UWC 大罢工法律顾问、制宪会议
06  意外当选 UUP 领袖 (1995) — Drumcree、击败 Taylor
07  从对抗到谈判 (1995–1998) — 与都柏林会面、同意与新芬党同席
08  耶稣受难日协议 (1998) — 全党谈判、公投 71%、说服本党
09  首任首席部长 (1998–2002) — 解除武装僵局、三次中断、连任
10  协议之后的争议 — Bloody Sunday 调查异议、Stormontgate
11  诺奖与荣誉 — 1998 共同得主、Legion d'Honneur 1999、Golden Plate 2002
12  晚年 — 上议院、保守党、Turkel 委员会观察员、2022 逝世
13  结尾
```

### 第 7 步：版式要点 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照标杆 `\profileslide`。
- 每写完一页 `make` 编译，`pdftoppm` 截图检查溢出；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距。

### 第 8 步：专属陷阱表 【人物专属，红线】

| 陷阱 | 说明 |
|------|------|
| 政治敏感红线 | 北爱冲突、准军事组织关联（Vanguard/UDU 等）一律按 page.md 客观记录，禁评价；Drumcree 争议只写事实两面（天主教徒视为冒犯、新教徒视为捍卫） |
| 共享奖措辞 | 1998 与 Hume 共享，理由主语是 "their efforts"；诺奖研究所引 his "political courage" 授奖词可原文引用 |
| 与 Adams 关系 | page.md 明载八个月谈判中「从未与 Adams 直接交谈」——禁建 colleague 关系、禁写成合作者 |
| Vanguard 定性 | page.md 用 "paramilitary-linked" 定性 Vanguard，保留原文限定语，勿简化为普通政党 |
| 首席部长中断 | 2000-02~05 职位暂停、2001-07 辞职 11 月复职（注：2001-07~11 由 Reg Empey 代理）、2002-10 起议会暂停——三条勿混 |
| 婚姻两段 | 首婚 Heather McComb 1968-09-06（唐纳迪教堂）、1976 离异、双胞胎夭折；次婚 Daphne Orr 1978-08-31；子女 Richard/Victoria/Nicholas/Sarah |
| 转折表述 | 从 1974 反对 Sunningdale 的法律顾问到 1998 捍卫协议，是 page.md 明载的轨迹，勿写成「一贯温和派」 |
| 生卒日期 | 1944-10-15 / 2022-07-25（邓唐纳德），享年 77；死因社区获得性肺炎（2021 失智+2022 肺癌背景） |
| 同名区分 | 全名 William David Trimble；Baron Trimble of Lisnagarvey（2006）；勿与 David Simpson（2005 击败者）混淆 |
| 无师承 | 无博士导师记载（LL.B 后任教），禁编造「博士/导师」 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Ulster Unionist Party (UUP) | 阿尔斯特联合党 | 第 12 任领袖 |
| First Minister | 首席部长 | 北爱首任，勿译「第一部长」 |
| Good Friday Agreement | 耶稣受难日协议 | 全篇统一，与 Hume 篇一致 |
| Vanguard | 先锋派联盟党 | paramilitary-linked 限定语保留 |
| Drumcree conflict | 德拉姆克里冲突 | 1995 游行角色 |
| decommissioning | 解除武装 | 僵局核心议题 |
| Stormontgate | 斯托蒙特门事件 | 2002 议会暂停导火索 |
| Ulster Workers' Council strike | 阿尔斯特工人委员会大罢工 | 1974，推翻 Sunningdale |
| life peerage | 终身贵族 | Baron Trimble of Lisnagarvey |
| Bloody Sunday Inquiry | 血色星期日调查 | 1998 宣布、2010 Saville 报告 |
| Privy Council | 枢密院 | 1998 新年授勋 |
| Légion d'Honneur | 荣誉军团勋章 | 1999-12-08 军官勋位 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions（manifest 预分配，勿改）
- **匹配理由**: 「海」的辽阔与暗涌匹配 Trimble 的生涯——在联合主义阵营的惊涛中为协议掌舵，三度中断仍复任；终章沉静呼应晚年淡出与 2022 谢幕。
- **本地路径**: `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` → 复制为 `presentations/20th_century/David_Trimble/SEA.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/David_Trimble/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/David_Trimble.yaml` | 社会关系/领域入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
