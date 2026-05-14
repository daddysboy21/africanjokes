# africanjokes data files

This directory holds the **canonical** data shipped by both the Python and
npm packages of `africanjokes`. Edit here, then run:

```bash
python ../../tools/validate_data.py
node ../../tools/sync_data.mjs       # mirrors into ../../npm/src/data/
```

## `jokes.json`

```json
{
  "schema_version": 1,
  "jokes": [
    {
      "text": "Why did the chicken cross the road in Lagos? To get to the other side of traffic!",
      "country": "Nigeria",
      "themes": ["traffic", "animals"]
    }
  ]
}
```

| Field | Type | Notes |
| --- | --- | --- |
| `text` | non-empty string | The joke as displayed. Unicode is fine. |
| `country` | non-empty string | A country name, or `"Pan-African"` if not country-specific. |
| `themes` | non-empty list of strings | Drawn from the controlled vocabulary in [`tools/validate_data.py`](../../tools/validate_data.py) (`ALLOWED_THEMES`). |

The validator enforces:

- presence of all three fields and that none are empty
- every `theme` is a member of the allowed vocabulary
- no duplicate `text` (case- and whitespace-insensitive)

## `proverbs.json`

```json
{
  "schema_version": 1,
  "proverbs": [
    {
      "text": "Until the lion learns to write, every story will glorify the hunter.",
      "country": "Nigeria",
      "attribution": "Igbo"
    }
  ]
}
```

| Field | Type | Notes |
| --- | --- | --- |
| `text` | non-empty string | The proverb. |
| `country` | non-empty string | The modern country most associated with the source culture. |
| `attribution` | non-empty string | The people / language group (e.g. `"Yoruba"`, `"Akan"`, `"Swahili"`). Use the demonym if a more specific group is unknown. |

The validator enforces presence of all three fields and disallows duplicates.

## Adding new data

See [`CONTRIBUTING.md`](../../CONTRIBUTING.md) at the repo root for the full
contribution flow, including authenticity rules for proverbs.
