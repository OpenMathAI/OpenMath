# 和平奖得主立传提示词（OpenPeace：Alva Myrdal / 阿尔娃·米达尔）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Alva Myrdal（1982 诺贝尔和平奖，裁军运动领袖、瑞典社会改革家）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth G. Wilson 提示词 + Beamer 立传骨架；和平奖侧沿用「身份信息页 + 领域结构化」骨架。
- **本实例**：Alva Myrdal（本姓 Reimer，1902-01-31 ~ 1986-02-01，享年 84 岁）。
- **设计哲学**：和平奖得主立传与科学家立传的核心差异，在于「事业领域」以**社会改革与外交斡旋**呈现；本篇双主线——「瑞典福利国家的缔造者」与「日内瓦裁军谈判的无阵营领袖」，两者交汇于 1982 诺奖。

---

## 二、背景信息 【人物专属】

- **目标人物**：Alva Myrdal（née Reimer，1902-01-31 生于乌普萨拉 ~ 1986-02-01 逝于瑞典丹德吕德 Danderyd，享年 84 岁，卒于 84 岁生日次日）
- **官方获奖理由**（照抄名录 `OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写；与 Alfonso García Robles 共享同句）：
  > 英文原文（nobel_peace_citations.json，清理引注噪声后）："for their work for disarmament and nuclear and weapon-free zones."
  > 中译：表彰他们在裁军以及无核武器区与无武器区方面的工作
- **气质关键词**：**福利国家的总设计师、日内瓦的无阵营旗手、理性必须胜利的信徒**。
- **设计母题**：**棋盘与圆桌（negotiation geometry）**——她在两大超级强权之间以不结盟阵营施压；视觉母题取「日内瓦谈判桌的几何 / 双极力量间的中立蓝」。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Alva_Myrdal/page.md`（Wikipedia 全文 + frontmatter，QID Q152437）。
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 和平奖项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（已核对 page.md，禁止杜撰） 【人物专属】

- 生卒：1902-01-31 生于乌普萨拉 ～ 1986-02-01 逝于丹德吕德，享年 84 岁（卒于生日次日）。
- 国籍：瑞典（名录口径）。
- 家庭：父 Albert Reimer（社会主义者、现代自由派），母 Lowa Jonsson；弟妹四人 Ruth/Folke/May/Stig，童年随家迁居 Eskilstuna/Älvsjö/斯德哥尔摩。
- 婚姻与子女：1924 与 **Gunnar Myrdal** 教授结婚；三子女——Jan Myrdal（1927 生）、Sissela Bok（1934 生）、Kaj Fölster（1936 生）。丈夫获 1974 诺贝尔经济学奖，夫妻是史上第四对诺奖夫妇、**第一对各自独立获奖**的夫妇（区别于科学家夫妻共享奖）。
- 教育：乌普萨拉出身，斯德哥尔摩 1924 获理学学士；学术方向为心理学与家庭社会学；1929 夫妇同赴美国任 Rockefeller Fellows（深造心理学/教育学/社会学），后赴日内瓦研究两次大战间欧洲人口衰退。
- 任职/政治：瑞典社会民主工人党资深成员；1934 与丈夫合著《Kris i befolkningsfrågan》（人口问题的危机）；1935 出版《Urban Children》；1936 共同创办国家教育研讨所（National Educational Seminar）并亲任教师培训师；1937 与建筑师 Sven Markelius 共同设计斯德哥尔摩合作住宅 Collective House；1937 加入「增加妇女代表权委员会」；1941 在美出版《Nation and Family》；1949 出任联合国福利政策部门负责人；1950–1955 任联合国教科文组织（UNESCO）社会科学部门主席——**联合国此类高级职位的首位女性**；1955–1956 出使新德里/仰光/科伦坡（驻印度、缅甸、斯里兰卡使节）；1956 与英国社会学家 Viola Klein 合著《Women's Two Roles: Home and Work》；1962 当选瑞典议会议员（Riksdag）；1962–1973 任瑞典驻日内瓦联合国裁军会议代表；1966 任斯德哥尔摩国际和平研究所（SIPRI）理事会首任主席；1967–1973 任裁军事务协商内阁大臣；1976 出版《The Game of Disarmament》；1983 平息 AF-striden（Adolf Fredrik 音乐学校之争）。
- 关键荣誉：West German Peace Prize 1970（与丈夫共同）；Wateler Peace Prize 1973；KTH Great Prize 1975；Monismanien Prize 1976；Albert Einstein Peace Prize 1980；Jawaharlal Nehru Award 1981；**Nobel Peace Prize 1982**（与 Alfonso García Robles 共享）；美国哲学学会会员 1982；12 个荣誉博士（Mount Holyoke 1950 → Linköping 1982，页面有完整清单）。
- 核心事业清单：
  1. 1930s 瑞典福利国家设计与人口政策（《人口问题的危机》）。
  2. 学前教育体系改革（1935《Urban Children》、1936 创办国家教育研讨所）。
  3. 妇女政治代表权与职业家庭两全（《Women's Two Roles》1956）。
  4. 联合国体系开创者（1949 福利政策、1950 UNESCO 社科首位女性主席）。
  5. 1962–1973 日内瓦裁军谈判：不结盟阵营领袖，向美苏施压实质性裁军。
  6. SIPRI 首任理事会主席 + 《The Game of Disarmament》(1976)。
- 关键时间线（18 节点）：1902 生于乌普萨拉 → 1924 理学学士 + 与 Gunnar 结婚 → 1929 Rockefeller Fellow 赴美 → 赴日内瓦研究人口问题 → 1934《人口问题的危机》→ 1935《Urban Children》→ 1936 创办国家教育研讨所 → 1937 Collective House + 妇女代表权委员会 → 1941《Nation and Family》→ 1949 联合国福利政策负责人 → 1950–55 UNESCO 社科主席 → 1955–56 驻新德里/仰光/科伦坡 → 1956《Women's Two Roles》→ 1962 入议会 + 日内瓦裁军代表 → 1966 SIPRI 首任主席 → 1967 裁军协商内阁大臣 → 1976《The Game of Disarmament》→ 1982 诺贝尔和平奖 → 1986-02-01 卒。
- 可用引语（仅限 page.md 载有原文者）：页面载「radical」为夫妇自评政治取向的用语；1981 广播访谈集标题 «Förnuftet måste segra!»（理性必须胜利）可用作气质句（书名形式，非引语）。

### 第 4 步：事业领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | disarmament | 裁军 | 1962–73 日内瓦谈判、不结盟阵营领袖，1982 诺奖核心 | 核心页 |
| 1 | social policy | 社会政策 | 瑞典福利国家设计、人口政策 | 核心页 |
| 2 | preschool education | 学前教育 | 1935《Urban Children》、1936 创办研讨所 | 早年页 |
| 3 | family sociology | 家庭社会学 | 学术出身与《人口问题的危机》合著 | 早年页 |
| 4 | women's rights | 女性权利 | 妇女代表权委员会、《Women's Two Roles》 | 核心页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Gunnar Myrdal | 无向 | 1924 结婚，1974 诺贝尔经济学奖得主，首对各自独立获奖的诺奖夫妇 |
| co-honored | Alfonso García Robles | 无向 | 1982 诺贝尔和平奖共同得主 |
| parent-child | Jan Myrdal | 无向 | 长子，1927 生 |
| parent-child | Sissela Bok | 无向 | 长女，1934 生，传记作者 |
| parent-child | Kaj Fölster | 无向 | 次女，1936 生 |
| colleague | Viola Klein | 无向 | 1956 合著 Women's Two Roles |
| colleague | Sven Markelius | 无向 | 1937 共同设计斯德哥尔摩 Collective House |

> 入库：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Alva_Myrdal.yaml`；校验 has_social_data=1、fields=5、relations=7。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色**：`#8C1515`（manifest 预分配，深绯红——社会民主党红与谈判桌上的旗帜），勿改。
- **辅助**：诺奖香槟金 `C9A227` + 四分类色：
  - `badgeA` 裁军 — 深绯 `#8C1515`
  - `badgeB` 社会政策 — 皇家蓝 `#2A4B7C`
  - `badgeC` 学前教育 — 暖金 `#C9A227`
  - `badgeD` 女性权利 — 紫红 `#7A2E5D`
- **背景母题**：双极对峙的几何（两簇大圆分踞左右、中央留白通道，隐喻两大强权间的不结盟空间）。

### 第 6 步：规划幻灯片序列（12 页规划）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 福利国家与裁军谈判桌 / Alva Myrdal 1902–1986 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍/家庭/教育/任职/荣誉/核心事业）
03  核心事业概览 — 福利国家设计 / 学前教育 / 联合国体系 / 日内瓦裁军
04  早年：乌普萨拉的 Reimer 家 (1902–1924) — 寒门长女、斯德哥尔摩理学学士
05  与 Gunnar：学术双星 (1924–1941) — Rockefeller Fellow、人口危机、Collective House
06  福利国家与学前教育 (1934–1937) — 人口问题的危机、国家教育研讨所
07  走向世界 (1949–1962) — 联合国福利政策、UNESCO 首位女性社科主席、南亚使节
08  日内瓦裁军谈判 (1962–1973)（核心贡献页）— 不结盟阵营领袖、向美苏施压
09  SIPRI 与 The Game of Disarmament — 1966 首任主席、1976 著作
10  荣誉与认可 — Einstein Peace 1980 · Nobel 1982 · 12 个荣誉博士
11  遗产：无核武器区的先声 — 与 García Robles 的共享奖
12  结尾
```

### 第 7–8 步：版式要点 + 本篇专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 共享奖口径 | 1982 与 Alfonso García Robles 共享，理由同一句 "for their work for disarmament and nuclear and weapon-free zones."；两篇理由须一致，勿各自改写 |
| 丈夫奖项 | Gunnar Myrdal 获 1974 **诺贝尔经济学奖**（瑞典央行纪念阿尔弗雷德·诺贝尔经济学奖），勿写成「和平奖」或泛称「诺贝尔奖」；「史上第四对诺奖夫妇、首对各自独立获奖」口径照页面 |
| 姓氏口径 | 本姓 Reimer；婚后 Myrdal；提示词/封面用 Alva Myrdal |
| 生日口径 | 1902-01-31 生、1986-02-01 卒（卒于生日次日，享年 84），勿写 85 |
| UNESCO 职位 | 「联合国此类高级职位的首位女性」限定在 page.md 原文语境（福利政策/教科文社科主席），勿扩大为「联合国首位女性高官」 |
| 议会年份 | 1962 当选议员与 1962 起任日内瓦裁军代表同年，勿错位成 1961/1963 |
| Monismanien Prize | 1976 得主（她在 1983 又平息同名音乐学校之争——AF-striden 是 1983 事件，与奖无关联） |
| 无载禁写 | 博士学位（页面仅理学学士，勿升格为博士）、具体导师姓名页面无载不入库、Jan Myrdal 政治立场禁写 |
| 政治敏感 | 冷战、美苏批评只作裁军谈判的客观背景记录，不加入阵营评价 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| disarmament | 裁军 | 1982 诺奖核心词 |
| nuclear and weapon-free zones | 无核武器区与无武器区 | 理由原文两个并列区 |
| Riksdag | 瑞典议会 | 勿译国会 |
| SIPRI | 斯德哥尔摩国际和平研究所 | 首任理事会主席 |
| UNESCO | 联合国教科文组织 | 社会科学部门主席 |
| Collective House | 集体住宅（合作住宅） | 1937 与 Markelius 合作 |
| Rockefeller Fellows | 洛克菲勒基金会研究员 | 1929 夫妇同赴美 |
| Kris i befolkningsfrågan | 人口问题的危机 | 1934 瑞典语书名 |
| The Game of Disarmament | 《裁军的博弈》 | 1976 著作 |
| AF-striden | AF 之争（音乐学校之争） | 1983，非其获奖事项 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 辽阔 / 沉静 / 长程视野
- **匹配理由**: 北欧的辽阔海面气质匹配其瑞典底色；裁军谈判是跨越二十年的长程博弈，沉静而有纵深的曲式正合「理性必须胜利」的克制信念。
- **本地路径**: `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` → `presentations/20th_century/Alva_Myrdal/SEA.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Alva_Myrdal/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录与官方获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节母本） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：事实全部锚定 page.md，无载禁写；共享奖理由与 García Robles 篇一致。**

---

## 六、第 1–3 步补充（模板通用） 【模板通用骨架】

### 第 1 步：建立目录

- 在 `peace/presentations/20th_century/` 下创建 `Alva_Myrdal/` 与 `images/`（提示词本文件已就位）。

### 第 2 步：复制 Makefile

- 复制同目录已立传成品的 `Makefile`（或标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`），设置 `MAIN=Alva_Myrdal_zh`、`VIDEO_NAME=Alva_Myrdal_zh`。

### 第 3 步：收集图片 【人物专属】

- **肖像**：`pages/Alva_Myrdal/images.txt` 仅载 1980 年前后与丈夫的合影 `Alva_and_Gunnar_Myrdal_at_desk_(edited).jpg`——无单人真照。处理次序：①Wikipedia REST API `page/summary/Alva_Myrdal` 查 infobox 1968 年单人照原图名，Commons `Special:FilePath/<文件名>?width=600` 下载 500px；②失败则用夫妻合影（图注必须注明「与丈夫 Gunnar Myrdal」，不得冒充单人照）；③仍不可用则装饰圆占位。curl 加 `-A "Mozilla/5.0"`，`file` 验证。
- **插图备选**：集体住宅 Collective House、SIPRI 大楼等页面无图，用文字版式，勿外抓。
- 404/HTML 时换文件名或用 REST API 回退。

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像/合影 + `draw=coveraccent!50` 细边框 + 姓名小字注（合影须注两人姓名）。
2. **封面有国籍**：顶部副标题或底部状态栏明示 Sweden；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心事业之前；左头像 + 右信息网格，至少含生卒/本姓/国籍/家庭/教育/任职/主要荣誉/核心事业，事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`；共享封面 `\input` 继承，子 deck 不重复。

---

## 七、执行清单（Checklist） 【模板通用】

1. 通读 `pages/Alva_Myrdal/page.md` 全文（本文件第 0 步已核对，执行时复核即可）。
2. 建目录 + 复制 Makefile + 下载肖像/合影（`file` 验证）。
3. 复制 BGM：`music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` → 目录内 `SEA.wav`。
4. 按 §4 领域表 + §4.5 关系表核对已入库 DB 字段（fields=5 / relations=7，勿改）。
5. 编写 Beamer 源码（每页 `\newcommand{\xxxslide}`，骨架参照标杆成品 tex）。
6. 编译循环：0 error、vbox ≤ 10pt、hbox ≤ 50pt；每写完一页即 make + `pdftoppm` 目检。
7. 页数对账：按 §6 规划逐帧核对（缺帧/合并帧都要能对上页数）。
8. 引语逐条核对 §0 白名单；无原文一律转述（本篇几乎无直接引语，以书名/称号形式呈现）。
9. 陷阱表逐条自查（共享奖理由、丈夫经济学奖口径、UNESCO「首位」限定）。
10. `make images && make video` 出片后，提示词回写 Review 备注（肖像来源/事实修正）。
