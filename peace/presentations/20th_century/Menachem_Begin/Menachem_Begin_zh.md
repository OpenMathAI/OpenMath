# 和平奖得主立传提示词（OpenPeace：Menachem Begin）

> **本文件是 OpenPeace 的「诺贝尔和平奖得主立传提示词」**，以 Menachem Begin（1978 诺贝尔和平奖，以色列总理）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），按 OpenPeace 立传执行。
> ★ 本篇涉及中东政治，全部内容只作 page.md 明载的客观事实记录，不加任何评价性语句。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他人物侧共享 GitHub）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词 + tex 结构）与和平奖侧批次经验。
- **本实例**：Menachem Begin（梅纳赫姆·贝京，以色列总理 1977–1983）。
- **设计哲学**：政治家立传必须有「身份信息页」（Identity / Bio 速览页），且强调「事业领域」的结构化表达——这两点构成骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Menachem Begin（1913-08-16 ~ 1992-03-09，享年 78 岁；生于俄罗斯帝国 Brest-Litovsk（今白俄罗斯布列斯特），卒于特拉维夫）
- **官方获奖理由（1978，与 Anwar Sadat 共享）**：
  > "for jointly having negotiated peace between Egypt and Israel in 1978."
  > （中译照抄名录：表彰二人共同谈判促成 1978 年埃及与以色列之间的和平）
- **气质关键词**：**从地下领袖到谈判桌的政治家、埃以和约的签署者、功成身退的隐居者**
- **设计母题**：**从地下室到草坪（from the underground to the lawn）**。从 MI5 悬赏 10,000 英镑的通缉者到 1979 年白宫草坪的签约人——以「隐匿的名字与公开的握手」对置作为视觉母题。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Menachem_Begin/page.md`
- **参考模板**：
  - 立传成品参照：OpenMathAI 各侧 15–16 页 Beamer（封面 `\input` 项目首页）
  - 项目封面模板：OpenPeace 侧共享 `cover/` 目录

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已按 page.md 核对）【人物专属】

- 生卒：1913-08-16 生于 Brest-Litovsk，家中三子女最幼；父 Zeev Dov、母 Hassia（姓氏原拼 Begun）；1992-03-09 卒于特拉维夫（3 月 3 日心脏病发作入院，9 日凌晨 3:30 去世）
- 家庭：妻 Aliza Arnold（1939-05-29 结婚，1982-11 去世）；子女 3 人：Binyamin（Benny Begin）、Leah、Hassia；母系出自拉比世家；父为木材商、犹太复国主义者、Herzl 崇拜者
- 大屠杀：1941 年 6 月底父亲与布列斯特 5,000 名犹太人一道被杀；母亲与长兄 Herzl 亦罹难
- 教育：cheder 传统教育 → Tachkemoni 学校 → 14 岁入波兰公立学校 → 16 岁加入 Betar（13 岁前属 Hashomer Hatzair）→ 华沙大学法学院 1935 年毕业（未执业律师），练就演说与修辞
- 关键经历：Jabotinsky 的追随者；1937 年 Betar 捷克斯洛伐克负责人、后任波兰分部负责人 → 1940-09-20 被苏联 NKVD 逮捕、判 8 年古拉格、Pechora 劳改营（回忆录《White Nights》）→ 1941 依 Sikorski–Mayski 协议获释、以列兵军士身份加入波兰 Anders 军 → 1942-05 随军抵巴勒斯坦 → 1942-12 退出 Anders 军加入 Irgun → 1944-02-01 宣布对英国委任统治当局起义并任 Irgun 领袖（国王大卫酒店爆炸案 91 人死亡；MI5 悬赏 10,000 英镑；化名「拉比 Sassover」「Yisrael Halperin」「Dr. Yonah Koenigshoffer」等隐匿）→ 1948-06 Altalena 事件 → 1948-08 创 Herut 党 → 1949 首届 Knesset 议员（14 席）→ 1952 赔偿协定风波（被禁足 Knesset 数月）→ 1953–1955 英国拒发入境签证（1972 获签）→ 1965 组 Gahal → 1967 六日战争入团结政府任不管部长（至 1970-08 因 Rogers 计划退出）→ 1973 组 Likud → 1977 大选胜利、6-21 就任总理（结束工党三十年主导）→ 1978 戴维营协议（外长 Dayan、防长 Weizman 协同，Carter 斡旋）→ 1978 诺贝尔和平奖 → 1979-03-26 签署埃以和平条约 → 1981-06-07 批准轰炸伊拉克 Osirak 反应堆（Operation Opera，Begin Doctrine）→ 1982-06 入侵黎巴嫩 → 1982-09 Sabra 与 Shatila 事件后 Kahan 委员会（1983-02 报告）→ 1982-11 妻 Aliza 去世 → 1983-10 辞职（交棒 Shamir）→ 隐居耶路撒冷 → 1992-03-09 卒，葬于橄榄山犹太公墓（与妻合葬，从简不从国葬，约 7.5 万人送葬）
- 著作：《The Revolt》（起义回忆）、《White Nights: The Story of a Prisoner in Russia》（古拉格回忆）
- 关键荣誉：诺贝尔和平奖（1978，与 Sadat 共享）
- 关键时间线（16 节点）：1913 生于布列斯特 → 16 岁入 Betar → 1935 华沙大学法学毕业 → 1939 结婚、战争爆发流亡维尔纽斯 → 1940 NKVD 逮捕、古拉格 → 1942 抵巴勒斯坦、入 Irgun → 1944 领导 Irgun 宣布起义 → 1948 Altalena 事件、创 Herut → 1949 首届 Knesset → 1967 入团结政府 → 1973 创 Likud → 1977 就任总理 → 1978 戴维营、诺贝尔和平奖 → 1979 埃以和约 → 1982 黎巴嫩战争与丧妻 → 1983 辞职 → 1992 卒于特拉维夫

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下建 `Menachem_Begin/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目近邻成品 Makefile，设 `MAIN=Menachem_Begin_zh`、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【人物专属】

- page.md 载 1978 年官方像、1940 年 NKVD 档案照、1932 年全家福、与 Sadat 的国会联席会议照、与 Brzezinski 对弈照、橄榄山纪念铭牌等；按 images.txt/REST API 下载，404 则用装饰圆占位

### 第 4 步：事业领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace negotiation | 和平谈判 | 戴维营协议与埃以和约 | 核心页 |
| 1 | politics | 政治治理 | 总理任期、Herut/Likud 创建与领导 | 政治页 |
| 2 | zionism | 犹太复国主义 | Betar 与修正主义传统 | 早年页 |
| 3 | guerrilla warfare | 地下武装斗争 | Irgun 领袖时期（按 page.md 客观记录） | 起义页 |
| 4 | diplomacy | 外交 | 对美对埃谈判、华盛顿签约 | 外交页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Anwar Sadat | 无向 | 1978 诺贝尔和平奖共同得主，埃以和约签署双方 |
| spouse | Aliza Begin | 无向 | 1939 年结婚，1982 年去世；死后与夫合葬橄榄山 |
| influence | Ze'ev Jabotinsky | 对方→本人 | 修正主义锡安主义创始人，Betar 时期的精神导师（page.md 载 disciple） |
| colleague | Jimmy Carter | 无向 | 斡旋戴维营协议并促成埃以和约；首会时「tertiated」一词对话 |
| colleague | Moshe Dayan | 无向 | 外长，1978 年协同赴华盛顿与戴维营谈判 |
| colleague | Ezer Weizman | 无向 | 防长，1978 年协同谈判 |
| colleague | Ariel Sharon | 无向 | 1973 年促成 Likud 组建方案，后任其防长 |
| colleague | Yitzhak Shamir | 无向 | 老战友，1983 年接任总理 |
| rival | David Ben-Gurion | 无向 | Altalena 事件结怨；长期拒绝与其对话或提名（page.md 明载） |

### 第 5 步：设计配色方案 【人物专属，勿改主色】

- **主色**：`#7A1E28`（深绯红——历史纵深与凝重）
- **辅色**：诺奖香槟金 `C9A227` + 四分类色：badgeA 和平谈判 `#2E5F7A`；badgeB 政治 `#8C6A2F`；badgeC 早年地下岁月 `#5B4A6B`；badgeD 外交 `#2E7D6B`
- **背景母题**：从地下室到草坪的对置剪影

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有肖像（或装饰圆占位）+ 姓名小字注；顶部/底部明示国籍（Israel）。
2. 必须有身份信息页：左肖像 + 右信息网格（生卒、家庭、教育、任职、著作、荣誉、核心领域）。
3. 结尾页品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00 OpenPeace 项目首页（\input cover 共享页）
01 封面 — 1978 诺贝尔和平奖 / Menachem Begin 1913–1992 + badge + 国籍行
02 身份信息页（★ 必做）
03 核心贡献概览 — 起义领袖 / 政治反对派 / 总理 / 埃以和约
04 早年：布列斯特与 Betar (1913–1939) — 家世、华沙大学法学、Jabotinsky 之门
05 古拉格与抵达 (1939–1942) — NKVD、《White Nights》、Anders 军、巴勒斯坦
06 Irgun 领袖与反英起义 (1944–1948) — 宣言、国王大卫酒店事件、化名岁月（客观记录）
07 建国之初 (1948–1952) — Altalena 事件、创 Herut、首届 Knesset、赔偿协定风波
08 三十年的反对派 (1952–1977) — Gahal、团结政府、Likud、1977 变天
09 1977 大选胜利 — 结束工党三十年主导、就任总理
10 戴维营 (1978) — Dayan/Weizman 协同、Carter 斡旋、tertiated 轶事
11 诺贝尔和平奖与埃以和约 (1978–1979) — 共享理由句、1979-03-26 华盛顿签署、西奈归还
12 总理任内其他大事 — 定居点扩建、Osirak 轰炸与 Begin Doctrine、黎巴嫩战争（客观记录）
13 退场 (1982–1983) — Sabra 与 Shatila 及 Kahan 委员会（客观记录）、丧妻、辞职
14 隐居与晚年 — 耶路撒冷隐居、1992 病逝、橄榄山从简安葬
15 遗产 — 埃以和约延续至今、The Revolt / White Nights 两部回忆录
16 结尾
```

### 第 7–8 步：Beamer 编写 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；写完即 make，`pdftoppm` 截图查溢出；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Menachem Begin 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 政治红线 | Irgun 武装活动、Deir Yassin、定居点、Osirak 轰炸、黎巴嫩战争、Sabra 与 Shatila 等议题一律只作 page.md 明载的客观事实记录，禁任何评价、辩护或谴责性语句；批评方（如 1948 年 Einstein 等公开信）与官方调查结论只能客观并列，均不进引文框 |
| 获奖口径 | 1978 诺贝尔和平奖与 Sadat 共享，理由句 "jointly having negotiated peace between Egypt and Israel in 1978"；勿把获奖写成"因其全部政治生涯" |
| 生卒日期 | 卒日 1992-03-09（3 月 3 日心脏病发作入院，勿把入院日当卒日）；生地 Brest-Litovsk 时属俄罗斯帝国（今白俄罗斯布列斯特） |
| 姓氏拼写 | 父母姓氏原拼 Begun（Zeev Dov 与 Hassia Begun）；本人通拼 Begin——家世段如实写，勿改 |
| 学位 | 华沙大学法学毕业（1935），从未执业——勿写成律师执业者 |
| 与 Sadat 篇对表 | 两篇共享同一理由句与华盛顿签约事件；Begin 篇亮点是"从地下领袖到签约人"的转变与后续争议，Sadat 篇亮点是"首位跨线访问的阿拉伯领导人"——勿互相写串 |
| Altalena 事件 | 1948 年 6 月，16 名 Irgun 战士与 3 名 IDF 士兵死亡（数字按 page.md）；事件是与 Ben-Gurion 关系恶化的起点 |
| 英国禁入境 | 1953–1955 拒发签证（因"臭名昭著的恐怖组织领导人"定性）、1972 获签——两段勿混为一段 |
| 大屠杀家史 | 父母与长兄均罹难——客观记录；「tertiated」（三去其一）一词源于此，可作花絮页小注 |
| 晚年 | 1983-10 辞职后隐居，抑郁（据心理学者/秘书 Kadishai 转述口径）；1990 摔伤髋部后迁特拉维夫——按 page.md 客观记录 |
| 命名混淆 | 1992 年另有同年获诺奖者；「Begin Doctrine」是其 Osirak 轰炸后声明——术语表勿与其个人奖项混淆 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Irgun | 伊尔贡（民族军事组织） | 地下武装组织，全称 Etzel |
| Betar | 贝塔尔 | 修正主义锡安主义青年运动 |
| Revisionist Zionism | 修正主义锡安主义 | Jabotinsky 创立 |
| Herut | 赫鲁特（自由党） | 1948 年创立 |
| Likud | 利库德集团 | 1973 年联合组建 |
| Altalena Affair | 「阿尔塔莱纳」号事件 | 1948-06 |
| Camp David Accords | 戴维营协议 | 1978 |
| Egypt–Israel peace treaty | 埃以和平条约 | 1979-03-26 |
| Begin Doctrine | 贝京主义 | 1981 年 Osirak 轰炸后声明 |
| White Nights | 《白夜》 | 古拉格回忆录，勿与陀思妥耶夫斯基同名作混淆 |

---

## 四、背景音乐 ✅ 【人物专属，manifest 预分配，勿改】

- **选定曲目**: **PAST** — Alex-Productions
- **匹配理由**: 「往昔」贴合其人生底色——布列斯特的少年、古拉格的白夜、地下的化名岁月一路背负到 1979 年的草坪；深沉的历史感匹配从大屠杀家史到和平条约的漫长弧线。
- **本地路径**: `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → 复制为 `presentations/20th_century/Menachem_Begin/PAST.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Menachem_Begin/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译（照抄，禁改写） |
| `MySQL/data/Menachem_Begin.yaml` | 入库 yaml（第 4/4.5 步落地） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
