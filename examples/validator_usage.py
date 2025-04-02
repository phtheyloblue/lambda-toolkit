
from lambda_toolkit.core import Abs, App, Var, beta_reduce, pretty_improved
from lambda_toolkit.validator import is_closed, is_normal_form, is_reducible

# Define expression: (λx.x) y → should be reducible
expr = App(Abs(Var(0)), Var(1))

print("Expression:")
print(pretty_improved(expr))

print("\nIs reducible?", is_reducible(expr))
print("Is normal form?", is_normal_form(expr))
print("Is closed?", is_closed(expr))

# Reduce it
reduced = beta_reduce(expr)
print("\nReduced Expression:")
print(pretty_improved(reduced))
print("Is normal form after reduction?", is_normal_form(reduced))
