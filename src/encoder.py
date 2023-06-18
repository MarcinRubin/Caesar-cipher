class NonAsciiCharacter(Exception):
    def __init__(self, invalid_character: str):
        self.invalid_character = invalid_character

    def __str__(self):
        return f"The {self.invalid_character} cannot be transformed into ascii code!"


class CaesarEncryptor:
    @staticmethod
    def encode(char: str, shift: int) -> chr:
        ascii_code = ord(char)

        if ascii_code < 32 or ascii_code > 126:
            raise NonAsciiCharacter(char)

        if 64 < ascii_code < 91:
            ascii_code = 65 + (ascii_code - 65 + shift) % 26
        elif 96 < ascii_code < 123:
            ascii_code = 97 + (ascii_code - 97 + shift) % 26

        return chr(ascii_code)

    @staticmethod
    def encrypt_message(message: str, shift: str) -> str:
        try:
            n_shift = int(shift)
            encrypted_message = "".join(
                [CaesarEncryptor.encode(letter, n_shift) for letter in message]
            )
            return encrypted_message
        except NonAsciiCharacter:
            return "There was a non ascii character in the given message!"
        except ValueError:
            return "The shift has to be an integer!"
