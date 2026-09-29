# 医学家立传提示词（Willem Einthoven）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1924 年得主（威廉·埃因托芬，心电图机之父）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Willem Einthoven（1860-05-21 生于荷属东印度三宝垄 Semarang ~ 1927-09-29 卒于荷兰莱顿，享年 67 岁）
- **气质关键词**：**第一台实用心电图机的发明者、临床心电图学的开创者、PQRST 与 Einthoven 三角的命名者** —— 1924 获奖理由（独享）：
  > "for the discovery of the mechanism of the electrocardiogram"（因发现心电图机制）
- **设计母题**：**心电曲线**。弦电流计在感光纸上划出的连续曲线——P、Q、R、S、T 五个波折是心跳写给医生的信。视觉隐喻以一条贯穿版面的心电迹线为背景母题，四种 badge 色对应五个波群的节律。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Willem_Einthoven/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Willem_Einthoven/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准——卒日双值裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Willem_Einthoven/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Willem_Einthoven_zh`、`VIDEO_NAME=Willem_Einthoven_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Willem_Einthoven/images.txt`（1906 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图必用早期 ECG 设备照（Willem_Einthoven_ECG.jpg）。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Willem_Einthoven.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 莱顿生理学教授（1886 起） | 身份页 |
| 1 | electrocardiography | 心电学 | 弦电流计 + PQRST + Einthoven 三角，1924 诺奖核心 | 核心页 |
| 2 | cardiovascular disease | 心血管疾病 | 心电图特征描述的系列疾病 | 临床页 |
| 3 | acoustics | 声学 | 晚年与 Battaerd 研究心音 | 晚年页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Frédérique Jeanne Louise de Vogel | 无向 | 表亲（first cousin）结婚，1861-1937 |
| colleague | P. Battaerd | 无向 | 晚年合作研究心音（声学） |

> **metadata-only 不入库**：metadata.json 有 `doctoral_advisor: Franciscus Donders`，但 **page.md 通篇无载**——按纪律不建边，在本表记录此裁定供 Review 核对。
> 不入库：其妻之弟 Willem Thomas de Vogel（资助其上学，家族事件）；女儿/子女 page.md 未载。
> 库内当时无 P. Battaerd 记录，由本 yaml 新建 stub。本页关系仅 2 条系诚实值（page.md 篇幅所限），Review 勿误判为缺漏。

## 五、配色方案 【人物专属】

- **气质**：感光纸的米白 + 电极的冷金属 + 心电迹线的墨青
- **主色**：心电青 `#0E7490`（感光纸上曲线的墨色，冷静精确）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 弦电流计 — 钢蓝 `#2E4A66`
  - `badgeB` PQRST/心电学 — 心电青 `#0E7490`
  - `badgeC` 临床心血管 — 朱红 `#B02A30`
  - `badgeD` 声学/心音 — 琥珀 `#C77F3B`
- **背景母题**：一条横贯版面的细心电迹线（P-Q-R-S-T 波折），badge 圆点像电极位置错落分布。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 心电图机之父 / Willem Einthoven 1860–1927 + 四色 badge + 右上头像 + 国籍行 Netherlands
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 Semarang/Leiden、教育 Utrecht MD 1885、
    任职 Leiden 1886 起、荣誉 Nobel 1924、核心领域、名下术语 PQRST/Einthoven 三角）
03  核心贡献概览 — 弦电流计 / 心电图机制 / PQRST 命名体系 / 临床心电学
04  东印度出生与乌得勒支求学 (1860–1885) — 三宝垄出生、幼年丧父、1870 随母回荷兰定居乌得勒支、
    1885 乌得勒支大学医学学位
05  莱顿教授 (1886–1901) — 1886 任莱顿大学教授、娶表亲 Frédérique de Vogel、
    资助其弟 Willem Thomas de Vogel 完成莱顿学业
06  问题：隔着的电 — 心脏电活动已知但无法体表精确测量（须直接贴电极于心脏），
    体表测量被肌肤骨骼衰减——技术缺口即机会
07  弦电流计 (1901–1906) — 1901 起系列原型、强电磁铁间导电细丝、光影投于感光纸卷、
    270 kg、需水冷、五人操作——灵敏度足以穿透体表
08  PQRST 与 Einthoven 三角 — 五个波群字母命名沿用至今、标准肢体导联的倒置等边三角形、
    术语体系是页面的"词汇遗产"
09  临床心电学 — 系列心血管疾病的心电图特征描述，把仪器变成诊断工具
10  1924 诺贝尔奖 — "for the discovery of the mechanism of the electrocardiogram"、
    1925-12-11 诺奖演讲 The String Galvanometer and the Measurement of the Action Currents of the Heart
11  晚年：心音的声学 — 转向声学、与 Battaerd 研究心音
12  荣誉与会员 — 1902 荷兰皇家艺术与科学院院士、皇家学会外籍会员、
    2019 入选 National Inventors Hall of Fame（metadata 载）
13  身后与纪念 — 1927-09-29 卒于莱顿、葬 Oegstgeest 改革宗"绿教堂"墓园、
    1970 月球背面 Einthoven 陨石坑、2019-05-21 159 岁冥诞 Google Doodle
14  遗产 — 从 270 kg 到腕表：心电设备的进化史以他为起点、术语沿用百年、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for the discovery of the mechanism of the electrocardiogram"；page.md 另有转述"发明首套实用心电诊断系统"，两者勿混用 |
| 独享 | 1924 无共享者，勿杜撰共同得主 |
| 卒日双值 ★ | metadata.json 双值 1927-09-28 / 09-29；infobox 与正文均为 **29 September 1927**——取 09-29，yaml/幻灯片一致 |
| 出生地 | 荷属东印度三宝垄（今印尼爪哇），勿写"生于荷兰" |
| 弦电流计数字 | 270 kg、需水冷、五人操作、1901 起原型——三个数字勿错 |
| PQRST | 字母命名沿用至今；勿写成"Einthoven 发明心电图"以外的过度归功（后续便携化由后人完成） |
| Donders 裁定 ★ | metadata 有 doctoral_advisor Franciscus Donders，page.md 无载——**不入库**（防无载边）；如 Review 追问以此裁定答复 |
| 妻子身份 | Frédérique 是其 first cousin（表亲），婚前姓 de Vogel；1861-01-07 生、1937-01-31 卒 |
| 莱顿任职 | 1886 任莱顿教授，1902 入荷兰皇家艺术与科学院——两个年份勿混 |
| 页面极简 | page.md 篇幅短（无师承/学生记载）——**勿从维基其他来源补料**，缺页处用仪器原理图与术语表充实 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| electrocardiogram (ECG/EKG) | 心电图 | EKG 为德语缩写，两者同义 |
| string galvanometer | 弦电流计 | 核心发明，勿写成"示波器" |
| Einthoven's triangle | Einthoven 三角 | 双臂+腿标准电极的倒置等边三角 |
| PQRST waves | PQRST 波群 | 心房除极 P 与心室除极/复极 QRS、T |
| lead | 导联 | 电极组合的测量通道 |
| transthoracic | 经胸的 | 体表测量得以实现的关键词 |
| action current | 动作电流 | 其诺奖演讲主题用语 |
| heart sounds | 心音 | 晚年声学研究对象 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart**（manifest 预分配）
- **风格**：律动 / 深情 / 电子氛围
- **匹配理由**：曲名"散落又重组"暗合心跳的电信号节律——弦电流计把看不见的心电"拆解"为可见曲线，Falling Apart 的起伏波形感与心电迹线的设计母题同构。
- **本地路径**：`music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav` → 复制为 `presentations/20th_century/Willem_Einthoven/Falling_Apart.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；page.md 篇幅短，宁少勿造。**
