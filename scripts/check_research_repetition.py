#!/usr/bin/env python3
"""Detect repeated 3-line windows inside research markdown files.

Ignore windows that contain blank lines so the checker focuses on repeated prose
rather than ordinary Markdown spacing.
"""
import sys
from pathlib import Path
from collections import defaultdict


def normalize(line: str) -> str:
    return ' '.join(line.split())


def scan(path: Path):
    lines = path.read_text(encoding='utf-8').splitlines()
    buckets = defaultdict(list)
    for i in range(len(lines) - 2):
        trio = lines[i:i + 3]
        if any(not line.strip() for line in trio):
            continue
        window = '\n'.join(normalize(line) for line in trio)
        if window:
            buckets[window].append(i + 1)
    return {k: v for k, v in buckets.items() if len(v) > 1}


def main():
    if len(sys.argv) < 2:
        print('usage: check_research_repetition.py <file-or-dir>')
        raise SystemExit(1)
    target = Path(sys.argv[1])
    files = [target] if target.is_file() else sorted(target.rglob('*.md'))
    failed = False
    for file in files:
        dupes = scan(file)
        if dupes:
            failed = True
            print(f'REPEATED WINDOW: {file}')
            for _, lines in list(dupes.items())[:10]:
                print('  lines:', ', '.join(map(str, lines)))
    if failed:
        raise SystemExit(1)
    print('OK: no repeated 3-line windows found')


if __name__ == '__main__':
    main()
