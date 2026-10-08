#!/usr/bin/env python3
"""Static contract fixtures for Astra quota emergency/caution control."""

from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROMPT_PATHS = (
    ROOT / "scripts/cxresearch_prompt.md",
    ROOT / "scripts/cxcycle_astra_prompt.md",
    ROOT / "분석/기본기_연구/ASTRA_START.md",
    ROOT / "분석/기본기_연구/ASTRA_CHECKPOINT.md",
)

EMERGENCY_WARNING = "less than 5% of your 5h limit left"
EMERGENCY_ALLOWED = frozenset(
    {"completed_raw_append", "emergency_checkpoint", "luna_spawn", "terminate"}
)
EMERGENCY_FORBIDDEN = (
    "scripts/codex_quota",
    "새 파일",
    "sealed",
    "rg",
    "grep",
    "find",
    "새 case/group/stage",
    "blind",
    "SDSS",
    "meta",
    "audit",
    "backlog",
    "/status",
)


@dataclass(frozen=True)
class QuotaState:
    runtime_warning: bool = False
    atomic_complete: bool = True
    primary_remaining: int = 100
    helper_called_before_warning: bool = False


def decide(state: QuotaState) -> dict:
    """Reference control contract; production prompts must express this policy."""
    if state.runtime_warning:
        actions = {"emergency_checkpoint", "luna_spawn", "terminate"}
        if state.atomic_complete:
            actions.add("completed_raw_append")
        return {
            "mode": "emergency",
            "actions": frozenset(actions),
            "quota_recheck": False,
            "new_semantic_stage": False,
            "hold_incomplete": not state.atomic_complete,
        }
    if state.primary_remaining <= 7:
        return {
            "mode": "normal_handoff",
            "actions": frozenset({"safe_raw_or_hold", "checkpoint", "luna_spawn", "terminate"}),
            "quota_recheck": False,
            "new_semantic_stage": False,
            "hold_incomplete": not state.atomic_complete,
        }
    if state.primary_remaining <= 10:
        return {
            "mode": "caution",
            "actions": frozenset({"completed_raw_append", "quota_check_before_next_stage"}),
            "quota_recheck": True,
            "new_semantic_stage": False,
            "hold_incomplete": False,
        }
    return {
        "mode": "normal",
        "actions": frozenset({"completed_raw_append", "next_atomic_stage_allowed"}),
        "quota_recheck": False,
        "new_semantic_stage": True,
        "hold_incomplete": False,
    }


def require(text: str, *needles: str) -> None:
    missing = [needle for needle in needles if needle not in text]
    if missing:
        raise AssertionError(f"production instruction missing: {missing}")


def main() -> None:
    texts = {path.name: path.read_text(encoding="utf-8") for path in PROMPT_PATHS}
    combined = "\n".join(texts.values())
    require(
        combined,
        EMERGENCY_WARNING,
        "EMERGENCY HANDOFF MODE",
        "quota helper",
        "incomplete",
        "Luna spawn",
        "Astra 종료",
    )
    require(texts["cxresearch_prompt.md"], "10% 이하", "7% 이하", "시작하기 전에 quota")
    require(texts["cxcycle_astra_prompt.md"], "primary remaining is 10% or lower")
    require(texts["ASTRA_CHECKPOINT.md"], "Runtime `<5%` emergency action whitelist")
    require(combined, "quota를 다시 확인하지", "새 source read", "sealed")

    # Scenario A: runtime warning wins even after a helper reported 8%.
    result = decide(QuotaState(runtime_warning=True, primary_remaining=8, helper_called_before_warning=True))
    assert result["mode"] == "emergency"
    assert result["actions"] == EMERGENCY_ALLOWED
    assert result["quota_recheck"] is False
    assert result["new_semantic_stage"] is False

    # Scenario B: an incomplete atomic stage is held, never completed by reasoning.
    result = decide(QuotaState(runtime_warning=True, atomic_complete=False))
    assert result["actions"] == EMERGENCY_ALLOWED - {"completed_raw_append"}
    assert result["hold_incomplete"] is True

    # Scenario C: 9% means one completed stage, then a check; 6% handoffs.
    result = decide(QuotaState(primary_remaining=9))
    assert result["mode"] == "caution"
    assert result["quota_recheck"] is True
    assert "quota_check_before_next_stage" in result["actions"]
    result_after_check = decide(QuotaState(primary_remaining=6))
    assert result_after_check["mode"] == "normal_handoff"
    assert result_after_check["new_semantic_stage"] is False

    # Scenario D: 13% preserves the existing cadence.
    result = decide(QuotaState(primary_remaining=13))
    assert result["mode"] == "normal"
    assert result["new_semantic_stage"] is True

    # The production text must state every emergency prohibition, not only a threshold.
    for forbidden in EMERGENCY_FORBIDDEN:
        assert forbidden in combined, f"emergency prohibition missing: {forbidden}"

    print("quota emergency fixtures: scenarios A-E passed; production contract strings verified")


if __name__ == "__main__":
    main()
