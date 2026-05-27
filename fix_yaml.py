import os, glob

for f in glob.glob('c:/Users/papag/Documents/Proyectos IA/papagamermex/_noticias/*.md') + glob.glob('c:/Users/papag/Documents/Proyectos IA/papagamermex/_para_padres/*.md'):
    with open(f, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    changed = False
    for i, line in enumerate(lines):
        if line.startswith('title: '):
            val = line[7:].strip()
            if val.startswith('"') and val.endswith('"'):
                inner = val[1:-1]
                if '"' in inner and '\\"' not in inner:
                    new_inner = inner.replace('"', '\\"')
                    lines[i] = f'title: "{new_inner}"\n'
                    changed = True
    if changed:
        with open(f, 'w', encoding='utf-8') as file:
            file.writelines(lines)
        print('Fixed:', f)
