from src.history import History


def test_should_return_message_no_operations_if_the_history_is_empty(capsys):
    history = History()
    history.write_all_operations()
    captured = capsys.readouterr()
    expected = "No operations\n"

    assert captured.out == expected


def test_should_return_all_operations_stored_in_the_dictionary(capsys):
    history = History()
    history.save_operation(
        "operation_type", "message_to_encode", "shifted_by", "result_or_error"
    )
    history.write_all_operations()
    captured = capsys.readouterr()

    expected = """
            Operation number: 0
            Operation type: operation_type
            Message to encode: message_to_encode
            Shifted by: shifted_by
            Result/Error: result_or_error
            \n"""

    assert captured.out == expected
