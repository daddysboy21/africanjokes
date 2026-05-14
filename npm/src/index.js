// africanjokes — JavaScript companion to the Python package.
//
// Public API (mirrors the Python module):
//   getJoke({ country, theme })            -> Joke
//   getJokes(n, { country, theme })        -> Joke[]
//   getProverb({ country })                -> Proverb
//   getProverbs(n, { country })            -> Proverb[]
//   allJokes()                             -> Joke[]
//   allProverbs()                          -> Proverb[]
//   listCountries(kind = "jokes"|"proverbs"|"all") -> string[]
//   listThemes()                           -> string[]
//   version                                -> "1.2.0"
//
// Joke and Proverb instances are plain objects with .text, .country, plus
// .themes (jokes) or .attribution (proverbs). They also implement
// .toString() so `String(joke)` / template literals print just the text.

import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

export const version = "1.2.0";

const HERE = dirname(fileURLToPath(import.meta.url));
const DATA_DIR = join(HERE, "data");

let _jokesCache = null;
let _proverbsCache = null;

function loadJSON(filename) {
  const path = join(DATA_DIR, filename);
  return JSON.parse(readFileSync(path, "utf8"));
}

function loadJokes() {
  if (_jokesCache !== null) return _jokesCache;
  const data = loadJSON("jokes.json");
  _jokesCache = data.jokes.map(
    (j) => new Joke(j.text, j.country, Object.freeze([...j.themes])),
  );
  return _jokesCache;
}

function loadProverbs() {
  if (_proverbsCache !== null) return _proverbsCache;
  const data = loadJSON("proverbs.json");
  _proverbsCache = data.proverbs.map(
    (p) => new Proverb(p.text, p.country, p.attribution),
  );
  return _proverbsCache;
}

export class Joke {
  constructor(text, country, themes) {
    this.text = text;
    this.country = country;
    this.themes = themes;
  }
  toString() {
    return this.text;
  }
}

export class Proverb {
  constructor(text, country, attribution) {
    this.text = text;
    this.country = country;
    this.attribution = attribution;
  }
  toString() {
    return this.text;
  }
}

class NoMatchError extends Error {
  constructor(message) {
    super(message);
    this.name = "NoMatchError";
  }
}

function pickRandom(pool) {
  return pool[Math.floor(Math.random() * pool.length)];
}

function sampleWithoutReplacement(pool, n) {
  if (n >= pool.length) {
    const shuffled = [...pool];
    for (let i = shuffled.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [shuffled[i], shuffled[j]] = [shuffled[j], shuffled[i]];
    }
    return shuffled;
  }
  const indices = new Set();
  while (indices.size < n) indices.add(Math.floor(Math.random() * pool.length));
  return [...indices].map((i) => pool[i]);
}

function ciEquals(a, b) {
  return a.toLowerCase() === b.toLowerCase();
}

function filterJokes({ country, theme } = {}) {
  let pool = loadJokes();
  if (country) pool = pool.filter((j) => ciEquals(j.country, country));
  if (theme) pool = pool.filter((j) => j.themes.some((t) => ciEquals(t, theme)));
  return pool;
}

function filterProverbs({ country } = {}) {
  let pool = loadProverbs();
  if (country) pool = pool.filter((p) => ciEquals(p.country, country));
  return pool;
}

function noMatch(kind, { country, theme } = {}) {
  const parts = [];
  if (country) parts.push(`country=${JSON.stringify(country)}`);
  if (theme) parts.push(`theme=${JSON.stringify(theme)}`);
  const suffix = parts.length ? ` (${parts.join(", ")})` : "";
  return new NoMatchError(`No ${kind} found${suffix}.`);
}

export function getJoke({ country, theme } = {}) {
  const pool = filterJokes({ country, theme });
  if (pool.length === 0) throw noMatch("joke", { country, theme });
  return pickRandom(pool);
}

export function getJokes(n = 1, { country, theme } = {}) {
  if (!Number.isInteger(n) || n < 1) {
    throw new RangeError("n must be a positive integer");
  }
  const pool = filterJokes({ country, theme });
  if (pool.length === 0) throw noMatch("joke", { country, theme });
  return sampleWithoutReplacement(pool, n);
}

export function getProverb({ country } = {}) {
  const pool = filterProverbs({ country });
  if (pool.length === 0) throw noMatch("proverb", { country });
  return pickRandom(pool);
}

export function getProverbs(n = 1, { country } = {}) {
  if (!Number.isInteger(n) || n < 1) {
    throw new RangeError("n must be a positive integer");
  }
  const pool = filterProverbs({ country });
  if (pool.length === 0) throw noMatch("proverb", { country });
  return sampleWithoutReplacement(pool, n);
}

export function allJokes() {
  return [...loadJokes()];
}

export function allProverbs() {
  return [...loadProverbs()];
}

export function listCountries(kind = "jokes") {
  const k = kind.toLowerCase();
  if (k === "jokes") {
    return [...new Set(loadJokes().map((j) => j.country))].sort();
  }
  if (k === "proverbs") {
    return [...new Set(loadProverbs().map((p) => p.country))].sort();
  }
  if (k === "all") {
    return [
      ...new Set([
        ...loadJokes().map((j) => j.country),
        ...loadProverbs().map((p) => p.country),
      ]),
    ].sort();
  }
  throw new Error(
    `kind must be "jokes", "proverbs", or "all", got ${JSON.stringify(kind)}`,
  );
}

export function listThemes() {
  const themes = new Set();
  for (const j of loadJokes()) for (const t of j.themes) themes.add(t);
  return [...themes].sort();
}

export { NoMatchError };

export default {
  version,
  Joke,
  Proverb,
  NoMatchError,
  getJoke,
  getJokes,
  getProverb,
  getProverbs,
  allJokes,
  allProverbs,
  listCountries,
  listThemes,
};
