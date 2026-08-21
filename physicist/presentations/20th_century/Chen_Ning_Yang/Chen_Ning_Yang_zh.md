# Chen Ning Yang（杨振宁）立传提示词

> 榜单：1957 诺贝尔物理学奖 · qid=Q181369 · 1922-10-01 – 2025-10-18 · 华裔美籍理论物理学家
> 本地 Wikipedia 数据源：`physicist/presentations/pages/20th_century/Chen_Ning_Yang/`（page.md + metadata.json，已下载）

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **标杆实例**：`20th_century/Kenneth_G_Wilson/`（完整成品，可对照）。
- **本实例**：Chen Ning Yang（杨振宁，英文惯称 C.N. Yang / Franklin Yang）。
- **设计哲学**：物理学家立传必须保留「身份信息页」（Identity / Bio 速览页）与「研究领域」的结构化表达——这是物理学家模板的骨架，务必保留。

## 二、背景信息【人物专属】

- **全名**：Chen Ning Yang（杨振宁；英文惯称 C.N. Yang / Franklin Yang）
- **生卒**：1922-10-01 生于安徽合肥 → 2025-10-18 逝于北京，享年 103
- **国籍（变迁）**：中华民国（1922–2015）→ 美国（1964–2015）→ 中华人民共和国（2015–2025，2015-04-01 正式放弃美国国籍）
- **身份**：华裔美籍理论物理学家（统计力学、规范场论、粒子物理、凝聚态物理）
- **气质关键词**：**规范场论的奠基人、对称性的大师、标准模型的先知** —— 1957 诺贝尔物理学奖获奖理由：
  > "for their penetrating investigation of the so-called parity laws which has led to important discoveries regarding the elementary particles"（对所谓宇称定律的深入考察，带来了关于基本粒子的重要发现，与李政道共同获奖）
- **设计母题**：**对称性（symmetry）**。杨-米尔斯理论的灵魂是「规范对称性决定相互作用」——与几何、群论、不变量天然对应，是比「粒子」更贴合杨振宁的视觉语言。
- **本地 Wikipedia**：`physicist/presentations/pages/20th_century/Chen_Ning_Yang/page.md`（第 0 步已下载）
- **参考模板**：
  - 物理学家标杆：`20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

## 三、任务流程【模板通用，逐步执行】

> 每完成一步汇报进度，遇到歧义先征求用户意见再继续。
> **数据库同步要求**：第 4 步（研究领域入库）与第 4.5 步（社会关系入库）写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面【人物专属】

- ✅ 已下载到 `pages/20th_century/Chen_Ning_Yang/`（page.md 57.8KB / page.html 592KB / metadata.json / images.txt）
- 事实基准（已从本地 page.md + metadata.json 提取核对）：
  - 生卒：1922-10-01 生于合肥 → 2025-10-18 逝于北京，享年 103（metadata 另有 1922-09-22 记录，infobox 采 10-01）
  - 国籍：中华民国(1922–2015) / 美国(1964–2015) / 中华人民共和国(2015–2025)
  - 父母：父杨武之（Ko-Chuen Yang，1896–1973，数学家）；母罗孟华（Luo Meng-hua）
  - 教育：西南联大 BS(1942，吴大猷指导分子光谱群论) → 国立清华 MS(1944，王竹溪指导统计力学) → 芝加哥大学 PhD(1948)
  - 博士导师：Edward Teller；其他学术顾问 Enrico Fermi（在芝加哥做 Fermi 助手一年）
  - 任职：芝加哥大学(Fermi 助手 1948-49) → 普林斯顿高等研究院 IAS(1949 受邀，1952 永久成员，1955 正教授) → 石溪分校(1965，Albert Einstein 讲座教授 + 理论物理研究所首任所长) → 清华大学(1999 退休后回京，高等研究中心首位黄汲清-陆启铿讲席教授)
  - 关键荣誉：Nobel 1957、Rumford Prize 1980、National Medal of Science 1986、Oskar Klein 奖 1988(首位)、Benjamin Franklin Medal 1993、Bower Award 1994、Albert Einstein Medal 1995、Lars Onsager Prize 1999、King Faisal Prize 2001
  - 婚姻：杜致礼(1950–2003)、翁帆(2005)
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 个节点）

### 第 1 步：建立目录【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Chen_Ning_Yang/` 与 `images/`。

### 第 2 步：复制 Makefile【模板通用】

- 复制 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Chen_Ning_Yang_zh`、`VIDEO_NAME=Chen_Ning_Yang_zh`。

### 第 3 步：收集图片【人物专属】

- 下载 Wikipedia infobox 肖像（`page.md` 中 1976 年照片或 1957 年照片）到 `images/`。

### 第 4 步：研究领域梳理 + 入库【模板通用，人物专属内容】

**杨振宁的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | gauge theory / Yang–Mills theory | 规范场论 | 杨-米尔斯理论(1954)，标准模型基石 | 封面、核心页 |
| 1 | parity violation (weak interaction) | 宇称不守恒 | 1957 诺奖核心，与李政道 | 核心页 |
| 2 | statistical mechanics | 统计力学 | Lee-Yang 定理、Yang-Baxter 方程、ODLRO | 统计页 |
| 3 | particle physics | 粒子物理 | Fermi-Yang 模型、Wu-Yang monopole | 粒子页 |

### 第 4.5 步：社会关系梳理 + 入库【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Edward Teller | 师→生（博士导师） | 芝加哥大学博士导师，氢弹之父 |
| advisor-student | Enrico Fermi | 师→生（学术顾问） | 芝加哥做 Fermi 助手一年 |
| colleague | Robert Mills | 无向 | 1954 杨-米尔斯理论合作者（核心思想属杨） |
| co-honored | Tsung-Dao Lee | 无向 | 1957 诺奖共同得主 |
| colleague | Tai Tsun Wu | 无向 | Wu-Yang monopole / Wu-Yang dictionary |
| colleague | Nina Byers | 无向 | Byers-Yang 定理（磁通量子化） |
| colleague | Kerson Huang | 无向 | Lee-Huang-Yang 修正（弱相互作用玻色气体） |
| colleague | Reinhard Oehme | 无向 | CPT 对称（1957） |
| spouse | 杜致礼 | 无向 | 1950–2003 |
| spouse | 翁帆 | 无向 | 2005 至今 |

**门生**：Bill Sutherland、Brosl Hasslacher、Alexander Wu Chao。

### 第 5 步：设计配色方案【人物专属】

- **气质**：对称性、深邃、跨越统计力学到规范场论。
- **配色**：深靛蓝（对称性/理论深度）+ 香槟金（诺奖）+ 四分类色
  - `badgeGauge` 规范场论 — 靛蓝 `#4C5FD5`
  - `badgeParity` 宇称不守恒 — 青绿 `#0E7C7B`
  - `badgeStat` 统计力学 — 琥珀 `#E07B30`
  - `badgeParticle` 粒子物理 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「对称性 / 规范不变性」的视觉语言。

### 5.1 物理学家格式硬要求【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自本地 Wikipedia infobox，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；GitHub 链接由首页模板 `\input` 继承；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 规范场论的奠基人 / 杨振宁 1922–2025 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格
03  核心贡献概览 — 规范场论 / 宇称不守恒 / 统计力学 / 粒子物理
04  早年与教育 (1922–1948) — 合肥出生、西南联大、清华硕士、芝加哥博士
05  杨-米尔斯理论 (1954) — 非阿贝尔规范场论、标准模型基石
06  宇称不守恒 (1956) — 与李政道、吴健雄实验、1957 诺奖
07  统计力学贡献 — Lee-Yang 定理、Yang-Baxter 方程、ODLRO、Byers-Yang
08  规范场的拓扑 — Wu-Yang monopole、Wu-Yang dictionary
09  十三项开创性贡献 — 清华黑方块（2012）
10  学术传承与回国 — 石溪、清华、Chern 数学研究所
11  荣誉与晚年 — 诺奖、回国定居、103 岁
12  结尾
```

### 第 7 步：编写 Beamer 源码【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）整体复用 `Physicist_Bio_Prompt_Template.md` 第四章骨架。

### 第 8 步：布局检查【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查【人物专属】

**杨振宁特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 杨-米尔斯理论归属 | 1954 与 Robert Mills 合作，**核心思想属杨振宁**（Mills 亲述"关键想法是杨的"），但勿写"独自发明"，需提 Mills |
| 宇称不守恒归属 | 与李政道共同提出，**吴健雄实验证实但未获诺奖**（诺奖委员会历史争议），勿写"杨独自提出" |
| 诺奖理由 | 官方措辞针对"宇称定律的深入考察"，**不是**因杨-米尔斯理论获奖，勿混淆 |
| 出生日期 | metadata 有 1922-10-01 与 1922-09-22 两条，**infobox 采 10-01**，以 10-01 为准 |
| 博士导师 | metadata `doctoral_advisor` 为 Edward Teller；Fermi 是"其他学术顾问"（芝加哥做其助手一年），勿写"Fermi 是博士导师" |
| 国籍变迁 | 1922–2015 中华民国 → 1964–2015 美国 → 2015 放弃美籍入中国籍，**时间线精确** |
| 首位华人诺奖 | 与李政道**并列**首届华人诺奖得主，勿写"杨独自是首位" |
| 石溪研究所命名 | 退休后理论物理研究所改名 C. N. Yang Institute for Theoretical Physics，勿遗漏 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Yang–Mills theory | 杨-米尔斯理论 | 非阿贝尔规范场论，勿译"杨-密尔" |
| parity violation | 宇称不守恒 | 与"宇称守恒"区分 |
| gauge theory | 规范场论 | 对称性决定相互作用 |
| Lee–Yang theorem | 李-杨定理 | 相变理论，与李政道共同 |
| Yang–Baxter equation | 杨-巴克斯特方程 | 可积系统 |
| ODLRO | 非对角长程序 | 宏观量子现象 |
| Wu–Yang monopole | 吴-杨磁单极子 | 无 Dirac 弦，与吴大峻 |
| CPT symmetry | CPT 对称 | 电荷-宇称-时间反演 |

## 四、背景音乐选择【人物专属】

- **气质**：对称性、深刻、奠基（杨-米尔斯是标准模型的长期纲领）。
- **首选曲目**：**Timeless** — Alex-Productions（沉稳/纪录片/长期纲领）
  - 理由：杨-米尔斯规范对称性不是单一突破，而是贯穿现代粒子物理的**长期纲领**——与 Timeless 的"永恒/纲领"气质匹配；杨振宁气质偏深沉、内敛，103 岁高龄跨越近一个世纪的物理史。
- **备选**：
  - Awaken / Daylight — "天才之光"，匹配 30 多岁获诺奖的年轻突破（模板 5.3 推荐杨振宁用此）
  - Expedition — "远征式叙事"，匹配从中国到普林斯顿、从统计力学到规范场论的理论探索
- **本地路径**：`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → `20th_century/Chen_Ning_Yang/Timeless.wav`
- **时长**：128 秒 > 12 页 × 7 秒 ≈ 84 秒 → ffmpeg `-shortest` 自动对齐

## 第 9.5 步：Review 完成后更新名单状态 ★

> **两轮 Review 全部完成后，必须同步更新总名单的「Review」列**，否则名单会一直停留在 🔲。

- 编辑 `physicist/generate_20th_century_list.py`，将杨振宁姓名加入 `BIOGRAPHIES_DONE`（立传）与 `REVIEWS_DONE`（Review）集合：
  ```python
  BIOGRAPHIES_DONE = {..., "Chen Ning Yang"}
  REVIEWS_DONE = {..., "Chen Ning Yang"}
  ```
- 重新生成名单：
  ```bash
  cd physicist && python3 generate_20th_century_list.py
  ```
- 校验：名单中杨振宁行应为 `| ✅ | ✅ |`，统计区「已立传」「已 Review」计数 +1。

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/pages/20th_century/Chen_Ning_Yang/page.md` | 本地 Wikipedia 正文 |
| `physicist/presentations/pages/20th_century/Chen_Ning_Yang/metadata.json` | Wikidata 结构化元数据 |
| `20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 标杆实例 Beamer 源码 |
| `20th_century/Physicist_Bio_Prompt_Template.md` | 通用提示词模板 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**

---

## Review-1 记录 (2026-08-21)

> 结合本地 Wikipedia (`pages/20th_century/Chen_Ning_Yang/page.md` + `metadata.json`) 逐页比对。

- **头像** ✅：`images/Yang.jpg`（Wikipedia "Yang in 1957" 照片，250×354 竖版，已下载）。封面右上角圆角裁剪 + 姓名注 "Yang, 1957"；身份信息页左侧竖版裁剪 + "Chen Ning Yang (1957)"。
- **国籍** ✅：封面底部 `中国（原美国）`，身份信息页 `中国（原美国·中华民国）`（Wikipedia Citizenship: ROC 1922–2015 → US 1964–2015 → PRC 2015–2025）。
- **身份信息页** ✅：Slide 2 存在，涵盖生卒/本名/国籍/师承/任职/荣誉/核心领域，符合 Wilson 模板硬性要求。
- **生卒**：1922-10-01 ~ 2025-10-18（103 岁），与 Wikipedia infobox + 正文一致（metadata 另含 1922-09-22 旧历，正文统一用 10-01）。
- **家庭**：父杨武之（Ko-Chuen Yang，1896–1973，数学家）、母罗孟华——与 Wikipedia 一致；tex 用"杨武之"（Wikipedia 汉字误作"楊克純"，tex 更准确）。
- **教育轨迹**：北平中小学 → 1937 合肥 → 1938 昆明西南联大 → 1942 BS（吴大猷·群论分子光谱）→ 1944 MS（清华·王竹溪·统计力学）→ 庚款留美 → 1946 芝加哥 → 1948 PhD（Teller）——全部准确。
- **核心贡献复核**：杨-米尔斯 1954（核心思想属杨，Mills 亲述）/ 宇称不守恒 1956（与李政道，吴健雄实验证实，Telegdi–Friedman、Garwin–Lederman 独立确认，1957 诺奖）/ 李-杨定理 1952 / 李-黄-杨修正 1957 / Byers–Yang 1961 / ODLRO 1962 / Yang–Baxter 1967 / Wu–Yang 磁单极子+词典 1975 / 积分形式 1974——全部准确，无杜撰。
- **13 项贡献**（2012 清华黑方块）：统计力学 4 项、凝聚态 2 项、粒子物理 4 项、场论 3 项，与 Wikipedia "13 seminal contributions" 逐一吻合。
- **生涯与荣誉**：石溪 1965–1999（Einstein 讲座教授、首任所长）→ 1999 退休回国清华 → 2015 弃美籍；Nobel 1957 / Rumford 1980 / 国家科学奖章 1986 / Oskar Klein 1988（首位得主）/ 爱因斯坦奖章 1995 / Onsager 1999 / King Faisal 2001 / Marcel Grossmann 2015；1955 APS 会士、1958 中央研究院院士、皇家学会/俄科院/美科院院士——全部准确。
- **门生**：Bill Sutherland (1968)、Brosl Hasslacher (1972)、Alexander Wu Chao (1974)，1986 应陈省身之邀建陈省身数学研究所理论物理分部——与 Wikipedia 一致。
- **编译**：`make` → ✅ 13 页，0 错误。

## Review-2 记录 (2026-08-21)

> 结构优化 + Overfull 检查 + 编译验证。

- **Overfull 现状**：`xelatex` 两遍编译后，Overfull 为 hbox 6.03pt / 5.85pt / 4.16pt + vbox 1.17pt，全部 **<10pt 可接受**。
  - line 235/236：结尾页 22pt 大字号金句「对称性，」「是相互作用的源泉。」——居中文本，溢出向两侧各约 1mm，不可见，保留 22pt 醒目字号。
  - line 242：共享封面模板 `openphysicist_page.tex` 的 `\openphysicistslide`——共享资源，不在本 tex 内改动。
- **肖像**：`keepaspectratio` 下封面 2.0×2.8cm、身份页 3.0×3.9cm 均正常缩放，无变形。
- **中文标点/断行**：全角引号、破折号、`\quad` 间距统一，与 Wilson 标杆一致。
- **编译**：`make distclean && make` → ✅ 13 页，169 比例，肖像已嵌入，中文渲染正常。

> 结论：两轮 Review 通过，无需事实修正；Overfull 均在可接受范围内。
