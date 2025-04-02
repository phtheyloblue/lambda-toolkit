
# Local application imports
from lambda_toolkit.nodes import Abs, App, Var


def is_closed(expr, depth=0):
    if isinstance(expr, Var):
        return expr.index < depth
    if isinstance(expr, Abs):
        return is_closed(expr.body, depth + 1)
    if isinstance(expr, App):
        return is_closed(expr.func, depth) and is_closed(expr.arg, depth)
    return False

def is_reducible(expr):
    if isinstance(expr, App):
        if isinstance(expr.func, Abs):
            return True
        return is_reducible(expr.func) or is_reducible(expr.arg)
    if isinstance(expr, Abs):
        return is_reducible(expr.body)
    return False

def is_normal_form(expr):
    return not is_reducible(expr)
