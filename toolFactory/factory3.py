from collections import defaultdict
from collections.abc import Sequence
from itertools import chain
from pathlib import PurePosixPath
from toolFactory import (
	astName_overload,
	astName_staticmethod,
	astName_typing_TypeAlias,
	DictionaryAstExprType,
	DictionaryToolMake,
	fileExtension,
	format_hasDOTIdentifier,
	formatTypeAliasSubcategory,
	getElementsBe,
	getElementsClassIsAndAttribute,
	getElementsDOT,
	getElementsMake,
	getElementsTypeAlias,
	keywordArgumentsIdentifier,
	listPylanceErrors,
	pathPackage,
	pythonVersionMinorMinimum,
	toolMakeFunctionDefReturnCall_keywords,
	)
from toolFactory.datacenter import getElementsGrab
from toolFactory.factory_annex import (
	FunctionDefGrab_andDoAllOf,
	FunctionDefMake_Attribute,
	FunctionDefMake_Import,
	listHandmadeTypeAlias_astTypes,
)
from toolFactory.docstrings import ClassDefDocstringBe, ClassDefDocstringClassIsAndAttribute, ClassDefDocstringGrab, ClassDefDocstringMake, ClassDefDocstringDOT, docstringWarning
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
		ClassDefIdentifier = dictionaryToolElements['ClassDefIdentifier']
		classAs_astAttribute = eval(dictionaryToolElements['classAs_astAttribute'])
		classVersionMinorMinimum = dictionaryToolElements['classVersionMinorMinimum']

		ast_stmt = ast.FunctionDef(
			name=ClassDefIdentifier
			, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='node', annotation=ast.Name('ast.AST'))], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
			, body=[ast.Return(value=ast.Call(func=ast.Name('isinstance'), args=[ast.Name('node'), classAs_astAttribute], keywords=[]))]
			, decorator_list=[astName_staticmethod]
			, returns=ast.Subscript(ast.Name('TypeGuard'), slice=classAs_astAttribute))

		if classVersionMinorMinimum > pythonVersionMinorMinimum:
			ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info')
						, ops=[ast.GtE()]
						, comparators=[ast.Tuple([ast.Constant(3)
												, ast.Constant(classVersionMinorMinimum)])])
					, body=[ast_stmt]
				)

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
							, orelse=orelse
			)

		return ast_stmt

	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringClassIsAndAttribute]

	dictionaryToolElements: dict[str, dict[str, DictionaryAstExprType]] = getElementsClassIsAndAttribute()

	# Process each attribute group to generate overloaded methods and implementations
	for attribute, dictionaryTypeAliasSubcategory in dictionaryToolElements.items():
		hasDOTIdentifier: str = format_hasDOTIdentifier.format(attribute=attribute)
		hasDOTTypeAliasName_Load: ast.Name = ast.Name(hasDOTIdentifier)
		orelse: list[ast.stmt] = []

		list_ast_exprType: list[ast.expr] = []
		dictionaryVersionsTypeAliasSubcategory: dict[int, list[ast.expr]] = defaultdict(list)

		if len(dictionaryTypeAliasSubcategory) > 1:
			for TypeAliasSubcategory, dictionary_ast_exprType in dictionaryTypeAliasSubcategory.items():
				attributeVersionMinorMinimum: int = dictionary_ast_exprType['attributeVersionMinorMinimum']
				astNameTypeAlias: ast.Name = ast.Name(formatTypeAliasSubcategory.format(hasDOTIdentifier=hasDOTIdentifier, TypeAliasSubcategory=TypeAliasSubcategory))
				body: list[ast.stmt] = [ast.Expr(ast.Constant(value=...))]
				decorator_list=[astName_staticmethod, astName_overload]
				returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Attribute(ast.Name('ast'), attr='AST')]), ast.BitOr.join([ast.Subscript(ast.Name('TypeGuard'), slice=astNameTypeAlias), ast.Name('bool')])])) # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]

				Z0Z_TypeWithoutNone = eval(dictionary_ast_exprType['ast_exprType'])
				annotation = ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([Z0Z_TypeWithoutNone]), ast.Name('bool')]))

				list_ast_exprType.append(annotation)
				dictionaryVersionsTypeAliasSubcategory[dictionary_ast_exprType['attributeVersionMinorMinimum']].append(annotation)

				list4ClassDefBody.append(create_ast_stmt())

		astNameTypeAlias = hasDOTTypeAliasName_Load
		if len(dictionaryVersionsTypeAliasSubcategory) > 1:
			attributeVersionMinorMinimum: int = min(dictionaryVersionsTypeAliasSubcategory.keys())
			decorator_list: list[ast.expr] = [astName_staticmethod]

			annotation = cast( ast.expr , ast.BitOr.join(dictionaryVersionsTypeAliasSubcategory[attributeVersionMinorMinimum])) # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
			workhorseReturnValue: ast.BoolOp = ast.BoolOp(op=ast.And(), values=[ast.Call(ast.Name('isinstance'), args=[ast.Name('node'), ast.Name('astClass')], keywords=[])])
			for node in ast.walk(annotation):
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

			buffaloBuffalo_workhorse_returnsAnnotation = cast(ast.expr, ast.BitOr.join([ast.Subscript(ast.Name('TypeGuard'), slice=astNameTypeAlias), ast.Name('bool')])) # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
			body: list[ast.stmt] = [ast.FunctionDef(name='workhorse',
						args=ast.arguments(args=[ast.arg('node', ast.Attribute(ast.Name('ast'), attr='AST'))])
						, body=[ast.Return(workhorseReturnValue)]
						, returns=buffaloBuffalo_workhorse_returnsAnnotation)
					, ast.Return(ast.Name('workhorse'))]
			returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Attribute(ast.Name('ast'), attr='AST')]), buffaloBuffalo_workhorse_returnsAnnotation]))

			del dictionaryVersionsTypeAliasSubcategory[attributeVersionMinorMinimum]
			orelse = [create_ast_stmt()]

		for TypeAliasSubcategory, dictionary_ast_exprType in dictionaryTypeAliasSubcategory.items():
			attributeVersionMinorMinimum: int = dictionary_ast_exprType['attributeVersionMinorMinimum']
			decorator_list=[astName_staticmethod]
			if list_ast_exprType:
				annotation = cast(ast.expr,  ast.BitOr.join(list_ast_exprType)) # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
			else:
				Z0Z_TypeWithoutNone = eval(dictionary_ast_exprType['ast_exprType'])
				annotation = ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([Z0Z_TypeWithoutNone]), ast.Name('bool')]))

			workhorseReturnValue: ast.BoolOp = ast.BoolOp(op=ast.And(), values=[ast.Call(ast.Name('isinstance'), args=[ast.Name('node'), ast.Name('astClass')], keywords=[])])
			for node in ast.walk(annotation):
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
			buffaloBuffalo_workhorse_returnsAnnotation = cast(ast.expr,  ast.BitOr.join([ast.Subscript(ast.Name('TypeGuard'), slice=astNameTypeAlias), ast.Name('bool')])) # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
			body: list[ast.stmt] = [ast.FunctionDef(name='workhorse',
						args=ast.arguments(args=[ast.arg('node', ast.Attribute(ast.Name('ast'), attr='AST'))])
						, body=[ast.Return(workhorseReturnValue)]
						, returns=buffaloBuffalo_workhorse_returnsAnnotation)
					, ast.Return(ast.Name('workhorse'))]
			returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Attribute(ast.Name('ast'), attr='AST')]), buffaloBuffalo_workhorse_returnsAnnotation]))

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
					, returns=returns
		)

		if attributeVersionMinorMinimum > pythonVersionMinorMinimum:
			ast_stmt = ast.If(ast.Compare(left=ast.Attribute(ast.Name('sys'), 'version_info')
								, ops=[ast.GtE()]
								, comparators=[ast.Tuple([ast.Constant(3), ast.Constant(attributeVersionMinorMinimum)])])
							, body=[ast_stmt]
							, orelse=orelse
			)

		return ast_stmt

	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringDOT]

	dictionaryToolElements: dict[str, dict[str, DictionaryAstExprType]] = getElementsDOT()

	# Process each attribute group to generate overloaded methods and implementations
	for attribute, dictionaryTypeAliasSubcategory in dictionaryToolElements.items():
		hasDOTIdentifier: str = format_hasDOTIdentifier.format(attribute=attribute)
		hasDOTTypeAliasName_Load: ast.Name = ast.Name(hasDOTIdentifier)
		orelse: list[ast.stmt] = []

		list_ast_exprType: list[ast.expr] = []
		dictionaryVersionsTypeAliasSubcategory: dict[int, list[ast.expr]] = defaultdict(list)
		if len(dictionaryTypeAliasSubcategory) > 1:
			for TypeAliasSubcategory, dictionary_ast_exprType in dictionaryTypeAliasSubcategory.items():
				attributeVersionMinorMinimum: int = dictionary_ast_exprType['attributeVersionMinorMinimum']
				astNameTypeAlias: ast.Name = ast.Name(formatTypeAliasSubcategory.format(hasDOTIdentifier=hasDOTIdentifier, TypeAliasSubcategory=TypeAliasSubcategory))
				body: list[ast.stmt] = [ast.Expr(ast.Constant(value=...))]
				decorator_list=[astName_staticmethod, astName_overload]
				returns = cast(ast.Attribute, eval(dictionary_ast_exprType['ast_exprType']))
				list_ast_exprType.append(returns)
				dictionaryVersionsTypeAliasSubcategory[dictionary_ast_exprType['attributeVersionMinorMinimum']].append(returns)
				list4ClassDefBody.append(create_ast_stmt())

		astNameTypeAlias = hasDOTTypeAliasName_Load
		if len(dictionaryVersionsTypeAliasSubcategory) > 1:
			body: list[ast.stmt] = [ast.Return(ast.Attribute(ast.Name('node'), attribute))]
			decorator_list: list[ast.expr] = [astName_staticmethod]
			attributeVersionMinorMinimum: int = min(dictionaryVersionsTypeAliasSubcategory.keys())
			returns = cast( ast.expr, ast.BitOr.join(dictionaryVersionsTypeAliasSubcategory[attributeVersionMinorMinimum])) # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
			del dictionaryVersionsTypeAliasSubcategory[attributeVersionMinorMinimum]
			orelse = [create_ast_stmt()]

		for TypeAliasSubcategory, dictionary_ast_exprType in dictionaryTypeAliasSubcategory.items():
			attributeVersionMinorMinimum: int = dictionary_ast_exprType['attributeVersionMinorMinimum']
			body: list[ast.stmt] = [ast.Return(ast.Attribute(ast.Name('node'), attribute))]
			decorator_list=[astName_staticmethod]
			if list_ast_exprType:
				returns = cast(ast.expr, ast.BitOr.join(list_ast_exprType)) # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]
			else:
				returns = cast(ast.Attribute, eval(dictionary_ast_exprType['ast_exprType']))
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
		for attributeVersionMinorMinimum, list_ast_exprType in listTypesByVersion:
			list_ast_expr4annotation: list[ast.expr] = []
			for ast_exprTypeAsStr in list_ast_exprType:
				ast_exprType = eval(ast_exprTypeAsStr)
				list_ast_expr4annotation.append(ast.Subscript(ast.Name('Callable'), slice=ast.Tuple([ast.List([ast_exprType]), ast_exprType])))

			ast_expr4annotation = cast(ast.expr, ast.BitOr.join(list_ast_expr4annotation)) # pyright: ignore[reportUnknownMemberType, reportAttributeAccessIssue]

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
				orelse=ast_stmtAtPythonMinimum
				)
		assert ast_stmt is not None
		return ast_stmt

	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringGrab, FunctionDefGrab_andDoAllOf]
	dictionaryToolElements = getElementsGrab()

	for attribute, listTypesByVersion in dictionaryToolElements.items():
		hasDOTIdentifier: str = format_hasDOTIdentifier.format(attribute=attribute)
		hasDOTTypeAliasName_Load: ast.Name = ast.Name(hasDOTIdentifier)
		ast_stmtAtPythonMinimum: list[ast.stmt] = []

		if len(listTypesByVersion) > 1:
			abovePythonMinimum = [((versionMax := max([typesForVersion[0] for typesForVersion in listTypesByVersion])),  sorted(chain(*[typesForVersion[1] for typesForVersion in listTypesByVersion]), key=str.lower))]
			for typesForVersion in listTypesByVersion:
				if typesForVersion[0] == versionMax:
					listTypesByVersion.remove(typesForVersion)
					break
			ast_stmtAtPythonMinimum = [create_ast_stmt()]
			listTypesByVersion = abovePythonMinimum

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
	setKeywordArgumentsAnnotationTypeAlias: set[str] = set()

	listDictionaryToolElements = getElementsMake()

	ff = ['AsyncFunctionDef', 'ClassDef', 'FunctionDef']
	for dictionaryToolElements in listDictionaryToolElements:
		if dictionaryToolElements['ClassDefIdentifier'] in ff:
			for k,v in dictionaryToolElements.items():
				print(k,v)
				continue
				print(k)
				if isinstance(v, list):
					for item in v:
						if isinstance(item, tuple):
							print(item[0], item[1], item[2], sep='\n\t')
						else:
							print('\t', item)
				else:
					print('\t', v)
			# continue
		"""
ClassDefIdentifier alias
classAs_astAttribute ast.Attribute(ast.Name('ast'), 'alias')
classVersionMinorMinimum -1
match_argsVersionMinorMinimum -1
listStr4FunctionDef_args ["ast.arg('name', ast.Name('str'))", "ast.arg('asName', ast.BinOp(left=ast.Name('str'), op=ast.BitOr(), right=ast.Constant(value=None)))"]
listDefaults ['ast.Constant(None)']
listTupleCall_keywords [('name', False, 'name'), ('asname', False, 'asName')]
kwarg int

		"""
		ClassDefIdentifier = str(dictionaryToolElements['ClassDefIdentifier'])
		if ClassDefIdentifier == 'Attribute':
			ast_stmt = FunctionDefMake_Attribute
			list4ClassDefBody.append(ast_stmt)
			continue
		if ClassDefIdentifier == 'Import':
			ast_stmt = FunctionDefMake_Import
			list4ClassDefBody.append(ast_stmt)
			continue

		classAs_astAttribute = cast(ast.expr, eval(dictionaryToolElements['classAs_astAttribute']))

		listFunctionDef_args: list[ast.arg] = [cast(ast.arg, eval(ast_argAsStr)) for ast_argAsStr in dictionaryToolElements['listStr4FunctionDef_args']]
		kwarg: ast.arg | None = None
		if str(dictionaryToolElements['kwarg']) != 'No':
			setKeywordArgumentsAnnotationTypeAlias.add(dictionaryToolElements['kwarg'])
			kwarg = ast.arg(keywordArgumentsIdentifier, annotation=ast.Name(str(dictionaryToolElements['kwarg'])))

		defaults: list[ast.expr] = [cast(ast.expr, eval(defaultAsStr)) for defaultAsStr in dictionaryToolElements['listDefaults']]

		listCall_keywords: list[ast.keyword] = []
		for tupleCall_keywords in dictionaryToolElements['listTupleCall_keywords']:
			argIdentifier, defaultValueNeedsEval, keywordValue = tupleCall_keywords
			if defaultValueNeedsEval:
				listCall_keywords.append(ast.keyword(argIdentifier, value=eval(keywordValue)))
			else:
				listCall_keywords.append(ast.keyword(argIdentifier, value=ast.Name(keywordValue)))
		if kwarg is not None:
			listCall_keywords.append(toolMakeFunctionDefReturnCall_keywords)

		# print(f"{ClassDefIdentifier=}")
		# print(ast.dump(classAs_astAttribute))
		# print('listFunctionDef_args', *[ast.dump(FunctionDef_arg) for FunctionDef_arg in listFunctionDef_args], sep='\n\t')
		# print(ast.dump(kwarg) if kwarg else kwarg)
		# print('defaults', f"{type(defaults)=}", *[ast.dump(ast_expr) for ast_expr in defaults], sep='\n\t')
		# print('listCall_keywords', *[ast.dump(Call_keyword) for Call_keyword in listCall_keywords], sep='\n\t')

		classVersionMinorMinimum: int = dictionaryToolElements['classVersionMinorMinimum']
		# if match_argsVersionMinorMinimum > classVersionMinorMinimum:
		# Do some variations of the method need to be conditional on the Python version?
		# if match_argsVersionMinorMinimum == classVersionMinorMinimum, then access to match_argsVersionMinorMinimum is already conditional on the python version because it is checked at the class level.
		match_argsVersionMinorMinimum: int = dictionaryToolElements['match_argsVersionMinorMinimum']

		ast_stmt = ast.FunctionDef(
			name=ClassDefIdentifier
			, args=ast.arguments(posonlyargs=[], args=listFunctionDef_args, vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=kwarg, defaults=defaults)
			, body=[ast.Return(ast.Call(classAs_astAttribute, args=[], keywords=listCall_keywords))]
			, decorator_list=[astName_staticmethod]
			, returns=classAs_astAttribute)

		# Does _every_ variation of the method need to be conditional on the Python version?
		if classVersionMinorMinimum > pythonVersionMinorMinimum:
			ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info')
						, ops=[ast.GtE()]
						, comparators=[ast.Tuple([ast.Constant(3)
												, ast.Constant(classVersionMinorMinimum)])])
					, body=[ast_stmt]
				)
		elif match_argsVersionMinorMinimum > classVersionMinorMinimum:
			# Only some variations of the method need to be conditional on the Python version.
			ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info')
						, ops=[ast.GtE()]
						, comparators=[ast.Tuple([ast.Constant(3)
												, ast.Constant(match_argsVersionMinorMinimum)])])
					, body=[ast_stmt]
				)

		list4ClassDefBody.append(ast_stmt)

	setKeywordArgumentsAnnotationTypeAlias.discard('int')
	list4ModuleBody: list[ast.stmt] = [
		ast.ImportFrom('astToolkit', [ast.alias(identifier) for identifier in sorted([*setKeywordArgumentsAnnotationTypeAlias, 'str_nameDOTname'])], 0)
		, ast.ImportFrom('collections.abc', [ast.alias('Sequence')], 0)
		, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('Literal')], 0)
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
	makeToolMake()
	makeTypeAlias()
