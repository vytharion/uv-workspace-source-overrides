from lib import greet


def test_greet_includes_name() -> None:
    assert "vytharion" in greet("vytharion")


def test_greet_says_hello() -> None:
    assert greet("anyone").startswith("Hello from lib")
