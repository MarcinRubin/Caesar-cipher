from src.encoder import CaesarEncryptor
from src.history import History


class InvalidOption(Exception):
    def __init__(self, invalid_option: str):
        self.invalid_option = invalid_option

    def __str__(self):
        return f"The option {self.invalid_option} is invalid!"


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
            "3": self._history_of_all_operations,
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
                4. Load messages from json file
                5. Save all operations to json file
                0. Quit program
                """
        )

    def _get_and_execute_choice(self, user_input):
        self.choices.get(user_input)()

    def _encrypt_message(self):
        msg = input("Write a message, program will return the encoded version of it:\n")
        shift = input("Shift by how many letter?:\n")
        encoded_msg = CaesarEncryptor.encrypt_message(msg, shift)
        self._history.save_operation("encryption", msg, shift, encoded_msg)
        print(encoded_msg)

    def _decrypt_message(self):
        msg = input("Write a message, program will return the encoded version of it:\n")
        shift = input("Shift by how many letter?:\n")
        encoded_msg = CaesarEncryptor.decrypt_message(msg, shift)
        self._history.save_operation("decryption", msg, shift, encoded_msg)
        print(encoded_msg)

    def _history_of_all_operations(self):
        self._history.write_all_operations()

    def _quit(self):
        print("Do you want to save history of all operations to file?")
        user_choice = ""
        while user_choice not in {"y", "n"}:
            user_choice = input("Write 'y' if you want to save and 'n' if not")

        if user_choice == "y":
            self._history.save_to_file()

        self.__is_running = False
