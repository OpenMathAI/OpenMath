# Tim Berners-Lee（蒂姆·伯纳斯-李）立传提示词

> qid=Q80 · 1955-06-08 生（在世留白） · 英国计算机科学家 · 20/21 世纪 · 2016 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/2016/Tim Berners-Lee/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、家庭、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（HTML/HTTP/URL 三要素 / "hypertext + TCP + DNS = Web" 的示意表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Sir Timothy John Berners-Lee（昵称 TimBL / TBL；中文惯称：蒂姆·伯纳斯-李）
- **头衔**：Sir（爵士，2004）、OM（功绩勋章，2007）、FRS、FREng
- **生卒**：1955-06-08 生于 London, England（英国）→ **在世留白**（页面无卒日，勿编造）
- **国籍**：英国（English / British）
- **身份**：计算机科学家；World Wide Web、HTML、URL、HTTP 的发明者
- **家庭**：父 Conway Berners-Lee（1921–2019）、母 Mary Lee Woods（1924–2017）——**两位都是数学家与计算机科学家**，均参与 **Ferranti Mark 1**（首台商用计算机）工作，皆来自 Birmingham；三个弟妹（弟弟 Mike 为生态学教授）。婚姻三次：Jane Northcote（1976 结婚，离异）→ Nancy Carlson（美国程序员，1990 结婚，育二子，2011 离异）→ Rosemary Leith（2014 结婚于 St James's Palace；WWWF 共同创始董事）；共 2 个子女 + 3 个继子女——仅一笔带过。
- **教育轨迹**：
  - Sheen Mount Primary School → Emanuel School（1969–73）；童年痴迷 trainspotting（看火车），靠改装火车模型学电子
  - 1976 年牛津 **The Queen's College** 物理**一等学位**（first in physics）；求学期间用旧电视攒出一台计算机
- **师承**：无传统博士师承（本科毕业即业界，页面无载导师，禁写）
- **研究领域**：计算机科学、Web 科学、语义网、去中心化数据（Solid）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **WWW 的发明（1989–1990）**：1989-03-12 在 CERN 提出信息管理系统提案；1990 年 redistribu 版获经理 **Mike Sendall** 批注 "vague, but exciting"（"模糊，但令人兴奋"）放行——此评语是页面实载名场片，必写。
2. **首次 HTTP 客户端-服务器通信**：1990 年 11 月中旬经互联网实现；首个浏览器+编辑器 **WorldWideWeb**（NeXTSTEP）、首个 Web 服务器 **CERN httpd**（跑在一台 NeXT Computer 上）；**1990-12-20** 发布第一个网站；**1991-08-06** 在 Usenet 公开发出协作邀请。
3. **可引用的核心自述**（页面实载）："I just had to take the hypertext idea and connect it to the TCP and DNS ideas and—ta-da!—the World Wide Web." 与 "Creating the web was really an act of desperation..."（超文本、互联网、多字体文本对象都已现成，"我只是把它们组合起来"——抽象一步：把所有文档系统视为一个更大的假想文档系统）。
4. **ENQUIRE（1980）**：1980 年 6–12 月首次以独立承包人身份在 CERN，做了基于超文本的原型系统 ENQUIRE——WWW 的前身。
5. **Robert Cailliau**：CERN 同事，独立提出过类似超文本系统提案，后作为**伙伴**（partner）与 Berners-Lee 共同推动 Web 落地——按页面实载"伙伴"表述，勿写成"共同发明人"。
6. **W3C（1994）**：在 MIT 创立 World Wide Web Consortium，制定 Web 标准；**关键决策：免专利、免版税**（royalty-free）——Web 得以普世的技术治理选择，本篇核心品格点。
7. **MIT / Southampton / Oxford 三站**：MIT CSAIL 3Com founders chair（Decentralized Information Group、Solid 项目）；2004 年 Southampton 计算机科学教席（Semantic Web）；2016 年牛津计算机系 professorial research fellow + Christ Church fellow。
8. **开放数据与 Web 治理**：2009 与 Rosemary Leith 共创 **World Wide Web Foundation**；2010 与 Nigel Shadbolt 建 **data.gov.uk**；2012 共创 **Open Data Institute**（任 president）；2013 领导 **A4AI**（可负担互联网联盟）；2019 发布 **Contract for the Web**；net neutrality 立场（"connectivity with no strings attached"）。
9. **Solid 与 Inrupt（2016–2018）**：让用户真正拥有数据所有权的去中心化 Web 项目；2018-09-30 创办开源公司 Inrupt——"Web 发明者重造 Web"的第二幕。
10. **EME/DRM 争议（2017）**：作为 W3C director 批准 EME 规范，遭 EFF/FSF 反对——页面实载的争议，保留语境一笔带过，勿渲染。
11. **大众时刻**：2012 伦敦奥运开幕式以 NeXT 计算机现场"被致敬"，tweet "This is for everyone"（2025 年用作回忆录书名）；1999 年入选 **Time 100**（"The World Wide Web is Berners-Lee's alone. He designed it. He loosed it on the world..."——页面实载引语）；2021 年 Web 源码以 **NFT** 拍出 $5,434,500；2025 年出版回忆录 *This Is for Everyone*（ghostwriter Stephen Witt，Stephen Fry 录有声书）。
12. **荣誉**：2016 图灵奖（2017-04-04 授予）、2004 爵士（New Year Honours，"for services to the global development of the Internet"）、2007 Order of Merit（限 24 位在世成员）、FRS 2001、NAS 外籍院士 2009、首届 Queen Elizabeth Prize for Engineering 2013、ACM Software System Award 1995。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（Web 三要素 — 蓝） | `#2E5A9E` | HTML / HTTP / URL |
| 分类色 2（CERN 时刻 — 青绿） | `#1E8E8E` | 1989 提案 / ENQUIRE / NeXT 服务器 |
| 分类色 3（开放治理 — 琥珀） | `#D9A441` | W3C / royalty-free / 开放数据 |
| 分类色 4（Web 的未来 — 玫瑰） | `#C0395B` | Solid / Inrupt / Contract for the Web |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：稀疏节点-连线（超链接图），呼应「超文本把文档连成宇宙」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：宏大 / 互联（一张网改变世界）
- **选定曲目**：Alex-Productions **Falling Apart**（manifest 预分配，直接沿用），匹配"打破信息壁垒、重构知识秩序"的史诗叙事。
- **落地文件**：`turing/presentations/Tim_Berners-Lee/FallingApart.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「WWW 发明者 · 英国」+ Berners-Lee 1955– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 家庭 / 教育 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1955–至今 生平纵览
4. **计算机科学家之家**：Ferranti Mark 1 双亲、伦敦少年、牛津物理
5. **早期职业**（1976–1984）：Plessey → D. G. Nash → CERN 独立承包 → ENQUIRE（1980）→ Image Computer Systems → 回 CERN
6. **1989 年 3 月 12 日：一份提案**："vague, but exciting"、Cailliau 加入
7. **1990 年冬天：Web 诞生**：WorldWideWeb 浏览器/编辑器、CERN httpd、12-20 首个网站、1991-08-06 Usenet 邀请
8. **三要素解构**（公式框）：HTML（内容）/ HTTP（传输）/ URL（地址）+ "hypertext + TCP + DNS = Web"
9. **免版税的抉择：W3C**（1994）：标准治理、royalty-free
10. **学术三站**：MIT CSAIL / Southampton 语义网 / Oxford
11. **开放 Web 的守护者**：WWWF、data.gov.uk、ODI、A4AI、net neutrality、Contract for the Web
12. **重造 Web：Solid 与 Inrupt**（2016–2018）：数据所有权
13. **争议一笔带过页**：EME/DRM 2017（按页面实载，保留 EFF 反对语境）
14. **荣誉与大众时刻**：Time 100 1999、骑士 2004、OM 2007、QE Prize 2013、奥运 2012、NFT 2021、回忆录 2025
15. **结尾**：在世留白；"This is for everyone"

## 5. 史实陷阱与敏感点（终审必须检查）

- **获奖理由（整句引用，核心红线）**：`"for inventing the World Wide Web, the first web browser, and the fundamental protocols and algorithms allowing the Web to scale"`（2016 图灵奖，2017-04-04 授予）。
- **日期红线**：提案 **1989-03-12**（页面另注"确切日期 unknown"用于早期参考处——以 1989-03-12 为准）；首次 HTTP 通信 1990-11 中旬；首个网站 **1990-12-20**；Usenet 公开 **1991-08-06**。勿把 1991 当"发明 Web"之年。
- **"发明人"边界**：页面表述 Web 是 Berners-Lee 一人设计（Time 100 引语），但 **Cailliau 是 partner**（伙伴推动者），勿写成"共同发明"，也勿完全抹去 Cailliau。
- **学位**：牛津 **物理** first（1976），非计算机；无博士，无导师记载——禁写师承。
- **父母职业**：双亲均参与 **Ferranti Mark 1**；Manchester Mark 1 是另一机（只在荣誉学位段提及父母 1940s 曾参与 Manchester Mark 1）——注意页面两处分别是 Ferranti Mark 1（正文）与 Manchester Mark 1（honorary degrees 段），执行时写 Ferranti Mark 1 为准，Manchester Mark 1 若提须注明"1940s"语境。
- **可引语**（页面实载）：两条自述（ta-da 句 / desperation 句）、"vague, but exciting"（Sendall 评语）、Time 100 评语、net neutrality 两句、"Not in the sense of most people. I'm atheist and Unitarian Universalist."（宗教问句——若用须标注）。
- **婚姻/家庭**：三段婚姻按 infobox/正文一笔带过（1976 Jane Northcote / 1990 Nancy Carlson / 2014 Rosemary Leith）；2 子女 + 3 继子女；宗教经历一句即可，不展开。
- **EME/DRM 争议**：仅按页面实载（2017 支持 EME、EFF 上诉失败、2017-09 成正式推荐）一笔带过，**勿渲染立场**。
- **W3C 地位**：页面称 "founder and **emeritus** director"——现任身份写 emeritus，勿写"现任 director"。
- **NFT 金额**：$5,434,500（2021-06，Sotheby's）——数字勿改。
- **在世留白**：born 1955-06-08，写作 `1955–`。
- **"首位/第一"红线**："first web browser / first web server / first website" 可按获奖理由与页面写；"互联网发明者"**禁写**（他发明的是 Web 不是 Internet）。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 伯纳斯-李（或 蒂姆·伯纳斯-李） | 待写入 |
| name_en | Tim Berners-Lee | 待写入 |
| birth_date | 1955-06-08 | 待写入 |
| death_date | NULL（在世） | 待写入 |
| nationality | United Kingdom | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | computer science / World Wide Web / semantic web | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **合作者**：Robert Cailliau（CERN，Web 落地伙伴）、Nigel Shadbolt（data.gov.uk、ODI 共同创始）、Rosemary Leith（WWWF 共同创始，妻子）、Mark Fischetti（Weaving the Web 合著）
- **家庭**：Conway Berners-Lee（父）、Mary Lee Woods（母）——均为数学家/计算机科学家，参与 Ferranti Mark 1
- **关键放行者**：Mike Sendall（CERN 经理，"vague, but exciting"）
- **页面无载的关系**：勿补（无导师记载；与 Vint Cerf 等人关系页面无展开）

## 8. 奖项清单

- ACM Software System Award（1995）
- Fellow of the Royal Society, FRS（2001）
- Knight Bachelor（2004 New Year Honours，invested 2004-07-16，"for services to the global development of the Internet"）
- American Philosophical Society（2004）、National Academy of Engineering（2007）
- Order of Merit, OM（2007-06-13，限 24 位在世成员）
- NAS Foreign Associate（2009）
- Queen Elizabeth Prize for Engineering（2013，首届）
- ACM Turing Award（2016，2017-04-04 授予）
- Time 100 Most Important People of the 20th century（1999）
- 荣誉学位：Manchester、Harvard、Yale 等（勿罗列过全）

## 9. 机构清单

- 教育：Sheen Mount Primary、Emanuel School（1969–73）、University of Oxford（The Queen's College，物理 first 1976）
- 任职：Plessey（Poole，1976–78 前后）、D. G. Nash（1978）、CERN 独立承包（1980-06–12）、Image Computer Systems（1980–84）、CERN fellow（1984 起）、MIT CSAIL（3Com founders chair）、University of Southampton（2004 教席，Semantic Web）、University of Oxford 计算机系（2016 起 professorial research fellow，Christ Church fellow）
- 创办：W3C（1994，emeritus director）、World Wide Web Foundation（2009）、Open Data Institute（2012）、Inrupt（2018）

## 10. 终审清单

- [ ] 生卒 1955-06-08 / 在世留白，出生地 London
- [ ] 获奖理由整句引用无误（2016 图灵奖，2017-04-04 授予）
- [ ] 1989-03-12 提案 / 1990-12-20 首个网站 / 1991-08-06 公开 年份链准确
- [ ] "vague, but exciting"（Sendall）与 ta-da 句引语完整
- [ ] 牛津物理 first（1976），无博士无师承
- [ ] Cailliau "伙伴"表述准确，非共同发明人
- [ ] W3C 1994 + royalty-free 决策表述准确；现职 emeritus director
- [ ] 发明的是 Web 不是 Internet；"互联网发明者"禁写
- [ ] EME/DRM 争议一笔带过不渲染；婚姻家庭一笔带过
- [ ] 国籍用「英国」，封面底部状态栏 `英国 | CERN · MIT · W3C · Oxford | Turing 2016`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2016/Tim Berners-Lee/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-Tim_Berners-Lee_at_the_2025_Web_Summit_Cropped_.jpg`（2025 最新肖像，取最大可用版）；示意图可用 `500px-First_Web_Server.jpg`（NeXT 首台 Web 服务器）作内容页插图
- [ ] **国籍**：封面顶部徽章明示英国
- [ ] **引语核对**：全部引语须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次图灵奖得主（Hennessy / Patterson）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
