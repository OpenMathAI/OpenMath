#!/usr/bin/env python3
"""
Fix duplicate "一句话：" in wolf_prize_allinone_zh.tex
1. Remove \textbf{一句话：} from the personslide macro template
2. Add \textbf{一句话：} prefix to one-liner (#9) of all inline \personslide calls
"""
import re

path = "/Users/ericksun/workspace/codebuddy/math/Wolf_Prize/video/episode-allinone/wolf_prize_allinone_zh.tex"
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Step 1: Fix the personslide macro template
# Change: \\[3pt]\textbf{一句话：} #9
# To:     \\[3pt]#9
content = content.replace(
    r'\\[3pt]\textbf{一句话：} #9',
    '\\\\[3pt]#9',
    1  # only first occurrence (the macro definition)
)
print("✓ Macro template fixed")

# Step 2: For inline \personslide calls (NOT \personslideA), add \textbf{一句话：} to the one-liner
# Pattern: after 8 args, the 9th arg is the one-liner
# Strategy: find \personslide\n  {Name}\n  {Chinese}... then count args

lines = content.split('\n')

# Find all lines with \personslide (not \personslideA)
person_lines = []
for i, l in enumerate(lines):
    s = l.strip()
    if s == r'\personslide':
        person_lines.append(i)

print(f"Found {len(person_lines)} \\personslide calls")

fixed = 0
for idx in person_lines:
    # Count braced args after \personslide
    # Args: name, chinese, image, credit, year, life, nat, inst, contrib, one-liner = 10 args
    args = []
    for j in range(idx+1, min(len(lines), idx+20)):
        s = lines[j].strip()
        if s.startswith('{') and '}' in s:
            args.append(j)
        if len(args) >= 10:
            break
    
    if len(args) >= 10:
        oneliner_line = args[9]  # the 10th arg = one-liner
        orig = lines[oneliner_line]
        # Check if it already has \textbf{一句话：}
        if r'\textbf{一句话：}' not in orig and r'\textbf{一句话:}' not in orig:
            # Add prefix
            indent = orig[:len(orig) - len(orig.lstrip())]
            inner = orig.lstrip()[1:-1]  # strip { and }
            new_line = f'{indent}{{\\textbf{{一句话：}}{inner}}}'
            if new_line != orig:
                lines[oneliner_line] = new_line
                fixed += 1

content = '\n'.join(lines)
print(f"✓ Added \\textbf{{一句话：}} to {fixed} inline one-liners")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Done")