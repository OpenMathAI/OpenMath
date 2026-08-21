# Tsung-Dao Lee（李政道）立传提示词

> 榜单：1957 诺贝尔物理学奖 · qid=Q183679 · 1926-11-24 – 2024-08-04 · 华裔美籍理论物理学家
> 本地 Wikipedia 数据源：`physicist/presentations/pages/20th_century/Tsung-Dao_Lee/`（page.md + metadata.json，已下载）

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **标杆实例**：`20th_century/Kenneth_G_Wilson/`（完整成品，可对照）。
- **本实例**：Tsung-Dao Lee（李政道；英文惯称 T.D. Lee）。
- **设计哲学**：物理学家立传必须保留「身份信息页」（Identity / Bio 速览页）与「研究领域」的结构化表达——这是物理学家模板的骨架，务必保留。

## 二、背景信息【人物专属】

- **全名**：Tsung-Dao Lee（李政道；英文惯称 T.D. Lee）
- **生卒**：1926-11-24 生于上海 → 2024-08-04 逝于美国旧金山，享年 97
- **国籍**：中华民国 → 美国（1963 入籍）；华裔美籍
- **身份**：华裔美籍理论物理学家（粒子物理、统计力学、天体物理、格点 QCD）
- **气质关键词**：**宇称不守恒的年轻天才、跨界探索者、中美物理教育的桥梁** —— 1957 诺贝尔物理学奖（与杨振宁共同获奖，获奖时仅 30 岁，二战后最年轻科学诺奖得主）：
  > "for their penetrating investigation of the so-called parity laws which has led to important discoveries regarding the elementary particles"（对所谓宇称定律的深入考察，带来了关于基本粒子的重要发现）
- **设计母题**：**对称性的破缺（symmetry breaking）**。宇称不守恒的本质是「自然界并不总是左右对称」——与镜像、不对称、破缺结构天然对应，是比「粒子」更贴合李政道的视觉语言。
- **本地 Wikipedia**：`physicist/presentations/pages/20th_century/Tsung-Dao_Lee/page.md`（第 0 步已下载）
- **参考模板**：
  - 物理学家标杆：`20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

## 三、任务流程【模板通用，逐步执行】

> 每完成一步汇报进度，遇到歧义先征求用户意见再继续。
> **数据库同步要求**：第 4 步（研究领域入库）与第 4.5 步（社会关系入库）写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面【人物专属】

- ✅ 已下载到 `pages/20th_century/Tsung-Dao_Lee/`（page.md 59.8KB / page.html 304KB / metadata.json / images.txt）
- 事实基准（已从本地 page.md + metadata.json 提取核对）：
  - 生卒：1926-11-24 生于上海 → 2024-08-04 逝于旧金山，享年 97（metadata 另有 1926-11-25 记录，infobox 采 11-24）
  - 国籍：中华民国 → 美国（1963 入籍）
  - 家庭：父李骏康（化学实业家，金陵大学早期毕业生）；祖父李仲覃（苏州圣约翰堂首位华人卫理公会主任牧师）；兄 Robert C. T. Lee（教育家）
  - 教育：浙江大学(1943 化工系转物理系，舒星北、王淦昌指导) → 西南联大(1945，吴大猷) → 芝加哥大学 PhD(1950，Fermi，白矮星氢含量)
  - 博士导师：Enrico Fermi
  - 任职：UC Berkeley(1950-51 研究助理/讲师) → 哥伦比亚大学(1953 加入，至 2012 退休，校聘教授 emeritus) → RIKEN-BNL 研究中心主任(1997-2003)
  - 关键荣誉：Nobel 1957、Albert Einstein 奖 1957、Guggenheim 1966、Galileo Galilei Medal 1979、Oskar Klein 1993、Matteucci Medal 1995、小行星 3443 命名 1997
  - 婚姻：秦惠䇹(1950–1996)
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 个节点）

### 第 1 步：建立目录【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Tsung-Dao_Lee/` 与 `images/`。

### 第 2 步：复制 Makefile【模板通用】

- 复制 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Tsung-Dao_Lee_zh`、`VIDEO_NAME=Tsung-Dao_Lee_zh`。

### 第 3 步：收集图片【人物专属】

- 下载 Wikipedia infobox 肖像（`page.md` 中 1956 年照片或 2006 年清华会议照片）到 `images/`。

### 第 4 步：研究领域梳理 + 入库【模板通用，人物专属内容】

**李政道的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | parity violation (weak interaction) | 宇称不守恒 | 1957 诺奖核心，与杨振宁 | 封面、核心页 |
| 1 | particle physics | 粒子物理 | Lee model、KLN 定理、高能中微子 | 核心页 |
| 2 | statistical mechanics | 统计力学 | Lee-Yang 定理、相变理论 | 统计页 |
| 3 | nontopological solitons / RHIC physics | 非拓扑孤子 / RHIC | 孤子星、高密度物质 | 孤子页 |

### 第 4.5 步：社会关系梳理 + 入库【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Enrico Fermi | 师→生（博士导师） | 芝加哥大学博士导师，1938 诺奖得主 |
| co-honored | Chen Ning Yang | 无向 | 1957 诺奖共同得主，共发表 32 篇论文 |
| colleague | Michael Nauenberg | 无向 | KLN 定理（1964，零质量粒子发散） |
| colleague | Richard M. Friedberg | 无向 | 薛定谔方程新解法、中微子矩阵 |
| colleague | Chien-Shiung Wu | 无向 | 吴健雄实验证实宇称不守恒（吴未获诺奖） |
| spouse | 秦惠䇹（Jeannette Hui-Chun Chin） | 无向 | 1950–1996 |

**门生**：Norman Christ、Richard M. Friedberg、Gerald Feinberg。

### 第 5 步：设计配色方案【人物专属】

- **气质**：年轻天才、跨界探索、宇称破缺。
- **配色**：深青蓝（破缺/深度）+ 香槟金（诺奖）+ 四分类色
  - `badgeParity` 宇称不守恒 — 青绿 `#0E7C7B`
  - `badgeParticle` 粒子物理 — 靛蓝 `#4C5FD5`
  - `badgeStat` 统计力学 — 琥珀 `#E07B30`
  - `badgeSoliton` 孤子/天体物理 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「对称性的破缺 / 镜像不对称」的视觉语言。

### 5.1 物理学家格式硬要求【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自本地 Wikipedia infobox，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；GitHub 链接由首页模板 `\input` 继承；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 宇称不守恒的年轻天才 / 李政道 1926–2024 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格
03  核心贡献概览 — 宇称不守恒 / 粒子物理 / 统计力学 / 孤子与天体物理
04  早年与教育 (1926–1950) — 上海出生、浙大、西南联大、芝加哥 Fermi 门下
05  宇称不守恒 (1956) — 与杨振宁、吴健雄实验、1957 诺奖、30 岁
06  Lee-Yang 定理与统计力学 (1952) — 相变理论
07  Lee model 与粒子物理 — 可解场论模型、KLN 定理、高能中微子
08  非拓扑孤子与孤子星 — RHIC 物理、高密度物质形态
09  格点 QCD 与超级计算 — QCDSP / QCDOC
10  CUSPEA 与教育贡献 — 中美物理桥梁、䇹政学者
11  荣誉与晚年 — 哥伦比亚退休、97 岁
12  结尾
```

### 第 7 步：编写 Beamer 源码【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）整体复用 `Physicist_Bio_Prompt_Template.md` 第四章骨架。

### 第 8 步：布局检查【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查【人物专属】

**李政道特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 宇称不守恒归属 | 与杨振宁共同提出，**吴健雄实验证实但未获诺奖**（诺奖委员会历史争议），勿写"李独自提出" |
| 最年轻诺奖表述 | 二战后最年轻科学诺奖得主（30 岁），历史上**第三年轻**（Bragg 25、Heisenberg 30），勿写"史上最年轻" |
| 博士导师 | Enrico Fermi（芝加哥大学），博士论文《白矮星的氢含量》 |
| Lee model | 1953 哥伦比亚大学早期可解量子场论模型，勿与"李-杨定理"混淆 |
| KLN 定理 | 与 Kinoshita、Nauenberg 共同（1964），勿写"李独自" |
| CUSPEA | 中美物理考试（China-U.S. Physics Examination and Application），教育贡献，勿遗漏 |
| 出生日期 | metadata 有 1926-11-24 与 1926-11-25 两条，**infobox 采 11-24**，以 11-24 为准 |
| 配偶 | 秦惠䇹（1950–1996 去世），1998 年设立䇹政基金纪念之 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| parity violation | 宇称不守恒 | 与"宇称守恒"区分 |
| Lee–Yang theorem | 李-杨定理 | 相变理论，与杨振宁共同 |
| Lee model | 李模型 | 可解量子场论模型 |
| KLN theorem | KLN 定理 | Kinoshita-Lee-Nauenberg |
| nontopological solitons | 非拓扑孤子 | 与拓扑孤子区分 |
| soliton stars | 孤子星 | 孤子星天体物理 |
| RHIC physics | 相对论重离子对撞物理 | 高密度物质 |
| CUSPEA | 中美物理考试 | 教育项目 |

## 四、背景音乐选择【人物专属】

- **气质**：年轻天才、跨界探索、宇称破缺的突破。
- **首选曲目**：**Awaken / Daylight** — Alex-Productions（明亮轻快/天才之光）
  - 理由：30 岁即获诺奖（二战后最年轻科学诺奖得主），宇称不守恒是"年轻天才改写物理史"的突破，明亮轻快的曲风匹配其天才气质。
- **备选**：
  - Expedition — "远征式叙事"，匹配从粒子物理到天体物理、从统计力学到格点 QCD 的跨界探索
  - Timeless — "长期纲领"，匹配 Lee-Yang 定理、KLN 定理等贯穿现代物理的贡献
- **本地路径**：`music_audio/alex-productions/` 下选定曲目 → `20th_century/Tsung-Dao_Lee/`
- **时长**：12 页 × 7 秒 ≈ 84 秒 → ffmpeg `-shortest` 自动对齐

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/pages/20th_century/Tsung-Dao_Lee/page.md` | 本地 Wikipedia 正文 |
| `physicist/presentations/pages/20th_century/Tsung-Dao_Lee/metadata.json` | Wikidata 结构化元数据 |
| `20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 标杆实例 Beamer 源码 |
| `20th_century/Physicist_Bio_Prompt_Template.md` | 通用提示词模板 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**

---

## Review-1 记录 (2026-08-21)

> 结合本地 Wikipedia (`pages/20th_century/Tsung-Dao_Lee/page.md` + `metadata.json`) 逐页比对。

- **头像** ✅：`images/Lee.jpg`（Wikipedia infobox 照片 "TD Lee.jpg"，即 "Lee in 1956"，280×396 竖版），用户已手工确认无误。
- **生卒**：1926-11-24 ~ 2024-08-04（享年 97），与 Wikipedia 一致（infobox Born 1926-11-24，Died 2024-08-04 aged 97）。
- **出生/去世地**：上海 → 旧金山（San Francisco），与 Wikipedia 一致。
- **国籍**：美国（原中华民国）；Wikipedia infobox nationality 为 China (1912–1949) / United States，1963 入籍美国。
- **家庭**：父李骏康（李駿康，金陵大学首批毕业生、化学实业家）、祖父李仲覃（李仲覃，苏州圣约翰堂首位华人卫理公会主任牧师）——全部准确。
- **教育轨迹**：上海东吴附中 + 江西联中（未获中学文凭）→ 1943 直接考入浙大（初入化工系转物理，舒星北、王淦昌指导）→ 1945 转西南联大师从吴大猷 → 1946 赴芝加哥大学师从 Fermi → 1950 博士《白矮星的氢含量》——准确。
- **核心贡献复核**：宇称不守恒 1956（与杨振宁、吴健雄实验证实、Steinberger 组先做超子检验、吴未获奖的争议）/ Lee-Yang 定理 1952 / Lee model 1953（哥大第一项工作，可解 QFT 模型）/ KLN 定理 1964 / 非拓扑孤子 1975 / 孤子星 / RHIC 物理 1974-75 / 时间离散化 1983——全部准确。
- **荣誉清单**：Nobel 1957、爱因斯坦奖 1957、Guggenheim 1966、Galileo Galilei 1979、意大利共和国功绩勋章 1986、Oskar Klein 1993、Matteucci 1995、小行星 3443 命名 1997、Marcel Grossmann 2015——与 Wikipedia 逐一吻合。
- **任职**：UC Berkeley 1950-51（research associate/lecturer）→ Columbia 1953-2012（退休）→ RIKEN-BNL 1997-2003（主任）。
- **最年轻诺奖表述**：Wikipedia 明确 "third-youngest in sciences after Bragg (25) and Heisenberg (also at 30)"，即史上第三年轻，Bragg 25 岁、Heisenberg 亦 30 岁——准确。
- **编译**：`make` → ✅ 13 页，0 错误。

### 🔴 事实性错误（已修复）

| # | 位置 | 当前内容 | 问题 | 修正 |
|---|------|------|------|------|
| 1 | 早年教育页 | 1946 年经**吴健雄**推荐获奖学金赴芝加哥大学 | Wikipedia "Professor Wu nominated Lee for a Chinese government fellowship" 中的 Wu 指代前文正文的 **吴大猷（Wu Ta-You）**（西南联大导师），非图片注中的吴健雄 | 改为"经**吴大猷**推荐" |

## Review-2 记录 (2026-08-21)

> 结构优化 + Overfull 检查 + 编译验证。

- **Overfull 现状**：`xelatex` 两遍编译后，Overfull 为 hbox 6.08pt + vbox 1.17pt，全部 **<10pt 可接受**。
  - line 234：结尾页 22pt 大字号金句「对称性，」「可以被打破。」——居中文本，溢出向两侧各约 1mm，不可见，保留醒目字号。
- **肖像**：`keepaspectratio` 下封面 2.0×2.8cm、身份页 3.0×3.9cm 正常缩放，无变形。
- **封面 badge 字体**：主标题 `\scriptsize`、副标题 `\tiny`（应需求缩小一档），编译无新增告警。
- **中文标点/断行**：全角引号、破折号、`\quad` 间距统一，与 Wilson 标杆一致。
- **编译**：`make distclean && make` → ✅ 13 页，169 比例，肖像已嵌入，中文渲染正常。

> 结论：两轮 Review 通过，修复 1 处 P0 事实错误（推荐人吴健雄→吴大猷）；Overfull 均在可接受范围内。
