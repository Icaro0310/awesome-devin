#!/usr/bin/env python3
"""check_registry_coverage.py — CI gate: every registry name appears in README.md.

The devin-powerups registry is the source of truth for first-party
products; awesome-devin is the public catalog. When a product ships
without a catalog entry, visitors can't find it — a silent coverage gap
(same class as a dead link, but upstream). This check fails CI listing
the uncovered names so the gap is loud, not silent.

Usage:
    python3 scripts/check_registry_coverage.py [--readme README.md]
        [--registry registry.json | --registry-url URL]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

DEFAULT_REGISTRY_URL = (
    "https://raw.githubusercontent.com/Icaro0310/devin-powerups/main/registry.json"
)


def load_registry(path: str | None, url: str | None) -> dict:
    if path:
        return json.loads(Path(path).read_text(encoding="utf-8"))
    req = urllib.request.Request(
        url or DEFAULT_REGISTRY_URL, headers={"User-Agent": "registry-coverage-gate"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def registry_names(registry: dict) -> list[str]:
    """Public entries only — private repos legitimately skip the catalog."""
    return sorted(
        r["name"]
        for r in registry.get("repositories", [])
        if r.get("name") and r.get("visibility") == "public")


def uncovered(readme: str, names: list[str]) -> list[str]:
    """Names with no backticked or linked mention in the README."""
    out = []
    for name in names:
        if not re.search(rf"(?<![\w-]){re.escape(name)}(?![\w-])", readme):
            out.append(name)
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--readme", default="README.md")
    ap.add_argument("--registry", help="local registry.json (default: fetch)")
    ap.add_argument("--registry-url", help="override registry URL")
    args = ap.parse_args()
    try:
        registry = load_registry(args.registry, args.registry_url)
    except (OSError, json.JSONDecodeError) as e:
        print(f"registry-coverage: cannot load registry — {e}", file=sys.stderr)
        return 2
    names = registry_names(registry)
    if not names:
        print("registry-coverage: registry has no repository names",
              file=sys.stderr)
        return 2
    readme = Path(args.readme).read_text(encoding="utf-8")
    missing = uncovered(readme, names)
    covered = len(names) - len(missing)
    print(f"registry-coverage: {covered}/{len(names)} registry names in "
          f"{args.readme}")
    for m in missing:
        print(f"  MISSING: {m}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
