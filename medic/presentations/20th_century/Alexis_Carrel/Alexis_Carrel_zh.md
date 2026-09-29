# 医学家立传提示词（Alexis Carrel）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Alexis Carrel（1912 年诺贝尔生理学或医学奖得主，法国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Alexis_Carrel/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Alexis Carrel（亚历克西·卡雷尔，1873-06-28 圣福特莱昂 ~ 1944-11-05 巴黎，享年 71 岁）
- **气质关键词**：**血管缝合的先行者、移植与胸外科的开路人、「不老细胞」的制造者与争议缠身的晚节** —— 1912 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json）：
  > "[for] his work on vascular suture and the transplantation of blood vessels and organs"
  > （因其关于血管缝合与血管和器官移植的工作）
- **设计母题**：**「三点的缝合」**。从绣花女工处学来的三角固定缝合法（triangulation）把血管吻合变成可重复的手术——视觉隐喻：三根定位缝线构成等边三角形，中心是吻合口的光点。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Alexis_Carrel/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Alexis_Carrel/`，成目录 `medic/presentations/20th_century/Alexis_Carrel/`，Makefile 复制后设 `MAIN=Alexis_Carrel_zh`、`VIDEO_NAME=Alexis_Carrel_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | vascular surgery | 血管外科 | 三点缝合、血管吻合，1912 诺奖核心 | 血管缝合页 |
| 1 | transplantology | 移植学 | 血管与器官移植实验先驱 | 移植页 |
| 2 | tissue culture | 组织培养 | 与 Burrows 开创；1912 鸡胚心「不老」培养 20 余年 | 组织培养页 |
| 3 | thoracic surgery | 胸外科 | 开拓性工作 | 胸外科页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Alexis_Carrel.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| collaborator | Charles Claude Guthrie | — | 芝加哥合作血管缝合与血管器官移植实验 |
| collaborator | Montrose Thomas Burrows | — | 洛克菲勒研究所合作开创组织培养 |
| collaborator | Charles Lindbergh | — | 1930s 合作研制灌流泵并合著 The Culture of Organs |
| collaborator | Henry Drysdale Dakin | — | 一战共创卡雷尔-达金伤口抗菌冲洗法 |
| influence | Alexis Presse | — | 1939 年相识的特拉普派修士，影响其晚年信仰回归 |

> 说明：page.md 提及「his wife」但全程未具名——配偶不建边；Lourdes 事件当事人 Marie Bailly、灵性导师语境的 Jesuits 教育、Jean Coutrot（1937 加入其研究中心）、Pétain/多里奥等维希政坛人物均不建人物关系边（维希角色在第七节陷阱中如实记载）；Albert Ebeling（接管培养的同事）仅注释级提及，不入库。

## 五、配色方案 【人物专属】

- **气质**：锋利、大胆、技术乌托邦式的野心与暗面
- **主色**：血管深红 `#7A1E28`（缝合线上的动脉血色）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 血管外科 — 吻合线红 `#B3402E`
  - `badgeB` 移植学 — 器官绛 `#8E3B5B`
  - `badgeC` 组织培养 — 培养基琥珀 `#C98A2E`
  - `badgeD` 胸外科 — 胸腔蓝灰 `#4E6478`
- **背景母题**：稀疏的缝线轨迹（弧形虚线）与三点缝合三角徽记，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 血管缝合的先行者 / Alexis Carrel 1873–1944 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像（1912 照）+ 右信息网格（生卒、里昂教育、芝加哥/洛克菲勒、荣誉、核心领域）
03  核心贡献概览 — 血管缝合 / 器官移植 / 组织培养 / 伤口抗菌
04  里昂青年 (1873–1902) — 耶稣会教育、1894 Sadi Carnot 遇刺的触动、1902 首篇血管缝合论文
05  卢尔德与转向 — 1902 Marie Bailly 事件、学术圈受挫、远走加拿大（The Voyage to Lourdes 身后出版）
06  芝加哥：与 Guthrie 的实验期 — 血管吻合、器官移植、头移植实验
07  洛克菲勒研究所 (1906–1939) — 加入新所、组织培养与 Burrows
08  血管缝合：三点法（核心页）— 绣花女工的启示、triangulation、1901–1910 动物实验全功
09  1912 诺贝尔奖（核心页）— citation 原文、诺奖演讲 Suture of Blood-Vessels and Transplantation of Organs
10  「不老」的鸡心 (1912–1946) — 20 余年培养、从未被重复、1960s Hayflick 极限的解释
11  一战：Carrel–Dakin 冲洗法 — 战地伤口清创、高达量抗菌液冲洗、荣誉军团勋章
12  灌流泵：与 Lindbergh 的十年 — 1930s 相识、1938-06-13 时代封面、1939 世博会、后世「不实用」评价
13  晚节之暗 — Man the Unknown 1935、维希基金会 1941、通敌指控与 1944 之死；1996 里昂医学院更名
14  遗产 — 月球环形山 Carrel、1972 瑞典邮票、2002 Lindbergh–Carrel 奖；器官移植与人工心脏的远源
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文（含方括号 "[for]" 处理为 [for] 或省略说明）；核心两要素是 vascular suture + transplantation，勿写成「因器官移植技术发明」 |
| 2 | 头移植实验 | 与 Guthrie 在芝加哥做过 head transplant 实验——page.md 明载可提，但须放在「动物实验探索」语境，勿渲染 |
| 3 | 灌流泵评价 | 须两面写：媒体盛赞（Time 封面/世博会）与后世认定 "impractical and difficult to use"（美国心血管灌流学会 2017 口径）——只写 page.md 实载，勿只留光辉面 |
| 4 | 鸡心实验 | 「维持 20 余年」是 Carrel 主张的结果，从未被重复；Hayflick/Witkowski 的质疑（换液引入新细胞）必须并写，勿当定论 |
| 5 | 维希与优生学 | page.md 大量明载：Man, the Unknown 言论、1941 维希基金会、PPF 党员、死后通敌指控未审。立传须如实、克制地记载（史实口径），不渲染、不辩护；法国 20 余城市除名、1996 里昂医学院更名可提 |
| 6 | 配偶 | page.md 仅 "his wife" 未具名——身份页与关系页均不出现配偶姓名，禁编造 |
| 7 | 引语 | 1942 年信仰声明 "I believe in the existence of God..." 有英文原文可引；Lindbergh「视 Carrel 为挚友」为转述，勿直引 |
| 8 | 与 Dakin 同名性 | Henry Drysdale Dakin 亦是 1910 诺奖得主 Kossel 的门生（库内同一记录）；本篇 note 写一战合作即可，勿写师生边 |
| 9 | 荣誉年代 | APS 1909、AAAS(American Academy of Arts and Sciences) 1914、苏联科学院通讯/荣誉成员 1924 与 1927 两说（页作 twice）——按页写「两次（1924、1927）」 |
| 10 | metadata 冲突 | metadata.json 的 occupations 含 sociologist（因社会著述）；yaml 主职业取 surgeon，occupations 已按事实取舍，立传以 page.md 为准 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| vascular suture | 血管缝合 | 诺奖理由核心词 |
| triangulation technique | 三点（三角固定）缝合法 | 受绣花工艺启发的定位法 |
| anastomosis | 吻合术 | 血管对接的正式术语 |
| perfusion pump | 灌流泵 | 与 Lindbergh 共同研制，勿称「人工心脏」 |
| tissue culture | 组织培养 | 与组织移植区分 |
| cellular senescence | 细胞衰老 | Hayflick 极限语境 |
| Carrel–Dakin method | 卡雷尔-达金冲洗法 | 氯系抗菌液伤口处理 |
| debridement | 清创术 | 冲洗法流程之一 |
| The Culture of Organs | 《器官的培养》 | 1930s 合著，勿译《器官文化》 |
| Man, the Unknown | 《人，这位未知者》 | 1935 畅销书，维希思想背景 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「电影感/戏剧张力」匹配其人生剧本——从里昂实习医生到诺奖、从时代封面到维希审判边缘，大起大落需要史诗配器
  - 也匹配技术乌托邦年代（1930s 灌流泵、世博会）的 media spectacle 气质
- **备选**（未采用）：Tragedy（本批次 Kocher 已用）、Falling Apart（暗面过重，压过手术成就主体）
- **本地路径**：按 music_audio/ 内 Alex-Productions Cinematic Experience 曲目复制至 `medic/presentations/20th_century/Alexis_Carrel/Cinematic_Experience.wav`，ffmpeg `-shortest` 对齐
