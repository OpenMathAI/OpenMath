# 图灵奖立传提示词批量撰写 · 共享工作流（1975–2025 批次）

> 本文件是并行 agent 的共享规范。逐人任务分配见 `prompt_manifest.json`（主控下达）。

## 1. 模板结构（强制）

每人的提示词写入 `presentations/{DirName}/{DirName}_zh.md`，其中 `{DirName}` 为 manifest 中 `pages_dir` 末段的下划线形式（如 `pages/1980/Tony Hoare` → `presentations/Tony_Hoare/Tony_Hoare_zh.md`；例外：`Jim Gray (computer scientist)` 用 `Jim_Gray`、`Charles H. Bennett (physicist)` 用 `Charles_H._Bennett`、`David Patterson (computer scientist)` 用 `David_Patterson`）。

结构 **严格对齐** `/Users/ericksun/workspace/codebuddy/OpenMathAI/turing/presentations/Marvin_Minsky/Marvin_Minsky_zh.md`（可另读 `John_McCarthy_zh.md` 作第二参照），共 11 节：

```
# {中文名}（{英文名}）立传提示词
> qid={manifest qid} · {生卒} · {国籍身份} · 20/21 世纪 · {年份} 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/{year}/{Title}/`（index.html + metadata.json + images）
## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）  ← 五条硬性要求照抄模板，仅替换公式框内容建议与国籍
## 1. 背景信息（用于 Slide 1-3）   ← 全名/生卒/国籍/身份/家庭/教育轨迹/师承/研究领域
## 2. 核心叙事亮点（用于 Slide 4-13） ← 8-12 条，每条含事实+写作口径
## 3. 配色方案（图灵紫品牌色 + 四分类色） ← 主色/强调色固定 #5B2D8E/#B03A2E，四分类色按人物领域语义命名（蓝#2E5A9E/青绿#1E8E8E/琥珀#D9A441/玫瑰#C0395B 可微调语义但建议沿用色值），背景母题一句
### 3.5 背景音乐选择 ✅【人物专属】 ← manifest 预分配的曲目+气质定位+落地文件名（曲目英文名去空格连写.wav）
## 4. Slide 规划（约 15 页，高斯版式结构） ← 封面/身份页/时间线 + 12 内容页逐一列出
## 5. 史实陷阱与敏感点（终审必须检查） ← ★核心节：从 Wikipedia 正文提炼 8-12 条禁写/勿混/年份红线
## 6. 数据库字段核对表 ← qid/name_zh/name_en/birth_date/death_date/nationality/primary_occupation/field_of_work/has_biography
## 7. 社会关系入库清单 ← 导师/合作者/门生，页面无载的明写"无载禁写"
## 8. 奖项清单 ← 图灵奖+其他荣誉，带年份
## 9. 机构清单 ← 教育履历+任职履历（带年份区间）
## 10. 终审清单 ← 8-12 条 checkbox，覆盖 §5 全部红线 + 版式/编译要求
## 11. Review 流程规范（两轮 Review） ← Review-1 事实终审（含头像文件核对）+ Review-2 结构优化，照抄模板改人名
```

## 2. 事实抽取流程（每人）

1. 用 python + bs4 把 `turing/pages/{year}/{Title}/index.html` 转纯文本再阅读（index.html 可能很大，勿直接 read_file）：

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/turing && python3 -c "
from bs4 import BeautifulSoup
from pathlib import Path
p = 'pages/{year}/{Title}'
html = (Path(p)/'index.html').read_text()
soup = BeautifulSoup(html, 'html.parser')
for sel in ['style','script','sup.reference','.reflist']:
    for n in soup.select(sel): n.decompose()
lines = [l.strip() for l in soup.get_text('\n').split('\n') if l.strip()]
out = Path('/tmp')/(p.split('/')[-1].replace(' ','_')+'.txt')
out.write_text('\n'.join(lines)); print(out, len(lines))
"
```

2. read_file 通读文本，建立事实基准；生卒/教育/奖项以 infobox + 正文为准。
3. **与 manifest 冲突时以本地 Wikipedia 为准**；Wikipedia 也含糊的，提示词中写明"以正文为准/页面未载禁写"。
4. 肖像：`ls pages/{year}/{Title}/images/` 找 infobox 头像（通常与人物同名的 jpg/png；带 250px/330px/500px 前缀的取最大可用版），在 §11 Review-1 中写明文件名；目录为空或无人像时写"无肖像，装饰圆占位"。在版式允许处可注明可用的示意图（如 CodasylB.png 之类的模型图）。

## 3. 事实红线通用规则

- 图灵奖**获奖理由**（ACM citation）尽量整句引用，这是每篇的核心红线。
- "首位/第一/唯一"类表述：页面无载禁写。
- 与同奖得主共享年份的（如 1975 Newell/Simon、2002 RSA 三人、2018 深度学习三杰），须写明共享结构，且每人篇目侧重各自贡献，避免完全重复；禁写页面上没有的内部矛盾/恩怨细节。
- 家庭/政治敏感细节仅按 Wikipedia 实载一笔带过，不渲染。
- 死因仅写页面实载（如 cancer/Parkinson's/heart attack）；未载写"未详述，勿编造"。
- 在世者死亡日期写"在世留白"。
- 引语：仅收录 Wikipedia 原文可见的引语并标注出处；无直接引语则在 §5 写"全文无直接引语，勿编造"。

## 4. BGM 预分配

manifest 已为每人预分配曲目（`bgm` 字段），**直接沿用勿自行更改**；§3.5 的"气质定位"由你按人物气质撰写一句。已在图灵项目使用的 New Lands/Timeless/Falling Apart/The Flow of Time/Expedition/Pathfinder 也可能再次出现于本批次，属正常复用。

## 5. 交付与汇报

- 每写完一人立即落盘，再写下一人；全部完成后向 main 一次性汇报：完成清单（人名/输出路径/页数无——提示词无页数）、发现的事实疑点（Wikipedia 与 manifest 冲突处）、无肖像者名单。
- 只写 `presentations/{DirName}/{DirName}_zh.md`，**不建 tex/pdf/mp4、不改 Makefile、不动其他目录**。
- 提示词结尾照抄模板两行：
  > **开始执行。每完成一步向我汇报。**
  > **最重要的事：每写一页就 make，看到溢出就修。**
