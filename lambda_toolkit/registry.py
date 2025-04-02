
# Local application imports
from lambda_toolkit.nodes import LambdaExpr

expression_registry = {}

def define(name: str, expr: LambdaExpr, lazy_args=None):
    """Register a named lambda expression with optional lazy argument metadata."""
    expression_registry[name] = {
        "expr": expr,
        "lazy_args": lazy_args if lazy_args is not None else []
    }

def lookup(name: str) -> LambdaExpr:
    return expression_registry[name]["expr"]

def get_lazy_spec(name: str):
    return expression_registry[name].get("lazy_args", [])

def list_definitions():
    return list(expression_registry.keys())

def save_definitions(path: str):
    import json
    def serialize(expr):
        return repr(expr)
    data = {
        name: {
            "expr": serialize(entry["expr"]),
            "lazy_args": entry.get("lazy_args", [])
        }
        for name, entry in expression_registry.items()
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_definitions(path: str):
    import json
    from ast import literal_eval
    with open(path, "r") as f:
        data = json.load(f)
    for name, entry in data.items():
        expr = literal_eval(entry["expr"])
        lazy_args = entry.get("lazy_args", [])
        define(name, expr, lazy_args)
