# 物理学家立传提示词（人物专属：Wilhelm Wien）

> 本文件是 OpenPhysicist 20 世纪诺贝尔物理学奖批量立传的**人物专属提示词**，结构对齐标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按完成步骤汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Wilhelm Wien（威廉·维恩），1911 年诺贝尔物理学奖得主，热辐射定律（维恩位移定律/维恩分布定律）与维恩滤波器的提出者，量子论前夜的摆渡人。
- **设计哲学**：保留物理学家模板两大骨架——「身份信息页」与「研究领域结构化表达」；本人物的设计重心是**量子论的前夜**：维恩定律"错得刚刚好"——它在高频有效、它在绝热不变量论证中通向普朗克，旧理论与新量子的接棒点。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Wilhelm Carl Werner Otto Fritz Franz Wien（1864-01-13 ~ 1928-08-30，享年 64 岁）
- **气质关键词**：**热辐射的度量者、量子论前夜的路标、经典—量子的摆渡人**
- **官方获奖理由（禁止改写）**：
  > "for his discoveries regarding the laws governing the radiation of heat"（因其关于热辐射规律的各项发现）
- **设计母题**：**辐射峰随温度滑移（displacement）**——黑体谱峰随温度升高向短波移动；视觉语言用黑体谱曲线族与 λ_max 标记点。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Wilhelm_Wien/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；首页 `cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ⏳ **待下载** `https://en.wikipedia.org/wiki/Wilhelm_Wien` 到 `{Dir}/Wilhelm_Wien.html`（本地暂只有 `page.md`）
- **事实基准**：
  - 生卒（1864-01-13 生于普鲁士加夫肯 Gaffken（今俄罗斯 Parusnoye） ~ 1928-08-30 卒于慕尼黑，享年 64；全名五段式 Wilhelm Carl Werner Otto Fritz Franz Wien）
  - 家庭（地主 Carl Wien 之子；1866 迁 Drachenstein（今 Smokowo）；表兄 Max Wien 为维恩电桥发明者——**勿混淆**）
  - 教育（1879 Rastenburg 就学 → 1880-82 海德堡市立中学 → 1882 格丁根大学+柏林大学 → 1883-85 在 Helmholtz 实验室工作 → 1886 以光在金属上的衍射及材料对折射光颜色影响的论文获柏林大学博士）
  - 任职（1896-99 亚琛工业大学讲师 → 1900 接替伦琴任维尔茨堡大学教授 → 1920 接替伦琴任慕尼黑大学教授；另曾任职吉森大学；**两度接任 Wilhelm Röntgen 的教席**）
  - 关键荣誉（Nobel 1911；巴伐利亚马克西米利安科学与艺术勋章；Guthrie Lecture；法兰克福物理协会荣誉会员；1913 哥伦比亚大学 Ernest Kempton Adams 讲座）
  - 知名学生（博士生：Arthur Jeffrey Dempster、Gabriel Gabrielsen Holtsmark、Eduard Rüchardt、Lars Vegard）
  - 核心贡献清单：
    1. 维恩位移定律（λ_max·T = constant，至今常用）
    2. 维恩分布定律（1896，高频黑体辐射，Wien–Planck law 先声）
    3. 绝热不变量论证（通向普朗克定律与量子论）
    4. 维恩滤波器（1898，正交电磁场速度选择器）
    5. 阳极射线类氢正粒子（1898，质谱法基础/质子前史）
    6. 电磁质量关系 m=(4/3)E/c²（1900，继 Searle）
  - 诺奖演讲（注记）：1911-12-11 *On the Laws of Thermal Radiation*
  - 核心时间线（1864 生 → 1882 格丁根/柏林 → 1883-85 Helmholtz 实验室 → 1886 博士 → 1896 维恩分布定律 → 1898 维恩滤波器+阳极射线中发现类氢正粒子 → 1900 维尔茨堡+电磁质量论文 m=(4/3)E/c² → 1900-01 普朗克定律接力 → 1911 诺贝尔奖 → 1913 Columbia 讲座 → 1920 慕尼黑 → 1928 卒）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下已有 `Wilhelm_Wien/`（本提示词所在），需新建 `images/` 子目录存放肖像与插图

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆目录 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Wilhelm_Wien_zh`、`VIDEO_NAME=Wilhelm_Wien_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：page.md 内嵌 "Wien in 1911" infobox 像；优先 Commons `Special:FilePath/Wilhelm Wien 1911.jpg?width=500`
- 404/HTML 则经 Wikipedia REST API `page/summary` 查 infobox 原图名再抓；再失败用装饰圆占位（主色边框圆 + 姓名缩写）
- 插图建议：黑体谱曲线族 λ_max 滑移示意（可 TikZ 绘制，勿用网图冒充史料照片）

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | thermal radiation | 热辐射 | 位移定律/分布定律，1911 诺奖核心 | 核心页 |
| 1 | thermodynamics | 热力学 | 绝热不变量论证 | 原理页 |
| 2 | electromagnetism | 电磁学 | 电磁质量、运动体电动力学 | EM 页 |
| 3 | mass spectrometry | 质谱法 | 1898 类氢正粒子，奠基质谱 | 质子前史页 |
| 4 | optics | 光学 | 博士论文：衍射与色散 | 早年页 |

入库：`MySQL/data/Wilhelm_Wien.yaml`（已备好，`cd MySQL && python3 seed_person.py data/Wilhelm_Wien.yaml`）。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hermann von Helmholtz | 师→生 | 柏林大学博士导师，1886 衍射论文 |
| advisor-student | Arthur Jeffrey Dempster | 维恩→学生 | 博士生 |
| advisor-student | Gabriel Gabrielsen Holtsmark | 维恩→学生 | 博士生 |
| advisor-student | Eduard Rüchardt | 维恩→学生 | 博士生 |
| advisor-student | Lars Vegard | 维恩→学生 | 博士生 |
| colleague | Max Planck | 无向 | 同事，在其定律基础上提出普朗克定律 |
| colleague | Wilhelm Conrad Röntgen | 无向 | 两度接任其教席（1900 维尔茨堡、1920 慕尼黑） |

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：辐射谱、温度、前夜
- **配色**：热辐射暗红（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 — 热辐射暗红 `#6E2B2B`
  - `badgeWien` 维恩位移定律 — `#D9822B`
  - `badgeQuantum` 黑体辐射与量子前夜 — `#3D5A80`
  - `badgeFilter` 维恩滤波器 — `#517A6E`
  - `badgeProton` 阳极射线与质子前史 — `#7A3B5E`
- **背景母题**：稀疏黑体谱曲线族（不同温度）+ λ_max 滑移标记点，呼应"峰值随温度移动"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素（维恩：德国 | 慕尼黑大学 | Nobel 1911）。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名（Wilhelm Carl Werner Otto Fritz Franz Wien，五段式全名）、国籍、出生地（加夫肯）、师承（Helmholtz）、任职（两度接任伦琴）、主要荣誉、核心领域。事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 热辐射定律的度量者 / Wilhelm Wien 1864–1928 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含五段式全名注记）
03  核心贡献概览 — 位移定律 / 分布定律 / 维恩滤波器 / 质子前史
04  东普鲁士地主之子 (1864–1882) — Gaffken、Drachenstein、Rastenburg、海德堡
05  Helmholtz 实验室与博士 (1883–1886) — 衍射与色散
06  1896：维恩分布定律 — 高频有效、低频低估（维恩近似）
07  维恩位移定律（核心贡献页，公式框 λ_max·T = constant）
08  普朗克的接力 — 维恩–普朗克定律→普朗克定律→量子论（按 page 原口径客观呈现）
09  1898：维恩滤波器 — 正交电场磁场速度选择器
10  阳极射线与质子前史 — 类氢正粒子→J.J. Thomson 1913 改进→Rutherford 1919 后得名
11  电磁质量 — m = (4/3)E/c²（继 Searle），按 page 口径注"后为相对论超越"则仅一句客观
12  两度接任伦琴 — 维尔茨堡 1900、慕尼黑 1920；亚琛/吉森岁月
13  1911 诺贝尔物理学奖 — 官方理由原句 + 1913 Columbia 讲座
14  科学政治与晚年 — 保守民族主义立场但未至 Deutsche Physik、敬重爱因斯坦与相对论；1928 卒于慕尼黑
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`；头部宏（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用标杆骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Wien 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 忠实英文原句 "for his discoveries regarding the laws governing the radiation of heat"（1911），勿写成"量子论先驱奖"或"发现维恩定律" |
| 两条定律勿混 | **位移定律**（λ_max·T=const）至今常用；**分布定律**（Wien approximation）仅高频有效、低频低估被普朗克定律取代——叙事分页呈现 |
| 普朗克接力 | page 口径：Planck 用电磁学+热力学给维恩定律理论基底（Wien–Planck law）→ 修正为 Planck's law → 量子论；勿写成"维恩创立量子论"或"普朗克推翻维恩" |
| 质子前史 | 1898 发现的是**质量≈氢原子的正粒子**；质子之名是 Rutherford 1919 工作之后才确立——禁写"维恩发现质子" |
| 电磁质量 | m=(4/3)E/c²（继 Searle 思路）系数 4/3 勿丢；禁写成 E=mc²；是否加"后为相对论取代"仅限一句客观注记 |
| 同名区分 | 表兄 Max Wien（Wien bridge）是工程师——身份页/陷阱页须区分；维恩本人勿与 Wien 效应、Wien 城市名混 |
| 全名 | 五段式全名仅身份页展示一次，勿每页重复 |
| 科学政治 | 保守民族主义、未到 Deutsche Physik 立场、尊重爱因斯坦与相对论——page 明载可写，客观一句，禁延伸评论 |
| 教席叙事 | "两度接任伦 rhein 伦琴教席"（1900 Würzburg / 1920 München）——勿写成"伦琴的学生" |
| 博士生标签 | Dempster 等 4 人 page 仅列名，note 只写"博士生"，禁追加"质谱仪发明者"等外部标签 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Wien's displacement law | 维恩位移定律 | λ_max·T = constant |
| Wien approximation | 维恩分布定律（维恩近似） | 高频/短波有效 |
| black-body radiation | 黑体辐射 | 1911 诺奖主题 |
| adiabatic invariance | 绝热不变量 | 维恩论证的根据 |
| Wien filter | 维恩滤波器（速度选择器） | 正交电磁场 |
| anode rays | 阳极射线 | 类氢正粒子来源 |
| electromagnetic mass | 电磁质量 | m=(4/3)E/c² |
| heat radiation | 热辐射 | 获奖理由用词 |
| diffraction | 衍射 | 博士论文主题 |
| proton | 质子 | 命名在其发现之后 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（时间感 / 纪录片，56k views）
- **匹配理由**：维恩是"经典走向量子"的时间接棒点——位移定律本身就是温度与波长的换算；"时间感/纪录片"匹配其从东普鲁士到慕尼黑、从经典电磁到量子前夜的演进叙事。
- **本地路径**：`music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`
- **备选**（未采用）：
  - ★★ The Invisible Light — "纪录片/稳重"匹配辐射谱叙事，但本批已分配给 Braun
  - ★ Nostalgia — "怀旧"匹配经典时代的落幕，但"前夜摆渡"更需要时间推进感而非回望感
- **时长核验**：曲目时长 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐
- **备注**：批内 BGM 去重——Lippmann=Shine Like The Sun、Marconi=SEA、Braun=The Invisible Light、van der Waals=Eternals。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Wilhelm_Wien/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Wilhelm_Wien.yaml` | 入库 yaml（已按本提示词 §4/§4.5 备好） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
