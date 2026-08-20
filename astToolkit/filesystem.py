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
	"""Specify keyword arguments for `ast.parse` [1] when calling parse functions in this module.

	(AI generated docstring)

	You can use `astParseParameters` as a `TypedDict` [2] to annotate keyword arguments forwarded
	to `ast.parse` [1] by `parseLogicalPath2astModule` and `parsePathFilename2astModule`. All fields
	are optional (`total=False`).

	Attributes
	----------
	mode : Literal['exec']
		Specifies the kind of code to parse. Only `'exec'` is accepted; only `'exec'` produces an
		`ast.Module` (Module).
	type_comments : bool
		When `True`, `ast.parse` [1] preserves `# type:` and `# type: ignore` (type ***ignore***)
		comments as specified by PEP 484 [3] and PEP 526 [4].
	feature_version : int | tuple[int, int] | None
		A mini-version controlling which Python grammar `ast.parse` [1] uses. For example, `(3, 9)`
		applies Python 3.9 grammar rules. When `None`, `ast.parse` [1] uses the current interpreter
		grammar.
	optimize : Literal[-1, 0, 1, 2]
		Controls AST optimization level (Python 3.13+ [5] only). `0` and `-1` apply no
		optimization; `1` applies basic optimizations; `2` applies aggressive optimizations.

	References
	----------
	[1] ast.parse - Python documentation
		https://docs.python.org/3/library/ast.html#ast.parse
	[2] TypedDict - Python documentation
		https://docs.python.org/3/library/typing.html#typing.TypedDict
	[3] PEP 484 - Type Hints
		https://peps.python.org/pep-0484/
	[4] PEP 526 - Syntax for Variable Annotations
		https://peps.python.org/pep-0526/
	[5] What's New In Python 3.13 - ast module changes
		https://docs.python.org/3/whatsnew/3.13.html
	"""
	mode: Literal['exec']
	type_comments: bool
	feature_version: int | tuple[int, int] | None
	optimize: Literal[-1, 0, 1, 2]

def parsePathFilename2astModule(pathFilename: PathLike[Any] | PurePath, **keywordArguments: Unpack[Parameters_astParse]) -> ast.Module:
	"""Parse a Python source file at `pathFilename` into an `ast.Module` (Module).

	(AI generated docstring)

	You can use `parsePathFilename2astModule` to read the content of a Python source file from
	`pathFilename` and parse it into an `ast.Module` (abstract syntax tree Module) using
	`ast.parse` [1]. `parsePathFilename2astModule` reads the file using UTF-8 encoding.
	`keywordArguments` accepts any subset of the keyword arguments defined in `astParseParameters`,
	forwarded directly to `ast.parse` [1].

	Parameters
	----------
	pathFilename : PathLike[Any] | PurePath
		The filesystem path of the Python source file to parse.

	Returns
	-------
	astModule : ast.Module
		The `ast.Module` (abstract syntax tree Module) representing the parsed source code of the
		file at `pathFilename`.

	ast.parse Parameters
	--------------------
	`keywordArguments` accepts any subset of the following `astParseParameters` [2] keyword
	arguments, which are forwarded directly to `ast.parse` [1].

	mode : Literal['exec'] = 'exec'
		Specifies the kind of code to parse. Only `'exec'` is accepted; only `'exec'` produces an
		`ast.Module` (Module).
	type_comments : bool = False
		When `True`, `ast.parse` [1] preserves `# type:` and `# type: ignore` (type ***ignore***)
		comments as specified by PEP 484 [3] and PEP 526 [4]. Type comments are attached to AST
		nodes in the `type_comment` (a `type` annotation in a comment) field and collected in
		`ast.Module.type_ignores` (type ***ignore*** comments).
	feature_version : int | tuple[int, int] | None = None
		A mini-version for parsing: when set to a tuple such as `(3, 9)`, `ast.parse` [1] attempts
		to parse using Python 3.9 grammar. The lowest supported version is `(3, 7)` as of 2025 July.
		When `None`, `ast.parse` [1] uses the current interpreter grammar.
	optimize : Literal[-1, 0, 1, 2] = -1
		Controls AST optimization level (Python 3.13+ [5] only).
		- `-1`: No optimization (default).
		- `0`: No optimization (same as `-1`).
		- `1`: Basic optimizations, for example constant folding and dead-code removal.
		- `2`: Aggressive optimizations; may remove docstrings.
		When `optimize > 0`, some AST nodes may be omitted or changed.

	References
	----------
	[1] ast.parse - Python documentation
		https://docs.python.org/3/library/ast.html#ast.parse
	[2] astParseParameters - Internal package reference
	[3] PEP 484 - Type Hints
		https://peps.python.org/pep-0484/
	[4] PEP 526 - Syntax for Variable Annotations
		https://peps.python.org/pep-0526/
	[5] What's New In Python 3.13 - ast module changes
		https://docs.python.org/3/whatsnew/3.13.html
	"""
	return ast.parse(Path(pathFilename).read_text(encoding="utf-8"), **keywordArguments)

def parseLogicalPath2astModule(logicalPath: identifierDotAttribute, package: str | None = None, **keywordArguments: Unpack[Parameters_astParse]) -> ast.Module:
	"""Parse the source code of a Python module at a logical import path into an `ast.Module` (Module).

	(AI generated docstring)

	You can use `parseLogicalPath2astModule` to import a module by its logical path (for example,
	`'scipy.signal.windows'`) using `importlib.import_module` [1], retrieve its source code with
	`inspect.getsource` [2], and then parse that source code into an `ast.Module` (abstract syntax
	tree Module) using `ast.parse` [3]. `keywordArguments` accepts any subset of the keyword
	arguments defined in `astParseParameters`, forwarded directly to `ast.parse` [3].

	Parameters
	----------
	logicalPath : identifierDotAttribute
		The logical import path to the module using dot notation (for example, `'numpy.typing'`).
	package : str | None = None
		The anchor package for a relative `logicalPath`, passed directly to
		`importlib.import_module` [1]. Provide `package` when `logicalPath` starts with a dot.

	Returns
	-------
	astModule : ast.Module
		The `ast.Module` (abstract syntax tree Module) representing the parsed source code of the
		imported module.

	ast.parse Parameters
	--------------------
	`keywordArguments` accepts any subset of the following `astParseParameters` [4] keyword
	arguments, which are forwarded directly to `ast.parse` [3].

	mode : Literal['exec'] = 'exec'
		Specifies the kind of code to parse. Only `'exec'` is accepted; only `'exec'` produces an
		`ast.Module` (Module).
	type_comments : bool = False
		When `True`, `ast.parse` [3] preserves `# type:` and `# type: ignore` (type ***ignore***)
		comments as specified by PEP 484 [5] and PEP 526 [6]. Type comments are attached to AST
		nodes in the `type_comment` (a `type` annotation in a comment) field and collected in
		`ast.Module.type_ignores` (type ***ignore*** comments).
	feature_version : int | tuple[int, int] | None = None
		A mini-version for parsing: when set to a tuple such as `(3, 9)`, `ast.parse` [3] attempts
		to parse using Python 3.9 grammar. The lowest supported version is `(3, 7)` as of 2025 July.
		When `None`, `ast.parse` [3] uses the current interpreter grammar.
	optimize : Literal[-1, 0, 1, 2] = -1
		Controls AST optimization level (Python 3.13+ [7] only).
		- `-1`: No optimization (default).
		- `0`: No optimization (same as `-1`).
		- `1`: Basic optimizations, for example constant folding and dead-code removal.
		- `2`: Aggressive optimizations; may remove docstrings.
		When `optimize > 0`, some AST nodes may be omitted or changed.

	References
	----------
	[1] importlib.import_module - Python documentation
		https://docs.python.org/3/library/importlib.html#importlib.import_module
	[2] inspect.getsource - Python documentation
		https://docs.python.org/3/library/inspect.html#inspect.getsource
	[3] ast.parse - Python documentation
		https://docs.python.org/3/library/ast.html#ast.parse
	[4] astParseParameters - Internal package reference
	[5] PEP 484 - Type Hints
		https://peps.python.org/pep-0484/
	[6] PEP 526 - Syntax for Variable Annotations
		https://peps.python.org/pep-0526/
	[7] What's New In Python 3.13 - ast module changes
		https://docs.python.org/3/whatsnew/3.13.html
	"""
	moduleImported: ModuleType = importlib.import_module(logicalPath, package)
	sourcePython: str = inspect_getsource(moduleImported)
	return ast.parse(sourcePython, **keywordArguments)

@overload
def write_astModule(astModule: ast.Module, pathFilename: PathLike[Any] | PurePath, settings: dict[str, dict[str, Any]] | None = None, identifierPackage: str = '') -> Path: ...
@overload
def write_astModule(astModule: ast.Module, pathFilename: io.TextIOBase, settings: dict[str, dict[str, Any]] | None = None, identifierPackage: str = '') ->  io.TextIOBase: ...
def write_astModule(astModule: ast.Module, pathFilename: PathLike[Any] | PurePath | io.TextIOBase, settings: dict[str, dict[str, Any]] | None = None, identifierPackage: str = '') -> Path | io.TextIOBase:
	"""Convert an `ast.Module` (Module) to Python source code and write it to a file or stream.

	(AI generated docstring)

	You can use `write_astModule` to serialize an `ast.Module` `object` to formatted Python source
	code and write the result to a filesystem path or an open text stream. `write_astModule` calls
	`ast.fix_missing_locations` [1] on `astModule` before unparsing, then delegates formatting and
	output to `writePython` from `hunterMakesPy` [2].

	By default, `write_astModule` uses `autoflake` [3] to remove unused imports and `isort` [4] to
	organize import statements. You can override this behavior by providing `settings`.

	Parameters
	----------
	astModule : ast.Module
		(Module) The `ast.Module` `object` to convert and write.
	pathFilename : PathLike[Any] | PurePath | io.TextIOBase
		The destination for the generated Python source code. `pathFilename` may be a filesystem
		path or an open `io.TextIOBase` [5] text stream.
	settings : dict[str, dict[str, Any]] | None = None
		Configuration for code-formatting tools. When `settings` is `None` and `identifierPackage`
		is non-empty, `write_astModule` uses `settings_autoflakeDEFAULT` from `hunterMakesPy` [2].
		Provide nested `dict` entries keyed by tool name (for example, `'autoflake'` or `'isort'`)
		to override the defaults.
	identifierPackage : str = ''
		An optional package name to preserve in the `autoflake` [3] additional-imports list when
		`settings` is `None`. `identifierPackage` has no effect when `settings` is provided.

	Returns
	-------
	outputDestination : Path | io.TextIOBase
		The written `pathlib.Path` `object` when `pathFilename` is a filesystem path, or the
		original `io.TextIOBase` [5] stream after writing when `pathFilename` is a stream.

	References
	----------
	[1] ast.fix_missing_locations - Python documentation
		https://docs.python.org/3/library/ast.html#ast.fix_missing_locations
	[2] hunterMakesPy - Context7
		https://context7.com/hunterhogan/huntermakespy
	[3] autoflake - PyPI
		https://pypi.org/project/autoflake/
	[4] isort - documentation
		https://pycqa.github.io/isort/
	[5] io.TextIOBase - Python documentation
		https://docs.python.org/3/library/io.html#io.TextIOBase
	"""
	ast.fix_missing_locations(astModule)
	pythonSource: str = ast.unparse(astModule)
	if identifierPackage and not settings:
		settings = {'autoflake': settings_autoflakeDEFAULT}
		settings['autoflake']['additional_imports'].append(identifierPackage)  # ty:ignore[unresolved-attribute]
	return writePython(pythonSource, pathFilename, settings)
