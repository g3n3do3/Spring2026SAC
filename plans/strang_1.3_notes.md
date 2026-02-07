# Strang 1.3 — Gaussian Elimination

## Core Idea

Gaussian elimination is the **systematic algorithm** for solving `Ax = b`. It transforms the system into an **upper triangular** form using row operations, then solves by **back substitution**.

This is how computers actually solve linear systems.

## Key Concepts

### The Algorithm

1. **Forward elimination**: use the pivot (leading entry) in each row to eliminate entries below it.
2. **Back substitution**: solve the triangular system from bottom to top.

### Example

```
 x + 2y + z =  2
3x + 8y + z = 12
     4y + z =  2
```

**Step 1:** Eliminate `x` from row 2. Subtract 3 × row 1 from row 2:

```
 x + 2y +  z =  2        (unchanged)
     2y - 2z =  6        (row2 - 3×row1)
     4y +  z =  2        (unchanged)
```

**Step 2:** Eliminate `y` from row 3. Subtract 2 × row 2 from row 3:

```
 x + 2y +  z =  2
     2y - 2z =  6
          5z = -10
```

Now it's upper triangular. The **pivots** are 1, 2, 5 (the leading entries on the diagonal).

**Step 3: Back substitution** — solve from bottom up:

- `5z = -10` → `z = -2`
- `2y - 2(-2) = 6` → `2y = 2` → `y = 1`
- `x + 2(1) + (-2) = 2` → `x = 2`

Solution: `x = 2, y = 1, z = -2`.

### Pivots

- Pivots are the diagonal entries after elimination.
- A pivot **cannot be zero**. If a zero appears on the diagonal, swap rows (row exchange).
- If no nonzero pivot can be found, the system is **singular** (no unique solution).

### Multipliers

The numbers used to eliminate entries are called **multipliers**. In step 1 above, the multiplier was 3 (from 3x/1x). These multipliers become the entries of the **L matrix** in LU decomposition (Section 1.5).

### Cost

For an n×n system, elimination takes roughly `n³/3` operations. This matters when n is large (thousands of features in ML).

## ML Connection

Every time a machine learning model solves a system of normal equations (e.g., closed-form linear regression via `(AᵀA)x = Aᵀb`), it uses a variant of Gaussian elimination internally. Understanding elimination helps you recognize when a system is **ill-conditioned** (near-singular) — a common source of numerical instability in ML.

---

## Practice Problems

### Problem 1
Apply Gaussian elimination to solve:

```
x + y = 5
2x + 4y = 16
```

**Solution:**

Subtract 2 × row 1 from row 2:

```
x + y = 5
    2y = 6
```

Back substitution: `y = 3`, then `x + 3 = 5` → `x = 2`.

Pivots: 1, 2.

### Problem 2
Apply Gaussian elimination. What goes wrong?

```
x + y = 3
2x + 2y = 6
```

**Solution:**

Subtract 2 × row 1 from row 2:

```
x + y = 3
    0 = 0
```

The second pivot is **zero**. The system is singular. The second equation gave no new information. Infinitely many solutions: `x = 3 - y` for any `y`.

### Problem 3
Solve by elimination:

```
2x + y - z =  1
   -y + z = -1
    6y - z =  7
```

**Solution:**

Row 1 already has no `x` to eliminate from rows 2 and 3 (they have no `x` terms). Proceed to eliminate `y` from row 3 using row 2.

Add 6 × row 2 to row 3:

```
2x + y - z =  1
    -y + z = -1
        5z =  1
```

Back substitution:
- `5z = 1` → `z = 1/5`
- `-y + 1/5 = -1` → `y = 6/5`
- `2x + 6/5 - 1/5 = 1` → `2x = 0` → `x = 0`

Solution: `x = 0, y = 6/5, z = 1/5`. Pivots: 2, -1, 5.
