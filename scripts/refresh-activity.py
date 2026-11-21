#!/usr/bin/env python3
"""Fetch the activity charts for the README and make them static.

The chart services emit SVGs whose text starts at opacity 0 and fades in
with a CSS animation. Inside a README <img> some renderers never run the
animation, so the chart reads blank. Here the animation is baked to its
final state: opacity 1, final font size, no keyframes.

Both themes are fetched, with rounded corners matching the portfolio's
radius, and stored under assets/activity/ so the README does not depend
on a third-party service being up when someone opens the profile.

    python3 scripts/refresh-activity.py
"""
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "activity"

USER = "CartagoGit"
RADIUS = 12

CHARTS = {
    "streak-dark": (
        "https://streak-stats.demolab.com"
        f"?user={USER}&theme=github-dark-blue&hide_border=true&border_radius={RADIUS}"
        "&background=0E1A2B"
    ),
    "streak-light": (
        "https://streak-stats.demolab.com"
        f"?user={USER}&theme=default&hide_border=true&border_radius={RADIUS}"
        "&background=F2F5FB"
    ),
    "graph-dark": (
        "https://github-readme-activity-graph.vercel.app/graph"
        f"?username={USER}&theme=github-dark&hide_border=true&radius={RADIUS}"
        "&bg_color=0E1A2B&color=7FB2FF&line=4D8DFF&point=C3D1D9&area_color=1B2D59"
    ),
    "graph-light": (
        "https://github-readme-activity-graph.vercel.app/graph"
        f"?username={USER}&theme=github-light&hide_border=true&radius={RADIUS}"
        "&bg_color=F2F5FB&color=1C5ED4&line=4D8DFF&point=475A7C&area_color=DBE3F1"
    ),
    "stats-dark": (
        "https://github-readme-stats-fast.vercel.app/api"
        f"?username={USER}&show_icons=true&theme=github_dark&hide_border=true"
        f"&include_all_commits=true&count_private=true&border_radius={RADIUS}"
        "&bg_color=0E1A2B&title_color=7FB2FF&text_color=C3D1D9&icon_color=7FB2FF"
    ),
    "stats-light": (
        "https://github-readme-stats-fast.vercel.app/api"
        f"?username={USER}&show_icons=true&theme=default&hide_border=true"
        f"&include_all_commits=true&count_private=true&border_radius={RADIUS}"
        "&bg_color=F2F5FB&title_color=1C5ED4&text_color=475A7C&icon_color=1C5ED4"
    ),
    "langs-dark": (
        "https://github-readme-stats-fast.vercel.app/api/top-langs/"
        f"?username={USER}&layout=compact&theme=github_dark&hide_border=true"
        f"&border_radius={RADIUS}&langs_count=8"
        "&bg_color=0E1A2B&title_color=7FB2FF&text_color=C3D1D9"
    ),
    "langs-light": (
        "https://github-readme-stats-fast.vercel.app/api/top-langs/"
        f"?username={USER}&layout=compact&theme=default&hide_border=true"
        f"&border_radius={RADIUS}&langs_count=8"
        "&bg_color=F2F5FB&title_color=1C5ED4&text_color=475A7C"
    ),
}


def _keyframe_blocks(css: str) -> list[tuple[str, str, int, int]]:
    """Find @keyframes blocks by counting braces, not by guessing indentation."""
    blocks = []
    for match in re.finditer(r"@keyframes\s+([\w-]+)\s*\{", css):
        depth = 1
        i = match.end()
        while i < len(css) and depth:
            if css[i] == "{":
                depth += 1
            elif css[i] == "}":
                depth -= 1
            i += 1
        blocks.append((match.group(1), css[match.end():i - 1], match.start(), i))
    return blocks


def _final_states(css: str) -> dict[str, dict[str, str]]:
    """Read each @keyframes block and keep the declarations of its last frame.

    Removing an animation is not enough: the property it animated stays at
    the *initial* value, which is usually the hidden one. The contribution
    line, for instance, sits at stroke-dashoffset: 5000 until `dash` brings
    it to 0 — strip the animation and the line disappears, leaving only the
    dots. The rank letter is drawn at translate(-5px, 5px) by its keyframes,
    so without them it sits off-centre inside its circle.
    """
    states: dict[str, dict[str, str]] = {}
    for name, body, _start, _end in _keyframe_blocks(css):
        frames = re.findall(r"(?:from|to|\d+%)\s*\{([^{}]*)\}", body)
        if not frames:
            continue
        decls = {}
        for decl in frames[-1].split(";"):
            if ":" in decl:
                prop, value = decl.split(":", 1)
                decls[prop.strip()] = value.strip()
        states[name] = decls
    return states


def bake(svg: str) -> str:
    """Freeze every animation at the state it ends in."""
    style_match = re.search(r"<style>(.*?)</style>", svg, re.S)
    css = style_match.group(1) if style_match else ""
    finals = _final_states(css)

    def settle(body: str) -> str:
        """Apply the final frame of every animation the rule declares."""
        for name in re.findall(r"animation:\s*([\w-]+)", body):
            for prop, value in finals.get(name, {}).items():
                if re.search(rf"{re.escape(prop)}\s*:", body):
                    body = re.sub(
                        rf"{re.escape(prop)}\s*:[^;}}]*", f"{prop}: {value}", body
                    )
                else:
                    body = body.rstrip().rstrip(";") + f"; {prop}: {value};"
        body = re.sub(r"animation:[^;}]*;?", "", body)
        body = re.sub(r"animation-delay:[^;}]*;?", "", body)
        body = re.sub(r"opacity:\s*0(?:\.\d+)?\s*;?", "opacity: 1;", body)
        return body

    # Drop the keyframes: they only describe the entrance.
    for _name, _body, start, end in reversed(_keyframe_blocks(svg)):
        svg = svg[:start] + svg[end:]

    # Class rules also hide elements until the animation runs
    # (.stagger { opacity: 0; animation: ... }). Bake those too.
    def rule_fix(match: re.Match) -> str:
        return "{" + settle(match.group(1)) + "}"

    svg = re.sub(r"\{([^{}]*)\}", rule_fix, svg)

    # Any inline style that hides the element until the animation runs is
    # replaced by the state the animation ends in.
    def style_fix(match: re.Match) -> str:
        style = match.group(1)
        style = re.sub(r"animation:[^;'\"]*;?", "", style)
        style = re.sub(r"animation-delay:[^;'\"]*;?", "", style)
        style = re.sub(r"opacity:\s*0(?:\.\d+)?", "opacity: 1", style)
        # The streak's big number animates its font size up to 28px.
        if "currstreak" in match.group(0):
            style = re.sub(r"font-size:\s*[\d.]+px", "font-size: 28px", style)
        return f"style='{style.strip()}'"

    svg = re.sub(r"style='([^']*)'", style_fix, svg)
    svg = re.sub(r'style="([^"]*)"', lambda m: style_fix(m).replace("'", '"'), svg)
    return svg


def fetch(url: str) -> str:
    out = subprocess.run(
        ["curl", "-sfL", "--max-time", "60", url],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        raise SystemExit(f"fetch failed for {url}: {out.stderr[:200]}")
    return out.stdout


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for name, url in CHARTS.items():
        svg = fetch(url)
        if "<svg" not in svg:
            raise SystemExit(f"{name}: service did not return an SVG")
        path = OUT / f"{name}.svg"
        path.write_text(bake(svg))
        print(f"wrote {path.relative_to(ROOT)} ({len(svg)} bytes)")


if __name__ == "__main__":
    main()
