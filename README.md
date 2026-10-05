# awesome-devin

A curated list of resources for **Devin** — the AI software engineer by Cognition — and the `devin-*` open-source tooling ecosystem.

> Community-maintained. Not affiliated with Cognition.

## Contents

- [Official Resources](#official-resources)
- [Ecosystem Catalog](#ecosystem-catalog)
- [Distribution & Infrastructure](#distribution--infrastructure)
- [Decision & QA Layer](#decision--qa-layer)
- [Configuration & Learning](#configuration--learning)
- [Data, History & Search](#data-history--search)
- [Operations](#operations)
- [Contributing](#contributing)

## Official Resources

- [Devin](https://devin.ai) — the AI software engineer.
- [Devin Documentation](https://docs.devin.ai) — official product docs.
- [Devin CLI](https://docs.devin.ai/cli) — run Devin in your terminal.
- [Devin API](https://docs.devin.ai/api) — sessions, enterprise features.

## Ecosystem Catalog

Reusable tooling that runs on the Devin CLI alone — no VM, tunnel, or external model server required. Windows and Linux supported.

### Distribution & Infrastructure

- [devin-devkit](https://github.com/Icaro0310/devin-devkit) — distribution: choose QA, evaluation, security, memory, operations or full profiles; installs Python CLIs in isolated environments with uv.
- [devin-powerups](https://github.com/Icaro0310/devin-powerups) — maintainer hub: registry source of truth, project template, catalog exporters and scheduled reports.

### Related Artifacts

- [poordjaevin](https://github.com/Icaro0310/poordjaevin) — related tool: local-first calibrated decision layer ("System One") with typed questions, honest confidence, ACP backend on Devin's own model, and offline NLI fallback.
- [qwenpaw-suite](https://github.com/Icaro0310/qwenpaw-suite) — related suite: optional self-hosted-model add-on; not required by the core tools.

### Decision & QA Layer

- [devin-qa-pack](https://github.com/Icaro0310/devin-qa-pack) — QA gates and test-generation workflows for Devin sessions.
- [devin-evals](https://github.com/Icaro0310/devin-evals) — evaluation harness for agent outputs.
- [devin-janitor](https://github.com/Icaro0310/devin-janitor) — session cleanup with judge policies before deletion.
- [devin-dream](https://github.com/Icaro0310/devin-dream) — synthetic Devin sessions with known verdicts, for testing judges and graders.

### Configuration & Learning

- [devin-doctor](https://github.com/Icaro0310/devin-doctor) — diagnostics for Devin CLI installs: config, stores, schema checks.
- [devin-internals-spec](https://github.com/Icaro0310/devin-internals-spec) — reverse-engineered notes on Devin CLI internals (sessions DB, ACP, state).
- [devin-skill-catalog](https://github.com/Icaro0310/devin-skill-catalog) — inventory, lint and quarantine for `.devin/skills` and rules, with G1/G2 gates.
- [devin-switch](https://github.com/Icaro0310/devin-switch) — swap Devin config profiles (hooks, MCP, models) with snapshot, dry-run and rollback.

### Data, History & Search

- [devin-history](https://github.com/Icaro0310/devin-history) — export and inspect Devin session history from the local sessions DB.
- [devin-memory](https://github.com/Icaro0310/devin-memory) — persistent memory layer for Devin sessions.
- [devin-search](https://github.com/Icaro0310/devin-search) — full-text search across sessions and artifacts.
- [devin-graph](https://github.com/Icaro0310/devin-graph) — session and artifact relationships as a graph.
- [devin-backup](https://github.com/Icaro0310/devin-backup) — snapshot and restore Devin CLI data.
- [devin-redact](https://github.com/Icaro0310/devin-redact) — scrub secrets from exports before sharing.

### Operations

- [devin-pm](https://github.com/Icaro0310/devin-pm) — project-management workflows on top of Devin.
- [devin-metrics](https://github.com/Icaro0310/devin-metrics) — usage and quality metrics from session data.
- [devin-bridge](https://github.com/Icaro0310/devin-bridge) — ACP client bridge for the Devin CLI (requires Node.js >= 20).
- [devin-orchestrator](https://github.com/Icaro0310/devin-orchestrator) — multi-tool orchestration across the ecosystem.
- [devin-office](https://github.com/Icaro0310/devin-office) — live Devin activity as an animated SVG circuit board: sessions, subagents, tools.

## What is this list?

An awesome list for **Devin** — the AI software engineer by Cognition AI —
and the open-source tooling built around its CLI. It answers two questions:
"what official resources exist for Devin?" and "what community tools extend
it?". Every entry links to its own repo with a one-line description; the list
itself contains no code. All listed ecosystem tools run on the Devin CLI
alone, locally, on Windows and Linux. Community-maintained; not affiliated
with, endorsed by, or sponsored by Cognition AI.

## Contributing

Suggestions via issues or pull requests. Entries must relate to Devin (CLI, API, sessions, or the devin-* tools) and include a one-line description.

## License

CC0 — public domain.
