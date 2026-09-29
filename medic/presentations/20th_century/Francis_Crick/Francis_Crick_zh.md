# 医学家立传提示词（Francis Crick）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1962 年得主（与 Watson/Wilkins 三人共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Francis Harry Compton Crick（1916-06-08 生于北安普敦 Weston Favell ~ 2004-07-28 逝于圣迭戈，享年 88 岁）
- **气质关键词**：**DNA 双螺旋的共同发现者、中心法则的提出者、从分子生物学转向意识之谜的终身提问者** —— 1962 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，三人共享同一句）：
  > "for their discoveries concerning the molecular structure of nucleic acids and its significance for information transfer in living material"
  > （因他们发现核酸的分子结构及其在生命物质中信息传递的意义）
- **设计母题**：**双螺旋与信息之流（the double helix & the flow of information）**。互补碱基对的氢键、DNA→RNA→蛋白质的信息流箭头——"生命的字母表被读懂的那一刻"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Francis_Crick/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Francis_Crick/page.md`；目录 `medic/presentations/20th_century/Francis_Crick/`；Makefile 改 `MAIN=Francis_Crick_zh`；肖像优先 images.txt 所列 Commons 图，失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Francis_Crick.yaml` 一致，勿重复入库；库内既有 stub id=1796 已 UPD 回填）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | molecular biology | 分子生物学 | 职业主领域，双螺旋与中心法则 | 核心页 |
| 1 | genetics | 遗传学 | 遗传密码与 adaptor 假说 | 密码页 |
| 2 | biophysics | 生物物理学 | X 射线衍射出身 | 早年页 |
| 3 | neuroscience | 神经科学 | Salk 期意识研究 | 意识页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Max Perutz | 师→本人 | Cavendish 博士导师（1954，多肽与蛋白 X 射线研究） |
| colleague | James Watson | 无向 | 1951-53 卡文迪什合作者，双螺旋共同发现者 |
| co-honored | James Watson | 无向 | 1962 诺贝尔生理学或医学奖三人共享（核酸分子结构） |
| colleague | Maurice Wilkins | 无向 | 挚友，King's College 数据共享的关键纽带 |
| co-honored | Maurice Wilkins | 无向 | 1962 诺贝尔生理学或医学奖三人共享（核酸分子结构） |
| controversy | Rosalind Franklin | 无向 | Photo 51 与 MRC 报告数据未经其知情被使用，学界长期争议 |
| influence | Erwin Chargaff | 无向 | Chargaff 比例（A=T/G=C）为碱基配对关键约束 |
| colleague | Sydney Brenner | 无向 | 卡文迪什与 MRC LMB 长期并肩，mRNA 概念与三联密码合作 |
| spouse | Ruth Doreen Dodd | 无向 | 1940 结婚，1947 离异，子 Michael |
| spouse | Odile Speed | 无向 | 1949 结婚，绘双螺旋草图者，育二女 |

> 对手方规范名：`Max Perutz`(2066)/`Linus Pauling`(2034)/`John Kendrew`(2067)/`Sydney Brenner`(3873)/`James Watson`(3787) 沿用库内记录——**Perutz advisor-student 边与 Brenner colleague 辑已由他批入库，本篇幂等合并不重复**；`Rosalind Franklin`/`Maurice Wilkins`/`Erwin Chargaff`/`Ruth Doreen Dodd`/`Odile Speed` 新建 stub。

## 五、配色方案

- **气质**：战时工程师的锋利 + 剑桥双螺旋的智性狂欢 + 圣地亚哥海边的终极提问
- **主色**：双螺旋深蓝 `#1F3A6E`（B-DNA 的经典配色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 双螺旋 — 螺旋蓝 `#2E6E9E`
  - `badgeB` 中心法则与遗传密码 — 信息金 `#C9A227`
  - `badgeC` 意识研究 — 神经紫 `#5E4B8B`
  - `badgeD` 争议与人文 — 档案灰红 `#A63A2B`
- **背景母题**：低透明度反向平行双螺旋 + DNA→RNA→蛋白信息流箭头。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — DNA 双螺旋的共同发现者 / Francis Crick 1916–2004 + 三人共享 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Weston Favell、UCL BSc 1937、剑桥 PhD 1954、卡文迪什/LMB/Salk、诺奖 1962）
03  核心贡献概览 — 双螺旋 / 中心法则 / 遗传密码与 adaptor / 意识的 Astonishing Hypothesis
04  鞋厂之家与 Mill Hill (1916–1937) — 祖父与达尔文通信、叔叔的棚屋里吹玻璃做实验、12 岁拒绝上教堂、Mill Hill 奖学金、UCL 物理
05  战争改写的人生 (1937–1947) — Andrade 门下"最无聊的水的黏度"博士课题被炸弹摧毁、海军部反磁性/声学水雷设计、布鲁克林博士后
06  "重生"转向生物学 (1947–1949) — Strangeways 实验室细胞质研究、薛定谔《生命是什么》与 Pauling 的吸引、自嘲物理学教会他"hubris"
07  Perutz 门下与卡文迪什 (1949–1951) — 蛋白质 X 射线晶体学、螺旋衍射理论（Cochran/Vand）、Bragg 与 Pauling 的竞赛背景
08  1951-53：双螺旋的攻坚（核心页一）— Watson 相遇（35 岁博士生 vs 23 岁博士）、Photo 51 与 Franklin 的化学洞见、Chargaff 比例、Donohue 确认碱基构型、1953-02-28 发现、1953-04-25 Nature
09  数据之惑（诚实一页）— Franklin 数据未经知情使用的长期争议（三个来源并列）、Wilkins 拒共同署名、Franklin 两稿几乎同时到达 Acta Crystallographica——客观呈现各方陈述
10  中心法则与 adaptor（核心页二）— 1956 adaptor 假说（后证实为 tRNA）、1958 蛋白合成要点清单、DNA→RNA→蛋白、"dogma"一词的误读注记；与 Brenner 1960-04-15 意识到 mRNA≠rRNA
11  三联密码的证实 — Crick, Brenner et al. 实验；Nirenberg 合成 RNA 破译密码、Crick 邀其向大会重讲的美谈
12  1962 诺贝尔奖 — 与 Watson、Wilkins 三人共享（Franklin 1958 已逝，page.md 未展开此点勿妄加）；官方理由全句；Lasker 1960/Gairdner 1962/Copley 1975/OM 1991；拒 CBE 1963
13  Salk 与意识 (1976–2004) — 1958 剑桥遗传学教授被拒的旧事（Watson 2003 揭评）、1976 迁加州、与 Koch 的意识合作（1990-2005）、reverse learning 假说、The Astonishing Hypothesis
14  人文与身后 — 无神论/人文主义者（引 Humanist Manifesto 2003 签署、Churchill College 辞职抗议）、1970s Directed panspermia 与 Orgel 的思辨（客观一句）、2004-07-28 逝于圣迭戈骨灰撒太平洋、诺奖章 2013 拍卖 227 万美元
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1962 三人共享同一句理由（Crick/Watson/Wilkins）；**Franklin 1958 年已去世未获奖**——页面未展开此点，行文勿杜撰评审内幕 |
| 数据争议 | Franklin 数据使用系学界长期争议（三个数据来源：1951 讲座/Wilkins 讨论/MRC 报告）——**四方事实并列客观呈现**，勿写"窃取"或"完全正当"任一极端；Crick 到模型发表后才见 Photo 51 原图系页面明载 |
| Wilkins 双行 | colleague（挚友+数据纽带）+ co-honored 双行；其曾拒绝在 Nature 论文署名——细节勿混 |
| 中心法则 | "dogma"原意为"有说服力但证据尚少的观念"而非"不可质疑的教条"——页面明载误读注记，须写入 |
| Franklin 时序 | 其 A 型两稿 1953-03-06 抵 Acta Crystallographica、比模型完成早一天；她本人也提出反平行骨架——贡献表述给足 |
| 敏感条目三则 | ①eugenics 私信观点②LSD 传言（身后传闻、时代 1960s 非发现期）③Nancy Hopkins 指控（当事人陈述）——**立传一律省略**，仅陷阱表留存；如 Review 要求补写须标注"指控/传闻"性质 |
| 宗教观 | 人文主义/无神论立场 page.md 大量明载——可客观一句（Humanist Manifesto 签署、Churchill 辞职），引原文需克制 |
| Directed panspermia | 与 Orgel 的定向泛种论系思辨假说，其本人后来自认对地球生命起源"unduly pessimistic"——一句带过，勿写成主张 |
| 家庭 | 两任妻子：Doreen Dodd（1940-1947，子 Michael）；Odile Speed（1949 起，画双螺旋Nature 草图的插画家，二女 Jacqueline 2011 先逝）——双 spouse 行 |
| 库内既有边 | Perutz advisor-student、Brenner colleague、Pauling influence、Walker/Kornberg 边均已由他批写入——本篇幂等合并，不删不改 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| double helix | 双螺旋 | 反向平行骨架 |
| central dogma | 中心法则 | DNA→RNA→蛋白，信息单流 |
| adaptor hypothesis | 接头假说 | 后证实为 tRNA |
| sequence hypothesis | 序列假说 | 碱基序列决定氨基酸 |
| wobble hypothesis | 摆动假说 | 密码子第三位简并性 |
| Photo 51 | 51 号照片 | Franklin/Gosling 的 B 型 DNA 衍射图 |
| Chargaff's rules | 查加夫法则 | A=T、G=C 比例 |
| directed panspermia | 定向泛种论 | 1970s 与 Orgel 的思辨 |
| reverse learning | 反向学习 | 1983 REM 睡眠假说 |

## 九、背景音乐选择

- **选定曲目**：**Awaken** — Alex-Productions（manifest 预分配）
- **匹配理由**："觉醒/揭开"贴合 1953-02-28 那个读懂生命字母表的上午——双螺旋的发现是分子生物学的觉醒时刻；带推进感的曲式亦容纳其晚年向意识之谜的再度进发。
- **本地路径**：music_audio/ 下 Alex-Productions Awaken 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
