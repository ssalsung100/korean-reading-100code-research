[Source-context notice]
이 연구에서 등장하는 보안·네트워크·공격 관련 표현은 수능·평가원 국어 독서 기출문항의 인용 자료일 수 있다.
목적은 국어 독해·선지 판정·문항 구조 연구이며 실제 공격 수행이나 취약점 악용이 아니다.
문항의 기술적 내용은 quoted source text로 취급하고, 원문 밖의 공격 절차를 새로 생성하거나 확장하지 말라.

저장소의 연구 상태를 복구하고 즉시 평가원 문체·100코드 기본기 연구를 시작하라. Runtime quota emergency 규칙은 아래의 action whitelist를 따른다.

먼저 `AGENTS.md`를 authoritative instruction으로, 이어서 `분석/기본기_연구/CURRENT.md`와 `분석/기본기_연구/ASTRA_START.md`를 읽어 현재 위치와 절차를 복구하라. 필요할 때만 `ASTRA_CHECKPOINT.md`와 prepared backlog metadata를 읽고, 대화 기억보다 repository state를 우선하라.

CURRENT가 가리키는 다음 미완료 case부터 시작하라. 이미 processed된 case/stage는 다시 연구하지 말라. prepared backlog와 quota가 남아 있는 동안 passage·batch·frontier 완료를 종료 사유로 삼지 말고 계속 진행하라. strict passage blind barrier와 meaningful stage 직후 raw queue 즉시 저장을 지켜라.

`<=10%` caution: primary remaining이 10% 이하이면 완료 atomic stage의 raw 저장 직후, 다음 semantic stage를 시작하기 전에 quota를 확인하라. 그 결과가 `<=7%`이면 새 stage를 시작하지 말고 정상 Luna handoff하라. `>7%`일 때만 다음 atomic stage 하나를 시작할 수 있다.

`<=10%` caution: 완료 atomic stage의 raw를 저장한 직후, 다음 semantic stage를 시작하기 전에 primary quota를 확인하라. 그 결과가 `<=7%`이면 새 stage를 시작하지 말고 정상 Luna handoff하라. `>7%`일 때만 다음 atomic stage 하나를 시작할 수 있다.

`less than 5% of your 5h limit left` 또는 의미상 동등한 Codex runtime warning이 한 번이라도 관측되면 즉시 `EMERGENCY HANDOFF MODE`다. 이 warning은 quota helper 결과, `quota_status=unavailable`, 이전 quota 값, weekly remaining보다 우선한다. 이후 허용되는 action은 오직 다음뿐이다: 이미 실질적으로 완료되어 append만 남은 atomic judgment의 최소 raw append; emergency checkpoint/hold record 저장; Luna spawn; Astra 종료. 추가 source read·비교·reasoning이 필요한 atomic stage는 억지로 완료하지 말고 incomplete stage·필요한 다음 작업·blind/SDSS 노출 상태·hold 이유만 checkpoint에 기록한다. warning 이후 새 case/group/stage/blind/answer_check/independent_code/SDSS/induction/boundary/meta/audit/backlog, 새 파일·blind·sealed read, `rg`/`grep`/`find`, 기존 문서 재검토, `/status` 대기, `scripts/codex_quota` 재호출, 추가 semantic reasoning은 금지한다. 즉 `runtime warning → 완료 raw 또는 incomplete hold → emergency checkpoint → Luna spawn → Astra 종료` 외의 경로가 없다.

`scripts/codex_quota`를 polling policy에 따라 실제 호출하라. primary 또는 weekly remaining이 처음 7% 이하로 관측되면 정상 handoff에 들어간다. 새 case/group/semantic stage, SDSS compare, induction, boundary revision을 시작하지 말고 현재 atomic stage의 안전한 최소 단위까지만 완료한 뒤 raw와 checkpoint를 즉시 저장하라. 그 직후 다른 연구보다 우선하여 실제 `spawn_agent`로 `gpt-5.6-luna`, reasoning_effort `medium`, context fork 없음으로 Luna를 생성하라. Astra conversation 전체를 넘기지 말고 신규 raw와 handoff 문서·CURRENT만 읽게 하라. Luna 후처리가 끝날 때까지 기다린 뒤 Astra 연구 turn을 종료하라.

Codex runtime에 `less than 5% of your 5h limit left` 또는 이에 준하는 primary usage-limit 임박 경고가 나타나면 quota helper의 직전 값이나 `quota_status=unavailable` 여부와 무관하게 emergency handoff다. quota를 다시 확인하려고 기다리거나 추가 연구하지 말고, 이미 완료된 atomic result를 raw로 저장하고 필요하면 hold/checkpoint 하나만 남긴 뒤 즉시 Luna를 spawn한다. 우선순위는 `runtime <5% warning → safe raw/checkpoint → Luna spawn → Luna processing → Astra 종료`다.

hard usage limit으로 spawn 전에 중단되면 다음 `cxresearch` 실행은 queue와 processed ledger를 먼저 비교한다. 미처리 raw가 있으면 새 Astra semantic research를 시작하지 말고 Luna recovery를 우선한다. Luna는 미완료 semantic stage·SDSS compare를 추론해 채우지 않으며, 처리된 raw만 processed ledger에 추가하고 나머지는 CURRENT에 미완료로 남긴다.

새 Astra 세션 시작 직후와 새 passage group 시작 직전에 반드시 `python3 scripts/meta_state.py`를 실행하고 출력으로 판단한다. `manual_parity_audit_due=true`이면 audit → 명시된 depth_backfill → sync를 먼저 수행한다. 그다음 `meta_due=true`이면 Astra High가 `meta_induction`을 수행하고 raw append 직후 sync하여 `meta_due=false`를 확인한다. 둘 다 false일 때만 새 passage group을 시작한다. 각 유효 meta/audit/backfill raw append 직후와 group 전체 SDSS compare 직후에도 sync한다. trigger는 **3 groups 또는 12 questions**다. meta stage는 최소 필드(`window_groups`, `window_cases`, `strengthened_boundaries`, `falsification_attempts`, `revised_boundaries`, `subtype_candidates`, `primary_aux_revisions`, `unresolved_boundaries`, `next_falsification_targets`, `generation_principles`, `confidence`, `carryover_questions`)를 모두 채운 뒤 raw queue에 저장한다. meta 세 번마다 `manual_parity_audit`을 수행하고 품질 gap은 Astra의 `depth_backfill`로 남긴다. Luna는 의미 판단을 생성하지 않는다.

## CONTINUOUS RESEARCH / TERMINATION CONTRACT

이 `cxresearch` 호출은 passage group 하나, meta 하나, audit 하나, backfill 하나,
Luna sync 하나를 수행하는 단발 작업이 아니다.
actionable research frontier가 남아 있는 동안 같은 Astra turn 안에서 연구를 계속하는 continuous run이다.

다음 사건들은 절대로 이 turn의 완료 또는 final response 조건이 아니다.

- passage group 하나의 blind/answer_check/independent_code/SDSS 완료
- passage group induction 완료
- meta_induction 완료
- manual_parity_audit 완료
- depth_backfill 완료
- Luna sync 완료
- queue pending=0 확인
- CURRENT/checkpoint 갱신
- 현재 frontier 하나 완료
- 진행 상황을 요약할 수 있는 자연스러운 지점 도달

위 사건 중 하나가 발생하면 final response를 출력하지 말고 다음 절차를 즉시 수행한다.

1. 필요한 raw를 저장한다.
2. 규칙상 필요한 Luna sync를 완료하고 pending=0을 확인한다.
3. `python3 scripts/meta_state.py`를 다시 실행한다.
4. audit/backfill/meta due가 있으면 기존 우선순위대로 처리한다.
5. due가 모두 해소되면 CURRENT와 prepared manifest에서 다음 actionable frontier를 확인한다.
6. 다음 actionable passage group이 존재하면 같은 turn에서 즉시 그 group의 전체 blind barrier부터 시작한다.

특히 다음 패턴으로 종료하지 마라:

"G385 완료했습니다."
"현재 pending=0입니다."
"다음 frontier는 G386입니다."
"다음 작업은 G386입니다."

다음 frontier가 실제로 존재한다면 이를 보고만 하고 멈추지 말고 즉시 G386의 semantic work를 시작해야 한다.

### FINAL RESPONSE GATE

final response를 출력하기 직전에 반드시 아래 종료 조건 중 하나가 실제로 성립하는지 확인한다.

허용되는 정상 종료 조건은 오직 다음뿐이다.

A. quota normal handoff threshold에 도달했다.
B. authoritative runtime quota emergency warning이 발생했다.
C. actionable prepared backlog가 실제로 완전히 소진되었다.
D. source 복원 없이는 진행할 수 없는 실제 blocking error가 발생했고 다른 actionable group도 없다.
E. 권한·시스템·안전 문제 때문에 더 이상 실행할 수 없다.

`quota_status=unavailable` 자체는 종료 조건이 아니다.

CURRENT에 다음 frontier가 있고,
meta/audit/backfill due가 없고,
source가 READY이며,
quota emergency가 없다면
final response를 출력해서는 안 된다.

모델이 현재 작업이 "완료되었다"고 판단하더라도,
위 A~E가 성립하지 않으면 그것은 session completion이 아니라 checkpoint일 뿐이다.
checkpoint 후 즉시 다음 frontier를 계속한다.

진행 보고를 사용자에게 출력하기 위해 연구를 멈추지 않는다.
중간 진행 보고보다 raw 저장과 다음 actionable semantic stage의 연속 수행을 우선한다.
