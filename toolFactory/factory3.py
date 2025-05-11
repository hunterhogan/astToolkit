from collections import defaultdict
from itertools import chain
from pathlib import PurePosixPath
from toolFactory import (
	astName_overload,
	format_hasDOTIdentifier,
	astName_staticmethod,
	astName_typing_TypeAlias,
	formatTypeAliasSubcategory,
	fileExtension,
	getElementsBe,
	getElementsDOT,
	getElementsGrab,
	getElementsMake,
	getElementsTypeAlias,
	keywordArgumentsIdentifier,
	pathPackage,
	pythonVersionMinorMinimum,
	)
from toolFactory.Z0Z_hardcoded import listPylanceErrors
from toolFactory.factory_annex import (
	FunctionDefGrab_andDoAllOf,
	FunctionDefMake_Attribute,
	FunctionDefMake_Import,
	listHandmadeTypeAlias_astTypes,
)
from toolFactory.docstrings import ClassDefDocstringBe, ClassDefDocstringGrab, ClassDefDocstringMake, docstringWarning, ClassDefDocstringDOT
from typing import cast
from Z0Z_tools import writeStringToHere
import ast
# NOTE you need these because of `eval()`
from ast import Name, Store

"""
class Name(expr):
...
	ctx: expr_context  # Not present in Python < 3.13 if not passed to `__init__`

TODO protect against AttributeError (I guess) in DOT, Grab, and ClassIsAndAttribute
	add docstrings to warn of problem, including in Make

"""
def writeModule(astModule: ast.Module, moduleIdentifier: str) -> None:
	ast.fix_missing_locations(astModule)
	pythonSource: str = ast.unparse(astModule)
	if 'ClassIsAndAttribute' in moduleIdentifier or 'DOT' in moduleIdentifier or 'Grab' in moduleIdentifier:
		pythonSource = "# ruff: noqa: F403, F405\n" + pythonSource
	# if 'ClassIsAndAttribute' in moduleIdentifier:
	# 	listTypeIgnore: list[ast.TypeIgnore] = []
	# 	tag = '[reportInconsistentOverload]'
	# 	for attribute in listPylanceErrors:
	# 		lineno = 0
	# 		for splitlinesNumber, line in enumerate(pythonSource.splitlines()):
	# 			# Cycle through the overloads and definitions: effectively keeping the last one, which is the definition.
	# 			if f"def {attribute}Is" in line:
	# 				lineno = splitlinesNumber + 1
	# 		listTypeIgnore.append(ast.TypeIgnore(lineno, tag))
	# 	astModule = ast.parse(pythonSource)
	# 	astModule.type_ignores.extend(listTypeIgnore)
	# 	pythonSource = ast.unparse(astModule)
	# 	pythonSource = "# ruff: noqa: F403, F405\n" + pythonSource
	if 'Grab' in moduleIdentifier:
		listTypeIgnore: list[ast.TypeIgnore] = []
		tag = '[reportArgumentType, reportAttributeAccessIssue]'
		for attribute in listPylanceErrors:
			for splitlinesNumber, line in enumerate(pythonSource.splitlines()):
				if 'node.'+attribute in line:
					listTypeIgnore.append(ast.TypeIgnore(splitlinesNumber+1, tag))
					break
		astModule = ast.parse(pythonSource)
		astModule.type_ignores.extend(listTypeIgnore)
		pythonSource = ast.unparse(astModule)
		pythonSource = "# ruff: noqa: F403, F405\n" + pythonSource
		pythonSource = pythonSource.replace('# type: ignore[', '# pyright: ignore[')
	pathFilenameModule = PurePosixPath(pathPackage, moduleIdentifier + fileExtension)
	writeStringToHere(pythonSource, pathFilenameModule)

def writeClass(classIdentifier: str, list4ClassDefBody: list[ast.stmt], list4ModuleBody: list[ast.stmt], moduleIdentifierPrefix: str | None = '_tool') -> None:
	if moduleIdentifierPrefix:
		moduleIdentifier = moduleIdentifierPrefix + classIdentifier
	else:
		moduleIdentifier = classIdentifier
	return writeModule(ast.Module(
			body=[docstringWarning
				, *list4ModuleBody
				, ast.ClassDef(name=classIdentifier, bases=[], keywords=[], body=list4ClassDefBody, decorator_list=[])
				]
			, type_ignores=[]
			)
		, moduleIdentifier)

def makeToolBe():
	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringBe]

	listDictionaryToolElements = getElementsBe()

	for dictionaryToolElements in listDictionaryToolElements:
		ClassDefIdentifier = cast(str, dictionaryToolElements['ClassDefIdentifier'])
		classAs_astAttribute = cast(ast.Attribute, eval(dictionaryToolElements['classAs_astAttribute']))
		classVersionMinorMinimum: int = dictionaryToolElements['classVersionMinorMinimum']

		ast_stmt = ast.FunctionDef(
			name=ClassDefIdentifier
			, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='node', annotation=ast.Name('ast.AST'))], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
			, body=[ast.Return(value=ast.Call(func=ast.Name('isinstance'), args=[ast.Name('node'), classAs_astAttribute], keywords=[]))]
			, decorator_list=[astName_staticmethod]
			, returns=ast.Subscript(value=ast.Name('TypeGuard'), slice=classAs_astAttribute))

		if classVersionMinorMinimum > pythonVersionMinorMinimum:
			ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info'),
				ops=[ast.GtE()],
				comparators=[ast.Tuple([ast.Constant(3),
							ast.Constant(classVersionMinorMinimum)])]),
				body=[ast_stmt])

		list4ClassDefBody.append(ast_stmt)

	list4ModuleBody: list[ast.stmt] = [
		ast.ImportFrom('typing', [ast.alias('TypeGuard')], 0)
		, ast.Import([ast.alias('ast')])
		, ast.Import([ast.alias('sys')])
	]

	writeClass('Be', list4ClassDefBody, list4ModuleBody)

def makeToolDOT():
	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringDOT]

	dictionaryToolElements: dict[str, dict[str, dict[str, int | str]]] = getElementsDOT()

	# Process each attribute group to generate overloaded methods and implementations
	for attribute, attributeDictionary in dictionaryToolElements.items():
		# print(attribute)
		listElementsHARDCODED = ['attribute', 'TypeAliasSubcategory', 'attributeVersionMinorMinimum', 'ast_exprType']
		for TypeAliasSubcategory, Z0Z_tired in attributeDictionary.items():
			# print('\t', TypeAliasSubcategory)
			ast_exprType = cast(ast.Attribute, eval(Z0Z_tired['ast_exprType'])) # pyright: ignore[reportArgumentType]
			# print('\t\t', ast_exprType)
			attributeVersionMinorMinimum: int = Z0Z_tired['attributeVersionMinorMinimum'] # pyright: ignore[reportAssignmentType]
			# print('\t\t', attributeVersionMinorMinimum)
			# continue

			ast_stmt = ast.FunctionDef(
				name=attribute,
				args=ast.arguments(
					posonlyargs=[],
					args=[ast.arg('node', ast.Name('hasDOT' + attribute))],
					vararg=None,
					kwonlyargs=[],
					kw_defaults=[],
					kwarg=None,
					defaults=[]
				),
				body=[ast.Expr(ast.Constant(value=...))],
				decorator_list=[astName_staticmethod, astName_overload],
				returns=ast_exprType
			)

			if attributeVersionMinorMinimum > pythonVersionMinorMinimum:
				ast_stmt = ast.If(test=ast.Compare(
					left=ast.Attribute(ast.Name('sys'), 'version_info'),
					ops=[ast.GtE()],
					comparators=[ast.Tuple(
						elts=[ast.Constant(3), ast.Constant(attributeVersionMinorMinimum)],
						ctx=ast.Load()
					)]
				),
				body=[ast_stmt],
				orelse=[])

			list4ClassDefBody.append(ast_stmt)

	list4ModuleBody: list[ast.stmt] = [docstringWarning
			, ast.ImportFrom(module='astToolkit', names=[ast.alias(name='ast_Identifier'), ast.alias(name='ast_expr_Slice'), ast.alias(name='astDOTtype_param')], level=0)
			, ast.ImportFrom(module='astToolkit._astTypes', names=[ast.alias(name='*')], level=0)
			, ast.ImportFrom(module='collections.abc', names=[ast.alias(name='Sequence')], level=0)
			, ast.ImportFrom(module='typing', names=[ast.alias(name='Any'), ast.alias(name='Literal'), ast.alias(name='overload')], level=0)
			, ast.Import(names=[ast.alias(name='ast')])
			, ast.Import(names=[ast.alias(name='sys')])
			]

	writeClass('DOT', list4ClassDefBody, list4ModuleBody)

def makeToolGrab():
	def create_ast_stmt():
		ast_stmt = None
		for attributeVersionMinorMinimum, list_ast_exprType in dictionaryAttribute.items():
			list_ast_expr4annotation = []
			for ast_exprTypeAsStr in list_ast_exprType:
				ast_exprType = eval(ast_exprTypeAsStr)
				list_ast_expr4annotation.append(ast.Subscript(ast.Name('Callable'), slice=ast.Tuple([ast.List([ast_exprType]), ast_exprType])))

			ast_expr4annotation = ast.BitOr.join(list_ast_expr4annotation) # pyright: ignore[reportAttributeAccessIssue]

			ast_stmt = ast.FunctionDef(attribute + 'Attribute'
				, args=ast.arguments(posonlyargs=[], args=[ast.arg('action', annotation=ast_expr4annotation)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
				, body=[ast.FunctionDef('workhorse'
						, args=ast.arguments(args=[ast.arg('node', hasDOTTypeAliasName_Load)])
						, body=[ast.Assign([ast.Attribute(ast.Name('node'), attribute, ast.Store())], value=ast.Call(ast.Name('action'), [ast.Attribute(ast.Name('node'), attribute)])), ast.Return(ast.Name('node'))]
						, returns=hasDOTTypeAliasName_Load), ast.Return(ast.Name('workhorse'))]
				, decorator_list=[astName_staticmethod]
				, returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([hasDOTTypeAliasName_Load]), hasDOTTypeAliasName_Load])))

			if attributeVersionMinorMinimum > pythonVersionMinorMinimum:
				ast_stmt = ast.If(test=ast.Compare(
					left=ast.Attribute(ast.Name('sys'), 'version_info'),
					ops=[ast.GtE()],
					comparators=[ast.Tuple(
						elts=[ast.Constant(3), ast.Constant(attributeVersionMinorMinimum)],
						ctx=ast.Load()
					)]
				),
				body=[ast_stmt],
				orelse=ast_stmtAtPythonMinimum if ast_stmtAtPythonMinimum is not None else [])
		assert ast_stmt is not None
		return ast_stmt

	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringGrab, FunctionDefGrab_andDoAllOf]
	dictionaryToolElements: dict[str, dict[int, list[str]]] = getElementsGrab()

	for attribute, dictionaryAttribute in dictionaryToolElements.items():
		hasDOTIdentifier: str = format_hasDOTIdentifier.format(attribute=attribute)
		hasDOTTypeAliasName_Load: ast.Name = ast.Name(hasDOTIdentifier)
		ast_stmtAtPythonMinimum = None

		if len(dictionaryAttribute) > 1:
			abovePythonMinimum: dict[int, list[str]] = {max(dictionaryAttribute.keys()) : sorted(chain(*dictionaryAttribute.values()), key=str.lower)}
			del dictionaryAttribute[max(dictionaryAttribute.keys())]
			ast_stmtAtPythonMinimum = [create_ast_stmt()]
			dictionaryAttribute = abovePythonMinimum

		list4ClassDefBody.append(create_ast_stmt())

	list4ModuleBody: list[ast.stmt] = [
			ast.ImportFrom('astToolkit', [ast.alias(identifier) for identifier in ['NodeORattribute']], 0)
			, ast.ImportFrom('astToolkit._astTypes', [ast.alias('*')], 0)
			, ast.ImportFrom('collections.abc', [ast.alias('Callable'), ast.alias('Sequence')], 0)
			, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('Literal')], 0)
			, ast.Import([ast.alias('ast')])
			, ast.Import([ast.alias('sys')])
			]

	writeClass('Grab', list4ClassDefBody, list4ModuleBody)

def makeToolMake():
	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringMake]

	listDictionaryToolElements = getElementsMake()

	for dictionaryToolElements in listDictionaryToolElements:
		ClassDefIdentifier = cast(str, dictionaryToolElements['ClassDefIdentifier'])
		classAs_astAttribute = cast(ast.Attribute, eval(dictionaryToolElements['classAs_astAttribute']))
		classVersionMinorMinimum: int = dictionaryToolElements['classVersionMinorMinimum']

		list4FunctionDef_args_args: list[ast.arg] = []

		keywordArguments_ast_arg=None
		keywordArguments_ast_keyword = None
		ast_stmt = ast.FunctionDef(
			name=ClassDefIdentifier
			, args=ast.arguments(posonlyargs=[], args=list4FunctionDef_args_args, vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=keywordArguments_ast_arg, defaults=[])
			, body=[ast.Return(value=ast.Call(classAs_astAttribute, args=[], keywords=[keywordArguments_ast_keyword] if keywordArguments_ast_keyword else []))]
			, decorator_list=[astName_staticmethod]
			, returns=classAs_astAttribute)

		if classVersionMinorMinimum > pythonVersionMinorMinimum:
			ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info'),
				ops=[ast.GtE()],
				comparators=[ast.Tuple([ast.Constant(3),
							ast.Constant(classVersionMinorMinimum)])]),
				body=[ast_stmt])

		list4ClassDefBody.append(ast_stmt)

	list4ModuleBody: list[ast.stmt] = [
		ast.ImportFrom('typing', [ast.alias('TypeGuard')], 0)
		, ast.Import([ast.alias('ast')])
		, ast.Import([ast.alias('sys')])
		]

	writeClass('Make', list4ClassDefBody, list4ModuleBody)

def makeTypeAlias():
	def append_ast_stmtTypeAlias():
		if len(dictionaryVersions) == 1:
			for versionMinor, listClassAs_astAttribute in dictionaryVersions.items():
				ast_stmt = ast.AnnAssign(astNameTypeAlias, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in listClassAs_astAttribute]), 1) # pyright: ignore[reportAttributeAccessIssue]
				if versionMinor > pythonVersionMinorMinimum:
					ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info')
								, ops=[ast.GtE()]
								, comparators=[ast.Tuple([ast.Constant(3),
										ast.Constant(versionMinor)])])
								, body=[ast_stmt])
				# This branch is the simplest case: one TypeAlias for the attribute for all Python versions
				astTypesModule.body.append(ast_stmt)
		else:
			# There is a smart way to do the following, but I don't see it right now. NOTE datacenter has the responsibility to aggregate all values <= pythonVersionMinorMinimum.
			listVersionsMinor = sorted(dictionaryVersions.keys(), reverse=False)
			if len(listVersionsMinor) > 2:
				raise NotImplementedError("Hunter's code can't handle this.")
			ast_stmtAtPythonMinimum = ast.AnnAssign(astNameTypeAlias, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in dictionaryVersions[min(listVersionsMinor)]]), 1) # pyright: ignore[reportAttributeAccessIssue]
			ast_stmtAbovePythonMinimum = ast.AnnAssign(astNameTypeAlias, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in sorted(chain(*dictionaryVersions.values()), key=str.lower)]), 1) # pyright: ignore[reportAttributeAccessIssue]

			ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info')
						, ops=[ast.GtE()]
						, comparators=[ast.Tuple([ast.Constant(3),
								ast.Constant(max(listVersionsMinor))])])
						, body=[ast_stmtAbovePythonMinimum]
						, orelse=[ast_stmtAtPythonMinimum])
			astTypesModule.body.append(ast_stmt)

	astTypesModule = ast.Module(
		body=[docstringWarning
			, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('TypeAlias', 'typing_TypeAlias')], 0)
			, ast.Import([ast.alias('ast')])
			, ast.Import([ast.alias('sys')])
			, *listHandmadeTypeAlias_astTypes
			]
		, type_ignores=[]
		)

	dictionaryToolElements: dict[str, dict[str, dict[int, list[str]]]] = getElementsTypeAlias()

	for attribute, dictionaryAttribute in dictionaryToolElements.items():
		hasDOTIdentifier: str = format_hasDOTIdentifier.format(attribute=attribute)
		hasDOTTypeAliasName_Store: ast.Name = ast.Name(hasDOTIdentifier, ast.Store())

		if len(dictionaryAttribute) == 1:
			astNameTypeAlias = hasDOTTypeAliasName_Store
			for TypeAliasSubcategory, dictionaryVersions in dictionaryAttribute.items():
				append_ast_stmtTypeAlias()
		else:
			# See?! Sometimes, I can see a smart way to do things. This defaultdict builds a dictionary to mimic the
			# process I'm already using to build the TypeAlias.
			attributeDictionaryVersions: dict[int, list[str]] = defaultdict(list)
			for TypeAliasSubcategory, dictionaryVersions in dictionaryAttribute.items():
				astNameTypeAlias: ast.Name = ast.Name(formatTypeAliasSubcategory.format(hasDOTIdentifier=hasDOTIdentifier, TypeAliasSubcategory=TypeAliasSubcategory), ast.Store())
				if any(dictionaryVersions.keys()) <= pythonVersionMinorMinimum:
					attributeDictionaryVersions[min(dictionaryVersions.keys())].append(ast.dump(astNameTypeAlias))
				else:
					attributeDictionaryVersions[min(dictionaryVersions.keys())].append(ast.dump(astNameTypeAlias))
					attributeDictionaryVersions[max(dictionaryVersions.keys())].append(ast.dump(astNameTypeAlias))
				append_ast_stmtTypeAlias()
			astNameTypeAlias = hasDOTTypeAliasName_Store
			dictionaryVersions: dict[int, list[str]] = attributeDictionaryVersions
			append_ast_stmtTypeAlias()

	writeModule(astTypesModule, '_astTypes')

if __name__ == "__main__":
	# makeToolBe()
	# makeToolDOT()
	makeToolGrab()
	makeTypeAlias()
