#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Turing Award video episode Beamer decks (ep01-10 + allinone).

Data: 81 laureates (1966-2025) grouped into 10 topical episodes (T1-T10).
Run from turing/:  python3 gen_turing.py
"""
import os
import re
import shutil
import unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(HERE, "pages")

# ---------------- data ----------------
# (name_en, subtitle_zh, year, life, country, inst, contribution)
DATA = {
    "ep01": [  # T1 理论计算机科学
        ("Stephen Cook", "史蒂芬·库克", 1982, "1939–", "美国/加拿大", "University of Toronto",
         "P 与 NP 问题、Cook-Levin 定理，计算复杂性理论奠基人之一。"),
        ("Richard Karp", "理查德·卡普", 1985, "1935–", "美国", "UC Berkeley",
         "NP 完全性理论、Karp 归约，组合优化的算法大师。"),
        ("John Hopcroft", "约翰·霍普克罗夫特", 1986, "1939–", "美国", "Cornell University",
         "算法设计与自动机理论，图算法经典教材作者。"),
        ("Robert Tarjan", "罗伯特·塔扬", 1986, "1948–", "美国", "Princeton University",
         "并查集、最近公共祖先、强连通分量等图算法的发明者。"),
        ("Juris Hartmanis", "尤里斯·哈特马尼斯", 1993, "1928–2022", "美国/拉脱维亚", "Cornell University",
         "计算复杂性分层定理，复杂性理论共同奠基人。"),
        ("Richard E. Stearns", "理查德·斯特恩斯", 1993, "1936–", "美国", "SUNY Albany",
         "计算复杂性理论奠基，与 Hartmanis 同获 1993 年奖。"),
        ("Manuel Blum", "曼努埃尔·布鲁姆", 1995, "1938–", "美国", "Carnegie Mellon University",
         "计算复杂性、Blum Blum Shub 伪随机生成器。"),
        ("Donald Knuth", "唐纳德·高德纳", 1974, "1938–", "美国", "Stanford University",
         "《计算机程序设计艺术》、算法分析、TeX 排版系统。"),
        ("Michael O. Rabin", "迈克尔·拉宾", 1976, "1931–", "以色列/美国", "Harvard University",
         "非确定性自动机、随机算法、米勒-拉宾素性检验。"),
        ("Leslie Valiant", "莱斯利·瓦利安特", 2010, "1949–", "英国/美国", "Harvard University",
         "PAC 学习理论、VLSI 计算复杂度，学习理论奠基人。"),
        ("Avi Wigderson", "阿维·威格德森", 2023, "1956–", "以色列/美国", "Institute for Advanced Study",
         "随机性与计算、伪随机性与去随机化，理论计算机巨星。"),
    ],
    "ep02": [  # T2 程序设计语言·编译·方法学
        ("Alan J. Perlis", "艾伦·佩利斯", 1966, "1922–1990", "美国", "Carnegie Mellon University",
         "首届得主，Algol 语言与编译技术先驱。"),
        ("John Backus", "约翰·巴克斯", 1977, "1924–2007", "美国", "IBM",
         "Fortran 语言之父，BNF 文法描述编程语言语法。"),
        ("Robert W. Floyd", "罗伯特·弗洛伊德", 1978, "1936–2001", "美国", "Stanford University",
         "程序设计方法学、Floyd 算法（判圈/最短路径）。"),
        ("Kenneth E. Iverson", "肯尼思·艾弗森", 1979, "1920–2004", "加拿大", "IBM",
         "APL 语言，交互式数组编程。"),
        ("Tony Hoare", "托尼·霍尔", 1980, "1934–", "英国", "University of Oxford",
         "快速排序、Hoare 逻辑（程序验证）、CSP 通信顺序进程。"),
        ("Niklaus Wirth", "尼克劳斯·沃斯", 1984, "1934–", "瑞士", "ETH Zurich",
         "Pascal、Modula 语言，结构化程序设计。"),
        ("Dana Scott", "达纳·斯科特", 1976, "1932–", "美国", "Carnegie Mellon University",
         "域理论，为程序语义学奠定数学基础。"),
        ("Robin Milner", "罗宾·米尔纳", 1991, "1934–2010", "英国", "University of Edinburgh",
         "ML 语言、LCF 定理证明、$\\pi$ 演算（并发理论）。"),
        ("Ole-Johan Dahl", "奥利-约翰·达尔", 2001, "1931–2002", "挪威", "University of Oslo",
         "面向对象编程（Simula 语言），OOP 先驱。"),
        ("Kristen Nygaard", "克里斯汀·尼加德", 2001, "1926–2002", "挪威", "University of Oslo",
         "面向对象编程（Simula 语言），与 Dahl 同获 2001 年奖。"),
        ("Alan Kay", "艾伦·凯", 2003, "1940–", "美国", "—",
         "Smalltalk、面向对象思想、图形用户界面，个人计算愿景。"),
        ("Peter Naur", "彼得·诺尔", 2005, "1928–2016", "丹麦", "—",
         "Algol 60、BNF 文法、软件工程方法论。"),
        ("Fred Brooks", "弗雷德·布鲁克斯", 1999, "1931–2022", "美国", "University of North Carolina",
         "OS/360 软件工程、《人月神话》作者。"),
        ("Alfred Aho", "阿尔弗雷德·阿霍", 2020, "1941–", "美国", "Columbia University",
         "编译器理论、《龙书》合著者。"),
        ("Jeffrey Ullman", "杰弗里·乌尔曼", 2020, "1942–", "美国", "Stanford University",
         "编译、数据库、数据挖掘、《龙书》合著者。"),
    ],
    "ep03": [  # T3 AI 与机器学习
        ("Marvin Minsky", "马文·明斯基", 1969, "1927–2016", "美国", "MIT",
         "人工智能奠基人，框架理论、神经网络早期研究。"),
        ("John McCarthy", "约翰·麦卡锡", 1971, "1927–2011", "美国", "Stanford University",
         "AI 奠基人，提出「人工智能」一词，Lisp 之父。"),
        ("Allen Newell", "艾伦·纽厄尔", 1975, "1927–1992", "美国", "Carnegie Mellon University",
         "人工智能、认知科学，逻辑理论机。"),
        ("Herbert A. Simon", "赫伯特·西蒙", 1975, "1916–2001", "美国", "Carnegie Mellon University",
         "认知科学，另获诺贝尔经济学奖（1978）——图灵+诺奖双料。"),
        ("Edward Feigenbaum", "爱德华·费根鲍姆", 1994, "1936–", "美国", "Stanford University",
         "专家系统、知识工程，AI 应用先驱。"),
        ("Raj Reddy", "拉吉·雷迪", 1994, "1937–", "美国/印度", "Carnegie Mellon University",
         "人工智能、语音识别。"),
        ("Judea Pearl", "朱迪亚·珀尔", 2011, "1936–", "美国/以色列", "UCLA",
         "贝叶斯网络、因果推断，AI 概率推理奠基人。"),
        ("Yoshua Bengio", "约书亚·本吉奥", 2018, "1964–", "加拿大/法国", "Université de Montréal",
         "深度学习三杰之一，表示学习与生成模型。"),
        ("Geoffrey Hinton", "杰弗里·辛顿", 2018, "1947–", "英国/加拿大", "University of Toronto",
         "深度学习三杰之一，反向传播、神经网络复兴。"),
        ("Yann LeCun", "杨立昆", 2018, "1960–", "法国/美国", "New York University",
         "深度学习三杰之一，卷积神经网络（CNN）之父。"),
        ("Andrew Barto", "安德鲁·巴托", 2024, "1948–", "美国", "University of Massachusetts",
         "强化学习奠基人，时间差分学习。"),
        ("Richard S. Sutton", "理查德·萨顿", 2024, "1956–", "加拿大/美国", "University of Alberta",
         "强化学习奠基人，《强化学习导论》合著者。"),
    ],
    "ep04": [  # T4 操作系统·体系结构
        ("Maurice Wilkes", "莫里斯·威尔克斯", 1967, "1913–2010", "英国", "University of Cambridge",
         "EDSAC 存储程序计算机、微程序设计。"),
        ("Ken Thompson", "肯·汤普森", 1983, "1943–", "美国", "Bell Labs",
         "Unix 操作系统与 C 语言共同之父。"),
        ("Dennis Ritchie", "丹尼斯·里奇", 1983, "1941–2011", "美国", "Bell Labs",
         "C 语言设计者、Unix 共同作者。"),
        ("John Cocke", "约翰·科克", 1987, "1925–2002", "美国", "IBM",
         "RISC 架构、编译器优化，IBM 体系结构先驱。"),
        ("Fernando J. Corbató", "费尔南多·科巴托", 1990, "1926–2019", "美国", "MIT",
         "分时系统 CTSS、Multics，操作系统奠基人。"),
        ("Frances E. Allen", "弗朗西丝·艾伦", 2006, "1932–2020", "美国", "IBM",
         "编译器优化、并行计算，首位女性图灵奖得主。"),
        ("John L. Hennessy", "约翰·亨尼西", 2017, "1952–", "美国", "Stanford University",
         "RISC 体系结构，计算机体系结构教科书作者。"),
        ("David Patterson", "大卫·帕特森", 2017, "1947–", "美国", "UC Berkeley",
         "RISC、RAID，与 Hennessy 共同奠基现代体系结构。"),
    ],
    "ep05": [  # T5 数据库
        ("Charles Bachman", "查尔斯·巴赫曼", 1973, "1924–2017", "美国", "—",
         "CODASYL 网状数据库模型，数据库系统奠基人。"),
        ("Edgar F. Codd", "埃德加·科德", 1981, "1923–2003", "英国/美国", "IBM",
         "关系数据库模型，SQL 的理论根基。"),
        ("Jim Gray", "吉姆·格雷", 1998, "1944–2012", "美国", "Microsoft Research",
         "事务处理、数据库系统与在线分析处理。"),
        ("Michael Stonebraker", "迈克尔·斯通布雷克", 2014, "1943–", "美国", "MIT",
         "Ingres、PostgreSQL 数据库系统，流处理先驱。"),
    ],
    "ep06": [  # T6 网络·万维网
        ("Vint Cerf", "文顿·瑟夫", 2004, "1943–", "美国", "—",
         "TCP/IP 协议共同设计者，互联网之父之一。"),
        ("Robert Kahn", "罗伯特·卡恩", 2004, "1938–", "美国", "—",
         "TCP/IP 协议共同设计者，互联网架构奠基。"),
        ("Tim Berners-Lee", "蒂姆·伯纳斯-李", 2016, "1955–", "英国", "W3C / MIT",
         "万维网（WWW）发明者，HTML、HTTP、URL。"),
        ("Robert Metcalfe", "罗伯特·梅特卡夫", 2022, "1946–", "美国", "MIT",
         "以太网（Ethernet）发明者，梅特卡夫定律。"),
    ],
    "ep07": [  # T7 分布式·并发·验证
        ("Edsger W. Dijkstra", "埃德加·迪杰斯特拉", 1972, "1930–2002", "荷兰", "Eindhoven University of Technology",
         "结构化编程、Dijkstra 最短路径算法、并发原语。"),
        ("Butler W. Lampson", "巴特勒·兰普森", 1992, "1943–", "美国", "Microsoft Research",
         "分布式系统、安全与容错，个人计算愿景。"),
        ("Amir Pnueli", "阿米尔·普努利", 1996, "1941–2009", "以色列", "Weizmann Institute",
         "时态逻辑、程序验证，反应系统形式化。"),
        ("Edmund M. Clarke", "埃德蒙·克拉克", 2007, "1945–2020", "美国", "Carnegie Mellon University",
         "模型检验（Model Checking）奠基人。"),
        ("E. Allen Emerson", "艾伦·埃默森", 2007, "1954–", "美国", "University of Texas at Austin",
         "模型检验、时态逻辑。"),
        ("Joseph Sifakis", "约瑟夫·西法基斯", 2007, "1946–", "法国/希腊", "Verimag",
         "模型检验、并发系统验证。"),
        ("Leslie Lamport", "莱斯利·兰波特", 2013, "1941–", "美国", "Microsoft Research",
         "Paxos 共识算法、时序逻辑、LaTeX。"),
        ("Barbara Liskov", "芭芭拉·利斯科夫", 2008, "1939–", "美国", "MIT",
         "分布式系统、数据抽象、Liskov 替换原则，第二位女性得主。"),
    ],
    "ep08": [  # T8 密码学·量子信息
        ("Andrew Yao", "姚期智", 2000, "1946–", "美国/中国", "Princeton University / Tsinghua",
         "通信复杂性、密码学、量子计算——首位华人图灵奖得主。"),
        ("Ronald Rivest", "罗纳德·里维斯特", 2002, "1947–", "美国", "MIT",
         "RSA 公钥密码学三杰之一。"),
        ("Adi Shamir", "阿迪·沙米尔", 2002, "1952–", "以色列", "Weizmann Institute",
         "RSA 三杰之一，Shamir 秘密共享、密码分析。"),
        ("Leonard Adleman", "伦纳德·阿德尔曼", 2002, "1945–", "美国", "MIT",
         "RSA 三杰之一，DNA 计算先驱。"),
        ("Shafi Goldwasser", "沙菲·戈德瓦瑟", 2012, "1958–", "美国/以色列", "MIT / Weizmann",
         "概率加密、零知识证明，现代密码学奠基。"),
        ("Silvio Micali", "西尔维奥·米卡利", 2012, "1954–", "意大利/美国", "MIT",
         "零知识证明、可验证随机函数。"),
        ("Whitfield Diffie", "惠特菲尔德·迪菲", 2015, "1944–", "美国", "—",
         "公钥密码学（Diffie-Hellman 密钥交换）。"),
        ("Martin Hellman", "马丁·赫尔曼", 2015, "1945–", "美国", "Stanford University",
         "公钥密码学（Diffie-Hellman 密钥交换）。"),
        ("Charles H. Bennett", "查尔斯·贝内特", 2025, "1943–", "美国", "IBM",
         "量子信息科学、BB84 量子密钥分发、可逆计算。"),
        ("Gilles Brassard", "吉勒·布拉萨", 2025, "1955–", "加拿大", "Université de Montréal",
         "量子密码学、BB84 协议、量子纠缠理论。"),
    ],
    "ep09": [  # T9 数值计算·高性能计算
        ("Richard Hamming", "理查德·汉明", 1968, "1915–1998", "美国", "Bell Labs",
         "数值方法、纠错码（汉明码），信息论先驱。"),
        ("James H. Wilkinson", "詹姆斯·威尔金森", 1970, "1919–1986", "英国", "National Physical Laboratory",
         "数值分析、舍入误差分析，线性代数数值算法。"),
        ("William Kahan", "威廉·卡汉", 1989, "1933–", "加拿大/美国", "UC Berkeley",
         "IEEE 754 浮点标准，数值分析大师。"),
        ("Jack Dongarra", "杰克·唐加拉", 2021, "1950–", "美国", "University of Tennessee",
         "LINPACK/LAPACK、MPI，高性能计算奠基人。"),
    ],
    "ep10": [  # T10 图形学·人机交互
        ("Ivan Sutherland", "伊万·萨瑟兰", 1988, "1938–", "美国", "—",
         "Sketchpad 交互式图形系统，计算机图形学之父。"),
        ("Douglas Engelbart", "道格拉斯·恩格尔巴特", 1997, "1925–2013", "美国", "—",
         "鼠标发明者、超文本、图形交互（NLS）。"),
        ("Charles P. Thacker", "查尔斯·萨克", 2009, "1943–2017", "美国", "Microsoft Research",
         "Alto 个人电脑、以太网、平板显示。"),
        ("Edwin Catmull", "埃德温·卡特穆尔", 2019, "1945–", "美国", "Pixar",
         "计算机图形学、纹理映射、皮克斯联合创始人。"),
        ("Pat Hanrahan", "帕特·汉拉汉", 2019, "1955–", "美国", "Stanford University",
         "RenderMan 渲染系统、图形着色语言。"),
    ],
}

# 各集主题元信息: (ep_key, dir, main, title, subtitle, range, note)
EPISODES = [
    ("ep01", "episode-01-theory-computation", "turing_ep01_zh",
     "理论计算机科学", "计算复杂性 · 算法 · 随机性", "1966 – 2023", "从 Cook 到 Wigderson"),
    ("ep02", "episode-02-programming-languages", "turing_ep02_zh",
     "程序设计语言与软件方法学", "编译 · 语言 · 工程", "1966 – 2020", "从 Perlis 到 Ullman"),
    ("ep03", "episode-03-ai-ml", "turing_ep03_zh",
     "人工智能与机器学习", "AI 奠基 · 深度学习 · 强化学习", "1969 – 2024", "从 Minsky 到 Sutton"),
    ("ep04", "episode-04-os-architecture", "turing_ep04_zh",
     "操作系统与体系结构", "Unix · RISC · 编译器", "1967 – 2017", "从 Wilkes 到 Patterson"),
    ("ep05", "episode-05-database", "turing_ep05_zh",
     "数据库与数据管理", "关系模型 · 事务处理", "1973 – 2014", "从 Bachman 到 Stonebraker"),
    ("ep06", "episode-06-network-web", "turing_ep06_zh",
     "网络与万维网", "TCP/IP · 以太网 · WWW", "2004 – 2022", "从 Cerf 到 Metcalfe"),
    ("ep07", "episode-07-distributed-verification", "turing_ep07_zh",
     "分布式系统与形式验证", "并发 · 共识 · 模型检验", "1972 – 2013", "从 Dijkstra 到 Lamport"),
    ("ep08", "episode-08-crypto-security", "turing_ep08_zh",
     "密码学与量子信息", "公钥密码 · 零知识 · 量子密钥", "2000 – 2025", "从 Yao 到 Brassard"),
    ("ep09", "episode-09-numerical-hpc", "turing_ep09_zh",
     "数值计算与高性能计算", "浮点 · 纠错码 · HPC", "1968 – 2021", "从 Hamming 到 Dongarra"),
    ("ep10", "episode-10-graphics-hci", "turing_ep10_zh",
     "计算机图形学与人机交互", "图形 · 鼠标 · 可视化", "1988 – 2019", "从 Sutherland 到 Hanrahan"),
]

NAMES_BAR = {
    "ep01": "Cook · Karp · Hopcroft · Tarjan · Knuth · Rabin · Blum · Valiant · Wigderson · Hartmanis · Stearns",
    "ep02": "Perlis · Backus · Floyd · Hoare · Wirth · Milner · Brooks · Aho · Ullman · Scott · Dahl · Nygaard · Kay · Iverson · Naur",
    "ep03": "Minsky · McCarthy · Newell · Simon · Feigenbaum · Reddy · Pearl · Bengio · Hinton · LeCun · Barto · Sutton",
    "ep04": "Wilkes · Thompson · Ritchie · Cocke · Corbató · Allen · Hennessy · Patterson",
    "ep05": "Bachman · Codd · Gray · Stonebraker",
    "ep06": "Cerf · Kahn · Berners-Lee · Metcalfe",
    "ep07": "Dijkstra · Lampson · Pnueli · Clarke · Emerson · Sifakis · Lamport · Liskov",
    "ep08": "Yao · Rivest · Shamir · Adleman · Goldwasser · Micali · Diffie · Hellman · Bennett · Brassard",
    "ep09": "Hamming · Wilkinson · Kahan · Dongarra",
    "ep10": "Sutherland · Engelbart · Thacker · Catmull · Hanrahan",
}

# 主要荣誉（Turing 之外的重要交叉荣誉，来源：Wikipedia 本地页 infobox，2026-08 全量核实）
HONORS = {
    "Herbert A. Simon":   "诺贝尔经济学奖 1978；美国国家科学奖章 1986",
    "Donald Knuth":       "京都奖 1996；美国国家科学奖章 1979",
    "John McCarthy":      "京都奖 1988；美国国家科学奖章 1990",
    "Marvin Minsky":      "日本国际奖 1990；美国国家科学奖章",
    "Andrew Yao":         "京都奖 2021；美国国家科学奖章",
    "Richard Karp":       "京都奖 2008；美国国家科学奖章 1996；EATCS 奖 2000",
    "Tony Hoare":         "京都奖 2000",
    "Ivan Sutherland":    "京都奖；IEEE 冯诺依曼奖 1998",
    "Alan Kay":           "京都奖",
    "John Backus":        "美国国家科学奖章 1975",
    "Dennis Ritchie":     "日本国际奖 2011",
    "Ken Thompson":       "日本国际奖 2011；IEEE 冯诺依曼奖",
    "Vint Cerf":          "日本国际奖 2008；马可尼奖；美国国家科学奖章",
    "Ronald Rivest":      "马可尼奖 2007",
    "Adi Shamir":         "沃尔夫数学奖 2024；英国皇家学会院士 2018",
    "Charles H. Bennett": "沃尔夫物理学奖 2018；香农奖 2020",
    "Gilles Brassard":    "沃尔夫物理学奖 2018",
    "Leslie Valiant":     "内万林纳奖 1986；EATCS 奖 2008",
    "Judea Pearl":        "鲁梅哈特奖 2011；美国国家科学奖章 2014",
    "Geoffrey Hinton":    "日本国际奖 2016；诺贝尔物理学奖 2024；英国皇家学会院士",
    "Yann LeCun":         "美国国家科学奖章 2023；英国皇家学会院士",
    "Yoshua Bengio":      "加拿大总督奖；英国皇家学会院士",
    "Shafi Goldwasser":   "哥德尔奖 1993/2001；美国科学院院士",
    "Silvio Micali":      "哥德尔奖 1993；美国科学院院士",
    "Avi Wigderson":      "哥德尔奖 2009；阿贝尔奖 2021；内万林纳奖 1994",
    "Whitfield Diffie":   "马可尼奖 2000；IEEE 香农奖 2021",
    "Martin Hellman":     "马可尼奖 2000；IEEE 香农奖 2021",
    "Richard Hamming":    "IEEE 香农奖 1996",
    "William Kahan":      "美国国家科学奖章 1989",
    "Jack Dongarra":      "美国国家科学奖章 2020",
    "Barbara Liskov":     "美国国家科学奖章 2005",
    "Leslie Lamport":     "IEEE 冯诺依曼奖 2008；美国国家科学奖章",
    "Tim Berners-Lee":    "千禧科技奖 2004；英国皇家学会院士",
    "Robert Metcalfe":    "美国国家科学奖章 2003",
}

HEADER = r"""% Turing Award Video — Episode {EP}
% {TITLE}（{RANGE}）
% Beamer layout mirrors COPSS/Fields video series
% Source: turing/pages 离线页面 + turing_award_winners.md + Wikipedia
\documentclass[aspectratio=169,14pt]{beamer}
\usetheme{default}\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{\hfill{\scriptsize\color{covermuted}\insertframenumber/\inserttotalframenumber}\hspace{0.4cm}\vspace{0.15cm}}
\usepackage{fontspec}\usepackage{xeCJK}
\setCJKmainfont{PingFang SC}[BoldFont=PingFang SC Semibold]
\setmainfont{Helvetica Neue}[BoldFont=Helvetica Neue Bold]
\usepackage{xcolor}\usepackage{tikz}\usepackage{graphicx}\usepackage{adjustbox}\usepackage{fontawesome5}\usepackage{ifthen}\usepackage{amssymb}
\usetikzlibrary{positioning,calc,arrows.meta,shadows}

% ===== 配色：图灵紫 + 琥珀金 + 青绿（区别于菲尔兹金/阿贝尔蓝/陈省身青/COPSS统计蓝）=====
\definecolor{bgmain}{RGB}{247,245,251}
\definecolor{coverprimary}{HTML}{5B2D8E}
\definecolor{coveraccent}{HTML}{B03A2E}
\definecolor{coveramber}{HTML}{D9A441}
\definecolor{coverpurple}{HTML}{1E8E8E}
\definecolor{coverdark}{HTML}{241A33}
\definecolor{covermuted}{HTML}{6B6478}
\definecolor{coverlight}{HTML}{EFEAF7}
\definecolor{titlecolor}{RGB}{36,26,51}
\definecolor{muteddark}{RGB}{96,90,110}
\definecolor{bluepanel}{RGB}{231,222,245}
\definecolor{redpanel}{RGB}{250,227,225}
\definecolor{goldpanel}{RGB}{250,243,226}
\definecolor{purplepanel}{RGB}{224,237,237}
\definecolor{graypanel}{RGB}{240,238,244}
\setbeamercolor{background canvas}{bg=bgmain}

\providecommand{\personhonors}{}

% 交叉奖项徽标（参考 Fields/COPSS 系列）
% 用 \raisebox 而非 \textsuperscript：避免 22pt 标题触发 15.4pt 数学字体缺失警告
% 符号+字母+品牌色：◆N 诺贝尔 · ★K 京都 · ◇G 哥德尔 · ★A 阿贝尔 · ★S 香农
\newcommand{\nobelbadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\clubsuit$\kern-0.5pt N}}
\newcommand{\kyotobadge}{\raisebox{0.55ex}{\tiny\color{coverprimary}$\blacklozenge$\kern-0.5pt K}}
\newcommand{\godelbadge}{\raisebox{0.55ex}{\tiny\color{coverpurple}$\diamond$\kern-0.5pt G}}
\newcommand{\abelbadge}{\raisebox{0.55ex}{\tiny\color{coveraccent}$\bigstar$\kern-0.5pt A}}
\newcommand{\shannonbadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\bigstar$\kern-0.5pt S}}
% ★W 沃尔夫 · ♥J 日本国际 · ▲N 内万林纳 · □E EATCS · ●M 马可尼 · ▲V 冯·诺依曼 · ◆T 千禧科技
\newcommand{\wolfbadge}{\raisebox{0.55ex}{\tiny\color{coveramber!70!black}$\bigstar$\kern-0.5pt W}}
\newcommand{\japanbadge}{\raisebox{0.55ex}{\tiny\color{coveraccent}$\heartsuit$\kern-0.5pt J}}
\newcommand{\nevanlinnabadge}{\raisebox{0.55ex}{\tiny\color{coverpurple}$\blacktriangle$\kern-0.5pt N}}
\newcommand{\eatcsbadge}{\raisebox{0.55ex}{\tiny\color{coverdark}$\square$\kern-0.5pt E}}
\newcommand{\marconibadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\bullet$\kern-0.5pt M}}
\newcommand{\neumannbadge}{\raisebox{0.55ex}{\tiny\color{coverprimary}$\blacktriangle$\kern-0.5pt V}}
\newcommand{\millenniumbadge}{\raisebox{0.55ex}{\tiny\color{coveraccent}$\blacklozenge$\kern-0.5pt T}}
% ♠M 国家科学奖章 · ■N 美国科学院 · ✓R 皇家学会 · ◆C 加拿大总督 · ◇R 鲁梅哈特
\newcommand{\nsmbadge}{\raisebox{0.55ex}{\tiny\color{coverprimary}$\spadesuit$\kern-0.5pt M}}
\newcommand{\nasbadge}{\raisebox{0.55ex}{\tiny\color{coverpurple}$\blacksquare$\kern-0.5pt N}}
\newcommand{\frsbadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\checkmark$\kern-0.5pt R}}
\newcommand{\govbadge}{\raisebox{0.55ex}{\tiny\color{coverdark}$\blacklozenge$\kern-0.5pt C}}
\newcommand{\rumelhartbadge}{\raisebox{0.55ex}{\tiny\color{coverpurple}$\diamondsuit$\kern-0.5pt R}}

\newcommand{\plainbar}{%
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverdark, opacity=0.06] (current page.south west) rectangle ([yshift=0.4cm]current page.south east);
  \draw[coverprimary, opacity=0.40, line width=0.8pt] ([yshift=0.4cm]current page.south west) -- ([yshift=0.4cm]current page.south east);
\end{tikzpicture}%
}

% 底部交叉荣誉边框：#1 = 图标串（\godelbadge 哥德尔奖 2009 ...）
\newcommand{\honorbar}[1]{%
  \begin{tikzpicture}[remember picture, overlay]
    \node[anchor=south, draw=coverprimary!55, fill=coverlight, rounded corners=6pt,
          inner xsep=8pt, inner ysep=5pt, yshift=0.65cm, text=coverdark!85] at (current page.south) {%
      \fontsize{7.5}{9.5}\selectfont\bfseries{\color{coverprimary} 其他殊荣}\enspace #1};
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

% ---- Person slide: #1 name #2 subtitle #3 img/none #4 credit/缩写 #5 获奖(年+岁) #6 life #7 country #8 inst #9 contribution ----
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
\begin{column}{0.20\textwidth}
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
\begin{column}{0.40\textwidth}
  \begin{tikzpicture}
    \node[fill=goldpanel, rounded corners=4pt, inner xsep=6pt, inner ysep=5pt, text width=4.0cm, align=left] {
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 获奖}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #5}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 生卒}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #6}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 国别}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #7}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 机构}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #8}
    };
  \end{tikzpicture}
\end{column}
\begin{column}{0.38\textwidth}
  \begin{tikzpicture}
    \node[draw=coverprimary!35, fill=bluepanel, rounded corners=5pt, inner sep=7pt, text width=3.8cm, align=left] {
      {\fontsize{8.2}{10}\selectfont\bfseries\color{coverprimary!82!black} 核心贡献}\\[3pt]
      {\fontsize{7}{8.5}\selectfont\color{coverdark!84} #9}
    };
  \end{tikzpicture}
\end{column}
\end{columns}
\if\relax\detokenize\expandafter{\personhonors}\relax\else\honorbar{\personhonors}\fi
\end{frame}
}
"""


def esc(s):
    return str(s).replace("&", "\\&")


def cmd_name(name):
    s = name.replace(".", "").replace("-", "").replace("(", "").replace(")", "").replace(" ", "").replace("'", "")
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return s.lower()


def compute_age(year, life):
    m = re.search(r'(19|20)\d{2}(?:/(19|20)\d{2})?', life.replace("–", "-"))
    if not m:
        return None
    part = m.group(0)
    if "/" in part:
        y1, y2 = part.split("/")
        lo, hi = min(year - int(y1), year - int(y2)), max(year - int(y1), year - int(y2))
        return "%d/%d岁" % (lo, hi) if lo != hi else "%d岁" % lo
    return "%d岁" % (year - int(part))


# 奖项 → (徽标命令, 显示名)
AWARD_ICONS = [
    ("诺贝尔", r"\nobelbadge", "诺贝尔奖"),
    ("京都", r"\kyotobadge", "京都奖"),
    ("沃尔夫", r"\wolfbadge", "沃尔夫奖"),
    ("哥德尔", r"\godelbadge", "哥德尔奖"),
    ("阿贝尔", r"\abelbadge", "阿贝尔奖"),
    ("香农", r"\shannonbadge", "香农奖"),
    ("日本国际", r"\japanbadge", "日本国际奖"),
    ("内万林纳", r"\nevanlinnabadge", "内万林纳奖"),
    ("EATCS", r"\eatcsbadge", "EATCS 奖"),
    ("马可尼", r"\marconibadge", "马可尼奖"),
    ("冯", r"\neumannbadge", "冯·诺依曼奖"),
    ("千禧", r"\millenniumbadge", "千禧科技奖"),
    ("国家科学奖章", r"\nsmbadge", "国家科学奖章"),
    ("科学院院士", r"\nasbadge", "美国科学院院士"),
    ("皇家学会院士", r"\frsbadge", "皇家学会院士"),
    ("加拿大总督", r"\govbadge", "加拿大总督奖"),
    ("鲁梅哈特", r"\rumelhartbadge", "鲁梅哈特奖"),
]


def badges_for(name):
    h = HONORS.get(name, "")
    b = ""
    for key, cmd, _label in AWARD_ICONS:
        if key in h:
            b += cmd
    return b


def honor_icons_for(name):
    """Bottom honor-bar icons: e.g. \\godelbadge 哥德尔奖 2009 \\enspace \\abelbadge 阿贝尔奖 2021"""
    h = HONORS.get(name, "")
    if not h:
        return ""
    parts = []
    for key, cmd, label in AWARD_ICONS:
        if key in h:
            # extract year(s) right after the keyword within the same '；' chunk
            year = ""
            for chunk in h.split("；"):
                if key in chunk:
                    m = re.search(r'(19|20)\d{2}(?:\s*/\s*(19|20)\d{2})?', chunk)
                    if m:
                        year = " " + m.group(0)
                    break
            parts.append("%s %s%s" % (cmd, label, year))
    return " \\enspace ".join(parts)


def find_portrait(name, year):
    """Try to find a real portrait in turing/pages/<year>/<dir>/images/."""
    year_dir = os.path.join(PAGES, str(year))
    if not os.path.isdir(year_dir):
        return None
    for sub in os.listdir(year_dir):
        img_dir = os.path.join(year_dir, sub, "images")
        if not os.path.isdir(img_dir):
            continue
        cands = []
        for f in os.listdir(img_dir):
            if not f.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            low = f.lower()
            if any(k in low for k in ("question_book", "flag_", "map_", "icon", "logo", "seal", "commons")):
                continue
            p = os.path.join(img_dir, f)
            try:
                sz = os.path.getsize(p)
            except OSError:
                sz = 0
            cands.append((sz, p))
        if cands:
            cands.sort(reverse=True)
            return cands[0][1]
    return None


FIGURES_DIR = os.path.join(HERE, "video", "episode-allinone", "figures")


def fig_key(fname):
    """Normalize a figures/ filename (e.g. 'Donald Knuth.jpeg', 'john_hopcroft.jpg')
    to the same lowercase key used by cmd_name()."""
    s = os.path.splitext(fname)[0]
    s = s.replace("_", " ")
    return cmd_name(s)


def find_figure(name):
    """Look for a manually calibrated portrait in episode-allinone/figures/."""
    if not os.path.isdir(FIGURES_DIR):
        return None
    key = cmd_name(name)
    for f in os.listdir(FIGURES_DIR):
        if f.startswith("."):
            continue
        if fig_key(f) == key:
            return os.path.join(FIGURES_DIR, f)
    return None


def copy_figure(src, dst):
    """Copy figures/ portrait to dst .jpg, converting webp if needed."""
    if src.lower().endswith(".webp"):
        try:
            from PIL import Image
            Image.open(src).convert("RGB").save(dst, "JPEG", quality=95)
            return
        except Exception:
            pass
    shutil.copy(src, dst)


def sync_photos(people, ep_dir):
    img_dir = os.path.join(HERE, "video", ep_dir, "images")
    os.makedirs(img_dir, exist_ok=True)
    for name, _cn, year, _life, _c, _i, _contrib in people:
        dst = os.path.join(img_dir, cmd_name(name) + ".jpg")
        # figures/ takes absolute priority: always force-overwrite
        fig = find_figure(name)
        if fig:
            copy_figure(fig, dst)
            continue
        # not in figures/: keep existing calibrated/current portrait; only fill missing
        if os.path.exists(dst) and os.path.getsize(dst) > 0:
            continue
        src = find_portrait(name, year)
        if src and os.path.exists(src):
            shutil.copy(src, dst)
        else:
            open(dst, "a").close()  # empty placeholder
    return len(people)


def initials(name):
    parts = [p for p in name.replace("-", " ").split() if p]
    if len(parts) >= 2:
        return "%s.%s." % (parts[0][0], parts[-1][0])
    return parts[0][:2].upper() + "."


def _honor_block(name):
    """Format HONORS as a multi-line block, each '；'-separated honor on its own line."""
    if name not in HONORS:
        return ""
    items = [esc(h).strip() for h in HONORS[name].split("；") if h.strip()]
    return "\\\\\\textbf{主要荣誉}\\\\" + " \\\\ ".join(items)


def person_slide(p, prefix="", ep_dir=""):
    name, cn, year, life, country, inst, contrib = p
    body = esc(contrib)
    body += _honor_block(name)
    cname = prefix + cmd_name(name)
    age = compute_age(year, life)
    year_str = "%d（%s）" % (year, age) if age else str(year)
    img_path = os.path.join(HERE, "video", ep_dir, "images", cmd_name(name) + ".jpg")
    if os.path.exists(img_path) and os.path.getsize(img_path) > 0:
        img, credit = "images/%s.jpg" % cmd_name(name), "Wikipedia"
    else:
        img, credit = "none", initials(name)
    honors = honor_icons_for(name)
    return ("\\newcommand{\\%sslide}{\\gdef\\personhonors{%s}\\personslide\n"
            "  {%s}{%s}\n"
            "  {%s}{%s}\n"
            "  {%s}{%s}{%s}{%s}\n"
            "  {%s}}\n" % (
                cname, honors,
                esc(name) + badges_for(name), esc(cn), img, credit, year_str,
                esc(life), esc(country), esc(inst), body))


def grid_dims(n):
    if n <= 6:
        return 3, 2, 1.50, 1.80, 0.14
    if n <= 10:
        return 5, 2, 1.35, 1.65, 0.14
    if n <= 15:
        return 6, 3, 1.25, 1.50, 0.12
    return 17, 5, 0.50, 0.60, 0.04


def make_cover_slide(people, title, sub, note, foot, ep_dir, cover_name="coverslide"):
    N_COLS, N_ROWS, W, H, GAP = grid_dims(len(people))
    TOTAL_H = (N_ROWS - 1) * (H + GAP)
    START_X = -((N_COLS - 1) * (W + GAP)) / 2
    START_Y = TOTAL_H / 2
    if len(people) <= 10:
        center_y, note_y = -0.30, None
        badge_y = None
    elif len(people) <= 15:
        center_y = -1.50
    else:
        # large grid (e.g. allinone 81): place below note line at yshift=0.10cm
        center_y = -1.80
    grid = ['  \\node[anchor=center] at ([yshift=%.2fcm]current page.center) {' % center_y,
            r'    \begin{tikzpicture}[scale=1]']
    for i, p in enumerate(people):
        name, *_ = p
        r, c = i // N_COLS, i % N_COLS
        x = START_X + c * (W + GAP)
        y = START_Y - r * (H + GAP)
        img_path = os.path.join(HERE, "video", ep_dir, "images", cmd_name(name) + ".jpg")
        if os.path.exists(img_path) and os.path.getsize(img_path) > 0:
            grid.append('      \\node[inner sep=0pt, draw=coverprimary!22, line width=0.2pt] at (%.2f,%.2f) {'
                        '\\includegraphics[width=%scm,height=%scm,keepaspectratio]{images/%s.jpg}};'
                        % (x, y, W, H, cmd_name(name)))
        else:
            grid.append('      \\node[circle, fill=coverprimary!8, draw=coverprimary!30, '
                        'minimum size=%scm, inner sep=0pt] at (%.2f,%.2f) {'
                        '\\fontsize{5}{6}\\selectfont\\color{covermuted} %s};'
                        % (min(W, H) * 0.9, x, y, initials(name)))
    grid.append(r'    \end{tikzpicture}')
    grid.append(r'  };')
    grid_tikz = '\n'.join(grid)
    return (r'''\newcommand{\coverslide}{%%
\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverprimary!6] (current page.north west) rectangle (current page.south east);
  \fill[coveraccent!10] (current page.south east) ++(-2.3,-1.7) circle (2.0cm);
  \fill[coveramber!14] (current page.north east) ++(-2.4,1.4) circle (1.2cm);
  \fill[coverpurple!10] (current page.north west) ++(3.0,-1.0) circle (0.9cm);
  \node[anchor=center, font=\fontsize{17}{22}\selectfont\bfseries, text=coverdark]
    at ([yshift=2.60cm]current page.center) {%s};
  \node[anchor=center, font=\fontsize{12}{15}\selectfont, text=coverprimary!85!black]
    at ([yshift=1.55cm]current page.center) {%s};
  \draw[coverprimary, line width=1.4pt] ([yshift=0.75cm, xshift=-5.2cm]current page.center)
    -- ([yshift=0.75cm, xshift=5.2cm]current page.center);
  \node[anchor=center, font=\fontsize{9.5}{12.5}\selectfont\bfseries, text=coveramber!58!black]
    at ([yshift=0.10cm]current page.center) {%s};
''' % (title, sub, note)) + grid_tikz + (r'''
  \node[anchor=south, font=\scriptsize, text=coverdark!40]
    at ([yshift=0.38cm]current page.south) {\faIcon{medal}\enspace ACM Turing Award\enspace|\enspace %s};
\end{tikzpicture}
\end{frame}
}''' % foot)


def synthesis_slide(ep_key, title, sub, summary):
    people = DATA[ep_key]
    cols = [("bluepanel", "coverprimary!35", "coverprimary!85!black"),
            ("goldpanel", "coveramber!35", "coveramber!85!black"),
            ("purplepanel", "coverpurple!35", "coverpurple!85!black"),
            ("redpanel", "coveraccent!35", "coveraccent!85!black")]
    xs = [-5.0, -2.5, 0.0, 2.5, 5.0]
    rows = []
    for i, p in enumerate(people):
        name, _cn, year, *_ = p
        col = cols[i % 4]
        x = xs[i % 5]
        y = 1.75 - (i // 5) * 1.5
        rows.append("  \\node[chip, fill=%s, draw=%s, text=%s] at (%s,%.2f) {\\textbf{%d}\\\\%s};" % (
            col[0], col[1], col[2], x, y, year, name.split()[-1]))
    chipblock = "\n".join(rows)
    return (r"""\newcommand{\synthesisslide}{%%
\begin{frame}
\plainbar
\sectiontitle{%s}{%s}
\begin{center}
\begin{tikzpicture}[
  chip/.style={rounded corners=4pt, inner xsep=4pt, inner ysep=3pt, text width=1.9cm, align=center, font=\fontsize{6}{7.2}\selectfont}
]
%s
\end{tikzpicture}
\end{center}
\vspace{0.12cm}
\begin{center}
\begin{tikzpicture}
  \node[draw=coverprimary!40, fill=bluepanel, rounded corners=5pt, inner sep=8pt, text width=13.4cm, align=center] at (0,0) {%%
    {\fontsize{8}{9.5}\selectfont\bfseries\color{coverdark!80} 本集综述}\par\vspace{3pt}
    {\fontsize{7.4}{8.8}\selectfont\color{coverdark!72} %s}
  };
\end{tikzpicture}
\end{center}
\end{frame}
}""" % (title, sub, chipblock, esc(summary)))


SYNTHESIS = {
    "ep01": ("理论之光：计算到底能算多快？", "P/NP 与随机性——计算复杂性的黄金时代",
             "从 Cook-Levin 定理到 Wigderson 的去随机化，这一代数学家严格回答了「什么问题算得快、什么问题不可能」。"),
    "ep02": ("语言与程序：人如何指挥机器", "编程语言与软件方法学——从 Fortran 到《龙书》",
             "Fortran、Algol、Pascal、ML、Smalltalk——每一种语言都是一次抽象革命；《龙书》与《人月神话》定义了编译与工程。"),
    "ep03": ("机器的智能：从推理到学习", "人工智能与机器学习——从符号推理到深度学习",
             "从明斯基的框架到 Hinton 的反向传播再到 Sutton 的强化学习，AI 用六十年完成从模仿思维到自动学习的跃迁。"),
    "ep04": ("系统之心：让机器跑起来", "操作系统与体系结构——Unix、RISC 与编译器",
             "Unix 与 C 塑造了现代软件；RISC 与编译器优化决定了硬件性能的每一次跃升。"),
    "ep05": ("数据的秩序：关系模型到数据库", "数据库——从 CODASYL 到 PostgreSQL",
             "Codd 的关系模型把数据变成数学；Gray 的事务处理让银行系统可信；Stonebraker 把数据库带入流时代。"),
    "ep06": ("连接世界：TCP/IP 与万维网", "网络——从以太网到 WWW",
             "TCP/IP 让全球计算机互联，WWW 让全人类共享信息——他们发明了今天的数字世界。"),
    "ep07": ("并发的秩序：分布式与验证", "分布式系统与形式验证——共识、时态逻辑与模型检验",
             "Dijkstra 的并发原语、Lamport 的 Paxos、Clarke 的模型检验——让复杂系统在并发中依然可信。"),
    "ep08": ("秘密与量子：密码学的新世纪", "密码学——从 RSA 到量子密钥分发",
             "RSA 与公钥密码守护互联网，零知识证明守护隐私，BB84 用量子物理守护未来。"),
    "ep09": ("数字的精度：数值与高性能计算", "数值计算——从汉明码到 LINPACK",
             "汉明码守护数字通信，IEEE 754 定义浮点世界，Dongarra 让超级计算机跑得更快。"),
    "ep10": ("看见与触摸：图形与人机交互", "计算机图形学——从 Sketchpad 到 RenderMan",
             "Sutherland 的画笔、Engelbart 的鼠标、Catmull 的皮克斯——让人类与机器温柔对话。"),
}


def make_episode_tex(ep_key, ep_dir, main, title, subtitle, rng, note):
    people = DATA[ep_key]
    out = [HEADER.replace("{EP}", ep_key[-1]).replace("{TITLE}", title).replace("{RANGE}", rng)]
    out.append(make_cover_slide(
        people, "ACM 图灵奖 · %s（%s）" % (title, rng.replace(" – ", "–")),
        "ACM Turing Award · %d 位得主" % len(people),
        "%s · %s" % (subtitle, note), rng.replace(" ", "") + " · %d 位得主" % len(people),
        ep_dir))
    out.append("\n% ========== SLIDES ==========\n")
    for p in people:
        out.append(person_slide(p, ep_dir=ep_dir))
    out.append(synthesis_slide(ep_key, *SYNTHESIS[ep_key]))
    names = [cmd_name(p[0]) for p in people]
    body = "\n".join("\\%sslide" % n for n in names)
    out.append("\n% ========== MAIN ==========\n\\begin{document}\n")
    out.append("\\coverslide\n")
    out.append(body + "\n")
    out.append("\\synthesisslide\n")
    out.append("\\end{document}\n")
    path = os.path.join(HERE, "video", ep_dir, main + ".tex")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("wrote", path)


MAKEFILE_TEMPLATE = r"""# Makefile for Turing video episode.
MAIN        = {MAIN}
VIDEO_NAME  = {MAIN}
OUTPUT_DIR  = output
IMAGES_DIR  = $(OUTPUT_DIR)/images
SLIDES_TXT  = $(OUTPUT_DIR)/slides.txt
DURATION    = 7
BGM         = $(wildcard *.wav)
LATEXMK     = latexmk
PDFTOPPM    = pdftoppm
FFMPEG      = ffmpeg
PYTHON      = python3

.PHONY: all pdf images video clean distclean
all: pdf

pdf: $(MAIN).pdf
$(MAIN).pdf: $(MAIN).tex
	$(LATEXMK) -xelatex -synctex=0 -interaction=nonstopmode $(MAIN).tex || \
	  (rm -f $(MAIN).fdb_latexmk && $(LATEXMK) -xelatex -synctex=0 -interaction=nonstopmode -f $(MAIN).tex)
	$(LATEXMK) -c $(MAIN).tex

images: $(IMAGES_DIR)/.done
$(IMAGES_DIR)/.done: $(MAIN).pdf
	@mkdir -p $(IMAGES_DIR)
	$(PDFTOPPM) -png -r 600 $(MAIN).pdf $(IMAGES_DIR)/slide
	@cd $(IMAGES_DIR) && for f in slide-*.png; do mv "$$f" "$$(echo $$f | sed 's/-/_/')"; done 2>/dev/null || true
	@touch $@

$(SLIDES_TXT): $(IMAGES_DIR)/.done
	@$(PYTHON) -c "\
	import os; \
	imgs = sorted([f for f in os.listdir('$(IMAGES_DIR)') if f.endswith('.png')]); \
	lines = []; \
	[lines.extend(['file 'images/' + f, 'duration $(DURATION)']) for f in imgs]; \
	lines.append('file 'images/' + imgs[-1]); \
	open('$(SLIDES_TXT)', 'w').write(chr(10).join(lines) + chr(10)); \
	print(f'  slides.txt: {len(imgs)} slides x $(DURATION)s = {len(imgs)*$(DURATION)}s')"

video: $(OUTPUT_DIR)/$(VIDEO_NAME).mp4
$(OUTPUT_DIR)/$(VIDEO_NAME).mp4: $(SLIDES_TXT)
	@mkdir -p $(OUTPUT_DIR)
	@rm -f $(OUTPUT_DIR)/$(VIDEO_NAME).tmp.mp4 $(OUTPUT_DIR)/$(VIDEO_NAME).mp4
ifeq ($(strip $(BGM)),)
	$(FFMPEG) -y -f concat -safe 0 -i $(SLIDES_TXT) \
	  -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -profile:v high -pix_fmt yuv420p \
	  -crf 15 -preset medium -r 24 $(OUTPUT_DIR)/$(VIDEO_NAME).tmp.mp4
else
	$(FFMPEG) -y -f concat -safe 0 -i $(SLIDES_TXT) -stream_loop -1 -i "$(firstword $(BGM))" \
	  -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -profile:v high -pix_fmt yuv420p \
	  -crf 15 -preset medium -r 24 -c:a aac -b:a 192k -shortest $(OUTPUT_DIR)/$(VIDEO_NAME).tmp.mp4
endif
	@mv $(OUTPUT_DIR)/$(VIDEO_NAME).tmp.mp4 $(OUTPUT_DIR)/$(VIDEO_NAME).mp4
	@cp $(OUTPUT_DIR)/$(VIDEO_NAME).mp4 $(VIDEO_NAME).mp4
	@echo "==== Done: $(VIDEO_NAME).mp4 ===="

clean:
	$(LATEXMK) -c $(MAIN).tex 2>/dev/null || true
	rm -f $(MAIN).{aux,log,toc,out,nav,snm,fls,fdb_latexmk,xdv}
	rm -f $(SLIDES_TXT) $(IMAGES_DIR)/.done c.log

distclean: clean
	rm -f $(MAIN).pdf
	rm -rf $(IMAGES_DIR)
	rm -f $(OUTPUT_DIR)/$(VIDEO_NAME).mp4 $(VIDEO_NAME).mp4
"""


def make_makefile(ep_dir, main):
    content = MAKEFILE_TEMPLATE.replace("{MAIN}", main)
    ep_mk = os.path.join(HERE, "video", ep_dir, "Makefile")
    os.makedirs(os.path.dirname(ep_mk), exist_ok=True)
    with open(ep_mk, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    make_makefile("episode-00-what-is-turing-award", "turing_ep00_zh")
    for ep_key, ep_dir, main, title, subtitle, rng, note in EPISODES:
        people = DATA[ep_key]
        sync_photos(people, ep_dir)
        make_episode_tex(ep_key, ep_dir, main, title, subtitle, rng, note)
        make_makefile(ep_dir, main)
    # allinone
    all_people = []
    for ep_key, *_ in EPISODES:
        all_people.extend(DATA[ep_key])
    sync_photos(all_people, "episode-allinone")
    make_allinone_tex(all_people)
    make_makefile("episode-allinone", "turing_allinone_zh")


def make_allinone_tex(all_people):
    ep_dir = "episode-allinone"
    main = "turing_allinone_zh"
    out = [HEADER.replace("{EP}", "allinone").replace("{TITLE}", "合集").replace("{RANGE}", "1966–2025")]
    out.append(make_cover_slide(
        all_people, "ACM 图灵奖：计算机科学的最高礼赞（1966–2025）",
        "ACM Turing Award（图灵奖）· 全 81 位得主",
        "从 Perlis 到 Brassard · 计算机界诺贝尔奖 · 兼获诺奖与阿贝尔奖的双料得主",
        "1966–2025 · 全 81 位得主", ep_dir, cover_name="coverslide"))
    out.append("\n% ========== SLIDES (sorted by year/edition) ==========\n")
    names = []
    # sort by award year (1966 → 2025); same-year keep stable by name
    ordered = sorted(all_people, key=lambda p: (p[2], p[0]))
    for p in ordered:
        cname = cmd_name(p[0])
        # person_slide with unique command name (allinone, names unique)
        out.append(person_slide_all(p, cname))
        names.append("\\%s" % cname)
    out.append("\n% ========== MAIN ==========\n\\begin{document}\n")
    out.append("\\coverslide\n")
    out.append("\n".join(names) + "\n")
    out.append("\\end{document}\n")
    path = os.path.join(HERE, "video", ep_dir, main + ".tex")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("wrote", path)




def person_slide_all(p, cname):
    name, cn, year, life, country, inst, contrib = p
    body = esc(contrib)
    body += _honor_block(name)
    age = compute_age(year, life)
    edition = year - 1965  # ACM Turing Award: 1966 = 1st edition
    # 届数加粗彩色（coveraccent 红）让数字醒目
    if age:
        year_str = "%d 年 · 第{\\bfseries\\color{coveraccent} %d} 届（%s）" % (year, edition, age)
    else:
        year_str = "%d 年 · 第{\\bfseries\\color{coveraccent} %d} 届" % (year, edition)
    img_path = os.path.join(HERE, "video", "episode-allinone", "images", cmd_name(name) + ".jpg")
    if os.path.exists(img_path) and os.path.getsize(img_path) > 0:
        img, credit = "images/%s.jpg" % cmd_name(name), "Wikipedia"
    else:
        img, credit = "none", initials(name)
    honors = honor_icons_for(name)
    return ("\\newcommand{\\%s}{\\gdef\\personhonors{%s}\\personslide\n"
            "  {%s}{%s}\n"
            "  {%s}{%s}\n"
            "  {%s}{%s}{%s}{%s}\n"
            "  {%s}}\n" % (
                cname, honors,
                esc(name) + badges_for(name), esc(cn),
                img, credit,
                year_str, esc(life), esc(country), esc(inst), body))


if __name__ == "__main__":
    main()
