#!/usr/bin/env python3
"""Add Wikipedia links to turing_award.md laureate table."""

BASE_URL = "https://en.wikipedia.org/wiki/"

# Each entry: (exact_text_in_table_cell, [wiki_page_titles...])
ENTRIES = [
    ("Alan Perlis（艾伦·佩利斯）", ["Alan_Perlis"]),
    ("Maurice Wilkes（莫里斯·威尔克斯）", ["Maurice_Wilkes"]),
    ("Richard Hamming（理查德·哈明）", ["Richard_Hamming"]),
    ("Marvin Minsky（马文·明斯基）", ["Marvin_Minsky"]),
    ("James H. Wilkinson（詹姆斯·威尔金森）", ["James_H._Wilkinson"]),
    ("John McCarthy（约翰·麦卡锡）", ["John_McCarthy_(computer_scientist)"]),
    ("Edsger W. Dijkstra（艾兹格·迪杰斯特拉）", ["Edsger_W._Dijkstra"]),
    ("Charles Bachman（查尔斯·巴赫曼）", ["Charles_Bachman"]),
    ("Donald Knuth（高德纳）", ["Donald_Knuth"]),
    ("Allen Newell & Herbert A. Simon（艾伦·纽厄尔、赫伯特·西蒙）", ["Allen_Newell", "Herbert_A._Simon"]),
    ("Michael O. Rabin & Dana Scott（迈克尔·拉宾、达纳·斯科特）", ["Michael_O._Rabin", "Dana_Scott"]),
    ("John Backus（约翰·巴科斯）", ["John_Backus"]),
    ("Robert W. Floyd（罗伯特·弗洛伊德）", ["Robert_W._Floyd"]),
    ("Kenneth E. Iverson（肯尼斯·艾佛森）", ["Kenneth_E._Iverson"]),
    ("Tony Hoare（托尼·霍尔）", ["Tony_Hoare"]),
    ("Edgar F. Codd（埃德加·科德）", ["Edgar_F._Codd"]),
    ("Stephen Cook（斯蒂芬·库克）", ["Stephen_Cook"]),
    ("Dennis Ritchie & Ken Thompson（丹尼斯·里奇、肯·汤普森）", ["Dennis_Ritchie", "Ken_Thompson"]),
    ("Niklaus Wirth（尼克劳斯·维尔特）", ["Niklaus_Wirth"]),
    ("Richard M. Karp（理查德·卡普）", ["Richard_M._Karp"]),
    ("John Hopcroft & Robert Tarjan（约翰·霍普克罗夫特、罗伯特·塔扬）", ["John_Hopcroft", "Robert_Tarjan"]),
    ("John Cocke（约翰·科克）", ["John_Cocke_(computer_scientist)"]),
    ("Ivan Sutherland（伊凡·苏泽兰）", ["Ivan_Sutherland"]),
    ("William Kahan（威廉·卡亨）", ["William_Kahan"]),
    ("Fernando J. Corbató（费尔南多·科尔巴托）", ["Fernando_J._Corbat%C3%B3"]),
    ("Robin Milner（罗宾·米尔纳）", ["Robin_Milner"]),
    ("Butler Lampson（巴特勒·兰普森）", ["Butler_Lampson"]),
    ("Juris Hartmanis & Richard E. Stearns（尤里斯·哈特马尼斯、理查德·斯特恩斯）", ["Juris_Hartmanis", "Richard_E._Stearns"]),
    ("Edward Feigenbaum & Raj Reddy（爱德华·费根鲍姆、拉吉·雷迪）", ["Edward_Feigenbaum", "Raj_Reddy"]),
    ("Manuel Blum（曼纽尔·布卢姆）", ["Manuel_Blum"]),
    ("Amir Pnueli（阿米尔·普努埃利）", ["Amir_Pnueli"]),
    ("Douglas Engelbart（道格拉斯·恩格尔巴特）", ["Douglas_Engelbart"]),
    ("Jim Gray（吉姆·格雷）", ["Jim_Gray_(computer_scientist)"]),
    ("Fred Brooks（弗雷德·布鲁克斯）", ["Fred_Brooks"]),
    ("Andrew Yao（姚期智）", ["Andrew_Yao"]),
    ("Ole-Johan Dahl & Kristen Nygaard（奥利-约翰·达尔、克利斯登·奈加特）", ["Ole-Johan_Dahl", "Kristen_Nygaard"]),
    ("Leonard Adleman, Ron Rivest & Adi Shamir（阿德曼、里维斯特、萨米尔）", ["Leonard_Adleman", "Ron_Rivest", "Adi_Shamir"]),
    ("Alan Kay（艾伦·凯）", ["Alan_Kay"]),
    ("Vint Cerf & Robert Kahn（文特·瑟夫、罗伯特·卡恩）", ["Vint_Cerf", "Robert_Kahn_(computer_scientist)"]),
    ("Peter Naur（彼得·诺尔）", ["Peter_Naur"]),
    ("Frances Allen（弗朗西丝·艾伦）", ["Frances_Allen"]),
    ("Edmund M. Clarke, E. Allen Emerson & Joseph Sifakis（克拉克、埃默森、西法基斯）", ["Edmund_M._Clarke", "E._Allen_Emerson", "Joseph_Sifakis"]),
    ("Barbara Liskov（芭芭拉·利斯科夫）", ["Barbara_Liskov"]),
    ("Charles P. Thacker（查尔斯·萨克）", ["Charles_P._Thacker"]),
    ("Leslie Valiant（莱斯利·瓦利安特）", ["Leslie_Valiant"]),
    ("Judea Pearl（朱迪亚·珀尔）", ["Judea_Pearl"]),
    ("Shafi Goldwasser & Silvio Micali（莎菲·戈德瓦塞尔、西尔维奥·米卡利）", ["Shafi_Goldwasser", "Silvio_Micali"]),
    ("Leslie Lamport（莱斯利·兰波特）", ["Leslie_Lamport"]),
    ("Michael Stonebraker（迈克尔·斯通布雷克）", ["Michael_Stonebraker"]),
    ("Whitfield Diffie & Martin Hellman（惠特菲尔德·迪菲、马丁·赫尔曼）", ["Whitfield_Diffie", "Martin_Hellman"]),
    ("Tim Berners-Lee（蒂姆·伯纳斯-李）", ["Tim_Berners-Lee"]),
    ("John L. Hennessy & David Patterson（约翰·轩尼诗、大卫·帕特森）", ["John_L._Hennessy", "David_Patterson_(computer_scientist)"]),
    ("Yoshua Bengio, Geoffrey Hinton & Yann LeCun（本吉奥、辛顿、杨立昆）", ["Yoshua_Bengio", "Geoffrey_Hinton", "Yann_LeCun"]),
    ("Edwin Catmull & Pat Hanrahan（埃德温·卡特姆尔、帕特·汉拉汉）", ["Edwin_Catmull", "Pat_Hanrahan"]),
    ("Alfred Aho & Jeffrey Ullman（阿尔佛雷德·阿霍、杰弗里·乌尔曼）", ["Alfred_Aho", "Jeffrey_Ullman"]),
    ("Jack Dongarra（杰克·东加拉）", ["Jack_Dongarra"]),
    ("Robert Metcalfe（罗伯特·梅特卡夫）", ["Robert_Metcalfe"]),
    ("Avi Wigderson（阿维·维格森）", ["Avi_Wigderson"]),
    ("Andrew Barto & Richard S. Sutton（安德鲁·巴托、理查德·萨顿）", ["Andrew_Barto", "Richard_S._Sutton"]),
    ("Charles H. Bennett & Gilles Brassard（查尔斯·贝内特、吉勒·布拉萨）", ["Charles_H._Bennett_(computer_scientist)", "Gilles_Brassard"]),
]

# Known name fragments that appear in the cell text (for multi-person entries)
# These are the exact English names to match and link
NAME_MAP = {
    "Alan Perlis": "Alan_Perlis",
    "Maurice Wilkes": "Maurice_Wilkes",
    "Richard Hamming": "Richard_Hamming",
    "Marvin Minsky": "Marvin_Minsky",
    "James H. Wilkinson": "James_H._Wilkinson",
    "John McCarthy": "John_McCarthy_(computer_scientist)",
    "Edsger W. Dijkstra": "Edsger_W._Dijkstra",
    "Charles Bachman": "Charles_Bachman",
    "Donald Knuth": "Donald_Knuth",
    "Allen Newell": "Allen_Newell",
    "Herbert A. Simon": "Herbert_A._Simon",
    "Michael O. Rabin": "Michael_O._Rabin",
    "Dana Scott": "Dana_Scott",
    "John Backus": "John_Backus",
    "Robert W. Floyd": "Robert_W._Floyd",
    "Kenneth E. Iverson": "Kenneth_E._Iverson",
    "Tony Hoare": "Tony_Hoare",
    "Edgar F. Codd": "Edgar_F._Codd",
    "Stephen Cook": "Stephen_Cook",
    "Dennis Ritchie": "Dennis_Ritchie",
    "Ken Thompson": "Ken_Thompson",
    "Niklaus Wirth": "Niklaus_Wirth",
    "Richard M. Karp": "Richard_M._Karp",
    "John Hopcroft": "John_Hopcroft",
    "Robert Tarjan": "Robert_Tarjan",
    "John Cocke": "John_Cocke_(computer_scientist)",
    "Ivan Sutherland": "Ivan_Sutherland",
    "William Kahan": "William_Kahan",
    "Fernando J. Corbató": "Fernando_J._Corbat%C3%B3",
    "Robin Milner": "Robin_Milner",
    "Butler Lampson": "Butler_Lampson",
    "Juris Hartmanis": "Juris_Hartmanis",
    "Richard E. Stearns": "Richard_E._Stearns",
    "Edward Feigenbaum": "Edward_Feigenbaum",
    "Raj Reddy": "Raj_Reddy",
    "Manuel Blum": "Manuel_Blum",
    "Amir Pnueli": "Amir_Pnueli",
    "Douglas Engelbart": "Douglas_Engelbart",
    "Jim Gray": "Jim_Gray_(computer_scientist)",
    "Fred Brooks": "Fred_Brooks",
    "Andrew Yao": "Andrew_Yao",
    "Ole-Johan Dahl": "Ole-Johan_Dahl",
    "Kristen Nygaard": "Kristen_Nygaard",
    "Leonard Adleman": "Leonard_Adleman",
    "Ron Rivest": "Ron_Rivest",
    "Adi Shamir": "Adi_Shamir",
    "Alan Kay": "Alan_Kay",
    "Vint Cerf": "Vint_Cerf",
    "Robert Kahn": "Robert_Kahn_(computer_scientist)",
    "Peter Naur": "Peter_Naur",
    "Frances Allen": "Frances_Allen",
    "Edmund M. Clarke": "Edmund_M._Clarke",
    "E. Allen Emerson": "E._Allen_Emerson",
    "Joseph Sifakis": "Joseph_Sifakis",
    "Barbara Liskov": "Barbara_Liskov",
    "Charles P. Thacker": "Charles_P._Thacker",
    "Leslie Valiant": "Leslie_Valiant",
    "Judea Pearl": "Judea_Pearl",
    "Shafi Goldwasser": "Shafi_Goldwasser",
    "Silvio Micali": "Silvio_Micali",
    "Leslie Lamport": "Leslie_Lamport",
    "Michael Stonebraker": "Michael_Stonebraker",
    "Whitfield Diffie": "Whitfield_Diffie",
    "Martin Hellman": "Martin_Hellman",
    "Tim Berners-Lee": "Tim_Berners-Lee",
    "John L. Hennessy": "John_L._Hennessy",
    "David Patterson": "David_Patterson_(computer_scientist)",
    "Yoshua Bengio": "Yoshua_Bengio",
    "Geoffrey Hinton": "Geoffrey_Hinton",
    "Yann LeCun": "Yann_LeCun",
    "Edwin Catmull": "Edwin_Catmull",
    "Pat Hanrahan": "Pat_Hanrahan",
    "Alfred Aho": "Alfred_Aho",
    "Jeffrey Ullman": "Jeffrey_Ullman",
    "Jack Dongarra": "Jack_Dongarra",
    "Robert Metcalfe": "Robert_Metcalfe",
    "Avi Wigderson": "Avi_Wigderson",
    "Andrew Barto": "Andrew_Barto",
    "Richard S. Sutton": "Richard_S._Sutton",
    "Charles H. Bennett": "Charles_H._Bennett_(computer_scientist)",
    "Gilles Brassard": "Gilles_Brassard",
}

import re

path = "/Users/ericksun/workspace/codebuddy/math/turing/turing_award.md"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

count = 0
for cell_text, pages in ENTRIES:
    if cell_text not in content:
        print(f"  WARN: not found: {cell_text[:60]}...")
        continue

    # Build replacement: replace each English name with linked version
    new_text = cell_text
    # Find English names in the cell text (before the Chinese part)
    # Extract the English part only (before the first fullwidth parenthesis)
    match = re.match(r'^([^(（]+)', cell_text)
    if not match:
        print(f"  SKIP: no match for {cell_text[:50]}")
        continue
    english_part = match.group(1)
    # Split on " & " or ", " to get individual names
    names_in_cell = re.split(r'\s*[,&]\s+', english_part)
    
    for i, name in enumerate(names_in_cell):
        if i >= len(pages):
            break
        # Replace the exact name with linked version (only first occurrence in the new_text)
        link = f"[{name}]({BASE_URL}{pages[i]})"
        new_text = new_text.replace(name, link, 1)

    content = content.replace(cell_text, new_text, 1)
    count += 1
    print(f"  OK: {cell_text[:60]}...")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\nDone! {count}/{len(ENTRIES)} entries updated.")