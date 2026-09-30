# OpenPeace 21 世纪和平奖得主立传提示词（实例：ICAN）

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他学科侧共享体系）。
- **本实例**：International Campaign to Abolish Nuclear Weapons（国际废除核武器运动，ICAN），2017 诺贝尔和平奖得主，全球公民社会联盟（**组织机构条目，is_org=true**）。
- **设计哲学**：机构立传以「机构概览页」替代个人身份信息页；以「从禁雷到禁核」为母题——公民社会联盟把人道主义视角带进裁军谈判。

---

## 二、背景信息 【人物专属】

- **目标机构**：International Campaign to Abolish Nuclear Weapons（ICAN；2006-09 IPPNW 赫尔辛基大会通过提案，2007-04-23 在墨尔本公开启动，总部日内瓦）
- **气质关键词**：**禁核公民联盟、人道主义裁军旗手、TPNW 推动者**
- **2017 官方获奖理由**（照抄名录，禁止改写）：
  > "for its work to draw attention to the catastrophic humanitarian consequences of any use of nuclear weapons and for its ground-breaking efforts to achieve a treaty-based prohibition of such weapons."
  > （表彰其唤起世人关注任何使用核武器行为的人道主义灾难性后果，并开创性地推动以条约禁绝此类武器）
- **设计母题**：**和平鸽与断链（禁绝核武）**。被剪断的锁链几何元素 + 日内瓦鸽形母题，呼应「以条约禁绝此类武器」。
- **本地数据源**：`peace/presentations/pages/21th_century/International_Campaign_to_Abolish_Nuclear_Weapons/page.md`
- **结构标杆**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节结构）
- **yaml 母本**：`MySQL/data/Frederick_Sanger.yaml`
- **库内复用**：ICAN 已有 stub（people id=6808），yaml `name_en` 沿用库内形式，seed_person.py 走 UPD 回填 QID=Q547940，勿新建。

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属】

- 性质：非营利国际运动／全球公民社会联盟，致力于推动《禁止核武器条约》（TPNW）的签署与全面落实。
- 成立：2006-09-07 IPPNW（国际防止核战争医生组织，1985 和平奖得主）在芬兰赫尔辛基双年大会上通过提案；2007-04-23 于澳大利亚墨尔本首次公开启动（澳大利亚分部 MAPW 负责筹资协调），2007-04-30 在维也纳《不扩散核武器条约》筹备会上国际启动。
- 总部：瑞士日内瓦（团队驻日内瓦负责协调）。2022 年成员规模：110 个国家 661 个伙伴组织。
- 领导人：Beatrice Fihn（2014-07-01 任执行主任，直至退休）；Daniel Högsta 任临时主任；现执行主任 Melissa Parke（infobox）；2021 起瑞士注册协会负责人 Akira Kawasaki（主席）、Clara Levin（司库）、Rebecca Johnson（秘书）。国际指导小组成员包括 IPPNW、WILPF（国际妇女争取和平与自由联盟）、Norwegian People's Aid、PAX、Peace Boat、Article 36 等。
- 使命：把裁军讨论重构为以人道主义威胁为中心（毁灭能力、健康与环境灾难、无差别打击、对医疗与救援的瘫痪性影响、长期辐射）。
- 关键荣誉：2017 诺贝尔和平奖（2017-10-06 宣布，独得）；2017 意大利 Archivio Disarmo「金鸽和平奖」。
- 核心事业清单：
  1. 以人道主义视角重构核裁军话语
  2. 推动奥斯陆/纳亚里特/维也纳三届核武器人道主义影响会议的公民社会参与
  3. 「Humanitarian Pledge」人道主义承诺动员（127 国签署）
  4. 推动 TPNW 谈判、通过（2017-07-07 联大 122:1）、生效（2021-01-22）
  5. "Don't Bank on the Bomb" 全球撤资倡议（2012）
  6. 广岛长崎原子弹轰炸周年纪念活动（2015 七十周年全球联动）
- 关键时间线（15–18 节点）：
  - 1997 渥太华禁雷条约缔结，禁雷运动的成功成为 ICAN 创始范本（背景）
  - 2006-09-07 IPPNW 赫尔辛基大会通过提案，将 ICAN 列为头号运动优先事项
  - 2007-04-23 墨尔本公开启动
  - 2007-04-30 维也纳 NPT 筹备会国际启动
  - 2010-05-28 NPT 审议大会期间呼吁支持核武器公约
  - 2011-06-27 P5 巴黎会议期间发布视频敦促五核国家增加透明度
  - 2011-11-26 欢迎红十字与红新月运动通过支持禁核国际协定的历史性决议
  - 2012-03-05 启动 "Don't Bank on the Bomb" 撤资倡议
  - 2013-03 协调奥斯陆核武器人道主义影响会议公民社会参与
  - 2014-02-13/14 纳亚里特会议（146 国与会）
  - 2014-07-01 Beatrice Fihn 出任执行主任
  - 2014-12 维也纳会议闭幕，奥地利发出 Humanitarian Pledge
  - 2015-11 Humanitarian Pledge 签署国达 127 个
  - 2016-10-27 联大一委通过 ICAN 支持的决议，决定 2017 年启动谈判
  - 2017-07-07 TPNW 在联合国以 122:1 表决通过
  - 2017-10-06 获 2017 诺贝尔和平奖
  - 2020-10-24 第 50 国批准条约；2021-01-22 TPNW 生效
  - 2022-06-21/23 TPNW 首届缔约国会议于维也纳举行，ICAN 任公民社会焦点

### 第 1 步：建立目录 【模板通用】

- 确认 `peace/presentations/21th_century/International_Campaign_to_Abolish_Nuclear_Weapons/` 目录与 `images/` 子目录。

### 第 2 步：复制 Makefile 【模板通用】

- 复制同世纪已完工篇目的 Makefile，设 `MAIN=International_Campaign_to_Abolish_Nuclear_Weapons_zh`、`VIDEO_NAME` 同名。

### 第 3 步：收集图片 【人物专属】

- page.md 有 2007 墨尔本启动照、2016 Fihn 与 Michael Douglas 合影、2024 奥斯陆诺贝尔周火炬游行照；无机构徽标时用断链/鸽形母题装饰占位。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nuclear disarmament | 核裁军 | infobox Fields 明载的核心领域 | 使命页 |
| 1 | humanitarian disarmament | 人道主义裁军 | 以人道后果为中心的议程重构 | 使命页 |
| 2 | treaty advocacy | 条约倡导 | 推动 TPNW 谈判、通过与生效 | 里程碑页 |
| 3 | civil society coalition | 公民社会联盟 | 110 国 661 个伙伴组织的联合体 | 成员页 |
| 4 | anti-nuclear movement | 反核运动 | 全球反核公民行动的一部分 | 参见页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| other | International Physicians for the Prevention of Nuclear War | 无向 | 发起母组织，1985 和平奖得主，2006 通过 ICAN 提案 |
| influence | International Campaign to Ban Landmines | 无向 | 禁雷运动 1997 渥太华条约成功是 ICAN 的创始范本 |
| other | Treaty on the Prohibition of Nuclear Weapons | 无向 | ICAN 推动达成并落实的禁核条约（2017 通过，2021 生效） |
| colleague | Beatrice Fihn | 无向 | 2014 起任执行主任，诺奖时点领导人 |

- 入库操作：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/International_Campaign_to_Abolish_Nuclear_Weapons.yaml`

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：大地褐的沉重与和平鸽白；主色 `#4E342E`（manifest 预分配，勿改）+ 诺奖香槟金 `#C9A227` + 四分类色：
  - `badgeDisarm` 核裁军 — 大地褐 `#4E342E`
  - `badgeHuma` 人道 — 玫瑰 `#C4204F`
  - `badgeTreaty` 条约 — 靛蓝 `#283593`
  - `badgeCoal` 联盟 — 深绿 `#1B5E20`
- **背景母题**：被剪断的锁链 + 纸鹤细线（呼应广岛长崎纪念与折叠千纸鹤传统）。

### 第 6 步：规划幻灯片序列 【人物专属，机构概览页替代身份信息页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 2017 诺贝尔和平奖 / ICAN + 四色 badge + 断链母题
02  机构概览页（★ 必做）— 缩写 ICAN、成立（2006 提案/2007 启动）、总部日内瓦、成员规模、领导人、主要荣誉
03  使命：人道主义视角 — 毁灭能力、健康环境灾难、无差别打击、医疗瘫痪、长期辐射
04  从禁雷到禁核 (2006–2007) — 禁雷运动范本、IPPNW 赫尔辛基提案、墨尔本与维也纳双启动
05  组织架构 — 661 个伙伴组织/110 国、国际指导小组、日内瓦团队
06  人道主义会议三部曲 (2013–2014) — 奥斯陆、纳亚里特、维也纳
07  Humanitarian Pledge (2014–2015) — 奥地利承诺、127 国签署
08  TPNW 的诞生 (2016–2017) — OEWG、联大一委决议、2017-07-07 122:1 通过
09  2017 诺贝尔和平奖 — 官方理由全文、委员会评语（new direction and new vigour）
10  条约生效与缔约国会议 (2020–2022) — 第 50 国批准、2021-01-22 生效、维也纳首届缔约会议
11  支持者与声援 — 图图、Jody Williams 等和平奖得主与公众人物；潘基文赞语
12  争议与评价 — The Economist 质疑（核国家拒绝）客观并陈；获奖后成员规模跃升
13  遗产：一纸条约改写裁军叙事
14  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

- 版式硬要求：封面右上用墨尔本启动照（draw=coveraccent!50 细边框）+ ICAN 缩写小字注；机构概览页用「成立/总部/成员/领导人/荣誉」五行信息网格；里程碑页时间线节点多，用双列或压缩行距（\itemsep −2pt、arraystretch 0.58）；\foreach 分隔符必须 ASCII 逗号；每页写完即编译，vbox 溢出 ≤10pt、hbox ≤50pt。
- 时间线页保险：Milestones 节点超过 12 个时优先拆两页（2006–2014 / 2015–2022），勿硬压单页。

**ICAN 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 2017 独得 | ICAN 独享 2017 和平奖，无共享得主，勿造 co-honored |
| 库内复用 | 已有 stub id=6808，yaml name_en 沿用库内形式走 UPD 回填 QID，勿新建第二记录 |
| 成立两日 | 2006-09-07 是提案通过日、2007-04-23 是墨尔本公开启动日——yaml birth_date 取 2007-04-23，提示词两日分述勿混 |
| 机构条目 | is_org=true：yaml 省 gender/nationalities；国家口径按 manifest「International organization」，总部写日内瓦即可 |
| 勿把领导人写成创始人 | Beatrice Fihn/Melissa Parke 是执行主任非创始人；提案通过主体是 IPPNW |
| 政治红线 | 五核国家（P5）拒绝条约、The Economist 批评只作客观事实并陈，不作立场表述；广岛长崎纪念只写活动事实 |
| 支持者名单 | 图图、Jody Williams 等声援仅叙述不入库；Michael Douglas 是声援合影非成员 |
| 缩写读音 | ICAN 发音 /ˈaɪkæn/，infobox 明载，可作趣味注脚 |
| 条约全称 | Treaty on the Prohibition of Nuclear Weapons（TPNW），勿与《不扩散核武器条约》（NPT）混淆 |
| 引语红线 | 引语框仅收 page.md 载英文原文语句（委员会评语、ICAN 对 TPNW 的评价等） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| TPNW | 《禁止核武器条约》 | 2017 通过 2021 生效 |
| NPT | 《不扩散核武器条约》 | 与 TPNW 是两个条约 |
| IPPNW | 国际防止核战争医生组织 | 1985 和平奖得主，发起方 |
| Humanitarian Pledge | 人道主义承诺 | 奥地利 2014 年发出 |
| OEWG | 开放式工作组 | 联合国机制缩写 |
| Don't Bank on the Bomb | 「别赌在炸弹上」 | 撤资倡议 |
| MAPW | 澳大利亚防止核战争医生组织 | IPPNW 澳洲分部 |
| Ottawa Treaty | 《渥太华条约》（禁雷条约） | 1997，禁雷运动的成果 |
| P5 | 五核国家 | 美俄英法中 |
| Golden Doves for Peace | 金鸽和平奖 | 意大利 Archivio Disarmo 颁发 |
| First Meeting of State Parties | 首届缔约国会议 | 2022 维也纳 |
| International Steering Group | 国际指导小组 | 联盟治理机构 |
| Ban Ki-moon | 潘基文 | 联合国秘书长声援，仅叙述 |
| Beatrice Fihn | 比阿特丽丝·芬 | 执行主任（2014 起） |
| 122-1 vote | 122:1 表决 | TPNW 联大通过票数 |

### 第 9 步：史实审查 + 术语审查 【人物专属】

- 核对官方理由与名录逐字一致；核对 TPNW 关键日期（通过 2017-07-07、生效 2021-01-22）；确认无任何评价性政治语句。

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（manifest 预分配，勿改）
- **风格**：时间流逝 / 纪录片 / 沉稳
- **匹配理由**：从 2006 提案到 2021 条约生效，是十五年公民社会长跑；「时间之流」匹配其跨越多届联合国会议的持久议程叙事。
- **本地路径**：`music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/International_Campaign_to_Abolish_Nuclear_Weapons/page.md` | 本地 Wikipedia 事实基准 |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译照抄 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **执行顺序**：提示词 → yaml → seed_person.py 入库（UPD 回填 QID） → 验证（has_social_data=1、fields≥4、relations≥2）。
