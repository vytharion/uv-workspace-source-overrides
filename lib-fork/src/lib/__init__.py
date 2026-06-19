"""Forked producer package — same import path, FORK-tagged payload."""


def greet(name: str) -> str:
    """Fork-distinguishing greeting; same signature as the workspace lib."""
    return f"Hello from lib (FORK), {name}!"


__all__ = ["greet"]
