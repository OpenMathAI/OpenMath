# 医学家立传提示词（Santiago Ramón y Cajal）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1906 年**得主（与 Camillo Golgi 共享）。
> 本文件是 Cajal 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Santiago Ramón y Cajal（1852-05-01 ~ 1934-10-17，享年 82 岁），西班牙神经科学家、病理学家、组织学家
- **气质关键词**：**现代神经科学之父、神经元学说的确立者、以画笔解剖大脑的人** —— 1906 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "in recognition of their work on the structure of the nervous system"（因其对神经系统结构的研究）
- **设计母题**：**生长锥与树突之林（growth cone & dendritic forest）**。Cajal 手绘的数百幅神经元图至今仍用于教学——以手绘线条质感的神经元森林作为贯穿全篇的背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Santiago_Ramón_y_Cajal/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Santiago_Ramón_y_Cajal/`；Makefile 复制后设 `MAIN=Santiago_Ramón_y_Cajal_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuroscience | 神经科学 | 1906 诺奖核心；现代神经科学奠基 | 核心页 |
| 1 | histology | 组织学 | 改良 Golgi 染色法、显微解剖 | 方法页 |
| 2 | neuroanatomy | 神经解剖学 | 神经元结构、大脑皮层比较研究 | 结构页 |
| 3 | pathology | 病理学 | 早期炎症病理与霍乱微生物研究 | 早年页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Aureliano Maestre de San Juan | 师→生（博士导师） | 博士导师（page frontmatter 有载） |
| spouse | Silveria Fañanás García | 无向 | 1879 结婚，育七女五子 |
| advisor-student | Rafael Lorente de Nó | 生（Cajal→学生） | 学生，将极化原理推进至电缆理论与神经回路分析 |
| colleague | Domingo Sánchez y Sánchez | 无向 | 同事，合作研究昆虫视觉神经系统 |
| co-honored | Camillo Golgi | 无向 | 1906 诺贝尔生理学或医学奖共享（神经系统结构研究） |
| controversy | Camillo Golgi | 无向 | 网状说与神经元学说对立，诺奖典礼上 Golgi 未回礼致意 |
| influence | Camillo Golgi | 无向 | 改进其黑色反应染色法并以之立神经元学说 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；`direction: student` = 对方是学生；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：叛逆而浪漫、艺术家手笔、显微镜下的诗意
- **主色**：`#0F4C5C`（深孔雀青，显微镜视野与地中海气质）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：
  - `badgeNeuron` 神经元学说 — 墨青 `#1B6B6B`
  - `badgeDraw` 手绘图谱 — 赭石 `#B0713A`
  - `badgeGrowth` 生长锥 — 嫩枝绿 `#4C7A3F`
  - `badgeCuba` 军旅与早年 — 军褐 `#6B4A2B`
- **背景母题**：米白底上手绘风神经元（细线树突 + 末端小锥形生长锥），如标本册页散布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 现代神经科学之父 / Santiago Ramón y Cajal 1852–1934 + 四色 badge + 右上肖像 + 国籍行（Spain）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Petilla de Aragón、萨拉戈萨/马德里、师承、任职、荣誉）
03  核心贡献概览 — 神经元学说 / 生长锥 / 树突棘 / Cajal 体
04  叛逆少年 (1852–1873) — 自制大炮入狱、拜师鞋匠理发师、墓地取骨画骨骼
05  军医生涯与古巴 (1873–1877) — 十年战争、染疟疾与结核、Panticosa 疗养、马德里博士 1877
06  萨拉戈萨与瓦伦西亚 (1877–1887) — 解剖博物馆主任、炎症病理与霍乱、瓦伦西亚解剖学教授
07  巴塞罗那的转折 (1887) — 初见 Golgi 染色法、改良铬银法、转向中枢神经系统
08  神经元学说（核心贡献页）— 神经细胞相邻而不连续、为 Waldeyer 命名的 neuron theory 提供决定性证据
09  手绘图谱 — 数百幅神经绘图、海马回路/小脑浦肯野细胞/视网膜、至今用于教学
10  生长锥、树突棘与 Cajal 体 — 以 Cajal 命名的发现群（ICC 细胞、Cajal-Retzius 细胞、轴-轴突触）
11  1894 Croonian 讲座 — 皮层锥体细胞如树般生长、「学习即神经元生长新连接」（突触记忆理论之源）
12  1906 诺贝尔奖 — 与 Golgi 共享、网状说之争的讽刺同框、首位获科学诺奖的西班牙人
13  马德里岁月与身后 — 1899 国立卫生研究所所长、1922 创立 Cajal 研究所、月面 Cajal 环形山
14  遗产：从科学到文化 — 1935 年 50 比塞塔钞票、UNESCO 世界遗产级遗存、Ramón y Cajal 奖学金
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1852-05-01 生于 Petilla de Aragón（纳瓦拉），1934-10-17 卒于马德里；临终仍在工作（正文明载） |
| 获奖理由 | 官方口径 "in recognition of their work on the structure of the nervous system"，用 **their**（与 Golgi 共享） |
| 「首位」表述 | 首位获科学类诺奖的**西班牙人**（正文明载）；勿扩大为"西班牙首位诺奖得主" |
| Golgi 染色法归属 | 方法是 **Golgi 发明**（1873），Cajal 1887 年才习得并改良——功劳表述必须区分 |
| 1897 年皇家学院演讲 | page.md 有西语原话 + 英译（ministro del progreso…），引原话须用此段，勿自造引语 |
| 「显微镜的堂吉诃德」 | 出自 J. Harley Williams 之评语（page.md 图注明载），转述时注明出处 |
| 「铁的外科医生」 | 源于其旧演讲，被 1937 年内战《Gaceta de Melilla》挪用——语境区分，勿写成其本人政治表态 |
| Nansen 先行工作 | Cajal 未引用 Nansen 关于神经细胞相邻性的先行研究（page.md 明载），Review 时勿补写 |
| 1890s 早年研究 | 瓦伦西亚时期做炎症病理、霍乱微生物、上皮组织——勿把神经工作提前到此期 |
| 子女 | 与 Silveria 育七女五子（正文明载）；子女姓名无载不入库 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| neuron doctrine | 神经元学说 | Cajal 立场；名称由 Waldeyer 提出 |
| growth cone | 生长锥 | Cajal 发现的轴突生长末端 |
| dendritic spine | 树突棘 | Cajal 力主其存在 |
| Cajal body | Cajal 体 | 核内细胞器，以其命名 |
| interstitial cell of Cajal (ICC) | Cajal 间质细胞 | 胃肠道起搏细胞 |
| Cajal-Retzius cell | Cajal-Retzius 细胞 | 与 Retzius 共同描述 |
| Golgi's method | 高尔基染色法 | Golgi 发明、Cajal 改良，归属勿混 |
| Croonian Lecture | 克罗尼安讲座 | 1894 年皇家学会讲座 |
| trisynaptic circuit | 三突触回路 | 海马回路 |
| "Vacation Stories" | 《假期故事》 | 1905 以笔名 Dr. Bacteria 发表的科幻小说 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（manifest 预分配）
- **风格**：进取 / 探险 / 叙事推进
- **匹配理由**：从叛逆少年到古巴军医再到显微镜前的远征——Cajal 的一生是向「大脑未知大陆」的探险；Expedition 的行进感匹配 1887 年巴塞罗那转折与神经元学说远征的胜利，也匹配其「显微镜的堂吉诃德」的浪漫骑士气质。
- **本地路径**：`music_audio/` 下 Expedition 曲目 → 复制为 `presentations/20th_century/Santiago_Ramón_y_Cajal/Expedition.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
