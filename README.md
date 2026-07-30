# OpenMath

> 🏆 Open-source LaTeX Beamer slides & video materials for the world's most prestigious mathematics and computer science awards — and the laureates behind them.

## 项目简介

**OpenMath** 是一个开源项目，致力于用精美的 LaTeX Beamer 幻灯片系统性地介绍世界顶级数学与计算机科学大奖及其得主。
我们的目标是：
- 📖 为每一位获奖数学家制作详尽的 Beamer 演示文档
- 🎬 生成可直接用于视频制作的 PDF 幻灯片
- 🌐 构建一个开放、可协作的数学荣誉档案馆

## 涵盖奖项

| 奖项 | 说明 | 目录 |
|:--|:--|:--|
| 🇳🇴 **Abel Prize** | 阿贝尔奖 · 数学终身成就 (2003–) | `Abel_Prize/` |
| 🥇 **Fields Medal** | 菲尔兹奖 · 40岁以下数学家最高荣誉 (1936–) | `Fields_Medal/` |
| 🇮🇱 **Wolf Prize** | 沃尔夫数学奖 (1978–) | `Wolf_Prize/` |
| 🏅 **Chern Medal** | 陈省身奖 · 终身杰出数学成就 (2010–) | `Chern_Medal/` |
| 💻 **Turing Award** | 图灵奖 · 计算机科学最高荣誉 (1966–) | `turing/` |

## 项目结构

```
OpenMath/
├── Abel_Prize/              # 阿贝尔奖：得主资料、视频系列 Beamer
├── Fields_Medal/            # 菲尔兹奖：得主资料、视频系列 Beamer
├── Wolf_Prize/              # 沃尔夫奖：得主资料、视频系列 Beamer
├── Chern_Medal/             # 陈省身奖：得主资料、视频系列 Beamer
├── turing/                  # 图灵奖：得主资料
├── mathematician/           # 数学家百科（Top 500）：Wikipedia 抓取 → LaTeX
├── medal_list_allinone/     # 各奖项汇总对比 Beamer（含交叉得主分析）
├── mathematics_awards.md    # 世界数学奖项总览
└── music_audio/             # 视频配乐素材（不入库）
```

## 技术栈

- **LaTeX / XeLaTeX** — 文档排版
- **Beamer** — 幻灯片框架
- **Python** — 数据抓取与自动化脚本
- **Makefile** — 构建自动化
- **Pandoc** — HTML → LaTeX 转换

## 环境要求

```bash
# LaTeX 发行版（macOS）
brew install --cask mactex

# 或 Linux
sudo apt install texlive-full

# Python 依赖
pip install requests beautifulsoup4 lxml

# 其他工具
brew install pandoc
```

## 快速开始

```bash
# 克隆仓库
git clone https://github.com/OpenMathAI/OpenMath.git
cd OpenMath

# 编译某个 Beamer 幻灯片（以阿贝尔奖序章为例）
cd Abel_Prize/video/episode-00-what-is-abel-prize
latexmk -xelatex abel_prize_ep00_zh.tex

# 编译奖项汇总列表
cd medal_list_allinone/abel_beamer
latexmk -xelatex abel_prize_laureates_beamer.tex
```

## 路线图

- [x] Abel Prize 全系列 Beamer（序章 + 分期 + 汇总）
- [x] Fields Medal 视频系列 Beamer
- [x] Wolf Prize 视频系列 Beamer
- [x] Chern Medal 视频系列 Beamer
- [x] 各奖项交叉得主分析（双料 & 大满贯）
- [x] Top 500 数学家 Wikipedia 抓取 & LaTeX 生成
- [ ] **逐一为每位数学家制作独立 Beamer 介绍文档**
- [ ] 图灵奖得主 Beamer 系列
- [ ] 英文版本 Beamer 幻灯片

## 贡献

欢迎 PR！你可以：
- 🐛 修复 LaTeX 编译问题
- 🎨 改进幻灯片设计与排版
- 📝 补充/修正得主信息
- 🌍 添加多语言版本
- 🧑‍🔬 为新的数学家撰写 Beamer 介绍

## 许可证

本项目采用 [MIT License](LICENSE) 开源。

## 致谢

- 数据来源：[Wikipedia](https://en.wikipedia.org/)、各奖项官方网站
- 配乐来源：YouTube Audio Library（免费商用）

---

<p align="center">
  <em>「数学是人类精神最纯粹的创造」—— David Hilbert</em>
</p>
