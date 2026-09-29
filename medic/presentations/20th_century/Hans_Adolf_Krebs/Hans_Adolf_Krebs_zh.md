# 医学家立传提示词（Hans Adolf Krebs）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1953 年**得主（与 Fritz Albert Lipmann 共享，各得一半）。
> 本文件是 Krebs 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Hans Adolf Krebs（1900-08-25 ~ 1981-11-22，享年 81 岁），德裔英籍医师、生物化学家
- **气质关键词**：**两个代谢循环的发现者、纳粹驱逐的流亡者、谢菲尔德「Krebs 帝国」的建造者** —— 1953 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for his discovery of the citric acid cycle"（因其发现柠檬酸循环）
- **设计母题**：**循环之轮（the cycle's wheel）**。柠檬酸循环首尾相接的代谢之环——以「闭环箭头链上八枚中间代谢物小圆」作为全篇视觉隐喻（其 1932 尿素环是史上首个代谢循环）。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Hans_Adolf_Krebs/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Hans_Adolf_Krebs/`；Makefile 复制后设 `MAIN=Hans_Adolf_Krebs_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 1953 诺奖核心 | 核心页 |
| 1 | metabolism | 代谢 | 柠檬酸循环/尿素循环/乙醛酸循环 | 核心页 |
| 2 | cellular respiration | 细胞呼吸 | 耗氧量测压法研究主线 | 研究页 |
| 3 | internal medicine | 内科学 | 医学出身、弗赖堡内科诊所行医 | 早年页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Wilhelm von Mollendorf | 师→生（早期导师） | 1920-23 组织染色法首篇论文在其指导下完成 |
| advisor-student | Otto Heinrich Warburg | 师→生（研究所导师） | 1926 入柏林达勒姆 Kaiser Wilhelm 生物学研究所，师从四年 |
| advisor-student | Kurt Henseleit | 生（Krebs→学生） | 医学生，1932 合作确立尿素循环（Krebs–Henseleit） |
| colleague | William Arthur Johnson | 无向 | 谢菲尔德合作确立柠檬酸循环（1937） |
| colleague | Hans Kornberg | 无向 | 1957 合作发现乙醛酸循环 |
| colleague | Frederick Gowland Hopkins | 无向 | 1933 因犹太出身被解职后即援手，招其入剑桥 |
| co-honored | Fritz Albert Lipmann | 无向 | 1953 诺贝尔生理学或医学奖共享（各得一半） |
| spouse | Margaret Cicely Fieldhouse | 无向 | 1938-03-22 结婚，「谢菲尔德的 19 年快乐时光」 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；`direction: student` = 对方是学生；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：德意志的严谨、流亡的坚韧、循环图谱的秩序美
- **主色**：`#2F4858`（代谢青灰，测压计与循环图）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeTCA` 柠檬酸循环 — 循环青 `#1B6B6B`；`badgeUrea` 尿素循环 — 尿素蓝 `#3B4E8C`；`badgeExile` 流亡与重建 — 流亡灰 `#5A6B7A`；`badgeMano` 测压法 — 仪器铜 `#A8752F`
- **背景母题**：青灰底上一枚环形箭头链（八节点闭环，首尾相接），如代谢循环简图散布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 代谢之环的发现者 / Hans Adolf Krebs 1900–1981 + 四色 badge + 右上肖像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Hildesheim、哥廷根/弗赖堡、剑桥/谢菲尔德/牛津、荣誉）
03  核心贡献概览 — 柠檬酸循环 / 尿素循环 / 乙醛酸循环 / Krebs–Henseleit 缓冲液
04  希尔德斯海姆与一战 (1900–1918) — 耳鼻喉外科医生之子、1918 应征入伍、紧急中学考试
05  医学生涯起点 (1918–1925) — 哥廷根→弗赖堡、Mollendorf 指导首篇论文、1925 汉堡医学博士
06  Warburg 门下四年 (1926–1930) — 达勒姆研究所、16 篇论文、测压计技术、被导师劝离单飞
07  弗赖堡与尿素循环 (1930–1933) — 与 Henseleit 1932 确立史上首个代谢循环、Krebs–Henseleit 缓冲液
08  1933 年的驱逐 — 犹太血统触犯《职业公务员法》、4 月解职、Hopkins 即刻援手、洛克菲勒基金资助剑桥
09  带走的关键行李 — Warburg 测压计与研究样品——日后全部发现的技术根基
10  谢菲尔德 19 年 (1935–1954) — 药理学讲师→生物化学系首任主任、「Krebs 帝国」、MRC 细胞代谢研究室
11  柠檬酸循环 (1937)（核心贡献页）— 与 Johnson、鸽胸肌实验、Nature 拒稿插曲、Enzymologia 刊发
12  1953 诺贝尔奖 — 与 Lipmann 共享各半、Lasker 奖同年、Royal Medal 1954 / Copley 1961
13  牛津岁月 (1954–1967) — Whitley 讲席、三一学院研究员、1957 与 Kornberg 乙醛酸循环
14  遗产与身后 — Krebs 循环入教科书、谢菲尔德 Krebs 研究所、2015 奖章拍卖设 Sir Hans Krebs Trust
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1900-08-25 生于 Hildesheim（普鲁士汉诺威省）；1981-11-22 卒于 Oxford，享年 81 |
| 获奖理由 | "for his discovery of the citric acid cycle"——**his**；与 Lipmann 同年共享但**各自理由不同**（Lipmann 是辅酶 A），勿写同一句理由 |
| 「各得一半」 | 正文明确 Lipmann 获一半、Krebs 获另一半——共享结构须写清 |
| 尿素循环先行 | 尿素循环（1932，与 Henseleit）是**史上首个被发现的代谢循环**——先于柠檬酸循环，叙事顺序勿倒 |
| Nature 拒稿 | 1937-06-10 投 Nature、06-14 被拒（「稿件已满七八周」）——学术史趣事，可写 |
| Warburg 的拒绝 | 用测压计检测葡萄糖代谢的设想曾向 Warburg 提出被其断然拒绝——师承与学术分歧并存，表述克制 |
| 1933 驱逐 | 因犹太血统被解职；允许携带的设备与研究样品（尤其 Warburg 测压计）成为日后发现的技术根基——流亡叙事亮点 |
| 家庭 | 1938-03-22 娶 Margaret Cicely Fieldhouse；二子 Paul/John 一女 Helen；子 Sir John Krebs（Baron Krebs）为著名鸟类学家、上议院议员——本批不建 parent-child 边 |
| 国籍口径 | manifest/Nobel 官方为 United Kingdom（1939 归化英籍）——表述「德裔英籍」 |
| 引语 | 正文有引语：「unduly lenient and sympathetic」（ suspected examiners）、「19 happy years」——引语仅用这些，勿自造 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| citric acid cycle | 柠檬酸循环 | 又名 Krebs cycle / TCA cycle |
| urea cycle | 尿素循环 | 又名 ornithine cycle / Krebs–Henseleit cycle |
| glyoxylate cycle | 乙醛酸循环 | 1957 与 Hans Kornberg 发现 |
| Krebs–Henseleit buffer | Krebs–Henseleit 缓冲液 | 生理缓冲灌注液 |
| manometer | 测压计 | Warburg 式，其方法根基 |
| cellular respiration | 细胞呼吸 | 耗氧产能过程 |
| acetyl-CoA | 乙酰辅酶 A | 1947 Lipmann 发现，衔接两环 |
| Whitley Professor | 惠特利生物化学讲席教授 | 牛津 1954-1967 |
| malate synthase / isocitrate lyase | 苹果酸合酶 / 异柠檬酸裂解酶 | 乙醛酸循环关键酶 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**With Me** — Alex-Productions（manifest 预分配）
- **风格**：陪伴感 / 温和 / 叙事
- **匹配理由**：被祖国驱逐的科学家，由 Hopkins 与剑桥「与他同在」——With Me 的陪伴感匹配流亡者重获实验室的温暖，也匹配 Henseleit/Johnson/Kornberg 一路同行的合作者群像。
- **本地路径**：`music_audio/` 下 With Me 曲目 → 复制为 `presentations/20th_century/Hans_Adolf_Krebs/With_Me.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

