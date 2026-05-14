# africanjokes

[![npm version](https://img.shields.io/npm/v/africanjokes)](https://www.npmjs.com/package/africanjokes)
[![Node Version](https://img.shields.io/node/v/africanjokes)](https://www.npmjs.com/package/africanjokes)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Random African jokes and proverbs — **540 jokes from 20 countries** and **156
proverbs from 44 distinct people / language attributions** — as a tiny,
zero-dependency Node.js library and CLI. The JavaScript companion to the
[Python package of the same name](https://pypi.org/project/africanjokes/),
sharing the same data files.

---

## Install

```bash
npm install africanjokes
```

Requires Node 16 or newer. ESM only.

For one-off CLI use without installing globally:

```bash
npx africanjokes --country Nigeria
```

---

## Quickstart

```js
import {
  getJoke,
  getJokes,
  getProverb,
  listCountries,
  listThemes,
} from "africanjokes";

console.log(String(getJoke()));
// "African weddings: Come for love, stay for the jollof."

console.log(String(getJoke({ country: "Nigeria" })));
console.log(String(getJoke({ theme: "power" })));
console.log(String(getProverb({ country: "Ghana" })));

const five = getJokes(5, { theme: "food" });
five.forEach((j) => console.log(String(j)));
```

The default export bundles every named export, so you can also do:

```js
import africanjokes from "africanjokes";
console.log(africanjokes.getJoke().text);
```

---

## CLI

```text
africanjokes [options]

Options:
  -j, --joke                   Print a random joke (default).
  -p, --proverb                Print a random African proverb.
  -c, --country NAME           Filter to jokes/proverbs from a country.
  -t, --theme NAME             Filter jokes by theme.
  -n, --count N                Print N items (default: 1).
      --metadata               Show country/theme alongside each item.
      --list-countries         List all countries that have jokes.
      --list-proverb-countries List all countries that have proverbs.
      --list-themes            List all joke themes.
  -v, --version                Print the installed version.
  -h, --help                   Show this message.
```

Examples:

```bash
africanjokes
africanjokes --country Liberia
africanjokes --theme power --count 3
africanjokes --proverb --country Ghana --metadata
```

---

## API

| Function | Returns | Notes |
| --- | --- | --- |
| `getJoke({ country?, theme? })` | `Joke` | Random joke, optionally filtered. |
| `getJokes(n = 1, { country?, theme? })` | `Joke[]` | `n` distinct jokes (capped at pool). |
| `getProverb({ country? })` | `Proverb` | Random proverb. |
| `getProverbs(n = 1, { country? })` | `Proverb[]` | `n` distinct proverbs. |
| `allJokes()` / `allProverbs()` | `Joke[]` / `Proverb[]` | Full data set (fresh array). |
| `listCountries(kind = "jokes")` | `string[]` | `"jokes"`, `"proverbs"`, or `"all"`. |
| `listThemes()` | `string[]` | All joke themes. |
| `version` | `string` | The installed library version. |

### Joke and Proverb instances

Both classes carry their text and metadata, and `toString()` returns the text
so they print naturally in template strings:

```js
const j = getJoke({ country: "Ghana" });
j.text         // "Ghana jollof rule: never compare to Nigeria's — never."
j.country      // "Ghana"
j.themes       // ["food", "politics"]
String(j)      // same as j.text
`${j}`         // same as j.text

const p = getProverb({ country: "Nigeria" });
p.attribution  // "Yoruba"
```

Filters are case-insensitive. Unknown countries or themes throw a
`NoMatchError` (a subclass of `Error`) with a clear message; non-positive
`n` throws `RangeError`.

---

## TypeScript

The package ships with `.d.ts` declarations. No `@types/*` install needed.

```ts
import { getJoke, Joke } from "africanjokes";

const j: Joke = getJoke({ country: "Nigeria" });
```

---

## Data Coverage

- **540 jokes** from 20 countries (Botswana, Cameroon, DRC, Egypt, Ethiopia,
  Ghana, Kenya, Liberia, Morocco, Mozambique, Nigeria, Pan-African, Rwanda,
  Senegal, Sierra Leone, South Africa, Tanzania, Uganda, Zambia, Zimbabwe),
  tagged with 19 themes.
- **156 proverbs** from 44 people / language attributions (Akan, Ashanti,
  Yoruba, Igbo, Hausa, Swahili, Kikuyu, Maasai, Buganda, Zulu, Xhosa,
  Setswana, Shona, Wolof, Mandinka, Bambara, Amharic, Oromo, Tigrigna,
  Berber, Egyptian Arabic, Lingala, Liberian, Kinyarwanda, Bemba, Chichewa,
  and more).

The data is shared with the Python package; both ship the same
`jokes.json` and `proverbs.json`.

---

## Contributing

Contributions are welcome — see
[CONTRIBUTING.md](https://github.com/daddysboy21/africanjokes/blob/main/CONTRIBUTING.md)
in the main repo. Data lives in `africanjokes/data/` (the canonical Python
copy); after editing, run `node tools/sync_data.mjs` to mirror the changes
into the npm package and validate.

---

## License

MIT — see [LICENSE](https://github.com/daddysboy21/africanjokes/blob/main/LICENSE).

**Author:** Morris D. Toclo · [github.com/daddysboy21](https://github.com/daddysboy21) · [daddysboy21.link](https://daddysboy21.link)
