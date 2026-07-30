import typing
import unittest

from bobber.bobber import execute_command, main, save_config


class TestReturnTypeAnnotations(unittest.TestCase):
    def test_no_no_return_annotations(self):
        for func in (save_config, execute_command, main):
            hints = typing.get_type_hints(func)
            self.assertIsNot(
                hints.get('return'), typing.NoReturn,
                f'{func.__name__} should not be annotated as NoReturn'
            )


