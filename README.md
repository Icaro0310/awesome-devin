<div align="center">

<a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"/></a>
<a href="https://github.com/Icaro0310/awesome-devin/actions/workflows/links.yml"><img src="https://github.com/Icaro0310/awesome-devin/actions/workflows/links.yml/badge.svg" alt="links"/></a>
<a href="https://scorecard.dev/viewer/?uri=github.com/Icaro0310/awesome-devin"><img src="https://api.scorecard.dev/projects/github.com/Icaro0310/awesome-devin/badge" alt="OpenSSF Scorecard"/></a>
<a href="https://deepwiki.com/Icaro0310/awesome-devin"><img src="https://deepwiki.com/badge.svg" alt="DeepWiki"/></a>
<a href="https://m8ven.ai/mcp/icaro0310-awesome-devin-1ve25w?s=readme"><img src="https://m8ven.ai/badge/mcp/icaro0310-awesome-devin-1ve25w" alt="M8ven Score"/></a>
<a href="LICENSE"><img src="https://img.shields.io/badge/license-CC0_1.0-lightgrey" alt="License: CC0 1.0"/></a>
<a href="https://github.com/Icaro0310/awesome-devin"><img src="https://img.shields.io/github/stars/Icaro0310/awesome-devin" alt="GitHub stars"/></a>
<a href="https://github.com/Icaro0310/awesome-devin/commits/main"><img src="https://img.shields.io/github/last-commit/Icaro0310/awesome-devin" alt="Last commit"/></a>
<a href="https://github.com/Icaro0310/awesome-devin/issues"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen" alt="PRs welcome"/></a>

</div>

# awesome-devin

A curated list of resources for **Devin** — the AI software engineer by Cognition — and the `devin-*` open-source tooling ecosystem.

> **This is not an official Cognition repository.** It is an unofficial community project, not affiliated with, endorsed by, or sponsored by Cognition AI. "Devin" is a trademark of Cognition AI. For official documentation and support, see [Official Resources](#official-resources).

![The devin-* ecosystem landscape](assets/landscape.png)

## Start here

1. [devin-doctor](https://github.com/Icaro0310/devin-doctor) — diagnose the local Devin install and stores.
2. [devin-qa-pack](https://github.com/Icaro0310/devin-qa-pack) — flagship audit of agent claims against tool-call evidence.
3. [devin-office](https://github.com/Icaro0310/devin-office) — watch live sessions as an animated circuit board.
4. [devin-devkit](https://github.com/Icaro0310/devin-devkit) — install the registry-supported profiles for Linux, Personal Windows or Corporate Windows.

## Contents

- [Official Resources](#official-resources)
- [Ecosystem Catalog](#ecosystem-catalog)
- [FAQ](#faq)
- [Community & Adjacent Lists](#community--adjacent-lists)
- [Contributing](#contributing)

## Official Resources

**Product**

- [Devin](https://devin.ai) — the AI software engineer.
- [Devin Documentation](https://docs.devin.ai) — official product docs.
- [Devin CLI](https://docs.devin.ai/work-with-devin/devin-cli) — run Devin in your terminal, hand off to cloud sessions with `/handoff`.
- [Ask Devin](https://docs.devin.ai/work-with-devin/ask-devin) — codebase Q&A, task planning, high-context sessions.
- [Devin Review](https://docs.devin.ai/work-with-devin/devin-review) — review and understand complex PRs.

**Programmatic surface**

- [Devin API v3](https://docs.devin.ai/api-reference/overview) — sessions, knowledge, playbooks, secrets, automations and analytics, with service users and org/enterprise RBAC.
- [Devin MCP](https://docs.devin.ai/work-with-devin/devin-mcp) — official MCP server: external agents can manage sessions, playbooks, knowledge, and repository docs.
- [MCP servers & marketplace](https://docs.devin.ai/work-with-devin/mcp) — connect external tools to Devin via MCP (STDIO, SSE, HTTP).
- [DeepWiki](https://deepwiki.com) + [DeepWiki MCP](https://docs.devin.ai/work-with-devin/deepwiki-mcp) — auto-generated docs and architecture diagrams for public repos; free MCP server (`ask_question`, `read_wiki_structure`, `read_wiki_contents`).
- [Python SDK](https://docs.devin.ai/federal/api/python-sdk) — analytics, groups, and ACU limits from Python.

**Agentic configuration**

- [Devin Skills](https://docs.devin.ai/product-guides/skills) — reusable `SKILL.md` procedures committed to repos, following the Agent Skills standard.
- [Devin Plugins](https://docs.devin.ai/product-guides/plugins) — versioned bundles of skills, rules, MCP servers, hooks, and subagents, with org/enterprise governance.
- [Playbooks](https://docs.devin.ai/product-guides/using-playbooks) — reusable org-shared prompts attached to sessions via macros.
- [Devin Memory & Dreaming](https://docs.devin.ai/product-guides/memory) — cross-session preference and lesson notes, organized automatically.
- [Integrations](https://docs.devin.ai/integrations/overview) — Slack, Teams, Linear, GitHub, PagerDuty, MCP.

**Operations**

- [Session Insights](https://docs.devin.ai/product-guides/session-insights) — analyze completed sessions, knowledge usage, and prompt coaching.
- [Scheduled Sessions & Automations](https://docs.devin.ai/product-guides/scheduled-sessions) — recurring and trigger-based work.
- [Security Profiles](https://docs.devin.ai/product-guides/security-profiles) — org-level restrictions on network, MCP, git, and `gh` access.
- [Personal Analytics](https://docs.devin.ai/enterprise/security-access/personal-analytics) — the official ACU consumption view (what local stores cannot tell you about cost).

## Ecosystem Catalog

One registry ([devin-powerups](https://github.com/Icaro0310/devin-powerups)) is the source of truth; [devin-devkit](https://github.com/Icaro0310/devin-devkit) is the distribution layer that installs it. Reusable tooling that runs on the Devin CLI alone — no VM, tunnel, or external model server required. Linux, Personal Windows and Corporate Windows are supported; Corporate Windows runs the registry-approved local-only subset.

### Distribution & Infrastructure

- [devin-devkit](https://github.com/Icaro0310/devin-devkit) — distribution: choose QA, evaluation, security, memory, operations or full profiles under Linux, Personal Windows or the explicit Corporate Windows local-only mode; installs Python CLIs in isolated environments with uv.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** distribution
  - **Interfaces:** cli, installer
  - **Platforms:** Windows, Linux
  </details>
- [devin-powerups](https://github.com/Icaro0310/devin-powerups) — maintainer hub: registry source of truth, project template, catalog exporters and scheduled reports.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** infrastructure
  - **Interfaces:** cli, registry, docs
  - **Platforms:** Windows, Linux
  </details>

### Related Artifacts

- [poordjaevin](https://github.com/Icaro0310/poordjaevin) — related tool: local-first calibrated decision layer ("System One") with typed questions, honest confidence, ACP backend on Devin's own model, and offline NLI fallback.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, library, mcp, bridge
  - **Platforms:** Windows, Linux
  </details>
- [qwenpaw-suite](https://github.com/Icaro0310/qwenpaw-suite) — related suite: optional self-hosted-model add-on; not required by the core tools.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** suite
  - **Interfaces:** service, bridge, docs
  - **Platforms:** Windows, Linux
  </details>

### Decision & QA Layer

- [devin-qa-pack](https://github.com/Icaro0310/devin-qa-pack) — flagship QA audit: PASS/PARTIAL/UNVERIFIED from tool-call evidence.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli
  - **Platforms:** Windows, Linux
  </details>
- [devin-evals](https://github.com/Icaro0310/devin-evals) — evaluation harness for agent outputs.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, library
  - **Platforms:** Windows, Linux
  </details>
- [devin-janitor](https://github.com/Icaro0310/devin-janitor) — session cleanup with judge policies before deletion.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, automation
  - **Platforms:** Windows, Linux
  </details>
- [devin-dream](https://github.com/Icaro0310/devin-dream) — synthetic Devin sessions with known verdicts, for testing judges and graders.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, library
  - **Platforms:** Windows, Linux
  </details>

### Configuration & Learning

- [devin-doctor](https://github.com/Icaro0310/devin-doctor) — diagnostics for Devin CLI installs: config, stores, schema checks.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli
  - **Platforms:** Windows, Linux
  </details>
- [devin-internals-spec](https://github.com/Icaro0310/devin-internals-spec) — reverse-engineered notes on Devin CLI internals (sessions DB, ACP, state).
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, library
  - **Platforms:** Windows, Linux
  </details>
- [devin-skill-catalog](https://github.com/Icaro0310/devin-skill-catalog) — inventory, lint and quarantine for `.devin/skills` and rules, with G1/G2 gates.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, registry
  - **Platforms:** Windows, Linux
  </details>
- [devin-switch](https://github.com/Icaro0310/devin-switch) — swap Devin config profiles (hooks, MCP, models) with snapshot, dry-run and rollback.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli
  - **Platforms:** Windows, Linux
  </details>

### Data, History & Search

- [devin-history](https://github.com/Icaro0310/devin-history) — export and inspect Devin session history from the local sessions DB.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli
  - **Platforms:** Windows, Linux
  </details>
- [devin-memory](https://github.com/Icaro0310/devin-memory) — persistent memory layer for Devin sessions.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, library, mcp, service
  - **Platforms:** Windows, Linux
  </details>
- [devin-search](https://github.com/Icaro0310/devin-search) — full-text search across sessions and artifacts.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli
  - **Platforms:** Windows, Linux
  </details>
- [devin-graph](https://github.com/Icaro0310/devin-graph) — session and artifact relationships as a graph.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, library
  - **Platforms:** Windows, Linux
  </details>
- [devin-backup](https://github.com/Icaro0310/devin-backup) — snapshot and restore Devin CLI data.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli
  - **Platforms:** Windows, Linux
  </details>
- [devin-redact](https://github.com/Icaro0310/devin-redact) — scrub secrets from exports before sharing.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, library
  - **Platforms:** Windows, Linux
  </details>

### Operations

- [devin-pm](https://github.com/Icaro0310/devin-pm) — project-management workflows on top of Devin.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, registry
  - **Platforms:** Windows, Linux
  </details>
- [devin-metrics](https://github.com/Icaro0310/devin-metrics) — local session observability: activity, context size and token peaks; no persisted cost fields.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, dashboard
  - **Platforms:** Windows, Linux
  </details>
- [devin-bridge](https://github.com/Icaro0310/devin-bridge) — ACP client bridge for the Devin CLI (requires Node.js >= 20).
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, bridge
  - **Platforms:** Windows, Linux
  </details>
- [devin-orchestrator](https://github.com/Icaro0310/devin-orchestrator) — multi-tool orchestration across the ecosystem.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** cli, automation
  - **Platforms:** Windows, Linux
  </details>
- [devin-office](https://github.com/Icaro0310/devin-office) — live Devin activity as an animated SVG circuit board: sessions, subagents, tools.
  <details><summary>type · interfaces · platforms</summary>

  - **Type:** tool
  - **Interfaces:** service, dashboard
  - **Platforms:** Windows, Linux
  </details>

## FAQ

**Is this affiliated with Cognition AI?**
No. This is an unofficial community project. For official resources, see [Official Resources](#official-resources).

**Do I need Devin installed?**
Not to explore. `devin-dream` generates synthetic sessions with labeled defects, and the [Agent Assurance demo](https://github.com/Icaro0310/devin-qa-pack/tree/main/examples/agent-assurance) runs end-to-end with only `git` + `curl`. The production tools do read local Devin CLI data, so they are most useful on machines where Devin CLI actually runs.

**Does it cost anything?**
The tools are open source and local-first — no accounts, no telemetry, no API keys for the core catalog. `poordjaevin`'s optional ACP backend reuses the model your Devin CLI already runs.

**Does it work on Windows?**
Yes. Linux and Personal Windows run the full catalog. Corporate Windows is supported through the explicit `devin-devkit` local-only profile, which installs the registry-approved subset — no VM, tunnel, or external compute required.

**Where do I start if I only try one thing?**
`devin-doctor` to see what your install looks like, then the [Agent Assurance demo](https://github.com/Icaro0310/devin-qa-pack/tree/main/examples/agent-assurance) to watch claims-vs-evidence auditing run on generated sessions.

**How do I suggest a resource?**
Open a [suggestion issue](https://github.com/Icaro0310/awesome-devin/issues/new?template=suggest-resource.yml) or a pull request.

## Community & Adjacent Lists

Curated lists in the same neighborhood — different scope, worth browsing:

- [e2b-dev/awesome-devins](https://github.com/e2b-dev/awesome-devins) — the landscape of "Devin-inspired" open and closed-source AI agents.
- [e2b-dev/awesome-ai-sdks](https://github.com/e2b-dev/awesome-ai-sdks) — SDKs and frameworks for building AI agents.
- [bradAGI/awesome-cli-coding-agents](https://github.com/bradAGI/awesome-cli-coding-agents) — terminal-native coding agents and the harnesses that orchestrate them.
- [ai-for-developers/awesome-ai-coding-tools](https://github.com/ai-for-developers/awesome-ai-coding-tools) — AI-powered coding tools across editors, CLIs, and agents.
- [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) — the canonical MCP server directory.
- [atinfo/awesome-test-automation](https://github.com/atinfo/awesome-test-automation) — test automation frameworks and tools across languages.
- [kmaasrud/awesome-obsidian](https://github.com/kmaasrud/awesome-obsidian) — Obsidian plugins, themes, and workflows.

## What is this list?

An awesome list for **Devin** — the AI software engineer by Cognition AI —
and the open-source tooling built around its CLI. It answers two questions:
"what official resources exist for Devin?" and "what community tools extend
it?". Every entry links to its own repo with a one-line description; the list
itself contains no code. Core ecosystem tools run on the Devin CLI alone,
locally, across Linux, Personal Windows and the Corporate Windows local-only
subset. Community-maintained; not affiliated with, endorsed by, or sponsored
by Cognition AI.

## Contributing

Suggestions via the [suggest-a-resource issue template](https://github.com/Icaro0310/awesome-devin/issues/new?template=suggest-resource.yml) or pull requests. Entries must relate to Devin (CLI, API, sessions, or the devin-* tools) and include a one-line description.

## License

CC0 — public domain.
