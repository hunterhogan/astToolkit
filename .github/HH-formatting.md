# Python Code Formatting Standards

Standards for Python code formatting: horizontal structure, vertical structure, indentation, delimiter layout, and whitespace semantics.

## Configuration Hierarchy

1. **.editorconfig** — Authoritative for basic settings (indentation, line endings, trailing whitespace, final newline).
2. **pyproject.toml** — Authoritative for all settings not in .editorconfig.
3. **Repository conventions** — Infer from existing code when explicit configuration is absent.

Before formatting, read .editorconfig and pyproject.toml from the repository root. Use values from .editorconfig for indentation style, indentation size, line endings, trailing whitespace policy, and final newline requirements.

## Foundational Principle: Left-to-Right Foreshadowing

Structure code so that readers encounter syntactic signals before the elements they govern. The reader should never be surprised by an operator or modifier encountered late in a statement.

## Horizontal Structure

### Line Length

- Prefer keeping function and method signatures on a single line when possible.
- If a signature must wrap, apply semantic line breaking (see below), not arbitrary character-count breaking.
- Do not use automated formatters (Black, yapf, autopep8) unless the repository already uses them consistently.

### Line Continuation

- **Prefer parentheses** for implicit line continuation.
- **Avoid backslash continuation** (`\`). The continuation marker at line end forces the reader to scan rightward to discover that the statement continues.

**Anti-pattern (backslash continuation):**

```python
isConditionMet = someFunction(argumentOne, argumentTwo) \
    + anotherFunction(argumentThree)
```

**Preferred (parenthetical continuation):**

```python
isConditionMet = (
    someFunction(argumentOne, argumentTwo)
    + anotherFunction(argumentThree)
)
```

### Semantic Line Breaking

Break lines at semantic boundaries, not at arbitrary character counts.

- Break before binary operators, not after.
- Keep logically related tokens on the same line.
- Preserve parallel structure across related lines.

## Vertical Structure

### Blank Line Policy

- Never insert more than one consecutive blank line.
- Insert one blank line between logical "paragraphs" of code.
- Insert one blank line before and after banner comments.

### Banner Comments

Major logical divisions use a banner comment with equals signs:

```python
#======== Section Title ========================================

```

- Comment marker, no space, eight equals signs reaching column 10, space, section title, space, equals signs to fill.
- One blank line before the banner.
- One blank line after the banner (required for folding behavior in editors).

Subdivisions within a major section use minus signs with identical formatting:

```python
#-------- Subsection Title -------------------------------------

```

### Vertical Grouping

- Group related definitions contiguously.
- Separate groups with a single blank line.
- Within a group, order alphabetically unless dependency ordering is required.

## Indentation and Continuation

### Indentation Settings

Obtain indentation style (spaces or tabs) and indentation size from .editorconfig.

### Continuation Indentation

For multi-line expressions, indent continuation lines one level from the start of the statement. Place connecting operators at the beginning of continuation lines to signal that the logical statement continues. Place the closing delimiter on its own line, aligned with the statement start, to clearly terminate the logical statement.

**Preferred pattern:**

```python
if ((addendDimension一零 in [一, 二, 三, 四])
    or ((addendDimension一零 == 五) and (addendDimension首零 != 一))
    or (addendDimension一 in [二, 三])
    or ((addendDimension一 == 一) and not (addendDimension零 == addendDimension首零 and addendDimension一零 < 0))
):
```

This structure provides:

- **Foreshadowing**: The opening `((` signals a complex expression.
- **Connection**: Each `or` at line start connects to the previous line.
- **Termination**: The `):` on its own line clearly ends the condition.

**Multi-line function calls:**

```python
processData(
    sourceFile
    , destinationPath
    , compressionLevel
)
```

### Closing Delimiter Placement

- If elements are on separate lines, place the closing delimiter on its own line.
- For `import` statements, the closing delimiter may appear on the same line as the final import.

## Delimiter Layout and Comma Placement

### Comma Position Encodes Semantic Information

Comma placement signals whether element order is semantically significant.

#### Trailing Commas: Order-Agnostic Collections

When elements can be reordered without affecting correctness, use trailing commas:

```python
listColors = [
    "blue",
    "green",
    "red",
]
```

#### Leading Commas: Order-Significant Sequences

When element order is meaningful (positional correspondence, algorithmic sequence), use leading commas:

```python
@pytest.mark.parametrize("inputValue", [
    caseAlpha
    , caseBeta
    , caseGamma
], ids=["alpha", "beta", "gamma"])
```

Leading commas create a visual marker at the semantic boundary and cause syntax errors if elements are accidentally reordered.

#### Function Arguments: Always Order-Significant

Multi-line function calls use leading commas because argument order is always significant:

```python
processData(
    sourceFile
    , destinationPath
    , compressionLevel
)
```

Single-line calls use standard comma placement: `processData(sourceFile, destinationPath, compressionLevel)`.

## Import Statement Formatting: Nunya

`isort` will handle it: it's nunya business.

## Quotation Mark Conventions

### Docstrings

- Always use triple double quotes: `"""`.
- Use raw strings (`r"""`) when the docstring contains backslashes.
- In rare cases requiring single quotes, add a `# NOTE` comment explaining the necessity.

### String Literals

| Context                      | Quotation Style                           |
| ---------------------------- | ----------------------------------------- |
| General string literals      | Single quotes: `'text'`                   |
| f-strings                    | Double quotes: `f"text {variable}"`       |
| Format strings (`.format()`) | Double quotes: `"template {placeholder}"` |
| Multi-line strings           | Triple double quotes: `"""text"""`        |
| Raw strings (regex)          | `r'pattern'` only when necessary          |

### Path Literals

Never use raw strings for file paths. Use `pathlib.Path` objects to construct, sanitize, and transport path data. Convert to string only at the interface boundary.

## Whitespace Semantics

### Trailing Whitespace

Remove trailing whitespace from all lines. Configure your editor to strip trailing whitespace on save.

### Vertical Alignment

Vertical alignment of related elements serves two cognitive functions: it enables rapid visual scanning and reveals lateral relationships between declarations.

#### When to Use Vertical Alignment

Use vertical alignment when:

- **Related variable declarations** share common structure (type annotations, initialization patterns)
- **Assignment statements** form a logical group with parallel roles
- **Type annotations** reveal conceptual relationships between variables
- **Tabular data** benefits from column-based reading
- **Dictionary literals or configuration blocks** where keys form a semantic category

```python
indexFirst:      int
indexLast:       int
indexCurrent:    int
valueMinimum:    float
valueMaximum:    float
valueAverage:    float
```

The alignment reveals two conceptual groups (index-related integers, value-related floats) that would be obscured by ragged formatting.

```python
pathInput       = Path(configFile)
pathOutput      = Path(resultsFile)
pathCache       = Path(cacheDirectory)
pathLogs        = Path(logDirectory)
```

#### When to Avoid Vertical Alignment

Do not use vertical alignment when:

- Elements lack semantic relationships (arbitrary code that happens to appear consecutively)
- The group is temporary or likely to change frequently
- Alignment obscures more important structure (e.g., indentation levels)
- Only two or three lines would be aligned (insufficient benefit for maintenance cost)

#### Alignment Preservation

When editing code with intentional columnar alignment (aligned `=` signs, aligned annotations, tabular data), preserve the alignment pattern. Do not collapse or reformat aligned blocks unless they violate other formatting rules.

If adding a new element to an aligned block, extend the alignment column if necessary to accommodate the new element. Update all lines in the block to maintain consistent alignment.
