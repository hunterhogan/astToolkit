---
description: 'Instructions for code executing after all defensive checks and validation'
---

# Post-Defensive Code Instructions

These instructions apply to code that executes **after** all defensive checks, validation, and boundary handling have been performed. Post-defensive code operates under the assumption that all invariants, preconditions, and data integrity guarantees are satisfied.

---

## Core Principle: Trust Established Invariants

When code runs post-defensively, all upstream validation has already occurred. Every data structure is valid, fully populated, and conforms to its type contract. Every precondition is satisfied.

### Prohibited Patterns

Do **not** add any of the following:

- **Truthiness guards**: `if not queue: return` or `value = value or default`
- **Emptiness checks**: `if not state.listPermutationSpace:` or `if len(collection) == 0:`
- **None guards**: `if value is None:` when the type contract guarantees non-None
- **Type checks**: `if isinstance(value, ExpectedType):` when static typing guarantees the type
- **Fallback defaults**: Optional parameters with sentinel defaults used solely to avoid exceptions
- **Safety branches**: `if <unexpected_condition>: continue` to skip "impossible" states
- **Dimension validation**: Re-checking array shapes, collection lengths, or value domains
- **Silent recovery**: `try/except` blocks that suppress exceptions indicating violated invariants

### Rationale

Each defensive check adds a conditional branch. In algorithms that execute billions of iterations, these branches accumulate catastrophic performance cost. More critically, defensive checks **inside** post-defensive code hide bugs by masking violated invariants instead of exposing them.

---

## Fail-Fast for Violated Invariants

If internal state violates an invariant post-defensively, that violation represents an upstream bug. Let the interpreter raise an exception immediately.

### Examples

**Anti-pattern (hiding bugs):**

```python
if len(parts) != expectedCount:
 continue  # Skip malformed record
```

**Preferred (exposing bugs):**

```python
# Access directly; IndexError exposes the upstream defect
value = parts[expectedIndex]
```

**Anti-pattern (silent recovery):**

```python
try:
 result = computation(state)
except KeyError:
 result = defaultValue  # Suppress the exception
```

**Preferred (fail immediately):**

```python
# Let KeyError propagate; it indicates violated invariant
result = computation(state)
```

---

## Single Return Point

Multiple return points introduce data-dependent branching that complicates static analysis and transformation.

Prohibited:

- Early-return guard clauses
- Short-circuit returns based on emptiness or truthiness
- Multiple exit points (except in rare cases justified by existential semantics)

---

## No Artificial Safety Limits

If an algorithm has potential for infinite loops, **fix the root cause**. Do not add artificial safety limits to prevent infinite loops.

### Anti-pattern

```python
maxIterations = 1_000_000
for iteration in range(maxIterations):
 if terminationCondition:
  break
 # ... computation
else:
 raise RuntimeError("Maximum iterations exceeded")
```

### Preferred

Fix the algorithm so that termination is guaranteed by construction, or prove that the loop terminates and remove the guard entirely.

---

## Let No-Op-Capable Operations No-Op

Many vectorized and functional operations naturally handle empty inputs by producing empty outputs. Do not guard these operations with data-dependent conditionals.

### Vectorized Operations

**Anti-pattern (data-dependent guard):**

```python
if numpy.any(mask):
 result = array[mask]
else:
 result = numpy.empty(0, dtype=array.dtype)
```

**Preferred (let empty mask no-op):**

```python
# Empty mask naturally produces empty result
result = array[mask]
```

**Anti-pattern (checking before reduction):**

```python
if numpy.count_nonzero(mask) > 0:
 filteredArray = applyMaskedOperation(array, mask)
```

**Preferred (apply operation directly):**

```python
# Masked operation naturally handles empty mask
filteredArray = applyMaskedOperation(array, mask)
```

Rationale:

1. **Performance**: Data-dependent conditionals (`numpy.any`, `numpy.all`, `count_nonzero`) add overhead and prevent vectorization.
2. **Control flow stability**: AST transformations require stable, non-data-dependent control flow.
3. **Correctness**: The operation already handles empty inputs correctly; the guard is redundant.

---

## Branch Cost Justification

Any modification that adds conditional branches must justify the addition by demonstrating removal of equal or greater branching cost elsewhere, or by explicit user approval.

### Rule

If you add an `if` statement, you must either:

1. Remove at least as many branches elsewhere in the same hot path, or
2. Obtain explicit confirmation that the performance cost is acceptable.

---

## Exception Propagation

Do not catch exceptions in post-defensive code unless you are crossing a system boundary (e.g., logging before process termination).

Let exceptions propagate to expose defects. Stack traces are diagnostic tools; suppressing them hides bugs.

---

## Summary: Trust, Fail Fast, No-Op Naturally

1. **Trust invariants**: All validation has already occurred.
2. **Fail fast**: Violated invariants indicate bugs; expose them immediately.
3. **No-op naturally**: Don't guard operations that handle empty inputs correctly.
4. **Single return**: Maintain stable control flow for AST transformations.
5. **No artificial limits**: Fix infinite loops at the root cause, don't mask them.
6. **Semantic indexing**: Use named identifiers, never hardcoded positions.
7. **Justify branches**: Every added branch must eliminate equal or greater cost elsewhere.
