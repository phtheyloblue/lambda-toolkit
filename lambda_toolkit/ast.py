
# Standard library imports
from abc import ABC, abstractmethod  # noqa: I001
from dataclasses import dataclass

# Local application imports
from lambda_toolkit.nodes import has_free_variable, shift, substitute

# === Base class ===
class LambdaExpr(ABC):
    @abstractmethod
    def __repr__(self):
        pass

    def __eq__(self, other):
        if not isinstance(other, LambdaExpr):
            return NotImplemented
        return self.__repr__() == other.__repr__()

    def reduce(self, strategy: str = "lazy") -> "LambdaExpr":
        return self  # Default is no-op

    def reduce_eta(self) -> "LambdaExpr":
        return self


# === Variable ===
@dataclass(frozen=True)
class Var(LambdaExpr):
    index: int

    def __repr__(self):
        return f"Var({self.index})"

# === Abstraction ===
@dataclass(frozen=True)
class Abs(LambdaExpr):
    body: LambdaExpr

    def __repr__(self):
        return f"Abs({self.body})"

    def reduce(self, strategy: str = "lazy") -> "LambdaExpr":
        return Abs(self.body.reduce(strategy=strategy))

    def reduce_eta(self) -> "LambdaExpr":
        """Apply eta-reduction: λx. (f x) → f if x not free in f"""
        if isinstance(self.body, App):
            f, arg = self.body.func, self.body.arg
            if isinstance(arg, Var) and arg.index == 0 and not has_free_variable(f, 0):
                return f
        return self

# === Application ===
@dataclass(frozen=True)
class App(LambdaExpr):
    func: LambdaExpr
    arg: LambdaExpr

    def __repr__(self):
        return f"App({self.func}, {self.arg})"

    def reduce(self, strategy: str = "lazy") -> "LambdaExpr":
        if isinstance(self.func, Abs):
            body = self.func.body
            if strategy == "lazy" and not has_free_variable(body, 0):
                return shift(body, -1)
            return shift(substitute(body, 0, self.arg), -1)

        reduced_func = self.func.reduce(strategy)
        return App(reduced_func, self.arg)

# === Local fallback utility ===
# Only define if lambda_toolkit.ast.has_free_variable is not available
def _has_free_variable(expr: LambdaExpr, var_index: int, depth: int = 0) -> bool:
    match expr:
        case Var(index):
            return index == var_index + depth
        case Abs(body):
            return _has_free_variable(body, var_index, depth + 1)
        case App(func, arg):
            return (_has_free_variable(func, var_index, depth) or
                    _has_free_variable(arg, var_index, depth))
