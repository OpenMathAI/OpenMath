# Leo Esaki（江崎玲于奈）立传提示词

> qid=Q179852 · 1925-03-12 生（在世）· 日本物理学家 · 20 世纪 · 1973 诺贝尔物理学奖
> 本地 Wikipedia 数据源：`physicist/presentations/20th_century/20th_century/Leo_Esaki/`（page.md + metadata.json + images.txt）
> ★ 国籍裁定：总名单 1973 行将 Esaki 国籍写为 "United States" 系错——以 page.md（"Japanese physicist"，生于大阪）与 metadata（Japan）为准，封面国籍徽章写「日本」。

---

## 0. 正文形式说明（参考物理学家标杆 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**。物理学家立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。`images.txt` 全为国旗/图标小图——**无任何可用肖像**，装饰圆占位（`\faIcon{user}\enspace Portrait`）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 日本`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承（工业研究体制下无传统博士导师——按 page.md 如实处理）、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色（诺奖金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「势垒 / 隧穿通道」母题（气泡被细窄通道贯穿）。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Leo Esaki（江崎 玲於奈，Esaki Reona）
- **生卒**：1925-03-12 生于大阪——**在世**（截至本页 Wikipedia 所载；生卒行写 "1925-03-12 – "，勿加卒年）
- **国籍**：日本
- **身份**：物理学家（工业研究出身：索尼前身 → IBM → 筑波大学校长）
- **家庭**：女儿 Anna Esaki 嫁 Craig S. Smith（《纽约时报》前上海站站长、《华尔街日报》前中国站站长）；妻子 page.md 未载——禁写
- **教育轨迹**：东京帝国大学（现东京大学）物理——B.S. 1947、Ph.D. 1959（博士学位是在工业研究取得成果后回校获得的）
- **Known for**：半导体隧穿、隧道二极管（江崎二极管）、超晶格、量子阱
- **研究领域**：物理

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **战后日本与神户工业（1947–1956）**：东京帝大物理毕业，加入 Kobe Kogyo Corporation——从战败废墟中起步的固体物理研究。
2. **东京通信工业主任物理学家（1956）**：即索尼前身——其获奖研究全部完成于索尼时期。
3. **隧道二极管（1957）**：发现锗 p–n 结宽度减薄时，电流-电压特性由隧穿效应主导；电压增大电流反而减小（负阻）——这是固体中隧穿效应的首次演示，也是第一个量子电子器件——隧道二极管（江崎二极管）的诞生。
4. **移美 IBM（1960–）**：加入纽约约克敦海茨的 Thomas J. Watson 研究中心；1967 年获聘 IBM Fellow。
5. **超晶格预言（1969）**：预言在半导体晶体中引入人工一维周期性结构变化可诱导微分负阻效应——半导体超晶格；其"分子束外延"薄膜晶体生长方法可在超高真空下精确调控。
6. **拒稿风波（1987 自述，原文可引）**："The original version of the paper was rejected for publication by *Physical Review* on the referee's unimaginative assertion that it was 'too speculative' and involved 'no new physics.' However, this proposal was quickly accepted by the Army Research Office..."——被拒的开创性思想后来长成一个领域。
7. **超晶格实现（1972）**：在 III-V 族半导体中实现超晶格概念；此后这一概念影响金属、磁性材料等众多领域。
8. **回日任筑波大学校长（1992–1998）**：在美三十余年后回日本执掌筑波大学。
9. **1973 诺贝尔物理学奖**：与 Giaever 共享一半（获奖理由中文口径"表彰他们分别关于半导体和超导体中隧穿现象的实验发现"——Esaki 对应半导体、Giaever 对应超导体），Josephson 独得另一半；诺奖演讲（1973-12-12）题为 "Long Journey into Tunnelling"。
10. **五个"不要"（1994 Lindau，原文可引）**：在林道诺奖得主会议上提出创造性人生的五条戒律——①不要被过去的经验困住；②不要过度依附本领域的任何权威（比如大教授）；③不要紧握不需要的东西；④不要回避冲突；⑤不要忘记童年时代的好奇心。两个月后诺贝尔物理学委员会主席 Carl Nordling 即在自己的演讲中引用。
11. **奖项长廊**：Nishina Memorial Prize 1959（引文即 "Invention of the Esaki diode"）、IRE Morris Liebmann Memorial Prize 1961、Stuart Ballantine Medal 1961、International Prize for New Materials 1985（与 Leroy Chang、Raphael Tsu 共享）、Harold Pender Award 1989、IEEE Medal of Honor 1991、Japan Prize 1998。
12. **会籍与纪念**：APS Fellow（1960）、日本学士院会员（1975）、美国国家科学院与国际国家工程院外籍会员（1976/1977）、美国哲学学会会员（1991）；2015 年筑波中央公园立起朝永振一郎、江崎玲于奈、小林诚三人铜像。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（日本藍绀青） | `#26428B` | 日本藍 / 工业研究的深蓝 |
| 强调色（诺奖金） | `#C9A227` | 诺贝尔奖 / 尊崇 |
| 分类色 1（半导体隧穿 — 亮蓝） | `#4169B8` | 隧道二极管 / p–n 结 |
| 分类色 2（负阻与器件 — 赭橙） | `#D0603A` | 负阻特性 / 量子电子器件 |
| 分类色 3（超晶格与量子阱 — 青） | `#2E8B8B` | 超晶格 / 分子束外延 |
| 分类色 4（工业与传承 — 石板灰） | `#5C6B73` | 索尼 → IBM → 筑波 / 五个不要 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落，**被细窄通道贯穿**），呼应「电子隧穿势垒」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：史诗 / 推进 / 突破前夕（穿过势垒的意象）
- **选定曲目**：Inspiring Electronic 合辑 **Through the Darkness**（Audiomachine / 史诗 / 黑暗 / 推进），匹配"电子隧穿势垒"与"从战败废墟到量子器件"的穿越叙事。
- **落地文件**：`physicist/presentations/20th_century/Leo_Esaki/Through the Darkness.wav`（复制自音乐库，不入 git）。
- **匹配理由**：隧穿的物理意象是"穿过看似不可穿越的屏障"——Through the Darkness 的推进感与这一母题同构；江崎的人生亦是从战后日本穿越到量子电子学前沿的"长旅程"（其诺奖演讲标题即 Long Journey into Tunnelling）。组内五人不重复。

## 4. Slide 规划（约 15 页，Wilson 式结构）

1. **封面**（`\titleslide`）：顶部标签「隧道二极管之父 · 日本」+ Leo Esaki 1925– + 装饰圆占位 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左装饰圆 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 任职 / 主要荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：隧道二极管 / 负阻 / 超晶格与量子阱 / 五个不要
4. **战后日本与神户工业**（1925–1956）：东京帝大、Kobe Kogyo
5. **索尼岁月与隧穿发现**（1956–1957，★ 概念页）：锗 p–n 结减薄、负阻（具体 I–V 公式 page.md 未载——用概念框呈现"电压增大电流反减"）
6. **隧道二极管：首个量子电子器件**：固体中隧穿的首次演示、从效应到器件
7. **移美 IBM**（1960–1967）：Watson 研究中心、IBM Fellow
8. **超晶格预言与拒稿风波**（1969）：人工一维周期结构、Physical Review 拒稿（1987 自述引文）
9. **超晶格实现与影响**（1972–）：III-V 族实现、辐射金属与磁性材料
10. **回日：筑波大学校长**（1992–1998）
11. **1973 诺贝尔物理学奖**：份额结构（Esaki+Giaever 一半 / Josephson 一半）、中文口径、演讲标题
12. **五个"不要"**（1994 Lindau，★ 引语页）：五条原文 + Nordling 引用
13. **荣誉长廊与会籍**：Nishina 1959 → Japan Prize 1998
14. **纪念与"最年长"**：筑波铜像（2015）、在世最年长的日本诺奖得主（时点表述）
15. **结尾**：长旅程——从隧穿到超晶格

## 5. 史实陷阱与敏感点（终审必须检查）

- **★ 国籍**：总名单 1973 行国籍 "United States" 系错——以 page.md 为准写「日本」；本条属总名单待修正事项。
- **★ "首位"禁写**：page.md 无任何"日本首位 X 诺奖"表述——禁写"日本首位科学诺奖"等；page.md 有载的唯一比较级表述是"自南部阳一郎 2015 年去世后，江崎是（当时）在世最年长的日本诺奖得主"——写入时须带时点限定（"截至 Wikipedia 页面所载"）。
- **出生地**：page.md infobox 为 Osaka；metadata place_of_birth "Takaida" 为噪声——以 page.md 为准写大阪。
- **在世人物**：1925-03-12 生、在世——生卒行 "1925-03-12 – "，勿加卒年、勿写"享年"。
- **★ 诺奖份额结构写准**：Esaki 与 Giaever 共同获得一半（理由为"分别关于半导体和超导体中隧穿现象的实验发现"），Josephson 独得另一半——勿写"三人平分"。
- **发现 vs 发明**：1957 年发现隧穿效应并发明隧道二极管（page.md 两种表述并存）；Nishina 1959 引文即 "Invention of the Esaki diode"——"Esaki diode" 之名可在此引文中出现；正文避免现代回望式命名造成年代混淆。
- **拒稿引语**：仅引 1987 年自述原文（含 'too speculative' / 'no new physics'），不自行扩写审稿人语境、不引申"物理审查制度"评论。
- **超晶格合作者**：Chang 与 Tsu 仅出现在 1985 International Prize for New Materials 的 shared 注记语境——勿写成超晶格论文共同作者（本篇 page.md 未载二人合著关系）。
- **家庭**：仅女儿 Anna 与女婿 Craig S. Smith（职务按 page.md）；妻子 page.md 未载——禁写。
- **教育**：page.md infobox 仅东京帝国大学（grad. 1947, 1959）；metadata 另列 Kyoto University / Third Higher School——正文以 page.md 为准；如入库以 metadata 为源单独注明。
- **metadata 噪声**：metadata employer 另列京都大学、横滨药科大学、关西学院大学等 page.md 未载的机构——正文不写。
- **引语纪律**：可引原文仅两处——1987 拒稿自述、1994 五个"不要"列表；其余全部间接转述。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q179852 | 待写入 |
| name_zh | 江崎玲于奈 | 待写入 |
| name_en | Leo Esaki | 待写入 |
| birth_date | 1925-03-12 | 待写入 |
| death_date | （空——在世） | 待写入 |
| nationality | Japan | 待写入 |
| primary_occupation | physicist | 待写入 |
| field_of_work | physics / semiconductor tunneling / superlattices | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **诺奖同届（co-honored 1973）**：Ivar Giaever（共享一半）、Brian Josephson（独得另一半）
- **家庭**：女儿 Anna Esaki；女婿 Craig S. Smith（《纽约时报》《华尔街日报》记者）
- **获奖共享（1985 International Prize for New Materials）**：Leroy Chang、Raphael Tsu
- **任职机构**（机构关系，非人物关系）：东京通信工业/索尼（1956 chief physicist）、IBM T. J. Watson 研究中心（1960 起，1967 IBM Fellow）、筑波大学（1992–1998 校长）
- **会籍**：日本学士院（1975）、美国国家科学院（1976）、美国国家工程院（1977）、美国哲学学会（1991）

## 8. 奖项清单

- 诺贝尔物理学奖（1973，与 Giaever 共享一半；Josephson 独得另一半）
- Nishina Memorial Prize（1959，引文 "Invention of the Esaki diode"）
- IRE Morris Liebmann Memorial Prize（1961，引文见 page.md）
- Stuart Ballantine Medal（1961，引文见 page.md）
- International Prize for New Materials（1985，APS，与 Chang、Tsu 共享；引文见 page.md）
- Harold Pender Award（1989，宾夕法尼亚大学）
- IEEE Medal of Honor（1991，引文见 page.md）
- Japan Prize（1998，引文见 page.md）
- Order of Culture、Person of Cultural Merit、旭日章一等（metadata 载，page.md 奖项表未载——正文不写，如入库以 metadata 为源注明）
- 会籍：APS Fellow（1960）、日本学士院（1975）、美国 NAS（1976）/NAE（1977）国际会员、美国哲学学会（1991）；HKUST 荣誉博士（2001）

## 9. 机构清单

- 教育：东京帝国大学（现东京大学，B.S. 1947 / Ph.D. 1959）
- 任职：Kobe Kogyo Corporation（1947 起）、东京通信工业/索尼主任物理学家（1956–1960）、IBM T. J. Watson 研究中心（1960–1992，1967 IBM Fellow）、筑波大学校长（1992–1998）
- 纪念：筑波中央公园铜像（2015，与朝永振一郎、小林诚并立）

## 10. 终审清单

- [ ] 生卒行 "1925-03-12 – "（在世），出生地大阪
- [ ] 国籍写「日本」（总名单 "United States" 系错，不跟随）
- [ ] 不写任何"日本首位"表述；"最年长"表述带时点
- [ ] 诺奖份额结构：Esaki+Giaever 一半 / Josephson 一半——表述准确
- [ ] 1957 发现效应并发明器件；Nishina 1959 表彰 "Invention of the Esaki diode"
- [ ] 拒稿引语与五个"不要"按原文引用；其余间接转述
- [ ] 家庭只写女儿与女婿；妻子不写
- [ ] 装饰圆占位（无肖像）；品牌 OpenMathAI；半角引号
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `20th_century/Leo_Esaki/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：无肖像，装饰圆占位
- [ ] **国籍**：封面顶部徽章明示日本
- [ ] **引语核对**：1987 拒稿自述与五个"不要"须能在 page.md 找到原文
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一（半角引号 " "）
- [ ] 与同组物理学家（Ivar_Giaever / Brian_Josephson）格式对齐，1973 诺奖份额口径三篇一致

## 12. 研究领域表（第 4 步 fields 入库底稿，与 yaml 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | semiconductor tunneling | 半导体隧穿 | 1957 首次演示固体中的隧穿效应 | 核心页 |
| 1 | tunnel diode | 隧道二极管 | 江崎二极管，首个量子电子器件 | 核心页 |
| 2 | superlattice | 超晶格 | 1969 预言 / 1972 III-V 族实现 | 超晶格页 |
| 3 | quantum well | 量子阱 | 与超晶格一脉相承的人工结构 | 超晶格页 |
| 4 | quantum electronics | 量子电子学 | 隧穿器件开出的领域 | 结尾页 |

## 13. 术语清单（英文 / 中文 / 风险点）

| 英文 | 中文 | 风险点 |
|------|------|------|
| tunnel diode | 隧道二极管 | 又称江崎二极管；命名源于 Nishina 1959 引文语境，正文避免现代回望式命名 |
| negative resistance | 负阻 | 电压增大电流反减；勿写成"负电阻率" |
| p–n junction | p–n 结 | 锗 p–n 结宽度减薄是 1957 发现的前提 |
| superlattice | 超晶格 | 1969 预言 / 1972 实现，两处年份勿混 |
| molecular-beam epitaxy | 分子束外延 | page.md 称其"unique"方法；勿写发明人归属细节 |
| quantum well | 量子阱 | Known for 之一 |
| III-V group semiconductors | III-V 族半导体 | 1972 实现所用的材料体系 |
| five don'ts | 五个"不要" | 1994 Lindau；五条按原文列表，勿增删 |
| Lindau Nobel Laureate Meetings | 林道诺奖得主会议 | 1994 年提出、两个月后 Nordling 引用 |
| Tokyo Tsushin Kogyo | 东京通信工业 | 索尼前身，1956 任主任物理学家 |
| IBM Fellow | IBM Fellow | 1967 年获聘，荣誉职衔勿译"研究员" |
| International Prize for New Materials | 国际新材料奖 | 1985 APS，与 Chang、Tsu 共享（仅 shared 注记，勿写合著） |

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
