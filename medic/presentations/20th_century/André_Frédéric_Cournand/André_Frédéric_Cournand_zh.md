# 医学家立传提示词（André Frédéric Cournand）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1956 年得主（安德烈·库尔南，心导管术的发展者之一）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：André Frédéric Cournand（1895-09-24 生于巴黎 ~ 1988-02-19 卒于马萨诸塞州 Great Barrington，享年 92 岁）
- **气质关键词**：**把福斯曼的孤勇变成临床科学的人、Bellevue 医院肺功能实验室的奠基者、法裔美籍的跨洋生理学家** —— 1956 获奖理由（与 Werner Forssmann、Dickinson W. Richards 三人共享）：
  > "for their discoveries concerning heart catheterization and pathological changes in the circulatory system"（因发现心导管术与循环系统的病理变化）
- **设计母题**：**导管的延长线**。1929 年福斯曼把导管插进自己的心脏，1930 年代末起库尔南与理查兹把这根线延展成诊断与研究的仪器。视觉隐喻：一条从手臂静脉出发、终化为心脏病学工具箱的弧线。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/André_Frédéric_Cournand/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/André_Frédéric_Cournand/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/André_Frédéric_Cournand/`（含 `images/`；目录名含 é，Makefile/shell 注意 UTF-8）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=André_Frédéric_Cournand_zh`、`VIDEO_NAME=André_Frédéric_Cournand_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/André_Frédéric_Cournand/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/André_Frédéric_Cournand.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cardiac catheterization | 心导管术 | 发展与应用，1956 诺奖核心 | 核心页 |
| 1 | pulmonary physiology | 肺生理 | 与 Richards 合作的起点 | 核心页 |
| 2 | circulatory physiology | 循环生理 | 创伤性休克与心衰的生理研究 | 研究页（Richards 页合作内容） |
| 3 | respiratory medicine | 呼吸医学 | 呼吸功能检测先驱 | 荣誉页（Kenéz 1975 文题） |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Werner Forssmann | 无向 | 1956 诺贝尔生理学或医学奖三人共享（心导管术与循环系统病理变化） |
| co-honored | Dickinson W. Richards | 无向 | 1956 诺贝尔生理学或医学奖三人共享（心导管术与循环系统病理变化） |
| colleague | Dickinson W. Richards | 无向 | Bellevue 医院长期合作，肺功能研究到心导管术的共同开发 |
| spouse | Beatrice | 无向 | 妻，1993 年以 90 岁去世 |

> **relations=4 为诚实值**——page.md 极简，除两人组与妻子外无其他个人关系记载，Review 勿误判缺漏。
> 不入库：世界文化理事会（1981 创始成员，机构）；各荣誉学位大学；References 中引文作者。
> 库内当时无 Werner Forssmann / Dickinson W. Richards / Beatrice 记录，均由本 yaml 新建 stub（Cournand/Forssmann/Richards 三人互为 co-honored+colleague，由三份 yaml 共同幂等覆盖）。

## 五、配色方案 【人物专属】

- **气质**：塞纳河的雅致灰蓝 + Bellevue 病房的务实 + 跨洋职业生涯的纵深
- **主色**：塞纳灰蓝 `#37548D`（法裔底色与临床科学的冷静）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 心导管术 — 塞纳灰蓝 `#37548D`
  - `badgeB` 肺生理 — 深青 `#0E7C7B`
  - `badgeC` 循环病理 — 暗红 `#8C2F1B`
  - `badgeD` 荣誉与国际承认 — 琥珀 `#A0722D`
- **背景母题**：一条从左下蜿蜒至右上的导管弧线（巴黎→纽约），badge 沿弧分布。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 心导管术的发展者 / André Frédéric Cournand 1895–1988 + 四色 badge + 右上头像 + 国籍行 France/USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生巴黎、教育巴黎大学、
    1930 移美/1941 入籍、任职哥伦比亚大学内外科医学院/Bellevue 医院、
    荣誉 Nobel 1956/Lasker 1949、核心领域）
03  核心贡献概览 — 心导管术的临床化 / 肺功能研究 / 循环病理刻画 / 国际学术承认
04  巴黎岁月与移美 (1895–1930) — 巴黎出生、巴黎大学受训、1930 移居美国
05  入籍与哥伦比亚 (1930–1941) — 1941 归化入籍、
    哥伦比亚大学内外科医学院教授、Bellevue 医院执业
06  与 Richards 的相遇与合作 — Richards 1928 起转肺与循环生理研究、
    二人在 Bellevue 医院就肺功能开展合作——从肺病患者的肺功能方法起步
07  从肺到心：导管的临床化 — 接续 Forssmann 1929 的自体实验、
    把导管术发展为心脏疾病诊断与研究工具（三人组的"接力"结构）
08  1956 诺贝尔奖 — 三人共享官方理由逐字引用、
   此前 1949 Albert Lasker 基础医学研究奖为前奏
09  循环病理的刻画 — 创伤性休克研究、心衰生理、心脏药物效应测量、
    慢性心脏病与肺病功能障碍各型及治疗、先天性心脏病诊断技术
    （以 Richards 页合作内容为共同叙事，注明）
10  荣誉编年 — Retzius 银章 1946、Lasker 1949、John Phillips 奖 1952、
    比利时皇家医学院与巴黎国家医学院金章 1956
11  荣誉学位与世界文化理事会 — Strasbourg 1957/Lyon 1958/Brussels 1959/Pisa 1961
    荣誉博士、Birmingham D.Sc. 1961、1981 世界文化理事会创始成员
12  个人生活 — 妻 Beatrice（1993 年以 90 岁去世）
13  学术传承 — 呼吸功能检测先驱（Kenéz 1975 文题口径）、
    Trudeau 奖章 1971（Am Rev Respir Dis 载）、心肺生理学的 Bellevue 学派
14  遗产 — 心导管术从"自杀式设想"到现代心脏病学基石、
    介入心脏病学的源头（Forssmann-Gruentzig 谱系）、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries concerning heart catheterization and pathological changes in the circulatory system"（三人共享、their）；page.md 简写"for the development of cardiac catheterization"——引用以 citation json 为准 |
| 三人分工 | Forssmann 首创自体实验、Cournand+Richards 发展临床应用并刻画循环病理——本篇以"发展者"定位，勿写成"发明心导管术" |
| 国籍裁定 ★ | manifest 仅 United States；citation json 官方口径 **"France United States"**；page.md metadata 双列——yaml 取 France(0)+United States(1)（官方顺序），幻灯片国籍行 France/USA，供主控统一口径 |
| 页面极简 | page.md 仅传记一段+荣誉清单——**宁少勿造**：无师承、无博士生、无早期生平细节（勿从 Nobel 官网传记补写建边）；relations=4 诚实值 |
| 妻子姓名 | page.md 仅载 "His widow Beatrice"（无姓）——yaml 存 'Beatrice'，幻灯片照实，勿杜撰全名 |
| Richards 页借力 | 循环病理细节（休克/心衰/药物效应/先心诊断）载于 Richards 页合作段落——本篇以"合作内容"口径引用，注明共同工作 |
| 目录名含 é | {Dir}=André_Frédéric_Cournand——Makefile/shell 引用注意 UTF-8；tex 中 é 原生支持 |
| Trudeau 奖 | 1971 年 Trudeau 奖章信息来自 References 的 Riley 1971 文（页面正文未展开）——可写但标注来源属性 |
| 荣誉学位清单 | Strasbourg(1957)/Lyon(1958)/Brussels(1959)/Pisa(1961)/Birmingham D.Sc.(1961)——年份勿错位 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| cardiac catheterization | 心导管术 | 1956 诺奖核心 |
| circulatory system | 循环系统 | 理由句第二半 |
| pulmonary function | 肺功能 | 与 Richards 合作的起点 |
| traumatic shock | 创伤性休克 | 导管术研究的应用对象 |
| congenital heart disease | 先天性心脏病 | 诊断技术贡献 |
| Bellevue Hospital | 贝尔维尤医院 | 合作现场 |
| honoris causa | 荣誉博士 | 多校荣誉的拉丁语口径 |
| World Cultural Council | 世界文化理事会 | 1981 创始成员 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Ascension**（manifest 预分配）
- **风格**：攀升 / 大气 / 庄严
- **匹配理由**：从巴黎到纽约、从肺功能到心脏导管——Ascension 的攀升感匹配"把一根细导管送入心脏、再送入现代医学核心"的上升叙事，也呼应其横跨两国、横跨半个世纪的学术生涯。
- **本地路径**：`music_audio/` 下 Ascension 对应文件（执行时以 `find music_audio -iname "*Ascension*"` 实际定位）→ 复制为 `presentations/20th_century/André_Frédéric_Cournand/Ascension.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；三人分工与"发展者"定位务必精确。**
