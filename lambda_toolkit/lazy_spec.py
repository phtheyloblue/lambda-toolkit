
# Local application imports
from lambda_toolkit.nodes import Abs, App, LambdaExpr
from lambda_toolkit.validator import has_free_variable


def lazy_beta_reduce_spec(expr: LambdaExpr) -> str:
    """
    Non-evaluating spec-style function that describes how lazy beta reduction would proceed.
    It explains whether an argument would be evaluated based on variable usage.
    """  # noqa: E501
    if isinstance(expr, App) and isinstance(expr.func, Abs):
        body = expr.func.body
        used = has_free_variable(body, 0)
        if not used:
            return "Body does not use argument: skip evaluating the argument (short-circuit)"  # noqa: E501
        else:
            return "Body uses argument: defer evaluation of argument until substituted"
    return "Expression is not reducible by lazy beta reduction"
