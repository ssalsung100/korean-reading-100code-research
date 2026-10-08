AGENTS.md, 분석/기본기_연구/CURRENT.md, 분석/기본기_연구/ASTRA_START.md를 먼저 읽어라.

그다음
분석/기본기_연구/review_20260915/implementation_tasks.md
의 "A. Luna에게 전달할 기계적 개선 작업"을 authoritative task specification으로 읽고 그대로 수행하라.

검토 배경이 필요할 때만:
- 분석/기본기_연구/review_20260915/review_report.md
- 분석/기본기_연구/review_20260915/evidence.md
를 참조한다.

중요:
- 새 문항 풀이 금지.
- 새 코드 판정 금지.
- 기존 semantic judgment 수정 금지.
- raw queue/processed의 기존 record 수정·삭제 금지.
- cxresearch/cxcycle/quota/meta cadence 수정 금지.
- prepared membership 수정 금지.
- 이번 작업은 scripts/build_question_views.py와 필요한 열람/검증/색인 코드 및 derived artifacts 개선으로 한정한다.
- source of truth는 raw queue와 실제 source assets다.
- 문항별_완성본은 derived view일 뿐 authoritative source가 아니다.

특히 다음 문제를 반드시 해결하라:
1. competing_codes 등 실제 필드가 기타 필드에 묻히지 않게 정규화.
2. 최초 판단과 후속 수정/유보를 덮어쓰지 않고 함께 표시.
3. CH 같은 빈 선택지, CT 같은 수식/분수 보충자료 누락을 source warning으로 검출.
4. 이미지 존재와 이미지 의미 검증을 구분.
5. sdss_compare=done이지만 실제 태그가 없는 경우를 '비교 완료'로 오인하지 않게 표시.
6. backfill 완료와 의미적 unresolved를 분리.
7. prepared 완료와 legacy 완료를 같은 모집단으로 섞지 않음.
8. 코드별 문항 수뿐 아니라 서로 다른 passage-group 수를 집계.
9. 동일 revision record가 여러 case에 나타나도 record_id 기준으로 중복 합산하지 않음.
10. 같은 입력 스냅샷 재실행 시 동일한 결과가 생성되는지 테스트.

구현 전 queue/processed/source의 hash와 meta_state를 snapshot하고,
완료 후 원본이 본 작업 때문에 바뀌지 않았음을 검증하라.

새로운 semantic stage를 수행하지 말고,
작업 완료 후 연구를 자동 재개하지 마라.

최종 출력:
- 변경 파일
- 생성된 색인/검증 파일
- prepared/legacy 각각의 case 수
- source incomplete 수
- SDSS tag missing 수
- unresolved 수
- 테스트 결과
- 원본 불변 여부