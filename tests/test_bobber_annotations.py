import ast
import unittest


class TestReturnAnnotations(unittest.TestCase):
    def _get_return_annotation(self, func_name):
        with open('bobber/bobber.py') as f:
            tree = ast.parse(f.read())
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == func_name:
                return node.returns
        self.fail(f'{func_name} not found')

    def test_save_config_returns_none(self):
        self.assertEqual(ast.unparse(self._get_return_annotation('save_config')), 'None')
