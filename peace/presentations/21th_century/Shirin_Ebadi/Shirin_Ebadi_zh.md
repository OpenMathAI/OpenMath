# OpenPeace 立传提示词（2003 · Shirin Ebadi 希琳·伊巴迪）

> 本文件是 OpenPeace 21 世纪批次的人物专属立传提示词（Beamer 执行用）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> ★ 21 世纪红线（伊朗相关）：**国内局势与各方表态一律只作 page.md 明载的客观事实记录，不加任何评价性语句**。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库）。
- **本实例**：Shirin Ebadi（希琳·伊巴迪），伊朗律师、前法官，2003 年诺贝尔和平奖得主——首位伊朗得主、首位穆斯林女性得主。
- **设计哲学**：伊巴迪的叙事轴是「法庭」——从首位女法官到被免职、从笔下案件到世界讲台；立传以「法官→书记员→律师→诺奖得主→流亡者」五幕展开。

## 二、背景信息 【人物专属】

- **目标人物**：Shirin Ebadi（شيرين عبادى；1947-06-21 生于伊朗哈马丹，在世，现居伦敦——2009 年起流亡）
- **气质关键词**：**法庭上的抗争者、儿童与妇女的辩护人、被没收奖章的得主** —— 2003 年诺贝尔和平奖获奖理由：
  > "for her efforts for democracy and human rights, focusing especially on the rights of women and children."
  **中译**：表彰她为民主与人权所做的努力，尤其聚焦于妇女与儿童的权利
- **设计母题**：**法槌与天平（gavel & scales）**——法官席的天平 + 律师卷宗，象征「用法律本身为权利辩护」。
- **本地数据源**：`peace/presentations/pages/21th_century/Shirin_Ebadi/page.md`

## 三、任务流程

### 第 0 步：事实基准（已核对，直接采用）

- 生年：1947-06-21 生于哈马丹，婴儿期随家迁德黑兰；父 Mohammad Ali Ebadi（哈马丹首席公证人、商法教授）；母 Minu Yamini（★ 父母仅叙述，不建关系行）
- 教育：Anoshiravn Dadgar 与 Reza Shah Kabir 学校 → 1965 入德黑兰大学法律系 → 1969-03 通过资格考试、实习六个月后正式任法官 → 续读德黑兰大学法学博士（1971 年授课教授之一为 Mahmoud Shehabi Khorassani）
- 法官生涯：伊朗最早的女法官之一；1975 成为德黑兰城市法院首位女性院长，任至 1979 革命；革命后女性不再任法官，被免职降为原法院书记员
- 律师生涯断档：虽有执业许可但申请屡被拒，1993 年才恢复执业；此间著书并为期刊撰稿
- 执业里程碑：代理连环谋杀案（Chain murders）遇害知识分子 Dariush Forouhar 与 Parvaneh Eskandari 夫妇家属；代理 1999 学生抗议遇难者 Ezzat Ebrahim-Nejad 家属；2000 「录像带案」被判五年监禁+吊照，最高法院后撤销；代理儿童受虐案（Arian Golshani、Leila）推动伊朗儿童监护法议题；协助起草 2002 年议会通过的禁止虐待儿童法
- 组织：1994 创立儿童权利保护协会（SPRC）；2001 创立人权捍卫者中心（DHRC）
- 荣誉：Rafto Prize 2001；Nobel Peace Prize 2003；Legion of Honour 2006；JPM Interfaith Award 2004；《福布斯》全球百位最具权力女性（2004）
- 诺奖细节：2003-10-10 公布；委员会称其为「从未理会自身安全威胁的勇敢者」；她是首位伊朗得主、首位穆斯林女性得主；获奖后自巴黎返抵德黑兰，数千人在 Mehrabad 机场迎接；颁奖演讲明确反对强行更迭政权、批评伊朗压制并主张伊斯兰与民主人权相容、亦批评美国外交政策（客观并列）；时任总统 Khatami 称该奖「政治性」（客观转述一句）
- 2009 流亡：总统选举后身在西班牙，未再返伊朗；2009-11 诺贝尔奖章与证书在德黑兰银行保险箱被革命法庭取走（挪方 Støre 首相表态「震惊」、伊朗否认）——「首次有诺贝尔和平奖被国家当局没收」（挪方声明口径）
- 晚近：2006 与五位女性诺奖得主共同创立诺贝尔女性倡议（Nobel Women's Initiative）；2004 起诉美国财政部出版限制并胜诉；2008 后为巴哈伊七人组辩护；2019 呼吁终止对妇女暴力条约；2026 被 Time 列入百位最具影响力人物（★ 2026 叙事仅一句存在性事实，细节不展开）
- 在世：death_date 省略，页面全部「享年」类表述禁用

### 第 4 步：研究领域/事业领域表（与 yaml 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | human rights | 人权 | 异见者与政治案件辩护 | 律师页 |
| 1 | women's rights | 妇女权利 | 获奖理由焦点；离婚权立法草案 | 诺奖页 |
| 2 | children's rights | 儿童权利 | SPRC、反虐待儿童法 | 事业页 |
| 3 | refugee rights | 难民权利 | 《Refugee Rights in Iran》2008 | 著述页 |
| 4 | rule of law | 法治 | 法官/律师视角的制度抗争 | 法庭页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致；★ 仅收 page.md 明载）

| 类型 | 对方 | 方向 | note |
|------|------|------|------|
| founder | Society for Protecting the Rights of the Child | 无向 | 1994 创立（SPRC） |
| founder | Defenders of Human Rights Center | 无向 | 2001 创立（DHRC），2008-12 办公室被查封 |
| advisor-student | Mahmoud Shehabi Khorassani | 师→生（direction: advisor） | 1971 德黑兰大学法学博士阶段授课教授之一 |
| colleague | Azadeh Moaveni | 无向 | 2006 回忆录 Iran Awakening 合作者 |

> 已存在的库内边（20 世纪批次写入，勿重复）：Betty Williams(6758)/Mairead Corrigan(6759)→本条 colleague（Nobel Women's Initiative 共同创始人）、本条→Jody Williams(6765)、本条→Rigoberta Menchú(6766) colleague 边；Wangari Maathai(6764) 边由本批 Maathai yaml 建立，本表勿重复。
> 不入库存档：丈夫（page.md 无姓名）、女儿 Nargess Tavassolian（无 wiki 链接）、Zahra Kazemi（委托代理关系，非白名单类型）、Reza Pahlavi（2026 任命，政治敏感慎之又慎不入）。

### 第 5 步：配色方案（manifest 预分配，勿改主色）

- **主色**：波斯松绿 `#145C54`（绿松石与法庭深绿的沉稳）
- **辅色**：诺奖香槟金 `#C9A227`
- **badgeA–D 四分类色**：
  - `badgeA` 人权辩护 — 靛蓝 `#4C5FD5`
  - `badgeB` 妇女权利 — 青绿 `#0E7C7B`
  - `badgeC` 儿童权利 — 琥珀 `#E07B30`
  - `badgeD` 法治 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡 + 细阿拉伯式几何网格线（八角星母题），呼应波斯法庭装饰

### 第 6 步：幻灯片序列（15 页 = 项目首页 + 13 帧正文 + 结尾，含身份信息页★）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 2003 诺贝尔和平奖 · Shirin Ebadi b. 1947 + 四色 badge + 右上肖像
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年/出生地/教育/任职/荣誉/组织）
03  2003 诺贝尔和平奖 — 理由 EN+中译；首位伊朗得主、首位穆斯林女性得主；机场迎接与国内反响（客观）
04  法官岁月 (1969–1979) — 首批女法官、1975 德黑兰城市法院首位女院长、革命后免职
05  断档十年 (1979–1993) — 降为书记员、执业被拒、著书撰稿
06  律师席上的案件 — Forouhar 夫妇、1999 学生抗议案、录像带案判决与撤销
07  儿童与妇女的权利 — Arian/Leila 案、儿童监护法、2002 反虐待儿童法（核心贡献页）
08  两个组织 — SPRC(1994) 与 DHRC(2001)
09  颁奖演讲与立场 — 反对强行政权更迭、伊斯兰与民主相容论（并列 page.md 各方表态，零评价）
10  诺贝尔女性倡议 (2006) — 六位女性诺奖得主联合创举
11  压力与流亡 (2008–2009) — 威胁声明、办公室查封、奖章被取走、定居伦敦
12  后诺奖岁月 — 美国财政部诉讼胜诉、巴哈伊案辩护、2019 妇女暴力条约呼吁
13  荣誉与著述 — Rafto/Legion of Honour、Iran Awakening 等
14  结尾 — 品牌标注 OpenMathAI
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 09/11 页为敏感内容：全部短句化、无形容词、每页 ≤7 条目。
- 时间线页若超载：05 与 06 可合并为「免职与复业 (1979–1993)」。

| 陷阱 | 说明 |
|------|------|
| 政治红线 | 1979 革命、核计划、2009 选举及抗议、2015/2018/2026 表态等一律只客观记录 page.md 句子，禁止任何立场词 |
| 各方表态并列 | 获奖后 Khatami「政治性」评论与机场民众欢迎必须并列呈现，单侧叙事禁写 |
| 原话引用 | 仅 page.md 载有英文原文者可入引文框（如「反对任何外国干涉」「I will shut up...」）；波斯语/转译句禁引 |
| 在世 | b. 1947 无卒日，三处（封面/身份页/结尾）一致「在世」；禁用享年 |
| 奖章被没收 | 表述用「被革命法庭取走（Ebadi 方陈述）+ 伊朗当局否认」，双口径并列；「首次被国家没收」标注挪方声明口径 |
| 教授关系 | 仅 Shehabi Khorassani 一人（1971 授课教授之一）；勿把「教授们」扩成导师名单 |
| 名字拼写 | 中文页用「希琳·伊巴迪」；波斯文原名列于封面即可，勿误写 Shirin Ebadi 为 Shirīn |
| 组织顺序 | SPRC(1994) 在先、DHRC(2001) 在后；DHRC 是其 Known for，页面权重 DHRC 优先但年份勿倒 |
| 女儿 | Nargess Tavassolian 被指控改信巴哈伊系 IRNA 攻击文章内容；转述时注明为官方媒体指控、本人否认 |
| 流亡年份 | 2009 年起定居伦敦（page.md 明文）；勿写「2009 被驱逐」 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Defenders of Human Rights Center | 人权捍卫者中心（DHRC） | 2001 创立 |
| Society for Protecting the Rights of the Child | 儿童权利保护协会（SPRC） | 1994 创立 |
| Nobel Women's Initiative | 诺贝尔女性倡议 | 2006 六人共同创立 |
| Rafto Prize | 拉夫托奖 | 2001，获奖前哨 |
| Chain murders of Iran | 伊朗连环谋杀案 | 1990 年代末，客观案件名 |
| Tape makers case | 录像带案 | 2000 判决后被撤销 |
| Iran Awakening | 《伊朗觉醒》 | 2006 回忆录 |
| Refugee Rights in Iran | 《伊朗的难民权利》 | 2008 专著 |
| pro bono | 义务辩护 | 其执业特征词 |
| transitional justice | 过渡司法 | 2026 委员会语境，仅名词不展开 |

## 四、BGM 【manifest 预分配，勿改】

- **选定曲目**：**With Me** — Alex-Productions
- **匹配理由**：钢琴与弦乐的克制陪伴感，匹配「孤独法庭上仍与受难者同行」的守护气质——辩护席而非讲台才是她的事业主场。
- **本地路径**：`music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav`
- **时长对齐**：15 页 ≈ 105 秒，ffmpeg `-shortest` 自动收尾

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/21th_century/Shirin_Ebadi/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md` | 获奖理由中译照抄来源 |
| `MySQL/data/Shirin_Ebadi.yaml` | 入库 yaml（stub #6763 UPD 回填 QID） |
| `peace/PROMPTS_WORKFLOW_21ST.md` | 21 世纪批次工作流（伊朗红线） |

> **执行要求：0 error、vbox≤10pt/hbox≤50pt、逐页 pdftoppm 目检、make images+video。**
