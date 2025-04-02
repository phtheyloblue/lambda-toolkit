# AST Node Definitions

These are the basic building blocks of lambda expressions used across the toolkit.

## `LambdaExpr`

Base class — can be `Var`, `Abs`, or `App`.

## `Var(index: int)`

References a variable bound by a surrounding abstraction.

## `Abs(body: LambdaExpr)`

Lambda abstraction — binds a new variable.

## `App(func: LambdaExpr, arg: LambdaExpr)`

Function application — applies `func` to `arg`.

For how these nodes are reduced, see [core.md](core.md).
For parser rules, see [index.md](index.md).
