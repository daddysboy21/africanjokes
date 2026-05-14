// Type declarations for the africanjokes npm package.

export const version: string;

export interface JokeFilters {
  country?: string;
  theme?: string;
}

export interface ProverbFilters {
  country?: string;
}

export class Joke {
  constructor(text: string, country: string, themes: readonly string[]);
  readonly text: string;
  readonly country: string;
  readonly themes: readonly string[];
  toString(): string;
}

export class Proverb {
  constructor(text: string, country: string, attribution: string);
  readonly text: string;
  readonly country: string;
  readonly attribution: string;
  toString(): string;
}

export class NoMatchError extends Error {
  readonly name: "NoMatchError";
}

/** Return a single random joke, optionally filtered by country and/or theme. */
export function getJoke(filters?: JokeFilters): Joke;

/**
 * Return `n` distinct random jokes (without replacement). If `n` exceeds the
 * matching pool, the entire pool is returned in shuffled order.
 */
export function getJokes(n?: number, filters?: JokeFilters): Joke[];

/** Return a single random African proverb, optionally filtered by country. */
export function getProverb(filters?: ProverbFilters): Proverb;

/** Return `n` distinct random proverbs (without replacement). */
export function getProverbs(n?: number, filters?: ProverbFilters): Proverb[];

/** Return the full list of jokes (a fresh array). */
export function allJokes(): Joke[];

/** Return the full list of proverbs (a fresh array). */
export function allProverbs(): Proverb[];

/**
 * Return the sorted list of countries.
 * @param kind one of `"jokes"` (default), `"proverbs"`, or `"all"`.
 */
export function listCountries(kind?: "jokes" | "proverbs" | "all"): string[];

/** Return the sorted list of joke themes. */
export function listThemes(): string[];

declare const _default: {
  version: string;
  Joke: typeof Joke;
  Proverb: typeof Proverb;
  NoMatchError: typeof NoMatchError;
  getJoke: typeof getJoke;
  getJokes: typeof getJokes;
  getProverb: typeof getProverb;
  getProverbs: typeof getProverbs;
  allJokes: typeof allJokes;
  allProverbs: typeof allProverbs;
  listCountries: typeof listCountries;
  listThemes: typeof listThemes;
};
export default _default;
