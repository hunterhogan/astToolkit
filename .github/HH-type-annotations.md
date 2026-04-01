# Type Annotation Instructions

Standards for Python type annotations emphasizing precision, completeness, modern syntax (PEP 585/604), and paradigm improvements (TypedDict, Protocol, TypeVar, overload).

## Core Philosophy

Type annotations are engineering tools that prevent bugs, communicate intent to human readers, and enable editor/tooling assistance. Every annotation must carry practical value. Completeness matters: annotate everything precisely—every function signature (all parameters and return types), every variable binding, every class attribute.

## Prohibited Types

### `Any` and `object` Are Prohibited

**Never annotate with `Any` or `object`.** These erase type information and defeat the purpose of type annotations.

When tempted to use `Any`:

| Situation                              | Use Instead                       |
| -------------------------------------- | --------------------------------- |
| Multiple possible types                | Union: `str \| int \| float`      |
| Truly polymorphic code                 | `TypeVar` with appropriate bounds |
| Dict with known keys                   | `TypedDict`                       |
| Accepts anything with specific methods | `Protocol`                        |
| Heterogeneous collection               | `list[str \| int]`                |

**Acceptable `Any` uses (extremely rare):**

- Third-party library genuinely returns `Any` and documentation confirms no better type exists
- Variadic `*args`/`**kwargs` that genuinely accept unbounded types
- Must be documented with justification

### Weak Types Are Prohibited

Replace bare containers with parameterized versions:

| Weak (Prohibited) | Strong (Required)                             |
| ----------------- | --------------------------------------------- |
| `dict`            | `dict[str, int]` or `Mapping[str, int]`       |
| `list`            | `list[str]` or `Sequence[str]`                |
| `tuple`           | `tuple[int, str, float]` or `tuple[int, ...]` |
| `set`             | `set[int]`                                    |
| `Callable`        | `Callable[[int, str], bool]`                  |
| `Iterator`        | `Iterator[str]`                               |
| `Generator`       | `Generator[YieldT, SendT, ReturnT]`           |

## Annotation Style (Non-Negotiable)

### PEP 585 Style (Required)

Use built-in generics, not `typing` module equivalents:

| Correct (PEP 585) | Incorrect         |
| ----------------- | ----------------- |
| `list[int]`       | `List[int]`       |
| `dict[str, int]`  | `Dict[str, int]`  |
| `tuple[int, str]` | `Tuple[int, str]` |
| `set[str]`        | `Set[str]`        |
| `frozenset[int]`  | `FrozenSet[int]`  |
| `type[MyClass]`   | `Type[MyClass]`   |

### PEP 604 Style (Required)

Use `|` for unions, not `Optional` or `Union`:

| Correct (PEP 604)     | Incorrect                |
| --------------------- | ------------------------ |
| `int \| None`         | `Optional[int]`          |
| `str \| int \| float` | `Union[str, int, float]` |
| `int \| None`         | `Union[int, None]`       |

### Container Abstraction Preference

For function parameters that only read from containers, prefer abstract types from `collections.abc`:

| Situation           | Prefer                                     | Over              |
| ------------------- | ------------------------------------------ | ----------------- |
| Read-only sequence  | `Sequence[T]`                              | `list[T]`         |
| Read-only mapping   | `Mapping[K, V]`                            | `dict[K, V]`      |
| Iterable (one-time) | `Iterable[T]`                              | `list[T]`         |

**Return types:** Use concrete types (`list[T]`, `dict[K, V]`) since callers can do whatever they want with the returned value.

## Prohibited Patterns

### Never Create Annotation-Only Statements

Do not create variable declarations with type annotations but no assignment:

**Prohibited:**

```python
def processData(start: int, stop: int, step: int) -> None:
    startAuthoritativeData: int
    stopAuthoritativeData: int
    stepAuthoritativeData: int
    # ... later assignments
```

**Required:**

```python
def processData(start: int, stop: int, step: int) -> None:
    # Annotate at point of assignment
    startAuthoritativeData: int = calculateStart(start)
    stopAuthoritativeData: int = calculateStop(stop)
    stepAuthoritativeData: int = validateStep(step)
```

If a variable truly needs declaration before assignment (rare), use actual initialization or reconsider the code structure.

### Never Expand Unpacking for Annotations

Do not convert idiomatic unpacking into multiple statements just to add type annotations:

**Prohibited:**

```python
tupleChicken = chicken()
xx: int = tupleChicken[0]
yy: float = tupleChicken[1]
```

**Required:**

```python
# Preserve unpacking - type is documented via function signature
xx, yy = chicken()
```

If the unpacked types are unclear from context, improve the return type annotation of the source function instead:

```python
def chicken() -> tuple[int, float]:
    """Return count and weight."""
    return 42, 3.14
```

**Rationale:** Preserving idiomatic Python patterns (like unpacking) is more valuable than explicit type annotations at every binding site. Type information should flow from function signatures, not require destructuring every tuple.

## Completeness Requirements

### Annotate All Identifiers

Every identifier must have a type annotation at its first authoritative introduction:

**Required annotations:**

- [ ] Every function/method parameter (including `self`, `cls` when needed)
- [ ] Every function/method return type (including `-> None`)
- [ ] Variables where type is not obvious from the right-hand side
- [ ] Class attributes (both instance and class-level)
- [ ] Module-level constants and variables
- [ ] Exception handler bindings (when used beyond the except block)
- [ ] Comprehension targets (when necessary for clarity)

**Examples:**

```python
# Function signatures - complete
def processData(
    sourceData: list[dict[str, int]],
    filterPredicate: Callable[[dict[str, int]], bool],
    maximumResults: int | None = None,
) -> list[dict[str, int]]: ...

# Variables - annotate when type not obvious
dataProcessed: list[dict[str, int]] = []  # Type not obvious from []
counterFiles = 0  # Type obvious from literal, annotation optional
pathConfiguration: Path = getConfigPath()  # Type not obvious from call

# Class attributes
class DataProcessor:
    """Process data with configurable settings."""

    # Class attribute
    defaultBatchSize: int = 100

    def __init__(self, sourcePath: Path) -> None:
        # Instance attributes
        self.sourcePath: Path = sourcePath
        self.recordsProcessed: int = 0
        self.errorLog: list[str] = []
```

## Type Source Precedence

When multiple type sources are available, select types in this precedence order:

1. **Same module**: Types defined in the current file
2. **Same package**: `_theTypes.py`, `_semiotics.py`, `_theSSOT.py` in the package
3. **Parent package types**: `hunterMakesPy.theTypes` (if dependency exists)
4. **Third-party**: Library's public type API
5. **Standard library**: `typing`, `collections.abc`, builtins

**Rationale:** Choose the most local type that accurately describes the value. Local types are more specific to the domain and easier to maintain.

## Adding Imports for Annotations

Type annotations may require importing types that aren't used at runtime.

### Standard Library Imports

Import from modern locations:

```python
# Correct
from collections.abc import Callable, Iterator, Sequence, Mapping
from typing import TypedDict, Protocol, TypeVar, overload, TYPE_CHECKING

# Incorrect - old locations
from typing import Callable, Iterator, List, Dict, Optional, Union
```

### Annotation-Only Imports

Use `TYPE_CHECKING` to avoid runtime import costs and circular dependencies:

```python
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from expensive_module import HeavyType
    from .sibling_module import RelatedClass
```

The `TYPE_CHECKING` constant is `False` at runtime, so the imports are only processed by type checkers.

### Import Organization

1. Group imports: standard library, third-party, local
2. Place `TYPE_CHECKING` block after regular imports
3. Keep annotations imports in the same grouping style as the rest of the file

## Paradigm Improvements

### When to Suggest TypedDict

Replace `dict[str, Any]` or unparameterized `dict` with `TypedDict` when:

- Dictionary has consistent string keys across usage
- JSON-like structures with known schemas
- Configuration dictionaries with known fields
- API response/request structures

**Before:**

```python
def processConfig(config: dict[str, Any]) -> bool:
    host: str = config["host"]
    port: int = config["port"]
    timeout: float | None = config.get("timeout")
    ...
```

**After:**

```python
from typing import TypedDict

class ServerConfig(TypedDict, total=False):
    """Configuration for server connection."""
    host: str
    port: int
    timeout: float | None  # Optional field

def processConfig(config: ServerConfig) -> bool:
    ...
```

### When to Suggest Protocol

Replace structural duck typing with `Protocol` when:

- Functions use only specific attributes/methods of parameters
- Multiple types share common interface but no inheritance
- `Any` used because "different types but same interface"

**Before:**

```python
def readData(source: Any) -> str:
    return source.read()  # Works for TextIO, BinaryIO, StringIO, etc.
```

**After:**

```python
from typing import Protocol

class Readable(Protocol):
    """Protocol for objects that support reading."""
    def read(self, size: int = -1) -> str: ...

def readData(source: Readable) -> str:
    return source.read()
```

### When to Suggest @overload

Use `@overload` when:

- Return type depends on input type
- Return type depends on a flag parameter value
- Union returns where actual type is deterministic per call

**Before:**

```python
def getValue(key: str, default: int | None = None) -> int | str:
    # If default is None, returns str; if default is int, returns int
    ...
```

**After:**

```python
from typing import overload

@overload
def getValue(key: str, default: None = None) -> str: ...

@overload
def getValue(key: str, default: int) -> int: ...

def getValue(key: str, default: int | None = None) -> int | str:
    ...
```

### When to Suggest TypeVar

Use `TypeVar` when:

- Functions return the same type as an input
- Container-preserving transformations
- Generic algorithms that work on any type

**Before:**

```python
def getFirst(items: list[Any]) -> Any:
    return items[0] if items else None
```

**After:**

```python
from typing import TypeVar

TypeElement = TypeVar("TypeElement")

def getFirst(items: list[TypeElement]) -> TypeElement | None:
    return items[0] if items else None
```

## Test Module Annotations

Test modules intentionally use invalid types to verify error handling. Use block directives to suppress false positives:

**Correct:**

```python
# pyright: reportArgumentType=false
def test_invalid_input_handling():
    assert functionUnderTest('invalid') == expectedError
    assert functionUnderTest(None) == expectedError
    assert functionUnderTest(-1) == expectedError
# pyright: reportArgumentType=true
```

**Incorrect:**

```python
# Don't use per-line suppression for multiple lines
assert functionUnderTest('invalid') == expectedError  # type: ignore
assert functionUnderTest(None) == expectedError  # type: ignore
```

## Special Cases

### Cleanup of typing.cast

When encountering `typing.cast`:

1. **Investigate necessity**: Does the type checker truly need help?
2. **Remove if unnecessary**: The only permitted runtime behavior change
3. **Keep if necessary**: Ensure it's documented (via comment or docstring)
4. **Report uncertainty**: If you cannot determine necessity, flag for human review

### Identifier Rules for New Typing Constructs

When creating `TypeVar`, `TypedDict`, `Protocol`, `TypeAlias`:

- Follow workspace identifier conventions (typically camelCase)
- Use full words (no abbreviations)
- No single-character identifiers (except mathematical contexts with strong convention)
- Make names descriptive of the type's purpose or constraint

**Examples:**

```python
# Good
TypeElement = TypeVar("TypeElement")
TypeComparable = TypeVar("TypeComparable", bound=Comparable)

class ResponsePayload(TypedDict):
    statusCode: int
    messageBody: str

class Drawable(Protocol):
    def draw(self, canvas: Canvas) -> None: ...

# Bad
T = TypeVar("T")  # Too generic
Resp = TypedDict(...)  # Abbreviated
P = Protocol  # Single character
```
