import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write,candidate
from resume_support_live import finish
assert not any(r['audit_id']=='QBF01-AUDIT017' for r in rows(OUT/'semantic_sample_audits.jsonl'))
assert not any(r['amendment_id']=='QBF01-AMD047' for r in rows(OUT/'scene_amendments.jsonl'))
qs=rows(OUT/'current_question_reviews.jsonl')
batch=[r for r in qs if r['batch_number']==17]
assert len(batch)==40
ss={s['event_id']:s for r in qs for s in r['scenes']}
candidate('BFP014','순유입의 개선과 보유량의 절대 증가를 구별',
 '유입과 유출 변화가 순유입을 높이는 방향임을 확인한 뒤,그 사실이 보유량의 전후 증가를 보장하는지 초기 순유입과 기간의 기준을 확인한다. 덜 감소함과 실제 증가함을 구별한다.',
 ['보유량이 일정 기간의 유입－유출에 따라 변하고,처치가 유입·유출의 방향을 바꾼다는 모형이 있어야 한다.','비교 대상이 무처치 대비인지 처치 전 보유량 대비인지 명시하거나 복원해야 한다.','현재 BHM 한 문항의 사후 충분성 점검에서 도출. 최초 실제 풀이 행동·반복 검증 후보로 확정하지 않는다.'],
 '순변화는 항들의 크기를 알아 합계의 부호를 계산하는 작업이다.여기서는 순유입의 개선 방향만 주어진 상태에서 기준 순유입의 부호 공백을 찾는다.조건부방향은 변화 방향의 전파,격차개별증감은 두 값과 그 차이의 변화 비교이므로 현재로서는 독립 단일 후보로 두고 향후 통합 여부를 검토한다.')
eid='QBF01-U0391-Q03-S02';old=ss[eid]['pattern_connections'];assert old==[]
new=[{'pattern_id':'BFP014','case_specific_fit':'저장 증가·자극분해 감소는 순유입 개선이나,투여 전후 보유 지방량 증가에는 기준 순유입·초기 균형 등의 연결이 필요하다.','definition_source':str(OUT/'new_pattern_candidates.jsonl'),'definition_reused':True}]
# 경로 표기는 다른 신규 후보와 동일하게 저장소 상대 경로로 둔다.
new[0]['definition_source']='분석/패턴_종합연구/20261012_question_backfill_01/new_pattern_candidates.jsonl'
append('scene_amendments.jsonl',[{'amendment_id':'QBF01-AMD047','event_id':eid,'reason':'이번 배치 귀납에서 BHM 사후 충분성 점검의 순유입/보유량 구별을 독립 단일 후보 BFP014로 등록. 추론·공식답·최초풀이 상태는 불변.','changes':[{'field_path':'pattern_connections','old_value':old,'new_value':new}]}])
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV061','pattern_ids':['BFP014','순변화','조건부방향','격차개별증감'],'evidence_event_ids':['QBF01-U0391-Q03-S01','QBF01-U0391-Q03-S02'],
 'finding':'BHM에서 저장 증가와 분해 감소는 같은 방향으로 순유입을 개선한다.하지만 투여 전8-5-5=-2,후8.5-4.5-5=-1이면 보기의 기초분해 고정을 만족하면서 보유량은 계속 감소한다.증가시키는 효과와 전후 절대 증가가 다르다.',
 'decision':'BFP014를 BHM 고유1문항·사후 감사에서 발견한 단일 후보로 등록한다.AMD047은 연결만 추가하며 새 문항이나 장면을 더 세지 않는다. 공식①과 성호르몬 투여 가정의 기존 유보를 유지한다. 초기 균형은 연결을 보장하는 충분한 추가 조건 중 하나이지 유일한 필요조건이 아니다.',
 'next_counterexample':'같은 기간의 무처치 상태와 비교하면 처치에 따른 상대적 개선은 말할 수 있는지,초기 균형이 없어도 최종 순유입의 양수가 별도로 주어지면 절대 증가가 확정되는지 검토한다. 이후 수요·재고·인구 등 독립 기출에서 실제 같은 연산이 나오는지 확인하기 전에는 반복 패턴으로 승격하지 않는다.',
 'educational_use':'저장되는 양과 줄어드는 양을 먼저 써서 순량을 만들고,증가라는 말의 기준점을 붙인다. 신규 문항에서는 투여 전 균형 또는 무투여 대비라는 조건을 명시해 정답 유일성을 확보한다.'},
 {'development_id':'QBF01-DEV062','pattern_ids':['지지방향','비교변인','강도보존'],'evidence_event_ids':['QBF01-U0371-Q03-S01','QBF01-U0377-Q03-S01','QBF01-U0379-Q02-S01','QBF01-U0390-Q03-S01','QBF01-U0391-Q03-S01'],
 'finding':'BFJ는 가설의 관측 예측을 시험하는 관련성,BGA는 가능한 역사적 저평가 배경,BGE는 복수 논거 중 한 연결의 약화,BHJ는 주장의 규범적 비용을 지적하는 비판,BHM은 관측 차이를 투여 예상으로 옮기는 추론이다.모두 강도의 제한이 있지만 수행하는 증거 작업은 다르다.',
 'decision':'관련성·가능한 설명·부분 약화·비판의 직접성·처치 효과 예측을 하나의 증명 행동으로 통합하지 않는다.BFJ/BGA/BHJ/BHM 유보는 유지하고 BGE는 남은 논거가 있어도 한 논거의 약화가 성립함을 기록한다.',
 'next_counterexample':'가설과 관련된 관측이어도 외기·체격을 함께 바꾸면 유일 인과 식별이 아니다.한 지지 논거를 약화해도 다른 독립 근거가 남을 수 있다.비판이 가능하다는 말이 표적의 실제 주장과 반대되는 전제를 사용할 면허는 아니다.',
 'educational_use':'실험·자료·비판 옆에 무엇을 확인하거나 손상하는가를 적고,관측됨·가능함·필연함·전체 반박됨을 다른 표현으로 남긴다. 출제 시 약화와 반박의 요구 강도를 일치시킨다.'},
 {'development_id':'QBF01-DEV063','pattern_ids':['대립가능성','관계귀속','강도보존','범위이동'],'evidence_event_ids':['QBF01-U0373-Q03-S02','QBF01-U0385-Q01-S02','QBF01-U0393-Q01-S01','QBF01-U0393-Q03-S01','QBF01-U0394-Q01-S02'],
 'finding':'BHS에서는 정확한 부정관계가 명시되어 비명령→소극허용이 성립한다.반면 BFP의 실체 면책은 제소허용·금지 어느 쪽도 결정하지 않고,BGU의 정보 활용 가능성은 모든 선율의 유일 복원 보장이 아니다.BHQ의 기여는 결과 보장이 아니며 BHT의 그대로 복사 부정은 모든 전환 부정이 아니다.',
 'decision':'부정어가 있다는 이유로 모든 사례에 동일한 대우·모순 규칙을 적용하지 않는다.명제 자체의 정확한 부정,다른 판단 대상의 비유도,방법 한정 부정,보장의 부정은 구별한다.BFP·BGU의 공식답 유지와 의미 유보를 동시에 보존한다.',
 'next_counterexample':'BHS에서 단순 양립불가만 주면 둘 다 거짓인 경우가 남아 결론이 달라진다.BFP에 제소 자체를 금지하는 별도 규정이 주어져야 현재 공백이 메워진다.BGU에 조성과 마디 조건이 있는 후속BGW의 제약을 소급하지 않는다.',
 'educational_use':'부정되는 술어·대상·범위를 괄호로 묶고 둘 다 참/둘 다 거짓의 가능성을 확인한다.정답을 정한 뒤 오답을 더 강한 모순으로 설명하지 않는다.'},
 {'development_id':'QBF01-DEV064','pattern_ids':['관계귀속','강도보존','분류기준','규칙우선순위'],'evidence_event_ids':['QBF01-U0370-Q02-S01','QBF01-U0370-Q02-S02','QBF01-U0372-Q01-S01','QBF01-U0372-Q03-S01','QBF01-U0376-Q03-S01','QBF01-U0383-Q03-S01','QBF01-U0386-Q03-S01','QBF01-U0389-Q01-S01','QBF01-U0391-Q01-S02'],
 'finding':'BFF는 정확한 미상 득표율 없이도 제곱합의 상한으로 지수 대소를 확정할 수 있다.BFK의 현재 음 일치와 BFM의 고대 참된 음 확신은 다른 판단이다.BFX 선지번호·BGQ 변수 결손은 공식 원문으로 보완되지만,BHF의 거리와 BHK의 세포/지방량·비례 문제는 원문 표현을 확인해도 의미적 범위가 남는다.',
 'decision':'원문 결손 해소와 해석 공백 해소를 구별한다.BFX/BGQ는 이번 사후 복원,BHS는 기존 독립판정 단계의 복원 승계이다.BGZ의 법 위계는 우선규정 없을 때 보충규정으로 이동하는 규칙우선순위와 같지 않아 이미 저장한 AMD046 제거를 감사에서 승인한다. 후보 정의 원본은 불변이다.',
 'next_counterexample':'미상 분포의 가능한 범위가 비교 대상 지수를 가로지르면 BFF처럼 대소를 확정할 수 없다.직접거리 같은 두 정당에서 방향 효용이 다를 수 있고,동방향 함수가 선형 비례일 필요는 없다.자료가 채워져도 개념의 범위 검사는 별도로 필요하다.',
 'educational_use':'제작 문항은 비교 축·기준 대상을 명시하고,원문 복원에는 보강 전 텍스트와 출처를 함께 남긴다.이름이 비슷하다는 이유만으로 후보를 연결하지 않고 실제 입력·연산·출력을 대조한다.'}
])
cases=['BFF','BFH','BFJ','BFK','BFM','BFP','BFX','BGA','BGE','BGQ','BGU','BGZ','BHF','BHJ','BHK','BHM','BHS','BHT']
sample=[r for r in batch if set(r['case_ids'])&set(cases)]
assert len(sample)==18 and sum(len(r['scenes']) for r in sample)==25
write('audit_017_selected_checks.json',{'scope':'17배치 표본의 수치·명제 관계 점검. 실제 관측 자료를 새로 생성한 것이 아님.',
 'BFF':{'parliament':'25/9','unknown_share_sum':0.1,'unknown_square_upper':0.01,'electoral_lower':'10/3','comparison':'10/3>25/9','context_limit':'보기의 내각 구성 관심은 의도된 참여 가능성 조건으로 해석하며 일반 충분조건으로 확정하지 않음.'},
 'BFK':{'pipe_length':9,'ruler_length':10,'pitch':'초기 기장관>중국음=밀랍관'},
 'BFX':{'distances':'AB4/8,AC3/8,AD2/8,BC7/8,BD6/8,CD3/8','merged':'AD-C3/8<AD-B5/8<BC7/8','choice':4},
 'BHF':{'direct_equal':[1,1],'directional_distinct':[2,0],'official':2,'hold':True},
 'BHM':{'net_before':8-5-5,'net_after':8.5-4.5-5,'rate_improves':True,'absolute_amount_increase_guaranteed':False},
 'BHS':{'permitted_states':3,'not_command_implies_passive_permission':True,'restoration':'이전 독립판정에서 이미 범위 복원; 이번 공식9쪽 재확인'},
 'record_corrections':['AMD046 기존 연결 제거의 적용 확인','AMD047 단일 후보 연결 추가'],
 'pass':True})
append('semantic_sample_audits.jsonl',[{'audit_id':'QBF01-AUDIT017','batch':17,'date':'2026-10-15','sample_case_ids':cases,'sample_questions':18,'sample_scenes':25,'sample_options':90,
 'method':'주 에이전트의 문항 작성 중 직접 읽은 원문·보기·전체 선지·기존풀이에 대한 감사.641~646은 packet 원문과 보기·현행 장면을 다시 대조하고,BFX/BGA/BGE/BGQ/BGU/BGZ 현행 전체 선지 근거와 추론도 재확인.671~680은 이번 연속 작성에서 직접 대조한 기록을 사용.기계적 구간·출처 검사는17배치40문항만 수행.',
 'dimensions':{'중간추론':'BFF 제곱합 상한,BFX 거리 평균,BHF 동일 직접거리 반례,BHM 순유입 개선과 절대량,BHS 부정관계의 포괄성 확인.','전체선지':'표본90선지의 채택·배제 근거를 확인.보기의 하위 명제와 조합 번호를 구별.','원문이력':'BFX/BGQ 신규 파생 복원,BHA/BHC 단위 복원,BHS 기존 복원 승계,BHK 원시험지 표현 확인을 구별.','후보경계':'AMD046 법 위계와 보충 규정 선택 구별. BFP014는 BHM의 사후 충분성 점검에 한정한 단일 후보이며 반복으로 확정하지 않음.','출제활용':'비교 기준·초기 균형·부정 범위·원점/직접 거리·정량 강도를 명시해야 정답 유일성을 검토할 수 있음.'},
 'findings':[{'cases':['BFJ','BGA','BHJ','BHM'],'issue':'관련성·가능한 설명·비판·처치효과의 증거 강도','resolution':'유보와 추가 전제 보존.DEV062.'},{'cases':['BFP','BGU','BHS'],'issue':'비유도와 반대 명제 확정의 구별','resolution':'BHS만 명시된 정확한 부정관계.다른 사례는 각 범위를 보존.DEV063.'},{'cases':['BFX','BGQ','BHS','BHK'],'issue':'원문 복원 시점과 의미 공백','resolution':'신규 해소·기존 해소 승계·원문 표현 자체의 유보를 분리.DEV064.'},{'cases':['BGZ','BHM'],'issue':'후보 경계','resolution':'AMD046 제거 적용 확인,AMD047로 단일 BFP014 연결.'}],
 'decision':'17배치40문항·52장면 저장과 표본 감사·귀납 완료.누적680문항1065장면,유보38문항.중대한 진행 차단 오류0.681부터18배치 계속.',
 'unresolved_blocking_error_count':0,'limitations':'표본외 의미 무오류 보장이나 공식 정답표 독립 전수 검증 아님.보호 원장 전수 해시·다른 모델 호출·Git push 없음.'}])
all_cases=[r['case_ids'][0] for r in batch]
finish('audit_017.py',all_cases,['17배치18문항25장면90선지 표본 감사·DEV061~064·BFP014단일후보·AMD047. 전체17배치40문항 기록 검사.681부터 계속.'])
c=json.loads((OUT/'checkpoint.json').read_text())
assert c['reviewed_questions']==680 and c['new_scene_count']==1065
c.update(last_saved_author='author_017m.py',last_saved_audit='audit_017.py',next_sample_audit_at=720)
write('checkpoint.json',c);write('batch_017_checkpoint.json',c)
p=json.loads((OUT/'continuous_research_progress.json').read_text());p.update(last_saved_author='author_017m.py',last_saved_audit='audit_017.py',next_sample_audit_at=720);write('continuous_research_progress.json',p)
write('batch_017_validation.json',json.loads((OUT/'audit_017_validation.json').read_text()))
print('17배치 감사 완료.681부터 계속.유보38.신규BFP014는단일사후후보.')
