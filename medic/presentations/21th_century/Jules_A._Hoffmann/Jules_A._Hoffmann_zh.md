# 医学家立传提示词（Jules A. Hoffmann）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2011 年得主 Jules A. Hoffmann（朱尔斯·霍夫曼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Jules_A._Hoffmann/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Jules Alphonse Nicolas Hoffmann（1941-08-02 生于卢森堡埃希特纳赫——当时为德占卢森堡，在世）
- **气质关键词**：**果蝇 Toll 的免疫破译者、先天免疫的复兴者、斯特拉斯堡的昆虫学家**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2011 条目；与 Bruce Beutler 共享**一半**奖金，理由同一句）：
  > "for their discoveries concerning the activation of innate immunity"（因他们发现先天免疫激活机制）
  - 另一半当年授予 Ralph M. Steinman（树突细胞与适应性免疫，理由不同、死后追授）——两层结构务必呈现。
- **设计母题**：**Toll 闸门**——果蝇体壁 Toll 受体被开启、抗菌肽基因点亮的意象：以闸门开启+防线点亮的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Jules_A._Hoffmann/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Jules_A._Hoffmann/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Jules_A._Hoffmann_zh`、`VIDEO_NAME=Jules_A._Hoffmann_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | innate immunity | 先天免疫 | Toll 通路抗真菌应答，2011 诺奖核心 |
| 1 | immunology | 免疫学 | infobox field_of_work 首项 |
| 2 | antimicrobial peptides | 抗菌肽 | Diptericin/Defensin/Cecropin/Attacin 鉴定 |
| 3 | insect immunity | 昆虫免疫 | 以昆虫为模式生物的终身方向 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Pierre Joly | 对方 → 导师 | 斯特拉斯堡大学博士导师（1969，蝗虫抗菌防御） |
| colleague | Bruno Lemaitre | 无向 | 1996 Toll 抗真菌应答论文共同发现者（后贡献争议见陷阱表） |
| co-honored | Bruce Beutler | 无向 | 2011 诺贝尔生理学或医学奖共享一半（先天免疫激活机制） |
| co-honored | Ruslan Medzhitov | 无向 | 2011 邵逸夫奖三人共享（与 Beutler、Medzhitov） |

**不入库但提示词可叙述**：Shizuo Akira（2011 Gairdner 共享）；Élie Metchnikoff（Hoffmann 实验证实其吞噬发现，科学史脉络非个人关系，库内有记录 4584 但不建边）；父 Jos Hoffmann（昆虫启蒙，家世叙述）；2015 Mainau 气候宣言联署（集体事件）。

## 五、配色方案 【人物专属】

- **气质**：欧洲的沉静、昆虫学的耐心、防线的锋利
- **主色**：`#1E3A5F`（斯特拉斯堡深蓝——CNRS 实验室的沉静）+ 香槟金诺奖色
- **badge 四分类色**：`badgeToll` Toll 通路 深蓝 `#1E3A5F`；`badgeInnate` 先天免疫 青绿 `#0E7C7B`；`badgePeptide` 抗菌肽 琥珀 `#C07A2A`；`badgeFly` 果蝇模式 玫瑰 `#A63A2B`
- **背景母题**：闸门开启+防线点亮的几何图案，呼应「Toll 闸门」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 先天免疫的复兴者 / Jules A. Hoffmann 1941– + 四色 badge + 右上头像 + 国籍行（France / Luxembourg）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1941-08-02、斯特拉斯堡大学 1969 博士、
    CNRS 研究主任、法国科学院院长 2007–2008、诺奖 2011）
03  核心贡献概览 — Toll 与真菌防线 / 抗菌肽家族 / Toll-Imd 双通路 / 哺乳类同源 TLR
04  卢森堡少年 (1941–1959) — 德占时期出生、父亲 Jos 的昆虫启蒙
05  斯特拉斯堡求学 (1959–1969) — 生物与化学本科、Pierre Joly 门下博士、蝗虫抗菌防御、
    证实 Metchnikoff 吞噬作用
06  CNRS 与 Marburg (1964–1978) — 1964 研究助理、1974 研究主任、1973–74 马尔堡博士后
07  从蝗虫到果蝇 (1980s) — Phormia terranovae 分离 82 残基富含甘氨酸的 Diptericin
08  抗菌肽家族与 NF-κB 之谜 — 启动子似 NF-κB 结合元件；Dorsal 突变体仍诱导 Diptericin → imd 基因
09  1996：Toll 掌握抗真菌钥匙（核心贡献页）— Lemaitre & Hoffmann：spätzle/Toll/cactus
    盒式调控果蝇成虫抗真菌应答；Drosomycin/Diptericin 分属 Toll/Imd 双通路
10  从果蝇到人类 — Toll 跨门类保守；哺乳类同源 TLR 由 Beutler 发现；败血性休克统一解释
11  CNRS 与科学组织 — 1978–2005 研究单元主任、1994–2005 分子与细胞生物学研究所所长、
    法国科学院副所长（2005–06）/院长（2007–08）
12  荣誉与认可 — Coley 2003、Koch 2004、Balzan 2007、Rosenstiel 2010、Keio 2010、
    Gairdner 2011、Shaw 2011、CNRS 金奖 2011、Nobel 2011、军团勋章
13  Lemaitre 争议 — 时任研究员对贡献承认度的公开主张（客观平衡呈现，见陷阱表）
14  遗产与结尾 — 先天免疫的复兴、TLR 药物学的地基、2012 Trinity College Dublin 荣誉教授
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 2011 两半结构 | Hoffmann 与 Beutler 共享一半（先天免疫激活，citation 同一句）；Steinman 独得另一半（树突细胞，理由不同）——勿写"三人共享同一理由" |
| Beutler 分工 | Toll 的果蝇功能归 Hoffmann/Lemaitre；哺乳类同源 Toll-like receptors 由 **Beutler** 发现——立传须写明分工，勿互串 |
| Lemaitre 争议 | page.md Controversy 节明载 Lemaitre 主张贡献未获充分承认——立传如处理必须客观一句带过（主张内容+其现任 EPFL 实验室），不得站队或渲染；争议属 Lemaitre 单方公开主张 |
| 国籍双口径 | Nobel 官方口径（citations json/总表）=France；frontmatter 双值 [France, Luxembourg]、正文 "Luxembourgish-French biologist"——yaml 取 France(0)+Luxembourg(1)，封面国籍行两写 |
| Dorsal 之谜 | Dorsal 属 NF-κB 家族，起初猜想直接调控 Diptericin，但突变体实验否定，改由 imd 基因承载——立传可写这条曲折，是科学叙事亮点 |
| 1996 论文标题 | "The Dorsoventral Regulatory Gene Cassette spätzle/Toll/cactus Controls the Potent Antifungal Response in Drosophila Adults"（Lemaitre 与 Hoffmann）——第一作者 Lemaitre，勿写反 |
| 早年证据链 | 证实 Metchnikoff 吞噬作用（注射 Bacillus thuringiensis 观察吞噬细胞增加）+X 射线处理与感染敏感性的造血关联——两实验都在博士阶段（Joly 实验室器官移植启发） |
| 在世者生卒 | 仅生年 1941-08-02，无卒年——封面用 1941– 开放区间 |
| 荣誉头衔 | 荣誉军团勋章 Commander（2012，此前 Officer）；橡树皇冠勋章 Grand Officer；旭日章金銀金星——级别与年份勿串 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| innate immunity | 先天免疫 | 获奖理由核心词 |
| Toll | Toll 受体/基因 | 果蝇之名；哺乳类同源为 Toll-like receptor（TLR） |
| Toll-like receptor (TLR) | Toll 样受体 | Beutler 发现哺乳类同源，勿归 Hoffmann |
| antimicrobial peptide | 抗菌肽 | Diptericin 等 |
| Diptericin | 双翅肽 | 82 残基、富含甘氨酸 |
| Drosomycin | 果蝇霉素 | 抗真菌肽，Toll 通路标志 |
| Imd pathway | Imd 通路 | 与 Toll 并行的另一抗菌通路 |
| NF-κB | 核因子 κB | 哺乳类与果蝇 Dorsal/Dif 的保守级联 |
| spätzle/Toll/cactus | 果蝇胚胎背腹轴基因盒 | 1996 论文标题骨架 |
| phagocytosis | 吞噬作用 | Metchnikoff 发现、Hoffmann 证实 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从 Metchnikoff 1880 年代的吞噬学到 1996 年 Toll 论文再到 2011 诺奖——先天免疫是被"重新发现"的百年主题；"Timeless" 匹配这条贯穿百年的免疫学主线与其在 CNRS 数十年如一日的坚守。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Jules_A._Hoffmann/Timeless.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
