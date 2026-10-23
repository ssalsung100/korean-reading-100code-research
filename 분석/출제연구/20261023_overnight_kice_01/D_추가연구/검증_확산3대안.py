"""원보기 보존·기존 검산 결과에 대한 새 선지 판정·조합의 정보 필요성을 확인한다."""
from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import re

ROOT = Path(__file__).resolve().parent
student = (ROOT/'04_사회적확산_학생용후보.md').read_text()
candidate = (ROOT/'08_확산3_고정상태_필수판단_대안.md').read_text()
old_q3 = student.split('## 3.', 1)[1]
new_q3 = candidate.split('### 3.', 1)[1].split('## 전 선지', 1)[0]
view = lambda s: re.sub(r'\s+', '', s[s.index('> **<보기>**'):s.index('\n①')])
assert view(old_q3) == view(new_q3), '현재 학생용과 채택 대안의 보기가 다름'
choices = re.findall(r'^([①②③④⑤]) (.+)$', new_q3, re.M)
assert [m for m, _ in choices] == list('①②③④⑤')
assert re.findall(r'^([①②③④⑤]) (.+)$', old_q3, re.M) == choices, '현재 학생용과 채택 대안의 선지가 다름'

# 최초 대안은 보기 전체를 보존했으나, 후속 검토에서 문턱의 양방향을 명시했다.
# 표가 바뀐 것은 아니며, 이전 충분조건만 읽을 때의 다른 모형을 국소 확인한다.
prior_student = (ROOT/'개정이력/학생용_v2_3번고정상태선택필수화전.md').read_text().split('## 3.',1)[1]
rows = lambda s: re.findall(r'^\|([A-F])\|([^|]+)\|([^|]+)\|$', s, re.M)
assert rows(new_q3) == rows(prior_student)
assert '아직 행동을 채택하지 않은 사람은' in new_q3
assert '그렇지 않으면 채택하지 않는다' in new_q3
graphs = [{v:set(col.replace(' ', '').split(',')) for v, *cols in rows(new_q3) for col in [cols[j]]} for j in [0,1]]
def counter_first(g):
    active=set('AB');steps=[active.copy()]
    while True:
        nxt=active | {v for v in g if len(g[v]&active)>=1}
        if nxt==active:
            break
        steps.append(nxt);active=nxt
    return next((i for i,x in enumerate(steps) if 'C' in x),None)
counter = [counter_first(g) for g in graphs]
assert counter == [2,1]
assert all((k<2) or (k>=1) for k in range(4))

# 이미 검증한 연결망 상태를 다시 산출하지 않고 새 선택지에 필요한 값만 읽는다.
prior = json.loads((ROOT/'사회적확산_검증결과.json').read_text())['모형']
actual = (prior['I']['최초채택']['C'], prior['II']['최초채택']['C'] is not None)
assert actual == (2, False)
assert prior['II']['마지막비채택자의_채택이웃수'] == {'C':1, 'E':1, 'F':1}

# 각 문장의 의미를 저자가 아래 두 축으로 옮겼다. 프로그램이 자연어를 증명하지 않는다.
# I의 최초 채택 단계(None=계속 미채택), II의 최종 채택 여부.
claims = [(1, True), (2, True), (2, False), (None, False), (1, False)]
truth = [claim == actual for claim in claims]
assert truth == [False, False, True, False, False]
i_only = [n+1 for n, claim in enumerate(claims) if claim[0] == actual[0]]
ii_only = [n+1 for n, claim in enumerate(claims) if claim[1] == actual[1]]
assert i_only == [2, 3] and ii_only == [3, 4, 5]
result = {
    '시각':datetime.now(ZoneInfo('Asia/Seoul')).isoformat(),
    '이전보기의표보존':True, '현재학생용과채택대안보기일치':True,
    '현재학생용과채택대안선지일치':True,
    '문턱의양방향명시':True,
    '이전충분조건만의반모형':{'문턱':1,'I_C최초채택':counter[0],'II_C최초채택':counter[1],
                     '설명':'한 명 문턱도 두 명 이상이면 채택한다는 충분조건은 만족하나 새로 명시한 미달 시 미채택 조건은 만족하지 않는다.'},
    '실제값':{'I_C최초채택':actual[0], 'II_C최종채택':actual[1]},
    'II_고정상태근거':prior['II']['마지막비채택자의_채택이웃수'],
    '선지진리값':truth, 'I만알때남는선지':i_only, 'II만알때남는선지':ii_only,
    '핵심':'②와③은 I의 시점이 같고 II의 결국 채택/계속 미채택만 다르다. 유한한 특정 단계의 미채택만으로②를 배제했다고 보지 않는다.',
    '한계':'기존 모형 검산 결과를 재사용한 국소 검증. 자연어의 의미 전사·기출 대응·실제 풀이 행동은 프로그램의 증명 범위 밖.',
    '통과':True,
}
(ROOT/'확산3대안_검증결과.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(result, ensure_ascii=False, indent=2))
