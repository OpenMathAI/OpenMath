# 医学家立传提示词（Jules Bordet）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1919 年得主 Jules Bordet（朱尔斯·博尔代）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Jules_Bordet/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Jules Jean Baptiste Vincent Bordet（1870-06-13 生于比利时苏瓦尼 ~ 1961-04-06 逝于布鲁塞尔，享年 90 岁）
- **气质关键词**：**补体的发现者、免疫学的奠基人、布鲁塞尔巴斯德式的建所人**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1919 条目）：
  > "for his discoveries relating to immunity"（因其关于免疫的发现）
- **设计母题**：**血清中的隐形卫兵（the invisible guardian in serum）**——抗体之外，血清中还有一种先天成分（他命名 alexine，今称 complement）协同溶解细菌；用「两种粒子协同攻破细菌壁」的抽象图形作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Jules_Bordet/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Jules_Bordet/`（肖像见 images.txt：Jules_Bordet.JPG，250px 可改 600px 经 Commons Special:FilePath）。Makefile 复制后设 `MAIN=Jules_Bordet_zh`、`VIDEO_NAME=Jules_Bordet_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Bordet 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | 补体与免疫发现，1919 诺奖核心 | 封面、核心页 |
| 1 | bacteriology | 细菌学 | 1907 布鲁塞尔自由大学细菌学教授；百日咳杆菌 | 核心页 |
| 2 | microbiology | 微生物学 | infobox field_of_work；Bordetella 属 | 核心页 |
| 3 | serology | 血清学 | 补体结合试验→梅毒血清诊断 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Élie Metchnikoff | 对方 → 导师 | 1894 入巴黎巴斯德研究所 Metchnikoff 实验室工作；frontmatter 亦载其为博士导师 |
| colleague | Octave Gengou | 无向 | 1906 共同纯培养分离百日咳杆菌 Bordetella pertussis |
| controversy | Felix d'Herelle | 无向 | 1930 Croonian 讲座否定噬菌体存在（主张细菌自溶），1941 Ruska 电镜照片证其误 |

**不入库但提示词可叙述**：August von Wassermann——其梅毒试验是基于 Bordet 补体结合法由 Wassermann 本人发展（技术因果链，非二人合作）；Helmut Ruska（电镜照片作者，仅事件）；名下机构（Institut Jules Bordet、Bordet 车站）非人物。

## 五、配色方案 【人物专属】

- **气质**：严谨、古典、比利时式的沉静
- **主色**：`#7A1E28`（比利时深红——巴斯德学派的血清与传承）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeComp` 补体与免疫 — 深红 `#7A1E28`
  - `badgeBact` 细菌学 — 深绿 `#1B4D3E`
  - `badgeSerum` 血清诊断 — 深蓝 `#16324F`
  - `badgeInst` 建所与建制 — 琥珀 `#B8860B`
- **背景母题**：血清液中浮游的球菌与溶破轨迹的抽象点阵，呼应「免疫的隐形战场」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 补体的发现者 / Jules Bordet 1870–1961 + 四色 badge + 右上头像 + 国籍行（Belgium）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地苏瓦尼、布鲁塞尔自由大学 MD 1892、
    巴黎巴斯德研究所、布鲁塞尔自由大学教授 1907、诺奖 1919、核心领域）
03  核心贡献概览 — 补体 / 溶血 / 补体结合试验 / 百日咳杆菌
04  早年与医学训练 (1870–1892) — 苏瓦尼出身，布鲁塞尔自由大学 1892 医学博士
05  巴黎巴斯德研究所 (1894–1900) — 入 Metchnikoff 实验室；吞噬细胞免疫的现场
06  补体的发现 (1895)（核心贡献页）— 特定抗体溶菌被先天血清成分增强，命名 alexine（今 complement）
07  溶血现象 (1899) — 免疫血清下异种红细胞破裂的类似过程
08  补体结合试验与梅毒诊断 — Wassermann 试验的技术基础，今日血清学之源
09  回布鲁塞尔建所 (1900) — 仿巴斯德式研究所；1907 任布鲁塞尔自由大学细菌学教授
10  百日咳杆菌 (1906) — 与 Gengou 纯培养分离 Bordetella pertussis，确立百日咳病原
11  荣誉与认可 — 1916 皇家学会外籍会员；1919 诺奖；1921 Cameron Prize；1930 Croonian Lecture
12  Croonian 讲座的误判 (1930) — 否定噬菌体存在、主张自溶；1941 电镜照片证其误（史实如实呈现）
13  以 Bordet 命名 — Bordetella 属 / Institut Jules Bordet 癌症医院 / Bordet 火车站
14  遗产与结尾 — 从补体到现代免疫学 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生卒日期 | frontmatter 双值噪声（1870-00-00），以正文 **1870-06-13 ~ 1961-04-06** 为准；葬于布鲁塞尔 Ixelles 墓园 |
| 1919 独得 | 1919 年为单独得主（一战停颁后首届），无 co-honored，勿写共享 |
| 博士导师口径 | frontmatter 载 Élie Metchnikoff；正文载 1894 入其巴黎巴斯德实验室——入库 advisor-student（direction: advisor），note 注明实验室经历 |
| alexine → complement | Bordet 当年命名 **alexine**，今称 complement（补体）——两个名字的沿革勿混，叙述需点明 |
| Wassermann 试验 | 是 Bordet 补体结合法**之上的应用**，由 August von Wassermann 发展；勿写"Bordet 与 Wassermann 合作" |
| 噬菌体误判 | 1930 Croonian 讲座断言噬菌体（d'Herelle 发现的"看不见的病毒"）不存在、细菌死于自溶；**1941 年 Helmut Ruska 电镜照片证其误**——如实写为历史错误，不作道德化渲染 |
| Metchnikoff 拼写 | page.md 正文作 Elie Metchnikoff（无重音）、frontmatter 作 Élie Metchnikoff；yaml/入库用 frontmatter 形式 Élie Metchnikoff，正文叙述两可但全篇统一 |
| 诺奖理由 | 官方措辞只有 "for his discoveries relating to immunity" 一句，勿扩写成"补体发现"字样 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| complement | 补体 | Bordet 原命名 alexine，沿革要点明 |
| alexine | 亚历克辛（旧称） | 历史名词，今已弃用 |
| bacteriolytic | 溶菌的 | 抗体+补体协同作用 |
| hemolysis | 溶血 | 1899 描述的异种红细胞溶解 |
| complement-fixation test | 补体结合试验 | 血清学诊断基础 |
| Wassermann test | 瓦瑟曼试验 | 梅毒血清诊断，技术源自 Bordet |
| Bordetella pertussis | 百日咳博德特菌 | 1906 与 Gengou 分离 |
| whooping cough | 百日咳 | 病原确立 |
| bacteriophage | 噬菌体 | d'Herelle 发现；Bordet 1930 误判不存在 |
| autolysis | 自溶 | Bordet 当年的（错误）解释 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Shine Like The Sun**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：补体如血清中恒常运转的先天卫兵，温和而不熄——"如太阳般闪耀"对应免疫学奠基者跨越半个世纪的持续贡献（1895 发现 → 1919 诺奖 → 1961 享年 90 岁辞世）；明亮温暖的大调气质也贴合布鲁塞尔建所、泽被后学的叙事。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Jules_Bordet/ShineLikeTheSun.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
