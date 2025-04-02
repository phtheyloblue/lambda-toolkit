
# Standard library imports
import unittest

# Local application imports
from lambda_toolkit.nodes import Abs, App, Var, beta_reduce, pretty_improved


class TestLambdaCore(unittest.TestCase):
    def test_identity_reduction(self):
        expr = App(Abs(Var(0)), Var(1))  # (λx.x) y
        reduced = beta_reduce(expr)
        self.assertEqual(repr(reduced), "Var(1)")

    def test_nested_abstraction(self):
        expr = Abs(Abs(App(Var(1), Var(0))))  # λx.λy.(x y)
        self.assertEqual(repr(expr), "Abs(Abs(App(Var(1), Var(0))))")

    def test_pretty_print(self):
        expr = Abs(Abs(App(Var(1), Var(0))))  # λx.λy.(x y)
        output = pretty_improved(expr)
        self.assertIn("λx0.", output)
        self.assertIn("λx1.", output)

if __name__ == "__main__":
    unittest.main()
