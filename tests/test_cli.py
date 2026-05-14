import africanjokes
from africanjokes.cli import main


def _run(capsys, *argv):
    code = main(list(argv))
    captured = capsys.readouterr()
    return code, captured.out, captured.err


def test_default_prints_a_joke(capsys):
    code, out, err = _run(capsys)
    assert code == 0
    assert err == ""
    assert out.strip()


def test_joke_flag_prints_a_joke(capsys):
    code, out, _ = _run(capsys, "--joke")
    assert code == 0
    assert out.strip()


def test_proverb_flag_prints_a_proverb(capsys):
    code, out, _ = _run(capsys, "--proverb")
    assert code == 0
    text = out.strip()
    assert text
    assert text in (str(p) for p in africanjokes.all_proverbs())


def test_count_returns_n_lines(capsys):
    code, out, _ = _run(capsys, "--count", "5")
    assert code == 0
    assert len([line for line in out.splitlines() if line.strip()]) == 5


def test_country_filter(capsys):
    code, out, _ = _run(capsys, "--count", "3", "--country", "Nigeria")
    assert code == 0
    nigerian = {str(j) for j in africanjokes.all_jokes() if j.country == "Nigeria"}
    for line in out.splitlines():
        assert line.strip() in nigerian


def test_unknown_country_exits_nonzero(capsys):
    code, out, err = _run(capsys, "--country", "Atlantis")
    assert code == 1
    assert "Atlantis" in err
    assert out == ""


def test_metadata_flag_includes_country(capsys):
    code, out, _ = _run(capsys, "--country", "Ghana", "--metadata")
    assert code == 0
    assert "Ghana" in out


def test_list_countries(capsys):
    code, out, _ = _run(capsys, "--list-countries")
    assert code == 0
    countries = {line.strip() for line in out.splitlines() if line.strip()}
    assert "Nigeria" in countries
    assert "Pan-African" in countries


def test_list_themes(capsys):
    code, out, _ = _run(capsys, "--list-themes")
    assert code == 0
    themes = {line.strip() for line in out.splitlines() if line.strip()}
    assert "power" in themes
    assert "internet" in themes


def test_list_proverb_countries(capsys):
    code, out, _ = _run(capsys, "--list-proverb-countries")
    assert code == 0
    countries = {line.strip() for line in out.splitlines() if line.strip()}
    assert "Ghana" in countries
    assert "Nigeria" in countries


def test_version(capsys):
    code, out, _ = _run(capsys, "--version")
    assert code == 0
    assert africanjokes.__version__ in out


def test_invalid_count(capsys):
    code, _, err = _run(capsys, "--count", "0")
    assert code == 2
    assert "count" in err.lower()


def test_theme_with_proverb_warns_but_succeeds(capsys):
    code, out, err = _run(capsys, "--proverb", "--theme", "power")
    assert code == 0
    assert "theme" in err.lower()
    assert out.strip()
