"""사용자 명시 중단 요청에 따라 현재 저장 상태와 다음 재개 위치만 보존한다."""
import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,write,rows

name='session_handoff_20261015_06.json'
if (OUT/name).exists():
    raise RuntimeError('기존 일시중단 인계 덮어쓰기 금지')
cp=json.loads((OUT/'checkpoint.json').read_text())
assert (cp['reviewed_questions'],cp['new_scene_count'],cp['next_order'])==(756,1180,757)
assert cp['last_saved_author']=='author_019l.py'
authors=[f'author_019{x}.py' for x in 'cdefghijkl']
validations=[]
for author in authors:
    fn=author.removesuffix('.py')+'_validation.json'
    val=json.loads((OUT/fn).read_text())
    assert val['pass'] is True and not val['errors'],fn
    validations.append({'file':fn,'questions':val['questions'],'scenes':val['scenes'],'options':val['options'],'pass':True})
assert sum(x['questions'] for x in validations)==30
assert sum(x['scenes'] for x in validations)==50
assert sum(x['options'] for x in validations)==150
old=json.loads((OUT/'session_handoff_20261015_05.json').read_text())
handoff={**old,
 'status':'사용자 요청으로 일시중단. 작업 중이던754~756 저장·인용 및 기록 검사 완료 후 중단.',
 'pause_request':'일단 지금 하는거 끝내고 잠깐 스탑',
 'pause_reason':'사용자 명시 요청. 배치 완료·임의 처리 목표·quota 경고에 따른 종료가 아님.',
 'authoritative_state':'checkpoint.json 및 current_question_reviews.jsonl. 이 인계보다 실제 원장 우선.',
 'last_completed_order':756,
 'last_completed_question':'U0432-Q01',
 'last_completed_cases':['BMD'],
 'last_saved_script':'author_019l.py',
 'last_validation':'author_019l_validation.json',
 'reviewed_questions':756,'new_scene_count':1180,'remaining_questions':321,
 'next_order':757,'next_question':'U0433-Q01','next_cases':['BMG'],
 'next_source_exposure':'757 신규 원문·선지·기존 개별 풀이 미열람. 다음 항목의 ID만 checkpoint에서 확인.',
 'read_but_not_saved':[],
 'unresolved_questions':sum(v['unresolved_questions'] for v in cp['by_exam'].values()),
 'by_exam':cp['by_exam'],
 'current_batch':{'batch':19,'orders':[721,760],'saved_questions':36,'saved_scenes':60,'remaining_questions_before_audit':4,'next_audit_at':760,'audit_status':'19배치 미완료로 표본 감사·귀납 아직 미실행. 18배치 감사 완료.'},
 'current_continuation_saved':{'orders':[727,756],'questions':30,'scenes':50,'scripts':authors,'checks':validations},
 'new_candidates_in_this_continuation':[],
 'new_interpretation_records':[
  'BLC_subset_scope_review.json: 다른 전체 유전체의 일부라는 정보만으로 아래 단계 정보의 필연 차이를 증명할 수 없음. ③의 근거 부족과 반대 명제 증명을 구별. 실제 종간 동일성 주장 아님.',
  'BLU_transport_scope_review.json:⑤ 오차 발생의 문맥 모형에 후대 유해물질 이동·검출·미보정 조건이 필요. 공식① 유지, 추가 조건 유보.',
  'BLW⑤ 기존 remaining_uncertainty 승계: R∧S→U와¬U에서R없이¬S만 도출 불가. 관련성충족을 문맥 전제로 수용하며 범위 유보.'
 ],
 'source_history':old['source_history']+[
  'BKO 비판·BKQ 온톨로지·BKU 최근의 극우민족주의·BLG 초봉의 몰락 과정: 기존 공식 HWP 인라인/발문 복원 부록 승계. 이번 원본 수정 없음.',
  'BLR 기존 수식복원 K=mv²/2,U=-GMm/r,E=K+U 및 변수 정의 승계. G467_visual01/02 직접 확인. 거리→중력 약화는 기존 풀이의 배경지식 사용으로 구별. 원궤도 속력식·힘 역제곱식이 원문에 있었다고 하지 않음.',
  'BLV A/B 범위 초기 오류 후 정정 이력 승계. BLW는 정정 부록과 BLV_B_official_bracket_crop.png 직접 확인: B=마지막 문단 전체.'
 ],
 'semantic_revision_history':[
  '이번727~756의 기존 정답 변경 없음. 과거 raw·scene 변경 없음. 인용 preflight에서 발견한 문자열 오기는 raw append 전에 수정.',
  'BLF SDSS 공개 전 독립판정2개 중 후속의 code4 과잉 연결 철회를 보존. 복합 전개 선지의 대상/방법 일부 불일치를 전칭 범위 반례로 분류하지 않음.',
  'BKJ 양의 순효용/최대화 유보는이전author019b 기록 유지. 이번 BLU⑤와BLW⑤ 유보2문항 추가·승계로 총44문항.'
 ],
 'audit_followup_topics':old['audit_followup_topics']+[
  '19배치 BKE10nm 사후판독/기존 제한, BKJ 국소 효용 비교/전역 최대, BLR 원문/배경지식 출처 구별',
  'BKP·BLA 모두 명제의 한쪽 반례와 불필요한 잔여 정보 미확정',
  'BKR 공통 표현/전체 표현력·함축 포함/진포함 비보장, BLC 다른 전체/같은 부분 반모형',
  'BLU⑤ 오염물질 이동 추가조건과 오차 필연 강도, BLW⑤ 결합요건 대우와 관련성 전제',
  'BLX⑤ 부가 속성/활동·경로 구조 구별, BLZ⑤ 모델 확장 필요와 원로그 시간차 계산 가능성 구별',
  'BKL 설명/금융 평가, BLI 병렬 장점/인과, BLK 과세대상·귀착·초과부담·목표 분리',
  'BLF 기존판정 수정 승계, BLH 거부순간/뒤수령 및 오해추측/실제동기, BMD 형식적 일관성/내용 정당성'
 ],
 'resume_command':'python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet 757 3',
 'next_procedure':'사용자가 재개하면 checkpoint 확인→757 BMG부터 기존풀이 활용 사후보완. 다음 신규 author는author_019m.py(실제 존재 확인). 기존author/audit 재실행 금지.760저장 후19배치 표본 감사·귀납·해당배치 기록 검사,이후761계속.',
 'pause_files':[name,'checkpoint.json','continuous_research_progress.json'],
 'this_save_notes':['사용자 요청에 따라 현재읽은754~756까지 완료. 다음757의 분석을 시작하지 않고 일시중단.'],
 'continuation':'현재 사용자 요청으로 정지. 사용자의 이후 재개 지시가 오면 연속 연구 정책으로 돌아감.'}
write(name,handoff)
cp.update(status='사용자 요청으로 일시중단',latest_session_handoff=name,pause_reason=handoff['pause_reason'],read_but_not_saved=[],resume_command=handoff['resume_command'])
write('checkpoint.json',cp)
progress=json.loads((OUT/'continuous_research_progress.json').read_text())
progress.update(status='사용자 요청으로 일시중단',latest_session_handoff=name,pause_reason=handoff['pause_reason'],read_but_not_saved=[])
write('continuous_research_progress.json',progress)
old.update(status='사용자 요청으로 일시중단; 상세 최신 인계는session_handoff_20261015_06.json',superseded_by=name,read_but_not_saved=[])
write('session_handoff_20261015_05.json',old)
for fn in ['checkpoint.json','continuous_research_progress.json',name]:
    x=json.loads((OUT/fn).read_text())
    assert x.get('next_order')==757
    assert '일시중단' in x['status']
print(json.dumps({'일시중단':True,'검토완료':756,'판단장면':1180,'유보':handoff['unresolved_questions'],'다음':'757 U0433-Q01 BMG','감사시점':760,'최신인계':name},ensure_ascii=False))
