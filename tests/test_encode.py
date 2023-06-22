import pytest

from src.encoder import CaesarEncryptor, NonAsciiCharacter


@pytest.mark.parametrize("char", ["ś", "ź", "ó", "ü", "ö", "ひ", "な", "â", "û"])
def test_should_throw_non_ascii_character_exception_if_non_ascii_character_is_provided(
    char,
):
    with pytest.raises(NonAsciiCharacter):
        CaesarEncryptor.encode(char, "0")


@pytest.mark.parametrize(
    "shift", ["1.5", "integer", "word", "f", "ghgh", "0.1.3", "-5.0", "3000.5"]
)
def test_should_throw_value_error_exception_if_shift_is_not_integer(shift):
    with pytest.raises(ValueError):
        CaesarEncryptor.encode("a", shift)


@pytest.mark.parametrize(
    "letter, shift, result",
    [
        ("a", "3", "d"),
        ("g", "5", "l"),
        ("x", "2", "z"),
        ("g", "-3", "d"),
        ("k", "-9", "b"),
    ],
)
def test_should_return_the_letter_that_is_shifted_from_the_given_letter_by_shift(
    letter, shift, result
):
    assert CaesarEncryptor.encode(letter, shift) == result


@pytest.mark.parametrize(
    "letter, shift, result",
    [
        ("z", "1", "a"),
        ("w", "6", "c"),
        ("p", "15", "e"),
        ("b", "-2", "z"),
        ("f", "-8", "x"),
    ],
)
def test_should_return_the_letter_that_is_shifted_from_the_given_letter_by_shift_but_loop_to_the_beginning_after_reaching_z_or_to_a_after_reaching_z(
    letter, shift, result
):
    assert CaesarEncryptor.encode(letter, shift) == result
