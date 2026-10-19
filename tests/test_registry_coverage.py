"""test_registry_coverage — synthetic fixtures only; no network, no real files."""
import importlib.util
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
_spec = importlib.util.spec_from_file_location(
    "check_registry_coverage", SCRIPTS / "check_registry_coverage.py")
gate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(gate)

REGISTRY = {
    "repositories": [
        {"name": "devin-explore", "visibility": "public",
         "url": "https://github.com/Icaro0310/devin-explore"},
        {"name": "devin-history", "visibility": "public",
         "url": "https://github.com/Icaro0310/devin-explore"},
        {"name": "devin-secret", "visibility": "private",
         "url": "https://github.com/Icaro0310/devin-secret"},
    ]
}


def test_public_only_excludes_private():
    assert gate.registry_names(REGISTRY) == ["devin-explore", "devin-history"]


def test_uncovered_detects_missing_name():
    readme = "- [`devin-explore`](https://github.com/Icaro0310/devin-explore)"
    assert gate.uncovered(readme, ["devin-explore", "devin-history"]) == [
        "devin-history"]


def test_covered_name_in_plain_text_counts():
    readme = "The devin-history package lives in devin-explore."
    assert gate.uncovered(readme, ["devin-history", "devin-explore"]) == []


def test_substring_does_not_count_as_coverage():
    readme = "- [`devin-explore-pro`](https://example.com)"
    assert gate.uncovered(readme, ["devin-explore"]) == ["devin-explore"]


def test_main_green_on_full_coverage(tmp_path, capsys):
    (tmp_path / "reg.json").write_text(
        '{"repositories": [{"name": "devin-x", "visibility": "public"}]}')
    (tmp_path / "README.md").write_text("`devin-x` is covered.")
    sys.argv = ["gate", "--registry", str(tmp_path / "reg.json"),
                "--readme", str(tmp_path / "README.md")]
    assert gate.main() == 0


def test_main_fails_listing_missing(tmp_path, capsys):
    (tmp_path / "reg.json").write_text(
        '{"repositories": [{"name": "devin-x", "visibility": "public"}]}')
    (tmp_path / "README.md").write_text("nothing here")
    sys.argv = ["gate", "--registry", str(tmp_path / "reg.json"),
                "--readme", str(tmp_path / "README.md")]
    assert gate.main() == 1
    assert "MISSING: devin-x" in capsys.readouterr().out


def test_main_fails_on_empty_registry(tmp_path):
    (tmp_path / "reg.json").write_text('{"repositories": []}')
    (tmp_path / "README.md").write_text("x")
    sys.argv = ["gate", "--registry", str(tmp_path / "reg.json"),
                "--readme", str(tmp_path / "README.md")]
    assert gate.main() == 2


def test_real_repo_coverage_green():
    """The shipped README covers every public registry name today."""
    repo = Path(__file__).resolve().parent.parent
    registry = gate.load_registry(
        str(repo.parent.parent / "devin-powerups" / "registry.json")
        if (repo.parent.parent / "devin-powerups" / "registry.json").is_file()
        else None, None)
    names = gate.registry_names(registry)
    readme = (repo / "README.md").read_text(encoding="utf-8")
    assert gate.uncovered(readme, names) == []
