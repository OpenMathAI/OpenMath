# 和平奖得主立传提示词（OpenPeace 实例：Henri La Fontaine）

> 本文件是 OpenPeace 项目的「诺贝尔和平奖得主立传提示词」，以 Henri La Fontaine（1913 诺贝尔和平奖，比利时法学家/和平运动领袖）为完整实例。
> 结构对齐 OpenPhysicist 标杆 `Kenneth_G_Wilson_zh.md`（一~五节）。凡标注【模板通用】可复用，【人物专属】按本人物执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Henri Marie La Fontaine（亨利·拉方丹），1913 诺贝尔和平奖得主，国际和平局主席。
- **设计哲学**：和平奖立传的「组织型」样本——La Fontaine 的贡献在于把散落各国的和平组织连成网络（国际和平局、国际协会联盟、文献学建制），立传以「和平国际主义的组织者」为叙事骨架，身份信息页必做。

---

## 二、背景信息 【人物专属】

- **目标人物**：Henri Marie La Fontaine（1854-04-22 ~ 1943-05-14，享年 89 岁）
- **气质关键词**：**欧洲和平运动的领袖、目录学与文献学的先行者、女性权利的早期倡导者**
- **官方获奖理由（英文原文照抄 nobel_peace_citations.json）**：
  > "for his unparalleled contribution to the organization of peaceful internationalism"
  - **中译（照抄名录 OpenPeace_20th_Century_Nobel_Laureates.md，禁止改写）**：表彰他对和平国际主义组织建设的无与伦比的贡献
  - ★ 1913 为独享年份；Wikipedia 导语另载诺奖理由转述 "he was the effective leader of the peace movement in Europe"——官方理由句以 citations json 为准
- **设计母题**：**索引卡与地球（index card & globe）**。La Fontaine 与 Otlet 的目录学革命（后来的万维网精神先声）+ 和平组织的国际网络——视觉语言宜用索引卡片、地球经纬、连线网络。
- **本地数据源**：`peace/presentations/pages/20th_century/Henri_La_Fontaine/page.md`（Wikipedia 全文 + frontmatter，事实基准唯一来源）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1854-04-22 生于布鲁塞尔 ~ 1943-05-14 卒于布鲁塞尔（享年 89）
- 国籍：比利时
- 家庭：妹 Léonie La Fontaine——姐弟同为女性权利与选举权的早期倡导者；配偶/子女 page.md 无载，禁写
- 共济会成员：布鲁塞尔 Les Amis Philanthropes 会员（page.md 明载，客观陈述）
- 教育：布鲁塞尔自由大学（Free University of Brussels，今分裂为 ULB 与 VUB）法学
- 任职时间线：
  - 1877 取得律师资格，以国际法权威立身
  - 1893 布鲁塞尔自由大学国际法教授
  - 1895 当选比利时参议员（社会党），1919–1932 任参议院副议长
  - 1907–1943 任国际和平局（International Peace Bureau）主席直至去世
  - 1919 比利时巴黎和会代表团成员；1920–21 国际联盟大会成员
- 关键荣誉：Nobel Peace Prize 1913
- 核心事业清单：
  1. 国际和平局：早期关注，推动 1899/1907 两次海牙和平会议之实现；1907 起任主席 36 年
  2. 与 Paul Otlet 共创国际协会联盟（Union of International Associations, 1907）
  3. 与 Paul Otlet 共创国际目录学会（Institut International de Bibliographie，后成为 FID）
  4. 创办 Centre Intellectuel Mondial（后并入国联知识合作组织）；倡设世界学校/世界大学/世界议会
  5. 1890 与妹妹 Léonie 共创比利时女性权利同盟（Belgian League for the Rights of Women）
  6. 一战后提议组建国际法院并列名候选人（Choate、Root、Eliot、White 等）
- 著作：《公共工程承包人的权利与义务》（1885）、《伪造论》（1888）、《国际判例集》（Pasicrisie internationale, 1902）、《和平与仲裁文献目录》（1904）；创办期刊 *La Vie Internationale*
- 关键时间线（15–20 节点）：1854 生于布鲁塞尔 → 布鲁塞尔自由大学法学 → 1877 律师资格 → 1890 共创女性权利同盟 → 1893 国际法教授 → 1895 参议员 → 1899/1907 海牙会议（和平局推动） → 1902 《国际判例集》 → 1904 《和平与仲裁文献目录》 → 1907 共创 UIA → 1907 任国际和平局主席 → 1913 获诺贝尔和平奖 → 一战→战后倡设国际法院并列名候选人 → 1919 巴黎和会代表团 → 1920–21 国联大会 → 创办 Centre Intellectuel Mondial → 1937 世界文献大会（与 Otlet） → 1943-05-14 卒于布鲁塞尔

### 第 4 步：研究领域/事业领域表 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international law | 国际法 | 布鲁塞尔自由大学教授、判例集作者 | 早年页 |
| 1 | peace movement | 和平运动 | 国际和平局主席 36 年，诺奖核心 | 和平局页 |
| 2 | bibliography | 目录学 | 国际目录学会共创、文献目录 | 文献页 |
| 3 | documentation science | 文献学 | UIA 与万国文献大会 | 文献页 |
| 4 | international relations | 国际关系 | 国联大会、巴黎和会 | 战后页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Paul Otlet | 无向 | 1907 共创 UIA，共创国际目录学会（IIB） |
| colleague | Léonie La Fontaine | 无向 | 妹妹，1890 共创比利时女性权利同盟 |
| founder | Union of International Associations | 无向 | 1907 与 Otlet 共创 |
| founder | Institut International de Bibliographie | 无向 | 与 Otlet 共创，后成 FID |
| founder | Centre Intellectuel Mondial | 无向 | 后并入国联知识合作组织 |
| colleague | International Peace Bureau | 无向 | 1907–1943 任主席（1882 创立，非创始人） |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色**：绛红 `#7E1E23`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeLAW` 国际法 — 靛蓝 `#3F5E9E`
  - `badgeMOV` 和平运动 — 青绿 `#0E7C7B`
  - `badgeBIB` 目录学/文献学 — 琥珀 `#C9821F`
  - `badgeIRL` 国际关系 — 玫瑰 `#B5495B`
- **背景母题**：索引卡网格底纹 + 连线圆点，呼应「把世界的知识与世界和平组织编目相连」

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 和平国际主义的组织者 / Henri La Fontaine 1854–1943 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/国籍/教育/任职/荣誉/核心领域）
03  核心贡献概览 — 国际和平局 / UIA / 目录学 / 女性权利
04  布鲁塞尔律师 (1854–1893) — 自由大学、1877 律师、国际法权威
05  参议员与女性权利 (1890–1919) — 1890 同盟、1893 教授、1895 参议员、1919 副议长
06  国际和平局 (1882–1943) — 海牙会议的推手、1907 起任主席 36 年
07  目录学革命：与 Otlet 同行 (1895–1937) — IIB、UIA、La Vie Internationale、1937 万国文献大会
08  诺贝尔和平奖 (1913) — 理由句原文呈现、欧洲和平运动领袖
09  战后秩序 (1919–1932) — 巴黎和会、国联大会、Centre Intellectuel Mondial、世界法院倡议
10  遗产：从索引卡到信息时代
11  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照 OpenPhysicist 成品 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**La Fontaine 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 官方理由 "unparalleled contribution to the organization of peaceful internationalism"；导语另有 "effective leader of the peace movement in Europe"——前者为主，后者只作 Wikipedia 转述，勿互换 |
| 国际和平局创立年份 | page.md 正文作 "founded in 1882"（名录页 1910 得主条目作 1891 founded）——本篇**只忠于本人 page.md**，行文以「La Fontaine 1907 起任主席」为核心，创立年份表述沿用本人页面口径 |
| 非创始人 | La Fontaine 是国际和平局主席而非创始人，勿写「创办国际和平局」 |
| 妹妹关系 | Léonie 是妹妹（sister）——库内无 sibling 类型，用 colleague 类型并注明「妹妹、共创同盟」 |
| 世界法院候选人 | page.md 载其 1916 提名 Choate/Root/Eliot/White 为世界法院候选人（NYT 报道）——仅为提名建议，**禁建师承/合作关系** |
| 共济会 | page.md 明载共济会会员身份，客观陈述即可，不加评论 |
| occupation 噪声 | frontmatter occupation 列表混入 "Andrea Martinucci"（噪声），禁写进任何正文 |
| 无载禁写 | 配偶/子女/1901 之前的家庭细节均无载，禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| International Peace Bureau | 国际和平局 | 勿写成「国际和平署」；1907 起任主席 |
| Union of International Associations | 国际协会联盟 | 简称 UIA，1907 共创 |
| Institut International de Bibliographie | 国际目录学会 | 后成为 FID |
| Centre Intellectuel Mondial | 世界知识中心 | 后并入国联知识合作组织 |
| Pasicrisie internationale | 《国际判例集》 | 1902，仲裁史文献汇编 |
| documentation science | 文献学 | 与目录学（bibliography）区分 |
| Belgian League for the Rights of Women | 比利时女性权利同盟 | 1890 与妹妹共创 |
| Les Amis Philanthropes | 「慈善之友」共济会分会 | 布鲁塞尔 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Empire Collapse** — Cold Cinema（manifest 预分配，勿改）
- **风格**: 史诗 / 戏剧 / 沉重
- **匹配理由**: 其生命横跨两次世界大战中的比利时——「帝国崩塌」的暗色史诗气质匹配其在一战战后重建国际秩序、1943 年于沦陷的布鲁塞尔辞世的悲怆底色
- **本地路径**: `music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`
- **时长对齐**: ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Henri_La_Fontaine/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/seed_person.py` | 研究领域 + 社会关系入库引擎 |

> **开始执行。每完成一步汇报。**
> **最重要的事：每写一页就 make，看到溢出就修；所有事实以 page.md 为准，无载禁写。**
