# 医学家立传提示词（Joseph Murray）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1990 年得主 Joseph Murray（约瑟夫·爱德华·默里）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Joseph_Murray/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Joseph Edward Murray（1919-04-01 生于马萨诸塞州米尔福德 ~ 2012-11-26 逝于波士顿，享年 93 岁），美国整形外科医生，"移植之父"，彼得·本特·布里格姆医院
- **气质关键词**：**首例成功人体器官移植的执刀者、脑死亡标准的定义者之一、以手术医治灵魂的外科圣手**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1990 条目，Murray/Thomas 两人共享）：
  > "for their discoveries concerning organ and cell transplantation in the treatment of human disease"（因其关于器官与细胞移植治疗人类疾病的发现）
- **设计母题**：**一只跨越孪生兄弟身体的肾脏（first kidney transplant, 1954-12-23）**；用「手术灯下的肾脏与连接的血管弧线」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Joseph_Murray/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Joseph_Murray/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Joseph_Murray_zh`、`VIDEO_NAME=Joseph_Murray_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Murray 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | organ transplantation | 器官移植 | 首例成功肾移植、免疫抑制方案、1990 诺奖核心 | 核心页 |
| 1 | plastic surgery | 整形外科 | 二战烧伤重建起步、真正的毕生热爱 | 职业页 |
| 2 | reconstructive surgery | 修复重建外科 | 儿童先天畸形与烧伤（波士顿儿童医院 1972-85） | 职业页 |
| 3 | transplant immunology | 移植免疫 | 排斥机制、供体健康与器官买卖反对立场 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Bradford Cannon | 对方 → 导师 | 二战 Valley Forge 总医院整形外科单元在其麾下，整形外科启蒙 |
| colleague | J. Hartwell Harrison | 无向 | 1954-12-23 首例成功肾移植（Herrick 孪生兄弟）的协作外科医生 |
| colleague | George H. Hitchings | 无向 | 合作将硫唑嘌呤（Imuran）定制用于移植免疫抑制 |
| colleague | Gertrude B. Elion | 无向 | 合作将 6-MP 衍生物发展为首个免疫抑制药 |
| co-honored | E. Donnall Thomas | 无向 | 1990 诺贝尔生理学或医学奖共享（器官与细胞移植治疗人类疾病） |
| spouse | Virginia Link | 无向 | Virginia "Bobby" Link，1945-06 结婚，育六子 |

**诚实值说明**：Murray 页无具名学生/学生段，relations=6 为诚实值；"启发全球移植领袖"为总括叙述。

**不入库但提示词可叙述**：Herrick 孪生兄弟 Ronald 与 Richard（供体与受体，患者非科研关系——但却是叙事核心，第 8 页专述）；Charles Woods（70% 烧伤飞行员，24 次手术——"决定我一生"引语的主人公）；Alexis Carrel（1912 诺奖得主、"生物力"阻隔移植论的参照）；Robert Ebert/William Sweet/Raymond Adams/William J. Curran（1967 脑死亡委员会同僚）。

## 五、配色方案 【人物专属】

- **气质**：手术灯的无影白、战后重建的暖意、天主教信仰的沉静
- **主色**：`#7A2430`（深砖红——心脏与血管的生命之色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeTrans` 首例肾移植 — 深砖红 `#7A2430`
  - `badgePlastic` 整形重建 — 深蓝 `#1E4E79`
  - `badgeEthics` 伦理与脑死亡 — 深青 `#0E7490`
  - `badgeHonor` 荣誉传承 — 赭金 `#B07D2B`
- **背景母题**：手术灯光环与移植血管弧线，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 移植之父 / Joseph Murray 1919–2012 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、米尔福德出身、圣十字学院/哈佛 MD 1943、
    Peter Bent Brigham 医院/波士顿儿童医院任职、诺奖 1990、核心领域；爱尔兰+意大利移民家庭注脚）
03  核心贡献概览 — 首例肾移植 1954 / 首例异体移植 1959 / 首例尸体供肾 1962 / 脑死亡标准 1967
04  米尔福德的运动员 (1919–1943) — 橄榄球冰球棒球、家庭医生点燃外科志向、
    圣十字学院古典学（希腊拉丁英文哲学）、哈佛 MD 1943
05  战火中的整形外科 (1944–1947) — Valley Forge 总医院、Bradford Cannon 门下、
    数千伤员的手与脸重建、烧伤异体植皮排斥缓慢的观察
06  Charles Woods 的启示（核心贡献页）— 70% 烧伤飞行员、24 次手术、尸体皮肤赢得自体皮时间、
    "决定我一生的问题与教训"引语
07  1954-12-23：首例成功肾移植（核心贡献页）— Herrick 孪生兄弟、手术 5.5 小时、
    Harrison 协助、Richard 多活 8 年结婚生子、Ronald 供体无恙活过 50 年
08  1959 与 1962：打破孪生限制 — 全身照射下首例成功异体移植（非同卵兄弟，存活 28 年）、
    与 Hitchings/Elion 合作定制 Imuran、1962 首例尸体供肾移植
09  移植的制度化 — 1962 首届国际肾移植会议、国家肾脏登记处（UNOS 前身）、
    反对器官买卖、活体供体健康研究
10  1967：定义脑死亡 — Ebert 召集的哈佛委员会（Sweet/Adams/Curran）→1981 UDDA
11  回到最初的爱 (1971–1986) — 辞去移植外科主任、波士顿儿童医院整形外科主任 1972-85、
    儿童先天畸形与烧伤、1986 荣休
12  1990 诺奖：与 Thomas 共享 — 获奖理由逐字呈现、Murray 器官移植/Thomas 骨髓细胞移植
13  荣誉与认可 — NAS 院士、Amory 奖、Golden Plate 1991、梵蒂冈宗座科学院 1996、
    Laetare Medal 2005、波士顿 350 杰出公民
14  遗产与结尾 — Surgery of the Soul 自传、感恩节当天在首例移植同一家医院辞世 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | **yaml/入库用 manifest 形式 "Joseph Murray"**；citation json 名 "Joseph E. Murray (1919–2012)"；封面写 Joseph E. Murray |
| 1990 两人分工 | **Murray=器官移植（肾）、Thomas=细胞移植（骨髓）**——同一句获奖理由下两条路线，勿混写；Thomas 由 med-batch-31 建档（本批已预建 stub） |
| 首例日期与细节 | 1954-12-23、Peter Bent Brigham 医院手术室 2、5.5 小时、Ronald→Richard 孪生兄弟、Richard 术后存活 8 年、Ronald 活过 50 年——数字勿串 |
| 与 Hitchings/Elion 边 | 三方合作定制 azathioprine/Imuran 用于移植——两条 colleague 边（Hitchings+Elion），是 1988 诺奖成果与 1990 诺奖成果的交汇点，叙述时双向呼应 |
| 古典学出身 | 圣十字学院主修希腊语/拉丁语/英语/哲学（非理科！）——"文科生的外科大师"反差叙事，勿写成医科预科 |
| Charles Woods 引语 | "The questions raised and lessons learned in trying to help Charles would determine the course of the rest of my professional life."——page.md 明载英文原话，可引 |
| 天主教与伦理 | 虔诚天主教徒、首例移植前咨询各宗派神职人员伦理问题、1996 梵蒂冈宗座科学院院士、2005 Laetare Medal（圣母大学表彰对教会与社会的服务）——可写，宗教线是其人物底色 |
| 反对器官买卖 | 对金钱化器官交易的"明确反对"（unequivocal opposition）——立场句 page.md 明载 |
| 职年链 | 哈佛 MD 1943 → Brigham 实习 → 1944-47 军队 → 通用外科住院医师 → 纽约整形训练 → 1951 Brigham 外科 staff → 移植外科主任 1951-71 → 儿童医院整形外科主任 1972-85 → 1986 荣休（小中风康复后）——勿串 |
| 死亡诗意 | 2012-11-26（感恩节）逝于 Brigham and Women's 医院——正是 1954 年首例移植的同一家医院——结尾页的天然闭环 |
| 引语清单 | Charles Woods 句（明载）；其余无直接引语，禁编 |
| 脑死亡委员会 | 1967 年 Ebert 召集：Sweet（神经外科）/Adams（神经科）/Curran（法学）与 Murray——致 1981 UDDA；成员为同僚不入库 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| organ and cell transplantation | 器官与细胞移植 | 获奖理由逐字对应 |
| kidney transplantation | 肾移植 | 首例成功人体器官移植 |
| allograft | 异体移植 | 1959 首例成功（非同卵） |
| cadaveric donor | 尸体供肾 | 1962 首例 |
| azathioprine (Imuran) | 硫唑嘌呤 | 与 Hitchings/Elion 合作定制 |
| 6-Mercaptopurine | 6-巯基嘌呤 | Imuran 的母体药物 |
| immunosuppressive agents | 免疫抑制药 | 打破排斥壁垒的关键 |
| brain death | 脑死亡 | 1967 哈佛委员会定义 |
| autograft | 自体皮移植 | Charles Woods 病例用语 |
| United Network for Organ Sharing (UNOS) | 器官共享联合网络 | 其国家肾脏登记处的后身 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Empire Collapse**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Murray 推倒的是医学史上最古老的"帝国"——免疫排斥不可逾越的定论（连 Carrel 的诺奖权威都如此断言）；Empire Collapse 的宏大崩塌感对应旧教条在新证据前的瓦解，也对应一台手术改写现代医学疆域的重量，以及这位外科医生在感恩节安然谢幕的终章。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Joseph_Murray/EmpireCollapse.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
