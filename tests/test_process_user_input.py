import pytest

from src.user_interface import UserInterface


@pytest.mark.parametrize("user_input", ["input", "", "29", "z", "a", "."])
def test_should_throw_an_exception_when_input_is_not_valid(user_input, monkeypatch):
    UserInterface()
    monkeypatch.setattr("builtins.input", lambda _: user_input)
