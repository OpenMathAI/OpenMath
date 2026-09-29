# OpenPeace 人物立传提示词（实例：Bertha von Suttner）

> **本文件是 OpenPeace 项目（诺贝尔和平奖得主立传）的人物立传提示词**，
> 以贝尔塔·冯·苏特纳（Bertha von Suttner，1905 诺贝尔和平奖，首位女性和平奖得主）为完整实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Bertha Sophie Felicitas Baroness von Suttner（née Countess Kinsky von Wchinitz und Tettau）。
- **设计哲学**：和平奖个人立传须有「身份信息页」（Identity / Bio 速览页），并以「事业领域」结构化表达；叙事主线是「从贵族小姐到世界和平运动领袖」的转折。

---

## 二、背景信息 【人物专属】

- **目标人物**：Bertha von Suttner（1843-06-09 布拉格 ~ 1914-06-21 维也纳，享年 71 岁）
- **气质关键词**：**《放下武器！》的作者、和平运动的第一夫人、诺奖遗嘱的隐形推手**
- **诺奖年份与官方获奖理由**：1905 年诺贝尔和平奖（独得）
  > 中文获奖理由（照抄名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写）：
  > **「表彰她敢于直面并反对战争的恐怖」**
- **设计母题**：**折断的剑与钢笔（broken sword & pen）**——她以小说与新闻为武器反对战争主义，视觉上以「剑折为笔」的意象贯穿
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Bertha_von_Suttner/page.md`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准（人物专属，第一轮已核对）

- 生卒：1843-06-09 生于布拉格 Kinský Palace（波希米亚王国，奥地利帝国）~ 1914-06-21 逝于维也纳（奥匈帝国），享年 71 岁；骨灰按 1907 年遗嘱存放于德国哥达（Gotha）当地骨灰堂
- 本名与家世：Countess Kinsky von Wchinitz und Tettau；父 Franz Michael Graf Kinsky（奥地利中将，她出生前去世）；母 Sophie Wilhelmine von Körner（比夫小 45 岁以上）；因「混合」血统被奥地利高等贵族排斥
- 家庭：丈夫 Arthur Gundaccar von Suttner（1850–1902，金斯基家家庭教师任上相识，因男方父母反对 1876 年秘密结婚、被家族剥夺继承权）
- 教育与才艺：无正规学校教育，私人教师教授法语/意大利语/英语；业余钢琴与演唱造诣深，曾师从 Gilbert Duprez（巴黎 1867）、Pauline Viardot（巴登-巴登 1868）追求歌剧演员生涯未果
- 任职/经历：金斯基家家庭教师（1873）→ 巴黎 Alfred Nobel 秘书兼管家（1876，仅数周）→ 格鲁吉亚明格列里亚/库塔伊西语言音乐教师（1876–1885）→ 回奥地利后专事写作与和平运动（1885 起）
- 关键荣誉：1905 诺贝尔和平奖（1905-12-10 授奖，1906-04-18 于克里斯蒂安尼亚发表诺奖演讲 *The Evolution of the Peace Movement*）
- 核心事业清单：
  1. 《放下武器！》（*Die Waffen nieder!*，1889）——37 个版本、译成 15 种语言，使其成为奥地利与欧洲和平运动领袖
  2. 创办并领导奥地利和平协会 *Gesellschaft der Friedensfreunde*（1891，任主席）与德国和平协会（1892 创立）
  3. 主编国际和平主义期刊 *Die Waffen nieder!*（1892–1899）
  4. 1897 向皇帝 Franz Joseph I 呈交签名请愿，敦促设立国际法院；1899 参加第一次海牙公约会议
  5. 1907 年第二届中国海牙和平会议唯一与会女性（对该会议持强烈批评并警告大战将至）
  6. 1911 加入卡内基国际和平基金会顾问委员会；临终前仍在筹组原定 1914-09 召开的和平会议
- 思想来源（page.md 明文）：其和平主义受 Kant、Buckle、Spencer、Darwin、Tolstoy 著作影响；主张和平权可依国际法主张，以达尔文式进步史观论证和平
- 关键时间线（15–20 节点）：1843 生于布拉格 → 1855 姨母与表妹加入家庭 → 1856/1859 随母赴威斯巴登赌博谋财失败迁居 → 1864 巴特洪堡结识明格列里亚王后 Ekaterine Dadiani 与沙皇亚历山大二世 → 1867/1868 巴黎与巴登-巴登声乐求学 → 1872 与 Sayn-Wittgenstein-Hohenstein 王子订婚（同年 10 月王子死于海难）→ 1873 金斯基家家庭教师 → 1876 巴黎任 Nobel 秘书（数周）→ 1876 与 Arthur 秘密结婚 → 1876–1885 格鲁吉亚流亡执教与写作 → 1877–78 俄土战争期间 Arthur 为《新自由报》战地报道 → 1883 《Inventarium einer Seele》出版（莱比锡）→ 1885 与 Suttner 家族和解，定居下奥地利 Harmannsdorf 城堡 → 1889 《放下武器！》出版 → 1891 奥地利和平协会（主席）→ 1892 德国和平协会创立 + 期刊创刊 → 1897 向皇帝呈签名请愿 → 1899 第一次海牙会议 → 1902 丈夫去世、卖掉城堡迁维也纳 → 1904 柏林国际妇女大会、七个月巡游美国（会晤罗斯福总统）→ 1905 获诺贝尔和平奖 → 1906-04-18 诺奖演讲 → 1907 第二次海牙会议（唯一女性）→ 1911 卡内基基金会顾问 → 1914-06-21 癌症逝于维也纳（七日后斐迪南大公遇刺，一战爆发）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Bertha_von_Suttner/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品的 Makefile，设置 `MAIN=Bertha_von_Suttner_zh`、`VIDEO_NAME=Bertha_von_Suttner_zh`

### 第 3 步：收集图片 【人物专属】

- page.md infobox 有真实肖像：`Bertha_von_Suttner_1860s.jpg`（1873 年青年照）与 `Bertha_von_Suttner.png`（1896）；优先取 1896 年版肖像（Commons Special:FilePath 取 500px），404 则退 1860s 版
- 另有 1912 年 *St. Louis Post-Dispatch* 想象画（Marguerite Martyn 作）可作插图

### 第 4 步：事业领域梳理 + 入库（fields，与 yaml 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace movement | 和平运动 | 组织建设、大会与巡回演讲，获奖核心 | 和平活动页 |
| 1 | pacifist literature | 和平主义文学 | 《放下武器！》等小说 | 写作页 |
| 2 | journalism | 新闻工作 | 期刊编辑、驻外通讯员、自宣传渠道 | 和平活动页 |
| 3 | disarmament | 裁军 | 一战前持续反对国际军备扩张 | 晚年页 |
| 4 | women's movement | 妇女运动 | 1904 柏林国际妇女大会、性别平等主张 | 性别平等节 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Arthur Gundaccar von Suttner | 无向 | 1876 秘密结婚，格鲁吉亚流亡与写作伴侣，1902 卒 |
| influence | Alfred Nobel | 无向 | 1876 短暂任其秘书，后通信至 1896；被认为促成其遗嘱设立和平奖 |
| influence | Immanuel Kant | 无向 | page.md 明文列其和平主义思想来源 |
| influence | Henry Thomas Buckle | 无向 | page.md 明文列其和平主义思想来源 |
| influence | Herbert Spencer | 无向 | page.md 明文列其和平主义思想来源 |
| influence | Charles Darwin | 无向 | page.md 明文列其和平主义思想来源 |
| influence | Leo Tolstoy | 无向 | 思想来源；托尔斯泰曾赞誉《放下武器！》 |
| colleague | Ernest Renan | 无向 | 回奥地利后与这位法国哲人书信往还 |
| colleague | Theodor Herzl | 无向 | 1899 海牙之行得其资助（以《Die Welt》通讯员身份） |

- Kant 沿用库内 'Immanuel Kant'(1256)、Darwin 用 'Charles Darwin'(4586)、Tolstoy 用 'Leo Tolstoy'(4903)；Herbert Spencer / Henry Thomas Buckle / Ernest Renan / Theodor Herzl / Alfred Nobel / Arthur Gundaccar von Suttner 新建 stub（不编造 qid）

#### 4.5.1 入库要点

- seed_person.py 幂等按 QID → name_en 匹配；influence 类型不写 direction（引擎按无向处理）
- 无 co-honored 关系（1905 独得）

### 第 5 步：配色方案（manifest 预分配，勿改）

- **主色**：`#0E4D64`（深海蓝——理性与坚定）
- **辅色**：诺奖香槟金 `C9A227`
- badgeA–D：badgeA 和平运动（`#1F6B4E`）、badgeB 和平主义文学（`#8C3B2E`）、badgeC 新闻（`#B08A2E`）、badgeD 妇女运动（`#5B4E8C`）

### 第 6 步：规划幻灯片序列（11–14 页）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 1905 诺贝尔和平奖 · 贝尔塔·冯·苏特纳 1843–1914 + 四色 badge + 右上肖像
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/本名/国籍/婚嫁/职业/荣誉/核心领域）
03  布拉格贵族的窘境 (1843–1873) — 混血血统、家庭教师、声乐梦
04  巴黎数周：Nobel 的秘书 (1876) — 秘密婚姻与流亡的起点
05  格鲁吉亚岁月 (1876–1885) — 库塔伊西执教、写作谋生
06  《放下武器！》(1889) — 37 版/15 语种、和平运动转折点
07  组织者：从维也纳到柏林 (1891–1897) — 两个和平协会 + 期刊
08  海牙与请愿 (1897–1907) — 1899 首届海牙、1907 唯一女性、对战争的警告
09  1905 诺贝尔和平奖 — 获奖理由 + 1906 演讲
10  美国之行与妇女大会 (1904) — 七个月巡游、会晤罗斯福
11  思想：宗教批判与性别平等 — 引文框用 page.md 载有原文者
12  晚年与未竟的会议 (1911–1914) — 卡内基顾问、癌症、1914-06-21
13  遗产 — 货币/邮票/Google Doodle、对和平运动的持久影响
14  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 「第二位女性诺奖得主」 | page.md 明文：继 1903 Marie Curie 之后第二位女性得主、首位女性和平奖得主、首位奥地利得主——三个「第一/第二」勿混 |
| 授奖时点 | 1905-12-10 授奖，**演讲在 1906-04-18**（克里斯蒂安尼亚），勿写 1905 年演讲 |
| Nobel 关系 | 仅任职数周的秘书 + 此后通信；「促成其遗嘱设立和平奖」是 page.md 的 believed/明文表述，勿升级为「事实证明」 |
| 与罗斯福 | 1904 美国巡游「会晤总统」仅一面之缘，**禁建关系行**、禁写「共同推动」 |
| 引语红线 | 正文长引语（婚姻回忆、海牙批评、1906 诺奖演讲引文）page.md 有英文原文可用；转述性中文引语禁造 |
| 生卒地 | 生于布拉格（当时属奥地利帝国），卒于维也纳——勿写「奥地利出生」 |
| 名字 | 本姓 Kinsky von Wchinitz und Tettau；"B. Oulot" 是她早期男性化笔名来源（Boulotte 绰号），勿写成真名 |
| 宗教内容 | 其宗教批判只按 page.md 客观转述（虚构场景中的「假洗脚」等），不评价宗教本身 |
| 政治敏感红线 | 对 1907 海牙会议的批评、一战前警告等只作 page.md 明载的客观事实记录，不加当代政治评价 |
| 同名区分 | 无，但 Arthur 无独立维基条目（红链），yaml stub 用全名 Arthur Gundaccar von Suttner |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Die Waffen nieder! | 《放下武器！》 | 意第绪/德语书名斜体；英译 Lay Down Your Arms! |
| pacifism | 和平主义 | 与 anti-militarism 区分 |
| Inter-Parliamentary Union | 各国议会联盟 | 她见证其成立 |
| Gesellschaft der Friedensfreunde | 和平之友协会 | 奥地利组织，1891 |
| German Peace Society | 德国和平协会 | 1892 她参与创立 |
| Hague Conventions 1899/1907 | 海牙公约（1899/1907） | 1899 与会 vs 1907 唯一女性，勿混 |
| Carnegie Endowment for International Peace | 卡内基国际和平基金会 | 1911 顾问委员会 |
| cremation / columbarium | 火化 / 骨灰堂 | 哥达（Gotha），勿写墓地土葬 |
| Nobel lecture | 诺贝尔演讲 | 1906-04-18，题目 The Evolution of the Peace Movement |

---

## 四、背景音乐 ✅（manifest 预分配，勿改）

- **选定曲目**: **Expedition** — Alex-Productions
- **匹配理由**: 远征感的行进节奏匹配她从布拉格→巴黎→格鲁吉亚→维也纳→海牙的漂泊与战斗轨迹；「探险」也隐喻和平运动的拓荒年代
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`
- **时长**: 以 ffmpeg `-shortest` 对齐页数

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Bertha_von_Suttner/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 0–11 节结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/Bertha_von_Suttner.yaml` | fields + relations 入库母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
