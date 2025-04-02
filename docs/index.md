# Lambda Toolkit Documentation

Version: 1.1.0

## Overview

Lambda Toolkit is a symbolic lambda calculus engine built with introspective evaluation, Church encodings, lazy reduction, and educational traceability. This toolkit supports recursive function modeling (via the Y combinator), semantic validation, and customizable expression registries for symbolic reasoning systems.

## Features

- Lazy beta-reduction
- Full De Bruijn indexing
- Step-by-step evaluation traces
- Expression registry (define/lookup)
- Church encodings (booleans, numerals, arithmetic, recursion)
- Validation (is_closed, is_normal_form, etc.)
- Mermaid architecture diagram
- Timeout mechanism with Garfield Easter egg

## Getting Started

Install locally:
```bash
pip install .
```

Explore Church encodings:
```python
from lambda_toolkit.core import lookup
print(lookup("TWO"))
```

Run validation:
```python
from lambda_toolkit.validator import is_normal_form
print(is_normal_form(lookup("TWO")))
```

See example workflows in `examples/`.

## License

Apache 2.0

## Example: Lazy Evaluation of IF

```lambda
IF TRUE (λx.x) (λx. x x)
```

Should evaluate to `λx.x` **without touching** the diverging branch `(λx. x x)`.

### Reduction Trace:
```
Step 0:
(  (    (      λx0.
        λx1.
          λx2.
            (              (x0
               x1)
             x2)
           λx0.
        λx1.
x0)
       λx0.
x0)
   λx0.
    (x0
     x0))

Step 1:
(  (    λx0.
      λx1.
        (          (            λx2.
              λx3.
x2
           x0)
         x1)
       λx0.
x0)
   λx0.
    (x0
     x0))

Step 2:
(  λx0.
    (      (        λx1.
          λx2.
x1
               λx1.
x1)
     x0)
   λx0.
    (x0
     x0))

Step 3:
(  (    λx0.
      λx1.
x0
       λx0.
x0)
   λx0.
    (x0
     x0))

Step 4:
(  λx0.
    λx1.
x1
   λx0.
    (x0
     x0))

Final:
λx0.
x0
```

This shows that the evaluation strategy correctly **short-circuits evaluation** of unnecessary branches. Only `TRUE` and the identity were evaluated.


## CLI Extras

- `--trace`: Show reduction steps (see [example_generation.md](example_generation.md))
- `monday`: Garfield's eternal return. See [easter_egg.md](easter_egg.md).
- `crowbar`: A nod to Half-Life. See [easter_egg.md](easter_egg.md).

For implementation details, check [core.md](core.md) and [nodes.md](nodes.md).
