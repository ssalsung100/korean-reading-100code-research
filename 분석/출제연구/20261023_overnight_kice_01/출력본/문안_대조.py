"""렌더된 PDF와 원본 Markdown을 대조한다. 제작 parser는 import하지 않는다."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import difflib
import hashlib
import html
import json
import re
import unicodedata
import fitz

OUT = Path(__file__).resolve().parent
ROOT = OUT.parent
CASES = [
    ('01_지역빈곤', 'A_지역빈곤/03_학생용_최종후보.md'),
    ('02_품질보증', 'B_품질보증/03_학생용_최종후보.md'),
    ('03_공유자원', 'C_공유자원/03_학생용_최종후보.md'),
    ('04_사회적확산', 'D_추가연구/04_사회적확산_학생용후보.md'),
]


def normalize(s):
    # 공백·정규화 표현만 무시한다. 숫자, 연산자, 조사, 문장부호는 보존한다.
    return re.sub(r'\s+', '', unicodedata.normalize('NFC', s))


def md_visible(source):
    lines = source.splitlines()
    title = lines.pop(0).removeprefix('# ')
    visible = []
    for line in lines:
        line = re.sub(r'^\s*>\s?', '', line).strip()
        if not line or line == '---':
            continue
        if line.startswith('|'):
            cells = [c.strip() for c in line.strip('|').split('|')]
            if all(re.fullmatch(r':?-+:?', c) for c in cells):
                continue
            line = ' '.join(cells)
        else:
            line = re.sub(r'^#{1,6}\s+', '', line)
            line = re.sub(r'^[-*]\s+', '• ', line)
        line = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', line)
        line = line.replace('**', '').replace('`', '')
        visible.append(html.unescape(line))
    return title, normalize('\n'.join(visible))


def main():
    report = {'시각': datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),
              '방법': '학생용: 변환 parser를 가져오지 않고 원MD 표시문자와 PDF본문 전체 순서 대조. 공백/NFC 이외의 문자 보존. 교사용: 기존 문안 조각 검출과 직접 지면 검토 병행.',
              '학생용': [], '교사용': []}
    for suffix, rel in CASES:
        source = ROOT/rel
        title, expected = md_visible(source.read_text())
        doc = fitz.open(OUT/f'학생용_{suffix}.pdf')
        body = ''.join(p.get_text(clip=fitz.Rect(84, 147, 762, 1107)) for p in doc)
        actual = normalize(body)
        prefix = normalize('[1~3] 다음 글을 읽고 물음에 답하시오.')
        assert actual.startswith(prefix)
        actual = actual[len(prefix):]
        first_diff = None
        if actual != expected:
            op = next(op for op in difflib.SequenceMatcher(None, expected, actual, autojunk=False).get_opcodes() if op[0] != 'equal')
            tag, a, b, c, d = op
            first_diff = {'종류': tag, '원MD': expected[max(0,a-30):b+30], 'PDF': actual[max(0,c-30):d+30]}
        report['학생용'].append({
            'pdf': f'학생용_{suffix}.pdf', '원본': rel,
            '원본_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
            '페이지': len(doc), '원본문자': len(expected), 'PDF문자': len(actual),
            '전체순서동일': actual == expected, '첫차이': first_diff,
            '머리글제목': normalize(title) in normalize(doc[0].get_text()),
            '선지표지수': {m: actual.count(m) for m in '①②③④⑤'},
            '해설누출검출': bool(re.search(r'정답|교사용|설계의도|연구기록', actual)),
            '글꼴': sorted({s['font'] for p in doc for b in p.get_text('dict')['blocks'] if 'lines' in b for l in b['lines'] for s in l['spans']}),
        })
    manifests = json.loads((OUT/'typst/문안_검증기준.json').read_text())
    for (suffix, _), manifest in zip(CASES, manifests):
        doc = fitz.open(OUT/f'교사용_{suffix}.pdf')
        body = normalize(''.join(p.get_text(clip=fitz.Rect(72, 68, 770, 1123)) for p in doc))
        missing = [s for s in manifest['teacher_atoms'] if normalize(s) not in body]
        source = ROOT/manifest['teacher_source']
        report['교사용'].append({'pdf':f'교사용_{suffix}.pdf','원본':manifest['teacher_source'],
                               '페이지':len(doc),'문안조각수':len(manifest['teacher_atoms']),
                               '검출실패':missing,'입력생성이후원고동일':hashlib.sha256(source.read_bytes()).hexdigest()==manifest['teacher_sha256']})
    report['통과'] = all(r['전체순서동일'] and r['머리글제목'] and not r['해설누출검출'] and set(r['선지표지수'].values())=={3} for r in report['학생용']) and all(not r['검출실패'] and r['입력생성이후원고동일'] for r in report['교사용'])
    report['한계'] = '학생용은 전체 문자열 순서까지 검증했으나 공백 차이를 판별하지 않는다. 표의 의미·배치는 직접 검수한다. 교사용 조각 검사는 중복·표 셀 배치·전체 순서의 독립 증명이 아니며 직접 지면 검토로 보완한다. 학생 난도·오답률 검증은 아니다.'
    (OUT/'문안대조_검증결과.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    if not report['통과']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
