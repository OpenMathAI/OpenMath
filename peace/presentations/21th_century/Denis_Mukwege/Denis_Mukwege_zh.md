# OpenPeace 21 世纪和平奖得主立传提示词（实例：Denis Mukwege）

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他学科侧共享体系）。
- **本实例**：Denis Mukwege（德尼·穆奎格），2018 诺贝尔和平奖共同得主，刚果（金）妇科医生、泛泽医院创办人。
- **设计哲学**：医者和平奖得主立传以「修复者」为母题——手术刀与话筒并举：白天修复身体，夜晚为正义发声。

---

## 二、背景信息 【人物专属】

- **目标人物**：Denis Mukwege（1955-03-01 生于比属刚果布卡武，在世）
- **气质关键词**：**战地修复者、性暴力之敌、从手术室走向世界讲坛**
- **2018 官方获奖理由**（与 Nadia Murad 共享，主语 their，照抄名录，禁止改写）：
  > "for their efforts to end the use of sexual violence as a weapon of war and armed conflict."
  > （表彰他们为终结在战争与武装冲突中将性暴力用作武器所做的努力）
- **设计母题**：**修复（repair）**。以缝合线、手掌、橄榄绿十字为视觉母题——他被称为「修复妇女的人」（L'homme qui répare les femmes）。
- **本地数据源**：`peace/presentations/pages/21th_century/Denis_Mukwege/page.md`
- **结构标杆**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节结构）
- **yaml 母本**：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属】

- 生卒：1955-03-01 生于比属刚果（今刚果民主共和国）布卡武，在世。九个孩子中的第三个，父为五旬节派牧师；出生时因感染险些夭折，被瑞典五旬节派传教士兼助产士 Majken Bergman 救回。
- 家庭：妻 Madeleine Mapendo Kaboyi，育有五个子女；侄 Mushaga Bakenga（运动员）。
- 教育：布隆迪大学医学博士（1983）；法国昂热大学妇产科硕士并完成住院医训练（1989）；布鲁塞尔自由大学博士（2015-09-24，论文研究刚果（金）东部创伤性瘘管）。学业主要由瑞典五旬节差会资助。
- 机构：莱梅拉医院儿科医生起步；1999 在布卡武创办 Panzi Hospital（泛泽医院，瑞典基督教援助组织与瑞典国际开发合作署出资建设，CEPAC 刚果五旬节运动运营）；2008 创立 Panzi Foundation DRC；后设 Panzi Foundation USA；2016 创立 Mukwege Foundation；与 Eve Ensler、Christine Schuler Deshryver 共创 City of Joy（2011 开门，2016 Netflix 纪录片）；全球冲突相关性暴力幸存者基金（Global Fund for Survivors of Conflict-Related Sexual Violence）共同创办人兼主席。
- 任职：Panzi Hospital 院长/共同创办人/首席医疗官；WHO 科学委员会成员（2021 起）；Clooney Foundation for Justice 董事会；Women Political Leaders 全球顾问委员会；2021 应英国 G7 轮值主席国任命加入性别平等咨询委员会（GEAC）。
- 关键荣誉（择要）：2008 联合国人权奖、奥洛夫·帕尔梅奖；2009 法国荣誉军团骑士、2013 军官级；2010 华伦伯格奖章（密歇根大学）；2011 比利时国王博杜安国际发展奖、克林顿全球公民奖；2013 瑞典正确生活方式奖、公民勇气奖；2014 萨哈罗夫思想自由奖；2015 古尔班基安奖；2016 首尔和平奖、四大自由奖；2018 诺贝尔和平奖（与 Nadia Murad 共享）；2024 Aurora 奖。
- 核心事业清单：
  1. 二次刚果战争以来治疗数千名遭性暴力伤害的妇女（Panzi 累计收治 8.2 万余例复杂妇科损伤，约六成源于性暴力）
  2. 泛泽医院的整体照护模式（医疗+法律+心理社会+社会经济）
  3. 在联合国讲坛谴责大规模强奸、呼吁将加害者送上国际法庭（2012-09）
  4. City of Joy 幸存者赋能项目
  5. 推动国际社会正视刚果冲突与性暴力问题（著作《The Power of Women》2021 等）
  6. 2023 竞选刚果（金）总统（第六位，39,639 票）
- 关键时间线（15–18 节点）：
  - 1955-03-01 生于布卡武（比属刚果）
  - 13 岁决定追随父亲成为五旬节派牧师（自述"说方言"的转折体验）
  - 1983 布隆迪大学医学毕业，任莱梅拉医院儿科医生
  - 目睹产科瘘管等产后并发症后转攻妇产科
  - 1989 昂热大学硕士并完成住院医训练，回莱梅拉医院
  - 1996 莱梅拉屠杀（第一次刚果战争开端），医院遇袭同事罹难，逃往布卡武
  - 1999 创办 Panzi Hospital
  - 2008 联合国人权奖、奥洛夫·帕尔梅奖；创立 Panzi Foundation DRC
  - 2011 City of Joy 开门
  - 2012-09 联合国演讲谴责大规模强奸
  - 2012-10-25 刺杀未遂（卫兵兼挚友中弹身亡），流亡欧洲
  - 2013-01-14 返回布卡武（病人卖菠萝洋葱为他集资回程机票，20 英里夹道欢迎）
  - 2014-11 获欧洲议会萨哈罗夫奖
  - 2015-09-24 获布鲁塞尔自由大学博士
  - 2016 创立 Mukwege Foundation
  - 2018-10 与 Nadia Murad 共获诺贝尔和平奖
  - 2021 加入 WHO 科学委员会；入选英国 G7 GEAC
  - 2023-10-02 宣布竞选总统，最终第六位
  - 2025-02 在《纽约时报》撰文呼吁关注 M23 攻势下的人道危机

### 第 1 步：建立目录 【模板通用】

- 确认 `peace/presentations/21th_century/Denis_Mukwege/` 目录与 `images/` 子目录。

### 第 2 步：复制 Makefile 【模板通用】

- 复制同世纪已完工篇目的 Makefile，设 `MAIN=Denis_Mukwege_zh`、`VIDEO_NAME` 同名。

### 第 3 步：收集图片 【人物专属】

- page.md 有 Mukwege 2018 年官方肖像、2013 泛泽办公室照、2014 斯特拉斯堡萨哈罗夫奖领奖照，下载 500px 真实肖像。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | gynecological surgery | 妇科修复外科 | 修复性暴力伤害的重建手术 | 医疗页 |
| 1 | wartime sexual violence | 战时性暴力 | 2018 诺奖理由核心议题 | 诺奖页 |
| 2 | women's health | 妇女健康 | 产科瘘管到整体照护 | 医疗页 |
| 3 | human rights advocacy | 人权倡导 | 联合国演讲与正义呼吁 | 倡导页 |
| 4 | humanitarian aid | 人道主义援助 | 泛泽体系与 City of Joy | 机构页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Madeleine Mapendo Kaboyi | 无向 | 妻子，育五子女 |
| co-honored | Nadia Murad | 无向 | 2018 诺贝尔和平奖共同得主 |
| founder | Panzi Hospital | 无向 | 1999 创办，任院长/首席医疗官 |
| founder | Panzi Foundation DRC | 无向 | 2008 创立的支持基金会 |
| founder | Mukwege Foundation | 无向 | 2016 创立，倡导终结战时性暴力 |
| founder | Global Fund for Survivors of Conflict-Related Sexual Violence | 无向 | 共同创办人兼主席 |
| colleague | Eve Ensler | 无向 | City of Joy 共同创办人 |

- 入库操作：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Denis_Mukwege.yaml`

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：深海蓝的坚忍 + 治愈绿；主色 `#0F4C5C`（manifest 预分配，勿改）+ 诺奖香槟金 `#C9A227` + 四分类色：
  - `badgeMed` 医疗 — 治愈绿 `#1B5E20`
  - `badgeJustice` 正义 — 深海蓝 `#0F4C5C`
  - `badgeAdvocacy` 倡导 — 玫瑰 `#C4204F`
  - `badgeFaith` 信念 — 琥珀 `#E07B30`
- **背景母题**：缝合线细纹 + 掌心轮廓，呼应「修复妇女的人」。

### 第 6 步：规划幻灯片序列 【人物专属】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 2018 诺贝尔和平奖 / Denis Mukwege 1955– + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、家庭、教育、机构、主要荣誉、核心领域）
03  事业概览 — 儿科 / 妇科 / 泛泽医院 / 倡导 / 从政
04  布卡武少年 (1955–1983) — 牧师之家、Majken Bergman 救回一命、从神学转向医学
05  从儿科到妇科 (1983–1989) — 莱梅拉医院、产科瘘管、昂热大学
06  泛泽医院 (1999– ) — 莱梅拉屠杀后创办、瑞典援助、8.2 万患者、17 小时工作日
07  联合国讲坛 (2012) — 谴责大规模强奸、呼吁国际法庭
08  刺杀与归来 (2012–2013) — 卫兵殉难、流亡欧洲、菠萝与洋葱的归途
09  泛泽体系与 City of Joy (2008–2016) — 三个基金会、整体照护、幸存者赋能
10  2018 诺贝尔和平奖 — 与 Nadia Murad 共享、官方理由全文、"their" 共享句
11  荣誉与认可 — 萨哈罗夫奖、正确生活方式奖、奥洛夫·帕尔梅奖、华伦伯格奖章
12  更广的战场 (2021– ) — WHO 科学委员会、G7 GEAC、2023 总统竞选、M23 人道呼吁
13  遗产：修复与正义
14  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

- 版式硬要求：封面右上肖像（draw=coveraccent!50 细边框 + 姓名小字注）+ 底部状态栏「国籍 | 机构 | 主要奖项」三要素；身份信息页左肖像右信息网格；荣誉页条目多（frontmatter 25 项），只取 8–10 条择要分两栏；缝合线母题作页面底纹细线，勿喧宾夺主；每页写完即编译，vbox 溢出 ≤10pt、hbox ≤50pt。

**Mukwege 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 共享理由主语 | 2018 理由是 "their" 共享句，与 Nadia Murad 同一句，勿改写为单数 |
| 主题克制 | 性暴力议题的呈现须克制、以治疗与正义为中心；统计数据（8.2 万患者/60%）用 page.md 数字，勿自行放大；受害者个体细节勿渲染 |
| 政治红线 | 刚果冲突、卢旺达/乌干达威胁来源、M23 危机、2023 总统选举只按 page.md 客观记录，不作立场评价 |
| 医学荣誉区分 | 获奖理由是和平奖（终止性暴力），非医学奖；2013 Right Livelihood 获奖理由是"治愈战争性暴力幸存者并直言其根源"，两处引语勿混 |
| 刺杀细节 | 2012-10-25 卫兵（挚友）身亡、本人伏地幸免；流亡与 2013-01-14 归来的「菠萝与洋葱」细节是 page.md 明载亮点 |
| 生日获救 | 出生时被瑞典助产士 Majken Bergman 救回——与他后来受瑞典资助的叙事线呼应，可写 |
| 兄弟姐妹 | 九个孩子中的第三个，手足不具名不入库；侄 Mushaga Bakenga 仅具名不入库 |
| City of Joy | 与 Eve Ensler、Christine Schuler Deshryver 三人共创，勿写成 Mukwege 独创 |
| 从政事实 | 2023 竞选第六位（39,639 票）客观记录，勿写评价 |
| 引语红线 | 引语框仅收 page.md 载英文原句（UN 演讲转述句、Nyhemsveckan 演讲英译、The Globe and Mail 评价等） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Panzi Hospital | 泛泽医院 | 布卡武，1999 创办 |
| obstetric fistula | 产科瘘管 | 转攻妇科的契机 |
| reconstructive surgery | 修复重建外科 | 核心医术 |
| City of Joy | 喜悦之城 | 幸存者赋能项目 |
| CEPAC | 刚果五旬节教会运动 | 泛泽医院运营方 |
| PMU | 瑞典五旬节差会发展合作组织 | 长期资助方 |
| Right Livelihood Award | 正确生活方式奖 | 2013，勿与诺奖混 |
| Sakharov Prize | 萨哈罗夫思想自由奖 | 2014 |
| Global Fund for Survivors | 全球冲突相关性暴力幸存者基金 | 共同创办 |
| L'homme qui répare les femmes | 「修复妇女的人」 | 书名/纪录片名 |
| Madeleine Mapendo Kaboyi | 玛德莱娜·马彭多·卡博伊 | 妻子 |
| Lemera massacre | 莱梅拉屠杀 | 第一次刚果战争开端 |
| The Power of Women | 《女性的力量》 | 2021 回忆录 |
| traumatic fistula | 创伤性瘘管 | 博士论文主题 |

### 第 9 步：史实审查 + 术语审查 【人物专属】

- 核对官方理由与名录逐字一致；核对共享得主 Nadia Murad 拼写；确认无任何评价性政治语句。

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（manifest 预分配，勿改）
- **风格**：黎明 / 希望 / 温暖叙事
- **匹配理由**：从莱梅拉屠杀的至暗时刻到「菠萝与洋葱」的归途，再到诺贝尔讲坛——「黎明」匹配幸存与修复的传记基调。
- **本地路径**：`music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Denis_Mukwege/page.md` | 本地 Wikipedia 事实基准 |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译照抄 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **执行顺序**：提示词 → yaml → seed_person.py 入库 → 验证（has_social_data=1、fields≥4、relations≥2）。
