
# Standard library imports
import unittest

# Local application imports
from lambda_toolkit.nodes import (
    Abs,
    App,
    Var,
    pretty_improved,
    reduce_eta,
    reduce_lambda_verbose,
)


class TestEtaReduction(unittest.TestCase):

    def test_eta_reducible(self):
        # λx. (f x) → f if x ∉ FV(f)
        f = Var(1)
        expr = Abs(App(f, Var(0)))  # λx. (f x)
        reduced = reduce_eta(expr)
        self.assertEqual(reduced, f)
        self.assertEqual(pretty_improved(reduced), "#1")

    def test_eta_not_reducible_due_to_capture(self):
        # λx. (x x) should NOT reduce
        x = Var(0)
        expr = Abs(App(x, x))  # λx. (x x)
        reduced = reduce_eta(expr)
        self.assertEqual(reduced, expr)  # Should remain unchanged

    def test_eta_reduction_nested_identity(self):
        # λx. ((λy.y) x) → λx. x → ID
        inner = Abs(Var(0))             # λy.y
        expr = Abs(App(inner, Var(0)))  # λx. ((λy.y) x)
        trace = reduce_lambda_verbose(expr, eta=True)
        final = trace[-1][1]
        self.assertEqual(pretty_improved(final), "λx0.\nx0")  # Should reduce to ID

    def test_eta_reduction_does_not_trigger_when_structure_mismatch(self):
        # λx. (f (x x)) → not reducible by eta
        f = Var(1)
        omega = App(Var(0), Var(0))
        expr = Abs(App(f, omega))
        reduced = reduce_eta(expr)
        self.assertEqual(reduced, expr)

if __name__ == "__main__":
    unittest.main()
