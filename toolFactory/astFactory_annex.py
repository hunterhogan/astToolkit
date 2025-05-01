from typing import cast
import ast

format_asNameAttribute: str = "astDOT{nameAttribute}"
listHandmadeTypeAlias_astTypes: list[ast.AnnAssign | ast.If] = []
astImportFromClassNewInPythonVersion: ast.ImportFrom = ast.ImportFrom('astToolkit', [], 0)

listStrRepresentationsOfTypeAlias: list[str] = [
	(astTypes_intORstr := "intORstr: typing_TypeAlias = Any"),
	(astTypes_intORstrORtype_params := "intORstrORtype_params: typing_TypeAlias = Any"),
	(astTypes_intORtype_params := "intORtype_params: typing_TypeAlias = Any"),
	(astTypes_yourPythonIsOld := "yourPythonIsOld: typing_TypeAlias = Any"),
]

listPythonVersionNewClass = [(11, ['TryStar']),
	(12, ['ParamSpec', 'type_param', 'TypeAlias', 'TypeVar', 'TypeVarTuple'])
]

for string in listStrRepresentationsOfTypeAlias:
	# The string representation of the type alias is parsed into an AST module.
	astModule = ast.parse(string)
	for node in ast.iter_child_nodes(astModule):
		if isinstance(node, ast.AnnAssign):
			listHandmadeTypeAlias_astTypes.append(node)

for tupleOfClassData in listPythonVersionNewClass:
	pythonVersionMinor: int = tupleOfClassData[0]

	conditionalTypeAlias = ast.If(
		test=ast.Compare(left=ast.Attribute(value=ast.Name('sys', ast.Load()), attr='version_info', ctx=ast.Load()),
						ops=[ast.GtE()],
						comparators=[ast.Tuple([ast.Constant(3), ast.Constant(pythonVersionMinor)], ast.Load())]),
		body=[ast.ImportFrom(module='ast', names=[
			], level=0)],
		orelse=[
				])

	for nameAttribute in tupleOfClassData[1]:
		asNameAttribute = format_asNameAttribute.format(nameAttribute=nameAttribute)
		cast(ast.ImportFrom, conditionalTypeAlias.body[0]).names.append(ast.alias(name=nameAttribute, asname=asNameAttribute))
		conditionalTypeAlias.orelse.append(ast.AnnAssign(target=ast.Name(asNameAttribute, ast.Store()), annotation=ast.Name('typing_TypeAlias', ast.Load()), value=ast.Name('yourPythonIsOld', ast.Load()), simple=1))
		astImportFromClassNewInPythonVersion.names.append(ast.alias(name=asNameAttribute))

	listHandmadeTypeAlias_astTypes.append(conditionalTypeAlias)

Grab_andDoAllOf: str = """@staticmethod
def andDoAllOf(listOfActions: list[Callable[[NodeORattribute], NodeORattribute]]) -> Callable[[NodeORattribute], NodeORattribute]:
	def workhorse(node: NodeORattribute) -> NodeORattribute:
		for action in listOfActions:
			node = action(node)
		return node
	return workhorse
"""

handmadeMethodsGrab: list[ast.FunctionDef] = []
for string in [Grab_andDoAllOf]:
	astModule = ast.parse(string)
	for node in ast.iter_child_nodes(astModule):
		if isinstance(node, ast.FunctionDef):
			handmadeMethodsGrab.append(node)

FunctionDefMake_Attribute: ast.FunctionDef = ast.FunctionDef(
	name='Attribute',
	args=ast.arguments(args=[ast.arg(arg='value', annotation=ast.Attribute(value=ast.Name('ast', ast.Load()), attr='expr', ctx=ast.Load()))], vararg=ast.arg(arg='attribute', annotation=ast.Name('ast_Identifier', ast.Load())), kwonlyargs=[ast.arg(arg='context', annotation=ast.Attribute(value=ast.Name('ast', ast.Load()), attr='expr_context', ctx=ast.Load()))], kw_defaults=[ast.Call(ast.Attribute(value=ast.Name('ast', ast.Load()), attr='Load', ctx=ast.Load()))], kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name('int', ast.Load()))),
	body=[
		ast.Expr(value=ast.Constant(' If two `ast_Identifier` are joined by a dot `.`, they are _usually_ an `ast.Attribute`, but see `ast.ImportFrom`.\n\tParameters:\n\t\tvalue: the part before the dot (e.g., `ast.Name`.)\n\t\tattribute: an `ast_Identifier` after a dot `.`; you can pass multiple `attribute` and they will be chained together.\n\t')),
		ast.FunctionDef(
			name='addDOTattribute',
			args=ast.arguments(args=[ast.arg(arg='chain', annotation=ast.Attribute(value=ast.Name('ast', ast.Load()), attr='expr', ctx=ast.Load())), ast.arg(arg='identifier', annotation=ast.Name('ast_Identifier', ast.Load())), ast.arg(arg='context', annotation=ast.Attribute(value=ast.Name('ast', ast.Load()), attr='expr_context', ctx=ast.Load()))], kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name('int', ast.Load()))),
			body=[ast.Return(value=ast.Call(ast.Attribute(value=ast.Name('ast', ast.Load()), attr='Attribute', ctx=ast.Load()), keywords=[ast.keyword(arg='value', value=ast.Name('chain', ast.Load())), ast.keyword(arg='attr', value=ast.Name('identifier', ast.Load())), ast.keyword(arg='ctx', value=ast.Name('context', ast.Load())), ast.keyword(value=ast.Name('keywordArguments', ast.Load()))]))],
			returns=ast.Attribute(value=ast.Name('ast', ast.Load()), attr='Attribute', ctx=ast.Load())),
		ast.Assign(targets=[ast.Name('buffaloBuffalo', ast.Store())], value=ast.Call(ast.Name('addDOTattribute', ast.Load()), args=[ast.Name('value', ast.Load()), ast.Subscript(value=ast.Name('attribute', ast.Load()), slice=ast.Constant(0), ctx=ast.Load()), ast.Name('context', ast.Load())], keywords=[ast.keyword(value=ast.Name('keywordArguments', ast.Load()))])),
		ast.For(target=ast.Name('identifier', ast.Store()), iter=ast.Subscript(value=ast.Name('attribute', ast.Load()), slice=ast.Slice(lower=ast.Constant(1), upper=ast.Constant(None)), ctx=ast.Load()),
			body=[ast.Assign(targets=[ast.Name('buffaloBuffalo', ast.Store())], value=ast.Call(ast.Name('addDOTattribute', ast.Load()), args=[ast.Name('buffaloBuffalo', ast.Load()), ast.Name('identifier', ast.Load()), ast.Name('context', ast.Load())], keywords=[ast.keyword(value=ast.Name('keywordArguments', ast.Load()))]))]),
		ast.Return(value=ast.Name('buffaloBuffalo', ast.Load()))],
	decorator_list=[ast.Name('staticmethod', ast.Load())],
	returns=ast.Attribute(value=ast.Name('ast', ast.Load()), attr='Attribute', ctx=ast.Load()))

MakeImportFunctionDef: ast.FunctionDef = ast.FunctionDef(name='Import', args=ast.arguments(args=[ast.arg(arg='moduleWithLogicalPath', annotation=ast.Name('str_nameDOTname', ast.Load())), ast.arg(arg='asName', annotation=ast.BinOp(left=ast.Name('ast_Identifier', ast.Load()), op=ast.BitOr(), right=ast.Constant(None)))], kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name('int', ast.Load())), defaults=[ast.Constant(None)]), body=[ast.Return(value=ast.Call(ast.Attribute(value=ast.Name('ast', ast.Load()), attr='Import', ctx=ast.Load()), keywords=[ast.keyword(arg='names', value=ast.List(elts=[ast.Call(ast.Attribute(value=ast.Name('Make', ast.Load()), attr='alias', ctx=ast.Load()), args=[ast.Name('moduleWithLogicalPath', ast.Load()), ast.Name('asName', ast.Load())])], ctx=ast.Load())), ast.keyword(value=ast.Name('keywordArguments', ast.Load()))]))], decorator_list=[ast.Name('staticmethod', ast.Load())], returns=ast.Attribute(value=ast.Name('ast', ast.Load()), attr='Import', ctx=ast.Load()))

listPylanceErrors: list[str] = ['annotation', 'arg', 'args', 'body', 'keys', 'name', 'names', 'op', 'orelse', 'pattern', 'returns', 'target', 'value',]

# ww='''
# if sys.version_info >= (3, 11):
# 	from ast import TryStar as astDOTTryStar
# else:
# 	astDOTTryStar: typing_TypeAlias = yourPythonIsOld
# '''

# print(ast.dump(ast.parse(ww, type_comments=True), indent=4))
# from ast import *
