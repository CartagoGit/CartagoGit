#!/usr/bin/env python3
"""Generate the section link bars for the README.

GitHub's native <details> marker cannot be hidden (the sanitizer strips
every style/class, and the marker is tied to the first <summary>, which
is also the only element that toggles). A floating triangle next to a
button reads as broken, so the sections are plain anchored headings at
the bottom of the README and these bars are premium link buttons:
gradient tile, icon chip, bold label and a content-count badge pinned to
the right edge. No arrows anywhere.

The bar is drawn at two fixed sizes, served through <picture media>:
820px for desktop columns and 280px for phones. Fixed sizes matter: an
SVG without a viewBox served through <img> is stretched by the browser
when CSS resizes it, which distorts the text; with a viewBox everything
scales uniformly and the text shrinks on phones. Two hand-laid sizes
keep every glyph at its intended pixel size on every screen.

    python3 scripts/make-summaries.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
OUT = ASSETS / "summary"

TILE_TOP = "#13253f"
TILE_BOTTOM = "#0c1727"
TILE_BORDER = "#2b4786"
LABEL = "#e9f0ff"
HINT = "#7fb2ff"
CHIP_OPACITY = "0.16"

LIGHT_TOP = "#ffffff"
LIGHT_BOTTOM = "#e9eef7"
LIGHT_BORDER = "#bfcee6"
LIGHT_LABEL = "#12233f"
LIGHT_HINT = "#1c5ed4"
LIGHT_CHIP_OPACITY = "0.10"

HEIGHT = 44
PAD = 10
CHIP = 28
ICON = 16
GAP = 10
FONT_SIZE = 15
HINT_SIZE = 11
BADGE_PAD = 10
BADGE_HEIGHT = 22
RIGHT_PAD = 12

# (section icon, label, hint, output name)
# Names carry a -v3 suffix: GitHub's image proxy caches by full URL and
# ignores query strings, so a changed asset must be renamed to be seen.
SECTIONS = [
    ("section-more-projects.svg", "More projects", "8 repositories", "more-projects-v3"),
    ("section-core-stack.svg", "Core stack", "40+ technologies", "core-stack-v3"),
    ("section-docker-images.svg", "Docker images", "5 public images", "docker-images-v3"),
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


def bar(icon_file: str, label: str, hint: str, light: bool, width: int) -> str:
    top = LIGHT_TOP if light else TILE_TOP
    bottom = LIGHT_BOTTOM if light else TILE_BOTTOM
    border = LIGHT_BORDER if light else TILE_BORDER
    text_colour = LIGHT_LABEL if light else LABEL
    hint_colour = LIGHT_HINT if light else HINT
    chip_opacity = LIGHT_CHIP_OPACITY if light else CHIP_OPACITY

    inner, view_box = icon_inner(icon_file)
    badge_w = text_width(hint, HINT_SIZE) + BADGE_PAD * 2
    baseline = HEIGHT / 2 + FONT_SIZE * 0.35
    badge_baseline = (HEIGHT - BADGE_HEIGHT) / 2 + BADGE_HEIGHT / 2 + HINT_SIZE * 0.35
    label_x = PAD + CHIP + GAP
    badge_x = width - RIGHT_PAD - badge_w
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{HEIGHT}" '
        f'viewBox="0 0 {width} {HEIGHT}">'
        f'<defs><linearGradient id="tile" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/>'
        f"</linearGradient></defs>"
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{HEIGHT - 1}" rx="10" '
        f'fill="url(#tile)" stroke="{border}"/>'
        f'<rect x="{PAD}" y="{(HEIGHT - CHIP) / 2}" width="{CHIP}" height="{CHIP}" rx="8" '
        f'fill="{hint_colour}" fill-opacity="{chip_opacity}"/>'
        f'<svg x="{PAD + (CHIP - ICON) / 2}" y="{(HEIGHT - ICON) / 2}" width="{ICON}" height="{ICON}" '
        f'viewBox="{view_box}" fill="{hint_colour}">{inner}</svg>'
        f'<text x="{label_x}" y="{baseline:.1f}" fill="{text_colour}" '
        f'font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif" font-size="{FONT_SIZE}" '
        f'font-weight="700">{label}</text>'
        f'<rect x="{badge_x:.1f}" y="{(HEIGHT - BADGE_HEIGHT) / 2}" width="{badge_w:.1f}" '
        f'height="{BADGE_HEIGHT}" rx="{BADGE_HEIGHT / 2}" fill="{hint_colour}" fill-opacity="{chip_opacity}"/>'
        f'<text x="{badge_x + badge_w / 2:.1f}" y="{badge_baseline:.1f}" text-anchor="middle" fill="{hint_colour}" '
        f'font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif" font-size="{HINT_SIZE}" '
        f'font-weight="600">{hint}</text>'
        f"</svg>"
    )


# Desktop bars fill the profile column; phone bars fit a 390px viewport
# (293px of content) without any downscaling.
WIDTHS = [("", 820), ("narrow/", 280)]


def main() -> None:
    for prefix, width in WIDTHS:
        out = OUT / prefix if prefix else OUT
        (out / "light").mkdir(parents=True, exist_ok=True)
        for icon_file, label, hint, name in SECTIONS:
            (out / f"{name}.svg").write_text(bar(icon_file, label, hint, False, width))
            (out / "light" / f"{name}.svg").write_text(bar(icon_file, label, hint, True, width))
        print("wrote", prefix or "wide/", "bars (dark + light)")


if __name__ == "__main__":
    main()
