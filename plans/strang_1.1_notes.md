# Strang 1.1 — Introduction to Linear Algebra

## Core Idea

Linear algebra is about **systems of linear equations** and their solutions. The central problem: solve `Ax = b`.

- `A` = coefficient matrix (known)
- `x` = unknown vector (what we solve for)
- `b` = right-hand side vector (known)

## Key Concepts

### Linear equations
A linear equation has the form:

```
a₁x₁ + a₂x₂ + ... + aₙxₙ = b
```

No powers, no products of unknowns. Each term is a constant times a variable.

### Systems of equations
Multiple linear equations with the same unknowns:

```
2x + 3y = 7
 x -  y = 1
```

This system has one solution: `x = 2.5, y = 0.667` — but not all systems do. A system can have:
- **One solution** (lines intersect at a point)
- **No solution** (parallel lines)
- **Infinitely many solutions** (same line)

### Matrix form: Ax = b
The system above becomes:

```
| 2  3 | | x |   | 7 |
| 1 -1 | | y | = | 1 |
```

This compact notation is the language of linear algebra.

## ML Connection

In machine learning, `A` is your **data matrix** (rows = samples, columns = features), `x` is a **weight vector**, and `b` is a **target/label vector**. Solving `Ax = b` is the foundation of linear regression: finding weights that map features to predictions.

---

## Practice Problems

### Problem 1
Write this system in matrix form `Ax = b`:

```
 x + 2y = 5
3x -  y = 4
```

**Solution:**

```
A = | 1  2 |    x = | x |    b = | 5 |
    | 3 -1 |        | y |        | 4 |
```

### Problem 2
Does this system have one solution, no solution, or infinitely many?

```
 x + y = 3
2x + 2y = 6
```

**Solution:**
The second equation is exactly 2× the first. They are the same line. **Infinitely many solutions**: any `(x, y)` where `x + y = 3`.

### Problem 3
Does this system have one solution, no solution, or infinitely many?

```
 x + y = 3
2x + 2y = 7
```

**Solution:**
The left sides are proportional (2× the first) but the right sides are not (7 ≠ 6). Parallel lines. **No solution.**
