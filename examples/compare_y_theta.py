from lambda_toolkit.core import App, reduce_lambda_verbose, pretty_improved  # noqa: I001
from lambda_toolkit.registry import lookup
from lambda_toolkit.ast import Abs, Var

# Recursive body: ID = λx.x
# So Y ID and THETA ID should behave identically

f = lookup("ID") if lookup("ID") is not None else Abs(Var(0))

# Check if "Y" and "THETA" are defined

y_func = lookup("Y")
theta_func = lookup("THETA")

if y_func is None:
    print("Error: 'Y' is not defined in the registry.")
else:
    print("Y ID:")
    y_expr = App(y_func, f)
    for label, step in reduce_lambda_verbose(y_expr, max_steps=5):
        print(f"{label}:\n{pretty_improved(step)}")

if theta_func is None:
    print("Error: 'THETA' is not defined in the registry.")
else:
    print("THETA ID:")
    theta_expr = App(theta_func, f)
    for label, step in reduce_lambda_verbose(theta_expr, max_steps=5):
        print(f"{label}:\n{pretty_improved(step)}")
