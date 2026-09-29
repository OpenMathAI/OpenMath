# 文学家立传提示词（OpenLiterature：Toni Morrison）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Toni Morrison（托妮·莫里森），1993 年诺贝尔文学奖得主，美国非裔小说家、编辑、教授。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对莫里森，即「最蓝的眼睛与宠儿之魂」：以抒情而带痛感的笔触为美国现实被压抑的一面赋形，以编辑席与讲台双线改写美国文学的正典边界；种族创痕客观呈现，**不作政治评价**。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Toni Morrison（本名 Chloe Anthony Wofford，1931–2019），美国小说家、编辑（兰登书屋首位非裔女性小说高级编辑）、普林斯顿大学人文讲席教授；1993 年诺贝尔文学奖得主（**任何国籍黑人女性中的首位**），1988 年普利策小说奖（《宠儿》）得主。
- **设计哲学**：以「最蓝的眼睛与宠儿之魂」为核心叙事——《最蓝的眼睛》写渴望蓝眼睛的黑人女孩，《宠儿》让被杀女婴的亡魂还家；「书写的语言」是诺奖演说的核心命题。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Toni Morrison（托妮·莫里森，本名 Chloe Ardelia Wofford，1931-02-18 ~ 2019-08-05，享年 88 岁）
- **官方获奖理由（Nobel 1993，禁止改写）**：
  > "who in novels characterized by visionary force and poetic import, gives life to an essential aspect of American reality"
  > （表彰其小说以先知般的力量与诗意内涵，赋予美国现实的一个本质面向以生命）
- **气质关键词**：**非裔记忆的赋形者、正典的改写者、编辑席上的推手**
- **设计母题**：**最蓝的眼睛与宠儿之魂（bluest eye & beloved's ghost）**——蓝眼睛的凝视构成视觉母题 A；门廊烛影与亡魂剪影构成视觉母题 B；Princeton Morrison Hall 与 Princeton 档案馆为结尾元素。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Toni_Morrison/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Toni_Morrison
- **肖像**：第 0 步优先用 page.md 内嵌图 1998 照或《最蓝的眼睛》初版作者肖像照（1970 dust jacket）；404 则用装饰圆占位。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1931-02-18 生于俄亥俄州克利夫兰以西的洛雷恩（Lorain），本名 Chloe Ardelia Wofford ～ 2019-08-05 卒于纽约布朗克斯 Montefiore 医疗中心（肺炎并发症），享年 88 岁；2019-11-21 圣约翰大教堂追思会（Oprah Winfrey、Angela Davis、Ondaatje、Ta-Nehisi Coates 等致悼词）。英语写作。
- **家世与童年**：工人阶级黑人家庭，四子女中排第二；母 Ramah（Willis）生于阿拉巴马州格林维尔， devout 的非洲卫理公会（AME）教徒；父 George Wofford 生于佐治亚州卡茨维尔，约 15 岁时目睹两位非裔商人被私刑处死（莫里森引述："He never told us that he'd seen bodies..."）——随后北迁洛雷恩，做焊工等杂工；莫里森约两岁时房东因缴不起房租纵火烧屋，全家以大笑回应她所谓的「怪诞的恶」；父母以民间故事、鬼故事与歌谣传递传承与语言；童年爱读 Jane Austen 与 Leo Tolstoy。
- **名字由来**：12 岁入天主教并领洗名 Anthony（取自帕多瓦圣安东尼），由此得昵称 Toni；洛雷恩高中辩论队/年刊/戏剧社成员。
- **霍华德与康奈尔**：1949 入霍华德大学（初读戏剧，师从名戏剧教师 Anne Cooke Reid 与 Owen Dodson；在校首次遭遇种族隔离餐馆与公交；与 Alain Locke、Sterling Brown 等「哈莱姆文艺复兴」一代共事；随 Howard Players 南方巡演——「塑造一生的经历」）；1953 英文毕业（辅修古典学）；1955 康奈尔大学美国文学硕士（论文题 "Virginia Woolf's and William Faulkner's treatment of the alienated"）。
- **教职**：1955–1957 得克萨斯南方大学（休斯顿）教英文 → 1957 回霍华德大学教英文七年（其间结识牙买加建筑师 Harold Morrison）→ 1984 获纽约州立大学奥尔巴尼分校 Albert Schweitzer 讲席 → 1986–88 巴德学院访问教授 → **1989–2006 普林斯顿大学 Robert F. Goheen 人文讲席**（创办 Princeton Atelier；2017 年 Princeton 将 West College 命名为 Morrison Hall）→ 1997–2003 康奈尔 Andrew D. White 常驻教授。
- **编辑生涯**：1965 婚变与幼子出生后入兰登书屋教材部 L. W. Singer（锡拉丘兹）→ 两年后调纽约总部，**成为虚构小说部首位非裔女性高级编辑**；把黑人文学带入主流：首两本书含《当代非洲文学》（1972，收 Wole Soyinka、Chinua Achebe 与南非剧作家 Athol Fugard）；扶持 Toni Cade Bambara、Angela Davis、Huey Newton、Gayl Jones（后者为其发掘）等新一代非裔作家；促成穆罕默德·阿里自传《 The Greatest: My Own Story》（1975）；主持《黑人之书》（*The Black Book*, 1974）——奴隶时代至 1920 年代黑人生活影像文档选（《宠儿》灵感源 Margaret Garner 的故事即在此发现）；1983 年辞职专事写作（Nyack 哈德逊河船屋）。
- **成名与「宠儿」三部曲**：霍华德大学非正式写作小组中提交蓝眼睛女孩短篇 → 发展为首作《最蓝的眼睛》（*The Bluest Eye*, 1970，39 岁；每天凌晨 4 点写作、独自抚养两个孩子；NYT 书评 John Leonard 赞其「精准到成诗的散文……又是历史、社会学、民俗、噩梦与音乐」）；《苏拉》（1973，国家图书奖提名）；《所罗门之歌》（1977，自 1940 年赖特《土生子》以来首部成为月度读书会主选的黑人作家小说，获全国书评人协会奖）；《柏油孩子》（1981）；《宠儿》（1987——取材 Margaret Garner 真实故事，写被杀女婴亡魂还家；畅销 25 周；落选 NBA/NBCC 后 48 位黑人评论家与作家联名抗议（含 Maya Angelou），两个月后获**普利策小说奖**与 Anisfield-Wolf 奖）；三部曲之二《爵士乐》（1992，哈莱姆文艺复兴背景）；之三《天堂》（1997，全黑人小镇）；2006 年《宠儿》被《纽约时报书评》选为「25 年来美国小说最佳作品」。
- **批评与讲演**：1992 首部文学批评《在黑暗中游戏：白与文学想象》（*Playing in the Dark*，1990 哈佛 Massey 讲座——论爱伦·坡、霍桑、梅尔维尔、凯瑟、海明威作品中「非白人非洲式在场」的建构）；1996 杰斐逊讲席（NEH 人文最高荣誉，讲题 "The Future of Time"）；2016 哈佛 Norton 诗歌讲席（成书《他者之源》2017）。
- **诺奖**：1993 年获诺贝尔文学奖，为**任何国籍黑人女性中的首位**；获奖演说名句："We die. That may be the meaning of life. But we do language. That may be the measure of our lives."（可引原文）；诺奖演说以老盲妇与年轻人的寓言谈「讲故事的力量」。
- **奖项**（择要）：1977 NBCC 奖 → 1988 普利策/美国图书奖/Anisfield-Wolf → 1993 诺贝尔 → 1996 国家图书基金会美国文学杰出贡献奖章 → 2000 国家人文奖章 → 2010 法兰西军团军官勋章 → 2012 总统自由勋章（奥巴马颁发）→ 2016 PEN/索尔·贝娄奖 → 2020 入选全国妇女名人堂（身后）。
- **家庭**：1958 嫁牙买加建筑师 Harold Morrison，1964 离婚（怀次子时）；长子 Harold Ford（1961 生）；次子 Slade Kevin Morrison（1965 生，画家兼音乐人，与母亲合写 7 部童书；**2010-12-22 因胰腺癌去世，45 岁**——莫里森因此停写《归乡》数月，后完成并献给儿子）；单身抚养两子多年。
- **跨艺术**：与 André Previn 合作歌曲套曲 *Honey and Rue*（1992，Kathleen Battle 首演）与 *Four Songs*（1994）；为 Jessye Norman 写 *Sweet Talk* 与 *Spirits In the Well*（Richard Danielpour 谱曲）；2002 完成《 Margaret Garner》歌剧脚本（Danielpour 谱曲，2005-05-07 底特律歌剧院首演）；2011 与 Peter Sellars、Rokia Traoré 合作《苔丝狄蒙娜》（重读《奥赛罗》）；1986 首部戏剧《梦见埃米特》（Emmett Till 私刑题材）。
- **政治与女性主义立场（客观简述，不作评价）**：1998 明言拒绝女权主义标签——「我一生所做的一切都是扩展表达而非封闭它」；区分 womanism 与白人女权；1987 与 2015 多次声明毕生写作拒斥「白人凝视」；1998 克林顿弹劾评论（"our first Black President" 语出莫里森，2008 年她自释语境）；2008 为奥巴马背书；2016 年大选后撰《哀悼白人性》（*The New Yorker*）——**政治言论只按 page.md 客观转述其立场，不展开政治叙事、不作评价**。
- **核心作品与贡献（5 条）**：
  1. 《宠儿》三部曲——《宠儿》（1987 普利策）+《爵士乐》（1992）+《天堂》（1997）：爱与非裔历史的连环书写；
  2. 《最蓝的眼睛》（1970）——渴望蓝眼睛的黑人女孩，处女作；
  3. 《所罗门之歌》（1977）——Milkman Dead 的寻根之旅，NBCC 奖；
  4. 编辑与推手——兰登书屋首位非裔女性小说高级编辑，《黑人之书》与新一代非裔作家的扶持；
  5. 《在黑暗中游戏》（1992）与「白人凝视」批评体系；2019 遗稿文选《自我尊重之源》。
- **关键时间线（18 节点）**：1931 生于洛雷恩 → 童年民间故事与 Austen/Tolstoy → 12 岁领洗名 Anthony → 1949 入霍华德 → 1953 英文毕业 → 1955 康奈尔硕士 → 1955–57 得克萨斯南方 → 1957 回霍华德任教 → 1958 嫁 Harold Morrison → 1961 长子生 → 1964 离婚 → 1965 入兰登书屋 → 1969–70 成为首任非裔女性小说高级编辑/《最蓝的眼睛》出版 → 1974 《黑人之书》→ 1977 《所罗门之歌》→ 1983 辞职专事写作 → 1987 《宠儿》→ 1988 普利策 → **1993 诺贝尔文学奖** → 1996 杰斐逊讲席 → 2002 《 Margaret Garner》歌剧脚本 → 2006 普林斯顿退休 → 2010 Slade 病逝 → 2012 总统自由勋章 → 2019-08-05 卒于布朗克斯。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | african-american literature | 非裔美国文学 | 全部核心作品的主战场 | 核心页 |
| 1 | literary fiction | 文学小说 | infobox Genre；抒情笔法与非线性叙事 | 书影页 |
| 2 | historical fiction | 历史小说 | 宠儿三部曲与奴隶记忆的还魂 | 宠儿页 |
| 3 | literary criticism | 文学批评 | 《在黑暗中游戏》：白人凝视与非洲式在场 | 批评页 |
| 4 | children's literature | 儿童文学 | 与 Slade 合写 7 部童书 | 童书页 |

#### 4.1 入库操作

- 新建/更新 `people` 主记录（`name_en` 用 page.md frontmatter 的 name，`qid` 以分批文件为准），设置 `primary_occupation='writer'`、`has_social_data=1`（`has_biography` 待 Beamer 立传后置 1）
- 关联职业 `writer`（rank 0）与 page.md 明载副职业（poet/novelist/playwright/essayist 等，1–3 行），国籍按 Nobel 官方口径
- 将上表 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`（fields 应为 5）

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Harold Morrison | 无向 | 牙买加建筑师，1958 年结婚，1964 年离婚 |
| parent-child | George Wofford | 无向 | 父亲，佐治亚出生焊工，少年目睹私刑创伤 |
| parent-child | Ramah Willis | 无向 | 母亲，阿拉巴马出身，非洲卫理公会教徒 |
| parent-child | Harold Ford Morrison | 无向 | 长子，1961 年生，纪录片《他者的家园》素材提供者 |
| parent-child | Slade Morrison | 无向 | 次子，画家兼音乐人，合写 7 部童书，2010 年病逝 |
| advisor-student | Anne Cooke Reid | Morrison ← 师（对方） | 霍华德大学戏剧教师 |
| advisor-student | Owen Dodson | Morrison ← 师（对方） | 霍华德大学戏剧教师 |
| colleague | Alain Locke | 无向 | 霍华德共事的哈莱姆文艺复兴关键人物 |
| colleague | Sterling Brown | 无向 | 霍华德共事的哈莱姆文艺复兴诗人学者 |
| colleague | Robert Gottlieb | 无向 | Knopf 主编，编辑其小说中除一部外的全部作品 |
| colleague | Toni Cade Bambara | 无向 | 其任编辑时扶持的作家 |
| colleague | Gayl Jones | 无向 | 其任编辑时发掘的作家 |
| colleague | André Previn | 无向 | 歌曲套曲 Honey and Rue 与 Four Songs 合作者 |

> Margaret Garner 为《宠儿》灵感来源（历史人物）**非关系不入库**；Wole Soyinka/Chinua Achebe/Athol Fugard 为其编辑书籍的入选作者**不入库**；Angela Davis/Huey Newton 为其出版书籍作者（政治人物）**不入库**；Maya Angelou 仅联名抗议信同署**不入库**；Oprah Winfrey 为影视改编与书选推手（媒体关系）**不入库**；Muhammad Ali 为其促成的自传作者**不入库**；Woolf/Faulkner 为硕士论文研究对象**不入库**；Zadie Smith 为身后致敬者**不入库**。

#### 4.5.1 入库操作

- 以 `name_en` 为中心写入 `person_relation`（yaml 路径见分批文件 `MySQL/data/Toni_Morrison.yaml`，引擎 `MySQL/seed_person.py`，幂等按 QID → name_en 匹配）
- 方向约定：`advisor-student` 有向（direction: advisor=对方是导师 / student=对方是学生）；`spouse` / `parent-child` / `colleague` / `influence` 无向（seed 自动 from<to 归一，yaml 勿写 direction）
- 对手方无库内记录时建 stub（不编造 qid，name_en 用规范全名）；库内已有同名记录按名幂等匹配并回填 QID；note 含 `: ` 须整体单引号包裹
- 校验：`SELECT COUNT(*) FROM person_relation WHERE from_id=<id> OR to_id=<id>`

- 校验本人物 relations 应为 13 行

### 第 5 步：设计配色 【人物专属】

- **主色**：藏蓝 `#14324F`（深水与记忆的底色）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgeBlue` 最蓝的眼睛 — 孔雀蓝 `#1B6B7A`
  - `badgeBeloved` 宠儿/记忆 — 深紫红 `#5B2A46`
  - `badgeEditor` 编辑/正典 — 烟灰紫 `#5E548E`
  - `badgeSong` 所罗门之歌 — 铜金 `#A8763E`
- **背景母题**：柔和气泡 + 门廊烛光光晕（记忆母题），批评页转为书页横纹。

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有肖像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明「肖像待补」。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 代表作 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧肖像 + 右侧信息网格，含至少：本名/笔名演变、生卒（含享年）、国籍、婚姻子女、教育与讲席任职、主要荣誉、核心领域。事实取自 page.md infobox 与正文，不得杜撰。
4. **文学家替代公式框**：代表作书影框 / 名句引文框 / 意象图式三选一——核心贡献页与诺奖页至少各出现一处；引语只允许使用第 7–8 步「引语白名单」内的条目，其余禁杜撰。
5. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenLiterature`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，16 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 最蓝的眼睛与宠儿之魂 / Toni Morrison 1931–2019 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（本名 Chloe Ardelia Wofford、生卒、国籍、编辑/讲席、荣誉、核心领域）
03  核心贡献概览 — 非裔文学正典 / 编辑推手 / 批评体系 / 跨艺术
04  洛雷恩童年 (1931–1949) — 工人家庭、民间故事、Austen 与 Tolstoy、领洗名 Toni（引文框①：获奖理由 EN 原文）
05  霍华德与康奈尔 (1949–1957) — 戏剧起点、Reid 与 Dodson、Locke 与 Brown、南方巡演、硕士论文
06  编辑席上的推手 (1965–1983) — 兰登书屋首位非裔女性小说高级编辑、《黑人之书》、扶持一代作家
07  最蓝的眼睛 (1970) — 凌晨四点的写作、John Leonard 书评（书影框②）
08  所罗门之歌 (1977) — Milkman Dead、NBCC 奖、月度读书会
09  宠儿 (1987) — Margaret Garner 的真事、48 位作家抗议与普利策（意象图式③：烛影亡魂）
10  1993 诺贝尔奖 — 任何国籍黑人女性首位 + "We do language" 演说引文
11  在黑暗中游戏 (1992) — 白人凝视与非洲式在场、杰斐逊讲席（批评页）
12  三部曲之后 (1997–2015) — 天堂/爱/仁慈/归乡/上帝帮助孩子、Margaret Garner 歌剧、童书与 Slade
13  白宫与讲台 — 总统自由勋章、普林斯顿 Atelier、Morrison Hall
14  遗产 — 2020 全国妇女名人堂、Morrison Society、邮票与 Toni Morrison Day
15  结尾
```

> 文学家无公式框：第 4/7/9/10 页用**代表作书影框 / 意象图式 / 获奖理由原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "who in novels characterized by visionary force and poetic import, gives life to an essential aspect of American reality"，逐词照引禁止改写 |
| 「第一」口径 | 「兰登书屋虚构小说部首位非裔女性（高级）编辑」与「诺奖首位任何国籍黑人女性」——两处 first 均照 page.md 原文口径，勿互相替换或扩大成「美国首位」 |
| 三人名多形态 | 本名 Chloe Ardelia Wofford；笔名源洗名 Anthony → 昵称 Toni + 夫姓 Morrison；Chloe Anthony Wofford 为正文另一表述——身份页以 frontmatter 本名为主、笔名演变一行讲清 |
| 政治内容红线 | 私刑家史、民权语境、克林顿评论、奥巴马背书、2016 大选文章：**只按 page.md 客观转述立场，不展开政治叙事、不作评价**；"our first Black President" 须带她 2008 年的自释语境 |
| 女性主义口径 | 她明确**拒绝**女权主义标签并区分 womanism——勿写成「黑人女权主义作家」；学界（Barbara Smith 等）对其作品的女权主义解读注明为批评界观点 |
| 48 位作家联名 | 抗议的是 NBA/NBCC **落选**（《宠儿》），随后获普利策——因果链按「抗议 → 两月后获奖」并陈，勿写成「抗议使其获奖」 |
| Slade 与《归乡》 | Slade 2010-12-22 病逝时《归乡》写到一半，她停笔数月后完成并献子——时间线勿压缩 |
| 论文与研究对象 | Woolf/Faulkner 是她硕士论文的研究对象，**勿写成「受其影响」入库** |
| 引语白名单 | ① 获奖理由官方原句；② "We die... But we do language..."（获奖演说，page 明载）；③ "He never told us that he'd seen bodies..."（其引述父亲）；④ John Leonard 书评句——其余禁杜撰 |
| 书名斜体 | 全部作品名在 tex 中用 `\textit{}`；《宠儿》既指 1987 小说又指 1998 电影与 2005 歌剧，年份随写防混 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| The Bluest Eye | 《最蓝的眼睛》 | 1970 处女作 |
| Sula | 《苏拉》 | 1973 |
| Song of Solomon | 《所罗门之歌》 | 1977，NBCC 奖 |
| Beloved | 《宠儿》 | 1987，普利策奖 |
| Jazz | 《爵士乐》 | 1992，三部曲之二 |
| Paradise | 《天堂》 | 1997，三部曲之三 |
| Playing in the Dark | 《在黑暗中游戏》 | 1992，白人凝视批评 |
| The Black Book | 《黑人之书》 | 1974，其主编的影像文档选 |
| Margaret Garner | 玛格丽特·加纳 | 《宠儿》灵感来源与同名歌剧 |
| Random House | 兰登书屋 | 首位非裔女性小说高级编辑 |
| Howard University | 霍华德大学 | 1949–1953 就读，1957–1964 任教 |
| Princeton Atelier | 普林斯顿工坊 | 1994 年代创办，学生与艺术家共创 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**SEA**（Alex-Productions）
- **风格标签**：辽阔 / 深沉 / 涌动
- **匹配理由**：莫里森的文字始终有深海般的涌动——记忆的暗流、亡魂的潮汐、被压抑者的浮出水面——「辽阔」匹配其横跨奴隶时代至今日的百年叙事画幅；「深沉」匹配《宠儿》还魂场景的重量；「涌动」匹配《爵士乐》的律动与「先知般的力量」。藏蓝主色配 SEA 的深海气质，与「宠儿之魂」的母题同构。
- **本地路径**：`music_audio/` 下 Alex-Productions SEA（对照 `curated_tracks.md`）→ 复制到 `literature/presentations/20th_century/Toni_Morrison/SEA.wav`。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Toni_Morrison/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Toni_Morrison/images.txt` | 内嵌图片 URL 清单（肖像第 0 步下载） |
| `literature/generate_20th_century_list.py` | 名录与获奖理由 CITATION_ZH（EN 原文+中译，禁止改写） |
| `literature/prompt_batches_lit.json` | 分批清单（qid/year/color/bgm 预分配） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `literature/presentations/cover/` | 统一封面 `\input` 模板 |
| `MySQL/data/Toni_Morrison.yaml` | 人物 fields + relations 入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等，按 QID → name_en 匹配） |

> **开始执行。每完成一步汇报；无载禁写与政治内容红线是最高红线。**
