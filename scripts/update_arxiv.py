#!/usr/bin/env python3
"""Fetch recent micro-gesture related arXiv papers and update README."""

from __future__ import annotations

import datetime as dt
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
README_PATH = ROOT / "README.md"
SEEN_IDS_PATH = ROOT / "data" / "seen_arxiv_ids.txt"

START_MARKER = "<!-- ARXIV_PAPERS_START -->"
END_MARKER = "<!-- ARXIV_PAPERS_END -->"

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
    with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
        payload = response.read()

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
                "published": published.date().isoformat(),
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


def format_bullet(entry: dict) -> str:
    author_text = ", ".join(entry["authors"]) if entry["authors"] else "Unknown"
    return (
        f"- [{entry['title']}]({entry['url']}) — Authors: {author_text}; "
        f"Published: {entry['published']}; arXiv: {entry['id']}"
    )


def ensure_marker_block(readme_text: str) -> str:
    if START_MARKER in readme_text and END_MARKER in readme_text:
        return readme_text

    lines = readme_text.splitlines()
    insert_at = 1 if lines and lines[0].startswith("#") else 0
    new_block = [
        "",
        "## Latest arXiv Papers",
        START_MARKER,
        "- _No recent arXiv updates yet. Run the updater workflow to populate this list._",
        END_MARKER,
        "",
    ]
    updated_lines = lines[:insert_at] + new_block + lines[insert_at:]
    return "\n".join(updated_lines).rstrip() + "\n"


def replace_marker_content(readme_text: str, new_lines: list[str]) -> str:
    pattern = re.compile(
        rf"{re.escape(START_MARKER)}\n.*?\n{re.escape(END_MARKER)}",
        flags=re.DOTALL,
    )
    replacement = "\n".join([START_MARKER, *new_lines, END_MARKER])
    if not pattern.search(readme_text):
        raise RuntimeError("README marker block missing after initialization.")
    return pattern.sub(replacement, readme_text, count=1)


def main() -> int:
    if not README_PATH.exists():
        print(f"ERROR: README not found at {README_PATH}", file=sys.stderr)
        return 1

    seen_ids = read_seen_ids(SEEN_IDS_PATH)

    try:
        entries = fetch_recent_entries()
    except Exception as exc:
        print(f"ERROR: failed to fetch arXiv feed: {exc}", file=sys.stderr)
        return 1

    deduped: dict[str, dict] = {}
    for item in entries:
        if item["id"] not in deduped:
            deduped[item["id"]] = item

    candidate_entries = [item for item in deduped.values() if is_relevant(item["text_blob"])]
    new_entries = [item for item in candidate_entries if item["id"] not in seen_ids][:MAX_PER_RUN]

    readme_text = README_PATH.read_text(encoding="utf-8")
    readme_text = ensure_marker_block(readme_text)

    if new_entries:
        bullets = [format_bullet(entry) for entry in new_entries]
    else:
        bullets = ["- _No new relevant papers found in this run._"]

    updated_readme = replace_marker_content(readme_text, bullets)
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
