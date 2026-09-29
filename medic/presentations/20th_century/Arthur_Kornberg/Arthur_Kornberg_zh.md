# 医学家立传提示词（Arthur Kornberg）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1959 年得主 Arthur Kornberg（阿瑟·科恩伯格）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Arthur_Kornberg/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Arthur Kornberg（1918-03-03 生于纽约布鲁克林 ~ 2007-10-26 逝于斯坦福，享年 89 岁，呼吸衰竭），美国生物化学家，DNA 聚合酶 I 的分离者
- **气质关键词**：**在试管里合成 DNA 的人、酶学的苦行僧、Kornberg 学派的族长**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1959 条目，Kornberg/Ochoa 共享）：
  > "for their discovery of the mechanisms in the biological synthesis of ribonucleic acid and deoxyribonucleic acid"（因其发现 RNA 与 DNA 生物合成的机制）
- **设计母题**：**试管里长出的 DNA 链（DNA polymerase I → enzymatic synthesis）**；用「试管中渐次延伸的双螺旋」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Arthur_Kornberg/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Arthur_Kornberg/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Arthur_Kornberg_zh`、`VIDEO_NAME=Arthur_Kornberg_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Kornberg 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | infobox primary；1959 诺奖学科 | 全篇 |
| 1 | enzymology | 酶学 | 酶纯化技术起家、Pfizer 酶化学奖 1951 | 核心页 |
| 2 | DNA replication | DNA 复制（DNA 聚合酶 I） | 1956 分离首个 DNA 聚合酶，1959 诺奖 | 核心页 |
| 3 | molecular biology | 分子生物学 | infobox Fields；ATP/NAD 代谢起步 | 职业页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Severo Ochoa | 对方 → 导师 | 1946 年转入其纽约大学实验室学习酶纯化技术（库内 #4291，1959 共享诺奖对手方） |
| advisor-student | Carl Ferdinand Cori | 对方 → 导师 | 1947 年华盛顿大学其实验室研修（frontmatter doctoral_advisor 明载） |
| advisor-student | Gerty Cori | 对方 → 导师 | 1947 年华盛顿大学 Cori 夫妇实验室研修 |
| co-honored | Severo Ochoa | 无向 | 1959 诺贝尔生理学或医学奖共享（RNA 与 DNA 生物合成的机制） |
| spouse | Sylvy Kornberg | 无向 | Sylvy Ruth Levy，生物化学家，DNA 聚合酶发现的重要贡献者（1943-1986；库内 #4322） |
| spouse | Charlene Walsh Levering | 无向 | 第二任妻子（1988-1995，先逝） |
| spouse | Carolyn Frey Dixon | 无向 | 第三任妻子（1998-2007） |
| parent-child | Roger D. Kornberg | 长子 | 2006 诺贝尔化学奖得主（父子双诺奖；库内 #4321） |
| parent-child | Thomas B. Kornberg | 次子 | 1970 年发现 DNA 聚合酶 II 与 III |
| parent-child | Kenneth Andrew Kornberg | 三子 | 生物医学实验室建筑师 |
| advisor-student | Randy Schekman | Kornberg → 博士生 | infobox 明载，2013 诺贝尔生理学或医学奖得主 |
| advisor-student | James Spudich | Kornberg → 博士生 | infobox Doctoral students 明载 |
| advisor-student | Tania A. Baker | Kornberg → 博士生 | infobox 明载，《DNA Replication》第二版合著者 |
| advisor-student | I. Robert Lehman | Kornberg → 思想之子 | "Kornberg school" 名单明载 |
| advisor-student | Charles C. Richardson | Kornberg → 思想之子 | "Kornberg school" 名单明载 |
| advisor-student | William T. Wickner | Kornberg → 思想之子 | "Kornberg school" 名单明载 |
| advisor-student | James Rothman | Kornberg → 思想之子 | "Kornberg school" 名单明载，2013 诺奖得主 |
| advisor-student | Arturo Falaschi | Kornberg → 思想之子 | "Kornberg school" 名单明载 |
| advisor-student | Ken-ichi Arai | Kornberg → 思想之子 | "Kornberg school" 名单明载 |

**不入库但提示词可叙述**：Rolla Dyer（NIH 院长因其论文邀其入 NIH——招募事件非师承）；Horace Barker（1951 伯克利访问实验室——访问非师承）；父母 Joseph 与 Lena（奥属加利西亚移民，亲子边不建）；祖父改姓 Queller→Kornberg 的家族轶事。

## 五、配色方案 【人物专属】

- **气质**：试管中的分子冷光、酶结晶的严谨、斯坦福的沙金色
- **主色**：`#8C2F1B`（深砖红——DNA 双螺旋的经典配色与酶液的暖光）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgePoly` DNA 聚合酶 — 深砖红 `#8C2F1B`
  - `badgeEnz` 酶学 — 深蓝 `#1E4E79`
  - `badgeSynth` 体外合成 — 青灰 `#0E7490`
  - `badgeSchool` Kornberg 学派 — 琥珀 `#B07D2B`
- **背景母题**：试管中渐次延伸的双螺旋与酶分子剪影，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 在试管里合成 DNA 的人 / Arthur Kornberg 1918–2007 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、布鲁克林出身、纽约城市学院/罗切斯特大学 MD、
    NIH/华盛顿大学/斯坦福任职、诺奖 1959、核心领域）
03  核心贡献概览 — ATP/NAD 代谢 / DNA 聚合酶 I 1956 / 体外酶促 DNA 合成 / 孢子研究
04  移民之家与杂货店 (1918–1941) — 加利西亚移民、九岁站柜台、CCNY 1937、罗切斯特 MD 1941、
    第一篇论文：吉尔伯特综合征自查
05  军医与 NIH (1941–1946) — 海岸警卫队船医、Dyer 院长邀入 NIH、大鼠营养实验的枯燥
06  Ochoa 实验室的酶学启蒙 (1946–1953) — 纽约大学学酶纯化、哥大暑期补化学、NIH 酶与代谢室主任、
    1947 华盛顿大学 Cori 夫妇实验室
07  1956：DNA 聚合酶 I（核心贡献页）— 华盛顿大学微生物系主任任上分离首个 DNA 聚合酶、
    体外酶促合成 DNA
08  Sylvy：被"抢劫"的合作者 — 1943 结婚、共同贡献聚合酶发现、"I was robbed!" 家族玩笑（page.md 明载）
09  1959 诺奖：与 Ochoa 共享 — 获奖理由逐字呈现（RNA 与 DNA 生物合成的机制）
10  斯坦福生化系 (1959– ) — 系执行主席、1997 访谈忆为 Lederberg 另建遗传学系（引语 page.md 明载）
11  孢子：母亲的病与一生的执念 — 1939 年母亲产褥气性坏疽离世→孢子研究（1962-1970，冷门但倾注半力）
12  Kornberg 学派（核心页）— "思想之子"谱系：Schekman/Rothman（2013 诺奖）、Lehman、Richardson 等
13  荣誉与认可 — Pfizer 酶化学奖 1951、NAS 1957、Nobel 1959、NMS 1979、Gairdner 1995、
    罗切斯特 Kornberg 医学研究所大楼 1999
14  遗产与结尾 — 著作等身（DNA Replication 教科书）、八十岁仍全职实验、多聚磷酸代谢收官 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | **yaml/入库用 manifest 形式 "Arthur Kornberg"**；库内既有 stub #3780 已 UPD 回填 Q295678 |
| 无 PhD | 学位是 CCNY BS 1937 + 罗切斯特 **MD 1941**——医学博士出身转基础研究，勿写"博士（PhD）"；frontmatter doctoral_advisor（Ochoa/Cori）实为博士后/研修导师性质，yaml note 已按"实验室研修/学习酶纯化技术"表述 |
| 与 Ochoa 双边 | advisor-student（1946 纽约大学）+ co-honored（1959）两条边并行勿合并；Ochoa 用库内记录 #4291（其 qid 由 med-batch-16 回填） |
| Sylvy 口径（★ 重要） | page.md 明载 Sylvy "worked closely with Kornberg and contributed significantly to the discovery of DNA polymerase"、家族玩笑 "I was robbed!"——叙述给足其贡献；三个儿子 Roger（2006 化学诺奖）/Thomas（聚合酶 II/III）/Kenneth（建筑师）以 parent-child 边呈现 |
| Cori 夫妇双导师 | 1947 华盛顿大学在 Carl Ferdinand Cori **与 Gerty Cori** 实验室研修——两条 advisor-student 边并行，勿只写 Carl |
| Kornberg school 口径 | "intellectual children include..."七人名单 page.md 明载——全部入库为思想之子；Schekman/Rothman 后获 2013 诺奖可点一句 |
| Lederberg 引语 | 1997 访谈："Lederberg really wanted to join my department... I was instrumental in establishing a department of genetics [at Stanford] of which he would be chairman."——page.md 明载英文原话可引；亦解释 1958 年斯坦福遗传学系由来 |
| 孢子研究叙事 | 1939 年母亲死于常规胆囊手术后气性坏疽（孢子感染）→一生孢子情结、1962-1970 倾注半力后放弃——动机链 page.md 明载，可作情感主线 |
| 体外合成表述 | "enzymatic synthesis of DNA" 是酶促体外合成——勿写成"人工创造生命"或"合成第一个基因" |
| 荣誉年份链 | Pfizer(Paul-Lewis) 酶化学奖 1951、NAS 1957、Nobel 1959、APS 1960、NMS 1979、Golden Plate 1991、Gairdner 1995、罗切斯特大楼 1999——勿串 |
| 职年链 | NIH 1942-45 营养组 →Ochoa 实验室 1946 → NIH 酶与代谢室主任 1947-53（其间 1947 华盛顿大学 Cori 实验室、1951 伯克利 Barker 实验室）→ 华盛顿大学微生物系教授主任 1953-59 → 斯坦福生化系 1959 直至逝世——勿串 |
| 死因 | 2007-10-26 逝于斯坦福医院，呼吸衰竭，89 岁；八十多岁仍全职研究（多聚磷酸代谢）——"在岗到最后"是结尾页素材 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| biological synthesis of RNA and DNA | RNA 与 DNA 的生物合成 | 获奖理由逐字对应 |
| DNA polymerase I | DNA 聚合酶 I | 1956 年分离的首个 DNA 聚合酶（原称 Kornberg enzyme） |
| DNA replication | DNA 复制 | 其核心领域 |
| enzymatic synthesis | 酶促（体外）合成 | 试管中合成 DNA 的口径 |
| enzyme purification | 酶纯化 | 在 Ochoa 实验室所学技术 |
| ATP / NAD / NADP | 腺苷三磷酸/烟酰胺辅酶 | NIH 时期代谢研究对象 |
| spore | 孢子 | 母亲之死引出的一生课题 |
| inorganic polyphosphate | 无机多聚磷酸 | 晚年研究主题 |
| Kornberg school | Kornberg 学派 | "思想之子/思想之孙"的传承谱系 |
| Gilbert's syndrome | 吉尔伯特综合征 | 其第一篇论文的自查主题 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Empire Collapse**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Kornberg 的诺奖宣告了一个"旧帝国"的终结——生命化学不再神秘不可合成；曲名的宏大与苍凉对应他从移民杂货店到分子生物学帝国的跨越，也对应这位学派族长 89 岁仍在实验室坚守、直到帝国基业交到第三代（Roger 2006、Schekman/Rothman 2013 双诺奖）手中的传承终章。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Arthur_Kornberg/EmpireCollapse.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
