# 物理学家立传提示词（Makoto Kobayashi 小林诚）

> **OpenPhysicist 21 世纪批次**人物专属立传提示词。以 Kenneth_G_Wilson_zh.md 为结构母本（0–11 节），
> 本文件为 Makoto Kobayashi（2008 诺贝尔物理学奖，CKM 矩阵与 CP 破缺）定制。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Makoto Kobayashi（小林诚，1944-04-07 ~ 在世）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页），且强调「研究领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Makoto Kobayashi（小林 诚，1944-04-07 生于名古屋，在世）
- **气质关键词**：**三代夸克的预言者、CP 破缺的解码者、名古屋学派的传承人** —— 2008 诺贝尔物理学奖获奖理由（官方原文，禁止改写）：
  > "for the discovery of the origin of the broken symmetry which predicts the existence of at least three families of quarks in nature"（发现对称性破缺的起源，预言了自然界至少存在三代夸克；与益川敏英共享 1/2 奖金，即个人得 1/4）
- **设计母题**：**三代扇形（three generations）**。CKM 矩阵把两代扩展为三代，像一个不断展开的扇形/旋转混合角——可用「重叠圆环 + 混合箭头」的视觉语言表达夸克代际之间的混合。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Makoto_Kobayashi/page.md`（已有本地）
- **待下载**：`Makoto_Kobayashi.html` 与 `images/` 待下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Makoto_Kobayashi`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属，page.md 已核对】

- 生卒：1944-04-07 生于名古屋（当时属大日本帝国），在世（卒日留白）。
- 国籍：日本。
- 家庭：2 岁丧父（父 Hisashi）；小林家宅毁于名古屋大空袭，寄住母家（母姓海部）。表兄两位：海部俊树（第 51 任日本首相）与海部北斗（Norio Kaifu，天文学家）。海部俊树回忆其幼时「安静可爱、总在读难懂的书」。
- 教育：1967 名古屋大学理学部毕业；1972 名古屋大学大学院理学研究科 DSc（理学博士）。大学期间受坂田昌一（Shoichi Sakata）等人指导。
- 博士导师：frontmatter 与 infobox 明载 Shoichi Sakata。
- 博士后：page.md 无载。
- 任职机构（Professional record 全表）：
  - 1972-04 京都大学理学部助手（research associate）
  - 1979-07 高能加速器研究机构（KEK）副教授
  - 1989-04 KEK 教授、物理第二研究部长
  - 1997-04 KEK 素粒子原子核研究所教授
  - 2003-04 KEK 素粒子原子核研究所所长
  - 2004-04 大学共同利用机关法人 KEK 理事
  - 2006-06 KEK 名誉教授
  - 2008 名古屋大学特聘招 faculties 教授（Distinguished Invited University Professor）
  - 2009 KEK 特别荣誉教授；日本学术振兴会制度审议机构理事兼所长
  - 2010 小林·益川研究所（KMI，名古屋大学）咨询委员会主席；日本学士院会员
  - 2018-04 KMI 所长
  - 2020-04 KMI 名誉所长
- 关键荣誉：仁科纪念奖 1979；樱井奖 1985；日本学士院奖 1985；中日文化奖 1994；朝日奖 1995；文化功劳者 2001；欧洲物理学会高能与粒子物理奖 2007；诺贝尔物理学奖 2008（1/4）；文化勋章 2008（授勋式于东京皇居）；日本学士院会员 2010；上海交通大学荣誉博士（frontmatter）。
- 知名学生：page.md 无载（禁写）。
- 核心贡献清单：
  1. 与益川敏英 1973 年论文《CP Violation in the Renormalizable Theory of Weak Interaction》——CP 破缺在小林·益川矩阵（CKM 矩阵）框架下的解释；
  2. 预言自然界至少存在三代夸克（六味夸克），四年后由底夸克发现实验证实；
  3. 该论文截至 2010 年为高能物理史上被引第四高的论文；
  4. 与益川共享 2008 诺贝尔奖 1/2（个人 1/4），另一半归南部阳一郎；
  5. KEK 长期领导物理第二研究部，推动日本高能物理实验与理论结合。
- 关键时间线（15 节点）：
  1. 1944-04-07 生于名古屋
  2. 1946（2 岁）父亲 Hisashi 去世
  3. 名古屋大空袭，家宅被毁，寄住海部家
  4. 1967 名古屋大学理学部毕业
  5. 大学期间受坂田昌一指导
  6. 1972 名古屋大学 DSc
  7. 1972-04 京都大学理学部助手
  8. 1973 与益川敏英发表 CP 破缺论文，预言三代夸克
  9. 1977 底夸克发现，三代预言四年内获证实
  10. 1979-07 任 KEK 副教授；同年获仁科纪念奖
  11. 1985 获樱井奖与日本学士院奖
  12. 1989-04 任 KEK 教授、物理第二研究部长
  13. 2007 获欧洲物理学会高能与粒子物理奖
  14. 2008 获诺贝尔物理学奖（1/4）与文化勋章
  15. 2010 入选日本学士院会员、任 KMI 咨询委员会主席
  16. 2015 筑波中央公园立小林诚铜像（与朝永振一郎、江崎玲于奈）
  17. 2018-04 任 KMI 所长；2020-04 任名誉所长

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `physicist/presentations/21th_century/` 下建 `Makoto_Kobayashi/` 与 `images/`；Makefile 设 `MAIN=Makoto_Kobayashi_zh`、`VIDEO_NAME=Makoto_Kobayashi_zh`。
- 肖像：Wikipedia infobox 无照片，可用 2008 斯德哥尔摩记者会合影（Cabibbo_Kobayashi_2.jpg 或六诺奖同框照，Commons 可取）裁右半；404 则用装饰圆占位。

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | particle physics | 粒子物理 | 主业：高能物理理论 | 封面、核心页 |
| 1 | CP violation | CP 破缺 | 1973 论文核心问题 | 核心页 |
| 2 | weak interaction | 弱相互作用 | 论文题目限定 renormalizable theory | 理论页 |
| 3 | quark mixing | 夸克混合 | CKM 矩阵的物理内涵 | 矩阵页 |
| 4 | standard model | 标准模型 | CKM 为其组成部分 | 脉络页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Shoichi Sakata | 师→生（博士导师） | 名古屋大学导师，坂田模型提出者 |
| colleague | Toshihide Maskawa | 无向 | 京都大学同事，1973 年 CP 破缺论文合作者 |
| co-honored | Toshihide Maskawa | 无向 | 2008 诺贝尔物理学奖共享 1/2 |
| co-honored | Yoichiro Nambu | 无向 | 2008 诺贝尔物理学奖另一半得主 |
| spouse | Sachiko Enomoto | 无向 | 1975 年结婚，育一子 Junichiro；后病故 |
| spouse | Emiko Nakayama | 无向 | 1990 年再婚，育一女 Yuka |

> 无载禁写：Nicola Cabibbo（仅同框照片与矩阵命名，正文无师承/合作叙述）；两位表兄海部俊树/海部北斗（家族逸闻不入库）；博士生（页面未载）。

### 第 5 步：配色方案 【人物专属】

- **气质**：沉稳、东方内敛、预言成真
- **主色**：深藏青 `#16324F`（理论纵深）+ 诺奖香槟金 `C9A227`
  - `badgeCP` CP 破缺 — 深红 `#9E2B25`
  - `badgeGen` 三代夸克 — 青绿 `#0E7C7B`
  - `badgeKEK` 实验机构 — 琥珀 `#C87F2F`
  - `badgeAcad` 学士院 — 靛蓝 `#4C5FD5`
- **背景母题**：三个错落的半透明圆环两两交叠，象征三代夸克的混合与 CKM 相位。

### 第 6 步：幻灯片序列（10–16 页规划）【人物专属】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 三代夸克的预言者 / Makoto Kobayashi 1944– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍/出生地/师承/任职/荣誉/核心领域）
03  核心贡献概览 — CP 破缺 / CKM 矩阵 / 三代预言 / KEK 领导
04  早年：名古屋 (1944–1967) — 丧父、空袭、海部家、坂田门下
05  名古屋大学：坂田学派传承 (1967–1972) — DSc、复合模型传统
06  京都岁月：与益川相遇 (1972–1979) — 1973 论文诞生
07  CKM 矩阵：CP 破缺的代数（核心贡献页，公式框放 CKM 矩阵 3×3 形式与相位 δ）
08  三代预言：从 2×2 到 3×3 — 1977 底夸克证实
09  KEK 三十年 (1979–2006) — 副教授→教授→所长→名誉教授
10  荣誉之年 2008 — Nobel 1/4 · 文化勋章 · 记者会同框
11  学士院与 KMI (2010–2020) — KMI 主席/所长/名誉所长
12  遗产：CP 破缺与现代粒子物理 — B 介子工厂、Kobayashi-Maskawa 研究所
13  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 得奖份额 | Kobayashi 与 Maskawa **共享 1/2**（个人 1/4），另一半归南部阳一郎；勿写成「三人平分」 |
| 名字拼写 | 页面正文用 Maskawa，同框照片说明用 Masukawa；立传统一用 Maskawa（益川敏英），勿混拼 |
| 获奖理由 | 官方措辞强调 "origin of the broken symmetry…at least three families of quarks"；勿改写成 "CKM matrix" 字样 |
| Cabibbo | 仅照片同框与 CKM 命名，page.md 无师承/合作叙述，**禁建关系** |
| 博士导师 | page.md 作「大学期间受坂田昌一等人指导」+ infobox doctoral advisor；勿写成「博士论文导师」以外的杜撰细节 |
| 家族逸闻 | 海部俊树（首相）与海部北斗（天文学家）是表兄；可作轶事页素材，不入社会关系库 |
| KEK 沿革 | KEK 即 National Laboratory of High Energy Physics；1997 前后机构名称与头衔变化多，按 Professional record 年份逐条照抄 |
| 铜像年份 | 筑波铜像立于 2015（与朝永振一郎、江崎玲于奈三人），勿写成获奖当年 |
| 亲属 | 第一任妻子 Sachiko Enomoto（1975 结婚、后病故）与第二任 Emiko Nakayama（1990 结婚）；子女 Junichiro/Yuka，勿张冠李戴 |
| 在世 | 1944 年生，在世；生卒页卒日留白 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| CKM matrix | 小林·益川矩阵（CKM 矩阵） | 全称 Cabibbo–Kobayashi–Maskawa matrix |
| CP violation | CP 破缺 | 非「CP 不守恒」的口语化 |
| broken symmetry | 对称性破缺 | 获奖理由原词，spontaneous 另译自发破缺 |
| quark generation | 夸克代 | 三代=六味夸克 |
| bottom quark | 底夸克 | 1977 发现，证实预言 |
| DSc | 理学博士 | 名古屋大学 1972 |
| KEK | 高能加速器研究机构 | 勿与 CERN 混淆 |
| Sakata model | 坂田模型 | 名古屋学派传统 |
| Order of Culture | 文化勋章 | 2008，东京皇居授勋 |
| Japan Academy | 日本学士院 | 2010 会员 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（纪录片/电影/稳重）
- **匹配理由**：纪录片质感匹配「1973 论文→四年后证实→35 年后诺奖」的长线叙事；稳重基调匹配小林诚内敛的气质；「不可见之光」暗合 CP 破缺这种肉眼不可见的对称性破缺。
- **备选**：Timeless（长期纲领感）、The Flow of Time（时间线叙事）。
- 批内不重复：本批 Maskawa=Cinematic Experience、Kao=Shine Like The Sun、Boyle=Daylight、Smith=Ascension。

---

## 五、执行红线 【模板通用】

- 只收 page.md 明载的关系；yaml note 含 ": " 或以引号开头时整体单引号包裹。
- 对手方入库用规范名：Shoichi Sakata（库内 id=2094 复用）、Toshihide Maskawa、Yoichiro Nambu、Sachiko Enomoto、Emiko Nakayama；不给对手方编造 qid。
- 禁止修改 generate_21st_century_list.py、名录 md、模板文件。
