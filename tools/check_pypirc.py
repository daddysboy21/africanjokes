"""Verify $HOME/.pypirc is well-formed and ready to publish, without echoing the token."""

import os
from configparser import ConfigParser

PLACEHOLDER = "REPLACE-WITH-YOUR-pypi-TOKEN"
PATH = os.path.expanduser("~/.pypirc")


def main() -> int:
    if not os.path.exists(PATH):
        print(f"NOT OK: {PATH} does not exist")
        return 1

    # Notepad on Windows saves UTF-8 with BOM by default, which breaks twine's
    # configparser. Detect and strip the BOM in place if present.
    with open(PATH, "rb") as f:
        raw = f.read()
    if raw.startswith(b"\xef\xbb\xbf"):
        with open(PATH, "wb") as f:
            f.write(raw[3:])
        print("note: stripped UTF-8 BOM from .pypirc (Notepad adds it on save)")

    c = ConfigParser()
    c.read(PATH, encoding="utf-8")

    has_section = c.has_section("pypi")
    user = c.get("pypi", "username", fallback="")
    pw = c.get("pypi", "password", fallback="")

    print(f"file: {PATH}")
    print(f"size: {os.path.getsize(PATH)} bytes")
    print(f"section [pypi] present: {has_section}")
    print(f"username value: {user!r}")
    print(f"password present: {bool(pw)}")
    print(f"password length: {len(pw)}")
    print(f"password starts with 'pypi-': {pw.startswith('pypi-')}")
    print(f"password is still the placeholder: {pw == PLACEHOLDER}")

    ok = (
        has_section
        and user == "__token__"
        and pw.startswith("pypi-")
        and pw != PLACEHOLDER
    )
    print(f"VERDICT: {'OK -- ready to publish' if ok else 'NOT OK -- update .pypirc'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
