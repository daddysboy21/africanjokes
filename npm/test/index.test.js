import { describe, it } from "node:test";
import { strict as assert } from "node:assert";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

import {
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
} from "../src/index.js";

const HERE = dirname(fileURLToPath(import.meta.url));
const CLI_PATH = join(HERE, "..", "src", "cli.js");

describe("library API", () => {
  it("reports the expected version", () => {
    assert.equal(typeof version, "string");
    assert.match(version, /^\d+\.\d+\.\d+$/);
  });

  it("returns a Joke with text/country/themes", () => {
    const joke = getJoke();
    assert.ok(joke instanceof Joke);
    assert.equal(typeof joke.text, "string");
    assert.ok(joke.text.length > 0);
    assert.equal(typeof joke.country, "string");
    assert.ok(Array.isArray(joke.themes) && joke.themes.length >= 1);
  });

  it("Joke.toString returns the text", () => {
    const joke = getJoke();
    assert.equal(String(joke), joke.text);
    assert.equal(`${joke}`, joke.text);
  });

  it("filters by country (case-insensitive)", () => {
    const lower = getJoke({ country: "nigeria" });
    const mixed = getJoke({ country: "NiGeRiA" });
    assert.equal(lower.country, "Nigeria");
    assert.equal(mixed.country, "Nigeria");
  });

  it("filters by theme", () => {
    const joke = getJoke({ theme: "power" });
    assert.ok(joke.themes.some((t) => t.toLowerCase() === "power"));
  });

  it("combines country + theme filters", () => {
    const joke = getJoke({ country: "Pan-African", theme: "animals" });
    assert.equal(joke.country, "Pan-African");
    assert.ok(joke.themes.includes("animals"));
  });

  it("throws NoMatchError on unknown country", () => {
    assert.throws(() => getJoke({ country: "Atlantis" }), NoMatchError);
  });

  it("throws NoMatchError on unknown theme", () => {
    assert.throws(() => getJoke({ theme: "quantum-physics" }), NoMatchError);
  });

  it("getJokes returns n distinct entries", () => {
    const jokes = getJokes(5);
    assert.equal(jokes.length, 5);
    assert.equal(new Set(jokes.map(String)).size, 5);
  });

  it("getJokes caps at the matching pool size", () => {
    const egypt = allJokes().filter((j) => j.country === "Egypt");
    const jokes = getJokes(99999, { country: "Egypt" });
    assert.equal(jokes.length, egypt.length);
    assert.ok(jokes.every((j) => j.country === "Egypt"));
  });

  it("getJokes rejects non-positive n", () => {
    assert.throws(() => getJokes(0), RangeError);
    assert.throws(() => getJokes(-1), RangeError);
  });

  it("returns a Proverb with text/country/attribution", () => {
    const p = getProverb();
    assert.ok(p instanceof Proverb);
    assert.equal(typeof p.text, "string");
    assert.ok(p.text.length > 0);
    assert.equal(typeof p.country, "string");
    assert.equal(typeof p.attribution, "string");
  });

  it("getProverb filters by country (case-insensitive)", () => {
    const p = getProverb({ country: "ghana" });
    assert.equal(p.country, "Ghana");
  });

  it("getProverbs returns n distinct entries", () => {
    const ps = getProverbs(3, { country: "Nigeria" });
    assert.equal(ps.length, 3);
    assert.equal(new Set(ps.map(String)).size, 3);
    assert.ok(ps.every((p) => p.country === "Nigeria"));
  });

  it("listCountries('jokes') includes known entries", () => {
    const cs = listCountries("jokes");
    for (const c of ["Nigeria", "Ghana", "Kenya", "Liberia", "Pan-African"]) {
      assert.ok(cs.includes(c), `expected ${c}`);
    }
  });

  it("listCountries('all') is the union of jokes + proverbs", () => {
    const j = new Set(listCountries("jokes"));
    const p = new Set(listCountries("proverbs"));
    const all = new Set(listCountries("all"));
    assert.deepEqual(all, new Set([...j, ...p]));
  });

  it("listCountries throws on bad kind", () => {
    assert.throws(() => listCountries("oranges"), Error);
  });

  it("listThemes includes known entries", () => {
    const themes = listThemes();
    for (const t of ["power", "internet", "food", "family", "animals"]) {
      assert.ok(themes.includes(t), `expected theme ${t}`);
    }
  });

  it("allJokes / allProverbs return independent lists", () => {
    const a = allJokes();
    const b = allJokes();
    assert.equal(a.length, b.length);
    assert.notEqual(a, b);
  });
});

function runCli(...argv) {
  const r = spawnSync(process.execPath, [CLI_PATH, ...argv], {
    encoding: "utf8",
  });
  return { code: r.status, out: r.stdout, err: r.stderr };
}

describe("CLI", () => {
  it("--version prints the installed version", () => {
    const r = runCli("--version");
    assert.equal(r.code, 0);
    assert.ok(r.out.includes(version));
  });

  it("default prints a single joke", () => {
    const r = runCli();
    assert.equal(r.code, 0);
    assert.ok(r.out.trim().length > 0);
  });

  it("--proverb prints a proverb", () => {
    const r = runCli("--proverb");
    assert.equal(r.code, 0);
    const proverbTexts = new Set(allProverbs().map(String));
    assert.ok(proverbTexts.has(r.out.trim()));
  });

  it("--count N prints N lines", () => {
    const r = runCli("--count", "5");
    assert.equal(r.code, 0);
    const lines = r.out.split("\n").filter((l) => l.trim());
    assert.equal(lines.length, 5);
  });

  it("--country filters output", () => {
    const r = runCli("--count", "3", "--country", "Nigeria");
    assert.equal(r.code, 0);
    const ng = new Set(
      allJokes().filter((j) => j.country === "Nigeria").map(String),
    );
    for (const line of r.out.split("\n").filter((l) => l.trim())) {
      assert.ok(ng.has(line), `unexpected line: ${line}`);
    }
  });

  it("unknown country exits non-zero with stderr message", () => {
    const r = runCli("--country", "Atlantis");
    assert.equal(r.code, 1);
    assert.ok(r.err.includes("Atlantis"));
    assert.equal(r.out, "");
  });

  it("--metadata includes country in the output", () => {
    const r = runCli("--country", "Ghana", "--metadata");
    assert.equal(r.code, 0);
    assert.ok(r.out.includes("Ghana"));
  });

  it("--list-countries lists known countries", () => {
    const r = runCli("--list-countries");
    assert.equal(r.code, 0);
    const set = new Set(r.out.split("\n").map((l) => l.trim()).filter(Boolean));
    assert.ok(set.has("Nigeria"));
    assert.ok(set.has("Pan-African"));
  });

  it("--list-themes lists known themes", () => {
    const r = runCli("--list-themes");
    assert.equal(r.code, 0);
    const set = new Set(r.out.split("\n").map((l) => l.trim()).filter(Boolean));
    assert.ok(set.has("power"));
    assert.ok(set.has("internet"));
  });

  it("invalid --count exits 2", () => {
    const r = runCli("--count", "0");
    assert.equal(r.code, 2);
    assert.ok(r.err.toLowerCase().includes("count"));
  });

  it("--proverb with --theme warns but succeeds", () => {
    const r = runCli("--proverb", "--theme", "power");
    assert.equal(r.code, 0);
    assert.ok(r.err.toLowerCase().includes("theme"));
    assert.ok(r.out.trim().length > 0);
  });
});
