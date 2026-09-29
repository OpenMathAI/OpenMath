# 和平奖得主立传提示词（OpenPeace：UNHCR，组织机构篇）

> **本文件是 OpenPeace 的「和平奖得主立传提示词（组织机构版）」**，以 Office of the United Nations High Commissioner for Refugees（联合国难民事务高级专员公署，1954 与 1981 两度诺贝尔和平奖）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；组织机构按共享工作流第 2 节特别规则执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Office of the United Nations High Commissioner for Refugees（UNHCR）——20 世纪 16 个机构得主之一，1954 与 1981 两度获奖（只做一次立传 + 一条 DB 记录，awards 含两条）。
- **设计哲学**：机构立传以「机构概览页」替代人物身份信息页；叙事重心是**为难民提供国际保护**——从战后欧洲流离失所者到全球托管义务，一条跨越七十年的保护红线。

---

## 二、背景信息 【机构专属】

- **目标机构**：Office of the United Nations High Commissioner for Refugees（1950-12-14 设立于日内瓦，全称直译「联合国难民事务高级专员公署」）
- **气质关键词**：**战创伤的治愈者、难民保护的国际托管人、全球人道网络的协调者** —— 两度获奖理由：
  > 1954: "for its efforts to heal the wounds of war by providing help and protection to refugees all over the world"（表彰它通过向全世界难民提供帮助与保护来治愈战争创伤的努力）
  > 1981: "for promoting the fundamental rights of refugees"（表彰其为维护难民基本权利所做的促进工作）
- **设计母题**：**帐篷与护照（shelter and documents）**。以蓝白主色下的帐篷轮廓、边境线、签证印章、迁徙路线图构成视觉语言，呼应「为无国籍者提供身份与庇护」的使命。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/United_Nations_High_Commissioner_for_Refugees/page.md`
- **参考模板**：标杆提示词 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；首页模板 `peace/presentations/cover/openpeace_page.tex`

---

## 三、任务流程 【模板通用骨架 + 机构专属内容】

### 第 0 步：核对本地页面，建立事实基准 【机构专属】

- ✅ 页面已抓取（frontmatter：QID Q132551 / field_of_work: refugee law, humanitarian aid / 奖项含两度 Nobel Peace Prize）
- **事实基准（第一轮已核对，全部以 page.md 为准）**：
  - 设立：1949-12 联合国大会第 319(IV) 号决议决定设立；1950-12-14 正式成立；1951-01-01 开始运作；初定仅运作 3 年
  - 性质：联合国大会下属机构（subsidiary organ），总部日内瓦；受联大与经社理事会治理
  - 使命：以非政治与人道主义为基础向难民提供国际保护，寻求永久解决方案（自愿遣返 / 当地融合 / 第三国重新安置）；保管难民信息数据库 ProGres
  - 法理基础：1951《关于难民地位的公约》与 1967 议定书（1967 议定书取消地理与时间限制，使命全球化）
  - 机构谱系：国际联盟 1921 任命 Fridtjof Nansen 为首任难民事务高级专员 → 1930 Nansen 国际办公室 → 1938 新任高级专员（1946 终止）→ 1944 UNRRA → 1946 IRO → 1950 UNHCR（承接 UNRRA 工作）
  - 里程碑：1956 匈牙利事件协调 → 1957 香港/阿尔及利亚难民 → 1960s 非洲非殖民化（十年间预算重心移向非洲）→ 1970s 东巴基斯坦/印度支那 → 1990s 冷战后族群冲突（1994 卢旺达）→ 2015 年 65 周年时累计援助逾 5000 万难民 → 2024 年底全球被迫流离失所 1.232 亿人
  - 关键荣誉：Nobel Peace Prize 1954、1981；Nansen Refugee Award（1954 起每年颁发）；Prince of Asturias Award 1991；Indira Gandhi Prize 2015
  - 历任高级专员：首任 Gerrit Jan van Heuven Goedhart（1951–1956）→ Sadako Ogata（1990–2000，在任 10 年）→ António Guterres（2005–2015）→ Filippo Grandi（2016–2025）→ Barham Salih（2026 起， incumbent）
  - 核心事业清单：① 国际保护与三 durable solutions；② 1951 公约框架下的全球难民法实践；③ 紧急救援（帐篷/医疗/饮水）；④ 无国籍者与境内流离失所者关注；⑤ 与联合国体系及 FAO/WFP 等机构协作
  - 关键时间线（15–20 节点）：1920 国际联盟成立 → 1921 Nansen 任国联高级专员 → 1930 Nansen 办公室 → 1938 国联新任高级专员 → 1944 UNRRA → 1946 IRO → 1949-12 联大 319(IV) 决议 → 1950-12-14 成立 → 1951-01-01 运作 + 1951 公约 → 1954 诺贝尔和平奖 → 1956 匈牙利 → 1967 议定书 → 1981 第二度诺贝尔和平奖 → 1990s 卢旺达/巴尔干 → 2005 Guterres 就任 → 2016 纽约宣言 → 2024 1.232 亿流离失所

### 第 1–3 步：目录 / Makefile / 图片 【模板通用】

- 在 `peace/presentations/20th_century/United_Nations_High_Commissioner_for_Refugees/` 下建 `images/`；Makefile 复制同项目成品并设 `MAIN=United_Nations_High_Commissioner_for_Refugees_zh`
- 视觉素材：用 page.md/images.txt 中的难民营实景与日内瓦总部照片（Genf_UNHCR.JPG 等）；下载失败用装饰圆占位并记录

### 第 4 步：使命领域梳理 + 入库 【模板通用，机构专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | refugee protection | 难民保护 | 非政治与人道基础上的国际保护，机构核心使命 | 使命页 |
| 1 | humanitarian aid | 人道主义援助 | 庇护所/医疗/紧急救援 | 职能页 |
| 2 | refugee law | 难民法 | 1951 公约与 1967 议定书的法律框架 | 历史页 |
| 3 | statelessness | 无国籍问题 | 关注人群扩展与保护短板 | 关注人群页 |
| 4 | forced displacement | 被迫流离失所 | 1.232 亿人（2024）全球态势 | 数据页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）【机构专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Gerrit Jan van Heuven Goedhart | 无向 | 首任难民事务高级专员（1951–1956） |
| other | United Nations | 无向 | 联合国大会下属机构，1949 年第 319(IV) 号决议设立 |
| other | United Nations Relief and Rehabilitation Administration | 无向 | 前身机构，1950 年成立时承接其工作 |
| other | Fridtjof Nansen | 无向 | 国际联盟首任难民事务高级专员（1921），机构谱系前身 |
| other | United Nations Relief and Works Agency for Palestine Refugees in the Near East | 无向 | 并行机构，巴勒斯坦难民由 UNRWA 负责 |

> 组织机构无 spouse/parent-child；两度诺奖均独享（1954/1981 单独得主），无 co-honored。

### 第 5 步：设计配色方案 【模板通用，机构专属色彩】

- **主色（manifest 预分配，勿改）**：深林绿 `#1B4D3E`
- 辅色：诺奖香槟金 `#C9A227` + 联合国蓝 `#5B92E5`（点缀，勿作主色）
- 四分类色：`badgeProtect` 难民保护 — 靛蓝 `#1F3A5F`；`badgeAid` 人道援助 — 青绿 `#0E7C7B`；`badgeLaw` 难民法 — 琥珀 `#E07B30`；`badgeData` 全球态势 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡 + 蓝色迁徙虚线，呼应「跨越边境的保护网络」

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面以机构标识/总部影像替代人物头像，右上 + 细边框 + 机构全名小字注。
2. **必须有机构概览页（替代身份信息页，★）**：左视觉素材 + 右信息网格（设立日期与决议、总部、性质、使命、历任首末任高级专员、两度诺奖年份、核心领域）。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【机构专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 难民保护的国际托管人 / UNHCR 1950– + badge + 国旗/标识 + 国际组织行
02  机构概览页（★ 必做）— 左视觉素材 + 右信息网格
03  使命概览 — 国际保护 / 三 durable solutions / 人道援助 / 难民法 / 无国籍
04  谱系前传：从 Nansen 到 IRO (1921–1950) — 国联高级专员谱系
05  创立：联大 319(IV) 决议与 1951 公约 (1949–1951) — 初定仅运作 3 年
06  第一次诺贝尔和平奖 1954 — heal the wounds of war
07  全球化：匈牙利 1956 与 1967 议定书 — 使命走出欧洲
08  非洲十年与亚洲危机 (1960s–1970s) — 非殖民化、印度支那
09  第二次诺贝尔和平奖 1981 — promoting the fundamental rights of refugees
10  冷战后挑战 (1990s–2000s) — 卢旺达、巴尔干、营内援助
11  数据看难民 — ProGres 数据库、2024 年 1.232 亿、预算从 30 万到 86 亿美元
12  高级专员传承 — van Heuven Goedhart / Ogata / Guterres / Grandi / Salih
13  荣誉与认可 — Nobel 1954/1981 · Asturias 1991 · Indira Gandhi 2015
14  遗产：一张覆盖全球的保护之网
15  结尾
```

### 第 7–8 步：Beamer 源码与布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；机构概览页参照 `\profileslide` 改造为 `\orgslide`。
- 每写完一页 `make` 并 `pdftoppm` 目检；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【机构专属】

**UNHCR 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 「创立者」勿写 | 机构由联合国大会决议设立，无个人创始人；勿把任何一任高级专员写成 founder |
| 首任 ≠ Nansen | Fridtjof Nansen 是**国际联盟**首任难民事务高级专员（1921），不是 UNHCR 首任；UNHCR 首任是 Gerrit Jan van Heuven Goedhart（1951） |
| 两度获奖 | 1954 与 1981 两次获奖理由不同（heal the wounds / fundamental rights），两页分开写，勿混用；两次均独享，勿写共享 |
| 决议编号 | 设立决议是联大第 319(IV) 号（1949-12）；章程附于 1950 年第 428(V) 号决议——两个编号勿混 |
| 成立日期 | 正式成立 1950-12-14、开始运作 1951-01-01，两个日期各有用途勿混写 |
| UNRWA 分工 | 巴勒斯坦难民由 UNRWA 负责，UNHCR 章程明确排除——勿写成 UNHCR「负责所有难民」 |
| 争议节处理 | Controversies 节（1995 罗兴亚遣返、西非性剥削报告等）只可作客观事实简述，禁评价性语句；乌伊格尔相关表述涉及敏感，只写 page.md 明载一句或整体回避 |
| 数据时效 | 受众数据逐年变化（57.9M/2015 → 43.4M refugees/2023 → 123.2M displaced/2024），引用必须带年份 |
| 机构性质 | 是 UN Programme（联大与经社理事会治理的方案），不是「政府间条约组织」；总部日内瓦 |
| 1981 未颁奖年 | 和平奖 1955/1956 等年未颁奖与本机构无关；1954/1981 均正常颁奖 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| UNHCR | 联合国难民事务高级专员公署 | 全称含 Office of，缩写 UNHCR/HCR |
| High Commissioner | （难民事务）高级专员 | 勿译「高级代表」 |
| 1951 Convention relating to the Status of Refugees | 《关于难民地位的公约》 | 国际难民法基石 |
| 1967 Protocol | 《难民地位议定书》 | 取消地理与时间限制 |
| durable solutions | 持久解决方案 | 遣返/融合/重安置三种 |
| internally displaced persons (IDPs) | 境内流离失所者 | 与难民法律地位不同 |
| statelessness | 无国籍状态 | 关注人群之一 |
| voluntary repatriation | 自愿遣返 | durable solution 之一 |
| resettlement | 重新安置（第三国） | 与当地融合并列 |
| Nansen Refugee Award | 南森难民奖 | UNHCR 自 1954 年颁发的年度奖项 |

---

## 四、背景音乐选择 ✅ 【机构专属】

- **选定曲目**: **Nostalgia** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 怀旧 / 温情 / 纪录片
- **匹配理由**:
  - 「怀旧」匹配七十年的机构史——从战后欧洲废墟到今天的全球保护网络，是回望式叙事
  - 「温情」匹配其人道底色——帐篷、粮食、身份文件背后的个体命运
  - 「纪录片」匹配两度诺奖的 institutional 传记——不是英雄叙事，而是一代代高级专员与两万职员的接力
- **本地路径**: `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` → 复制为 `presentations/20th_century/United_Nations_High_Commissioner_for_Refugees/Nostalgia.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/United_Nations_High_Commissioner_for_Refugees/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 1954/1981 获奖理由中译（照抄勿改） |
| `peace/prompt_manifest.json` | batch=peace-batch-11（主色/BGM 预分配，is_org=true） |
| `MySQL/data/United_Nations_High_Commissioner_for_Refugees.yaml` | 使命领域+社会关系入库文件 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
