# 医学家立传提示词（Harvey J. Alter）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2020 年得主（哈维·奥尔特，非甲非乙肝炎的确认者、丙肝病毒发现三人组之首）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Harvey James Alter（1935-09-12 生于纽约市，在世）
- **气质关键词**：**输血安全的守护者、"非甲非乙肝炎"的确认者、NIH 五十年如一日的临床研究者** —— 2020 获奖理由（与 Michael Houghton、Charles M. Rice 三人共享）：
  > "for the discovery of Hepatitis C virus"（因发现丙型肝炎病毒）
- **设计母题**：**储存在冰箱里的答案**。Alter 在 NIH 临床中心建立的血样储存库，让 1988 年能用十几年前的样本确认新病毒——"耐心保存的样本终会开口说话"。视觉隐喻：一排血样试管与日历长廊。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Harvey_J._Alter/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Harvey_J._Alter/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Harvey_J._Alter/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Harvey_J._Alter_zh`、`VIDEO_NAME=Harvey_J._Alter_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Harvey_J._Alter/images.txt`（2020 照 / 2000 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 2020 诺奖三人实验示意图（15_Hegasy_Nobel_Prize_2020_HepC.jpg）。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Harvey_J._Alter.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 非甲非乙肝炎→丙肝，2020 诺奖核心 | 核心页 |
| 1 | transfusion medicine | 输血医学 | NIH 输血医学部资深研究员/副主任 | 身份页 |
| 2 | infectious diseases | 传染病学 | 临床中心传染病组首席 | 身份页 |
| 3 | hematology | 血液学 | Georgetown 血液学研究员出身 | 早年页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Michael Houghton (virologist) | 无向 | 2020 诺贝尔生理学或医学奖三人共享（发现丙型肝炎病毒） |
| co-honored | Charles M. Rice | 无向 | 2020 诺贝尔生理学或医学奖三人共享（发现丙型肝炎病毒） |
| colleague | Baruch Blumberg | 无向 | 1964 共同发现澳大利亚抗原，乙肝病毒分离的关键 |
| collaborator | Bob Purcell | 无向 | 合作经黑猩猩传代实验证明非甲非乙肝炎的病毒病因 |
| colleague | Edward Tabor | 无向 | 与其平行独立证明 NANBH 病因大概率为病毒 |
| spouse | Barbara Bailey | 无向 | 前妻，育二子（Mark 为医师、Stacey 为教师） |
| spouse | Diane Dowling | 无向 | 现任妻子，两继女 |

> 在世者，relations=7 为诚实值，Review 勿误判虚增或缺漏。
> 不入库：Harvey Klein（Lasker 颁奖辞引用者，红链）；Baruch Blumberg 的诺奖线（1976）只作背景叙事；NIH 上下级未具名者；九位孙辈。
> 库内当时无 Baruch Blumberg / Bob Purcell / Edward Tabor / Michael Houghton / Charles M. Rice 记录，均由本 yaml 新建 stub（Houghton 用 manifest 全名 `Michael Houghton (virologist)`——消歧义括号是规范名一部分）。

## 五、配色方案 【人物专属】

- **气质**：血样试管的暗红 + NIH 白墙的克制 + 五十年守候的耐心
- **主色**：血样暗红棕 `#7A3B2E`（输血医学的血色与年代感）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 澳大利亚抗原 — 琥珀 `#A0722D`
  - `badgeB` NANBH 确认 — 暗红 `#8C2F1B`
  - `badgeC` 血液筛查革命 — 深青 `#0E7C7B`
  - `badgeD` NIH 岁月 — 钢蓝 `#2E4A66`
- **背景母题**：一排竖直细试管（血样储存库）+ 横向年代刻度线，四色错落标记关键年份。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 丙肝病毒的发现者之一 / Harvey J. Alter 1935– + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生纽约、教育 Rochester BA 1956/MD 1960、
    任职 NIH 临床中心输血医学部 1969 起、荣誉 Nobel 2020/Lasker 2000/Distinguished Service Medal、
    核心领域）
03  核心贡献概览 — 澳大利亚抗原 / NANBH 的确认 / 血液筛查革命 / 与 Houghton/Rice 的接力
04  纽约与罗切斯特 (1935–1960) — 犹太家庭、纽约出生、Rochester 大学 BA 1956、MD 1960、
    Strong Memorial 住院医起点
05  游学历练 (1961–1969) — NIH 临床研究员（1961-64）、华盛顿大学内科住院医（1964-65）、
    Georgetown 血液学研究员（1965-66）、Georgetown 血液研究主任（1966-69）
06  1964：澳大利亚抗原 — 与 Baruch Blumberg 共同发现澳大利亚抗原、
    成为分离乙肝病毒的关键——Klein 评价引语："对许多人是生涯巅峰，对 Alter 只是吉兆"
07  NIH：血液储存库的远见 (1969–) — 临床中心输血医学部资深研究员（1969 至今）、
    传染病组首席（1972 起）、研究副主任（1987 起）、储存输血相关肝炎血样的项目
08  1970s：非甲非乙肝炎的确认 — 多数输血后肝炎并非甲肝或乙肝所致、
    与 Purcell 合作、与 FDA 的 Tabor 平行独立——黑猩猩传代实验证明病因大概率为病毒
09  血液筛查革命 — 基于其工作的全美献血者筛查、输血相关肝炎风险从 30%（1970）降至近 0
10  1988-1989：新病毒现身 — 用储存的 NANBH 样本 panel 确认新病毒存在、
    1989-04 Science 两篇文章正式命名丙型肝炎病毒（HCV）
11  三人接力与 2020 诺贝尔奖 — Alter 确认未知病毒存在 → Houghton 克隆病毒 → Rice 证明致病、
    2020 三人共享 "for the discovery of Hepatitis C virus"
12  荣誉与认可 — Karl Landsteiner Award 1992、Lasker 2000（与 Houghton）、
    Distinguished Service Medal（美国政府公卫系统最高文职奖）、NAS/IOM 院士、
    INSERM 国际奖 2005、Gairdner 2013、Grand Hamdan 2016
13  个人生活 — 前妻 Barbara Bailey（二子 Mark/Stacey）、现任妻子 Diane Dowling（两继女）、
    九个孙辈
14  遗产 — 美国血液供应史上最安全时代的奠基人之一、
    从"看不见的肝炎"到可筛查可治愈的丙肝、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方 citation json 逐字为 "for the discovery of Hepatitis C virus"；page.md 转述另有 "discoveries that led to the identification of the Hepatitis C virus"——引用以 citation json 为准 |
| 三人接力结构 | Alter（确认未知病毒存在）→ Houghton（克隆/鉴定病毒）→ Rice（感染性克隆证明单独致病）——本篇以第一棒为主线，勿替他人立传 |
| 平行独立 | Edward Tabor（FDA）是**平行独立**证明——"independently" 一词必须保留，勿写成合作或师承 |
| Blumberg 角色 | 澳大利亚抗原是 1964 与 Blumberg 共同发现（Blumberg 后获 1976 诺奖）——Alter 的生涯起点而非终点，用 Klein 引语点题 |
| 数字锚点 | 输血肝炎风险 30%（1970）→ 近 0；1988 用储存 panel 确认；1989-04 Science 两篇文章——三组数字/时间勿错 |
| 血样储存库 | "储存血样以查明输血相关肝炎成因并降低风险" 是其方法学远见——核心叙事，勿省略 |
| 两任妻子 | Barbara Bailey（前妻，二子 Mark 医师/Stacey 教师）+ Diane Dowling（现任，两继女 Lydia Rodin/Erinn Torres）——两行 spouse，note 区分 |
| 犹太家庭 | page.md 明载犹太家庭出身——客观背景一句带过 |
| 机构时长 | 1969 入 NIH 至今（page.md 口径 "from July 1969 to present"）——"五十年"叙事以此为准 |
| 奖项归属 | Lasker 2000 为**临床**医学研究奖（Clinical），与 Houghton 共享；Rice 的 2016 Lasker 属另一届——勿混写 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Australia antigen | 澳大利亚抗原 | = HBsAg，乙肝检测的关键 |
| non-A, non-B hepatitis (NANBH) | 非甲非乙肝炎 | 丙肝的旧称，命名史关键 |
| chimpanzee transmission studies | 黑猩猩传代实验 | 病因确证的实验路径 |
| blood donor screening | 献血者筛查 | 公卫影响的核心 |
| transfusion-associated hepatitis | 输血相关肝炎 | 研究对象 |
| stored specimen panel | 储存样本组 | 1988 确认病毒的方法学 |
| Distinguished Service Medal | 杰出服务勋章 | 美国公卫最高文职奖 |
| hepatitis C virus (HCV) | 丙型肝炎病毒 | 1989 正式命名 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart**（manifest 预分配）
- **风格**：律动 / 深情 / 电子氛围
- **匹配理由**：跨越半个世纪的谜题缓缓拼合——从"看不见的肝炎"到病毒现形，Falling Apart 的层层剥解感匹配"用储存样本慢慢逼出真相"的耐心叙事；曲名的离散与重组亦呼应三人接力最终合流。
- **本地路径**：`music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav` → 复制为 `presentations/21th_century/Harvey_J._Alter/Falling_Apart.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；三人接力与平行独立证明务必精确。**
