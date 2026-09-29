# 医学家立传提示词（Edward Calvin Kendall）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1950 年得主 Edward Calvin Kendall（爱德华·卡尔文·肯德尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Edward_Calvin_Kendall/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Edward Calvin Kendall（1886-03-08 生于康涅狄格州南诺沃克 ~ 1972-05-04 逝于新泽西州普林斯顿，享年 86 岁）
- **气质关键词**：**甲状腺素的分离者、可的松的化学缔造者、Mayo 生化掌门**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1950 条目，三人共享同句）：
  > "for their discoveries relating to the hormones of the adrenal cortex , their structure and biological effects"（因其关于肾上腺皮质激素的结构与生物学效应的发现）
- **设计母题**：**从腺体到晶体（from gland to crystal）**——分离甲状腺素、结晶谷胱甘肽、析出肾上腺皮质类固醇；用「腺体剪影渐变为分子晶体结构」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Edward_Calvin_Kendall/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Edward_Calvin_Kendall/`（1950 年像，见 images.txt）。Makefile 复制后设 `MAIN=Edward_Calvin_Kendall_zh`、`VIDEO_NAME=Edward_Calvin_Kendall_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Kendall 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | Mayo 生化部主任；1950 诺奖核心 | 封面、核心页 |
| 1 | endocrinology | 内分泌学 | 肾上腺皮质激素（Compound E→cortisone）与甲状腺素 | 核心页 |
| 2 | thyroid research | 甲状腺研究 | 分离甲状腺素（其自认最重要发现） | 核心页 |
| 3 | structural biochemistry | 结构生物化学 | 谷胱甘肽结晶与结构鉴定团队 | 成果页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Philip Showalter Hench | 无向 | Mayo Clinic 同事：Kendall 分离的 Compound E 由 Hench 用于类风湿关节炎治疗并命名 cortisone |
| co-honored | Philip Showalter Hench | 无向 | 1950 诺贝尔生理学或医学奖共享（官方理由句同一） |
| co-honored | Tadeus Reichstein | 无向 | 1950 诺贝尔生理学或医学奖共享（官方理由句同一）；1951 两人又共享爱丁堡 Cameron Prize |
| spouse | Rebecca Kennedy | 无向 | 1915 结婚，育四子女；妻 1973 去世 |

**不入库但提示词可叙述**：四名子女（page.md 仅具数量）；Parke-Davis / St. Luke's Hospital / Mayo / Princeton 的机构同僚；谷胱甘肽团队其他成员（"along with associates" 未具名）。

## 五、配色方案 【人物专属】

- **气质**：化学的晶体感、Mayo 实验室的克制、双激素（甲状腺+肾上腺）的纵深
- **主色**：`#8B1A1A`（结晶深红——甲状腺素碘化结晶与实验室的恒久之火）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeThyr` 甲状腺素分离 — 深红 `#8B1A1A`
  - `badgeCort` 可的松合成线 — 深金 `#B8860B`
  - `badgeMayo` Mayo 生化建制 — 深蓝 `#16324F`
  - `badgeGSH` 谷胱甘肽结构 — 苔绿 `#175E54`
- **背景母题**：腺体剪影渐变为分子晶体结构的多面体点阵。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 可的松的化学缔造者 / Edward C. Kendall 1886–1972 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、南诺沃克出身、哥伦比亚大学 BS 1908/MS 1909/PhD 1910、
    Mayo 生化部主任、普林斯顿 1951–1972、诺奖 1950、核心领域）
03  核心贡献概览 — 甲状腺素分离 / 可的松 / 谷胱甘肽结构 / Mayo 建制
04  哥伦比亚三连读 (1886–1910) — BS 1908、MS 1909、化学 PhD 1910
05  Parke-Davis 与甲状腺素 (1910–1914) — 首个任务即分离甲状腺激素；St. Luke's Hospital 续研
06  Mayo 生化掌门 (1915–1951) — 生化组主任、翌年任生化部主任
07  甲状腺素的分离 — 其自认最重要的发现（虽非获诺奖之作）
08  谷胱甘肽的结晶与结构 — 与合作者共同完成
09  肾上腺皮质类固醇 — 分离多种皮质类固醇，其一即 Compound E
10  与 Hench 的双线会合 — Compound E 治疗类风湿关节炎；命名 cortisone（核心贡献页）
11  1950 三人共享诺奖 — 与 Hench（Mayo 同事）、Reichstein；官方理由句；演讲《The Development of Cortisone As a Therapeutic Agent》
12  Mayo 之外的岁月 (1951–1972) — 强制退休年龄离任；普林斯顿客座教授直至去世
13  荣誉与纪念 — Lasker 1949 / Passano 1950 / Cameron 1951 / Golden Plate 1966；NAS 1950、AAAS+APS 1951；诺沃克 Kendall 小学冠名
14  遗产与结尾 — 双激素时代的生物化学 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1950 三人共享同句理由 | 与 Hench、Reichstein 共享且**官方理由同句**（"for their discoveries relating to the hormones of the adrenal cortex, their structure and biological effects"）——引用以 citations json 逐字为准 |
| 甲状腺素 vs 可的松 | 其最重要发现是**甲状腺素分离**（1910s，Parke-Davis 首个任务），诺奖理由却是**肾上腺皮质激素**——两条激素线勿混，获奖口径勿写成甲状腺研究 |
| 与 Hench 的双线 | Mayo **同事** + **共同得主**两重关系，yaml 分建 colleague 与 co-honored 两行，勿合并 |
| Cameron Prize 的第二次共享 | 1951 年与 **Reichstein** 共享爱丁堡 Cameron Prize——在 co-honored 边 note 中一并注明，不再单建边 |
| Compound E → cortisone | Kendall 分离的类固醇当时代号 Compound E，经 Hench 临床治疗后命名 cortisone——化学端与临床端分工明确 |
| 谷胱甘肽 | "worked with the team that crystallized glutathione and identified its chemical structure"——团队工作未具名成员，叙述用「与合作者」 |
| 退休的特殊原因 | 1951 年离开 Mayo 是因**强制退休年龄**（mandatory retirement age）——勿写成自行引退；此后普林斯顿客座教授至 1972 去世 |
| 学会年份 | NAS 1950；AAAS 与 APS 均 1951——三个年份勿混 |
| 奖项 | Lasker 1949 / Passano 1950 / Cameron 1951 / Golden Plate 1966；七校荣誉博士——与诺奖 1950 的年份关系勿乱 |
| 家庭 | 妻 Rebecca Kennedy（1915 结婚，1973 去世），四子女未具名不入库；Norwalk 的 Kendall Elementary School 冠名 |
| 页面较短 | page.md 材料有限——15 页规划靠身份页/荣誉页/建制页撑起，禁杜撰细节 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| thyroxine | 甲状腺素 | 其最重要分离成果（非诺奖理由） |
| cortisone | 可的松 | Compound E 的命名，诺奖理由域 |
| hormones of the adrenal cortex | 肾上腺皮质激素 | 获奖理由核心词 |
| Compound E | E 化合物 | 可的松前身代号 |
| glutathione | 谷胱甘肽 | 结晶与结构鉴定 |
| adrenal gland | 肾上腺 | 皮质激素来源腺体 |
| thyroid gland | 甲状腺 | 甲状腺素来源腺体，与肾上腺勿混 |
| Mayo Foundation | 梅奥基金会研究生院 | 任职机构（Graduate School） |
| mandatory retirement age | 强制退休年龄 | 1951 离任原因 |
| biochemistry division | 生化部 | Mayo 主任职位 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Kendall 的科学人生是一条漫长的时间之流——25 岁进 Parke-Davis、65 岁才因可的松获奖、86 岁逝于普林斯顿讲席；「时间之流」的绵长感对应其四十年 Mayo 建制与双激素研究的持续沉淀。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Edward_Calvin_Kendall/TheFlowOfTime.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
