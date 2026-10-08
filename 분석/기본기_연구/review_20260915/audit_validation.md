# 사후 semantic audit 완료 검증

검증일: 2026-09-15. 범위는 `ASTRA_SEMANTIC_REVIEW_PROMPT.md`가 지정한 완료 anchor에 대한 사후 감사다.

## 결과

| 항목 | 결과 |
|---|---|
| 사례별 직접 원문 검토 및 상세 evidence record | 지정 21개 case 전부 포함, 중복 case 0 |
| 서로 다른 passage group | 15개; manifest와 각 evidence record의 group 일치 |
| 감사 전 단계 완료 | 21개 모두 기존 blind/answer_check/independent_code/sdss_compare의 done 기록 존재 |
| 새 raw | depth_backfill 6건 + boundary_revision 2건 = 8건 |
| queue | 기존858건 → 현재866건, record_id 중복0 |
| 원문·보충·상태 snapshot | 30개 파일 대상 |
| 기존 queue 보존 | 최초1,266,677바이트 prefix의 SHA-256 일치 |
| 그 외 snapshot 보존 | 대상 source·보충 파일, manifest, CURRENT, meta_state의 크기·SHA-256 일치; processed는 기존858건 prefix 보존 후 새8건을 의도적으로 append |
| 상세 JSON과 실제 원장 | raw_batches의8개 record가 실제 append된 record와 객체 전체 일치 |
| 원장 근거 연결 | 모든 source_record_ids 실재 확인 |
| 사례별 필드 | 발문·대상·근거 위치·증거 종류·기존 코드 층·강한 경쟁·경쟁 관계 존재 확인 |
| CT 산술 재계산 | 노력 상승100/700=1/7; 노력 무관300/700=3/7 |
| EF 그림 | 주 에이전트 직접 판독; 목적·실제 밑줄·선지 위치 확인 |
| processed | 기존858건 prefix 보존 + 새 raw 8건 반영 = 866건; pending 0건 |
| 새 corpus/strict blind 성과 | 0건 |

기존 queue prefix SHA-256:

`a4c2ef4ca60189db3f819fb21730782fc1c2e9051f65814dbe08ce2e565866b6`

기존 processed SHA-256:

`bc01e91bd3d8252fdc5bbac950c5683ea76013de90772cafff26a875df3e761d`

snapshot은 [audit_baseline.json](audit_baseline.json)이다. 후처리 전용 검증은 queue prefix·source/manifest/meta 상태의 불변과 processed 8건 append를 별도로 확인했다. snapshot 당시 processed 전체 해시와 현재 해시는 의도된 append 때문에 다르다. 원문 불변 검사는 snapshot에 명시된 대상에 한정한다. 전체 저장소 파일 전부에 대한 해시 감사라는 뜻은 아니다.

## 의미 검토의 한계

GC② 상세 문리 해석, CT 공식 원 배포본 직접 대조, 어휘 사전 뜻 구획, 코드 원저자 정의·유일 주 우선순위는 유보했다. 기계적 필드 검증 통과나 정답 기록 일치는 이 유보의 해소를 뜻하지 않는다.

CT 수치는 기존 XML equation supplement를 사용했다. EF 그림은 로컬 HWPX 렌더의 크롭을 확인했으며, 공식 원 배포본이나 고해상도 원본 확인으로 표현하지 않았다. 문항별 완성본의 누락 내용을 의미로 추측해 채우지 않았다.

보고 중 잠정 수량 표현이 있었으나 최종 manifest 집계는 **21문항·15개 지문 그룹**이다. O1~O8의 독립성·완전성 및 외부 검증 성공을 주장하지 않는다. 비교별 복제본과 최소 변형을 새 표본으로 합산하지 않았다.

## 종료

새 raw만 append했고 기존 판정·진행 상태는 소급 수정하지 않았다. 후속 기계 sync에서 새 raw 8건을 processed ledger와 기존 절차 문서에 반영했고, 문항별 파생 뷰를 재생성했다. 현재 queue 866건·processed 866건이며 pending raw는 0건이다. 이번 작업은 새 passage group을 완료하는 연구 재개가 아니므로 신규 group 완료/정기 meta cadence를 만들지 않았다. `meta_state.json`의 corpus 수치와 `meta_induction_count=10`, `meta_due=false`, `manual_parity_audit_due=false`는 그대로다. `수행연산_후보_v1.md`의 의미 내용은 수정하지 않았다.
