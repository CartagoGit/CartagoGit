<p align="center">
  <img src="./assets/banner-03-neon.png" alt="Mario Cabrero Volarich" width="100%">
</p>

<h1 align="center">Mario Cabrero Volarich</h1>

<p align="center">
  <strong>Full-stack TypeScript engineer building developer tooling, AI infrastructure and product software.</strong><br>
  <sub>Angular · Vue · React · NestJS · Bun · Rust/Tauri · Godot · Docker</sub>
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/mario-cabrero-volarich"><img src="./assets/linkedin-profile-badge.svg" alt="LinkedIn profile" height="28"></a>
  <a href="https://www.npmjs.com/~cartago-git"><img src="https://img.shields.io/badge/npm-%40cartago--git-CB3837?style=flat-square&logo=npm&logoColor=white" alt="npm packages" height="28"></a>
  <a href="https://hub.docker.com/u/cartagodocker"><img src="https://img.shields.io/badge/Docker%20Hub-%E2%86%97-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker Hub images" height="28"></a>
  <a href="https://github.com/CartagoGit?tab=repositories"><img src="https://img.shields.io/badge/GitHub-%E2%86%97-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub repositories" height="28"></a>
</p>

---

## How to read this profile

The products I build move fast and get renamed as they mature — a repository name is today's
label, not the point. So this page describes my work **by the capability it proves**, and links
to the repository that carries it. If a project changes name tomorrow, the capability still stands
and only the link changes.

Everything below is **independent work**: repositories, libraries, images and experiments built
in my own time. My professional work is not published here.

---

## What I work on

| Capability | What it means in practice | Where the evidence is |
| --- | --- | --- |
| **AI infrastructure & developer tooling** | An MCP runtime with a lazily-loaded plugin surface, hermetic execution, typed public errors, a CLI-first workflow and a proposal-driven release process. | [MCP runtime core](https://github.com/CartagoGit/DelendAI) · [Model serialization library](https://github.com/CartagoGit/quickmodel) · [Secret manager CLI](https://github.com/CartagoGit/Keyer) |
| **Static analysis & developer experience** | Recovering an API from source code — no server, no annotations — across 25 frameworks, exported to Postman, Bruno, Insomnia, HAR, OpenAPI or cURL. | [API discovery engine](https://github.com/CartagoGit/api-source-tanit) |
| **Product engineering** | Full-stack delivery with Angular (zoneless SSR), Vue and React on the front, NestJS and Bun on the back, with unit, integration and end-to-end coverage. | [Angular SSR site](https://github.com/CartagoGit/portfolio) · [Vue CV application](https://github.com/CartagoGit/print-cv) · [NestJS AI API](https://github.com/CartagoGit/NestGpt) |
| **Desktop, game & content engineering** | Local-first desktop apps (Tauri 2 + Rust + SQLite), games in Godot/C#, and schema-validated content pipelines with localisation. | [Local-first desktop manager](https://github.com/CartagoGit/steam-keys) · [Game content pipeline](https://github.com/CartagoGit/aoe2-mods) · [AI-assisted game delivery](https://github.com/CartagoGit/player-club-dynasty) |
| **Infrastructure & delivery** | Bun-first workspaces, reproducible Docker images, CI quality gates, and releases driven by machine-checked proposals. | [Docker images](#docker-images) · [Angular workspace template](https://github.com/CartagoGit/template-angular) |

---

## Featured work

#### 🧩 MCP runtime core — extensible server core and CLI plugin loader

A project-agnostic core for building MCP servers, and the plugin loader that feeds them.
Tools are named capabilities resolved at runtime; the surface is lazy, the errors are public and
the data stays private. Around it sits a full delivery pipeline: proposals, worktrees, agent
locks, coverage ratchets and release gates.

[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![Bun](https://img.shields.io/badge/runtime-Bun-000000?style=flat-square&logo=bun&logoColor=F9F1E1)](https://bun.sh)
[![MCP](https://img.shields.io/badge/Model%20Context%20Protocol-111111?style=flat-square&logo=modelcontextprotocol&logoColor=white)](https://modelcontextprotocol.io)
[![License](https://img.shields.io/badge/license-BSD--3--Clause-blue.svg)](https://github.com/CartagoGit/DelendAI/blob/develop/LICENSE)

[![Repository](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/DelendAI)

---

#### 🔎 API discovery engine — recover an API from source code

Points at a project directory and produces a ready-to-import API description. The framework is
detected from the code itself, request bodies are recovered from validation schemas, and the
result is exported to the tools teams already use. Ships as CLI, desktop builds for Linux, macOS
and Windows, and containers.

[![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)
[![OpenAPI](https://img.shields.io/badge/OpenAPI-6BA539?style=flat-square&logo=openapi&logoColor=white)](https://swagger.io/specification/)
[![MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/CartagoGit/api-source-tanit/blob/main/LICENSE)

[![Repository](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/api-source-tanit)

---

#### 🧱 Model serialization library — typed models, SOLID architecture

Automatic type transformation, validation adapters, security tests and benchmarks, published as a
library with an MCP server on top so it can be used from an editor or an agent. The test suite is
larger than the source on purpose.

[![npm](https://img.shields.io/badge/npm-v1.0.0-CB3837?style=flat-square&logo=npm&logoColor=white)](https://www.npmjs.com/package/quickmodel)
[![TypeScript](https://img.shields.io/badge/TypeScript-3.4+-3178C6?style=flat-square&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)

[![Repository](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/quickmodel)

---

#### 🖥️ Local-first desktop manager — game keys that never leave the machine

A Tauri 2 desktop application (Rust + React + SQLite) to keep, organise and audit game keys.
No accounts, no cloud, no telemetry: the database and the exports live next to the executable,
and the repository never contains a real key.

[![Tauri](https://img.shields.io/badge/Tauri-2-FFC131?style=flat-square&logo=tauri&logoColor=black)](https://tauri.app)
[![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)](https://www.rust-lang.org)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org)

[![Repository](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/steam-keys)

---

## Evidence

Measured on the repositories linked above — source lines exclude tests, fixtures and generated
files; test lines are the test suites themselves.

| Repository | Commits | Source lines | Test lines | Test files | Packages |
| --- | ---: | ---: | ---: | ---: | ---: |
| [MCP runtime core](https://github.com/CartagoGit/DelendAI) | 17,484 | 628,712 | 460,854 | 2,709 | 84 |
| [API discovery engine](https://github.com/CartagoGit/api-source-tanit) | 1,876 | 99,398 | 73,489 | 362 | 53 |
| [Model serialization library](https://github.com/CartagoGit/quickmodel) | 550 | 58,636 | 100,258 | 407 | 1 |
| [AI-assisted game delivery](https://github.com/CartagoGit/player-club-dynasty) | 294 | 36,041 | 13,628 | 9 | 2 |
| [Local-first desktop manager](https://github.com/CartagoGit/steam-keys) | 117 | 33,518 | 11,462 | 50 | 2 |
| [Game content pipeline](https://github.com/CartagoGit/aoe2-mods) | 1,123 | 31,838 | 7,382 | 19 | 1 |
| [Angular SSR site](https://github.com/CartagoGit/portfolio) | 162 | 6,352 | 1,047 | 21 | 2 |
| [Vue CV application](https://github.com/CartagoGit/print-cv) | 132 | 2,179 | 230 | 7 | 1 |

---

## How I work

- **Proposals before code.** Every non-trivial change starts as a written proposal with a goal,
  a design, slices, an acceptance criteria and a risk section. Nothing lands without a machine
  checkable acceptance test.
- **Tests as a ratchet.** Coverage thresholds only ever move upwards, and the script that enforces
  it fails the build when they slip.
- **Quality gates, not opinions.** Lint, typecheck, tests, generated-file drift, catalogue
  consistency and i18n parity run in CI — 18 workflows in the runtime core alone.
- **Documentation as code.** Architecture decisions are numbered and committed next to the code
  they explain; the runtime core carries more than 2,000 Markdown files.
- **AI-assisted delivery, human-owned decisions.** Work is routed through a proposal → implement →
  review → release pipeline where the agent proposes and the gates decide.
- **Bun first.** `bun` is the daily runtime for scripts, tests and workspaces; Node.js remains
  supported where production demands it.
- **Local-first and private by default.** Keys, databases and secrets stay on the machine, and
  repositories ship the `.gitignore` that guarantees it.

---

<details>
<summary><strong>Core stack</strong></summary>

**Languages & runtimes**

![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white)
![C#](https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=flat-square&logo=php&logoColor=white)
![Bun](https://img.shields.io/badge/Bun-000000?style=flat-square&logo=bun&logoColor=F9F1E1)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)

**Front-end**

![Angular](https://img.shields.io/badge/Angular-DD0031?style=flat-square&logo=angular&logoColor=white)
![Vue](https://img.shields.io/badge/Vue-4FC08D?style=flat-square&logo=vuedotjs&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![RxJS](https://img.shields.io/badge/RxJS-B7178C?style=flat-square&logo=reactivex&logoColor=white)
![Ionic](https://img.shields.io/badge/Ionic-3880FF?style=flat-square&logo=ionic&logoColor=white)
![Capacitor](https://img.shields.io/badge/Capacitor-119EFF?style=flat-square&logo=capacitor&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Sass](https://img.shields.io/badge/Sass-CC6699?style=flat-square&logo=sass&logoColor=white)

**Back-end, data & tooling**

![NestJS](https://img.shields.io/badge/NestJS-E0234E?style=flat-square&logo=nestjs&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Zod](https://img.shields.io/badge/Zod-3E67B1?style=flat-square&logo=zod&logoColor=white)
![OpenAPI](https://img.shields.io/badge/OpenAPI-6BA539?style=flat-square&logo=openapi&logoColor=white)
![Model Context Protocol](https://img.shields.io/badge/Model_Context_Protocol-111111?style=flat-square&logo=modelcontextprotocol&logoColor=white)
![Tauri](https://img.shields.io/badge/Tauri-2-FFC131?style=flat-square&logo=tauri&logoColor=black)
![Godot](https://img.shields.io/badge/Godot-478CBF?style=flat-square&logo=godotengine&logoColor=white)

**Quality & delivery**

![Vitest](https://img.shields.io/badge/Vitest-6E9F18?style=flat-square&logo=vitest&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![ESLint](https://img.shields.io/badge/ESLint-4B32C3?style=flat-square&logo=eslint&logoColor=white)
![Prettier](https://img.shields.io/badge/Prettier-F7B93E?style=flat-square&logo=prettier&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![GitLab CI](https://img.shields.io/badge/GitLab_CI-FC6D26?style=flat-square&logo=gitlab&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

</details>

<details>
<summary><strong>Docker images</strong></summary>

Public development images for reproducible environments. Pull counts are live Docker Hub values.

| Image | Pulls | Link |
| --- | --- | --- |
| **nodebun** — Node.js + Bun | ![Docker Pulls](https://img.shields.io/docker/pulls/cartagodocker/nodebun?style=flat-square&logo=docker&label=pulls) | [![Image](https://img.shields.io/badge/Image_%E2%86%97-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/cartagodocker/nodebun) |
| **zsh** — batteries-included shell | ![Docker Pulls](https://img.shields.io/docker/pulls/cartagodocker/zsh?style=flat-square&logo=docker&label=pulls) | [![Image](https://img.shields.io/badge/Image_%E2%86%97-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/cartagodocker/zsh) |
| **ionic-cover** | ![Docker Pulls](https://img.shields.io/docker/pulls/cartagodocker/ionic-cover?style=flat-square&logo=docker&label=pulls) | [![Image](https://img.shields.io/badge/Image_%E2%86%97-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/cartagodocker/ionic-cover) |
| **nestjs-cover** | ![Docker Pulls](https://img.shields.io/docker/pulls/cartagodocker/nestjs-cover?style=flat-square&logo=docker&label=pulls) | [![Image](https://img.shields.io/badge/Image_%E2%86%97-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/cartagodocker/nestjs-cover) |
| **angular** | ![Docker Pulls](https://img.shields.io/docker/pulls/cartagodocker/angular?style=flat-square&logo=docker&label=pulls) | [![Image](https://img.shields.io/badge/Image_%E2%86%97-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/r/cartagodocker/angular) |

[![Docker Hub](https://img.shields.io/badge/Docker_Hub_%E2%86%97-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/u/cartagodocker)

</details>

<details>
<summary><strong>Also worth a look</strong></summary>

| Project | Focus | Link |
| --- | --- | --- |
| Secret manager CLI | Published npm package to encrypt keys, API keys and `.env` files. | [![Repository](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/Keyer) |
| NestJS AI API | Typed DTOs, file uploads, Docker-based delivery for AI-enabled apps. | [![Repository](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/NestGpt) |
| React front-end | The client that talks to the NestJS AI API. | [![Repository](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/ReactGpt) |
| Zoneless Angular | Angular without zone.js, exercised by unit and integration tests. | [![Repository](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/zoneless-calculator) |
| Static portfolio | Dependency-free site published from GitHub Pages. | [![Repository](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/CartagoGit.github.io) |
| Workspace template | The Angular workspace every new app starts from. | [![Repository](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/template-angular) |
| Practice repositories | Daily puzzles and katas, one commit per solution. | [![codember-dev](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/codember-dev) [![codewars](https://img.shields.io/badge/Repository_%E2%86%97-2F81F7?style=flat-square&logo=github&logoColor=white)](https://github.com/CartagoGit/codewars) |

</details>

<details>
<summary><strong>GitHub activity</strong></summary>

<p align="center">
  <img src="https://streak-stats.demolab.com?user=CartagoGit&theme=github-dark-blue&hide_border=true" alt="GitHub contribution streak" width="495">
</p>

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=CartagoGit&theme=github-dark&hide_border=true" alt="GitHub contribution activity" width="790">
</p>

</details>

---

<p align="center">
  <sub>Independent work, published in my own time. Professional and client work is not published here.<br>
  <a href="https://www.linkedin.com/in/mario-cabrero-volarich">LinkedIn</a> · <a href="https://github.com/CartagoGit?tab=repositories">All repositories</a></sub>
</p>
