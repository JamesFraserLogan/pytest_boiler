import pytest
import tomllib

from fib import fib, MAX_RECURSION


def test_upper_limit() -> None:
    with pytest.raises(ValueError):
        fib(MAX_RECURSION + 1)


def test_lower_limit() -> None:
    with pytest.raises(ValueError):
        fib(-1)


def test_values() -> None:
    with open("tests/fib.toml", "rb") as f:
        data = tomllib.load(f)
    test_list: list = data["FIRST_TEN"]
    for index, value in enumerate(test_list):
        assert value == fib(index)
