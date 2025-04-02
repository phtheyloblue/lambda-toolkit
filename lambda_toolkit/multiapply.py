
# Local application imports
from lambda_toolkit.core import beta_reduce
from lambda_toolkit.nodes import App
from lambda_toolkit.registry import get_lazy_spec, lookup


def apply_operator(name: str, args: list, strategy: str = "lazy") -> App:
    """
    Applies a multi-argument combinator by respecting its lazy_args metadata.

    Args:
        name (str): The name of the registered combinator (e.g. 'IF')
        args (list[LambdaExpr]): List of arguments to apply
        strategy (str): Global fallback evaluation strategy if metadata is missing

    Returns:
        LambdaExpr: Fully applied expression
    """
    expr = lookup(name)
    lazy_spec = get_lazy_spec(name)
    full_app = expr

    for i, arg in enumerate(args):
        lazy = lazy_spec[i] if i < len(lazy_spec) else (strategy == "lazy")
        if not lazy:
            arg = beta_reduce(arg, strategy)
        full_app = App(full_app, arg)

    return full_app
