# 医学家立传提示词（Mario Capecchi）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2007 年得主（与 Martin Evans、Oliver Smithies 共享）。
> 本文件是 Mario Capecchi 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面，
> 执行方按本提示词产出 15 页 Beamer 立传（本阶段不写 tex，仅沉淀事实与规范）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Mario Ramberg Capecchi（1937-10-06 生于意大利维罗纳，在世）
- **气质关键词**：**从街头孤儿到基因敲除之父、Hox 基因的解码者、犹他大学的长期主义者**
- **诺奖获奖理由（2007，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discoveries of principles for introducing specific gene modifications in mice by the use of embryonic stem cells ."
  > （因其发现利用胚胎干细胞对小鼠引入特定基因改造的原理）——注意 "their"：与 Martin Evans、Oliver Smithies 三人共享
- **设计母题**：**基因敲除（knockout）与重生**。被"关闭"的单个基因位点（视觉上一处留白的空位）与
  从战火街头走回实验室的人生轨迹互为镜像——"删除与重建"的双重隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Mario_Capecchi/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/21th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/21th_century/Mario_Capecchi/`，数据库写 greatminds 库（MySQL）。

- **第 0 步**：核对本地 page.md 事实基准（本提示词第三、四、七节已沉淀，执行时再逐句复核）
- **第 1 步**：建目录 `medic/presentations/21th_century/Mario_Capecchi/`（含 `images/`）
- **第 2 步**：复制 Makefile，设 `MAIN=Mario_Capecchi_zh`、`VIDEO_NAME=Mario_Capecchi_zh`
- **第 3 步**：收集肖像（page.md 无 infobox 肖像 URL 时用 Commons Special:FilePath 回退，404 则装饰圆占位）
- **第 4~9 步**：tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | molecular genetics | 分子遗传学 | 基因打靶/敲除小鼠，诺奖核心 | 核心页 |
| 1 | genetics | 遗传学 | infobox Fields 首列 | 身份页 |
| 2 | developmental biology | 发育生物学 | 小鼠 Hox 基因家族系统分析 | Hox 页 |
| 3 | biophysics | 生物物理学 | 哈佛 1967 PhD 学位科目 | 教育页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | James D. Watson | 师→生（博士导师） | 哈佛博士导师（DNA 双螺旋共同发现者），1967 生物物理学博士 |
| co-honored | Martin Evans | 无向 | 2007 诺贝尔生理学或医学奖三人共享（利用胚胎干细胞对小鼠引入特定基因改造的原理） |
| co-honored | Oliver Smithies | 无向 | 2007 诺贝尔生理学或医学奖三人共享（利用胚胎干细胞对小鼠引入特定基因改造的原理） |

> 说明：relations=3 为诚实值。母亲 Lucy Ramberg、舅舅 Edward Ramberg（RCA 物理学家）等家人不入库；
> 2008 年确认的同父异母妹妹 Marlene Bonelli 不入库（家族叙事可作人生页素材，不建关系边）。
> 对手方规范名：James D. Watson 用库内 id=3610 'James D. Watson'（库内另有 'James Watson' id=3787 分裂记录，
> 勿用后者，防撞键）；Oliver Smithies 用库内 id=4407；Martin Evans 库内暂无，由 med21-batch-04 建 yaml 时 UPD。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 3。

## 五、配色方案

- **气质**：坚韧、重生、长跑者的定力
- **主色**：深绛红 `#7E1E23`（战火记忆与意大利血统的深沉红）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：
  - `badgeKO` 基因敲除 — 石墨灰 `#37474F`
  - `badgeHox` Hox 基因 — 冷青 `#0E7C7B`
  - `badgeES` 胚胎干细胞 — 靛蓝 `#4C5FD5`
  - `badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：染色体带纹横条中一节"空心"段（敲除位点），配疏落星点（重生意象）

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover 共享首页）
01  封面 — 从街头到基因 / Mario Capecchi 1937– + 四色 badge + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒/维罗纳出身/教育 Antioch BS 1961 + Harvard PhD 1967/任职犹他大学/核心领域
03  核心贡献概览 — 基因打靶 / 敲除小鼠 / Hox 基因 / 三人共享诺奖
04  战火童年 (1937–1945) — 维罗纳出生；1941 母亲因反法西斯传单被捕流放德国；流落博尔扎诺街头、几死于营养不良；母亲战后寻回（page.md 明载可展开，勿添油加醋）
05  新大陆 (1946–1961) — 舅舅 Edward Ramberg（RCA 物理学家）资助赴美；宾州 Bryn Gweled 合作社区；George School 1956；Antioch College 化学+物理 BS 1961
06  从物理到分子生物学 (1961–1967) — MIT 研究生拟攻物理与数学，转向分子生物学（理由：小团队、不靠大机器）；转哈佛入 Watson 实验室；1967 生物物理学 PhD
07  哈佛与西行 (1967–1973) — 1967–69 Harvard Society of Fellows Junior Fellow；1969 哈佛医学院生化系助理教授、1971 副教授；1973 转犹他大学
08  基因打靶原理（核心贡献页）— 与 Smithies（各自独立）发展特定基因修饰原理、Evans 提供胚胎干细胞——三人拼合出敲除小鼠技术路线
09  Hox 基因家族 — 小鼠 Hox 基因系统分析：控制胚胎发育沿体轴从头到尾的细胞排布
10  2007 诺贝尔奖 — 理由逐字；诺奖演讲 "Gene Targeting 1977 - Present"（2007-12-07）
11  荣誉前奏 — Gairdner 1993 · Sloan 1994 · Kyoto 1996 · Franklin 1997 · Lasker 2001（与 Evans/Smithies 共同）· National Medal of Science 2001 · Massry 2002 · Wolf 2002/2003 · March of Dimes 2005
12  寻亲 (2007–2008) — 诺奖公布后 Marlene Bonelli 自称妹妹；2008 年 5 月北意大利会面确认——一句带过的温情注脚
13  犹他与 HHMI — Howard Hughes Medical Institute investigator（1988 起）；犹他大学人类遗传学与生物学 Distinguished Professor；NAS 院士
14  遗产：敲除时代 — 敲除小鼠成为发育生物学与医学研究的通用平台
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for their discoveries of principles for introducing specific gene modifications in mice by the use of embryonic stem cells ."；"discoveries" 复数、"principles" 表原理层贡献 |
| 2 | 三人分工 | page.md 只说 Evans/Smithies "who also contributed"——分工表述克制，勿过度演绎谁做了哪一步 |
| 3 | 国籍 | 出生意大利维罗纳，Nobel 官方口径与 infobox 均 **United States**；勿写意大利籍或双籍 |
| 4 | 早年叙事边界 | page.md 自注 "the details of his early life are unclear"——街头岁月、1942 与父亲短暂同住等细节须保留"细节不详/意大利档案显示"的措辞，勿补足成完整时间线 |
| 5 | 寻回时间 | 母亲战后寻找一年，"finally found him on his ninth birthday"（九岁生日当天在雷焦艾米利亚医院找到）；赴美资金来自舅舅 Edward Ramberg |
| 6 | 博士导师 | James D. Watson（DNA 结构共同发现者），1967 哈佛生物物理学 PhD；论文 "On the Mechanism of Suppression and Polypeptide Chain Initiation" |
| 7 | Junior Fellow | 1967–1969 哈佛 Society of Fellows Junior Fellow——是 fellowship 非学位，勿写成博士后或第二博士 |
| 8 | Watson 规范名 | 库内存在 'James D. Watson'(3610) 与 'James Watson'(3787) 分裂 stub——本篇统一用 'James D. Watson'，合并工作留主控 |
| 9 | Lasker/Wolf 年份 | Lasker 2001（三人共同）、Massry 2002、Wolf "2002–2003"（page.md 两种写法并存，表述为"2002/2003 期间"）、National Medal of Science 2001——勿互串 |
| 10 | Marlene Bonelli | 诺奖公布后自称同父异母妹妹，2008-05 北意大利会面确认——仅作叙事素材，不建关系边、不做家庭评价 |
| 11 | 奖项大表 | Honors 列表 30 余项（1969 Eli Lilly 起），页面只取代表性 8-10 项，勿逐条罗列挤爆版面；荣誉博士学位（Bologna 2012/Cardiff 2013/Ben-Gurion 2013/Yale 2024 等）可合并一句 |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| knockout mouse | 敲除小鼠 | 特定基因被关闭的工程小鼠 |
| gene targeting | 基因打靶 | 诺奖演讲标题用词 |
| embryonic stem cells (ES) | 胚胎干细胞 | Evans 贡献端 |
| homologous recombination | 同源重组 | 打靶的分子机制（如展开须有页面依据） |
| Hox genes | Hox 基因 | 体轴发育定位基因家族 |
| biophysics | 生物物理学 | 1967 哈佛 PhD 科目 |
| Antioch College | 安蒂奥克学院 | 1961 BS 化学+物理 |
| Society of Fellows | 哈佛学会青年研究员 | 1967–1969，非学位 |

## 九、背景音乐选择

- **选定曲目**：**Lonesome** — Alex-Productions（manifest 预分配）
- **匹配理由**：Lonesome 的孤寂底色对应本篇最独特的叙事起点——五岁流落街头、孤儿院、几死于营养不良的
  战火童年；而音乐后半程的开阔感呼应"从维罗纳街头到盐湖城实验室"的重生弧线。孤独与坚韧，正是 Capecchi 的气质。
- **备选（未采用）**：Timeless（长期主义感可用但更适合"纲领型"叙事）、Last Hope（希望感强但弱化了童年段的重量）
- **本地路径**：`music_audio/` 下 alex-productions 曲库按 curated_tracks.md 对应条目复制为
  `medic/presentations/21th_century/Mario_Capecchi/Lonesome.wav`
