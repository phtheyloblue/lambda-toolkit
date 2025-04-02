from lambda_toolkit.core import Abs, App, Var, pretty_improved, reduce_lambda_verbose
from lambda_toolkit.multiapply import apply_operator
from lambda_toolkit.registry import define, lookup

# Define IF: λb.λt.λf. b t f
if_expr = Abs(Abs(Abs(App(App(Var(2), Var(1)), Var(0)))))

# condition = eager; branches = lazy
define(
    "IF",
    if_expr,
    lazy_args=[False, True, True]
)

# TRUE = λx.λy. x
true_expr = Abs(Abs(Var(1)))
define("TRUE", true_expr)

# Sample branches
then_branch = Abs(Var(0))  # identity
else_branch = Abs(App(Var(0), Var(0)))  # (λx. x x) — diverging if forced

# Apply IF TRUE then_branch else_branch using apply_operator
full_expr = apply_operator("IF", [lookup("TRUE"), then_branch, else_branch])

# Trace the result
steps = reduce_lambda_verbose(full_expr, max_steps=5)

print("Reduction Trace for IF TRUE identity (x) (diverging):")
for label, step in steps:
    print(label + ":\n" + pretty_improved(step) + "\n")
