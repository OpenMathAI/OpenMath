# Turing Award Video Series — Missing Portrait Checklist

> Source: `turing/pages/<year>/<Name>/images/` (downloaded 2026-08-08)
> 资料基准日：2026-08-09。共 81 位得主中 **2 位** 缺真人肖像，待人工补图。

## 缺照片得主

| 年份 | 得主 | 占位文件 | 所在集 | 备注 |
|---|---|---|---|---|
| 2020 | Alfred Aho | `alfredaho.jpg` | ep02、allinone | Wikipedia 页面无合适真人照片 |
| 2020 | Jeffrey Ullman | `jeffreyullman.jpg` | ep02、allinone | Wikipedia 页面无合适真人照片 |

## 如何补图

1. 在以下来源下载真人肖像（建议按优先级）：
   - Wikipedia Commons（如有图像类条目）
   - 哥伦比亚大学（Aho）/斯坦福大学（Ullman）官方主页
   - DBLP / ACM Fellow 照片页
   - 学术会议照（如 ACM 现场照）
2. 保存为 `.jpg`（首选）/`.jpeg`/`.png`/`.webp`，覆盖以下两个空文件：
   - `turing/video/episode-02-programming-languages/images/alfredaho.jpg`
   - `turing/video/episode-02-programming-languages/images/jeffreyullman.jpg`
   - `turing/video/episode-allinone/images/alfredaho.jpg`
   - `turing/video/episode-allinone/images/jeffreyullman.jpg`
3. 重新运行 `python3 gen_turing.py`（脚本会自动检测非空文件并使用），或在每集目录执行 `make` / `make video`。

## 当前状态

- 总得主：**81 位**（1966–2025）
- 真人肖像在位：**79 位**
- 缺肖像（占位）：**2 位**（Aho、Ullman，均为 2020 年合著《龙书》者）
- 脚本逻辑：`gen_turing.py` 的 `find_portrait()` 自动从 `turing/pages/<year>/<Name>/images/` 选择最大的非图标图片（过滤 `question_book`/`flag_`/`map_`/`icon`/`logo`/`seal`/`commons` 等）。
