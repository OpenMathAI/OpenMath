# 医学家立传提示词（Joshua Lederberg）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1958 年得主 Joshua Lederberg（乔舒亚·莱德伯格）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Joshua_Lederberg/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Joshua Lederberg（1925-05-23 生于新泽西州蒙特克莱 ~ 2008-02-02 逝于纽约，享年 82 岁），美国分子生物学家，ForMemRS，33 岁获诺奖，洛克菲勒大学第五任校长（1978-1990）
- **气质关键词**：**发现细菌"婚配"的人、天体生物学（Exobiology）创词者、DENDRAL 的人工智能先驱**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1958 条目，Lederberg 独得一半；Tatum/Beadle 共享另一半）：
  > "for his discoveries concerning genetic recombination and the organization of the genetic material of bacteria"（因其关于细菌遗传重组与遗传物质组织的发现）
- **设计母题**：**两个细菌之间的基因之桥（bacterial conjugation）**——细菌并非克隆式复制，而能"交配"交换基因；用「两枚杆菌之间细桥连接」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Joshua_Lederberg/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Joshua_Lederberg/`（肖像见 images.txt；与 Esther/Stent/Brenner 1965 合照可作插图）。Makefile 复制后设 `MAIN=Joshua_Lederberg_zh`、`VIDEO_NAME=Joshua_Lederberg_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Lederberg 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microbial genetics | 微生物遗传学（细菌接合/转导） | 1958 诺奖核心 | 核心页 |
| 1 | molecular biology | 分子生物学 | 细菌染色体作图 | 核心页 |
| 2 | exobiology | 天体生物学（Exobiology） | 创词者，与 Sagan 推动 NASA 生物学 | 太空页 |
| 3 | artificial intelligence | 人工智能（DENDRAL） | 与 Feigenbaum 合作化学专家系统 | AI 页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Francis J. Ryan | 对方 → 本科导师 | 哥伦比亚大学，Neurospora 生化遗传研究 |
| advisor-student | Edward Lawrie Tatum | 对方 → 博士导师 | 耶鲁（1947，大肠杆菌遗传重组；合作发现细菌接合） |
| colleague | Edward Lawrie Tatum | 无向 | 1946-1947 耶鲁合作证明 E. coli 可经接合交换遗传信息 |
| co-honored | Edward Lawrie Tatum | 无向 | 1958 诺贝尔生理学或医学奖（Tatum/Beadle 共享一半，Lederberg 独得另一半） |
| co-honored | George Wells Beadle | 无向 | 1958 同届诺奖 |
| influence | Oswald Avery | 无向 | 受其 DNA 发现启发提出细菌重组假说 |
| spouse | Esther Lederberg | 无向 | Esther Miriam Zimmer，1946-1966；细菌遗传学合作者，F 因子发现者，贡献长期未被署名 |
| colleague | Esther Lederberg | 无向 | 实验室长期合作（专化转导 1956、F 因子论文、1956 Pasteur 奖章同获） |
| advisor-student | Norton Zinder | Lederberg → 博士生 | infobox 明载，1951 共同发现转导 |
| spouse | Marguerite Stein Kirsch | 无向 | 精神科医生，1968 结婚，育一女 Anne |
| colleague | Carl Sagan | 无向 | 携手倡导天体生物学，推动 NASA 生物学计划（库内 id=3202） |
| colleague | Edward Feigenbaum | 无向 | 斯坦福合作开发 DENDRAL（库内 id=246） |
| colleague | Frank Macfarlane Burnet | 无向 | 1958 年后斯坦福合作研究病毒抗体 |

**不入库但提示词可叙述**：M. Laurance Morse 与 Luigi Luca Cavalli-Sforza（专化转导/F 因子论文合著者，按择要口径未建边）；Gustav Nossal（自述视 Lederberg 为导师——单方表述不建边）；Gunther Stent、Sydney Brenner（1965 合照友人）。

## 五、配色方案 【人物专属】

- **气质**：培养皿的冷调、星际视野的深邃、跨界的锋利
- **主色**：`#46627F`（菌落灰蓝——细菌培养与太空时代的冷静）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeConj` 细菌接合/转导 — 灰蓝 `#46627F`
  - `badgeSpace` 天体生物学 — 深紫蓝 `#3D3B63`
  - `badgeAI` 人工智能 DENDRAL — 青灰 `#0E7490`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：杆菌接合桥与星轨曲线交错，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 细菌"婚配"的发现者 / Joshua Lederberg 1925–2008 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、蒙特克莱出身、Stuyvesant 15 岁毕业、
    哥伦比亚/耶鲁、威斯康星/斯坦福/洛克菲勒校长任职、诺奖 1958、核心领域）
03  核心贡献概览 — 细菌接合 1946 / 转导 1951 / 专化转导 1956 / DENDRAL 与 Exobiology
04  拉比之子与神童 (1925–1944) — Stuyvesant 15 岁毕业、美国科学院科学实验室、哥伦比亚动物学、
    Ryan 门下 Neurospora、海军医院化验兵
05  Avery 的启发 (1944–1946) — DNA 是转化物质→细菌会交换基因的假说、致信 Tatum
06  耶鲁：接合的证明（核心贡献页）— 1946-47 与 Tatum 证明 E. coli 有"性"、染色体作图、1947 PhD
07  Esther：被遮蔽的合作者 — 1946-12-13 结婚、F 因子发现、专化转导 1956、Pasteur 奖章同获、
    1966 离婚（贡献未被署名的口径，page.md 明载）
08  威斯康星与转导 (1947–1958) — 助理教授、与 Zinder 发现转导 1951、1957 创医学遗传学系、NAS 1957
09  1958 诺奖：33 岁独得一半 — 获奖理由逐字呈现、Tatum/Beadle 共享另一半（结构讲清）
10  斯坦福与星际视野 — 遗传学系创建、与 Burnet 合作病毒抗体、Sputnik 1957 之忧、
    与 Sagan 共倡 Exobiology、飞船消毒与宇航员隔离主张
11  DENDRAL：分子世界的 AI (1960s) — 与 Feigenbaum 的化学专家系统、ACM Fellow
12  洛克菲勒大学校长 (1978–1990) — 第五任校长、退休后名誉教授（分子遗传学与信息学）
13  政府科学顾问与荣誉 — 总统科学顾问委员会、国防科学委员会、NMS 1989、总统自由勋章 2006、
    火星 Lederberg 撞击坑 2012
14  遗产与结尾 — 微生物遗传学+计算机科学+太空生物学的三重奠基 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | **yaml/入库用 manifest 形式 "Joshua Lederberg"**；33 岁获奖是亮点数字 |
| 1958 的"一半"结构 | **Lederberg 独得一半（细菌重组）+ Tatum/Beadle 共享另一半**——勿三人平分；获奖理由是 "for **his** discoveries..."（与前两者 "for their..." 不同句） |
| Esther 口径（★ 重要） | page.md 明载其接合研究"alongside his wife Esther, who was uncredited for her contributions"、F 因子由 Esther 发现、1956 两人同获 Pasteur 奖章——叙述须给足 Esther 地位，spouse+colleague 双边并行；1946 结婚/1966 离婚两个年份勿混 |
| 政治敏感禁写 | ①1986 Sverdlovsk 炭疽事件中 Lederberg 附和苏方"动物传人"说法的两句引语（后被证实为军方泄漏）——**立传中整体回避**，不引用不展开；②海湾战争综合征工作组、总统癌症小组等仅列职衔不展开 |
| 转导归属 | 1951 转导=与博士生 Zinder（Salmonella，噬菌体介导）；1956 专化转导=Morse+Esther+Joshua（lambda 噬菌体）——两条线勿混 |
| Avery 边性质 | "Inspired by Avery's discovery" 是文献启发，建 influence 边但叙述勿写成师承或共事 |
| 双学位口径 | 哥伦比亚 BA 1944（动物学）→ 耶鲁 PhD 1947；**哥伦比亚医学院学业中途放弃（未获 MD）**——选择遗传学而非行医是关键转折，勿写"医学博士" |
| 校长顺位 | 洛克菲勒大学第五任校长（1978-1990），前任 Frederick Seitz、后任 David Baltimore——顺位可写一句 |
| 三个机构连续性 | 威斯康星（1947 助理教授、1957 创医学遗传学系）→ 斯坦福（1958 创遗传学系任主席）→ 洛克菲勒（1978 校长）——三段勿串 |
| 荣誉年份链 | NAS 1957、AAAS 1959、APS 1960、NMS 1989、Benjamin Franklin Medal 2002、总统自由勋章 2006、火星撞击坑命名 2012、ForMemRS——勿串 |
| 引语红线 | 除 Sverdlovsk 两句（禁用）外 page.md 无可用直接引语；Nossal 的 "lightning fast" 是他人评价，可作第三方转述 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| genetic recombination | 遗传重组 | 获奖理由核心词 |
| organization of the genetic material of bacteria | 细菌遗传物质的组织 | 获奖理由另一半 |
| bacterial conjugation | 细菌接合 | 1946-47 与 Tatum 证明 |
| transduction | 转导 | 1951 与 Zinder，噬菌体介导 |
| specialized transduction | 专化转导 | 1956，lambda 噬菌体 |
| fertility factor (F) | 致育因子（F 因子） | Esther 发现 |
| Escherichia coli / Salmonella typhimurium | 大肠杆菌/鼠伤寒沙门氏菌 | 实验材料，斜体 |
| exobiology | 天体生物学（外空生物学） | Lederberg 创的术语 |
| DENDRAL | DENDRAL 专家系统 | 与 Feigenbaum 合作的化学 AI |
| euphenics | 优型学 | 其创词，与优生学相区别（叙述可一笔） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Lederberg 总是在"穿越黑暗"——穿越"细菌只是克隆"的旧共识、穿越从生物学到计算机到太空的学科边界、也穿越妻子 Esther 被历史遮蔽的公案；Through the Darkness 的行进感对应他 22 岁便敢挑战教条、并一路把微生物遗传学带进分子时代与太空时代。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Joshua_Lederberg/ThroughTheDarkness.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
