# 物理学家立传提示词（Hiroshi Amano 天野浩）

> **OpenPhysicist 21 世纪批次 · 人物专属立传提示词**。
> 目标人物：Hiroshi Amano（天野 浩，1960-09-11 ~ 在世），2014 诺贝尔物理学奖得主（蓝光 LED 三人组之一）。
> 执行方式：复制本文件到新对话中，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Hiroshi Amano（天野 浩），日本材料科学家/半导体工程学者，氮化镓（GaN）蓝光 LED 共同发明人。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页），且强调「研究领域」的结构化表达——这两点构成骨架，务必保留。天野浩篇的叙事核心是「从冷门实验室的不夜城，到点亮世界的蓝光」——一个在赛场上被普遍认为不可能的材料上做出突破的工程师型科学家。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Hiroshi Amano（天野 浩，1960-09-11 生于日本静冈县滨松市，在世）
- **气质关键词**：**蓝光点灯者、不夜城实验室主、氮化镓的守望者** —— 2014 诺贝尔物理学奖获奖理由（官方英文原文，禁止改写）：
  > "for the invention of efficient blue light-emitting diodes which has enabled bright and energy-saving white light sources."（发明高效蓝光二极管，实现了明亮且节能的白色光源）
- **设计母题**：**蓝光（blue glow）**。GaN 蓝光 LED 是「在蓝色宝石衬底上长出的蓝光」——视觉语言可用深蓝背景 + 一束蓝光穿出，呼应其从 AlN 缓冲层到 p-n 结点亮的三十余年坚持。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Hiroshi_Amano/page.md`
- **第 0 步状态**：page.md 已有本地；`Hiroshi_Amano.html` 与 `images/` 待下载，Wikipedia URL：`https://en.wikipedia.org/wiki/Hiroshi_Amano`
- **参考模板**：
  - 物理学家成品骨架：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已核对 page.md，建 Beamer 前须再对照原文）

- 生卒：1960-09-11 生于静冈县滨松市，在世（享年不写）
- 国籍：日本
- 父母：父 Tatsuji（达治）、母 Yoshiko（良子），page.md 仅载名字
- 早年：小学踢足球（守门员）、打垒球（捕手）；热衷业余无线电；讨厌读书但擅长数学；进入高中后发奋成为优等生
- 教育：1979 年进名古屋大学工学部，1983 学士、1985 硕士、1989 工学博士（D.Eng.）
- 博士导师：Isamu Akasaki（赤崎勇），1982 年本科阶段即加入赤崎研究室
- 主要任职：1988 名古屋大学工学部研究助手；1992–2010 名城大学理工学部（助教→副教授→教授）；2010 回任名古屋大学研究生院工学教授；2011 起任赤崎研究中心主任
- 关键荣誉：Rank Prize for Optoelectronics 1998；Nobel 2014；Asia Game Changer Award 2015；Asian Scientist 100 2016；文化勋章・文化功勋者（frontmatter award_received）
- 会士/院士：2009 日本应用物理学会 Fellow；2015 美国 APS Fellow；2016 美国国家工程院 International Member；2019 中国工程院外籍院士；2022 日本学士院会员
- 荣誉学位：2016 帕多瓦大学、2017 林雪平大学、2025 米兰比可科大学
- 核心贡献清单：
  1. 1985 年发明低温沉积缓冲层（AlN buffer layer），解决蓝宝石衬底上生长 III 族氮化物薄膜的难题
  2. 1989 年世界首次实现 p 型 GaN 生长并制成 p-n 结型 GaN 紫外/蓝光 LED
  3. LEEBI（低能电子束辐照）处理 Mg 掺杂 GaN 获得 p 型导电
  4. III 族氮化物半导体的生长、表征与器件应用系列工作，奠定蓝光 LED 与激光二极管基础
- 关键时间线（15–20 节点）：1960 出生滨松 → 小学足球/垒球/业余无线电 → 高长发奋 → 1979 入名古屋大学 → 1982 加入赤崎研究室 → 1983 学士 → 1985 硕士 + AlN 缓冲层论文 → 1988 名大研究助手 → 1989 工学博士 + p 型 GaN/p-n 结 LED（LEEBI 论文） → 1992 转名城大学 → 1995 量子阱器件受激发射论文 → 1998 Rank Prize → 2009 JSAP Fellow → 2010 回名大教授 → 2011 赤崎研究中心主任 → 2014 诺贝尔物理学奖 → 2015 APS Fellow / Asia Game Changer → 2016 NAE 国际会员 → 2019 中国工程院外籍院士 → 2022 日本学士院会员

### 第 4 步：研究领域表（与 yaml fields 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | gallium nitride | 氮化镓（GaN） | III 族氮化物半导体，毕生主战场 | 核心页 |
| 1 | light-emitting diodes | 发光二极管 | 蓝光 LED 共同发明，2014 诺奖核心 | 核心页 |
| 2 | epitaxial growth | 外延生长 | 低温 AlN 缓冲层、MOVPE 生长工艺 | 方法页 |
| 3 | materials science | 材料科学 | infobox Fields 明载 | 身份页 |
| 4 | optoelectronics | 光电子学 | Rank Prize 授奖领域 | 荣誉页 |

### 第 4.5 步：社会关系表（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Isamu Akasaki | 导师 | 名古屋大学博士导师，2014 诺贝尔物理学奖共同得主 |
| co-honored | Isamu Akasaki | 无向 | 2014 诺贝尔物理学奖共同得主 |
| co-honored | Shuji Nakamura | 无向 | 2014 诺贝尔物理学奖共同得主，日亚化学蓝光 LED |
| colleague | Nobuhiko Sawaki | 无向 | 名古屋大学同事，1986 AlN 缓冲层论文共同署名 |
| colleague | Kazumasa Hiramatsu | 无向 | 名古屋大学 GaN 系列合作者，多篇论文共同署名 |

> 注：妻子（page.md 载其曾任斯洛伐克考门斯基大学日语讲师）page.md 未载姓名，不入 spouse 关系；仅收集 page.md 明载关系。

### 第 5 步：配色方案 【人物专属】

- **气质**：深蓝、明亮、工程师的坚实感
- **配色**：LED 蓝（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - `mainclr` 主色 — LED 蓝 `#1E5AA8`（批内不重复）
  - `badgeGaN` 氮化镓 — 靛蓝 `#4C5FD5`
  - `badgeLED` 蓝光 LED — 青绿 `#0E7C7B`
  - `badgeEpi` 外延生长 — 琥珀 `#E07B30`
  - `badgeOpto` 光电子学 — 玫瑰 `#C4204F`
- **背景母题**：深蓝底色上稀疏光点 + 一束自下而上的蓝色光锥，呼应「蓝光点亮世界」

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 蓝光点灯者 / Hiroshi Amano 1960– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、出生地、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — AlN 缓冲层 / p 型 GaN / 蓝光 LED / 氮化物器件
04  早年：滨松少年 (1960–1979) — 足球守门员、业余无线电、高中发奋
05  名古屋大学与赤崎研究室 (1979–1989) — 1982 入组、工学三部曲 1983/1985/1989
06  突破一：AlN 低温缓冲层 (1985) — 蓝宝石衬底上的高质量 GaN 薄膜（公式框：MOVPE 生长示意/概念图式，page.md 无具体公式须注明）
07  突破二：p 型 GaN 与 p-n 结 LED (1989) — LEEBI 处理 Mg 掺杂，世界首次点灯
08  名城大学岁月 (1992–2010) — 助教到教授、量子阱受激发射
09  回归名大与赤崎研究中心 (2010– ) — 2011 起任中心主任
10  荣誉与认可 — Nobel 2014 · Rank Prize 1998 · 文化勋章 · 各国院士
11  「不夜城」实验室 — 学生口中的乐观温和、永不发怒的实验室主
12  遗产：从蓝光 LED 到白光照明革命 — 节能白光源改变世界
13  结尾
```

### 第 7–8 步：版式要点 + 天野浩专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "for the invention of efficient blue light-emitting diodes which has enabled bright and energy-saving white light sources."；禁写「发明蓝光 LED 照亮世界」之类改写口径 |
| 三人共享 | 2014 奖由 Akasaki + Amano（名古屋系）与 Nakamura（日亚系）三人共享；Amano 是 Akasaki 的学生，Nakamura 与二人无师承关系，勿混写 |
| Nakamura 归属 | Nakamura 时在日亚化学（Nichia），勿写成与名古屋大学合作 |
| 首次 p 型 GaN | 1989 年「世界首次」生长 p 型 GaN 并制成 p-n 结型紫外/蓝光 LED，系 page.md 明载；勿提前到 1985（1985 是缓冲层） |
| 博士年份 | 工学博士 1989 年取得；1988 已任研究助手（先任职后取得学位），勿写反 |
| 职业口径 | page.md 导语称 materials scientist；frontmatter 载 doctor of engineering and physicist；infobox Fields 为 Materials science——身份页以「材料科学家 / 工学博士」为主口径 |
| 无载禁写 | 博士论文题目、Nakamura 与 Amano 的私人关系、蓝光 LED 的产业化细节（日亚诉讼等）page.md 均无载，一律禁写 |
| 家庭 | 妻子未载姓名，仅可写「曾任斯洛伐克考门斯基大学日语讲师」，勿编造姓名 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| gallium nitride (GaN) | 氮化镓 | 勿写成「镓氮」 |
| buffer layer | 缓冲层 | AlN，低温沉积 |
| sapphire substrate | 蓝宝石衬底 | 非蓝色宝石的误读 |
| p-type semiconductor | p 型半导体 | LEEBI 处理后获得 |
| LEEBI | 低能电子束辐照 | Low-Energy Electron Beam Irradiation 缩写 |
| p-n junction | p-n 结 | 二极管核心结构 |
| MOVPE | 金属有机气相外延 | 论文标题作 metalorganic vapor phase epitaxy |
| blue LED | 蓝光二极管 | 官方口径 light-emitting diode |
| laser diode | 激光二极管 | 氮化物基蓝绿激光 |
| quantum well | 量子阱 | 1995 受激发射器件 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（79k views，鼓舞/明亮）
- **匹配理由**：
  - 「鼓舞/明亮」匹配蓝光 LED 的点灯意象——从被认为不可能的材料上点亮第一束蓝光
  - 「开场/突破」匹配 1985 缓冲层 → 1989 点灯的突破叙事
- **备选**（未采用）：Shine Like The Sun（更明亮但留给同批 Nakamura）、Expedition（远征感偏史诗）
- **本地路径**：`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`
- **时长**：约 3 分 39 秒 > 14 页 × 7 秒 ≈ 98 秒 → ffmpeg `-shortest` 自动对齐
