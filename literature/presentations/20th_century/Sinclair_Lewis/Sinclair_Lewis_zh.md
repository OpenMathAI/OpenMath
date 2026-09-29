# 文学家立传提示词（OpenLiterature 实例：Sinclair Lewis）

> 本文件是 OpenLiterature 的「文学家立传提示词」人物专属实例，以 Sinclair Lewis（1930 诺贝尔文学奖，美国首位文学奖得主）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；文学家适配：无公式框，以**代表作书影 / 名句引文框 / 意象图式**替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Harry Sinclair Lewis（辛克莱·刘易斯）。
- **设计哲学**：保留「身份信息页」骨架；以**文学领域表**替代研究领域表、以**引文框/书影/意象图式**替代公式框。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Sinclair Lewis（1885-02-07 ~ 1951-01-10，享年 65 岁）
- **气质关键词**：**主街的解剖者、巴比特的创造者、美国第一位文学奖得主** —— 1930 诺贝尔文学奖获奖理由：
  > "for his vigorous and graphic art of description and his ability to create, with wit and humor, new types of characters"
  > （官方中译，照 `literature/generate_20th_century_list.py` CITATION_ZH，禁止改写）：表彰其强劲而生动的描写艺术，以及以机智与幽默创造新型人物的能力
- **设计母题**：**主街（Main Street）**。美国中西部小镇的主街立面——邮局、银行、理发店的招牌排成一排，远处玉米田平线——呼应他笔下的 Gopher Prairie 与 Zenith；badge 圆可做成 storefront 灯牌式圆框。
- **本地数据源**：`literature/presentations/pages/20th_century/Sinclair_Lewis/page.md`（Wikipedia 全文，事实基准已核对）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Sinclair_Lewis
- **肖像**：第 0 步待下载（1930 年像或 1914/1944 年照，images.txt 有线索）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（人物专属，第一轮已核对）

- 生卒：1885-02-07 生于明尼苏达州苏克中心（Sauk Centre）～ 1951-01-10 逝于意大利罗马（晚期酒精中毒；友人 Shirer 称心脏病发作——两说并存见陷阱表），享年 65 岁；骨灰葬苏克中心 Greenwood 墓园
- 国籍：美国
- 家庭：父 Edwin J. Lewis（威尔士裔医生，严苛）；母 Emma Kermott Lewis（1891 年去世）；继母 Isabel Warner（1892 年再娶，关系尚好）；兄 Fred(1875)/Claude(1878)；妻 Grace Livingston Hegger（《Vogue》编辑，1914–1928，子 Wells 1917–1944 阵亡）；妻 Dorothy Thompson（国际记者/专栏作家，1928–1942，子 Michael 1930–1975 舞台演员）
- 教育：Oberlin Academy（1902–03 预科一年）→ 耶鲁 1903 入学、1908 才获 BA（休学期间在 Upton Sinclair 的 Helicon Home Colony 合作社做工、赴巴拿马旅行）；耶鲁 *Courant* 与 *Literary Magazine* 编辑
- 文学师承与影响（page.md 明载）： Cayuse 无导师制师承；受惠于 Carmel 文人圈（诗人 George Sterling 帮其在《旧金山晚邮报》谋职）、1910 年会 Jack London、向 London 出售小说情节；社会主义党纽约支部同侪 Walter Lippmann/Ernest Poole 等；Mencken 称其 "red-haired tornado from the Minnesota wilds"
- 任职/流亡：无流亡；早期辗转记者/出版业（Waterlow, Iowa 社论撰稿 1908、Carmel、San Francisco、纽约 Frederick A. Stokes 1910）；1940 秋在威斯康星大学麦迪逊分校教创意写作（五节课后自言倾囊而别）
- 关键荣誉：Nobel Literature 1930（瑞典学院 Henrik Schück 提名）——**美国（乃至美洲）首位文学奖得主**；普利策小说奖 1926（*Arrowsmith*，**拒绝领取**，因不满 *Main Street* 落选）；美国邮政「伟大美国人」系列邮票
- 核心作品与贡献（4–6 条）：
  1. *Main Street*（1920，六个月售 18 万册、数年内约 200 万册）
  2. *Babbitt*（1922，讽刺美国商业文化与 boosterism；虚构 Zenith, Winnemac）
  3. *Arrowsmith*（1925，理想主义医生；取材微生物学家 Paul de Kruif；1926 普利策拒领）
  4. *Elmer Gantry*（1927，伪善福音牧师；多城被禁）
  5. *Dodsworth*（1929，上流社会的无意义人生）
  6. *It Can't Happen Here*（1935，法西斯当选总统的反乌托邦讽刺）
- 关键时间线（15–20 节点）：
  1. 1885-02-07 生于苏克中心
  2. 1891 母逝；1892 父再娶
  3. 13 岁离家出走欲当美西战争鼓手未遂
  4. 1902–03 Oberlin Academy 预科
  5. 1903 入耶鲁（1908 才毕业；休学赴 Helicon Home Colony 与巴拿马）
  6. 1908 Waterloo, Iowa 报社社论撰稿
  7. 1908–10 Carmel 文人圈；会 George Sterling；旧金山晚邮报
  8. 1910 会 Jack London；赴纽约 Frederick A. Stokes
  9. 1911 加入美国社会主义党纽约支部
  10. 1912 处女作 *Hike and the Aeroplane*（笔名 Tom Graham）
  11. 1914 首部严肃小说 *Our Mr. Wrenn*；与 Grace Hegger 结婚
  12. 1917 子 Wells 出生
  13. 1920-10-23 *Main Street* 出版——「20 世纪美国出版史最轰动事件」（传记家 Schorer 语）
  14. 1922 *Babbitt*
  15. 1925 *Arrowsmith*；1926 拒领普利策
  16. 1927 *Elmer Gantry*；1929 *Dodsworth*
  17. 1928-04-16 与 Grace 离婚；05-14 与 Dorothy Thompson 结婚
  18. 1930 诺贝尔文学奖（美国首位）；诺奖演讲《美国的文学恐惧》盛赞 Dreiser/Cather/Hemingway 并批判美国文学界
  19. 1931 公开指控 Dreiser 抄袭妻子 Thompson 著作，公开互殴；1935 *It Can't Happen Here*；1937 Austen Riggs 戒酒治疗 10 天离院
  20. 1940-10-29 子 Wells 于法国阵亡；1942 与 Thompson 离婚；1947 *Kingsblood Royal*（民权先声）；1951-01-10 卒于罗马

### 第 1 步：建立目录

- 在 `literature/presentations/20th_century/` 下创建 `Sinclair_Lewis/` 与 `images/`

### 第 2 步：复制 Makefile

- 设置 `MAIN=Sinclair_Lewis_zh`、`VIDEO_NAME=Sinclair_Lewis_zh`

### 第 3 步：收集图片

- 肖像：待下载（1930 年像或 LOC 1914 照）
- 备选插图：苏克中心童年故居博物馆（page.md 有图）

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | satire | 讽刺 | Babbitt/Elmer Gantry 的商业与宗教讽刺 | 核心页 |
| 1 | novel | 长篇小说 | 六大畅销小说的创作力 | 作品页 |
| 2 | social criticism | 社会批判 | 批判战间期美国资本主义与物质主义（page.md 明载） | 主题页 |
| 3 | dystopian fiction | 反乌托邦小说 | It Can't Happen Here（"dystopian satire" 明载） | 代表作页 |
| 4 | realism | 现实主义 | "realistic novel about small-town life" 的 Main Street 起点 | 代表作页 |

#### 4.1 入库操作（yaml 见 `MySQL/data/Sinclair_Lewis.yaml`）

- 新建 people 主记录（`name_en='Sinclair Lewis'`，qid=Q123469），`primary_occupation='writer'`、`has_social_data=1`
- 关联职业 writer(rank 0)/novelist/playwright；国籍 United States
- 5 个领域写入 `person_field`；校验同标杆第 4 步

### 第 4.5 步：社会关系梳理 + 入库

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Grace Livingston Hegger | 无向 | 1914–1928，Vogue 编辑 |
| spouse | Dorothy Thompson | 无向 | 1928–1942，国际记者与专栏作家 |
| parent-child | Wells Lewis | 无向 | 长子，二战美军中尉，1944 年法国阵亡 |
| parent-child | Michael Lewis | 无向 | 次子，舞台演员 |
| controversy | Theodore Dreiser | 无向 | 1931 年抄袭指控引发公开互殴；1944 年又为其进艺术学院奔走 |
| colleague | Jack London | 无向 | 1910 年相识；曾向其出售小说情节 |
| colleague | Upton Sinclair | 无向 | 曾在其 Helicon Home Colony 合作社工作 |
| colleague | George Sterling | 无向 | Carmel 诗人，助其获旧金山晚邮报职位 |
| colleague | H. L. Mencken | 无向 | 称其为「明尼苏达荒野的红发旋风」 |
| colleague | Paul de Kruif | 无向 | 微生物学家，Arrowsmith 的取材对象 |

#### 4.5.1 入库操作

- 以 `name_en='Sinclair Lewis'` 为中心写入 `person_relation`；缺失人物建占位（不编造 qid）
- 同名区分：**Sinclair Lewis ≠ Upton Sinclair**（两人是不同作家；Upton Sinclair 是合作社雇主）；备注写清身份

### 第 5 步：设计配色方案

- **气质**：中西部尘土金、报纸油墨黑、店面暖光
- **配色**：深墨蓝（主色，预分配 `#14324F`）+ 香槟金 `C9A227` + 四分类色
  - `badgeA` satire 讽刺 — 油墨黑 `#263238`
  - `badgeB` novel 长篇小说 — 尘土金 `#B58A3C`
  - `badgeC` social criticism 社会批判 — 砖红 `#8C4A3C`
  - `badgeD` dystopian fiction 反乌托邦 — 铁灰 `#4A5A66`

### 5.1 文学家格式硬要求

1. 封面有头像 + 细边框 + 姓名小字注。
2. 封面明示国籍；底部状态栏 `国籍 | 代表作 | 主要奖项`。
3. 必须有身份信息页（生卒、本名、国籍、出生地、教育、两段婚姻、荣誉、核心领域）。
4. 品牌口径 `OpenMathAI`；引号半角。
5. 无公式框——引文框用诺奖演讲英文原句（page.md 有载）："Our American professors like their literature clear and cold and pure and very dead."

### 第 6 步：规划幻灯片序列

```
00  OpenLiterature 项目首页
01  封面 — 主街的解剖者 / Sinclair Lewis 1885–1951 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）
03  核心贡献概览 — Main Street / Babbitt / Arrowsmith / It Can't Happen Here
04  苏克中心童年 (1885–1902) — 医生之家、孤独瘦高的少年
05  耶鲁与流浪记者岁月 (1903–1914) — Helicon、Carmel、London/Sterling
06  Main Street (1920) — 六个月 18 万册的出版史事件
07  Babbitt 与 Zenith（代表作书影 + 引文框）— Winnemac 州宇宙
08  Arrowsmith·Elmer Gantry·Dodsworth (1925–1929) — 拒领普利策
09  1930 诺贝尔奖 — 美国首位得主、Schück 提名、诺奖演讲引文框
10  It Can't Happen Here (1935) 与后期创作 — Kingsblood Royal
11  婚姻与 Dorothy Thompson — 两段婚姻、两子
12  晚年与遗产 — 罗马 1951、声誉沉浮与 2010s 复兴
13  结尾
```

### 第 7–8 步：编写源码与布局检查 【模板通用】

- 每页定义 `\newcommand{\xxxslide}`；写完即 `make` + `pdftoppm` 目检。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Lewis 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 本名 | Harry Sinclair Lewis——本名 Harry，笔名/通行名 Sinclair Lewis；勿与 Upton Sinclair 混淆 |
| 生日双值 | frontmatter 有 1885-02-07 与 1885-05-07 两值，以 infobox 1885-02-07 为准 |
| 首位口径 | 美国首位 + 美洲首位文学奖得主（page.md 双口径明载），勿只写其一 |
| 普利策 | 1926 年**拒绝** Arrowsmith 普利策（因 Main Street 1921 年落选积怨）——「拒绝」方向勿写反 |
| 死因两说 | 正文明载 advanced alcoholism；Shirer 主张心脏病发作——两说并存且一致表述，勿裁成单一死因 |
| Wells 之名 | 长子 Wells Lewis 非以 H. G. Wells 命名（母亲回忆录否认）——勿写「以威尔斯命名」 |
| Dreiser 恩怨 | 1931 抄袭指控→互殴；1944 他又力推 Dreiser 入美国艺术暨文学学会——两段都要写，勿只取一半 |
| 社会主义党 | 1911 年加入纽约支部——客观一句；政治内容不评价、不展开 |
| 引语红线 | 诺奖演讲与 Mencken 评语均有英文原文可引；其余禁编 |
| 邮票/半身像 | 「伟大美国人」邮票与 Sauk Centre 图书馆半身像（雕塑家 Kiselewski）——年份口径按 page.md |
| 二子 | Michael Lewis 是舞台演员（1930–1975）；Wells 是长子（1917–1944 阵亡）——两人身份勿互换 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| *Main Street* | 《大街》 | 1920；Gopher Prairie 小镇 |
| *Babbitt* | 《巴比特》 | 1922；Babbitt 已成英文常用名词 |
| *Arrowsmith* | 《阿罗史密斯》 | 1925；取材微生物学家 de Kruif |
| *Elmer Gantry* | 《埃尔默·甘特里》 | 1927；多城遭禁 |
| *It Can't Happen Here* | 《这事不会发生在这里》 | 1935 反乌托邦讽刺 |
| boosterism | 吹嘘主义/地方自夸 | Babbitt 讽刺对象 |
| Zenith, Winnemac | 泽尼斯，温尼马克 | 虚构州与城，多部小说共用 |
| Nobel Lecture "The American Fear of Literature" | 诺奖演讲《美国的文学恐惧》 | 1930-12-12 |

---

## 四、背景音乐选择 【预分配】

- **选定曲目**: **Timeless**
- **风格**: 沉稳 / 纪录片 / 经典
- **匹配理由**:
  - "经典" 匹配其「美国首位文学奖得主」的里程碑地位——1930 斯德哥尔摩那一刻已是文学史时间轴上的固定坐标
  - "纪录片" 匹配传记叙事结构——小镇少年→耶鲁流浪记者→六大畅销小说→诺奖→沉浮与复兴，是典型的时代观察者纪录
  - 沉稳节奏匹配 Main Street 式的全景扫视：不加评判地推过一整条街的橱窗
- **本地路径**: 曲库对应曲目拷贝至 `literature/presentations/20th_century/Sinclair_Lewis/Timeless.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Sinclair_Lewis/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/generate_20th_century_list.py` | 官方获奖理由中译 CITATION_ZH（禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `music_audio/curated_tracks.md` | BGM 曲库标签对照 |

> **开始执行。最重要的事：事实只写 page.md 明载内容；Sinclair Lewis 与 Upton Sinclair 防同名混淆。**
