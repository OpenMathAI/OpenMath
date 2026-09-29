# 和平奖得主立传提示词（OpenPeace：Arthur Henderson）

> **本文件是 OpenPeace 项目的人物专属立传提示词**，以 Arthur Henderson（1934 诺贝尔和平奖，工党领袖、国联裁军会议主席）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节 + 第 0–9 步）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenPhysicist / OpenMedic 同属 OpenMathAI 共享仓库）。
- **模板来源**：综合物理学家标杆（Kenneth G. Wilson 提示词 + Beamer 结构）与医学/化学侧批量立传经验。
- **本实例**：Arthur Henderson（阿瑟·亨德森），英国工党三度领袖、首位工党阁员、1932–33 日内瓦裁军会议主席。
- **设计哲学**：和平奖得主立传的核心骨架是「身份信息页 + 结构化事业领域」；政治人物的叙事主线是「工运—建党—组阁—裁军」，务必保留身份信息页。

---

## 二、背景信息 【人物专属】

- **目标人物**：Arthur Henderson（1863-09-13 ~ 1935-10-20，享年 72 岁）
- **气质关键词**：**「Uncle Arthur」、调停与仲裁的信徒、三度执掌工党的组织者** —— 1934 诺贝尔和平奖获奖理由：
  > "for his untiring struggle and his courageous efforts as Chairman of the League of Nations Disarmament Conference 1931-34."（表彰他作为 1931–1934 年国际联盟裁军会议主席所进行的不懈斗争与勇敢努力）
- **设计母题**：**调停的天平（conciliation）**。其一生关键词是「仲裁与调停」——工会争议调停、党内派系弥合、国际裁军谈判；视觉上可用「天平/圆桌/握手」呼应。
- **本地 Wikipedia**：`peace/presentations/pages/20th_century/Arthur_Henderson/page.md`（含 frontmatter QID Q208665 与 infobox）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）
  - 名录（官方理由照抄源）：`peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（据本地 page.md，无载禁写） 【人物专属】

- 生卒：1863-09-13 生于格拉斯哥 Anderston 区 Paterson 街 10 号 ~ 1935-10-20 逝于伦敦，享年 72 岁；逝后火化于 Golders Green 火葬场
- 国籍：英国（United Kingdom）
- 家庭：母 Agnes（家仆）、父 David Henderson（纺织工人，Arthur 十岁时去世）；母后改嫁 Robert Heath；三个儿子均参加一战——长子 David 1916 阵亡（Middlesex Regiment 上尉），次子 William（1945 获封 Baron Henderson）、三子 Arthur（1966 获封 Baron Rowley）
- 教育：无正规学历——12 岁入 Robert Stephenson and Sons 铸造厂，17 岁满徒后任铸铁工（iron moulder）
- 宗教：1879 成为 Wesleyan Methodist，任 Methodist local preacher；1884 失业后专心传道
- 任职/身份：1892 Friendly Society of Iron Founders 受薪组织者；1893 Newcastle 市议员（自由党）；1903 LRC 司库 + Barnard Castle 补选议员；1903–04 Darlington 市长；内阁——1915 教育委员会主席（首位工党阁员）、1916 无任所大臣（战时内阁）、1915–16/1916 岁入主计长、1924 内政大臣、1929–31 外交大臣；工党领袖三任（1908–10、1914–17、1931–32）
- 关键荣誉：Nobel Peace Prize 1934（1934-12-11 发表诺奖演讲 Essential Elements of a Universal and Enduring Peace）
- 核心事业清单（4–6 条）：
  1. 工会组织与劳资调停（反对罢工、支持仲裁）
  2. LRC → 工党建党组织工作（1900 LRC 代表；1918 与 MacDonald、Sidney Webb 建立全国选区组织网络）
  3. 首位工党内阁阁员（1915）与三任工党领袖（三个不同年代）
  4. 1929–31 外交大臣：恢复对苏邦交、全面支持国联
  5. 日内瓦裁军会议主席（1932-02-02 开幕发言）与世界和平联盟工作
- 关键时间线（15–20 节点）：1863 出生 → 12 岁进铸造厂 → 1879 入卫理公会 → 1892 工会组织者 → 1900 LRC → 1903 议员+司库 → 1906 工党正式成立 → 1908 首任领袖 → 1914 二任领袖（接替辞职的 MacDonald）→ 1915 首位工党阁员 → 1916 战时内阁 → 1917 辞职 → 1918 党组织重建 → 1919 Widnes 补选 → 1924 内政大臣 → 1929 外交大臣 → 1931 危机与党魁 → 1932 裁军会议 → 1933 Clay Cross 补选（五度补选复出纪录）→ 1934 诺奖 → 1935 去世

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

**Henderson 的事业领域（按 rank 排序，已入库 person_field，与 yaml fields 一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | labour politics | 工党政治 | 三任工党领袖、党组织重建 | 建党页 |
| 1 | trade unionism | 工会运动 | 铸造工会组织者、劳资调停 | 早年页 |
| 2 | disarmament | 裁军 | 1931–34 国联裁军会议主席，诺奖理由 | 裁军页 |
| 3 | diplomacy | 外交 | 1929–31 外交大臣 | 外相页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 与 `MySQL/data/Arthur_Henderson.yaml` 完全一致；只收 page.md 明载关系。
> 注意：父与长子同名 David Henderson——为防库内同名 stub 分裂，父以「David Henderson」入库（父亲身份明确），长子不入库（见陷阱表）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Ramsay MacDonald | 无向 | 1918 共建工党组织网络，1931 党魁之争后由 Henderson 接任 |
| colleague | Sidney Webb | 无向 | 1918 共建选区组织网络，Webb 起草党纲 Labour and the New Social Order |
| colleague | Keir Hardie | 无向 | 1900 LRC 同仁，1908 接替其出任工党领袖 |
| colleague | David Lloyd George | 无向 | 1916–1917 战时内阁共事 |
| parent-child | David Henderson | 父→子 | 父亲，纺织工人，Henderson 十岁时去世 |
| parent-child | William Henderson, 1st Baron Henderson | 父→子 | 次子，1945 获封男爵 |
| parent-child | Arthur Henderson, Baron Rowley | 父→子 | 三子，1966 获封男爵 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：敦厚、调停、组织之力
- **配色**：深棕（铸造工与工会底色，manifest 预分配 `#5C3A1E`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeUnion` 工会运动 — 琥珀 `#E07B30`
  - `badgeParty` 工党建党 — 玫瑰 `#C4204F`
  - `badgeCabinet` 内阁任职 — 靛蓝 `#4C5FD5`
  - `badgeDisarm` 裁军外交 — 青绿 `#0E7C7B`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），以「天平两端的圆」呼应调停母题

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover 共享封面）
01  封面 — 裁军会议主席 / Arthur Henderson 1863–1935 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、出生地、国籍、职业、任职、荣誉、核心领域）
03  核心事业概览 — 工会调停 / 建党组织 / 内阁任职 / 裁军外交
04  早年：从格拉斯哥到铸造厂 (1863–1892) — 丧父、12 岁进厂、卫理公会传道
05  工会组织者 (1892–1900) — 友好铸造工会、东北调停委员会、反罢工立场
06  LRC 与建党 (1900–1908) — Hardie 议案、1903 补选、Darlington 市长、1908 接任领袖
07  首位工党阁员 (1915–1917) — 教育委员会、战时内阁、1917 辞职
08  重建工党 (1918–1924) — 选区网络、Labour and the New Social Order、内政大臣
09  外交大臣 (1929–1931) — 对苏复交、支持国联
10  1931 危机与党魁 — 拒绝削减失业救济、唯一投反对票者、1931 惨败
11  裁军会议与诺贝尔奖（核心页）— 1932 日内瓦开幕、1934 获奖理由
12  家人与身后 — 三子从军、长子阵亡、Golders Green、奖章 2013 被盗未寻回
13  遗产：调停者的政治生涯
14  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照物理学家标杆 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用标杆 tex 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Henderson 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 党魁任期 | 三任领袖：1908–10（接 Hardie）、1914–17（接辞职的 MacDonald）、1931–32——勿写成连续任期 |
| Lord Privy Seal 细节 | 1916 先任 Paymaster General（1916-08-18~12-10）再任 Minister without Portfolio（1916-12-10~1917-08-12），勿合并 |
| 1917 辞职 | 因其国际会议提案被内阁否决而于 1917-08-11 辞职——勿写成反战辞职 |
| MacDonald 关系 | 1914 接党魁后「两人成为敌人」；1918 仍合作建党；1931 MacDonald 另组国民政府被开除出党而 Henderson 投唯一反对票——三段关系勿简化 |
| 首子不入库 | 长子 David 1916 阵亡，page.md 仅作 David，且与祖父同名 David Henderson——防同名分裂不入库，正文可用「长子 David」 |
| 列宁评价 | 列宁 1922 信中贬低 Henderson 是单方评论，禁写为「论战/争议关系」，正文可客观一句 |
| 妻子 | 名录石碑有「his wife」但 page.md 全文未载其名——禁写姓名 |
| 补选纪录 | 五度在非在任选区补选当选（1903/1919/1923/1924/1933），为下院失去席位后复出次数纪录保持者——勿写「五次补选当选」的模糊说法 |
| 奖章被盗 | 2013-04-03 Newcastle 市长办公室失窃，窃贼入狱、奖章未寻回——勿写成「下落不明于史」 |
| 无载禁写 | 无大学教育、无师承可写；World League of Peace 细节 page.md 无展开勿编 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Labour Representation Committee | 劳工代表委员会（LRC） | 1906 年才更名工党 |
| iron moulder | 铸铁工 | 勿译「钢铁工人」泛称 |
| Friendly Society of Iron Founders | 铸铁工友会 | 工会名 |
| Methodist local preacher | 卫理公会平信徒传道人 | 非牧师 |
| Chief Whip | 党团督导长 | 1919–21 等 |
| Foreign Secretary | 外交大臣 | 1929–31 |
| World Disarmament Conference | 世界裁军会议 | 1932 日内瓦开幕 |
| by-election | 补选 | 五度复出 |
| coupon election | 「联署选举」（1918） | 勿直译「优惠券」 |
| conciliation | 调停/和解 | 母题词 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Eternals** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 宏大 / 深远 / 长期影响
- **匹配理由**:
  - 「长期影响」匹配其组织遗产——1918 年建成的选区网络与党纲延续至 1950 年
  - 「宏大」匹配裁军会议的历史尺度——一人 chair 一场没能阻止二战却定义了时代努力的大会
- **本地路径**: `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`
- **时长**: 以 ffmpeg `-shortest` 对齐视频长度

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Arthur_Henderson/page.md` | 本地 Wikipedia 正文（唯一事实源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/Arthur_Henderson.yaml` | 入库数据（fields/relations 与本文件一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步向我汇报。**
