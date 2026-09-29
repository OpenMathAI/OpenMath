# 医学家立传提示词（August Krogh）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1920 年得主 August Krogh（奥古斯特·克罗格）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/August_Krogh/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Schack August Steenberg Krogh（1874-11-15 生于丹麦 Grenaa ~ 1949-09-13 逝于哥本哈根，享年 74 岁）
- **气质关键词**：**毛细血管的测量者、比较生理学的开山者、Novo Nordisk 的催生者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1920 条目）：
  > "for his discovery of the capillary motor regulating mechanism"（因其发现毛细血管运动调节机制）
- **设计母题**：**开合的毛细血管网（opening & closing capillaries）**——骨骼肌按需求开启/关闭微动脉与毛细血管、血流灌注随需分配，是「生命按需供血」的视觉隐喻：由细线网络渐次点亮/熄灭的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/August_Krogh/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/August_Krogh/`（肖像约 1900 年像，见 images.txt）。Makefile 复制后设 `MAIN=August_Krogh_zh`、`VIDEO_NAME=August_Krogh_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Krogh 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 毛细血管调节，1920 诺奖核心 | 封面、核心页 |
| 1 | vascular physiology | 血管生理学 | 毛细血管运动调节机制（微动脉开合） | 核心页 |
| 2 | respiratory physiology | 呼吸生理学 | 皮肤与肺呼吸、CO 弥散容量 | 核心页 |
| 3 | comparative physiology | 比较生理学 | 水生动物渗透调节、Krogh 原则 | 后期页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Christian Bohr | 对方 → 导师 | infobox Doctoral advisor 明载（1903 博士，蛙皮肤与肺呼吸论文） |
| spouse | Marie Krogh | 无向 | 1905 结婚（née Jørgensen，1874–1943），自身为知名科学家、长期密切合作 |
| colleague | George de Hevesy | 无向 | 1930s 合作重水与放射性同位素膜通透研究（库内规范名，id=2132） |
| colleague | Niels Bohr | 无向 | 1930s 合作并共同为丹麦取得首台回旋加速器（库内规范名，id=1104） |
| colleague | Hans Christian Hagedorn | 无向 | 1923 共同创建 Nordisk Insulinlaboratorium 在丹麦产胰岛素 |
| influence | William Sørensen | 对方 → 影响 | 终生挚友，Krogh 称其「领我入科学方法之门」的老师 |
| advisor-student | Knut Schmidt-Nielsen | Krogh → 学生 | infobox Notable students 明载 |
| advisor-student | Hans Ussing | Krogh → 学生 | infobox Notable students 明载 |
| advisor-student | Torkel Weis-Fogh | Krogh → 学生 | 昆虫飞行研究先驱；1951 与 Krogh 合著经典论文 |
| parent-child | Bodil Schmidt-Nielsen | Krogh → 女 | 1918 生，生理学家，1975 首位美国生理学会女主席 |

**不入库但提示词可叙述**：Marie Krogh 的科研合作者身份（合作不设 colleague 边，spouse 一行承载）；1922 多伦多之行会见 Banting/Best/Macleod（一次性访问，获北欧胰岛素生产授权，非持续关系）；J.M.C. Schiödte / Japetus Steenstrup / Eug. Warming（Sørensen 恩怨链中的旁支人物）；其余子女 Erik/Ellen/Agnes（仅具名无实质）；女婿身份（Bodil 嫁 Knut Schmidt-Nielsen）不另设边。

## 五、配色方案 【人物专属】

- **气质**：清冽、精确、北欧的实验台之光
- **主色**：`#1E4E79`（丹麦海峡蓝——哥本哈根实验室的沉静测量）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeCap` 毛细血管调节 — 海蓝 `#1E4E79`
  - `badgeResp` 呼吸生理 — 青绿 `#0E7C7B`
  - `badgeComp` 比较生理 — 苔绿 `#175E54`
  - `badgeNovo` 胰岛素事业 — 琥珀 `#C07A2A`
- **背景母题**：细密毛细血管网按需点亮的线条图案，呼应「灌注随需分配」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 毛细血管的测量者 / August Krogh 1874–1949 + 四色 badge + 右上头像 + 国籍行（Denmark）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地 Grenaa、哥本哈根大学 MSc 1899/PhD 1903、
    哥本哈根动物生理学教授 1916–1945、诺奖 1920、核心领域）
03  核心贡献概览 — 毛细血管调节 / 呼吸交换 / 渗透调节 / 胰岛素产业
04  格勒纳少年与海上学徒 (1874–1889) — 14 岁毕业、炮艇 HDMS Hauch 上的海洋志愿实习生
05  哥本哈根求学 (1889–1903) — MSc 1899；博士论文蛙的皮肤与肺呼吸 1903，师从 Christian Bohr
06  毛细血管运动调节机制（核心贡献页）— 微动脉与毛细血管按需开合、灌注适应需求
07  呼吸交换与仪器制作 — 《The Respiratory Exchange of Animals and Man》1916；肺活量计、基础代谢率仪
08  动物生理学实验室 (1908–1916) — 1908 讲师、1916 正教授，丹麦首个动物生理实验室主任
09  比较生理学与渗透调节 — 《Osmotic Regulation》1939、《Comparative Physiology of Respiratory Mechanisms》1941
10  Krogh 原则 — 「大量问题总有一种最合适的动物可供研究」引语（page.md 明载）
11  与 Hevesy、Bohr 的合作 (1930s) — 重水与放射性同位素膜通透；丹麦首台回旋加速器
12  胰岛素与 Novo Nordisk (1922–1925) — 多伦多之行获授权；1923 Nordisk Insulinlaboratorium；
    1925 Novo 另立、1989 合并（时间线分立呈现）
13  家学与传承 — 妻 Marie（合作者）；女 Bodil（首位美国生理学会女主席）；学生 Schmidt-Nielsen/Ussing/Weis-Fogh
14  遗产与结尾 — Krogh length / Krogh 原则 / 现代血管生理 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1920 独得 | 单独得主，无 co-honored；获奖理由官方口径 "capillary motor regulating mechanism"（毛细血管运动调节机制），勿写成"肌肉灌注研究"泛化 |
| 两位 Bohr | 博士导师 **Christian Bohr**（玻尔之父）≠ 库内 id=1104 的物理学家 **Niels Bohr**——师生边用 Christian Bohr（新建 stub），同事边用 Niels Bohr（库内既有），两条边不可互串 |
| 全名 | Schack August Steenberg Krogh；yaml/manifest 用 **August Krogh**，正文可交代全名 |
| 10 万公里血管 | Krogh 著作普及了「人体血管总长 100,000 km」——**page.md 明载这是错误数字**（实际约 9,000–19,000 km，基于 unrealistic 140 kg 假设体型），立传如实写为历史讹误，Review 勿"替他改正" |
| Novo ≠ Nordisk | 1923 Nordisk Insulinlaboratorium（Krogh+Hagedorn）；1925 前员工 Pedersen 兄弟另创 **Novo**；两公司竞争至 **1989 才合并**为 Novo Nordisk——三个时间点勿混写为"Krogh 创立 Novo Nordisk" |
| Marie 的角色 | 妻 Marie 自身是知名科学家、"much of his work was carried out in close collaboration with her"——可写合作，但奖项为 Krogh 独得，勿写共享或共同获奖 |
| Sørensen 引语 | "my teacher into scientific method" 为 page.md 明载引语，可引原文+译文；Sørensen 是 Krogh 父亲的童年好友、年长 26 岁 |
| 学派恩怨 | Krogh 站队 Sørensen/Schiödte 一方攻击 Steenstrup 一派，得罪 Warming（1908 讲席推荐委员会成员）但未影响生涯——可叙述，人物均不入库 |
| 学术会员年份 | 1931 美国艺术与科学院 / 1937 美国 NAS / 1941 美国哲学会——三个年份勿混 |
| 命名遗存 | Krogh length（毛细血管间距）、Krogh model、Krogh's principle——均为遗存命名，与诺奖理由区分；200+ 篇论文 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| capillary motor regulating mechanism | 毛细血管运动调节机制 | 获奖理由核心词，逐字对应 |
| arteriole | 微动脉 | 开合控制的主体 |
| perfusion | 灌注 | 血流按需分配 |
| diffusing capacity for carbon monoxide | 一氧化碳弥散容量 | Krogh 已知贡献之一 |
| Krogh's principle | 克罗格原则 | 「选对动物」的比较生理学方法论 |
| Krogh length | 克罗格长度 | 毛细血管间扩散距离 |
| osmotic regulation | 渗透调节 | 水生动物方向，1939 专著 |
| basal metabolic rate | 基础代谢率 | 其仪器可测量 |
| spirometer | 肺活量计 | 发明/改良的仪器 |
| zoophysiology | 动物生理学 | 哥本哈根教席名称（1916–1945） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Ascension**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从格勒纳少年到哥本哈根讲席、从毛细血管的显微观察到为丹麦赢得第一台回旋加速器——「攀升」对应其不断扩展的研究疆域；同时 Novo Nordisk 至今惠及全球糖尿病患者的产业遗产，是超越个人一生的上升线。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/August_Krogh/Ascension.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
