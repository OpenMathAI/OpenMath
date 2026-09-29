# 文学家立传提示词（John Galsworthy）

> **OpenLiterature 人物专属立传提示词**：John Galsworthy（约翰·高尔斯华绥，1932 诺贝尔文学奖，英国小说家与剧作家，《福尔赛世家》作者）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框——用名句引文框/意象图式/书影替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：John Galsworthy（1867–1933），爱德华时代小说与社会问题剧双栖作家。
- **设计哲学**：文学家立传必须有「身份信息页」，并以**代表作书影/名句引文框/意象图式**替代公式框——本篇设计母题为「福尔赛宅邸的窗」。

---

## 二、背景信息 【人物专属】

- **目标文学家**：John Galsworthy（1867-08-14 ~ 1933-01-31，享年 65 岁）
- **气质关键词**：**福尔赛世家的缔造者、社会问题剧旗手、PEN 国际首任主席**
- **官方获奖理由（禁止改写）**：
  - EN: "for his distinguished art of narration which takes its highest form in The Forsyte Saga"
  - 中译（取自 CITATION_ZH）：「表彰其卓越的叙事艺术，其最高成就体现于《福尔赛世家》」
  - 注：1932 年末获奖时已病重，未能赴斯德哥尔摩领奖；1933-01-31 去世。
- **设计母题**：**福尔赛宅邸的窗**。上流中产家族三代的全景小说——玻璃橱窗里陈列的财产、婚姻与体面；视觉语言用爱德华时代客厅、窗格分割的伦敦天际线、三联画式三代人剪影。
- **本地数据源**：`literature/presentations/pages/20th_century/John_Galsworthy/page.md`（+ 同目录 `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/John_Galsworthy
- **肖像**：第 0 步待下载（1930 年 correcting a manuscript 肖像照；images.txt 无 URL 则回退 REST API / Special:FilePath，404 用装饰圆占位）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】（已核对 page.md）

- 生卒：1867-08-14 生于萨里郡泰晤士河畔金斯敦 Parkfield（今 Galsworthy House）~ 1933-01-31 逝于伦敦汉普斯特德，享年 65 岁（死因：脑血栓、动脉硬化，或兼脑瘤）
- 家庭：父 John Galsworthy senior（1817–1904，伦敦知名律师，Devon 农家出身经船具业致富，为 Old Jolyon 原型）；母 Blanche Bailey née Bartleet（1837–1915，与父 20 岁年龄差、关系紧张）；妹 Lilian Sauter（夫为德国画家 Georg Sauter，一战被拘后驱逐）；外甥 Rudolf Helmut Sauter
- 教育：家庭女教师 → 1876 Bournemouth 预备学校 Saugeen → 1881 Harrow School（校足球队、舍队队长）→ 1886 入牛津 New College 攻法律，1889 二等学位；牛津剧社经历、单恋 Sybil Carlisle
- 律师与旅行：1890 Lincoln's Inn 取得律师资格；1891 加拿大行；1892–93 南太平洋—澳—南非之旅（赴萨摩亚欲访 Stevenson 未果）；对律师业自陈「几乎不执业且深恶之」
- **1893 年 4 月**阿德莱德—开普敦航程中结识大副 **Joseph Conrad**（尚未开始写作生涯），成为终身挚友
- 爱情：1895 与堂兄 Arthur 之妻 Ada Galsworthy 相恋（秘密恋情至 1904 父卒）；1905-09-23 结婚，无子女，白头至终；Ada 被传记家视为其小说与戏剧发展的重要推手；《福尔赛世家》中 Irene 与 Soames 的原型来自 Ada 的首段婚姻
- 早期笔名 **John Sinjon**（父在世时前四本书署此名）
- 1906 奇迹之年（annus mirabilis）：《有产业的人》（The Man of Property，Heinemann 出版）与首剧《银匣》（The Silver Box，皇家宫廷剧院，Granville-Barker 导演）
- 三部曲体系：The Forsyte Saga（1906/1920/1921，1922 合卷）→ A Modern Comedy（1924/1926/1928，1929 合卷）→ End of the Chapter（1931/1932/1933 遗著，1935 合卷）
- 戏剧：28 部职业剧；Strife（1909，康沃尔锡矿劳资）、Justice（1910，抨击独囚）、The Eldest Son（1912，女性压抑）、The Mob（1914，沙文主义与战争）、The Skin Game（1920，首个票房大成功）、Old English（1924）
- 社会运动：戏剧审查改革委员会（与 J. M. Barrie、Gilbert Murray 创立，Archer、Granville-Barker 强力声援）；动物福利（人道屠宰，1912–13）；监狱改革、女权、最低工资；自列运动清单（见 page.md 注 5）
- 一战：母国立场矛盾（反战又认为须保卫比利时）；妹婿 Sauter 被拘；捐美版税给战争慈善；赴法志愿做按摩师疗伤兵（1915–1917）
- 荣誉：1917 拒绝骑士爵位（"no artist of Letters ought to dally with titles"）；1929 接受功绩勋章 OM；七校荣誉学位；1931 牛津 Romanes Lecture「Shakespeare and Spiritual Life」
- PEN：1921-10 国际笔会（PEN）创立于伦敦，任主席至 1933-10 去世（继任 H. G. Wells）
- 1932 诺贝尔文学奖：1933-01-31 去世；私人葬礼后威斯敏斯特教堂追思会（首相 Ramsay MacDonald 等出席）；骨灰遵遗嘱由飞机撒在南唐斯丘陵
- 声誉：现代主义同代人（Woolf 称之"爱德华时代人"、Lawrence 1927 攻击）贬其作；1967 BBC 26 集《福尔赛世家》电视剧引发作品再热
- 关键时间线：1867 生 → 1886 牛津 → 1890 取得律师资格 → 1893 遇 Conrad → 1895 与 Ada 相恋 → 1897 首书 From the Four Winds（自费）→ 1904 父卒、《岛上的法利赛人》→ 1906 《有产业的人》《银匣》→ 1909 Strife → 1910 Justice → 1918 Five Tales → 1920 The Skin Game、In Chancery → 1921 To Let、创 PEN 任主席 → 1922 Forsyte Saga 合卷 → 1926 购 Bury House → 1929 OM、A Modern Comedy 合卷 → 1931 Romanes Lecture → 1932 诺奖 → 1933-01-31 去世

### 第 1–3 步：目录 / Makefile / 图片 【模板通用】

- `literature/presentations/20th_century/John_Galsworthy/` + `images/`；Makefile 改 `MAIN=John_Galsworthy_zh`；肖像 `file` 验证。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | family saga novel | 家族史诗小说 | 福尔赛编年史三代人全景 | 核心页 |
| 1 | social problem drama | 社会问题剧 | 28 部剧的社会主题传统（与 Shaw、Granville-Barker 并列） | 戏剧页 |
| 2 | naturalism | 自然主义 | Ibsen 式现代主义剧作法、含蓄自然的舞台呈现 | 戏剧页 |
| 3 | social criticism | 社会批评 | 小说戏剧与运动清单：审查/监狱/女权/动物福利 | 运动页 |

- 入库：`MySQL/seed_person.py data/John_Galsworthy.yaml`。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Ada Galsworthy | 无向 | 1905 结婚；鼓励其写作，被传记家视为其发展的重要影响 |
| influence | Ivan Turgenev | 对方→本人 | 研习其作学习文学技巧 |
| influence | Guy de Maupassant | 对方→本人 | 研习其作学习文学技巧 |
| colleague | Joseph Conrad | 无向 | 1893 航程中相识的终身挚友 |
| colleague | George Bernard Shaw | 无向 | 同为社会问题剧作家并称 |
| colleague | Harley Granville-Barker | 无向 | 导演其《银匣》，审查改革同盟 |
| colleague | J. M. Barrie | 无向 | 戏剧审查改革委员会共同创立 |

### 第 5 步：配色 【人物专属】

- 主色 `#1E4D3B`（分批预分配，深英伦绿）+ 香槟金 `C9A227` + badgeA–D（badgeA 家族 `#3E7C5B` / badgeB 戏剧 `#8A5A2E` / badgeC 运动 `#4E6E8E` / badgeD 荣誉 `#B08A2E`）。
- 背景母题：窗格矩形与三联画框。

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面头像+细边框；封面国籍行 `United Kingdom`。
2. **身份信息页必做**（生卒/国籍/出生地 Kingston upon Thames/教育 Harrow+New College Oxford/配偶 Ada/任职 PEN 主席/荣誉 OM+Nobel 1932/核心领域）。
3. 品牌口径统一 `OpenMathAI`；引号半角 `" "`。
4. 引文框只放 page.md 明载原句（如 1919 Lowell 演讲的 "that most superb instrument..."、1917 拒爵理由句、1932 官方获奖理由句）；禁编造小说台词。

### 第 6 步：幻灯片序列 【人物专属，14 页】

```
00  OpenLiterature 项目首页
01  封面 — 福尔赛世家的叙事者 / John Galsworthy 1867–1933 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）
03  核心概览 — 福尔赛编年史 / 社会问题剧 / 社会运动 / PEN
04  金斯敦与哈罗 (1867–1886) — 律师之子的爱德华式教养
05  牛津与律师席 (1886–1893) — New College、Lincoln's Inn、南洋之旅
06  1893：甲板上的 Conrad — 终身友谊起点
07  Ada：从秘密恋情到缪斯 (1895–1905) — Wingstone 岁月、John Sinjon 笔名
08  1906 奇迹之年 — 《有产业的人》+《银匣》双线突破
09  社会问题剧十年 — Strife / Justice / The Eldest Son / The Mob
10  审查改革与运动清单 — Barrie/Murray 委员会、人道屠宰、监狱改革
11  三部福尔赛三部曲 — Saga / A Modern Comedy / End of the Chapter 图式
12  PEN 国际首任主席 (1921–1933) — 拒爵与受勋的荣誉观
13  1932 诺奖与谢幕 — 官方理由引文框、骨灰撒南唐斯
14  声誉沉浮：从"爱德华时代人"到 1967 BBC — 遗产与结尾
```

### 第 7–8 步：Beamer 与布局检查 【模板通用】

- 头部宏复用同侧成品骨架；每页 make+目检；表格页注意 arraystretch 压缩。

### 第 9 步：史实 + 术语审查 【人物专属】

**Galsworthy 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖序列 | 1932 是"1901 年设奖以来第二位英格兰作家"（首位 1907 Kipling；其间 Yeats/Shaw/Lewis 为非英格兰英语作家）——勿写成"英国第二人"含糊口径 |
| 获奖理由 | 官方原句锚定 The Forsyte Saga，勿扩写 |
| 笔名 | John Sinjon（父在世时用），勿拼成 Sinjohn 之外的变体后又混用 |
| Ada 婚史 | Ada 首婚对象是堂兄 Arthur Galsworthy（1891 婚、1905-02 离婚判决、13 天后与 John 完婚）——年份链条勿错 |
| 死因 | 脑血栓+动脉硬化（可能兼脑瘤）——勿单写"病逝"或脑瘤定论 |
| 拒爵与受勋 | 1917 拒骑士、1929 受 OM——两者对照写，勿颠倒顺序 |
| 现代主义攻击 | Woolf/Lawrence 的攻击按 page.md 客观引述，不加褒贬评价 |
| 剧作复排 | 其剧"很少复排"、小说常再版——勿写成"剧作被遗忘"的绝对化 |
| 一战立场 | 反战又主保卫比利时的矛盾自陈——客观呈现，勿简化为反战作家 |
| Conrad 关系 | 1893 航程相识时 Conrad 尚未开始写作——勿写成"文坛初识" |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| The Forsyte Saga | 《福尔赛世家》 | 1922 三卷合卷本口径 |
| The Forsyte Chronicles | 福尔赛编年史 | 含三部曲+短篇的总称 |
| A Modern Comedy | 《现代喜剧》 | 第二三部曲 1929 合卷 |
| End of the Chapter | 《篇章末章》 | 第三三部曲 1935 合卷（含遗著） |
| The Man of Property | 《有产业的人》 | 1906，Saga 首卷 |
| social problem drama | 社会问题剧 | 与 Shaw 并列口径 |
| John Sinjon | 约翰·辛琼（笔名） | 拼写固定 |
| PEN International | 国际笔会 | 1921 创立，首任主席 |
| Order of Merit (OM) | 功绩勋章 | 1929 接受，非爵位 |
| Romanes Lecture | 罗曼斯讲座 | 1931 牛津 |
| annus mirabilis | 奇迹之年 | 1906，传记家 Marrot 用语 |
| South Downs | 南唐斯丘陵 | 骨灰撒布地 |

---

## 四、BGM 建议 ✅ 【人物专属】

- **选定曲目**: **Nostalgia** — Alex-Productions
- **匹配理由**: "怀旧" 完美匹配福尔赛编年史的回望结构——三代人的财产与体面在时间中褪色；也匹配本篇"声誉沉浮"的叙事弧（被现代主义贬抑、被 1967 电视复燃）。
- **备选**（未采用）: The Flow of Time（时间感亦合但弱于怀旧的具体性）；With Me（已被 turing 侧使用）。
- **本地路径**: 复制 Nostalgia 对应曲目 → `presentations/20th_century/John_Galsworthy/Nostalgia.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/John_Galsworthy/page.md` | 事实基准（已核对） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `literature/generate_20th_century_list.py` | CITATION_ZH 获奖理由中译（禁改） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
