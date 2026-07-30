#!/usr/bin/env python3
"""
Add portrait thumbnails to the bottom half of each Abel Prize beamer data slide.
Each slide shows portraits of the laureates listed on that page.
"""
import re

path = "/Users/ericksun/workspace/codebuddy/math/medal_list_allinone/abel_beamer/abel_prize_laureates_beamer.tex"
with open(path, 'r', encoding='utf-8') as f:
    tex = f.read()

# Map: slide title -> [(english_name, image_file), ...]
slides = {
    '2003–2006': [
        ('Jean-Pierre Serre', 'serre.jpg'),
        ('Michael Atiyah', 'atiyah.jpg'),
        ('Isadore Singer', 'singer.jpg'),
        ('Peter Lax', 'lax.jpg'),
        ('Lennart Carleson', 'carleson.jpg'),
    ],
    '2007–2010': [
        ('S. R. Srinivasa Varadhan', 'varadhan.jpg'),
        ('John G. Thompson', 'thompson.jpg'),
        ('Jacques Tits', 'tits.jpg'),
        ('Mikhail Gromov', 'gromov.jpg'),
        ('John Tate', 'tate.jpg'),
    ],
    '2011–2014': [
        ('John Milnor', 'milnor.jpg'),
        ('Endre Szemerédi', 'szemeredi.jpg'),
        ('Pierre Deligne', 'deligne.jpg'),
        ('Yakov Sinai', 'sinai.jpg'),
    ],
    '2015–2018': [
        ('John F. Nash Jr.', 'nash.jpg'),
        ('Louis Nirenberg', 'nirenberg.jpg'),
        ('Andrew Wiles', 'wiles.jpg'),
        ('Yves Meyer', 'meyer.jpg'),
        ('Robert Langlands', 'langlands.jpg'),
    ],
    '2019–2021': [
        ('Karen Uhlenbeck', 'uhlenbeck.jpg'),
        ('Hillel Furstenberg', 'furstenberg.jpg'),
        ('Gregory Margulis', 'margulis.jpg'),
        ('László Lovász', 'lovasz.jpg'),
        ('Avi Wigderson', 'wigderson.jpg'),
    ],
    '2022–2026': [
        ('Dennis Sullivan', 'sullivan.jpg'),
        ('Luis Caffarelli', 'caffarelli.jpg'),
        ('Michel Talagrand', 'talagrand.jpg'),
        ('Masaki Kashiwara', 'kashiwara.jpg'),
        ('Gerd Faltings', 'faltings.jpg'),
    ],
}

replaced = 0
for title, laureates in slides.items():
    n = len(laureates)
    # Calculate positions: spread evenly over ~10cm
    if n == 5:
        positions = [-4.4, -2.2, 0.0, 2.2, 4.4]
    elif n == 4:
        positions = [-3.3, -1.1, 1.1, 3.3]
    else:
        continue

    # Build portrait row tikz
    portrait_lines = []
    for (name, img), x in zip(laureates, positions):
        portrait_lines.append(
            f'      \\node[inner sep=0pt] at ({x:.1f},0) {{'
        )
        portrait_lines.append(
            f'        \\includegraphics[width=0.55cm,height=0.65cm,keepaspectratio]{{images/{img}}}'
        )
        portrait_lines.append(
            f'      }};'
        )

    portrait_tikz = (
        '\\vspace{6pt}\n'
        '  {\\centering\n'
        '  \\begin{tikzpicture}\n'
        + '\n'.join(portrait_lines) + '\n'
        '  \\end{tikzpicture}}\n'
    )

    # Find the slide and replace \end{tabular}\end{frame}
    # We need to find the specific slide's end pattern
    search_start = tex.find(f'{{{title}}}')
    if search_start == -1:
        print(f'WARNING: slide "{title}" not found')
        continue

    # Find the next \end{frame} after this title
    end_frame_pos = tex.find('\\end{frame}', search_start)
    # Find the last \end{tabular} before that end_frame
    subsection = tex[search_start:end_frame_pos]
    last_tabular = subsection.rfind('\\end{tabular}')
    if last_tabular == -1:
        print(f'WARNING: no tabular in slide "{title}"')
        continue

    tabular_end_in_full = search_start + last_tabular + len('\\end{tabular}')

    # Check what's between \end{tabular} and \end{frame}
    tail = tex[tabular_end_in_full:end_frame_pos]
    if 'tikzpicture' in tail:
        print(f'  Skipping "{title}": already has portraits')
        continue

    # Insert portrait tikz between \end{tabular} and \end{frame}
    old = tex[tabular_end_in_full:end_frame_pos + len('\\end{frame}')]
    new = '\n' + portrait_tikz + '\\end{frame}'
    tex = tex[:tabular_end_in_full] + new + tex[end_frame_pos + len('\\end{frame}'):]
    replaced += 1
    print(f'  ✓ {title} ({n} portraits)')

with open(path, 'w', encoding='utf-8') as f:
    f.write(tex)

print(f'\nDone: {replaced} slides updated')