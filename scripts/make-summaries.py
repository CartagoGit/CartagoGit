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

# (section icon, label, compact hint, output name)
# Every heading has a unique icon and a fresh -v6 asset name so GitHub's
# image proxy cannot reuse an earlier render with a different symbol.
SECTIONS = [
    ("section-work.svg", "What I build", "Delivery", "what-i-build-v6"),
    ("section-featured.svg", "Featured Projects", "6 highlighted", "featured-projects-v6"),
    ("section-experience.svg", "Professional experience", "10+ years", "professional-experience-v6"),
    ("section-beyond.svg", "Beyond the front-end", "Tools + runtime", "beyond-front-end-v6"),
    ("section-evidence.svg", "Evidence", "89 repositories", "evidence-v6"),
    ("section-process.svg", "How I work", "7 principles", "how-i-work-v6"),
    ("section-activity.svg", "GitHub Activity", "Live snapshots", "github-activity-v6"),
    ("section-more-projects.svg", "More projects", "8 repositories", "more-projects-v6"),
    ("section-core-stack.svg", "Core stack", "40+ technologies", "core-stack-v6"),
    ("section-docker-images.svg", "Docker images", "5 public images", "docker-images-v6"),
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
