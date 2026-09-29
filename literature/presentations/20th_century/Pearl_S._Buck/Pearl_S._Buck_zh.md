# 文学家立传提示词（OpenLiterature 批次实例：Pearl S. Buck）

> 本文件是 OpenLiterature 的「文学家立传提示词」，以 Pearl S. Buck（1938 诺贝尔文学奖，《大地》）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框，以代表作书影/名句引文框/意象图式替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 共享仓库，结尾页品牌统一 `OpenMathAI`）。
- **本实例**：Pearl S. Buck（赛珍珠，1892–1973），1938 诺贝尔文学奖得主，**首位获诺贝尔文学奖的美国女性**。
- **设计哲学**：文学家立传以「代表作意象 + 文学领域结构化表达 + 身份信息页」为骨架；Buck 的核心视觉语言是**大地与两个世界（the Good Earth and her several worlds）**——她自述活在「几个世界」之间：父母的长老会世界与「博大、深情、热闹的中国世界」。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Pearl Comfort Sydenstricker Buck（1892-06-26 ~ 1973-03-06，享年 80 岁）
- **气质关键词**：**跨太平洋的叙事者、中国农民的史诗书写者、人道主义行动派**
- **官方获奖理由（1938）**：
  > EN: "for her rich and truly epic descriptions of peasant life in China and for her biographical masterpieces"
  > 中译：表彰其对中国农民生活的丰富而真正的史诗式描写，以及其传记性的杰作
  > （来源：`literature/generate_20th_century_list.py` CITATION_ZH[("1938","Pearl Buck")] + `literature/nobel_literature_citations.json`，禁止改写）
- **设计母题**：**大地与双重世界**——以土地色块/河流冲积平原图式呈现《大地》三部曲的世界；两侧以对照色呈现「父母的白色长老会世界」与「中国的世界」。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Pearl_S._Buck/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`；Wikipedia URL: https://en.wikipedia.org/wiki/Pearl_S._Buck
  - 肖像（第 0 步下载）：`images/` 下待下载（infobox 有 1932 年照片及 Smithsonian 画像等，404 则装饰圆占位）

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md；frontmatter 生日噪声 ["1892-06-26","1892-00-00"] 取 1892-06-26）

- **生卒**：1892-06-26 生于美国西弗吉尼亚州 Hillsboro；1973-03-06 卒于佛蒙特州 Danby（肺癌），享年 80 岁。葬于宾州 Perkasie 的 Green Hills Farm，**墓碑仅以中文篆书「賽珍珠」镌刻**。
- **国籍**：美国（United States）。
- **本名与中文名**：本名 Pearl Comfort Sydenstricker；中文名**赛珍珠**（Sài Zhēnzhū）。
- **家庭**：父 Absalom Sydenstricker（1852–1931，南长老会传教士）；母 Caroline Maude Stulting（1857–1921）；兄 Edgar Sydenstricker（公共卫生领域）；妹 Grace Sydenstricker Yaukey（笔名 Cornelia Spencer，作家）。长女 Carol 患苯丙酮尿症致重度发育障碍；共 8 个孩子（含收养）。
- **婚姻**：1917-05-13 与农经学家传教士 John Lossing Buck 结婚（1935-06-11 于 Reno 离婚）；**同日**与出版人 Richard J. Walsh（John Day 出版社）结婚（Walsh 1960 年去世）。
- **教育**：Randolph-Macon Woman's College（BA，1914，Phi Beta Kappa）；Cornell University（MA，1924）。
- **经历**：5 个月大随父母赴中国，长于淮安、镇江（1896 起），夏季居庐山牯岭（在此立志成为作家）；1914–1932 任长老会传教士；1920–1933 居南京金陵大学校园并在金陵大学、国立中央大学等任教英语文学；1927 南京事件避居日本一年；1934 离华返美定居宾州 Bucks County 的 Green Hills Farm。1949 年后多次申请返华被拒；1972 年未能随尼克松访华。
- **文学师承与影响**：page.md 明载——狄更斯（Charles Dickens）小说她一生「每年重读一遍」；诺贝尔演说自述「我讲故事的最初心得来自中国」，并论及《三国演义》《水浒传》《红楼梦》；与中国作家徐志摩、林语堂的友好交往鼓励她成为职业作家。
- **核心作品与贡献（4–6 条）**：
  1. *The Good Earth*（1931）——《大地》三部曲首部，1931/1932 全美畅销书榜首，1932 普利策小说奖。
  2. 《大地》三部曲：*The Good Earth*（1931）/ *Sons*（1933）/ *A House Divided*（1935）。
  3. 父母双传：*The Exile*（1936，写母亲）与 *Fighting Angel*（1936，写父亲）——即获奖理由中的「传记性杰作」。
  4. *All Men Are Brothers*（1933）——英译《水浒传》。
  5. *The Big Wave*（1948，儿童文学，Josette Frank 奖前身获奖）。
  6. 人道主义事业：1949 创立 The Welcome House（首个收养亚裔/混血儿童的国际跨种族收养机构）；Pearl S. Buck Foundation（1964 韩国 Opportunity Center 等）；1967 捐出逾 700 万美元版税。
- **关键荣誉**：Pulitzer 1932；William Dean Howells Medal 1935；Nobel 1938（**首位获文学奖的美国女性**）；National Women's Hall of Fame 1973；1983 美国 5 美分纪念邮票。
- **关键时间线（18 节点）**：
  1. 1892-06-26 生于 Hillsboro, West Virginia
  2. 1892-10（5 个月大）随父母移居中国，先居淮安
  3. 1896 迁居镇江
  4. 1899–1901 义和团运动波及全家
  5. 童年每年庐山牯岭避暑，立志写作
  6. 1911 返美入 Randolph-Macon Woman's College
  7. 1914 毕业（Phi Beta Kappa）返华
  8. 1917-05-13 与 John Lossing Buck 结婚，移居安徽宿州（淮河流域）
  9. 1920–1933 居南京，多校任教；1920 长女 Carol 出生
  10. 1921 母亲去世
  11. 1924 赴美获 Cornell 硕士；1925 收养 Janice
  12. 1927 南京事件，避居日本一年
  13. 1930 *East Wind: West Wind*（Walsh 接受出版）
  14. 1931 *The Good Earth*；1932 Pulitzer
  15. 1933 英译《水浒》*All Men Are Brothers*
  16. 1934 离华返美；1935-06-11 离婚当日与 Walsh 结婚，定居 Green Hills Farm
  17. 1938 诺贝尔文学奖（首位美国女性）；1949 创立 Welcome House
  18. 1960 Walsh 去世；1973-03-06 卒于 Danby, Vermont，墓碑篆书「賽珍珠」
- **诺贝尔演说**：题为 "The Chinese Novel"（1938-12-12），page.md 实载引语可引："I am an American by birth and by ancestry"；"my earliest knowledge of story, of how to tell and write stories, came to me in China"。

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- `literature/presentations/20th_century/Pearl_S._Buck/`（含 `images/`）；Makefile 设 `MAIN=Pearl_S._Buck_zh`；肖像按 `images.txt` 下载，404 用装饰圆占位。

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | epic novel | 史诗式小说 | 中国农民生活的丰富而真正的史诗式描写（获奖理由） | 核心页 |
| 1 | biographical literature | 传记文学 | 父母双传《异邦客》《战斗的天使》 | 传记页 |
| 2 | cross-cultural literature | 跨文化写作 | 中美之间的「几个世界」叙事 | 文化页 |
| 3 | children's literature | 儿童文学 | *The Big Wave* 等四十余种 | 儿童页 |

- 入库：`MySQL/data/Pearl_S._Buck.yaml` → `python3 seed_person.py data/Pearl_S._Buck.yaml`（primary_occupation: writer）。

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | John Lossing Buck | 无向 | 1917 结婚，农经学家传教士，1935 离婚 |
| spouse | Richard J. Walsh | 无向 | 1935 结婚，John Day 出版人，1960 去世 |
| influence | Charles Dickens | Dickens → Buck | 其小说她一生每年重读一遍 |
| colleague | Xu Zhimo | 无向 | 与其时中国名作家的友好交往鼓励她职业写作 |
| colleague | Lin Yutang | 无向 | 同上，与其时中国名作家交往 |

> page.md 明载仅以上 5 条。父亲 Absalom 是传记对象与父母关系，page.md 有载——但为防家庭边噪音，本批只收配偶与文学关系（父母/子女边如需可由 Review 阶段裁定补充）。Nobel 委员会引文与 Nixon/Jiang Qing 等政治语境不入关系表。

### 第 5 步：设计配色方案

- **主色**（批次预分配）：蓝灰 `#37474F`（土地的沉稳与跨文化的克制）
- **辅色**：诺奖香槟金 `#C9A227`
- **badgeA–D**：badgeA 史诗小说 — 土棕 `#7A5230`；badgeB 传记文学 — 灰蓝 `#546E7A`；badgeC 跨文化 — 靛青 `#2C6E8F`；badgeD 儿童文学 — 暖橙 `#C97B30`
- **背景母题**：大地色块水平分层（田垄线）+ 双色对照圆（两个世界）。

### 第 6 步：幻灯片序列（16 页）

```
00  OpenLiterature 项目首页（\input cover 共享首页）
01  封面 — 大地与双重世界 / Pearl S. Buck 1892–1973 + 主色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、本名/赛珍珠、国籍、教育、婚姻、荣誉、核心领域）
03  核心贡献概览 — 大地三部曲 / 父母双传 / 水浒英译 / 人道主义事业
04  童年：几个世界之间 (1892–1911) — 淮安、镇江、庐山牯岭、义和团
05  求学与返华 (1911–1917) — Randolph-Macon、Cornell、宿州
06  南京岁月与写作志业 (1920–1934) — 金陵大学任教、Carol、南京事件、决意职业写作
07  《大地》：土地的史诗 (1931) — 三部曲结构 + 书影
08  父母双传 (1936) — The Exile / Fighting Angel（获奖理由中的「传记性杰作」）
09  官方获奖理由引文框（EN 原文 + 中译，禁止改写）
10  诺贝尔演说：The Chinese Novel — page.md 实载引语 + 三大中国古典小说
11  荣誉与认可 — Pulitzer 1932 / Howells 1935 / Nobel 1938（首位美国女性）/ 名人堂
12  人道主义事业 — Welcome House 1949、基金会、700 万美元捐赠、混血儿童收养
13  晚年 (1960–1973) — Walsh 去世、Danby 辞世、篆书「賽珍珠」墓碑
14  遗产 — 南京大学故居纪念馆、镇江研究会、对美国人中国观的塑造
15  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

- 版式：作品页多（三部曲/双传/水浒），用书影小图横排；引文框用 tcolorbox；时间线 18 节点分两栏。
- **陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名形式 | yaml name_en 用 frontmatter 的 **Pearl Buck**；叙述可用 Pearl S. Buck / 赛珍珠；本名 Pearl Comfort Sydenstricker 勿当姓 Buck 的变体 |
| 生日噪声 | frontmatter 有 ["1892-06-26","1892-00-00"]，取 1892-06-26；卒日同理取 1973-03-06 |
| 诺奖理由 | 官方 EN 整句引用 + CITATION_ZH 中译，禁止改写；「传记性杰作」指父母双传 |
| 首位口径 | 「首位获诺贝尔文学奖的美国女性」（page.md 明载）；勿拔高为「首位获奖女性」 |
| 宗教争议 | 基本教义-现代派论战与辞职仅客观一笔，不评价传教事业 |
| 政治内容 | 南京事件/文化大革命被谴责/1972 未能随尼克松访华（page.md 归因 Jiang Qing）/1962 为 Eichmann 求情——只按 page.md 客观一笔，**不作政治评价、不展开政治叙事** |
| Theodore Harris | 晚年财务顾问争议客观简述或略写，不做人身评判；三份遗嘱纠纷可一笔带过 |
| 笔名 | 部分小说以笔名 **John Sedges** 发表（The Townsman 等），勿与真名混淆 |
| 引语 | 仅引 page.md 实载英文原句（诺贝尔演说等），禁编造中文名句 |

### 第 9 步：术语审查清单

| 英文 | 中文 | 风险 |
|------|------|------|
| The Good Earth | 大地 | 1931；1937 年有电影版 |
| House of Earth trilogy | 大地三部曲 | Good Earth / Sons / A House Divided |
| The Exile | 异邦客 | 写母亲 Caroline |
| Fighting Angel | 战斗的天使 | 写父亲 Absalom |
| All Men Are Brothers | 《水浒传》英译 | 1933，勿与原书名 Water Margin 混用 |
| The Chinese Novel | 中国小说 | 诺贝尔演说题 |
| Zhenjiang | 镇江 | 旧 postal romanization 作 Chingkiang |
| Kuling, Mount Lu | 庐山牯岭 | 避暑别墅立志处 |
| Welcome House | 欢迎之家 | 1949 国际跨种族收养机构 |
| Pearl S. Buck Foundation | 赛珍珠基金会 | 1999 更名 International |
| Green Hills Farm | 绿丘农场 | 宾州故居与葬地 |
| Sai Zhenzhu | 赛珍珠 | 墓碑篆书，中文姓名姓氏在前 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（批次预分配）
- **匹配理由**：「白昼感」匹配 Buck 叙事的明亮底色——对农民的深情、对儿童的守护与人道主义的行动性；不同于以悲剧著称的中国题材刻板印象，她笔下是土地的丰饶与人间的烟火气。温暖、开阔、行动感强，匹配其「作家 + 行动派」的双重人生。
- **对照**：`music_audio/curated_tracks.md`（alex-productions 系列）。封面主色 `#37474F`，批次内唯一。
