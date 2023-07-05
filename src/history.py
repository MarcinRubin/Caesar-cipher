import datetime
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
            "time": datetime.datetime.now(),
            "message": message,
            "shift": shift,
            "result": result,
        }
        self.previous_operations.update({self.id: new_record})
        self.id += 1

    def write_all_operations(self) -> None:
        if self.id == 0:
            print("No operations")
        for idx, data in self.previous_operations.items():
            print(
                f"""
            Operation number: {idx}
            Operation type: {data['operation_type']}
            Date: {data['time']}
            Message to encode: {data['message']}
            Shifted by: {data['shift']}
            Result/Error: {data['result']}
            """
            )

    def save_to_file(self) -> None:
        with open("history_output.txt", "w", encoding="utf-8") as file:
            json.dump(self.previous_operations, file)
