#!/usr/bin/env python3
"""Create a deterministic SHA-256 manifest for the project asset backup."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path.cwd()
OUT_DIR = ROOT / "백업_원장"
OUT_JSON = OUT_DIR / "핵심자산_SHA256_20260906_v1.json"
OUT_MD = OUT_DIR / "핵심자산_백업범위_20260906_v1.md"
EXCLUDED_TOP = {"output", "백업_원장"}
EXCLUDED_NAMES = {"__pycache__"}
EXCLUDED_SUFFIXES = {".pyc"}


def included(path: Path) -> bool:
    relative = path.relative_to(ROOT)
    if relative.parts and relative.parts[0] in EXCLUDED_TOP:
        return False
    if any(part in EXCLUDED_NAMES for part in relative.parts):
        return False
    return path.suffix.lower() not in EXCLUDED_SUFFIXES


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(4 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def main() -> None:
    files = sorted(
        (path for path in ROOT.rglob("*") if path.is_file() and included(path)),
        key=lambda path: path.relative_to(ROOT).as_posix(),
    )
    records = []
    total_bytes = 0
    for index, path in enumerate(files, 1):
        size = path.stat().st_size
        total_bytes += size
        records.append(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "bytes": size,
                "sha256": sha256(path),
            }
        )
        if index % 500 == 0:
            print(f"HASHED {index}/{len(files)}", flush=True)

    payload = {
        "status": "source_manifest_complete",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "root_name": ROOT.name,
        "selection": {
            "included": "all project files except explicitly excluded generated output/cache paths",
            "excluded_top_level": sorted(EXCLUDED_TOP),
            "excluded_directory_names": sorted(EXCLUDED_NAMES),
            "excluded_suffixes": sorted(EXCLUDED_SUFFIXES),
        },
        "file_count": len(records),
        "total_bytes": total_bytes,
        "records": records,
    }
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    OUT_MD.write_text(
        "\n".join(
            [
                "# 핵심 자산 백업 범위 — 2026-09-06 v1",
                "",
                f"- 파일 수: {len(records):,}개",
                f"- 원본 총량: {total_bytes:,}바이트",
                "- 포함: 원본 HWP/HWPX/PDF, 정본 Markdown·JSONL, 이미지·표, 검증 원장, 제작물과 스크립트",
                "- 제외: `output/`, `백업_원장/`, `__pycache__/`, `*.pyc`",
                "- 각 파일의 경로·크기·SHA-256은 동명의 JSON 원장에 기록했다.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    print(f"COMPLETE files={len(records)} bytes={total_bytes} manifest={OUT_JSON}")


if __name__ == "__main__":
    main()
