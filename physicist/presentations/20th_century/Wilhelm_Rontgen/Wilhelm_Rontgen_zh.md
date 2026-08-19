# 威廉·康拉德·伦琴 (Wilhelm Conrad Röntgen) 立传提示词

> 本提示词严格遵循 `physicist` 项目的人物立传规范（`Physicist_Bio_Prompt_Template.md`），并参照物理学家侧标杆实例 `Kenneth_G_Wilson_zh.md` 与首例 `Eugene_Wigner_zh.md` 的结构（含「研究领域」与「社会关系 + 数据库入库」两章），为伦琴制作 Beamer 演示文稿。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息 【人物专属】

- **目标物理学家**: Wilhelm Conrad Röntgen（威廉·康拉德·伦琴，1845-03-27 ~ 1923-02-10，享年 77 岁）
- **气质关键词**: **X 射线的发现者、实验物理的静默大师、医学成像的开启者** — "因发现后来以他的名字命名的非凡射线所作出的杰出贡献"（1901 诺贝尔物理学奖获奖理由，史上首位诺贝尔物理学奖得主）
- **本地 Wikipedia**:
  - 权威数据源：`physicist/presentations/pages/20th_century/Wilhelm_Conrad_Röntgen/page.md`（已含完整 infobox + 正文）
  - 立传目录 HTML：`physicist/presentations/20th_century/Wilhelm_Rontgen/Wilhelm_Rontgen.html`
- **参考模板**:
  - 物理学家模板标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`
  - 通用模板：`physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md`
- **后续配套数据库脚本**（见第 4 步 / 第 4.5 步）：
  - `MySQL/seed_rontgen_full.py` — 人物主记录 + 研究领域入库（`person_field`）
  - `MySQL/seed_rontgen_relations.py` — 社会关系入库（`person_relation`）

---

## 你的任务

按照本提示词的步骤依次完成。**每完成一步向我汇报进度**，遇到歧义时先征求我的意见再继续。

> **数据库同步要求**：本提示词包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤。请严格按步骤操作，将伦琴的**研究领域**与**社会关系**写入 `greatminds` 数据库（MySQL），这是 OpenPhysicist 项目人物关系网络的一部分，与 Beamer 立传并行。

---

## 第 0 步：确认 Wikipedia 页面已就绪

- 读取本地 Wikipedia `page.md` 与 `page.html` 的 infobox 与正文
- 输出供校验的信息（事实基准如下）：

  - **生卒日期**：1845-03-27 生于普鲁士伦内普（Lennep，现属雷姆沙伊德）～ 1923-02-10 逝于德国慕尼黑，享年 77 岁，死因结直肠癌
  - **国籍变迁**：普鲁士（至 1848）→ 无国籍（1848–1888，随父母迁居荷兰）→ 德国（1888 起，重新取得德国国籍）
  - **父母**：父 Friedrich Conrad Röntgen（商人 / 布料制造商）；母 Charlotte Constanze Frowein
  - **教育**：苏黎世联邦理工学院（ETH Zurich，机械工程）；苏黎世大学博士 1869，论文《Studien über Gase》（论气体）
  - **博士导师**：Gustav Zeuner；**学术导师**：August Kundt（伦琴是其最喜爱的学生，毕业后跟随 Kundt 辗转维尔茨堡 → 斯特拉斯堡）
  - **主要任职机构**：斯特拉斯堡大学讲师 1874 → 物理教授 1876；霍恩海姆农学院教授 1875；吉森大学物理教席 1879；维尔茨堡大学 1888；慕尼黑大学 1900（巴伐利亚政府特邀）
  - **关键荣誉**：诺贝尔物理学奖 1901（首位得主）；Rumford Medal 1896（与 Philipp Lenard 共享）；Matteucci Medal 1896；Elliott Cresson Medal 1898（infobox 记 1897，正文表格记 1898，Beamer 采用 1898）；Pour le Mérite 1911
  - **知名学生**：Abram Ioffe（阿布拉姆·约费，苏联物理学奠基人）、Rudolf Ladenburg、Herman March、Ernst Wagner、Emil Silbernagel、John Patrick Donaghey
  - **核心贡献**：1895-11-08 在维尔茨堡大学物理研究所发现 X 射线（详见第 4 步）
  - **关键时间线**（15–20 个节点）：
    1. 1845-03-27 生于伦内普
    2. 1848 随父母迁居荷兰，成为无国籍者
    3. 1862 就读乌得勒支技术学校
    4. 1865 被诬陷画教师讽刺漫画而被开除
    5. 1865 进入苏黎世联邦理工学院（机械工程）
    6. 1869 苏黎世大学博士毕业
    7. 1872 与 Anna Bertha Ludwig 结婚
    8. 1874 斯特拉斯堡大学讲师
    9. 1876 斯特拉斯堡大学物理教授
    10. 1879 吉森大学物理教席
    11. 1888 重新取得德国国籍，获维尔茨堡大学物理教席
    12. 1895-11-08 发现 X 射线
    13. 1895-12-28 发表《Ueber eine neue Art von Strahlen》
    14. 1896 获 Rumford Medal、Matteucci Medal
    15. 1900 转任慕尼黑大学
    16. 1901 获首届诺贝尔物理学奖（拒绝发表演讲、拒绝申请专利）
    17. 1911 获 Pour le Mérite
    18. 1919 妻子 Anna Bertha 去世
    19. 1923-02-10 因结直肠癌逝于慕尼黑

---

## 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Wilhelm_Rontgen/` 子目录与 `images/`

---

## 第 2 步：复制 Makefile 【模板通用】

- 复制标杆实例 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Wilhelm_Rontgen_zh`、`VIDEO_NAME=Wilhelm_Rontgen_zh`

---

## 第 3 步：收集图片 【人物专属】

- 从 Wikipedia infobox 下载伦琴肖像到 `images/Rontgen.jpg`

---

## 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> **目的**：把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

### 4.1 伦琴的研究领域（按重要性 rank 排序）

| rank | 领域（name_en） | 中文 | 说明 | 对应 Beamer 页 |
|:--:|------|------|------|------|
| 0 | X-ray physics | X 射线物理 | 发现并系统研究 X 射线的性质 | 封面、核心页 |
| 1 | experimental physics | 实验物理学 | 阴极射线管实验、真空放电研究 | 核心页 |
| 2 | electromagnetic radiation | 电磁辐射 | X 射线作为电磁波谱的发现 | 核心页 |
| 3 | cathode rays | 阴极射线 | 研究背景：Crookes–Hittorf 管、Lenard 管 | 发现页 |
| 4 | medical imaging | 医学成像 | X 射线摄影术的开创性应用 | 应用影响页 |

> 领域字典 `fields` 表：`statistical mechanics` 等部分领域可能已存在，缺失的 `X-ray physics`/`experimental physics`/`electromagnetic radiation`/`cathode rays`/`medical imaging` 由 `seed_rontgen_full.py` 自动补建。

### 4.2 入库操作（见 `MySQL/seed_rontgen_full.py`）

- 新建 `people` 主记录：`name_en='Wilhelm Conrad Röntgen'`、`name_zh='威廉·康拉德·伦琴'`、`primary_occupation='physicist'`、`has_biography=1`、`has_social_data=1`，qid=`Q35149`
- 关联职业 `physicist`（rank 0）、国籍 `Germany`（德国，最终国籍）
- 将 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 执行后校验：
  ```sql
  SELECT f.name_en, pf.rank FROM person_field pf
  JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank;
  ```

---

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> **目的**：将伦琴的师承、合作、门生、家庭与科学影响写入 `person_relation`，形成可查询的人物关系网络。

### 4.5.1 关系清单（从 Wikipedia 提取）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gustav Zeuner | 师→生（博士导师） | 苏黎世大学博士导师 |
| advisor-student | August Kundt | 师→生（学术导师） | 伦琴是其最喜爱的学生，毕业后跟随 Kundt 辗转 |
| advisor-student | Abram Ioffe | 生→师（伦琴为学生） | 苏联物理学奠基人之一 |
| advisor-student | Rudolf Ladenburg | 生→师（伦琴为学生） | 物理学家 |
| colleague | Philipp Lenard | 无向 | 阴极射线研究同行，1896 共享 Rumford Medal |
| colleague | Henri Becquerel | 无向 | X 射线工作启发 Becquerel 发现天然放射性 |
| colleague | Marie Curie / Pierre Curie | 无向 | 受 X 射线工作影响，转向放射性同位素研究 |
| spouse | Anna Bertha Ludwig | 无向（夫妻） | 妻子，1872 结婚；其手部 X 光片为史上第一张医学 X 光片 |

> 关系类型键取自 `relation_types`：`advisor-student` / `colleague` / `spouse`。

### 4.5.2 入库操作（见 `MySQL/seed_rontgen_relations.py`）

- 连接 `greatminds` 库，以 `name_en='Wilhelm Conrad Röntgen'` 为中心
- 库中已存在人物优先复用（如 Becquerel、Curie 夫妇可能已在库），不在库的先建占位（`has_biography=0`），关系 note 加 `[材料待展开] ` 前缀
- 有向关系 advisor-student 按师→生；无向（colleague/spouse）按 `MIN(id)→MAX(id)` 存储
- 执行后校验并汇报：新建 X 人（占位）、新增 Y 条关系

---

## 第 5 步：设计配色方案 【人物专属】

- **气质**：X 射线的神秘穿透力、实验物理的严谨、静默探索的深沉
- **建议配色**：深邃黑蓝 + 香槟金（诺奖）+ 四个分类色
  - `badgeXray` X 射线物理 — 深靛蓝 `#1A237E`
  - `badgeExp` 实验物理 — 青绿 `#0E7C7B`
  - `badgeEm` 电磁辐射 — 琥珀 `#E07B30`
  - `badgeMed` 医学成像 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），以不同尺度呼应"穿透性/透视"主题——X 射线穿透物质看到内在，正如设计以层层透明度呼应

### 5.1 物理学家格式硬要求 ★

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自本地 Wikipedia，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

---

## 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 顶部标签「20 世纪物理学 · X 射线」/ Wilhelm Röntgen 1845–1923 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 主标题「威廉·伦琴 - 从伦内普到诺贝尔奖」+ 左头像 + 右 2×2 信息网格
03  核心贡献概览 — X 射线物理 / 实验物理 / 电磁辐射 / 医学成像
04  早年：伦内普与乌得勒支 — 1845 出生、1848 迁荷兰成为无国籍者、1865 被诬陷开除
05  苏黎世求学 — ETH 机械工程、苏黎世大学博士、Kundt 门下
06  斯特拉斯堡与吉森 — 讲师到教授、1879 吉森物理教席
07  维尔茨堡：发现 X 射线 — 1895-11-08、阴极射线实验、Crookes–Hittorf 管
08  X 射线：一种新的射线 — 《Ueber eine neue Art von Strahlen》、妻子手部照片、三篇论文
09  科学反响 — Becquerel 放射性、居里夫妇
10  1901 诺贝尔奖 — 史上首位得主、拒绝演讲、拒绝专利
11  门生与传承 — Abram Ioffe、Rudolf Ladenburg
12  荣誉与纪念 — Rumford Medal、元素 111 roentgenium、世界放射学日
13  晚年：慕尼黑 — 1900 慕尼黑教席、一战、通胀破产
14  遗产 — X 射线改变医学与物理学
15  结尾
```

---

## 第 7 步：编写 Beamer 源码 【模板通用】

- 文件名：`physicist/presentations/20th_century/Wilhelm_Rontgen/Wilhelm_Rontgen_zh.tex`
- 每页用 `\newcommand{\xxxslide}{...}` 定义，配色与卡片版式复用标杆实例骨架
- **身份信息页实现模式**（参照 `\profileslide`）：
  - 左：`\IfFileExists{images/Rontgen.jpg}{\includegraphics[width=3.0cm,height=3.9cm,keepaspectratio]{Rontgen.jpg}}{...}` 头像 + 姓名注
  - 右：2×2 信息网格，`infob` 圆角卡片（上排两张 `anchor=north`，下排两张 `anchor=south`）
    - 上排：生卒+本名+国籍 / 师承+任职
    - 下排：出生地+去世地+教育 / 主要荣誉+核心领域
  - 任职务必含 `Strasbourg · Hohenheim · Giessen · Würzburg · Munich`（Hohenheim 为 1875 年农学院教授，勿遗漏），与封面底部状态栏一致；国籍栏补充 `普鲁士 → 无国籍 → 德国` 的变迁

---

## 第 8 步：布局检查 ★★★ 编译即查

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图肉眼检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标

---

## 第 9 步：史实审查 + 术语审查

### 伦琴特殊陷阱

| 陷阱 | 说明 |
|------|------|
| 首位诺奖得主 | 1901 诺贝尔物理学奖史上首位得主，但勿写成"首个诺贝尔奖"（文学/和平/化学等奖项同年各有得主） |
| 国籍变迁 | 1848–1888 年是无国籍状态（随父母迁居荷兰），1888 年才重新取得德国国籍，勿简单写"德国人" |
| 被开除事件 | 1865 年被诬陷画教师讽刺漫画而被乌得勒支技术学校开除，漫画实为他人所画，勿写成"违纪被开除" |
| 博士导师 | 博士导师是 Gustav Zeuner，August Kundt 是"学术导师/最喜爱的老师"，两者勿混淆 |
| 发现日期 | X 射线发现于 1895-11-08（周五），论文发表于 1895-12-28，勿混用 |
| 拒绝专利 | 与居里夫妇一样拒绝为 X 射线申请专利，希望全社会受益，勿写成"无商业头脑" |
| 拒绝诺奖演讲 | 因公开演讲害羞而拒绝发表诺贝尔演讲，勿写成"缺席颁奖" |
| 妻子 X 光片 | 史上第一张医学 X 光片是其妻子 Anna Bertha 的手（1895-12-22），妻子惊呼"I have seen my death!" |
| 元素命名 | 第 111 号元素 roentgenium（錀，Rg）2004 年以他命名，勿写成"伦琴元素" |
| Elliott Cresson Medal 年份 | Wikipedia 内部矛盾：infobox 写 1897，正文 Recognition 表格写 1898。Beamer 采用 1898（正文表格更详细、有 citation 支撑）；如需进一步核实可查 Franklin Institute 官方记录 |
| 晚年 | 一战后德国通胀导致其破产，晚年生活困顿，勿忽略此史实 |

### 术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| X-ray | X 射线 | 又称伦琴射线（Röntgen rays），德语系称 Röntgenstrahlen |
| Crookes–Hittorf tube | 克鲁克斯-希托夫管 | 真空放电管 |
| cathode rays | 阴极射线 | 与 X 射线的区别 |
| barium platinocyanide | 铂氰酸钡 | 荧光屏材料 |
| radiograph | X 光片 / 放射影像 | 早期称 X 射线照片 |
| roentgenium | 錀（Rg） | 第 111 号元素 |
| fluoroscopy | 荧光透视 | X 射线透视成像 |

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/pages/20th_century/Wilhelm_Conrad_Röntgen/page.md` | 本地 Wikipedia 正文（权威事实基准） |
| `physicist/presentations/20th_century/Wilhelm_Rontgen/Wilhelm_Rontgen.html` | 本地 Wikipedia HTML |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 模板标杆 Beamer 源码 |
| `physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex` | 首例成品参考 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_rontgen_full.py` | 研究领域入库（第 4 步） |
| `MySQL/seed_rontgen_relations.py` | 社会关系入库（第 4.5 步） |

## 背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Beethoven · Karajan — Symphony No. 3 "Eroica"** 或 **Timeless**（Alex-Productions）
- **风格**: 古典庄严 / 沉稳纪录片
- **匹配理由**:
  - 伦琴是古典物理时代的里程碑人物，X 射线的发现开创了现代物理与医学的新纪元，古典交响乐的庄严与其历史地位相称
  - "沉稳"匹配其静默探索的气质——不事张扬，拒绝专利、拒绝演讲，甘愿让全社会受益
  - "穿透/透视"的母题契合 X 射线穿透物质、揭示内在的隐喻
- **本地路径**: `music_audio/` 下选定曲目 → `presentations/20th_century/Wilhelm_Rontgen/`
- **时长**: 与 16 页 × 7 秒 ≈ 112 秒对齐，ffmpeg `-shortest` 自动对齐

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
