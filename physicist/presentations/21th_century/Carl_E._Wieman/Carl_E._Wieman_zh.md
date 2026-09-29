# 物理学家立传提示词（21 世纪批次 · Carl E. Wieman）

> **本文件是 OpenPhysicist 21 世纪诺奖物理学家立传提示词**，目标人物：Carl E. Wieman（2001 诺贝尔物理学奖，玻色–爱因斯坦凝聚；后转物理教育研究）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Carl Edwin Wieman（卡尔·维曼），21 世纪（2001）诺奖得主系列。
- **设计哲学**：保留「身份信息页 + 研究领域表」骨架；Wieman 篇的双线叙事独此一家——前半生把原子测到极致（精密光谱、铷 BEC），后半生把课堂测到极致（PhET、peer instruction、教育研究），母题是「精度」的迁移。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Carl Edwin Wieman（1951-03-26 生于俄勒冈州科瓦利斯，在世）
- **气质关键词**：**铷原子 BEC 的共同实现者、从 Lamb 位移到课堂测量的精度迁移者、PhET 创始人** —— 2001 诺贝尔物理学奖获奖理由（官方原文，禁止改写）：
  > "for the achievement of Bose-Einstein condensation in dilute gases of alkali atoms, and for early fundamental studies of the properties of the condensates"（因实现稀薄碱金属气体中的玻色–爱因斯坦凝聚，以及对凝聚体性质的早期基础研究）
- **设计母题**：**精度的迁移（precision, twice）**。前半程用激光光谱把氢 Lamb 位移测到极致，后半程用教育测量把课堂改进到极致——封面视觉用同一套同心刻度环从原子谱线过渡到课堂坐标。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Carl_E._Wieman/page.md`（**已有本地**）
- **页面 HTML 与图片**：`Carl_E._Wieman.html` 与 `images/` **待下载**，Wikipedia URL：`https://en.wikipedia.org/wiki/Carl_E._Wieman`
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇到歧义先征求意见再继续。
> 数据库写入 `greatminds`（MySQL），yaml 母本 `MySQL/data/Kenneth_G_Wilson.yaml`，入库引擎 `MySQL/seed_person.py`。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ `page.md` 已有本地（21th_century/21st_century/Carl_E._Wieman/）
- 🔲 待下载 `Carl_E._Wieman.html` 与 infobox 头像 `images/`（404 则装饰圆占位）
- 事实基准（已按 page.md 核对）：
  - 生卒：1951-03-26 生于 Corvallis, Oregon（在世）；父 N. Orr Wieman、母 Alison Marjorie Fry；祖父 Henry Nelson Wieman 为宗教哲学家；兄弟 Howard Wieman 等
  - 国籍：美国
  - 教育：Corvallis High School；MIT BS 1973；Stanford PhD 1977，论文《Polarization Spectroscopy and the Measurement of the Lamb Shift in the Ground State of Hydrogen》；芝加哥大学荣誉理学博士 1997
  - 博士导师：Theodor W. Hänsch（Stanford；2005 诺奖得主）
  - 任职：科罗拉多大学博尔德分校（1995 BEC 期间）；不列颠哥伦比亚大学 2007-01-01 起主持科学教育计划（保留科罗拉多 20%）；斯坦福 2013-09-01 起物理系 + 教育研究生院联合聘任；康奈尔大学 A. D. White Professor at Large
  - 关键荣誉：E. O. Lawrence 1993 · Fritz London 1996 · King Faisal 1997 · Lorentz 1998 · Benjamin Franklin 2000 · Nobel 2001 · 美国年度教授 2004 · Oersted 2007 · Yidan 教育研究奖 2020
  - 知名学生：Wendy Adams、Christopher Monroe（infobox 博士生）
  - 核心贡献：①与 Cornell 1995 实现铷原子首个 BEC；②凝聚体早期基本性质研究（涡旋、坍缩动力学等合作论文）；③精密光谱（铯超精细结构等）；④PhET 交互模拟创始人；⑤peer instruction 教育研究与 NAS 科学教育委员会主席 2005–2009
  - 公共服务：2010-03-24 提名白宫科技政策办公室（OSTP）科学副主任，2010-09-16 一致通过确认，2012-06 离任以治疗多发性骨髓瘤
  - 个人生活：page.md **无载配偶与子女**，勿写
  - 诺奖演讲：2001-12-08 "Bose-Einstein Condensation in a Dilute Gas; The First 70 Years and Some Recent Experiments"
  - 关键时间线（≥15 节点）：1951 生科瓦利斯 → Corvallis HS → 1973 MIT BS → 1977 Stanford 博士（Lamb 位移）→ 精密光谱年代（铯超精细 1988 等）→ 1993 Lawrence 奖 → 1995-06 与 Cornell 实现铷 BEC → 1996 London 奖 → 1997 Faisal/芝大荣誉博士 → 1998 Lorentz → 2000 Franklin → 2001 诺奖 → 2004 年度教授 → 2005–2009 NAS 科学教育委员会主席 → 2006–2007 创 PhET（科罗拉多）→ 2007 Oersted → 2007-01-01 赴 UBC → 2010–2012 OSTP → 2013 起斯坦福 → 2020 Yidan 奖

### 第 4 步：研究领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | Bose-Einstein condensate | 玻色–爱因斯坦凝聚 | 1995 铷原子首次实现，2001 诺奖核心 | 核心页 |
| 1 | precision spectroscopy | 精密光谱学 | 博士论文 Lamb 位移与铯超精细测量 | 早年页 |
| 2 | laser cooling | 激光冷却 | BEC 路线的降温手段 | 方法页 |
| 3 | atomic physics | 原子物理 | JILA/科罗拉多主业 | 身份页 |
| 4 | physics education | 物理教育研究 | PhET/peer instruction/NAS 教育委员会 | 教育页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Theodor W. Hänsch | 师→生（博士导师） | Stanford 博士导师，Lamb 位移精密测量，2005 诺奖 |
| colleague | Eric A. Cornell | 无向 | Boulder 博士后导师与 BEC 合作者（1995） |
| co-honored | Eric A. Cornell | 无向 | 2001 诺贝尔物理学奖共享 |
| co-honored | Wolfgang Ketterle | 无向 | 2001 诺贝尔物理学奖共享 |
| advisor-student | Wendy Adams | Wieman→学生 | 博士生，物理教育方向 |
| advisor-student | Christopher Monroe | Wieman→学生 | 博士生，离子阱量子信息先驱 |
| influence | Eric Mazur | 影响者→Wieman | 其 peer instruction 教学法被 Wieman 推广 |

> 方向约定：导师有向；学生有向；同事/共同荣誉无向；influence 方向为「影响者→本人」。

### 第 5 步：设计配色方案

- **气质**：精密度量、课堂明亮、温润转型
- **配色**：暖琥珀棕（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - `mainclr` 暖琥珀棕 `#7A5230`
  - `badgeBEC` 玻色–爱因斯坦凝聚 `#A0672F`
  - `badgeSpec` 精密光谱 `#3E6FB0`
  - `badgeCool` 激光冷却 `#0E7C7B`
  - `badgeEdu` 物理教育 `#B0413E`
- **背景母题**：柔和气泡——同心刻度环从原子谱线渐变为课堂坐标格

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. 封面明示国籍，底部状态栏 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：左头像 + 右信息网格，事实取自 page.md，不得杜撰。
4. 品牌口径：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列（14 页）

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 从原子精度到课堂精度 / Carl E. Wieman 1951– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 铷 BEC / 精密光谱 / PhET 与 peer instruction / 教育政策
04  科瓦利斯与 MIT (1951–1973) — 家族、Corvallis HS、MIT 本科
05  Stanford 博士：Hänsch 门下 (1973–1977) — 偏振光谱与氢基态 Lamb 位移
06  精密光谱年代 — 铯超精细结构、Lawrence 1993
07  1995：铷原子的首个玻色–爱因斯坦凝聚（核心贡献页；公式框放概念图式——同心刻度环「精度迁移」示意，page.md 无公式，注明）
08  凝聚体性质的早期研究 — 涡旋、坍缩动力学合作论文
09  转向教育：PhET 与 peer instruction
10  教育制度化 — NAS 科学教育委员会 2005–2009、UBC 2007、斯坦福 2013
11  华盛顿岁月与病痛 — OSTP 2010–2012、多发性骨髓瘤
12  荣誉与认可 — Lawrence 1993 · London 1996 · Lorentz 1998 · Nobel 2001 · Oersted 2007 · Yidan 2020
13  遗产：诺奖之后重新定义"教与学"
14  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 表格页安全负间距：顶部 −0.35cm、arraystretch 0.78–0.82；公式框前 −0.35~−0.55cm；希腊字母一律数学模式。

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 只写官方原句，勿缩写 |
| 首个 BEC 归属 | Wieman+Cornell 合作实现铷 BEC；Ketterle 独立实现钠 BEC——勿写 Wieman"最早"或"独自" |
| 博士后导师身份 | Wieman 是 Cornell 的博士后导师（page.md 明载），关系用 colleague + note，白名单无 postdoc 类型 |
| 学生归属 | Wendy Adams 是物理教育方向博士生；Christopher Monroe 是离子阱量子信息先驱（后获 Bunge 等），note 勿张冠李戴 |
| Mazur 关系 | Wieman "使用并推广" Mazur 的 peer instruction——是教学法影响（influence），不是师生，勿写成 advisor-student |
| 家庭信息 | page.md **无载**其配偶与子女，全篇禁写 |
| OSTP 离任原因 | 因患多发性骨髓瘤离任（2012-06），客观一句即可 |
| 在世留白 | 在世人物 death_date 省略 |
| 芝大荣誉博士 | honoris causa 1997，勿写成正式学位 |

### 第 9 步：术语审查清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Lamb shift | 兰姆位移 | 氢基态测量为博士论文主题 |
| polarization spectroscopy | 偏振光谱学 | 博士论文方法 |
| peer instruction | 同伴教学 | 归属 Mazur，Wieman 是推广者 |
| PhET Interactive Simulations | PhET 交互模拟 | 科罗拉多发起的开放教育资源 |
| rubidium | 铷 | 1995 BEC 原子种 |
| Yidan Prize | 一丹奖 | 2020 教育研究奖，勿译"伊丹" |
| Oersted Medal | 奥斯特奖章 | AAPT 物理教学奖 |
| multiple myeloma | 多发性骨髓瘤 | 医学术语客观使用 |
| A. D. White Professor at Large | A. D. White 特聘教授 | 康奈尔荣誉职衔，不译"怀特讲席" |
| hyperfine structure | 超精细结构 | 铯精密测量对象 |

---

## 四、背景音乐选择 ✅

- **选定曲目**：**Daylight** — Alex-Productions（53k views，明亮/轻快）
- **匹配理由**："组合数学、现代成果、结尾轻收"的明亮气质正合 Wieman 后半程的课堂与教育改革叙事；与前两位 2001 得主的突破/远征底色区分。
- **本地路径**：`music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav` → 复制为 `presentations/21th_century/Carl_E._Wieman/Daylight.wav`
- **备选**：SEA（流动/平稳）、New Lands

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Carl_E._Wieman/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
