#!/usr/bin/env python3
"""Validate whether a skill repo has real captured source materials."""
from __future__ import annotations

import sys
from pathlib import Path

THRESHOLDS = {
    "aristotle-skill": {"books": 3, "articles": 2, "transcripts": 0},
    "socrates-skill": {"books": 3, "articles": 2, "transcripts": 0},
    "sun-tzu-skill": {"books": 3, "articles": 2, "transcripts": 0},
    "confucius-skill": {"books": 3, "articles": 2, "transcripts": 0},
    "leonardo-da-vinci-skill": {"books": 3, "articles": 2, "transcripts": 0},
    "isaac-newton-skill": {"books": 3, "articles": 2, "transcripts": 0},
    "sigmund-freud-skill": {"books": 3, "articles": 2, "transcripts": 0},
    "carl-jung-skill": {"books": 3, "articles": 2, "transcripts": 0},
    "friedrich-nietzsche-skill": {"books": 3, "articles": 2, "transcripts": 0},
    "warren-buffett-skill": {"books": 2, "articles": 3, "transcripts": 3},
    "duan-yongping-skill": {"books": 2, "articles": 3, "transcripts": 3},
    "nikola-tesla-skill": {"books": 1, "articles": 3, "transcripts": 3},
    "zhang-xue-skill": {"books": 1, "articles": 3, "transcripts": 3},
    "mao-zedong-skill": {"books": 2, "articles": 3, "transcripts": 2},
    "xi-skill": {"books": 2, "articles": 3, "transcripts": 2},
    "moshi-jibao-skill": {"books": 0, "articles": 5, "transcripts": 2},
    "first-principles-skill": {"books": 4, "articles": 4, "transcripts": 2},
}


def source_files(path: Path) -> list[Path]:
    return [p for p in path.rglob("*.md") if p.is_file() and p.name.lower() != "readme.md"]


def has_capture_section(path: Path) -> bool:
    text = path.read_text(encoding="utf-8", errors="ignore")
    return "## Captured Full Text" in text or "## Captured Long Extract" in text


def main() -> int:
    repo = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    name = repo.name
    expected = THRESHOLDS.get(name)
    if not expected:
        print(f"FAIL {name}: no threshold entry")
        return 1

    failed = False
    for kind in ("books", "transcripts", "articles"):
        files = source_files(repo / "references" / "sources" / kind)
        need = expected.get(kind, 0)
        if len(files) < need:
            failed = True
            print(f"FAIL {name}: {kind} count {len(files)} < {need}")
        missing_capture = [str(path) for path in files if not has_capture_section(path)]
        if missing_capture:
            failed = True
            print(f"FAIL {name}: {kind} files without captured content:")
            for path in missing_capture:
                print(f"  - {path}")

    if failed:
        return 1

    counts = {kind: len(source_files(repo / 'references' / 'sources' / kind)) for kind in ('books', 'transcripts', 'articles')}
    print(f"OK {name}: books={counts['books']} transcripts={counts['transcripts']} articles={counts['articles']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
