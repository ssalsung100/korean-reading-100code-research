# 패턴 적용 코드북 v0.2

동결: 2026-10-10T17:36:33+09:00

[동결 보고·핵심 해시](freeze_report.md) · [전체 manifest](freeze_manifest.json) · [manifest SHA-256](freeze_manifest.sha256)

|산출물|내용|
|---|---|
|[코드북 JSON](codebook_v0.2.json) / [MD](codebook_v0.2.md)|13개 후보의 상위 원리·하위 조작·조건·행동·가치 평가|
|[장면 매핑 JSONL](event_mapping_v0.2.jsonl) / [표](event_mapping_v0.2.md)|46장면의 복수 pattern_relation·하위형·인용 승계|
|[계수 규칙](counting_rules.md) / [기존 수치 대조](count_reconciliation.md)|E028 제외, 고유 단위·역할별 계수, 목적 표본 제한|
|[사전 판정 프로토콜](application_protocol.md)|적용/비적용/미확인/미분류·대안 풀이·버전 변경 규칙|
|[독립 검증 입력](independent_validation_inputs.md)|제공할 파일과 공개 시점|
|[주석 스키마](annotation_schema.json) / [빈 템플릿](external_annotation_template.json)|후속 외부 표본 기록 형식|
|[관리 메타데이터](management_metadata.json)|표본 ID·hold·값 제거된 노출 이력|
|[검사 결과](validation_report.json) / [입력 목록](input_inventory.json)|구조·계수·보존 확인 및 재사용 근거|

기존 결과의 재사용과 외부 적용 기준 동결만 수행했다. 검증용 6세트 적용·새 지문 제작은 하지 않았다. G095의 노출 이력 메타데이터에 포함된 정답·코드가 재노출된 사실은 관리 기록과 동결 보고에 명시했다.

`python3 verify_freeze.py`는 동결 파일·기존 두 실행 파일의 해시와 계수를 읽기 전용으로 확인한다. build_codebook.py·validate_codebook.py·freeze.py는 동결 후 재작성을 거부한다.
