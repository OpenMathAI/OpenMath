# 和平奖得主立传提示词（OpenPeace：The Viscount Cecil of Chelwood）

> **本文件是 OpenPeace 项目的人物专属立传提示词**，以 Robert Cecil, 1st Viscount Cecil of Chelwood（1937 诺贝尔和平奖，国际联盟的设计师与捍卫者）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节 + 第 0–9 步）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenPhysicist / OpenMedic 同属 OpenMathAI 共享仓库）。
- **模板来源**：综合物理学家标杆（Kenneth G. Wilson 提示词 + Beamer 结构）与医学/化学侧批量立传经验。
- **本实例**：Edgar Algernon Robert Gascoyne-Cecil, 1st Viscount Cecil of Chelwood（塞西尔子爵），国联设计师、国联协会会长。
- **设计哲学**：和平奖得主立传的核心骨架是「身份信息页 + 结构化事业领域」；建制派和平家（律师/贵族/阁员）的主线是「法律—战争内阁—国联设计—民间动员」，务必保留身份信息页。

---

## 二、背景信息 【人物专属】

- **目标人物**：Edgar Algernon Robert Gascoyne-Cecil, 1st Viscount Cecil of Chelwood, CH, PC, QC（1864-09-14 ~ 1958-11-24，享年 94 岁）；1868–1923 称 Lord Robert Cecil
- **气质关键词**：**国联的设计师、裁军的终身倡导者、自由贸易的托利党人** —— 1937 诺贝尔和平奖获奖理由：
  > "for his tireless effort in support of the League of Nations, disarmament and peace."（表彰他为支持国际联盟、裁军与和平所做的不倦努力）
- **设计母题**：**圆桌的蓝图（the covenant blueprint）**。其一生围绕「把大国围到圆桌前、用公约与制裁约束战争」——备忘录、盟约草案、国联协会民间动员；视觉上可用「圆桌/蓝图线稿/🕊 纸鸢」呼应（不用 emoji，用线稿图形）。
- **本地 Wikipedia**：`peace/presentations/pages/20th_century/Robert_Cecil_1st_Viscount_Cecil_of_Chelwood/page.md`（含 frontmatter QID Q12702 与 infobox）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）
  - 名录（官方理由照抄源）：`peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（据本地 page.md，无载禁写） 【人物专属】

- 生卒：1864-09-14 生于伦敦 Cavendish Square ~ 1958-11-24 逝于东 Sussex 郡 Danehill 的 Chelwood Gate 自宅，享年 94 岁；无嗣，子爵爵位断绝
- 国籍：英国（United Kingdom）；政党：保守党（1921 曾辞党鞭）
- 家庭：索尔兹伯里侯爵三世家 Robert Gascoyne-Cecil（三任首相）与 Georgina Alderson 之第六子第三子；兄 James（第四代侯爵）、Lord William Cecil（主教）、Lord Edward Cecil、Lord Quickswood；表亲 Arthur Balfour；1889-01-22 娶 Lady Eleanor Lambton（Durham 第二代伯爵 George Lambton 之女），自称此婚是其「平生最聪明的一件事」
- 教育：家庭教育至 13 岁 → Eton 四年 → 牛津 University College 攻法律（知名辩手）
- 法律生涯：1886–88 任首相父亲私人秘书；1887 Inner Temple 取得律师资格；1887–1906 执业民法（Chancery 与议会实务）；1899-06-15 御用大律师（QC）；合著 Principles of Commercial Law；1910 出任 General Council of the Bar 成员、Inner Temple Bencher；治安法官、1911 起 Hertfordshire 季度法庭主席
- 议会：1906–10 Marylebone East 保守党议员（自由贸易派，反对 Joseph Chamberlain 关税改革）；1910 两次大选落败（Blackburn/Wisbech）；1911 Hitchin 补选（独立保守党）议员至 1923；1923-12-28 受封 Viscount Cecil of Chelwood 入上院
- 战时任职：一战先在红十字会；1915-05-30 外交部政务次官；1915-06-16 入枢密院；1916-02-23~1918-07-18 封锁大臣（Minister of Blockade）；1919 获牛津荣誉院士+MA+荣誉民法博士
- 关键荣誉：Nobel Peace Prize 1937（1938-06-01 发表诺奖演讲 The Future of Civilization）；Companion of Honour 1956；伯明翰大学校监 1918–44；Aberdeen 大学学监 1924–27；Woodrow Wilson 基金会和平奖 1924
- 核心事业清单（4–6 条）：
  1. 1916-09《关于减少未来战争诱因的备忘录》——其自称「英国官方倡导国联的第一份文件」
  2. 1917《维护未来和平的建议》与 Phillimore 委员会推动（1918-05 将报告转交 Wilson 与豪斯上校）
  3. 巴黎和会国联盟委员会：与 David Hunter Miller 共拟 Cecil–Miller 草案；捍卫英国草案要素
  4. 国联协会（League of Nations Union）会长 1923–1945——民间动员、扩大保守与工党支持
  5. 1923 互助条约草案、1925 鸦片会议英国代表团长、1927 为日内瓦海军会议辞职（巡洋舰数量之争）
  6. 1930s：世界裁军会议批评政府、与 Pierre Cot 共同创立国际和平运动（Rassemblement universel pour la paix）、批评慕尼黑协定；1946 国联末次会议致辞「国联已死，联合国万岁！」
- 关键时间线（15–20 节点）：1864 出生 → 1887 律师资格 → 1889 结婚 → 1899 QC → 1906 议员 → 1911 Hitchin → 1915 外交部次官 → 1916 封锁大臣 → 1916-09 国联备忘录 → 1918 Phillimore 报告转交 → 1919 巴黎和会盟约谈判 → 1919-11 辞去政府职务 → 1920–22 代表南非出席国联大会 → 1923 子爵+枢密院长 → 1924–27 兰开斯特公爵郡大臣 → 1927 海军会议辞职 → 1929 行人协会会长 → 1932–33 裁军会议论战 → 1935 阿比西尼亚危机中的国联动员 → 1937 诺奖 → 1938 诺奖演讲 → 1946 国联谢幕致辞 → 1953 上院末次演讲 → 1958 去世

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

**Cecil 的事业领域（按 rank 排序，已入库 person_field，与 yaml fields 一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international organization | 国际组织建设 | 国联设计与捍卫，诺奖理由核心 | 国联页 |
| 1 | collective security | 集体安全 | 盟约、制裁与互助条约草案 | 备忘录页 |
| 2 | disarmament | 裁军 | 裁军会议与海军会议 | 裁军页 |
| 3 | diplomacy | 外交 | 战时与战后的外交任职 | 阁员页 |
| 4 | law | 法律实务 | QC、民法与议会实务 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 与 `MySQL/data/Robert_Cecil_1st_Viscount_Cecil_of_Chelwood.yaml` 完全一致；只收 page.md 明载关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Lady Eleanor Lambton | 无向 | 1889 结婚 |
| parent-child | Robert Gascoyne-Cecil, 3rd Marquess of Salisbury | 父→子 | 父亲，三任英国首相 |
| parent-child | Georgina Alderson | 父→子 | 母亲 |
| colleague | Arthur Balfour | 无向 | 表亲，1905 为其起草关税备忘录、1917 经其批准设国联委员会 |
| colleague | Woodrow Wilson | 无向 | 巴黎和会国联盟委员会共事、共同起草盟约 |
| colleague | David Hunter Miller | 无向 | 1919 共拟 Cecil–Miller 草案 |
| colleague | Gilbert Murray | 无向 | 国联事业共事，多次通信 |
| colleague | Pierre Cot | 无向 | 共同创立国际和平运动并任双主席 |
| controversy | Maurice Hankey | 无向 | Hankey 批评国联构想并称其为 crank，Cecil 批评其 Hankeyism |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：庄重、执着、蓝图感
- **配色**：深松绿（贵族与律政的沉稳，manifest 预分配 `#1E4D3B`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeCovenant` 国联蓝图 — 靛蓝 `#4C5FD5`
  - `badgeBlockade` 战时封锁 — 玫瑰 `#C4204F`
  - `badgeUnion` 国联协会 — 琥珀 `#E07B30`
  - `badgeBar` 律政生涯 — 青绿 `#0E7C7B`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），以「圆桌座席的圆」呼应圆桌母题

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover 共享封面）
01  封面 — 国联的设计师 / The Viscount Cecil of Chelwood 1864–1958 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、本名、国籍、教育、任职、荣誉、核心领域）
03  核心事业概览 — 国联蓝图 / 战时封锁 / 国联协会 / 裁军论战
04  早年与律政生涯 (1864–1906) — 索尔兹伯里之子、Eton、牛津、Inner Temple、QC
05  自由贸易的托利党人 (1906–1914) — Marylebone East、反关税改革、Hitchin 补选
06  战时任职 (1914–1919) — 红十字会、外交部次官、封锁大臣
07  国联备忘录（核心页）— 1916-09 备忘录、1917 建议、Phillimore 委员会
08  巴黎和会与盟约（核心页）— Wilson 草案批评、Cecil–Miller 草案、豪斯的告诫
09  国联协会岁月 (1920–1927) — 会长 1923–45、南非代表、世界语提案、1927 辞职
10  裁军论战 (1931–1936) — 满洲危机、Hankeyism、阿比西尼亚、Hoare–Laval
11  1937 诺贝尔和平奖 — 获奖理由、1938 演讲 The Future of Civilization
12  慕尼黑与国联谢幕 — 1938 批评慕尼黑、1946「国联已死，联合国万岁！」、联合国协会终身荣誉会长
13  家人与身后 — 无嗣爵位断绝、上院悼词、荣誉学位与 CH 1956
14  遗产：圆桌上的和平蓝图
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照物理学家标杆 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用标杆 tex 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Cecil 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名称谓 | 全名 Edgar Algernon Robert Gascoyne-Cecil；1868–1923 称 Lord Robert Cecil（幼子礼称非贵族）；1923-12-28 起为 Viscount Cecil of Chelwood——三个称谓勿混用；正文统一用 Robert Cecil / Cecil |
| Lord Privy Seal 卸任日 | infobox 作 1924-01-22、正文作 1924-02-22——两说并存，正文取 infobox 并加注 |
| 子爵受封日 | London Gazette 1923-12-28、Burke's Peerage 作 12-24——取 Gazette 口径加注 |
| 国联归因 | Cecil 是国联的设计师**之一**（Egerton 评价限于盟约第二阶段工作）；勿写成「独自发明国联」，Wilson/Phillimore 等人贡献勿吞 |
| 备忘录地位 | 「英国官方倡导国联的第一份文件」是 Cecil 自评原话，可引用但注明是其自述 |
| 慕尼黑批评 | 引语（Khartoum 类比、Guardian 信件）page.md 载原文可选段；历史评价保持客观叙述 |
| 晚年政论 | 1953 上院演讲涉意识形态论断（反 dialectical materialism 等）——只作演讲内容客观转述，勿作评价性展开 |
| 拒绝入自由党 | 因 Asquith 在位而拒绝——勿写成「加入工党」；1935 曾考虑加入 Labour 但仅是 contemplated |
| 无载禁写 | 无博士导师/门生；与 Colonel House、Eyre Crowe 是文献中的互动勿建关系；Pedestrians Association（1929 会长）是机构非关系 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| League of Nations | 国际联盟 | 勿简称「国联」于首次出现 |
| Covenant of the League of Nations | 《国际联盟盟约》 | 条约文本名 |
| League of Nations Union | 国际联盟协会 | 民间团体≠国联本体 |
| Minister of Blockade | 封锁大臣 | 战时经济战职位 |
| Cecil–Miller draft | Cecil–Miller 草案 | 1919 与 Miller 共拟 |
| collective security | 集体安全 | 核心理念词 |
| Tariff Reform | 关税改革运动 | Joseph Chamberlain 主张 |
| Queen's Counsel | 御用大律师（QC） | 1899 |
| Rassemblement universel pour la paix | 世界和平集会（国际和平运动法文名） | 与 Pierre Cot 共创 |
| Esperanto | 世界语 | 1921 提案 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Nostalgy** — AShamaluevMusic（manifest 预分配，勿改）
- **风格**: 怀旧 / 忧郁 / 纪录片
- **匹配理由**:
  - 「怀旧」匹配其一生底色——为一个未能阻止二战的理想组织奋斗四十年
  - 「纪录片」匹配长跨度叙事——从 1916 备忘录到 1946 国联谢幕，蓝图与幻灭的双线
- **本地路径**: `music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav`
- **时长**: 以 ffmpeg `-shortest` 对齐视频长度

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Robert_Cecil_1st_Viscount_Cecil_of_Chelwood/page.md` | 本地 Wikipedia 正文（唯一事实源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/Robert_Cecil_1st_Viscount_Cecil_of_Chelwood.yaml` | 入库数据（fields/relations 与本文件一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
