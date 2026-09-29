# 医学家立传提示词（Corneille Heymans）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1938 年得主 Corneille Heymans（科内耶·海曼斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Corneille_Heymans/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Corneille Jean François Heymans（1892-03-28 生于比利时根特 ~ 1968-07-18 逝于比利时克诺克，享年 76 岁）
- **气质关键词**：**颈动脉窦的解码者、交叉灌流的实验大师、药理学世家的传人**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1938 条目）：
  > "for the discovery of the role played by the sinus and aortic mechanisms in the regulation of respiration"（因其发现窦与主动脉机制在呼吸调节中的作用）
- **设计母题**：**窦弓反射的双线（sinus & aortic reflex arcs）**——血压与血氧信息经迷走神经（而非血液本身）上传大脑；用「两条上行反射弧线条（窦线+主动脉线）汇入脑形轮廓」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Corneille_Heymans/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Corneille_Heymans/`。Makefile 复制后设 `MAIN=Corneille_Heymans_zh`、`VIDEO_NAME=Corneille_Heymans_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Heymans 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 呼吸与循环的反射调节，1938 诺奖核心 | 封面、核心页 |
| 1 | cardiovascular physiology | 心血管生理学 | 颈动脉窦压力感受器与血压调节 | 核心页 |
| 2 | respiratory physiology | 呼吸生理学 | 外周化学感受器与呼吸调节 | 核心页 |
| 3 | pharmacology | 药理学 | 根特药理学教授、J. F. Heymans 研究所所长 | 职业页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Jean-François Heymans | 对方 → 父 | 1930 继其父任根特大学药理学教授兼 J. F. Heymans 研究所所长 |
| colleague | Fernando de Castro | 无向 | 西班牙神经组织学家，详述主动脉-颈动脉区神经支配，其同事与友人；后人认为其贡献堪与共享诺奖 |
| advisor-student | Paul Janssen | Heymans → 学生 | infobox Notable students 明载 |
| advisor-student | Émile Gley | 对方 → 导师 | 毕业后法兰西公学院（Gley 门下）游学 |
| advisor-student | Maurice Arthus | 对方 → 导师 | 洛桑大学（Arthus 门下）游学 |
| advisor-student | Hans Horst Meyer | 对方 → 导师 | 维也纳大学（Meyer 门下）游学（库内既有 id=4449） |
| advisor-student | Ernest Starling | 对方 → 导师 | 伦敦大学学院（Starling 门下）游学 |
| advisor-student | Carl J. Wiggers | 对方 → 导师 | 凯斯西储医学院（Wiggers 门下）游学 |
| spouse | Berthe May | 无向 | 1929 结婚（1892–1974），眼科医生 |

**不入库但提示词可叙述**：Santiago Ramón y Cajal（de Castro 的老师，与 Heymans 无师承关系）；五名子女（page.md 仅具数量无名字）；机构类身份（期刊主编、宗座科学院/法兰西科学院/皇家艺术学会会员）。

## 五、配色方案 【人物专属】

- **气质**：严谨、生理学的精密测量、根特的学术传承
- **主色**：`#16324F`（根特深蓝——北海低地的实验台沉静）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeSinus` 窦弓反射 — 深蓝 `#16324F`
  - `badgeChemo` 化学感受器 — 青绿 `#0E7C7B`
  - `badgePharm` 药理学 — 深绿 `#1B4D3E`
  - `badgeFam` 家学传承 — 琥珀 `#C07A2A`
- **背景母题**：颈动脉窦与主动脉弓两条上行反射弧的抽象线条，汇入脑形轮廓。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 颈动脉窦的解码者 / Corneille Heymans 1892–1968 + 四色 badge + 右上头像 + 国籍行（Belgium）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、根特出身、根特大学博士 1920、
    根特药理学教授 1930、J. F. Heymans 研究所所长、诺奖 1938、核心领域）
03  核心贡献概览 — 压力感受器 / 化学感受器 / 交叉灌流 / 窦弓反射
04  根特与耶稣会学校 (1892–1920) — Sint-Barbaracollege；根特大学医学博士 1920
05  五站游学 (1920s) — 巴黎 Gley / 洛桑 Arthus / 维也纳 Meyer / 伦敦 Starling / 克利夫兰 Wiggers
06  继承父席 (1922–1930) — 1922 药效学讲师；1930 继父任药理学教授、研究所所长
07  交叉灌流双犬实验（核心贡献页）— 孤离头仅以神经连体；第二犬供血
08  经神经而非血液 — 心血管反射弧由自身迷走神经传递；供血犬血中药物无效应
09  外周化学感受器 — 呼吸调节的证据链，诺奖理由所在
10  颈动脉体定位 — de Castro 详述神经支配：压力感受器在窦、化学感受器在体
11  被遗忘的共享者 — de Castro 同事与友人；后人认为其贡献堪与共享诺奖（Cajal 最后的直系弟子）
12  荣誉与认可 — 1938 诺奖（1945-12-12 演讲）；月球 Heymans 环形山；1962 美国哲学会
13  家学与学生 — 父 Jean-François 同席前任；学生 Paul Janssen；妻 Berthe May（眼科医生）
14  遗产与结尾 — 窦弓反射的现代生理学地位 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生卒日期 | frontmatter 双值噪声（1892-00-00/1968-00-00），以正文 **1892-03-28 ~ 1968-07-18** 为准；卒于克诺克（中风），享年 76 |
| 1938 独得 | 单独得主，无 co-honored；诺奖演讲迟至 **1945-12-12**（二战推迟），勿写 1938 当年演讲 |
| 获奖理由表述 | 官方口径 "sinus and aortic mechanisms in the regulation of respiration"（窦与主动脉机制/呼吸调节），勿写成泛泛的"血压调节"或"化学感受器发现" |
| de Castro 不是共同得主 | page.md 明载 "it was later recognized that he **deserved** to share the Nobel Prize"——写「后人认为其贡献堪与共享」，禁写成共同得主或漏领奖 |
| Cajal 归属 | Cajal 是 de Castro 的老师（"maybe the last direct disciple"），与 Heymans **无师承关系**，禁写 |
| 父子同席 | 1930 年 Heymans 继任的是其**父亲** Jean-François Heymans 的根特药理学教席并执掌以其父命名的研究所——父子两代同一教席是亮点，勿写成普通前任 |
| 游学五站 | Gley（法兰西公学院）/ Arthus（洛桑）/ Meyer（维也纳）/ Starling（UCL）/ Wiggers（凯斯西储）均为正文明载的 postdoc 游学站——师承边全部入库；Starling 勿与 Hill 篇的 UCL 教席混淆 |
| 双犬实验叙述 | 第一犬头与自身躯体仅以神经相连、第二犬躯体交叉供血——反射弧经自身迷走神经传导、供血血中药物无效；"via the nerves and **not by the blood itself**" 是关键表述 |
| 妻子身份 | Berthe May 是眼科医生，1929 结婚，育五子女——子女无名可考不入库 |
| 宗教与勋章 | 天主教徒；获教廷圣墓骑士团/圣西尔维斯特骑士指挥官勋章等——可选叙述，与科学贡献分开 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| sinus and aortic mechanisms | 窦与主动脉机制 | 获奖理由核心词，逐字对应 |
| carotid sinus | 颈动脉窦 | 压力感受器所在 |
| carotid body | 颈动脉体 | 化学感受器所在，与窦区分 |
| baroreceptor | 压力感受器 | 血压反射起点 |
| chemoreceptor | 化学感受器 | 血氧/呼吸调节 |
| vagus nerve | 迷走神经 | 反射弧的传入通路 |
| cross-perfusion | 交叉灌流 | 双犬实验方法名 |
| vivisection | 活体解剖实验 | 历史方法学表述 |
| pharmacodynamics | 药效学 | 1922 根特讲师职位名 |
| pressor / depressor reflex | 加压/减压反射 | 心血管反射弧 traffic |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Invisible Light**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：血压与血氧的感知深藏于颈动脉窦与主动脉弓、信号经无形的神经上传——「不可见之光」对应这一看不见的感知系统；曲名的深邃感也贴合交叉灌流实验抽丝剥茧的推理之美。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Corneille_Heymans/TheInvisibleLight.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
