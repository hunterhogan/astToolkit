---
description: 'Standards for syntactic clarity: operator visibility, semantic identifiers, comparison orientation, and import structure.'
---

# Python Syntactic Clarity Standards

Standards for writing Python expressions that humans can parse left-to-right with minimal cognitive overhead. These standards address operator precedence, operator visibility, semantic constants, comparison orientation, and import organization.

## Foundational Principle: Left-to-Right Parsing

Human readers parse Python code left-to-right, not inside-out like a compiler. Code should signal syntactic structure as early as possible so readers encounter operators and modifiers *before* processing the expressions they govern.

**Goal**: Eliminate the need for readers to mentally reparse statements after encountering unexpected operators.

---

## Operator Visibility

### Deferred Operators (Anti-Pattern)

A **deferred operator** appears after an expression it modifies, forcing the reader to reparse the statement upon discovering the operator.

**Problematic example:**

```python
state.productsOfDimensions[dimensionNearest首(leafAt一零) - 1]
```

**Human parsing sequence (left-to-right):**

1. `state` → accessing state
2. `.productsOfDimensions` → accessing attribute
3. `[...]` → indexing operation
4. `dimensionNearest首(...)` → function call returns index value
5. `leafAt一零` → function argument
6. **`- 1`** → **Surprise!** Must reparse: the function return is modified before indexing

The `- 1` is a **deferred operator** because the reader has already mentally processed `dimensionNearest首(leafAt一零)` as complete before discovering it must be decremented.

### Foreshadowing with Explicit Structure

Transform deferred operators by using explicit function calls or parentheses that signal continuation from the start.

**Improved example:**

```python
getitem(state.productsOfDimensions, (dimensionNearest首(leafAt一零) - 1))
```

**Human parsing sequence:**

1. `getitem(...)` → **signals** two-argument indexing operation
2. First argument: `state.productsOfDimensions`
3. Second argument: `(...)` → **signals** compound expression
4. `dimensionNearest首(leafAt一零) - 1` → expected transformation within compound expression

The opening `getitem(` and inner `(` both signal that expressions will be combined, eliminating surprise.

### When to Apply Explicit Structural Signals

- **Simple expressions**: Do not add explicit structure. `value[index]` is clearer than `getitem(value, index)`.
- **Complex expressions**: If an operator appears after a function call, nested subscript, or multi-level attribute access, use explicit structure.

**Heuristic**: If you can parse the expression in one left-to-right pass without "backing up" mentally, it's simple enough. If you must reparse upon reaching an operator, apply explicit structure.

### Hidden Operators

Some operators are visually inconspicuous, especially in complex expressions:

| Hidden Operator                              | Problem                        | Explicit Replacement           |
| -------------------------------------------- | ------------------------------ | ------------------------------ |
| `~value`                                     | Single character, easy to miss | `operator.invert(value)`       |
| `-value` (negation)                          | Ambiguous with subtraction     | `operator.neg(value)`          |
| `value[key]` (in complex nested expressions) | Operator position unclear      | `operator.getitem(value, key)` |

**Apply explicit forms only when:**

- The operator is embedded in a complex expression
- The operator's presence might escape notice during code review

**Example (hidden negation):**

```python
# Hidden operator in complex expression
result = computeValue(~mask & 0xFF) + offset
```

**Explicit form:**

```python
result = computeValue(operator.invert(mask) & 0xFF) + offset
```

The function call `operator.invert(mask)` is impossible to miss, whereas `~mask` might be overlooked.

---

## Semantic Identifiers for Ambiguous Literals

### The Problem with "Semantically-Useless Operators"

Consider this expression:

```python
range(bottles + 1)
```

**Why `+ 1`?** Three possible explanations:

1. Compensating for Python's exclusive upper bound (inclusive → exclusive)
2. Compensating for 0-based indexing (count → index)
3. Adding a sentinel element

Without context, the reader must analyze surrounding code to infer intent. This is cognitive overhead.

### Replace Ambiguous Adjustments with Semantic Identifiers

**Preferred form:**

```python
range(bottles + inclusive)
```

The identifier `inclusive` self-documents the reason for the adjustment.

### Standard Semantic Identifiers

Most packages define semantic identifiers in a module named `_semiotics.py` or `theTypes.py`. Common semantic identifiers include:

```python
inclusive: int = 1
"""Include the last value in a `range`: change from [p, q) to [p, q]."""

zeroIndexed: int = 1
"""Adjust a count to an index: compensate for 0-based indexing."""

decreasing: int = -1
"""Iterator direction: reverse traversal."""

offsetForExclusiveUpperBound: int = 1
"""Adjust for Python's exclusive upper bound in range()."""
```

These identifiers are typically re-exported by `__init__.py` files for package-wide availability.

### When to Define a New Semantic Identifier

If an adjustment appears multiple times in a module and its purpose is not immediately obvious, define a semantic identifier.

**Anti-pattern (repeated ambiguous adjustment):**

```python
for idx in range(len(collection) - 1):  # Why - 1?
    process(collection[idx], collection[idx + 1])  # Why + 1?
```

**Preferred (semantic identifier):**

```python
# In _semiotics.py or module-level constants
offsetForPairwiseComparison: int = 1
"""Adjustment for accessing the next element in pairwise iteration."""

# In code
for idx in range(len(collection) - offsetForPairwiseComparison):
    process(collection[idx], collection[idx + offsetForPairwiseComparison])
```

### Importing Semantic Identifiers

Import semantic identifiers from the package's public API:

```python
from packageName import inclusive, zeroIndexed, decreasing
```

If the package does not re-export them, import from `_semiotics`:

```python
from packageName._semiotics import inclusive, zeroIndexed, decreasing
```

Never define semantic identifiers inline. Centralize them in `_semiotics.py` for SSOT.

---

## Comparison Operator Standardization

### Use Only Less-Than Orientation

Standardize all comparison operators to use `<` or `<=` rather than `>` or `>=`. This eliminates variation, reducing cognitive load and the risk of transcription errors.

**Rationale**:

- Consistent orientation reduces the number of patterns readers must recognize
- `<` and `<=` naturally align with left-to-right reading
- Eliminates the need to mentally "flip" comparisons during review

**Anti-pattern:**

```python
if maximum > value:
    takeAction()

if minimum >= threshold:
    proceedWithOperation()
```

**Preferred:**

```python
if value < maximum:
    takeAction()

if threshold <= minimum:
    proceedWithOperation()
```

### When Operand Order Matters

If the natural reading order requires `>`, swap the operands:

```python
# Natural phrasing: "If the maximum exceeds the value..."
# Standard form: "If the value is less than the maximum..."
if value < maximum:
```

This may feel unnatural at first but becomes automatic with practice. The benefit is a codebase where every comparison follows the same visual pattern.

---

## Import Statement Organization

### Import Statement Formatting: Nunya

`isort` will handle it: it's nunya business.

### Import from Public APIs

Import from the highest-level public interface of a package, not from internal submodules.

**Anti-pattern (importing from private modules):**

```python
from thirdPartyPackage._internal._submodule import publicSymbol
```

**Preferred (importing from public API):**

```python
from thirdPartyPackage import publicSymbol
```

If a package re-exports symbols at the top level via `__init__.py`, use the re-export rather than importing from deeper modules.

### Relative Imports in Local Packages

For modules within the same package, prefer absolute imports over relative imports:

**Preferred:**

```python
from packageName.submodule import helper
```

**Anti-pattern:**

```python
from .submodule import helper
```

Absolute imports make it immediately clear where symbols originate, especially when reviewing code outside the editor.

---

## Working with Existing Package Conventions

### Discovering Semantic Identifiers

Before defining new semantic identifiers, check whether the package already has them:

1. Look for `_semiotics.py` in the package root or subpackages
2. Look for `_theTypes.py` or `theTypes.py` (may contain semantic constants in addition to type definitions)
3. Check `__init__.py` to see what identifiers are re-exported

**Example (mapFolding package):**

```python
# mapFolding/_semiotics.py defines:
inclusive: int = 1
zeroIndexed: int = 1
decreasing: int = -1

# mapFolding/__init__.py re-exports them:
from mapFolding._semiotics import inclusive, zeroIndexed, decreasing
```

### When to Propose New Semantic Identifiers

If you encounter an ambiguous literal that:

- Appears multiple times in the code
- Has no existing semantic identifier
- Requires context to understand

Then propose a new semantic identifier. Report it to the user with:

- The proposed identifier name
- Its value
- Its docstring
- Where it should be defined (typically `_semiotics.py`)
- Whether it should be re-exported in `__init__.py`

---

## Transformation Workflow

### Step 1: Identify Violations

Scan code for:

- **Deferred operators**: Operators appearing after expressions they modify
- **Hidden operators**: `~`, unary `-`, or subscripting in complex expressions
- **Ambiguous literals**: Numeric constants without semantic meaning
- **Wrong comparison orientation**: Use of `>` or `>=`
- **Disorganized imports**: Import statements not grouped or ordered correctly

### Step 2: Locate Semantic Identifiers

Check the package for `_semiotics.py` or equivalent. Read its contents to discover available semantic identifiers.

### Step 3: Transform Expressions

For each violation:

**Deferred operators:**

1. Determine whether the expression is simple or complex
2. If complex, add parentheses or use explicit function calls (`operator.getitem`)

**Hidden operators:**

1. Replace `~` with `operator.invert`
2. Replace unary `-` with `operator.neg`
3. Replace complex subscripting with `operator.getitem`

**Ambiguous literals:**

1. Identify the adjustment's purpose from context
2. Find or propose a semantic identifier
3. Import the semantic identifier
4. Replace the literal with `literal_value + semantic_identifier` or equivalent

**Wrong comparison orientation:**

1. Swap operands to use `<` or `<=`
2. Verify the swapped form has the same semantics

### Step 4: Verify No Behavior Change

After transformations:

1. Read the transformed code and verify it computes the same result
2. Run syntax verification: `pylance-mcp-server/pylanceFileSyntaxErrors`
3. If tests exist, run them to confirm behavior preservation

---

## Examples

### Example 1: Deferred Operator

**Before:**

```python
leafNearest = state.mappingPileToLeaf[pileIndex] - 1
```

**After (simple expression, parentheses sufficient):**

```python
leafNearest = (state.mappingPileToLeaf[pileIndex] - 1)
```

**Or (complex expression, explicit indexing):**

```python
leafNearest = operator.getitem(state.mappingPileToLeaf, pileIndex) - 1
```

### Example 2: Hidden Operator

**Before:**

```python
result = computeHash(~mask & 0xFF)
```

**After:**

```python
result = computeHash(operator.invert(mask) & 0xFF)
```

### Example 3: Ambiguous Literal

**Before:**

```python
for index in range(len(collection) - 1):
    compare(collection[index], collection[index + 1])
```

**After:**

```python
# Assuming _semiotics.py defines:
# offsetPairwise: int = 1
# """Access the next element in pairwise iteration."""

from packageName import offsetPairwise

for index in range(len(collection) - offsetPairwise):
    compare(collection[index], collection[index + offsetPairwise])
```

### Example 4: Comparison Orientation

**Before:**

```python
if threshold > minimum:
    issueWarning()

if maximum >= value:
    clampToMaximum()
```

**After:**

```python
if minimum < threshold:
    issueWarning()

if value <= maximum:
    clampToMaximum()
```
