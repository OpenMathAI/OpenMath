# 医学家立传提示词（Thomas Huckle Weller）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1954 年得主（托马斯·韦勒，脊髓灰质炎病毒组织培养的共同发明人）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Thomas Huckle Weller（1915-06-15 生于密歇根州安娜堡 ~ 2008-08-23 卒于马萨诸塞州尼德姆，享年 93 岁）
- **气质关键词**：**把脊髓灰质炎病毒"请进"试管的组织培养先驱、从鱼寄生虫到热带公共卫生的宽域研究者、水痘病毒的首位分离者** —— 1954 获奖理由（与 John Franklin Enders、Frederick Chapman Robbins 三人共享）：
  > "for their discovery of the ability of poliomyelitis viruses to grow in cultures of various types of tissue"（因发现脊髓灰质炎病毒可在多种类型的组织培养物中生长）
- **设计母题**：**试管里的病毒**。在人胚皮肤与肌肉组织组合中培养脊灰病毒——疫苗之路由此打开。视觉隐喻：一排培养管中的淡色组织块与游动的病毒颗粒，向外连接出疫苗的剪影。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Thomas_Huckle_Weller/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Thomas_Huckle_Weller/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Thomas_Huckle_Weller/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Thomas_Huckle_Weller_zh`、`VIDEO_NAME=Thomas_Huckle_Weller_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Thomas_Huckle_Weller/images.txt`（1954 诺奖肖像）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Thomas_Huckle_Weller.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 脊灰病毒组织培养，1954 诺奖核心 | 核心页 |
| 1 | tissue culture | 组织培养 | 人胚皮肤+肌肉组织组合的关键方法 | 核心页 |
| 2 | parasitology | 寄生虫学 | 硕士论文鱼寄生虫；血吸虫病治疗贡献 | 早年页 |
| 3 | tropical public health | 热带公共卫生 | 1954 起哈佛公共卫生学院热带公共卫生系主任 | 身份页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John Franklin Enders | 导师 | 1939 起在 Enders 门下进入病毒与组织培养研究（哈佛医学院/波士顿儿童医院） |
| co-honored | John Franklin Enders | 无向 | 1954 诺贝尔生理学或医学奖三人共享（脊髓灰质炎病毒可在多种组织培养物中生长） |
| co-honored | Frederick Chapman Robbins | 无向 | 1954 诺贝尔生理学或医学奖三人共享（脊髓灰质炎病毒可在多种组织培养物中生长） |
| parent-child | Carl Vernon Weller | 父 | 父，密歇根大学病理学系教授 |
| spouse | Kathleen Fahey | 无向 | 1945 结婚，育二子二女，2011 年以 95 岁去世 |

> relations=5 为诚实值，Review 勿误判缺漏。
> 不入库：二战 Antilles 医学实验室上下级；Armed Forces Epidemiological Board 寄生虫病委员会（机构职务）；四名子女未具名于 page.md。
> 库内当时无 John Franklin Enders / Frederick Chapman Robbins / Carl Vernon Weller / Kathleen Fahey 记录，均由本 yaml 新建 stub——**Enders/Robbins 若由 med-batch-13（1954 同届）agent 规范化，将按名幂等回填**。

## 五、配色方案 【人物专属】

- **气质**：安娜堡的学术蓝 + 培养管的透明质感 + 热带公共卫生的深绿
- **主色**：培养管青蓝 `#1E5F74`（玻璃与培养液的冷静色，亦是"病毒学实验室"的底色）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 脊灰病毒培养 — 培养管青蓝 `#1E5F74`
  - `badgeB` 组织培养方法 — 琥珀 `#A0722D`
  - `badgeC` 寄生虫与热带医学 — 深绿 `#2F6B4F`
  - `badgeD` 战时军医岁月 — 灰蓝 `#4A5A6A`
- **背景母题**：一排竖直培养管细线 + 管内淡色圆点（组织块/病毒斑），四色错落。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 脊灰病毒的组织培养者 / Thomas Huckle Weller 1915–2008 + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Ann Arbor、教育 Michigan BS/MS/
    Harvard MD 1940、导师 Enders、任职波士顿儿童医院/哈佛公卫学院、
    荣誉 Nobel 1954/Mead Johnson 1953/Walter Reed 1996、核心领域）
03  核心贡献概览 — 脊灰病毒的组织培养 / 水痘病毒首分 / 巨细胞病毒与风疹 / 热带寄生虫病
04  安娜堡与病理学系家庭 (1915–1936) — 生于并长于安娜堡、Ann Arbor High School、
    父 Carl Vernon Weller 为密歇根大学病理学系教授、
    密歇根大学医学动物学 BS/MS（硕士论文鱼寄生虫）
05  哈佛与 Enders 门下 (1936–1942) — 1936 入哈佛医学院、1939 起随 Enders 研究
    病毒与组织培养技术、1940 MD、波士顿儿童医院
06  战时军医 (1942–1945) — 陆军医疗队、安的列斯医学实验室（波多黎各）、
    少校军衔、统辖细菌学/病毒学/寄生虫学三部门
07  重返儿童医院与传染病研究部 (1945–1954) — 1945 与 Kathleen Fahey 结婚、
    1947 重返波士顿儿童医院加入 Enders 新建的传染病研究部、
    脊灰病毒在人胚皮肤与肌肉组织组合中培养成功
08  1954 诺贝尔奖 — 三人共享官方理由逐字引用、1954-07 出任哈佛公卫学院
    热带公共卫生系主任、1954-12-11 Nobel Lecture "The Cultivation of the Poliomyelitis
    Viruses in Tissue Culture"
09  超越脊灰：水痘与巨细胞病毒 — 首次分离水痘病毒、
    1954 George Ledlie 奖表彰其在风疹/脊灰/巨细胞病毒上的研究
10  血吸虫病与热带医学 — 血吸虫病治疗贡献、Coxsackie 病毒研究、
    1953-1959 美国武装部队流行病学委员会寄生虫病委员会主任
11  荣誉与认可 — E. Mead Johnson Award 1953、Nobel 1954、
    Walter Reed Medal 1996（美国热带医学与卫生学会）
12  学术生涯收官 — 哈佛公卫学院热带公共卫生系主任（1954 起）、
    多个领导职务、2008-08-23 卒于尼德姆（93 岁）
13  个人生活 — 妻 Kathleen Fahey（1945 结婚、2011 逝）、二子二女
14  遗产 — 组织培养打开疫苗时代之门（Salk/Sabin 疫苗的前置技术）、
    Enders-Weller-Robbins 三人组的"在浑水中钓鱼"、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discovery of the ability of poliomyelitis viruses to grow in cultures of various types of tissue"（三人共享、their）；本页另有泛称"因脊灰研究"——引用以 citation json 为准 |
| 三人分工 | Enders 是导师与团队核心、Weller 与 Robbins 是组织培养的执行关键——本篇以 Weller 视角：1939 入门 → 战时中断 → 1947 重返 → 培养成功；勿把方法发明全归于 Enders |
| 培养材料 | page.md 明载"人胚皮肤与肌肉组织的组合"（human embryonic skin and muscle tissue）——材料表述精确，勿写成"猴肾"（那是后续疫苗生产方法，page 未载） |
| 父亲身份 | Carl Vernon Weller 系密歇根大学病理学系教授（page.md 明载）——parent-child 入库；注意其 wiki 链接为红链 |
| 学位口径 | 密歇根 BS+MS（医学动物学、硕士论文鱼寄生虫）+ 哈佛 MD 1940——无 PhD；勿写成"博士" |
| 军衔与部门 | 战时少校、统辖安的列斯医学实验室细菌/病毒/寄生虫三部门——具体勿泛化为"军医" |
| 水痘病毒 | "首位分离水痘（varicella）责任病毒者"——page.md 明载 first，勿弱化为"参与" |
| Ledlie 奖 | 1954 George Ledlie 奖表彰风疹+脊灰+巨细胞病毒三线研究——别与诺奖年份混淆成同年同因 |
| 在世者规则 | 本篇主角 2008 年逝，无在世问题；relations=5 系 page.md 所限诚实值 |
| 姓名拼写 | Thomas Huckle Weller（中间名 Huckle 勿丢）；dir 名与 yaml 文名一致 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| poliomyelitis | 脊髓灰质炎 | 俗称小儿麻痹 |
| tissue culture | 组织培养 | 人胚皮肤+肌肉组合 |
| varicella | 水痘 | 首次分离其病毒 |
| cytomegalovirus (CMV) | 巨细胞病毒 | Ledlie 奖对象之一 |
| rubella | 风疹 | Ledlie 奖对象之一 |
| schistosomiasis | 血吸虫病 | 热带医学贡献 |
| medical zoology | 医学动物学 | 其本科-硕士专业 |
| Antilles Medical Laboratory | 安的列斯医学实验室 | 战时驻地波多黎各 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Invisible Light**（manifest 预分配）
- **风格**：微光 / 静谧 / 探微
- **匹配理由**：肉眼不可见的病毒在试管中首次"被养活"——The Invisible Light 的微光质感匹配"让看不见的敌人显形"的组织培养叙事，亦呼应其一生在寄生虫与热带病这些"被忽视的暗处"工作。
- **本地路径**：`music_audio/alex-productions/` 下 The Invisible Light 对应文件（执行时以 `find music_audio -iname "*Invisible*"` 实际定位）→ 复制为 `presentations/20th_century/Thomas_Huckle_Weller/The_Invisible_Light.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；培养材料表述与三人分工务必精确。**
