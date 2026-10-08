#!/usr/bin/env python3
"""Build read-only, derived per-question Markdown views from Astra raw records."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = ROOT / "data/기본기_연구/astra_handoff_queue.jsonl"
PROCESSED_PATH = ROOT / "data/기본기_연구/astra_handoff_processed.jsonl"
BLIND_DIR = ROOT / "data/기본기_연구/prepared_backlog/blind_sources"
OUTPUT_DIR = ROOT / "분석/기본기_연구/문항별_완성본"
META_STATE_SCRIPT = ROOT / "scripts/meta_state.py"
MANIFEST_PATH = ROOT / "data/기본기_연구/prepared_backlog/manifest.jsonl"
META_STATE_PATH = ROOT / "data/기본기_연구/meta_state.json"

REQUIRED_STAGES = ("blind", "answer_check", "independent_code", "sdss_compare")
STAGE_LABELS = {
    "blind": "최초 blind 풀이",
    "answer_check": "공식 정답 대조",
    "independent_code": "독립 코드 판정",
    "sdss_compare": "SDSS 사후 대조",
    "depth_backfill": "후속 보강",
    "boundary_revision": "경계 수정 기록",
    "induction": "집단 귀납 기록",
    "meta_induction": "교차 사례 귀납 기록",
}
CORE_FIELDS = {
    "blind": [
        (("selected_answer", "answer"), "선택 답"),
        (("confidence",), "확신도"),
        (("needed_information_and_location", "needed_information", "necessary_information", "locations"), "필요 정보와 위치"),
        (("minimal_logic_without_codes", "minimal_logic", "code_free_logic"), "코드명 없는 최소 논리 구조"),
        (("intermediate_inference", "intermediate_reasoning"), "중간 추론"),
        (("most_attractive_wrong_answer", "most_attractive_wrong_option", "strongest_distractor"), "가장 매력적인 오답"),
        (("exact_error_of_wrong_answer",), "오답의 정확한 오류"),
        (("exposure",), "노출 정보"),
    ],
    "answer_check": [
        (("selected_answer", "initial_answer"), "최초 선택"),
        (("official_answer",), "공식 정답"),
        (("match",), "일치 여부"),
        (("answer_check_reasoning", "code_free_logic", "logic_frozen", "reasoning"), "정답 대조 reasoning"),
        (("exact_error", "exact_error_of_wrong_answer"), "오답의 정확한 오류"),
    ],
    "independent_code": [
        (("primary",), "주 코드"),
        (("auxiliary", "secondary"), "보조 코드"),
        (("surface",), "표면 코드"),
        (("competitors", "competitors_rejected", "competing_codes", "competing_codes_refuted"), "경쟁 코드 및 반증"),
        (("similarity",), "유사성"),
        (("rejection",), "기각 이유"),
        (("tracked", "tracked_difference"), "추적한 차이"),
        (("promotion_condition",), "주 코드 승격 조건"),
        (("confidence",), "확신도"),
        (("boundary_note",), "경계 메모"),
        (("qualification",), "판정의 한정"),
        (("merge_decision",), "통합 판단"),
    ],
    "sdss_compare": [
        (("site_original_codes", "original_site_tags", "site_original_tags"), "사이트 원래 코드"),
        (("site_code_numbers",), "사이트 코드 번호"),
        (("independent_primary_codes", "independent_primary", "independent_primary_preserved"), "독립 주 코드"),
        (("comparison",), "비교"),
        (("semantic_comparison",), "의미 비교"),
        (("independent_judgment_preserved", "independent_decision_preserved"), "독립 판정 보존"),
        (("sdss_role",), "SDSS의 역할"),
    ],
}

FIELD_ALIASES = {
    "primary": ("primary", "independent_primary", "current_primary_candidates", "revised_primary_candidates"),
    "auxiliary": ("auxiliary", "secondary", "independent_auxiliary"),
    "competitors": ("competitors", "competitors_rejected", "competing_codes", "competing_codes_refuted"),
    "site_tags": ("site_original_codes", "original_site_tags", "site_original_tags"),
}
OTHER_KEYS = {"기타 기록 필드", "other_fields", "other", " 기타 기록 필드"}


class ViewBuildError(RuntimeError):
    pass


def file_fingerprint(path: Path) -> tuple[str, int, int]:
    stat = path.stat()
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return digest, stat.st_size, stat.st_mtime_ns


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ViewBuildError(f"{path}:{line_number}: JSON 파싱 실패: {exc}") from exc
            if not isinstance(row, dict):
                raise ViewBuildError(f"{path}:{line_number}: 객체가 아닌 queue record")
            row["_queue_index"] = len(rows)
            rows.append(row)
    return rows


def latest_done(records: list[dict[str, Any]], stage: str) -> dict[str, Any] | None:
    matches = [r for r in records if r.get("stage") == stage and r.get("status") == "done"]
    return matches[-1] if matches else None


def latest_status_record(records: list[dict[str, Any]], stage: str) -> dict[str, Any] | None:
    matches = [r for r in records if r.get("stage") == stage]
    return matches[-1] if matches else None


def json_fence(value: Any) -> str:
    body = json.dumps(value, ensure_ascii=False, indent=2)
    longest = max((len(match.group(0)) for match in re.finditer(r"`+", body)), default=0)
    fence = "`" * max(3, longest + 1)
    return f"{fence}json\n{body}\n{fence}"


def text_fence(value: str) -> str:
    longest = max((len(match.group(0)) for match in re.finditer(r"`+", value)), default=0)
    fence = "`" * max(3, longest + 1)
    return f"{fence}text\n{value}\n{fence}"


def render_value(value: Any, indent: int = 0) -> str:
    """Render each stored value without paraphrasing or dropping nested fields."""
    pad = "  " * indent
    if isinstance(value, str):
        return text_fence(value)
    if isinstance(value, (dict, list)):
        return json_fence(value)
    return f"`{json.dumps(value, ensure_ascii=False)}`"


def display_core_fields(stage: str, payload: dict[str, Any]) -> tuple[list[tuple[str, Any]], dict[str, Any]]:
    shown: list[tuple[str, Any]] = []
    consumed: set[str] = set()
    for aliases, label in CORE_FIELDS.get(stage, []):
        key = next((candidate for candidate in aliases if candidate in payload), None)
        if key is not None:
            shown.append((label, payload[key]))
            consumed.add(key)
    remaining = {key: value for key, value in payload.items() if key not in consumed}
    return shown, remaining


def _nested_field_values(payload: dict[str, Any], aliases: tuple[str, ...]) -> list[tuple[str, Any]]:
    """Read aliases from the payload and explicitly nested 'other' fields only."""
    found: list[tuple[str, Any]] = []
    for key in aliases:
        if key in payload:
            found.append((key, payload[key]))
    for key in OTHER_KEYS:
        nested = payload.get(key)
        if isinstance(nested, dict):
            for alias in aliases:
                if alias in nested:
                    found.append((f"{key}.{alias}", nested[alias]))
    return found


def normalized_sections(payload: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    """Create display-only sections while retaining the original key/value."""
    result: dict[str, list[dict[str, Any]]] = {}
    for section, aliases in FIELD_ALIASES.items():
        values = _nested_field_values(payload, aliases)
        if values:
            result[section] = [{"source_key": key, "value": value} for key, value in values]
    return result


def render_normalized_sections(lines: list[str], payload: dict[str, Any]) -> None:
    sections = normalized_sections(payload)
    labels = {"primary": "정규화된 주 코드 후보", "auxiliary": "정규화된 보조 코드", "competitors": "정규화된 경쟁 코드 및 반증", "site_tags": "정규화된 사이트 태그"}
    for section in ("primary", "auxiliary", "competitors", "site_tags"):
        if section not in sections:
            continue
        lines.append(f"\n**{labels[section]}**\n")
        lines.append(json_fence(sections[section]))


def put_payload(lines: list[str], stage: str, record: dict[str, Any]) -> None:
    payload = record.get("payload")
    payload = payload if isinstance(payload, dict) else {}
    lines.append(f"### {STAGE_LABELS.get(stage, stage)} — `{record.get('record_id', 'record_id 없음')}`")
    core, remaining = display_core_fields(stage, payload)
    for label, value in core:
        lines.append(f"\n**{label}**\n\n{render_value(value)}")
    if stage == "independent_code":
        render_normalized_sections(lines, payload)
    if remaining:
        lines.append("\n**기타 기록 필드**\n")
        lines.append(render_value(remaining))
    if not payload:
        lines.append("\n기록 payload가 없습니다.")
    lines.append("")


def source_identifier_rows(source: dict[str, Any], records: list[dict[str, Any]]) -> list[tuple[str, Any]]:
    rows: list[tuple[str, Any]] = []
    id_keys = ("question_id", "source_id", "question_identifier", "source_identifier", "passage_id")
    seen: set[tuple[str, str]] = set()
    for key in id_keys:
        if key in source:
            marker = (key, json.dumps(source[key], ensure_ascii=False, sort_keys=True))
            if marker not in seen:
                rows.append((key, source[key]))
                seen.add(marker)
    for record in records:
        payload = record.get("payload")
        if not isinstance(payload, dict):
            continue
        for key in id_keys:
            if key in payload:
                marker = (key, json.dumps(payload[key], ensure_ascii=False, sort_keys=True))
                if marker not in seen:
                    rows.append((key, payload[key]))
                    seen.add(marker)
    return rows


def _path_candidates(value: Any) -> list[str]:
    if isinstance(value, str):
        return [value] if "/" in value and "." in Path(value).name else []
    if isinstance(value, dict):
        return [item for child in value.values() for item in _path_candidates(child)]
    if isinstance(value, list):
        return [item for child in value for item in _path_candidates(child)]
    return []


def resolve_source_path(raw: str) -> Path:
    path = Path(raw)
    return path if path.is_absolute() else ROOT / path


def source_audit(case_id: str, source: dict[str, Any], case_records: list[dict[str, Any]]) -> dict[str, Any]:
    refs = _path_candidates(source.get("provenance", {}))
    for record in case_records:
        payload = record.get("payload") if isinstance(record.get("payload"), dict) else {}
        refs.extend(_path_candidates(payload.get("source")))
        refs.extend(_path_candidates(payload.get("supplement")))
    refs = list(dict.fromkeys(refs))
    assets = [{"path": raw, "exists": resolve_source_path(raw).is_file(), "kind": "image" if Path(raw).suffix.lower() in {".png", ".jpg", ".jpeg", ".bmp", ".svg"} else "supplement_or_source"} for raw in refs]
    choices = source.get("choices")
    choice_values = list(choices.values()) if isinstance(choices, dict) else choices if isinstance(choices, list) else []
    all_empty = bool(choice_values) and all(value is None or (isinstance(value, str) and not value.strip()) for value in choice_values)
    missing_fields = [key for key in ("passage_text", "stem", "choices") if key not in source or source.get(key) in (None, "", [])]
    warnings = []
    if all_empty:
        warnings.append("선지 필드가 존재하지만 모든 선택지 값이 비어 있음")
    if missing_fields:
        warnings.append("원문 필드 누락/빈 값: " + ", ".join(missing_fields))
    broken = [item["path"] for item in assets if not item["exists"]]
    if broken:
        warnings.append("참조한 보충/원문 자산이 export에 없음: " + ", ".join(broken))
    return {
        "case_id": case_id, "source_file_exists": bool(source),
        "mechanically_linked": bool(source) and source.get("case_id", case_id) == case_id,
        "assets": assets, "image_files_exist": all(item["exists"] for item in assets if item["kind"] == "image"),
        "image_meaning_verified": False, "choice_count": len(choice_values), "all_choices_empty": all_empty,
        "warnings": warnings, "ready": bool(source) and not warnings,
    }


def case_group(records: list[dict[str, Any]], source: dict[str, Any]) -> Any:
    for record in records:
        payload = record.get("payload")
        if isinstance(payload, dict) and "passage_group" in payload:
            return payload["passage_group"]
    return source.get("passage_group")


def list_case_link_values(value: Any, case_id: str, key: str = "") -> bool:
    explicit_keys = {
        "case_ids", "window_cases", "cases", "affected_cases", "related_cases",
        "related_case_ids", "case_id", "case",
    }
    if key in explicit_keys:
        if value == case_id:
            return True
        if isinstance(value, list) and any(item == case_id for item in value):
            return True
    if isinstance(value, dict):
        return any(list_case_link_values(child, case_id, str(child_key)) for child_key, child in value.items())
    if isinstance(value, list):
        return any(list_case_link_values(child, case_id, key) for child in value)
    return False


def explicitly_linked_records(case_id: str, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
    case_record_ids = {
        record.get("record_id") for record in records if record.get("case") == case_id and record.get("record_id")
    }
    linked: list[dict[str, Any]] = []
    allowed_stages = {"depth_backfill", "boundary_revision", "induction", "meta_induction"}
    for record in records:
        if record.get("stage") not in allowed_stages:
            continue
        if record.get("case") == case_id:
            linked.append(record)
            continue
        payload = record.get("payload")
        if not isinstance(payload, dict):
            continue
        if list_case_link_values(payload, case_id):
            linked.append(record)
            continue
        referenced_ids = set()

        def collect_exact_strings(node: Any) -> None:
            if isinstance(node, str):
                if node in case_record_ids:
                    referenced_ids.add(node)
            elif isinstance(node, dict):
                for child in node.values():
                    collect_exact_strings(child)
            elif isinstance(node, list):
                for child in node:
                    collect_exact_strings(child)

        collect_exact_strings(payload)
        if referenced_ids:
            linked.append(record)
    return linked


def render_case(case_id: str, case_records: list[dict[str, Any]], source: dict[str, Any] | None,
                records: list[dict[str, Any]], selected: dict[str, dict[str, Any]]) -> str:
    source = source or {}
    group = case_group([selected["blind"]], source)
    lines = [
        f"> 이 파일은 원장으로부터 자동 생성된 열람용 파생본이다. 연구의 authoritative source는 raw queue이며, 이 파일을 직접 편집하지 않는다.",
        "",
        f"# {case_id}",
        "",
        "## 0. 문항 정보",
        "",
    ]
    if group is not None:
        lines.append(f"- **Passage group:** {compact_cell(group)}")
    identifiers = source_identifier_rows(source, case_records)
    if identifiers:
        lines.append("- **문항/source identifier:**")
        for key, value in identifiers:
            lines.append(f"  - `{key}`: {compact_cell(value)}")
    for key, label in (("passage_text", "제시문"), ("stem", "발문"), ("choices", "선지")):
        if key in source:
            lines.append(f"\n### {label}\n\n{render_value(source[key])}")
    if not source:
        lines.append("blind-only source 파일이 없습니다. 원문과 선지를 추정하지 않았습니다.")
    elif not any(key in source for key in ("passage_text", "stem", "choices")):
        lines.append("blind-only source에 제시문·발문·선지 필드가 없습니다.")
    lines.extend(["", "### 원문 자료 감사", "", json_fence(source_audit(case_id, source, case_records))])

    lines.extend(["", "## 1. 최초 blind 풀이", ""])
    put_payload(lines, "blind", selected["blind"])
    render_record_history(lines, "blind", case_records)

    lines.extend(["## 2. 공식 정답 대조", ""])
    put_payload(lines, "answer_check", selected["answer_check"])
    render_record_history(lines, "answer_check", case_records)

    lines.extend(["## 3. 독립 코드 판정", ""])
    put_payload(lines, "independent_code", selected["independent_code"])
    render_record_history(lines, "independent_code", case_records)

    lines.extend([
        "## 4. SDSS 사후 대조",
        "",
        "> SDSS는 독립 판정 후 공개된 제3자 후보 라벨이다. 이 기록은 독립 판정의 근거로 소급 사용하지 않는다.",
        "",
    ])
    put_payload(lines, "sdss_compare", selected["sdss_compare"])
    render_record_history(lines, "sdss_compare", case_records)

    linked = explicitly_linked_records(case_id, records)
    supplements = [r for r in linked if r.get("stage") in {"depth_backfill", "boundary_revision"}]
    related_group = [r for r in linked if r.get("stage") in {"induction", "meta_induction"}]
    lines.extend(["## 5. 후속 보강", ""])
    if supplements:
        lines.append("아래 기록은 시간순으로 덧붙였다. 최초 blind·정답·독립 코드 판정을 대체하지 않는다.\n")
        for record in supplements:
            put_payload(lines, str(record.get("stage")), record)
    else:
        lines.append("이 case에 명시적으로 연결된 depth_backfill 또는 case-specific boundary_revision 기록이 없습니다.\n")
    if related_group:
        lines.append("### 명시적으로 연결된 집단 기록 참조\n")
        for record in related_group:
            lines.append(f"- `{record.get('record_id', 'record_id 없음')}` — {STAGE_LABELS.get(str(record.get('stage')), str(record.get('stage')))} (집단/교차 사례 기록; 개별 case 판단으로 변환하지 않음)")

    lines.extend(["", "## 6. 원장 추적", "", "사용된 원장 record_id (queue 순서):"])
    ids_seen: set[str] = set()
    tracking_records = list(case_records)
    tracking_records.extend(r for r in linked if r not in case_records)
    tracking_records.sort(key=lambda r: int(r.get("_queue_index", -1)))
    for record in tracking_records:
        record_id = record.get("record_id")
        if not record_id or record_id in ids_seen:
            continue
        ids_seen.add(record_id)
        lines.append(f"- `{record_id}` — {STAGE_LABELS.get(str(record.get('stage')), str(record.get('stage')))} / {record.get('status', '상태 없음')}")
    if not ids_seen:
        lines.append("- 사용된 record_id 없음")
    return "\n".join(lines).rstrip() + "\n"


def render_record_history(lines: list[str], stage: str, case_records: list[dict[str, Any]]) -> None:
    history = [record for record in case_records if record.get("stage") == stage]
    if len(history) <= 1:
        return
    lines.append("\n**동일 단계 원문 기록 이력(최초 기록 보존)**\n")
    for index, record in enumerate(history, 1):
        lines.append(f"- 기록 {index}: `{record.get('record_id', 'record_id 없음')}` / `{record.get('status', '상태 없음')}`")
        put_payload(lines, stage, record)


def compact_cell(value: Any) -> str:
    if value is None:
        return "—"
    text = json.dumps(value, ensure_ascii=False, separators=(",", ":")) if not isinstance(value, str) else value
    return text.replace("|", "\\|").replace("\r", " ").replace("\n", "<br>")


def compact_code_cell(value: Any) -> str:
    """Expose only stored code identifiers in the index; full records remain in each view."""
    if isinstance(value, list):
        parts = [compact_code_cell(item) for item in value]
        return ", ".join(part for part in parts if part) or "—"
    if isinstance(value, dict) and "code" in value:
        code = value["code"]
        name = value.get("name")
        if name is not None:
            return f"#{code} {compact_cell(name)}"
        return f"#{code}"
    return compact_cell(value)


def first_payload_value(record: dict[str, Any] | None, keys: tuple[str, ...]) -> Any:
    if not record:
        return None
    payload = record.get("payload")
    if not isinstance(payload, dict):
        return None
    for key in keys:
        if key in payload:
            return payload[key]
    return None


def index_markdown(records: list[dict[str, Any]], case_order: list[str], complete: dict[str, dict[str, dict[str, Any]]],
                   incomplete: dict[str, list[dict[str, Any]]], sources: dict[str, dict[str, Any]], generated_at: str,
                   meta_total: int) -> str:
    complete_rows = []
    for case_id in case_order:
        if case_id not in complete:
            continue
        chosen = complete[case_id]
        group = case_group([chosen["blind"]], sources.get(case_id, {}))
        initial = first_payload_value(chosen["blind"], ("selected_answer", "answer"))
        official = first_payload_value(chosen["answer_check"], ("official_answer",))
        primary = first_payload_value(chosen["independent_code"], ("primary",))
        site = first_payload_value(chosen["sdss_compare"], ("site_original_codes", "original_site_tags", "site_original_tags"))
        if not nonempty(site):
            site = "태그 미확보/비교불가"
        complete_rows.append((case_id, group, "완료", initial, official, primary, site))

    lines = [
        "# 문항별 연구 결과 색인",
        "",
        f"- 완전 완료 문항 수: **{len(complete)}**",
        f"- 생성 시각: **{generated_at}**",
        f"- 미완료 case 수: **{len(incomplete)}**",
        f"- source queue record 수: **{len(records)}**",
        f"- meta_state.py completed_questions_total: **{meta_total}**",
        "",
        "## 완전 완료 문항",
        "",
        "| Case | Passage Group | 상태 | 최초답 | 공식답 | 독립 주 코드 | SDSS | 파일 |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for case_id, group, status, initial, official, primary, site in complete_rows:
        lines.append(
            f"| {case_id} | {compact_cell(group)} | {status} | {compact_cell(initial)} | {compact_cell(official)} | {compact_code_cell(primary)} | {compact_cell(site)} | [{case_id}](./{case_id}.md) |"
        )
    lines.extend(["", "## 진행 중", ""])
    if incomplete:
        lines.extend([
            "아래 문항은 필요한 네 단계 중 하나 이상이 없거나 `done`이 아니어서 완성본 파일을 만들지 않았습니다.",
            "",
            "| Case | Passage Group | 단계 상태 | 파일 |",
            "|---|---|---|---|",
        ])
        for case_id, case_records in incomplete.items():
            blind = latest_done(case_records, "blind") or latest_status_record(case_records, "blind")
            payload = blind.get("payload", {}) if blind else {}
            group = payload.get("passage_group") if isinstance(payload, dict) else None
            states = []
            for stage in REQUIRED_STAGES:
                done_record = latest_done(case_records, stage)
                event = done_record or latest_status_record(case_records, stage)
                if done_record:
                    state = "완료"
                elif event:
                    state = str(event.get("status", "기록됨"))
                else:
                    state = "대기"
                states.append(f"{stage}={state}")
            lines.append(f"| {case_id} | {compact_cell(group)} | {compact_cell(' · '.join(states))} | — |")
    else:
        lines.append("미완료 문항이 없습니다.")
    lines.append("")
    return "\n".join(lines)


def nonempty(value: Any) -> bool:
    return value not in (None, "", [], {}, ())


def load_manifest() -> dict[str, dict[str, Any]]:
    if not MANIFEST_PATH.is_file():
        return {}
    result = {}
    for line in MANIFEST_PATH.read_text(encoding="utf-8").splitlines():
        if line.strip():
            row = json.loads(line)
            if isinstance(row, dict) and isinstance(row.get("case_id"), str):
                result[row["case_id"]] = row
    return result


def build_derived_indexes(records: list[dict[str, Any]], candidate_cases: list[str], complete: dict[str, Any],
                          incomplete: dict[str, list[dict[str, Any]]], sources: dict[str, dict[str, Any]],
                          by_case: dict[str, list[dict[str, Any]]], manifest: dict[str, dict[str, Any]]) -> dict[str, Any]:
    source_audits = {case: source_audit(case, sources.get(case, {}), by_case[case]) for case in candidate_cases}
    tag_missing = []
    unresolved = []
    for case in candidate_cases:
        sdss = latest_done(by_case[case], "sdss_compare")
        tags = first_payload_value(sdss, FIELD_ALIASES["site_tags"])
        if sdss and not nonempty(tags):
            tag_missing.append(case)
        for record in by_case[case]:
            value = first_payload_value(record, ("unresolved",))
            if nonempty(value):
                unresolved.append({"case_id": case, "record_id": record.get("record_id"), "stage": record.get("stage"), "value": value})
    # Count code-bearing records once by record_id, even when a revision links several cases.
    code_rows: dict[str, dict[str, Any]] = {}
    for record in records:
        if record.get("stage") != "independent_code" or record.get("status") != "done":
            continue
        rid = record.get("record_id")
        if not rid or rid in code_rows:
            continue
        payload = record.get("payload") if isinstance(record.get("payload"), dict) else {}
        case_links = [record.get("case")] if isinstance(record.get("case"), str) else []
        for key in ("case_ids", "affected_cases", "related_case_ids"):
            if isinstance(payload.get(key), list):
                case_links.extend(item for item in payload[key] if isinstance(item, str))
        code_rows[rid] = {"record_id": rid, "case_ids": sorted(set(case_links)), "payload": payload}
    code_index: dict[str, dict[str, Any]] = {}
    for row in code_rows.values():
        payload = row["payload"]
        for field in ("primary", "auxiliary", "secondary"):
            value = payload.get(field)
            values = value if isinstance(value, list) else [value] if value is not None else []
            for item in values:
                code = item.get("code") if isinstance(item, dict) else item if isinstance(item, (int, str)) else None
                if code is None:
                    continue
                entry = code_index.setdefault(str(code), {"code": code, "case_ids": set(), "passage_groups": set(), "record_ids": set(), "roles": set()})
                entry["case_ids"].update(row["case_ids"])
                entry["record_ids"].add(row["record_id"])
                entry["roles"].add(field)
                for case in row["case_ids"]:
                    group = case_group(by_case.get(case, []), sources.get(case, {}))
                    if group is not None:
                        entry["passage_groups"].add(str(group))
    for entry in code_index.values():
        for key in ("case_ids", "passage_groups", "record_ids", "roles"):
            entry[key] = sorted(entry[key])
        entry["case_count"] = len(entry["case_ids"])
        entry["passage_group_count"] = len(entry["passage_groups"])
    prepared_cases = set(manifest)
    completed_cases = set(complete)
    prepared_completed = sorted(completed_cases & prepared_cases)
    legacy_completed = sorted(completed_cases - prepared_cases)
    return {
        "schema_version": 2,
        "case_order": candidate_cases,
        "prepared": {"manifest_case_count": len(prepared_cases), "completed_case_ids": prepared_completed, "completed_case_count": len(prepared_completed)},
        "legacy": {"completed_case_ids": legacy_completed, "completed_case_count": len(legacy_completed)},
        "source_incomplete_case_ids": sorted(case for case, audit in source_audits.items() if not audit["ready"]),
        "source_audits": source_audits,
        "sdss_tag_missing_case_ids": sorted(set(tag_missing)),
        "unresolved": unresolved,
        "code_index": code_index,
        "record_dedupe": {"independent_code_unique_record_count": len(code_rows)},
    }


def load_meta_state() -> dict[str, Any]:
    try:
        value = json.loads(META_STATE_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ViewBuildError(f"meta_state.json이 JSON이 아닙니다: {exc}") from exc
    if not isinstance(value, dict) or not isinstance(value.get("completed_questions_total"), int):
        raise ViewBuildError("meta_state.py에 정수 completed_questions_total 필드가 없습니다.")
    return value


def write_atomic(path: Path, content: str) -> None:
    temporary = path.with_name(path.name + ".tmp")
    with temporary.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(content)
        stream.flush()
        os.fsync(stream.fileno())
    temporary.replace(path)


def main() -> int:
    if not QUEUE_PATH.is_file():
        raise ViewBuildError(f"queue 파일이 없습니다: {QUEUE_PATH}")
    tracked_inputs = [QUEUE_PATH, MANIFEST_PATH, META_STATE_PATH]
    if PROCESSED_PATH.is_file():
        tracked_inputs.append(PROCESSED_PATH)
    tracked_inputs.extend(sorted(path for path in BLIND_DIR.rglob("*") if path.is_file()))
    before = {path: file_fingerprint(path) for path in tracked_inputs}
    records = read_jsonl(QUEUE_PATH)

    by_case: dict[str, list[dict[str, Any]]] = defaultdict(list)
    blind_order: list[str] = []
    seen_blind: set[str] = set()
    for record in records:
        case_id = record.get("case")
        if not isinstance(case_id, str) or not case_id:
            continue
        by_case[case_id].append(record)
        if record.get("stage") == "blind" and case_id not in seen_blind:
            seen_blind.add(case_id)
            blind_order.append(case_id)

    # Only cases with a blind-stage record are question candidates. Group-level hold/meta records
    # are never mistaken for individual questions.
    candidate_cases = [case_id for case_id in blind_order if re.fullmatch(r"[A-Za-z0-9_-]+", case_id)]
    if len(candidate_cases) != len(blind_order):
        invalid = [case_id for case_id in blind_order if not re.fullmatch(r"[A-Za-z0-9_-]+", case_id)]
        raise ViewBuildError(f"안전한 파일명으로 쓸 수 없는 case ID가 blind stage에 있습니다: {invalid}")

    source_by_case: dict[str, dict[str, Any]] = {}
    for case_id in candidate_cases:
        path = BLIND_DIR / f"{case_id}.json"
        if path.is_file():
            before[path] = file_fingerprint(path)
            try:
                source = json.loads(path.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                raise ViewBuildError(f"{path}: JSON 파싱 실패: {exc}") from exc
            if not isinstance(source, dict):
                raise ViewBuildError(f"{path}: blind source가 JSON 객체가 아닙니다.")
            source_by_case[case_id] = source

    selected_by_case: dict[str, dict[str, dict[str, Any]]] = {}
    incomplete: dict[str, list[dict[str, Any]]] = {}
    for case_id in candidate_cases:
        case_records = by_case[case_id]
        selected = {stage: latest_done(case_records, stage) for stage in REQUIRED_STAGES}
        blind_records = [r for r in case_records if r.get("stage") == "blind" and r.get("status") == "done"]
        if blind_records:
            selected["blind"] = blind_records[0]
        if all(selected.values()):
            selected_by_case[case_id] = selected  # type: ignore[assignment]
        else:
            incomplete[case_id] = case_records

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for case_id, selected in selected_by_case.items():
        content = render_case(case_id, by_case[case_id], source_by_case.get(case_id), records, selected)
        write_atomic(OUTPUT_DIR / f"{case_id}.md", content)

    # The generated directory is a derived artifact. Remove stale case views from earlier runs.
    current_files = {f"{case_id}.md" for case_id in selected_by_case}
    for path in OUTPUT_DIR.glob("*.md"):
        if path.name == "INDEX.md" or not re.fullmatch(r"[A-Za-z0-9_-]+\.md", path.name):
            continue
        if path.name not in current_files:
            path.unlink()

    meta = load_meta_state()
    meta_total = meta["completed_questions_total"]
    generated_at = datetime.now(ZoneInfo("Asia/Seoul")).isoformat(timespec="seconds")
    index_content = index_markdown(
        records, blind_order, selected_by_case, incomplete, source_by_case, generated_at, meta_total
    )
    write_atomic(OUTPUT_DIR / "INDEX.md", index_content)
    derived = build_derived_indexes(records, candidate_cases, selected_by_case, incomplete, source_by_case, by_case, load_manifest())
    write_atomic(OUTPUT_DIR / "RESEARCH_VIEW_INDEX.json", json.dumps(derived, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    write_atomic(OUTPUT_DIR / "SOURCE_AUDIT.json", json.dumps(derived["source_audits"], ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    write_atomic(OUTPUT_DIR / "CODE_COVERAGE.json", json.dumps(derived["code_index"], ensure_ascii=False, indent=2, sort_keys=True) + "\n")

    # Confirm input files remained byte- and metadata-identical during generation.
    changed_inputs = []
    for path, old_fingerprint in before.items():
        try:
            if file_fingerprint(path) != old_fingerprint:
                changed_inputs.append(str(path.relative_to(ROOT)))
        except OSError:
            changed_inputs.append(str(path.relative_to(ROOT)) + " (사라짐)")

    missing_stage_cases = []
    for case_id, selected in selected_by_case.items():
        for stage in REQUIRED_STAGES:
            record = latest_done(by_case[case_id], stage)
            if record is None or record.get("status") != "done":
                missing_stage_cases.append(f"{case_id}:{stage}")

    manifest_ids = set(load_manifest())
    prepared_selected = set(selected_by_case) & manifest_ids
    meta_ids = set(meta.get("completed_case_ids", [])) & manifest_ids
    count_matches = prepared_selected == meta_ids
    print(f"생성 경로: {OUTPUT_DIR}")
    print(f"완전 완료 case: {len(selected_by_case)}")
    print(f"진행 중 case: {len(incomplete)}")
    print(f"prepared 완료 case: {len(derived['prepared']['completed_case_ids'])}")
    print(f"legacy 완료 case: {len(derived['legacy']['completed_case_ids'])}")
    print(f"source incomplete: {len(derived['source_incomplete_case_ids'])}")
    print(f"SDSS tag missing: {len(derived['sdss_tag_missing_case_ids'])}")
    print(f"unresolved: {len(derived['unresolved'])}")
    print(f"source queue record 수: {len(records)}")
    print(f"meta_state.py completed_questions_total: {meta_total}")
    print("대표 파일: " + ", ".join(f"{case_id}.md" for case_id in (
        next(iter(selected_by_case), "—"),
        list(selected_by_case)[len(selected_by_case) // 2] if selected_by_case else "—",
        next(reversed(selected_by_case), "—"),
    )))

    errors = []
    if not count_matches:
        extras = sorted(prepared_selected - meta_ids)
        absent = sorted(meta_ids - prepared_selected)
        extras_without_blind_source = sorted(case_id for case_id in extras if case_id not in source_by_case)
        source_note = (
            f" 이 가운데 blind_sources 파일이 없는 case: {extras_without_blind_source}."
            if extras_without_blind_source else ""
        )
        errors.append(
            f"prepared scope 완료 집합 불일치: queue {len(prepared_selected)}개, "
            f"meta_state completed_case_ids {len(meta_ids)}개. "
            f"meta_state completed_case_ids에 없는 단계완료 case: {extras or '없음'}; "
            f"meta 목록에는 있으나 queue 조건을 충족하지 않는 case: {absent or '없음'}.{source_note} "
            "파일 수를 강제로 맞추지 않았습니다."
        )
    if missing_stage_cases:
        errors.append("완료 파일의 필수 stage 누락: " + ", ".join(missing_stage_cases))
    if changed_inputs:
        errors.append("원본 입력 hash/size/mtime 변경 감지: " + ", ".join(changed_inputs))
    else:
        print("원본 queue/processed/manifest/blind source hash·size·mtime 변경: 없음")
    after = {path: file_fingerprint(path) for path in before if path.is_file()}
    snapshot = {
        "schema_version": 1,
        "queue_last_record_id": records[-1].get("record_id") if records else None,
        "tracked_input_count": len(before),
        "before": {str(path.relative_to(ROOT)): list(value) for path, value in before.items()},
        "after": {str(path.relative_to(ROOT)): list(after.get(path, ())) for path in before},
        "unchanged": not changed_inputs,
    }
    write_atomic(OUTPUT_DIR / "VIEW_BUILD_SNAPSHOT.json", json.dumps(snapshot, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    if errors:
        for error in errors:
            print("검증 오류: " + error, file=sys.stderr)
        return 1
    print("검증: 완료 수 일치, 필수 stage 존재, 원본 무변경")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ViewBuildError as exc:
        print(f"오류: {exc}", file=sys.stderr)
        raise SystemExit(2)
