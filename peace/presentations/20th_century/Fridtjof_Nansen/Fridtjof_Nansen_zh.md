# OpenPeace 和平奖得主立传提示词（人物：Fridtjof Nansen）

> **本文件是 OpenPeace「诺贝尔和平奖得主立传提示词」的人物专属实例**，以 Fridtjof Nansen（1922 诺贝尔和平奖，国际联盟难民高级专员）为对象。
> 结构母本沿用标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` 骨架，按和平奖人物特点适配。
> 凡标注【模板通用】可复用；标注【人物专属】按 Nansen 替换。直接复制本文件到新对话执行，逐步汇报。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Fridtjof Wedel-Jarlsberg Nansen（弗里乔夫·南森），挪威探险家、科学家、外交官与人道主义者，1922 诺贝尔和平奖独得者。
- **设计哲学**：Nansen 是本批唯一「多重人生」得主（探险家→科学家→建国外交官→国际人道领袖），立传要做成**四幕剧结构**；「身份信息页」与「事业领域结构化表达」骨架务必保留；涉及种族/战争/人物争议的内容一律只作 page.md 明载的客观事实记录。

---

## 二、背景信息 【人物专属】

- **目标人物**：Fridtjof Wedel-Jarlsberg Nansen（1861-10-10 ~ 1930-05-13，享年 68 岁）
- **获奖理由（1922 诺贝尔和平奖，独得）**：
  > "for his leading role in the repatriation of prisoners of war, in international relief work and as the League of Nations' High Commissioner for refugees"（表彰他在战俘遣返与国际救援工作中的领导作用，以及担任国际联盟难民事务高级专员的贡献）
  > 英文原文取自 `peace/nobel_peace_citations.json`，中译照抄名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写。
- **气质关键词**：**极地的征服者、神经元学说的挪威第一辩护人、五万无国籍者的护照**
- **设计母题**：**极地航迹与难民护照（polar tracks and the Nansen passport）**。前半生的冰原航迹线与后半生的救济文书/护照印章构成双母题——同一种「向无人之境推进」的精神贯穿探险与人道两段事业。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Fridtjof_Nansen/page.md`（Wikipedia 全文 + frontmatter：QID Q72292）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - OpenPeace 同批实例：`peace/presentations/20th_century/Woodrow_Wilson/Woodrow_Wilson_zh.md`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报；含「事业领域梳理+入库」（第 4 步）与「社会关系梳理+入库」（第 4.5 步），写入 greatminds 库。

### 第 0 步：通读 page.md 建立事实基准 【人物专属，已核对】

- 生卒：1861-10-10 生于克里斯蒂安尼亚（今奥斯陆）近郊 Store Frøen ~ 1930-05-13 逝于吕萨克 Polhøgda 家中（心脏病），享年 68 岁；非宗教式国葬后火化，骨灰葬于 Polhøgda 树下（葬礼只有音乐：舒伯特《死神与少女》，Eva 生前常唱）
- 国籍：挪威（生于瑞典-挪威联盟时期）；父系源出丹麦（先祖 Hans Nansen 为白海探险者、1654 年哥本哈根市长）
- 家庭：父 Baldur Fridtjof Nansen（律师、挪威最高法院书记官）；母 Adelaide Wedel-Jarlsberg（1877 夏去世）；配偶 Eva Sars（1889-09-06 结婚，1907-12-08 病逝，次女高音歌唱家、女子滑雪先驱、Michael Sars 之女）；二房 Sigrun Munthe（1919-01-17 结婚，婚姻不睦，子女不悦）；五子女（Liv/Kåre/Irmelin/Odd/Asmund，1903 幼子 Asmund 病亡），Odd Nansen 有独立条目
- 教育：Royal Frederick University（今奥斯陆大学）动物学（1880 通过 examen artium，1881 入学）
- 科学任职：卑尔根博物馆动物部策展人（1882–88，与麻风杆菌发现者 Gerhard Armauer Hansen、馆长 Daniel Cornelius Danielssen 共事；神经元学说的挪威第一辩护人，1887 博士论文《中枢神经系统组织学元素的结构与组合》）→ 1897 皇家弗雷德里克大学动物学教授 → 1900 北海研究国际实验室主任、协助创建国际海洋考察理事会（ICES）→ 1908 教席改为海洋学
- 核心事业清单（四幕剧）：
  1. **探险**——1888 首次横越格陵兰冰盖（东→西，49 天，六人小队含 Otto Sverdrup/Samuel Balto/Ole Nielsen Ravna 等）；1893–96 Fram 号北极漂流探险，抵达北纬 86°14′ 纪录；发明南森雪橇/南森炉/分层穿衣法，影响一代极地探险（给 Scott 提供装备建议）
  2. **科学**——《最北之境》（Farthest North，1897）；Fram 科学成果六卷报告；Nansen 采水器（Nansen bottle）；与 Ekman 的数据合作确立埃克曼螺旋；1909 与 Bjørn Helland-Hansen 合著《挪威海物理海洋学》；1910–14 多次海洋学航次；1911《北方雾国》（Nord i Tåkeheimen）
  3. **建国与外交**——1905 瑞典-挪威联盟解体中为分离派撰文著书（1905-05-17 演讲）、密使赴哥本哈根劝丹麦卡尔王子接受挪威王位（即 Haakon VII）；1906–08 驻伦敦首任公使，谈成保障挪威独立的《完整条约》（1907-11-02 签署）
  4. **国际人道**——1917 华盛顿粮食使命（自签协定换配给制）；1920 起任国联代表并主持约 50 万战俘遣返（至 1922 最终报告 427,886 人遣返约 30 国）；1921-09-01 出任国联难民事务高级专员（英国代表 Philip Noel-Baker 提议）；俄国饥荒救济（Nansen Mission，与苏俄外长 Chicherin 签援助协议）；发明南森护照（无国籍者身份证件，后获 50+ 国承认）；1922–23 洛桑会议后主持希土人口互换方案；1925 起为亚美尼亚难民奔走（主要助手 Vidkun Quisling）；1926《禁奴公约》签署人；促成德国 1926-09 加入国联；1926 当选圣安德鲁斯大学校长（首位外籍人士）
- 荣誉：Nobel Peace Prize 1922（奖金悉数捐国际救援）；挪威圣奥拉夫大十字带颈链、法国荣誉军团勋章、英国皇家维多利亚大十字等（infobox 全列，挑主要）
- 关键时间线（15–20 节点）：1861 生 → 1880 examen artium → 1882 Viking 号猎豹船科考 → 1882–88 卑尔根博物馆 → 1887 博士论文 → 1888 格陵兰横越 → 1889 凯旋+与 Eva 结婚 → 1890 公布 Fram 计划 → 1893–96 Fram 探险 86°14′N → 1897 教授+《最北之境》→ 1900 北海实验室主任 → 1905 联盟解体+密使 → 1906–08 驻伦敦公使 → 1907-12-08 Eva 病逝 → 1908 教席改海洋学 → 1913 西伯利亚之行 → 1917 华盛顿粮食使命 → 1919-01-17 续弦 Sigrun → 1920 战俘遣返 → 1921-09-01 难民高级专员 → 1922 诺奖+南森护照 → 1923《亚美尼亚与近东》→ 1926 圣安德鲁斯校长+禁奴公约 → 1930-05-13 逝世

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/` 下建 `Fridtjof_Nansen/`；Makefile 设 `MAIN=Fridtjof_Nansen_zh`
- 肖像：page.md 内嵌多幅照片（1890 年标准像、Fram 探险照、1930 Bundesarchiv 晚年照等），优先取 1890 年肖像 500px 下载；失败按兄弟项目经验走 Commons Special:FilePath 回退
- 插图建议：格陵兰横越路线图（Nansen_Greenland_Crossing_Map.png）与南森护照（Nansenpass.jpg）双插图

### 第 4 步：事业领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | humanitarian aid | 人道救援 | 战俘遣返、饥荒救济、难民高级专员，诺奖理由核心 | 人道三连页 |
| 1 | oceanography | 海洋学 | 1908 教席、Nansen 采水器、挪威海研究 | 科学页 |
| 2 | polar exploration | 极地探险 | 格陵兰横越、Fram 探险、装备发明 | 探险两页 |
| 3 | neuroanatomy | 神经解剖学 | 卑尔根时期、神经元学说辩护、1887 博士 | 科学页 |
| 4 | diplomacy | 外交 | 驻伦敦公使、国联代表、德国入盟斡旋 | 外交页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

> 只收 page.md 明载关系；note 简洁，Quisling 行只作客观事实记录。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Eva Sars | 无向 | 1889 结婚，1907 病逝；次女高音歌唱家 |
| spouse | Sigrun Munthe | 无向 | 1919 结婚，婚姻不睦 |
| parent-child | Baldur Fridtjof Nansen | 无向 | 父亲，律师 |
| parent-child | Odd Nansen | 无向 | 儿子，五子女中具独立条目者 |
| colleague | Gerhard Armauer Hansen | 无向 | 卑尔根博物馆共事，麻风杆菌发现者 |
| colleague | Daniel Cornelius Danielssen | 无向 | 卑尔根博物馆馆长 |
| colleague | Walfrid Ekman | 无向 | 以 Fram 观测数据助其确立埃克曼螺旋 |
| colleague | Bjørn Helland-Hansen | 无向 | 1909 合著《挪威海物理海洋学》 |
| colleague | Roald Amundsen | 无向 | 让予 Fram 号供其探险，后为其南極改向背书 |
| colleague | Philip Noel-Baker | 无向 | 英国代表，促其 1921 出任难民高级专员 |
| colleague | Vidkun Quisling | 无向 | 亚美尼亚救援主要助手，后为二战纳粹合作者（page.md 客观明载） |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#16324F`（极夜深蓝——冰原与北海，manifest 预分配，勿改）
- **辅色**：诺奖香槟金 `#C9A227`
- **四分类色（badgeA–D）**：`#4C5FD5`（探险与极地）· `#0E7C7B`（海洋学）· `#E07B30`（建国外交）· `#C4204F`（人道救援与护照）
- **背景母题**：雪原等高线 + 航迹虚线 + 护照印章圆框

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页，四幕剧】

```
00  OpenPeace 项目首页（\input 项目首页模板）
01  封面 — 极地与人道的双重远征 / Fridtjof Nansen 1861–1930 + badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/全名/国籍/教育/任职/荣誉/核心领域）
03  第一幕·滑雪少年 (1861–1882) — Store Frøen、速滑全国纪录、Viking 号科考
04  卑尔根与神经元 (1882–1888) — Hansen/Danielssen、神经元学说、1887 博士
05  格陵兰横越 (1888) ★核心页 — 东进西出无退路哲学、49 天、六人小队
06  Fram 探险：86°14′ (1893–1896) ★核心页 — 漂流计划、弃船向北、纪录与荣誉
07  《最北之境》与海洋学 (1897–1908) — 教授、北海实验室、Nansen bottle、Ekman spiral
08  第二幕·建国外交 (1905–1908) — 联盟解体、哥本哈根密使、伦敦公使、《完整条约》
09  第三幕·战时人道 (1914–1921) — 华盛顿粮食使命、战俘遣返 427,886 人
10  难民高级专员与南森护照 (1921–1922) ★核心页 — 高专任命、俄国饥荒、护照 50+ 国
11  诺贝尔和平奖 (1922) — 获奖理由原句、洛桑闻讯、奖金悉数捐救援
12  希土互换与亚美尼亚 (1923–1928) — 人口互换、亚美尼亚家园计划、圣安德鲁斯校长、禁奴公约
13  第四幕·晚年与身后 (1929–1930) — Polhøgda 逝世、Nansen 国际难民办公室 1938 诺奖、Nansen 奖章 1954
14  遗产：从冰原到国际难民制度
15  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

- 版式沿用标杆：`\plainbar`/`\deckbackground`/`\sectiontitle` 骨架可整体复用 Kenneth_G_Wilson_zh.tex；每写一页 make，溢出修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距 → 调 y 坐标
- 品牌口径统一：结尾页底部品牌写 `OpenMathAI`；引号用半角 `" "`
- OpenPeace 品牌口径：封面国籍行 `\faIcon{globe}\enspace Norway`；本篇独得，无共享标注

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方 citation 用 json 原句（repatriation…relief work…High Commissioner）；page.md 洛桑段另载一段更长的 committee 措辞引文，两者是不同文本，勿混用，立传一律用官方 citation |
| 独得 | 1922 独享，无共同得主，勿从 Nansen Office（1938 得奖）反推共享 |
| 北纬纪录 | 86°14′（Fram）；1900 被 Abruzzi 队 86°34′ 超越——两个数字勿混 |
| 奖金去向 | 1922 奖金悉数捐国际救援，勿写「捐给国联」或「留用」 |
| Quisling | 仅客观记录「亚美尼亚救援主要助手，后为二战纳粹合作者」，禁加评价或展开其战后事迹（红线） |
| 婚姻 | Eva（1889–1907）与 Sigrun（1919–1930）两段；Sigrun 婚姻不睦、子女不悦为 page.md 明载，仅客观一句；Kathleen Scott 绯闻为 Huntford 主张且被 Louisa Young 否认，若提必须两说并陈或干脆不写 |
| 神经科学定位 | Nansen 是神经元学说的「挪威第一辩护人」、研究下等海洋动物中枢神经系统；Cajal 因同一课题获 1906 诺奖——勿写「Nansen 与 Cajal 共同发现」 |
| 无神论者 | page.md 明载 atheist + 国葬非宗教式，可客观记入，勿引申宗教评论 |
| Fram 归属 | Fram 船 1909 前后让予 Amundsen；Amundsen 改向南极时 Nansen 站在他一边——两件事都在 page.md，勿写「Nansen 反对」 |
| 人口互换 | 希土互换方案含「50 万在希土耳其人返回土耳其+财政补偿」，争议与成功两面都写 |
| 译名 | Nansen passport 译「南森护照」；Integrity Treaty 译《挪威完整条约》；Farthest North 译《最北之境》；Nansen bottle 译「南森采水器」 |
| 葬礼 | 非宗教式国葬+火化+Polhøgda 树下，只放音乐（舒伯特），细节可写且动人，勿添仪式描写 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Nansen passport | 南森护照 | 无国籍者证件，50+ 国承认 |
| High Commissioner for Refugees | 难民事务高级专员 | 国联职位，1921 |
| Fram expedition | 前进号探险 | 1893–96 漂流北极 |
| Greenland crossing | 格陵兰横越 | 1888，首次 |
| Nansen bottle | 南森采水器 | 深层海水采样 |
| Ekman spiral | 埃克曼螺旋 | 风生流理论 |
| population exchange | 人口互换 | 希土 1922–23 |
| Integrity Treaty | 《挪威完整条约》 | 1907 |
| Fatherland League | 祖国联盟 | 1924 反共政治团体，共同创建者 |
| Slavery Convention | 禁奴公约 | 1926 签署人 |
| neuron doctrine | 神经元学说 | 挪威第一辩护人 |
| Farthest North | 《最北之境》 | 1897 畅销书 |

### 引语白名单 【人物专属，仅 page.md 载有英文原文者可入引文框】

| 原文（节选） | 场景 | 出处 |
|------|------|------|
| "Now have all ways of retreat been closed… to a free Norway" | 1905-05-17 宪法日演讲 | 联盟解体 |
| "Never in my life have I been brought into touch with so formidable an amount of suffering." | 1920 战俘遣返报告 | 国联大会 |
| "There was in various transatlantic countries such an abundance of maize…" | 俄国饥荒救济的苦涩总结 | 饥荒节 |
| "We all have a Land of Beyond to seek in our life…" | 圣安德鲁斯校长就职演讲 | 1926 |
| "To talk of the right of revolution… idiotic nonsense." | 祖国联盟成立大会 | 1924 |
| "He found an unknown grave under the clear sky of the icy world…" | 悼念 Amundsen 广播 | 1928 |

> 白名单之外一律转述不引号；中文引号内不写「原话」除非 page.md 有英文原文（红线）。

### 第 10 步：完成判据 【模板通用】

- pdf 0 error、溢出达标（vbox ≤10pt / hbox ≤50pt）、逐页目检通过
- DB `has_social_data=1`、fields≥4、relations≥2；yaml 与提示词第 4/4.5 步完全一致
- 目录内临时目检图（preview/）最后清理

---

## 四、背景音乐 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（manifest 预分配，勿改）
- **风格**：史诗 / 探索 / 电子
- **匹配理由**：「新大陆」是 Nansen 一生的字面写照——格陵兰冰盖、北极浮冰、西伯利亚铁路、亚美尼亚重建，每一步都是向「无人之境」的推进；曲目气质同时承载探险的辽阔与人道的温度，与本篇四幕剧结构天然对位
- **本地路径**：`music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Fridtjof_Nansen/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录与获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Fridtjof_Nansen.yaml` | 入库 yaml（第 4/4.5 步） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

---

## 六、与同批人物的交叉注记 【人物专属，Review 对照用】

- **Wilson/Bourgeois/Branting/Lange 篇**：Nansen 的国联角色是「难民高级专员 + 战俘遣返 + 挪威代表」，与前四人（缔造者/大会首任主席/把瑞典带进国联/常驻代表）四层角色互不重叠；洛桑会议（1922–23）与 Bourgeois 无直接交集，勿混写。
- 1905 瑞挪联盟解体：Branting 篇（瑞典反战）与 Nansen 篇（挪威分离派）是同一场危机的两面，两篇各忠于本人页面、口径不冲突。
