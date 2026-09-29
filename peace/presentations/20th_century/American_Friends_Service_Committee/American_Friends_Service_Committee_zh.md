# 组织机构立传提示词（OpenPeace 批次 10 实例：American Friends Service Committee）

> **本文件是 OpenPeace 的「和平奖得主（组织机构）立传提示词」**，以 American Friends Service Committee（美国公谊服务委员会，1947 诺贝尔和平奖）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本机构替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享体系，与 OpenPhysicist / OpenMedic 平级）。
- **本实例**：American Friends Service Committee（美国公谊服务委员会，AFSC）—— 本批次唯一的**组织机构**条目（is_org=true）。
- **设计哲学**：组织机构立传与个人立传的核心差异，在于以「**机构概览页**」替代「身份信息页」，叙事重心从「个人生平」转向「**使命—行动—遗产**」三段式；「研究领域」相应替换为「使命领域」结构化表达，务必保留骨架。

---

## 二、背景信息 【人物专属】

- **目标机构**：American Friends Service Committee（AFSC），1917-04-30 成立于美国费城（infobox 明载 Founded April 30, 1917；正文另作 "In April 1917"，取 infobox 精确日期）
- **气质关键词**：**贵格和平见证的化身、战火中的救济者、以爱代力的和平实践者**
- **诺奖**：1947 诺贝尔和平奖，与英国对应机构 Friends Service Council 共享，获奖理由（Nobel 官方英文原文照抄）：
  > "for their pioneering work in the international peace movement and compassionate effort to relieve human suffering, thereby promoting the fraternity between nations."（表彰它们在国际和平运动中的开创性工作与减轻人类苦难的仁爱努力，从而促进各国人民之间的友爱）
- **设计母题**：**烛光与犁铧（candlelight & ploughshare）**。贵格会「把刀剑打成犁头」的和平见证 + 战地救济的烛光意象——视觉语言采用提灯、麦穗、鸽影与货箱轮廓；柔和圆点背景呼应「服务即见证」的朴素信仰。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/American_Friends_Service_Committee/page.md`
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报。数据库同步要求：包含「使命领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库。

### 第 0 步：事实基准（第一轮已核对，勿改） 【人物专属】

- 性质：贵格会（Religious Society of Friends）背景的非营利和平组织（501(c)(3)），总部费城 Cherry St 1501 号，发源地宾州 Haverford；1999-11-06 列入宾州历史地标
- 成立：1917-04-30，由美国贵格会各分支的 **17 名成员**共同创立（为一战平民受害者提供救济；为良心拒服兵役者提供替代服务）
- 现任领导：Joyce Ajlouny（General Secretary）；规模约 350 名员工、数千志愿者，年预算约 4090 万美元（FY2022）
- 关键荣誉：1947 诺贝尔和平奖（与 Friends Service Council 共享，代表全球贵格会徒受奖）；Wateler Peace Prize（frontmatter 载）
- 使命领域：①战时平民救济与良心拒服兵役者替代服务②种族关系与民权③难民与移民④和平建设与非暴力⑤核裁军倡导
- 关键时间线（18 节点）：1917-04-30 费城创立 / 1917–1918 法国战场替代服务、为流离失所者募集衣食 / 1918–1920s 扩展至俄罗斯、塞尔维亚、波兰；在德奥设儿童食堂；受 Hoover 总统委任对德救济 / 1920s Interracial Section 改善种族关系、主张开放移民法、支持罢工矿工 / 1930s 协助纳粹德国难民（侧重无其他机构援助者）/ 1936–1939 西班牙内战双方儿童救济、维希法国难民支持 / 二战期间运营 Civilian Public Service 营 / 1942 起协助日裔美国人转学与重新安置 / 1937–1943 为失业矿工建 Penn-Craft 社区 / 1947 印巴分治难民安置 / 1947 获诺贝尔和平奖；此后不久成为最早获联合国咨商地位的 NGO 之一，促成 Quaker United Nations Office（QUNO）设立 / 1948-12-07 受 UN 秘书长 Trygve Lie 邀请执行加沙紧急救济计划（预算 3200 万美元）/ 1949-03-30 为 1.6 万名儿童建起简易学校 / 1950-04 全部加沙项目移交 UNRWA / 1955 出版 *Speak Truth to Power*（Stephen G. Cary、A. J. Muste、Robert Pickus、Bayard Rustin 等执笔）/ 1950s–1960s 朝鲜战争、1956 匈牙利事件、阿尔及利亚战争、尼日利亚-比夫拉战争中两侧平民救济 / 1966 越南南北双方平民医疗援助与假肢供应、征兵咨询 / 1970s 起深度参与反核军备运动 / 2004 启动 *Eyes Wide Open* 伊拉克-阿富汗战争代价展 / 2020–2030 战略规划（公正和平、公正经济、流离失所应对）

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/American_Friends_Service_Committee/` 下建 `images/`；Makefile 设 `MAIN=American_Friends_Service_Committee_zh`、`VIDEO_NAME=American_Friends_Service_Committee_zh`
- 肖像：page.md 仅载 AFSC 历史徽标（logo）图，无人物肖像；机构条目**用徽标或成立地照片替代人物头像**，404 则用装饰圆占位并在图注注明「机构徽标」

### 第 4 步：使命领域梳理 + 入库 【模板通用，机构专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | humanitarian aid | 人道主义援助 | 一战至今的战地救济主线 | 历史页 |
| 1 | peacebuilding | 和平建设 | 冷战冲突两侧调停式服务、当代三大战略之首 | 项目页 |
| 2 | nonviolence | 非暴力 | 贵格和平见证与替代服务传统 | 背景页 |
| 3 | social justice | 社会正义 | 种族关系、移民、劳工与经济正义 | 历史页 |
| 4 | refugee relief | 难民救济 | 纳粹难民、日裔美国人、加沙、印巴分治 | 历史页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【模板通用，机构专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Friends Service Council | 无向 | 1947 诺贝尔和平奖共同得主（英国对应机构，今 Quaker Peace and Social Witness） |
| other | Quaker United Nations Office | 无向 | 1947 年获联合国咨商地位后促成设立，AFSC 为其提供行政支持 |

- 方向约定：机构关系均无向（seed 幂等归一 from<to）
- 不入库（无类型可归或无载）：17 名贵格创始人（集体，无个人姓名）、Joyce Ajlouny（现任干事非创始人）、Herbert Hoover（委任救济为事件非持续关系）、*Speak Truth to Power* 四位执笔人（事件性作者群）、Friends World Committee for Consultation（QUNO 的监督方，非与 AFSC 直接关系）、UNRWA（项目移交对象为事件）

### 第 5 步：设计配色方案 【模板通用，机构专属色彩】

- **气质**：朴素、温润、信仰驱动的坚韧
- **配色**：主色深酒红 `#750014`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeAid` 救济 — 香槟金 `#C9A227`
  - `badgePeace` 和平建设 — 靛 `#4C5FD5`
  - `badgeJust` 社会正义 — 青绿 `#0E7C7B`
  - `badgeRef` 难民救济 — 琥珀 `#E07B30`
- **背景母题**：柔和圆点，疏朗温润，呼应贵格会「每个人内在皆有光」的朴素信仰与服务传统

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有机构徽标或代表图像（右上 + 细边框）；2. 封面明示「美国 · 费城」与 `成立 | 总部 | 主要奖项` 状态栏；3. **必须有机构概览页**（替代身份信息页：成立时间/创始人/性质/总部/使命/规模/荣誉网格）；4. 品牌口径统一 `OpenMathAI`，引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【机构专属，15 页规划】

```
00  OpenPeace 项目首页（\input cover 封面）
01  封面 — 以服务为见证 / American Friends Service Committee 1917– + 四色 badge + 国别行
02  机构概览页（★ 必做，替代身份信息页）— 成立/创始人/性质/总部/规模/使命/荣誉
03  贵格和平见证 — 拒服兵役传统与 AFSC 的诞生逻辑
04  起源：1917 费城 — 征兵阴影下的替代服务构想（核心页之一）
05  一战救济 — 法兰西战场、俄塞波 expansion、Hoover 委任对德救济
06  两次大战之间 — 种族关系、移民法、劳工与 Penn-Craft 社区
07  二战岁月 — 纳粹难民、西班牙内战儿童、CPS 营与日裔美国人援助
08  1947 诺贝尔和平奖 — 与 Friends Service Council 共享、代表全体贵格会徒受奖（核心页）
09  加沙紧急救济 (1948–1950) — Trygve Lie 邀请、32 亿美元计划、移交 UNRWA
10  冷战岁月 — Speak Truth to Power 与冲突两侧的平民救济
11  越南与民权 — 南北两侧医疗援助、征兵咨询、族裔权利倡导
12  反核与当代项目 — 1970s 反核军备、Eyes Wide Open、2020–2030 战略
13  批评与自省 — 客观记录 page.md 明载的争议（单侧叙事禁写）
14  遗产：以爱代力 — 联合国咨商地位、QUNO 与贵格服务传统 + 结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；每写完一页 `make`，`pdftoppm` 目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查 【机构专属】

**AFSC 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 创始人 | 是 **17 名贵格会成员**（集体创立），勿把任何个人（含现任干事 Joyce Ajlouny）写成创始人 |
| 1947 共享 | 与英国 Friends Service Council（今 Quaker Peace and Social Witness）**共享**，获奖理由用 "their"（复数）；勿写成 AFSC 独得 |
| 受奖口径 | 诺奖是「代表全世界贵格会徒」（on behalf of all Quakers worldwide）颁发的，勿写成仅表彰 AFSC 一家 |
| QUNO 归属 | QUNO 由 Friends World Committee for Consultation 监督，AFSC 只是为纽约办公室**提供行政支持**，勿写成 AFSC 下属机构 |
| 加沙计划 | 1948-12-07 由 UN 秘书长 Trygve Lie 官方邀请；1950-04 整体移交 UNRWA；预算 3200 万美元（其中美国承担 1600 万）——三个数字勿混 |
| Speak Truth to Power | 1955 年出版，71 页，作者为 Stephen G. Cary、A. J. Muste、Robert Pickus、Bayard Rustin 等一群人，勿署名给单人 |
| 政治红线 | Criticism 一节（教内批评、Lewy 书、中东立场争议等）只作 page.md 明载的客观事实记录，禁加任何评价性语句；阿以冲突相关内容（1948 加沙计划等）同样只作事实陈述 |
| 成立日期 | infobox 载 April 30, 1917；正文作 April 1917——取 infobox 精确日期，勿写 1916 |
| 日裔美国人 | page.md 用语为 forcibly relocated / inland concentration camps，转述时保持历史事实口径，不加渲染 |
| 机构与人物 | 幻灯片全部以机构为叙事主语，无「早年」「晚年」页；身份信息页换为机构概览页 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Religious Society of Friends | 贵格会（公谊会） | 勿译成「朋友会」 |
| conscientious objector (CO) | 良心拒服兵役者 | 替代服务传统的起点 |
| alternative service | 替代服务 | 勿与「义务劳动」混译 |
| Civilian Public Service | 民事公共服务营 | 二战期间 CPS 营 |
| Quaker Peace Testimony | 贵格和平见证 | 信仰原则非政治纲领 |
| consultative status | （联合国）咨商地位 | 1947 年后首批 NGO 之一 |
| Quaker United Nations Office (QUNO) | 贵格会驻联合国办公室 | 纽约+日内瓦两处 |
| UNRWA | 联合国近东巴勒斯坦难民救济和工程处 | 1950 接手加沙项目 |
| Speak Truth to Power | 以真相言说力量 | 1955 小册子，勿译成「向权力说出真相」标题化 |
| Friends Service Council | 公谊服务理事会 | 英国对应机构，1947 共同得主 |
| Interracial Section | 种族关系部 | 1920s 设立 |
| Penn-Craft | 佩恩克拉夫特社区 | 1937–1943 失业矿工社区 |

---

## 四、背景音乐选择 ✅ 【机构专属】

- **选定曲目**: **Winds Of Freedom** — Really Slow Motion & Giant Apes（manifest 预分配，勿改）
- **风格**: 史诗 / 英雄管弦 / 自由气息
- **匹配理由**: "自由之风"匹配跨越两次大战与冷战的人道主义服务史——从法兰西战场到加沙难民营，AFSC 的工作始终是乱世中吹向平民的一缕自由之风；"史诗/英雄管弦"匹配机构叙事的集体英雄主义（17 名创始人到数千志愿者），而非个人传奇。
- **本地路径**: `music_audio/inspiring-electronic/25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav` → 复制为 `presentations/20th_century/American_Friends_Service_Committee/Winds Of Freedom.wav`
- **时长**: 以实际文件为准 → ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/American_Friends_Service_Committee/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译口径 |
| `MySQL/data/American_Friends_Service_Committee.yaml` | 入库 yaml（第 4 / 4.5 步落地） |
| `MySQL/seed_person.py` | 幂等入库引擎 |
| `music_audio/curated_tracks.md` | BGM 曲库 |

- **备选** (未采用):
  - ★★ Expedition — 「远征感」匹配战地救济的机动性，但组织条目更需要集体史诗而非冒险叙事
  - ★ SEA — 「辽阔」匹配全球服务范围，但偏静，弱于机构叙事所需的推动力

---

## 六、数据库落地命令 【模板通用】

- **yaml**: `MySQL/data/American_Friends_Service_Committee.yaml`（第 4 步使命领域表与第 4.5 步关系表为其唯一事实来源）
- **入库**（幂等；撞 fields/occupations 字典表唯一键时等 2 秒重跑一次）：

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/American_Friends_Service_Committee.yaml
```

- **验证**（要求 `has_social_data=1`、fields≥4、relations≥2）：

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 -c "
from db_mysql import get_conn
conn=get_conn(); cur=conn.cursor()
cur.execute(\"SELECT id,name_en,has_social_data FROM people WHERE qid='Q464677'\")
p=cur.fetchone(); print(p)
cur.execute('SELECT COUNT(*) FROM person_field WHERE person_id=%s',(p[0],)); print('fields:',cur.fetchone()[0])
cur.execute('SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s',(p[0],p[0])); print('relations:',cur.fetchone()[0])"
```

- **本实例参考值**: 已入库 id=6856，fields=5，relations=2（组织机构条目按工作流第 2 节省略 gender/nationalities，co-honored 对手方为 Friends Service Council）。
- **注意事项**: 组织机构 yaml 无 gender/nationalities 字段；对手方 `Friends Service Council` 与 `Quaker United Nations Office` 的 name_en 用 manifest `name` 字段原文。

> **开始执行。每完成一步汇报。**
> **最重要的事：无载禁写；机构条目无「早年/晚年」页；每写一页就 make，看到溢出就修。**
