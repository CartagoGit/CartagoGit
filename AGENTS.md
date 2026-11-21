# AGENTS.md

Instructions for AI agents and humans working on this repository.
Keep this file current: an outdated instruction is worse than none.

## What this repository is

The public GitHub profile of Mario Cabrero Volarich (`CartagoGit`).
The `README.md` at the root is rendered on the profile page. Everything
else supports it: generated SVG assets, brand logos, the generators
themselves and the documentation of the decisions taken.

GitHub renders the README without JavaScript and strips `style` on
most elements. Layout is built from fixed-size SVG assets and inline
image flow. Nothing here relies on custom CSS.

## Layout

```
assets/
  projects/    hand-made or official brand assets, one per project
  brand/       technology logos (colour lives inside each file)
  site/        static imagery of the profile itself (banner)
  generated/   script output: cards/, buttons/, summaries/, activity/
scripts/
  assets/      generators, named after what they produce
  repositories/ tooling that operates on other repositories
docs/          curation and maintenance decisions
CHANGELOG.md   notable changes, one entry per release
```

`assets/generated/` is fully reproducible. Never hand-edit a file in
it: change the generator in `scripts/assets/` and re-run it. The
hand-made folders (`assets/projects/`, `assets/brand/`, `assets/site/`)
are the only places with authored files.

## Commands

```bash
bun run assets:cards      # regenerate project/evidence/docker cards
bun run assets:headers    # regenerate section title bars
bun run assets:buttons    # regenerate the legacy button tiles
bun run assets:activity   # refetch and bake the activity charts
bun run typecheck         # tsc --noEmit
```

After regenerating, verify the README still resolves every asset:

```bash
python3 - <<'PY'
from pathlib import Path
import re
s = Path('README.md').read_text()
missing = [r for r in re.findall(r'(?:src|srcset)="([^"]+)"', s)
           if r.startswith('./') and not Path(r[2:]).exists()]
print(sorted(set(missing)))
PY
```

## Branching model

- `develop` — the working branch. Every change lands here first.
- `main` — the release branch. It is what the world sees, because the
  profile renders from `main`. Merge into it only to publish.
- Branches per topic off `develop` when the change is not trivial:
  `feat/<topic>`, `fix/<topic>`.

Flow:

1. Branch off `develop` (or work directly on `develop` for small fixes).
2. Validate locally: regenerate assets if touched, zero missing
   references, `bun run typecheck` green.
3. Merge or push to `develop`.
4. To publish: merge `develop` into `main`, bump the version, update
   `CHANGELOG.md`, tag, push `main` and the tag.

## Versioning and releases

Semantic versioning. Every publish to `main` produces exactly one
version and one tag.

- **patch** (1.0.x) — visual fixes, asset tweaks, copy corrections,
  documentation updates. This is the everyday release: if it changes
  how the profile looks or reads, it ships as a patch.
- **minor** (1.x.0) — a new section, a new capability in the
  generators, a structural addition to the layout.
- **major** (x.0.0) — a different identity or a breaking change in the
  asset pipeline (paths agents depend on, generator interfaces).

Release checklist (do it in one commit on `main`):

1. Merge `develop` into `main` (fast-forward preferred).
2. Bump `"version"` in `package.json`.
3. Add the entry at the top of `CHANGELOG.md` with the new version and
   today's date, describing what the release contains.
4. Verify: every README asset resolves, sections and Core stack
   categories are all present, no `<table>`, typecheck green.
5. Commit `chore(release): vX.Y.Z`, tag `vX.Y.Z` (annotated), push
   `main` and the tag together.
6. Open the render at github.com/CartagoGit and check it in desktop
   and mobile widths: zero broken images, no horizontal overflow.

## Assets and cache

GitHub proxies images and caches aggressively by URL. When the content
of a generated SVG changes, its filename must change too: bump the
version suffix in the generator (`project-*-v6.svg` → `v7`) and update
the README. Never edit an asset in place expecting GitHub to refresh.

Generated files embed their source logos as data URIs, so cards stay
self-contained. If a source logo changes, regenerate the cards that
use it and bump their version suffix.

## Conventions

- English copy in the README; the docs may be Spanish.
- No HTML tables in the README: GitHub renders them unpredictably on
  narrow screens. Cards and inline image flow instead.
- Every interactive icon that carries no label gets `title` and
  `aria-label`/`alt` describing the destination.
- Sections keep this order: intro → Featured Projects → Docker images
  → Professional experience → Beyond the front-end → How I work →
  GitHub Activity → Evidence → Core stack → More projects.
- The five Core stack categories (Front-end, Services/data/runtime,
  Tooling & AI infrastructure, Quality & delivery, With AI) are
  content, not layout: never drop one to fix a layout problem.
- The portfolio site (`CartagoGit.github.io`) is a separate repository.
  Nothing here should reach into it.
