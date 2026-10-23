"""계속 연구의 저장 검증·현재 위치 기록. 배치 완료로 종료하지 않는다."""
import json
from backfill_io import OUT,rows,write
from resume_support_20261015 import guard,prior,finish as previous_finish

def finish(author,cases,notes=()):
    previous_finish(author,cases,notes)
    c=json.loads((OUT/'checkpoint.json').read_text())
    audits=rows(OUT/'semantic_sample_audits.jsonl');last=max(a['batch'] for a in audits)
    amendments=OUT/'audit_amendments.jsonl'
    if amendments.exists():
        for a in rows(amendments):
            target=next(r for r in audits if r['audit_id']==a['audit_id'])
            for change in a['changes']:
                assert target[change['field']]==change['old_value']
                target[change['field']]=change['new_value']
        write('current_semantic_sample_audits.json',{'basis':'semantic_sample_audits.jsonl + audit_amendments.jsonl; 최초 감사 기록 보존','audits':audits})
        c['audit_current_view']='current_semantic_sample_audits.json'
        c['audit_amendments']='audit_amendments.jsonl'
    c.update(last_saved_audit=f'audit_{last:03}.py',next_sample_audit_at=(last+1)*40,latest_session_progress='continuous_research_progress.json',continuation_policy='배치·임의응답작업예산을종료사유로삼지않고다음문항계속. 실제환경제한·사용자중단시저장위치보존.')
    write('checkpoint.json',c)
    write('continuous_research_progress.json',{'status':'계속 진행 중','start_reviewed':646,'start_scenes':1022,'current_reviewed':c['reviewed_questions'],'current_scenes':c['new_scene_count'],'added_questions':c['reviewed_questions']-646,'added_scenes':c['new_scene_count']-1022,'last_saved_author':author,'next_order':c['next_order'],'next_question':c['next_question'],'next_cases':c['next_case_ids'],'next_sample_audit_at':c['next_sample_audit_at'],'read_but_not_saved':[],'other_models_called':False})
    write('session_handoff_20261015_05.json',{
        'status':'연속 연구 중 자동 갱신하는 재개 기록; 중단 보고 아님',
        'authoritative_state':'checkpoint.json 및 current_question_reviews.jsonl. 이 기록보다 실제 원장 우선.',
        'reviewed_questions':c['reviewed_questions'],'new_scene_count':c['new_scene_count'],
        'remaining_questions':c['target_count']-c['reviewed_questions'],'by_exam':c['by_exam'],
        'last_completed_question':next(r['unique_question'] for r in reversed(rows(OUT/'raw_question_reviews.jsonl'))),
        'last_saved_script':author,'last_validation':author.replace('.py','_validation.json'),
        'next_order':c['next_order'],'next_question':c['next_question'],'next_cases':c['next_case_ids'],
        'last_audited_batch':last,'next_sample_audit_at':c['next_sample_audit_at'],
        'last_development':rows(OUT/'pattern_development.jsonl')[-1]['development_id'],
        'resume_command':f"python3 분석/패턴_종합연구/20261012_question_backfill_01/backfill_io.py packet {c['next_order']} 3",
        'new_candidate':['BFP014: 순유입 개선과 보유량 절대 증가 구별. BHM 한 문항의 사후 충분성 점검 후보. 반복 확정 아님.','BFP015: 입력 구조가 검사 조건의 중복을 만드는지 확인. BJE 한 문항 후보. 비순환성으로 방문길이5가 전체5정점 포함을 함축하며 순환 반모형으로 일반화를 제한.'],
        'corrections':['AMD046 BGZ의 규칙우선순위 과잉 연결 제거','AMD047 BHM 기존 장면에 BFP014 연결 추가','AUDAMD001 감사017 서술52장면→실제51장면. 누적1065·표본25·실제집계는불변. current_semantic_sample_audits.json 참조.'],
        'source_history':['BFX 공식 선지번호 대조·파생본: 이번 사후 해소','BGQ 공식 식·변수 복원·파생본: 이번 사후 해소','BHA/BHC 공식 단위μm 파생복원','BHS·BIQ[A]는 기존 독립판정에서 해소된 범위복원 승계','BHK③⑤ 표현은 공식 원문에도 존재하여 교정하지 않음','BIK 그래프·BIU 세포도식 직접 확인; 원문 수정 없음','BJA/BJF/BJR/BJX/BKK 인라인·발문 기존 복원 승계','BKE 기존 눈금 잘림 판독 제한 보존. 이번 현행 이미지 및 공식2019홀수형5쪽9번에서10nm 확인. 원이미지 수정 없음. BKE_scale_review.json 참조.'],
        'audit_followup_topics':['BIA 수정허용의 거래 증가 가능성/주된 제도예측 구별','BID 분모 감소만으로 비율 증가 미보장·분자조건·0분모','BII 동일 담보가치 정책 효과와 전후 실제한도 구별','BIN 자손자격제재와 본인형벌·유죄절차의 구별','BFP015 다른 기출의 독립 재현 및 비순환성 이외 검사 함축 조건 탐색'],
        'unresolved_questions':sum(x['unresolved_questions'] for x in c['by_exam'].values()),
        'read_but_not_saved':[],'this_save_notes':list(notes),
        'execution':'주 에이전트 직접 의미 판단. 신규 blind·다른 모델 호출·Git push 없음. quota 수치 미노출, 실제 emergency 경고 없음.',
        'preservation':'현재 작업폴더만 쓰기. 원문·기본기 raw·기존616장면/95후보/동결코드북/processed/CURRENT 불변. G024/G370 hold 유지.',
        'next_procedure':f"기저장 author/audit 재실행 금지. resume_support_live.guard/prior/finish를 사용해 새 author 작성→preflight 인용검사→한 번 실행→종료와 validation 확인.{c['next_sample_audit_at']}에서{last+1}배치감사 후 후속문항 계속.",
        'continuation':'배치·임의 응답작업예산은 종료 사유 아님. 실제 환경 제한 또는 사용자 중단 전 계속.'})
