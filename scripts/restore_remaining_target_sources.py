#!/usr/bin/env python3
"""Deterministic source-only restoration for current NEEDS_RESTORE targets.

The parser never prints source text and never opens answer/SDSS or semantic
research files. Run without arguments for a read-only dry run; pass --commit
to write prepared blind sources and explicit unresolved restoration records.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/기본기_연구"
PREP = BASE / "prepared_backlog"
TARGET = BASE / "target_completion_crosswalk_v1.jsonl"
MANIFEST = PREP / "manifest.jsonl"
MAPPING = PREP / "sealed/provenance_mapping.jsonl"
ANSWERS = PREP / "sealed/answer_sdss.jsonl"
RESTORATIONS = PREP / "sealed/source_restorations_v1.jsonl"
RULES = [
    "all_group_blind_records_before_any_group_answer_check",
    "all_group_independent_code_records_before_any_group_sdss_disclosure",
]
LABELS = ["①", "②", "③", "④", "⑤"]
RANGE_RE = re.compile(r"^\s*(?:#{1,6}\s*)?\[(\d+)\s*[~～〜–—-]\s*(\d+)\][^\n]*$", re.M)
QUESTION_HEADING_RE = re.compile(r"^\s*#{2,6}\s+(\d+)\.\s*([^\n]*)$", re.M)
ANSWER_HEADING_RE = re.compile(r"^\s*##\s*(?:정답|해설|대조\s*메모)(?:\s|$)[^\n]*$", re.M)
VISUAL_RE = re.compile(r"<(?:그림|표)>|\[(?:그림|표)\]|!\[|\[시각\s*자료", re.I)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_name, path)
    except Exception:
        try:
            os.unlink(temp_name)
        except FileNotFoundError:
            pass
        raise


def append_jsonl(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    payload = "".join(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n" for row in rows).encode("utf-8")
    path.parent.mkdir(parents=True, exist_ok=True)
    fd = os.open(path, os.O_WRONLY | os.O_APPEND | os.O_CREAT, 0o644)
    try:
        os.write(fd, payload)
        os.fsync(fd)
    finally:
        os.close(fd)


def alpha_value(value: str) -> int:
    result = 0
    for char in value:
        result = result * 26 + ord(char) - 64
    return result


def alpha(number: int) -> str:
    out = ""
    while number:
        number, rem = divmod(number - 1, 26)
        out = chr(65 + rem) + out
    return out


def trim_sealed_tail(text: str) -> str:
    match = ANSWER_HEADING_RE.search(text)
    return text[:match.start()] if match else text


def parse_choice_body(body: str, allow_empty_stem: bool = False) -> tuple[str, list[str]] | None:
    matches = list(re.finditer(r"([①②③④⑤])\s*", body))
    start = -1
    for i in range(len(matches) - 4):
        if [m.group(1) for m in matches[i:i + 5]] == LABELS:
            start = i
            break
    if start < 0:
        return None
    marks = matches[start:start + 5]
    stem = body[:marks[0].start()].strip()
    choices = [body[mark.end():marks[i + 1].start() if i < 4 else len(body)].strip()
               for i, mark in enumerate(marks)]
    if (not allow_empty_stem and not stem) or len(choices) != 5 or any(not x for x in choices):
        return None
    return stem, choices



def rewind_visual_stem_prefix(tail: str, split: int) -> int:
    """Rewind a legacy stem split when a short visual-reference prefix
    immediately before the split actually belongs to the next question.

    Examples:
        위 글의
        <그림>

        에 대한 설명으로 ...

        <그림>
        와
        <그림>

        의 공통적인 원인이 ...
    """
    right = tail[split:].strip()

    # Keep this deliberately narrow. These are continuation forms that
    # normally cannot constitute the beginning of a complete question
    # when a visual-reference phrase immediately precedes them.
    if not re.match(r"^(?:에\s+대한|의(?:\s|$))", right):
        return split

    left = tail[:split]

    blanks = list(re.finditer(r"\n\s*\n", left))

    for match in reversed(blanks):
        suffix = left[match.end():].strip()

        if not suffix:
            continue

        # Only rewind a short reference phrase containing a visual marker.
        if len(suffix) > 80:
            continue

        if not re.search(r"<(?:그림|표)>", suffix):
            continue

        # It must not contain choices or an already-complete sentence.
        if re.search(r"[①②③④⑤]", suffix):
            continue

        if re.search(r"[?？]", suffix):
            continue

        return match.start()

    return split


def legacy_stem_cut(tail: str) -> int:
    def accepted(right: str) -> bool:
        # The prompt can be followed by supplementary material. Judge only
        # the first paragraph of the candidate stem, and ignore a trailing
        # score annotation such as "[3점]".
        prompt = re.split(r"\n\s*\n", right.strip(), maxsplit=1)[0].strip()
        prompt = re.sub(r"\s*\[\s*\d+\s*점\s*\]\s*$", "", prompt).strip()
        prompt = re.split(r"\n\s*<(?:그림|표)>", prompt, maxsplit=1)[0].strip()
        return len(prompt) >= 8 and bool(re.search(r"[?？]$", prompt)) and not re.search(r"[①②③④⑤]", prompt)

    blanks = list(re.finditer(r"\n\s*\n", tail))
    for match in reversed(blanks):
        left = tail[:match.start()].strip()
        right = tail[match.end():].strip()
        if left and accepted(right):
            return rewind_visual_stem_prefix(tail, match.start())
    breaks = list(re.finditer(r"\n", tail))
    for match in reversed(breaks):
        left = tail[:match.start()].strip()
        right = tail[match.end():].strip()
        if left and accepted(right):
            return rewind_visual_stem_prefix(tail, match.start())
    return -1


def legacy_stem_cut_with_inline_supplement(tail: str) -> int:
    """Fallback only when strict legacy_stem_cut() fails.

    Accept a candidate next-question stem when its first paragraph contains
    a question mark and a supplementary marker begins shortly after it.
    This handles structures such as a prompt referring to <보기>, followed
    by the actual <보기> material in the same paragraph.
    """
    def accepted(right: str) -> bool:
        first = re.split(r"\n\s*\n", right.strip(), maxsplit=1)[0].strip()

        if len(first) < 8 or re.search(r"[①②③④⑤]", first):
            return False

        qpos = max(first.rfind("?"), first.rfind("？"))
        if qpos < 0:
            return False

        after = first[qpos + 1:]
        marker = re.search(r"<(?:보기|가정|그림|표)>", after)
        if marker is None:
            return False

        # Keep this fallback narrow: the supplementary marker must begin
        # shortly after the question mark.
        return marker.start() <= 16

    blanks = list(re.finditer(r"\n\s*\n", tail))
    for match in reversed(blanks):
        left = tail[:match.start()].strip()
        right = tail[match.end():].strip()
        if left and accepted(right):
            return match.start()

    breaks = list(re.finditer(r"\n", tail))
    for match in reversed(breaks):
        left = tail[:match.start()].strip()
        right = tail[match.end():].strip()
        if left and accepted(right):
            return match.start()

    return -1


def exact_range_block(text: str, start: int, end: int, allow_range_alias: bool = False) -> tuple[str, str] | None:
    ranges = list(RANGE_RE.finditer(text))
    hits = [i for i, m in enumerate(ranges) if (int(m.group(1)), int(m.group(2))) == (start, end)]
    if len(hits) == 1:
        i = hits[0]
    elif allow_range_alias and not hits and len(ranges) == 1:
        i = 0
    else:
        return None
    head = ranges[i]
    stop = ranges[i + 1].start() if i + 1 < len(ranges) else len(text)
    return text[head.end():stop], text[head.start():stop]


def parse_markdown_group(raw: str, start: int, end: int, allow_range_alias: bool = False) -> tuple[str, dict[int, dict]] | None:
    usable = trim_sealed_tail(raw)
    block_info = exact_range_block(usable, start, end, allow_range_alias)
    if block_info is None:
        return None
    block, _full = block_info
    count = end - start + 1
    heads = list(QUESTION_HEADING_RE.finditer(block))
    if heads:
        nums = [int(h.group(1)) for h in heads]
        if nums == list(range(start, end + 1)):
            mapped = list(range(start, end + 1))
        elif nums == list(range(1, count + 1)) and start != 1:
            mapped = list(range(start, end + 1))
        else:
            mapped = []
        if mapped:
            passage = block[:heads[0].start()].strip()
            questions: dict[int, dict] = {}
            for i, h in enumerate(heads):
                stop = heads[i + 1].start() if i + 1 < len(heads) else len(block)
                body = block[h.end():stop].strip()
                parsed = parse_choice_body(body, allow_empty_stem=True)
                if parsed is None:
                    return None
                stem, choices = parsed
                heading_text = h.group(2).strip()
                if heading_text:
                    stem = f"{heading_text}\n\n{stem}".strip()
                if not stem:
                    return None
                questions[mapped[i]] = {"stem": stem, "choices": choices}
            if passage and set(questions) == set(range(start, end + 1)):
                return passage, questions

    explicit = list(re.finditer(r"^\s*(\d+)\.\s*", block, re.M))
    explicit = [m for m in explicit if start <= int(m.group(1)) <= end]
    if [int(m.group(1)) for m in explicit] == list(range(start, end + 1)):
        passage = block[:explicit[0].start()].strip()
        questions = {}
        for i, h in enumerate(explicit):
            stop = explicit[i + 1].start() if i + 1 < len(explicit) else len(block)
            body = block[h.end():stop].strip()
            parsed = parse_choice_body(body)
            if parsed is None:
                return None
            stem, choices = parsed
            questions[int(h.group(1))] = {"stem": stem, "choices": choices}
        if passage and set(questions) == set(range(start, end + 1)):
            return passage, questions

    # Legacy canonical Markdown uses a common passage followed by unnumbered
    # prompts, with each five-choice cycle serving as the question boundary.
    markers = list(re.finditer(r"([①②③④⑤])\s*", block))
    cycles = []
    cursor = 0
    while cursor + 4 < len(markers):
        if [m.group(1) for m in markers[cursor:cursor + 5]] == LABELS:
            cycles.append(markers[cursor:cursor + 5])
            cursor += 5
        else:
            cursor += 1
    if len(cycles) != count:
        return None
    first_prefix = block[:cycles[0][0].start()]
    first_cut = legacy_stem_cut(first_prefix)
    if first_cut < 0:
        return None
    passage = first_prefix[:first_cut].strip()
    first_stem = first_prefix[first_cut:].strip()
    if not passage or not first_stem:
        return None
    questions = {}
    for i, cycle in enumerate(cycles):
        stem = first_stem
        choice5_end = len(block)
        if i > 0:
            between = block[cycles[i - 1][4].end():cycle[0].start()]
            split = legacy_stem_cut(between)
            if split < 0:
                split = legacy_stem_cut_with_inline_supplement(between)
            if split < 0:
                return None
            stem = between[split:].strip()
        if i + 1 < len(cycles):
            between = block[cycle[4].end():cycles[i + 1][0].start()]
            split = legacy_stem_cut(between)
            if split < 0:
                split = legacy_stem_cut_with_inline_supplement(between)
            if split < 0:
                return None
            choice5_end = cycle[4].end() + split
        choices = [block[m.end():cycle[j + 1].start() if j < 4 else choice5_end].strip()
                   for j, m in enumerate(cycle)]
        if not stem or any(not x for x in choices):
            return None
        questions[start + i] = {"stem": stem, "choices": choices}
    return passage, questions


def safe_object(pairs):
    allowed = {
        "question_id", "question_number", "passage_id", "group_id", "passage_text", "passage",
        "passage_markdown", "stem", "prompt", "prompt_markdown", "choices", "label", "text",
        "visual", "visual_assets", "visual_material", "source", "canonical_markdown", "content",
        "markdown", "passage_content",
        "canonical_markdown_sha256", "verification_status", "official_pages", "verification",
    }
    return {k: v for k, v in pairs if k in allowed}


def load_filtered_jsonl(path: Path, wanted_ids: set[str], id_fields: tuple[str, ...] = ("question_id",)) -> dict[str, dict]:
    found = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not any(qid in line for qid in wanted_ids):
            continue
        row = json.loads(line, object_pairs_hook=safe_object)
        key = next((row.get(field) for field in id_fields if row.get(field) in wanted_ids), None)
        if key in wanted_ids:
            found[key] = row
    return found


def parse_json_question(row: dict, expected_passage_id: str, require_passage: bool = True) -> tuple[str | None, str, list[str]] | None:
    if row.get("passage_id", row.get("group_id")) != expected_passage_id:
        return None
    passage = row.get("passage_text") or row.get("passage") or row.get("passage_markdown") or row.get("passage_content") or row.get("content")
    stem = row.get("stem") or row.get("prompt_markdown") or row.get("prompt")
    choices_raw = row.get("choices")
    if (require_passage and (not isinstance(passage, str) or not passage.strip())) or not isinstance(stem, str) or not stem.strip():
        return None
    if not isinstance(choices_raw, list) or len(choices_raw) != 5:
        return None
    choices = []
    for i, item in enumerate(choices_raw):
        if isinstance(item, dict):
            label = item.get("label") or LABELS[i]
            value = item.get("text")
        else:
            label, value = LABELS[i], item
        if not isinstance(value, str) or not value.strip() or label != LABELS[i]:
            return None
        choices.append(f"{label} {value.strip()}")
    return (passage.strip() if isinstance(passage, str) else None), stem.strip(), choices



def restore_verified_leet_visual_text(
    year_folder: str,
    start: int,
    end: int,
    passage: str,
    questions: dict[int, dict],
) -> tuple[str, dict[int, dict]] | None:
    """Restore only locally verified text objects and extraction artifacts.

    This is deliberately narrow. It does not infer visual content and does
    not apply to any LEET group other than the explicitly verified groups
    below.
    """
    visual_re = re.compile(r"<(?:그림|표)>|\[(?:그림|표)\]")

    def replace_exact(text: str, replacements: list[str]) -> str | None:
        markers = list(visual_re.finditer(text))

        # Also tolerate an already-restored source.
        if not markers:
            return text if all(x in text for x in replacements) else None

        if len(markers) != len(replacements):
            return None

        out = []
        last = 0
        for marker, replacement in zip(markers, replacements):
            out.append(text[last:marker.start()])
            out.append(replacement)
            last = marker.end()
        out.append(text[last:])
        return "".join(out)

    # Work on a copy so a failed validation cannot partially mutate input.
    restored_questions = {
        n: {
            "stem": q["stem"],
            "choices": list(q["choices"]),
        }
        for n, q in questions.items()
    }

    if year_folder == "2009" and (start, end) == (8, 10):
        new_passage = replace_exact(
            passage,
            ["‘중간 상인’ 역할", "수직적 계열화"],
        )
        new_q9 = replace_exact(
            restored_questions[9]["stem"],
            ["‘중간 상인’ 역할"],
        )
        new_q10 = replace_exact(
            restored_questions[10]["stem"],
            ["수직적 계열화"],
        )

        if None in (new_passage, new_q9, new_q10):
            return None

        restored_questions[9]["stem"] = new_q9
        restored_questions[10]["stem"] = new_q10
        return new_passage, restored_questions

    if year_folder == "2009" and (start, end) == (17, 19):
        new_passage = replace_exact(
            passage,
            [
                "두 뺨에 서린 발그레한 홍조",
                "온 방 안에 가득 찬 금빛",
            ],
        )
        new_q18 = replace_exact(
            restored_questions[18]["stem"],
            [
                "두 뺨에 서린 발그레한 홍조",
                "온 방 안에 가득 찬 금빛",
            ],
        )

        if None in (new_passage, new_q18):
            return None

        restored_questions[18]["stem"] = new_q18
        return new_passage, restored_questions

    # 2009 preliminary: HWP control-coordinate verification found no
    # visual/table controls inside these exact passage spans. The Markdown
    # <표> tokens occur only between otherwise continuous prose and are
    # extraction artifacts, so remove only the exact verified counts.
    if year_folder == "2009예비" and (start, end) == (11, 13):
        new_passage = replace_exact(passage, ["", ""])
        if new_passage is None:
            return None
        return new_passage, restored_questions

    if year_folder == "2009예비" and (start, end) == (22, 25):
        new_passage = replace_exact(passage, [""])
        if new_passage is None:
            return None
        return new_passage, restored_questions

    if year_folder == "2009예비" and (start, end) == (32, 34):
        new_passage = replace_exact(passage, ["", ""])
        if new_passage is None:
            return None
        return new_passage, restored_questions

    # 2010 Q19-21: the leading marker maps to a one-cell HWP table control
    # (page 8, anchor paragraph 266). Its complete content is prose and has
    # no row/column relation to preserve.
    if year_folder == "2010" and (start, end) == (19, 21):
        new_passage = replace_exact(
            passage,
            [
                "등장인물들은 조당전의 집에서 <영월행 일기>에 따라 역할놀이를 한다. "
                "이어서 <세조실록>과 <해안지록>을 함께 놓고 원탁 독회를 하며 관련 내용을 확인한다. "
                "서재 뒤편에는 다른 방으로 통하는 미닫이문이 있다. 역할놀이를 위해 소도구가 사용된다."
            ],
        )
        if new_passage is None:
            return None
        return new_passage, restored_questions

    # 2011 Q6-8: both markers map in document order to the same actual
    # textbox text, in the passage and Q6 stem respectively.
    if year_folder == "2011" and (start, end) == (6, 8):
        new_passage = replace_exact(passage, ["철학적 근대"])
        new_q6 = replace_exact(restored_questions[6]["stem"], ["철학적 근대"])
        if None in (new_passage, new_q6):
            return None
        restored_questions[6]["stem"] = new_q6
        return new_passage, restored_questions

    # 2011 Q9-11: passage and Q10 markers map to the textbox phrase. Q11's
    # marker maps to a 3x2 HWP view-box with one continuous prose cell; the
    # remaining cells are empty layout cells, so no spatial data is lost.
    if year_folder == "2011" and (start, end) == (9, 11):
        view_box = (
            "<보 기> 경기 도중 득점 기회를 잡은 선수 A를 막으려고 상대 팀 선수 B가 정당하게 몸싸움을 벌였다. "
            "하지만 다음 순간 A는 경기장이 미끄러운 탓에 몸싸움을 이기지 못하고 넘어졌다. "
            "심판 C는 이 상황을 제대로 보지 못하고 B를 퇴장시켰다. "
            "심판은 판정 과정에서 어떠한 영향도 받지 않아야 하는 지위에 있기 때문에, "
            "B의 팀은 C의 판정에 따라 한 명이 줄어든 상태에서 경기를 해야 했다. "
            "감독 D는 수비 약화를 우려하여, 뛰고 있던 공격수를 빼고 몸을 풀고 대기 중인 선수 E를 투입했다."
        )
        new_passage = replace_exact(passage, ["권리의 문법"])
        new_q10 = replace_exact(restored_questions[10]["stem"], ["권리의 문법"])
        new_q11 = replace_exact(restored_questions[11]["stem"], [view_box])
        if None in (new_passage, new_q10, new_q11):
            return None
        restored_questions[10]["stem"] = new_q10
        restored_questions[11]["stem"] = new_q11
        return new_passage, restored_questions

    # 2011 Q27-29: the passage marker is the HWP [A] label. Q29's marker
    # precedes a 3x2 view-box whose only nonempty body cell is continuous
    # prose; preserve that text in reading order without empty layout cells.
    if year_folder == "2011" and (start, end) == (27, 29):
        view_box = (
            "<보 기> 하늘이 백성을 내시고 이를 나누어 사민(四民)을 삼으셨으니, "
            "사․농․공․상이 각각 자기의 분수가 있습니다. 선비는 여러 가지 일을 다스리고, "
            "농부는 농사에 힘쓰며, 공인은 공예를 맡고, 상인은 물화를 유통시키는 것이니 뒤섞여서는 안 되는 것입니다. "
            "역관과 의관 등의 잡학인은 나라에 없을 수 없지만, 직임은 각기 분수에 마땅하게 해야 할 것입니다. "
            "어찌 반드시 군자와 소인을 같이 거처하게 하고, 귀천을 섞이게 한 연후에야 권장이 되겠습니까? "
            "벼슬과 상은 임금이 영웅을 다루는 방도입니다. 그러므로 옛날의 성왕(聖王)은 재덕(才德)이 탁월하거나, "
            "혹은 공로가 중대하고, 혹은 다스린 성과가 제일인 자를 발탁한 일은 있어도, "
            "환관과 역관, 의관을 중용했다는 것은 듣지 못하였습니다. 삼가 바라건대 즉시 내리신 명령을 거두시어 "
            "잡학인이 청류(淸流)에 섞이지 않게 하소서."
        )
        new_passage = replace_exact(passage, ["[A]"])
        new_q29 = replace_exact(restored_questions[29]["stem"], [view_box])
        if None in (new_passage, new_q29):
            return None
        restored_questions[29]["stem"] = new_q29
        return new_passage, restored_questions

    # 2012 Q27-29: high-coverage exact passage alignment places the marker
    # between continuous HWP prose paragraphs; no visual/table control is
    # present in the exact span and the adjacent sentences remain complete.
    # Require the verified neighboring prose as well as the exact marker
    # count, so a marker alone can never trigger deletion.
    if year_folder == "2012" and (start, end) == (27, 29):
        markers = list(visual_re.finditer(passage))
        if len(markers) != 1:
            return None
        marker = markers[0]
        before = "“이 동네에 들인 공이 아까워서예요. 생각해 보세요.”\n\n"
        after = "\n우리네 장닭의 당당한 울음소리를 들을 수 없게 된 지도 오래였다."
        if not passage[:marker.start()].endswith(before) or not passage[marker.end():].startswith(after):
            return None
        new_passage = replace_exact(passage, [""])
        if new_passage is None:
            return None
        return new_passage, restored_questions

    # 2014 Q23-25: both markers map to the same one-cell text object.
    if year_folder == "2014" and (start, end) == (23, 25):
        new_passage = replace_exact(passage, ["정치적 거래 비용 이론"])
        new_q25 = replace_exact(restored_questions[25]["stem"], ["정치적 거래 비용 이론"])
        if None in (new_passage, new_q25):
            return None
        restored_questions[25]["stem"] = new_q25
        return new_passage, restored_questions

    # 2014 Q26-29: both markers map to the same one-cell text object.
    if year_folder == "2014" and (start, end) == (26, 29):
        new_passage = replace_exact(passage, ["기만"])
        new_q29 = replace_exact(restored_questions[29]["stem"], ["기만"])
        if None in (new_passage, new_q29):
            return None
        restored_questions[29]["stem"] = new_q29
        return new_passage, restored_questions

    # 2015 Q17-20: three marker occurrences map to one poem line and the
    # same one-cell term object in the passage and Q19 stem.
    if year_folder == "2015" and (start, end) == (17, 20):
        new_passage = replace_exact(
            passage,
            [
                "살았대나 죽었대나 같은 말을 가지고 사람은 살아서 늙어서야 죽나니, "
                "그러하면 그 역시 그럴 듯도 한 일을, 하필코 내 몸이라 그 무엇이 어째서 오늘도 산마루에 올라서서 우느냐.",
                "형이상학적 전율",
            ],
        )
        new_q19 = replace_exact(restored_questions[19]["stem"], ["형이상학적 전율"])
        if None in (new_passage, new_q19):
            return None
        restored_questions[19]["stem"] = new_q19
        return new_passage, restored_questions

    # 2016 Q33-35: the passage marker maps to the HWP [가] label. The final
    # <표> follows a complete choice 5 at EOF; HWP's next substantive object
    # is the exam confirmation TableControl. Remove only this guarded tail.
    if year_folder == "2016" and (start, end) == (33, 35):
        new_passage = replace_exact(passage, ["[가]"])
        if new_passage is None:
            return None
        choice5 = restored_questions[35]["choices"][4]
        expected_suffix = (
            "권리를 입증하지 못하여 패소한 이가 이후에 자신이 당사자가 아닌 소송의 판결 때문에 "
            "거듭 불이익을 받을 수 있다는 결론이 도출되지만, 그것이 부당하지 않다고 보았다."
        )
        markers = list(visual_re.finditer(choice5))
        if markers:
            marker = markers[0]
            if (
                len(markers) != 1
                or marker.group() != "<표>"
                or choice5[marker.end():].strip()
                or choice5[:marker.start()].rstrip() != expected_suffix
            ):
                return None
            restored_questions[35]["choices"][4] = choice5[:marker.start()].rstrip()
        elif choice5 != expected_suffix:
            return None
        return new_passage, restored_questions

    # 2019 Q28-30: passage/Q28 figure markers map to the same textbox text;
    # the passage table marker maps to [A]. The final <표> is the EOF marker
    # for HWP's exam confirmation TableControl, not part of Q30 choice 5.
    if year_folder == "2019" and (start, end) == (28, 30):
        new_passage = replace_exact(passage, ["근대법의 기획", "[A]"])
        new_q28 = replace_exact(restored_questions[28]["stem"], ["근대법의 기획"])
        if None in (new_passage, new_q28):
            return None
        choice5 = restored_questions[30]["choices"][4]
        expected_suffix = (
            "행위가 법률로 금지되는 것인지 여부를 행위 당시에 알 수 있었는지에 대하여 "
            "법관은 입법자의 입장에서 판단해야 할 것이다."
        )
        markers = list(visual_re.finditer(choice5))
        if markers:
            marker = markers[0]
            if (
                len(markers) != 1
                or marker.group() != "<표>"
                or choice5[marker.end():].strip()
                or choice5[:marker.start()].rstrip() != expected_suffix
            ):
                return None
            restored_questions[30]["choices"][4] = choice5[:marker.start()].rstrip()
        elif choice5 != expected_suffix:
            return None
        restored_questions[28]["stem"] = new_q28
        return new_passage, restored_questions

    # 2020 Q16-18: both markers map to the same actual textbox text.
    if year_folder == "2020" and (start, end) == (16, 18):
        new_passage = replace_exact(passage, ["탈근대적 지식 문화"])
        new_q17 = replace_exact(restored_questions[17]["stem"], ["탈근대적 지식 문화"])
        if None in (new_passage, new_q17):
            return None
        restored_questions[17]["stem"] = new_q17
        return new_passage, restored_questions

    # 2021 Q28-30: the two passage markers map to the single-cell [A]
    # label table and the textbox phrase, respectively. Q29's stem marker
    # maps to the same textbox phrase. The Q29 choice-tail marker sits
    # before an empty, invisible HWP rectangle (no fill, stroke, picture,
    # or text); Q30's terminal marker is the generic confirmation table.
    # Guard each trailing-marker removal by its exact field and full prose.
    if year_folder == "2021" and (start, end) == (28, 30):
        new_passage = replace_exact(
            passage,
            ["[A]", "판단하기 어려운 사안"],
        )
        new_q29_stem = replace_exact(
            restored_questions[29]["stem"],
            ["판단하기 어려운 사안"],
        )
        if None in (new_passage, new_q29_stem):
            return None

        q29_choice5 = restored_questions[29]["choices"][4]
        q29_expected = (
            "형식상 드러나 있는 법률의 흠결을 보충하기 위해서도 해당 법률의 "
            "본래적 구상보다는 전체 법질서를 고려한 해석이 필요하다."
        )
        q29_markers = list(visual_re.finditer(q29_choice5))
        if q29_markers:
            marker = q29_markers[0]
            if (
                len(q29_markers) != 1
                or marker.group() != "<그림>"
                or q29_choice5[marker.end():].strip()
                or q29_choice5[:marker.start()].rstrip() != q29_expected
            ):
                return None
            restored_questions[29]["choices"][4] = q29_choice5[:marker.start()].rstrip()
        elif q29_choice5 != q29_expected:
            return None

        q30_choice5 = restored_questions[30]["choices"][4]
        q30_expected = (
            "여러 종류의 야생동물의 유전자를 조합하여 실험실에서 창조한 동물을 기르는 것이 "
            "금지되었다면, ‘야생동물’의 언어적 의미를 자연에서 태어나 살아가는 동물로 보았을 것이다."
        )
        q30_markers = list(visual_re.finditer(q30_choice5))
        if q30_markers:
            marker = q30_markers[0]
            if (
                len(q30_markers) != 1
                or marker.group() != "<표>"
                or q30_choice5[marker.end():].strip()
                or q30_choice5[:marker.start()].rstrip() != q30_expected
            ):
                return None
            restored_questions[30]["choices"][4] = q30_choice5[:marker.start()].rstrip()
        elif q30_choice5 != q30_expected:
            return None

        restored_questions[29]["stem"] = new_q29_stem
        return new_passage, restored_questions

    return passage, restored_questions


def source_for_group(key, items, meet_index, kice_index, kice_passage_index):
    family, year, exam_label, passage_id, canonical_path = key
    numbers = sorted(int(r["target_source_coordinate"]["question_number"]) for r in items)
    match = re.search(r"-Q0*(\d+)-0*(\d+)(?:-S[^-]+)?$", str(passage_id or ""))
    if not match:
        return {"error": "parser/source_structure_unresolved", "source_path": canonical_path}
    start, end = map(int, match.groups())

    if family == "LEET":
        year_folder = f"{year}예비" if "예비" in str(passage_id) else str(year)
        transcript = ROOT / f"자료/LEET_언어이해/전사_검수완료/{year_folder}/q{start:02d}-{end:02d}.md"
        if transcript.is_file():
            source_path = transcript.relative_to(ROOT).as_posix()
        else:
            source_path = str(canonical_path)
        path = ROOT / source_path
        if not path.is_file():
            return {"error": "source_missing_candidate", "source_path": source_path}
        raw_bytes = path.read_bytes()
        raw = raw_bytes.decode("utf-8-sig")
        parsed = parse_markdown_group(raw, start, end)
        if parsed is None:
            return {"error": "parser/source_structure_unresolved", "source_path": source_path, "source_hash": sha(raw_bytes)}
        passage, questions = parsed
        if not set(numbers).issubset(questions):
            return {"error": "parser/source_structure_unresolved", "source_path": source_path, "source_hash": sha(raw_bytes)}

        restored = restore_verified_leet_visual_text(
            year_folder, start, end, passage, questions
        )
        if restored is None:
            return {
                "error": "parser/source_structure_unresolved",
                "source_path": source_path,
                "source_hash": sha(raw_bytes),
            }
        passage, questions = restored

        return {"source_path": source_path, "source_hash": sha(raw_bytes), "source_bytes": raw_bytes,
                "source_type": "verified_leet_transcript_markdown" if source_path.startswith("자료/LEET_언어이해/전사_검수완료/") else "canonical_leet_odd_markdown",
                "passage": passage, "questions": questions}

    if family == "MEET":
        transcript = ROOT / f"자료/MEET_언어추론/전사_검수완료/{year}/q{start:02d}-{end:02d}.md"
        source_path = transcript.relative_to(ROOT).as_posix() if transcript.is_file() else str(canonical_path)
        path = ROOT / source_path
        raw_bytes = path.read_bytes() if path.is_file() else b""
        raw = raw_bytes.decode("utf-8-sig") if raw_bytes else ""
        parsed = parse_markdown_group(raw, start, end) if raw else None
        if parsed is not None:
            passage, questions = parsed
            if set(numbers).issubset(questions):
                return {"source_path": source_path, "source_hash": sha(raw_bytes), "source_bytes": raw_bytes,
                        "source_type": "verified_meet_transcription_markdown", "passage": passage, "questions": questions}
        wanted = {r.get("target_question_id") for r in items if r.get("target_question_id")}
        canonical = meet_index
        questions = {}
        passage = None
        for r in items:
            qid = r.get("target_question_id")
            row = canonical.get(qid)
            extracted = parse_json_question(row, passage_id) if row else None
            if extracted is None:
                return {"error": "parser/source_structure_unresolved", "source_path": source_path,
                        "source_hash": sha(raw_bytes) if raw_bytes else None}
            p, stem, choices = extracted
            passage = passage or p
            if p != passage:
                return {"error": "parser/source_structure_unresolved", "source_path": source_path}
            questions[int(r["target_source_coordinate"]["question_number"])] = {"stem": stem, "choices": choices}
        if passage and set(numbers).issubset(questions):
            return {"source_path": "data/meet_questions.jsonl", "source_hash": sha((ROOT / "data/meet_questions.jsonl").read_bytes()),
                    "source_bytes": None, "source_type": "canonical_meet_jsonl_without_answer_fields",
                    "passage": passage, "questions": questions, "transcription_path": source_path,
                    "transcription_hash": sha(raw_bytes) if raw_bytes else None}
        return {"error": "parser/source_structure_unresolved", "source_path": source_path}

    if family == "KICE":
        # Prefer the passage-scoped canonical Markdown when it is present.
        # Its filename is tied to the exact passage ID, including its page
        # span, so unrelated questions cannot enter the extracted block.
        md_matches = []
        suffix = re.search(r"-Q\d+-\d+-(S[^-]+)$", str(passage_id or ""))
        if suffix:
            md_name = f"Q{start:02d}-{end:02d}-{suffix.group(1).replace('~', '-')}.md"
            md_root = ROOT / "data/기출_MD_정본/연도별" / str(year)
            if md_root.is_dir():
                md_matches = [p for p in md_root.rglob(md_name) if p.is_file()]
        if len(md_matches) == 1:
            md_path = md_matches[0]
            md_bytes = md_path.read_bytes()
            md_raw = md_bytes.decode("utf-8-sig")
            parsed_md = parse_markdown_group(md_raw, start, end, allow_range_alias=True)
            if parsed_md is not None and all(n in parsed_md[1] for n in numbers):
                passage_md, questions_md = parsed_md
                rel = md_path.relative_to(ROOT).as_posix()
                return {"source_path": rel, "source_hash": sha(md_bytes), "source_bytes": md_bytes,
                        "source_type": "canonical_kice_passage_markdown", "passage": passage_md,
                        "questions": questions_md}

        path = ROOT / str(canonical_path)
        if not path.is_file():
            return {"error": "source_missing_candidate", "source_path": str(canonical_path)}
        wanted = {r.get("target_question_id") for r in items if r.get("target_question_id")}
        index = kice_index
        qid = next(iter(wanted), None)
        row = index.get(qid) if qid else None
        extracted = parse_json_question(row, passage_id, require_passage=False) if row else None
        raw_bytes = path.read_bytes()
        passage_row = kice_passage_index.get(passage_id)
        passage = None
        if passage_row:
            passage = (passage_row.get("passage_text") or passage_row.get("passage") or
                       passage_row.get("passage_markdown") or passage_row.get("passage_content") or
                       passage_row.get("content") or passage_row.get("markdown") or passage_row.get("text"))
        if extracted is None or not isinstance(passage, str) or not passage.strip():
            return {"error": "parser/source_structure_unresolved", "source_path": str(canonical_path), "source_hash": sha(raw_bytes)}
        _unused_passage, stem, choices = extracted
        qn = int(items[0]["target_source_coordinate"]["question_number"])
        return {"source_path": str(canonical_path), "source_hash": sha(raw_bytes), "source_bytes": None,
                "source_type": "canonical_kice_jsonl_without_answer_fields", "passage": passage.strip(),
                "questions": {qn: {"stem": stem, "choices": choices}},
                "passage_source_path": "data/kice_passages.jsonl",
                "passage_source_hash": sha((ROOT / "data/kice_passages.jsonl").read_bytes())}

    return {"error": "parser/source_structure_unresolved", "source_path": canonical_path}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--commit", action="store_true", help="write validated READY sources and unresolved reasons")
    args = parser.parse_args()

    targets = read_jsonl(TARGET)
    manifest = read_jsonl(MANIFEST)
    mappings = read_jsonl(MAPPING)
    restorations = read_jsonl(RESTORATIONS)
    needs = [r for r in targets if r.get("status") == "NOT_COMPLETED_NEEDS_RESTORE"]
    by_group = defaultdict(list)
    for row in needs:
        c = row.get("target_source_coordinate", {})
        key = (c.get("exam_family"), c.get("year"), c.get("exam_label"), c.get("canonical_passage_id"), c.get("source_path"))
        by_group[key].append(row)

    prepared_candidates = set()
    for row in mappings:
        p = row.get("provenance", {})
        cid = p.get("candidate_id") or row.get("candidate_id")
        if cid:
            prepared_candidates.add(cid)

    meet_ids = {r.get("target_question_id") for r in needs if r.get("target_source_coordinate", {}).get("exam_family") == "MEET"}
    kice_ids = {r.get("target_question_id") for r in needs if r.get("target_source_coordinate", {}).get("exam_family") == "KICE"}
    kice_passage_ids = {r.get("target_source_coordinate", {}).get("canonical_passage_id") for r in needs
                        if r.get("target_source_coordinate", {}).get("exam_family") == "KICE"}
    meet_index = load_filtered_jsonl(ROOT / "data/meet_questions.jsonl", meet_ids) if meet_ids else {}
    kice_index = load_filtered_jsonl(ROOT / "data/kice_questions.jsonl", kice_ids) if kice_ids else {}
    kice_passage_index = load_filtered_jsonl(ROOT / "data/kice_passages.jsonl", kice_passage_ids,
                                              ("passage_id", "group_id", "question_id")) if kice_passage_ids else {}

    planned = []
    for key, items in by_group.items():
        family, year, _label, passage_id, _path = key
        items = sorted(items, key=lambda x: int(x["target_source_coordinate"]["question_number"]))
        nums = [int(x["target_source_coordinate"]["question_number"]) for x in items]
        candidate_ids = [x["candidate_id"] for x in items]
        src = source_for_group(key, items, meet_index, kice_index, kice_passage_index)
        result = {"key": key, "items": items, "nums": nums, "source": src, "candidate_ids": candidate_ids,
                  "family": family, "year": year, "passage_id": passage_id}
        if any(cid in prepared_candidates for cid in candidate_ids):
            result["error"] = "duplicate_candidate_protection"
        elif src.get("error"):
            result["error"] = src["error"]
        else:
            passage = src["passage"]
            questions = src["questions"]
            if not isinstance(passage, str) or not passage.strip():
                result["error"] = "empty_passage"
            elif any(n not in questions or not str(questions[n].get("stem", "")).strip() for n in nums):
                result["error"] = "empty_stem"
            elif any(len(questions[n].get("choices", [])) != 5 or any(not str(x).strip() for x in questions[n].get("choices", [])) for n in nums):
                result["error"] = "invalid_choice_count"
            else:
                marker_counts = Counter()
                for text in [passage] + [questions[n]["stem"] for n in nums] + [x for n in nums for x in questions[n]["choices"]]:
                    for match in re.finditer(r"<(그림|표)>|\[(그림|표)\]|!\[|\[시각\s*자료", text, re.I):
                        token = match.group(1) or match.group(2) or "image_link"
                        marker_counts[token] += 1
                qice_visual_review = src.get("source_type") != "canonical_kice_passage_markdown" and any(
                    r.get("match_evidence", {}).get("canonical_connection_status") == "exact_canonical_kice_question_visual_choice_review_required"
                    for r in items
                )
                if marker_counts or qice_visual_review:
                    result["error"] = "visual_manual_review_required"
                    result["marker_counts"] = dict(marker_counts)
                else:
                    result["error"] = None
                    result["marker_counts"] = {}
        planned.append(result)

    # Dry-run and commit both visit every eligible group. A source parser
    # failure is isolated to its passage group.
    max_group = max((int(str(r.get("passage_group", "G000")).removeprefix("G")) for r in manifest), default=0)
    case_values = [alpha_value(r["case_id"]) for r in manifest if re.fullmatch(r"[A-Z]+", str(r.get("case_id", "")))]
    next_group = max_group + 1
    next_case = max(case_values, default=0) + 1
    used_case_ids = {r.get("case_id") for r in manifest}
    used_questions = {r.get("provenance", {}).get("question_id") for r in mappings}
    used_candidates = {r.get("provenance", {}).get("candidate_id") for r in mappings}
    outputs = []
    restored = []
    unresolved = []

    for result in planned:
        if result["error"]:
            unresolved.append(result)
            continue
        group_id = f"G{next_group:03d}"
        case_ids = [alpha(next_case + i) for i in range(len(result["items"]))]
        result["group_id"] = group_id
        result["case_ids"] = case_ids
        group_case_ids = case_ids
        case_rows = []
        for row, case_id in zip(result["items"], case_ids):
            c = row["target_source_coordinate"]
            qn = int(c["question_number"])
            q = result["source"]["questions"][qn]
            blind = {
                "blind_only": True,
                "passage_group": group_id,
                "case_id": case_id,
                "provenance": {"source_role": "anonymous_blind_source"},
                "passage_text": result["source"]["passage"],
                "stem": q["stem"],
                "choices": q["choices"],
            }
            case_rows.append({"row": row, "case_id": case_id, "blind": blind, "question_number": qn})
        result["case_rows"] = case_rows
        restored.append(result)
        next_group += 1
        next_case += len(case_ids)

    # Independent, source-text-free structural validation before any writes.
    all_new_candidate_ids = [r["candidate_id"] for g in restored for r in g["items"]]
    all_new_question_ids = [r.get("target_question_id") for g in restored for r in g["items"]]
    all_new_case_ids = [c["case_id"] for g in restored for c in g["case_rows"]]
    checks = {
        "duplicate_candidate": len(all_new_candidate_ids) - len(set(all_new_candidate_ids)),
        "duplicate_question": len(all_new_question_ids) - len(set(all_new_question_ids)),
        "duplicate_case": len(all_new_case_ids) - len(set(all_new_case_ids)),
        "existing_candidate_overlap": len(set(all_new_candidate_ids) & prepared_candidates),
        "existing_question_overlap": len(set(all_new_question_ids) & used_questions),
        "existing_case_overlap": len(set(all_new_case_ids) & used_case_ids),
        "completed_hold_ambiguous_overlap": sum(1 for r in targets if r.get("candidate_id") in set(all_new_candidate_ids)
            and r.get("status") in {"COMPLETED_TARGET", "HOLD", "AMBIGUOUS_COMPLETION"}),
    }
    output_conflicts = []
    for g in restored:
        for c in g["case_rows"]:
            rel = f"data/기본기_연구/prepared_backlog/blind_sources/{c['case_id']}.json"
            path = ROOT / rel
            if path.exists():
                output_conflicts.append(rel)
            if set(c["blind"]) != {"blind_only", "passage_group", "case_id", "provenance", "passage_text", "stem", "choices"}:
                checks["blind_schema_error"] = checks.get("blind_schema_error", 0) + 1
            if len(c["blind"]["choices"]) != 5 or VISUAL_RE.search(c["blind"]["passage_text"] + c["blind"]["stem"] + "\n".join(c["blind"]["choices"])):
                checks["blind_source_completeness_error"] = checks.get("blind_source_completeness_error", 0) + 1
            if not c["blind"]["passage_text"].strip() or not c["blind"]["stem"].strip():
                checks["empty_passage_stem"] = checks.get("empty_passage_stem", 0) + 1
        rels = [f"data/기본기_연구/prepared_backlog/packets/{c['case_id']}.md" for c in g["case_rows"]]
        rels += [f"data/기본기_연구/prepared_backlog/packets/{g['case_ids'][0]}.json"]
        output_conflicts.extend(rel for rel in rels if (ROOT / rel).exists())
    checks["output_path_conflict"] = len(output_conflicts)

    report = {
        "mode": "commit" if args.commit else "dry_run",
        "before": dict(Counter(r.get("status") for r in targets)),
        "needs_questions": len(needs),
        "needs_groups": len(planned),
        "restored_questions": sum(len(g["items"]) for g in restored),
        "restored_groups": len(restored),
        "restored_by_family": dict(Counter(g["family"] for g in restored)),
        "unresolved_groups": len(unresolved),
        "unresolved_by_reason": dict(Counter(g.get("error") for g in unresolved)),
        "groups": [{
            "family": g["family"], "year": g["year"],
            "question_numbers": g["nums"], "candidate_ids": g["candidate_ids"],
            "source_path": g["source"].get("source_path"),
            "source_hash": g["source"].get("source_hash"),
            "parser": "success" if not g.get("error") else g.get("error"),
            "passage_nonempty": bool(g["source"].get("passage", "").strip()),
            "stem_nonempty": all(bool(g["source"].get("questions", {}).get(n, {}).get("stem", "").strip()) for n in g["nums"]),
            "choice_counts": [len(g["source"].get("questions", {}).get(n, {}).get("choices", [])) for n in g["nums"]],
            "markers": g.get("marker_counts", {}),
            "linkage": "exact" if not g.get("error") else "unresolved",
            "result": "READY_LOCAL_SOURCE" if not g.get("error") else f"NEEDS_RESTORE:{g.get('error')}",
            "created_group": g.get("group_id"), "created_cases": g.get("case_ids", []),
        } for g in planned],
        "checks": checks,
    }
    print(json.dumps(report, ensure_ascii=False, separators=(",", ":")))

    if not args.commit:
        return 0 if all(v == 0 for v in checks.values()) else 1
    if any(v != 0 for v in checks.values()):
        return 2

    new_manifest, new_mappings, new_answers, new_restorations = [], [], [], []
    crosswalk_updates = {r["candidate_id"]: dict(r) for r in targets}
    for g in restored:
        source = g["source"]
        case_ids = g["case_ids"]
        for c in g["case_rows"]:
            row, qn, case_id = c["row"], c["question_number"], c["case_id"]
            coord = row["target_source_coordinate"]
            qid = row.get("target_question_id")
            passage_id = coord.get("canonical_passage_id")
            blind_rel = f"data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json"
            atomic_write(ROOT / blind_rel, (json.dumps(c["blind"], ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
            new_manifest.append({
                "case_id": case_id, "status": "prepared", "passage_group": g["group_id"],
                "group_case_ids": case_ids, "group_release_rules": RULES,
                "blind_source": blind_rel,
                "exclusion_checks": {"exposure_status": "unknown", "semantic_review": "not_reviewed",
                    "source_quality": {"visual_placeholder": False, "canonical_link": "exact",
                        "choice_parse": "five_exact_choices", "text_markers_preserved": True,
                        "source_verification": source["source_type"]}},
            })
            new_mappings.append({
                "case_id": case_id, "passage_group": g["group_id"], "group_case_ids": case_ids,
                "provenance": {"candidate_id": row["candidate_id"], "exam_family": g["family"],
                    "academic_year": g["year"], "exam_label": coord.get("exam_label"),
                    "question_number": qn, "question_id": qid, "passage_id": passage_id,
                    "source_path": source["source_path"], "canonical_source_path": source["source_path"],
                    "source_sha256": source["source_hash"], "source_type": source["source_type"],
                    "official_pages": [], "linked_visual_assets": [], "source_role": "sealed_provenance_mapping"},
                "source_status": source["source_type"],
            })
            new_answers.append({"case_id": case_id, "candidate_id": row["candidate_id"],
                "official_answer": None, "official_answer_source": "not accessed during source preparation; resolve after group blind barrier",
                "site_original_codes": None, "site_marked_answer": None, "source_role": "sealed_for_after_blind",
                "passage_group": passage_id, "release_rule": RULES[0]})
            target = crosswalk_updates[row["candidate_id"]]
            target["status"] = "NOT_COMPLETED_READY_LOCAL_SOURCE"
            target["match_method"] = "deterministic_source_restoration"
            target["match_evidence"] = {**(target.get("match_evidence") or {}),
                "restoration_result": "READY_LOCAL_SOURCE", "restoration_group": g["group_id"],
                "restoration_case": case_id, "source_path": source["source_path"],
                "source_sha256": source["source_hash"], "source_parser": "deterministic_source_restoration_v1",
                "blind_linkage": "exact candidate_id + target_question_id + canonical passage range"}

        packet = {"blind_packet": True, "passage_group": g["group_id"], "group_case_ids": case_ids,
                  "group_release_rules": RULES,
                  "source_files": [f"data/기본기_연구/prepared_backlog/blind_sources/{case}.json" for case in case_ids]}
        atomic_write(PREP / f"packets/{case_ids[0]}.json", (json.dumps(packet, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))
        for case_id in case_ids:
            md = (f"# Blind source packet — {g['group_id']}\n\n" +
                  "all_group_blind_records_before_any_group_answer_check\n" +
                  "all_group_independent_code_records_before_any_group_sdss_disclosure\n\n" +
                  f"- {case_id}: `data/기본기_연구/prepared_backlog/blind_sources/{case_id}.json`\n")
            atomic_write(PREP / f"packets/{case_id}.md", md.encode("utf-8"))
        new_restorations.append({"passage_group": g["group_id"], "source_passage_id": g["passage_id"],
            "family": g["family"], "year": g["year"], "question_range": [min(g["nums"]), max(g["nums"])],
            "target_question_numbers": g["nums"], "candidate_ids": g["candidate_ids"],
            "case_ids": case_ids, "selected_text_source": source["source_path"],
            "source_sha256": source["source_hash"], "source_priority": "verified transcript, canonical markdown/json",
            "parser": "deterministic_source_restoration_v1", "restoration_type": "source_preparation_only",
            "restoration_status": "READY_LOCAL_SOURCE", "visual_marker_count": 0})

    for g in unresolved:
        source = g["source"]
        reason = g.get("error", "parser/source_structure_unresolved")
        next_action = ("official-page-verified minimal crop/asset linkage for the exact marker(s)" if reason == "visual_manual_review_required"
                       else "resolve the deterministic parser boundary against the verified local source without exposing source text to the model")
        new_restorations.append({"source_passage_id": g["passage_id"], "family": g["family"], "year": g["year"],
            "question_range": [min(g["nums"]), max(g["nums"])], "target_question_numbers": g["nums"],
            "candidate_ids": g["candidate_ids"], "case_ids": [], "selected_text_source": source.get("source_path"),
            "source_sha256": source.get("source_hash"), "parser": "deterministic_source_restoration_v1",
            "restoration_type": "source_preparation_only", "restoration_status": "NEEDS_RESTORE",
            "unresolved_reason": reason, "marker_counts": g.get("marker_counts", {}),
            "tool_policy_block": False, "exact_next_action": next_action})
        for row in g["items"]:
            target = crosswalk_updates[row["candidate_id"]]
            target["match_evidence"] = {**(target.get("match_evidence") or {}),
                "restoration_result": "NEEDS_RESTORE", "unresolved_reason": reason,
                "source_path_checked": source.get("source_path"), "source_sha256": source.get("source_hash"),
                "source_parser": "deterministic_source_restoration_v1", "exact_next_action": next_action}

    # Persist only after all blind payloads and metadata have passed preflight.
    append_jsonl(MANIFEST, new_manifest)
    append_jsonl(MAPPING, new_mappings)
    append_jsonl(ANSWERS, new_answers)
    append_jsonl(RESTORATIONS, new_restorations)
    merged = [crosswalk_updates.get(r["candidate_id"], r) for r in targets]
    atomic_write(TARGET, ("".join(json.dumps(r, ensure_ascii=False, separators=(",", ":")) + "\n" for r in merged)).encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
