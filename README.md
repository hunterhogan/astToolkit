# astToolkit

## Do You Want This Package?

astToolkit provides a powerfully composable system for manipulating Python Abstract Syntax Trees. Use it when:

- You need to programmatically analyze, transform, or generate Python code.
- You want type-safe operations that help prevent AST manipulation errors.
- You prefer working with a consistent, fluent API rather than raw AST nodes.
- You desire the ability to compose complex AST transformations from simple, reusable parts.

Don't use it for simple text-based code manipulation—use regex or string operations instead.

## Architecture

astToolkit implements a layered architecture designed for composability and type safety:

1. **Core "Atomic" Classes** - The foundation of the system:
   - `Be`: Type guards that return `TypeGuard[ast.NodeType]` for safe type narrowing.
   - `DOT`: Read-only accessors that retrieve node attributes with proper typing.
   - `Grab`: Transformation functions that modify specific attributes while preserving node structure.
   - `Make`: Factory methods that create properly configured AST nodes with consistent interfaces.

2. **Traversal and Transformation** - Built on the visitor pattern:
   - `NodeTourist`: Extends `ast.NodeVisitor` to extract information from nodes that match the antecedent (sometimes called "predicate").
   - `NodeChanger`: Extends `ast.NodeTransformer` to selectively transform nodes that match antecedents.

3. **Composable APIs** - The antecedent-action pattern:
   - `ClassIsAndAttribute`: A powerful antecedent constructor: it confirms the class type of `node`, then applies whatever condition check you want to an attribute of `node`. As long as you listen to your type checker, you won't accidentally pair an attribute to a class that doesn't have that attribute. Furthermore, your IDE's hover type hints will tell you which classes are valid for the attribute you are checking.
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

## Usage

astToolkit provides a comprehensive set of tools for AST manipulation, organized in a layered architecture for composability and type safety. The following examples demonstrate how to use these tools in real-world scenarios.

### Core Pattern: Layered AST Manipulation

The astToolkit approach follows a layered pattern:

1. **Create/Access/Check** - Use `Make`, `DOT`, and `Be` to work with AST nodes
2. **Locate** - Use `IfThis` predicates to identify nodes of interest
3. **Transform** - Use `NodeChanger` and `Then` to modify nodes
4. **Extract** - Use `NodeTourist` to collect information from the AST

### Example 1: Extracting Information from AST

This example shows how to extract information from a function's parameters:

```python
from astToolkit import Be, DOT, NodeTourist, Then
import ast

# Parse some Python code into an AST
code = """
def process_data(state: DataClass):
    result = state.value * 2
    return result
"""
tree = ast.parse(code)

# Extract the parameter name from the function
function_def = tree.body[0]
param_name = NodeTourist(
    Be.arg,                  # Look for function parameters
    Then.extractIt(DOT.arg)  # Extract the parameter name
).captureLastMatch(function_def)

print(f"Function parameter name: {param_name}")  # Outputs: state

# Extract the parameter's type annotation
annotation = NodeTourist(
    Be.arg,                       # Look for function parameters
    Then.extractIt(DOT.annotation)  # Extract the type annotation
).captureLastMatch(function_def)

if annotation and Be.Name(annotation):
    annotation_name = DOT.id(annotation)
    print(f"Parameter type: {annotation_name}")  # Outputs: DataClass
```

### Example 2: Transforming AST Nodes

This example demonstrates how to transform a specific node in the AST:

```python
from astToolkit import Be, IfThis, Make, NodeChanger, Then
import ast

# Parse some Python code into an AST
code = """
def double(x):
    return x * 2
"""
tree = ast.parse(code)

# Define a predicate to find the multiplication operation
find_mult = Be.Mult

# Define a transformation to change multiplication to addition
change_to_add = Then.replaceWith(ast.Add())

# Apply the transformation
NodeChanger(find_mult, change_to_add).visit(tree)

# Now the code is equivalent to:
# def double(x):
#     return x + x
print(ast.unparse(tree))
```

### Example 3: Advanced AST Transformation with Custom Predicates

This example shows a more complex transformation inspired by the mapFolding package:

```python
from astToolkit import ast_Identifier, Be, DOT, Grab, IfThis as astToolkit_IfThis, Make, NodeChanger, Then
import ast

# Define custom predicates by extending IfThis
class IfThis(astToolkit_IfThis):
  @staticmethod
  def isAttributeNamespace_IdentifierGreaterThan0(
      namespace: ast_Identifier,
      identifier: ast_Identifier
      ) -> Callable[[ast.AST], TypeGuard[ast.Compare] | bool]:

    return lambda node: (
        Be.Compare(node)
        and IfThis.isAttributeNamespace_Identifier(namespace, identifier)(DOT.left(node))
        and Be.Gt(node.ops[0])
        and IfThis.isConstant_value(0)(node.comparators[0]))

  @staticmethod
  def isWhileAttributeNamespace_IdentifierGreaterThan0(
      namespace: ast_Identifier,
      identifier: ast_Identifier
      ) -> Callable[[ast.AST], TypeGuard[ast.While] | bool]:

    return lambda node: (
        Be.While(node)
        and IfThis.isAttributeNamespace_IdentifierGreaterThan0(namespace, identifier)(DOT.test(node)))

# Parse some code
code = """
while claude.counter > 0:
    result += counter
    counter -= 1
"""
tree = ast.parse(code)

# Find the while loop with our custom predicate
find_while_loop = IfThis.isWhileAttributeNamespace_IdentifierGreaterThan0("claude", "counter")

# Replace counter > 0 with counter > 1
change_condition = Grab.testAttribute(
    Grab.comparatorsAttribute(
        Then.replaceWith([Make.Constant(1)])
    )
)

# Apply the transformation
NodeChanger(find_while_loop, change_condition).visit(tree)

print(ast.unparse(tree))
# Now outputs:
# while counter > 1:
#     result += counter
#     counter -= 1
```

### Example 4: Building Code Generation Systems

The following example shows how to set up a foundation for code generation and transformation systems:

```python
from astToolkit import (
    Be, DOT, IngredientsFunction, IngredientsModule, LedgerOfImports,
    Make, NodeTourist, Then, parseLogicalPath2astModule, write_astModule
)
import ast

# Parse a module to extract a function
module_ast = parseLogicalPath2astModule("my_package.source_module")

# Extract a function and track its imports
function_name = "target_function"
function_def = NodeTourist(
    IfThis.isFunctionDef_Identifier(function_name),
    Then.extractIt
).captureLastMatch(module_ast)

if function_def:
    # Create a self-contained function with tracked imports
    ingredients = IngredientsFunction(
        function_def,
        LedgerOfImports(module_ast)
    )

    # Rename the function
    ingredients.astFunctionDef.name = "optimized_" + function_name

    # Add a decorator
    decorator = Make.Call(
        Make.Name("jit"),
        [],
        [Make.keyword("cache", Make.Constant(True))]
    )
    ingredients.astFunctionDef.decorator_list.append(decorator)

    # Add required import
    ingredients.imports.addImportFrom_asStr("numba", "jit")

    # Create a module and write it to disk
    module = IngredientsModule(ingredients)
    write_astModule(module, "path/to/generated_code.py", "my_package")
```

### Example 5: Extending Core Classes

To create specialized patterns for your codebase, extend the core classes:

```python
from astToolkit import ast_Identifier, Be, IfThis as astToolkit_IfThis
from collections.abc import Callable
from typing import TypeGuard
import ast

class IfThis(astToolkit_IfThis):
    @staticmethod
    def isAttributeNamespace_IdentifierGreaterThan0(
        namespace: ast_Identifier,
        identifier: ast_Identifier
    ) -> Callable[[ast.AST], TypeGuard[ast.Compare] | bool]:
        """Find comparisons like 'state.counter > 0'"""
        return lambda node: (
            Be.Compare(node)
            and IfThis.isAttributeNamespace_Identifier(namespace, identifier)(node.left)
            and Be.Gt(node.ops[0])
            and IfThis.isConstant_value(0)(node.comparators[0])
        )

    @staticmethod
    def isWhileAttributeNamespace_IdentifierGreaterThan0(
        namespace: ast_Identifier,
        identifier: ast_Identifier
    ) -> Callable[[ast.AST], TypeGuard[ast.While] | bool]:
        """Find while loops like 'while state.counter > 0:'"""
        return lambda node: (
            Be.While(node)
            and IfThis.isAttributeNamespace_IdentifierGreaterThan0(namespace, identifier)(node.test)
        )
```

### Real-world Application: Code Transformation Assembly-line

In the [mapFolding](https://github.com/hunterhogan/mapFolding) project, astToolkit is used to build a complete transformation assembly-line that:

1. Extracts algorithms from source modules
2. Transforms them into optimized variants
3. Applies numerical computing decorators
4. Handles dataclass management and type systems
5. Generates complete modules with proper imports

This pattern enables the separation of readable algorithm implementations from their high-performance variants while ensuring they remain functionally equivalent.

For deeper examples, see the [mapFolding/someAssemblyRequired](https://github.com/hunterhogan/mapFolding/tree/main/mapFolding/someAssemblyRequired/) directory.

## Installation

```bash
pip install astToolkit
```

## My Recovery

[![Static Badge](https://img.shields.io/badge/2011_August-Homeless_since-blue?style=flat)](https://HunterThinks.com/support)
[![YouTube Channel Subscribers](https://img.shields.io/youtube/channel/subscribers/UC3Gx7kz61009NbhpRtPP7tw)](https://www.youtube.com/@HunterHogan)

## How to code

Coding One Step at a Time:

0. WRITE CODE.
1. Don't write stupid code that's hard to revise.
2. Write good code.
3. When revising, write better code.

[![CC-BY-NC-4.0](https://github.com/hunterhogan/astToolkit/blob/main/CC-BY-NC-4.0.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
