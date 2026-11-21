#!/usr/bin/env python3
"""Generate responsive, linked profile cards for project and evidence grids.

Each card is a fixed-width SVG wrapped by an HTML link in README.md.
Inline images naturally wrap: three columns on desktop, one on phones.
Unlike tables, they never need horizontal scrolling.
"""
import html
import pathlib
import re
import textwrap

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

PROJECTS = [
    ("delendai", "DelendAI", "Extensible MCP server core", "62 isolated plugins · CLI · 18 CI gates", "assets/delendai.svg"),
    ("tanit", "API Source Tanit", "Static API discovery", "25 frameworks · 7 import/export formats", "assets/tanit.svg"),
    ("quickmodel", "QuickModel", "TypeScript serialization", "Validation adapters · benchmarks · MCP", "assets/quickmodel-rounded.png"),
    ("keyer", "Keyer", "Published secrets CLI", "Encrypts keys and .env files · npm", "assets/keyer.svg"),
    ("print-cv", "Print CV", "Print-ready CV application", "Vue 3 · i18n · real-paper layout", "assets/print-cv.svg"),
    ("cartago", "Cartago", "The site behind this profile", "Angular SSR · tests · bilingual · themed", "assets/cartago.svg"),
]

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


def project_card(name: str, title: str, subtitle: str, detail: str, asset: str, light: bool) -> str:
    palette = (LIGHT_TOP, LIGHT_BOTTOM, LIGHT_BORDER, LIGHT_TEXT, LIGHT_MUTED, LIGHT_ACCENT) if light else (DARK_TOP, DARK_BOTTOM, DARK_BORDER, DARK_TEXT, DARK_MUTED, DARK_ACCENT)
    top, bottom, border, text, muted, accent = palette
    safe_title, safe_subtitle, safe_detail = map(html.escape, (title, subtitle, detail))
    icon = embedded_asset(asset, 18, 16, 54)
    github = embedded_asset("assets/brand/github.svg", 31, 139, 14)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="250" height="176" viewBox="0 0 250 176" role="img" aria-label="{safe_title}: {safe_subtitle}. Opens GitHub repository."><defs><linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/></linearGradient></defs><rect x=".5" y=".5" width="249" height="175" rx="12" fill="url(#tile)" stroke="{border}"/>{icon}<text x="86" y="37" fill="{text}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="17" font-weight="700">{safe_title}</text><text x="86" y="57" fill="{accent}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="11.5" font-weight="600">{safe_subtitle}</text><line x1="18" y1="83" x2="232" y2="83" stroke="{border}"/><text x="20" y="106" fill="{muted}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="11">{safe_detail}</text><rect x="20" y="131" width="118" height="27" rx="8" fill="{accent}" fill-opacity=".16"/>{github}<text x="52" y="149" fill="{accent}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="11" font-weight="700">Repository</text><text x="231" y="150" text-anchor="end" fill="{accent}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="18" font-weight="700">↗</text></svg>'''


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
    for p in PROJECTS:
        (OUT / f"project-{p[0]}-v2.svg").write_text(project_card(*p, light=False))
        (OUT / "light" / f"project-{p[0]}-v2.svg").write_text(project_card(*p, light=True))
    for e in EVIDENCE:
        (OUT / f"evidence-{e[0]}-v2.svg").write_text(evidence_card(*e, light=False))
        (OUT / "light" / f"evidence-{e[0]}-v2.svg").write_text(evidence_card(*e, light=True))

    for name, label, icon_path in [
        ("open-repository-v2", "Repository", "assets/brand/github.svg"),
        ("open-docker-v2", "Docker Hub", "assets/brand/docker.svg"),
    ]:
        (ASSETS / "btn" / f"{name}.svg").write_text(action_button(label, icon_path, False))
        (ASSETS / "btn" / "light" / f"{name}.svg").write_text(action_button(label, icon_path, True))
    print(f"wrote {len(PROJECTS)} project cards + {len(EVIDENCE)} evidence cards + 2 action buttons (dark + light, v2)")


if __name__ == "__main__":
    main()
