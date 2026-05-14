# Changelog

All notable changes to **africanjokes** are documented here.
The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.2.0] — 2026-05-14

### Added
- **Jokes:** expanded from 252 to **540** entries, with broader country
  coverage (40 Nigerian, 28 Liberian, 26 each from Ghana / Kenya / South Africa,
  19 Ethiopian, plus deeper representation for Tanzania, Uganda, Egypt,
  Morocco, DRC, Senegal, Zimbabwe, Cameroon, Mozambique, Sierra Leone, Zambia,
  Botswana, and Rwanda).
- **Proverbs:** expanded from 60 to **156** entries across **44 distinct
  attributions** (Akan, Amharic, Ashanti, Bambara, Bantu, Bemba, Berber,
  Bondei, Buganda, Chichewa, Egyptian Arabic, Ethiopian, Ewe, Ghanaian, Hausa,
  Igbo, Kenyan, Kikuyu, Kinyarwanda, Liberian, Lingala, Maasai, Malian,
  Mandinka, Mongo, Ndebele, Nigerian, Oromo, Pan-African, Rwandan, Setswana,
  Shona, Sierra Leonean, Sudanese, Swahili, Tanzanian, Tigrigna, Ugandan,
  Wolof, Xhosa, Yoruba, Zulu).
- **`tools/validate_data.py`** — schema validator that enforces the data
  contract, theme controlled vocabulary, and duplicate detection. Used by CI
  and recommended for contributors.
- **`py.typed`** marker (PEP 561) so type checkers pick up the inline type
  hints when consumers import `africanjokes`.
- **`CONTRIBUTING.md`** with a data-contribution guide, PR checklist, and
  setup instructions.
- **`CHANGELOG.md`** (this file).

### Changed
- Tightened controlled theme vocabulary (validator-enforced — see
  `ALLOWED_THEMES` in `tools/validate_data.py`).

## [1.1.0] — 2026-05-14

### Added
- **Structured data:** migrated from flat `africanjokes/jokes.txt` to
  `africanjokes/data/jokes.json` (252 jokes tagged with `country` and `themes`)
  and `africanjokes/data/proverbs.json` (60 sourced African proverbs with
  `country` and `attribution`).
- **Typed Python API**:
  - `Joke` and `Proverb` are `str` subclasses that carry metadata.
  - `get_joke(country=, theme=)`, `get_jokes(n=, country=, theme=)`.
  - `get_proverb(country=)`, `get_proverbs(n=, country=)`.
  - `all_jokes()`, `all_proverbs()`.
  - `list_countries(kind="jokes" | "proverbs" | "all")`, `list_themes()`.
  - `__version__` exposed at the package level.
- **Expanded CLI** flags: `--country`, `--theme`, `--count N`, `--proverb`,
  `--metadata`, `--list-countries`, `--list-proverb-countries`, `--list-themes`.
  CLI now reconfigures stdout/stderr to UTF-8 so curly quotes and em dashes
  render on Windows consoles.
- **Test suite** in `tests/` with 37 pytest cases covering the library API and
  CLI end-to-end.
- Optional install extra `[test]` for pytest.

### Removed
- `africanjokes/jokes.txt` (replaced by structured JSON).
- Root-level `test_basic.py` (replaced by the `tests/` package).

## [1.0.1]

Initial public release on PyPI.

### Added
- `get_joke()` returning a random joke from a flat `jokes.txt`.
- `africanjokes` console script with `--joke`, `--version`, `--help`.

[Unreleased]: https://github.com/daddysboy21/africanjokes/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/daddysboy21/africanjokes/releases/tag/v1.2.0
[1.1.0]: https://github.com/daddysboy21/africanjokes/releases/tag/v1.1.0
[1.0.1]: https://github.com/daddysboy21/africanjokes/releases/tag/v1.0.1
