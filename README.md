
# Lambda Toolkit

A plug-and-play symbolic lambda calculus engine with full beta-reduction support, Church encodings, introspective validation, and reduction tracing. Designed for education, program synthesis, and integration with symbolic/LLM-based reasoning systems.

---

## Features

- **Lambda Expression Engine**
  - De Bruijn-indexed lambda calculus (`Var`, `Abs`, `App`)
  - Beta-reduction with substitution and variable shifting

- **Church Encoding Library**
  - Booleans: `TRUE`, `FALSE`, `NOT`, `OR`, `IF`
  - Numerals: `ZERO`, `ONE`, `TWO`, `SUCC`, `PLUS`, `MULT`, `PRED`, `ISZERO`

- **Introspection Tools**
  - `is_normal_form()`, `is_reducible()`, `is_closed()`, `has_free_variable()`

- **Trace and Visualization**
  - Step-by-step reduction tracing
  - Human-readable pretty-printing

- **Environment & Utilities**
  - `define(name, expr)` and `lookup(name)` to store/retrieve expressions
  - Registry serialization via JSON (`standard.json`)

- **Fully Testable and Lintable**
  - Unit tests with `unittest`
  - Ruff formatting (`pyproject.toml` + optional pre-commit hooks)

---

## Installation

```bash
git clone https://your-repo-url/lambda_toolkit.git
cd lambda_toolkit
pip install .
```

---

## Example: SUCC 1 → 2

```python
from lambda_toolkit.core import App, reduce_lambda_verbose, pretty_improved
from lambda_toolkit.core import church_succ, church_one

expr = App(church_succ(), church_one())
trace = reduce_lambda_verbose(expr)

for label, step in trace:
    print(f"{label}:
{pretty_improved(step)}
")
```

---

## Structure

```text
lambda_toolkit/
├── core.py               # Lambda engine + expression primitives
├── validator.py          # Structural validators
├── encodings/
│   └── standard.json     # Predefined Church encodings
├── __init__.py
tests/
├── test_core.py
├── test_encodings.py
├── test_validator.py
examples/
├── succ_one.py
├── validator_usage.py
setup.py
README.md
pyproject.toml
.pre-commit-config.yaml
```

---

## Mermaid Diagram

See `docs/architecture.mmd` for an architecture diagram in Mermaid format.

---

## License

Apache 2.0 – open, auditable, extensible.


---

## Development

To run tests:
```bash
python -m unittest discover tests
```

To lint and autoformat:
```bash
ruff check . --fix
```

To contribute:
- Fork the repo
- Create a branch
- Submit a pull request

---

## Version

**v1.0.0** — Lazy by default, Garfield approved.

