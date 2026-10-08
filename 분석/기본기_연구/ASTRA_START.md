# Astra 시작

## 2026-09-15 운영 규칙 보강

3개 passage group 완전 완료마다 Astra가 due `meta_induction`·`manual_parity_audit`·필요 `depth_backfill`을 먼저 저장한다. 이어 Luna sync 1회를 수행하고 pending raw=0을 검증한 뒤에만 다음 group 연구를 계속한다. quota emergency 경고가 발생하면 이 순서보다 emergency handoff whitelist를 우선한다.

## TUI 연구 시작

기본 연구 경로는 새 TUI다. 저장소 루트에서 `scripts/cx1m`을 실행하면 `gpt-6-astra`, reasoning `high`, `model_context_window=1000000`, `model_auto_compact_token_limit=900000`, `workspace-write`로 시작한다. `resume` 세션을 기본 연구 경로로 사용하지 않는다. 시작 후 `/status`에서 model, reasoning, context override를 확인한다.

연구 중 quota는 `scripts/codex_quota`로 직접 조회한다. primary remaining이 10% 이하이면 완료 atomic stage raw 저장 직후 다음 semantic stage 전에 quota를 확인하고, 결과가 7% 이하이면 즉시 정상 handoff한다. primary와 weekly 중 하나라도 처음 `remaining <= 7%`로 관측되면 새 case·새 semantic stage·SDSS compare·induction·boundary revision을 시작하지 말고 현재 안전한 atomic stage와 raw/checkpoint만 저장한 뒤, Astra TUI의 실제 `spawn_agent`로 `gpt-5.6-luna` medium subagent를 `fork_context: false`로 생성한다. Astra 대화 전체를 전달하지 말고 신규 raw와 handoff instruction·CURRENT만 읽게 한다. Luna 후처리가 끝날 때까지 기다린 뒤 Astra turn을 종료한다.

Codex runtime에 `less than 5% of your 5h limit left` 또는 이에 준하는 primary usage-limit 경고가 보이면 즉시 `EMERGENCY HANDOFF MODE`다. warning 이후 허용 action은 오직 이미 완료되어 append만 남은 atomic raw의 최소 저장, emergency checkpoint/hold 저장, Luna spawn, Astra 종료다. 추가 source read·sealed read·`rg`/`grep`/`find`·새 semantic reasoning·새 case/group/stage/blind/SDSS/meta/audit/backlog 작업은 금지한다. 판단이 미완료라 추가 read/reasoning이 필요한 경우 억지로 완료하지 않고 incomplete/hold, 필요한 다음 작업, blind/SDSS 노출 상태를 checkpoint에 남긴다. quota를 다시 확인하지 않으며 helper 결과, unavailable, 이전 값, weekly remaining보다 이 warning을 우선한다. 조회 실패 시 `{"quota_status":"unavailable"}`를 보존하고 값을 추측하지 않으며, unavailable 자체는 handoff가 아니다.

`AGENTS.md`와 `분석/기본기_연구/CURRENT.md`만 먼저 읽어라. 이 문서는 그 다음 필요한 최소 실행 규칙이다.

CURRENT의 frontier를 실제로 수행한 뒤 `data/기본기_연구/prepared_backlog/manifest.jsonl`에서 다음 준비 사례를 순서대로 계속 소비하라. 상세 과거 파일은 현재 판단에 필요할 때만 선택적으로 읽어라. 기존 `blind → 공식답 → 독립 코드 판정 → SDSS 대조 → 귀납` 순서를 지켜라.

준비 사례 blind 단계에서는 manifest의 `blind_source`만 열어라. canonical question JSONL, candidate index, sealed answer/SDSS, 기존 해설·코드 판정은 blind raw record 저장 전 금지한다. 동일 `passage_group`에 여러 case가 있으면 그 group의 모든 case를 먼저 blind 풀이·raw 저장하고, 전부 확인한 뒤에만 group 전체의 answer_check를 시작한다.
group별로 `all_group_blind_records_before_any_group_answer_check`를 지킨 뒤 group 전체 answer_check, group 전체 independent_code(주/보조/표면과 경쟁 코드 검토), `all_group_independent_code_records_before_any_group_sdss_disclosure` 확인, SDSS 공개·대조, 필요 시 induction/boundary revision 순서로 진행한다. SDSS를 본 case가 있는 동안 같은 group의 미완료 independent_code를 판단하지 않는다.

각 판단 단계 완료 직후 다음 최소 schema로 queue에 한 record를 append하라. `record_id`는 사례·단계·순번으로 안정적으로 생성하고, `payload`에는 그 단계에서 실제로 판단한 내용만 넣는다. `stage`는 `blind`, `answer_check`, `independent_code`, `sdss_compare`, `induction`, `boundary_revision`, `meta_induction`, `manual_parity_audit`, `depth_backfill`, `exclude`, `hold` 중 하나를 쓴다. queue에 저장하지 않은 판단은 완료로 보지 않는다.

새 세션에서는 `data/기본기_연구/meta_state.json`을 먼저 읽는다. `meta_due=true`이면 새 passage group보다 Astra High의 cross-group `meta_induction`을 먼저 수행한다. `manual_parity_audit_due=true`이면 audit을 새 passage group보다 먼저 수행한다. 세 meta마다 `manual_parity_audit`을 수행하며, 품질 gap은 `depth_backfill`으로 남긴다. 세 stage의 최소 payload schema는 각각 meta 필수 12개 필드, audit의 `for_meta_count`·`sample_case_ids`·`dimension_scores`·`gaps`·`depth_backfill_case_ids`·`confidence`, backfill의 `case_ids`·`original_blind_preserved`·`evidence_additions`·`boundary_or_generation_impact`·`confidence`다. Luna는 이 세 stage의 의미를 생성하지 않는다.

```json
{"record_id":"case-stage-YYYYMMDD-seq","case":"P","stage":"blind","status":"done","timestamp":"YYYY-MM-DD","payload":{}}
```

상세 Markdown/JSONL 정리, CURRENT 갱신, 진행률 계산, audit, 긴 checkpoint 보고서는 수행하지 않는다. 각 판단 단계의 raw queue append는 즉시 수행한다. 현재 소수 frontier·batch·induction·진행 보고가 끝났다는 이유로 종료하지 말고 prepared backlog의 다음 사례로 이동한다. 5h primary 또는 weekly remaining이 처음 7% 이하(`used_percent >= 93`)면 신규 semantic work를 멈추고 안전 단계 또는 hold record를 저장한 뒤 즉시 Luna를 handoff한다. runtime `<5%` warning은 별도 emergency trigger이며 helper unavailable보다 우선한다. hard limit recovery에서는 미처리 raw를 먼저 Luna가 후처리하고 미완료 semantic stage는 CURRENT에 남긴다.
