"""africanjokes — a small Python library of African jokes and proverbs.

The public API is intentionally small:

    >>> import africanjokes
    >>> africanjokes.get_joke()                       # random joke (any country)
    >>> africanjokes.get_joke(country="Nigeria")      # filter by country
    >>> africanjokes.get_joke(theme="power")          # filter by theme
    >>> africanjokes.get_jokes(5)                     # five distinct random jokes
    >>> africanjokes.get_proverb()                    # random African proverb
    >>> africanjokes.get_proverb(country="Ghana")
    >>> africanjokes.list_countries()                 # countries that have jokes
    >>> africanjokes.list_themes()                    # joke themes

`Joke` and `Proverb` are subclasses of `str`, so they print and concatenate as
plain strings while still exposing `.country`, `.themes` (jokes — a tuple of
tags), and `.attribution` (proverbs) for callers that want the metadata.
"""

from __future__ import annotations

import importlib.resources
import json
import random as _random
from typing import List, Optional, Tuple

__version__ = "1.2.0"

__all__ = [
    "Joke",
    "Proverb",
    "get_joke",
    "get_jokes",
    "get_proverb",
    "get_proverbs",
    "all_jokes",
    "all_proverbs",
    "list_countries",
    "list_themes",
    "__version__",
]


class Joke(str):
    """A joke. Behaves like its text (str subclass) and carries country/themes metadata.

    ``themes`` is a tuple of one or more theme tags (e.g. ``("animals", "internet")``).
    """

    country: str
    themes: Tuple[str, ...]

    def __new__(cls, text: str, country: str, themes) -> "Joke":
        instance = super().__new__(cls, text)
        instance.country = country
        instance.themes = tuple(themes)
        return instance

    def __repr__(self) -> str:
        return (
            f"Joke(text={str.__repr__(self)}, "
            f"country={self.country!r}, themes={self.themes!r})"
        )


class Proverb(str):
    """An African proverb. Str subclass with country and attribution metadata.

    ``attribution`` names the people / language group the proverb is traditionally
    associated with (for example ``"Yoruba"``, ``"Akan"``, ``"Swahili"``).
    """

    country: str
    attribution: str

    def __new__(cls, text: str, country: str, attribution: str) -> "Proverb":
        instance = super().__new__(cls, text)
        instance.country = country
        instance.attribution = attribution
        return instance

    def __repr__(self) -> str:
        return (
            f"Proverb(text={str.__repr__(self)}, "
            f"country={self.country!r}, attribution={self.attribution!r})"
        )


_jokes_cache: Optional[List[Joke]] = None
_proverbs_cache: Optional[List[Proverb]] = None


def _load_data(filename: str) -> dict:
    data_path = importlib.resources.files("africanjokes.data") / filename
    with data_path.open(encoding="utf-8") as f:
        return json.load(f)


def _all_jokes_internal() -> List[Joke]:
    global _jokes_cache
    if _jokes_cache is None:
        data = _load_data("jokes.json")
        _jokes_cache = [
            Joke(j["text"], j["country"], j.get("themes", []))
            for j in data["jokes"]
        ]
    return _jokes_cache


def _all_proverbs_internal() -> List[Proverb]:
    global _proverbs_cache
    if _proverbs_cache is None:
        data = _load_data("proverbs.json")
        _proverbs_cache = [
            Proverb(p["text"], p["country"], p["attribution"]) for p in data["proverbs"]
        ]
    return _proverbs_cache


def all_jokes() -> List[Joke]:
    """Return a fresh list containing every joke."""
    return list(_all_jokes_internal())


def all_proverbs() -> List[Proverb]:
    """Return a fresh list containing every proverb."""
    return list(_all_proverbs_internal())


def _filter_jokes(country: Optional[str], theme: Optional[str]) -> List[Joke]:
    jokes = _all_jokes_internal()
    if country:
        c = country.strip().lower()
        jokes = [j for j in jokes if j.country.lower() == c]
    if theme:
        t = theme.strip().lower()
        jokes = [j for j in jokes if any(tag.lower() == t for tag in j.themes)]
    return jokes


def _filter_proverbs(country: Optional[str]) -> List[Proverb]:
    proverbs = _all_proverbs_internal()
    if country:
        c = country.strip().lower()
        proverbs = [p for p in proverbs if p.country.lower() == c]
    return proverbs


def _no_match(country: Optional[str], theme: Optional[str], kind: str) -> str:
    parts = []
    if country:
        parts.append(f"country={country!r}")
    if theme:
        parts.append(f"theme={theme!r}")
    suffix = " (" + ", ".join(parts) + ")" if parts else ""
    return f"No {kind} found{suffix}."


def get_joke(country: Optional[str] = None, theme: Optional[str] = None) -> Joke:
    """Return a random joke, optionally filtered by country and/or theme.

    Both filters are case-insensitive. Raises LookupError if no joke matches.
    """
    pool = _filter_jokes(country, theme)
    if not pool:
        raise LookupError(_no_match(country, theme, "joke"))
    return _random.choice(pool)


def get_jokes(
    n: int = 1,
    country: Optional[str] = None,
    theme: Optional[str] = None,
) -> List[Joke]:
    """Return ``n`` distinct random jokes (without replacement).

    If ``n`` exceeds the matching pool size, the entire matching pool is
    returned in shuffled order. Raises ValueError if ``n < 1`` and LookupError
    if no jokes match the filters.
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    pool = _filter_jokes(country, theme)
    if not pool:
        raise LookupError(_no_match(country, theme, "joke"))
    if n >= len(pool):
        shuffled = list(pool)
        _random.shuffle(shuffled)
        return shuffled
    return _random.sample(pool, n)


def get_proverb(country: Optional[str] = None) -> Proverb:
    """Return a random African proverb, optionally filtered by country."""
    pool = _filter_proverbs(country)
    if not pool:
        raise LookupError(_no_match(country, None, "proverb"))
    return _random.choice(pool)


def get_proverbs(n: int = 1, country: Optional[str] = None) -> List[Proverb]:
    """Return ``n`` distinct random proverbs (without replacement)."""
    if n < 1:
        raise ValueError("n must be >= 1")
    pool = _filter_proverbs(country)
    if not pool:
        raise LookupError(_no_match(country, None, "proverb"))
    if n >= len(pool):
        shuffled = list(pool)
        _random.shuffle(shuffled)
        return shuffled
    return _random.sample(pool, n)


def list_countries(kind: str = "jokes") -> List[str]:
    """Return a sorted list of unique countries.

    ``kind`` is one of ``"jokes"`` (default), ``"proverbs"``, or ``"all"``.
    """
    k = kind.lower()
    if k == "jokes":
        return sorted({j.country for j in _all_jokes_internal()})
    if k == "proverbs":
        return sorted({p.country for p in _all_proverbs_internal()})
    if k == "all":
        return sorted(
            {j.country for j in _all_jokes_internal()}
            | {p.country for p in _all_proverbs_internal()}
        )
    raise ValueError(f"kind must be 'jokes', 'proverbs', or 'all', got {kind!r}")


def list_themes() -> List[str]:
    """Return a sorted list of unique joke themes (flattened across all jokes)."""
    return sorted({tag for j in _all_jokes_internal() for tag in j.themes})
