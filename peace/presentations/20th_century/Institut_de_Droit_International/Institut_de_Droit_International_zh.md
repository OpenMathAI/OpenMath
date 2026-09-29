# OpenPeace 机构立传提示词（实例：Institute of International Law）

> **本文件是 OpenPeace 项目（诺贝尔和平奖得主立传）的机构立传提示词**，
> 以国际法研究院（Institute of International Law，1904 诺贝尔和平奖）为完整实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Institute of International Law（国际法研究院，法语 Institut de Droit International，缩写 IDI）。
- **特殊性**：本篇是**组织机构立传**（非个人），第 2 步用「机构概览页」替代个人「身份信息页」，叙事主体为机构而非个人，勿把任何一位领导人写成创始人或代言人。

---

## 二、背景信息 【人物/机构专属】

- **机构**：Institute of International Law（国际法研究院）
- **成立**：1873-09-08，比利时根特市政厅 *Salle de l'Arsenal*；总部现设瑞士日内瓦（Graduate Institute of International and Development Studies，随秘书长国籍轮换）
- **诺奖年份与官方获奖理由**：1904 年诺贝尔和平奖（机构得主）
  > 中文获奖理由（照抄名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写）：
  > **「表彰该机构致力于发展公法以促进国家间和平关系，并推动战争法规更加人道化」**
- **气质关键词**：**公法学者的议会、战争的法度化者、和平的制度工程**
- **设计母题**：**天平与法典（scales & codex）**——机构以科学方法研究并发展国际法，用「条文、决议、年鉴」为战争立法度，视觉上以法律符号与跨国界的条文线条呼应
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Institut_de_Droit_International/page.md`

---

## 三、任务流程 【模板通用骨架 + 机构专属内容】

### 第 0 步：事实基准（机构专属，第一轮已核对）

- 机构性质：NGO / 学会（private body），由 associates / members / honorary members 组成；80 岁以下成员与准成员总数不超过 132 人；成员每两年选举一次，须在国际法领域有杰出学术成就且相对不受政治压力
- 成立时间与地点：1873-09-08，根特（Ghent），比利时
- 创始人：**Gustave Moynier 与 Gustave Rolin-Jaequemyns 牵头，连同其他九位国际法学家共 11 人**（另有应邀但未及与会的 August von Bulmerincq，后被计入创始成员）：
  Pasquale Stanislao Mancini（主席，罗马）、Emile de Laveleye（列日）、Tobias Michael Carel Asser（阿姆斯特丹）、James Lorimer（爱丁堡）、Wladimir Besobrassof（圣彼得堡）、Gustave Moynier（日内瓦）、Jean Gaspar Bluntschli（海德堡）、Augusto Pierantoni（那不勒斯）、Carlos Calvo（布宜诺斯艾利斯）、Gustave Rolin-Jaequemyns（根特）、David Dudley Field（纽约）
- 运作方式：每两年一届大会（biannual congresses），研究现行国际法并通过提出修改建议的决议；**不对具体争端发表评论**
- 决议重点领域：人权法（human rights law）与和平解决争端（peaceful dispute resolution）——**这正是其获诺贝尔和平奖的原因**（page.md 明文）
- 咨询地位：ECOSOC（联合国经社理事会）与 HCCH（海牙国际私法会议）的 consultant
- 出版物：*Yearbook*（年鉴，载委员会报告、全体会议审议、宣言与决议、行政会议记录）
- 关键时间线：
  - 1873-09-08 根特成立（11 位创始人）
  - 1904 获诺贝尔和平奖
  - 2005 克拉科夫届会（page.md 所附历史照片）
  - 2023-09 昂热（Angers）第 81 届会庆祝成立 150 周年；法国三位部长与会，马克龙与古特雷斯视频致辞；发布机构历史纪录片（含多位国际法院现任法官出镜）
  - 2023-08 最近一届大会（昂热）
- 秘书长（现任）：Marcelo Kohen（page.md infobox 明载；注意：**现任秘书长 ≠ 创始人**）
- 现任成员构成：知名律师、法学学者、前大使、国际法院（ICJ）与国际海洋法法庭（ITLOS）法官
- 近年决议主题举例：普遍管辖权、临时措施、残骸制度、豁免、环境、武力使用等

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Institut_de_Droit_International/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品的 Makefile，设置 `MAIN=Institut_de_Droit_International_zh`、`VIDEO_NAME=Institut_de_Droit_International_zh`

### 第 3 步：收集图片 【机构专属】

- 机构无统一「肖像」；page.md 所附可用图为 2005 年克拉科夫届会成员合影（`IDI_Krakow_Session_2005.jpg`，250px 缩略图，可尝试经 Commons 取 500px）
- 下载失败则用装饰圆 + 天平纹章占位（机构篇允许）

### 第 4 步：使命领域梳理 + 入库（fields，与 yaml 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international law | 国际法 | 机构使命核心：研究与研制国际法 | 概览页 |
| 1 | human rights law | 人权法 | 决议重点领域之一，获奖原因 | 核心页 |
| 2 | peaceful dispute resolution | 和平解决争端 | 决议重点领域之二，获奖原因 | 核心页 |
| 3 | international law codification | 国际法编纂 | 通过决议提出对国际法的修改建议 | 决议页 |
| 4 | international law scholarship | 国际法学术研究 | 两年一会、*Yearbook* 出版与教学 | 机构页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Gustave Moynier | 无向 | 1873-09-08 根特创立，11 位创始人之一（与 Rolin-Jaequemyns 牵头） |
| founder | Gustave Rolin-Jaequemyns | 无向 | 1873-09-08 根特创立，11 位创始人之一（与 Moynier 牵头） |
| other | 联合国经社理事会 ECOSOC | 无向 | 机构为其咨询机构（consultant）；HCCH 亦然 |

- 对手方 name_en 用库内/规范形式；创始人 stub 不编造 qid
- 其余 9 位创始人与 Bulmerincq 仅在正文与时间线中列名，**不入库**（防 stub 泛滥），在提示词与正文说明即可

### 第 5 步：配色方案（manifest 预分配，勿改）

- **主色**：`#8C1515`（深绯红——法学庄重与根特血统）
- **辅色**：诺奖香槟金 `C9A227`
- badgeA–D 四分类色：badgeA 国际法（`#1F3A5F`）、badgeB 人权法（`#0E7C7B`）、badgeC 和平解决争端（`#C9A227`）、badgeD 学术与年鉴（`#6B4E71`）

### 第 6 步：规划幻灯片序列（机构篇，10–14 页）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 1904 诺贝尔和平奖 · 国际法研究院 / 1873 根特创立 + 四色 badge
02  机构概览页（★ 必做，替代身份信息页）— 成立时间/地点/性质/成员规模/总部/咨询地位/方法论
03  创立时刻：1873 根特 — 11 位创始人与 Salle de l'Arsenal
04  使命与运作 — 两年一届大会、决议机制、不对具体争端评论
05  人权法与和平解决争端 — 获奖理由所在的两大决议领域
06  1904 诺贝尔和平奖 — 获奖理由 + Nobel 官方口径
07  学术产出 — Yearbook、决议主题（普遍管辖权/豁免/环境/武力使用…）
08  成员与治理 — 132 人上限、选举制、ICJ/ITLOS 法官与前大使
09  150 周年：2023 昂热 — 马克龙/古特雷斯视频致辞、纪录片
10  遗产 — 从 1873 到今天对国际法体系的塑造
11  结尾
```

### 第 7–8 步：版式要点 + 机构篇专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 创始人归属 | 只有两个「牵头」名字：Gustave Moynier 与 Gustave Rolin-Jaequemyns；Mancini 是**首届主席**，勿写成创始人代表 |
| 现任秘书长 | Marcelo Kohen 是现任秘书长，**绝非创始人**；总部随其所在地轮换的机制勿写死 |
| 不评论个案 | 机构「不对具体争端发表评论」，勿写成调解机构或法庭 |
| 获奖原因 | page.md 明文：因其决议特别关注人权法与和平解决争端；勿编造其他颁奖理由细节 |
| 官方理由中译 | 名录口径「发展公法……战争法规更加人道化」照抄，勿改写 |
| 1904 独得 | 1904 年该机构独得和平奖，无共同得主，勿虚构 co-honored |
| 成员数 | 80 岁以下成员与准成员 ≤132（Statute 规定），勿写「约 132 人成员」之类模糊口径 |
| Bulmerincq | 应邀未及与会、后计入创始成员——勿写成现场签署人 |
| 政治敏感红线 | 150 周年马克龙/古特雷斯致辞只作客观事实记录，不加评价 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Institut de Droit International | 国际法研究院 | 勿译「国际法学会」 |
| learned society | 学术团体 | 强调私人性质，非政府间机构 |
| biannual congress | 两年一届大会 | 勿写成年会 |
| resolution | 决议 | 建议性质，无拘束力表述勿强加 |
| Yearbook | 年鉴 | 斜体书名 |
| consultant (ECOSOC) | 咨询机构 | 勿写成「成员」或「附属机构」 |
| honorary member | 名誉成员 | 三类成员之一 |

---

## 四、背景音乐 ✅（manifest 预分配，勿改）

- **选定曲目**: **SEA** — Alex-Productions
- **匹配理由**: 深海般的开阔与秩序感，匹配机构「为战争立法度、为国家间和平奠基」的百年工程气质
- **本地路径**: `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`
- **时长**: 以 ffmpeg `-shortest` 对齐页数

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Institut_de_Droit_International/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 0–11 节结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/Institut_de_Droit_International.yaml` | fields + relations 入库母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：机构篇以「机构概览页」替代身份信息页。**
