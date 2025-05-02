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
	args=ast.arguments(args=[ast.arg(arg='value', annotation=ast.Attribute(value=ast.Name('ast'), attr='expr'))], vararg=ast.arg(arg='attribute', annotation=ast.Name('ast_Identifier')), kwonlyargs=[ast.arg(arg='context', annotation=ast.Attribute(value=ast.Name('ast'), attr='expr_context'))], kw_defaults=[ast.Call(ast.Attribute(value=ast.Name('ast'), attr='Load'))], kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name('int'))),
	body=[
		ast.Expr(value=ast.Constant(' If two `ast_Identifier` are joined by a dot `.`, they are _usually_ an `ast.Attribute`, but see `ast.ImportFrom`.\n\tParameters:\n\t\tvalue: the part before the dot (e.g., `ast.Name`.)\n\t\tattribute: an `ast_Identifier` after a dot `.`; you can pass multiple `attribute` and they will be chained together.\n\t')),
		ast.FunctionDef(
			name='addDOTattribute',
			args=ast.arguments(args=[ast.arg(arg='chain', annotation=ast.Attribute(value=ast.Name('ast'), attr='expr')), ast.arg(arg='identifier', annotation=ast.Name('ast_Identifier')), ast.arg(arg='context', annotation=ast.Attribute(value=ast.Name('ast'), attr='expr_context'))], kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name('int'))),
			body=[ast.Return(value=ast.Call(ast.Attribute(value=ast.Name('ast'), attr='Attribute'), keywords=[ast.keyword(arg='value', value=ast.Name('chain')), ast.keyword(arg='attr', value=ast.Name('identifier')), ast.keyword(arg='ctx', value=ast.Name('context')), ast.keyword(value=ast.Name('keywordArguments'))]))],
			returns=ast.Attribute(value=ast.Name('ast'), attr='Attribute')),
		ast.Assign(targets=[ast.Name('buffaloBuffalo', ast.Store())], value=ast.Call(ast.Name('addDOTattribute'), args=[ast.Name('value'), ast.Subscript(value=ast.Name('attribute'), slice=ast.Constant(0)), ast.Name('context')], keywords=[ast.keyword(value=ast.Name('keywordArguments'))])),
		ast.For(target=ast.Name('identifier', ast.Store()), iter=ast.Subscript(value=ast.Name('attribute'), slice=ast.Slice(lower=ast.Constant(1), upper=ast.Constant(None))),
			body=[ast.Assign(targets=[ast.Name('buffaloBuffalo', ast.Store())], value=ast.Call(ast.Name('addDOTattribute'), args=[ast.Name('buffaloBuffalo'), ast.Name('identifier'), ast.Name('context')], keywords=[ast.keyword(value=ast.Name('keywordArguments'))]))]),
		ast.Return(value=ast.Name('buffaloBuffalo'))],
	decorator_list=[ast.Name('staticmethod')],
	returns=ast.Attribute(value=ast.Name('ast'), attr='Attribute'))

MakeImportFunctionDef: ast.FunctionDef = ast.FunctionDef(name='Import', args=ast.arguments(args=[ast.arg(arg='moduleWithLogicalPath', annotation=ast.Name('str_nameDOTname')), ast.arg(arg='asName', annotation=ast.BinOp(left=ast.Name('ast_Identifier'), op=ast.BitOr(), right=ast.Constant(None)))], kwarg=ast.arg(arg='keywordArguments', annotation=ast.Name('int')), defaults=[ast.Constant(None)]), body=[ast.Return(value=ast.Call(ast.Attribute(value=ast.Name('ast'), attr='Import'), keywords=[ast.keyword(arg='names', value=ast.List(elts=[ast.Call(ast.Attribute(value=ast.Name('Make'), attr='alias'), args=[ast.Name('moduleWithLogicalPath'), ast.Name('asName')])])), ast.keyword(value=ast.Name('keywordArguments'))]))], decorator_list=[ast.Name('staticmethod')], returns=ast.Attribute(value=ast.Name('ast'), attr='Import'))

listPylanceErrors: list[str] = ['annotation', 'arg', 'args', 'body', 'keys', 'name', 'names', 'op', 'orelse', 'pattern', 'returns', 'target', 'value',]

# ww='''
# TypeGuard[ast.AnnAssign] | bool
# '''

# print(ast.dump(ast.parse(ww, type_comments=True), indent=4))
# from ast import *
