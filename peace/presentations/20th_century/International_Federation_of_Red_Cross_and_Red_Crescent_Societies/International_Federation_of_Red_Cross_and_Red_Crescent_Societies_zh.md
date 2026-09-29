# 和平奖得主立传提示词（OpenPeace 批次实例：League of Red Cross Societies）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 League of Red Cross Societies（红十字会协会，1963 诺贝尔和平奖共同得主，今 IFRC）为实例。
> **本篇为组织机构篇**：用「机构概览页」替代人物身份信息页，无个人生平叙事，叙事主线为机构的使命与演变。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放和平奖得主人物史（与 OpenPhysicist / OpenChemist 等共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：沿用物理学家侧标杆 Kenneth G. Wilson 提示词的 0–11 节骨架，适配组织机构叙事（机构概览页 + 使命领域表 + 机构关系表）。
- **本实例**：League of Red Cross Societies（LORCS，1919–1983）→ League of Red Cross and Red Crescent Societies（1983–1991）→ International Federation of Red Cross and Red Crescent Societies（IFRC，1991–今）。
- **设计哲学**：机构立传强调「使命的延续与名称的演变」——按时间线呈现改名史，三个名称均须出现且以获奖时名称 League of Red Cross Societies 为主线。

---

## 二、背景信息 【机构专属】

- **目标机构**：League of Red Cross Societies（红十字会协会，1919-05-05 成立于巴黎；2006 年 wiki 条目现名 IFRC）
- **气质关键词**：**全球最大人道网络的国家社会联合会、灾害救援的协调者、非武装冲突人道救援的开创者** —— 1963 诺贝尔和平奖获奖理由（与红十字国际委员会共同获得）：
  > "for promoting the principles of the Geneva Convention and cooperation with the UN"（表彰其推广《日内瓦公约》原则并与联合国开展合作）
- **设计母题**：**红十字与红新月双徽（the combined emblem）**。白底上并立的红十字与红新月、环绕红框——是本机构（及整个运动）的核心视觉符号，配 "Per Humanitatem ad Pacem" 拉丁语箴言；可作封面主图形与 badge 底纹。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/International_Federation_of_Red_Cross_and_Red_Crescent_Societies/page.md`（已抓取，事实基准见第 0 步）
- **参考模板**：
  - 物理学家标杆提示词：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节结构母本）
  - 同批成品参照：`peace/presentations/20th_century/Albert_Luthuli/Albert_Luthuli_zh.md`
  - 项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：社会关系已入库（第 4.5 步），立传 Beamer 完成后由主控将 `has_biography` 置 1。

### 第 0 步：核对本地 Wikipedia 页面 【机构专属】

- ✅ 已抓取页面到 `peace/presentations/pages/20th_century/International_Federation_of_Red_Cross_and_Red_Crescent_Societies/page.md`，**事实基准如下**：
  - 成立：1919-05-05 于巴黎，由协约国五国红十字会（英、法、意、日、美）代表共同创建；倡议者 Henry P. Davison（美国红十字会 War Committee 主席），获 Woodrow Wilson 总统支持；首任总干事为英军将领 Sir David Henderson；现总部日内瓦（1959 年迁入 Petit-Saconnex 现址；1922–1939 曾驻巴黎）
  - 性质：International Red Cross and Red Crescent Movement（国际红十字与红新月运动）三大组成部分之一（另两支为 ICRC 与 191 个国家红会）；人道主义援助组织
  - 规模：年触达 1.6 亿人；191 个成员国家红会；运动整体近 1,830 万志愿者（2025）
  - 使命演变：成立目标为"加强并联合既有红会开展卫生活动、促进新红会创建"——把运动的国际授权从 ICRC 的武装冲突场景扩展到**非武装冲突的灾害与卫生紧急情况**
  - 与 ICRC 的紧张与合作：初创时 ICRC 担忧主导权被削弱；Davison 拒绝吸纳战败国红会（违背 ICRC 普遍性原则）；1921/1923/1926 三届国际会议 + 1928 海牙章程厘清双方角色；1941 ICRC 发起 Joint Relief Commission；1997 Seville Agreement 进一步划分职责
  - 关键事业节点：首个行动任务为波兰斑疹伤寒疫情观察 → 1923 日本关东大地震首次大规模联合救援（35 国红会、2.77 亿瑞士法郎）→ 1920 起国际公共卫生护理研究生课程 → Junior Red Cross 青少年项目 → 1932 道路急救常设委员会 → 1930s 西班牙内战与二战援 ICRC → 1948 参与联合国巴勒斯坦难民紧急救援（负责黎巴嫩/叙利亚/约旦）→ 1950s 去殖民化后成员激增 → 2004 南亚海啸最大规模行动（40+ 国红会、2.2 万志愿者）→ 全球地雷禁用倡导
  - 改名史：1919 League of Red Cross Societies → 1983 League of Red Cross and Red Crescent Societies → 1991 International Federation of Red Cross and Red Crescent Societies（IFRC）
  - 关键荣誉：**Nobel Peace Prize 1963（1963-12-10 与 ICRC 共同获得）**；Nansen Refugee Award；七项基本原则 1965 年 XX 届国际会议通过
  - 关键时间线（15–20 节点）：1919-05-05 巴黎成立 → 1920 首期公共卫生护理课程/总理事会扩容 → 1922 秘书处迁巴黎 → 1923 日本地震联合救援 → 1925 开始发布救援呼吁 → 1928 海牙章程与国际理事会 → 1932 道路急救委员会 → 1934 苏联红会加入（58 国）→ 1939-09 秘书处回日内瓦 → 1941 Joint Relief Commission → 1945-10 战后理事会复会 → 1948 联合国巴勒斯坦难民项目 → 1951–1954 灾害救援转型 → 1959 现总部启用 → 1963-12-10 与 ICRC 共获诺贝尔和平奖 → 1965 七项基本原则 → 1983 更名加入红新月 → 1991 更名 IFRC → 1997 Seville Agreement → 2004 南亚海啸行动
  - 领奖现场：1963 奥斯陆领奖者为 ICRC 主席 Léopold Boissier 与 League 主席 John MacAulay（1959–1965 在任），挪威国王 Olav V 在场（page.md 图注明载）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `International_Federation_of_Red_Cross_and_Red_Crescent_Societies/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品的 `Makefile`，设置 `MAIN=International_Federation_of_Red_Cross_and_Red_Crescent_Societies_zh`、`VIDEO_NAME=International_Federation_of_Red_Cross_and_Red_Crescent_Societies_zh`

### 第 3 步：收集图片 【机构专属】

- 优先用 `page.md` 正文 Commons 图（如 1963 颁奖典礼照 Friedensnobelpreis-1963.jpg、Henry Davison 肖像、红新月邮票）；下载失败用装饰圆占位并在图注说明

### 第 4 步：使命领域表 【已入库，与 yaml fields 一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | humanitarian aid | 人道主义援助 | 全球最大人道网络的核心使命 | 概览页 |
| 1 | disaster relief | 灾害救援 | 1923 日本地震 → 2004 海啸的救灾协调 | 行动页 |
| 2 | public health | 公共卫生 | 护理培训、疫情应对、Junior Red Cross | 早期页 |
| 3 | international cooperation | 国际合作 | 与 ICRC/联合国/国家红会的协作网络 | 合作页 |
| 4 | peace education | 和平教育 | 培育和平文化、青少年人道教育 | 使命页 |

### 第 4.5 步：机构关系表 【已入库，与 yaml relations 一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Henry Pomeroy Davison | 机构←创始人 | 1919 倡议创建，美国红十字会 War Committee 主席 |
| colleague | John MacAulay | 无向 | 领奖时任主席（1959–1965），1963 奥斯陆代表协会领奖 |
| co-honored | International Committee of the Red Cross | 无向 | 1963 诺贝尔和平奖共同得主 |
| other | International Red Cross and Red Crescent Movement | 无向 | 母体运动之成员（与 ICRC 并列） |

- 入库操作见 `MySQL/data/International_Federation_of_Red_Cross_and_Red_Crescent_Societies.yaml`（seed_person.py 幂等入库；co-honored 与批次 4 ICRC yaml 的镜像行幂等去重）
- **方向约定**：founder 为有向（创始人→机构）；colleague/co-honored/other 无向

### 第 5 步：设计配色方案 【模板通用，机构专属色彩】

- **气质**：中立、普遍、行动力
- **配色**：深靛蓝（manifest 预分配主色 `#283593`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeRelief` 灾害救援 — 警示红 `#A63A2B`
  - `badgeHealth` 公共卫生 — 青绿 `#0E7C7B`
  - `badgeNobel` 诺奖 — 香槟金 `#C9A227`
  - `badgeMovement` 红十字运动 — 深靛 `#283593`
- **背景母题**：白底红十字/红新月双徽轮廓 + 柔和色块，呼应机构徽记

### 5.1 和平奖得主格式硬要求 【模板通用，★ 必须满足】

1. **封面有徽记/头像**：右上角双徽或机构图 + 细边框 + 机构名小字注。
2. **封面有属性**：明示 International organization（总部日内瓦），底部状态栏给出 `性质 | 总部 | 主要奖项` 三要素。
3. **必须有机构概览页**（替代身份信息页）：左徽记/图 + 右信息网格，含至少：成立时间与地点、创始人、总部沿革（巴黎→日内瓦）、成员规模、改名史、主要奖项、核心使命。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【机构专属，可微调】

```
00  OpenPeace 项目首页（\input cover 封面模板）
01  封面 — 全球人道网络的联合会 / League of Red Cross Societies 1919 + 四色 badge + 徽记 + 机构属性行
02  机构概览页（★ 必做）— 左徽记 + 右信息网格（成立、创始人、总部沿革、成员规模、改名史、荣誉）
03  核心使命概览 — 人道援助 / 灾害救援 / 公共卫生 / 国际合作
04  缘起：一战后的巴黎 (1919) — Davison 倡议、五国红会、Wilson 支持、初创争议
05  与 ICRC 的紧张与合作 — 主导权之争、1928 海牙章程、Seville Agreement
06  早期行动 (1920–1939) — 护理课程、Junior Red Cross、1923 日本地震、巴黎→日内瓦
07  战时与战后 (1939–1948) — Joint Relief Commission、理事会复会、联合国难民项目
08  转型与扩张 (1950s) — 灾害救援转型、去殖民化后的成员增长
09  诺贝尔和平奖 (1963) — 与 ICRC 共享、获奖理由、奥斯陆领奖现场
10  改名与原则 (1965–1991) — 七项基本原则、1983/1991 两次更名
11  走向今天 — Seville Agreement、2004 海啸、地雷倡导、1,830 万志愿者
12  遗产 — 运动三支柱的国家红会联合会、Per Humanitatem ad Pacem
13  结尾
```

### 第 7–8 步：版式要点 + 该机构专属陷阱表 【模板通用 + 机构专属】

**League of Red Cross Societies 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 三段改名史 | LORCS（1919）→ 红新月加入（1983）→ IFRC（1991）；wiki 条目现名 IFRC，但获奖时名称是 **League of Red Cross Societies**——全篇以获奖名为主线，现名仅在当代部分使用 |
| 共同得主 | 1963 与 **ICRC 共享**（同一获奖理由），勿写成独得；两机构是运动中并列的姊妹组织，非上下级 |
| 创始人口径 | 创始人是 **Henry Pomeroy Davison**；Woodrow Wilson 只是"支持者"，禁入 founder；Sir David Henderson 是首任总干事（受 Davison 协助），不是创始人 |
| Henderson 入库裁定 | 首任总干事 Sir David Henderson 仅正文一句提及，库内已有裸 stub 'David Henderson'（id=6840）身份难辨（可能为同名的当代人物），**禁入库**防分裂，仅在正文叙述 |
| 与 ICRC 早期冲突 | 初创时的主导权之争、战败国红会排斥等按 page.md 客观呈现——这是 Davison 篇章的史实，勿回避也勿渲染 |
| 联合国关系 | 1948 参与的是联合国巴勒斯坦难民紧急救援项目（受邀参与），IFRC **不是联合国机构**，勿写"联合国下属机构" |
| 领奖人 | 1963 领奖者为 ICRC 主席 Boissier 与 League 主席 MacAulay（图注明载）；现任领导 Kate Forbes/Jagan Chapagain 与获奖无关，勿混入历史叙事 |
| 政治敏感红线 | 涉及一战战胜国/战败国、去殖民化、巴勒斯坦难民项目、当代战争（乌克兰）等内容一律只作 page.md 明载的客观事实记录，不加评价性语句 |
| 无载禁写 | 各国红会（American/British/German 红会等）仅作为成员列举，不逐一建关系；Nansen Refugee Award 获奖年份页面未载，勿编造 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| League of Red Cross Societies | 红十字协会 | 获奖时名称（LORCS） |
| IFRC | 红十字会与红新月会国际联合会 | 1991–今现名 |
| International Committee of the Red Cross | 红十字国际委员会（ICRC） | 并列姊妹组织，勿混 |
| International Red Cross and Red Crescent Movement | 国际红十字与红新月运动 | 三支柱母体 |
| National Society | 国家红会 | 运动的成员单位 |
| Geneva Convention | 《日内瓦公约》 | 获奖理由核心文本 |
| disaster relief | 灾害救援 | 区别于 ICRC 的武装冲突场景 |
| Seville Agreement | 《塞维利亚协议》 | 1997 职责划分 |
| seven fundamental principles | 七项基本原则 | 1965 通过 |
| Per Humanitatem ad Pacem | 以人道通向和平 | 机构箴言 |
| Junior Red Cross | 少年红十字 | 青少年教育项目 |
| Nansen Refugee Award | 南森难民奖 | 页面未载年份，勿编造 |

---

## 四、背景音乐选择 ✅ 【机构专属】

- **选定曲目**: **Tragedy** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 深沉 / 史诗 / 救援
- **匹配理由**:
  - "深沉" 匹配机构语境——灾难与战争创伤中的救援行动，1923 日本地震、二战救济、2004 海啸
  - "史诗" 匹配其规模——从五国红会到 191 个成员、1,830 万志愿者的全球网络百年演变
  - "救援" 匹配叙事主线——这不是个人英雄的叙事，而是一部有组织的集体人道响应史
- **本地路径**: `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav` → `presentations/20th_century/International_Federation_of_Red_Cross_and_Red_Crescent_Societies/Tragedy.wav`
- **时长**: 以实际音频时长为准，14 页 × 7 秒 ≈ 98 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/International_Federation_of_Red_Cross_and_Red_Crescent_Societies/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 0–11 节结构母本 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `MySQL/data/International_Federation_of_Red_Cross_and_Red_Crescent_Societies.yaml` | 使命领域 + 机构关系入库文件 |
| `MySQL/data/International_Committee_of_the_Red_Cross.yaml` | 批次 4 ICRC yaml（co-honored 镜像对照） |
| `peace/nobel_peace_citations.json` | 获奖理由英文原文 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
