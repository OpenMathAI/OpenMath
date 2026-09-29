# 和平奖得主立传提示词（OpenPeace 实例：Yitzhak Rabin）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」实例**，以 Yitzhak Rabin（1994 诺贝尔和平奖，与阿拉法特、佩雷斯共同获奖）为对象。
> 凡标注 `【模板通用】` 的部分复用 OpenPeace 共享骨架；标注 `【人物专属】` 的部分为本人物专属内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 各学科侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：对齐物理学家侧标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` 的 0–11 节结构。
- **本实例**：Yitzhak Rabin（伊扎克·拉宾），以色列两任总理（1974–77、1992–95）、首位本土出生总理、1995-11-04 遇刺。
- **设计哲学**：和平奖得主立传必须有「身份信息页」与「和平事业结构化表达」；军人出身的和平缔造者是本篇叙事张力——将军与握手两个意象并置，只写事实，不作评价。

---

## 二、背景信息 【人物专属】

- **目标人物**：Yitzhak Rabin（1922-03-01 ~ 1995-11-04，享年 73 岁，遇刺身亡）
- **气质关键词**：**从将军到和平缔造者、务实的安全鹰派、奥斯陆的签署者** —— 1994 诺贝尔和平奖获奖理由：
  > "for their efforts to create peace in the Middle East"（表彰他们为在中东缔造和平所做的努力）
- **设计母题**：**放下枪的手**。1993-09-13 白宫握手与「血泪够了（Enough of blood and tears）」演说——视觉语言用握手剪影、橄榄枝、军帽与白鸽的对置构图。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Yitzhak_Rabin/page.md`（含 frontmatter QID Q34060）
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - OpenPeace 共享封面：`peace/presentations/cover/openpeace_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇到歧义先征求主控意见再继续。
> **数据库同步要求**：包含「和平事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1922-03-01 生于耶路撒冷 Shaare Zedek 医院（当时为英属巴勒斯坦托管地）~ 1995-11-04 逝于特拉维夫 Ichilov 医院（枪击遇刺，享年 73）
- 家庭：父 Nehemiah Rubitzov（乌克兰移民、美国转经、犹太军团志愿兵）；母 Rosa Cohen（明斯克出身、会计、特拉维夫市议会议员，1937 病逝）；妹 Rachel Rabin（1925–2026，基布兹 Manara 先驱、教育家）
- 教育：Tel Aviv Beit Hinuch Leyaldei Ovdim（1928–1935）→ 基布兹 Givat Hashlosha 农业学校（1935 入校，14 岁加入哈加纳受训）→ Kadoorie Agricultural High School（1937–1940-08 毕业；师长 Yigal Allon）；曾考虑 UC Berkeley 灌溉工程奖学金，最终留下
- 军旅：Palmach 作战处长（1948 战争）→ IDF 27 年职业军人，1959–1963 领导作战局 → 1964 任总参谋长（最高军衔 Rav Aluf），指挥 1967 六日战争 → 1968 退役
- 任职：驻美大使（1968–1973）→ 劳工部长（1974-03）→ 总理第一任期 1974-06-03–1977-06-21 → 国会议员（1974–1995）→ 国防部长（1984–1990，1992–1995）→ 总理第二任期 1992-07-13–1995-11-04
- 关键荣誉：诺贝尔和平奖 1994（与阿拉法特、佩雷斯共同）、里根自由奖、费利克斯·乌弗埃-博瓦尼和平奖、阿斯图里亚斯亲王国际合作奖、多所大学荣誉博士
- 核心事业清单：
  1. 第一任期：西奈临时协议签署、恩德培行动（1976）授权；1977 因妻子外汇账户风波辞职
  2. 国防部长任内（1984–90）：黎巴嫩撤军至安全区；第一次大起义爆发期在任
  3. 1992 以和平进程为纲领再胜选；1993-09-09 与 Arafat 交换承认信件（PLO 承认以色列、以色列承认 PLO）
  4. 1993-09-13 白宫签署奥斯陆一号协议；1994-10-26 与侯赛因国王签署约以和约（终结 46 年官方战争状态）
  5. 1994-12-10 与 Arafat、Peres 同获诺贝尔和平奖（奥斯陆）
  6. 国内改革：私有化、Yozma 风投计划（1993）、1995 国民健康保险法（全民医保）、教育支出 +70%
  7. 1995-11-04 特拉维夫国王广场和平集会遇刺身亡（凶手 Yigal Amir 反对奥斯陆协议，判终身监禁）；1995-11-06 葬于 Herzl 山
- 关键时间线（15–20 节点）：1922 生于耶路撒冷 → 1937 入 Kadoorie → 1940 毕业 → 1941 加入 Palmach → 1948 独立战争作战处长 → 1948 与 Leah 结婚 → 1950 长女 Dalia 生 → 1955 次子 Yuval 生 → 1964 总参谋长 → 1967 六日战争 → 1968–73 驻美大使 → 1974 总理（首次）→ 1977 辞职 → 1980 工党党魁挑战 Peres 落败 → 1984–90 国防部长 → 1992 再任总理 → 1993-09-13 奥斯陆一号 → 1994 约以和约 → 1994-12-10 诺奖 → 1995-11-04 遇刺 → 2000 遗孀 Leah 逝并合葬

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下确认 `Yitzhak_Rabin/` 与 `images/` 存在

### 第 2 步：复制 Makefile 【模板通用】

- 复制同侧已有成品目录 Makefile，设置 `MAIN=Yitzhak_Rabin_zh`、`VIDEO_NAME=Yitzhak_Rabin_zh`

### 第 3 步：收集图片 【人物专属】

- infobox 肖像 1994 年照（images.txt 有 URL 则直接取，250px 改 500px）；备用插图：1993-09-13 白宫三人握手照、1994 约以和约签署照
- 404 则用 Wikipedia REST API page/summary 查 infobox 原图名，再不行用装饰圆占位

### 第 4 步：和平事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace negotiation | 和平谈判 | 奥斯陆协议、约以和约 | 封面、核心页 |
| 1 | military leadership | 军事领导 | IDF 总参谋长、六日战争指挥 | 军旅页 |
| 2 | diplomacy | 外交 | 驻美大使（1968–73） | 大使页 |
| 3 | national security | 国家安全政策 | 两任国防部长 | 国防页 |
| 4 | economic reform | 经济改革 | 私有化、Yozma、全民医保 | 改革页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Leah Rabin | 无向 | 1948 结婚，2000 逝世合葬 Herzl 山 |
| parent-child | Dalia Rabin-Pelossof | 无向 | 长女，1999 入选议会 |
| parent-child | Yuval Rabin | 无向 | 次子 |
| co-honored | Yasser Arafat | 无向 | 1994 诺贝尔和平奖共同得主 |
| co-honored | Shimon Peres | 无向 | 1994 诺贝尔和平奖共同得主 |
| rival | Shimon Peres | 无向 | 工党领袖长期竞争者 |
| colleague | Hussein of Jordan | 无向 | 1994 约以和约签署对方 |

### 第 5 步：设计配色方案 【人物专属，主色勿改】

- **主色**：钢蓝 `#2F4470`（军装蓝与理性）+ 诺奖香槟金 `C9A227`
- badgeA 和平谈判 — 橄榄绿 `#175E54`；badgeB 军事领导 — 深蓝 `#1E3A5F`；badgeC 外交 — 赭金 `#B08D2E`;badgeD 国家安全 — 暗红 `#7E1E23`
- **背景母题**：握手剪影与白鸽光带，四色光斑交替

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框）与国籍行（底部状态栏 `国籍 | 机构 | 主要奖项` 三要素）。
2. 必须有身份信息页（★ 必做）：左头像 + 右信息网格（生卒、本名、国籍、出生地、教育、任职、荣誉、核心事业）。
3. 结尾页品牌统一 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 从将军到和平缔造者 / Yitzhak Rabin 1922–1995 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  和平事业概览 — 和平谈判 / 军事领导 / 外交 / 国家安全 / 经济改革
04  早年：耶路撒冷与特拉维夫 (1922–1941) — 移民家庭、农业学校、哈加纳受训
05  军旅三十年 (1941–1968) — Palmach、总参谋长、六日战争
06  大使与第一任期 (1968–1977) — 华盛顿岁月、西奈临时协议、恩德培、辞职
07  在野与国防部长 (1977–1992) — 1980 党魁之争、黎巴嫩撤军、大起义
08  重返总理府 (1992–1993) — 和平纲领胜选、承认信件交换
09  奥斯陆（核心贡献页）— 1993-09-13 白宫握手、Enough 演说
10  约以和约 1994 — 与侯赛因国王、终结 46 年战争状态
11  诺贝尔和平奖 1994 — 三人共享、颁奖词、诺奖演讲引语
12  国内改革 — 私有化、Yozma、全民医保
13  1995-11-04 遇刺 — 国王广场、Yigal Amir、Herzl 山国葬
14  遗产 — Rabin 广场、纪念中心、和平进程象征
15  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 无载禁写 | 凡 page.md 未载的细节一律不写；不从颁奖词反推关系 |
| 引语白名单 | 仅可用 page.md 明载英文原句：「Enough of blood and tears. Enough!」（1993 握手后演说）、「Military cemeteries... silent testimony...」（1994 诺奖演讲）、「I always believed that most of the people want peace...」（1995 集会）；引语不得改写 |
| 政治敏感红线 | 以色列-巴勒斯坦内容一律按 page.md 客观事实记录（六日战争、大起义镇压口径、奥斯陆反对声浪、刺杀事件），不加任何评价性语句 |
| 两任总理 | 1974-06-03–1977-06-21 与 1992-07-13–1995-11-04，勿混任次；首位本土出生（sabra）总理、唯一被刺杀的总理、Eshkol 之后第二位任内去世 |
| Peres 双重关系 | Peres 既是「长期政治竞争对手」（1980 党魁挑战、1974 接班之争）又是 1994 共同得主与内阁同僚——co-honored 与 rival 两条分立，勿混写一条 |
| 刺杀口径 | 1995-11-04（希伯来历 Heshvan 12）国王广场集会后遇刺，凶手 Yigal Amir 判终身监禁；「Shalom, haver」是 Clinton 悼词用希伯来语，勿写成 Rabin 语录 |
| 妹妹生卒 | Rachel Rabin 页面作 1925–2026，按本地照实 |
| 军衔译名 | Rav Aluf 为 IDF 最高军衔（常译中将/上将级），页内以「Rav Aluf（IDF 最高军衔）」呈现 |
| 金钱风波 | 1977 辞职原因是其妻 Leah 的美元账户风波（financial scandal），勿写成本人贪腐 |
| 反对手方 | Yigal Amir、Golda Meir、Yigal Allon 等不建关系（非白名单关系类型/无载禁建） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Palmach | 帕尔马赫突击队 | 哈加纳精锐 |
| IDF | 以色列国防军 | 首次出现用全称 |
| Rav Aluf | IDF 最高军衔 | 勿译「元帅」 |
| Knesset | 以色列议会 | 通行音译「克奈塞特」慎用 |
| Oslo Accords | 奥斯陆协议 | Oslo I 1993 / Oslo II 1995 |
| letters of recognition | 互相承认信件 | 1993-09-09 交换 |
| Israel–Jordan peace treaty | 约以和约 | 1994-10-26 |
| Kings of Israel Square / Rabin Square | 以色列诸王广场（今拉宾广场） | 刺杀地 |
| Yozma | Yozma 风投计划 | 1993 设立 |
| Sabra | 以色列本土出生者（沙布拉） | 首位 sabra 总理 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配勿改】

- **选定曲目**: **The Invisible Light** — Infraction
- **风格**: 纪录片 / 沉静 / 微光
- **匹配理由**: 「看不见的光」呼应设计母题——将军放下的枪、谈判桌上看不见的信任；纪录片气质匹配其两任总理的漫长弧线，微光感贴合 1995 年集会那盏熄灭于夜晚的和平之光
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Yitzhak_Rabin/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。**

---

## 六、执行清单 【模板通用，逐项勾选】

- [ ] 第 0 步：通读 page.md 全文，核对本文件「事实基准」与正文一致（重点核对两任总理起讫日与部长序列年份）
- [ ] 第 1 步：确认目录 `Yitzhak_Rabin/`（含 `images/`）存在
- [ ] 第 2 步：复制 Makefile，改 `MAIN` / `VIDEO_NAME` 为 `Yitzhak_Rabin_zh`
- [ ] 第 3 步：下载肖像并 `file` 验证格式；404 则 REST API 查 infobox 原图名；再不行装饰圆占位
- [ ] 第 4 步：按领域表写入 `MySQL/data/Yitzhak_Rabin.yaml` 的 `fields`（5 条，rank 0–4）
- [ ] 第 4.5 步：按社会关系表写入 yaml `relations`（7 条；Peres 的 rival 与 co-honored 两条分立）
- [ ] 第 5 步：tex 头部宏定义配色（主色 #2F4470 + C9A227 + badgeA–D 四分类色），宏名统一 `mainclr/accentclr/badgeA..D`，注释写语义
- [ ] 第 6 步：按幻灯片序列逐页定义 `\newcommand{\xxxslide}`（宏名禁数字、禁 `\u00b7`）
- [ ] 第 7 步：编译循环：`make distclean && make`（latexmk 多遍），0 error、vbox≤10pt、hbox≤50pt
- [ ] 第 8 步：`pdftoppm` 逐页目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标
- [ ] 第 9 步：史实审查（对照陷阱表逐条核，引语白名单逐句核对）+ 术语审查（对照术语清单核译名）
- [ ] 收尾：`make pdf` 后核对页数与第 6 步规划一致；`make images && make video` 出 mp4

---

## 七、版式补遗 【模板通用，OpenPeace 沉淀】

- 表格页安全负间距：顶部 −0.35cm、`arraystretch 0.78–0.82`、公式框前 −0.35~−0.55cm（条目多时 −0.45cm 起）
- honors 类页 itemize 用 `\itemsep −2.5pt + topsep 0 + arraystretch 0.58` + 顶部 −0.55cm 压 4 条目（−0.65cm 会遮副标题）
- `leg` 节点 `x=±5.4cm` 的固有 hbox 8–9pt 属模板继承，不需修；时间线 `\foreach` 分隔符必须 ASCII 逗号
- 军旅页时间线节点多（1941–1968 七节点），可用两行式 `\foreach` 或拆左右列，防底部溢出
- 希伯来文名 יִצְחָק רַבִּין 入封面时用 `\newfontfamily\hebrewfont[Script=Hebrew]{Arial Hebrew}`（参照 Wigderson 篇先例）

---

## 八、入库回查清单 【模板通用】

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 -c "
from db_mysql import get_conn
conn=get_conn(); cur=conn.cursor()
cur.execute(\"SELECT id,name_en,has_social_data FROM people WHERE qid='Q34060'\")
p=cur.fetchone(); print(p)
cur.execute('SELECT COUNT(*) FROM person_field WHERE person_id=%s',(p[0],)); print('fields:',cur.fetchone()[0])
cur.execute('SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s',(p[0],p[0])); print('relations:',cur.fetchone()[0])"
```

- 预期：`has_social_data=1`、fields=5、relations=7；并发撞字典表唯一键（Duplicate entry）等 2 秒重跑一次（幂等）
