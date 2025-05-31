"""
AST Toolkit for Python - A comprehensive utility library for AST manipulation and transformation

The astToolkit package provides a powerful set of tools for working with Python's Abstract Syntax Tree (AST),
enabling sophisticated code analysis, transformation, and generation. The toolkit is designed around a
composable architecture with specialized modules for different aspects of AST manipulation:

Core Components:
- NodeTourist/NodeChanger: AST traversal and transformation engines
- Make: Factory methods for creating AST nodes with clean semantics
- IfThis/Then: Predicate-based node matching and transformation
- IngredientsFunction/IngredientsModule: Containers for storing code components with dependencies

Tool Categories:
- Antecedents: Be, ClassIsAndAttribute, IfThis
- Actions: Make, Then
- Modify antecedents and actions: DOT, Grab
- AST Organization: LedgerOfImports - Manage import statements
- Code Generation: extractFunctionDef, parseLogicalPath2astModule - Extract and parse code

The toolkit enables developers to perform complex AST operations with semantically clear code,
maintaining type safety and providing a declarative approach to code transformation.
"""

from astToolkit._astTypes import *  # noqa: F403

from astToolkit._types import (
	identifierDotAttribute as identifierDotAttribute,
)

# from astToolkit._dumpFunctionDef import dump as dump
from astToolkit._dumpHandmade import dump as dump

from astToolkit._toolkitNodeVisitor import (
	NodeChanger as NodeChanger,
	NodeTourist as NodeTourist,
)

from astToolkit._toolBe import Be as Be
from astToolkit._toolClassIsAndAttribute import ClassIsAndAttribute as ClassIsAndAttribute
from astToolkit._toolDOT import DOT as DOT
from astToolkit._toolGrab import Grab as Grab
from astToolkit._toolMake import Make as Make

from astToolkit._toolIfThis import IfThis as IfThis
from astToolkit._toolThen import Then as Then

from astToolkit._toolkitContainers import (
	IngredientsFunction as IngredientsFunction,
	IngredientsModule as IngredientsModule,
	LedgerOfImports as LedgerOfImports,
)

from astToolkit._toolkitAST import (
	astModuleToIngredientsFunction as astModuleToIngredientsFunction,
	extractClassDef as extractClassDef,
	extractFunctionDef as extractFunctionDef,
	parseLogicalPath2astModule as parseLogicalPath2astModule,
	parsePathFilename2astModule as parsePathFilename2astModule,
)
