# africanjokes

<!-- Main project stats badges -->
[![PyPI version](https://img.shields.io/pypi/v/africanjokes)](https://pypi.org/project/africanjokes/)
[![npm version](https://img.shields.io/npm/v/africanjokes)](https://www.npmjs.com/package/africanjokes)
[![Downloads](https://img.shields.io/pepy/dt/africanjokes)](https://pepy.tech/project/africanjokes)
[![Actions Status](https://github.com/daddysboy21/africanjokes/actions/workflows/python-app.yml/badge.svg)](https://github.com/daddysboy21/africanjokes/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/africanjokes)](https://pypi.org/project/africanjokes/)
[![Node Version](https://img.shields.io/node/v/africanjokes)](https://www.npmjs.com/package/africanjokes)
[![Maintenance](https://img.shields.io/maintenance/yes/2025)](https://github.com/daddysboy21/africanjokes)

<!-- GitHub community stats badges -->
[![stars](https://img.shields.io/github/stars/daddysboy21/africanjokes)](https://github.com/daddysboy21/africanjokes/stargazers)
[![forks](https://img.shields.io/github/forks/daddysboy21/africanjokes)](https://github.com/daddysboy21/africanjokes/network)
[![watchers](https://img.shields.io/github/watchers/daddysboy21/africanjokes)](https://github.com/daddysboy21/africanjokes/watchers)
[![Last Commit](https://img.shields.io/github/last-commit/daddysboy21/africanjokes)](https://github.com/daddysboy21/africanjokes/commits)
[![Open Issues](https://img.shields.io/github/issues/daddysboy21/africanjokes)](https://github.com/daddysboy21/africanjokes/issues)

<br>

<!-- Social & support badges grouped for clarity -->
[![Twitter](https://img.shields.io/twitter/follow/daddysboy_21?style=social)](https://twitter.com/daddysboy_21)
[![GitHub](https://img.shields.io/github/followers/daddysboy21?label=Follow&style=social)](https://github.com/daddysboy21)
[![Instagram](https://img.shields.io/badge/@daddysboy.21-E4405F?style=flat&logo=instagram&logoColor=white)](https://instagram.com/daddysboy.21)
[![TikTok](https://img.shields.io/badge/TikTok-@daddysboy.21-black?style=flat&logo=tiktok)](https://tiktok.com/@daddysboy.21)
[![Twitch](https://img.shields.io/badge/Twitch-daddysboy_21-9146FF?style=flat&logo=twitch&logoColor=white)](https://twitch.tv/daddysboy_21)
[![Gravatar](https://img.shields.io/badge/Gravatar-daddysboy21-4B8BBE?style=flat&logo=gravatar&logoColor=white)](https://daddysboy21.link)
[![WhatsApp](https://img.shields.io/badge/WhatsApp-Chat-green?style=flat&logo=whatsapp&logoColor=white)](https://wa.me/231555557034)
[![Buy Me A Coffee](https://img.shields.io/badge/Support-Buy%20Me%20a%20Coffee-orange?style=flat&logo=buy-me-a-coffee)](https://buymeacoffee.com/PBEzMY14YC)

---

**africanjokes** is a small, dependency-free library and CLI that delivers
random African jokes and proverbs - categorised by country and theme - straight
into your terminal, scripts, bots, or applications. Available for **Python**
(via `pip`) and **Node.js** (via `npm`), with a shared dataset and matching
APIs in both ecosystems.

> v1.2.0 ships **540 jokes from 20 countries**, **156 proverbs across 44
> distinct people / language attributions**, typed APIs in both Python and
> JavaScript, and an expanded CLI with country / theme filters.

---

## Table of Contents

- [Installation](#installation)
- [Quickstart](#quickstart)
- [Python API](#python-api)
- [JavaScript API](#javascript-api)
- [CLI Usage](#cli-usage)
- [Data Coverage](#data-coverage)
- [Contributing](#contributing)
- [Development](#development)
- [License](#license)
- [Author](#author)
- [Connect with Me](#connect-with-me)
- [Support & Spread Laughter](#support--spread-laughter)

---

## Installation

**Python (PyPI):**

```bash
pip install africanjokes
```

Requires Python 3.9+. No third-party dependencies.

**Node.js (npm):**

```bash
npm install africanjokes
```

Requires Node 16+. ESM only, no runtime dependencies. TypeScript types ship
in the package — no `@types/*` install needed.

Both packages run on Windows, macOS, and Linux.

---

## Quickstart

**Python:**

```python
import africanjokes

print(africanjokes.get_joke())
print(africanjokes.get_joke(country="Nigeria"))
print(africanjokes.get_joke(theme="power"))
print(africanjokes.get_proverb(country="Ghana"))
```

**JavaScript:**

```js
import { getJoke, getProverb } from "africanjokes";

console.log(String(getJoke()));
console.log(String(getJoke({ country: "Nigeria" })));
console.log(String(getJoke({ theme: "power" })));
console.log(String(getProverb({ country: "Ghana" })));
```

**CLI** (identical flags whichever package you installed):

```bash
africanjokes                        # random joke
africanjokes --country Nigeria      # random Nigerian joke
africanjokes --proverb              # random African proverb
africanjokes --count 5 --theme food # five food-themed jokes
```

For a one-off run without installing globally, Node users can do
`npx africanjokes --country Liberia`.

---

## Python API

Every function is fully typed and documented. The full public surface:

| Function | Description |
| --- | --- |
| `get_joke(country=None, theme=None)` | A random joke, optionally filtered. Returns a `Joke` (a `str` subclass with `.country` and `.themes`). |
| `get_jokes(n=1, country=None, theme=None)` | `n` distinct random jokes (capped at the matching pool size). |
| `get_proverb(country=None)` | A random African proverb. Returns a `Proverb` (a `str` with `.country` and `.attribution`). |
| `get_proverbs(n=1, country=None)` | `n` distinct random proverbs. |
| `all_jokes()` / `all_proverbs()` | The full data set as lists. |
| `list_countries(kind="jokes")` | Sorted list of countries. `kind` is `"jokes"`, `"proverbs"`, or `"all"`. |
| `list_themes()` | Sorted list of joke themes. |
| `__version__` | The installed library version (`"1.2.0"`). |

`Joke` and `Proverb` are subclasses of `str`, so they print and concatenate
exactly like strings — but you can still inspect their metadata:

```python
joke = africanjokes.get_joke(country="Ghana")
print(joke)               # the joke text
print(joke.country)       # "Ghana"
print(joke.themes)        # ("food", "politics")

proverb = africanjokes.get_proverb()
print(proverb)            # the proverb text
print(proverb.country)    # "Nigeria"
print(proverb.attribution)# "Yoruba"
```

Filters are case-insensitive. Unknown countries or themes raise `LookupError`
with a clear message.

---

## JavaScript API

The npm package mirrors the Python API with idiomatic JS naming:

| Function | Returns | Notes |
| --- | --- | --- |
| `getJoke({ country?, theme? })` | `Joke` | Random joke, optionally filtered. |
| `getJokes(n = 1, { country?, theme? })` | `Joke[]` | `n` distinct jokes (capped at pool). |
| `getProverb({ country? })` | `Proverb` | Random proverb. |
| `getProverbs(n = 1, { country? })` | `Proverb[]` | `n` distinct proverbs. |
| `allJokes()` / `allProverbs()` | `Joke[]` / `Proverb[]` | Full data set. |
| `listCountries(kind = "jokes")` | `string[]` | `"jokes"`, `"proverbs"`, or `"all"`. |
| `listThemes()` | `string[]` | All joke themes. |
| `version` | `string` | Installed library version. |

`Joke` and `Proverb` instances expose `.text`, `.country`, plus `.themes` or
`.attribution`. They implement `toString()` so they print naturally:

```js
import { getJoke, getProverb, Joke } from "africanjokes";

const j: Joke = getJoke({ country: "Ghana" });
j.text         // the text
j.country      // "Ghana"
j.themes       // ["food", "politics"]
`${j}`         // same as j.text

const p = getProverb();
p.attribution  // e.g. "Yoruba"
```

Filters are case-insensitive. Unknown countries/themes throw `NoMatchError`
(an `Error` subclass); non-positive `n` throws `RangeError`.

See [`npm/README.md`](npm/README.md) for the package-local docs.

---

## CLI Usage

```text
africanjokes [-h] [-j | -p | --list-countries | --list-proverb-countries | --list-themes | -v]
             [-c NAME] [-t NAME] [-n N] [--metadata]
```

### Flags

| Flag | Description |
| --- | --- |
| `-j`, `--joke` | Print a random joke (default behavior). |
| `-p`, `--proverb` | Print a random African proverb. |
| `-c NAME`, `--country NAME` | Filter to jokes/proverbs from a country. |
| `-t NAME`, `--theme NAME` | Filter jokes by theme. (Ignored for proverbs.) |
| `-n N`, `--count N` | Print `N` items (default: 1). |
| `--metadata` | Show country/theme alongside each item. |
| `--list-countries` | List all countries that have jokes. |
| `--list-proverb-countries` | List all countries that have proverbs. |
| `--list-themes` | List all joke themes. |
| `-v`, `--version` | Print the installed version. |
| `-h`, `--help` | Show usage. |

### Examples

```bash
$ africanjokes
African weddings: Come for love, stay for the jollof.

$ africanjokes --country Liberia
In Liberia, taxis don't use maps—they use destiny.

$ africanjokes --theme power --count 3
African presidents: they promise light but deliver darkness.
African horror movie: When NEPA goes off and your phone is on 2%.
African kids do homework with candlelight and still pass.

$ africanjokes --proverb --country Ghana --metadata
Wisdom is like a baobab tree; no one individual can embrace it.  [Ghana · Akan]

$ africanjokes --list-themes
animals
family
fashion
food
internet
... (and more)

$ africanjokes --version
africanjokes 1.2.0
```

---

## Data Coverage

- **Jokes:** 540 entries across 20 countries (Botswana, Cameroon, DRC, Egypt,
  Ethiopia, Ghana, Kenya, Liberia, Morocco, Mozambique, Nigeria, Pan-African,
  Rwanda, Senegal, Sierra Leone, South Africa, Tanzania, Uganda, Zambia,
  Zimbabwe), tagged with 19 themes (animals, family, fashion, food, internet,
  money, music, politics, power, religion, school, sports, technology, time,
  traffic, transport, weather, weddings, work).
- **Proverbs:** 156 entries with attribution to 44 distinct people /
  language groups (Akan, Ashanti, Bambara, Bantu, Bondei, Buganda, Hausa, Igbo,
  Mongo, Swahili, Wolof, Yoruba, Zulu, and others).

The data lives in `africanjokes/data/jokes.json` and
`africanjokes/data/proverbs.json` — easy to extend in a PR.

---

## Contributing

Got a great African joke or proverb to share? Pull requests are welcome.

1. Fork the repo.
2. Add your joke to `africanjokes/data/jokes.json` (with `country` and at least
   one `themes` entry) — or your proverb to
   `africanjokes/data/proverbs.json` (with `country` and `attribution`).
3. Run the tests with `pytest`.
4. Submit a PR.

See the [contributing wiki](https://github.com/daddysboy21/africanjokes/wiki/Contributing)
for the full guide.

---

## Development

```bash
git clone https://github.com/daddysboy21/africanjokes
cd africanjokes

# Python package
pip install -e ".[test]"
pytest                                     # 37 tests

# npm package
cd npm && npm test                         # 30 tests
cd ..

# Validate data files (schema, theme vocabulary, duplicates)
python tools/validate_data.py

# Sync canonical Python data into the npm copy after editing
node tools/sync_data.mjs
```

`pyproject.toml`, `africanjokes/__init__.py` (`__version__`), and
`npm/package.json` are kept in lockstep. See
[`CONTRIBUTING.md`](CONTRIBUTING.md) for the data-contribution flow and the
release checklist.

---

## License

MIT — see [`LICENSE`](https://github.com/daddysboy21/africanjokes/blob/main/LICENSE).
Free to use, modify, and distribute.

---

## Author

**`Morris D. Toclo`**  
Co-Founder & Co-CEO of LoneScore  
Student — BlueCrest University College Liberia  
Monrovia, Liberia

---

## Connect with Me

- [`Website`](https://daddysboy21.link)
- [`GitHub`](https://github.com/daddysboy21)
- [`LinkedIn`](https://www.linkedin.com/in/morris-toclo-a83858275)
- [`X (Twitter)`](https://x.com/daddysboy_21)
- [`Twitch`](https://twitch.tv/daddysboy_21)
- [`Instagram`](https://instagram.com/daddysboy.21)
- [`TikTok`](https://tiktok.com/@daddysboy.21)
- [`WhatsApp`](https://wa.me/231555557034)
- [`Buy Me a Coffee`](https://buymeacoffee.com/PBEzMY14YC)
- [`Gravatar`](https://daddysboy21.link)

---

## Support & Spread Laughter

If you enjoy using africanjokes, please:

- Star the repo
- Contribute your own jokes or proverbs
- [`Buy Me a Coffee`](https://buymeacoffee.com/PBEzMY14YC)
- Share it with your community

Let’s spread African joy — one joke at a time.  
**`Made with love in Africa.`**

---
