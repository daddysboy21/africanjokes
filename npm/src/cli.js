#!/usr/bin/env node
// africanjokes CLI — JavaScript companion. Mirrors the Python CLI flags.

import { parseArgs } from "node:util";
import {
  version,
  getJokes,
  getProverbs,
  listCountries,
  listThemes,
} from "./index.js";

const USAGE = `Usage: africanjokes [options]

Options:
  -j, --joke                     Print a random joke (default).
  -p, --proverb                  Print a random African proverb.
  -c, --country NAME             Filter to jokes/proverbs from a country.
  -t, --theme NAME               Filter jokes by theme. (Ignored for proverbs.)
  -n, --count N                  Print N items (default: 1).
      --metadata                 Show country/theme alongside each item.
      --list-countries           List all countries that have jokes.
      --list-proverb-countries   List all countries that have proverbs.
      --list-themes              List all joke themes.
  -v, --version                  Print the installed version.
  -h, --help                     Show this message and exit.
`;

function formatJoke(joke, withMetadata) {
  if (!withMetadata) return joke.text;
  const themes = joke.themes.length ? joke.themes.join(", ") : "—";
  return `${joke.text}  [${joke.country} · ${themes}]`;
}

function formatProverb(proverb, withMetadata) {
  if (!withMetadata) return proverb.text;
  return `${proverb.text}  [${proverb.country} · ${proverb.attribution}]`;
}

function fail(message, code = 1) {
  process.stderr.write(`africanjokes: ${message}\n`);
  process.exit(code);
}

export function main(argv = process.argv.slice(2)) {
  let parsed;
  try {
    parsed = parseArgs({
      args: argv,
      options: {
        joke: { type: "boolean", short: "j" },
        proverb: { type: "boolean", short: "p" },
        country: { type: "string", short: "c" },
        theme: { type: "string", short: "t" },
        count: { type: "string", short: "n", default: "1" },
        metadata: { type: "boolean" },
        "list-countries": { type: "boolean" },
        "list-proverb-countries": { type: "boolean" },
        "list-themes": { type: "boolean" },
        version: { type: "boolean", short: "v" },
        help: { type: "boolean", short: "h" },
      },
      strict: true,
      allowPositionals: false,
    });
  } catch (err) {
    fail(err.message, 2);
  }

  const opts = parsed.values;

  if (opts.help) {
    process.stdout.write(USAGE);
    return 0;
  }
  if (opts.version) {
    process.stdout.write(`africanjokes ${version}\n`);
    return 0;
  }
  if (opts["list-countries"]) {
    for (const c of listCountries("jokes")) process.stdout.write(`${c}\n`);
    return 0;
  }
  if (opts["list-proverb-countries"]) {
    for (const c of listCountries("proverbs")) process.stdout.write(`${c}\n`);
    return 0;
  }
  if (opts["list-themes"]) {
    for (const t of listThemes()) process.stdout.write(`${t}\n`);
    return 0;
  }

  const count = Number.parseInt(opts.count, 10);
  if (!Number.isFinite(count) || count < 1) {
    fail("--count must be a positive integer.", 2);
  }

  const modeFlags = [opts.joke, opts.proverb].filter(Boolean).length;
  if (modeFlags > 1) fail("--joke and --proverb are mutually exclusive.", 2);

  try {
    if (opts.proverb) {
      if (opts.theme) {
        process.stderr.write(
          "africanjokes: --theme has no effect on proverbs.\n",
        );
      }
      const items = getProverbs(count, { country: opts.country });
      for (const p of items) {
        process.stdout.write(`${formatProverb(p, opts.metadata)}\n`);
      }
    } else {
      const items = getJokes(count, {
        country: opts.country,
        theme: opts.theme,
      });
      for (const j of items) {
        process.stdout.write(`${formatJoke(j, opts.metadata)}\n`);
      }
    }
  } catch (err) {
    fail(err.message);
  }

  return 0;
}

const isMain = import.meta.url === `file://${process.argv[1].replace(/\\/g, "/")}`
  || process.argv[1]?.endsWith("cli.js")
  || process.argv[1]?.endsWith("africanjokes");

if (isMain) {
  main();
}
