# 医学家立传提示词（Godfrey Hounsfield）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1979 年得主（戈弗雷·豪斯菲尔德，CT 扫描的发明者之一）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Godfrey Newbold Hounsfield（1919-08-28 生于诺丁汉郡 Sutton-on-Trent ~ 2004-08-12 卒于大伦敦 Kingston upon Thames，享年 84 岁）
- **气质关键词**：**没有大学文凭的诺奖工程师、英国首台全晶体管计算机的设计参与者、以 Hounsfield 单位铭刻于医学的发明家** —— 1979 获奖理由（与 Allan MacLeod Cormack 两人共享）：
  > "for the development of computer assisted tomography"（因开发计算机辅助断层扫描）
- **设计母题**：**乡间漫步时的一瞥**。"绕着盒子从各角度拍 X 光就能看清盒内"的念头诞生于一次乡间远足——视觉隐喻：一条环绕物体的 X 射线束与逐层显影的"切片"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Godfrey_Hounsfield/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Godfrey_Hounsfield/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准——生日双值与 EMI 入职年份裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Godfrey_Hounsfield/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Godfrey_Hounsfield_zh`、`VIDEO_NAME=Godfrey_Hounsfield_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Godfrey_Hounsfield/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用现代腹部 CT 图。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Godfrey_Hounsfield.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | electrical engineering | 电气工程 | 本行；雷达/制导武器/EMIDEC 1100 | 早年页 |
| 1 | computed tomography | 计算机辅助断层扫描 | CT 原型机与全身扫描仪，1979 诺奖核心 | 核心页 |
| 2 | medical imaging | 医学成像 | 1971-10-01 首次临床应用 | 核心页 |
| 3 | computer engineering | 计算机工程 | 英国首台商用全晶体管计算机 EMIDEC 1100 | 履历页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Allan McLeod Cormack | 无向 | 1979 诺贝尔生理学或医学奖两人共享（计算机辅助断层扫描的开发） |

> **relations=1 为诚实值**——page.md 无任何师承/家庭/合作者细节（Hounsfield 终生未婚、无子女亦无记载），Review 勿误判缺漏。
> 不入库：父母 Thomas Hounsfield（Beighton 农场主，与 Hackenthorpe Hall 的 Hounsfield/Newbold 家族有渊源）与 Blanche Dilcock（家族叙事）；两名兄长两名姐姐；EMI 同事（未具名）。
> ★对手方名裁定：page.md 正文作 **Allan MacLeod Cormack**、citation json 作 "Allan M. Cormack"——yaml 取正文全名 `Allan MacLeod Cormack`（防未来与其本人批次记录分裂），此处记录供主控统一。

## 五、配色方案 【人物专属】

- **气质**：诺丁汉农场的机件铁灰 + X 光片的冷白 + 切片成像的层析蓝
- **主色**：层析蓝 `#1B5E8C`（CT 切片的层叠与冷静）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` CT 发明 — 层析蓝 `#1B5E8C`
  - `badgeB` Hounsfield 单位 — 琥珀 `#A0722D`
  - `badgeC` EMIDEC 计算机 — 灰紫 `#5C5470`
  - `badgeD` 农场少年与军旅 — 深绿 `#2F6B4F`
- **背景母题**：多层水平切片线（CT 层叠）自左向右渐次显影出圆形轮廓。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — CT 扫描的发明者 / Godfrey Hounsfield 1919–2004 + 四色 badge + 右上头像 + 国籍行 UK
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Sutton-on-Trent、教育 Magnus 学校/
    Faraday House 电气工程学院 DFH、无大学学位、任职 RAF/EMI 1949 起、
    荣誉 Nobel 1979/FRS 1975/爵士 1981、核心领域）
03  核心贡献概览 — CT 断层扫描 / Hounsfield 单位 / EMIDEC 1100 / 全身扫描仪
04  农场 tinkering 少年 (1919–1939) — 五子最幼、被农场上电器与机械迷住、
    自制电气录音机、干草堆自制滑翔机、水桶+电石水火箭"差点丧命"、
    Magnus 文法学校——"不学术"的学生
05  RAF 与 Faraday House (1939–1949) — 二战前以志愿预备役加入皇家空军、
    学得电子学与雷达基础、战后 Faraday House 电气工程学院 DFH 文凭
06  EMI 与 EMIDEC 1100 (1949–1958) — 1949-10-10 入 EMI（自传误写 1951，传记勘正）、
    制导武器与雷达研究、1958 参与设计英国首台商用全晶体管计算机 EMIDEC 1100
07  乡间漫步的一瞥 — "绕着盒子从各角度拍 X 光就能看清盒内"——
    构想一台从各角度采集 X 射线、由计算机重建"切片"图像的机器
08  不知情的平行者 — 当时并不知道 Cormack 已做过该设备的理论数学——两人独立的会合
09  原型机三部曲 — 头部扫描原型机：先测保存的人脑→再测肉铺新鲜牛脑→最后测自己
10  1971-10-01：临床首秀 — Atkinson Morley 医院（伦敦温布尔登）成功扫描
    脑囊肿患者——CT 进入医疗实践
11  1975：全身扫描仪 — 从头部到全身、Hounsfield 单位（HU：空气 -1000→水 0→
    致密皮质骨 +1000+）成为 CT 通用标尺
12  1979 诺贝尔奖 — 与 Cormack 两人共享官方理由逐字引用、
    1979 前荣誉：Exner Medal 1974/FRS 1975/Duddell 1976/Mullard 1977/Potts 1977
13  荣誉序列 — CBE 1976、爵士（1981 生日荣誉）、Gairdner、Lasker-DeBakey 临床奖、
    国家发明家名人堂、皇家外科医学院荣誉院士、Dennis Gabor Medal、John Scott Award、
    1994 皇家工程院荣誉院士
14  遗产 — 诺奖奖金在家建私人实验室、诺丁汉大学 Hounsfield 设施（2014，3-D CT 土壤成像）、
    CT 原理沿用至今、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for the development of computer assisted tomography"（与 Cormack 两人共享）；page.md 另有"his part in developing"口径——引用以 citation json 为准 |
| 生日双值 ★ | metadata 双值 1919-08-28 / 08-18；infobox 与正文均 **28 August 1919**——取 08-28 |
| EMI 入职年份 ★ | 自传误写 1951；传记勘正为 **1949-10-10**——page.md 明载此勘误，采用 1949 并可注明勘误 |
| 学历口径 | **无大学学位**：Magnus 文法学校"不学术"、RAF 学电子与雷达、Faraday House DFH 文凭（大学级专门电气工程学院）——"非学院派诺奖得主"是本篇最大反差，勿美化成名校出身 |
| 原型机顺序 | 保存的人脑 → 肉铺新鲜牛脑 → 自己——三部曲顺序勿错 |
| Hounsfield 单位 | −1000（空气）/0（水）/+1000+（致密皮质骨）——三个锚点数字勿错 |
| Cormack 独立性 | Hounsfield 构想时**不知** Cormack 的理论数学工作——独立会合口径保留 |
| 对手方名裁定 ★ | yaml 取 page.md 正文全名 `Allan MacLeod Cormack`（citation json 缩写作 "Allan M. Cormack"）——若其本人批次用缩写形，主控统一时合并 |
| 单身终身 | page.md 无婚姻/子女记载，relations=1 系诚实值；遗产：诺奖奖金建私人实验室、诺丁汉大学 Hounsfield 设施（2014，土壤 3-D CT） |
| 军旅口径 | 二战前志愿预备役加入 RAF——"volunteer reservist"口径，勿写成正式参军 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| computed tomography (CT) | 计算机辅助断层扫描 | 获奖理由核心词 |
| Hounsfield scale / HU | Hounsfield 标尺/单位 | −1000/0/+1000 锚点 |
| radiodensity | 放射密度 | HU 度量的对象 |
| EMIDEC 1100 | EMIDEC 1100 计算机 | 英国首台商用全晶体管计算机 |
| Faraday House | 法拉第学院 | 大学级电气工程专门学院 |
| EMI, Ltd. | EMI 公司 | 1949 入职 Hayes |
| Atkinson Morley Hospital | 阿特金森·莫利医院 | 1971 临床首秀地 |
| DFH | 法拉第学院文凭 | 其最高学历 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配）
- **风格**：沉稳 / 纪录片 / 长期纲领
- **匹配理由**：从农场少年到 CT 原理沿用至今——Timeless 的沉稳纪录片感匹配"一项发明定义一个世纪医学影像"的时间纵深；"时无英雄"的非学院派人生也在沉稳曲调中显得从容。
- **本地路径**：`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → 复制为 `presentations/20th_century/Godfrey_Hounsfield/Timeless.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；生日/EMI 年份勘正与"无大学学位"反差务必保留。**
