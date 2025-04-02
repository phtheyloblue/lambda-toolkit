
# Standard library imports
import os
import unittest

# Local application imports
from lambda_toolkit.nodes import (
    beta_reduce,
    load_definitions,
    lookup,
    pretty_improved,
)

ENCODING_FILE = os.path.join(os.path.dirname(__file__), '..', 'lambda_toolkit', 'encodings', 'standard.json')  # noqa: E501

class TestSavedEncodings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        load_definitions(ENCODING_FILE)

    def test_all_defined_expressions_reduce_or_print(self):
        failures = []
        for name in lookup_all():
            expr = lookup(name)
            try:
                _ = beta_reduce(expr)
                _ = pretty_improved(expr)
            except Exception as e:
                failures.append((name, str(e)))
        self.assertEqual(len(failures), 0, f"Failures in: {failures}")

def lookup_all():
    from lambda_toolkit.core import expression_registry
    return list(expression_registry.keys())

if __name__ == "__main__":
    unittest.main()
