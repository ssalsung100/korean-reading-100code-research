# LOCAL_INGEST_PLAN

> 다운로드 없이 현재 로컬 원자료만으로 ingestion 가능한 항목. 다운로드 필요 항목은 DOWNLOAD_PLAN에만 둔다.

| 시험 | source path | 복원 가능 문항 수 | 필요 작업 |
|---|---|---:|---|
| KICE 2016학년도 수능 국어 B형 | `data/기본기_연구/prepared_backlog/sealed/G086_official_provenance/2016_KICE_Korean_B_problem_and_answer_archive.pdf` + `data/기본기_연구/prepared_backlog/sealed/G086_official_provenance/2016_KICE_Korean_B_odd_answer_table.pdf` | 4 | PDF 문항 범위 확인, answer linkage, canonical record 생성 |

기존 독서 원자료 묶음은 4문항이며, 아래 마더텅 문학 중앙화로 45문항이 추가되어 현재 로컬 ingestion 가능 source는 총 49문항이다. 이 목록은 연구 결과나 queue가 아니라 문제·정답 원자료 묶음만 대상으로 한다.

## KICE 문학 재감사 결과 (2026-09-20)

대상 45문항(2026 수능 Q18–34, 2024 수능 Q22–29·Q32, 2023 수능 Q31–34, 2023 9월 Q28–31, 2023 6월 Q32–34, 2022 수능 Q28–31, 2021 수능 Q43, 2020 수능 Q43–45)은 외부 마더텅 국어 문학 HWPX에서 지문·발문·선지·보기 원문을 확인했다. 모두 `LOCAL_COMPLETE`로 승격했으며 KICE 다운로드 항목은 `DOWNLOAD_PLAN.md`에서 제거했다.

문항별 source path·SHA-256·candidate mapping은 `data/corpus_ingest/kice_literature_local_audit_target_mapping.json`, 조사 보고서는 `data/corpus_ingest/KICE_LITERATURE_MOTHERTONG_INGEST.md`에 있다. 중앙 문학 MD는 13개, 새 asset은 0개다.
