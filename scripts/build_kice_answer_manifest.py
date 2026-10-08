#!/usr/bin/env python3
"""Build a provenance manifest for Korean-language KICE answer files."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("자료/평가원_정답표")
ROOT.mkdir(parents=True, exist_ok=True)


def safe_name(s: str) -> str:
    s = re.sub(r"[\\/:*?\"<>|]", "_", s)
    return re.sub(r"\s+", "_", s).strip("._")


def load(path: str, board_id: str, exam_type: str) -> list[dict]:
    rows = json.loads(Path(path).read_text(encoding="utf-8"))
    result: list[dict] = []
    for row in rows:
        if row.get("area") not in {"국어", "언어"} or int(row.get("year", 0)) < 2010:
            continue
        answer_files = [f for f in row.get("files", []) if "정답" in f.get("name", "")]
        # Older mock records bundle problem and answer files in one ZIP.
        if not answer_files:
            answer_files = [f for f in row.get("files", []) if f.get("name", "").lower().endswith(".zip")]
        for f in answer_files:
            name = f["name"]
            ext = Path(name).suffix.lower() or ".bin"
            label = f"{row['year']}_{row.get('month', '').strip('_')}_국어_{name}"
            result.append({
                "source": "한국교육과정평가원 수능 홈페이지",
                "official_page": (
                    "https://www.suneung.re.kr/boardCnts/view.do?"
                    f"boardID={board_id}&boardSeq={row['board_seq']}&lev=0&m=0403&s=suneung"
                ),
                "download_url": (
                    "https://www.suneung.re.kr/boardCnts/fileDown.do?"
                    f"fileSeq={f['seq']}"
                ),
                "board_id": board_id,
                "board_seq": row["board_seq"],
                "exam_type": exam_type,
                "academic_year": row["year"],
                "month": row.get("month"),
                "area": row["area"],
                "registered": row.get("date"),
                "file_seq": f["seq"],
                "file_name": name,
                "container": "zip" if ext == ".zip" else "pdf",
                "local_name": safe_name(label),
                "status": "downloaded" if (
                    ROOT / ("원본/수능" if exam_type == "수능" else "원본/모의평가") / safe_name(label)
                ).exists() else "pending_download",
            })
    return result


csat_index = "자료/평가원_정답표/board_index_csats.json"
mock_index = "자료/평가원_정답표/board_index_mock.json"
entries = load(csat_index if Path(csat_index).exists() else "/tmp/kice_rows.json", "1500234", "수능")
entries += load(mock_index if Path(mock_index).exists() else "/tmp/kice_mock_rows.json", "1500236", "수능 모의평가")
unique = {}
for entry in entries:
    unique.setdefault((entry["board_id"], entry["file_seq"]), entry)
entries = sorted(unique.values(), key=lambda e: (e["academic_year"], e.get("month") or "", e["exam_type"], e["file_name"]))

payload = {
    "generated_from": [
        "https://www.suneung.re.kr/boardCnts/list.do?boardID=1500234&m=0403&s=suneung",
        "https://www.suneung.re.kr/boardCnts/list.do?boardID=1500236&m=0403&s=suneung",
    ],
    "scope": "2010학년도 이후 국어/언어 수능 및 수능 모의평가",
    "count": len(entries),
    "entries": entries,
}
(ROOT / "manifest.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
cols = ["exam_type", "academic_year", "month", "board_seq", "file_seq", "file_name", "container", "download_url", "official_page", "local_name", "status"]
(ROOT / "manifest.tsv").write_text(
    "\t".join(cols) + "\n" + "\n".join("\t".join(str(e.get(c, "")) for c in cols) for e in entries) + "\n",
    encoding="utf-8",
)
print(f"wrote {ROOT / 'manifest.json'} ({len(entries)} files)")
print(f"pdf={sum(e['container'] == 'pdf' for e in entries)}, zip={sum(e['container'] == 'zip' for e in entries)}")
