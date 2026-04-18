#!/usr/bin/env python3
"""Validate relative markdown links inside README/SKILL files."""
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r'\[[^\]]+\]\(([^)]+)\)')
IGNORE_PREFIXES = ('http://', 'https://', '#', 'mailto:')

def check_file(path: Path):
    text = path.read_text(encoding='utf-8')
    bad = []
    for link in LINK_RE.findall(text):
        link = link.strip()
        if not link or link.startswith(IGNORE_PREFIXES):
            continue
        if link.startswith('<') and link.endswith('>'):
            link = link[1:-1]
        target = (path.parent / link).resolve()
        if not target.exists():
            bad.append(link)
    return bad

def main():
    if len(sys.argv) < 2:
        print('usage: check_links.py <file-or-dir>')
        raise SystemExit(1)
    target = Path(sys.argv[1])
    files = [target] if target.is_file() else [p for p in target.rglob('*.md') if p.name in {'README.md','README_EN.md','SKILL.md','README_ES.md','README_JA.md','README_KO.md'}]
    failed = False
    for file in files:
        bad = check_file(file)
        if bad:
            failed = True
            print(f'BROKEN LINKS: {file}')
            for link in bad:
                print('  ', link)
    if failed:
        raise SystemExit(1)
    print('OK: no broken relative links found')

if __name__ == '__main__':
    main()
