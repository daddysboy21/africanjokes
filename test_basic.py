import africanjokes

def test_get_joke_returns_string():
    joke = africanjokes.get_joke()
    assert isinstance(joke, str)
    assert joke
    