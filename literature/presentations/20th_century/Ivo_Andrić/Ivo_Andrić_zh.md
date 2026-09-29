# 文学家立传提示词（Ivo Andrić）

> **OpenLiterature 人物专属立传提示词**：Ivo Andrić（伊沃·安德里奇，1961 诺贝尔文学奖，南斯拉夫）。
> 执行 agent 按第三部分第 0–9 步逐步执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist/OpenMath 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Ivo Andrić（伊沃·安德里奇），前南斯拉夫唯一诺贝尔文学奖得主。
- **设计哲学**：文学家立传无公式框，以**代表作书影、名句引文框、意象图式**替代物理公式表达；必须有「身份信息页」（Identity / Bio 速览页），务必保留。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Ivo Andrić（1892-10-09 ~ 1975-03-13，享年 82 岁；出生日期 metadata 有 10-09/10-10 两值，以正文 10-09 为准）
- **官方获奖理由（Nobel 官方 EN 原文 + 名录中译，禁止改写）**：
  > "for the epic force with which he has traced themes and depicted human destinies drawn from the history of his country"
  > 「表彰其史诗般的力量，从其国家的历史中提炼主题并描绘人类命运」（1961-10-26 授予）
- **气质关键词**：**大桥的记录者、波斯尼亚的史诗家、乱世中的外交官作家**。
- **设计母题**：**桥（the Bridge）**。德里纳河上的穆罕默德·帕夏·索科洛维奇桥横跨东西方，既是其 magnum opus 的主角，也是南斯拉夫「东西方之间桥梁」的历史隐喻——视觉语言用桥拱、河面倒影与多民族文化纹样。
- **本地数据源**：`literature/presentations/pages/20th_century/Ivo_Andrić/page.md`（+ metadata.json / images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Ivo_Andrić
- **肖像**：第 0 步待下载（images.txt 有 1961 获悉获奖照、书房照等真实照片可用）。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；封面 `\input` 项目共享首页。

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md，直接使用）

- 生卒：1892-10-09 生于特拉夫尼克附近 Dolac（奥匈帝国托管波斯尼亚）~ 1975-03-13 凌晨 1:15 逝于贝尔格莱德军事医学院，享年 82 岁；骨灰 1975-04-24 安放于贝尔格莱德新公墓名人巷，送葬约 1 万人。
- 本名 Ivan Andrić，Ivo 为昵称形式；波斯尼亚克罗地亚天主教家庭出身，后自我认同为塞尔维亚人；塞尔维亚-克罗地亚语（早年 Ijekavian 方言，贝尔格莱德时期改用 Ekavian）。
- 家庭：独子；父 Antun 银匠 32 岁死于肺结核（安德里奇时年 2 岁），由姨父 Ivan Matković（维舍格勒警察）与姨母 Ana 抚养长大；母 Katarina 赴萨拉热窝做工。
- 教育：萨拉热窝大中学（1902 入学，拉丁/希腊/德语见长、数学吃力曾留级）→ 萨格勒布大学（1912，数理系因奖学金）→ 维也纳大学（1913）→ 雅盖隆大学克拉科夫（1914 第 4 学期）→ 一战后获萨格勒布南斯拉夫史与文学本科（1919）→ **格拉茨大学博士 1924-07-13**，论文《土耳其统治影响下波斯尼亚精神生活的发展》（德文）。
- 早年 activism：南斯拉夫青年组织成员（SHNO 首任主席 1911、Young Bosnia 重要成员）；1914 年斐迪南大公遇刺后（刺客 Princip 为其密友）被奥匈当局逮捕，1915-03-20 获释流放 Ovčarevo，1917-07-02 大赦。
- 外交官生涯：南斯拉夫王国外交部 1920–1923、1924–1941（梵蒂冈、布加勒斯特、的里雅斯特、格拉茨、马赛、巴黎、马德里、布鲁塞尔、日内瓦国联代表团、贝尔格莱德总部；1937 任首相 Stojadinović 外交助理；**1939 任驻德国大使**，1941-04 德军入侵后卸任）。
- 二战：拒领养老金、拒与傀儡政权合作、拒签《告塞尔维亚民族书》、拒迁往克罗地亚独立国，隐居贝尔格莱德友人公寓（传记家喻为软禁），完成两部最重要的小说。
- 关键荣誉：Legion of Honour Grand Officer（1937）；Nobel Literature（1961，胜出 Tolkien/Frost/Steinbeck/Forster）；Order of the Republic（1962）；AVNOJ Award（1967）；Order of the Hero of Socialist Labour（1972）；塞尔维亚皇家科学院正式院士（1926-02），克罗地亚/波黑/斯洛文尼亚科学院成员或通讯院士；贝尔格莱德、萨拉热窝、克拉科夫三校荣誉博士。（Order of the German Eagle 1939 为纳粹德国所授，属客观史实，幻灯片不展开。）
- 核心作品（4–6 条）：《德里纳河上的桥》*Na Drini ćuprija*（1945，magnum opus，16 世纪建桥至一战桥头编年史）；《特拉夫尼克纪事》*Travnička hronika*（1945，拿破仑战争时期法国领事在波斯尼亚）；《小姐》*Gospođica*（1945，萨拉热窝女性一生）；中篇《地狱》*Prokleta avlija*（1954，伊斯坦布尔奥斯曼监狱）；散文诗集 *Ex ponto*（1918，处女作）与 *Nemiri*（1920）；短篇《阿里·杰尔泽莱兹之旅》（1920，首篇短篇）。
- 关键时间线（15–20 节点）：1892 生 Dolac → 1894 丧父寄养维舍格勒 → 1902 萨拉热窝大中学 → 1911 首两首诗刊于 *Bosanska vila*、任 SHNO 主席 → 1912 萨格勒布入学 → 1913 维也纳 → 1914 克拉科夫、7 月被捕 → 1915-03 释出流放 Ovčarevo → 1917-07 大赦 → 1918 *Ex ponto* → 1919 萨格勒布毕业入宗教部 → 1920 转外交部（梵蒂冈）、*Nemiri* → 1923 格拉茨任副领事 → 1924 博士、首部短篇集 → 1926 马赛/巴黎、入科学院 → 1928 马德里（撰玻利瓦尔/戈雅随笔，始写《地狱》）→ 1930 日内瓦国联 → 1937 首相外交助理、荣誉军团军官级 → 1939 驻德大使 → 1941-04 卸任归国隐居写作 → 1945 三部小说同年出版 → 1946 南斯拉夫作家协会主席 → 1953 入南共盟 → 1954 *Prokleta avlija* → 1958 婚 Milica Babić、首获诺奖提名 → 1961-10-26 诺奖（奖金约 3000 万第纳尔全数捐作波黑购书基金）→ 1968 妻逝 → 1974-12 入院 → 1975-03-13 逝于贝尔格莱德 → 1975 遗嘱设 Andrić Prize → 1976 Ivo Andrić 基金会成立。

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | epic novel | 史诗小说 | 诺奖理由核心：从民族历史提炼人类命运 | 核心贡献页 |
| 1 | historical fiction | 历史小说 | 奥斯曼/奥匈治下波斯尼亚三百年 | 核心贡献页 |
| 2 | short story | 短篇小说 | 1924 起多部短篇集，遗嘱设年度短篇奖 | 短篇页 |
| 3 | prose poetry | 散文诗 | *Ex ponto*/*Nemiri* 早年代表 | 早年页 |
| 4 | essay | 随笔 | 论卡拉季奇、涅戈什、科契奇等 | 晚年页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Milica Babić | 无向 | 塞尔维亚国家剧院服装设计师，1958-09-27 结婚（安德里奇 66 岁），1968-03-16 妻先逝 |
| influence | Franz Kafka | 对方→本人 | page.md 明载卡夫卡对其散文有显著影响 |
| influence | Søren Kierkegaard | 对方→本人 | 克尔凯郭尔著作强塑其哲学观 |
| influence | Vuk Karadžić | 对方→本人 | 推崇并撰文论及的塞尔维亚语文学奠基人 |
| influence | Petar II Petrović-Njegoš | 对方→本人 | 推崇并撰文论及的黑山诗人主教 |
| influence | Petar Kočić | 对方→本人 | 推崇并撰文论及的波斯尼亚塞尔维亚作家 |
| colleague | Gavrilo Princip | 无向 | 萨拉热窝青年时代密友（Young Bosnia/SHNO），客观史实简述 |
| colleague | Tugomir Alaupović | 无向 | 中学文学老师、终生挚友与仕途提携者（诗人/部长） |
| influence | Branko Ćopić | 本人→对方 | page.md 明载受其作品影响的作家 |
| influence | Vladan Desnica | 本人→对方 | page.md 明载受其作品影响的作家 |
| influence | Mihailo Lalić | 本人→对方 | page.md 明载受其作品影响的作家 |
| influence | Meša Selimović | 本人→对方 | page.md 明载受其作品影响的作家 |

入库：`MySQL/seed_person.py data/Ivo_Andrić.yaml`（幂等，QID 匹配）。

### 第 5 步：配色方案

- 主色：深绿 `#1B4D3E`（德里纳河谷与桥体的沉稳）；辅助：诺奖香槟金 `C9A227`。
- badgeA 史诗小说 — 墨绿 `#2E5E4E`；badgeB 历史小说 — 赭石 `#8A5A2B`；badgeC 短篇 — 靛蓝 `#2C4A6E`；badgeD 散文诗 — 暗玫瑰 `#8A3B4A`。
- 背景母题：桥拱弧线与河面倒影波纹（低饱和细线，勿喧宾夺主）。

### 5.1 格式硬要求 【★ 必须满足】

1. 封面右上角肖像 + 细边框 + 姓名小字注；顶部/底部明示国籍（Yugoslavia）。
2. **身份信息页**：封面之后、核心贡献之前，左头像右信息网格（生卒/本名/国籍变迁/教育/外交官经历/主要荣誉/核心领域）。
3. 结尾页品牌统一 `OpenMathAI`；引号用半角 `" "`。
4. 名句引文框替代公式框：*The Bridge on the Drina* 桥头编年史意象句或 1940 日记句（page.md 有英文原文方可引用，中文语境用忠实转述）。

### 第 6 步：幻灯片序列（14 页）

```
00 OpenLiterature 项目首页（共享封面 \input）
01 封面 — 大桥的记录者 / Ivo Andrić 1892–1975 + 四色 badge + 右上头像 + 国籍行
02 身份信息页（★ 必做）
03 核心贡献概览 — 史诗小说 / 历史小说 / 短篇 / 散文诗
04 早年：维舍格勒的河边童年（1892–1911）— 丧父寄养、德里纳河与大桥、萨拉热窝大中学
05 青年：诗人与囚徒（1911–1918）— SHNO、Young Bosnia、1914 被捕与流放、*Ex ponto*
06 外交官岁月（1920–1941）— 梵蒂冈到柏林、格拉茨博士 1924、驻德大使
07 二战隐居（1941–1945）— 拒合作、公寓里的写作、1945 三部曲同年问世
08 《德里纳河上的桥》专页 — 桥的编年史、东西方之间的南斯拉夫隐喻（引文框）
09 特拉夫尼克纪事与小姐 — 拿破仑时代的领事、萨拉热窝女性
10 短篇与中篇 — Alija Đerzelez、地狱、维齐尔的大象
11 战后与晚年 — 作协主席、诺奖 1961、奖金捐书、Milica
12 荣誉与认可 — Nobel 1961 · 三国科学院 · 荣誉博士
13 遗产：安德里奇格、基金会、前南唯一的诺奖作家
14 结尾
```

### 第 7–8 步：Beamer 源码与布局检查

- 每页 `\newcommand{\xxxslide}` 定义；骨架复用 Kenneth_G_Wilson_zh.tex（配色宏/`\plainbar`/`\deckbackground` 等）。
- 每写完一页 `latexmk -c` 清理后 `make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查

**Andrić 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 出生日期 | 1892-10-09（正文），metadata 有 10-10 噪声值，勿混用 |
| 生育/族裔 | 生于波斯尼亚克罗地亚天主教家庭、自我认同塞尔维亚人；诺奖委员会口径 Yugoslav；勿写成单一「塞尔维亚作家」或「克罗地亚作家」 |
| 博士 | 格拉茨大学 1924-07-13，德文论文论奥斯曼统治下的波斯尼亚；勿写维也纳/萨格勒布博士 |
| 获奖胜出者 | 1961 委员会在 Tolkien/Frost/Steinbeck/Forster 之间选择了安德里奇（档案 50 年后解密），可作客观事实 |
| 奖金去向 | 约 3000 万第纳尔全数捐出指定购买波黑图书馆用书，勿写成「捐给基金会」 |
| 妻子 | Milica Babić 是国家剧院服装设计师、小近 20 岁，1958 结婚 1968 先逝；勿与早年「作家不宜婚」引语混淆时间线 |
| 政治红线 | 二战立场、战后与南共关系、波斯尼亚批评者的指控（反穆斯林偏见/剽窃等）与克罗地亚 1990s 黑名单：只按 page.md 客观简述，不作政治评价、不展开政治叙事；Princip 只写「青年密友」事实 |
| 纳粹奖章 | Order of the German Eagle（1939）客观存在于 award_received，幻灯片荣誉页不陈列、不解释 |
| 方言 | 早年 Ijekavian、贝尔格莱德时期改 Ekavian，勿写成「波斯尼亚语」 |
| 无载禁写 | 与 Thomas Mann 等仅列「阅读过的作家」，无思想影响明载不入库；不给任何「弟子」编造师承 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| The Bridge on the Drina | 《德里纳河上的桥》 | *Na Drini ćuprija* 原名；勿译「德里纳河大桥」 |
| Višegrad | 维舍格勒 | 成长地与桥之所在 |
| Travnička hronika | 《特拉夫尼克纪事》 | 亦译《波斯尼亚纪事》 |
| Prokleta avlija | 《地狱》 | 中篇，伊斯坦布尔监狱 |
| Ex ponto | 《出海之上》 | 散文诗集处女作，拉丁语题名 |
| Serbo-Croatian | 塞尔维亚-克罗地亚语 | 诺奖委员会语言口径 |
| Young Bosnia | 年轻波斯尼亚 | 青年组织，客观史实简述 |
| Kingdom of Yugoslavia | 南斯拉夫王国 | 外交官任职国 |
| House arrest | 软禁 | 传记家比喻用语，非官方罪名 |
| epic force | 史诗般的力量 | 诺奖理由核心词 |

---

## 四、背景音乐建议

- **选定曲目**：**Cinematic Experience**（分批文件预分配）。
- **匹配理由**：电影感/史诗气质匹配「桥的编年史」跨四个世纪的时间纵深；弦乐铺陈贴合外交官-囚徒-隐士三重人生的命运感；与 1961 诺奖理由「epic force」同构。
- **备选**（未采用）：New Lands（宏大但缺历史纵深）、Timeless（沉稳但电影感不足）。
- **本地路径**：按 `music_audio/curated_tracks.md` 索引拷贝至 `presentations/20th_century/Ivo_Andrić/Cinematic Experience.wav`。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Ivo_Andrić/page.md` | 事实基准（唯一来源） |
| `literature/presentations/20th_century/OpenLiterature_20th_Century_Nobel_Laureates.md` | 名录与中译理由 |
| `MySQL/data/Ivo_Andrić.yaml` | 入库 yaml（本提示词第 4/4.5 步落地） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
