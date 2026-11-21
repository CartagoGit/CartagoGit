#!/usr/bin/env python3
"""Generate the link buttons used in the profile README.

GitHub strips every `style` attribute and every `<style>` block from a README,
and the reader may be looking at it in a light or a dark theme. So a link
cannot be restyled from the markdown side, and a bare hyperlink always looks
like a purple hyperlink.

The way out is an image that carries its own contrast: a rounded tile with a
fixed fill, the icon inside it and the label next to it. The tile reads the
same on a white page and on a dark one, and the whole thing looks like a
button rather than a link.

Run it from the repository root:

    python3 scripts/make-buttons.py
"""
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
OUT = ASSETS / "btn"

# The tile: a deep navy that belongs to the palette of the portfolio site, with
# a border that separates it from a white page without glowing on a dark one.
TILE = "#0e1a2b"
TILE_BORDER = "#2b4786"
ICON_COLOR = "#7fb2ff"
LABEL = "#e9f0ff"

HEIGHT = 30
PAD = 10
ICON = 15
GAP = 7
FONT_SIZE = 12.5

# Approximate advance widths in em for Inter at FONT_SIZE. A single average
# would cut the longer labels short, so the narrow and the wide characters
# are counted apart.
_NARROW = "iljtfrI.,:;'|!()[]{}/\\"
_WIDE = "mwMW@%"
_GLYPH_W = {
    " ": 0.28,
    "I": 0.30,
    "l": 0.28,
    "i": 0.28,
    "j": 0.28,
    "t": 0.36,
    "f": 0.34,
    "r": 0.38,
    "M": 0.86,
    "W": 0.86,
    "m": 0.84,
    "w": 0.72,
    ".": 0.28,
    ",": 0.28,
    ":": 0.28,
    ";": 0.28,
    "'": 0.22,
    "’": 0.22,
    "í": 0.28,
    "ú": 0.56,
    "ó": 0.56,
    "é": 0.55,
    "á": 0.55,
    "ñ": 0.57,
}


def text_width(text: str) -> float:
    """Width of a label in pixels, close enough to not clip it."""
    total = 0.0
    for ch in text:
        if ch in _GLYPH_W:
            total += _GLYPH_W[ch]
        elif ch in _NARROW:
            total += 0.36
        elif ch in _WIDE:
            total += 0.86
        elif ch.isupper():
            total += 0.68
        elif ch.isdigit():
            total += 0.56
        else:
            total += 0.55
    return total * FONT_SIZE

# (icon file, label, output name)
BUTTONS = [
    ("github.svg", "DelendAI", "repo-delendai"),
    ("github.svg", "API Source Tanit", "repo-tanit"),
    ("github.svg", "QuickModel", "repo-quickmodel"),
    ("github.svg", "Keyer", "repo-keyer"),
    ("github.svg", "Print CV", "repo-print-cv"),
    ("github.svg", "Cartago", "repo-cartago"),
    ("github.svg", "Aoe2 mods", "repo-aoe2"),
    ("github.svg", "PC Fútbol 6", "repo-pcfutbol"),
    ("github.svg", "Steam Keys", "repo-steam-keys"),
    ("github.svg", "Player Club Dynasty", "repo-pcd"),
    ("releases.svg", "Releases", "releases"),
    ("docs.svg", "Docs", "docs"),
    ("live.svg", "Live", "live"),
    ("package.svg", "npm", "npm"),
    ("brand/github.svg", "GitHub", "github"),
    ("live.svg", "Portfolio", "portfolio"),
    ("brand/launch.svg", "Activity", "activity"),
    ("brand/linkedin.svg", "LinkedIn", "linkedin"),
    ("brand/npm.svg", "npm", "npm-brand"),
    ("brand/docker.svg", "Docker Hub", "docker"),
]


def icon_markup(name: str) -> tuple[str, str, str]:
    """Return (content, view_box, colour) of an existing icon file."""
    raw = (ASSETS / name).read_text()
    view_box = re.search(r'viewBox="([^"]+)"', raw)
    box = view_box.group(1).split() if view_box else ["0", "0", "24", "24"]
    root_fill = re.search(r'<svg[^>]*\sfill="([^"]+)"', raw)
    colour = root_fill.group(1) if root_fill else ICON_COLOR
    # Keep only the drawing instructions: the root <svg> attributes are
    # replaced by the nested one we build ourselves.
    inner = re.sub(r"^.*?<svg[^>]*>", "", raw, flags=re.S)
    inner = re.sub(r"</svg>\s*$", "", inner, flags=re.S)
    # Iconify ships 1em boxes; the size is decided by the nested viewport.
    inner = re.sub(r'\s(width|height)="[^"]*"', "", inner)
    # The path fills would win over the colour of the nested svg.
    inner = re.sub(r'\sfill="[^"]*"', "", inner)
    inner = re.sub(r'\sstroke="[^"]*"', "", inner)
    return inner, " ".join(box), colour


def button(icon_file: str, label: str) -> str:
    inner, view_box, colour = icon_markup(icon_file)
    label_w = text_width(label)
    width = PAD + ICON + GAP + label_w + PAD
    text_x = PAD + ICON + GAP
    baseline = HEIGHT / 2 + FONT_SIZE * 0.35
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width:.0f}" height="{HEIGHT}" '
        f'viewBox="0 0 {width:.0f} {HEIGHT}" role="img" aria-label="{label}">'
        f'<rect x="0.5" y="0.5" width="{width - 1:.0f}" height="{HEIGHT - 1}" rx="6" '
        f'fill="{TILE}" stroke="{TILE_BORDER}"/>'
        f'<svg x="{PAD}" y="{(HEIGHT - ICON) / 2}" width="{ICON}" height="{ICON}" '
        f'viewBox="{view_box}" fill="{colour}">{inner}</svg>'
        f'<text x="{text_x:.1f}" y="{baseline:.1f}" fill="{LABEL}" '
        f'font-family="Inter,Segoe UI,Helvetica,Arial,sans-serif" font-size="{FONT_SIZE}" '
        f'font-weight="600">{label}</text>'
        f"</svg>"
    )


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for icon_file, label, name in BUTTONS:
        path = OUT / f"{name}.svg"
        path.write_text(button(icon_file, label))
        print("wrote", path.relative_to(ROOT))


if __name__ == "__main__":
    main()
