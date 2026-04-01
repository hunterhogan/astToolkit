# Python Diagnostic Message Standards

Standards for creating diagnostic messages (errors, warnings, logs) with consistent syntax, self-describing content, and appropriate delivery mechanisms.

## Message Syntax Standard

### Variable Assignment Pattern

Always assign the message to a typed variable. Never embed f-strings directly in `raise`, `warn()`, or logging calls.

```python
# Correct: Assign to variable, then use
message: str = f"I received `{parameterValue = }`, but I need a positive integer."
raise ValueError(message)

# Incorrect: Inline f-string (violates Ruff EM102)
raise ValueError(f"I received `{parameterValue = }`, but I need a positive integer.")
```

The variable identifier is always `message: str`. This pattern applies uniformly:

```python
# Exception
message: str = f"I received `{value = }`, but I need a value greater than 0."
raise ValueError(message)

# Warning
message: str = f"I received `{value = }`, but I need a value greater than 0."
warnings.warn(message, category=UserWarning)

# Logging
message: str = f"I received `{value = }`, but I need a value greater than 0."
logger.error(message)

# Standard output
message: str = f"I received `{value = }`, but I need a value greater than 0."
print(message)
```

### Debug Representation Syntax

Use Python's self-documenting expression syntax to include both the identifier name and its value:

```python
# Self-documenting: Shows "dimensionLength = 0" in output
message: str = f"I received `{dimensionLength = }`, but I need a value greater than 1."

# In this case, the parameter is `computationDivisions`, so {computationDivisionsAsString = } would be slightly confusing.
message: str = f"I received '{computationDivisionsAsString}' for `computationDivisions`, but this value is not supported."
```

Wrap identifiers in backticks within the message string for visual distinction.

## Message Content Principles

### First-Party State Observation

Report what the function observed, not what the caller did. The function knows its received state; it cannot know the caller's intent or actions.

```python
# Correct: Reports observed state
message: str = f"I did not receive a value for `parameterName`, but it is required."
message: str = f"I received `{allegedInt = }`, but `parameterName` must be an integer."
message: str = f"I could not find `{identifier = }` in `{container = }`."

# Incorrect: Attributes causation to caller
message: str = f"You must supply all values."
message: str = f"You cannot pass a float as a parameter."
message: str = f"`parameterName` is required."
```

Use first-person perspective: "I received", "I did not receive", "I could not find", "I expected".

### Thesis-Condition Alignment

The message thesis must correspond to the triggering condition. If the condition tests membership, the message must address membership.

```python
# Condition tests membership
if testCase.oeisID not in dictionaryOEISMapFolding:
    # Correct: Message reflects the membership test
    message: str = f"I could not find `{testCase.oeisID = }` in `dictionaryOEISMapFolding`."

    # Incorrect: Message makes unrelated claim
    message: str = f"`{testCase.oeisID}` does not define a map shape."
```

### Self-Describing Content

Include the actual runtime values that triggered the condition. A diagnostic message should provide sufficient context for debugging without requiring a debugger.

```python
# Self-describing: Contains actual values and expected constraints
message: str = f"I received `{dimensionAsNonnegativeInteger = }`, but I need a value that is an integer power of `{dimensionLength = }`."

# Insufficient: Missing actual values
message: str = f"The dimension must be a power of the dimension length."
```

### Contrastive Structure

When appropriate, structure messages as "received X, but expected Y" to clarify the discrepancy:

```python
message: str = f"I received `{integerNonnegative = }`, but I need a value greater than or equal to 0."
message: str = f"I received `{dimensionLength = }`, but I need an integer value greater than 1."
```

## Delivery Mechanism Selection

Choose the appropriate mechanism based on execution context:

| Context                | Mechanism                    | Rationale                          |
| ---------------------- | ---------------------------- | ---------------------------------- |
| Precondition violation | `raise` exception            | Halt execution, caller must handle |
| Recoverable anomaly    | `warnings.warn()`            | Alert without halting              |
| Operational logging    | `logging` module             | Structured, configurable output    |
| Interactive feedback   | `print()` / rich output      | User-facing status                 |
| Test assertions        | `pytest.fail()` / assertions | Test framework integration         |

### Context Awareness

Do not create diagnostic messages that the execution context will suppress or ignore:

```python
# Inside a pytest test function, custom exception messages are often invisible
# because pytest captures and reformats assertion failures.
# Use pytest's native assertion mechanisms instead.

def test_module_creation():
    # Avoid: pytest won't display this message usefully
    if not spec:
        message: str = f"Failed to create module specification from {pathFilenameModule}"
        raise ImportError(message)

    # Prefer: Use pytest assertions
    assert spec is not None, f"Module specification creation failed for {pathFilenameModule}"
```

## ANSI Formatting for Terminal Output

For terminal status output, ANSI color codes may be used:

```python
message: str = f"{ansiColors.YellowOnBlack}I received {state.dimensionsTotal = }, but I could not find the data at:\n\t{pathFilename!r}.{ansiColorReset}"
```

Never use ANSI codes in exception messages or log entries—only for direct terminal output.

## Terminology Standards

### Backtick Usage

- Wrap all identifiers in backticks: `` `parameterName` ``, `` `ValueError` ``
- Wrap Python keywords in backticks: `` `None` ``, `` `True` ``
- Use backticks for code elements referenced in prose
