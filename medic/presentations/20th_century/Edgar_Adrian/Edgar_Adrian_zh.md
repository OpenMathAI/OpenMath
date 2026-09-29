# 医学家立传提示词（Edgar Adrian）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1932 年**得主（与 Charles Scott Sherrington 共享）。
> 本文件是 Adrian 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Edgar Douglas Adrian, 1st Baron Adrian（1889-11-30 ~ 1977-08-04，享年 87 岁），英国电生理学家
- **气质关键词**：**听见神经电声音的人、全或无定律的实验证人、三一学院之主** —— 1932 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for their discoveries regarding the functions of neurons"（因其关于神经元功能的发现）
- **设计母题**：**扬声器里的神经脉冲（spikes in the loudspeaker）**。1928 年暗室里，Adrian 从与放大器相连的扬声器中「听见」蛙眼视神经在报告自己的动作——以声波纹与脉冲尖峰作为全篇视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Edgar_Adrian/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Edgar_Adrian/`；Makefile 复制后设 `MAIN=Edgar_Adrian_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | electrophysiology | 电生理学 | 1932 诺奖核心：单神经纤维电记录 | 核心页 |
| 1 | physiology | 生理学 | 剑桥生理学教席（1937-1951） | 任职页 |
| 2 | neuroscience | 神经科学 | 感觉映射、脑电图、嗅觉晚年研究 | 研究页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Charles Scott Sherrington | 无向 | 1932 诺贝尔生理学或医学奖共享（神经元功能发现） |
| spouse | Hester Agnes Pinsent | 无向 | 1923-06-14 结婚；Ellen Pinsent 之女 |
| influence | Keith Lucas | 无向 | 续其「全或无」研究并以毛细管静电计放大神经信号 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：工程师的精确、剑桥的优雅、电信号的锐利
- **主色**：`#1E4E79`（剑桥蓝，三一学院）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：
  - `badgeSpike` 神经脉冲 — 电光橙 `#D07B2A`
  - `badgeAllNone` 全或无定律 — 靛蓝 `#3B4E8C`
  - `badgeEEG` 脑电与感官地图 — 神经青 `#1B7A6B`
  - `badgeTrinity` 三一学院 — 深酒红 `#6E1E2B`
- **背景母题**：剑桥蓝底上稀疏的脉冲尖峰序列（细竖线 + 顶点亮圆），如扬声器波形散布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 听见神经的人 / Edgar Adrian 1889–1977 + 四色 badge + 右上肖像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Hampstead、Westminster/三一学院、任职、荣誉）
03  核心贡献概览 — 全或无定律 / 单纤维记录 / 感官适配 / 脑电
04  早年与三一学院 (1889–1915) — Hampstead 出生、1911 毕业、1913 因「全或无」研究当选三一研究员
05  战地医官 (1915–1919) — St Bartholomew's 医院治神经损伤与弹震症伤员
06  续写 Keith Lucas (1919–1925) — 毛细管静电计 + 阴极射线管放大、1919 返剑桥讲师
07  1928 暗室的意外（核心贡献页）— 蟾蜍视神经扬声器原话、单神经纤维放电记录
08  全或无与频率编码 — 恒定刺激下脉冲强度不变而频率递减、感官适配机制
09  感觉皮层地图 — 痛觉信号接收、体感皮层空间分布、homunculus 观念之源
10  脑电与嗅觉 — Berger 节律异常研究为癫痫铺路、晚年转向嗅觉
11  1932 诺贝尔奖 — 与 Sherrington 共享、1934 Royal Medal / 1946 Copley
12  荣衔与职守 — Foulerton 教授 1929-37、剑桥生理学教授 1937-51、皇家学会会长 1950-55、三一院长 1955-65
13  男爵与校长 — 1955 封 Baron Adrian、剑桥校长 1967-75、Leicester 校长 1957-71
14  遗产：从单纤维记录到现代神经科学 — 频率编码进入教科书、感觉映射的后续
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | "for their discoveries regarding the functions of neurons"——**their**（与 Sherrington 共享）；Adrian 侧重点是单纤维电记录与频率编码 |
| 全名与头衔 | 全名 Edgar Douglas Adrian、1955 封 1st Baron Adrian（剑桥男爵）；行文可用 Lord Adrian，首次出现用全名 |
| 1928 原话 | 蟾蜍视神经扬声器段为正文引语（"I had arranged electrodes on the optic nerve of a toad..."）——引原话须用此段，勿自造 |
| 「全或无」归属 | 定律非其首创：1913 当选三一研究员是因对其研究；Adrian 提供的是实验证据并续 Keith Lucas 之业——功劳表述区分 |
| Lucas 关系 | 正文只说 "Continuing earlier studies of Keith Lucas"，未言师承——用 influence 而非 advisor-student |
| 家庭 | 1923 娶 Hester Agnes Pinsent；三子女（Anne 嫁生理学家 Richard Keynes——达尔文玄孙、Richard 2nd Baron、Jennet）——正文有载；本批仅入库配偶，子女边留待主控口径 |
| Berger 关系 | 研究的是「Berger 节律」，与 Hans Berger 无直接共事记载——不建关系边，此处注明 |
| 职务年代 | 皇家学会会长 1950-55（第 49 任）、三一院长 1955-65、剑桥校长 1967-75、Leicester 校长 1957-71——四个年份勿混 |
| 战时临床 | 一战在 St Bartholomew's 治神经损伤与 shell shock——是其神经兴趣的临床源头 |
| 实验动物 | 蛙/蟾蜍（正文括注 "It seems he used frogs in his experiments"）——表述留余地 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| all-or-none law | 全或无定律 | Adrian 提供实验证据，非其首创 |
| nerve impulse | 神经冲动 | 单纤维放电记录 |
| frequency coding | 频率编码 | 强度恒定而频率递减的适配 |
| sensory adaptation | 感官适配 | 1928 关键结果 |
| homunculus | 小人图 | 体感皮层感觉地图观念之源 |
| capillary electrometer | 毛细管静电计 | 其记录工具 |
| cathode-ray tube | 阴极射线管 | 信号放大显示 |
| Berger rhythm | Berger 节律（脑电 α 波） | 其异常研究为癫痫铺路 |
| olfaction | 嗅觉 | 晚年研究方向 |
| electrophysiology | 电生理学 | 其本业 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（manifest 预分配）
- **风格**：进取 / 探险 / 叙事推进
- **匹配理由**：Adrian 的工作是把放大器探针插进生命信号的核心地带——从战地医官到「听见神经」再到皇家学会之巅，是一条清晰的进取弧线；Expedition 的行进感匹配其 1928 年暗室突破的探险气质（第二次使用该曲，首用 Cajal，同为神经科学远征者遥相呼应）。
- **本地路径**：`music_audio/` 下 Expedition 曲目 → 复制为 `presentations/20th_century/Edgar_Adrian/Expedition.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
