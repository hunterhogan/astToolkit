"""Read Python source into AST modules and write AST modules as formatted Python.

(AI generated docstring)

You can obtain an `ast.Module` (abstract syntax tree Module) from a UTF-8 source file or
an importable module, then write generated or transformed source to a file or text stream.
Parser options control grammar selection, type comments, and AST optimization.

Contents
--------
Functions
	parseLogicalPath2astModule
		Import a module and parse its available Python source.
	parsePathFilename2astModule
		Parse a UTF-8 Python source file without importing it.
	write_astModule
		Format Python source from an AST module and write it to a file or text stream.

Classes
	Parameters_astParse
		Describe optional parser settings for the source-reading functions.
"""

from __future__ import annotations

from hunterMakesPy.filesystemToolkit import settings_autoflakeDEFAULT, writePython
from inspect import getsource as inspect_getsource
from pathlib import Path
from typing import overload, TYPE_CHECKING, TypedDict, Unpack
import ast
import importlib

if TYPE_CHECKING:
	from astToolkit import identifierDotAttribute
	from os import PathLike
	from pathlib import PurePath
	from types import ModuleType
	from typing import Any, Literal
	import io

class Parameters_astParse(TypedDict, total=False):
	"""Specify parser options for producing an `ast.Module` (Module).

	(AI generated docstring)

	You can use `Parameters_astParse` to annotate keyword arguments for
	`parseLogicalPath2astModule` and `parsePathFilename2astModule`. Every key is optional.
	The attribute defaults below apply when a key is omitted.

	Attributes
	----------
	mode : {'exec'} = 'exec'
		The parsing mode that produces an `ast.Module` (Module).
	type_comments : bool = False
		Whether to preserve `# type:` comments and collect `# type: ignore` (type ***ignore***)
		comments in `ast.Module.type_ignores`.
	feature_version : int | tuple[int, int] | None = None
		The Python grammar version to request. An integer selects a Python 3 minor version;
		a tuple specifies `(3, minor)`. `None` uses the running interpreter's grammar.
		The requested grammar is an approximation, not an exact older interpreter [1].
	optimize : {-1, 0, 1, 2} = -1
		The AST optimization level. `-1` and `0` produce an unoptimized tree; positive levels
		request an optimized tree [1], which can change or remove source constructs.

	See Also
	--------
	`parseLogicalPath2astModule`
		Parse an imported module with these options.
	`parsePathFilename2astModule`
		Parse a UTF-8 source file with these options.

	References
	----------
	[1] Python documentation, `ast.parse`.
		https://docs.python.org/3/library/ast.html#ast.parse
	"""
	mode: Literal['exec']
	type_comments: bool
	feature_version: int | tuple[int, int] | None
	optimize: Literal[-1, 0, 1, 2]

def parsePathFilename2astModule(pathFilename: PathLike[Any] | PurePath, **keywordArguments: Unpack[Parameters_astParse]) -> ast.Module:
	"""Parse a UTF-8 Python source file into an `ast.Module` (Module).

	(AI generated docstring)

	Parameters
	----------
	pathFilename : PathLike[Any] | PurePath
		The filesystem path of the Python source file to parse.
	keywordArguments : Unpack[Parameters_astParse]
		Optional parser settings. Omitted settings use the defaults documented in
		`Parameters_astParse`.

	Returns
	-------
	astModule : ast.Module
		The `ast.Module` (abstract syntax tree Module) representing the file's source code.

	See Also
	--------
	`Parameters_astParse`
		Inspect the accepted parser settings and their defaults.
	`parseLogicalPath2astModule`
		Parse a module identified by its import path.
	`write_astModule`
		Write an AST module as formatted Python source.
	"""
	return ast.parse(Path(pathFilename).read_text(encoding="utf-8"), **keywordArguments)

def parseLogicalPath2astModule(logicalPath: identifierDotAttribute, package: str | None = None, **keywordArguments: Unpack[Parameters_astParse]) -> ast.Module:
	"""Parse a module at a logical import path into an `ast.Module` (Module).

	(AI generated docstring)

	You can obtain the source tree of an importable Python module without locating its source
	file yourself. The module must have source code available to `inspect.getsource`.

	Parameters
	----------
	logicalPath : identifierDotAttribute
		The module's logical import path in dot notation.
	package : str | None = None
		The anchor package for a relative `logicalPath`. Supply `package` when
		`logicalPath` starts with a dot.
	keywordArguments : Unpack[Parameters_astParse]
		Optional parser settings. Omitted settings use the defaults documented in
		`Parameters_astParse`.

	Returns
	-------
	astModule : ast.Module
		The `ast.Module` (abstract syntax tree Module) representing the imported module's source.

	See Also
	--------
	`Parameters_astParse`
		Inspect the accepted parser settings and their defaults.
	`parsePathFilename2astModule`
		Read source directly from a file without importing the module.

	Module Import
	-------------
	Importing `logicalPath` can execute module-level code before the source is parsed.
	"""
	moduleImported: ModuleType = importlib.import_module(logicalPath, package)
	sourcePython: str = inspect_getsource(moduleImported)
	return ast.parse(sourcePython, **keywordArguments)

@overload
def write_astModule(astModule: ast.Module, pathFilename: PathLike[Any] | PurePath, settings: dict[str, dict[str, Any]] | None = None, identifierPackage: str = '') -> Path: ...
@overload
def write_astModule(astModule: ast.Module, pathFilename: io.TextIOBase, settings: dict[str, dict[str, Any]] | None = None, identifierPackage: str = '') ->  io.TextIOBase: ...
def write_astModule(astModule: ast.Module, pathFilename: PathLike[Any] | PurePath | io.TextIOBase, settings: dict[str, dict[str, Any]] | None = None, identifierPackage: str = '') -> Path | io.TextIOBase:
	"""Write an `ast.Module` (Module) as formatted Python source to a file or text stream.

	(AI generated docstring)

	You can write generated or transformed source with unused imports removed by `autoflake`
	and import statements organized by `isort`. The `settings` entries configure these tools.

	Parameters
	----------
	astModule : ast.Module
		(Module) The source tree to convert and write.
	pathFilename : PathLike[Any] | PurePath | io.TextIOBase
		The destination file path or open text stream.
	settings : dict[str, dict[str, Any]] | None = None
		Formatter settings keyed by tool name. The `'autoflake'` and `'isort'` entries each
		replace that tool's defaults. Missing entries use the defaults from `hunterMakesPy`.
		`None` and an empty `dict` use defaults, with the package adjustment described below.
	identifierPackage : str = ''
		A package name to add to the `autoflake` additional-imports list when `settings` is
		`None` or empty. A nonempty `settings` mapping disables this adjustment.

	Returns
	-------
	outputDestination : Path | io.TextIOBase
		The written `pathlib.Path` for a filesystem destination, or the supplied text stream.

	See Also
	--------
	`parsePathFilename2astModule`
		Read a Python source file into an AST module.
	`astToolkit.containers.IngredientsModule`
		Assemble module sections and imports before writing source.

	Source and Destination Changes
	------------------------------
	Missing source locations are filled in on `astModule` in place. An existing destination
	file is overwritten; text streams receive text at their current position.

	When `identifierPackage` applies, the package name is appended to the shared
	`settings_autoflakeDEFAULT['additional_imports']` list from `hunterMakesPy`. The name
	therefore remains in that default list for later writes in the same process.
	"""
	ast.fix_missing_locations(astModule)
	pythonSource: str = ast.unparse(astModule)
	if identifierPackage and not settings:
		settings = {'autoflake': settings_autoflakeDEFAULT}
		settings['autoflake']['additional_imports'].append(identifierPackage)  # ty:ignore[unresolved-attribute]
	return writePython(pythonSource, pathFilename, settings)
