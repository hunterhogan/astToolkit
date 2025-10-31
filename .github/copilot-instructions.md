# GitHub Copilot Instructions for astToolkit

## Project Overview

astToolkit is a powerfully composable, type-safe Python toolkit for Abstract Syntax Tree (AST) manipulation, analysis, transformation, and code generation. It provides a layered architecture designed for building sophisticated code processing assembly-lines.

**Key Design Principles:**
- Type safety: Extensive use of TypeIs, TypeGuard, and type annotations
- Composability: Small, reusable components that combine into powerful transformations
- Layered architecture: Core "atomic" classes build up to higher-level tools
- Fluent API: Consistent, readable interfaces across all components

## Repository Structure

```
astToolkit/
├── astToolkit/           # Main package
│   ├── _astTypes.py      # 120+ specialized types for AST components
│   ├── _toolBe.py        # Type guards (Be.*)
│   ├── _toolDOT.py       # Read-only accessors (DOT.*)
│   ├── _toolGrab.py      # Transformation functions (Grab.*)
│   ├── _toolMake.py      # Factory methods (Make.*)
│   ├── _toolIfThis.py    # Predicate functions (IfThis.*)
│   ├── _toolThen.py      # Action functions (Then.*)
│   ├── _toolkitNodeVisitor.py  # NodeTourist and NodeChanger
│   ├── _toolkitAST.py    # Higher-level AST operations
│   ├── containers.py     # IngredientsFunction, IngredientsModule
│   └── transformationTools.py  # Advanced utilities
├── tests/                # Test suite
│   ├── test_Be.py        # Tests for Be type guards
│   ├── test_IfThis.py    # Tests for IfThis predicates
│   └── dataSamples/      # Test data generation
└── .github/
    ├── workflows/        # CI/CD workflows
    └── agents/           # Custom agent definitions
```

## Architecture & Patterns

### Layered Architecture

1. **Core "Atomic" Classes** (Foundation):
   - `Be`: Type guards returning `TypeIs[ast.NodeType]`
   - `DOT`: Read-only accessors with proper typing
   - `Grab`: Transformation functions preserving node structure
   - `Make`: Factory methods for creating AST nodes

2. **Traversal and Transformation**:
   - `NodeTourist`: Extends `ast.NodeVisitor` to extract information
   - `NodeChanger`: Extends `ast.NodeTransformer` to modify nodes

3. **Composable APIs** (Antecedent-Action Pattern):
   - `IfThis`: Predicate functions to identify nodes
   - `Then`: Action functions to specify operations on matched nodes
   - `ClassIsAndAttribute`: Powerful antecedent constructor

4. **Higher-level Tools**:
   - `_toolkitAST.py`: Common operations (extract functions, imports)
   - `transformationTools.py`: Advanced utilities (inlining, generation)
   - `IngredientsFunction` and `IngredientsModule`: Component containers

5. **Type System**:
   - 120+ specialized types for AST components
   - Custom type annotations for node attributes
   - Union types modeling Python's AST structure
   - Type guards for static type checking

### The Antecedent-Action Pattern

Code follows the pattern:
```python
NodeChanger(
    antecedent=IfThis.someCondition(...),  # Identifies nodes
    action=Then.someAction(...)            # Transforms them
).visit(tree)
```

## Coding Standards

### Python Version and Type Safety

- **Requires Python 3.12+**
- **Type hints are mandatory** - all functions must have complete type annotations
- Use `TypeIs`, `TypeGuard` from `typing` for type narrowing
- Listen to your type checker - it prevents pairing wrong attributes with classes
- IDE hover hints should guide you to valid class-attribute combinations

### Naming Conventions

- **Classes**: PascalCase (e.g., `NodeTourist`, `ClassIsAndAttribute`)
- **Functions/Methods**: camelCase (e.g., `extractFunctionDef`, `parseLogicalPath2astModule`)
- **Constants**: UPPER_SNAKE_CASE
- **Private members**: Leading underscore (e.g., `_theSSOT.py`)

### Code Style

- Follow existing patterns in the codebase
- Prefer composition over inheritance
- Keep functions focused and single-purpose
- Use descriptive names that explain intent
- Avoid comments unless explaining complex AST transformations
- Chain operations fluently when it improves readability

### File Organization

- Files prefixed with `_` are internal implementation
- `_theSSOT.py` is the Single Source of Truth for core definitions
- Tool classes (`_tool*.py`) each handle one aspect of AST manipulation
- Each tool file exports a single main class or set of related functions

## Testing Requirements

### Test Structure

- Tests are in `tests/` directory
- Test files named `test_*.py`
- Use pytest as the test framework
- Test data generation in `tests/dataSamples/`

### Running Tests

```bash
# Install with testing dependencies
pip install -e ".[testing]"

# Run all tests
pytest

# Run tests with coverage
pytest --cov=astToolkit --cov-report=term-missing

# Run specific test file
pytest tests/test_Be.py -v
```

### Writing Tests

- **Test naming**: `test_<component>_<scenario>` (e.g., `test_BeIdentifierClassPositive`)
- **Use parametrize**: Tests are often parameterized to cover many AST node types
- **Test both positive and negative cases**: Ensure type guards work correctly
- **Generate test data systematically**: See `tests/dataSamples/createTestData.py`
- **Verify type narrowing**: Tests should confirm that type guards enable proper type checking

### Test Coverage

- Aim for high coverage, especially for core "atomic" classes
- All public APIs must have tests
- Edge cases and error conditions must be tested
- Type-related behavior is critical to test

## Building and Development

### Installation

```bash
# Development installation
pip install -e ".[testing,development]"

# Production installation
pip install astToolkit
```

### Dependencies

- **Runtime**: `hunterMakesPy>=0.3.0`, `typing_extensions>=4.10.0`
- **Testing**: `pytest`, `pytest-cov`, `pytest-xdist`
- **Build**: `setuptools`, `setuptools-scm`

### Code Quality

- Use type checkers (mypy, pyright) - type safety is critical
- Follow PEP 8 for general Python style
- Use isort for import organization (config in `.isort.cfg`)
- Keep the `py.typed` marker file for PEP 561 compliance

## Common Tasks and Patterns

### Adding a New AST Node Type

1. Add type definition to `_astTypes.py`
2. Add type guard to `_toolBe.py`
3. Add accessor to `_toolDOT.py` if needed
4. Add factory method to `_toolMake.py`
5. Add tests to `tests/test_Be.py`

### Creating a New Predicate

1. Add to `IfThis` class in `_toolIfThis.py`
2. Use composition of existing predicates when possible
3. Return `Callable[[ast.AST], TypeIs[SpecificType] | bool]`
4. Add tests to `tests/test_IfThis.py`

### Adding a Transformation

1. Decide if it belongs in `Grab`, `Then`, or higher-level tools
2. Preserve node structure when using `Grab`
3. Use `Then.replaceWith` for node replacement
4. Use `Then.extractIt` for information extraction
5. Compose transformations from atomic operations

### Working with Type Guards

- Type guards use `TypeIs` from `typing` (Python 3.13+) or `typing_extensions`
- Pattern: `def Be.SomeNode(node: ast.AST) -> TypeIs[ast.SomeNode]:`
- Always check isinstance() inside type guards
- Type guards enable static type checkers to narrow types

## AST Manipulation Best Practices

### Node Creation

- Use `Make.*` factory methods, not direct AST constructors
- Factory methods provide consistent interfaces and defaults
- Always fill required fields for AST nodes

### Node Transformation

- Use `NodeChanger` with predicates and actions
- Test transformations on small code samples first
- Use `ast.unparse()` to verify output is valid Python
- Remember: AST transformations must preserve Python semantics

### Node Traversal

- Use `NodeTourist` to extract information without modification
- Capture matches with `.captureLastMatch()` or similar
- Predicates should be pure functions without side effects

### Type Safety in AST Operations

- Let type guards narrow types before accessing specific attributes
- IDE hover hints show which classes have which attributes
- Type checker prevents invalid attribute access
- Use `DOT.*` accessors for type-safe attribute reading

## CI/CD and Workflows

### GitHub Actions Workflows

- **pythonTests.yml**: Runs tests on multiple Python versions (3.12+)
- **pypiRelease.yml**: Publishes to PyPI
- **githubRelease.yml**: Creates GitHub releases
- **updateCitation.yml**: Maintains CITATION.cff

### Pull Request Requirements

- All tests must pass
- Type checking must pass
- Code should follow existing patterns
- No decrease in type safety
- Preserve backwards compatibility unless major version change

## Extending astToolkit

### Creating Custom Predicates

Users often extend `IfThis` for domain-specific predicates:

```python
from astToolkit import IfThis as astToolkit_IfThis

class IfThis(astToolkit_IfThis):
    @staticmethod
    def customPredicate(...) -> Callable[[ast.AST], TypeIs[ast.SomeType] | bool]:
        return lambda node: (
            # Compose existing predicates
            Be.SomeType(node)
            and IfThis.someOtherCheck(...)(node)
        )
```

### The toolFactory Pattern

The `toolFactory` directory/package allows customization of:
- Core classes: `Be`, `DOT`, `GRAB`, `Make`
- Type aliases (100+)
- Custom behaviors for specific use cases

## Important Notes

### DO

- Follow type hints religiously
- Compose from existing tools when possible
- Test with multiple Python versions (CI handles this)
- Use descriptive variable names for AST nodes
- Preserve AST node structure in transformations
- Document complex AST transformation logic

### DON'T

- Don't bypass type system with `# type: ignore` without good reason
- Don't mutate AST nodes in predicates (use `Then` actions)
- Don't create deeply nested transformations (break into steps)
- Don't use string manipulation for code generation (use AST)
- Don't forget to run tests after changes
- Don't modify `_theSSOT.py` without understanding full impact

## Real-World Usage Examples

See the [mapFolding](https://github.com/hunterhogan/mapFolding) project for:
- Complete transformation assembly-lines
- Algorithm extraction and optimization
- Numerical computing decorators integration
- Dataclass management with AST
- Module generation with proper imports

Check `mapFolding/someAssemblyRequired/` for in-depth examples.

## License and Attribution

- License: CC-BY-NC-4.0 (Creative Commons Attribution-NonCommercial 4.0)
- Maintain license notices in all files
- Attribute original author (Hunter Hogan) when extending

## Getting Help

- **Issues**: Use GitHub Issues for bugs and feature requests
- **Patterns**: Check existing code for similar operations
- **Documentation**: README.md contains usage examples
- **Type hints**: Let your IDE guide you with hover information

## Task Assignment Guidelines

### Good Tasks for Copilot Coding Agent

- Adding new AST node type support
- Writing tests for existing functionality
- Fixing type annotation issues
- Adding new predicates to `IfThis`
- Creating new factory methods in `Make`
- Documentation improvements
- Test coverage improvements
- Bug fixes with clear reproduction steps

### Tasks Requiring Human Review

- Changes to core architecture
- Modifications to `_theSSOT.py`
- Breaking API changes
- Performance-critical optimizations
- Complex AST transformation algorithms
- Changes affecting type system design

## Version Information

- Current version: 0.9.0 (Beta)
- Python requirement: >=3.12
- Status: Active development, API may evolve
- Type system maturity: High (120+ types)
- Test coverage: Comprehensive for core features
