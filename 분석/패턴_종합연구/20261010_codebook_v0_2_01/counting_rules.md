# 빈도 계수 규칙 — v0.2 동결

집계 함수는 [count_patterns.py](count_patterns.py)이며 입력은 [event_mapping_v0.2.jsonl](event_mapping_v0.2.jsonl)이다. 기존 `pattern_ids` 또는 새 `legacy_pattern_ids`의 단순 빈도를 사용하지 않는다. 후보별 상태, 빈도, 강의 가치, 교재 가치, 창작 가능성은 별도 필드다.

## 관계와 계수

|필드 또는 관계|계수하는 것|계수하지 않는 것|
|---|---|---|
|structure_present|구조를 확인한 고유 passage_id|문항 활용이나 학생 수행의 자동 증거|
|item_utilized|특정 발문·보기·선지에 실제 쓰인 조작의 고유 passage_id·question_id·event_id|정답 선택에 반드시 필요한 행동이라는 주장|
|solution_helpful|근거와 중간 조작이 연결된 유효 풀이의 event_id·question_id|모든 타당한 풀이의 필수성·실제 학생 사용률|
|explanatory_only|별도의 설명 사례 수 및 출처 문항 수|그 패턴의 직접 활용 수|
|boundary_case|별도 경계 목록|출현·문항 활용·유효 풀이 빈도|
|unconfirmed|미확인 목록|적용 또는 비적용 확정 수|
|unclassified|미분류 목록|13개 후보 중 임의의 출현 수|

`pattern_relation`은 복수 값을 허용한다. 구조가 있고 설명 사례이면서 직접 수행의 경계일 수도 있다. 같은 관계의 `decision`은 **그 관계 기록의 근거 상태**이지 모든 역할에서 패턴이 적용된다는 전역 판정이 아니다. 따라서 E028의 `confirmed_inherited`는 구조 설명·경계 관계를 승계했다는 뜻이며 문항 활용 확정이 아니다.

`confirmed_inherited`는 기존 발견용 분석의 판단을 승계한다. 이번 정본 재검증이나 외부 표본 검증 성공이 아니다. `confirmed_new`는 원문 대조, 카드 최소 근거 충족, 정확한 인용 참조, 중간 추론이 저장되어야 계수할 수 있다. `new_evidence.canonical_checked`, `minimum_evidence_met`가 true이고 `references`, `reasoning`이 비어 있지 않아야 함수가 받아들인다. 문자열이 존재한다는 사실만으로 의미적 충족을 보증하지 않으므로 판정 프로토콜도 지켜야 한다. `non_applicable_inherited`, `non_applicable_new`, `unconfirmed`, `unclassified`는 양성 계수에서 제외한다.

새 자료와 기존 발견 자료는 파일·sample_split으로 분리해 집계한 뒤 나란히 보고한다. 합친 수만으로 검증 성과를 보고하지 않는다. 이번 매핑 파일은 전부 발견용 재사용 자료다.

`confirmed_inherited`는 sample_split=discovery인 기존 자료에서만 계수한다. 외부 표본에 이 상태를 복사하여 정본·최소 근거 검사를 우회하면 계수 함수가 제외한다. 외부 표본의 신규 확정에는 confirmed_new와 실제 근거가 필요하다.

## 고유 단위와 중복 제거

1. 지문 단위는 정본에 연결된 `passage_id`를 사용한다. `passage_group`은 관리 좌표이며 다른 alias를 독립 지문으로 늘리지 않는다. 동일성 연결이 불확실하면 미확인으로 남긴다.
2. 문항 단위는 `question_id`, 장면 단위는 `event_id`이다. 같은 문항의 선지 두 개나 장면 여러 개를 여러 문항으로 세지 않는다.
3. 같은 패턴·같은 event·같은 역할이 중복 입력되어도 한 번만 센다. 한 사건에 여러 패턴이 성립하면 각 후보에서는 한 번씩 허용하되, 전체 고유 문항 수는 패턴별 합이 아니라 집합의 합집합이다.
4. 정답 결정, 비정답 검토, 보조 활용은 구별해 보존한다. 세 역할 모두 특정 선지에서 실제 활용되면 item_utilized가 될 수 있다. AA④의 활용이 AA①의 정답 경로 전체를 설명한다는 뜻은 아니다.
5. 선택한 오답을 설명하는 데 유용함, 문제에서 요구한 실제 조작, 지문이 그 조작을 설명하는 것은 서로 다르다. `solution_helpful`과 `item_utilized`는 자동으로 서로 복사하지 않는다. 이번 기존 장면에서 둘이 겹치더라도 새 표본의 제약이 아니다.

## E028/ZE와 기존 수치 대조

E028은 `legacy_pattern_ids=[P05]`를 유지하면서 `pattern_relation=[structure_present, explanatory_only, boundary_case]`로 기록한다. 구조의 형태는 `structure_mode=설명된 구조`이다. **item_utilized와 solution_helpful은 없다.** 같은 지문의 E030/ZF④·⑤는 문맥을 이용해 해석을 확인하는 보조 활용이므로 두 역할을 유지한다.

P05의 기존 값은 연결 장면 5개, 구조 확인 4지문, 출처 문항 5개, 실제 활용 4지문·4문항이다. v0.2는 이를 그대로 재현해야 한다. E028을 빼도 E030이 같은 G160 지문의 실제 활용 근거이므로 지문 수는 줄지 않고 활용 문항 수만 출처 문항 수와 달라진다. 설명 사례 E028을 직접 활용으로 오인하면 5문항으로 늘어나는 것을 회귀 검사로 막는다.

`evidence_events`는 긍정적 연결 관계(structure_present / item_utilized / solution_helpful / explanatory_only)의 고유 장면 수다. 설명 사례도 포함하므로 이 필드를 직접 활용 빈도로 부르지 않는다. `observed_passages`는 structure_present의 고유 지문 수이며 ‘설명된 구조’도 포함한다. 구체적 구현만 연구하려면 structure_mode를 별도 분리해야 한다. `source_questions`는 긍정 연결의 출처 문항 수, `utilized_questions`는 item_utilized의 문항 수다.

## 해석 제한

표본은 목적 표집한 12지문·39문항이며 모든 원자 장면을 전수 추출한 자료가 아니다. 0은 현재 연결된 근거가 없다는 뜻이지 그 시험·지문에 해당 패턴이 없다는 증명이 아니다. 분모 39로 나눈 백분율을 원 코퍼스 발생률·수능 출제 확률·학생 오답률로 보고하지 않는다. KICE·LEET·MEET는 따로 표시하고 동일 지문의 복수 문항 반복과 독립 지문 반복도 구별한다.
