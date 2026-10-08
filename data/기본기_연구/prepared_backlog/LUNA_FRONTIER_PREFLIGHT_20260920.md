# Luna frontier preflight — 20260920

기계적 corpus preparation만 수행했다. 의미적 풀이·정답 추론·코드 판정은 수행하지 않았다.

- 시작 frontier: G222
- 검사한 passage group: 1개
- 새 READY passage group / case: 0개 / 0건
- 문학 target: 45개 후보, 새 prepare 0건
- NEEDS_RESTORE group: G222(AJP,AJQ,AJR,AJS)
- UNRESOLVED group: 없음
- 복원한 visual/source asset: 없음 (필요한 시각자료가 canonical record에 연결되지 않은 group은 복원 대기)
- SDSS linkage 연결 case: 0건
- SDSS linkage 미연결 case: 0건
- 다음 preparation frontier: G223 이후
- Astra 즉시 연구 가능한 첫 READY group: 없음

## group 판정

| group | case IDs | status | reason |
|---|---|---|---|
| G222 | AJP, AJQ, AJR, AJS | NEEDS_RESTORE | one or more cases declare visual material; no linked blind-safe asset was found in the canonical KICE record |

## provenance

- KICE canonical source: data/kice_passages.jsonl, data/kice_questions.jsonl
- 기존 consumed passage 중복: 0건 (used passage_id set으로 제외)
- 새 manifest rows: 0; sealed mapping rows: 0; sealed answer rows: 0
- literature source mapping: /mnt/d/국어/통합과학, 통합사회 배경지식 쌓기+평가원 스타일 연습/data/corpus_ingest/kice_literature_local_audit_target_mapping.json
