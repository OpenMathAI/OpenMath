# 医学家立传提示词（Henrik Dam）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1943 年得主 Henrik Dam（亨里克·达姆）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Henrik_Dam/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Carl Peter Henrik Dam（1895-02-21 生于哥本哈根 ~ 1976-04-17 逝于哥本哈根，享年 81 岁）
- **气质关键词**：**维生素 K 的发现者、胆固醇实验的意外收获者、凝血密码的破译人**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1943 条目，Dam 半边口径）：
  > "for his discovery of vitamin K"（因其发现维生素 K）
- **设计母题**：**凝血的开关（the coagulation switch）**——无胆固醇饲料的小鸡出血不止、补胆固醇无效——缺失的是另一因子；用「血滴与网络化的纤维蛋白丝」作背景母题：散落的红点被渐次织入金色网格。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Henrik_Dam/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Henrik_Dam/`（有 1946 与妻子斯德哥尔摩合影，见 images.txt）。Makefile 复制后设 `MAIN=Henrik_Dam_zh`、`VIDEO_NAME=Henrik_Dam_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Dam 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 维生素 K 发现（Koagulationsvitamin），1943 诺奖核心 | 封面、核心页 |
| 1 | physiology | 生理学 | 维生素 K 的生理功能 | 核心页 |
| 2 | hematology | 血液学 | 凝血机制与出血病变 | 核心页 |
| 3 | sterol biochemistry | 甾醇生物化学 | 博士论文：甾醇的生物学意义（1934） | 早年页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Fritz Pregl | 对方 → 导师 | 1925 格拉茨大学随 Pregl 学微量化学（infobox Academic advisors；库内既有 id=3522，1923 诺贝尔化学奖得主） |
| co-honored | Edward Adelbert Doisy | 无向 | 1943 诺贝尔生理学或医学奖共享（Dam 发现维生素 K / Doisy 确定其化学性质） |

**不入库但提示词可叙述**：妻子（1946 斯德哥尔摩合影出现，**page.md 全文未给姓名**，不建 spouse 边，陷阱表注明）；Ontario 农学院三人组 McFarlane/Graham/Richardson（其氯仿脱脂饲料实验被 Dam 复制——实验源头，非个人关系）；哥本哈根/罗切斯特的机构同事。

## 五、配色方案 【人物专属】

- **气质**：丹麦式的清冽、实验意外之美、凝血的红与金
- **主色**：`#175E54`（峡湾青绿——哥本哈根实验室的冷静观察）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeK` 维生素 K — 青绿 `#175E54`
  - `badgeCoag` 凝血机制 — 深红 `#8C1F28`
  - `badgeSterol` 甾醇化学 — 深蓝 `#16324F`
  - `badgeRoch` 罗切斯特岁月 — 灰紫 `#46356B`
- **背景母题**：血滴与渐次织成的纤维蛋白金色网格。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 维生素 K 的发现者 / Henrik Dam 1895–1976 + 四色 badge + 右上头像 + 国籍行（Denmark）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、哥本哈根出身、哥本哈根理工学院化学 1920、
    格拉茨微量化学 1925、哥本哈根博士 1934、诺奖 1943、核心领域）
03  核心贡献概览 — 维生素 K 的发现 / 凝血功能 / 甾醇研究 / 罗切斯特时期
04  哥本哈根求学与教职 (1895–1923) — 理工学院化学学位 1920；农兽医学院助教
05  格拉茨：Pregl 门下 (1925) — 微量化学训练；1923 诺奖化学得主的传授
06  哥本哈根生化研究所 (1928–1934) — 助理教授；1934 甾醇博士论文
07  无胆固醇饲料实验（核心贡献页）— 复制 OAC 氯仿脱脂饲料：小鸡出血
08  补胆固醇无效 — 缺的不是胆固醇而是「第二因子」——凝血维生素
09  命名维生素 K — 德文 Koagulationsvitamin 首报于德国期刊，故得字母 K
10  与 Doisy 的双线 — Dam 发现功能性因子 / Doisy 分离并定其化学性质；平行而互补
11  罗切斯特岁月 (1942–1945) — 高级研究员；1943 获奖于旅美期间；1946-12-12 诺奖演讲
12  荣誉与认可 — 1943 诺奖；1951 首届林道诺奖得主会议七人之一
13  维生素 K 的医学意义 — 凝血功能与治疗应用的现代地位
14  遗产与结尾 — 从意外出血到新生儿维生素 K 常规 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1943 共享但理由句不同 | Dam 半边 "for his discovery of vitamin K"；Doisy 半边 "for his discovery of the chemical nature of vitamin K"——**发现 vs 化学性质**，两句不可互换 |
| page.md 的转述句 | page.md 开头写 "for joint work with Edward Doisy in discovering vitamin K"——这是 Wikipedia 叙述口径；获奖理由以 citations json 官方句为准 |
| 妻子无姓名 | 1946 斯德哥尔摩合影有妻子出镜，但 page.md 全文未给姓名——禁建 spouse 边、禁杜撰姓名 |
| Pregl 身份 | Fritz Pregl 是 1923 诺贝尔化学奖得主（微量分析），1925 年 Dam 随其学微量化学——师承边成立（正文+infobox 双明载），note 点明其诺奖身份 |
| 实验源头归属 | 氯仿脱脂小鸡饲料实验是 Ontario 农学院 McFarlane/Graham/Richardson 首报、Dam 复制并深挖——「复制他人实验后的意外发现」是叙事亮点，勿写成 Dam 凭空首创 |
| 双重职位年份 | 1928 与 1929 哥本哈根生化研究所两个助理教授任命（page.md 两句并列）——按原文转述，勿擅自合并 |
| 博士论文 | 1934 年提交哥本哈根：甾醇的生物学意义（丹麦文标题）——胆固醇实验与此线相承 |
| 旅美与获奖 | 1942–45 罗切斯特大学高级研究员，1943 获奖于旅美期间；诺奖演讲 1946-12-12 |
| 页面较短 | page.md 材料有限——宁可从简（15 页规划已含封面/结尾），禁杜撰生平细节补页 |
| 林道会议 | 1951 首届林道诺奖得主会议，Dam 为出席的七位得主之一（与 Domagk 同场，可交叉提示但不建边） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| vitamin K | 维生素 K | K=德文 Koagulationsvitamin（凝血维生素） |
| coagulation | 血液凝固 | 维生素 K 的生理功能域 |
| cholesterol-free diet | 无胆固醇饲料 | 关键实验条件 |
| chloroform extraction | 氯仿提取（脱脂） | OAC 实验方法，溶出第二因子的操作 |
| hemorrhage | 出血 | 小鸡模型病变 |
| sterol | 甾醇 | 博士论文主题（胆固醇属甾醇类） |
| microchemistry | 微量化学 | Pregl 门下所学 |
| biochemistry | 生物化学 | 主领域 |
| fat-depleted chow | 脱脂饲料 | 实验变量 |
| dietary deficiency | 营养缺乏 | 维生素类发现的方法学背景 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Ascension**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从复制他人实验的意外出血，到为丹麦摘得战时诺奖、再到林道会议的 setter 位——「攀升」对应其由技术员到诺奖得主的稳步上升线；旋律的开阔感也贴合维生素 K 从实验室意外走向新生儿常规护理的普及之路。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Henrik_Dam/Ascension.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
