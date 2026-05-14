# Contributing to africanjokes

Thanks for wanting to help! This guide covers the two most common
contributions: **adding jokes or proverbs**, and **changing the library code**.

## Getting set up

```bash
git clone https://github.com/daddysboy21/africanjokes
cd africanjokes
pip install -e ".[test]"
```

Verify your environment:

```bash
pytest                          # all tests should pass
python tools/validate_data.py   # data files should validate cleanly
africanjokes --version          # CLI should report the installed version
```

## Adding jokes

Jokes live in [`africanjokes/data/jokes.json`](africanjokes/data/jokes.json).
Each entry is one JSON object on its own line, with three required fields:

```json
{"text": "...", "country": "Nigeria", "themes": ["traffic", "animals"]}
```

- **`text`** — the joke itself. Keep it punchy. Curly quotes (`’` `“ ”`) and
  em dashes (`—`) are encouraged.
- **`country`** — one of the existing countries (`africanjokes --list-countries`)
  or a new one. Use `Pan-African` for jokes that aren't tied to a specific country.
- **`themes`** — at least one theme from the controlled vocabulary. The full
  list lives in `tools/validate_data.py` (`ALLOWED_THEMES`) and is also visible
  via `africanjokes --list-themes`. Add a new theme there in the same PR if
  you need one — keep the vocabulary tight.

After editing, run:

```bash
python tools/validate_data.py
```

The validator catches missing fields, unknown themes, and duplicate joke text.

## Adding proverbs

Proverbs live in [`africanjokes/data/proverbs.json`](africanjokes/data/proverbs.json):

```json
{"text": "...", "country": "Ghana", "attribution": "Akan"}
```

- **`text`** — the proverb as it's traditionally said.
- **`country`** — the modern country most associated with the language group.
- **`attribution`** — the people / language group the proverb comes from
  (e.g. `Yoruba`, `Akan`, `Swahili`, `Wolof`, `Amharic`). Be honest: only add
  proverbs you can attribute. Don't invent or paraphrase wisdom and assign it
  to a culture.

## Code changes

- All public API lives in [`africanjokes/__init__.py`](africanjokes/__init__.py).
  Keep it typed, keep it small, keep new functions backwards compatible where
  possible.
- The CLI is in [`africanjokes/cli.py`](africanjokes/cli.py). Tests for it are in
  [`tests/test_cli.py`](tests/test_cli.py) — please add a test for any new flag.
- Run the full test suite (`pytest`) before opening a PR.

## PR checklist

- [ ] `pytest` passes
- [ ] `python tools/validate_data.py` passes
- [ ] New jokes / proverbs follow the schema and are not duplicates
- [ ] CHANGELOG.md updated under the **Unreleased** section
- [ ] No emoji introduced into source files (the maintainer prefers plain text)

## Reporting bugs

Open an issue with:
1. What you ran (`africanjokes --joke --country …`, the Python snippet, etc.)
2. What you expected.
3. What actually happened (full traceback if any).
4. Your Python version and OS.
