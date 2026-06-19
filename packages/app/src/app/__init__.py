"""Consumer package — delegates to lib.greet."""

from lib import greet


def run(name: str) -> str:
    """Wrap lib.greet so callers see app's banner before lib's payload."""
    return f"[app] {greet(name)}"


__all__ = ["run"]
