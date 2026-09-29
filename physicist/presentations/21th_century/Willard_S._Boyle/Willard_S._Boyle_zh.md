# 物理学家立传提示词（Willard S. Boyle 威拉德·博伊尔）

> **OpenPhysicist 21 世纪批次**人物专属立传提示词。以 Kenneth_G_Wilson_zh.md 为结构母本（0–11 节），
> 本文件为 Willard S. Boyle（2009 诺贝尔物理学奖，CCD 电荷耦合器件）定制。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Willard Sterling Boyle（威拉德·斯特林·博伊尔，1924-08-19 ~ 2011-05-07，享年 86 岁）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页），且强调「研究领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Willard Sterling Boyle（1924-08-19 生于新斯科舍省阿默斯特 ~ 2011-05-07 逝于新斯科舍省特鲁罗），加拿大应用物理学家
- **气质关键词**：**CCD 之父、阿波罗幕后推手、连续红宝石激光首创者** —— 2009 诺贝尔物理学奖获奖理由（官方原文，禁止改写）：
  > "for the invention of an imaging semiconductor circuit - the CCD sensor"（发明成像半导体电路——CCD 传感器；与 George E. Smith 共享 1/2 奖金）
- **设计母题**：**像素矩阵（charge buckets）**。CCD 把光子变成电荷再变成图像——可用「暗背景上的像素点阵渐次点亮成一幅图像」的视觉语言，呼应「人类视觉的延伸」。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Willard_S._Boyle/page.md`（已有本地）
- **待下载**：`Willard_S._Boyle.html` 与 `images/` 待下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Willard_S._Boyle`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属，page.md 已核对】

- 生卒：1924-08-19 生于新斯科舍省阿默斯特 ~ 2011-05-07 逝于新斯科舍省特鲁罗医院（肾病并发症，享年 86 岁）。
- 国籍：加拿大（frontmatter 另含 United States）。
- 家庭：约 2 岁随父母移居魁北克；14 岁前由母亲在家教育；1946 年与 Betty 结婚（风景画家），育 4 子女、10 孙辈、6 曾孙辈；退休后往返哈利法克斯与华莱士，与妻子在 Wallace 共同创办美术馆。
- 教育：14 岁入蒙特利尔 Lower Canada College；McGill 大学——1943 因二战中断加入皇家加拿大海军（借调皇家加拿大海军航空兵，战争结束前学习驾驶喷火战斗机在航母降落）；战后复学，1947 B.Sc.、1948 M.Sc.、1950 PhD（质谱方向，论文：建造 Dempster 型质谱仪并测碱金属在钨中的扩散率）。
- 博士导师：H. Watson（McGill，infobox 明载；正文无更多叙述）。
- 博士后段：博士毕业后在加拿大 Radiation Lab 一年 + 皇家军事学院教物理两年。
- 任职机构：
  - 1953 加入 Bell Telephone Laboratories
  - 1962 与 Don Nelson 发明首台连续运转红宝石激光器；半导体注入激光器首件专利在列
  - 1962 任 Bell Labs 子公司 Bellcomm 空间科学与探索研究部主任——支持阿波罗计划、参与挑选登月点
  - 1964 回 Bell Labs，集成电路研发
  - 1975–1979 Bell Labs 研究执行总监（Executive Director of Research），1979 退休
- 关键荣誉：Stuart Ballantine Medal 1973（CCD 结构发明）；IEEE Liebmann Award 1974；美国工程院院士 1974；C&C Prize 1999；Edwin H. Land Medal 2001；Charles Stark Draper Prize 2006；诺贝尔物理学奖 2009；加拿大勋章同伴（Companion of the Order of Canada）2010；National Inventors Hall of Fame（frontmatter）。
- 知名学生：page.md 无载（禁写；工业实验室无博士生）。
- 核心贡献清单：
  1. 1969 与 George E. Smith 发明电荷耦合器件（CCD）——成像半导体电路；
  2. CCD 让 NASA 从太空传回清晰图像，也是今日数码相机的核心技术；
  3. 1962 与 Don Nelson 发明首台连续运转红宝石激光器；半导体注入激光器首件专利在列；
  4. Bellcomm 空间科学与探索研究部主任——阿波罗计划支持与登月点遴选；
  5. Bell Labs 研究执行总监（1975–1979）。
- 关键时间线（15 节点）：
  1. 1924-08-19 生于新斯科舍省阿默斯特
  2. 约 1926 随父母移居魁北克
  3. 14 岁前母亲在家教育
  4. 14 岁入 Lower Canada College
  5. 1943 二战中断学业，加入皇家加拿大海军
  6. 借调海军航空兵，学习航母降落喷火战机
  7. 1947 McGill B.Sc.
  8. 1948 McGill M.Sc.
  9. 1950 McGill PhD（质谱）
  10. Radiation Lab 一年 + 皇家军事学院执教两年
  11. 1953 加入 Bell Labs
  12. 1962 与 Don Nelson 发明连续运转红宝石激光器；同年任 Bellcomm 空间研究部主任（阿波罗）
  13. 1964 回 Bell Labs（集成电路）；1969 与 Smith 发明 CCD
  14. 1975–1979 Bell Labs 研究执行总监
  15. 1973 Ballantine · 1974 Liebmann/NAE · 1999 C&C · 2001 Land · 2006 Draper
  16. 2009-10 诺贝尔物理学奖（12-08 诺奖演讲 "CCD – an Extension of Man's Vision"）
  17. 2010 加拿大勋章同伴
  18. 2011-05-07 逝于特鲁罗，享年 86 岁

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `physicist/presentations/21th_century/` 下建 `Willard_S._Boyle/` 与 `images/`；Makefile 设 `MAIN=Willard_S._Boyle_zh`、`VIDEO_NAME=Willard_S._Boyle_zh`。
- 肖像：Wikipedia infobox 有 2009 年照片；404 则用装饰圆占位。

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | charge-coupled device | 电荷耦合器件（CCD） | 1969 发明，2009 诺奖核心 | 核心页 |
| 1 | semiconductor laser | 半导体激光器 | 注入激光器首件专利、红宝石激光 | 激光页 |
| 2 | physics | 物理学 | infobox Fields，应用物理 | 身份页 |
| 3 | image processing | 图像处理 | CCD 成像应用 | 应用页 |
| 4 | space research | 空间研究 | Bellcomm/阿波罗支持 | 阿波罗页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | H. Watson | 师→生（博士导师） | McGill 博士导师（1950 质谱论文） |
| colleague | George E. Smith | 无向 | Bell Labs 同事，1969 年 CCD 共同发明人 |
| co-honored | George E. Smith | 无向 | 2009 诺贝尔物理学奖共享 1/2 |
| co-honored | Charles Kuen Kao | 无向 | 2009 诺贝尔物理学奖另一半得主（光纤通信） |
| colleague | Don Nelson | 无向 | Bell Labs 同事，1962 年首台连续运转红宝石激光器合作者 |
| spouse | Betty Boyle | 无向 | 1946 年结婚，风景画家，育 4 子女 |
| controversy | Eugene I. Gordon | 无向 | 已退休 Bell Labs 同事，主张 CCD 用于摄影非 Boyle 所创 |
| controversy | Michael Francis Tompsett | 无向 | 已退休 Bell Labs 同事，主张 CCD 用于摄影非 Boyle 所创 |

> 无载禁写：Betty 仅 spouse（美术馆合作不另立关系）；Gordon/Tompsett 争议仅录 page.md 原文主张，note 不做倾向性评断；学生（页面未载）。

### 第 5 步：配色方案 【人物专属】

- **气质**：实用、明亮、影像化
- **主色**：琥珀 `#A3571B`（CCD 硅片与暖色影像）+ 诺奖香槟金 `C9A227`
  - `badgeCCD` CCD — 深青 `#0A5555`
  - `badgeLaser` 激光 — 深红 `#8C1F28`
  - `badgeApollo` 阿波罗 — 靛蓝 `#2B3A67`
  - `badgeCanada` 加拿大勋章 — 枫红 `#B0413E`
- **背景母题**：像素点阵——稀疏小方格由暗至亮渐次点亮，右下角汇成一枚发光的「感光单元」。

### 第 6 步：幻灯片序列（10–16 页规划）【人物专属】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — CCD 之父 / Willard S. Boyle 1924–2011 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍/出生地/师承/任职/荣誉/核心领域）
03  核心贡献概览 — CCD / 红宝石激光 / 阿波罗 / Bell Labs 领导
04  早年：新斯科舍与家庭学校 (1924–1943) — 母亲教育、14 岁入学
05  海军岁月与 McGill (1943–1950) — 喷火战机航母降落、质谱 PhD
06  Bell Labs 前奏 (1953–1962) — 红宝石激光、Don Nelson、注入激光专利
07  阿波罗幕后 (1962–1964) — Bellcomm、登月点遴选
08  1969：CCD 诞生（核心贡献页，公式框放 CCD 电荷转移概念图式并注明）
09  "化学摄影死了" — Smith 语、数码相机时代
10  荣誉长廊 — Ballantine 1973 · Draper 2006 · Nobel 2009 · 加拿大勋章 2010
11  争议与回声 — Gordon/Tompsett 的署名之争（客观一句）
12  退休岁月与辞世 — Wallace 美术馆、2011 特鲁罗
13  遗产：人类视觉的延伸 — NASA 太空成像、诺奖演讲题词
14  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 得奖份额 | Boyle 与 Smith **共享 1/2**，Kao 独得另 1/2；勿写成「三人平分」或「Boyle 得一半的一半」 |
| 获奖理由 | 官方措辞 "for the invention of an imaging semiconductor circuit - the CCD sensor"；勿写成 "inventing the digital camera" |
| CCD 归属争议 | Gordon 与 Tompsett（已退休 Bell Labs 同事）主张 CCD 的摄影应用非 Boyle 首创（Wikinews 有 2009 诺奖争议条目）——立传可客观一句记录，**勿替任何一方背书**；Smith 名言 "After making the first couple of imaging devices, we knew for certain that chemistry photography was dead" 可引（page.md 有英文原文） |
| 红宝石激光 | 1962 与 Don Nelson 发明的是**首台连续运转**红宝石激光器（此前 Maiman 1960 为脉冲式——page.md 未载 Maiman，勿写）；「半导体注入激光器首件专利在列」是另一条事实，勿混为一谈 |
| 博士导师 | infobox 作 H. Watson（McGill 1950）；正文无更多叙述，勿杜撰全名或事迹 |
| 海军经历 | 1943 加入皇家加拿大海军、借调海军航空兵学航母降落喷火战机；是「学习」而非「参战飞行员」，措辞注意 |
| Bellcomm | 是 Bell Labs 子公司，Boyle 任空间科学与探索研究部主任（1962），1964 回 Bell Labs 本部；两段任职勿混 |
| 退休年份 | 1975–1979 任研究执行总监，1979 退休；勿写成「1975 退休」 |
| 卒因 | 肾病并发症，2011-05-07 逝于特鲁罗医院，享年 86 |
| 同名区分 | George E. Smith（CCD）勿与其他 Smith 混淆；Betty Boyle 是妻子（风景画家）非学术界人物 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| charge-coupled device (CCD) | 电荷耦合器件 | 1969 发明 |
| imaging semiconductor circuit | 成像半导体电路 | 诺奖理由原词 |
| ruby laser | 红宝石激光器 | 1962 连续运转首创 |
| semiconductor injection laser | 半导体注入激光器 | 首件专利在列 |
| Bellcomm | 贝尔康姆 | Bell Labs 子公司 |
| Executive Director of Research | 研究执行总监 | 1975–1979 |
| mass spectrometry | 质谱 | PhD 方向（Dempster 型） |
| Companion of the Order of Canada | 加拿大勋章同伴 | 2010 |
| Charles Stark Draper Prize | 德雷珀奖 | 2006，美国工程院 |
| Nobel lecture | 诺奖演讲 | 2009-12-08 "CCD – an Extension of Man's Vision" |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（明亮/轻快）
- **匹配理由**：「日光」正是 CCD 的日常写照——把每一缕光变成像素；明亮轻快基调匹配工业发明家务实乐观的气质与「人类视觉延伸」的正向叙事。
- **备选**：Awaken（突破/明亮）、Expedition（阿波罗探索感）。
- 批内不重复：本批 Kobayashi=The Invisible Light、Maskawa=Cinematic Experience、Kao=Shine Like The Sun、Smith=Ascension。

---

## 五、执行红线 【模板通用】

- 只收 page.md 明载的关系；yaml note 含 ": " 或以引号开头时整体单引号包裹。
- 对手方入库用规范名：H. Watson、George E. Smith（Kao 篇已建 stub，按 name_en 复用）、Charles Kuen Kao（库内 id=3022 复用）、Don Nelson、Betty Boyle、Eugene I. Gordon、Michael Francis Tompsett；不给对手方编造 qid。
- 禁止修改 generate_21st_century_list.py、名录 md、模板文件。
