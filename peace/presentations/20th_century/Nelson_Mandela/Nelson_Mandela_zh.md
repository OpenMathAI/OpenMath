# OpenPeace 和平奖得主立传提示词（Nelson Mandela）

> **本文件是 OpenPeace 项目「诺贝尔和平奖得主 Beamer 立传」的人物专属提示词**。
> 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> ★ 政治敏感纪律：反种族隔离斗争内容（MK 武装、审判、入狱、谈判、总统任期）**按 page.md 明载事实客观记录**，
> 不加评价性语句、不引渲染性言论；"争议人物"两说并陈即可（page.md 明载），不展开定性。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（品牌口径统一写 `OpenMathAI`）。
- **本实例**：Nelson Rolihlahla Mandela（纳尔逊·曼德拉，1993 诺贝尔和平奖**与 F. W. de Klerk 共同获得**，1918-2013）。
- **设计哲学**：和平奖得主立传必须有「身份信息页」与「事业领域」结构化表达——这两点构成骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Nelson Rolihlahla Mandela（本名 Rolihlahla，1918-07-18 ~ 2013-12-05，享年 95 岁；科萨人，腾布王族，尊称 Madiba）
- **气质关键词**：**种族和解的践行者、27 年铁窗的坚守者、民主新南非的缔造者** —— 1993 诺贝尔和平奖官方获奖理由（与 de Klerk 共同）：
  > "for their work for the peaceful termination of the apartheid regime, and for laying the foundations for a new democratic South Africa."
  > 中译（照抄名录 `OpenPeace_20th_Century_Nobel_Laureates.md`）：表彰他们和平终结种族隔离制度的工作，以及为新民主南非奠定基础。
- **设计母题**：**长廊尽头的光（long walk to light）**。27 年囚禁到和解之门敞开——用门与光的渐变几何承载"漫长的自由之路"，贴合其自传 Long Walk to Freedom 的意象。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Nelson_Mandela/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- 生卒：1918-07-18 生于东开普 Mvezo（腾布王族）~ 2013-12-05 逝于约翰内斯堡，享年 95 岁；葬于 Qunu 家族墓地
- 家庭：三任妻子——Evelyn Mase（1944 结婚，1958 离异）、Winnie Madikizela-Mandela（1958 结婚，1992-04-13 公开分居，1996 离异）、Graça Machel（1998 结婚，莫桑比克活动家、前总统 Samora Machel 遗孀）；子女 6 人，具名者有 Makgatho Mandela、Makaziwe Mandela、Zenani Mandela-Dlamini、Zindziswa Mandela
- 教育：Fort Hare 大学（学习法律）、University of London、南非大学（UNISA）、Witwatersrand 大学；约翰内斯堡执业律师
- 从政轨迹：1943 加入 ANC；1944 参与创建 ANC 青年联盟；1952 抵制运动（Defiance Campaign）核心人物、任 ANC 德兰士瓦分部主席；1955 人民大会（Congress of the People）；1956 叛国罪审判（未定罪）；1961 参与创建武装组织 Umkhonto we Sizwe 并领导破坏行动；1962-08-05 被捕；Rivonia 审判（破坏与阴谋颠覆国家罪）判终身监禁
- 囚禁：共 27 年——Robben Island（1964-1982）、Pollsmoor Prison（1982-1988）、Victor Verster Prison（1988-1990）；狱中完成自传手稿
- 获释与谈判：1989-12 与 de Klerk 会面；1990-02 de Klerk 宣布无条件释放、解禁各政党；1990-02-11 步出 Victor Verster 监狱（全球直播）；1990 非洲多国与欧美访问（法、梵蒂冈、英、美等）；1990-05 Groot Schuur Minute、1990-08 Pretoria Minute（停火）；1991-07 当选 ANC 主席（接替 Tambo）；1991-12 起 CODESA 谈判；1993 临时宪法（自由民主模式、权利法案、九省制）
- 诺贝尔：1993 与 de Klerk 共同获诺贝尔和平奖；同年两人各自访美获 Liberty Medal（1993-07）
- 总统任期：1994-04-27 多种族大选，ANC 获 63% 选票；1994-05-10 比勒陀利亚就职，成为南非首位黑人国家元首、首位全民普选产生的总统；民族团结政府（de Klerk 与 Mbeki 任副总统）；推动种族和解、设立真相与和解委员会（Truth and Reconciliation Commission）；新宪法；拒绝连任，1999 由 Mbeki 接任
- 晚年：1998-1999 任不结盟运动秘书长；1995 创立 Nelson Mandela Children's Fund（捐出年收入三分之一）；晚年经 Nelson Mandela Foundation 致力消除贫困与 HIV/AIDS 事业；1994-12 出版自传 Long Walk to Freedom（狱中手稿 + Richard Stengel 访谈补充）
- 关键荣誉：Nobel Peace Prize 1993（共同）；Sakharov Prize；Lenin Peace Prize；Order of Lenin；UN Human Rights Prize；Bharat Ratna；Gandhi Peace Prize；Presidential Medal of Freedom；Congressional Gold Medal；费城自由勋章（1993）；超过 250 项荣誉；联合国大会 2009 定其生日 7 月 18 日为 Mandela Day（捐 67 分钟公益，纪念其 67 年运动生涯）
- 核心事业清单（4–6 条）：① 反种族隔离运动（ANC/青年联盟/抵制运动）；② 和平谈判终结种族隔离（与 de Klerk）；③ 民主南非的缔造（首届民选总统、民族团结政府、新宪法）；④ 真相与和解委员会；⑤ 公益慈善（Children's Fund、Nelson Mandela Foundation、HIV/AIDS）；⑥ 著述（Long Walk to Freedom）
- 关键时间线（15–20 节点）：
  1. 1918-07-18 生于 Mvezo
  2. 1943 加入 ANC；Fort Hare / Witwatersrand 学法律、约翰内斯堡执业律师
  3. 1944 参与创建 ANC 青年联盟；与 Evelyn Mase 结婚
  4. 1952 抵制运动；任 ANC 德兰士瓦分部主席
  5. 1955 人民大会
  6. 1956-1961 叛国罪审判（未定罪）
  7. 1958 与 Winnie Madikizela 结婚
  8. 1961 参与创建 Umkhonto we Sizwe
  9. 1962-08-05 被捕
  10. 1964 Rivonia 审判判终身监禁，入 Robben Island（至 1982）
  11. 1982-1988 Pollsmoor Prison
  12. 1988-1990 Victor Verster Prison
  13. 1990-02-11 无条件获释（全球直播）
  14. 1991-07 当选 ANC 主席；CODESA 谈判开启（1991-12）
  15. 1993 与 de Klerk 共同获诺贝尔和平奖；临时宪法达成
  16. 1994-04-27 首次全民普选（ANC 63%）；1994-05-10 就任总统
  17. 1994-12 出版 Long Walk to Freedom
  18. 1995 创立 Nelson Mandela Children's Fund
  19. 1996 与 Winnie 离婚；1998 与 Graça Machel 结婚；1998-99 任不结盟运动秘书长
  20. 1999-06-14 卸任（拒绝连任），Mbeki 接任
  21. 2009 联合国设立 Mandela Day（7 月 18 日）
  22. 2013-12-05 逝于约翰内斯堡，享年 95 岁，葬于 Qunu

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Nelson_Mandela/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 设置 `MAIN=Nelson_Mandela_zh`、`VIDEO_NAME=Nelson_Mandela_zh`

### 第 3 步：收集图片 【人物专属】

- 优先 page.md/images.txt 中的肖像 URL（250px 改 500px）；回退 Commons `Special:FilePath`；再失败装饰圆占位
- 可选插图：1992 达沃斯与 de Klerk 合影（page.md 图注明载）

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | anti-apartheid movement | 反种族隔离运动 | ANC/青年联盟/抵制运动/人民大会 | 早年页 |
| 1 | racial reconciliation | 种族和解 | 就任后核心方针、真相与和解委员会 | 总统页 |
| 2 | constitutional democracy | 宪政民主 | 临时宪法、新宪法、首届全民普选 | 谈判页/总统页 |
| 3 | human rights | 人权 | 获奖理由与 TRC 授权调查 | 诺奖页 |
| 4 | philanthropy | 公益慈善 | Children's Fund、Nelson Mandela Foundation、HIV/AIDS | 晚年页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致，仅收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Frederik Willem de Klerk | 无向 | 1993 诺贝尔和平奖共同得主 |
| colleague | Frederik Willem de Klerk | 无向 | 终结种族隔离的谈判对手方，民族团结政府副总统 |
| spouse | Evelyn Mase | 无向 | 1944 结婚，1958 离异 |
| spouse | Winnie Madikizela-Mandela | 无向 | 1958 结婚，1992 公开分居，1996 离异 |
| spouse | Graça Machel | 无向 | 1998 结婚，莫桑比克活动家、Samora Machel 遗孀 |
| parent-child | Makgatho Mandela | 无向 | 子（page.md 具名 6 子女之一） |
| parent-child | Makaziwe Mandela | 无向 | 女（page.md 具名 6 子女之一） |
| parent-child | Zenani Mandela-Dlamini | 无向 | 女（page.md 具名 6 子女之一） |
| parent-child | Zindziswa Mandela | 无向 | 女（page.md 具名 6 子女之一） |
| colleague | Oliver Tambo | 无向 | ANC 长期同事与流亡时期的党主席 |
| colleague | Walter Sisulu | 无向 | ANC 副主席，罗本岛狱友同代人 |
| colleague | Thabo Mbeki | 无向 | 民族团结政府副总统，1999 接任总统 |
| founder | Nelson Mandela Children's Fund | 创始人→机构 | 1995 创立，捐出年收入三分之一 |

> 入库注意：de Klerk 双行（co-honored + colleague）系 page.md 明载两重关系（1993 共同得主 + 谈判对手方/副总统）；批 19 de Klerk 篇互写镜像行。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：深蓝的坚忍 + 大地的温暖、门与光的意象
- **配色**：主色（manifest 预分配，勿改）`#37548D` 靛蓝 + 诺奖香槟金 `#C9A227` + 四分类色：
  - `badgeA` 反种族隔离 — 深红 `#8C3B2E`
  - `badgeB` 种族和解 — 橄榄绿 `#4E6B30`
  - `badgeC` 宪政民主 — 靛青 `#2E5E7D`
  - `badgeD` 公益慈善 — 赭金 `#B07D2B`
- **背景母题**：门与光的长廊几何（纵深透视线 + 渐亮色阶），呼应"漫长的自由之路"

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上角肖像 + 细边框 + 姓名小字注）。
2. 封面明示国籍（Nobel 官方口径 `South Africa`）与生卒年，底部状态栏 `国籍 | 身份 | 主要奖项` 三要素。
3. 必须有身份信息页：左侧头像 + 右侧信息网格（生卒、本名与尊称、教育、三段婚姻、囚禁年表、荣誉）。
4. 品牌口径统一：结尾页底部品牌标注写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属】

```
00  OpenPeace 项目首页（共享封面 \input）
01  封面 — 长路之光 / Nelson Mandela 1918–2013 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（本名/尊称、教育、婚姻、囚禁年表、荣誉）
03  特兰斯凯童年 (1918–1934) — Mvezo、腾布王族
04  求学与律师岁月 (1934–1943) — Fort Hare、Witwatersrand、约翰内斯堡执业
05  ANC 崛起 (1943–1960) — 青年联盟、抵制运动、人民大会、叛国罪审判
06  Rivonia 审判与铁窗 (1962–1990) — MK、终身监禁、三所监狱 27 年
07  获释 (1990) — 2-11 走出 Victor Verster、全球直播、和平与和解演讲
08  谈判之路 (1990–1993) — Groot Schuur/Pretoria Minute、CODESA、临时宪法
09  1993 诺贝尔和平奖 — 官方获奖理由页（英文原文 + 中译，与 de Klerk 共享）
10  总统岁月 (1994–1999) — 首位民选黑人总统、民族团结政府、TRC、新宪法
11  自传与晚年初章 — Long Walk to Freedom、Children's Fund、不结盟运动
12  退而不休 (1999–2013) — Nelson Mandela Foundation、HIV/AIDS、Mandela Day
13  家庭 — 三段婚姻与六个子女（客观叙述）
14  遗产 — 超过 250 项荣誉、Madiba 与"国父"之称（page.md 明载）
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**本篇专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| ★ 共享奖 | 1993 与 **F. W. de Klerk** 共同获得（批 19 立传互为镜像），全篇不得写成独得；正文以官方 citation 原句为准 |
| 获奖理由 | "for their work for the peaceful termination of the apartheid regime, and for laying the foundations for a new democratic South Africa."——注意主语是 they |
| 生卒 | 1918-07-18（frontmatter 另有 1918-01-01 噪声值，以正文与 Mandela Day 口径 07-18 为准）；卒 2013-12-05 约翰内斯堡、葬 Qunu |
| 本名 | Rolihlahla；"Nelson"是上学时所得教名（page.md 早年节）；Madiba 是科萨氏族名尊称，非本名 |
| 囚禁年表 | Robben Island 1964-82 / Pollsmoor 1982-88 / Victor Verster 1988-90，共 27 年；三段勿混 |
| 获释日期 | 1990-02-11 步出 Victor Verster（page.md 明载"Leaving Victor Verster Prison on 11 February"），勿写成 2 月 15 日 |
| 审判罪名 | Rivonia 审判定罪为破坏与阴谋颠覆国家（sabotage and conspiracy），判终身监禁；1956 叛国罪审判未定罪——两案勿混 |
| 婚姻 | Evelyn Mase 1944-1958 / Winnie 1958-1996（1992-04-13 公开分居）/ Graça Machel 1998- ；divorce 年份勿写错 |
| 子女 | 6 名，具名 4 人入库；其余不具名不入库 |
| 总统任期 | 1994-05-10 至 1999-06-14；拒绝连任是 page.md 明载，勿写"连任落败" |
| NAM 职务 | 1998-09 至 1999-06 任不结盟运动秘书长（infobox），勿写成"两届" |
| 政治立场叙述 | African nationalist + socialist、受马克思主义影响、秘密加入 SACP 等 page.md 明载事实可客观记录，不加评价；批评者两说（右翼/极左）并陈即可 |
| Mandela Day | 2009 联大设立，7 月 18 日，67 分钟公益 = 纪念 67 年运动生涯，勿写错数字 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| apartheid | 种族隔离 | 获奖理由关键词 |
| African National Congress (ANC) | 非洲人国民大会 | 1943 加入 |
| ANC Youth League | ANC 青年联盟 | 1944 参与创建 |
| Umkhonto we Sizwe (MK) | "民族之矛" | 1961 参与创建 |
| Rivonia Trial | 瑞佛尼亚审判 | 1964 终身监禁 |
| Robben Island | 罗本岛 | 1964-82 囚禁地 |
| Truth and Reconciliation Commission | 真相与和解委员会 | 总统任内设立 |
| Government of National Unity | 民族团结政府 | de Klerk/Mbeki 任副总统 |
| CODESA | 民主南非大会 | 1991-12 开启 |
| Long Walk to Freedom | 《漫漫自由路》 | 1994 自传 |
| Madiba | 马迪巴 | 科萨氏族名尊称 |
| Mandela Day | 曼德拉日 | 7 月 18 日 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配勿改】

- **选定曲目**: **Last Hope**
- **风格**: 坚毅 / 悲壮转昂扬 / 史诗
- **匹配理由**: 27 年铁窗到和平交接的叙事弧线——从至暗坚守到希望落地，"最后的希望"正是 1990-1994 转型岁月的注脚
- **本地路径**: `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`
- **时长**: 以实际文件为准，ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Nelson_Mandela/page.md` | 本地 Wikipedia 正文 + frontmatter（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 结构标杆（Beamer 骨架） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等；本例 UPD 复用库内 id=5903 并回填 Q8023） |
| `peace/PROMPTS_WORKFLOW.md` | 共享工作流与红线 |

> **开始执行。每完成一步汇报。最重要的事：共享奖口径（与 de Klerk）不可写错。**
