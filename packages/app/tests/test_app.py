from app import run


def test_run_includes_name() -> None:
    assert "vytharion" in run("vytharion")
