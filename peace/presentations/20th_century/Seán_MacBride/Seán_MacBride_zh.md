# 和平奖得主立传提示词（人物专属实例：Seán MacBride）

> 本文件是 OpenPeace 的「和平奖得主立传提示词」，以 Seán MacBride（肖恩·麦克布赖德，1974 诺贝尔和平奖，人权活动家）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 旗下与 physicist/chemist/medic/literature 平级）。
- **模板来源**：Kenneth_G_Wilson_zh.md 结构母本 + 和平奖项目共享工作流 `peace/PROMPTS_WORKFLOW.md`。
- **本实例**：Seán MacBride（1904–1988，爱尔兰政治家、外交官、律师与人权活动家）。
- **设计哲学**：和平奖立传同样需要「身份信息页」与「事业领域」结构化表达；本篇的最大特色是「一生两次转身」——从 IRA 参谋长到人权国际主义者，视觉叙事以「转身」为母题；北爱尔兰相关内容只作客观事实记录。

---

## 二、背景信息 【人物专属】

- **目标人物**：Seán MacBride（1904-01-26 生于巴黎 ~ 1988-01-15 卒于都柏林，享年 83 岁）
- **诺奖年份与官方获奖理由**（1974，与 Eisaku Satō 共享；英文原文照抄 `peace/nobel_peace_citations.json`，中译照抄名录，禁止改写）：
  > "for his efforts to secure and develop human rights throughout the world"（表彰他为在全世界保障与发展人权所做的努力）
  > （诺奖委员会另评其 "mobilised the conscience of the world in the fight against injustice"——page.md 明载转述，可用）
- **气质关键词**：**从革命者到人权活动家、国际人权机制的缔造者、两大和平奖双料得主**
- **设计母题**：**转身与桥梁（turning & bridges）**——从武装斗争转身走向法治与人权；连接爱尔兰与日内瓦、欧洲与非盟的桥梁意象。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Seán_MacBride/page.md`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准（已按 page.md 核对）

- **生卒**：1904-01-26 生于巴黎；1988-01-15 卒于都柏林（84 岁生日前 11 天）；葬 Glasnevin 公墓（母亲与亡妻墓旁）。
- **国籍**：生于法国巴黎（首语为法语，终身带法语口音），爱尔兰政治家（Nobel 名录 country=Ireland）。
- **家庭**：父 Major John MacBride（爱尔兰旅旅长， Boer 战争抗英，1916 复活节起义后遭英军处决）；母 Maud Gonne（Inghinidhe na hÉireann 与 Cumann na mBan 创始成员，爱尔兰民族主义著名人物）；同母异父妹 Iseult Gonne。1925-01 与 Catalina "Kid" Bulfin 结婚（m. 1924–1976，妻子 1976 去世），育二人。
- **教育**：巴黎耶稣会 Lycée Saint-Louis-de-Gonzague → 1916 父就义后入爱尔兰 Mount St Benedict's（Gorey）/ Downside School → University College Dublin 学法律（1924 出狱后），1937 取得律师资格（called to the bar）。
- **主要任职（政务）**：1936–1937 任 IRA 参谋长；1937 爱尔兰宪法生效后退出 IRA，改行律师（常为 IRA 犯人辩护）；1946 创建 Clann na Poblachta 党并任党魁（1946–1965）；1947 补选当选 TD；1948–1951 任外交部长（联合政府，Taoiseach 为 John A. Costello）；1948–1951 任 OEEC 副主席；1950 任欧洲理事会外长会议主席；1947–1957 任众议员（TD）；1957/1961 竞选失败后退出政坛。
- **国际任职（人权事业）**：1961 共同创建 Amnesty International 并任国际主席（1961–1975）；1963 协助起草非洲统一组织（OAU）宪章；1963–1971 任国际法学家委员会（ICJ）秘书长；1968/1975 任国际和平局（International Peace Bureau, Geneva）主席（至 1985）；1973–1977 由联大选出任联合国纳米比亚专员（助理秘书长级）；1977–1980 任 UNESCO 国际传播问题研究委员会主席（1980 产出 MacBride Report）；1982 任以色列侵黎国际调查委员会主席（1983 报告《Israel in Lebanon》）；1980s 发起「律师反核战呼吁」推动 ICJ 核武器合法性咨询意见（1996 下达）。
- **关键荣誉**：Nobel Peace Prize 1974；Lenin Peace Prize 1975–76（因反对「绝对淫秽的军备竞赛」——本人措辞，page.md 明载）；UNESCO Silver Medal for Service 1980；Golden Plate Award 1978。与 Linus Pauling 为仅有的两位「列宁和平奖+诺贝尔和平奖」双料得主（page.md 明载）。
- **晚年爱尔兰事务**：1977 与 Desmond Boal 共同担任 PIRA 与 UVF 联邦方案秘密调解人；1981 主编爱尔兰刑罚制度调查报告《Crime and Punishment》；1984 联名提出 MacBride Principles（北爱公平雇佣原则，促成英美立法）。
- **关键时间线（18 节点）**：1904 生巴黎 → 1916 父就义、赴爱尔兰求学 → 1918 为 Sinn Féin 助选 → 1919 15 岁谎报年龄加入 Irish Volunteers → 1921 反对英爱条约、内战被囚 → 1924 出狱入 UCD 学法律 → 1925 与 Catalina Bulfin 结婚 → 1927 回都柏林任 IRA 情报部长 → 1931 创 Saor Éire → 1936–1937 任 IRA 参谋长 → 1937 取得律师资格并退出 IRA → 1946 创建 Clann na Poblachta → 1948–1951 任外交部长 → 1950 推动欧洲人权公约（罗马签署 1950-11-04）→ 1961 共同创建 Amnesty International → 1963–1971 任 ICJ 秘书长 → 1974 获诺贝尔和平奖 → 1977–1980 任 UNESCO 传播委员会主席 → 1988-01-15 卒于都柏林。

### 第 4 步：事业领域表（与 yaml `fields` 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | human rights | 人权 | Amnesty International、MacBride Principles | 核心页 |
| 1 | international law | 国际法 | 国际法学家委员会秘书长、OAU 宪章 | 国际组织页 |
| 2 | diplomacy | 外交 | 爱尔兰外交部长、联合国纳米比亚专员 | 政务页 |
| 3 | politics | 政治 | Clann na Poblachta 党魁、TD | 政党页 |
| 4 | peace activism | 和平运动 | 国际和平局主席、反核战呼吁 | 国际组织页 |

### 第 4.5 步：社会关系表（与 yaml `relations` 完全一致）

| 关系类型 | 对方（name_en） | 方向 | note |
|---------|------|------|------|
| parent-child | John MacBride | 无向 | 父，1916 复活节起义后遭英军处决 |
| parent-child | Maud Gonne | 无向 | 母，爱尔兰民族主义运动著名人物 |
| spouse | Catalina Bulfin | 无向 | 1925 结婚（m. 1924–1976） |
| co-honored | Eisaku Satō | 无向 | 1974 诺贝尔和平奖共同得主 |
| colleague | Éamon de Valera | 无向 | 曾任其私人秘书，同游罗马 |

### 第 5 步：配色方案 【manifest 预分配，勿改】

- **主色**：`#0B5351`（深青绿——从武装到法治的沉静转身）
- **诺奖香槟金**：`#C9A227`
- **四分类色（badgeA–D）**：badgeA 人权事业 `#1E6B5A`；badgeB 国际法 `#2F4F6F`；badgeC 爱尔兰政务 `#5C4A1E`；badgeD 和平运动 `#6E3B2B`
- **背景母题**：桥梁拱线 + 法典条文淡纹（呼应「转身与桥梁」母题）

### 第 6 步：幻灯片序列（14 页规划，含身份信息页★必做）

```
00  OpenPeace 项目首页（共享封面）
01  封面 — 从革命者到人权活动家 / Seán MacBride 1904–1988 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、家庭、教育、任职、荣誉、核心领域）
03  巴黎童年与父辈 (1904–1916) — 父 Boer 战争、1916 就义、母 Maud Gonne
04  革命年代 (1918–1937) — Irish Volunteers、内战被囚、IRA 情报部长→参谋长
05  律师生涯 (1937–1946) — 出庭辩护、Portlaoise 监狱条件公案
06  政党与外交部长 (1946–1951) — Clann na Poblachta、欧洲人权公约、爱尔兰共和国法案
07  退出政坛与转身 (1951–1961) — 律师执业、JUSTICE 创建
08  人权事业的黄金年代 (1961–1975)（核心页）— Amnesty International、ICJ、国际和平局
09  联合国与 UNESCO (1973–1985) — 纳米比亚专员、MacBride Report
10  1974 诺贝尔和平奖（★ 必做专页）— 获奖理由、与佐藤荣作共享、双料和平奖（Pauling 并列）
11  晚年爱尔兰事务 (1977–1988) — 秘密调解、MacBride Principles、刑罚报告
12  遗产 — MacBride Prize、Seán MacBride House、纳米比亚街道命名
13  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

- **版式**：对齐 Kenneth_G_Wilson 模板骨架；vbox≤10pt、hbox≤50pt；爱尔兰语变音符（á/é/í）与越南语不同，XeLaTeX 主字体即可渲染，仍须单页试渲染。
- **陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方为 "for his efforts to secure and develop human rights throughout the world"，勿把委员会评语 "mobilised the conscience..." 混入获奖理由句 |
| 共享对象 | 1974 与 Eisaku Satō 共享；勿与 1973 Kissinger/Thọ 混淆 |
| 双料和平奖 | 与 Linus Pauling 并列双料得主——Pauling 只是并列事实，**不入库建关系** |
| 父母身份 | 父 John MacBride（Boer 战争爱尔兰旅长+1916 就义）、母 Maud Gonne；勿写成岳父母或混淆 Iseult Gonne 为全妹（同母异父妹） |
| 结婚年份 | page.md 正文作 1925-01（21 岁生日），infobox 作 m. 1924；yaml note 用「1925 结婚（m. 1924–1976）」并存口径 |
| IRA 经历 | 1936–1937 参谋长一段是 page.md 明载事实，客观记录；1920s 与苏联情报合作仅按 page.md 摘要一句，不展开 |
| 不入库项 | Francis Boyle/Hans Köchler（反核呼吁合作者，仅叙述）、Desmond Boal（调解搭档，仅叙述）、Linus Pauling（并列事实非关系） |
| 卒日 | 1988-01-15，84 岁生日前 11 天，葬 Glasnevin 公墓 |

### 第 9 步：术语审查

| 英文 | 中文 | 风险 |
|------|------|------|
| Amnesty International | 国际特赦组织 | 1961 共同创建，勿写「创始人」（page.md 用 co-founder） |
| International Commission of Jurists | 国际法学家委员会 | 秘书长 1963–1971 |
| International Peace Bureau | 国际和平局 | 日内瓦，1975–1985 主席 |
| European Convention on Human Rights | 欧洲人权公约 | 1950-11-04 罗马签署 |
| Clann na Poblachta | 共和氏族党 | 1946 创建 |
| Teachta Dála (TD) | 众议员 | 1947–1957 |
| MacBride Report | 麦克布赖德报告 | 1980 UNESCO 传播报告 |
| MacBride Principles | 麦克布赖德原则 | 1984 北爱公平雇佣 |
| UN Commissioner for Namibia | 联合国纳米比亚专员 | 1973–1977 |
| Glasnevin Cemetery | 格拉斯内文公墓 | 安葬地 |

---

## 四、背景音乐 ✅ 【manifest 预分配，勿改】

- **选定曲目**：**Ascension** — Cold Cinema（inspiring-electronic 曲库）
- **匹配理由**：自低处向高处的上升旋律线，匹配「从武装革命的地下岁月拾级而上、抵达国际人权事业的殿堂」的两次转身叙事；"Ascension" 亦呼应其晚年作为「世界良知动员者」的精神高度。
- **本地路径**：`music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`
- **时长处理**：ffmpeg `-shortest` 自动对齐视频长度。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Seán_MacBride/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录（中译获奖理由照抄源） |
| `peace/nobel_peace_citations.json` | 官方英文获奖理由 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/PROMPTS_WORKFLOW.md` | 共享工作流与红线 |
| `MySQL/data/Seán_MacBride.yaml` | 入库 yaml（fields/relations 与本文一致） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
