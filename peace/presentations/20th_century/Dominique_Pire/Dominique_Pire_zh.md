# 和平奖得主立传提示词（OpenPeace：Dominique Pire）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Dominique Pire（1958 诺贝尔和平奖，比利时道明会士、战后欧洲难民援助者）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Dominique Pire（多米尼克·皮尔，1958 诺贝尔和平奖）——从比利时抵抗运动随军司铎到战后 60,000 名流离失所者的援助者，「让难民走出难民营」的实践者。
- **设计哲学**：保留「身份信息页」与「事业领域结构化表达」两大骨架；本篇叙事重心是**信仰与行动的分离**——他坚持不把个人信仰混入公共援助事业，以四家组织的接力构成「从救济到发展」的完整链条。

---

## 二、背景信息 【人物专属】

- **目标人物**：Dominique Pire, O.P.（俗名 Georges Charles Clement Ghislain Pire，1910-02-10 ~ 1969-01-30，享年 58 岁）
- **气质关键词**：**难民之友、行动的司铎、从救济到发展的先行者** —— 1958 诺贝尔和平奖获奖理由：
  > "for his efforts to help refugees to leave their camps and return to a life of freedom and dignity"（表彰他帮助难民走出难民营、回归自由与尊严生活的不懈努力）
- **设计母题**：**从难民营到村庄（from camp to village）**。以帐篷→房屋→田地的三级演进剪影、比利时蓝与暖橙构成视觉语言，呼应「帮助难民走出难民营、重建有尊严的生活」的核心事业。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Dominique_Pire/page.md`
- **参考模板**：标杆提示词 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；首页模板 `peace/presentations/cover/openpeace_page.tex`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：核对本地页面，建立事实基准 【人物专属】

- ✅ 页面已抓取（frontmatter：QID Q158850 / 生卒 / 国籍 Belgium / 职业 / 奖项 / 教育经历）
- **事实基准（第一轮已核对，全部以 page.md 为准）**：
  - 生卒：1910-02-10 生于比利时迪南（Dinant）~ 1969-01-30 逝于 Herent 的鲁汶天主教医院（前列腺手术并发症），享年 58 岁
  - 国籍：比利时
  - 家庭：四子之长；父 Georges Pire Sr. 为市政官员，母 Berthe (Ravet) Pire
  - 早年：1914 一战爆发随家乘船逃往法国，1918 停战后返回已成废墟的迪南
  - 教育：Collège de Bellevue 攻读古典学与哲学 → 18 岁入于伊（Huy）La Sarte 道明会修院 → 1932-09-23 发终身愿、取会名 Dominique（取自会祖）→ 罗马宗座国际学院 Angelicum 攻读神学与社会学，1936 以论文《L'Apatheia ou insensibilité irréalisable et destructrice》获神学博士（1934–1936）→ 1936–1937 鲁汶天主教大学
  - 任职主线：回 La Sarte 讲授社会学，致力于帮助贫困家庭有尊严地生活 → 二战任比利时抵抗运动随军司铎，参与协助盟军飞行员出境等活动，战后获多枚勋章 → 1949 起研究战后流离失所者问题并著书《Du Rhin au Danube avec 60,000 D. P.》→ 创办援助组织，1950 年代在奥地利与德国为难民建村 → 1958 获诺贝尔和平奖（Oslo，12 月，诺奖演讲 Brotherly Love: Foundation of Peace）→ 获奖后创办「和平大学」→ 后创办「和平之岛」投身发展中国家农村长期发展（孟加拉国、印度）
  - 关键荣誉：Nobel Peace Prize 1958；德国联邦功绩十字勋章（Commander's Cross）；比利时 1940–1945 战争十字勋章
  - 核心事业清单：① 战后流离失所者的家庭资助计划；② 奥地利/德国难民村建设；③ Service d'Entraide Familiale（困难者社会重返）；④ Université de Paix（家庭与职场冲突预防）；⑤ Islands of Peace（发展中国家农村长期发展，后扩展至布基纳法索/贝宁/马里/几内亚比绍/厄瓜多尔/玻利维亚/秘鲁）
  - 关键时间线（15–20 节点）：1910 迪南出生 → 1914 逃往法国 → 1918 返回废墟 → 1928 入 La Sarte 修院 → 1932 终身愿+会名 Dominique → 1934–1936 Angelicum 神学博士 → 1936–1937 鲁汶 → 1930s La Sarte 社会学教学与扶贫 → 1940–1945 抵抗运动司铎 → 1949 研究流离失所者 → 1950s 出版《Du Rhin au Danube》+ 创办组织 + 难民村 → 1958-12 诺贝尔和平奖与演讲 → 获奖后创办和平大学 → 创办 Islands of Peace → 孟加拉国/印度项目启动 → 1969-01-30 手术并发症去世 → 身后四组织持续运作；2008 牛津 Blackfriars Hall 设纪念项目

### 第 1–3 步：目录 / Makefile / 图片 【模板通用】

- 在 `peace/presentations/20th_century/Dominique_Pire/` 下建 `images/`；Makefile 复制同项目成品并设 `MAIN=Dominique_Pire_zh`
- 肖像：page.md 实载 1958 年诺贝尔领奖照（Georges_Pire_1958_nobel.jpg，Gunnar Jahn 授奖）；下载失败用装饰圆占位并记录

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | refugee aid | 难民援助 | 家庭资助与难民村，获奖核心 | 核心页 |
| 1 | humanitarian aid | 人道主义援助 | 战后流离失所者救济 | 事业页 |
| 2 | peace education | 和平教育 | 获奖后创办和平大学 | 获奖后页 |
| 3 | poverty reduction | 扶贫 | 和平之岛的发展项目 | 晚年页 |
| 4 | theology | 神学 | Angelicum 博士与社会学教学 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Georges Pire Sr. | 无向 | 父亲，迪南市市政官员 |
| parent-child | Berthe Ravet Pire | 无向 | 母亲 |
| founder | Service d'Entraide Familiale | 无向 | 创办，帮助困难者社会重返 |
| founder | Aide aux Personnes Déplacées | 无向 | 创办，援助难民并资助发展中国家儿童 |
| founder | Université de Paix | 无向 | 获奖后创办「和平大学」，预防家庭与职场冲突 |
| founder | Islands of Peace | 无向 | 创办「和平之岛」，发展中国家农村长期发展 |

> 只收 page.md 明载的关系：页面未载其婚姻与子嗣信息，禁写 spouse/parent-child（子女向）；Gunnar Jahn 仅为颁奖人，不入库；宗教会长上级未具名，不入库。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色（manifest 预分配，勿改）**：深红 `#8C1515`
- 辅色：诺奖香槟金 `#C9A227`
- 四分类色：`badgeCamp` 难民援助 — 靛蓝 `#1F3A5F`；`badgeAid` 人道援助 — 青绿 `#0E7C7B`；`badgePeaceEdu` 和平教育 — 琥珀 `#E07B30`；`badgeDev` 发展项目 — 橄榄绿 `#6B7F3A`
- **背景母题**：柔和气泡 + 帐篷→房屋→田地演进剪影，呼应「从难民营到村庄」

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）与国籍行。
2. 必须有身份信息页（★）：左头像 + 右信息网格（生卒、俗名与会名、国籍、出生地、教育、任职、主要荣誉、核心领域）。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 难民之友 / Dominique Pire 1910–1969 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心事业概览 — 难民资助 / 难民村 / 四家组织 / 和平大学
04  早年：迪南与战火童年 (1910–1928) — 逃亡与废墟
05  修道之路 (1928–1937) — La Sarte、会名 Dominique、Angelicum 博士
06  司铎与社会学 (1937–1940) — 贫困家庭的尊严
07  抵抗运动司铎 (1940–1945) — 协助盟军飞行员、战后勋章
08  六万名 D.P.：从书到行动 (1949–1957)（核心贡献页）— 《Du Rhin au Danube》与难民村
09  诺贝尔和平奖 1958 — 获奖理由 + Oslo 演讲 Brotherly Love: Foundation of Peace
10  信仰与事业的分离 — 拒绝把个人信仰混入公共援助（宗教上级的不解）
11  从救济到发展 — 和平大学与 Islands of Peace、孟加拉国/印度项目
12  四家组织的传承 — EF / ADP / UdP / IoP 至今仍在运作
13  荣誉与认可 — Nobel 1958 · 联邦功绩十字 · 战争十字
14  遗产：有尊严的生活与 2008 牛津纪念项目
15  结尾
```

### 第 7–8 步：Beamer 源码与布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式。
- 每写完一页 `make` 并 `pdftoppm` 目检；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Pire 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名系统 | 俗名 Georges Charles Clement Ghislain Pire；1932 发终身愿后取会名 Dominique（取自道明会会祖圣道明）——署名一律 Dominique Pire, O.P.，勿把俗名当笔名或改名 |
| 获奖理由口径 | 官方为 "for his efforts to help refugees to leave their camps and return to a life of freedom and dignity"，核心是「走出难民营、回归自由与尊严」，勿写成「为难民提供救济物资」 |
| 书名 | 《Du Rhin au Danube avec 60,000 D. P.》——D. P. 是 displaced persons（流离失所者）缩写，勿写成「六万难民签字」或书名意译过度 |
| 信仰分离 | page.md 明载他坚持不把个人信仰混入对弱势者的公共援助，且不为宗教上级所理解——这是本篇重要立场，但表述保持客观，勿引申评价教会 |
| 组织谱系 | 四家组织名目与分工各不相同（见第 4.5 步表），勿合并叙述或张冠李戴；「和平大学」Université de Paix 主打冲突预防而非学历教育 |
| 演讲标题 | 1958-12 诺奖演讲 Brotherly Love: Foundation of Peace——标题可直接写，但无英文原文段落禁整段引用 |
| 去世口径 | 1969-01-30 逝于 Herent 的鲁汶天主教医院，前列腺手术并发症，58 岁——勿写「病逝于迪南」 |
| 战功表述 | 二战角色是「随军司铎（chaplain）」协助盟军飞行员出境等，勿写成「武装抵抗战士」；勋章为战后所授 |
| 无师承可写 | page.md 未载任何博导/导师姓名，禁编造 advisor；Angelicum 与鲁汶只是就读经历 |
| 地名精度 | 出生 Dinant、修院在 Huy 的 La Sarte、就读 Leuven（鲁汶）——三地勿混 |

**术语清单**：

| 英文/法文 | 中文 | 风险 |
|------|------|------|
| Dominican Order (O.P.) | 道明会 | 旧译多明我会/多米尼克会 |
| displaced persons (D.P.) | 流离失所者 | 二战后专用术语，勿泛译「难民」 |
| chaplain | 随军司铎 | 抵抗运动中的角色 |
| La Sarte | 拉萨尔特修院 | 位于于伊（Huy） |
| Angelicum | 天使大学（宗座圣托马斯大学） | 罗马，神学博士 1936 |
| Service d'Entraide Familiale | 家庭互助服务社 | 组织名，勿意译缩写 |
| Aide aux Personnes Déplacées | 流离失所者援助会 | 组织名 |
| Université de Paix | 和平大学 | 冲突预防机构 |
| Islands of Peace | 和平之岛 | 发展 NGO |
| Brotherly Love: Foundation of Peace | 《手足之爱：和平的基础》 | 1958 诺奖演讲标题 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 辽阔 / 深远 / 纪录片
- **匹配理由**:
  - 「辽阔」匹配其跨国行动半径——比利时→罗马→奥地利→德国→孟加拉国/印度，援助半径跨越欧洲与发展中世界
  - 「深远」匹配「从救济到发展」的理念纵深——不止于一时救济，而是重建有尊严的生活
  - 「纪录片」匹配四家组织接力传承的机构叙事——一人发起、组织长存
- **本地路径**: `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` → 复制为 `presentations/20th_century/Dominique_Pire/SEA.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Dominique_Pire/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `peace/prompt_manifest.json` | batch=peace-batch-11（主色/BGM 预分配） |
| `MySQL/data/Dominique_Pire.yaml` | 研究领域+社会关系入库文件 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
