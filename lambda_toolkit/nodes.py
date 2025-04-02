
# Standard Library imports
from abc import ABC, abstractmethod
from dataclasses import dataclass


# Shared AST node definitions
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


@dataclass(frozen=True)
class Var(LambdaExpr):
    index: int

@dataclass(frozen=True)
class Abs(LambdaExpr):
    body: LambdaExpr

    def reduce(self, strategy: str = "lazy") -> "LambdaExpr":
        return Abs(self.body.reduce(strategy=strategy))

    def reduce_eta(self) -> "LambdaExpr":
        """Apply eta-reduction: λx. (f x) → f if x not free in f"""
        if isinstance(self.body, App):
            f, arg = self.body.func, self.body.arg
            if isinstance(arg, Var) and arg.index == 0 and not has_free_variable(f, 0):
                return f
        return self

@dataclass(frozen=True)
class App(LambdaExpr):
    func: LambdaExpr
    arg: LambdaExpr

    def reduce(self, strategy: str = "lazy") -> "LambdaExpr":
        if isinstance(self.func, Abs):
            body = self.func.body
            if strategy == "lazy" and not has_free_variable(body, 0):
                return shift(body, -1)
            return shift(substitute(body, 0, self.arg), -1)

        reduced_func = self.func.reduce(strategy)
        return App(reduced_func, self.arg)

def has_free_variable(expr: LambdaExpr, index: int) -> bool:
    if isinstance(expr, Var):
        return expr.index == index
    elif isinstance(expr, Abs):
        return has_free_variable(expr.body, index + 1)
    elif isinstance(expr, App):
        return has_free_variable(expr.func, index) or has_free_variable(expr.arg, index)
    return False

def shift(expr: LambdaExpr, d: int, cutoff: int = 0) -> LambdaExpr:
    """Shift De Bruijn indices in an expression by d, respecting cutoff."""
    if isinstance(expr, Var):
        return Var(expr.index + d) if expr.index >= cutoff else expr
    if isinstance(expr, Abs):
        return Abs(shift(expr.body, d, cutoff + 1))
    if isinstance(expr, App):
        return App(shift(expr.func, d, cutoff), shift(expr.arg, d, cutoff))
    return expr

def substitute(expr: LambdaExpr, j: int, s: LambdaExpr) -> LambdaExpr:
    """Substitute variable at index j in expr with s."""
    if isinstance(expr, Var):
        return s if expr.index == j else expr
    if isinstance(expr, Abs):
        return Abs(substitute(expr.body, j + 1, shift(s, 1)))
    if isinstance(expr, App):
        return App(substitute(expr.func, j, s), substitute(expr.arg, j, s))
    return expr
