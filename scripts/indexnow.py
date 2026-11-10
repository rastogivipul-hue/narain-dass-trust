#!/usr/bin/env python3
"""Ping IndexNow (Bing, Yandex and other participants) with every URL in sitemap.xml.

The key file is the 32-character hex file at the site root
(https://ndrtrust.org/<key>.txt). Its contents are the key. IndexNow is a
hint to search engines; it does not change the site. Network and HTTP errors
are printed and the process exits 0 so a failure cannot fail the Vercel deploy
or a required check.

Usage (from the repository root):
    python3 scripts/indexnow.py
"""
from __future__ import annotations

import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HOST = "ndrtrust.org"
SITEMAP = ROOT / "sitemap.xml"
ENDPOINT = "https://api.indexnow.org/indexnow"
NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}


def find_key() -> str | None:
    for path in ROOT.glob("*.txt"):
        name = path.stem
        if re.fullmatch(r"[a-f0-9]{32}", name) and path.read_text(encoding="utf-8").strip() == name:
            return name
    return None


def urls_from_sitemap() -> list[str]:
    if not SITEMAP.is_file():
        print("indexnow: sitemap.xml not found", file=sys.stderr)
        return []
    tree = ET.parse(SITEMAP)
    found = []
    for loc in tree.findall(".//sm:loc", NS):
        text = (loc.text or "").strip()
        if text.startswith("https://ndrtrust.org/") or text == "https://ndrtrust.org/":
            found.append(text)
    # ElementTree may not match if the default namespace handling differs.
    if not found:
        for loc in tree.iter():
            if loc.tag.endswith("loc") and loc.text:
                text = loc.text.strip()
                if text.startswith("https://" + HOST):
                    found.append(text)
    return found


def main() -> int:
    key = find_key()
    if not key:
        print("indexnow: no key file found; skipping", file=sys.stderr)
        return 0
    url_list = urls_from_sitemap()
    if not url_list:
        print("indexnow: no URLs in sitemap; skipping", file=sys.stderr)
        return 0
    payload = {
        "host": HOST,
        "key": key,
        "keyLocation": f"https://{HOST}/{key}.txt",
        "urlList": url_list,
    }
    import json

    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        ENDPOINT,
        data=data,
        headers={"Content-Type": "application/json; charset=utf-8"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            print(f"indexnow: HTTP {resp.status} for {len(url_list)} URLs")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")[:500]
        print(f"indexnow: HTTP {exc.code} {body}", file=sys.stderr)
    except Exception as exc:  # network, DNS, timeout: do not fail the deploy
        print(f"indexnow: {type(exc).__name__}: {exc}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
