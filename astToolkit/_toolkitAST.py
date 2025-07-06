from astToolkit import identifierDotAttribute, IfThis, IngredientsFunction, LedgerOfImports, NodeTourist, Then
from hunterMakesPy import raiseIfNone
from inspect import getsource as inspect_getsource
from os import PathLike
from pathlib import Path, PurePath
from typing import Any, Literal, TYPE_CHECKING, TypedDict, Unpack
import ast
import importlib
import sys

if sys.version_info >= (3, 13):
	# The 'optimize' parameter is only available in Python 3.13+
	class astParseParameters(TypedDict, total=False):
		mode: Literal['exec']
		type_comments: bool
		feature_version: int | tuple[int, int] | None
		optimize: Literal[-1, 0, 1, 2]
else:
	class astParseParameters(TypedDict, total=False):
		mode: Literal['exec']
		type_comments: bool
		feature_version: int | tuple[int, int] | None

if TYPE_CHECKING:
	from types import ModuleType

def astModuleToIngredientsFunction(astAST: ast.AST, identifier: str) -> IngredientsFunction:
	"""
	Extract a function definition from an AST module and create an `IngredientsFunction`.

	(AI generated docstring)

	This function finds a function definition with the specified identifier in the given AST module, extracts it, and stores all module imports in the `LedgerOfImports`.

	Parameters
	----------
	astAST : ast.AST
		The AST module containing the function definition.
	identifier : str
		The name of the function to extract.

	Returns
	-------
	ingredientsFunction
		`IngredientsFunction` object containing the `ast.FunctionDef` and all imports from the source module.

	"""
	astFunctionDef: ast.FunctionDef = raiseIfNone(extractFunctionDef(astAST, identifier))
	return IngredientsFunction(astFunctionDef, LedgerOfImports(astAST))

def extractClassDef(astAST: ast.AST, identifier: str) -> ast.ClassDef | None:
	"""
	Extract an `ast.ClassDef` from an `ast.AST` `object`.

	This function searches through `ast.AST` for an `ast.ClassDef` that matches the provided identifier and returns it if found.

	Parameters
	----------
	astAST : ast.AST
		The AST object to search within.
	identifier : str
		The name of the class to find.

	Returns
	-------
	astClassDef | None
		The matching class definition AST node, or `None` if not found.

	"""
	return NodeTourist(IfThis.isClassDefIdentifier(identifier), Then.extractIt).captureLastMatch(astAST)

def extractFunctionDef(astAST: ast.AST, identifier: str) -> ast.FunctionDef | None:
	"""
	Extract a function definition with a specific name from an AST module.

	(AI generated docstring)

	This function searches through an AST module for a function definition that matches the provided identifier and returns it if found.

	Parameters
	----------
	astAST : ast.AST
		The AST object to search within.
	identifier : str
		The name of the function to find.

	Returns
	-------
	astFunctionDef | None
		The matching function definition AST node, or `None` if not found.

	"""
	return NodeTourist(IfThis.isFunctionDefIdentifier(identifier), Then.extractIt).captureLastMatch(astAST)

def parseLogicalPath2astModule(logicalPath: identifierDotAttribute, package: str | None = None, **keywordArguments: Unpack[astParseParameters]) -> ast.Module:
	"""
	Parse a logical Python module path into an `ast.Module`.

	(AI generated docstring)

	This function imports a module using its logical path (e.g., 'scipy.signal.windows') and converts its source code into an
	`ast.Module` (abstract syntax tree) object. Supports all relevant `ast.parse` parameters.

	Parameters
	----------
	logicalPath : identifierDotAttribute
		The logical path to the module using dot notation (e.g., 'numpy.typing').
	package : str | None = None
		The package identifier to use if the module path is relative, defaults to None.
	mode : Literal['exec', 'eval', 'func_type', 'single'] = 'exec'
		Specifies the kind of code to parse
		- 'exec': Parse a module or sequence of statements (default; produces an `ast.Module`).
		- 'eval': Parse a single expression (produces an `ast.Expression`).
		- 'single': Parse a single interactive statement (produces an `ast.Interactive`).
		- 'func_type': Parse a function type annotation (produces an `ast.FunctionType`).
	type_comments : bool = False
		If True, preserves type comments as specified by PEP 484 and PEP 526. This includes `# type:` and `# type: ignore`
		comments, which are attached to AST nodes as the `type_comment` field and collected in the `type_ignores` attribute of
		`ast.Module`. If False, type comments are ignored and not present in the AST.
	feature_version : int | tuple[int, int] | None = None
		A "mini-version" for parsing: if set to a tuple like (3, 9), attempts to parse using Python 3.9 grammar, disallowing
		features introduced in later versions (best-effort, not guaranteed to match the actual Python version). The lowest
		supported is (3, 7) as of 2025 July; the highest is the running interpreter's version. If None, uses the current interpreter's grammar.
	optimize : Literal[-1, 0, 1, 2] = -1
		Controls AST optimization level (Python 3.13+ only)
		- -1: No optimization (default; equivalent to ast.PyCF_ONLY_AST).
		- 0: No optimization (same as -1).
		- 1: Basic optimizations (e.g., constant folding, dead code removal).
		- 2: Aggressive optimizations (may remove docstrings and perform more constant folding).
		If optimize > 0, the returned AST may be altered for performance, and some code objects may be omitted or changed.

	Returns
	-------
	astModule
		An AST Module object representing the parsed source code of the imported module.

	"""
	moduleImported: ModuleType = importlib.import_module(logicalPath, package)
	sourcePython: str = inspect_getsource(moduleImported)
	return ast.parse(sourcePython, **keywordArguments)

def parsePathFilename2astModule(pathFilename: PathLike[Any] | PurePath, **keywordArguments: Unpack[astParseParameters]) -> ast.Module:
	"""
	Parse a file from a given path into an `ast.Module`.

	(AI generated docstring)

	This function reads the content of a file specified by `pathFilename` and parses it into an Abstract Syntax Tree (AST) Module
	using Python's ast module. Supports all relevant `ast.parse` parameters.

	Parameters
	----------
	pathFilename : PathLike[Any] | PurePath
		The path to the file to be parsed.
	mode : Literal['exec', 'eval', 'func_type', 'single'] = 'exec'
		Specifies the kind of code to parse
		- 'exec': Parse a module or sequence of statements (default; produces an `ast.Module`).
		- 'eval': Parse a single expression (produces an `ast.Expression`).
		- 'single': Parse a single interactive statement (produces an `ast.Interactive`).
		- 'func_type': Parse a function type annotation (produces an `ast.FunctionType`).
	type_comments : bool = False
		If True, preserves type comments as specified by PEP 484 and PEP 526. This includes `# type:` and `# type: ignore`
		comments, which are attached to AST nodes as the `type_comment` field and collected in the `type_ignores` attribute of
		`ast.Module`. If False, type comments are ignored and not present in the AST.
	feature_version : int | tuple[int, int] | None = None
		A "mini-version" for parsing: if set to a tuple like (3, 9), attempts to parse using Python 3.9 grammar, disallowing
		features introduced in later versions (best-effort, not guaranteed to match the actual Python version). The lowest
		supported is (3, 7) as of 2025 July; the highest is the running interpreter's version. If None, uses the current interpreter's grammar.
	optimize : Literal[-1, 0, 1, 2] = -1
		Controls AST optimization level (Python 3.13+ only)
		- -1: No optimization (default; equivalent to ast.PyCF_ONLY_AST).
		- 0: No optimization (same as -1).
		- 1: Basic optimizations (e.g., constant folding, dead code removal).
		- 2: Aggressive optimizations (may remove docstrings and perform more constant folding).
		If optimize > 0, the returned AST may be altered for performance, and some code objects may be omitted or changed.

	Returns
	-------
	astModule
		The parsed abstract syntax tree module.

	"""
	return ast.parse(Path(pathFilename).read_text(encoding="utf-8"), **keywordArguments)

