# Leopold Ružička（莱奥波德·鲁日奇卡）立传提示词

> qid=Q122996 · 1887-09-13 – 1976-09-26 · 克罗地亚-瑞士化学家 · 20 世纪 · 诺贝尔化学奖（1939，与 Adolf Butenandt 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Leopold_Ružička/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传的 Beamer 格式与提示词结构**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 仅有故居博物馆照与墓照（**均不可作肖像**；infobox 标注 "Ružička in 1935" 但 images.txt 未提供该图）；先尝试 Wikipedia REST API `page/summary` 取 infobox 原图（Commons `Special:FilePath` 回退，250px 改 500px）；404 则用**装饰圆占位**（主色渐变圆 + 首字母 LR），并在 Review 时记录。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 大环与萜烯大师\enspace·\enspace 克罗地亚/瑞士`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Lavoslav Stjepan Ružička、国籍（克罗地亚出生 / 1917 年入瑞士籍）、教育（奥西耶克文理中学 → Karlsruhe）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「大环 / 多员环」母题——大小错落的圆环暗示麝香酮十五元环与灵猫酮十七元环。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如大环酮结构 / 异戊二烯规则。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Lavoslav Stjepan Ružička（通称 Leopold Ružička；ForMemRS）
- **生卒**：1887-09-13 生于克罗地亚-斯拉沃尼亚王国 Vukovar（时属奥匈帝国，今克罗地亚）→ 1976-09-26 逝于瑞士 Mammern（博登湖畔小村），享年 89
- **国籍**：克罗地亚-瑞士——Transleithania（1887–1917）、**Switzerland（1917–1976）**；家庭为工匠与农民，多数是克罗地亚人，有一位捷克曾祖父母
- **身份**：化学家（萜烯、甾体激素、大环香料；ETH Zurich 有机化学教授）
- **家庭**：4 岁丧父（Stjepan），母亲 Amalija Sever 带他与其弟 Stjepan 迁居奥西耶克；两次婚姻——1912 年娶 Anna Hausmann，1951 年娶 Gertrud Acklin（Gertrud Frei 与他合葬苏黎世 Fluntern 公墓）
- **教育轨迹**：
  - 奥西耶克文理中学（Real Gymnasium Osijek）古典科班；本想当神父后改学技术学科
  - 选化学部分因为奥西耶克新开糖厂的就业预期
  - 因生计与政治环境的困顿离乡，入德国卡尔斯鲁厄高等技术学校（Technische Hochschule Karlsruhe）
  - 在 **Hermann Staudinger** 系里学习，1910 年获博士学位；随后随 Staudinger 赴苏黎世任其助理
- **导师**：Hermann Staudinger（博士导师，1953 诺贝尔化学奖得主）
- **研究领域**：有机化学——萜烯与多萜、甾体激素（雄甾酮/睾酮合成）、大环香料分子（麝香酮/灵猫酮）、生物发生的异戊二烯规则

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **武科瓦尔孤儿（1887）**：4 岁丧父，母亲带兄弟迁居奥西耶克；从神父梦到化学路——起因可能只是家乡新糖厂的一个职位。
2. **卡尔斯鲁厄：与 Haber 的插曲**：物理化学教授 Fritz Haber（1918 诺贝尔化学奖得主）曾**反对**其 summa cum laude 学位评定——学术路上的早期波折。
3. **Staudinger 门下（1910）**：在 Staudinger 系里获博士学位并随师赴苏黎世任助理——与除虫菊素（pyrethrins）合成打了五年半交道。
4. **"我们钻错了牛角尖"**：五年半除虫菊素合成工作后他断定方向有误（自述句，page.md 原文引语，见 §5）——由此接触松油醇（terpineol）与香料工业。
5. **与香料工业结盟（1916–1921）**：获 Haarman & Reimer（Holzminden，世界最老香料制造商）支持；1917 年入瑞士籍；1918 年通过 Habilitation；1919 年与 Fornasir 分离出芳樟醇（linalool）。
6. **麝香酮与灵猫酮：大环定音**：率博士生团队证明麝香酮（musk deer）与灵猫酮（civet cat）结构——**首批被证明含六个以上原子环的天然产物**；灵猫酮被推定为十七元环（当时合成技术只知道八元环以内）。
7. **大环合成法**：发展大环合成方法——今称 Ružička reaction / Ružička large ring synthesis；1927 年以此法制备灵猫酮；**首个工业规模合成麝香**（奇华顿前身 Chuit & Naef 命名 Exaltone）。
8. **乌得勒支与回归苏黎世（1927–1929）**：1927 年接任乌得勒支大学有机化学讲席，三年后因瑞士化学工业的优势条件回瑞士；1929 年起住 Freudenbergstrasse 101。
9. **雄甾酮与睾酮（1934–1935）**：1934 年合成雄性激素**雄甾酮**（androsterone）并证明其与甾醇的结构构型关系；1935 年部分合成活性更强的**睾酮**（testosterone）——奠定瑞士工业在甾体激素领域的领先地位；1934–1939 发表 70 篇药用甾体激素论文并申报数十项专利。
10. **ETH 巅峰岁月**：任 ETH Zurich 有机化学教授，实验室成为世界有机化学中心之一；1936 年获哈佛大学荣誉学位。
11. **1939 诺贝尔化学奖**：官方理由 "for his work on polymethylenes and higher terpenes"，"including the first chemical synthesis of male sex hormones"；与 Adolf Butenandt **共享**；1940 年应邀回国在克罗地亚化学家协会演讲《From the Dalmatian Insect Powder to Sex Hormones》。
12. **异戊二烯规则（1953）**：提出 Biogenetic Isoprene Rule（萜烯碳骨架由异戊二烯单元规则或不规则连接构成）——学术生涯巅峰；1952 年与 Jeger 团队分离羊毛甾醇（lanosterol），确立萜烯与甾体的联系。
13. **传承与身后**：二战中失去部分合作者后重建实验室，纳入年轻的 **Vladimir Prelog**（未来诺奖得主）；1957 年退休交棒 Prelog；ETH 设 Ružička Award（1957）；1970 年林道演讲《Nobel Prizes and the chemistry of life》；Vukovar 1977 年建故居博物馆；583 篇论文署名、八个荣誉博士；反对核武器；荷兰名画收藏赠苏黎世美术馆（Kunsthaus Zürich）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（黛蓝 indigo-navy） | `#14324F` | 大环结构的深沉（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（大环香料 badgeMacrocycle） | `#2E5A9E` | 蓝麝香酮 / 灵猫酮 / Exaltone |
| 分类色 2（萜烯 badgeTerpene） | `#1B7A43` | 绿萜烯 / 异戊二烯规则 |
| 分类色 3（甾体激素 badgeSteroid） | `#C9702A` | 橙雄甾酮 / 睾酮合成 |
| 分类色 4（学派传承 badgeLegacy） | `#8C3A5B` | 玫瑰 ETH 学派 / Prelog 接棒 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「十五/十七元大环」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions（文件 `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav`；不要复制 wav 文件，Makefile 直接引用该路径）
- **风格**：乡愁 / 温厚 / 纪录片
- **匹配理由**：
  - "乡愁" 匹配鲁日奇卡的生平弧线——从武科瓦尔的孤儿到瑞士国宝化学家，1940 年回克罗地亚演讲《从达尔马提亚除虫菊粉到性激素》正是乡愁的注脚
  - "温厚" 匹配其晚年气质——反对核武器、名画赠美术馆、基金会奖掖青年
  - 叙事质感匹配「学徒 → Staudinger 门下 → 香料工业 → 大环定音 → 激素合成 → 异戊二烯规则」的漫长学术马拉松
- **时长对齐**：以实际曲目时长与 15 页 × 7 秒 ≈ 105 秒比较，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 大环与萜烯大师 / Leopold Ružička 1887–1976 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名 Lavoslav Stjepan Ružička/国籍变迁/出生地/去世地/教育/博士导师/领域/荣誉）
03  鲁日奇卡的一生 — 高斯式时间线（10 节点：1887→1910→1916→1917→1926→1929→1934→1939→1953→1976）
04  武科瓦尔的孤儿 (1887–1906) — 表格「时间|事件|结果」
05  卡尔斯鲁厄：Haber 的反对与 Staudinger 的赏识 (1906–1910) — 表格「人物|角色|影响」
06  除虫菊与香料工业 (1910–1919) — "钻错牛角尖" 转折 / Haarman & Reimer / 入瑞士籍 / linalool
07  大环定音：麝香酮与灵猫酮 (1920s) — 表格「分子|来源|环员数」+ 公式框：Ružička 大环合成
08  香料工业与乌得勒支 (1921–1929) — Chuit & Naef / Exaltone / CIBA / Utrecht→ETH
09  甾体激素：雄甾酮与睾酮 (1934–1935) — 表格「年份|激素|意义」+ 公式框：雄甾酮→甾醇构型关系
10  1939 诺贝尔化学奖 — 官方获奖理由 + 与 Butenandt 共享 + 1940 克罗地亚演讲
11  异戊二烯规则 (1953) — Biogenetic Isoprene Rule / lanosterol（公式框）
12  ETH 学派与传承 — 九位博士生表格 / Prelog 接棒（1957）/ Ružička Award
13  荣誉与收藏 — 八个荣誉博士 / ForMemRS / Faraday Lectureship（1958）/ 名画收藏 / 反核武器
14  结尾 — 「他从除虫菊粉里嗅出了大环的形状。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1939 共享 | 与 Adolf Butenandt **共享**；两人理由**不同**：Ružička 官方理由 "for his work on polymethylenes and higher terpenes" "including the first chemical synthesis of male sex hormones"；Butenandt 为 "work on sex hormones"——勿互串 |
| 本名 | 本名 **Lavoslav Stjepan Ružička**，通称 Leopold Ružička——身份页两写；克罗地亚语发音注记可加 |
| 国籍口径 | 出生时属奥匈帝国（今克罗地亚）；**1917 年入瑞士籍**；行文"克罗地亚-瑞士"；入库写 Switzerland + Croatia 两条（见 §6），勿写"奥地利籍" |
| Haber 关系 | Fritz Haber 是其**物理化学教授**且曾反对其 summa cum laude 学位——非导师非合作者，入库用 other 类型 |
| 唯一引语 | page.md 唯一直接引语："Toward the end of five and a half years of mainly synthetic work on the pyrethrins I had come to the firm conclusion that we were barking up the wrong tree."（除虫菊素五年半后的自省）——全文仅此一句可作引号原话 |
| "首批"断言 | "the first natural products shown to have rings with more than six atoms" 是 page.md 明载——仅限麝香酮/灵猫酮语境；"first chemical synthesis of male sex hormones" 在获奖理由内——两处 "first" 勿扩大 |
| 环员数 | 灵猫酮**十七元环**（civetone 17-member ring）、麝香酮 3-甲基环十五烷酮（1904 分离，鲁日奇卡方确认结构）——数字勿错 |
| 名字拼写 | Firmenich（page.md 两处拼写 Firmsenech/Firmenech 为变体，用 Firmenich）；香水公司前身 Chuit & Naef（Geneva） |
| Prelog | "young scientist and future Nobel laureate Vladimir Prelog" 进入其实验室、1957 年接掌实验室——colleague；勿写成师承（page.md 未载博士生关系） |
| Jeger | 1952 年 "Oskar Jeger and he supervised a team" 分离羊毛甾醇——一次性合作，**不单独入库**（避免低价值 stub） |
| 婚姻 | 两任妻子：Anna Hausmann（1912）、Gertrud Acklin（1951）——两条 spouse 关系；合葬 Fluntern 是与 Gertrud Frei（Gertrud Acklin 的图注名，注意图注写法 Gertrud Frei） |
| 生日/忌日 | 9 月 13 日生、9 月 26 日逝（1976），享年 89——勿写"生日当天去世"（那是 Haworth） |
| 同名区分 | Leopold Ružička 与 Ruzicka 拼写变体（英文页面亦作 Ruzicka）；His brother Stjepan 与父亲 Stjepan 同名勿混 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q122996 | ✅（metadata.json） |
| name_zh | 莱奥波德·鲁日奇卡 | ✅ |
| name_en | Leopold Ružička | ✅（page.md 规范名，db_id 空；yaml/清单统一用带变音符形式） |
| birth_date | 1887-09-13 | ✅ |
| death_date | 1976-09-26 | ✅ |
| nationality | Switzerland, Croatia（两条带 rank） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：terpenes / steroid hormones / macrocyclic chemistry / natural products，带 rank） | ✅ |
| has_biography | false（立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 门生 / 合作者 / 共同得主**（仅收 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hermann Staudinger | 师→生（博士导师） | 卡尔斯鲁厄其系里获 1910 博士学位，随师赴苏黎世任助理 |
| spouse | Anna Hausmann | 无向 | 1912 年结婚（第一任妻子） |
| spouse | Gertrud Acklin | 无向 | 1951 年结婚（第二任妻子），合葬苏黎世 Fluntern 公墓 |
| advisor-student | George Büchi | Ružička→学生 | infobox doctoral students |
| advisor-student | Duilio Arigoni | Ružička→学生 | infobox doctoral students |
| advisor-student | Arie Jan Haagen-Smit | Ružička→学生 | infobox doctoral students |
| advisor-student | Moses Wolf Goldberg | Ružička→学生 | infobox doctoral students |
| advisor-student | Klaus H. Hofmann | Ružička→学生 | infobox doctoral students |
| advisor-student | George Rosenkranz | Ružička→学生 | infobox doctoral students |
| advisor-student | Cyril A. Grob | Ružička→学生 | infobox doctoral students |
| advisor-student | Edgar Heilbronner | Ružička→学生 | infobox doctoral students |
| advisor-student | Albert Eschenmoser | Ružička→学生 | infobox doctoral students |
| colleague | Vladimir Prelog | 无向 | 二战后进入其实验室的未来诺奖得主；1957 年退休时接掌实验室 |
| co-honored | Adolf Butenandt | 无向 | 1939 诺贝尔化学奖共同得主 |
| other | Fritz Haber | 无向 | 卡尔斯鲁厄物理化学教授，曾反对其 summa cum laude 学位评定 |

> **禁入库名单（metadata-only / 背景人物）**：Fornasir（分离 linalool 的合作者，page.md 一笔带过且为姓氏）、Oskar Jeger（一次性合作分离 lanosterol）、父亲 Stjepan 与母亲 Amalija Sever（未载学术关系）、弟 Stjepan、Chuit & Naef / CIBA / Haarman & Reimer / Sandoz（机构非人物）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1939，与 Adolf Butenandt 共享）
- Marcel Benoist Prize（1938）
- Faraday Lectureship Prize（1958）
- Werner Prize（infobox 载）
- Foreign Member of the Royal Society，ForMemRS（1942）
- US National Academy of Sciences 国际院士（1944）
- Royal Netherlands Academy of Arts and Sciences 外籍院士（1940）
- 八个荣誉博士学位（含 1936 Harvard 荣誉学位；萨格勒布大学荣誉博士等）
- Order of the Yugoslav Flag with Golden Wreath（1974）
- 荣誉会员：Polish Chemical Society（1965）、American Academy of Arts and Sciences、Yugoslav Academy of Sciences and Arts 荣誉院士
- 纪念：Ružička Award（ETH，1957 设立）、Vukovar 故居博物馆（1977）

## 9. 机构清单

- 教育：Real Gymnasium Osijek（古典科班）、Technische Hochschule Karlsruhe（PhD 1910，Staudinger 系）
- 任职：苏黎世（Staudinger 助理）、ETH Zurich 与 University of Zurich（1918 高级讲师，1923 荣誉教授）、Utrecht University（1927 有机化学讲席，三年）、ETH Zurich（有机化学教授，至 1957 退休；实验室交棒 Prelog）
- 工业合作：Chuit & Naef / Firmenich（Geneva）、Haarman & Reimer（Holzminden）、CIBA（Basel）、晚年任 Sandoz AG 顾问
- 纪念：ETH Ružička Award（1957）、Vukovar Leopold Ružička Memorial Museum（1977）、苏黎世 Kunsthaus Ružička 收藏、档案藏 ETH

## 10. 终审清单

- [ ] 生卒 1887-09-13 / 1976-09-26，享年 89；出生地 Vukovar、去世地 Mammern
- [ ] 1939 与 Butenandt 共享；两条官方理由互不串用；"first chemical synthesis of male sex hormones" 仅在获奖理由内
- [ ] 本名 Lavoslav Stjepan Ružička；1917 年入瑞士籍；国籍两条入库
- [ ] Haber 为物理化学教授（反对学位），非导师；博士导师 Staudinger 表述准确
- [ ] 麝香酮/灵猫酮环员数（3-甲基环十五烷酮 / 十七元环）准确；"首批>六元环天然产物" 原句语境
- [ ] 唯一引语（除虫菊素自省句）原文准确；其余全部间接转述
- [ ] 九位博士生一一对应 infobox；Prelog 为同事非学生
- [ ] 中文引号内无 page.md 无法溯源的"原话"
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Leopold_Ružička/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 仅故居/墓照——REST API / Special:FilePath 尝试结果与占位方案记录回写本节
- [ ] **国籍**：封面顶部明示克罗地亚/瑞士
- [ ] **引语核对**：全文唯一引语为除虫菊素自省句，其余转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 模板）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，执行者不改。
> **最重要的事：每写一页就 make，看到溢出就修。**
