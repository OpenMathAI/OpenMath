# 医学家立传提示词（Severo Ochoa）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1959 年得主（与 Kornberg 共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Severo Ochoa de Albornoz（1905-09-24 生于西班牙 Luarca ~ 1993-11-01 逝于马德里，享年 88 岁）
- **气质关键词**：**RNA/DNA 生物合成机制的共同发现者、从西班牙内战流亡到纽约的生化巨匠** —— 1959 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Arthur Kornberg 共享同一句）：
  > "for their discovery of the mechanisms in the biological synthesis of ribonucleic acid and deoxyribonucleic acid"
  > （因他们发现了核糖核酸与脱氧核糖核酸生物合成的机制）
- **设计母题**：**酶反应之涡（the enzyme vortex）**。多核苷酸磷酸化酶把核苷二磷酸聚成长链、试管中"无中生有"的 RNA——"在玻璃器皿里重演生命的书写"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Severo_Ochoa/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Severo_Ochoa/page.md`；目录 `medic/presentations/20th_century/Severo_Ochoa/`；Makefile 改 `MAIN=Severo_Ochoa_zh`；肖像优先 images.txt 所列 Commons 图（Ochoa in 1958、与妻 1959 瑞典照），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Severo_Ochoa.yaml` 一致，勿重复入库；库内既有 stub id=4291 已 UPD 回填）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 职业主领域（infobox Fields） | 封面 |
| 1 | molecular biology | 分子生物学 | RNA/DNA 合成机制 | 诺奖页 |
| 2 | enzymology | 酶学 | 甘油醛酶起步、终身志业 | 早年页 |
| 3 | intermediary metabolism | 中间代谢 | 伦敦期糖酵解与柠檬酸循环研究 | 研究页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Otto Fritz Meyerhof | 师→本人 | 柏林凯撒威廉生物研究所入门（1929，诺奖得主） |
| influence | Juan Negrín | 无向 | 马德里医学院老师，引其读外语科学专著（page.md 有原话可引） |
| influence | Henry Hallett Dale | 无向 | 伦敦国家医学研究所博士后东家（1931，糖酵解酶起步） |
| co-honored | Arthur Kornberg | 无向 | 1959 诺贝尔生理学或医学奖共享（RNA 与 DNA 生物合成机制） |
| spouse | Carmen García Cobián | 无向 | 1931 结婚，无子女，1986 先逝 |

> 对手方规范名：`Arthur Kornberg` 沿用库内记录（id=3780，其批次已写 co-honored 镜像边，幂等合并）；Meyerhof/Negrín/Dale/Carmen 按 page.md 形式新建（Dale 用库内既有 Henry Hallett Dale id=3588 复用）。**库内另存 Irwin Rose→Ochoa colleague 边（乙酸盐激酶合作，他批写入）与 Kornberg→Ochoa advisor-student 边（11320，他批口径），本篇不重复不删改。**

## 五、配色方案

- **气质**：阿斯图里亚斯的乡愁 + 战火中的流亡 + 纽约实验室的丰产
- **主色**：大西洋蓝 `#17566B`（比斯开湾与跨洋流亡）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` RNA 合成 — 核苷橙 `#C97B2D`
  - `badgeB` 酶学与中间代谢 — 酶青 `#2E7D8C`
  - `badgeC` 西班牙岁月 — 故土红 `#9E2B25`
  - `badgeD` NYU 建制 — 紫罗兰 `#5E4B8B`
- **背景母题**：低透明度酶-底物涡旋与核苷酸链生长线。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — RNA/DNA 生物合成机制的共同发现者 / Severo Ochoa 1905–1993 + badge + 右上头像 + 国籍行（United States，生于西班牙）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Luarca、马德里医学院 MD 1930、Meyerhof 门下、NYU 教授、诺奖 1959）
03  核心贡献概览 — 多核苷酸磷酸化酶 / RNA 体外合成 / 柠檬酸循环 / 蛋白合成与 RNA 病毒
04  卢阿尔卡与马德里 (1905–1929) — 七岁丧父随母迁马拉加、Cajal 著作点燃生物学兴趣（慕 Cajal 而来其已退休）、师从 Arrupe 与 Negrín、肌酸酐测定首篇论文
05  柏林：Meyerhof 门下 (1929–1930) — 凯撒威廉生物研究所的生化"温床"、Warburg/Neuberg/Lundsgaard/Lipmann 群星之间
06  伦敦与流亡 (1931–1941) — Dale 门下乙二醛酶研究（酶学起点）、内战爆发弃"永久性摧毁科研生涯"的环境、"漂泊岁月"：德国→英国→美国
07  纽约定居 (1942–1956) — NYU 医学研究员→助理教授 1945→药理学教授 1946→生物化学教授 1954→系主任；1956 入籍美国
08  1955：多核苷酸磷酸化酶 — 体外合成 RNA 的发现（诺奖核心）；1957 NAS/美国艺术与科学院双院士
09  1959 诺贝尔奖 — 与 Kornberg 共享（Kornberg=DNA 聚合酶线、Ochoa=RNA 合成线）；官方理由全句
10  荣誉 — Paul Karrer 金质奖章 1963、美国国家科学奖章 1979、阿斯图里亚斯金质奖章、英国皇家学会外籍院士
11  晚年与回归 (1961–1993) — 美国哲学学会 1961、持续研究蛋白合成与 RNA 病毒复制至 1985、回民主西班牙任科学顾问、CBM 中心以其命名
12  家庭与身后 — 妻 Carmen García Cobián（1931 结婚、无子女、1986 先逝）；1993-11-01 逝于马德里
13  纪念 — 马德里自治大学 CBM 更名 Severo Ochoa 中心、医院与地铁站命名、小行星 117435 Severochoa、2003 西班牙邮票与 2011 美国科学家邮票
14  遗产：从试管 RNA 到分子生物学时代 — 体外合成核酸为遗传密码破译铺路
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1959 两人共享同一句理由；分工：Ochoa=RNA 合成（多核苷酸磷酸化酶）、Kornberg=DNA 合成（DNA 聚合酶）——勿混写；citation json 为 RNA+DNA 全句 |
| 双导师口径 | infobox Academic advisors 含 Arrupe/Negrín/Meyerhof/Dale 四人，但性质各异：仅 **Meyerhof** 系正规 research 门徒（1929 邀请入门）；Arrupe 系医学院同学式"studied with"（裁定不入库）；Negrín/Dale 分别为 teacher/postdoc 东家——入库用 influence |
| Cajal | 仅"著作激发兴趣"、从未谋面（报到时已退休）——不入库，正文可一句 |
| 多核苷酸磷酸化酶 | 页面只写"发现 RNA/DNA 生物合成机制"与诺奖理由；酶的后续评价（如生理意义争议）page.md 无载，**禁展开** |
| 国籍 | citation json "Spain United States"、页面 Citizenship: Spanish 1905-56 / American 1956-93——yaml 按 US(0)+Spain(1)，正文写"西班牙裔美国生物化学家" |
| Sara Montiel 轶闻 | 演员 Sara Montiel 在其身后自述 1950s 恋情系孤证转述——**禁写**（涉私德且无对证） |
| 无子女 | 与妻无子女（page.md 明载），家庭页勿虚构 |
| Kornberg 库内边 | 库内已有 Kornberg 批次写的 co-honored 镜像边与 Kornberg→Ochoa advisor-student 边（note 口径与他批），本篇不删改——Review 若裁口径冲突由主控处理 |
| 引语红线 | Negrín 段有英文原话（"Negrin opened wide, fascinating vistas..."）可引节选；"wander years"/"one could see muscles twitching" 亦实载可引；其余转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| polynucleotide phosphorylase | 多核苷酸磷酸化酶 | 1955 年发现（页面以诺奖理由表述为准） |
| in vitro synthesis | 体外合成 | 玻璃器皿中聚合核酸 |
| intermediary metabolism | 中间代谢 | 伦敦期研究主线 |
| glyoxalase | 乙二醛酶 | Dale 实验室课题 |
| citric acid cycle | 柠檬酸循环 | NYU 期贡献之一 |
| Kaiser Wilhelm Institute | 凯撒威廉研究所 | 柏林-达勒姆/海德堡 |
| wander years | 漂泊岁月 | 1936-1940 流亡期 |
| ForMemRS | 英国皇家学会外籍院士 | Ochoa 头衔之一 |

## 九、背景音乐选择

- **选定曲目**：**Timeless** — Alex-Productions（manifest 预分配）
- **匹配理由**："长期纲领/沉稳"贴合其横跨两国、贯穿生化黄金时代的漫长科学生涯——从马德里课堂到纽约试管，RNA 合成的发现是永恒性的奠基；沉稳曲式承载流亡者的坚韧。
- **本地路径**：music_audio/ 下 Alex-Productions Timeless 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
