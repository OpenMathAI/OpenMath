# 和平奖得主立传提示词（OpenPeace 实例：Shimon Peres）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」实例**，以 Shimon Peres（1994 诺贝尔和平奖，与拉宾、阿拉法特共同获奖）为对象。
> 凡标注 `【模板通用】` 的部分复用 OpenPeace 共享骨架；标注 `【人物专属】` 的部分为本人物专属内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 各学科侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：对齐物理学家侧标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` 的 0–11 节结构。
- **本实例**：Shimon Peres（希蒙·佩雷斯），以色列两任总理（1984–86、1995–96）、第九任总统（2007–2014）、70 年政坛生涯。
- **设计哲学**：和平奖得主立传必须有「身份信息页」与「和平事业结构化表达」；长寿政治家立传强调**时间跨度叙事**——政坛长跑与身份转换（鹰派国防部长→和平设计师→总统）只按事实呈现。

---

## 二、背景信息 【人物专属】

- **目标人物**：Shimon Peres（1923-08-02 ~ 2016-09-28，享年 93 岁）
- **气质关键词**：**建国的最后见证者、从鹰派到和平设计师、政坛长跑者** —— 1994 诺贝尔和平奖获奖理由：
  > "for their efforts to create peace in the Middle East"（表彰他们为在中东缔造和平所做的努力）
- **设计母题**：**长跑与接力**。70 年公职、12 届内阁、48 年议员——视觉语言用长时段时间线、接力棒/握手、橄榄枝与风（Winds of Freedom）。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Shimon_Peres/page.md`（含 frontmatter QID Q57410）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - OpenPeace 共享封面：`peace/presentations/cover/openpeace_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇到歧义先征求主控意见再继续。
> **数据库同步要求**：包含「和平事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1923-08-02 生于波兰 Wiszniew（今白俄罗斯 Vishnyeva，本名 Szymon Perski）~ 2016-09-28 逝于拉马特甘 Sheba 医疗中心（脑卒中后脑干不可逆损伤，享年 93）
- 家庭：父 Yitzhak Perski（木材富商，二战从军被俘囚于 Auschwitz 附属战俘营 E715）；母 Sara（图书馆员）；弟 Gershon；祖父 Rabbi Zvi Meltzer 亲自教授《塔木德》；远亲影星 Lauren Bacall（本人称关系不确定）
- 教育：Balfour 学校与 Geula 商业中学（特拉维夫）→ Ben Shemen 农业学校（15 岁转入）、Kibbutz Geva 劳作 → 后在 The New School / NYU / Harvard 进修（无学位叙事按 page.md）
- 早年：1941 当选 Labor Zionist 青年运动 HaNoar HaOved VeHaLomed 书记；Alumot 基布兹创社先驱；1942 登马萨达；姓氏 Peres 取自 Hebrew 语「鹫」（bearded vulture）
- 任职：1952 国防部副总局长（28 岁）→ 1953–1959 国防部总局长（29 岁，最年轻）→ 1959-11 起任议员（48 年最长纪录，唯三 2006 年初三个月短暂离任）→ 国防部长（1974–1977）→ 代理总理（1977-04）→ 总理第一任期 1984-09-13–1986-10-20（轮换政府）→ 外长（1986–88、1988–90 财政、1992–1995）→ 总理第二任期 1995-11-04–1996-06（接遇刺的拉宾）→ 2005 加入 Kadima → 总统 2007-07-15–2014-07-24
- 关键荣誉：诺贝尔和平奖 1994（与拉宾、阿拉法特共同）、总统自由勋章（2012）、国会金质奖章（2014）、法国荣誉军团、阿斯图里亚斯亲王国际合作奖等
- 核心事业清单：
  1. 1956 参与塞夫尔协议谈判；1963 与肯尼迪政府谈判购得 Hawk 导弹（美国对以首次军售）
  2. 1984–86 轮换政府总理：经济通胀治理与撤军黎巴嫩（page.md 明载事项为准）
  3. 1992–1995 外长任内：1992–93 秘密参与奥斯陆谈判（1993-08-19 秘密飞奥斯陆）、1993-09-13 代表以色列签署奥斯陆一号
  4. 1994 主持/推动约以和约（10-26 签署，终结 46 年官方战争状态）；1994-12-10 与拉宾、阿拉法特同获诺贝尔和平奖
  5. 1995-11 接任总理维持和平进程；1996 输给内塔尼亚胡
  6. 1996 创立 Peres Center for Peace（促进中东持久和平与宽容、经济技术合作）
  7. 2007–2014 任总统：在任时为全球最年长国家元首；2016 创立以色列创新中心（特拉维夫 Ajami 区）后逝世
- 关键时间线（15–20 节点）：1923 生于波兰 → 1934 随家移居特拉维夫 → 1941 青年运动书记 → 1947–49 从军与外交历练（page.md 口径）→ 1952 国防部副总局长 → 1953 总局长 → 1956 塞夫尔协议 → 1959 入议会 → 1974 国防部长 → 1977 代理总理 → 1984 轮换总理 → 1986 与 Shamir 对调外长 → 1990–92 在野 → 1992 外长 → 1993-09-13 奥斯陆一号 → 1994 约以和约 → 1994-12-10 诺奖 → 1995-11-04 拉宾遇刺后接任总理 → 1996 创 Peres 和平中心、败选 → 2005 转投 Kadima → 2007 当选总统 → 2013 宣布不再连任 → 2014-07-24 卸任 → 2016-09-13 中风 → 2016-09-28 逝世 → 2016-09-30 Herzl 山国葬（75 国代表）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下确认 `Shimon_Peres/` 与 `images/` 存在

### 第 2 步：复制 Makefile 【模板通用】

- 复制同侧已有成品目录 Makefile，设置 `MAIN=Shimon_Peres_zh`、`VIDEO_NAME=Shimon_Peres_zh`

### 第 3 步：收集图片 【人物专属】

- infobox 肖像 1996 年官方照（images.txt 有 URL 则直接取，250px 改 500px）；备用插图：1993-09-13 奥斯陆一号签署照、1994-12-10 奥斯陆三人领奖照
- 404 则用 Wikipedia REST API page/summary 查 infobox 原图名，再不行用装饰圆占位

### 第 4 步：和平事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace negotiation | 和平谈判 | 奥斯陆密谈与一号协议签署 | 封面、核心页 |
| 1 | diplomacy | 外交 | 塞夫尔协议、Hawk 谈判、约以和约推动 | 外交页 |
| 2 | defense policy | 国防政策 | 国防部总局长、两任国防部长 | 国防页 |
| 3 | economic development | 经济发展 | 轮换政府经济治理、晚年创新推广 | 改革/晚年页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Sonya Gelman | 无向 | 1945 结婚，2011 逝世 |
| parent-child | Tsvia Walden | 无向 | 子女之一（语言学家，page.md 具名） |
| parent-child | Chemi Peres | 无向 | 子女之一（风险投资人，page.md 具名） |
| co-honored | Yitzhak Rabin | 无向 | 1994 诺贝尔和平奖共同得主 |
| co-honored | Yasser Arafat | 无向 | 1994 诺贝尔和平奖共同得主 |
| rival | Yitzhak Rabin | 无向 | 工党领袖长期竞争者 |
| influence | David Ben-Gurion | 无向 | 政治导师与提携者（protégé） |
| colleague | Yitzhak Shamir | 无向 | 1984–86 轮换政府总理/外长对调 |

### 第 5 步：设计配色方案 【人物专属，主色勿改】

- **主色**：暗酒红 `#750014`（庄重的政坛长跑）+ 诺奖香槟金 `C9A227`
- badgeA 和平谈判 — 橄榄绿 `#175E54`；badgeB 外交 — 靛蓝 `#2F4470`；badgeC 国防政策 — 深灰蓝 `#37474F`；badgeD 经济发展 — 赭金 `#B08D2E`
- **背景母题**：长时段时间线光带与风纹（呼应 Winds Of Freedom），橄榄枝收束于握手剪影

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）与国籍行（底部状态栏 `国籍 | 机构 | 主要奖项` 三要素）。
2. 必须有身份信息页（★ 必做）：左头像 + 右信息网格（生卒、本名、国籍、出生地、教育、任职、荣誉、核心事业）。
3. 结尾页品牌统一 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 建国的最后见证者 / Shimon Peres 1923–2016 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  和平事业概览 — 和平谈判 / 外交 / 国防政策 / 经济发展
04  早年：从 Wiszniew 到特拉维夫 (1923–1947) — 本名 Perski、祖父、青年运动
05  国防部岁月 (1952–1959) — 28 岁副总局长、塞夫尔协议、Hawk 谈判
06  议会与在野 (1959–1984) — 1974 国防部长、1977 代理总理、党魁之争
07  轮换政府总理 (1984–1986) — 与 Shamir 轮换、经济治理
08  外长与奥斯陆（核心贡献页）— 秘密谈判、1993-09-13 签署
09  约以和约 1994 — 终结 46 年战争状态
10  诺贝尔和平奖 1994 — 三人共享、颁奖词、挪威委员会争议只述事实
11  第二任期总理 (1995–1996) — 接任、维持和平进程、败选
12  Peres 和平中心与晚年政坛 (1996–2007) — 创中心、转投 Kadima
13  总统岁月 (2007–2014) — 最年长元首、2014 卸任
14  逝世与国葬 — 中风、75 国代表、Herzl 山安葬于 Rabin 与 Shamir 之间
15  遗产与结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 无载禁写 | 凡 page.md 未载的细节一律不写；不从颁奖词反推关系 |
| 引语白名单 | 仅可用 page.md 明载英文原句（如 Lauren Bacall 亲缘关系自述、Peres Center 使命句）；全篇引语从严，无原句则转述 |
| 政治敏感红线 | 以色列-巴勒斯坦内容一律按 page.md 客观事实记录（奥斯陆争议、2002 挪威委员成员遗憾言论、1996 Qana 炮击事件），只述事实不作评价 |
| 本名 | 原名 Szymon Perski（波兰语）；Peres 姓氏取自 Hebrew 语「鹫」（bearded vulture，1944 内盖夫远征遇鸟得名的 page.md 口径）——勿写「原名佩雷斯」 |
| 总理任次 | 三段总理经历：1977-04-22–06-21 代理、1984-09-13–1986-10-20 轮换、1995-11-04–1996-06-18 接任； presidency 2007-07-15–2014-07-24 |
| 议员纪录 | 48 年议员（1959-11-30–2006-01-15 + 2006-03-28–2007-06-13），最长纪录；「除 2006 年初三个月外连续任职」口径照写 |
| Rabin 双重关系 | 与 Rabin 既是党魁之争的长期对手（rival）又是 1994 共同得主与外长/总理同僚——co-honored 与 rival 两条分立 |
| 子女口径 | page.md infobox 作「3, including Tsvia and Chemi」——具名两人入库，第三人无名不入库 |
| 表亲争议 | Lauren Bacall 表亲关系本人自述「不确定谁说的」，若提及只作存疑注记，不建关系 |
| 死因口径 | 2016-09-13 中风→脑干不可逆损伤→09-28 逝世，勿写「心脏病」 |
| 反对手方 | Obama/Clinton/Sharon/Netanyahu 等不建关系（无白名单关系类型载体） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| rotation government | 轮换政府 | 1984–88 工党-利库德大联合 |
| Oslo I Accord | 奥斯陆一号协议 | 1993-09-13 白宫签署 |
| Israel–Jordan peace treaty | 约以和约 | 1994-10-26 |
| Peres Center for Peace | 佩雷斯和平中心 | 1996 创立 |
| Knesset | 以色列议会 | 48 年最长议员 |
| aliyah | 移居以色列（阿利亚） | 最后一位移居而非本土出生的总理 |
| Protocol of Sèvres | 塞夫尔协议 | 1956 |
| Kadima | 前进党 | 2005 加入 |
| brainstem | 脑干 | 死因链终点 |
| Mount Herzl | Herzl 山 | 葬于 Rabin 与 Shamir 墓间 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配勿改】

- **选定曲目**: **Winds Of Freedom** — Really Slow Motion & Giant Apes
- **风格**: 英雄管弦 / 开阔 / 长时段
- **匹配理由**: 「自由之风」贴合本篇设计母题——70 年政坛长跑中始终在场、从国防鹰派到和平设计师再到国家元老的开阔弧线；史诗管弦感匹配 75 国代表送别的国葬与跨越世纪的建国一代告别
- **本地路径**: `music_audio/inspiring-electronic/25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Shimon_Peres/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。**

---

## 六、执行清单 【模板通用，逐项勾选】

- [ ] 第 0 步：通读 page.md 全文，核对本文件「事实基准」与正文一致（重点核对三段总理经历与议员 48 年纪录口径）
- [ ] 第 1 步：确认目录 `Shimon_Peres/`（含 `images/`）存在
- [ ] 第 2 步：复制 Makefile，改 `MAIN` / `VIDEO_NAME` 为 `Shimon_Peres_zh`
- [ ] 第 3 步：下载肖像（1996 官方照）并 `file` 验证格式；404 则 REST API 查 infobox 原图名；再不行装饰圆占位
- [ ] 第 4 步：按领域表写入 `MySQL/data/Shimon_Peres.yaml` 的 `fields`（4 条，rank 0–3）
- [ ] 第 4.5 步：按社会关系表写入 yaml `relations`（8 条；Rabin 的 rival 与 co-honored 两条分立）
- [ ] 第 5 步：tex 头部宏定义配色（主色 #750014 + C9A227 + badgeA–D 四分类色），宏名统一 `mainclr/accentclr/badgeA..D`，注释写语义
- [ ] 第 6 步：按幻灯片序列逐页定义 `\newcommand{\xxxslide}`（宏名禁数字、禁 `\u00b7`）
- [ ] 第 7 步：编译循环：`make distclean && make`（latexmk 多遍），0 error、vbox≤10pt、hbox≤50pt
- [ ] 第 8 步：`pdftoppm` 逐页目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标
- [ ] 第 9 步：史实审查（对照陷阱表逐条核，本名与姓氏来历口径核对）+ 术语审查（对照术语清单核译名）
- [ ] 收尾：`make pdf` 后核对页数与第 6 步规划一致；`make images && make video` 出 mp4

---

## 七、版式补遗 【模板通用，OpenPeace 沉淀】

- 表格页安全负间距：顶部 −0.35cm、`arraystretch 0.78–0.82`、公式框前 −0.35~−0.55cm（条目多时 −0.45cm 起）
- honors 类页 itemize 用 `\itemsep −2.5pt + topsep 0 + arraystretch 0.58` + 顶部 −0.55cm 压 4 条目（−0.65cm 会遮副标题）
- `leg` 节点 `x=±5.4cm` 的固有 hbox 8–9pt 属模板继承，不需修；时间线 `\foreach` 分隔符必须 ASCII 逗号
- 本篇时间跨度大（93 年 / 70 年公职），时间线页建议分段两行或用世代区块（建国一代→轮换政府→奥斯陆→总统府），防单行超宽
- 希伯来文名 שמעון פרס 入封面时用 `\newfontfamily\hebrewfont[Script=Hebrew]{Arial Hebrew}`（参照 Wigderson 篇先例）

---

## 八、入库回查清单 【模板通用】

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 -c "
from db_mysql import get_conn
conn=get_conn(); cur=conn.cursor()
cur.execute(\"SELECT id,name_en,has_social_data FROM people WHERE qid='Q57410'\")
p=cur.fetchone(); print(p)
cur.execute('SELECT COUNT(*) FROM person_field WHERE person_id=%s',(p[0],)); print('fields:',cur.fetchone()[0])
cur.execute('SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s',(p[0],p[0])); print('relations:',cur.fetchone()[0])"
```

- 预期：`has_social_data=1`、fields=4、relations=8；并发撞字典表唯一键（Duplicate entry）等 2 秒重跑一次（幂等）
