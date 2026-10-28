# astToolkit

## Easily and Confidently Transform Python Code Using Unadulterated AST Classes

astToolkit provides composable, typed tools for analyzing, transforming, and generating Python code. Select the nodes you care about, describe an action, and apply it through a visitor.

**Compatibility with the standard library's [`ast`](https://docs.python.org/3/library/ast.html) is an intentional design goal.** astToolkit works directly with the same `ast.AST` objects. You can parse with `ast`, transform with astToolkit, and return to `ast` for inspection, unparsing, or compilation. There is no conversion step or separate tree representation.

```python
import ast
from astToolkit import Grab, IfThis, NodeChanger, Then

astModule: ast.Module = ast.parse('result = value * 2')

NodeChanger(
    IfThis.isNameIdentifier('value'),
    Grab.idAttribute(Then.replaceWith('amount')),
).visit(astModule)

print(ast.unparse(astModule))
# result = amount * 2
```

This changes the identifier on the existing `ast.Name` node. The module and its nodes remain available to your own visitors and other tools that work with stdlib ASTs.

## Installation

Requires **Python 3.14 or later**.

```bash
pip install astToolkit
```

## Compose the operation you need

The core pattern is **predicate + action + visitor**. A predicate identifies a node; an action reads or changes it; a visitor applies that operation throughout a tree.

| Tool | Purpose |
| --- | --- |
| `Be` | Check node types with `TypeIs` guards, such as `Be.FunctionDef`, and compose conditions on their fields. |
| `DOT` | Read node attributes through typed getters, such as `DOT.name` or `DOT.value`. |
| `Grab` | Transform an attribute while retaining its containing node. |
| `Make` | Construct AST nodes with typed parameters and convenient defaults. |
| `IfThis` | Match identifiers, structure, and combinations of conditions. |
| `Then` | Collect, extract, insert, replace, or remove matched nodes. |
| `NodeTourist` | Visit nodes for inspection and collection; `captureLastMatch` returns the last action result. |
| `NodeChanger` | Transform matching nodes, including replacing or removing them. |

`NodeTourist` extends `ast.NodeVisitor`; `NodeChanger` extends `ast.NodeTransformer`. A matching `NodeChanger` node is handed to its action without automatically visiting that node's children. Compose visitors or attribute actions when a transformation needs to continue inside a match.

### Read and collect

Use a `DOT` getter to retrieve an attribute directly, or `Then.appendTo` to collect matching nodes:

```python
import ast
from astToolkit import Be, DOT, NodeTourist, Then

astModule: ast.Module = ast.parse('result = value * 2')

identifier: str | None = NodeTourist(
    Be.Name, DOT.id,
).captureLastMatch(astModule)

print(identifier)
# value

list_astName: list[ast.Name] = []
NodeTourist(Be.Name, Then.appendTo(list_astName)).visit(astModule)
```

The collected nodes are the original objects in `astModule`. Extraction does not copy or wrap them.

### Build nodes

`Make` works with stdlib node types. For example, `Make.Name('amount')` returns an `ast.Name` with a `Load` context:

```python
import ast
from astToolkit import Make

astName: ast.Name = Make.Name('amount')

print(type(astName) is ast.Name)
# True

print(ast.compare(astName, ast.Name(id='amount', ctx=ast.Load())))
# True
```

Operator joins assemble expressions without manually nesting each binary operation:

```python
import ast
from astToolkit import Make

ast_expr: ast.expr = Make.Add.join([
    Make.Name('subtotal'),
    Make.Name('tax'),
    Make.Name('shipping'),
])

print(ast.unparse(ast_expr))
# subtotal + tax + shipping

astModule: ast.Module = Make.Module([Make.Expr(ast_expr)])
compile(ast.fix_missing_locations(astModule), '<generated>', 'exec')
```

Some `Make` operator classes, including `Make.Add`, subclass their stdlib counterparts to provide `join`. They work with stdlib AST tools; `ast.compare` distinguishes those subclasses from the exact stdlib classes. I want to change this.

### Match structure

Use `IfThis.astIs(referenceNode)` for structural matching through `ast.compare`. Field predicates, such as `Be.Assign.valueIs(...)`, select a containing node by a condition on one of its fields. `IfThis.isAllOf(...)` applies every condition to the same node; nested visitors search within a selected subtree.

## Find the function you need

Utility functions have focused module homes:

| Module | Functions |
| --- | --- |
| [`astToolkit.changeDef`](astToolkit/changeDef.py) | `extractClassDef`, `extractFunctionDef`, `makeDictionaryAsyncFunctionDef`, `makeDictionaryClassDef`, `makeDictionaryFunctionDef`, `makeDictionaryMosDef`, `inlineFunctionDef`, `removeUnusedParameters` |
| [`astToolkit.filesystem`](astToolkit/filesystem.py) | `parsePathFilename2astModule`, `parseLogicalPath2astModule`, `write_astModule` |
| [`astToolkit.ohWow`](astToolkit/ohWow.py) | `pythonCode2ast_expr`, `unjoinBinOP`, `unparseFindReplace` |

- **Definitions:** extract a named function or class, index definitions by name, inline supported local function calls, or remove unused parameters.
- **Files:** parse a source file without importing it, parse an importable module's source, or write an `ast.Module` as formatted Python. `parseLogicalPath2astModule` imports the module; `write_astModule` removes unused imports and organizes imports.
- **Expressions:** parse expression text, collect binary-operation operands, or replace nodes by matching their unparsed text.

Import these functions from their modules, for example:

```python
from astToolkit.changeDef import extractFunctionDef, removeUnusedParameters
from astToolkit.filesystem import parsePathFilename2astModule, write_astModule
```

[Type aliases](astToolkit/theTypes.py) describe AST fields and the node types that contain them. The package includes `py.typed` for static type checking.

**Breaking change in 0.13.0:** `IngredientsFunction`, `IngredientsModule`, and `LedgerOfImports` have been removed.

## Larger workflows

[mapFolding](https://github.com/hunterhogan/mapFolding) uses astToolkit to transform readable algorithms into specialized variants and generate Python modules.

Most of the core toolkit code is generated by the separate [astToolFactory](https://github.com/hunterhogan/astToolFactory) project.

## Support my work

If astToolkit saves you time, please [sponsor my work on GitHub](https://github.com/sponsors/hunterhogan). Monthly or one-time support helps me survive. You can also [choose another way to support me](https://hunterthinks.com/support).

[![Homeless since August 2011](https://img.shields.io/badge/2011_August-Homeless_since-blue?style=flat)](https://hunterthinks.com/support)

## Citation and license

Citation metadata is available in [CITATION.cff](citations/CITATION.cff).

[![CC-BY-NC-4.0](https://raw.githubusercontent.com/hunterhogan/astToolkit/refs/heads/main/.github/CC-BY-NC-4.0.png)](https://creativecommons.org/licenses/by-nc/4.0/)
