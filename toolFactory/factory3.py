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
	getElementsClassIsAndAttribute,
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
from toolFactory.docstrings import ClassDefDocstringBe, ClassDefDocstringClassIsAndAttribute, ClassDefDocstringGrab, ClassDefDocstringMake, docstringWarning, ClassDefDocstringDOT
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
	if 'ClassIsAndAttribute' in moduleIdentifier:
		pythonSource = "# pyright: reportArgumentType=false\n" + pythonSource
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
			, returns=ast.Subscript(ast.Name('TypeGuard'), slice=classAs_astAttribute))

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

def makeToolClassIsAndAttribute():
	def create_ast_stmt():
		ast_stmt = ast.FunctionDef(attribute + 'Is'
				, args=ast.arguments(posonlyargs=[]
					, args=[ast.arg('astClass', annotation = ast.Subscript(ast.Name('type'), astNameTypeAlias))
						, ast.arg('attributeCondition', annotation=annotation)
					], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
					, body=body
					, decorator_list=decorator_list
					, returns=returns
		)

		if attributeVersionMinorMinimum > pythonVersionMinorMinimum:
			ast_stmt = ast.If(ast.Compare(left=ast.Attribute(ast.Name('sys'), 'version_info')
								, ops=[ast.GtE()]
								, comparators=[ast.Tuple([ast.Constant(3), ast.Constant(attributeVersionMinorMinimum)])])
							, body=[ast_stmt]
							, orelse=orelse # pyright: ignore[reportUnknownArgumentType]
			)

		return ast_stmt

	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringClassIsAndAttribute]

	dictionaryToolElements: dict[str, dict[str, dict[str, int | str]]] = getElementsClassIsAndAttribute()

	# Process each attribute group to generate overloaded methods and implementations
	for attribute, dictionaryTypeAliasSubcategory in dictionaryToolElements.items():
		hasDOTIdentifier: str = format_hasDOTIdentifier.format(attribute=attribute)
		hasDOTTypeAliasName_Load: ast.Name = ast.Name(hasDOTIdentifier)
		orelse = []

		list_ast_exprType: list[ast.expr] = []
		dictionaryVersionsTypeAliasSubcategory: dict[int, list[ast.expr]] = defaultdict(list)

		if len(dictionaryTypeAliasSubcategory) > 1:
			for TypeAliasSubcategory, dictionary_ast_exprType in dictionaryTypeAliasSubcategory.items():
				attributeVersionMinorMinimum: int = dictionary_ast_exprType['attributeVersionMinorMinimum'] # pyright: ignore[reportAssignmentType]
				astNameTypeAlias: ast.Name = ast.Name(formatTypeAliasSubcategory.format(hasDOTIdentifier=hasDOTIdentifier, TypeAliasSubcategory=TypeAliasSubcategory))
				body: list[ast.stmt] = [ast.Expr(ast.Constant(value=...))]
				decorator_list=[astName_staticmethod, astName_overload]
				returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Attribute(ast.Name('ast'), attr='AST')]), ast.BitOr.join([ast.Subscript(ast.Name('TypeGuard'), slice=astNameTypeAlias), ast.Name('bool')])])) # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]

				Z0Z_TypeWithoutNone = eval(dictionary_ast_exprType['ast_exprType']) # pyright: ignore[reportArgumentType]
				annotation = ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([Z0Z_TypeWithoutNone]), ast.Name('bool')]))

				list_ast_exprType.append(annotation)
				dictionaryVersionsTypeAliasSubcategory[dictionary_ast_exprType['attributeVersionMinorMinimum']].append(annotation) # pyright: ignore[reportArgumentType]

				list4ClassDefBody.append(create_ast_stmt())

		astNameTypeAlias = hasDOTTypeAliasName_Load
		if len(dictionaryVersionsTypeAliasSubcategory) > 1:
			attributeVersionMinorMinimum: int = min(dictionaryVersionsTypeAliasSubcategory.keys()) # pyright: ignore[reportAssignmentType]
			decorator_list=[astName_staticmethod]

			annotation: ast.expr = ast.BitOr.join(dictionaryVersionsTypeAliasSubcategory[attributeVersionMinorMinimum]) # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType, reportAttributeAccessIssue]
			workhorseReturnValue: ast.BoolOp = ast.BoolOp(op=ast.And(), values=[ast.Call(ast.Name('isinstance'), args=[ast.Name('node'), ast.Name('astClass')], keywords=[])])
			for node in ast.walk(annotation): # pyright: ignore[reportUnknownArgumentType]
				if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) and node.value.id == 'Sequence' and isinstance(node.slice, ast.BinOp) and isinstance(node.slice.right, ast.Constant) and node.slice.right.value is None:
					workhorseReturnValue.values.append(ast.Compare(ast.Attribute(ast.Name('node'), attribute)
													, ops=[ast.NotEq()]
													, comparators=[ast.List([ast.Constant(None)])]))
					break
				if isinstance(node, ast.Constant) and node.value is None:
					workhorseReturnValue.values.append(ast.Compare(ast.Attribute(ast.Name('node'), attribute)
													, ops=[ast.IsNot()]
													, comparators=[ast.Constant(None)]))
					break

			workhorseReturnValue.values.append(ast.Call(ast.Name('attributeCondition'), args=[ast.Attribute(ast.Name('node'), attribute)]))

			buffaloBuffalo_workhorse_returnsAnnotation: ast.expr = ast.BitOr.join([ast.Subscript(ast.Name('TypeGuard'), slice=astNameTypeAlias), ast.Name('bool')]) # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType, reportAttributeAccessIssue]
			body: list[ast.stmt] = [ast.FunctionDef(name='workhorse',
						args=ast.arguments(args=[ast.arg('node', ast.Attribute(ast.Name('ast'), attr='AST'))])
						, body=[ast.Return(workhorseReturnValue)]
						, returns=buffaloBuffalo_workhorse_returnsAnnotation) # pyright: ignore[reportUnknownArgumentType]
					, ast.Return(ast.Name('workhorse'))]
			returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Attribute(ast.Name('ast'), attr='AST')]), buffaloBuffalo_workhorse_returnsAnnotation])) # pyright: ignore[reportUnknownArgumentType]


			del dictionaryVersionsTypeAliasSubcategory[attributeVersionMinorMinimum]
			orelse = [create_ast_stmt()]

		for TypeAliasSubcategory, dictionary_ast_exprType in dictionaryTypeAliasSubcategory.items():
			attributeVersionMinorMinimum: int = dictionary_ast_exprType['attributeVersionMinorMinimum'] # pyright: ignore[reportAssignmentType]
			decorator_list=[astName_staticmethod]
			if list_ast_exprType:
				annotation: ast.expr = ast.BitOr.join(list_ast_exprType) # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType, reportAttributeAccessIssue]
			else:
				Z0Z_TypeWithoutNone = eval(dictionary_ast_exprType['ast_exprType']) # pyright: ignore[reportArgumentType]
				annotation = ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([Z0Z_TypeWithoutNone]), ast.Name('bool')]))

			workhorseReturnValue: ast.BoolOp = ast.BoolOp(op=ast.And(), values=[ast.Call(ast.Name('isinstance'), args=[ast.Name('node'), ast.Name('astClass')], keywords=[])])
			for node in ast.walk(annotation): # pyright: ignore[reportUnknownArgumentType]
				if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) and node.value.id == 'list' and isinstance(node.slice, ast.BinOp) and isinstance(node.slice.right, ast.Constant) and node.slice.right.value is None:
					workhorseReturnValue.values.append(ast.Compare(ast.Attribute(ast.Name('node'), attribute)
													, ops=[ast.NotEq()]
													, comparators=[ast.List([ast.Constant(None)])]))
					break
				if isinstance(node, ast.Constant) and node.value is None:
					workhorseReturnValue.values.append(ast.Compare(ast.Attribute(ast.Name('node'), attribute)
													, ops=[ast.IsNot()]
													, comparators=[ast.Constant(None)]))
					break

			workhorseReturnValue.values.append(ast.Call(ast.Name('attributeCondition'), args=[ast.Attribute(ast.Name('node'), attribute)]))
			buffaloBuffalo_workhorse_returnsAnnotation: ast.expr = ast.BitOr.join([ast.Subscript(ast.Name('TypeGuard'), slice=astNameTypeAlias), ast.Name('bool')]) # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType, reportAttributeAccessIssue]
			body: list[ast.stmt] = [ast.FunctionDef(name='workhorse',
						args=ast.arguments(args=[ast.arg('node', ast.Attribute(ast.Name('ast'), attr='AST'))])
						, body=[ast.Return(workhorseReturnValue)]
						, returns=buffaloBuffalo_workhorse_returnsAnnotation) # pyright: ignore[reportUnknownArgumentType]
					, ast.Return(ast.Name('workhorse'))]
			returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Attribute(ast.Name('ast'), attr='AST')]), buffaloBuffalo_workhorse_returnsAnnotation])) # pyright: ignore[reportUnknownArgumentType]

			list4ClassDefBody.append(create_ast_stmt())
			break

	list4ModuleBody: list[ast.stmt] = [
			ast.ImportFrom('astToolkit._astTypes', [ast.alias('*')], 0)
			, ast.ImportFrom('collections.abc', [ast.alias('Callable'), ast.alias('Sequence')], 0)
			, ast.ImportFrom('typing', [ast.alias(identifier) for identifier in ['Any', 'Literal', 'overload', 'TypeGuard']], 0)
			, ast.Import([ast.alias('ast')])
	]

	writeClass('ClassIsAndAttribute', list4ClassDefBody, list4ModuleBody)

def makeToolDOT():
	def create_ast_stmt():
		ast_stmt = ast.FunctionDef(attribute
				, args=ast.arguments(posonlyargs=[]
					, args=[ast.arg('node', astNameTypeAlias)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
					, body=body
					, decorator_list=decorator_list
					, returns=returns # pyright: ignore[reportUnknownArgumentType]
		)

		if attributeVersionMinorMinimum > pythonVersionMinorMinimum:
			ast_stmt = ast.If(ast.Compare(left=ast.Attribute(ast.Name('sys'), 'version_info')
								, ops=[ast.GtE()]
								, comparators=[ast.Tuple([ast.Constant(3), ast.Constant(attributeVersionMinorMinimum)])])
							, body=[ast_stmt]
							, orelse=orelse # pyright: ignore[reportUnknownArgumentType]
			)

		return ast_stmt

	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringDOT]

	dictionaryToolElements: dict[str, dict[str, dict[str, int | str]]] = getElementsDOT()

	# Process each attribute group to generate overloaded methods and implementations
	for attribute, dictionaryTypeAliasSubcategory in dictionaryToolElements.items():
		hasDOTIdentifier: str = format_hasDOTIdentifier.format(attribute=attribute)
		hasDOTTypeAliasName_Load: ast.Name = ast.Name(hasDOTIdentifier)
		orelse=[]

		list_ast_exprType: list[ast.expr] = []
		dictionaryVersionsTypeAliasSubcategory: dict[int, list[ast.expr]] = defaultdict(list)
		if len(dictionaryTypeAliasSubcategory) > 1:
			for TypeAliasSubcategory, dictionary_ast_exprType in dictionaryTypeAliasSubcategory.items():
				attributeVersionMinorMinimum: int = dictionary_ast_exprType['attributeVersionMinorMinimum'] # pyright: ignore[reportAssignmentType]
				astNameTypeAlias: ast.Name = ast.Name(formatTypeAliasSubcategory.format(hasDOTIdentifier=hasDOTIdentifier, TypeAliasSubcategory=TypeAliasSubcategory))
				body: list[ast.stmt] = [ast.Expr(ast.Constant(value=...))]
				decorator_list=[astName_staticmethod, astName_overload]
				returns = cast(ast.Attribute, eval(dictionary_ast_exprType['ast_exprType'])) # pyright: ignore[reportArgumentType]
				list_ast_exprType.append(returns)
				dictionaryVersionsTypeAliasSubcategory[dictionary_ast_exprType['attributeVersionMinorMinimum']].append(returns) # pyright: ignore[reportArgumentType]
				list4ClassDefBody.append(create_ast_stmt())

		astNameTypeAlias = hasDOTTypeAliasName_Load
		if len(dictionaryVersionsTypeAliasSubcategory) > 1:
			body: list[ast.stmt] = [ast.Return(ast.Attribute(ast.Name('node'), attribute))]
			decorator_list=[astName_staticmethod]
			attributeVersionMinorMinimum: int = min(dictionaryVersionsTypeAliasSubcategory.keys()) # pyright: ignore[reportAssignmentType]
			returns: ast.expr = ast.BitOr.join(dictionaryVersionsTypeAliasSubcategory[attributeVersionMinorMinimum]) # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType, reportAttributeAccessIssue]
			del dictionaryVersionsTypeAliasSubcategory[attributeVersionMinorMinimum]
			orelse = [create_ast_stmt()]

		for TypeAliasSubcategory, dictionary_ast_exprType in dictionaryTypeAliasSubcategory.items():
			attributeVersionMinorMinimum: int = dictionary_ast_exprType['attributeVersionMinorMinimum'] # pyright: ignore[reportAssignmentType]
			body: list[ast.stmt] = [ast.Return(ast.Attribute(ast.Name('node'), attribute))]
			decorator_list=[astName_staticmethod]
			if list_ast_exprType:
				returns: ast.expr = ast.BitOr.join(list_ast_exprType) # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType, reportAttributeAccessIssue]
			else:
				returns = cast(ast.Attribute, eval(dictionary_ast_exprType['ast_exprType'])) # pyright: ignore[reportArgumentType]
			list4ClassDefBody.append(create_ast_stmt())
			break

	list4ModuleBody: list[ast.stmt] = [
			ast.ImportFrom(module='astToolkit._astTypes', names=[ast.alias(name='*')], level=0)
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
			list_ast_expr4annotation: list[ast.expr] = []
			for ast_exprTypeAsStr in list_ast_exprType:
				ast_exprType = eval(ast_exprTypeAsStr)
				list_ast_expr4annotation.append(ast.Subscript(ast.Name('Callable'), slice=ast.Tuple([ast.List([ast_exprType]), ast_exprType])))

			ast_expr4annotation: ast.expr = ast.BitOr.join(list_ast_expr4annotation) # pyright: ignore[reportUnknownVariableType, reportUnknownMemberType, reportAttributeAccessIssue]

			ast_stmt = ast.FunctionDef(attribute + 'Attribute'
				, args=ast.arguments(posonlyargs=[], args=[ast.arg('action', annotation=ast_expr4annotation)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]) # pyright: ignore[reportUnknownArgumentType]
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
				orelse=ast_stmtAtPythonMinimum # pyright: ignore[reportUnknownArgumentType]
				)
		assert ast_stmt is not None
		return ast_stmt

	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringGrab, FunctionDefGrab_andDoAllOf]
	dictionaryToolElements: dict[str, dict[int, list[str]]] = getElementsGrab()

	for attribute, dictionaryAttribute in dictionaryToolElements.items():
		hasDOTIdentifier: str = format_hasDOTIdentifier.format(attribute=attribute)
		hasDOTTypeAliasName_Load: ast.Name = ast.Name(hasDOTIdentifier)
		ast_stmtAtPythonMinimum = []

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
			# This branch is the simplest case: one TypeAlias for the attribute for all Python versions
			for versionMinor, listClassAs_astAttribute in dictionaryVersions.items():
				ast_stmt = ast.AnnAssign(astNameTypeAlias, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in listClassAs_astAttribute]), 1) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType, reportAttributeAccessIssue]
				if versionMinor > pythonVersionMinorMinimum:
					ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info')
								, ops=[ast.GtE()]
								, comparators=[ast.Tuple([ast.Constant(3),
										ast.Constant(versionMinor)])])
								, body=[ast_stmt])
		else:
			# There is a smart way to do the following, but I don't see it right now. NOTE datacenter has the responsibility to aggregate all values <= pythonVersionMinorMinimum.
			listVersionsMinor = sorted(dictionaryVersions.keys(), reverse=False)
			if len(listVersionsMinor) > 2:
				raise NotImplementedError
			ast_stmtAtPythonMinimum = ast.AnnAssign(astNameTypeAlias, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in dictionaryVersions[min(listVersionsMinor)]]), 1) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType, reportAttributeAccessIssue]
			ast_stmtAbovePythonMinimum = ast.AnnAssign(astNameTypeAlias, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in sorted(chain(*dictionaryVersions.values()), key=str.lower)]), 1) # pyright: ignore[reportUnknownArgumentType, reportUnknownMemberType, reportAttributeAccessIssue]

			ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info')
						, ops=[ast.GtE()]
						, comparators=[ast.Tuple([ast.Constant(3),
								ast.Constant(max(listVersionsMinor))])])
						, body=[ast_stmtAbovePythonMinimum]
						, orelse=[ast_stmtAtPythonMinimum])
		astTypesModule.body.append(ast_stmt) # pyright: ignore[reportPossiblyUnboundVariable]

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

	for attribute, dictionaryTypeAliasSubcategory in dictionaryToolElements.items():
		hasDOTIdentifier: str = format_hasDOTIdentifier.format(attribute=attribute)
		hasDOTTypeAliasName_Store: ast.Name = ast.Name(hasDOTIdentifier, ast.Store())

		if len(dictionaryTypeAliasSubcategory) == 1:
			astNameTypeAlias = hasDOTTypeAliasName_Store
			for TypeAliasSubcategory, dictionaryVersions in dictionaryTypeAliasSubcategory.items():
				append_ast_stmtTypeAlias()
		else:
			# See?! Sometimes, I can see a smart way to do things. This defaultdict builds a dictionary to mimic the
			# process I'm already using to build the TypeAlias.
			attributeDictionaryVersions: dict[int, list[str]] = defaultdict(list)
			for TypeAliasSubcategory, dictionaryVersions in dictionaryTypeAliasSubcategory.items():
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
	makeToolBe()
	makeToolClassIsAndAttribute()
	makeToolDOT()
	makeToolGrab()
	makeTypeAlias()
