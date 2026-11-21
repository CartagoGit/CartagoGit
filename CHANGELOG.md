# Changelog

All notable changes to this project are documented here.
The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and the project adheres to [Semantic Versioning](https://semver.org/).

## [1.0.1] - 2026-11-21

### Added

- `AGENTS.md`: branch model (`develop` to work, `main` to publish),
  semantic versioning policy with a patch per publish, release
  checklist and repository conventions for agents and humans.

### Fixed

- The profile banner now lives in `assets/site/` instead of floating
  at the root of `assets/`.

## [1.0.0] - 2026-11-21

First stable release of the profile: the README layout, the asset
pipeline and the repository structure are all settled and documented.

### Added

- `CHANGELOG.md` with semantic versioning and a tagged `v1.0.0`.
- `package.json` declares `"version": "1.0.0"` in sync with the tag.
- Repository layout aligned with what each folder contains:
  - `assets/projects/` — the hand-made or official brand assets of
    each published project (DelendAI, Tanit, QuickModel, Keyer,
    Print CV, Cartago, ReactGpt, Steam Keys, AOE2, PC Fútbol,
    Codember, Codewars).
  - `assets/brand/` — technology logos used across the profile and
    the static site.
  - `assets/generated/` — everything a script builds: `cards/`,
    `buttons/`, `summaries/` and `activity/`.
  - `scripts/assets/` — the generators, named after what they
    produce (`generate-cards.py`, `generate-headers.py`,
    `generate-buttons.py`, `generate-cartago-thumbnail.py`,
    `normalize-brand-icons.py`, `refresh-activity.py`).
  - `scripts/repositories/` — tooling that operates on other
    repositories (`add-mit-license-all-repositories.ts`,
    `audit-workspace.ts`).
  - `docs/` — the curation and maintenance guides.
- npm scripts to run every generator (`assets:cards`,
  `assets:headers`, `assets:buttons`, `assets:activity`).

### Changed

- Every README reference updated to the new layout; zero broken
  asset paths.
- GitHub workflows updated to the new script and asset locations.
- Project logos now come from each project's own brand: ReactGpt
  uses its repository logo, AOE2 and PC Fútbol use their official
  marks, Codember uses its favicon and Codewars its logomark.

### Removed

- 574 legacy generated assets (three dead generations of cards,
  headers and buttons that no README referenced).
- Loose icons at the root of `assets/` (they moved into
  `assets/projects/` or `assets/generated/buttons/`).
- `scripts/__pycache__` from the working tree.
