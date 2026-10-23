import sys,json
sys.dont_write_bytecode=True
from backfill_io import OUT,rows,append,write,evidence,BYQ
from resume_support_20261015 import finish
qs={r['unique_question']:r for r in rows(OUT/'current_question_reviews.jsonl')}
ss={s['event_id']:s for s in rows(OUT/'new_judgment_scenes.jsonl')}
assert not any(a['audit_id']=='QBF01-AUDIT013' for a in rows(OUT/'semantic_sample_audits.jsonl'))
assert not any(a['amendment_id']=='QBF01-AMD032' for a in rows(OUT/'scene_amendments.jsonl')),'부분 실행 시 미저장 잔여만 복구'
fixes=[
 ('QBF01-AMD032','QBF01-U0192-Q01-S02','미확정유지','AKQ는 세 명제의 동시 유지 역설과 단순 기술문 환원을 구별한다. 실험 가설의 미입증/부재/대안 확정이라는 기존 D를 모든 부정 추론에 넓히지 않는다. 분기망라와 실제 추론은 보존.'),
 ('QBF01-AMD033','QBF01-U0194-Q02-S02','미확정유지','AKX의 유보는 기준 문구 해석의 논리 방향에 관한 근거 수준이지 실험 가설의 확인 실패가 아니다. 정의방향을 유지하고 미확정유지 연결만 제거.'),
 ('QBF01-AMD034','QBF01-U0191-Q03-S02','누락연결전제','AKP는 배제 논증에 문제를 제기하는 대안 가능성을 고른다. 기존 E의 필수 전제를 요구하는 발문 조건과 다르므로 같은 확정 후보로 직접 계수하지 않는다. 배제 연결에 대한 설명과 지지방향은 보존하고 확장 가능성은 귀납에서 별도 검토.'),
 ('QBF01-AMD035','QBF01-U0193-Q03-S01','누락연결전제','AKV는 명시된 공개 기준에 없는 면제 규칙을 선지가 추가한 사례다. 필수 전제를 선택하는 기존 E와 다르므로 후보 연결만 제거하고 기준내부검사 및 구체 면제 연결 분석은 보존.'),
 ('QBF01-AMD036','QBF01-U0198-Q02-S01','대상인식방식','ALI는 대상 구조와 인식 형식의 호응을 읽는다. 기존 D/E의 중심 사례인 내용어와 실제 인식 행동의 감각/표상/개념 분류를 혼동하지 않는 행동과 동일성이 아직 부족하다. 관계귀속을 남기며 향후 실제 대응 사례에서 통합 가능성 검토.')]
am=[]
for aid,eid,pid,reason in fixes:
 old=ss[eid]['pattern_connections'];new=[p for p in old if p['pattern_id']!=pid]
 assert len(new)==len(old)-1
 am.append({'amendment_id':aid,'event_id':eid,'reason':reason,'changes':[{'field_path':'pattern_connections','old_value':old,'new_value':new}]})
eid='QBF01-U0213-Q02-S02'
am.append({'amendment_id':'QBF01-AMD037','event_id':eid,'reason':'AMZ는 원칙을 유지하며 근거를 새로 설명한다. 기존 이론부분유지 D/E의 선행 가정 반박·명제별 계승/폐기와 완전히 같다고 하기 어렵다. 바뀐 근거/유지된 원칙을 분리하는 속성분리로 연결을 제한하며 구체 추론 불변.','changes':[{'field_path':'pattern_connections','old_value':ss[eid]['pattern_connections'],'new_value':[{'pattern_id':'속성분리','case_specific_fit':'정당화 근거가 바뀐 것과 합의 준수 원칙이 유지된 것을 나눈다.','definition_source':'분석/패턴_종합연구/20261012_corpus_sweep_01/pattern_candidates.json','definition_reused':True}]}]})
append('scene_amendments.jsonl',am)
q=qs['U0213-Q02']
assert not any(a['amendment_id']=='QBF01-QAMD005' for a in rows(OUT/'question_amendments.jsonl'))
append('question_amendments.jsonl',[{'amendment_id':'QBF01-QAMD005','unique_question':'U0213-Q02','reason':'AMZ⑤ 근거의 짧은 단편을 두 판단 원칙의 실제 문장으로 교체해 공통 기능의 참조를 명료화. 정답·추론 불변.','changes':[{'field_path':'option_checks.4.source_evidence','old_value':q['option_checks'][4]['source_evidence'],'new_value':[evidence(BYQ['U0213-Q02'],'형식의 옷을 입지 않은 합의만으로는 소권(訴權)이 생기지 않는다'),evidence(BYQ['U0213-Q02'],'합의는 어떠한 형식의 것이든 준수되어야 한다')]}]}])
assert not any(d['development_id']=='QBF01-DEV044' for d in rows(OUT/'pattern_development.jsonl'))
append('pattern_development.jsonl',[
 {'development_id':'QBF01-DEV044','pattern_ids':['정의방향','필요요건역전금지','분류기준'],'evidence_event_ids':['QBF01-U0191-Q01-S02','QBF01-U0191-Q03-S01','QBF01-U0194-Q02-S02','QBF01-U0213-Q02-S01'],
 'finding':'기준·필요·수용이라는 어휘만으로 필요충분을 정할 수 없다. AKN④는 문두의 규범 전제 복원, AKP④는㉠의 필요성을 인정하면서 충분성만 부정, AKX④는 기준의 충분 방향에 대한 해석, AMZ는 형식 부재의 부족 조건을 각각 사용한다.',
 'decision':'관계의 방향·양화 범위·근거 수준을 따로 기록한다. 특히 AKX의 배제 사례는 ¬H→¬S이며④에 필요한 H→S를 독립적으로 증명하지 않는다. AKN/AKX 공식답을 바꾸지 않고 사후 유보를 유지한다. 기존 정의를 자동 확대하지 않는다.',
 'next_counterexample':'교육용 논리 반례 H=참,S=거짓은 ¬H→¬S와 양립하지만 ¬S→¬H를 깨뜨린다. 실제 인간·로봇의 상태에 대한 경험 주장이 아니다. 감정 있음→수용 의무는 감정 없음→수용 이유 없음의 역이므로 별도 규범 연결이 필요하다.',
 'educational_use':'제작 시 필요한 방향을 직접 제시한다. 학생에게 기준 문장/실제 포함·배제 사례/선지에 필요한 방향을 세 줄로 쓰게 한다. 충분 방향을 빼면 정답이 문맥 추정에 의존하거나 판단 불가능해질 수 있음을 명시한다.'},
 {'development_id':'QBF01-DEV045','pattern_ids':['범위이동','분류기준','관계귀속','포함반례'],'evidence_event_ids':['QBF01-U0187-Q01-S02','QBF01-U0192-Q01-S01','QBF01-U0196-Q02-S02','QBF01-U0197-Q02-S01','QBF01-U0198-Q01-S01','QBF01-U0198-Q01-S02','QBF01-U0199-Q01-S01'],
 'finding':'대표성/전원합의, 방식의 차이/작용 부재, 환원 거부/요인 배제, 좋은 여성상 부적합/나쁜 여성상 전체 확정, 범주 포함/최고 단계, 기능적 내재/사건집합 포함은 모두 표현의 적용 범위를 고정해야 하는 사례다.',
 'decision':'공통 작업은 판단 단위를 먼저 고정함이다. 그러나 대표성은 양화, 방식은 상하위 범주, 최고 단계는 수준, 내재는 기능 구성이라는 관계 차이가 있어 하나의 무차별 패턴으로 통합하지 않는다. ALH는 내부 반례가 명시되어 포함반례를 유지하며 ALK는 사건집합의 상호 포함을 추가하지 않는다.',
 'next_counterexample':'최고 단계의 요건이 기본 범주 전체에 직접 정의되어 있다면 ALH식 내부 반례가 성립하지 않는다. 특정 방식을 제외했는데 다른 방식이 존재하지 않는 완전 정의라면 AKQ식 유보와 달라진다. 모두 가상 경계 검토이며 기출 관측 결과가 아니다.',
 'educational_use':'제작 시 범주명·관계 종류·전체에 부과한 성질과 반례의 실제 소속을 명시한다. 한 오답을 고칠 때 범주명만 교체하여 다른 속성을 과잉 확정하지 않도록 전체 절을 검사한다.'},
 {'development_id':'QBF01-DEV046','pattern_ids':['지지방향','누락연결전제','기준내부검사','강도보존'],'evidence_event_ids':['QBF01-U0191-Q03-S02','QBF01-U0193-Q03-S01','QBF01-U0195-Q03-S01','QBF01-U0195-Q03-S02'],
 'finding':'AKP는 대체 구현의 가능성으로 배제 연결을 약화한다. AKV는 결과 타당성에 의한 과정 공개 면제라는 미제시 규칙을 기각한다. ALB는 실험이 어느 대상·비교 단위의 결론을 강화하는지 확인한다.',
 'decision':'세 사례 모두 연결을 검토하지만 필수 전제 선택, 비판적 대안 제시, 기존 기준의 적용, 실험 강화는 서로 같은 과제로 확정하지 않는다. 기존 누락연결전제 E가 필수 전제 발문을 요구하므로 AMD034/035로 직접 연결을 제거했다. 비필수 발문으로의 범용 확장 가능성은 잠정 검토 사항으로 남긴다.',
 'next_counterexample':'결론에 유리한 대안 하나가 빠졌다고 모든 논증이 반드시 무효인 것은 아니다. ALB의 단일 제거 결과를 모든 수송 경로의 신호 필요성으로 올리면 동반 수송이라는 본문 경로를 놓친다.',
 'educational_use':'대상 결론/증거 대상/조작 조건/기대 결과/실제 지지 강도를 분리한다. 필요 전제 문항은 그 전제의 부정으로 논증 연결이 끊기는지 추가 검토하고, 강화 문항은 단순 관련성과 비교 단위의 일치를 확인한다.'},
 {'development_id':'QBF01-DEV047','pattern_ids':['미확정유지','이론부분유지','대상인식방식','관계귀속','속성분리'],'evidence_event_ids':['QBF01-U0191-Q01-S02','QBF01-U0192-Q01-S02','QBF01-U0194-Q02-S02','QBF01-U0198-Q02-S01','QBF01-U0213-Q02-S02'],
 'finding':'확정하지 않는다는 공통 표현만으로 실험 미입증, 기준 문구의 방향 해석, 명령 형식의 역설을 같은 후보로 연결하기 어렵다. 대상-인식 방식의 호응과 내용어에 현혹된 인식 행동 분류도 차이가 있다. 원칙의 재정당화와 기존 이론 일부 반박도 구별된다.',
 'decision':'AMD032/033/036/037로 직접 연결을 축소하고 실제 추론은 보존한다. AKN은 외적 행동 증거로 내적 경험을 확정할 수 없다는 가설 확인의 한계가 있어 미확정유지 연결을 유지한다. AMZ는 기존 근거의 반박을 추가하지 않고 근거 변화/원칙 유지로 한정한다. 원95 정의 불변.',
 'next_counterexample':'후속 실제 지문이 기존 근거를 반박하고 동일 결론을 독립적으로 재증명한다면 이론부분유지 연결을 다시 검토한다. 대상 관련 단어 때문에 실제 인식 행동을 오분류하는 추가 선지가 있다면 대상인식방식과의 동일성 근거가 강해진다.',
 'educational_use':'후보 이름보다 실제 입력·중간 판단·결론을 먼저 적고 기존 D/E에 맞는지 검사한다. 기존 후보에 억지로 맞추지 못한 세부 구조도 사례별 교육·제작 설명에는 보존한다.'}
])
cases=['AKH','AKN','AKP','AKQ','AKV','AKX','ALB','ALF','ALH','ALI','ALK','AMZ']
sample=[q for q in qs.values() if set(q['case_ids'])&set(cases)]
assert len(sample)==12 and sum(len(q['scenes']) for q in sample)==22
append('semantic_sample_audits.jsonl',[{'audit_id':'QBF01-AUDIT013','batch':13,'date':'2026-10-15','sample_case_ids':cases,'sample_questions':12,'sample_scenes':22,'sample_options':60,
 'method':'주 에이전트가 이번에 직접 읽은 원문·전체 선지·기존 최초/독립/정답 기록과 저장된 현행 문항을 대조. 기존 후보 D/E/F를 읽고 적용 범위 감사. 표본은13배치의 LEET 문항이며 완료 KICE 재분석 없음.',
 'dimensions':{'중간추론':'AKH 준비 조건의 논리합, AKN 규범 전제 복원과 AKP 필요/충분 차이, AKQ 두 명령 분기, AKX 기준 방향, ALB 실험 대상과 세포 종류 비교를 확인.','모든선지':'표본12문항60개 선택행 확인. ALB는 a,b,c 각각의 판단과5개 조합행을 함께 확인. ALF와ALH에서 부적합 배제와 대안 전체 확정을 구별.','후보경계':'AMD032~037로6개 장면 연결 수정. AKN 행동 증거의 비결정성은 미확정유지로 보존하되 AKQ 역설·AKX 기준 해석은 제외.','원문과이력':'기존 최초·공식 답 및 독립 판정 유일성 미확정 보존. AKN/AKX 사후 유보2문항 추가. AMZ⑤ 근거 단편을 실제 두 원칙으로 QAMD005 보강.','교육출제':'가상 조건·논리 반례를 기출 관측과 분리. 국소 수정 후 전체 복합 선지와 정답 유일성을 다시 검토하도록 기록.'},
 'findings':[{'case':'AKQ/AKX/AKP/AKV/ALI/AMZ','issue':'기존 D/E보다 넓은 후보 연결','resolution':'AMD032~037. 실제 추론·정답·원raw 보존.'},{'case':'AKN/AKX','issue':'문맥 복원 전제와 직접 입증된 조건 방향을 구별할 필요','resolution':'공식답 유지하며 비차단 사후 유보2건 보존.'},{'case':'AMZ','issue':'⑤의 근거 인용이 지나치게 짧음','resolution':'QAMD005로 두 원칙 문장에 직접 연결.'}],
 'decision':'13배치 표본 감사·귀납 완료. 중대한 진행 차단 오류 없음. 521번 LEET부터 계속. 표본 외 의미 무오류 보장은 아님.','unresolved_blocking_error_count':0,'limitations':'공식 정답은 기존 대조 기록 활용. 원전 답표 독립 전수 재검증·보호 자산 전수 해시·모델 비교 없음.'}])
finish('audit_013.py',cases,['13배치 표본 감사12문항22장면60선지 완료. AMD032~037 후보 연결6건 축소·교체, QAMD005 AMZ⑤ 근거 보강, DEV044~047 저장. AKN/AKX 추가 유보로 총23문항 유보; 공식답 변경 없음.'])
c=json.loads((OUT/'checkpoint.json').read_text());c['last_saved_author']='author_013k.py';c['last_saved_audit']='audit_013.py';write('checkpoint.json',c);write('batch_013_checkpoint.json',c)
write('batch_013_validation.json',json.loads((OUT/'audit_013_validation.json').read_text()))
h=json.loads((OUT/'session_handoff_20261013.json').read_text());h.update(last_saved_author='author_013k.py',last_saved_audit='audit_013.py',next_author_suggestion='author_014a.py',batch_state='001~013 저장·표본 감사 완료.520문항834장면.521번부터14배치 계속.');write('session_handoff_20261013.json',h)
