#!/usr/bin/env python3
"""Fetch recent micro-gesture related arXiv papers and update README."""

from __future__ import annotations

import datetime as dt
import os
import re
import time
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
SEEN_IDS_PATH = ROOT / "data" / "seen_arxiv_ids.txt"

ARXIV_API_URL = "https://export.arxiv.org/api/query"
QUERY_TERMS = [
    "micro gesture",
    "micro-gesture",
    "subtle gesture",
    "fine-grained gesture",
    "gesture understanding",
    "gesture recognition",
]

# Keep recall high; filter obvious noise from text-heavy domains.
NEGATIVE_TERMS = {
    "quantum",
    "protein",
    "molecule",
    "medical imaging",
    "galaxy",
    "stock market",
    "speech recognition",
}
POSITIVE_TERMS = {
    "gesture",
    "micro-gesture",
    "micro gesture",
    "hand",
    "body",
    "skeleton",
    "emg",
    "imu",
    "sign language",
    "pose",
    "video",
    "vision",
    "wearable",
    "emotion",
}

MAX_PER_RUN = 8
MAX_SEARCH_RESULTS = 80
RECENT_DAYS = 45
REQUEST_TIMEOUT_SECONDS = 25
MAX_FETCH_RETRIES = 3

NS = {
    "atom": "http://www.w3.org/2005/Atom",
}


def read_seen_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def write_seen_ids(path: Path, ids: Iterable[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = sorted(set(ids))
    path.write_text("\n".join(lines) + ("\n" if lines else ""), encoding="utf-8")


def normalize_arxiv_id(raw_id: str) -> str:
    match = re.search(r"arxiv\.org/(?:abs|pdf)/([^v?/]+)", raw_id)
    if match:
        return match.group(1)
    return raw_id.rsplit("/", 1)[-1]


def build_query() -> str:
    quoted = [f'all:"{term}"' for term in QUERY_TERMS]
    return " OR ".join(quoted)


def get_text(node: ET.Element | None, default: str = "") -> str:
    if node is None or node.text is None:
        return default
    return re.sub(r"\s+", " ", node.text).strip()


def fetch_recent_entries() -> list[dict]:
    params = {
        "search_query": build_query(),
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "start": 0,
        "max_results": MAX_SEARCH_RESULTS,
    }
    url = ARXIV_API_URL + "?" + urllib.parse.urlencode(params)

    request = urllib.request.Request(url, headers={"User-Agent": "Awesome-Micro-Gesture-ArXiv-Updater/1.0"})
    payload: bytes | None = None
    last_error: Exception | None = None
    for attempt in range(1, MAX_FETCH_RETRIES + 1):
        try:
            with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
                payload = response.read()
            break
        except Exception as exc:  # noqa: BLE001 - keep error handling broad for network robustness.
            last_error = exc
            if attempt < MAX_FETCH_RETRIES:
                time.sleep(attempt * 2)
            else:
                raise RuntimeError(f"arXiv request failed after {MAX_FETCH_RETRIES} attempts: {last_error}") from exc

    if payload is None:
        raise RuntimeError("arXiv response payload is empty.")

    root = ET.fromstring(payload)

    entries: list[dict] = []
    now = dt.datetime.now(dt.timezone.utc)
    oldest_allowed = now - dt.timedelta(days=RECENT_DAYS)

    for entry in root.findall("atom:entry", NS):
        published_text = get_text(entry.find("atom:published", NS))
        if not published_text:
            continue
        published = dt.datetime.fromisoformat(published_text.replace("Z", "+00:00"))
        if published < oldest_allowed:
            continue

        raw_id = get_text(entry.find("atom:id", NS))
        arxiv_id = normalize_arxiv_id(raw_id)
        title = get_text(entry.find("atom:title", NS))
        summary = get_text(entry.find("atom:summary", NS)).lower()
        authors = [get_text(author.find("atom:name", NS)) for author in entry.findall("atom:author", NS)]
        authors = [name for name in authors if name]

        entries.append(
            {
                "id": arxiv_id,
                "title": title,
                "url": f"https://arxiv.org/abs/{arxiv_id}",
                "authors": authors,
                "published": published.strftime("%Y-%m"),
                "text_blob": f"{title.lower()} {summary}",
            }
        )

    return entries


def is_relevant(text_blob: str) -> bool:
    if "gesture" not in text_blob:
        return False
    if not any(term in text_blob for term in POSITIVE_TERMS):
        return False
    if any(term in text_blob for term in NEGATIVE_TERMS):
        return False
    return True


def format_table_row(entry: dict) -> str:
    author_text = ", ".join(entry["authors"]) if entry["authors"] else "Unknown"
    date_text = entry["published"].replace("-", "/")
    paper_cell = f"[{entry['title']}]({entry['url']})<br>Authors: {author_text}<br>arXiv: {entry['id']}"
    return f"| {date_text} | - | {paper_cell} | ArXiv | - |"


def update_methods_table(readme_text: str, new_rows: list[str]) -> str:
    lines = readme_text.splitlines()
    methods_idx = None
    for i, line in enumerate(lines):
        if line.strip() == "## 🔨Methods":
            methods_idx = i
            break
    if methods_idx is None:
        raise RuntimeError("Could not find '## 🔨Methods' section in README.")

    table_start = None
    for i in range(methods_idx + 1, len(lines)):
        if lines[i].startswith("|"):
            table_start = i
            break
    if table_start is None or table_start + 1 >= len(lines):
        raise RuntimeError("Could not find Methods table header in README.")

    # header line + separator line
    data_start = table_start + 2
    data_end = data_start
    while data_end < len(lines):
        line = lines[data_end]
        if line.startswith("## "):
            break
        if line and not line.startswith("|"):
            break
        data_end += 1

    existing_rows = [row for row in lines[data_start:data_end] if row.strip()]
    merged_rows = new_rows + existing_rows
    updated = lines[:data_start] + merged_rows + lines[data_end:]
    return "\n".join(updated).rstrip() + "\n"


def main() -> int:
    if not README_PATH.exists():
        print(f"ERROR: README not found at {README_PATH}", file=sys.stderr)
        return 1

    seen_ids = read_seen_ids(SEEN_IDS_PATH)

    try:
        entries = fetch_recent_entries()
    except Exception as exc:
        strict_mode = os.getenv("ARXIV_STRICT_FETCH", "0") == "1"
        level = "ERROR" if strict_mode else "WARNING"
        print(f"{level}: failed to fetch arXiv feed: {exc}", file=sys.stderr)
        if strict_mode:
            return 1
        print("Continuing without README/data changes because strict fetch mode is disabled.")
        return 0

    deduped: dict[str, dict] = {}
    for item in entries:
        if item["id"] not in deduped:
            deduped[item["id"]] = item

    candidate_entries = [item for item in deduped.values() if is_relevant(item["text_blob"])]
    new_entries = [item for item in candidate_entries if item["id"] not in seen_ids][:MAX_PER_RUN]

    readme_text = README_PATH.read_text(encoding="utf-8")

    if not new_entries:
        print("No new relevant papers found; README and seen IDs are unchanged.")
        return 0

    rows = [format_table_row(entry) for entry in new_entries]
    updated_readme = update_methods_table(readme_text, rows)
    README_PATH.write_text(updated_readme, encoding="utf-8")

    updated_seen = set(seen_ids)
    updated_seen.update(entry["id"] for entry in new_entries)
    write_seen_ids(SEEN_IDS_PATH, updated_seen)

    print(
        f"Fetched {len(entries)} recent entries, {len(candidate_entries)} passed filters, "
        f"added {len(new_entries)} new paper(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
