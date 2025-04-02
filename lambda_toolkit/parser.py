
# Standard library imports
import re

# Local application imports
from lambda_toolkit.nodes import Abs, App, LambdaExpr, Var


def tokenize(expr: str):
    # Normalize known lambda forms to a single λ
    expr = re.sub(r"(\\\\|\\|lambda|L)(?=\s*[a-zA-Z_])", "λ", expr)

    # Add spacing around λ, parentheses, and dot
    expr = re.sub(r"(λ|[()\.])", r" \1 ", expr)

    # Tokenize and clean
    tokens = [t for t in expr.strip().split() if t]
    return tokens

def parse(tokens, ctx=None):
    if ctx is None:
        ctx = []

    def parse_expr(tokens, ctx):
        if not tokens:
            raise ValueError("Unexpected end of tokens")
        token = tokens.pop(0)
        if token == "(":
            sub_expr = parse_expr(tokens, ctx)
            while tokens and tokens[0] != ")":
                sub_expr = App(sub_expr, parse_expr(tokens, ctx))
            if not tokens or tokens[0] != ")":
                raise ValueError("Unmatched parenthesis")
            tokens.pop(0)
            return sub_expr
        elif token == "λ":
            if not tokens:
                raise ValueError("Missing variable name after λ")
            param = tokens.pop(0)
            if not re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", param):
                raise ValueError(f"Invalid parameter name: {param}")
            if not tokens or tokens.pop(0) != ".":
                raise ValueError("Expected '.' after parameter")
            body = parse_expr(tokens, [param] + ctx)
            return Abs(body)
        else:
            if token not in ctx:
                raise ValueError(f"Unbound variable: {token}")
            return Var(ctx.index(token))

    return parse_expr(tokens, ctx)

def parse_lambda(src: str) -> LambdaExpr:
    tokens = tokenize(src)
    return parse(tokens)
