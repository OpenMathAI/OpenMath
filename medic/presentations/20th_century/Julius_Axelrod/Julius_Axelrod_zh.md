# 医学家立传提示词（Julius Axelrod）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1970 年得主 Julius Axelrod（朱利叶斯·阿克塞尔罗德）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Julius_Axelrod/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Julius Axelrod（1912-05-30 生于美国纽约 ~ 2004-12-29 逝于马里兰州贝塞斯达，享年 92 岁）
- **气质关键词**：**再摄取机制的发现者、对乙酰氨基酚的推手、松果腺生物钟的破译者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1970 条目，与 Katz、von Euler 三人共享同一理由）：
  > "for their discoveries concerning the humoral transmitters in the nerve terminals and the mechanism for their storage, release and inactivation"（因他们发现神经末梢中的体液递质及其贮存、释放与失活机制）
- **设计母题**：**回收的递质（reuptake）**——突触递质被突触前末梢重新摄取、循环再用的意象：以循环箭头+突触间隙的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Julius_Axelrod/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Julius_Axelrod/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Julius_Axelrod_zh`、`VIDEO_NAME=Julius_Axelrod_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | catecholamine metabolism | 儿茶酚胺代谢 | 释放/再摄取/贮存机制，1970 诺奖核心 |
| 1 | neurochemistry | 神经化学 | COMT 酶鉴定、MAO 抑制剂研究 |
| 2 | pharmacology | 药理学 | 镇痛药代谢起步、COMT/SSRIs 药理学地基 |
| 3 | chronobiology | 时间生物学 | 松果腺褪黑素与昼夜节律 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Bernard Brodie | 对方 → 导师 | Goldwater 医院药理研究导师（1946 起，镇痛药代谢合作；infobox Academic advisors 明载） |
| advisor-student | Solomon Snyder | Axelrod → 学生 | Research trainees 明载 |
| advisor-student | Irwin Kopin | Axelrod → 学生 | Research trainees 明载 |
| advisor-student | Richard J. Wurtman | Axelrod → 学生 | Research trainees 明载（松果腺方向） |
| spouse | Sally Taub | 无向 | 1938 结婚，妻 1992 去世；二子 Paul 与 Alfred |
| co-honored | Bernard Katz | 无向 | 1970 诺贝尔生理学或医学奖三人共享（神经末梢体液递质及贮存释放失活机制） |
| co-honored | Ulf von Euler | 无向 | 1970 诺贝尔生理学或医学奖三人共享（神经末梢体液递质及贮存释放失活机制） |

**不入库但提示词可叙述**：Research trainees 名单中未链接者（Ronald W. Holz、Rudi Schmid、Bruce R. Conklin、Ron M. Burch、Juan M. Saavedra、Marty Zatz、Richard M. Weinshilboum、Michael Brownstein、Chris Felder、Lewis Landsberg、Robert Kanterman——仅列名无实质叙述，不入库防噪声）；Nirenberg/Anfinsen（1973 联名请愿同僚，公共事件）；苏联科学家声援（公共事件）。

## 五、配色方案 【人物专属】

- **气质**：纽约移民的勤恳、实验室的意外之眼、神经化学的微光
- **主色**：`#5C3A21`（琥珀褐——贝塞斯达实验台的旧木与铜色）+ 香槟金诺奖色
- **badge 四分类色**：`badgeReuptake` 再摄取 琥珀褐 `#5C3A21`；`badgeCOMT` COMT 酶 青绿 `#0E7C7B`；`badgePineal` 松果腺 深蓝 `#1E4E79`；`badgeAnalgesic` 镇痛药起步 玫瑰 `#9E2B25`
- **背景母题**：循环箭头+突触间隙图案，呼应「回收的递质」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 再摄取机制的发现者 / Julius Axelrod 1912–2004 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1912-05-30 纽约 ~ 2004-12-29 贝塞斯达、
    CCNY BS 1933/NYU MS 1941/乔治华盛顿 PhD 1955、NIH 终身研究者、诺奖 1970）
03  核心贡献概览 — 对乙酰氨基酚 / 再摄取 / COMT / 松果腺与褪黑素
04  纽约移民之子 (1912–1935) — 波兰犹太移民家庭、CCNY 生物学士 1933、医学院全拒、
    市卫生局维生素检测员
05  夜校硕士与 Brodie 门下 (1935–1949) — NYU 夜校 MS 1941、1946 Goldwater 医院
    Brodie 实验室： acetanilide 致高铁血红蛋白血症、代谢物对乙酰氨基酚（Tylenol）登场
06  NIH 与博士逆袭 (1949–1955) — 国家心脏研究所、咖啡因/可待因/吗啡/甲基苯丙胺/麻黄碱、
    早期 LSD 实验；1954 请假读博、1955 一年速成 PhD
07  1957：再摄取（核心贡献页）— MAO 抑制剂研究中发现儿茶酚胺递质并非失活即弃、
    而被突触前末梢重新摄取循环——SSRIs（Prozac 类）的药理学地基
08  1958：COMT（核心贡献页）— 发现并表征儿茶酚-O-甲基转移酶，儿茶酚胺分解的另一翼
09  递质家族的拼图 — 肾上腺素/去甲肾上腺素的不活跃贮存形式、按需释放；
    多巴胺后来归入家族
10  松果腺与生物钟 — 褪黑素源自色氨酸（与血清素同源）、视交叉上核驱动的
    昼夜节律合成释放、松果腺作为生物钟
11  荣誉与认可 — Gairdner 1967、Nobel 1970、美国艺术与科学院 1971、
    英国皇家学会外籍院士 1979、Gerard 奖 1992、美国哲学会 1995
12  独眼与人格 — 实验室氨瓶爆炸伤左眼终身戴眼罩；无神论者而认同犹太文化、
    参与反犹主义抗争（客观叙述）
13  科学公共政策 — 1973 与 Nirenberg、Anfinsen 组织科学家请愿反对单一癌症机构、
    声援苏联被囚科学家（公共事件叙述）
14  遗产与结尾 — 从再摄取到百忧解：现代精神药理学的地基；NIH 工作至 2004 辞世
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 三人分工 | von Euler 发现去甲肾上腺素递质身份与囊泡贮存；Katz 量子式释放；Axelrod 再摄取与失活——citation 同一句，侧重分层勿互串 |
| 1970 获奖核心 | 官方理由 "humoral transmitters in the nerve terminals... storage, release and inactivation"——Axelrod 侧对应 release/reuptake/storage；勿写成"发现多巴胺"（dopamine 是 later discovered 归类） |
| 对乙酰氨基酚 | 1940s Brodie/Axelrod 查明 acetanilide 副作用、推荐其代谢物 acetaminophen（paracetamol, Tylenol）——是"推荐替代"而非"发明" |
| PhD 时间线 | 1954 请假赴乔治华盛顿大学、**1955 一年获 PhD**（部分既往研究折抵）——36 岁读博速成叙事勿写错年 |
| 学生边界 | 入库仅 wiki 链接三人 Snyder/Kopin/Wurtman（research trainees 首列）；名单其余 11 人仅列名不入库 |
| 国籍口径 | frontmatter 双值 [United States, Poland]（父系波兰移民背景），但 Axelrod 生于纽约、citations json=United States——yaml 仅 US，Poland 只作家世叙述 |
| 左眼 | 氨瓶爆炸伤左眼终身戴眼罩（page.md 明载）——可用作身份页细节，勿戏剧化 |
| 在世口径 | 已故（2004-12-29，享年 92，贝塞斯达）——封面写 1912–2004 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| reuptake | 再摄取 | 获奖机制核心词 |
| catecholamine | 儿茶酚胺 | 肾上腺素/去甲肾上腺素（+后归类的多巴胺） |
| catechol-O-methyl transferase (COMT) | 儿茶酚-O-甲基转移酶 | 1958 鉴定 |
| monoamine oxidase (MAO) inhibitor | 单胺氧化酶抑制剂 | 1957 研究切入点 |
| acetaminophen / paracetamol | 对乙酰氨基酚 | Tylenol 主体 |
| methemoglobinemia | 高铁血红蛋白血症 | acetanilide 副作用 |
| pineal gland | 松果腺 | 后期研究方向 |
| melatonin | 褪黑素 | 色氨酸来源 |
| suprachiasmatic nucleus | 视交叉上核 | 昼夜节律起搏器 |
| SSRI | 选择性血清素再摄取抑制剂 | Axelrod 工作的药理学延伸 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从被医学院全拒的检测员到 NIH 的终身研究者——Axelrod 的一生是对旧日岁月的漫长回答；"PAST" 的怀旧质感匹配其大器晚成与贝塞斯达半个世纪的坚守。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Julius_Axelrod/PAST.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
