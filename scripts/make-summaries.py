#!/usr/bin/env python3
"""Generate the summary bars for the README's <details> sections.

GitHub strips every style from a README, so a bare <summary> reads as
plain text and nobody knows it can be opened. The way out is the same as
with the link buttons: an image that carries its own tile, icon, label
and content hint.

The native disclosure triangle cannot be hidden, but it CAN be moved to
the right edge — where an accordion's chevron belongs — with
`<summary dir="rtl" align="left">` plus `width="97%"` on the image:
GitHub keeps those three attributes, the marker takes the last ~26px of
the line and the bar fills the rest. The bar is drawn WITHOUT a viewBox
so that stretching it to the column width only widens the background
rect; icon and text keep their pixel size. The intrinsic width is kept
under ~270px so narrow phones never scale the image down.

    python3 scripts/make-summaries.py
"""
import base64
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
OUT = ASSETS / "summary"

TILE = "#0e1a2b"
TILE_BORDER = "#2b4786"
LABEL = "#e9f0ff"
HINT = "#7fb2ff"

LIGHT_TILE = "#f2f5fb"
LIGHT_BORDER = "#bfcee6"
LIGHT_LABEL = "#12233f"
LIGHT_HINT = "#1c5ed4"

HEIGHT = 38
PAD = 12
ICON = 18
GAP = 8
FONT_SIZE = 14
HINT_SIZE = 11
# Room for GitHub's native disclosure marker, which sits on the same line
# at the right edge of the bar (summary dir="rtl" + img width="97%").
MARKER = 24

# (section icon, label, hint, output name)
SECTIONS = [
    ("section-more-projects.svg", "More projects", "8 repositories", "more-projects"),
    ("section-core-stack.svg", "Core stack", "40+ technologies", "core-stack"),
    ("section-docker-images.svg", "Docker images", "5 public images", "docker-images"),
]


def text_width(text: str, size: float = FONT_SIZE) -> float:
    # Per-character advance widths measured from Liberation Sans Bold
    # (metric-compatible with Arial/Segoe UI), as a fraction of the size.
    wide = "mwMW@"
    narrow = "iljtfrI.,:;'|"
    total = 0.0
    for ch in text:
        if ch in wide:
            total += 0.86
        elif ch in narrow:
            total += 0.28
        elif ch == " ":
            total += 0.28
        elif ch.isupper():
            total += 0.68
        elif ch.isdigit():
            total += 0.56
        else:
            total += 0.55
    return total * size + 4


def icon_inner(name: str) -> tuple[str, str]:
    raw = (ASSETS / "brand" / name).read_text()
    box = re.search(r'viewBox="([^"]+)"', raw)
    view_box = box.group(1) if box else "0 0 24 24"
    inner = re.sub(r"^.*?<svg[^>]*>", "", raw, flags=re.S)
    inner = re.sub(r"</svg>\s*$", "", inner, flags=re.S)
    inner = re.sub(r'\s(width|height)="[^"]*"', "", inner)
    inner = re.sub(r'\sfill="[^"]*"', "", inner)
    return inner, view_box


def bar(icon_file: str, label: str, hint: str, light: bool) -> str:
    tile = LIGHT_TILE if light else TILE
    border = LIGHT_BORDER if light else TILE_BORDER
    text_colour = LIGHT_LABEL if light else LABEL
    hint_colour = LIGHT_HINT if light else HINT

    inner, view_box = icon_inner(icon_file)
    label_w = text_width(label)
    hint_w = text_width(hint, HINT_SIZE)
    # Intrinsic width: content plus the marker slot. Kept under ~270px so
    # a 390px phone (284px column at 97%) never scales the image down.
    # No viewBox on the root: user units == CSS pixels, so when the README
    # stretches the image to the column width only the background rect grows.
    width = PAD + ICON + GAP + label_w + GAP + hint_w + MARKER + PAD
    baseline = HEIGHT / 2 + FONT_SIZE * 0.35
    hint_x = PAD + ICON + GAP + label_w + GAP
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{HEIGHT}">'
        f'<rect x="0.5" y="0.5" width="99%" height="{HEIGHT - 1}" rx="8" '
        f'fill="{tile}" stroke="{border}"/>'
        f'<svg x="{PAD}" y="{(HEIGHT - ICON) / 2}" width="{ICON}" height="{ICON}" '
        f'viewBox="{view_box}" fill="{hint_colour}">{inner}</svg>'
        f'<text x="{PAD + ICON + GAP}" y="{baseline:.1f}" fill="{text_colour}" '
        f'font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif" font-size="{FONT_SIZE}" '
        f'font-weight="700">{label}</text>'
        f'<text x="{hint_x:.1f}" y="{baseline:.1f}" fill="{hint_colour}" '
        f'font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif" font-size="{HINT_SIZE}" '
        f'font-weight="600">{hint}</text>'
        f"</svg>"
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "light").mkdir(parents=True, exist_ok=True)
    for icon_file, label, hint, name in SECTIONS:
        (OUT / f"{name}.svg").write_text(bar(icon_file, label, hint, light=False))
        (OUT / "light" / f"{name}.svg").write_text(bar(icon_file, label, hint, light=True))
        print("wrote", name, "(dark + light)")


if __name__ == "__main__":
    main()
