"""
AST Transformation Tools for Code Optimization and Generation

This module provides higher-level transformation tools that operate on AST structures to perform
complex code optimizations and transformations. The module includes five key functions:

1. makeDictionaryFunctionDef: Creates a lookup dictionary mapping function names to their AST definitions
   within a module, enabling efficient access to specific function definitions.

2. inlineFunctionDef: Performs function inlining by recursively substituting function calls with their
   implementation bodies, creating self-contained functions without external dependencies.

3. removeUnusedParameters: Optimizes function signatures by analyzing and removing unused parameters,
   updating the function signature, return statements, and type annotations accordingly.

4. unparseFindReplace: Recursively replaces AST nodes throughout a tree structure using textual
   representation matching, providing a brute-force but effective approach for complex replacements.

5. write_astModule: Converts an IngredientsModule to optimized Python source code and writes it to a file,
   handling import organization and code formatting in the process.

These transformation tools form the backbone of the code optimization pipeline, enabling sophisticated
code transformations while maintaining semantic integrity and performance characteristics.
"""

from astToolkit import (
	Be, ClassIsAndAttribute, DOT, Grab, IfThis, IngredientsFunction, IngredientsModule, Make,
	NodeChanger, NodeTourist, Then, 个, 木,
)
from autoflake import fix_code as autoflake_fix_code
from collections.abc import Callable, Mapping, Sequence
from copy import deepcopy
from os import PathLike
from pathlib import PurePath
from typing import Any, cast
from Z0Z_tools import raiseIfNone, writeStringToHere
import ast

# TODO Some `DOT` methods return lists, notably DOT.targets, which is an attribute of ast.Assign.
# But, none or almost none of the other functions and methods accept a list as input.
# This is most obviously a problem in `ClassIsAndAttribute.targetsIs` because the user needs to pass
# a function that can take list[ast.expr] as a parameter.
# I don't know if the following works, but it is interesting.
# ClassIsAndAttribute.targetsIs(ast.Assign, lambda list_expr: any([IfThis.isSubscriptIdentifier('foldGroups')(node) for node in list_expr]))

class cleverNamePrototype:
    @staticmethod
    def index(at: int) -> Callable[[Sequence[个]], 个]:
        def workhorse(zzz: Sequence[个]) -> 个:
            node = zzz[at]
			# slice?
            return node
        return workhorse

def makeDictionaryFunctionDef(module: ast.Module) -> dict[str, ast.FunctionDef]:
	"""
	Create a dictionary mapping function names to their AST definitions.

	This function creates a dictionary that maps function names to their AST function
	definition nodes for all functions defined in the given module.

	Parameters:
		module: The AST module to extract function definitions from.

	Returns:
		A dictionary mapping function identifiers to their AST function definition nodes.
	"""
	dictionaryIdentifier2FunctionDef: dict[str, ast.FunctionDef] = {}
	NodeTourist(Be.FunctionDef, Then.updateKeyValueIn(DOT.name, Then.extractIt, dictionaryIdentifier2FunctionDef)).visit(module)
	return dictionaryIdentifier2FunctionDef

def inlineFunctionDef(identifierToInline: str, module: ast.Module) -> ast.FunctionDef:
	"""
	Inline function calls within a function definition to create a self-contained function.

	This function takes a function identifier and a module, finds the function definition,
	and then recursively inlines all function calls within that function with their
	implementation bodies. This produces a fully inlined function that doesn't depend
	on other function definitions from the module.

	Parameters:
		identifierToInline: The name of the function to inline.
		module: The AST module containing the function and its dependencies.

	Returns:
		A modified function definition with all function calls inlined.

	Raises:
		ValueError: If the function to inline is not found in the module.
	"""
	dictionaryFunctionDef: dict[str, ast.FunctionDef] = makeDictionaryFunctionDef(module)
	try:
		FunctionDefToInline = dictionaryFunctionDef[identifierToInline]
	except KeyError as ERRORmessage:
		raise ValueError(f"FunctionDefToInline not found in dictionaryIdentifier2FunctionDef: {identifierToInline = }") from ERRORmessage

	listIdentifiersCalledFunctions: list[str] = []
	findIdentifiersToInline = NodeTourist(findThis = IfThis.isCallToName
							, doThat = Grab.funcAttribute(cast(Callable[[ast.expr], ast.expr], Grab.idAttribute(cast(Callable[[str], str], Then.appendTo(listIdentifiersCalledFunctions))))))
	findIdentifiersToInline.visit(FunctionDefToInline)

	dictionary4Inlining: dict[str, ast.FunctionDef] = {}
	for identifier in sorted(set(listIdentifiersCalledFunctions).intersection(dictionaryFunctionDef.keys())):
		if NodeTourist(IfThis.matchesMeButNotAnyDescendant(IfThis.isCallIdentifier(identifier)), Then.extractIt).captureLastMatch(module) is not None:
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
				if NodeTourist(IfThis.matchesMeButNotAnyDescendant(IfThis.isCallIdentifier(identifier)), Then.extractIt).captureLastMatch(module) is not None:
					FunctionDefTarget = dictionaryFunctionDef[identifier]
					if len(FunctionDefTarget.body) == 1:
						replacement = NodeTourist(Be.Return, Then.extractIt(DOT.value)).captureLastMatch(FunctionDefTarget)

						findThis = IfThis.isCallIdentifier(identifier)
						doThat = Then.replaceWith(replacement)
						inliner = NodeChanger(findThis, doThat)
						for astFunctionDef in dictionary4Inlining.values():
							inliner.visit(astFunctionDef)
					else:
						inliner = NodeChanger(ClassIsAndAttribute.valueIs(ast.Assign, IfThis.isCallIdentifier(identifier)),Then.replaceWith(FunctionDefTarget.body[0:-1]))
						for astFunctionDef in dictionary4Inlining.values():
							inliner.visit(astFunctionDef)

	for identifier, FunctionDefTarget in dictionary4Inlining.items():
		if len(FunctionDefTarget.body) == 1:
			replacement = NodeTourist(Be.Return, Then.extractIt(DOT.value)).captureLastMatch(FunctionDefTarget)
			inliner = NodeChanger(IfThis.isCallIdentifier(identifier), Then.replaceWith(replacement))
			inliner.visit(FunctionDefToInline)
		else:
			inliner = NodeChanger(ClassIsAndAttribute.valueIs(ast.Assign, IfThis.isCallIdentifier(identifier)),Then.replaceWith(FunctionDefTarget.body[0:-1]))
			inliner.visit(FunctionDefToInline)
	ast.fix_missing_locations(FunctionDefToInline)
	return FunctionDefToInline

def removeUnusedParameters(ingredientsFunction: IngredientsFunction) -> IngredientsFunction:
	"""
	Removes unused parameters from a function's AST definition, return statement, and annotation.

	This function analyzes the Abstract Syntax Tree (AST) of a given function and removes
	any parameters that are not referenced within the function body. It updates the
	function signature, the return statement (if it's a tuple containing unused variables),
	and the return type annotation accordingly.

	Parameters
	----------
	ingredientsFunction : IngredientsFunction
		An object containing the AST representation of a function to be processed.

	Returns
	-------
	IngredientsFunction
		The modified IngredientsFunction object with unused parameters and corresponding
		return elements/annotations removed from its AST.

	The modification is done in-place on the original AST nodes within the IngredientsFunction object.
	"""
	list_argCuzMyBrainRefusesToThink = ingredientsFunction.astFunctionDef.args.args + ingredientsFunction.astFunctionDef.args.posonlyargs + ingredientsFunction.astFunctionDef.args.kwonlyargs
	list_arg_arg: list[str] = [ast_arg.arg for ast_arg in list_argCuzMyBrainRefusesToThink]
	listName: list[ast.Name] = []
	fauxFunctionDef = deepcopy(ingredientsFunction.astFunctionDef)
	NodeChanger(Be.Return, Then.removeIt).visit(fauxFunctionDef)
	NodeTourist(Be.Name, Then.appendTo(listName)).visit(fauxFunctionDef)
	listIdentifiers: list[str] = [astName.id for astName in listName]
	listIdentifiersNotUsed: list[str] = list(set(list_arg_arg) - set(listIdentifiers))
	for argIdentifier in listIdentifiersNotUsed:
		remove_arg = NodeChanger(IfThis.is_argIdentifier(argIdentifier), Then.removeIt)
		remove_arg.visit(ingredientsFunction.astFunctionDef)

	list_argCuzMyBrainRefusesToThink = ingredientsFunction.astFunctionDef.args.args + ingredientsFunction.astFunctionDef.args.posonlyargs + ingredientsFunction.astFunctionDef.args.kwonlyargs

	listName = [Make.Name(ast_arg.arg) for ast_arg in list_argCuzMyBrainRefusesToThink]
	replaceReturn = NodeChanger(Be.Return, Then.replaceWith(Make.Return(Make.Tuple(listName))))
	replaceReturn.visit(ingredientsFunction.astFunctionDef)

	list_annotation: list[ast.expr] = [ast_arg.annotation for ast_arg in list_argCuzMyBrainRefusesToThink if ast_arg.annotation is not None]
	ingredientsFunction.astFunctionDef.returns = Make.Subscript(Make.Name('tuple'), Make.Tuple(list_annotation))

	ast.fix_missing_locations(ingredientsFunction.astFunctionDef)

	return ingredientsFunction

def unparseFindReplace(astTree: 木, mappingFindReplaceNodes: Mapping[ast.AST, ast.AST]) -> 木:
	"""
	Recursively replace AST nodes based on a mapping of find-replace pairs.

	This function applies brute-force node replacement throughout an AST tree
	by comparing textual representations of nodes. While not the most semantic
	approach, it provides a reliable way to replace complex nested structures
	when more precise targeting methods are difficult to implement.

	The function continues replacing nodes until no more changes are detected
	in the AST's textual representation, ensuring complete replacement throughout
	the tree structure.

	Parameters:
		astTree: The AST structure to modify.
		mappingFindReplaceNodes: A mapping from source nodes to replacement nodes.

	Returns:
		newTree: The modified AST structure with all matching nodes replaced.
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

# @overload
# def write_astModule(astModule: ast.AST, pathFilename: PathLike[Any] | PurePath, packageName: str | None = None) -> None:...
# @overload
# def write_astModule(ingredients: IngredientsModule, pathFilename: PathLike[Any] | PurePath, packageName: str | None = None) -> None:...
def write_astModule(ingredients: IngredientsModule, pathFilename: PathLike[Any] | PurePath, packageName: str | None = None) -> None:
	"""
	Convert an IngredientsModule to Python source code and write it to a file.

	This function renders an IngredientsModule into executable Python code,
	applies code quality improvements like import organization via autoflake,
	and writes the result to the specified file path.

	The function performs several key steps:
	1. Converts the AST module structure to a valid Python AST
	2. Fixes location attributes in the AST for proper formatting
	3. Converts the AST to Python source code
	4. Optimizes imports using autoflake
	5. Writes the final source code to the specified file location

	This is typically the final step in the code generation assembly line,
	producing optimized Python modules ready for execution.

	Parameters:
		ingredients: The IngredientsModule containing the module definition.
		pathFilename: The file path where the module should be written.
		packageName: Optional package name to preserve in import optimization.

	Raises:
		FREAKOUT: If the generated source code is empty.
	"""
	# if ingredients:
	# 	astModule = Make.Module(ingredients.body, ingredients.type_ignores)
	astModule = Make.Module(ingredients.body, ingredients.type_ignores)
	ast.fix_missing_locations(astModule)
	pythonSource: str = raiseIfNone(ast.unparse(astModule))
	autoflake_additional_imports: list[str] = ingredients.imports.exportListModuleIdentifiers()
	if packageName:
		autoflake_additional_imports.append(packageName)
	pythonSource = autoflake_fix_code(pythonSource, autoflake_additional_imports, expand_star_imports=False, remove_all_unused_imports=True, remove_duplicate_keys = False, remove_unused_variables = False)
	writeStringToHere(pythonSource, pathFilename)
