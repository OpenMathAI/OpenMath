# 医学家立传提示词（George Whipple）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1934 年**得主（与 George Minot、William P. Murphy 三人共享）。
> 本文件是 Whipple 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：George Hoyt Whipple（1878-08-28 ~ 1976-02-01，享年 97 岁），美国医师、病理学家
- **气质关键词**：**肝疗法的第一人、罗切斯特医学院的缔造者、Whipple 病的命名者** —— 1934 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for their discoveries concerning liver therapy in cases of anaemia"（因其关于贫血的肝疗法发现）
- **设计母题**：**再生之肝（the regenerating liver）**。喂给贫血犬的生肝让红细胞重新充盈——以「肝脏剪影中上升的红细胞曲线」作为全篇视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/George_Whipple/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/George_Whipple/`；Makefile 复制后设 `MAIN=George_Whipple_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | hematology | 血液学 | 1934 诺奖核心：贫血的肝疗法实验基础 | 核心页 |
| 1 | pathology | 病理学 | 约翰霍普金斯病理系出身、罗切斯特病理学主任 | 任职页 |
| 2 | medicine | 医学 | 罗切斯特医学院创院院长 | 建制页 |
| 3 | biochemistry | 生物化学 | 胆色素代谢、血浆蛋白与氨基酸研究 | 研究页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | George Minot | 无向 | 1934 诺贝尔生理学或医学奖共享（贫血肝疗法） |
| co-honored | William P. Murphy | 无向 | 1934 诺贝尔生理学或医学奖共享（贫血肝疗法） |
| spouse | Katherine Ball Waring | 无向 | 1914 结婚，育二子 |
| colleague | Frieda Robscheit-Robbins | 无向 | 研究助手，合著 21 篇，医学创造性伙伴关系 |
| influence | William H. Welch | 无向 | 约翰霍普金斯病理系导师之一 |
| influence | Eugene Opie | 无向 | 约翰霍普金斯病理系导师之一 |
| influence | William McCallum | 无向 | 约翰霍普金斯病理系导师之一 |
| influence | Lafayette Mendel | 无向 | 耶鲁高年级深受其影响（自传原话） |
| colleague | Hans Meyer | 无向 | 1911 维也纳合作研究肝门静脉血流 |
| colleague | Samuel Darling | 无向 | 巴拿马 Ancon 医院共事热带病 |
| colleague | Allen Whipple | 无向 | 同名不同宗的终生好友（Whipple procedure 描述者） |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：新英格兰的质朴、户外人的坚韧、97 岁一生的稳健
- **主色**：`#3D6B35`（再生绿，肝脏与红细胞再生）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeLiver` 肝与再生 — 肝红 `#8C3A26`；`badgeAnemia` 贫血研究 — 血浆橙 `#C0722E`；`badgeRochester` 罗切斯特岁月 — 石板蓝 `#3A5A6E`；`badgeOutdoors` 户外人生 — 林绿 `#4C7A3F`
- **背景母题**：浅绿底上肝脏剪影与上升的红细胞小圆序列，错落铺陈。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 肝疗法第一人 / George Whipple 1878–1976 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Ashland、耶鲁/约翰霍普金斯、UCSF/罗切斯特、荣誉）
03  核心贡献概览 — 贫血肝疗法 / 肝再生 / 胆色素与铁代谢 / 血浆蛋白动态平衡
04  新罕布什尔孤儿 (1878–1900) — 两岁丧父、母训「勤劳与教育」、耶鲁户外人、体操与赛艇
05  约翰霍普金斯 (1901–1914) — Abel 药理系助教、Welch/Opie/McCallum 门下转向病理学
06  巴拿马与海德堡 (1907–1911) — Ancon 医院热带病与黑水热、Krehl/Morawitz 处学兔贫血、维也纳 Hans Meyer
07  肝再生与纤维蛋白原 (1905–1914) — 犬肝细胞近乎无限再生、肝为纤维蛋白原合成场所
08  「重症贫血之血液再生」系列 (1925–)（核心贡献页）— 生肝最有效、动物组织与熟杏亦有益、铁含量与效力关联
09  Whipple 病 — 命名肠源性脂肪营养不良、正确指出细菌病因——与诺奖工作无关勿混
10  从犬到人：Minot 与 Murphy — Holmgren 颁奖词：Whipple 先行、给二人以 idea、恶性贫血由绝症变可治
11  罗切斯特建院 (1921–1953) — Rhees 三顾、创院院长、医学院与医院同址愿景
12  1934 诺贝尔奖 — 与 Minot/Murphy 三人共享、1930 Popular Science 金奖（与 Minot）、Gerhard 金奖 1934
13  争议与自省 — 招生歧视黑人学生、1939 纽约州裁定违规后改正——正文明载，客观呈现
14  遗产：97 岁的一生 — 静脉营养之基（氨基酸混合物）、Schoenheimer 动态平衡、骨灰撒 Mount Hope
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1878-08-28 生于 Ashland, New Hampshire；1976-02-01 卒于 Rochester，享年 97 |
| 获奖理由 | "for their discoveries concerning liver therapy in cases of anaemia"——**their**（与 Minot/Murphy 三人共享） |
| 三人分工 | Holmgren 颁奖词明载：**Whipple 最先开始该研究**，其结果给了 Minot/Murphy 做恶性贫血实验的想法——链条勿颠倒 |
| 机制修正 | 肝疗法有效成分实为 **B12 而非铁**（正文有载）——表述须带此修正 |
| 两个 Whipple | George Whipple 病（肠源性脂肪营养不良，细菌病因判断正确）与诺奖肝疗法无关；Whipple procedure 系 Allen Whipple（同名不同宗挚友）——勿混 |
| Robscheit-Robbins | 研究助手 Frieda Robscheit-Robbins 合著 21 篇（1925-1930），被称「医学伟大创造性伙伴关系」——勿写成学生 |
| 建校叙事 | 1921 Rhees 亲赴旧金山力邀，1925 URMC 首批学生入学——创院院长身份是其第二标签 |
| 招生歧视 | 任院长期间以格式信拒收非裔学生，1939 被纽约州委员会裁定违反反歧视法后改正——正文明载，客观呈现勿回避 |
| 引语 | 自传《A Dozen Doctors》「I would be remembered as a teacher」及童年户外自述为正文原话——引语仅用这些 |
| 家庭 | 1914 娶 Katherine Ball Waring，育二子；1976 卒后骨灰撒 Rochester Mount Hope 墓园 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| liver therapy | 肝疗法 | 诺奖理由核心词 |
| pernicious anemia | 恶性贫血 | 当时不治之症，肝浓缩物可治 |
| Whipple's disease | Whipple 病 | 肠源性脂肪营养不良，与诺奖工作无关 |
| fibrinogen | 纤维蛋白原 | 肝为其合成场所（氯仿损伤实验） |
| bile pigment | 胆色素 | 胆红素代谢路线 |
| blood regeneration | 血液再生 | 1925 系列研究标题 |
| plasma protein | 血浆蛋白 | 动态平衡理论 |
| parenteral nutrition | 肠外营养 | 氨基酸混合物研究的应用遗产 |
| blackwater fever | 黑水热 | 巴拿马时期的溶血研究 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（manifest 预分配）
- **风格**：明亮 / 温暖 / 乐观
- **匹配理由**：Whipple 的底色是户外人与教师的明亮——从新罕布什尔湖区的少年到把恶性贫血从绝症里带出来的 daylight；Daylight 的温暖乐观匹配「再生」母题与其 97 岁的圆满一生（第二次使用该曲，首用 Metchnikoff，同为乐观派）。
- **本地路径**：`music_audio/` 下 Daylight 曲目 → 复制为 `presentations/20th_century/George_Whipple/Daylight.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
