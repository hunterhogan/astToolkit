from pathlib import PurePosixPath
from toolFactory import (
	astName_overload,
	astName_staticmethod,
	astName_typing_TypeAlias,
	fileExtension,
	getElementsBe,
	getElementsTypeAlias,
	keywordArgumentsIdentifier,
	moduleIdentifierPrefix,
	pathPackage,
	pythonVersionMinorMinimum,
	getElementsMake,
	)
from toolFactory.factory_annex import (
	FunctionDefMake_Attribute,
	FunctionDefMake_Import,
	listHandmadeTypeAlias_astTypes,
)
from toolFactory.docstrings import ClassDefDocstringBe, ClassDefDocstringMake, docstringWarning
from typing import cast, TypedDict
from Z0Z_tools import writeStringToHere
import ast

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
	# if moduleIdentifier in {'ClassIsAndAttribute', 'DOT', 'Grab'}:
	# 	pythonSource = "# ruff: noqa: F403, F405\n" + pythonSource
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
	# if 'Grab' in moduleIdentifier:
	# 	listTypeIgnore: list[ast.TypeIgnore] = []
	# 	tag = '[reportAttributeAccessIssue]'
	# 	for attribute in listPylanceErrors:
	# 		for splitlinesNumber, line in enumerate(pythonSource.splitlines()):
	# 			if 'node.'+attribute in line:
	# 				listTypeIgnore.append(ast.TypeIgnore(splitlinesNumber+1, tag))
	# 				break
	# 	astModule = ast.parse(pythonSource)
	# 	astModule.type_ignores.extend(listTypeIgnore)
	# 	pythonSource = ast.unparse(astModule)
	# 	pythonSource = "# ruff: noqa: F403, F405\n" + pythonSource
	pathFilenameModule = PurePosixPath(pathPackage, moduleIdentifier + fileExtension)
	writeStringToHere(pythonSource, pathFilenameModule)

def makeTypeAlias():
	astTypesModule = ast.Module(
		body=[docstringWarning
			, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('TypeAlias', 'typing_TypeAlias')], 0)
			, ast.Import([ast.alias('ast')])
			, ast.Import([ast.alias('sys')])
			, *listHandmadeTypeAlias_astTypes
			]
		, type_ignores=[]
		)

	typeAliasData: dict[str, dict[str, dict[int, list[str]]]] = getElementsTypeAlias()

	for attribute, dictionaryAttribute in typeAliasData.items():
		hasDOTIdentifier: str = 'hasDOT' + attribute
		hasDOTTypeAliasName_Load: ast.Name = ast.Name(hasDOTIdentifier)
		hasDOTTypeAliasName_Store: ast.Name = ast.Name(hasDOTIdentifier, ast.Store())

		if len(dictionaryAttribute) == 1:
			for TypeAliasSubcategory, dictionaryVersions in dictionaryAttribute.items():
				if len(dictionaryVersions) == 1:
					for versionMinor, listClassAs_astAttribute in dictionaryVersions.items():
						ast_stmt = ast.AnnAssign(hasDOTTypeAliasName_Store, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in listClassAs_astAttribute]), 1)
						if versionMinor > pythonVersionMinorMinimum:
							ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info')
										, ops=[ast.GtE()]
										, comparators=[ast.Tuple([ast.Constant(3),
												ast.Constant(versionMinor)])])
										, body=[ast_stmt])
							# print(versionMinor, attribute, listClassAs_astAttribute, sep='\t')
						# This branch is the simplest case: one TypeAlias for the attribute for all Python versions
						astTypesModule.body.append(ast_stmt)
						# print(attribute, listClassAs_astAttribute, sep='\t')
				else:
					listVersionsMinor = sorted(dictionaryVersions.keys(), reverse=False)
					versionMinorMinimum = -1
					ast_stmtGreater = None
					ast_stmtLesser = None
					for versionMinor in listVersionsMinor:
						versionMinorMinimum = max(versionMinorMinimum, versionMinor)
						if versionMinor > pythonVersionMinorMinimum:
							ast_stmtGreater = ast.AnnAssign(hasDOTTypeAliasName_Store, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in sorted(iter(*dictionaryVersions.values()), key=lambda classAs_astAttribute: classAs_astAttribute.lower())]), 1)
							# print(versionMinor, attribute, dictionaryVersions[versionMinor], sep='\t')
						else:
							ast_stmtLesser = ast.AnnAssign(hasDOTTypeAliasName_Store, astName_typing_TypeAlias, ast.BitOr.join([eval(classAs_astAttribute) for classAs_astAttribute in dictionaryVersions[versionMinor]]), 1)
							# print('else', attribute, dictionaryVersions[versionMinor], sep='\t')
					ast_stmt = ast.If(ast.Compare(ast.Attribute(ast.Name('sys'), 'version_info')
								, ops=[ast.GtE()]
								, comparators=[ast.Tuple([ast.Constant(3),
										ast.Constant(versionMinorMinimum)])])
								, body=[ast_stmtGreater]
								, orelse=[ast_stmtLesser])
					astTypesModule.body.append(ast_stmt)
		if len(dictionaryAttribute) != 1:
			continue
			print(attribute)
			for TypeAliasSubcategory, dictionaryVersions in dictionaryAttribute.items():
				print('\t', TypeAliasSubcategory)
				for versionMinor, listClassAs_astAttribute in dictionaryVersions.items():
					print('\t\t', versionMinor, listClassAs_astAttribute, sep='\t')

	writeModule(astTypesModule, '_astTypes')

def makeToolBe():
	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringBe]

	listDictionaryToolElements = getElementsBe(sortOn='ClassDefIdentifier')

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

	ClassDefBe = ast.ClassDef(name='Be', bases=[], keywords=[], body=list4ClassDefBody, decorator_list=[])

	ClassDef = ClassDefBe
	writeModule(ast.Module(
		body=[docstringWarning
			, ast.ImportFrom('typing', [ast.alias('TypeGuard')], 0)
			, ast.Import([ast.alias('ast')])
			, ast.Import([ast.alias('sys')])
			, ClassDef
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDef.name)
	del ClassDef

def makeToolMake():
	list4ClassDefBody: list[ast.stmt] = [ClassDefDocstringMake]

	listDictionaryToolElements = getElementsMake(sortOn='ClassDefIdentifier')

	for dictionaryToolElements in listDictionaryToolElements:
		ClassDefIdentifier = cast(str, dictionaryToolElements['ClassDefIdentifier'])
		classAs_astAttribute = cast(ast.Attribute, eval(dictionaryToolElements['classAs_astAttribute']))
		classVersionMinorMinimum: int = dictionaryToolElements['classVersionMinorMinimum']

		list4FunctionDef_args_args: list[ast.arg] = []
		keywordArguments_ast_arg=[]
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

	ClassDefMake = ast.ClassDef(name='Make', bases=[], keywords=[], body=list4ClassDefBody, decorator_list=[])

	ClassDef = ClassDefMake
	writeModule(ast.Module(
		body=[docstringWarning
			, ast.ImportFrom('typing', [ast.alias('TypeGuard')], 0)
			, ast.Import([ast.alias('ast')])
			, ast.Import([ast.alias('sys')])
			, ClassDef
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDef.name)
	del ClassDef

# scrap parts

class AnnotationsAndDefs(TypedDict):
	astAnnotation: ast.expr
	listClassDefIdentifier: list[str]

class MakeDictionaryOf_astClassAnnotations(ast.NodeVisitor):
	def __init__(self, astAST: ast.AST) -> None:
		super().__init__()
		self.astAST = astAST
		self.dictionarySubstitutions: dict[str, ast.Attribute] = {
			'_Pattern': ast.Attribute(value=ast.Name('ast'), attr='pattern'),
		}

	def visit_ClassDef(self, node: ast.ClassDef) -> None:
		NameOrAttribute = ast.Attribute(value=ast.Name('ast'), attr=node.name)
		self.dictionarySubstitutions[node.name] = NameOrAttribute

	def getDictionary(self) -> dict[str, ast.Attribute]:
		self.visit(self.astAST)
		return self.dictionarySubstitutions

class Prepend_ast2astClasses(ast.NodeTransformer):
	def __init__(self, dictionarySubstitutions: dict[str, ast.Attribute | ast.Name]) -> None:
		super().__init__()
		self.dictionarySubstitutions = dictionarySubstitutions

	def visit_Name(self, node: ast.Name) -> ast.Attribute | ast.Name:
		if node.id in self.dictionarySubstitutions:
			return self.dictionarySubstitutions[node.id]
		return node

def makeTools(astStubFile: ast.AST) -> None:

	ClassDefClassIsAndAttribute = ast.ClassDef(name='ClassIsAndAttribute', bases=[], keywords=[], body=[], decorator_list=[])
	ClassDefDOT = ast.ClassDef(name='DOT', bases=[], keywords=[], body=[], decorator_list=[])
	ClassDefGrab = ast.ClassDef(name='Grab', bases=[], keywords=[], body=[], decorator_list=[])

	dictionaryOf_astDOTclass: dict[str, ast.Attribute] = MakeDictionaryOf_astClassAnnotations(astStubFile).getDictionary()

	attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier: dict[str, dict[str, AnnotationsAndDefs]] = {}

	# NOTE Convert each ast.ClassDef into `TypeAlias` and methods in `Be`, `DOT`, `Grab`, and `Make`.
	for node in ast.walk(astStubFile):
		if not isinstance(node, ast.ClassDef):
			continue
		if not (node.name == 'AST' or (node.bases and isinstance(node.bases[0], ast.Name))):
			continue

		# Change the identifier solely for the benefit of clarity as you read this code.
		astDOTClassDef = node

		# Create ast "fragments" before you need them.
		ClassDefIdentifier: str = astDOTClassDef.name
		classAs_astAttribute: ast.Attribute | ast.Name = dictionaryOf_astDOTclass[ClassDefIdentifier]
		# Reset these identifiers in case they were changed
		keywordArguments_ast_arg: ast.arg | None = ast.arg(keywordArgumentsIdentifier, ast.Name('int'))
		keywordArguments_ast_keyword: ast.keyword | None = ast.keyword(None, ast.Name(keywordArgumentsIdentifier))

		match ClassDefIdentifier:
			case 'Module' | 'Interactive' | 'FunctionType' | 'Expression':
				keywordArguments_ast_arg = None
				keywordArguments_ast_keyword = None
			case _:
				pass

	# astTypesModule = ast.Module(
	# 	body=[docstringWarning
	# 		, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('TypeAlias', 'typing_TypeAlias')], 0)
	# 		, ast.Import([ast.alias('ast')])
	# 		, ast.Import([ast.alias('sys')])
	# 		, *listHandmadeTypeAlias_astTypes
	# 		]
	# 	, type_ignores=[]
	# 	)

	listAttributeIdentifier: list[str] = list(attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier.keys())
	listAttributeIdentifier.sort(key=lambda attributeIdentifier: attributeIdentifier.lower())

	for attributeIdentifier in listAttributeIdentifier:
		hasDOTTypeAliasIdentifier: str = 'hasDOT' + attributeIdentifier
		hasDOTTypeAliasName_Store: ast.Name = ast.Name(hasDOTTypeAliasIdentifier, ast.Store())
		hasDOTTypeAliasName_Load: ast.Name = ast.Name(hasDOTTypeAliasIdentifier)
		list_hasDOTTypeAliasAnnotations: list[ast.Name] = []

		attributeAnnotationUnifiedAsAST = None

		for attributeAnnotationAsStr4TypeAliasIdentifier, classDefAttributeMapping in attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier[attributeIdentifier].items():
			listClassDefIdentifier = classDefAttributeMapping['listClassDefIdentifier']
			attributeAnnotationAsAST = classDefAttributeMapping['astAnnotation']
			if not attributeAnnotationUnifiedAsAST:
				attributeAnnotationUnifiedAsAST = attributeAnnotationAsAST
			else:
				attributeAnnotationUnifiedAsAST = ast.BinOp(
					left=attributeAnnotationUnifiedAsAST,
					op=ast.BitOr(),
					right=attributeAnnotationAsAST
				)

			hasDOTTypeAliasClassesBinOp: ast.Attribute | ast.BinOp = dictionaryOf_astDOTclass[listClassDefIdentifier[0]]
			if len(listClassDefIdentifier) > 1:
				for ClassDefIdentifier in listClassDefIdentifier[1:]:
					hasDOTTypeAliasClassesBinOp = ast.BinOp(left=hasDOTTypeAliasClassesBinOp, op=ast.BitOr(), right=dictionaryOf_astDOTclass[ClassDefIdentifier])
			if len(attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier[attributeIdentifier]) == 1:
				pass
				# astTypesModule.body.append(ast.AnnAssign(hasDOTTypeAliasName_Store, astName_typing_TypeAlias, hasDOTTypeAliasClassesBinOp, 1))
			else:
				list_hasDOTTypeAliasAnnotations.append(ast.Name(hasDOTTypeAliasIdentifier + '_' + attributeAnnotationAsStr4TypeAliasIdentifier.replace('list', 'list_'), ast.Store()))
				# astTypesModule.body.append(ast.AnnAssign(list_hasDOTTypeAliasAnnotations[-1], astName_typing_TypeAlias, hasDOTTypeAliasClassesBinOp, 1))
				# overload definitions for `ClassIsAndAttribute` class
				potentiallySuperComplicatedAnnotationORbool = ast.Name('bool')
				buffaloBuffalo_workhorse_returnsAnnotation = ast.BinOp(ast.Subscript(ast.Name('TypeGuard'), list_hasDOTTypeAliasAnnotations[-1]), ast.BitOr(), ast.Name('bool'))
				ClassDefClassIsAndAttribute.body.append(ast.FunctionDef(name=attributeIdentifier + 'Is'
					, args=ast.arguments(posonlyargs=[]
						, args=[ast.arg('astClass', annotation = ast.Subscript(ast.Name('type'), list_hasDOTTypeAliasAnnotations[-1]))
							, ast.arg('attributeCondition', annotation=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([attributeAnnotationAsAST]), potentiallySuperComplicatedAnnotationORbool])))
						], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
					, body=[ast.Expr(value=ast.Constant(value=Ellipsis))]
					, decorator_list=[astName_staticmethod, astName_overload]
					, returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Attribute(ast.Name('ast'), attr='AST')]), buffaloBuffalo_workhorse_returnsAnnotation]))
				))
				# overload definitions for `DOT` class
				ClassDefDOT.body.append(ast.FunctionDef(name=attributeIdentifier
					, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='node', annotation=ast.Name(list_hasDOTTypeAliasAnnotations[-1].id))], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
					, body=[ast.Expr(value=ast.Constant(value=Ellipsis))]
					, decorator_list=[astName_staticmethod, astName_overload]
					, returns=attributeAnnotationAsAST
				))

		assert attributeAnnotationUnifiedAsAST is not None, 'Brinkmanship to appease the type checker!'
		workhorseReturnValue: ast.BoolOp = ast.BoolOp(op=ast.And(), values=[ast.Call(ast.Name('isinstance'), args=[ast.Name('node'), ast.Name('astClass')], keywords=[])])
		for node in ast.walk(attributeAnnotationUnifiedAsAST):
			if isinstance(node, ast.Subscript) and isinstance(node.value, ast.Name) and node.value.id == 'Sequence' and isinstance(node.slice, ast.BinOp) and isinstance(node.slice.right, ast.Constant) and node.slice.right.value is None:
				workhorseReturnValue.values.append(ast.Compare(ast.Call(ast.Attribute(ast.Name('DOT'), attributeIdentifier), args=[ast.Name('node')])
												, ops=[ast.NotEq()]
												, comparators=[ast.List([ast.Constant(None)])]))
				break
			if isinstance(node, ast.Constant) and node.value is None:
				workhorseReturnValue.values.append(ast.Compare(ast.Call(ast.Attribute(ast.Name('DOT'), attributeIdentifier), args=[ast.Name('node')])
												, ops=[ast.IsNot()]
												, comparators=[ast.Constant(None)]))
				break
		workhorseReturnValue.values.append(ast.Call(ast.Name('attributeCondition'), args=[ast.Call(ast.Attribute(ast.Name('DOT'), attr=attributeIdentifier), args=[ast.Name('node')])], keywords=[]))

		buffaloBuffalo_workhorse_returnsAnnotation = ast.BinOp(ast.Subscript(ast.Name('TypeGuard'), hasDOTTypeAliasName_Load), ast.BitOr(), ast.Name('bool'))

		potentiallySuperComplicatedAnnotationORbool = ast.Name('bool')

		ClassDefClassIsAndAttribute.body.append(
			ast.FunctionDef(name=attributeIdentifier + 'Is'
				, args=ast.arguments(posonlyargs=[]
					, args=[ast.arg('astClass', annotation = ast.Subscript(ast.Name('type'), hasDOTTypeAliasName_Load))
						, ast.arg('attributeCondition', annotation=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([attributeAnnotationUnifiedAsAST]), potentiallySuperComplicatedAnnotationORbool])))
					], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
				, body=[ast.FunctionDef(name='workhorse',
							args=ast.arguments(args=[ast.arg('node', ast.Attribute(ast.Name('ast'), attr='AST'))])
							, body=[ast.Return(workhorseReturnValue)]
							, returns=buffaloBuffalo_workhorse_returnsAnnotation)
						, ast.Return(ast.Name('workhorse'))]
				, decorator_list=[astName_staticmethod]
				, returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Attribute(ast.Name('ast'), attr='AST')]), buffaloBuffalo_workhorse_returnsAnnotation]))
			))

		ClassDefDOT.body.append(ast.FunctionDef(name=attributeIdentifier
				, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='node', annotation=hasDOTTypeAliasName_Load)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
				, body=[ast.Return(value=ast.Attribute(value=ast.Name('node'), attr=attributeIdentifier))]
				, decorator_list=[astName_staticmethod]
				, returns=attributeAnnotationUnifiedAsAST
			))

		# `astTypesModule`: When one attribute has multiple return types
		# if list_hasDOTTypeAliasAnnotations:
		# 	hasDOTTypeAliasClassesBinOp = list_hasDOTTypeAliasAnnotations[0] # pyright: ignore[reportAssignmentType]
		# 	for index in range(1, len(list_hasDOTTypeAliasAnnotations)):
		# 		hasDOTTypeAliasClassesBinOp = ast.BinOp(left=hasDOTTypeAliasClassesBinOp, op=ast.BitOr(), right=list_hasDOTTypeAliasAnnotations[index])
		# 	astTypesModule.body.append(ast.AnnAssign(hasDOTTypeAliasName_Store, astName_typing_TypeAlias, hasDOTTypeAliasClassesBinOp, 1))
		astAssignValue = ast.Call(ast.Name('action'), args=[ast.Attribute(ast.Name('node'), attr=attributeIdentifier)])
		if (isinstance(attributeAnnotationUnifiedAsAST, ast.Subscript) and isinstance(attributeAnnotationUnifiedAsAST.value, ast.Name) and attributeAnnotationUnifiedAsAST.value.id == 'Sequence'
		or isinstance(attributeAnnotationUnifiedAsAST, ast.BinOp) and isinstance(attributeAnnotationUnifiedAsAST.right, ast.Subscript) and isinstance(attributeAnnotationUnifiedAsAST.right.value, ast.Name) and attributeAnnotationUnifiedAsAST.right.value.id == 'Sequence'):
			astAssignValue = ast.Call(ast.Name('list'), args=[ast.Call(ast.Name('action'), args=[ast.Attribute(ast.Name('node'), attr=attributeIdentifier)])])
		ClassDefGrab.body.append(ast.FunctionDef(name=attributeIdentifier + 'Attribute'
			, args=ast.arguments(posonlyargs=[]
				, args=[ast.arg('action'
					, annotation=ast.Subscript(ast.Name('Callable')
						, slice=ast.Tuple(elts=[
							ast.List(elts=[attributeAnnotationUnifiedAsAST])
							,   attributeAnnotationUnifiedAsAST]
						)))]
				, vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
			, body=[ast.FunctionDef(name='workhorse',
						args=ast.arguments(args=[ast.arg('node', hasDOTTypeAliasName_Load)]),
					body=[ast.Assign(targets=[ast.Attribute(ast.Name('node'), attr=attributeIdentifier, ctx=ast.Store())],
						value = astAssignValue)
						, ast.Return(ast.Name('node'))],
						returns=hasDOTTypeAliasName_Load),
			ast.Return(ast.Name('workhorse'))]
			, decorator_list=[astName_staticmethod], type_comment=None
			, returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([hasDOTTypeAliasName_Load]), hasDOTTypeAliasName_Load]))))

		del attributeAnnotationUnifiedAsAST

if __name__ == "__main__":
	makeTypeAlias()
	makeToolBe()
