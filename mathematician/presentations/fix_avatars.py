#!/usr/bin/env python3
import os, re

base = '/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations'

tasks = {
    'Richard_Brauer': 'Richard_Brauer.jpg',
    'Issai_Schur': 'Issai_Schur.jpg',
    'Paul_Lévy': 'Paul_Levy.jpg',
    'Bartel_Leendert_van_der_Waerden': 'Bartel_van_der_Waerden.jpg',
    'Edmund_Landau': 'Edmund_Landau.jpg',
    'Goro_Shimura': 'Goro_Shimura.jpg',
    'Thoralf_Skolem': 'Thoralf_Skolem.jpg',
    'Oswald_Teichmüller': 'Oswald_Teichmuller.jpg',
    'Émile_Picard': 'Emile_Picard.jpg',
    'Salomon_Bochner': 'Salomon_Bochner.jpg',
    'Alfred_North_Whitehead': 'Alfred_North_Whitehead.jpg',
    'Andrey_Tikhonov': 'Andrey_Tikhonov.jpg',
    'Nikolai_Luzin': 'Nikolai_Luzin.jpg',
    'Pavel_Alexandrov': 'Pavel_Alexandrov.jpg',
    'Tadashi_Nakayama': 'Tadashi_Nakayama.jpg',
    'Mikio_Sato': 'Mikio_Sato.jpg',
    'Ernst_Lindelöf': 'Ernst_Lindelof.jpg',
    'Oskar_Perron': 'Oskar_Perron.jpg',
    'Camille_Jordan': 'Camille_Jordan.jpg',
    'Felix_Bernstein': 'Felix_Bernstein.jpg',
    'Albert_W._Tucker': 'Albert_W._Tucker.jpg',
    'Ivan_Vinogradov': 'Ivan_Vinogradov.jpg',
    'Yuri_Linnik': 'Yuri_Linnik.jpg',
    'Ivan_Petrovsky': 'Ivan_Petrovsky.jpg',
    'Vladimir_Rokhlin': 'Vladimir_Rokhlin.jpg',
    'Torsten_Carleman': 'Torsten_Carleman.jpg',
    'Mikhail_Suslin': 'Mikhail_Suslin.jpg',
    'E._C._Zeeman': 'Christopher_Zeeman.jpg',
    'Fukuhara_Masuo': 'Fukuhara_Masuo.jpg',
}

ok, fail = 0, 0
for d, img in tasks.items():
    tex = os.path.join(base, d, d + '_zh.tex')
    if not os.path.exists(tex):
        print(f'SKIP: {d}')
        fail += 1
        continue
    with open(tex) as f:
        content = f.read()
    avatar = '  \\node[anchor=north east, inner sep=0pt] at ([xshift=0cm, yshift=0cm]current page.north east) {\\includegraphics[width=3.2cm]{' + img + '}};\n'
    # Pattern: optional comment line + decorative circle block after Chinese name
    pat = r'(\{[^}]*\};\n)(  % [^\n]*\n  \\node\[anchor=center, inner sep=0pt\] at \(\[xshift=-6\.6cm, yshift=0\.55cm\].*?\\end\{tikzpicture\}\};)'
    m = re.search(pat, content, re.DOTALL)
    if m:
        new_content = content[:m.start()] + m.group(1) + avatar + content[m.end():]
        with open(tex, 'w') as f:
            f.write(new_content)
        print(f'OK: {d}')
        ok += 1
    else:
        # Try without comment line
        pat2 = r'(\{[^}]*\};\n)(  \\node\[anchor=center, inner sep=0pt\] at \(\[xshift=-6\.6cm, yshift=0\.55cm\].*?\\end\{tikzpicture\}\};)'
        m2 = re.search(pat2, content, re.DOTALL)
        if m2:
            new_content = content[:m2.start()] + m2.group(1) + avatar + content[m2.end():]
            with open(tex, 'w') as f:
                f.write(new_content)
            print(f'OK: {d} (no comment)')
            ok += 1
        else:
            print(f'FAIL: {d}')
            fail += 1
print(f'\nDone: {ok} OK, {fail} FAIL')
