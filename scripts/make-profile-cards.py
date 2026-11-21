#!/usr/bin/env python3
"""Generate evidence cards and shared action buttons for the profile README.

Featured projects are rendered as full-width HTML table rows so each
project can own multiple real links while the row itself remains inert.
Only evidence metrics still need embedded SVG cards.
"""
import html
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
OUT = ASSETS / "cards"

DARK_TOP = "#13253f"
DARK_BOTTOM = "#0c1727"
DARK_BORDER = "#2b4786"
DARK_TEXT = "#e9f0ff"
DARK_MUTED = "#9fb0ca"
DARK_ACCENT = "#7fb2ff"

LIGHT_TOP = "#ffffff"
LIGHT_BOTTOM = "#e9eef7"
LIGHT_BORDER = "#bfcee6"
LIGHT_TEXT = "#12233f"
LIGHT_MUTED = "#475a7c"
LIGHT_ACCENT = "#1c5ed4"

# Evidence card data: id, title, commits, source, tests, ratio, icon.
EVIDENCE = [
    ("delendai", "DelendAI", "17,519 commits", "638K source", "462K tests", "72%", "assets/delendai.svg"),
    ("tanit", "API Source Tanit", "1,924 commits", "92K source", "78K tests", "85%", "assets/tanit.svg"),
    ("quickmodel", "QuickModel", "550 commits", "49K source", "104K tests", "213%", "assets/quickmodel-rounded.png"),
    ("pcd", "Player Club Dynasty", "294 commits", "37K source", "14K tests", "38%", "assets/brand/godot.svg"),
    ("steam-keys", "Steam Keys", "117 commits", "34K source", "12K tests", "34%", "assets/brand/steam-keys.svg"),
    ("portfolio", "Cartago", "164 commits", "12K source", "1K tests", "9%", "assets/cartago.svg"),
    ("print-cv", "Print CV", "133 commits", "3K source", "230 tests", "8%", "assets/print-cv.svg"),
]


def embedded_asset(path: str, x: int, y: int, size: int) -> str:
    """Embed the complete original image so no nested SVG styles are lost."""
    import base64
    source = ROOT / path
    mime = "image/png" if source.suffix == ".png" else "image/svg+xml"
    data = base64.b64encode(source.read_bytes()).decode("ascii")
    return f'<image href="data:{mime};base64,{data}" x="{x}" y="{y}" width="{size}" height="{size}" preserveAspectRatio="xMidYMid meet"/>'


def evidence_card(name: str, title: str, commits: str, source: str, tests: str, ratio: str, asset: str, light: bool) -> str:
    top, bottom, border, text, muted, accent = (LIGHT_TOP, LIGHT_BOTTOM, LIGHT_BORDER, LIGHT_TEXT, LIGHT_MUTED, LIGHT_ACCENT) if light else (DARK_TOP, DARK_BOTTOM, DARK_BORDER, DARK_TEXT, DARK_MUTED, DARK_ACCENT)
    title = html.escape(title)
    icon = embedded_asset(asset, 14, 15, 38)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="250" height="126" viewBox="0 0 250 126" role="img" aria-label="{title}: {commits}, {source}, {tests}, tests over source {ratio}"><defs><linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/></linearGradient></defs><rect x=".5" y=".5" width="249" height="125" rx="12" fill="url(#tile)" stroke="{border}"/>{icon}<text x="64" y="32" fill="{text}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="16" font-weight="700">{title}</text><text x="64" y="51" fill="{muted}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="11">{commits}</text><line x1="14" y1="64" x2="236" y2="64" stroke="{border}"/><text x="18" y="88" fill="{accent}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="13" font-weight="700">{source}</text><text x="118" y="88" fill="{accent}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="13" font-weight="700">{tests}</text><text x="232" y="88" text-anchor="end" fill="{accent}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="13" font-weight="700">{ratio}</text><text x="18" y="108" fill="{muted}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="10">SOURCE</text><text x="118" y="108" fill="{muted}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="10">TESTS</text><text x="232" y="108" text-anchor="end" fill="{muted}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="10">TESTS/SOURCE</text></svg>'''


def action_button(label: str, icon_path: str, light: bool) -> str:
    background = "#f5f8fd" if light else "#12223a"
    border = "#bfcee6" if light else "#2b4786"
    colour = "#1c5ed4" if light else "#7fb2ff"
    icon = embedded_asset(icon_path, 9, 8, 16)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="112" height="32" viewBox="0 0 112 32"><rect x=".5" y=".5" width="111" height="31" rx="8" fill="{background}" stroke="{border}"/>{icon}<text x="34" y="21" fill="{colour}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="12" font-weight="700">{html.escape(label)}</text></svg>'''


def main() -> None:
    (OUT / "light").mkdir(parents=True, exist_ok=True)
    for e in EVIDENCE:
        (OUT / f"evidence-{e[0]}-v2.svg").write_text(evidence_card(*e, light=False))
        (OUT / "light" / f"evidence-{e[0]}-v2.svg").write_text(evidence_card(*e, light=True))

    for name, label, icon_path in [
        ("open-repository-v2", "Repository", "assets/brand/github.svg"),
        ("open-docker-v2", "Docker Hub", "assets/brand/docker.svg"),
    ]:
        (ASSETS / "btn" / f"{name}.svg").write_text(action_button(label, icon_path, False))
        (ASSETS / "btn" / "light" / f"{name}.svg").write_text(action_button(label, icon_path, True))
    print(f"wrote {len(EVIDENCE)} evidence cards + 2 action buttons (dark + light, v2)")


if __name__ == "__main__":
    main()
