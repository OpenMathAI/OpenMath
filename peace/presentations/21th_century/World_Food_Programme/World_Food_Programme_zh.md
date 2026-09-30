# OpenPeace 立传提示词：World Food Programme（世界粮食计划署，2020 诺贝尔和平奖）

> 本文件是 OpenPeace 21 世纪批次的人物专属立传提示词（**组织机构篇**），结构对齐标杆
> `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库）。
- **本实例**：World Food Programme（世界粮食计划署，WFP），2020 年诺贝尔和平奖得主，联合国体系内全球最大人道主义组织。**组织机构篇：用「机构概览页」替代身份信息页，无生平叙事，以使命/运作/治理为主线。**
- **设计哲学**：机构立传的核心是**把使命变成可图形化的领域图**——从紧急救济到气候韧性、从学校供餐到区块链援助，呈现「粮食即和平」的工作谱系。

---

## 二、背景信息 【机构专属】

- **目标机构**：World Food Programme（WFP，世界粮食计划署）
- **成立**：1961-12-19（infobox 明载 Formation）；1963 年由 FAO 与联合国大会以三年试验期启动首批项目（苏丹 Wadi Halfa 努比亚人援助）；1965 年转为常设
- **气质关键词**：**最大的人道组织、零饥饿引擎、粮食和平论** —— 2020 年诺贝尔和平奖获奖理由：
  > "for its efforts to combat hunger, for its contribution to bettering conditions for peace in conflict-affected areas and for acting as a driving force in efforts to prevent the use of hunger as a weapon of war and conflict."（表彰其为战胜饥饿所做的努力、对改善冲突地区和平条件的贡献，以及在防止将饥饿用作战争与冲突武器方面的推动作用）
- **设计母题**：**麦穗与罗盘（wheat and compass）**——全球粮食走廊与罗盘式导航；视觉可用麦穗环绕的地球与航线网。
- **本地数据源**：`peace/presentations/pages/21th_century/World_Food_Programme/page.md`
- **参考模板**： physicist 侧标杆 `Kenneth_G_Wilson_zh.tex` 骨架。

---

## 三、任务流程 【模板通用骨架 + 机构专属内容】

### 第 0 步：事实基准 【机构专属，已核对 page.md】

- 性质：联合国体系内国际组织（政府间组织），母机构为联合国大会；总部罗马，87 国设办公室，120+ 国家和地区有存在
- 规模：2023 年员工 22,300+；2023 年援助超 1.52 亿人；全球最大人道主义组织、学校供餐首要提供者
- 治理：执行局由 36 个成员国代表组成（经社理事会 18 + FAO 18）；欧盟为常驻观察员；执行主任由联合国秘书长与 FAO 总干事联合任命，任期五年
- 首任执行主任：Addeke Hendrik Boerma（荷兰，1962-05–1967-12）；2020 诺奖受奖时执行主任 David Beasley（2017-04–2023-04）；2026-09 起Luke Lindberg
- 缘起：1960 年 FAO 大会后，美国 Food for Peace 计划主任 George McGovern 提议建立多边粮食援助计划
- 使命领域：紧急粮食救济；应急准备与响应能力建设；供应链与物流（Logistics Cluster 主导机构、UNHAS 人道航空服务 300+ 目的地、UNHRD 全球枢纽）；社会安全网；气候韧性；现金援助（2022 上半年 16 亿美元/70 国 3,700 万人）；SDG 2「零饥饿」（联合国可持续发展集团执行成员）
- 标志性项目：Purchase for Progress（P4P，2008 五年试点、20 国、培训 80 万农民、36.6 万吨粮食、农户增收 1.48 亿美元）；Food Assistance for Assets（FFA）；Building Blocks（2017，约旦叙利亚难民区块链粮食援助，虹膜识别）；SMP PLUS（AI 学校餐单工具）；创新加速器 60+ 项目/45 国
- 资金：依赖政府/企业/个人自愿捐款；2022 年创纪录 141 亿美元（需求 214 亿）；2023 年 83 亿（2010 年以来首次下降，缺口 64%）；美国为最大捐助国；2025-02 美国政府指示停用多笔 USAID 资助项目（Rubio 紧急豁免部分基本粮食援助）
- 2020 诺奖：应对饥饿的努力、改善冲突地区和平条件、防止饥饿被用作战争武器；受奖时 Beasley 呼吁亿万富翁出资 50 亿美元救助 3,000 万濒临饥荒人口
- 批评（page.md 明载，两说并陈）：2018 年全球发展中心在 40 个援助项目研究中将 WFP 排名末位（效率/制度建设/负担/透明度四组指标）；内部文化问题（性骚扰）调查报道存在；援助净效力的一般性辩论
- 关键时间线（15 节点）：1961-12-19 成立（McGovern 提议）→ 1963 首批项目（Wadi Halfa）→ 1965 转常设 → 1962 首任执行主任 Boerma 就任 → 1992–2002 Catherine Bertini 任期 → 2008 P4P 试点 → 2012–2017 Ertharin Cousin → 2013 加入国际援助透明度倡议（IATI 第 150 成员）→ 2017 Building Blocks 上线 → 2017-04 David Beasley 就任 → 2019-03 Idai 气旋莫桑比克响应 → 2020-07 苏丹洪灾 16 万人援助 → 2020-10-09 诺贝尔和平奖 → 2022 资金创纪录 141 亿美元 → 2023-03 Cindy McCain 就任 → 2023 援助 1.52 亿人 → 2025-02 美国 USAID 项目停摆指令 → 2026 Lindberg 就任

### 第 4 步：使命领域表（4–5 行）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | food assistance | 粮食援助 | 核心使命，2020 诺奖理由 | 诺奖页 |
| 1 | food security | 粮食安全 | SDG 2 零饥饿优先 | 使命页 |
| 2 | humanitarian logistics | 人道物流 | Logistics Cluster、UNHAS、UNHRD | 运作页 |
| 3 | school meals | 学校供餐 | 全球首要提供者 | 项目页 |
| 4 | emergency relief | 紧急救济 | 突发灾害第一响应 | 应急页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| other | United Nations | — | 隶属联合国体系，母机构为联合国大会 |
| other | Food and Agriculture Organization | — | 与 FAO、联大共同发起设立；执行主任由联合国秘书长与 FAO 总干事联合任命 |
| colleague | Addeke Hendrik Boerma | 无向 | 首任执行主任（1962-05–1967-12） |
| colleague | David Beasley | 无向 | 2017–2023 执行主任，2020 诺奖受奖时领奖并呼吁筹资 |
| other | George McGovern | — | 设立提案人（美国 Food for Peace 计划主任） |

> 不入库（仅叙述）：历届其余 13 位执行主任（列表过长，幻灯片精选叙述）；World Food Program USA（税务独立实体）；FAO/IFAD 三方联合声明；执行局与欧盟观察员。

### 第 5 步：配色方案 【manifest 预分配，勿改主色】

- **主色**：深青绿 `#145C54`（粮食、生命）
- **辅助**：诺奖香槟金 `C9A227`
- **badge 四色**（使命分类）：
  - `badgeFA` 粮食援助 — 青绿 `#0E7C7B`
  - `badgeHL` 人道物流 — 琥珀 `#E07B30`
  - `badgeSM` 学校供餐 — 靛蓝 `#4C5FD5`
  - `badgeER` 紧急救济 — 玫瑰 `#C4204F`
- **背景母题**：麦穗弧线与航线网（点线连缀的全球网络），主色渐变

### 第 6 步：规划幻灯片序列（12 页 = 共享封面 + 11 帧）

```
00  OpenPeace 项目首页（\input cover 共享首页）
01  封面 — 零饥饿的全球引擎 / World Food Programme 1961– + 四色 badge + 机构行
02  机构概览页（★ 必做，替代身份信息页）— 成立/总部/隶属/规模/治理/使命/诺奖
03  使命概览 — 粮食援助 / 粮食安全 / 人道物流 / 学校供餐 / 紧急救济
04  缘起 (1961–1965) — McGovern 提议、FAO+联大试验启动、Wadi Halfa、转常设
05  诺贝尔和平奖 2020 — 获奖理由 EN+中译；Beasley 领奖与筹资呼吁
06  应急响应 — 武装冲突与粮食不安全（60%+ 饥饿人口生活在武装暴力地区）、
    热点展望（Haiti/Mali/Palestine/South Sudan/Sudan）、洪灾与气旋响应
07  人道物流 — Logistics Cluster、UNHAS 300+ 目的地、UNHRD、COVID-19 期间通达
08  气候与韧性 — 孟加拉预警现金、巴哈马 Dorian 飓风、萨赫勒集水与土地恢复
09  营养·学校供餐·小农 — P4P 数据、Farm to Market Alliance、FFA
10  现金援助与数字创新 — 2022 上半年 16 亿美元/70 国、ESSN 研究结论、
    Building Blocks 区块链、SMP PLUS、创新加速器
11  治理·资金·批评（两说并陈）+ 结尾 — 36 国执行局、16 任执行主任时间带、
    志愿捐款波动（2022 峰值/2023 缺口 64%/2025 USAID 停摆）、
    CGD 2018 排名与内部文化问题（注明"研究报告/调查显示"）
```

### 第 7–8 步：版式要点 + 本篇专属陷阱表

- 机构无生平，第 02 页用「信息网格」呈现机构档案（成立/总部/母机构/规模/治理/现任首长）；时间带页用 \foreach 时间线（**分隔符必须 ASCII 逗号**）。

| 陷阱 | 说明 |
|------|------|
| ★勿把领导人写成创始人 | 执行主任是行政首长**非创始人**；设立提案人是 George McGovern；组织由 FAO+联大发起 |
| 成立三日期 | 1961-12-19 成立 / 1963 启动首批项目（三年试验）/ 1965 转常设——三者勿混 |
| 诺奖理由结构 | 三层并列（战胜饥饿/改善冲突地区和平条件/防止饥饿武器化），EN+中译整句照抄，勿拆改 |
| 敏感地区表述 | Gaza/乌克兰/也门/苏丹等行动地区与 2025 Houthi 扣押事件**只按 page.md 客观记录，零评价、零立场**；2025 美国 USAID 停摆指令亦只作事实记录 |
| 资金数字 | 2022=141 亿（需求 214 亿）、2023=83 亿（缺口 64%）、2022 上半年现金=16 亿美元/70 国/3,700 万人——勿互串 |
| 批评归属 | CGD 2018 排名末位、"internal culture problems including sexual harassment"——必须写"研究报告显示/据调查"，零引申 |
| P4P 数据包 | 20 国/80 万农民/36.6 万吨/1.48 亿美元——四数字成组勿拆 |
| 规模口径 | 员工 22,300+（2023）、2023 援助 1.52 亿人、87 国办公室、120+ 国家和地区存在——勿混 |
| UNHAS 全称 | United Nations Humanitarian Air Service（WFP 管理），非"联合国航空署" |
| 现任首长 | 2026-09 起 Luke Lindberg；McCain 2023-03–2026-05；Skau 代职 2026-05–09（按 page.md 时间线） |

### 第 9 步：术语清单（8–12 条）

| 英文 | 中文 | 风险点 |
|------|------|------|
| World Food Programme (WFP) | 世界粮食计划署 | 联合国机构名，勿译"世界粮食署" |
| food assistance | 粮食援助 | 诺奖理由核心词 |
| zero hunger (SDG 2) | 零饥饿 | 可持续发展目标 2 |
| Logistics Cluster | 物流集群 | IASC 协调机制，WFP 主导 |
| UNHAS | 联合国人道航空服务 | WFP 管理，300+ 目的地 |
| UNHRD | 联合国人道响应仓库 | 全球枢纽网络 |
| Purchase for Progress (P4P) | 购粮于农进步计划 | 2008 试点，数字成组 |
| Building Blocks | 区块链援助项目 | 2017 约旦叙利亚难民场景 |
| cash transfer | 现金转移支付 | 实物/银行卡/代金券三种 |
| Hunger Hotspots | 饥饿热点展望 | WFP 与 FAO 联合发布 |
| Food Assistance for Assets (FFA) | 资产型粮食援助 | 以工代赈转向 |
| executive board | 执行局 | 36 国（经社 18+FAO 18） |

---

## 四、背景音乐选择 ✅ 【manifest 预分配，勿改】

- **选定曲目**: **With Me** — Alex-Productions
- **bgm_path**: `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav`
- **匹配理由**: 温暖坚定的合奏质感，匹配"与饥饿人口同行"的全球人道协作叙事——宏大而不煽情。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/World_Food_Programme/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节） |
| `MySQL/data/World_Food_Programme.yaml` | 社会关系/领域入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步汇报。**
> **最重要的事：无载禁写；机构领导人≠创始人；敏感地区行动只作客观记录。**
