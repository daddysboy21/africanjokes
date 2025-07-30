import random
import importlib.resources

def get_joke():
    with importlib.resources.open_text(
        "africanjokes", "jokes.txt", encoding="utf-8"
    ) as f:
        jokes = f.readlines()
    return random.choice(jokes).strip()
