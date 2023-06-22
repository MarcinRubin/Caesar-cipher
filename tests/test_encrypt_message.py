import pytest

from src.encoder import CaesarEncryptor, NonAsciiCharacter


@pytest.mark.parametrize("non_ascii", ["ś", "ź", "ó", "ü", "ö", "ひ", "な", "â", "û"])
def test_if_function_return_message_if_the_char_in_the_string_cannot_be_transformed_into_ascii(
    mocker, non_ascii
):
    mocker.patch(
        "src.encoder.CaesarEncryptor.encode", side_effect=NonAsciiCharacter(non_ascii)
    )
    message = "message"
    assert (
        CaesarEncryptor.encrypt_message(message, "3")
        == f"The {non_ascii} cannot be transformed into ascii code!"
    )


def test_should_return_appropriate_message_if_the_shift_is_not_a_valid_integer(mocker):
    mocker.patch("src.encoder.CaesarEncryptor.encode", side_effect=ValueError)
    message = "message"
    shift = 0
    assert (
        CaesarEncryptor.encrypt_message(message, shift)
        == "The shift has to be an integer!"
    )
