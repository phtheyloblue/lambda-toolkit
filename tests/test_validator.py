
# Standard library imports
import unittest

# Local application imports
from lambda_toolkit.nodes import Abs, App, Var
from lambda_toolkit.validator import (
    has_free_variable,
    is_closed,
    is_normal_form,
    is_reducible,
)


class TestValidator(unittest.TestCase):
    def test_is_normal_form(self):
        expr = Abs(Var(0))  # λx.x
        self.assertTrue(is_normal_form(expr))

        expr2 = App(Abs(Var(0)), Var(1))  # (λx.x) y
        self.assertFalse(is_normal_form(expr2))

    def test_is_reducible(self):
        expr = Abs(Var(0))  # λx.x
        self.assertFalse(is_reducible(expr))

        expr2 = App(Abs(Var(0)), Var(1))  # (λx.x) y
        self.assertTrue(is_reducible(expr2))

    def test_is_closed(self):
        expr = Abs(Var(0))  # λx.x
        self.assertTrue(is_closed(expr))

        expr2 = Var(0)
        self.assertFalse(is_closed(expr2))

    def test_has_free_variable(self):
        expr = App(Var(0), Abs(Var(1)))  # x (λy.y)
        self.assertTrue(has_free_variable(expr, 0))
        self.assertFalse(has_free_variable(expr, 1))

if __name__ == "__main__":
    unittest.main()
