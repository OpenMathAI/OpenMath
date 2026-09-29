# 和平奖得主立传提示词（OpenPeace 实例：Joseph Rotblat）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」实例**，以 Joseph Rotblat（1995 诺贝尔和平奖，与帕格沃什会议共同获奖）为对象。
> 凡标注 `【模板通用】` 的部分复用 OpenPeace 共享骨架；标注 `【人物专属】` 的部分为本人物专属内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 各学科侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：对齐物理学家侧标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` 的 0–11 节结构。
- **本实例**：Joseph Rotblat（约瑟夫·罗特布拉特），波兰裔英国物理学家、唯一在曼哈顿计划中途因良知退出的科学家、帕格沃什会议缔造者。
- **设计哲学**：和平奖得主立传必须有「身份信息页」与「和平事业结构化表达」；科学家和平主义者立传强调**科学与良知的关系叙事**——核物理出身与核裁军事业的张力只按事实呈现。

---

## 二、背景信息 【人物专属】

- **目标人物**：Joseph Rotblat（1908-11-04 ~ 2005-08-31，享年 96 岁）
- **气质关键词**：**退出原子弹的人、帕格沃什的缔造者、科学家的希波克拉底誓言** —— 1995 诺贝尔和平奖获奖理由（与 Pugwash Conferences 共享）：
  > "for efforts to diminish the part played by nuclear arms in international affairs and, in the longer run, to eliminate such arms"（表彰他们为削弱核武器在国际政治中的作用、并在长远上消除核武器所做的努力）
- **设计母题**：**半途而返者与观测之光**。1944 年走出洛斯阿拉莫斯、1955 年罗素-爱因斯坦宣言最年轻的签署者——视觉语言用回折的轨迹线、放射性衰变曲线化为鸽群、伦敦帕格沃什讲台。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Joseph_Rotblat/page.md`（含 frontmatter QID Q219982）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - OpenPeace 共享封面：`peace/presentations/cover/openpeace_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇到歧义先征求主控意见再继续。
> **数据库同步要求**：包含「和平事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1908-11-04 生于华沙（时属俄国统治下的波兰会议王国）~ 2005-08-31 逝于伦敦 Royal Free 医院（败血症，享年 96）
- 本名：Józef Rotblat（波兰语名）；波兰犹太家庭，七子之二夭折；父 Zygmunt 经营全国马车行，一战后破产
- 教育：cheder 私塾与技工学校（电工学，1923 文凭）→ 自由波兰大学（1929-01 考试，物理轻松通过）→ 1932 MA → 华沙大学 1938 物理学博士 → 利物浦大学 PhD 1950（论文《Determination of a number of neutrons emitted from a source》）
- 师承与引荐人：Ludwik Wertenstein（自由波兰大学理学院长，师承居里夫人与卢瑟福，录取 Rotblat 并引荐）；博士导师 James Chadwick（利物浦，1932 诺奖·中子发现者）
- 家庭：妻子 Tola Gryn（1930 夏令营相识的文学学生；1939 病留华沙，1942 死于 Belzec 集中营，终未再婚）；1946-01-08 入籍英国
- 任职：华沙科学学会放射实验室研究员、自由波兰大学原子物理研究所副所长（1938）→ 利物浦大学（Oliver Lodge Fellowship）→ 1944-02 加入洛斯阿拉莫斯（Chadwick 英国使团；先在 Egon Bretscher 组、后在 Robert R. Wilson 回旋加速器组）→ 1944 年末以良知为由退出项目返利物浦 → 1949 St Bartholomew's 医院（Barts）物理学教授至 1976 荣休 → 爱丁堡大学 Montague 国际关系访问教授（1975–76）
- 关键荣誉：诺贝尔和平奖 1995（与帕格沃什会议共同）、CBE（1965）、FRS（1995）、KCMG（1998）、Albert Einstein Peace Prize（1992）、Jamnalal Bajaj Award（1999）、Polonia Restituta 勋章带星指挥官
- 核心事业清单：
  1. 战前波兰：核裂变释能微秒级计算（1939）；Nature 1939 论文《Emission of Neutrons accompanying the Fission of Uranium Nuclei》
  2. Tube Alloys 与曼哈顿计划（1939–1944）：以「威慑纳粹」为参与前提；1944-03 Chadwick 家晚宴闻 Groves「压制苏联」言论（1985 年回忆）；同年末确认德国 1942 已放弃核计划后以良知退出——史上唯一中途退出的曼哈顿计划科学家（page.md 口径为「on grounds of conscience」）
  3. 核沉降研究：1949 起 Barts 研究辐射生物效应（衰老与生育）；1955 Castle Bravo 比基尼沉降研究证明污染远超官方口径（钋-90/锶-90 口径按 page.md 实载为 strontium-90），推动 1963 部分禁止核试验条约批准
  4. 帕格沃什：1955 罗素-爱因斯坦宣言最年轻签署者并主持发布记者会；1957 与罗素等组织首届帕格沃什会议，任秘书长至 1973、后任主席；CND 执委（1958）
  5. 科学伦理：倡导「科学家的希波克拉底誓言」（1999 Science 论文）；SIPRI 共同创建者；1960–72 主编《Physics in Medicine and Biology》
  6. 1988–2004 每年提名 Mordechai Vanunu 诺贝尔和平奖
- 关键时间线（15–20 节点）：1908 生于华沙 → 1923 电工学徒 → 1929 入自由波兰大学 → 1932 MA → 1938 华沙大学博士 → 1939 赴利物浦 Chadwick 门下（Oliver Lodge Fellowship）→ 1939-08 离华沙（妻病留，战后死于 Belzec）→ 1939 Nature 论文 → 1944-02 洛斯阿拉莫斯 → 1944 末退出项目 → 1946 入籍英国 → 1949 Barts 教授 → 1950 利物浦 PhD → 1955 Castle Bravo 论文 + 罗素-爱因斯坦宣言签署 → 1957 首届帕格沃什会议 → 1958 CND 执委 → 1960–72 主编期刊 → 1965 CBE → 1973 前卸任帕格沃什秘书长 → 1976 Barts 荣休 → 1992 Einstein 和平奖 → 1995 FRS + 诺贝尔和平奖 → 1998 KCMG → 2004 中风 → 2005-08-31 逝世

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下确认 `Joseph_Rotblat/` 与 `images/` 存在

### 第 2 步：复制 Makefile 【模板通用】

- 复制同侧已有成品目录 Makefile，设置 `MAIN=Joseph_Rotblat_zh`、`VIDEO_NAME=Joseph_Rotblat_zh`

### 第 3 步：收集图片 【人物专属】

- infobox 肖像为 1944 洛斯阿拉莫斯证件照（images.txt 有 URL 则直接取，250px 改 500px）；备用插图：1957 帕格沃什会议历史照、1995 奥斯陆领奖照
- 404 则用 Wikipedia REST API page/summary 查 infobox 原图名，再不行用装饰圆占位

### 第 4 步：和平事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nuclear disarmament | 核裁军 | 帕格沃什会议、反核军备竞赛 | 封面、核心页 |
| 1 | nuclear physics | 核物理 | 裂变中子、回旋加速器研究 | 学术页 |
| 2 | medical physics | 医学物理 | Barts 辐射生物效应、核沉降研究 | Barts 页 |
| 3 | scientific ethics | 科学伦理 | 科学家希波克拉底誓言 | 伦理页 |
| 4 | peace research | 和平研究 | SIPRI 共同创建、东西方科学家对话 | 帕格沃什页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Tola Gryn | 无向 | 1939 前结婚，1942 死于 Belzec 集中营 |
| advisor-student | James Chadwick | 对方是导师 | 利物浦大学博士导师（1950 PhD），Tube Alloys 同事 |
| co-honored | Pugwash Conferences on Science and World Affairs | 无向 | 1995 诺贝尔和平奖共同得主 |
| colleague | Bertrand Russell | 无向 | 1955 宣言共同签署者，1957 共同组织首届帕格沃什会议 |
| colleague | Ludwik Wertenstein | 无向 | 自由波兰大学理学院长、录取并引荐人 |
| colleague | Stanisław Ulam | 无向 | 洛斯阿拉莫斯同侪波兰裔犹太科学家（库内规范名 Stanisław Ulam） |

### 第 5 步：设计配色方案 【人物专属，主色勿改】

- **主色**：深湖蓝 `#1B4D6B`（理性与深海般的克制）+ 诺奖香槟金 `C9A227`
- badgeA 核裁军 — 暗红 `#7E1E23`；badgeB 核物理 — 靛蓝 `#2F4470`；badgeC 医学物理 — 深青 `#175E54`；badgeD 科学伦理 — 赭金 `#B08D2E`
- **背景母题**：回折轨迹线与光点衰变（轨迹从核符号折向橄榄枝），帕格沃什圆桌光晕

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）与国籍行（底部状态栏 `国籍 | 机构 | 主要奖项` 三要素，国籍可写 Poland → United Kingdom）。
2. 必须有身份信息页（★ 必做）：左头像 + 右信息网格（生卒、本名、国籍、出生地、师承、任职、荣誉、核心事业）。
3. 结尾页品牌统一 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 退出原子弹的人 / Joseph Rotblat 1908–2005 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  和平事业概览 — 核裁军 / 核物理 / 医学物理 / 科学伦理 / 和平研究
04  早年：华沙 (1908–1939) — 贫困、电工学徒、Wertenstein 门下、1939 Nature 论文
05  利物浦与离别 (1939–1944) — Chadwick 门下、妻留华沙与 Belzec 集中营之殇
06  曼哈顿计划 (1944) — Tube Alloys、洛斯阿拉莫斯、Groves 晚宴回忆、良知退出
07  安全档案风波 — 指控与证伪（只述事实）
08  Barts 医学物理 (1949–1976) — 辐射生物效应、Castle Bravo 1955 论文
09  罗素-爱因斯坦宣言 (1955) — 最年轻签署者、主持发布记者会
10  帕格沃什（核心贡献页）— 1957 首届会议、秘书长 16 年、冷战东西方对话
11  政策影响 — 部分禁止核试验条约 (1963)、不扩散条约 (1968) 等铺路（page.md 口径）
12  科学家的希波克拉底誓言 — 1999 Science 论文、SIPRI、期刊主编
13  诺贝尔和平奖 1995 — 与帕格沃什共同、颁奖词、Remember your humanity 演讲结语
14  晚年与遗产 — Vanunu 提名 17 年、2004 中风、2005 逝世、伦敦纪念牌 (2017)
15  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 无载禁写 | 凡 page.md 未载的细节一律不写；不从颁奖词反推关系 |
| 引语白名单 | 仅可用 page.md 明载英文原句：Groves 晚宴语（1985 Rotblat 回忆，标明为回忆）、Foreign Office 官员评语句、宣言结语「Above all, remember your humanity」；引语不得改写 |
| 政治敏感红线 | 冷战、核武器、以色列核计划（Vanunu 事件）一律按 page.md 客观事实记录，不加评价性语句 |
| 「唯一退出者」 | page.md 口径是「left the Los Alamos Laboratory on grounds of conscience after it became clear to him in 1944 that Germany had ceased development」——写「以良知为由退出」，禁写「唯一」除非引 page.md 实载表述 |
| Groves 言论 | 1985 年 Rotblat 回忆口径；Bernstein 对记忆准确性存疑的评论也在 page.md——两说并陈，不采单侧 |
| 核沉降元素 | page.md 实载为 strontium-90（锶-90），勿误写钋-90；「钋」只用于 Arafat/死因语境 |
| 妻子之殇 | Tola Gryn 1942 死于 Belzec 集中营（Holocaust），1939 出走华沙时因病留下——客观一句，勿渲染；「never remarried」如实 |
| 帕格沃什职位 | 秘书长 1957–1973，后任主席（president）——两职勿混 |
| 共同获奖口径 | 1995 与 Pugwash 会议组织共享同一句理由（efforts...），对手方 name_en 用 manifest 全称 Pugwash Conferences on Science and World Affairs（批次 20 建组织记录） |
| Ulam 库名 | 库内有 Stanisław Ulam(354) 与 Stanislaw Ulam(658) 两条分裂 stub——本篇 yaml 用规范重音形式 Stanisław Ulam；分裂合并留主控处理 |
| 博士时间 | 华沙大学博士 1938 与利物浦 PhD 1950 两个学位并存，勿混 |
| 反对手方 | Niels Bohr（协助救妻未果的求助对象）、Egon Bretscher/Robert R. Wilson（课题组负责人）不建关系（非白名单关系类型载体） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Manhattan Project | 曼哈顿计划 | 1942–1946 |
| Tube Alloys | 管合金（英国原子弹计划） | 1941–46 代号 |
| British Mission | 英国使团 | Chadwick 率队赴洛斯阿拉莫斯 |
| nuclear fallout | 核沉降 | 1955 Castle Bravo 研究 |
| Partial Nuclear Test Ban Treaty | 部分禁止核试验条约 | 1963 |
| Russell–Einstein Manifesto | 罗素-爱因斯坦宣言 | 1955 |
| Pugwash Conferences | 帕格沃什会议 | 1957 首届 |
| Hippocratic Oath for scientists | 科学家希波克拉底誓言 | 1999 Science 论文 |
| St Bartholomew's Hospital | 圣巴塞洛缪医院（Barts） | 1949–1976 |
| CND | 核裁军运动 | 1958 入执委 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配勿改】

- **选定曲目**: **Falling Apart** — Michael FK & Andy Leech
- **风格**: 电影感 / 沉重 / 崩解与重构
- **匹配理由**: 「Falling Apart」呼应本篇的双重复——旧世界在战争中崩解（华沙沦陷、Belzec 集中营之殇）与一个科学家对核时代的良知断裂（1944 走出洛斯阿拉莫斯）；低回的弦乐也贴合 96 岁漫长一生的克制与悲悯
- **本地路径**: `music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Joseph_Rotblat/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。**

---

## 六、执行清单 【模板通用，逐项勾选】

- [ ] 第 0 步：通读 page.md 全文，核对本文件「事实基准」与正文一致（重点核对两个博士学位与帕格沃什两职任期）
- [ ] 第 1 步：确认目录 `Joseph_Rotblat/`（含 `images/`）存在
- [ ] 第 2 步：复制 Makefile，改 `MAIN` / `VIDEO_NAME` 为 `Joseph_Rotblat_zh`
- [ ] 第 3 步：下载肖像（1944 洛斯阿拉莫斯证件照）并 `file` 验证格式；404 则 REST API 查 infobox 原图名；再不行装饰圆占位
- [ ] 第 4 步：按领域表写入 `MySQL/data/Joseph_Rotblat.yaml` 的 `fields`（5 条，rank 0–4）
- [ ] 第 4.5 步：按社会关系表写入 yaml `relations`（6 条；Pugwash co-honored 对手方用 manifest 全称）
- [ ] 第 5 步：tex 头部宏定义配色（主色 #1B4D6B + C9A227 + badgeA–D 四分类色），宏名统一 `mainclr/accentclr/badgeA..D`，注释写语义
- [ ] 第 6 步：按幻灯片序列逐页定义 `\newcommand{\xxxslide}`（宏名禁数字、禁 `\u00b7`）
- [ ] 第 7 步：编译循环：`make distclean && make`（latexmk 多遍），0 error、vbox≤10pt、hbox≤50pt
- [ ] 第 8 步：`pdftoppm` 逐页目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标
- [ ] 第 9 步：史实审查（对照陷阱表逐条核，锶-90/钋之辨、两说并陈处核对）+ 术语审查（对照术语清单核译名）
- [ ] 收尾：`make pdf` 后核对页数与第 6 步规划一致；`make images && make video` 出 mp4

---

## 七、版式补遗 【模板通用，OpenPeace 沉淀】

- 表格页安全负间距：顶部 −0.35cm、`arraystretch 0.78–0.82`、公式框前 −0.35~−0.55cm（条目多时 −0.45cm 起）
- honors 类页 itemize 用 `\itemsep −2.5pt + topsep 0 + arraystretch 0.58` + 顶部 −0.55cm 压 4 条目（−0.65cm 会遮副标题）
- `leg` 节点 `x=±5.4cm` 的固有 hbox 8–9pt 属模板继承，不需修；时间线 `\foreach` 分隔符必须 ASCII 逗号
- 96 年人生跨两个世纪与两次大战，时间线页建议按「波兰—利物浦—洛斯阿拉莫斯—Barts—帕格沃什—晚年」六段区块分色，防单行超宽
- Radioactive 衰变曲线作装饰时只取示意形（无刻度、无数据），避免与真实数据混淆

---

## 八、入库回查清单 【模板通用】

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 -c "
from db_mysql import get_conn
conn=get_conn(); cur=conn.cursor()
cur.execute(\"SELECT id,name_en,has_social_data FROM people WHERE qid='Q219982'\")
p=cur.fetchone(); print(p)
cur.execute('SELECT COUNT(*) FROM person_field WHERE person_id=%s',(p[0],)); print('fields:',cur.fetchone()[0])
cur.execute('SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s',(p[0],p[0])); print('relations:',cur.fetchone()[0])"
```

- 预期：`has_social_data=1`、fields=5、relations=8（含既有 Chadwick/Powell/Pugwash 四行）；并发撞字典表唯一键（Duplicate entry）等 2 秒重跑一次（幂等）
