# 医学家立传提示词（António Egas Moniz）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1949 年得主 António Egas Moniz（安东尼奥·埃加斯·莫尼斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/António_Egas_Moniz/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：António Caetano de Abreu Freire Egas Moniz（1874-11-29 生于葡萄牙阿万卡 ~ 1955-12-13 逝于里斯本，享年 81 岁），通称 **Egas Moniz**；本名 António Caetano de Abreu Freire de Resende
- **气质关键词**：**脑血管造影之父、精神外科的开创者、兼任外交官的神经学家、葡萄牙首位诺奖得主**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1949 条目，Moniz 半边口径，括号亦为官方原文）：
  > "for his discovery of the therapeutic value of leucotomy ( lobotomy ) in certain psychoses"（因其发现脑白质切断术（lobotomy）对某些精神病的治疗价值）
- **设计母题**：**显影的脑与切断的环路（the imaged brain & the severed loop）**——脑血管造影让大脑首次在 X 光下显影，leucotomy 切断额叶白质环路；用「造影剂在脑血管树中渐次显影 + 一条被切断的环路细线」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/António_Egas_Moniz/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/António_Egas_Moniz/`（1932 年 José Malhoa 所绘博士礼服肖像，见 images.txt）。Makefile 复制后设 `MAIN=António_Egas_Moniz_zh`、`VIDEO_NAME=António_Egas_Moniz_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Moniz 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neurology | 神经病学 | 里斯本神经学教授 1911–1944 | 封面、职业页 |
| 1 | cerebral angiography | 脑血管造影 | 1927 首例成功，放射显影大脑第一人 | 核心页 |
| 2 | psychosurgery | 精神外科 | leucotomy（今称 lobotomy），1949 诺奖理由 | 核心页 |
| 3 | neuroradiology | 神经放射学 | Thorotrast 造影剂改良、颈动脉闭塞检测 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Walter Rudolf Hess | 无向 | 1949 诺贝尔生理学或医学奖共享（Moniz：leucotomy 治疗价值 / Hess：间脑作为内脏活动协调者的功能组织，理由句各一） |
| colleague | Pedro Almeida Lima | 无向 | 长期下属、神经外科医生：受 Moniz 指示执行最初 20 例手术并共同发明 leucotome 白质刀 |
| spouse | Elvira de Macedo Dias | 无向 | 1901 结婚，1945 去世 |

**不入库但提示词可叙述**：John Farquhar Fulton 与 C.F. Jacobsen（耶鲁黑猩猩额叶切除实验，Moniz leucotomy 理论参照——方法学渊源非个人关系）；Walter Jackson Freeman II 与 James W. Watts（美国改良术式并改名 lobotomy）；批评者 Elliot Valenstein、Oliver Sacks（身后学术批评）；舅父兼教父 Caetano de Pina Resende Abreu e Sá Freire（改姓缘由）；政界同僚 Sidónio Pais 等；1939 枪击他的患者（无名）。

## 五、配色方案 【人物专属】

- **气质**：葡萄牙的深沈、造影显影的冷光、争议人物的复杂
- **主色**：`#2E1A47`（神经深紫——造影剂冷光与里斯本黄昏）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeAngio` 脑血管造影 — 深紫 `#2E1A47`
  - `badgeLeuco` 精神外科 — 暗红 `#7A1E28`
  - `badgeDiplo` 外交与政坛 — 军灰 `#37474F`
  - `badgeCrit` 争议与遗产 — 深金 `#B8860B`
- **背景母题**：脑内血管树渐次显影的线条，其中一条环路以虚线中断。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 葡萄牙首位诺奖得主 / Egas Moniz 1874–1955 + 四色 badge + 右上头像 + 国籍行（Portugal）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、本名与改姓典故、科英布拉医学 1899、
    里斯本神经学教授 1911–1944、外交部长 1918–1919、诺奖 1949、核心领域）
03  核心贡献概览 — 脑血管造影 / leucotomy / 外交生涯 / 争议遗产
04  阿万卡与改姓 (1874–1899) — 本名 de Resende；舅父兼教父援引中世纪贵族 Egas Moniz o Aio 改姓
05  科英布拉与里斯本讲席 (1899–1911) — 基础医学讲师 12 年；1911 里斯本神经学教授
06  政坛岁月 (1900–1919) — 议员、一战驻西班牙大使、外交部长、巴黎和会代表团长；1919 决斗后退出
07  51 岁重返实验室 (1926–1927) — 显影脑血管的假说；锶/锂溴化物初试失败（一例死亡）
08  脑血管造影成功（核心贡献页）— 25% 碘化钠、三例成功；1927 巴黎神经学会与法国医学科学院报告
09  Thorotrast 与临床推广 — 颈动脉闭塞检测；112 篇造影论文 2 部专著
10  leucotomy 的思想来源 — 「突触固定」假说；Fulton/Jacobsen 黑猩猩实验参照；额叶战伤观察
11  Lima 执刀的第一批手术 (1935) — 20 例；七例治愈七例改善六例无效；leucotome 白质刀共同发明
12  1949 诺奖与另一半 — 与 Walter Rudolf Hess 各半（间脑功能组织）；获奖理由官方句（含 lobotomy 括号）
13  争议与批评 — 并发症低估、随访不足之责；Freeman/Watts 美国改名 lobotomy；身后撤销诺奖呼声与辩护并存
14  遗产与结尾 — 1939 枪击余生、抗精神病药物问世后 leucotomy 退场、葡萄牙的纪念 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1949 共享的结构 | 与 **Walter Rudolf Hess** 共享但**理由句各一**：Moniz 半边是 leucotomy 治疗价值，Hess 半边是 "for his discovery of the functional organization of the interbrain as a coordinator of the activities of the internal organs"（间脑功能组织）——两句不可互换；Hess 是生理学家，勿写成精神外科同道 |
| 获奖理由逐字 | Moniz 官方句含括号：`"for his discovery of the therapeutic value of leucotomy ( lobotomy ) in certain psychoses"`——引用时括号与空格保留原样 |
| 命名沿革 | Moniz 命名 **leucotomy**；美国医生 Freeman 与 Watts 采用改良术式后改名 **lobotomy**——两个名字的关系要点明，勿混为一人命名 |
| Moniz 本人从未执刀 | 因缺乏神经外科训练+痛风致手部活动受限，手术全部由 **Pedro Almeida Lima** 执行；「Instructed by Moniz, Lima performed ten of the first twenty surgeries」——叙事勿写成 Moniz 亲自主刀 |
| 政治身份 | 议员（1900 起）、驻西班牙大使（1918）、外交部长（1918-10~1919-03）、巴黎和会代表团长；1919 年因政治口角**决斗**后退政——史实克制陈述 |
| 改姓典故 | 本名 de Resende；舅父兼教父坚信家族为中世纪贵族 Egas Moniz o Aio 后裔而说服改姓——个人史亮点 |
| 初试失败 | 最初锶/锂溴化物试验三例失败且**一例死亡**，后经兔/犬/尸体头试验改用 25% 碘化钠成功——失败史如实呈现 |
| 1939 遭枪击 | 被一名精神分裂症患者多次开枪击中——此后继续行医至 1955；勿与 leucotomy 并发症叙事混淆 |
| 争议呈现 | 批评（低估并发症、记录不足、随访缺失；Valenstein/Sacks 的批评；撤销诺奖呼声）与辩护（历史语境中的科学贡献）**两面平衡**，禁单边定性 |
| 姓名与生卒 | 全名 António Caetano de Abreu Freire Egas Moniz；1874-11-29 ~ 1955-12-13（内出血逝于里斯本）；yaml/manifest 用 **António Egas Moniz** |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cerebral angiography | 脑血管造影 | 1927 首创，Moniz 第一身份 |
| leucotomy | 脑白质切断术 | Moniz 命名，诺奖理由用词 |
| lobotomy | 脑叶白质切断术 | 美国改名，官方句括号内亦载 |
| psychosurgery | 精神外科 | 领域名 |
| leucotome | 白质刀 | 可伸缩金属线圈器械，与 Lima 共同发明 |
| radiopaque dye | 显影剂 | 锶/锂溴化物→25% 碘化钠→Thorotrast |
| fixation of synapses | 突触固定 | Moniz 精神病病因假说 |
| prefrontal | 前额叶 | 手术靶区 |
| interbrain | 间脑 | Hess 半边理由核心词，勿混入 Moniz 叙述 |
| carotid occlusion | 颈动脉闭塞 | 造影的临床应用 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Egas Moniz 的一生横跨大西洋两岸的外交与实验室——伊比利亚半岛的海洋气质贴合其葡萄牙底色；SEA 的开阔与暗涌也对应其争议遗产：如海面之下深流，褒贬交织而气象不息。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/António_Egas_Moniz/SEA.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
