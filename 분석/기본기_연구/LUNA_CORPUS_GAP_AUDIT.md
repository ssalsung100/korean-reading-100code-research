# Luna Corpus Gap Audit

이 작업은 semantic research가 아니다.

목적은 현재 프로젝트의 전체 연구 대상 universe와
현재 canonical corpus를 기계적으로 대조하여,
앞으로 실제로 어떤 시험 원자료를 추가 확보해야 하는지
시험·회차 단위로 정확하게 산출하는 것이다.

문항을 풀거나 100코드를 판정하지 않는다.

---

# 0. 보호 대상

절대 수정하지 않는다.

- data/기본기_연구/astra_handoff_queue.jsonl
- data/기본기_연구/astra_handoff_processed.jsonl
- data/기본기_연구/meta_state.json
- 기존 blind/answer_check/independent_code/sdss_compare
- 기존 완료 문항 수
- 기존 연구 의미 판단

이 작업은 audit/report 전용이다.

---

# 1. 전체 target universe의 authoritative source부터 찾기

현재 프로젝트에서는 약 1,147개 unique question이
전체 연구 대상이라고 사용되어 왔다.

그러나 숫자 1,147을 하드코딩하여 정답으로 취급하지 말고
실제 저장소에서 이 수의 근거가 되는 원장을 찾아라.

우선 조사 후보:

- data/기본기_연구/code_study_candidates_v2.jsonl
- 기타 code_study_candidates*.jsonl
- candidate index
- SDSS 관련 candidate 자료
- KICE/LEET/MEET question index
- DB_자산_인덱스.md
- 새대화용_평가원형_지문문항_생성_인수인계.md
- 연구 계획/진행 기록에서 전체 corpus 수를 설명하는 부분

중복 제거 기준을 확인한다.

가능한 key:

- canonical question_id
- exam family + year + exam + question number
- candidate canonical_connection
- source URL/ID

동일 문항이 여러 코드 후보로 중복 등장할 수 있으므로
candidate row 수를 question 수로 세지 않는다.

최종적으로 다음을 보고한다.

target_unique_questions = N
target_source = ...
deduplication_rule = ...

실제 저장소 계산 결과가 1,147과 다르면
임의로 1,147에 맞추지 말고 차이와 원인을 보고한다.

---

# 2. 현재 canonical corpus 계산

다음을 읽는다.

- data/kice_passages.jsonl
- data/kice_questions.jsonl
- 기타 현재 canonical LEET/MEET corpus가 존재하면 그것도 포함

이번 작업 직전 상태에서 KICE canonical은
2027 자료 ingestion으로 확장되었을 수 있으므로
숫자를 기억에 의존하지 말고 파일에서 다시 센다.

다음 수치를 구한다.

- canonical KICE passage 수
- canonical KICE question 수
- canonical LEET question 수
- canonical MEET/DEET question 수
- 기타 family 수
- 전체 canonical unique question 수

---

# 3. target ↔ canonical exact mapping

전체 target unique question 각각에 대해 다음 상태 중 하나를 부여한다.

## A. CANONICAL_READY
현재 canonical corpus에 정확히 존재.

## B. LOCAL_SOURCE_AVAILABLE
canonical에는 없지만 로컬에 원자료가 존재.

예:
- 검수완료 MD
- HWP
- HWPX
- PDF
- 기존 JSON
- 페이지 이미지

즉 다운로드 없이 ingestion 가능.

## C. LOCAL_PARTIAL
로컬에 자료는 있으나 다음 중 하나 때문에 바로 canonicalization 불가.

- passage 없음
- stem/choices 누락
- 이미지 없음
- [A]/<보기> 범위 없음
- 정답표 없음
- provenance 충돌
- OCR 손상
- variant 불명

## D. EXTERNAL_SOURCE_NEEDED
로컬 저장소에 충분한 원자료가 없어 외부에서 새 자료 확보 필요.

## E. TARGET_MAPPING_UNRESOLVED
target row 자체가 어느 공식 문항인지 확정 불가.

---

# 4. 절대 문항별 다운로드 목록으로 끝내지 말 것

EXTERNAL_SOURCE_NEEDED를 시험 회차 단위로 묶는다.

예:

KICE / 2018학년도 / 6월 모평
missing questions: 15
needed package:
- 문제지 PDF
- 정답표 PDF
priority: HIGH

한 시험 PDF 하나로 여러 문항을 복원할 수 있으므로
다운로드해야 할 "파일 묶음 수"를 계산한다.

가능하면 다음 수준으로 묶는다.

exam_family
academic_year
exam_label
variant
missing_question_count
missing_question_numbers
required_source_types
local_partial_sources
reason
priority

---

# 5. 로컬 파일 전수 재검색

EXTERNAL_SOURCE_NEEDED로 판정하기 전에
반드시 저장소 전체에서 실제 source를 재검색한다.

확장자:

- .md
- .pdf
- .hwp
- .hwpx
- .json
- .jsonl
- .png
- .jpg
- .bmp

다음 디렉터리도 조사한다.

- 고3 기출/
- 자료/
- 평가원 관련 디렉터리
- LEET
- MEET
- DEET
- 기출
- 전사
- 검수완료

단 연구 결과/queue 자체를 source로 오인하지 않는다.

동일 시험 자료가 다른 이름으로 존재할 수 있으므로
파일명만 보지 말고 가능한 경우 내부 제목/학년도/문항번호를 확인한다.

---

# 6. KICE / LEET / MEET를 분리

최종 gap을 반드시 family별로 나눈다.

## KICE

- 수능
- 6월 모평
- 9월 모평
- 예시문항
- A/B형이 있던 연도는 variant 보존

## LEET

언어이해 등 실제 target에 포함된 시험만.

## MEET / DEET

실제 target에 포함된 범위만.

기타 시험 family가 target에 있다면 별도 구분한다.

---

# 7. 연도별 coverage

최종적으로 연도/시험별 표를 만든다.

예:

| family | 학년도 | 시험 | target | canonical | local_ingestable | external_needed | unresolved |
|---|---:|---|---:|---:|---:|---:|---:|

KICE는 가능하면 시험별로 모두 출력한다.

---

# 8. 다운로드 패키지 목록

사람이 실제로 다운로드해야 할 목록을 별도 생성한다.

파일:

data/corpus_ingest/DOWNLOAD_PLAN.md
data/corpus_ingest/download_plan.json

DOWNLOAD_PLAN.md에는 우선순위별로 작성한다.

# Priority 1 — 한 파일로 많은 문항 확보

예:
- [ ] 2014학년도 6월 모평 국어 문제지
- [ ] 2014학년도 6월 모평 국어 정답표
  - 복원 예상: 15문항
  - 현재 로컬 자료: 없음
  - family: KICE

# Priority 2
...

다운로드 source URL을 로컬 metadata에서 확실하게 알고 있는 경우에만 기록한다.
URL을 추측하지 않는다.

---

# 9. ingestion-only 목록 별도 생성

다운로드가 필요 없는 항목은 따로 만든다.

data/corpus_ingest/LOCAL_INGEST_PLAN.md

형식:

시험
source path
복원 가능 문항 수
필요 작업
- MD parse
- HWPX XML extract
- image restore
- answer linkage
등

즉:

"다운로드해야 함"
과
"이미 있는데 ingest만 하면 됨"

을 절대로 섞지 않는다.

---

# 10. 우선순위 계산

다운로드 효율을 위해 다음을 기준으로 정렬한다.

1. 하나의 문제지/정답표로 확보 가능한 target question 수
2. 현재 연구에서 아직 부족한 family
3. provenance가 명확한 공식 시험
4. visual 복원 부담이 적은 것
5. unresolved mapping은 마지막

임의의 숫자 score를 만들 필요는 없다.

HIGH / MEDIUM / LOW 정도의 기계적 우선순위면 충분하다.

---

# 11. 반드시 reconciliation equation을 출력

최종적으로 다음 등식이 성립해야 한다.

TARGET_UNIQUE =
CANONICAL_READY
+ LOCAL_SOURCE_AVAILABLE
+ LOCAL_PARTIAL
+ EXTERNAL_SOURCE_NEEDED
+ TARGET_MAPPING_UNRESOLVED

각 숫자를 출력한다.

합이 맞지 않으면 보고서를 완료 처리하지 않는다.

또 현재 연구 완료 문항 수와 canonical 수는 서로 다른 개념임을 유지한다.

예:

research_completed <= canonical_ready

가 일반적이나 historical exposure / hold 등의 예외를 설명한다.

---

# 12. 출력 파일

반드시 생성:

data/corpus_ingest/CORPUS_GAP_AUDIT.md
data/corpus_ingest/corpus_gap_audit.json
data/corpus_ingest/DOWNLOAD_PLAN.md
data/corpus_ingest/download_plan.json
data/corpus_ingest/LOCAL_INGEST_PLAN.md

CORPUS_GAP_AUDIT.md 첫 부분에는 다음 summary를 넣는다.

Target unique questions:
Canonical:
Already researched:
Local source available:
Local partial:
External download needed:
Unresolved:
Estimated exam packages to download:

KICE:
LEET:
MEET/DEET:
Other:

---

# 13. 최종 터미널 출력

마지막에는 짧게:

Gap audit 완료.

Target: N
Canonical: N
연구 완료: N

추가 다운로드 없이 ingest 가능: N문항
부분 자료 보유: N문항
외부 원자료 필요: N문항
mapping unresolved: N문항

실제 다운로드 예상 시험 묶음:
KICE N회
LEET N회
MEET/DEET N회
기타 N회

가장 먼저 확보할 10개 시험:
...

보고서:
...

semantic research를 수행하지 않았음.

형식으로 종료한다.
