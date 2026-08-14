# Hookslide 布局调整反思

> 问题：把 hookslide 的 4 个边框（badge）上移、紧贴 subtitle，前后改了 10+ 次才调好。
> 反思：为什么费这么大劲？根本原因是什么？下次如何一次到位？

---

## 一、问题描述

原始需求：hookslide 里 4 个 badge 与上方 subtitle（"数的几何 · Minkowski 时空 · 相对论几何化 · Hilbert 挚友"）之间的空白太大，要把 badge 上移、紧贴 subtitle（后来还要求去掉蓝色横线）。

## 二、走过的弯路（哪些改动是无效的）

| 轮次 | 改动 | 结果 | 错误认知 |
|---|---|---|---|
| 1-6 | 反复改 badge 的 y 值：1.7 → 2.41 → 3.46 → 1.0 → 1.3 → 5.5 | 用户反馈"没有变化""gap 还是很大" | 以为改 y 就能移动 badge 在页面上的位置 |
| 7 | 认为方向搞反，反向改 y | 仍无效 | 归因于"y 坐标方向反了" |
| 8 | 给 sectiontitle 加可选参数去掉蓝线 | 蓝线没了，但 gap 依旧 | 以为 gap 来自蓝线 |
| 9-10 | 继续改 y：5.5 → 2.5 → 3.21 | 仍"没有变化" | 还是在数值上打转 |

**关键信号被忽略**：无论 y 改成什么值，badge 在页面上的位置几乎不变，只有 summary（大边框）在上下跳动、甚至溢出页面。

## 三、根本原因（一次就要看出来的）

**`\begin{center}` 让大尺寸 tikzpicture 在可用空间内「垂直居中」**。

原始 hookslide 结构：

```latex
\sectiontitle{...}{...}
\begin{center}                     % ← 罪魁祸首
  \begin{tikzpicture}[...]
    \node[nodebox] at (-5.5, 5.5) {...};   % badge
    ...
    \node[graypanel] at (0, -1.0) {...};   % summary
  \end{tikzpicture}
\end{center}
```

两点叠加导致"改了没变化"：

1. **TikZ 自动 bounding box**：picture 的高度 = max(content y) - min(content y)。当 badge 是 y 最大的内容时，`badge_top == picture_top`。所以改 badge 的 y 值，**不会改变 badge 顶边在 picture 里的位置（它永远是 picture 顶端），只会改变 picture 的底部**（因为 summary 在低 y，picture 底由 summary 决定）。

2. **center 垂直居中**：`\begin{center}` 除了水平居中，还会在 picture 上下加弹性空白。picture 越高（badge y 越大 → picture 越"高"），badge 越被推到页面中央而非顶端。

**结论**：badge 的页面位置由「sectiontitle 结束位置 + center 的垂直居中」决定，**与 badge 的 y 值几乎无关**。所以改 y 是南辕北辙。

## 四、正确解法（两行改动）

```latex
\sectiontitle[skip]{...}{...}
% 去掉 \begin{center} 和 \end{center}
\begin{tikzpicture}[...]   % picture 从顶端自然流下，不再垂直居中
  \node[nodebox] at (-5.5, 5.5) {...};
  ...
\end{tikzpicture}
```

去掉 `\begin{center}` 后，picture 从 sectiontitle 下方自然流下，badge 紧贴 subtitle（仅剩 sectiontitle 的 0.06cm vspace）。y 值只需保证 badge_top 是 picture 顶端即可。

## 五、经验教训（下次一次到位）

1. **先看结构，再看数值**：改布局前先读完整结构——有没有 `\begin{center}`（垂直居中）、`overlay/remember picture`（绝对定位）、`\vspace`、`\plainbar` 等。数值问题占比远低于结构问题。

2. **"改了没变化" = 结构问题信号**：如果改了 y 值但视觉位置不变，立刻怀疑是 TikZ 自动 bounding box + 环境居中/定位在作祟，不要再继续调数值。

3. **TikZ 坐标 ≠ 页面坐标**：
   - `at (x,y)` 是 picture **内部**的相对坐标，origin 在 picture bounding box 左下（默认 y-up）。
   - badge 是 y 最大内容时，badge_top 恒等于 picture 顶端，改 y 不改变它在页面的位置。
   - picture 在页面上的位置由 LaTeX 排版流（sectiontitle 之后 + center/vspace 等）决定。

4. **建立基准再改**：第一次改动前，先 `pdftoppm` 渲染原始 PDF，用像素坐标测量 subtitle 和 badge 的位置，确定 gap 的像素值。每次改动后重渲染对比，而不是凭感觉。

5. **一次改一个变量**：不要同时改 y 值、蓝线、summary、center 包装。每次只动一个，便于定位。

6. **分清「页面定位」和「picture 内布局」**：
   - 想把整个 picture 上移/下移 → 改 LaTeX 环境（去掉 center、加 \vspace、改 sectiontitle）
   - 只想调整 picture 内部元素相对位置 → 改 `at (x,y)`

## 六、本次最终改动清单

1. `sectiontitle` 加可选参数 `[line]`（默认画蓝线，传 `[skip]` 不画）—— 仅 hookslide 传 `[skip]`
2. hookslide 去掉 `\begin{center}` / `\end{center}` —— **核心修复**
3. badge y = 5.5，summary y = 1.0 —— 保证 badge_top 是 picture 顶端、summary 完整可见

## 七、可复用的排查套路

```
改布局没反应？
├─ 1. 读结构：有 \begin{center}？有 overlay/remember picture？有 \vspace？
├─ 2. 确认 y 是 picture 内坐标还是页面坐标
├─ 3. 渲染原始 PDF，测像素，建立基准
├─ 4. 每次只改一个变量，改完立刻渲染对比
└─ 5. "改了没变化" → 90% 是结构问题（居中/定位），不是数值
```
