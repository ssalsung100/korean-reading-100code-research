"""Sol이 직접 작성한 판단을 새 실행 폴더에 기록한다."""
from pathlib import Path
import json

RUN = Path(__file__).resolve().parent

def record(group, passage, questions):
    out = RUN / 'analysis'
    out.mkdir(exist_ok=True)
    assert len(questions) == len([p for p in (RUN / 'sources').glob('*.json')
                                 if json.loads(p.read_text())['passage_group'] == group])
    payload = {'passage_group': group, 'passage_analysis': passage, 'questions': questions}
    target = out / (group + '.json')
    assert not target.exists(), '완료한 독립 판단의 덮어쓰기 금지'
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n')
    print(group, len(questions), '독립 판단 저장')

def q(case, answer, confidence, used, process, options, behavior, conditions, forbidden,
      alternatives, application, hold=None):
    return {'case_id': case, 'independent_answer': answer, 'confidence': confidence,
            'answer_status': '판단 보류' if hold else '독립 선택·공식 미대조',
            'hold_reason': hold, 'passage_features_used': used,
            'question_design': process[0], 'reasoning_steps': process[1:],
            'option_judgments': [{'option': i + 1, 'statement_status': x[0],
                                 'evidence_ids': x[1], 'specific_reason': x[2]}
                                for i, x in enumerate(options)],
            'repeatable_action': behavior, 'applicable_when': conditions,
            'do_not_apply_when': forbidden, 'alternative_routes': alternatives,
            'production_implications': application,
            'historical_exposure': '과거 Astra 노출 이력·엄격 blind 별도 제외' if case in ('NK','NL','NM','NN','NO') else '사용자 고지상 과거 노출 없음',
            'current_session_answer_or_pattern_exposure': False}
