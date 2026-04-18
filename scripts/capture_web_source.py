#!/usr/bin/env python3
"""Capture a web source into a Markdown file with metadata and cleaned text."""
from __future__ import annotations

import argparse
import datetime as dt
import io
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from pypdf import PdfReader

TODAY = dt.date.today().isoformat()
TIMEOUT = 20
UA = {"User-Agent": "Mozilla/5.0 Codex/1.0"}

FULL_TYPES = {
    "public_domain_book",
    "classical_text",
    "classical_text_selection",
    "official_collected_work",
    "official_speech",
    "speech_transcript",
    "public_recipe_page",
}
FULL_DOMAINS = {
    "classics.mit.edu",
    "ctext.org",
    "www.marxists.org",
    "marxists.org",
    "gov.cn",
    "www.gov.cn",
}
INDEX_TYPES = {
    "official_site",
    "index_page",
    "archive_root",
    "archive_index",
    "official_archive_card",
    "official_long_text_index",
    "blog_corpus_index",
    "corpus_reference_page",
}
NAV_WORDS = {
    "home",
    "browse and comment",
    "browse",
    "search",
    "help",
    "buy books and cd-roms",
    "commentary",
    "download",
    "table of contents",
    "language",
    "rss",
    "newsletters",
    "follow us",
    "sign in",
    "sign out",
    "your account",
    "share",
    "copied",
    "choose your language",
    "radio",
    "tv",
    "live",
    "opinions",
    "video",
    "home >",
    "home >>",
    "首页",
    "简",
    "繁",
    "en",
    "打开app",
    "用app打开",
    "app中查看更多做法",
    "follow cgtn on:",
    "we are china",
    "archive",
    "archives",
    "home page",
    "recently viewed",
    "you may also like",
    "notify me",
}


def yaml_quote(value: str) -> str:
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


def fetch_via_jina(url: str) -> dict:
    wrapped = f"https://r.jina.ai/http://{url}"
    response = requests.get(wrapped, headers=UA, timeout=TIMEOUT)
    response.raise_for_status()
    text = response.text.replace("\r\n", "\n")
    final_url = url
    match = re.search(r"^URL Source:\s*(.+)$", text, re.M)
    if match:
        final_url = match.group(1).strip()
    markdown = text.split("Markdown Content:\n", 1)[1] if "Markdown Content:\n" in text else text
    return {
        "status": response.status_code,
        "final_url": final_url,
        "content_type": response.headers.get("content-type", "text/plain"),
        "text": markdown.strip(),
    }


def fetch_direct_html(url: str) -> dict:
    response = requests.get(url, headers=UA, timeout=TIMEOUT)
    response.raise_for_status()
    response.encoding = response.apparent_encoding or response.encoding or "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    for tag in soup(["script", "style", "noscript", "svg", "path", "form", "button"]):
        tag.decompose()
    for tag in soup.find_all(["header", "footer", "nav", "aside"]):
        tag.decompose()
    root = soup.find("article") or soup.find("main") or soup.body or soup
    lines = []
    if title:
        lines.append(f"# {title}")
    for element in root.find_all(["h1", "h2", "h3", "h4", "p", "li", "blockquote", "pre", "td"]):
        text = re.sub(r"\s+", " ", element.get_text(" ", strip=True)).strip()
        if text:
            lines.append(text)
    return {
        "status": response.status_code,
        "final_url": response.url,
        "content_type": response.headers.get("content-type", "text/html"),
        "text": "\n".join(lines),
    }


def fetch_pdf(url: str) -> dict:
    response = requests.get(url, headers=UA, timeout=TIMEOUT)
    response.raise_for_status()
    reader = PdfReader(io.BytesIO(response.content))
    parts = []
    for page in reader.pages:
        try:
            parts.append(page.extract_text() or "")
        except Exception:
            pass
    return {
        "status": response.status_code,
        "final_url": url,
        "content_type": response.headers.get("content-type", "application/pdf"),
        "text": "\n\n".join(parts).strip(),
    }


def fetch_url(url: str) -> dict:
    if url.lower().endswith(".pdf"):
        return fetch_pdf(url)
    try:
        return fetch_via_jina(url)
    except Exception:
        return fetch_direct_html(url)


def choose_mode(source_type: str, url: str) -> str:
    domain = urlparse(url).netloc.lower()
    if source_type in FULL_TYPES:
        return "full"
    if domain in FULL_DOMAINS and source_type not in INDEX_TYPES:
        return "full"
    return "extract"


def md_link_text(line: str) -> str:
    line = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", line)
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", line)


def clean_markdown(text: str, mode: str) -> tuple[str, str, list[str]]:
    lines = []
    seen = set()
    for raw in text.splitlines():
        line = md_link_text(raw).strip()
        if not line:
            continue
        line = re.sub(r"\s+", " ", line)
        low = line.lower().strip(" -:*_#")
        if low in NAV_WORDS:
            continue
        if re.fullmatch(r"[-*_ ]+", line):
            continue
        if line.startswith("URL Source:") or line.startswith("Published Time:"):
            continue
        if sum(token in low for token in ["asia-pacific", "middle east", "americas", "opinions", "documentary"]) >= 2:
            continue
        if "albanian shqip" in low or "arabic العربية" in low:
            continue
        if line not in seen:
            lines.append(line)
            seen.add(line)
    headings = []
    for line in lines:
        if line.startswith("#"):
            heading = re.sub(r"^#+\s*", "", line).strip()
            if heading and heading not in headings:
                headings.append(heading)
    if len(lines) > 8:
        start = 0
        for index, line in enumerate(lines):
            if len(line) > 80 and not line.startswith("#") and "[" not in line:
                start = max(0, index - 1)
                break
        if start:
            lines = ([lines[0]] if lines[0].startswith("#") else []) + lines[start:]
    captured = "\n\n".join(lines).strip()
    if mode == "full":
        limit = 80000
        heading_label = "## Captured Full Text"
    else:
        limit = 16000
        heading_label = "## Captured Long Extract"
    truncated = len(captured) > limit
    captured = captured[:limit].rstrip()
    if truncated:
        captured += f"\n\n[Truncated after {limit} characters to keep the repo readable.]"
    return heading_label, captured, headings[:20]


def build_markdown(args, fetched: dict) -> str:
    mode = choose_mode(args.source_type, args.url)
    heading_label, captured, headings = clean_markdown(fetched["text"], mode)
    capture_method = "auto_capture_fulltext" if mode == "full" else "auto_capture_long_extract"
    metadata = {
        "title": args.title,
        "author": args.author,
        "date": args.date,
        "url": args.url,
        "source_type": args.source_type,
        "capture_method": capture_method,
        "language": args.language,
        "rights_note": args.rights_note,
        "captured_at": TODAY,
    }
    frontmatter = "---\n" + "\n".join(f"{key}: {yaml_quote(value)}" for key, value in metadata.items()) + "\n---\n\n"
    sections = [
        f"# {args.title}",
        "## Source Metadata\n"
        f"- Author: {args.author}\n"
        f"- Date: {args.date}\n"
        f"- URL: {args.url}\n"
        f"- Source type: `{args.source_type}`\n"
        f"- Capture method: `{capture_method}`\n"
        f"- Language: `{args.language}`\n"
        f"- Rights note: {args.rights_note}",
        heading_label + "\n\n" + captured,
    ]
    if headings:
        sections.append("## Extracted Headings\n" + "\n".join(f"- {heading}" for heading in headings))
    sections.append(
        "## Traceability\n"
        f"- Original URL: {args.url}\n"
        f"- Final URL: {fetched.get('final_url', args.url)}\n"
        f"- HTTP status: {fetched.get('status', '')}\n"
        f"- Content type: {fetched.get('content_type', '')}\n"
        f"- Capture mode: `{mode}`\n"
        f"- Captured at: {TODAY}"
    )
    return frontmatter + "\n\n".join(sections).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument("output")
    parser.add_argument("--title", required=True)
    parser.add_argument("--author", default="Unknown")
    parser.add_argument("--date", default="Unknown")
    parser.add_argument("--source-type", default="article")
    parser.add_argument("--language", default="zh")
    parser.add_argument("--rights-note", default="Metadata + cleaned capture")
    args = parser.parse_args()

    fetched = fetch_url(args.url)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_markdown(args, fetched), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
