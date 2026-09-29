# 医学家立传提示词（James Watson）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：James Watson（1962 年诺贝尔生理学或医学奖得主，美国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/James_Watson/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：James Dewey Watson（詹姆斯·杜威·沃森，1928-04-06 芝加哥 ~ 2025-11-06 纽约州东诺斯波特，享年 97 岁）
- **气质关键词**：**DNA 双螺旋的共同发现者、分子生物学时代的开启者、人类基因组计划的首任掌门与终身争议者** —— 1962 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Crick、Wilkins 三人共享）：
  > "for their discoveries concerning the molecular structure of nucleic acids and its significance for information transfer in living material"
  > （因其关于核酸分子结构及其在生命物质信息传递中的意义的发现）
- **设计母题**：**「双螺旋与它的阴影」**。1953 年的纸板模型改变了生物学，而数据归属的争议与晚年的言论风波构成同一条链的暗面——视觉隐喻：明亮的螺旋主链与背景中低透明度的阴影螺旋互为镜像。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/James_Watson/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/James_Watson/`，成目录 `medic/presentations/20th_century/James_Watson/`，Makefile 复制后设 `MAIN=James_Watson_zh`、`VIDEO_NAME=James_Watson_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库：本人记录复用库内既有 stub（id=3787）UPD 回填 QID Q83333；同名分裂 stub「James D. Watson」(3610，Perutz/Kendrew/Horvitz/Capecchi 四边) 已归并改指至 3787 并删除。`has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | molecular biology | 分子生物学 | DNA 双螺旋（1953），1962 诺奖核心 | 双螺旋页 |
| 1 | genetics | 遗传学 | 噬菌体学派训练、基因物质基础 | 遗传页 |
| 2 | genomics | 基因组学 | 人类基因组计划首任负责人（1988-1992） | 基因组页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/James_Watson.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Salvador Luria | 师 | 印第安纳大学博士导师，噬菌体学派 |
| influence | Max Delbrück | — | 噬菌体学派共同领袖，多次咨询其噬菌体实验方向 |
| co-honored | Francis Crick | — | 1962 诺贝尔生理学或医学奖三人共享（DNA 结构） |
| co-honored | Maurice Wilkins | — | 1962 诺贝尔生理学或医学奖三人共享（DNA 结构） |
| collaborator | Francis Crick | — | 1953 年 Nature DNA 双螺旋论文共同作者 |
| controversy | Rosalind Franklin | — | 未经知情同意使用其衍射数据且归因不足，晚年备受批评 |
| spouse | Elizabeth Lewis | — | 1968 年成婚 |
| parent-child | Jean Mitchell | 母 | — |
| parent-child | Rufus Robert Watson | 子 | 患精神分裂症，推动遗传学解精神疾病 |
| parent-child | Duncan James Watson | 子 | 1972 年生 |
| advisor-student | Peter B. Moore | 生 | 博士生（infobox 明载） |
| advisor-student | David Schlessinger | 生 | 博士生（infobox 明载） |
| advisor-student | Joan Steitz | 生 | 博士生（infobox 明载） |
| advisor-student | Phillip Allen Sharp | 生 | 博士后（infobox 明载） |
| advisor-student | Richard J. Roberts | 生 | 博士后（infobox 明载） |

> 说明：Capecchi/Horvitz 两条师生边已由其本人批次先建（库内 3787 名下），本 yaml 不重复列；Pauling influence 边已由 Pauling 侧先建（8932），亦不重复。父亲 James D. Watson 与本人在库内历史 stub 中同名——为防「父名=子名」混淆（Richet 之子先例），父不入库仅文字叙述。其余不入库：Kalckar/Maaløe（博士后东家，前者互动不顺）、Hermann Muller（ attract 因素仅一句）、Raymond Gosling（Franklin 学生，归 Wilkins/Franklin 篇）、Venter（宿怨无事件边）、E.O. Wilson（口角）、Healy（基因专利冲突系机构争议）、Brenner/Dunitz/Hodgkin/Orgel（1953 年看模型的观众群）。六个 postdoc/学生中 Sharp/Roberts（1993 诺奖）与三位博士生入库，Birney/Davis/Tooze/Nancy Hopkins 不入库。

## 五、配色方案 【人物专属】

- **气质**：锐利、冒进、天才与争议同体的双面性
- **主色**：螺旋靛蓝 `#2B4A8C`（1953 年模型与 Nature 版面的冷调）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 分子生物学 — 双螺旋青 `#1F7A6D`
  - `badgeB` 遗传学 — 噬菌体紫 `#5B4E8E`
  - `badgeC` 基因组学 — 测序蓝 `#33637D`
  - `badgeD` 争议暗面 — 阴影灰 `#6E7378`
- **背景母题**：明亮双螺旋主链 + 低透明度阴影螺旋（母题的双重性），稀疏碱基对短杆，铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — DNA 双螺旋的共同发现者 / James Watson 1928–2025 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — 双螺旋 / 噬菌体学派 / 人类基因组计划 / 冷泉港时代
04  芝加哥神童 (1928–1947) — Quiz Kids、观鸟少年、15 岁入芝加哥大学、《What Is Life?》转向遗传学
05  印第安纳：Luria 门下 (1947–1950) — 噬菌体学派、1950 博士（X 射线灭活噬菌体）
06  哥本哈根与那不勒斯 (1950–1951) — Kalckar 实验室不顺、那不勒斯听到 Wilkins 的 DNA 衍射报告
07  卡文迪什：与 Crick 会师 (1951–1953)（核心页）— 剑桥 MRC、第一次错误模型（骨架在内）
08  1953：双螺旋（核心页）— Franklin/Gosling 数据的关键作用（Photo 51、空间群反平行）、1953-04-25 Nature 论文
09  数据归属的暗面 — Franklin 数据三渠道、1954 年致谢原文、后世批评与修正观点并陈
10  1962 诺贝尔奖（核心页）— citation 原文、三人共享、Franklin 1958 逝世无缘提名
11  哈佛与教科书 (1956–1976) — RNA 研究、Gene/Cell/Recombinant DNA 三教科书、1968《双螺旋》出版风波
12  冷泉港与基因组计划 (1968–1992) — CSHL 35 年经营、HGP 首任负责人、反对基因专利与 Healy 冲突辞职
13  晚年争议 — 2007 辞职与 2019 荣衔撤销（一句史实口径）、2014 拍卖奖章与退还
14  遗产的两面 — NYT「20 世纪最重要科学家之一」与种族言论争议并存；分子生物学时代由他开启
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries concerning the molecular structure of nucleic acids and its significance for information transfer in living material"（their 三人共享）；勿写成「因发现 DNA」——DNA 本身并非三人发现 |
| 2 | 种族言论（★ 高压线） | 2007 年言论致 CSHL 停职辞职、2019 年纪录片后 CSHL 撤销全部荣衔并断绝关系——只以一句中性史实口径记载「就种族与智力发表争议言论，遭机构切割」，**禁转述其言论内容**，禁引用其原话 |
| 3 | Franklin 争议 | 数据未经知情同意使用、归因不足、The Double Helix 的「Rosy」刻画受批评——如实呈现；同时并写 Cobb/Comfort「非受害者而是平等贡献者」与 1954 年致谢原文「would have been most unlikely, if not impossible」、晚年通信转善，两面并陈勿单边定性 |
| 4 | 死亡日期 | 1928-04-06 ~ 2025-11-06（享年 97）——2025 年 11 月逝世为 page.md 明载，勿按旧记忆写成在世 |
| 5 | 库内同名 | 分裂 stub「James D. Watson」已归并删除；其父同名 James D. Watson 不入库（防再分裂），父子仅文字叙述 |
| 6 | 师承与学生 | Luria 师生+Delbrück influence；学生入库者 Moore/Schlessinger/Steitz（博士）+Sharp/Roberts（博士后）；Capecchi/Horvitz 他批已建不重复；其余名单不入库 |
| 7 | 引语红线 | 「The luckiest thing...」、基因组 belong to the world's people、Crick 骂书语等均有英文原文可引（用于争议帧须配中文语境说明）；种族言论原话一律禁引 |
| 8 | 诺奖演讲 | 诺奖演讲 1962-12-12；诺奖纪念碑只刻美国人名（不含 Crick/Wilkins）——可作细节帧 |
| 9 | 奖章拍卖 | 2014 年 Christie's 410 万美元拍出、买家 Usmanov 退还——首例在世诺奖得主拍卖奖章，时间线勿错 |
| 10 | metadata 冲突 | occupation 列表含 physicist 等噪声；yaml 主职业 molecular biologist；国籍单值 United States |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| double helix | 双螺旋 | 1953 年模型核心 |
| Photo 51 | 51 号照片 | Franklin/Gosling 的 B 型 DNA 衍射图 |
| antiparallel | 反平行 | 两链方向相反，Franklin 空间群提示 |
| bacteriophage | 噬菌体 | 噬菌体学派的实验系统 |
| Phage Group | 噬菌体学派 | Luria/Delbrück 领袖群体 |
| space group | 空间群 | 晶体学术语 |
| Human Genome Project | 人类基因组计划 | 1988-1992 首任负责人 |
| Cold Spring Harbor Laboratory | 冷泉港实验室 | 1968 起执掌 35 年 |
| The Double Helix | 《双螺旋》 | 1968 畅销回忆录 |
| MRC (Medical Research Council) | 医学研究会 | 英 MRC 实验室体系是数据流通的体制背景 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「海」的辽阔与暗流匹配其人生——从芝加哥湖畔到双螺旋的海量数据，再到晚年言论风暴的深水区
  - 宽广而克制的编曲同时容纳「开启时代」的荣光与「争议缠身」的阴影，符合双面母题
- **备选**（未采用）：Expedition（本批 Wilkins 已用）、The Flow of Time（本批 Eccles 已用）
- **本地路径**：按 music_audio/ 内 Alex-Productions SEA 曲目复制至 `medic/presentations/20th_century/James_Watson/SEA.wav`，ffmpeg `-shortest` 对齐
