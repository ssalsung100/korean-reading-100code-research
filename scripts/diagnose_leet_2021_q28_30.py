#!/usr/bin/env python3

import json
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

XML = Path('자료/LEET_언어이해/검증/HWP_XML/2021.xml')
CTRL = Path('자료/LEET_언어이해/검증/HWP_홀수형_컨트롤_좌표/2021.json')


def lname(tag):
    return tag.split('}')[-1]


def txt(e):
    return ''.join(
        x.text or ''
        for x in e.iter()
        if lname(x.tag) == 'Text'
    )


root = ET.parse(XML).getroot()
parent = {child: par for par in root.iter() for child in par}
paras = [
    e for e in root.iter()
    if lname(e.tag) == 'Paragraph'
    and e in parent
    and lname(parent[e].tag) == 'ColumnSet'
]
controls = json.loads(CTRL.read_text(encoding='utf-8-sig'))['records']

print('columnset_paragraphs =', len(paras))

for i in range(max(0, 295), min(len(paras), 335)):
    p = paras[i]
    text = txt(p)
    tags = Counter(lname(e.tag) for e in p.iter())
    ctrls = [
        c for c in controls
        if c.get('anchor_para') == i
        and str(c.get('control_name') or '') not in {'', '문단 나눔'}
    ]
    interesting = (
        text.strip() or ctrls
        or tags.get('TextboxParagraphList')
        or tags.get('TableControl')
        or tags.get('GShapeObjectControl')
    )
    if not interesting:
        continue

    print('\nPARA', i)
    print('paragraph_id =', p.get('paragraph-id'))
    print('text_len =', len(text))
    print('text_prefix =', repr(text[:180]))
    print('tags =', {
        k: v for k, v in tags.items()
        if k in {
            'TableControl', 'TableBody', 'TableRow', 'TableCell',
            'TextboxParagraphList', 'GShapeObjectControl',
            'ShapeRectangle', 'ShapeLine', 'ShapeEllipse', 'ShapeArc',
            'PictureControl',
        } and v
    })
    print('controls =', [
        {
            'order': c.get('control_order'),
            'name': c.get('control_name'),
            'page': c.get('printed_page'),
            'column': c.get('column_number'),
            'line': c.get('line_number'),
            'anchor_pos': c.get('anchor_pos'),
        }
        for c in ctrls
    ])

    for bi, tb in enumerate(
        [x for x in p.iter() if lname(x.tag) == 'TextboxParagraphList'], 1
    ):
        t = txt(tb)
        print('TEXTBOX', bi, 'len=', len(t), 'text=', repr(t))

    tables = [x for x in p.iter() if lname(x.tag) == 'TableControl']
    for ti, table in enumerate(tables, 1):
        cells = [x for x in table.iter() if lname(x.tag) == 'TableCell']
        print('TABLE', ti, 'cells=', len(cells))
        for ci, cell in enumerate(cells, 1):
            ct = txt(cell)
            print(' CELL', ci, 'len=', len(ct), 'text=', repr(ct))

    shapes = [x for x in p.iter() if lname(x.tag) == 'GShapeObjectControl']
    for si, shape in enumerate(shapes, 1):
        print('SHAPE', si, 'attrs=', dict(shape.attrib))
        descendants = Counter(lname(x.tag) for x in shape.iter())
        print(' shape_tags=', dict(descendants))
        st = txt(shape)
        print(' shape_text_len=', len(st), 'shape_text=', repr(st))
        for node in shape.iter():
            attrs = dict(node.attrib)
            if attrs:
                print('  NODE', lname(node.tag), attrs)
