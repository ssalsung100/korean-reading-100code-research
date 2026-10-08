#!/usr/bin/env python3

from __future__ import annotations

import bisect
import json
import re
import sys
import xml.etree.ElementTree as ET

from collections import Counter
from pathlib import Path

ROOT = Path('.')
sys.path.insert(0, str(ROOT / 'scripts'))
import restore_remaining_target_sources as restore

GROUPS = [
    ('2010', 19, 21), ('2011', 6, 8), ('2011', 9, 11),
    ('2011', 27, 29), ('2012', 27, 29), ('2014', 23, 25),
    ('2014', 26, 29), ('2015', 17, 20), ('2016', 33, 35),
    ('2019', 28, 30), ('2020', 16, 18), ('2021', 28, 30),
]
CONTROL_ROOT = ROOT / '자료/LEET_언어이해/검증/HWP_홀수형_컨트롤_좌표'
XML_ROOT = ROOT / '자료/LEET_언어이해/검증/HWP_XML'
VISUAL_MAPPING = ROOT / '자료/LEET_언어이해/검증/HWP_홀수형_시각자료_문항매핑_v1.json'
MARKER_RE = re.compile(r'<(그림|표)>|\[(그림|표)\]|!\[|\[시각\s*자료', re.I)


def lname(tag: str) -> str:
    return tag.split('}')[-1]


def norm(text: str) -> str:
    text = text or ''
    text = re.sub(r'<(?:그림|표)>|\[(?:그림|표)\]', '', text)
    return ''.join(ch for ch in text if ch.isalnum() or ('가' <= ch <= '힣'))


def paragraph_text(p):
    return ''.join(e.text or '' for e in p.iter() if lname(e.tag) == 'Text')


def main_body_paragraphs(root):
    parent = {child: par for par in root.iter() for child in par}
    return [e for e in root.iter() if lname(e.tag) == 'Paragraph' and e in parent and lname(parent[e].tag) == 'ColumnSet']


def marker_summary(passage, questions):
    records = []
    def collect(location, text, qno=None, choice=None):
        if not isinstance(text, str):
            return
        for m in MARKER_RE.finditer(text):
            records.append({'location': location, 'question': qno, 'choice': choice,
                            'token': m.group(1) or m.group(2) or 'image_link', 'raw_offset': m.start()})
    collect('passage', passage)
    for qno, q in questions.items():
        collect('stem', q.get('stem', ''), qno=qno)
        choices = q.get('choices', [])
        iterator = choices.items() if isinstance(choices, dict) else enumerate(choices, 1)
        for choice_no, choice in iterator:
            collect('choice', choice, qno=qno, choice=choice_no)
    return records


def passage_anchor(passage, paras):
    key = norm(passage)
    ptexts = [norm(paragraph_text(p)) for p in paras]
    body = ''
    starts = []
    for text in ptexts:
        starts.append(len(body))
        body += text
    CHUNK, STEP = 28, 14
    hits = []
    if len(key) < CHUNK:
        return {'passage_chars': len(key), 'unique_anchor_hits': 0, 'coverage': 0.0,
                'xml_para_start': None, 'xml_para_end': None, 'first_hits': [], 'last_hits': []}
    for off in range(0, len(key) - CHUNK + 1, STEP):
        sig = key[off:off + CHUNK]
        pos = body.find(sig)
        if pos < 0 or body.find(sig, pos + 1) >= 0:
            continue
        para = bisect.bisect_right(starts, pos) - 1
        if para >= 0:
            hits.append((off, pos, para))
    if not hits:
        return {'passage_chars': len(key), 'unique_anchor_hits': 0, 'coverage': 0.0,
                'xml_para_start': None, 'xml_para_end': None, 'first_hits': [], 'last_hits': []}
    first_off, last_off = hits[0][0], hits[-1][0]
    return {'passage_chars': len(key), 'unique_anchor_hits': len(hits),
            'coverage': round((last_off - first_off + CHUNK) / len(key), 4),
            'xml_para_start': min(x[2] for x in hits), 'xml_para_end': max(x[2] for x in hits),
            'first_hits': [(x[0], x[2]) for x in hits[:6]], 'last_hits': [(x[0], x[2]) for x in hits[-6:]]}


def control_summary(control_records, anchor):
    lo, hi = anchor.get('xml_para_start'), anchor.get('xml_para_end')
    if lo is None or hi is None:
        return []
    out = []
    for c in control_records:
        ap = c.get('anchor_para')
        if not isinstance(ap, int) or not (max(0, lo - 1) <= ap <= hi + 1):
            continue
        name = str(c.get('control_name') or '')
        if name in {'', '문단 나눔'}:
            continue
        out.append({'anchor_para': ap, 'control_order': c.get('control_order'), 'control_name': name,
                    'page': c.get('printed_page'), 'column': c.get('column_number'),
                    'line': c.get('line_number'), 'anchor_pos': c.get('anchor_pos')})
    return out


def textbox_summary(paras, controls):
    out, seen = [], set()
    for c in controls:
        ap = c.get('anchor_para')
        if not isinstance(ap, int) or not (0 <= ap < len(paras)) or ap in seen:
            continue
        seen.add(ap)
        boxes = [tb for tb in paras[ap].iter() if lname(tb.tag) == 'TextboxParagraphList']
        for i, tb in enumerate(boxes, 1):
            text = ''.join(e.text or '' for e in tb.iter() if lname(e.tag) == 'Text')
            out.append({'anchor_para': ap, 'box': i, 'text': text, 'normalized_len': len(norm(text))})
    return out


def exact_assets(mapping, label, start, end):
    paper = next((p for p in mapping.get('papers', []) if str(p.get('label')) == str(label)), None)
    if paper is None:
        return []
    return [{'kind': a.get('kind'), 'asset_number': a.get('asset_number'),
             'mapping_basis': a.get('mapping_basis'), 'mapping_confidence': a.get('mapping_confidence')}
            for a in paper.get('assets', []) if a.get('question_group') == [start, end]]


def preliminary_classification(markers, anchor, controls, textboxes, assets):
    if anchor['coverage'] < 0.98:
        return 'UNRESOLVED_LOW_ANCHOR_COVERAGE'
    visual_assets = [a for a in assets if a.get('kind') in {'embedded_figure', 'data_table', 'choice_table'}]
    if visual_assets:
        return 'REAL_VISUAL_CANDIDATE'
    if textboxes:
        return 'VERIFIED_TEXTBOX_CANDIDATE'
    if not controls:
        return 'ARTIFACT_CANDIDATE'
    return 'UNRESOLVED_CONTROL_PRESENT'


def source_path_for(label):
    return ROOT / f'자료/LEET_언어이해/텍스트/{label}/{label}_question_odd.md'


def run_group(mapping, label, start, end):
    md_path, xml_path, ctrl_path = source_path_for(label), XML_ROOT / f'{label}.xml', CONTROL_ROOT / f'{label}.json'
    result = {'year': label, 'range': [start, end], 'source_path': str(md_path), 'xml_path': str(xml_path),
              'parse_success': False, 'error': None}
    try:
        for path in (md_path, xml_path, ctrl_path):
            if not path.is_file():
                raise FileNotFoundError(path)
        raw = md_path.read_text(encoding='utf-8-sig')
        parsed = restore.parse_markdown_group(raw, start, end)
        if parsed is None:
            result['error'] = 'parse_markdown_group_failed'
            return result
        passage, questions = parsed
        result['parse_success'] = True
        result['passage_nonempty'] = bool(passage.strip())
        result['question_count'] = len(questions)
        result['choice_counts'] = {str(n): len(questions[n].get('choices', [])) for n in range(start, end + 1) if n in questions}
        markers = marker_summary(passage, questions)
        result['markers'] = markers
        result['marker_counts'] = dict(Counter(x['token'] for x in markers))
        xml_root = ET.parse(xml_path).getroot()
        paras = main_body_paragraphs(xml_root)
        result['columnset_paragraph_count'] = len(paras)
        anchor = passage_anchor(passage, paras)
        result['anchor'] = anchor
        controls_json = json.loads(ctrl_path.read_text(encoding='utf-8-sig'))
        controls = control_summary(controls_json.get('records', []), anchor)
        result['controls'] = controls
        result['textboxes'] = textbox_summary(paras, controls)
        assets = exact_assets(mapping, label, start, end)
        result['exact_assets'] = assets
        result['preliminary_classification'] = preliminary_classification(markers, anchor, controls, result['textboxes'], assets)
        return result
    except Exception as e:
        result['error'] = repr(e)
        return result


def main():
    mapping = json.loads(VISUAL_MAPPING.read_text(encoding='utf-8-sig'))
    results = [run_group(mapping, label, start, end) for label, start, end in GROUPS]
    out_path = ROOT / '자료/LEET_언어이해/검증/remaining_visual_diagnostic.json'
    out_path.write_text(json.dumps(results, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(results, ensure_ascii=False, indent=2))
    print('\nwritten =', out_path)


if __name__ == '__main__':
    main()
