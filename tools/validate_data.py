"""Validate africanjokes/data/*.json against the package's schema.

Run from the repo root:

    python tools/validate_data.py

Exits 0 on success, 1 on any validation failure. Used by CI and recommended for
contributors before submitting a PR that touches the data files.

Checks performed:
  jokes.json
    - top-level shape: {"schema_version": int, "jokes": list}
    - each joke has: text (non-empty str), country (non-empty str),
      themes (non-empty list of non-empty strs)
    - themes are drawn from the controlled vocabulary
    - no duplicate joke texts (case- and whitespace-insensitive)
  proverbs.json
    - top-level shape: {"schema_version": int, "proverbs": list}
    - each proverb has: text (non-empty str), country (non-empty str),
      attribution (non-empty str)
    - no duplicate proverb texts (case- and whitespace-insensitive)
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "africanjokes" / "data"

ALLOWED_THEMES = {
    "animals",
    "family",
    "fashion",
    "food",
    "internet",
    "money",
    "music",
    "politics",
    "power",
    "religion",
    "school",
    "sports",
    "technology",
    "time",
    "traffic",
    "transport",
    "weather",
    "weddings",
    "work",
}


def _norm(text: str) -> str:
    return " ".join(text.split()).casefold()


def _check_str(value: object, label: str, errors: list[str]) -> bool:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{label} must be a non-empty string, got {value!r}")
        return False
    return True


def validate_jokes(path: Path, errors: list[str]) -> int:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict) or "jokes" not in data:
        errors.append(f"{path.name}: top-level object must have a 'jokes' key")
        return 0
    if not isinstance(data.get("schema_version"), int):
        errors.append(f"{path.name}: 'schema_version' must be an integer")

    jokes = data["jokes"]
    if not isinstance(jokes, list) or not jokes:
        errors.append(f"{path.name}: 'jokes' must be a non-empty list")
        return 0

    seen: dict[str, int] = {}
    for index, joke in enumerate(jokes):
        loc = f"{path.name}#{index}"
        if not isinstance(joke, dict):
            errors.append(f"{loc}: must be an object, got {type(joke).__name__}")
            continue
        _check_str(joke.get("text"), f"{loc}.text", errors)
        _check_str(joke.get("country"), f"{loc}.country", errors)

        themes = joke.get("themes")
        if not isinstance(themes, list) or not themes:
            errors.append(f"{loc}.themes must be a non-empty list")
        else:
            for theme in themes:
                if not isinstance(theme, str) or not theme:
                    errors.append(f"{loc}.themes contains an invalid entry: {theme!r}")
                    continue
                if theme not in ALLOWED_THEMES:
                    errors.append(
                        f"{loc}.themes uses unknown theme {theme!r} "
                        f"(allowed: {sorted(ALLOWED_THEMES)})"
                    )

        text = joke.get("text")
        if isinstance(text, str):
            key = _norm(text)
            if key in seen:
                errors.append(
                    f"{loc}.text duplicates entry #{seen[key]}: {text!r}"
                )
            else:
                seen[key] = index

    return len(jokes)


def validate_proverbs(path: Path, errors: list[str]) -> int:
    with path.open(encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, dict) or "proverbs" not in data:
        errors.append(f"{path.name}: top-level object must have a 'proverbs' key")
        return 0
    if not isinstance(data.get("schema_version"), int):
        errors.append(f"{path.name}: 'schema_version' must be an integer")

    proverbs = data["proverbs"]
    if not isinstance(proverbs, list) or not proverbs:
        errors.append(f"{path.name}: 'proverbs' must be a non-empty list")
        return 0

    seen: dict[str, int] = {}
    for index, proverb in enumerate(proverbs):
        loc = f"{path.name}#{index}"
        if not isinstance(proverb, dict):
            errors.append(f"{loc}: must be an object, got {type(proverb).__name__}")
            continue
        _check_str(proverb.get("text"), f"{loc}.text", errors)
        _check_str(proverb.get("country"), f"{loc}.country", errors)
        _check_str(proverb.get("attribution"), f"{loc}.attribution", errors)

        text = proverb.get("text")
        if isinstance(text, str):
            key = _norm(text)
            if key in seen:
                errors.append(
                    f"{loc}.text duplicates entry #{seen[key]}: {text!r}"
                )
            else:
                seen[key] = index

    return len(proverbs)


def main() -> int:
    errors: list[str] = []
    jokes_path = DATA_DIR / "jokes.json"
    proverbs_path = DATA_DIR / "proverbs.json"

    n_jokes = validate_jokes(jokes_path, errors)
    n_proverbs = validate_proverbs(proverbs_path, errors)

    if errors:
        print(f"Found {len(errors)} validation error(s):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK: {n_jokes} jokes, {n_proverbs} proverbs validated cleanly.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
