
# Standard library imports
import unittest

# Local application imports
from lambda_toolkit.nodes import Abs, App, Var, reduce_lambda_verbose
from lambda_toolkit.registry import lookup


class TestFixedPointCombinators(unittest.TestCase):
    def test_y_and_theta_identity(self):
        identity = Abs(Var(0))
        y_app = App(lookup("Y"), identity)
        theta_app = App(lookup("THETA"), identity)

        y_steps = reduce_lambda_verbose(y_app, max_steps=5)
        theta_steps = reduce_lambda_verbose(theta_app, max_steps=5)

        self.assertEqual(
            repr(y_steps[-1][1]), repr(theta_steps[-1][1]),
            "Y and THETA should produce the same final result on identity"
        )
