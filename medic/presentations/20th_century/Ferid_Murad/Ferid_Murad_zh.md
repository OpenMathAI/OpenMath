# 医学家立传提示词（Ferid Murad）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Ferid Murad（1998 年诺贝尔生理学或医学奖得主，美国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Ferid_Murad/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Ferid Murad（费里德·穆拉德，1936-09-14 印第安纳州怀廷 ~ 2023-09-04 加州门洛帕克，享年 86 岁）
- **气质关键词**：**揭开硝酸甘油百年谜题的人、cGMP 信号的奠基者、Sutherland 门下首届 MD-PhD** —— 1998 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Furchgott、Ignarro 三人共享）：
  > "for their discoveries concerning nitric oxide as a signalling molecule in the cardiovascular system"
  > （因其关于一氧化氮作为心血管系统信号分子的发现）
- **设计母题**：**「释放的气体」**。硝酸甘油在体内悄悄释放 NO、升高 cGMP、舒张平滑肌——视觉隐喻：药片晶体中逸出的气体分子撬开血管锁扣。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Ferid_Murad/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Ferid_Murad/`，成目录 `medic/presentations/20th_century/Ferid_Murad/`，Makefile 复制后设 `MAIN=Ferid_Murad_zh`、`VIDEO_NAME=Ferid_Murad_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库：本人记录复用库内既有 stub（id=6150）UPD 回填 QID Q295999，`has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pharmacology | 药理学 | 临床药理学系主任等任职，1998 诺奖核心 | 总览页 |
| 1 | cyclic GMP | 环鸟苷酸 | 硝酸甘油经释放 NO 升高 cGMP 舒张平滑肌 | cGMP 页 |
| 2 | nitric oxide signalling | 一氧化氮信号 | 信号链缺环的补全者 | NO 页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Ferid_Murad.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Robert F. Furchgott | — | 1998 诺贝尔生理学或医学奖三人共享（一氧化氮信号） |
| co-honored | Louis Ignarro | — | 1998 诺贝尔生理学或医学奖三人共享（一氧化氮信号） |
| advisor-student | Earl Wilbur Sutherland Jr. | 师 | Case Western 首届 MD-PhD 项目师从（他批已建同边） |
| advisor-student | Theodore W. Rall | 师 | 博士导师之一（infobox 与 Sutherland 并列） |
| spouse | Carol A. Leopold | — | 妻，育五子 |
| parent-child | John Murad | 父 | 阿尔巴尼亚移民，原名 Xhabir Murat Ejupi |
| parent-child | Henrietta Josephine Bowman | 母 | — |

> 说明：与 Sutherland 的师生边已由 med-batch-21（Sutherland 篇）先建（库内 11905），本 yaml 同边幂等跳过。Rall 用库内既有记录 Theodore W. Rall（batch-21 建为 Sutherland 同事，6149）。父亲原名 Xhabir Murat Ejupi、移民入境时改名 John Murad——stub 用改名后的 John Murad（与本人 Ferid Murad 不冲突）；家庭宗教细节（穆斯林父亲/浸信会母亲/天主教抚养/大学改宗圣公会）为 page.md 明载家世，一句带过。五个子女未具名不入库；Forst Fuller（建议读 MD-PhD 的导师）为过场不入库。

## 五、配色方案 【人物专属】

- **气质**：移民家庭的踏实、临床与基础双修的全面、多机构辗转的韧性
- **主色**：cGMP 深蓝 `#2C4E7E`（第二信使的分子蓝）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 药理学 — 听诊蓝 `#33637D`
  - `badgeB` 环鸟苷酸 — cGMP 青 `#1F7A6D`
  - `badgeC` 一氧化氮信号 — NO 紫 `#7B4FA0`
  - `badgeD` 临床研究 — 白大褂银灰 `#8A98A8`
- **背景母题**：药片晶体中逸出的气体分子链与平滑肌舒张弧线，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 揭开硝酸甘油谜题的人 / Ferid Murad 1936–2023 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像（2008 照）+ 右信息网格（生卒、教育、七站任职、家庭、荣誉、核心领域）
03  核心贡献概览 — 硝酸甘油释放 NO / cGMP 信号 / 临床药理学建制
04  移民家庭 (1936–1954) — 阿尔巴尼亚父亲的爱丽丝岛改名、家庭餐馆里长大、八年级作文的三个职业志愿
05  迪保尔与转机 (1954–1958) — Rector 奖学金、化学学士、Fuller 与 Sutherland 家的双重建议
06  Case Western 首届 MD-PhD (1958–1965)（核心页）— Sutherland/Rall 门下、1965 双学位、此项目后来演变为 MSTP
07  马萨诸塞总医院与 NHLI (1965–1970) — 内科实习住院、公共卫生服务研究员
08  弗吉尼亚大学 (1970–1981) — 副教授到正教授、临床研究中心与临床药理学分部主任
09  硝酸甘油之谜解开（核心页）— 硝酸甘油经释放 NO 升高 cGMP 舒张平滑肌
10  1998 诺贝尔奖（核心页）— citation 原文、三人共享、Lasker 1996（与 Furchgott 两人）
11  Stanford-Abbott-创业 (1981–1997) — 帕洛阿尔托 VA 主任、Abbott 药物发现副总裁、创办 Molecular Geriatrics
12  得州与华府 (1997–2017) — McGovern 医学院整合生物药学系创系主任、GWU 教授、Palo Alto VA (2017-2023)
13  荣誉与公共事务 — NAS 院士 · Ciba 奖 1988 · 2015 年林道会议签署气候变化主瑙宣言（76 位诺奖得主）
14  遗产 — cGMP 信号通路与 NO 药理学；Herbal medicine 书系主编；2023-09-04 辞世
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文（their 三人共享）；Murad 分段是「硝酸甘油经释放 NO 起效、cGMP 为第二信使」——链条的上游 |
| 2 | 双博士导师 | infobox 并列 Earl Sutherland Jr. 与 Theodore Rall——两条师生边分别建；Sutherland 边他批已建幂等跳过（note 为对方批次版本）；Rall 用库内形式 Theodore W. Rall |
| 3 | Sutherland 关系细节 | Sutherland 是 1971 诺奖得主（cAMP）；其子 Bill Sutherland 的同学建议是 Murad 选 MD-PhD 的机缘之一——叙事可写，勿把「同学建议」写成 Sutherland 招生 |
| 4 | 家庭宗教线 | 父穆斯林/母浸信会/兄妹天主教抚养/本人大学改宗圣公会——page.md 明载家世，一句带过即可，不展开宗教议题 |
| 5 | 父亲改名 | 原名 Xhabir Murat Ejupi、1913 年爱丽丝岛入境时改为 John Murad——身份页可作细节；stub 用 John Murad 防阿尔巴尼亚原名拼写漂移 |
| 6 | 主瑙宣言 | 2015 年签署气候变化主瑙宣言（76 位诺奖得主、递交 Hollande、COP21）——page 明载可写，一句带过、不展开气候政治 |
| 7 | 引语红线 | 八年级作文三志愿（医生/教师/药剂师）为叙述性事实；本篇无直接引语，禁编造 |
| 8 | 任职七站 | UVA 1970-81 → Stanford 1981-88 → Northwestern 1988-98 → Abbott 1988-93（重叠）→ UTHealth 1997-2011 → GWU 2011-17 → Palo Alto VA 2017-23——infobox 与正文有重叠期，按正文叙事归置 |
| 9 | Lasker 份额 | 1996 Lasker 为 Murad 与 Furchgott 两人（Ignarro 未在其列）——勿写三人同获 |
| 10 | metadata 冲突 | frontmatter doctoral_advisor 仅 Sutherland，infobox 双导师——按 infobox 双载建两条边；生卒 1936-09-14/2023-09-04 一致 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| nitroglycerin | 硝酸甘油 | 释放 NO 的机理是 Murad 的核心发现 |
| cyclic GMP | 环鸟苷酸（cGMP） | 第二信使 |
| smooth muscle | 平滑肌 | 血管舒张的效应细胞 |
| MD-PhD program | 医学博士-哲学博士双学位项目 | Case Western 1957 首创 |
| MSTP | 医学科学家培训计划 | 该项目后续演变 |
| Mainau Declaration | 主瑙宣言 | 2015 气候变化版 |
| Lindau Meeting | 林道诺贝尔奖得主大会 | 65 届（2015） |
| Abbott Laboratories | 雅培实验室 | 药物发现副总裁 |
| Molecular Geriatrics | 分子老年病学公司 | 1993 自创 |
| integrative biology | 整合生物学 | 其创系方向 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Ascension** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「攀升」匹配其人生的双螺旋上升——移民餐馆少年到七站学术阶梯，再到斯德哥尔摩
  - 也匹配 cGMP 信号从药片到血管的分子级联攀升意象
- **备选**（未采用）：Shine Like The Sun（本批 Ignarro 已用，三人组区分）、Awaken（batch-11 Hess 已用）
- **本地路径**：按 music_audio/ 内 Alex-Productions Ascension 曲目复制至 `medic/presentations/20th_century/Ferid_Murad/Ascension.wav`，ffmpeg `-shortest` 对齐
