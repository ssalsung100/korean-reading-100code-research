"""이번 개정에 필요한 수치·반모형·보존만 검사한다. 독립 검토를 대체하지 않는다."""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]
OLD = ROOT.parent


def metrics(incomes, z=100):
    n = len(incomes)
    gaps = [max(F(0), F(z) - F(y)) for y in incomes]
    q = sum(F(y) < z for y in incomes)
    return {
        '소득': incomes,
        '빈곤인원': q,
        'H': F(q, n),
        'G': sum(gaps) / (n * z),
        'S': sum(g * g for g in gaps) / (n * z * z),
        '부족액합': sum(gaps),
        '빈곤층평균부족비율': sum(gaps) / (q * z) if q else None,
    }


def serial(v):
    if isinstance(v, F):
        return {'정확값': str(v), '소수': float(v)}
    if isinstance(v, dict):
        return {k: serial(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [serial(x) for x in v]
    return v


states = {k: metrics(v) for k, v in {
    '지급전': [20, 80, 100, 160],
    '본문_이전후': [30, 70, 100, 160],
    '갑': [20, 100, 100, 160],
    '을': [40, 80, 100, 160],
    '병': [25, 85, 105, 165],
    '을_뒤_B에서A로10': [50, 70, 100, 160],
    '갑_뒤_B에서A로10': [30, 90, 100, 160],
    '을_뒤_40씩': [80, 120, 100, 160],
    '을_뒤_부족액만큼': [100, 100, 100, 160],
    'Q1_2_상태가': [40, 40, 100, 160],
    'Q1_2_상태나': [10, 80, 100, 160],
    'Q1_4_가능예전': [20, 100, 100, 160],
    'Q1_4_가능예후': [80, 90, 100, 160],
    'Q2_50미만1명': [30, 90, 120, 160],
    'Q2_50미만0명': [60, 60, 120, 160],
}.items()}
a, b, c = (states[k] for k in ['갑', '을', '병'])
old = states['지급전']
assert (old['H'], old['G'], old['S']) == (F(1, 2), F(1, 4), F(17, 100))
assert (a['H'], a['G'], a['S']) == (F(1, 4), F(1, 5), F(4, 25))
assert (b['H'], b['G'], b['S']) == (F(1, 2), F(1, 5), F(1, 10))
assert (c['H'], c['G'], c['S']) == (F(1, 2), F(9, 40), F(117, 800))
assert old['G'] == states['본문_이전후']['G']
assert old['S'] > states['본문_이전후']['S']

# 1번②의 반모형: 같은 인원, 총량 감소, 제곱 집계 증가.
x, y = states['Q1_2_상태가'], states['Q1_2_상태나']
assert x['H'] == y['H'] and x['G'] > y['G'] and x['S'] < y['S']
# 1번④의 전제가 실현 가능함. 일반 증명은 해설에 별도 기록.
x, y = states['Q1_4_가능예전'], states['Q1_4_가능예후']
assert x['빈곤인원'] < y['빈곤인원'] and x['G'] > y['G']
assert x['빈곤층평균부족비율'] > y['빈곤층평균부족비율']

# 2번: 같은 보고값·다른 최저 소득과 문턱 아래 인원.
for key, count in [('Q2_50미만1명', 1), ('Q2_50미만0명', 0)]:
    d = states[key]
    assert (d['H'], d['G']) == (F(1, 2), F(1, 5))
    assert d['빈곤층평균부족비율'] == F(2, 5)
    assert sum(v < 50 for v in d['소득']) == count
    assert sum(v for v in d['소득'] if v < 100) == 120

t3, t4, uniform = (states[k] for k in ['을_뒤_B에서A로10', '갑_뒤_B에서A로10', '을_뒤_40씩'])
q3_truth = [
    a['H'] != b['H'] and a['G'] == b['G'],
    old['G'] - c['G'] < old['G'] - a['G'],
    b['G'] == t3['G'] and b['S'] > t3['S'],
    a['H'] < t4['H'] and a['S'] > t4['S'],
    b['부족액합'] == 80 and uniform['H'] == 0,
]
assert q3_truth == [True, True, True, True, False]
assert uniform['부족액합'] == 20
assert states['을_뒤_부족액만큼']['H'] == 0

# 기출의 계산과 별도 조건을 함께 재검산. 현행 BIS 규정 검증은 아니다.
did = (F('20.9') - F('19.6')) - (F('20.2') - F('22.3'))
assert did == F('3.4')
bis = {'II_공시': F(110, 1000), 'III_증액후총비율': F(80, 1000), 'III_증액후기본': F(50, 1000)}
assert bis['III_증액후총비율'] == F('0.08') and bis['III_증액후기본'] < F('0.06')

original = (OLD / '07_학생용_최종.md').read_text()
revised = (ROOT / '03_학생용_개정본.md').read_text()
def q2(s):
    return s[s.index('## 2.'):s.index('## 3.')]
assert q2(original) == q2(revised)
for num in range(1, 4):
    block = revised.split(f'## {num}.', 1)[1].split('\n## ', 1)[0]
    assert re.findall(r'^([①②③④⑤]) ', block, flags=re.M) == list('①②③④⑤')
assert '적절하지 않은 것은?' in revised.split('## 3.')[1]
hashes = json.loads((ROOT / '검증/기존본_보존해시.json').read_text())
for p, expected in hashes.items():
    assert hashlib.sha256((OLD / p).read_bytes()).hexdigest() == expected

body = revised.split('물음에 답하시오.**\n\n', 1)[1].split('\n## 1.', 1)[0].strip()
result = {
    '검증범위': '이번 개정의 유리수 검산·반모형·2번 문자열·기존 4개 파일 보존. 독립 풀이 또는 품질 인증 아님.',
    '상태별_값': states,
    'Q1_최종_선지진리값_일반증명은해설참조': [False, False, False, True, False],
    'Q2_최종_선지진리값_일반증명은해설참조': [False, True, False, False, False],
    'Q3_최종_선지진리값': q3_truth,
    '정답': ['④', '②', '⑤'],
    'Q3_발문': '적절하지 않은 것',
    '기출_이중차분_추정치': did,
    '기출_BIS': bis,
    '2번_문자열동일': True,
    '기존4파일_해시동일': True,
    '본문문단수': len(body.split('\n\n')),
    '본문글자수_공백포함': len(body),
    '본문글자수_공백제외': len(re.sub(r'\s', '', body)),
}
(ROOT / '검증/개정본_검산결과.json').write_text(json.dumps(serial(result), ensure_ascii=False, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k in ['정답', '2번_문자열동일', '기존4파일_해시동일', '본문문단수', '본문글자수_공백포함']}, ensure_ascii=False))
