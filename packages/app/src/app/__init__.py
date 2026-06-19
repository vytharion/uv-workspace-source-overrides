"""Consumer package — exposes run() entrypoint."""


def run(name: str) -> str:
    """Lesson 1 placeholder; later lessons delegate to lib.greet."""
    return f"Hello from app, {name}!"


__all__ = ["run"]
