from __future__ import annotations

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SPECS = ROOT / "specs"
SKILLS = ROOT / "skills"

REQUIRED_SPECS = [
    "_meta.md",
    "functional.md",
    "openclaw_integration.md",
    "technical.md",
]


def fail(message: str) -> None:
    print(f"SPEC-CHECK FAIL: {message}")
    sys.exit(1)


def main() -> None:
    missing_specs = [name for name in REQUIRED_SPECS if not (SPECS / name).exists()]
    if missing_specs:
        fail(f"Missing spec files: {', '.join(missing_specs)}")

    readmes = list(SKILLS.rglob("README.md"))
    if not readmes:
        fail("No skill README.md files found under /skills")

    for readme in readmes:
        text = readme.read_text(encoding="utf-8").lower()
        if "input" not in text or "output" not in text:
            fail(f"Skill README missing Input/Output sections: {readme}")

    print("SPEC-CHECK PASS")


if __name__ == "__main__":
    main()