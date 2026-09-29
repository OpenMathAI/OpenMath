# 医学家立传提示词（Harald zur Hausen）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2008 年得主（HPV 半奖） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Harald zur Hausen（1936-03-11 生于盖尔森基兴 ~ 2023-05-29 逝于海德堡，享年 87 岁）
- **气质关键词**：**肿瘤病毒学家、HPV 致宫颈癌的证明者、HPV 疫苗的科学奠基人** —— 2008 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，本奖"HPV/HIV 两半"中 HPV 半奖）：
  > "for his discovery of human papilloma viruses causing cervical cancer"
  > （因其发现人乳头瘤病毒导致宫颈癌）
- **设计母题**：**病毒颗粒与疫苗之盾（virion & shield of vaccine）**。HPV 球状颗粒、Southern blot 的杂交条带、挡在宫颈细胞前的疫苗屏障——"从争议到防线"的视觉隐喻。
- **本地 Wikipedia 路径**：medic/presentations/pages/21th_century/Harald_zur_Hausen/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/21th_century/Harald_zur_Hausen/page.md`；目录 `medic/presentations/21th_century/Harald_zur_Hausen/`；Makefile 改 `MAIN=Harald_zur_Hausen_zh`；肖像优先 images.txt 所列 Commons 图（zur Hausen in 2010），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Harald_zur_Hausen.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 职业主领域（infobox Fields） | 封面 |
| 1 | tumor virology | 肿瘤病毒学 | EBV 转化、HPV 致癌、oncovirus | 核心页 |
| 2 | oncology | 肿瘤学 | 宫颈癌病因与疫苗 | 诺奖页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Werner Henle | 无向 | 费城儿童医院病毒实验室同事（EBV 致癌研究） |
| colleague | Gertrude Henle | 无向 | 费城儿童医院病毒实验室同事（EBV 致癌研究） |
| collaborator | Lutz Gissmann | 无向 | 合作分离 HPV6（生殖器疣） |
| spouse | Ethel-Michele de Villiers | 无向 | 1993 结婚，DKFZ 同事研究员 |
| collaborator | Ethel-Michele de Villiers | 无向 | 1981 年起长期合著乳头瘤病毒论文 |
| co-honored | Luc Montagnier | 无向 | 2008 诺贝尔生理学或医学奖同届共享（HPV 与 HIV 两半） |
| co-honored | Françoise Barré-Sinoussi | 无向 | 2008 诺贝尔生理学或医学奖同届共享（HPV 与 HIV 两半） |
| co-honored | Ian Frazer | 无向 | 2006 William B. Coley 奖共享 |

> 对手方规范名：本篇对手方均无库内记录，按 page.md 形式新建 stub（Werner/Gertrude Henle 拆两条，勿与库内 Jacob Henle id=4470 混淆）；2008 三人 co-honored 边与 Montagnier/Barré-Sinoussi 两篇镜像幂等合并。

## 五、配色方案

- **气质**：德国实验室的坚韧 + 逆流而行的孤证 + 疫苗防护的公共关怀
- **主色**：病毒红 `#9E2B25`（警示与 HPV 防线的双关）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` HPV 与宫颈癌 — 病灶红 `#B23A48`
  - `badgeB` 肿瘤病毒（EBV/oncovirus）— 病毒紫 `#5E4B8B`
  - `badgeC` HPV 疫苗 — 防护绿 `#3E6B4F`
  - `badgeD` DKFZ 建制 — 德国灰蓝 `#3A4A6B`
- **背景母题**：低透明度球状病毒颗粒阵列 + 一道弧形屏障线（疫苗之盾）。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — HPV 致宫颈癌的证明者 / Harald zur Hausen 1936–2023 + badge + 右上头像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Gelsenkirchen、医学博士 1960 杜塞尔多夫、DKFZ 主席 20 年、诺奖 2008）
03  核心贡献概览 — EBV 致癌证明 / HPV 假说 / HPV16/18 鉴定 / HPV 疫苗基础
04  战时童年与医学之路 (1936–1962) — 天主教家庭、Vechta Antonianum 中学、Bonn/Hamburg/Düsseldorf 三校医学、1960 医学博士、1962 取得医师资格
05  费城与 EBV (1964–1969) — 与 Werner/Gertrude Henle 共事；1967 参与首次证明 EBV 可将淋巴细胞转化为癌细胞
06  德国辗转 (1969–1983) — Würzburg 教授、Erlangen-Nürnberg、Freiburg 病毒与卫生系主任
07  1976 假说：HPV 致宫颈癌 — 逆主流（当时普遍怀疑）提出；与 Gissmann 自生殖器疣离心分离 HPV6
08  1983-84：HPV16/18 现身 — Southern blot 杂交在宫颈癌组织中鉴定 HPV16（1983）、HPV18（1984），覆盖约 75% 宫颈癌；公布引发重大科学争议（后获证实）
09  2008 诺贝尔奖 — 官方理由全句（his discovery，独享 HPV 半）；同届 Montagnier/Barré-Sinoussi 得 HIV 半
10  争议与澄清（客观一页）— 诺奖公布后 Bo Angelin 兼任 AstraZeneca 董事会引发的利益冲突质疑；Nobel 秘书长声明 Angelin 表决时不知情、同僚普遍认为奖当其得——仅 page.md 实载
11  DKFZ 二十年 (1983–2003) — 董事会主席兼科学顾问委员会成员、海德堡大学医学教授；晚年 Konstanz Zukunftskolleg、International Journal of Cancer 主编、德国癌症援助副会长 (2010)
12  家庭 — 三子（Jan Dirk/Axel/Gerrit）；1993 娶 DKFZ 同事 Ethel-Michele de Villiers（1981 年起合著者），诺奖传记中致谢其贡献
13  荣誉长廊 — Robert Koch Prize 1975、Gairdner 2008、Warren Alpert 2007、Prince Mahidol 2005、Paul Ehrlich 奖 1994、Coley 奖 2006（与 Ian Frazer）、德国联邦十字勋章 2009
14  遗产：一支疫苗的诞生 — HPV 疫苗 2006 上市，宫颈癌成为可预防癌症
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 两半结构 | 2008 = zur Hausen **独享一半**（HPV，"his discovery"）+ Montagnier/Barré-Sinoussi 共享另一半（HIV，"their discovery"）——"共享"表述勿混 |
| 死亡日期 | metadata 双值 2023-05-29 / 05-28，**以 page.md 正文 29 May 2023 为准** |
| Henle 夫妇 | Werner 与 Gertrude 是两人（从纳粹德国出逃的病毒学家夫妇）——拆两条 colleague 边，勿写成一人或"导师" |
| EBV 年份 | 1967 参与首次证明病毒（EBV）能把健康淋巴细胞转为癌细胞——"参与"而非独功 |
| HPV 鉴定链 | HPV6 自生殖器疣离心分离（与 Gissmann）→ 1983 HPV16（Southern blot）→ 1984 HPV18；75% 是 HPV16/18 覆盖的宫颈癌比例——链条与数字勿混 |
| 争议双重含义 | 页面有两处争议：①HPV 假说初遭科学界大量批评（后被证实）②诺奖 AstraZeneca 利益冲突质疑——两件事勿混，后者主语是委员会成员 Angelin 而非 zur Hausen |
| 疫苗时间 | HPV 疫苗"首个制剂 2006 商业化"；zur Hausen 的工作是"使之可能"（made possible）——勿写他"发明疫苗"（研发者另有其人，page.md 无载禁写） |
| 在世者配偶 | de Villiers 与其 1981 年起即合著、1993 结婚——spouse+collaborator 双行；"诺奖传记致谢"系 page.md 明载可写 |
| 引语红线 | page.md 无整句直接引语——全部转述，中文引号内不得出现"原话" |
| 早年德国 | 出生于 Gelsenkirchen（纳粹德国时期的 Gau Westphalia-North）——正文可写今地名，政治语境一律从略 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| human papillomavirus (HPV) | 人乳头瘤病毒 | HPV16/18 为高危型 |
| cervical cancer | 宫颈癌 | 全球女性主要癌症死因之一 |
| oncovirus | 肿瘤病毒 | 致癌病毒统称 |
| Epstein–Barr virus (EBV) | EB 病毒 | 1967 首证病毒致癌（淋巴细胞） |
| Southern blot | Southern 印迹杂交 | 1983 鉴定 HPV16 的方法 |
| genital warts | 生殖器疣 | HPV6 相关 |
| DKFZ | 德国癌症研究中心（DKFZ） | 海德堡，任职主席 1983-2003 |
| William B. Coley Award | 科利奖 | 2006 与 Ian Frazer 共享 |

## 九、背景音乐选择

- **选定曲目**：**Ascension** — Alex-Productions（manifest 预分配）
- **匹配理由**："攀升/升华"贴合其逆流而上的科学轨迹——假说被质疑二十年、终成疫苗防线并登顶诺奖；曲式的层层推进呼应"从孤证到共识"的攀升弧线。
- **本地路径**：music_audio/ 下 Alex-Productions Ascension 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
