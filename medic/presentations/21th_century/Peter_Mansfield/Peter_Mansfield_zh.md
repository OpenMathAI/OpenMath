# 医学家立传提示词（Peter Mansfield）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2003 年得主 Peter Mansfield（彼得·曼斯菲尔德）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Peter_Mansfield/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Peter Mansfield（1933-10-09 生于伦敦 Lambeth ~ 2017-02-08 逝于诺丁汉，享年 83 岁），FRS，1993 年受封 Knight Bachelor
- **气质关键词**：**15 岁辍学的印刷学徒、自测第一台全身 MRI 的教授、回波平面成像之父**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2003 条目，Lauterbur/Mansfield 两人共享）：
  > "for their discoveries concerning magnetic resonance imaging"（因其关于磁共振成像的发现）
- **设计母题**：**层层选片与快速回波（slice selection & echo-planar imaging）**——从整块人体中"选出"一层截面、再让信号以回波平面方式飞速成图；用「多层截面片叠加」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Peter_Mansfield/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Peter_Mansfield/`（世纪目录一律 `21th_century`，肖像见 images.txt）。Makefile 复制后设 `MAIN=Peter_Mansfield_zh`、`VIDEO_NAME=Peter_Mansfield_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Mansfield 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | magnetic resonance imaging | 磁共振成像 | 选片与回波平面成像，2003 诺奖核心 | 核心页 |
| 1 | nuclear magnetic resonance | 核磁共振 | Queen Mary 起步，脉冲 NMR 谱仪 | 教育页 |
| 2 | physics | 物理学 | 诺丁汉大学物理系教授（1979） | 职业页 |
| 3 | biophysics | 生物物理学 | metadata occupation 有载 | 身份页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Jack Powles | 对方 → 导师 | 伦敦大学 Queen Mary 学院博士导师（1962，固体中质子磁共振弛豫） |
| advisor-student | Charles Pence Slichter | 对方 → 博士后合作者 | 伊利诺伊大学厄巴纳-香槟分校博士后（掺杂金属 NMR 研究；库内 id=2179） |
| co-honored | Paul Lauterbur | 无向 | 2003 诺贝尔生理学或医学奖共享（关于磁共振成像的发现） |
| spouse | Jean Margaret Kibble | 无向 | 1962-09-01 结婚，育二女 |

**不入库但提示词可叙述**：John Mallard 与 Jim Hutchinson（1990 Mullard Award 共同得主，奖项合作非科研关系）；父母 Sidney George Mansfield 与 Lillian Rose Turner；两位兄长；2009 年颁奖的 Gordon Brown。

## 五、配色方案 【人物专属】

- **气质**：伦敦东区工人的坚韧、诺丁汉的严谨、第一次躺进磁体的勇气
- **主色**：`#35506B`（石板蓝——诺丁汉石墙与磁体冷光）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeSlice` 选片成像 — 石板蓝 `#35506B`
  - `badgeEPI` 回波平面成像 — 深青 `#14647E`
  - `badgeFast` 快速成像/fMRI — 琥珀 `#B07D2B`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：平行的轴向截面片与回波信号曲线，稀疏错落。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 回波平面成像之父 / Peter Mansfield 1933–2017 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、伦敦 Lambeth 出身、Queen Mary 学院、
    诺丁汉大学任职、诺奖 2003、核心领域）
03  核心贡献概览 — 选片技术 / 信号数学解析 / 回波平面成像 / 首台全身扫描自测
04  伦敦东区少年 (1933–1948) — 战时疏散 Sevenoaks 与 Torquay、11+ 落榜、15 岁被断言"不适合科学"
05  印刷学徒与火箭 (1948–1952) — 印刷助理、火箭推进部岗位、两年义务兵役
06  夜校与 Queen Mary (1950s–1959) — 夜读 A-level、物理学士、Powles 门下的地磁 NMR 谱仪
07  博士与博士后 (1959–1964) — 脉冲 NMR 研究固体聚合物、1962 PhD、UIUC Slichter 处研究掺杂金属
08  诺丁汉之路 (1964–1979) — 讲师→高级讲师→Reader→教授、MRC 经费支持 MRI 设备研制
09  选片与信号解析（核心贡献页）— slice selection、MRI 信号的数学分析、频率/相位编码
10  回波平面成像 EPI（核心页）— T2* 加权图像数倍提速、使 fMRI 成为可能
11  1978：第一台全身扫描与自测 — 圣诞节前装机、自愿躺入、首例活体扫描、原型机藏于科学博物馆
12  2003 诺奖：与 Lauterbur 接力 — 同一句获奖理由、Lauterbur 开创→Mansfield 提速的接力结构
13  荣誉与认可 — FRS 1987、爵士 1993、Mullard 1990、ISMAR 1992、Gordon Brown 终身成就奖 2009
14  遗产与结尾 — EPI 与 fMRI 的日常化、小行星 Petermansfield + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名形式 | 全名 Sir Peter Mansfield，**yaml/入库用 manifest 形式 "Peter Mansfield"** |
| 2003 共享的结构 | 与 Lauterbur 共享同一句获奖理由；关系是**技术接力**（Lauterbur 的投影重建法慢且易生伪影→Mansfield 换成频率/相位编码+傅里叶变换提速），勿写成共同实验或师承 |
| 15 岁辍学叙事 | 15 岁被职业教师告知"科学不适合他"、辍学当印刷助理——与 2003 诺奖形成反差主线；11+ 考试落榜细节 page.md 明载 |
| 博士导师与博士后 | 博士导师 Jack Powles（Queen Mary，1962 年 PhD）；博士后为 UIUC 的 Charlie Slichter——两条 advisor-student 边并行，Slichter 入库用规范名 "Charles Pence Slichter" |
| 履历年份链 | 1959 学士→1962 博士→1962-64 UIUC→1964 诺丁汉讲师→1968 高级讲师→1970 Reader→1972-73 海德堡马普医学研究所 Senior Visitor→1979 教授→1994 退休——勿串 |
| Mullard Award | 1990 年与 John Mallard、Jim Hutchinson 三人共享——奖项共享勿写成科研合作 |
| ISMAR 奖 | 1992 ISMAR 奖与 P. Lauterbur 共同获得——是诺奖之外的早期共同荣誉，可与 2003 共享诺奖分开叙述 |
| 首例活体扫描 | 1978 年圣诞前诺丁汉装机首台全身原型，Mansfield **自愿躺入自测**并完成首例活体扫描；原型机现存伦敦科学博物馆医学展区 |
| EPI 与 fMRI | 回波平面成像使 T2* 加权图像采集大幅提速，进而使 fMRI 可行——因果链 page.md 明载，勿把 fMRI 发明权单独归他 |
| 死亡地与年龄 | 2017-02-08 逝于诺丁汉，享年 83 岁 |
| 荣誉年份 | FRS 1987、爵士 1993、SMRM 金奖 1983、皇家学会 Wellcome 基金会金奖 1984（共同）、Duddell 1988、Mullard 1990、2009 Pride of Britain 终身成就奖（Gordon Brown 颁）、小行星 262972 Petermansfield（2016 命名）——年份勿串 |
| 国籍口径 | 英格兰物理学家；出生地 Lambeth、成长地 Camberwell、逝地诺丁汉，三地勿混 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| magnetic resonance imaging (MRI) | 磁共振成像 | 获奖理由核心词 |
| slice selection | 选片 | 局部轴向截面选择性成像，Mansfield 贡献 |
| echo-planar imaging (EPI) | 回波平面成像 | 快速成像协议，使 fMRI 可行 |
| T2*-weighted imaging | T2* 加权成像 | EPI 的主要加权方式 |
| functional MRI (fMRI) | 功能磁共振成像 | EPI 使其可行 |
| pulsed NMR spectrometer | 脉冲核磁共振谱仪 | 博士阶段自建，研究固体聚合物 |
| proton magnetic resonance relaxation | 质子磁共振弛豫 | 博士论文主题（1962） |
| projection-reconstruction | 投影重建 | Lauterbur 原始方法，被其取代 |
| frequency and phase encoding | 频率与相位编码 | 梯度场下的编码方法 |
| Earth's field NMR | 地磁场核磁共振 | 本科毕业设计（便携谱仪测地磁场） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从 15 岁辍学学徒到 83 岁辞世的诺奖教授，Mansfield 的一生是"时间之流"的最佳注脚——夜校的漫长坚持、1978 年躺入自测的一瞬、EPI 把成像时间压缩数倍，慢与快的张力贯穿始终。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Peter_Mansfield/TheFlowOfTime.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
