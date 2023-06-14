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

    def show_menu(self):
        is_running = True
        while is_running:
            print(
                "Main menu\n"
                "Choose one of the options\n"
                "1. Encode your message\n"
                "2. Decode your message\n"
                "3. Write history of all operations\n"
                "4. Load messages form json file\n"
                "5. Save all operations to json file\n"
                "0. Quit program"
            )
            user_input = input("Choose one option:")
            try:
                is_running = self.process_user_input(user_input)
            except InvalidOption as err:
                print(err)

    def process_user_input(self, user_input):
        match user_input:
            case "1":
                return True
            case "2":
                return True
            case "3":
                return True
            case "4":
                return True
            case "5":
                return True
            case "0":
                return False
            case _:
                raise InvalidOption(user_input)
