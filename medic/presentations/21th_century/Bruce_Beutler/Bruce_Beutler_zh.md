# 医学家立传提示词（Bruce Beutler）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2011 年得主（布鲁斯·博伊特勒，TLR4 受体的发现者、先天免疫激活机制共同得主）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Bruce Alan Beutler（1957-12-29 生于芝加哥，在世）
- **气质关键词**：**追猎内毒素受体三十年的"遗传学猎人"、TNF 双重身份的揭示者、正向遗传学的机械化革新者** —— 2011 获奖理由（与 Jules A. Hoffmann 共享一半；另一半授予 Ralph M. Steinman）：
  > "for their discoveries concerning the activation of innate immunity"（因发现先天免疫激活机制）
- **设计母题**：**猎人与开关**。LPS（内毒素）是细菌的"总开关"，Beutler 用五年定位克隆找到哺乳动物细胞上的那把锁——TLR4。视觉隐喻：迷宫中一枚发光的锁孔（受体）与插入的钥匙（LPS），辅以 ENU 诱变的点阵意象。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Bruce_Beutler/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Bruce_Beutler/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Bruce_Beutler/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Bruce_Beutler_zh`、`VIDEO_NAME=Bruce_Beutler_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Bruce_Beutler/images.txt`（UT Southwestern 2021 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 2011 卡罗林斯卡记者会照（与 Hoffmann 同框）。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Bruce_Beutler.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | innate immunity | 先天免疫 | TLR4 受体发现，2011 诺奖核心 | 核心页 |
| 1 | immunology | 免疫学 | TNF 双重身份、炎症与休克 | TNF 页 |
| 2 | genetics | 遗传学 | ENU 正向遗传学与 AMM 自动减数分裂图谱 | 遗传学页 |
| 3 | Toll-like receptors | Toll 样受体信号 | TLR4-TLR3-TRIF-UNC93B1 信号链 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Jules A. Hoffmann | 无向 | 2011 诺贝尔生理学或医学奖共享一半（激活先天免疫的发现） |
| co-honored | Ralph M. Steinman | 无向 | 2011 诺贝尔生理学或医学奖另一半（树突状细胞，死后追授） |
| advisor-student | Anthony Cerami | 导师 | 洛克菲勒大学博士后导师（1983-86），cachectin 鉴定为 TNF |
| advisor-student | Abraham Braude | 导师 | 本科期间在其 LPS 生物学实验室工作（metadata 载为 doctoral advisor） |
| advisor-student | Dan Lindsley | 导师 | UCSD 本科期间在其果蝇遗传学实验室学习表型定位 |
| colleague | Shizuo Akira | 无向 | TLR 家族感应功能主要阐明者；共享 2004 Robert Koch Prize 与 2006 Coley Award |
| colleague | Ruslan Medzhitov | 无向 | 共享 2011 Shaw Prize；h-Toll 过表达激活 NF-κB 研究 |
| parent-child | Ernest Beutler | 父 | 父，血液学家与医学遗传学家（G-6-PD 缺乏症、X 染色体失活），父子曾合作 |
| spouse | Barbara Lanzl | 无向 | 1980 结婚，1988 离异，育三子 |

> 在世者，relations=9 为诚实值。Review 勿误判虚增。
> 不入库：David Crawford / Karsten Peppel（TNF 抑制剂发明的研究生与博后，非知名独立学者）；Charles Janeway（h-Toll 语境人物，未共享奖项且已故，防弱边）；Charles A. Dinarello（2009 Albany Prize 共享，非主线）；Alexander Poltorak（positioning cloning 博后团队成员）；R. Shimazu（MD-2）、Jie-Oh Lee（复合物结构）；Hoffmann 侧的 Spätzle/NF-κB 语境人物。父亲 Ernest Beutler 用 parent-child（Family 节明载父子合作）。
> 库内当时无上述对手方记录，均由本 yaml 新建 stub；Jules A. Hoffmann / Ralph M. Steinman 用 citation json 姓名（Jules A. Hoffmann / Ralph M. Steinman），注意与化学家 Roald Hoffmann（#3521）无关。

## 五、配色方案 【人物专属】

- **气质**：免疫风暴的暗红 + 遗传学图谱的冷静 + 芝加哥的克制
- **主色**：炎症暗红 `#8C2F1B`（TNF 与免疫应答的血色，亦含"猎手"的锋利）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` TLR4 之谜 — 炎症暗红 `#8C2F1B`
  - `badgeB` TNF 双重身份 — 深青 `#0E7C7B`
  - `badgeC` ENU 正向遗传学 — 钢蓝 `#2E4A66`
  - `badgeD` AMM 与药物 — 琥珀 `#B4632C`
- **背景母题**：细密的点阵（ENU 突变点）+ 一条贯穿的"锁孔-钥匙"光路，四色错落。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 内毒素受体的猎人 / Bruce Beutler 1957– + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Chicago、成长 Arcadia、教育 UCSD BA 1976/
    Chicago MD 1981、导师语境 Cerami、任职 Rockefeller/UT Southwestern/Trinity Dublin、
    荣誉 Nobel 2011/Shaw 2011/Balzan 2007、核心领域）
03  核心贡献概览 — TNF 双重身份 / TNF 抑制剂发明 / TLR4 的发现 / ENU 正向遗传学与 AMM
04  医学世家 (1957–1981) — 犹太家庭、芝加哥出生、Arcadia 长大、圣盖博山徒步唤起生物兴趣、
    14 岁起在父亲 Ernest 实验室（City of Hope）学酶学、17 岁发表论文、
    Ohno 实验室接触 H-Y 抗原与免疫遗传、16 岁高中毕业、UCSD 18 岁 BA、芝加哥 MD 23 岁
05  放弃临床，回归实验室 (1981–1983) — UT Southwestern 内科实习与神经科住院医、
    "临床不如实验室有趣"的转向
06  洛克菲勒岁月：cachectin = TNF (1983–1986) — Cerami 实验室、从 LPS 激活巨噬细胞培养液
    纯化 cachectin 至均一、N 端测序认出 = 小鼠 TNF、人 TNF 亦有恶病质活性——
    TNF 的"分解代谢开关"第二身份
07  TNF 是脓毒性休克的元凶 — 抗 TNF 抗体被动免疫显著缓解 LPS 休克、
    TNF 受体两种亲和型的推断（p55/p75）、与 Dayer 证明滑膜细胞炎症反应——
    类风湿关节炎因果链的先声
08  发明 TNF 抑制剂 (1986–) — 与 Crawford/Peppel 设计受体-Ig 融合蛋白、专利 US5447851B1、
    人 p75 融合蛋白成为药物 Etanercept（Amgen）、累计销售逾 $74B——
    基础研究通往.class 药物的完整闭环
09  五年猎捕 LPS 受体 (1993–1998) — Lps 位点（4 号染色体）之谜、positioning cloning、
    >2000 次减数分裂、5.8 Mb 区间测序、两株 LPS 抗性小鼠（C3H/HeJ、C57BL/10ScCr）
    的 Tlr4 有害突变——TLR4 即 LPS 受体的跨膜组分
10  TLR 家族图景 — 人 TLR 十种、各司其 microbes 特征分子感应、
    Hoffmann 的果蝇 Toll 先声（抗菌肽应答）、Janeway/Medzhitov 的 h-Toll 过表达、
    Akira 对其他 TLR 的系统阐明——三条线汇成先天免疫激活的大图
11  2011 诺贝尔奖 — 与 Hoffmann 共享一半、Steinman 另一半（树突状细胞、死后追授）、
    Nobel lecture "How Mammals Sense Infection"（官方页载）
12  ENU 正向遗传学工厂 — 随机种系诱变→表型筛选→定位克隆、
    36 基因 77 突变、Ticam1/TRIF（Lps2）、Unc93b1（3d 三重缺陷）、SLC15A4（feeble）、
    MCMV resistome、铁吸收/听觉/色素/代谢新基因
13  AMM：自动减数分裂图谱 (2013–) — 定位克隆加速约 200 倍、26 万+ 突变测定、
    约 2500 基因 5800+ 因果判定、基因组饱和度量化、机器学习质控
14  遗产与现在 — UT Southwestern Regental Professor、宿主防御遗传学中心主任、
    TLR 激动剂药物（neoseptins/diprovocims，X 射线晶体学验证）、
    从内毒素到免疫疗法的长线、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖结构 ★ | 2011 三人得奖但**份额为 1/2 + 1/4 + 1/4**：Beutler 与 Hoffmann 共享一半（同一理由句 "for their discoveries concerning the activation of innate immunity"），Steinman 得另一半（树突状细胞、死后追授）——勿写成"三人平分"或"三人共享同一理由" |
| 理由句人称 | Beutler/Hoffmann 行用 "their"，Steinman 行用 "his"——引用时按 citation json 分别照抄 |
| TLR4 发现路径 | Janeway/Medzhitov 的 h-Toll 是**过表达推测**（page.md 明言"未证明配体"、且有 TLR2 误判的平行论文）；Beutler 的定位克隆才是**遗传学证据**——因果链勿倒置 |
| Hoffmann 的 Toll | 果蝇 Toll 感应的是内源配体 Spätzle（蛋白酶级联），**真菌分子并不直接结合 Toll**——page.md 明载，勿写成" Toll 直接识别真菌" |
| TNF 双重身份 | cachectin（恶病质因子）= TNF；"杀死癌细胞"的旧定义与"分解代谢开关"新身份并列——两个名字都要出现 |
| Etanercept 数字 | 累计销售逾 $74B（Amgen 销售）——数字勿错；专利号 US5447851B1 |
| Braude 定位 | metadata 载为 doctoral advisor；正文语境是**本科期间**在其 LPS 实验室——note 按正文措辞，勿写"博士导师"（MD 期间导师语境 page.md 未载） |
| 父子关系 | Ernest Beutler（1928-2008）是血液学家/医学遗传学家（G-6-PD 缺乏症、X 染色体失活发现者），父子曾在多个课题合作——parent-child + 合作叙事，Family 节明载 |
| 犹太家庭表述 | page.md 载出身犹太家庭、祖母为柏林 Charité 训练的儿科医生——客观背景，勿过度铺陈 |
| 在世者关系 | relations=9 均有 page.md 依据，Review 勿误判；Steinman 与 Beutler 无私人交往边，仅 co-honored |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| lipopolysaccharide (LPS) | 脂多糖/内毒素 | 革兰阴性菌外膜成分 |
| Toll-like receptor 4 (TLR4) | Toll 样受体 4 | LPS 受体复合物跨膜组分 |
| tumor necrosis factor (TNF) | 肿瘤坏死因子 | = cachectin，双重身份 |
| cachectin | 恶病质素 | TNF 的旧名/别名 |
| positional cloning | 定位克隆 | TLR4 发现的方法学 |
| ENU mutagenesis | ENU 诱变 | 烷化剂随机种系突变 |
| Etanercept | 依那西普 | p75 受体-Ig 融合药物 |
| dendritic cell | 树突状细胞 | Steinman 半奖主题，提及勿展开 |
| resistome | 抵抗组 | MCMV 感染生死基因全集 |
| automated meiotic mapping (AMM) | 自动减数分裂图谱 | 其发明（约 200 倍加速） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Empire Collapse**（manifest 预分配）
- **风格**：厚重 / 张力 / 史诗推演
- **匹配理由**：免疫应答本身即一场"帝国的建立与崩塌"——LPS 引爆的脓毒性休克是炎症帝国的失控，而找到 TLR4 就是找到开关；Empire Collapse 的厚重张力匹配"五年围猎一个受体 + TNF 休克机制"的高压叙事。
- **本地路径**：`music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav` → 复制为 `presentations/21th_century/Bruce_Beutler/Empire_Collapse.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；2011 份额结构与 TLR4 归属链务必精确。**
