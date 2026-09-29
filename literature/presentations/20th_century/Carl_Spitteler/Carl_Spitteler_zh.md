# 文学家立传提示词（OpenLiterature：Carl Spitteler）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Carl Friedrich Georg Spitteler（卡尔·施皮特勒），1919 年诺贝尔文学奖得主。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对施皮特勒，即「奥林波斯之春」：以希腊神话的宏大喻像承载对宇宙与人类的关切。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Carl Friedrich Georg Spitteler（1845–1924），德语写作的瑞士诗人，以史诗《奥林波斯之春》获 1919 年诺贝尔文学奖；作品兼有悲观与英雄气质的诗篇。
- **设计哲学**：以「神话喻现实」为核心叙事——从拒任牧职出走神学的青年，到俄国八年的家庭教师，再到以扬抑抑格六音步写就诸神之春的史诗诗人；一个把「史诗诗人使命」置于世俗职业之上的独行者。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Carl Friedrich Georg Spitteler（卡尔·弗里德里希·格奥尔格·施皮特勒，1845-04-24 ~ 1924-12-29，享年 79 岁）
- **官方获奖理由（Nobel 1919，禁止改写）**：
  > "in special appreciation of his epic, Olympian Spring"
  > （特别表彰其史诗《奥林波斯之春》）
- **气质关键词**：**奥林波斯史诗的筑造者、神话喻现实的讽喻家、瑞士良心的发声者**
- **设计母题**：**奥林波斯之春（Olympian Spring）**。其史诗「混合奇幻、自然主义、宗教与神话主题，处理人类对宇宙的关切」——以四卷结构的春之阶梯（登临 → 赫拉为新娘 → 鼎盛 → 终与转）、诸神剪影与六音步诗行的韵律线构成视觉母题。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Carl_Spitteler/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Carl_Spitteler
- **肖像**：第 0 步从 images.txt / Wikipedia REST API 下载；404 则用装饰圆占位（标注「肖像待补」）。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1845-04-24 生于 Liestal（瑞士）～ 1924-12-29 卒于 Lucerne（瑞士），享年 79 岁。德语写作，瑞士籍。
- **家庭**：父亲为政府官员，1849–1856 任**瑞士联邦财政秘书长**（Federal Secretary of the Treasury）。
- **教育**：巴塞尔文理中学（gymnasium），教师中有语文学家 **Wilhelm Wackernagel** 与历史学家 **Jacob Burckhardt**；1863 年起在苏黎世大学学法律；1865–1870 在苏黎世、海德堡与巴塞尔学神学——**牧师职位虚位以待时他选择拒绝**：他已意识到自己的使命是史诗诗人，拒入他受训多年的行当。
- **俄国岁月**：1871 年 8 月起在俄国任家庭教师（其间数段逗留芬兰），直至 1879。
- **教书与报业**：伯尔尼与 La Neuveville 的小学教师；*Der Kunstwart* 撰稿记者；*Neue Zürcher Zeitung* 编辑。**1883 年与 Marie op der Hoff 结婚——她此前是他在 Neuveville 的学生。**
- **核心作品与贡献（5 条）**：
  1. *Prometheus und Epimetheus*（1881，笔名 **Carl Felix Tandem**）——讽喻散文诗：借普罗米修斯与厄庇墨透斯的神话对峙「理想与教条」；1921 年 **Carl Gustav Jung** 在《心理类型》中对其作了长篇心理学阐释；晚年以本名重写为 *Prometheus der Dulder*（《受难的普罗米修斯》，1924）；
  2. *Olympischer Frühling*（《奥林波斯之春》，1900–1905，1910 修订，四卷：Die Auffahrt / Hera die Braut / Die Hohe Zeit / Ende und Wende）——扬抑抑格六音步的讽喻史诗，1919 诺奖核心；
  3. *Imago*（1906）——自传性中篇：以内心独白审视无意识在创造心灵与市民拘束之间的冲突；
  4. 短篇与抒情：*Friedli, der Kalderi*（1891，自述描绘「俄国现实主义」）、*Balladen*（1896）、*Glockenlieder*（1906）、*Die Mädchenfeinde*（1907，自传性童年经验）、戏剧 *Conrad der Leutnant*（1898，显出他此前对立的自然主义的影响）；
  5. 一战立场：随笔 **"Unser Schweizer Standpunkt"**（我们的瑞士立场）——反对瑞士德语多数的亲德态度。
- **荣誉**：Nobel 1919；Schiller 奖（frontmatter award_received）。
- **身后**：文稿藏于伯尔尼瑞士文学档案馆、苏黎世中央图书馆与 Liestal 诗人城市博物馆。
- **流行文化注脚**：Jung 自称其「阿尼玛」原型概念基于施皮特勒所描述的 'My Lady Soul'（唯一短语引语，Jung 转述）；2015 年 Tanja Stark 将其与 Bowie《Lady Grinning Soul》相联——**只作一句带过或省略，不入库**。
- **关键时间线（16 节点）**：
  1845-04-24 生于 Liestal → 父任联邦财政秘书长（1849–56）→ 巴塞尔文理中学（Wackernagel/Burckhardt 门下）→ 1863 苏黎世学法律 → 1865–70 神学（苏黎世/海德堡/巴塞尔）→ 拒任牧师 → 1871–79 俄国（与芬兰）家庭教师 → 1881 *Prometheus und Epimetheus*（笔名 Carl Felix Tandem）→ 1882/1883 *Extramundana*（年份两说，见陷阱表）→ 1883 与 Marie op der Hoff 结婚 → 1885 弃教从文（巴塞尔报业）→ 1891 *Friedli, der Kalderi* → 1898 *Conrad der Leutnant* → 1900–05 *Olympischer Frühling*（1910 修订）→ 1906 *Imago* → 一战《Unser Schweizer Standpunkt》→ **1919 诺贝尔文学奖** → 1924 *Prometheus der Dulder* → 1924-12-29 卒于 Lucerne。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | epic poetry | 史诗 | *Olympischer Frühling* 四卷六音步，1919 诺奖核心 | 封面、核心页 |
| 1 | prose poem | 散文诗 | *Prometheus und Epimetheus* 讽喻散文诗 | 普罗米修斯页 |
| 2 | allegory | 讽喻 | 理想与教条的对峙、*Literarische Gleichnisse* | 核心页 |
| 3 | psychological fiction | 心理小说 | *Imago*：无意识与内心独白 | 小说页 |
| 4 | lyric poetry | 抒情诗 | *Balladen*、*Glockenlieder*、*Schmetterlinge* | 抒情页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Jacob Burckhardt | 对方 → Spitteler | 巴塞尔文理中学历史学教师 |
| influence | Wilhelm Wackernagel | 对方 → Spitteler | 巴塞尔文理中学语文学教师 |
| influence | Carl Gustav Jung | Spitteler → 对方 | Jung 在《心理类型》（1921）对其 Prometheus und Epimetheus 作长篇心理学阐释，并称阿尼玛原型概念源于其 My Lady Soul |
| spouse | Marie op der Hoff | 无向 | 1883 年结婚，此前是他在 Neuveville 的学生 |

> 希腊神话人物（Prometheus 等）非历史人物不入库；Jung 关系方向是「Spitteler 影响了 Jung」；Bowie/Stark 流行文化关联不入库。

### 第 5 步：设计配色 【人物专属】

- **主色**：深海军蓝 `#1F3A5F`（奥林波斯的夜空与史诗的庄重）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgeEpic` 史诗 — 奥林波斯金 `#B8860B`
  - `badgeMyth` 神话讽喻 — 绛紫 `#6B3FA0`
  - `badgePsy` 心理小说 — 青灰 `#4A7A8C`
  - `badgeVoice` 瑞士立场 — 铁锈红 `#9E3B2B`
- **背景母题**：柔和气泡 + 「春之四阶」阶梯图形（对应史诗四卷标题），呼应设计母题。

### 第 6 步：规划幻灯片序列 【人物专属，15 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 奥林波斯之春的筑造者 / Carl Spitteler 1845–1924 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、全名、笔名、国籍、教育、职业轨迹、荣誉、核心领域）
03  核心贡献概览 — 史诗 / 讽喻散文诗 / 心理小说 / 抒情诗
04  早年：Liestal 与巴塞尔师承 (1845–1863) — 父为联邦财政秘书长、Wackernagel 与 Burckhardt 门下
05  神学与出走 (1863–1871) — 法学→神学、拒任牧职、史诗诗人使命
06  俄国家庭教师 (1871–1879) — 八年漂泊（含芬兰逗留）
07  Prometheus und Epimetheus (1881) — 笔名 Carl Felix Tandem、理想与教条的对峙（书影框①）
08  教书与报业 (1883–1890s) — 结婚、弃教从文、NZZ 编辑、Friedli/Balladen/Conrad der Leutnant
09  Olympischer Frühling (1900–1905) — 四卷六音步、1910 修订（四阶阶梯意象图式②）
10  Imago (1906) — 无意识、内心独白、创造心灵 vs 市民拘束
11  一战立场 (1914–1918) — Unser Schweizer Standpunkt：反对亲德多数
12  1919 诺贝尔奖 — 特别表彰史诗（获奖理由 EN 原文引文框）
13  Jung 与 Prometheus — 《心理类型》阐释、阿尼玛原型与 My Lady Soul
14  晚年与遗产 — Prometheus der Dulder（1924）、档案馆、结尾
```

> 文学家无公式框：第 7/9/12 页用**代表作书影框 / 四阶阶梯意象图式 / 获奖理由原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "in special appreciation of his epic, Olympian Spring"（json 引号噪声清理后引用），是「特别表彰」其史诗——1919 唯一得主，勿写共享 |
| Extramundana 年份 | page 内部两说：正文作 **1882**、作品表作 1883——提示词统一取正文 1882 并加注「页内年份两说」 |
| 笔名与重写 | 早期笔名 **Carl Felix Tandem**（1881 *Prometheus und Epimetheus*）与 1924 本名重写本 *Prometheus der Dulder* 是两个版本节点，勿混为一书 |
| 父亲职务 | Federal Secretary of the Treasury（1849–56），是**联邦财政秘书长**，勿写成"财政部长"或泛称官员 |
| 神学身份 | 受过神学训练但**拒绝牧师职位**，勿把 theologian（frontmatter 噪声）写成职业；infobox Occupation 仅 Poet |
| Jung 方向 | 是 **Jung 阐释 Spitteler**（1921《心理类型》）、Jung 的阿尼玛概念源自 Spitteler——影响方向是 Spitteler → Jung，勿写反 |
| 引语红线 | 唯一短语引语是 'My Lady Soul'（Jung 转述 Spitteler 的描述，保留转述语气）；其余禁杜撰名句 |
| 一战立场 | 「反对瑞士德语多数的亲德态度」按 page.md 客观陈述，**不作政治评价、不展开战争叙事** |
| 国籍/语言 | 瑞士籍、德语写作，勿写成德国作家；出生地 Liestal 与去世地 Lucerne 勿混 |
| Marie op der Hoff | 结婚前是他的学生——按 page.md 原文客观陈述即可，勿加演绎 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Olympischer Frühling | 《奥林波斯之春》 | 1900–05，1910 修订，四卷，诺奖理由所指 |
| Prometheus und Epimetheus | 《普罗米修斯与厄庇墨透斯》 | 1881 散文诗，笔名发表 |
| Prometheus der Dulder | 《受难的普罗米修斯》 | 1924 本名重写本 |
| Imago | 《心影》/《意象》 | 1906 自传性中篇，通行译名可从 |
| Carl Felix Tandem | 卡尔·菲利克斯·坦德姆 | 早期笔名 |
| iambic hexameter | 扬抑抑格六音步 | 史诗诗律 |
| Unser Schweizer Standpunkt | 《我们的瑞士立场》 | 一战随笔 |
| Die Mädchenfeinde | 《两个小厌女者》 | 1907，Two Little Misogynists |
| allegory | 讽喻 | 其核心手法，勿与 fable（寓言故事）混 |
| anima | 阿尼玛 | Jung 概念，源自 Spitteler 的 My Lady Soul |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken**（Alex-Productions）
- **风格标签**：觉醒 / 升腾 / 宏大
- **匹配理由**：施皮特勒一生的枢纽是「觉醒」——从神学出走、意识到史诗诗人使命的顿悟时刻；「升腾」匹配《奥林波斯之春》「Die Auffahrt（登临）」的启程意象与四卷春之阶梯；「宏大」匹配六音步史诗的规模感。
- **本地路径**：`music_audio/` 下 Alex-Productions Awaken（对照 `curated_tracks.md`）→ 复制到 `literature/presentations/20th_century/Carl_Spitteler/Awaken.wav`。

> **开始执行。每完成一步汇报；无载禁写是最高红线。**
