import json
from pathlib import Path
from fetch_full_pages import WANTED_PROPS, _build_frontmatter

qid = 'Q39599'
name = 'Christiaan Huygens'
ent = json.load(open('/tmp/huygens.json'))['entities'][qid]
claims = ent.get('claims', {})

labels = {}
ldata = json.load(open('/tmp/huygens_labels.json'))
for q, e in ldata.get('entities', {}).items():
    lab = e.get('labels', {}).get('en', {}).get('value')
    if lab:
        labels[q] = lab

raw = {}
for pid, key in WANTED_PROPS.items():
    vals = []
    for c in claims.get(pid, []):
        dv = c.get('mainsnak', {}).get('datavalue')
        if not dv:
            continue
        v = dv.get('value')
        if dv.get('type') == 'wikibase-entityid':
            qid_ref = v.get('id')
            if qid_ref:
                vals.append(labels.get(qid_ref, qid_ref))
        elif dv.get('type') == 'time':
            vals.append(v.get('time', '').lstrip('+').split('T')[0])
        elif dv.get('type') == 'string':
            vals.append(str(v))
    if vals:
        raw[key] = vals

meta = {
    'name': name, 'lang': 'en', 'qid': qid,
    'label': ent.get('labels', {}).get('en', {}).get('value'),
    'description': ent.get('descriptions', {}).get('en', {}).get('value'),
    'properties': raw,
}

d = Path('presentations/17th_century/pages/Christiaan_Huygens')
(d / 'metadata.json').write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding='utf-8')

text = (d / 'page.md').read_text(encoding='utf-8')
idx = text.find('\n---\n', 1)
if idx != -1:
    body = text[idx + len('\n---\n'):]
    (d / 'page.md').write_text(_build_frontmatter(name, 'en', meta) + '\n\n' + body.lstrip('\n'), encoding='utf-8')

print('DONE props:', sorted(raw.keys()))
print('nationality:', raw.get('nationality'))
print('field_of_work:', raw.get('field_of_work'))
