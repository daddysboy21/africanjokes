import pytest

import africanjokes
from africanjokes import Proverb


def test_get_proverb_returns_str_subclass():
    proverb = africanjokes.get_proverb()
    assert isinstance(proverb, str)
    assert isinstance(proverb, Proverb)
    assert proverb


def test_proverb_has_country_and_attribution():
    proverb = africanjokes.get_proverb()
    assert isinstance(proverb.country, str) and proverb.country
    assert isinstance(proverb.attribution, str) and proverb.attribution


def test_get_proverb_country_filter():
    proverb = africanjokes.get_proverb(country="Ghana")
    assert proverb.country == "Ghana"


def test_get_proverb_country_filter_case_insensitive():
    proverb = africanjokes.get_proverb(country="ghana")
    assert proverb.country == "Ghana"


def test_get_proverb_unknown_country_raises():
    with pytest.raises(LookupError):
        africanjokes.get_proverb(country="Atlantis")


def test_get_proverbs_returns_n_distinct():
    proverbs = africanjokes.get_proverbs(3, country="Nigeria")
    assert len(proverbs) == 3
    assert len({str(p) for p in proverbs}) == 3
    assert all(p.country == "Nigeria" for p in proverbs)


def test_get_proverbs_caps_at_pool_size():
    proverbs = africanjokes.get_proverbs(99999, country="DRC")
    assert all(p.country == "DRC" for p in proverbs)
    assert len(proverbs) == sum(1 for p in africanjokes.all_proverbs() if p.country == "DRC")


def test_get_proverbs_invalid_n_raises():
    with pytest.raises(ValueError):
        africanjokes.get_proverbs(0)


def test_all_proverbs_returns_independent_list():
    a = africanjokes.all_proverbs()
    b = africanjokes.all_proverbs()
    assert a == b
    assert a is not b
