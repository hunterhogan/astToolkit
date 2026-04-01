"""IDK how I want to organize the namespace."""
from astToolkit import Be, DOT, Grab, identifierDotAttribute, IfThis, Make, NodeChanger, NodeTourist, Then
from collections.abc import Mapping
from copy import deepcopy
from hunterMakesPy import raiseIfNone
from hunterMakesPy.filesystemToolkit import settings_autoflakeDEFAULT, writePython
from inspect import getsource as inspect_getsource
from os import PathLike
from pathlib import Path, PurePath
from types import ModuleType
from typing import Any, Literal, overload, TypedDict, Unpack
import ast
import importlib
import io

def makeDictionaryAsyncFunctionDef(astAST: ast.AST) -> dict[str, ast.AsyncFunctionDef]:
	"""Make a `dict` (***dict***ionary) mapping each `async def` (***async***hronous ***def***inition) function name to its `ast.AsyncFunctionDef` (***Async***hronous Function ***Def***inition) `object`.

	(AI generated docstring)

	You can use `makeDictionaryAsyncFunctionDef` to collect every `ast.AsyncFunctionDef` found anywhere
	in an `ast.AST` (Abstract Syntax Tree) `object`, organized into a `dict` indexed by
	`ast.AsyncFunctionDef.name`.

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The `ast.AST` `object` to search for `ast.AsyncFunctionDef` nodes.

	Returns
	-------
	dictionaryIdentifier2AsyncFunctionDef : dict[str, ast.AsyncFunctionDef]
		A `dict` mapping each `ast.AsyncFunctionDef.name` `str` to its `ast.AsyncFunctionDef` `object`.

	References
	----------
	[1] ast.AsyncFunctionDef - Python documentation
		https://docs.python.org/3/library/ast.html#ast.AsyncFunctionDef
	[2] astToolkit - Context7
		https://context7.com/hunterhogan/asttoolkit
	"""
	dictionaryIdentifier2AsyncFunctionDef: dict[str, ast.AsyncFunctionDef] = {}
	NodeTourist(Be.AsyncFunctionDef, Then.updateKeyValueIn(DOT.name, Then.extractIt, dictionaryIdentifier2AsyncFunctionDef)).visit(astAST)  # ty:ignore[invalid-argument-type]
	return dictionaryIdentifier2AsyncFunctionDef

def makeDictionaryClassDef(astAST: ast.AST) -> dict[str, ast.ClassDef]:
	"""Make a `dict` (***dict***ionary) mapping each `class` definition name to its `ast.ClassDef` (***Class*** ***Def***inition) `object`.

	(AI generated docstring)

	You can use `makeDictionaryClassDef` to collect every `ast.ClassDef` found anywhere in an
	`ast.AST` (Abstract Syntax Tree) `object`, organized into a `dict` indexed by `ast.ClassDef.name`.

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The `ast.AST` `object` to search for `ast.ClassDef` nodes.

	Returns
	-------
	dictionaryIdentifier2ClassDef : dict[str, ast.ClassDef]
		A `dict` mapping each `ast.ClassDef.name` `str` to its `ast.ClassDef` `object`.

	References
	----------
	[1] ast.ClassDef - Python documentation
		https://docs.python.org/3/library/ast.html#ast.ClassDef
	[2] astToolkit - Context7
		https://context7.com/hunterhogan/asttoolkit
	"""
	dictionaryIdentifier2ClassDef: dict[str, ast.ClassDef] = {}
	NodeTourist(Be.ClassDef, Then.updateKeyValueIn(DOT.name, Then.extractIt, dictionaryIdentifier2ClassDef)).visit(astAST)  # ty:ignore[invalid-argument-type]
	return dictionaryIdentifier2ClassDef

def makeDictionaryFunctionDef(astAST: ast.AST) -> dict[str, ast.FunctionDef]:
	"""Make a `dict` (***dict***ionary) mapping each `def` (***def***inition) function name to its `ast.FunctionDef` (Function ***Def***inition) `object`.

	(AI generated docstring)

	You can use `makeDictionaryFunctionDef` to collect every `ast.FunctionDef` found anywhere in an
	`ast.AST` (Abstract Syntax Tree) `object`, organized into a `dict` indexed by
	`ast.FunctionDef.name`.

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The `ast.AST` `object` to search for `ast.FunctionDef` nodes.

	Returns
	-------
	dictionaryIdentifier2FunctionDef : dict[str, ast.FunctionDef]
		A `dict` mapping each `ast.FunctionDef.name` `str` to its `ast.FunctionDef` `object`.

	References
	----------
	[1] ast.FunctionDef - Python documentation
		https://docs.python.org/3/library/ast.html#ast.FunctionDef
	[2] astToolkit - Context7
		https://context7.com/hunterhogan/asttoolkit
	"""
	dictionaryIdentifier2FunctionDef: dict[str, ast.FunctionDef] = {}
	NodeTourist(Be.FunctionDef, Then.updateKeyValueIn(DOT.name, Then.extractIt, dictionaryIdentifier2FunctionDef)).visit(astAST)  # ty:ignore[invalid-argument-type]
	return dictionaryIdentifier2FunctionDef

def makeDictionaryMosDef(astAST: ast.AST) -> dict[str, ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef]:
	"""Make a `dict` (***dict***ionary) mapping each identifier to its `ast.AsyncFunctionDef` (***Async***hronous Function ***Def***inition), `ast.ClassDef` (***Class*** ***Def***inition), or `ast.FunctionDef` (Function ***Def***inition) `object`.

	(AI generated docstring)

	You can use `makeDictionaryMosDef` to collect every `ast.AsyncFunctionDef`, `ast.ClassDef`, and
	`ast.FunctionDef` found anywhere in an `ast.AST` (Abstract Syntax Tree) `object`, organized into
	a single `dict` indexed by name. `makeDictionaryMosDef` combines the results of
	`makeDictionaryAsyncFunctionDef`, `makeDictionaryClassDef`, and `makeDictionaryFunctionDef`.

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The `ast.AST` `object` to search for `ast.AsyncFunctionDef`,
		`ast.ClassDef`, and `ast.FunctionDef` nodes.

	Returns
	-------
	dictionaryIdentifier2MosDef : dict[str, ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef]
		A `dict` mapping each definition name `str` to its `ast.AsyncFunctionDef`,
		`ast.ClassDef`, or `ast.FunctionDef` `object`.

	See Also
	--------
	makeDictionaryAsyncFunctionDef : Collect only `ast.AsyncFunctionDef` nodes.
	makeDictionaryClassDef : Collect only `ast.ClassDef` nodes.
	makeDictionaryFunctionDef : Collect only `ast.FunctionDef` nodes.

	References
	----------
	[1] ast - Abstract Syntax Trees - Python documentation
		https://docs.python.org/3/library/ast.html
	[2] astToolkit - Context7
		https://context7.com/hunterhogan/asttoolkit
	"""
	dictionaryIdentifier2MosDef: dict[str, ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef] = {}
	dictionaryIdentifier2MosDef.update(makeDictionaryAsyncFunctionDef(astAST))
	dictionaryIdentifier2MosDef.update(makeDictionaryClassDef(astAST))
	dictionaryIdentifier2MosDef.update(makeDictionaryFunctionDef(astAST))
	return dictionaryIdentifier2MosDef

def inlineFunctionDef(identifierToInline: str, astModule: ast.Module) -> ast.FunctionDef:
	"""Synthesize an `ast.FunctionDef` (Function ***Def***inition) with each called function's `body` substituted inline.

	(AI generated docstring)

	You can use `inlineFunctionDef` to transform the `ast.FunctionDef` (Function ***Def***inition)
	named `identifierToInline` in `astModule` (abstract syntax tree Module) by replacing calls to
	other functions defined in the same `astModule` with each matched function's `body`.

	`inlineFunctionDef` searches `identifierToInline` for `ast.Call` (Call) nodes that target an
	`ast.Name` (***id***entifier), for example `Path`, but not an `ast.Attribute` (***attr***ibute)
	such as `pathlib.Path`. The `ast.Name.id` (***id***entifier) must match an `ast.FunctionDef.name`
	in `astModule`. When a match is found, `inlineFunctionDef` replaces the `ast.Call` with the
	body of the matched `ast.FunctionDef`.

	`inlineFunctionDef` repeats the inlining process until no more locally defined functions remain
	to be inlined. Functions not called directly by `identifierToInline` in the original `astModule`
	may therefore be inlined if they are called by an already-inlined function.

	Parameters
	----------
	identifierToInline : str
		The name of the target `ast.FunctionDef` (Function ***Def***inition); `identifierToInline`
		must match an `ast.FunctionDef.name` in `astModule`.
	astModule : ast.Module
		(abstract syntax tree Module) An `ast.Module` containing the `ast.FunctionDef` named
		`identifierToInline` and zero or more additional `ast.FunctionDef` `object` to inline.

	Returns
	-------
	FunctionDefToInline : ast.FunctionDef
		The synthesized `ast.FunctionDef` (Function ***Def***inition) with inlined logic from
		other functions defined in `astModule`.

	Raises
	------
	ValueError
		Raised when `identifierToInline` does not match any `ast.FunctionDef.name` in `astModule`.

	Inlining Restrictions
	---------------------
	`inlineFunctionDef` does not inline an `ast.FunctionDef` if that `ast.FunctionDef` calls itself
	(direct recursion), or if any function transitively reachable from `identifierToInline` calls
	back to `identifierToInline` (mutual recursion). Recursive call graphs are left unchanged.

	References
	----------
	[1] ast.FunctionDef - Python documentation
		https://docs.python.org/3/library/ast.html#ast.FunctionDef
	[2] ast.Call - Python documentation
		https://docs.python.org/3/library/ast.html#ast.Call
	[3] Inline expansion - Wikipedia
		https://en.wikipedia.org/wiki/Inline_expansion
	[4] astToolkit - Context7
		https://context7.com/hunterhogan/asttoolkit
	"""
	dictionaryFunctionDef: dict[str, ast.FunctionDef] = makeDictionaryFunctionDef(astModule)
	try:
		FunctionDefToInline = dictionaryFunctionDef[identifierToInline]
	except KeyError as ERRORmessage:
		message = f"I was unable to find an `ast.FunctionDef` with name {identifierToInline = } in {astModule = }."
		raise ValueError(message) from ERRORmessage

	listIdentifiersCalledFunctions: list[str] = []
	findIdentifiersToInline = NodeTourist[ast.Call, ast.expr](IfThis.isCallToName
		, Grab.funcAttribute(Grab.idAttribute(Then.appendTo(listIdentifiersCalledFunctions))))
	findIdentifiersToInline.visit(FunctionDefToInline)

	dictionary4Inlining: dict[str, ast.FunctionDef] = {}
	for identifier in sorted(set(listIdentifiersCalledFunctions).intersection(dictionaryFunctionDef.keys())):
		if NodeTourist(IfThis.matchesMeButNotAnyDescendant(IfThis.isCallIdentifier(identifier)), Then.extractIt).captureLastMatch(astModule) is not None:
			dictionary4Inlining[identifier] = dictionaryFunctionDef[identifier]

	keepGoing = True
	while keepGoing:
		keepGoing = False
		listIdentifiersCalledFunctions.clear()
		findIdentifiersToInline.visit(Make.Module(list(dictionary4Inlining.values())))

		listIdentifiersCalledFunctions = sorted((set(listIdentifiersCalledFunctions).difference(dictionary4Inlining.keys())).intersection(dictionaryFunctionDef.keys()))
		if len(listIdentifiersCalledFunctions) > 0:
			keepGoing = True
			for identifier in listIdentifiersCalledFunctions:
				if NodeTourist(IfThis.matchesMeButNotAnyDescendant(IfThis.isCallIdentifier(identifier)), Then.extractIt).captureLastMatch(astModule) is not None:
					FunctionDefTarget = dictionaryFunctionDef[identifier]
					if len(FunctionDefTarget.body) == 1:
						replacement = NodeTourist(Be.Return, Then.extractIt(DOT.value)).captureLastMatch(FunctionDefTarget)
						inliner = NodeChanger[ast.Call, ast.expr | None](
							findThis = IfThis.isCallIdentifier(identifier), doThat = Then.replaceWith(replacement))
						for astFunctionDef in dictionary4Inlining.values():
							inliner.visit(astFunctionDef)
					else:
						inliner = NodeChanger(Be.Assign.valueIs(IfThis.isCallIdentifier(identifier)), Then.replaceWith(FunctionDefTarget.body[0:-1]))
						for astFunctionDef in dictionary4Inlining.values():
							inliner.visit(astFunctionDef)

	for identifier, FunctionDefTarget in dictionary4Inlining.items():
		if len(FunctionDefTarget.body) == 1:
			replacement = NodeTourist(Be.Return, Then.extractIt(DOT.value)).captureLastMatch(FunctionDefTarget)
			inliner = NodeChanger(IfThis.isCallIdentifier(identifier), Then.replaceWith(replacement))
			inliner.visit(FunctionDefToInline)
		else:
			inliner = NodeChanger(Be.Assign.valueIs(IfThis.isCallIdentifier(identifier)), Then.replaceWith(FunctionDefTarget.body[0:-1]))
			inliner.visit(FunctionDefToInline)
	ast.fix_missing_locations(FunctionDefToInline)
	return FunctionDefToInline

def pythonCode2ast_expr(string: str) -> ast.expr:
	"""Convert a single Python expression `str` (***str***ing) to an `ast.expr` (***expr***ession) node.

	(AI generated docstring)

	You can use `pythonCode2ast_expr` to parse a `str` containing exactly one Python expression into
	an `ast.expr` node. `pythonCode2ast_expr` parses `string` using `ast.parse` [1], then extracts
	the value of the first `ast.Expr` (***Expr***ession) statement node. See `Make.expr` [2] for an
	approximate list of applicable `ast.expr` subclasses.

	Parameters
	----------
	string : str
		(***str***ing) A `str` containing exactly one Python expression. `string` must be a valid
		Python expression that `ast.parse` [1] can parse into a single `ast.Expr` statement node.

	Returns
	-------
	astExpression : ast.expr
		The `ast.expr` (***expr***ession) node extracted from `string`.

	Limitations
	-----------
	This prototype shortcut has approximately 482 implied constraints and pitfalls. If `string` does
	not produce a single `ast.Expr` statement, `pythonCode2ast_expr` will raise a `ValueError` via
	`raiseIfNone` [3]. When the shortcut does not behave as expected, using `ast.parse` [1] directly
	will provide more control.

	References
	----------
	[1] ast.parse - Python documentation
		https://docs.python.org/3/library/ast.html#ast.parse
	[2] astToolkit Make.expr - Context7
		https://context7.com/hunterhogan/asttoolkit
	[3] hunterMakesPy raiseIfNone - Context7
		https://context7.com/hunterhogan/huntermakespy
	"""
	return raiseIfNone(NodeTourist(Be.Expr, Then.extractIt(DOT.value)).captureLastMatch(ast.parse(string)))  # ty:ignore[invalid-return-type]

def removeUnusedParameters(FunctionDef: ast.FunctionDef) -> ast.FunctionDef:
	"""Remove unused `ast.arg` (***arg***ument) parameters from an `ast.FunctionDef` (Function ***Def***inition).

	(AI generated docstring)

	You can use `removeUnusedParameters` to strip `ast.arg` parameters from the `ast.arguments`
	(***arg***ument***s***) of an `ast.FunctionDef` when those parameters are not referenced anywhere
	in the `ast.FunctionDef.body`, or are only referenced within `ast.Return` statements.
	`removeUnusedParameters` examines `ast.arguments.args`, `ast.arguments.posonlyargs`
	(***pos***itional-only ***arg***ument***s***), and `ast.arguments.kwonlyargs` (***k***ey***w***ord-only
	***arg***ument***s***).

	After removing unused parameters, `removeUnusedParameters` replaces every `ast.Return` statement
	with a new `ast.Return` that returns a `ast.Tuple` of all remaining parameters, and updates the
	`ast.FunctionDef.returns` annotation to match.

	Parameters
	----------
	FunctionDef : ast.FunctionDef
		(Function ***Def***inition) The `ast.FunctionDef` `object` to process. `removeUnusedParameters`
		modifies `FunctionDef` in place and also returns `FunctionDef`.

	Returns
	-------
	FunctionDef : ast.FunctionDef
		The modified `ast.FunctionDef` (Function ***Def***inition) `object` with unused parameters
		and corresponding return elements and annotations removed.

	References
	----------
	[1] ast.FunctionDef - Python documentation
		https://docs.python.org/3/library/ast.html#ast.FunctionDef
	[2] ast.arguments - Python documentation
		https://docs.python.org/3/library/ast.html#ast.arguments
	[3] astToolkit - Context7
		https://context7.com/hunterhogan/asttoolkit
	"""
	list_argCuzMyBrainRefusesToThink = FunctionDef.args.args + FunctionDef.args.posonlyargs + FunctionDef.args.kwonlyargs
	list_arg_arg: list[str] = [ast_arg.arg for ast_arg in list_argCuzMyBrainRefusesToThink]
	listName: list[ast.Name] = []
	fauxFunctionDef = deepcopy(FunctionDef)
	NodeChanger(Be.Return, Then.removeIt).visit(fauxFunctionDef)
	NodeTourist(Be.Name, Then.appendTo(listName)).visit(fauxFunctionDef)
	listIdentifiers: list[str] = [astName.id for astName in listName]
	listIdentifiersNotUsed: list[str] = list(set(list_arg_arg) - set(listIdentifiers))
	for argIdentifier in listIdentifiersNotUsed:
		remove_arg = NodeChanger(IfThis.is_argIdentifier(argIdentifier), Then.removeIt)
		remove_arg.visit(FunctionDef)

	list_argCuzMyBrainRefusesToThink = FunctionDef.args.args + FunctionDef.args.posonlyargs + FunctionDef.args.kwonlyargs

	listName = [Make.Name(ast_arg.arg) for ast_arg in list_argCuzMyBrainRefusesToThink]
	replaceReturn = NodeChanger(Be.Return, Then.replaceWith(Make.Return(Make.Tuple(listName))))
	replaceReturn.visit(FunctionDef)

	list_annotation: list[ast.expr] = [ast_arg.annotation for ast_arg in list_argCuzMyBrainRefusesToThink if ast_arg.annotation is not None]
	FunctionDef.returns = Make.Subscript(Make.Name('tuple'), Make.Tuple(list_annotation))

	ast.fix_missing_locations(FunctionDef)

	return FunctionDef

def unjoinBinOP(astAST: ast.AST, operator: type[ast.operator] = ast.operator) -> list[ast.expr]:
	"""Decompose a nested `ast.BinOp` (***Bin***ary ***Op***eration) tree into a flat `list` of `ast.expr` (***expr***ession) nodes.

	(AI generated docstring)

	You can use `unjoinBinOP` to flatten a binary operation tree rooted at `astAST` (abstract syntax
	tree) into a `list` of `ast.expr` leaf nodes. `unjoinBinOP` traverses the tree collecting the
	right-hand operands of every matching `ast.BinOp` and accumulating all non-`ast.BinOp` nodes
	into the result.

	Parameters
	----------
	astAST : ast.AST
		(abstract syntax tree) The root `ast.AST` `object` to decompose. `astAST` is typically an
		`ast.BinOp` node, but `unjoinBinOP` accepts any `ast.AST` `object`.
	operator : type[ast.operator] = ast.operator
		(***op***erator) The `ast.operator` subclass to match when deciding whether to descend into
		an `ast.BinOp.op` (***op***erator). Defaults to `ast.operator`, which matches all binary
		operators.

	Returns
	-------
	list_ast_expr : list[ast.expr]
		A flat `list` of `ast.expr` (***expr***ession) nodes that were the operands of the matched
		`ast.BinOp` nodes.

	Algorithm Details
	-----------------
	`unjoinBinOP` uses a `workbench` to hold `ast.BinOp` nodes encountered as left-hand operands
	of outer `ast.BinOp` nodes. The traversal continues until `workbench` is empty, at which point
	all nested `ast.BinOp` nodes have been decomposed and their non-`ast.BinOp` operands have been
	collected into the result `list`.

	References
	----------
	[1] ast.BinOp - Python documentation
		https://docs.python.org/3/library/ast.html#ast.BinOp
	[2] ast.operator - Python documentation
		https://docs.python.org/3/library/ast.html#ast.operator
	[3] astToolkit - Context7
		https://context7.com/hunterhogan/asttoolkit
	"""
	list_ast_expr: list[ast.expr] = []
	workbench: list[ast.expr] = []

	findThis = Be.BinOp.opIs(lambda this_op: isinstance(this_op, operator))
	doThat = Grab.andDoAllOf([Grab.leftAttribute(Then.appendTo(workbench)), Grab.rightAttribute(Then.appendTo(list_ast_expr))])
	breakingBinOp = NodeTourist(findThis, doThat)

	breakingBinOp.visit(astAST)

	while workbench:
		ast_expr = workbench.pop()
		if isinstance(ast_expr, ast.BinOp):
			breakingBinOp.visit(ast_expr)
		else:
			list_ast_expr.append(ast_expr)

	return list_ast_expr

def unparseFindReplace[木: ast.AST, 文件: ast.AST, 文义](astTree: 木, mappingFindReplaceNodes: Mapping[文件, 文义]) -> 木:
	"""Replace `ast.AST` (Abstract Syntax Tree) nodes in `astTree` using a find-replace `Mapping`.

	(AI generated docstring)

	You can use `unparseFindReplace` to substitute nodes throughout an `ast.AST` tree by comparing
	unparsed text representations. `unparseFindReplace` iterates the replacement pass until the
	unparsed form of `astTree` no longer changes, ensuring all matching nodes are replaced
	regardless of nesting depth. `unparseFindReplace` does not modify `astTree` in place; it
	returns a modified deep copy of the same type.

	Parameters
	----------
	astTree : ast.AST
		(abstract syntax tree) The root `ast.AST` `object` whose nodes `unparseFindReplace` will
		replace. `astTree` is not modified in place.
	mappingFindReplaceNodes : Mapping[ast.AST, ast.AST]
		A `Mapping` from source `ast.AST` nodes to replacement `ast.AST` nodes. Each entry
		specifies one find-replace substitution.

	Returns
	-------
	newTree : ast.AST
		A deep copy of `astTree`, of the same concrete type as `astTree`, with all nodes matching
		keys in `mappingFindReplaceNodes` replaced by their corresponding values.

	Algorithm Details
	-----------------
	`unparseFindReplace` compares nodes by their unparsed text representation using `ast.unparse`
	[1]. The outer loop repeats until `ast.unparse(newTree) == ast.unparse(astTree)`, guaranteeing
	convergence but potentially requiring multiple passes for deeply nested or chained substitutions.
	This text-based approach does not rely on node identity or structural equality.

	References
	----------
	[1] ast.unparse - Python documentation
		https://docs.python.org/3/library/ast.html#ast.unparse
	[2] collections.abc.Mapping - Python documentation
		https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping
	[3] astToolkit IfThis.unparseIs - Context7
		https://context7.com/hunterhogan/asttoolkit
	"""
	keepGoing = True
	newTree = deepcopy(astTree)

	while keepGoing:
		for nodeFind, nodeReplace in mappingFindReplaceNodes.items():
			NodeChanger(IfThis.unparseIs(nodeFind), Then.replaceWith(nodeReplace)).visit(newTree)

		if ast.unparse(newTree) == ast.unparse(astTree):
			keepGoing = False
		else:
			astTree = deepcopy(newTree)
	return newTree

@overload
def write_astModule(astModule: ast.Module, pathFilename: PathLike[Any] | PurePath, settings: dict[str, dict[str, Any]] | None = None, identifierPackage: str='') -> Path: ...
@overload
def write_astModule(astModule: ast.Module, pathFilename: io.TextIOBase, settings: dict[str, dict[str, Any]] | None = None, identifierPackage: str='') ->  io.TextIOBase: ...
def write_astModule(astModule: ast.Module, pathFilename: PathLike[Any] | PurePath | io.TextIOBase, settings: dict[str, dict[str, Any]] | None = None, identifierPackage: str='') -> Path | io.TextIOBase:
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

class astParseParameters(TypedDict, total=False):
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

def extractClassDef(astAST: ast.AST, identifier: str) -> ast.ClassDef | None:
	"""Extract an `ast.ClassDef` (***Class*** ***Def***inition) from an `ast.AST` (Abstract Syntax Tree) `object` by name.

	(AI generated docstring)

	You can use `extractClassDef` to retrieve the first `ast.ClassDef` whose `ast.ClassDef.name`
	equals `identifier` from within `astAST`. `extractClassDef` returns `None` when no matching
	`ast.ClassDef` is found.

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The `ast.AST` `object` to search for `ast.ClassDef` nodes.
	identifier : str
		The name to match against `ast.ClassDef.name`.

	Returns
	-------
	astClassDef : ast.ClassDef | None
		The first `ast.ClassDef` (***Class*** ***Def***inition) `object` whose
		`ast.ClassDef.name == identifier`, or `None` if `extractClassDef` does not find a matching
		`ast.ClassDef`.

	References
	----------
	[1] ast.ClassDef - Python documentation
		https://docs.python.org/3/library/ast.html#ast.ClassDef
	[2] astToolkit - Context7
		https://context7.com/hunterhogan/asttoolkit
	"""
	return NodeTourist(IfThis.isClassDefIdentifier(identifier), Then.extractIt).captureLastMatch(astAST)

def extractFunctionDef(astAST: ast.AST, identifier: str) -> ast.FunctionDef | None:
	"""Extract an `ast.FunctionDef` (Function ***Def***inition) from an `ast.AST` (abstract syntax tree) `object` by name.

	(AI generated docstring)

	You can use `extractFunctionDef` to retrieve the first `ast.FunctionDef` whose
	`ast.FunctionDef.name` equals `identifier` from within `astAST`. `extractFunctionDef` returns
	`None` when no matching `ast.FunctionDef` is found.

	Parameters
	----------
	astAST : ast.AST
		(abstract syntax tree) The `ast.AST` `object` to search for `ast.FunctionDef` nodes.
	identifier : str
		The name to match against `ast.FunctionDef.name` (***id***entifier of the function).

	Returns
	-------
	astFunctionDef : ast.FunctionDef | None
		The first `ast.FunctionDef` (Function ***Def***inition) `object` whose
		`ast.FunctionDef.name == identifier`, or `None` if `extractFunctionDef` does not find a
		matching `ast.FunctionDef`.

	References
	----------
	[1] ast.FunctionDef - Python documentation
		https://docs.python.org/3/library/ast.html#ast.FunctionDef
	[2] astToolkit - Context7
		https://context7.com/hunterhogan/asttoolkit
	"""
	return NodeTourist(IfThis.isFunctionDefIdentifier(identifier), Then.extractIt).captureLastMatch(astAST)

def parseLogicalPath2astModule(logicalPath: identifierDotAttribute, package: str | None = None, **keywordArguments: Unpack[astParseParameters]) -> ast.Module:
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

def parsePathFilename2astModule(pathFilename: PathLike[Any] | PurePath, **keywordArguments: Unpack[astParseParameters]) -> ast.Module:
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

