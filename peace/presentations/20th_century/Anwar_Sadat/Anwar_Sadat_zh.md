# 和平奖得主立传提示词（OpenPeace：Anwar Sadat）

> **本文件是 OpenPeace 的「诺贝尔和平奖得主立传提示词」**，以 Anwar Sadat（1978 诺贝尔和平奖，埃及总统）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），按 OpenPeace 立传执行。
> ★ 本篇涉及中东政治，全部内容只作 page.md 明载的客观事实记录，不加任何评价性语句。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他人物侧共享 GitHub）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词 + tex 结构）与和平奖侧批次经验。
- **本实例**：Muhammad Anwar es-Sadat（穆罕默德·安瓦尔·萨达特，埃及第三任总统）。
- **设计哲学**：政治家立传必须有「身份信息页」（Identity / Bio 速览页），且强调「事业领域」的结构化表达——这两点构成骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Anwar Sadat（1918-12-25 ~ 1981-10-06，享年 62 岁；生于尼罗河三角洲 Monufia 省 Mit Abu El Kom，卒于开罗 Nasr City——遇刺）
- **官方获奖理由（1978，与 Menachem Begin 共享）**：
  > "for jointly having negotiated peace between Egypt and Israel in 1978."
  > （中译照抄名录：表彰二人共同谈判促成 1978 年埃及与以色列之间的和平）
- **气质关键词**：**跨越火线的访问者、戴维营的谈判者、为和平付出生命的总统**
- **设计母题**：**握手（the handshake across the line）**。1977 年耶路撒冷之行与 1979 年白宫草坪上的握手——以「两只手越过中线相握」作为视觉母题，呼应其从战场到谈判桌的轨迹。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Anwar_Sadat/page.md`
- **参考模板**：
  - 立传成品参照：OpenMathAI 各侧 15–16 页 Beamer（封面 `\input` 项目首页）
  - 项目封面模板：OpenPeace 侧共享 `cover/` 目录

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已按 page.md 核对）【人物专属】

- 生卒：1918-12-25 生于 Mit Abu El Kom（时为 Sultanate of Egypt）；1981-10-06 在开罗十月战争胜利阅兵式上遇刺身亡，享年 62 岁；安葬于开罗无名战士纪念碑
- 家庭：贫寒家庭，兄弟姐妹 14 人；胞弟 Atef Sadat 为飞行员，1973 年十月战争阵亡；母 Sit Al-Berain（埃及母亲与苏丹父亲之女）；父 Anwar Mohammed El Sadat 曾驻苏丹任军医；名字取自青年土耳其革命「自由英雄」Enver Pasha
- 婚姻：Eqbal Afifi（分居）；Jehan Sadat（1949 年结婚）；子女 7 人
- 教育：开罗皇家军事学院 1938 年毕业，任职通信兵部队；少尉派驻英埃苏丹，结识 Nasser，共创 Free Officers（自由军官组织）
- 军衔：上校（现役）、元帅（荣誉）
- 任职轨迹：1952-07-23 自由军官革命（宣读革命第一份广播声明）→ 1954 国务部长兼《Al Gomhuria》报主编 → 1959 民族联盟书记 → 1960–1968 国民议会第二任议长 → 1964/1969 两度副总统 → 1970-09-28 Nasser 去世后继任总统（至 1981）→ 1980-05 兼任总理
- 总统任期大事：1971-05-15「纠正革命」清洗纳赛尔派；驱逐苏联军事人员；1971 致函支持 Jarring 调解方案（未果）；1973-10-06 与叙利亚 Assad 联手发动十月战争（Operation Badr 渡过苏伊士运河、突破 Bar Lev 防线，「渡河英雄」）；两次脱离接触协议（1974-01-18 / 1975-09-04）；1974 第 43 号法《Infitah》开放政策；恢复多党制；1977-01 面包骚乱；1977-11 访问耶路撒冷（首位正式到访以色列控制区的阿拉伯领导人，在 Knesset 演说，主张全面实施联合国 242/338 号决议）；1978 戴维营协议（Carter 斡旋）；1979-03-26 华盛顿签署埃以和平条约（埃及成为首个正式承认以色列的阿拉伯国家，西奈分阶段归还至 1982）；埃及 1979–1989 被中止阿盟成员资格
- 关键荣誉：诺贝尔和平奖（1978，与 Begin 共享）；Presidential Medal of Freedom；Congressional Gold Medal；Order of the Nile 等多国勋章
- 关键时间线（16 节点）：1918 生于 Mit Abu El Kom → 1938 军校毕业入通信兵 → 驻苏丹结识 Nasser、入 Free Officers → 二战期间入狱多年 → 1952 七月革命宣读声明 → 1954 国务部长/报主编 → 1960 议长 → 1969 副总统 → 1970-10 继任总统 → 1971 纠正革命 → 1973-10-06 十月战争 → 1974 Infitah → 1977-11 耶路撒冷之行 → 1978 戴维营协议、诺贝尔和平奖 → 1979-03-26 埃以和约 → 1981-10-06 阅兵式遇刺

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下建 `Anwar_Sadat/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目近邻成品 Makefile，设 `MAIN=Anwar_Sadat_zh`、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【人物专属】

- page.md 载 1970 年官方像、1978 访美照、1979-03-26 白宫签署条约合影（Carter-Sadat-Begin）等；按 images.txt/REST API 下载，404 则用装饰圆占位

### 第 4 步：事业领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace negotiation | 和平谈判 | 耶路撒冷之行、戴维营、埃以和约 | 核心页 |
| 1 | diplomacy | 外交 | 与西方修复关系、Jarring 方案、联合国决议框架 | 外交页 |
| 2 | politics | 政治治理 | 总统任期、纠正革命、恢复多党制 | 政治页 |
| 3 | military leadership | 军事领导 | 自由军官组织、十月战争渡河作战 | 军事页 |
| 4 | economic liberalization | 经济开放 | Infitah 第 43 号法 | 经济页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Menachem Begin | 无向 | 1978 诺贝尔和平奖共同得主，埃以和约签署双方 |
| colleague | Gamal Abdel Nasser | 无向 | 驻苏丹时期结识、共创自由军官组织，任其副总统并于其身后继任总统 |
| colleague | Hafez al-Assad | 无向 | 1973-10-06 联合发动十月战争 |
| colleague | Jimmy Carter | 无向 | 斡旋 1978 戴维营协议并促成 1979 埃以和约 |
| colleague | Hosni Mubarak | 无向 | 副总统（1975–1981），遇刺后继任总统 |
| spouse | Jehan Sadat | 无向 | 1949 年结婚 |
| spouse | Eqbal Afifi | 无向 | 分居 |

### 第 5 步：设计配色方案 【人物专属，勿改主色】

- **主色**：`#372A75`（深紫罗兰蓝——庄重与跨越）
- **辅色**：诺奖香槟金 `C9A227` + 四分类色：badgeA 和平谈判 `#2E5F7A`；badgeB 军事 `#7A3E48`；badgeC 政治 `#8C6A2F`；badgeD 经济开放 `#2E7D6B`
- **背景母题**：越线相握的手与西奈地平线

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有肖像（或装饰圆占位）+ 姓名小字注；顶部/底部明示国籍（Egypt）。
2. 必须有身份信息页：左肖像 + 右信息网格（生卒、家庭、教育、军衔、任职、荣誉、核心领域）。
3. 结尾页品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00 OpenPeace 项目首页（\input cover 共享页）
01 封面 — 1978 诺贝尔和平奖 / Anwar Sadat 1918–1981 + badge + 国籍行
02 身份信息页（★ 必做）
03 核心贡献概览 — 十月战争 / 耶路撒冷之行 / 戴维营 / 埃以和约
04 早年与从军 (1918–1952) — Mit Abu El Kom、1938 军校、驻苏丹结识 Nasser
05 自由军官与七月革命 — 二战入狱岁月、1952-07-23 广播声明
06 纳赛尔时代的副手 — 议长、两度副总统、《Al Gomhuria》主编
07 总统：纠正革命 (1970–1972) — 继任、清洗纳赛尔派、驱逐苏联军事人员
08 十月战争 (1973) — 10-06 联合 Assad 发动、Operation Badr 渡河、Bar Lev 防线
09 从战争到谈判 (1974–1977) — 两次脱离接触协议、Infitah、多党制、面包骚乱
10 耶路撒冷之行 (1977-11) — 首位到访以色列控制区的阿拉伯领导人、Knesset 演说
11 戴维营与诺贝尔和平奖 (1978) — Carter 斡旋、共享理由句
12 埃以和平条约 (1979-03-26) — 华盛顿签署、西奈归还、阿盟中止
13 遇刺 (1981-10-06) — 阅兵式遇刺、葬礼（三位美国前总统同席、Begin 徒步送葬）
14 遗产 — 埃以和约延续至今、无名战士纪念碑安葬
15 结尾
```

### 第 7–8 步：Beamer 编写 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；写完即 make，`pdftoppm` 截图查溢出；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Anwar Sadat 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 政治红线 | 中东议题（阿以冲突、和约、阿盟中止等）一律只作 page.md 明载的客观事实记录，禁任何评价性语句；条约在阿拉伯世界的反对、遇刺背景等按 page.md 双方事实并列，不进引文框、不作定性 |
| 获奖口径 | 1978 诺贝尔和平奖与 Begin 共享，理由句 "jointly having negotiated peace between Egypt and Israel in 1978"——领奖演说提到阿拉伯人与以色列人共同期盼的和平（page.md 明载，可转述） |
| 十月战争命名 | October War / Yom Kippur War / Ramadan War 同指 1973 战争；本篇统一用「十月战争」并注别名 |
| 时间巧合 | 1973-10-06 发动战争与 1981-10-06 遇刺同为 10 月 6 日——两处日期勿误写 |
| 耶路撒冷之行 | 1977-11，首位正式访问以色列控制区的阿拉伯领导人；演说主张实施 UN 242/338 号决议——勿写成"访问以色列国"细节外推 |
| 条约签署地 | 1979-03-26 签于华盛顿白宫草坪（page.md 图注明载），非戴维营；戴维营是 1978 年协议 |
| 名字来源 | 取自 Enver Pasha——勿漏；母系有苏丹血统 |
| 二战经历 | 曾与纳粹德国合作（Operation Salam）并因此入狱多年——按 page.md 客观记录，禁美化或回避 |
| 继任者 | 副总统 Mubarak 继任；总理任期（1980–1981）由本人兼任——勿混 |
| 伊朗关系 | 与巴列维国王的友谊、为流亡国王举行国葬——按 page.md 客观记录，篇幅从简 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Free Officers | 自由军官组织 | 1952 年革命主体 |
| Corrective Revolution | 纠正革命 | 1971-05-15 |
| October War | 十月战争 | 又称赎罪日战争/斋月战争 |
| Operation Badr | 「 Badr 」行动 | 渡河作战，又称 The Crossing |
| Bar Lev Line | 巴列夫防线 | 以军运河防线 |
| Infitah | 开放政策 | 1974 第 43 号法 |
| Camp David Accords | 戴维营协议 | 1978，Carter 斡旋 |
| Egypt–Israel peace treaty | 埃以和平条约 | 1979-03-26 签于华盛顿 |
| Knesset | 以色列议会 | 1977 演说地点 |
| Hero of the Crossing | 渡河英雄 | 战后称号 |

---

## 四、背景音乐 ✅ 【人物专属，manifest 预分配，勿改】

- **选定曲目**: **Timeless** — Alex-Productions
- **匹配理由**: 「恒久」对应其和约遗产——1979 年签署的埃以和平条约延续至今；沉稳的纪录片气质匹配从军校生到诺贝尔奖得主再到遇刺的完整人生弧线。
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → 复制为 `presentations/20th_century/Anwar_Sadat/Timeless.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Anwar_Sadat/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译（照抄，禁改写） |
| `MySQL/data/Anwar_Sadat.yaml` | 入库 yaml（第 4/4.5 步落地） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
