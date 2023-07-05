import json

import sentry_sdk

from src.encoder import CaesarEncryptor
from src.history import History


class InvalidOption(Exception):
    def __str__(self):
        return "There is no such option!"


class EncoderModuleError(Exception):
    def __init__(self, invalid_module: str):
        self.__invalid_module = invalid_module

    def __str__(self):
        return (
            f"The option: {self.__invalid_module} is invalid name for encoder "
            f"module!"
        )


class UserInterface:
    def __init__(self):
        """
        in the constructor the object responsible for encryption
        and decryption will be created along with the object
        responsible for storing the history of all operations.
        Rhe final module will be responsible for loading and saving
        data as json files (3 classes total)
        """
        self.__is_running = True
        self.choices = {
            "1": self._encrypt_message,
            "2": self._decrypt_message,
            "3": self._write_history_of_all_operations,
            "4": self._encode_from_file,
            "0": self._quit,
        }
        self._history = History()
        self._initialize()

    def _initialize(self):
        """loop"""
        while self.__is_running:
            self._show_menu()
            user_input = input("Choose one option:")
            self._get_and_execute_choice(user_input)

    @staticmethod
    def _show_menu():
        print(
            """
                ====================Main menu=======================
                1. Encode your message
                2. Decode your message
                3. History of all operations
                4. Load and encrypt messages from json file
                0. Quit program
                """
        )

    def _get_and_execute_choice(self, user_input):
        try:
            self.choices.get(user_input, self._invalid_input)()
        except InvalidOption as err:
            sentry_sdk.capture_exception(err)
            print(err)

    def _encrypt_message(self):
        msg = input("Write a message, program will return the encoded version of it:\n")
        shift = input("Shift by how many letter?:\n")
        encoded_msg = CaesarEncryptor.encrypt_message(msg, shift)
        self._history.save_operation("encryption", msg, shift, encoded_msg)
        print(encoded_msg)

    def _decrypt_message(self):
        msg = input("Write a message, program will return the decoded version of it:\n")
        shift = input("Shift by how many letter?:\n")
        decoded_msg = CaesarEncryptor.decrypt_message(msg, shift)
        self._history.save_operation("decryption", msg, shift, decoded_msg)
        print(decoded_msg)

    def _encode_from_file(self):
        with open("input.json", "r", encoding="utf-8") as file:
            read_file = json.loads(file.read())
        for i in read_file.values():
            message = i["message"]
            shift = i["shift"]
            operation_type = i["operation_type"]
            processed_msg = ""

            try:
                if operation_type == "encryption":
                    processed_msg = CaesarEncryptor.encrypt_message(message, shift)
                elif operation_type == "decryption":
                    processed_msg = CaesarEncryptor.decrypt_message(message, shift)
                else:
                    raise EncoderModuleError(operation_type)
            except EncoderModuleError as err:
                processed_msg = str(err)
                sentry_sdk.capture_exception(err)
            finally:
                print(processed_msg)
                self._history.save_operation(
                    operation_type, message, shift, processed_msg
                )

    def _write_history_of_all_operations(self):
        self._history.write_all_operations()

    def _quit(self):
        print("Do you want to save history of all operations to file?")
        user_choice = ""
        while user_choice not in {"y", "n"}:
            user_choice = input("Write 'y' if you want to save and 'n' if not")

        if user_choice == "y":
            self._history.save_to_file()

        self.__is_running = False

    def _invalid_input(self):
        raise InvalidOption()
