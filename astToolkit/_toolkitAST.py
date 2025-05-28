from astToolkit import (
	identifierDotAttribute, IfThis, IngredientsFunction, LedgerOfImports, NodeTourist, Then,
)
from inspect import getsource as inspect_getsource
from os import PathLike
from pathlib import Path, PurePath
from types import ModuleType
from typing import Any, Literal
from Z0Z_tools import raiseIfNone
import ast
import importlib

def astModuleToIngredientsFunction(astModule: ast.AST, identifierFunctionDef: str) -> IngredientsFunction:
	"""
	Extract a function definition from an AST module and create an `IngredientsFunction`.

	This function finds a function definition with the specified identifier in the given AST module, extracts it, and
	stores all module imports in the `LedgerOfImports`.

	Parameters:
		astModule: The AST module containing the function definition.
		identifierFunctionDef: The name of the function to extract.

	Returns:
		ingredientsFunction: `IngredientsFunction` object containing the `ast.FunctionDef` and _all_ imports from the
		source module.
	"""
	astFunctionDef = raiseIfNone(extractFunctionDef(astModule, identifierFunctionDef))
	return IngredientsFunction(astFunctionDef, LedgerOfImports(astModule))

def extractClassDef(module: ast.AST, identifier: str) -> ast.ClassDef | None:
	"""
	Extract a class definition with a specific name from an AST module.

	This function searches through an AST module for a class definition that matches the provided identifier and returns
	it if found.

	Parameters:
		module: The AST module to search within.
		identifier: The name of the class to find.

	Returns:
		astClassDef|None: The matching class definition AST node, or `None` if not found.
	"""
	return NodeTourist(IfThis.isClassDefIdentifier(identifier), Then.extractIt).captureLastMatch(module)

def extractFunctionDef(module: ast.AST, identifier: str) -> ast.FunctionDef | None:
	"""
	Extract a function definition with a specific name from an AST module.

	This function searches through an AST module for a function definition that matches the provided identifier and
	returns it if found.

	Parameters:
		module: The AST module to search within.
		identifier: The name of the function to find.

	Returns:
		astFunctionDef|None: The matching function definition AST node, or `None` if not found.
	"""
	return NodeTourist(IfThis.isFunctionDefIdentifier(identifier), Then.extractIt).captureLastMatch(module)

def parseLogicalPath2astModule(logicalPathModule: identifierDotAttribute, packageIdentifierIfRelative: str | None = None, mode: Literal['exec'] = 'exec') -> ast.Module:
	"""
	Parse a logical Python module path into an `ast.Module`.

	This function imports a module using its logical path (e.g., 'package.subpackage.module') and converts its source
	code into an Abstract Syntax Tree (AST) Module object.

	Parameters
	----------
	logicalPathModule
		The logical path to the module using dot notation (e.g., 'package.module').
	packageIdentifierIfRelative : None
		The package identifier to use if the module path is relative, defaults to None.
	mode : 'exec'
		The mode parameter for `ast.parse`. Default is `'exec'`. Options are `'exec'`, `'eval'`, `'func_type'`, `'single'`. See
		`ast.parse` documentation.

	Returns
	-------
	astModule
		An AST Module object representing the parsed source code of the imported module.
	"""
	moduleImported: ModuleType = importlib.import_module(logicalPathModule, packageIdentifierIfRelative)
	sourcePython: str = inspect_getsource(moduleImported)
	return ast.parse(sourcePython, mode)

def parsePathFilename2astModule(pathFilename: PathLike[Any] | PurePath, mode: Literal['exec'] = 'exec') -> ast.Module:
	"""
	Parse a file from a given path into an `ast.Module`.

	This function reads the content of a file specified by `pathFilename` and parses it into an Abstract Syntax Tree
	(AST) Module using Python's ast module.

	Parameters
	----------
	pathFilename
		The path to the file to be parsed. Can be a string path, PathLike object, or PurePath object.
	mode : 'exec'
		The mode parameter for `ast.parse`. Default is `'exec'`. Options are `'exec'`, `'eval'`, `'func_type'`, `'single'`. See
		`ast.parse` documentation.

	Returns
	-------
	astModule
		The parsed abstract syntax tree module.
	"""
	return ast.parse(Path(pathFilename).read_text(), mode)

