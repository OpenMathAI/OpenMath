# 和平奖得主立传提示词（OpenPeace · María Corina Machado）

> **本文件是 María Corina Machado（2025 诺贝尔和平奖得主）的 OpenPeace 人物专属立传提示词**。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库）。
- **模板来源**：OpenPeace 20 世纪批次沉淀的执行模板（对齐 Kenneth_G_Wilson_zh.md 骨架：身份信息页必做 + 事业领域结构化表达）。
- **本实例**：María Corina Machado Parisca（玛丽亚·科里娜·马查多，1967–在世），2025 诺贝尔和平奖得主。
- **设计哲学**：和平奖立传必须保留「身份信息页」（Identity / Bio 速览页）与「事业领域表」的结构化骨架；本篇为 21 世纪单人次得主（2025 委内瑞拉），叙事重心是「从选举监督到民主过渡斗争」的事业线。

---

## 二、背景信息 【人物专属】

- **目标人物**：María Corina Machado Parisca（1967-10-07 生于加拉加斯，在世）
- **气质关键词**：**选举透明的守护者、反对派的统一旗手、从藏匿到领奖台的远行者** —— 2025 诺贝尔和平奖获奖理由：
  > "for her tireless work promoting democratic rights for the people of Venezuela and for her struggle to achieve a just and peaceful transition from dictatorship to democracy"
  > （表彰她不知疲倦地促进委内瑞拉人民的民主权利，并为实现从专制到民主的公正和平过渡而斗争）
  > ★ 英文原句照抄诺贝尔官方，中译照抄 `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` 2025 行，禁改写。
- **设计母题**：**跨越（crossing）**。2025-12 她为出席奥斯陆颁奖典礼经秘密路线渡海离境（危险航行至库拉索），与她在国内政治中长期「在体制与流亡之间摆渡」的处境互为镜像；视觉可用海路航线、船与灯塔、旗帜与选票等元素。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/21th_century/María_Corina_Machado/page.md`（Wikipedia 全文 + frontmatter：Q439564 / 1967-10-07 / Venezuela / politician, human rights defender, industrial engineer）
- **肖像**：真实照片可用 —— infobox 主图为 Nobel Week 2025 奥斯陆照片（images.txt 第 8 条 `María_Corina_Machado_greeting_crowd_during_Nobel_Week_2025_01.jpg`）；备选 2023 记者会照（第 6 条）。下载后用 `file` 验证格式。
- **参考模板**：
  - OpenPeace 20 世纪成品：`peace/presentations/20th_century/` 下已完成 Beamer 的目录（如 Henry_Dunant）
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 每完成一步向我汇报，遇到歧义先征求意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），yaml 母本 = `MySQL/data/Frederick_Sanger.yaml`。

### 第 0 步：通读 page.md 并核对事实基准 【人物专属】

- 生卒：1967-10-07 生于加拉加斯（Republic of Venezuela），在世（death_date 留白）。
- 国籍：Venezuela（单一）。
- 家庭：四姐妹中的长女；母 Corina Parisca Pérez（心理学家）、父 Henrique Machado Zuloaga（钢铁业企业家）；保守天主教家庭。曾曾祖父 Eduardo Blanco（作家，1881 年著《Venezuela Heroica》）。离异，三个子女（女儿 Ana Corina Sosa 2025-12-10 代母领奖并致答词）。
- 教育：Andrés Bello Catholic University 工业工程学士；IESA（Instituto de Estudios Superiores de Administración）金融硕士（page.md 未载具体年份，禁编）。
- 早年职业：Valencia 汽车行业工作；1992 创立 Fundación Atenea（救助加拉加斯街头孤儿与问题少年）；曾任 Oportunitas Foundation 主席。
- 任职：2011-01-05 ~ 2014-03-21 全国大会议员（Miranda 州，全国最高得票当选）；Vente Venezuela 全国协调人（2012-05-24 起在任）。
- 关键荣誉：Yale World Fellows 2009；Cádiz Cortes Ibero-American Freedom Prize 2015（与 López、Ledezma）；Prize for Freedom（Liberal International）2019；BBC 100 Women 2018；Václav Havel Human Rights Prize 2024；Sakharov Prize 2024（与 Edmundo González 共享）；Time 100 2025；诺贝尔和平奖 2025。
- 核心事业清单：① Súmate 选举监督组织共同创立（2001）；② 2004 罢免公投请愿与后续叛国指控风波；③ 2010 当选全国大会议员（全国最高票）、2012 国会公开质询；④ 2014 抗议中的领导角色与 La Salida；⑤ 2023 反对派初选胜利与 15 年禁任；⑥ 2024 大选团结阵营实际领袖与藏匿；⑦ 2025 诺奖与秘密离境领奖。
- 关键时间线（18 节点）：
  1967-10-07 生于加拉加斯 → 1992 创立 Fundación Atenea → 2001 与 Alejandro Plaz 创立 Súmate → 2002 政变未遂期间 Carmona Decree 签名风波 → 2004 罢免公投请愿、NED 资金叛国指控 → 2005-05-31 白宫会晤布什 → 2006-02 审判搁置（后无限期延宕） → 2009 Yale World Fellows → 2010-02 辞 Súmate、04 赢得初选 → 2010-09-25 当选全国大会（全国最高得票） → 2012-01-13 国会质询查韦斯（八小时国情咨文中途） → 2012 反对派总统初选败于 Capriles → 2014-03-21 因出席 OAS 被逐出国会 → 2014 与 López 发起 La Salida → 2015 加的斯自由奖 → 2023-06-30 被禁任公职 15 年、10-26 赢得初选 → 2024-10-24 萨哈罗夫奖（与 González）、选举后藏匿 → 2025-01-09 Chacao 现身后遭逮捕未遂 → 2025-10-10 获 2025 诺贝尔和平奖 → 2025-12 秘密离境经库拉索、12-10 女儿代领奖 → 2026-01-15 白宫向特朗普赠出诺奖勋章。

### 第 4 步：事业领域梳理 + 入库 【与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pro-democracy activism | 民主运动 | 2025 诺奖核心：促进民主权利与和平过渡 | 核心页、诺奖页 |
| 1 | electoral transparency | 选举透明 | Súmate 共同创立，2004 罢免公投监督 | Súmate 页 |
| 2 | human rights | 人权 | 萨哈罗夫奖 2024 / 哈维尔人权奖 2024 | 荣誉页 |
| 3 | opposition politics | 反对派政治 | 2010-2014 议员、2023 团结候选人 | 议会页、初选页 |
| 4 | civil society organizing | 公民社会组织 | Atenea/Oportunitas 基金会与 Súmate | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致】

> 只收 page.md 明载的关系；对手方均不在库内，yaml 关系将自动建 stub（name_en 用下表形式）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Súmate | 本人→机构 | 2001 与 Alejandro Plaz 共同创立的选举监督组织 |
| colleague | Alejandro Plaz | 无向 | 2001 共同创立 Súmate；因 NED 资金同遭叛国指控 |
| colleague | Edmundo González | 无向 | 2024 萨哈罗夫奖共同得主，2024 大选团结候选人 |
| colleague | Leopoldo López | 无向 | 2014 共同发起 La Salida；2015 加的斯自由奖共同得主 |
| colleague | Antonio Ledezma | 无向 | 2015 加的斯议会伊比利亚美洲自由奖共同得主 |
| colleague | Juan Guaidó | 无向 | 反对派同僚；2019 危机期间马查多表态若其召集大选将参选 |
| rival | Henrique Capriles | 无向 | 2012 反对派总统初选对手，马查多提前认败并表态支持 |
| controversy | Diosdado Cabello | 无向 | 2014 被逐出国会后马查多公开指责时任议会议长 |
| controversy | Jorge Rodríguez | 无向 | 2014 年其公布指马查多等策划推翻政府的邮件后经 Kivu 分析认定伪造 |
| parent-child | Corina Parisca | 无向 | 母亲，心理学家 |
| parent-child | Henrique Machado Zuloaga | 无向 | 父亲，钢铁业企业家 |
| parent-child | Ana Corina Sosa | 无向 | 女儿，2025-12-10 代母领奖并致答词 |

- 慎之又慎的不入库清单：查韦斯/马杜罗/特朗普/内塔尼亚胡等当代政治人物一律不建关系（★红线）；Rubio/Scott 等提名支持者；Corina Yoris（被指定替补后未获登记）；Lilian Tintori（合影）；great-great-grandfather Eduardo Blanco（隔代过远）；不具名子女与前夫（page.md 未具名）。
- 入库：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/María_Corina_Machado.yaml`（撞字典唯一键等 2 秒重跑）。

### 第 5 步：设计配色方案 【人物专属色彩】

- **主色（manifest 预分配，勿改）**：深青绿 `#0B5351`（沉静坚毅）+ 诺奖香槟金 `#C9A227`。
- badgeA 民主运动 — 深蓝 `#1F4E79`；badgeB 选举透明 — 金 `#C9A227`；badgeC 人权抗争 — 砖红 `#7A1E28`；badgeD 公民社会 — 青碧 `#1E6B5A`。
- **背景母题**：柔和斜向航线光带 + 稀疏圆点，呼应「跨越」母题（海路航线与远行领奖）。

### 第 6 步：规划幻灯片序列 【人物专属，12–14 页可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 2025 诺贝尔和平奖 / María Corina Machado 1967– + badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/国籍/教育/任职/荣誉/核心领域）
03  核心事业概览 — Súmate / 议员 / 反对派领袖 / 诺奖
04  早年与家世（1967–1992）— 加拉加斯长女、Eduardo Blanco 家世、UCAB 与 IESA
05  工程师与基金会岁月（1992–2001）— Atenea 基金会、Oportunitas
06  Súmate：选举透明的守护者（2001–2006）— 公投请愿、叛国指控、2005 白宫会晤
07  全国大会岁月（2010–2014）— 全国最高得票、2012 质询、2014-03-21 被逐
08  2014 抗议与 La Salida — López 合照插图、屡遭攻击（2011/2013/2014 客观列举）
09  反对派领袖之路（2019–2023）— 初选胜利、15 年禁任与国际反应（客观）
10  2024 大选与藏匿 — González 顶替、WSJ 公开信、2025-01-09 逮捕未遂
11  荣誉与认可 — 哈维尔奖/萨哈罗夫奖/BBC 100 Women/Time 100/加的斯奖
12  2025 诺贝尔和平奖 — 获奖理由整句、诺奖委员会「统一人物」评语、秘密离境
13  颁奖典礼与勋章去向 — 女儿代领、背伤、2026-01-15 赠勋章与委员会表态（客观两说并陈）
14  结尾
```

### 第 6.5 步：各页事实要点速查 【人物专属，写页时对照】

| 页 | 必含事实（全部取自 page.md） |
|----|------|
| 01 封面 | 姓名、生年 1967、国籍 Venezuela、2025 Nobel Peace Prize、主色 #0B5351 + 香槟金 |
| 02 身份信息页 | 全名 María Corina Machado Parisca；1967-10-07 加拉加斯；UCAB 工业工程 + IESA 金融硕士；Vente Venezuela 全国协调人（2012-05-24 起在任）；2011-2014 全国大会议员（Miranda）；三大荣誉（哈维尔奖 2024 / 萨哈罗夫奖 2024 / 诺奖 2025） |
| 03 概览 | 四条事业线：Súmate（2001）→ 议员（2010-2014）→ 反对派团结领袖（2023-2024）→ 诺奖（2025） |
| 04 早年 | 四姐妹之长女；母心理学家/父钢铁企业家；曾曾祖父 Eduardo Blanco 1881《Venezuela Heroica》；曾叔祖 Armando Zuloaga Blanco 1929 起义被杀；保守天主教家庭 |
| 05 基金会岁月 | Valencia 汽车行业；1992 Fundación Atenea（街头儿童救助，私人捐赠）；Oportunitas Foundation 主席；后因 Súmate 角色离开 Atenea 以免其政治化 |
| 06 Súmate | 2001 酒店大堂与 Plaz 相遇创立；2004 罢免公投请愿；NED 资金 → Article 132 叛国+阴谋指控（HRW 称指控 dubious 且政治动机）；2005-05-31 椭圆办公室会晤布什；2006-02 审判搁置、后无限期延宕 |
| 07 议会岁月 | 2010-02 辞 Súmate；04 赢得初选；09-25 当选（全国最高得票，与 Enrique Mendoza 并列两位最高）；2012-01-13 八小时国情咨文中途质询查韦斯（短缺/治安/国有化）；家族企业 Sivensa/Sidetur 被征收（NYT 报道口径） |
| 08 抗议与 La Salida | 2014-03-18 国会要求刑事调查；03-21 应巴拿马请求以 alternate envoy 出席 OAS 后被逐；2014-04-01 游行遭国民警卫队催泪瓦斯；屡遭攻击：2011-07-05 独立日石块袭击、2011-10-16 Turmero、2013-04-30 议会斗殴鼻骨骨折、2014-07-30 colectivos 袭车（全部客观列举不加定性） |
| 09 反对派之路 | 2019-02-01 表态若 Guaidó 召集大选将参选；2022-08-14 确认参加初选；2023-03-15 Mérida 起步全国行；2023-06-30 应 José Brito 请求被总审计长禁任 15 年（UN/OAS/EU 多方谴责、欧洲议会称 arbitrary and politically fabricated —— 仅转述）；2023-10-26 赢初选；2024-01 最高法院确认禁任 |
| 10 大选与藏匿 | Corina Yoris 被指定替补未获登记 → Edmundo González 顶替；2024-07-04 共同启动竞选（数万人游行）；2024-08-01 WSJ 公开信自称藏匿；2025-01-09 Chacao 现身后车辆遭暴力拦截；2026-01-03 马杜罗被美军扣押后呼吁 González 就任（客观一句） |
| 11 荣誉页 | Yale World Fellows 2009；加的斯奖 2015（与 López/Ledezma）；BBC 100 Women 2018；Prize for Freedom 2019；哈维尔人权奖 2024（欧洲委员会，三强入围）；萨哈罗夫奖 2024-10-24（与 González）；Time 100 2025 |
| 12 诺奖页 | 2025-10-10 获奖；获奖理由 EN 整句 + 名录中译；Inspira América 基金会 2024-08-16 发起提名、2025-08-26 Rubio 等公开支持；诺奖委员会评语 "a key, unifying figure..."；2025-12 秘密离境（陆路转移+海上 12 小时延误+失联漂流数小时+库拉索转机，WSJ 版本客观转述） |
| 13 典礼与勋章 | 12-10 未能及时到场，女儿 Ana Corina Sosa 代领并致答词；其后抵达首次公开露面；旅途背椎骨折；2026-01-15 白宫赠勋章；委员会表态头衔不可转移；可比附 1943 Hamsun 先例（page.md 明载，客观一句） |
| 14 结尾 | 收束于获奖理由中译句 + 「跨越」母题视觉元素回扣；品牌标注 OpenMathAI |

### 第 7–8 步：版式要点 + 本篇专属陷阱表

- 版式：对齐 OpenPeace 既有成品（身份信息页 `\profileslide` 模式；荣誉页 itemize 压行距 arraystretch 0.6–0.7；topsep/partopsep 归零；顶部负间距 −0.35 ~ −0.55cm 压多条目）。
- 每写完一页 `make` 并 `pdftoppm` 截图目检溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。
- 陷阱表（Review 锚点）：

| 陷阱 | 说明 |
|------|------|
| ★政治敏感红线 | 2025 委内瑞拉国内局势、2026 美国军事干预、美委/以委关系、特朗普与马杜罗等当代政治内容全部按 page.md 客观事实记录，全篇零评价性语句、零立场表述 |
| 获奖理由措辞 | 官方原句强调 "promoting democratic rights ... just and peaceful transition from dictatorship to democracy"，勿简化为「反独裁斗士」之类自创语 |
| 勋章赠特朗普 | 仅客观记录：2026-01-15 赠出勋章；挪威诺奖委员会明载「奖一经颁发不可撤销/共享/转让，头衔不随实物转移」，特朗普不列入得主名单；与 1943 Hamsun 赠 Goebbels 并列仅为 page.md 明载史实 |
| 争议两说并陈 | 2025-12 颁奖典礼后的抗议示威与她对「委内瑞拉已被渗透」的回应，均为 page.md 明载，两说并陈不作裁断 |
| 数据库同名区分 | 库内 `Antonio Machado`（诗人，#5680）与本人无关，勿混；对手方建 stub 一律用第 4.5 步表的精确 name_en |
| 教育年份 | UCAB/IESA 均未载具体年份，禁编 |
| 引语红线 | 仅可引 page.md 明载英文原句（如 Súmate 创立回忆 "It was a choice of ballots over bullets."、诺奖委员会评语 "a key, unifying figure in a political opposition that was once deeply divided"）；禁自编中译「原话」，中译仅作转述并标注 |
| 肖像 | Nobel Week 2025 照为主肖像；2002 与布什合影可作 Súmate 页插图；La Salida 2014 合照可作第 08 页插图；均注明图注 |

### 第 9 步：术语审查清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Súmate | 苏马特（选举监督组织） | 不译「总和」；共同创立勿写成独自创立 |
| Vente Venezuela | 委内瑞拉前进党 | National Coordinator ≠ 总统候选人 |
| National Assembly | 全国大会（议会） | 2014 被逐为议会决议，措辞客观 |
| recall referendum | 罢免公投 | 2004，结果为反对罢免 |
| Carmona Decree | 卡莫纳法令 | 签名风波须含其本人解释 |
| disqualification | 禁任公职 | 15 年，2023-06-30 起；勿写「辞职」 |
| Unitary Platform | 团结平台 | 反对派联盟，2023 初选主办方 |
| La Salida | 「出路」倡议 | 2014 与 López 共同发起 |
| Sakharov Prize | 萨哈罗夫奖 | 2024 与 González 共享，非诺奖 |
| Nobel Week | 诺奖周 | 2025-12 奥斯陆 |
| colectivos | 协会武装团体（colectivos） | 攻击事件叙述仅客观列举，不加定性词 |
| Freedom Manifesto | 《自由宣言》 | 2025-11-18 WaPo 预发布评述、2026-02 出版（scheduled 口径） |

### 第 10 步：执行清单（做完勾掉）

1. [ ] 复制 Makefile 并设置 `MAIN=María_Corina_Machado_zh`、`VIDEO_NAME=María_Corina_Machado_zh`（文件名含重音字符，编译前先确认 latexmk/xelatex 对 UTF-8 文件名兼容，必要时 ASCII 别名 `Maria_Corina_Machado`）
2. [ ] 下载主肖像（Nobel Week 2025 照，250px 改 600px）+ 两张插图（2002 白宫照、2014 La Salida 合照），`file` 验证格式
3. [ ] 复制 BGM `Ascension.wav` 到本目录
4. [ ] 写 tex：配色宏（#0B5351 主色 + badgeA–D）+ 第 6 步 14 帧 + 身份信息页
5. [ ] 编译循环：0 error、vbox ≤ 10pt、hbox ≤ 50pt
6. [ ] pdftoppm 逐页目检（页数对照第 6 步规划）
7. [ ] make images/video 产出 mp4
8. [ ] Review-1 修正写回本提示词
9. [ ] DB 复核：has_social_data=1、fields=5、relations=12、QID Q439564

---

## 四、背景音乐选择 ✅ 【manifest 预分配，勿改】

- **选定曲目**：**Ascension** — Cold Cinema（Cinematic Dramatic Epic Orchestra Sci-Fi Trailer）
- **匹配理由**：「Ascension（攀升/跨越）」精确对应本篇母题——从藏匿到领奖台的远行与事业的阶梯式攀升；史诗管弦张力匹配秘密离境的惊险叙事。
- **本地路径**：`music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/María_Corina_Machado/page.md` | 本地 Wikipedia 正文（事实唯一基准） |
| `peace/presentations/pages/21th_century/María_Corina_Machado/images.txt` | 肖像与插图 URL |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 幂等入库引擎 |
| `peace/PROMPTS_WORKFLOW_21ST.md` / `peace/PROMPTS_WORKFLOW.md` | 工作流与红线 |

> **开始执行。每完成一步汇报。最重要的事：事实只取 page.md，评价一律不写。**
