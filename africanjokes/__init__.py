import random
import importlib.resources


def get_joke():
    jokes_path = importlib.resources.files("africanjokes") / "jokes.txt"
    with jokes_path.open(encoding="utf-8") as f:
        jokes = f.readlines()
    return random.choice(jokes).strip()
