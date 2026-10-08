#!/usr/bin/env python3
"""Export LEET HWP control anchors in isolated Hancom processes."""
from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path


ROOT = Path.cwd()
CORPUS = ROOT / "자료/LEET_언어이해/extracted_assets_manifest.json"
OUT = ROOT / "자료/LEET_언어이해/검증/HWP_홀수형_컨트롤_좌표"
INSPECTOR = ROOT / "scripts/inspect_hwp_control_positions.ps1"
WIN_TEMP = Path("/mnt/c/Windows/Temp/leet_control_positions")


def winpath(path: Path) -> str:
    result = subprocess.run(
        ["wslpath", "-w", str(path)],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def main() -> None:
    corpus = json.loads(CORPUS.read_text(encoding="utf-8"))
    entries = [
        item
        for item in corpus["records"]
        if item["kind"] == "question_odd"
        and item["method"] == "hwp5txt_direct"
        and int(item["year"]) <= 2021
        and Path(item["source_file"]).suffix.lower() == ".hwp"
    ]
    entries.sort(key=lambda item: (int(item["year"]), item["label"]))
    OUT.mkdir(parents=True, exist_ok=True)
    WIN_TEMP.mkdir(parents=True, exist_ok=True)

    records: list[dict] = []
    errors: list[str] = []
    for index, entry in enumerate(entries, 1):
        label = str(entry["label"])
        source = ROOT / entry["source_file"]
        safe = f"{int(entry['year'])}_{index:02d}"
        temp_linux = WIN_TEMP / f"{safe}.json"
        temp_windows = rf"C:\Windows\Temp\leet_control_positions\{safe}.json"
        target = OUT / f"{label}.json"
        if target.is_file():
            try:
                payload = json.loads(target.read_text(encoding="utf-8-sig"))
                records.append(
                    {
                        "label": label,
                        "year": int(entry["year"]),
                        "source_file": entry["source_file"],
                        "source_sha256": entry["source_sha256"],
                        "control_file": str(target.relative_to(ROOT)),
                        "page_count": int(payload["page_count"]),
                        "record_count": int(payload["record_count"]),
                    }
                )
                print(f"REUSED {label} pages={payload['page_count']} controls={payload['record_count']}", flush=True)
                continue
            except (ValueError, KeyError, json.JSONDecodeError):
                target.unlink(missing_ok=True)
        temp_linux.unlink(missing_ok=True)
        command = [
            "powershell.exe",
            "-NoProfile",
            "-STA",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            winpath(INSPECTOR),
            "-Source",
            winpath(source),
            "-Output",
            temp_windows,
        ]
        result = subprocess.run(
            command,
            text=True,
            encoding="cp949",
            errors="replace",
            capture_output=True,
            timeout=180,
        )
        if result.returncode != 0 or not temp_linux.is_file():
            errors.append(
                f"{label}: exit={result.returncode} stdout={result.stdout[-300:]!r} "
                f"stderr={result.stderr[-500:]!r}"
            )
            print(f"FAILED {label}", flush=True)
            continue
        payload = json.loads(temp_linux.read_text(encoding="utf-8-sig"))
        shutil.copyfile(temp_linux, target)
        records.append(
            {
                "label": label,
                "year": int(entry["year"]),
                "source_file": entry["source_file"],
                "source_sha256": entry["source_sha256"],
                "control_file": str(target.relative_to(ROOT)),
                "page_count": payload["page_count"],
                "control_count": payload["record_count"],
                "status": "hwp_anchor_exported",
            }
        )
        print(
            f"EXPORTED {label} pages={payload['page_count']} controls={payload['record_count']}",
            flush=True,
        )

    manifest = {
        "status": "complete" if len(records) == len(entries) and not errors else "partial",
        "expected_records": len(entries),
        "record_count": len(records),
        "method": "Hancom control GetAnchorPos(0), SetPosBySet, and KeyIndicator",
        "records": records,
        "errors": errors,
    }
    (OUT / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"WROTE {len(records)}/{len(entries)} error_count={len(errors)}")
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
