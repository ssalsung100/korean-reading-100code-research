#!/usr/bin/env python3
"""Extract searchable text and embedded figures from the LEET archive.

Original HWP/PDF files are never modified.  The output is a convenience
layer for later passage/code analysis; each output record keeps source paths,
page numbers and hashes where applicable.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import shutil
import subprocess
import tempfile
from pathlib import Path

import fitz
from bs4 import BeautifulSoup

ROOT = Path("자료/LEET_언어이해")
MANIFEST = ROOT / "manifest.json"
TEXT_ROOT = ROOT / "텍스트"
IMAGE_ROOT = ROOT / "이미지"
PAGE_ROOT = ROOT / "페이지"
TABLE_ROOT = ROOT / "표"
OUT = ROOT / "extracted_assets_manifest.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def clean_text(s: str) -> str:
    s = html.unescape(s).replace("\r\n", "\n").replace("\r", "\n")
    s = s.replace("\u00a0", " ")
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{4,}", "\n\n\n", s)
    return s.strip()


def hwp_extract(path: Path, image_dir: Path, table_dir: Path, answer: bool) -> tuple[str, list[dict], list[dict], str]:
    """Extract direct HWP text plus BinData figures and every HTML table.

    Question text comes from hwp5txt because it follows the document stream
    and does not duplicate layout tables. Answer files are tables, so their
    table text is used instead. No OCR or inferred wording is introduced.
    """
    image_dir.mkdir(parents=True, exist_ok=True)
    table_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="leet-hwp-") as tmp:
        outdir = Path(tmp) / "html"
        subprocess.run(
            ["hwp5html", "--output", str(outdir), str(path)],
            check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,
        )
        index = outdir / "index.xhtml"
        soup = BeautifulSoup(index.read_text(encoding="utf-8"), "html.parser")
        # Insert explicit markers before converting HTML to plain text. This
        # retains the location of diagrams that hwp5txt would call <그림>.
        figures: list[dict] = []
        for n, img in enumerate(soup.find_all("img"), 1):
            src = img.get("src", "")
            src_path = outdir / src
            if not src_path.exists():
                continue
            data = src_path.read_bytes()
            ext = src_path.suffix.lower() or ".bin"
            name = f"image_{n:03d}{ext}"
            target = image_dir / name
            target.write_bytes(data)
            marker = soup.new_string(f" [[IMAGE:{name}]] ")
            img.replace_with(marker)
            figures.append({"file": str(target), "name": name,
                            "sha256": sha256_bytes(data), "source": src})
        tables: list[dict] = []
        table_texts: list[str] = []
        for n, table in enumerate(soup.find_all("table"), 1):
            rows = []
            for tr in table.find_all("tr"):
                cells = [" ".join(td.stripped_strings) for td in tr.find_all(["td", "th"])]
                if cells:
                    rows.append(" | ".join(cells))
            if rows:
                table_text = "\n".join(rows)
                target = table_dir / f"table_{n:03d}.md"
                target.write_text(f"# table {n}\n\n{table_text}\n", encoding="utf-8")
                tables.append({"file": str(target), "name": target.name,
                               "row_count": len(rows)})
                table_texts.append(table_text)
        if answer:
            text = clean_text("\n\n".join(table_texts))
            method = "hwp5html_table"
        else:
            result = subprocess.run(
                ["hwp5txt", str(path)], check=True, text=True,
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            text = clean_text(result.stdout)
            method = "hwp5txt_direct"
        return text, figures, tables, method


def pdf_extract(path: Path, image_dir: Path, page_dir: Path) -> tuple[str, list[dict], list[dict], str]:
    image_dir.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(path)
    chunks: list[str] = []
    figures: list[dict] = []
    page_renders: list[dict] = []
    seen: set[str] = set()
    image_only = all(not page.get_text().strip() for page in doc)
    if image_only:
        page_dir.mkdir(parents=True, exist_ok=True)
    for page_no, page in enumerate(doc, 1):
        chunks.append(f"<!-- page {page_no} -->\n\n{page.get_text('text').strip()}")
        # Some official PDFs are scans or have every text line encoded as an
        # image. In that case the tiny extracted line-images are not useful
        # for reading, so preserve a full-page rendering as well.
        if image_only:
            target = page_dir / f"page_{page_no:03d}.png"
            pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
            pix.save(str(target))
            data = target.read_bytes()
            page_renders.append({"file": str(target), "page": page_no,
                                 "bytes": len(data), "sha256": sha256_bytes(data)})
        for img_no, info in enumerate(page.get_images(full=True), 1):
            xref = info[0]
            try:
                extracted = doc.extract_image(xref)
            except Exception:
                continue
            data = extracted.get("image", b"")
            if not data:
                continue
            digest = sha256_bytes(data)
            if digest in seen:
                continue
            seen.add(digest)
            ext = "." + extracted.get("ext", "bin")
            name = f"page_{page_no:03d}_image_{img_no:02d}{ext}"
            target = image_dir / name
            target.write_bytes(data)
            figures.append({"file": str(target), "name": name,
                            "sha256": digest, "page": page_no, "xref": xref})
    return clean_text("\n\n".join(chunks)), figures, page_renders, "pymupdf" 


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    records: list[dict] = []
    for entry in manifest["entries"]:
        src = Path(entry["file"])
        base = f"{entry['label']}_{entry['kind']}"
        text_target = TEXT_ROOT / entry["label"] / f"{base}.md"
        image_dir = IMAGE_ROOT / entry["label"] / base
        page_dir = PAGE_ROOT / entry["label"] / base
        table_dir = TABLE_ROOT / entry["label"] / base
        try:
            if src.suffix.lower() == ".hwp":
                text, figures, tables, method = hwp_extract(
                    src, image_dir, table_dir, entry["kind"] == "answer"
                )
                page_renders = []
            elif src.suffix.lower() == ".pdf":
                text, figures, page_renders, method = pdf_extract(src, image_dir, page_dir)
                tables = []
            else:
                text, figures, tables, page_renders, method = "", [], [], [], "unsupported"
            text_target.parent.mkdir(parents=True, exist_ok=True)
            title = f"# {entry['label']} LEET 언어이해 {entry['kind']}\n\n"
            notice = ""
            if page_renders and not re.search(r"[가-힣A-Za-z0-9]", re.sub(r"<!--.*?-->", "", text, flags=re.S)):
                notice = "[공식 PDF에 텍스트 레이어가 없음. 아래 페이지 표지만 있으며, 검증 전 OCR 문장은 삽입하지 않음.]\n\n"
            text_target.write_text(title + notice + text + "\n", encoding="utf-8")
            status = "extracted"
        except Exception as exc:
            text_target.parent.mkdir(parents=True, exist_ok=True)
            text_target.write_text(f"# {base}\n\n[추출 실패: {type(exc).__name__}: {exc}]\n", encoding="utf-8")
            figures, tables, page_renders, method, status = [], [], [], type(exc).__name__, "failed"
        records.append({
            "year": entry["year"], "label": entry["label"], "kind": entry["kind"],
            "source_file": entry["file"], "source_sha256": entry["sha256"],
            "text_file": str(text_target), "image_dir": str(image_dir),
            "figure_count": len(figures), "figures": figures,
            "table_dir": str(table_dir), "table_count": len(tables), "tables": tables,
            "page_dir": str(page_dir), "page_render_count": len(page_renders),
            "page_renders": page_renders,
            "method": method, "status": status,
        })
        print(entry["label"], entry["kind"], status, "figures", len(figures))
    payload = {
        "source_manifest": "manifest.json", "entry_count": len(records),
        "records": records,
        "note": "Text/images are derived convenience files; original HWP/PDF files remain authoritative.",
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print("wrote", OUT)


if __name__ == "__main__":
    main()
