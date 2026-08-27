import typing

from bobber.bobber import execute_command


def test_execute_command_return_annotation_is_none():
    """Verify execute_command is annotated to return None."""
    hints = typing.get_type_hints(execute_command)
    assert "return" in hints
    assert hints["return"] is None

