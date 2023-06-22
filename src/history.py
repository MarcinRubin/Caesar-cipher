import json


class History:
    def __init__(self):
        self.previous_operations = {}
        self.id = 0

    def save_operation(
        self, operation_type: str, message: str, shift: str, result: str
    ) -> None:
        new_record = {
            "operation_type": operation_type,
            "message": message,
            "shift": shift,
            "result": result,
        }
        self.previous_operations.update({self.id: new_record})
        self.id += 1

    def write_all_operations(self) -> None:
        if self.id == 0:
            print("No operations")
        for i in self.previous_operations.items():
            print(
                f"""
            Operation number: {i[0]}
            Operation type: {i[1]['operation_type']}
            Message to encode: {i[1]['message']}
            Shifted by: {i[1]['shift']}
            Result/Error: {i[1]['result']}
            """
            )

    def save_to_file(self) -> None:
        with open("history_output.txt", "w", encoding="utf-8") as file:
            json.dump(self.previous_operations, file)
