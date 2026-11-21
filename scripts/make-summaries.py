#!/usr/bin/env python3
"""Generate the summary bars for the README's <details> sections.

GitHub strips every style from a README, so a bare <summary> reads as
plain text and nobody knows it can be opened. The way out is the same as
with the link buttons: an image that carries its own tile, icon, label
and a chevron that says "this opens".

A second variant with the chevron pointing up is served through
`details[open] .when-open` — GitHub keeps that selector working, so the
bar itself tells you whether the section is open or closed.

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
PAD = 14
ICON = 18
GAP = 9
FONT_SIZE = 14
CHEVRON = 16
CHEVRON_GAP = 12

# (section icon, label, hint, output name)
SECTIONS = [
    ("section-more-projects.svg", "More projects", "8 repositories", "more-projects"),
    ("section-core-stack.svg", "Core stack", "40+ technologies", "core-stack"),
    ("section-docker-images.svg", "Docker images", "5 public images", "docker-images"),
]


def text_width(text: str) -> float:
    wide = "mwMW@"
    narrow = "iljtfrI.,:;'|"
    total = 0.0
    for ch in text:
        if ch in wide:
            total += 0.86
        elif ch in narrow:
            total += 0.34
        elif ch == " ":
            total += 0.28
        elif ch.isupper():
            total += 0.68
        elif ch.isdigit():
            total += 0.56
        else:
            total += 0.55
    return total * FONT_SIZE * 1.22 + 4


def icon_inner(name: str, colour: str) -> tuple[str, str]:
    raw = (ASSETS / "brand" / name).read_text()
    box = re.search(r'viewBox="([^"]+)"', raw)
    view_box = box.group(1) if box else "0 0 24 24"
    inner = re.sub(r"^.*?<svg[^>]*>", "", raw, flags=re.S)
    inner = re.sub(r"</svg>\s*$", "", inner, flags=re.S)
    inner = re.sub(r'\s(width|height)="[^"]*"', "", inner)
    inner = re.sub(r'\sfill="[^"]*"', "", inner)
    return inner, view_box


def chevron(direction: str, colour: str) -> str:
    # A simple V, drawn here so the rotation is exact.
    if direction == "down":
        path = "M4 6 L8 10 L12 6"
    else:
        path = "M4 10 L8 6 L12 10"
    return (
        f'<svg viewBox="0 0 16 16" width="{CHEVRON}" height="{CHEVRON}">'
        f'<path d="{path}" fill="none" stroke="{colour}" stroke-width="2" '
        f'stroke-linecap="round" stroke-linejoin="round"/></svg>'
    )


def bar(icon_file: str, label: str, hint: str, direction: str, light: bool) -> str:
    tile = LIGHT_TILE if light else TILE
    border = LIGHT_BORDER if light else TILE_BORDER
    text_colour = LIGHT_LABEL if light else LABEL
    hint_colour = LIGHT_HINT if light else HINT

    inner, view_box = icon_inner(icon_file, hint_colour)
    label_w = text_width(label)
    hint_w = text_width(hint) * 0.82
    width = PAD + ICON + GAP + label_w + GAP + hint_w + CHEVRON_GAP + CHEVRON + PAD
    baseline = HEIGHT / 2 + FONT_SIZE * 0.35
    hint_x = PAD + ICON + GAP + label_w + GAP
    chev_x = width - PAD - CHEVRON
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{HEIGHT}" '
        f'viewBox="0 0 {width:.0f} {HEIGHT}" role="img" aria-label="{label}">'
        f'<rect x="0.5" y="0.5" width="{width - 1:.0f}" height="{HEIGHT - 1}" rx="8" '
        f'fill="{tile}" stroke="{border}"/>'
        f'<svg x="{PAD}" y="{(HEIGHT - ICON) / 2}" width="{ICON}" height="{ICON}" '
        f'viewBox="{view_box}" fill="{hint_colour}">{inner}</svg>'
        f'<text x="{PAD + ICON + GAP}" y="{baseline:.1f}" fill="{text_colour}" '
        f'font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif" font-size="{FONT_SIZE}" '
        f'font-weight="700">{label}</text>'
        f'<text x="{hint_x:.1f}" y="{baseline:.1f}" fill="{hint_colour}" '
        f'font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif" font-size="{FONT_SIZE * 0.82:.1f}" '
        f'font-weight="600">{hint}</text>'
        f'<g transform="translate({chev_x:.1f},{(HEIGHT - CHEVRON) / 2})">'
        + chevron(direction, hint_colour)
        + "</g>"
        f"</svg>"
    )


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "light").mkdir(parents=True, exist_ok=True)
    for icon_file, label, hint, name in SECTIONS:
        for direction in ("down",):
            suffix = "" if direction == "down" else "-open"
            path = OUT / f"{name}{suffix}.svg"
            path.write_text(bar(icon_file, label, hint, direction, light=False))
            light_path = OUT / "light" / f"{name}{suffix}.svg"
            light_path.write_text(bar(icon_file, label, hint, direction, light=True))
        print("wrote", name, "(closed + open, dark + light)")


if __name__ == "__main__":
    main()
