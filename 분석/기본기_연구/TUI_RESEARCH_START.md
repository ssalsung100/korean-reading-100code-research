# TUI 연구 시작

저장소 루트에서 다음 한 명령으로 새 Astra TUI를 연다.

```bash
scripts/cx1m
```

이 launcher는 다음을 고정한다.

- model: `gpt-6-astra`
- reasoning: `high`
- context: `model_context_window=1000000`
- auto compact: `model_auto_compact_token_limit=900000`
- sandbox: `workspace-write`

TUI가 열린 뒤 `/status`에서 설정을 확인하고 `AGENTS.md`, `분석/기본기_연구/CURRENT.md`, `분석/기본기_연구/ASTRA_START.md` 순으로 상태를 복구한다.

quota는 다음 helper로 조회한다.

```bash
scripts/codex_quota
```

helper는 `codex app-server --stdio`의 `account/rateLimits/read`를 호출한다. `primary_remaining_percent`와 `weekly_remaining_percent` 중 하나라도 처음 7% 이하로 관측되면 새 case·새 semantic stage·SDSS compare·induction·boundary revision을 시작하지 않는다. 현재 atomic stage를 raw queue에 저장하고, `ASTRA_CHECKPOINT.md`를 확인한 뒤 실제 `spawn_agent`로 다음 설정의 Luna를 생성한다. Runtime의 `less than 5% of your 5h limit left` 또는 이에 준하는 primary usage-limit 경고는 helper 값과 무관한 emergency trigger이며, 재조회 없이 raw/checkpoint 후 Luna를 spawn한다. `quota_status=unavailable` 자체는 handoff가 아니고 값을 추정하지 않는다.

```text
model: gpt-5.6-luna
reasoning_effort: medium
fork_context: false
```

Luna에는 Astra 대화 전체를 전달하지 않고 신규 raw queue와 `분석/기본기_연구/LUNA_HANDOFF_START.md`, `분석/기본기_연구/LUNA_HANDOFF.md`만 읽도록 지시한다. `cxcycle`은 unattended fallback으로 유지한다.
