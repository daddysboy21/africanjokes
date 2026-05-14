import pytest

import africanjokes
from africanjokes import Joke


def test_get_joke_returns_str_subclass():
    joke = africanjokes.get_joke()
    assert isinstance(joke, str)
    assert isinstance(joke, Joke)
    assert joke.strip() == joke
    assert joke


def test_joke_has_country_and_themes():
    joke = africanjokes.get_joke()
    assert isinstance(joke.country, str) and joke.country
    assert isinstance(joke.themes, tuple) and len(joke.themes) >= 1
    assert all(isinstance(t, str) and t for t in joke.themes)


def test_get_joke_country_filter_is_case_insensitive():
    joke_lower = africanjokes.get_joke(country="nigeria")
    joke_mixed = africanjokes.get_joke(country="NiGeRiA")
    assert joke_lower.country == "Nigeria"
    assert joke_mixed.country == "Nigeria"


def test_get_joke_theme_filter():
    joke = africanjokes.get_joke(theme="power")
    assert "power" in (t.lower() for t in joke.themes)


def test_get_joke_combined_filters():
    joke = africanjokes.get_joke(country="Pan-African", theme="animals")
    assert joke.country == "Pan-African"
    assert "animals" in joke.themes


def test_get_joke_unknown_country_raises():
    with pytest.raises(LookupError):
        africanjokes.get_joke(country="Atlantis")


def test_get_joke_unknown_theme_raises():
    with pytest.raises(LookupError):
        africanjokes.get_joke(theme="quantum-physics")


def test_get_jokes_returns_n_distinct():
    jokes = africanjokes.get_jokes(5)
    assert len(jokes) == 5
    assert len({str(j) for j in jokes}) == 5


def test_get_jokes_caps_at_pool_size():
    jokes = africanjokes.get_jokes(99999, country="Egypt")
    egypt_pool_size = sum(1 for j in africanjokes.all_jokes() if j.country == "Egypt")
    assert len(jokes) == egypt_pool_size
    assert all(j.country == "Egypt" for j in jokes)


def test_get_jokes_invalid_n_raises():
    with pytest.raises(ValueError):
        africanjokes.get_jokes(0)
    with pytest.raises(ValueError):
        africanjokes.get_jokes(-3)


def test_all_jokes_returns_independent_list():
    a = africanjokes.all_jokes()
    b = africanjokes.all_jokes()
    assert a == b
    assert a is not b


def test_list_countries_includes_known_entries():
    countries = africanjokes.list_countries()
    for expected in ("Nigeria", "Ghana", "Kenya", "Liberia", "Pan-African"):
        assert expected in countries


def test_list_themes_includes_known_entries():
    themes = africanjokes.list_themes()
    for expected in ("power", "internet", "food", "family", "animals"):
        assert expected in themes


def test_list_countries_kind_all_is_superset():
    jokes_only = set(africanjokes.list_countries("jokes"))
    proverbs_only = set(africanjokes.list_countries("proverbs"))
    combined = set(africanjokes.list_countries("all"))
    assert jokes_only | proverbs_only == combined


def test_list_countries_invalid_kind_raises():
    with pytest.raises(ValueError):
        africanjokes.list_countries("oranges")
