# 物理学家立传提示词（人物专属：Gabriel Lippmann）

> 本文件是 OpenPhysicist 20 世纪诺贝尔物理学奖批量立传的**人物专属提示词**，结构对齐标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Gabriel Lippmann（加布里埃尔·李普曼），1908 年诺贝尔物理学奖得主，彩色摄影干涉法的发明者。
- **设计哲学**：保留物理学家模板两大骨架——「身份信息页」与「研究领域结构化表达」；本人物的设计重心是**光与颜色的物理**：把"颜色"还原为"波长"，用干涉把光谱固定在干板上。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Gabriel Lippmann（1845-08-16 ~ 1921-07-12，享年 75 岁）
- **气质关键词**：**干涉光谱的雕刻师、彩色摄影的开创者、实验物理的巧匠**
- **官方获奖理由（禁止改写）**：
  > "for his method of reproducing colours photographically based on the phenomenon of interference"（因其基于干涉现象的彩色摄影复制方法）
- **设计母题**：**驻波与干涉条纹（standing waves / interference lamellae）**——光在反射面与感光乳剂之间形成驻波，波节波腹的层状结构把颜色"刻"进干板；视觉语言用细密平行条纹与光谱渐变。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Gabriel_Lippmann/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 标杆提示词：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 物理学家成品参照：`physicist/presentations/20th_century/Antoine_Henri_Becquerel/Antoine_Henri_Becquerel_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ⏳ **待下载** `https://en.wikipedia.org/wiki/Gabriel_Lippmann` 到 `{Dir}/Gabriel_Lippmann.html`（本地暂只有 `page.md`，无 html 与 images/）
- 提取 infobox 与正文，输出供校验（**事实基准如下**）：
  - 生卒（1845-08-16 生于卢森堡霍勒里希 ~ 1921-07-12 卒于大西洋海上（自加拿大返法途中），享年 75 岁；**frontmatter 作 1921-07-13，以正文/infobox 12 日为准**）
  - 国籍（卢森堡出生，犹太家庭，1848 年迁巴黎，后归化法国）
  - 家庭（父在霍勒里希经营手套作坊；1888 年娶小说家 Victor Cherbuliez 之女）
  - 教育（1858 入 Lycée Napoléon（今 Henri-IV）；1868 入巴黎高等师范学院，agrégation 落榜；1873 赴德科学考察，海德堡大学随 Kühne 与 Kirchhoff，1874 summa cum laude 获博士；1874 柏林短暂拜访 Helmholtz；1875-07-24 向巴黎大学提交电毛细现象博士论文 *Relations entre les phénomènes électriques et capillaires*）
  - 博士导师（infobox：Jules Jamin + Gustav Kirchhoff；Helmholtz 仅为短暂拜访，见陷阱表）
  - 任职（1878 入巴黎大学理学院；1883 数学物理教授；1886 实验物理教授并接 Jamin 任物理研究所所长）
  - 关键荣誉（Nobel 1908；Progress Medal 1897；荣誉军团骑士 1881/军官 1894/指挥官 1900/大军官 1919；法兰西科学院院士 1886；英国皇家学会外籍会员 1896）
  - 知名学生（博士生：Pierre Curie、Marie Curie、Jean Lecomte、Constantin Miculescu；其他知名学生：Paul Langevin）
  - 核心贡献清单：
    1. Lippmann 干板彩色摄影（驻波干涉记录 λ/(2n) 层状结构，1908 诺奖核心）
    2. Lippmann 静电计（毛细管静电计，用于第一台 ECG 机器）
    3. 1881 年预言逆压电效应
    4. 1908 年集成摄影（透镜阵列→光场成像先声）
    5. coelostat 定天镜（补偿地球自转的天文摄影装置）
    6. 1895 年计时去人差法 + 1900 年布朗棘轮思想实验
  - 关键时间线（1845 生 → 1848 迁巴黎 → 1858 中学 → 1868 高师 → 1873-74 海德堡 → 1875 巴黎大学博士 → 1878 入索邦 → 1881 预言逆压电效应 → 1883 数学物理教授 → 1886 实验物理教授/所长 + 转向彩色摄影 → 1888 成婚 → 1891-02-02 宣布彩色摄影成功 → 1895 计时法 → 1897 Progress Medal → 1900 布朗棘轮 → 1908 集成摄影 + 诺奖 → 1919 大军官 → 1921 卒于归途海上）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下已有 `Gabriel_Lippmann/`（本提示词所在），需新建 `images/` 子目录存放肖像与插图

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆目录 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Gabriel_Lippmann_zh`、`VIDEO_NAME=Gabriel_Lippmann_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：先试 Commons `Special:FilePath/Le professeur Lippmann dans le laboratoire des recherches physiques de la Sorbonne.jpg?width=500`（索邦实验室照，page.md 内嵌）
- 404 则退 Nobelprize.org laureate/12 页面像；再失败用装饰圆占位（主色边框圆 + 姓名缩写）

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | color photography | 彩色摄影 | Lippmann 干板，1908 诺奖核心 | 核心页 |
| 1 | optics | 光学 | 干涉/驻波原理 | 原理页 |
| 2 | piezoelectricity | 压电效应 | 1881 预言**逆**压电效应 | 压电页 |
| 3 | electrocapillarity | 电毛细现象 | 博士论文 + Lippmann 静电计 | 早年页 |
| 4 | integral photography | 集成摄影（光场成像） | 1908 提出，光场相机先声 | 集成页 |

入库：`MySQL/data/Gabriel_Lippmann.yaml`（已备好，`cd MySQL && python3 seed_person.py data/Gabriel_Lippmann.yaml`）。
校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gustav Kirchhoff | 师→生 | 海德堡大学博士导师之一，1874 summa cum laude |
| advisor-student | Jules Jamin | 师→生 | 巴黎大学博士导师之一（infobox 明载） |
| advisor-student | Pierre Curie | 李普曼→学生 | 博士生，1903 诺奖得主 |
| advisor-student | Marie Curie | 李普曼→学生 | 博士生，两届诺奖得主 |
| advisor-student | Paul Langevin | 李普曼→学生 | 其他知名学生 |
| advisor-student | Jean Lecomte | 李普曼→学生 | 博士生 |
| advisor-student | Constantin Miculescu | 李普曼→学生 | 博士生 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：光谱、精致、实验室匠心
- **配色**：干涉光谱蓝（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 — 干涉光谱蓝 `#0F4C81`
  - `badgeInterf` 干涉光学 — `#2E86AB`
  - `badgePhoto` 彩色摄影 — `#C0392B`
  - `badgePiezo` 压电 — `#7D5BA6`
  - `badgeIntegral` 集成摄影 — `#1E8A5A`
- **背景母题**：细密平行干涉条纹 + 稀疏光谱色圆点，呼应"驻波把颜色刻进乳剂"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素（李普曼：卢森堡/法国 | 巴黎大学 | Nobel 1908）。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名（Jonas Ferdinand Gabriel Lippmann）、国籍、出生地（霍勒里希）、师承（Jamin/Kirchhoff）、任职（巴黎大学）、主要荣誉、核心领域。事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 干涉彩色摄影发明人 / Gabriel Lippmann 1845–1921 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 彩色摄影 / 逆压电 / 静电计 / 集成摄影
04  早年：卢森堡到巴黎 (1845–1868) — 手套作坊之子、Henri-IV、高师、agrégation 落榜
05  德国岁月 (1873–1875) — 海德堡 Kühne/Kirchhoff、柏林拜访 Helmholtz、巴黎大学博士
06  索邦教席 (1878–1886) — 数学物理→实验物理教授、接任 Jamin 任所长
07  电毛细现象与 Lippmann 静电计 — 用于第一台 ECG 机器
08  1881：预言逆压电效应 — 正效应归居里兄弟，逆效应属李普曼
09  彩色摄影：把光谱刻进干板（核心贡献页，公式框 λ/(2n) 层间距）
10  集成摄影 (1908) — 透镜阵列→光场相机/3D 成像先声
11  其他发明 — coelostat 定天镜、计时去人差、布朗棘轮思想实验
12  门生与传承 — Pierre/Marie Curie、Langevin
13  荣誉与认可 — Nobel 1908 · Progress Medal 1897 · 荣誉军团四级 · 院士
14  遗产：从干涉照相到激光全息（Lippmann–Bragh 全息）
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`；头部宏（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用标杆骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Lippmann 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 卒日噪声 | 正文/infobox 1921-**07-12**（海上），frontmatter 作 07-13，一律以正文为准 |
| 国籍表述 | 卢森堡出生→法国归化，禁写成"法国人李普曼生于巴黎"；犹太家庭背景 page 明载可客观一句 |
| 博士导师 | infobox 为 **Jamin + Kirchhoff**；Helmholtz 仅 1874 短暂拜访（frontmatter 有列但 infobox 未列），禁写"受业于 Helmholtz" |
| 逆压电效应 | 1881 年预言的是**逆效应**（converse effect）；正效应 1880 由居里兄弟发现，勿写"发现压电效应" |
| 获奖理由 | 忠实英文原句 "for his method of reproducing colours photographically based on the phenomenon of interference"，勿改写成"发明彩色摄影"泛称 |
| ECG | 其静电计被**用于**第一台心电图机器，勿写成"发明心电图" |
| 学生归属 | Pierre/Marie Curie 为其博士生系 infobox 明载，可写；勿追加 page 未载的其他师承 |
| 集成摄影 | 1908 年仅理论提出、无实物演示（透镜阵列材料当时缺乏），勿写成"发明光场相机" |
| 布朗棘轮 | 1900 年提出的是思想实验（麦克斯韦妖的力学版本），勿写成实验装置 |
| 引语红线 | 仅 1891-02-02 向法兰西科学院的宣布句可引（page 明载英译），其余一律转述 |
| 与贝克勒尔 | 勿把他与 Becquerel 家族的彩色摄影尝试混写（page 未载其互动） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Lippmann plate | 李普曼干板 | 干涉彩色感光板，非普通底片 |
| interference | 干涉 | 光学驻波成因 |
| standing wave | 驻波 | 波节波腹层状结构 |
| lamellae | 薄层（干涉条纹层） | 间距 = λ/(2n) |
| electrocapillarity | 电毛细现象 | 博士论文主题 |
| converse piezoelectric effect | 逆压电效应 | 勿与正效应混淆 |
| integral photography | 集成摄影 | 光场成像先声 |
| coelostat | 定天镜 | 补偿地球自转的天文装置 |
| light field | 光场 | 现代光场相机概念源头 |
| electrometer | 静电计 | 毛细管静电计 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Really Slow Motion（史诗 / 美丽 / 振奋）
- **匹配理由**：彩色摄影是把"太阳的颜色"永久固定在干板上的发明，曲目名与"光谱/光明"母题直接呼应；光明结尾匹配其优雅而唯一的干涉照相遗产。
- **本地路径**：`music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav`
- **备选**（未采用）：
  - ★★ The Flow of Time — "时间感"匹配 76 年跨度，但本批已分配给 Wien
  - ★ Awaken — "明亮/突破"匹配 1891 年首次成功的宣布，但"鼓舞"气质与其匠人心略偏
- **时长核验**：曲目 2:49 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐
- **备注**：批内 BGM 去重——Marconi=SEA、Braun=The Invisible Light、van der Waals=Eternals、Wien=The Flow of Time。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Gabriel_Lippmann/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Gabriel_Lippmann.yaml` | 入库 yaml（已按本提示词 §4/§4.5 备好） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
