# 패턴 적용 코드북 v0.2 동결 보고

동결 시각: 2026-10-10T17:36:33+09:00 (Asia/Seoul)

새 실행 폴더: `분석/패턴_종합연구/20261010_codebook_v0_2_01`

13개 후보의 상태를 보존하고 상위 원리·하위 조작·적용 단위·최소 근거·조건·제외·인접 구별·학생 행동·대안 풀이 허용을 고정했다. 기존 46장면을 매핑했고, 기존 원장·100코드·pilot·application은 변경하지 않았다. 검증용 6세트에는 적용하지 않았다.

## 핵심 파일과 SHA-256

|파일|SHA-256|
|---|---|
|[codebook_v0.2.json](codebook_v0.2.json)|`cb25b7b5438863c4c0f437f5f2e115cc30865183202edd79b0e7a8de5b5c9dff`|
|[codebook_v0.2.md](codebook_v0.2.md)|`70f8dfa698b5901abc94ffd84b4a68ad81bbee396a27b0174e7f4018b29cee27`|
|[event_mapping_v0.2.jsonl](event_mapping_v0.2.jsonl)|`49cc6fb521fb9ac6c44289934740428b48e544f662e55ef4143b61dc7d0de1f5`|
|[counting_rules.md](counting_rules.md)|`4309da1f34d4c1206a3e5303a6e2a00b95dc5854bbdc3a9d850cf63890415e7e`|
|[application_protocol.md](application_protocol.md)|`9c88dc1d2b577f722dfe8669374c0bc8a574259ba79e79c363761a495b9d1be3`|
|[independent_validation_inputs.md](independent_validation_inputs.md)|`d4e08ba3079706983bd49477c6eed7869a2a0974603a385944988439887118cd`|

전체 파일별 해시와 날짜는 [freeze_manifest.json](freeze_manifest.json)에 있다. manifest 자체의 해시는 [freeze_manifest.sha256](freeze_manifest.sha256)에 따로 기록한다. manifest와 그 해시 파일은 자기 참조를 피하기 위해 파일 목록에서 제외한다. Python 캐시는 동결 산출물이 아니다.

## 계수 결과

- pattern_ids가 아니라 pattern_relation과 관계의 근거 상태로 고유 지문·문항·사건을 센다. 같은 사건의 복수 패턴·역할을 허용하되 중복 행은 중복 계수하지 않는다.
- E028/ZE는 P05 구조 설명·explanatory_only·boundary_case로 남기고 item_utilized·solution_helpful에서 제외했다. E030/ZF④·⑤의 보조 활용은 유지했다.
- P05는 연결 장면 5개, 출처 문항 5개, 구조 4지문, 실제 활용 4지문·4문항이다. 모든 후보의 기존 계수 필드와 application의 시험별 활용 수가 일치했다.
- 46장면 중 기존 미분류 12개와 정답 경로 보완 3개는 미분류로 유지했다. 경계·미확인·미분류는 활용 계수에 넣지 않는다.
- 목적 표본의 연결 수이며 원 코퍼스 발생률·출제 확률이 아니다. 강의·교재·창작 가치는 별도 항목으로 기록했다.

## 보류한 경계

P04의 AA 명시 요건/GM 측정 기전/BK 권한·범위, P01의 단항 귀속/원인/관계 양 끝/평가 근거, P03의 역순/연쇄/비율, P07의 처리/기전/역사는 하위형을 유지했다. 외부 전이 전 통합·분할을 확정하지 않는다. S05/P02 중첩과 S01~S06의 단일 지문 잠정 상태도 유지했다. P07 명분/실태 경계는 E032/AJP①, S01 약함/전무 경계는 E014/BK②다.

## 다음 독립 검증의 입력

[입력 목록](independent_validation_inputs.md)에 제공 시점을 고정했다. 코드북·동결 해시·역할 스키마·판정 프로토콜·계수 규칙·값 제거된 관리 메타데이터가 먼저 필요하다. 후속 원문·문항·도표는 정답·기존 풀이·예상 패턴과 분리하여 제공한다. group 최초 풀이 뒤 공식 답, 독립 판단 잠금 뒤 비교 자료를 공개한다. 이번에는 이 자료를 열거나 제공하지 않았다.

## 확인 범위와 제한

카드·역할·계수·범위·두 기존 실행 폴더 37파일의 불변을 검사했다. 검증용 본문·선지는 열지 않았고 정본 원문·원장의 의미적 재검증도 수행하지 않았다. 인용은 application의 교정을 승계하며 GL④ 수식 등 기존 유보를 유지한다. 별도 JSON Schema 엔진은 미실행이며 JSON 구문과 주요 구조·관계 제약은 로컬 assertion으로 검사했다.

**범위 위반 기록:** 노출 이력 메타데이터인 기존 sample_annotations.json을 확인하며 G095/NM의 기존 정답·코드 값이 재출력되었다. 금지된 값의 재노출로 관리 기록에 남겼으며 여기에는 값을 복사하지 않았다. G095는 현재 실행 주체의 미노출 검증에 사용할 수 없다. 다른 검증 세트의 내용·정답·예상 패턴은 확인하지 않았다.

G024/G370 hold를 유지했다. 신규 패턴 강제 통합, 발견용 재풀이, 검증 적용, 새 창작 지문, 다른 모델 호출, Git push는 수행하지 않았다. 동결 이후 수정은 새 버전·새 폴더에서만 한다.
