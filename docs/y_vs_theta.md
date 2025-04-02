# Y vs Θ (Turing's Fixed-Point Combinator)

## Y Combinator

**Definition:**
```
Y ≡ λf.(λx.f (x x)) (λx.f (x x))
```

- Minimalist recursive pattern
- Elegant but fragile under eager evaluation
- Requires lazy/normal-order strategy to terminate properly
- Useful for theoretical elegance and symbolic purity

## Θ (Turing's Combinator)

**Definition:**
```
Θ ≡ (λx.λy. y (x x y)) (λx.λy. y (x x y))
```

- Uses two arguments: `x` and `y`
- Wraps recursion in an outer shell of delayed execution
- Often more robust to eager evaluation
- Historically defined by Turing himself in 1937

## When to Use Each

| Scenario                     | Use Y           | Use Θ             |
|------------------------------|------------------|-------------------|
| Fully lazy interpreter       | ✅               | ✅                |
| Mixed or eager evaluation    | ⚠️ may recurse    | ✅ more stable     |
| Educational purposes         | ✅ classic form   | ✅ historical basis|
| DSL strategy specialization  | ✅ as symbolic ID | ✅ alternate option|

## Toolkit Integration

Both are registered:
- `lookup("Y")`
- `lookup("THETA")`

You can apply either to a recursive function body to achieve self-reference.
