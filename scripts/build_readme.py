#!/usr/bin/env python3
"""Build a combined README.md from README_EN.md and README_IT.md.

Usage: python3 scripts/build_readme.py
This writes/overwrites README.md with a bilingual document and top navigation.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EN = ROOT / "README_EN.md"
IT = ROOT / "README_IT.md"
OUT = ROOT / "README.md"

def read_text(p: Path) -> str:
    if not p.exists():
        return f"<!-- missing: {p.name} -->\n"
    return p.read_text(encoding="utf-8").strip() + "\n"

def build():
    en = read_text(EN)
    it = read_text(IT)

    parts = []
    parts.append("[English](#english) | [Italiano](#italiano)\n")
    parts.append("\n")
    parts.append("<a id=\"english\"></a>\n\n")
    parts.append(en)
    parts.append("\n---\n\n")
    parts.append("<a id=\"italiano\"></a>\n\n")
    parts.append(it)
    content = "\n".join(parts)

    OUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUT}")

if __name__ == '__main__':
    build()
