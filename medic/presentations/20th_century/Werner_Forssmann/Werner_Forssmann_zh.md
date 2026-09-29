# 医学家立传提示词（Werner Forssmann）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1956 年得主（维尔纳·福斯曼，心导管术的首创者——在自己身上完成第一例）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Werner Theodor Otto Forßmann（Forssmann）（1904-08-29 生于柏林 ~ 1979-06-01 卒于西德朔普夫海姆，享年 74 岁）
- **气质关键词**：**把导管插进自己心脏的孤勇者、被医学界放逐二十七年的先知、心导管术的始祖** —— 1956 获奖理由（与 André Frédéric Cournand、Dickinson W. Richards 三人共享）：
  > "for their discoveries concerning heart catheterization and pathological changes in the circulatory system"（因发现心导管术与循环系统的病理变化）
- **设计母题**：**60 厘米的勇气**。1929 年，一根导尿管从肘前静脉推进 60 厘米抵达右心房——X 光片上那根安静躺在心脏旁的导管，是医学史上最勇敢的"自拍"。视觉隐喻：一条从手臂出发、终于心脏轮廓的导管线，身后是被放逐的漫长阴影。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Werner_Forssmann/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Werner_Forssmann/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Werner_Forssmann/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Werner_Forssmann_zh`、`VIDEO_NAME=Werner_Forssmann_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Werner_Forssmann/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Werner_Forssmann.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cardiac catheterization | 心导管术 | 1929 首例人体自体实验，1956 诺奖核心 | 核心页 |
| 1 | cardiology | 心脏病学 | 直接给药/造影剂/测压的设想 | 核心页 |
| 2 | surgery | 外科学 | Charité 外科训练与临床任职 | 履历页 |
| 3 | urology | 泌尿外科学 | 转行后的长期执业（Bad Kreuznach 等） | 履历页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | André Frédéric Cournand | 无向 | 1956 诺贝尔生理学或医学奖三人共享（心导管术与循环系统病理变化） |
| co-honored | Dickinson W. Richards | 无向 | 1956 诺贝尔生理学或医学奖三人共享（心导管术与循环系统病理变化） |
| colleague | André Frédéric Cournand | 无向 | 战俘被拘期间其 1929 论文为 Cournand/Richards 所读，二人发展出临床应用 |
| colleague | Dickinson W. Richards | 无向 | 战俘被拘期间其 1929 论文为 Cournand/Richards 所读，二人发展出临床应用 |
| colleague | Ferdinand Sauerbruch | 无向 | 柏林 Charité 上司，见其自体实验论文后将其解雇（"外科不能这样开端"） |
| spouse | Elsbet Engel | 无向 | 泌尿科专科医生，1933 结婚，育六子女 |

> relations=6 为诚实值，Review 勿误判虚增。
> 不入库：Gerda Ditzen（1929 自体实验中被说服/被骗的手术室护士——关键事件人物但非持续关系，入幻灯片叙事不入库）；Karl Heusch（Rudolf Virchow 医院泌尿科学习指导，转行训练）；子女六人（Wolf 首分心房利钠肽、Bernd 参与首台临床碎石机——仅作彩蛋叙事）；战俘营美军方；Nazi Party（组织非个人）。
> 库内当时无上述对手方记录，均由本 yaml 新建 stub（Cournand/Richards 由本批各自 yaml 幂等覆盖）。

## 五、配色方案 【人物专属】

- **气质**：X 光片的冷白 + 导管金属的冷光 + 二十七年放逐的暗影
- **主色**：导管钢蓝 `#2E4A66`（X 光显影的金属冷调）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 1929 自体实验 — 导管钢蓝 `#2E4A66`
  - `badgeB` 放逐岁月 — 灰紫 `#5C5470`
  - `badgeC` 泌尿科执业 — 深青 `#0E7C7B`
  - `badgeD` 1956 迟到的承认 — 香槟金 `#D4AF37`
- **背景母题**：一条导管细线从版面左下推进到右上的心脏剪影，线的中段以灰紫暗影断续（放逐年代）。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 心导管术的首创者 / Werner Forssmann 1904–1979 + 四色 badge + 右上头像 + 国籍行 Germany
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生柏林、教育柏林大学（Askanisches
    Gymnasium）、1929 国家考试、任职 Eberswalde/Charité/Dresden-Friedrichstadt/
    Bad Kreuznach/Mainz 荣誉教授、荣誉 Nobel 1956、核心领域）
03  核心贡献概览 — 首例人体心导管术 / 直接给药与造影设想 / 从放逐到诺奖 / 介入心脏病学源头
04  柏林求学 (1904–1929) — Askanisches Gymnasium、柏林大学学医、1929 通过国家考试
05  假设与恐惧 (1928–1929) — 导管可直接入心（给药/注射造影剂/测压）、
    时人普遍认为入心即致命——"用自己的身体证明"
06  1929：Eberswalde 的自体实验 — 无视科室主任、说服护士 Gerda Ditzen 协助、
    以局部麻醉"调包"在自己肘前静脉插入导尿管、行至 X 光科透视下
    再推进 60 厘米达右心室腔、X 光片记录导管位于右心房——首例人体心导管术
07  争议与肯定的第一线 — 主任初怒后见 X 光片认可、允许在绝症女患者上再施导管术
    （给药后病情改善）、获 Charité 无薪职位
08  Sauerbruch 的放逐 — Ferdinand Sauerbruch 见论文后将其解雇
    （引语 "You certainly can't begin surgery in that manner"，可引原文）、
    1932 再因"未达科学预期"被迫离开、1933 与泌尿科医生 Elsbet Engel 结婚后
    退出心脏科转泌尿科
09  战争与战俘 (1932–1945) — 1932-45 为 Nazi Party 党员（客观事实陈述）、
    二战军医升至少校、被俘入美军战俘营——被拘期间 Cournand 与 Richards 读到其论文
10  1945–1956：黑森林的乡村医生 — 伐木工/黑森林乡村医生、1950 Bad Kreuznach
    泌尿科执业——与诺奖之间的漫长沉默
11  1956 诺贝尔奖 — 三人共享（首创者+发展者同台）、Leibniz Medal 1954（德国科学院）为前奏
12  迟来的承认 — Mainz 外科与泌尿科荣誉教授、1961 Córdoba 国立大学荣誉教授、
    1962 德国外科学会执行董事会成员、美国胸科医师学会会员、
    瑞典心脏病学会/德国泌尿学会荣誉会员
13  家庭与身后 — 妻 Elsbet（泌尿专科医生，1993 逝）、六子女、
    彩蛋：子 Wolf 首次分离心房利钠肽（ANP）、子 Bernd 参与首台临床碎石机研制、
    1979-06-01 卒于 Schopfheim（心力衰竭）
14  遗产 — 从自体实验到介入心脏病学（Gruentzig 谱系的源头）、
    医学自体实验伦理的世纪标本、"被放逐的先知"的科学史标本、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries concerning heart catheterization and pathological changes in the circulatory system"（三人共享、their）——首创者是 Forssmann，但理由句为三人共用 |
| 姓名拼写 | 德文 Forßmann（ß）、英文 Forssmann（ss）——正文统一 Forssmann，可在身份页注明德文原名 Forßmann；yaml/库内用 manifest 形式 `Werner Forssmann` |
| Gerda Ditzen 叙事 | 护士 Ditzen 同意协助但要求"在她身上做"，Forssmann 以约束+假装麻醉"调包"在自己身上完成——page.md 明载的戏剧性事件，**如实叙述即可，勿美化"调骗"细节，也不回避**；Ditzen 不入库 |
| Nazi Party ★ | 1932-45 为纳粹党党员——page.md 明载，**客观事实陈述一句带过，置于战时段落，不渲染也不删节** |
| Sauerbruch 引语 | "You certainly can't begin surgery in that manner"（page.md 英文原文在，可引）；解雇因果链（见论文→解雇→离开 Charité→1932 再被迫离开）须分段准确 |
| 技术细节 | 肘前静脉（median cubital vein）、导尿管、60 厘米、右心室腔推进、X 光片示右心房——数字与解剖部位勿错 |
| 转行逻辑 | 名誉受损难求职→弃心脏科转泌尿科（师从 Karl Heusch）——因果链如实，Heusch 不入库 |
| 国籍裁定 ★ | manifest "Germany"；citation json 官方口径 "West Germany"；metadata 列 German Reich/West Germany/German Empire 三朝——yaml 取 Germany(0)，幻灯片国籍行 Germany，出生时属德意志帝国、获奖时属西德的口径可在身份页注明 |
| 子女彩蛋 | Wolf（ANP 首分）与 Bernd（碎石机）——page.md 明载，作为"医学世家"彩蛋一句，不入库 |
| 死因 | 心力衰竭（heart failure）——卒于 Schopfheim，1979-06-01 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| cardiac catheterization | 心导管术 | 1956 诺奖核心 |
| self-experimentation | 自体实验 | 1929 Eberswalde |
| median cubital vein | 肘正中静脉 | 插管部位 |
| fluoroscope | 荧光透视镜 | 推进导管的引导设备 |
| radiopaque dye | 不透 X 光造影剂 | 其设想应用之一 |
| urology | 泌尿外科学 | 转行后的执业领域 |
| atrial natriuretic peptide (ANP) | 心房利钠肽 | 子 Wolf 首次分离（彩蛋） |
| lithotriptor | 碎石机 | 子 Bernd 参与（彩蛋） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Winds Of Freedom**（manifest 预分配）
- **风格**：自由 / 苍凉 / 归来
- **匹配理由**：从被医学界放逐到战俘营、再到黑森林的乡村诊所——Winds Of Freedom 的"自由与归来"气质匹配其 27 年的放逐与 1956 年迟来的正名；那根 60 厘米的导管，是向教条争来的自由。
- **本地路径**：`music_audio/` 下 Winds Of Freedom 对应文件（执行时以 `find music_audio -iname "*Winds*"` 实际定位）→ 复制为 `presentations/20th_century/Werner_Forssmann/Winds_Of_Freedom.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；自体实验细节与 Nazi 党员事实务必按 page.md 客观呈现。**
