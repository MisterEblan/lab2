from main import main
from unittest.mock import MagicMock, patch

@patch("builtins.input", return_value="-0.5")
@patch("builtins.print")
def test_normal(
    mock_input: MagicMock,
    mock_print: MagicMock
) -> None:
    main()

    called_args = [c for c in mock_print.call_args_list]
    assert ("f=" in arg for arg in called_args)
    assert ("x=0.5" in arg for arg in called_args)


@patch("builtins.input", return_value="0.2")
@patch("builtins.print")
def test_normal_1(
    mock_input: MagicMock,
    mock_print: MagicMock
) -> None:
    main()

    called_args = [c for c in mock_print.call_args_list]
    assert ("f=" in arg for arg in called_args)
    assert ("x=0.2" in arg for arg in called_args)

@patch("builtins.input", return_value="0.5")
@patch("builtins.print")
def test_normal_2(
    mock_input: MagicMock,
    mock_print: MagicMock
) -> None:
    main()

    called_args = [c for c in mock_print.call_args_list]
    assert ("f=" in arg for arg in called_args)
    assert ("x=0.5" in arg for arg in called_args)
