# Strang 1.2 — Geometry of Linear Equations

## Core Idea

There are **two geometric ways** to see the system `Ax = b`:

1. **Row picture** — each equation is a line (2D) or plane (3D). The solution is where they intersect.
2. **Column picture** — the solution is a **linear combination** of column vectors that produces `b`.

Both views describe the same system. The column picture is more powerful and central to linear algebra.

## Key Concepts

### Row Picture

Given:

```
2x -  y = 0
-x + 2y = 3
```

Each equation defines a line in the x-y plane. Plot both lines; they cross at `(1, 2)`. That's the solution.

In 3D, each equation is a plane. Three planes intersect at a point (if a unique solution exists).

### Column Picture

Rewrite the same system as a **vector equation**:

```
x | 2| + y |-1| = |0|
  |-1|     | 2|   |3|
```

Question: what combination of the column vectors gives `b`?

Answer: `1 × col₁ + 2 × col₂ = b`. So `x = 1, y = 2`.

### Linear Combination

The expression `c₁v₁ + c₂v₂ + ... + cₙvₙ` is a **linear combination** of vectors `v₁, ..., vₙ` with scalar weights `c₁, ..., cₙ`.

This is the single most important operation in linear algebra.

### When does it break?

- If the columns point in the **same direction** (one is a multiple of the other), they can only reach points along that line — not all of 2D space. The system may have no solution.
- If the columns **span** all of 2D space, every `b` has a solution.

## ML Connection

In ML, each feature column is a vector. A model's prediction is a **linear combination** of feature vectors weighted by learned parameters. If features are redundant (collinear), the model can't distinguish their individual effects — this is **multicollinearity**, a direct consequence of the column picture failing.

---

## Practice Problems

### Problem 1
For this system, draw (or describe) the row picture and column picture:

```
x + y = 4
x - y = 2
```

**Solution:**

**Row picture:** Line 1 is `y = 4 - x`. Line 2 is `y = x - 2`. They intersect at `(3, 1)`.

**Column picture:**

```
x |1| + y | 1| = |4|
  |1|     |-1|   |2|
```

We need `3 × (1,1) + 1 × (1,-1) = (3+1, 3-1) = (4, 2)`. Confirmed: `x=3, y=1`.

### Problem 2
Consider columns `v₁ = (1, 2)` and `v₂ = (3, 6)`. Can you reach every `b` in 2D?

**Solution:**
No. `v₂ = 3 × v₁`, so both columns point in the same direction. Any linear combination `c₁v₁ + c₂v₂ = (c₁ + 3c₂)(1, 2)` lies along the line through the origin with slope 2. You can only reach targets on that line.

### Problem 3
Write the column picture for:

```
 x + 3y = 9
2x +  y = 8
```

Find the solution using the column picture (guess and check).

**Solution:**

```
x |1| + y |3| = |9|
  |2|     |1|   |8|
```

Try `x=3, y=2`: `3(1,2) + 2(3,1) = (3+6, 6+2) = (9, 8)`. Confirmed.
