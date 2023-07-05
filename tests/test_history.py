from freezegun import freeze_time

from src.history import History


def test_should_return_message_no_operations_if_the_history_is_empty(capsys):
    history = History()
    history.write_all_operations()
    captured = capsys.readouterr()
    expected_message = "No operations\n"

    assert captured.out == expected_message


@freeze_time("2014-02-16 12:00:01")
def test_should_return_all_operations_stored_in_the_dictionary(capsys):
    history = History()
    history.save_operation(
        "operation_type", "message_to_encode", "shifted_by", "result_or_error"
    )
    history.write_all_operations()
    captured = capsys.readouterr()

    expected_output = """
            Operation number: 0
            Operation type: operation_type
            Date: 2014-02-16 12:00:01
            Message to encode: message_to_encode
            Shifted by: shifted_by
            Result/Error: result_or_error
            \n"""

    assert captured.out == expected_output
