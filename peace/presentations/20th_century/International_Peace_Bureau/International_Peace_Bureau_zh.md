# 和平奖得主立传提示词（OpenPeace 模板实例：International Peace Bureau，组织机构篇）

> **本文件是 OpenPeace 的「机构专属立传提示词」**，以 Kenneth_G_Wilson_zh.md（0–11 节结构母本）为结构标杆，
> 以 Frederick_Sanger.yaml 为 yaml 字段母本，为 International Peace Bureau（1910 诺贝尔和平奖得主，组织机构，is_org=true）定制。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【机构专属】` 的部分为 IPB 专属内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。
> **机构篇特殊规则**：机构概览页替代身份信息页；勿把机构领导人写成创始人；省略 gender/nationalities。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 体系，与 OpenPhysicist / OpenChemist / OpenMedic 平级）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的任务流程骨架 + 诺贝尔奖立传通用版式。
- **本实例**：International Peace Bureau（国际和平局，IPB，1891 年成立，1910 年诺贝尔和平奖得主，本批次唯一组织机构）。
- **设计哲学**：机构立传以「使命—网络—传承」替代人物的「生卒—师承—成就」：以机构概览页呈现使命领域，以得主席位网络页（13 位相关诺奖得主）呈现其作为「各国和平团体纽带」的独特地位。

---

## 二、背景信息 【机构专属】

- **机构名称**：英文 International Peace Bureau（IPB；法文 Bureau international de la paix）；中文 国际和平局
- **获奖时名称**：Permanent International Peace Bureau（Bureau International Permanent de la Paix，1891 年成立时的名称，manifest DATA 规范名即此）
- **成立**：1891-11-13（infobox Formation 明载精确日期）；1912 年起改用现名 International Peace Bureau；1946–1961 曾名 International Liaison Committee of Organizations for Peace – ILCOP
- **总部**：德国柏林（2017 年前在瑞士日内瓦；另在西班牙巴塞罗那、瑞士日内瓦设办公室）
- **性质**：NGO / 非营利；世界最悠久的国际和平联合会之一；成员为 70 国 300 个组织
- **诺奖年份**：1910（机构独得）
- **官方获奖理由英文原文**（照抄 nobel_peace_citations.json，禁止改写）：
  > "for acting as a link between the peace societies of the various countries, and helping them to organize the world rallies of the international peace movement."
- **官方获奖理由中译**（照抄名录 OpenPeace_20th_Century_Nobel_Laureates.md，禁止改写）：
  > 表彰它作为各国和平团体之间的纽带，协助组织国际和平运动的世界性集会
- **气质关键词**：**各国和平团体的纽带、核裁军运动的百年旗舰、世界和平大会的组织者**
- **设计母题**：**环环相扣的链条（interlinked rings）**。获奖理由核心是 "acting as a link between the peace societies"——以相扣的圆环链构成视觉母题，象征其把 70 国 300 组织连结为一体；亦呼应后世和平象征符号的圆环语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/International_Peace_Bureau/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/`（OpenPeace 共享封面）
  - yaml 字段母本：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 机构专属内容】

> 每完成一步汇报，遇到歧义先征求主控意见再继续。
> **数据库同步要求**：包含「使命领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准 【机构专属，全部取自 page.md，无载禁补】

- 成立：1891-11-13，初名 Permanent International Peace Bureau（page.md **未载创始人姓名，禁写创始人**）
- 名称演变：1891 Permanent International Peace Bureau → 1912 起 International Peace Bureau → 1946–1961 ILCOP
- 总部与网络：总部柏林（2017 年前日内瓦）；巴塞罗那、日内瓦办公室；70 国 300 个成员组织
- 核心使命与项目：
  1. 全球军事开支运动（Global Campaign on Military Spending, GCOMS，2014-12 创设）：推动各国将军费转投医疗、教育、就业与气候；主张每年至少实际重配 10% 军费；GCOMS 由巴塞罗那办公室与 Centre Delàs d'Estudis per la Pau 协调管理，35 国 100+ 组织加入；每年组织 Global Day of Action on Military Spending（GDAMS）
  2. 可持续发展裁军（disarmament for sustainable development）：核武器、常规武器、生物武器、地雷、轻小武器
  3. 核裁军行动（1945 年以来一直走在前列）：NPT、CTBT、World Court Project、TPNW；当前推动 TPNW 签署与批准生效
  4. 与联合国体系：经社理事会（ECOSOC）咨询地位；全球传播部（Department of Global Communications）联系地位
- 诺奖关联：
  - 1910 年机构本身获奖；**截至 2012 年另有 11 位诺奖得主为其成员**
  - 1913 年 Henri La Fontaine 以国际和平局领导人（head）身份获奖
  - 1992 年创设 Seán MacBride Peace Prize（以 1968–1974 主席、1974–1985 总裁 MacBride 命名），获奖者含 Nihon Hidankyō（2003）、Mayors for Peace（2006）、John Hume（1998）、Noam Chomsky（2017）等
- 历届主席（page.md 明载名单）：Henri La Fontaine 1907–1943、Ernst Wolf 1963–1974、Seán MacBride 1974–1985、Bruce Kent 1985–1992、Maj Britt Theorin 1992–2000、Cora Weiss 2000–2006、Tomas Magnusson 2006–2013、Ingeborg Breines 2009–2016、Reiner Braun 2013–2019、Lisa Clark 2016–2022、Philip Jennings 2019–2025、Corazon Valdez Fabros 2025–、Joseph Gerson 2025–（现行双主席制保证性别均衡，每人最多两个三年任期）
- 关键荣誉：1910 年诺贝尔和平奖
- 关键时间线（16 节点，全部 page.md 明载）：
  1. 1891-11-13 成立于 Permanent International Peace Bureau 之名
  2. 19 世纪末成为各国和平团体的国际联络中枢
  3. 1901–1913 间多位成员/职员相继获诺贝尔和平奖（Passy 1901、Ducommun/Gobat 1902、Suttner 1905、Moneta 1907、Bajer 1908、Fried 1911、La Fontaine 1913）
  4. 1910 机构获诺贝尔和平奖
  5. 1912 改名 International Peace Bureau
  6. 1913 La Fontaine 以局领导人身份获奖
  7. 1945 起投身核裁军行动
  8. 1946–1961 改名 ILCOP
  9. 1968–1985 MacBride 任主席/总裁
  10. 1992 设立 Seán MacBride Peace Prize
  11. 2012 前后成员网络达 70 国 300 组织
  12. 2014-12 创设 GCOMS 全球军事开支运动
  13. 2017 总部由日内瓦迁柏林
  14. 近年推行双主席制
  15. 持续推动 TPNW 签署与批准
  16. 2025 双主席换届（Fabros / Gerson）

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/International_Peace_Bureau/` 下建 `images/`
- Makefile 设置 `MAIN=International_Peace_Bureau_zh`、`VIDEO_NAME=International_Peace_Bureau_zh`
- 图片：page.md 内嵌历史照片可用（1899 年伯尔尼理事会会议照、1935 年大会照、2016 年柏林世界大会照）；「机构肖像」可用其中 1899 年会议照作主图，无独立肖像概念

### 第 4 步：使命领域表 + 入库 【机构专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | world peace | 世界和平 | infobox Fields 明载的使命领域 | 概览页 |
| 1 | disarmament | 裁军 | 常规/生物武器、地雷、轻小武器 | 项目页 |
| 2 | nuclear disarmament | 核裁军 | NPT/CTBT/TPNW，1945 年以来前列 | 核裁军页 |
| 3 | peace education | 和平教育 | Seminars and Conferences / Education 方法 | 概览页 |
| 4 | international peace movement | 国际和平运动 | 各国和平团体的纽带与集会组织 | 诺奖页 |

- yaml `fields` 与上表一致（5 条）；入库 `person_field` 带 rank

### 第 4.5 步：社会关系表 + 入库 【机构专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Henri La Fontaine | 无向 | 1907–1943 任主席；1913 以国际和平局领导人身份获诺贝尔和平奖 |
| colleague | Fredrik Bajer | 无向 | 荣誉主席，1908 诺贝尔和平奖得主 |
| colleague | Élie Ducommun | 无向 | 首任荣誉秘书之一，1902 诺贝尔和平奖得主 |
| colleague | Albert Gobat | 无向 | 首任荣誉秘书之一，1902 诺贝尔和平奖得主 |
| colleague | Bertha von Suttner | 无向 | 荣誉副主席，1905 诺贝尔和平奖得主 |
| colleague | Seán MacBride | 无向 | 1968–1974 任主席、1974–1985 任总裁；1974 诺贝尔和平奖得主；机构奖以其命名 |

- 均为 page.md「Nobel Peace Prizes / Presidents」两节明载的任职关系，type 用 colleague（机构—人物任职语境）；**page.md 未载创始人，禁建 founder 关系**
- 其余 council member（Passy/Moneta/Fried/Quidde/Noel-Baker/Pauling/Myrdal 等）只叙述不入库，防 stub 泛滥
- 与联合国 ECOSOC 的咨询地位系机构间关系，不入 person_relation

### 第 5 步：配色方案 【模板通用，机构专属色彩】

- **气质**：百年的厚重、网络的连结、和平的恒久
- **配色**：主色 `#17435B`（深海蓝，manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + badgeA–D 四分类色
  - `badgeA` 世界和平 — 靛蓝 `#3F51B5`
  - `badgeB` 核裁军 — 青绿 `#0E7C7B`
  - `badgeC` 和平教育 — 琥珀 `#E07B30`
  - `badgeD` 得主席位网络 — 玫瑰 `#C4204F`
- **背景母题**：相扣圆环链（interlinked rings）+ 稀疏金色圆点，呼应「纽带」母题

### 第 6 步：规划幻灯片序列 【机构专属，14–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 各国和平团体的纽带 / International Peace Bureau 1891– + 四色 badge + 主图 + International organization 行
02  机构概览页（★ 必做，替代身份信息页）— 名称演变 / 成立 / 总部 / 性质 / 成员规模 / 使命 / 诺奖
03  使命概览 — 世界和平 / 裁军 / 核裁军 / 和平教育 / 国际和平运动
04  1891 年的诞生 — Permanent International Peace Bureau、伯尔尼理事会
05  纽带的使命 (1910 诺奖) — 官方理由、世界性集会组织
06  得主席位网络（★ 本篇特色页）— Passy / Ducommun / Gobat / Suttner / Moneta / Bajer / Fried / La Fontaine / Quidde / Noel-Baker / Pauling / Myrdal / MacBride（13 位，任职身份标注）
07  名称与身份的演变 — 1912 改名、1946–1961 ILCOP
08  核裁军七十年 — 1945 以来 NPT / CTBT / World Court Project / TPNW
09  GCOMS 全球军事开支运动 — 2014 创设、10% 重配主张、GDAMS
10  Seán MacBride Peace Prize — 1992 创设、获奖者概览
11  历届主席 — La Fontaine 1907–1943 至 2025 双主席制
12  与联合国体系 — ECOSOC 咨询地位、全球传播部联系地位
13  今日 IPB — 70 国 300 组织、柏林总部、三大办公室
14  遗产 — 最悠久的国际和平联合会
15  结尾
```

### 第 7–8 步：Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；机构概览页实现模式参照标杆 `\profileslide`（把「生卒/师承」字段替换为「成立/总部/性质/使命」）
- 每写完一页 `make distclean && make`，`pdftoppm` 截图检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标
- 得主席位网络页 13 条目用两栏 `itemize` 或 `arraystretch 0.58` 压缩，只写姓名+年份+身份，不写理由全文

### 第 9 步：史实审查 + 术语审查 【机构专属】

**IPB 专属陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 创始人禁写 | page.md 只写 "founded in 1891"，**未载创始人姓名**；勿把首任主席 La Fontaine 或任何领导人写成创始人；禁建 founder 关系 |
| 获奖时名称 | 1910 年获奖时名为 Permanent International Peace Bureau（manifest DATA 规范名）；1912 起才叫 International Peace Bureau；封面用现名、诺奖页注明获奖时名称 |
| ILCOP 时期 | 1946–1961 曾名 ILCOP，是同一机构的更名史，勿写成「前身/另一机构」 |
| 勿与伯尔尼和平局混淆 | 1902 年 Ducommun 获奖理由表彰的是 "the Bern Peace Bureau"（伯尔尼国际和平局 Ducommun 主持的机构），与 IPB 是两条线索，勿混写 |
| 1913 La Fontaine | 是其**个人**获奖（以 IPB 领导人身份），不是 IPB 第二次获奖 |
| 得主成员口径 | "As of 2012, eleven other Nobel Peace Prize laureates have been members"——数字 11 以 2012 年为锚点，勿写成恒定值；得主席位网络页逐人标注任职身份（council member / honorary secretary / honorary vice-president / honorary president / president / vice-president / chairman） |
| 双主席制 | 现行 co-president 制（2025 年起 Fabros 与 Gerson；此前 Jennings/Fabros 并列），勿写成单一「现任主席」 |
| MacBride 奖 | 奖项以 MacBride 命名（其 1968–1974 主席 / 1974–1985 总裁任期 page.md 明载），获奖者表格只择要列举，勿全列 |
| 无载禁写清单 | 创始人、成立地点（1891 年成立城市 page.md 未载，勿写）、早期具体活动年份、ILCOP 时期细节、各任主席国籍——一律禁写 |
| 政治敏感红线 | Seán MacBride 奖获奖者涉及当代政治人物与争议议题（Chomsky、Corbyn、Marshall Islands 等）只作「某年授予某人」的客观记录，禁写理由全文与评价；核裁军议题只列条约参与事实，不加政治评价 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| International Peace Bureau | 国际和平局 | IPB，1912 起现名 |
| Permanent International Peace Bureau | 常设国际和平局 | 1891 初名，获奖时名称 |
| peace federation | 和平联合会 | 勿译「联盟」 |
| link between the peace societies | 各国和平团体之间的纽带 | 官方理由核心词 |
| consultative status | 咨询地位 | ECOSOC 语境 |
| Global Campaign on Military Spending | 全球军事开支运动 | GCOMS |
| Treaty on the Prohibition of Nuclear Weapons | 《禁止核武器条约》 | TPNW |
| honorary president | 荣誉主席 | Bajer 身份 |
| honorary secretary | 荣誉秘书 | Ducommun/Gobat 身份 |
| council member | 理事会成员 | Passy/Moneta/Fried 等身份 |
| Seán MacBride Peace Prize | Seán MacBride 和平奖 | 人名保留爱尔兰语拼写 |

---

## 四、背景音乐选择 【机构专属，manifest 预分配，勿改】

- **选定曲目**：**Lonesome** — inspiring-electronic / AShamaluevMusic（Sad and Emotional Cinematic Music）
- **bgm_path**：`music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`
- **匹配理由**：深沉而克制的情绪化配乐，匹配一个跨越两次大战、见证和平理想屡遭挫败却百年不改其志的「孤独守望者」气质；悲伤与坚韧并存的基调贴合和平运动 1914–1945 年间的沉重历史。
- **备选**（未采用，仅存档）：Timeless（百年恒久感贴切但已多处用曲）、The Invisible Light（气质偏科学家传记）。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/International_Peace_Bureau/page.md` | 本地 Wikipedia 正文（唯一事实来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节母本） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参考 |
| `peace/presentations/cover/` | OpenPeace 共享封面 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |

> **开始执行。每完成一步汇报。**
