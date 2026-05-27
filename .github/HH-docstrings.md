---
name: Docstring Standards
description: Standards for Python docstrings.
---
# Write Consistent, Precise NumPy-style Docstrings

Use [NumPy v1.10 style](https://numpydoc.readthedocs.io/en/v1.10.0/format.html#docstring-standard) with the following modifications and additions.

## Modifications to the NumPy Docstring Standards

1. Replace the generic "Notes" section with one or more semantic section names instead.
2. Public, non-method attributes must be documented.
3. Use Unicode for all mathematical symbols, not LaTeX.
4. Use plain text with NumPy-style section headers, not reStructuredText.
5. In a `class` docstring, put the Parameters section in the `__init__` method docstring, not the class docstring.

## Technical Syntax

- **Triple double quotes.** Always use `"""`, never `'''`.
- **Full stops.** End every sentence with a full stop, including the summary line.
- **No end-of-line colons in prose.** Machine parsers may interpret a trailing colon as syntax. Restructure the sentence instead.
- **No LaTeX.** Use Unicode characters for all mathematical symbols (e.g., ×, ÷, √, ∑, ≤, ∈, →).
- **No reST.** Do not use reStructuredText directives, roles, or markup (e.g., no `.. note::`, no `:param:`, no `:math:`). Write plain text with NumPy-style section headers.
- **Indentation.** Follow the project `.editorconfig` for indentation width and type. Within a docstring, indent continuation lines by one level relative to the section entry.
- **Line length.** Aim for about 102 characters per docstring line. Break earlier when it improves scanning.

## Docstring Layout

### Sections and their Order Within a Docstring

1. Summary line (on the same line as the opening triple quotes)
2. (AI generated docstring) marker, if applicable
3. Non-technical description
4. Technical section(s), when applicable
5. `Parameters`
6. `Returns` or `Yields`
7. `Raises`, judicious, not comprehensive
8. `Warns`, judicious, not comprehensive
9. `Other Parameters`
10. `See Also`
11. Extended discussions, details, warnings, gotchas, notes, and other information too lengthy or too narrow to put in a description: section names should have semantic value. Never use "Notes".
12. `Examples`
13. `References`

### Formatting a Docstring Section

Use this structure for named sections unless a later subsection defines a specialized layout:

```text
[blank line]
Section Name
------------
entry : datatype
    Definition or description.
entry : datatype = defaultValue
    Definition or description.
```

For `Mathematics` entries, the description may be a fenced block. Align the opening and closing
fences with the entry label, and indent the fenced contents one additional level.

### Formatting a Function

```python
def exampleFunction(parameterFirst: int, parameterSecond: str = "default") -> bool:
    """Validate input parameters and return success status.

    (AI generated docstring)

    You can use this function to validate input parameters before processing. The function
    checks each parameter against defined constraints and returns success status. Extended
    description uses explicit subjects to provide context. Cite references in text [1].

    Parameters
    ----------
    parameterFirst : int
        Description of the parameter.
    parameterSecond : str = "default"
        Description with default value noted after the type.

    Returns
    -------
    isValid : bool
        Description of the return value.

    References
    ----------
    [1] Relevant documentation or concept being referenced
        https://example.com/documentation
    """
```

### Formatting a Module

Place the module docstring at the very top of the file, before imports. Include a table of contents listing all public identifiers.

```python
"""Perform map-folding computations and analysis.

(AI generated docstring)

You can use this module to compute distinct foldings of multi-dimensional maps. The module
provides the core algorithms and orchestrates computation workflows. Extended description
of module purpose and organization.

Contents
--------
Functions
    functionAlpha
        One-line description of functionAlpha.
    functionBeta
        One-line description of functionBeta.

Classes
    ClassAlpha
        One-line description of ClassAlpha.

"""
import ...
```

#### Include all public identifiers in the table of contents

- List all public functions, classes, and other exported identifiers.
- If there are sections (`#======== Boolean filters ====`) and subsections (`#---- Specific filters ----`), reflect that hierarchy.
- Maintain alphabetical order within each section.
- Provide one-line descriptions for each item.
- Omit private identifiers (those starting with `_`).

### Formatting a Package `__init__.py`

Document what the package exposes and its organizational purpose. Include a table of contents of public modules and subpackages.

```python
"""Access map-folding algorithms and utilities.

(AI generated docstring)

You can use this package to compute distinct foldings of multi-dimensional maps. This package
provides implementations of various map-folding counting algorithms, state management for
parallel computations, and interfaces to OEIS sequences.

Modules
-------
basecamp
    Entry point for map-folding computations with algorithm selection.
dataBaskets
    State containers and data structures for folding computations.
filesystemToolkit
    Utilities for result persistence and caching.

Subpackages
-----------
algorithms
    Collection of map-folding algorithm implementations.
_e
    Experimental elimination-based algorithms (internal research code).
"""
```

#### Include all public modules and subpackages in the table of contents

- List public modules with brief descriptions.
- List subpackages with brief descriptions.
- Use section headers (`Modules`, `Subpackages`) with dashed underlines.
- Omit private modules (starting with `_`) unless they are documented internal APIs.

### Formatting a Top-Level Package `__init__.py`

The top-level `__init__.py` follows the same format as any package `__init__.py`, but the extended description should also state the package's purpose and scope for users encountering it for the first time.

### Documenting and Formatting Variables and ~~Constants~~

Public class-level and instance-level variables must be documented, either in the class `Attributes` section, as an inline docstring immediately after the assignment, or both. Python does not have constants: never describe something as a constant.

```python
class Configuration:
    """Store and manage configuration settings.

    (AI generated docstring)

    You can use this class to maintain configuration values across the application.

    Attributes
    ----------
    settingDefault : int
        The default setting value applied when no override is provided.
    """

    settingDefault: int = 42
    """The default setting value applied when no override is provided."""
```

Module-level variables follow the same sections as functions where applicable: summary, extended description, `See Also`, `References`, `Examples`.

## Docstring Sections

### Summary Line

**For public identifiers** (functions, classes, methods, variables without leading underscore):

Write the summary line as an implied `You can ...` sentence without the words `You can`.

- Start with a verb on the opening `"""` line.
- State what the identifier lets the reader do, inspect, compute, or obtain.
- Keep the summary short.
- End with a full stop.

- ✅ Correct: "Express descending iteration or a reverse direction."
- ✅ Correct: "Compute the total number of distinct map foldings for a given shape."
- ✅ Correct: "Convert a pile range to an iterator of individual leaves."
- ✅ Correct: "Validate folding constraints before computation."

- **Tie the summary line to the signature.** If the signature contains opaque names such as `t`, `q`,
  `k`, `x`, or `freqs`, include the role-bearing value in the summary line. The reader should learn
  what the identifier acts on, produces, or exposes before reading the next sentence.

- ❌ Incorrect: "You can express descending iteration." (explicit subject - too verbose for summary)
- ❌ Incorrect: "Do the map-folding computation." (command-like and too vague)
- ❌ Incorrect: "Computes foldings." (third person, not second person)
- ❌ Incorrect: "Returns the iterator." (too passive, not focused on reader capability)

**For private identifiers** (functions, classes, methods, variables with leading underscore):

Write the summary line as an `I use this ...` sentence that explains the private identifier's role
in the codebase.

- Use first person from the maintainer's perspective.
- Explain how the identifier supports other code, such as control flow, caching, validation, or
    adaptation.
- Focus on architectural role, not just local behavior.

- ✅ Correct: "I use this shared subroutine for validating input across multiple public methods."
- ✅ Correct: "I use this to manage control flow between the preprocessing and computation phases."
- ✅ Correct: "I use this to cache intermediate results during recursive folding operations."

- ❌ Incorrect: "You can validate input." (second person - implies public API)
- ❌ Incorrect: "Validates input." (third person - too passive, doesn't explain architectural role)
- ❌ Incorrect: "Validate input before processing." (imperative - doesn't explain usage context)

### AI-Generated Marker

When creating a new docstring, place "(AI generated docstring)" on its own line after the summary line and a blank line. When reformatting an existing docstring, do NOT add or remove "(AI generated docstring)".

### Non-technical Description for Non-specialists

After the summary line, start the body text with an **explicit subject** such as "You can...",
"This function...", or "The identifier...". Use the first paragraph to explain purpose, not
implementation detail or background theory.

Write this description for readers who may not know Python, PyTorch, the package, or the domain.
The first paragraph should answer three questions:

- What is the identifier for?
- Which value does the identifier act on?
- What does the identifier return or expose?

Name opaque identifiers in plain language, for example query `Tensor` `q`, key `Tensor` `k`, input
`Tensor` `t`, or angle `Tensor` `freqs`.

Leave notation, broadcasting, cache windows, dtype rules, and other expert mechanics to technical
sections unless those mechanics are the main user-facing point.

### Parameters

- Use the parameter name exactly as it appears in the signature.
- Include the type annotation from the signature.
- If a default value exists (in signature or logic), append `= defaultValue` after the type.
- Use one level of indentation for the description.
- When a parameter accepts a fixed set of values, list them in braces with the default first: `order : {'C', 'F', 'A'}`.
- Always use PEP 585 style (`list[int]`, not `List[int]`).
- Use PEP 604 style (`int | None`, not `Optional[int]`; `int | str`, not `Union[int, str]`).

### Returns and Yields

- Use a meaningful identifier, not just the type.
- Format: `meaningfulName : returnType`
- For generators, use `Yields` instead of `Returns`.

### See Also

- Use `See Also` only when a reader could reasonably choose the referenced symbol instead of the
    current symbol.
- Do not use `See Also` for caller-callee relationships, implementation-detail relationships,
    containment relationships, or dependency relationships. Use the non-technical description or
    `References` instead.
- Always format each `See Also` entry on two lines because formatters and IDE renderers are more
    reliable with this layout.

```text
See Also
--------
`alternativeSymbol`
        One-line description.
`package.other_module.AlternativeClass`
        One-line description.
```

- When the referenced symbol is in the same module, use the local symbol name in backticks.
- When the referenced symbol is in another module of the same package, use the full package path in
    backticks.

### Make Section Names Predict Their Contents

When additional information is needed beyond the standard sections, choose a section name that lets
the reader predict the content before reading the body. Never use `Notes`.

- Good section names name one concrete topic, for example `Mathematics`, `PyTorch`,
    `Shape Transformation`, `Caching`, `Position Alignment`, `Sequence Trimming`,
    `Head-Axis Broadcasting`, or `Autocast Behavior`.
- Avoid catch-all labels such as `Algorithm Details`, `Implementation Notes`, or `Technical Notes`.
- Avoid broad systems labels such as `Concurrency` or `Memory Management` unless the section is
    literally about concurrency or memory management.

#### Use `Mathematics` for formal notation

- Write `Mathematics` sections for academic experts without simplification.
- A `Mathematics` entry should usually do three things in order: bridge from Python identifiers to
    symbols, state the mathematics in pure notation, then bridge from symbols back to Python
    identifiers.
- Within a `Mathematics` entry, avoid prose sentences. Use establishing lines and equations.
- Keep mathematical notation out of summary, non-technical description, parameters, and returns.
- Because IDE renderers are finicky, use fenced blocks with the fences aligned to the entry label and
    the fenced contents indented one additional level.

##### Example 1

quarter turn : equation
```
    Let  d ≜ `x.shape[-1]`,  y ≜ `rotated`

    R(π/2) ≜ [[0, −1], [1, 0]]
    (y₂ⱼ, y₂ⱼ₊₁) = R(π/2) · (x₂ⱼ, x₂ⱼ₊₁)   ∀ j ∈ {0, …, d/2 − 1}
```

last-axis reshaping : transformation
```
    Let  m ≜ d / 2

    x ∈ ℝ^{…, 2m}
    x ↦ x̃ ∈ ℝ^{…, m, 2}
    (a, b) ↦ (−b, a)
    x̃ ↦ y ∈ ℝ^{…, 2m}
```

##### Example 2

rotated block : equation
```
    Let  Ω ≜ `freqs`,  s ≜ `scale`,  J ≜ `rotate_half()`
         n ≜ `start_index`,  m ≜ n + `freqs.shape[-1]`
         t = [tˡ ‖ tᵐ ‖ tʳ]

    y = [tˡ ‖ tᵐ ⊙ cos Ω ⊙ s + J(tᵐ) ⊙ sin Ω ⊙ s ‖ tʳ]

    where  y ≜ `out`
```

sequence trimming : equation
```
    Let  Ω₀ ≜ `freqs`,  L ≜ `t.shape[seq_dim]`
         σ ≜ `freqs_seq_dim`,  N ≜ |Ω₀|_σ

    N > L  ⟹  Ω = Ω₀_[N − L, N)
    N ≤ L  ⟹  Ω = Ω₀
```

#### Use `PyTorch` for library-specific behavior

- Use a `PyTorch` section when the detail is specific to torch semantics, broadcasting, buffers,
    autocast, device placement, or API behavior.
- If a PyTorch behavior can also be expressed mathematically, put the notation in `Mathematics` as
    well. Use `PyTorch` to explain the torch-specific part.

### Draw Examples from Real Usage, Never from Invention or Tests

Private identifiers (starting with `_`) do not require an `Examples` section.

Examples must be drawn from actual usage in the codebase. To find examples, search for real invocations of the documented identifier, then select and simplify representative usage.

1. Use code search to find real invocations of the documented function/class.
2. Select representative usage that demonstrates typical or important patterns.
3. Simplify if needed, but preserve the identifier style and conventions of the codebase.
4. If no real usage exists in the codebase, note this limitation.

**Never create contrived examples.** Real code demonstrates actual patterns and validates that the function works as documented.

- Examples must follow the identifier and style conventions of the codebase.
- Include context if needed for clarity (imports, setup, etc.).
- Use triple-backtick code fences for all code examples, not REPL-style `>>>` prompts. Indent the code fence block one level deeper than the surrounding explanatory text.

### References

Docstrings must provide navigation to related code and external resources. All references should be collected in a `References` section at the end of the docstring, numbered sequentially, and cited in the text using `[1]`, `[2]`, etc.

**Reference any concept or identifier a reader might need to look up.** The following categories always need references.

1. **External packages and APIs**: Any mention of third-party libraries or their components.
   - `pandas.DataFrame`, `numpy.ndarray`, `requests.Session`
   - Use Context7 links when available for well-documented packages.
   - Use official documentation links as fallback.

2. **Standard library items** (selective):
   - Rarely used modules or functions.
   - Edge cases or subtle behaviors.
   - Complex APIs (e.g., `asyncio`, `collections.abc`, `operator`).
   - Skip universally known items (e.g., `list`, `dict`, `str`, `int`).

3. **Same-package references**:
   - Functions, classes, or methods defined elsewhere in the package.
   - Related utilities.
   - Algorithms or data structures used internally.

4. **Theoretical foundations**:
   - Mathematical concepts (group theory, graph theory, combinatorics).
   - Algorithms (sorting, searching, optimization).
   - Academic papers or textbooks.
   - Wikipedia articles for established concepts.

5. **Standards and specifications**:
   - IETF RFCs, W3C specifications, PEPs.
   - File formats (JSON, CSV, HDF5).
   - Protocols (HTTP, TCP, MQTT).

**Backticks indicate but do not determine the need for a reference.** Skip references for identifiers already in the function signature. Conversely, some concepts need references even without backticks (e.g., "Chinese numerals" refers to a cultural/linguistic system).

```python
def exampleFunction(data: list[int]) -> int:
    """Compute the sum using this positional notation system [1].

    This function implements the algorithm described in [2] using `gmpy2` [3]
    for arbitrary-precision arithmetic. The approach is related to
    `mapFolding.basecamp.countFolds` [4].

    Parameters
    ----------
    data : list[int]
        Input values in positional notation.

    Returns
    -------
    total : int
        Sum of input values.

    References
    ----------
    [1] Positional notation - Wikipedia
        https://en.wikipedia.org/wiki/Positional_notation
    [2] Knuth, D. E. (1997). The Art of Computer Programming, Volume 2:
        Seminumerical Algorithms (3rd ed.). Addison-Wesley.
    [3] gmpy2 - Context7
        https://gmpy2.readthedocs.io/en/latest/
    [4] `mapFolding.basecamp.countFolds`
    """
```

**Verify every link and cite references in order of first appearance.**

- When modifying an existing docstring, verify all existing links as a maintenance task.
- Cite references in the text using `[1]`, `[2]`, etc., immediately after the relevant term or concept.
- Multiple references for one concept: `[1, 2]` or `[1][2]` (be consistent within a docstring).
- List references in order of first citation.
- For same-package references, enclose the referenced module path or symbol name in backticks.
- When the referenced symbol is in the same module, use only the local symbol name in backticks.
- When the referenced symbol is in another module of the same package, use the full package path in
    backticks.
- Leave one blank line after each same-package reference entry because some IDE renderers collapse
    consecutive one-line entries.
- Include both title/description and URL for web resources.
- For packages: prefer Context7 links when available.
- For academic papers: include full citation (author, year, title, publication).

**Prefer these documentation URLs when referencing these packages.** Add other packages as needed using the same pattern (Context7 when available, official documentation otherwise).

- `hunterMakesPy`: <https://context7.com/hunterhogan/huntermakespy>
- `astToolkit`: <https://context7.com/hunterhogan/asttoolkit>
- `numpy`: <https://numpy.org/doc/stable/reference/index.html>
- `pandas`: <https://pandas.pydata.org/docs/reference/index.html>
- `gmpy2`: <https://gmpy2.readthedocs.io/en/latest/>
- `numba`: <https://numba.readthedocs.io/en/stable/>

## Write Consistent, Precise Technical Documentation

Technical documentation requires consistency and precision. Literary prose avoids repetition through synonyms and pronouns.

### Write for Non-Native Speakers, Machine Translation, and AI Assistants

The audience for these docstrings includes developers, researchers using Python as a tool, hobbyists, machine translators, and AI assistants. Two-thirds of the human audience are non-native English speakers, and half will use some machine translation.

- **Use active voice**: "This function returns X" rather than "X is returned by this function".
- **Use technical terms, not idioms or colloquialisms**: "fails quickly" not "bails out", "prevents errors" not "catches issues".
- **Use consistent terms**: Machine translation and AI retrieval work better with repeated exact phrases.
- **Be explicit and precise**: Avoid pronouns, cultural context, and implied knowledge.
- **Short, complete sentences**: Better for parsing and translation than long, flowing prose.

### Repeat Identifiers Instead of Using Pronouns

- **Repeat nouns instead of using pronouns**: Write "`parameterFirst`" every time, not "it" or "the parameter".
- **Repeat exact identifiers**: Don't vary between "`handler`", "the handler", or "this callback".
- **Use _the_ technical term, not synonyms**: Don't alternate, for example, between "function" and "routine". Synonyms suggest false distinctions: some readers will wonder if "handler" and "callback" mean different things.

❌ **Bad** (prose-style with pronouns and synonyms):

> Process the data using the handler. It will transform the input
and pass the result to the callback, which processes it further.

✅ **Good** (technical style with repetition):

> Process `data` using `handler`. The `handler` transforms `data`
and passes `data` to `handler`, which processes `data` further.

### Always Use Backticks for Code

- Always use backticks when referring to:
  - Identifiers and other labels: `parameterName`, `className`
  - Python keywords: `try`, `except`, `class`
  - Types: `Exception`, `None`, `bool`
  - Code elements: `self`, `cls`
- Natural language discussing concepts uses standard English without backticks.
- Never write lowercase technical terms: write `Exception`, never "exception" when referring to the Python type.

### Do Not Force English Plurality on Identifiers

- **Do not force English plurality on identifiers**: `keyword` not `keywords` or `keyword`s.
- **Preserve parameter names exactly**: `handlers` (the field) not "the handlers parameter".
- **Use generalized nouns to avoid plurality**: Do not pluralize identifiers or add possessives to them. Instead, precede the strict identifier with a generalized noun or quantifier.
  - ❌ Incorrect: "Returns the `iterator`'s `leaves`." (Modified identifiers)
  - ✅ Correct: "Returns the `iterator` of `type` `int` `leaf`." (Noun "type int" precedes `leaf`)
  - ❌ Incorrect: "Enumerate `dimensionIndices`." (Pluralized identifier)
  - ✅ Correct: "Enumerate each `dimensionIndex`." (Quantifier "each" precedes `dimensionIndex`)
- **Reinforce meaning through context** rather than breaking identifiers for prose.

### Say What an Ambiguous Term Refers To

- Say what an ambiguous term refers to: "Python keyword `try`" not just "`try`".
- Maintain precision: "`class` `Exception`" rather than "the `Exception` `class`".
- Avoid compound hyphenation with technical terms: not "`Exception`-free" "completion without an `Exception`".

### Never Use "Pipeline"

- Never use "pipeline". Use "assembly line" if describing a sequence of transformations.

### Put Purpose in Non-technical Sections and Mechanics in Technical Sections

Use non-technical sections to answer **when and why** a reader would use the identifier. Use
technical sections to answer **exactly how** the identifier works.

- **Non-technical sections** (`Summary`, non-technical description, `Parameters`, `Returns`,
    `Raises`) explain purpose, inputs, outputs, and user-facing behavior.
- **Technical sections** (`Mathematics`, `PyTorch`, `Caching`, `Shape Transformation`, and similar
    concrete section names) explain notation, tensor algebra, broadcasting, cache alignment,
    precision rules, and other expert mechanics.
- If a reader can decide whether to call the identifier without reading the technical sections, the
    split is correct.
