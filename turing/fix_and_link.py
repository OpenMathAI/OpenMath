#!/usr/bin/env python3
"""Rebuild turing_award.md table with clean Wikipedia links."""
import re

BASE = "https://en.wikipedia.org/wiki/"
path = "/Users/ericksun/workspace/codebuddy/math/turing/turing_award.md"

# year -> [(name, wiki_page), ...]
LAUREATES = [
    (1966, [("Alan Perlis", "Alan_Perlis")]),
    (1967, [("Maurice Wilkes", "Maurice_Wilkes")]),
    (1968, [("Richard Hamming", "Richard_Hamming")]),
    (1969, [("Marvin Minsky", "Marvin_Minsky")]),
    (1970, [("James H. Wilkinson", "James_H._Wilkinson")]),
    (1971, [("John McCarthy", "John_McCarthy_(computer_scientist)")]),
    (1972, [("Edsger W. Dijkstra", "Edsger_W._Dijkstra")]),
    (1973, [("Charles Bachman", "Charles_Bachman")]),
    (1974, [("Donald Knuth", "Donald_Knuth")]),
    (1975, [("Allen Newell", "Allen_Newell"), ("Herbert A. Simon", "Herbert_A._Simon")]),
    (1976, [("Michael O. Rabin", "Michael_O._Rabin"), ("Dana Scott", "Dana_Scott")]),
    (1977, [("John Backus", "John_Backus")]),
    (1978, [("Robert W. Floyd", "Robert_W._Floyd")]),
    (1979, [("Kenneth E. Iverson", "Kenneth_E._Iverson")]),
    (1980, [("Tony Hoare", "Tony_Hoare")]),
    (1981, [("Edgar F. Codd", "Edgar_F._Codd")]),
    (1982, [("Stephen Cook", "Stephen_Cook")]),
    (1983, [("Dennis Ritchie", "Dennis_Ritchie"), ("Ken Thompson", "Ken_Thompson")]),
    (1984, [("Niklaus Wirth", "Niklaus_Wirth")]),
    (1985, [("Richard M. Karp", "Richard_M._Karp")]),
    (1986, [("John Hopcroft", "John_Hopcroft"), ("Robert Tarjan", "Robert_Tarjan")]),
    (1987, [("John Cocke", "John_Cocke_(computer_scientist)")]),
    (1988, [("Ivan Sutherland", "Ivan_Sutherland")]),
    (1989, [("William Kahan", "William_Kahan")]),
    (1990, [("Fernando J. Corbató", "Fernando_J._Corbat%C3%B3")]),
    (1991, [("Robin Milner", "Robin_Milner")]),
    (1992, [("Butler Lampson", "Butler_Lampson")]),
    (1993, [("Juris Hartmanis", "Juris_Hartmanis"), ("Richard E. Stearns", "Richard_E._Stearns")]),
    (1994, [("Edward Feigenbaum", "Edward_Feigenbaum"), ("Raj Reddy", "Raj_Reddy")]),
    (1995, [("Manuel Blum", "Manuel_Blum")]),
    (1996, [("Amir Pnueli", "Amir_Pnueli")]),
    (1997, [("Douglas Engelbart", "Douglas_Engelbart")]),
    (1998, [("Jim Gray", "Jim_Gray_(computer_scientist)")]),
    (1999, [("Fred Brooks", "Fred_Brooks")]),
    (2000, [("Andrew Yao", "Andrew_Yao")]),
    (2001, [("Ole-Johan Dahl", "Ole-Johan_Dahl"), ("Kristen Nygaard", "Kristen_Nygaard")]),
    (2002, [("Leonard Adleman", "Leonard_Adleman"), ("Ron Rivest", "Ron_Rivest"), ("Adi Shamir", "Adi_Shamir")]),
    (2003, [("Alan Kay", "Alan_Kay")]),
    (2004, [("Vint Cerf", "Vint_Cerf"), ("Robert Kahn", "Robert_Kahn_(computer_scientist)")]),
    (2005, [("Peter Naur", "Peter_Naur")]),
    (2006, [("Frances Allen", "Frances_Allen")]),
    (2007, [("Edmund M. Clarke", "Edmund_M._Clarke"), ("E. Allen Emerson", "E._Allen_Emerson"), ("Joseph Sifakis", "Joseph_Sifakis")]),
    (2008, [("Barbara Liskov", "Barbara_Liskov")]),
    (2009, [("Charles P. Thacker", "Charles_P._Thacker")]),
    (2010, [("Leslie Valiant", "Leslie_Valiant")]),
    (2011, [("Judea Pearl", "Judea_Pearl")]),
    (2012, [("Shafi Goldwasser", "Shafi_Goldwasser"), ("Silvio Micali", "Silvio_Micali")]),
    (2013, [("Leslie Lamport", "Leslie_Lamport")]),
    (2014, [("Michael Stonebraker", "Michael_Stonebraker")]),
    (2015, [("Whitfield Diffie", "Whitfield_Diffie"), ("Martin Hellman", "Martin_Hellman")]),
    (2016, [("Tim Berners-Lee", "Tim_Berners-Lee")]),
    (2017, [("John L. Hennessy", "John_L._Hennessy"), ("David Patterson", "David_Patterson_(computer_scientist)")]),
    (2018, [("Yoshua Bengio", "Yoshua_Bengio"), ("Geoffrey Hinton", "Geoffrey_Hinton"), ("Yann LeCun", "Yann_LeCun")]),
    (2019, [("Edwin Catmull", "Edwin_Catmull"), ("Pat Hanrahan", "Pat_Hanrahan")]),
    (2020, [("Alfred Aho", "Alfred_Aho"), ("Jeffrey Ullman", "Jeffrey_Ullman")]),
    (2021, [("Jack Dongarra", "Jack_Dongarra")]),
    (2022, [("Robert Metcalfe", "Robert_Metcalfe")]),
    (2023, [("Avi Wigderson", "Avi_Wigderson")]),
    (2024, [("Andrew Barto", "Andrew_Barto"), ("Richard S. Sutton", "Richard_S._Sutton")]),
    (2025, [("Charles H. Bennett", "Charles_H._Bennett_(computer_scientist)"), ("Gilles Brassard", "Gilles_Brassard")]),
]

# Chinese display names (from original md)
CHINESE = {
    "Alan Perlis": "艾伦·佩利斯", "Maurice Wilkes": "莫里斯·威尔克斯",
    "Richard Hamming": "理查德·哈明", "Marvin Minsky": "马文·明斯基",
    "James H. Wilkinson": "詹姆斯·威尔金森", "John McCarthy": "约翰·麦卡锡",
    "Edsger W. Dijkstra": "艾兹格·迪杰斯特拉", "Charles Bachman": "查尔斯·巴赫曼",
    "Donald Knuth": "高德纳", "Allen Newell": "艾伦·纽厄尔",
    "Herbert A. Simon": "赫伯特·西蒙", "Michael O. Rabin": "迈克尔·拉宾",
    "Dana Scott": "达纳·斯科特", "John Backus": "约翰·巴科斯",
    "Robert W. Floyd": "罗伯特·弗洛伊德", "Kenneth E. Iverson": "肯尼斯·艾佛森",
    "Tony Hoare": "托尼·霍尔", "Edgar F. Codd": "埃德加·科德",
    "Stephen Cook": "斯蒂芬·库克", "Dennis Ritchie": "丹尼斯·里奇",
    "Ken Thompson": "肯·汤普森", "Niklaus Wirth": "尼克劳斯·维尔特",
    "Richard M. Karp": "理查德·卡普", "John Hopcroft": "约翰·霍普克罗夫特",
    "Robert Tarjan": "罗伯特·塔扬", "John Cocke": "约翰·科克",
    "Ivan Sutherland": "伊凡·苏泽兰", "William Kahan": "威廉·卡亨",
    "Fernando J. Corbató": "费尔南多·科尔巴托", "Robin Milner": "罗宾·米尔纳",
    "Butler Lampson": "巴特勒·兰普森", "Juris Hartmanis": "尤里斯·哈特马尼斯",
    "Richard E. Stearns": "理查德·斯特恩斯", "Edward Feigenbaum": "爱德华·费根鲍姆",
    "Raj Reddy": "拉吉·雷迪", "Manuel Blum": "曼纽尔·布卢姆",
    "Amir Pnueli": "阿米尔·普努埃利", "Douglas Engelbart": "道格拉斯·恩格尔巴特",
    "Jim Gray": "吉姆·格雷", "Fred Brooks": "弗雷德·布鲁克斯",
    "Andrew Yao": "姚期智", "Ole-Johan Dahl": "奥利-约翰·达尔",
    "Kristen Nygaard": "克利斯登·奈加特", "Leonard Adleman": "阿德曼",
    "Ron Rivest": "里维斯特", "Adi Shamir": "萨米尔", "Alan Kay": "艾伦·凯",
    "Vint Cerf": "文特·瑟夫", "Robert Kahn": "罗伯特·卡恩",
    "Peter Naur": "彼得·诺尔", "Frances Allen": "弗朗西丝·艾伦",
    "Edmund M. Clarke": "克拉克", "E. Allen Emerson": "埃默森",
    "Joseph Sifakis": "西法基斯", "Barbara Liskov": "芭芭拉·利斯科夫",
    "Charles P. Thacker": "查尔斯·萨克", "Leslie Valiant": "莱斯利·瓦利安特",
    "Judea Pearl": "朱迪亚·珀尔", "Shafi Goldwasser": "莎菲·戈德瓦塞尔",
    "Silvio Micali": "西尔维奥·米卡利", "Leslie Lamport": "莱斯利·兰波特",
    "Michael Stonebraker": "迈克尔·斯通布雷克", "Whitfield Diffie": "惠特菲尔德·迪菲",
    "Martin Hellman": "马丁·赫尔曼", "Tim Berners-Lee": "蒂姆·伯纳斯-李",
    "John L. Hennessy": "约翰·轩尼诗", "David Patterson": "大卫·帕特森",
    "Yoshua Bengio": "本吉奥", "Geoffrey Hinton": "辛顿", "Yann LeCun": "杨立昆",
    "Edwin Catmull": "埃德温·卡特姆尔", "Pat Hanrahan": "帕特·汉拉汉",
    "Alfred Aho": "阿尔佛雷德·阿霍", "Jeffrey Ullman": "杰弗里·乌尔曼",
    "Jack Dongarra": "杰克·东加拉", "Robert Metcalfe": "罗伯特·梅特卡夫",
    "Avi Wigderson": "阿维·维格森", "Andrew Barto": "安德鲁·巴托",
    "Richard S. Sutton": "理查德·萨顿", "Charles H. Bennett": "查尔斯·贝内特",
    "Gilles Brassard": "吉勒·布拉萨",
}

# Contribution text per year
CONTRIB = {
    1966: "高级编程技术与编译器构造",
    1967: "EDSAC 设计者，程序库先驱",
    1968: "数值方法、自动编码、检错纠错码",
    1969: "人工智能的奠基性工作",
    1970: "数值分析、线性代数、后向误差分析",
    1971: "人工智能研究，LISP 语言之父",
    1972: "将编程确立为一门智力学科；正确程序设计",
    1973: "数据库技术",
    1974: "算法分析、编程语言设计、《计算机程序设计艺术》",
    1975: "人工智能、人类认知、表处理",
    1976: "非确定性机器 / 有限自动机理论",
    1977: "高级编程系统，尤其是 FORTRAN",
    1978: "语法分析、语义、程序验证、算法分析",
    1979: "编程语言与记号，APL 语言创造者",
    1980: "编程语言的定义与设计",
    1981: "数据库管理系统的理论与实践（关系模型）",
    1982: "计算复杂性；创立 NP 完全性理论",
    1983: "操作系统理论与 UNIX 系统",
    1984: "创新语言：EULER、ALGOL-W、MODULA、PASCAL",
    1985: "算法理论、网络流、NP 完全性",
    1986: "算法与数据结构的设计与分析",
    1987: "编译器设计与理论、RISC 架构、优化编译器",
    1988: "计算机图形学，从 Sketchpad 开始",
    1989: "数值分析与浮点计算（IEEE 754）",
    1990: "分时系统 CTSS 与 Multics",
    1991: "LCF、ML 语言、通信系统演算",
    1992: "分布式与个人计算环境",
    1993: "计算复杂性理论基础",
    1994: "大规模人工智能系统",
    1995: "复杂性理论基础、密码学、程序检查",
    1996: "计算中的时序逻辑；程序与系统验证",
    1997: "交互式计算的构想与关键使能技术（鼠标）",
    1998: "数据库与事务处理研究",
    1999: "计算机架构、操作系统、软件工程",
    2000: "计算理论、伪随机性、密码学、通信复杂性",
    2001: "通过 Simula 实现面向对象编程",
    2002: "实用公钥密码学（RSA）",
    2003: "面向对象编程、Smalltalk、个人计算",
    2004: "网络互联与 TCP/IP 协议",
    2005: "编程语言设计与 ALGOL 60",
    2006: "优化编译技术与自动并行执行；首位女性得主",
    2007: "模型检验作为验证技术",
    2008: "数据抽象、容错、分布式计算",
    2009: "首台现代 PC（Xerox Alto）、以太网、局域网贡献",
    2010: "计算理论、PAC 学习、并行/分布式计算",
    2011: "人工智能中的概率与因果推理",
    2012: "密码学的复杂性理论基础",
    2013: "分布式与并发系统的理论与实践",
    2014: "现代数据库系统的概念与实践",
    2015: "公钥密码学与密钥交换",
    2016: "发明万维网及其基础协议",
    2017: "计算机架构设计的定量方法",
    2018: "深度神经网络",
    2019: "三维计算机图形学与电影 CGI",
    2020: "算法与编程语言实现理论",
    2021: "高性能计算的数值算法与库",
    2022: "以太网的发明、标准化与商业化",
    2023: "计算理论，尤其是随机性的作用",
    2024: "强化学习的概念与算法基础",
    2025: "点燃并塑造计算与信息技术的量子革命（量子信息科学、量子密码 BB84）",
}

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the table section
table_start = None
table_end = None
for i, line in enumerate(lines):
    if line.strip() == '| 年份 | 得主 | 贡献领域 |':
        table_start = i
    elif table_start is not None and i > table_start and line.strip().startswith('|') and '|---|' not in line:
        table_end = i
    elif table_end is not None and not line.strip().startswith('|'):
        break

# Remove old table rows (keep header and separator)
table_end += 1  # Last table line + 1
new_rows = [lines[table_start], lines[table_start + 1]]  # header + separator

for year, people in LAUREATES:
    contrib = CONTRIB.get(year, "")
    # Build name cell: combine linked names + Chinese
    parts = []
    cn_parts = []
    for name, page in people:
        parts.append(f"[{name}]({BASE}{page})")
        cn_parts.append(CHINESE.get(name, name))
    
    separator = " & " if len(people) == 2 else (", " if len(people) > 2 else "")
    # For 3 people with mix of , and &: use , for all but last which uses &
    if len(people) == 3:
        name_part = parts[0] + ", " + parts[1] + " & " + parts[2]
    else:
        name_part = separator.join(parts)
    
    name_cell = f"{name_part}（{'、'.join(cn_parts)}）"
    new_rows.append(f"| {year} | {name_cell} | {contrib} |\n")

# Replace old table with new
result = lines[:table_start] + new_rows + lines[table_end:]
with open(path, 'w', encoding='utf-8') as f:
    f.writelines(result)

print("Done! Table fully rebuilt with clean Wikipedia links.")