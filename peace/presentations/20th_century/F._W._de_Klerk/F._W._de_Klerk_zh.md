# 和平奖得主立传提示词（OpenPeace 实例：Frederik Willem de Klerk）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」实例**，以 Frederik Willem de Klerk（1993 诺贝尔和平奖，与曼德拉共同获奖）为对象。
> 凡标注 `【模板通用】` 的部分复用 OpenPeace 共享骨架；标注 `【人物专属】` 的部分为本人物专属内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 各学科侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：对齐物理学家侧标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` 的 0–11 节结构。
- **本实例**：Frederik Willem de Klerk（弗雷德里克·威廉·德克勒克），南非末位种族隔离时代国家总统。
- **设计哲学**：和平奖得主立传必须有「身份信息页」与「和平事业结构化表达」；政治人物立传强调**政治转型叙事**的克制呈现——只写事实，不作评价。

---

## 二、背景信息 【人物专属】

- **目标人物**：Frederik Willem de Klerk（1936-03-18 ~ 2021-11-11，享年 85 岁）
- **气质关键词**：**旧秩序的终结者、谈判桌上的改革者、争议中的妥协者** —— 1993 诺贝尔和平奖获奖理由：
  > "for their work for the peaceful termination of the apartheid regime, and for laying the foundations for a new democratic South Africa"（表彰他们和平终结种族隔离制度的工作，以及为新民主南非奠定基础）
- **设计母题**：**打开的门（the open door）**。de Klerk 1989 年下令允许开普敦反种族隔离游行时说「通往新南非的门已经打开，无需强行撞开」——视觉语言用「开启之门 / 拆除之墙 / 汇流的路径」呼应体制转型。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/F._W._de_Klerk/page.md`（含 frontmatter QID Q151813）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - OpenPeace 共享封面：`peace/presentations/cover/openpeace_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇到歧义先征求主控意见再继续。
> **数据库同步要求**：包含「和平事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1936-03-18 生于约翰内斯堡 Mayfair 区 ~ 2021-11-11 逝于开普敦 Fresnaye 自宅（间皮瘤并发症，享年 85）
- 国籍：南非（南非荷兰语母语，先祖 1680 年代抵南非，法国胡格诺姓氏 Le Clerc 系）
- 家庭：父 Johannes "Jan" de Klerk（参议员、参议院议长七年、代国家总统、三届内阁部长）；兄 Willem de Klerk（长八岁，政治分析家，后脱党创立民主党）；姑父为前总理 J. G. Strijdom
- 教育：Hoërskool Monument（克鲁格斯多普，1953 一等通过）；Potchefstroom University（1954–1958，BA + LLB）；Goodenough College（伦敦）
- 法律生涯：Klerksdorp Pelser 律所实习 → 比勒陀利亚 Mac-Robert 律所 → 1962 年在 Vereeniging 自办律所十年
- 任职：1972-11 当选众议院议员（Vereeniging 选区）；部长序列——社会福利与抚恤（1978）、邮电（1978–79）、体育娱乐（1978–79）、矿业与能源（1979–82）、内政（1982–85）、国家教育与计划（1984–89）；1981 获 Meritorious Service 勋章
- 关键荣誉：诺贝尔和平奖 1993（与曼德拉共同）、费利克斯·乌弗埃-博瓦尼和平奖、阿斯图里亚斯亲王国际合作奖、费城自由奖章、Mapungubwe 金质勋章、美国哲学会会员（1994）、母校荣誉博士（1990）
- 核心事业清单：
  1. 1989-02 当选国民党领袖（击败 Barend du Plessis，69–61 票），1989-08-15 代总统、1989-09-20 正式就任国家总统
  2. 1989-10 释放 Walter Sisulu 等老年政治犯、准许开普敦游行（约 3 万人）、关闭国家安全管理体系；1989-12 探狱与曼德拉会谈三小时
  3. 1990-02-02 议会演讲：解禁非国大与南非共产党、宣布释放曼德拉（一周后获释）、废除《Separate Amenities Act 1953》；同年下令终止南非核武器计划（1991 基本完成，1993 才公开承认）
  4. 1992-03-17 白人公投：三分之二多数支持继续谈判终结种族隔离
  5. 1993-04-30 就种族隔离危害公开道歉；1993-10-10 授权 Mthatha 突袭（TRC 定性为严重侵犯人权）
  6. 1993-07 与曼德拉同获费城自由奖章；1993-12-10 同获诺贝尔和平奖（奥斯陆）
  7. 1994-04 首次全民普选（ANC 62%、国民党 20%）；1994–1996 与 Thabo Mbeki 并任副总统（民族团结政府）；1996-05-09 退出联合政府，1996-07 起任反对党领袖，1997 退出政坛
- 关键时间线（15–20 节点）：1936 生于约翰内斯堡 → 1953 中学毕业 → 1954–58 Potchefstroom 双学位 → 1959 与 Marike Willemse 结婚 → 1962 自办律所 → 1972 入国会 → 1978 入阁 → 1984–89 教育部长 → 1989-02 国民党领袖 → 1989-09 国家总统 → 1990-02-02 解禁演讲 → 1990 终止核计划 → 1992 公投 → 1993-04 道歉 → 1993-12-10 诺奖 → 1994 大选与副总统 → 1996 退出联合政府 → 1997 退政坛 → 1999 离婚再婚、出版自传 → 2000 创办 FW de Klerk 基金会 → 2004 创办 Global Leadership Foundation → 2001 前妻遇害 → 2021-11-11 逝世，身后视频「无保留道歉」

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下确认 `F._W._de_Klerk/` 与 `images/` 存在

### 第 2 步：复制 Makefile 【模板通用】

- 复制同侧已有成品目录 Makefile，设置 `MAIN=F._W._de_Klerk_zh`、`VIDEO_NAME=F._W._de_Klerk_zh`

### 第 3 步：收集图片 【人物专属】

- infobox 肖像 1993 年照（images.txt 有 URL 则直接取，250px 改 500px）；备用插图：Davos 1992 与曼德拉握手照、费城自由奖章同框照
- 404 则用 Wikipedia REST API page/summary 查 infobox 原图名，再不行用装饰圆占位

### 第 4 步：和平事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | democratic transition | 民主转型 | 终结种族隔离、引入普选 | 封面、核心页 |
| 1 | constitutional negotiation | 宪法谈判 | 与非国大谈判新宪法与过渡安排 | 谈判页 |
| 2 | anti-apartheid reform | 反种族隔离改革 | 解禁政党、释放政治犯、废歧视立法 | 1990 改革页 |
| 3 | nuclear disarmament | 核裁军 | 1990 下令终止南非核武器计划 | 核裁军页 |
| 4 | law | 法学 | 律师出身、法学讲席受聘 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Marike de Klerk | 无向 | 1959 结婚，1996 离婚；2001 遇害 |
| spouse | Elita Georgiades | 无向 | 1999 再婚 |
| parent-child | Jan de Klerk | 无向 | 父亲，参议员/代国家总统 |
| co-honored | Nelson Mandela | 无向 | 1993 诺贝尔和平奖共同得主 |
| colleague | Nelson Mandela | 无向 | 谈判终结种族隔离；1994–96 曼德拉政府副总统 |
| colleague | Thabo Mbeki | 无向 | 民族团结政府两位副总统并任 |
| controversy | Desmond Tutu | 无向 | 真相与和解委员会主席，就安全部队侵权行为质询 |

### 第 5 步：设计配色方案 【人物专属，主色勿改】

- **主色**：深砖红 `#7E1E23`（旧秩序与转型的重量）+ 诺奖香槟金 `C9A227`
- badgeA 民主转型 — 赭金 `#B08D2E`；badgeB 宪法谈判 — 靛蓝 `#2F4470`；badgeC 反隔离改革 — 深青 `#175E54`；badgeD 核裁军 — 暗紫 `#5B2A86`
- **背景母题**：开启的门与光带（几何门框 + 斜向光线），呼应「门已打开」

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）与国籍行（底部状态栏 `国籍 | 机构 | 主要奖项` 三要素）。
2. 必须有身份信息页（★ 必做）：左头像 + 右信息网格（生卒、本名、国籍、出生地、教育、任职、荣誉、核心事业）。
3. 结尾页品牌统一 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 旧秩序的终结者 / F. W. de Klerk 1936–2021 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  和平事业概览 — 民主转型 / 宪法谈判 / 反隔离改革 / 核裁军
04  早年：政治世家 (1936–1972) — 政治家族、Potchefstroom、律师岁月
05  部长岁月 (1972–1989) — 六任部长、保守派名声、1989 党魁之争 69–61
06  转折：1989 — 游行准许、释放 Sisulu、探狱曼德拉、关闭 NSMS
07  1990-02-02 议会演讲（核心贡献页）— 解禁、释放曼德拉、废法
08  核裁军：悄然终结的核武库 — 1990 下令、1991 完成、1993 公开
09  谈判年代 — 1992 公投、Boipatong 风波、1993 道歉
10  诺贝尔和平奖 1993 — 与曼德拉共享、颁奖词
11  副总统与决裂 (1994–1996) — 民族团结政府、1996 退出
12  真相与和解委员会 — Vlakplaas 作证、Khotso House 争议
13  晚年 (1997–2021) — 基金会、自传、前妻遇害、身后视频道歉
14  争议与遗产 — 两面批评、最后一讯
15  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 无载禁写 | 凡 page.md 未载的细节（家庭其他成员、其他奖项细节、私人言论）一律不写 |
| 引语白名单 | 仅可用 page.md 明载英文原句：门已打开句（1989）、议会演讲段（1990-02）、道歉段（1993-04-30）、临终视频道歉段（2021）；引语不得改写 |
| 政治敏感红线 | 种族隔离、南非政治只作 page.md 客观事实记录（含 As 用语、TRC 定性、两面批评），不加任何评价性语句；2012 BBC 访谈与 2020 "agitprop" 言论若提及仅客观陈述「引发争议、基金会数日后撤回」 |
| 年份口径 | 国民党领袖任期 1989-02-02 起；代总统 1989-08-15–09-20；正式总统 1989-09-20–1994-05-10；副总统 1994-05-10–1996-06-30；反对党领袖 1996-07-01–1997-09-08 |
| 兄弟角色 | 兄 Willem 是政治分析家、脱离国民党创民主党——勿写成「同僚政客」 |
| 双诺奖口径 | 1993 与曼德拉「共同获奖」，理由句为同一句（they），勿写成独得或拆分理由 |
| TRC 定性 | TRC 曾认定其为「严重侵犯人权的帮凶」（Khotso House 知情未披露），de Klerk 抗议后委员会让步；2002 终版报告改为有限指控——两个口径都写、注明演变 |
| 前妻之死 | Marike 2001-12-03 在开普敦遇害，凶手系保安（2003 判两终身监禁）——客观一句即可，勿渲染 |
| 名字形式 | 英文通用名 F. W. de Klerk / Frederik Willem de Klerk，中文名「弗雷德里克·威廉·德克勒克」，勿简写为「德克勒克总统」以外的不规范形 |
| Mthatha 突袭 | 1993-10-08，致 3 名少年与 2 名 12 岁儿童死亡，TRC 定性严重侵犯人权——如实记录 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| apartheid | 种族隔离制度 | 勿译「种族隔离政策」以外的含糊词 |
| State President | （南非）国家总统 | 1984–1994 宪制职位，勿与「总理」混 |
| National Party | 国民党 | 与 1997 后的 New National Party 区分 |
| universal suffrage | 普选权 | 1994 首次全民选举 |
| Government of National Unity | 民族团结政府 | 两副总统并任 |
| Truth and Reconciliation Commission | 真相与和解委员会 | 简称 TRC |
| referendum | （1992 白人）公投 | 仅限白人选民 |
| mesothelioma | 间皮瘤 | 死因 |
| FW de Klerk Foundation | 德克勒克基金会 | 2000 创办 |
| Global Leadership Foundation | 全球领导力基金会 | 2004 创办 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配勿改】

- **选定曲目**: **Empire Collapse** — Cold Cinema
- **风格**: 电影感 / 史诗 / 旧秩序崩塌
- **匹配理由**: 「帝国崩塌」直接呼应本篇设计母题——一个旧体制在谈判桌上被和平拆除，末位总统亲手终结三百年白人统治；管弦压迫感匹配转型的历史重量与 de Klerk 两面受敌的争议处境
- **本地路径**: `music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/F._W._de_Klerk/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。**

---

## 六、执行清单 【模板通用，逐项勾选】

- [ ] 第 0 步：通读 page.md 全文，核对本文件「事实基准」与正文一致（重点核对部长序列年份与两任婚姻年份）
- [ ] 第 1 步：确认目录 `F._W._de_Klerk/`（含 `images/`）存在
- [ ] 第 2 步：复制 Makefile，改 `MAIN` / `VIDEO_NAME` 为 `F._W._de_Klerk_zh`
- [ ] 第 3 步：下载肖像并 `file` 验证格式（JFIF density 异常用 sips 改 72dpi）；404 则 REST API 查 infobox 原图名；再不行装饰圆占位
- [ ] 第 4 步：按领域表写入 `MySQL/data/F._W._de_Klerk.yaml` 的 `fields`（5 条，rank 0–4）
- [ ] 第 4.5 步：按社会关系表写入 yaml `relations`（7 条；note 含英文缩写与年份，勿加评价）
- [ ] 第 5 步：tex 头部宏定义配色（主色 #7E1E23 + C9A227 + badgeA–D 四分类色），宏名统一 `mainclr/accentclr/badgeA..D`，注释写语义
- [ ] 第 6 步：按幻灯片序列逐页定义 `\newcommand{\xxxslide}`（宏名禁数字、禁 `\u00b7`）
- [ ] 第 7 步：编译循环：`make distclean && make`（latexmk 多遍），0 error、vbox≤10pt、hbox≤50pt
- [ ] 第 8 步：`pdftoppm` 逐页目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标
- [ ] 第 9 步：史实审查（对照陷阱表逐条核）+ 术语审查（对照术语清单核译名）
- [ ] 收尾：`make pdf` 后核对页数与第 6 步规划一致（页数不符=有帧未渲染或被合并）；`make images && make video` 出 mp4

---

## 七、版式补遗 【模板通用，OpenPeace 沉淀】

- 表格页安全负间距：顶部 −0.35cm、`arraystretch 0.78–0.82`、公式框前 −0.35~−0.55cm（条目多时 −0.45cm 起）
- honors 类页 itemize 用 `\itemsep −2.5pt + topsep 0 + arraystretch 0.58` + 顶部 −0.55cm 压 4 条目（−0.65cm 会遮副标题）
- `leg` 节点 `x=±5.4cm` 的固有 hbox 8–9pt 属模板继承，不需修；时间线 `\foreach` 分隔符必须 ASCII 逗号
- 文本模式希腊字母缺字须改数学模式；带圈数字 U+2460–2473 需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`；★号 U+2605 在 lmsans-oblique 缺字，用 `\faStar` 或换字体
- 长英文头衔（State President / Deputy President）入 badge 时缩写为 SP/DP 并在脚注展开，避免溢出

---

## 八、入库回查清单 【模板通用】

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 -c "
from db_mysql import get_conn
conn=get_conn(); cur=conn.cursor()
cur.execute(\"SELECT id,name_en,has_social_data FROM people WHERE qid='Q151813'\")
p=cur.fetchone(); print(p)
cur.execute('SELECT COUNT(*) FROM person_field WHERE person_id=%s',(p[0],)); print('fields:',cur.fetchone()[0])
cur.execute('SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s',(p[0],p[0])); print('relations:',cur.fetchone()[0])"
```

- 预期：`has_social_data=1`、fields=5、relations=7；并发撞字典表唯一键（Duplicate entry）等 2 秒重跑一次（幂等）

