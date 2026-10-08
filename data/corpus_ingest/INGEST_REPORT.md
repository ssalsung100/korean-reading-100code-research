# KICE corpus ingestion 보고서

## 처리 원칙

이번 작업은 corpus ingestion / source restoration / indexing만 수행했으며 문제 풀이, 정답 추론, 100코드·O1~O8·SDSS 분석 및 기존 연구 기록 수정을 수행하지 않았다.

## 결과

- canonical passage: 169
- canonical question: 700
- 신규 발견 시험: 2 (2027학년도 6월·9월 모평)
- staging passage/question: 6/22
- canonical merge passage/question: 6/22
- duplicate 제외: 0
- NEEDS_RESTORE/CONFLICT/UNRESOLVED: 0/0/0
- 중앙 독서 MD: 169 / 문학 MD: 2
- 이번 중앙 라이브러리 추가 MD: 8 (기존 canonical section 중앙화 163)
- 이미지·표·그래프 asset 추가: 2

## 문학 처리

2027학년도 6월·9월 4~9번 문학 원문은 중앙 MD와 inventory에 보존했으나 현재 canonical이 독서 전용이므로 `unsupported_current_schema`로 보고하고 canonical에 편입하지 않았다.

## 다음 준비

다음 cxprepare가 준비할 신규 canonical passage/question: 0/0 (이번 ingestion으로 merge 완료)

## 경로

- `data/기출_MD_정본/INDEX.md`
- `data/기출_MD_정본/index.json`
- `data/corpus_ingest/INGEST_REPORT.md
