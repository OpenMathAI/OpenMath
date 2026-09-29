# OpenPeace 人物立传提示词（实例：Theodore Roosevelt）

> **本文件是 OpenPeace 项目（诺贝尔和平奖得主立传）的人物立传提示词**，
> 以西奥多·罗斯福（Theodore Roosevelt，1906 诺贝尔和平奖，美国第 26 任总统）为完整实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Theodore Roosevelt Jr.（美国第 26 任总统）。
- **设计哲学**：政治家立传的特殊性在于「和平奖只是其一生的一个切面」——叙事必须以和平调停为主线（诺奖理由），其余成就（进步主义改革、保护主义、海军战略）作为背景支撑，**不得喧宾夺主，也不得做任何当代政治评价**。

---

## 二、背景信息 【人物专属】

- **目标人物**：Theodore Roosevelt Jr.（1858-10-27 纽约市 ~ 1919-01-06 萨加莫尔山，享年 60 岁）
- **气质关键词**：**质朴生活的信奉者、朴茨茅斯的调停人、第一位非欧洲诺奖得主**
- **诺奖年份与官方获奖理由**：1906 年诺贝尔和平奖（独得）
  > 中文获奖理由（照抄名录 `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写）：
  > **「表彰他促成当时世界上两大强国日本与俄国之间血腥战争的终结」**
- **设计母题**：**天平上的橄榄枝与巨棒（olive branch & big stick）**——1906 年《Puck》漫画「The Man of the Hour」所描绘的「1898 战士 / 1905 调停人」双重形象，视觉上以「战争与和平的天平」贯穿
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Theodore_Roosevelt/page.md`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准（人物专属，第一轮已核对）

- 生卒：1858-10-27 生于纽约市东 20 街 28 号 ~ 1919-01-06 凌晨逝于长岛萨加莫尔山（Sagamore Hill，肺栓塞，睡梦中），享年 60 岁；葬于 Oyster Bay 的 Youngs Memorial Cemetery
- 国籍：美国；政党：共和党（1880–1912、1916–1919），1912–1916 进步党（Bull Moose）
- 家庭：父 Theodore Roosevelt Sr.（商人）、母 Martha Stewart Bulloch；姐 Anna（Bamie）、弟 Elliott、妹 Corinne
- 婚姻：1880 娶 Alice Hathaway Lee（1884-02-14 妻与母同日去世，日记写「The light has gone out of my life」）；1886-12-02 伦敦娶青梅竹马 Edith Kermit Carow
- 子女（6）：Alice（长女，1884）、Theodore III（1887）、Kermit（1889）、Ethel（1891）、Archibald（1894）、Quentin（1897，1918-07-14 法驾机阵亡）
- 教育：家庭学校 → 1876 入哈佛（1880 毕业 Phi Beta Kappa，22/177，A.B. magna cum laude）→ 哥伦比亚法学院（辍学从政）
- 任职履历（含年份）：纽约州议员（1882–1884，多数党领袖）→ 达科他牧场主（1883–1887）→ 美国文官委员会（1889–1895）→ 纽约市警察委员会主席（1895–1897）→ 海军助理部长（1897–1898）→ 莽骑兵上校（1898，圣胡安山）→ 纽约州州长（1899–1900）→ 美国第 25 任副总统（1901-03 至 09）→ 第 26 任总统（1901-09-14 继任至 1909，42 岁就职为最年轻在任总统；1904 大选 336:140 完整任期）
- 关键荣誉：1906 诺贝尔和平奖（**首位非欧洲诺贝尔奖得主**）；荣誉勋章（2001 追授，唯一获此勋章的总统）；拉什莫尔山四位总统之一
- 核心事业清单（以和平外交为纲）：
  1. **日俄战争调停**（1904–05 双方均请求斡旋，1905 朴茨茅斯和会成功，因此获 1906 和平奖）
  2. 摩洛哥危机调停（召集阿尔赫西拉斯会议，避免法德开战）
  3. 1902–03 委内瑞拉危机导向海牙仲裁
  4. 1907–08 大白舰队环球航行与 Root–Takahira 协定（美日缓和）
  5. 1908 庚子赔款用于留美奖学金（Boxer Indemnity Scholarships）
  6. 国内：Square Deal、反托拉斯（44 起诉讼）、自然保护（国家公园/森林/纪念碑）
- 和平观与晚年：1910 诺贝尔演讲主张「League of Peace」（有执行力的和平联盟、美国参与）；1914 提出「World League for the Peace of Righteousness」；1918 年称此为最可行的国联方案；1912 组进步党参选失败（密尔沃基遇刺后仍演说 90 分钟，弹头终身留体内）；1919-01-06 去世
- 关键时间线（15–20 节点）：1858 生于纽约 → 1876 入哈佛 → 1880 毕业+首次结婚 → 1882 《1812 年海战史》出版+州议员 → 1884 妻母同日去世、赴达科他 → 1886 竞选纽约市长失败（27%）+ 娶 Edith → 1889 文官委员会 → 1895 纽约市警察委员会主席 → 1897 海军助理部长 → 1898 莽骑兵与圣胡安山 → 1899–1900 纽约州州长 → 1901-03 副总统 → 1901-09-14 麦金莱遇刺后继任总统 → 1904 大选大胜 → 1905 朴茨茅斯和会 → 1906 获诺贝尔和平奖（首位非欧洲得主）→ 1907–09 大白舰队环球航行 → 1908 扶持 Taft 接班 → 1909–10 非洲狩猎科学考察 → 1912 进步党竞选与遇刺演说 → 1913–14 亚马逊 River of Doubt 考察 → 1918 幼子 Quentin 阵亡 → 1919-01-06 去世

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Theodore_Roosevelt/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品的 Makefile，设置 `MAIN=Theodore_Roosevelt_zh`、`VIDEO_NAME=Theodore_Roosevelt_zh`

### 第 3 步：收集图片 【人物专属】

- page.md infobox 用 1904 年肖像（`Roosevelt in 1904`）；备选：1903 年 John Singer Sargent 白宫官方画像、1898 莽骑兵照、1905 年「The Man of the Hour」漫画（ warrior/peacemaker 对照）
- 经 Commons Special:FilePath 取 500px

### 第 4 步：事业领域梳理 + 入库（fields，与 yaml 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace mediation | 和平调停 | 日俄朴茨茅斯调停，1906 诺奖核心 | 调停页 |
| 1 | diplomacy | 外交 | 摩洛哥危机、委内瑞拉仲裁、大白舰队外交 | 外交页 |
| 2 | progressive politics | 进步主义政治 | Square Deal、反托拉斯、联邦监管 | 内政页 |
| 3 | conservation | 自然保护 | 国家公园/森林/纪念碑体系 | 保护页 |
| 4 | naval history | 海军史与海权 | 《1812 年海战史》、海军扩张 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Alice Hathaway Lee | 无向 | 1880 结婚，1884-02-14 与婆母同日去世 |
| spouse | Edith Kermit Carow | 无向 | 1886-12-02 伦敦结婚 |
| parent-child | Theodore Roosevelt Sr. | 无向 | 父，商人 |
| parent-child | Martha Bulloch Roosevelt | 无向 | 母，1884-02-14 同日去世 |
| parent-child | Alice Roosevelt Longworth | 无向 | 长女（1884） |
| parent-child | Theodore Roosevelt III | 无向 | 子（1887） |
| parent-child | Kermit Roosevelt | 无向 | 子（1889） |
| parent-child | Ethel Roosevelt Derby | 无向 | 女（1891） |
| parent-child | Archibald Roosevelt | 无向 | 子（1894） |
| parent-child | Quentin Roosevelt | 无向 | 幼子（1897），1918 一战阵亡 |
| colleague | William McKinley | 无向 | 1901 副总统搭档，麦金莱遇刺后继任总统 |
| colleague | William Howard Taft | 无向 | 战争部长与继任总统 |
| rival | William Howard Taft | 无向 | 1912 共和党分裂，双方竞逐提名与总统 |
| rival | Woodrow Wilson | 无向 | 1912 总统竞选对手；一战期间公开论战 |
| colleague | Leonard Wood | 无向 | 1898 共同组建莽骑兵兵团 |
| colleague | Henry Cabot Lodge | 无向 | 挚友与政治盟友，屡次推举其出任要职 |

- Booker T. Washington（白宫晚宴）、Jane Addams（1912 为进步党助选）等 page.md 明载互动**不入库**（无稳定关系类型，防误标），只在正文叙述

### 第 5 步：配色方案（manifest 预分配，勿改）

- **主色**：`#4E342E`（深褐——勇士与荒野气质）
- **辅色**：诺奖香槟金 `C9A227`
- badgeA–D：badgeA 和平调停（`#1F6B4E`）、badgeB 外交（`#1F3A5F`）、badgeC 进步主义（`#B08A2E`）、badgeD 保护与海军（`#8C3B2E`）

### 第 6 步：规划幻灯片序列（12–15 页）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 1906 诺贝尔和平奖 · 西奥多·罗斯福 1858–1919 + 四色 badge + 右上肖像
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/教育/任职履历/家庭/荣誉/核心领域）
03  纽约与荒野 (1858–1886) — 哮喘、《1812 年海战史》、达科他牧场、1884 双重丧礼
04  崛起：从警局到海军部 (1889–1898) — 文官改革、警队整顿、海军助理部长
05  莽骑兵与圣胡安山 (1898) — 「我一生中伟大的一天」
06  从州长到白宫 (1899–1901) — 州长改革、副总统、麦金莱遇刺
07  Square Deal 总统 (1901–1905) — 反托拉斯、保护主义、1904 大选
08  朴茨茅斯调停 (1905)（核心页）— 日俄双方斡旋、和会成功
09  1906 诺贝尔和平奖 — 获奖理由 + 首位非欧洲得主
10  外交全景 (1904–1909) — 阿尔赫西拉斯、委内瑞拉仲裁、大白舰队、庚款留学
11  和平观：League of Peace (1910) — 诺贝尔演讲、1914 国联构想
12  进步党与最后一战 (1912–1918) — Bull Moose、密尔沃基遇刺演说、Quentin 阵亡
13  遗产 — 拉什莫尔山、荣誉勋章、「现代总统制的设计师」
14  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 诺奖理由口径 | 官方理由只讲「促成日俄战争终结」；「首位非欧洲诺贝尔奖得主」是 page.md 明文补充事实，勿写进理由句 |
| 调停细节 | page.md 明文「双方均请求斡旋、和会在新罕布什尔朴茨茅斯」；「秘密偏向日本」为 page.md 明载，客观转述即可 |
| 最年轻总统 | 42 岁继任为「最年轻的在任总统」（不是最年轻当选总统），勿混 |
| 两任 Spouse | Alice（1880–1884）与 Edith（1886–）须分别成行；Edith 小节标题 page.md 原文误作 widowerhood，实际是 second marriage，按事实写 |
| rival 关系 | Taft 同时有 colleague（内阁/继任）与 rival（1912 分裂）两行，note 分清，勿合并成一行 |
| 死因 | 1919-01-06 肺栓塞（pulmonary embolism），睡梦中逝于萨加莫尔山——勿写「心脏病」 |
| 名言红线 | 「Speak softly and carry a big stick」page.md 明载可引；未载出处的排比名言禁造 |
| 引语红线 | 正文所引段落（ diary、Round-Robin、Nobel address 1910）page.md 有英文原文；中文语境转述并保留关键英文短语 |
| 政治敏感红线 | 涉种族问题（Brownsville、white supremacy 言论）、帝国主义、对 Wilson 的攻击等只作 page.md 明载的客观事实记录，**不加任何评价性语句**，不展开立场叙事 |
| 同名区分 | Franklin D. Roosevelt（库内 4982）是堂侄一辈的另一位总统，本篇**禁写**任何「叔侄关系」（page.md 本页未载）；库内检索时勿误匹配 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Treaty of Portsmouth | 朴茨茅斯条约/和会 | 1905，新罕布什尔 |
| Rough Riders | 莽骑兵 | 第 1 志愿骑兵团 |
| Square Deal | 公平交易（ Square Deal） | 保留英文名并附译 |
| Bull Moose Party | 雄鹿党/进步党 | 1912 |
| Big stick ideology | 巨棒主义 | 1901-09-02 首次公开 |
| Great White Fleet | 大白舰队 | 1907–09 环球航行 |
| Roosevelt Corollary | 罗斯福推论 | 对门罗主义的补充，1904 |
| Boxer Indemnity Scholarship | 庚子赔款奖学金 | 1908，40 年资助中国学生留美 |
| League of Peace | 和平联盟 | 1910 诺贝尔演讲主张 |
| Medal of Honor | 荣誉勋章 | 2001 追授，唯一总统 |

---

## 四、背景音乐 ✅（manifest 预分配，勿改）

- **选定曲目**: **The Flow of Time** — Alex-Productions
- **匹配理由**: 时间流转的史诗感匹配从 1858 纽约到 1919 萨加莫尔山的六十年跨度；「调停者的暮色」气质贴合其从战士到和平缔造者的形象转换
- **本地路径**: `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`
- **时长**: 以 ffmpeg `-shortest` 对齐页数

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Theodore_Roosevelt/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 0–11 节结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `MySQL/data/Theodore_Roosevelt.yaml` | fields + relations 入库母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：政治敏感内容只作客观事实记录。**
