# Nobel Peace Video Series — Missing Portrait Checklist

> Source: `peace/presentations/pages/{20th,21th}_century/<Dir>/images.txt`（自动下载）
> 共 143 条记录 / 140 位获奖者中 **4 位** 缺真人肖像，待人工补图。

## 缺照片获奖者

| 年份 | 获奖者 | 占位文件 | 页面目录 | 备注 |
|---|---|---|---|---|
| 1902 | Charles Albert Gobat | `episode-allinone/images/charlesalbertgobat.jpg` | `pages/20th_century/Charles_Albert_Gobat` | images.txt 无匹配人像（已过滤旗帜/签名/图标），或候选图下载失败 |
| 1904 | Institute of International Law | `episode-allinone/images/instituteofinternationallaw.jpg` | `pages/20th_century/Institut_de_Droit_International` | images.txt 无匹配人像（已过滤旗帜/签名/图标），或候选图下载失败 |
| 1947 | Friends Service Council | `episode-allinone/images/friendsservicecouncil.jpg` | `pages/20th_century/Quaker_Peace_and_Social_Witness` | images.txt 无匹配人像（已过滤旗帜/签名/图标），或候选图下载失败 |
| 2022 | Centre for Civil Liberties | `episode-allinone/images/centreforcivilliberties.jpg` | `pages/21th_century/Centre_for_Civil_Liberties_Ukrainian_civil_society_organization` | images.txt 无匹配人像（已过滤旗帜/签名/图标），或候选图下载失败 |

## 如何补图

1. 从 Wikipedia Commons / 官方主页 / Nobel 官网下载真人肖像（建议宽 ≥ 250px）。亦可把人工校准图放入 `peace/video/episode-allinone/figures/`（文件名为人物英文名，如 `Henry Dunant.jpg`，优先级最高）。
2. 保存为 `.jpg`（首选）/`.jpeg`/`.png`/`.webp`，命名与下表占位文件同名（扩展名可不同），放入 `peace/video/episode-allinone/images/`。
3. 重新运行 `python3 gen_peace.py`（自动检测非空文件并使用），再 `make pdf && make video`。

## 当前状态

- 总获奖者：**140 位**（含机构，1901–2025）
- 真人肖像在位：**139 条记录**
- 缺肖像（占位）：**4 条记录**
