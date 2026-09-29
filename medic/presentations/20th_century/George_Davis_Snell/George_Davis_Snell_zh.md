# 医学家立传提示词（George D. Snell）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1980 年得主（乔治·斯内尔，小鼠 H-2 复合体的发现者、移植免疫学的奠基人）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：George Davis Snell（1903-12-19 生于马萨诸塞州 Bradford ~ 1996-06-06 卒于缅因州 Bar Harbor，享年 92 岁）
- **气质关键词**：**H 抗原概念的提出者、小鼠 H-2 复合体的发现者、Jackson Laboratory 一生只换过一次工作的.mouse geneticist** —— 1980 获奖理由（与 Baruj Benacerraf、Jean Dausset 三人共享）：
  > "for their discoveries concerning genetically determined structures on the cell surface that regulate immunological reactions"（因发现细胞表面调控免疫反应的遗传决定结构）
- **设计母题**：**小鼠背上的免疫地图**。H-2 复合体在小鼠中的发现，映射到人类的 HLA——"动物模型里的答案写给全人类"。视觉隐喻：小鼠剪影上的发光基因位点，延展为人类的 HLA 图谱。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/George_Davis_Snell/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/George_Davis_Snell/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/George_Davis_Snell/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=George_Davis_Snell_zh`、`VIDEO_NAME=George_Davis_Snell_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/George_Davis_Snell/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/George_Davis_Snell.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | genetics | 遗传学 | H-2 复合体发现，1980 诺奖核心 | 核心页 |
| 1 | immunology | 免疫学 | 移植免疫与 H 抗原概念 | 核心页 |
| 2 | mouse genetics | 小鼠遗传学 | Jackson Laboratory 终身研究 | 身份页 |
| 3 | histocompatibility | 组织相容性 | 移植可能性的遗传因子 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Baruj Benacerraf | 无向 | 1980 诺贝尔生理学或医学奖三人共享（细胞表面遗传决定结构调控免疫反应的发现） |
| co-honored | Jean Dausset | 无向 | 1980 诺贝尔生理学或医学奖三人共享（细胞表面遗传决定结构调控免疫反应的发现） |
| advisor-student | William E. Castle | 导师 | 哈佛博士导师（1930，小鼠遗传连锁），首位在哺乳动物中寻找孟德尔遗传的美国生物学家 |
| advisor-student | Hermann Joseph Muller | 导师 | 德克萨斯大学博士后两年（X 射线对小鼠的遗传效应，1946 诺奖得主） |
| spouse | Rhoda Carson | 无向 | Bar Harbor 结婚，育三子女，1994 年去世 |

> relations=5 为诚实值，Review 勿误判缺漏。
> 不入库：John Gerould（Dartmouth 遗传学教授，推荐读研者——事件性）；C.C. Little（Jackson Laboratory 创始人、Castle 早期学生，机构语境）；Peter Alfred Gorer 与 Leroy Stevens（See also 列举，无正文关系）；父亲（YMCA 秘书/发明线圈绕制装置，背景叙事）；三名子女未具名。
> 库内已有 George D. Snell stub（#5884，并行 1980 三人组 agent 预建），本 yaml UPD 回填 Q295666；Castle/Muller 新建 stub（Muller 用 page.md 缩写形式 H.J. Muller，即赫尔曼·穆勒 1946 诺奖得主）。

## 五、配色方案 【人物专属】

- **气质**：缅因海岸的冷杉绿 + 小鼠遗传学的素净 + 92 岁一生的沉静
- **主色**：冷杉绿 `#175E54`（Bar Harbor 森林与 Jackson Laboratory 的底色）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` H-2 复合体 — 冷杉绿 `#175E54`
  - `badgeB` Castle/Muller 师承 — 琥珀 `#A0722D`
  - `badgeC` 移植免疫 — 暗红 `#8C2F1B`
  - `badgeD` 伦理学著作 — 灰紫 `#5C5470`
- **背景母题**：小鼠剪影上的发光位点（H-2 基因座）延展为人类 HLA 图谱的虚线。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 移植免疫学的奠基人 / George D. Snell 1903–1996 + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Bradford、教育 Dartmouth BS 1926/
    哈佛 DSc 1930（Castle 门下）、德州 Muller 门下博后、
    任职 Brown/Washington Univ./Jackson Laboratory（1935-1996）、
    荣誉 Nobel 1980/Wolf 1978/Gairdner 1976、核心领域）
03  核心贡献概览 — H 抗原概念 / H-2 复合体 / 移植可能性的遗传因子 / 小鼠遗传学的世界重镇
04  Bradford 与 Dartmouth (1903–1926) — 三子最幼、父为 YMCA 秘书兼业余发明者、
    Brookline 学校、Dartmouth 数学与科学（遗传学方向）、1926 BS
05  哈佛：Castle 门下 (1926–1930) — 遗传学教授 Gerould 推荐、
    随 William E. Castle（首位在哺乳动物中寻找孟德尔遗传的美国生物学家）读博、
    1930 PhD 论文：小鼠的遗传连锁
06  Muller 门下与转向 (1930–1935) — Brown 大学教师（1930-31）、
    德克萨斯大学 H.J. Muller（辐射遗传学先驱，1946 诺奖）门下博后两年、
    X 射线对小鼠的遗传效应研究——自述"研究才是我真正的热爱"（自传引语可引）、
    1933-34 圣路易斯华盛顿大学任教、1935 入 Jackson Laboratory
07  Jackson Laboratory 的 H-2 — Bar Harbor 的"小鼠遗传学麦加"、
    发现决定个体间组织移植可能性的遗传因子、提出 H 抗原概念、H-2 复合体
08  从小鼠到人类 — 小鼠 H-2 与人类（及所有脊椎动物）HLA 的同源对应、
    这些关键基因的确认是组织与器官移植成功的前提
09  1980 诺贝尔奖 — 三人共享官方理由逐字引用、
    1978 Wolf 医学奖/Coley 奖/Gairdner 1976 为前奏、Nobel Lecture "Studies in Histocompatibility"
10  荣誉序列 — AAAS 1952/Hekteon Medal 1955/Mendel Medal 1967/NAS 1970/法国科学院外籍院士 1979、
    美国哲学会 1982、世界文化理事会创始成员 1981、英国移植学会/英国免疫学会荣誉会员
11  1988：伦理学著作 — 《Search for a Rational Ethic》：
    以演化为基础、他相信适用于全人类的伦理规则——科学家的人文面向
12  个人生活 — Bar Harbor 与 Rhoda Carson 结婚、三子女、
    滑雪（Dartmouth 起的爱好）与网球、1996-06-06 卒于 Bar Harbor（92 岁）、妻 1994 先逝
13  学术年表 — 1935-68 Jackson staff scientist、1968-96 senior staff scientist emeritus、
    一所实验室工作终身的样本
14  遗产 — 移植配型从艺术变为科学、H-2 到 HLA 的跨物种对应、
    小鼠遗传学的世纪重镇、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries concerning genetically determined structures on the cell surface that regulate immunological reactions"（三人共享、their） |
| Snell 专属贡献 | "发现了决定个体间组织移植可能性的遗传因子，并提出 H 抗原概念"（page.md 引 Nobel 表述）——小鼠 H-2 → 人类 HLA 的对应关系是三人组的桥梁 |
| 页面极简 ★ | page.md 无 Research 独立章节（Work 一段）——宁少勿造；relations=5 诚实值 |
| 双导师 | Castle（哈佛博士导师，1930 遗传连锁论文）+ H.J. Muller（德克萨斯博后两年，辐射遗传学）——两条 advisor-student 边 note 区分学位/博后阶段；Muller 系 1946 诺奖得主 |
| Muller 姓名形式 | page.md 用缩写 "H.J. Muller"（Hermann Joseph Muller）——yaml 采用 page.md 缩写形式，若其他批次用全名需主控统一 |
| Castle 定位 | "first American biologist to look for Mendelian inheritance in mammals"（page.md 明载 first）——师承亮点 |
| Jackson Laboratory | 1935 入职、1935-68 staff scientist、1968-96 emeritus——**一所实验室工作终身**的样本；自传引语（"research was my real love..."）可引 |
| 兄弟姐妹 | 三子最幼——兄姐未具名不入库 |
| 父亲 | YMCA 秘书、发明汽艇引擎感应线圈绕制装置——背景趣味一句 |
| 伦理学著作 | 1988《Search for a Rational Ethic》——演化基础的伦理学， Nobel 得主的人文面向，勿漏 |
| 在世者规则 | 本篇主角 1996 年逝；妻 Rhoda 1994 先逝（page.md 口径） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| H-2 complex | H-2 复合体 | 小鼠主要组织相容性复合体 |
| H antigens | H 抗原 | Snell 提出的概念 |
| HLA | 人类白细胞抗原 | 人类对应系统 |
| histocompatibility | 组织相容性 | 移植成败的关键 |
| genetic linkage | 遗传连锁 | 博士论文主题 |
| Jackson Laboratory | 杰克逊实验室 | 小鼠遗传学"麦加" |
| radiation genetics | 辐射遗传学 | Muller 门下方向 |
| Search for a Rational Ethic | 《寻找一种理性的伦理》 | 1988 著作 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia**（manifest 预分配）
- **风格**：回望 / 温情 / 坚韧
- **匹配理由**：从 1930 年的遗传连锁论文到 1996 年的生命终点，同一座海滨实验室守望一甲子——Nostalgia 的回望气质匹配"一生一事"的沉静坚守；92 年人生横跨孟德尔遗传学的验证时代到 HLA 的临床应用，本身就是一部回望之书。
- **本地路径**：`music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` → 复制为 `presentations/20th_century/George_Davis_Snell/Nostalgia.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；双导师阶段区分与"一所实验室终身"主线务必保留。**
