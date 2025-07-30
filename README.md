# africanjokes 🌍

[![PyPI version](https://img.shields.io/pypi/v/africanjokes)](https://pypi.org/project/africanjokes/)
[![Downloads](https://img.shields.io/pepy/dt/africanjokes)](https://pepy.tech/project/africanjokes)
[![GitHub Actions Status](https://github.com/daddysboy21/africanjokes/actions/workflows/python-app.yml/badge.svg)](https://github.com/daddysboy21/africanjokes/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/africanjokes)](https://pypi.org/project/africanjokes/)
[![GitHub Stars](https://img.shields.io/github/stars/daddysboy21/africanjokes?style=social)](https://github.com/daddysboy21/africanjokes/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/daddysboy21/africanjokes)](https://github.com/daddysboy21/africanjokes/commits)
[![Open Issues](https://img.shields.io/github/issues/daddysboy21/africanjokes)](https://github.com/daddysboy21/africanjokes/issues)


**africanjokes** is a simple, lightweight Python library that delivers random African jokes —  
because every coder deserves a laugh, especially from the Motherland.  
Spread joy, lighten up your day, and code with a smile! 😄

---

---

## 📚 Table of Contents

- [Installation](#-installation)
- [What is africanjokes?](#-what-is-africanjokes)
- [Quickstart](#-quickstart)
- [Contributing](#️-contributing)
- [License](#-license)
- [Author](#-author)
- [Connect with Me](#-connect-with-me)
- [Support & Spread Laughter](#-support--spread-laughter)

---

## 📦 Installation

Get started instantly with pip:

```bash
pip install africanjokes
```

---

## 🤔 What is africanjokes?

`africanjokes` brings the vibrant humor of Africa right into your terminal, scripts, bots, or applications.

**Perfect for:**
- Coding sessions 👨‍💻
- Presentations 🗣️
- Discord/Telegram bots 🤖
- Slack integrations 💬
- Daily CLI jokes ☀️

Whether you're looking to break the ice or just need a pick-me-up, africanjokes has you covered!

---

## 🚀 Quickstart

### Use in Python

```python
import africanjokes

joke = africanjokes.get_joke()
print(joke)
```

### Use from Command Line

```bash
africanjokes --joke
```

Get a new random African joke every time you run it!

---

## 🖥️ CLI Usage

africanjokes comes with a handy command-line interface.

### Commands

- `--joke` or `-j`  
  Output a random African joke.

- `--version` or `-v`  
  Show the current africanjokes version.

- `--help` or `-h`  
  Display help message and usage.

### Example Output

```bash
$ africanjokes --joke
Why did the chicken cross the road in Lagos? To buy suya on the other side!

$ africanjokes --version
africanjokes version 1.0.0

$ africanjokes --help
Usage: africanjokes [OPTIONS]
Options:
  --joke, -j      Show a random African joke
  --version, -v   Show version info
  --help, -h      Show this help message
```

---

## 👀 Preview

Here’s what you get when you use africanjokes:

```python
import africanjokes

print(africanjokes.get_joke())
# Output: Why did the goat refuse to leave the party? Because it was the G.O.A.T!
```

---

## 🐍 Python Version Compatibility

africanjokes supports:

- Python 3.7+
- Works on Windows, macOS, and Linux

---

## 🤖 CLI Testing Automation

CLI commands are tested automatically using [pytest](https://pytest.org/) and [pytest-console-scripts](https://github.com/manahl/pytest-plugins/tree/master/pytest-console-scripts).

Example test (see `tests/test_cli.py`):

```python
def test_cli_joke(script_runner):
    result = script_runner.run('africanjokes', '--joke')
    assert result.success
    assert "Why" in result.stdout 
```

---

## 🛠️ Contributing

Got a great African joke to share?  
Help us keep the laughter flowing — contributions are welcome!

1. **Fork** the repo  
2. **Add** your joke  
3. **Submit** a PR  

See [`CONTRIBUTING wiki`](https://github.com/daddysboy21/africanjokes/wiki/Contributing) for full details.

---

## 📄 License

This project is licensed under the [`MIT License`](https://github.com/daddysboy21/africanjokes/blob/main/LICENSE)
 — free to use, modify, and distribute.

---

## 👤 Author

**`Morris D. Toclo`**  
Co-Founder & Co-CEO of LoneScore  
Student — BlueCrest University College Liberia  
Monrovia, Liberia `🇱🇷`

---

## 🌐 Connect with Me

- [`Website`](https://daddysboy21.link)
- [`GitHub`](https://github.com/daddysboy21)
- [`LinkedIn`](https://www.linkedin.com/in/morris-toclo-a83858275)
- [`X (Twitter)`](https://x.com/daddysboy_21)
- [`Twitch`](https://twitch.tv/daddysboy_21)
- [`Instagram`](https://instagram.com/daddysboy.21)
- [`TikTok`](https://tiktok.com/@daddysboy.21)
- [`WhatsApp`](https://wa.me/231555557034)
- [`Buy Me a Coffee`](https://buymeacoffee.com/PBEzMY14YC)
- [`Gravatar`](https://daddysboy21.link)

---

## 💖 Support & Spread Laughter

If you enjoy using africanjokes, please:

- ⭐ Star the repo  
- 🛠️ Contribute your own jokes  
- ☕ [`Buy Me a Coffee`](https://buymeacoffee.com/PBEzMY14YC)  
- 📣 Share it with your community  

Let’s spread African joy — one joke at a time.  
**`Made with ❤️ in Africa.`**

---
