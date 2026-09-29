# 文学家立传提示词（OpenLiterature 21 世纪批次：Mo Yan / 莫言）

> **本文件是 Mo Yan（莫言，2012 诺贝尔文学奖）的人物专属立传提示词**，供后续 Beamer 立传 agent 直接复制到新对话中按步执行。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（内容适配文学家）。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 旗下，与 mathematician/physicist/chemist 侧同构）。
- **本实例**：Mo Yan（莫言，本名管谟业 Guan Moye），中国小说家、编剧，2012 诺贝尔文学奖得主——首位获诺贝尔文学奖的中国公民。
- **设计哲学**：文学家立传保留「身份信息页」与「研究领域结构化表达」两大骨架；文学家无公式框——用**名句引文框 / 代表作书影 / 意象图式**替代。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Mo Yan（莫言，本名 Guan Moye 管谟业，1955-02-17 生于山东高密，在世）
- **官方获奖理由**（2012，Wikipedia 原文照录，禁止改写）：
  > "with hallucinatory realism merges folk tales, history and the contemporary"（中译照录 `generate_21st_century_list.py` CITATION_ZH：表彰其以魔幻现实主义融合民间故事、历史与当代）
- **气质关键词**：**幻象现实主义、高密东北乡、民间说书的想象力** —— 2012 年时被译最多的中国文学作家。
- **设计母题**：**红高粱地（the sorghum field）**。其文学宇宙根植于山东高密东北乡——红高粱、土地、民俗与民间戏曲——视觉语言取「高粱地的大地色块 + 深绿主色」：大地色横带 + 麦金光斑，呼应「以乡土滋养的幻象世界」。
- **本地数据源**：
  - `literature/presentations/pages/21st_century/Mo_Yan/page.md`（Wikipedia 全文 + frontmatter）
  - `literature/presentations/pages/21st_century/Mo_Yan/metadata.json`、`images.txt`
  - Wikipedia URL: https://en.wikipedia.org/wiki/Mo_Yan （肖像：infobox「Mo Yan in 2008」，第 0 步待下载）

---

## 三、任务流程 【逐步执行】

> 数据库同步要求：包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 greatminds 库（MySQL），yaml 路径 `MySQL/data/Mo_Yan.yaml`，入库引擎 `MySQL/seed_person.py`。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已下载（事实基准如下，第一轮已核对）
- 肖像待下载：infobox 照片（Mo Yan in 2008）
- **事实基准**：
  - 生年：1955（infobox 1955-02-17；正文导语作 03-05——**两说并存，取 frontmatter/infobox 02-17 并加注**）
  - 国籍：中华人民共和国
  - 家庭：山东高密平安村农家，行四（两兄一姐）；父读过四年私塾通古籍；母不识字
  - 教育：五年级辍学（文革中 11 岁）放牧自学《新华字典》→ 1976 年底参军 → 1984 解放军艺术学院文学系首届（主任徐怀中）→ 1988 中国作协与北京师范大学合办研究生班 → 1991 北师大文学硕士
  - 笔名「莫言」：1981 在保定《莲池》投稿时起；拆「謨」字、亦有「少说话」的时代印痕；后因领稿费之便成为法定姓名
  - 关键荣誉：Nonino 2005 · 福冈亚洲文化奖 2006 · Newman Prize 2009 · 茅盾文学奖 2011（《蛙》）· Nobel 2012；另获多所高校荣誉博士
  - 配偶：杜勤兰（1979 结婚）；女儿管笑笑（1981 生）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列展开）

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/21st_century/` 下创建 `Mo_Yan/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同批已完成人物目录的 Makefile，设置 `MAIN=Mo_Yan_zh`、`VIDEO_NAME=Mo_Yan_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：infobox 照片（curl -A "Mozilla/5.0"，500px）；404 则用 images.txt 兜底，再不行用装饰圆占位
- 可选插图：《红高粱家族》书影或电影《红高粱》（1988 柏林金熊）剧照意象

### 第 4 步：文学领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | hallucinatory realism | 幻象现实主义 | 诺奖理由核心词，其标志风格 | 诗学/风格页 |
| 1 | magical realism | 魔幻现实主义 | infobox Movement；承袭马尔克斯 | 风格页 |
| 2 | historical novel | 历史小说 | 史诗性长篇，1923–1976 家族史等 | 作品页 |
| 3 | satire | 讽刺（黑色幽默） | 酒国/生死疲劳的社会讽刺 | 风格页 |
| 4 | folk literature | 民间文学 | 民间传说、地方戏曲、说书传统 | 根源页 |

- 入库：`fields` 写入 `person_field`（带 rank）；缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

> 只收 page.md 明载关系；yaml 与本表完全一致。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Du Qinlan（杜勤兰） | 无向 | 妻子，1979 结婚 |
| parent-child | Guan Xiaoxiao（管笑笑） | 无向 | 女儿，1981 生 |
| advisor-student | Xu Huaizhong（徐怀中） | 徐→莫言（导师） | 解放军艺术学院文学系主任，其导师；将《金萝卜》改名《透明的红萝卜》 |
| influence | Sun Li（孙犁） | 无向 | 早期文学范本，以优美抒情文风著称 |
| influence | William Faulkner | 无向 | 《喧哗与骚动》启发其写熟悉的家乡人 |
| influence | Gabriel García Márquez | 无向 | 魔幻现实主义之影响 |
| influence | Lu Xun（鲁迅） | 无向 | 社会现实主义影响；酒国以吃人隐喻承其笔法 |
| colleague | Zhang Yimou（张艺谋） | 无向 | 《红高粱》改编电影导演，1988 柏林金熊 |
| colleague | Howard Goldblatt（葛浩文） | 无向 | 美国汉学家，其作英译者，助其走向国际 |
| colleague | Liu Xinwu（刘心武） | 无向 | 《人民文学》主编因《欢乐》停职；1999 网易文学大赛共同评委 |
| colleague | Wang Meng（王蒙） | 无向 | 1999 网易文学大赛共同评委 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **主色**：深绿 `#1E4D3B`（高粱地与黄土地的深绿基调）
- **诺奖香槟金**：`C9A227`
- 四分类色（badgeA–D）：
  - `badgeA` 幻象/魔幻现实主义 — 靛蓝 `#4C5FD5`
  - `badgeB` 史诗历史长篇 — 琥珀 `#E07B30`
  - `badgeC` 民间文学与戏曲 — 青绿 `#0E7C7B`
  - `badgeD` 社会讽刺 — 玫瑰 `#C4204F`
- **背景母题**：大地色横带 + 麦金光斑，呼应「红高粱地」母题

### 5.1 文学家格式硬要求 【★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：底部状态栏给出 `国籍 | 身份 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心内容之前。左头像 + 右信息网格，含至少：生年、本名、笔名来历、国籍、出生地、家庭、教育、职业（小说家/编剧）、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注 `OpenMathAI`；引号用半角 `" "`；中文引号内不写「原话」，除非 page.md 有英文原文。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenLiterature 项目首页（\input cover/openliterature_page.tex）
01  封面 — 幻象现实主义大师 / Mo Yan 莫言 1955– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  高密童年 (1955–1976) — 农家行四、五年级辍学放牧、《新华字典》自学、棉花加工厂
04  笔名「莫言」 — 1981《莲池》起笔；拆「謨」字与「少说话」的双重来历；后成法定姓名
05  军旅与学院 (1976–1991) — 参军、军图书管理员读千册、解放军艺术学院徐怀中门下、北师大硕士
06  成名 — 1984《透明的红萝卜》→ 1986《红高粱家族》→ 张艺谋电影 1988 柏林金熊
07  作品长廊 — 11 长篇时间轴（红高粱 1986 → 蛙 2009）
08  风格（核心贡献页）— 幻象现实主义 + 黑色幽默 + 民间说书传统；42 天毛笔写就《生死疲劳》
09  影响谱系 — Faulkner / Márquez / 鲁迅 / 孙犁 / 《水浒》《西游》《红楼》意象图式
10  争议简述 — 2012 获奖后的批评与莫言回应，按 page.md 客观简述（见第 9 步陷阱）
11  荣誉长廊 — Nonino 2005 · 福冈 2006 · Newman 2009 · 茅盾文学奖 2011 · Nobel 2012
12  遗产与结尾 — 首位中国籍诺奖文学得主；2012 年译本最多的中国作家
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现参照成品 `\profileslide`。
- 引文框/意象图式替代公式框：代表作页用 tikz 引文框呈现书名与年份（勿杜撰情节外的「原话」）。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删装饰元素 → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Mo Yan 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 政治红线 | 2012 获奖后争议（延安文艺座谈会讲话手抄、未签刘晓波请愿、Rushdie 批评、斯德哥尔摩发布会答问）**只按 page.md 客观简述一页/一句，不作政治评价、不展开叙事、不进引文框**；《天堂蒜薹之歌》因天安门事件后遭禁又解禁等经历只作作品背景客观陈述 |
| 获奖理由口径 | EN 原文是 "with hallucinatory realism merges folk tales, history and the contemporary"；CITATION_ZH 中译作「魔幻现实主义」——中译照录不改，英文侧勿把 hallucinatory 写成 magical |
| 生年两说 | infobox/frontmatter 1955-02-17 vs 正文导语 03-05——采用 02-17 并加注两说 |
| 笔名来历 | 拆「謨」字 + 父母告诫少说话的双重来历；后因邮局领稿费不便成为法定姓名——两条都写，勿只写其一 |
| 导师 | 徐怀中（解放军艺术学院文学系主任，导师）；《透明的红萝卜》原名《金萝卜》系徐改名 |
| 早期范本 | 早期文学范本是孙犁（Sun Li, born 1913），勿与孙中山等同名混淆 |
| 《欢乐》事件 | 1987《欢乐》在《人民文学》引发风波、主编刘心武停职——客观一句，属作品史实非政治叙事 |
| 荣誉博士 | 正文列 6 所（CUNY/佛光/索菲亚/香港公开/澳门/浸会 2013–2017）；frontmatter 的 CUHK、Aix-Marseille 正文无载——以正文为准 |
| 手写偏好 | 《生死疲劳》42 天、50 余万字毛笔手写于传统纸；反对拼音输入「限制词汇」——数字勿写错 |
| 无载禁写 | 母亲姓名、兄姐姓名、孙辈等 page.md 未载者一律不写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| hallucinatory realism | 幻象现实主义 | 诺奖理由原词，勿与魔幻现实主义混写 |
| magical realism | 魔幻现实主义 | infobox Movement 口径 |
| Gaomi | 高密 | 山东高密东北乡，文学地图核心 |
| pen name | 笔名 | 莫言 = "don't speak" |
| social commentary | 社会批判 | 作品主基调 |
| black humour | 黑色幽默 | 风格要素 |
| Xungen movement | 寻根文学 | 《老枪》被视为寻根文学范例 |
| Pinyin input | 拼音输入法 | 其手写偏好的对照 |
| adaptation | 影视改编 | 红高粱/幸福时光/暖等 |
| folk oral literature | 民间口传文学 | 其语言养分，勿写成「口头文学」 |

---

## 四、背景音乐建议 ✅ 【人物专属】

- **选定曲目**: **With Me** — Alex-Productions（52k views，高受众 / 温和 / 稳定）
- **匹配理由**:
  - 「温和/稳定」匹配其叙事气质 —— 苦难书写之上的幽默与温情，笔名「莫言」的自持内敛
  - 「人物介绍」型曲风匹配高密乡土的长线人生叙事 —— 放牧童年 → 军旅 → 学院 → 成名，段落平实不夸张
  - 主色深绿的大地基调与该曲的稳定律动相称，避免过度戏剧化盖过「民间说书」的从容
- **备选**（未采用）：★★ Savage（叙事张力强，但其争议页需克制处理，温和曲更稳妥）
- **本地路径**: `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` → 复制到本目录 `WithMe.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/21st_century/Mo_Yan/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `literature/generate_21st_century_list.py` | 获奖理由中译（CITATION_ZH）对照 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
