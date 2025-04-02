
# Standard library imports
import os
from typing import List, Tuple  # noqa: F401, I001 FUTURE IMPLEMENTATIONS

# Local application imports
from lambda_toolkit.core import pretty_improved, reduce_lambda_verbose
from lambda_toolkit.multiapply import apply_operator


def generate_example_trace(
    name: str,
    args: list,
    out_path: str,
    strategy: str = "lazy",
    max_steps: int = 10
):
    """
    Generate a pretty-printed stepwise reduction trace for a combinator application.

    Args:
        name (str): Name of the registered combinator
        args (list): Arguments to apply
        out_path (str): File path to save the output trace
        strategy (str): Evaluation strategy (default: lazy)
        max_steps (int): Max number of beta reduction steps
    """
    expr = apply_operator(name, args, strategy=strategy)
    trace = reduce_lambda_verbose(expr, max_steps=max_steps)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        f.write(f"Reduction trace for {name} applied to {len(args)} args:\n\n")
        for label, step in trace:
            f.write(f"{label}:\n{pretty_improved(step)}\n\n")
