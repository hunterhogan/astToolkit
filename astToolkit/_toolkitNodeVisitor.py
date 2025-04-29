"""
Core AST Traversal and Transformation Utilities for Python Code Manipulation

This module provides the foundation for traversing and modifying Python Abstract Syntax Trees (ASTs). It contains two
primary classes:

1. NodeTourist: Implements the visitor pattern to traverse an AST and extract information from nodes that match specific
	predicates without modifying the AST.

2. NodeChanger: Extends ast.NodeTransformer to selectively transform AST nodes that match specific predicates, enabling
	targeted code modifications.

The module also provides utilities for importing modules, loading callables from files, and parsing Python code into AST
structures, creating a complete workflow for code analysis and transformation.
"""

from astToolkit import ast_Identifier, str_nameDOTname
from collections.abc import Callable
from inspect import getsource as inspect_getsource
from os import PathLike
from pathlib import Path, PurePath
from types import ModuleType
from typing import Any, Literal
import ast
import importlib
import importlib.util

# TODO Identify the logic that narrows the type and can help the user during static type checking.

class NodeTourist(ast.NodeVisitor):
	"""
	Visit and extract information from AST nodes that match a predicate.

	NodeTourist implements the visitor pattern to traverse an AST, applying a predicate function to each node and
	capturing nodes or their attributes when they match. Unlike NodeChanger, it doesn't modify the AST but collects
	information during traversal.

	This class is particularly useful for analyzing AST structures, extracting specific nodes or node properties, and
	gathering information about code patterns.
	"""
	def __init__(self, findThis: Callable[..., Any], doThat: Callable[..., Any]) -> None:
		self.findThis = findThis
		self.doThat = doThat
		self.nodeCaptured: Any | None = None

	def visit(self, node: ast.AST) -> None:
		if self.findThis(node):
			nodeActionReturn = self.doThat(node)
			if nodeActionReturn is not None:
				self.nodeCaptured = nodeActionReturn
		self.generic_visit(node)

	def captureLastMatch(self, node: ast.AST) -> Any | None:
		self.nodeCaptured = None
		self.visit(node)
		return self.nodeCaptured

class NodeChanger(ast.NodeTransformer):
	"""
	Transform AST nodes that match a predicate by applying a transformation function.

	NodeChanger is an AST node transformer that applies a targeted transformation to nodes matching a specific
	predicate. It traverses the AST and only modifies nodes that satisfy the predicate condition, leaving other nodes
	unchanged.

	This class extends ast.NodeTransformer and implements the visitor pattern to systematically process and transform an
	AST tree.
	"""
	def __init__(self, findThis: Callable[..., Any], doThat: Callable[..., Any]) -> None:
		self.findThis = findThis
		self.doThat = doThat

	def visit(self, node: ast.AST) -> ast.AST:
		if self.findThis(node):
			return self.doThat(node)
		return super().visit(node)

def importLogicalPath2Callable(logicalPathModule: str_nameDOTname, identifier: ast_Identifier, packageIdentifierIfRelative: ast_Identifier | None = None) -> Callable[..., Any]:
	"""
	Import a callable object (function or class) from a module based on its logical path.

	This function imports a module using `importlib.import_module()` and then retrieves a specific attribute (function,
	class, or other object) from that module.

	Parameters
	----------
	logicalPathModule
		The logical path to the module, using dot notation (e.g., 'package.subpackage.module').
	identifier
		The name of the callable object to retrieve from the module.
	packageIdentifierIfRelative : None
		The package name to use as the anchor point if `logicalPathModule` is a relative import. If None, absolute
		import is assumed.

	Returns
	-------
	Callable[..., Any]
		The callable object (function, class, etc.) retrieved from the module.
	"""
	moduleImported: ModuleType = importlib.import_module(logicalPathModule, packageIdentifierIfRelative)
	return getattr(moduleImported, identifier)

def importPathFilename2Callable(pathFilename: PathLike[Any] | PurePath, identifier: ast_Identifier, moduleIdentifier: ast_Identifier | None = None) -> Callable[..., Any]:
	"""
	Load a callable (function, class, etc.) from a Python file.

	This function imports a specified Python file as a module, extracts a callable object from it by name, and returns
	that callable.

	Parameters
	----------
	pathFilename
		Path to the Python file to import.
	identifier
		Name of the callable to extract from the imported module.
	moduleIdentifier
		Name to use for the imported module. If None, the filename stem is used.

	Returns
	-------
	Callable[..., Any]
		The callable object extracted from the imported module.

	Raises
	------
	ImportError
		If the file cannot be imported or the importlib specification is invalid.
	AttributeError
		If the identifier does not exist in the imported module.
	"""
	pathFilename = Path(pathFilename)

	importlibSpecification = importlib.util.spec_from_file_location(moduleIdentifier or pathFilename.stem, pathFilename)
	if importlibSpecification is None or importlibSpecification.loader is None: raise ImportError(f"I received\n\t`{pathFilename = }`,\n\t`{identifier = }`, and\n\t`{moduleIdentifier = }`.\n\tAfter loading, \n\t`importlibSpecification` {'is `None`' if importlibSpecification is None else 'has a value'} and\n\t`importlibSpecification.loader` is unknown.")

	moduleImported_jk_hahaha: ModuleType = importlib.util.module_from_spec(importlibSpecification)
	importlibSpecification.loader.exec_module(moduleImported_jk_hahaha)
	return getattr(moduleImported_jk_hahaha, identifier)

def parseLogicalPath2astModule(logicalPathModule: str_nameDOTname, packageIdentifierIfRelative: ast_Identifier | None = None, mode: Literal['exec'] = 'exec') -> ast.Module:
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
	mode : Literal['exec']
		The mode parameter for `ast.parse`. Default is `Literal['exec']`. Options are `Literal['exec']`, `"exec"` (which
		is _not_ the same as `Literal['exec']`), `Literal['eval']`, `Literal['func_type']`, `Literal['single']`. See
		`ast.parse` documentation for some details and much confusion.

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
	mode : Literal['exec']
		The mode parameter for `ast.parse`. Default is `Literal['exec']`. Options are `Literal['exec']`, `"exec"` (which
		is _not_ the same as `Literal['exec']`), `Literal['eval']`, `Literal['func_type']`, `Literal['single']`. See
		`ast.parse` documentation for some details and much confusion.

	Returns
	-------
	astModule
		The parsed abstract syntax tree module.
	"""
	return ast.parse(Path(pathFilename).read_text(), mode)
