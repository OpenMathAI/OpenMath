# 和平奖得主立传提示词（OpenPeace 实例：Yasser Arafat）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」实例**，以 Yasser Arafat（1994 诺贝尔和平奖，与拉宾、佩雷斯共同获奖）为对象。
> 凡标注 `【模板通用】` 的部分复用 OpenPeace 共享骨架；标注 `【人物专属】` 的部分为本人物专属内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 各学科侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：对齐物理学家侧标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` 的 0–11 节结构。
- **本实例**：Yasser Arafat（亚西尔·阿拉法特），巴解组织主席（1969–2004）、巴勒斯坦国首任总统、巴勒斯坦民族权力机构首任主席。
- **设计哲学**：和平奖得主立传必须有「身份信息页」与「和平事业结构化表达」；政治人物立传强调**事实叙事**——争议经历（武装斗争/恐怖主义指控/死亡疑云）只按 page.md 客观记录，不作评价。

---

## 二、背景信息 【人物专属】

- **目标人物**：Yasser Arafat（c. 1929-08 ~ 2004-11-11，享年 75 岁）
- **气质关键词**：**巴勒斯坦事业的化身、橄榄枝与步枪并举者、争议中的幸存者** —— 1994 诺贝尔和平奖获奖理由：
  > "for their efforts to create peace in the Middle East"（表彰他们为在中东缔造和平所做的努力）
- **设计母题**：**橄榄枝与凯菲耶（keffiyeh）**。1974 年联合国演讲「一手持橄榄枝、一手持自由战士的步枪」与黑白格头巾意象——视觉语言用橄榄枝、头巾黑白几何纹、地图与握手剪影。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Yasser_Arafat/page.md`（含 frontmatter QID Q34211）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - OpenPeace 共享封面：`peace/presentations/cover/openpeace_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇到歧义先征求主控意见再继续。
> **数据库同步要求**：包含「和平事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：c. 1929-08-04（一说 08-24，page.md 作 4 or 24 August 1929）生于开罗 ~ 2004-11-11 逝于法国克拉马（Clamart）珀西军医院（出血性脑卒中，享年 75）
- 本名：Mohammed Abdel Rahman Abdel Raouf Arafat al-Qudwa al-Husseini；绰号（kunya）Abu Ammar；1950 年代初取名 Yasser
- 家庭：父 Abdel Raouf al-Qudwa（加沙来的巴勒斯坦人，开罗纺织商）；母 Zahwa Abul Saud（1933 病逝）；七子女中排第二幼；弟 Fathi；童年曾寄居耶路撒冷老城摩洛哥区舅舅家四年
- 教育：开罗国王费萨尔一世大学（今开罗大学）1944 入学，土木工程学士；1952–1956 任巴勒斯坦学生总会（GUPS）主席
- 任职：法塔赫 1959 年立（科威特），终身领导；PLO 主席 1969-02-04–2004-10；巴勒斯坦国总统 1989-04-02–2004；PNA 主席 1994-07-05–2004-11-11
- 关键荣誉：诺贝尔和平奖 1994（与拉宾、佩雷斯共同）、尼赫鲁国际理解奖、费利克斯·乌弗埃-博瓦尼和平奖、阿斯图里亚斯亲王国际合作奖、意大利共和国功绩大十字勋章等
- 核心事业清单：
  1. 1948 参战（随穆斯林兄弟会武装，未入该组织）；1950 年代末与 Abu Iyad、Abu Jihad 等共同创建法塔赫
  2. 1968 卡拉迈之战后声名鹊起（《时代》1968-12-13 封面）；1969-02-04 当选 PLO 主席
  3. 1970 黑九月事件后转移黎巴嫩；1974 拉巴特峰会 PLO 获「巴勒斯坦人民唯一合法代表」地位，成为首个在联大全会发言的非政府组织代表（橄榄枝演讲）
  4. 1982 黎巴嫩战争后流亡突尼斯（1985 木腿行动空袭幸免）；1987 第一次大起义；1988-11-15 巴勒斯坦国宣告成立，12 月宣布放弃一切形式恐怖主义、接受安理会 242 号决议与以色列和平生存权
  5. 1993 奥斯陆密谈：交换承认信件；1993-09-13 白宫签署奥斯陆一号协议（与拉宾、克林顿同框握手）
  6. 1994-07 返回加沙组建 PNA；1996-01-20 当选 PNA 主席（88.2%）；1998 怀伊河备忘录；2000 戴维营峰会拒绝巴拉克方案
  7. 2001 起被以军围困拉姆安拉官邸（Mukata'a）逾两年；2003 让出总理职位予 Mahmoud Abbas；2004-11-11 逝世，死因三方调查结论不一（瑞士测得钋、法俄判自然原因、2015 法国检方结案）
- 关键时间线（15–20 节点）：1929 生于开罗 → 1933 母逝 → 1944 入开罗大学 → 1948 参战 → 1952–56 GUPS 主席 → 1957 赴科威特 → 1959 法塔赫立 → 1967 加入 PLO → 1968 卡拉迈 → 1969-02 PLO 主席 → 1970 黑九月 → 1974 联大演讲 → 1982 流亡突尼斯 → 1988 建国宣言与转变 → 1989 巴勒斯坦国总统 → 1991 马德里和会 → 1993-09 奥斯陆一号 → 1994-07 回加沙 → 1994-12-10 诺奖 → 1996 当选 PNA 主席 → 2000 戴维营 → 2002 官邸围困 → 2004-11-11 逝世 → 2007 拉姆安拉陵墓揭幕

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下确认 `Yasser_Arafat/` 与 `images/` 存在

### 第 2 步：复制 Makefile 【模板通用】

- 复制同侧已有成品目录 Makefile，设置 `MAIN=Yasser_Arafat_zh`、`VIDEO_NAME=Yasser_Arafat_zh`

### 第 3 步：收集图片 【人物专属】

- infobox 肖像 1996 年照（images.txt 有 URL 则直接取，250px 改 500px）；备用插图：1993-09-13 白宫握手照、1994-12-10 奥斯陆三人领奖照
- 404 则用 Wikipedia REST API page/summary 查 infobox 原图名，再不行用装饰圆占位

### 第 4 步：和平事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | palestinian nationalism | 巴勒斯坦民族运动 | 法塔赫创建与 PLO 领导 | 封面、核心页 |
| 1 | peace negotiation | 和平谈判 | 马德里/奥斯陆/戴维营/怀伊河 | 奥斯陆页 |
| 2 | diplomacy | 外交 | 1974 联大演讲、国际承认 | 联大页 |
| 3 | state building | 自治政府建设 | PNA 机构组建与 1996 普选 | PNA 页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Suha Arafat | 无向 | 1990 结婚，育女 Zahwa |
| co-honored | Yitzhak Rabin | 无向 | 1994 诺贝尔和平奖共同得主 |
| co-honored | Shimon Peres | 无向 | 1994 诺贝尔和平奖共同得主 |
| colleague | Mahmoud Abbas | 无向 | PLO 继任者；2003 任其总理 |
| colleague | Salah Khalaf | 无向 | 长期副手 Abu Iyad |
| colleague | Khalil al-Wazir | 无向 | 长期副手 Abu Jihad，1988 遇刺 |
| controversy | Hafez al-Assad | 无向 | 叙利亚总统，关系长期不睦（1966 判决风波至黎巴嫩对峙） |

### 第 5 步：设计配色方案 【人物专属，主色勿改】

- **主色**：深松绿 `#0B5351`（橄榄枝与土地）+ 诺奖香槟金 `C9A227`
- badgeA 巴勒斯坦民族运动 — 深红 `#7E1E23`；badgeB 和平谈判 — 靛蓝 `#2F4470`；badgeC 外交 — 赭金 `#B08D2E`；badgeD 自治政府建设 — 深青 `#175E54`
- **背景母题**：橄榄枝与黑白几何纹（keffiyeh 图案抽象化），光束指向握手剪影

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）与国籍行（底部状态栏 `国籍 | 机构 | 主要奖项` 三要素）。
2. 必须有身份信息页（★ 必做）：左头像 + 右信息网格（生卒、本名、国籍、出生地、教育、任职、荣誉、核心事业）。
3. 结尾页品牌统一 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 巴勒斯坦事业的化身 / Yasser Arafat 1929–2004 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  和平事业概览 — 巴勒斯坦民族运动 / 和平谈判 / 外交 / 自治政府建设
04  早年：开罗与耶路撒冷 (1929–1948) — 政治世家、土木工程、1948 参战
05  学生领袖与法塔赫创建 (1952–1967) — GUPS、科威特、法塔赫立
06  卡拉迈与 PLO 主席 (1968–1970) — 时代封面、1969 当选
07  黑九月与黎巴嫩岁月 (1970–1982) — 转移、联大演讲、黎巴嫩内战
08  突尼斯与转变 (1983–1992) — 木腿行动、1988 建国宣言与放弃恐怖主义
09  奥斯陆（核心贡献页）— 密谈、交换承认、1993 白宫握手
10  诺贝尔和平奖 1994 — 三人共享、颁奖词
11  PNA 岁月 (1994–2000) — 回加沙、1996 普选、怀伊河、戴维营
12  围困与晚年 (2001–2004) — Mukata'a、Abbas 任总理、病逝克拉马
13  死因争议 — 三方调查结论并陈（只述事实）
14  争议与遗产 — 两面评价并陈、身后纪念
15  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 无载禁写 | 凡 page.md 未载的细节一律不写；不从颁奖词反推关系 |
| 引语白名单 | 仅可用 page.md 明载英文原句：橄榄枝句（1974 联大）、卡拉迈「We want to convince the world...」句、1988-08 旧语（作对比时）、耶路撒冷「先知亚伯拉罕之前」句；引语不得改写 |
| 政治敏感红线 | 以色列-巴勒斯坦冲突内容一律按 page.md 客观事实记录（含恐怖袭击指控、慕尼黑事件、黑九月、财政争议、两面评价），不加任何评价性语句、不作单侧叙事 |
| 生年口径 | page.md 作 4 or 24 August 1929（frontmatter 08-04），正文统一写「c. 1929 年 8 月」或 08-04 并注明两说 |
| 本名与绰号 | 全名 Mohammed Abdel Rahman Abdel Raouf Arafat al-Qudwa al-Husseini；Yasser 为 1950 年代自取名；Abu Ammar 为 nom de guerre——三者勿混 |
| 三人共享 | 1994 三人共享同一句理由（they），挪威委员会成员 Kåre Kristiansen 抗议辞职为 page.md 明载事实，只述事实 |
| 死因争议 | 瑞士（钋测得/可疑支持）、法国（环境性钋铅痕迹）、俄罗斯（自然原因）三方结论并陈，2015 法国检方结案——禁写任何「被害/未被暗杀」的定论 |
| 副手称呼 | Salah Khalaf=Abu Iyad、Khalil al-Wazir=Abu Jihad，库内用本名形式入库，note 里注阿拉伯绰号 |
| 反对手方 | 库内无 Amin al-Husseini、Saddam Hussein 等关系的入库口径，无载禁建关系；al-Assad 只建 controversy 一条 |
| 与批次 18 | 1993 Mandela 与 de Klerk 的共享年份与本篇无关，勿误写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| PLO (Palestine Liberation Organization) | 巴勒斯坦解放组织 | 与 PNA/Fatah 区分 |
| Fatah | 法塔赫 | 巴解主流派 |
| PNA (Palestinian National Authority) | 巴勒斯坦民族权力机构 | 1994 设立 |
| Oslo Accords | 奥斯陆协议 | Oslo I 1993 / Oslo II 1995 |
| kunya | 阿拉伯尊称（Abu Ammar） | 非本名 |
| keffiyeh | 凯菲耶头巾 | 个人标志 |
| intifada | 大起义 | 一起 1987 / 二起 2000 |
| two-state solution | 两国方案 | 1988 转向后立场 |
| Mukata'a | 拉姆安拉官邸 | 2001–04 围困地 |
| polonium | 钋 | 死因调查争议元素 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配勿改】

- **选定曲目**: **Ascension** — Cold Cinema
- **风格**: 电影感 / 上行推进 / 戏剧张力
- **匹配理由**: 「Ascension（攀升）」贴合阿拉法特的一生轨迹——从流亡学生到卡拉迈崛起、联大讲台、再到奥斯陆领奖台与总统府；上行旋律对应其从战士到谈判者的身份转换，也容纳其争议性人生的厚重感
- **本地路径**: `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Yasser_Arafat/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。**

---

## 六、执行清单 【模板通用，逐项勾选】

- [ ] 第 0 步：通读 page.md 全文，核对本文件「事实基准」与正文一致（重点核对生年两说与三个主席职位任期）
- [ ] 第 1 步：确认目录 `Yasser_Arafat/`（含 `images/`）存在
- [ ] 第 2 步：复制 Makefile，改 `MAIN` / `VIDEO_NAME` 为 `Yasser_Arafat_zh`
- [ ] 第 3 步：下载肖像并 `file` 验证格式；404 则 REST API 查 infobox 原图名；再不行装饰圆占位
- [ ] 第 4 步：按领域表写入 `MySQL/data/Yasser_Arafat.yaml` 的 `fields`（4 条，rank 0–3）
- [ ] 第 4.5 步：按社会关系表写入 yaml `relations`（7 条；对手方用本名，绰号入 note）
- [ ] 第 5 步：tex 头部宏定义配色（主色 #0B5351 + C9A227 + badgeA–D 四分类色），宏名统一 `mainclr/accentclr/badgeA..D`，注释写语义
- [ ] 第 6 步：按幻灯片序列逐页定义 `\newcommand{\xxxslide}`（宏名禁数字、禁 `\u00b7`）
- [ ] 第 7 步：编译循环：`make distclean && make`（latexmk 多遍），0 error、vbox≤10pt、hbox≤50pt
- [ ] 第 8 步：`pdftoppm` 逐页目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标
- [ ] 第 9 步：史实审查（对照陷阱表逐条核，死因三说并陈、引语白名单逐句核对）+ 术语审查（对照术语清单核译名）
- [ ] 收尾：`make pdf` 后核对页数与第 6 步规划一致；`make images && make video` 出 mp4

---

## 七、版式补遗 【模板通用，OpenPeace 沉淀】

- 表格页安全负间距：顶部 −0.35cm、`arraystretch 0.78–0.82`、公式框前 −0.35~−0.55cm（条目多时 −0.45cm 起）
- honors 类页 itemize 用 `\itemsep −2.5pt + topsep 0 + arraystretch 0.58` + 顶部 −0.55cm 压 4 条目（−0.65cm 会遮副标题）
- `leg` 节点 `x=±5.4cm` 的固有 hbox 8–9pt 属模板继承，不需修；时间线 `\foreach` 分隔符必须 ASCII 逗号
- keffiyeh 黑白几何纹做装饰元素时降低不透明度（30% 以下），避免与正文文字抢对比
- 阿拉伯人名转写统一用 page.md 英文拼写（al-Qudwa/al-Husseini），勿自行改用其他转写系统

---

## 八、入库回查清单 【模板通用】

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 -c "
from db_mysql import get_conn
conn=get_conn(); cur=conn.cursor()
cur.execute(\"SELECT id,name_en,has_social_data FROM people WHERE qid='Q34211'\")
p=cur.fetchone(); print(p)
cur.execute('SELECT COUNT(*) FROM person_field WHERE person_id=%s',(p[0],)); print('fields:',cur.fetchone()[0])
cur.execute('SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s',(p[0],p[0])); print('relations:',cur.fetchone()[0])"
```

- 预期：`has_social_data=1`、fields=4、relations=7；并发撞字典表唯一键（Duplicate entry）等 2 秒重跑一次（幂等）
