# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - Initial Release

### Added
- Core lambda calculus engine with De Bruijn indices (`Var`, `Abs`, `App`)
- Lazy beta-reduction by default (prevents infinite recursion with `Y`)
- Full support for Church encodings:
  - Booleans: `TRUE`, `FALSE`, `NOT`, `OR`, `IF`
  - Numerals: `ZERO`, `ONE`, `TWO`, etc.
  - Arithmetic: `SUCC`, `PLUS`, `MULT`, `PRED`, `ISZERO`
  - Recursion: `Y` combinator
- Expression registry (`define`, `lookup`, `list_definitions`)
- JSON save/load support for named expressions
- Step-by-step reduction tracing with `pretty_improved()`
- Structural validators:
  - `is_closed`, `is_reducible`, `is_normal_form`, `has_free_variable`
- Formal lazy evaluation specification module (`lazy_spec.py`)
- Infinite recursion timeout safeguard with `Garfield` ASCII easter egg
- Complete test suite with `unittest`
- Documentation:
  - `README.md`, `index.md`, and module-specific docs
  - Mermaid architecture diagram
- GitHub-ready scaffolding (`.gitignore`, `setup.py`, `pyproject.toml`)

---


## [1.1.0] - CLI Expansion and Lazy Evaluation Framework

### Added
- `cli.py` interface with command-line support:
  - `generate-example` — create reduction traces from combinators
  - `list` — show all registered expressions and their lazy args
  - `show` — pretty-print any registered combinator
  - `evaluate` / `eval` — directly reduce and print combinator result
- CLI documentation at `docs/example_generation.md`
- Automatic trace generation via `generate_example_trace()`
- Pretty-trace examples for `IF`, `AND`, `OR`, `ISZERO`
- Evaluation strategy metadata (`lazy_args`) respected per combinator
- CLI entry point: `lambda-toolkit` via `setup.py`

### Changed
- Refactored core architecture to move AST into `ast.py` and eliminate circular imports

### Fixed
- Pretty-printer newline handling and format issues
- CLI recognition and path resolution for external use

