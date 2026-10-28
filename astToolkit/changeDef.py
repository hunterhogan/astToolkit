"""Find, index, and transform Python function and class definitions.

(AI generated docstring)

You can extract a named definition or index definitions throughout an `ast.AST`
(Abstract Syntax Tree), including nested definitions and methods. Extraction and indexing
retain the original nodes. The transformations modify supplied function definitions in
place to substitute function logic or remove unused parameters and rewrite returns.

Contents
--------
Functions
	extractClassDef
		Extract the last class definition matching a name.
	extractFunctionDef
		Extract the last synchronous function definition matching a name.
	inlineFunctionDef
		Substitute local function logic at supported call sites.
	makeDictionaryAsyncFunctionDef
		Index asynchronous function definitions by name.
	makeDictionaryClassDef
		Index class definitions by name.
	makeDictionaryFunctionDef
		Index synchronous function definitions by name.
	makeDictionaryMosDef
		Combine asynchronous functions, classes, and synchronous functions in one index.
	removeUnusedParameters
		Remove unused named parameters and rewrite returns and their annotation.
"""

from __future__ import annotations

from astToolkit import Be, DOT, Grab, IfThis, Make, NodeChanger, NodeTourist, Then
from copy import deepcopy
import ast

def extractClassDef(astAST: ast.AST, identifier: str) -> ast.ClassDef | None:
	"""Extract a named class definition from an `ast.AST` (Abstract Syntax Tree).

	(AI generated docstring)

	You can retrieve the last `ast.ClassDef` (***Class*** ***Def***inition) whose
	`ast.ClassDef.name` equals `identifier`. The search includes nested definitions.

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The tree to search for `ast.ClassDef` nodes.
	identifier : str
		The name to match against `ast.ClassDef.name`.

	Returns
	-------
	astClassDef : ast.ClassDef | None
		The last matching `ast.ClassDef` (***Class*** ***Def***inition) in traversal order,
		or `None` when no match exists. The node belongs to `astAST` and is not copied.

	See Also
	--------
	`makeDictionaryClassDef`
		Index class definitions by name.
	`extractFunctionDef`
		Extract a synchronous function definition by name.
	"""
	return NodeTourist(IfThis.isClassDefIdentifier(identifier), Then.extractIt).captureLastMatch(astAST)

def extractFunctionDef(astAST: ast.AST, identifier: str) -> ast.FunctionDef | None:
	"""Extract a named function definition from an `ast.AST` (Abstract Syntax Tree).

	(AI generated docstring)

	You can retrieve the last `ast.FunctionDef` (Function ***Def***inition) whose
	`ast.FunctionDef.name` equals `identifier`. The search includes nested definitions and
	methods, and excludes `ast.AsyncFunctionDef` (***Async***hronous Function ***Def***inition).

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The tree to search for `ast.FunctionDef` nodes.
	identifier : str
		The name to match against `ast.FunctionDef.name` (***id***entifier of the function).

	Returns
	-------
	astFunctionDef : ast.FunctionDef | None
		The last matching `ast.FunctionDef` (Function ***Def***inition) in traversal order,
		or `None` when no match exists. The node belongs to `astAST` and is not copied.

	See Also
	--------
	`makeDictionaryFunctionDef`
		Index synchronous function definitions by name.
	`astToolkit.containers.astModuleToIngredientsFunction`
		Package an extracted function with its imports.
	"""
	return NodeTourist(IfThis.isFunctionDefIdentifier(identifier), Then.extractIt).captureLastMatch(astAST)

def inlineFunctionDef(identifierToInline: str, astModule: ast.Module) -> ast.FunctionDef:
	"""Substitute locally defined function logic into an `ast.FunctionDef`.

	(AI generated docstring)

	You can replace calls to synchronous functions defined in `astModule` with expressions or
	statements from those functions. The result is the selected `ast.FunctionDef` (Function
	***Def***inition), modified in place rather than a newly synthesized function.

	Calls must use an `ast.Name` (***id***entifier) as their `ast.Call.func`, with a name
	matching a definition in `astModule`. Calls through an `ast.Attribute` (***attr***ibute),
	such as `pathlib.Path`, are excluded.

	Parameters
	----------
	identifierToInline : str
		The name of the `ast.FunctionDef` to modify. When several definitions share the name,
		the last definition in traversal order is selected.
	astModule : ast.Module
		(abstract syntax tree Module) The module containing the function to modify and the
		synchronous function definitions available for substitution, including nested definitions.

	Returns
	-------
	FunctionDefToInline : ast.FunctionDef
		The selected `ast.FunctionDef` (Function ***Def***inition) from `astModule`, with
		supported call sites replaced.

	Raises
	------
	ValueError
		If no `ast.FunctionDef.name` in `astModule` matches `identifierToInline`.

	See Also
	--------
	`extractFunctionDef`
		Retrieve a function without changing its body.
	`makeDictionaryFunctionDef`
		Inspect the function definitions available by name.

	Supported Substitutions
	-----------------------
	A function with a one-statement body supplies the expression from its last `ast.Return`.
	Such a body must contain a return expression suitable for the call site.

	A function with a longer body supplies every statement except its final statement.
	Only an `ast.Assign` whose entire `value` is the matching call is replaced in this case.
	The assignment itself is discarded, including its targets.

	Call arguments are not bound to parameters, and local names are not renamed to avoid
	collisions. The supplied functions must already use compatible names and statement
	structures. Name matching does not resolve Python scopes. Recursive call graphs are
	unsupported; the dependency search does not guarantee termination.

	Input Mutation
	--------------
	The selected function and other function definitions in `astModule` can be changed.
	Inserted expressions and statements are shared with their source definitions.
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

def makeDictionaryAsyncFunctionDef(astAST: ast.AST) -> dict[str, ast.AsyncFunctionDef]:
	"""Index asynchronous function definitions by name.

	(AI generated docstring)

	You can collect `async def` (***async***hronous ***def***inition) nodes throughout an
	`ast.AST` (Abstract Syntax Tree) in a `dict` (***dict***ionary). The search includes
	methods and nested definitions without distinguishing their Python scopes.

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The tree to search for `ast.AsyncFunctionDef`
		(***Async***hronous Function ***Def***inition) nodes.

	Returns
	-------
	dictionaryIdentifier2AsyncFunctionDef : dict[str, ast.AsyncFunctionDef]
		Each `ast.AsyncFunctionDef.name` mapped to its original node. The last definition
		in traversal order wins when names repeat. The nodes are not copied.

	See Also
	--------
	`makeDictionaryFunctionDef`
		Index synchronous function definitions.
	`makeDictionaryMosDef`
		Combine asynchronous functions, classes, and synchronous functions in one index.
	"""
	dictionaryIdentifier2AsyncFunctionDef: dict[str, ast.AsyncFunctionDef] = {}
	NodeTourist(Be.AsyncFunctionDef, Then.updateKeyValueIn(DOT.name, Then.extractIt, dictionaryIdentifier2AsyncFunctionDef)).visit(astAST)
	return dictionaryIdentifier2AsyncFunctionDef

def makeDictionaryClassDef(astAST: ast.AST) -> dict[str, ast.ClassDef]:
	"""Index class definitions by name.

	(AI generated docstring)

	You can collect `class` definitions throughout an `ast.AST` (Abstract Syntax Tree) in
	a `dict` (***dict***ionary). The search includes nested classes without distinguishing
	their Python scopes.

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The tree to search for `ast.ClassDef`
		(***Class*** ***Def***inition) nodes.

	Returns
	-------
	dictionaryIdentifier2ClassDef : dict[str, ast.ClassDef]
		Each `ast.ClassDef.name` mapped to its original node. The last definition in
		traversal order wins when names repeat. The nodes are not copied.

	See Also
	--------
	`extractClassDef`
		Retrieve a single class definition by name.
	`makeDictionaryMosDef`
		Combine classes and function definitions in one index.
	"""
	dictionaryIdentifier2ClassDef: dict[str, ast.ClassDef] = {}
	NodeTourist(Be.ClassDef, Then.updateKeyValueIn(DOT.name, Then.extractIt, dictionaryIdentifier2ClassDef)).visit(astAST)
	return dictionaryIdentifier2ClassDef

def makeDictionaryFunctionDef(astAST: ast.AST) -> dict[str, ast.FunctionDef]:
	"""Index synchronous function definitions by name.

	(AI generated docstring)

	You can collect `def` (***def***inition) nodes throughout an `ast.AST` (Abstract Syntax
	Tree) in a `dict` (***dict***ionary). The search includes methods and nested definitions
	without distinguishing their Python scopes.

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The tree to search for `ast.FunctionDef`
		(Function ***Def***inition) nodes.

	Returns
	-------
	dictionaryIdentifier2FunctionDef : dict[str, ast.FunctionDef]
		Each `ast.FunctionDef.name` mapped to its original node. The last definition in
		traversal order wins when names repeat. The nodes are not copied.

	See Also
	--------
	`extractFunctionDef`
		Retrieve a single synchronous function definition by name.
	`makeDictionaryAsyncFunctionDef`
		Index asynchronous function definitions.
	`makeDictionaryMosDef`
		Combine function definitions and classes in one index.
	"""
	dictionaryIdentifier2FunctionDef: dict[str, ast.FunctionDef] = {}
	NodeTourist(Be.FunctionDef, Then.updateKeyValueIn(DOT.name, Then.extractIt, dictionaryIdentifier2FunctionDef)).visit(astAST)
	return dictionaryIdentifier2FunctionDef

def makeDictionaryMosDef(astAST: ast.AST) -> dict[str, ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef]:
	"""Index asynchronous functions, classes, and synchronous functions by name.

	(AI generated docstring)

	You can collect `ast.AsyncFunctionDef` (***Async***hronous Function ***Def***inition),
	`ast.ClassDef` (***Class*** ***Def***inition), and `ast.FunctionDef` (Function ***Def***inition)
	nodes throughout an `ast.AST` (Abstract Syntax Tree) in one `dict` (***dict***ionary).

	Parameters
	----------
	astAST : ast.AST
		(Abstract Syntax Tree) The tree to search, including nested definitions and methods.

	Returns
	-------
	dictionaryIdentifier2MosDef : dict[str, ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef]
		Each definition name mapped to its original node, without Python scope distinctions.
		Within each node type, the last definition in traversal order wins. For names shared
		by different node types, `ast.FunctionDef` takes precedence over `ast.ClassDef`,
		which takes precedence over `ast.AsyncFunctionDef`. The nodes are not copied.

	See Also
	--------
	`makeDictionaryAsyncFunctionDef`
		Collect only asynchronous function definitions.
	`makeDictionaryClassDef`
		Collect only class definitions.
	`makeDictionaryFunctionDef`
		Collect only synchronous function definitions.
	"""
	dictionaryIdentifier2MosDef: dict[str, ast.AsyncFunctionDef | ast.ClassDef | ast.FunctionDef] = {}
	dictionaryIdentifier2MosDef.update(makeDictionaryAsyncFunctionDef(astAST))
	dictionaryIdentifier2MosDef.update(makeDictionaryClassDef(astAST))
	dictionaryIdentifier2MosDef.update(makeDictionaryFunctionDef(astAST))
	return dictionaryIdentifier2MosDef

def removeUnusedParameters(FunctionDef: ast.FunctionDef) -> ast.FunctionDef:
	"""Remove unused `ast.arg` (***arg***ument) parameters and rewrite function returns.

	(AI generated docstring)

	You can remove named parameters that have no matching `ast.Name` (***id***entifier)
	outside `ast.Return` statements, then make every return yield a tuple of the remaining
	named parameters.

	The named parameters come from `ast.arguments` (***arg***ument***s***) fields
	`args` (***arg***ument***s***), `posonlyargs` (***pos***itional-only ***arg***ument***s***),
	and `kwonlyargs` (***k***ey***w***ord-only ***arg***ument***s***). Variadic parameters
	`*args` and `**kwargs` are excluded from the removal candidates and the returned tuple.

	Parameters
	----------
	FunctionDef : ast.FunctionDef
		(Function ***Def***inition) The function to modify in place.

	Returns
	-------
	FunctionDef : ast.FunctionDef
		The supplied `ast.FunctionDef` (Function ***Def***inition), with unused named parameters
		removed, existing returns replaced, and its return annotation rewritten.

	See Also
	--------
	`astToolkit.containers.IngredientsFunction`
		Manage a function definition and its imports, including parameter removal.

	Parameter Use
	-------------
	Any matching `ast.Name` outside an `ast.Return` subtree counts as use, including names
	in annotations, defaults, decorators, assignment targets, and nested definitions.
	Names are compared as text without resolving Python scopes.

	Input Mutation
	--------------
	Parameter removal and return replacement also reach nested definitions. Default-value
	lists are not realigned after parameters are removed.

	Every existing `ast.Return` becomes a return of an `ast.Tuple` containing the remaining
	named parameters in `args`, `posonlyargs`, then `kwonlyargs` order. No return is added
	where none exists. The function's return annotation becomes `tuple[...]` using only the
	remaining parameter annotations that are present, so unannotated parameters have no
	corresponding annotation entry.
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
