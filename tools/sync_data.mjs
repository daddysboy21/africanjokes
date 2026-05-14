#!/usr/bin/env node
// Copy the canonical data files from africanjokes/data into npm/src/data
// and run the Python validator if it is available. Used by the npm
// package's `prepack` script and recommended after editing the data files.

import { copyFileSync, mkdirSync, existsSync } from "node:fs";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO = dirname(HERE);
const PY_DATA = join(REPO, "africanjokes", "data");
const NPM_DATA = join(REPO, "npm", "src", "data");

const FILES = ["jokes.json", "proverbs.json"];

function main() {
  if (!existsSync(PY_DATA)) {
    console.error(`sync_data: source directory missing: ${PY_DATA}`);
    process.exit(1);
  }
  mkdirSync(NPM_DATA, { recursive: true });

  for (const name of FILES) {
    const src = join(PY_DATA, name);
    const dst = join(NPM_DATA, name);
    copyFileSync(src, dst);
    console.log(`sync_data: copied ${name}`);
  }

  // Validate the canonical Python copy if Python is on PATH. We don't fail
  // sync just because Python isn't installed (the npm package may be built
  // in a Node-only CI lane).
  const py = spawnSync(
    process.platform === "win32" ? "python" : "python3",
    [join(REPO, "tools", "validate_data.py")],
    { stdio: "inherit" },
  );
  if (py.error && py.error.code === "ENOENT") {
    console.warn("sync_data: python not found on PATH, skipping validation.");
    return;
  }
  if (py.status !== 0) {
    console.error("sync_data: validator failed.");
    process.exit(py.status ?? 1);
  }
}

main();
