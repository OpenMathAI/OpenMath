# OpenPeace 立传提示词：Abiy Ahmed（阿比·艾哈迈德，2019 诺贝尔和平奖）

> 本文件是 OpenPeace 21 世纪批次的人物专属立传提示词，结构对齐标杆
> `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库）。
- **本实例**：Abiy Ahmed Ali（阿比·艾哈迈德·阿里），2019 年诺贝尔和平奖得主，埃塞俄比亚现任总理（2018-04-02 就任）。
- **设计哲学**：本篇是典型「在任政治人物」立传——以**诺奖理由（埃厄和平）为叙事中轴**，前后按 page.md 客观并陈其军旅/情报/改革轨迹与后续争议，**全程零评价**，两说并陈。

---

## 二、背景信息 【人物专属】

- **目标人物**：Abiy Ahmed Ali（1976-08-15 生于埃塞俄比亚 Beshasha，在世）
- **气质关键词**：**和平撮合者、改革者、争议中的在任者** —— 2019 年诺贝尔和平奖获奖理由：
  > "for his efforts to achieve peace and international cooperation, and in particular for his decisive initiative to resolve the border conflict with neighbouring Eritrea."（表彰他为实现和平与国际合作所做的努力，尤其是为解决与邻国厄立特里亚边界冲突采取的决定性行动）
- **设计母题**：**握手与桥（handshake and bridge）**——2018-07-09 亚的斯亚贝巴与阿斯马拉之间的「和平与友好联合宣言」；视觉可用跨越裂谷的桥与握手剪影。
- **本地数据源**：`peace/presentations/pages/21th_century/Abiy_Ahmed/page.md`
- **参考模板**： physicist 侧标杆 `Kenneth_G_Wilson_zh.tex` 骨架。

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 出生：1976-08-15，埃塞俄比亚 Beshasha 小镇；父 Ahmed Ali 为穆斯林奥罗莫长者，母 Tezeta Wolde；父之第 13 子、母之第 6 子（最小）；乳名 Abiyot（意为"革命"）
- 母亲族裔两说：2018 年对《纽约时报》称母为阿姆哈拉人、东正教徒婚后改宗伊斯兰；2021 年 Oromia 广播访谈又称父母均为奥罗莫人（两说并陈，勿裁决）
- 军旅：14 岁（1991 年初）加入反对门格斯图政权的武装（OPDO，约 200 人，隶属 EPRDF 联军）；Derg 倒台后受正式军训（Assefa 旅，West Wollega）；1993 入埃塞国防军（ENDF）情报与通信部门；1995 驻卢旺达 UNAMIR；1998–2000 埃厄战争任无线电/情报军官；军衔中校；2010 退役从政
- 信仰：2000 年 6 月战争中险些阵亡后改宗五旬节基督教；属埃塞俄比亚全福信教会，偶有讲道
- 教育（均为服役期间在职攻读）：Microlink 信息与技术学院计算机工程学士（2009）→ University of Greenwich 转型领导力硕士（2011）→ Leadstar 管理学院 MBA（与 Ashland University 合作，2013）→ 亚的斯亚贝巴大学和平与安全研究所博士（2016 提交、2017 答辩；论文题目 *Social Capital and its Role in Traditional Conflict Resolution in Ethiopia: The Case of Inter-Religious Conflict In Jimma Zone State*，导师 Amr Abdallah）
- 仕途时间线：2006 参与创建信息安全局 INSA（仿美国 NSA）并历任要职、约两年代理局长 → 2010 当选联邦人民代表院议员（Agaro 选区）→ 2014 出任科技信息中心（STIC）主任 → 2015-10 科技部长（约 12 个月）→ 2016-10 奥罗米亚州副州长（州长 Lemma Megersa 班子）→ 2017-10 任 ODP 秘书处负责人 → 2018-02-22 接任 ODP 主席 → 2018-03-27 当选 EPRDF 主席（108 票 vs Shiferaw 58、Debretsion 2）→ 2018-04-02 当选总理并宣誓 → 2019-12-01 解散 EPRDF、组建繁荣党并任主席
- 总理任期关键事实（page.md 明载）：
  - 释放数千政治犯（2018-05 单奥罗米亚赦免逾 7,600 人）；邀请流亡媒体回归；修改反恐法；提前结束紧急状态（2018-06-04 议会批准）
  - 经济改革：国企（含埃塞俄比亚航空）部分/全部私有化、电信/航空/电力/物流打破垄断、筹建证券交易所
  - 内阁改组：部委 28→20、一半阁员为女性（首位女总统 Sahle-Work Zewde、首位女国防部长等）
  - 2018-06-23 梅斯克尔广场手榴弹袭击（2 死 165+ 伤，其本人无恙）
  - 2018-07-08 阿斯马拉峰会：20 余年来埃塞领导人首会厄方；7 月 9 签《和平与友好联合宣言》（复交、重开直航/电信/公路、马萨瓦与阿萨布港使用权）
  - Green Legacy Initiative（绿色遗产植树运动）；2022 Green Legacy 获美国成就学院奖
  - 2020-06 大选因 COVID-19 推迟、2021 年举行（非盟评"较 2015 年有改善"）
  - 2020-11 提格雷战争爆发（TPLF 攻击 ENDF 北方司令部起，历时两年，致严重人道危机与流离失所）；2022-11《比勒陀利亚协议》结束战争；2023 起推动地方武装整编，Fano 拒绝并引发阿姆哈拉战争
- 争议（page.md 明载，**两说并陈、零评价**）：
  - 自 2019 年起，HRW/CPJ/大赦国际等组织指其政府逮捕记者、关闭媒体、暂停路透社记者证、警告 BBC/DW 记者；2021 年 46 名记者被拘
  - 互联网关闭：HRW/NetBlocks/Access Now 指关闭频次与时长加剧
  - 学界对博士论文的批评：2023 年 Alex de Waal 等建议亚的斯亚贝巴大学复核其论文是否存在抄袭（此为指控方观点，须注明"de Waal 等人称/建议复核"）
  - 2021-06 多国代表呼吁重新考虑其和平奖；Guardian 评论员 Tisdall 撰文主张退还；Change.org 请愿至 2021-09 约 3 万签名
  - 埃厄和平协议被描述为"largely unimplemented"（批评者观点），2020-07 厄信息部声明埃军仍驻其领土
- 关键荣誉：Nobel Peace Prize 2019（2019-10-11 宣布）；Félix Houphouët-Boigny–UNESCO 和平奖 2019；黑森和平奖 2019；乌干达"非洲之珠"勋章 2018；阿联酋扎耶德勋章 2018；沙特阿卜杜勒-阿齐兹国王勋章 2018；埃塞正教会"和平与和解"特别奖 2018；Time 100（2018/2019）
- 家庭：妻 Zinash Tayachew（阿姆哈拉人、福音歌手，两人同在 ENDF 服役时结婚）；三女一养子；会奥罗莫语、阿姆哈拉语、提格雷尼亚语、英语
- 关键时间线（18 节点）：1976 生于 Beshasha → 1991-14 岁加入反 Derg 武装（OPDO）→ 1993 入 ENDF → 1995 UNAMIR 卢旺达 → 1998–2000 埃厄战争情报军官 → 2000-06 险些阵亡后改宗五旬节 → 2006 参与创建 INSA → 2009 计算机工程学士 → 2010 退役、当选议员（Agaro）→ 2011/2013 硕士+MBA → 2014 STIC 主任 → 2015-10 科技部长 → 2016-10 奥罗米亚副州长 → 2018-02-22 ODP 主席 → 2018-03-27 EPRDF 主席 → 2018-04-02 就任总理 → 2018-07-08/09 阿斯马拉峰会+《和平与友好联合宣言》→ 2019-10-11 诺贝尔和平奖 → 2019-12-01 繁荣党成立 → 2020-11 提格雷战争爆发 → 2022-11 比勒陀利亚协议 → 2023 阿姆哈拉战争

### 第 4 步：事业领域表（4–5 行）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace diplomacy | 和平外交 | 埃厄和解，2019 诺奖核心 | 诺奖页 |
| 1 | political reform | 政治改革 | 释放政治犯、开放政治空间 | 改革页 |
| 2 | economic liberalization | 经济自由化 | 国企私有化、开放关键部门 | 经济页 |
| 3 | conflict resolution | 冲突调解 | 博士论文主题、宗教和平论坛 | 学历页 |
| 4 | religious reconciliation | 宗教和解 | Religious Forum for Peace、正教会奖 | 和解页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Zinash Tayachew | 无向 | 福音歌手，两人同在 ENDF 服役时结婚，育三女一养子 |
| advisor-student | Amr Abdallah | 师→生（博士导师） | 亚的斯亚贝巴大学博士论文导师 |
| colleague | Isaias Afwerki | 无向 | 厄立特里亚总统，2018-07-09 签署和平与友好联合宣言 |
| colleague | Lemma Megersa | 无向 | 奥罗米亚州长班子共事，2018 ODP 主席接任其位 |
| colleague | Hailemariam Desalegn | 无向 | 总理前任，2018-02-15 辞职引发党魁竞选 |

> 不入库（仅叙述）：Demeke Mekonnen / Shiferaw Shigute / Debretsion Gebremichael（2018 党魁竞选对手，选战事实在幻灯片叙述）；Sahle-Work Zewde 等内阁任命；Mohammed Hussein Al Amoudi（获释事件）；各外国领导人会面（普京/拜登/马克龙/默克尔/莫迪等，仅握手合影非稳定关系）；Mary Robinson（Tipperary 奖同届提名）。

### 第 5 步：配色方案 【manifest 预分配，勿改主色】

- **主色**：靛蓝紫 `#283593`（庄重、外交）
- **辅助**：诺奖香槟金 `C9A227`
- **badge 四色**（事业分类）：
  - `badgePD` 和平外交 — 青绿 `#0E7C7B`
  - `badgePR` 政治改革 — 琥珀 `#E07B30`
  - `badgeEL` 经济自由化 — 靛蓝 `#4C5FD5`
  - `badgeRR` 宗教和解 — 玫瑰 `#C4204F`
- **背景母题**：桥形几何与握手剪影，主色渐变

### 第 6 步：规划幻灯片序列（13 页 = 共享封面 + 12 帧）

```
00  OpenPeace 项目首页（\input cover 共享首页）
01  封面 — 埃厄和平的撮合者 / Abiy Ahmed 1976– + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 生卒/出生地/家庭/教育/军旅/党职/主要荣誉/核心领域
03  核心事业概览 — 和平外交 / 政治改革 / 经济自由化 / 冲突调解 / 宗教和解
04  早年与军旅 (1976–2010) — Beshasha、14 岁入伍、UNAMIR、埃厄战争、中校
05  情报与转型 (2006–2015) — INSA 共同创建、议员、STIC、科技部长
06  飙升之路 (2015–2018) — 奥罗米亚副州长、ODP 主席、EPRDF 党魁竞选 108:58:2
07  总理百日改革 (2018) — 释放政治犯、反恐法修改、紧急状态提前解除、女性过半内阁
08  埃厄和平：诺奖核心 — 2018-07 阿斯马拉峰会、联合宣言、复交与港口
09  诺贝尔和平奖 2019 — 获奖理由 EN+中译；奥斯陆受奖
10  任内延续 (2019–2024) — 繁荣党、2021 大选、绿色遗产、对外交往
11  争议与批评（两说并陈）— 提格雷战争与比勒陀利亚协议 / 记者拘押与网络关闭（NGO 观点）/ 诺贝尔奖撤销呼吁 / 论文复核之争——全部注明"批评者/组织称"，零评价
12  结尾 — 家庭与信仰 + 遗产两说
```

### 第 7–8 步：版式要点 + 本篇专属陷阱表

- 第 11 页信息量大，用双栏 itemize（\topsep=0、\itemsep=-2.5pt）+ arraystretch 0.62 控制高度；标题勿用"评价性"字眼，用「争议与批评（两说并陈）」。

| 陷阱 | 说明 |
|------|------|
| ★政治敏感红线 | 提格雷战争、阿姆哈拉战争、厄立特里亚、埃及大坝争端、民主倒退指控——**全部按 page.md 客观事实记录，零评价、零立场**；指控内容必须标注归属（"HRW 称""批评者认为"），不使用煽动性引语（如"geographic prison""No force can stop..."等战争/主权言论**禁用**） |
| 诺贝尔奖争议 | "撤销/重新考虑和平奖"是 page.md 明载事件（多国代表呼吁、Tisdall 文章、请愿 3 万签），只作事实并陈，注明来源，勿写成定论 |
| 母亲族裔两说 | 2018 NYT 访谈 vs 2021 OBN 访谈两说并陈，勿裁决 |
| 党魁竞选票数 | 2018-03-27：Abiy 108 / Shiferaw 58 / Debretsion 2（勿写成"全票"） |
| 就任日期 | 2018-04-02 由人民代表院选出并宣誓；党魁 2018-03-27、ODP 主席 2018-02-22 三者勿混 |
| INSA 数字 | INSA 2006 年成立（正文），2008–2015 任职为 infobox 口径；"约两年代理局长"勿写成任期首脑 |
| 学位口径 | 三硕一博均为在职获得；Greenwich 硕士 2011、Leadstar MBA 2013、博士 2016 提交 2017 答辩 |
| 论文争议 | 2023 de Waal 等建议复核抄袭——必须写"de Waal 等人称/建议"，其"perhaps enough for an undergraduate paper"等评价引语**禁用** |
| 埃厄协议现状 | "largely unimplemented"是批评者描述；2020-07 厄方声明引语勿转述成事实 |
| 名字全称 | Abiy Ahmed Ali（正文）；党职多任更替时间线须逐一对表，勿压缩 |
| 荣誉完整性 | UNESCO 2019、黑森 2019、非洲之珠 2018、扎耶德 2018、阿卜杜勒-阿齐兹 2018、正教会 2018；FAO Agricola Medal 2024 勿漏 |

### 第 9 步：术语清单（8–12 条）

| 英文 | 中文 | 风险点 |
|------|------|------|
| Eritrea–Ethiopia border conflict | 埃厄边界冲突 | 诺奖理由核心，勿写成"埃塞-厄立特里亚战争"泛称 |
| Joint Declaration of Peace and Friendship | 和平与友好联合宣言 | 2018-07-09 签署 |
| Algiers Agreement (2000) | 阿尔及尔协定 | 巴德梅归属裁决依据 |
| Badme | 巴德梅 | 争议边境小镇，2018-06 宣布移交 |
| EPRDF | 埃塞俄比亚人民革命民主阵线 | 执政联盟，2019-12 解散 |
| Prosperity Party | 繁荣党 | 2019-12-01 成立 |
| INSA | 信息网络安全局 | 仿美国 NSA，2006 成立 |
| ODP / OPDO | 奥罗莫民主党 | 前身 OPDO，勿混 |
| Tigray War | 提格雷战争 | 2020-11 至 2022-11，客观记录 |
| Pretoria Agreement | 比勒陀利亚协议 | 2022-11 结束提格雷战争 |
| Green Legacy Initiative | 绿色遗产倡议 | 植树运动 |
| Religious Forum for Peace | 宗教和平论坛 | 吉马州宗教和解机制 |

---

## 四、背景音乐选择 ✅ 【manifest 预分配，勿改】

- **选定曲目**: **Tragedy** — Alex-Productions
- **bgm_path**: `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`
- **匹配理由**: 沉重而克制的叙事底色，匹配"和平功业与后续战火并陈"的双面传记——不渲染悲情，也不作颂扬。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Abiy_Ahmed/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节） |
| `MySQL/data/Abiy_Ahmed.yaml` | 社会关系/领域入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步汇报。**
> **最重要的事：无载禁写；政治敏感内容只作 page.md 明载的客观记录，指控必注归属。**
