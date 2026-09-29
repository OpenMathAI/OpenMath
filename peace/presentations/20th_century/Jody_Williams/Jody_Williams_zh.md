# 和平奖得主立传提示词（OpenPeace 批次 20 · Jody Williams）

> 本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」之一，对象为个人：
> 乔迪·威廉斯（Jody Williams，1997 诺贝尔和平奖共同得主，国际禁止地雷运动创始协调员）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他人物侧共享 GitHub）。
- **本实例**：Jody Williams（美国政治活动家、教师，诺贝尔女性倡议创建者之一）。
- **设计哲学**：和平奖得主立传必须保留**「身份信息页」（Identity / Bio 速览页）**与「事业领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Jody Williams（1950-10-09 生于佛蒙特州拉特兰，在世）
- **气质关键词**：**把 1300 家 NGO 拧成一股绳的战略家、反「天堂幻想」的现实主义者、从禁雷到女性和平的接力者** —— 1997 诺贝尔和平奖获奖理由：
  > "for their work for the banning and clearing of anti-personnel mines"
  > （中译照抄名录：表彰他们为禁止与清除杀伤人员地雷所做的工作；该句为 ICBL 与 Williams 共享）
- **设计母题**：**织网（weaving the network）**。她把一个光杆办公室织成 90 国 1300 家组织的运动之网——网格隐喻公民社会的横向组织力，是比「火炬」更贴合其方法论的视觉语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Jody_Williams/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（OpenPeace 共享封面由主控统一建，若已有 `peace/presentations/cover/` 则优先用之）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：本批已完成「事业领域 + 社会关系入库」（见第 4 / 4.5 步表格），立传时以库内与 yaml 为准，不要另起炉灶。

### 第 0 步：下载并核对数据页面 【人物专属】

- ✅ 已抓取 Wikipedia 页面到 `peace/presentations/pages/20th_century/Jody_Williams/`（四件套）
- 提取 infobox 与正文，**事实基准如下**（第一轮已核对）：
  - 生卒：1950-10-09 生于佛蒙特州拉特兰，在世
  - 教育：1972 佛蒙特大学学士（BA）→ 1976 国际培训学院（SIT, Brattleboro）西班牙语与 ESL 教学文学硕士 → 1984 约翰斯·霍普金斯大学保罗·尼采高级国际研究学院（SAIS）国际关系硕士
  - 禁雷事业：1992 年初至 1998-02 任国际禁止地雷运动（ICBL）创始协调员；此前十一年从事尼加拉瓜与萨尔瓦多战争相关项目（《人权百科全书》称她「在 1980 年代从事危及生命的人权工作」）；与政府、联合国机构、红十字国际委员会协作，任 ICBL 首席战略家与发言人，把两家 NGO（员工只有她自己一人）发展为 90 国 1300 家 NGO 的国际运动
  - 里程碑：1997-09 奥斯陆外交大会通过禁雷条约（渥太华条约，归于她和 ICBL 名下）→ 三周后与 ICBL 共获诺贝尔和平奖；获奖时成为该奖近百年历史上第十位女性、第三位美国女性
  - 后续事业：2004-11 与伊朗和平奖得主 Shirin Ebadi、肯尼亚的 Wangari Maathai 商议后创建诺贝尔女性倡议（Nobel Women's Initiative，2006-01 启动），任主席（荣誉成员 Aung San Suu Kyi）；2020 呼吁雪佛龙为 Lago Agrio 油田清污付费；2019 支持 Every Woman Coalition 呼吁缔结终止对妇女暴力条约
  - 学术任职：2003 年起休斯顿大学社会工作研究生院全球正义杰出访问教授；2007 年起任 Sam and Cele Keeper 和平与社会正义讲席教授
  - 荣誉：15 个荣誉学位；2004 福布斯首届全球百大权力女性榜；Glamour「年度女性」
  - 著作：1995 合著地雷危机开山之作《After the Guns Fall Silent: The Enduring Legacy of Landmines》；2008《Banning Landmines: Disarmament, Citizen Diplomacy and Human Security》；2013 回忆录《My Name Is Jody Williams: A Vermont Girl's Winding Path to the Nobel Peace Prize》；另为多家大报撰稿
  - 关键时间线（15–20 节点）：1950 生于拉特兰 → 1972 UVM 学士 → 1976 SIT 硕士 → 1980s 中美地带人权工作 → 1984 SAIS 硕士 → 1992 创建 ICBL → 1995 合著出书 → 1997-09 奥斯陆条约 → 1997-10 诺奖公布 → 1998-02 卸任协调员 → 2003 休斯顿大学 → 2004 福布斯榜与商议 → 2006 诺贝尔女性倡议启动 → 2008 禁雷专著 → 2013 回忆录 → 2019 Every Woman 倡议 → 2020 雪佛龙呼吁
- 图片资源：infobox 有 2001 年 Williams 照片（page.md 图片链接）

### 第 1 步：建立目录 【模板通用】

- `peace/presentations/20th_century/Jody_Williams/` 已在（提示词所在），建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 参照 OpenPeace 已完成成品或 Kenneth_G_Wilson/Makefile，设置 `MAIN=Jody_Williams_zh`、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【人物专属】

- 下载 infobox 2001 年肖像（250px 改 500px）到 `images/` 并 `file` 验证；404 用 Commons `Special:FilePath` 回退；再失败用装饰圆占位

### 第 4 步：事业领域梳理（已入库） 【模板通用，人物专属内容】

**Williams 的事业领域（按 rank 排序，与 yaml/DB 一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | landmine ban | 禁雷运动 | 1997 诺奖核心：ICBL 与渥太华条约 | 禁雷页 |
| 1 | disarmament | 裁军 | 公民社会裁军运动方法论 | 禁雷页 |
| 2 | human rights | 人权 | 1980 年代中美洲人权工作至今 | 早年页 |
| 3 | women's rights | 女性权利 | 人权防卫的重点与诺贝尔女性倡议 | 倡议页 |
| 4 | peace and social justice | 和平与社会正义 | 休斯顿大学讲席教授领域 | 学术页 |

### 第 4.5 步：社会关系（已入库） 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | International Campaign to Ban Landmines | 无向 | 1997 诺贝尔和平奖共同得主 |
| colleague | Shirin Ebadi | 无向 | 共同商建诺贝尔女性倡议（2004–2006） |
| colleague | Wangari Maathai | 无向 | 共同商建诺贝尔女性倡议（2004–2006） |

> 注：她与 ICBL 的 founder（创始人→机构）关系已由 ICBL 侧 yaml 建行，本篇不重复建反向行。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：务实、草根动员的能量、清醒的锋利
- **配色**：主色深绿 `#1B4D3E`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeLandmine` 禁雷运动 — 靛蓝 `#4C5FD5`
  - `badgeNetworks` 公民网络 — 青绿 `#0E7C7B`
  - `badgeWomen` 女性倡议 — 琥珀 `#E07B30`
  - `badgeAcademic` 学术讲席 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），呼应「织网」母题——大小圆点以细线相连成网状布点，象征 1300 家组织的横向联合

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input 共享封面）
01  封面 — 把 1300 家 NGO 拧成一股绳 / Jody Williams 1950– + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、任职、主要荣誉、核心事业）
03  事业概览 — 禁雷 / 裁军 / 人权 / 女性权利 / 和平与社会正义
04  佛蒙特女孩 (1950–1984) — 拉特兰出身、UVM→SIT→SAIS 三段学历
05  中美地带的十年 (1980s) — 尼加拉瓜与萨尔瓦多项目、危及生命的人权工作
06  织网者：创建 ICBL (1992) — 两家 NGO 起步、员工一人、六组织结盟
07  首席战略家 (1992–1997) — 与政府/UN/红十字协作、1300 家 NGO、90 国网络
08  渥太华进程 (1997) — 奥斯陆条约通过、三周后诺奖
09  1997 诺贝尔和平奖 — 与 ICBL 共享、第十位女性、第三位美国女性
10  卸任之后 (1998–2003) — 卸任协调员、著述与讲台
11  诺贝尔女性倡议 (2004–2006) — Ebadi/Maathai 商议、2006 启动
12  学术讲席 (2003–) — 休斯顿大学、Keeper 讲席、全球正义
13  声音与现实 — 「天堂幻想」之讥、2019 妇女条约倡议、2020 雪佛龙呼吁
14  荣誉与著作 — 15 个荣誉学位、福布斯 2004、三本书与回忆录
15  遗产：一个人的办公室如何改变军备政治
16  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

**Williams 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 「第十位女性」 | 获奖时是和平奖近百年历史上**第十位女性**、**第三位美国女性**——两个序数勿互换，也勿外推成其他口径 |
| 诺奖「共同」 | 1997 与 **ICBL（组织）**共同获奖，理由句主语是 their（ICBL+Williams）；勿写成个人独得或与 1995/1996 得主混淆 |
| 头衔精确 | 她的 ICBL 头衔是 founding coordinator（创始协调员，1992 初–1998-02）——勿写成「主席」「秘书长」 |
| 学历三段 | UVM 1972 / SIT 1976 / SAIS 1984——SAIS 是约翰斯·霍普金斯分院（国际关系硕士），SIT 是西语+ESL 教学硕士；三校三科三年份勿串 |
| 一人办公室 | 「两家 NGO、员工只有她自己」描述 ICBL 起步规模——勿与 1992 年六组织结盟口径冲突，可并列解释 |
| 女性倡议时序 | 2004-11 与 Ebadi、Maathai 商议 → 2006-01 启动——两年两日期勿混；Suu Kyi 是荣誉成员非发起人 |
| 引语 | page.md 明载其「和平鸽/彩虹/kumbaya 把和平幼稚化」一段英文原话，可入引文框；除此之外勿杜撰引语 |
| 政治红线 | 涉及雪佛龙诉讼、中美洲等当代议题只作 page.md 明载客观事实记录，不加评价性语句 |
| 同名区分 | 库内另有数学家 Jody Williamson（不同人）——入库/引用时姓名精确到 Jody Williams |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| anti-personnel mine | 杀伤人员地雷 | 勿译「反人员地雷」 |
| Ottawa Treaty | 渥太华条约 | 1997-09 奥斯陆通过 |
| founding coordinator | 创始协调员 | Williams 的准确头衔 |
| chief strategist | 首席战略家 | 她在 ICBL 的角色 |
| Nobel Women's Initiative | 诺贝尔女性倡议 | 2006-01 启动 |
| human security | 人类安全 | 2008 专著关键词 |
| citizen diplomacy | 公民外交 | 其运动方法论 |
| landmine survivor | 地雷幸存者 | 援助对象 |
| Sam and Cele Keeper Professor | Keeper 讲席教授 | 休斯顿大学 2007 |
| School for International Training | 国际培训学院（SIT） | 1976 硕士 |
| SAIS | 保罗·尼采高级国际研究学院 | 霍普金斯 1984 |
| Glamour Woman of the Year | 年度女性 | Glamour 杂志 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配勿改】

- **选定曲目**: **Nostalgia** — Alex-Productions
- **风格**: 深情 / 回望 / 坚韧
- **匹配理由**: 「乡愁」匹配佛蒙特女孩走向世界又以回忆录回望一生（2013 My Name Is Jody Williams）；坚韧感匹配从一人办公室到百国网络的漫长织网；深情感匹配其为幸存者发声的底色
- **本地路径**: `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav`
- **时长**: 与 16 页成片用 ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Jody_Williams/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节） |
| `MySQL/data/Jody_Williams.yaml` | 领域/关系入库母本 |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
