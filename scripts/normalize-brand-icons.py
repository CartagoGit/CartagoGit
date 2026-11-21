#!/usr/bin/env python3
"""Give every brand icon its own colour.

Simple Icons ship without a fill, so the browser paints them black and the
CSS has to force them white for a dark background — which is why they all
looked identical, and why they disappeared on a light one.

Here the colour is written into the file itself, on the root `<svg>`, and
the per-path fills are removed so every path inherits it. The icon then
carries its brand colour wherever it is used.

    python3 scripts/normalize-brand-icons.py <folder> [<folder> ...]
"""
import json
import pathlib
import re
import sys

# The colour each brand uses. Where the official colour is too dark to read
# on the navy tile the icons sit on, the lighter variant is used instead.
COLORS = {
    # front-end
    "angular": "#dd0031",
    "sass": "#cc6699",
    "ionic": "#3880ff",
    "typescript": "#3178c6",
    "rxjs": "#b7178c",
    "capacitor": "#119eff",
    "tailwindcss": "#06b6d4",
    "vue": "#41b883",
    "react": "#61dafb",
    # services and data
    "nestjs": "#e0234e",
    "bun": "#fbf1e1",
    "nodejs": "#5fa04e",
    "postgresql": "#4169e1",
    "sqlite": "#44a2de",
    "mongodb": "#47a248",
    "zod": "#3e67b1",
    "openapi": "#6ba539",
    # tooling
    "model-context-protocol": "#ffffff",
    "tauri": "#ffc131",
    "rust": "#dea584",
    "godot": "#478cbf",
    "python": "#3776ab",
    "storybook": "#ff4785",
    "prime-ng": "#dd0031",
    # quality and delivery
    "vitest": "#8dc63f",
    "playwright": "#2ead33",
    "eslint": "#4b32c3",
    "prettier": "#f7b93e",
    "docker": "#2496ed",
    "gitlab": "#fc6d26",
    "github-actions": "#2088ff",
    "linux": "#fcc624",
    # AI
    "claude": "#d97757",
    "openai": "#ffffff",
    "minimax": "#ff6b35",
    "grok": "#ffffff",
    # destinations
    "github": "#ffffff",
    "linkedin": "#4a9ee8",
    "npm": "#cb3837",
    # generic glyphs: they are not brands, so they take the accent
    "docs": "#7fb2ff",
    "live": "#7fb2ff",
    "package": "#7fb2ff",
    "releases": "#7fb2ff",
    "launch": "#7fb2ff",
    "mods": "#7fb2ff",
}

# Icons that are a whole picture and must not be recoloured: they carry their
# own background and their own shape.
SKIP = {"steam-keys"}


def normalise(path: pathlib.Path, colour: str) -> None:
    raw = path.read_text()

    match = re.search(r"<svg[^>]*>", raw)
    if match is None:
        return
    tag = re.sub(r'\sfill="[^"]*"', "", match.group(0))
    tag = tag[:-1] + f' fill="{colour}">'

    head = tag
    body = raw[match.end():]

    # Path and shape fills would win over the root one.
    body = re.sub(r'\sfill="[^"]*"', "", body)
    body = re.sub(r'\sstroke="[^"]*"', "", body)

    # A `currentColor` left behind would resolve to black inside an <img>.
    body = body.replace("currentColor", colour)

    path.write_text(head + body)


def main():
    folders = [pathlib.Path(f) for f in sys.argv[1:]]
    if not folders:
        folders = [pathlib.Path("assets/brand")]

    report = {}
    for folder in folders:
        for svg in sorted(folder.glob("*.svg")):
            name = svg.stem
            if name in SKIP:
                continue
            colour = COLORS.get(name)
            if colour is None:
                report[name] = "no colour, left as it was"
                continue
            normalise(svg, colour)
            report[name] = colour

    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
