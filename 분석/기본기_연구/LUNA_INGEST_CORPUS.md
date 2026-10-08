# Luna KICE Corpus Ingestion

이 작업은 semantic research가 아니다.

목적은 현재 저장소에 흩어져 있는 평가원/수능 국어 원자료와 Markdown을
전수 조사하여, 아직 canonical KICE corpus에 들어오지 않은 독서·문학
기출을 찾아 구조화하고, 이후 `cxprepare`가 소비할 수 있도록
`data/kice_passages.jsonl`, `data/kice_questions.jsonl`을 확장하는 것이다.

동시에 앞으로 사람이 기출 Markdown을 다시 찾아다닐 필요가 없도록
연도별 중앙 MD 라이브러리를 구축·갱신한다.

대화 기억보다 저장소의 실제 파일 상태를 우선한다.

---

# 0. 역할 제한

너는 corpus ingestion / source restoration / indexing 담당 Luna다.

다음은 절대 수행하지 않는다.

- 문제 풀이
- 정답 추론
- 100코드 판정
- O1~O8 판정
- 코드 경계 수정
- SDSS 의미 분석
- Astra 연구 결과 수정
- 기존 blind 결과 수정
- 기존 answer_check 수정
- 기존 independent_code 수정
- 기존 sdss_compare 수정

특히 다음 연구 상태는 보호한다.

- data/기본기_연구/astra_handoff_queue.jsonl
- data/기본기_연구/astra_handoff_processed.jsonl
- data/기본기_연구/meta_state.json
- 기존 완료 case 연구 기록

새 corpus가 추가되었다는 이유로
완료 passage/question 수를 증가시키지 않는다.

---

# 1. 현재 canonical 상태 확인

먼저 다음을 읽는다.

- AGENTS.md
- 분석/기본기_연구/CURRENT.md
- data/kice_passages.jsonl
- data/kice_questions.jsonl
- data/기본기_연구/prepared_backlog/sealed/provenance_mapping.jsonl
- data/기본기_연구/prepared_backlog/manifest.jsonl

현재 canonical에 이미 존재하는 시험/지문/문항을
다음 식별자로 set화한다.

- academic_year
- exam_label
- passage_id
- question_id
- question_number

파일명만으로 중복을 판정하지 않는다.

---

# 2. 저장소 전체 원자료 탐색

저장소 전체를 대상으로 다음 확장자를 조사한다.

- .md
- .hwp
- .hwpx
- .pdf
- .json
- .jsonl
- .png
- .jpg
- .jpeg
- .bmp

단 다음 영역은 corpus source 탐색 대상에서 제외한다.

- 분석/기본기_연구의 연구 결과 문서
- prepared_backlog의 생성 결과
- astra/luna queue
- node_modules
- .git
- .venv
- 임시/캐시 디렉터리

특히 이름 또는 내용에 다음이 나타나는 자료를 우선 조사한다.

- 평가원
- 수능
- 모의평가
- 6월
- 9월
- 독서
- 비문학
- 문학
- 국어
- 예시문항

기존에 이미 기출 MD를 연도별로 정리한 디렉터리가 존재하는지도 먼저 찾는다.

이미 실질적으로 동일한 중앙 corpus 폴더가 있다면 새 폴더를 중복 생성하지 말고
그 구조를 확장한다.

없다면 아래 중앙 라이브러리를 사용한다.

`data/기출_MD_정본/`

---

# 3. 중앙 Markdown 라이브러리

기출 Markdown은 앞으로 다음 위치에서 한 번에 찾을 수 있어야 한다.

기본 구조:

data/기출_MD_정본/
├── README.md
├── INDEX.md
├── index.json
├── 연도별/
│   ├── 2017/
│   │   ├── 6월_모평/
│   │   │   ├── 독서/
│   │   │   └── 문학/
│   │   ├── 9월_모평/
│   │   │   ├── 독서/
│   │   │   └── 문학/
│   │   └── 수능/
│   │       ├── 독서/
│   │       └── 문학/
│   ├── 2018/
│   └── ...
└── 미분류/

연도는 academic_year 기준으로 통일한다.

시험명은 가능한 한 다음 값으로 정규화한다.

- 6월_모평
- 9월_모평
- 수능
- 예시문항
- 기타

영역은 최소 다음으로 분리한다.

- 독서
- 문학

화법과 작문, 언어와 매체 등은 발견하더라도
이번 연구 corpus에 자동 편입하지 말고 별도 상태로 기록한다.

---

# 4. 기존 Markdown 중앙화 정책

기존 Markdown 원본은 삭제하거나 이동하지 않는다.

중앙 라이브러리는 사람이 탐색하기 위한 정리된 정본 view다.

기존 MD가 중앙 라이브러리에 없는 경우:

1. 시험 연도/시험 종류/영역을 판별한다.
2. 대응하는 중앙 경로를 정한다.
3. 원본 내용을 보존하여 중앙 라이브러리에 복사한다.
4. source_original_path와 SHA-256을 index.json에 기록한다.
5. 동일 hash 파일이 이미 있으면 중복 생성하지 않는다.
6. 동일 시험·문항인데 내용 hash가 다르면 자동 overwrite하지 않고 conflict로 기록한다.

새로 HWP/HWPX/PDF에서 생성하는 Markdown은
처음부터 이 중앙 라이브러리에 저장한다.

즉 앞으로 사람이 기출 MD를 찾을 때는
`data/기출_MD_정본/연도별/`만 보면 되도록 한다.

---

# 5. HWP / HWPX 판별

`.hwp`라는 확장자만 믿지 않는다.

파일 signature를 확인한다.

ZIP/HWPX 구조라면 HWPX로 처리한다.

legacy OLE HWP라면 단순히 확장자를 바꿨다는 이유만으로
HWPX 변환 완료로 기록하지 않는다.

단 실제 파일이 ZIP/XML HWPX인데 확장자만 `.hwp`인 경우에는
오표기로 판단하여 `.hwpx` 사본을 만들어 사용할 수 있다.

원본 파일은 삭제하지 않는다.

legacy HWP의 경우 현재 환경에서 읽을 수 있는 parser 또는 변환 도구가 있으면 사용한다.

없으면:

`conversion_blocked`

상태로 기록한다.

---

# 6. HWPX 추출 규칙

HWPX는 OCR보다 XML을 우선한다.

ZIP 내부의 다음을 조사한다.

- Contents/section*.xml
- header/footer
- content manifest
- BinData
- 표
- shape
- 그림
- 수식

다음을 보존한다.

- 문단 경계
- 탭 뒤 텍스트
- ①~⑤
- <보기>
- [A], [B]
- ㉠, ㉡
- ⓐ, ⓑ
- 밑줄 범위
- 표 cell
- 병합 cell
- 수식
- 그림 anchor

XML에서 확인 가능한 정보를 OCR로 대체하지 않는다.

---

# 7. PDF

PDF는 HWP/HWPX에 대응 원본이 없거나
시각 자료 검증이 필요한 경우 사용한다.

텍스트 레이어가 있으면 텍스트 레이어를 우선한다.

다음은 page image를 직접 확인한다.

- 그래프
- 표
- 도식
- 선택지 그림
- [A]/[B] 괄호 범위
- 밑줄 범위
- 조판에 의해 의미가 정해지는 자료

OCR 결과만으로 숫자·선지·기호를 확정하지 않는다.

---

# 8. 시험 inventory 작성

발견한 모든 평가원/수능 자료를 시험 단위로 inventory한다.

각 시험마다 다음 상태를 기록한다.

academic_year
exam_label
reading_source_present
literature_source_present
reading_md_present
literature_md_present
canonical_reading_present
canonical_literature_present
question_range
source_paths
md_paths
visual_assets
issues

저장 위치:

`data/기출_MD_정본/index.json`

사람용 표:

`data/기출_MD_정본/INDEX.md`

README에는 이 디렉터리가
“연도별 평가원/수능 국어 Markdown 중앙 탐색 위치”임을 명확히 적는다.

---

# 9. 기존 canonical과 대조

각 지문/문항을 현재:

- data/kice_passages.jsonl
- data/kice_questions.jsonl

과 비교한다.

다음이면 이미 canonical에 존재한다고 본다.

시험 식별 + 문항번호 + passage/question 내용이 동일하거나
기존 canonical provenance가 정확히 일치함.

파일명이 다르다는 이유로 새 문항으로 만들지 않는다.

반대로 원자료 또는 MD에는 존재하지만 canonical에 없는 경우
신규 ingestion candidate로 분류한다.

---

# 10. staging 우선

신규 발견 내용을 즉시 canonical에 append하지 않는다.

먼저 다음 staging 파일을 사용한다.

data/corpus_ingest/staging_passages.jsonl
data/corpus_ingest/staging_questions.jsonl
data/corpus_ingest/ingest_inventory.json
data/corpus_ingest/INGEST_REPORT.md

디렉터리가 없으면 생성한다.

staging에는 source provenance를 반드시 포함한다.

최소 provenance:

- source_path
- source_type
- academic_year
- exam_label
- question_number
- extraction_method
- source_hash
- visual_asset_paths
- source_confidence

---

# 11. 신규 passage/question 구조화

기존 `data/kice_passages.jsonl`,
`data/kice_questions.jsonl` schema를 그대로 따라라.

새 schema를 만들지 않는다.

신규 문항은 반드시:

- passage 완전
- stem 완전
- choices 완전
- 선택번호 정확
- question number 정확
- 시험 연결 정확
- passage ↔ question mapping 정확

해야 한다.

답이 원자료에서 기계적으로 확인되지 않으면
답을 추론해서 채우지 않는다.

---

# 12. visual asset

문항이 그림·표·그래프·도식을 필요로 하면 실제 asset을 추출한다.

중앙 저장 위치 기본값:

data/기출_MD_정본/assets/<academic_year>/<exam_label>/

파일명에는 가능하면 question number를 넣는다.

예:

Q31_graph.png
Q08_table.png
Q17_figure_1.png

Markdown은 상대경로로 이를 참조한다.

canonical question에도 기존 schema가 visual 정보를 지원하면
그 convention을 따른다.

지원하지 않는다면 별도 provenance/index에 asset을 기록하고,
임의 schema를 canonical에 추가하지 않는다.

---

# 13. MD 생성 형식

기존에 이미 표준 MD 형식이 있으면 그대로 따른다.

없다면 한 지문군당 하나의 Markdown을 기본으로 한다.

파일명 예:

`Q27-32_환율과_통화정책.md`

단 제목을 알 수 없으면 내용을 보고 임의의 문학적 제목을 만들지 말고:

`Q27-32.md`

처럼 중립적으로 저장한다.

MD에는 원문만 보존한다.

추가하지 않는다:

- 해설
- 정답 추론
- 100코드
- Astra 분석
- 출제 의도 추측

---

# 14. 독서와 문학 모두 조사

현재 연구가 독서 중심이라도
중앙 MD 라이브러리는 독서와 문학 모두 정리한다.

다만 `data/kice_passages.jsonl`,
`data/kice_questions.jsonl`의 현재 연구 schema가 독서 전용이라면
문학을 억지로 같은 canonical에 넣지 않는다.

이 경우 문학은 중앙 MD 라이브러리와 inventory까지만 완성하고:

`canonical_ingest_status = unsupported_current_schema`

등으로 보고한다.

현재 canonical schema가 문학도 지원한다면 정상 ingestion한다.

---

# 15. validation

staging 생성 후 다음을 검사한다.

- 기존 canonical과 duplicate 없음
- 신규 staging 내부 duplicate 없음
- 같은 시험/문항번호 collision 없음
- passage/question 참조 무결성
- 선택지 5개 여부
- 비어 있는 stem 여부
- `[A]`, `<보기>` 등 참조 marker가 있는데 source 범위가 없는지
- visual reference가 있는데 asset이 없는지
- academic_year/exam_label 이상 여부
- source provenance 존재
- source hash 존재

하나라도 심각한 오류가 있으면 해당 row는 canonical에 넣지 않는다.

상태:

READY_TO_MERGE
NEEDS_RESTORE
CONFLICT
UNRESOLVED

로 구분한다.

---

# 16. canonical merge

validation을 통과한 `READY_TO_MERGE` 항목만
기존 canonical schema에 맞춰 append한다.

절대 기존 row를 대량 rewrite하지 않는다.

가능하면 append 전:

data/corpus_ingest/backups/

아래에 기존 canonical 두 파일의 timestamp backup을 만든다.

merge 후 다시 duplicate/integrity validation한다.

실패하면 새 append를 성공으로 보고하지 않는다.

---

# 17. 연구 상태 보호

이 ingestion 과정에서는 다음 파일 내용을 변경하지 않는다.

data/기본기_연구/astra_handoff_queue.jsonl
data/기본기_연구/astra_handoff_processed.jsonl
data/기본기_연구/meta_state.json

CURRENT.md에는 필요한 경우
“새 canonical source N건 추가됨, cxprepare 필요”
정도의 기계적 ingestion 상태만 기록할 수 있다.

기존 연구 완료 수는 바꾸지 않는다.

---

# 18. 중앙 MD index

작업 종료 전 반드시:

data/기출_MD_정본/INDEX.md
data/기출_MD_정본/index.json
data/기출_MD_정본/README.md

를 최신화한다.

INDEX.md는 연도별로 다음처럼 사람이 바로 볼 수 있어야 한다.

# 2026

## 6월 모평

### 독서
- Q4~9 — ...
- Q10~13 — ...

### 문학
- Q18~21 — ...
- ...

## 9월 모평
...

## 수능
...

각 항목은 중앙 MD 상대경로 링크를 건다.

없는 자료도 숨기지 말고:

- MISSING_SOURCE
- MISSING_MD
- NEEDS_RESTORE

로 표시한다.

---

# 19. 최종 보고

마지막에 다음을 보고한다.

현재 canonical passage/question 수
새로 발견한 시험 수
새로 발견한 passage 수
새로 발견한 question 수
staging passage/question 수
canonical merge passage/question 수
중복으로 제외한 수
NEEDS_RESTORE 수
CONFLICT 수
UNRESOLVED 수

독서 MD 총 수
문학 MD 총 수
이번에 중앙 라이브러리에 추가한 MD 수
이미지/표/그래프 asset 추가 수

연도별 coverage 요약

다음 `cxprepare`가 준비할 수 있는
새 canonical passage/question 수

그리고 다음 경로를 출력한다.

- data/기출_MD_정본/INDEX.md
- data/기출_MD_정본/index.json
- data/corpus_ingest/INGEST_REPORT.md

semantic research를 수행하지 않았음을 확인한다.