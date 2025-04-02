
# Standard library imports
from typing import List, Tuple  # noqa: I001

# Local application imports
from lambda_toolkit.nodes import LambdaExpr, Var, Abs, App, has_free_variable, shift, substitute  # noqa: E501

def beta_reduce(expr: LambdaExpr, strategy: str = "lazy") -> LambdaExpr:
    """Delegates reduction to the AST node’s reduce() method."""
    return expr.reduce(strategy)
    if isinstance(expr, App):
        if isinstance(expr.func, Abs):
            body = expr.func.body
            arg = expr.arg
            if strategy == "lazy" and not has_free_variable(body, 0):
                return shift(body, -1)
            return shift(substitute(body, 0, arg), -1)
        return App(beta_reduce(expr.func, strategy), expr.arg)
    if isinstance(expr, Abs):
        return Abs(beta_reduce(expr.body, strategy))
    return expr

def reduce_lambda_verbose(
    expr: LambdaExpr,
    max_steps: int = 10,
    strategy: str = "lazy",
    eta: bool = False) -> List[Tuple[str, LambdaExpr]]:
    steps = []
    current = expr
    for i in range(max_steps):
        steps.append(("Step " + str(i), current))
        reduced = beta_reduce(current, strategy)
        if eta:
            reduced = reduce_eta(reduced)
        if repr(reduced) == repr(current):
            break
        current = reduced
    steps.append(("Final", current))
    return steps

def pretty_improved(expr: LambdaExpr, ctx: List[str] = None, level: int = 0) -> str:
    """Return an indented, human-readable representation of a De Bruijn expression."""
    if ctx is None:
        ctx = []
    indent = "  " * level
    if isinstance(expr, Var):
        if expr.index < len(ctx):
            return ctx[-(expr.index + 1)]
        return "#" + str(expr.index)
    if isinstance(expr, Abs):
        var_name = "x" + str(len(ctx))
        body_str = pretty_improved(expr.body, ctx + [var_name], level + 1)
        return indent + "λ" + var_name + ".\n" + body_str
    if isinstance(expr, App):
        func_str = pretty_improved(expr.func, ctx, level + 1)
        arg_str = pretty_improved(expr.arg, ctx, level + 1)
        return indent + "(" + func_str + "\n" + indent + " " + arg_str + ")"
    return indent + "<?>"


def reduce_eta(expr: LambdaExpr) -> LambdaExpr:
    """Apply a single eta-reduction step if possible."""
    if isinstance(expr, Abs):
        return expr.reduce_eta()
    if isinstance(expr, App):
        return App(reduce_eta(expr.func), reduce_eta(expr.arg))
    if isinstance(expr, Var):
        return expr
    return expr
