# 和平奖得主立传提示词（OpenPeace：George Catlett Marshall Jr.）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 George Catlett Marshall Jr.（1953 诺贝尔和平奖，马歇尔计划）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：George Catlett Marshall Jr.（乔治·卡特利特·马歇尔，1953 诺贝尔和平奖，历史上唯一获和平奖的美国陆军五星上将）。
- **设计哲学**：和平奖得主立传保留物理学家模板的两大骨架——「身份信息页」与「事业领域结构化表达」；本篇的叙事重心是**从军人到重建者**：二战「胜利的组织者」转身成为战后欧洲经济复兴的设计者与代言人。

---

## 二、背景信息 【人物专属】

- **目标人物**：George Catlett Marshall Jr.（1880-12-31 ~ 1959-10-16，享年 78 岁）
- **气质关键词**：**胜利的组织者、欧洲复兴的设计师、克己寡言的军人政治家** —— 1953 诺贝尔和平奖获奖理由：
  > "for proposing and supervising the plan for the economic recovery of Europe"（表彰他提出并主持欧洲经济复兴计划（马歇尔计划））
- **设计母题**：**废墟上的重建（reconstruction from ruins）**。以战后欧洲的城市剪影、钢筋与麦穗、援助物资与地图等高线构成视觉语言，呼应「让欧洲重新站起来」的核心事业。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/George_Marshall/page.md`
- **参考模板**：
  - 物理学家标杆提示词：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：核对本地页面，建立事实基准 【人物专属】

- ✅ 页面已抓取（含 frontmatter：QID Q151414 / 生卒 / 国籍 / 职业 / 奖项 / 教育经历）
- **事实基准（第一轮已核对，全部以 page.md 为准）**：
  - 生卒：1880-12-31 生于宾夕法尼亚州尤宁敦（Uniontown）~ 1959-10-16 逝于华盛顿特区沃尔特·里德医院（多次中风后），享年 78 岁；葬于阿灵顿国家公墓
  - 国籍：美国
  - 家庭：幼子；父 George Catlett Marshall 经营煤与焦炭生意；兄 Stuart、姐 Marie Louise；与兄因婚事长期失和（无载细节禁写）
  - 婚姻：1902-02-11 娶 Elizabeth Carter "Lily" Coles（1927-09-15 病逝，无子女）；1930-10-15 娶 Katherine Boyce Tupper Brown（Pershing 任伴郎；妻携三名前婚子女，本人无亲生子女）
  - 教育：Virginia Military Institute（VMI，1897 入学，1901 毕业，列第 15/34，获文凭非学位）；1907 Infantry-Cavalry School 五名荣誉毕业生之首；1908 Army Staff College 第一名
  - 任职主线：1902 少尉赴菲律宾 → 一战第 1 师作战助理参谋长、AEF 总部位 G-3（默兹-阿戈讷攻势关键计划人）→ 1919 起任 Pershing 副官 → 1927 步兵学校助理校长 → 1938 作战计划处/副参谋长 → 1939-09-01 任美国陆军参谋长（至 1945-11）→ 1945-12 特使赴华 → 1947-01-20 国务卿（至 1949-01-07）→ 1949 美国战争纪念碑委员会主席 + 美国红十字会会长 → 1950-09 国防部长（至 1951-09）
  - 关键荣誉：Nobel Peace Prize 1953（唯一获和平奖的美国陆军上将）；国会金质奖章 1946；Charlemagne Prize 1959；Time 年度人物 1943/1947；五星上将（General of the Army）
  - 核心事业清单：① 二战扩军——美国史上最大规模军事扩张的组织者；② 盟军欧洲/太平洋作战协调；③ 1945-46 中国调停使命；④ 国务卿任内倡导欧洲重建，1947-06-05 哈佛演说提出欧洲复兴方案；⑤ 战争纪念碑委员会：8 国 14 座战后墓园建设；⑥ 朝鲜战争初期重建国防部士气
  - 关键时间线（15–20 节点，执行者照此铺开）：1880 出生 → 1897 入 VMI → 1901 毕业 → 1902 少尉+结婚+赴菲律宾 → 1907/1908 两校第一名 → 1916 任 Bell 副官 → 1917 第 1 师赴法 → 1918 Cantigny 与默兹-阿戈讷计划 → 1919 任 Pershing 副官 → 1927 步兵学校助理校长 + 前妻病逝 → 1930 再婚 → 1938 副参谋长 → 1939-09-01 参谋长 → 1943/1947 Time 年度人物 → 1944 晋五星上将 → 1945-12 使华 → 1947 国务卿 → 1947-06-05 哈佛演说（马歇尔计划）→ 1949 因健康辞职 → 1950 国防部长 → 1951 退休 → 1953 诺贝尔和平奖 → 1953 率团出席伊丽莎白二世加冕 → 1959 逝世

### 第 1–3 步：目录 / Makefile / 图片 【模板通用】

- 在 `peace/presentations/20th_century/George_Marshall/` 下建 `images/`；Makefile 复制同项目成品并设 `MAIN=George_Marshall_zh`
- 肖像：优先用 page.md/images.txt 中的官方肖像（1946 official portrait）；下载失败用装饰圆占位并在提示词记录

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | marshall plan | 马歇尔计划 | 1947 哈佛演说提出的欧洲复兴方案，1953 和平奖核心 | 核心页 |
| 1 | post-war reconstruction | 战后重建 | 欧洲经济复兴与美国对欧承诺 | 核心页 |
| 2 | diplomacy | 外交 | 国务卿任内多边与双边斡旋 | 国务卿页 |
| 3 | military leadership | 军事领导 | 二战美国史上最大规模扩军的组织者 | 二战页 |
| 4 | international relations | 国际关系 | 使华调停、纪念碑委员会等战后事务 | 使华/晚年页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Elizabeth Carter "Lily" Coles | 无向 | 1902 结婚，1927 病逝，无子女 |
| spouse | Katherine Tupper Marshall | 无向 | 1930 结婚，Pershing 任伴郎 |
| colleague | John J. Pershing | 无向 | 一战后任其副官，1930 婚礼任伴郎 |
| colleague | Harry S. Truman | 无向 | 先后任命其为国务卿与国防部长 |
| colleague | Henry L. Stimson | 无向 | 二战陆军部长，扩军期间紧密合作 |
| colleague | Dwight D. Eisenhower | 无向 | 1945 接任其陆军参谋长职务 |
| colleague | Dean Acheson | 无向 | 国务院副手，1949 继任国务卿 |
| colleague | Robert A. Lovett | 无向 | 副国务卿，分担国务院主要工作 |
| colleague | Winston Churchill | 无向 | 二战盟军领袖，称其为「organizer of victory」 |

> 只收 page.md 明载的关系；Chiang Kai-shek / Mao Zedong / Zhou Enlai 系调停对手方，属政治敏感面，不入库，正文只作客观时间线叙述。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色（manifest 预分配，勿改）**：深酒红 `#7A1E28`（军人红/胜利与庄重）
- 辅色：诺奖香槟金 `#C9A227`
- 四分类色：`badgePlan` 马歇尔计划 — 靛蓝 `#1F3A5F`；`badgeWar` 军事领导 — 钢灰 `#37474F`；`badgeDip` 外交 — 青绿 `#0E7C7B`；`badgeMemo` 晚年与纪念 — 琥珀 `#E07B30`
- **背景母题**：柔和气泡 + 细地图等高线纹理，呼应「欧洲复兴地图」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）与国籍行。
2. 必须有身份信息页（★）：左头像 + 右信息网格（生卒、本名、国籍、出生地、教育、任职、主要荣誉、核心领域）。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 胜利的组织者 / George C. Marshall 1880–1959 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心事业概览 — 扩军 / 盟军协调 / 使华 / 马歇尔计划 / 纪念碑
04  早年：尤宁敦到 VMI (1880–1901) — 兄长的「家族之辱」论、橄榄球 All-Southern
05  早期军旅与一战 (1902–1918) — 菲律宾、Cantigny、默兹-阿戈讷
06  两次大战之间 (1919–1938) — Pershing 副官、步兵学校改革、CCC 营地
07  陆军参谋长：扩军四十倍 (1939–1945) — 「organizer of victory」、Time 年度人物
08  使华调停 (1945–1947) — 联合政府斡旋未成（只作客观叙述）
09  国务卿与马歇尔计划 (1947–1949) — 1947-06-05 哈佛演说（核心贡献页）
10  国防部长与朝鲜战争 (1950–1951) — 国会豁免案第一人
11  诺贝尔和平奖 1953 — 获奖理由 + 加冕礼上全场起立的插曲
12  家庭与晚年 — 两任妻子、Dodona Manor、园艺、纪念碑墓园
13  荣誉与认可 — 国会金质奖章 · Charlemagne Prize · 五星上将
14  遗产：马歇尔计划与战后秩序
15  结尾
```

### 第 7–8 步：Beamer 源码与布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式。
- 每写完一页 `make` 并 `pdftoppm` 目检；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Marshall 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 官方为 "for proposing and supervising the plan for the economic recovery of Europe"，勿写成「因创建联合国」或「因二战功勋」 |
| 计划署名 | 方案正式名 European Recovery Program；Truman 坚持以其命名「Marshall Plan」——他自己不设计细节，是「代言人」与「倡导者」，勿写成方案操盘手 |
| 军衔 | 五星上将 General of the Army（1944 晋升），勿写成「元帅」或「六星」 |
| 国防部长豁免 | 1947 年《国家安全法》禁止现役军人出任国防部长，Marshall 是获国会豁免第一人（2017 Mattis、2021 Austin 为第二三人），勿遗漏 |
| 中国调停 | 1945-12 至 1947-01 使华斡旋国共联合政府，双方均拒绝其方案——只作客观时间线，禁写政治评价，相关人物不入关系表 |
| 两任妻子 | 前妻 Lily Coles（1927 病逝）与 Katherine Tupper 勿混；Katherine 携三名前婚子女，Marshall 本人无亲生子女 |
| VMI 学位 | 1901 毕业获 diploma（文凭）非 degree（学位），列第 15/34；勿写「以优异成绩获学士学位」 |
| 生卒地 | 生于尤宁敦（宾州）、逝于华盛顿特区；葬阿灵顿——三地勿混 |
| 诺奖「唯一」 | 是唯一获诺贝尔和平奖的美国陆军将领（only Army general ever to receive the honor），可写；勿扩写成「唯一获和平奖的军人」 |
| 同名区分 | 父亲 George Catlett Marshall（Sr.）、本人 George Catlett Marshall Jr.；远房堂亲 Richard J. Marshall 与大法官 John Marshall 仅注「远亲」，勿与本人混淆 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Marshall Plan | 马歇尔计划 | 正式名 European Recovery Program |
| European Recovery Program | 欧洲复兴计划 | 与「马歇尔计划」同指，首现注明 |
| General of the Army | 陆军五星上将 | 非元帅 |
| Chief of Staff of the United States Army | 美国陆军参谋长 | 勿译「总参谋长」 |
| Secretary of State | 美国国务卿 | 与「国务院总理」无关 |
| Meuse-Argonne Offensive | 默兹-阿戈讷攻势 | 一战关键战役 |
| Civilian Conservation Corps | 民间资源保护队 | 大萧条时期新政机构 |
| Congressional Gold Medal | 国会金质奖章 | 1946 授予 |
| Charlemagne Prize | 查理曼奖 | 1959 年亚琛授予 |
| Dodona Manor | 多多纳庄园 | 弗吉尼亚利斯堡故居 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **PAST** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 历史感 / 深沉 / 纪录片
- **匹配理由**:
  - 「历史感」匹配其人生跨度——从美西战争后的菲律宾驻军到冷战初年的欧洲重建，几乎纵贯美国陆军现代史
  - 「深沉」匹配其克己寡言的军人气质——不居功、不著回忆录式的冷静叙事
  - 「纪录片」匹配传记叙事——扩军 → 胜利 → 调停 → 复兴计划 → 诺奖，是责任递进的纪录而非浪漫史诗
- **本地路径**: `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → 复制为 `presentations/20th_century/George_Marshall/PAST.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/George_Marshall/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `peace/prompt_manifest.json` | batch=peace-batch-11（主色/BGM 预分配） |
| `MySQL/data/George_Marshall.yaml` | 研究领域+社会关系入库文件 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
