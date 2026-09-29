# 医学家立传提示词（George Wells Beadle）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1958 年得主 George Wells Beadle（乔治·韦尔斯·比德尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/George_Wells_Beadle/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：George Wells Beadle（1903-10-22 生于内布拉斯加州 Wahoo ~ 1989-06-09 逝于加州波莫纳，享年 85 岁，阿尔茨海默并发症），美国遗传学家，芝加哥大学第七任校长（1961-1968）
- **气质关键词**：**一基因一酶的提出者、内布拉斯加农家子、退休后破解玉米起源的老顽童**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1958 条目，Beadle/Tatum 共享一半；Lederberg 独得另一半）：
  > "for their discovery that genes act by regulating definite chemical events"（因其发现基因通过调控特定化学反应而起作用）
- **设计母题**：**一条被射线打断的代谢通路（X-ray → auxotroph → one gene-one enzyme）**；用「玉米田与代谢通路阶梯的叠影」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/George_Wells_Beadle/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/George_Wells_Beadle/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=George_Wells_Beadle_zh`、`VIDEO_NAME=George_Wells_Beadle_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Beadle 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | genetics | 遗传学 | infobox Fields 明载 | 全篇 |
| 1 | biochemical genetics | 生化遗传学（一基因一酶） | 1958 诺奖核心 | 核心页 |
| 2 | maize genetics | 玉米遗传学（大刍草起源） | 退休后的定论性实验：5-6 个遗传位点差异 | 玉米页 |
| 3 | cytogenetics | 细胞遗传学 | 康奈尔博士：玉米孟德尔不联会 | 教育页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Franklin D. Keim | 对方 → 导师 | 内布拉斯加本科后导师（杂交小麦），为其谋得康奈尔助教职位 |
| advisor-student | Rollins A. Emerson | 对方 → 博士导师 | 康奈尔（1931，玉米孟德尔不联会） |
| advisor-student | Lester W. Sharp | 对方 → 并列博士导师 | 康奈尔（细胞学） |
| advisor-student | Thomas Hunt Morgan | 对方 → 博士后阶段 | 加州理工 1931-1936（infobox Other academic advisors 明载；库内 id=5339） |
| colleague | Boris Ephrussi | 无向 | 1935 巴黎半年合作，果蝇眼色素移植实验，引向 Neurospora 生化遗传学 |
| colleague | Theodosius Dobzhansky | 无向 | 加州理工时期果蝇交叉遗传合作（库内 id=5353） |
| colleague | Alfred Sturtevant | 无向 | 加州理工时期果蝇交叉遗传合作（库内 id=5342） |
| co-honored | Edward Lawrie Tatum | 无向 | 1958 诺贝尔生理学或医学奖共享一半 |
| co-honored | Joshua Lederberg | 无向 | 1958 同届诺奖（Lederberg 独得细菌遗传重组一半） |
| spouse | Muriel McClure | 无向 | 第二任妻子（1915-1994），知名作家 |
| advisor-student | Robert Metzenberg | Beadle → 博士生 | infobox Doctoral students 明载 |
| advisor-student | Norman Horowitz | Beadle → 博士后合作者 | infobox Other notable students 明载 |
| advisor-student | Herschel K. Mitchell | Beadle → 博士后合作者 | infobox Other notable students 明载 |
| advisor-student | William D. McElroy | Beadle → 博士后合作者 | infobox Other notable students 明载 |
| advisor-student | Clement Markert | Beadle → 博士后合作者 | infobox Other notable students 明载 |

**不入库但提示词可叙述**：S. Emerson（与 Dobzhansky/Sturtevant 并列提及，仅姓氏无法定位规范名）；第一任妻子与长子 David（前妻未具名，不建边）；Norman Horowitz 关于基因/生物合成史意义的回忆（"As recalled by Horowitz"——引述源非边）。

## 五、配色方案 【人物专属】

- **气质**：内布拉斯加的玉米金、加州理工的严谨、芝加哥校长的器度
- **主色**：`#8C6D1F`（玉米金——大平原农田与玉米起源实验）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeOne` 一基因一酶 — 玉米金 `#8C6D1F`
  - `badgeMold` Neurospora 实验 — 砖橙 `#C1502E`
  - `badgeTeos` 大刍草起源 — 深绿 `#146B3A`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：玉米叶脉与代谢通路阶梯，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 一基因一酶的提出者 / George W. Beadle 1903–1989 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Wahoo 出身、内布拉斯加/康奈尔、
    加州理工/哈佛/斯坦福/芝大任职、诺奖 1958、核心领域）
03  核心贡献概览 — Neurospora 突变体 / 一基因一酶 / 基因调控化学反应 / 玉米起源
04  Wahoo 农家子 (1903–1926) — 40 英亩农场、恩师引路进农学院、1926 BS
05  Keim 与康奈尔 (1926–1931) — 杂交小麦一年、MS 1927、Emerson/Sharp 门下玉米不联会、1931 PhD
06  加州理工研究员 (1931–1936) — Morgan 门下、与 Dobzhansky/Sturtevant 果蝇交叉遗传
07  巴黎半年：Ephrussi (1935) — 果蝇眼色素移植实验——通往生化遗传学的桥
08  斯坦福与 Tatum (1937–1946) — 果蝇→Neurospora、X 射线诱变、1941 三个营养缺陷型
09  一基因一酶假说（核心贡献页）— 基因调控特定化学反应；"基因只管眼色须毛"旧观念的革命
10  1958 诺奖：与 Tatum 共享一半 — 获奖理由逐字呈现、Lederberg 独得另一半（结构讲清）
11  芝加哥校长岁月 (1961–1968) — Chancellor→第七任校长、1962 与学生 Sanders 同框（见陷阱表：回避）
12  退休再战：玉米起源（核心页）— 大刍草杂交实验、5-6 个位点差异、驯化起源定论
13  荣誉与认可 — Lasker 1950、Mendel Medal 1958、Kimber 1960、Morgan Medal 1984、ForMemRS、
    遗传学会 George W. Beadle 奖以其名立
14  遗产与结尾 — 分子遗传学的奠基人之一 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | **yaml/入库用 manifest 形式 "George Wells Beadle"**；封面写 George W. Beadle 或全名均可 |
| 1958 的"一半"结构 | **Beadle/Tatum 共享一半 + Lederberg 独得另一半**——勿三人平分；与 Tatum 同句理由（"for their discovery..."） |
| 无博士导师单选 | 康奈尔阶段 Emerson 与 Sharp **并列双导师**——两条边并行勿合并；Keim 是本科后导师（亦列 infobox Other academic advisors），Morgan 是博士后阶段——四条 advisor-student 边各有其位 |
| 政治人物回避 | 1962 年与学生 Bernie Sanders 在 CORE 住房静坐集会同框的照片为 page.md 实载——**政治敏感人物，插图与正文均回避** |
| 玉米起源数字 | 二代分离中约 1/500 植株与亲本一致、推算玉米与大刍草差 5-6 个遗传位点——两个数字勿混 |
| "旧观念"转述 | 1941 年时"非遗传学家认为基因只管眼色/须毛等小事、基础生化由细胞质决定"——是 page.md 对时代背景的转述，勿写成 Beadle 原话 |
| 果蝇图片噪声 | page.md 果蝇图说明 "the object of Beadle's science" 系模板复用（与 Hall/Tatum 页同图）——Beadle 的诺奖对象是 Neurospora 不是果蝇，正文以 Neurospora 为准 |
| 私生活口径 | 两婚：前妻未具名（长子 David 住海牙）；第二任 Muriel McClure 为知名作家——spouse 边只建 Muriel；爱好攀岩/滑雪/园艺、首登阿拉斯加 Doonerak 山、内布拉斯加 FarmHouse 兄弟会——身份页调剂 |
| 死因 | 1989-06-09 逝于波莫纳退休社区，阿尔茨海默病并发症——勿写成自然衰老；其无神论立场可一句带过 |
| 荣誉年份链 | AAAS Fellow 1946、Lasker 1950、Dyer 1951、Hansen 1953、Einstein 纪念奖+Mendel Medal+Nobel 1958、癌症学会全国奖 1959、Kimber 1960、Morgan Medal 1984——勿串；荣誉博士 12 个择要列举 |
| 引语红线 | page.md 无 Beadle 直接引语——禁编引语；Horowitz 回忆段是转述 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| genes act by regulating definite chemical events | 基因通过调控特定化学反应起作用 | 获奖理由逐字对应 |
| one gene-one enzyme hypothesis | 一基因一酶假说 | 后有"限定与修正"，至今基本成立 |
| Neurospora crassa | 粗糙脉孢菌 | X 射线诱变材料，斜体 |
| auxotroph | 营养缺陷型 | 最小培养基筛选体系 |
| Mendelian asynapsis | 孟德尔不联会 | 博士论文主题（Zea mays） |
| crossing-over | 交换 | 果蝇时期的课题 |
| teosinte | 大刍草 | 玉米野生祖先，5-6 位点差异 |
| eye pigment transplant | 眼色素移植 | 1935 与 Ephrussi 的果蝇实验 |
| metabolic pathway | 代谢通路 | 基因作用的层级 |
| George W. Beadle Award | Beadle 奖 | 遗传学会以其名立的奖项 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Beadle 的一生像海市蜃楼般不断变换风景——内布拉斯加麦田、康奈尔玉米地、巴黎实验室、斯坦福霉菌、芝加哥校长府、再到退休后的中美洲玉米起源之谜；Mirage 的流转感对应这种跨越学科与地理的多幕人生，也对应"基因如何指挥化学反应"这一曾被认为不可解的幻影终被钉牢。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/George_Wells_Beadle/Mirage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
