# africanjokes data files

This directory ships the curated joke and proverb corpus that the library
loads at runtime.

## Files

| File | Schema | Description |
| --- | --- | --- |
| `jokes.json` | `{schema_version: int, jokes: Joke[]}` | All jokes. |
| `proverbs.json` | `{schema_version: int, proverbs: Proverb[]}` | All proverbs. |

Both files are loaded lazily on first access via `importlib.resources` and
cached in module-level state — see `africanjokes/__init__.py`.

## Joke schema

```json
{"text": "string", "country": "string", "themes": ["string", ...]}
```

- **`text`** *(required)* — the joke. Curly quotes (`’` `“ ”`) and em dashes
  (`—`) are encouraged.
- **`country`** *(required)* — one of the existing country labels, or
  `"Pan-African"` for jokes that aren't tied to a specific country. Use the
  modern country name in English (e.g. `"DRC"`, not `"Democratic Republic of
  the Congo"`).
- **`themes`** *(required)* — one or more strings drawn from the controlled
  vocabulary. The full list lives in
  [`tools/validate_data.py`](../../tools/validate_data.py) under
  `ALLOWED_THEMES`. Today the vocabulary is:

  `animals`, `family`, `fashion`, `food`, `internet`, `money`, `music`,
  `politics`, `power`, `religion`, `school`, `sports`, `technology`, `time`,
  `traffic`, `transport`, `weather`, `weddings`, `work`.

## Proverb schema

```json
{"text": "string", "country": "string", "attribution": "string"}
```

- **`text`** *(required)* — the proverb as it's traditionally said. For proverbs
  in non-English languages, include the original then a translation
  (`"Haraka haraka haina baraka — hurry, hurry, has no blessing."`).
- **`country`** *(required)* — the modern country most associated with the
  language group.
- **`attribution`** *(required)* — the people / language group the proverb
  comes from (e.g. `"Yoruba"`, `"Akan"`, `"Swahili"`, `"Wolof"`).

## Validation

Run the validator from the repo root before submitting any data change:

```bash
python tools/validate_data.py
```

It enforces:
- Top-level shape and `schema_version` is an integer.
- Every entry has the required fields, all non-empty.
- Joke `themes` are in the controlled vocabulary.
- No duplicate `text` (case- and whitespace-insensitive) within a file.

The validator exits non-zero on any failure and is run in CI on every PR.

## Adding a new country

If your contribution introduces a new country that isn't already represented:

1. Add jokes / proverbs that use the new country label.
2. Run `python tools/validate_data.py` (the validator does not restrict
   countries — only themes are vocabulary-checked).
3. The `africanjokes --list-countries` and `--list-proverb-countries` CLI
   commands will pick it up automatically.

## Adding a new theme

Themes *are* vocabulary-checked — adding a new one requires updating
`ALLOWED_THEMES` in `tools/validate_data.py` in the same PR. Keep the
vocabulary small and orthogonal; if a new candidate overlaps an existing
theme, prefer the existing one.
