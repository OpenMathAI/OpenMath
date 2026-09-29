# 和平奖得主立传提示词（OpenPeace · Jane Addams）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Jane Addams（1931 诺贝尔和平奖，美国社会工作奠基人、Hull House 创办人）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。
> 标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库下的 peace 侧）。
- **本实例**：Laura Jane Addams（简·亚当斯），1931 诺贝尔和平奖得主（与 Nicholas Murray Butler 共享），美国首位获和平奖的女性。
- **设计哲学**：Addams 的事业横跨**睦邻运动、社会工作奠基、女性参政与和平运动**四条线，立传以 Hull House 为空间锚点、以 1915 海牙妇女大会与 WILPF 为和平主线。模板骨架沿用「身份信息页 + 领域结构化表达」，领域表换为「事业领域表」。

---

## 二、背景信息 【人物专属】

- **目标人物**：Laura Jane Addams（1860-09-06 ~ 1935-05-21，享年 74 岁）
- **气质关键词**：**Hull House 的缔造者、美国社会工作奠基人、和平织造（peaceweaving）的哲学家** —— 1931 诺贝尔和平奖获奖理由（与 Butler 共享同一句）：
  > "for their assiduous effort to revive the ideal of peace and to rekindle the spirit of peace in their own nation and in the whole of mankind."（表彰他们不懈努力重振和平理想，在本国乃至全人类心中重新点燃和平精神）
- **设计母题**：**织造和平（peaceweaving）**。Addams 的和平哲学被概括为 peaceweaving——经纬交叠、由关系织成布匹；视觉母题可用「织机与经纬线」「多色丝线汇成和平鸽」，呼应「人际关系织就和平」。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Jane_Addams/page.md`（Wikipedia 全文 + frontmatter，已抓取；长文 581 行，分节核对）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1860-09-06 生于伊利诺伊州 Cedarville（本名 Laura Jane Addams）~ 1935-05-21 逝于芝加哥 Passavant 医院（腹部梗阻手术后），享年 74 岁；安葬于故乡 Cedarville。⚠️ frontmatter 生卒均有噪声值（生 1860-01-01；卒 1935-01-01/05-22），一律以 infobox 正文 **09-06 / 05-21** 为准。
- 国籍：美国（英裔移民后裔，家世可溯至殖民地宾夕法尼亚）。
- 家庭：八子女中最幼；父 John H. Addams（伊利诺伊州参议员 1855–1870、共和党州创始成员、Freeport 第二国民银行行长）；母 Sarah（née Weber）1863 年怀第九胎时去世；继母 Anna Hosteler Haldeman；姐 Alice Haldeman；侄 James Weber Linn（芝加哥大学英语教师）。
- 教育：Rockford Female Seminary（今 Rockford University），1881 届毕业致辞代表（valedictorian）、Phi Beta Kappa；1881–82 就读宾州女子医学院一年，因脊椎手术与精神崩溃未获学位；1883–85 欧洲游历。
- 健康背景：四岁患脊柱结核（Pott's disease），脊柱侧弯、终身跛行；1926 心脏病发作，1931 确诊癌症（本人未被告知）。
- 任职与活动轨迹（全部 page.md 明载）：
  1. 1889 与 Ellen Gates Starr 共同创办芝加哥 Hull House（美国最著名的睦邻住宅之一），高峰期每周约 2000 人来访，最终发展为 13 栋建筑群；
  2. 1894 成为芝加哥第 19 选区首位女性卫生督察（垃圾之战）；
  3. 全国妇女参政协会（NAWSA）副主席；
  4. 1910 获耶鲁大学荣誉文学硕士学位——耶鲁首位获荣誉学位的女性；
  5. 1912 帮助创建进步党并支持老罗斯福竞选；
  6. 1915-01 当选 Woman's Peace Party 全国主席；1915-04-28~30 主持海牙国际妇女大会（约 1200 名代表、12 国），并率团走访交战国；
  7. 1919 苏黎世会议当选 International Committee of Women for a Permanent Peace 主席——后发展为 WILPF（妇女国际和平自由联盟），任主席至终；
  8. 1920 参与共同创立美国公民自由联盟（ACLU）；
  9. 1931 与 Nicholas Murray Butler 共享诺贝尔和平奖，是美国首位和平奖女性得主，奖金份额捐予 WILPF。
- 核心事业清单：
  1. Hull House 睦邻运动（社会服务 + 社区艺术 + 社会调查）；
  2. 美国社会工作职业的奠基（被称 "Mother of Social Work"）；
  3. 社会学领域：Hull-House Maps and Papers（1893）、美国社会学会创始会员（1905）、American Journal of Sociology 1896–1914 五篇论文、与芝加哥学派共事；
  4. 女性参政与「公民持家」（civic housekeeping）论述；
  5. 和平运动：Woman's Peace Party → 海牙大会 → WILPF；反战立场在 1917 参战后遭《纽约时报》等抨击、1915 卡内基音乐厅演讲被嘘，DAR 开除其会籍，而 Coolidge 与中产舆论在 1920s 支持其禁毒气与废战努力；
  6. 著述：*Twenty Years at Hull-House* (1910)、*Newer Ideals of Peace* (1907)、*A New Conscience and an Ancient Evil* (1912)、*Peace and Bread in Time of War*、*The Second Twenty Years at Hull-House* (1930)、*Women at The Hague*（与 Balch/Hamilton 合著）。
- 关键时间线（16 节点）：1860 生于 Cedarville → 1863 母逝 → 1864 脊柱结核 → 1881 Rockford 毕业 + 父逝 → 1881–82 女子医学院 → 1883–85 欧游 → 1886 受洗 → 1887 再访欧洲读 Toynbee Hall → 1889 创办 Hull House → 1893 Hull-House Maps and Papers → 1894 首位女卫生督察 → 1907 *Newer Ideals of Peace* → 1910 耶鲁荣誉硕士 → 1912 进步党 → 1915-01 Woman's Peace Party 主席 → 1915-04 海牙大会 → 1919 WILPF 前身主席 → 1920 ACLU 共同创立 → 1926 心脏病 → 1931 诺贝尔和平奖 → 1934 Mary Rozet Smith 逝 → 1935-05-21 逝世。

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | social work | 社会工作 | 美国社会工作职业奠基人 | 核心页 |
| 1 | settlement movement | 睦邻运动 | Hull House (1889) | Hull House 页 |
| 2 | peace activism | 和平运动 | 海牙大会、WILPF 主席 | 和平页 |
| 3 | sociology | 社会学 | 芝加哥学派共创者、应用社会学 | 社会学页 |
| 4 | women's suffrage | 女性参政 | NAWSA 副主席、civic housekeeping | 妇女页 |

- 入库：`person_field` 5 条（rank 0–4），与下方 yaml `fields` 完全一致。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 一致】

> 只收 page.md 明载关系；metadata-only 一律不入库。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | John H. Addams | 无向 | 父亲，伊利诺伊州参议员与实业家 |
| colleague | Ellen Gates Starr | 无向 | Rockford 同学，1889 共同创办 Hull House，早年伴侣 |
| colleague | Mary Rozet Smith | 无向 | 三十余年伴侣与 Hull House 主要资助人（至 1934） |
| colleague | Emily Greene Balch | 无向 | 1915 海牙大会同席代表、*Women at The Hague* 合著者（Balch 系 1946 和平奖得主） |
| colleague | Alice Hamilton | 无向 | 1915 海牙大会同席代表、*Women at The Hague* 合著者 |
| colleague | John Dewey | 无向 | 长期深谈重释民主的哲学家、社会改革并肩者 |
| colleague | George Herbert Mead | 无向 | 社会改革合作者（女权/禁童工/1910 成衣工罢工调停） |
| influence | Leo Tolstoy | 无向 | 托尔斯泰著作与基督教早期社群是其核心思想来源 |
| co-honored | Nicholas Murray Butler | 无向 | 1931 诺贝尔和平奖共同得主 |

- 说明：Smith/Starr 与 Addams 未有法定婚姻，用 colleague + note 客观记录（page.md 原文 romantic partner）；Balch 用其链接页全名 Emily Greene Balch；DAR 开除、报刊攻讦等属事件不入关系。
- 入库：`person_relation` 9 条；对手方 Tolstoy 用库内 'Leo Tolstoy'(4903)、Dewey 用 'John Dewey'(5661)、Hamilton 用 'Alice Hamilton'(5364)；Butler 本批并行入库，按 manifest name 字段形式匹配。

### 第 5 步：设计配色方案 【人物专属】

- **主色**：`#2A4B7C`（睦邻深蓝——芝加哥湖畔的沉稳与公共精神，manifest 预分配，勿改）
- **辅色**：诺奖香槟金 `#C9A227`
- badgeA–D 四分类色（事业领域）：
  - `badgeA` 和平运动 — 鸽青 `#2E7D6E`
  - `badgeB` 社会工作 — 砖红 `#A3552E`（Hull House 砖墙）
  - `badgeC` 女性参政 — 紫藤 `#6A4A8C`（参政运动紫）
  - `badgeD` 社会学 — 靛蓝 `#3E5F8C`
- **背景母题**：经纬细线与织物质理色块，呼应「织造和平」。

### 第 6 步：规划幻灯片序列 【人物专属，共 16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 织造和平 / Jane Addams 1860–1935 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 本名、生卒、家庭、教育、荣誉、核心事业
03  核心事业概览 — Hull House / 社会工作 / 和平运动 / 女性参政 / 社会学
04  早年：Cedarville 的小女儿 (1860–1881) — 母逝、脊柱结核、Rockford 致辞代表
05  医学折翼与欧游 (1881–1888) — 女子医学院、Toynbee Hall 的启迪
06  创办 Hull House (1889) — 与 Starr、移民社区、13 栋建筑群（核心页）
07  Hull House 的调查与改革 — 卫生督察、垃圾之战、社会调查方法论
08  公民持家与女性参政 — civic housekeeping、NAWSA 副主席、进步党 1912
09  社会学的奠基者之一 — 芝加哥学派、Dewey/Mead、应用社会学
10  1915： Woman's Peace Party 与海牙大会 — 1200 名代表、走访交战国（和平主线页）
11  WILPF 与战时批判 — 1919 苏黎世、舆论攻击与 Coolidge 支持（客观记录）
12  1931 诺贝尔和平奖 — 与 Butler 共享、美国首位和平奖女性、奖金捐 WILPF
13  和平哲学家：peaceweaving — 正和平/负和平、Shields-Soeters 概括
14  晚年与遗产 (1926–1935) — ACLU、著作、"Mother of Social Work"
15  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 版式：每页 `\newcommand{\xxxslide}` 定义；`make` 后 `pdftoppm` 截图查溢出；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距。
- **Addams 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 日期噪声 | frontmatter 生卒各有多值（1860-01-01、1935-01-01、1935-05-22 均为噪声），取 infobox **1860-09-06 / 1935-05-21** |
| 共享理由 | 1931 与 Butler 共享同一句理由（"their"），勿写成单独理由；Addams 是**美国首位**和平奖女性得主（page.md 明载可写），但勿写「全球第几位」 |
| Smith/Starr 定性 | 用 colleague + note 客观记录伴侣关系；二人非法律婚姻，**禁用 spouse 类型** |
| Tolstoy 影响方向 | 托尔斯泰是思想来源（influence），勿写「合作者」 |
| 优生学内容 | page.md 有 Eugenics 节（支持优生学、与美国社会卫生协会），如需提及只作客观事实一句，**不加评价、不展开**，避免喧宾夺主 |
| 政治敏感 | 反战遭攻讦、DAR 开除、进步党、ACLU 等均按 page.md 客观记录，不站队、不加评价 |
| 组织职衔 | Woman's Peace Party 是「全国主席」；NAWSA 是「副主席」，两个头衔勿混 |
| 引语红线 | Balch 1915 日记评语、Addams 书信（"I miss you dreadfully..."）为 page.md 原文可引；其余禁编引语 |
| 母亲亡故 | 1863 年 Sarah Addams 亡故，勿写「Addams 幼年丧父」；父 1881 年因阑尾炎猝逝 |
| 无载禁写 | 获奖致辞内容、Stockholm 领奖行程、与 Butler 的私人交往等 page.md 未载一律不写 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| settlement house | 睦邻住宅 | 与「安置房」区分 |
| Hull House | 赫尔馆 | 惯译，勿译「赫尔之家」 |
| peaceweaving | 和平织造 | Shields-Soeters 概括的哲学概念 |
| civic housekeeping | 公民持家 | Addams 自创论述 |
| WILPF | 妇女国际和平自由联盟 | 1919 前身为 International Committee of Women for a Permanent Peace |
| Woman's Peace Party | 妇女和平党 | 1915-01 全国主席 |
| International Congress of Women | 国际妇女大会 | 1915 海牙 |
| negative/positive peace | 消极和平/积极和平 | 和平理论框架 |
| Pott's disease | 脊柱结核（波特病） | 童年疾患 |
| Toynbee Hall | 汤因比馆 | 伦敦世界首座睦邻住宅 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 激昂 / 张力 / 战斗感
- **匹配理由**：Addams 在举国主战氛围中逆流而行——被嘘下台、被报业围剿、被组织除名，仍把和平织成运动；"Savage" 的张力与斗志匹配其「以柔韧对抗时代狂潮」的一生。
- **本地路径**：`music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav` → 复制到 `peace/presentations/20th_century/Jane_Addams/Savage.wav`
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Jane_Addams/page.md` | 本地 Wikipedia 正文 + frontmatter（事实基准，581 行长文） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（一~五节） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID→name_en 匹配） |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
> **红线：无载禁写；引语仅限 page.md 原文；政治内容只作客观记录。**
