from __future__ import annotations

from astToolkit import Be, DOT, Grab, IfThis, Make, NodeChanger, NodeTourist, Then
from copy import deepcopy
import ast

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
	NodeTourist(Be.AsyncFunctionDef, Then.updateKeyValueIn(DOT.name, Then.extractIt, dictionaryIdentifier2AsyncFunctionDef)).visit(astAST)
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
	NodeTourist(Be.ClassDef, Then.updateKeyValueIn(DOT.name, Then.extractIt, dictionaryIdentifier2ClassDef)).visit(astAST)
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
	NodeTourist(Be.FunctionDef, Then.updateKeyValueIn(DOT.name, Then.extractIt, dictionaryIdentifier2FunctionDef)).visit(astAST)
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

	Recursive Functions
	-------------------
	Direct recursion
		If an `ast.FunctionDef` calls itself, it is not inlined.

	Mutual recursion
		If any function transitively reachable from `identifierToInline` calls back to
		`identifierToInline`, it is not inlined.

	Raises
	------
	ValueError
		If `identifierToInline` does not match any `ast.FunctionDef.name` in `astModule`.

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
	except KeyError as 拦message:
		message: str = f"I was unable to find an `ast.FunctionDef` with name {identifierToInline = } in {astModule = }."
		raise ValueError(message) from 拦message

	listIdentifiersCalledFunctions: list[str] = []
	findIdentifiersToInline = NodeTourist[ast.Call, ast.Call](IfThis.isCallToName
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
						replacement = NodeTourist[ast.AST, ast.expr](Be.Return, Then.extractIt(DOT.value)).captureLastMatch(FunctionDefTarget)
						inliner = NodeChanger(
							findThis=IfThis.isCallIdentifier(identifier), doThat=Then.replaceWith(replacement))
						for astFunctionDef in dictionary4Inlining.values():
							inliner.visit(astFunctionDef)
					else:
						inliner = NodeChanger(Be.Assign.valueIs(IfThis.isCallIdentifier(identifier)), Then.replaceWith(FunctionDefTarget.body[0:-1]))
						for astFunctionDef in dictionary4Inlining.values():
							inliner.visit(astFunctionDef)

	for identifier, FunctionDefTarget in dictionary4Inlining.items():
		if len(FunctionDefTarget.body) == 1:
			replacement = NodeTourist[ast.AST, ast.expr](Be.Return, Then.extractIt(DOT.value)).captureLastMatch(FunctionDefTarget)
			inliner = NodeChanger(IfThis.isCallIdentifier(identifier), Then.replaceWith(replacement))
			inliner.visit(FunctionDefToInline)
		else:
			inliner = NodeChanger(Be.Assign.valueIs(IfThis.isCallIdentifier(identifier)), Then.replaceWith(FunctionDefTarget.body[0:-1]))
			inliner.visit(FunctionDefToInline)
	ast.fix_missing_locations(FunctionDefToInline)
	return FunctionDefToInline

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
