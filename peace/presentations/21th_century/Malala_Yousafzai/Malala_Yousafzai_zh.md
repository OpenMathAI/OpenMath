# OpenPeace 21 世纪和平奖得主立传提示词（实例：Malala Yousafzai）

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他学科侧共享体系）。
- **本实例**：Malala Yousafzai（马拉拉·优素福扎伊），2014 诺贝尔和平奖共同得主，史上最年轻诺贝尔奖得主。
- **设计哲学**：和平奖得主立传必须有「身份信息页」，且强调「事业领域」的结构化表达；本篇以「教育之光」为母题——书本胜过子弹，笔尖战胜暴力。

---

## 二、背景信息 【人物专属】

- **目标人物**：Malala Yousafzai（1997-07-12 生于巴基斯坦斯瓦特明戈拉，在世）
- **气质关键词**：**史上最年轻诺奖得主、女童教育旗手、从幸存者到全球运动领袖**
- **2014 官方获奖理由**（与 Kailash Satyarthi 共享，主语 their，照抄名录，禁止改写）：
  > "for their struggle against the suppression of children and young people and for the right of all children to education."
  > （表彰他们对抗对儿童与青年的压迫、争取所有儿童受教育权的斗争）
- **设计母题**：**笔与书（books, not bullets）**。她在黎巴嫩贝卡谷地难民学校落成时呼吁世界领导人投资 "books, not bullets"——以书页、钢笔、打开的书本几何母题贯穿全篇。
- **本地数据源**：`peace/presentations/pages/21th_century/Malala_Yousafzai/page.md`
- **结构标杆**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节结构）
- **yaml 母本**：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属】

- 生卒：1997-07-12 生于巴基斯坦开伯尔-普什图省（当时称西北边境省）斯瓦特地区明戈拉，在世。
- 家庭：父 Ziauddin Yousafzai（教育活动家、办学人，Khushal Public School 链创办者）；母 Toor Pekai Yousafzai；两个弟弟 Khushal 与 Atal。普什图族 Yusufzai 部落，逊尼派穆斯林。名字取自阿富汗民间女英雄 Malalai of Maiwand。
- 教育：父亲所办学校；2013–2017 伯明翰 Edgbaston High School（2015 GCSE 6A*+4A）；牛津大学 Lady Margaret Hall 攻读 PPE（哲学、政治学与经济学），2020-06 毕业；2023 成为牛津 Linacre College 最年轻荣誉院士。
- 机构：Malala Fund 联合创始人（与 Shiza Shahid）。
- 关键荣誉（择要）：2011 巴基斯坦首届 National Youth Peace Prize；2012 Sitara-e-Shujaat（巴基斯坦第二高平民勇气勋章）；2013 萨哈罗夫思想自由奖、Simone de Beauvoir 奖、Anna Politkovskaya 奖、国际儿童和平奖；2014 诺贝尔和平奖（17 岁，史上最年轻）、费城自由勋章；2016 微笑勋章；2017 最年轻联合国和平使者、荣誉加拿大公民（最年轻在加拿大下议院演讲者）；2018 哈佛肯尼迪学院 Gleitsman 奖；2015 小行星 316201 Malala 命名。
- 核心事业清单：
  1. BBC 乌尔都语博客 Gul Makai（2009，11 岁）记录塔利班占领下巴斯瓦特的日常
  2. 女童受教育权公开倡导（2008 白沙瓦记者俱乐部首次公开演讲起）
  3. 2012-10-09 遭塔利班枪击头部后康复并走向全球舞台
  4. 联合创建 Malala Fund，推动全球女童教育
  5. 联合国大会演讲与 "Malala Day"（2013-07-12，16 岁生日）
  6. 著作与影像：《I Am Malala》（2013，与 Christina Lamb 合著）、《Malala's Magic Pencil》（2017）、《We Are Displaced》（2019）、《Finding My Way》（2025）、纪录片《He Named Me Malala》（2015）
- 关键时间线（15–20 节点）：
  - 1997-07-12 生于明戈拉
  - 2008-09 白沙瓦记者俱乐部首次公开演讲谈教育权
  - 2009-01-03 BBC 乌尔都语博客 Gul Makai 首篇（2009-03-12 结束）
  - 2009 夏《纽约时报》Adam B. Ellick 拍摄纪录片《Class Dismissed》；第二次斯瓦特战役中家庭流离
  - 2011-10 Desmond Tutu 提名国际儿童和平奖
  - 2011-12 获巴基斯坦首届 National Youth Peace Prize
  - 2012-10-09 放学车上遭塔利班枪手袭击，头部中弹
  - 2012-10 转送英国伯明翰伊丽莎白女王医院救治
  - 2013-01-03 出院；2013-02 颅骨重建+人工耳蜗手术
  - 2013-07-12 联合国演讲，联合国定名 "Malala Day"
  - 2013-10 《I Am Malala》出版
  - 2013-11 获欧洲议会萨哈罗夫奖
  - 2014-10-10 宣布与印度 Kailash Satyarthi 共获 2014 诺贝尔和平奖（17 岁，史上最年轻）
  - 2015-07-12 18 岁生日在黎巴嫩贝卡谷地为叙利亚难民开办学校，呼吁 "books, not bullets"
  - 2017-07 受任最年轻联合国和平使者；获荣誉加拿大公民
  - 2017-08 入读牛津 Lady Margaret Hall（PPE）
  - 2020-06 牛津毕业
  - 2021-11-09 在伯明翰与 Asser Malik 结婚
  - 2023 复返牛津任 Linacre College 荣誉院士
  - 2025 出版第二部回忆录《Finding My Way》

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/21th_century/` 下确认 `Malala_Yousafzai/` 目录与 `images/` 子目录。

### 第 2 步：复制 Makefile 【模板通用】

- 复制同世纪已完工篇目的 Makefile，设 `MAIN=Malala_Yousafzai_zh`、`VIDEO_NAME=Malala_Yousafzai_zh`。

### 第 3 步：收集图片 【人物专属】

- 首选真实肖像（page.md 内 Wikimedia Commons 图，如 2014 Women of the World Festival 照 `Malala_Yousafzai.jpg`，下载 500px）；404 则用装饰圆占位。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | female education advocacy | 女童教育倡导 | 核心事业，2014 诺奖理由核心 | 核心页 |
| 1 | children's rights | 儿童权利 | 对抗对儿童与青年的压迫 | 理由页 |
| 2 | human rights advocacy | 人权倡导 | 教育权作为基本人权 | 倡导页 |
| 3 | education activism | 教育行动主义 | BBC 博客到全球运动 | 早年页 |
| 4 | memoir writing | 回忆录写作 | I Am Malala 等四部著作 | 著作页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Asser Malik | 无向 | 2021-11-09 伯明翰成婚，巴基斯坦板球委员会经理 |
| parent-child | Ziauddin Yousafzai | 无向 | 父亲，教育活动家兼办学人 |
| parent-child | Toor Pekai Yousafzai | 无向 | 母亲 |
| co-honored | Kailash Satyarthi | 无向 | 2014 诺贝尔和平奖共同得主 |
| founder | Malala Fund | 无向 | 与 Shiza Shahid 联合创办的女童教育非营利组织 |
| colleague | Shiza Shahid | 无向 | Malala Fund 联合创始人 |
| colleague | Christina Lamb | 无向 | 《I Am Malala》合著者，英国记者 |
| influence | Benazir Bhutto | 无向 | page.md 明载的 role model，两度当选后被刺杀的巴基斯坦总理 |
| influence | Abdul Ghaffar Khan | 无向 | 即 Bacha Khan，page.md 明载的 role model，非暴力 Khudai Khidmatgar 运动领袖 |

- 入库操作：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Malala_Yousafzai.yaml`

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：钢青色沉静 + 暖金希望；主色 `#37474F`（manifest 预分配，勿改）+ 诺奖香槟金 `#C9A227` + 四分类色：
  - `badgeEdu` 女童教育 — 暖金 `#C9A227`
  - `badgeRight` 儿童权利 — 钢青 `#37474F`
  - `badgeUN` 全球舞台 — 靛蓝 `#3F51B5`
  - `badgePen` 著作与影像 — 玫瑰 `#C4204F`
- **背景母题**：稀疏书页/钢笔笔尖几何元素 + 柔和圆点，呼应 "books, not bullets"。

### 第 6 步：规划幻灯片序列 【人物专属】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 史上最年轻诺奖得主 / Malala Yousafzai 1997– + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、出生地、族群、教育、机构、主要荣誉、核心领域）
03  事业概览 — BBC 博客 / 女童教育 / Malala Fund / 著作与影像
04  斯瓦特童年 (1997–2008) — 明戈拉、父亲学校、Malalai of Maiwand 得名
05  Gul Makai：11 岁的博客 (2009) — BBC 乌尔都语、笔名由来、学校关闭日记
06  枪击与重生 (2012) — 10 月 9 日袭击、伯明翰救治、颅骨重建、国际声援
07  Malala Day (2013) — 联合国演讲 16 岁生日、披 Benazir Bhutto 披肩、"力量诞生"演讲
08  Malala Fund 与著作 (2013– ) — 与 Shiza Shahid 共创、I Am Malala、四部著作
09  2014 诺贝尔和平奖 — 与 Kailash Satyarthi 共享、17 岁最年轻、官方理由全文
10  books, not bullets (2015) — 贝卡谷地难民学校、18 岁生日
11  从牛津到全球舞台 (2017–2023) — 联合国和平使者、荣誉加拿大公民、PPE 毕业、Linacre 荣誉院士
12  荣誉与认可 — 萨哈罗夫奖、Sitara-e-Shujaat、费城自由勋章、微笑勋章、Gleitsman 奖
13  遗产：一个女孩的世界回响 — 小行星命名、纪录片、教育运动
14  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

- 版式：Beamer + Metropolis 风格；引语框仅收 page.md 载英文原文的语句（如 2013 联合国演讲 "weakness, fear and hopelessness died. Strength, power and courage was born"）；每页写完即编译检查溢出。

**Malala 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 最年轻口径 | 17 岁获 2014 和平奖，是**史上最年轻诺贝尔奖得主**（所有奖项）与最年轻和平奖得主，两说一致可写 |
| 共享理由主语 | 2014 理由是 "their" 共享句，与 Satyarthi 同一句，勿改写为单数 "her" |
| 第二位巴基斯坦诺奖得主 | 排 1979 物理奖得主 Abdus Salam 之后，勿写成"首位" |
| 唯一普什图 | 是唯一获诺贝尔奖的普什图人，page.md 明载 |
| 名字来源 | 名字取自 Malalai of Maiwand（'grief-stricken' 之意），勿与 Malala Fund 混淆 |
| 笔名 | BBC 博客笔名 Gul Makai（普什图语"矢车菊"），取自普什图民间故事角色 |
| 政治红线 | 塔利班袭击、Rohingya、克什米尔、加沙等话题只按 page.md 客观记录，不加评价；**Obama 仅叙述为其 role model，禁建关系**；巴基斯坦国内争议（I Am Not Malala、阴谋论）只作事实并陈 |
| 引语红线 | 引语框仅收 page.md 明载英文原话；乌尔都语/普什图语原文勿直译当引语 |
| 婚姻 | 2021-11-09 婚前她曾公开表示对婚姻制度的疑虑，2021 后改口支持个人选择，两说按时间呈现勿混 |
| 学位年份 | 牛津 PPE 2020-06 毕业（2017 入学），勿写 2019 |
| 弟弟 | 两个弟弟 Khushal 与 Atal，仅具名不入库 |
| 刑事审判 | 2015 密审八人无罪释放与 2025 两名已决犯获释的反复，只按 page.md 事实并陈 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Gul Makai | 古尔·玛凯（矢车菊） | 笔名，勿当本名 |
| Malala Fund | 马拉拉基金 | 非营利组织，与奖名区分 |
| PPE | 哲学、政治学与经济学 | 牛津学位 |
| Sakharov Prize | 萨哈罗夫思想自由奖 | 欧洲议会颁发 |
| Swat Valley | 斯瓦特谷地 | 事发地 |
| Khyber Pakhtunkhwa | 开伯尔-普什图省 | 时称西北边境省 |
| Pashtun | 普什图人 | 族群 |
| Kainat Riaz / Shazia Ramzan | 同车受伤同学 | 仅叙述不入库 |
| Sitara-e-Shujaat | 勇气之星勋章 | 巴基斯坦第二高平民勇气勋章 |
| He Named Me Malala | 《他以马拉拉为名》 | 2015 纪录片 |

### 第 9 步：史实审查 + 术语审查 【人物专属】

- 校验生卒、获奖年份、共享得主姓名拼写（Satyarthi）；核对官方理由与名录逐字一致；确认无任何评价性政治语句。

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（manifest 预分配，勿改）
- **风格**：觉醒 / 上扬 / 叙事
- **匹配理由**：11 岁执笔 → 枪击幸存 → 联合国演讲 → 17 岁诺奖，是一条"觉醒"弧线；Awaken 的上行叙事气质匹配"从幸存者到全球运动领袖"的传记节奏。
- **本地路径**：`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Malala_Yousafzai/page.md` | 本地 Wikipedia 事实基准 |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译照抄 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **执行顺序**：提示词 → yaml → seed_person.py 入库 → 验证（has_social_data=1、fields≥4、relations≥2）。
