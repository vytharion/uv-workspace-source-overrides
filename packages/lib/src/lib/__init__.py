"""Producer package — exposes greet()."""


def greet(name: str) -> str:
    """Return a workspace-friendly greeting."""
    return f"Hello from lib, {name}!"


__all__ = ["greet"]
