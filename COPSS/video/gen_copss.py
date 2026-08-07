#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate COPSS video episode Beamer decks (ep01-05 + allinone).

Data source: ../copss_winners.md (46 laureates, 1981-2026).
Run from COPSS/video/:  python3 gen_copss.py
"""
import os
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------- data ----------------
# name_en | name_zh(subtitle) | year | life | country | inst | tag | contrib | img | credit/initials
PEOPLE = {
    "ep01": [
        ("Peter J. Bickel", "彼得·比克尔 \\enspace·\\enspace 首位 COPSS 得主", 1981, "1940–", "美国（生于罗马尼亚）", "UC Berkeley",
         "非参数与半参数统计", "经验过程理论、自适应估计、半参数效率界。他以严格的数学为统计推断奠定现代基础，其学生包括范剑青、吴建福等。",
         "images/bickel.jpg", "Wikipedia"),
        ("Stephen Fienberg", "斯蒂芬·费恩伯格", 1982, "1942–2016", "美国（生于加拿大）", "Carnegie Mellon University",
         "列联表与社会统计", "对数线性模型、列联表分析、统计与法律、数据隐私。他推动统计方法进入司法与公共政策领域。",
         "none", "S.F."),
        ("Tze Leung Lai", "黎子良 \\enspace·\\enspace 首位华人得主", 1983, "1945–2023", "美国（生于香港）", "Stanford University",
         "序贯分析与随机逼近", "序贯分析、随机逼近渐近理论、变化点问题。他在自适应试验设计与金融统计上影响深远。",
         "none", "T.L.L."),
        ("David V. Hinkley", "戴维·欣克利", 1984, "1944–2019", "美国（生于英国）", "UC Santa Barbara",
         "Bootstrap 与渐近理论", "Bootstrap 变换法、鞍点近似、渐近理论。他与 Efron 共同发展了 Bootstrap 的理论基础，导师为大卫·考克斯。",
         "none", "D.H."),
        ("James O. Berger", "詹姆斯·伯杰", 1985, "1950–", "美国", "Purdue University",
         "统计决策与贝叶斯", "统计决策论、客观贝叶斯分析、模型选择。他是贝叶斯学派现代复兴的核心人物。",
         "images/berger.jpg", "Wikipedia"),
        ("Ross L. Prentice", "罗斯·普伦蒂斯", 1986, "1946–", "加拿大", "Fred Hutchinson Cancer Research Center",
         "生存分析与流行病学", "生存分析、临床试验设计、营养流行病学。Cox 模型在应用中的标准框架由他系统建立。",
         "none", "R.P."),
        ("C. F. Jeff Wu", "吴建福", 1987, "1949–", "美国（生于台湾）", "Georgia Institute of Technology",
         "试验设计与工业统计", "试验设计、鲁棒参数设计、EM 算法收敛定理。他为工程统计学奠定现代方法论。",
         "images/wu.jpg", "Wikipedia"),
        ("Raymond J. Carroll", "雷蒙德·卡罗尔", 1988, "1949–", "美国（生于日本）", "Texas A&M University",
         "测量误差模型", "测量误差模型、非参数回归、函数型数据、生物统计方法。测量误差的统计理论以他为核心奠基人。",
         "none", "R.C."),
        ("Peter Hall", "彼得·霍尔 \\enspace·\\enspace 首位澳大利亚得主", 1989, "1951–2016", "澳大利亚", "Australian National University",
         "非参数统计与 Bootstrap", "Bootstrap 渐近理论、非参数曲线估计、经验似然。他是非参数统计领域最高产的奠基者之一。",
         "images/hall.jpg", "Wikipedia"),
        ("Peter McCullagh", "彼得·麦卡拉", 1990, "1952–", "美国（生于北爱尔兰）", "University of Chicago",
         "广义线性模型", "广义线性模型（GLM）、张量方法、分类数据分析。他与 Nelder 合著的 GLM 经典改变了应用统计，2026 年获 Guy 金奖章。",
         "none", "P.M."),
    ],
    "ep02": [
        ("Bernard Silverman", "伯纳德·西尔弗曼", 1991, "1952–", "英国", "University of Oxford",
         "密度估计与非参数回归", "密度估计、非参数回归、函数型数据分析。他的经典著作定义了密度估计这一方向。",
         "images/silverman.jpg", "Wikipedia"),
        ("Nancy Reid", "南希·里德 \\enspace·\\enspace 首位女性得主", 1992, "1952–", "加拿大", "University of Toronto",
         "渐近理论与复合似然", "复合似然、似然高阶渐近、鞍点近似。她是加拿大统计学的旗帜人物。",
         "images/reid.jpg", "Wikipedia"),
        ("Wing Hung Wong", "黄永康", 1993, "1952–", "美国（生于香港）", "Stanford University",
         "MCMC 与贝叶斯计算", "MCMC 方法、吉布斯抽样理论、计算生物学。他为贝叶斯计算的实用化作出开创性贡献。",
         "none", "W.H.W."),
        ("David L. Donoho", "戴维·多诺霍", 1994, "1957–", "美国", "Stanford University",
         "小波与压缩感知", "小波分析、压缩感知、高维统计推断。他是压缩感知的奠基人之一，2018 年获香农奖。",
         "images/donoho.jpg", "Wikipedia"),
        ("Iain M. Johnstone", "伊恩·约翰斯通", 1995, "1956–", "美国（生于加拿大）", "Stanford University",
         "随机矩阵与高维统计", "随机矩阵理论、小波阈值去噪、稀疏主成分。他在高维统计的理论化上影响深远。",
         "images/johnstone.jpg", "Wikipedia"),
        ("Robert J. Tibshirani", "罗伯特·蒂布希拉尼", 1996, "1956–", "美国/加拿大", "Stanford University",
         "LASSO 与统计学习", "LASSO、Bootstrap、交叉验证。他与 Hastie、Friedman 合著的 ESL 是现代统计学习经典。",
         "images/tibshirani.jpg", "Wikipedia"),
        ("Kathryn Roeder", "凯瑟琳·罗德", 1997, "1960–", "美国", "Carnegie Mellon University",
         "统计遗传学与多重检验", "统计遗传学、混合物模型、法医统计。她在疾病基因定位的统计方法上贡献突出。",
         "none", "K.R."),
        ("Pascal Massart", "帕斯卡尔·马萨尔 \\enspace·\\enspace 首位法国得主", 1998, "1958–", "法国", "Université de Paris-Sud",
         "浓度不等式与模型选择", "浓度不等式、经验过程、模型选择理论。他与 Bousquet 的工作重塑了非渐近统计学。",
         "none", "P.M."),
        ("Larry A. Wasserman", "拉里·瓦瑟曼", 1999, "1959–", "美国/加拿大", "Carnegie Mellon University",
         "非参数推断", "非参数推断、置信带方法、统计学习。他的 All of Statistics 是流传最广的统计入门之一。",
         "images/wasserman.png", "Wikipedia"),
        ("Jianqing Fan", "范剑青 \\enspace·\\enspace 首位华人·普林斯顿", 2000, "1962–", "美国（生于中国）", "Princeton University",
         "非参数与高维统计", "非参数模型、变系数模型、高维统计学习。他是华人统计学家的杰出代表。",
         "images/fan.jpg", "Wikipedia"),
    ],
    "ep03": [
        ("Xiao-Li Meng", "孟晓犁", 2001, "1963–", "美国（生于中国）", "Harvard University",
         "贝叶斯统计与计算", "EM 算法理论、MCMC 收敛诊断、缺失数据。他是哈佛统计系创系主任。",
         "none", "X.M."),
        ("Jun Liu", "刘军", 2002, "1965–", "美国（生于中国）", "Harvard University",
         "MCMC 与计算生物学", "MCMC 方法、序贯蒙特卡洛、系统生物学。他是贝叶斯计算与计算生物学交叉的领军者。",
         "none", "J.L."),
        ("Andrew Gelman", "安德鲁·格尔曼", 2003, "1965–", "美国", "Columbia University",
         "多层次贝叶斯模型", "多层次贝叶斯模型、Stan 概率编程、后验预测检查。BDA 经典教材影响一代统计学家。",
         "images/gelman.jpg", "Wikipedia"),
        ("Michael A. Newton", "迈克尔·牛顿", 2004, "1964–", "加拿大", "University of Wisconsin",
         "计算生物学", "计算生物学、基因表达数据分析、贝叶斯推断。他在基因组统计方法上持续深耕。",
         "none", "M.N."),
        ("Mark J. van der Laan", "马克·范德兰", 2005, "1967–", "美国（生于荷兰）", "UC Berkeley",
         "目标学习与因果推断", "目标极大似然估计（TMLE）、超级学习者、半参数因果推断。他为观察性研究提供严谨推断框架。",
         "none", "M.L."),
        ("Xihong Lin", "林希虹", 2006, "1966–", "美国（生于中国）", "Harvard University",
         "统计遗传学", "基因-环境交互、全基因组关联分析（GWAS）。她是华人女性统计学家典范。",
         "images/lin.jpg", "Wikipedia"),
        ("Jeff Rosenthal", "杰夫·罗森塔尔", 2007, "1967–", "加拿大", "University of Toronto",
         "MCMC 收敛理论", "MCMC 收敛理论、随机过程模拟。他的随机游走 Metropolis 收敛分析被广泛应用。",
         "images/rosenthal.jpg", "Wikipedia"),
        ("T. Tony Cai", "蔡天文", 2008, "1967–", "美国（生于中国）", "University of Pennsylvania",
         "高维统计推断", "高维协方差矩阵估计、非参数函数估计极小极大最优、多重检验。他是华人高维统计的代表。",
         "images/cai.jpg", "Wikipedia"),
        ("Rafael Irizarry", "拉斐尔·伊里萨里", 2009, "1972–", "美国（波多黎各）", "Harvard University",
         "基因组数据分析", "基因组数据标准化、微阵列方法、数据可视化。他的工具推动了生物信息学的标准化。",
         "none", "R.I."),
        ("David Dunson", "戴维·邓森", 2010, "1972–", "美国", "Duke University",
         "贝叶斯非参数", "贝叶斯非参数、高维潜变量模型、函数型数据先验。他在贝叶斯非参数的现代化上影响深远。",
         "none", "D.D."),
    ],
    "ep04": [
        ("Nilanjan Chatterjee", "尼兰詹·查特吉 \\enspace·\\enspace 首位印度裔得主", 2011, "1972–", "美国（生于印度）", "Johns Hopkins University",
         "统计遗传学与流行病学", "多基因风险评分、癌症风险建模、流行病学方法。他在疾病风险预测上贡献突出。",
         "images/chatterjee.png", "Wikipedia"),
        ("Samuel Kou", "寇星昌", 2012, "1974–", "美国（生于中国）", "Harvard University",
         "随机过程与生物物理", "单分子生物物理、随机过程与统计推断。他建立了单分子数据的统计推断框架。",
         "none", "S.K."),
        ("Marc A. Suchard", "马克·苏查德", 2013, "1972–", "美国", "UCLA",
         "贝叶斯系统发生学", "贝叶斯系统发生学、BEAST 软件、MCMC 计算。他的软件让系统发生学进入贝叶斯时代。",
         "none", "M.S."),
        ("Martin J. Wainwright", "马丁·温赖特", 2014, "1973–", "美国/加拿大", "UC Berkeley",
         "高维统计与图模型", "高维统计、图模型、信息论与优化。他的 High-Dimensional Statistics 是该领域标准教材。",
         "none", "M.W."),
        ("John D. Storey", "约翰·斯托里", 2015, "1978–", "美国", "Princeton University",
         "多重检验与 q-value", "q-value 框架、FDR 控制、统计基因组学。他的方法改变了组学数据分析。",
         "none", "J.S."),
        ("Nicolai Meinshausen", "尼古拉·迈因斯豪森 \\enspace·\\enspace 首位瑞士得主", 2016, "1978–", "瑞士/德国", "ETH Zürich",
         "高维统计与因果", "高维变量选择、不变因果预测、随机森林稳定性。他连接了高维统计与因果推断。",
         "none", "N.M."),
        ("Tyler J. VanderWeele", "泰勒·范德维勒", 2017, "1977–", "美国", "Harvard University",
         "因果中介分析", "因果中介分析、直接与间接效应分解、流行病学方法。他是现代因果推断方法论的代表人物，也研究宗教与健康的关系。",
         "images/vanderweele.jpg", "Wikipedia"),
        ("Richard J. Samworth", "理查德·萨姆沃思", 2018, "1978–", "英国", "University of Cambridge",
         "高维非参数估计", "高维非参数估计、变点检测、聚类与分类。他在理论统计与数据科学的交叉上成果丰硕。",
         "images/samworth.jpg", "Wikipedia"),
        ("Hadley Wickham", "哈德利·威克姆 \\enspace·\\enspace 数据科学革命", 2019, "1979–", "新西兰", "RStudio / Posit",
         "数据科学与可视化", "ggplot2、tidyverse、数据科学工作流。他是首位以软件开发为主要贡献获奖的得主。",
         "images/wickham.jpg", "Wikipedia"),
        ("Rina Foygel Barber", "里娜·巴伯 \\enspace·\\enspace 第二位女性得主", 2020, "1982/1983–", "美国", "University of Chicago",
         "选择性推断", "选择性推断、Knockoff 方法、FDR 后选择控制。她为高维回归的选择后推断奠定理论，2024 年获麦克阿瑟天才奖。",
         "none", "R.B."),
    ],
    "ep05": [
        ("Jeffrey T. Leek", "杰弗里·利克", 2021, "1980–", "美国", "Fred Hutchinson Cancer Center",
         "数据科学与可重复研究", "数据科学教育、可重复研究、统计基因组学。他的 Coursera 课程教育了全球数据科学家。",
         "images/leek.jpg", "Wikipedia"),
        ("Daniela Witten", "丹妮拉·维滕 \\enspace·\\enspace 第三位女性得主", 2022, "1984–", "美国", "University of Washington",
         "高维无监督学习", "高维无监督学习、稀疏聚类、图模型。她与 Hastie、Tibshirani 合著 ISLR 经典教材，其父为物理学家 Edward Witten。",
         "none", "D.W."),
        ("Ryan Tibshirani", "瑞安·蒂布希拉尼", 2023, "1985–", "美国/加拿大", "UC Berkeley",
         "保形预测与分布推断", "保形预测、分布推断、非参数回归。他推动了分布自由的现代推断方法。",
         "images/tibshirani_ryan.jpg", "Wikipedia"),
        ("Veronika Ročková", "维罗妮卡·罗奇科娃 \\enspace·\\enspace 第四位女性得主", 2024, "1985–", "美国（生于捷克斯洛伐克）", "University of Chicago",
         "贝叶斯高维模型选择", "尖峰平板先验（Spike-and-Slab）、贝叶斯高维模型选择、EM 变量选择。",
         "none", "V.R."),
        ("Lester Mackey", "莱斯特·麦基 \\enspace·\\enspace 首位工业界得主", 2025, "1983–", "美国", "Microsoft Research",
         "大规模机器学习", "大规模核方法、随机特征、概率推理与优化。他连接统计计算与大规模机器学习。",
         "none", "L.M."),
        ("Weijie Su", "苏炜杰 \\enspace·\\enspace 第九位华人得主", 2026, "1988–", "美国（生于中国）", "University of Pennsylvania",
         "深度学习理论", "深度学习理论、差分隐私、强化学习数学基础。他以数学工具严格化 AI 前沿。",
         "none", "W.S."),
    ],
}

EPISODES = [
    ("ep01", "episode-01-foundations-1981-1990", "copss_ep01_zh",
     "奠基年代", "1981–1990 · 统计理论大厦的奠基", "1981 – 1990", "从 Bickel 到 McCullagh"),
    ("ep02", "episode-02-bayesian-computation-1991-2000", "copss_ep02_zh",
     "贝叶斯复兴与计算革命", "1991–2000 · MCMC、小波与 LASSO", "1991 – 2000", "从 Silverman 到 Fan"),
    ("ep03", "episode-03-biostatistics-bioinformatics-2001-2010", "copss_ep03_zh",
     "生物统计爆发与华人崛起", "2001–2010 · 基因组时代与统计计算", "2001 – 2010", "从 Meng 到 Dunson"),
    ("ep04", "episode-04-highdim-ml-2011-2020", "copss_ep04_zh",
     "高维统计与机器学习融合", "2011–2020 · 高维推断与数据科学", "2011 – 2020", "从 Chatterjee 到 Barber"),
    ("ep05", "episode-05-data-science-ai-2021-2026", "copss_ep05_zh",
     "数据科学、AI 与贝叶斯革新", "2021–2026 · 统计学站上 AI 前沿", "2021 – 2026", "从 Leek 到 Su"),
]

NAMES_BAR = {
    "ep01": "Bickel · Fienberg · Lai · Hinkley · Berger · Prentice · Wu · Carroll · Hall · McCullagh",
    "ep02": "Silverman · Reid · Wong · Donoho · Johnstone · R. Tibshirani · Roeder · Massart · Wasserman · Fan",
    "ep03": "Meng · Liu · Gelman · Newton · van der Laan · Lin · Rosenthal · Cai · Irizarry · Dunson",
    "ep04": "Chatterjee · Kou · Suchard · Wainwright · Storey · Meinshausen · VanderWeele · Samworth · Wickham · Barber",
    "ep05": "Leek · Witten · R. Tibshirani · Ročková · Mackey · Su",
}

SYNTHESIS = {
    "ep01": {
        "title": "十年奠基：统计理论的现代格局",
        "sub": "1981–1990 · 从经验过程到 GLM",
        "chips": [("1981", "Bickel", "经验过程"), ("1984", "Hinkley", "Bootstrap"),
                  ("1985", "Berger", "贝叶斯决策"), ("1986", "Prentice", "生存分析"),
                  ("1987", "Wu", "试验设计"), ("1988", "Carroll", "测量误差"),
                  ("1989", "Hall", "非参数曲线"), ("1990", "McCullagh", "GLM")],
        "summary": "这一代把统计推断建立在严格的数学之上：经验过程、Bootstrap、GLM、试验设计与生存分析——经典现代统计的框架在此十年成形。",
    },
    "ep02": {
        "title": "计算革命：贝叶斯复兴与高维萌芽",
        "sub": "1991–2000 · MCMC、小波、LASSO",
        "chips": [("1991", "Silverman", "密度估计"), ("1992", "Reid", "复合似然"),
                  ("1993", "Wong", "MCMC"), ("1994", "Donoho", "小波/压缩感知"),
                  ("1995", "Johnstone", "随机矩阵"), ("1996", "R. Tibshirani", "LASSO"),
                  ("1998", "Massart", "浓度不等式"), ("2000", "Fan", "非参数统一")],
        "summary": "MCMC 让贝叶斯方法成为可能，小波与 LASSO 开启高维与信号处理的先声，浓度不等式则为非渐近理论奠基——统计学的计算时代到来。",
    },
    "ep03": {
        "title": "生物化、计算化与华人崛起",
        "sub": "2001–2010 · 基因组、因果与贝叶斯软件",
        "chips": [("2001", "Meng", "EM 理论"), ("2003", "Gelman", "Stan/多层次"),
                  ("2005", "van der Laan", "TMLE"), ("2006", "Lin", "GWAS"),
                  ("2007", "Rosenthal", "MCMC 收敛"), ("2008", "Cai", "高维协方差"),
                  ("2009", "Irizarry", "基因组数据"), ("2010", "Dunson", "贝叶斯非参数")],
        "summary": "统计全面拥抱基因组学与计算：TMLE 严格化因果推断，GWAS 方法支撑现代遗传学，同时华人得主在本十年集中涌现（孟晓犁、刘军、林希虹、蔡天文）。",
    },
    "ep04": {
        "title": "高维时代：统计×机器学习×数据科学",
        "sub": "2011–2020 · 高维推断、因果、多重检验",
        "chips": [("2014", "Wainwright", "高维理论"), ("2015", "Storey", "q-value"),
                  ("2016", "Meinshausen", "不变因果"), ("2017", "VanderWeele", "中介分析"),
                  ("2018", "Samworth", "高维非参数"), ("2019", "Wickham", "tidyverse"),
                  ("2020", "Barber", "Knockoff"), ("2020", "—", "选择性推断")],
        "summary": "高维统计理论走向成熟，因果推断与多重检验方法论成型，而 Wickham 的 tidyverse 让统计学的工具民主化——统计与数据科学全面融合。",
    },
    "ep05": {
        "title": "AI 时代的统计学",
        "sub": "2021–2026 · 数据科学、保形预测、深度学习",
        "chips": [("2021", "Leek", "数据科学教育"), ("2022", "Witten", "高维无监督"),
                  ("2023", "R. Tibshirani", "保形预测"), ("2024", "Ročková", "尖峰平板"),
                  ("2025", "Mackey", "大规模核方法"), ("2026", "Su", "深度学习理论")],
        "summary": "统计学成为数据科学的核心语言：保形预测定义分布推断新范式，贝叶斯高维方法革新，而 Su 以深度学习理论获奖，标志着统计学站上 AI 前沿。",
    },
}

HEADER = r"""% COPSS Presidents' Award Video — Episode {EP}
% {TITLE}（{RANGE}）
% 参照 Abel_Prize / Chern_Medal / Fields_Medal video 系列的 Beamer 版式
% Source: COPSS/pages 离线页面 + copss_winners.md + Wikipedia
\documentclass[aspectratio=169,14pt]{beamer}
\usetheme{default}\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{\hfill{\scriptsize\color{covermuted}\insertframenumber/\inserttotalframenumber}\hspace{0.4cm}\vspace{0.15cm}}
\usepackage{fontspec}\usepackage{xeCJK}
\setCJKmainfont{PingFang SC}[BoldFont=PingFang SC Semibold]
\setmainfont{Helvetica Neue}[BoldFont=Helvetica Neue Bold]
\usepackage{xcolor}\usepackage{tikz}\usepackage{graphicx}\usepackage{adjustbox}\usepackage{fontawesome5}\usepackage{ifthen}
\usetikzlibrary{positioning,calc,arrows.meta,shadows}

% ===== 配色：COPSS —— 统计蓝主色 + 统计红强调 + 暖金 + 紫罗兰 =====
\definecolor{bgmain}{RGB}{238,244,251}
\definecolor{panel}{RGB}{240,246,253}
\definecolor{factbg}{RGB}{246,249,253}
\definecolor{coverprimary}{HTML}{2166AC}
\definecolor{coveraccent}{HTML}{B2182B}
\definecolor{coveramber}{HTML}{E0913A}
\definecolor{coverpurple}{HTML}{6A51A3}
\definecolor{coverdark}{HTML}{1B2A41}
\definecolor{covermuted}{HTML}{5B6B7F}
\definecolor{coverlight}{HTML}{E6EBF2}
\definecolor{titlecolor}{RGB}{22,32,46}
\definecolor{muteddark}{RGB}{72,90,110}
\definecolor{bluepanel}{RGB}{220,235,250}
\definecolor{redpanel}{RGB}{250,226,228}
\definecolor{goldpanel}{RGB}{250,240,224}
\definecolor{purplepanel}{RGB}{235,230,248}
\definecolor{graypanel}{RGB}{239,243,248}
\definecolor{greenpanel}{RGB}{225,242,235}
\setbeamercolor{background canvas}{bg=bgmain}

\newcommand{\plainbar}{%
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverdark, opacity=0.06] (current page.south west) rectangle ([yshift=0.4cm]current page.south east);
  \draw[coverprimary, opacity=0.40, line width=0.8pt] ([yshift=0.4cm]current page.south west) -- ([yshift=0.4cm]current page.south east);
\end{tikzpicture}%
}

\newcommand{\sectiontitle}[2]{%
\vspace{-0.52cm}
\begin{center}
  {\fontsize{20}{24}\selectfont\bfseries\color{titlecolor} #1}\\[2pt]
  {\fontsize{7.5}{9.5}\selectfont\itshape\color{muteddark} #2}
\end{center}
\vspace{0.06cm}
}

% ---- Person slide: #1 name #2 subtitle #3 img或none #4 credit或缩写 #5 year #6 life #7 country #8 inst #9 contribution(含研究方向) ----
\newcommand{\personslide}[9]{%
\begin{frame}
\plainbar
\vspace{-0.45cm}
\begin{center}
  {\fontsize{22}{26}\selectfont\bfseries\color{coverdark} #1}\\[2pt]
  {\fontsize{9.5}{11.5}\selectfont\color{muteddark} #2}
\end{center}
\vspace{0.1cm}
\begin{columns}[c]
\begin{column}{0.22\textwidth}
  \centering
  \ifthenelse{\equal{#3}{none}}{%
    \begin{tikzpicture}
      \node[circle, fill=coverprimary!12, draw=coverprimary!38, minimum size=2.6cm]
        {\fontsize{16}{19}\selectfont\bfseries\color{coverprimary!75!black} #4};
    \end{tikzpicture}
    {\par\vspace{1pt}\fontsize{6.2}{7.2}\selectfont\color{covermuted} 暂无公开照片\par}
  }{%
    \begin{tikzpicture}
      \node[draw=coverprimary!28, line width=0.7pt, fill=white, rounded corners=3pt, inner sep=2.5pt, drop shadow={shadow xshift=0.5pt, shadow yshift=-0.5pt, opacity=0.12}] {
        \includegraphics[width=2.2cm,height=2.7cm,keepaspectratio]{#3}
      };
    \end{tikzpicture}
    {\par\vspace{1pt}\fontsize{6.2}{7.2}\selectfont\color{covermuted} 图片来源：#4\par}
  }
\end{column}
\begin{column}{0.28\textwidth}
  \begin{tikzpicture}
    \node[fill=goldpanel, rounded corners=4pt, inner xsep=6pt, inner ysep=5pt, text width=3.8cm, align=left] {
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 获奖}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #5}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 生卒}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #6}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 国别}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #7}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 机构}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #8}
    };
  \end{tikzpicture}
\end{column}
\begin{column}{0.48\textwidth}
  \begin{tikzpicture}
    \node[draw=coverprimary!35, fill=bluepanel, rounded corners=5pt, inner sep=7pt, text width=6.4cm, anchor=north west] at (0,0) {
      {\fontsize{8.2}{10}\selectfont\bfseries\color{coverprimary!82!black} 核心贡献}\\[3pt]
      {\fontsize{7}{8.5}\selectfont\color{coverdark!84} #9}
    };
  \end{tikzpicture}
\end{column}
\end{columns}
\end{frame}
}

% ---- Title slide: #1 集数徽章 #2 大标题 #3 副标题 #4 年份范围 #5 说明 #6 得主名字条 ----
\newcommand{\titleslide}[6]{%
\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverprimary!6] (current page.north west) rectangle (current page.south east);
  \fill[coverprimary!14] ([xshift=-4.1cm,yshift=3.2cm]current page.west) rectangle ([xshift=-3.7cm,yshift=-3.2cm]current page.west);
  \fill[coveraccent!10] (current page.south east) ++(-2.3,-1.7) circle (2.0cm);
  \fill[coveramber!14] (current page.north east) ++(-2.4,1.4) circle (1.2cm);
  \fill[coverpurple!10] (current page.north west) ++(3.0,-1.0) circle (0.9cm);
  \fill[coveramber!12] (current page.south west) ++(2.8,1.7) circle (1.2cm);
  % 集数徽章
  \node[rounded corners=7pt, fill=coveraccent, inner xsep=10pt, inner ysep=5pt,
        font=\fontsize{9.5}{11}\selectfont\bfseries, text=white,
        drop shadow={shadow xshift=0.4pt, shadow yshift=-0.4pt, opacity=0.15}]
    at ([yshift=3.30cm]current page.center) {#1};
  % 大标题
  \node[anchor=center, font=\fontsize{30}{36}\selectfont\bfseries, text=coverdark]
    at ([yshift=2.00cm]current page.center) {#2};
  % 副标题
  \node[anchor=center, font=\fontsize{13.5}{17}\selectfont, text=coverprimary!85!black]
    at ([yshift=1.00cm]current page.center) {#3};
  \draw[coverprimary!60, line width=1.4pt] ([yshift=0.18cm, xshift=-4.55cm]current page.center)
    -- ([yshift=0.18cm, xshift=4.55cm]current page.center);
  % 年份范围
  \node[anchor=center, font=\fontsize{13}{16}\selectfont\bfseries, text=coveramber!70!black]
    at ([yshift=-0.62cm]current page.center) {#4};
  % 说明
  \node[anchor=center, font=\fontsize{8.5}{10.5}\selectfont, text=covermuted]
    at ([yshift=-1.30cm]current page.center) {#5};
  % 得主名字条
  \node[anchor=center, font=\fontsize{7.2}{8.6}\selectfont\bfseries, text=coverdark!70]
    at ([yshift=-2.25cm]current page.center) {#6};
  % 底部角标
  \node[anchor=south, font=\scriptsize, text=coverdark!40]
    at ([yshift=0.38cm]current page.south) {\faIcon{medal}\enspace COPSS Presidents' Award\enspace|\enspace 1981–2026};
\end{tikzpicture}
\end{frame}
}
"""


def cmd_name(name):
    s = name.replace(".", "").replace("-", "").replace(" ", "").replace("'", "")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return s.lower()


def esc(s):
    return str(s).replace("&", "\\&")


def compute_age(year, life):
    """Award age = award year - birth year (e.g. '1940–' -> 41 for 1981).
    Returns '37/38岁' for ambiguous '1982/1983–', None if no birth year."""
    import re as _re
    m = _re.search(r'(19|20)\d{2}(?:/(19|20)\d{2})?', life.replace("–", "-"))
    if not m:
        return None
    part = m.group(0)
    if "/" in part:
        y1, y2 = part.split("/")
        a1, a2 = year - int(y1), year - int(y2)
        lo, hi = min(a1, a2), max(a1, a2)
        return "%d/%d岁" % (lo, hi) if lo != hi else "%d岁" % lo
    return "%d岁" % (year - int(part))


def resolve_img(p, ep_dir):
    """If a laureate has no photo ('none') but a non-empty images/<name>.<ext>
    file exists in the episode dir, use it automatically."""
    name, subtitle, year, life, country, inst, tag, contrib, img, credit = p
    if img == "none" and ep_dir:
        base = cmd_name(name)
        for ext in (".jpg", ".jpeg", ".png", ".webp"):
            cand = os.path.join(HERE, ep_dir, "images", base + ext)
            if os.path.exists(cand) and os.path.getsize(cand) > 0:
                return "images/" + base + ext
    return img


def person_slide(p, prefix="", ep_dir=None):
    name, subtitle, year, life, country, inst, tag, contrib, img, credit = p
    img = resolve_img(p, ep_dir)
    body = "研究方向：%s。%s" % (tag, contrib)
    cname = prefix + cmd_name(name)
    age = compute_age(year, life)
    year_str = "%d（%s）" % (year, age) if age else str(year)
    return ("\\newcommand{\\%sslide}{\\personslide\n"
            "  {%s}{%s}\n"
            "  {%s}{%s}\n"
            "  {%s}{%s}{%s}{%s}\n"
            "  {%s}}\n" % (
                cname,
                esc(name), esc(subtitle), img, credit, year_str, esc(life),
                esc(country), esc(inst), esc(body)))


def synthesis_slide(ep):
    s = SYNTHESIS[ep]
    # build chips with alternating colors
    cols = [("bluepanel", "coverprimary!35", "coverprimary!85!black"),
            ("goldpanel", "coveramber!35", "coveramber!85!black"),
            ("redpanel", "coveraccent!35", "coveraccent!85!black"),
            ("purplepanel", "coverpurple!35", "coverpurple!85!black")]
    xs = [-5.4, -2.7, 0.0, 2.7, 5.4]
    rows = []
    n = len(s["chips"])
    for i, (yr, nm, kw) in enumerate(s["chips"]):
        col = cols[i % 4]
        x = xs[i % 5]
        y = 1.55 - (i // 5) * 1.35
        rows.append("  \\node[chip, fill=%s, draw=%s, text=%s] at (%s,%.2f) {\\textbf{%s}\\\\%s\\\\%s};" % (
            col[0], col[1], col[2], x, y, yr, nm, kw))
    chipblock = "\n".join(rows)
    return ("\\newcommand{\\synthesisslide}{%%\n"
            "\\begin{frame}\n"
            "\\plainbar\n"
            "\\sectiontitle{%s}{%s}\n"
            "\\begin{center}\n"
            "\\begin{tikzpicture}[\n"
            "  chip/.style={rounded corners=4pt, inner xsep=4pt, inner ysep=3pt, text width=1.9cm, align=center, font=\\fontsize{6}{7.2}\\selectfont}\n"
            "]\n%s\n"
            "\\end{tikzpicture}\n"
            "\\end{center}\n"
            "\\vspace{0.12cm}\n"
            "\\begin{center}\n"
            "\\begin{tikzpicture}\n"
            "  \\node[draw=coverprimary!40, fill=bluepanel, rounded corners=5pt, inner sep=8pt, text width=13.4cm, align=center] at (0,0) {%%\n"
            "    {\\fontsize{8}{9.5}\\selectfont\\bfseries\\color{coverdark!80} 本集综述}\\par\\vspace{3pt}\n"
            "    {\\fontsize{7.4}{8.8}\\selectfont\\color{coverdark!72} %s}\n"
            "  };\n"
            "\\end{tikzpicture}\n"
            "\\end{center}\n"
            "\\end{frame}\n"
            "}\n" % (s["title"], s["sub"], chipblock, esc(s["summary"])))


def make_episode_tex(ep_key, ep_dir, main, title, subtitle, rng, note):
    people = PEOPLE[ep_key]
    out = [HEADER.replace("{EP}", ep_key[-1]).replace("{TITLE}", title).replace("{RANGE}", title)]
    out.append("\n% ========== SLIDES ==========\n")
    # person slides
    for p in people:
        out.append(person_slide(p, ep_dir=ep_dir))
    # synthesis
    out.append(synthesis_slide(ep_key))
    # main
    names = [cmd_name(p[0]) for p in people]
    body = "\n".join("\\%sslide" % n for n in names)
    out.append("\n% ========== MAIN ==========\n\\begin{document}\n")
    out.append("\\titleslide{%s}{%s}{%s}{%s}{%s}{%s}\n" % (
        "第 %s 集" % ep_key[-1], title, subtitle, rng,
        "%s · %d 位得主" % (note, len(people)), NAMES_BAR[ep_key]))
    out.append(body + "\n")
    out.append("\\synthesisslide\n")
    out.append("\\end{document}\n")
    path = os.path.join(HERE, ep_dir, main + ".tex")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("wrote", path)


def make_makefile(ep_dir, main):
    tmpl = open(os.path.join(HERE, "episode-00-what-is-copss-presidents-award", "Makefile"),
                encoding="utf-8").read()
    tmpl = tmpl.replace("copss_ep00_zh", main)
    path = os.path.join(HERE, ep_dir, "Makefile")
    with open(path, "w", encoding="utf-8") as f:
        f.write(tmpl)
    print("wrote", path)


# ---- allinone ----
# num | prefix(纯字母命令名前缀) | title | subtitle | range | ep_key
CHAPTERS = [
    ("01", "epone", "奠基年代", "统计理论大厦的奠基", "1981–1990", "ep01"),
    ("02", "eptwo", "贝叶斯复兴与计算革命", "MCMC、小波与 LASSO", "1991–2000", "ep02"),
    ("03", "epthree", "生物统计爆发与华人崛起", "基因组时代与统计计算", "2001–2010", "ep03"),
    ("04", "epfour", "高维统计与机器学习融合", "高维推断与数据科学", "2011–2020", "ep04"),
    ("05", "epfive", "数据科学、AI 与贝叶斯革新", "统计学站上 AI 前沿", "2021–2026", "ep05"),
]

CHAPTER_SLIDE = r"""
% ---- Chapter divider: #1 num #2 title #3 subtitle #4 range ----
\newcommand{\chapterslide}[4]{%
\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverprimary!10] (current page.north west) rectangle (current page.south east);
  \fill[coveraccent!12] (current page.north west) ++(1.9,-1.5) circle (2.3cm);
  \fill[coveramber!12] (current page.south east) ++(-2.0,1.6) circle (2.5cm);
  \node[anchor=center, font=\fontsize{14}{18}\selectfont\bfseries, text=coveraccent!80!black]
    at ([yshift=2.0cm]current page.center) {第 #1 章};
  \node[anchor=center, font=\fontsize{30}{36}\selectfont\bfseries, text=coverdark]
    at ([yshift=0.9cm]current page.center) {#2};
  \node[anchor=center, font=\fontsize{14}{18}\selectfont, text=coverprimary!85!black]
    at ([yshift=-0.5cm]current page.center) {#3};
  \draw[coverprimary, line width=1.4pt] ([yshift=-1.3cm, xshift=-4.55cm]current page.center)
    -- ([yshift=-1.3cm, xshift=4.55cm]current page.center);
  \node[anchor=center, font=\fontsize{10}{12}\selectfont\bfseries, text=coveramber!60!black]
    at ([yshift=-1.9cm]current page.center) {#4};
\end{tikzpicture}
\end{frame}
}
"""


def make_coverslide(ep_dir):
    """Cover slide: title + 46 portrait thumbnails grid (16x3)."""
    people = []
    for num, prefix, title, subtitle, rng, ep_key in CHAPTERS:
        people.extend(PEOPLE[ep_key])
    N_COLS, N_ROWS = 16, 3
    W, H, GAP = 0.60, 0.70, 0.05
    TOTAL_W = (N_COLS - 1) * (W + GAP)
    TOTAL_H = (N_ROWS - 1) * (H + GAP)
    START_X = -TOTAL_W / 2
    START_Y = TOTAL_H / 2
    grid = []
    grid.append(r'  \node[anchor=center] at ([yshift=-1.50cm]current page.center) {')
    grid.append(r'    \begin{tikzpicture}[scale=1]')
    count = 0
    for row in range(N_ROWS):
        for col in range(N_COLS):
            if count >= len(people):
                break
            p = people[count]
            img = resolve_img(p, ep_dir)
            x = START_X + col * (W + GAP)
            y = START_Y - row * (H + GAP)
            grid.append('      \\node[inner sep=0pt, draw=coverprimary!22, line width=0.2pt] at (%.2f,%.2f) {' % (x, y))
            grid.append('        \\includegraphics[width=%scm,height=%scm,keepaspectratio]{%s}' % (W, H, img))
            grid.append('      };')
            count += 1
    grid.append(r'    \end{tikzpicture}')
    grid.append(r'  };')
    grid_tikz = '\n'.join(grid)
    return (r'''\newcommand{\coverslide}{%
\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverprimary!6] (current page.north west) rectangle (current page.south east);
  \fill[coveraccent!10] (current page.south east) ++(-2.3,-1.7) circle (2.0cm);
  \fill[coveramber!14] (current page.north east) ++(-2.4,1.4) circle (1.2cm);
  \fill[coverpurple!10] (current page.north west) ++(3.0,-1.0) circle (0.9cm);
  \node[anchor=center, font=\fontsize{24}{30}\selectfont\bfseries, text=coverdark]
    at ([yshift=2.60cm]current page.center) {COPSS 会长奖 · 全部得主};
  \node[anchor=center, font=\fontsize{12.5}{16}\selectfont, text=coverprimary!85!black]
    at ([yshift=1.45cm]current page.center) {COPSS Presidents' Award · 统计学界的最高荣誉 · 全 46 位得主合集};
  \draw[coverprimary, line width=1.4pt] ([yshift=0.75cm, xshift=-5.2cm]current page.center)
    -- ([yshift=0.75cm, xshift=5.2cm]current page.center);
  \node[anchor=center, font=\fontsize{10.5}{14}\selectfont\bfseries, text=coveramber!58!black]
    at ([yshift=0.05cm]current page.center) {1981–2026 · 从 Bickel 到 Su · 46 位统计学家};
''' + grid_tikz + r'''
  \node[anchor=south, font=\scriptsize, text=coverdark!40]
    at ([yshift=0.38cm]current page.south) {\faIcon{medal}\enspace COPSS Presidents' Award\enspace|\enspace 1981–2026\enspace|\enspace 合集};
\end{tikzpicture}
\end{frame}
}''')


def make_allinone_tex():
    ep_dir = "episode-allinone"
    main = "copss_allinone_zh"
    out = [HEADER.replace("{EP}", "allinone").replace("{TITLE}", "合集").replace("{RANGE}", "1981–2026")]
    out.append(CHAPTER_SLIDE)
    out.append(make_coverslide(ep_dir))
    out.append("\n% ========== SLIDES ==========\n")
    # per-chapter person slides with unique prefixes
    for num, prefix, title, subtitle, rng, ep_key in CHAPTERS:
        for p in PEOPLE[ep_key]:
            out.append(person_slide(p, prefix=prefix, ep_dir=ep_dir))
    # main: cover + chapter dividers + person slides
    out.append("\n% ========== MAIN ==========\n\\begin{document}\n")
    out.append("\\coverslide\n")
    for num, prefix, title, subtitle, rng, ep_key in CHAPTERS:
        out.append("\\chapterslide{%s}{%s}{%s}{%s}\n" % (num, title, subtitle, rng))
        body = "\n".join("\\%s%sslide" % (prefix, cmd_name(p[0])) for p in PEOPLE[ep_key])
        out.append(body + "\n")
    out.append("\\end{document}\n")
    path = os.path.join(HERE, ep_dir, main + ".tex")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("wrote", path)


def main():
    for ep_key, ep_dir, main, title, subtitle, rng, note in EPISODES:
        make_episode_tex(ep_key, ep_dir, main, title, subtitle, rng, note)
        make_makefile(ep_dir, main)
    make_allinone_tex()
    make_makefile("episode-allinone", "copss_allinone_zh")


if __name__ == "__main__":
    main()
