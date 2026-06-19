from app import run


def test_run_includes_name() -> None:
    assert "vytharion" in run("vytharion")


def test_run_delegates_to_lib() -> None:
    # The "Hello from lib" prefix is owned by lib.greet — proves cross-package
    # resolution worked end-to-end.
    out = run("anyone")
    assert "Hello from lib" in out
    assert out.startswith("[app]")
