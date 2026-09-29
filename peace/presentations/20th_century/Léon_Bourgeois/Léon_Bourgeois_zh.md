# OpenPeace 和平奖得主立传提示词（人物：Léon Bourgeois）

> **本文件是 OpenPeace「诺贝尔和平奖得主立传提示词」的人物专属实例**，以 Léon Bourgeois（1920 诺贝尔和平奖，国际联盟大会首任主席）为对象。
> 结构母本沿用标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` 骨架，按和平奖人物特点适配。
> 凡标注【模板通用】可复用；标注【人物专属】按 Bourgeois 替换。直接复制本文件到新对话执行，逐步汇报。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Léon Victor Auguste Bourgeois（莱昂·布尔茹瓦），法国政治家，1920 诺贝尔和平奖得主。
- **设计哲学**：和平奖人物立传以**事业与历史场域**为叙事重心，但「身份信息页」与「事业领域结构化表达」骨架务必保留；涉及政治争议的内容一律只作 page.md 明载的客观事实记录，不加评价。

---

## 二、背景信息 【人物专属】

- **目标人物**：Léon Victor Auguste Bourgeois（1851-05-21 ~ 1925-09-29，享年 74 岁）
- **获奖理由（1920 诺贝尔和平奖）**：
  > "for his longstanding contribution to the cause of peace and justice and his prominent role in the establishment of the League of Nations"（表彰他长期致力于和平与正义事业，并在创建国际联盟中发挥的突出作用）
  > 英文原文取自 `peace/nobel_peace_citations.json`，中译照抄名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写。
- **气质关键词**：**团结主义的理论家、强制仲裁的倡导者、国联大会首任主席**
- **设计母题**：**天平与圆桌（scales and round table）**。从海牙常设仲裁法院到国联大会主席，其事业母线是「以规则与仲裁代替武力」；辅以团结主义的天平意象（社会债务与再分配）。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Léon_Bourgeois/page.md`（Wikipedia 全文 + frontmatter：QID Q217706）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - OpenPeace 同批实例：`peace/presentations/20th_century/Woodrow_Wilson/Woodrow_Wilson_zh.md`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报；含「事业领域梳理+入库」（第 4 步）与「社会关系梳理+入库」（第 4.5 步），写入 greatminds 库。

### 第 0 步：通读 page.md 建立事实基准 【人物专属，已核对】

- 生卒：1851-05-21 生于巴黎 ~ 1925-09-29 逝于马恩省奥热（Oger），享年 74 岁；安葬于 Châlons-en-Champagne 的 Cimetière de l'Ouest
- 国籍：法国；出身巴黎一个共和派家庭，父为勃艮第裔钟表匠
- 家庭：配偶 Virginie Marguerite Sellier（page.md 仅载姓名，无婚期等细节）
- 教育：巴黎大学法学院（Paris Law Faculty），1874 年毕业
- 政治生涯任职（共和派/激进党）：
  1. 公共工程部下属职位（1876）→ 塔恩省省长（1882）→ 上加龙省省长（1885）→ 回巴黎入内政部
  2. 巴黎警察总监（1887-11，正值总统 Grévy 辞职的危机时刻）
  3. 马恩省众议员（1888，击败 Boulanger 派，加入激进左翼）；Floquet 内阁内政部次长（1888）
  4. Tirard 内阁内政部长；1890-03-18 转任公共教育部长（Freycinet 内阁），1890 年推行中等教育重要改革
  5. 司法部长（1892 年底，Ribot 内阁）——巴拿马丑闻期坚决起诉，被控对被告之妻施压取证，1893-03 辞职后旋即复职
  6. **法国总理**（1895-11-01 ~ 1896-04-29，兼任内政部长，1896-03-28 起兼任外交部长）——因参议院拒绝投票拨款引发宪政危机而倒阁
  7. 公共教育部长（1898，Brisson 内阁），组织成人初等教育课程
  8. 1899 海牙和会法国代表；1903 当选常设仲裁法院成员；1899/1907 两次海牙大会代表
  9. 众议院议长（1902-06-06 ~ 1904-01-12）；马恩省参议员（1905）
  10. 外交部长（1906-05，Sarrien 内阁），主持阿尔赫西拉斯会议上的法国外交
  11. 国务部长（1915-10-29 ~ 1916-12-12，Briand 内阁；1917-09-12 ~ 1917-11-13，Painlevé 内阁）
  12. 1919 巴黎和会法国代表，力挺日本种族平等提案
  13. 战后任**国际联盟大会主席**；1920 获诺贝尔和平奖
- 学术/社会身份：团结主义（solidarism）学说创立者——主张富人对穷人有「社会债务」，应以所得税偿付以支撑社会政策；参议院反对其所得税案直至倒阁；1895-12-27 任内通过工人养老金偿还权法
- 关键荣誉：Nobel Peace Prize 1920；荣誉军团勋章（军官级）；圣安德烈/罗马尼亚之星/圣亚历山大·涅夫斯基等外国勋章
- 关键时间线（15–20 节点）：1851 生巴黎 → 1874 法学院毕业 → 1876 入公共工程部 → 1882 塔恩省长 → 1885 上加龙省长 → 1887-11 警察总监 → 1888 众议员+内政次长 → 1890-03 公共教育部长 → 1892-12 司法部长（巴拿马案）→ 1893-03 辞职复职 → 1895-11-01 组阁总理 → 1896-04-29 倒阁 → 1898 成人教育课程 → 1899 海牙和会 → 1902-06 众议院议长 → 1903 常设仲裁法院 → 1905 参议员 → 1906-05 外交部长+阿尔赫西拉斯 → 1907 第二次海牙大会 → 1907–1922 巴黎自然历史博物馆之友首任会长 → 1915/1917 国务部长 → 1919 巴黎和会 → 1920-01 参议院议长 → 1920 诺贝尔和平奖 → 1922-12 诺奖演讲《国际联盟的理由》→ 1925-09-29 逝世

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/` 下建 `Léon_Bourgeois/`；Makefile 设 `MAIN=Léon_Bourgeois_zh`
- 肖像：page.md 有总理官方照（`Léon_Bourgeois,_French_Prime_minister.jpg`），走 Commons Special:FilePath 500px 下载；失败按兄弟项目经验换文件名回退，再失败用装饰圆占位
- 项目 logo/BGM 文件按 `music_audio/` 曲库路径复制

### 第 4 步：事业领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international organization | 国际组织 | 国联创建的突出作用、战后国联大会首任主席 | 国联核心页 |
| 1 | international arbitration | 国际仲裁 | 海牙和会代表、常设仲裁法院成员、强制仲裁主张 | 仲裁页 |
| 2 | diplomacy | 外交 | 外交部长、阿尔赫西拉斯会议、巴黎和会代表 | 外交页 |
| 3 | solidarism | 团结主义 | 社会债务/所得税/社会保险的社会学说 | 内政页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

> 只收 page.md 明载关系；colleague 无向自动 from<to 归一。本人生涯以职位链为主，人物对手方仅收明载同僚。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Virginie Marguerite Sellier | 无向 | 配偶，page.md 仅载姓名 |
| colleague | Alexandre Ribot | 无向 | Ribot 内阁任司法部长，1895 接替 Ribot 出任总理 |
| colleague | Henri Brisson | 无向 | 1898 Brisson 内阁任公共教育部长 |
| colleague | Ferdinand Sarrien | 无向 | 1896 接任其内政部长，1906 Sarrien 内阁任外交部长 |
| colleague | Aristide Briand | 无向 | 1915–1916 Briand 内阁任国务部长 |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#750014`（深酒红——法兰西共和派的庄重，manifest 预分配，勿改）
- **辅色**：诺奖香槟金 `#C9A227`
- **四分类色（badgeA–D）**：`#4C5FD5`（国联/国际组织）· `#0E7C7B`（仲裁与海牙）· `#E07B30`（外交）· `#C4204F`（团结主义与社会立法）
- **背景母题**：天平轮廓与圆桌同心圆 + 淡色和约文书横线

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input 项目首页模板）
01  封面 — 国联大会首任主席 / Léon Bourgeois 1851–1925 + badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/全名/国籍/教育/任职/荣誉/核心领域）
03  巴黎钟表匠之子 (1851–1887) — 法学院、省长历练、危机时刻的警察总监
04  进入议会：激进左翼 (1888–1895) — 马恩议员、内政/公共教育部长、司法部长与巴拿马案
05  总理六个月与团结主义 (1895–1896) — 所得税案、参议院拒拨款的宪政危机
06  海牙与仲裁 (1899–1907) — 两次海牙大会、常设仲裁法院、强制仲裁主张 ★核心页
07  众议院议长与外交部长 (1902–1906) — 阿尔赫西拉斯会议
08  战时国务部长 (1915–1917) — Briand/Painlevé 两届
09  巴黎和会 (1919) — 种族平等提案的法国支持者
10  国际联盟大会首任主席 (1920) — 与诺贝尔和平奖 ★核心页
11  诺奖演讲《国际联盟的理由》(1922) 与晚年 (1920–1925) — 参议院议长、逝世
12  遗产：从团结主义到集体安全
13  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

- 版式沿用标杆：`\plainbar`/`\deckbackground`/`\sectiontitle` 骨架可整体复用 Kenneth_G_Wilson_zh.tex；每写一页 make，溢出修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标
- 品牌口径统一：结尾页底部品牌写 `OpenMathAI`；引号用半角 `" "`

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句照抄（longstanding contribution…），勿把「国联大会首任主席」写成获奖理由本身 |
| 生年双值 | frontmatter 有 05-29 与 05-21，以 infobox/正文 **05-21** 为准 |
| 国联职务 | 战后任「国际联盟大会主席（President of the Assembly）」，勿写成国联主席/秘书长 |
| 总理垮台 | 1896 倒阁原因是参议院拒绝投票拨款引发宪政危机，勿写成选举失利 |
| solidarism 译名 | 译「团结主义」，勿译「社团主义/组合主义」；页面英文 solidarism 与 corporatism 有区分 |
| 巴拿马案 | 被控对被告之妻施压取证属指控，仅客观记录，他随即辞职后复职，勿写「定罪」 |
| 共济会 | page.md 明载 eminent Freemason 且 8 位阁员同为共济会员，仅客观事实记录、不加评价（红线） |
| 种族平等提案 | 1919 他支持日本提案并称其为 "an indisputable principle of justice"，引语须原文；注意 Wilson 作为主席推翻了该提案（见 Wilson 篇交叉注记） |
| 全名 | Léon Victor Auguste Bourgeois；DB/封面用 Léon Bourgeois，勿与法语词 bourgeois（资产者）望文生义 |
| 配偶 | Virginie Marguerite Sellier 仅载姓名，婚期/子嗣无载禁写 |
| 海牙三次 | 1899 和会代表 / 1903 常设仲裁法院成员 / 1907 大会代表是三件事，勿合并成一句 |
| 自然历史博物馆 | 巴黎自然历史博物馆之友首任会长（1907–1922），是科学公益身份，勿写成博物馆馆长 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| solidarism | 团结主义 | 勿译社团主义 |
| compulsory arbitration | 强制仲裁 | 其和平方案核心 |
| Permanent Court of Arbitration | 常设仲裁法院 | 1903 成员 |
| Hague Conventions (1899 and 1907) | 海牙公约 | 两次大会代表 |
| League of Nations Assembly | 国际联盟大会 | 首任主席 |
| Radical Party | 激进党 | 法国激进共和传统 |
| Algeciras Conference | 阿尔赫西拉斯会议 | 1906 摩洛哥危机 |
| Panama scandals | 巴拿马丑闻 | 1892–93 司法部长任期 |
| President of the Senate | 参议院议长 | 1920–1923 |
| economic sanctions | 经济制裁 | 其国联方案要素 |

### 引语白名单 【人物专属，仅 page.md 载有英文原文者可入引文框】

| 原文 | 场景 | 出处 |
|------|------|------|
| "an indisputable principle of justice" | 支持日本种族平等提案 | 1919 巴黎和会 |

> 白名单之外一律转述不引号；中文引号内不写「原话」除非 page.md 有英文原文（红线）。

### 第 10 步：完成判据 【模板通用】

- pdf 0 error、溢出达标（vbox ≤10pt / hbox ≤50pt）、逐页目检通过
- DB `has_social_data=1`、fields≥4、relations≥2；yaml 与提示词第 4/4.5 步完全一致
- 目录内临时目检图（preview/）最后清理

---

## 四、背景音乐 【人物专属】

- **选定曲目**：**Winds Of Freedom** — Really Slow Motion & Giant Apes（manifest 预分配，勿改）
- **风格**：史诗 / 英雄管弦
- **匹配理由**：「自由之风」匹配其从海牙仲裁到国联大会的跨国外交生涯——一生致力于把民族国家纳入规则的共同天空；史诗管弦质感托起「长期贡献」的厚重感
- **本地路径**：`music_audio/inspiring-electronic/25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Léon_Bourgeois/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录与获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Léon_Bourgeois.yaml` | 入库 yaml（第 4/4.5 步） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步汇报。最重要的事：史实全部锚定 page.md，无载禁写。**

---

## 六、与同批人物的交叉注记 【人物专属，Review 对照用】

- **Wilson 篇**：两人 1919 同在巴黎和会——Wilson 主持国联盟约起草委员会并任和会主席角色，Bourgeois 为法国代表；Wilson 篇记其推翻种族平等提案，本篇记 Bourgeois 支持该提案，两处口径必须一致、各忠于本人页面。
- **国联口径**：Wilson 是「缔造者（founder）」，Bourgeois 是「创建中的突出作用 + 战后大会首任主席」——获奖理由 EN 原句已天然区分，勿互换措辞。
- 1921 年度共享得主 Branting/Lange 的 co-honored 关系只出现在两人各自的篇目，本篇无需涉及。
