# 医学家立传提示词（Frederick Banting）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1923 年得主（弗雷德里克·班廷，胰岛素共同发现者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Frederick Grant Banting（1891-11-14 生于安大略省 Alliston 附近农场 ~ 1941-02-21 卒于纽芬兰 Musgrave Harbour 空难，享年 49 岁）
- **气质关键词**：**胰岛素的共同发现者、最年轻的生理学或医学奖得主（32 岁）、战地军医出身的实践型研究者** —— 1923 获奖理由（与 John Macleod 共享）：
  > "for the discovery of insulin"（因发现胰岛素）
- **设计母题**：**第一支胰岛素**。1922-01-11 多伦多总医院，14 岁的 Leonard Thompson 接受史上第一针胰岛素——视觉隐喻可用「注射器 + 瓶中清液 + 从绝望到生机的光线」，辅以加拿大枫叶与北极写生笔触呼应其画家身份。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Frederick_Banting/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Frederick_Banting/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Frederick_Banting/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Frederick_Banting_zh`、`VIDEO_NAME=Frederick_Banting_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Frederick_Banting/images.txt` 中 URL（250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证）；404 则用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 Banting/Best 合影（1924）与 Time 封面（1923-08-27）。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Frederick_Banting.yaml`，`cd MySQL && python3 seed_person.py data/Frederick_Banting.yaml` 幂等入库）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`（latexmk 多遍），0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | endocrinology | 内分泌学 | 胰岛素发现，1923 诺奖核心 | 胰岛素页 |
| 1 | diabetes | 糖尿病研究 | 从绝症到可控的治疗革命 | 胰岛素页 |
| 2 | pharmacology | 药理学 | infobox Fields 载明；1921-22 在多伦多讲授 | 身份页 |
| 3 | aviation medicine | 航空医学 | 二战 RCAF 第 1 临床研究组（CIU）负责人 | 战时页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | John Macleod (physiologist) | 无向 | 1923 诺贝尔生理学或医学奖共享（for the discovery of insulin） |
| controversy | John Macleod (physiologist) | 无向 | 胰岛素发现功劳归属之争，二人终生不睦（1928 拒出席其欢送晚宴） |
| advisor-student | Charles Best | 学生 | 学生，1921-22 共同分离胰岛素（Banting 分一半奖金予 Best） |
| colleague | James Collip | 无向 | 生物化学家，协助以酒精法纯化胰岛素提取物 |
| colleague | Wilbur Franks | 无向 | 二战期间协助其研制 G-suit 抗荷服，1941 搭机赴英测试 |
| spouse | Marion Robertson | 无向 | 1924 结婚，1932 离异，育一子 |
| spouse | Henrietta Ball | 无向 | 1937 结婚 |

> 不入库：画家 A. Y. Jackson / Lawren Harris（艺术挚友，非科学关系，可在幻灯片叙事中提及）；患者 Leonard Thompson、Elizabeth Hughes Gossett（医患）；一战上级 Starr、Palmer。
> 库内当时无 Charles Best / James Collip / John Macleod 记录，均由本 yaml 新建 stub（Macleod 用 manifest 全名 `John Macleod (physiologist)`，其本人 yaml 将回填 QID）。

## 五、配色方案 【人物专属】

- **气质**：加拿大荒野的质朴 + 医学的生机 + 军人的克制
- **主色**：加拿大枫叶红 `#C8102E`（胰岛素带来的"生命之血"，亦呼应国籍）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 胰岛素/内分泌 — 朱红 `#B02A30`
  - `badgeB` 糖尿病治疗 — 青绿 `#0E7C7B`
  - `badgeC` 军旅与航空医学 — 钢蓝 `#2E4A66`
  - `badgeD` 绘画与北极 — 琥珀 `#C77F3B`
- **背景母题**：稀疏大圆 + 细线（注射刻度与心电式曲线的呼应），四色错落，呼应"从农场到实验室再到北极写生"的多面人生。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页（\input 共享封面，参照 openphysicist_page.tex 机制）
01  封面 — 胰岛素的共同发现者 / Frederick Banting 1891–1941 + 四色 badge + 右上头像 + 国籍行 Canada
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地 Alliston、教育 Toronto MB/MD、
    任职 Western Ontario/Toronto、荣誉 Nobel 1923/KBE 1934/FRS 1935、核心领域）
03  核心贡献概览 — 胰岛素的分离 / 糖尿病治疗革命 / 航空医学 / 业余画家
04  农场少年与求学 (1891–1916) — Alliston 农家、Victoria College 首年挂科重读、1912 入医学院、
    1916-12-09 MB 毕业次日即报到参军
05  一战军医 (1915–1919) — 两次因视力被拒、Amiens 与 Cambrai、炮弹创伤、Military Cross
    （"exceptional bravery while attending the wounded under fire"）
06  乡村医生与转折点 (1919–1920) — London, Ontario 行医不顺、西安大略兼职教骨科学、
    1920-11-01 胰腺讲课触发阅读、Barron 1920 胰管结扎论文启发
07  多伦多实验室：Banting & Best (1921) — 向 Macleod 陈情、获实验室与 Best、犬切除胰腺模型、
    1921-11 胎牛胰腺提取物的关键突破
08  胰岛素的诞生 (1922) — 成人胰腺提取成功、1922-01-11 Leonard Thompson 首次注射、
    Collip 酒精纯化法、商业来源猪牛胰腺直至基因工程菌
09  四人分赏与诺贝尔奖 (1923) — 与 Macleod 共享、Banting 分半奖给 Best、Macleod 分半给 Collip、
    32 岁为生理学或医学奖最年轻得主、加拿大议会终身年金 $7,500
10  胰岛素之后 — Banting and Best 医学研究讲席教授（1923）、研究硅肺/癌症/溺水机制
11  航空医学与二战 — 1938 RCAF CIU 主持、飞行员"blackout"研究、协助 Franks 发明 G-suit、
    芥子气解毒剂以身试毒
12  画家班廷 — 1921 起作画、Group of Seven 的 A. Y. Jackson 挚友、1927 北极 Beothic 号写生、
    加拿大最杰出的业余画家之一
13  荣誉与认可 — Nobel 1923、John Scott Medal 1923、Cameron Prize 1927、Flavelle Medal 1931、
    FRS 1935、KBE 1934、1941 空难殉职（赴英测试飞行服途中）
14  遗产 — World Diabetes Day（11-14 生日，1991 IDF+WHO 设立）、Flame of Hope（1989 王太后点燃，
    治愈之日熄灭）、Banting Postdoctoral Fellowship、月球 Banting 陨石坑、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字为 "for the discovery of insulin"，与 Macleod 共享；勿改写为"发现并应用胰岛素" |
| 四人分赏结构 | Banting 分**自己那一半**给 Best；Macleod 分另一半给 Collip——不要写成"两人各分一半给 Best 和 Collip"之外的花样 |
| 最年轻 | 32 岁是**生理学或医学奖**最年轻得主（page.md 明载），勿扩大为"全部诺奖最年轻" |
| 死亡细节 | 1941-02-21 纽芬兰 Musgrave Harbour 空难**次日伤重不治**（非当场死亡）；飞行目的是测试 Franks 飞行服；两台发动机故障 |
| 学历时间线 | MB 1916-12-09、MD 1922（金奖）；大学第一年曾挂科重读、拼写困难——勿写成少年天才 |
| 胰岛素时间线 | 1920-11-01 讲课 → Barron 论文 → 1921 夏 Macleod 实验室 → 1921-11 胎牛胰腺 → 1922-01-11 Leonard Thompson 首针，勿错置 |
| 专利 | US patent no.1,469,994（1923-01-12 申报、1923-10-09 授权，Banting/Best/Collip）；Macleod 页另载专利转予 MRC 防滥用的口径 |
| 军衔与战争 | 1915 入伍（两次因视力被拒）、上尉、Military Cross 1919；Amiens/Cambrai 均为一战战役，勿与二战混淆 |
| 世界糖尿病日 | 1991 年由 IDF 与 WHO 以其生日 11-14 设立，勿写"联合国大会设立" |
| metadata 冲突 | metadata occupation 含 writer 等；正文口径为 pharmacologist/orthopedist/field surgeon——以 page.md 为准 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| insulin | 胰岛素 | Schafer 命名的假想激素，Banting 前未提取成功 |
| islets of Langerhans | 胰岛（朗格汉斯岛） | 与腺泡细胞区分是实验关键 |
| pancreatic duct ligature | 胰管结扎 | Barron 1920 论文的思想起点 |
| trypsin | 胰蛋白酶 | 破坏胰岛素的酶，须先灭活其来源细胞 |
| fetal pancreas extract | 胎儿胰腺提取物 | 1921-11 产量突破的关键 |
| G-suit | 抗荷服 | Franks 发明、Banting 协助，勿写"班廷发明" |
| Military Cross | 军功十字勋章 | 一战嘉奖，1919 |
| annuity | 年金 | 1923 加拿大议会终身年金 $7,500 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配）
- **风格**：开拓 / 前行 / 沉稳史诗
- **匹配理由**：从安大略农场少年到"胰岛素之路"的开拓者——Pathfinder 的行进感匹配"乡村医生 → 多伦多实验室 → 第一支胰岛素 → 32 岁诺奖 → 战时空难殉职"的拓荒叙事。
- **本地路径**：`music_audio/inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav` → 复制为 `presentations/20th_century/Frederick_Banting/Pathfinder.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；事实全部以 page.md 为准。**
