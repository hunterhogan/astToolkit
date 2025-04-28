from astToolkit import str_nameDOTname, The
from pathlib import PurePosixPath
from string import ascii_letters
from toolFactory import ast_Identifier, list_astDOTnew, sys_version_infoTarget
from toolFactory.astFactory_annex import handmadeMethodsGrab, handmadeTypeAlias_astTypes, MakeAttributeFunctionDef, MakeImportFunctionDef
from toolFactory.docstrings import docstringWarning, ClassDefDocstringBe, ClassDefDocstringDOT, ClassDefDocstringGrab, ClassDefDocstringMake
from typing import cast, TypedDict
from Z0Z_tools import writeStringToHere
import ast

class AnnotationsAndDefs(TypedDict):
	astAnnotation: ast.expr
	listClassDefIdentifier: list[ast_Identifier | str_nameDOTname]

astImportFromClassNewInPythonVersion = ast.ImportFrom('astToolkit', [ast.alias(post310class) for post310class in list_astDOTnew], 0)

keywordArgumentsIdentifier: ast_Identifier = 'keywordArguments'
moduleIdentifierPrefix: str = '_tool'
overloadName = ast.Name('overload', ast.Load())
staticmethodName = ast.Name('staticmethod', ast.Load())
typing_TypeAliasName: ast.expr = cast(ast.expr, ast.Name('typing_TypeAlias', ast.Load()))

class MakeDictionaryOf_astClassAnnotations(ast.NodeVisitor):
	def __init__(self, astAST: ast.AST) -> None:
		super().__init__()
		self.astAST = astAST
		self.dictionarySubstitutions: dict[ast_Identifier, ast.Attribute | ast.Name] = {
			'_Identifier': ast.Name('ast_Identifier'),
			'_Pattern': ast.Attribute(value=ast.Name('ast'), attr='pattern', ctx=ast.Load()),
			'_Slice': ast.Name('ast_expr_Slice'),
			'str': ast.Name('ast_Identifier'),
		}

	def visit_ClassDef(self, node: ast.ClassDef) -> None:
		if 'astDOT' + node.name in list_astDOTnew:
			NameOrAttribute = ast.Name('astDOT' + node.name, ctx=ast.Load())
		else:
			NameOrAttribute = ast.Attribute(value=ast.Name('ast'), attr=node.name, ctx=ast.Load())
		self.dictionarySubstitutions[node.name] = NameOrAttribute

	def getDictionary(self) -> dict[ast_Identifier, ast.Attribute | ast.Name]:
		self.visit(self.astAST)
		return self.dictionarySubstitutions

class Prepend_ast2astClasses(ast.NodeTransformer):
	"""The _effect_ of this `NodeTransformer` is to replace a naked `Jabberwocky` identifier with the specific
	`ast.Jabberwocky` identifier.

	The explanation, however, sounds like "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo."

	Initialize `ast.NodeTransformer` with mapping from subclass `ast._Identifier` of class `AST`, which is implemented
	in C, imported from module `_ast`, and defined in stub `ast.pyi`, to subclass `ast.Attribute`, rendered as
	"ast._Identifier" or subclass `ast.Name` for `AST` subclasses implemented later than Python version 3.10, rendered
	as "astDOT_Identifier" and defined as `typing.TypeAlias` or `typing.Any` depending on the runtime Python version in
	"__init__".

	Call method `visit` of `ast.NodeTransformer` with class `AST` or `AST` subclass parameter. `ast.NodeTransformer`
	will call `visit_Name` to visit each node descendant class `AST` or `AST` subclass parameter of class `ast.Name`.
	The class `ast.Name` descendant node identifier is `node`. If method `visit_Name` matches subclass `ast._Identifier`
	`node.id` to a mapping key, it returns the subclass `ast.Attribute` or subclass `ast.Name` mapping value. Otherwise,
	`visit_Name` returns subclass `ast.Name` `node`.
	"""
	def __init__(self, dictionarySubstitutions: dict[ast_Identifier, ast.Attribute | ast.Name]) -> None:
		super().__init__()
		self.dictionarySubstitutions = dictionarySubstitutions

	def visit_Name(self, node: ast.Name) -> ast.Attribute | ast.Name:
		if node.id in self.dictionarySubstitutions:
			return self.dictionarySubstitutions[node.id]
		return node

def makeTools(astStubFile: ast.AST, logicalPathInfix: str_nameDOTname = None) -> None:
	def writeModule(astModule: ast.Module, moduleIdentifier: ast_Identifier) -> None:
		ast.fix_missing_locations(astModule)
		pythonSource: str = ast.unparse(astModule)
		if 'Grab' in moduleIdentifier or 'DOT' in moduleIdentifier:
			pythonSource = "# ruff: noqa: F403, F405\n" + pythonSource
		pathFilenameModule = PurePosixPath(The.pathPackage, moduleIdentifier + The.fileExtension)
		writeStringToHere(pythonSource, pathFilenameModule)

	# Create each ClassDef and add directly to it instead of creating unnecessary intermediate structures.
	# fewer identifiers == fewer bugs
	ClassDefBe = ast.ClassDef(name='Be', bases=[], keywords=[], body=[], decorator_list=[])
	ClassDefDOT = ast.ClassDef(name='DOT', bases=[], keywords=[], body=[], decorator_list=[])
	ClassDefMake = ast.ClassDef(name='Make', bases=[], keywords=[], body=[], decorator_list=[])
	ClassDefGrab = ast.ClassDef(name='Grab', bases=[], keywords=[], body=[], decorator_list=[])

	dictionaryOf_astDOTclass: dict[ast_Identifier, ast.Attribute | ast.Name] = MakeDictionaryOf_astClassAnnotations(astStubFile).getDictionary()

	attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier: dict[ast_Identifier, dict[str, AnnotationsAndDefs]] = {}

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
		ClassDefIdentifier: ast_Identifier = astDOTClassDef.name
		ClassDef_astNameOrAttribute: ast.Attribute | ast.Name = dictionaryOf_astDOTclass[ClassDefIdentifier]
		# Reset these identifiers in case they were changed
		keywordArguments_ast_arg: ast.arg | None = ast.arg(keywordArgumentsIdentifier, ast.Name('int', ctx=ast.Load()))
		keywordArguments_ast_keyword: ast.keyword | None = ast.keyword(None, ast.Name(keywordArgumentsIdentifier, ctx=ast.Load()))

		ClassDefBe.body.append(ast.FunctionDef(name=ClassDefIdentifier
			, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='node', annotation=ast.Name('ast.AST'))], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
			, body=[ast.Return(value=ast.Call(func=ast.Name('isinstance'), args=[ast.Name('node'), ClassDef_astNameOrAttribute], keywords=[]))]
			, decorator_list=[staticmethodName]
			, returns=ast.Subscript(value=ast.Name('TypeGuard'), slice=ClassDef_astNameOrAttribute, ctx=ast.Load())))

		# Start: cope with different arguments for Python versions. ==============================================================
		# NOTE: I would love suggestions to improve this section.
		list_astDOTClassDefAttributeIdentifier: list[ast_Identifier] = []
		list__match_args__: list[list[ast_Identifier]] = []
		dictAttributes: dict[tuple[int, int], list[ast_Identifier]] = {}
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
				if any(sys_version_info < key for key in dictAttributes.keys()): # pyright: ignore[reportOperatorIssue]
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
			, decorator_list=[staticmethodName]
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

					append2args = None
					match ClassDefIdentifier:
						case 'Attribute':
							if cast(ast.FunctionDef, ClassDefMake.body[-1]).name == ClassDefIdentifier:
								ClassDefMake.body.pop(-1)
							ClassDefMake.body.append(MakeAttributeFunctionDef)
							continue
						case 'Import':
							if cast(ast.FunctionDef, ClassDefMake.body[-1]).name == ClassDefIdentifier:
								ClassDefMake.body.pop(-1)
							ClassDefMake.body.append(MakeImportFunctionDef)
							continue
						case _:
							pass

					def list2Sequence():
						nonlocal append2args, attributeAnnotation_ast_expr
						cast(ast.Name, cast(ast.Subscript, attributeAnnotation_ast_expr).value).id = 'Sequence'
						append2args = ast.Call(ast.Name('list', ctx=ast.Load()), args=[ast.Name(attributeIdentifier, ctx=ast.Load())])

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
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.Call(ast.Attribute(ast.Name('ast', ctx=ast.Load()), attr='Load', ctx=ast.Load())))
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
							cast(ast.arg, cast(ast.FunctionDef, ClassDefMake.body[-1]).args.kwarg).annotation = ast.Name('intORstr', ctx=ast.Load())
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
									, ast.Call(func=ast.Name('int', ctx=ast.Load()), args=[ast.Call(func=ast.Name('isinstance', ctx=ast.Load()), args=[ast.Name('target', ctx=ast.Load()), ast.Attribute(value=ast.Name('ast', ctx=ast.Load()), attr='Name', ctx=ast.Load())])])))
							continue
						case 'targets':
							list2Sequence()
						case 'type_comment':
							cast(ast.arg, cast(ast.FunctionDef, ClassDefMake.body[-1]).args.kwarg).annotation = ast.Name('intORstr', ctx=ast.Load())
							continue
						case 'type_ignores':
							cast(ast.FunctionDef, ClassDefMake.body[-1]).args.defaults.append(ast.List([]))
						case 'type_params':
							list2Sequence()
							match ClassDefIdentifier:
								case 'AsyncFunctionDef' | 'FunctionDef':
									cast(ast.arg, cast(ast.FunctionDef, ClassDefMake.body[-1]).args.kwarg).annotation = ast.Name('intORstrORtype_params', ctx=ast.Load())
									continue
								case 'ClassDef':
									cast(ast.arg, cast(ast.FunctionDef, ClassDefMake.body[-1]).args.kwarg).annotation = ast.Name('intORtype_params', ctx=ast.Load())
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
						append2args = ast.Name(attributeIdentifier, ctx=ast.Load())
					cast(ast.FunctionDef, ClassDefMake.body[-1]).args.args.append(ast.arg(arg=attributeIdentifier, annotation=attributeAnnotation_ast_expr))
					cast(ast.Call, cast(ast.Return, cast(ast.FunctionDef, ClassDefMake.body[-1]).body[0]).value).args.append(append2args)

	ClassDefBe.body.sort(key=lambda astFunctionDef: cast(ast.FunctionDef, astFunctionDef).name.lower())
	ClassDefMake.body.sort(key=lambda astFunctionDef: cast(ast.FunctionDef, astFunctionDef).name.lower())

	astTypesModule = ast.Module(
		body=[ast.Expr(ast.Constant(docstringWarning))
			, astImportFromClassNewInPythonVersion
			, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('TypeAlias', 'typing_TypeAlias')], 0)
			, ast.Import([ast.alias('ast')])
			, *handmadeTypeAlias_astTypes
			]
		, type_ignores=[]
		)

	listAttributeIdentifier: list[ast_Identifier] = list(attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier.keys())
	listAttributeIdentifier.sort(key=lambda attributeIdentifier: attributeIdentifier.lower())

	for attributeIdentifier in listAttributeIdentifier:
		hasDOTIdentifier: ast_Identifier = 'hasDOT' + attributeIdentifier
		hasDOTName_Store: ast.Name = ast.Name(hasDOTIdentifier, ast.Store())
		hasDOTName_Load: ast.Name = ast.Name(hasDOTIdentifier, ast.Load())
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

			astAnnAssignValue = dictionaryOf_astDOTclass[listClassDefIdentifier[0]]
			if len(listClassDefIdentifier) > 1:
				for ClassDefIdentifier in listClassDefIdentifier[1:]:
					astAnnAssignValue = ast.BinOp(left=astAnnAssignValue, op=ast.BitOr(), right=dictionaryOf_astDOTclass[ClassDefIdentifier])
			if len(attributeIdentifier2Str4TypeAlias2astAnnotationAndListClassDefIdentifier[attributeIdentifier]) == 1:
				astTypesModule.body.append(ast.AnnAssign(hasDOTName_Store, typing_TypeAliasName, astAnnAssignValue, 1))
			else:
				list_hasDOTNameTypeAliasAnnotations.append(ast.Name(hasDOTIdentifier + '_' + attributeAnnotationAsStr4TypeAliasIdentifier.replace('list', 'list_'), ast.Store()))
				astTypesModule.body.append(ast.AnnAssign(list_hasDOTNameTypeAliasAnnotations[-1], typing_TypeAliasName, astAnnAssignValue, 1))
				ClassDefDOT.body.append(ast.FunctionDef(name=attributeIdentifier
					, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='node', annotation=ast.Name(list_hasDOTNameTypeAliasAnnotations[-1].id, ast.Load()))], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
					, body=[ast.Expr(value=ast.Constant(value=Ellipsis))]
					, decorator_list=[staticmethodName, overloadName]
					, returns=attributeAnnotationAsAST
				))

		ClassDefDOT.body.append(ast.FunctionDef(name=attributeIdentifier
				, args=ast.arguments(posonlyargs=[], args=[ast.arg(arg='node', annotation=hasDOTName_Load)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
				, body=[ast.Return(value=ast.Attribute(value=ast.Name('node', ast.Load()), attr=attributeIdentifier, ctx=ast.Load()))]
				, decorator_list=[staticmethodName]
				, returns=attributeAnnotationUnifiedAsAST
			))

		ClassDefGrab.body.append(ast.FunctionDef(name=attributeIdentifier + 'Attribute'
			, args=ast.arguments(posonlyargs=[]
				, args=[ast.arg('action'
					, annotation=ast.Subscript(ast.Name('Callable', ast.Load())
						, slice=ast.Tuple(elts=[
							ast.List(elts=[attributeAnnotationUnifiedAsAST or ast.Name('Any', ast.Load())], ctx=ast.Load())
							,   attributeAnnotationUnifiedAsAST or ast.Name('Any', ast.Load())]
						, ctx=ast.Load()), ctx=ast.Load()))]
				, vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[])
			, body=[ast.FunctionDef(name='workhorse',
						args=ast.arguments(args=[ast.arg('node', hasDOTName_Load)]),
					body=[ast.Assign(targets=[ast.Attribute(ast.Name('node', ast.Load()), attr=attributeIdentifier, ctx=ast.Store())],
						value=ast.Call(ast.Name('action', ast.Load()), args=[ast.Attribute(ast.Name('node', ast.Load()), attr=attributeIdentifier, ctx=ast.Load())]))
						, ast.Return(ast.Name('node', ast.Load()))],
						returns=hasDOTName_Load),
			ast.Return(ast.Name('workhorse', ctx=ast.Load()))]
			, decorator_list=[staticmethodName], type_comment=None
			, returns=ast.Subscript(ast.Name('Callable', ast.Load()), ast.Tuple([ast.List([hasDOTName_Load], ast.Load()), hasDOTName_Load], ast.Load()), ast.Load())))

		# `astTypesModule`: When one attribute has multiple return types
		if list_hasDOTNameTypeAliasAnnotations:
			astAnnAssignValue = list_hasDOTNameTypeAliasAnnotations[0]
			for index in range(1, len(list_hasDOTNameTypeAliasAnnotations)):
				astAnnAssignValue = ast.BinOp(left=astAnnAssignValue, op=ast.BitOr(), right=list_hasDOTNameTypeAliasAnnotations[index])
			astTypesModule.body.append(ast.AnnAssign(hasDOTName_Store, typing_TypeAliasName, astAnnAssignValue, 1))

	writeModule(astTypesModule, '_astTypes')

	ClassDefBe.body.insert(0, ast.Expr(value=ast.Constant(value=ClassDefDocstringBe)))
	ClassDefDOT.body.insert(0, ast.Expr(value=ast.Constant(value=ClassDefDocstringDOT)))
	ClassDefGrab.body.insert(0, ast.Expr(value=ast.Constant(value=ClassDefDocstringGrab)))
	ClassDefMake.body.insert(0, ast.Expr(value=ast.Constant(value=ClassDefDocstringMake)))

	ClassDefGrab.body.extend(handmadeMethodsGrab)

	writeModule(ast.Module(
		body=[ast.Expr(ast.Constant(docstringWarning))
			, astImportFromClassNewInPythonVersion
			, ast.ImportFrom('typing', [ast.alias('TypeGuard')], 0)
			, ast.Import([ast.alias('ast')])
			, ClassDefBe
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDefBe.name)

	writeModule(ast.Module(
		body=[ast.Expr(ast.Constant(docstringWarning))
			, ast.ImportFrom('collections.abc', [ast.alias('Sequence')], 0)			, ast.ImportFrom('astToolkit._astTypes', [ast.alias('*')], 0)
			, ast.ImportFrom('astToolkit', [ast.alias(identifier) for identifier in ['ast_Identifier', 'ast_expr_Slice', 'astDOTtype_param']], 0)
			, ast.ImportFrom('typing', [ast.alias(identifier) for identifier in ['Any', 'Literal', 'overload']], 0)
			, ast.Import([ast.alias('ast')])
			, ClassDefDOT
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDefDOT.name)

	writeModule(ast.Module(
		body=[ast.Expr(ast.Constant(docstringWarning))
			, ast.ImportFrom('collections.abc', [ast.alias('Callable'), ast.alias('Sequence')], 0)
			, astImportFromClassNewInPythonVersion			, ast.ImportFrom('astToolkit', [ast.alias(identifier) for identifier in ['ast_Identifier', 'ast_expr_Slice', 'NodeORattribute', 'ImaCallToName']], 0)
			, ast.ImportFrom('astToolkit._astTypes', [ast.alias('*')], 0)
			, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('Literal')], 0)
			, ast.Import([ast.alias('ast')])
			, ClassDefGrab
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDefGrab.name)

	writeModule(ast.Module(
		body=[ast.Expr(ast.Constant(docstringWarning))
			, ast.ImportFrom('collections.abc', [ast.alias('Sequence')], 0)
			, astImportFromClassNewInPythonVersion
			, ast.ImportFrom('astToolkit', [ast.alias(identifier) for identifier in ['ast_Identifier', 'ast_expr_Slice', 'intORstr', 'intORstrORtype_params', 'intORtype_params', 'str_nameDOTname']], 0)
			, ast.ImportFrom('typing', [ast.alias('Any'), ast.alias('Literal')], 0)
			, ast.Import([ast.alias('ast')])
			, ClassDefMake
			],
		type_ignores=[]
		)
		, moduleIdentifierPrefix + ClassDefMake.name)
