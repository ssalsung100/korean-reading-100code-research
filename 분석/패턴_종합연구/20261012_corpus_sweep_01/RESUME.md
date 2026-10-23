# 후속 보완 인계

495/495지문1차종합 완료. 지문 미처리0.590고유 문항·616장면.

체크포인트에 다음 지문은 없으며 기존 author 파일을 재실행하지 않는다. `최종_진행보고.md`, `final_scope_summary.json`, `question_coverage.jsonl`부터 읽는다.

후속은1077개 미추출 문항의 추가 장면, `depth_followup_questions.jsonl`의 지정 과제, 미분류15개 기록의 경계 검토다. 겹치는 대상을 합산하지 않는다. `followup_evidence_index.jsonl`의 유보 필드는 자동 해소 판정이 아니다.

지문별 최초 추출은 immutable로 보존한다. 의미 수정은 `scene_amendments.jsonl`, 추가 선지 장면은 신규 별도 보완 원장에 저장해 기존 event ID와 중복되지 않게 한다. group_extractions를 다시 record하여 완료지문을 재처리하지 않는다. G024/G370 hold·기존 raw·processed·CURRENT·Astra 동결 자료는 변경하지 않는다.

8A/7B 층위의 추가 근거는 `layer_evidence_extension.jsonl`까지 적용되어 있다. 원래 `layer_induction.py`만 재실행하면 추가 근거가 빠지므로 현재JSONL을 기준으로 삼는다. 집계 재생성은report.py, 파일·연결 검사는verify_outputs.py다. 모두 완료상태 next_group=null을 처리한다.
