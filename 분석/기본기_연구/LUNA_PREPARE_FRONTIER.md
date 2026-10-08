# Luna Prepared Backlog Preflight

이 작업은 semantic research가 아니라 다음 Astra 연구를 위한 기계적 corpus preparation이다.

먼저 다음을 authoritative instruction으로 읽어라.

1. AGENTS.md
2. 분석/기본기_연구/CURRENT.md
3. 분석/기본기_연구/LUNA_HANDOFF_START.md
4. 필요한 경우 기존 prepared_backlog manifest와 source/provenance schema

대화 기억보다 repository state를 우선한다.

## 목적

CURRENT의 다음 미연구 frontier부터 가능한 한 연속된 30개 passage group을
Astra가 즉시 blind 연구할 수 있는 상태로 준비한다.

단, 원천 corpus가 부족하면 가능한 범위까지만 준비한다.

## 절대 금지

- 문제를 의미적으로 풀이하지 말 것
- 정답을 추론하지 말 것
- 100코드를 새로 판정하지 말 것
- O1~O8 또는 수행연산 가설을 적용하지 말 것
- 기존 blind/answer_check/independent_code/sdss_compare를 수정하지 말 것
- astra_handoff_queue.jsonl을 semantic record로 추가하지 말 것
- astra_handoff_processed.jsonl을 수정하지 말 것
- CURRENT의 연구 완료 수를 증가시키지 말 것
- meta_state의 corpus 진행 수치나 cadence를 변경하지 말 것
- 답/SDSS/기존 해설/기존 코드 판정을 blind packet에 넣지 말 것

## 기본 준비

각 passage group에 대해 기존 저장소의 정본 자료와 색인을 이용하여:

1. 다음 미연구 case/group인지 확인
2. 기존 연구 case와 중복 여부 확인
3. group_case_ids 확인
4. blind packet 생성/검증
5. sealed answer/SDSS packet 생성/검증
6. provenance 보존
7. 기존 manifest schema를 유지해 등록

blind packet에는 오직 blind-safe 자료만 들어간다.

sealed에는 확인된 공식 답과,
기존 색인에서 기계적으로 정확히 연결 가능한 SDSS 정보만 분리한다.

SDSS linkage가 없거나 불확실하면 빈 값으로 남긴다.
의미적 유사성으로 태그를 추정하지 않는다.

## KICE 문학 source extension

기존 KICE 독서 canonical에 없는 문학 target은 다음 authoritative mapping에서만 읽는다.

`data/corpus_ingest/kice_literature_local_audit_target_mapping.json`

후보 조건은 `source_status=LOCAL_COMPLETE`, `preparation_status=READY_LOCAL_LITERATURE_SOURCE`, `additional_download_required=false`이다. 이미 sealed provenance/answer, 기존 blind case, queue 또는 연구 기록에 candidate가 있으면 중복 준비하지 않는다.

문학 target은 중앙 MD(`central_md_path`)를 실제 지문군 source로 사용한다. MD의 문제편 블록에서 공통 지문, 작품 구획, 산문·운문 구분, `[A]`·`[B]`, `㉠`·`㉡`, `<보기>`, 발문, ①~⑤ 선택지를 보존하여 blind source의 기존 허용 필드(`passage_text`, `stem`, `choices`)에 담는다. 작품 구조를 독서 canonical passage로 병합하거나 평탄화하지 않는다.

문학 blind source에도 `blind_only`, `passage_group`, `case_id`, anonymous `provenance`만 유지한다. source path, 학년도, 시험명, candidate_id, 작품명, SHA-256, official answer path는 blind JSON에 넣지 않고 sealed provenance에만 둔다. sealed mapping의 `source_role`은 `literature_source`, `source_type`은 `mother_tong_hwp_or_hwpx_transcription`으로 기록한다. 공식 답은 mapping의 `official_answer_source_path`만 연결하며, 마더텅 해설·정답은 사용하지 않는다.

공식 답안표가 기계적으로 정규화되어 있는 경우 `자료/평가원_정답표/normalized_answer_keys.json`에서 해당 공식 PDF의 답을 sealed answer row에만 기록한다. 정규화되지 않은 경우에는 답을 추정하지 않고 null로 둔다.

문학 source에 실제 그림·표 참조가 있고 blind-safe asset이 없으면 `NEEDS_RESTORE` 또는 `UNRESOLVED`로 둔다. 중앙화된 현재 45문항은 target block에 필요한 visual reference가 없으므로 asset 없이 READY로 준비할 수 있다.

## 강화된 source / visual preflight

각 case를 prepared로 올리기 전에 반드시 다음을 실제로 검사한다.

### 텍스트
- passage 완전성
- stem 완전성
- choices 개수와 번호 매핑
- HTML escape/OCR 손상
- 분수, 수식, 첨자, 특수기호 손상
- ㉠/㉡/ⓐ/ⓑ 등의 지시 대상
- <보기>의 전체 범위
- [A], [B] 등 지정 범위의 실제 시작/끝
- 밑줄 표시의 실제 범위

### 시각자료
본문/발문/선지가 그림·그래프·표·도식을 참조하는지 검사한다.

참조한다면 실제 asset이 blind packet에 존재하는지 확인한다.

특히:
- 공통 passage 그림
- <보기> 그림
- 선지별 그림/그래프
- 표
- 좌표축/범례/라벨
- A~E 등 위치 기호
- 선택번호와 그림의 대응
- 수식 이미지

`visual_placeholder=false` 같은 메타데이터만 믿지 말고
실제 문제 구조와 asset 연결을 확인한다.

필요한 asset이 빠졌다면 가능한 경우 로컬 정본
(PDF/HWPX/기존 canonical source)에서 blind-safe하게 복원한다.

복원 시:
- 답/해설을 이용하지 않는다.
- 원본 위치/provenance를 기록한다.
- 로컬 편집본과 공식 원배포본의 차이를 구분한다.
- 의미 판단은 하지 않는다.

## READY 판정

아래를 모두 만족하는 group만 Astra가 연구할 수 있는 prepared 상태로 둔다.

- passage/stem/choices가 완전
- 모든 지시 범위가 복원됨
- 필요한 시각자료가 존재
- 선택번호↔시각자료 대응 확인
- blind/sealed 분리 확인
- 기존 연구와 중복 아님

문제가 남은 group은 prepared로 위장하지 않는다.

기존 repository schema와 convention에 따라 복원 대기 상태로 남기고,
보고에서는 다음 중 하나로 구분한다.

- READY
- NEEDS_RESTORE
- UNRESOLVED

새 manifest schema를 임의로 만들지 말고 현재 저장소의 기존 필드와 convention을 사용한다.

문학 신규 case의 누수·중복·SHA-256·중앙 MD·공식 정답표 연결은 `python3 scripts/verify_literature_prepared.py`로 별도 검증한다. `scripts/verify_prepared_backlog.py`의 historical warning은 신규 문학 case 오류와 분리해 보고한다.

## 기존 상태 보존 검증

작업 전후 다음을 확인한다.

- astra_handoff_queue semantic 내용 불변
- astra_handoff_processed 불변
- meta_state corpus 완료 수 불변
- CURRENT 연구 완료 frontier 불변
- 기존 blind/sealed 파일 내용 불변
  (새 preparation 파일 추가는 허용)

## 완료 보고

마지막에 다음만 요약한다.

- 시작 frontier
- 검사한 passage group 수
- 새 READY passage group 수 / case 수
- NEEDS_RESTORE group과 이유
- UNRESOLVED group과 이유
- 복원한 visual/source asset 목록
- SDSS linkage 연결 case 수
- SDSS linkage 미연결 case 수
- 다음 preparation frontier
- Astra가 즉시 연구 가능한 첫 READY group
- semantic research를 수행하지 않았음을 확인

준비만 완료하고 종료한다.
Astra 연구를 시작하지 않는다.
