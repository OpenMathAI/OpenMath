# 和平奖得主立传提示词（OpenPeace：Carlos Saavedra Lamas）

> **本文件是 OpenPeace 项目的人物专属立传提示词**，以 Carlos Saavedra Lamas（1936 诺贝尔和平奖，首位拉丁美洲和平奖得主）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节 + 第 0–9 步）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenPhysicist / OpenMedic 同属 OpenMathAI 共享仓库）。
- **模板来源**：综合物理学家标杆（Kenneth G. Wilson 提示词 + Beamer 结构）与医学/化学侧批量立传经验。
- **本实例**：Carlos Saavedra Lamas（卡洛斯·萨维德拉·拉马斯），阿根廷外长、《非侵略与和解公约》起草人、恰科战争调停者。
- **设计哲学**：和平奖得主立传的核心骨架是「身份信息页 + 结构化事业领域」；外交家型得主的主线是「法学—教职—公约—调停」，务必保留身份信息页。

---

## 二、背景信息 【人物专属】

- **目标人物**：Carlos Saavedra Lamas（1878-11-01 ~ 1959-05-05，享年 80 岁）
- **气质关键词**：**《阿根廷反战公约》之父、恰科战争的调停者、首位拉美和平奖得主** —— 1936 诺贝尔和平奖获奖理由：
  > "for his role as father of the Argentine Antiwar Pact of 1933, which he also used as a means to mediate peace between Paraguay and Bolivia in 1935."（表彰他作为 1933 年《阿根廷反战公约》缔造者的角色，并借此于 1935 年在巴拉圭与玻利维亚之间斡旋和平）
- **设计母题**：**南美的规约（the pact）**。其一生围绕「以条约文本框定和平」——公约起草、仲裁条约、国联大会议长；视觉上可用「签署的卷轴/南美地图/天平与鹅毛笔」呼应。
- **本地 Wikipedia**：`peace/presentations/pages/20th_century/Carlos_Saavedra_Lamas/page.md`（含 frontmatter QID Q193672 与 infobox）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）
  - 名录（官方理由照抄源）：`peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（据本地 page.md，无载禁写） 【人物专属】

- 生卒：1878-11-01 生于布宜诺斯艾利斯 ~ 1959-05-05 逝于布宜诺斯艾利斯（脑溢血），享年 80 岁；葬于 La Recoleta 墓园
- 国籍：阿根廷（Argentina）
- 家庭：出身阿根廷早期爱国者后裔之家；娶总统 Roque Sáenz Peña 之女（page.md 未载其名，禁写姓名）
- 教育：Lacordaire College → 布宜诺斯艾利斯大学法学院，1903 以 summa cum laude 获法学博士 → 巴黎深造
- 教职：La Plata 大学法律与宪法史教授（教学生涯逾四十年）；后在 UBA 开设社会学课程、讲授政治经济学与宪法，1941-10-17~1943-07-30 任 UBA 校长，执教至 1946
- 任职/身份：1906 公共信贷主任；1907 布宜诺斯艾利斯市政秘书长；1908 两连任国会议员；1915-08-20~1916-10-12 司法与公共教育部长；1932-02-20~1938-02-20 外交与宗教事务部长（总统 Agustín P. Justo 任命）
- 学术著作：Centro de legislación social y del trabajo（1927）、Traités internationaux de type social（1924）、三卷本 Código nacional del trabajo（1933）、La Crise de la codification et de la doctrine argentine de droit international（1931）、Vida internacional（七十岁所著）
- 关键荣誉：Nobel Peace Prize 1936（首位拉丁美洲得主）；法国荣誉军团大十字；捷克斯洛伐克白狮勋章一级（1936-12-15）
- 核心事业清单（4–6 条）：
  1. 劳动立法与国际法学者（支持 1919 年 ILO 创立，1928 主持其日内瓦会议并率阿根廷代表团）
  2. 1932 华盛顿 8 月 3 日宣言（美洲各国不承认武力造成的领土变更）
  3. 1933《非侵略与和解公约》（Saavedra Lamas Treaty）：1933-10 六个南美国家签署，两个月后第七届泛美会议（蒙得维的亚）美洲各国签署
  4. 1934 向国联提交南美反战公约（11 国签署）
  5. 1935 六个美洲中立国调停结束恰科战争（1932–1935，巴拉圭 vs 玻利维亚）
  6. 1936 当选国联大会主席；把阿根廷带回国联（缺席 13 年之后）
- 关键时间线（15–20 节点）：1878 出生 → 1903 法学博士 → 1906 公共信贷主任 → 1908 议员 → 1915 司法部长 → 1919 支持 ILO 创立 → 1924/1927/1933 劳动法著作 → 1928 ILO 日内瓦会议主席 → 1932 外长+8月3日宣言 → 1933 非侵略公约 → 1934 国联提交公约 → 1935 恰科调停 → 1936 国联大会主席+诺奖 → 1938 卸任外长 → 1941–43 UBA 校长 → 1946 停止执教 → 1959 去世

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

**Saavedra Lamas 的事业领域（按 rank 排序，已入库 person_field，与 yaml fields 一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | diplomacy | 外交 | 六年外长、南美外交主导者 | 外长页 |
| 1 | international law | 国际法 | 公约起草、国联大会主席 | 公约页 |
| 2 | labor law | 劳动法 | 三卷本劳动法典、ILO 工作 | 学者页 |
| 3 | constitutional law | 宪法学 | UBA 宪法讲席 | 教职页 |
| 4 | international arbitration | 国际仲裁 | 恰科战争调停、仲裁条约 | 调停页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 与 `MySQL/data/Carlos_Saavedra_Lamas.yaml` 完全一致；只收 page.md 明载关系。
> 注意：妻子无姓名禁入库；Roque Sáenz Peña 是岳父（姻亲无对应类型）不入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Agustín P. Justo | 无向 | 1932 任命其为外交与宗教事务部长 |
| colleague | Victorino de la Plaza | 无向 | 1915 任内出任司法与公共教育部长 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：典雅、法理、外交辞令
- **配色**：深靛蓝灰（法理与外交的庄重，manifest 预分配 `#17435B`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgePact` 反战公约 — 玫瑰 `#C4204F`
  - `badgeMediate` 恰科调停 — 琥珀 `#E07B30`
  - `badgeAcademy` 学术与教职 — 靛蓝 `#4C5FD5`
  - `badgeLeague` 国联舞台 — 青绿 `#0E7C7B`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），以「卷轴与印章的圆形」呼应规约母题

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover 共享封面）
01  封面 — 反战公约之父 / Carlos Saavedra Lamas 1878–1959 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、国籍、教育、任职、荣誉、核心领域）
03  核心事业概览 — 劳动法学者 / 外长岁月 / 公约与调停 / 国联舞台
04  早年与法学之路 (1878–1903) — Lacordaire、UBA summa cum laude、巴黎深造
05  议会与司法部长 (1906–1916) — 公共信贷、议员立法、1915 司法与公共教育部长
06  劳动立法学者 — 三卷本 Código nacional del trabajo、ILO 1928 日内瓦会议主席
07  外长岁月 (1932–1938)（核心页）— Agustín P. Justo 任命、阿根廷重返国联
08  八月三日宣言与非侵略公约（核心页）— 1932 华盛顿、1933 六国签署、蒙得维的亚扩签
09  恰科战争调停 (1935) — 六中立国调停、结束巴拉圭与玻利维亚之战
10  国联大会主席 (1936) — 南美反战公约 11 国、大会议长
11  1936 诺贝尔和平奖 — 获奖理由、首位拉美得主、白狮勋章与荣誉军团
12  学术晚景与身后 — UBA 校长 1941–43、1959 去世、奖章 2014 拍卖流落
13  遗产：以规约求和平的外交家
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照物理学家标杆 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用标杆 tex 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Saavedra Lamas 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 妻子无名 | 仅载「娶总统 Roque Sáenz Peña 之女」，禁写姓名、禁写婚姻年份；岳父不入库（姻亲无类型） |
| 政党历史两说 | infobox：National Autonomist Party（至 1916）+ National Democratic Party（1931–1959）；注释载西语维基更详细版本且无 inline 引用——以 infobox 口径为准并加注 |
| 获奖理由句 | 「father of the Argentine Antiwar Pact of 1933」——是公约缔造者，勿写成「反战公约以他命名」之外的杜撰；公约正式名 Treaty of Nonaggression and Conciliation（Saavedra Lamas Treaty 为别称） |
| 恰科战争年份 | 战争 1932–1935，他 1935 年促成六国调停结束战争——勿写「结束 1935 年战争」 |
| 签署国数字 | 公约 1933-10 为六个南美国家签署、两个月后蒙得维的亚全美洲国家签署；1934 国联版本 11 国签署——三组数字勿混 |
| 奖章下落 | 2014-03 南美当铺发现后拍卖；国会曾提案回购；最终由私人亚洲藏家购得；成交价 $1,116,250 与 $1.38M 两说并存——正文写「由私人亚洲藏家购得」即可 |
| 「争议人物」表述 | 当代观察认为其精英气、偏保守、亲英（铁路）——page.md 明载可客观一句，勿展开评价 |
| 无载禁写 | 与 Justo 只有任命关系、与 de la Plaza 只有任命关系，勿编导师/门生；无 PhD 导师可写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Treaty of Nonaggression and Conciliation | 《非侵略与和解公约》 | 1933，别称 Saavedra Lamas Treaty |
| Chaco War | 查科战争 / 恰科战争 | 1932–1935 |
| League of Nations Assembly | 国际联盟大会 | 1936 主席 |
| International Labour Organization | 国际劳工组织（ILO） | 1919 创立支持、1928 主持会议 |
| summa cum laude | 最优等 | 1903 博士 |
| Pan-American Conference | 泛美会议 | 第七届蒙得维的亚 |
| labor legislation | 劳动立法 | 学术主业 |
| rector | 大学校长 | UBA 1941–43 |
| brain hemorrhage | 脑溢血 | 死因 |
| La Recoleta Cemetery | 拉雷科莱塔墓园 | 安葬地 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Lonesome** — AShamaluevMusic（manifest 预分配，勿改）
- **风格**: 忧郁 / 情感深沉 / 电影感
- **匹配理由**:
  - 「深沉」匹配外交孤旅——在武装冲突频发的年代以条约文本独行调停
  - 「电影感」匹配奖章流落的尾声——2014 年当铺重现，历史人物的身后余音
- **本地路径**: `music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`
- **时长**: 以 ffmpeg `-shortest` 对齐视频长度

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Carlos_Saavedra_Lamas/page.md` | 本地 Wikipedia 正文（唯一事实源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/Carlos_Saavedra_Lamas.yaml` | 入库数据（fields/relations 与本文件一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
