import pytest

from src.user_interface import InvalidOption, UserInterface


@pytest.mark.parametrize("user_input", ["input", "", "29", "z", "a", "."])
def test_should_return_throw_an_exception_when_input_is_not_valid(user_input):
    ui = UserInterface()
    with pytest.raises(InvalidOption):
        ui.process_user_input(user_input)


@pytest.mark.parametrize("user_input", ["1", "2", "3", "4", "5"])
def test_should_return_true_for_valid_menu_options(user_input):
    ui = UserInterface()
    assert ui.process_user_input(user_input)


def test_should_return_false_for_user_input_equal_to_0():
    user_input = "0"
    ui = UserInterface()
    assert not ui.process_user_input(user_input)
