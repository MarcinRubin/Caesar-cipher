import pytest

from src.encoder import CaesarEncryptor


@pytest.mark.parametrize(
    "message, letter",
    [
        ("iść", "ś"),
        ("gwizdać", "ć"),
        ("żaba", "ż"),
        ("ümlaut", "ü"),
        ("öffnen", "ö"),
        ("ひ", "ひ"),
        ("な", "な"),
        ("â", "â"),
        ("û", "û"),
    ],
)
def test_if_function_return_message_if_the_char_in_the_string_cannot_be_transformed_into_ascii(
    message, letter
):
    err_message = f"The {letter} cannot be transformed into ascii code!"
    assert CaesarEncryptor.decrypt_message(message, "3") == err_message


@pytest.mark.parametrize(
    "shift", ["zebra", ".01", "1.5gh", "999999.g", "2..56", "2.5.66"]
)
def test_should_return_appropriate_message_if_the_shift_is_not_a_valid_integer(shift):
    message_to_encode = "message"
    err_msg = "The shift has to be an integer!"
    assert CaesarEncryptor.decrypt_message(message_to_encode, shift) == err_msg


@pytest.mark.parametrize("shift", ["0", "6", "99999", "-99999", "1253635", "-23125356"])
def test_should_return_an_empty_string_if_empty_string_is_provided_as_an_message_to_encode(
    shift,
):
    message_to_encode = ""
    assert CaesarEncryptor.decrypt_message(message_to_encode, shift) == ""


@pytest.mark.parametrize(
    "message_to_encode, shift, coded_message",
    [
        ("What can I Do?", "7", "Patm vtg B Wh?"),
        ("I don't understand!", "-7", "P kvu'a buklyzahuk!"),
        (
            "What if I shift beyond the alphabet?!",
            "35",
            "Nyrk zw Z jyzwk svpfeu kyv rcgyrsvk?!",
        ),
        ("Now, message is shifted by 0!", "0", "Now, message is shifted by 0!"),
        (
            "Beyond alphabet, but negative shifts!",
            "-40",
            "Psmcbr ozdvopsh, pih bsuohwjs gvwthg!",
        ),
    ],
)
def test_should_encode_the_given_message_properly_given_valid_message_and_valid_shift(
    message_to_encode, shift, coded_message
):
    assert CaesarEncryptor.decrypt_message(message_to_encode, shift) == coded_message
