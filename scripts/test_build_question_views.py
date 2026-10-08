#!/usr/bin/env python3
"""기계적 Luna view builder의 fixture·재실행 검증."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_question_views as v  # noqa: E402


def test_normalization_and_history() -> None:
    payload = {"기타 기록 필드": {"competing_codes": [{"code": 17, "rejection": "입력 종류와 다름"}]}, "current_primary_candidates": [75, 80]}
    sections = v.normalized_sections(payload)
    assert sections["competitors"][0]["source_key"] == "기타 기록 필드.competing_codes"
    assert sections["primary"][0]["value"] == [75, 80]
    records = [{"record_id": "P-blind-1", "stage": "blind", "status": "done", "payload": {"selected_answer": 1}}, {"record_id": "P-blind-2", "stage": "blind", "status": "done", "payload": {"selected_answer": 2}}]
    lines: list[str] = []
    v.render_record_history(lines, "blind", records)
    assert "P-blind-1" in "\n".join(lines) and "P-blind-2" in "\n".join(lines)


def test_source_warnings() -> None:
    empty = {"case_id": "CH", "passage_text": "p", "stem": "s", "choices": ["", "", "", "", ""]}
    audit = v.source_audit("CH", empty, [{"payload": {"supplement": "data/not-exported.json"}}])
    assert audit["all_choices_empty"] and not audit["ready"]
    assert any("모든 선택지" in warning for warning in audit["warnings"])
    assert any("not-exported" in warning for warning in audit["warnings"])


def test_scope_tag_unresolved_and_record_dedupe() -> None:
    records = [
        {"record_id": "A-ic", "case": "A", "stage": "independent_code", "status": "done", "payload": {"primary": [{"code": 45}], "passage_group": "G1"}},
        {"record_id": "REV-ic", "case": "A", "stage": "independent_code", "status": "done", "payload": {"case_ids": ["A", "B"], "primary": [{"code": 45}], "passage_group": "G1"}},
        {"record_id": "A-sdss", "case": "A", "stage": "sdss_compare", "status": "done", "payload": {"site_original_codes": [], "unresolved": "태그 미확인"}},
    ]
    by_case = {"A": records, "B": [records[1]]}
    result = v.build_derived_indexes(records, ["A", "B"], {}, {}, {"A": {"case_id": "A"}, "B": {}}, by_case, {"A": {}, "B": {}})
    assert result["sdss_tag_missing_case_ids"] == ["A"]
    assert result["unresolved"][0]["case_id"] == "A"
    assert result["code_index"]["45"]["record_ids"] == ["A-ic", "REV-ic"]
    assert result["code_index"]["45"]["passage_group_count"] == 1


def test_production_rerun_is_stable() -> None:
    root = Path(__file__).resolve().parents[1]
    out = root / "분석/기본기_연구/문항별_완성본"
    subprocess.run([sys.executable, str(root / "scripts/build_question_views.py")], cwd=root, check=True, capture_output=True, text=True)
    first = {name: (out / name).read_text(encoding="utf-8") for name in ("INDEX.md", "RESEARCH_VIEW_INDEX.json", "SOURCE_AUDIT.json", "CODE_COVERAGE.json")}
    subprocess.run([sys.executable, str(root / "scripts/build_question_views.py")], cwd=root, check=True, capture_output=True, text=True)
    second = {name: (out / name).read_text(encoding="utf-8") for name in first}
    first["INDEX.md"] = "\n".join(line for line in first["INDEX.md"].splitlines() if "생성 시각" not in line)
    second["INDEX.md"] = "\n".join(line for line in second["INDEX.md"].splitlines() if "생성 시각" not in line)
    assert first == second
    index = json.loads(second["RESEARCH_VIEW_INDEX.json"])
    assert index["prepared"]["completed_case_count"] == 174
    assert index["legacy"]["completed_case_count"] == 3


if __name__ == "__main__":
    tests = [test_normalization_and_history, test_source_warnings, test_scope_tag_unresolved_and_record_dedupe, test_production_rerun_is_stable]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
