# 物理学家立传提示词（Jim Peebles）

> 本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主的「人物专属立传提示词」。
> 目标人物：Phillip James Edwin Peebles（2019 诺贝尔物理学奖，物理宇宙学的奠基者，半个世纪把宇宙学变成精密科学）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Phillip James Edwin Peebles（菲利普·詹姆斯·埃德温·皮布尔斯，通称 Jim Peebles），2019 年诺贝尔物理学奖（一半奖金），普林斯顿 Albert Einstein 科学讲席荣休教授。
- **设计哲学**：保留「身份信息页 + 结构化研究领域」骨架；Peebles 篇叙事主线是「把宇宙学从思辨变成精密科学」—— Shaw 奖引文是其一生工作的最佳概括。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Phillip James Edwin Peebles（1935-04-25 生于加拿大曼尼托巴省温尼伯 St. Vital；在世）
- **气质关键词**：**物理宇宙学的奠基人、CMB 的解读者、冷暗物质与结构形成的先驱**
- **官方获奖理由（2019，一半奖金）**：
  > "for theoretical discoveries in physical cosmology"（因物理宇宙学的理论发现）
  - 另一半由 Michel Mayor 与 Didier Queloz 共享（绕类日恒星运行的系外行星发现），本篇提及但重心在宇宙学。
- **设计母题**：**从原初到结构（from plasma to galaxies）**。3K 宇宙微波背景、太初核合成、暗物质与结构形成——视觉以温度渐变的宇宙网为核心意象。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Jim_Peebles/page.md`（**已有本地**）
- **待下载**：`{Dir}.html` 与 `images/` 肖像待下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Jim_Peebles`
- **参考模板**：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1935-04-25 生于温尼伯 St. Vital（今属曼尼托巴省温尼伯）；在世（death_date 留白）
- **国籍**：加拿大、美国（citizenship 双籍；frontmatter nationality Canada + United States）
- **家庭**：父 Andrew Charles Peebles（温尼伯谷物交易所职员）、母 Ada Marion（née Green，家庭主妇）；妻 Alison Peebles（1958 年结婚），三子女；自称坚定的不可知论者（convinced agnostic）
- **教育**：曼尼托巴大学 BS → 普林斯顿大学 MS、PhD 1962
- **博士导师**：Robert Dicke；博士论文 *Observational Tests and Theoretical Problems Relating to the Conjecture That the Strength of the Electromagnetic Interaction May Be Variable*（1962）
- **任职机构**：普林斯顿大学（一生从未离开；Albert Einstein Professorship in Science, emeritus）；高等研究院（IAS）自然科学院 Member 1977–78，1990–91、1998–99 再访
- **关键荣誉（年份齐全）**：APS Fellow 1964；Eddington Medal 1981；Heineman Prize 1982；FRS 1982；Henry Norris Russell Lectureship 1993；Bruce Medal 1995；Oskar Klein Medal 1997；RAS Gold Medal 1998；Gruber Cosmology Prize 2000（与 Allan Sandage）；Harvey Prize 2001；Shaw Prize 2004；美国哲学学会会员 2004；Crafoord Prize 2005（与 James E. Gunn、Martin Rees）；Hitchcock Professorship 2006；ICTP Dirac Medal 2013；Order of Manitoba 2017；Nobel 2019；AAS Legacy Fellow 2020；Carnegie Great Immigrants Award 2021；Golden Plate Award 2024；小行星 18242 Peebles 命名；Companion of the Order of Canada / Petrie Prize Lecture / Jansky Lectureship / Tomalla Prize / Georges Lemaître Prize（frontmatter 有载、正文无年份）
- **知名学生**：Margaret J. Geller、Stuart L. Shapiro（infobox Doctoral students 明载）
- **核心贡献清单**：
  1. 1965 与 Dicke 及另两位普林斯顿物理学家把 Penzias & Wilson 发现的 CMB 与早期宇宙等离子体冷却事件相连——轰动学界，大爆炸模型被广泛接受
  2. 以 3K 辐射温度计算太初核合成（Big Bang nucleosynthesis）首个准确的太初元素丰度估计
  3. 1970 年代初确立暗物质问题；1970 年代结构形成理论的主要先驱
  4. Ostriker–Peebles criterion（星系形成稳定性判据）
  5. 1987 提出太初等曲率重子模型（primordial isocurvature baryon model）
  6. 教科书体系：*Physical Cosmology*（1971）、*Large-Scale Structure of the Universe*（1980）、*Principles of Physical Cosmology*（1993）、*Cosmology's Century*（2020）、*The Whole Truth*（2022）等
- **关键时间线（17 节点）**：1935 生于温尼伯 → 曼尼托巴 BS → 普林斯顿研究生 → 1962 PhD（Dicke 门下）→ 1964 转向当时被视为「死胡同」的宇宙学 → 1965 CMB 解读（与 Dicke 组）→ 1970s 暗物质问题与结构形成 → 1971 *Physical Cosmology* → 1977–78 IAS Member → 1980 *Large-Scale Structure* → 1982 Heineman/FRS → 1987 等曲率重子模型 → 1993 *Principles of Physical Cosmology* → 2000 Gruber（与 Sandage）→ 2004 Shaw → 2005 Crafoord（与 Gunn/Rees）→ 2019-10-08 获诺奖 → 2019-12-08 诺奖演讲 *How Physical Cosmology Grew*

### 第 4 步：研究领域表 【人物专属，与 yaml fields 一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physical cosmology | 物理宇宙学 | 获奖理由原词、一生主线 | 全篇 |
| 1 | cosmic microwave background | 宇宙微波背景 | 1965 解读 CMB | 核心页 |
| 2 | Big Bang nucleosynthesis | 大爆炸核合成 | 3K 温度推太初丰度 | 核心页 |
| 3 | dark matter | 暗物质 | 1970s 确立暗物质问题 | 暗物质页 |
| 4 | structure formation | 结构形成 | 1970s 主要先驱 | 结构页 |

### 第 4.5 步：社会关系表 【人物专属，与 yaml relations 一致；只收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert H. Dicke | 师→生（博士导师） | 普林斯顿博士导师，1965 CMB 解读合作 |
| advisor-student | Margaret J. Geller | Peebles → 学生 | 天文学家，星系巡天代表人物 |
| advisor-student | Stuart L. Shapiro | Peebles → 学生 | 相对论天体物理学家 |
| co-honored | Michel Mayor | 无向 | 2019 诺贝尔物理学奖共享（Peebles 得一半，Mayor/Queloz 共享另一半） |
| co-honored | Didier Queloz | 无向 | 2019 诺贝尔物理学奖共享（同上） |
| colleague | Jeremiah P. Ostriker | 无向 | Ostriker–Peebles criterion（星系稳定性判据）共同提出者 |
| co-honored | Allan Sandage | 无向 | 2000 Gruber Cosmology Prize 共同得主 |
| co-honored | James E. Gunn | 无向 | 2005 Crafoord Prize 共同得主 |
| co-honored | Martin Rees | 无向 | 2005 Crafoord Prize 共同得主 |
| spouse | Alison Peebles | 无向 | 1958 年结婚 |

### 第 5 步：配色方案 【人物专属】

- **气质**：深邃、冷峻、长时段
- **主色**：深靛蓝 `#1E3A5F`（3K 宇宙的冷与深空）+ 诺奖香槟金 `C9A227`
  - `badgeCMB` 宇宙微波背景 — 电光青 `#0E7C9B`
  - `badgeBBN` 太初核合成 — 琥珀 `#E07B30`
  - `badgeDM` 暗物质 — 深紫 `#4A3B8C`
  - `badgeSF` 结构形成 — 苔绿 `#3E7C4F`
- **背景母题**：柔和气泡 + 由密到疏的宇宙网点阵（原初均匀 → 结构化）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）；无真实肖像则用装饰圆占位。
2. 封面有国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页（封面之后、核心贡献之前）。
4. 结尾页品牌标注统一 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 物理宇宙学奠基人 / Jim Peebles 1935– + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、出生地、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — CMB / 太初核合成 / 暗物质 / 结构形成
04  温尼伯到普林斯顿 (1935–1962) — 曼尼托巴 BS、Dicke 门下博士
05  1965：解读 CMB（核心贡献页一）— 与 Dicke 组把 Penzias/Wilson 发现连到早期宇宙等离子体冷却
06  太初核合成 — 3K 温度推太初元素丰度（公式框放太初丰度/膨胀-核物理概念图式）
07  死胡同里的坚守 — 1964 年宇宙学被视作 dead end、缓慢建立学科尊严
08  暗物质与结构形成 (1970s) — Ostriker–Peebles criterion、1987 等曲率重子模型
09  教科书体系 — Physical Cosmology / Large-Scale Structure / Principles of Physical Cosmology
10  2019 诺贝尔奖 — 一半奖金；Mayor/Queloz 共享另一半（系外行星）
11  荣誉长廊 — Eddington 1981 · Heineman 1982 · Bruce 1995 · Shaw 2004 · Crafoord 2005 · Dirac 2013
12  对「开端」的怀疑 — 不可知论与对宇宙起点的谨慎（引语页，仅用白名单引语）
13  遗产：从思辨到精密科学 — Shaw 引文收束
14  结尾
```

### 第 7–8 步：版式要点 + 陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖份额 | Peebles 独得**一半**，Mayor 与 Queloz **共享另一半**（工作互不相关）；勿写成三人平分 |
| 获奖理由 | 官方措辞 "for theoretical discoveries in physical cosmology"；强调**理论发现**，勿写成观测发现 |
| 1965 小组 | page.md 只写 "Peebles, with Dicke and two other Princeton physicists"——另两位**未具名**（勿自行补 Roll/Wilkinson 名字）；发现者 Penzias/Wilson 是贝尔实验室方，与普林斯顿组是「解读」关系，**勿写成同一团队的共同发现** |
| 姓名 | 全名 Phillip James Edwin Peebles，通称 Jim/P. J. E. Peebles；书籍署名 P.J.E.；勿与他人混淆 |
| 双籍 | Citizenship 为 Canadian, American；身份页两籍并列，勿只写一国 |
| 引语白名单 | 仅 page.md 英文原句可用："It's very unfortunate that one thinks of the beginning…"、"It was not a single step…"、Shaw 引文 "He laid the foundations…"；**其余禁杜撰** |
| 分享奖项年份 | Gruber 2000 与 Sandage、Crafoord 2005 与 Gunn/Rees——各自年份与同伴勿错配 |
| 无年份荣誉 | Companion of the Order of Canada、Petrie、Jansky、Tomalla、Lemaître 仅 frontmatter 有载，如列须标「年份不详」或省略 |
| IAS 身份 | 1977–78 是 Member（年度成员），1990–91/1998–99 为再访；勿写成 IAS 长期教授 |
| 宗教观 | "convinced agnostic" 明载可写一句；勿引申更多 |
| 论文题目 | 博士论文主题是「电磁相互作用强度可变」的检验——与其后来的宇宙学无直接关系，勿写成宇宙学论文 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| physical cosmology | 物理宇宙学 | 获奖理由原词 |
| cosmic microwave background (CMB) | 宇宙微波背景 | 非单纯「背景辐射」，含 3K 黑体谱 |
| Big Bang nucleosynthesis | 大爆炸核合成 / 太初核合成 | 以核物理+膨胀计算丰度 |
| dark matter | 暗物质 | 与 dark energy 区分 |
| structure formation | 结构形成 | 1970s 先驱 |
| primordial isocurvature baryon model | 太初等曲率重子模型 | 1987 提出 |
| Ostriker–Peebles criterion | Ostriker–Peebles 判据 | 星系形成稳定性 |
| Lyman-alpha emitter | 莱曼阿尔法发射体 | known-for 列表项 |
| quintessence | 第五要素（精质） | 暗能量模型，known-for 列表项 |
| cosmic infrared background | 宇宙红外背景 | known-for 列表项 |
| cold dark matter | 冷暗物质 | known-for 列表项 |
| recombination | 复合（宇宙学） | known-for 列表项；注意拼写非 recomination |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（宏大/深远/长期影响）
- **匹配理由**：「基础理论/长期影响」匹配半个世纪奠基一门学科的一生；宏大气质贴合 3K 宇宙与结构形成的尺度感。
- **备选**（未采用）：The Flow of Time（时间感贴切但受众偏低）；Timeless（沉稳纪录片，但已被多个标杆篇目使用，批内避开）。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Jim_Peebles/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Jim_Peebles.yaml` | 社会关系/领域入库数据 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
