#!/usr/bin/env python3
"""Generate visual section-title bars for every H2 in the README.

Each bar is used inside a real <h2>, so GitHub keeps semantic headings,
anchor links and a consistent visual hierarchy. There are three fixed
widths for desktop, tablet and phones, with light/dark versions.

GitHub can render interactive <details>, but the native marker cannot
be hidden or styled. These title bars therefore behave as section titles,
not fake accordions: content is always visible directly underneath.

    python3 scripts/make-summaries.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[2]
ASSETS = ROOT / "assets"
OUT = ASSETS / "generated" / "summaries"

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

# (section icon, label, compact hint, output name)
# v7 adds a 54px hero treatment for Featured Projects and GitHub Activity.
# Every asset is uniquely named so GitHub's image proxy cannot reuse v6.
SECTIONS = [
    ("section-work.svg", "What I build", "Delivery", "what-i-build-v7"),
    ("section-featured.svg", "Featured Projects", "6 highlighted", "featured-projects-v7"),
    ("section-experience.svg", "Professional experience", "10+ years", "professional-experience-v7"),
    ("section-beyond.svg", "Beyond the front-end", "Tools + runtime", "beyond-front-end-v7"),
    ("section-evidence.svg", "Evidence", "89 repositories", "evidence-v7"),
    ("section-process.svg", "How I work", "7 principles", "how-i-work-v7"),
    ("section-activity.svg", "GitHub Activity", "Live snapshots", "github-activity-v7"),
    ("section-more-projects.svg", "More projects", "8 repositories", "more-projects-v7"),
    ("section-core-stack.svg", "Core stack", "40+ technologies", "core-stack-v7"),
    ("section-docker-images.svg", "Docker images", "5 public images", "docker-images-v7"),
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
    hero = label in {"Featured Projects", "GitHub Activity"}
    height = 54 if hero else HEIGHT
    chip = 34 if hero else CHIP
    icon = 20 if hero else ICON
    font_size = 17 if hero else FONT_SIZE
    top = "#1b3763" if hero and not light else LIGHT_TOP if light else TILE_TOP
    bottom = "#0b1b32" if hero and not light else LIGHT_BOTTOM if light else TILE_BOTTOM
    border = "#4d8dff" if hero else LIGHT_BORDER if light else TILE_BORDER
    text_colour = LIGHT_LABEL if light else LABEL
    hint_colour = LIGHT_HINT if light else HINT
    chip_opacity = LIGHT_CHIP_OPACITY if light else CHIP_OPACITY

    inner, view_box = icon_inner(icon_file)
    badge_w = text_width(hint, HINT_SIZE) + BADGE_PAD * 2
    baseline = height / 2 + font_size * 0.35
    badge_baseline = (height - BADGE_HEIGHT) / 2 + BADGE_HEIGHT / 2 + HINT_SIZE * 0.35
    label_x = PAD + chip + GAP
    badge_x = width - RIGHT_PAD - badge_w
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">'
        f'<defs><linearGradient id="tile" x1="0" y1="0" x2="0" y2="1">'
        f'<stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/>'
        f"</linearGradient></defs>"
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" '
        f'fill="url(#tile)" stroke="{border}"/>'
        f'<rect x="{PAD}" y="{(height - chip) / 2}" width="{chip}" height="{chip}" rx="9" '
        f'fill="{hint_colour}" fill-opacity="{chip_opacity}"/>'
        f'<svg x="{PAD + (chip - icon) / 2}" y="{(height - icon) / 2}" width="{icon}" height="{icon}" '
        f'viewBox="{view_box}" fill="{hint_colour}">{inner}</svg>'
        f'<text x="{label_x}" y="{baseline:.1f}" fill="{text_colour}" '
        f'font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif" font-size="{font_size}" '
        f'font-weight="700">{label}</text>'
        f'<rect x="{badge_x:.1f}" y="{(height - BADGE_HEIGHT) / 2}" width="{badge_w:.1f}" '
        f'height="{BADGE_HEIGHT}" rx="{BADGE_HEIGHT / 2}" fill="{hint_colour}" fill-opacity="{chip_opacity}"/>'
        f'<text x="{badge_x + badge_w / 2:.1f}" y="{badge_baseline:.1f}" text-anchor="middle" fill="{hint_colour}" '
        f'font-family="Inter,Segoe UI,Arial,sans-serif" font-size="{HINT_SIZE}" '
        f'font-weight="600">{hint}</text>'
        f"</svg>"
    )


# One hand-laid size per layout breakpoint, so glyphs are never scaled
# below ~80%: phones (<500px viewport), tablet/laptop (500-1199px) and
# desktop (>=1200px, where the profile column is ~831-846px).
WIDTHS = [("", 820), ("mid/", 480), ("narrow/", 340)]


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
