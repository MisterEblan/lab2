from main import main
from unittest.mock import MagicMock, patch

@patch("builtins.print")
@patch("builtins.input", return_value="2, 2")
def test_in_ring(
    mock_input: MagicMock,
    mock_print: MagicMock,
    in_ring_message: str,
) -> None:
        main()

        for arg in mock_print.call_args_list:
            if in_ring_message in str(arg):
                assert True
                return
        assert False, "Ожидалось сообщение о том, что точка будет в кольце"


@patch("builtins.print")
@patch("builtins.input", return_value="3, 2")
def test_in_ring_1(
    mock_input: MagicMock,
    mock_print: MagicMock,
    in_ring_message: str
) -> None:
    main()

    for arg in mock_print.call_args_list:
        if in_ring_message in str(arg):
            assert True
            return
    assert False, "Ожидалось сообщение о том, что точка будет в кольце"

@patch("builtins.print")
@patch("builtins.input", return_value="0, 0")
def test_out_of_ring(
    mock_input: MagicMock,
    mock_print: MagicMock,
    out_of_ring_message: str
) -> None:
    main()

    for arg in mock_print.call_args_list:
        if out_of_ring_message in str(arg):
            assert True
            return
    assert False, "Ожидалось сообщение о том, что точка будет вне кольца"

@patch("builtins.print")
@patch("builtins.input", return_value="0, 6")
def test_out_of_ring_2(
    mock_input: MagicMock,
    mock_print: MagicMock,
    out_of_ring_message: str
) -> None:
    main()

    for arg in mock_print.call_args_list:
        if out_of_ring_message in str(arg):
            assert True
            return
    assert False, "Ожидалось сообщение о том, что точка будет вне кольца"
