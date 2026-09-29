# 医学家立传提示词（Salvador Luria）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1969 年得主 Salvador Luria（萨尔瓦多·卢里亚）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Salvador_Luria/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Salvador Edward Luria（本名 Salvatore Luria，1912-08-13 生于意大利都灵 ~ 1991-02-06 逝于美国马萨诸塞州列克星敦，享年 78 岁）
- **气质关键词**：**噬菌体学派的缔造者、细菌遗传学的统计证明者、MIT 癌症研究中心的建系人**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1969 条目，与 Max Delbrück、Alfred Hershey 三人共享同一理由）：
  > "for their discoveries concerning the replication mechanism and the genetic structure of viruses"（因他们发现病毒复制机制和病毒遗传结构）
- **设计母题**：**突变的手气（fluctuation test）**——Luria–Delbrück 实验中"老虎机"式的突变随机涨落意象：以培养皿上抗性菌落的随机散点分布作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Salvador_Luria/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Salvador_Luria/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Salvador_Luria_zh`、`VIDEO_NAME=Salvador_Luria_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | bacterial genetics | 细菌遗传学 | 突变的达尔文式证明、抗性遗传，1969 诺奖核心 |
| 1 | molecular biology | 分子生物学 | infobox Fields 明载；噬菌体学派 |
| 2 | virology | 病毒学 | 噬菌体复制机制与遗传结构 |
| 3 | restriction enzymes | 限制性内切酶基础 | 与 Bertani 发现宿主控限现象 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Giuseppe Levi | 对方 → 导师 | 都灵大学医学院老师（MD 1935） |
| advisor-student | James Watson | Luria → 学生 | 印第安纳大学首位研究生；后与 Crick 发现 DNA 双螺旋 |
| advisor-student | Jon Kabat-Zinn | Luria → 学生 | infobox Doctoral students 明载 |
| spouse | Zella Luria | 无向 | 1945 结婚，育一子 |
| colleague | Rita Levi-Montalcini | 无向 | 都灵 Levi 门下同门，未来诺奖得主 |
| colleague | Renato Dulbecco | 无向 | 都灵 Levi 门下同门，未来诺奖得主 |
| colleague | Max Delbrück | 无向 | 1943 涨落实验合作者，Cold Spring Harbor/Vanderbilt 合作 |
| colleague | Giuseppe Bertani | 无向 | 1950s 共同发现宿主控限现象 |
| co-honored | Max Delbrück | 无向 | 1969 诺贝尔生理学或医学奖三人共享（病毒复制机制与遗传结构） |
| co-honored | Alfred Hershey | 无向 | 1969 诺贝尔生理学或医学奖三人共享（病毒复制机制与遗传结构） |

**不入库但提示词可叙述**：Enrico Fermi（助其获洛克菲勒基金会奖学金）；Latarjet（1947 Luria–Latarjet 效应合著）；Esther Lederberg 等 1953 冷泉港合影人物；Pauling（1957 联名抗议核试验）；Baltimore/Tonegawa/Sharp/Horvitz（MIT 中心同事，机构叙述）；Chomsky/Wiesel（友人，正文不展开）。

## 五、配色方案 【人物专属】

- **气质**：流亡者的坚韧、统计学的冷静、建系者的担当
- **主色**：`#0F3B5C`（地中海深蓝——从都灵到波士顿的流亡航线）+ 香槟金诺奖色
- **badge 四分类色**：`badgePhage` 噬菌体学派 深蓝 `#0F3B5C`；`badgeFluct` 涨落实验 青绿 `#0E7C7B`；`badgeRestrict` 限制修饰 琥珀 `#C07A2A`；`badgeMIT` MIT 建系 玫瑰 `#A63A2B`
- **背景母题**：培养皿上抗性菌落的随机散点分布，呼应「突变的手气」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 噬菌体学派的缔造者 / Salvador Luria 1912–1991 + 四色 badge + 右上头像 + 国籍行（United States / Italy）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1912-08-13 都灵 ~ 1991-02-06 列克星敦、
    都灵大学 MD 1935、1950 入籍美国、MIT 微生物学系主任 1959、诺奖 1969）
03  核心贡献概览 — 涨落实验 / 抗性遗传 / Luria–Latarjet 效应 / 限制修饰现象
04  都灵与 Levi 门下 (1912–1937) — 塞法迪犹太家庭、Giuseppe Levi 门下、
    同门 Levi-Montalcini 与 Dulbecco、Radiology 进修初遇 Delbrück 基因分子观
05  流亡之路 (1938–1940) — 意大利种族法禁犹太人领研究金、赴巴黎、
    1940 骑车逃马赛、9 月抵纽约（改名 Salvador Edward）
06  美国起步与噬菌体小组 (1940–1943) — Fermi 助力洛克菲勒奖学金、哥伦比亚大学、
    结识 Delbrück 与 Hershey、冷泉港合作
07  1943：涨落实验（核心贡献页）— 细菌突变按达尔文式而非拉马克式发生、
    病毒不在场时抗性突变已随机出现——抗生素抗性的理论根基
08  Luria–Latarjet 效应 (1947) — 紫外线照射下噬菌体胞内增殖的抗性先升后降、
    DNA 修复通路的后知
09  印第安纳与 Watson (1943–1950) — 首位研究生 James D. Watson；1950 迁伊利诺伊
10  限制修饰现象 (1950s)（核心贡献页）— 与 Bertani 发现宿主控限、
    后人发现限制性内切酶——分子生物学主要工具的源头之一
11  MIT 岁月 (1959–) — 微生物学系主任、1963 巴斯德研究所休假发现细菌素破膜、
    离子梯度机制；1972 创建癌症研究中心（Baltimore/Tonegawa/Sharp/Horvitz）
12  荣誉与认可 — Guggenheim 1942、NAS 1960、美国微生物学会主席 1968–69、
    Horwitz Prize 1969（与 Delbrück）、Nobel 1969、国家科学奖章 1991
13  公共良知 — 1957 与 Pauling 联名反对核试验、反对越战、支持工会、
    基因工程温和监管立场、1969 短暂被 NIH 列入黑名单（客观叙述）
14  遗产与结尾 — 噬菌体学派的传承谱系（Watson 一脉的分子生物学）；1974 国家图书奖
    科普写作；《A Slot Machine, A Broken Test Tube》自传书名点题
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名链条 | 本名 Salvatore Luria，抵美后改 Salvatore→Salvador Edward；manifest/DB 用 Salvador Luria，正文可交代本名 |
| 涨落实验年份 | 1943 年与 Delbrück 完成（Luria–Delbrück experiment）——统计证明突变是随机的、达尔文式，勿写成"证明细菌会突变"泛化 |
| 诺奖三人分工 | Delbrück（基因作为分子的理论框架）、Luria（细菌抗性遗传/涨落实验）、Hershey（噬菌体实验体系与 Hershey–Chase）——citation 同一句，个人侧重分层；Hershey–Chase 实验 page.md 未载细节，Hershey 侧重表述从简 |
| 限制修饰归属 | 现象由 Luria 与 Bertani 发现（1950s）；**限制性内切酶本身由其他研究者**（Arber/Nathans/Smith）随后发现——勿写"Luria 发现限制性内切酶" |
| Luria–Latarjet 效应 | 1947 紫外照射下噬菌体抗性先升后降；后来归因于噬菌体编码的多条 DNA 修复通路——"先升后降"方向勿写反 |
| Watson 师承 | Watson 是 Luria 在**印第安纳大学**的首位研究生——与 Watson-Crick 的 DNA 结构（1953 剑桥）区分，勿把 Watson 写成"在 Luria 实验室发现双螺旋" |
| 两位都灵同门 | Levi-Montalcini 与 Dulbecco 都是 Levi 门下同学（"met" 明载）——colleague 边即可，勿写成合作研究 |
| 国籍口径 | citations json "Italy United States"、正文 "Italian microbiologist, later naturalized U.S. citizen"——yaml 取 US(0)+Italy(1)；封面国籍行两写 |
| 政治内容 | 反核/反越战/工会/基因工程监管立场为 page.md 明载（含 1969 被 NIH 短暂黑名单）——按项目纪律政治主张**不入正文**，仅机构与科学事件可客观叙述；正文从简 |
| 卒因 | 1991-02-06 心脏病发作逝于列克星敦，享年 78 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Luria–Delbrück experiment | 卢里亚–德尔布吕克实验 | 涨落分析/波动实验 |
| fluctuation test | 涨落实验 | 统计学证明突变随机性 |
| Darwinian inheritance | 达尔文式遗传 | 与拉马克式对立 |
| bacteriophage | 噬菌体 | 感染细菌的病毒 |
| host-controlled restriction and modification | 宿主控限的限制与修饰 | 限制酶现象源头 |
| bacteriocin | 细菌素 | MIT 期转向研究对象 |
| electrochemical gradient | 电化学梯度 | 细菌素破膜机制的后果 |
| restriction enzyme | 限制性内切酶 | 后人发现，非 Luria 亲手 |
| phage group | 噬菌体小组 | Delbrück/Luria/Hershey 学派 |
| Life: the Unfinished Experiment | 《生命：未完成的实验》 | 1974 国家图书奖科普书 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从都灵医学院到噬菌体小组再到 MIT 癌症中心——Luria 的遗产是一条穿越纳粹阴云而绵延不绝的学术血脉；"Timeless" 匹配其学派传承的永恒性与流亡者重建的定力。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Salvador_Luria/Timeless.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
