# 文学家立传提示词（V. S. Naipaul / V. S. 奈保尔）

> **OpenLiterature** 诺贝尔文学奖得主「人物专属立传提示词」，结构对齐 OpenPhysicist 标杆 Kenneth_G_Wilson_zh.md。
> 适配要点：文学家无公式框——用**名句引文框 / 意象图式 / 代表作书影**替代；核心页为「文学领域表」。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Vidiadhar Surajprasad Naipaul（V. S. 奈保尔），特立尼达裔英国小说家/旅行作家/随笔作家，2001 年诺贝尔文学奖得主（21 世纪文学奖首位得主）。
- **设计哲学**：保留「身份信息页 + 研究领域结构化」骨架，叙事重心放在**"被压抑的历史"的发掘者与后殖民世界的审视者**上——以殖民地的"无历史"与抵达之谜支撑叙事张力。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Vidiadhar Surajprasad Naipaul（1932-08-17 ~ 2018-08-11，享年 85 岁）
- **诺奖年份**：2001 年诺贝尔文学奖，官方获奖理由（EN 原文，禁止改写）：
  > "for having united perceptive narrative and incorruptible scrutiny in works that compel us to see the presence of suppressed histories"
  > （中译：表彰其将敏锐的叙事与不屈的审视融于著作之中，促使我们看到被压抑的历史之存在）
- **气质关键词**：**被压抑历史的发掘者、后殖民世界的旁观审判者、以英文写作的印度裔特立尼达人**
- **设计母题**：**抵达之谜（the enigma of arrival）**——以"旅程线：查瓜纳斯 → 西班牙港 → 牛津 → 伦敦 → 世界"的渐远渐深意象图式，呼应其"书写者永远在离开与抵达之间"的核心主题。
- **本地数据源**：`literature/presentations/pages/21st_century/V._S._Naipaul/page.md`（+ metadata.json、images.txt）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/V._S._Naipaul
- **肖像**：第 0 步待下载（2016 年照片，见 infobox）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1932-08-17 生于特立尼达查瓜纳斯（Chaguanas，甘蔗种植园镇）~ 2018-08-11 逝于伦敦家中，享年 85 岁；临终与床边人诵读丁尼生诗《Crossing the Bar》，葬于 Kensal Green Cemetery（page.md 明载，客观陈述）。
- 国籍：特立尼达和多巴哥 → 英国（Trinidadian-British；yaml 按 page.md 口径分两条）。
- 家庭：父 Seepersad Naipaul（《Trinidad Guardian》英文记者，《毕斯沃斯先生的房子》主人公原型，1953-10 卒）；母 Droapatie（娘家 Capildeo 家族）；婆罗门印度移民家庭，祖父辈自英属印度以契约劳工身份来特立尼达。弟 Shiva Naipaul（小说家/记者，1985 年卒，年 40）；妹 Savi Naipaul Akal。
- 婚姻：Patricia Ann Hale（1955 结婚，1952 牛津学院戏剧上相识，1996 病逝，终身"关键支柱与第一读者"，无子女）；Margaret Murray Gooding（1972 阿根廷之行起婚外情 24 年，非婚姻不入 spouse，提示词可按 page.md 客观简述、不展开细节）；Nadira Alvi（1996 结婚，巴基斯坦记者，较其年轻 20 余岁；2003 收养其女 Maleeha）。
- 教育：Queen's Royal College（西班牙港，1942–1950，17 岁前获特立尼达政府奖学金）→ University College, Oxford（1950–1953，英文系，"damn, bloody ... second"二等学位；1954 B.Litt. 口试被 F. P. Wilson 判不及格——同一 F. P. Wilson 在 Tolkien 眼中其古英语论文为全校最佳，诺奖评审语境的对照可写）。
- 关键荣誉：诺贝尔文学奖 2001；Booker Prize 1971（《In a Free State》）；Jerusalem Prize 1983；Somerset Maugham Award 1961（《Miguel Street》，Maugham 本人首肯首位非欧洲得主）；John Llewellyn Rhys Prize 1958（《The Mystic Masseur》）；Trinity Cross 1990（特立尼达最高国家荣誉）；Knight Bachelor 1990。
- 核心作品与贡献（4–6 条）：
  1. 《The Mystic Masseur》（1957）/《Miguel Street》（1959）——特立尼达喜剧早期小说；
  2. 《A House for Mr Biswas》（1961）——以父亲一生为蓝本的突破之作，Patrick French 评"如狄更斯或托尔斯泰般普遍"；
  3. 《The Middle Passage》（1962）/《An Area of Darkness》（1964）——旅行写作与"祖先之地"审视的开端；
  4. 《In a Free State》（1971，Booker Prize）/《Guerrillas》（1975）/《A Bend in the River》（1979）——"更广大世界中的疏离"小说；
  5. 《The Enigma of Arrival》（1987）——五部分自传性小说，写作生涯中期转折；
  6. 《Beyond Belief》（1998）/《The Masque of Africa》（2010）——晚期非虚构（其中关于伊斯兰的论点引发争议，按 page.md 客观简述，见陷阱表）。
- 关键时间线（15–20 节点）：
  1. 1932 生于查瓜纳斯甘蔗镇，婆罗门契约劳工家庭第二代；
  2. 1939/1941 随家迁西班牙港；1942 入 Queen's Royal College；
  3. 1949/1950 获特立尼达政府奖学金，选择赴牛津读英文——"in order at last to write"；
  4. 1950-08 乘机经纽约转船抵伦敦，笔记成为 37 年后《抵达之谜》"Journey"章的底稿；
  5. 1952 牛津遇 Patricia Ann Hale；抑郁与"nervous breakdown"（他 30 年后称"something like a mental illness"）；
  6. 1953 父 Seepersad 卒（ unable 返乡，8 岁的 Shiva 代行长子火葬礼）；1953 与 Pat 同时毕业（二等学位）；
  7. 1954 B.Litt. 被 F. P. Wilson 判败，学术路断；
  8. 1954-12 加入 BBC《Caribbean Voices》（制作人 Henry Swanzy），Langham Hotel 自由撰稿人房间；
  9. 1955-01 与 Pat 秘密结婚（仅两名法定证人）；同年夏在自由撰稿人房间打出《Miguel Street》首篇；
  10. 1955 秋写成《The Mystic Masseur》，André Deutsch 接受出版（稿费 £125）；
  11. 1957 《The Mystic Masseur》出版；唯一全职：C&CA 编辑助理（10 周）；经 Francis Wyndham 引识 Anthony Powell，获《New Statesman》月度书评（至 1961）；
  12. 1958 《The Mystic Masseur》获 John Llewellyn Rhys Prize；1958-07 与 BBC 决裂；
  13. 1961 《A House for Mr Biswas》出版、《Miguel Street》获 Somerset Maugham Award；
  14. 1960–61 受 Eric Williams 总理之邀访加勒比，1962 成《The Middle Passage》；
  15. 1962–63 携 Pat 首访印度（祖先之地），1964 成《An Area of Darkness》；
  16. 1966 乌干达 Makerere University 驻校作家，快速完成《The Mimic Men》（1967）；在坎帕拉遇青年 Paul Theroux，同行坦桑尼亚；
  17. 1969 《The Loss of El Dorado》（Pat 协助 British Library 档案研究两年）；1971 《In a Free State》获 Booker Prize；
  18. 1972 布宜诺斯艾利斯之行（遇 Margaret Murray；遇 Borges 并在 NYRB 撰批评文）；1973 获 Artur Lundkvist 提名诺贝尔奖；
  19. 1979 《A Bend in the River》；1987 《The Enigma of Arrival》；1990 Trinity Cross + 爵士；1996 Pat 病逝后两个月内娶 Nadira Alvi；
  20. 2001 获诺贝尔文学奖；2018-08-11 卒于伦敦。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | postcolonial literature | 后殖民文学 | 殖民/去殖民社会的"被压抑历史"书写（诺奖理由核心） | 核心页 |
| 1 | travel writing | 旅行写作 | 《The Middle Passage》《An Area of Darkness》以降的审视式非虚构 | 旅行页 |
| 2 | novel | 小说 | 喜剧早期特立尼达小说 → 疏离小说（《A Bend in the River》） | 小说页 |
| 3 | narrative non-fiction | 叙事性非虚构 | 《The Loss of El Dorado》档案叙事史、《Beyond Belief》 | 非虚构页 |
| 4 | essay | 随笔 | 《The Writer and the World》等文集；NYRB 撰稿 | 随笔页 |

#### 4.1 入库操作

- 新建/复用 `people` 记录（name_en 用 page.md frontmatter `Vidiadhar Surajprasad Naipaul`，qid=Q44593；先 SELECT 查库内是否已有该 QID stub，**复用勿新建**），`primary_occupation='writer'`、`has_social_data=1`、`has_biography: false`
- occupations：writer(0)、novelist(1)、journalist(2)
- 5 个领域写入 `person_field`（postcolonial literature 等缺失字典项先补建）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属】

> 只收 page.md 明载关系。Margaret Murray Gooding 为婚外情非婚姻，不入 spouse；Shiva Naipaul 为兄弟（无 sibling 类型），仅提示词呈现；Artur Lundkvist 仅提名事件，不入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Patricia Ann Hale | 无向 | 第一任（1955–1996），牛津相识，其事业的关键支柱 |
| spouse | Nadira Alvi | 无向 | 第二任（1996 起），巴基斯坦记者 |
| parent-child | Seepersad Naipaul | 对方→本人 | 父，《Trinidad Guardian》记者，《毕斯沃斯先生的房子》主人公原型 |
| influence | Joseph Conrad | 对方→本人 | 瑞典学院颁奖词称其为"Conrad's heir as the annalist"（委员会明载的谱系） |
| colleague | Henry Swanzy | 无向 | BBC《Caribbean Voices》制作人，1954 给其首份有薪工作 |
| colleague | Derek Walcott | 无向 | 《Caribbean Voices》同圈青年作家；曾评其为"最成熟的西印度作家之一" |
| colleague | Diana Athill | 无向 | André Deutsch 出版社编辑，审读并支持《Miguel Street》 |
| colleague | Anthony Powell | 无向 | 经 Francis Wyndham 引识；为其引荐《New Statesman》书评职 |
| colleague | Antonia Fraser | 无向 | 1960 年代引其进入英国上流文人圈 |
| colleague | Paul Theroux | 无向 | 坎帕拉相识的青年美国作家，同行非洲旅行 |
| colleague | Robert B. Silvers | 无向 | 《New York Review of Books》主编，长期约稿（阿根廷/美国报道） |
| controversy | Edward Said | 无向 | 萨义德批评其为"西方起诉的证人"、贩卖"殖民神话"（page.md 明载的批评谱系） |

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#8B1A1A`（京都红——甘蔗田的凝重与审视者的锋利）
- **辅助**：诺奖香槟金 `#C9A227`
- badge 四分类：badgePostcolonial 靛蓝 `#4C5FD5`；badgeTravel 青绿 `#0E7C7B`；badgeNovel 琥珀 `#E07B30`；badgeNonfiction 玫瑰 `#C4204F`
- **背景母题**：渐远旅程线（一条从热带海岛伸向伦敦的细线 + 错落圆点，呼应"抵达之谜"）

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 抵达之谜 / V. S. Naipaul 1932–2018 + badge + 右上头像 + 国籍行（Trinidad and Tobago → UK）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/两任妻子/父亲原型/荣誉/核心领域）
03  核心创作概览 — 后殖民文学 / 旅行写作 / 疏离小说 / 叙事非虚构
04  早年：查瓜纳斯与女王皇家学院 (1932–1950)【意象图式：契约劳工航线】
05  牛津与伦敦低谷 (1950–1954)【引文框："in order at last to write"】
06  BBC 自由撰稿人房间 (1954–1958)【书影：Miguel Street】
07  《毕斯沃斯先生的房子》(1961)【书影+引文框：Streatham Hill "my Eden"】
08  旅行写作三部曲：加勒比与祖先之地 (1962–1964)【书影：An Area of Darkness】
09  疏离小说与布克奖 (1967–1979)【书影：In a Free State / A Bend in the River】
10  抵达之谜与"被压抑的历史" (1987–2001)【引文框：官方获奖理由 EN+中译】
11  争议与晚年 (1972–2018)——萨义德批评与私人生活按 page.md 客观简述各一句，不展开
12  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式宏名统一；旅程图式可用 tikz 简单曲线+节点，勿复杂化；身份页 `\profileslide`。
- 陷阱表：

| 陷阱 | 说明 |
|------|------|
| 姓名规范 | 全名 Vidiadhar Surajprasad Naipaul；frontmatter 即此形式，yaml name_en 用库内既有形式（先查 Q44593） |
| 国籍 | Trinidadian-British：yaml 分列 Trinidad and Tobago + United Kingdom，勿只写英国 |
| 父亲角色 | Seepersad 是记者、《毕斯沃斯》原型；1953 死时 Naipaul 未能返特多，幼弟 Shiva 代行火葬礼（可写，人物对照） |
| 学位 | 牛津英文系二等学位 + B.Litt. 被判败（1954）；"hated Oxford"为自述转述，可注明 |
| 诺奖理由 | 官方句重"perceptive narrative and incorruptible scrutiny"/"suppressed histories"；委员会另有 "Conrad's heir"、"transforms rage into precision" 转述，两类引语勿混 |
| 争议红线 | Said 的批评、Robert Harris "racist" 评语、性别虐待指控：只按 page.md 客观一句带过，**不作评价、不展开、不引骂评细节**；伊斯兰主题（《Beyond Belief》）争议同此处理 |
| 私生活 | Margaret Murray 婚外情与虐待自述仅按 page.md 中性简述或整体回避；Nadira Alvi 婚期 1996（Pat 病逝后两个月内），勿写错 |
| 奖项年份 | John Llewellyn Rhys 1958 / Somerset Maugham 1961 / Booker 1971 / Jerusalem 1983 / Trinity Cross+爵士 1990 / Nobel 2001，勿错位 |
| 无载禁写 | 不编造"文学师承"（其写作无导师制师承）；Tolkien 只可写"判其古英语论文全校最佳"这一明载事件，勿写成师承 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| postcolonial literature | 后殖民文学 | 与"后殖民批评理论"（Said 系）勿混 |
| A House for Mr Biswas | 毕斯沃斯先生的房子 | 1961；主人公以父为原型 |
| The Enigma of Arrival | 抵达之谜 | 1987，五部分 |
| In a Free State | 自由国度 | 1971，Booker Prize |
| A Bend in the River | 河湾 | 1979 |
| An Area of Darkness | 幽暗国度 | 1964，印度三部曲之一 |
| Caribbean Voices | 加勒比之声 | BBC 广播节目，Langham Hotel 房间 |
| indentured labour | 契约劳工 | 祖辈自英属印度来特多的身份 |
| suppressed histories | 被压抑的历史 | 官方获奖理由关键词，勿改写 |
| Trinity Cross | 三一十字勋章 | 1990，特多最高国家荣誉 |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions
- **匹配理由**："新大陆"意象匹配其一生跨越特立尼达 → 牛津 → 伦敦 → 加勒比 → 印度 → 非洲的地理与心理迁徙；曲目的开拓/求索感匹配"被压抑历史的发掘者"气质。
- **本地路径**：`music_audio/alex-productions/` 下 New Lands 对应 wav → `presentations/21st_century/V._S._Naipaul/New_Lands.wav`（对照 `curated_tracks.md` 取实际文件名）。

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/V._S._Naipaul/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/21st_century/V._S._Naipaul/images.txt` | 肖像/插图 URL 清单 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `literature/presentations/21st_century/OpenLiterature_21st_Century_Nobel_Laureates.md` | 总名录（官方理由中译） |
| `literature/generate_21st_century_list.py` | `CITATION_ZH`（获奖理由取用，禁止改写该脚本） |
| `MySQL/data/V._S._Naipaul.yaml` | 社会关系入库 yaml（与第 4.5 步一致） |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库（New Lands 实际文件名） |

## 六、执行清单 【模板通用，逐项打勾】

1. ☐ 第 0 步：核对 page.md 事实基准 + 下载肖像（infobox 2016 年照片，curl -A "Mozilla/5.0" + file 验证；404 则按 Wikipedia REST API / Special:FilePath 回退，仍失败用装饰圆占位）
2. ☐ 第 1 步：建目录 `V._S._Naipaul/images/`
3. ☐ 第 2 步：复制 Makefile，设 `MAIN=V._S._Naipaul_zh`、`VIDEO_NAME=V._S._Naipaul_zh`
4. ☐ 第 3 步：复制 New Lands wav（对照 curated_tracks.md 文件名）
5. ☐ 第 4 步：yaml 入库（fields≥4、relations≥2）
6. ☐ 第 5 步：按配色写 tex 头部宏（mainclr=#8B1A1A）
7. ☐ 第 6 步：逐页写 slide → 逐页 make → pdftoppm 截图检查
8. ☐ 第 7 步：0 error、vbox≤10pt、hbox≤50pt 达标
9. ☐ 第 8 步：逐页目检（人物/年份/书名拼写；引语归属复核）
10. ☐ 第 9 步：make images + make video（mp4）→ 汇报

> **开始执行。每完成一步汇报。最重要的事：逐页 make，看到溢出就修。**
