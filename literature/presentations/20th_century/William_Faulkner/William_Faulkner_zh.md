# 文学家立传提示词（OpenLiterature：William Faulkner）

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 共享仓库，与数学/物理/化学侧同构）。
- **本实例**：William Cuthbert Faulkner（威廉·福克纳），1949 年诺贝尔文学奖得主，美国南方文学的最高峰、约克纳帕塔法王国的缔造者。
- **设计哲学**：文学家立传以「身份信息页 + 研究领域表」为骨架（与物理学家模板同构），但以**代表作书影 / 名句引文框 / 意象图式**替代公式框——福克纳的视觉母题是「一块邮票大小的故乡土地」：约克纳帕塔法县地图、罗温橡树庄园（Rowan Oak）墙上的手迹、《喧嚣与骚动》的意识流拼贴。

## 二、背景信息 【人物专属】

- **目标文学家**：William Faulkner（1897-09-25 ~ 1962-07-06，享年 64 岁）
- **姓名**：William Cuthbert Faulkner（本姓 Falkner，1918 年因排版误印改为 Faulkner，「两种写法都行」）／ 威廉·福克纳
- **诺奖年份**：1949 年诺贝尔文学奖，官方获奖理由（禁止改写）：
  > "for his powerful and artistically unique contribution to the modern American novel"（表彰其对现代美国小说有力而在艺术上独树一帜的贡献）
  > 注：该奖于 1950 年 12 月斯德哥尔摩颁奖晚宴上与 1950 年度奖（Bertrand Russell）一同颁发。
- **气质关键词**：约克纳帕塔法的缔造者、意识流的南方史诗者、拒绝好莱坞的文化巴比伦囚徒
- **设计母题**：**「邮票大的乡土」**——Faulkner 自称约克纳帕塔法县是他的 "postage stamp"（以拉法耶特县为原型近乎地理复刻）；配 Rowan Oak 书房墙上的《寓言》一周情节手迹、《喧哗与骚动》的时分叙事碎片，构成「心智风景」（mental landscape）的视觉语言。
- **本地数据源**：`literature/presentations/pages/20th_century/William_Faulkner/page.md`（+ metadata.json、images.txt）
- **Wikipedia**：https://en.wikipedia.org/wiki/William_Faulkner （肖像第 0 步下载：infobox 用 1954 年照 File:William_Faulkner_1954_(2)_(photo_by_Carl_van_Vechten).jpg；备选 1924 宣传照、1918 年加拿大约克训练队照）

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇歧义先征求意见。含「研究领域梳理+入库」（第 4 步）与「社会关系梳理+入库」（第 4.5 步），写入 greatminds 库（MySQL）。

### 第 0 步：事实基准（已核对，以正文为准）

- **生卒**：1897-09-25 生于密西西比州新奥尔巴尼（New Albany）～ 1962-07-06 逝于密西西比州拜黑利亚（Byhalia）Wright 疗养院（6-17 坠马重伤致血栓、心脏病发），享年 64 岁；葬于牛津（Oxford, Mississippi）圣彼得墓园。
- **国籍**：美国（唯一的密西西比州出生诺奖得主）。
- **家庭**：长门四子之首；父 Murry Cuthbert Falkner（牛津开马厩与五金店、后任密西西比大学事务经理），母 Maud Butler；1902 年全家迁牛津，此后终老于此。曾祖父 William Clark Falkner（"老上校"：邦联上校、两度涉杀受审无罪、州议员、铁路股东、终遭合伙人谋杀）为其命名来源与创作原型库。1929 年与 Estelle Oldham 成婚（她携前夫 Cornell Franklin 的两个孩子来归），育一女 Jill（1933–2008）；1931 年长女 Alabama 出生九天夭折。
- **教育**：牛津高中（重读十一、十二年级，未毕业）；1919 入密西西比大学（Ole Miss），三学期后于 1920-11 退学（英文课得 D）；frontmatter educated_at 亦列 University of Virginia（1957–1958 任首届驻校作家，非学位）。
- **军旅**：一战加入英加空军（Royal Flying Corps (Canada)），1918-07-10 多伦多入伍（二等兵 No.173799），未参战、未受飞行训练，1919-01-04 退役；曾向熟人虚构战功与战伤——按 page.md 客观转述。
- **文学师承与影响（仅收 page.md 明载）**：17 岁遇 Phil Stone（耶鲁才子，早其四年），第一位赏识者与导师（引荐 Joyce 等作家，并代投诗稿）；Stone 引荐下结识 Sherwood Anderson、Robert Frost、Ezra Pound；1925 新奥尔良时期由维多利亚风转向现代主义；自述影响书单：《旧约》、狄更斯、康拉德、塞万提斯（每年重读《堂吉诃德》）、福楼拜、巴尔扎克、陀思妥耶夫斯基、托尔斯泰、莎士比亚；与同代 Joyce、Eliot 同用「古典素材放进现代语境」的神话方法（《喧哗与骚动》题出《麦克白》、《我弥留之际》题出《奥德赛》阿伽门农语）。
- **任职/经历**：牛津邮局局长（1923 辞职信名句）；1925 上半年新奥尔良法国区（与 William Spratling 合租圣彼得街公寓，1926 合印《舍伍德·安德森与其他著名克里奥尔人》画册戏仿）；1932–1954 断续在好莱坞写剧本约 50 部（米高梅起步，与 Howard Hawks 结为酒猎之友；代表作改编剧本《有多少就有多少》《夜长梦多》；Meta Carpenter 婚外情）；1957–1958 弗吉尼亚大学首届驻校作家。
- **关键荣誉**：1949 诺贝尔文学奖；1951 + 1955 美国国家图书奖（《短篇小说集》/《寓言》）；1955 + 1963 普利策小说奖（《寓言》/《掠夺者》——1955 一次为评委会否决改判的政治性争议，按 page.md 客观转述）；1951 法国荣誉军团骑士勋章；William Dean Howells Medal；O. Henry Award。
- **核心作品与贡献（4–6 条）**：
  1. 《喧哗与骚动》（1929，31 岁生日后动笔，「关上门，现在我可以写了」——班吉、昆丁、杰生、迪尔西四重时分叙事）
  2. 《我弥留之际》（1930，在密西西比大学电厂夜班写成；59 节 15 位叙述者）
  3. 《圣殿》（1931，为钱而写）与《八月之光》（1932）
  4. 《押沙龙，押沙龙！》（1936）与《野棕榈》（1939）
  5. 短篇：《献给爱米丽的一朵玫瑰花》等（首部集《这十三篇》1931）；斯诺普斯三部曲（小镇/城镇/大宅）
  6. 《寓言》（1954）与绝笔《掠夺者》（1962，第 19 部长篇）
- **关键时间线（15–20 节点）**：1897 生于新奥尔巴尼 → 1902 迁牛津 → 1914–1915 结识 Phil Stone → 1918 多伦多 RFC(C) 入伍（未参战）→ 姓氏 Falkner→Faulkner → 1919–1920 Ole Miss 三学期退学 → 1922 〈Portrait〉刊于新奥尔良《Double Dealer》→ 1923 邮局长辞职 → 1924 首部诗集《大理石牧神》→ 1925 新奥尔良、首部长篇《士兵的报酬》（Anderson 促成出版）→ 1927 写成《尘埃中的旗帜》（被拒）→ 1929 经经纪人 Ben Wasson 删改以《沙托里》出版（首部约克纳帕塔法小说）；与 Estelle 成婚；《喧嚣与骚动》→ 1930《我弥留之际》、购 Oxford 宅「罗温橡树」（Rowan Oak）→ 1931《圣殿》、Alabama 夭折 → 1932《八月之光》、赴好莱坞 → 1936《押沙龙，押沙龙！》→ 1942《去吧，摩西》（题献保姆 Caroline Barr）→ 1943 起构思《寓言》；致信鼓励青年 Eudora Welty → 1944–1946《有多少就有多少》《夜长梦多》剧本 → 1946 Cowley 编《袖珍福克纳》出、声誉复苏（此前多数长篇绝版）→ 1949 诺贝尔奖（1950-12 领奖，受奖辞论「人类精神的不朽」，捐出部分奖金设新人小说基金 → 威廉·福克纳基金会 1960–1970）→ 1951 荣誉军团勋章、国家图书奖 → 1954《寓言》获普利策 → 1955《寓言》再获国家图书奖 → 1957–1958 弗吉尼亚大学驻校作家 → 1961 写《掠夺者》 → 1962-06-17 坠马 → 1962-07-06 逝于 Byhalia → 1987 美国邮政 22 美分纪念邮票、2019 密西西比作家之路标牌立于 Rowan Oak。

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 目录 `literature/presentations/20th_century/William_Faulkner/`（+ `images/`），Makefile 设 `MAIN=William_Faulkner_zh`；肖像下载（curl `-A "Mozilla/5.0"`，file 验证；失败用 Commons Special:FilePath 回退）。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | novel | 长篇小说 | 19 部长篇构成约克纳帕塔法史诗 | 作品页 |
| 1 | short story | 短篇小说 | 《献给爱米丽的一朵玫瑰花》等 | 短篇页 |
| 2 | Southern Gothic | 南方哥特 | 怪诞与悲剧底色的南方叙事 | 风格页 |
| 3 | stream of consciousness | 意识流 | 《喧哗与骚动》《我弥留之际》的叙事实验 | 风格页 |
| 4 | screenwriting | 电影剧本 | 1932–1954 好莱坞约 50 部影片 | 好莱坞页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Phil Stone | 影响→福克纳 | 早其四年的牛津才子，首位赏识者与导师，引荐 Joyce 等 |
| influence | James Joyce | 影响→福克纳 | 经 Stone 引荐阅读；神话方法同脉 |
| colleague | Sherwood Anderson | 无向 | 新奥尔良时期引路人，促成《士兵的报酬》《蚊群》出版 |
| colleague | William Spratling | 无向 | 1925 年合租合著《舍伍德·安德森与其他著名克里奥尔人》 |
| colleague | Ben Wasson | 无向 | 文学经纪人，删改《尘埃中的旗帜》成《沙托里》 |
| colleague | Howard Hawks | 无向 | 好莱坞合作导演兼酒猎之友，《夜长梦多》等 |
| colleague | Malcolm Cowley | 无向 | 《袖珍福克纳》（1946）编者，声誉复苏关键 |
| colleague | Ernest Hemingway | 无向 | 同代对照（极简 vs 意识流），曾改编其《有多少就有多少》 |
| colleague | Albert Camus | 无向 | 改编《修女安魂曲》为舞台剧并推崇其悲剧移植 |
| colleague | Joseph Blotner | 无向 | 传记作者，手稿档案核心关联人 |
| spouse | Estelle Oldham | 无向 | 1929 年成婚，青少年时代恋人，1972 年去世 |
| parent-child | Jill Faulkner | 福克纳→女 | 1933–2008，二人唯一的共同孩子 |
| influence | Flannery O'Connor | 福克纳→影响 | 称其临在改变南方作家的写作尺度 |
| influence | Gabriel García Márquez | 福克纳→影响 | 马孔多「与约克纳帕塔法同脉」 |
| influence | Claude Simon | 福克纳→影响 | 法国新小说代表明载承其影响 |
| influence | Mario Vargas Llosa | 福克纳→影响 | 自述在约克纳帕塔法学到比课堂更多 |
| influence | Cormac McCarthy | 福克纳→影响 | 被称为「福克纳的门徒」 |

#### 4.5.1 入库操作

- `MySQL/data/William_Faulkner.yaml` + `cd MySQL && python3 seed_person.py data/William_Faulkner.yaml`（幂等）；校验 fields≥4、relations≥2。

### 第 5 步：设计配色 【人物专属】

- **主色**：南方深褐 `#4E342E`（预分配，勿改）；诺奖香槟金 `C9A227`。
- badgeA–D：badgeA 约克纳帕塔法 — 靛蓝 `#4C5FD5`；badgeB 意识流 — 青绿 `#0E7C7B`；badgeC 南方哥特 — 琥珀 `#E07B30`；badgeD 好莱坞 — 玫瑰 `#C4204F`。
- 背景母题：手绘县地图线条 + 邮票齿孔边框（postage stamp 母题）。

### 第 6 步：规划幻灯片序列（16 页）

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 邮票大的乡土史诗者 / William Faulkner 1897–1962 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、本名 Falkner→Faulkner、教育、婚姻、Rowan Oak、荣誉、核心领域）
03  核心作品概览 — 六大长篇年表书影（喧哗→弥留→圣殿/八月→押沙龙→寓言→掠夺者）
04  老上校的阴影 (1897–1918) — 曾祖父传奇、牛津、RFC(C) 未参战的军旅
05  Phil Stone 与退学生涯 (1914–1924) — 导师、《大理石牧神》、邮局辞职信
06  新奥尔良转折 (1925–1926) — 法国区、Spratling、《士兵的报酬》
07  约克纳帕塔法建国 (1927–1929) — 尘埃中的旗帜→沙托里、成婚
08  《喧哗与骚动》(1929) — 神话方法、麦克白题辞引文框、「现在我可以写了」
09  《我弥留之际》与《八月之光》(1930–1932) — 电厂夜班、15 叙述者
10  好莱坞岁月 (1932–1954) — Hawks、文化巴比伦书信、《夜长梦多》
11  《押沙龙，押沙龙！》与《去吧，摩西》 — 南方史观与献给 Mammy 的题辞
12  《袖珍福克纳》与诺贝尔奖 (1946–1950) — Cowley 复苏、受奖辞引文框、基金会
13  《寓言》与《掠夺者》(1954–1962) — 普利策争议、绝笔、Rowan Oak 墙上手迹
14  荣誉与认可 — Nobel 1949 · 国家图书奖 ×2 · 荣誉军团 · 引语（「读四遍」）
15  遗产：从马孔多到佩恩·福克纳奖 — 拉美 Boom 一脉、法国「福克纳是神」、结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【模板通用，人物专属内容】

- 版式：`p{}` 窄列用 `\newcolumntype{P}[1]`；南方口语引文用小号；frame 标题过长缩短即可；文学页用书影/引文框替代公式框。
- 陷阱：

| 陷阱 | 说明 |
|------|------|
| 姓氏拼写 | 本姓 Falkner，1918 年因排版误印改 Faulkner（「Either way suits me」）——全篇口径统一为 Faulkner，本名仅在身份页注记 |
| 诺奖年份口径 | 1949 年度奖，1950-12 与 1950 年度奖（Russell）同席颁发——勿写成「1950 获奖」，也勿与 Russell 写成「共享」（两人奖项独立） |
| 军旅口径 | RFC(C) 训练未参战、未飞行、曾虚构战功——按 page.md 客观转述，不渲染 |
| 军种表述 | 正文首段作 Royal Canadian Air Force、后文详述为 Royal Flying Corps (Canada)——用后者精确口径 |
| 普利策 1955 | 评委会原选 Milton Lott《最后的狩猎》，被主管 Hohenberg 说服董事会改判《寓言》——争议按 page.md 客观转述 |
| 种族议题 | 福克纳主张渐进废除种族隔离又反对强制快速融合（Baldwin 批评其「中间地带」）；对 Oppenheimer 的失言按 page.md 客观简述、**不得引用原词**——只作时代局限注记，不展开政治叙事 |
| 受奖辞引语 | "I feel that this award was not made to me as a man…" 为 page.md 实载英段，可用；其余引语核对实载 |
| 军事细节 | 女儿 Jill 从校长处得知父亲得诺奖——细节仅按 page.md |
| 《尘埃中的旗帜》 | 原版 1973 年由 Douglas Day 复原、Noel Polk 版为现行定本——版本沿革一句带过勿展开 |
| 同名区分 | 曾祖父 William Clark Falkner 与本人同名异代，note/图注务必区分 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Yoknapatawpha County | 约克纳帕塔法县 | 虚构县，原型拉法耶特县 |
| postage stamp | 「邮票大」 | 其自况的创作疆域 |
| stream of consciousness | 意识流 | 与 Hemingway 极简对举 |
| Southern Gothic | 南方哥特 | 亦涉 grotesque 怪诞 |
| Snopes trilogy | 斯诺普斯三部曲 | 小镇/城镇/大宅 |
| Rowan Oak | 罗温橡树 | 牛津宅，1950 年代手迹存墙 |
| The Portable Faulkner | 《袖珍福克纳》 | 1946，Cowley 编 |
| Soldiers' Pay | 《士兵的报酬》 | 1925 首部长篇 |
| Flags in the Dust | 《尘埃中的旗帜》 | 1929 以删改版《沙托里》(Sartoris) 出版 |
| Go Down, Moses | 《去吧，摩西》 | 1942，题献 Caroline Barr |
| Writer-in-Residence | 驻校作家 | 弗吉尼亚大学首届（1957–1958） |
| PEN/Faulkner Award | 佩恩/福克纳奖 | 1981 起由其基金会奖沿革而来 |

---

## 四、BGM 建议 ✅ 【人物专属】

- **选定曲目**：**Timeless**（分批文件预分配，勿改）
- **匹配理由**：Timeless 的「沉稳/纪录片/长期纲领」标签匹配福克纳的双层时间感——其一，约克纳帕塔法史诗以「过去的永不消逝」统摄 19 部长篇，是被批评家称为「心智风景」的超时间构造；其二，其声誉曲线（1946 年前多数长篇绝版 → Cowley《袖珍福克纳》复苏 → 诺奖 → 身后成为拉美 Boom 与世界文学源头）正是「时间最终站在作品一边」的纪录片式叙事。
- **备选（未采用）**：Last Hope（苍凉感匹配晚期作品，但受众与标签弱于 Timeless）；Tragedy（1930 年代悲剧气质贴切但已在他批高频使用，避撞曲）。
- **本地路径**：对照 `music_audio/curated_tracks.md` 取 Timeless 音频复制到本目录，`make video` 时 ffmpeg `-shortest` 对齐。

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
