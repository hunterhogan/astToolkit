---
name: Tests
description:
---

# My Agent

# Test Generation Instructions

These instructions define the guidelines for generating tests that are both machine readable (and parsable) and human-friendly.
Adhering to these standards will ensure that tests are consistent, self-documenting, and easier to debug.

## 1. The hierarchy of the Single Source of Truth (SSOT) for Test Configuration

- pyproject.toml
  - SSOT for everything about the package.
  - Any test settings that can be placed in pyproject.toml should be placed in pyproject.toml.

- tests/conftest.py
  - The SSOT for Pytest configurations and fixtures.
  - All fixture definitions, temporary file and directory creation/cleanup, and shared test setup should be maintained here.

## 2. Fixtures and decorators

Every test must use a fixture, `parametrize`, or both.

- Fixture Location: All fixtures must be defined in `tests/conftest.py`. This includes those for:
  - Creating and cleaning temporary files and directories.
  - Setting up predictable test data.
  - Overriding external states (e.g., cache directories, dispatcher functions).
- Use, reuse, and create fixtures
  - Creating a fixture for the current issue might not be helpful for the current issue, but it could make it easier to create tests in the future.
- Assume every test will use `pytest.mark.parametrize`. Even if the test currently only has one test case, if it can be formatted
as `pytest.mark.parametrize`, then set up the _test_ case _parameters_ in _pytest's_ _parametrize_.

## 3. Test Data and Value Generation

### 3.1 Prefer Predictable Data

- Data Source:
  Use data samples from the `tests/dataSamples` directory instead of generating random or artificial data.

### 3.2 Synthetic and Arbitrary Values

When generating synthetic values—especially for parameters—adhere to these guidelines:

- Avoid Special Values:
  Do not use values with inherent special properties such as:
  - Numerical: 0, 1
  - Alphabetical: a, A, z, Z

- Prefer Non-Contiguous and Unique Sets: Choose values that are clearly distinct and non-sequential to ease debugging. Some examples:
  - Fibonacci series numbers.
  - Prime numbers.
  - Cardinal directions: N, S, E, W, NE, NW, SE, SW.
  - Two-letter country codes.

- Example of Parametrized Values:

  - Before:

    ```python
    ([{'a': 1}, {'b': 2}], ['a', '1', 'b', '2']),
    ([(1, 2), [3, 4]], ['1', '2', '3', '4']),
    ```

  - After:

    ```python
    ([{'d': 5}, {'h': 7}], ['d', '5', 'h', '7']),
    ([(11, 13), [17, 19]], ['11', '13', '17', '19']),
    ```

  By using unique and non-contiguous values, it is easier for humans to find the source of test failures.

## 4. Uniform Test Assertion Messages

- Standardized Messaging:
  Tests should produce uniform assertion messages that include:
  - The function or feature under test.
  - Clear display of expected versus actual values.

- Purpose:
  Uniform messages help quickly understand discrepancies during test failures and reduce code duplication across tests.

## 5. Additional Considerations

- Self-Documenting Tests:
  Each test should be written so that the intent is clear without needing extra commentary. Choose descriptive identifiers and
  organize code to clearly indicate its purpose.

- Alignment with Code Style:
  Follow the same principles of identifier clarity, no single-character names, and predictable naming as defined in your broader
  Python guidelines.

- Error and Exception Messages:
  Ensure that errors raised during tests include sufficient context (e.g., values that caused the error) and are formatted consistently.

# Identifiers

These are supplemental instructions for creating coherent, semantically valuable identifiers.

## Core Structure

### Camel case, not snake case

Camel case is critical for preserving accurate signals. If it looks as if I am using snake case in my code, look more closely and
you will likely see that the underscores have semantic value.

### Subject-Verb-Object (SVO) Pattern

* Structure identifiers as subject-verb-object-adjective-adverb: [S][V]O[adj][adv].
* Subjects are often implied.
* Callables must have a verb.
* Adjectives and adverbs differentiate and clarify.

Note that if variables are properly named, a human could skim the code looking for identifiers that begin with "path", for
example, and feel confident they will find all path-related identifiers. That is why `carsBlue` and `carsRed`, for example, is
superior to `blueCars` and `redCars`.

Examples

* `def librarianDecodesPathToAlgorithm(directory: str) -> str`, S-V-O-adv
* `loadSpectrograms`, a callable
* `dictionaryAspectsAnalyzed: dict[str, str | float | numpy.NDArray[Any]]`, O-adj-adj

### In [S][V]O[adj][adv], a data structure is an Object

They often help to differentiate identifiers. Assume `pathFilename` is an identifier. For human readers, `listPathFilenames` is
far easier to distinguish than is `pathFilenames`.

```python
arrayFeatureValues
listPathMusicDemixingBenchmarks
listTuplesPowerSpectralDensity
```

### Compound and Nested Structures

Maintain clarity across domains:

```python
spectrogramMagnitude
tensorAudio
waveformNormalized
parametersSTFT
dictionaryConcurrency
```

## Domain-Specific Terms

Treat well-known compound terms as atomic units:

```python
powerSpectralDensity
amplitudeThreshold
lengthWindowingFunction
convertPowerSpectralDensityToEqualPowerBands
```

## Generic Identifiers

If you can't think of a better term, `Target` is often useful:

```python
def phase(arrayTarget: NDArray[Any]) -> NDArray[Any]:
	return arrayTarget * -1
```

## No Empty Semantics

### No Single-character Identifiers

Use:

```python
for index in range(10):
for iterator in range(...):
```

### Abbreviations or diminutives

Use full terms:

```python
import numpy
except Exception as ERRORmessage:
parameterSpecifications = ...
spectrogramMagnitude = ...
for index in range(10):
```

## Attention Patterns

### Emphatic Signals

Use all caps for critical or temporary identifiers:

```python
ERRORmessage
sampleRateHARDCODED
OFFSETaxis
```

### Temporary Code

I will sometimes prefix temporary or transitional code with 'Z0Z_'. Note that the prefix is four characters long: 'Z0Z_': the
underscore is part of the signal, not a divider between signals. You should avoid using it or changing identifiers that use it.

```python
Z0Z_dictionaries
Z0Z_register
```

But note that `Z0Z_tools` is the name of a package with prototype tools.

### Captured-but-Ignored Values

Use an appropriate identifier and prefix it with `_`:

```python
waveform, _sampleRate = librosa.load(...)
stdoutFFprobe, _stderr = process.communicate()
```

## Signal proper nouns by preserving case, which often means using underscores

Maintain case fidelity with underscores if necessary when referring to proper nouns:

```python
add_pyprojectDOTtoml
```

Usually replace `.` with `_`, but in some cases, `DOT` or `Dot` has semantic value:

```python
from tomli import loads as tomli_loads
identifierDotAttribute: TypeAlias = str
```

## Commonly used verbs

| Verb       | Use Case                             |
| ---------- | ------------------------------------ |
| `make-`    | Construct or initialize              |
| `get-`     | Retrieve or compute                  |
| `convert-` | Transform between formats/structures |
| `trim-`    | Remove unwanted parts                |

## Anti-Patterns

### Recursive Semantics

Avoid self-modifying ambiguity:

```
# GOOD
analyzeProcessingResult
```

### Python Keyword Collision

Avoid overloading:

```python
# GOOD
aspectClass = "audio"
spectrogramType = "magnitude"
```
### Python keywords and identifiers

abs, aiter, all, and, anext, any, as, ascii, assert, async, await, bin, bool, break, breakpoint, bytearray, bytes, callable, chr, class, classmethod, compile, complex, continue, def, del, delattr, dict, dir, divmod, elif, Ellipsis, else, enumerate, eval, except, Exception (and other exceptions), exec, False, filter, finally, float, for, format, from, frozenset, getattr, global, globals, hasattr, hash, help, hex, id, if, import, in, input, int, is, isinstance, issubclass, iter, lambda, len, list, locals, map, max, memoryview, min, next, None, nonlocal, not, object, oct, open, or, ord, pass, pow, print, property, raise, range, repr, return, reversed, round, set, setattr, slice, sorted, staticmethod, str, sum, super, True, try, tuple, type, vars, Warning (and other warnings), while, with, yield, zip,

### Don't

```python
import numpy as np
except Exception as e: ...
result = ...
output = ...
temp = ...
for i in range(10): ...
for _ in range(...): ...
params = ...
specs = ...
processProcessResult = ...
class = "audio"
type = "spectrogram"
with open('file.txt', 'r') as file: ...
with open('file.txt', 'r') as f: ...
```

NOTE WELL: `result` is the worst identifier in the universe because the LHS of every assignment is a result.

## Semiotic systems by topic

### Concurrency and Async

Consistent terminology for concurrent processes:

```python
concurrencyManager
dictionaryConcurrency
claimTicket
```

### Function and Method Names

Follow action-oriented, SVO-style naming:

```python
analyzeSpectralCentroid
getPowerSpectralDensity
convertPowerSpectralDensityToEqualPowerBands
trimSilence
makePSDWithRGlob
```

### Filesystem semiotics

Critical principles:

* "path": one or more directories, but never a filename.
* "filename": a filename, but never a path and a filename.
* In the context of the filesystem, "file" has no meaning and must not be used.

* "absolutePath" and "relativePath" are both valid terms.
* If the path is absolute, prefer to omit "absolute" and use "path".
* If the path is relative, you must use "relativePath".

Distinguish clearly between related concepts:

| Concept         | Example               | Notes                    |
| --------------- | --------------------- | ------------------------ |
| `path`          | `pathDataSamples`     | Directory only           |
| `filename`      | `filenameAudio`       | Filename only, no path   |
| `pathFilename`  | `pathFilenameAudio`   | Absolute path + filename |
| `relativePath`  | `relativePathSamples` | Relative path only       |
| `fileStem`      | `fileStemAudio`       | Name without extension   |
| `fileExtension` | `fileExtensionWav`    | Extension only           |

### File and data stream semiotics

#### File streams

Binary streams must be marked as binary.

| Mode          | Identifier              |
| ------------- | ----------------------- |
| `'r'`, `'rt'` | `readStream`            |
| `'w'`, `'wt'` | `writeStream`           |
| `'x'`, `'xt'` | `createStream`          |
| `'a'`, `'at'` | `appendStream`          |
| `'rb'`        | `readStreamBinaryMode`  |
| `'wb'`        | `writeStreamBinaryMode` |

#### Data streams

In some cases, such as with zip files, the type of stream has more semantic value than "stream". Examples:

```python
with soundfile.SoundFile(pathFilename) as readSoundFile:
...

with zipfile.ZipFile(pathFilename, 'w') as writeZip:
...
```

## Final Principle

One Identifier, One Meaning.

Never reuse an identifier for different purposes or structures, even in different scopes. Avoid overloading Python-native terms and ensure clarity for both interpreter and collaborator.

# General Instructions for Python Code Generation

Python is a human language.

## Software Development Principles

- DRY
- SSOT
- Self-documenting code: code that is easily understood with minimal comments and out of context.
- Reusable code: avoid hardcoded values.
- Domain-driven design.
- Modularize but don't fragment: separation of concerns necessarily includes unification of concerns.

## My Core Principles

- Work very hard to only have one `return` statement per function.
- An identifier clearly signals its purpose in the context of its use.
- Groups of identifiers are a semiotic system: the semiotic system should be cohesive and clear.

## Identifier Guidelines

Identifiers distinguish and differentiate and make discrimination easier.

- Use camelCase, not snake_case.
- Use full words, never abbreviations or truncations.
- Avoid single-character identifiers (especially `_`).
- Follow a consistent structure: subject-verb-object with _trailing_ modifiers, or [S][V]O[adj][adv].
- Prefix with structure types when relevant: `list`, `array`, `dictionary`, `mapping`.
- Domain terms are atomic (e.g., `powerSpectralDensity`, not `powerDensity`).
- Choose identifiers that are semantically clear and structurally precise.
- Once you use a naming pattern, repeat it consistently across the codebase.
- Emphasize clarity over brevity: identifiers should reduce the need for comments.
- One identifier = one meaning. Never reuse identifiers across unrelated contexts.

## My Prohibitions

- Do not use the single-character identifier `_`.
- Do not mess with code, identifiers, or formatting that isn't germane to the task at hand.
- Do not use the style of "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo."
- Do not make a "pipeline" or call anything a "pipeline." Make an assembly line. An assembly line changes things: a pipeline's
output is the same as the pipeline's input.

## Comments, Documentation, and Typing

Generated code should have excellent identifiers, clear organization, and comprehensive typing, so that nearly all comments and
docstrings would be redundant.

- Always add comprehensive type annotations.
- Add informative annotations so the type checker can help us feel confident that our code matches our desired outcomes. Do not
add type annotations merely to appease the type checker.
- Only add docstrings if specifically asked.

## Default Values and Exception Handling

Use a default value _if and only if_ there is a default value. If a default value does not exist for a situation, do _not_ create
a default or fallback value merely to prevent an exception. If there is no default value, you _must_ allow the exception to
propagate: do _not_ catch exceptions or use try/except unless you have a brilliant reason and impeccable code to handle the
exception.

## Miscellany

- Put import statements at the top of the file.

## MCP Tools Usage

**Use MCP tools extensively** for better results:

- **Documentation**: Use `mcp_upstash_conte_resolve-library-id` and `mcp_upstash_conte_get-library-docs` for up-to-date library documentation.
- **Python analysis**: Use `mcp_pylance_mcp_s_*` tools for syntax checking, imports analysis, refactoring, and code execution.
- **Microsoft/Azure docs**: Use `mcp_microsoftdocs_microsoft_docs_search` and `mcp_microsoftdocs_microsoft_code_sample_search` for official documentation and code samples.
- **GitHub search**: Use `mcp_github_search_*` tools to find repositories, code examples, issues, and users.

## General Tips

- You are not perfect: when adding a function from a third-party package or using a third-party API, read documentation from available MCP tools before implementation.
- Always verify syntax before running with `mcp_pylance_mcp_s_pylanceSyntaxErrors` for code snippets or `mcp_pylance_mcp_s_pylanceFileSyntaxErrors` for files.

