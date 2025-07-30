import random
import os

def get_joke():
    jokes_path = os.path.join(os.path.dirname(__file__), "jokes.txt")
    with open(jokes_path, "r", encoding="utf-8") as f:
        jokes = f.readlines()
    return random.choice(jokes).strip()