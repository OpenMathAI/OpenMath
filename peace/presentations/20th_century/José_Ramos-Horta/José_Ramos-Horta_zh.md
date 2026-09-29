# 和平奖得主立传提示词（OpenPeace 批次 20 · José Ramos-Horta）

> 本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」之一，对象为个人：
> 若泽·拉莫斯·奥尔塔（José Ramos-Horta，1996 诺贝尔和平奖共同得主，东帝汶总统）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他人物侧共享 GitHub）。
- **本实例**：José Manuel Ramos-Horta（东帝汶政治家，第 4、7 任总统）。
- **设计哲学**：和平奖得主立传必须保留**「身份信息页」（Identity / Bio 速览页）**与「事业领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：José Manuel Ramos-Horta（1949-12-26 生于葡属帝汶帝力，在世）
- **气质关键词**：**流亡中的国家代言人、联合国外交的老兵、从诺贝尔奖到国家元首** —— 1996 诺贝尔和平奖获奖理由：
  > "for their work towards a just and peaceful solution to the conflict in East Timor"
  > （中译照抄名录：表彰他们为公正和平地解决东帝汶冲突所做的工作）
- **设计母题**：**漂泊的旗帜（exile flag）**。他把一个不被承认的小国声音带进联合国大厅二十余年——流亡者的旗帜隐喻无根而有向的坚持，是比「橄榄枝」更贴合其外交生涯的视觉语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/José_Ramos-Horta/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（OpenPeace 共享封面由主控统一建，若已有 `peace/presentations/cover/` 则优先用之）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：本批已完成「事业领域 + 社会关系入库」（见第 4 / 4.5 步表格），立传时以库内与 yaml 为准，不要另起炉灶。

### 第 0 步：下载并核对数据页面 【人物专属】

- ✅ 已抓取 Wikipedia 页面到 `peace/presentations/pages/20th_century/José_Ramos-Horta/`（四件套）
- 提取 infobox 与正文，**事实基准如下**（第一轮已核对）：
  - 生卒：1949-12-26 生于葡属帝汶帝力，在世；混血（Mestiço）：葡萄牙父亲 Francisco Horta、葡帝混血母亲；外祖父 Arsénio José Filipe 曾被葡当局流放帝汶；兄妹十一人中四人死于印尼军之手
  - 教育：Soibada 天主教会学校 → 1983 海牙国际法学院（国际公法）→ 1983 斯特拉斯堡国际人权学院（人权法）→ 1983 哥伦比亚大学美国外交政策研究生课程 → 1984-12 安条克大学和平研究个人化文学硕士（主修国际公法与国际关系）；1987 年起牛津 St Antony's College Senior Associate Member；通葡、英、法、西、德顿五语
  - 流亡与外交：1970–1971 因参与政治觉醒活动被流放葡属东非两年；Fretilin 创始成员（1988 退党成无党派）；1975-11 出任「东帝汶民主共和国」外交部长（时年 25 岁）；印尼入侵前三天离境赴联合国申诉；此后十年任 Fretilin 驻联合国常驻代表（抵美时口袋仅 25 美元）
  - 关键荣誉：1993 Rafto Prize 授予东帝汶人民（他代表领奖）；1996-12-10 诺贝尔和平奖（与 Ximenes Belo 共享）；2002 金盘奖；2013-11-25 澳大利亚荣誉同伴勋章；2010 何塞·马蒂勋章；2011 阿米尔卡·卡布拉尔勋章一等；2022 卡蒙斯勋章大领；2007 恩里克王子勋章大领；1998-06-09 自由勋章大十字；2010 柬埔寨大学政治学荣誉博士
  - 独立后仕途：2000-03-01 主持与 UNTAET 联合工作坊、2000-05 深化、参与缔造独立制度基础 → 2002-09-27 首任外交部长 → 2006-06-25 辞职（2006 危机）→ 2006-07-10 第二任总理 → 2007-05-20 第四任总统（决选 69.18%）→ 2008-02-11 遇刺中弹（叛军头目 Reinado 被击毙；Darwin 治疗至 4 月回国）→ 2012 任满卸任 → 2013-01-02 联合国几内亚比绍建设和平综合办（UNIOGBIS）特别代表兼负责人 → 2022-05-20 第七任总统（决选 62.10%，独立 20 周年就职）
  - 其他活动：2000 年起 TheCommunity.com 和平与人权网站顾问委员会主席、2001 汇集 28 位和平奖得主 9·11 后声明；Global Leadership Foundation 成员；2021 加入扎耶德人类博爱奖评审委员会；著作《Words of Hope in Troubled Times》；RTTL 主持 Horta Show
  - 家庭：与 Ana Pessoa Pinto（东帝汶国务与内政部长）离婚；独子 Loro Horta 生于流亡地莫桑比克
  - 关键时间线（15–20 节点）：1949 生 → 1970 流放 → 1975 Fretilin 与外长 → 1975-12 入侵前赴美 → 1975–1985 驻联合国代表 → 1983–1984 三校进修 → 1987 牛津 → 1988 退党 → 1993 Rafto → 1996 诺奖 → 2000 制度谈判 → 2002 外长 → 2006 总理 → 2007 总统 → 2008 遇刺 → 2012 卸任 → 2013 联合国特使 → 2022 复任总统

### 第 1 步：建立目录 【模板通用】

- `peace/presentations/20th_century/José_Ramos-Horta/` 已在（提示词所在），建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 参照 OpenPeace 已完成成品或 Kenneth_G_Wilson/Makefile，设置 `MAIN=José_Ramos-Horta_zh`（含重音字符需与文件系统核对，必要时 ASCII 化为 `Jose_Ramos-Horta_zh`）、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【人物专属】

- page.md 有 2023 官方肖像、1976 年青照、与奥巴马及卢配合照等真实 URL；下载官方肖像 500px 到 `images/` 并 `file` 验证；404 用 Commons `Special:FilePath` 回退；再失败用装饰圆占位

### 第 4 步：事业领域梳理（已入库） 【模板通用，人物专属内容】

**Ramos-Horta 的事业领域（按 rank 排序，与 yaml/DB 一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | diplomacy | 外交 | 流亡代表→首任外长→总统的外交主线 | 外长页 |
| 1 | self-determination | 民族自决 | 1975 年起为东帝汶事业代言 | 诺奖页 |
| 2 | international law | 国际法 | 海牙学院/安条克主修与法律顾问执业 | 教育页 |
| 3 | peace studies | 和平研究 | 安条克大学和平研究硕士 | 教育页 |
| 4 | human rights | 人权 | 斯特拉斯堡人权法训练与人权倡导 | 教育页 |

### 第 4.5 步：社会关系（已入库） 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Carlos Filipe Ximenes Belo | 无向 | 1996 诺贝尔和平奖共同得主 |
| spouse | Ana Pessoa Pinto | 无向 | 已离婚，曾任东帝汶国务与内政部长 |
| parent-child | Loro Horta | 父→子 | 独子，生于流亡地莫桑比克 |
| parent-child | Francisco Horta | 父→子 | 葡萄牙裔父亲 |
| influence | Mahatma Gandhi | Gandhi→Horta | 自述「最大的英雄」 |
| colleague | Xanana Gusmão | 无向 | 总统任内任命其为总理，2022 竞选支持者 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：坚韧、流亡者的孤独、外交场上的从容
- **配色**：主色深紫蓝 `#372A75`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeDiplo` 外交生涯 — 靛蓝 `#4C5FD5`
  - `badgeSelfdet` 民族自决 — 青绿 `#0E7C7B`
  - `badgeIntlLaw` 国际法 — 琥珀 `#E07B30`
  - `badgeStatecraft` 治国理政 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），呼应「漂泊的旗帜」母题——圆点如散落在世界地图上的流亡足迹

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input 共享封面）
01  封面 — 流亡中的国家代言人 / José Ramos-Horta 1949– + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、家世、教育、党派、
    历任职务、主要荣誉、核心事业）
03  事业概览 — 外交 / 民族自决 / 国际法 / 和平研究 / 人权
04  早年：帝力的混血少年 (1949–1970) — 家世流放传统、Soibada 教会学校、兄妹之殇
05  流放与觉醒 (1970–1975) — 葡属东非两年、Fretilin 创始、25 岁外长
06  联合国的十年 (1975–1985) — 入侵前三天离境、25 美元闯纽约、安理会申诉
07  学业与重塑 (1983–1988) — 海牙/斯特拉斯堡/哥大/安条克、牛津、退党独立
08  1996 诺贝尔和平奖 — 与 Belo 共享、"leading international spokesman since 1975"
09  独立的制度设计师 (1999–2002) — UNTAET 工作坊、CNRT、过渡内阁蓝图
10  外长与总理 (2002–2007) — 首任外长、2006 危机、辞职与临危受命
11  总统第一任 (2007–2012) — 决选 69.18%、2008 遇刺与康复、2012 谢幕
12  国际公务员 (2013–2022) — UNIOGBIS 特使、斡旋几内亚比绍
13  东山再起 (2022–) — 决选 62.10%、独立 20 周年就职、第七任总统
14  荣誉与著述 — 各国勋章、Words of Hope in Troubled Times、28 位得主声明
15  遗产：从诺奖得主到国家元首
16  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

**Ramos-Horta 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 任数口径 | 他是第 4 任（2007–2012）与第 7 任（2022– ）总统；frontmatter description 写 "2nd and 5th" 与 infobox 口径不符——以 infobox「4th & 7th」为准并留意页面自身口径冲突 |
| 菲律宾总统 | 1994 年欲禁马尼拉会议的是 Fidel Ramos（页面明文 no relation 无亲缘），勿与本传混淆 |
| 姓名重音 | José 带重音，目录/文件名已含 ó——Makefile/tex 文件名建议 ASCII 化防编译事故，正文保留重音 |
| 诺奖「共同」 | 1996 与 Ximenes Belo **共同**获奖；委员会另有措辞 "sustained efforts to hinder the oppression of a small people"，与官方 citation 句并存勿混用 |
| 离境时点 | 他在印尼入侵前三天离境——勿写成「入侵后流亡」； Fretilin 常驻代表任期为「此后十年」 |
| 学历细节 | 安条克 MA 于 1984-12 授予（Individualized MA in peace studies）；海牙/斯特拉斯堡/哥大均为 1983 年课程——四个年份勿互相挪用；牛津是 Senior Associate Member 非学位 |
| 遇刺细节 | 2008-02-11 中弹 2–3 枪、最重伤在右肺、2-21 恢复意识、4-17 回帝力——日期序列勿乱；Reinado 在交火中被击毙 |
| 总理过渡 | 2006-06-26 代理、7-08 获任命、7-10 宣誓——三个日期勿混；先辞外长（6-25）后撤回辞呈争总理 |
| 政治红线 | 伊拉克战争立场、缅甸/沙特等当代议题只作 page.md 明载客观事实记录，不加评价性语句；确需叙述时一句带过 |
| 引语 | 可用引语："I can wait five years..."（2012 UN 设想）、2022 胜选 "I have received this mandate from our people..."、Gandhi 为 greatest hero——其余勿杜撰 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Mestiço | 混血（葡亚混血） | 葡语借词 |
| Fretilin | 东帝汶独立革命阵线 | 1974-1988 党籍 |
| UNTAET | 联合国东帝汶过渡行政当局 | 2000 工作坊对手方 |
| CNRT | 全国重建大会 | 独立制度谈判参与方 |
| persona non grata | 不受欢迎的人 | 1994 泰国宣布 |
| Rafto Prize | 拉夫托奖 | 1993 授予东帝汶人民 |
| UNIOGBIS | 联合国几内亚比绍建设和平综合办 | 2013 特使职务 |
| self-determination | 民族自决 | 委员会期望的解决基础 |
| St Antony's College | 圣安东尼学院（牛津） | Senior Associate Member |
| Tetum | 德顿语 | 东帝汶最通用语言 |
| Order of Australia | 澳大利亚勋章 | 荣誉同伴（Honorary Companion） |
| Zayed Award for Human Fraternity | 扎耶德人类博爱奖 | 2021 评委 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配勿改】

- **选定曲目**: **Timeless** — Alex-Productions
- **风格**: 沉稳 / 纪录片 / 长期纲领
- **匹配理由**: 「永恒」匹配其跨越半个世纪的外交坚持——从 25 美元闯纽约到两任总统；纪录片气质匹配流亡—抗争—建国的完整叙事弧线；沉稳感匹配其外交场上的从容底色
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`
- **时长**: 与 16 页成片用 ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/José_Ramos-Horta/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节） |
| `MySQL/data/José_Ramos-Horta.yaml` | 领域/关系入库母本 |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
