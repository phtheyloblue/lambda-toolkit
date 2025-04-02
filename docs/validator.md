# Validator Module

Provides introspection and correctness checks for lambda expressions.

## Functions

### `is_normal_form(expr)`
- Returns `True` if `expr` cannot be reduced further.

### `is_reducible(expr)`
- Returns `True` if `expr` *can* be reduced.

### `is_closed(expr)`
- Returns `True` if `expr` has no free variables.

### `has_free_variable(expr, var_index)`
- Returns `True` if the given variable index is free in the expression.

These utilities are essential for:
- Implementing lazy evaluation
- Ensuring safe substitution
- Reasoning symbolically
