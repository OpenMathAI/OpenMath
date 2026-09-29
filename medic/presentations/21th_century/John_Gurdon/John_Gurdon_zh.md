# 医学家立传提示词（John Gurdon）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2012 年得主 John Gurdon（约翰·格登）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/John_Gurdon/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Sir John Bertrand Gurdon（1933-10-02 生于英格兰萨里郡 Dippenhall ~ 2025-10-07 去世，享年 92 岁）
- **气质关键词**：**细胞核移植的先驱、"被评判最不适合成为科学家的人"、克隆时代的开门者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2012 条目，与 Shinya Yamanaka 共享同一理由）：
  > "for the discovery that mature cells can be reprogrammed to become pluripotent"（因发现成熟细胞可被重编程为多能性细胞）
- **设计母题**：**细胞核的易主（nuclear transplant）**——去核卵细胞接纳新核、重启发育的意象：以卵形轮廓+移入的核+重新启动的分裂弧线作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/John_Gurdon/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/John_Gurdon/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=John_Gurdon_zh`、`VIDEO_NAME=John_Gurdon_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | nuclear transfer | 细胞核移植 | 1958 爪蟾体细胞核克隆，2012 诺奖核心 |
| 1 | developmental biology | 发育生物学 | infobox Fields 明载，细胞分化研究 |
| 2 | cellular reprogramming | 细胞重编程 | 组蛋白变体、移植 DNA 去甲基化机制 |
| 3 | cellular differentiation | 细胞分化 | 分化细胞核仍保有全套遗传潜能的证明 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Michail Fischberg | 对方 → 导师 | 牛津大学 DPhil 导师（1960，爪蟾核移植论文） |
| advisor-student | Douglas A. Melton | Gurdon → 学生 | infobox Doctoral students 明载 |
| advisor-student | Edward M. De Robertis | Gurdon → 学生 | infobox Doctoral students 明载 |
| spouse | Jean Elizabeth Margaret Curtis | 无向 | 妻（Personal life 节明载），育二子女 |
| co-honored | Shinya Yamanaka | 无向 | 2012 诺贝尔生理学或医学奖共享（成熟细胞重编程为多能性） |

**不入库但提示词可叙述**：Robert Briggs 与 Thomas Joseph King（1952 胚胎细胞核移植先例，科学史脉络）；Har Swarup（1956 刺鱼多倍体）；J. B. S. Haldane（1963 描述 Gurdon 结果时率先对动物使用 "clone" 一词，库内数学家侧有记录但不建边）；Basel 免疫学研究所团队（1975 用淋巴细胞核补上终证）。

## 五、配色方案 【人物专属】

- **气质**：隐忍、逆转、生命时钟的回拨
- **主色**：`#16324F`（牛津深蓝——Christ Church 的古典与克制）+ 香槟金诺奖色
- **badge 四分类色**：`badgeNT` 核转移 深蓝 `#16324F`；`badgeClone` 克隆 青绿 `#0E7C7B`；`badgeXenopus` 爪蟾模型 苔绿 `#175E54`；`badgeiPS` 重编程之桥 玫瑰 `#A63A2B`
- **背景母题**：卵形轮廓+移入的核+重启分裂弧线，呼应「细胞核的易主」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 核移植的先驱 / John Gurdon 1933–2025 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1933-10-02 Dippenhall ~ 2025-10-07、
    伊顿公学、牛津 Christ Church 古典学转动物学、DPhil 1960、剑桥教授 1983、诺奖 2012）
03  核心贡献概览 — 1958 核移植克隆 / 分化核的全能性 / 爪蟾卵表达系统 / 重编程机制
04  "最不适合成为科学家" (1933–1952) — 伊顿公学 250 人中生物学垫底、
    学区报告原话（page.md 明载英文可引，他终身装裱此报告）
05  牛津：从古典学到动物学 — Christ Church 读 classics 转 zoology、MA 学位
06  Fischberg 门下与 1958 克隆（核心贡献页）— 爪蟾蝌蚪体细胞完整核移植入去核卵、
    获得活蛙；Briggs & King 1952 先例的延伸
07  分化核的边界之问 — 当时未能确证核来自完全分化细胞；1975 巴塞尔组用淋巴细胞核补上终证
08  "clone" 一词 — 源自希腊语 κλών（嫩枝），20 世纪初用于植物；
    1963 Haldane 描述 Gurdon 结果成为动物语境最早使用者之一
09  爪蟾卵表达系统 — 微量注射 mRNA 翻译技术，鉴定蛋白功能的通用工具
10  剑桥岁月 (1972–) — 动物学系 1972 起、教授 1983、MRC LMB；1989 创立 Wellcome/CRC
    研究所、2004 更名 Gurdon Institute（任主席至 2001）
11  重编程机制 — 移植核的组蛋白变体与 DNA 去甲基化；细胞间信号因子分析
12  荣誉与认可 — FRS 1971、Royal Medal 1985、Int'l Prize for Biology 1987、Wolf 1989、
    Copley、Lasker 2009、Nobel 2012（讲演 "The Egg and the Nucleus: A Battle for Supremacy"）
13  学院与公共事务 — Magdalene 院长 1995–2002、Nuffield 生物伦理理事会、下级勋位爵士 1995
14  遗产与结尾 — 从克隆蛙到 iPS 的五十年回响（与 Yamanaka 的接力）；2025-10-07 辞世
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 卒日与享年 | 2025-10-07 去世（92 岁生日 5 天后）——yaml 已填 death_date；封面/身份页写 1933–2025，勿再当"在世者"处理 |
| 1958 克隆对象 | 用 *Xenopus* 蝌蚪**体细胞的完整核**移植入去核卵获活蛙——"用肠上皮细胞"是大众讹传的简化（Yamanaka 篇背景节作"肠上皮"表述时须注意 page.md 措辞为 somatic cells of a tadpole） |
| 完全分化证明 | Gurdon 1958 当时**未能**确证移植核来自完全分化细胞；1975 年巴塞尔免疫学研究所用抗体产生淋巴细胞核补上终证——勿把终证归给 Gurdon |
| clone 一词 | Gurdon 是"clone 用于动物"的对象而非首创者；1963 Haldane 描述其结果——归属写清 |
| Briggs & King | 1952 年胚胎囊胚细胞核移植是先例，Gurdon 是"重要延伸"（体细胞核）——勿写成"史上第一次核移植" |
| 伊顿报告引语 | "I believe he has ideas about becoming a scientist; on his present showing this is quite ridiculous." 为 page.md 明载英文，可引原文+译文；"他装裱了这份报告"与对记者的另一句原话均可引 |
| 获奖 | 2012 与 Yamanaka 共享同一理由；Gurdon 一侧是 1958-1960s 核移植，Yamanaka 一侧是 2006 iPS——五十年接力勿混写 |
| Nobel lecture | "The Egg and the Nucleus: A Battle for Supremacy"（2012-12-07）——标题勿错 |
| 宗教与政治 | "middle of the road"、不可知论"no scientific proof either way"、圣公会基督徒——page.md 明载可客观一句；Magdalene 院士小礼拜堂演讲风波可提，勿渲染 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| nuclear transplantation | 细胞核移植 | 获奖工作核心，非"生殖克隆" |
| somatic cell nuclear transfer | 体细胞核移植（SCNT） | Yamanaka 篇背景用词 |
| pluripotent | 多能性 | 获奖理由核心词 |
| Xenopus laevis | 非洲爪蟾 | 模式生物，勿写"青蛙"泛称 |
| enucleated egg | 去核卵细胞 | 受体 |
| clone | 克隆 | κλών 嫩枝本义 |
| oocyte translation system | 卵母细胞表达系统 | 微注 mRNA 翻译技术 |
| histone variants | 组蛋白变体 | 重编程机制方向 |
| demethylation | 去甲基化 | 移植 DNA 表观遗传重置 |
| Gurdon Institute | 格登研究所 | 2004 更名致敬 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：一个被判定"绝不可能成为科学家"的少年，把细胞核送进了另一片"新大陆"（去核卵）并重启了生命——"New Lands" 匹配其逆转命运与逆转细胞命运的双重弧线。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/John_Gurdon/New_Lands.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
