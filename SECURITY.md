# Security Policy

## What this repository is

This repository is a **curated list and documentation** — it contains no
runtime code, no telemetry, and nothing that transmits data. The tools it
links to are independent repositories, each with its own security policy.

## Sensitive data handling

- Never commit Devin session databases, `.env` files, tokens, or pairing
  codes to this repository.
- Linked tools have their own data policies; check each repo's
  `SECURITY.md` before trusting a claim.

## Reporting a vulnerability

Open a **private** security advisory on GitHub, or open an issue marked
`[SECURITY]` **without** including the vulnerable data itself.

Do not file public issues containing secrets, tokens, or session content.
