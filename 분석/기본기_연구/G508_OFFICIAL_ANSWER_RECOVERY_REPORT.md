# G508 Official Answer Recovery 보고서

작성일: 2026-10-08

## 대상 및 좌표 확정

대상은 BQJ, BQK, BQL, BQM 네 case다. `research_data_index_enriched_v2.json` 좌표를 `prepared_backlog/sealed/provenance_mapping.jsonl`의 case별 provenance와 대조했다. 네 case 모두 KICE, 2016학년도 대학수학능력시험 국어 B형, passage `KICE-2016-수능국어B형-Q21-24`이며, case별 `official_pages`가 동일한 B형 **홀수형** 공통 지문(PDF page index 39)과 각 문항 페이지(index 40)를 명시한다. 좌표 claim 간 충돌은 없었다.

| case_id | 시험·형식 | 문항 | question_id | 공식 정답 | 상태 |
|---|---|---:|---|---|---|
| BQJ | 2016 수능 국어 B형 홀수형 | 21 | `KICE-2016-수능국어B형-Q21-24-Q21` | ③ | RECOVERED |
| BQK | 2016 수능 국어 B형 홀수형 | 22 | `KICE-2016-수능국어B형-Q21-24-Q22` | ③ | RECOVERED |
| BQL | 2016 수능 국어 B형 홀수형 | 23 | `KICE-2016-수능국어B형-Q21-24-Q23` | ③ | RECOVERED |
| BQM | 2016 수능 국어 B형 홀수형 | 24 | `KICE-2016-수능국어B형-Q21-24-Q24` | ② | RECOVERED |

## 정답 출처와 판정 방식

사용한 공식 정답 자료는 `자료/평가원_정답표/원본/수능/2016__국어_정답표_국어영역.pdf` 3쪽이다. 해당 페이지의 표제는 “2016학년도 대학수학능력시험 국어 영역 정답표 (B형) 홀수형”이며 각 문항 번호의 정답 행을 확인했다. case별 sealed provenance가 질문 PDF의 홀수형과 해당 문항을 특정하므로 네 답 모두 시험·형식·문항 좌표가 일치한다.

정답은 직접 풀이, 선지 내용, 기존 Astra 풀이, SDSS candidate marked answer, case 순서 또는 이웃 문항으로 추론하지 않았다. 기존 answer_check raw는 정답 선택 근거로 사용하지 않았고 비교도 수행하지 않았다. semantic research 결과는 재판정하지 않았다. **Conflict: 없음.** 최종 상태는 RECOVERED 4, UNRESOLVED 0, CONFLICT 0이다.

절차 메모: 연도·B형·문항 좌표를 확인한 뒤 정답표에서 형식별 정답 차이를 먼저 확인했으나, 이 시점에는 답을 배정하지 않았다. 이후 case-specific sealed provenance로 홀수형 연결을 확인한 뒤에만 정답표 행을 적용했다. 형식은 정답 차이나 문항 내용을 보고 역추론하지 않았다.

## 원장 불변 검증

복구 전후 SHA-256은 동일하며 pending/duplicate/orphan 상태도 모두 전후 동일하다.

| 파일 | SHA-256 | 상태 |
|---|---|---|
| `astra_handoff_queue.jsonl` | `74b1e630ddb3808a1fc25d5d047514b8558ddd8f271d1d41a5d629fd568b4195` | unchanged |
| `astra_handoff_processed.jsonl` | `c49e67a393b517671b94b6e0267689f8250fe55f6d4f2cd38e0cd954ef311818` | unchanged |
| `prepared_backlog/manifest.jsonl` | `29bbdf41af019151d0342a846b3cfa48cec22142f41f24f5d895c4b8e4392e48` | unchanged |
| `meta_state.json` | `2ac212abe6f83b7d2e97f9b2ef0b706bca92bd8bda7dfafb1a2482044be480fc` | unchanged |

| 지표 | 전 | 후 |
|---|---:|---:|
| pending | 0 | 0 |
| queue duplicates | 0 | 0 |
| processed duplicates | 0 | 0 |
| orphan processed IDs | 0 | 0 |

G024/G370 hold와 기존 index·manifest·semantic raw는 수정하지 않았다. 새 산출물은 `data/기본기_연구/G508_official_answer_recovery_20261008.json`과 본 보고서뿐이다.
