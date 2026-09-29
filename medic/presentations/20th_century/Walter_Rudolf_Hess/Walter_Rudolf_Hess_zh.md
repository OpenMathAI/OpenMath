# 医学家立传提示词（Walter Rudolf Hess）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Walter Rudolf Hess（1949 年诺贝尔生理学或医学奖得主，瑞士）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Walter_Rudolf_Hess/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Walter Rudolf Hess（瓦尔特·鲁道夫·赫斯，1881-03-17 弗劳恩费尔德 ~ 1973-08-12 洛迦诺，享年 92 岁）
- **气质关键词**：**用电流绘制间脑地图的人、从眼科诊所转身走进脑室的「中途改道者」、间脑功能组织学的奠基人** —— 1949 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 António Egas Moniz 各得一半）：
  > "for his discovery of the functional organization of the interbrain as a coordinator of the activities of the internal organs"
  > （因其发现间脑作为内脏活动协调者的功能组织）
- **设计母题**：**「间脑地图」**。以细电极在猫脑特定点位施加断续直流，诱发从嗜睡到暴怒的全谱行为——视觉隐喻：猫脑矢状剖面上的坐标网格与发光刺激点。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Walter_Rudolf_Hess/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Walter_Rudolf_Hess/`，成目录 `medic/presentations/20th_century/Walter_Rudolf_Hess/`，Makefile 复制后设 `MAIN=Walter_Rudolf_Hess_zh`、`VIDEO_NAME=Walter_Rudolf_Hess_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 苏黎世生理研究所教授兼所长（1917–1951），1949 诺奖核心 | 总览页 |
| 1 | neuroscience | 神经科学 | 间脑（下丘脑）电刺激测绘、断续直流刺激法 | 间脑页 |
| 2 | ophthalmology | 眼科学 | 前半程职业：Hess 屏发明者、拉珀斯维尔私人诊所 | 眼科页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Walter_Rudolf_Hess.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | António Egas Moniz | — | 1949 同年各得一半，Moniz 得脑白质切断术一半 |
| advisor-student | Justus Gaule | 师 | 1912 年弃诊转入其苏黎世生理研究所，1913 年完成教授资格 |
| influence | Conrad Brunner | — | 明斯特林根外科训练导师 |
| influence | Otto Haab | — | 1907 年苏黎世师从改攻眼科 |
| influence | Max Verworn | — | 一战期间波恩生理研究所访学一年 |
| spouse | Louise Sandmeier | — | 妻，1987 年卒 |
| parent-child | Clemens Hess | 父 | 携其在家做物理实验引向科学 |
| parent-child | Gertrud Fischer | 母 | — |
| parent-child | Gertrud Hess | 女 | 1910 年生 |
| parent-child | Rudolf Max Hess | 子 | 1913 年生，神经学家，后证实其睡眠诱导发现 |

> 说明：母亲与长女同名 Gertrud——母以娘家姓 Gertrud Fischer 入库、女以 Gertrud Hess 入库，防同名自环。Moniz 用 manifest 规范名 António Egas Moniz（med-batch-12，本批只建自己侧边）。Brunner/Haab 为训练/转科师承建 influence，Gaule 是转入研究后的教授资格导师建师生边；Verworn 为一年访学建 influence。1949 年另一半理由（Moniz 的 leucotomy）在陷阱表对照，正文不展开额叶切断术伦理。

## 五、配色方案 【人物专属】

- **气质**：精密制图学的冷静、瑞士 physiologie 的内敛、中途改道者的决断
- **主色**：间脑深蓝紫 `#4A3562`（脑图坐标网格的底色）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生理学 — 血流青 `#2E7A8C`
  - `badgeB` 神经科学 — 刺激橙 `#C0622E`
  - `badgeC` 眼科学 — Hess 屏黑白格 `#8A8F98`
  - `badgeD` 内脏协调 — 迷走绿 `#3A7A5C`
- **背景母题**：猫脑矢状剖面网格与稀疏发光刺激点、Hess 屏棋盘格线稿，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 绘制间脑地图的人 / Walter Rudolf Hess 1881–1973 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、四校求学、执业-研究两段式、荣誉、核心领域）
03  核心贡献概览 — 间脑功能组织 / 断续直流刺激法 / Hess 屏 / 血液黏度计
04  弗劳恩费尔德 (1881–1899) — 父亲的家用物理实验室、三兄妹中的次子
05  辗转四校的医学训练 (1899–1906) — 洛桑-柏林-基尔-苏黎世、1906 医学博士（血液黏度与心脏做功、自制黏度计）
06  外科与眼科岁月 (1906–1912) — Brunner 门下外科训练、Haab 门下改攻眼科、拉珀斯维尔开业、发明 Hess 屏、结婚生子
07  1912：弃诊从研 — 放弃高收入诊所、转入 Gaule 的苏黎世生理研究所、1913 完成教授资格
08  主掌研究所 (1917–1951) — Gaule 退休后 interim 接任、正式教授兼所长 34 年；血流与呼吸调节研究
09  1930s：间脑地图（核心页）— 猫脑定点电刺激、断续直流参数（12.5/25 ms、0.5–1.5 V、8 Hz）、0.25 mm 细电极
10  1949 诺贝尔奖（核心页）— citation 原文、与 Moniz 各半、1949-12-12 诺奖演讲 The Central Control of the Activity of Internal Organs
11  前部与后部：行为的两极 — 刺激前部→血压降/呼吸缓/饥饿渴尿便；刺激后部→兴奋与防御姿态；诱导睡眠的争议与后来被证实（含其子 Rudolf Max 的工作）
12  多面手 — Jungfraujoch 高山研究站奠基与首任所长 (1930–1937)、反对反活体解剖立法的公开行动
13  荣誉与认可 — Marcel Benoist Prize（1931/1932 两说）· 伯尔尼日内瓦麦吉尔弗赖堡荣誉博士 · Carl-Ludwig 奖章
14  遗产 — 下丘脑功能图谱成为神经内分泌与自主神经调控的基石；1951 退休后仍在大学办公、1967 移居 Ascona
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for his discovery of the functional organization of the interbrain as a coordinator of the activities of the internal organs"（his 独享一半）；interbrain=间脑（diencephalon 同义），两词并存 |
| 2 | 「一半」结构 | 1949 两半：Hess（间脑功能组织）+ Moniz（ certain psychoses 的 leucotomy/lobotomy 治疗价值）——正文对 Moniz 一半只需一句对照，额叶切断术的历史伦理评价 page.md 未载、不展开 |
| 3 | 死亡日期双值 | frontmatter 有 1973-08-12 与 1973-09-12 噪声，正文/infobox 均为 1973-08-12（heart failure）——取 08-12 |
| 4 | Marcel Benoist 年份 | infobox 作 1931、Honours 列表作 1932——两说并存，页面采用 infobox 1931 并在荣誉帧标注年份两说 |
| 5 | 同名母女 | 母亲 Gertrud Hess（née Fischer）与长女 Gertrud Hess 同名——行文务必区分（母以娘家姓 Fischer 出现），yaml 已分立两记录 |
| 6 | 两段式人生 | 眼科执业（1907-1912，收入优渥）→ 1912 弃诊从研——「中途改道」是本篇最大叙事钩子，Hess 屏是眼科段成果，勿与诺奖工作混淆 |
| 7 | 师承分层 | Gaule（研究导师，师生边）≠ Brunner（外科训练）≠ Haab（眼科训练）≠ Verworn（一年访学）——四层已分别裁定（1 师生 + 3 influence），勿合并 |
| 8 | 争议发现 | 诱导睡眠「highly controversial at the time but later confirmed」——被谁证实？其子 Rudolf Max Hess 等（page 明载）；如实写，勿扩大证实者名单 |
| 9 | 反活体解剖行动 | Hess 政治性反对反活体解剖立法——一句史实记载即可，不展开动物实验伦理论战 |
| 10 | metadata 冲突 | frontmatter occupation 含 art historian 噪声；fields 含 surgery——yaml 取 physiologist 主职业，外科/眼科作为前半程职业叙述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| interbrain / diencephalon | 间脑 | 同义两写，勿当两个结构 |
| hypothalamus | 下丘脑 | 间脑的刺激靶区 |
| interrupted direct-current stimulation | 断续直流刺激法 | Hess 自创技术名 |
| Hess screen | 赫斯屏 | 眼科斜视检查屏，前半程成果 |
| viscosimeter | 血液黏度计 | 1906 论文装置 |
| micturition | 排尿 | 前部刺激反应术语 |
| Privatdozent / habilitation | 无俸讲师 / 教授资格 | 1913 完成教资 |
| brain mapping | 脑功能定位绘图 | 方法论关键词 |
| Jungfraujoch | 少女峰高山研究站 | 1930 奠基 |
| Marcel Benoist Prize | 马塞尔·伯努瓦奖 | 瑞士科学奖，1931/1932 两说 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「觉醒」双关贴切：其电刺激图谱 literally 揭示了唤醒-嗜睡两极的脑区控制（前部诱导睡眠/后部激发兴奋），Awaken 正是这套行为谱系的题眼
  - 渐强结构也匹配「从乡村诊所到诺贝尔讲坛」的二次出发
- **备选**（未采用）：The Invisible Light（不可见之光意象贴电极刺激但偏物理叙事）、Timeless（已被本批 Carl 占用）
- **本地路径**：按 music_audio/ 内 Alex-Productions Awaken 曲目复制至 `medic/presentations/20th_century/Walter_Rudolf_Hess/Awaken.wav`，ffmpeg `-shortest` 对齐
