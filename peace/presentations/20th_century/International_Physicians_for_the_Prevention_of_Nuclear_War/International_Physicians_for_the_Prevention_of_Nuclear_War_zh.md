# 和平奖得主立传提示词（OpenPeace 实例：International Physicians for the Prevention of Nuclear War）

> **本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」的批次实例**，
> 以 International Physicians for the Prevention of Nuclear War（IPPNW，1985 诺贝尔和平奖）为对象。
> **本对象为组织机构（is_org=true）**：第 6 步用「机构概览页」替代身份信息页；yaml 省略 gender/nationalities。
> 结构母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：International Physicians for the Prevention of Nuclear War（国际防止核战争医生组织，IPPNW）——1985 年诺贝尔和平奖得主，横跨冷战铁幕的医生联合会的组织机构立传首例之一。
- **设计哲学**：机构立传与个人立传的核心差异，在于**主角是「组织的使命与网络」而非个人生平**——版面以「成立—发展—获奖—遗产」的组织史时间线为骨架，人物（创始人、领导人）作为机构史的节点出现。

---

## 二、背景信息 【人物专属】

- **机构名称**：International Physicians for the Prevention of Nuclear War（IPPNW，国际防止核战争医生组织）
- **成立**：1980 年（1980-12 日内瓦会议正式成形；前奏为 1961 年 Bernard Lown 在哈佛创立美国 PSR）
- **总部**：美国马萨诸塞州莫尔登（Malden, Massachusetts；另载 Boston）
- **性质**：无党派国际医生联合会（NGO），成员遍布 63 国
- **诺奖年份与官方获奖理由**：1985 年诺贝尔和平奖（独得）：
  > "for spreading authoritative information and by creating awareness of the catastrophic consequences of nuclear war"
  > （表彰其传播权威信息，唤醒世人对核战争灾难性后果的认识）
  > ※ 中译以名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` 为准，禁止改写。
- **气质关键词**：**跨越铁幕的白大褂、医学现实的先知、核裁军的医嘱**
- **设计母题**：**听诊器与蘑菇云的对照（medicine vs. mushroom cloud）**——IPPNW 标志正是以蛇杖（Rod of Asclepius）上立导弹为图形；版面用「医嘱/处方」意象包装「核战争是最后的流行病、无药可医」的核心讯息。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/International_Physicians_for_the_Prevention_of_Nuclear_War/page.md`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对本地页面与事实基准 【人物专属】

- 事实基准（以本地 page.md 为准）：
  - 前史（1961 年 Bernard Lown 在哈佛创立美国 Physicians for Social Responsibility（PSR）；PSR 参与推动 Baby Tooth Survey，促成 1963《部分禁止核试验条约》）
  - 成立（1980 年 12 月，Lown 与苏联心脏病学研究所 Yevgeny Chazov 经 6 封信件往来与 4 月莫斯科会晤后，偕 Eric Chivian、James E. Muller、Herbert Abrams、Leonid Ilyin、Mikhail Kuzin 于日内瓦创立 IPPNW）
  - 创始共同主席（Bernard Lown【美】与 Yevgeniy Chazov【苏】）；其他早期领导人（James E. Muller、Ioan Moraru【罗马尼亚】、Eric Chivian、Herb Abrams【美】、Mikhail Kuzin、Leonid Ilyin【苏】）
  - 奖项（UNESCO Prize for Peace Education 1984-10-30 于巴黎 UNESCO 总部；Nobel Peace Prize 1985-12-10 于奥斯陆，Lown 与 Chazov 代表领奖）
  - 核心事业清单（见第 4 步）
  - 关键时间线（15 节点：1961 PSR 成立 → 1963 部分禁试条约 → 1980-12 日内瓦创立 → 1984 UNESCO 和平教育奖 → 1985-12-10 诺贝尔和平奖 → 1990s 国际委员会调查核武器生产健康环境影响（Radioactive Heaven and Earth / Plutonium / Nuclear Wastelands 三书）→ 1991 冷战结束 → 1990s 扩展至武装暴力议题 → 2001 Aiming for Prevention → 2007-10 与英国皇家医学会伦敦会议、核饥荒项目 → 2007 发起 ICAN → 2010 国际理事会决议呼吁全球禁止铀矿开采 → 2017 ICAN 获诺贝尔和平奖）
  - 领奖仪式外的抗议事件（200–300 名人权活动人士在会场外抗议，指共同领奖人 Chazov 参与了 1972 年针对萨哈罗夫的政治攻击；德国基民盟 Heiner Geißler 1985-11-12 致信评委会；委员会主席 Egil Aarvik 回应）——**只作客观事实记录，禁加评价**

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `International_Physicians_for_the_Prevention_of_Nuclear_War/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 设置 `MAIN=International_Physicians_for_the_Prevention_of_Nuclear_War_zh`（文件名过长可用 `IPPNW_zh` 作 MAIN 并在 Makefile 注明）、`VIDEO_NAME` 同步

### 第 3 步：收集图片 【人物专属】

- 机构无人物肖像：用组织 logo（蛇杖+导弹）矢量重绘或 Wellcome 领奖历史照片（`International_Physicians_for_the_Prevention_of_Nuclear_War_Wellcome_L0075338.jpg`，1985 领奖场景）
- 下载失败则用装饰圆占位

### 第 4 步：使命领域梳理 + 入库 【模板通用，组织机构内容】

**IPPNW 的使命领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nuclear disarmament | 核裁军 | 呼吁消除核武器，1985 诺奖核心 | 封面、使命页 |
| 1 | prevention of nuclear war | 防止核战争 | 传播核战争医学后果的权威信息 | 成立页 |
| 2 | peace education | 和平教育 | UNESCO 1984 奖项理由、医疗专业教育 | 奖项页 |
| 3 | armed violence prevention | 防止武装暴力 | Aiming for Prevention、地雷/小武器/ATT | 扩展页 |
| 4 | public health | 公共卫生 | 铀矿开采健康调查、医用同位素反应堆转化 | 近年页 |

#### 4.1 入库操作

- 新建/更新 `people` 主记录（`name_en='International Physicians for the Prevention of Nuclear War'`），`primary_occupation='peace organization'`、`has_social_data=1`、`has_biography=0`
- **组织机构省略 gender 与 nationalities**；`birth_date` 用 `1980`（成立年）
- 将 5 个领域写入 `person_field`（带 rank），缺失领域先建字典项

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，组织机构内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Bernard Lown | 人→机构 | 创始人兼首任共同主席（美），1985 代表领奖 |
| founder | Yevgeniy Chazov | 人→机构 | 创始人兼首任共同主席（苏），1985 代表领奖 |
| colleague | James E. Muller | 无向 | 早期领导人，日内瓦创立会议参与者 |
| colleague | Eric Chivian | 无向 | 早期领导人，日内瓦创立会议参与者 |
| colleague | Herbert Abrams | 无向 | 早期领导人，日内瓦创立会议参与者 |
| other | Physicians for Social Responsibility | 无向 | 美国分会/前身姊妹组织（Lown 1961 创立），1985 领奖时共享荣誉 |
| other | International Campaign to Abolish Nuclear Weapons | 无向 | 2007 年由 IPPNW 发起的子组织，2017 诺贝尔和平奖得主 |

#### 4.5.1 入库操作

- 以机构记录为中心写入 `person_relation`；founder 类型从创始人指向机构
- 对手方 name_en 先查库沿用库内形式；缺失人物先建占位（`has_biography=0`）
- 无载禁写：Ioan Moraru / Mikhail Kuzin / Leonid Ilyin 仅具名为早期领导人（无独立事迹展开），不入库并在本表备注；抗议事件中的 Sakharov / Geißler / Aarvik 为事件人物，不入库

### 第 5 步：设计配色方案 【模板通用，组织机构色彩】

- **配色**：manifest 预分配主色 **钢蓝 `#2A4B7C`** + 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeFound` 创立 — 深红 `#A63A2B`
  - `badgeInfo` 信息传播 — 青绿 `#0E7C7B`
  - `badgeNobel` 获奖荣誉 — 琥珀 `#E07B30`
  - `badgeICAN` 子组织/遗产 — 紫 `#52307C`
- **背景母题**：地球圆弧 + 医学十字/蛇杖线条 + 稀疏气泡（呼应跨国联合会网络）

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页，机构概览页★】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 跨越铁幕的白大褂 / IPPNW 1980– + 四色 badge + logo + 「国际组织」行
02  机构概览页（★ 必做）— 左 logo/领奖照 + 右信息网格（成立、总部、性质、覆盖、奖项、使命）
03  使命概览 — 核裁军 / 防止核战争 / 和平教育 / 防止武装暴力 / 公共卫生
04  前史：PSR 与婴儿牙齿调查 (1961–1963) — Lown 创立 PSR、1963 部分禁试条约
05  创立：日内瓦 (1980) — Lown–Chazov 六封信与莫斯科会晤、六位创立者
06  医学现实政治化 — 「核战争是最后的流行病」、广岛长崎数据、David Lange 评语
07  UNESCO 和平教育奖 (1984) — 获奖理由、巴黎颁奖
08  1985 诺贝尔和平奖 — 获奖理由原句、奥斯陆颁奖、与 PSR 共享荣誉
09  颁奖典礼风波 — 会场外抗议、Geißler 信件、Aarvik 回应（仅客观事实）
10  冷战后的转型 (1991–2007) — 三部曲报告、核饥荒项目、伦敦会议
11  议题扩展：Aiming for Prevention (2001–) — 地雷、小武器、ATT、IANSA
12  ICAN：从发起 to 2017 诺奖 — 2007 发起、子组织获 2017 诺贝尔和平奖
13  遗产与结尾 — 8 个核倡导诺奖得主之一 + OpenMathAI 品牌口径
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 机构概览页实现模式参照 `\profileslide`（左图右网格）；其余同个人立传骨架

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠

### 第 9 步：史实审查 + 术语审查 【人物专属】

**IPPNW 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 官方措辞 "for spreading authoritative information and by creating awareness of the catastrophic consequences of nuclear war"，勿写"因反核运动"泛化表述；1985 为独得年份 |
| 获奖日期 | 1985-12-10 于奥斯陆（ Oslo，勿拼作 Olso）；Lown 与 Chazov 代表领奖 |
| 与 PSR 关系 | PSR（1961，Lown 创立）是 IPPNW 的**前身姊妹组织/美国分会**，勿写成 IPPNW 的分支下级或子公司；page.md 明载领奖时荣誉与 PSR 共享 |
| 与 ICAN 关系 | ICAN 由 IPPNW 于 2007 年**发起**（daughter organization），2017 年获诺奖——时间方向勿写反 |
| 创始人口径 | 创始共同主席仅 Lown 与 Chazov 两人；Muller/Chivian/Abrams/Moraru/Kuzin/Ilyin 是"早期领导人"，勿升级为"共同创始人" |
| Chazov 争议 | 1985 颁奖典礼抗议事件只作客观事实记录（抗议人数、Geißler 信件日期 1985-11-12、Aarvik 回应原句），禁写任何立场评价 |
| 成立地点 | 1980 年 12 月日内瓦会议创立；总部在 Malden, Massachusetts（infobox 另载 Boston），两说并存时以正文 Malden 为主 |
| 成立前奏 | Lown–Chazov 经 6 封信件往来 + 4 月莫斯科会晤后成行，勿漏中间人 Eric Chivian 等 |
| 成员规模 | 63 国的全国医学组织联合会（federation），勿写成"63 国医生个人会员组织" |
| 组织机构规则 | yaml 省略 gender/nationalities；birth_date 用 1980；无"国籍徽章"版式（机构概览页替代身份信息页） |
| 核饥荒项目 | 基于 2007 伦敦会议的区域核战争气候效应数据，勿与广岛长崎医疗数据研究（1980s）混淆 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| IPPNW | 国际防止核战争医生组织 | 全称长，幻灯片用缩写 IPPNW |
| federation | 联合会 | 强调各分会独立 |
| nuclear disarmament | 核裁军 | 与 arms control（军控）区分 |
| Physicians for Social Responsibility | 美国社会责任医生组织 | 缩写 PSR，美国分会 |
| Partial Nuclear Test Ban Treaty | 《部分禁止核试验条约》 | 1963，禁止大气层试验 |
| Rod of Asclepius | 阿斯克勒庇俄斯之杖（蛇杖） | 医学标志，logo 元素 |
| nuclear famine | 核饥荒 | 2007 后的气候效应项目 |
| Aiming for Prevention | 「以防为目标」项目 | 2001 小武器/武装暴力项目 |
| Arms Trade Treaty | 《武器贸易条约》 | 缩写 ATT |
| International Campaign to Abolish Nuclear Weapons | 国际废除核武器运动 | 缩写 ICAN，2017 诺奖 |
| UNESCO Prize for Peace Education | 教科文组织和平教育奖 | 1984，先于诺奖 |
| final epidemic | 最后的流行病 | IPPNW 医学警告核心隐喻 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Savage** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 紧张 / 深沉 / 张力
- **匹配理由**:
  - "Savage"（冷峻/张力）匹配核战争威胁这一主题的紧迫感与冷战对峙的时代氛围
  - 与「核战争是最后的流行病、无药可医」的医学警告气质吻合——不是乐观颂歌，而是警世的低音
  - 结尾可落在 ICAN 2017 诺奖的传承转折，紧张之后的希望
- **本地路径**: `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav` → `presentations/20th_century/International_Physicians_for_the_Prevention_of_Nuclear_War/Savage.wav`
- **时长**: 以实际文件为准，14 页 × 7 秒 ≈ 98 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/International_Physicians_for_the_Prevention_of_Nuclear_War/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/presentations/cover/openpeace_page.tex` | 项目首页模板 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：无载禁写；政治敏感内容只作客观事实记录。**
