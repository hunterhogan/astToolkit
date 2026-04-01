# Python Identifier and Label Standards

Standards for naming identifiers and other labels in Python code, including variables, functions, classes, types, mapping keys, and filesystem names.

## What "Identifiers and other labels" means

In Python, an `identifier` has a technical meaning. In this system, **Identifiers and other labels** includes *any* name that identifies something, such as:

- Python identifiers (variables, parameters, functions, methods, classes, attributes, modules, packages)
- Type identifiers (type aliases, `TypeVar` names)
- Mapping key names (including string-literal keys when they are part of the program's naming system)
- Filenames and directory names (especially those participating in Python imports)
- Exported names (`__all__`), entry points, CLI flag names, environment-variable names

The rules for valid Python identifiers are the most restrictive. By default, apply those same restrictions to **all** Identifiers and other labels unless the user explicitly opts into an exception.

## Core Principles

### Reading order and directionality (mandatory)

Identifiers and other labels are read left-to-right. Therefore, name structure must follow:

- past → future (left → right)
- cause → effect (left → right)
- general → specific (left → right)

Practical rules:

- Put inputs/causes first; put outputs/effects later.
- Prefer direction-explicit verbs (e.g., "converts", "encodes", "decodes", "formats", "interprets").
- Prefer `…To…` direction over effect-first constructions.

### CamelCase, not snake_case

- Default: **camelCase** for variables, parameters, functions, methods, and most other labels.
- Exceptions:
  - tests may use `test_*`
  - dunder names required by Python (`__init__`, `__iter__`, …)
  - underscore-separated tokens are allowed **only** when they carry meaning (see below)

For filenames and directory names, default to the same character restrictions as Python identifiers for the "stem" (the part without an extension), unless the user explicitly opts into a looser filesystem convention.

## Naming Patterns by Category

### Functions and methods: explicit Subject–Verb–Object

Use the pattern: `[S][V]O[adj][adv]`

- Callables must include a **verb**.
- For functions and methods, the **subject must be explicit** (an actor/role/system/component), not implied.
- Prefer **general → specific** ordering (shared prefix first) for skimming.

Good patterns:

- `archivistEncodes…`
- `librarianDecodes…`
- `valetOutfits…`

Examples:

- `librarianDecodesPathToAlgorithm`
- `convertPowerSpectralDensityToEqualPowerBands`
- `dictionaryAspectsAnalyzed`

### Structure-prefix objects (skimmability)

To avoid `pathFilenames`, which you should not use because it is too similar to pathFilename, prepend the type. Or if the type is semantically important, prepend it.

- `listPathFilenames…`
- `arraySpectrograms…`
- `dictionaryConcurrency…`

Keep same-prefix groups **alphabetized** unless dependency ordering is required by Python.

### Domain compound terms are atomic

Treat well-known compound terms as a single token:

- `powerSpectralDensity`
- `amplitudeThreshold`
- `lengthWindowingFunction`

### Proper nouns preserve case (underscores may be semantic)

Preserve case fidelity for proper nouns and special spellings; use underscores where necessary:

- `add_pyprojectDOTtoml`
- use `DOT` / `Dot` if it increases semantic clarity

If you are naming something *about* a specific module/symbol, reuse that module/symbol name as an atomic token rather than inventing a near-miss spelling.

### Underscores are allowed only as semantic tokens

Underscores are allowed when they preserve **meaningful token boundaries**, for example:

- `path_tmpTesting` (`tmp` is an atomic filesystem namespace token)
- `uuid_hex` (`hex` is an atomic encoding token)
- `_sampleRateIgnored` is acceptable for "captured-but-ignored", but never use bare `_`.

Underscores are not a substitute for clarity. If a token boundary is meaningful, it must still be semantically meaningful.

### Boolean-returning callables must read as assertions

In English, questions require question words and/or punctuation/tone. Many "is/has" style identifiers read like questions but have none of those markers.

For boolean-returning functions/methods, prefer a declarative assertion with an explicit subject:

- Prefer `thisIs…` / `valueIs…` / `candidateIs…` / `pathIs…` patterns.
- Avoid bare "question-shaped" prefixes that omit an explicit subject.

If a name truly is a question, include an unambiguous question marker.

### Type aliases and TypeVar names (special rules)

Python gives type aliases and `TypeVar` special treatment, and this naming system does too.

- Use an initial capital (TitleCase).
- Prefer **Adjective–Noun** (rarely just a noun).
- Keep type identifiers distinct from value identifiers to preserve discrimination.
- Do not append suffixes like "type" to make the distinction.

Example distinction that is strong enough:

- `leavesPinned: PinnedLeaves = {}`

## Special Cases

### Preserve case for domain type names and column identifiers

#### AST type names (e.g., `ast.keyword`, `ast.expr`, `ast.stmt`)

- ✅ `make_keywordFromAttributeDefaultValue` — lowercase `keyword` matches `ast.keyword`
- ❌ `makeKeywordWithDefault` — capital-K `Keyword` is ambiguous; "Default" is a diminutive

#### DataFrame column names (e.g., `defaultValue`, `Call_keyword`) must preserve their exact case when referenced in identifiers

- ✅ `updateCall_keywordColumn` — preserves `Call_keyword` column name case
- ❌ `updateCallKWColumn` — "KW" is an abbreviation

#### Anti-pattern: Truncating or capitalizing domain terms

- ❌ `makeKeywordWithDefault` — two violations:
  - "Keyword" does not preserve the `ast.keyword` type name case
  - "Default" is a diminutive for `defaultValue` (column/variable name)
- ✅ `makeKeywordFromAttributeDefaultValue` — explicit, preserves case, no abbreviations

When a domain type or column name appears in an identifier:

- Match the case exactly (`keyword`, not `Keyword`)
- Never truncate (`defaultValue`, not `Default` or `Def`)
- If ambiguity exists (multiple "keyword" concepts), add clarifying context

### "One identifier, one meaning"

Never reuse a name for different meanings, even in different scopes.
Avoid Python keyword collisions: don't use `type`, `class`, etc.

### Filesystem semiotics (mandatory)

In filesystem contexts:

- **`path`**: directories only
- **`filename`**: filename only (no path)
- **`pathFilename`**: full path including filename
- **`relativePath`**: relative path only

Never use the word "file" in identifiers (it has no meaning in this system).

### Mapping keys and serialized names

Mapping keys, JSON keys, column names, and other serialized names are **Identifiers and other labels**.

- Default: do not rename them unless the user opts in.
- If the keys are part of a public/serialized interface, treat renaming as a breaking change and ask for confirmation.

### Generic identifier guidance

Avoid empty semantics (`result`, `output`, `temp`, `data`, `thing`, `value`).
If you TRULY need a generic placeholder, `Target` is acceptable, but do not append "Target" to identifiers unless it is necessary for distinction:

- `arrayTarget`
- `mappingTarget`

### Emphatic / temporary signals

- All caps is allowed for critical temporary emphasis: `ERRORmessage`, `OFFSETaxis`.
- `Z0Z_` is a special prefix (do not modify unless asked).

## Prohibited Patterns

- **Do not use single-character identifiers**, especially the lone underscore `_`.
- **Do not introduce abbreviations** (e.g., `np`, `cfg`, `params`, `specs`).
- **Do not introduce diminutives.** Do not shorten or "generalize" a name by dropping meaning-bearing tokens.

When a label references a specific existing symbol (module/function/class/constant), treat it as a **proper noun**:

- preserve the referenced symbol's canonical spelling and casing
- do not invent mixed-case spellings
- do not truncate the referenced name to a vague "nickname"
