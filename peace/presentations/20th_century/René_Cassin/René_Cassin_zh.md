# 诺贝尔和平奖得主立传提示词（René Cassin，1968）

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库）。
- **本篇对象**：勒内·卡森 René Samuel Cassin（1887–1976），法国法学家，《世界人权宣言》主要起草人，1968 年诺贝尔和平奖得主。
- **设计哲学**：法学家立传以"文本的生命"为叙事主线——从一战战伤到流亡伦敦，从《世界人权宣言》修订稿到欧洲人权法院，一位法学者用条文对抗暴力。

## 二、背景信息 【人物专属】

- **姓名**：René Samuel Cassin（勒内·塞缪尔·卡森）；1887-10-05 生于法国巴约讷 ~ 1976-02-20 逝于巴黎，享年 88 岁（**生卒以正文/导语 10 月 5 日、2 月 20 日为准；infobox 与 frontmatter 有 4 月 5 日、2 月 6 日噪声**）
- **1968 年诺贝尔和平奖，官方获奖理由（EN 原文照抄 Nobel 名录，禁止改写）**：
  > "for his struggle to ensure the rights of man as stipulated in the UN Declaration."
  > 中译（照抄 `OpenPeace_20th_Century_Nobel_Laureates.md`）：表彰他为保障《世界人权宣言》所载人权而进行的斗争
- **气质关键词**：**人权利法的总建筑师、自由法国的法律大脑、战争伤员的终身代言人**
- **设计母题**：**镌刻的条文（engraved text）**——《世界人权宣言》三十条、欧洲人权法院的石柱，视觉语言用羊皮纸条文、天平、鸽羽笔。
- **本地数据源**：`peace/presentations/pages/20th_century/René_Cassin/page.md`

## 三、任务流程

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1887-10-05 巴约讷（Bayonne）~ 1976-02-20 巴黎，享年 88 岁；塞法迪犹太家庭，长于尼斯
- 国籍：法国（1941 年被维希法国剥夺国籍，1942 年被缺席判处死刑——客观事实记录）
- 家庭：page.md 未载妻子与子嗣，**无载禁写**
- 教育：尼斯 Lycée Masséna（17 岁获业士）；埃克斯-普罗旺斯法学院（政治经济学/宪政史/罗马法，法学 distinction）；1914 年巴黎大学法学·经济学·政治学博士
- 一战：1916 默兹战役率队冲锋，机枪重伤（臂/肋/腹）， Antibes 手术；获 Croix de Guerre；以战争伤残退伍
- 任职机构（含年份）：国际联盟法国代表（1924–1938）；里尔法学教授（1920）、巴黎法学教授（1929–1960）；海牙国际法学院、日内瓦高等研究院兼课；法国国务院（Council of State，1944–1959）；法国宪法委员会创始成员（1960-07-11–1971-03-02）；联合国人权委员会；海牙常设仲裁法院；欧洲人权法院法官（1959–1965）、院长（1965–1968）
- 关键荣誉：Nobel Peace Prize 1968；UN 人权奖 1968；Companion of the Liberation；Grand Cross of the Legion of Honour；Médaille militaire；Oxford 荣誉博士
- 核心事业清单：①《世界人权宣言》修订起草 ②自由法国法律建制 ③战争伤残退伍军人组织 ④国际法教育与裁军外交 ⑤犹太人组织领袖（AIU 主席）
- 关键时间线（15–20 节点）：1887 生于巴约讷 → 尼斯 Lycée Masséna → 埃克斯法学院 → 1914 巴黎博士 → 1916 默兹战役重伤 → 1918 创立法兰西战争伤残军人联合会（任主席至 1940，后荣誉主席）→ 战间期共创 Union fédérale（左翼和平主义退伍军人组织）→ 1920 里尔教授 → 1924–1938 国联代表（力推裁军与国际冲突解决建制）→ 1929 巴黎教授 → 1940-06-24 乘 SS Ettrick 赴伦敦响应戴高乐六·一八呼吁，最早追随者之一 → 1941 伦敦广播呼吁法国犹太人加入自由法国 → 1941 维希剥夺国籍 → 1942 缺席判死刑 → 1944–1959 国务院委员 → 1945 应戴高乐建议任 Alliance Israélite Universelle（AIU）主席；与 AJC/Anglo-Jewish Association 共创 Jewish Organisations 协商理事会 → 1947 创立法兰西行政科学学会（IFSA）并任首任主席 → 1947–1948 借联合国人权司 Humphrey 清单修订扩写《世界人权宣言》草案 → 1948 宣言通过 → 1959–1965 欧洲人权法院法官 → 1965–1968 任院长 → 1968 诺贝尔和平奖 + UN 人权奖 → 1968-12-11 诺奖演讲 *The Charter of Human Rights* → 1971 退出宪法委员会 → 1976-02-20 逝于巴黎 → 初葬蒙帕纳斯 → 1987 遗骸迁入先贤祠

### 第 4 步：研究领域梳理 + 入库 【与 yaml fields 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international human rights law | 国际人权法 | 《世界人权宣言》修订起草，1968 诺奖核心 | 核心页 |
| 1 | human rights | 人权 | 保障宣言所载权利的终身斗争 | 获奖页 |
| 2 | international law | 国际法 | 国联代表、海牙仲裁法院法官 | 事业页 |
| 3 | administrative law | 行政法 | IFSA 创立者、法国行政法学说建设 | 晚年页 |
| 4 | legal education | 法学教育 | 里尔/巴黎教授、海牙国际法学院兼课 | 教育页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml relations 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Charles de Gaulle | 无向 | 1940 伦敦加入自由法国，起草自由法国章程（库内已有 id=4896，沿用该名） |
| colleague | John Peters Humphrey | 无向 | 基于其人权清单产出《世界人权宣言》修订扩写稿 |
| colleague | Karim Azkoul | 无向 | 1950-11-10 联合国广播法语国家圆桌同台 |

- 入库规则：仅收 page.md 明载关系；Eden（"认识的政治人物"）仅一面之词、AIU/AJC 等组织关系不入库；Azkoul 行 note **不写锡安主义分歧**（政治敏感）。

### 第 5 步：设计配色方案 【manifest 预分配，勿改主色】

- **主色**：`#14324F`（深海军蓝——法国蓝与法学的庄重）
- **辅助**：诺奖香槟金 `#C9A227` + 四分类色：
  - badgeA 人权法 — 玫瑰 `#C4204F`
  - badgeB 自由法国 — 军蓝 `#3A5A78`
  - badgeC 国际仲裁 — 青绿 `#0E7C7B`
  - badgeD 法学教育 — 琥珀 `#E07B30`
- **背景母题**：柔和圆点 + 细条文线（呼应宣言条文）。

### 第 6 步：幻灯片序列（10–16 页规划）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 人权宣言的总建筑师 / René Cassin 1887–1976 + 四色 badge + 肖像位
02  身份信息页（★ 必做）— 生卒/出生地/国籍/教育/任职/荣誉/核心领域
03  核心贡献概览 — 宣言起草 / 自由法国 / 退伍军人组织 / 国际法与仲裁
04  早年：巴约讷与尼斯 (1887–1914) — 17 岁业士、埃克斯、1914 巴黎博士
05  一战：默兹战役的战伤 (1916) — 重伤、Croix de Guerre、战争伤残退伍
06  战间期：为伤残者与和平立法 (1918–1939) — 伤残军人联合会、Union fédérale、国联裁军
07  1940：伦敦的抉择 — SS Ettrick、自由法国章程、1942 缺席死刑（客观记录）
08  《世界人权宣言》：从 Humphrey 清单到 Cassin 草案（核心贡献页）
09  战后建制：国务院与宪法委员会 (1944–1971)
10  欧洲人权法院：法官与院长 (1959–1968)
11  AIU 与犹太组织网络 (1945–) — 戴高乐建议、协商理事会共创
12  1968 诺贝尔和平奖 — 官方理由原文 + 中译 + 12-11 演讲
13  荣誉与认可 — UN 人权奖 1968 · 解放同伴勋章 · 1987 先贤祠
14  遗产：以条文护佑人权
15  结尾
```

### 第 7 步：版式要点 【模板通用骨架 + 人物专属】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 实现。
- 配色宏统一 `mainclr/accentclr/badgeA..D/panelA..D`，注释写语义。
- 表格页安全负间距：顶部 -0.35cm、`arraystretch 0.78–0.82`。

### 第 8 步：本人物专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 生卒日噪声 | frontmatter 双值 02-05/10-05、infobox 04-05；正文与导语一致 **1887-10-05**；卒日 infobox 02-06 vs 正文 02-20，**以正文 1976-02-20 为准** |
| 宣言贡献定位 | Cassin 是 "major contributor"：基于 Humphrey 清单"产出修订稿并扩写文本"（page.md 明载），**勿写"独笔起草"**，也勿忽略 Humphrey 的原始清单 |
| 维希迫害 | 1941 剥夺国籍、1942 缺席判死刑是 page.md 明载客观事实，只可客观记录，**禁加评价性形容** |
| 锡安主义 | Karim Azkoul 段涉 Zionism 政治评价——**整段敏感内容禁入正文与关系 note** |
| 1932 教授年份 | 1920 里尔、1929 巴黎（正文口径）；执教至 1960 |
| 同名区分 | 与经济史家等无关；本篇唯一 Cassin；先贤祠入葬年份 1987（迁葬），勿写卒年 |
| 无载禁写 | 妻离子女、罗斯福夫人合作细节、宣言逐条归属（除 Humphrey 清单+Cassin 扩写外）page.md 未载一律不写 |
| 诺奖口径 | 获奖理由 "for his struggle to ensure the rights of man as stipulated in the UN Declaration"，单人不共享 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险点 |
|------|------|------|
| Universal Declaration of Human Rights | 世界人权宣言 | 1948 联大通过 |
| Free France | 自由法国 | 1940 伦敦，非"流亡政府"泛称 |
| Council of State (France) | 法国国务院 | 最高行政法院，1944–1959 |
| Constitutional Council | 宪法委员会 | 1960 创始成员至 1971 |
| European Court of Human Rights | 欧洲人权法院 | 1959–65 法官、1965–68 院长 |
| Permanent Court of Arbitration | 海牙常设仲裁法院 | 任职明载 |
| Croix de Guerre | 战争十字勋章 | 1916 默兹战役 |
| Alliance Israélite Universelle | 世界以色列联盟 | 1945 起任主席 |
| IFSA | 法兰西行政科学学会 | 1947 创立、首任主席 |
| Panthéon | 先贤祠 | 1987 迁葬 |

---

## 四、背景音乐 ✅ 【manifest 预分配，勿改】

- **选定曲目**：**Cinematic Experience** — Alex-Productions
- **匹配理由**："史诗/电影感" 匹配其人生弧线——战伤、流亡、宣言、法院；1940 年伦敦抉择与 1948 年宣言通过的戏剧张力与纪录片叙事相称。
- **本地路径**：`music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/René_Cassin/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

---

## 六、执行清单

1. 建 `peace/presentations/20th_century/René_Cassin/` 目录 + `images/`；下载 Cassin 肖像（page.md 图库有 Forbach 纪念像与伦敦法国民族委员会合影，人物真实照片若 404 用装饰圆占位）。
2. 复制 Makefile，设 `MAIN=René_Cassin_zh`、`VIDEO_NAME=René_Cassin_zh`（宏/文件名避免生僻字符可改 `Rene_Cassin_zh`）。
3. 按 §三 第 6 步序列写 tex；每写一页 make 检查溢出（vbox≤10pt、hbox≤50pt）。
4. `pdftoppm` 逐页目检 → make images/video。
5. yaml 入库：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/René_Cassin.yaml`；验证 has_social_data=1。

---

## 七、版式补遗

- 文件名含 é：Makefile 变量与 xelatex 兼容，但建议目录内保持一致命名；若编译报错降级为 ASCII 名。
- 结尾页底部品牌统一 `OpenMathAI`；引号用半角 `" "`。
- \foreach 时间线分隔符必须 ASCII 逗号；宏名禁数字。
