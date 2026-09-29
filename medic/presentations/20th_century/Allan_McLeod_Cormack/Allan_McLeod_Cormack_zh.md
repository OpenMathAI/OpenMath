# 医学家立传提示词（Allan McLeod Cormack）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1979 年**得主（与 Godfrey Hounsfield 共享）。
> 本文件是 Cormack 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Allan MacLeod Cormack（1924-02-23 ~ 1998-05-07，享年 74 岁），南非/美国物理学家
- **气质关键词**：**CT 的理论奠基者、无博士学位的诺奖得主、从开普敦到塔夫茨的物理学家** —— 1979 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for the development of computer assisted tomography"（因其开发计算机辅助断层成像）
- **设计母题**：**数学切出的切片（slices made by mathematics）**。不用一刀而「看穿」头颅——以「头颅轮廓内一叠平行的重建切片」作为 CT 的视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Allan_McLeod_Cormack/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Allan_McLeod_Cormack/`；Makefile 复制后设 `MAIN=Allan_McLeod_Cormack_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | computed tomography | 计算机断层成像 | 1979 诺奖核心：CT 理论基础 | 核心页 |
| 1 | physics | 物理学 | 本业：粒子物理（塔夫茨教授） | 任职页 |
| 2 | x-ray technology | X 射线技术 | 副业兴趣引出 CT | 研究页 |
| 3 | crystallography | 晶体学 | 开普敦硕士方向（1945） | 早年页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Godfrey Hounsfield | 无向 | 1979 诺贝尔生理学或医学奖共享（CT；两地独立互不合作） |
| spouse | Barbara Seavey | 无向 | 剑桥相识的美国物理学生，1950 同返开普敦 |

**方向约定**：无向关系 from<to 自动归一。

## 五、配色方案 【人物专属】

- **气质**：理论家的冷静、南非与剑桥的双重底色、CT 层片的秩序感
- **主色**：`#46627F`（断层蓝灰，扫描层片）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeCT` 断层成像 — 层片蓝 `#46627F`；`badgeMath` 重建数学 — 理论青 `#1B6B6B`；`badgeUCT` 开普敦岁月 — 好望角金 `#A8752F`；`badgeTufts` 塔夫茨岁月 — 学院红 `#8C4A3A`
- **背景母题**：蓝灰底上头颅轮廓内一叠平行切片线，每片间以细亮线分隔，错落延展。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 数学切开的视界 / Allan MacLeod Cormack 1924–1998 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、约翰内斯堡、开普敦/剑桥、塔夫茨、荣誉）
03  核心贡献概览 — CT 理论 / 重建算法 / 两篇论文 / 与 Hounsfield 的独立双线
04  约翰内斯堡到开普敦 (1924–1944) — Rondebosch 男校、辩论与网球队、1944 物理 BS
05  晶体学硕士与剑桥 (1944–1949) — 1945 晶体学 MSc、1947-49 剑桥博士生、遇见 Barbara Seavey
06  开普敦讲师与哈佛访学 (1950–1957) — 1956-57 哈佛休假、决定移居美国
07  塔夫茨物理学教授 (1957–) — 1957 秋上任、粒子物理主业、1966 入美国籍
08  副业的伏笔 (1956–1957)（核心贡献页）— 开普敦/格鲁特·舒尔医院起步、X 射线剂量问题的重建数学
09  两篇论文 (1963–1964) — Journal of Applied Physics、学界几无回应的十年
10  Hounsfield 的工程实现 (1971) — 英国首台 CT 扫描仪、理论落地为应用
11  1979 诺贝尔奖 — 两人「不同大陆、互不合作」做出同类装置、共享物理或医学奖
12  无博士学位的诺奖得主 — 「significant and unusual achievement」：无任何领域博士学历
13  荣誉 — 1990 国家科学奖章、美国物理学会会士、慕尼黑国际科学院成员
14  身后之荣 — 1998 卒于 Winchester；2002 追授南非 Order of Mapungubwe 金质勋章（共同发明 CT）
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 姓氏拼写 | 标题栏作 Allan **MacLeod** Cormack、页面名/Wikidata 作 McLeod——目录名与 yaml 用 manifest 形式 McLeod，行文可从页面 MacLeod；两种拼写并存需注明 |
| 生卒日 | 1924-02-23 生于约翰内斯堡；1998-05-07 卒于 Winchester, Massachusetts（癌症），享年 74 |
| 获奖理由 | "for the development of computer assisted tomography"——**their**（与 Hounsfield 共享） |
| 双线独立 | 正文强调两人「不同大陆、互不合作」做出非常相似的装置——独立发现叙事是本篇灵魂，勿写成协作 |
| 无博士学位 | "did not hold a doctoral degree in any scientific field"——医学诺奖得主的罕见背景，正文明载的「significant and unusual achievement」 |
| 分工表述 | Cormack 是**理论奠基**（1963/1964 两篇论文），Hounsfield 是 1971 **首台扫描仪的工程实现**——功劳链勿倒 |
| 十年冷遇 | 两篇论文发表后「generated little interest」——被忽视的十年是叙事张力 |
| 国籍口径 | manifest/Nobel 官方为 United States（1966 入籍）；生于南非——表述「南非/美国物理学家」，南非追授勋章可写 |
| 剑桥身份 | 1947-49 为剑桥博士生阶段但未获博士学位——勿写成博士毕业；导师未载不建边 |
| 引语 | 本页正文无直接引语——引号内不得出现「原话」 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| computed tomography (CT) | 计算机断层成像 | 诺奖理由核心词 |
| computer assisted tomography | 计算机辅助断层成像 | citation 原文措辞 |
| x-ray computed tomography | X 射线 CT | 具体模态 |
| reconstruction | 重建（算法） | 由投影复原切片 |
| crystallography | 晶体学 | 硕士方向 |
| particle physics | 粒子物理 | 其本业 |
| Order of Mapungubwe | 马普古布韦勋章 | 2002 南非追授（金级） |
| Tufts University | 塔夫茨大学 | 1957 起教职 |
| Groote Schuur Hospital | 格鲁特·舒尔医院 | CT 思想起点 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Empire Collapse** — Alex-Productions（manifest 预分配）
- **风格**：厚重 / 沉郁 / 大结构感
- **匹配理由**：一篇被冷落十年的两页论文，最终重构了整个医学影像的版图——Empire Collapse 的大结构感匹配「旧秩序被数学切片重写」的主题，也匹配其身后南非以最高勋章追认的迟来加冕（第二次使用该曲，首用 Corbató，同为体系重构者）。
- **本地路径**：`music_audio/` 下 Empire Collapse 曲目 → 复制为 `presentations/20th_century/Allan_McLeod_Cormack/Empire_Collapse.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

