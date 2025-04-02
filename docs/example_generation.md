# Example Generation CLI

Lambda Toolkit includes a command-line tool for generating reduction traces of symbolic expressions.

## Usage

```bash
python -m lambda_toolkit.cli generate-example <NAME> <ARG1> <ARG2> ... --output <path> [--strategy lazy|eager]
```

## Parameters

- `<NAME>`: Name of a registered combinator, e.g., `IF`, `AND`, `ISZERO`
- `<ARG1> <ARG2> ...>`: Names of registered expressions to pass as arguments (must be defined)
- `--output`: Path to write the reduction trace output
- `--strategy`: Evaluation strategy (`lazy` is default)

## Example

```bash
python -m lambda_toolkit.cli generate-example IF TRUE ID DIVERGING --output examples/generated/if_trace.txt
```

This command:
- Applies the `IF` combinator to `TRUE`, `ID`, and `DIVERGING`
- Uses `lazy_args` declared during definition
- Saves a human-readable trace to `if_trace.txt`

## Notes

- All arguments must be registered beforehand using `define(...)`
- The evaluator respects laziness based on combinator metadata
- Traces are written in a pretty format using De Bruijn reconstruction

---

## Additional CLI Commands

### `list`

```bash
lambda-toolkit list
```

Lists all registered expressions and their lazy argument configuration.

---

### `show <NAME>`

```bash
lambda-toolkit show IF
```

Pretty-prints the structure of a registered expression.

---

### `evaluate` / `eval <NAME> <ARGS...>`

```bash
lambda-toolkit evaluate IF TRUE ID DIVERGING
lambda-toolkit eval AND FALSE DIVERGING
```

- Applies a combinator to named arguments
- Reduces the result and prints it directly
- Supports `--strategy lazy|eager`

This is ideal for fast debugging or shell scripting without saving to file.

---



---

### 🧪 Inline Tracing

You can now view reduction traces directly using:

```bash
lambda-toolkit evaluate ID TRUE --trace
```

This reuses the same logic as `generate-example`, powered by `reduce_lambda_verbose()` from [core.md](core.md).
