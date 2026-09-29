# 医学家立传提示词（Albert Claude）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1974 年得主 Albert Claude（阿尔伯特·克劳德）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Albert_Claude/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Albert Claude（1899-08-24 生于比利时 Longlier ~ 1983-05-22 逝于布鲁塞尔，享年 83 岁），比利时-美国细胞生物学家、医学博士，现代细胞生物学奠基人之一
- **气质关键词**：**细胞分级分离之父、生物电子显微术第一人、细胞器世界的哥伦布**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1974 条目，Claude/de Duve/Palade 三人共享）：
  > "for their discoveries concerning the structural and functional organization of the cell"（因其关于细胞结构与功能组织的发现）
- **设计母题**：**离心管里的细胞分层（cell fractionation）**——把细胞磨碎、离心、按质量分层，让每个细胞器各就其位；用「离心管中的分层色带」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Albert_Claude/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Albert_Claude/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Albert_Claude_zh`、`VIDEO_NAME=Albert_Claude_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Claude 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cell biology | 细胞生物学 | infobox Fields；1974 诺奖学科 | 全篇 |
| 1 | biochemistry | 生物化学 | 分离劳氏肉瘤病毒组分为核糖核蛋白（RNA） | 核心页 |
| 2 | electron microscopy | 生物电子显微术 | 首个把电镜用于生物细胞（1945 线粒体结构） | 核心页 |
| 3 | virology | 病毒学 | 1938 首次纯化劳氏肉瘤病毒致病组分 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Christian de Duve | 无向 | 1974 诺贝尔生理学或医学奖三人共享 |
| co-honored | George Emil Palade | 无向 | 1974 诺贝尔生理学或医学奖三人共享 |
| advisor-student | George Emil Palade | Claude → 学生 | 其学生（Claude 页明载 his student），1970 Horwitz 奖同获 |
| colleague | Keith R. Porter | 无向 | 与助手 Porter 发现内质网（鱼网状结构） |
| colleague | Emil Mrena | 无向 | 紧密合作者（1969-1974 合著 5 篇），助其家庭离开捷克斯洛伐克 |
| colleague | Christian de Duve | 无向 | 同事与挚友，1972 助其任卢万天主教大学教授 |
| spouse | Julia Gilder | 无向 | 1935 年结婚，洛克菲勒期间离婚 |
| parent-child | Philippa Claude | 无向 | 女儿，神经科学家，嫁 Antony Stretton |

**不入库但提示词可叙述**：Simon Flexner（1929 接受其洛克菲勒申请的所长，招募事件）；Albert Fischer（柏林 Kaiser Wilhelm 研究所组织培养实验室博士后东家，访问性质不入库）；Marcel Florkin（促成退伍军人入学法案的教育官员）；画家 Diego Rivera/Paul Delvaux 与音乐家 Varèse（挚友圈，非科研关系，身份页可点一笔）。

## 五、配色方案 【人物专属】

- **气质**：离心管的金属冷光、比利时阿登森林的沉绿、电镜荧屏的微蓝
- **主色**：`#2F4470`（隐蓝——离心分层与细胞内部世界）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeFrac` 细胞分级分离 — 隐蓝 `#2F4470`
  - `badgeEM` 生物电镜 — 青灰 `#0E7490`
  - `badgeVirus` 劳氏肉瘤病毒 — 暗红 `#7A2430`
  - `badgeOrganelle` 细胞器发现 — 赭金 `#B07D2B`
- **背景母题**：离心管分层色带与细胞器剪影，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 细胞分级分离之父 / Albert Claude 1899–1983 + 四色 badge + 右上头像 + 国籍行（Belgium）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Longlier 出身、列日大学 MD 1928、
    洛克菲勒/居里·博尔代研究所/布鲁塞尔自由大学/卢万任职、诺奖 1974、核心领域）
03  核心贡献概览 — 细胞分级分离 1930 / 劳氏肉瘤病毒 1938 / 生物电镜 1945 / 细胞器图谱
04  阿登少年与一战 (1899–1922) — 牧师家庭出身的面包师之子、母早逝、辍学照料叔父、
    受丘吉尔感召参加抵抗运动加入英国情报部门、两度入集中营、Interallied 奖章
05  列日大学 (1922–1928) — 退伍军人免试入学法案（Florkin 主政）破格录取、1928 MD
06  柏林与洛克菲勒 (1928–1929) — 小鼠肿瘤移植论文旅行资助、Fischer 组织培养实验室、
    Flexner 接纳其劳氏肉瘤病毒分离提案
07  1930：细胞分级分离（核心贡献页）— 研磨-过滤-离心-分层的完整方法论
08  劳氏肉瘤病毒与微粒体（核心页）— 1938 纯化"核糖核蛋白"（即 RNA）、微粒体后更名核糖体
09  电镜下的细胞内部 — 1945 线粒体结构、与 Porter 发现内质网、线粒体=细胞动力厂
10  1949 回比利时：居里·博尔代研究所 — 所长兼布鲁塞尔自由大学教授、1971 荣休
11  Mrena 与卢万晚年 — 布拉迪斯拉发电镜会议结识、助其脱离铁幕、Louvain-la-Neuve 实验室
12  1974 诺奖：三人共享 — 与学生 Palade、挚友 de Duve 共享，获奖理由逐字呈现
13  荣誉与认可 — Baron Holvoet 1965、Horwitz 1970、Paul Ehrlich 1971、法国科学院/比利时王家院士、
    Léopold II 大绶勋章
14  遗产与结尾 — 现代细胞生物学的地基、隐居研究至 1983 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生年双值裁定 | metadata 四值（1898/1899 各两说）；page.md 正文与 infobox 均 1899-08-24——**以正文 1899-08-24 为准**（ civil register 1898 之说可注一句） |
| 国籍口径 | Citizenship Belgium and United States（1941 入籍）；citation json "Belgium United States"——双入，封面国籍行 Belgium |
| 独有叙事：一战间谍 | 参加抵抗运动、服务于英国情报部门、两度被关集中营、获 Interallied Medal 与退伍军人身份——是"免试入学"的因果起点，勿删 |
| 免试入学机制 | Florkin 任高等教育局长时通过法案使退伍军人免文凭入学——因果链 page.md 明载，勿写成"天赋破格" |
| 无导师边 | 列日 MD 1928、柏林博士后（Fischer 实验室）——page.md 未载博士导师，**不建 advisor-student 边**（Fischer 仅访问性质） |
| Palade 边方向 | Claude 页明载 "his student George Palade"——Claude→Palade 学生边；同时 Palade 页明载"met Claude 后加入其实验室"——两侧口径一致 |
| 微粒体=核糖体 | Claude 命名 "microsomes"（富 RNA 颗粒），后被更名 ribosomes——表述"后更名"，勿写成他直接发现核糖体 |
| 1945 双 first | 1945 首次电镜研究生物细胞（线粒体结构）+ 1945 发表首张细胞精细结构——两个"第一"都在 1945 |
| 引语红线 | 正文仅一处引语：小学教育 "excellent"——可小字用；其余无引语，禁编 |
| 去世口径 | 1983-05-22（周日夜）逝于布鲁塞尔家中自然原因；1976 起已因体弱不再去实验室——"隐居研究"叙事以此为准 |
| 政治元素 | 一战情报工作与 Mrena 脱离共产主义捷克斯洛伐克——均为 page.md 实载；前者客观一句，后者一句带过即可，勿展开冷战渲染 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| structural and functional organization of the cell | 细胞的结构与功能组织 | 获奖理由逐字对应 |
| cell fractionation | 细胞分级分离 | 研磨→过滤→离心→分层方法学 |
| Rous sarcoma virus | 劳氏肉瘤病毒 | 1938 纯化其组分 |
| ribose nucleoprotein | 核糖核蛋白 | 即 RNA 的早期命名 |
| microsomes | 微粒体 | 后更名为核糖体 |
| endoplasmic reticulum | 内质网 | 拉丁文"鱼网"，与 Porter 共同发现 |
| mitochondrion | 线粒体 | "细胞动力厂"表述 |
| electron microscopy | 电子显微镜技术 | 首次用于生物细胞 |
| Institut Jules Bordet | 居里·博尔代研究所 | 布鲁塞尔癌症研究治疗所，1949 任所长 |
| Interallied Medal | 协约国奖章 | 一战服役荣誉 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Claude 的少年是一部苦难史诗——丧母、辍学、照料瘫痪的叔父、两进集中营；然而正是从战火里走出来的人，用一台离心机把生命的最小单元层层铺开。Tragedy 的深沉对应其前半生的暗色，也让后半生"在碎片中重建细胞秩序"的成就更显重量。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Albert_Claude/Tragedy.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
