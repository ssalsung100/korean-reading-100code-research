#!/usr/bin/env python3
"""Download all language-understanding LEET papers and answer keys.

The legacy Uway LEET board is the official public archive used here.  Every
download keeps its board-view URL, attachment URL, original title and hash.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import ssl
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

BASE = "https://leet.uwayapply.com"
ROOT = Path("자료/LEET_언어이해")
RAW = ROOT / "원본"
PAGES = ROOT / "게시판"


class AnchorParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.href: str | None = None
        self.buf: list[str] = []
        self.links: list[tuple[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() == "a":
            self.href = dict(attrs).get("href")
            self.buf = []

    def handle_data(self, data: str) -> None:
        if self.href is not None:
            self.buf.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "a" and self.href is not None:
            self.links.append((self.href, re.sub(r"\s+", " ", html.unescape("".join(self.buf))).strip()))
            self.href = None
            self.buf = []


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "*/*"})
    with urllib.request.urlopen(req, context=ssl._create_unverified_context(), timeout=60) as res:
        return res.read()


def safe(s: str) -> str:
    s = re.sub(r"[\\/:*?\"<>|]+", "_", s)
    return re.sub(r"\s+", "_", s).strip("._") or "download"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def abs_url(href: str) -> str:
    if href.startswith("BoardView.htm"):
        return BASE + "/board/" + href
    return urllib.parse.urljoin(BASE + "/", href)


def main() -> None:
    RAW.mkdir(parents=True, exist_ok=True)
    PAGES.mkdir(parents=True, exist_ok=True)
    posts: dict[str, dict] = {}
    for page in range(1, 8):
        list_url = f"{BASE}/board/BoardList.htm?board_id=84&page={page}&select=&key=&admin_id="
        data = fetch(list_url)
        page_path = PAGES / f"page_{page}.html"
        page_path.write_bytes(data)
        # The legacy list markup omits closing </a> tags in the table.  Use a
        # narrow row-level regex rather than relying solely on HTMLParser.
        page_text = data.decode("utf-8", errors="replace")
        row_pattern = re.compile(
            r'<a\s+href="(?P<href>BoardView\.htm\?[^"<>]+)"[^>]*>\s*'
            r'(?P<title>[^<]+?)\s*</td>', re.S
        )
        for match in row_pattern.finditer(page_text):
            href = match.group("href")
            title = re.sub(r"\s+", " ", html.unescape(match.group("title"))).strip()
            if "언어이해" not in title or "문제 및 정답" not in title:
                continue
            posts.setdefault(abs_url(href), {"title": title, "page": page})

    entries: list[dict] = []
    for view_url, post in sorted(posts.items(), key=lambda x: x[1]["title"]):
        data = fetch(view_url)
        view = AnchorParser()
        view.feed(data.decode("utf-8", errors="replace"))
        m = re.search(r"(20\d{2})학년도", post["title"])
        if not m:
            continue
        year = int(m.group(1))
        label = f"{year}예비" if "예비" in post["title"] else str(year)
        attachments = [(abs_url(h), t) for h, t in view.links if "script.curlGetFile.php" in h and t]
        # The page can contain a related-post link, so only keep actual file
        # links and deduplicate by attachment URL.
        seen: set[str] = set()
        for idx, (source_url, title) in enumerate(attachments, 1):
            if source_url in seen:
                continue
            seen.add(source_url)
            kind = "answer" if "정답" in title else (
                "question_even" if ("짝수" in title or "(짝)" in title) else (
                    "question_odd" if ("홀수" in title or "(홀)" in title) else "question"
                )
            )
            target_dir = RAW / label
            target_dir.mkdir(parents=True, exist_ok=True)
            target = target_dir / f"{label}_{kind}_{safe(title)}"
            if not target.exists() or target.stat().st_size == 0:
                target.write_bytes(fetch(source_url))
            entries.append({
                "year": year,
                "label": label,
                "kind": kind,
                "title": title,
                "board_page": view_url,
                "source_url": source_url,
                "file": str(target),
                "bytes": target.stat().st_size,
                "sha256": sha256(target),
            })
            print(label, kind, target)
    entries.sort(key=lambda e: (e["year"], e["label"], e["kind"], e["title"]))
    (ROOT / "manifest.json").write_text(json.dumps({
        "source": "법학적성시험 공식 홈페이지(Uway legacy board)",
        "board": "https://leet.uwayapply.com/board/BoardList.htm?board_id=84",
        "scope": "2009학년도 예비시험 및 2009~2027학년도 LEET 언어이해",
        "post_count": len(posts),
        "file_count": len(entries),
        "entries": entries,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"posts={len(posts)} files={len(entries)}")


if __name__ == "__main__":
    main()
