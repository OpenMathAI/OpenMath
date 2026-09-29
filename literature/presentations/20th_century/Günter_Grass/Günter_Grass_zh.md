# 文学家立传提示词（实例：Günter Grass）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Günter Grass（1999 诺贝尔文学奖，《铁皮鼓》作者）为对象。
> 结构对齐物理学家侧标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（OpenMathAI 共享仓库 literature/ 侧）。
- **本实例**：Günter Wilhelm Grass（君特·格拉斯），德国小说家、诗人、剧作家、版画家、雕塑家。
- **设计哲学**：文学家立传无公式框——用**代表作书影 / 名句引文框 / 意象图式**替代；必须有「身份信息页」，并以**文学领域表**做结构化表达。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Günter Grass（1927-10-16 ~ 2015-04-13，享年 87 岁）
- **气质关键词**：**但泽三部曲的缔造者、魔幻现实主义巨匠、"Vergangenheitsbewältigung"（直面过去）的良心**
- **官方获奖理由**（1999，EN 原文照 `nobel_literature_citations.json`，禁止改写）：
  > "whose frolicsome black fables portray the forgotten face of history"
  > 中译（照 `generate_20th_century_list.py` CITATION_ZH）：「表彰其嬉戏般的黑色寓言，描绘了历史被遗忘的面貌」
- **设计母题**：**铁皮鼓与洋葱**——《铁皮鼓》的鼓面节奏（魔幻现实的敲击）+ 《剥洋葱》的层层记忆（回忆录三部曲的叙事隐喻），配但泽克拉托尔 Crane 门与吕贝克烟斗剪影。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Günter_Grass/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`
  - Wikipedia URL：https://en.wikipedia.org/wiki/G%C3%BCnter_Grass
- **肖像**：第 0 步待下载——infobox 用图 `Günter_Grass_(1986)_by_Erling_Mandelmann.jpg`（Erling Mandelmann 摄， Commons 直链在 images.txt 第 4 条）；备选 `Günter_Grass_auf_dem_Blauen_Sofa.jpg`（2006）。250px 改 500px 下载，curl 加 `-A "Mozilla/5.0"`。
- **参考成品**：`literature/presentations/20th_century/` 下已完成的 16 页立传（封面 `\input` 共享 OpenLiterature 首页模板）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已核对，以此为准）

- **生卒**：1927-10-16 生于但泽自由市 Danzig-Langfuhr（今波兰格但斯克 Wrzeszcz）～ 2015-04-13 卒于吕贝克医院（肺部感染），享年 87 岁；2015-04-29 私人家庭仪式葬于 Behlendorf（1995 年起定居）。
- **国籍/认同**：生于但泽自由市（Free City of Danzig），战后入德国籍；自我认同卡舒比人（Kashubian）。
- **家庭**：父 Wilhelm Grass（1899–1979，德裔路德宗新教徒）与母 Helene（娘家姓 Knoff，1898–1954，卡舒比-波兰裔天主教徒）经营带住房的杂货店；妹 Waltraud（1930 生）。
- **教育**：但泽 Conradinum 文理中学；战后石匠训练（1946–47 矿上做工）；杜塞尔多夫艺术学院（雕塑与版画）；1953 迁西柏林，柏林艺术大学。
- **服役经历（客观简述，禁评价）**：1943 年 16 岁任 Luftwaffenhelfer；随后 Reichsarbeitsdienst；1944-11 17 岁生日后自愿报名潜艇部队（Kriegsmarine）被拒，被征入 Waffen-SS 第 10 装甲师 Frundsberg（受训坦克炮手），1945-02 至 1945-04-20 负伤，在 Marienbad 被美军俘虏，关押 Bad Aibling 战俘营，1946-04 获释。**此事 2006 年才公开**（见第 11 页与陷阱表）。
- **婚姻**：1954 娶瑞士舞者 Anna Margareta Schwarz（1978 离异，四子女 Franz 1957 / Raoul 1957 / Laura 1961 / Bruno 1965）；1972 分居后与 Veronika Schröter 生女 Helene（1974）、与 Ingrid Kruger 生女 Nele（1979）；1979 娶风琴师 Ute Grunert（相伴终老，两名继子 Malte/Hans）；孙辈 18 人。
- **文学师承与影响**：page.md 明载受其影响者 Salman Rushdie（明言欠《铁皮鼓》的债）；同社关系 Hans Werner Richter（四七社组织者）。
- **关键荣誉**：Nobel 1999；Georg Büchner Prize 1965；Prince of Asturias Award（文学）1999；Hermann Kesten Prize 1995；Honorary Fellow RSL 1993；Hidalgo Prize 1992（捍卫罗姆人）；European of the Year 2012；格但斯克荣誉市民；吕贝克设 Günter Grass 之家（展馆藏档）。
- **核心作品与贡献**（4–6 条）：
  1. 《铁皮鼓》*The Tin Drum*（1959）——欧洲魔幻现实主义关键文本，但泽三部曲首部；诺奖委员会称其出版"如同德语文学在数十年语言与道德毁灭后获得新生"。
  2. 但泽三部曲：《铁皮鼓》+《猫与鼠》*Cat and Mouse*（1961）+《狗年月》*Dog Years*（1963），写纳粹兴起与战争中的但泽。
  3. 《比目鱼》*The Flounder*（1977）——渔夫与妻子童话改写，两性之争。
  4. 《我的世纪》*My Century*（1999）——按年编排的 20 世纪马赛克叙事。
  5. 回忆录三部曲：《剥洋葱》*Peeling the Onion*（2006）/《盒式相机》*The Box*（2008）/《格林的词语》*Grimms Wörter*（2010）。
  6. 《蟹行》*Crabwalk*（2002）——难民船沉没，晚年代表作。
- **关键时间线**（16 节点）：1927 但泽出生 → 1943 Luftwaffenhelfer → 1944-11 征入 Waffen-SS → 1945-04 负伤被俘 → 1946-04 战俘营获释 → 1946–47 矿工与石匠学徒 → 杜塞尔多夫学雕塑版画、四七社 → 1953 迁西柏林 → 1959《铁皮鼓》→ 1961《猫与鼠》/公开反对柏林墙 → 1963《狗年月》→ 1965 Büchner 奖 → 1977《比目鱼》→ 1979 电影《铁皮鼓》金棕榈+奥斯卡外语片 / 与 Ute 再婚 → 1983–86 柏林艺术学院院长 → 1980s 和平运动、加尔各答六月、*Zunge zeigen* → 1990 反对两德仓促统一 → 1999 诺奖+阿斯图里亚斯奖、《我的世纪》→ 2001 提议德波流失艺术博物馆 → 2002《蟹行》→ 2006《剥洋葱》+ Waffen-SS 披露风波 → 2007《纽约客》自述 → 2008/2010 回忆录二、三卷 → 2012 诗《不得不说》与《欧洲的耻辱》→ 2015-04-13 逝世，遗作 *Vonne Endlichkait*（2015-08 出版）。

### 第 4 步：文学领域表（与 yaml fields 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | magic realism | 魔幻现实主义 | 《铁皮鼓》为欧洲关键文本 | 核心页 |
| 1 | postwar German literature | 战后德语文学 | Vergangenheitsbewältigung 运动 | 三部曲页 |
| 2 | drama | 戏剧 | 剧作家面向 | 贡献页 |
| 3 | graphic arts | 版画与雕塑 | 艺术家双重身份、 drawing 配文 | 学徒页 |
| 4 | political essay | 政论随笔 | 演讲文集贯穿一生 | 同行者页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致，仅收 page.md 明载）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Hans Werner Richter | 无向 | 四七社（Group 47）组织者，Grass 为共同创立者 |
| colleague | Willy Brandt | 无向 | 勃兰特总理任期内积极支持者，1972 同框 |
| colleague | Volker Schlöndorff | 无向 | 《铁皮鼓》1979 电影改编导演，追思会出席者 |
| colleague | John Irving | 无向 | 盛赞者兼辩护者，2015 追思会致主悼词 |
| influence | Salman Rushdie | 无向 | Rushdie 明言受《铁皮鼓》影响 |
| spouse | Anna Margareta Schwarz | 无向 | 1954 结婚 1978 离异，瑞士舞者，育四子女 |
| spouse | Ute Grunert | 无向 | 1979 再婚相伴终老，风琴师 |
| parent-child | Wilhelm Grass | 父→子 | 德裔路德宗新教徒，杂货店主 |
| parent-child | Helene Grass | 母→子 | 娘家姓 Knoff，卡舒比-波兰裔天主教徒 |
| parent-child | Franz | 子 | 1957 生 |
| parent-child | Raoul | 子 | 1957 生 |
| parent-child | Laura | 女 | 1961 生 |
| parent-child | Bruno | 子 | 1965 生 |
| parent-child | Helene | 女 | 1974 生，母 Veronika Schröter |
| parent-child | Nele | 女 | 1979 生，母 Ingrid Kruger |
| controversy | Rolf Hochhuth | 无向 | 2006 披露后斥其 hypocrisy |
| controversy | Joachim Fest | 无向 | 2006 批评其忏悔"来得太迟" |

### 第 5 步：配色方案 【人物专属】

- **主色**：深松绿 `#1B4D3E`（分批文件预分配）
- **辅色**：诺奖香槟金 `#C9A227`
- **badge 四分类**：badgeA 魔幻现实主义 — 鼓面红 `#8C2F1B`；badgeB 但泽三部曲 — 波罗的海蓝 `#175873`；badgeC 版画雕塑 — 铅灰 `#4E4A45`；badgeD 政论随笔 — 麦金 `#A8742A`
- **背景母题**：柔和气泡 + 稀疏鼓点圆环（呼应铁皮鼓节奏）；洋葱层弧线用于回忆录页

### 第 6 步：幻灯片序列（14 页，含共享封面）

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 但泽三部曲的缔造者 / Günter Grass 1927–2015 + 四 badge + 右上头像 + 国籍行（但泽自由市 → 德国）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/出生地/家庭/教育/服役/任职/荣誉/核心领域）
03  核心贡献概览 — 铁皮鼓 / 但泽三部曲 / 比目鱼 / 回忆录三部曲
04  但泽童年 (1927–1944) — 杂货店、卡舒比血统、双亲双信仰
05  战争与战俘 (1944–1946) — 征召、负伤、Bad Aibling（客观简述）
06  艺术学徒 (1946–1956) — 石匠、杜塞尔多夫、四七社、西柏林
07  铁皮鼓与但泽三部曲 (1959–1963)（核心贡献页：书影 + 诺奖委员会评语引文框）
08  比目鱼与我的世纪 — 童话改写、编年马赛克
09  政治同行者 — 勃兰特、蜗牛日记、和平运动、统一之争
10  回忆录三部曲 — 剥洋葱/The Box/Grimms Wörter，记忆的层
11  2006 披露风波 — Hochhuth/Fest 批评 vs Irving/Wałęsa 辩护（双声客观呈现）
12  荣誉与认可 — Nobel 1999 · Büchner 1965 · Asturias 1999 · Grass 之家
13  遗产与结尾 — Crabwalk、Vonne Endlichkait、"frolicsome black fables"
14  结尾
```

### 第 7–8 步：版式要点 + Grass 专属陷阱表

- 版式照 literature 侧既成 16 页骨架；引文框替代公式框；书影图配图注。

| 陷阱 | 说明 |
|------|------|
| Waffen-SS 口径 | 只按 page.md 客观事实：1944-11 报名海军被拒后被征入第 10 装甲师 Frundsberg、1945-02–04 服役至负伤、2006-08 FAZ 访谈首次公开、Spiegel 2006-08-15 刊三份 1946 美军文件；**不作道德评价、不展开政治叙事** |
| 引语白名单 | 仅 page.md 载英文原文者可入引文框：Grass 忏悔语（"It was a weight on me..."）、Nobel committee 两句（"frolicsome black fables..." 与 "a new beginning after decades..."）、Irving "simply the most original and versatile writer alive"、Fest/Wałęsa/Updike 语；中文不造"原话" |
| 《狗年月》年份 | infobox 作 1963、正文一处作 1965——以 1963（三部曲序列）为准，可加注 |
| 布莱梅奖 | 因《铁皮鼓》"immorality" 被布不来梅市撤销——可写，属接受史 |
| 关系边界 | Veronika Schröter / Ingrid Kruger 为子女之母但 page.md 未载婚姻关系，不入 spouse；妹 Waltraud 无 sibling 类型不入库；孙辈 18 人不入库 |
| 双奖同片 | 1979 电影《铁皮鼓》同年获金棕榈+奥斯卡最佳外语片，两奖并列勿漏 |
| 卒因 | 肺部感染（lung infection），吕贝克医院；葬 Behlendorf 非吕贝克市内 |
| 国籍徽章 | 写「但泽自由市 → 德国」，勿只写 Germany；卡舒比认同可注 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| The Tin Drum | 铁皮鼓 | Die Blechtrommel |
| Danzig Trilogy | 但泽三部曲 | 三部 1959/1961/1963 |
| magic realism | 魔幻现实主义 | 非"魔幻现实主義"繁简混排 |
| Vergangenheitsbewältigung | 直面过去 | 德语原词可保留，加释义 |
| Free City of Danzig | 但泽自由市 | 今格但斯克 Gdańsk |
| Kashubian | 卡舒比人 | 族群认同，非"波兰裔"泛称 |
| Group 47 | 四七社 | Hans Werner Richter 组织 |
| Waffen-SS | 武装党卫军 | 仅客观服役事实 |
| Peeling the Onion | 剥洋葱 | 回忆录三部曲卷一 |
| Crabwalk | 蟹行 | Im Krebsgang |
| unreliable narrator | 不可靠叙事者 | 风格术语 |
| Georg Büchner Prize | 格奥尔格·毕希纳奖 | 1965 |

---

## 四、BGM 建议 ✅

- **选定曲目**：**With Me** — Alex-Productions（52k views，标签：高受众/温和/稳定）
- **匹配理由**：
  - "温和/稳定" 匹配 Grass 长达近六十年的多面创作生涯（小说/诗/戏剧/版画/雕塑），叙事是长线纪录而非单点爆点
  - "与我同行"（With Me）呼应其"蜗牛的步伐"（*Aus dem Tagebuch einer Schnecke*）的民主改革同行者意象与 1972 与勃兰特同框的政治陪伴
  - "高受众" 匹配其德语世界国民作家地位
- **本地路径**：`music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` → 复制为 `presentations/20th_century/Günter_Grass/With-Me.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Günter_Grass/page.md` | 事实基准（唯一数据源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构母本 |
| `MySQL/data/Günter_Grass.yaml` | 入库 yaml（与本文件 §4/§4.5 一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `literature/generate_20th_century_list.py` | 获奖理由中译来源（禁止修改） |

## 六、执行清单（逐项打勾）

1. [ ] 下载肖像 `Günter_Grass_(1986)_by_Erling_Mandelmann.jpg`（curl -A "Mozilla/5.0"，250px→500px，`file` 验证为 JPEG；404 则换 `Günter_Grass_auf_dem_Blauen_Sofa.jpg`；再 404 用装饰圆占位）
2. [ ] 建目录 `literature/presentations/20th_century/Günter_Grass/`（含 `images/`）
3. [ ] 复制既成立传 Makefile，改 `MAIN=Günter_Grass_zh`、`VIDEO_NAME=Günter_Grass_zh`
4. [ ] 复制 BGM：`music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` → `With-Me.wav`
5. [ ] 写 tex（配色 §5 / badge 四色 / 幻灯片序列 §6 共 15 帧含共享封面）
6. [ ] 编译循环：0 error；vbox ≤10pt；hbox ≤50pt；`latexmk -c` 清理（勿用 rm -f）
7. [ ] 取日志后重新 `make pdf`（单遍 xelatex 会破坏 remember picture）
8. [ ] `pdftoppm` 逐页目检（含身份信息页与第 11 页争议页双声平衡）
9. [ ] `make images && make video` 出 mp4
10. [ ] Review-1 修正写回本提示词 §8 陷阱表

## 七、版式补遗（literature 侧沉淀经验）

- **身份信息页**：左 40% 头像（draw=coveraccent!50 细边框）+ 右信息网格 `\infob` 行式（生卒/出生地/家庭/教育/任职/荣誉/核心领域），行高用 `\baselineskip` 微调不硬压。
- **引文框**：替代公式框——`beamercolorbox` + 左侧 2.5pt 主色竖线，字号 `\small`，引文后括注来源（如 Nobel committee / FAZ 2006）；中引文不造原话，只转述 page.md 英文原文。
- **表格页预算**：4 行表 + 引文框顶满时 `arraystretch 0.60~0.62` + 顶部 `-0.45cm`；`tabularx` X 列内禁 `\\`，须用 `\newline`。
- **时间线**：`\foreach` 分隔符必须 ASCII 逗号（中文逗号会吞条目）；年份节点 15–20 个，跨页可拆两栏。
- **宏名**：`\newcommand` 名禁数字（如 `\grass1959slide` 会截断成垃圾页），用 `\grassdrumslide` 语义命名。
- **书影/插图**：但泽 Krantor 明信片（images.txt 第 3 条）可作第 7 页背景插图，图注写清 "Danzig Krantor waterfront (postcard, c. 1900)"； POW 档案照（images.txt 第 7 条）仅用于第 5/11 页客观史料位。
- **结尾品牌**：底部品牌统一 `OpenLiterature`（共享仓库口径为 OpenMathAI），引号半角 `" "`。

> **开始执行。每完成一步汇报。最重要的事：事实只出自 page.md，无载禁写。**
