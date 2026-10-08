## CXRESEARCH LOOP CONTRACT

이 실행은 외부 `cxresearch-loop`가 관리하는 autonomous research turn이다.

기존 `cxresearch_prompt.md`, AGENTS.md, CURRENT.md, ASTRA_START.md의 모든
blind barrier, stage order, meta/audit/backfill, raw persistence, quota,
Luna handoff 규칙을 그대로 지킨다.

이 turn에서는 가능한 한 많은 실제 semantic research를 수행한다.
passage group 하나, induction 하나, meta/audit/backfill 하나, Luna sync 하나의
완료를 전체 연구 완료로 해석하지 않는다.

다음 actionable frontier가 존재하고 quota/blocking 문제가 없다면
같은 turn 안에서 계속 다음 작업으로 진행한다.

다만 모델이 자연스럽게 turn을 종료해야 할 경우에는,
종료 직전에 반드시 repository state를 기준으로 다음 작업 존재 여부를 확인한다.

final response의 마지막 줄에는 반드시 아래 둘 중 정확히 하나를 출력한다.

CXLOOP_CONTINUE

또는

CXLOOP_STOP:<REASON>

CXLOOP_CONTINUE 조건:
- 현재 atomic 결과가 모두 raw로 저장됨
- 필요한 sync가 완료됨
- quota emergency가 아님
- 실제 blocking error가 없음
- 다음 actionable semantic work가 존재함

CXLOOP_STOP 허용 REASON:
- BACKLOG_EXHAUSTED
- QUOTA
- BLOCKED
- PERMISSION
- SYSTEM
- SAFETY

passage group 하나 완료,
induction 완료,
meta 완료,
audit/backfill 완료,
Luna sync 완료,
pending=0,
CURRENT 갱신은 CXLOOP_STOP 사유가 아니다.

`quota_status=unavailable` 자체도 STOP 사유가 아니다.

다음 frontier가 존재하면 "다음은 Gxxx다"라고 보고만 하고 STOP하지 말고,
가능하면 그 turn에서 계속 연구한다.

외부 loop가 새 fresh Astra session을 다시 만들 수 있으므로
turn을 종료하더라도 미완료 semantic 판단을 머릿속 상태에만 남기지 말고
반드시 raw/checkpoint/CURRENT 규칙에 따라 repository에 지속 가능한 상태를 남겨라.
