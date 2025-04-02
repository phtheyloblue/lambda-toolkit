

# Standard library imports
import sys

sys.path.insert(0, '/mnt/data/lambda_toolkit')

from lambda_toolkit.ast import Abs, App, Var

expr = Abs(App(Var(1), Var(0)))  # λx. (f x)

if hasattr(expr, "reduce_eta"):
    print("OK: reduce_eta is present.")
else:
    print("FAIL: reduce_eta is missing.")
