#!/usr/bin/env python3
"""
build.py — sync shared partials into every page that uses them.

Each shared block in /_partials/<name>.html is the single source of truth.
Pages declare an insertion point with a pair of HTML comment markers:

    <!-- @partial:<name> -->
    ...inlined content...
    <!-- @endpartial -->

Running this script reads each partial and rewrites the markup between the
matching markers in every *.html file at the project root. Any indentation
on the @partial marker line is preserved on every line of the inlined block,
so the rendered HTML stays tidy.

Usage:
    python3 build.py            # process all *.html files in this folder
    python3 build.py --check    # exit non-zero if any page is out of sync

After editing a partial, run `python3 build.py` and commit the resulting
diff. Pages then work as plain HTML from any location (file:// or any
static host) with no runtime JS dependency.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PARTIALS_DIR = ROOT / "_partials"

# Capture: leading indent, partial name, the existing inlined block, the
# closing marker (with its own optional indent).
PATTERN = re.compile(
    r"(?P<indent>[ \t]*)<!--\s*@partial:(?P<name>[\w\-]+)\s*-->"
    r"(?P<body>.*?)"
    r"(?P<close_indent>[ \t]*)<!--\s*@endpartial\s*-->",
    re.DOTALL,
)


def load_partial(name: str) -> str:
    path = PARTIALS_DIR / f"{name}.html"
    if not path.is_file():
        raise FileNotFoundError(f"Missing partial: {path}")
    return path.read_text(encoding="utf-8").rstrip("\n")


def render_block(name: str, indent: str) -> str:
    # Inline the partial body verbatim — DO NOT reindent. Reindenting can
    # add leading whitespace inside multi-line text nodes (e.g. <span>RGB…
    # \nCMYK…</span>) which would corrupt the rendered text.
    body = load_partial(name)
    return (
        f"{indent}<!-- @partial:{name} -->\n"
        f"{body}\n"
        f"{indent}<!-- @endpartial -->"
    )


def process(html: str) -> tuple[str, int]:
    replacements = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal replacements
        name = match.group("name")
        indent = match.group("indent")
        replacements += 1
        return render_block(name, indent)

    return PATTERN.sub(replace, html), replacements


def main() -> int:
    check_mode = "--check" in sys.argv
    pages = sorted(p for p in ROOT.glob("*.html") if p.is_file())
    out_of_sync: list[Path] = []
    total_replacements = 0
    print(f"Found {len(pages)} page(s) and {len(list(PARTIALS_DIR.glob('*.html')))} partial(s).")
    for page in pages:
        original = page.read_text(encoding="utf-8")
        updated, count = process(original)
        if count and updated != original:
            if check_mode:
                out_of_sync.append(page)
            else:
                page.write_text(updated, encoding="utf-8")
                print(f"  updated {page.name} ({count} block{'s' if count != 1 else ''})")
        elif count:
            print(f"  {page.name}: {count} block{'s' if count != 1 else ''} already in sync")
        total_replacements += count
    if check_mode and out_of_sync:
        print("\nOut of sync:")
        for p in out_of_sync:
            print(f"  {p.name}")
        print("\nRun `python3 build.py` to update.")
        return 1
    print(f"\nDone. {total_replacements} block(s) processed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
