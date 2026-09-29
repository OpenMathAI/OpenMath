# 医学家立传提示词（Tu Youyou 屠呦呦）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2015 年得主 Tu Youyou（屠呦呦）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Tu_Youyou/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：屠呦呦（1930-12-30 生于浙江宁波，**在世**），中国药学家，中国中医科学院首席科学家，共和国勋章获得者（2019）
- **气质关键词**：**青蒿一握的千年智慧、低温萃取的执着、以身试药的第一人**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2015 条目，屠呦呦独得一半；Campbell/Ōmura 共享另一半）：
  > "for her discoveries concerning a novel therapy against malaria"（因其关于疟疾新疗法的发现）
- **设计母题**：**一株青蒿与《肘后备急方》的一句话（qinghao → low-temperature extraction → artemisinin）**——"青蒿一握，以水二升渍，绞取汁"；用「古籍书页与青蒿叶片交叠、析出结晶」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Tu_Youyou/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Tu_Youyou/`（世纪目录一律 `21th_century`，肖像见 images.txt）。Makefile 复制后设 `MAIN=Tu_Youyou_zh`、`VIDEO_NAME=Tu_Youyou_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。**在世者注意**：封面写 b.1930。

## 三、研究领域梳理 + 入库 【人物专属】

**屠呦呦的研究领域（按 rank 排序，已入库 person_field，取 infobox Fields 四项）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | medicinal chemistry | 药物化学 | 青蒿素分离与结构确定 | 核心页 |
| 1 | Chinese herbology | 中草药学 | 2000 余方药筛选、640 处方笔记 | 核心页 |
| 2 | antimalarial medication | 抗疟药物 | 青蒿素/双氢青蒿素，2015 诺奖核心 | 核心页 |
| 3 | clinical research | 临床研究 | 以身试药与临床试验 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Lou Zhicen | 对方 → 导师 | 北京医学院药学系从其受业（infobox Academic advisors 明载） |
| co-honored | Satoshi Ōmura | 无向 | 2015 同届诺奖（屠呦呦独得疟疾疗法半边，Ōmura/Campbell 共享线虫半边） |
| co-honored | William C. Campbell (scientist) | 无向 | 2015 同届诺奖（屠呦呦独得疟疾疗法半边，Ōmura/Campbell 共享线虫半边） |

**在世者诚实值说明**：屠呦呦在世，page.md 叙事聚焦科研而非人际，relations=3 为诚实值，Review 勿"补足"。

**不入库但提示词可叙述**：523 项目研究组同事（未具名）；1977 年"屠呦呦等"集体署名发表；Ge Hong 葛洪（《肘后备急方》作者，文献启发非个人关系，不建 influence 边）；父亲（名字出处之给予者，非学术关系）。

## 五、配色方案 【人物专属】

- **气质**：古籍的墨色、青蒿的青碧、以身试药的沉勇
- **主色**：`#2F5D50`（青蒿青——蒿叶与中医科学院的沉静）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeHerb` 中草药筛选 — 青蒿青 `#2F5D50`
  - `badgeArt` 青蒿素 — 深青 `#0E7490`
  - `badgeClinic` 临床验证 — 琥珀 `#B07D2B`
  - `badgeHonor` 荣誉传承 — 暗红 `#8C2F1B`
- **背景母题**：古籍竖排书页与青蒿叶脉，低温蒸馏器剪影点缀。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 青蒿素的发现者 / Tu Youyou b.1930 + 四色 badge + 右上头像 + 国籍行（China）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生、宁波出身、北京医学院药学系、中医科学院任职、
    诺奖 2015、核心领域；"三无科学家"注脚）
03  核心贡献概览 — 2000 方药筛选 / 低温萃取 / 青蒿素 1972 / 双氢青蒿素 1973
04  名字的预言 (1930–1951) — 《诗经》"呦呦鹿鸣，食野之蒿"、宁波求学、肺结核休学与从医之志
05  北京医学院 (1951–1955) — 药学系、Lou Zhicen 门下、1955 毕业入中医科学院
06  早年研究：血吸虫与半边莲 — Lobelia chinensis 治血吸虫病
07  523 项目 (1967–1969) — 1967-05-23 启动的抗疟药物项目（背景一笔带过）、
    1969 年屠呦呦任课题组组长、海南疫区考察
08  两千方药的筛选（核心贡献页）— 640 处方笔记、2000 余方/380 提取物/200 草本、青蒿初试无效之谜
09  低温萃取的突破（核心页）— 《肘后备急方》"绞取汁"启示、葛洪 340 年、乙醚低温提取、小鼠猴子有效
10  1972：青蒿素问世 — 纯品获得并命名 qinghaosu、结构确定、1973 意外合成双氢青蒿素
11  以身试药 — "作为组长我责无旁贷"引语、无不良反应后开展临床试验、1977 匿名发表、1981 WHO 会议
12  2015 诺奖：独得一半 — 获奖理由逐字呈现、Campbell/Ōmura 共享另一半（结构讲清）、
    中国首位医学诺奖/首位女性诺奖得主
13  荣誉与认可 — Lasker 2011（中国首位）、Warren Alpert 2015、国家最高科技奖 2016、
    共和国勋章 2019、NAS 国际院士 2025、Time 1979 年度封面
14  遗产与结尾 — 挽救数百万生命、青蒿素类药物家族、三无科学家的启示 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名与在世口径 | **yaml/入库用 manifest 形式 "Tu Youyou"**；1930-12-30 生于宁波，**在世**——封面写 b.1930 |
| 2015 的"一半"结构 | **屠呦呦独得一半（疟疾）+ Campbell/Ōmura 共享另一半（线虫）**——她页面 Awards 段明载 "awarded one half of this prize"；勿写三人平分，勿写共同研究（两条工作线互不相关） |
| 与 Campbell/Ōmura 无合作 | 三人仅同届共享诺奖，研究平行独立——co-honored 边 note 写"同届/两半结构"，正文勿写协作 |
| 政治口径（★ 重要） | 523 项目的立项背景（越战请求、领导人决策）与文革背景**一律不展开**：只客观写"1967 年 5 月 23 日启动的抗疟药物保密项目（523 项目）"，人物（胡志明/周恩来/毛泽东）不出现；Tang Feifan"死于迫害"条目整段回避 |
| 名字出处引语 | 2011 年 Lasker 受访引语（呦呦鹿鸣/食野之蒿/青蒿之缘）page.md 明载英文译文，可引（注明 2011 年访谈）；"As head of this research group, I had the responsibility" 亦明载可引 |
| 数字防混淆 | 全球已筛 240,000 化合物无果 vs 屠呦呦组筛 2000 余方/380 提取物/200 草本；640 处方笔记——四组数字各归其位 |
| 教育沿革注释 | 北京医学院（1952 独立建制）→1985 北京医科大学→2005 并回北大为北京大学医学部——page.md 注释明载，身份页按 1951-1955 北京医学院口径写即可，勿写"北京大学毕业"的现代口径 |
| 青蒿素时间线 | 1971 低温提取有效 →1972 纯品命名 qinghaosu →1973 意外合成双氢青蒿素 →1977 匿名发表 →1980 研究员 →1981 WHO 会议 →2001 博士生导师——年份勿串 |
| "三无科学家" | 无后学位/无留学/非两院院士——page.md 明载的绰号可写（客观），亦是诺奖评审价值的注脚 |
| 双氢青蒿素来历 | 1973 年为验证羰基时**意外合成**——"意外"二字保留，勿写成定向设计 |
| metadata 噪声 | metadata nationalities 含 People's Republic of China + Republic of China（生于 1930 年 ROC 之历史噪声）——**以 page.md/Nobel 口径为准仅入 China** |
| 荣誉年份 | Lasker 2011（中国首位）、Alpert 2015-06、Nobel 2015-10、国家最高科技奖 2016、共和国勋章 2019-09、NAS 国际院士 2025、Time 1979 年度女性封面（2018 制作）——年份勿串 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| malaria | 疟疾 | 获奖理由核心词 |
| artemisinin (qinghaosu) | 青蒿素 | 1972 年命名 qinghaosu |
| dihydroartemisinin | 双氢青蒿素 | 1973 年意外合成 |
| Artemisia annua | 黄花蒿（青蒿） | 植物学名斜体 |
| low-temperature (ether) extraction | 低温（乙醚）萃取 | 突破关键，热水破坏活性成分 |
| Project 523 | 523 项目 | 1967-05-23 启动，仅客观提及 |
| Emergency Prescriptions Kept Up One's Sleeve | 《肘后备急方》 | 葛洪 340 年，"绞取汁"启示 |
| chloroquine resistance | 氯喹抗性 | 项目立项的医学背景 |
| "Three-Without Scientist" | 三无科学家 | 无后学位/无留学/非院士 |
| Medal of the Republic | 共和国勋章 | 2019 年，中国最高荣誉勋章 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：一株青蒿连接 1600 年前的葛洪与 21 世纪的诺奖——青蒿素挽救的是跨越世代的数百万生命；Eternals 的永恒感正对应这份"古籍—分子—生命"的时间纵深，也对应一位在实验室沉默耕耘半个世纪的科学家最终被世界看见的隽永。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Tu_Youyou/Eternals.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
