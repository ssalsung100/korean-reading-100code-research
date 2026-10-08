# KICE 문학 로컬 원자료 재감사

2026-09-20 외부 authoritative 후보인 `/mnt/d/국어/평가원 선지 빼먹기/2027_마더텅_수능기출문제집_국어_문학_문제편_한글_파일`을 전수 조사했다. 원본 HWPX 7개와 추출 MD 8개를 확인했고, HWPX ZIP 내부 `Contents/section*.xml`을 우선 추출했다.

## 회차별 판정

| 학년도 | 시험 | 대상 문항 | 로컬 source | 중앙 MD | 상태 | 추가 다운로드 필요 |
|---:|---|---:|---|---|---|---|
| 2026 | 수능 | Q18–34 (17) | 마더텅 HWPX 4개 | Q18-21, Q22-26, Q27-30, Q31-34 | LOCAL_COMPLETE | 없음 |
| 2024 | 수능 | Q22–29, Q32 (9) | 마더텅 HWPX 3개 | Q22-27, Q28-31, Q32-34 | LOCAL_COMPLETE | 없음 |
| 2023 | 수능 | Q31–34 (4) | 마더텅 현대시 HWPX | Q31-34 | LOCAL_COMPLETE | 없음 |
| 2023 | 9월 모평 | Q28–31 (4) | 마더텅 현대소설 HWPX | Q28-31 | LOCAL_COMPLETE | 없음 |
| 2023 | 6월 모평 | Q32–34 (3) | 마더텅 현대시 HWPX | Q32-34 | LOCAL_COMPLETE | 없음 |
| 2022 | 수능 | Q28–31 (4) | 마더텅 고전산문 HWPX | Q28-31 | LOCAL_COMPLETE | 없음 |
| 2021 | 수능 | Q43 (1) | 마더텅 현대시 HWPX | Q43-45 원문 블록 | LOCAL_COMPLETE | 없음 |
| 2020 | 수능 | Q43–45 (3) | 마더텅 현대시 HWPX | Q43-45 | LOCAL_COMPLETE | 없음 |

문항별 provenance와 target mapping은 [kice_literature_local_audit_target_mapping.json](kice_literature_local_audit_target_mapping.json)에 기록했다. 중앙화 상세와 SHA-256은 [KICE_LITERATURE_MOTHERTONG_INGEST.md](KICE_LITERATURE_MOTHERTONG_INGEST.md)에 있고, 파일별 inventory는 [KICE_LITERATURE_MOTHERTONG_SOURCE_INVENTORY.json](KICE_LITERATURE_MOTHERTONG_SOURCE_INVENTORY.json)에 있다.

## 총계

- 재검사 KICE target: 45
- LOCAL_COMPLETE: 45
- LOCAL_RESTORABLE: 0
- LOCAL_PARTIAL: 0
- EXTERNAL_SOURCE_NEEDED: 0
- 새 중앙 문학 MD: 13
- 새 asset: 0
- 실제 KICE 다운로드 필요 회차: 0

검산: `45 = 45 + 0 + 0 + 0`.

문항 풀이·정답 추론·100코드 판정은 수행하지 않았다.
