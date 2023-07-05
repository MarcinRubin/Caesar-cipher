import sentry_sdk


class NonAsciiCharacter(Exception):
    def __init__(self, invalid_character: str):
        self.invalid_character = invalid_character

    def __str__(self):
        return f"The {self.invalid_character} cannot be transformed into ascii code!"


class CaesarEncryptor:
    @staticmethod
    def encode(char: str, shift: str) -> chr:
        ascii_code = ord(char)
        n_shift = int(shift)

        if ascii_code < 32 or ascii_code > 126:
            raise NonAsciiCharacter(char)

        if 64 < ascii_code < 91:
            ascii_code = 65 + (ascii_code - 65 + n_shift) % 26
        elif 96 < ascii_code < 123:
            ascii_code = 97 + (ascii_code - 97 + n_shift) % 26

        return chr(ascii_code)

    @staticmethod
    def encrypt_message(message: str, shift: str) -> str:
        try:
            encrypted_message = "".join(
                [CaesarEncryptor.encode(letter, shift) for letter in message]
            )
            return encrypted_message
        except NonAsciiCharacter as err:
            sentry_sdk.capture_exception(err)
            return str(err)
        except ValueError as err:
            sentry_sdk.capture_exception(err)
            return "The shift has to be an integer!"

    @staticmethod
    def decrypt_message(message: str, shift: str) -> str:
        if shift[0] == "-":
            shift = shift[1:]
        else:
            shift = "-" + shift
        return CaesarEncryptor.encrypt_message(message, shift)
