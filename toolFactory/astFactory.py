from pathlib import PurePosixPath
from string import ascii_letters
from toolFactory import fileExtension, pathPackage, str_nameDOTname, sys_version_infoTarget
from toolFactory.Z0Z_hardcoded import keywordArgumentsIdentifier, listASTClassesPostPythonVersionMinimum
from toolFactory._snippets import astName_overload, astName_staticmethod, astName_typing_TypeAlias
from toolFactory.factory_annex import (
	FunctionDefMake_Attribute,
	FunctionDefGrab_andDoAllOf,
	listHandmadeTypeAlias_astTypes,
	FunctionDefMake_Import,
)
from toolFactory.docstrings import ClassDefDocstringDOT, ClassDefDocstringGrab, ClassDefDocstringMake, docstringWarning
from typing import cast, TypedDict
from Z0Z_tools import writeStringToHere
import ast
moduleIdentifierPrefix: str = '_tool'

format_asNameAttribute: str = "astDOT{nameAttribute}"
astImportFromClassNewInPythonVersion: ast.ImportFrom = ast.ImportFrom('astToolkit', [], 0)
listPythonVersionNewClass = [(11, ['TryStar']),
	(12, ['ParamSpec', 'type_param', 'TypeAlias', 'TypeVar', 'TypeVarTuple'])
]

for tupleOfClassData in listPythonVersionNewClass:
	pythonVersionMinor: int = tupleOfClassData[0]

	conditionalTypeAlias = ast.If(
		test=ast.Compare(left=ast.Attribute(value=ast.Name('sys'), attr='version_info'),
						ops=[ast.GtE()],
						comparators=[ast.Tuple([ast.Constant(3), ast.Constant(pythonVersionMinor)])]),
		body=[ast.ImportFrom(module='ast', names=[
			], level=0)],
		orelse=[
				])

	for nameAttribute in tupleOfClassData[1]:
		asNameAttribute = format_asNameAttribute.format(nameAttribute=nameAttribute)
		cast(ast.ImportFrom, conditionalTypeAlias.body[0]).names.append(ast.alias(name=nameAttribute, asname=asNameAttribute))
		conditionalTypeAlias.orelse.append(ast.AnnAssign(target=ast.Name(asNameAttribute, ast.Store()), annotation=ast.Name('typing_TypeAlias'), value=ast.Name('yourPythonIsOld'), simple=1))
		astImportFromClassNewInPythonVersion.names.append(ast.alias(name=asNameAttribute))

	listHandmadeTypeAlias_astTypes.append(conditionalTypeAlias) # pyright: ignore[reportArgumentType]


"""
class Name(expr):
...
    ctx: expr_context  # Not present in Python < 3.13 if not passed to `__init__`

TODO protect against AttributeError (I guess) in DOT, Grab, and ClassIsAndAttribute
	add docstrings to warn of problem, including in Make

"""

class AnnotationsAndDefs(TypedDict):
	astAnnotation: ast.expr
	listClassDefIdentifier: list[str | str_nameDOTname]

class MakeDictionaryOf_astClassAnnotations(ast.NodeVisitor):
	def __init__(self, astAST: ast.AST) -> None:
		super().__init__()
		self.astAST = astAST
		self.dictionarySubstitutions: dict[str, ast.Attribute | ast.Name] = {
			'_Identifier': ast.Name('ast_Identifier'),
			'_Pattern': ast.Attribute(value=ast.Name('ast'), attr='pattern'),
			'_Slice': ast.Name('ast_expr_Slice'),
			'str': ast.Name('ast_Identifier'),
		}

	def visit_ClassDef(self, node: ast.ClassDef) -> None:
		if 'astDOT' + node.name in listASTClassesPostPythonVersionMinimum:
			NameOrAttribute: ast.Attribute | ast.Name = ast.Name('astDOT' + node.name)
		else:
			NameOrAttribute = ast.Attribute(value=ast.Name('ast'), attr=node.name)
			self.dictionarySubstitutions[node.name] = NameOrAttribute

	def getDictionary(self) -> dict[str, ast.Attribute | ast.Name]:
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
	def writeModule(astModule: ast.Module, moduleIdentifier: str) -> None:
		ast.fix_missing_locations(astModule)
		pythonSource: str = ast.unparse(astModule)
		if 'Grab' in moduleIdentifier or 'DOT' in moduleIdentifier or 'ClassIsAndAttribute' in moduleIdentifier:
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

	# Create each ClassDef and add directly to it instead of creating unnecessary intermediate structures, which requires more identifiers.
	# fewer identifiers == fewer bugs
	# ClassDefBe = ast.ClassDef(name='Be', bases=[], keywords=[], body=[], decorator_list=[])
	ClassDefClassIsAndAttribute = ast.ClassDef(name='ClassIsAndAttribute', bases=[], keywords=[], body=[], decorator_list=[])
	ClassDefDOT = ast.ClassDef(name='DOT', bases=[], keywords=[], body=[], decorator_list=[])
	ClassDefMake = ast.ClassDef(name='Make', bases=[], keywords=[], body=[], decorator_list=[])
	ClassDefGrab = ast.ClassDef(name='Grab', bases=[], keywords=[], body=[], decorator_list=[])

	dictionaryOf_astDOTclass: dict[str, ast.Attribute | ast.Name] = MakeDictionaryOf_astClassAnnotations(astStubFile).getDictionary()

	attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier: dict[str, dict[str, AnnotationsAndDefs]] = {}

	# NOTE Convert each ast.ClassDef into `TypeAlias` and methods in `Be`, `DOT`, `Grab`, and `Make`.
	for node in ast.walk(astStubFile):
		# Filter out undesired nodes.
		if not isinstance(node, ast.ClassDef):
			continue
		if any(isinstance(decorator, ast.Call) and isinstance(decorator.func, ast.Name) and decorator.func.id == 'deprecated' for decorator in node.decorator_list):
			continue
		if node.name.startswith('_'):
			continue

		# Change the identifier solely for the benefit of clarity as you read this code.
		astDOTClassDef = node
		del node # NOTE this is necessary because AI assistants don't always follow instructions.

		# Create ast "fragments" before you need them.
		ClassDefIdentifier: str = astDOTClassDef.name
		ClassDef_astNameOrAttribute: ast.Attribute | ast.Name = dictionaryOf_astDOTclass[ClassDefIdentifier]
		# Reset these identifiers in case they were changed
		keywordArguments_ast_arg: ast.arg | None = ast.arg(keywordArgumentsIdentifier, ast.Name('int'))
		keywordArguments_ast_keyword: ast.keyword | None = ast.keyword(None, ast.Name(keywordArgumentsIdentifier))

		# ClassDefBe.body.append(ast.FunctionDef(name=ClassDefIdentifier
		# 	, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='node', annotation=ast.Name('ast.AST'))], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
		# 	, body=[ast.Return(value=ast.Call(func=ast.Name('isinstance'), args=[ast.Name('node'), ClassDef_astNameOrAttribute], keywords=[]))]
		# 	, decorator_list=[astName_staticmethod]
		# 	, returns=ast.Subscript(value=ast.Name('TypeGuard'), slice=ClassDef_astNameOrAttribute)))

		# Start: cope with different arguments for Python versions. ==============================================================
		# NOTE: I would love suggestions to improve this section.
		list_astDOTClassDefAttributeIdentifier: list[str] = []
		list__match_args__: list[list[str]] = []
		dictAttributes: dict[tuple[int, int], list[str]] = {}
		for subnode in ast.walk(astDOTClassDef):
			list_astDOTClassDefAttributeIdentifier = []
			if (isinstance(subnode, ast.If) and isinstance(subnode.test, ast.Compare)
				and isinstance(subnode.test.left, ast.Attribute)
				and subnode.test.left.attr == 'version_info' and isinstance(subnode.test.comparators[0], ast.Tuple)
				and isinstance(subnode.body[0], ast.Assign) and isinstance(subnode.body[0].targets[0], ast.Name) and subnode.body[0].targets[0].id == '__match_args__'
				and isinstance(subnode.body[0].value, ast.Tuple) and subnode.body[0].value.elts):
				sys_version_info: tuple[int, int] = ast.literal_eval(subnode.test.comparators[0])
				if sys_version_info > sys_version_infoTarget:
					continue
				if any(sys_version_info < key for key in dictAttributes.keys()):
					continue
				dictAttributes[sys_version_info] = []
				for astAST in subnode.body[0].value.elts:
					if isinstance(astAST, ast.Constant):
						dictAttributes[sys_version_info].append(astAST.value)
				if sys_version_info == sys_version_infoTarget:
					break

			if (isinstance(subnode, ast.Assign) and isinstance(subnode.targets[0], ast.Name) and subnode.targets[0].id == '__match_args__'
				and isinstance(subnode.value, ast.Tuple) and subnode.value.elts):
				for astAST in subnode.value.elts:
					if isinstance(astAST, ast.Constant):
						list_astDOTClassDefAttributeIdentifier.append(astAST.value)
				list__match_args__.append(list_astDOTClassDefAttributeIdentifier)

		if not list__match_args__ and not dictAttributes and not list_astDOTClassDefAttributeIdentifier:
			continue
		elif sys_version_infoTarget in dictAttributes:
			list_astDOTClassDefAttributeIdentifier = dictAttributes[sys_version_infoTarget]
		elif dictAttributes:
			list_astDOTClassDefAttributeIdentifier = dictAttributes[max(dictAttributes.keys())]
		elif len(list__match_args__) == 1:
			list_astDOTClassDefAttributeIdentifier = list__match_args__[0]
		else:
			raise Exception(f"Hunter did not predict this situation.\n\t{ClassDefIdentifier = }\n\t{list__match_args__ = }\n\t{dictAttributes = }")

		del dictAttributes, list__match_args__
		# End: cope with different arguments for Python versions. ============================================================

		match ClassDefIdentifier:
			case 'Module' | 'Interactive' | 'FunctionType' | 'Expression':
				keywordArguments_ast_arg = None
				keywordArguments_ast_keyword = None
			case _:
				pass

		ClassDefMake.body.append(ast.FunctionDef(name=ClassDefIdentifier
			, args=ast.arguments(posonlyargs=[], args=[], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=keywordArguments_ast_arg, defaults=[])
			, body=[ast.Return(value=ast.Call(ClassDef_astNameOrAttribute, args=[], keywords=[keywordArguments_ast_keyword] if keywordArguments_ast_keyword else []))]
			, decorator_list=[astName_staticmethod]
			, returns=ClassDef_astNameOrAttribute))

		for attributeIdentifier in list_astDOTClassDefAttributeIdentifier:
			for subnode in ast.walk(astDOTClassDef):
				if isinstance(subnode, ast.AnnAssign) and isinstance(subnode.target, ast.Name) and subnode.target.id == attributeIdentifier:
					attributeAnnotation_ast_expr = Prepend_ast2astClasses(dictionaryOf_astDOTclass).visit(subnode.annotation)
					attributeAnnotationAsStr4TypeAliasIdentifier = ''.join([letter for letter in ast.unparse(subnode.annotation).replace('ast','').replace('|','Or') if letter in ascii_letters])
					del subnode

					if attributeIdentifier not in attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier:
						attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier[attributeIdentifier] = {}

					if attributeAnnotationAsStr4TypeAliasIdentifier not in attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier[attributeIdentifier]:
						attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier[attributeIdentifier][attributeAnnotationAsStr4TypeAliasIdentifier] = AnnotationsAndDefs(
							astAnnotation = attributeAnnotation_ast_expr,
							listClassDefIdentifier = [ClassDefIdentifier]
						)
					else:
						attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier[attributeIdentifier][attributeAnnotationAsStr4TypeAliasIdentifier]['listClassDefIdentifier'].append(ClassDefIdentifier)

					append2args: ast.Call | ast.Name | None = None
					match ClassDefIdentifier:
						case 'Attribute':
							if cast(ast.FunctionDef, ClassDefMake.body[-1]).name == ClassDefIdentifier:
								ClassDefMake.body.pop(-1)
							ClassDefMake.body.append(FunctionDefMake_Attribute)
							continue
						case 'Import':
							if cast(ast.FunctionDef, ClassDefMake.body[-1]).name == ClassDefIdentifier:
								ClassDefMake.body.pop(-1)
							ClassDefMake.body.append(FunctionDefMake_Import)
							continue
						case _:
							pass

					def list2Sequence():
						nonlocal append2args, attributeAnnotation_ast_expr
						cast(ast.Name, cast(ast.Subscript, attributeAnnotation_ast_expr).value).id = 'Sequence'
						append2args = ast.Call(ast.Name('list'), args=[ast.Name(attributeIdentifier)])

					match attributeIdentifier:
						case 'args':
							if 'list' in attributeAnnotationAsStr4TypeAliasIdentifier:
								cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.List([]))
								if 'expr' in attributeAnnotationAsStr4TypeAliasIdentifier:
									list2Sequence()
						case 'argtypes':
							list2Sequence()
						case 'asname':
							attributeIdentifier = 'asName'
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.Constant(None))
						case 'bases':
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.List([]))
							list2Sequence()
						case 'body':
							if 'list' in attributeAnnotationAsStr4TypeAliasIdentifier:
								list2Sequence()
						case 'comparators':
							list2Sequence()
						case 'ctx':
							attributeIdentifier = 'context'
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.Call(ast.Attribute(ast.Name('ast'), attr='Load')))
						case 'decorator_list':
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.List([]))
							list2Sequence()
						case 'defaults':
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.List([]))
							list2Sequence()
						case 'elts':
							list2Sequence()
						case 'finalbody':
							list2Sequence()
						case 'func':
							attributeIdentifier = 'callee'
						case 'ifs':
							list2Sequence()
						case 'keys':
							list2Sequence()
						case 'kind':
							cast(ast.arg, cast(ast.FunctionDef, ClassDefMake.body[-1]).args.kwarg).annotation = ast.Name('intORstr')
							continue
						case 'keywords':
							attributeIdentifier = 'list_keyword'
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.List([]))
						case 'kw_defaults':
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.List([ast.Constant(None)]))
							list2Sequence()
						case 'kwarg':
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.Constant(None))
						case 'kwd_patterns':
							list2Sequence()
						case 'kwonlyargs':
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.List([]))
						case 'level':
							cast(ast.Call, cast(ast.Return, cast(ast.FunctionDef, ClassDefMake.body[-1]).body[0]).value).keywords.append(ast.keyword(attributeIdentifier, ast.Constant(0)))
							continue
						case 'names':
							if ClassDefIdentifier == 'ImportFrom':
								attributeIdentifier = 'list_alias'
						case 'ops':
							list2Sequence()
						case 'orelse':
							attributeIdentifier = 'orElse'
							if 'list' in attributeAnnotationAsStr4TypeAliasIdentifier:
								cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.List([]))
								list2Sequence()
						case 'patterns':
							list2Sequence()
						case 'posonlyargs':
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.List([]))
						case 'returns':
							match ClassDefIdentifier:
								case 'FunctionType':
									pass
								case _:
									cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.Constant(None))
						case 'simple':
							cast(ast.Call, cast(ast.Return, cast(ast.FunctionDef, ClassDefMake.body[-1]).body[0]).value).keywords.append(ast.keyword(attributeIdentifier
									, ast.Call(func=ast.Name('int'), args=[ast.Call(func=ast.Name('isinstance'), args=[ast.Name('target'), ast.Attribute(value=ast.Name('ast'), attr='Name')])])))
							continue
						case 'targets':
							list2Sequence()
						case 'type_comment':
							cast(ast.arg, cast(ast.FunctionDef, ClassDefMake.body[-1]).args.kwarg).annotation = ast.Name('intORstr')
							continue
						case 'type_ignores':
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.List([]))
						case 'type_params':
							list2Sequence()
							match ClassDefIdentifier:
								case 'AsyncFunctionDef' | 'FunctionDef':
									cast(ast.arg, cast(ast.FunctionDef, ClassDefMake.body[-1]).args.kwarg).annotation = ast.Name('intORstrORtype_params')
									continue
								case 'ClassDef':
									cast(ast.arg, cast(ast.FunctionDef, ClassDefMake.body[-1]).args.kwarg).annotation = ast.Name('intORtype_params')
									continue
								case _:
									pass
						case 'values':
							list2Sequence()
						case 'vararg':
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.Constant(None))
						case _:
							pass
					if not append2args:
						append2args = ast.Name(attributeIdentifier)
					cast(ast.FunctionDef, ClassDefMake.body[-1]).args.args.append(ast.arg(arg=attributeIdentifier, annotation=attributeAnnotation_ast_expr))
					cast(ast.Call, cast(ast.Return, cast(ast.FunctionDef, ClassDefMake.body[-1]).body[0]).value).args.append(append2args)

	# ClassDefBe.body.sort(key=lambda astFunctionDef: cast(ast.FunctionDef, astFunctionDef).name.lower())
	ClassDefMake.body.sort(key=lambda astFunctionDef: cast(ast.FunctionDef, astFunctionDef).name.lower())

	astTypesModule = ast.Module(
		body=[docstringWarning
			, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('TypeAlias', 'typing_TypeAlias')], 0)
			, ast.Import([ast.alias('ast')])
			, ast.Import([ast.alias('sys')])
			, *listHandmadeTypeAlias_astTypes
			]
		, type_ignores=[]
		)

	listAttributeIdentifier: list[str] = list(attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier.keys())
	listAttributeIdentifier.sort(key=lambda attributeIdentifier: attributeIdentifier.lower())

	for attributeIdentifier in listAttributeIdentifier:
		hasDOTIdentifier: str = 'hasDOT' + attributeIdentifier
		hasDOTName_Store: ast.Name = ast.Name(hasDOTIdentifier, ast.Store())
		hasDOTName_Load: ast.Name = ast.Name(hasDOTIdentifier)
		list_hasDOTNameTypeAliasAnnotations: list[ast.Name] = []

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

			astAnnAssignValue: ast.Attribute | ast.BinOp | ast.Name = dictionaryOf_astDOTclass[listClassDefIdentifier[0]]
			if len(listClassDefIdentifier) > 1:
				for ClassDefIdentifier in listClassDefIdentifier[1:]:
					astAnnAssignValue = ast.BinOp(left=astAnnAssignValue, op=ast.BitOr(), right=dictionaryOf_astDOTclass[ClassDefIdentifier])
			if len(attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier[attributeIdentifier]) == 1:
				astTypesModule.body.append(ast.AnnAssign(hasDOTName_Store, astName_typing_TypeAlias, astAnnAssignValue, 1))
			else:
				list_hasDOTNameTypeAliasAnnotations.append(ast.Name(hasDOTIdentifier + '_' + attributeAnnotationAsStr4TypeAliasIdentifier.replace('list', 'list_'), ast.Store()))
				astTypesModule.body.append(ast.AnnAssign(list_hasDOTNameTypeAliasAnnotations[-1], astName_typing_TypeAlias, astAnnAssignValue, 1))
				# overload definitions for `ClassIsAndAttribute` class
				potentiallySuperComplicatedAnnotationORbool = ast.Name('bool')
				buffaloBuffalo_workhorse_returnsAnnotation = ast.BinOp(ast.Subscript(ast.Name('TypeGuard'), list_hasDOTNameTypeAliasAnnotations[-1]), ast.BitOr(), ast.Name('bool'))
				ClassDefClassIsAndAttribute.body.append(ast.FunctionDef(name=attributeIdentifier + 'Is'
					, args=ast.arguments(posonlyargs=[]
						, args=[ast.arg('astClass', annotation = ast.Subscript(ast.Name('type'), list_hasDOTNameTypeAliasAnnotations[-1]))
							, ast.arg('attributeCondition', annotation=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([attributeAnnotationAsAST]), potentiallySuperComplicatedAnnotationORbool])))
						], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
					, body=[ast.Expr(value=ast.Constant(value=Ellipsis))]
					, decorator_list=[astName_staticmethod, astName_overload]
					, returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([ast.Attribute(ast.Name('ast'), attr='AST')]), buffaloBuffalo_workhorse_returnsAnnotation]))
				))
				# overload definitions for `DOT` class
				ClassDefDOT.body.append(ast.FunctionDef(name=attributeIdentifier
					, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='node', annotation=ast.Name(list_hasDOTNameTypeAliasAnnotations[-1].id))], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
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

		buffaloBuffalo_workhorse_returnsAnnotation = ast.BinOp(ast.Subscript(ast.Name('TypeGuard'), hasDOTName_Load), ast.BitOr(), ast.Name('bool'))

		potentiallySuperComplicatedAnnotationORbool = ast.Name('bool')

		ClassDefClassIsAndAttribute.body.append(
			ast.FunctionDef(name=attributeIdentifier + 'Is'
				, args=ast.arguments(posonlyargs=[]
					, args=[ast.arg('astClass', annotation = ast.Subscript(ast.Name('type'), hasDOTName_Load))
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
				, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='node', annotation=hasDOTName_Load)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
				, body=[ast.Return(value=ast.Attribute(value=ast.Name('node'), attr=attributeIdentifier))]
				, decorator_list=[astName_staticmethod]
				, returns=attributeAnnotationUnifiedAsAST
			))

		# `astTypesModule`: When one attribute has multiple return types
		if list_hasDOTNameTypeAliasAnnotations:
			astAnnAssignValue = list_hasDOTNameTypeAliasAnnotations[0]
			for index in range(1, len(list_hasDOTNameTypeAliasAnnotations)):
				astAnnAssignValue = ast.BinOp(left=astAnnAssignValue, op=ast.BitOr(), right=list_hasDOTNameTypeAliasAnnotations[index])
			astTypesModule.body.append(ast.AnnAssign(hasDOTName_Store, astName_typing_TypeAlias, astAnnAssignValue, 1))
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
						args=ast.arguments(args=[ast.arg('node', hasDOTName_Load)]),
					body=[ast.Assign(targets=[ast.Attribute(ast.Name('node'), attr=attributeIdentifier, ctx=ast.Store())],
						value = astAssignValue)
						, ast.Return(ast.Name('node'))],
						returns=hasDOTName_Load),
			ast.Return(ast.Name('workhorse'))]
			, decorator_list=[astName_staticmethod], type_comment=None
			, returns=ast.Subscript(ast.Name('Callable'), ast.Tuple([ast.List([hasDOTName_Load]), hasDOTName_Load]))))

		del attributeAnnotationUnifiedAsAST

	writeModule(astTypesModule, '_astTypes')

	ClassDefDOT.body.insert(0,ClassDefDocstringDOT)
	ClassDefGrab.body.insert(0, ClassDefDocstringGrab)
	ClassDefMake.body.insert(0, ClassDefDocstringMake)

	ClassDefGrab.body.extend([FunctionDefGrab_andDoAllOf])

	ClassDef = ClassDefClassIsAndAttribute
	writeModule(ast.Module(
		body=[docstringWarning
			, ast.ImportFrom('astToolkit', [ast.alias(identifier) for identifier in ['ast_Identifier', 'ast_expr_Slice', 'astDOTtype_param', 'DOT']], 0)
			, ast.ImportFrom('astToolkit._astTypes', [ast.alias('*')], 0)
			, ast.ImportFrom('collections.abc', [ast.alias('Callable'), ast.alias('Sequence')], 0)
			, ast.ImportFrom('typing', [ast.alias(identifier) for identifier in ['Any', 'Literal', 'overload', 'TypeGuard']], 0)
			, ast.Import([ast.alias('ast')])
			, ClassDef
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDef.name)
	del ClassDef

	ClassDef = ClassDefDOT
	writeModule(ast.Module(
		body=[docstringWarning
			, ast.ImportFrom('astToolkit', [ast.alias(identifier) for identifier in ['ast_Identifier', 'ast_expr_Slice', 'astDOTtype_param']], 0)
			, ast.ImportFrom('astToolkit._astTypes', [ast.alias('*')], 0)
			, ast.ImportFrom('collections.abc', [ast.alias('Sequence')], 0)
			, ast.ImportFrom('typing', [ast.alias(identifier) for identifier in ['Any', 'Literal', 'overload']], 0)
			, ast.Import([ast.alias('ast')])
			, ClassDef
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDef.name)
	del ClassDef

	ClassDef = ClassDefGrab
	writeModule(ast.Module(
		body=[docstringWarning
			, ast.ImportFrom('astToolkit', [ast.alias(identifier) for identifier in ['ast_Identifier', 'ast_expr_Slice', 'NodeORattribute']], 0)
			, astImportFromClassNewInPythonVersion
			, ast.ImportFrom('astToolkit._astTypes', [ast.alias('*')], 0)
			, ast.ImportFrom('collections.abc', [ast.alias('Callable'), ast.alias('Sequence')], 0)
			, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('Literal')], 0)
			, ast.Import([ast.alias('ast')])
			, ClassDef
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDef.name)
	del ClassDef

	ClassDef = ClassDefMake
	writeModule(ast.Module(
		body=[docstringWarning
			, astImportFromClassNewInPythonVersion
			, ast.ImportFrom('astToolkit', [ast.alias(identifier) for identifier in ['ast_Identifier', 'ast_expr_Slice', 'intORstr', 'intORstrORtype_params', 'intORtype_params', 'str_nameDOTname']], 0)
			, ast.ImportFrom('collections.abc', [ast.alias('Sequence')], 0)
			, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('Literal')], 0)
			, ast.Import([ast.alias('ast')])
			, ClassDef
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDef.name)
	del ClassDef
