# 物理学家立传提示词（Shuji Nakamura 中村修二）

> **OpenPhysicist 21 世纪批次 · 人物专属立传提示词**。
> 目标人物：Shuji Nakamura（中村 修二，1954-05-22 ~ 在世），2014 诺贝尔物理学奖得主（蓝光 LED 三人组之一）。
> 执行方式：复制本文件到新对话中，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Shuji Nakamura（中村 修二），日裔美国电子工程师，高效蓝光 LED 与白光 LED、蓝光激光二极管的发明者/共同发明人。
- **设计哲学**：物理学家立传必须有「身份信息页」，且强调「研究领域」的结构化表达。中村篇的叙事核心是「企业实验室里的孤胆发明人」——在小型化工公司日亚化学独自坚持 GaN 研究、一举做出千倍亮度蓝光 LED，再以发明人诉讼改写日本职场规则，最后跨太平洋到 UCSB 开创固态照明。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Shuji Nakamura（中村 修二，1954-05-22 生于日本爱媛县伊方町，在世）
- **气质关键词**：**蓝光激光的孤勇者、白光照明的点灯人、发明人权益的斗士** —— 2014 诺贝尔物理学奖获奖理由（官方英文原文，禁止改写）：
  > "for the invention of efficient blue light-emitting diodes which has enabled bright and energy-saving white light sources."（发明高效蓝光二极管，实现了明亮且节能的白色光源）
- **设计母题**：**从蓝到白（blue to white）**。蓝光芯片 + 黄色荧光粉 = 白光照明——视觉语言可用深蓝底色上蓝黄双色光束交汇成白光，呼应其技术路线：先点亮蓝，再合成白。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Shuji_Nakamura/page.md`
- **第 0 步状态**：page.md 已有本地；`Shuji_Nakamura.html` 与 `images/` 待下载，Wikipedia URL：`https://en.wikipedia.org/wiki/Shuji_Nakamura`
- **参考模板**：
  - 物理学家成品骨架：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已核对 page.md，建 Beamer 前须再对照原文）

- 生卒：1954-05-22 生于爱媛县伊方町，在世
- 国籍：日本（至 2005）→ 美国（2005 起）
- 教育：德岛大学电子工学 1977 学士（B.Eng.）、1979 硕士（M.Eng.）、1994 工学博士（D.Eng.，以论文成果提交方式取得，doctoral thesis submitted by publication）
- 博士导师：page.md 无载（勿写）
- 任职：日亚化学（Nichia）1979–1999；加州大学圣塔芭芭拉分校（UCSB）材料系与电子计算机工程系教授 1999 起（校长 Henry T. Yang 三赴日本亲邀）
- 关键荣誉：IEEE Jack A. Morton Award 1998；Rank Prize 1998；朝日奖 2000；Nick Holonyak Jr. Award 2001；Millennium Technology Prize 2006（首位）；阿斯图里亚斯亲王奖 2008；Harvey Prize 2009；Nobel 2014；Draper Prize 2015；Global Energy Prize 2015；Asia Game Changer 2015；Mountbatten Medal 2017；Queen Elizabeth Prize for Engineering 2021；Golden Plate 2022；文化勋章 2014（明仁天皇授予）
- 会士/院士：2003 美国国家工程院院士；2019 英国皇家工程院国际会士；美国发明家名人堂（frontmatter award_received）
- 专利：截至 2020-05-05 持有 208 项美国实用专利
- 核心贡献清单：
  1. 1993 年制成首个商用高亮度 GaN 蓝光 LED（比此前成功者亮 3 个数量级）
  2. 热退火法实现 p 型 GaN（相较 Akasaki 组的电子束辐照法更适合量产），并查明氢钝化受主的机理
  3. 蓝光 + 荧光粉部分转换成黄光 = 白光 LED，奠定固态照明
  4. 蓝光激光二极管（用于 Blu-ray Disc 与 HD DVD）
  5. 绿光 LED 系列、纯 GaN 衬底固态照明（Soraa）
  6. 2022 年共同创立激光聚变公司 Blue Laser Fusion
- 关键时间线（15–20 节点）：1954 出生伊方町 → 1977 德岛大学学士 → 1979 硕士 + 入职日亚化学 → （创始人小川信雄支持 GaN 项目）→ 1989 小川英嗣接任社长、被令中止 GaN → 1993 蓝光 LED 成功（独自继续开发）→ 1994 工学博士 → 1998 Morton Award/Rank Prize → 2000 朝日奖 → 2001 起诉日亚（20 亿日元发明报酬诉讼）→ 2003 NAE 院士 → 2006 千年技术奖 → 2008 阿斯图里亚斯奖 + 与 DenBaars/Speck 共同创立 Soraa → 2009 Harvey Prize → 1999 起 UCSB 教授 → 2014 诺贝尔物理学奖 + 文化勋章 → 2005 入籍美国 → 2015 Draper/Global Energy/Asia Game Changer → 2021 伊丽莎白女王工程奖 → 2022 Blue Laser Fusion 创立
- 诉讼脉络（page.md 明载，可立一页）：2000 与 Cree 约定共同起诉日亚并获股票期权 → 2001 起诉，主张 20 亿日元 → 地方法院判 200 亿日元 → 2005 和解 8.4 亿日元（日本公司对员工发明支付的最高额，仅够诉讼费）→ 此后反复批评日本企业不善待研究者

### 第 4 步：研究领域表（与 yaml fields 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | gallium nitride | 氮化镓（GaN） | 高亮度蓝光 LED 的材料基础 | 核心页 |
| 1 | light-emitting diodes | 发光二极管 | 蓝/绿/白 LED，2014 诺奖核心 | 核心页 |
| 2 | laser diodes | 激光二极管 | 蓝光激光，Blu-ray/HD DVD 光源 | 激光页 |
| 3 | optoelectronics | 光电子学 | infobox Fields 明载 | 身份页 |
| 4 | solid-state lighting | 固态照明 | 白光 LED 照明革命、Soraa | 遗产页 |

### 第 4.5 步：社会关系表（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Isamu Akasaki | 无向 | 2014 诺贝尔物理学奖共同得主 |
| co-honored | Hiroshi Amano | 无向 | 2014 诺贝尔物理学奖共同得主 |
| spouse | Yuki Nakamura | 无向 | 妻子 |
| colleague | Steven P. DenBaars | 无向 | UCSB 同事，2008 共同创立固态照明公司 Soraa |
| colleague | James Speck | 无向 | UCSB 同事，2008 共同创立固态照明公司 Soraa |
| influence | Nobuo Ogawa | 无向 | 日亚化学创始人，其 GaN 项目的支持与资助者 |

> 注：博士导师 page.md 无载禁写；Draper Prize/Global Energy Prize 的共同得主注释在 page.md 脚注中未与具体奖项行明确对应，不入库以防错配。

### 第 5 步：配色方案 【人物专属】

- **气质**：明亮、锐利、企业实验室的攻坚感
- **配色**：激光绿（主色，呼应绿光 LED 与蓝激光的「光」意象）+ 诺奖香槟金 `C9A227` + 四分类色
  - `mainclr` 主色 — 激光绿 `#0E6B3C`（批内不重复）
  - `badgeGaN` 氮化镓 — 靛蓝 `#2B4C9B`
  - `badgeLED` 蓝/白 LED — 亮蓝 `#1E88C7`
  - `badgeLD` 激光二极管 — 紫蓝 `#5B3A99`
  - `badgeSSL` 固态照明 — 暖金 `#C9A227`
- **背景母题**：深色底上蓝黄双色光束交汇为白光的几何图形

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 蓝光孤勇者 / Shuji Nakamura 1954– + 四色 badge + 右上头像 + 国籍行（日本→美国）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍变迁、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 蓝光 LED / 热退火 p 型 GaN / 白光 LED / 蓝光激光
04  德岛与日亚 (1954–1989) — 德岛大学三部曲、入职日亚、小川信雄的支持
05  孤独的 GaN (1989–1993) — 被令中止、独自坚持、1993 千倍亮度点灯
06  突破机理：热退火与氢钝化（核心贡献页）— p 型 GaN 量产化、氢钝化受主的物理（公式框：p-n 结发光示意/概念图式，page.md 无具体公式须注明）
07  从蓝到白：固态照明革命 (1993– ) — 荧光粉转换白光、照明能效革命
08  蓝光激光与光盘时代 — Blu-ray Disc / HD DVD
09  发明人诉讼 (2001–2005) — 200 亿判决与 8.4 亿和解、日本职场启示
10  太平洋东渡：UCSB 岁月 (1999– ) — Henry T. Yang 三赴亲邀、Soraa 创立
11  荣誉与认可 — Nobel 2014 · Millennium 2006 · QE Prize 2021 · NAE 2003
12  新边界：Blue Laser Fusion (2022– ) — 激光聚变创业
13  遗产：点亮世界的白光
14  结尾
```

### 第 7–8 步：版式要点 + 中村修二专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文与 Akasaki/Amano 相同："for the invention of efficient blue light-emitting diodes…"；禁改写 |
| 与赤崎组的口径 | Nakamura 是**利用** Akasaki 组发表的电子束辐照法做 p 型 GaN 的知识基础、再发明更适合量产的热退火法；勿写成独立发现 p 型 GaN，也勿写成 Akasaki 学生 |
| 无博士导师 | page.md 无载导师（1994 学位以成果提交取得），禁编造 |
| 国籍口径 | 日本（至 2005）→ 美国（2005 起），身份页写「日本/美国（2005 入籍）」 |
| 诉讼金额 | 主张 20 亿日元、地方法院判 200 亿日元、2005 和解 8.4 亿日元（≈US$8.1M）——三个数字勿混 |
| 亮度对比 | 1993 器件比此前成功蓝光 LED 亮 3 个数量级（1000 倍），勿写成「10 倍」 |
| 千年技术奖 | 2006 年首届 Millennium Technology Prize 得主，page.md 明载获奖但「首位」为通行说法，Beamer 中谨慎措辞 |
| 创业区分 | 2008 Soraa（固态照明，与 DenBaars/Speck）≠ 2022 Blue Laser Fusion（激光聚变，与 Hiroaki Ohta），勿混 |
| 无载禁写 | 蓝光 LED 之外的商业细节、家庭子女、日亚内部人事纠纷细节超出 page.md 者禁写 |
| 同名区分 | 中村修二 vs 长岗/中村其他人物无关；Henry T. Yang 是 UCSB 校长（招募者），勿写成合作者入库 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| gallium nitride (GaN) | 氮化镓 | 勿写成「镓氮」 |
| high brightness blue LED | 高亮度蓝光二极管 | 1993 商用化 |
| thermal annealing | 热退火 | p 型化的量产方法 |
| hydrogen passivation | 氢钝化 | 钝化受主的"元凶" |
| acceptor | 受主 | p 型掺杂Mg |
| phosphor | 荧光粉 | 蓝光转黄光成白光 |
| blue laser diode | 蓝光激光二极管 | Blu-ray 光源 |
| solid-state lighting | 固态照明 | 白光 LED 照明 |
| GaN substrate | GaN 衬底 | Soraa 纯 GaN 路线 |
| doctoral thesis by publication | 以成果提交的博士论文 | 1994 德岛大学 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Really Slow Motion（2:49，史诗/美丽/振奋）
- **匹配理由**：
  - 「光明/振奋」匹配白光照明的意象——从蓝光到点亮世界的白光
  - 「定理证明、光明的结尾」匹配 1993 点灯与 2014 诺奖的高潮叙事
- **备选**（未采用）：Awaken（留给同批 Amano）、Last Hope（戏剧性偏诉讼段但整体基调不符）
- **本地路径**：`music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav`
- **时长**：169 秒 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐
