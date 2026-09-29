# 医学家立传提示词（John Eccles (neurophysiologist)）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：John Eccles（1963 年诺贝尔生理学或医学奖得主，澳大利亚）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/John_Eccles_neurophysiologist/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir John Carew Eccles（约翰·卡鲁·埃克尔斯，1903-01-27 墨尔本 ~ 1997-05-02 瑞士特内罗-孔特拉，享年 94 岁）
- **气质关键词**：**突触离子机制的测绘者、从错误假说走向真理的「化学派辩手」、晚年转向心灵哲学的三元交互主义者** —— 1963 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Hodgkin、Huxley 三人共享）：
  > "for their discoveries concerning the ionic mechanisms involved in excitation and inhibition in the peripheral and central portions of the nerve cell membrane"
  > （因其关于神经细胞膜外周与中枢部分兴奋和抑制的离子机制的发现）
- **设计母题**：**「兴奋与抑制的天平」**。EPSP 叠加触发动作电位、IPSP 从中减除——视觉隐喻：天平两端分别托起兴奋性/抑制性突触电位波形。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/John_Eccles_neurophysiologist/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/John_Eccles_neurophysiologist/`，成目录 `medic/presentations/20th_century/John_Eccles_neurophysiologist/`，Makefile 复制后设 `MAIN=John_Eccles_neurophysiologist_zh`、`VIDEO_NAME=John_Eccles_neurophysiologist_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库：本人记录复用库内既有 stub（id=5082）UPD 回填 QID Q273223；同名分裂 stub「John Carew Eccles」(5327，Sherrington 师生边) 已归并改指至 5082 并删除。`has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neurophysiology | 神经生理学 | 脊髓运动神经元突触研究，1963 诺奖核心 | 总览页 |
| 1 | synaptic transmission | 突触传递 | EPSP/IPSP 叠加与减除、化学传递的实验确证 | 突触页 |
| 2 | philosophy of mind | 心灵哲学 | 与 Popper 合著、交互主义/三元论 | 哲学页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/John_Eccles_neurophysiologist.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Charles Scott Sherrington | 师 | 罗德学者赴牛津师从，1929 年 DPhil（他批已建同边） |
| co-honored | Alan Lloyd Hodgkin | — | 1963 诺贝尔生理学或医学奖三人共享（离子机制） |
| co-honored | Andrew Huxley | — | 1963 诺贝尔生理学或医学奖三人共享（离子机制） |
| colleague | Bernard Katz | — | 合作实验确证乙酰胆碱为脑内神经递质，悉尼共事 |
| colleague | Karl Popper | — | 心灵哲学伙伴，合著 The Self and Its Brain，三元交互主义 |
| spouse | Irene Frances Miller Eccles | — | 1928 年成婚，1968 年离异 |
| spouse | Helena Táboríková | — | 1968 年成婚，神经心理学家，婚后研究合作至终老 |
| advisor-student | Wilfrid Rall | 生 | 博士生（infobox 明载） |
| advisor-student | Stephen Kuffler | 生 | 博士生（infobox 明载） |
| advisor-student | Rodolfo Llinás | 生 | 博士生（infobox 明载） |

> 说明：与 Dale 的 controversy 边（1940s 化学/电突触之争）已由 batch-08 Dale 侧先建（库内 10509），本篇不重复列。Katz 同时出现在 Dale/Hodgkin 篇——共享同一库内记录。九名子女未具名不入库；Cyril Höschl（1993 合影）不入库；与 Popper 的师友关系用 colleague（合著者）。

## 五、配色方案 【人物专属】

- **气质**：南半球的开阔、电生理的精密、哲学晚境的思辨
- **主色**：突触电位青 `#2E7A8C`（示波器波形的冷光）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 神经生理学 — 脊髓蓝 `#33637D`
  - `badgeB` 突触传递 — EPSP 橙 `#C07A2E`
  - `badgeC` 离子机制 — 通道紫 `#5B4E8E`
  - `badgeD` 心灵哲学 — 三界金灰 `#8A7A4E`
- **背景母题**：EPSP/IPSP 上下波形对偶曲线、稀疏突触小体剪影，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 突触离子机制的测绘者 / John Eccles 1903–1997 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像（1963 照）+ 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — EPSP/IPSP / 化学传递确证 / 离子机制 / 心灵哲学
04  墨尔本与家庭教育 (1903–1925) — 教师父母居家教育至 12 岁、17 岁奖学金入墨尔本大学、1925 一等荣誉毕业
05  牛津：Sherrington 门下 (1925–1929) — 罗德奖学金、马格德伦学院、1929 DPhil
06  归澳与战时 (1937–1945) — Kanematsu 研究所所长、与 Katz 的悉尼讲座、战时军事研究
07  奥塔哥与堪培拉 (1945–1962) — 奥塔哥教授、1952-62 约翰柯廷医学研究院
08  1950s：伸张反射模型（核心页）— 股四头肌运动神经元、EPSP 空间叠加、IPSP 减除
09  从错误到真理 — 至 1949 年坚信电传递、其论战反促化学传递实验确证（与 Katz 乙酰胆碱工作）
10  1963 诺贝尔奖（核心页）— citation 原文、与 Hodgkin/Huxley 三人共享、同年 Australian of the Year
11  1966-1975：美国岁月 — 西北大学不遂、布法罗纽约州立大学至退休
12  心灵的三重世界 — 与 Popper 的交互主义/三元论、The Self and Its Brain、晚年转向
13  荣誉与认可 — Knight Bachelor 1958 · Royal Medal 1962 · Nobel 1963 · Companion of the Order of Australia 1990 · 世界文化理事会创始成员 1981
14  遗产 — Eccles 神经科学研究所（JCSMR, 2012）、奥塔哥 Eccles Building（2021）；突触生理学教科书级贡献
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries concerning the ionic mechanisms involved in excitation and inhibition in the peripheral and central portions of the nerve cell membrane"（their 三人共享）；Hodgkin/Huxley 份额是外周动作电位，Eccles 是中枢突触——三分工勿混 |
| 2 | 与 Dale 的论战定位 | Eccles 至 1949 年主张电传递（错），但其论战「led him and others to perform experiments which proved chemical transmission」——正文须写「错误的假说催化了正确的实验」，勿简单写成「他错了」 |
| 3 | 库内同名 | 分裂 stub「John Carew Eccles」(5327) 已归并删除；库内唯一规范名 John Eccles (neurophysiologist)（manifest 形式），勿用裸形式建边 |
| 4 | 师承边 | Sherrington 师生边他批已建（10763，note 为对方批次版本），本 yaml 同边幂等跳过——正文本篇照常叙述罗德学者师承 |
| 5 | 国籍链 | Australia 出生；citizenship 含 UK（罗德学者时期）与 Switzerland（晚年）——yaml/Nobel 口径 Australia，正文可叙三重身份 |
| 6 | 哲学段尺度 | Popper 三重世界/交互主义/二元→三元——page.md 大段明载，建议压缩为一帧（引用一小段英文原文+概述），勿整页堆引文 |
| 7 | 两个妻子 | Irene Miller（1928-1968 离异）与 Helena Táboríková（1968-1997）——两段均建 spouse 边；Helena 系查理大学医学博士、神经心理学家，婚后合作；九名子女未具名不入库 |
| 8 | 学生名单 | Rall/Kuffler/Llinás 仅 infobox 明载（正文无展开）——按「infobox 属 page.md 内容」口径入库并标注；若 Review 认为证据不足可降级为文字叙述 |
| 9 | 引语红线 | 哲学章引语有英文原文可引；其余叙事无直接引语，禁编造；Katz 合作的「strongly influencing the intellectual environment」为叙述语 |
| 10 | metadata 冲突 | frontmatter occupation 含 philosopher——yaml 第三职业保留 neuroscientist 主位，哲学作为 fields 第 3 项；死因无载（仅年龄地点） |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| EPSP | 兴奋性突触后电位 | 空间叠加可触发动作电位 |
| IPSP | 抑制性突触后电位 | 从叠加中减除 |
| stretch reflex | 牵张反射 | 其双神经元模型系统 |
| muscle spindle | 肌梭 | 感觉神经元 |
| motor neurone | 运动神经元 | — |
| synaptic transmission | 突触传递 | 电 vs 化学之争的焦点 |
| acetylcholine | 乙酰胆碱 | 与 Katz 合作确证的脑内递质 |
| interactionism / trialism | 交互主义 / 三元论 | 其晚年哲学立场 |
| Rhodes Scholarship | 罗德奖学金 | 1925 赴牛津 |
| Kanematsu Institute | 金松研究所 | 悉尼，战时所长任内 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「时间之流」匹配其学术弧线的三段式——牛津师承、堪培拉黄金十年、瑞士晚年的哲学沉思，一生横跨科学与哲学两岸
  - 流动的钢琴织体契合 EPSP/IPSP 波形的起伏意象
- **备选**（未采用）：Awaken（batch-11 Hess 已用，且「觉醒」意象更贴电刺激主题）、Timeless（batch-11 Carl 已用）
- **本地路径**：按 music_audio/ 内 Alex-Productions The Flow of Time 曲目复制至 `medic/presentations/20th_century/John_Eccles_neurophysiologist/The_Flow_of_Time.wav`，ffmpeg `-shortest` 对齐
