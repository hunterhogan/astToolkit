"""
AST Transformation Tools for Code Optimization and Generation.

(AI generated docstring)

This module provides higher-level transformation tools that operate on AST structures to perform complex code optimizations and
transformations. The module includes five key functions:

1. makeDictionaryFunctionDef: Creates a lookup dictionary mapping function names to their AST definitions within a module,
	enabling efficient access to specific function definitions.

2. inlineFunctionDef: Performs function inlining by recursively substituting function calls with their implementation bodies,
	creating self-contained functions without external dependencies.

3. removeUnusedParameters: Optimizes function signatures by analyzing and removing unused parameters, updating the function
	signature, return statements, and type annotations accordingly.

4. unparseFindReplace: Recursively replaces AST nodes throughout a tree structure using textual representation matching, providing
	a brute-force but effective approach for complex replacements.

5. write_astModule: Converts an IngredientsModule to optimized Python source code and writes it to a file, handling import
	organization and code formatting in the process.

These transformation tools form the backbone of the code optimization pipeline, enabling sophisticated code transformations while
maintaining semantic integrity and performance characteristics.
"""
from astToolkit._namespaceUncertainty import (
	inlineFunctionDef as inlineFunctionDef, makeDictionaryAsyncFunctionDef as makeDictionaryAsyncFunctionDef,
	makeDictionaryClassDef as makeDictionaryClassDef, makeDictionaryFunctionDef as makeDictionaryFunctionDef,
	makeDictionaryMosDef as makeDictionaryMosDef, pythonCode2ast_expr as pythonCode2ast_expr, removeUnusedParameters as removeUnusedParameters,
	unjoinBinOP as unjoinBinOP, unparseFindReplace as unparseFindReplace, write_astModule as write_astModule)
