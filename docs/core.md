# Core Module

The `core.py` module defines the fundamental lambda calculus structures and evaluation logic.

## Classes

### `Var(index: int)`
- Represents a variable using De Bruijn index.

### `Abs(body: LambdaExpr)`
- Lambda abstraction (λx.M).

### `App(func: LambdaExpr, arg: LambdaExpr)`
- Function application (M N).

## Functions

### `beta_reduce(expr)`
- Performs one step of **lazy** beta reduction.
- Substitutes only if the bound variable is used.

### `substitute(expr, j, s)`
- Replaces `Var(j)` with `s` in `expr`.

### `shift(expr, d, cutoff=0)`
- Shifts all free De Bruijn indices by `d`.

### `reduce_lambda_verbose(expr, max_steps=10)`
- Traces evaluation step-by-step.

### `pretty_improved(expr)`
- Pretty-prints expressions in a readable tree format.

---
