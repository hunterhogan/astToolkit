# astToolkit

## Do You Want This Package?

astToolkit provides a powerfully composable system for manipulating Python Abstract Syntax Trees. Use it when:

- You need to programmatically analyze, transform, or generate Python code.
- You want type-safe operations that help prevent AST manipulation errors.
- You prefer working with a consistent, fluent API rather than raw AST nodes.
- You desire the ability to compose complex AST transformations from simple, reusable parts.

Don't use it for simple text-based code manipulation—use regex or string operations instead.

## Usage

### Core Atomic Operations

astToolkit provides four core classes that perform "atomic" operations on every AST class and attribute:

```python
from astToolkit import Be, DOT, Grab, Make
import ast

# Create an AST node
node = Make.Name("example")

print(f"{ast.dump(node) = }\n")

# Access node properties safely with type checking
myNameDOTidIs = DOT.id(node)

print(f"{myNameDOTidIs = }\n")

# Check node type with type guard functions
CallNode = Make.Call(node)
print(f"{ast.dump(CallNode) = }\n")

print(f"{Be.Name(CallNode) = }")
print(f"{Be.Name(node) = }")

print(f"{Be.Call(CallNode) = }\n{Be.Name(DOT.func(CallNode)) = }\n")

# Transform node attributes while preserving structure
action = lambda idValue: f"modified_{idValue}"
doThis = Grab.idAttribute(action)
nodeAfterAction = doThis(node)
print(f"{ast.dump(node) = }")
```

### AST Traversal and Transformation

The real power lies in composable traversal and transformation using `NodeTourist` and `NodeChanger`:

```python

"""
The AI assistant's example was stupid and wrong. I'm too sick right
now to make a better one.
"""

```

### Extending `IfThis` and `Then` Classes

Extend these classes to create custom predicate and action functions:

```python
from astToolkit import ast_Identifier, Be, IfThis as astToolkit_IfThis
from collections.abc import Callable
from typing import Any, TypeGuard
import ast

class IfThis(astToolkit_IfThis):
  @staticmethod
  def isAttributeNamespace_IdentifierGreaterThan0(
      namespace: ast_Identifier,
      identifier: ast_Identifier
      ) -> Callable[[ast.AST], TypeGuard[ast.Compare] | bool]:

    return lambda node: (
        Be.Compare(node)
        and IfThis.isAttributeNamespace_Identifier(namespace, identifier)(node.left)
        and Be.Gt(node.ops[0])
        and IfThis.isConstant_value(0)(node.comparators[0]))

  @staticmethod
  def isIfAttributeNamespace_IdentifierGreaterThan0(
      namespace: ast_Identifier,
      identifier: ast_Identifier
      ) -> Callable[[ast.AST], TypeGuard[ast.If] | bool]:

    return lambda node: (
        Be.If(node)
        and IfThis.isAttributeNamespace_IdentifierGreaterThan0(namespace, identifier)(node.test))

  @staticmethod
  def isWhileAttributeNamespace_IdentifierGreaterThan0(
      namespace: ast_Identifier,
      identifier: ast_Identifier
      ) -> Callable[[ast.AST], TypeGuard[ast.While] | bool]:

    return lambda node: (
        Be.While(node)
        and IfThis.isAttributeNamespace_IdentifierGreaterThan0(namespace, identifier)(node.test))

  # Or, make the comparison value a parameter
  @staticmethod
  def isAttributeNamespace_IdentifierGreaterThanThis(
      namespace: ast_Identifier,
      identifier: ast_Identifier,
      value: Any
      ) -> Callable[[ast.AST], TypeGuard[ast.Compare] | bool]:

    return lambda node: (
        Be.Compare(node)
        and IfThis.isAttributeNamespace_Identifier(namespace, identifier)(node.left)
        and Be.Gt(node.ops[0])
        and IfThis.isConstant_value(value)(node.comparators[0]))
```

### Easy-to-use Tools for Annoying Tasks

- extractClassDef
- extractFunctionDef
- parseLogicalPath2astModule
- parsePathFilename2astModule

### Easy-to-use Tools for More Complicated Tasks

- removeUnusedParameters
- write_astModule

### The `toolFactory`

Hypothetically, you could customize every aspect of the classes `Be`, `DOT`, `GRAB`, and `Make` and more than 100 `TypeAlias` in the toolFactory directory/package.

## Installation

```bash
pip install astToolkit
```

## Technical Details

### Architecture

astToolkit implements a layered architecture designed for composability and type safety:

1. **Core "Atomic" Classes** - The foundation of the system:
   - `Be`: Type guards that return `TypeGuard[ast.NodeType]` for safe type narrowing.
   - `DOT`: Read-only accessors that retrieve node attributes with proper typing.
   - `Grab`: Transformation functions that modify specific attributes while preserving node structure.
   - `Make`: Factory methods that create properly configured AST nodes with consistent interfaces.

2. **Traversal and Transformation** - Built on the visitor pattern:
   - `NodeTourist`: Extends `ast.NodeVisitor` to extract information from nodes that match predicates.
   - `NodeChanger`: Extends `ast.NodeTransformer` to selectively transform nodes that match predicates.

3. **Composable APIs** - The predicate-action pattern:
   - `IfThis`: Generates predicate functions that identify nodes based on structure, content, or relationships.
   - `Then`: Creates action functions that specify what to do with matched nodes (extract, replace, modify).

4. **Higher-level Tools** - Built from the core components:
   - `_toolkitAST.py`: Functions for common operations like extracting function definitions or importing modules.
   - `transformationTools.py`: Advanced utilities like function inlining and code generation.
   - `IngredientsFunction` and `IngredientsModule`: Containers for holding AST components and their dependencies.

5. **Type System** - Over 120 specialized types for AST components:
   - Custom type annotations for AST node attributes.
   - Union types that accurately model Python's AST structure.
   - Type guards that enable static type checkers to understand dynamic type narrowing.

## My Recovery

[![Static Badge](https://img.shields.io/badge/2011_August-Homeless_since-blue?style=flat)](https://HunterThinks.com/support)
[![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UC3Gx7kz61009NbhpRtPP7tw)](https://www.youtube.com/@HunterHogan)

[![CC-BY-NC-4.0](https://github.com/hunterhogan/astToolkit/blob/main/CC-BY-NC-4.0.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
