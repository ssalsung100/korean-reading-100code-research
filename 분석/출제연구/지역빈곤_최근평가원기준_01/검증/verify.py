"""이번 산출물의 수치·참조·포장 검사. 기존 원장에는 쓰지 않는다."""
from fractions import Fraction as F
from pathlib import Path
from hashlib import sha256
import json
import re
import zipfile

OUT = Path(__file__).resolve().parents[1]
ROOT = OUT.parents[2]

def stats(incomes, z=100):
    n = len(incomes)
    gaps = [max(F(z) - y, F(0)) / z for y in incomes]
    q = sum(y < z for y in incomes)
    s = sum(gaps, F(0))
    return {"N": n, "q": q, "S": s, "H": F(q, n),
            "I": s/q if q else None, "G": s/n}

def encode(value):
    if isinstance(value, F):
        return {"정확값": str(value), "소수": float(value)}
    if isinstance(value, dict):
        return {k: encode(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [encode(v) for v in value]
    return value

student_path = OUT / '03_학생용_지문과3문항.md'
student = student_path.read_text(encoding='utf-8')
sections = re.split(r'^## ([123])\. ', student, flags=re.M)
assert len(sections) == 7
choices = {}
for j in (1, 3, 5):
    q = int(sections[j])
    found = re.findall(r'^([①②③④⑤]) (.+)$', sections[j+1], flags=re.M)
    assert [a for a, _ in found] == list('①②③④⑤')
    choices[q] = [b for _, b in found]
assert not any(w in student for w in ['정답', '해설', '제작자', 'R1', 'AI 판단'])
assert '보다 작겠군' in choices[2][3]

# 원본 편집본의 기존 문장 보존과 추가 한 문장을 확인한다.
original = (ROOT / '분석/출제연구/지역빈곤_학생용편집_01/01_학생용_지문.md').read_text()
old_paragraphs = original.strip().split('\n\n')[1:]
body = sections[0].split('\n---\n')[0].strip()
new_paragraphs = body.split('\n\n')[1:]
assert len(old_paragraphs) == 7 and len(new_paragraphs) == 8
assert old_paragraphs[:6] == new_paragraphs[:6]
assert ' '.join(new_paragraphs[6:]).startswith(old_paragraphs[6])

# 1번: 일반 항등식은 교사용에서 증명. 여기서는 반례와 국소 수치 확인.
reverse_a = [F(2, 5), F(3, 20)]
reverse_b = [F(4, 5), F(1, 20)]
weights = [F(1, 5), F(4, 5)]
aggregate_a = sum(a*w for a, w in zip(reverse_a, weights))
aggregate_b = sum(a*w for a, w in zip(reverse_b, weights))
assert aggregate_a == aggregate_b == F(1, 5) and reverse_a != reverse_b
person_weights = [F(1, k)*F(k, 100) for k in range(1, 101)]
q1 = [F(5)*F(2, 5)/10 == F(2, 5),
      F(3, 5)*F(1, 5) > F(3, 10)*F(4, 5),
      (F(1, 5)+F(2, 5))/2 == F(1, 5)+F(2, 5),
      all(w == F(1, 100) for w in person_weights),
      not (aggregate_a == aggregate_b and reverse_a != reverse_b)]

# 2번: 모두 정확한 유리수로 계산한다.
n = [200, 300, 500]
h = [F(1, 2), F(2, 5), F(1, 5)]
i = [F(2, 5), F(1, 2), F(3, 5)]
g = [a*b for a, b in zip(h, i)]
poor = [a*b for a, b in zip(n, h)]
s = [a*b for a, b in zip(n, g)]
c = [x/sum(n) for x in s]
G = sum(c)
I = sum(s)/sum(poor)
wrong_I = sum(F(nk, sum(n))*ik for nk, ik in zip(n, i))
q2 = [g[0] > g[1], G == sum(g)/3,
      g[1] != g[2] and c[1] == c[2],
      i[1] < I,
      c[2] == F(6, 100) and s[2]/sum(s) == F(6, 100)]
assert I == F(1, 2) and wrong_I == F(53, 100)
assert not (i[1] > wrong_I) and i[1] < wrong_I

# 3번: 보기에 명시한 100명 전체를 직접 구성한다.
a0 = [F(0), F(90)] + [F(100)]*48
b0 = [F(60), F(60)] + [F(100)]*48
a1 = [F(30), F(120)] + [F(100)]*48
b1 = [F(90), F(90)] + [F(100)]*48
A0, B0, A1, B1 = [stats(x) for x in (a0, b0, a1, b1)]
T0, TA, TB = [stats(x) for x in (a0+b0, a1+b0, a0+b1)]
drop_a, drop_b = T0['G']-TA['G'], T0['G']-TB['G']
q3 = [A0['S']/100 < B0['S']/100,
      A1['H'] == A0['H'] and A1['I'] < A0['I'],
      B1['H'] < B0['H'] and TB['H'] < T0['H'],
      drop_a == drop_b, drop_b > drop_a]
assert [drop_a, drop_b] == [F(4, 1000), F(6, 1000)]
assert A1['I'] > A0['I'] and A1['G'] < A0['G']

# 경계와 구획 변경. 여러 지역 단순 평균의 불변은 주장하지 않는다.
assert stats([F(0)])['G'] == 1
assert stats([F(100)])['G'] == 0
assert stats([F(130)])['G'] == 0
assert stats([F(100), F(130)])['I'] is None
people = [F(0), F(50), F(100), F(75), F(100)]
partitions = [[people[:2], people[2:]], [people[:1], people[1:3], people[3:]]]
partition_G = [sum(stats(p)['G']*len(p)/len(people) for p in parts) for parts in partitions]
simple_G = [sum(stats(p)['G'] for p in parts)/len(parts) for parts in partitions]
assert all(x == stats(people)['G'] for x in partition_G)
assert simple_G[0] != simple_G[1]

truths = [q1, q2, q3]
answers = [[k+1 for k, truth in enumerate(row) if truth] for row in truths]
assert answers == [[4], [3], [5]]

# 읽은 26문항의 기존 공식대조 답 필드만 확인한다. 기존 파일 쓰기 없음.
expected = {(2023, '6월 모평', 14): '①', (2023, '6월 모평', 15): '⑤',
 (2023, '6월 모평', 16): '④', (2023, '6월 모평', 17): '②',
 (2024, '수능', 4): '⑤', (2024, '수능', 5): '③', (2024, '수능', 6): '②', (2024, '수능', 7): '②',
 (2025, '6월 모평', 4): '①', (2025, '6월 모평', 5): '⑤', (2025, '6월 모평', 6): '②', (2025, '6월 모평', 7): '①',
 (2026, '6월 모평', 4): '②', (2026, '6월 모평', 5): '③', (2026, '6월 모평', 6): '④',
 (2026, '6월 모평', 7): '④', (2026, '6월 모평', 8): '⑤', (2026, '6월 모평', 9): '①',
 (2027, '6월 모평', 10): '②', (2027, '6월 모평', 11): '③', (2027, '6월 모평', 12): '⑤', (2027, '6월 모평', 13): '⑤',
 (2027, '9월 모평', 14): '②', (2027, '9월 모평', 15): '③', (2027, '9월 모평', 16): '④', (2027, '9월 모평', 17): '⑤'}
matched = []
for line in (ROOT/'data/kice_questions.jsonl').read_text().splitlines():
    r = json.loads(line)
    key = (r['academic_year'], r['exam_label'], r['question_number'])
    if key in expected:
        assert r['answer'] == expected[key] and r['official_answer_verified']
        matched.append({'시험': list(key), '답': r['answer']})
assert len(matched) == 26

# 해설이 들어갈 수 없게 파일을 명시하여 포장한다.
archive_path = OUT/'독립풀이용.zip'
with zipfile.ZipFile(archive_path, 'w', compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write(student_path, arcname=student_path.name)
with zipfile.ZipFile(archive_path) as zf:
    assert zf.namelist() == [student_path.name]
    assert zf.read(student_path.name) == student_path.read_bytes()
    archive_names = zf.namelist()

required = ['00_README.md', '01_최근동분야_기출대조.md', '02_현재원고_진단과설계결정.md',
 '03_학생용_지문과3문항.md', '04_교사용_정답과선지해설.md', '05_기출판단과_신규문항_대응.md',
 '06_수정기록과_남은한계.md', '07_연구자_읽기안내.md', '독립풀이용.zip']
assert all((OUT/f).exists() and (OUT/f).stat().st_size > 0 for f in required)
broken = []
local_link_count = 0
for md in OUT.rglob('*.md'):
    for link in re.findall(r'\]\(([^)]+)\)', md.read_text()):
        if link.startswith(('http:', 'https:', '#')):
            continue
        target = link.split('#')[0].strip('<>')
        if not target:
            continue
        local_link_count += 1
        resolved = (md.parent/target).resolve()
        # 결과 파일은 아래에서 생성된다.
        if resolved == (OUT/'검증/검증결과.json').resolve():
            continue
        if not resolved.exists():
            broken.append({'파일': str(md.relative_to(OUT)), '링크': link})

report = {'상태': '통과' if not broken else '참조 수정 필요', '날짜': '2026-10-22',
 '검증범위': '정확 수치·반례·문항수·로컬 참조·ZIP. 의미 판독의 자동 증명 아님.',
 '문항수': 3, '선지수': 15, '수치검산_진위': truths, '정답': answers,
 '1번_역복원반례': {'인구비중': weights, '구성1': reverse_a, '구성2': reverse_b, '같은전체G': aggregate_a},
 '2번': {'G': g, '빈곤인구': poor, '부족비율합': s, '기여분': c, '전체G': G,
          '전체I': I, '잘못된인구가중I': wrong_I, '3번선지외연산필수여부': False},
 '3번': {'지원전': T0, '갑지원후': TA, '을지원후': TB, '감소폭': [drop_a, drop_b],
          '갑_평균부족비율': [A0['I'], A1['I']]},
 '경계값': '0 소득·빈곤선 동일 소득·빈곤층 없음·비빈곤층 0 확인',
 '구획변경': {'전체G': partition_G, '단순평균': simple_G},
 '기존공식답필드대조': matched, '새공식답PDF전수검증': False,
 '학생용_기존P1_P6동일': True, '본문문단수': len(new_paragraphs),
 '학생용_sha256': sha256(student_path.read_bytes()).hexdigest(),
 'ZIP내용': archive_names, 'ZIP학생용과원파일동일': True,
 '필수산출물': required, '로컬링크수': local_link_count, '깨진링크': broken,
 '학생실증': '미수행', '기존원장쓰기': False}
(OUT/'검증/검증결과.json').write_text(json.dumps(encode(report), ensure_ascii=False, indent=2)+'\n')
print(json.dumps({'상태': report['상태'], '정답': answers, '문항': 3, '선지': 15,
                  'ZIP': archive_names, '깨진링크': broken}, ensure_ascii=False, indent=2))
assert not broken, '로컬 참조를 수정해야 함'
