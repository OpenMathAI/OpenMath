# 陈省身奖章视频材料 — Chern Medal Video

> 以 `Fields_Medal/video_timeline` 与 `Abel_Prize/video` 的 Beamer 版式为模板。
> 一部介绍片（什么是陈省身奖章）+ 一部得主枚举片（2010–2026 全部 5 位得主）。
> 人物照片取自 `Chern_Medal/pages/` 离线维基百科页面（Nirenberg 照片取自 Abel_Prize 页面）。

---

## 剧集目录

| 集数 | 标题 | 内容 | 页数 |
|---|---|---|---:|
| 00 | 什么是陈省身奖章 | 介绍片：陈省身其人、奖项由来、三大奖对比 | 6 |
| 01 | 全部得主 | 枚举片：2010–2026 全部 5 位得主 | 7 |

---

## 关于陈省身奖章

- **命名**：纪念华裔数学家**陈省身（Shiing-Shen Chern, 1911–2004）**，「微分几何之父」。
- **颁发**：国际数学联盟（IMU）与陈省身奖章基金会共同设立，**2010 年**首颁。
- **节奏**：每四年一届，配合国际数学家大会（ICM）；表彰**终身成就**，不设年龄限制。
- **奖金**：50 万美元，其中一半须捐赠给获奖者指定的数学机构。

## 全部得主（第 01 集）

| 年份 | 得主 | 领域 |
|---|---|---|
| 2010 | Louis Nirenberg | 非线性椭圆型 PDE（亦为 2015 阿贝尔奖得主）|
| 2014 | Phillip Griffiths | 复几何、Hodge 理论 |
| 2018 | Masaki Kashiwara | 代数分析、表示论（亦为 2025 阿贝尔奖得主）|
| 2022 | Barry Mazur | 拓扑、算术几何、数论 |
| 2026 | Graeme Segal | 拓扑、数学物理、范畴论 |

> 注意：本材料所述为 **IMU 陈省身奖章**，与国际华人数学家大会（ICCM）颁发的 **ICCM 陈省身奖**不同。

---

## 版式说明

- XeLaTeX + Beamer（16:9，中文 PingFang SC）。
- 人物页统一使用 `\personslide` 宏：左侧照片、中间信息卡（获奖/生卒/国别/机构）、右侧核心贡献。
- 配色以深青／翡翠绿（`#0F6E5C`）+ 暖金为主，呼应几何主题与东方渊源，区别于菲尔兹奖（金）与阿贝尔奖（深蓝）系列。

---

## 编译

需要 `xelatex`（TeX Live）。生成视频还需 `pdftoppm`（poppler）与 `ffmpeg`。

```bash
make              # 编译全部 PDF
make EP=00        # 只编译介绍片
make EP=01        # 只编译得主片
make images       # 由 PDF 生成每页 PNG
make video        # 合成 MP4（目录内放入 .wav 则自动作为背景音乐）
make clean        # 清理中间文件
make distclean    # 清理全部生成物
```

---

## 资料来源

- 离线人物页面：`Chern_Medal/pages/<年份>/<姓名>/`
- 得主名录与获奖理由：`Chern_Medal/chern_medal_laureates.md`
- IMU 官方页面：<https://www.mathunion.org/imu-awards/chern-medal-award>
- 陈省身奖章（Wikipedia）：<https://en.wikipedia.org/wiki/Chern_Medal>
- 陈省身（Wikipedia）：<https://en.wikipedia.org/wiki/Shiing-Shen_Chern>
