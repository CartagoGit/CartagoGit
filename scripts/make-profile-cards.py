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
    ("aoe2", "Aoe2 mods", "1,123 commits", "32K source", "7K tests", "23%", "assets/brand/mods.svg"),
    ("portfolio", "Cartago", "164 commits", "12K source", "1K tests", "9%", "assets/cartago.svg"),
    ("print-cv", "Print CV", "133 commits", "3K source", "230 tests", "8%", "assets/print-cv.svg"),
]

PROJECTS = [
    ("delendai", "DelendAI", "Extensible MCP server core", "62 plugins · CLI · 18 CI gates", "assets/delendai.svg"),
    ("tanit", "API Source Tanit", "Static API discovery", "25 frameworks · 7 formats", "assets/tanit.svg"),
    ("quickmodel", "QuickModel", "TypeScript serialization", "Validation · benchmarks · MCP", "assets/quickmodel-rounded.png"),
    ("keyer", "Keyer", "Published secrets CLI", "Encrypts keys and .env files", "assets/keyer.svg"),
    ("print-cv", "Print CV", "Print-ready CV application", "Vue 3 · i18n · print layout", "assets/print-cv.svg"),
    ("cartago", "Cartago", "The site behind this profile", "Angular SSR · tests · bilingual", "assets/cartago.svg"),
]

MORE_PROJECTS = [
    ("nestgpt", "NestGpt", "AI-enabled NestJS API", "DTOs · uploads · streaming · Docker", "assets/brand/nestjs.svg"),
    ("reactgpt", "ReactGpt", "React front-end", "Client for the NestJS AI API", "assets/brand/react.svg"),
    ("zoneless", "Zoneless Angular", "Angular without zone.js", "Unit and integration tests", "assets/brand/angular.svg"),
    ("aoe2", "Aoe2 mods", "Game modding tools", "Binary formats · localisation · automation", "assets/brand/mods.svg"),
    ("pcfutbol", "PC Fútbol 6 mods", "Game content pipeline", "Schemas · assets · automation", "assets/brand/mods.svg"),
    ("pcd", "Player Club Dynasty", "Godot/C# football manager", "Proposal → implement → review", "assets/brand/godot.svg"),
    ("steam-keys", "Steam Keys", "Local-first desktop app", "Tauri 2 · Rust · SQLite", "assets/brand/steam-keys.svg"),
    ("template-angular", "Angular template", "Workspace starter", "Architecture ready for new apps", "assets/brand/angular.svg"),
    ("codember", "Codember", "Daily puzzle solutions", "Consistent small challenges", "assets/brand/typescript.svg"),
    ("codewars", "Codewars", "Practice repository", "Focused katas and one solution per commit", "assets/brand/typescript.svg"),
]

DOCKER_IMAGES = [
    ("nodebun", "nodebun", "Node.js + Bun + fnm", "Pinned multi-runtime environment"),
    ("zsh", "zsh", "Batteries-included shell", "Daily CLI environment"),
    ("ionic", "ionic-cover", "Ionic build environment", "Angular + Capacitor tooling"),
    ("nestjs", "nestjs-cover", "NestJS build environment", "Typed services and CI"),
    ("angular", "angular", "Angular build environment", "Reproducible front-end delivery"),
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


def project_card(name: str, title: str, subtitle: str, detail: str, asset: str, light: bool, width: int) -> str:
    top, bottom, border, text, muted, accent = (LIGHT_TOP, LIGHT_BOTTOM, LIGHT_BORDER, LIGHT_TEXT, LIGHT_MUTED, LIGHT_ACCENT) if light else (DARK_TOP, DARK_BOTTOM, DARK_BORDER, DARK_TEXT, DARK_MUTED, DARK_ACCENT)
    title, subtitle, detail = map(html.escape, (title, subtitle, detail))
    compact = width < 280
    icon_size = 40 if compact else 54
    icon_x = 12
    text_x = 60 if compact else 84
    icon = embedded_asset(asset, icon_x, 16, icon_size)
    title_size = 13 if compact else 18
    subtitle_size = 9.5 if compact else 12
    detail_size = 9.5 if compact else 11.5
    height = 124
    body = f'M12 .5H{width-1}V{height-0.5}H12Q.5 {height-0.5} .5 12V12Q.5 .5 12 .5Z'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{title}: {subtitle}"><defs><linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/></linearGradient></defs><path d="{body}" fill="url(#tile)" stroke="{border}"/>{icon}<text x="{text_x}" y="37" fill="{text}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="{title_size}" font-weight="700">{title}</text><text x="{text_x}" y="58" fill="{accent}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="{subtitle_size}" font-weight="600">{subtitle}</text><line x1="16" y1="82" x2="{width-1}" y2="82" stroke="{border}"/><text x="18" y="105" fill="{muted}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="{detail_size}">{detail}</text></svg>'''


def compact_card(title: str, subtitle: str, detail: str, asset: str, light: bool, width: int) -> str:
    top, bottom, border, text, muted, accent = (LIGHT_TOP, LIGHT_BOTTOM, LIGHT_BORDER, LIGHT_TEXT, LIGHT_MUTED, LIGHT_ACCENT) if light else (DARK_TOP, DARK_BOTTOM, DARK_BORDER, DARK_TEXT, DARK_MUTED, DARK_ACCENT)
    title, subtitle, detail = map(html.escape, (title, subtitle, detail))
    compact = width < 240
    icon_size = 34 if compact else 42
    text_x = 55 if compact else 68
    icon = embedded_asset(asset, 12, 12, icon_size)
    height = 92
    title_size = 12.5 if compact else 15
    subtitle_size = 9.5 if compact else 11.5
    body = f'M10 .5H{width-1}V{height-0.5}H10Q.5 {height-0.5} .5 10V10Q.5 .5 10 .5Z'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{title}: {subtitle}"><defs><linearGradient id="tile" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/></linearGradient></defs><path d="{body}" fill="url(#tile)" stroke="{border}"/>{icon}<text x="{text_x}" y="30" fill="{text}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="{title_size}" font-weight="700">{title}</text><text x="{text_x}" y="49" fill="{accent}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="{subtitle_size}" font-weight="600">{subtitle}</text><line x1="14" y1="64" x2="{width-1}" y2="64" stroke="{border}"/><text x="16" y="82" fill="{muted}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="10">{detail}</text></svg>'''


def docker_card(title: str, subtitle: str, detail: str, light: bool, width: int) -> str:
    return compact_card(title, subtitle, detail, "assets/brand/docker.svg", light, width)


def evidence_focus_card(title: str, subtitle: str, detail: str, asset: str, light: bool, width: int) -> str:
    return compact_card(title, subtitle, detail, asset, light, width)


def action_button(label: str, icon_path: str, light: bool) -> str:
    background = "#f5f8fd" if light else "#12223a"
    border = "#bfcee6" if light else "#2b4786"
    colour = "#1c5ed4" if light else "#7fb2ff"
    icon = embedded_asset(icon_path, 9, 8, 16)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="112" height="32" viewBox="0 0 112 32"><rect x=".5" y=".5" width="111" height="31" rx="8" fill="{background}" stroke="{border}"/>{icon}<text x="34" y="21" fill="{colour}" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="12" font-weight="700">{html.escape(label)}</text></svg>'''


def action_dock(icon_path: str, light: bool, height: int) -> str:
    top, bottom, border = (LIGHT_TOP, LIGHT_BOTTOM, LIGHT_BORDER) if light else (DARK_TOP, DARK_BOTTOM, DARK_BORDER)
    colour = LIGHT_ACCENT if light else DARK_ACCENT
    icon = embedded_asset(icon_path, 8, (height - 18) // 2, 18)
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="34" height="{height}" viewBox="0 0 34 {height}" role="img"><rect x="0" y=".5" width="34" height="{height-1}" fill="{bottom}" stroke="{border}"/><line x1="0" y1="1" x2="0" y2="{height-1}" stroke="{colour}" opacity=".35"/>{icon}</svg>'''


def card_cap(light: bool, height: int) -> str:
    bottom, border = (LIGHT_BOTTOM, LIGHT_BORDER) if light else (DARK_BOTTOM, DARK_BORDER)
    radius = 11 if height > 100 else 9
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="6" height="{height}" viewBox="0 0 6 {height}" aria-hidden="true"><path d="M0 .5H{6-radius}Q5.5 .5 5.5 {radius}V{height-radius}Q5.5 {height-.5} {6-radius} {height-.5}H0Z" fill="{bottom}" stroke="{border}"/></svg>'''


def main() -> None:
    for prefix, total_width, action_count in [("", 390, 2), ("mid/", 350, 2), ("narrow/", 293, 2), ("tiny/", 223, 2)]:
        out = OUT / prefix if prefix else OUT
        (out / "light").mkdir(parents=True, exist_ok=True)
        body_width = total_width - action_count * 34 - 6
        for p in PROJECTS:
            (out / f"project-{p[0]}-v4.svg").write_text(project_card(*p, light=False, width=body_width))
            (out / "light" / f"project-{p[0]}-v4.svg").write_text(project_card(*p, light=True, width=body_width))
        compact_width = total_width - 34 - 6
        for card in MORE_PROJECTS:
            name, title, subtitle, detail, asset = card
            (out / f"more-{name}-v2.svg").write_text(compact_card(title, subtitle, detail, asset, False, compact_width))
            (out / "light" / f"more-{name}-v2.svg").write_text(compact_card(title, subtitle, detail, asset, True, compact_width))
        for card in DOCKER_IMAGES:
            name, title, subtitle, detail = card
            (out / f"docker-{name}-v2.svg").write_text(docker_card(title, subtitle, detail, False, compact_width))
            (out / "light" / f"docker-{name}-v2.svg").write_text(docker_card(title, subtitle, detail, True, compact_width))
    for e in EVIDENCE:
        (OUT / f"evidence-{e[0]}-v3.svg").write_text(evidence_card(*e, light=False))
        (OUT / "light" / f"evidence-{e[0]}-v3.svg").write_text(evidence_card(*e, light=True))
    dock_icons = {
        "repository": "assets/brand/github.svg",
        "releases": "assets/brand/releases.svg",
        "docs": "assets/brand/docs.svg",
        "npm": "assets/brand/npm.svg",
        "live": "assets/brand/live.svg",
        "docker": "assets/brand/docker.svg",
    }
    for name, icon_path in dock_icons.items():
        for height, suffix in [(124, "project"), (92, "compact")]:
            (ASSETS / "btn" / f"{name}-{suffix}-dock-v4.svg").write_text(action_dock(icon_path, False, height))
            (ASSETS / "btn" / "light" / f"{name}-{suffix}-dock-v4.svg").write_text(action_dock(icon_path, True, height))
    for height, suffix in [(124, "project"), (92, "compact")]:
        (ASSETS / "btn" / f"card-cap-{suffix}-v4.svg").write_text(card_cap(False, height))
        (ASSETS / "btn" / "light" / f"card-cap-{suffix}-v4.svg").write_text(card_cap(True, height))
    for name, label, icon_path in [
        ("open-repository-v2", "Repository", "assets/brand/github.svg"),
        ("open-docker-v2", "Docker Hub", "assets/brand/docker.svg"),
    ]:
        (ASSETS / "btn" / f"{name}.svg").write_text(action_button(label, icon_path, False))
        (ASSETS / "btn" / "light" / f"{name}.svg").write_text(action_button(label, icon_path, True))
    print(f"wrote {len(PROJECTS)} featured, {len(MORE_PROJECTS)} more, {len(DOCKER_IMAGES)} docker and {len(EVIDENCE)} measured evidence cards")


if __name__ == "__main__":
    main()
